# referee_maths_wave4_sl3p — adversarial MATHS referee report on `wave4_sl3p_20260812.md`

*Wave-4 referee (maths half, house rule), F2 campaign, 2026-08-12. Target:
`wave4_sl3p_20260812.md` (Stage-2 finisher: Theorem SL3', the banded
mid-exponent upgrade `gamma* = 0.42/0.42/0.40/0.40/0.38/0.34/0.32`). Also
read in full: `wave4_sl3p_ROUTE_20260812.md` (Stage 1 — its Lemmas E.1/E.2/
E.3 are load-bearing for Stage 2 and were re-derived by hand here), all six
scripts + archived outputs under `g2_scripts/campaign_20260811/wave4_sl3p/`,
`wp4_draft_composite.md` (the citation substrate and the §5.3 SL3' spec),
`referee_maths_wp4.md` + `referee_numerics_wp4.md` (corrected budgets),
`STATUS_wave3.md`. `g2_draft_t1_20260803.md` not read (house rule); no other
wave-4 bridge draft read (referee independence on the blind pieces). Default
posture: REFUTATION — this chain feeds the flip of the paper's main
conjecture to a theorem. My own checks: every script re-run and diffed
against its archive; every analytic lemma re-derived by hand; independent
dps-30 re-derivation of every named constant, every band threshold, and
every printed worst cell; a 162-point direct-summation truth attack that
shares no code and no identity with the draft's route. Referee scripts
(SAVED and RUN 2026-08-12, outputs archived beside them) in
`referee_maths_wave4_sl3p_scripts/`: `ref_msl3p_a_constants.py`
(`out_ref_msl3p_a.txt`, addendum `out_ref_msl3p_a2.txt`),
`ref_msl3p_b_truth.py` (`out_ref_msl3p_b.txt`), edge audit
(`out_ref_msl3p_c_edges.txt`). No existing file modified; this file is new.*

## Verdict: **MINOR_REPAIRS**

**on the draft's claim AS STATED** — Theorem SL3' PROVED modulo the finite
monotone-cell certificates E.5.3 / E.6.A/B/C, explicitly flagged as the
campaign's accepted grid-certificate class (float64 corner evaluations of
closed-form monotone cell bounds). After adversarial checking I confirm:
every analytic step (E.4a, E.4b, E.5.1, E.5.2, E.6a, E.6c, the §6 assembly)
is a correct, complete proof with correct explicit constants; every
certificate cell bound has rigorous inequality directions; every printed
number I traced exists verbatim in an archived output that re-runs
byte-identically; every named constant survives independent dps-30
re-derivation; the certificates' worst cells recompute independently to the
printed values and sit strictly below true `delta_norm`; and the theorem's
truth survives a 162-point direct attack (independent computational path,
zero violations, worst ratio 1.0592 exactly at the route's predicted W5
point). The interfaces to the composite (band geometry, the SL2 variance
identity, the §5.3 `gamma*` targets, the untouched `c2` tier) are
verbatim-true, and there is no circularity with Prop 3.5 content. The
repairs (§2) are wording/honest-register level; the one with quantitative
content is R1: the headline "worst headroom 7.96x" is the CELL-part margin
only — the certified margin at the analytic/cell crossover `tau_start` is
as thin as **1.30x** (W7), and that, not 7.96x, is the number a downstream
consumer must budget off. Nothing found moves a constant, a band, a
PASS/FAIL, or the flagged-class status.

## 1. What I verified, layer by layer

### 1.1 Stage-1 inheritance (E.1, E.2, E.3) — re-derived by hand: CORRECT

