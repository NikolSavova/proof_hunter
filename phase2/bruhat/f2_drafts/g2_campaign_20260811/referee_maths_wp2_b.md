# Adversarial maths referee report — wp2_draft_b (T.9 Taylor bucket, w^2-envelope audit, C_R assembly)

*Referee pass 2026-08-11. Target: `g2_campaign_undefined/wp2_draft_b.md` + its five
scripts under `g2_scripts/campaign_undefined/wp2_b/`. Blind protocol maintained: no
other campaign draft, no `g2_draft_t1`, nothing else under `campaign_undefined` was
read. Background read in the required order: `F2_PROOF_DRAFT.md`, `g1_draft_b.md`,
`g2_draft_t2_20260803.md`, `g2_item1_deep_tilt_notes_20260805.md`. The item-4 notes
(`g2_item4_bucket_notes_20260805.md`) were consulted only to verify the draft's
citation of the 1.5491/4.0889/4.9126 grid values (they match, lines 69–71).*

*Referee scripts (all saved and run 2026-08-11, CPython 3.12.2, sympy 1.14.0,
mpmath 1.3.0; scratchpad `/private/tmp/claude-501/-Users-sihaohuang-Desktop/`
`0c711691-81ac-42b2-8712-819b1ee08f6b/scratchpad/`): `ref_v1_cumulants.py`,
`ref_v2_bounds.py`, `ref_v3_taylor_truth.py`, `ref_v4_resid_limit.py`. Every number
quoted below is from a real run.*

**VERDICT: SURVIVES WITH MINOR REPAIRS.** No load-bearing step is wrong. The two
delivered buckets (Taylor, linearization), the model polynomial, the dictionary
lemmas, and the exact W.7 decomposition all verify — by hand recomputation, by
re-running the draft's scripts (all outputs reproduce exactly), and by independent
re-implementation. I found one real (benign) code bug, one status-inflation that
must be relabeled, and several small certificate gaps, listed in §3. The draft's own
honesty is high: every claimed script exists and reproduces its quoted output; the
pending kernel bucket is exactly defined and its true size measured, not hidden;
T.9 is correctly left PARTIAL.

---

## 1. What I verified and how

### 1.1 Hand recomputations (independent of all scripts)

1. **Fourier rule** `(1/2pi) int t^n e^{-s2 t^2/2} e^{-itx} dt = (-i)^n s2^{-n/2}
   Z(y) He_n(y)`: rederived from differentiation under the integral. Correct.
2. **Model polynomial (Lemma W.0).** Expanded `exp(-i alpha t^3 - beta t^4
   + i delta t^5 - gamma t^6)` to `O(t^8)` by hand and pushed each term through the
   Fourier rule: the `(-i)^n` phases produce exactly
   `P = 1 + a He_3 - b He_4 + d He_5 + (g + a^2/2) He_6 - ab He_7 + (b^2/2 + ad)
   He_8`, real, `s2`-free. The sign conventions match T2's (T.6iii) sign note
   (`log phi = -s2 t^2/2 - i kappa_3 t^3/6 + kappa_4 t^4/24 + i kappa_5 t^5/120
   - kappa_6 t^6/720 + ...`). Untilted limit matches g1_draft_b's `P`. Correct.
3. **The `-36 a^2` split and the weight-4 residual monomials.** Computed `P(0),
   P'(0), P''(0)` at `y = 0` by hand (`He_2(0) = -1, He_4(0) = 3, He_6(0) = -15,
   He_8(0) = 105`) and extracted from `N(0) = -P''(0)P(0) + P'(0)^2 + 12b P(0)^2`
   the coefficients: bare `a^2`: `9 - 45 = -36` ✓; `b`-linear cancels (`+12b - 12b`)
   ✓; `g`: `-90` ✓; `b^2`: `456 - 72 = 384` ✓; `ad`: `840 - 90 = 750` ✓; `a^2 b`:
   `225 - 630 - 180 = -585` ✓; `a^4`: `675/2` ✓. All match the table.
