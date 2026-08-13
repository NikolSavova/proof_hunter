#!/usr/bin/env python3
"""Two adversarial referee lanes on the Bregman Part I proof (house rule: nothing counts
until both pass). gpt-5.6-sol at effort=max, run in parallel.

Design lesson carried over from the Bruhat campaign (2026-08-12): HAND OVER THE ARTIFACT,
NEVER THE ASSURANCE. One FATAL verdict there was caused purely by a brief that told an
agent a certificate was "established" instead of pasting it. So both lanes below receive
the full proof text, the frozen PROBLEM.md, the harness source AND its archived output, and
the prior-art constraints — nothing is referred to, everything is attached.

Usage: ./referee.py [maths] [numerics]
"""
import json, pathlib, sys, threading, time

import openai

HERE = pathlib.Path(__file__).resolve().parent
BASE = HERE.parent
KEY = (pathlib.Path.home() / ".config/proof_hunter/openai_key.txt").read_text().strip()
MODEL, EFFORT = "gpt-5.6-sol", "max"
IDS = HERE / "referee_ids.json"
_lock = threading.Lock()


def cat(p, cap=60_000):
    p = pathlib.Path(p)
    return f"\n\n===== {p.name} =====\n" + p.read_text()[:cap] if p.exists() else f"\n\n===== MISSING: {p} =====\n"


PROOF = cat(BASE / "proof_part1_20260813.md")
PROBLEM = cat(BASE / "PROBLEM.md", 20_000)
HARNESS = cat(BASE / "verify.py", 25_000)
HARNESS_OUT = cat(BASE / "out_verify.txt", 10_000)

COMMON = r"""You are an adversarial referee on a short mathematics result. DEFAULT TO REFUTATION:
your job is to kill this proof, and it survives only if you fail. Do not be agreeable.

THE RESULT UNDER REVIEW answers an open problem posed by Bauschke, Macklem and Wang,
"Chebyshev Sets, Klee Sets, and Chebyshev Centers with respect to Bregman Distances: Recent
Results and Open Problems" (arXiv:1003.3127, 2010), attached to their Fact 3.2:

  Fact 3.2. If (a) dom f = X, (b) C subset U closed nonempty with cl C* subset U*, and (c) C
  is right D-Chebyshev, then C* = grad f(C) is convex.
  OPEN: is hypothesis (a) necessary?

Definitions: X = R^n; f Legendre; U = int dom f; U* = int dom f*;
D_f(x,y) = f(x) - f(y) - <grad f(y), x-y>. The RIGHT projection is
P^->_C(x) = argmin_{y in C} D_f(x,y) (SECOND argument varies); C is right D-Chebyshev if that
argmin is a singleton for every x in U.

CONTEXT YOU MUST HOLD THE PROOF TO:
 * A prior-art sweep returned AMBER. The novelty claim is NARROW and the proof must not exceed
   it: the survey ALREADY contains nonconvex right-Chebyshev sets for negative entropy (its
   Example 3.3), and Laude-Ochs-Cremers (JOTA 184, 2020) have a LOCAL negative-entropy
   nonconvex-arc construction. The only defensible claim is an explicit GLOBALLY right
   D_f-Chebyshev set whose gradient image is nonconvex, showing (a) is not removable even when
   (b) holds. Flag ANY sentence claiming more.
 * Luo, Meng, Wen & Yao, Optimization 68(8) (2019), was read and cleared: their right-projection
   Theorem 3.12 needs U = X, which IS full domain. If you find the proof contradicts a published
   theorem, say so loudly -- that is the single most valuable thing you could find.

ATTACHED, in full: the proof; the frozen problem statement; the numeric harness SOURCE and its
ARCHIVED OUTPUT. Judge from these, not from anything you are told is established elsewhere."""

MATHS = COMMON + r"""

YOUR LANE: MATHEMATICS.

Recompute everything by hand. Specifically:
 1. Lemma SOL.2's analytic bound. Verify the derivative identity q'(t) = e^t + 4t(3-2t^2)e^{-t^2};
    the three-interval monotonicity argument; every rational constant it invents (67/16, 65/32,
    806769/40320, 41/12, 17/5, p(3/2) = 9, p(2) = 40); and in particular the TIGHT step
    e^{15/4} > 40 via e^3 > 20 and e^{3/4} > 2 -- the true value is 42.52, a 1.06x margin, so
    check the series bounds actually establish it rather than merely being plausible.
 2. The reduction D_f(x, c(t)) = K(x) + h_x(t): is K(x) genuinely independent of t? Is the
    identity exact, including the -x_j ln c_j(t) terms?
 3. Uniqueness: strict convexity on a compact interval gives a unique minimiser -- but check the
    ENDPOINT reasoning, and check the claim holds for EVERY x in R^2_++ including as x approaches
    the boundary of U or goes to infinity in either coordinate.
 4. That f is genuinely Legendre; that grad f is a bijection U -> U* = R^2; that dom f = R^2_+
    really is != R^2; and that cl C* subset U* -- i.e. that the example isolates hypothesis (a)
    and does not silently violate (b) or anything else.
 5. Nonconvexity of C*, and the separate claim that C itself is nonconvex.
 6. Whether Theorem SOL.8's stated conclusion is exactly what the six items support -- no
    overreach, no understatement.
Hunt for: circular reasoning, a hypothesis used but not verified, a quantifier silently swapped
(for every x vs for some x), and any place the proof proves something weaker than it states."""

