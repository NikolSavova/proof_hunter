# Adversarial numerics referee report — wp2_draft_b (T.9 Taylor bucket, w^2-envelope audit, C_R assembly)

*Referee pass 2026-08-11. Target: `g2_campaign_undefined/wp2_draft_b.md` and its
scripts `g2_scripts/campaign_undefined/wp2_b/{wp2b_lib.py, wp2b_nc1_model_poly.py,
wp2b_nc2_dictionary.py, wp2b_nc3_taylor.py, wp2b_nc4_assembly.py,
wp2b_n0_resid_table.py}`. Mandate: default to refutation; re-run every script;
verify every quoted number; re-implement float-dependent checks in exact/
high-precision arithmetic; hunt fabricated numbers; spot-check every grid claim
off-grid. Blind protocol respected: no other campaign draft read; judged on its
own inputs (merged draft, g1_draft_b, g2_draft_t2, the two item-notes files).
Environment used: CPython 3.12.2, sympy 1.14.0, mpmath 1.3.0 (matches the
draft's banner; note numpy 1.26.4 is listed there but no wp2_b script imports
it). To respect the no-overwrite rule (nc1 regenerates
`wp2b_n0_resid_table.py`), all runs were made on a byte-copy of the script
directory in the session scratchpad
(`/private/tmp/claude-501/-Users-sihaohuang-Desktop/0c711691-81ac-42b2-8712-819b1ee08f6b/scratchpad/`,
subdir `wp2b_ref/`); referee scripts `ref1_indep_poly.py`,
`ref2_taylor_indep.py`, `ref3_offgrid.py`, `ref4c_exact_truth.py`,
`ref5_misc.py` and their outputs `out_*.txt` live there (session-local; every
number I cite below is quoted verbatim from those outputs, and the
load-bearing outputs are reproduced in this report).*

## VERDICT: MINOR_REPAIRS

I tried to kill this draft and failed. All four scripts exist, run, and PASS;
**every number-bearing line quoted in the draft's §7 matches the real re-run
output (programmatic audit: 0 mismatches)**; the symbolic core survives a fully
independent re-derivation; the headline tables survive independent
re-implementation from the displayed formulas alone; the exact-harness truth
table survives an exact-Fraction/30-digit re-run; and **no fabricated number was
found anywhere** — every prose-only number I hunted down (0.367, −0.32, 0.083,
"w ~ 3.3", every ratio in §8) is real and reproducible. The repairs below are
genuinely minor: one beyond-grid exceedance of a grid-certified constant
(+0.22% at K = 4, in a column the draft itself scopes as "m <= 2000"), one
grid-max footnote, two harmless series-coefficient typos in the shared library,
and one diagnosis in §5 that my measurements show is more pessimistic than the
truth.

---

## 1. Script re-runs: all reproduce exactly

| script | draft claim | re-run result |
|---|---|---|
| `wp2b_nc1_model_poly.py` | PASS; Im P = 0; bare coeff −36; min weight 4; dev 1.07e-14; ratio 0.810 | **PASS, all quoted values identical** |
| `wp2b_nc2_dictionary.py` | PASS; E(1)=0.004006927541, E(2)=0.003587187144, E(3)=0.003040358636; ratios 0.99999206/0.54166193; box ratios 0.9994/0.9851/0.9983/0.5413/0.4761/0.7861/0.9959; deficit max 0.3789 at (30,4.0); floors 0.9698/0.8887/0.6629 | **PASS, all quoted values identical** |
| `wp2b_nc3_taylor.py` | PASS; full T(K,m) table; Pmin(4,30)=0.8710; truth ratios 0.008–0.60; quad dev 1.19e-16/3.08e-17 | **PASS, all quoted values identical** (worst truth ratio 6.0e-01 is indeed at m=120, K=1, w=1.0) |
| `wp2b_nc4_assembly.py` | PASS; PW 1.5491/4.0889/4.9126; PW_closed 10.278/21.063/187.414 (10^4: 10.268/20.942/178.694); c_w 0.4067/0.4658/0.9506 (worst m=180); Lin 0.2308/0.2571/0.3719; full table (6) | **PASS, all quoted values identical, including all 12 rows of table (6)** |

