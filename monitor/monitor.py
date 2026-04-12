#!/usr/bin/env python3
"""
Tech Monitor: Hacker News + Reddit + Twitter → Telegram
Runs every hour via GitHub Actions. Sends viral tech/AI content.
"""

import asyncio
import json
import os
import requests
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR   = Path(__file__).parent
SEEN_FILE    = SCRIPT_DIR / "seen.json"
COOKIES_FILE = SCRIPT_DIR / "twitter_cookies.json"

TELEGRAM_TOKEN    = os.environ.get("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT_ID  = os.environ.get("TELEGRAM_CHAT_ID", "")
TWITTER_USERNAME  = os.environ.get("TWITTER_USERNAME", "")
TWITTER_EMAIL     = os.environ.get("TWITTER_EMAIL", "")
TWITTER_PASSWORD  = os.environ.get("TWITTER_PASSWORD", "")

# --- Thresholds (tune these if you get too many / too few notifications) ---
HN_MIN_SCORE       = 150    # HN points
REDDIT_MIN_UPVOTES = 300    # Reddit upvotes
TWITTER_MIN_LIKES  = 1500   # Twitter likes

REDDIT_SUBS = [
    "MachineLearning",
    "LocalLLaMA",
    "artificial",
    "singularity",
    "programming",
    "ChatGPT",
    "OpenAI",
]

TWITTER_QUERIES = [
    "AI LLM",
    "Claude Anthropic",
    "open source model",
    "agentic AI",
    "vibe coding",
]

# ---------------------------------------------------------------------------

def load_seen() -> dict:
    if SEEN_FILE.exists():
        try:
            return json.loads(SEEN_FILE.read_text())
        except Exception:
            pass
    return {"hn": [], "reddit": [], "twitter": []}

def save_seen(seen: dict):
    seen["hn"]      = seen["hn"][-500:]
    seen["reddit"]  = seen["reddit"][-500:]
    seen["twitter"] = seen["twitter"][-500:]
    SEEN_FILE.write_text(json.dumps(seen, indent=2))

def send_telegram(text: str):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print(f"  [Telegram stub] {text[:80]}")
        return
    try:
        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": text,
                "parse_mode": "HTML",
                "disable_web_page_preview": False,
            },
            timeout=10,
        )
    except Exception as e:
        print(f"  Telegram error: {e}")

# --- Hacker News --------------------------------------------------------

def fetch_hn(seen_ids: list) -> list:
    results = []
    try:
        top_ids = requests.get(
            "https://hacker-news.firebaseio.com/v0/topstories.json",
            timeout=10,
        ).json()[:50]

        for item_id in top_ids:
            if str(item_id) in seen_ids:
                continue
            try:
                item = requests.get(
                    f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json",
                    timeout=8,
                ).json()
                if (
                    item
                    and item.get("type") == "story"
                    and item.get("score", 0) >= HN_MIN_SCORE
                ):
                    results.append({
                        "id":       str(item_id),
                        "title":    item.get("title", ""),
                        "url":      item.get("url") or f"https://news.ycombinator.com/item?id={item_id}",
                        "score":    item["score"],
                        "comments": item.get("descendants", 0),
                    })
            except Exception:
                continue
    except Exception as e:
        print(f"  HN error: {e}")
    return results

# --- Reddit -------------------------------------------------------------

def fetch_reddit(seen_ids: list) -> list:
    results = []
    headers = {"User-Agent": "StartupResearch-Monitor/1.0 (personal project)"}
    for sub in REDDIT_SUBS:
        try:
            data = requests.get(
                f"https://www.reddit.com/r/{sub}/hot.json?limit=10",
                headers=headers,
                timeout=10,
            ).json()
            for post in data["data"]["children"]:
                p = post["data"]
                pid = p["id"]
                if pid in seen_ids or p.get("stickied"):
                    continue
                if p.get("ups", 0) >= REDDIT_MIN_UPVOTES:
                    results.append({
                        "id":        pid,
                        "title":     p["title"],
                        "url":       f"https://reddit.com{p['permalink']}",
                        "upvotes":   p["ups"],
                        "subreddit": sub,
                    })
        except Exception as e:
            print(f"  Reddit r/{sub} error: {e}")
    return results

