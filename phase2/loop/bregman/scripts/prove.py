#!/usr/bin/env python3
"""Complete the PROOF of arXiv:1003.3127 Problem 2 — both halves, rigorously.

Not a write-up run. Two parallel gpt-5.6-sol agents at effort=max:
  part1  turn the numerically-verified counterexample into a fully rigorous proof
  part2  the second, genuinely open half: is cl C* subset U* necessary?

Provenance note: the Part I construction was built by a Fable skeptic agent during the
2026-07-09 Tier-2 re-tag (it was told to refute the problem's tractability and failed,
producing the construction instead). This session reconstructed the explicit curve and
verified it numerically. Neither step is a proof, which is what these runs are for.

Usage: ./prove.py [part1] [part2]
"""
import json, pathlib, sys, threading, time

import openai

HERE = pathlib.Path(__file__).resolve().parent
BASE = HERE.parent
KEY = (pathlib.Path.home() / ".config/proof_hunter/openai_key.txt").read_text().strip()
MODEL, EFFORT = "gpt-5.6-sol", "max"
IDS = HERE / "prove_ids.json"
_lock = threading.Lock()

SETUP = r"""SETTING (fixed; use exactly this notation).
X = R^n. f: X -> ]-inf,+inf] Legendre. U = int dom f, U* = int dom f*.
D_f(x,y) = f(x) - f(y) - <grad f(y), x-y>.
RIGHT Bregman projection: P^->_C(x) = argmin_{y in C} D_f(x,y)  (the SECOND argument varies).
C is right D-Chebyshev if P^->_C(x) is a singleton for every x in U.  C* := grad f(C).

THE THEOREM UNDER TEST (Bauschke-Macklem-Wang, arXiv:1003.3127, Fact 3.2):
  If (a) dom f = X, (b) C subset U closed nonempty with cl C* subset U*, and (c) C is right
  D-Chebyshev, then C* is convex.
Their open problem asks which of these hypotheses are necessary."""

PART1 = SETUP + r"""

YOUR TASK: PART I — make the full-domain half fully rigorous.

A candidate counterexample exists and has been verified NUMERICALLY only. Your job is to turn it
into a proof with no numerical step left load-bearing, or to find that it fails.

THE CANDIDATE:
  f = negative entropy on R^2: f(x) = sum_j (x_j ln x_j - x_j), with 0 ln 0 = 0, and f = +inf off
  R^2_+. Then dom f = R^2_+ != R^2 (so hypothesis (a) FAILS -- this is the point), U = R^2_++,
  grad f(x) = (ln x_1, ln x_2), U* = R^2, and D_f is the generalized KL divergence
  D(x,y) = sum_j [x_j ln(x_j/y_j) - x_j + y_j].
  C = {(e^t, e^{-t^2}) : t in [1,2]}, compact in U.
  Reduction: D(x, c(t)) = const(x) + h_x(t) with h_x(t) = e^t + e^{-t^2} - x_1 t + x_2 t^2.
  h_x''(t) = e^t + (4t^2 - 2) e^{-t^2} + 2 x_2.
  C* = {(t, -t^2) : t in [1,2]}, a strictly concave arc, nonconvex; cl C* = C* subset U* = R^2,
  so hypothesis (b) HOLDS and only (a) is dropped.

WHAT MUST BE PROVED, with no appeal to numerics:
 1. An ANALYTIC proof that inf_{t in [1,2]} [ e^t + (4t^2-2) e^{-t^2} ] > 0 with an explicit
    constant. (Numerically it is 3.4540...; a clean rigorous bound such as > 3 or > 3.4 is worth
    more than a sharp unproved one. Give the argument -- e.g. monotonicity of each summand on
    subintervals, or Taylor bounds with explicit remainder.)
 2. That C is right D-Chebyshev: for EVERY x in U = R^2_++ the minimiser of h_x over [1,2] is
    unique. Handle endpoints explicitly -- a strictly convex function on a compact interval has a
    unique minimiser which may be an endpoint; say so rather than assuming interiority.
 3. That the reduction D(x,c(t)) = const(x) + h_x(t) is exact, with const(x) identified.
 4. That C is closed, nonempty, contained in U; that grad f is a bijection U -> U* = R^2; and that
    cl C* subset U* -- i.e. hypothesis (b) genuinely holds, so the example isolates (a).
 5. Nonconvexity of C* with an explicit witness.
 6. State the resulting theorem precisely: exactly what is shown about Fact 3.2's hypothesis (a).

Also verify whether C itself is convex, and say whether that matters (Fact 3.2 concludes C* is
convex, not C). Flag any hypothesis of Fact 3.2 you find we are silently violating.

NOVELTY CONSTRAINT (from a completed prior-art sweep -- respect it): the survey ALREADY contains
nonconvex right-Chebyshev sets for negative entropy (its Example 3.3), and Laude-Ochs-Cremers
(JOTA 184, 2020; arXiv:1907.04306) have a LOCAL negative-entropy nonconvex-arc construction. The
defensible claim is narrow: an explicit GLOBALLY right D_f-Chebyshev set whose gradient image is
nonconvex, showing (a) cannot be dropped even when (b) holds. Do not overstate."""