The generated `wp2b_n0_resid_table.py` regenerates **byte-identically** (diff
clean against the committed file). Programmatic §7 quote audit
(`ref5_misc.py (h)`): every number-bearing line in all four quoted blocks found
in the real outputs; the "trimmed" elisions hide nothing that disagrees.

## 2. Independent verification of the mathematical core

**Lemma W.0 (model polynomial), independently re-derived** (`ref1_indep_poly.py`,
my own sympy route — I additionally verified the Fourier rule
`(1/2pi)∫ t^n e^{−s2 t²/2} e^{−itx} dt = (−i)^n s2^{−n/2} Z(y) He_n(y)` itself by
direct symbolic integration for n = 0..8, which the draft's script assumes):

```
(0) Fourier rule ... n=0..8: True
(1) Im P == 0: True ; s2-free: True
(1) P == draft closed form: True
(2) bare a^2 coefficient: -36 (must be -36)
(2) residual monomial dict == committed table (28 rows): True (28 mine vs 28 theirs)
(2) min weight: 4 (need >= 4)
(3) L'''' quotient identity: True
```

All 28 committed residual monomials (exponents AND coefficients, including the
half-integer 675/2 and 12105/2) match my independent derivation exactly.

**Lemma W.4 (Taylor bucket), independently re-implemented** from the draft's
displayed formulas only (`ref2_taylor_indep.py`, exact Fractions to the final
sqrt): all 18 table entries agree to the printed 5 decimals; Pmin(4,30) =
0.8710; hmax = 0.04607 ≤ 0.0461; Lin(K,180) = 0.2308/0.2571/0.3719; and the
pretty identity C6 = 240ζ(6)/(2π)⁶ = **1/252 exactly** (so the certified decimal
3.96835e-3 is sound), C5 = 0.0050826522… ≤ 5.08266e-3. I also re-checked by
hand every displayed derivation the scripts lean on: W.2(a)'s
12ζ(4)/(2π)⁴ = 1/120 (exact), W.2(b)'s 273·221.3 = 60414.9 ≤ 60480 (so u²/273
is legitimate), the eight Hermite falling-factorial rows of p₁..p₄ and the
P_min row (all coefficients re-derived: 3/12/15/90/105/840 etc. — correct), the
1/12 integral-remainder factor, and the eight |y| ≤ 1/2 Hermite sup
inequalities (all hold; see repair 5a). The scripts test the actual claims,
not strawmen.

**PW_closed independently recomputed** (`ref5_misc.py (f)`) from my own boxes +
the independently-verified monomial table: 10.278/21.063/187.414 at m=180 and
10.268/20.942/178.694 at m=10⁴ — identical; monotone decrease re-verified at
step 7 (off their step-60 grid).

