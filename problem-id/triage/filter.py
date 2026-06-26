"""Stage 1 — cheap, LLM-free pre-filter + dedup. Runs before Stage-2 triage.

At thousands-scale this is what stops us paying triage cost on garbage/duplicates.
- famous-impossible reject (title-level, conservative)
- too-short / empty statement reject
- cross-source dedup (normalized-title token Jaccard)

ingested -> prefiltered | rejected | duplicate

Usage:
    python triage/filter.py            # filter all 'ingested'
    python triage/filter.py --dry      # report only, no DB writes
"""
from __future__ import annotations
import argparse, pathlib, re, sys, time
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import common  # noqa: E402

FAMOUS = [
    "riemann hypothesis", "p versus np", "p vs np", "p = np", "p != np",
    "navier-stokes", "navier–stokes", "hodge conjecture", "yang-mills", "yang–mills",
    "birch and swinnerton", "mass gap", "goldbach", "collatz", "twin prime conjecture",
    "continuum hypothesis", "abc conjecture",
]
MIN_STATEMENT_CHARS = 60

def norm_tokens(s: str) -> set[str]:
    s = re.sub(r"[^a-z0-9 ]", " ", (s or "").lower())
    stop = {"the", "a", "an", "of", "for", "and", "or", "to", "in", "on", "is", "are",
            "problem", "open", "conjecture", "question", "with", "all", "every", "that"}
    return {t for t in s.split() if t and t not in stop and len(t) > 2}

def jaccard(a: set, b: set) -> float:
    return len(a & b) / len(a | b) if (a or b) else 0.0

def is_famous(title: str, statement: str) -> str | None:
    head = ((title or "") + " " + (statement or "")[:300]).lower()
    for f in FAMOUS:
        if f in head:
            return f
    return None

def run(dry=False):
    con = common.db()
    rows = con.execute("SELECT * FROM problems WHERE stage='ingested'").fetchall()
    print(f"[filter] {len(rows)} ingested problems")
    # existing non-rejected corpus to dedup against (so re-runs dedup vs the whole DB)
    kept = con.execute("SELECT id,title,restatement,statement FROM problems "
                       "WHERE stage IN ('prefiltered','triaged','filtered','finalist','deep')").fetchall()
    kept_tok = {r["id"]: norm_tokens((r["title"] or "") + " " + (r["restatement"] or "")) for r in kept}

    counts = {"prefiltered": 0, "rejected": 0, "duplicate": 0}
    for r in rows:
        title, statement = r["title"], r["statement"]
        fam = is_famous(title, statement)
        if fam:
            counts["rejected"] += 1
            if not dry:
                con.execute("UPDATE problems SET stage='rejected', drop_reason=? WHERE id=?",
                            (f"famous-impossible: {fam}", r["id"]))
            continue
        if len((statement or "").strip()) < MIN_STATEMENT_CHARS:
            counts["rejected"] += 1
            if not dry:
                con.execute("UPDATE problems SET stage='rejected', drop_reason='statement too short' WHERE id=?",
                            (r["id"],))
            continue
        tok = norm_tokens((title or "") + " " + (r["restatement"] or ""))
        dup_of = next((kid for kid, kt in kept_tok.items() if jaccard(tok, kt) >= 0.80), None)
        if dup_of:
            counts["duplicate"] += 1
            if not dry:
                con.execute("UPDATE problems SET stage='duplicate', drop_reason=? WHERE id=?",
                            (f"dup of {dup_of}", r["id"]))
            continue
        counts["prefiltered"] += 1
        kept_tok[r["id"]] = tok  # so later rows in THIS batch dedup against it too
        if not dry:
            con.execute("UPDATE problems SET stage='prefiltered' WHERE id=?", (r["id"],))
    if not dry:
        con.commit()
    print(f"[filter] {'(dry) ' if dry else ''}results: {counts}")
    return counts

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    run(ap.parse_args().dry)
