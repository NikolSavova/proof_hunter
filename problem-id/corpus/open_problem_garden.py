"""Tier-A ingester: Open Problem Garden (openproblemgarden.org).

A community-curated wiki of open problems across graph theory, combinatorics, number theory,
algebra, geometry, logic, probability, analysis and TCS. Each problem is a human-written /op/<slug>
page (statement + importance + keywords + solved-marker). Community-curated + not arXiv/Wikipedia =
low LLM saturation; multi-field breadth spans both Nikol's and Sihao's lanes.

Strategy: crawl the topic/field category pages, collect the union of /op/<slug> links (deduped,
tracking which field(s) each came from), then fetch each problem page.

Usage:
    python corpus/open_problem_garden.py            # ingest all
    python corpus/open_problem_garden.py --limit 5  # smoke test (first 5 problems)
"""
from __future__ import annotations
import argparse, pathlib, re, sys, time
import requests
from bs4 import BeautifulSoup

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import common  # noqa: E402

SOURCE = "opg"
ROOT = "https://www.openproblemgarden.org"
UA = {"User-Agent": "problem-id research pipeline"}
MIN_STATEMENT = 60

# OPG is a community wiki and has accumulated game-cheat/generator spam pages. These tokens are
# high-precision spam signals that ~never appear in mathematics — deliberately NOT using math-
# colliding words like "free" (triangle-free), "generator" (group generators), or "spins" (quantum).
SPAM_TOKENS = {
    "cheats", "vbucks", "v_bucks", "robux", "pokecoin", "apk", "simoleons", "chrono_crystals",
    "gift_card", "tiktok", "instagram", "casino", "giveaway", "dealdash", "gardenscapes",
    "warframe", "genshin", "fortnite", "monopoly_go", "jurassic_world", "family_island",
    "hollywood_story", "dragon_ball", "dragon_city", "fire_kirin", "sims_freeplay",
    "call_of_duty", "mod_menu", "no_human_verification", "platinum_cheats", "coin_master",
}


def is_spam(slug: str, title: str, text: str) -> bool:
    blob = (slug + " " + (title or "") + " " + (text or "")[:500]).lower()
    return any(tok in blob for tok in SPAM_TOKENS)

# topic categories -> our field taxonomy (author/person categories are skipped)
CATEGORIES: dict[str, list[str]] = {
    "graph_theory": ["graph-theory"], "basic_graph_theory": ["graph-theory"],
    "algebraical_graph_theory": ["graph-theory"], "extremal_graph_theory": ["graph-theory"],
    "topological_graph_theory": ["graph-theory", "topology"], "directed_graphs": ["graph-theory"],
    "infinite_graphs": ["graph-theory"], "random_graphs": ["graph-theory", "probability"],
    "coloring": ["graph-theory"], "hypergraphs": ["graph-theory"],
    "graph_algorithms": ["graph-theory", "theoretical-cs"],
    "combinatorics": ["combinatorics"], "number_theory": ["number-theory"],
    "algebra": ["algebra"], "group_theory": ["group-theory"],
    "geometry": ["discrete-geometry"], "analysis": ["analysis"], "pdes": ["analysis"],
    "probability": ["probability"], "logic": ["logic"],
    "theoretical_computer_science": ["theoretical-cs"], "topology": ["topology"],
    "unsorted": [],
}


def get(url: str):
    try:
        r = requests.get(url, timeout=30, headers=UA)
        if r.status_code == 200:
            return r.text
        print(f"  ! {url} HTTP {r.status_code}")
    except Exception as e:
        print(f"  ! {url} error: {e}")
    return None


def collect_slugs() -> dict[str, set[str]]:
    """slug -> set of our-fields, gathered across all topic category pages."""
    slug_fields: dict[str, set[str]] = {}
    for cat, fields in CATEGORIES.items():
        html = get(f"{ROOT}/category/{cat}")
        if not html:
            continue
        found = set(re.findall(r'href="/op/([a-z0-9_./-]+)"', html))
        for s in found:
            slug_fields.setdefault(s, set()).update(fields)
        print(f"  [cat] {cat:32} {len(found)} problems")
        time.sleep(0.4)
    return slug_fields


def parse_problem(slug: str, fields: set[str]) -> dict | None:
    url = f"{ROOT}/op/{slug}"
    html = get(url)
    if not html:
        return None
    soup = BeautifulSoup(html, "lxml")
    for s in soup.select("script, style"):
        s.decompose()
    title = (soup.title.string if soup.title else slug)
    title = re.sub(r"\s*\|\s*Open Problem Garden\s*$", "", title).strip()
    text = re.sub(r"\n{3,}", "\n\n", soup.get_text("\n")).strip()
    if len(text) < MIN_STATEMENT:
        return None
    if is_spam(slug, title, text):
        print(f"  - SPAM skipped: {slug[:50]}")
        return None
    low = text.lower()
    solved = ("was solved" in low or "has been solved" in low or "this problem is solved" in low)
    m = re.search(r"\b(18|19|20)\d{2}\b", text)
    year = int(m.group(0)) if m else None
    flist = sorted(fields) if fields else ["combinatorics"]
    return {
        "id": f"{SOURCE}:{slug}",
        "source": SOURCE,
        "source_url": url,
        "title": title[:300],
        "statement": text[:8000],
        "field": flist,
        "year_posted": year,
        "status_claimed": "solved" if solved else "open",
        "tags": ["low-saturation", "open-problem-garden", "human-curated", "single-problem"] + flist,
        "stage": "ingested",
        "raw": {"slug": slug, "categories": flist},
    }


def ingest(limit=None) -> int:
    con = common.db()
    print(f"[opg] crawling {len(CATEGORIES)} topic categories at {ROOT} ...")
    slug_fields = collect_slugs()
    slugs = sorted(slug_fields)
    print(f"[opg] {len(slugs)} unique problems across categories")
    added = 0
    for slug in slugs:
        rec = parse_problem(slug, slug_fields[slug])
        if rec:
            common.upsert(con, rec); added += 1
            print(f"  + {rec['id'][:40]:40} [{rec['status_claimed']:6}] {','.join(rec['field'])}")
            if limit and added >= limit:
                break
        time.sleep(0.4)  # politeness
    print(f"[opg] ingested {added} problems -> {common.DB_PATH}")
    return added


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None)
    a = ap.parse_args()
    ingest(a.limit)