**Certificates upgraded from sampled to exhaustive** (`ref2`, `ref5 (g)`): the
draft's exact certificates `(S_4+m)·545 ≤ 120 m⁵` and `(S_6+m)·1500 ≤ 273 m⁷`
were script-checked only on m = 30..199 ∪ {500, 1000, 2000} (a gap at
200..499). I verified them in exact Fractions for **every** m in 30..3000, with
the differences increasing at the top (safe beyond). Likewise
coef(m) = S_4/(240m²λ) ≤ 0.0330 and strictly decreasing for **every** m in
30..3000 (0.031088 → 0.030010), and the Taylor bucket nonincreasing at **every
integer** m in 30..3000 (the draft's script stepped by 10). All hold.

**Exact-harness truth table (6), re-run in exact/high-precision arithmetic**
(`ref4c_exact_truth.py`: u = r(k)−1 as an exact Fraction of the integer
Mahonian rows; lam(k) by Newton on 30-digit mpmath cumulants, residual
|mu−k| ≤ 5e-27; hybrid series/closed-form g-derivatives immune to the
small-u cancellation that invalidates naive high-precision closed forms):

```
m=60:  rows used = 361;  min v = 0.00016
  K=1: needed0=0.543 (0.543)  needed_env=0.089 (0.089)  ker_truth=1.386 (1.386)  OK
  K=2: needed0=2.146 (2.146)  needed_env=0.089 (0.089)  ker_truth=4.070 (4.070)  OK
  K=4: needed0=5.233 (5.233)  needed_env=0.089 (0.089)  ker_truth=5.022 (5.022)  OK
m=140: rows used = 1939; min v = 1.29e-5
  K=1: needed0=1.523 (1.523)  needed_env=0.070 (0.070)  ker_truth=1.386 (1.386)  OK
  K=2: needed0=5.175 (5.175)  needed_env=0.070 (0.070)  ker_truth=4.059 (4.059)  OK
  K=4: needed0=12.280 (12.280) needed_env=0.070 (0.070) ker_truth=5.038 (5.038)  OK
```

All 12 verified cells reproduce the draft to the printed 3 decimals. This also
confirms Theorem W.7's assertion v = F(0) − 1 > 0 on the measured range (min
1.29e-5, at the m=140 center). The float lib itself was validated against the
30-digit ground truth: max relative deviation of (s2, k3..k6) over
m ∈ {30,60,120,300}, w ≤ 4 (down to w = 0.001) is **2.66e-6** — comfortably
below every quoted margin.

## 3. Off-grid adversarial spot checks (`ref3_offgrid.py`, `ref5_misc.py`)

1. **PW_grid, K = 1 and K = 2: the certified maxima are genuine.** Off-grid
   scan over 40 unsampled m (31..20000, incl. primes) × 160 w-points: maxima
   1.5481 (m=31) and 4.0863 (m=31) — strictly below the certified 1.5491 /
   4.0889 attained at the sampled m=30. Holds up.
2. **PW_grid, K = 4: beyond-grid exceedance (repair 1).** The certified max
   4.9126 sits at the *edge* of the sampled range (m=2000, w=2.8), and the
   bucket is still increasing in m there: measured 4.9141 (m=5000, w=2.8),
   4.9150 (m=10⁵, w=2.8), and **4.9233 at (m, w) = (20000, 2.725)** — 0.22%
   above the certified value, at an off-grid w as well. The draft's scoping
   ("grid cert., m <= 2000", §6 remark 1, §9 item 3) is honest, so no false
   statement exists — but the K=4 grid number is demonstrably NOT an all-m
   constant, and the assembled `C_R^PT grid` K=4 entry 5.2985 should read
   ≈ 5.31 for the all-m version.
3. **W.1(ii) band bound: conclusion holds everywhere; the max location
   footnote (repair 2).** Scanning **every** integer m in 30..400 (plus large
   m) × 200 w-points: global max **0.379644 at (32, 4.0)** — slightly above the
   draft's grid max 0.3789 at (30, 4.0), because the bound bumps at
   m ≡ 0 (mod 4) (floor effects in the band cuts); still ≤ 0.40 with margin
   0.0204, so `c_4 = 0.60` stands. On the draft's own sampled m-grid its
   statement is literally true. The prose-only "continuum limit 0.367"
   verified: 0.3667.
4. **c_w(K, m): the 4-point max is the real max.** Dense m-scan (step 20 to
   600, then 700..10⁴): max at m = 180 for every K, values identical to the
   draft's (0.4067 / 0.4658 / 0.9506). The "for m ≥ 180" claim survives.
5. **kappa_4 sign change: "near w ~ 3.3" is accurate.** Solved: w₀ = 3.3132
   (m=30), 3.3397 (60), 3.3533 (120), 3.3616 (300).

