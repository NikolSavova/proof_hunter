"""Stage 3 — adversarial kill-search on the top finalists with GPT-5.5-Pro + live web search.

For each finalist: try HARD to prove it's already solved / the gap is closed (the Erdősgate
discipline), estimate LLM-saturation, sketch an attack. Verdict green/amber/red.

triaged -> finalist (green/amber) | deep-rejected (red)

Pro models run via the Responses API and force >= medium reasoning -> EXPENSIVE & slow
(~30-120s/call). Always cuts to the top-N finalists; never run on the whole corpus.

Usage:
    python killsearch/killsearch.py --limit 1                 # smoke test (one call)
    python killsearch/killsearch.py --top 50                  # the real run
    python killsearch/killsearch.py --model gpt-5.5 --top 50  # cheaper model
"""
from __future__ import annotations
import argparse, json, pathlib, sys, time
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import common  # noqa: E402

MODEL = "gpt-5.5-pro"
# gpt-5.5-pro TPM on this org is 200k and one Pro+web-search call can approach it, so:
SEARCH_CONTEXT = "low"   # bound how much web text gets pulled into context
INTER_CALL_SLEEP = 12    # seconds between calls to stay under TPM
MAX_RETRIES = 4          # backoff on 429 (TPM resets each minute, so ~60s waits clear it)

SCHEMA = {
    "type": "object", "additionalProperties": False,
    "properties": {
        "still_open": {"type": "boolean"},
        "verdict": {"type": "string", "enum": ["green", "amber", "red"]},
        "closest_prior": {"type": "string"},        # closest existing result / where it may be solved
        "novelty_notes": {"type": "string"},
        "llm_saturation_note": {"type": "string"},   # has any AI / frontier-lab effort touched it?
        "attack_sketch": {"type": "string"},         # concrete Engine A/B plan; why ~1 week
        "confidence": {"type": "string", "enum": ["low", "medium", "high"]},
    },
    "required": ["still_open", "verdict", "closest_prior", "novelty_notes",
                 "llm_saturation_note", "attack_sketch", "confidence"],
}

PROMPT = """You are an adversarial referee doing prior-art KILL-SEARCH on an open math problem \
for a team aiming to publish a NEW result in ~1 week (tools: GPT-5.5-Pro, Claude Opus, OpenEvolve \
evolutionary search, SAT, Lean).

Your job is to TRY HARD TO KILL IT. Use web search aggressively to determine:
1. Is it ACTUALLY still open, or already solved / the gap already closed? Beware the "Erdősgate" \
trap: a problem listed as "open" in some database may have been resolved decades ago and just not \
logged. Find the closest existing result and cite it.
2. LLM-saturation: has any frontier-lab / AI effort (GPT-5 Erdős runs, AlphaEvolve, formal-conjectures \
repo, etc.) already attacked this exact problem?
3. A concrete attack sketch (Engine A = cross-domain lemma / quantitative-extension; Engine B = \
evolutionary or SAT search for a construction/counterexample) and whether ~1 week is realistic.

Verdict: RED = already solved / gap closed / clearly out of reach in a week -> kill. \
AMBER = open but with a real risk (derivable-on-sight, adjacent dense literature, ambiguous statement). \
GREEN = genuinely open, checkable, and a credible 1-week attack exists. Default toward AMBER/RED when \
uncertain; GREEN must be earned. Be specific and cite what you find."""

def _retrieve(client, rid):
    """Poll one response id to terminal state, tolerating transient connection drops."""
    import openai
    while True:
        try:
            resp = client.responses.retrieve(rid)
        except (openai.APIConnectionError, openai.APITimeoutError):
            time.sleep(8); continue
        if resp.status in ("completed", "failed", "incomplete", "cancelled"):
            return resp
        time.sleep(8)

