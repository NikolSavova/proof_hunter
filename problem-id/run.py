"""End-to-end orchestrator for the problem-identification funnel.

Stages (each idempotent / resumable — only acts on its input stage):
    0 ingest (optional)  ->  1 filter  ->  2 triage  ->  3 kill-search  ->  4 report

Usage:
    python run.py                      # filter -> triage -> killsearch(top 50) -> report
    python run.py --ingest iqoqi colt  # also run those ingesters first
    python run.py --no-killsearch      # stop before the expensive Stage 3
    python run.py --top 50 --killsearch-model gpt-5.5-pro
"""
from __future__ import annotations
import argparse, importlib, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent
for sub in ("", "corpus", "triage", "killsearch", "review"):
    sys.path.insert(0, str(ROOT / sub))
import common  # noqa: E402
import filter as stage1          # noqa: E402  triage/filter.py
import score as stage2           # noqa: E402  triage/score.py
import killsearch as stage3      # noqa: E402  killsearch/killsearch.py
import report as stage4          # noqa: E402  review/report.py

def tally(con):
    return {r["stage"]: r["n"] for r in
            con.execute("SELECT stage,COUNT(*) n FROM problems GROUP BY stage ORDER BY stage")}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ingest", nargs="*", default=[], help="ingester module names in corpus/ (e.g. iqoqi colt_pmlr)")
    ap.add_argument("--top", type=int, default=50, help="finalist count for kill-search")
    ap.add_argument("--no-killsearch", action="store_true")
    ap.add_argument("--killsearch-model", default=stage3.MODEL)
    ap.add_argument("--ks-limit", type=int, default=None, help="cap kill-search calls (smoke test)")
    a = ap.parse_args()
    con = common.db()
    rubric = common.load_rubric()

    print("=== START ===  corpus:", tally(con))

    # Stage 0 — optional ingest
    for name in a.ingest:
        mod = importlib.import_module(name)  # corpus/ is on sys.path
        print(f"\n--- ingest: {name} ---")
        mod.ingest()

    # Stage 1 — cheap filter + dedup
    print("\n--- Stage 1: filter ---")
    stage1.run()

    # Stage 2 — triage
    print("\n--- Stage 2: triage ---")
    stage2.score_all()

    # floor-40 guard (locked rule)
    n_pass = con.execute("SELECT COUNT(*) FROM problems WHERE stage='triaged'").fetchone()[0]
    floor = rubric["thresholds"]["finalist_floor"]
    if n_pass < floor:
        print(f"\n[run] NOTE: {n_pass} passed triage (< floor {floor}). "
              f"Kill-search will still take the top by composite, but ingest more sources for a full finalist set.")

    # Stage 3 — kill-search (expensive; skippable)
    if not a.no_killsearch:
        print("\n--- Stage 3: kill-search ---")
        stage3.run(top=a.top, limit=a.ks_limit, model=a.killsearch_model)

    # Stage 4 — report finalists (green/amber survivors if Stage 3 ran, else triaged)
    print("\n--- Stage 4: report ---")
    final_stage = "finalist" if not a.no_killsearch else "triaged"
    stage4.main(stage=final_stage, top=max(a.top, 50))

    print("\n=== DONE ===  corpus:", tally(con))

if __name__ == "__main__":
    main()