## 4. Prose-number audit — no fabrications

Every number appearing in prose but in no script output was re-derived and
verified: continuum limit 0.367 (→ 0.3667, `ref5 (e)`); B_lam/B_m ≈ −0.32 at
(60, 4) (→ −0.3182, `ref5 (c)`); the part-(I) envelope floor ~0.083
(→ 0.0824); "kappa_4 crosses zero near w ~ 3.3" (→ 3.31–3.36); §8's slack
ratios 5.1x / 25x / 30x / 150x / "~3.2 / ~8.4 / ~10.3" / "≥ 9x" (all recomputed
from the table values: 1.7803/0.35 = 5.09, 1.7803/0.070 = 25.4, 10.509/0.35 =
30.0, 10.509/0.070 = 150.1, 1.7803+1.39 = 3.17, 4.347+4.07 = 8.42, 5.2985+5.04
= 10.34, 3.17/0.35 = 9.06); §6 remark 2's "C_ker ≤ 10⁴-scale" (the actual
ceiling at m=180, K=1 is ≈ 1.6e4). Also confirmed: "needed_env reproduces
NC-T8's 0.343/0.089/0.022/0.070" (measured 0.344/0.089/0.022/0.070 —
"near-identical" is fair), and the item-4 notes' 1.5491/4.0889/4.9126 are
indeed what that file claims.

## 5. Bugs found (none changes any quoted digit)

1. **Two wrong series coefficients in `wp2b_lib.py` (repair 3).** The
   Bernoulli-series fallbacks (used for |u| < 0.1) have `g4: ... - u**5/22176`
   where the true series is **−u⁵/15840**, and `g5: ... - u**4/4435.2` where the
   true series is **−u⁴/3168** (sympy-confirmed, `ref5 (a)`). Measured impact
   (`ref4b/ref4c`): ≤ 2.8e-6 / 1.7e-5 relative on g4/g5 over (0, 0.1], ≤ 2.7e-6
   on any cumulant consumed downstream — the smallest margin any affected
   certified ratio enjoys is 4e-3 (NC-W2(d) k6 ratio 0.9959), so every quoted
   digit and every PASS is unaffected. Fix for hygiene.
2. **Hermite sup grids vs stated range (repair 5a).** Lemma W.4 Step 3 states
   the sups "for |y| ≤ 1/2"; NC-W3(1) certifies them only on |y| ≤ 0.05. The
   used range (h ≤ 0.04607) is covered by the grid, and I verified all eight
   inequalities on the full |y| ≤ 1/2 by hand (each is the one-line polynomial
   inequality claimed) — but the script's grid should match the stated range
   or the statement should quote the used range.
3. **A rounding slip in §4's parenthetical (repair 5b).** "e^{1.5/s2min} ≤
   1.00001 at m ≥ 180" holds only at K = 1 (1.0000095); at K = 4, m = 180 the
   factor is 1.0000153. The Lin *values* are computed with the true factor and
   are correct (independently reproduced).
4. **Cosmetic:** numpy is listed in the environment banner but unused by any
   wp2_b script.

## 6. A measurement the draft should incorporate (repair 4 — diagnosis, not error)

§5's Finding and §9 item 2 claim the true w²-envelope (~0.01 B_m w², vs the
proved 0.95 at K=4) arises from "a cancellation between (I) and (II) **and the
kernel bucket**", so that "proving c_w(4) = 1/2 would need a cancellation lemma
**coupling the buckets**". My signed measurement (`ref5 (d)`) contradicts the
coupling part: the TRUE signed sum the envelope must bound,
[(B_lam − B_m) + 36a²/P0²]/(B_m w²), is already only **+0.0050 .. +0.0109**
across m = 60..2000, w ≤ 4 — parts (I) (≈ −0.082 at w=4) and (II) (≈ +0.087)
cancel each other almost completely with **no kernel involvement**. So
c_w(4) ≤ 1/2 (indeed ~0.1-class) should be provable *inside Prop W.6 alone* by
a signed two-sided treatment of B_lam − B_m against 36a²/P0² — which needs
exactly the two-sided (signed) kappa_3-along-the-tilt boxes the draft's §9
item 4 already identifies as the missing ingredient for the closed-form PW
refinement. The repair is easier than the draft says; its proved constants are
still correct *as bounds*, and its c_w(4) = 1 fallback remains valid.

