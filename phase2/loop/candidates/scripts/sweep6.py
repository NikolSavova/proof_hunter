#!/usr/bin/env python3
"""Prior-art sweep on six counterexample-shaped open problems (gpt-5.6-sol, effort=max).

Context. On 2026-07-20 Levent Alpoge announced a counterexample to the JACOBIAN CONJECTURE
found with Fable 5: an explicit degree-7 polynomial map C^3 -> C^3 with constant Jacobian
determinant -2 that is generically 3-to-1. Tao's digestion makes clear WHY it was findable:
not brute force -- the naive count is ~1329 constraints against ~360 degrees of freedom -- but a
REPRESENTATION SHIFT (view the domain as pairs (L,Q) of a linear and a quadratic form; the
scaling symmetry (L,Q) -> (lambda L, lambda^-1 Q) preserves LQ; the 3-to-1 collapse is the
three ways a generic cubic factors as linear times quadratic). The conjecture had been believed
on a HEURISTIC -- "a counterexample would need exotic geometry" -- that was an artifact of
looking in the wrong coordinates.

This sweep applies the house rule (prior-art kill-search is step one, never skipped; "open in a
database" is NOT evidence of open) to six problems selected for the same shape:
a counterexample would be a short explicit finite object, cheap to verify once exhibited.

The sweep is adversarial in BOTH directions, which is the point:
  - find out whether the problem is already resolved (kills it as a target), AND
  - find out where counterexample search is already DEAD (bounds, verified ranges, structural
    theorems), because that is what stops us burning compute in a region someone has cleared.

Usage: ./sweep6.py [name ...]   (default: all six, run concurrently)
"""
import json, pathlib, sys, threading, time

import openai

HERE = pathlib.Path(__file__).resolve().parent
BASE = HERE.parent
KEY = (pathlib.Path.home() / ".config/proof_hunter/openai_key.txt").read_text().strip()
MODEL, EFFORT = "gpt-5.6-sol", "max"
IDS = HERE / "sweep6_ids.json"
_lock = threading.Lock()

DEV = """You are running an adversarial prior-art search for a mathematics project that intends to
spend real compute hunting for an explicit COUNTEREXAMPLE to the stated conjecture.

Two failure modes you must avoid, both of which have cost this project results:

1. Confirming a problem is "listed as open" and stopping. A problem being open in a database, a
   survey, or a Wikipedia article is NOT evidence it is still open. Assume it has been resolved
   and try to find where. Check arXiv listings from the last 24 months specifically.

2. Answering the right question about the wrong axis. This project once cleared a paper by asking
   "did they remove hypothesis A?" (no) when the question that mattered was "did they remove the
   hypothesis WE remove?" (yes). Before you conclude anything, state explicitly which axis you
   checked and which you did not.

Report negatives honestly. Say exactly what you searched and what you could not reach (paywalls,
closed indexes) so a human can judge coverage. Do not inflate partial results into resolutions,
and do not deflate a resolution into a partial result."""