4. **Lemma W.2(a).** Rederived `g''(u) = 4u sum_n (3v_n^2 - u^2)/(u^2+v_n^2)^3`
   from the cotangent partial fractions; the summand-positivity condition is
   `u^2 <= 3 v_1^2 = 12 pi^2` ✓; the bound `12 sum v_n^{-4} = 12 zeta(4)/(2pi)^4 =
   1/120` is exact ✓. Proof correct, scope `|u| <= 2 pi sqrt 3` correct.
5. **Lemma W.2(b).** Rederived `g''' = 12 sum_n (u^4 - 6u^2v_n^2 + v_n^4)/
   (u^2+v_n^2)^4`, `g'''(0) = 1/120` ✓, the `d phi/d s` numerator
   `-2s^2 + 20sv^2 - 10v^4` ✓, and the constant chase `(512 + 320 v^2 + 10 v^4)/
   v^{10} <= 18.44/v^6` for `v^2 >= 4 pi^2`, `s <= 16` ✓; `221.28 zeta(6)/(2pi)^6
   = 221.28/60480 <= 1/273` ✓. Proof correct, scope `|u| <= 4` correct.
6. **Lemma W.3.** Each line checked termwise against the cumulant closed forms
   (2.2)–(2.5) extended to r = 5, 6; sign pattern `kappa_r = (-1)^{r+1}[sum_j j^r
   g^{(r-1)}(lam j) - m g^{(r-1)}(lam)]` rederived from T.2 — the lib's index
   pattern for `k5`, `k6` is correct. `C5 = 2*4! zeta(5)/(2pi)^5`, `C6 = 2*5!
   zeta(6)/(2pi)^6 = 1/252` are the correct T.9''(a) instances. Scaled boxes
   (`amax` … `hmax`) all recomputed ✓; `hmax(30, K=4) = 0.60*785.42^{-1/2}` →
   `0.0461` ✓.
7. **Lemma W.4 chain.** Step 1 ratio identity ✓ (`Z(0)^2/(Z(h)Z(-h)) = e^{h^2}`,
   `h^2 = 1/s2` exact); Step 2 integral-remainder Taylor ✓ (`int_0^1 (1-tau)^3
   = 1/4`, remainder `<= h^4 sup|L''''|/12`, odd orders cancel in the symmetric
   difference even though tilted `L` is not even); `-L''(0) = -12b + N(0)/P(0)^2`
   ✓; the Hermite sups on `|y| <= 1/2` ✓ (each a one-line inequality, checked);
   every one of the `p_1..p_4`, `P_min` coefficient rows recomputed from
   `P^{(r)} = sum c_n (n)_r He_{n-r}` — **all 30 coefficients match**; the
   quotient-rule identity for `L''''` is the standard one, and the pointwise
   triangle-inequality bound from `(p_r, P_min)` is valid. Proof correct.
8. **Lemma W.5.** `e^rho - 1 - rho <= rho^2 e^rho/2`, `rho <= 1.5/s2` from the
   hypothesis, `r(k) >= 1` from Bóna log-concavity (legitimate ambient fact per
   the merged draft §7). `m^2 Lin(1, 180) = 32400*1.125/(0.967*163337.5) = 0.2308`
   recomputed ✓. Correct, honestly conditional.
