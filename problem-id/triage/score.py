"""Stage-2 batch triage: score each ingested problem on the rubric with a cheap
model (gpt-5-mini), structured output. Composite + gates computed in code.

Usage:
    python triage/score.py --limit 2          # smoke test (spends a little API $)
    python triage/score.py                     # score all un-triaged
    python triage/score.py --recompute         # recompute composites from stored
                                               # scores after editing rubric.yaml (no API)
"""
from __future__ import annotations
import argparse, json, pathlib, sys, time
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import common  # noqa: E402

MODEL = "gpt-5-mini"
AXES = ["self_certifying", "llm_saturation_inv", "ai_tractability", "verifiability",
        "crowdedness_inv", "meaningfulness", "novelty_checkability", "one_week_shaped", "statability"]

SCHEMA = {
    "name": "triage",
    "strict": True,
    "schema": {
        "type": "object", "additionalProperties": False,
        "properties": {
            "restatement": {"type": "string"},
            "field": {"type": "array", "items": {"type": "string"}},
            "scores": {
                "type": "object", "additionalProperties": False,
                "properties": {a: {"type": "integer", "minimum": 1, "maximum": 5} for a in AXES},
                "required": AXES,
            },
            "detectors": {
                "type": "object", "additionalProperties": False,
                "properties": {k: {"type": "boolean"} for k in
                               ["quantitative_extension", "construction_target", "default_method_stalled"]},
                "required": ["quantitative_extension", "construction_target", "default_method_stalled"],
            },
            "win_condition": {"type": "string"},
            "suggested_engine": {"type": "string", "enum": ["A", "B", "both", "none"]},
            "one_line_rationale": {"type": "string"},
        },
        "required": ["restatement", "field", "scores", "detectors",
                     "win_condition", "suggested_engine", "one_line_rationale"],
    },
}

def system_prompt(rubric: dict) -> str:
    s = rubric["scope"]
    return (
        "You screen OPEN mathematics problems for a small AI-augmented team: an Oxford pure-math "
        "undergrad (logic/sets, number theory, Galois, graph theory, combinatorics, measure, probability) "
        "and an MIT physics grad (ML, CS, quantum information). Tools: GPT-5.5-Pro, Claude Opus, OpenEvolve "
        "(evolutionary program search for constructions/bounds), SAT solvers, Lean (formal verification). "
        "Goal: find problems where they could get a MODEST but genuinely-new, VERIFIABLE, publishable result "
        "in ~1 week.\n\n"
        "Score each axis 1-5 (5=best). Be skeptical and calibrated — MOST problems are a poor fit; reserve "
        "5s. Key axes:\n"
        "- self_certifying: success = an explicit object / certificate / Lean statement anyone can check "
        "(NOT 'experts agree'). Highest priority.\n"
        "- llm_saturation_inv: 5 if this problem/source is NOT being mechanically swept by frontier-lab LLM "
        "efforts; 1 if it is (e.g. famous Erdős problems, formal-conjectures repo targets).\n"
        "- ai_tractability: could a cross-domain lemma / a quantitative-extension / an evolutionary or SAT "
        "search plausibly crack it in ~1 week?\n"
        "- verifiability: Lean-formalizable / certificate / re-runnable evaluator.\n"
        "- crowdedness_inv: 5 if quietly open (no recent flurry of papers / hot seminars); 1 if mobbed.\n"
        "- meaningfulness, novelty_checkability, one_week_shaped, statability: per their names.\n\n"
        "detectors: quantitative_extension = a KNOWN qualitative/asymptotic theorem that lacks an explicit "
        "rate/constant (high-value template). construction_target = success is exhibiting an object beating "
        "a public record. default_method_stalled = long-open under ONE dominant technique.\n\n"
        f"Field scope (set field-fit accordingly). CORE: {s['core']}. ADJACENT (ok): {s['adjacent']}. "
        f"EXCLUDE unless clearly self-certifying & tractable: {s['exclude_unless_self_certifying']}.\n\n"
        "win_condition: state the concrete artifact that would = success, or exactly 'none' if there is no "
        "self-certifying/checkable success criterion. If the problem is RH / P!=NP / Millennium-class or "
        "otherwise hopeless in a week, set scores low and win_condition may still describe the ideal artifact.\n"
        "Output ONLY the JSON schema."
    )

def call(client, rubric, prob) -> dict:
    user = (f"TITLE: {prob['title']}\nSOURCE: {prob['source']}  ({prob['source_url']})\n"
            f"FIELD (ingest guess): {prob['field']}\nYEAR: {prob['year_posted']}  "
            f"LAST PROGRESS: {prob['last_progress']}\n\nPROBLEM TEXT:\n{prob['statement'] or '(none)'}")
    kwargs = dict(
        model=MODEL,
        messages=[{"role": "system", "content": system_prompt(rubric)},
                  {"role": "user", "content": user}],
        response_format={"type": "json_schema", "json_schema": SCHEMA},
        max_completion_tokens=4000,
    )
    try:
        resp = client.chat.completions.create(reasoning_effort="low", **kwargs)
    except TypeError:
        resp = client.chat.completions.create(**kwargs)
    return json.loads(resp.choices[0].message.content)

