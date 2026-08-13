#!/usr/bin/env python3
"""Cross-model attack on (S1)-(S4) with OpenAI gpt-5.6-sol (house rule: cross-examine
with the other model). One call per statement, narrow scope — the same decomposition
lesson the Claude fleet learned. Outputs are SINGLE-MODEL, UNREFEREED drafts, saved as
sol_<target>_20260812.md next to the campaign ledgers; nothing counts until the usual
two-referee pass. Pattern per killsearch.py: Responses API, background=True, poll.

Usage: ./run_sol.py [target ...]   (default: s1 s2 s3 s4)
"""
import json, os, pathlib, sys, time

import openai

ROOT = pathlib.Path(__file__).resolve()
BRUHAT = ROOT.parents[4]                      # wave6_sol -> campaign -> g2_scripts -> f2_drafts -> bruhat
CAMP = BRUHAT / "f2_drafts" / "g2_campaign_20260811"
KEY = (pathlib.Path.home() / ".config/proof_hunter/openai_key.txt").read_text().strip()
MODEL = os.environ.get("SOL_MODEL", "gpt-5.6-sol")
EFFORT = os.environ.get("SOL_EFFORT", "high")
POLL_S, TIMEOUT_S = 20, 7200


def read(name, cap=60_000):
    p = CAMP / name
    return f"\n\n===== FILE: {name} =====\n" + p.read_text()[:cap] if p.exists() else ""


BASE_CTX = (
    "You are attacking one open statement in a mathematics campaign on the Mahonian "
    "distribution (coefficients of prod_{j=1..m}(1+q+...+q^{j-1}); r(k) = a_k^2/(a_{k-1}a_{k+1}); "
    "target Theorem A: sigma^2(r_m(k)-1) -> 1). A single lemma CL(79, 20, 0.89) at m >= 561 "
    "is all that remains, and CL is proved modulo four statements (S1)-(S4). The campaign "
    "ledger below states them precisely, with measured numerical margins. Everything the "
    "ledger marks two-referee/citable you may use as established; everything marked open is open."
    + read("STATUS_wave5.md")
    # NOTE 2026-08-12: wave5 predates (S1)'s proof. wave6 is the current ledger —
    # agents briefed on wave5 alone wrongly report (S1) as open.
    + read("STATUS_wave6.md", 40_000)
    + read("CL_composition_20260812.md", 40_000)
)

