#!/bin/bash
SKILL_DIR="/home/jim/workspace/ai-yt-transcripts/.agents/skills/baoyu-imagine"
PROMPT_DIR="/home/jim/workspace/ai-yt-transcripts/infographic/5-levels-ai-coding/prompts"
OUT_DIR="/home/jim/workspace/ai-yt-transcripts/infographic/5-levels-ai-coding"

CONTENT='## The 5 Levels of AI Coding

IMPORTANT RULES:
- ONLY use text provided below. Do NOT invent statistics, timings, percentages, or any data not listed.
- Do NOT render any hex colour codes as visible text.
- Keep it clean and minimal. Short labels only.

LAYOUT: Pyramid with 5 tiers. Level 1 at the bottom (widest), Level 5 at the top (narrowest). Each tier has a level number, a title, and a short subtitle.

### Level 5 (top): SOFTWARE FACTORY
Subtitle: "Fully autonomous"

### Level 4: STRONG DM
Subtitle: "Human sets intent, AI executes"

### Level 3: DEVELOPER AS MANAGER
Subtitle: "Direct AI, review output"

### Level 2: AI PAIR PROGRAMMER
Subtitle: "90% think they are here"

### Level 1 (bottom): AUTOCOMPLETE
Subtitle: "Tab-complete suggestions"'

COMMON='Create a professional infographic following these specifications:

## Image Specifications
- **Type**: Infographic
- **Layout**: hierarchical-layers (pyramid)
- **Language**: en

## Core Principles
- ONLY include text explicitly provided. Do NOT hallucinate or invent any data.
- Keep information concise — short labels only, no sentences.
- Clear visual hierarchy with Level 5 at the top and Level 1 at the bottom.

## Layout Guidelines
Pyramid / triangle structure with 5 horizontal tiers stacked vertically.
- Level 5 at the TOP (narrowest tier)
- Level 1 at the BOTTOM (widest tier)
- Each tier clearly labelled with level number, title, and short subtitle
- Visual progression from bottom to top suggesting increasing sophistication'

declare -A STYLES

STYLES[bold-graphic]="High-contrast comic/pop-art style with heavy black outlines and dramatic halftone dots. Bold primary colours, energetic composition, punchy and attention-grabbing. Comic-book typography."

STYLES[chalkboard]="Hand-drawn chalk lettering and sketchy illustrations on a dark chalkboard. Coloured chalk accents in yellow, pink, blue, and green. Informal educational feel, hand-drawn arrows and boxes."

STYLES[corporate-memphis]="Flat vector illustrations with vibrant colours. White or light pastel background, bold purple, orange, teal, and yellow. Simple geometric shapes, clean modern typography, friendly and approachable tech feel."

STYLES[ikea-manual]="Minimal wordless line-art instruction style. Black lines on white/cream background, red for warnings, blue for highlights. Numbered steps with arrows, ultra-clean and uncluttered. Simple iconic illustrations."

for style in "${!STYLES[@]}"; do
    cat > "$PROMPT_DIR/$style.md" << PROMPT
$COMMON

## Style Guidelines
- **Style**: $style
${STYLES[$style]}

---

Generate the infographic based on the content below:

$CONTENT
PROMPT
    echo "Created: $style.md"
done

echo ""
echo "Generating 4 images in parallel..."

for style in "${!STYLES[@]}"; do
    echo "Starting: $style"
    bun "$SKILL_DIR/scripts/main.ts" \
        --promptfiles "$PROMPT_DIR/$style.md" \
        --image "$OUT_DIR/style-$style.png" \
        --ar 16:9 --quality 2k \
        --provider google --model gemini-3.1-flash-image-preview \
        2>&1 &
done

wait
echo "All done!"
