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
--no-decay        Disable time decay (show raw similarity scores)
```

By default, results are scored with exponential time decay (60-day half-life) so newer videos rank higher. Use `--no-decay` for raw similarity ranking.

Examples:

```bash
python -m src.query "Claude vs ChatGPT strategy" --limit 10
python -m src.query "hiring and AI" --date-from 2026-02-01
python -m src.query "prompt engineering" --date-from 2026-02-01 --date-to 2026-03-01
```

## Adding new transcripts

### Automated: Fetch from YouTube channel

```bash
# Fetch latest videos not already in transcripts/
python -m src.fetch --channel @NateBJones

# Fetch specific video by URL
python -m src.fetch --url "https://www.youtube.com/watch?v=VIDEO_ID"

# Fetch and immediately re-ingest
python -m src.fetch --channel @NateBJones && python -m src.ingest
```

### Daily cron

A script at `scripts/daily-fetch.sh` handles the full pipeline: fetch new videos, re-ingest into LanceDB, commit, and push. It skips everything if there's nothing new.

```bash
# Add to your crontab (runs daily at 9:17 AM)
crontab -e

# Add this line:
17 9 * * * cd /path/to/ai-yt-transcripts && bash scripts/daily-fetch.sh >> /tmp/yt-fetch.log 2>&1
```

### Manual

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

## How the transcripts were collected

The initial corpus was scraped from [@NateBJones](https://www.youtube.com/@NateBJones) (Jan 12 - Mar 12, 2026) using this workflow:

1. **Browse channel** — Playwright browser automation navigated to the channel's `/videos` page and scrolled to load all recent uploads
2. **Extract video metadata** — Titles, video IDs, view counts, and relative dates were parsed from the page snapshot
3. **Fetch transcripts** — `youtube-transcript-api` Python library pulled auto-generated captions for each video. When rate-limited, `yt-dlp` was used as a fallback to download VTT/json3 subtitle files
4. **Generate markdown** — Each video was written as a markdown file (`YYYY-MM-DD-kebab-title.md`) with metadata header and full transcript text formatted into flowing paragraphs

The `src/fetch.py` script automates steps 2-4 for ongoing updates.

## Architecture

- **Embeddings:** OpenAI `text-embedding-3-large` at 1536 dimensions (Matryoshka)
- **Vector DB:** LanceDB (local, no server needed)
- **Chunking:** ~500 tokens with ~100 token overlap, using tiktoken
- **No frameworks:** Direct OpenAI SDK + LanceDB, no LangChain/LlamaIndex
