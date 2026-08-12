# Numerics referee report — wp3_draft_a2.md (wp3-a2, wave 2, 2026-08-11)

**Referee role:** adversarial numerics. Default to refutation. Judged alone
(no other wave-2 draft read; `g2_draft_t1_20260803.md` kept blind).
**Target:** `g2_campaign_20260811/wp3_draft_a2.md` and its four scripts under
`g2_scripts/campaign_20260811/wp3_a2/`.
**Referee scripts** (all new files, saved and run 2026-08-11):
`g2_campaign_20260811/referee_numerics_wp3_a2_scripts/ref_E_closedform.py`,
`ref_p4_chain.py`, `ref_p5_offgrid.py`, `ref_stitch_checks.py`,
`ref_nc3d_recheck.py`. Every number below is from a real run.

## VERDICT: MINOR_REPAIRS

All four draft scripts are genuine, run, and reproduce every quoted figure.
The load-bearing numerics — the P.4 constant chain, the m_p thresholds, the
P.5 ground-truth grid (which I extended 2x off-grid), the E(4) operating
constant, the deep-band eps truth, and the entire Theorem S threshold table —
survive independent re-implementation, including exact-arithmetic and
closed-form (series-free, pi-free) reroutes. No fabricated number and no
fabricated PASS was found. The findings (F1–F8 below) are: one wave-1-R1-class
unsafe-rounding defect in the "certified lower decimals" table (four of six
E-entries are NOT lower bounds as printed — though the operating point E(4)
is), one false truncation claim, one double-counted bucket constant
(safe direction), one wrong unscripted number ("~68" should be 82), and
prose/labeling repairs. None changes a threshold, a conclusion, or the
reduction's two named conditions.

## 1. Reproduction of the draft's scripts (all re-run)

| script | re-run result | quoted figures |
|---|---|---|
| `wp3a2_nc1_pentagon.py` (0.2 s) | PASS: 0 identity mismatches (7 m-values), 0 bracket/floor violations (min floor margin 0.00053 at (60,2)), 0 exact violations of `r(k)-1 >= (m-1)/(2k(m+k))` on 8<=m<=200, global min ratio 2.0002 at (200,2) | all match draft §3/§7 exactly |
| `wp3a2_nc2_constants.py` (0.2 s) | table (xc, Phimin, C_d, C_A, C_P, m_p) = draft §2 table exactly; m_p = 30/83/300/1581; measured maxima 0.7409–0.7482 / 1.0000 / 0.9471–0.9951 | match ("0.75", "1.00", "0.95..1.00" are fair summaries) |
| `wp3a2_nc3_handoff.py` (25 s) | caps approached from below (15 rows, none violated); E-decimals and floors as quoted; NC-P3(c) all 10 rows ok; NC-P3(d) rows 0.0385/0.0194/0.0117/0.0084 with trueC0 = 0.00 | match; see F1, F2, F6 |
| `wp3a2_nc4_stitch.py` (0.01 s) | operating point, clause ladder (79/20, 527/136), legacy rows (2.3e9, 6000, 3.8e5x), R1 margins (1879, 17364), crossover 63.3 | match; see F4, F5 |

## 2. Independent verification performed (adversarial reroutes)

1. **E(u) closed form, series-free** (`ref_E_closedform.py`): the draft
   computes `E(u)` as a 50000-term float partial sum of the partial-fraction
   series. I recomputed `E(u) = (1/12 - 1/u^2 + e^u/(e^u-1)^2)/u^2` in
   60-digit Decimal (no pi, no series; Decimal.exp is correctly rounded).
   The partial sums sit BELOW truth by ~4e-16..1e-15 for every u = 1..8
   (so the partial-sum mechanism is sound); the defects are in the printing
   (F1) and the tail claim (F2). The P.7 deficit identity
   `lambda - s2 = lam^2 [sum j^4 E(lam j) - m E(lam)]` was verified
   numerically to 1.6e-16 relative at three (m, lam), and the floor-step
   direction `lam^2[E(w)S_4 - m/240] <= lambda - s2` at three more.
