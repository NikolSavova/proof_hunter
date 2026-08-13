#!/usr/bin/env python3
"""Part I VERIFICATION GATE — three independent Sol lanes, effort=max.

Why this exists. Part I already passed two adversarial lanes on 2026-08-12. This run is not a
repeat: it is the gate the Luo clearance memo itself demanded ("a referee lane should re-read
Theorem 3.12 and Lemma 3.2 independently before submission"), and it is the gate the PART II
POST-MORTEM demands. On 2026-08-13 the Part II novelty claim died because the clearance asked
"did Luo remove FULL DOMAIN?" (no) and stopped, when the question that mattered was "did Luo
remove the hypothesis WE remove?" (yes). The same reader wrote the Part I clearance. So Part I's
novelty is re-derived here from the paper text, by a reader who is told about that failure.

  v1_maths   fresh adversarial maths referee on the Part I proof. Deliberately NOT told about
             the earlier lanes or their findings — a genuinely independent read, not a re-audit.
  v2_sun     the SHARPER CLAIM surfaced by re-reading Luo's actual Theorem 3.13 (whose real
             hypotheses are narrower than the Part II adjudication paraphrased). If our example
             satisfies 3.13, then C is a ->D_f-SUN while Luo's (i) and (iv) FAIL, which makes it
             a counterexample to the equivalence in their Theorem 3.12(2) without U = X. That
             would be a second, independent payload for the note. Verify or kill it.
  v3_novelty prior-art re-sweep on the Part I axis, told exactly how the Part II clearance failed.

Per the standing rule ("hand over the artifact, never the assurance") every lane receives the
verbatim text of Luo et al. sections 2 and 3 and the full Part I proof, not a summary of them.

Usage: ./verify_part1.py [v1_maths] [v2_sun] [v3_novelty]
"""
import json, pathlib, sys, threading, time

import openai

HERE = pathlib.Path(__file__).resolve().parent
BASE = HERE.parent
KEY = (pathlib.Path.home() / ".config/proof_hunter/openai_key.txt").read_text().strip()
MODEL, EFFORT = "gpt-5.6-sol", "max"
IDS = HERE / "verify_part1_ids.json"
LUO = pathlib.Path("/Users/sihaohuang/.claude/jobs/eb370033/tmp")
_lock = threading.Lock()


def attach(p, cap=90_000):
    """Attach an ARTIFACT verbatim. Never paraphrase a source into a brief: the 2026-08-12
    FATAL and the 2026-08-13 novelty collapse were both caused by a brief that ASSERTED what a
    source said instead of handing the source over."""
    p = pathlib.Path(p)
    if not p.exists():
        raise FileNotFoundError(p)
    return f"\n\n===== {p.name} =====\n" + p.read_text()[:cap]


PROOF = attach(BASE / "proof_part1_20260813.md")
LUO_TEXT = ("\n\n===== Luo, Meng, Wen & Yao, Optimization 68(8) (2019) 1599-1624 =====\n"
            "Verbatim pdftotext extraction. Section 2 (preliminaries and definitions), then the\n"
            "head of Section 3 (standing hypotheses), then Section 3.2 (RIGHT projections, which\n"
            "is our case: Prop 3.10, Def 3.11, Thm 3.12, Thm 3.13, Cor 3.14). Layout artefacts\n"
            "from the extraction are present; the arrows over Pi and D render as separated glyphs.\n"
            + attach(LUO / "luo_prelim.txt") + attach(LUO / "luo_s3head.txt")
            + attach(LUO / "luo_s32.txt"))

