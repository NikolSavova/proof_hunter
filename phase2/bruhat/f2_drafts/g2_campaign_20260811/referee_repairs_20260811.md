# Referee report: repairs_20260811.md (repair-application session)

*Verifier session, 2026-08-11. Target: `repairs_20260811.md` + all scripts and
archived outputs under `g2_scripts/campaign_20260811/repairs/`. Method: every
script re-run and diffed byte-for-byte against its archived `out_*.txt`; every
STATUS.md §2a/§2b/§3 repair checked off against the doc, the scripts, the
referee reports, and the underlying drafts; the load-bearing exact-arithmetic
claims re-derived by hand where feasible. No file modified; this report is new.*

**VERDICT: SURVIVES.** Every repair in STATUS §2a (R1–R5), §2b (1–8), and §3
(F1–F9) is genuinely applied, and every numeric claim traces to a saved script
whose archived output reproduces exactly. No repair was skipped, misapplied, or
claimed without a script. The no-erasing rule was respected (verified: the
originals still contain their bugs). Three label-precision observations are
recorded in §5 — none demands a change; the repairs doc itself already carries
the honest phrasing in each case.

## Contents
1. Reproduction protocol and results (all scripts)
2. §2a (wp1-c R1–R5) — item-by-item verification
3. §2b (wp2-b 1–8) — item-by-item verification, incl. hand-checked identities
4. §3 (T2 F1–F9) — item-by-item verification, incl. the T.9-Step2' chain
5. Observations (non-blocking)
6. What remains (unchanged; confirmed accurate)

---

## 1. Reproduction protocol and results

All runs 2026-08-11 (this session), CPython 3.12, same machine class as the
repair session. Each command's stdout was diffed against the archived output.

| script / artifact | re-run result |
|---|---|
| `rep_wp1c_repairs.py` vs `out_rep_wp1c.txt` | **byte-identical**; VERDICT PASS |
| `rep_t2f1_blam_chain.py` vs `out_rep_t2f1.txt` | **byte-identical**; VERDICT PASS |
| `rep_wp2b_extras.py` vs `out_rep_wp2b_extras.txt` | **byte-identical**; VERDICT PASS |
| `rep_t2_numerics.py` vs `out_rep_t2_numerics.txt` | **byte-identical**; VERDICT PASS |
| `wp2_b/wp2b_nc{2,3,4}*.py` (originals) vs `out_nc{2,3,4}_orig.txt` | **byte-identical** (all three) |
| `repairs/wp2b_nc{2,3,4}_*_fixed.py` vs `out_nc{2,3,4}_fixed.txt` | **byte-identical** (all three); all self-report PASS |
| `t2/t2_nc10_far.py` (untouched original) vs `out_t2_nc10_rerun.txt` | **byte-identical** |
| `t2/t2_nc5_cf.py` (untouched original) vs `out_t2_nc5_rerun.txt` | **byte-identical** |

The §D no-digit-moves claim was re-established independently:
`diff out_nc2_orig.txt out_nc2_fixed.txt` — empty; `nc4` — empty; `nc3` —
exactly ONE line differs, the float-precision diagnostic
`1.19e-16 -> 1.25e-16`, explicitly labeled "(float-precision comparison)" in
the output. This is precisely what repairs §D claims, no more, no less.

**Fixed-copy provenance verified by diff against the originals:** the only
changes in `wp2b_lib_fixed.py` are the docstring and the two coefficient
lines (`-u**5/22176 -> -u**5/15840`, `-u**4/4435.2 -> -u**4/3168`); the three
`*_fixed.py` NC scripts change only their import lines. **Both corrected
coefficients re-derived by hand from the Bernoulli series** of
`g(u) = 1/u - 1/(e^u - 1) = 1/2 - u/12 + u^3/720 - u^5/30240 + u^7/1209600
- u^9/47900160 - ...` (B_10 = 5/66 gives the u^9 term): the 4th derivative of
`-u^9/47900160` is `-3024 u^5/47900160 = -u^5/15840`, the 5th is
`-15120 u^4/47900160 = -u^4/3168`. Fixed values exact; the old ones were off
by 5/7, as both wp2-b referees found.

**No-erasing rule verified:** the originals still contain their defects —
`wp2_b/wp2b_lib.py` lines 55/62 still read `/22176` and `/4435.2`;
`t2/t2_nc5_cf.py` line 15 still has the docstring typo `0.015549`. All
repairs are new files; no draft was edited (errata are recorded for
paper-assembly, per the stated protocol).

---

## 2. STATUS §2a — wp1-c repairs R1–R5: all APPLIED and certified

