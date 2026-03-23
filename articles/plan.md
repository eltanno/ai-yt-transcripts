# Article Writing System — Plan

## Goal

Build a Claude-assisted article writing workflow for corporate SharePoint. Articles cover Jim's personal engineering discoveries in AI, drawing on both direct experience and the YouTube transcript archive captured in this project. Articles should be professional but with Jim's personal voice — not AI slop.

## What We Have (All Offline)

### Reference Skills (saved in `articles/reference-skills/`)

| Skill | Purpose | Source |
|-------|---------|--------|
| `stop-slop-SKILL.md` | Anti-slop editing pass — 8 core rules, scoring rubric, phrase/structure catalogs | hardikpandya/stop-slop |
| `deslop-SKILL.md` | Professional/scientific variant — 10 rules, AI tropes catalog from tropes.fyi | stephenturner/skill-deslop |
| `humanizer-SKILL.md` | 25-pattern detection from Wikipedia AI Cleanup — unique "add soul" section | blader/humanizer |
| `voice-matched-content-SKILL.md` | Voice DNA extraction from writing samples — 8 dimensions, 4-phase process | openclaw/skills (brianrwagner) |
| `content-research-writer-SKILL.md` | Collaborative article writing workflow — outline, research, draft, feedback | ComposioHQ/awesome-claude-skills |

### Transcript Database
- Searchable via `python3 -m src.query "search terms" --limit N`
- Contains Nate B Jones, Nate Herk, Gary's Economics, and other channels
- Key transcripts on AI writing quality already identified (see Research Notes below)

---

## The Plan

### Step 1: Gather Writing Samples (Jim's action)

**What's needed:** 3-5 pieces of writing that sound like Jim. The more variety, the better the voice profile.

**Good candidates:**
- Slack messages or threads where you explained something technical
- Emails to colleagues about AI discoveries
- Any existing blog posts, internal wiki pages, or documentation you've written
- Casual writing (even texts or chat messages) that captures how you naturally explain things
- Meeting notes or summaries you wrote yourself

**How to provide them:**
- Paste them into a file: `articles/writing-samples/sample-1.md`, `sample-2.md`, etc.
- Or paste them directly into chat when we start working

**Tip from the research:** The samples you wrote fast without overthinking are the most useful — that's where your real voice lives.

---

### Step 2: Build Voice DNA Profile

Once samples are provided, Claude will:

