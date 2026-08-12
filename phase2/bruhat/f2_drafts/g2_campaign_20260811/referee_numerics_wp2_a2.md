# Numerics referee report — wp2_draft_a2.md (package wp2-a2)

*Adversarial numerics referee, wave 2, 2026-08-11/12. Target:
`wp2_draft_a2.md` + scripts under `g2_scripts/campaign_20260811/wp2_a2/`
(2 libraries + 6 NC scripts, incl. the 3 inherited files disclosed in the
draft's provenance note). Protocol: default to refutation; re-run every
script; verify every quoted number against real output; re-implement
float-dependent checks independently (mpmath dps 30–60, exact ints/Fractions
where feasible); spot-check every grid OFF-grid (wave-1 precedent: a K=4
grid bound exceeded just past the grid edge). Other wave-2 drafts not read
(`wp3_draft_a2.md` untouched; `g2_draft_t1` blind). New files only:
this report + 4 referee scripts under `referee_numerics_wp2_a2_scripts/`.*

## VERDICT: MINOR_REPAIRS

Every one of the six NC scripts is genuine, runs, and reproduces the draft's
§8 quoted outputs **verbatim — zero mismatches at every printed digit**. My
independent dps-60 re-implementation of the entire refined bound from the
draft's formulas (not the code) matches the shipped float assembly to
relative 1e-15 on every headline constant and every per-piece entry. The
grid-certified monotonicity claims survive aggressive off-grid attack
(unit-step 1000–3000, step-20 3000–10^4, and m up to 10^6: all decreasing,
all below the headline constants). An independent ground-truth measurement
(own Mahonian implementation, exact Fractions, mpmath Newton with asserted
residuals) reproduces the m = 60 anchors to 4 decimals. No fabricated
number anywhere. The repairs demanded (§4) are prose/table-level: one
misdescribed grid density in §0, one per-piece table row that silently
mixes m-values, one misquoted truth range, one un-scripted aside constant.
None touches a theorem constant, threshold, or verdict.

---

## 1. Reproduction of the draft's scripts (all six re-run)

| script | draft verdict | my re-run | quoted-vs-actual output |
|---|---|---|---|
| `wp2a2_nc1_model_err.py` (NC-A1, inherited) | PASS | PASS (12.1 s) | every §8 line identical: eps table (0.1735/0.1932/0.2796 at 180; 0.1873/0.2087/0.3019 at 30), global ratios 0.999312 / 0.191026, cumulant dev 1.33e-12, kernel-identity devs 3.21e-38 / 1.25e-41 / 6.19e-38 / 5.01e-41 |
| `wp2a2_nc2_buckets.py` (NC-A2, inherited) | FAIL (by design) | FAIL, exit 1 (9.2 s) | crude row 180/1: 47.4418 → 53.4047; 180/4: 449739.9956 (far 3.62e+05); thresholds 136/181/367; non-monotone at m = 787/256/368 — all identical |
| `wp2a2_nc3_refined.py` (NC-A3) | PASS | PASS (65 s) | split ratios WR 0.085347 / WI 0.191037 / ZI 0.943412; every quoted per-piece row identical (27.3882/3.4951/30.8863; 209.0224 at 181 via (5); 37810.0442 at 367; 21.0810 at 400; 14.0048 at 2000); mker 136/181/367; monotone True ×3; comparison table 22.2x/51.4x/7502.0x |
| `wp2a2_nc4_truth.py` (NC-A4) | PASS | PASS (1.3 s) | ports (10.277/21.059/187.265 vs certified, all below, within 0.1%); truth 1.386/4.070/5.022 (m=60 full scans, 101/197/357 pts) and 1.354/4.054/5.038 (m=140 step 8); min v 1.288e-05; LFlow table incl. 0.92237/0.96388/0.98716 |
| `wp2a2_nc5_merge.py` (NC-A5) | PASS | PASS (0.9 s) | C_R tables 32.4358/41.1647, 213.1123/230.0864, 37814.9708/37997.4722; H = 0.0097/0.0241/0.3321; 3000-vs-10^4 rows 13.20>11.75, 130.70>126.18, 30909.94>30283.47; honesty 118x/657x/108564x |
| `wp2a2_nc6_zbar.py` (NC-A6) | PASS | PASS (0.3 s) | max zbar = 3.394e-07 at (4, 367) |

Headline-constant arithmetic re-verified by hand: C_ker roundings 30.8863 →
30.89, 209.0224 → 209.03, 37810.0442 → 37811 (all safe-up); every C_R sum
(PW + T + C_ker, both flavors, all K) recomputed exactly from the certified
addends — all six table entries correct; H(K, M(K)) recomputed — correct.

**Fabrication scan: NEGATIVE.** Every number quoted in the draft (§0, §2,
§5–§9 and the §8 transcripts) traces to one of the six saved scripts I
re-ran, with two disclosed-as-such exceptions handled in §3 below (the §7
aside "m ~ 27", finding R-F4; and inherited-package citations, all of which
I verified against their source files — §3.4).

## 2. Independent adversarial verification (4 new referee scripts)

All under `referee_numerics_wp2_a2_scripts/`, run 2026-08-12; full outputs
quoted in the run transcripts below each item.

### 2.1 R1 `ref_a2_monotone_offgrid.py` — the grid attack. **PASS.**

The constant flavor of Theorem D.5 rests on `C_ker2(K, m) <= C_ker2(K,
M(K))`, certified by NC-A3(3) on [M(K), 1000] unit-step + (1000, 3000]
step 10, and by NC-A5(3) at the single pair (3000, 10^4). I attacked every
gap:

- Faulhaber closed forms for S4/S5/S6 verified exactly (Fraction equality)
  against the library's direct sums, then patched in (bit-identical Cker
  confirmed at (4, 3000): 30909.9360988850 both routes);