2. **P.2/P.4 exact algebra** (`ref_p4_chain.py`): the shift-difference
   identities, the closed forms for `Delta^2 x_1`, `Delta^2 x_2`, the
   general-g `Delta^2` formula, and every per-g bound of the P.4 proof
   (`|d_g+| <= g x+^g/(k+1)`, `|d_g-| <= g x(k)^g/k`, `|D2 x_{1,2}| <= 2/m^2`,
   `|D2 x_g| <= 6 g^2 x+^{g-2}/m^2`, g >= 5) — exact Fractions, all m in
   {30, 45, 101}, all k in 2..m-1, all pentagonal g <= k+1: **0 mismatches,
   0 violations**. End-to-end P.4 conclusions (|d| <= C_d/m, |A| <= C_A/m^2,
   and the exact log-free surrogate `Phi(k-1)Phi(k+1) <= Phi(k)^2(1+C_P/m^2)`)
   against exact binomial Phi at (c, m) covering all four clauses incl.
   m = 101: **0 violations**.
3. **Constants recomputed with independent code** (`ref_p4_chain.py` part 4):
   pentagonal sums to g <= 600 with EXACT Fraction tails for BOTH sigma_1'
   and sigma_2^- (the draft's script omits the sigma_1' tail, ~1e-118, and
   uses a float tail for sigma_2^-): C_d/C_A/C_P agree with the draft's to
   9 decimals and **m_p = 30/83/300/1581 is reproduced exactly**. The
   omissions are certified harmless.
4. **Off-grid extension of NC-P1(c)** (`ref_p5_offgrid.py`) — wave-1
   precedent (a K=4 grid bound failed just past the grid edge): I extended
   the exact integer check of `r(k)-1 >= (m-1)/(2k(m+k))` to **all
   m = 201..400, all 2 <= k <= m-1: 0 violations**; global min ratio
   2.000038 at (400, 2), min over the c=1 band k > 0.7m: 2.001363 at
   (400, 281). Exact closed-form probe of the k = 2, 3 corner (Phi is
   exactly 1 - x_1 - x_2 there) at m = 10^3..10^6: ratio decreasing to 2
   from above (2.000006 at 10^3, 2.00000000 at 10^6), never below. The
   observed min corner cannot cross the factor-2 statement. Row generator
   sanity: sum = m!, symmetry, m=5 row vs A008302 — PASS.
5. **Stitch arithmetic exact** (`ref_stitch_checks.py`): B_m as exact
   Fractions (`B_m <= 1.08/m` for m >= 100 PASS; max of B_m·m = 1.079995,
   monotone toward 1296/1200 from below); the R3 w^2-bracket exact at
   m = 401 (`0.01627 - 0.00269 = +0.01358 > 0`); R2 budget with
   safe-direction rho (0.727106): eps* = 0.258352, budget 20/79.5317 =
   0.251472 <= eps*, conclusion 1.029462 >= 1.02; floors v(0.7)·401 =
   79.5317 >= 79 and v(1)·1581 = 527 exact; C* caps 20/136 reproduced;
   tilt caps as exact Decimal-ln inequalities (log 3 <= 1.0987,
   log(17/7) <= 0.8874, log 2 <= 0.6932, and the NC-P4 prints 0.8873/0.6931
   are valid lower roundings); legacy rows (2.304e9, 6000, 3.84e5) exact.
