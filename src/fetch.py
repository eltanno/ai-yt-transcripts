"""Fetch new YouTube transcripts and save as markdown files.

Usage:
    # Fetch latest from a channel (skips videos already in transcripts/)
    python -m src.fetch --channel @NateBJones

    # Fetch a specific video
    python -m src.fetch --url "https://www.youtube.com/watch?v=VIDEO_ID"

    # Fetch with a limit on how many new videos to grab
    python -m src.fetch --channel @NateBJones --limit 10

Requires: yt-dlp, youtube-transcript-api
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from rich.console import Console

from src.config import TRANSCRIPTS_DIR

console = Console()


def slugify(text: str, max_length: int = 60) -> str:
    """Convert title to kebab-case slug for filename."""
    text = text.lower()
    # Remove common filler words for shorter filenames
    for word in ["here's", "heres", "that's", "thats", "nobody's", "nobodys",
                 "what's", "whats", "it's", "you're", "don't", "didn't",
                 "won't", "isn't", "aren't", "we're", "they're", "i'm",
                 "here is", "what actually", "and why", "and how"]:
        text = text.replace(word, "")
    # Replace non-alphanumeric chars with hyphens
    text = re.sub(r"[^a-z0-9]+", "-", text)
    # Clean up multiple hyphens and trim
    text = re.sub(r"-+", "-", text).strip("-")
    # Truncate to max length at word boundary
    if len(text) > max_length:
        text = text[:max_length].rsplit("-", 1)[0]
    return text


def get_existing_video_ids(transcripts_dir: Path) -> set[str]:
    """Scan existing markdown files to find already-downloaded video IDs."""
    ids = set()
    for md_file in transcripts_dir.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        match = re.search(r"watch\?v=([a-zA-Z0-9_-]{11})", content)
        if match:
            ids.add(match.group(1))
    return ids


def get_channel_videos(channel_handle: str, limit: int = 50) -> list[dict]:
    """Get recent video metadata from a channel using yt-dlp."""
    url = f"https://www.youtube.com/{channel_handle}/videos"
    console.print(f"[bold]Fetching video list from {channel_handle}...[/bold]")

    cmd = [
        "yt-dlp",
        "--flat-playlist",
        "--dump-json",
        "--playlist-end", str(limit),
        url,
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if result.returncode != 0:
        console.print(f"[red]yt-dlp error: {result.stderr[:500]}[/red]")
        return []

    videos = []
    for line in result.stdout.strip().split("\n"):
        if line.strip():
            try:
                data = json.loads(line)
                videos.append({
                    "id": data.get("id", ""),
                    "title": data.get("title", ""),
                    "duration": data.get("duration"),
                    "view_count": data.get("view_count"),
                    "upload_date": data.get("upload_date", ""),  # YYYYMMDD
                    "url": f"https://www.youtube.com/watch?v={data.get('id', '')}",
                })
            except json.JSONDecodeError:
                continue

    return videos


def get_video_metadata(video_id: str) -> dict:
    """Get metadata for a single video using yt-dlp."""
    cmd = [
        "yt-dlp",
        "--dump-json",
        "--skip-download",
        f"https://www.youtube.com/watch?v={video_id}",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        console.print(f"[red]yt-dlp error for {video_id}: {result.stderr[:300]}[/red]")
        return {}

    try:
        data = json.loads(result.stdout)
        return {
            "id": data.get("id", video_id),
            "title": data.get("title", ""),
            "duration": data.get("duration"),
            "view_count": data.get("view_count"),
            "upload_date": data.get("upload_date", ""),
            "channel": data.get("uploader", ""),
            "url": f"https://www.youtube.com/watch?v={video_id}",
        }
    except json.JSONDecodeError:
        return {}


def fetch_transcript(video_id: str) -> str:
    """Fetch transcript for a video. Tries youtube-transcript-api first, falls back to yt-dlp."""
    # Try youtube-transcript-api first
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)
        lines = [entry.text for entry in transcript]
        return "\n".join(lines)
    except Exception:
        pass

    # Fallback: yt-dlp subtitle download
    try:
        cmd = [
            "yt-dlp",
            "--write-auto-sub",
            "--sub-lang", "en",
            "--sub-format", "json3",
            "--skip-download",
            "--output", f"/tmp/yt-sub-{video_id}",
            f"https://www.youtube.com/watch?v={video_id}",
        ]
        subprocess.run(cmd, capture_output=True, text=True, timeout=60)

        sub_file = Path(f"/tmp/yt-sub-{video_id}.en.json3")
        if sub_file.exists():
            data = json.loads(sub_file.read_text())
            lines = []
            for event in data.get("events", []):
                segs = event.get("segs", [])
                text = "".join(s.get("utf8", "") for s in segs).strip()
                if text and text != "\n":
                    lines.append(text)
            sub_file.unlink()
            # Deduplicate consecutive identical lines
            deduped = []
            for line in lines:
                if not deduped or line != deduped[-1]:
                    deduped.append(line)
            return "\n".join(deduped)
    except Exception:
        pass

    return ""


def format_transcript_paragraphs(text: str, lines_per_para: int = 8) -> str:
    """Join transcript lines into flowing paragraphs."""
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    paragraphs = []
    for i in range(0, len(lines), lines_per_para):
        para = " ".join(lines[i:i + lines_per_para])
        paragraphs.append(para)
    return "\n\n".join(paragraphs)


def format_duration(seconds: int | None) -> str:
    """Format seconds into human-readable duration."""
    if not seconds:
        return "Unknown"
    minutes = seconds // 60
    secs = seconds % 60
    if secs:
        return f"{minutes}:{secs:02d}"
    return f"{minutes} min"


def format_views(count: int | None) -> str:
    """Format view count."""
    if not count:
        return "Unknown"
    if count >= 1_000_000:
        return f"{count / 1_000_000:.1f}M views"
    if count >= 1_000:
        return f"{count / 1_000:.0f}K views"
    return f"{count} views"


def format_date(date_str: str) -> str:
    """Convert YYYYMMDD to YYYY-MM-DD."""
    if len(date_str) == 8:
        return f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
    return date_str


def save_transcript(video: dict, transcript: str, transcripts_dir: Path) -> Path:
    """Save a video transcript as a markdown file."""
    date = format_date(video.get("upload_date", ""))
    title = video.get("title", "untitled")
    slug = slugify(title)
    filename = f"{date}-{slug}.md"
    filepath = transcripts_dir / filename

    channel = video.get("channel", "Unknown")
    duration = format_duration(video.get("duration"))
    views = format_views(video.get("view_count"))
    url = video.get("url", "")

    formatted_transcript = format_transcript_paragraphs(transcript)

    content = f"""# {title}