Stage 2 stands on the route file's three lemmas, so I re-proved all three.
**E.1**: `nu_j(t) = [(1-q)/(1-q^j)] (1-(qe^{it})^j)/(1-qe^{it})` (finite
geometric sum); `|1-re^{is}|^2 = (1-r)^2 + 4r sin^2(s/2)` and
`4r/(1-r)^2 = 1/sinh^2(log(1/r)/2)` — both identities re-derived; the
quotient collapses to `|nu_j|^2 = [1+sin^2(jt/2)/sinh^2(jlam/2)]/[1+
sin^2(t/2)/sinh^2(lam/2)]`, so `-2log|phi| = m g(lam,t) - sum_j g(jlam,jt)`.
Valid for `q > 1` (i.e. `lam < 0`) as well since all factors are even in the
first slot — the WLOG is sound, and centering does not affect `|phi|`.
**E.2**: `lam^2 Var(U_j) = h(lam) - h(jlam)` re-derived from
`Var = d^2/dlam^2 log Z_j` (`Z_j = (1-e^{-jlam})/(1-e^{-lam})`), summed;
subtracting termwise gives exactly `-2log|phi| - 2 gamma* s2 t^2 =
sum_j [F(lam) - F(jlam)]`, and the equivalence with the band statement is
immediate. The identity is also cited via the composite's Theorem A2
mechanism line (`v = 1 - h`) — citation verbatim-true, and E.1's own
`t^2`-coefficient reproduces it, so the dependence is doubly grounded.
**E.3**: the `u cot u <= 1 < v coth v` argument re-derived; strict on
`(0, 2pi/tau)`.

### 1.2 Lemma E.4a (discretization) — CORRECT, sharper than the route's plan

Re-derived in full. g-part: E.3 makes the left-Riemann comparison valid on
grid points `jlam <= X = 2pi/tau`; extension of the integral to `w` uses
`g >= 0` (legitimate). Beyond-arch: `jlam > X >= 2.5pi > 2pi` so L-env
applies (`(1-e^{-y})^{-2}` decreasing — checked; `C_env` true value
`4.014981 <= 4.04`, my dps-30); the geometric-sum bound
`e^{-X}/(1-e^{-lam})`, `1/(1-e^{-lam}) <= 1/lam + 1` (from
`e^{lam} >= 1+lam`), and `4.04(1/4 + 1/401) = 1.020075 <= 1.03` — all
re-derived (the draft prints the intermediate as `1.0202`, an up-rounding,
safe direction: R5). h-part: right-Riemann for decreasing `h`, the boundary
term is exactly `h <= 1` on one cell of length `lam` — giving the exact
`+2 gamma* tau^2` and no variation constant. The claimed validity range
(`gamma* in [0.32, 0.42]`, `m >= 401`, `w > 4`, `tau <= 4/5`) is exactly
what the proof uses (`1/lam <= m/4` needs `w > 4`; `1 <= m/401` needs
`m >= 401`). I additionally checked the DISPLAY itself directly (script B):
at `(m, lam, gamma) = (401, 0.3, 0.32)`, `(401, 5/401, 0.42)`,
`(500, 0.1, 0.38)`, `tau = 0.8`: `sum_j F(jlam) <=` RHS holds with visible
slack each time. The replacement of the route's `V' = 0.5` proposal by this
split is real and is an improvement, as the draft says.

### 1.3 Lemma E.4b (left-edge Taylor) — CORRECT

Re-derived: `psi(lam) = tau^2 S(u) H(v)` with `u^2 = tau^2 v^2` (exact);
`log((1+tau^2)/(1+psi)) <= tau^2(1-SH) <= tau^2[(1-S)+(1-H)]`; the three
series facts: `1 - S <= u^2/3` is exact (alternating series, term ratio
`4u^2/((2k+1)(2k+2)) < 1` — checked); `sinh^2 v - v^2 <= 1.01 v^4/3` and
`1-H >= 0.99 v^2/3` on `v <= 0.15` are grid-certified (script A c1/c2) but
also PROVABLE: `sinh^2 v - v^2 = (v^4/3)(1 + (2/15)v^2 + ...)` gives true
factor `<= 1.0031` at `v = 0.15`, and `1-H >= (v^2/3)H(v) >=
(v^2/3)(0.9925)` — I verified both series arguments by hand, so the two
grid constants are not load-bearing beyond the flagged class. Assembling:
`K1'(g*) = (1.65 - 1.98 g*)/12`, values `0.0682–0.0847` re-derived for all
five `gamma*`. Off-grid corner spot (`lam = 0.3, tau = 0.8`, dps 30): max
ratio `0.35416 <= 1` (script A [2]) — consistent with the draft's honesty
note that the constant is ~3x conservative. *(Note: the c1/c2 grid
endpoints `0.999645` and `1.000021` are small-`v` float64 cancellation
artifacts in the UNUSED directions; the used directions have real margins
attained at `v = 0.15`.)*