SETUP = r"""SETTING. X = R^n; f Legendre; U = int dom f; U* = int dom f*;
D_f(x,y) = f(x) - f(y) - <grad f(y), x-y>. RIGHT projection P^->_C(x) = argmin_{y in C} D_f(x,y)
(the SECOND argument varies); C is right D-Chebyshev if that argmin is a SINGLETON for every
x in U. C* := grad f(C).

Bauschke, Macklem & Wang, arXiv:1003.3127 (2010), Fact 3.2:

  If (a) dom f = X, (b) C subset U is closed nonempty with cl C* subset U*, and (c) C is right
  D-Chebyshev, then C* is convex.

Their open problem, which is our target: IS HYPOTHESIS (a) NECESSARY?

OUR ANSWER (Part I): yes, and here is the counterexample. f = negative entropy on R^2, so
dom f = R^2_+ != R^2 and (a) FAILS; C = {(e^t, e^{-t^2}) : t in [1,2]}, compact, contained in
U = R^2_++. Then (b) and (c) both HOLD and C* = {(t,-t^2) : t in [1,2]} is nonconvex. So (a)
cannot simply be deleted. The full proof is attached."""

MATHS = SETUP + r"""

YOUR LANE: ADVERSARIAL MATHS REFEREE ON THE ATTACHED PROOF. DEFAULT TO REFUTATION.

Assume the proof is wrong and find where. A counterexample paper dies on a single unchecked
hypothesis, so check every one of them, including the ones the author thinks are obvious.

Attack, at minimum:

 1. **Is f really Legendre?** Essential smoothness AND essential strict convexity, with the
    boundary behaviour at x_j = 0 handled correctly. Lemma SOL.1 argues dom(partial f) = U via
    a subgradient inequality; check that argument rather than trusting the standard fact.
 2. **Is U* really all of R^2?** This is load-bearing: if cl C* were NOT inside U*, the example
    would be dropping TWO hypotheses rather than isolating (a), and would prove nothing about
    (a). Verify f*(u) = e^{u_1} + e^{u_2} and dom f* = R^2 from the definition.
 3. **Is C right D_f-Chebyshev for EVERY x in U — including the hard cases?** Lemma SOL.5
    reduces to strict convexity of h_x on [1,2]. Check the reduction (Lemma SOL.4) is exact,
    check the endpoint analysis is genuinely exhaustive, and check what happens as x approaches
    bd U (x_2 -> 0+, x_1 -> 0+, x_1 -> infinity). Uniqueness must not degrade anywhere in U.
 4. **Lemma SOL.2's curvature bound, in exact arithmetic.** It claims inf_{[1,2]} q = q(1) =
    e + 2/e > 41/12 > 17/5 via a three-interval monotonicity argument and truncated exponential
    series with explicit rational constants (67/16, 806769/40320, 65/32, 8/3). Recompute every
    one. Check each series truncation is used in the CORRECT DIRECTION (a lower bound on e^a
    from a partial sum is valid since omitted terms are positive; an UPPER bound on e^a is NOT
    obtained that way, so flag any place an upper bound is needed). Check the interval endpoints
    sqrt(3/2), 3/2, 2 and that the three intervals actually cover [1,2].
    CONTEXT YOU SHOULD USE: an earlier draft of the surrounding notes asserted h'' >= 3.454041
    when e + 2/e = 3.454040710802..., i.e. it rounded the WRONG WAY and the bound was false in
    the limit x_2 -> 0+. That error is not in the attached proof, but it shows the author's
    rounding discipline is not reliable. Re-derive, do not spot-check.
 5. **The nonconvexity witness** (Lemma SOL.6) and the claim that C itself is nonconvex
    (Lemma SOL.7, whose psi'' computation should be recomputed).
 6. **Any silent hypothesis violation.** Fact 3.2 as quoted may sit under standing assumptions
    from its source paper (Legendre, plus possibly 1-coercivity/supercoercivity in the R^n
    section). The proof includes an "additional standing-condition check" for 1-coercivity —
    verify it. If the example violated a standing assumption we would be attacking a straw man.
 7. **Does the conclusion actually follow?** The proof states its conclusion narrowly ("(a)
    cannot simply be omitted from the universal theorem", NOT "full domain is necessary in every
    individual instance"). Check the stated conclusion is exactly what the construction supports
    — neither more nor less. Flag any sentence that overclaims.

Report every real defect. If you find none, say so plainly and state which step you consider the
most fragile and why."""

