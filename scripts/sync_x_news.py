#!/usr/bin/env python3
import html
import json
import os
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "_config.yml"
DATA_PATH = ROOT / "_data" / "x_news.json"

DEFAULT_INSTANCES = [
    "https://rsshub.rssforever.com",
    "https://rsshub.pseudoyu.com",
    "https://rsshub.in",
]


def read_handle() -> str:
    env_handle = os.environ.get("X_NEWS_HANDLE", "").strip().lstrip("@")
    if env_handle:
        return env_handle

    if CONFIG_PATH.exists():
        text = CONFIG_PATH.read_text(encoding="utf-8")
        match = re.search(r"twitter:\s*\"?([^\"\n]+)\"?", text)
        if match:
            return match.group(1).strip().lstrip("@")

    raise RuntimeError("Could not determine X handle from X_NEWS_HANDLE or _config.yml")


def candidate_feed_urls(handle: str):
    explicit = os.environ.get("X_NEWS_FEED_URL", "").strip()
    if explicit:
        return [explicit]

    encoded_handle = urllib.parse.quote(handle)
    urls = []
    for base in DEFAULT_INSTANCES:
        urls.append(f"{base}/twitter/user/{encoded_handle}")
        urls.append(f"{base}/x/user/{encoded_handle}")
    return urls


def clean_text(value: str) -> str:
    if not value:
        return ""
    value = html.unescape(value)
    value = re.sub(r"<br\s*/?>", " ", value, flags=re.I)
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def truncate_words(text: str, limit: int = 38) -> str:
    words = text.split()
    if len(words) <= limit:
        return text
    return " ".join(words[:limit]).rstrip(".,;:!?") + "…"


def parse_date(raw: str):
    if not raw:
        return None, ""
    try:
        dt = parsedate_to_datetime(raw)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        dt = dt.astimezone(timezone.utc)
        return dt.isoformat(), dt.strftime("%b %-d, %Y")
    except Exception:
        return "", raw


def fetch_feed(url: str):
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "TongLab News Sync/1.0 (+https://github.com/the-star-sea/TongLab)",
            "Accept": "application/rss+xml, application/xml, text/xml;q=0.9, */*;q=0.1",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = response.read()
    root = ET.fromstring(payload)
    return payload, root


def parse_items(root: ET.Element, handle: str, limit: int):
    channel = root.find("channel")
    if channel is None:
        raise RuntimeError("RSS feed did not contain a channel element")

    items = []
    for item in channel.findall("item")[:limit]:
        title = clean_text(item.findtext("title"))
        description = clean_text(item.findtext("description"))
        link = (item.findtext("link") or "").strip()
        published_iso, published_label = parse_date(item.findtext("pubDate") or "")

        summary = description or title
        if summary == title:
            summary = ""
        if summary:
            summary = truncate_words(summary)

        if not title:
            title = truncate_words(description or f"Latest post from @{handle}", 20)

        items.append(
            {
                "title": title,
                "summary": summary,
                "url": link,
                "published": published_iso,
                "published_label": published_label,
            }
        )

    source_title = clean_text(channel.findtext("title"))
    source_link = (channel.findtext("link") or f"https://x.com/{handle}").strip()
    return source_title, source_link, items


def main() -> int:
    handle = read_handle()
    max_items = int(os.environ.get("X_NEWS_MAX_ITEMS", "6"))
    existing_data = {}
    existing_items = []
    if DATA_PATH.exists():
        try:
            existing_data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
            existing_items = existing_data.get("items") or []
        except Exception:
            existing_data = {}
            existing_items = []

    errors = []

    for feed_url in candidate_feed_urls(handle):
        try:
            _, root = fetch_feed(feed_url)
            source_title, source_link, items = parse_items(root, handle, max_items)
            if not items and existing_items:
                raise RuntimeError("Feed returned zero items, keeping existing non-empty cache")

            now = datetime.now(timezone.utc)
            data = {
                "handle": handle,
                "profile_url": f"https://x.com/{handle}",
                "source": source_title or "X feed",
                "source_url": source_link,
                "last_synced": now.isoformat(),
                "last_synced_label": now.strftime("%b %-d, %Y %H:%M UTC"),
                "items": items,
            }
            DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
            DATA_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            print(f"Synced {len(items)} items from {feed_url}")
            return 0
        except Exception as exc:
            errors.append(f"{feed_url}: {exc}")

    if DATA_PATH.exists():
        print("Feed sync failed, keeping existing cached data.", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 0

    print("Feed sync failed and no cached data exists.", file=sys.stderr)
    for err in errors:
        print(f"  - {err}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