1. Read all samples and analyse 8 dimensions:
   - Sentence architecture (length, fragments, variety)
   - Opening patterns (hooks, energy level)
   - Transition signatures (your bridge phrases — these are fingerprints)
   - Energy mapping (baseline, triggers, humor style)
   - Authority zones vs. learning zones (what you're confident about vs. exploring)
   - Vocabulary fingerprint (favorites, allergies, jargon stance)
   - Structural preferences (lists, headers, paragraph style)
   - Editing instincts (do you cut or expand? what makes you cringe?)

2. Generate a Voice DNA Profile document saved to `articles/voice-profile.md`

3. Jim reviews and corrects anything that's off

**Output:** A reusable voice profile that gets loaded before writing anything.

---

### Step 3: Build Custom Article-Writer Skill

Rather than installing an external skill wholesale, we build a custom `SKILL.md` tailored to Jim's SharePoint articles. It will combine:

- **Voice profile** — loaded as context for every article
- **Article structure** — tailored to the corporate SharePoint format
- **Research integration** — how to pull from the transcript database
- **De-slop pass** — cherry-picked rules from stop-slop, deslop, and humanizer (the best of each, merged and deduplicated)
- **Quality scoring** — the 5-dimension rubric (directness, rhythm, trust, authenticity, density) with 35/50 threshold

The skill goes in `.claude/skills/write-article/SKILL.md` (or similar).

**Article workflow the skill will encode:**

```
1. TOPIC — Jim describes what to write about
2. RESEARCH — Query transcript DB + any web research for supporting material
3. OUTLINE — Collaborative outline with Jim's input
4. DRAFT — Write first draft using voice profile
5. DE-SLOP — Run anti-slop pass (structural changes, not just word swaps)
6. VOICE CHECK — 5-question authenticity check against the profile
7. REVIEW — Jim reads, gives feedback, we iterate
8. IMAGES — Generate article header/illustrations
9. FINAL — Polish and prepare for SharePoint
```

---

### Step 4: Image Generation Setup

**Options (pick one based on API access):**

| Option | Best For | Needs |
|--------|----------|-------|
| GPT Image 1.5 via OpenAI API | Fast iteration, good text rendering | OpenAI API key |
| FLUX 2 Pro via Replicate/BFL | Consistent style, brand colors | Replicate or BFL API key |
| Nano Banana Pro | Free/cheap, good quality | API key |

**What we'll build:**
- A simple image generation script or skill that takes an article title + description and generates a header image
- Style consistent across articles (same visual language for the SharePoint column)
- Jim reviews and picks from 2-3 options

**Jim's action:** Decide which image API you have access to or want to set up.

---

### Step 5: First Article (Test Run)

Pick a topic from your AI discoveries. Write it end-to-end using the new system. Iterate on the voice profile and skill based on what works and what doesn't.

**Good first article candidates:**
- Something you know well (authority zone) so we can focus on voice/quality rather than research
- Something with good transcript material to draw from

---

### Step 6: Self-Improving Skill Loop

The skill should get better with every article written. Three mechanisms make this work:

#### 6a. Skill Document Self-Updates

After each article is finished, the skill appends a **Learnings** section to itself. This captures:
- Voice corrections Jim made during review (e.g., "Jim removed all instances of X phrasing", "Jim shortened the intro — prefers diving straight in")
- Structural patterns that worked well (e.g., "opening with a personal anecdote landed better than a statistic")
- Things Jim rejected (e.g., "too many subheadings — Jim prefers flowing prose for this length")
- De-slop patterns that keep recurring and need harder enforcement

The next article starts by reading these learnings, so the same mistakes don't repeat. This is the pattern Nate Herk uses in his Blotato content machine — the skill doc accumulates "Known Issues and Findings" with each run.

Format in the skill doc:
```markdown
## Learnings Log

### Article 1: [Title] (YYYY-MM-DD)
- VOICE: Jim cut "essentially" three times — add to vocabulary allergies
- STRUCTURE: Opening anecdote worked better than data hook
- REJECTED: Bold-first bullet format in the recommendations section
- SCORE: 38/50 (directness: 8, rhythm: 7, trust: 8, authenticity: 8, density: 7)

### Article 2: [Title] (YYYY-MM-DD)
- ...
```

#### 6b. Article Archive as Context

Each finished article goes in `articles/published/`. These serve as:
- **Voice reference** — the best examples of Jim's actual voice in article form (better than the original writing samples over time)
- **Topic memory** — so we don't repeat the same ground or can deliberately build on prior articles
- **Quality benchmark** — compare new drafts against published articles for consistency

The skill should reference the 2-3 most recent published articles before writing a new one.

#### 6c. Voice Profile Refinement

Every time Jim edits a draft, those edits are voice data. After each article:
1. Compare the draft Claude wrote vs. what Jim actually published
2. Extract the delta — what did Jim change?
3. Update `articles/voice-profile.md` with new patterns, corrections, or vocabulary changes
4. Over time, the voice profile shifts from "extracted from writing samples" to "proven across published articles"

#### 6d. Quality Scoring Over Time

Run the de-slop scoring rubric (directness, rhythm, trust, authenticity, density — each 1-10) on every draft and every final version. Track scores:

```markdown
## Score History

| Article | Draft Score | Final Score | Delta | Key Fix |
|---------|-------------|-------------|-------|---------|
| Article 1 | 31/50 | 39/50 | +8 | Cut filler, varied rhythm |
| Article 2 | 36/50 | 41/50 | +5 | Stronger opening, less hedging |
| Article 3 | 40/50 | 43/50 | +3 | Minor voice tweaks only |
```

The goal: draft scores trend upward as the skill learns. The gap between draft and final narrows. Eventually the first draft is close to publishable.

#### 6e. Periodic Skill Eval (Optional, When We Have 5+ Articles)

Borrow from Anthropic's skill-creator eval approach:
- Test the skill against the archive of published articles — can it reproduce the quality?
- Benchmark "with skill" vs "without skill" on a test topic
- Check whether model updates have caused regressions
- Trim the skill if parts are no longer needed (Goldilocks — don't let it bloat)

---

## Research Notes

### What Nate B Jones says about AI writing quality

**"I Stopped Drowning in AI Slop" (2025-10-10)**
- Slop is fixable but not with one magic bullet
- Build quality filter prompts per use case (not generic)
- Use AI as evaluator, not just generator — scoring rubrics with JSON output
- "I don't care if AI wrote it. I care if it's good."

**"I Spent 200 Hours Teaching AI Writing" (2025-10-24)** — 6 principles:
1. The bottleneck is never AI capability — it's ability to articulate what good looks like
2. AI forces tacit knowledge into explicit standards
3. Templates without business logic produce terrible output — define intent, not just format
4. You need 5-7 failure examples (what bad looks like)
5. AI default voice "obscures intent" — diplomatically hedged, pseudo-comprehensive, bland
6. Put AI on the evaluation side too, not just writing

**"How I Improved AI Output Quality 10X" (2025-11-13)** — Goldilocks prompting:
- 80% of prompts should be at the right altitude — enough context but not exhaustive
- Under 500 tokens for the common case
- Over-specification kills creativity and burns context
- Modular "slugs" of context (layout, color, tone) that stack

### What Nate Herk shows about content workflows and self-improving skills

**"Claude Code + Blotato = Content Machine" (2026-03-17)**
- Skill-based approach: each run improves the skill document
- When Claude hits a problem (e.g., API rejects oversized images), it adds "Known Issues and Findings" to the SKILL.md
- Next run reads those findings and avoids the same mistake
- Iterative refinement: "Think about how much better this will be after 10 runs"
- Brand assets folder for consistent visuals
- The more business context and brand guidelines you add, the better it gets

**"Claude Code Skills Just Got Even Better" (2026-03-05)** — The eval loop:
- Anthropic's `skill-creator` skill can evaluate, benchmark, and improve other skills
- Two types of skills: capability uplift (teach Claude something) vs encoded preference (your specific workflow)
- Encoded preference skills stay durable across model updates — the process is specific to you
- Evals catch regressions (skill works worse after model update) and spot growth (skill is no longer needed)
- Benchmarks compare with-skill vs without-skill on pass rate, time, tokens
- Trigger tuning: tests natural language prompts to make sure the right skill fires
- Built a YouTube weekly roundup skill in 20 mins. First run: data wrong. Gave feedback, improved. Second run: accurate.
- Key quote: "The more you use a skill, the better and better because you're able to give feedback on what you like and what you don't"

**"Turn Claude Code Into Your Executive Assistant" (2026-03-05)** — Project-level accumulation:
- Every research report, decision, and piece of feedback persists in the project folder
- CLAUDE.md points to context files (me.md, work.md, priorities.md) rather than loading everything
- Each session builds on prior sessions because artefacts persist on disk
- "It gets smarter and smarter about what you're doing the more you use it"
- Brand assets folder, decision logs, project readmes — all referenceable context

### Key anti-slop principles (consolidated from all reference skills)

**What works:** Structural changes — varying sentence length ("burstiness"), breaking intro-list-conclusion patterns, injecting specific personal experience, the read-aloud test.

**What doesn't work:** Surface-level vocabulary swaps (replacing "delve" with "examine" but keeping the same formulaic structure).

**The humanizer's unique insight:** Sterile, voiceless writing is just as obvious as slop. Having opinions, acknowledging complexity, using first person, and letting some mess in — these are what make writing human.

---

## Prompt Injection Safety

Before using any external skill:
- Every SKILL.md in `reference-skills/` has been read and reviewed
- No hidden instructions, system prompt overrides, or tool-calling directives found
- No API keys or credentials requested by the skill content itself
- The skills we saved are pure markdown instruction files (no bundled scripts)
- When we build the custom skill, it will be written from scratch drawing on these references — not copy-pasted wholesale

---

## File Structure

```
articles/
├── plan.md                          # This file
├── voice-profile.md                 # (Step 2 — generated from writing samples)
├── score-history.md                 # (Step 6d — quality scores over time)
├── writing-samples/                 # (Step 1 — Jim provides these)
│   ├── sample-1.md
│   ├── sample-2.md
│   └── ...
├── reference-skills/                # Raw reference skills (read-only)
│   ├── stop-slop-SKILL.md
│   ├── deslop-SKILL.md
│   ├── humanizer-SKILL.md
│   ├── voice-matched-content-SKILL.md
│   └── content-research-writer-SKILL.md
├── drafts/                          # (Step 5 — working drafts)
│   └── ...
└── published/                       # (Step 6b — finished articles as reference)
    └── ...
```

---

## Next Steps (When Ready)

1. Jim gathers 3-5 writing samples and saves them to `articles/writing-samples/`
2. Point Claude at this plan: "Read `articles/plan.md` and start Step 2"
3. We build the voice profile
4. We build the custom article-writer skill
5. We write the first article
