Create a professional infographic following these specifications:

## Image Specifications

- **Type**: Infographic
- **Layout**: linear-progression
- **Language**: en

## Core Principles

- Follow the layout structure precisely for information architecture
- Apply style aesthetics consistently throughout
- Keep information concise, highlight keywords and core concepts
- Use ample whitespace for visual clarity
- Maintain clear visual hierarchy
- ONLY include text that is explicitly provided. Do NOT hallucinate or invent any statistics, timings, numbers, or data.

## Text Requirements

- All text must match the specified style treatment
- Main titles should be prominent and readable
- Key concepts should be visually emphasized
- Labels should be clear and appropriately sized
- Use English for all text content

## Layout Guidelines

Sequential progression showing a 4-stage data pipeline flowing left to right.

- Linear horizontal arrangement with 4 main nodes
- Connecting lines/arrows between each stage showing data flow direction
- Clear start (YouTube) and end (Response) points
- Directional flow indicators between stages
- Each node is a distinct pipeline stage with an icon and description
- Numbered steps at each node

## Style Guidelines

- **Style**: technical-schematic
Technical diagram with engineering precision and clean geometry. Blueprint aesthetic with deep blue background, subtle grid pattern, white and cyan lines, amber accent highlights. Clean sans-serif typography, all-caps labels, geometric precision.

---

Generate the infographic based on the content below:

## How YouTube RAG Search Works

4-stage pipeline: YouTube transcripts → vector search → AI answers.

IMPORTANT RULES:
- ONLY use text provided in this prompt. Do NOT invent statistics, timings, percentages, or any data not listed below.
- Do NOT render any hex colour codes as visible text.
- NO text outside or below the boxes. Only the title at the top and the 4 boxes connected by arrows.
- Keep it clean and minimal.

LAYOUT RULES:
- 4 boxes in a row connected by arrows
- Each box has: a number, a title, an icon, and 2 short subtitle labels INSIDE the box

### Stage 1: FETCH
Icon: download arrow. Subtitles inside box: "yt-dlp" and "Markdown"

### Stage 2: INGEST
Icon: database. Subtitles inside box: "Embeddings" and "LanceDB"

### Stage 3: QUERY
Icon: magnifying glass. Subtitles inside box: "Vector search" and "Time decay"

### Stage 4: RESPOND
Icon: chat bubble. Subtitles inside box: "Claude" and "Quotes + URL"