TARGETS = {
    "s1": ("Prove (S1), the banded cumulant scale bounds, band by band. A constants re-architecture "
           "plan may accompany this prompt (FILE wave6_s1_plan_20260812.md below); if present, prove the "
           "RE-ARCHITECTED targets (they carry more margin), else the ledger's originals. "
           "If a band resists, prove the best constant you can and state the delta."
           + read("wave6_s1_plan_20260812.md", 40_000)),
    "s2": ("Prove (S2), the R5 bound, exactly as the composition consumes it."),
    # Attempt 2: attempt 1 was FATAL because the prompt gave it no band definitions.
    # The full brief now lives in a reviewable artifact; attempt 1 + its referee report
    # are attached so the correct machinery is reused and the framing errors are not.
    "s2b": ("PROVE (S2), second attempt. Your complete brief is the first file below — "
            "read it in full and follow it exactly; it states the bands, the constants, "
            "the model, and (critically) WHY a cancellation-free bound cannot work. The "
            "remaining files are attempt 1 and its adversarial referee report: attempt 1's "
            "lemmas are verified correct and reusable, but it proved none of the seven "
            "bounds and made framing errors the brief lists. Do not repeat them."
            + read("s2b_briefing.md", 20_000)
            + read("sol_s2_20260812.md", 45_000)
            + read("referee_maths_sol_s2.md", 55_000)),
    # Attempt 3: numerics fully replayed cross-model; this run closes the MATHS lane.
    "s2c": ("CLOSE (S2) — attempt 3. Your brief is the first file below; follow it exactly. "
            "Attempt 2's numbers have ALL been independently reproduced, so this run is not "
            "about numerics: it must supply the missing DERIVATIONS, fix the five named "
            "defects (cell width; the underivable 2w in SOL.7.8; the unaudited lemmas; the "
            "four razor-thin margins incl. G(0.89) at 0.056% slack; the undefined G and F_1), "
            "and produce ONE self-contained rigorous proof of (S2). The remaining files are "
            "attempt 2 and the cross-model replay report that verified it."
            + read("s2c_briefing.md", 25_000)
            + read("sol_s2b_20260812.md", 60_000)
            + read("referee_replay_sol_s2b_20260812.md", 30_000)),
    # ---- parallel closure fleet, 2026-08-12 (Sol replaces the Fable fleet; always max) ----
    "s3w7sign": ("""CLOSE THE (S3) W7 SIGN GAP. Context: the adversarial maths referee of sol_s3_20260812.md
found its ONE genuinely mathematical hole (its issue 4), and it is the blocking item for (S3):

  In SOL.4 the draft asserts 0 <= B <= m h_3(lam), where B = m h_3(lam) - sum_{j=1}^m h_3(j lam).
  Nonnegativity of the summands gives only B <= m h_3(lam). The bound on B^2/A^2 in (SOL.12)
  needs |B| <= m h_3, for which B >= 0 is LOAD-BEARING and is nowhere proved.

A cross-model check has now reduced this to a single-variable inequality — your job is to prove it
rigorously and assemble the consequence.

  (i) B >= 0 follows IMMEDIATELY if h_3 is decreasing on (0, oo): j lam >= lam for j >= 1, so
      h_3(j lam) <= h_3(lam), hence sum_j h_3(j lam) <= m h_3(lam).
  (ii) h_3(x) = x^3 sum_{k>=1} k^2 e^{-kx} = 2 y^3 cosh(y)/sinh^3(y) with y = x/2. Then
       (log h_3)'(y) = 3/y + tanh(y) - 3 coth(y), so h_3 is decreasing iff
             3(coth y - 1/y) > tanh y      for all y > 0.
       Series: 3(coth y - 1/y) = y - y^3/15 + 2y^5/315 - ...,  tanh y = y - y^3/3 + 2y^5/15 - ...,
       so the difference is (4/15) y^3 + O(y^5) > 0 near 0. Numerically the inequality holds on the
       whole half-line (checked: max of h_3' over a fine grid on (0,45] is -2.55e-15 < 0).
  PROVE (ii) rigorously for ALL y > 0 (not just numerically) — a clean proof of
  3(coth y - 1/y) - tanh y > 0 — then state (i) as a corollary and write out the corrected SOL.4
  step with B >= 0 justified.

ALSO in the same document, close the second, smaller referee item (its issue 5): (SOL.13)'s
half-line application assumes the B_8 endpoint term vanishes. Prove it: h_n^(7)(0) = 0 for n = 2,3,4
(h_n is EVEN, so all odd derivatives vanish at 0) and h_n^(7)(x) -> 0 as x -> oo (exponential decay).
State it as a lemma with proof. NOTE it does NOT rescue the finite-w case, where h_n^(7)(w) != 0 —
there the corrected kernel constant must be used (see Lemma EM' below).

CORRECTED REMAINDER LEMMA you must use throughout (established, exact-arithmetic verified):
  With the expansion retaining endpoint terms through B_6 and NO B_8 endpoint term,
    |E_{n,8}| <= (17/10321920) lam^8 int_0^w |h_n^(8)|,   since sup_x |B_8({x}) - B_8| = 17/256
    = (2 - 2^-7)|B_8|; the draft's 1/1209600 is the B_8-endpoint-term form and is NOT available.
Also established and citable: |h_n^(8)| <= 10^12 on (0,40] is now CERTIFIED (Cauchy bound on
|z|=6 for x in [0,1]; direct Leibniz series on [1,40]), and Lemma SOL.3's compact bands W1-W6b are
certified at cell width 1/128."""),

    "s3w7cert": ("""SUPPLY THE (S3) W7 CERTIFICATES. Context: referee finding F1 on sol_s3_20260812.md listed
three unrun certificates. TWO ARE NOW DONE by a cross-model pass: Lemma SOL.3's compact bands
W1-W6b (executed, all certified at cell width 1/128, using the corrected constant below), and
(SOL.5) |h_n^(8)| <= 10^12 on (0,40] (certified). THE REMAINING ONE IS YOURS: band W7's
(SOL.16)/(SOL.17), together with the W7 lemmas the referee listed as load-bearing-but-unsupported:
    h_2 - dT_2 > 9/10,   h_4 - dT_4 > 49/10,   U_7 <= 12/5,   int_0^oo |h_n^(8)| < 10^12.
W7 is the band 40 < w <= 0.89 m (so up to w = 499.29 at m = 561) — the compact-band cell method does
not reach it; give an analytic treatment with explicit constants, or a certificate whose cell count
is stated and finite.

CORRECTED REMAINDER LEMMA you must use (established, exact-arithmetic verified): with endpoint terms
through B_6 and no B_8 endpoint term, the kernel constant is 17/10321920 = (2 - 2^-7)|B_8|/8!, NOT
the draft's 1/1209600 (sup_x |B_8({x}) - B_8| = 17/256, verified exactly and on a 2000-point grid).
Every W7 bound you write must carry this constant. Note also that the W7 sign hypothesis B >= 0 is
being closed separately (h_3 is decreasing) — you may assume it, but flag where you use it."""),

    "s4seed": ("""PROVE THE (S4) SEED LEMMA — the last piece of (S4). Context: the first maths referee of
wave4_sl4p_repaired_20260812.md established (its M2) that the INFL/QUADF self-consistency bootstrap
CLOSES given one a-priori input, and supplied the closure argument itself:

  G(x) = a(1+u) + b(1+u)/(1-u) with u = Theta + d is convex increasing; the two endpoint evaluations
    G(20/m) = 0.0491712 < 20/m = 0.0498753   (W5 at m = 401)
    G(20/m) = 0.0421217 < 20/m = 0.0431965   (W1 at m = 463)
  give G < id on all of [20/m, 0.89] by a chord argument, and the monotone iteration
  x_{n+1} = G(x_n) descends from any seed in the basin to a fixed point < 20/m. Measured basin:
  x_seed = sup{x : G(x) <= x} = 0.90182 (W5) / 0.89412 (W1 @ 463).

  THEREFORE the ONLY open input is the a-priori SEED BOUND:
        |s2 (r(k) - 1) - 1| <= 0.89     on the deep-tilt band, for m >= 700.
  (The obligation starts at m >= 700: the same referee's M3 finding closes [561, 699] outright by
  per-cell floors — worst row bound 0.416537 at m = 561 — so you need only m >= 700.)

PROVE THAT SEED BOUND. Notes that should make it easier than it looks:
 * 0.89 is an ENORMOUSLY loose target — the truth is O(1/m), i.e. ~0.03 at m = 700 and shrinking.
   You do not need sharpness, only a crude two-sided bound. Do not attempt a sharp estimate.
 * The referee characterises it as "weak-CL-shaped": log-concavity of the tilted Mahonian law gives
   the LOWER side (r >= 1, hence s2(r-1) >= 0) for free via Bona's classical result; the work is the
   UPPER side, s2(r(k)-1) <= 1.89.
 * Established, citable machinery: s2 = m A_1(lam) - sum_j j^2 A_1(j lam) with
   A_1(z) = e^-z/(1-e^-z)^2; the tilted cumulant identity
   L^(n)(lam) = (-1)^n (m A_{n-1}(lam) - sum_j j^n A_{n-1}(j lam)); the far-region bounds of wp1-c
   (two-referee); Prop 3.5(ii) = Theorem T.9-final (CLOSED); and G(y) = y^2 A_1(y) is decreasing with
   int_0^oo G = pi^2/3.
If the 0.89 target is unreachable by crude means, prove the best constant you can and say exactly
what it is — the bootstrap basin is ~0.90, so anything below that still closes M2."""),
    "comprepair": ("""REPAIR THE COMPOSITION. Context: `CL_composition_20260812.md` is the document that
converts the four statements (S1)-(S4) into CL(79, 20, 0.89) for m >= 561. Its adversarial maths
referee returned MAJOR_ISSUES with seven findings (full report attached). Two of them are NEW
MATHEMATICS, not bookkeeping, and they are the reason closing (S1)-(S4) would NOT by itself close
CL. Your job is to produce a corrected composition that answers all seven.

THE TWO SUBSTANTIVE ONES:

 (a) FINDING 1 — a MISSING w-CONTINUUM CERTIFICATE (effectively a fifth hypothesis).
     Fact R.G's universal W1 rung rests on 25,122 = 237*106 probes, i.e. a FINITE w-grid.
     Theorem X.1 gives monotonicity in tau, NOT in w, so it does not interpolate between the 106
     sampled w-values; and probing w = 4 + 1e-9 does not cover 4 < w < 4 + 1e-9. The proposed M3
     replacement (per-cell floors from Lemma R.1) is asserted but never reproduced: no bound, cell
     formula, endpoint argument, or landed lemma. EITHER write out the M3 per-cell-floor argument
     in full as a proved w-uniform statement on (4, 5], OR supply a genuine w-continuum interval
     certificate, OR state it explicitly as a fifth hypothesis. Do not leave it as probes.

 (b) FINDING 2 — the (S4) BOOTSTRAP CLOSURE IS INSUFFICIENT AS STATED.
     With x = |s2(r-1) - 1| and a = 20/m, deducing x <= a needs BOTH x <= G(x) and G(t) < t for
     all a < t <= 0.89. Convexity plus G(a) < a does NOT give the second: a convex increasing
     function can cross the diagonal later. A chord argument additionally needs a rigorous
     G(0.89) < 0.89, the correct inequality direction, and a reduction showing the two thinnest
     rows dominate every band and every m >= 561. Note 0.89 sits only ~0.00412 below the quoted
     worst basin, so directed rounding matters. State this as a lemma with G, its domain, endpoint
     signs, and uniformity — a citation to an unlanded referee construction is not enough.
     (The (S4) seed lemma itself has now been drafted separately — attached — for m >= 700.)

THE FIVE BOOKKEEPING ONES (fix each explicitly):
 3. The band table W1-W7 is never defined in the composition: import it with open/closed endpoint
    conventions, and give the EXACT rational J_0(W) values, not decimals.
 4. Theorem E is invoked by substituting (S1)+(S3), but its hypotheses are (E-A2)+(E1)+(E2)+(E3):
    identify them clause by clause, and check whether E2 needs a signed or absolute fourth-cumulant
    bound and whether its band-edge conventions match S1's.
 5. `min(m, s2) = m` is used but NOT established: the only universal floor stated is
    s2 >= 1122800/7921 = 141.749779..., which is LESS than every m >= 561. Quote the exact bandwise
    formula proving s2/m >= 1 and check its worst band edge.
 6. Input I3 consumes the hygiene overlay's M_H = 560 repair, but that overlay has zero referees.
    Either stop consuming it or mark the dependency honestly; the claim that every input is
    two-referee is currently false.
 7. Prop E.3 shows the OLD route insufficient; it does not show the joint bound is logically
    unavoidable. Reword.

DELIVERABLE: a corrected composition document that states, at the end, exactly which hypotheses CL
now rests on and their status — with no silent omissions. If the honest count is five rather than
four, say five."""
                   + read("solref_maths_CL_composition_20260812.md", 40_000)
                   + read("CL_composition_20260812.md", 45_000)
                   + read("sol_s4seed_20260812.md", 20_000)),
    "s3": ("Prove (S3), the joint-cancellation statement J <= J0(W) (worst measured margin 32.6% at "
           "(561, 5.0)). Constraint: a refereed impossibility result (Prop E.3, excerpted below) shows "
           "the sign-lemma route CANNOT work — do not use it; find another route."
           + read("wave5_sl4pe_20260812.md", 30_000)),
    "s4": ("Prove (S4), the bootstrap seed: an a-priori bound |s2(r(k)-1) - 1| <= 0.89 on the region "
           "where the INFL/QUADF bootstrap starts (context below; note [561,699] is already closed, so "
           "the obligation may start at m >= 700)."
           + read("wave4_sl4p_repaired_20260812.md", 30_000)),
}

