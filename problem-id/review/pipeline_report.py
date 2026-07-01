"""Pipeline report — an at-a-glance dashboard of the whole funnel.

Reads top-to-bottom as a story:
  SOURCES   — databases ingested (done) vs backlog (pending / blocked).
  FUNNEL    — the narrowing pipeline: how many problems survive each screening gate, and where
              the bottleneck is (how many are still waiting to be screened).
  PHASE II  — deep-pass verdicts (GO / MAYBE / NO-GO) + the proof engines each finalist will run
              through (mostly not yet built — they light up as we tag solve attempts).

Adaptable: SOURCE_REGISTRY (top) lists sources we intend to do so blocked/pending ones show with
zero rows; PROOF_METHODS wires each engine to a real DB column/tag so counts appear automatically.

Usage:
    python review/pipeline_report.py            # the dashboard
    python review/pipeline_report.py --detail    # + full source × stage matrix
    python review/pipeline_report.py --source kourovka
"""
from __future__ import annotations
import argparse, json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import common  # noqa: E402

# ---- registries (edit as the project grows) ------------------------------------------------------
SOURCE_REGISTRY = [
    # key (== DB source)   short   display name                          status
    ("erdos",              "erdos",    "Erdős problems",                 "done"),
    ("arxiv-openproblem",  "arxiv",    "arXiv open-problem papers",      "done"),
    ("opg",                "opg",      "Open Problem Garden",            "done"),
    ("topp",               "topp",     "The Open Problems Project",      "done"),
    ("colt-openproblem",   "colt",     "COLT open-problem track",        "done"),
    ("west-graphtheory",   "west",     "West — Graph Theory",            "done"),
    ("iqoqi-oqp",          "iqoqi",    "IQOQI Open Quantum Problems",    "done"),
    ("kourovka",           "kourovka", "Kourovka Notebook (≥2014)",      "done"),
    ("dagstuhl",           "dagstuhl", "Dagstuhl Reports",               "done"),
    # backlog (not in DB)
    ("guy-bmp",            "",  "Guy NT + Brass–Moser–Pach",   "blocked · copyright"),
    ("hannover-qi",        "",  "Hannover OpenQIProblemsWiki", "blocked · unreachable"),
    ("kourovka-old",       "",  "Kourovka Notebook (<2014)",   "pending · older issues"),
    ("oeis",               "",  "OEIS open-conjecture entries","pending"),
    ("kirby",              "",  "Kirby's list (low-dim top.)", "pending"),
    ("formal-conjectures", "",  "DeepMind formal-conjectures", "pending"),
]

PROOF_METHODS = [
    ("Engine A — LLM lemma/extension", "tag:engineA-attempted"),
    ("Engine B — evolutionary/SAT",    "tag:engineB-attempted"),
    ("Lean formalization",             "col:formalized"),
    ("Verified artifact / arXiv-ready","tag:verified"),
]

# Rough $/call by model, for the spend estimate (edit as billing reality shifts). Filter is free
# (deterministic, no API). Triage is cheap bulk; kill-search (web+reasoning) and deep-pass are the
# expensive ones — the whole point of the SPEND column is to make that visible.
RATE = {"gpt-5-mini": 0.002, "gpt-5.5 + web": 0.30, "gpt-5.5": 0.10}

BAR, EMPTY = "█", "░"


def bar(n, total, width=22):
    if total <= 0 or n <= 0:
        return ""
    return BAR * max(1, round(width * n / total))


def cover(done, elig, width=18):
    """Fixed-width coverage bar (filled = screened fraction of what's eligible)."""
    if elig <= 0:
        return " " * width
    f = max(1, round(width * done / elig)) if done else 0
    f = min(f, width)
    return BAR * f + EMPTY * (width - f)


def deeppass_rec(blob):
    try:
        rec = json.loads(blob).get("one_week_recommendation", "").lower()
    except Exception:
        return None
    return {"go": "GO", "maybe": "MAYBE", "no-go": "NO-GO", "nogo": "NO-GO"}.get(rec)


