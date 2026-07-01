"""Tier-A ingester: Dagstuhl Reports — conference open-problem sessions.

Schloss Dagstuhl runs invitation-only research seminars; each publishes a "Dagstuhl Report"
(open-access, CC-BY, on DROPS) that often includes an **Open Problems** session — fresh, expert-
vouched problems posed at the workshop and rarely indexed anywhere else. Exactly the low-LLM-
saturation ∩ human-vouched-important intersection, and squarely in our TCS / combinatorics /
discrete-geometry / quantum lanes.

Pipeline (per report):
  1. enumerate DagRep volumes -> issues -> per-seminar PDFs + titles (DROPS entity pages);
  2. field-filter by seminar TITLE (theory/math keywords) so we don't download HCI/systems reports;
  3. download the PDF, extract text (pymupdf), isolate the "Open Problem(s)" section(s);
  4. LLM-extract each distinct posed problem (reuses expand_compilations' extractor + scope filter);
  5. upsert each as a child record `dagstuhl:<seminar>#<n>` (stage=ingested) for the normal funnel.

DagRep volume N == year 2010+N (vol 15 = 2025). Idempotent: children are upserted by id; re-runs
overwrite the same rows. Requires `pymupdf` (added to the venv 2026-07-01).

Usage:
    python corpus/dagstuhl.py --volumes 15 --limit 3     # smoke test (few seminars, one volume)
    python corpus/dagstuhl.py --volumes 13,14,15         # the bounded run (2023-2025)
    python corpus/dagstuhl.py --volumes 13,14,15 --dry   # preview extraction, no DB writes
"""
from __future__ import annotations
import argparse, pathlib, re, sys, time
from urllib.parse import urljoin
import requests
import fitz  # pymupdf

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import common  # noqa: E402
from corpus.expand_compilations import EXTRACT_SCHEMA, system_prompt, extract, MAX_TEXT_CHARS  # noqa: E402

SOURCE = "dagstuhl"
BASE = "https://drops.dagstuhl.de"
UA = {"User-Agent": "problem-id research pipeline"}
MAX_PROBLEMS = 30

# Only download reports whose TITLE looks like theory / discrete math / TCS / quantum (Dagstuhl is
# CS-wide; this skips HCI / systems / security / ML-applied where formal open-problem sections and
# our scope don't apply). The downstream "Open Problems section" test + the LLM scope filter do the
# rest, so this list only needs to be roughly right.
INCLUDE = re.compile(
    r"graph|combinat|geometr|discrete|coding|\bcodes?\b|complexity|algorithm|logic|number theor|"
    r"quantum|optimiz|probabilis|extremal|ramsey|matroid|\bsat\b|satisfiab|constraint|automata|"
    r"proof|comput geom|lattice|counting|enumerat|spectral|hypergraph|polynomial|algebra|"
    r"parameteriz|approximation|randomness|combinatorial|topolog|game theor|fdefinable|category",
    re.IGNORECASE,
)
SKIP_TITLE = re.compile(r"complete issue|front matter|table of contents", re.IGNORECASE)

# Headings that introduce an open-problem section inside a Dagstuhl report.
OPEN_HEAD = re.compile(
    r"(?im)^[ \t]*(?:\d+(?:\.\d+)*\.?\s*)?(open\s+problems?|open\s+questions?|"
    r"problem\s+session|collection\s+of\s+open\s+problems|list\s+of\s+open\s+problems)\b.*$"
)
SECTION_WINDOW = 6000   # chars to pull after each open-problem heading


def issue_links(volume: int) -> list[str]:
    r = requests.get(f"{BASE}/entities/volume/DagRep-volume-{volume}", timeout=40, headers=UA)
    r.raise_for_status()
    return sorted(set(re.findall(rf"/entities/issue/DagRep-volume-{volume}-issue-\d+", r.text)),
                  key=lambda s: int(s.rsplit("-", 1)[-1]))


def seminars_in_issue(issue_path: str) -> list[dict]:
    """Return [{title, seminar, pdf_url}] for the real seminar reports on an issue page."""
    r = requests.get(BASE + issue_path, timeout=40, headers=UA)
    r.raise_for_status()
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.text, "lxml")
    out = []
    for a in soup.find_all("a", href=True):
        if not re.search(r"/storage/.+DagRep.*\.pdf$", a["href"]):
            continue
        # climb to the container holding this item's descriptive text
        node, text = a, ""
        for _ in range(6):
            node = node.parent
            if node is None:
                break
            text = node.get_text(" ", strip=True)
            if len(text) > 30:
                break
        m = re.search(r"DagRep\.[\d.]+\s+(.+?)\s+\(Dagstuhl Seminar (\d{5})\)", text)
        if not m or SKIP_TITLE.search(text):
            continue
        out.append({"title": m.group(1).strip(), "seminar": m.group(2),
                    "pdf_url": urljoin(BASE, a["href"])})
    return out


