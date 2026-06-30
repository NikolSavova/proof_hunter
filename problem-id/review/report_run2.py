"""Run-2 reporter — emit ONLY the newly-kill-searched finalists to NEW files.

Non-destructive by design: never touches review/finalists.md or finalists_detailed.md (run-1).
Writes review/finalists_run2.md (terse table) + finalists_run2_detailed.md (full dossier),
containing only finalists whose id is NOT in the prior-kill-search snapshot (i.e. this run's).

Usage:
    python review/report_run2.py
    python review/report_run2.py --snapshot /path/prior_ks_ids.txt --include-red
"""
from __future__ import annotations
import argparse, json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import common  # noqa: E402

HERE = pathlib.Path(__file__).parent
DEFAULT_SNAP = "/private/tmp/claude-501/-Users-nikolsavova-Documents-GitHub-proof-hunter/" \
               "f79ab8cf-7c64-4abf-bc11-548592adad3a/scratchpad/prior_ks_ids.txt"

def load_prior(snap):
    p = pathlib.Path(snap)
    return set(l.strip() for l in p.read_text().splitlines() if l.strip()) if p.exists() else set()

def main(snapshot, include_red=False):
    con = common.db()
    prior = load_prior(snapshot)
    # this run's results = have a killsearch verdict AND were not already kill-searched in run-1
    rows = con.execute("SELECT * FROM problems WHERE killsearch IS NOT NULL ORDER BY composite DESC").fetchall()
    new = [r for r in rows if r["id"] not in prior]
    finalists = [r for r in new if r["stage"] == "finalist"]
    reds = [r for r in new if r["stage"] == "deep-rejected"]
    keep = finalists + (reds if include_red else [])
    keep.sort(key=lambda r: r["composite"] or 0, reverse=True)

    # --- terse table ---
    t = [f"# Finalists — RUN 2 (diversified corpus, {len(finalists)} finalists of {len(new)} kill-searched)\n",
         "_New finalists only. Run-1 dossier is preserved in finalists.md / finalists_detailed.md "
         "(and backups finalists_run1*.md). Nothing from run-1 is included or altered here._\n",
         "| # | verdict | comp | conf | source | problem | closest prior |",
         "|---|---------|------|------|--------|---------|---------------|"]
    for i, r in enumerate(keep, 1):
        ks = json.loads(r["killsearch"])
        rest = (r["restatement"] or r["title"] or "").replace("|", "\\|")[:80]
        cp = (ks["closest_prior"] or "").replace("|", "\\|")[:50]
        t.append(f"| {i} | {ks['verdict'].upper()} | {r['composite']} | {ks['confidence']} "
                 f"| {r['source']} | {rest} | {cp} |")
    (HERE / "finalists_run2.md").write_text("\n".join(t) + "\n")

    # --- full dossier ---
    d = [f"# Vetted Finalists — RUN 2 full kill-search dossier\n",
         f"_{len(finalists)} finalists (verdict green/amber) from the diversified corpus, "
         f"kill-searched by gpt-5.5 + web. Run-1 dossier untouched in finalists_detailed.md._\n"]
    for i, r in enumerate(keep, 1):
        ks = json.loads(r["killsearch"])
        field = json.loads(r["field"] or "[]")
        det = json.loads(r["detectors"] or "{}")
        flags = ",".join(k for k, v in det.items() if v) or "-"
        d.append(f"\n## {i}. [{ks['verdict'].upper()}] {r['id']}  "
                 f"(composite {r['composite']}, confidence {ks['confidence']}, still_open={ks['still_open']})")
        d.append(f"**Source:** {r['source']} · **Field:** {field} · **Flags:** {flags} · "
                 f"[{r['source_url']}]({r['source_url']})\n")
        d.append(f"**Problem:** {r['restatement'] or r['title']}\n")
        d.append(f"**Win condition:** {r['win_condition']}\n")
        d.append(f"**Closest prior / novelty check:** {ks['closest_prior']}\n")
        d.append(f"**Novelty notes / residual risk:** {ks['novelty_notes']}\n")
        d.append(f"**LLM-saturation:** {ks['llm_saturation_note']}\n")
        d.append(f"**Attack sketch:** {ks['attack_sketch']}\n")
    (HERE / "finalists_run2_detailed.md").write_text("\n".join(d) + "\n")

    print(f"[report_run2] {len(finalists)} finalists ({len(reds)} red-killed) of {len(new)} kill-searched")
    print(f"  -> {HERE/'finalists_run2.md'}")
    print(f"  -> {HERE/'finalists_run2_detailed.md'}")
    print("  (run-1 files untouched)")
    from collections import Counter
    print("  finalist source mix:", dict(Counter(r["source"] for r in finalists)))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--snapshot", default=DEFAULT_SNAP)
    ap.add_argument("--include-red", action="store_true")
    a = ap.parse_args()
    main(a.snapshot, a.include_red)
