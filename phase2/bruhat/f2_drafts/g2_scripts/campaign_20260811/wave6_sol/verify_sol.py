#!/usr/bin/env python3
"""Adversarial verification of a campaign draft via OpenAI gpt-5.6-sol (the cheap
verification lane — Fable fleets are off per Sihao's 2026-08-12 budget policy).
Runs a maths-referee pass and/or numerics-referee pass on a target file, saving
reports as solref_{maths,numerics}_<name>.md with the standard verdict scale.
Same hardened Responses-API pattern as run_sol.py (background, id journal, retry).

Usage: ./verify_sol.py <target-file-relative-to-campaign-dir> [maths|numerics|both]
"""
import json, os, pathlib, sys, time

import openai

ROOT = pathlib.Path(__file__).resolve()
BRUHAT = ROOT.parents[4]
CAMP = BRUHAT / "f2_drafts" / "g2_campaign_20260811"
KEY = (pathlib.Path.home() / ".config/proof_hunter/openai_key.txt").read_text().strip()
MODEL = os.environ.get("SOL_MODEL", "gpt-5.6-sol")
EFFORT = os.environ.get("SOL_EFFORT", "max")   # policy 2026-08-12: Sol always at max
POLL_S, TIMEOUT_S = 20, 7200
IDS = ROOT.parent / "verify_ids.json"

CTX = ("You are an adversarial referee on a mathematics campaign (Mahonian distribution, "
       "Theorem A: sigma^2(r_m(k)-1) -> 1; the remaining lemma CL(79,20,0.89) at m >= 561 "
       "hangs on statements (S1)-(S4)). DEFAULT TO REFUTATION — your job is to kill the "
       "draft; it survives only if you fail. Campaign ledger for context:\n"
       + (CAMP / "STATUS_wave5.md").read_text()[:40_000]
       + ((CAMP / "STATUS_wave6.md").read_text()[:40_000]
          if (CAMP / "STATUS_wave6.md").exists() else ""))

BRIEF = {
    "maths": ("MATHS REFEREE: recompute the key algebra by hand, lemma by lemma; hunt "
              "circularity, scope drift, silently-assumed hypotheses, and interface "
              "mismatches with what the composition chain consumes; check band edges and "
              "threshold arithmetic. Cite each issue as (location, claim, why wrong)."),
    "numerics": ("NUMERICS REFEREE: derive concrete numerical checks for every checkable "
                 "claim (write out the exact formulas and expected values so a human can "
                 "script them); evaluate what you can exactly; flag any number that appears "
                 "without derivation as FABRICATED-until-sourced; probe off-grid corners "
                 "the draft avoids."),
}
TAIL = ("\n\nEnd with: VERDICT: SURVIVES | MINOR_REPAIRS | MAJOR_ISSUES | FATAL, then a "
        "numbered issue list (empty if SURVIVES).")


def _retry(fn, what, tries=60, wait=30):
    for i in range(tries):
        try:
            return fn()
        except (openai.APIConnectionError, openai.APITimeoutError, openai.InternalServerError) as e:
            print(f"  ({what}: {type(e).__name__}, retry {i + 1}/{tries} in {wait}s)", flush=True)
            time.sleep(wait)
    raise RuntimeError(f"{what}: still failing after {tries} retries")


def run(target_rel, kind):
    client = openai.OpenAI(api_key=KEY)
    target = (CAMP / target_rel).read_text()
    key = f"{kind}:{target_rel}"
    known = json.loads(IDS.read_text()) if IDS.exists() else {}
    if key in known:
        print(f"{key}: resuming {known[key]}", flush=True)
        resp = _retry(lambda: client.responses.retrieve(known[key]), f"{key} retrieve")
    else:
        resp = _retry(lambda: client.responses.create(
            model=MODEL,
            input=[{"role": "developer", "content": CTX},
                   {"role": "user", "content": BRIEF[kind] + "\n\n===== DRAFT UNDER REVIEW: "
                    + target_rel + " =====\n" + target[:80_000] + TAIL}],
            reasoning={"effort": EFFORT},
            background=True,
        ), f"{key} create")
        known[key] = resp.id
        IDS.write_text(json.dumps(known, indent=1))
        print(f"{key}: submitted, id = {resp.id}", flush=True)
    t0 = time.time()
    while resp.status in ("queued", "in_progress"):
        if time.time() - t0 > TIMEOUT_S:
            raise TimeoutError(key)
        time.sleep(POLL_S)
        resp = _retry(lambda: client.responses.retrieve(resp.id), f"{key} poll")
    if resp.status != "completed":
        raise RuntimeError(f"{key}: {resp.status}: {getattr(resp, 'error', None)}")
    stem = pathlib.Path(target_rel).stem
    out = CAMP / f"solref_{kind}_{stem}.md"
    out.write_text(f"# {kind} referee ({MODEL}, effort={EFFORT}) — {target_rel} — {time.strftime('%Y-%m-%d %H:%M')}\n\n"
                   "> Cross-model referee report (Sol on the reviewed draft). Numeric checks are\n"
                   "> DERIVED, not executed — script them before trusting.\n\n" + resp.output_text)
    print(f"{key}: completed -> {out.name}", flush=True)


if __name__ == "__main__":
    rel = sys.argv[1]
    kinds = ["maths", "numerics"] if len(sys.argv) < 3 or sys.argv[2] == "both" else [sys.argv[2]]
    for k in kinds:
        run(rel, k)
