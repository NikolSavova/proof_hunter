"""Tier-A ingester: IQOQI Vienna 'Open Quantum Problems' (oqp.iqoqi.oeaw.ac.at).

A curated, low-LLM-saturation list (Werner et al.) — our QIT alpha source.
Parses the 48-row listing table, then each detail page for the statement.

Usage:
    python corpus/iqoqi.py            # ingest all
    python corpus/iqoqi.py --limit 5  # smoke test
"""
from __future__ import annotations
import argparse, pathlib, re, sys, time
import requests
from bs4 import BeautifulSoup

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import common  # noqa: E402

LIST_URL = "https://oqp.iqoqi.oeaw.ac.at/open-quantum-problems"
HEADERS = {"User-Agent": "Mozilla/5.0 (problem-id research pipeline; contact: nikol)"}
SOURCE = "iqoqi-oqp"

def _get(url: str) -> str:
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.text

def _year(s: str) -> int | None:
    m = re.search(r"(19|20)\d{2}", s or "")
    return int(m.group(0)) if m else None

def parse_list(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "lxml")
    table = soup.find("table")
    rows = []
    if not table:
        return rows
    for tr in table.find_all("tr"):
        cells = tr.find_all(["td", "th"])
        if len(cells) < 5:
            continue
        link = tr.find("a", href=re.compile(r"oqp\.iqoqi\.oeaw\.ac\.at/[a-z0-9-]+/?$"))
        if not link:
            continue  # skips the header row (no problem link)
        texts = [c.get_text(" ", strip=True) for c in cells]
        nr = next((t for t in texts if t.strip().isdigit()), None)
        cats = texts[-1] if texts else ""
        # date columns are the YYYY/MM/DD-looking cells
        dates = [t for t in texts if re.search(r"\d{4}\s*/\s*\d{1,2}", t)]
        rows.append({
            "nr": nr,
            "title": link.get_text(" ", strip=True),
            "url": link["href"].rstrip("/") + "/",
            "date_posted": dates[0] if len(dates) >= 1 else "",
            "last_progress": dates[1] if len(dates) >= 2 else "",
            "categories": cats,
        })
    return rows

def parse_detail(html: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    # exact-class match first; the broad regex was matching a tiny wrapper div.
    node = (soup.find("div", class_="entry-content")
            or soup.find("div", class_="post-content")
            or soup.find("article") or soup.find("main"))
    if not node:
        return ""
    for bad in node.find_all(["script", "style", "nav", "footer", "form"]):
        bad.decompose()
    text = node.get_text("\n", strip=True)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text[:8000]

def ingest(limit: int | None = None) -> int:
    con = common.db()
    rows = parse_list(_get(LIST_URL))
    print(f"[iqoqi] listing rows parsed: {len(rows)}")
    if limit:
        rows = rows[:limit]
    n = 0
    for row in rows:
        try:
            statement = parse_detail(_get(row["url"]))
        except Exception as e:  # be resilient; record what we have
            statement = ""
            print(f"  ! detail fetch failed {row['url']}: {e}")
        pid = f"{SOURCE}:{row['nr'] or row['url'].rstrip('/').rsplit('/',1)[-1]}"
        common.upsert(con, {
            "id": pid,
            "source": SOURCE,
            "source_url": row["url"],
            "title": row["title"],
            "statement": statement,
            "field": ["quantum-information"],
            "year_posted": _year(row["date_posted"]),
            "last_progress": row["last_progress"],
            "status_claimed": "open",      # the list is, by construction, open problems
            "tags": ["curated-list", "low-saturation", "tier-a"],
            "stage": "ingested",
            "raw": {"categories": row["categories"], "nr": row["nr"]},
        })
        n += 1
        print(f"  + {pid}  {row['title'][:60]}  ({len(statement)} chars)")
        time.sleep(0.8)  # be polite to a small academic server
    print(f"[iqoqi] ingested {n} problems -> {common.DB_PATH}")
    return n

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None)
    ingest(ap.parse_args().limit)