SUN = SETUP + r"""

YOUR LANE: VERIFY OR KILL A SHARPER SECOND CLAIM.

Also attached, verbatim, is Luo, Meng, Wen & Yao, "Bregman distances without coercive condition:
suns, Chebyshev sets and Klee sets", Optimization 68(8) (2019) 1599-1624 — sections 2, the head
of section 3 (standing hypotheses), and section 3.2 (right projections). Their Theorem 3.12
states, for a ->D_f-proximinal C, relations between (i) a variational characterisation (34),
(ii) C is a ->D_f-sun, (iii) a rescaling property, and (iv) grad f(C) is convex; part (2)
requires U = X and part (3) requires grad f(U) = U* plus f* Gateaux differentiable and strictly
convex on U*. Their Theorem 3.13 says a boundedly compact ->D_f-Chebyshev C is a ->D_f-sun,
under stated total-convexity hypotheses. Definition 2.1 defines totally convex / locally
uniformly totally convex at a point; Definition 3.11 defines ->D_f-sun.

THE CLAIM TO ADJUDICATE — I believe our Part I example does more than answer
Bauschke-Macklem-Wang. I believe it ALSO shows the hypothesis "U = X" in Luo et al.'s
Theorem 3.12(2) cannot be dropped. The alleged chain, which you must check step by step:

  (A) For f = negative entropy on R^2: f is totally convex at every point of U (indeed of
      dom f), because for y in U and t > 0 the modulus nu_f(y,t) is an infimum of the
      continuous, strictly positive function D_f(.,y) over the COMPACT set
      {x in dom f = R^2_+ : ||x - y|| = t}, which omits y. Note D_f(x,y) stays FINITE at
      boundary points where x_j = 0, with the convention 0 ln 0 = 0.
  (B) grad f(U) = R^2 = U*.
  (C) f*(u) = e^{u_1} + e^{u_2} is locally uniformly totally convex at every point of
      U* = R^2, by the same compactness argument applied to the locally uniform modulus.
  (D) Our C is COMPACT, hence boundedly compact, and is ->D_f-Chebyshev (Part I, Lemma SOL.5).
  (E) Therefore Theorem 3.13 applies, and C IS a ->D_f-sun — i.e. Luo's condition (ii) HOLDS.
  (F) Theorem 3.12(3)'s hypotheses hold for us (grad f(U) = U*; f* is smooth and strictly convex
      on R^2), so (i) <=> (iv). Our C* is nonconvex, so (iv) FAILS, so (i) FAILS.
  (G) Hence (ii) holds and (i) fails, with U = R^2_++ != R^2 = X. Since Theorem 3.12(2) asserts
      (i) <=> (ii) under U = X, and Theorem 3.12(1) gives (i) => (ii) unconditionally, our
      example shows the converse (ii) => (i) genuinely REQUIRES U = X. Their Corollary 3.14 is
      not contradicted, since it assumes total convexity at every point of X and grad f(X) = U*,
      which presuppose U = X.

YOUR JOB:
 1. Check (A)-(G) against the ATTACHED TEXT, not against your memory of the literature. Quote
    the exact hypothesis lists you are checking against. Get the definition of the modulus
    nu_f(y,t) right, and say explicitly whether the infimum is over dom f or over X.
 2. Pay special attention to (A) and (C). Total convexity in a Banach space is a real condition;
    I am claiming it is free here by finite-dimensional compactness. Is my compactness argument
    correct, including at the boundary of dom f where D_f is finite but f is not differentiable?
    For (C), the LOCALLY UNIFORM modulus takes a liminf over shrinking balls — check that the
    compactness argument really covers the liminf and not merely each fixed u.
 3. Check the standing hypotheses at the head of their Section 3 (X a Banach space, C nonempty
    closed subset of U, f Gateaux differentiable on U, etc.) are ALL satisfied by our example.
    If any fails, the whole claim collapses and you should say so.
 4. INDEPENDENTLY of Theorem 3.13, try to verify or refute the sun property DIRECTLY from
    Definition 3.11 for our concrete example: for x in U and y = P^->_C(x), is y still the right
    projection of z_lambda = lambda x + (1-lambda) y for every lambda >= 0 with z_lambda in U?
    A direct verification (or a concrete failure) is worth more than the citation. Note the
    reduction: minimising D_f(z, c(t)) over t is minimising h_z(t) = e^t + e^{-t^2} - z_1 t +
    z_2 t^2, so the projection parameter t_z depends on z only through (z_1, z_2), and the
    first-order condition is e^t - 2t e^{-t^2} - z_1 + 2 z_2 t = 0. Work with that.
    If the direct check CONTRADICTS (E), that is the most important thing you can tell me: it
    would mean one of the total-convexity hypotheses fails and my reading of 3.13 is wrong.
 5. Separately: does anything in the attached text ALREADY state that U = X is essential in
    3.12(2), or already give an example like ours? If they have already observed this, the
    second claim is theirs, not ours, and I need to know that now.

Be adversarial. I would rather lose this second claim now than publish it wrong. End with a
clear verdict on the sharper claim: CONFIRMED / REFUTED / CONFIRMED-BUT-ALREADY-KNOWN, with
reasons."""