def wrap_join(chunks, indent, width=64):
    lines, cur = [], ""
    for ch in chunks:
        if cur and len(cur) + len(ch) + 2 > width:
            lines.append(cur); cur = ""
        cur += (ch if not cur else "  " + ch)
    if cur:
        lines.append(cur)
    return ("\n" + indent).join(lines)


def run(source_filter=None, detail=False):
    con = common.db()
    where, args = ((" WHERE source=?", (source_filter,)) if source_filter else ("", ()))

    def c(cond):
        q = f"SELECT COUNT(*) FROM problems{where}" + (" AND " if where else " WHERE ") + cond
        return con.execute(q, args).fetchone()[0]

    total = con.execute(f"SELECT COUNT(*) FROM problems{where}", args).fetchone()[0]
    db_src = dict(con.execute(
        f"SELECT source, COUNT(*) FROM problems{where} GROUP BY source", args).fetchall())

    # deep-pass verdicts
    recs = {"GO": 0, "MAYBE": 0, "NO-GO": 0}
    dq = f"SELECT deeppass FROM problems{where}" + (" AND" if where else " WHERE") + " deeppass IS NOT NULL"
    for (blob,) in con.execute(dq, args):
        r = deeppass_rec(blob)
        if r:
            recs[r] += 1

    n_final = c("stage='finalist'")
    W = 62
    print("━" * W)
    print("  PROOF HUNTER — pipeline dashboard")
    bits = [f"{total:,} problems", f"{sum(1 for k in db_src)} sources",
            f"{n_final} finalists", f"{recs['GO']} GO"]
    print("  " + "   ·   ".join(bits))
    print("━" * W)

    # ---------- SOURCES ----------
    print("\n  SOURCES")
    done = [f"{sh}·{db_src.get(k,0)}" for k, sh, _, st in SOURCE_REGISTRY if st == "done" and db_src.get(k)]
    pend = [nm for k, sh, nm, st in SOURCE_REGISTRY if st.startswith("pending")]
    block = [f"{nm} ({st.split('·',1)[1].strip()})" for k, sh, nm, st in SOURCE_REGISTRY if st.startswith("blocked")]
    print("    ✓ ingested  " + wrap_join(done, " " * 16))
    if pend:
        print("    ⋯ pending   " + wrap_join(pend, " " * 16))
    if block:
        print("    ✗ blocked   " + wrap_join(block, " " * 16))

    # ---------- SCREENING & SPEND (the hero) ----------
    # Each gate: how many we've SCREENED (processed) vs how many are still WAITING, plus the model
    # and rough $ spent — so the expensive stages (kill-search, deep-pass) and their backlog pop out.
    pending_filter = c("stage='ingested'")
    dropped_filter = c("stage IN ('rejected','duplicate')")
    low_score = c("stage='filtered'")
    queued_ks = c("stage='triaged'")
    red = c("stage='deep-rejected'")
    filter_done = total - pending_filter
    triage_done = c("composite IS NOT NULL")
    triage_wait = c("stage='prefiltered'")
    ks_done = c("killsearch IS NOT NULL")
    dp_done = c("deeppass IS NOT NULL")
    dp_wait = c("stage='finalist' AND deeppass IS NULL")

    # (label, model, done, waiting)  — model None == free/deterministic
    gates = [
        ("① Filter",      None,            filter_done, pending_filter),
        ("② Triage",      "gpt-5-mini",    triage_done, triage_wait),
        ("③ Kill-search", "gpt-5.5 + web", ks_done,     queued_ks),
        ("④ Deep-pass",   "gpt-5.5",       dp_done,     dp_wait),
    ]
    print("\n  SCREENING & SPEND")
    print("    " + f"{'gate':<13} {'model':<14} {'$':<4} {'coverage':<18}  done / waiting")
    print("    " + "─" * 55)
    spend = {}
    for label, model, done, wait in gates:
        elig = done + wait
        cost = "—" if not model else ("$" if RATE.get(model, 0) < 0.05 else "$$$")
        est = done * RATE.get(model, 0) if model else 0
        if model:
            spend[label] = est
        print(f"    {label:<13} {(model or 'rules + dedup'):<14} {cost:<4} "
              f"{cover(done, elig)}  {done:>5} / {wait:<5}")
    paid = sum(spend.values())
    print(f"\n    paid-model calls:  {triage_done:,} triage ($)  ·  {ks_done} kill-search ($$$)  "
          f"·  {dp_done} deep-pass ($$$)")
    print(f"    ≈ spend (rough):   triage ${spend['② Triage']:.0f}  ·  kill-search ${spend['③ Kill-search']:.0f}"
          f"  ·  deep-pass ${spend['④ Deep-pass']:.0f}   →  ~${paid:.0f} total on GPT")

    # ---------- OUTCOMES (compact funnel result) ----------
    print("\n  OUTCOMES")
    print(f"    kept {total-pending_filter-dropped_filter-low_score:,} of {total:,}"
          f"  →  {n_final} finalists  →  GO {recs['GO']} · MAYBE {recs['MAYBE']} · NO-GO {recs['NO-GO']}")
    print(f"    dropped along the way:  {dropped_filter} filter · {low_score} low-score · {red} kill-searched-out")

    # ---------- BY SOURCE (compact) ----------
    fin_by = dict(con.execute(
        f"SELECT source, COUNT(*) FROM problems{where}"
        + (" AND" if where else " WHERE") + " stage='finalist' GROUP BY source", args).fetchall())
    print("\n  BY SOURCE" + " " * 12 + "total   finalists")
    for src in sorted(db_src, key=lambda s: (-fin_by.get(s, 0), -db_src[s])):
        f = fin_by.get(src, 0)
        note = ""
        if f == 0:
            ing = con.execute("SELECT COUNT(*) FROM problems WHERE source=? AND stage='ingested'", (src,)).fetchone()[0]
            tri = con.execute("SELECT COUNT(*) FROM problems WHERE source=? AND stage='triaged'", (src,)).fetchone()[0]
            if ing:
                note = "awaiting filter/triage"
            elif tri:
                note = "awaiting kill-search"
        print(f"    {src:<20}{db_src[src]:>5}   {f:>7}   {note}")

    # ---------- optional full matrix ----------
    if detail:
        print("\n  DETAIL — source × stage")
        stages = ["ingested", "prefiltered", "rejected", "duplicate", "filtered",
                  "triaged", "deep-rejected", "finalist"]
        mat = {}
        for s, st, n in con.execute(
                f"SELECT source, stage, COUNT(*) FROM problems{where} GROUP BY source, stage", args):
            mat[(s, st)] = n
        hdr = "    " + f"{'source':<20}" + "".join(f"{st[:6]:>8}" for st in stages)
        print(hdr)
        for src in sorted(db_src, key=lambda s: -db_src[s]):
            print("    " + f"{src:<20}" + "".join(f"{mat.get((src,st),'') or '':>8}" for st in stages))

    # ---------- PHASE II ----------
    print("\n  PHASE II — proof engines")
    for name, tracked in PROOF_METHODS:
        kind, key = tracked.split(":", 1)
        n = (c(f"{key} IS NOT NULL") if kind == "col"
             else con.execute("SELECT COUNT(*) FROM problems WHERE tags LIKE ?", (f'%{key}%',)).fetchone()[0])
        dot = "●" if n else "○"
        print(f"    {dot} {name:<34} {n if n else 'planned'}")
    print("━" * W)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default=None, help="focus a single source")
    ap.add_argument("--brief", "--compact", dest="brief", action="store_true",
                    help="hide the full source × stage matrix (shown by default)")
    # --detail/--detailed are now the default; kept as accepted no-ops for compatibility
    ap.add_argument("--detail", "--detailed", dest="_detail", action="store_true", help=argparse.SUPPRESS)
    a = ap.parse_args()
    run(a.source, detail=not a.brief)
