#!/usr/bin/env python3
"""
Research Collector — Mansur's StartupResearch vault automation.

Searches Hacker News, Reddit, and YouTube for a given topic and saves all
raw data as a clean markdown file in raw/. No API key required by default.
Reddit uses the public JSON API when REDDIT_CLIENT_ID is not set; set it
in .env to switch to PRAW for broader multi-subreddit coverage.
Analysis is done separately via Claude Code.

Usage:
    python agent.py "problems developers face with AI tools"
    python agent.py "KZ accounting software gaps" --no-youtube
    python agent.py "vibe coding security" --hn-limit 20
"""

import argparse
import os
import re
import sys
from datetime import date
from pathlib import Path

import requests
from dotenv import load_dotenv

# ── Vault paths ────────────────────────────────────────────────────────────────
VAULT_ROOT = Path(__file__).parent
RAW_DIR = VAULT_ROOT / "raw"
LOG_FILE = VAULT_ROOT / "log.md"
HOT_FILE = VAULT_ROOT / "hot.md"

# Multi-subreddit search string for PRAW
SUBREDDITS = (
    "SideProject+microsaas+startups+programming+webdev+"
    "indiehackers+entrepreneur+ChatGPT+MachineLearning+"
    "software+technology+learnprogramming+freelance"
)

# Endpoints for the public Reddit JSON API (no auth)
_REDDIT_PUBLIC_ENDPOINTS: list[tuple[str, int]] = [
    ("https://www.reddit.com/search.json",                        25),
    ("https://www.reddit.com/r/webdev/search.json",               10),
    ("https://www.reddit.com/r/SideProject/search.json",          10),
    ("https://www.reddit.com/r/ExperiencedDevs/search.json",      10),
]

# Browser UA avoids Reddit's bot filter on the public JSON API
_REDDIT_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)


# ── Helpers ────────────────────────────────────────────────────────────────────

def slugify(text: str) -> str:
    """Convert a topic string to a URL-safe kebab-case slug (max 60 chars)."""
    s = text.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"[\s-]+", "-", s).strip("-")
    return s[:60]


def trunc(text: str, n: int) -> str:
    return text[:n] + "…" if len(text) > n else text


def banner(msg: str) -> None:
    print(f"\n{'─' * 52}")
    print(f"  {msg}")
    print(f"{'─' * 52}")


# ── 1. Reddit ──────────────────────────────────────────────────────────────────

def search_reddit(query: str, limit: int = 20) -> list[dict]:
    """Search Reddit posts + top comments via PRAW (read-only, no login needed)."""
    try:
        import praw
    except ImportError:
        print("  [reddit] praw not installed — run: pip install praw")
        return []

    cid = os.environ.get("REDDIT_CLIENT_ID")
    csec = os.environ.get("REDDIT_CLIENT_SECRET")
    if not cid or not csec:
        print("  [reddit] REDDIT_CLIENT_ID / REDDIT_CLIENT_SECRET not set — skipping")
        return []

    reddit = praw.Reddit(
        client_id=cid,
        client_secret=csec,
        user_agent=os.environ.get("REDDIT_USER_AGENT", "StartupResearch/1.0"),
    )

    results: list[dict] = []
    try:
        for post in reddit.subreddit(SUBREDDITS).search(
            query, sort="relevance", time_filter="year", limit=limit
        ):
            comments: list[dict] = []
            try:
                post.comments.replace_more(limit=0)
                for c in post.comments[:6]:
                    if hasattr(c, "body") and c.score > 2:
                        comments.append({"score": c.score, "text": trunc(c.body, 600)})
            except Exception:
                pass

            results.append({
                "title": post.title,
                "url": f"https://reddit.com{post.permalink}",
                "score": post.score,
                "subreddit": post.subreddit.display_name,
                "text": trunc(post.selftext, 1500) if post.selftext else "",
                "comments": comments,
            })
    except Exception as e:
        print(f"  [reddit] error: {e}")

    print(f"  [reddit] {len(results)} posts")
    return results


# ── 1b. Reddit public JSON API (no credentials) ────────────────────────────────