- **unit-step [1000, 3000]** (fills the draft's step-10 band): decreasing,
  K = 1, 2, 4 — no violation at any of the 3 × 2001 points;
- **step-20 [3000, 10000]** (fills the endpoint-only band): decreasing ×3;
- **beyond the draft's last point**: m ∈ {1e4, 2e4, 5e4, 1e5, 2e5, 5e5,
  1e6}: strictly decreasing throughout, limits ~10.40 / 122.61 / 29914.8 —
  every value far below the headline constants 30.8863 / 209.0224 /
  37810.0442.

```
  (b) unit-step monotone decrease on [1000, 3000]:  K=1/2/4: True True True
  (c) step-20 monotone decrease on [3000, 10000]:   K=1/2/4: True True True
  (d) K=1 m=1000000  Cker2 =      10.3950  <    30.8863: True  (< prev)
      K=2 m=1000000  Cker2 =     122.6050  <   209.0224: True  (< prev)
      K=4 m=1000000  Cker2 =   29914.7765  < 37810.0442: True  (< prev)
R1 VERDICT: PASS
```

The wave-1 failure mode (bound exceeded just past the grid) does NOT occur
here; the draft's §6 exponent-audit story (all rows negative net m-power
except the pure-alpha quartics, which decrease to positive limits) is
quantitatively confirmed. The grid-certificate flag the draft itself
carries for m > 3000 (§6 scope note, §10 item 2) is honest and, per this
check, safe. (But see R-F1: §0 misdescribes the shipped grid density.)

### 2.2 R2 `ref_a2_highprec.py` — independent dps-60 re-implementation. **PASS.**