def open_problem_text(pdf_bytes: bytes) -> str | None:
    """Extract text after each open-problem heading; None if the report has no such section."""
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    full = "\n".join(p.get_text() for p in doc)
    doc.close()
    heads = list(OPEN_HEAD.finditer(full))
    if not heads:
        return None
    blob, seen = [], set()
    for m in heads:
        s = m.start()
        if any(abs(s - t) < SECTION_WINDOW for t in seen):  # skip overlapping windows
            continue
        seen.add(s)
        blob.append(full[s:s + SECTION_WINDOW])
    text = "\n\n---\n\n".join(blob)
    return text[:MAX_TEXT_CHARS] if len(text.strip()) > 200 else None


def ingest(volumes, limit=None, workers=4, dry=False, effort="low") -> int:
    con = common.db()
    rubric = common.load_rubric()
    client = common.openai_client()

    # 1-2) enumerate + field-filter
    candidates = []
    for v in volumes:
        for iss in issue_links(v):
            for s in seminars_in_issue(iss):
                if INCLUDE.search(s["title"]):
                    s["volume"] = v
                    candidates.append(s)
            time.sleep(0.5)
    print(f"[dagstuhl] {len(candidates)} theory/math seminars in volumes {volumes} (title-filtered)")
    if limit:
        candidates = candidates[:limit]

    total = 0
    for s in candidates:
        try:
            pdf = requests.get(s["pdf_url"], timeout=90, headers=UA).content
            section = open_problem_text(pdf)
        except Exception as e:
            print(f"  ! {s['seminar']} fetch/parse failed: {repr(e)[:100]}")
            continue
        if not section:
            print(f"  - {s['seminar']} no open-problem section: {s['title'][:60]}")
            continue
        try:
            out = extract(client, rubric, f"Dagstuhl Seminar {s['seminar']}: {s['title']}", section, effort)
        except Exception as e:
            print(f"  ! {s['seminar']} extract failed: {repr(e)[:100]}")
            continue
        if not out.get("in_scope"):
            print(f"  · {s['seminar']} out-of-scope: {s['title'][:60]}")
            continue
        probs = [p for p in out["problems"] if p.get("still_open", True)][:MAX_PROBLEMS]
        year = 2010 + s["volume"]
        n = 0
        for i, p in enumerate(probs, 1):
            stmt = p["statement"].strip()
            if len(stmt) < 40:
                continue
            n += 1
            rec = {
                "id": f"{SOURCE}:{s['seminar']}#{i}",
                "source": SOURCE,
                "source_url": s["pdf_url"],
                "title": p["title"].strip()[:300],
                "statement": (f"{p['title'].strip()}\n\n{stmt}")[:8000],
                "field": p.get("field") or ["theoretical-cs"],
                "year_posted": year,
                "status_claimed": "open",
                "tags": ["tier-a", "low-saturation", "dagstuhl", "conference-open-problem",
                         "human-curated", "single-problem"],
                "stage": "ingested",
                "raw": {"seminar": s["seminar"], "volume": s["volume"],
                        "seminar_title": s["title"], "child_index": i},
            }
            if dry:
                print(f"    DRY {rec['id']:22} {rec['title'][:80]}")
            else:
                common.upsert(con, rec)
        total += n
        print(f"  + {s['seminar']} [{n} problems] {s['title'][:56]}")
    print(f"[dagstuhl] {'(dry) ' if dry else ''}extracted {total} open problems "
          f"from volumes {volumes} -> {common.DB_PATH}")
    return total


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--volumes", default="13,14,15", help="comma-separated DagRep volume numbers")
    ap.add_argument("--limit", type=int, default=None, help="cap seminars processed (smoke test)")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--effort", default="low", choices=["low", "medium", "high"])
    a = ap.parse_args()
    vols = [int(x) for x in a.volumes.split(",") if x.strip()]
    ingest(vols, a.limit, a.workers, a.dry, a.effort)