def famous_impossible(text: str) -> bool:
    t = (text or "").lower()
    return any(k in t for k in ["riemann hypothesis", "p versus np", "p vs np", "p != np",
                                "navier-stokes", "birch and swinnerton", "hodge conjecture",
                                "yang-mills", "twin prime conjecture"])

def score_all(limit=None, recompute=False, workers=8, rescore=False):
    con = common.db()
    rubric = common.load_rubric()
    if recompute:  # re-derive composites from stored scores after a weight edit; no API
        rows = con.execute("SELECT * FROM problems WHERE scores IS NOT NULL").fetchall()
        for r in rows:
            comp = common.composite_score(json.loads(r["scores"]),
                                          json.loads(r["detectors"] or "{}"), rubric)
            con.execute("UPDATE problems SET composite=? WHERE id=?", (comp, r["id"]))
        con.commit()
        print(f"[recompute] updated {len(rows)} composites")
        return

    client = common.openai_client()
    # consume Stage-1 output ('prefiltered'); also accept raw 'ingested' if filter wasn't run.
    # `scores IS NULL` is the hard idempotency guard: anything already scored is NEVER re-scored,
    # so re-running after the corpus grows only spends on genuinely-new problems. (Use --rescore to override.)
    cond = "stage IN ('prefiltered','ingested')" + ("" if rescore else " AND scores IS NULL")
    rows = con.execute(f"SELECT * FROM problems WHERE {cond} ORDER BY id").fetchall()
    if limit:
        rows = rows[:limit]
    cutoff = rubric["thresholds"]["stage2_composite_cutoff"]
    print(f"[score] {len(rows)} problems to triage with {MODEL} (cutoff {cutoff}, {workers} workers)")

    def persist(r, out):
        scores, detectors = out["scores"], out["detectors"]
        comp = common.composite_score(scores, detectors, rubric)
        wc = out["win_condition"].strip().lower()
        rejected = (rubric["gates"]["require_win_condition"] and wc in ("none", "", "n/a")) \
            or (rubric["gates"]["reject_if_famous_impossible"]
                and famous_impossible((r["statement"] or "") + " " + (r["title"] or "")))
        passed = (not rejected) and comp >= cutoff
        common.upsert(con, {
            "id": r["id"], "restatement": out["restatement"], "field": out["field"],
            "scores": scores, "detectors": detectors, "composite": comp,
            "win_condition": out["win_condition"], "suggested_engine": out["suggested_engine"],
            "attack_sketch": out["one_line_rationale"],
            "stage": "rejected" if rejected else ("triaged" if passed else "filtered"),
            "drop_reason": ("no-win-condition/famous-impossible" if rejected
                            else (None if passed else f"composite {comp} < {cutoff}")),
            "scored_at": time.time(),
        })
        flags = ",".join(k for k, v in detectors.items() if v) or "-"
        return (f"  {r['id']}: comp={comp:>4} eng={out['suggested_engine']:<4} "
                f"{'REJ' if rejected else ('PASS' if passed else 'cut')} [{flags}] {out['restatement'][:60]}")

    def work(r):
        prob = dict(r); prob["field"] = json.loads(r["field"] or "[]")
        return r, call(client, rubric, prob)

    done = 0
    if workers <= 1:
        for r in rows:
            try:
                _, out = work(r); print(persist(r, out))
            except Exception as e:
                print(f"  ! {r['id']} scoring failed: {repr(e)[:120]}")
            done += 1
    else:
        from concurrent.futures import ThreadPoolExecutor, as_completed
        with ThreadPoolExecutor(max_workers=workers) as ex:
            futs = {ex.submit(work, r): r for r in rows}
            for fut in as_completed(futs):  # DB writes happen here, in the main thread -> safe
                r = futs[fut]
                try:
                    _, out = fut.result(); line = persist(r, out)
                except Exception as e:
                    line = f"  ! {r['id']} scoring failed: {repr(e)[:120]}"
                done += 1
                if done % 10 == 0 or done == len(rows):
                    print(f"[{done}/{len(rows)}] {line}")
    # summary
    c = con.execute("SELECT stage, COUNT(*) n, ROUND(AVG(composite),2) avg FROM problems "
                    "WHERE scores IS NOT NULL GROUP BY stage").fetchall()
    print("[score] stage tallies:", {row["stage"]: (row["n"], row["avg"]) for row in c})

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--recompute", action="store_true")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--rescore", action="store_true", help="re-score even already-scored problems (off by default)")
    a = ap.parse_args()
    score_all(a.limit, a.recompute, a.workers, a.rescore)
