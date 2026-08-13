#!/usr/bin/env python3
"""Part II, attempt 2 — two ADVERSARIALLY OPPOSED Sol agents on the ghost-face obstruction.

Attempt 1 (proof_part2_20260813.md) did not settle hypothesis (b) for n >= 2, but it reduced
the question to one precisely-shaped phenomenon (its Lemma SOL.6). Attempt 2 does not restart:
both agents receive attempt 1 IN FULL and attack the named obstruction from opposite sides.

  part2a  CONSTRUCT the ghost face  -> settles (A), a counterexample
  part2b  EXCLUDE the ghost face    -> settles (B), (b) is removable

Note on "trying harder": effort=max is the API ceiling and attempt 1 already ran ~35 min at
it. The lever here is not the dial but (i) a target narrowed to one lemma, (ii) attached
artifacts rather than assurances, and (iii) two genuinely different angles rather than two
identical rolls.

Usage: ./prove2.py [part2a] [part2b]
"""
import json, pathlib, sys, threading, time

import openai

HERE = pathlib.Path(__file__).resolve().parent
BASE = HERE.parent
KEY = (pathlib.Path.home() / ".config/proof_hunter/openai_key.txt").read_text().strip()
MODEL, EFFORT = "gpt-5.6-sol", "max"
IDS = HERE / "prove2_ids.json"
_lock = threading.Lock()


def cat(p, cap=70_000):
    p = pathlib.Path(p)
    return f"\n\n===== {p.name} =====\n" + p.read_text()[:cap] if p.exists() else ""


ATTEMPT1 = cat(BASE / "proof_part2_20260813.md")
PART1 = cat(BASE / "proof_part1_20260813.md", 20_000)

SETUP = r"""SETTING. X = R^n; f Legendre; U = int dom f; U* = int dom f*;
D_f(x,y) = f(x) - f(y) - <grad f(y), x-y>. RIGHT projection
P^->_C(x) = argmin_{y in C} D_f(x,y) (SECOND argument varies); C is right D-Chebyshev if that
argmin is a singleton for every x in U. C* := grad f(C).

Bauschke-Macklem-Wang (arXiv:1003.3127) Fact 3.2: if (a) dom f = X, (b) C subset U closed
nonempty with cl C* subset U*, and (c) C is right D-Chebyshev, then C* is convex.

PART I IS DONE AND REFEREED: hypothesis (a) is necessary (negative entropy, C = {(e^t,e^{-t^2})}
on [1,2]; attached). THE OPEN QUESTION HERE IS (b), WITH (a) HELD:
  (A) exhibit f Legendre with dom f = X, and C subset U closed nonempty right D-Chebyshev,
      with cl C* NOT contained in U*, and C* nonconvex; or
  (B) prove that under (a) and (c), C* is convex without assuming (b).

ATTEMPT 1 (attached in full) did NOT settle this, but proved real structure. Take its results
as established unless you find an error (say so loudly if you do):
 * Its Lemma SOL.1: via duality the right projection becomes minimisation of a LINEAR TILT of
   h = f* + iota_S over S := C*.
 * Its Lemma SOL.3/SOL.4: (b) can be replaced by the strictly weaker requirement that
   h = f* + iota_{C*} be lower semicontinuous on X.
 * Its Lemma SOL.5: in dimension n = 1, (b) is COMPLETELY REMOVABLE.
 * ITS LEMMA SOL.6 IS THE CRUX. Assume (a) and (c); let hbar be the lsc hull of h and let
   p_x in S be the unique minimiser of h(p) - <x,p>. Then p_x also minimises hbar(p) - <x,p>;
   every ADDITIONAL minimiser of that lies in cl S \ U* subset bd U*; and if no such additional
   boundary minimiser exists for any x, then S IS CONVEX.

CONSEQUENCE, and your target: S nonconvex REQUIRES that for some x the lsc-hull tilt has a tie
between p_x in S and a "ghost" point on bd U*. Attempt 1 calls this a FINITE-HEIGHT GHOST
BOUNDARY FACE: it needs C* to accumulate on bd U* with f* staying BOUNDED there."""

