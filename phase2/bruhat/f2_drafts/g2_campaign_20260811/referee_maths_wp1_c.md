# Adversarial maths referee report — wp1_draft_c (Lemma W chain, tilted far-region bound)

*Referee pass 2026-08-11, blind protocol maintained: only `wp1_draft_c.md`, its
scripts under `g2_scripts/campaign_undefined/wp1_c/`, and the four required
context documents were read; no other campaign draft, no `g2_draft_t1`.
Default-to-refutation stance: every lemma re-derived by hand, every script
re-run, every constant independently recomputed (independent quadrature, not
the draft's closed form), the master bound stress-tested against
direct-weight-sum truth (NOT the draft's own W.1 factorization) at 4500+
adversarial cases off the draft's grids. Referee scripts (run 2026-08-11,
CPython 3, mpmath): session scratchpad `ref_wp1c_indep.py` plus inline checks;
key outputs quoted below.*

## VERDICT: MINOR_REPAIRS

**Every load-bearing mathematical claim survives.** Lemmas W.1–W.3,
Corollaries W.4–W.5, and Clause W.6 are correct as stated (one statement/proof
range mismatch in W.5(iii), in the safe direction), the proofs are genuinely
elementary and self-contained, no circularity exists, the historical failure
mode (silently assumed `w <= pi`) is absent — the master lemma is
unconditional in `lam` and every scope restriction downstream is an explicit
hypothesis used exactly where stated. All five verification scripts exist,
run, and reproduce the quoted outputs exactly. The repairs needed are
text-level: one false numeric side-claim about rounding margins, one wrong
digit in a non-load-bearing aside, one statement/proof alignment, one
missing one-line proof behind a "no grid certificates" claim. List in §4.

---

## 1. What was verified and how

### 1.1 Hand re-derivation of every proof (all correct)

**W.1 (exact modulus factorization).** Recomputed:
`|1 - e^{-(a+ib)}|^2 = 1 - 2e^{-a}cos b + e^{-2a} = (1-e^{-a})^2 + 4e^{-a}sin^2(b/2)`,
and `(1-e^{-a})^2 = 4e^{-a}sinh^2(a/2)` — hence
`|1-e^{-(a+ib)}|^2 = 4e^{-a}[sinh^2(a/2)+sin^2(b/2)]`. Applied to
`nu_j = z_j(lam - it)/z_j(lam)` top and bottom, all `e^{-lam}`-prefactors
cancel exactly; the `j = 1` factor is 1; the `lam -> 0` limit is the Dirichlet
factor. **Correct.** (Also confirmed: `|phi_lam|` even and `2pi`-periodic in
`t`, even in `lam` — the WLOG is sound.)

**W.2 (envelope).** Both induction inequalities checked
(`|sin((j+1)v)| <= |sin jv| + |sin v|`; `sinh((j+1)u) >= sinh(ju) + sinh(u)`
by `cosh >= 1`, nonneg. terms; evenness gives `S_j >= j^2 S` for all real
`lam`). The algebra `[S/(S+s)](1 + min(1, j^2 s)/(j^2 S)) =
(S + min(1/j^2, s))/(S+s)` checks. The `lam = 0` case handled separately
(direct Dirichlet bound), so no 0·∞ issue. **Correct.** The remark that at
`lam = 0` the envelope dominates the SQUARE of Lemma 1.4's envelope also
checks (`s >= (t/pi)^2` gives `1/(j^2 s) <= (pi/(jt))^2`).

**W.3 (master bound).** The chain: envelope → `j`-th term `= f(jh)` with
`f(u) = log[(1+r)u^2/(ru^2+1)]` on `u >= 1`, `f = 0` below (continuous at
`u = 1` since `f(1) = 0`); `f' = 2/[u(ru^2+1)] > 0` (recomputed) so `f`
nondecreasing; `f(jh) >= (1/h)∫_{(j-1)h}^{jh} f`; the intervals for
`j = 2..m` tile `[h, mh]` and `f = 0` on `[h, 1]` (`h <= 1` always). Hence
`-log|phi| >= I(M,r)/(2h) = m q(M,r)`. **Correct, and unconditional in
`lam`** — this is the structural point that kills the historical `w <= pi`
failure mode at the master-lemma level.

*Closed form:* re-derived independently:
`∫ log(ru^2+1) du = u log(ru^2+1) - 2u + (2/sqrt r)arctan(sqrt r u)`;
assembling over `[1, M]` the constant terms cancel and the displayed `I(M,r)`
results; `r = 0` limit `2(M log M - M + 1)`. **Correct.** Also verified
independently by numerical quadrature (referee script, dps 60): closed form
vs quadrature agree to `< 4e-62` at every named-constant argument, and to
`5.35e-33` on a 7×7 `(M,r)` grid at dps 40.

*Monotonicity (i):* `(d/dM)[I/(2M)] = [M f(M) - I]/(2M^2) >= 0` via
`I <= (M-1)f(M)`; `∂f/∂r = (1-u^2)/[(1+r)(ru^2+1)] <= 0` for `u >= 1`.
**Correct.**

*(W.3d):* `f(u) = log(1+1/r) - log(1+1/(ru^2)) >= log(1+1/r) - 1/(ru^2)`,
integrate; `(1/(2M))(1/r)(1-1/M) = ((M-1)/(2M))·(1/(rM))`. **Correct**
(this is also Clause W.6 verbatim).

*The `q(2,0) = log 2 - 1/2` corner:* exact —
`I(2,0)/4 = (4 log 2 - 2)/4 = log 2 - 1/2 = 0.19314...`, precisely Lemma
1.4's constant. Verified symbolically and at dps 50 (deviation 0.0).

**W.4 (small tilt).** Chain (a)–(e) re-verified line by line:
(a) `sin x/x` decreasing on `(0, pi/2]` (proved in the text via `tan x > x`),
so `m sin(c/m)` increasing; floors `30 sin(sqrt2 pi/60) = 2.219411 >= 2.2194`
and `30 sin(pi/30) = 3.135853 >= 3.1358` (referee-recomputed, dps 50).
(b) `2.2194^2 = 4.92574 >= 4.9257`, `3.1358^2 = 9.83324 >= 9.8332` — verified
in EXACT rational arithmetic (referee script part (2)).
(c) `sinh x <= x cosh x` (proved in text); `cosh^2(1/8) <= 1.0157066`
re-certified by the referee in exact rationals (Taylor with explicit tail
bound: exact upper bound 1.01570654994 <= 1.0157066); needs
`|lam|/2 <= 1/8`, i.e. the explicit hypothesis `K <= m/4` — used, stated.
(d) `0.253927/4.9257 = 0.0515514... <= 0.05156` and
`0.253927/9.8332 = 0.0258234... <= 0.02583` — verified in exact rationals.
(e) corner monotonicity: `q(M(t), r(t)) >= q(M_min, r_max)` valid since `q`
monotone in each argument separately. **Correct.**

**W.5 (deep tilt).** (i): on `t >= t_rho(lam)`, `r <= rho` and `M >= M_rho`
by definition of `arcsin`; hypothesis `sinh(|lam|/2) <= sqrt rho` makes
`t_rho` well-defined; nonvacuity condition `M_rho > 1` stated. **Correct.**
(ii): floor `M_1 = m sinh(|lam|/2) >= m|lam|/2 >= pi/2` via `sinh x >= x`,
`|lam| >= pi/m`; `q(pi/2, 1) = 0.0373606...` (referee-recomputed);
large-`M` limit of `q(M,1)` is `(1/2)log 2` (re-derived from the closed
form). **Correct.** (iii): case 1 (`|lam| <= pi/m`, `t >= pi/m`):
`M >= 30 sin(pi/60) = 1.570078 >= 1.5700`;
`r <= [sinh(pi/60)/sin(pi/60)]^2 = 1.0018293 <= 1.00183`; case 2 reduces to
(ii) plus `q(pi/2, 1) >= q(1.5700, 1.00183) = 0.0372513 >= 0.0372`
(corner monotonicity — both arguments move the right way). `t_0(lam) >= lam`
via `arcsin x >= x`, `sinh u >= u`. **Correct** (but see repair R3: the
STATEMENT's `t`-range is `[max(pi/m, t_0(lam)), pi]` while case 1 of the
proof establishes the larger range `[pi/m, pi]` for all `|lam| <= pi/m`,
which is what §6's coverage table row 3 quotes).

**W.6.** Is (W.3d) re-read; the geometric-limit interpretation checks:
`|cf(Geom(e^{-lam}))|^2 = S/(S+s)` (recomputed), `Var = 1/(4S)`,
`(1/2)log(1+s/S) ~ t^2/(8S) = Var·t^2/2`. **Correct.**

### 1.2 Scripts: all real, all re-run, all outputs match

All five scripts exist at the stated path and were re-run by the referee
(2026-08-11). Every quoted number in the draft's §7 table and §8 tables
reproduces exactly: NC-W1 (5.94e-40 / 5.84e-32 / +8.36e-8), NC-W2 (3.76e-14;
global max ratio 0.988902 at m=100, lam=2.5, t=pi), NC-W3 (all certificates
True; c_1(1) = 0.225989909281, c_1(4) = 0.101983937137, c_V = 0.0372513232987,
`|q(2,0)-(log2-1/2)| = 0.0`), NC-W4 (143/190/267/379; old 7338/66010/593181/
5076022; (V): 1065849/292672 old, 879/185 new; g1: 180 old, 60 new), NC-W5
(slack table incl. m=40 untilted max 1.141e-16 vs ledger NC-5's 1.1e-16;
W.6 min ratio 1.0182). No fabricated PASS anywhere — a first for this
campaign's unrefereed drafts.

### 1.3 Independent adversarial attack on the master bound (the kill attempt)

The draft's own NC-W2(b) computes "truth" via the W.1 factorization — if W.1
were wrong that check would be circular. The referee therefore recomputed
`-log|phi_lam(t)|` DIRECTLY from the per-factor weight sums
(`nu_j = sum_i e^{(it-lam)i} / sum_i e^{-lam i}`, mpmath dps 30–50) and
attacked the bound at corners the draft's grids do not cover:

- `m in {2, 3, 5, 12, 30, 100}` × `lam in {0, ±0.001, ±0.1, ±0.5, ±2, 5, 10,
  pi/m, 4/m}` × `t` including `M = 1+eps` boundary points, `t = pi`,
  resonances `2pi k/j ± 1e-5`: **1820 cases, max bound/truth = 0.98999 <= 1.**
- off-grid sweep `m in {31, 47, 150, 400, 1000}`, `lam` including negative,
  `1.7627`, `2.0`, `3.5`, `6.0`, random + boundary `t`: **2690 cases, max
  ratio 0.9989967 (at m=1000, lam=6, t=pi) <= 1.**
- the reported global worst corner (m=100, lam=2.5, t=pi) recomputed at dps
  50 from direct weight sums: `-log|phi| = 16.28837`, `m q = 16.10760`,
  ratio 0.98890 — confirms the draft's 0.988902 exactly.

The bound survived every attempt, including deep tilts (`lam = 6, 10`) far
beyond any clause's scope — consistent with W.3's claimed unconditional
validity. The discrete-sum-vs-integral step was also checked directly
(300 random `(m, lam, t)`: min margin +2.7e-5 >= 0).

### 1.4 Corner floors and constants, independently

For every claimed constant, the referee re-verified the corner logic by brute
force: min over 600-point `t`-grids of `q(M(t), r(t))` at `lam = K/m` (the
worst tilt) for `m in {30, 31, 45, 100, 400}`, all `K in {1,2,3,4,pi}` on
`[t_1, pi]` and `K in {0,1,2,4}` on `[2pi/m, pi]`, plus the W.5(iii) floor at
`m in {30, 60, 200}` across sub-`pi/m` and deep tilts: **every floor holds.**
All named constants recomputed via independent quadrature at dps 60: every
quoted value is a valid rounded-DOWN bound (margins all positive; see R1 for
the margin-size claim). Thresholds independently recomputed with
referee-written loops: **143/190/267/379 exact match**, old-criterion
reproductions exact match (7338/66010/5076022), (V) numbers and the g1
far-arc numbers exact match.

### 1.5 Circularity and citation audit

- Nothing in W.1–W.6 assumes any part of Prop 3.5 (G2's target) or any T2
  §8 OPEN item. The chain's only external inputs are: Lemma T.2's weight
  formula (PROVED in T2; and W.1's proof is in fact self-contained given the
  geometric-sum identity), the T.6(i) identity (PROVED; W.1 is its modulus
  form, reproved from scratch), and B.0(i) (PROVED in g1b) — used only
  inside the threshold *reporting*, which the draft explicitly labels
  "reported facts under the standing criterion, not new theorems".
- Cited prior lemmas are quoted with true hypotheses and scope: T.7b-final
  correctly described as scope `lam <= pi/m` with exponent `m_*/4730`;
  T.7c correctly `|w| <= K` with `0.06 e^{-2K}`; Lemma 1.4 correctly
  `2e^{-0.19314 m}` on `[2pi/m, pi]`; T.9'' correctly `|t| <= t_1` uniform
  in `lam`. The diagnostic's findings (no `exp(-c m)` possible at `t = pi/m`
  for fixed `lam`) are correctly used as motivation for the `t_0(lam)`-moving
  range, not as proof input.
- The `(t, lam)` coverage table (§6) was checked row by row against the
  proved clauses: each row is backed (row 3 by W.5(iii)'s proof case 1 —
  see R3). The T.9 handoff has genuinely no gap: core `|t| <= t_1` (T.9'')
  and far `[t_1, pi]` (W.4(i)) share the split point `t_1`.
- The draft does NOT claim T.9 or T.8 is now closed; §9 items 1–2 correctly
  state that the bucket-table assembly (T2 §8 item 4) and the deep-tilt core
  model remain open. Honest scoping throughout.

---

## 2. Assessment of the contribution

The master lemma is a real improvement in kind, not just in constants: a
single elementary bound, unconditional in the tilt, from which the untilted
Lemma 1.4 (`q(2,0) = log 2 - 1/2`, exactly), the small-tilt clauses (28x to
5067x better than T.7c's proved exponents), the previously-nonexistent
deep-tilt bound (in the `t_0(lam)`-moving form the diagnostic proved
necessary), and the crossover clause (within 2% of truth pointwise on the
tested zone) all fall out as corner evaluations. The grid-certified Dirichlet
inequalities (T.7b-cert), (T.7c-cert) are indeed superseded on every range
the campaign consumes. Measured sharpness (55–76% of the true exponent
captured) is credible and honestly reported. This closes T2 §8 item 5 and
the far-region half of item 1 as claimed.

---

## 3. Kill attempts that failed (for the record)

1. Master bound false somewhere? — 4510 adversarial cases from
   direct-weight-sum truth, incl. m=2, lam=±2..10, resonances, M→1+: no
   violation (max ratio 0.999).
2. Circular verification (truth via W.1 in NC-W2)? — W.1 independently
   confirmed per-factor (dps 40) and whole-product vs exact tilted Mahonian
   sum at m=12; referee reconfirmed with direct sums at m up to 1000.
3. Corner-floor logic broken at some interior t or non-tabulated m? — floors
   re-verified by brute force at m ∈ {30, 31, 45, 100, 400} for all clauses.
4. Rounding in the wrong direction? — all named constants recomputed at dps
   60 by independent quadrature: all quoted values round DOWN (safe).
   (But the margin-size claim is wrong — R1.)
5. Silent `w <= pi`-type scope assumption (the historical failure)? — W.3
   unconditional; W.4's `K <= m/4` explicit and used exactly at step (c);
   W.5's `sinh(|lam|/2) <= sqrt rho` explicit; no hidden scope anywhere.
6. Threshold numbers fabricated or criterion quietly changed? — criterion
   reproduces T2's old numbers exactly (7338 vs "~7.3e3" etc.) and g1's
   m_1 = 180; new numbers independently recomputed, exact match.

---

## 4. Required repairs (all minor; none touches a proof or constant)

**R1 (false numeric side-claim — the one real honesty defect).** §9 item 3
claims the named constants were "rounded in the safe direction with margin
`>= 5e-5`". FALSE for six of the thirteen named constants: the actual
margins are `c_1(0)`: 9.1e-6, `c_1(3)`: 2.4e-5, `c_1(6)`: 1.3e-5,
`c_1(pi)`: 4.4e-5, `c_1'(2)`: 1.5e-5, `c_1'(4)`: 1.8e-5 (referee
quadrature, dps 60; minimum 9.1e-6 at `c_1(0)`). Every rounding IS in the
safe direction and every margin is still ~35 orders above the evaluation
error, so no constant changes — but the stated margin bound must be
corrected (e.g. to "margin `>= 9e-6`, eleven orders above evaluation
error").

**R2 (wrong digit in an aside).** §5 "Beyond `|lam| = 1.7627`":
`2 asinh(sqrt 10) = 3.7371...`, not "3.7358". Non-load-bearing (the
rho-family statement itself is correct); fix the digit.

**R3 (statement/proof range alignment in W.5(iii)).** The statement's range
`t in [max(pi/m, t_0(lam)), pi]` is SMALLER than what its proof establishes:
case 1 proves the bound on all of `[pi/m, pi]` for every `|lam| <= pi/m`
(including the sliver `[pi/m, t_0(lam)]` when `t_0(lam) > pi/m`, which
happens for `lam` within `O(1/m^3)` of `pi/m` — e.g. m=30, lam=pi/m:
t_0 = 0.104816 > pi/m = 0.104720). §6's coverage row 3 and the "supersedes
T.7b-final on its whole scope" claim rely on the proof's range, which is
fine — but restate (iii) case-wise (`[pi/m, pi]` for `|lam| <= pi/m`;
`[t_0(lam), pi]` for `pi/m <= |lam| <= 1.7627`) so statement and use match.

**R4 (one grid-certified monotonicity vs the "no grid certificates" claim).**
`sinh(x)/sin(x)` increasing on `(0, pi/2)` (used for `r_V <= 1.00183` in
W.5(iii) case 1) is asserted and certified only by NC-W3's grid — which
contradicts §0's "no grid-certified inequality appears anywhere". The fix is
one line: `(cosh x sin x - sinh x cos x)' = 2 sinh x sin x > 0` and the
expression vanishes at 0, i.e. `tan x > tanh x` on `(0, pi/2)`
(referee-verified). Add it and the "no grids" claim becomes true.

**R5 (wording).** (a) "Supersedes Lemma T.7c everywhere": W.4 carries the
extra hypothesis `K <= m/4` that T.7c did not have; for `K > m/4` T.7c's
statement (vacuous in practice, `exp(-0.06e^{-2K}m) ≈ 1`) is not literally
covered. Say "supersedes T.7c in every downstream use (fixed K, m >= 30)"
or add the rho-family pointer for the complement. (b) NC-W4(b)'s
"reproduced: 292672" for T2's "~2.5e5": same order, not a reproduction —
say "same convention recomputed: 2.9e5 (T2 quoted ~2.5e5; discrepancy in
T2's own loop, not material since both old numbers are catastrophic)".

---

## 5. Verdict justification

Load-bearing content — the master lemma, its four corner corollaries, all
thirteen named constants, the coverage map, and the threshold restorations —
survived hand re-derivation, exact-rational re-certification of the
inequality chain, independent recomputation of every constant, and 4500+
adversarial numerical attacks with independently computed truth. The five
repairs are text-level and none alters a stated constant, hypothesis, or
conclusion. Under this campaign's scale that is **MINOR_REPAIRS** (the same
grade g1_draft_b carried into citable status); with R1–R5 applied this
draft is citable as the campaign's far-region foundation: T2 §8 item 5
closed, item 1's far-region half closed, items 1-core and 4 open exactly as
the draft itself states.

*End of referee report. Referee scripts: session scratchpad
`ref_wp1c_indep.py` (independent quadrature constants + exact-rational
certificates + direct-weight-sum adversarial sweeps + threshold loops);
outputs quoted verbatim in §1.2–§1.4 and §4.*
