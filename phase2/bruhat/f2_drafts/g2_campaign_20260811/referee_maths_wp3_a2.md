# Adversarial MATHS referee report — `wp3_draft_a2.md` (wp3-a2, region-2 handoff)

*Referee pass 2026-08-11 (wave 2). Target: `wp3_draft_a2.md` + its four
scripts under `g2_scripts/campaign_20260811/wp3_a2/`. Method: every lemma
re-derived by hand (the P.2/P.4 shift identities and second-difference
displays additionally re-verified in EXACT `Fraction` arithmetic by my own
scripts, independent code); the whole P.4/P.5 constant chain independently
recomputed at 50 dps; Theorem P.5's ground truth re-checked on an
independently coded Mahonian generator; every kernel/deficit constant of
P.7 recomputed from the closed form (not the draft's partial sums); every
citation (T2, g1_draft_b, wp1-c, wp2-b, `referee_t2_maths.md`,
`repairs_20260811.md`, `harness_m200_20260811.md`) opened and checked
against the quoted hypotheses and statuses; circularity with Prop 3.5
hunted explicitly; the Theorem S partition checked for `(m, k)` gaps
boundary by boundary. Default-to-refutation stance. Blind protocol: neither
`g2_draft_t1_20260803.md` nor any `wp2_a2` material was read. No existing
file modified; referee scripts saved (new files) under
`g2_campaign_20260811/referee_wp3a2_scripts/` (`ref_wp3a2_check1.py`,
`ref_wp3a2_check2.py`; both run 2026-08-11, verbatim output quoted in §5
below).*

---

## VERDICT: MINOR_REPAIRS

**The mathematics survives.** The new pentagonal machinery (Lemmas P.1–P.4,
Theorem P.5) — the genuinely novel content of this package — is correct: I
re-derived every identity by hand, confirmed the three second-difference
displays in exact arithmetic (zero mismatches over full `(m, k, g)` grids),
reproduced the `C_d/C_A/C_P/m_p` table independently to all printed digits,
and re-verified `r(k)-1 >= (m-1)/(2k(m+k))` with zero violations on an
independently written row generator. Lemmas P.6 and P.8 are correct
one-liners from correctly quoted citable inputs; P.8's conditional-mean
argument is sound. Theorem S's four-region partition is genuinely gap-free
in `(m, k)`, its two named conditions (wp4's `CL(79, 20, 0.89)`; wp2-a's
`C_ker`) are exactly the right residue, and — critically — the draft
nowhere assumes Prop 3.5, nowhere uses T.8's uncertified `C_0 = 2000` /
`C = 600`, and nowhere uses the two T2 items the T2 maths referee broke
(T.10(2), T.8''). All citation statuses claimed in the draft check out
against the actual files on disk (verified: `referee_t2_maths.md` is
MINOR_REPAIRS with T.5/T.4-kernel/T.9'' confirmed and T.10(2)/T.8''
broken, exactly as the draft says; `repairs_20260811.md` +
`referee_repairs_20260811.md` [SURVIVES] discharge the wp1-c/wp2-b lists
including `c_w(4) = 1` (B2); `harness_m200_20260811.md` certifies C1–C6
exactly to `m = 400`).

**What does not survive as written** is a cluster of statement-level and
rounding-direction defects, none of which moves a conclusion:

- **(R1, the only finding with mathematical content)** Lemma P.7's first
  clause is stated for *every real `w`* but its displayed proof establishes
  it only where the bracket `1 - 1/(48 E(w) m^4)` is >= 6.85/6.857 — the
  draft's own parenthetical concedes `|w| <= 8` (at `m >= 30`). At, e.g.,
  `m = 30`, `|w| >~ 57` the displayed chain no longer delivers the constant
  6.85. The clause is numerically true at large `w` (I measured deficits
  0.93–0.99 vs floors 0.55–0.57 at `w = 20, 60`) but not proved as stated.
  Repair: rescope clause 1 to `|w| <= 8` — the draft never uses more (the
  operating point is `w0 = 4`; the table stops at `w0 = 6`).
- **(R2)** Four of the six "certified lower decimals" for `E(w0)` are
  round-to-NEAREST, not round-down: true values `E(1) = 0.0040069275...`,
  `E(2) = 0.0035871871...`, `E(3) = 0.0030403586...`,
  `E(6) = 0.0016124067...` are all *below* the printed
  `.00400693/.00358719/.00304036/.00161241`. Consequent unsafe roundings
  at the 1e-5-and-below level: the operating-point pair
  `deficit >= 0.2729` / `rho(4) <= 0.7271` (proved: `0.272895` /
  `0.727105`), the `w0 = 2` row `0.0983`/`0.9017` (proved
  `0.098289`/`0.901711`), R2's "`= 1.0294`" (true `1.02929`), and
  "`>= 0.01628`" (true `0.0162749`). Every downstream margin absorbs these
  (R2 needs only `>= 1.02`, actual `1.0293`), but this is exactly the
  wp1-c-R1 class of error the campaign has already been burned by.
- **(R3)** Derivation note 2's "`m >= ~68` with it" is printed by NO saved
  script (honesty-rule breach) and is WRONG: with exact `B_m`, the bracket
  `6.85 E(4)(1 - 17B_m - C/m^2) - B_m` first turns nonnegative at
  **`m = 82`**, not 68. The load-bearing claims survive untouched: the
  bracket is `+0.00317` at `m = 100` (the row's "valid `m >= 100`" is
  correct) and `+0.01359` at `m = 401`.

Plus the smaller items R4–R8 (§4). With R1–R3 applied — one rescoped
statement, one table of decimals reprinted truncated-down, one parenthetical
corrected — the package stands. **No constant, threshold, region boundary,
or conditional changes.**

---

## 1. What was independently verified (and how)

### 1.1 Lemma P.1 (pentagonal expansion to `k = m`) — CORRECT.
Hand-check: `prod_{j=1}^m (1-q^j) = prod_{j>=1}(1-q^j) * prod_{j>m}(1-q^j)^{-1}`
and the second factor is `1 + O(q^{m+1})`, so degrees `<= m` agree; Euler
plus convolution with `(1-q)^{-m}` gives the display. The restriction
`k <= m` is real and correctly observed everywhere downstream (§3 remark 3
honestly explains why `k > m` fails). Script NC-P1(a) re-run: 0 mismatches,
7 values of `m`.

### 1.2 Lemma P.2 (correction factor, shift ratios) — CORRECT.
- `x_g(k) = T(k-g)/T(k) = prod_{i<g} (k-i)/(m+k-1-i)`: telescoping from
  `T(j-1)/T(j) = j/(m+j-1)`; my exact check over all `(m, k, g)` grids
  (`m in {5, 17, 30}`, all `k <= m`, all `g <= k`): **0 mismatches**.
- Envelope (i): cross-product difference is `i(m-1) >= 0` — re-derived, sign
  correct (each factor `<= x(k)`, so `x_g <= x^g`).
- Shift-difference forms (iii): both numerators reduce to `g(m-1)` — I
  expanded both by hand ((k+1)(m+k-g) - (k+1-g)(m+k) = g(m-1); one step
  down likewise) and confirmed the boundary cases `g = k+1` (up-shift) and
  `g = k` (down-shift) where one side vanishes: the identities remain exact.

### 1.3 Lemma P.3 (bracketing, floor) — CORRECT.
Signs of the pentagonal pairs verified against Euler (`(1,2) -> -`,
`(5,7) -> +`, `(12,15) -> -`); `x_g` nonincreasing in `g` since each added
factor is `<= 1`; alternating-pair bracket standard. Floor: `1 - x - x^2 > 0`
below the golden ratio; `x(k) <= m/(2m-1) <= 30/59` for `k <= m, m >= 30`
(monotone in `m`, worst at 30 — checked); `811/3481 = 0.232978...` exact.
One pinhole (R7): P.4(iii) applies the floor at `j = k-1 = 1` when `k = 2`,
outside P.3's stated range `2 <= k <= m`; trivially true there
(`Phi(1) = 1 - 1/m`), one-line fix.

### 1.4 Lemma P.4 (difference bounds) — CORRECT; chain reproduced exactly.
My exact-`Fraction` verification of the three displayed second differences:

- `Delta^2 x_1 = -2(m-1)/[(m+k)(m+k-1)(m+k-2)]`: verified for
  `m in {7, 30, 101}`, all `2 <= k <= m-1` — **0 mismatches** (I also
  re-derived it by hand; the numerator collapses to `2(k - (m+k) + 1)`).
- `Delta^2 x_2 = 2(m-1)(m-2k)/[(m+k)(m+k-1)(m+k-2)(m+k-3)]`: same grids,
  **0 mismatches**, including `k = 2` (where the draft's
  `(k-1)`-cancellation remark is right).
- The `g >= 5` display
  `Delta^2 x_g = x_g(k) g(m-1)[(g-1)(m+k) - (g+1)k]/[(k+1-g)k(m+k)(m+k-1-g)]`:
  verified exactly for `g in {5, 7, 12, 15}` on the case range
  `g <= (k+1)/2` — **0 mismatches**. The inequality steps
  (`|(g-1)(m+k)-(g+1)k| <= 2g(m+k)`, `k+1-g >= (k+1)/2`,
  `m+k-1-g >= m-1`, `(k+1)/k <= 3/2`) all check; the complementary case
  `g > (k+1)/2` (separate one-sided differences, `k+1 <= 2g`) closes with
  `5g^2 <= 6g^2` as displayed, and the boundary terms (`g = k, k+1`) are
  covered because the difference identities remain exact there (1.2).
- Constant chain: my independent 50-dps recomputation of
  `sigma_1'(xc)/xc`, `4 + 6 sigma_2^-(xc)`, `C_P = C_A/Phimin + C_d^2/Phimin^2`:
  `C_d = 1.46748/1.80531/2.08225/2.48038`,
  `C_A = 5.92307/12.4429/20.6492/34.920`,
  `C_P = 12.3359/36.165/83.6064/263.23` — the draft's table to all printed
  digits, with the printed values correctly rounded UP (safe for an error
  constant). `xc(c) = (30c+1)/(30(1+c))` is decreasing in `m` (checked by
  differentiation), so "worst `m = 30`" is right; the `c = 1` special case
  `30/59` is right for `k <= m-1`.

### 1.5 Theorem P.5 — CORRECT (statement, proof, thresholds, and truth).
`log r = log r_T + D_Phi` with `r_T(k) - 1 = (m-1)/(k(m+k))` re-derived
exactly (`(m+k-1)(k+1) = k(m+k) + (m-1)`). The threshold algebra
`m >= 3 C_P c(1+c) + 1` reproduces `m_p = 30/83/300/1581` from my
independent `C_P` values (`ceil(12.565/82.371/299.475/1580.382)` — matches).
Ground truth: my independently coded generator (naive polynomial product,
different algorithm from the draft's running-sum) at `m = 50, 121`, all
`2 <= k <= m-1`, exact cross-multiplication: **0 violations**, min ratios
2.0024/2.0004 — consistent with the draft's 0 violations and global min
2.0002 at `(200, 2)` (its script re-run reproduced verbatim).

### 1.6 Lemma P.6 — CORRECT.
T.5-final is quoted with its true hypotheses (interior `k <= N/2`, `m >= 2`)
and its true status (T2 maths referee §2.6: "CORRECT, fully" — I opened the
report and confirmed). Monotonicity in `k` is trivial; the `c = 1` band
(`k >= m`) gives `>= m/3` verbatim.

### 1.7 Lemma P.7 — CORRECT at every consumed point; statement over-scoped (R1).
The engine identity `lambda - s2 = lam^2 sum_j [j^4 E(lam j) - E(lam)]` — T2's
(T.4) Step-2 display, confirmed correct by the T2 maths referee — was
additionally re-verified by me against exact truncated-geometric variances
(40 dps): rel. deviation `<= 1e-36` at `(m, w) in {25, 60} x {1, 4, 6}`.
The chain `E` decreasing `=> sum >= E(w) S_4 - m/240`, then
`S*_4 >= m^5/5` (`m >= 8`, T2's exact bracket — note the draft uses
`S_4 >= m^5/5`, which is *weaker* than the certified `S_4 - m >= m^5/5`:
safe), then `lambda <= 1.05 m^3/36` (B.0(i), correctly an UPPER bound since
it divides a positive deficit): `36/(5 * 1.05) = 6.857...` — all checks.
The monotone second clause via merged-draft Lemma 3.3 (fully proved) is
legitimate. Scope defect and rounding defects: R1, R2 (§4).

### 1.8 Lemma P.8 — CORRECT.
`E[G | G < j] <= E[G]` for the geometric (conditioning on a lower set lowers
the mean — the draft's one-line argument is sound since
`E[G | G >= j] >= j > E[G | G < j]`), `mu(lam) <= m/(e^lam - 1)`,
`mu(lam_c) <= cm <= k`, `mu` strictly decreasing. I verified
`mu(lam_c) <= cm` numerically at `(m, c) in {30, 300} x {1/2, 7/10, 1}` —
all hold (e.g. `mu(log 2, 300) = 297.256 <= 300`); the caps
`1.0987/0.8874/0.6932` are correctly rounded UP in the text (the NC-P4
table's `0.6931` print is a display slip, R8).

### 1.9 Theorem S — the reduction is sound; partition verified gap-free.
- **Partition**: `{1} ∪ [2, K_c] ∪ {k > K_c, |w| > 4} ∪ {k > K_c, |w| <= 4}`
  covers every interior `k <= N/2` (WLOG by exact palindromy); integer
  boundary at `K_c = min(cm, m-1)` checked: `k > K_c => k > cm` in all
  cases (including `c = 1`: `k >= m`), so P.6/P.8's hypotheses hold with
  no boundary slop. `m`-ladder: harness `4..400` (C1–C6 verified on disk),
  `c = 7/10` on `[401, 1581)` (`m_p = 300 <= 401`), `c = 1` on
  `[1581, inf)` (`m_p = 1581`). **No `(m, k)` gap found.**
- **R1a**: Lemma 3.6 at `k = 1` needs `m >= 16` — satisfied; value
  `~ 9 x 10^5` at `m = 401`.
- **R1b**: floor formula `(m-1)^2(2m+5)/(144 c(1+c) m)` re-derived and
  recomputed: `1879.06` at `m = 401` — matches.
- **R2**: `s2 >= 0.1983m >= 79.5` (so `C_0* = 79` is reachable),
  `min(m, s2) >= 79.5` for ALL `m >= 401` (since `0.1983 m >= 79.5` and
  `m > 79.5`), tilt cap `0.8873 <= 0.89`, `20/79.5 = 0.25157 <=
  1 - 1.02 rho(4) = 0.25835`: the CL spec arithmetic closes with true
  margin `1.0293 >= 1.02` (the printed `1.0294` is R2's rounding slip).
  T.8-final/`C = 600`/`C_0 = 2000` genuinely appear nowhere; R2 does not
  overlap T.8-final's `|lam| <= pi/m` scope (`|w| > 4 > pi`) — checked.
- **R3**: the chain `lambda(r-1) >= (1+D)(1 - B_m(1+w^2) - C/m^2)` with
  `D >= 6.85 E(4) w^2` and the `w^2`-bracket discarded only when
  nonnegative — algebra re-derived; bracket positive from `m = 82` (R3
  note), comfortably at `m >= 100` and `m = 401`. Inputs quoted with true
  hypotheses: W.7 at `K = 4`, `m >= 180` (>= 401 ok), `c_w(4) = 1` per
  discharged repair B2; PW-grid caveat (+0.22% beyond `m = 2000`, repair
  B3) carried honestly in marker 2. The `m_2(4) = 379` far-bucket
  threshold is used *as the proxy it is* and flagged twice (§6.3, marker
  2) — acceptable, see R6.
- **Conditionality/circularity**: CL is a named PARAMETER (Prop 3.5(i)
  shape) — a legitimate reduction, prominently labeled, never silently
  assumed; R3's condition is exactly wp2-a's `Delta_ker`. Nothing in
  P.1–P.8 uses any part of Prop 3.5, T.9, or T.8. The two broken T2 items
  (T.10(2), T.8'') are not used — confirmed by grep and by reading the
  chains. **No circularity.**

### 1.10 Citation-status audit (all opened and read).
`referee_t2_maths.md`: exists, VERDICT MINOR_REPAIRS; T.5 "CORRECT,
fully" (§2.6); T.4 partial-fraction kernel verified; T.9'' "fully sound";
T.10(2) FALSE as displayed (repair `rho = 1 - 0.022 w_0^2` — the constant
P.7 improves on, correctly quoted); T.8'' proof broken. All exactly as the
draft represents. `repairs_20260811.md` + `referee_repairs_20260811.md`
(SURVIVES): wp1-c R1–R5 and wp2-b B1–B8 discharged, including B2
(`c_w(4) = 1`) and B3 (PW K=4 grid caveat) — as the draft represents.
`harness_m200_20260811.md`: C1–C6 exact to `m = 400`, scripts present on
disk (`run_m200.py`, `results_m200.txt`) — supports Theorem S's
`m <= 400` row. wp1-c W.5(ii)/W.6, quoted in §6.1 for wp4's scope: the
wp1-c maths referee confirms both "correct as stated" (its R3 concerns
W.5(iii)'s statement range, not the clauses used here). No misquoted
hypothesis found anywhere — in particular no silent `w <= pi`-class scope
assumption (the historical failure this campaign checks for).

---

## 2. Script audit

All four scripts exist, run, and reproduce every quoted number verbatim
(re-run this session; NC-P1 0.24 s, NC-P2 ~1 s, NC-P3 25.2 s, NC-P4
instant). Verdict-path arithmetic in NC-P1/NC-P2 is genuinely exact
(integer cross-multiplication / `Fraction`s); NC-P3/NC-P4 are honestly
labeled measurement. The pentagonal-row generator, the staircase
convolution, the bisection for `lam(k)`, and the `E`-series partial sums
are all correctly implemented (checked line by line). Two honest-labeling
defects: the "certified lower decimals" are printed with `%.8f`
round-to-nearest (R2), and NC-P3(d) scans `k in [2, N/2]`, not "every
interior k" (R5). One number in the draft appears in no script (R3).
NC-P3(d)'s `trueC0 = 0.00` output confirms the draft's "no variance
threshold at all on the tested range" gloss for `k >= 2`.

---

## 3. Attacks attempted and their outcomes

1. **Break the `g >= 5` second-difference bound at boundary `g ~ k`** —
   failed: the shift identities are exact even where `x_g(k-1) = 0` or
   `x_g(k) = 0` (checked algebraically and in exact arithmetic).
2. **Break P.3's floor at `k + 1 = m` or `k = 2`** — failed:
   `x(m) = m/(2m-1) <= 30/59` for `m >= 30`; only the trivial `j = 1`
   range pinhole (R7).
3. **Find an `(m, k)` gap in Theorem S** (integer boundaries at `K_c`,
   the `c`-switch at 1581, the harness/analytic seam at 400/401, the
   `|w| = 4` split, `N` even center) — failed except for one lattice
   pinhole: at `N` even, `k = N/2` has `lam(k) = 0`, formally outside
   W.7's stated `0 < lam(k)` hypothesis (R4; covered by B.8/Cor 2.3, so a
   one-line fix, not a gap).
4. **Find circular use of Prop 3.5 / T.8 / T.9** — none (§1.9).
5. **Refute the P.5 inequality itself by brute force** — failed on an
   independent implementation (0 violations, `m <= 121` exhaustive by me,
   `m <= 200` by the draft's exact script).
6. **Refute P.7 at large `|w|`** (where the proof lapses) — the
   *statement* held at every probe (`w = 8, 20, 60`), but the proof does
   not cover it: R1 stands as a statement-scope repair, not a
   counterexample.
7. **Check every named constant's rounding direction** — caught R2 (four
   unsafe decimals + five downstream echoes); everything else
   (`C_P` roundings, caps, `m_p` ceilings, `6.857`, `811/3481`,
   `0.25157 <= 0.2584`) is rounded the safe way.

---

## 4. Repair list (all statement/text-level; no constant or threshold moves)

- **R1 (moderate; the only mathematical-content item).** Rescope Lemma
  P.7 clause 1 to `|w| <= 8` (or add the explicit condition
  `48 E(w) m^4 >= 1000`): as displayed, the proof's bracket argument does
  not deliver `6.85` for arbitrarily large `|w|` at fixed `m` (e.g.
  `m = 30, |w| >~ 57`). Everything consumed downstream lives at
  `w0 <= 6`. (Same class as wp1-c repair R3: statement/proof range
  alignment.)
- **R2 (rounding directions).** Reprint the `E(w0)` table truncated DOWN
  (`E(1) >= 0.00400692`, `E(2) >= 0.00358718`, `E(3) >= 0.00304035`,
  `E(6) >= 0.00161240`; `E(4)`, `E(5)` are already safe), and propagate:
  `deficit(4) >= 0.2728` (or `0.27289`), `rho(4) <= 0.7272` (or
  `0.72711`), `deficit(2) >= 0.0982`, `rho(2) <= 0.9018`, R2's value
  `>= 1.0292`, note-2's `>= 0.01627`. All downstream inequalities
  re-close with the corrected values (I re-ran the R2 chain:
  `0.7484/0.72711 = 1.02928 >= 1.02`; `0.25157 <= 1 - 1.02*0.72711 =
  0.25835`).
- **R3 (honesty rule + wrong number).** Derivation note 2's "`m >= ~68`
  with it" is from no saved script and is false: the true crossover of
  `6.85E(4)(1 - 17B_m - C/m^2) >= B_m` with exact `B_m` is `m = 82`.
  Replace by "`m = 82` (script-checked)" or drop the parenthetical; the
  row's "valid `m >= 100`" claim is correct and is what Theorem S uses.
- **R4 (one lattice point).** R3's row cites only W.7, whose stated
  hypothesis is `0 < lam(k) <= K/m`; at `N` even, `k = N/2` has
  `lam = 0`. Add the one-line note that the exact center is covered by
  g1_draft_b (Cor B.9 / Cor 2.3, `m >= 180`) or by W.7's untilted limit.
- **R5 (overstatement of a measured claim).** "`eps(k) <= 0.0385` over
  EVERY interior `k`" (§0.2, §6.1.2): NC-P3(d) scans `2 <= k <= N/2`;
  `k = 1` is untested (and by symmetry that is fine for `k >= N/2`).
  Say "every `2 <= k <= N-2`" or extend the scan; irrelevant to the spec
  (which lives at `s2 >= 79`).
- **R6 (labeling).** Theorem S's summary line "no condition other than
  those two named open packages remains" is mildly stronger than §6.3's
  own caveat: the R3 far bucket's `m_2(4) = 379` is a proxy-criterion
  number, so the wp2-a condition implicitly includes "its merged assembly
  lands at threshold `<= 400` (or the harness is extended)". The draft
  says exactly this in §6.3 and marker 2 — mirror that qualifier in the
  Theorem S statement itself.
- **R7 (trivial).** P.4(iii) uses the P.3(ii) floor at `j = 1` (when
  `k = 2`), outside P.3's stated range `2 <= k <= m`; add "and trivially
  at `k = 1`, where `Phi = 1 - 1/m`".
- **R8 (trivial display).** NC-P4's table prints the `c = 1` tilt cap as
  `0.6931` (round-down of `log 2` — wrong direction for a cap; the
  draft's own text correctly uses `0.6932`); likewise Theorem S's R2 row
  could cite `1.0292` per R2 above. Also: the R3 conclusion line
  `[C_R^PT(4) + C_ker + Lin]/m^2` double-counts `Lin` (wp2-b's
  `C_R^PT` already contains it) — safe direction, but say so or drop the
  extra `Lin`.

---

## 5. Referee-script outputs (verbatim key lines)

Independent exact algebra + constants (`ref_wp3a2_check1.py`):

```
(1) x_g(k) = T(k-g)/T(k) product formula: mismatches: 0
(2) Delta^2 x_1 mismatches: 0   Delta^2 x_2 mismatches: 0
(3) Delta^2 x_g (g>=5) display: mismatches: 0
(4) c=1/4: Cd=1.46748 CA=5.92307 CP=12.3359 m_p=ceil(12.56487)
    c=1/2: Cd=1.80531 CA=12.4429 CP=36.165  m_p=ceil(82.37131)
    c=7/10: Cd=2.08225 CA=20.6492 CP=83.6064 m_p=ceil(299.4748)
    c=1:   Cd=2.48038 CA=34.92   CP=263.23  m_p=ceil(1580.382)
(5) E(1) = 0.00400692754113  printed 0.00400693 -> UNSAFE (printed > true)
    E(2) = 0.00358718714373  printed 0.00358719 -> UNSAFE
    E(3) = 0.00304035863603  printed 0.00304036 -> UNSAFE
    E(4) = 0.00248992442455  printed 0.00248992 -> SAFE(lower)
    E(5) = 0.00200652024854  printed 0.00200652 -> SAFE(lower)
    E(6) = 0.00161240672218  printed 0.00161241 -> UNSAFE
    proved deficit floor = 0.27289523 (draft claims >= 0.2729 -> UNSAFE)
    proved rho(4) <= 0.72710477 (draft claims <= 0.7271 -> UNSAFE)
    R2 chain: (1-0.2516)/rho = 1.0292877 (draft: 1.0294)
(6) smallest m with bracket >= 0: 82  (draft note says '~68')
    bracket at m=100: 0.0031678; at m=401: 0.013585
```

Independent ground truth (`ref_wp3a2_check2.py`):

```
(7) P.5 truth, independent generator: m=50: violations=0, min ratio=2.0024
                                      m=121: violations=0, min ratio=2.0004
(8) T.4 Step-2 identity vs exact variances: rel dev <= 3.63e-37 (4 probes)
(9) P.7 floor vs exact deficit at w=4/8/20/60: all OK (true >> floor)
(10) mu(lam_c) <= c*m at (m,c) in {30,300}x{1/2,7/10,1}: all OK
(11) R1b margin at (401, 0.7): 1879.06 (two independent routes agree)
```

Draft scripts re-run: NC-P1/P2/P3/P4 all reproduce the quoted outputs
verbatim (including `trueC0 = 0.00` in NC-P3(d), global min `2.0002` at
`(200, 2)` in NC-P1, and the `C_P` table in NC-P2).

---

## 6. What remains (unchanged by this report; confirmed accurate as drafted)

The draft's own §8 residue list is honest and correct: the deep-tilt core
(wp4, spec'd at `CL(79, 20, 0.89)`) and wp2-a's `Delta_ker` are the only
mathematical conditions of Theorem S; the `m_2(4)` proxy caveat and the
grid-certificate statuses are carried with correct labels; T2 §8 item 2 in
its original arithmetic form is genuinely closed by P.5 + P.6 (the
quadratic-to-linear reduction is real and I verified both ends of the
comparison). Under the house rule this package now carries ONE maths
referee (this report, MINOR_REPAIRS); it still needs its numerics referee.

**Verdict: MINOR_REPAIRS** — apply R1–R8 (one rescoped lemma statement,
one decimal table reprinted in the safe direction, one unscripted-and-wrong
parenthetical, five note-level fixes); every theorem, constant, threshold,
and the entire reduction survive as stated.

*End of report.*
