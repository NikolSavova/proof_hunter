"""Deep pass — high-confidence vetting of the top finalists with gpt-5.5-pro + web search.

Runs AFTER the bulk kill-search, on the best few survivors only. A stronger model + a deeper
prompt: re-confirm genuine openness, give an explicit go/maybe/no-go for a 1-week attack, and
name the first concrete step. This is the de-risking read before committing Phase II.

NON-DESTRUCTIVE: writes ONLY to a NEW file (review/deeppass_run2.md). It does NOT write to the
DB — existing kill-search verdicts and stages are left exactly as they are. Results also append
to the file incrementally, so a long/interrupted run keeps partial progress.

Usage:
    python killsearch/deeppass.py --top 8                      # top-8 run-2 finalists by composite
    python killsearch/deeppass.py --ids arxiv-openproblem:..#3 # specific problems
    python killsearch/deeppass.py --top 8 --model gpt-5.5      # cheaper model if Pro is throttled
"""
from __future__ import annotations
import argparse, json, pathlib, sys, time
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import common  # noqa: E402
import killsearch  # reuse the robust background-response poller  # noqa: E402

MODEL = "gpt-5.5-pro"
OUT = pathlib.Path(__file__).resolve().parents[1] / "review" / "deeppass_run2.md"
SNAP = ("/private/tmp/claude-501/-Users-nikolsavova-Documents-GitHub-proof-hunter/"
        "f79ab8cf-7c64-4abf-bc11-548592adad3a/scratchpad/prior_ks_ids.txt")

SCHEMA = {
    "type": "object", "additionalProperties": False,
    "properties": {
        "still_open": {"type": "boolean"},
        "openness_confidence": {"type": "string", "enum": ["low", "medium", "high"]},
        "verdict": {"type": "string", "enum": ["green", "amber", "red"]},
        "closest_prior": {"type": "string"},
        "why_not_already_done": {"type": "string"},   # deeper: why is this still open?
        "one_week_recommendation": {"type": "string", "enum": ["go", "maybe", "no-go"]},
        "first_concrete_step": {"type": "string"},     # what to literally do on day 1
        "key_risk": {"type": "string"},
        "engine": {"type": "string", "enum": ["A", "B", "both"]},
    },
    "required": ["still_open", "openness_confidence", "verdict", "closest_prior",
                 "why_not_already_done", "one_week_recommendation", "first_concrete_step",
                 "key_risk", "engine"],
}

PROMPT = """You are a senior mathematician giving a GO/NO-GO read on whether a small AI-augmented \
team (Oxford pure-math undergrad + MIT physics/ML grad; tools: GPT-5.5-Pro, Claude Opus, OpenEvolve \
evolutionary search, SAT, Lean) could produce a NEW, verifiable, publishable result on this problem \
in ~1 WEEK. This is a higher-confidence second pass after a cheaper kill-search already marked it AMBER.

Use web search aggressively. Be decisive and concrete:
1. Re-confirm genuine openness — find the closest existing result; is the gap really still open, or \
derivable-on-sight from known work? (Erdősgate discipline: "listed as open" != unsolved.)
2. why_not_already_done: if it IS open, explain WHY it survived — what makes it non-trivial yet not hopeless.
3. one_week_recommendation: GO (clear self-certifying win achievable in a week), MAYBE (plausible but \
real risk), or NO-GO (too hard / likely already done / not self-certifying in a week). Earn a GO.
4. first_concrete_step: the literal Day-1 action (the SAT/MILP encoding, the lemma to draft, the \
evaluator to build). key_risk: the single thing most likely to sink it. engine: A (lemma/quant-extension) \
or B (search/construction) or both."""

