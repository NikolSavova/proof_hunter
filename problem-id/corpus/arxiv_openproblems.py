"""High-volume ingester: arXiv papers with "open problem(s)" in the title.

Captures the field-specific "N open problems in X" genre + single "Open Problem:" papers
across all our home + adjacent fields via the arXiv API. Compilation papers (plural title)
are tagged so a later pass can expand them into individual problems.

Usage:
    python corpus/arxiv_openproblems.py                 # all categories
    python corpus/arxiv_openproblems.py --cats math.CO  # one category
    python corpus/arxiv_openproblems.py --per 30        # max results per category
"""
from __future__ import annotations
import argparse, pathlib, sys, time
import requests, feedparser

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import common  # noqa: E402

SOURCE = "arxiv-openproblem"
API = "http://export.arxiv.org/api/query"
# category -> our field label (scope §2)
CATS = {
    "math.CO": "combinatorics", "math.NT": "number-theory", "math.PR": "probability",
    "math.MG": "discrete-geometry", "math.OC": "optimization", "math.FA": "functional-analysis",
    "cs.CC": "complexity", "cs.IT": "information-theory", "cs.LG": "machine-learning-theory",
    "stat.ML": "machine-learning-theory", "quant-ph": "quantum-information",
    "cond-mat.stat-mech": "statistical-mechanics", "math.AG": "algebraic-geometry",
}

def fetch_category(cat: str, per: int) -> list:
    params = {"search_query": f'cat:{cat} AND ti:"open problem"',
              "start": 0, "max_results": per,
              "sortBy": "submittedDate", "sortOrder": "descending"}
    try:
        r = requests.get(API, params=params, timeout=40,
                         headers={"User-Agent": "problem-id research pipeline"})
        r.raise_for_status()
    except Exception as e:
        print(f"  ! {cat} query failed: {e}"); return []
    return feedparser.parse(r.text).entries

def ingest(cats=None, per=40) -> int:
    con = common.db()
    cats = cats or list(CATS)
    n = 0
    for cat in cats:
        field = CATS.get(cat, cat)
        entries = fetch_category(cat, per)
        print(f"[arxiv] {cat}: {len(entries)} open-problem papers")
        for e in entries:
            arxiv_id = e.id.rsplit("/", 1)[-1]
            title = e.title.replace("\n", " ").strip()
            is_compilation = "open problems" in title.lower()  # plural -> a list of problems
            year = int(e.published[:4]) if getattr(e, "published", "") else None
            common.upsert(con, {
                "id": f"{SOURCE}:{arxiv_id}",
                "source": SOURCE,
                "source_url": e.link,
                "title": title,
                "statement": f"{title}\n\n{e.summary.strip()}"[:8000],
                "field": [field],
                "year_posted": year,
                "status_claimed": "open",
                "tags": (["tier-a", "low-saturation", "arxiv-openproblem"]
                         + (["compilation"] if is_compilation else ["single-problem"])),
                "stage": "ingested",
                "raw": {"arxiv_id": arxiv_id, "category": cat, "compilation": is_compilation},
            })
            n += 1
        time.sleep(3)  # arXiv API politeness
    print(f"[arxiv] ingested {n} open-problem papers (dedup by arxiv id on upsert) -> {common.DB_PATH}")
    return n

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--cats", nargs="*", default=None)
    ap.add_argument("--per", type=int, default=40)
    a = ap.parse_args()
    ingest(a.cats, a.per)
