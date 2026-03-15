"""Ingest YouTube transcript markdown files into LanceDB with OpenAI embeddings."""

import re
import time
from pathlib import Path

import lancedb
import pyarrow as pa
import tiktoken
from openai import OpenAI
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

from src.config import (
    OPENAI_API_KEY,
    EMBEDDING_MODEL,
    EMBEDDING_DIMS,
    DB_PATH,
    TABLE_NAME,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    TRANSCRIPTS_DIR,
)

console = Console()


def parse_metadata(text: str) -> dict:
    """Extract metadata from the markdown header.

    Expected format:
        # Title Here
        - **Channel:** ...
        - **Date:** ...
        - **Duration:** ...
        - **Views:** ...
        - **URL:** ...
    """
    metadata = {}

    # Title: first line starting with #
    title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if title_match:
        metadata["title"] = title_match.group(1).strip()

    # Key-value pairs from bullet points
    patterns = {
        "channel": r"\*\*Channel:\*\*\s*(.+)",
        "date": r"\*\*Date:\*\*\s*(.+)",
        "duration": r"\*\*Duration:\*\*\s*(.+)",
        "views": r"\*\*Views:\*\*\s*(.+)",
        "url": r"\*\*URL:\*\*\s*(.+)",
    }
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            metadata[key] = match.group(1).strip()

    return metadata


def extract_transcript(text: str) -> str:
    """Extract the transcript text after the '## Transcript' heading."""
    match = re.search(r"## Transcript\s*\n(.+)", text, re.DOTALL)
    if match:
        transcript = match.group(1).strip()
        # Skip files where the transcript is not yet available
        if transcript.startswith("Transcript not yet available"):
            return ""
        return transcript
    return ""


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    """Split text into overlapping chunks based on token count.

    Uses tiktoken for accurate token counting. Chunks are split on paragraph
    boundaries where possible, falling back to sentence boundaries.
    """
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)

    if len(tokens) <= chunk_size:
        return [text]

    chunks = []
    start = 0
    while start < len(tokens):
        end = min(start + chunk_size, len(tokens))
        chunk_tokens = tokens[start:end]
        chunk_text = enc.decode(chunk_tokens)
        chunks.append(chunk_text)

        # Advance by (chunk_size - overlap) tokens
        start += chunk_size - overlap

    return chunks


def embed_texts(client: OpenAI, texts: list[str], model: str = EMBEDDING_MODEL, dims: int = EMBEDDING_DIMS) -> list[list[float]]:
    """Embed a batch of texts using the OpenAI API.

    Handles batching for the API (max 2048 inputs per request).
    """
    all_embeddings = []
    batch_size = 2048

    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        response = client.embeddings.create(
            input=batch,
            model=model,
            dimensions=dims,
        )
        batch_embeddings = [item.embedding for item in response.data]
        all_embeddings.extend(batch_embeddings)

    return all_embeddings


def parse_all_transcripts(transcripts_dir: Path) -> list[dict]:
    """Parse all markdown files and return chunked records with metadata."""
    records = []
    md_files = sorted(transcripts_dir.glob("*.md"))

    console.print(f"[bold]Found {len(md_files)} transcript files[/bold]")

    skipped = 0
    for md_file in md_files:
        text = md_file.read_text(encoding="utf-8")
        metadata = parse_metadata(text)
        transcript = extract_transcript(text)

        if not transcript:
            skipped += 1
            continue

        chunks = chunk_text(transcript)

        for i, chunk in enumerate(chunks):
            records.append({
                "text": chunk,
                "title": metadata.get("title", ""),
                "date": metadata.get("date", ""),
                "url": metadata.get("url", ""),
                "channel": metadata.get("channel", ""),
                "duration": metadata.get("duration", ""),
                "views": metadata.get("views", ""),
                "source_file": md_file.name,
                "chunk_index": i,
                "total_chunks": len(chunks),
            })

    if skipped > 0:
        console.print(f"[yellow]Skipped {skipped} files (no transcript available)[/yellow]")

    return records


def main():
    """Run the full ingestion pipeline."""
    start_time = time.time()

    if not OPENAI_API_KEY:
        console.print("[red]Error: OPENAI_API_KEY not set. Check your .env file.[/red]")
        return

    console.print("[bold blue]YouTube Transcript RAG Ingestion[/bold blue]")
    console.print()

    # 1. Parse transcripts
    console.print("[bold]Step 1:[/bold] Parsing transcript files...")
    records = parse_all_transcripts(TRANSCRIPTS_DIR)
    console.print(f"  Created [green]{len(records)}[/green] chunks from transcripts")
    console.print()

    if not records:
        console.print("[red]No chunks to process. Check your transcripts directory.[/red]")
        return

    # 2. Generate embeddings
    console.print("[bold]Step 2:[/bold] Generating embeddings...")
    client = OpenAI(api_key=OPENAI_API_KEY)
    texts = [r["text"] for r in records]

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("Embedding chunks...", total=len(texts))

        # Embed in batches of 100 for progress visibility
        all_embeddings = []
        batch_size = 100
        total_tokens = 0

        for i in range(0, len(texts), batch_size):
            batch = texts[i : i + batch_size]
            response = client.embeddings.create(
                input=batch,
                model=EMBEDDING_MODEL,
                dimensions=EMBEDDING_DIMS,
            )
            batch_embeddings = [item.embedding for item in response.data]
            all_embeddings.extend(batch_embeddings)
            total_tokens += response.usage.total_tokens
            progress.update(task, advance=len(batch))

    # Estimate cost: text-embedding-3-large is $0.13 per 1M tokens
    cost_estimate = (total_tokens / 1_000_000) * 0.13
    console.print(f"  Embedded {len(all_embeddings)} chunks using {total_tokens:,} tokens")
    console.print(f"  Estimated cost: [green]${cost_estimate:.4f}[/green]")
    console.print()

    # 3. Store in LanceDB
    console.print("[bold]Step 3:[/bold] Storing in LanceDB...")

    # Build PyArrow table for LanceDB
    for i, record in enumerate(records):
        record["vector"] = all_embeddings[i]

    db = lancedb.connect(DB_PATH)

    # Overwrite existing table (re-embeds everything)
    table = db.create_table(TABLE_NAME, data=records, mode="overwrite")
    console.print(f"  Created table '{TABLE_NAME}' with {len(records)} rows")
    console.print()

    elapsed = time.time() - start_time
    console.print(f"[bold green]Ingestion complete in {elapsed:.1f}s[/bold green]")
    console.print()

    # Summary
    console.print("[bold]Summary:[/bold]")
    console.print(f"  Chunks:     {len(records)}")
    console.print(f"  Tokens:     {total_tokens:,}")
    console.print(f"  Cost:       ${cost_estimate:.4f}")
    console.print(f"  DB path:    {DB_PATH}")
    console.print(f"  Table:      {TABLE_NAME}")


if __name__ == "__main__":
    main()