A = SETUP + r"""

YOUR TASK: SETTLE (A) — CONSTRUCT THE GHOST FACE.

Build f and C realising the tie, or prove the specific construction family cannot.

WHAT ATTEMPT 1 ALREADY KILLED for f(x) = sqrt(1+|x|^2) (do not repeat these):
its Lemma SOL.8 (an affine line gives every desired failure EXCEPT existence), SOL.9 (an offset
halfspace has nonconvex C* but existence fails), SOL.10 (a simple unbounded nonconvex set loses
uniqueness), SOL.11 (a large class where (b) fails but convexity survives). Read them; the
pattern is that existence or uniqueness dies exactly when nonconvexity is achieved.

THE ARITHMETIC OF THE SPHERE CASE, which you should verify and then exploit or abandon.
For f(x) = sqrt(1+|x|^2): dom f* = closed unit ball, U* = open unit ball, and
f*(p) = -sqrt(1-|p|^2), which is FINITE (= 0) on the sphere — a finite-height boundary, exactly
the ghost-face regime. The tilt is phi_x(p) = -sqrt(1-|p|^2) - <x,p>. Over the WHOLE closed
ball the minimiser is always interior, at p* = x/sqrt(1+|x|^2), with value -sqrt(1+|x|^2);
on the sphere the best value is -|x|, and sqrt(1+|x|^2) > |x| strictly. So for the full ball the
boundary NEVER ties. A tie can only occur for a constrained S that excludes the good interior
region. Verify this computation before building on it.

A STRUCTURAL IDEA WORTH TESTING (verify or discard — do not take on trust). The sphere is
STRICTLY convex, so boundary points are separated by every linear functional and ties are hard.
A kernel whose dual domain has FLAT FACES should host ghost ties far more easily, because a whole
face shares one value of <x,p>. Candidate:
    f(x) = sum_j sqrt(1 + x_j^2),
for which dom f* = the closed box [-1,1]^n, U* = the open box, and
f*(p) = -sum_j sqrt(1 - p_j^2), again finite on the boundary. Now bd U* contains flat faces
{p_1 = 1} etc., on which the tilt is affine in the remaining coordinates. Investigate whether an
S accumulating on such a face can keep existence AND uniqueness over S for every x while being
nonconvex. Other kernels with polyhedral dual domain are equally fair game.

DELIVER: either an explicit f and C with full proofs of (i) dom f = X, (ii) C closed nonempty in
U, (iii) EXISTENCE and uniqueness of the right projection for every x in U — existence is the
step that killed attempt 1's candidates, so prove it, do not assume it — (iv) cl C* NOT contained
in U*, (v) C* nonconvex with an explicit witness; or a proof that the flat-face route (and any
other you try) provably cannot work, which is itself progress toward (B)."""

B = SETUP + r"""

YOUR TASK: SETTLE (B) — PROVE THE GHOST FACE CANNOT EXIST.

Attempt 1 stated the missing statement as a question. Answer it in the affirmative direction:

  > GHOST-FACE EXCLUSION PRINCIPLE. Suppose (a) and (c) hold, so every linear tilt of
  > h = f* + iota_S has a unique attained minimiser p_x in S. Can a minimiser of the
  > lsc-hull tilt lying on bd U* coexist with p_x in a way that leaves S nonconvex?
  > Prove that it CANNOT — whence, by attempt 1's Lemma SOL.6(3), S is convex and (b) is
  > removable.

ANGLES WORTH TRYING (verify or discard; find your own if better):
 1. PERTURBATION. Suppose at some x there is a tie between p_x in S and a ghost q in bd U*.
    Perturb x to x + eps*d. The interior value moves smoothly; the ghost value moves like
    -<x+eps d, q>. Choose d to make the ghost strictly better; then the minimum over S is not
    attained near p_x, and for small eps the true minimiser over S must jump. Show this either
    contradicts uniqueness over S at some nearby x, or contradicts attainment (the infimum over
    S is approached only along a sequence escaping to bd U*, so the argmin over S is EMPTY,
    contradicting (c), which asserts a singleton and therefore attainment).
    NOTE this is the most promising angle: (c) gives ATTAINMENT for every x, which is a strong
    hypothesis, and a ghost face is exactly a mechanism for losing attainment.
 2. RECESSION / HORIZON ANALYSIS. dom f = X forces f* supercoercive (attempt 1's Lemma SOL.2).
    Study the horizon function of h and show a finite-height boundary accumulation forces either
    non-attainment at some tilt or a flat direction contradicting strict convexity of f* on U*.
 3. EXPOSED-FACE ARGUMENT. Each x exposes a face of cl conv S. Show ghost faces would make some
    tilt's exposed face contain a boundary point and an interior point simultaneously, and that
    this contradicts strict convexity of f* on U* together with uniqueness over S.
 4. DIMENSION INDUCTION. n = 1 is settled (attempt 1's SOL.5). Try slicing an n-dimensional
    configuration by lines and applying the 1-D result to each slice.

If (B) is FALSE, the honest deliverable is the obstruction to proving it, stated as sharply as
attempt 1 stated its own — ideally a concrete configuration showing which angle fails and why."""

TARGETS = {"part2a": A, "part2b": B}
RULES = ("\n\nRULES: every lemma with hypotheses; every analytic inequality with explicit "
         "constants; number lemmas SOL.1, SOL.2, ...; a VERIFICATION RECIPE of exact scriptable "
         "checks; and a WHAT REMAINS section listing every gap. A clean partial result with a "
         "named gap is worth far more than a fabricated closure — attempt 1's honesty about "
         "failing is precisely why this attempt has a sharp target. Do NOT claim to have settled "
         "(A) or (B) unless you actually have."
         + ATTEMPT1 + PART1)


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
            model=MODEL, input=[{"role": "user", "content": TARGETS[name] + RULES}],
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
    out = BASE / f"proof_{name}_20260813.md"
    out.write_text(f"# Bregman Problem 2, Part II attempt 2 — {name} "
                   f"({MODEL}, effort={EFFORT}, {time.strftime('%Y-%m-%d %H:%M')})\n\n"
                   "> SINGLE-MODEL, UNREFEREED. Attacks the ghost-face obstruction isolated by\n"
                   "> attempt 1's Lemma SOL.6. part2a tries to CONSTRUCT it, part2b to EXCLUDE it.\n\n"
                   + resp.output_text)
    print(f"{name}: completed, {len(resp.output_text)} chars -> {out.name}", flush=True)


if __name__ == "__main__":
    names = sys.argv[1:] or ["part2a", "part2b"]
    ths = [threading.Thread(target=run, args=(n,)) for n in names]
    for t in ths:
        t.start()
        time.sleep(3)
    for t in ths:
        t.join()
