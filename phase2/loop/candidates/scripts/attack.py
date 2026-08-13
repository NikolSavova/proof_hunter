#!/usr/bin/env python3
"""Three lanes on the two surviving targets (gpt-5.6-sol, effort=max).

Strategy (Sihao, 2026-08-13): mine the downstream of recently AI-resolved results rather than
attacking open problems directly. See ../AI_RESOLVED_INVENTORY.md. The Jacobian orbit turned out
to be picked clean within days of the 20 July announcement, which is the evidence for the
inventory's central claim -- the edge is inversely proportional to publicity. So the top target is
now the UNIT DISTANCE disproof, three months old rather than three weeks.

  ud_status     what is already taken downstream of the unit distance disproof
  ud_hadwiger   stress-test MY OWN idea, that the new constructions bear on Hadwiger-Nelson
  jac_mindegree the one construction-shaped item left in the Jacobian orbit: lower the degree

Lane 2 exists because it is my idea and I want it attacked, not confirmed. The project has a bad
record with my own unverified inferences: today alone I proposed a Dixmier corollary for A_2 that
was a straightforward logic error, and before that cleared a paper on the wrong axis and lost a
result. An idea of mine gets an adversarial lane, not a friendly one.

Usage: ./attack.py [ud_status] [ud_hadwiger] [jac_mindegree]
"""
import json, pathlib, sys, threading, time

import openai

HERE = pathlib.Path(__file__).resolve().parent
BASE = HERE.parent
KEY = (pathlib.Path.home() / ".config/proof_hunter/openai_key.txt").read_text().strip()
MODEL, EFFORT = "gpt-5.6-sol", "max"
IDS = HERE / "attack_ids.json"
_lock = threading.Lock()

UD = r"""BACKGROUND: THE UNIT DISTANCE DISPROOF.

Erdos (1946) conjectured that n points in the plane determine at most c * n^{1+o(1)} unit
distances. In May 2026 an OpenAI internal model DISPROVED this: there are infinite families of
planar point sets beating that bound by an explicit polynomial factor. After a refinement by Will
Sawin the exponent is about n^{1.014}. Key artifacts: "Remarks on the disproof of the unit
distance conjecture", arXiv:2605.20695; OpenAI's own remarks PDF; Gil Kalai's blog post of
2026-05-21. Anthropic subsequently reported an autonomous disproof of the strongest form.

The method is the interesting part, and is why this is worth mining: ALGEBRAIC NUMBER FIELDS and
GOLOD-SHAFAREVICH TOWERS, with ideas attributed to Ellenberg-Venkatesh and
Hajir-Maire-Ramakrishna. That is class field theory imported into discrete geometry -- a
cross-domain representation shift, the same pattern that made the Jacobian counterexample
findable."""

STATUS = UD + r"""

YOUR LANE: FIND WHAT IS ALREADY TAKEN DOWNSTREAM.

Calibration from a sweep run today on the Jacobian counterexample: within ONE DAY of that
announcement, the Dixmier corollary, the Mathieu fallout, the cubic reductions and the
family/moduli follow-up were all claimed. Assume the same has happened here over three months.
Your job is to find what survived, not to admire the result.

Address each, marking TAKEN (reference + date) / IN PROGRESS / UNCLAIMED:

 1. **What was CONDITIONAL on the unit distance bound?** This is the main event. Unit distance
    upper bounds are an INPUT to other theorems, unlike the Jacobian conjecture which was mostly a
    terminal node. Enumerate published results of the form "assuming the unit distance conjecture,
    X" or which use c*n^{1+o(1)} as a hypothesis. Each is now void or needs restating. Has anyone
    published the list? Incidence geometry, additive combinatorics, and the
    Erdos distinct distances circle are the places to look.

 2. **Does the technique transplant?** Golod-Shafarevich towers gave a construction denser than
    everyone expected. What OTHER extremal problems in combinatorial geometry have conjectured
    upper bounds resting on the same intuition -- "algebraic constructions cannot be that dense"?
    Has anyone applied the same machinery elsewhere since May? Name specific conjectures that
    should now be re-examined. This is the highest-value question if it is unclaimed.

 3. **The exponent.** Sawin refined it to about 1.014. What is the current best exponent, who
    holds it, and is there an obvious ceiling to the method? Is anyone running an optimisation
    over the tower parameters?

 4. **Distinct distances.** Guth-Katz settled Erdos's distinct distances problem. Does the unit
    distance disproof interact with it, with the Szemeredi-Trotter machinery, or with the
    polynomial method more broadly? Any published note?

 5. **Higher dimensions and other norms.** Unit distances in R^3 and R^d; other metrics. Have the
    corresponding conjectures fallen to the same construction?

 6. Anything else downstream I have not thought of.

DELIVERABLE: a TAKEN / UNCLAIMED table, then a ranking of the unclaimed items by value and by how
fast someone else will take them. Be blunt about what is gone."""

