# Structured Content: How YouTube RAG Search Works

## Title
How YouTube RAG Search Works

## Learning Objectives
- Understand the end-to-end pipeline from YouTube video to searchable knowledge
- See how embeddings and vector search enable semantic matching
- Know the role of each component in the system

## Sections

### Section 1: Fetch
- **Key Concept:** Automated transcript collection from YouTube
- **Content:** yt-dlp downloads transcripts from tracked YouTube channels in batches of 50 videos. Date-windowed pagination handles channels with >50 videos. A daily cron job automates this.
- **Visual Element:** YouTube icon → yt-dlp → Markdown files
- **Labels:** "yt-dlp", "50 videos/batch", "daily-fetch.sh cron", "transcripts/*.md"

### Section 2: Ingest
- **Key Concept:** Converting text to searchable vectors
- **Content:** Transcripts are chunked by token count with overlap. Each chunk is sent to OpenAI text-embedding-3-large, producing 1536-dimensional vectors. These are stored in a local LanceDB database.
- **Visual Element:** Markdown file → chunking → embedding model → vector DB
- **Labels:** "text-embedding-3-large", "1536 dimensions", "LanceDB", "chunk + overlap"

### Section 3: Query
- **Key Concept:** Semantic similarity search with time decay
- **Content:** User's search query is embedded using the same model. LanceDB finds the most similar transcript chunks via vector distance. An exponential time-decay function boosts recent content: score = similarity × max(floor, 0.5^(age/half_life)).
- **Visual Element:** Search box → embedding → vector comparison → ranked results
- **Labels:** "semantic search", "cosine similarity", "time decay scoring", "top-K results"

### Section 4: Respond
- **Key Concept:** AI-powered summarisation of results
- **Content:** Claude (Sonnet for routine, Opus for complex analysis) receives the top matching chunks and summarises them with video title, date, YouTube URL, and relevant quotes from the transcript.
- **Visual Element:** Ranked chunks → Claude → formatted response
- **Labels:** "Claude Sonnet/Opus", "title + date + URL + quotes"

## Data Points
- Embedding model: text-embedding-3-large
- Vector dimensions: 1536
- Vector DB: LanceDB (local)
- Fetch batch size: 50 videos
- Scoring: similarity × time decay
- Automation: daily cron
