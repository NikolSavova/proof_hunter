"""Tier-A ingester: COLT 'Open Problem' track via PMLR.

The Conference on Learning Theory runs an annual open-problem session whose papers
are short, precise, self-contained, and LOW-saturation — purpose-built for our funnel.
We harvest every paper whose title starts with "Open Problem:" across COLT volumes.

Usage:
    python corpus/colt_pmlr.py                  # default years
    python corpus/colt_pmlr.py --years 2025 2024
    python corpus/colt_pmlr.py --limit 4        # smoke test (first N open-problems found)
"""
from __future__ import annotations
import argparse, pathlib, re, sys, time
import requests
from bs4 import BeautifulSoup

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import common  # noqa: E402

HEADERS = {"User-Agent": "Mozilla/5.0 (problem-id research pipeline; contact: nikol)"}
SOURCE = "colt-openproblem"

# COLT year -> PMLR volume. (Open-problem track is reliably present from ~2015 on.)
VOLUMES = {2025: "v291", 2024: "v247", 2023: "v195", 2022: "v178", 2021: "v134",
           2020: "v125", 2019: "v99", 2018: "v75", 2017: "v65", 2016: "v49", 2015: "v40"}
DEFAULT_YEARS = [2025, 2024, 2023, 2022, 2021, 2020, 2019]

def _get(url: str) -> str | None:
    try:
        r = requests.get(url, headers=HEADERS, timeout=30)
        r.raise_for_status()
        return r.text
    except Exception as e:
        print(f"  ! fetch failed {url}: {e}")
        return None

def open_problems_in_volume(vol: str) -> list[dict]:
    html = _get(f"https://proceedings.mlr.press/{vol}/")
    if not html:
        return []
    soup = BeautifulSoup(html, "lxml")
    out = []
    for div in soup.find_all("div", class_="paper"):
        t = div.find("p", class_="title")
        if not t or not t.get_text(strip=True).lower().startswith("open problem"):
            continue
        links = div.find("p", class_="links")
        abs_url = next((a["href"] for a in links.find_all("a")
                        if a["href"].endswith(".html")), None) if links else None
        details = div.find("p", class_="details")
        out.append({"title": t.get_text(" ", strip=True),
                    "abs_url": abs_url,
                    "authors": details.get_text(" ", strip=True) if details else ""})
    return out

def fetch_abstract(abs_url: str) -> str:
    html = _get(abs_url)
    if not html:
        return ""
    node = BeautifulSoup(html, "lxml").select_one("#abstract, div.abstract")
    return node.get_text(" ", strip=True)[:8000] if node else ""

def ingest(years=None, limit=None) -> int:
    con = common.db()
    years = years or DEFAULT_YEARS
    n = 0
    for year in years:
        vol = VOLUMES.get(year)
        if not vol:
            print(f"[colt] no volume mapping for {year}, skipping"); continue
        problems = open_problems_in_volume(vol)
        print(f"[colt] {year} ({vol}): {len(problems)} open-problem papers")
        for p in problems:
            if limit and n >= limit:
                break
            slug = re.sub(r"\.html$", "", (p["abs_url"] or "").rsplit("/", 1)[-1]) or p["title"][:30]
            statement = fetch_abstract(p["abs_url"]) if p["abs_url"] else ""
            common.upsert(con, {
                "id": f"{SOURCE}:{slug}",
                "source": SOURCE,
                "source_url": p["abs_url"] or f"https://proceedings.mlr.press/{vol}/",
                "title": p["title"],
                "statement": f"{p['title']}\nAuthors: {p['authors']}\n\n{statement}",
                "field": ["machine-learning-theory"],
                "year_posted": year,
                "status_claimed": "open",
                "tags": ["curated-list", "low-saturation", "tier-a", "colt-open-problem"],
                "stage": "ingested",
                "raw": {"authors": p["authors"], "volume": vol},
            })
            n += 1
            print(f"  + {SOURCE}:{slug}  {p['title'][:62]}  ({len(statement)} chars)")
            time.sleep(0.5)
    print(f"[colt] ingested {n} open problems -> {common.DB_PATH}")
    return n

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--years", type=int, nargs="*", default=None)
    ap.add_argument("--limit", type=int, default=None)
    a = ap.parse_args()
    ingest(a.years, a.limit)
