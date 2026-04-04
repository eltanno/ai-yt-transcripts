# Analysis: How YouTube RAG Search Works

## Topic
End-to-end pipeline for semantic search over YouTube video transcripts using Retrieval-Augmented Generation (RAG).

## Data Type
Technical system architecture — pipeline/workflow with distinct stages.

## Complexity
Medium — 4 main stages (Fetch → Ingest → Query → Respond), each with clear sub-steps.

## Tone
Technical/educational — explaining a real working system.

## Audience
Technical users interested in RAG pipelines, AI tooling, or building similar systems.

## Key Components
1. **YouTube Channels** — Source data (tracked channels like @NateBJones, @garyseconomics)
2. **yt-dlp** — Fetches transcripts, paginated in batches of 50
3. **Markdown Files** — Raw transcript storage in `transcripts/` directory
4. **OpenAI text-embedding-3-large** — Converts transcript chunks into 1536-dim vectors
5. **LanceDB** — Local vector database storing embeddings
6. **Semantic Query** — User search terms → embedding → vector similarity search
7. **Time Decay** — Exponential decay scoring: `similarity * max(floor, 0.5^(age/half_life))`
8. **Claude (Sonnet/Opus)** — Summarizes results with video title, date, URL, and quotes
9. **Daily Cron** — Automated fetch + ingest + git commit via `daily-fetch.sh`

## Design Instructions
Show the flow from YouTube → local storage → vector DB → user query → response. Emphasize the pipeline nature — data flows left to right (or top to bottom).