9. **Prop W.6 bound structure.** `B_lam/B_m = [kappa_4(lam)/kappa_4(0)] *
   (lambda/s2)^2` ✓ (normalizations consistent with `B_m = -kappa_4/(2 sigma^4)`);
   the two-branch upper bound, the `q > 1` lower branch
   `1 + (q-1)(1+devB) = q(1+devB) - devB` ✓ rederived; `R >= 1` uses merged Lemma
   3.2 (`sigma_lam^2 <= lambda`, fully proved) ✓; T.4' is used strictly inside its
   scope (`|w| <= pi`, `m >= 30`) with the W.3 recentred bound taking over on
   `(pi, 4]` — **no silent `w <= pi` assumption anywhere** (the historical G2
   failure mode; explicitly hunted, not found). `|kappa_4(0)| >= m^5/600` rests on
   T2's certified `S*_4 >= m^5/5` (m >= 8) ✓. Note: the script's upper branch 1
   carries a spurious `+(dir_ratio - 1)` addend — it only *weakens* the bound, so
   soundness is unaffected (see F2 for the consequence at small unsampled `w`:
   none, the binding branch is elsewhere).
10. **Theorem W.7 chain.** `s2 log r = s2 log F(0) + Delta_ker` is exact *by
    definition* of `Delta_ker`; combined with W.4 + the `N(0)` split + W.6 it gives
    exactly the displayed decomposition. No hidden LCLT input; the entire far
    region/kernel content sits inside `Delta_ker`, correctly delegated to wp2-a.
    No circularity: nothing from Prop 3.5, from T2's OPEN items (T.8-final's (V),
    the `m_2(K)` thresholds, deep tilt), or from B.8's untilted window law is
    consumed anywhere. (T.7c) is mentioned only as context for what remains.

### 1.2 Re-runs of the draft's scripts

All four (`wp2b_nc1_model_poly.py`, `wp2b_nc2_dictionary.py`, `wp2b_nc3_taylor.py`,
`wp2b_nc4_assembly.py`) were re-run 2026-08-11. **Every quoted number in the
draft's §7 blocks reproduces exactly**, including: the 28-row residual table with
min weight 4; `E(1) = 0.004006927541`; `g''` ratio `0.99999206`; the cumulant-box
ratios `0.9994/0.9851/0.9983/0.5413/0.4761/0.7861/0.9959`; deficit-bound max
`0.3789 at (30, 4.0)`; floors `0.9698/0.8887/0.6629`; the full Taylor table
(`0.02034 … 0.00009`) with `Pmin(4,30) = 0.8710`; truth ratios `0.008–0.60`;
quadrature deviations `1.19e-16 / 3.08e-17`; PW_grid `1.5491/4.0889/4.9126` at the
same argmaxes; PW_closed `10.278/21.063/187.414`; `c_w = 0.4067/0.4658/0.9506`;
`Lin = 0.2308/0.2571/0.3719`; and the entire NC-W4(6) truth table (needed0,
needed_env, ker_truth — all 12 rows identical). The `needed_env` column reproduces
T2's NC-T8 calibration (0.343/0.089/0.022/0.070) as claimed.

### 1.3 Independent verification (referee scripts; the links wp2-b never checks)

**V1 (`ref_v1_cumulants.py`) — the k5/k6 closed forms.** NC-W2(d) only compares
the closed forms against bounds *derived for those same closed forms*; NC-T1 (T2)
verified r <= 4 only. I verified `lib.cumulants` (all six outputs) against direct
50-digit weight-moment→cumulant computation at `m in {8, 30}`,
`lam in {0.01, 0.1, 0.5}`:

```
mu: 5.63e-15  s2: 1.35e-12  k3: 4.81e-09  k4: 9.10e-09  k5: 1.45e-07  k6: 7.27e-07
```

The k5/k6 deviations are fully explained by double-precision cancellation in the
`-120/u^6 + Eulerian` closed forms plus the fallback bug of F1 below — the
**formulas are correct** (the Eulerian polynomials `1,11,11,1` / `1,26,66,26,1` are
the right ones; checked against mpmath numeric derivatives of `g`, rel. dev
`<= 9.1e-06`, dominated by the F1 bug).