NOVELTY = SETUP + r"""

YOUR LANE: ADVERSARIAL PRIOR-ART SEARCH. Your job is to KILL our Part I claim by finding it
already published. A problem being listed as open in a 2010 survey is NOT evidence it stayed
open. Assume it is known and find where.

READ THIS POST-MORTEM FIRST — it tells you the exact failure mode you must avoid.

  This project had a SECOND result (Part II: that Fact 3.2's hypothesis (b), cl C* subset U*, is
  redundant). It was proved and survived four adversarial passes. It was then killed on novelty,
  because the earlier prior-art reader asked the WRONG QUESTION about Luo et al. (2019). That
  reader asked "did Luo remove the FULL DOMAIN hypothesis?", correctly answered "no, their
  Theorem 3.12(2) still carries U = X", and stopped. But the question that mattered was "did Luo
  remove the hypothesis WE remove?" — and their Theorem 3.12 never assumed dual closure at all,
  so Part II fell out of their machinery in three lines. A correct answer to the wrong question
  cost this project a result.
  THE SAME READER WROTE THE PART I CLEARANCE. Your job is to find the analogous wrong question.
  Do not clear Part I by confirming that nobody removed full domain. Ask instead: does anything
  in the literature ALREADY IMPLY that full domain cannot be removed, or already contain an
  example that does what ours does, or make ours routine?

SEARCH EXHAUSTIVELY, and be specific (titles, authors, years, venues, arXiv ids, DOIs, URLs):

 1. Any published example of a NONCONVEX set that is right D_f-Chebyshev (equivalently, by the
    duality, a nonconvex LEFT D_{f*}-Chebyshev set for f* = sum of exponentials) with f of
    non-full domain. The survey (arXiv:1003.3127) has its own Example 3.3 and related examples —
    read them and say whether ours is a variation of one of them.
 2. The survey's Problem 4 asks for a CHARACTERIZATION of right D-Chebyshev sets for the
    negative entropy. If anyone has answered it, that answer subsumes our example and kills the
    claim. This is our declared kill criterion #2 — check it hard.
 3. Anywhere Fact 3.2 (or Bauschke-Borwein-Combettes / Bauschke-Wang-Ye-Yuan antecedents) is
    restated with dom f = X WEAKENED or replaced, or where someone remarks that it cannot be.
 4. Luo, Meng, Wen & Yao (2019) and everything citing it; Laude, Ochs & Cremers, JOTA 184 (2020),
    arXiv:1907.04306; Themelis & Wang, arXiv:2506.00465 (2025); and the Bregman-projection /
    D-Chebyshev-set / Bregman-sun literature 2010-2026 generally.
 5. Whether the ENTROPY-specific phenomenon here is folklore: the map t -> (t, -t^2) is just a
    parabolic arc in the dual, and our C is its preimage under the coordinatewise exponential.
    Somebody may have written down exactly this. Search for it as a dual-side statement too: a
    strictly concave arc in R^2 that is left-Chebyshev for the Bregman distance of
    f*(u) = e^{u_1} + e^{u_2}.
 6. Textbook/monograph treatments (Bauschke-Combettes; Butnariu-Iusem; Censor-Zenios;
    Borwein-Vanderwerff) that may contain this as an exercise or remark.

DELIVERABLE: VERDICT RED (already published — exact reference and what it says) / AMBER
(adjacent work a referee will demand we cite or distinguish) / GREEN (no resolution found;
state your coverage). List the works actually examined and what each does. Name everything that
MUST be cited. State explicitly what you could NOT check (paywalls, unreachable databases) so a
human can judge the coverage. If the honest answer is that the result is small but new, say
that; if it is that the result is new only when stated very narrowly, tell me the narrowest
statement that survives."""

