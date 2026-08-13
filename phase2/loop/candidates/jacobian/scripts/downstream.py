#!/usr/bin/env python3
"""What is now unclaimed downstream of the Jacobian conjecture counterexample?

On 2026-07-20 Levent Alpoge announced, with Fable 5, an explicit polynomial map C^3 -> C^3 with
constant Jacobian determinant -2 that is generically 3-to-1. The Jacobian conjecture is therefore
FALSE in dimension >= 3. The plane case survives.

A counterexample to a conjecture that has stood since 1939 does not just close a question -- it
opens every implication that ever pointed at it. Dozens of papers prove "X implies JC" or
"JC is equivalent to Y". Each of those is now a live question with a known answer on one side,
and the explicit map may make the corresponding explicit object COMPUTABLE rather than merely
existent. That is construction work, not search, which is the kind of work we want.

The result is three weeks old and strong people are on it, so this sweep exists to find out what
is ALREADY TAKEN. Being second here is worth nothing.

  status       what has been claimed, posted or published since 2026-07-20
  reductions   what the classical reduction theorems YIELD when fed this specific map

Usage: ./downstream.py [status] [reductions]
"""
import json, pathlib, sys, threading, time

import openai

HERE = pathlib.Path(__file__).resolve().parent
BASE = HERE.parent
KEY = (pathlib.Path.home() / ".config/proof_hunter/openai_key.txt").read_text().strip()
MODEL, EFFORT = "gpt-5.6-sol", "max"
IDS = HERE / "downstream_ids.json"
_lock = threading.Lock()

MAP = r"""THE COUNTEREXAMPLE (Alpoge, with Fable 5, announced 2026-07-20; digested by Terence Tao,
"A digestion of the Jacobian conjecture counterexample", 2026-07-21). F : C^3 -> C^3,

    a = (1 + x y)^3 z + y^2 (1 + x y)(4 + 3 x y)
    b = y + 3 x (1 + x y)^2 z + 3 x y^2 (4 + 3 x y)
    c = 2 x - 3 x^2 y - x^3 z

with det DF = -2 identically, yet F(0,0,-1/4) = F(1,-3/2,13/2) = F(-1,3/2,13/2) = (-1/4,0,0),
so F is generically 3-to-1 and not injective.

Structure, per Tao: view the domain as pairs (L,Q) with L a linear form and Q a quadratic form,
multiplying to a cubic; the scaling symmetry (L,Q) -> (lambda L, lambda^{-1} Q) preserves LQ, and
the 3-to-1 collapse is exactly the three ways a generic cubic factors as linear times quadratic.
Local injectivity survives because the linear factor's root separates from the quadratic's roots.
There is a grading with deg(x) = -1, deg(y) = 1, deg(z) = 2."""

STATUS = MAP + r"""

YOUR LANE: FIND OUT WHAT IS ALREADY TAKEN.

Search exhaustively for everything posted since 2026-07-20 that builds on this counterexample.
arXiv (math.AC, math.AG, math.RA, math.QA), blogs (Tao, Secret Blogging Seminar, Xena,
Aaronson), MathOverflow, the n-Category Cafe, Mathstodon, and any formalisation repositories
(DeepMind Formal Conjectures, mathlib, Lean Zulip -- Paul Lezeau reportedly formalised the
counterexample already).

For EACH of the following, tell me: has someone already done it, is it in progress, or is it
unclaimed? Give the reference and date if taken.

 1. **The DIXMIER conjecture.** The Weyl algebra A_n; Dixmier asked whether every endomorphism of
    A_n is an automorphism. Tsuchimoto (2005) and Belov-Kanel & Kontsevich (2005-2007) proved a
    relationship between the Dixmier conjecture D_n and the Jacobian conjecture JC_{2n}.
    CRITICAL: I need the EXACT statement and, above all, THE DIRECTION. Is it a genuine
    biconditional D_n <=> JC_{2n}, or only D_n => JC_{2n}? If the implication JC_{2n} => D_n holds,
    then JC being false in dimension 4 (append an identity coordinate to the dimension-3 map)
    makes D_2 FALSE, which would be an immediate corollary. Has anyone stated it? Has anyone
    written down the explicit endomorphism of A_2 that fails to be an automorphism? Be precise
    about the direction -- do not guess, quote the theorem.

 2. **The MATHIEU-ZHAO conjecture** (and Mathieu's original conjecture on invariant measures for
    compact groups). Mathieu's conjecture is known to IMPLY the Jacobian conjecture. If so, the
    counterexample REFUTES Mathieu's conjecture outright. Has this been observed and written up?
    Similarly for Zhao's vanishing conjecture and image conjecture, and Duistermaat-van der Kallen.
    Enumerate every published statement of the form "X implies JC" -- each such X is now FALSE and
    somebody has to say so.

 3. **The cubic reductions.** Bass, Connell and Wright proved that JC holds in general iff it holds
    for maps of the form x + H with H cubic HOMOGENEOUS (in every dimension); Druzkowski sharpened
    this to the cubic linear form x + (Ax)^{*3}, componentwise cube of a linear map. These
    reductions are EXPLICIT AND ALGORITHMIC. Applying them to Alpoge's degree-7 map in dimension 3
    must therefore produce an explicit CUBIC HOMOGENEOUS counterexample, and an explicit
    DRUZKOWSKI counterexample, in some computable higher dimension.
    Has anyone carried this out? What dimension does it land in? This looks to me like the single
    most concrete unclaimed computation in the area, and it is a construction rather than a search.
    If it is unclaimed, say so loudly.

 4. **The plane case.** What has happened to JC in dimension 2 since 20 July? Any new attacks,
    any reason to think the dimension-3 construction adapts or provably cannot? Tao's account
    suggests the (L,Q) factorisation genuinely needs the room that dimension 3 provides -- is that
    written down anywhere as an obstruction for n = 2?

 5. **Minimality questions.** Is dimension 3 minimal (yes, since the plane case is open)? What is
    the minimal DEGREE of a counterexample in dimension 3 -- Alpoge's is degree 7; has anyone found
    a lower-degree one or proved a lower bound? Is there a moduli/family of such counterexamples,
    or is this map essentially rigid? A family would be a natural follow-up construction.

 6. **Everything else downstream** I have not thought of: tame vs wild automorphisms, the Nagata
    automorphism, Zariski cancellation, the LNED and related conjectures, the Poisson analogue of
    Dixmier, deformation quantisation consequences, and any conjecture in the Essen-van den Essen
    monograph "Polynomial Automorphisms and the Jacobian Conjecture" that is now settled.

DELIVERABLE: a table of downstream items, each marked TAKEN (with reference and date) / IN
PROGRESS / UNCLAIMED, followed by your ranking of the unclaimed ones by value and by how quickly
they would be taken by someone else. Be blunt about what is already gone."""

