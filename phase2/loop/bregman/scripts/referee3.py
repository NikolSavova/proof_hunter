#!/usr/bin/env python3
"""Wave 3 — adversarial referee lanes on the claim that hypothesis (b) is REMOVABLE.

Two agents converged on (B) in wave 2. Convergence is suggestive, not decisive: both worked
from the same attempt-1 framing, so a shared blind spot is possible. These lanes attack it.

  ref_maths   default-to-refutation maths referee on both wave-2 proofs
  ref_break   tasked SPECIFICALLY with constructing a configuration that evades the argument
              (the fastest way to expose a hole, if one exists)

Artifacts attached in full, per the standing rule. Usage: ./referee2.py [ref_maths] [ref_break]
"""
import json, pathlib, sys, threading, time

import openai

HERE = pathlib.Path(__file__).resolve().parent
BASE = HERE.parent
KEY = (pathlib.Path.home() / ".config/proof_hunter/openai_key.txt").read_text().strip()
MODEL, EFFORT = "gpt-5.6-sol", "max"
IDS = HERE / "referee3_ids.json"
_lock = threading.Lock()


def cat(p, cap=70_000):
    p = pathlib.Path(p)
    return f"\n\n===== {p.name} =====\n" + p.read_text()[:cap] if p.exists() else ""


ATT = cat(BASE / "proof_part2_consolidated_20260813.md", 90_000)

SETUP = r"""SETTING. X = R^n; f Legendre; U = int dom f; U* = int dom f*;
D_f(x,y) = f(x) - f(y) - <grad f(y), x-y>. RIGHT projection P^->_C(x) = argmin_{y in C} D_f(x,y)
(SECOND argument varies); C is right D-Chebyshev if that argmin is a SINGLETON for every x in U.
C* := grad f(C).

Bauschke-Macklem-Wang (arXiv:1003.3127) Fact 3.2: if (a) dom f = X, (b) C subset U closed
nonempty with cl C* subset U*, and (c) C is right D-Chebyshev, then C* is convex. They ask which
hypotheses are necessary.

THE DOCUMENT UNDER REVIEW is a CONSOLIDATED, REPAIRED proof (attached in full) claiming:
  **Theorem 1.** If dom f = X and C subset X is ARBITRARY with argmin_{y in C} D_f(x,y) a
  singleton for every x in X, then (1) C is automatically nonempty and closed, and
  (2) C* = grad f(C) is convex. Hypothesis (b) of Fact 3.2 is entirely redundant.

It merges two independently-written proofs and applies four referee repairs (R1 use the lsc
hull k = cl(f*+iota_S) rather than continuity of f*; R2 state the tie at hull height
k(q)-<x0,q> = m_0; R3 DERIVE nonemptiness/closedness rather than assume them; R4 an
arbitrary-slope bound for supercoercivity). NEW SURFACES TO ATTACK, beyond the earlier lanes:
its Lemma 4 (attainment forces C nonempty and closed — is that really true for ARBITRARY C?),
its Lemma 6 (arbitrary-slope supercoercivity), its section 10 (why the hull height is
indispensable), and its section 11 reconciling the two source proofs — check that the
reconciliation is honest and that no step was silently dropped in the merge.

ITS KEY STEP, which is what you must attack. Suppose C* =: S is nonconvex. Attempt 1's Lemma
SOL.6 then supplies x0 and a "ghost" q in bd U*, lying in cl S, tied with the true minimiser
p_0 in S of phi_0(p) := f*(p) - <x0,p>, with common value m_0. Let n be an OUTWARD SUPPORTING
NORMAL to U* at q, and perturb x0 -> x0 + t n for t > 0, writing phi_t(p) = phi_0(p) - t<n,p>.
Then for every p in S:
      phi_t(p) = phi_0(p) - t<n,p>  >=  m_0 - t<n,p>  >  m_0 - t<n,q>  =  phi_t(q),
the last step strict because S subset U* is OPEN and a supporting hyperplane at a boundary point
puts every interior point strictly on one side. But q in cl S and f* is continuous at q (finite
height is exactly the ghost regime), so phi_t(p_k) -> phi_t(q) along p_k in S with p_k -> q.
Hence inf_S phi_t = phi_t(q) and is NOT ATTAINED, so argmin over S is EMPTY. Since (a) gives
U = X, the point x0 + t n lies in U, and (c) demands a singleton there. Contradiction."""

MATHS = SETUP + r"""

YOUR LANE: ADVERSARIAL MATHS REFEREE. DEFAULT TO REFUTATION. Kill this.

Attack, at minimum:
 1. **The duality (attempt-1 Lemma SOL.1).** Does the right projection over C really correspond
    to minimising the tilt phi_x over S = C*? Check the direction of the Legendre transform, the
    role of the second argument, and whether the correspondence is a bijection of argmin SETS
    (a singleton argmin over C must correspond to a singleton argmin over S, or the contradiction
    fails).
 2. **Lemma SOL.6 itself**, which both wave-2 proofs consume. Is it true that S nonconvex forces
    a ghost? Its step "S = dom partial(hbar**)" and the convexification argument deserve scrutiny.
 3. **Existence of the outward supporting normal n at q.** U* is open convex; q in bd U*. Is n
    guaranteed? Is <n,p> < <n,q> STRICT for every p in U*, or only <= ? If U* is unbounded or q
    sits on a flat portion, does anything change?
 4. **Continuity of f* at q.** The argument needs phi_t(p_k) -> phi_t(q). f* is lsc always, but
    CONTINUITY at a boundary point of its domain is a real assumption. Is it justified? What if
    f* is finite at q but discontinuous there? Construct such an f if you can.
 5. **Whether t can be taken small enough** that nothing else breaks — e.g. does x0 + t n stay in
    U (yes if dom f = X, but check the argument does not secretly need x0 + t n in some smaller
    set), and is q still the relevant ghost for the PERTURBED tilt?
 6. **The finite-height assumption.** Attempt 1 restricted the obstruction to finite-height ghosts
    (sup_k f*(p_k) < infinity). Do the wave-2 proofs handle INFINITE-height accumulation too, or
    silently assume finite height? If the latter, the theorem is incomplete as stated.
 7. Any gap between what the two wave-2 proofs assert and what they actually establish; any
    disagreement BETWEEN them (they were written independently — if they differ anywhere, that
    difference is a lead)."""

