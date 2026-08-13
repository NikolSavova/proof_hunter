#!/usr/bin/env python3
"""Seymour second-neighbourhood campaign — two Sol lanes at effort=max.

DECISION (2026-08-13): of six counterexample-shaped candidates, Seymour is the only one with a
BOUNDED search space, so it gets the whole budget. Casas-Alvero is proved (Ghosh, arXiv:2501.09272v2),
union-closed is hopeless, Kaplansky's live space needs a group hunt rather than a search, and
lonely runner leaves ~10^286 possibilities. See ../../SUMMARY.md.

The slice we intend to attack is

    delta^+ = 8,   19 <= n <= 36

and it is finite ONLY because of three claims, two of which are unrefereed 2026 preprints. If any
of the three is wrong the campaign is either pointless or unbounded. So lane A audits them BEFORE
we spend compute, and lane B designs the encoding. No CP-SAT run starts until lane A reports.

  audit    independently check the three load-bearing claims that define the slice
  encode   design the CP-SAT/PB encoding, symmetry breaking and decomposition

Local compute: 14 cores, 36 GB, OR-Tools CP-SAT 9.15. The search itself costs no API spend, which
is the whole reason this target was chosen.

Usage: ./design.py [audit] [encode]
"""
import json, pathlib, sys, threading, time

import openai

HERE = pathlib.Path(__file__).resolve().parent
BASE = HERE.parent
KEY = (pathlib.Path.home() / ".config/proof_hunter/openai_key.txt").read_text().strip()
MODEL, EFFORT = "gpt-5.6-sol", "max"
IDS = HERE / "design_ids.json"
_lock = threading.Lock()

SETUP = r"""SETTING. An ORIENTED GRAPH is a finite digraph with no loops and no digons: for each
unordered pair {u,v} at most one of the arcs u->v, v->u is present. For a vertex v write N^+(v)
for its out-neighbourhood and N^{++}(v) for its SECOND out-neighbourhood, i.e. the set of vertices
at exact directed distance 2 from v (reachable by a directed path of length 2, excluding v itself
and excluding N^+(v)).

SEYMOUR'S SECOND NEIGHBOURHOOD CONJECTURE. Every oriented graph has a vertex v (a "Seymour vertex")
with |N^{++}(v)| >= |N^+(v)|.

A COUNTEREXAMPLE is an oriented graph in which EVERY vertex v satisfies |N^{++}(v)| < |N^+(v)|.
Verification is trivial: O(n^3) bitset operations on the adjacency matrix, no numerics.

WHAT A PRIOR-ART SWEEP ESTABLISHED (2026-08-13, Sol effort=max, web_search). The conjecture is
OPEN. The relevant frontier:

 * Kaneko and Locke (Congressus Numerantium 148 (2001) 201-206) proved it for minimum out-degree
   delta^+ <= 6. THIS IS PEER-REVIEWED AND IS OUR ONLY SOLID GROUND. Hence any counterexample has
   delta^+ >= 7.
 * Sadhukhan, Sandeep and Sen, "A proof of Seymour's second neighborhood conjecture for oriented
   graphs with minimum out-degree equal to 7", arXiv:2606.30588 (2026). UNREFEREED PREPRINT.
   Structural reductions plus OR-Tools CP-SAT infeasibility checks on local obstruction models in
   the |A|=7, |B|=6, |A_1|=2 branch, split into r=5 and r=6 cases. It is NOT an exhaustive search
   over all graphs of a given order. If correct, every counterexample has delta^+ >= 8.
 * Jake Brukhman, "A dense-case theorem for Seymour's second neighborhood conjecture",
   arXiv:2608.11530 (12 August 2026 -- ONE DAY OLD). UNREFEREED PREPRINT, five pages, a counting
   proof. Rules out n <= 2*delta + 2.
 * Zelenskyi, Darmosiuk and Nalivayko, "A note on possible density and diameter of counterexamples
   to Seymour's second neighborhood conjecture", Opuscula Mathematica 41(4) (2021) 601-605. A
   degree-parametrised finite reduction: if there is a counterexample of minimum out-degree delta,
   then there is one on at most some explicit bound many vertices. Quoted by Guo, Kang and
   Zwaneveld, "Seymour-tight orientations", arXiv:2603.29626 (2026).

Combining these: at n = 19 a minimum out-degree of 9 or more would force all C(19,2) = 171 pairs
to be arcs, i.e. a regular tournament, and tournaments are settled (Fisher's proof of Dean's
conjecture; Havet-Thomasse median orders). So the only live degree at n = 19 is delta^+ = 8, and
the finite reduction bounds a minimum counterexample with delta^+ = 8 to n <= 36. Hence the slice

    delta^+ = 8,   19 <= n <= 36.

Also relevant: Chen, Shen and Yuster (Ann. Comb. 7 (2003) 15-20) give a vertex with
|N^{++}| >= gamma |N^+| for gamma the real root of 2x^3 + x^2 - 1 (about 0.657); Huang and Peng,
arXiv:2412.20234 (2024), improved the bound; Guo-Kang-Zwaneveld study "Seymour-tight" orientations,
where equality holds at every vertex, which is exactly the boundary a counterexample must cross."""

