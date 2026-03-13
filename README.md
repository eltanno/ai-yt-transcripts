# AI YouTube Transcripts RAG

Semantic search over YouTube transcript archives using LanceDB and OpenAI embeddings.

## Prerequisites

- Python 3.10+
- OpenAI API key

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Configure your API key
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

## Usage

### Ingest transcripts

Parse all markdown files in `transcripts/`, chunk them, generate embeddings, and store in LanceDB:

```bash
python -m src.ingest
```

Re-running ingestion replaces existing data (idempotent).

### Query

Single query:

```bash
python -m src.query "what did Nate say about vibe coding?"
```

Interactive mode (REPL):

```bash
python -m src.query
```

Options:

```
--limit, -k       Number of results (default: 5)
--date-from       Filter from date (YYYY-MM-DD)
--date-to         Filter to date (YYYY-MM-DD)
```

Examples:

```bash
python -m src.query "Claude vs ChatGPT strategy" --limit 10
python -m src.query "hiring and AI" --date-from 2026-02-01
python -m src.query "prompt engineering" --date-from 2026-02-01 --date-to 2026-03-01
```

## Adding new transcripts

1. Add `.md` files to `transcripts/` following the existing format:
   ```markdown
   # Video Title

   - **Channel:** Channel Name
   - **Date:** YYYY-MM-DD
   - **Duration:** XX min
   - **Views:** XXK
   - **URL:** https://youtube.com/watch?v=...

   ## Transcript

   Full transcript text here...
   ```
2. Re-run ingestion: `python -m src.ingest`

## Architecture

- **Embeddings:** OpenAI `text-embedding-3-large` at 1536 dimensions (Matryoshka)
- **Vector DB:** LanceDB (local, no server needed)
- **Chunking:** ~500 tokens with ~100 token overlap, using tiktoken
- **No frameworks:** Direct OpenAI SDK + LanceDB, no LangChain/LlamaIndex