PART2 = SETUP + r"""

YOUR TASK: PART II — the second, genuinely open half. Is hypothesis (b), cl C* subset U*, necessary?

Part I (handled separately) shows hypothesis (a) dom f = X cannot be dropped. A complete answer to
the survey's problem also needs: with (a) HELD, can (b) be dropped?

CONCRETELY, either:
  (A) EXHIBIT f Legendre with dom f = X (full domain HOLDS), and C subset U closed nonempty and
      right D-Chebyshev, such that cl C* is NOT contained in U*, and C* is nonconvex; or
  (B) PROVE that under (a) and (c), C* is convex without assuming (b) -- i.e. (b) is removable.

STRUCTURAL HINT (verify or discard -- do not take on trust). If dom f = X but f is not
supercoercive, then dom f* is a proper subset of X, so U* is bounded-ish and C* can approach its
boundary only if C is UNBOUNDED. Compactness is therefore lost and the Part I uniqueness argument
(strict convexity on a compact interval) must be redone: minimisers can escape to infinity, so
EXISTENCE itself needs an argument. Families worth testing:
  f(x) = sqrt(1 + |x|^2), where grad f maps R^n into the open unit ball so U* is bounded;
  f(x) = sum_j sqrt(1 + x_j^2); or a Legendre kernel with dom f* a box.
Investigate whether an unbounded C with C* approaching bd U* can still be right D-Chebyshev, and
whether C* can then be nonconvex.

DELIVER whichever of (A) or (B) is true. If (A): give f and C in closed form, prove EXISTENCE and
uniqueness of the right projection for every x in U (existence is not automatic here), prove
cl C* is not inside U*, and exhibit the nonconvexity witness. If (B): give the proof. If the truth
is subtler -- e.g. (b) is removable only under an extra mild condition -- say exactly that and
prove the sharpest statement you reach.

BE HONEST: if you cannot settle it, report precisely what you established, where the argument
breaks, and the smallest missing statement. A clean partial result with a named gap is worth more
than a fabricated closure -- this project has been burned repeatedly by drafts asserting
certificates they never ran."""

RULES = """

RULES: state every lemma with its hypotheses; prove every analytic inequality with explicit
constants (no "clearly", and no numerical evidence standing in for a proof); number lemmas
SOL.1, SOL.2, ...; finish with a VERIFICATION RECIPE giving exact checks a referee can script,
and a WHAT REMAINS section listing every gap however small. If the target statement is FALSE,
demonstrate that and prove the strongest true variant."""

TARGETS = {"part1": PART1 + RULES, "part2": PART2 + RULES}


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
            model=MODEL, input=[{"role": "user", "content": TARGETS[name]}],
            reasoning={"effort": EFFORT}, background=True), f"{name} create")
        with _lock:
            known = json.loads(IDS.read_text()) if IDS.exists() else {}
            known[name] = resp.id
            IDS.write_text(json.dumps(known, indent=1))
        print(f"{name}: submitted ({MODEL}, effort={EFFORT}), id = {resp.id}", flush=True)
    t0 = time.time()
    while resp.status in ("queued", "in_progress"):
        if time.time() - t0 > 7200:
            raise TimeoutError(name)
        time.sleep(20)
        resp = retry(lambda: client.responses.retrieve(resp.id), f"{name} poll")
    if resp.status != "completed":
        raise RuntimeError(f"{name}: {resp.status}: {getattr(resp, 'error', None)}")
    out = BASE / f"proof_{name}_20260813.md"
    out.write_text(
        f"# Bregman Problem 2 — {name} ({MODEL}, effort={EFFORT}, {time.strftime('%Y-%m-%d %H:%M')})\n\n"
        "> SINGLE-MODEL, UNREFEREED. Counts for nothing until two adversarial lanes pass it.\n"
        "> Construction origin: the Part I counterexample was built by a Fable skeptic agent during\n"
        "> the 2026-07-09 Tier-2 re-tag, not by this run.\n\n" + resp.output_text)
    print(f"{name}: completed, {len(resp.output_text)} chars -> {out.name}", flush=True)


if __name__ == "__main__":
    names = sys.argv[1:] or ["part1", "part2"]
    ths = [threading.Thread(target=run, args=(n,)) for n in names]
    for t in ths:
        t.start()
        time.sleep(3)
    for t in ths:
        t.join()
