---
name: deslop
description: Remove AI writing patterns from prose. Calibrated for both professional/scientific and blog writing. Covers 10 primary issues with detailed reference catalogs.
source: https://github.com/stephenturner/skill-deslop
---

# Deslop: Remove AI Writing Patterns from Prose

Strip predictable AI patterns from writing. Make prose sound like a specific human wrote it, not like a language model generated it.

## Core Rules

### 1. Cut filler phrases
Remove throat-clearing openers ("Here's the thing:"), emphasis crutches ("Let that sink in."), business jargon ("navigate the landscape"), and meta-commentary ("In this section, we'll explore...").

### 2. Break formulaic structures
Avoid binary contrasts ("Not X. Y."), negative listings ("Not a X. Not a Y. A Z."), dramatic fragmentation ("Speed. That's it. That's the tradeoff."), self-posed rhetorical questions ("The result? Devastating."), and anaphora/tricolon abuse.

### 3. Eliminate AI tropes
Watch for: "quietly" and other magic adverbs, "delve" and its cousins, the "serves as" dodge, false ranges ("from X to Y" where the range is meaningless), superficial participle analyses ("highlighting its importance"), invented concept labels ("the supervision paradox"), grandiose stakes inflation, patronizing analogies, and false vulnerability.

### 4. Use active voice with human subjects
Prefer active constructions with named actors. "The complaint becomes a fix" is wrong. "The team fixed it" is right. If no specific person fits, use "we" in scientific prose or "you" in blog posts.

### 5. Be specific
No vague declaratives ("The reasons are structural"). Name the specific thing. No vague attributions ("Experts argue..."). If you cannot name the expert, you do not have a source. Domain terminology is fine. Business buzzwords and AI vocabulary tells are not.

### 6. Match register to context
Blog posts: put the reader in the room. "You" beats "People."
Scientific writing: use "we" for your own work, cite specific authors, maintain formality without narrator-distance.

### 7. Vary rhythm
Mix sentence lengths. Two items beat three. End paragraphs differently. No em dashes. Do not stack short punchy fragments.

### 8. Trust readers
State facts directly. Skip softening, justification, hand-holding. No "Let's break this down." No fractal summaries.

### 9. Watch formatting tells
No bold-first bullets. No unicode arrows. No em dashes. No signposted conclusions ("In conclusion..."). No "Despite these challenges..." formulas.

### 10. Do not dilute
One point per section. Do not restate the same argument in ten different ways. Do not beat a single metaphor to death.

## Quick Checks

- Heavy use of adverbs or -ly words? Cut them.
- Any passive voice? Find the actor, make them the subject.
- Inanimate thing doing a human verb? Name the person.
- Any "here's what/this/that" throat-clearing? Cut to the point.
- Any "not X, it's Y" contrasts? State Y directly.
- Any self-posed rhetorical question answered immediately? Fold into a statement.
- Three consecutive sentences match length? Break one.
- Em dash anywhere? Remove it.
- "It's worth noting" or similar filler? Delete.
- Same metaphor used more than twice? Replace or cut repeats.
- "Despite these challenges..." formula? Rewrite.
- Bold-first bullet pattern? Remove bold leads.
- Tricolon (three-item list)? Use two items or one.

## Scoring

Rate 1-10 on each dimension:

| Dimension | Question |
|-----------|----------|
| Directness | Statements or announcements? |
| Rhythm | Varied or metronomic? |
| Trust | Respects reader intelligence? |
| Authenticity | Sounds like a specific human wrote it? |
| Density | Anything cuttable? |

Below 35/50: revise.

## AI Tropes Catalog (from tropes.fyi)

### Word Choice
- **"Quietly" and magic adverbs**: "deeply", "fundamentally", "remarkably", "arguably"
- **"Delve" and friends**: "certainly", "utilize", "leverage", "robust", "streamline", "harness"
- **"Tapestry" and "Landscape"**: ornate nouns where simpler words work
- **"Serves as" dodge**: replacing "is" with pompous alternatives

### Sentence Structure
- **Negative parallelism**: "It's not X -- it's Y" (the #1 AI tell)
- **"Not X. Not Y. Just Z."**: dramatic countdown
- **"The X? A Y."**: self-posed rhetorical questions
- **Anaphora abuse**: repeating same sentence opening
- **Tricolon abuse**: rule-of-three overuse
- **"It's worth noting"**: filler transitions
- **Superficial analyses**: participle phrases tacking on hollow significance
- **False ranges**: "from X to Y" where there's no real spectrum

### Paragraph Structure
- **Short punchy fragments**: manufactured emphasis via fragments
- **Listicle in a trench coat**: numbered points disguised as prose

### Tone
- **"Here's the kicker"**: false suspense transitions
- **"Think of it as..."**: patronizing analogies
- **"Imagine a world where..."**: AI futurism invitation
- **False vulnerability**: simulated self-awareness
- **"The truth is simple"**: asserting clarity instead of proving it
- **Grandiose stakes inflation**: everything is world-historically important
- **"Let's break this down"**: pedagogical voice for expert audiences
- **Vague attributions**: "Experts argue..." without naming anyone
- **Invented concept labels**: "the supervision paradox", "the acceleration trap"

### Formatting
- **Em-dash addiction**: 20+ per piece vs human 2-3
- **Bold-first bullets**: every list item starts with bolded keyword
- **Unicode decoration**: fancy arrows and smart quotes

### Composition
- **Fractal summaries**: telling what you'll say, saying it, summarizing
- **Dead metaphor**: same metaphor repeated 5-10 times
- **Historical analogy stacking**: rapid-fire company name-drops
- **One-point dilution**: restating same argument 10 ways
- **Signposted conclusion**: "In conclusion..."
- **"Despite its challenges..."**: acknowledge then dismiss formula

## Examples

### Scientific writing:

**Before:**
> "It's worth noting that these findings have important implications for how we navigate the challenges of forecast ensembling moving forward. Despite these challenges, this work contributes meaningfully to the growing body of literature, highlighting the need for continued evaluation."

**After:**
> "If individual model rankings are unstable across geography and time, ensemble methods that weight models by past performance may not improve on equal-weight approaches."

### Blog post:

**Before:**
> "Here's the thing: most bioinformatics pipelines break in production. Not because the code is bad. Because the data is bad. Let that sink in."

**After:**
> "Most bioinformatics pipelines break in production. The code runs fine. The data doesn't match the assumptions baked into it."
