# Adversarial numerics referee report — wp1_draft_c (Lemma W far-region bound)

*Referee run 2026-08-11. Target: `g2_campaign_undefined/wp1_draft_c.md` and its five
scripts in `g2_scripts/campaign_undefined/wp1_c/`. Protocol: default-to-refutation;
every script re-run (CPython 3.12.2, mpmath 1.3.0); every quoted number verified
against real output; float-dependent and rational-arithmetic steps re-implemented
independently (exact `Fraction` arithmetic where feasible, dps-60 mpmath elsewhere,
quadrature instead of the draft's closed form, direct weight sums instead of the
draft's factorization); off-grid adversarial sweep of the master inequality.
Blind protocol maintained: nothing else under `g2_campaign_undefined/` or
`g2_scripts/campaign_undefined/` was read, nor `g2_draft_t1_*`. The T2 script
`g2_scripts/t2/t2_nc10_far.py` (not blinded) was read to check the draft's
"criterion replicated verbatim" claim. Referee script:
`ref_wp1c_indep.py` (session scratchpad; key outputs quoted below).*

## VERDICT: **MINOR_REPAIRS**

The draft survives every attack I could mount. All five scripts exist, run, PASS,
and reproduce **every** number quoted in the draft, to the digit. The five
load-bearing analytic claims (W.1, W.2, W.3 incl. closed form / monotonicity /
(W.3d), W.4's constant chain, W.5, W.6) were verified line by line by hand and
re-verified numerically by independent implementations; no error was found. No
fabricated number exists anywhere in the draft. The repairs listed at the end are
prose-level: two factually incorrect peripheral numeric statements, one
grid-backed monotonicity assertion contradicting the draft's "no grid
certificates anywhere" boast, and one over-broad supersession claim. None touches
any named constant, any stated lemma, or any threshold.

---

## 1. Script re-runs: all PASS, all quoted numbers reproduced exactly

| script | re-run result | draft's quotes checked | match |
|---|---|---|---|
| `wp1c_nc1_identity.py` | PASS, exit 0 | max rel dev 5.94e-40 at (13, 0.01, 2.899...); product dev 5.84e-32 (m=12, exact `a_k`); envelope min margin +8.36e-8 over 2780 cases; induction grids PASS | **exact** |
| `wp1c_nc2_master.py` | PASS, exit 0 | quad dev 3.76e-14; all 36 (m, lam) rows <= 1; GLOBAL max ratio 0.988902 at (100, 2.5, 3.14159); monotone grids PASS | **exact** |
| `wp1c_nc3_constants.py` | PASS, exit 0 | all chain certificates True; `c_1(1) = 0.225989909281`, `c_1(4) = 0.101983937137`, `c_V = 0.0372513232987`, `|q(2,0) - (log2 - 1/2)| = 0.0`; improvement factors x28/x164/x915/x5067/x554; deep-tilt table (`lam = 0.3`: 0.296614 / 0.329431 = draft's "0.2966 / 0.3294") | **exact** |
| `wp1c_nc4_thresholds.py` | PASS, exit 0 | m_2 = 143/190/267/379 (new), 7338/66010/593181/5076022 (old, coarse T10d loop); (V): 1065849 / 292672 (old), 879 / 185 (new); g1 arc: 180 (old) / 60 (new) | **exact** |
| `wp1c_nc5_sharpness.py` | PASS, exit 0 | full §8 slack table (e.g. m=100 K=1: e^-29.793 / e^-22.590); untilted m=40 measured 1.141e-16 vs ledger NC-5's 1.1e-16; deep-tilt slacks e^7.0/e^2.6/e^1.6/e^0.8 at m=300; W.6 min ratio 1.0182 at (300, 0.5, 0.5095) | **exact** |

The §7 "verbatim excerpts" block matches the real outputs verbatim. The §8
percentage claims recompute correctly from the table (K=1: 6.777/9.238 = 73.4%,
22.590/29.793 = 75.8% → "73–76%"; K=4: 55.7–56.8% → "55–57%").

**Criterion-fidelity check.** `t2_nc10_far.py` part (d) uses exactly
`16 sqrt(2pi) (1.05 m^3/36)^{3/2} e^{-cm} <= 0.2/m^2` with a coarse loop
(start m=100, step ×1.05). NC-W4 replicates this verbatim for the "old" column
(reproducing T2's 7338 = "~7.3e3", 5076022 = "~5.1e6" exactly) and uses a
unit-step scan of the same criterion for the "new" column — labeled honestly.
The scripts test what the prose claims; no strawman found.

## 2. Independent re-verification (referee's own implementations)

1. **Named constants by quadrature, dps=60** — `q(M,r)` recomputed by
   `mpmath.quad` of `f(u) = log[(1+r)u^2/(ru^2+1)]` over `[1, M]`, bypassing the
   draft's closed form entirely. All 13 named constants agree with the closed
   form to `< 4e-61`, and every quoted constant is rounded DOWN (safe direction
   for a decay exponent). Minimum rounding margin: 9.116e-6 (at `c_1(0)`) — see
   repair R2. `q(pi/2, 1) = 0.0373606933...` and `q(2,0) - (log 2 - 1/2) = 0`
   to 60 digits, confirming the Lemma 1.4 corner identity.
2. **Exact rational arithmetic (stdlib `Fraction`)** for every purely arithmetic
   chain step: `cosh^2(1/8) <= 1.0157066` (via Taylor series with explicit tail
   bound: exact upper bound 1.015706549940 <= 1.0157066 ✓);
   `1.0157066/4 <= 0.253927` ✓; `0.253927/4.9257 <= 0.05156` ✓;
   `0.253927/9.8332 <= 0.02583` ✓; `2.2194^2 >= 4.9257`, `3.1358^2 >= 9.8332` ✓.
3. **Worst-corner cross-check, independent of the W.1 factorization** — at the
   reported global maximum (m=100, lam=2.5, t=pi), `-log|phi|` recomputed at
   dps=50 by direct per-factor weight sums (not the sinh/sin identity):
   `-log|phi| = 16.2883679127`, `m q = 16.1076001376`, ratio `0.98890203 < 1`.
   The draft's 0.988902 is genuine, not a float artifact, and the inequality
   holds with ~1.1% true margin at its tightest tested point.
4. **Off-grid adversarial sweep** (dps=30): 2690 cases at
   `m ∈ {31, 47, 150, 400, 1000}`, `lam` off the draft's grid including
   `1e-5, 0.003, 4.7/m, 0.25, 0.777, 1.2, 1.7627, 2.0, 3.5, 6.0` and **negative**
   tilts (`-0.3, -1.0, -5/m`), with `t` at random points, at `t = pi` and near-pi,
   at Dirichlet resonances `2pi k/j ± 1e-5` (j <= 7), and just above the `M = 1`
   validity boundary (`M = 1 + eps`, eps down to 1e-3). Max ratio
   `m q/(-log|phi|) = 0.9989967` (at m=1000, lam=6.0, t=pi) — the bound holds
   everywhere, approaching 1 exactly where the §2 remark predicts (deep-factor
   tightness), never exceeding it.
5. **Thresholds recomputed with independent loop code**: 143/190/267/379,
   7338/66010/5076022, 1065849/879/185, 180/60 — all reproduced.
6. **Tightest chain certificate** re-verified at dps=60:
   `r_V = [sinh(pi/60)/sin(pi/60)]^2 = 1.0018293758... <= 1.00183`
   (margin 6.24e-7 — small but real and in the safe direction).

## 3. Hand-verification of the analytic content (what an adversary checked)

- **W.1**: `|1-e^{-(a+ib)}|^2 = 4e^{-a}[sinh^2(a/2) + sin^2(b/2)]` and the exact
  cancellation of all exponential prefactors — algebra checked by hand; identity
  confirmed at dps=40 against direct weight sums and, at m=12, against exact
  integer Mahonian rows.
- **W.2**: both induction inequalities (`|sin jv| <= j|sin v|`,
  `sinh(ju) >= j sinh u`) checked; the min/1-form of the envelope is correct.
- **W.3**: the reduction to `f(jh)`, the tiling `[h, mh]` (with `f = 0` on
  `[h, 1]`), the monotone-minorant integral step, the closed form of `I(M,r)`
  (antiderivative differentiated back by hand; `r -> 0` limit `2(M-1)` of the
  arctan term checked), the `M`-monotonicity (`I <= M f(M)`), the
  `r`-monotonicity (`∂f/∂r = (1-u^2)/[(1+r)(ru^2+1)] <= 0`), and — notably —
  **(W.3d) is exact, not lossy**: the integral deficit `(1/(2M))(1/r)(1 - 1/M)`
  equals the displayed `((M-1)/(2M))·(1/(rM))` identically. All correct.
- **W.4**: the five-step chain (a)–(e) is sound; worst-`t` at the left endpoint
  is correct for both `M` and `r`; the `K <= m/4` hypothesis is exactly what
  step (c) needs (`lam/2 <= 1/8`).
- **W.5**: (i)/(ii)/(iii) verified including `t_0 >= lam >= pi/m` (so the max is
  `t_0`), the `M_1 >= pi/2` floor via `sinh x >= x`, the case-1 corner
  `(M, r) = (1.5700, 1.00183)`, and the cross-case floor consistency
  `q(1.5700, 1.00183) = 0.037251 <= q(pi/2, 1) = 0.037361`.
- **W.6**: is (W.3d) with `1/r = s/S`; the geometric-cf interpretation
  (`|cf|^2 = S/(S+s)`, `Var = 1/(4S)`) checked by hand.
- **Consistency of the supersession targets**: T.7c's `0.06 e^{-2K}` and
  T.7b-final's `exp(-m_*/4730)`, `m_* >= m/pi - 1` are quoted correctly from the
  T2 draft; Lemma 1.4's `2e^{-0.19314 m}` correctly from the merged draft; the
  envelope-vs-Lemma-1.4 comparison (`sin(t/2) >= t/pi` on `[0, pi]`) is correct.

## 4. Findings (all minor; repair list)

**R1 (incorrect prose number, no script behind it).** §5 "Beyond |lam| = 1.7627":
`2 asinh(sqrt 10) = 3.7358` is **wrong** — the true value is `3.7371022...`
(referee, dps=60). Illustrative aside only; no downstream use. Under the house
honesty rule (every numeric claim from a script) this is exactly the class of
number that must not be hand-waved. Fix the digit string (or delete the aside).

**R2 (overstated margin claim).** §9 item 3 claims the named constants were
"rounded in the safe direction with margin >= 5e-5". False for six of the
thirteen: measured margins `c_1(0)` 9.1e-6, `c_1(6)` 1.25e-5, `c_1'(2)` 1.48e-5,
`c_1'(4)` 1.85e-5, `c_1(3)` 2.35e-5, `c_1(pi)` 4.44e-5. Every rounding IS in the
safe direction, and every margin is still ~40 orders above the dps-50 evaluation
error, so no constant is affected — but the stated "5e-5" is not true of the
draft's own numbers. Restate as "margin >= 9e-6" or give the per-constant list.

**R3 (a load-bearing monotonicity is grid-backed, contradicting the "no grid
certificates anywhere" claim).** W.5(iii)'s case 1 uses "`sinh(x)/sin(x)` is
increasing on `(0, pi/2)`" (it sets the worst case m = 30 for `r_V`, hence
`c_V`), certified in the draft only by NC-W3's 1500-point grid. The draft's §0
and §9 assert "no grid-certified inequality appears anywhere". The fact has a
two-line analytic proof — `(cosh x sin x - sinh x cos x)' = 2 sinh x sin x > 0`
on `(0, pi)`, so the numerator of `(sinh/sin)'` is positive — which the draft
should simply include (referee verified it). With that line added, the "no grid"
claim becomes true; as written it is not.

**R4 (over-broad supersession claim).** §0/§4 "Supersedes Lemma T.7c
everywhere": W.4 carries the hypotheses `m >= 30` **and** `K <= m/4`, whereas
T.7c is stated for any fixed `K` at `m >= 64` — so for `K > m/4` (i.e.
`lam > 1/4`, where T.7c's bound is astronomically weak but formally nonvacuous)
W.4 does not apply and the supersession is by W.5/W.6 on *different* `t`-ranges.
Practically irrelevant; scope the sentence.

**Nits (no repair demanded).** (i) "The exact harness certifies the refined law
itself for m <= 150 (NC-1, NC-T8)" is inherited from T2; NC-T8 measured the
needed `C_R` only at m ∈ {30, 60, 100, 140}, so "no uncovered m at all for
K = 1" leans on a spot-checked, not exhaustively certified, m <= 150 claim —
the draft's own §9 item 1 already names the bucket assembly as the real
remaining obstruction, which is the honest bottom line. (ii) K=6 improvement
"~163000x" computes to ~162,200x (within its "~"). (iii) The (V)-convention
discrepancy (T2's "~2.5e5" vs the recomputed 292672 at `s2 = C_0`) is
documented transparently in §9 item 6 — no action needed.

## 5. What I failed to break

- The master inequality `-log|phi_lam(t)| >= m q(M, r)`: 2690 off-grid
  adversarial cases (deep tilt to lam = 6, m to 1000, negative lam, resonances,
  `M -> 1+` boundary, t = pi) — zero violations; max ratio 0.99900.
- Every named constant, by independent quadrature at dps=60 and exact rational
  arithmetic for the rational steps.
- Every threshold and every comparison factor, by independent loop code.
- The claimed exactness `q(2, 0) = log 2 - 1/2` (60 digits).
- The sharpness measurements, including the ledger cross-check (m=40 untilted
  max 1.141e-16 vs NC-5's 1.1e-16).

The draft's honest-markers section (§9) is accurate: it claims only the
far-region half of T2 §8 items 1 and 5, and correctly leaves the bucket table
(item 4) and the deep-tilt core model open. Statuses PROVED/reported-fact are
used correctly throughout. Modulo the four listed repairs — all prose-level,
none touching a constant or a lemma — this work package delivers what it says.

*End of referee report.*
