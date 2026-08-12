# referee_numerics_wave4_sl3p — adversarial numerics report on `wave4_sl3p_20260812.md` (Theorem SL3', Stage 2)

*Adversarial NUMERICS referee, wave 4, 2026-08-12. Target:
`wave4_sl3p_20260812.md` (+ its Stage-1 companion
`wave4_sl3p_ROUTE_20260812.md` and all six scripts in
`g2_scripts/campaign_20260811/wave4_sl3p/`). Consumer context read:
`wp4_draft_composite.md` §0/§5.3, `STATUS_wave3.md`, `referee_numerics_wp4.md`
(corrected budgets). Default-to-refutation posture applied: every script
re-run; every quoted number checked; independent third-path re-implementation
of the final statement; exact-rational budget audit; independent
finer-quadrature rebuild of the E.5.3 certificate; ground-truth quadrature at
worst cells; off-grid probes at band edges, the regime corner (0.30, 0.58),
the w ~ 4.9 CL-max, m = 401/402 and large m. Referee scripts + archived
outputs: `referee_numerics_wave4_sl3p_scripts/` (ref_sl3p_r1..r5, out_*.txt,
rerun_*.txt).*

## VERDICT: MINOR_REPAIRS

The certificate package is numerically sound. All six scripts re-run
byte-identical; the E.5.3 and E.6 certificates survive an independent
rebuild, exact-rational budget audit, ground-truth quadrature, and off-grid
adversarial scans; the final SL3' inequality itself holds at 241 independent
adversarial probe points (worst ratio 1.0592, exactly the draft's W5 figure)
and at m up to 10^6. Two repairs, both non-load-bearing: a wrong commentary
number in the honest register (F1) and a formal fp-grid coverage sliver at
the tau = 0.8 endpoint for three bands (F2). Nothing FABRICATED: every
quoted number traces to an archived, re-run-verified output.

## 1. Re-run of the draft's scripts (all PASS, byte-identical)

All from `g2_scripts/campaign_20260811/wave4_sl3p/`, re-run 2026-08-12,
outputs archived as `referee_numerics_wave4_sl3p_scripts/rerun_*.txt`:

| script | diff vs archived output |
|---|---|
| `sl3p_s2a_constants.py` | IDENTICAL |
| `sl3p_s2b_e5cert.py` | IDENTICAL |
| `sl3p_s2c_e6cert.py` | IDENTICAL |
| `sl3p_nc1_identity_master.py` | identical except `total time 12.6 s` -> `12.8 s` |
| `sl3p_nc2_continuum.py` | IDENTICAL (incl. its timing line) |
| `sl3p_nc3_split.py` | IDENTICAL |

Every number quoted in draft §7.1/§7.2/§7.3 is verbatim in the archived
outputs (the §7.1 "(i)" line is an honest condensation of five archived
lines, all with positive direct-domination minima 1e-6..6e-6; §7.1 is
labeled "key lines" — the wp3-a2-F7 repair class, correctly flagged).

## 2. Independent verification

### 2.1 Final-statement direct check (REF-R1, third computational path)

`ref_sl3p_r1_direct.py` verifies `-2 log|phi_lam(t)| >= 2 gamma*(W) s2 t^2`
with an implementation sharing NOTHING with the draft's two paths: log-moduli
via the closed form `|1-z^j|^2 = (1-q^j)^2 + 4 q^j sin^2(jt/2)` (not the
E.1 g/h identity, not NC1's series summation), and `s2` from the
truncated-geometric variance formula `Var(U_j) = q/(1-q)^2 -
j^2 q^j/(1-q^j)^2` (not via `h`). Verbatim:

```
points checked: 241   FAILs (slack<=0): 0
worst gamma_ach/gamma* = 1.05921 at m=401 w=20.0 tau=0.8 (W5)
  m=401 w=4.05  tau=0.8 [W1]: -2log|phi| = 76.8524292638 ... gamma_ach = 0.492265
  m=401 w=4.9   tau=0.8 [W1]: ... slack = 12.0123  gamma_ach = 0.480888
  m=401 w=356.89 tau=0.8 [W7]: ... slack = 28.314  gamma_ach = 0.379407
```

The probe set includes: both sides of every band boundary at offset 1e-5,
`w = 4.000001` (the `w > 4` scope edge), the CL-evidence maximum `w = 4.9`
(ratio 1.145 — comfortable), `lam = 0.3` exactly and both sides of the W7
regime split (`w = 120.3/120.35` at `m = 401`), `lam = 0.89` at four `m`,
`tau in {0.005, ..., 0.7975, 0.8}` (incl. every `tau_start` neighborhood),
and `m in {401, 402, 1000, 5000}`. Float64 sweeps at `m = 2*10^5` and
`10^6`: all PASS, `gamma_ach(m=10^6, w=20, tau=0.8) = 0.402547` — converged
onto NC2's continuum `G_min(W5) = 0.402547`, confirming the continuum
functional is the honest `m -> infinity` envelope. The identity-path values
reproduce NC1's to all printed digits (e.g. `76.8524292638`).

### 2.2 Certificate E.5.3: exact budget + independent rebuild (REF-R2)

`ref_sl3p_r2_e53_indep.py`, three layers, all PASS:

1. **Exact-rational `b(W)` audit** (Fractions): e.g. `b(W1) =
   702473/257281600 = 0.002730366`, `b(W7) = 493431/50125000 =
   0.009844010`; all seven printed 6dp values are the correctly rounded
   exact rationals.
2. **Independent rebuild at quadrature `D = 0.0005`** (draft used `0.001`),
   freshly written cell code, same cell layout: ALL BANDS PASS, identical
   worst cells, minima `+5.2e-6 .. +8.0e-5` ABOVE the draft's (sharper
   quadrature moves the certified bound up, as it must — the draft's coarser
   sums are the conservative side). Draft's `tau_start` values reproduced
   exactly (0.4150/0.4200/0.4850/0.4875/0.5500/0.6750/0.7275).
3. **Ground truth**: `delta_norm(w, tau)` by mpmath arch-subdivided
   quadrature at every band's worst-cell corners: true minima exceed the
   certified minima everywhere (concessions +0.0045..+0.0107 on W1–W6b;
   +0.0552 on W7, where the crude `1 - avg_h <= 1` is used) — the
   lower-bound property holds at every probed corner.

### 2.3 Certificate E.6: off-grid attack (REF-R3)

`ref_sl3p_r3_e6_probe.py`:

- **(a) Off-grid fine scan** of `F(lam) - F(x)` over `[0.30, 0.89] x
  [0.58, 0.8] x [2 lam, 7.85]` with irrational-offset grids (609 x 195 x
  ~2065 points, nothing shared with the certificate's cell edges): global
  min `+0.002673` at exactly the regime corner `(0.30, 0.58, 0.60)`;
  positive everywhere. Corner refinement (steps 1e-4) confirms `+0.002673`.
- **(b) Tail**: max `F(x)` on `[7.85, 60] x {tau <= 0.8}` = `+1.639e-4 <=
  eps_t = 1.5602e-3` (9.5x margin below the tail constant); independent
  floor min `F(lam) = 0.066956 >= eps_t` (draft's certified floor 0.066061
  is below the truth, correct direction).
- **(c) Condition C** continuous scan (step 1.3e-5): min margin `1.1374` at
  `lam = 0.89` — above the cell-certified 1.1294, consistent.
- **(d) Small-tau side** (`tau <= 0.58`, E.6a's regime) off-grid: min
  `+1.339e-6` at `(0.30, 0.013, 0.60)` — exactly the `tau^2`-scaling of the
  proven normalized floor (`0.0079 * 0.013^2 = 1.3e-6`), positive.
- **(f) The §5.2 honesty note is REAL**: re-running Part B with the uniform
  `d lam = 0.002` grid the draft says FAILED gives min cell slack
  `-0.001559` at `(0.30, 0.6195)`, 8913 cells below guard — the recorded
  first-pass FAIL is REPRODUCED, and the zoned refinement was necessary.

### 2.4 Lemmas E.4a/E.4b as direct inequalities (REF-R4)

`ref_sl3p_r4_e4ab.py`: E.4a's discretization inequality `sum F(j lam) <=
(1/lam) Int_0^w F + 2 g* tau^2 + m * 1.03 e^{-2pi/tau}` verified by direct
mpmath summation vs arch-subdivided quadrature at 11 adversarial
`(m, w, tau, gamma*)` cases (band tops, `lam = 0.3` split edge, `tau = 0.05`,
both gamma extremes, `m` to 2000): all PASS, slacks +0.002..+1.29. E.4b
verified at the `(0.3, 0.8)` corner for all five gammas (mpmath dps 30,
ratios 0.195..0.353) and on 10^6 random off-grid points per gamma: max
ratio always < 0.36 << 1.

### 2.5 K1' commentary ratio (REF-R5 — an attack that FAILED, in the draft's favor)

My first random probe showed ratio 0.35675 > the draft's "true ratio
<= 0.355" (§3). `ref_sl3p_r5_k1ratio.py` resolves it: the true sup is the
analytic `lam -> 0` limit `(1 - 2 g*)/(12 K1') = 0.354191` (tau-independent
at leading order, mpmath-confirmed at `lam = 1e-6` for `tau = 1e-6` and
`0.8` alike; interior values smaller). The float64 excess was catastrophic
cancellation at tiny `lam` (`F(0)-F(lam) ~ 1e-14` computed as a difference
of O(0.1) quantities). The draft's 0.355 claim is CORRECT, and its script's
grid choice (`lam >= 1e-4`, noted "away from catastrophic cancellation" for
c3) is the right hygiene.

## 3. Findings

- **F1 (the one substantive text repair).** §5.2's and §8's decomposition of
  the E.6.B worst cell is wrong: "the true corner slack is ~0.004; the cell
  bound concedes ~0.0026". Referee measurement (REF-R3(a), two independent
  resolutions): the TRUE slack at the regime corner `(lam, tau, x) =
  (0.30, 0.58, 0.60)` is `+0.002673`, so the cell bound concedes
  `0.002673 - 0.001448 = 0.001225`. Both sub-numbers must be replaced
  (`~0.004 -> ~0.0027`, `~0.0026 -> ~0.0012`); §5.2's mechanism sentence
  ("edge loss ~coth(lam/2) d lam exceeds the true slack ~0.004") should also
  read `~0.0027` — note the coarse edge loss `~0.0033` indeed exceeds
  0.0027 (it would NOT exceed 0.004, so the corrected number actually makes
  the recorded FAIL story consistent). The certified `+1.448e-3`, the PASS,
  and the safe direction (truth > certificate) are all unaffected.
- **F2 (formal coverage sliver at `tau = 0.8`).** fp-arange audit
  (REF-R3(e)): in script B the last tau edge falls SHORT of 0.8 for
  W5/W6b/W7 by 5.3e-15/2.7e-15/1.6e-15 (the append-0.8 tolerance `1e-12` is
  tighter than arange's accumulated fp error; W1–W4 land at
  `0.8000000000000003` and do cover 0.8); in script C Part B the last tau
  edge is `0.8 - 2.4e-14`. Strictly, the certificates as run cover
  `tau <= 0.8 - O(1e-14)`, while Theorem SL3' claims the closed endpoint
  `t = 0.8 lam`. Impact nil in substance (the certified functions are C^1
  with O(1) tau-derivatives; margins at the top cells are 0.0286+ in script
  B and 1.45e-3 in script C, vs an O(1e-14) continuation cost), but a
  "PROVED modulo certificates" claim should not need a continuity argument
  the draft never states. Repair (one line each): append 0.8 whenever
  `tedges[-1] < 0.8` (tolerance 1e-9) and re-run — or add the one-sentence
  endpoint-continuity remark to §7's certificate-class flag.
- **F3 (observation).** §2 prints `4.04 (1/4 + 1/401) ... = 1.0202`; the
  value is `1.020075` — an up-rounding presented as equality. Safe (the
  consumed constant is `<= 1.03`); print `<= 1.0201` or `1.02008`.
- **F4 (observation, no action).** Draft §3's "true ratio <= 0.355"
  VERIFIED (see §2.5; sup = 0.354191 at `lam -> 0`). Recorded because this
  campaign has a history of grid-artifact headroom claims (wave-3 F2): this
  one is NOT a grid artifact.
- **F5 (observation, no action).** Script C's lam-edge array has 1192 edges
  (fp arange emits an extra `0.40` edge), giving one near-degenerate
  lam-cell; the printed "1191 lam-rows" = len-1 is consistent and the
  degenerate cell is harmless (its bound is still valid).

## 4. Quoted-number audit (spot table; all verified against re-run outputs)

| draft claim | referee check | status |
|---|---|---|
| `C_env = 4.0150`, `<= 4.04` | 4.014981 (rerun A(a)) | OK |
| L2 min ratio 408 | 408.075 at `u = 1.25`, monotone | OK |
| `K1'(0.32) = 0.08470`, ratios 0.354/0.328/0.267/0.233/0.196 | rerun A(d) + R4 + R5 | OK |
| `I_h`: right-sum 2.784022, `>= 2.7` | rerun A(e); mpmath quad consistent | OK |
| `c_B = 26.34`, min ratio 14.08, `1.871 < 26.34` | 26.3415; 26.3415/1.87141 = 14.076 | OK |
| E.5.2 spot min `+6.33e-4` at (200, 0.05) | rerun A(g) | OK |
| `eps_hat = 6.25e-4`, true `6.248e-4` | 6.247645e-4; script B uses 6.25e-4 (inflates b, safe) | OK |
| §4.3 table (b, q, tau_c', cells, minima, headrooms) | byte-identical rerun + independent rebuild (§2.2) + exact b(W) | OK |
| worst headroom 7.96x (W7) | 0.078395/0.009844010 = 7.964 | OK |
| E.6.A min margin 1.1294 at [0.8875, 0.89] | rerun C Part A; continuous truth 1.1374 | OK |
| E.6.B min slack +0.001448 at (0.30, 0.58), 0 < guard | rerun; truth +0.002673 above it | OK (commentary: F1) |
| `eps_t = 1.5603e-3 <= 1.57e-3`; `2pi/0.8 - 7.85 = 0.003982 > 0` | 1.560224e-3; OK | OK |
| E.6.C floor 0.066061, 42.3x | 0.066061/1.560224e-3 = 42.34; indep floor 0.066956 | OK |
| `1.0202` in §2 | 1.020075 | F3 |
| "true corner slack ~0.004 / concedes ~0.0026" (§5.2, §8) | truth +0.002673 / concession +0.001225 | **F1** |
| coarse `d lam = 0.002` first pass FAILED | REPRODUCED: min slack −0.001559, 8913 cells < guard | OK |
| consumer impact `0.008935 / 101.5 / 2.7e-6 / 5.2e-8` | rerun NC3 byte-identical + hand recompute | OK |
| delivered bands = composite §5.3 targets; `t`-scope superset of `[lam/2, 0.8 lam]` | composite lines 52–54, 429–430 checked | OK |

## 5. Scope notes

- The certificate CLASS (float64 cell corners, guard 1e-6, Sturm-able in
  principle) is exactly the campaign's flagged grid-certificate class; the
  draft flags it correctly in §7 and §8. fp error at the probed scales is
  O(1e-13) as claimed (R2's D-halving moved minima by < 8e-5, all upward).
- The mathematical proofs (E.1–E.6a chain, directions of every Riemann sum
  and corner bound) were re-derived here only to the extent needed to attack
  the numerics; I checked every inequality DIRECTION used by the two
  certificate scripts and found all sound (h-sums: left=upper/right=lower;
  g-majorant globally decreasing incl. at the arch junction; numerator
  positivity asserted before division; W7's `1 - avg_h <= 1` safe side;
  E.6.B pins the sin^2 argument at the cell's x-left edge legitimately since
  `7.85 < 2pi/0.8`). Full proof-correctness certification belongs to the
  maths referee.
- CL-composite consumption: delivered gamma* bands identical to the §5.3
  targets, so `C*_eff = 16.9088` is consumed unchanged — no re-pricing
  needed. Confirmed against composite §5.3's displayed target line.

*End of referee_numerics_wave4_sl3p.md.*
