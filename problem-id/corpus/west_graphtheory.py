"""Tier-A ingester: Douglas B. West's "Problems in Graph Theory and Combinatorics".

A curated, low-saturation list (dwest.web.illinois.edu/openp) of named graph-theory /
combinatorics conjectures, each on its own HTML page (statement + originators + motivation).
Exactly our combinatorics/graph-theory sweet spot. Scrape the index, then each problem page.

Usage:
    python corpus/west_graphtheory.py            # ingest all
    python corpus/west_graphtheory.py --limit 5  # smoke test
"""
from __future__ import annotations
import argparse, pathlib, re, sys, time
import requests
from bs4 import BeautifulSoup

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import common  # noqa: E402

SOURCE = "west-graphtheory"
INDEX = "https://dwest.web.illinois.edu/openp/"
# index links that are navigation/glossary, not problems:
SKIP = {"gloss.html", "../igt/notat.html", "notat.html"}

def problem_links() -> list[str]:
    r = requests.get(INDEX, timeout=30, headers={"User-Agent": "problem-id research pipeline"})
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "lxml")
    seen, out = set(), []
    for a in soup.find_all("a", href=True):
        h = a["href"].strip()
        if h.endswith(".html") and not h.startswith("http") and h not in SKIP and h not in seen:
            seen.add(h); out.append(h)
    return out

def parse_problem(page: str) -> dict | None:
    url = INDEX + page
    try:
        r = requests.get(url, timeout=30, headers={"User-Agent": "problem-id research pipeline"})
        r.raise_for_status()
    except Exception as e:
        print(f"  ! {page} fetch failed: {e}"); return None
    soup = BeautifulSoup(r.text, "lxml")
    for s in soup.select("script, style"):
        s.decompose()
    title = (soup.title.string if soup.title else page).strip().strip('"')
    text = re.sub(r"\n{2,}", "\n", soup.get_text("\n")).strip()
    # year is usually in the first line as "Name/1972" or "(1994)"
    m = re.search(r"\b(19|20)\d{2}\b", text[:200])
    year = int(m.group(0)) if m else None
    if len(text) < common_min():
        return None
    return {
        "id": f"{SOURCE}:{page[:-5]}",          # drop ".html"
        "source": SOURCE,
        "source_url": url,
        "title": title[:300],
        "statement": text[:8000],
        "field": ["graph-theory", "combinatorics"],
        "year_posted": year,
        "status_claimed": "open",
        "tags": ["tier-a", "low-saturation", "graph-theory", "west", "single-problem"],
        "stage": "ingested",
        "raw": {"page": page},
    }

def common_min() -> int:
    return 60  # mirror filter.py MIN_STATEMENT_CHARS

def ingest(limit=None) -> int:
    con = common.db()
    pages = problem_links()
    if limit:
        pages = pages[:limit]
    print(f"[west] {len(pages)} problem pages from {INDEX}")
    n = 0
    for page in pages:
        rec = parse_problem(page)
        if rec:
            common.upsert(con, rec); n += 1
            print(f"  + {rec['id']:28} {rec['title'][:60]}")
        time.sleep(1)  # politeness
    print(f"[west] ingested {n} graph-theory problems -> {common.DB_PATH}")
    return n

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None)
    a = ap.parse_args()
    ingest(a.limit)