def search_reddit_public(query: str) -> list[dict]:
    """Search Reddit via the public .json API — no credentials required.

    Hits the global search endpoint plus three targeted subreddits.
    Deduplicates by post ID, then fetches up to 5 top comments per post.
    A 0.5 s pause between comment fetches keeps us well under rate limits.
    """
    import time

    session = requests.Session()
    session.headers.update({"User-Agent": _REDDIT_UA})

    seen_ids: set[str] = set()
    results: list[dict] = []

    for url, per_limit in _REDDIT_PUBLIC_ENDPOINTS:
        is_subreddit = "/r/" in url
        params: dict = {
            "q": query,
            "sort": "top",
            "t": "year",
            "limit": per_limit,
        }
        if is_subreddit:
            params["restrict_sr"] = "on"

        try:
            resp = session.get(url, params=params, timeout=12)
            resp.raise_for_status()
            children = resp.json().get("data", {}).get("children", [])
        except Exception as e:
            print(f"  [reddit_public] {url.split('reddit.com')[1]} — {e}")
            continue

        for child in children:
            post = child.get("data", {})
            post_id = post.get("id", "")
            if not post_id or post_id in seen_ids:
                continue
            seen_ids.add(post_id)

            permalink = post.get("permalink", "")
            selftext = post.get("selftext", "")
            # Reddit returns "[removed]" or "[deleted]" for dead posts
            if selftext in ("[removed]", "[deleted]"):
                selftext = ""

            # Fetch top comments for this post
            comments: list[dict] = []
            if permalink:
                try:
                    cr = session.get(
                        f"https://www.reddit.com{permalink}.json",
                        params={"limit": 10, "depth": 1, "sort": "top"},
                        timeout=12,
                    )
                    cr.raise_for_status()
                    comment_listing = cr.json()[1].get("data", {}).get("children", [])
                    for cc in comment_listing:
                        cdata = cc.get("data", {})
                        body = cdata.get("body", "")
                        cscore = cdata.get("score", 0)
                        if body and body not in ("[deleted]", "[removed]") and cscore > 1:
                            comments.append({"score": cscore, "text": trunc(body, 600)})
                        if len(comments) >= 5:
                            break
                    time.sleep(0.5)
                except Exception:
                    pass

            results.append({
                "title": post.get("title", ""),
                "url": post.get("url") or f"https://reddit.com{permalink}",
                "score": post.get("score", 0),
                "subreddit": post.get("subreddit", ""),
                "text": trunc(selftext, 1500),
                "comments": comments,
            })

    print(f"  [reddit_public] {len(results)} posts (no credentials)")
    return results


# ── 2. Hacker News ─────────────────────────────────────────────────────────────

def search_hackernews(query: str, limit: int = 50) -> tuple[list[dict], list[dict]]:
    """Search HN stories AND comments via the Algolia API (no key needed).

    Returns (stories, comments) as separate lists so both can be rendered
    independently in the output markdown.
    """
    MIN_SCORE = 10
    stories: list[dict] = []
    comments: list[dict] = []
    seen_ids: set[str] = set()

    # ── 2a. Stories ────────────────────────────────────────────────────────────
    try:
        resp = requests.get(
            "https://hn.algolia.com/api/v1/search",
            params={
                "query": query,
                "tags": "story",
                "hitsPerPage": limit,
                "numericFilters": f"points>={MIN_SCORE}",
            },
            timeout=10,
        )
        resp.raise_for_status()

        for hit in resp.json().get("hits", []):
            hn_id = hit.get("objectID", "")
            if hn_id in seen_ids:
                continue
            seen_ids.add(hn_id)

            story: dict = {
                "title": hit.get("title", ""),
                "url": (hit.get("url")
                        or f"https://news.ycombinator.com/item?id={hn_id}"),
                "hn_url": f"https://news.ycombinator.com/item?id={hn_id}",
                "score": hit.get("points", 0),
                "num_comments": hit.get("num_comments", 0),
                "author": hit.get("author", ""),
                "date": (hit.get("created_at") or "")[:10],
                "text": trunc(hit.get("story_text") or "", 1000),
                "comments": [],
            }

            # Fetch top 10 comments from the item endpoint
            if hn_id:
                try:
                    cr = requests.get(
                        f"https://hn.algolia.com/api/v1/items/{hn_id}", timeout=8
                    )
                    for child in (cr.json().get("children") or [])[:10]:
                        txt = child.get("text") or ""
                        if txt:
                            story["comments"].append({
                                "author": child.get("author") or "",
                                "score": child.get("points") or 0,
                                "text": trunc(txt, 600),
                            })
                except Exception:
                    pass

            stories.append(story)

    except Exception as e:
        print(f"  [hn] stories error: {e}")

    # ── 2b. Comments (the real pain points live here) ──────────────────────────
    try:
        resp = requests.get(
            "https://hn.algolia.com/api/v1/search",
            params={
                "query": query,
                "tags": "comment",
                "hitsPerPage": limit,
            },
            timeout=10,
        )
        resp.raise_for_status()

        for hit in resp.json().get("hits", []):
            cid = hit.get("objectID", "")
            if cid in seen_ids:
                continue
            seen_ids.add(cid)

            story_id = hit.get("story_id") or hit.get("parent_id") or ""
            comments.append({
                "text": trunc(hit.get("comment_text") or "", 800),
                "author": hit.get("author", ""),
                "score": hit.get("points", 0),
                "story_title": hit.get("story_title") or "",
                "story_url": (f"https://news.ycombinator.com/item?id={story_id}"
                              if story_id else ""),
                "url": f"https://news.ycombinator.com/item?id={cid}",
                "date": (hit.get("created_at") or "")[:10],
            })

    except Exception as e:
        print(f"  [hn] comments error: {e}")

    print(f"  [hn] {len(stories)} stories · {len(comments)} comments")
    return stories, comments


