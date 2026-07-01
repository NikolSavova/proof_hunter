"""Tier-A ingester: The Open Problems Project (TOPP) — computational / discrete geometry.

A hand-curated list maintained since ~2001 by Demaine, Mitchell & O'Rourke
(https://topp.openproblem.net/). ~75+ open problems in computational geometry, each on its own
page /pN with a Statement and a Status. Human-curated + format-siloed = low LLM saturation, and
squarely in the discrete-geometry / TCS sweet spot (Nikol's lane; strong Engine-B/certificate fit).

Enumerates /p1, /p2, ... until pages run out (stops after several consecutive misses).

Usage:
    python corpus/topp.py            # ingest all
    python corpus/topp.py --limit 5  # smoke test (first 5)
"""
from __future__ import annotations
import argparse, pathlib, re, sys, time
import requests
from bs4 import BeautifulSoup

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import common  # noqa: E402

SOURCE = "topp"
BASE = "https://topp.openproblem.net/p"
UA = {"User-Agent": "problem-id research pipeline"}
MISS_STOP = 5          # stop after this many consecutive 404s
HARD_CAP = 200         # safety bound on N
MIN_STATEMENT = 60     # mirror filter.py MIN_STATEMENT_CHARS


def parse_status(text: str) -> str:
    """Best-effort: pull the Status line and normalize to open/partially-solved/solved."""
    m = re.search(r"\bStatus\b\s*[:\-]?\s*(.{0,80})", text, re.IGNORECASE)
    s = (m.group(1) if m else "").lower()
    if "unsolved" in s or "open" in s:
        return "open"
    if "partial" in s:
        return "partially-solved"
    if "solved" in s:
        return "solved"
    return "open"   # TOPP default posture is open


def parse_problem(n: int) -> dict | None:
    url = f"{BASE}{n}"
    try:
        r = requests.get(url, timeout=30, headers=UA)
    except Exception as e:
        print(f"  ! p{n} fetch error: {e}"); return None
    if r.status_code == 404:
        return "MISS"  # sentinel
    if r.status_code != 200:
        print(f"  ! p{n} HTTP {r.status_code}"); return None
    soup = BeautifulSoup(r.text, "lxml")
    for s in soup.select("script, style"):
        s.decompose()
    raw_title = (soup.title.string if soup.title else f"Problem {n}").strip()
    # "TOPP: Problem 12: Point Set Diameter" -> "Point Set Diameter"
    title = re.sub(r"^TOPP:\s*Problem\s*\d+:\s*", "", raw_title).strip() or raw_title
    text = re.sub(r"\n{2,}", "\n", soup.get_text("\n")).strip()
    if len(text) < MIN_STATEMENT:
        return None
    status = parse_status(text)
    m = re.search(r"\b(19|20)\d{2}\b", text)
    year = int(m.group(0)) if m else None
    return {
        "id": f"{SOURCE}:p{n}",
        "source": SOURCE,
        "source_url": url,
        "title": title[:300],
        "statement": text[:8000],
        "field": ["discrete-geometry", "computational-geometry", "theoretical-cs"],
        "year_posted": year,
        "status_claimed": status,
        "tags": ["tier-a", "low-saturation", "discrete-geometry", "topp",
                 "human-curated", "single-problem"],
        "stage": "ingested",
        "raw": {"n": n, "status_raw": status},
    }


def ingest(limit=None) -> int:
    con = common.db()
    print(f"[topp] enumerating problems at {BASE}N ...")
    n, misses, added = 0, 0, 0
    i = 0
    while i < HARD_CAP and misses < MISS_STOP:
        i += 1
        rec = parse_problem(i)
        if rec == "MISS":
            misses += 1
            continue
        misses = 0
        if rec:
            common.upsert(con, rec); added += 1
            print(f"  + {rec['id']:12} [{rec['status_claimed']:16}] {rec['title'][:56]}")
            if limit and added >= limit:
                break
        time.sleep(1)  # politeness
    print(f"[topp] ingested {added} computational-geometry problems -> {common.DB_PATH}")
    return added


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None)
    a = ap.parse_args()
    ingest(a.limit)