HADWIGER = UD + r"""

YOUR LANE: ADVERSARIALLY STRESS-TEST AN IDEA OF MINE. DEFAULT TO REFUTATION.

I want you to try to kill the following, not to develop it. I am the author of it and I have a
documented tendency to state inferences before checking them, so treat it as a suspect claim.

MY IDEA. The chromatic number of the plane -- the Hadwiger-Nelson problem -- is exactly the
chromatic number of the UNIT DISTANCE GRAPH on R^2: vertices are points of the plane, edges join
points at distance exactly 1. De Grey (2018) exhibited a 1581-vertex unit-distance graph with
chromatic number 5, giving chi >= 5, and the bounds have been stuck at 5 <= chi <= 7 since. The
unit distance disproof produces planar point configurations with MORE unit distances than anyone
believed possible. Denser unit-distance graphs are exactly the substrate a chi >= 6 argument would
need. So: do the new constructions yield finite unit-distance graphs with chromatic number 6?

WHY THIS MIGHT BE WORTHLESS, and I want you to check each honestly:

 (a) **Asymptotic versus finite.** The disproof gives an infinite FAMILY with a better exponent.
     Hadwiger-Nelson needs ONE finite graph with a specific chromatic number. A better exponent in
     an asymptotic family may say nothing about the chromatic number of any member. This is the
     objection I most expect to be fatal. Is it?

 (b) **Density is the wrong invariant.** Chromatic number is not monotone in edge density in any
     useful way here. Known lower-bound constructions (Moser spindle, de Grey's graph, the
     Exoo-Ismailescu and Heule reductions) are engineered for rigidity and specific forbidden
     colourings, not for having many edges. A graph can have many unit distances and still be
     4-colourable. Does the extra density actually help, or is it orthogonal?

 (c) **Scale and realisability.** Do the new constructions live at a single scale, so that "unit"
     distance is meaningful for them, or do they require rescaling that destroys the property?
     Are the point sets in general position in a way that ruins the rigidity these arguments need?

 (d) **Already done.** Has anyone connected the unit distance disproof to Hadwiger-Nelson since
     May 2026? Check Kalai's blog and comments, the Polymath16 wiki and its successors, Aubrey de
     Grey's and Jaan Parts's recent work, and arXiv listings. If someone has already tried this
     and it failed, I want to know why it failed.

 (e) **The upper bound direction.** Could the constructions instead bear on chi <= 7, or on the
     measurable/Borel chromatic number variants, where the answers differ and more is known?

If after real effort the idea survives, say precisely what the strongest defensible version is and
what the next concrete step would be. If it dies, say which of (a)-(e) killed it and stop -- a
clean kill is worth more to me than a hedged maybe, and I would much rather lose this idea today
than build on it for a week.

END WITH: VERDICT: DEAD / MARGINAL / WORTH PURSUING, and one paragraph of reasons."""