AUDIT = SETUP + r"""

YOUR LANE: AUDIT THE THREE LOAD-BEARING CLAIMS. Do not design anything. Do not search for a
counterexample. Your entire job is to tell me whether the slice above is real.

We are about to spend serious compute on the region delta^+ = 8, 19 <= n <= 36. That region is
finite, and is the right region, only if all three of the following hold. Fetch and read the actual
papers -- they are on arXiv and open access -- and check the arguments, not the abstracts.

 A. **The upper bound is the most load-bearing claim of the three, and the least scrutinised.**
    Zelenskyi-Darmosiuk-Nalivayko give a degree-parametrised bound: a counterexample of minimum
    out-degree delta implies one on at most f(delta) vertices. I need:
      (i) the EXACT statement and the exact function f, quoted verbatim;
      (ii) the value f(8) -- is it really 36?
      (iii) whether the proof is correct, or at least whether it is plausible and where its weight
           lies. A reduction of this kind usually works by deleting or contracting vertices while
           preserving the counterexample property; check that the operation really does preserve
           "every vertex has strict negative margin", which is a global condition and is exactly
           the sort of thing such arguments break.
      (iv) IF THIS BOUND IS WRONG, THE SEARCH SPACE IS INFINITE AND THE CAMPAIGN IS OFF. Say so
           in the first line of your report if you find a problem.

 B. Brukhman, arXiv:2608.11530, one day old, five pages, rules out n <= 2*delta + 2. Read the
    counting proof line by line and either confirm it or find the error. It is short, so there is
    no excuse for a hedge: give me a verdict. Note we do NOT need this claim to be true to run the
    campaign -- without it the floor merely drops from n = 19 to something smaller and the search
    gets harder, not impossible. Tell me exactly what the floor becomes if it fails.

 C. Sadhukhan-Sandeep-Sen, arXiv:2606.30588, the delta^+ = 7 case. This one is a computer-assisted
    proof whose computational part is a set of CP-SAT infeasibility checks on local obstruction
    models, not an exhaustive graph search. Assess: is the case analysis exhaustive? Do the local
    obstruction models genuinely cover every configuration? Is the reduction from "delta^+ = 7"
    to those finitely many models sound? If this fails, the live degree at n = 19 becomes 7 as
    well and the slice grows.

 D. Separately and importantly: is there ANY published bound on the minimum out-degree of a
    smallest counterexample? The sweep says no, and calls this the central obstacle -- it means
    even a complete UNSAT result for delta^+ = 8 leaves delta^+ = 9, 10, ... untouched. Confirm
    that there is no such bound, and report anything that would give one.

 E. Also check: Charles N. Glover, arXiv:2501.00614, is at v14 (May 2026) and claims a full proof
    of the conjecture via a minimum-counterexample graph level order. Fourteen versions is a
    signal. Has it been refuted, withdrawn, accepted? If that proof is CORRECT the whole campaign
    is dead, so this is worth ten minutes of your attention.

DELIVERABLE: a verdict on each of A-E: CONFIRMED / PLAUSIBLE / BROKEN / CANNOT TELL, with reasons
tied to specific steps in the papers. Then a single line: IS THE SLICE delta^+ = 8, 19 <= n <= 36
REAL AND FINITE? And if not, what is the correct slice to attack instead?"""

