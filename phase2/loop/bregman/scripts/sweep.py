#!/usr/bin/env python3
"""Erdősgate novelty sweep for arXiv:1003.3127 Problem 2 (right Bregman-Chebyshev, full domain).

House rule: prior-art kill-search is STEP ONE, never skipped. "Open in a database" is not
evidence a problem is unsolved. This runs BEFORE any proof drafting.

gpt-5.6-sol at effort=max with the web_search tool (pattern from problem-id/killsearch/killsearch.py:
Responses API, background=True, poll). Output: a dossier the human reads before we commit.
"""
import json, os, pathlib, time

import openai

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "sweep_20260813.md"
IDS = HERE / "sweep_ids.json"
KEY = (pathlib.Path.home() / ".config/proof_hunter/openai_key.txt").read_text().strip()
MODEL, EFFORT = "gpt-5.6-sol", "max"

DEV = """You are running an adversarial prior-art search for a mathematics project. Your job is to
KILL a candidate result by finding that it is already known. The project's cardinal rule is that a
problem being listed as open in a survey or database is NOT evidence that it is unsolved: a 2010
survey's open problem may have been answered in 2012 in a paper nobody indexed against it. Assume
the result IS already published and try to find where. Report negative results honestly."""

USER = r"""TARGET SURVEY: Bauschke, Macklem, Wang, "Chebyshev Sets, Klee Sets, and Chebyshev Centers
with respect to Bregman Distances: Recent Results and Open Problems", arXiv:1003.3127 (2010).

THE SPECIFIC OPEN PROBLEM (its Problem 2, around Fact 3.2):
  Fact 3.2 states: if f is Legendre with dom f = X (FULL DOMAIN), C subset U = int dom f is closed
  nonempty with cl C* subset U* where C* = grad f(C), and C is right D-Chebyshev (for every x in U
  the right Bregman projection P^->_C(x) = argmin_{y in C} D_f(x,y) is a singleton), THEN C* is convex.
  OPEN: is the full-domain hypothesis dom f = X necessary?

THE CANDIDATE ANSWER we are about to write up (find out if it is already published):
  Take f = negative entropy on R^2 (so dom f = R^2_+ != R^2 -- full domain FAILS, while
  U* = grad f(R^2_++) = R^2 so the cl C* subset U* hypothesis still HOLDS).
  Take C = {(e^t, e^{-t^2}) : t in [1,2]}, a compact arc in R^2_++.
  Then D(x, c(t)) = const(x) + e^t + e^{-t^2} - x_1 t + x_2 t^2, whose second derivative
  e^t + (4t^2-2)e^{-t^2} + 2 x_2 >= 3.454 > 0 on [1,2]; so the minimizer is unique and C is right
  D-Chebyshev, while C* = {(t,-t^2) : t in [1,2]} is a strictly concave arc, hence NONCONVEX.
  This shows the full-domain hypothesis cannot be dropped.
  NOTE: this is a small variation on the survey's OWN Example 3.3, which is why it may well have
  been noticed by someone.

WHAT TO SEARCH, exhaustively:
 1. Papers CITING arXiv:1003.3127 (Google Scholar, Semantic Scholar, arXiv listings, MathSciNet if
    reachable). Go through them looking for any that answer Problem 2 or discuss the necessity of
    the full-domain / dom f = X hypothesis in Fact 3.2.
 2. Later work by the SURVEY'S OWN AUTHORS -- Heinz Bauschke, Mason Macklem, Xianfu Wang -- and
    close collaborators (Borwein, Combettes, Noll, Lucet, Moffat). Authors often quietly resolve
    their own posed problems in a later paper.
 3. The literature on Bregman/D-Chebyshev sets, Bregman projections onto nonconvex sets, and
    Chebyshev sets for the Kullback-Leibler divergence, 2010-2026.
 4. Anything that characterizes right D-Chebyshev sets for the negative entropy (that is the
    survey's Problem 4; a full characterization would SUBSUME our counterexample and kill its novelty).
 5. Whether Fact 3.2 itself has been superseded by a stronger theorem with weaker hypotheses.
 6. Any appearance of this specific construction shape: a nonconvex curve/arc in the positive
    orthant that is right-Chebyshev for KL, or an image under grad f = log that is nonconvex.

DELIVERABLE -- a dossier with:
 * VERDICT: one of RED (already resolved/published -- give the exact reference and what it says),
   AMBER (adjacent work exists that a referee would demand we address -- list it), or
   GREEN (no resolution found; state exactly what you searched so a human can judge coverage).
 * The list of citing works you actually examined, with what each does.
 * Any paper that must be cited or distinguished in a write-up, even if it does not resolve the problem.
 * An explicit statement of what you could NOT check (paywalls, unreachable databases).
Be concrete: give titles, authors, years, venues, arXiv ids, and URLs. Do not pad with generalities."""


def retry(fn, what, tries=60, wait=30):
    for i in range(tries):
        try:
            return fn()
        except (openai.APIConnectionError, openai.APITimeoutError, openai.InternalServerError) as e:
            print(f"  ({what}: {type(e).__name__}, retry {i+1}/{tries})", flush=True)
            time.sleep(wait)
    raise RuntimeError(what)


client = openai.OpenAI(api_key=KEY)
known = json.loads(IDS.read_text()) if IDS.exists() else {}
k = "sweep_p2"
if k in known:
    print(f"resuming {known[k]}", flush=True)
    resp = retry(lambda: client.responses.retrieve(known[k]), "retrieve")
else:
    resp = retry(lambda: client.responses.create(
        model=MODEL,
        input=[{"role": "developer", "content": DEV}, {"role": "user", "content": USER}],
        tools=[{"type": "web_search", "search_context_size": "high"}],
        reasoning={"effort": EFFORT}, background=True), "create")
    known[k] = resp.id
    IDS.write_text(json.dumps(known, indent=1))
    print(f"submitted ({MODEL}, effort={EFFORT}, web_search), id = {resp.id}", flush=True)

t0 = time.time()
while resp.status in ("queued", "in_progress"):
    if time.time() - t0 > 7200:
        raise TimeoutError()
    time.sleep(20)
    resp = retry(lambda: client.responses.retrieve(resp.id), "poll")
if resp.status != "completed":
    raise RuntimeError(f"{resp.status}: {getattr(resp, 'error', None)}")
OUT.write_text(f"# Prior-art sweep — arXiv:1003.3127 Problem 2 ({MODEL}, effort={EFFORT}, web_search)\n"
               f"# {time.strftime('%Y-%m-%d %H:%M')}\n\n"
               "> Erdősgate rule: run BEFORE drafting. Single-model; a human reads the verdict.\n\n"
               + resp.output_text)
print(f"completed, {len(resp.output_text)} chars -> {OUT.name}", flush=True)