### 1.4 Lemmas E.5.1 / E.5.2 — CORRECT

**E.5.1**: `(d/dw) avg_f = (f(w) - avg_f)/w` — checked. Case A by E.3.
Case B re-derived completely: `S >= 4/pi^2` on the first half-arch (chord
bound), `g >= psi/(1+tau^2)`, `Int_0^{pi/tau} h >= I_h = 2.7` (my dps-30
quad: `Int_0^{pi/0.8} h = 2.78402579896`, so the script's right-sum
`2.784022` is indeed a valid lower bound and `2.7` is safe);
`c_B' tau^2/w > c_B/w^3` uses `tau > 2pi/w` (the Case-B hypothesis) —
correct; `c_B = 26.341463` and `4.04(2pi)^3 e^{-2pi} = 1.8714 < c_B`
re-derived; `w^3 e^{-w}` decreasing for `w > 3` — correct. **E.5.2**:
`log(1+u) >= u/(1+u)` with `u = (tau^2 - psi)/(1+psi)` collapses to
`(tau^2-psi)/(1+tau^2)` EXACTLY (nice step, verified), then `psi <= tau^2 h`
(L2, itself re-derived: `psi = tau^2 h S` exactly). The sign subtlety at
large `tau` (the bracket `1/(1+tau^2) - 2 gamma*` can go negative above
`tau_c'`) is correctly managed: the analytic bound is only ever invoked for
`tau <= tau_start < tau_c'`, where the bracket is positive and decreasing —
I checked the per-band assert values by hand (ana(tau_start): W1 0.003901,
W7 0.012768, all `>= b`).

### 1.5 Certificate E.5.3 — construction audited at source level; independently recomputed

Every inequality direction in `sl3p_s2b_e5cert.py` verified against the
maths: `q(W) = 1 - Ah_ub(w_bot)` (left-Riemann UPPER on decreasing `h` —
correct safe direction; my dps-30 `q_true` sits above every printed `q`,
e.g. W1 `0.29825 <= 0.2983334`, W7 `0.91774 <= 0.9177533`); numerator at
the cell's `w`-bottom via E.5.1 with `log(1+t1^2)` (lower end of the
`tau`-cell) and the decreasing majorant `g_ub(.; t2)` (upper end) — the
majorant's three-piece definition is valid (`sin^2` increasing on
`[0, pi/2]` for the first arch; `min(t2^2 h, 1/sinh^2)` globally valid
beyond; junction continuous with no upward jump, so the left-Riemann sum is
a genuine upper sum); positivity asserted before dividing by
`t2^2 >= tau^2`; subtracted term at the cell's `w`-top with the
right-Riemann LOWER sum on `h` (correct direction); W7's single unbounded
cell uses `1 - avg_h <= 1` (correct). Budget `b(W) = K1' lam_max^2 +
eps_hat + 2 gamma*/401`: all seven values re-derived by hand and at dps 30
(match to all printed digits); `eps_hat`: `1.03 e^{-2.5pi}/0.64 =
6.2476e-4 <= 6.25e-4` and the monotonicity of `e^{-2pi/tau}/tau^2`
re-derived (`(2/tau)(pi/tau - 1) > 0`). `tau_c'` formula re-derived and all
seven values reproduced; `lam_max(W) = w_top/401` vs the E.4b scope
`lam <= 0.3`: W6b's `40/401 = 0.09975` and W7's `0.30` both inside.
**Worst cells recomputed independently** (script A [4] + addendum): my
true-integral version of each band's printed worst cell reproduces the
printed `min delta_cert` from above (the script's Riemann version is
correctly the conservative one), e.g. W1 `0.0362143` vs printed `0.036055`,
W7 `0.078405` vs printed `0.078395`; and TRUE `delta_norm` at each worst
cell sits strictly above (W1 `0.04682`, W4 `0.03572`, W7 at
`(40, 0.7975)` `0.13635`). Coverage: `w`-cells hit the band tops exactly
(float check); `tau`-cells start exactly at `tau_start` where the analytic
bound is asserted (overlap, no gap); see R4 for the ~1e-14 top-edge float
sliver.

