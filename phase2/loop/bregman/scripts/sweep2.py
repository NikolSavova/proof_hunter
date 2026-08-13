#!/usr/bin/env python3
"""Erdősgate sweep #2 — novelty of the NEW theorem, not the counterexample.

The first sweep (sweep_20260813.md) cleared the Part I COUNTEREXAMPLE: is full domain
necessary? Part II has since produced a DIFFERENT and stronger result — a strengthening of
the published Fact 3.2 itself — and the house rule applies to it independently. A theorem that
deletes a hypothesis from a published result is exactly the kind of thing someone may already
have proved, possibly in the very papers we cleared for a different question.

Usage: ./sweep2.py
"""
import json, pathlib, time

import openai

HERE = pathlib.Path(__file__).resolve().parent
BASE = HERE.parent
KEY = (pathlib.Path.home() / ".config/proof_hunter/openai_key.txt").read_text().strip()
MODEL, EFFORT = "gpt-5.6-sol", "max"
IDS = HERE / "sweep2_ids.json"

DEV = """You are running an adversarial prior-art search for a mathematics project. Your job is to
KILL a candidate theorem by finding it already published. A problem being open in a 2010 survey is
NOT evidence it stayed open. Assume the theorem IS known and find where. Report negatives honestly
and say exactly what you searched so a human can judge coverage."""

USER = r"""TARGET: Bauschke, Macklem & Wang, arXiv:1003.3127 (2010), their Fact 3.2:

  If (a) dom f = X, (b) C subset U = int dom f is closed nonempty with cl C* subset U*
  (C* := grad f(C)), and (c) C is right D_f-Chebyshev — i.e. argmin_{y in C} D_f(x,y) is a
  SINGLETON for every x in U, the RIGHT projection, second argument varying — then C* is convex.

THE NEW THEOREM we are about to claim (find out if it is already published):

  THEOREM. Let f be Legendre on X = R^n with dom f = X. Let C subset X be ARBITRARY. If
  argmin_{y in C} D_f(x,y) is a singleton for every x in X, then (1) C is automatically nonempty
  and closed, and (2) C* = grad f(C) is convex.

  I.e. hypothesis (b) is entirely REDUNDANT, and closedness/nonemptiness of C need not be assumed
  either. This STRENGTHENS the published Fact 3.2 rather than merely answering an open problem
  about it. Proof route: right projection dualises to minimising the tilt f*(p) - <x,p> over
  S = C*; if S were nonconvex a "ghost" minimiser appears on bd U* in the lsc hull
  k = cl(f* + iota_S); perturbing x along an OUTWARD SUPPORTING NORMAL to U* at the ghost makes
  every point of S strictly worse than the hull height while the infimum still equals it, so the
  argmin over S is EMPTY — contradicting the attainment that (c) asserts.

SEARCH EXHAUSTIVELY, and be specific (titles, authors, years, venues, arXiv ids, URLs):
 1. Anyone who states Fact 3.2 WITHOUT hypothesis (b), or notes that (b) is redundant/automatic.
 2. Later work by Bauschke, Macklem, Wang and close collaborators (Borwein, Combettes, Noll,
    Lucet, Moffat, Bolte, Teboulle) — authors often strengthen their own results quietly.
 3. Luo, Meng, Wen & Yao, "Bregman distances without coercive condition: suns, Chebyshev sets and
    Klee sets", Optimization 68(8) (2019) 1599-1624. WE HAVE READ THIS: its right-projection
    Theorem 3.12 needs U = X for the full equivalence, so it does NOT remove full domain. But
    check whether any of ITS results, or a paper citing it, removes the DUAL-CLOSURE hypothesis
    cl C* subset U* — that is a different question and is exactly our claim.
 4. Laude, Ochs & Cremers, JOTA 184 (2020), arXiv:1907.04306, and work citing it.
 5. Themelis & Wang, "On the natural domain of Bregman operators", arXiv:2506.00465 (2025) —
    explicitly about domain-aware Bregman operators; check whether it contains this redundancy.
 6. The general literature on Bregman projections onto NONCONVEX sets, D-Chebyshev sets, suns,
    and Chebyshev sets for Legendre kernels, 2010-2026.
 7. Whether the "attainment forces closedness" half (1) is folklore — it may be standard and need
    citing rather than claiming.
 8. Whether the perturbation-along-a-supporting-normal technique is a known device with a name
    (it feels like it should be); if so, cite it rather than present it as new.

DELIVERABLE: VERDICT RED (already published — give the exact reference and what it says) /
AMBER (adjacent work a referee would demand we address) / GREEN (no resolution found; state
coverage). List the works actually examined and what each does; name anything that must be cited
or distinguished; state explicitly what you could NOT check (paywalls, unreachable databases)."""


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
k = "sweep_thm"
if k in known:
    print(f"resuming {known[k]}", flush=True)
    resp = retry(lambda: client.responses.retrieve(known[k]), "retrieve")
else:
    resp = retry(lambda: client.responses.create(
        model=MODEL, input=[{"role": "developer", "content": DEV}, {"role": "user", "content": USER}],
        tools=[{"type": "web_search", "search_context_size": "high"}],
        reasoning={"effort": EFFORT}, background=True), "create")
    known[k] = resp.id
    IDS.write_text(json.dumps(known, indent=1))
    print(f"submitted ({MODEL}, effort={EFFORT}, web_search), id = {resp.id}", flush=True)

t0 = time.time()
while resp.status in ("queued", "in_progress"):
    if time.time() - t0 > 10800:
        raise TimeoutError()
    time.sleep(20)
    resp = retry(lambda: client.responses.retrieve(resp.id), "poll")
if resp.status != "completed":
    raise RuntimeError(f"{resp.status}: {getattr(resp, 'error', None)}")
out = BASE / "sweep2_theorem_20260813.md"
out.write_text(f"# Prior-art sweep #2 — novelty of the (b)-redundancy THEOREM "
               f"({MODEL}, effort={EFFORT}, {time.strftime('%Y-%m-%d %H:%M')})\n\n"
               "> Sweep #1 cleared the Part I counterexample. Part II produced a different and\n"
               "> stronger claim — a strengthening of the published Fact 3.2 — so the Erdosgate\n"
               "> rule applies to it independently.\n\n" + resp.output_text)
print(f"completed, {len(resp.output_text)} chars -> {out.name}", flush=True)