I re-implemented the ENTIRE refined bound (boxes A3–A7, eps, split
majorants WR/WI/VE/VO/VQ, Gaussian moments, tails, far, D_box/D_tail/D_out,
E_pt, dbar, core/vS2, zbar, Cker) in mpmath dps 60 **from the draft's
displayed formulas (Lemmas D.1'–D.4, Theorem D.5), not from the library
code**, and compared at 8 (K, m) pairs including all three headline points:

```
  K=1 m= 180  Cker(hp) = 30.886327536  rel dev = 5.62e-16  worst piece dev = 3.19e-15
  K=2 m= 181  Cker(hp) = 209.022408731 rel dev = 7.49e-16  worst piece dev = 9.47e-15
  K=4 m= 367  Cker(hp) = 37810.0442233 rel dev = 4.12e-16  worst piece dev = 8.08e-15
  (+ 400 ×3, 2000 ×2: all rel devs <= 1.31e-15, pieces <= 7.34e-14)
R2 VERDICT: PASS
```

Two conclusions: (i) no float-cancellation artifact anywhere in the
assembly (everything is a positive sum; confirmed); (ii) **the shipped code
implements exactly the draft's formulas** — I derived the monomial algebra
independently (D_2 moduli from U_0^2/2 degree 9–12; WR/WI from the
integral-form cube remainder with the |sin(tau zI)| <= tau|zI| trick; the
four-slot box bracket; the st-cross-term cancellation; the strip covers)
and found full agreement. The pair/J/tail conventions all check.

### 2.3 R3 `ref_a2_offgrid_truth.py` — majorant truth OFF the draft's grids. **PASS.**

NC-A1(b,c)/NC-A3(1) used m ∈ {30, 60, 120}, w ∈ {K/4, K/2, K}, t-grids
t1·i/48. I used m ∈ {45, 240} (both off the draft's set), w ∈ {0.15K,
0.7K, 0.95K, K}, and OFFSET grids t = t1(i−0.37)/64 (no shared point,
probing nearer t = 0), dps 40 — additionally testing two bounds the draft
uses but never truth-checked numerically (|Re e^{-z}| <= EE and the
Q-majorants VE, VO):

```
  GLOBAL maxima: a 0.999780  wr 0.121544  wi 0.211168  zi 0.944298
                 re 0.999783  ve 0.996044  vo 0.945311
R3 VERDICT: PASS
```

All seven ratio families stay <= 1 at all 1536 off-grid points (2 m × 3 K
× 4 w × 64 t). Note the
margins are real but not decorative: A.1a reaches 0.9998, |Re Q−1|/VE
reaches 0.9960 (at small w), Im-family ~0.944–0.945. These bounds hold by
the analytic proofs (which I checked line-by-line for D.1/D.1'/D.3/D.4(i)
and found sound — the eps-absorption bookkeeping included); the numerics
confirm no slip in the constants.

### 2.4 R4 `ref_a2_truth_indep.py` — independent ground truth at m = 60. **PASS.**

Fully independent of the package's float library: own Mahonian rows (direct
convolution, checked sum = 60! and palindromy — 1771 exact integer
coefficients), u as exact Fraction, lam(k) by mpmath Newton on the g0
closed form with **asserted** residual < 1e-20 at every k (the draft's
lam_solve computes but never asserts its residual — R-F7), v and s2 from
mp.diff cumulants at dps 30, full interior scans:

```
  K=1: measured m^2|Delta_ker| = 1.3863  (anchor 1.386, ok)  <= bound 25268.2
  K=2: measured m^2|Delta_ker| = 4.0702  (anchor 4.070, ok)  <= bound 439342.8
  K=4: measured m^2|Delta_ker| = 5.0216  (anchor 5.022, ok)  <= bound inf (not assembled at m=60, K=4 — not claimed either)
  min v over the scan: 1.5981e-04 > 0
R4 VERDICT: PASS
```

This confirms, independently of wp2-b AND of this package's float code,
the truth anchors and the measured-below-bound claims, and the v > 0
measurement (the draft's smaller 1.288e-05 minimum comes from its m = 140
scan; v ~ 1/s2 shrinks with m — consistent).

---

## 3. Do the scripts test what the prose claims? (audit outcomes)

### 3.1 The port question (NC-A4(1)'s "-0.08%, safe") — RESOLVED, legitimate.
The wp2a2 port of `PW_closed` sits 0.001–0.149 below wp2-b's certified
values because `wp2a2_lib.P0_min` DROPS the three odd h-terms
(`3ah + 15dh + 105abh`) that wp2-b's `P0_min` carries. I checked the
mathematics: at y = 0 the odd Hermite values vanish (`He_3(0) = He_5(0) =
He_7(0) = 0`), so `P(0) = 1 − 3b − 15(g + a²/2) + 105(b²/2 + ad)` and the
h-free floor is VALID (indeed sharper); wp2-b's h-terms were a harmless
extra conservatism. Consequences verified: (i) the merge table carries
wp2-b's certified larger values verbatim (safe); (ii) inside `core`
(D.4(iii)) the port's own chain `|N(0)/P(0)²| <= 36a²/P0min² + PW/m²` is
internally consistent with its own valid P0min — NOT an anti-conservative
mix. No defect; the draft should say in one line why the port differs
(currently only "port −0.08%, safe" — see R-F5).

