#!/usr/bin/env bash
# Daily fetch + ingest + commit + push for YouTube transcripts
set -euo pipefail

cd "$(dirname "$0")/.."

echo "=== $(date '+%Y-%m-%d %H:%M') Starting daily fetch ==="

# Fetch new videos
python -m src.fetch --channel @NateBJones --limit 10

# Check if any new files were added
if git diff --quiet && [ -z "$(git ls-files --others --exclude-standard transcripts/)" ]; then
    echo "No new transcripts — skipping ingest and commit."
    exit 0
fi

# Re-ingest into LanceDB
python -m src.ingest

# Commit and push new transcripts
git add transcripts/ db/
git commit -m "Add new transcripts $(date '+%Y-%m-%d')"
git push

echo "=== Done ==="