TARGETS = {"v1_maths": (MATHS, PROOF, False),
           "v2_sun": (SUN, PROOF + LUO_TEXT, False),
           "v3_novelty": (NOVELTY, PROOF, True)}

TAIL = ("\n\nEnd with: VERDICT: SURVIVES | MINOR_REPAIRS | MAJOR_ISSUES | FATAL "
        "(or RED/AMBER/GREEN for the prior-art lane), then a numbered issue list "
        "(location, claim, why wrong, suggested fix).\n\nATTACHMENTS FOLLOW.")


def retry(fn, what, tries=60, wait=30):
    for i in range(tries):
        try:
            return fn()
        except (openai.APIConnectionError, openai.APITimeoutError, openai.InternalServerError) as e:
            print(f"  ({what}: {type(e).__name__}, retry {i+1}/{tries})", flush=True)
            time.sleep(wait)
    raise RuntimeError(what)


def run(name):
    prompt, att, websearch = TARGETS[name]
    client = openai.OpenAI(api_key=KEY)
    with _lock:
        known = json.loads(IDS.read_text()) if IDS.exists() else {}
    if name in known:
        print(f"{name}: resuming {known[name]}", flush=True)
        resp = retry(lambda: client.responses.retrieve(known[name]), f"{name} retrieve")
    else:
        kw = {"tools": [{"type": "web_search", "search_context_size": "high"}]} if websearch else {}
        resp = retry(lambda: client.responses.create(
            model=MODEL, input=[{"role": "user", "content": prompt + TAIL + att}],
            reasoning={"effort": EFFORT}, background=True, **kw), f"{name} create")
        with _lock:
            known = json.loads(IDS.read_text()) if IDS.exists() else {}
            known[name] = resp.id
            IDS.write_text(json.dumps(known, indent=1))
        print(f"{name}: submitted ({MODEL}, effort={EFFORT}"
              f"{', web_search' if websearch else ''}), id = {resp.id}", flush=True)
    t0 = time.time()
    while resp.status in ("queued", "in_progress"):
        if time.time() - t0 > 14400:
            raise TimeoutError(name)
        time.sleep(20)
        resp = retry(lambda: client.responses.retrieve(resp.id), f"{name} poll")
    if resp.status != "completed":
        raise RuntimeError(f"{name}: {resp.status}: {getattr(resp, 'error', None)}")
    out = BASE / f"verify1_{name}_20260813.md"
    out.write_text(f"# Part I verification gate — {name} ({MODEL}, effort={EFFORT}, "
                   f"{time.strftime('%Y-%m-%d %H:%M')})\n\n"
                   "> Independent re-verification of Part I before write-up. The prior-art lane\n"
                   "> was briefed on how the Part II clearance failed, so it looks for the\n"
                   "> analogous wrong question rather than repeating the same check.\n\n"
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