def kill_one(client, model, prob) -> dict:
    """Submit as a background response (robust to long Pro+web-search runtimes), then poll."""
    import openai
    user = (f"PROBLEM (id {prob['id']}, source {prob['source']}, {prob['source_url']})\n"
            f"TITLE: {prob['title']}\nRESTATEMENT: {prob['restatement']}\n"
            f"WIN CONDITION: {prob['win_condition']}\n\nFULL TEXT:\n{(prob['statement'] or '')[:3500]}")
    tool = {"type": "web_search", "search_context_size": SEARCH_CONTEXT}
    for attempt in range(MAX_RETRIES):
        try:
            resp = client.responses.create(
                model=model,
                input=[{"role": "developer", "content": PROMPT},
                       {"role": "user", "content": user}],
                tools=[tool], reasoning={"effort": "medium"},
                text={"format": {"type": "json_schema", "name": "killsearch",
                                 "schema": SCHEMA, "strict": True}},
                background=True,
            )
            resp = _retrieve(client, resp.id)
            if resp.status == "completed":
                return json.loads(resp.output_text)
            err = getattr(resp, "error", None)
            code = getattr(err, "code", "") or ""
            if "rate_limit" in str(code) or "rate_limit" in str(err):
                wait = 70 * (attempt + 1)  # background failure due to TPM -> back off past the 1-min window
                print(f"    (TPM rate limit in response; waiting {wait}s, attempt {attempt+1}/{MAX_RETRIES})")
                time.sleep(wait); continue
            raise RuntimeError(f"response {resp.status}: {err}")
        except openai.RateLimitError:
            wait = 70 * (attempt + 1)
            print(f"    (429 TPM; waiting {wait}s, attempt {attempt+1}/{MAX_RETRIES})")
            time.sleep(wait)
        except openai.APIConnectionError:
            wait = 20 * (attempt + 1)
            print(f"    (connection error; retry in {wait}s, attempt {attempt+1}/{MAX_RETRIES})")
            time.sleep(wait)
        except TypeError:  # API build without search_context_size
            tool = {"type": "web_search"}
    raise RuntimeError("kill_one: exhausted retries")

def run(top=50, limit=None, model=MODEL, exclude_compilations=False):
    con = common.db()
    # finalists = top-N by composite among scored & not gate-rejected (cutoff only labels
    # triaged/filtered; selection is top-N so we always fill toward the ~50 target).
    excl = "AND tags NOT LIKE '%compilation%' " if exclude_compilations else ""
    rows = con.execute(f"SELECT * FROM problems WHERE stage IN ('triaged','filtered') "
                       f"AND composite IS NOT NULL {excl}ORDER BY composite DESC LIMIT ?", (top,)).fetchall()
    if limit:
        rows = rows[:limit]
    n_pass = con.execute("SELECT COUNT(*) FROM problems WHERE stage='triaged'").fetchone()[0]
    if n_pass < 40:
        print(f"[killsearch] WARNING: only {n_pass} problems passed triage (<40 floor). "
              f"Ingest more sources before relying on this finalist set.")
    client = common.openai_client()
    print(f"[killsearch] {len(rows)} finalists -> {model} (web search, medium effort). This is the expensive stage.")
    for r in rows:
        prob = dict(r)
        t0 = time.time()
        try:
            ks = kill_one(client, model, prob)
        except Exception as e:
            print(f"  ! {r['id']} kill-search failed: {repr(e)[:200]}")
            continue
        new_stage = "deep-rejected" if ks["verdict"] == "red" else "finalist"
        common.upsert(con, {
            "id": r["id"], "killsearch": ks, "attack_sketch": ks["attack_sketch"],
            "stage": new_stage,
            "drop_reason": (f"killsearch RED: {ks['closest_prior'][:120]}" if new_stage == "deep-rejected" else None),
        })
        print(f"  {r['id']}: {ks['verdict'].upper():5} (conf {ks['confidence']}, {time.time()-t0:.0f}s) "
              f"open={ks['still_open']}  {ks['novelty_notes'][:80]}")
        time.sleep(INTER_CALL_SLEEP)  # stay under the 200k TPM cap
    tally = con.execute("SELECT stage,COUNT(*) n FROM problems WHERE killsearch IS NOT NULL GROUP BY stage").fetchall()
    print("[killsearch] verdict tally:", {row["stage"]: row["n"] for row in tally})

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=50)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--model", default=MODEL)
    ap.add_argument("--exclude-compilations", action="store_true")
    a = ap.parse_args()
    run(a.top, a.limit, a.model, a.exclude_compilations)