## 7. Status-label honesty check

The draft's own PROVED/PARTIAL/grid-certified markers survive scrutiny: W.0
(exact computation — verified independently), W.1(i) proved / W.1(ii) honestly
grid-labeled (and now exhaustively m-scanned by me), W.2–W.3 proved (hand-check
of the partial-fraction chains passes; box ratios ≤ 1 with stated margins), W.4
proved given its inputs (its only grid dependence at K=4 is W.1(ii), correctly
flagged; for K ≤ 2 the inputs are the proved W.1(i)/W.2/W.3, as claimed), W.5
conditional-as-labeled, W.6 sound (both min-clauses of the script's upper/lower
bounds are valid; the first upper clause even carries harmless extra slack
+(dir_ratio − 1)), W.7 an exact decomposition by construction with the kernel
bucket honestly left "pending (wp2-a)" and T.9 explicitly kept PARTIAL. §9's
"What remains" list is complete as far as my checks reach; nothing is claimed
closed that is not.

## 8. Required repairs (all minor)

1. **PW_grid K=4 scope/limit** (§0 item 3, Theorem W.7 table, §8 item 2):
   annotate that the certified 4.9126 is exceeded beyond the grid — measured
   4.9233 at (m, w) = (20000, 2.725) (+0.22%), still rising slowly in m —
   and either extend the certificate grid (finer w near 2.7, m to ~10⁵) and
   restate ≈ 4.93, or carry the K=4 grid-flavor row explicitly as "m ≤ 2000".
   Downstream comparisons (§8) are unaffected at their precision
   (C_R^PT grid K=4: 5.2985 → ≈ 5.31).
2. **W.1(ii) footnote**: the all-integer-m max of the four-band bound is
   0.379644 at (32, 4.0) (mod-4 bumps), not 0.3789 at (30, 4.0); ≤ 0.40 and
   c_4 = 0.60 unaffected.
3. **Fix the two `wp2b_lib.py` series coefficients** (g4: −u⁵/15840;
   g5: −u⁴/3168) and re-run — no quoted number will change at its printed
   precision (measured impact ≤ 2.7e-6 on cumulants).
4. **Reword §5 Finding / §9 item 2** per §6 above: the cancellation is
   internal to W.6's two parts (measured signed sum ≈ +0.005..+0.011 B_m w²);
   no bucket-coupling lemma is needed for c_w(4) ≤ 1/2, only signed two-sided
   kappa_3 boxes (already on the draft's own wish list, §9 item 4).
5. **Cosmetic**: (a) align NC-W3(1)'s Hermite grid range with the stated
   |y| ≤ 1/2 (or restate as the used range); (b) "1.00001" → "1.000016" in
   §4's parenthetical; (c) drop numpy from the environment line.

## What remains (referee's view)

Identical to the draft's own §9, which I endorse as honest and complete: the
kernel bucket (wp2-a) is the one missing piece of T2 §8 item 4; the
grid-certificate statuses (W.1(ii), PW grid flavor, Hermite sups) are
Sturm-able finite computations, correctly labeled; the far-region exponent and
m_2(K) thresholds (T2 §8 items 1, 5) are untouched here and remain the binding
constraint of T.9. Nothing in this report blocks the wp2-a merge; repairs 1–5
are one short editing session plus one library fix.

*End of report. Referee scripts and outputs: session scratchpad as listed in
the header; the four target scripts were re-run unmodified from a byte-copy;
no repository file other than this report was created or altered.*
