#!/usr/bin/env python3
"""Wave 4 — consolidate Part II into ONE repaired, self-contained theorem document.

The mathematical question is settled: two independent agents proved hypothesis (b) removable,
a dedicated break-agent failed on three attack routes (SURVIVES), and the maths lane returned
MINOR_REPAIRS while explicitly certifying the three load-bearing steps (duality, supporting
normal, infinite-height). Per the overnight stopping rules, proving stops here; what remains is
to apply the four repairs and produce a document a referee can accept on its own contents.

This mirrors the `s3consol` pattern from the Bruhat campaign, whose lesson was: a document that
CITES its evidence gets rejected; a document that CARRIES it does not.

Usage: ./consolidate.py
"""
import json, pathlib, time

import openai

HERE = pathlib.Path(__file__).resolve().parent
BASE = HERE.parent
KEY = (pathlib.Path.home() / ".config/proof_hunter/openai_key.txt").read_text().strip()
MODEL, EFFORT = "gpt-5.6-sol", "max"
IDS = HERE / "consolidate_ids.json"


def cat(p, cap=70_000):
    p = pathlib.Path(p)
    return f"\n\n===== {p.name} =====\n" + p.read_text()[:cap] if p.exists() else ""


BRIEF = r"""CONSOLIDATE PART II INTO ONE REPAIRED, SELF-CONTAINED THEOREM DOCUMENT.

SETTING. X = R^n; f Legendre; U = int dom f; U* = int dom f*;
D_f(x,y) = f(x) - f(y) - <grad f(y), x-y>. RIGHT projection P^->_C(x) = argmin_{y in C} D_f(x,y)
(SECOND argument varies); C is right D-Chebyshev if that argmin is a SINGLETON for every x in U.
C* := grad f(C).

Bauschke-Macklem-Wang (arXiv:1003.3127) Fact 3.2: if (a) dom f = X, (b) C subset U closed
nonempty with cl C* subset U*, and (c) C is right D-Chebyshev, then C* is convex.

WHAT IS ESTABLISHED (all attached in full):
 * Attempt 1 reduced the question to a single object, its Lemma SOL.6: if C* is nonconvex then
   some tilt has a "ghost" minimiser on bd U* in the lsc hull.
 * Two INDEPENDENT agents then proved hypothesis (b) is REMOVABLE (part2a was told to construct
   a counterexample, failed, and proved the impossibility instead; part2b proved it directly).
   Key step: perturb along an OUTWARD SUPPORTING NORMAL n to U* at the ghost q; every point of
   S = C* becomes strictly worse than the ghost height, while the infimum over S still equals
   that height and is NOT ATTAINED — contradicting the attainment that (c) asserts.
 * A dedicated BREAK agent attacked three ways (boundary discontinuity, unbounded domain,
   infinite-height accumulation) and FAILED: verdict SURVIVES.
 * The maths lane returned MINOR_REPAIRS and explicitly CERTIFIED the three load-bearing steps:
   the duality preserves argmin sets AND cardinalities; every boundary ghost admits a normal
   strict on all of U* (unboundedness and flat faces do not affect strictness for interior
   points); and every t > 0 is admissible with infinite-height cases leaving no gap.

YOUR JOB: produce ONE document proving the theorem, with these FOUR REPAIRS applied. They are
the referee's findings 1-4; do not skip any.

 R1. **Do not claim f* is continuous at the ghost.** Finite boundary value does NOT imply
     continuity — the referee exhibited a Legendre counterexample, g(u,v) = u^2 - sqrt(u) + v^2/u.
     Benchmark the perturbation against k(q), where k := cl_lsc(f* + iota_S), using a RECOVERY
     SEQUENCE with f*(s_j) -> k(q).
 R2. **State the tie at the hull height.** Lemma SOL.6 yields an EPIGRAPH ghost at height k(q),
     which may STRICTLY EXCEED f*(q). The tie must read k(q) - <x_0, q> = m_0, not
     f*(q) - <x_0, q> = m_0.
 R3. **Close the gap between the headline and the theorem.** The written theorems still assume C
     closed and nonempty, so "under (a) and (c) alone" overstates. Either add the short lemma
     that full-domain right-projection attainment FORCES C nonempty and closed, or state the
     hypotheses honestly. Prove whichever you choose.
 R4. **Fix part2b's SOL.2.** Its displayed unit-slope bound implies COERCIVITY only, not
     supercoercivity. State and prove the arbitrary-slope bound obtained by taking a sphere of
     radius R + L.

REQUIREMENTS FOR THE DOCUMENT:
 * Self-contained: state and prove every lemma you use, including the duality and the ghost
   reduction. Do NOT write "as established in the attached" — carry the argument. A referee must
   be able to accept or reject it on its own contents alone.
 * State the final theorem precisely, with its exact hypotheses, and say plainly what it does and
   does not improve on Fact 3.2.
 * Reconcile the two wave-2 proofs where they differ; if they disagree anywhere, say so and say
   which is right and why.
 * A VERIFICATION RECIPE of exact scriptable checks (the discontinuity example, the supporting
   normal strictness, the recovery-sequence convergence).
 * A WHAT REMAINS section listing every residual gap, however small, and any hypothesis that is
   assumed rather than proved.
 * Honesty rule: this project has been burned all week by drafts asserting more than they
   establish. If a repair cannot be carried out, say so rather than papering over it."""


def retry(fn, what, tries=60, wait=30):
    for i in range(tries):
        try:
            return fn()
        except (openai.APIConnectionError, openai.APITimeoutError, openai.InternalServerError) as e:
            print(f"  ({what}: {type(e).__name__}, retry {i+1}/{tries})", flush=True)
            time.sleep(wait)
    raise RuntimeError(what)


ATT = (cat(BASE / "proof_part2a_20260813.md") + cat(BASE / "proof_part2b_20260813.md") +
       cat(BASE / "referee2_ref_maths_20260813.md", 40_000) +
       cat(BASE / "referee2_ref_break_20260813.md", 30_000) +
       cat(BASE / "proof_part2_20260813.md", 45_000))

client = openai.OpenAI(api_key=KEY)
known = json.loads(IDS.read_text()) if IDS.exists() else {}
k = "consol"
if k in known:
    print(f"resuming {known[k]}", flush=True)
    resp = retry(lambda: client.responses.retrieve(known[k]), "retrieve")
else:
    resp = retry(lambda: client.responses.create(
        model=MODEL, input=[{"role": "user", "content": BRIEF + "\n\nATTACHMENTS:" + ATT}],
        reasoning={"effort": EFFORT}, background=True), "create")
    known[k] = resp.id
    IDS.write_text(json.dumps(known, indent=1))
    print(f"submitted ({MODEL}, effort={EFFORT}), id = {resp.id}", flush=True)

t0 = time.time()
while resp.status in ("queued", "in_progress"):
    if time.time() - t0 > 10800:
        raise TimeoutError()
    time.sleep(20)
    resp = retry(lambda: client.responses.retrieve(resp.id), "poll")
if resp.status != "completed":
    raise RuntimeError(f"{resp.status}: {getattr(resp, 'error', None)}")
out = BASE / "proof_part2_consolidated_20260813.md"
out.write_text(f"# Part II consolidated — hypothesis (b) is removable "
               f"({MODEL}, effort={EFFORT}, {time.strftime('%Y-%m-%d %H:%M')})\n\n"
               "> Merges the two independent wave-2 proofs with the four referee repairs applied.\n"
               "> Self-contained by construction. Still requires its own referee lane.\n\n"
               + resp.output_text)
print(f"completed, {len(resp.output_text)} chars -> {out.name}", flush=True)
