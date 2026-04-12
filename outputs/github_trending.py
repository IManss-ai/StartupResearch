#!/usr/bin/env python3
"""
GitHub Trending CLI/AI/MCP Tool Scanner
Runs daily — saves results to outputs/YYYY-MM-DD-github-trending.md
"""

import requests
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

# --- Config ---
OUTPUT_DIR = Path(__file__).parent  # saves next to this script in outputs/
RESULTS_PER_PAGE = 100
MIN_STARS = 5  # ignore noise below this threshold

# Keywords that signal relevance to AI/CLI/MCP/orchestration
SIGNAL_KEYWORDS = [
    "cli", "command-line", "command line", "terminal",
    "mcp", "model context protocol", "model-context-protocol",
    "llm", "gpt", "claude", "anthropic", "openai", "gemini",
    "agent", "agentic", "ai", "copilot",
    "orchestration", "orchestrator", "workflow", "pipeline",
    "rag", "embedding", "vector",
    "framework", "toolkit", "devtool", "developer tool",
]

def yesterday_iso():
    d = datetime.now(timezone.utc) - timedelta(days=1)
    return d.strftime("%Y-%m-%d")

def fetch_trending(date_from: str) -> list[dict]:
    """Query GitHub Search API for repos created recently, sorted by stars."""
    url = "https://api.github.com/search/repositories"
    params = {
        "q": f"created:>{date_from} stars:>={MIN_STARS}",
        "sort": "stars",
        "order": "desc",
        "per_page": RESULTS_PER_PAGE,
    }
    headers = {"Accept": "application/vnd.github+json"}

    r = requests.get(url, params=params, headers=headers, timeout=15)
    r.raise_for_status()
    return r.json().get("items", [])

def is_relevant(repo: dict) -> bool:
    """Return True if the repo matches any signal keyword."""
    text = " ".join([
        (repo.get("description") or "").lower(),
        (repo.get("name") or "").lower(),
        " ".join(repo.get("topics", [])).lower(),
        (repo.get("language") or "").lower(),
    ])
    return any(kw in text for kw in SIGNAL_KEYWORDS)

def format_repo(repo: dict) -> str:
    name        = repo["full_name"]
    stars       = repo["stargazers_count"]
    desc        = repo.get("description") or "_no description_"
    topics      = ", ".join(repo.get("topics", [])) or "_none_"
    language    = repo.get("language") or "_unknown_"
    url         = repo["html_url"]
    return (
        f"### [{name}]({url})\n"
        f"- **Stars:** {stars:,}\n"
        f"- **Language:** {language}\n"
        f"- **Topics:** {topics}\n"
        f"- **Description:** {desc}\n"
    )

def main():
    today     = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    date_from = yesterday_iso()

    print(f"Fetching repos created after {date_from}...")
    all_repos = fetch_trending(date_from)
    print(f"  Total fetched: {len(all_repos)}")

    relevant = [r for r in all_repos if is_relevant(r)]
    print(f"  Relevant (AI/CLI/MCP): {len(relevant)}")

    # --- Build markdown output ---
    lines = [
        f"# GitHub Trending — {today}",
        f"",
        f"> Repos created after {date_from} · sorted by stars · filtered for AI/CLI/MCP/orchestration",
        f"",
        f"**Total scanned:** {len(all_repos)}  |  **Relevant:** {len(relevant)}",
        f"",
        f"---",
        f"",
    ]

    if relevant:
        for repo in relevant:
            lines.append(format_repo(repo))
            lines.append("")
    else:
        lines.append("_No relevant repos found today._")

    # --- Also include top 10 overall (regardless of filter) ---
    lines += [
        "---",
        "",
        "## Top 10 Overall (unfiltered)",
        "",
    ]
    for repo in all_repos[:10]:
        lines.append(format_repo(repo))
        lines.append("")

    output_path = OUTPUT_DIR / f"{today}-github-trending.md"
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  Saved to: {output_path}")

if __name__ == "__main__":
    main()