### 3.2 Coverage claims. The strip covers (D.3 ii/iii) double-count corners
in the safe direction (checked); the st-cross-term drop is exact by oddness
over the symmetric domain, applied to a bound that is already pointwise
nonnegative times the nonnegative kernel majorant `(s−t)²/2` (checked);
extension of box integrals from [−t1, t1] to R is monotone (nonnegative
integrands — checked). The far constant: `far = 2(π − t1)e^{−c1(K)m}`
correctly instantiates wp1-c W.4(i) (measure of the strip × sup bound;
hypotheses `|lam| <= K/m <= 1/4·1`, `m >= 30` hold on every use;
`t_1 = sqrt(2)π/m` matches wp1-c's definition — verified against
`wp1_draft_c.md` lines 87/352).

### 3.3 The odd-cube finding (§6) is real and correctly diagnosed. NC-A2
(crude route) genuinely fails monotonicity at m = 787/256/368 (re-run,
exit 1), while the split route passes everywhere including my off-grid
scans; the mechanism (bare `A3³ t^9` row entering at `K³m^{−3/2}`) is
visible in the monomial algebra I re-derived in R2. Keeping the FAIL
script as the record is proper practice.

### 3.4 Inherited-package citations spot-checked against sources (all correct):
- wp1-c: `c_1(1) = 0.2259, c_1(2) = 0.1802, c_1(4) = 0.1019`; W.4(i) on
  `[t_1, π]`, `m >= 30`, `K <= m/4` — matches `wp1_draft_c.md` (§4, lines
  349–352, 390–393);
- wp2-b: PW_grid 1.5491/4.0889/4.9126 (m <= 2000, K=4 repair-B3 caveat
  carried in the draft's §7 — carried correctly), PW_closed
  10.278/21.063/187.414, T 0.00035/0.00100/0.01402, m²Lin
  0.2308/0.2571/0.3719, Lin = (9/8)e^{1.5/s2min}/s2min with the
  `|s2 log r − 1| <= 1/2` hypothesis, c_w = 0.407/0.466/1 (0.4067/0.4658
  rounded safe-up + repair B2), NC-W4(6) anchors incl. the m = 140 row
  (1.386/4.059/5.038), needed_env worst 0.35 — all match `wp2_draft_b.md`;
- g1_draft_b: `B_m <= 1.080/m` for m >= 30 is exactly B.0(ii);
- T2 (+ its wave-2 maths referee, which the draft cites for two-referee
  status): `A7 = (m+1)^8/2.8e6` with "chain gives 2.8549e6" — matches
  `referee_t2_maths.md` §2.12 (`1/2.8549e6 >= 1/2.8e6`, safe direction
  confirmed: the smaller denominator ENLARGES A7); the "ratio 0.212"
  aside in §9 item 2 matches `g2_draft_t2_20260803.md` line 1073;
- harness: `harness_m200_20260811.md` does certify exact ground truth on
  `4 <= m <= 400` ("# rows: 397, failures: 0"), so the §7 coverage
  argument's premise holds; `M(K) = 180/181/367 <= 400` re-verified.
- constants: `C5UP = 5.08266e-3 >= 48ζ(5)/(2π)^5 = 5.082653...e-3` and
  `C6UP = 3.96835e-3 >= 240ζ(6)/(2π)^6 = 1/252 = 3.968253...e-3` — both
  safe-up (recomputed);  `CK = {0.967, 0.868, 0.60}` and their statuses
  (c_4 grid-certified) flagged in the draft exactly as STATUS §2b demands.

### 3.5 Merge arithmetic (Theorem T.9-final). All six C_R entries, the
three H values, and the coverage logic re-verified by hand and by NC-A5
re-run; the Lin-discharge inequality chain `|s2 log r − 1| <=
(1.080/m)(1 + c_w K²) + C_R/m²`, decreasing in m, is correctly evaluated
at M(K) (H = 0.0097/0.0241/0.3321, checked digit-by-digit). The `w`-
uniformity remark (D.5's bound has no residual w-dependence beyond the
K-boxes) is accurate as a description of the code: every majorant
coefficient uses the box `A3(K)`, never `w` itself — confirmed in R2.

---

## 4. Findings and required repairs (none touches a constant, threshold, or verdict)

**R-F1 (the only substantive one — misdescribed certificate grid).** §0
item 1 states the constant-flavor monotonicity is "certified DECREASING in
`m` on the stated range (unit-step to 3000, spot-checked to 10^4)". The
shipped NC-A3(3) grid is **unit-step only to 1000, step 10 on (1000,
3000]** — §6's scope note and §10 item 2 describe it correctly, so §0
contradicts the draft's own fine print. Repair: reword §0 to match §6
("unit step to 1000, step 10 to 3000, spot 10^4"), or cite this report's
R1, which has now verified unit-step on [1000, 3000], step-20 on [3000,
10^4], and decrease through m = 10^6 — the stronger claim is TRUE, it just
was not what the draft's script did.

**R-F2 (per-piece table hygiene).** Theorem D.5's table rows labeled
`181 2` and `367 4` silently mix m-values: box and far carry the honest
parentheticals "(at 180)"/"(at 379)", but the tail and den columns are
ALSO from m = 180/379 (e.g. den 17.65 is the m = 180 value; den 1380.6310
is the m = 379 value printed in the m = 367 row) while only C_ker
(209.022/37810.044) is the true M(K) value (from NC-A3(5)). NC-A3(2)
simply never prints full rows at 181/367. Repair: print genuine full rows
at m = 181 and 367 (one-line script change), or extend the parenthetical
to all four borrowed columns.

**R-F3 (misquoted truth range, trivia).** §6: "m²|Delta_ker| is measured
FLAT at 1.374–1.386 over m = 30..140 (wp2-b NC-W4(6))". wp2-b's table has
**1.391 at m = 100** (K = 1); the range should read 1.374–1.391. No
consequence (headline bound 30.89).

**R-F4 (un-scripted numeric aside).** §7 "Downstream arithmetic": "C' = 42
moves the center-margin crossover only to m ~ 27 << 400" — no script in
this package (or quoted from elsewhere) produces 27; house honesty rule
requires script provenance for every numeric claim. Low stakes (explicitly
an aside for G4, which is untouched), but repair: add the two-line solve
to a script, or soften to "to m of order 30 (NC-13's scaling)".

**R-F5 (documentation of the port difference).** NC-A4(1)'s "PW = 187.265
(187.414, port −0.08%, safe)" is correct but unexplained; per §3.1 the
cause is the (valid, sharper) h-term-free `P0_min` at y = 0. One sentence
in §5 or the lib docstring should record this so a future reader does not
suspect a porting bug. (I verified there is none.)

**R-F6 (rounding provenance, cosmetic).** §5's "(NC-A4(3): LFlow >= 0.9224
at every (K, m) the theorem uses)": the constant 0.9224 is 0.92237 — the
(K, m) = (4, 180) value — rounded UP, and (4, 180) is not theorem-used
(M(4) = 367, where LFlow = 0.96388). The claim as stated is true (min over
theorem-used pairs is 0.96388 >= 0.9224) but the quoted constant is an
unsafe rounding of a non-theorem point. Restate as ">= 0.9223" or quote
0.96388.