# ── 3. YouTube ─────────────────────────────────────────────────────────────────

def _parse_vtt(vtt_text: str) -> str:
    """Strip VTT timing lines and tags, return plain transcript text."""
    vtt_text = re.sub(r"\d{2}:\d{2}:\d{2}\.\d{3} --> .*", "", vtt_text)
    vtt_text = re.sub(r"<[^>]+>", "", vtt_text)
    lines = [
        l.strip()
        for l in vtt_text.splitlines()
        if l.strip() and not l.strip().startswith("WEBVTT") and not l.strip().isdigit()
    ]
    # Deduplicate consecutive duplicate lines (VTT rolling captions)
    deduped: list[str] = []
    for line in lines:
        if not deduped or line != deduped[-1]:
            deduped.append(line)
    return " ".join(deduped)


def search_youtube(query: str, limit: int = 7) -> list[dict]:
    """Search YouTube via yt-dlp and fetch English transcripts (no API key)."""
    try:
        import yt_dlp  # noqa: PLC0415
    except ImportError:
        print("  [youtube] yt-dlp not installed — run: pip install yt-dlp")
        return []

    import tempfile

    results: list[dict] = []

    # Step 1: collect video IDs + titles from search
    search_opts: dict = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": True,
    }
    entries: list[dict] = []
    try:
        with yt_dlp.YoutubeDL(search_opts) as ydl:
            info = ydl.extract_info(f"ytsearch{limit}:{query}", download=False)
        entries = info.get("entries") or []
    except Exception as e:
        print(f"  [youtube] search error: {e}")
        return []

    if not entries:
        print("  [youtube] no results found")
        return []

    # Step 2: fetch subtitles for each video into a temp dir
    with tempfile.TemporaryDirectory() as tmpdir:
        for entry in entries:
            vid_id = entry.get("id")
            title = entry.get("title", "")
            if not vid_id:
                continue

            transcript = ""
            sub_opts: dict = {
                "quiet": True,
                "no_warnings": True,
                "skip_download": True,
                "writesubtitles": True,       # manual captions first
                "writeautomaticsub": True,    # fall back to auto-generated
                "subtitleslangs": ["en", "en-US"],
                "subtitlesformat": "vtt",
                "outtmpl": f"{tmpdir}/{vid_id}",
            }

            try:
                with yt_dlp.YoutubeDL(sub_opts) as ydl:
                    ydl.download([f"https://youtube.com/watch?v={vid_id}"])

                # Pick the first .vtt file that belongs to this video
                vtt_path = None
                for fname in sorted(os.listdir(tmpdir)):
                    if vid_id in fname and fname.endswith(".vtt"):
                        vtt_path = os.path.join(tmpdir, fname)
                        break

                if vtt_path:
                    raw_vtt = Path(vtt_path).read_text(encoding="utf-8", errors="ignore")
                    transcript = _parse_vtt(raw_vtt)
                    os.remove(vtt_path)

            except Exception:
                pass  # No transcript available — still record the video

            results.append({
                "video_id": vid_id,
                "title": title,
                "url": f"https://youtube.com/watch?v={vid_id}",
                "transcript": trunc(transcript, 4000) if transcript else "",
            })

    with_transcripts = sum(1 for r in results if r["transcript"])
    print(f"  [youtube] {len(results)} videos · {with_transcripts} with transcripts")
    return results