- **R1 (A1) — APPLIED + certified.** All 13 constants recomputed two ways
  (closed form vs independent quadrature, dps 60, agreement < 1e-50 asserted
  in-script); every margin positive; min = 9.116e-6 at `c_1(0)`; the six
  sub-5e-5 constants are exactly the referees' list. The restated claim
  "margin >= 9e-6" is TRUE; erratum text recorded. Output reproduces.
- **R2 (A2) — APPLIED.** `2 asinh(sqrt 10) = 3.7371022422` certified;
  erratum "3.7358 -> 3.7371" recorded. Non-load-bearing, as stated.
- **R3 (A3) — APPLIED (text-only, correctly so).** I checked the restated
  W.5(iii') against `wp1_draft_c.md` §5's actual proof: case 1 does establish
  the bound on ALL of `[pi/m, pi]` for `|lam| <= pi/m`, and case 2 on
  `[t_0(lam), pi]` for `pi/m <= |lam| <= 1.7627`, both with
  `c_V = q(1.5700, 1.00183) = 0.0372`. The restatement is exactly the proof's
  two cases; no number involved; A1 re-certifies the constants. Correct.
- **R4 (A4) — APPLIED + certified.** The one-line proof is mathematically
  correct (checked by hand: `F = cosh x sin x - sinh x cos x`, `F(0) = 0`,
  `F' = 2 sinh x sin x > 0`, `(sinh x/sin x)' = F/sin^2 x > 0`); the script
  certifies the derivative identity (max rel dev 1.69e-61), grid
  monotonicity, and `tan > tanh` spots. This replaces the grid-only
  certification at `wp1_draft_c.md` line ~457, making the "no grid
  certificates" claim true — as required.
- **R5 (A5) — APPLIED + certified.** Unit-step scans reproduce all four
  thresholds exactly: 292672 / 1065849 (old exponent, easy/worst) and
  879 / 185 (new exponents) — matching wp1-c's quoted values; the reworded
  "(V) reproduced" erratum matches the referee's demand. (Also discharges
  T2-F3, see §4.)

No constant, lemma, hypothesis, or threshold changed — confirmed.

---

## 3. STATUS §2b — wp2-b repairs 1–8: all APPLIED and certified

- **B1 — APPLIED + certified.** Fixed copies only (originals untouched);
  coefficient derivation verified by hand (§1); NC-W2/3/4 re-run; the
  no-digit-moves prediction holds exactly (§1). The NC-W1 exclusion is
  properly justified (it does not exercise the fallbacks; regeneration would
  violate no-erasing; the maths referee already verified byte-identical
  regeneration).
- **B2 — APPLIED as errata (correct form).** Relabel W.6 grid-certified,
  `c_w(4) = 1`, spurious-addend note — all text-level; the underlying numbers
  (0.4067 / 0.4658 / 0.9506, worst at m = 180) confirmed present in the
  reproduced `out_nc4_*` outputs. The optional per-piece-monotonicity upgrade
  is honestly deferred to "What remains".
- **B3 — APPLIED + certified.** The referee's beyond-grid point reproduced to
  all four digits: 4.9233 at (20000, 2.725), with the extension 4.9234 at
  m = 50000 still rising; restated working figure 4.93 with the certified row
  kept at "m <= 2000"; `C_R^PT grid` K=4 restated 5.32 = safe rounding of
  4.93 + 0.01402 + 0.3719 = 5.3159 (STATUS suggested "~5.31"; 5.32 is the
  conservative direction — fine). See observation O2.
- **B4 — APPLIED + certified.** Exhaustive integer sweep m = 30..400 x 200
  w-points with exact integer band sums: max 0.379644 at (32, 4.0) — the
  referee's value to all six digits; <= 0.40 so `c_4 = 0.60` stands. See
  observation O1 on the word "exhaustive".
- **B5 — APPLIED + certified in exact arithmetic; identities re-derived by
  hand.** (i) I expanded `330 m^2(m-1)(2m+5) - 100(m+1)(2m+1)(3m^2+3m-1)`
  independently: `60m^4 - 510m^3 - 2650m^2 + 100 = 10(6m^4 - 51m^3 - 265m^2
  + 10)` — matches; `6*900 - 51*30 - 265 = 3605 > 0` with vertex `51/12 < 30`
  — the positivity argument is complete; and the reduction from
  `coef(m) <= 33/1000` (via `S_4 = m(m+1)(2m+1)(3m^2+3m-1)/30`,
  `lambda = m(m-1)(2m+5)/72`) is algebraically exact. (ii) I re-derived
  `30(120m^5 - 545(S_4+m)) = 330m^5 - 8175m^4 - 5450m^3 - 15805m` — matches
  q4 exactly; the termwise dominations at m >= 30 check out (330*30 = 9900 >=
  8175+1725; 1725*30 = 51750 >= 5450+46300; 46300*900 >= 15805; and for q6,
  2466*30 = 73980 >= 31500+42480, 42480*30 >= 31500+64500). The exhaustive
  Fraction checks (30..5000 / 30..3000) reproduce. W.1(i) is now genuinely
  PROVED for all m >= 30 — this is what T2-F1's repair chain consumes.