RULES = ("\n\nRULES: complete rigorous proof with every constant explicit and named; number your "
         "lemmas SOL.1, SOL.2, ...; include a final section 'VERIFICATION RECIPE' giving exact "
         "numerical checks (formulas + expected values) a referee can script; end with an honest "
         "'WHAT REMAINS' section listing any gap, however small. If the statement is FALSE or "
         "unprovable as stated, demonstrate why and prove the strongest true variant.")


IDS = ROOT.parent / "ids.json"


def _ids():
    return json.loads(IDS.read_text()) if IDS.exists() else {}


def _retry(fn, what, tries=60, wait=30):
    """Survive transient network drops (the 2026-08-12 DNS outage killed two polls)."""
    for i in range(tries):
        try:
            return fn()
        except (openai.APIConnectionError, openai.APITimeoutError, openai.InternalServerError) as e:
            print(f"  ({what}: {type(e).__name__}, retry {i + 1}/{tries} in {wait}s)", flush=True)
            time.sleep(wait)
    raise RuntimeError(f"{what}: still failing after {tries} retries")


def run(target):
    client = openai.OpenAI(api_key=KEY)
    known = _ids()
    if target in known:
        rid = known[target]
        print(f"{target}: resuming existing response id = {rid}", flush=True)
        resp = _retry(lambda: client.responses.retrieve(rid), f"{target} retrieve")
    else:
        resp = _retry(lambda: client.responses.create(
            model=MODEL,
            input=[{"role": "developer", "content": BASE_CTX},
                   {"role": "user", "content": TARGETS[target] + RULES}],
            reasoning={"effort": EFFORT},
            background=True,
        ), f"{target} create")
        known[target] = resp.id
        IDS.write_text(json.dumps(known, indent=1))
        print(f"{target}: submitted ({MODEL}, effort={EFFORT}), id = {resp.id}", flush=True)
    t0 = time.time()
    while resp.status in ("queued", "in_progress"):
        if time.time() - t0 > TIMEOUT_S:
            raise TimeoutError(f"{target}: exceeded {TIMEOUT_S}s")
        time.sleep(POLL_S)
        resp = _retry(lambda: client.responses.retrieve(resp.id), f"{target} poll")
    if resp.status != "completed":
        raise RuntimeError(f"{target}: {resp.status}: {getattr(resp, 'error', None)}")
    out = CAMP / f"sol_{target}_20260812.md"
    header = (f"# ({target.upper()}) attempt — {MODEL}, reasoning={EFFORT}, {time.strftime('%Y-%m-%d %H:%M')}\n\n"
              "> ⚠️ SINGLE-MODEL, UNREFEREED (house rule: does not count until an adversarial\n"
              "> maths referee + numerics referee both pass it). Generated by run_sol.py.\n\n")
    out.write_text(header + resp.output_text)
    print(f"{target}: completed, {len(resp.output_text)} chars -> {out.name}")


if __name__ == "__main__":
    for t in (sys.argv[1:] or ["s1", "s2", "s3", "s4"]):
        run(t)