# ── 4. Build raw markdown ──────────────────────────────────────────────────────

def build_raw_markdown(
    topic: str,
    reddit: list[dict],
    hn_stories: list[dict],
    hn_comments: list[dict],
    yt: list[dict],
    reddit_source: str = "Reddit (PRAW)",
) -> str:
    """Assemble all collected data into a structured markdown file for Claude Code analysis."""
    today = date.today().isoformat()
    yt_with = sum(1 for v in yt if v["transcript"])

    parts: list[str] = [
        f"# Raw Research: {topic}\n\n",
        f"| Field | Value |\n",
        f"|---|---|\n",
        f"| Collected | {today} |\n",
        f"| {reddit_source} posts | {len(reddit)} |\n",
        f"| HN stories | {len(hn_stories)} (≥10 pts) |\n",
        f"| HN comments | {len(hn_comments)} |\n",
        f"| YouTube videos | {len(yt)} ({yt_with} with transcripts) |\n",
        f"\n---\n\n",
    ]

    # ── Reddit ─────────────────────────────────────────────────────────────────
    if reddit:
        parts.append("## Reddit\n\n")
        for i, p in enumerate(reddit, 1):
            parts.append(
                f"### [{i}] r/{p['subreddit']} · {p['score']} upvotes\n"
                f"**{p['title']}**  \n"
                f"<{p['url']}>\n\n"
            )
            if p["text"]:
                parts.append(f"{p['text']}\n\n")
            for c in p["comments"]:
                parts.append(f"> **[{c['score']} pts]** {c['text']}\n\n")
            parts.append("---\n\n")

    # ── HN Stories ─────────────────────────────────────────────────────────────
    if hn_stories:
        parts.append("## Hacker News — Stories\n\n")
        for i, s in enumerate(hn_stories, 1):
            parts.append(
                f"### [{i}] {s['score']} pts · {s['num_comments']} comments · {s['date']}\n"
                f"**{s['title']}**  \n"
                f"Link: <{s['url']}>  \n"
                f"Discussion: <{s['hn_url']}>\n\n"
            )
            if s["text"]:
                parts.append(f"{s['text']}\n\n")
            if s["comments"]:
                parts.append("**Top comments:**\n\n")
                for c in s["comments"]:
                    score_str = f"[{c['score']} pts] " if c["score"] else ""
                    author_str = f"_{c['author']}_ — " if c["author"] else ""
                    parts.append(f"> {score_str}{author_str}{c['text']}\n\n")
            parts.append("---\n\n")

    # ── HN Comments ────────────────────────────────────────────────────────────
    if hn_comments:
        parts.append("## Hacker News — Standalone Comments\n\n")
        parts.append(
            "_These comments matched the search query directly — "
            "often the richest source of pain points._\n\n"
        )
        for i, c in enumerate(hn_comments, 1):
            story_ref = ""
            if c["story_title"]:
                story_ref = f"  \nFrom story: [{c['story_title']}]({c['story_url']})"
            parts.append(
                f"#### [{i}] _{c['author']}_ · {c['date']}{story_ref}\n\n"
                f"{c['text']}\n\n"
                f"<{c['url']}>\n\n"
                "---\n\n"
            )

    # ── YouTube ────────────────────────────────────────────────────────────────
    if yt:
        parts.append("## YouTube Transcripts\n\n")
        for i, v in enumerate(yt, 1):
            parts.append(
                f"### [{i}] {v['title']}\n"
                f"<{v['url']}>\n\n"
            )
            if v["transcript"]:
                parts.append(f"{v['transcript']}\n\n")
            else:
                parts.append("_No transcript available._\n\n")
            parts.append("---\n\n")

    raw = "".join(parts)
    if len(raw) > 100_000:
        raw = raw[:100_000] + "\n\n[Content truncated at 100k chars]"
    return raw


# ── 5. File I/O ────────────────────────────────────────────────────────────────

def save_raw_file(slug: str, content: str) -> Path:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    path = RAW_DIR / f"{today}-{slug}.md"
    path.write_text(content, encoding="utf-8")
    return path