- **B6 — APPLIED as erratum.** The Delta_ker caveat sentence; text-only,
  structurally correct given W.7's decomposition.
- **B7 — APPLIED + certified.** Signed sum measured [+0.0050, +0.0114] on an
  enlarged (m, w) set, consistent with the referee's [+0.0050, +0.0109]
  (the doc correctly attributes the upper-end extension to the added m/grid
  points); the reworded Finding matches the referee's demand.
- **B8 — APPLIED + certified, all seven sub-items.** 15 weight-8/10 monomials
  (28 = 5 + 8 + 15, counted from the committed table); 187.414 confirmed in
  the reproduced nc4 output; numpy-banner drop (text); `v > 0` proved on
  W.7's stated scope m >= 180 via the nc3 boxes (sufficient condition 0.0080
  .. 0.1053 < 1 at every in-scope table point; the K=4, m=30 failure is
  correctly noted as outside scope with the harness covering it); Lin
  monotonicity one-liner (the derivative computation is correct) + numeric
  confirmation 0.3719/0.2795/0.1346/0.0674; Hermite sups re-run on the full
  stated `|y| <= 1/2` (max ratio 1.0000); `1.000016` (1.0000153 at K=4).

Both restated table entries (4.93-scope and 0.379644) are exactly the two the
referees demanded, in the measured direction — confirmed.

---

## 4. STATUS §3 — T2 numerics repairs F1–F9: all APPLIED and certified