### 1.6 E.6a / E.6c and Certificates E.6.A/B/C — CORRECT

**E.6a** re-derived line by line: `C` forces `D_0 >= h(lam)tau_0^2lam^2/12`
(factor `1-2gamma(1+tau_0^2) = 0.14470 in (0,1)` — checked);
`S(u) >= 1-u^2/3` exact for `u <= 1` (hypothesis `tau_0 lam <= 2` gives
`u <= 1`; at the operating corner `0.58 x 0.89/2 = 0.258`); the MVT step
with both arguments in `[0, tau^2]` (L2) — correct; the final
`tau`-monotonization (LHS coefficient decreasing, RHS increasing in `tau`)
— correct. **E.6.A** cell directions (`h(l2)-h(2l1)` below, `h(l1) l2^2`
above) — correct; worst cell `[0.8875, 0.89]` recomputed at dps 30:
`lhs/rhs = 1.12943` (printed 1.1294), and the pointwise margin at
`lam = 0.89` is `1.13742` (matches script A(i)'s 1.1374) — the cell loss is
visible and small. **E.6.B**: all six corner-bound directions re-derived
(`sin^2` monotone below `t2 l2/2 <= 0.356 < pi/2`; E.3 pins the `x`-slot at
`x1` because `7.85 < 2pi/0.8 = 7.853982` — margin `0.00398`, checked; `h`
directions correct; `sin2max` is the exact interval max). Worst cell
`(0.30, 0.58)` fully recomputed at dps 30 over its entire x-sweep: slack
`0.00144803` (printed `0.001448`), max at `x1 = 0.6` — reproduced.
Coverage: `lam`-edges strictly increasing, 1191 rows, last edge
`>= 0.89` (audited; the segment join at `0.40` creates one sliver-thin but
valid cell, NOT a reversal); x-cells reach `7.85` exactly. **E.6c**
re-derived: both cases correct; `eps_t = 1.560224e-3` (dps 30), and the
floor comparison `0.066061/eps_t = 42.3x` reproduces. The three parts
compose with no `(tau, x)` gap: E.6a covers ALL `x >= 2lam` for
`tau <= 0.58`; B covers `x <= 7.85`, C covers `x > 7.85` for
`tau in [0.58, 0.8]` (floor over exactly the part-B cells — correct
quantifier).

### 1.7 §6 assembly — algebra re-derived, regime split airtight

The chain `M >= m tau^2 [delta_norm - K1' lam^2 - eps_env/tau^2 -
2 gamma*/m] >= m tau^2 [delta_norm - b(W)] >= 0` re-derived symbolically
(the identity `m[F(0) - avg_F] = m tau^2 delta_norm` is exact). Regime
coverage: W1–W6b have `lam <= 40/401 < 0.3` always (`m >= 401`); W7 splits
at `lam_split = 0.30` with both regimes covering the boundary; the
large-lam regime is termwise for ANY `m` (the `j = 1` summand vanishes
identically); the small-lam W7 cell `[40, infty)` covers every
`w = m lam > 40`. Evenness/WLOG carried by E.1 (§1.1). The scope decision
(keep all of `(0, 0.8 lam]`) is correctly grounded: E.5.2 (averaged
regime) and E.6a (termwise regime) are analytic at the `tau -> 0` end.
The claimed consumer interface is verbatim-true: delivered `gamma*` equals
composite §5.3's target list symbol-for-symbol; the consumed interval
`[lam/2, 0.8 lam]` is a strict subset of the delivered `(0, 0.8 lam]`; the
`c2` crossover tier is correctly left with Theorem A3 (whose two-tier
statement I re-checked against composite §1). Route-file E.7 numbers quoted
in §6 (`0.008935` / `101.5` / `2.7e-6` / `5.2e-8`, REF-C C7's `101.41`)
all exist verbatim in `out_sl3p_nc3.txt` / `referee_numerics_wp4.md`.
`10.081 <= 136` is quoted in the maths-referee-repaired form (R2 of
`referee_maths_wp4.md`) — good.

### 1.8 Circularity — NONE

The full chain consumes: the tilt frame and band geometry (composite §0),
the SL2 variance identity (elementary, proved, two-referee), and elementary
analysis of `sin/sinh`. No `r(k)`, no Prop 3.5(i)/(ii), no Theorem A
content, no T.9/T.10 machinery, no other wave-4 bridge piece. `gamma = 1/8`
is not re-litigated (REF-C C7 correctly cited for that).

### 1.9 Truth attack (mine, independent path) — 0 violations in 162 checks

`ref_msl3p_b_truth.py` computes `|phi_lam(t)|` by DIRECT termwise summation
of every factor's finite series (numpy complex128; mpmath dps-25 spot) and
`s2` by direct probability-mass summation — no E.1, no closed forms shared
with the draft. Attacked: band edges on both sides (`w = 4.0001, 5.0,
5.0001, ..., 40.0001`), the `w -> 4+` and `lam = 0.89` corners, `m in
{401, 402, 1000}`, `tau in {0.05, 0.2, 0.415, 0.4175, 0.5, 0.58, 0.7275,
0.7975, 0.8}` (including both analytic/cell crossovers, which no draft
grid distinguishes). Verbatim:

```
all 162 (m,w,tau) checks PASS: True
worst ratio -2log|phi| / 2 gamma* s2 t^2 = 1.0592 at (m,w,tau)=(401, 20.0, 0.8)
[mp] -2log|phi|(401, w=4.05, tau=0.8) = 76.8524292638   (NC1 archived: 76.8524292638)
```

The worst measured margin (5.92%, W5 top edge) lands exactly where the
route file said it would, and my independent 12-digit reproduction of NC1's
probe confirms the identity route against direct computation.

## 2. Findings and repairs (all text-level; no constant, band, threshold, or verdict moves)

**R1 (headroom headline — the one substantive finding).** The Bottom line
and §8 say "All certificates PASS with worst headroom **7.96x** (E.5.3,
W7)". That is the worst margin of the CELL part only. The E.5.3 certificate
also relies, for every `tau <= tau_start(W)`, on the E.5.2 analytic floor
`q(W)(1/(1+tau^2) - 2 gamma*)`, whose certified margin over `b(W)` at
`tau = tau_start` is much thinner — my dps-30 values (script A [3]):
**W1 1.4286x, W2 1.4409x, W3 1.7065x, W4 1.7732x, W5 1.9241x, W6b
1.8654x, W7 1.2971x**. The certificate is rigorous (the floor is a
closed-form bound, asserted in-script, safe-direction `q`), so the theorem
is unaffected — but the certified worst margin of the WHOLE certificate is
**1.30x (W7, at tau_start = 0.7275)**, not 7.96x. Since the thin
`tau_start` margins are exactly the kind of number a wave-4/SL4' consumer
or a repairs session might budget off (the F2-class lesson of
`referee_numerics_wp4.md`), the two headline sentences must be reworded,
e.g.: "worst CELL headroom 7.96x; the analytic floor at the crossover
`tau_start` is the thinnest certified link, 1.30x (W7; 1.43x W1)". Note
also the TRUE `delta_norm` at the W7 crossover is comfortable
(my script A [4]: `delta_norm(40, 0.7275) = 0.1615`, ~16x `b = 0.0098`);
it is the BOUND that is thin, not the truth — one clause saying so would
preempt alarm.

**R2 (label, established repair class = wp3-a2-F7 / assembly MR-3).**
§7.2 heads its table "(verbatim table)" but the quoted rows are condensed:
the archived `out_sl3p_s2b.txt` rows carry a trailing
`worst cell (w1c,t1,t2)=(...)` field (with full float digits) that the
draft drops (it is summarized in prose below the table — accurately, I
checked all seven). Relabel "condensed; full rows archived, re-run
byte-identical" or reprint in full. §7.1's "(key lines)" and §7.3
(essentially verbatim) are fine.

**R3 (corner-slack decomposition in §5.2/§8 — wrong numbers, safe
direction).** §8 says the E.6.B regime-corner cell `(0.30, 0.58)` has
"true corner slack ~0.004; the cell bound concedes ~0.0026"; §5.2's FAIL
anecdote likewise says "the true slack ~0.004 near lam = 0.30". My dps-30
measurement (script A [6]): true pointwise `min_x [F(0.30) - F(x)]` at
`tau = 0.58` is **0.00267** (and the route file's own NC3 normalized floor
`0.007921 x 0.3364 = 0.00266` agrees), so the cell bound `0.001448`
concedes **~0.0012**, not ~0.0026. The PASS/FAIL story is unchanged (with
`d lam = 0.002` the `lam`-edge loss `~0.0034` indeed exceeds the true
slack `0.00267` — the anecdote's logic survives with the corrected
number), but both parentheticals should be corrected to "true ~0.0027,
concession ~0.0012".

**R4 (float-edge slivers — one-line note wanted).** §4.3/§5.2 claim the
cells "tile [band] x [tau_start, 0.8]" (resp. the E.6.B box). Edge audit
(`out_ref_msl3p_c_edges.txt`): the `np.arange` top `tau`-edges land at
`0.8 - 5.3e-15` (W5), `0.8 - 2.7e-15` (W6b), `0.8 - 1.6e-15` (W7) in
script B and `0.8 - 2.4e-14` in script C, so read as exact real intervals
the certificates stop a `~1e-14`-wide `tau`-sliver short of `4/5`.
Continuity of `delta_norm`/`F` in `tau` (derivative `O(1)`) against the
certified margins (`>= 2.6e-2` and `>= 1.4e-3`) closes the sliver by ~11
orders of magnitude; W1–W4 and both `lam`-grids overshoot their endpoints
(no sliver), and the E.6.B `lam`-edge join at `0.40` is a thin VALID cell,
not a reversal. Add one sentence acknowledging the float-edge convention
(it is part of the declared float64-certificate flag, but the word "tile"
should not be quotable against exact endpoints).

**R5 (display trivia, F1/rounding class — record).** (i) §2's intermediate
`4.04(1/4 + 1/401) ... = 1.0202` is an up-rounding of `1.020075` printed
with "=" (safe direction, still `<= 1.03`). (ii) `eps_t ... = 1.5603e-3`
in §1/§5.3: true value `1.560224e-3` (nearest `1.5602e-3`); up-rounded
upper bound, safe, but the "=" should be `<=` or the extra digit printed
(the in-lemma comparison uses the exact value). (iii) §7's preamble says
the corner evaluations carry "a stated guard (1e-6...)": the guard exists
only in script C (Part B); script B's effective guard is its macroscopic
margin — a half-sentence would make the flag exact. (iv) Script A's c1/c2
grid ENDPOINTS `0.999645`/`1.000021` are small-`v` float-cancellation
artifacts in the unused directions (see §1.3) — worth a parenthetical so
nobody reads `1.000021 > 1` as contradicting the exact `S`-series claim.

**Explicitly checked and clean (no finding):** the seven `b(W)` values
(hand + dps-30, all digits); the seven `q(W)` safe-direction values vs my
quad truth; the seven `tau_c'`/`tau_start` values and every in-script
analytic assert; `K1'` for all five `gamma*`; `C_env`, `eps_hat`, `I_h`,
`c_B`, `eps_t`, the `408.075` and `14.08` monotonicity minima; E.6.A's
`236` cells / worst margin `1.12943`; E.6.B's `1191 x 440` cells / slack
`0.00144803` / `nfail = 0`; E.6.C's `0.066061 = 42.3 eps_t`; the band
partition vs composite §0 (verbatim); the delivered-vs-spec `gamma*` list
(verbatim = composite §5.3); the `lam_split = 0.30` double coverage; the
`min(m,s2)`-free statement (SL3' needs no `s2 >= 79` clause — correct);
the W5-fallback-not-needed claim; the quoted route/REF-C numbers
(`101.41`/`101.5`/`129.86`/`0.008935`/`2.7e-6`/`5.2e-8`); the
`10.081 <= 136` repaired-form quote; `40/401 < 0.0998`; `7.85 <
2pi/0.8` (margin `0.00398`); `t2 l2/2 = 0.356 < pi/2`.

## 3. Script verification summary

All six scripts under `g2_scripts/campaign_20260811/wave4_sl3p/` re-run
(python3, this machine, 2026-08-12) and diffed against their archives:
`sl3p_s2a_constants.py`, `sl3p_s2b_e5cert.py`, `sl3p_s2c_e6cert.py` —
**byte-identical** (0.4 s / 0.4 s / 4.9 s); `sl3p_nc1_identity_master.py`,
`sl3p_nc2_continuum.py`, `sl3p_nc3_split.py` — **identical modulo the
timing line** (the established wp-class convention). Proof-bearing source
audit: script B's Riemann/corner directions all safe (§1.5); script C's
corner directions all safe (§1.6); script A is constants/spot-check only
(non-certificate lines clearly so). The draft's §7 quotes exist verbatim
in the archives (R2's condensation noted).

## 4. Independent referee scripts (mine; SAVED and RUN, outputs archived)

`referee_maths_wave4_sl3p_scripts/ref_msl3p_a_constants.py` — dps-30
constants, budgets, thresholds, worst-cell and truth-delta recomputation
(key lines quoted in §1.5/§1.6 above; full output
`out_ref_msl3p_a.txt` + `out_ref_msl3p_a2.txt`).
`ref_msl3p_b_truth.py` — the 162-point direct-summation truth attack + the
E.4a display check + the NC1 12-digit cross-reproduction
(`out_ref_msl3p_b.txt`, quoted in §1.9). Edge audit in
`out_ref_msl3p_c_edges.txt` (quoted in R4).

## 5. Bottom line for the campaign ledger

- `wave4_sl3p_20260812.md`: **MINOR_REPAIRS** (R1–R5, all text-level; R1
  is the one a downstream consumer must see). **Theorem SL3' stands as
  stated — PROVED modulo the flagged finite-certificate class** (the same
  class as the chain's other accepted certified inputs, and here genuinely
  monotone-cell, not point-sampled), on the full claimed scope `m >= 401`,
  `|lam| in (4/m, 0.89]`, `t in (0, 0.8|lam|]`, with the delivered bands
  exactly the composite §5.3 targets. The analytic chain
  E.4a/E.4b/E.5.1/E.5.2/E.6a/E.6c is complete and correct; the route's
  Stage-1 lemmas E.1/E.2/E.3 were re-derived here and are correct.
- Margins for the record (post-R1 wording): worst CELL headroom 7.96x
  (E.5.3 W7); worst certified margin overall **1.30x at W7's
  `tau_start = 0.7275`** (analytic floor; truth at that point is
  ~16x the budget, so the thinness is in the bound, not the fact);
  E.6.B worst cell slack `+1.448e-3` (true corner slack `~0.0027`);
  E.6.A worst cell margin `1.1294x`.
- This report is the MATHS half; house rule still owes the package its
  NUMERICS referee (independent re-build of the two big cell certificates
  at higher precision and an off-grid attack on the `tau_start`
  crossovers would complete the two-referee pattern). SL3' feeds SL4';
  per composite §5.3 the remaining bridge pieces (SL1', SL4', SL-sliver)
  are untouched by this report.

*End of referee_maths_wave4_sl3p.md.*