COMMON = r"""
DELIVERABLE -- answer ALL of the following, with specific citations (authors, title, year, venue,
arXiv id, DOI, URL) for every claim:

 1. STATUS as of August 2026. Exactly one of: OPEN / PROVED / DISPROVED / PARTIALLY RESOLVED.
    If proved or disproved, give the reference and stop -- that kills it as a target and is the
    single most valuable thing you can tell me. Search arXiv's recent listings explicitly; a 2025
    or 2026 preprint is exactly what a survey-based search would miss.

 2. WHERE COUNTEREXAMPLE SEARCH IS ALREADY DEAD. This is the second most valuable output. List
    every theorem, verified range, and exhaustive computation that RULES OUT a counterexample in
    some region: proven special cases, dimension/degree/size bounds, exhaustive enumerations and
    the bound they reached, SAT/computer searches and their scope. Be quantitative. If someone
    has already enumerated everything below size N, we must not spend compute below size N.

 3. WHY IS IT BELIEVED? Distinguish sharply between (a) a structural reason the statement should
    be true, and (b) "we looked and did not find a counterexample". The Jacobian conjecture fell
    because the belief was type (b) dressed as type (a). Which type is this, and on what evidence?

 4. REFORMULATIONS AND REPRESENTATION SHIFTS. The Jacobian counterexample was found by changing
    coordinates, not by searching harder. What equivalent formulations exist? Is there a known
    reduction to a finite/algebraic/combinatorial search? Has anyone parametrised the space of
    potential counterexamples, and what does that parametrisation look like? Which reformulation
    would a search be best run in?

 5. NEAR MISSES. Objects that satisfy most of the conditions, tight or extremal examples, cases
    where a related conjecture is FALSE (a false analogue in another characteristic, dimension,
    or category is a strong lead). Anything a previous searcher flagged as "the hard case".

 6. WHO IS ACTIVELY WORKING ON IT, and is there an AI-assisted or automated-search effort already
    running? If a group is mid-search with more compute than we have, say so.

 7. TRACTABILITY CALL for an AI-assisted counterexample hunt: is the counterexample object
    genuinely small and cheaply verifiable? What is the realistic size of the search space in the
    best known parametrisation? Give an honest verdict of PROMISING / MARGINAL / HOPELESS with
    reasons, and say what the single biggest obstacle is.

End with: VERDICT: <STATUS> | <PROMISING|MARGINAL|HOPELESS> and a two-sentence summary."""