- **T1 = F1 (the mathematical repair) — APPLIED; the new chain is SOUND.**
  I verified Lemma T.9-Step2' end to end:
  * *Cited inputs exist and are in scope.* (2)'s recentred bound
    `|kappa_4(lam) - kappa_4(0)| <= w^2 m^5/2200` is (T.4') verbatim
    (`g2_draft_t2_20260803.md` line 469; note `kappa_4(0) = -S*_4/120`, so
    the recentring is exact); `S*_4 >= m^5/5` is T2's certified bracket
    (line 400, B.0-style, m >= 30 — covering the lemma's scope); hence
    `c_A = (m^5/2200)/(m^5/600) = 600/2200 = 3/11` is legitimate. (3)'s
    `delta <= 0.0330 w^2` is wp2-b Lemma W.1(i) (`wp2_draft_b.md` line 128),
    upgraded to all m >= 30 by repair B5 — the dependency is real and now
    proved, so the chain does NOT rest on a sampled range.
  * *The corrected inequality.* The identity `(1-d)^{-2} - 1 - 2d = d^2
    (3/(1-d) + d/(1-d)^2)` is exact (script asserts it in Fractions; I
    checked it symbolically); phi increasing on [0,1) is right (positive
    power-series coefficients); I recomputed `phi(33/1000) =
    2901000/935089 + 33000/935089 = 2934000/935089 = 3.1377 <= 3.5` by hand
    — matches the script's exact rational.
  * *Assembly.* `c_R = 2(0.033) + 3.5(0.033)^2 = 0.0698115`;
    `c_A + c_R + c_A c_R = 0.361578 <= 0.362` (exact Fractions in-script;
    the `w^4 <= w^2` absorption on `|w| <= 1` is used correctly); lower side
    `>= 1 - c_A w^2` uses `R >= 1` correctly.
  * *Downstream.* `0.362 + 0.09 = 0.452 < 0.5` exact — the `c_w = 1/2`
    sub-claim of T.9 Step 2 closes on `|w| <= 1`; wider `w` correctly
    delegated to Prop W.6 (with its post-B2 grid-certified label and
    `c_w(4) = 1`).
  * *Truth margin.* Referee's 0.1134 reproduced; dual-precision agreement
    asserted at every grid point. (The untilted reference uses lam = 1e-12
    rather than exact 0 — measurement-only, harmless at the 2e-5 tolerance.)
  * The old display's falsity is reproduced (FALSE at d = 0.033, 0.1, 0.35).
- **T2 = F2 — APPLIED.** Chain gives 2.6113e-4 > printed 2.61e-4 (unsafe);
  corrected 2.62e-4 certified; (T.9''b)'s 2.8e6 confirmed safe (2.8548e6).
- **T3 = F3 — APPLIED** (via R5's scans): 292672 (~2.9e5, easiest point) and
  1065849 (~1.07e6, worst case); "~2.5e5" confirmed not reproducible; the
  referee's own 2.96e5 (`ref_misc_recheck.py`) differs from 292672 at
  loop-grain/convention level only — same order, both catastrophic, and the
  erratum wording says exactly that. Honest.
- **T4 = F4 — APPLIED.** The untouched `t2_nc10_far.py` re-run reproduces
  byte-identically; I recomputed the slacks from its part-(c) rows myself:
  0.9955/1.262e-3 = 789x (min) and 0.6143/1.447e-8 = 4.25e7x (max) — the
  erratum "789x–4.25e7x" is exactly right; "24x" indeed matches nothing.
- **T5 = F5 — APPLIED.** FALSE at (4,3) and (5,3) (1.5625 < 4, 3.24 < 5),
  TRUE for m >= 6, exact Fractions; erratum m >= 4 -> m >= 6; lemma scope
  unaffected. Certified.
- **T6 = F6 — APPLIED.** 17.000 at m = 2 (chain fails) / 11.879 at m = 3;
  the direct m = 2, w = pi check (deficit 0.43007 <= pi^2/20 = 0.49348) uses
  the correct model (only the j = 2 factor carries variance; untilted
  lambda = 1/4). Certified.
- **T7 = F7 — APPLIED.** Dropped-term relative size `5w^2/(19m^4)`: max
  3.21e-6 (= 5 pi^2/(19*30^4), which I confirmed) <= 3.3e-6; absorbed by the
  0.02857 -> 0.0285 rounding. Display fix recorded.
- **T8 = F8 — APPLIED.** (i) `42/1209600 = 1/28800` exact (and consistent
  with my §1 Bernoulli re-derivation; the corrected ratio remark 1/19.05
  keeps the alternating argument valid); numeric limit 3.4718e-5 agrees.
  (ii) `q(1+q)/(1-q)^2 = 6.2939` at q = e^{-1/2} (hand-checked), 317.77 >
  316 so the downstream claim survives a fortiori. (iii) sin^2(1/8) =
  0.0155438; the docstring typo is real (original line 15 still says
  0.015549 — correctly left in place under no-erasing, correction recorded).
- **T9 = F9 — RECORDED (as demanded — a flag, not a change).** The archived
  `out_t2_nc5_rerun.txt` reproduces; max ratio 0.0167 at (30, 0.001) = the
  ~60x headroom quoted. Properly left for the T2 maths referee.

The C-summary's scope discipline is correct: these repairs feed the T2 maths
referee pass and are not claimed to substitute for it.

---

## 5. Observations (non-blocking; no action required before citation)

- **O1 (B4 wording).** The headline "EXHAUSTIVE sweep" covers every integer
  m in [30, 400] (x a 200-point w-grid); m > 400 still rests on the prior
  sampled tail (500..3000) + continuum limit. The erratum text itself states
  this precisely ("still grid-certificate class in w, Sturm-able on demand")
  — keep that precise phrasing, not the headline, at paper-assembly.
- **O2 (B3 scope).** "Global max on extended range = 4.9234" is over a
  targeted w-window (2.6..2.9) around the known maximizer and five m values
  up to 5e4, and the sequence is still (slowly) rising at m = 5e4. The doc
  correctly carries 4.93 as a *working figure* with the certified row pinned
  at "m <= 2000"; any eventual closed-form K = 4 row must not silently
  promote 4.93 to certified.
- **O3 (T1 header nit).** `rep_t2f1_blam_chain.py`'s header cites
  "S*_4 >= m^5/5 (m >= 8)"; T2's certified bracket is stated for m >= 30.
  The lemma's scope is m >= 30, so nothing is affected (the m >= 8 claim is
  also trivially true, but "certified" should read m >= 30).

None of these affects a constant, a conclusion, or a citation.

---

## 6. What remains — confirmed accurate

The repairs doc's closing list matches STATUS §4 items 2–5 verbatim: the T2
MATHS referee pass (house-rule debt — untouched by this session, correctly so),
wp2-a's `Delta_ker` bucket, the harness extension to m ~ 200, Prop 3.5(i)'s
open mathematics, and the optional upgrades (W.6 per-piece monotonicity,
signed kappa_3/kappa_5 boxes, Sturm certificates). No overclaim found: the doc
nowhere asserts G2 or Theorem A is closed, and it correctly re-flags the
single-referee status of T2's inventory.

**Final verdict: SURVIVES.** STATUS §4 item 1 ("apply the listed repairs") is
discharged: wp1-c and wp2-b are citable with their repair lists applied;
T2's repairs F1–F9 are in place as input to the still-outstanding maths pass.

*End of referee_repairs_20260811.md.*