NUMERICS = COMMON + r"""

YOUR LANE: NUMERICS AND CERTIFICATES.

The attached harness (verify.py) and its archived output are the numerical evidence. Attack them:
 1. Does the harness test what the proof CLAIMS, or a weaker proxy? In particular block [D] tests
    uniqueness by scanning a grid of x -- is that adequate, and are the sampled x adversarial
    enough? What x would you have tested that it does not?
 2. Recompute the key quantities yourself, exactly where possible: e + 2/e; the claimed
    inf q = 3.454041; the nonconvexity witness (midpoint of (1,-1) and (2,-4) versus the arc at
    t = 1.5); K(x) for a couple of x; and the block [C] interval bound.
 3. The harness reports its block [C] interval enclosure as 3.453673 while the pointwise value at
    t = 1 is 3.454041. Is that discrepancy explained (cell enclosure) or is something wrong?
 4. Flag as FABRICATED-until-sourced any number in the PROOF that no attached artifact produces.
 5. Probe the corners the harness avoids: x with wildly different scales, x near 0, x near
    infinity, and t exactly at the endpoints 1 and 2. Does uniqueness hold there?
 6. State exactly which claims of the proof are supported by executed computation, which by
    analytic argument, and which by neither."""

TARGETS = {"maths": MATHS, "numerics": NUMERICS}
TAIL = ("\n\nATTACHMENTS:" + PROOF + PROBLEM + HARNESS + HARNESS_OUT +
        "\n\nEnd with: VERDICT: SURVIVES | MINOR_REPAIRS | MAJOR_ISSUES | FATAL, then a numbered "
        "issue list with (location, claim, why wrong, suggested fix). Empty list if SURVIVES.")


def retry(fn, what, tries=60, wait=30):
    for i in range(tries):
        try:
            return fn()
        except (openai.APIConnectionError, openai.APITimeoutError, openai.InternalServerError) as e:
            print(f"  ({what}: {type(e).__name__}, retry {i+1}/{tries})", flush=True)
            time.sleep(wait)
    raise RuntimeError(what)


def run(kind):
    client = openai.OpenAI(api_key=KEY)
    with _lock:
        known = json.loads(IDS.read_text()) if IDS.exists() else {}
    if kind in known:
        print(f"{kind}: resuming {known[kind]}", flush=True)
        resp = retry(lambda: client.responses.retrieve(known[kind]), f"{kind} retrieve")
    else:
        resp = retry(lambda: client.responses.create(
            model=MODEL, input=[{"role": "user", "content": TARGETS[kind] + TAIL}],
            reasoning={"effort": EFFORT}, background=True), f"{kind} create")
        with _lock:
            known = json.loads(IDS.read_text()) if IDS.exists() else {}
            known[kind] = resp.id
            IDS.write_text(json.dumps(known, indent=1))
        print(f"{kind}: submitted ({MODEL}, effort={EFFORT}), id = {resp.id}", flush=True)
    t0 = time.time()
    while resp.status in ("queued", "in_progress"):
        if time.time() - t0 > 7200:
            raise TimeoutError(kind)
        time.sleep(20)
        resp = retry(lambda: client.responses.retrieve(resp.id), f"{kind} poll")
    if resp.status != "completed":
        raise RuntimeError(f"{kind}: {resp.status}: {getattr(resp, 'error', None)}")
    out = BASE / f"referee_{kind}_part1_20260813.md"
    out.write_text(f"# Part I referee — {kind} lane ({MODEL}, effort={EFFORT}, "
                   f"{time.strftime('%Y-%m-%d %H:%M')})\n\n"
                   "> Adversarial, default-to-refutation. Numeric claims made HERE are derived,\n"
                   "> not executed — script them before trusting.\n\n" + resp.output_text)
    print(f"{kind}: completed, {len(resp.output_text)} chars -> {out.name}", flush=True)


if __name__ == "__main__":
    kinds = sys.argv[1:] or ["maths", "numerics"]
    ths = [threading.Thread(target=run, args=(k,)) for k in kinds]
    for t in ths:
        t.start()
        time.sleep(3)
    for t in ths:
        t.join()