6. **NC-P3 independent implementation** (`ref_nc3d_recheck.py`): tilted
   moments recomputed by direct prefix-sum weighted sums (no g/q closed
   forms, no series); agreement with the draft's closed forms to 1e-15
   relative at four spot points. NC-P3(c)'s 10 rows reproduce identically.
   NC-P3(d) recomputed over **every** interior k in [2, N/2] at
   m = 30/60/140: max eps = 0.0385 (k=114) / 0.0194 (k=476) / 0.0084
   (k=2652) — the max over ALL interior k EQUALS the band max (so draft
   §6.1's "over EVERY interior k" claim is TRUE), and no k has eps > 0.25
   (the "trueC0 = 0" claim is TRUE).

## 3. Findings (most severe first)

**F1 (the only substantive one; wave-1 R1 class). Four of the six
"certified lower decimals" for E(w0) are NOT lower bounds as printed.**
The draft (P.7 table, §7 NC-P3b) presents the 8-decimal prints as certified
lower bounds ("50000-term positive partial sums"). The partial sums ARE
below truth, but the script prints them with `%.8f` NEAREST rounding, which
rounds UP for E(1), E(2), E(3), E(6) (and E(8) in the output):
60-digit truth E(1) = 0.0040069275411..., printed 0.00400693 (high by
4.6e-9); E(2) = 0.0035871871437..., printed 0.00358719; E(3) =
0.0030403586360..., printed 0.00304036; E(6) = 0.0016124067221..., printed
0.00161241. **E(4) = 0.0024899244245... and E(5) survive as printed** — the
w0 = 4 operating point is safe. Derived unsafe roundings: deficit floor at
w0 = 2 printed 0.0983 (true floor 0.0982889), at w0 = 4 printed 0.2729
(true 0.2728957); hence **"rho(4) <= 0.7271" is unsafe by 4.8e-6** (true
bound from the certified E(4): 0.7271048) — it appears in the P.7 box, §0,
and Theorem S's operating point. *Impact: nil on conclusions — I re-ran the
whole R2 chain with the safe rho = 0.727106: eps* = 0.258352, budget
0.251472, conclusion 1.029462 >= 1.02 all still hold. Repair: truncate
(don't round) the E prints, or quote E(1..3,6) one ulp lower and
rho(4) <= 0.7272 (or 0.727105).*

**F2. The truncation claim "< 2e-21" is false by ~4 orders of magnitude.**
The script's "omitted tail ~ 3x first term" heuristic is wrong for a ~n^-4
series: the true tail is ~(N/3)·(first term). Rigorous integral bound:
tail <= 6/(2 pi)^4 · 1/(3·50000^3) ~ 1.03e-17 (and the float-summation
error, ~6e-16, dominates even that). Measured: E_true - partial_sum =
+3.8e-16..+1.1e-15 over u = 1..8 — still comfortably below the 8th decimal,
so nothing downstream moves; but §7's precision note ("truncation size
printed (< 2e-21)") and P.7's "truncation < 2e-21" must be restated as
"< 2e-15 (float summation dominated)".

**F3. Lin is double-counted in Theorem S's R3 row (safe direction).**
wp2-b defines `C_R^PT = PW + T + Lin` (wp2_draft_b.md line 574: "pointwise
+ Taylor + Lin, kernel excluded"; its 5.2985 = 4.9126 + 0.01402 + 0.3719).
The draft's R3 row lists "buckets C_R^PT(4) = 5.30 ... + Lin = 0.372" and
concludes `>= 1 - B_m - [C_R^PT(4) + C_ker + Lin]/m^2`; §6.2 repeats it as
"[5.30 + C_ker + 0.38]/m^2". Lin (0.372) is already inside 5.2985. The
error is in the SAFE direction (overstates the error budget by 0.37/m^2)
and the bracket stays positive either way (verified exact with C = 10.71),
but the constant as displayed misquotes wp2-b's defined object. Repair:
either `[C_R^PT(4) + C_ker]/m^2` with C_R^PT = 5.30, or spell out
`[PW + T + Lin + C_ker]/m^2 = [4.93 + 0.37 + C_ker]/m^2`.

**F4. Unscripted number "~68" is wrong; truth is 82.** Derivation note 2
says the w^2-bracket crossover is "m >= 63.3 ignoring the (1 - 17 B_m)
factor, m >= ~68 with it". NC-P4 prints only 63.3; no script computes the
"with it" version. Exact recomputation (Fraction B_m, certified E(4),
C = 10.71): the bracket first becomes (and stays) positive at **m = 82**.
The claims actually consumed ("valid m >= 100" in the R3 row; positivity at
m = 401) are both TRUE (verified exact: +0.01358 at m = 401). Repair:
replace "~68" by 82, or drop the aside.

**F5. "17364x" overstates the exact margin.** R1 margin at (m, c) =
(1581, 1) is exactly (1580)^2·3167/(144·2·1581) = 17363.524; NC-P4's
`%.0f` print rounds it UP to 17364 and §3 remark 1 quotes "17364x". The
(401, 7/10) companion "1879x" is safe (exact 1879.056). Trivial magnitude,
margin-remark only. Repair: "17363x" or ">= 1.7e4 x".

**F6. §7's "Key verbatim excerpts" are not verbatim.** The excerpts are
condensed/reformatted (columns dropped, rows merged) and the NC-P3(d) block
contains a line no script prints: "(eps never exceeds 0.25 at ANY interior
k on the tested range)". The FACT is true — my independent implementation
confirms eps <= 0.25 (indeed <= 0.0385/0.0194/0.0084) at every interior k
for m = 30/60/140, and the script's trueC0 = 0.00 column implies it — but
an editorial sentence inside a quoted-output code block violates the
quote-real-output rule. Repair: relabel "condensed excerpts", move the
eps-line into prose, or add the print to the script and re-run.

**F7. Display roundings in the §2 constants table are nearest, not
safe-direction** (same class as F1, display-only): C_A(1/4) printed 5.923
vs true 5.923067 (low), C_d(1/2) 1.8053 vs 1.805309, C_A(7/10) 20.649 vs
20.649186, C_A(1) 34.920 vs 34.920037, C_P(1) 263.23 vs 263.230377,
Phimin(1/4) printed 0.7220 vs true 0.721956 (high — unsafe for a lower
bound). Harmless here because every downstream use (m_p ceilings, P.4
verdicts) is computed from the exact Fractions inside the script — I
reproduced m_p = 30/83/300/1581 from independently-coded exact constants
WITH exact tails for both series. The draft's §7 note already flags the
Phimin case (0.2330 vs 811/3481) but not the others. Repair: one sentence
("table entries are nearest-rounded displays of exact Fractions; all
verdicts use the exact values"), and note the omitted sigma_1' tail
(~1e-118, certified harmless).

**F8 (observation, no repair needed).** §7's NC-P3 summary "floors hold
with 82–90% capture" silently inherits P.7's w0 <= 4 scope; at w0 = 6 the
capture is 74.7%. P.7's own text states the scope correctly.

## 4. Spot-checks that found nothing wrong (for the record)

- NC-P1(c)'s four range rows all reporting the same min is genuine (the
  min sits at k = 2, inside every range) — draft §3 already remarks this.
- P.3(ii) floor constant 811/3481 = 0.232979 >= 0.2329: exact and safe;
  x(k) <= m/(2m-1) <= 30/59 at m >= 30: exact.
- P.6/NC-P4 floors: v(1/2) = 1/8, v(7/10) = 0.19833 (quoted 0.1983 as a
  floor coefficient — safe), v(1)·1581 = 527 exact.
- P.8 caps rounded UP (1.0987/0.8874/0.6932) — all safe (Decimal ln); the
  measured approach-from-below rows reproduce.
- B_401 quoted "0.00270" vs exact 0.0026900 — safe overcount.
- "6.85 E(1) = 0.02745 > 0.022" (T.10(2) comparison): true 0.0274475 — the
  displayed "0.02745" is nearest-rounded but the comparison is safe.
- Legacy arithmetic (2.3e9, 6000, 3.8e5x, 10086 for the c = 0.7 flavor)
  exact. Harness cross-claims ("m = 400", "C1–C6", "321 s") match
  `harness_m200_20260811.md` (320.9 s).
- eps*/0.0385 = 6.71: "margin ~7x" (NC-P4 print) and §6.1's "6x-plus" both
  fair.

## 5. What this report does NOT cover

Citation fidelity of T.x/W.x/W2b-x statements and the P.1–P.8 proofs' prose
logic are the maths referee's jurisdiction; I verified their numerical
content (identities, bound directions, constants) only. The two named
conditions of Theorem S (wp4's CL spec, wp2-a's C_ker) are open by the
draft's own honest labeling; nothing numeric contradicts the spec's
feasibility (the measured eps margin at the spec point is 6.7x, reproduced
independently).

*End of report. Verdict: **MINOR_REPAIRS** — repairs F1–F7, all text/print
level; no constant, threshold, table entry (at its true exact value), or
conclusion of wp3_draft_a2.md is invalidated.*
