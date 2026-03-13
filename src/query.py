"""Query the YouTube transcript RAG database."""

import argparse
import sys

import lancedb
from openai import OpenAI
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from src.config import (
    OPENAI_API_KEY,
    EMBEDDING_MODEL,
    EMBEDDING_DIMS,
    DB_PATH,
    TABLE_NAME,
    DEFAULT_TOP_K,
)

console = Console()


def get_query_embedding(client: OpenAI, text: str) -> list[float]:
    """Embed the query text."""
    response = client.embeddings.create(
        input=[text],
        model=EMBEDDING_MODEL,
        dimensions=EMBEDDING_DIMS,
    )
    return response.data[0].embedding


def search(
    table,
    client: OpenAI,
    query: str,
    limit: int = DEFAULT_TOP_K,
    date_from: str | None = None,
    date_to: str | None = None,
) -> list[dict]:
    """Search the transcript database using vector similarity."""
    query_vector = get_query_embedding(client, query)

    search_builder = table.search(query_vector).limit(limit)

    # Apply date filters if provided
    if date_from and date_to:
        search_builder = search_builder.where(
            f"date >= '{date_from}' AND date <= '{date_to}'"
        )
    elif date_from:
        search_builder = search_builder.where(f"date >= '{date_from}'")
    elif date_to:
        search_builder = search_builder.where(f"date <= '{date_to}'")

    results = search_builder.to_list()
    return results


def display_results(results: list[dict], query: str):
    """Display search results in a readable format."""
    if not results:
        console.print("[yellow]No results found.[/yellow]")
        return

    console.print()
    console.print(f"[bold]Results for:[/bold] \"{query}\"")
    console.print(f"[dim]Found {len(results)} matching chunks[/dim]")
    console.print()

    for i, result in enumerate(results, 1):
        # LanceDB returns _distance (lower = more similar)
        distance = result.get("_distance", 0)
        # Convert distance to a similarity score (1 / (1 + distance))
        similarity = 1 / (1 + distance)

        title = result.get("title", "Unknown")
        date = result.get("date", "")
        url = result.get("url", "")
        chunk_idx = result.get("chunk_index", 0)
        total_chunks = result.get("total_chunks", 0)
        text = result.get("text", "")

        # Truncate text for display (show first ~300 chars)
        display_text = text[:500] + "..." if len(text) > 500 else text

        header = f"[bold]#{i}[/bold] {title}"
        if date:
            header += f" [dim]({date})[/dim]"

        meta_parts = []
        if url:
            meta_parts.append(f"[link={url}]{url}[/link]")
        meta_parts.append(f"Chunk {chunk_idx + 1}/{total_chunks}")
        meta_parts.append(f"Similarity: {similarity:.3f}")

        panel_content = "\n".join(meta_parts) + "\n\n" + display_text

        console.print(Panel(
            panel_content,
            title=header,
            title_align="left",
            border_style="blue" if i == 1 else "dim",
            padding=(1, 2),
        ))


def interactive_mode(table, client: OpenAI, limit: int, date_from: str | None, date_to: str | None):
    """Run an interactive query REPL."""
    console.print("[bold blue]YouTube Transcript Search[/bold blue]")
    console.print("[dim]Type your query and press Enter. Type 'quit' or Ctrl+C to exit.[/dim]")
    console.print()

    while True:
        try:
            query = console.input("[bold green]> [/bold green]").strip()
            if not query:
                continue
            if query.lower() in ("quit", "exit", "q"):
                break

            results = search(table, client, query, limit=limit, date_from=date_from, date_to=date_to)
            display_results(results, query)
            console.print()

        except KeyboardInterrupt:
            console.print("\n[dim]Goodbye.[/dim]")
            break
        except EOFError:
            break


def main():
    """Main entry point for the query CLI."""
    parser = argparse.ArgumentParser(
        description="Search YouTube transcripts using semantic similarity",
        prog="python -m src.query",
    )
    parser.add_argument(
        "query",
        nargs="?",
        default=None,
        help="Search query (omit for interactive mode)",
    )
    parser.add_argument(
        "--limit", "-k",
        type=int,
        default=DEFAULT_TOP_K,
        help=f"Number of results to return (default: {DEFAULT_TOP_K})",
    )
    parser.add_argument(
        "--date-from",
        type=str,
        default=None,
        help="Filter results from this date (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--date-to",
        type=str,
        default=None,
        help="Filter results up to this date (YYYY-MM-DD)",
    )

    args = parser.parse_args()

    if not OPENAI_API_KEY:
        console.print("[red]Error: OPENAI_API_KEY not set. Check your .env file.[/red]")
        sys.exit(1)

    # Connect to LanceDB
    try:
        db = lancedb.connect(DB_PATH)
        table = db.open_table(TABLE_NAME)
    except Exception as e:
        console.print(f"[red]Error opening database: {e}[/red]")
        console.print("[yellow]Have you run the ingestion script? python -m src.ingest[/yellow]")
        sys.exit(1)

    client = OpenAI(api_key=OPENAI_API_KEY)

    if args.query:
        # Single query mode
        results = search(table, client, args.query, limit=args.limit, date_from=args.date_from, date_to=args.date_to)
        display_results(results, args.query)
    else:
        # Interactive mode
        interactive_mode(table, client, limit=args.limit, date_from=args.date_from, date_to=args.date_to)


if __name__ == "__main__":
    main()
