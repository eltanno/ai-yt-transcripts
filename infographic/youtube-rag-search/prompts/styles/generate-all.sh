#!/bin/bash
# Generate infographic in 8 different styles
# Uses the same content, different style guidelines

BASE_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
SKILL_DIR="$(cd "$(dirname "$0")/../../../../.agents/skills/baoyu-imagine" && pwd)"
PROMPT_DIR="$(dirname "$0")"
OUT_DIR="$BASE_DIR"

CONTENT='## How YouTube RAG Search Works

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
Icon: chat bubble. Subtitles inside box: "Claude" and "Quotes + URL"'

COMMON_HEADER='Create a professional infographic following these specifications:

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
- Numbered steps at each node'

declare -A STYLES

STYLES[technical-schematic]="Technical diagram with engineering precision and clean geometry. Blueprint aesthetic with deep blue background, subtle grid pattern, white and cyan lines, amber accent highlights. Clean sans-serif typography, all-caps labels, geometric precision."

STYLES[subway-map]="Transit diagram style with coloured route lines at strict 45/90-degree angles and station markers. White or light gray background, bold transit colours (red, blue, green, yellow). Station dots at each stage, clean route lines connecting them."

STYLES[corporate-memphis]="Flat vector illustrations with vibrant colours. White or light pastel background, bold purple, orange, teal, and yellow. Simple geometric shapes, clean modern typography, friendly and approachable tech feel."

STYLES[bold-graphic]="High-contrast comic/pop-art style with heavy black outlines and dramatic halftone dots. Bold primary colours, energetic composition, punchy and attention-grabbing. Comic-book typography."

STYLES[pop-laboratory]="Lab manual precision meets pop-art colour on a blueprint grid. Light grayish-white grid background, muted teal, fluorescent pink, and lemon yellow highlights. Coordinate markers, precise technical feel with personality."

STYLES[ikea-manual]="Minimal wordless line-art instruction style. Black lines on white/cream background, red for warnings, blue for highlights. Numbered steps with arrows, ultra-clean and uncluttered. Simple iconic illustrations."

STYLES[chalkboard]="Hand-drawn chalk lettering and sketchy illustrations on a dark chalkboard. Coloured chalk accents in yellow, pink, blue, and green. Informal educational feel, hand-drawn arrows and boxes."

STYLES[cyberpunk-neon]="Glowing neon outlines on deep dark background. Neon pink, cyan, and electric blue glow effects. Futuristic digital aesthetic, dark purple/black background, high-tech feel."

for style in "${!STYLES[@]}"; do
    prompt_file="$PROMPT_DIR/$style.md"
    cat > "$prompt_file" << PROMPT
$COMMON_HEADER

## Style Guidelines

- **Style**: $style
${STYLES[$style]}

---

Generate the infographic based on the content below:

$CONTENT
PROMPT
    echo "Created prompt: $style.md"
done

echo ""
echo "All prompt files created. Now generating images..."
echo ""

for style in "${!STYLES[@]}"; do
    echo "Generating: $style..."
    bun "$SKILL_DIR/scripts/main.ts" \
        --promptfiles "$PROMPT_DIR/$style.md" \
        --image "$OUT_DIR/style-$style.png" \
        --ar 16:9 --quality 2k \
        --provider google --model gemini-3.1-flash-image-preview \
        2>&1 &
done

echo "All 8 generations launched in parallel. Waiting..."
wait
echo "Done! All images generated."