**V2 (`ref_v2_bounds.py`).**
- W.1(i)'s constant `0.0330` is a genuine all-m theorem: `coef(m) <= 33/1000`
  reduces (my reduction, cross-checked in exact Fractions at 4 values of m) to
  `6m^4 - 51m^3 - 265m^2 + 10 >= 0`, verified exactly for **every** integer
  `m in [30, 5000]`, with the termwise tail `6m^4 >= 180m^3 > 51m^3 + 129m^3`,
  `129m^3 > 265m^2` for `m >= 30`. **W.1(i) is now fully closed, better than the
  draft's own 30..300-step-10 certificate.**
- NC-W2(f) tails: `(S_4+m)/m^5` and `(S_6+m)/m^7` decreasing (exact Fractions,
  sampled) and the inequalities hold at m = 199 — so the exhaustive 30..199 check
  extends to all m >= 30 by monotonicity. Closes the m in (200, 499) etc. holes.
- Independent `c_w` re-implementation (without the spurious `dir_ratio - 1` term),
  4000-point w-grid, every integer m in [180, 260], then to 10^4:
  `K=1: 0.4067 at m=180; K=2: 0.4658 at m=180; K=4: 0.9509 at m=180`.
  Confirms K=1, 2 exactly and worst-at-180; at K=4 the finer grid finds **0.9509 >
  the draft's 0.9506** — see F2.
- `|g''(u)| <= |u|/120` holds to u = 10 (ratio 0.999997), consistent with the
  proved scope `2 pi sqrt 3`.
- `lib.mahonian` rows == the official harness `mahonian.py` rows (m = 12, 20).

**V3 (`ref_v3_taylor_truth.py`).**
- The Taylor bucket table re-typed independently from the draft's §2–§3 displays
  (not from the script): all 9 spot values match to all printed digits.
- The NC-W4(6) truth line at (m, K) = (30, 1) reproduced end-to-end with my own
  bisection lam-solver and the **official** harness rows:
  `needed0 = 0.349, ker_truth = 1.374` — identical.
- PW_closed keeps decreasing at m = 3000/5000/20000 (10.268 / …).
- Second quadrature check of the model pipeline at (m, w) = (60, 2): `phat` vs
  `Z*P` rel. dev `1.57e-16`; ratio identity `1.98e-16`. The Fourier/polynomial
  pipeline is right at a second point, not just the draft's (30, 1).

