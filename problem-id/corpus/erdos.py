"""High-volume ingester: erdosproblems.com (Thomas Bloom's database, ~1000+ problems).

Tier-B (rising LLM-saturation — frontier labs sweep these), but a large, clean, often
self-certifying corpus. We enumerate /<n>, detect the status banner, and ingest ONLY
problems that are NOT already solved/disproved (the Erdősgate-cheap-guard).

Usage:
    python corpus/erdos.py --max 1100         # full sweep
    python corpus/erdos.py --range 700 720    # a slice
    python corpus/erdos.py --limit 5          # smoke test (first N open ones found)
"""
from __future__ import annotations
import argparse, pathlib, re, sys, time
import requests
from bs4 import BeautifulSoup

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import common  # noqa: E402

HEADERS = {"User-Agent": "Mozilla/5.0 (problem-id research pipeline; contact: nikol)"}
SOURCE = "erdos"
# The page banner is the FIRST word: OPEN / PROVED / DISPROVED / SOLVED.
# (Must read the first token only — the OPEN banner text itself contains "resolved".)
SOLVED_BANNERS = {"PROVED", "DISPROVED", "SOLVED"}

def parse_problem(html: str) -> dict | None:
    soup = BeautifulSoup(html, "lxml")
    box = soup.find("div", class_="problem-text")
    if not box:
        return None
    text = box.get_text(" ", strip=True)
    add = soup.find("div", class_="problem-additional-text")
    add_text = add.get_text(" ", strip=True) if add else ""
    m0 = re.match(r"\s*([A-Za-z]+)", text)
    banner = (m0.group(1).upper() if m0 else "")
    solved = banner in SOLVED_BANNERS
    prize = None
    m = re.search(r"\$(\d[\d,]*)", text)
    if m:
        prize = m.group(0)
    return {"statement": (text + ("\n\n" + add_text if add_text else ""))[:8000],
            "solved": solved, "prize": prize}

def ingest(max_n=1100, rng=None, limit=None) -> int:
    con = common.db()
    nums = range(rng[0], rng[1] + 1) if rng else range(1, max_n + 1)
    n_open = n_solved = n_missing = 0
    for i in nums:
        if limit and n_open >= limit:
            break
        try:
            r = requests.get(f"https://www.erdosproblems.com/{i}", headers=HEADERS, timeout=20)
            if r.status_code == 404:
                n_missing += 1; continue
            r.raise_for_status()
        except Exception as e:
            print(f"  ! /{i} fetch failed: {e}"); continue
        prob = parse_problem(r.text)
        if not prob:
            n_missing += 1
        elif prob["solved"]:
            n_solved += 1     # skip already-solved (Erdősgate-cheap-guard)
        else:
            n_open += 1
            tags = ["curated-list", "tier-b", "erdos"] + (["has-prize"] if prob["prize"] else [])
            common.upsert(con, {
                "id": f"{SOURCE}:{i}",
                "source": SOURCE,
                "source_url": f"https://www.erdosproblems.com/{i}",
                "title": f"Erdős Problem #{i}",
                "statement": prob["statement"],
                "field": ["combinatorics", "number-theory"],  # broad; triage re-assigns
                "status_claimed": "open",
                "tags": tags,
                "stage": "ingested",
                "raw": {"prize": prob["prize"], "number": i},
            })
            if n_open % 50 == 0:
                print(f"  ... {n_open} open ingested (at #{i})")
        time.sleep(0.3)  # be polite
    print(f"[erdos] open ingested: {n_open} | skipped solved: {n_solved} | missing/404: {n_missing}")
    return n_open

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=1100)
    ap.add_argument("--range", type=int, nargs=2, default=None)
    ap.add_argument("--limit", type=int, default=None)
    a = ap.parse_args()
    ingest(a.max, a.range, a.limit)