REDUCTIONS = MAP + r"""

YOUR LANE: WORK OUT WHAT THE CLASSICAL REDUCTIONS ACTUALLY YIELD FOR THIS MAP.

This is a mathematics lane, not a literature lane, though you should check the literature for
whether each computation has already been published. I want to know what concrete objects fall
out of feeding Alpoge's map into the standard machinery, and how big they are.

 1. **Bass-Connell-Wright cubic homogeneous reduction.** State the reduction precisely (the
    standard reference is Bass, Connell and Wright, Bull. AMS 7 (1982) 287-330, and van den Essen's
    monograph). It converts a polynomial map of degree d in dimension n with constant nonzero
    Jacobian into one of the form x + H, H cubic homogeneous, in a larger dimension N, preserving
    (non-)injectivity. Compute N for Alpoge's map: n = 3, degree 7. Give the exact N the standard
    construction produces, and describe the resulting map concretely enough to implement -- what
    the auxiliary variables are and how H is built. If N is enormous, say so and say how enormous.

 2. **Druzkowski's form.** Same for the reduction to x + (Ax)^{*3} where (Ax)^{*3} is the
    componentwise cube. What is A, and what dimension? Is the Druzkowski reduction applied to the
    BCW output, or directly?

 3. **Does non-injectivity survive?** This is the crux and I want it checked, not assumed. Both
    reductions are usually stated as "JC holds for all cubic homogeneous maps in all dimensions
    IFF JC holds in general". The contrapositive gives existence of a cubic counterexample. But
    does the standard proof produce it CONSTRUCTIVELY from a given counterexample, and does the
    specific failure -- three points colliding -- transfer explicitly? Trace it. If the reduction
    only preserves the truth of the statement and not the witness, say so plainly, because that
    kills the computation.

 4. **The Dixmier direction.** Independently of what the literature says, reason about the
    Tsuchimoto / Belov-Kanel-Kontsevich correspondence between the Weyl algebra A_n and polynomial
    maps in dimension 2n. Which direction is proved? If JC_{2n} => D_n, sketch how one would write
    down the explicit endomorphism of A_2 corresponding to the dimension-4 extension of Alpoge's
    map (append w as a fourth coordinate). Is that endomorphism explicitly computable, or does the
    correspondence pass through a non-constructive step such as reduction mod p and ultraproducts?
    I suspect the latter, and if so the "explicit Dixmier counterexample" may be much harder than
    the corollary -- say so.

 5. **Feasibility.** Of the objects above, which could actually be computed on a laptop with a
    computer algebra system, and which are hopeless on size grounds? Give estimates: number of
    variables, number of monomials, degree.

DELIVERABLE: for each reduction, the exact resulting dimension and form, whether the witness
transfers constructively, and a feasibility verdict. Flag clearly anything where you are
reasoning rather than citing."""

TARGETS = {"status": STATUS, "reductions": REDUCTIONS}


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
            tools=[{"type": "web_search", "search_context_size": "high"}],
            reasoning={"effort": EFFORT}, background=True), f"{name} create")
        with _lock:
            known = json.loads(IDS.read_text()) if IDS.exists() else {}
            known[name] = resp.id
            IDS.write_text(json.dumps(known, indent=1))
        print(f"{name}: submitted ({MODEL}, effort={EFFORT}, web_search), id = {resp.id}", flush=True)
    t0 = time.time()
    while resp.status in ("queued", "in_progress"):
        if time.time() - t0 > 14400:
            raise TimeoutError(name)
        time.sleep(20)
        resp = retry(lambda: client.responses.retrieve(resp.id), f"{name} poll")
    if resp.status != "completed":
        raise RuntimeError(f"{name}: {resp.status}: {getattr(resp, 'error', None)}")
    out = BASE / f"downstream_{name}_20260813.md"
    out.write_text(f"# Jacobian aftermath — {name} ({MODEL}, effort={EFFORT}, "
                   f"{time.strftime('%Y-%m-%d %H:%M')})\n\n"
                   "> The counterexample is three weeks old. This sweep is about finding what is\n"
                   "> ALREADY TAKEN, not about admiring the result.\n\n" + resp.output_text)
    print(f"{name}: completed, {len(resp.output_text)} chars -> {out.name}", flush=True)


if __name__ == "__main__":
    names = sys.argv[1:] or list(TARGETS)
    ths = [threading.Thread(target=run, args=(n,)) for n in names]
    for t in ths:
        t.start()
        time.sleep(3)
    for t in ths:
        t.join()