def deep_one(client, model, prob):
    import openai
    user = (f"PROBLEM (id {prob['id']}, source {prob['source']}, {prob['source_url']})\n"
            f"TITLE: {prob['title']}\nRESTATEMENT: {prob['restatement']}\n"
            f"WIN CONDITION: {prob['win_condition']}\nPRIOR KILL-SEARCH NOTES: "
            f"{json.loads(prob['killsearch'] or '{}').get('novelty_notes','')}\n\n"
            f"FULL TEXT:\n{(prob['statement'] or '')[:3500]}")
    tool = {"type": "web_search", "search_context_size": "low"}
    for attempt in range(killsearch.MAX_RETRIES):
        try:
            resp = client.responses.create(
                model=model,
                input=[{"role": "developer", "content": PROMPT},
                       {"role": "user", "content": user}],
                tools=[tool], reasoning={"effort": "high"},
                text={"format": {"type": "json_schema", "name": "deeppass",
                                 "schema": SCHEMA, "strict": True}},
                background=True,
            )
            resp = killsearch._retrieve(client, resp.id)
            if resp.status == "completed":
                return json.loads(resp.output_text)
            err = getattr(resp, "error", None)
            if "rate_limit" in str(getattr(err, "code", "")) or "rate_limit" in str(err):
                w = 70 * (attempt + 1); print(f"    (TPM; wait {w}s)"); time.sleep(w); continue
            raise RuntimeError(f"response {resp.status}: {err}")
        except openai.RateLimitError:
            w = 70 * (attempt + 1); print(f"    (429 TPM; wait {w}s)"); time.sleep(w)
        except openai.APIConnectionError:
            w = 20 * (attempt + 1); print(f"    (conn; retry {w}s)"); time.sleep(w)
        except TypeError:
            tool = {"type": "web_search"}
    raise RuntimeError("deep_one: exhausted retries")

def select(con, ids, top):
    if ids:
        rows = [con.execute("SELECT * FROM problems WHERE id=?", (i,)).fetchone() for i in ids]
        return [r for r in rows if r]
    prior = set(l.strip() for l in open(SNAP)) if pathlib.Path(SNAP).exists() else set()
    rows = con.execute("SELECT * FROM problems WHERE stage='finalist' AND killsearch IS NOT NULL "
                       "ORDER BY composite DESC").fetchall()
    new = [r for r in rows if r["id"] not in prior]   # run-2 finalists only
    return new[:top]

def run(ids=None, top=8, model=MODEL):
    con = common.db()
    client = common.openai_client()
    rows = select(con, ids, top)
    print(f"[deeppass] {len(rows)} finalists -> {model} (web, high effort). Writing to {OUT.name} (no DB writes).")
    header = (f"# Deep pass — high-confidence GO/NO-GO on the top run-2 finalists\n\n"
              f"_Stronger model ({model}) + web search, high effort. A second read after the AMBER "
              f"kill-search. NON-DESTRUCTIVE: new file only; DB and all other dossiers untouched._\n")
    OUT.write_text(header)
    results = []
    for r in rows:
        prob = dict(r); t0 = time.time()
        try:
            dp = deep_one(client, model, prob)
        except Exception as e:
            print(f"  ! {r['id']} deep-pass failed: {repr(e)[:160]}"); continue
        results.append((r, dp))
        rec = (f"\n## [{dp['verdict'].upper()} · {dp['one_week_recommendation'].upper()}] {r['id']} "
               f"(composite {r['composite']}, openness conf {dp['openness_confidence']})\n"
               f"**Problem:** {r['restatement'] or r['title']}\n\n"
               f"**Win condition:** {r['win_condition']}\n\n"
               f"**Still open / closest prior:** open={dp['still_open']} — {dp['closest_prior']}\n\n"
               f"**Why not already done:** {dp['why_not_already_done']}\n\n"
               f"**1-week recommendation:** {dp['one_week_recommendation'].upper()} "
               f"(engine {dp['engine']})\n\n"
               f"**First concrete step:** {dp['first_concrete_step']}\n\n"
               f"**Key risk:** {dp['key_risk']}\n")
        with open(OUT, "a") as f:
            f.write(rec)
        print(f"  {r['id']}: {dp['verdict'].upper()}/{dp['one_week_recommendation'].upper()} "
              f"({time.time()-t0:.0f}s) eng={dp['engine']}  {dp['why_not_already_done'][:70]}")
        time.sleep(killsearch.INTER_CALL_SLEEP)
    # summary footer
    from collections import Counter
    rec = Counter(dp["one_week_recommendation"] for _, dp in results)
    with open(OUT, "a") as f:
        f.write(f"\n---\n_Summary: {dict(rec)} across {len(results)} problems._\n")
    print(f"[deeppass] done: {dict(rec)} -> {OUT}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids", nargs="*", default=None)
    ap.add_argument("--top", type=int, default=8)
    ap.add_argument("--model", default=MODEL)
    a = ap.parse_args()
    run(a.ids, a.top, a.model)