**R-F7 (script hygiene, no action forced).** NC-A4's `lam_solve` computes
its Newton residual and discards it (no assertion); a silent
non-convergence would corrupt the truth scan invisibly. My R4 re-ran the
m = 60 scans with asserted residuals < 1e-20 and reproduced every value
(1.3863/4.0702/5.0216), so the shipped numbers are right; add the assert
in any future re-run. Also trivia, same class: NC-A2(2)'s `first_ok`
branch is dead code (inherited FAIL-record script — fine to leave).

## 5. Status assessment

The draft's own labels are honest and correctly propagated: the m-dependent
Theorem D.5 flavor is proof-grade GIVEN its inputs; the constant flavor and
the inherited items (c_4 floor, c_w envelope, PW grid) carry grid-
certificate flags exactly as STATUS §2b requires, itemized in §1 and §10.
The 22x/51x/7502x slack over truth is disclosed prominently (§0, §9) with
per-piece attribution that matches the actual code output. From the
numerics side, T2 §8 item 4's closure claim is supported: the missing
bucket now has a real, reproducible, off-grid-robust explicit bound, and
the merge arithmetic is verified end to end.

**VERDICT: MINOR_REPAIRS** — all seven findings are text/label-level;
apply R-F1–R-F4 (and optionally R-F5–R-F7) in a repairs file per the
no-erasing rule. No mathematical or numerical defect found: all 6 scripts
reproduce exactly, the independent dps-60 rebuild agrees to 1e-15, all
grids survive off-grid attack to m = 10^6, and the ground truth
reproduces independently.

*Referee scripts (saved + run): `referee_numerics_wp2_a2_scripts/`
`ref_a2_monotone_offgrid.py` (R1), `ref_a2_highprec.py` (R2),
`ref_a2_offgrid_truth.py` (R3), `ref_a2_truth_indep.py` (R4). No existing
file modified.*