# --- Twitter (twikit) ---------------------------------------------------

async def _twitter_async(seen_ids: list) -> list:
    results = []
    if not TWITTER_USERNAME or not TWITTER_PASSWORD:
        print("  Twitter credentials not set — skipping.")
        return results

    try:
        from twikit import Client
    except ImportError:
        print("  twikit not installed — skipping Twitter.")
        return results

    client = Client("en-US")

    # Restore saved cookies to avoid logging in every hour
    if COOKIES_FILE.exists():
        try:
            client.load_cookies(str(COOKIES_FILE))
            print("  Loaded Twitter cookies.")
        except Exception:
            print("  Cookies invalid — re-logging in.")
            COOKIES_FILE.unlink(missing_ok=True)

    if not COOKIES_FILE.exists():
        try:
            await client.login(
                auth_info_1=TWITTER_USERNAME,
                auth_info_2=TWITTER_EMAIL,
                password=TWITTER_PASSWORD,
            )
            client.save_cookies(str(COOKIES_FILE))
            print("  Logged in and saved cookies.")
        except Exception as e:
            print(f"  Twitter login failed: {e}")
            return results

    for query in TWITTER_QUERIES[:3]:   # max 3 queries to stay under rate limit
        try:
            tweets = await client.search_tweet(query, product="Top", count=10)
            for tweet in tweets:
                tid   = str(tweet.id)
                likes = getattr(tweet, "favorite_count", 0) or 0
                if tid in seen_ids or likes < TWITTER_MIN_LIKES:
                    continue
                author = ""
                if tweet.user:
                    author = getattr(tweet.user, "screen_name", "") or ""
                results.append({
                    "id":       tid,
                    "text":     (tweet.text or "")[:280],
                    "url":      f"https://x.com/i/web/status/{tid}",
                    "likes":    likes,
                    "retweets": getattr(tweet, "retweet_count", 0) or 0,
                    "author":   author,
                    "query":    query,
                })
        except Exception as e:
            print(f"  Twitter query '{query}' error: {e}")

    return results

def fetch_twitter(seen_ids: list) -> list:
    return asyncio.run(_twitter_async(seen_ids))

# --- Main ---------------------------------------------------------------

def main():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"\n=== Tech Monitor {now} ===\n")

    seen     = load_seen()
    new_items = []

    hn_items = fetch_hn(seen["hn"])
    print(f"HN:      {len(hn_items)} new")
    for item in hn_items:
        seen["hn"].append(item["id"])
        new_items.append(("hn", item))

    reddit_items = fetch_reddit(seen["reddit"])
    print(f"Reddit:  {len(reddit_items)} new")
    for item in reddit_items:
        seen["reddit"].append(item["id"])
        new_items.append(("reddit", item))

    twitter_items = fetch_twitter(seen["twitter"])
    print(f"Twitter: {len(twitter_items)} new")
    for item in twitter_items:
        seen["twitter"].append(item["id"])
        new_items.append(("twitter", item))

    # Send — max 15 per run to avoid flooding your Telegram
    sent = 0
    for source, item in new_items:
        if sent >= 15:
            break

        if source == "hn":
            msg = (
                f"🔥 <b>Hacker News</b>\n"
                f"<b>{item['title']}</b>\n"
                f"⭐ {item['score']} pts · 💬 {item['comments']} comments\n"
                f"{item['url']}"
            )
        elif source == "reddit":
            msg = (
                f"⬆️ <b>r/{item['subreddit']}</b>\n"
                f"<b>{item['title']}</b>\n"
                f"⭐ {item['upvotes']:,} upvotes\n"
                f"{item['url']}"
            )
        else:
            msg = (
                f"🐦 <b>@{item['author']}</b>\n"
                f"{item['text']}\n"
                f"❤️ {item['likes']:,} · 🔁 {item['retweets']:,}\n"
                f"{item['url']}"
            )

        send_telegram(msg)
        sent += 1

    print(f"\nSent {sent} notifications.")
    save_seen(seen)

if __name__ == "__main__":
    main()