def update_log(slug: str, topic: str, raw_path: Path) -> None:
    """Append a row to log.md (append-only)."""
    if not LOG_FILE.exists():
        return

    today = date.today().isoformat()
    row = (
        f"| {today} | agent.py: \"{trunc(topic, 55)}\" | "
        f"`{raw_path.relative_to(VAULT_ROOT)}` (created) | "
        f"Auto: HN + YouTube raw data collected (no analysis) |"
    )

    text = LOG_FILE.read_text(encoding="utf-8")
    anchor = "\n---\n\n_Add a row here"
    if anchor in text:
        text = text.replace(anchor, f"\n{row}{anchor}", 1)
    else:
        text = text.rstrip() + f"\n{row}\n"

    LOG_FILE.write_text(text, encoding="utf-8")


def update_hot(topic: str, raw_path: Path) -> None:
    """Overwrite hot.md with current session context (500-char limit)."""
    today = date.today().isoformat()
    content = (
        f"# Hot Context\n\n"
        f"_500-char max. Overwrite completely each session._\n\n"
        f"**Last updated:** {today}\n\n"
        f"agent.py collected raw data for: \"{topic}\". "
        f"Saved to {raw_path.name}. "
        f"Run: claude code on this file to generate analysis."
    )
    HOT_FILE.write_text(content[:540], encoding="utf-8")


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Research collector: HN + YouTube (+ Reddit) → raw markdown in raw/.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  python agent.py "problems developers face with AI tools"
  python agent.py "KZ accounting software gaps" --no-youtube
  python agent.py "vibe coding security" --hn-limit 20
        """,
    )
    parser.add_argument("topic", help="Research topic in quotes")
    parser.add_argument("--reddit-limit", type=int, default=20, metavar="N",
                        help="Max Reddit posts to collect (default: 20)")
    parser.add_argument("--hn-limit", type=int, default=50, metavar="N",
                        help="Max HN stories/comments to fetch per search (default: 50)")
    parser.add_argument("--yt-limit", type=int, default=7, metavar="N",
                        help="Max YouTube videos to attempt (default: 7)")
    parser.add_argument("--no-reddit", action="store_true", help="Skip Reddit")
    parser.add_argument("--no-hn", action="store_true", help="Skip Hacker News")
    parser.add_argument("--no-youtube", action="store_true", help="Skip YouTube")
    args = parser.parse_args()

    # Load .env from vault root (for optional Reddit credentials)
    load_dotenv(VAULT_ROOT / ".env")

    topic = args.topic.strip()
    if not topic:
        sys.exit("Error: topic cannot be empty.")

    slug = slugify(topic)

    banner("RESEARCH COLLECTOR")
    print(f"  Topic  : {topic}")
    print(f"  Slug   : {slug}")
    print(f"  Vault  : {VAULT_ROOT}")

    # ── Step 1: Collect ────────────────────────────────────────────────────────
    banner("STEP 1 / 2 — Collecting data")

    reddit: list[dict] = []
    reddit_source = "Reddit"
    if not args.no_reddit:
        if os.environ.get("REDDIT_CLIENT_ID"):
            reddit = search_reddit(topic, args.reddit_limit)
            reddit_source = "Reddit (PRAW)"
        else:
            print("  [reddit] no credentials — using public JSON API")
            reddit = search_reddit_public(topic)
            reddit_source = "Reddit (public API)"

    hn_stories, hn_comments = ([], []) if args.no_hn else search_hackernews(topic, args.hn_limit)
    yt = [] if args.no_youtube else search_youtube(topic, args.yt_limit)

    total = len(reddit) + len(hn_stories) + len(hn_comments) + len(yt)
    print(
        f"\n  Total  : {total} items  "
        f"({reddit_source}: {len(reddit)}, HN stories: {len(hn_stories)}, "
        f"HN comments: {len(hn_comments)}, YouTube: {len(yt)})"
    )

    if total == 0:
        print("\n  No data collected. Check internet connection.")
        sys.exit(1)

    # ── Step 2: Save raw markdown ──────────────────────────────────────────────
    banner("STEP 2 / 2 — Saving raw data")
    raw_md = build_raw_markdown(topic, reddit, hn_stories, hn_comments, yt, reddit_source)
    raw_path = save_raw_file(slug, raw_md)
    update_log(slug, topic, raw_path)
    update_hot(topic, raw_path)

    banner("DONE")
    print(f"  raw file  →  {raw_path.relative_to(VAULT_ROOT)}")
    print(f"  log.md    →  updated")
    print(f"  hot.md    →  updated")
    print(f"\n  Next: open Claude Code and run /startup on {raw_path.name}\n")


if __name__ == "__main__":
    main()
