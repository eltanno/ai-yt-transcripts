# Infographic Pipeline

Generate infographics from text prompts using Claude Code + Google's Nano Banana 2 image model.

## How It Works

Two skills work together:

1. **baoyu-infographic** — Analyses your content, structures it for visual layout, recommends a layout + style combination, and builds the image generation prompt.
2. **baoyu-imagine** — Takes the prompt and calls the image generation API (Google Gemini / Nano Banana 2). Returns a PNG.

The pipeline is: **Content → Structured prompt → Nano Banana 2 → PNG**

## Why Nano Banana 2

We tested GPT-image-1.5 (OpenAI) first — it misspells text constantly ("Voutube", "Mamdown", "Emteddings"). Nano Banana 2 (Google's Gemini image model) renders text accurately and is cheap (~$0.04-0.07 per image).

We also tested generating infographics as HTML + Playwright screenshots. Text was perfect but the output looked like a dashboard, not an infographic. AI image models produce much better visual design.

## Skills

Both skills are installed via the [skills.sh](https://skills.sh) CLI (Vercel-backed, security-audited):

```bash
npx skills add jimliu/baoyu-skills --skill baoyu-infographic --skill baoyu-imagine
```

This installs to `.agents/skills/` with symlinks in `.claude/skills/`.

### baoyu-infographic

- **Source:** jimliu/baoyu-skills
- **Audit:** Gen: Safe, Socket: 0 alerts, Snyk: Low Risk
- **What it does:** Content analysis, 21 layout types (linear-progression, pyramid, bento-grid, etc.), 20 visual styles (chalkboard, bold-graphic, corporate-memphis, etc.), structured prompt generation
- **Files:** SKILL.md + 41 reference files (layouts, styles, templates)

### baoyu-imagine

- **Source:** jimliu/baoyu-skills
- **Audit:** Gen: Safe, Socket: 0 alerts, Snyk: Low Risk
- **What it does:** Calls image generation APIs. Supports Google, OpenAI, Azure OpenAI, Replicate, and 5 others.
- **Files:** SKILL.md + TypeScript scripts with provider implementations
- **Runtime:** Requires `bun` or `npx`

## Styles We Tested

From 20 available styles, these worked best for tech content:

| Style | Description | Best for |
|-------|-------------|----------|
| **chalkboard** | Chalk on dark board, coloured accents | Educational, informal — our favourite |
| **bold-graphic** | Comic/pop-art, halftone dots, heavy outlines | Eye-catching, punchy |
| **corporate-memphis** | Flat vector, vibrant pastels | Modern SaaS, approachable |
| **ikea-manual** | Minimal line art, black on white | Ultra-clean, no clutter |

## Setup for a New Project

### 1. Install the skills

```bash
cd your-project
npx skills add jimliu/baoyu-skills --skill baoyu-infographic --skill baoyu-imagine
```

This creates:
- `.agents/skills/baoyu-imagine/` — actual skill files
- `.agents/skills/baoyu-infographic/` — actual skill files
- `.claude/skills/baoyu-imagine` — symlink
- `.claude/skills/baoyu-infographic` — symlink
- `skills-lock.json` — lockfile

### 2. Get a Google AI API key

Go to https://aistudio.google.com/apikey and create a key. Enable billing on the associated Google Cloud project (image generation has no free API tier, but costs pennies per image).

### 3. Create the .env file

```bash
mkdir -p .baoyu-skills
echo "GOOGLE_API_KEY=your-key-here" > .baoyu-skills/.env
```

Edit the file to add your real key. **Do not paste keys into Claude Code chat** — edit the file directly, ideally when no Claude Code session is active (file change notifications can expose secrets in the session context).

### 4. Add .env to .gitignore

```
echo ".baoyu-skills/.env" >> .gitignore
```

### 5. Create the config files

```bash
mkdir -p .baoyu-skills/baoyu-imagine
mkdir -p .baoyu-skills/baoyu-infographic
```

`.baoyu-skills/baoyu-imagine/EXTEND.md`:
```yaml
---
version: 1
default_provider: google
default_quality: 2k
default_aspect_ratio: null
default_image_size: null
default_model:
  google: gemini-3.1-flash-image-preview
  openai: gpt-image-1.5
  azure: null
  openrouter: null
  dashscope: null
  minimax: null
  replicate: null
---
```

`.baoyu-skills/baoyu-infographic/EXTEND.md`:
```yaml
---
version: 1
default_provider: google
default_quality: 2k
default_aspect_ratio: null
default_image_size: null
default_model:
  google: gemini-3.1-flash-image-preview
  openai: gpt-image-1.5
  azure: null
  openrouter: null
  dashscope: null
  minimax: null
  replicate: null
---
```

### 6. Generate an infographic

Ask Claude Code to create an infographic, or call the skill directly:

```bash
bun .agents/skills/baoyu-imagine/scripts/main.ts \
  --promptfiles path/to/prompt.md \
  --image output.png \
  --ar 16:9 --quality 2k \
  --provider google --model gemini-3.1-flash-image-preview
```

## Prompt Tips

- **Less text = better output.** Use short labels, not paragraphs. The model renders everything you give it.
- **No hex codes in the prompt.** The model treats them as text and renders them visibly. Describe colours by name instead.
- **Add anti-hallucination rules.** Without them, the model invents statistics, timings, and data you never provided. Include:
  ```
  IMPORTANT RULES:
  - ONLY use text provided in this prompt. Do NOT invent statistics, timings, percentages, or any data not listed.
  - Do NOT render any hex colour codes as visible text.
  ```
- **Each generation is slightly different.** Run a few and pick the best. At ~$0.05/image it's cheap to iterate.
- **Specify layout explicitly.** "4 boxes in a row connected by arrows" works better than hoping the model interprets "linear-progression" correctly.

## Costs

| Item | Cost |
|------|------|
| skills.sh CLI | Free |
| baoyu skills | Free |
| Google AI API key | Free to create |
| Image generation (Nano Banana 2) | ~$0.04-0.07 per image |
| Typical infographic session (5-10 iterations) | ~$0.25-0.70 |

## File Structure

```
.agents/skills/
  baoyu-imagine/          # Image generation skill
  baoyu-infographic/      # Infographic workflow skill

.baoyu-skills/
  .env                    # API keys (gitignored)
  baoyu-imagine/
    EXTEND.md             # Provider/model config
  baoyu-infographic/
    EXTEND.md             # Provider/model config

.claude/skills/
  baoyu-imagine           # Symlink → .agents/skills/baoyu-imagine
  baoyu-infographic       # Symlink → .agents/skills/baoyu-infographic

infographic/              # Generated outputs
  {topic}/
    prompts/              # Prompt files
    style-{name}.png      # Generated images
    analysis.md           # Content analysis
    generate.sh           # Batch generation script
```
