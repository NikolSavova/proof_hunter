"""Stage-1.5 — research-grade gate for compilation-expanded children.

The compilation-expansion scope filter (corpus/expand_compilations.py) is per-paper but, at
low reasoning effort, lets through applied-engineering / recreational / benchmark-meta /
deep-machinery surveys whose extracted "problems" then score highly on self_certifying +
llm_saturation_inv despite not being research-grade open problems for our team.

This gate re-judges each PARENT paper once (cheap, title+abstract only — no re-fetch) against a
strict rubric, and REJECTS all children of papers that fail. Concentrating the judgment at the
parent level is both efficient (~150 calls, not ~1300) and correct (the noise is whole-paper:
a wireless survey or a 13th-century arithmetic list is uniformly out).

Idempotent: stores the verdict in the parent's raw.research_grade_gate; re-runs skip judged
parents unless --recheck. Rejected children get stage='rejected', drop_reason='gate: ...'.

Usage:
    python triage/research_grade_gate.py --dry     # judge + preview, no rejects
    python triage/research_grade_gate.py           # judge and reject failing children
    python triage/research_grade_gate.py --recheck # re-judge already-judged parents
"""
from __future__ import annotations
import argparse, json, pathlib, sys, time
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import common  # noqa: E402

MODEL = "gpt-5-mini"

SCHEMA = {
    "name": "research_grade_gate",
    "strict": True,
    "schema": {
        "type": "object", "additionalProperties": False,
        "properties": {
            "keep": {"type": "boolean"},
            "category": {"type": "string", "enum": [
                "research-grade-in-scope", "recreational-or-historical", "benchmark-or-meta",
                "applied-engineering", "deep-machinery-excluded", "out-of-scope-other"]},
            "reason": {"type": "string"},
        },
        "required": ["keep", "category", "reason"],
    },
}

def system_prompt(rubric: dict) -> str:
    s = rubric["scope"]
    return (
        "You judge whether a survey / 'open problems' PAPER is a source of RESEARCH-GRADE open "
        "mathematics problems for a team (Oxford pure-math undergrad + MIT physics/ML grad) hunting a "
        "modest but genuinely-new, verifiable, publishable result in ~1 week.\n\n"
        f"IN SCOPE (keep=true): core {s['core']}; adjacent {s['adjacent']}. The paper must pose real, "
        "currently-open RESEARCH problems/conjectures by working mathematicians.\n\n"
        "An elementary / olympiad-FLAVOURED statement is NOT a defect — simple-to-state OPEN problems "
        "(e.g. Erdős-style) are top targets. Reject for being CLOSED, not for being simple.\n\n"
        "REJECT (keep=false) if the paper is primarily:\n"
        "- recreational-or-historical: problems posed as puzzles/curiosities whose answers are known or "
        "readily findable, or historical lists whose entries are already solved (NOT merely elementary "
        "problems that happen to be open — keep those);\n"
        "- benchmark-or-meta: AI/LLM benchmark or evaluation collections, 'test-time learning', "
        "verifier-design tasks, ML-evaluation harnesses;\n"
        "- applied-engineering: wireless/6G/networking, UAVs, applied deep learning / reinforcement "
        "learning systems, federated learning, data mining, hardware, biology, control engineering;\n"
        f"- deep-machinery-excluded: {s['exclude_unless_self_certifying']} and similar (algebraic "
        "geometry, operator algebras / von Neumann factors, geometric topology, hard PDE) UNLESS the "
        "problems are concretely self-certifying;\n"
        "- out-of-scope-other: anything else outside the fields above.\n\n"
        "Judge the PAPER as a whole by its title + abstract. Output ONLY the schema."
    )

def judge(client, rubric, parent) -> dict:
    user = (f"PAPER TITLE: {parent['title']}\nFIELD (ingest guess): {parent['field']}\n\n"
            f"ABSTRACT / TEXT:\n{(parent['statement'] or '')[:3000]}")
    kwargs = dict(model=MODEL,
                  messages=[{"role": "system", "content": system_prompt(rubric)},
                            {"role": "user", "content": user}],
                  response_format={"type": "json_schema", "json_schema": SCHEMA},
                  max_completion_tokens=1500)
    last = None
    for attempt in range(4):
        try:
            try:
                resp = client.chat.completions.create(reasoning_effort="medium", **kwargs)
            except TypeError:
                resp = client.chat.completions.create(**kwargs)
            return json.loads(resp.choices[0].message.content)
        except Exception as e:
            last = e
            if attempt < 3: time.sleep(3 * (attempt + 1))
    raise last

def run(dry=False, recheck=False, workers=6):
    con = common.db()
    rubric = common.load_rubric()
    client = common.openai_client()
    # distinct parent ids that have expanded children
    pids = [r["pid"] for r in con.execute(
        "SELECT DISTINCT json_extract(raw,'$.parent_id') pid FROM problems "
        "WHERE tags LIKE '%expanded-child%' AND json_extract(raw,'$.parent_id') IS NOT NULL")]
    parents = [con.execute("SELECT * FROM problems WHERE id=?", (pid,)).fetchone() for pid in pids]
    parents = [p for p in parents if p]
    if not recheck:
        parents = [p for p in parents if "research_grade_gate" not in (p["raw"] or "")]
    print(f"[gate] judging {len(parents)} parent papers ({MODEL}, medium, workers={workers}, dry={dry})")

    def work(p): return p, judge(client, rubric, p)
    results = []
    from concurrent.futures import ThreadPoolExecutor, as_completed
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(work, p): p for p in parents}
        for fut in as_completed(futs):
            try: results.append(fut.result())
            except Exception as e:
                p = futs[fut]; print(f"  ! {p['id']} gate failed: {repr(e)[:90]}")

    kept = dropped = rejected_children = 0
    for p, v in results:
        praw = json.loads(p["raw"] or "{}"); praw["research_grade_gate"] = v
        kids = con.execute("SELECT id FROM problems WHERE json_extract(raw,'$.parent_id')=?", (p["id"],)).fetchall()
        if v["keep"]:
            kept += 1
        else:
            dropped += 1
            print(f"  DROP [{v['category']}] {p['id'].split(':')[-1]:14} {p['title'][:50]} -> {len(kids)} kids ({v['reason'][:50]})")
            if not dry:
                for k in kids:
                    con.execute("UPDATE problems SET stage='rejected', drop_reason=? WHERE id=?",
                                (f"gate: {v['category']}", k["id"]))
                rejected_children += len(kids)
        if not dry:
            con.execute("UPDATE problems SET raw=? WHERE id=?", (json.dumps(praw), p["id"]))
    if not dry:
        con.commit()
    print(f"[gate] {'(dry) ' if dry else ''}kept {kept} parents, dropped {dropped} parents "
          f"-> {'would reject' if dry else 'rejected'} {rejected_children} children")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--recheck", action="store_true")
    ap.add_argument("--workers", type=int, default=6)
    a = ap.parse_args()
    run(a.dry, a.recheck, a.workers)