MINDEG = r"""TARGET: LOWER THE DEGREE OF A JACOBIAN COUNTEREXAMPLE IN DIMENSION 3.

On 2026-07-20 Levent Alpoge, with Fable 5, announced a counterexample to the Jacobian conjecture:
F : C^3 -> C^3,

    a = (1 + x y)^3 z + y^2 (1 + x y)(4 + 3 x y)
    b = y + 3 x (1 + x y)^2 z + 3 x y^2 (4 + 3 x y)
    c = 2 x - 3 x^2 y - x^3 z

with det DF = -2 identically (I have verified this in exact arithmetic, along with the collision
F(0,0,-1/4) = F(1,-3/2,13/2) = F(-1,3/2,13/2) = (-1/4,0,0)). Component degrees are 7, 6, 4, so the
map has total degree 7.

A sweep on 2026-08-13 found that essentially every cheap consequence was claimed within days: the
Dixmier corollary for A_3, the Mathieu fallout, the cubic-homogeneous and degree-3 reductions, the
moduli/family follow-up, the Lean formalisation. What remains open is the MINIMAL DEGREE of a
counterexample in dimension 3, where the reported bounds are

    4 <= d_min(3) <= 7.

YOUR TASK. Lower the upper bound, or raise the lower bound. Concretely, EITHER

 (A) construct an explicit Keller map C^3 -> C^3 of total degree 4, 5 or 6 -- polynomial, with
     constant nonzero Jacobian determinant -- that is NOT injective, giving explicit colliding
     points; OR

 (B) prove that no counterexample of some degree in that range exists, raising the lower bound.

This is a CONSTRUCTION problem, not a search problem, and that distinction is the whole point of
the assignment. A brute-force sweep over coefficient space is hopeless: the naive count for the
degree-7 map is roughly 1329 constraints against 360 degrees of freedom, and it is findable only
because of structure. Per Tao's digestion, Alpoge's map becomes natural when the domain is viewed
as pairs (L,Q) with L linear and Q quadratic, multiplying to a cubic; the scaling symmetry
(L,Q) -> (lambda L, lambda^{-1} Q) preserves the product LQ, and the generic 3-to-1 collapse is
exactly the three ways a generic cubic factors as linear times quadratic. Local injectivity
survives because the linear factor's root separates from the quadratic's roots. There is a grading
with deg(x) = -1, deg(y) = 1, deg(z) = 2.

SO: work structurally.
 * Can the same factorisation idea be realised in lower degree? The cubic-factorisation mechanism
   forces certain degrees; identify exactly which parts of the degree-7 map are essential to the
   mechanism and which are slack that a different normalisation could remove.
 * Is there a different collapse mechanism -- 2-to-1 rather than 3-to-1, or a different symmetry
   group -- that a lower-degree map could support? A 2-to-1 collapse via a quadratic factorisation
   is the obvious thing to try, and I want to know why it does or does not work.
 * Exploit the grading: search for graded ansatze of total degree 4, 5 and 6 with an analogous
   symmetry, where the Jacobian condition becomes tractable.
 * What is known about low-degree Keller maps in dimension 3? Wang's theorem gives the conjecture
   for degree <= 2 in all dimensions; the reported lower bound of 4 suggests degree 3 in dimension
   3 is also settled. Confirm what is actually proved, since that determines the real target.

For any candidate you produce, give the map explicitly with exact rational or integer
coefficients, state det DF, and give explicit colliding points -- I will verify all of it
independently in exact arithmetic, so an unverified or approximate answer is worth nothing.

If you cannot construct one, that is an acceptable outcome, but then tell me precisely WHERE the
obstruction lies: which degree is the real barrier, and what structural fact prevents the
mechanism from operating below it. A sharp obstruction is itself a publishable observation and is
far better than a fabricated map. Do not invent a map you have not checked."""

TARGETS = {"ud_status": (STATUS, True), "ud_hadwiger": (HADWIGER, True),
           "jac_mindegree": (MINDEG, True)}


def retry(fn, what, tries=60, wait=30):
    for i in range(tries):
        try:
            return fn()
        except (openai.APIConnectionError, openai.APITimeoutError, openai.InternalServerError) as e:
            print(f"  ({what}: {type(e).__name__}, retry {i+1}/{tries})", flush=True)
            time.sleep(wait)
    raise RuntimeError(what)


def run(name):
    prompt, websearch = TARGETS[name]
    client = openai.OpenAI(api_key=KEY)
    with _lock:
        known = json.loads(IDS.read_text()) if IDS.exists() else {}
    if name in known:
        print(f"{name}: resuming {known[name]}", flush=True)
        resp = retry(lambda: client.responses.retrieve(known[name]), f"{name} retrieve")
    else:
        kw = {"tools": [{"type": "web_search", "search_context_size": "high"}]} if websearch else {}
        resp = retry(lambda: client.responses.create(
            model=MODEL, input=[{"role": "user", "content": prompt}],
            reasoning={"effort": EFFORT}, background=True, **kw), f"{name} create")
        with _lock:
            known = json.loads(IDS.read_text()) if IDS.exists() else {}
            known[name] = resp.id
            IDS.write_text(json.dumps(known, indent=1))
        print(f"{name}: submitted ({MODEL}, effort={EFFORT}), id = {resp.id}", flush=True)
    t0 = time.time()
    while resp.status in ("queued", "in_progress"):
        if time.time() - t0 > 14400:
            raise TimeoutError(name)
        time.sleep(20)
        resp = retry(lambda: client.responses.retrieve(resp.id), f"{name} poll")
    if resp.status != "completed":
        raise RuntimeError(f"{name}: {resp.status}: {getattr(resp, 'error', None)}")
    out = BASE / f"attack_{name}_20260813.md"
    out.write_text(f"# {name} ({MODEL}, effort={EFFORT}, {time.strftime('%Y-%m-%d %H:%M')})\n\n"
                   + resp.output_text)
    print(f"{name}: completed, {len(resp.output_text)} chars -> {out.name}", flush=True)


if __name__ == "__main__":
    names = sys.argv[1:] or list(TARGETS)
    ths = [threading.Thread(target=run, args=(n,)) for n in names]
    for t in ths:
        t.start()
        time.sleep(3)
    for t in ths:
        t.join()