BREAK = SETUP + r"""

YOUR LANE: BREAK IT BY CONSTRUCTION. Your job is to build a counterexample to the claim.

Do not write a general critique. Try to EXHIBIT f Legendre with dom f = X and C closed nonempty
right D_f-Chebyshev with C* nonconvex — i.e. settle alternative (A) after all, refuting wave 2.

The argument above has specific load-bearing requirements. Each is an attack surface:
 * it needs an OUTWARD SUPPORTING NORMAL at the ghost with a STRICT inequality on U*;
 * it needs f* CONTINUOUS at the ghost q;
 * it needs a sequence in S converging to q (so that the infimum equals the ghost value);
 * it needs x0 + t n to remain a legitimate tilt parameter;
 * it needs FINITE height at the ghost.
Engineer a configuration where one of these fails while (a) and (c) still hold and C* is still
nonconvex. Concretely worth trying:
 - a Legendre f with dom f = X whose conjugate f* has a boundary point where f* is finite but
   NOT continuous (lsc but not continuous), so the infimum does not approach the ghost value;
 - U* unbounded, or with a boundary point admitting no strict supporting separation;
 - INFINITE-height accumulation, where sup_k f*(p_k) = +infinity, which attempt 1 explicitly
   excluded from the ghost regime — is convexity still forced there, or is that a genuine gap?
 - n >= 3, where the boundary geometry has more room than the plane.

Verify every candidate against ALL THREE of (a), (c), and nonconvexity of C* — attempt 1's four
failed candidates each died because existence or uniqueness quietly failed, so check those first
and in that order. If after real effort you cannot break it, say so plainly and report WHICH of
the load-bearing requirements proved most robust; a failed break that maps the theorem's true
boundary is a valuable result, and far better than a fabricated counterexample."""

TARGETS = {"ref_maths": MATHS, "ref_break": BREAK}
TAIL = ("\n\nATTACHMENTS (wave-2 proofs, then attempt 1):" + ATT +
        "\n\nEnd with: VERDICT: SURVIVES | MINOR_REPAIRS | MAJOR_ISSUES | FATAL, then a numbered "
        "issue list (location, claim, why wrong, suggested fix). For the BREAK lane, a successful "
        "construction is FATAL for the claim; state it as such and give the full certificate.")


def retry(fn, what, tries=60, wait=30):
    for i in range(tries):
        try:
            return fn()
        except (openai.APIConnectionError, openai.APITimeoutError, openai.InternalServerError) as e:
            print(f"  ({what}: {type(e).__name__}, retry {i+1}/{tries})", flush=True)
            time.sleep(wait)
    raise RuntimeError(what)


def run(name):
    client = openai.OpenAI(api_key=KEY)
    with _lock:
        known = json.loads(IDS.read_text()) if IDS.exists() else {}
    if name in known:
        print(f"{name}: resuming {known[name]}", flush=True)
        resp = retry(lambda: client.responses.retrieve(known[name]), f"{name} retrieve")
    else:
        resp = retry(lambda: client.responses.create(
            model=MODEL, input=[{"role": "user", "content": TARGETS[name] + TAIL}],
            reasoning={"effort": EFFORT}, background=True), f"{name} create")
        with _lock:
            known = json.loads(IDS.read_text()) if IDS.exists() else {}
            known[name] = resp.id
            IDS.write_text(json.dumps(known, indent=1))
        print(f"{name}: submitted ({MODEL}, effort={EFFORT}), id = {resp.id}", flush=True)
    t0 = time.time()
    while resp.status in ("queued", "in_progress"):
        if time.time() - t0 > 10800:
            raise TimeoutError(name)
        time.sleep(20)
        resp = retry(lambda: client.responses.retrieve(resp.id), f"{name} poll")
    if resp.status != "completed":
        raise RuntimeError(f"{name}: {resp.status}: {getattr(resp, 'error', None)}")
    out = BASE / f"referee3_{name}_20260813.md"
    out.write_text(f"# Wave 5 — {name} ({MODEL}, effort={EFFORT}, {time.strftime('%Y-%m-%d %H:%M')})\n\n"
                   "> Adversarial lane on the claim that hypothesis (b) is removable.\n\n" + resp.output_text)
    print(f"{name}: completed, {len(resp.output_text)} chars -> {out.name}", flush=True)


if __name__ == "__main__":
    names = sys.argv[1:] or ["ref_maths", "ref_break"]
    ths = [threading.Thread(target=run, args=(n,)) for n in names]
    for t in ths:
        t.start()
        time.sleep(3)
    for t in ths:
        t.join()