- **Channel:** {channel}
- **Date:** {date}
- **Duration:** {duration}
- **Views:** {views}
- **URL:** {url}

## Transcript

{formatted_transcript}
"""

    filepath.write_text(content, encoding="utf-8")
    return filepath


def main():
    parser = argparse.ArgumentParser(description="Fetch YouTube transcripts")
    parser.add_argument("--channel", help="YouTube channel handle (e.g. @NateBJones)")
    parser.add_argument("--url", help="Single YouTube video URL")
    parser.add_argument("--limit", type=int, default=50, help="Max videos to check from channel (default: 50)")
    args = parser.parse_args()

    if not args.channel and not args.url:
        parser.print_help()
        sys.exit(1)

    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    existing_ids = get_existing_video_ids(TRANSCRIPTS_DIR)
    console.print(f"[dim]Found {len(existing_ids)} existing transcripts[/dim]")

    videos_to_fetch = []

    if args.url:
        # Single video
        match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", args.url)
        if not match:
            console.print("[red]Could not extract video ID from URL[/red]")
            sys.exit(1)
        video_id = match.group(1)
        if video_id in existing_ids:
            console.print(f"[yellow]Video {video_id} already exists, skipping[/yellow]")
            sys.exit(0)
        meta = get_video_metadata(video_id)
        if meta:
            videos_to_fetch.append(meta)

    elif args.channel:
        # Channel — get recent videos
        all_videos = get_channel_videos(args.channel, limit=args.limit)
        for v in all_videos:
            if v["id"] not in existing_ids:
                videos_to_fetch.append(v)

        console.print(f"[bold]{len(all_videos)} videos on channel, {len(videos_to_fetch)} new[/bold]")

    if not videos_to_fetch:
        console.print("[green]Nothing new to fetch![/green]")
        return

    # Fetch transcripts
    success = 0
    failed = 0
    for i, video in enumerate(videos_to_fetch, 1):
        title = video.get("title", video["id"])
        console.print(f"\n[bold][{i}/{len(videos_to_fetch)}][/bold] {title}")

        # Get full metadata if we only have flat playlist data
        if not video.get("channel"):
            full_meta = get_video_metadata(video["id"])
            if full_meta:
                video.update(full_meta)

        transcript = fetch_transcript(video["id"])
        if not transcript:
            console.print(f"  [yellow]No transcript available — creating placeholder[/yellow]")
            transcript = "Transcript not yet available."

        filepath = save_transcript(video, transcript, TRANSCRIPTS_DIR)
        console.print(f"  [green]Saved:[/green] {filepath.name}")
        success += 1

    console.print(f"\n[bold green]Done![/bold green] {success} new, {failed} failed")
    if success > 0:
        console.print(f"\n[dim]Run 'python -m src.ingest' to re-embed and update the database[/dim]")


if __name__ == "__main__":
    main()