TARGETS = {

"kaplansky": r"""TARGET: the KAPLANSKY ZERO-DIVISOR CONJECTURE.

Statement: if K is a field and G is a TORSION-FREE group, then the group ring K[G] has no zero
divisors. Related and to be treated together: the Kaplansky IDEMPOTENT conjecture (K[G] has no
idempotents other than 0 and 1) and the UNIT conjecture (the only units are trivial units kg).

Why this target. The UNIT conjecture was DISPROVED by Giles Gardam in 2021 ("A counterexample to
the unit conjecture for group rings", Annals of Mathematics), with an explicit nontrivial unit in
F_2[P] where P is the Promislow / Hantzsche-Wendt / Fibonacci group, a torsion-free crystallographic
group of Hirsch length 3. It was found by SAT/computer search over a structured ansatz. That is
EXACTLY the precedent we want to copy: a decades-old conjecture killed by a short explicit object
found by machine search over a well-chosen finite parametrisation.

Specifically determine:
 - Has the ZERO-DIVISOR conjecture been resolved since 2021, in either direction?
 - What did the follow-up work do? Alan Murray's extensions of Gardam's counterexample to other
   fields/characteristics; Gardam's own later papers; anything on whether P or a similar
   crystallographic group could also carry a zero divisor.
 - For which classes of torsion-free groups is the zero-divisor conjecture PROVED? (left-orderable
   / bi-orderable, elementary amenable, residually torsion-free nilpotent, unique product groups,
   groups satisfying Baum-Connes or Farrell-Jones, hyperbolic groups.) Which classes remain open,
   and is P itself covered by any of them? Crucially: does the unit-conjecture counterexample's
   existence in F_2[P] tell us anything about zero divisors in F_2[P] -- is that case OPEN?
 - What is the exact search formulation Gardam used (support size, symmetry reduction, SAT
   encoding), and is the analogous formulation for zero divisors written down anywhere?
 - What is the smallest support size for which a zero divisor in F_2[P] has been ruled out?""",

"casas_alvero": r"""TARGET: the CASAS-ALVERO CONJECTURE.

Statement: let K be a field of characteristic 0 and let p be a monic polynomial of degree n over K.
If p shares a common root with each of its derivatives p', p'', ..., p^(n-1) (a possibly DIFFERENT
root with each derivative), then p = (x - a)^n for some a.

Why this target. A counterexample is a single explicit polynomial, and verification is a resultant
computation -- about as cheap as verification gets. The conjecture is known for several degrees but
NOT in general, and the pattern of known degrees is arithmetic rather than structural, which smells
like type-(b) belief.

Specifically determine:
 - Current status, and the exact set of degrees n for which it is PROVED. I believe it is known
   for n = p^k and for n = 2p^k, 3p^k, 4p^k and similar (Graf von Bothmer, Labs, Schicho, van de
   Woestijne, "The Casas-Alvero conjecture for infinitely many degrees", J. Algebra 2007). Confirm
   and give the complete current list. WHAT IS THE SMALLEST DEGREE STILL OPEN? That number is the
   single most useful fact you can return.
 - The POSITIVE CHARACTERISTIC situation. The conjecture is FALSE in characteristic p, with known
   counterexamples. Give them explicitly. This is the most important lead in the whole sweep: a
   false analogue tells us what a characteristic-0 counterexample would have to look like and why
   the standard reduction fails. Explain exactly where the char-0 proofs use char 0.
 - Any 2024-2026 preprints. There has been recurring activity here; check carefully whether
   someone has announced a proof or a counterexample recently.
 - The parametrisation: the conditions cut out a variety in coefficient space. What is known about
   its dimension and components? Has anyone run a Grobner/numerical-algebraic-geometry search over
   it, and to what degree?""",

"crouzeix": r"""TARGET: CROUZEIX'S CONJECTURE.

Statement: for every square complex matrix A and every polynomial p,
    ||p(A)|| <= 2 * sup{ |p(z)| : z in W(A) },
where W(A) is the numerical range (field of values) of A and ||.|| the spectral norm.

Why this target. A counterexample is a matrix plus a polynomial, and checking it is a numerical
eigenvalue computation -- verification is essentially free, and can be made rigorous with interval
arithmetic. The constant 2 is conjectured optimal.

Specifically determine:
 - Status as of 2026. Has it been proved or disproved?
 - The best PROVEN constant. Crouzeix and Palencia (2017) proved 1 + sqrt(2) ~ 2.414. Has that
   been improved since? Give the current record and the reference.
 - For which classes is the constant 2 PROVED? (2x2 matrices, Jordan blocks, nilpotent of low
   order, contractions/power-bounded cases, normal matrices, tridiagonal, etc.) Where exactly does
   the proof stop?
 - EXTREMAL AND NEAR-EXTREMAL EXAMPLES. Which matrices come closest to the bound 2, and how close?
   Greenbaum, Overton and collaborators ran substantial numerical optimisation over this problem;
   report what the best observed ratios are, at what dimensions, and whether the optimisation
   appeared to converge to 2 or to plateau below it. If the observed supremum is strictly below 2
   across large searches, say so -- that would be evidence the conjecture is not tight and that
   counterexample hunting is hopeless.
 - Has anyone searched with certified/interval arithmetic rather than floating point?
 - Is there a known reduction to a finite-dimensional or low-dimensional search?""",

"lonely_runner": r"""TARGET: the LONELY RUNNER CONJECTURE.

Statement: for n runners on a unit circular track with distinct constant speeds, starting together,
each runner is at some time at distance at least 1/n from every other runner. Equivalently, for
distinct positive integers v_1, ..., v_{n-1} there is a real t with ||t v_i|| >= 1/n for all i,
where ||.|| is distance to the nearest integer.

Why this target. A counterexample is a finite vector of integer speeds and verification is a
one-dimensional optimisation over a compact interval -- trivially checkable, and rigorously
certifiable by interval arithmetic.

Specifically determine:
 - Exactly how many runners is it PROVED for? I believe up to 7 runners (Barajas and Serra, 2008,
   "The lonely runner with seven runners"), leaving 8 open. Confirm this and report any progress
   since. WHAT IS THE SMALLEST OPEN NUMBER OF RUNNERS as of 2026?
 - What computational searches have been run, over what speed ranges, and with what result? If
   someone has exhaustively checked all speed vectors up to some bound for 8 runners, that bound is
   critical to us.
 - Is restricting to INTEGER speeds without loss of generality, and is there a known bound on the
   speeds of a minimal counterexample? A bound would convert this into a finite search.
 - TIGHT CASES. Which speed sets achieve exactly 1/n or come closest? The known extremal families
   are the most likely place for a counterexample to hide.
 - Reformulations: the view-obstruction problem of Cusick, the Wills formulation, flows in
   matroids/graphs (Bienia et al.), and any lattice or Fourier-analytic reformulation. Which is
   best suited to machine search?
 - Any 2024-2026 progress, including partial results for restricted speed sets.""",

"seymour": r"""TARGET: SEYMOUR'S SECOND NEIGHBOURHOOD CONJECTURE.

Statement: every finite oriented graph (a digraph with no loops, no digons, i.e. an orientation of
a simple graph) has a vertex v whose second out-neighbourhood is at least as large as its first:
|N^{++}(v)| >= |N^{+}(v)|.

Why this target. A counterexample is a finite digraph; verification is a trivial computation over
all vertices. If a counterexample exists at small order, exhaustive or SAT search finds it.

Specifically determine:
 - Status as of 2026, including any 2024-2026 preprints claiming a proof.
 - What is PROVED: tournaments (Fisher's proof of Dean's conjecture via the Fisher/Havet-Thomasse
   median order argument), digraphs of small order, oriented graphs with minimum out-degree
   conditions, graphs with specific girth or degree constraints, the weighted version, and the
   known constant-factor results (a vertex with |N^{++}| >= gamma |N^{+}| for gamma ~ 0.657, the
   real root of 2x^3 + x^2 - 1, due to Chen, Shen and Yuster). Report the current best gamma.
 - EXHAUSTIVE SEARCH: has anyone verified the conjecture for all oriented graphs up to n vertices?
   What is n? This is the decisive number -- it tells us the floor for any search we run.
 - Are there known families that are TIGHT (equality for every vertex)? Tight families are where a
   counterexample would live.
 - Reformulations, especially any reduction to a finite or LP/flow problem, and any SAT encoding.""",

"union_closed": r"""TARGET: the UNION-CLOSED SETS CONJECTURE (Frankl's conjecture).

Statement: every finite union-closed family of sets, other than the family consisting only of the
empty set, contains an element belonging to at least half of the sets in the family.

Why this target. A counterexample is an explicit finite family of finite sets -- fully checkable.
I rate this the WEAKEST of my six candidates because it has been searched hard, and I want you to
tell me whether that assessment is right.

Specifically determine:
 - Status as of 2026.
 - The state of the CONSTANT. Gilmer (2022) gave an entropy argument proving a constant of about
   0.01; this was rapidly improved to (3 - sqrt 5)/2 ~ 0.38 by several groups independently
   (Alweiss-Huang-Sellke, Chase-Lovett, Pebody, Sawin). Report the current best constant, and
   critically: is there a BARRIER RESULT showing 0.38 is the ceiling of the entropy method? If so,
   is the barrier evidence that 1/2 is false, or just that the method is exhausted?
 - VERIFIED RANGES. For which ground-set sizes n and family sizes |F| has the conjecture been
   exhaustively verified? I believe it is known for n <= 12 or thereabouts and for |F| below some
   bound. Give exact numbers with references -- this determines whether any search we run is
   already dead on arrival.
 - Structural results: it is known for families containing a singleton or a doubleton, for lattices
   of certain types, etc. Summarise what a counterexample is forced to look like -- the constraints
   accumulated over 40 years are effectively a specification for the object we would search for.
 - Given all of the above, is counterexample search here HOPELESS? Say so plainly if it is.""",
}


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
            model=MODEL,
            input=[{"role": "developer", "content": DEV},
                   {"role": "user", "content": TARGETS[name] + "\n" + COMMON}],
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
    out = BASE / f"sweep_{name}_20260813.md"
    out.write_text(f"# Prior-art sweep — {name} ({MODEL}, effort={EFFORT}, "
                   f"{time.strftime('%Y-%m-%d %H:%M')})\n\n"
                   "> Counterexample-shaped target, selected after the Jacobian conjecture\n"
                   "> counterexample (Alpoge/Fable 5, 2026-07-20). Sweep asks BOTH whether the\n"
                   "> problem is already resolved AND where counterexample search is already dead.\n\n"
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