**V4 (`ref_v4_resid_limit.py`).**
- Independent sympy regeneration of the `N(0)` residual table from the *closed
  form* of P (a different construction path from NC-W1's Fourier route): **all 28
  monomials and coefficients identical.**
- Large-m limits of the c_w pieces (K = 1/2/4, m up to 10^6): the bare part tends
  to 0.1327/0.1835/0.5556 — *below* its m = 180 value — and `dir_ratio - 1 -> 0`,
  so "worst at m = 180" survives the m -> infinity limit.

---

## 2. Honesty audit

- Every script named in the draft exists on disk with plausible timestamps, runs,
  and reproduces its quoted output verbatim. No fabricated PASSes found.
- Statuses are per-result and mostly accurate; grid-certificate items are flagged
  as such *except* Prop W.6's headline (F2).
- The pending kernel bucket is not smuggled in anywhere: `Delta_ker` is defined
  exactly, its truth is measured and *reported as large* (comparable to the whole
  PW bucket), and §8 explicitly concedes the assembled route is >= 9x above the
  measured need. T.9 is correctly declared still PARTIAL.
- The `c_w(4)` FALSE-as-proved finding against T2's own `c_w = 1/2` claim is a
  genuine, verified statement-level correction (kappa_4 sign flip confirmed:
  `kappa_4(lam)/kappa_4(0) = -0.1417` at m=60, w=4, reproduced), with the honest
  observation that the true envelope (~0.01 B_m w^2) is a cancellation the
  triangle-inequality route cannot see.
- Prior lemmas are quoted with true hypotheses and scope: T.4' only on
  `|w| <= pi, m >= 30`; T.9''(a) global-in-lam; merged Lemma 3.2 for `R >= 1`;
  Bóna for `r >= 1`; the item-4 notes' numbers quoted correctly. One nuance worth
  a sentence in revision: T2's *packaged* (T.4a'') display is scoped `|u| <= pi`,
  while W.1 uses `E <= 1/240` and E-decreasing out to `u = 4`; the cited
  partial-fraction summand argument in T2 is in fact u-global (I re-checked the
  summand derivative computation — nothing in it uses `u <= pi`), and NC-W2(a)
  grid-certifies on (0, 4], so the use is legitimate — but the draft should say
  explicitly that it is citing the global mechanism, not the packaged statement.

---

## 3. Findings (ranked)

**F1 (real bug, benign — must fix).** `wp2b_lib.g4`'s small-u series fallback has
last coefficient `-u^5/22176`; the true Taylor coefficient of `g''''` is
`-u^5/15840` (from g's `-u^9/47900160` term: `-3024/47900160 = -1/15840`).
Likewise `g5`'s fallback has `-u^4/4435.2`; truth is `-u^4/3168`
(`-15120/47900160`). Both off by the same factor 5/7 (verified in V1c; e.g.
`|lib.g4(0.099) - true| = 1.71e-10` against `|g4| ~ 3.9e-4`). Impact: relative
errors up to ~9e-6 in g5 near the fallback boundary, ~7e-7 in k6 — at least an
order of magnitude below every quoted margin (nearest: kappa_6 box ratio 0.9959;
all PW/truth values stable at the printed 4 digits). **No verdict flips.** Repair:
fix the two coefficients, re-run NC-W2/NC-W3/NC-W4 (minutes).

**F2 (status inflation — the main repair).** Prop W.6 is headlined "PROVED for
K = 1, 2" (§0 item 4, §5). What actually exists is: explicit valid formulas,
maximized on a 400-point w-grid at **four** m-values {180, 500, 2000, 10^4}. That
is grid-certificate status (like W.1(ii)), not "PROVED". Consequences, verified:

- At K = 1, 2 the binding branch is piecewise-constant/endpoint-attained in w
  (`600/2200 = 0.2727` exactly at K=1; the `q > 1` branch at the endpoint w = 2
  gives 0.2802 at K=2), and my fine m-scan + m -> infinity limits confirm
  worst-at-180 — so **the conclusions 0.4067 / 0.4658 <= 1/2 are correct** and can
  be upgraded to proofs with one page of per-piece monotonicity (all pieces are
  monotone; I checked each).
- At K = 4 the reported `c_w(4) = 0.9506` is **not a safe upper bound**: my
  4000-point grid finds >= 0.9509 (the max sits between the draft's grid points).
  The draft's own recommendation "use 1" is safe and should become the stated
  constant.

Repair: relabel W.6 as grid-certified (Sturm-able / monotonicity-provable), state
`c_w(4) = 1`, and add the one-line note that the script's upper branch 1 carries a
harmless spurious `+(dir_ratio - 1)` addend.

**F3 (grid holes, minor).** W.1(ii)'s certificate samples 12 m-values in
[30, 3000] (holes at 31–39, 41–49, …) and an 80-point w-grid; the draft calls this
"same status class as (T.7b-cert)", but (T.7b-cert) was exhaustive in its discrete
parameter up to the monotone regime. With max 0.3789 vs threshold 0.40 and the
weak, decreasing m-dependence this is safe, but the label overstates. Repair: run
every integer m in [30, 300] (seconds) + the monotone-tail note; or Sturm.

**F4 (certificate tails — now closed by this report).** W.1(i)'s "decreasing on
30..300 step 10" and NC-W2(f)'s sampled ranges left tail gaps. V2 closes both:
`6m^4 - 51m^3 - 265m^2 + 10 >= 0` exhaustively on [30, 5000] + termwise tail
(making W.1(i) genuinely PROVED for all m >= 30), and the `(S_r+m)/m^{r+1}`
monotone-decrease + m = 199 endpoint closes (f) for all m >= 30. Repair: cite or
inline these two one-line arguments.

**F5 (caveat to propagate).** "T.9's c_w = 1/2 is PROVED for K = 1, 2" concerns
parts (I) + (II) of the envelope only. The final T.9 statement's envelope can be
fixed only after wp2-a's `Delta_ker` bound lands — if that bound carries its own
`w^2`-dependence at order `w^2/m`, the merged c_w may exceed 1/2 even at K = 1.
The W.7 decomposition makes this structurally clear; add one sentence so a merge
editor cannot mistake the audit for the final envelope.

**F6 (trivia).**
- §1 says "(13 monomials of weight 8 and 10"; the table has 9 + 6 = **15**.
- §0 quotes `PW_closed(4) = 187.5` vs computed 187.414 (rounded up — safe) and
  `21.07` vs 21.063.
- The scripts header lists numpy 1.26.4; no wp2-b script imports numpy.
- Theorem W.7 asserts `v := F(0) - 1 > 0` without proof; only `F(0) > 0` (which
  follows from `P > 0` on J) is actually needed. Either prove it (easy at the
  table's parameters: `log F = h^2(1 - L''(0)) - rem > 0` since `|L''(0)| +
  sup|L''''|/(12 s2) < 1` there) or drop the claim.
- Lin's "decreasing in m" is asserted; it is trivially `~ 1/(c_K m)` but no check
  is run. One line.

**Positive findings (attacks that failed).** (i) No circularity: Prop 3.5 is
nowhere assumed; T2's Section-8 OPEN items are never cited as inputs; B.8's window
law is not used (the draft correctly rebuilds the B.7-machinery in the tilted
frame instead — the very trap T2's Step 1 documented). (ii) No hidden
`w <= pi` assumption — every box used on `w <= 4` has a proof valid there (W.2(a)
to `2 pi sqrt 3`, W.2(b) to 4, T.9''a global); W.6 switches from T.4' to the W.3
bound exactly at pi. (iii) The k5/k6 closed forms, the model polynomial, the
`-36a^2` split, the residual table, the Taylor table, and the harness-truth
numbers all survive independent recomputation. (iv) The `(K, m)` coverage the
draft claims is the coverage it has; the K in {1, 2, 4} restriction (vs T.9's "fix
K >= 1") is adequate for the downstream Theorem-A handoff, which needs `w_0 <= 1`.

---

## 4. Required repairs (all small)

1. Fix `wp2b_lib.g4`/`g5` fallback coefficients (`-1/15840`, `-1/3168`); re-run
   NC-W2/3/4 and refresh any digits that move (none should at 4 digits). [F1]
2. Relabel Prop W.6 from "PROVED" to grid-certified; state `c_w(4) = 1`; note the
   spurious `+(dir_ratio - 1)` addend; optionally add the per-piece monotonicity
   page to upgrade K = 1, 2 to fully proved. [F2]
3. Exhaustive integer-m sweep for W.1(ii) on [30, 300] + monotone-tail remark;
   adjust the status-class sentence. [F3]
4. Inline the two one-line tail arguments for W.1(i) and NC-W2(f) (or cite this
   report's V2). [F4]
5. Add the F5 sentence (final envelope awaits `Delta_ker`). [F5]
6. Fix the F6 trivia (15 monomials; 187.414; numpy; `v > 0`; Lin monotonicity).

None of these threatens the deliverable: the Taylor and linearization buckets are
correct with the stated constants; the assembly identity is exact; item 4 of T2 §8
remains, exactly as the draft says, waiting only on wp2-a's kernel bucket — and
the draft's measurement that this pending bucket is *large* (~1.4/4.1/5.0 in C_R
units) is verified and is important, honest information for the merge editor.

**Final verdict: MINOR_REPAIRS.**

*End of referee report.*
