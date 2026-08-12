#!/usr/bin/env python3
"""Cross-model attack on (S1)-(S4) with OpenAI gpt-5.6-sol (house rule: cross-examine
with the other model). One call per statement, narrow scope — the same decomposition
lesson the Claude fleet learned. Outputs are SINGLE-MODEL, UNREFEREED drafts, saved as
sol_<target>_20260812.md next to the campaign ledgers; nothing counts until the usual
two-referee pass. Pattern per killsearch.py: Responses API, background=True, poll.

Usage: ./run_sol.py [target ...]   (default: s1 s2 s3 s4)
"""
import json, pathlib, sys, time

import openai

ROOT = pathlib.Path(__file__).resolve()
BRUHAT = ROOT.parents[4]                      # wave6_sol -> campaign -> g2_scripts -> f2_drafts -> bruhat
CAMP = BRUHAT / "f2_drafts" / "g2_campaign_20260811"
KEY = (pathlib.Path.home() / ".config/proof_hunter/openai_key.txt").read_text().strip()
MODEL = "gpt-5.6-sol"
POLL_S, TIMEOUT_S = 20, 3600


def read(name, cap=60_000):
    p = CAMP / name
    return f"\n\n===== FILE: {name} =====\n" + p.read_text()[:cap] if p.exists() else ""


BASE_CTX = (
    "You are attacking one open statement in a mathematics campaign on the Mahonian "
    "distribution (coefficients of prod_{j=1..m}(1+q+...+q^{j-1}); r(k) = a_k^2/(a_{k-1}a_{k+1}); "
    "target Theorem A: sigma^2(r_m(k)-1) -> 1). A single lemma CL(79, 20, 0.89) at m >= 561 "
    "is all that remains, and CL is proved modulo four statements (S1)-(S4). The campaign "
    "ledger below states them precisely, with measured numerical margins. Everything the "
    "ledger marks two-referee/citable you may use as established; everything marked open is open."
    + read("STATUS_wave5.md")
    + read("CL_composition_20260812.md", 40_000)
)

TARGETS = {
    "s1": ("Prove (S1), the banded cumulant scale bounds, band by band. A constants re-architecture "
           "plan may accompany this prompt (FILE wave6_s1_plan_20260812.md below); if present, prove the "
           "RE-ARCHITECTED targets (they carry more margin), else the ledger's originals. "
           "If a band resists, prove the best constant you can and state the delta."
           + read("wave6_s1_plan_20260812.md", 40_000)),
    "s2": ("Prove (S2), the R5 bound, exactly as the composition consumes it."),
    "s3": ("Prove (S3), the joint-cancellation statement J <= J0(W) (worst measured margin 32.6% at "
           "(561, 5.0)). Constraint: a refereed impossibility result (Prop E.3, excerpted below) shows "
           "the sign-lemma route CANNOT work — do not use it; find another route."
           + read("wave5_sl4pe_20260812.md", 30_000)),
    "s4": ("Prove (S4), the bootstrap seed: an a-priori bound |s2(r(k)-1) - 1| <= 0.89 on the region "
           "where the INFL/QUADF bootstrap starts (context below; note [561,699] is already closed, so "
           "the obligation may start at m >= 700)."
           + read("wave4_sl4p_repaired_20260812.md", 30_000)),
}

RULES = ("\n\nRULES: complete rigorous proof with every constant explicit and named; number your "
         "lemmas SOL.1, SOL.2, ...; include a final section 'VERIFICATION RECIPE' giving exact "
         "numerical checks (formulas + expected values) a referee can script; end with an honest "
         "'WHAT REMAINS' section listing any gap, however small. If the statement is FALSE or "
         "unprovable as stated, demonstrate why and prove the strongest true variant.")


IDS = ROOT.parent / "ids.json"


def _ids():
    return json.loads(IDS.read_text()) if IDS.exists() else {}


def _retry(fn, what, tries=60, wait=30):
    """Survive transient network drops (the 2026-08-12 DNS outage killed two polls)."""
    for i in range(tries):
        try:
            return fn()
        except (openai.APIConnectionError, openai.APITimeoutError, openai.InternalServerError) as e:
            print(f"  ({what}: {type(e).__name__}, retry {i + 1}/{tries} in {wait}s)", flush=True)
            time.sleep(wait)
    raise RuntimeError(f"{what}: still failing after {tries} retries")


def run(target):
    client = openai.OpenAI(api_key=KEY)
    known = _ids()
    if target in known:
        rid = known[target]
        print(f"{target}: resuming existing response id = {rid}", flush=True)
        resp = _retry(lambda: client.responses.retrieve(rid), f"{target} retrieve")
    else:
        resp = _retry(lambda: client.responses.create(
            model=MODEL,
            input=[{"role": "developer", "content": BASE_CTX},
                   {"role": "user", "content": TARGETS[target] + RULES}],
            reasoning={"effort": "high"},
            background=True,
        ), f"{target} create")
        known[target] = resp.id
        IDS.write_text(json.dumps(known, indent=1))
        print(f"{target}: submitted, response id = {resp.id}", flush=True)
    t0 = time.time()
    while resp.status in ("queued", "in_progress"):
        if time.time() - t0 > TIMEOUT_S:
            raise TimeoutError(f"{target}: exceeded {TIMEOUT_S}s")
        time.sleep(POLL_S)
        resp = _retry(lambda: client.responses.retrieve(resp.id), f"{target} poll")
    if resp.status != "completed":
        raise RuntimeError(f"{target}: {resp.status}: {getattr(resp, 'error', None)}")
    out = CAMP / f"sol_{target}_20260812.md"
    header = (f"# ({target.upper()}) attempt — {MODEL}, reasoning=high, {time.strftime('%Y-%m-%d %H:%M')}\n\n"
              "> ⚠️ SINGLE-MODEL, UNREFEREED (house rule: does not count until an adversarial\n"
              "> maths referee + numerics referee both pass it). Generated by run_sol.py.\n\n")
    out.write_text(header + resp.output_text)
    print(f"{target}: completed, {len(resp.output_text)} chars -> {out.name}")


if __name__ == "__main__":
    for t in (sys.argv[1:] or ["s1", "s2", "s3", "s4"]):
        run(t)