ENCODE = SETUP + r"""

YOUR LANE: DESIGN THE CP-SAT / PSEUDO-BOOLEAN ENCODING. Assume the slice is real; another lane is
auditing it. Do not search for a counterexample yourself -- design the search that we will run
locally on 14 cores with 36 GB and OR-Tools CP-SAT 9.15.

The raw space is hopeless by brute force: 3^C(19,2) = 3^171 is about 4 x 10^81 labelled oriented
graphs, and 3^C(36,2) = 3^630 at the top of the slice. Isomorphism reduction alone does not touch
this. So the design has to carry the whole weight. Address all of the following concretely, with
actual constraint formulations I can implement, not advice:

 1. **Base encoding.** Boolean arc[u][v] for ordered pairs, with arc[u][v] + arc[v][u] <= 1. Give
    the encoding of N^{++}. The natural route is auxiliary variables
    reach2[v][w] <-> OR_u (arc[v][u] AND arc[u][w]), then
    second[v][w] <-> reach2[v][w] AND NOT arc[v][w] AND (w != v),
    which is O(n^3) conjunctions -- 6859 at n = 19, small. Is there a better encoding? In
    particular, can the cardinality condition |N^{++}(v)| < |N^+(v)| be expressed without
    materialising second[][], for example as a single pseudo-Boolean constraint per vertex?

 2. **Symmetry breaking.** This is where the campaign is won or lost, because the expected outcome
    is UNSAT and vertex-label symmetry means 19! equivalent models. Give me a concrete scheme:
    lex-leader constraints, partial/incomplete symmetry breaking, degree-ordering constraints,
    fixing a canonical minimum-out-degree root vertex and its out-neighbourhood, orbit-based
    breaking. State precisely which constraints to post and, crucially, WHICH ARE SAFE -- a
    symmetry-breaking constraint that is not implied by the existence of SOME counterexample in
    the isomorphism class would make an UNSAT result meaningless. Flag any that only preserve
    satisfiability up to isomorphism versus those that are fully sound.

 3. **Structural constraints that a MINIMUM counterexample must satisfy.** Every one of these
    prunes hard, and each must be justified: strong connectivity; no dominated or twin vertices
    (Halkiewicz's split-twin extensions suggest twins are removable -- check the direction);
    not a tournament; every vertex has strict negative margin so |N^{++}(v)| <= |N^+(v)| - 1;
    the local structure at a minimum-degree root (exactly 8 first out-neighbours, at most 7 second).
    Derive as many valid inequalities as you can. A counting/discharging argument that bounds the
    total number of arcs, or forces a degree-sequence pattern, is worth more than any solver tuning.

 4. **Decomposition.** How should we split the slice into subproblems that run in parallel across
    14 cores? By n, by degree sequence, by the structure of the root's out-neighbourhood? Give an
    ordering: which subproblem is most likely to be SAT if a counterexample exists, and which is
    cheapest to refute? We want the cheapest refutations first to build confidence in the model,
    but the most likely SAT case early enough to matter.

 5. **Proof logging.** An unverifiable solver log is not a mathematical result. What does CP-SAT
    actually emit, and how do we get DRAT/LRAT or VeriPB certificates out of this pipeline? If
    CP-SAT cannot produce checkable certificates, say so plainly and tell me what to use instead
    (Kissat/CaDiCaL with a PB-to-CNF front end, and which encoding of the cardinality constraints
    keeps the proofs small).

 6. **A validation plan.** Before trusting anything at n = 19, the model must reproduce known
    facts. What small cases should it be checked against? It must find no counterexample for
    delta^+ <= 6 (Kaneko-Locke) and must agree with exhaustive enumeration at small n. Give me a
    concrete list of assertions the encoding must pass before we believe an UNSAT at n = 19.

 7. **An honest feasibility estimate.** Given 14 cores and this encoding, how long is n = 19,
    delta^+ = 8 likely to take? If the answer is "longer than the age of the universe", say that
    now rather than after we have burned a week. What is the largest n you expect to be reachable?

DELIVERABLE: an implementable specification. Concrete constraints, concrete symmetry breaking,
concrete decomposition, concrete validation assertions, and an honest time estimate."""

TARGETS = {"audit": AUDIT, "encode": ENCODE}
TOOLS = {"audit": True, "encode": False}   # the auditor needs to fetch the papers


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
        kw = {"tools": [{"type": "web_search", "search_context_size": "high"}]} if TOOLS[name] else {}
        resp = retry(lambda: client.responses.create(
            model=MODEL, input=[{"role": "user", "content": TARGETS[name]}],
            reasoning={"effort": EFFORT}, background=True, **kw), f"{name} create")
        with _lock:
            known = json.loads(IDS.read_text()) if IDS.exists() else {}
            known[name] = resp.id
            IDS.write_text(json.dumps(known, indent=1))
        print(f"{name}: submitted ({MODEL}, effort={EFFORT}"
              f"{', web_search' if TOOLS[name] else ''}), id = {resp.id}", flush=True)
    t0 = time.time()
    while resp.status in ("queued", "in_progress"):
        if time.time() - t0 > 14400:
            raise TimeoutError(name)
        time.sleep(20)
        resp = retry(lambda: client.responses.retrieve(resp.id), f"{name} poll")
    if resp.status != "completed":
        raise RuntimeError(f"{name}: {resp.status}: {getattr(resp, 'error', None)}")
    out = BASE / f"design_{name}_20260813.md"
    out.write_text(f"# Seymour campaign — {name} ({MODEL}, effort={EFFORT}, "
                   f"{time.strftime('%Y-%m-%d %H:%M')})\n\n" + resp.output_text)
    print(f"{name}: completed, {len(resp.output_text)} chars -> {out.name}", flush=True)


if __name__ == "__main__":
    names = sys.argv[1:] or list(TARGETS)
    ths = [threading.Thread(target=run, args=(n,)) for n in names]
    for t in ths:
        t.start()
        time.sleep(3)
    for t in ths:
        t.join()
