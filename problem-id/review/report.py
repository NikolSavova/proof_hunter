"""Stage-4 review helper: emit a ranked finalists table from the DB.

Usage:
    python review/report.py                 # top problems by composite -> stdout + review/finalists.md
    python review/report.py --stage triaged # only those that passed the cutoff
    python review/report.py --top 50
"""
from __future__ import annotations
import argparse, json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import common  # noqa: E402

def main(stage=None, top=50):
    con = common.db()
    q = "SELECT * FROM problems WHERE scores IS NOT NULL"
    if stage:
        q += f" AND stage='{stage}'"
    q += " ORDER BY composite DESC"
    rows = con.execute(q).fetchall()[:top]
    lines = [f"# Finalists — ranked by composite ({len(rows)} shown)\n"]
    lines.append("| # | comp | eng | source | problem | win-condition | flags |")
    lines.append("|---|------|-----|--------|---------|---------------|-------|")
    for i, r in enumerate(rows, 1):
        det = json.loads(r["detectors"] or "{}")
        flags = ",".join(k.split("_")[0] for k, v in det.items() if v) or "-"
        rest = (r["restatement"] or r["title"] or "").replace("|", "\\|")[:90]
        wc = (r["win_condition"] or "").replace("|", "\\|")[:60]
        lines.append(f"| {i} | {r['composite']} | {r['suggested_engine']} | {r['source']} "
                     f"| {rest} | {wc} | {flags} |")
    out = "\n".join(lines) + "\n"
    (pathlib.Path(__file__).parent / "finalists.md").write_text(out)
    print(out)
    # stage tally
    tally = con.execute("SELECT stage, COUNT(*) n FROM problems WHERE scores IS NOT NULL GROUP BY stage").fetchall()
    print("stage tallies:", {row["stage"]: row["n"] for row in tally})

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", default=None)
    ap.add_argument("--top", type=int, default=50)
    a = ap.parse_args()
    main(a.stage, a.top)
