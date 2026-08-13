# referee_numerics_sol_s1 — adversarial numerics referee for `sol_s1_20260812.md` (wave 6b)

*Cross-model refereeing pass, F2 campaign, 2026-08-12. Target:
`sol_s1_20260812.md` (gpt-5.6-sol, single-model UNREFEREED attempt at (S1)),
attacked against the RE-ARCHITECTED band targets of
`wave6_s1_plan_20260812.md`. Mandate: maximal bar, default to refutation;
script the draft's VERIFICATION RECIPE in full AND design adversarial checks
the recipe omits. Sources read: `sol_s1_20260812.md`, `wave6_s1_plan_20260812.md`
(+ its archived scout output `wave6_scout/out_scout_s1_targets.txt`),
`STATUS_wave5.md` (S1 rows), `CL_composition_20260812.md` §4 ((S1) statement
form). NOT read: `g2_draft_t1_20260803.md`. `gamma = 1/8` untouched. All four
referee scripts SAVED and RUN 2026-08-12, outputs archived beside them in
`g2_scripts/campaign_20260811/wave6b_ref_s1/`:*

- `ref1_sentinels_engine.py` (`out_ref1_sentinels_engine.txt`) — independent
  cumulant engine + V1/V2 + reflection + envelope-at-finite-m + adversarial
  truth sweep;
- `ref2_mn_bounds.py` (`out_ref2_mn_bounds.txt`) — V3 derivative bounds (17)
  + symbolic recurrences (18)/(19);
- `ref3_band_certificate_iv.py` (`out_ref3_band_certificate_iv.txt`) —
  RIGOROUS outward-rounded interval re-certification of the SOL.6 table
  (V4+V5), mpmath.iv, prec 100 bits, adaptive cells to 2^-14;
- `ref4_envelope_vs_Dn.py` (`out_ref4_envelope_vs_Dn.txt`) — direct
  falsification test of (15)–(22) against the actual finite-m `D_n`.

**VERDICT: MINOR_REPAIRS.** Every mathematical claim and every constant in
the draft is TRUE and now independently certified, with visible margin at
every layer (truth < my rigorous certificate < the draft's ceilings < the
plan's targets). The repairs are provenance/statement-hygiene items, not
mathematics: the draft's central "exact rational interval certificate" was
asserted with NO saved script or archived output anywhere in the repo, and
its final statement drops the `w > 4` (i.e. `lam in (4/m, 0.89]`) range that
the consumed (S1) form carries. Details in §5.

---

## 1. What the draft must deliver, and does it target the right constants

The re-architected (S1) (plan §2, form unchanged from
`CL_composition_20260812.md` §4): for `m >= 561`, `lam in (4/m, 0.89]`, band
`W` of `w = m lam`: `|kappa_3| <= R31*(W) s2/lam`, `kappa_4 <= R42*(W)
s2/lam^2`, with

```
R31* = 1.19 / 1.44 / 1.82 / 2.04 / 2.38 / 2.56 / 2.71
R42* = 0.87 / 1.62 / 3.11 / 4.27 / 6.38 / 7.33 / 8.17
```

The draft's SOL.9 proves exactly these fourteen constants on exactly the
plan's partition W1 (4,5], W2 (5,6], W3 (6,8], W4 (8,10], W5 (10,20],
W6b (20,40], W7 (40,oo). Literal comparison (ref3, "constants consumption"):

```
  draft R31* == plan R31*: True
  draft R42* == plan R42*: True
```

The plan's chain certificate consumes these same constants; its closure
arithmetic re-checked (ref3):

```
  20 * worst row 0.978293 = 19.56586  (plan quotes C* = 19.5659; |diff| < 5e-5: True)  <= 20: True
  20 * worst row(1581) 0.75839 = 15.1678  (plan quotes 15.1678; match: True)  <= 136: True
```

So the chain closes at `19.5659 <= 20` on `[561, 1580]` and `15.1678 <= 136`
at `m >= 1581` exactly as the plan states, PROVIDED the plan's row
recomputation (block [C]) is re-certified by its own referee — that is §9
item 1/3 of the plan and is NOT this draft's burden. The draft even proves
STRICTLY MORE than each target: its certified per-band ceilings
(0.900/1.090/1.370/1.550/1.850/1.970 and 0.680/1.250/2.400/3.260/4.980/5.650,
plus 2.1304/6.4114 on W7) all sit strictly below the targets.

The draft also correctly does NOT claim the (S2) adjustment
(`C5*(W7): 0.80 -> 0.50`) — its WHAT-REMAINS item 3 matches the plan's §6
caveat. No scope creep found.

## 2. Independent engine and the recipe's own checks (V1, V2)

My engine (`ref1`) was written directly from the tilted-factor definition
and validated two independent ways before use:

```
  brute-force (m=6, lam=0.3): k2 rel err 2.709e-50  k3 rel err 1.477e-49  k4 rel err 5.211e-48
  diff-of-logZ (m=50, lam=0.2): rel errs 7.527e-51 1.234e-50 1.628e-50
```

(exact enumeration of the tilted Mahonian by polynomial convolution, and
numerical differentiation of `log Z` — both agree with the draft's SOL.1
`g_n`-sum formulas to ~1e-48). The `D_n = lam^{n+1} kappa_n` identity (5)
verified to 1e-48 at three (m, w) pairs; `kappa_3 > 0` at all of them
(SOL.2's claim).

**V1 sentinels — all six rows reproduced** (m = 561, `lam = w/561` exact):

```
  w=  5: r31=0.88636451 (draft 0.88636)   r42=0.6506471 (draft 0.65065)
  w=  6: r31=1.0738715 (draft 1.0739)     r42=1.2057655 (draft 1.2058)
  w=  8: r31=1.3484805 (draft 1.3485)     r42=2.3075471 (draft 2.3075)
  w= 10: r31=1.5183545 (draft 1.5184)     r42=3.1636382 (draft 3.1636)
  w= 20: r31=1.8035605 (draft 1.8036)     r42=4.820621  (draft 4.8206)
  w= 40: r31=1.9113505 (draft 1.9114)     r42=5.4653371 (draft 5.4653)
  ALL SENTINELS MATCH: True
```

**V2 geometric values — both enclosures verified**, at dps 50 (ref1) and
again in outward-rounded interval arithmetic (ref3):

```
  a(0.89) = 2.1303060576444510159   in (2.1302, 2.1304): True   < 2.71: True
  b(0.89) = 6.4112558488549645817   in (6.4111, 6.4114): True   < 8.17: True
  zeta(2) = 1.644934066848226436472415  in draft enclosure (24): True
  e^-4 = 0.0183156... < 1/54 = 0.0185185...: True
```

## 3. V3 derivative bounds and the analytic skeleton

`ref2` differentiates the closed forms SYMBOLICALLY (sympy, exact) and
evaluates at dps 40 on a step-0.02 grid over [0, 40] with an off-grid
excursion bound from the gridded third derivative (x2 safety):

```
  symbolic (18) residual 2h2 - x h2' - h3 == 0: True
  symbolic (19) residual 3h3 - x h3' - h4 == 0: True
  h2'': certified sup bound 0.1685862497 < 1.0: True
  h3'': certified sup bound 0.184454918  < 4.0: True
  h4'': certified sup bound 0.5300420082 < 20.0: True
```

So (17) holds with factors 5.9x / 21.7x / 37.7x to spare (see finding F3).
The series about 0 (`h2 = 1 - x^2/12 + x^4/240...`, `h3 = 2 - x^4/120...`,
`h4 = 6 + x^4/120...`) confirm the removable values (h2,h3,h4)(0) = (1,2,6)
and, notably, that `h4` INCREASES near 0 — the draft never assumes h4
monotone, and its SOL.3 handles h4 through `b = h4/h2` increasing, which is
the correct route. I re-derived SOL.2 and SOL.3's monotonicity proofs by
hand (the `F(x) = x cosh x + 2x - 3 sinh x` argument and
`a' > 0 <=> sinh x > x` are both correct; `b = x^2 + 6 h2` confirmed), and
verified a/b monotonicity numerically (a: 2.0067 < 2.0415 < 2.1303 and
b: 6.0200 < 6.1265 < 6.4113 at lam = 0.2/0.5/0.89).

## 4. The band certificate (V4+V5): rigorously re-certified, and the crux

`ref3` is a fully rigorous independent certificate of the SOL.6 table:
mpmath.iv outward-rounded interval arithmetic (100 bits), cells of width
2^-8 with the draft's own lambda rule (`lam in [0, B/561]`, B = cell right
edge), monotone endpoint enclosures for the series term `S_n(w)` (termwise
decreasing — elementary), h2/h3 by proved monotonicity, h4 by direct
interval evaluation (no monotonicity assumed), series tail enclosed by
`[0, 1e-36]` after the next-term bound drops below 1e-38 (the w >= 4 term
ratio is < e^-4 * 16 < 0.3). Result: **every cell of every band passes with
zero bisections needed**, and the three-layer margin structure is:

| band | truth sup r31 (ref1) | my rigorous sup bound | draft ceiling | target | truth sup r42 | my bound | ceiling | target |
|---|---|---|---|---|---|---|---|---|
| [4,5]   | 0.886365 | 0.891618 | 0.900 | 1.19 | 0.650647 | 0.662566 | 0.680 | 0.87 |
| [5,6]   | 1.073872 | 1.078050 | 1.090 | 1.44 | 1.205766 | 1.214615 | 1.250 | 1.62 |
| [6,8]   | 1.348481 | 1.351876 | 1.370 | 1.82 | 2.307547 | 2.314811 | 2.400 | 3.11 |
| [8,10]  | 1.518354 | 1.521490 | 1.550 | 2.04 | 3.163638 | 3.171079 | 3.260 | 4.27 |
| [10,20] | 1.803561 | 1.806643 | 1.850 | 2.38 | 4.820621 | 4.830802 | 4.980 | 6.38 |
| [20,40] | 1.911351 | 1.916144 | 1.970 | 2.56 | 5.465337 | 5.485773 | 5.650 | 7.33 |

L2 floors likewise: my certified infima 1.192113 / 1.960097 / 2.833867 /
4.737293 / 6.715123 / 16.705894 all >= the draft's floors 1.15 / 1.90 /
2.75 / 4.65 / 6.60 / 16.50, all positive (so the ratio division is licit).
Verbatim verdict line:

```
ALL SIX BANDS RIGOROUSLY CERTIFIED (table (V5)+(V4) TRUE): True
```

I also ran the draft's exact resolution (width-2^-12 cells) at each band's
right edge — the presumptively binding cells — and each passes with margin
(e.g. `[4.99975585938, 5.0]: U3/L2 <= 0.8883349...` vs ceiling 0.900), so
the draft's specified procedure is not merely true-in-conclusion but
plausibly executable exactly as specified.

**The middle link, attacked directly** (`ref4` — a check the recipe omits):
the envelope formulas (20)–(22) evaluated POINTWISE (lambda a point, no
interval slack) against the actual finite-m `D_n` at 104 adversarial
(m, w) pairs (m in {561, 562, 563, 600, 701, 1000, 2500, 10000}, w
including off-grid values 4.001, 5.7, 7.3, 9.9, 15.5, 33.7):

```
check 1 -- pointwise L2 <= D2, D3 <= U3, D4 <= U4 at ALL probes: True
check 2 -- |eps_n| <= w lam^2 M_n/12 with draft M=(1,4,20) at ALL probes: True
          with ref2 measured M=(0.1686,0.1845,0.5301) at ALL probes: True
worst |eps|/draft-cap ratio: 0.0408221 at (m,w,n)=(561, '4.001', 2)
```

The trapezoid error model of SOL.5 is confirmed not just as an inequality
but as a mechanism (observed error is 4% of the generous cap, and passes
even the 5–38x tighter measured-M caps).

**Adversarial truth sweep** (ref1 [G] — off-grid edges, multiple m, worst
plan corners): truth `r31/r42` <= the certified ceilings at every one of
~170 sampled (band, w, m) points, maxima always at (right edge, m = 561) —
consistent with the plan's block [T]; W7 probed at w = 40.0001, the deep
corner lam = 0.89 for m up to 100000 (r31 -> 2.130271, monotone from below,
always under both the geometric envelope and 2.71), and lam = 0.88999/0.089:

```
  truth <= certified ceilings at ALL sampled adversarial points: True
  W7 truth under 2.71/8.17 (and under a(0.89)/b(0.89)) at all probes: True
```

**Reflection (SOL.9's negative-lambda step)** — verified exactly (ref1 [E]):
`kappa_2, kappa_4` even and `kappa_3` odd in lambda to 1e-50 at
lam = ±0.03/±0.5/±0.89, matching the parity argument (h2, h4 even, g3 odd),
which I also confirmed analytically.

## 5. Findings

- **F1 (provenance — the reason this is not SURVIVES).** The draft asserts
  "Exact outward-rounded rational interval evaluation gives: [table]" and
  "(17) ... rational interval verification ... specified in the
  VERIFICATION RECIPE", but NO script and NO output artifact exists on the
  sol side (`wave6_sol/` contains only the API driver `run_sol.py` and
  `ids.json`). Under the house rule (every numeric from a SAVED+RUN script
  with output quoted), the draft's central certificate was, as shipped, an
  unexecuted claim. It happens to be TRUE — `ref3` + `ref2` now constitute
  an executed, archived certificate of every number in SOL.6/(17) — but the
  ledger must record that the certificate artifact is THIS referee's, not
  the prover's. REPAIR: adopt `wave6b_ref_s1/ref3_band_certificate_iv.py`
  (+ `ref2`) as the certificate of record, or have the prover run its own.
- **F2 (statement hygiene).** Theorem SOL.9 quantifies over
  `0 < |lam| <= 0.89` with "W determined by w = m|lam|" and never states
  `w > 4`. The bands' union is (4, oo), so no claim is made for w <= 4 and
  nothing false is asserted, but the consumed (S1) form carries
  `lam in (4/m, 0.89]` explicitly. REPAIR: one line in SOL.9 restoring the
  range (and noting the two-sided |lam| version is a superset of the
  consumed one-sided statement).
- **F3 (observation, no action).** (17) is generous by factors 5.9/21.7/38
  (measured sups 0.1686/0.1845/0.5301 vs 1/4/20). The certificate's error
  terms could be tightened ~6x if a future re-architecture needs slack;
  harmless as is.
- **F4 (recipe coverage — recorded, discharged here).** The recipe's V1
  samples only the plan's own measured friendly points (band right edges at
  m = 561, matching `out_scout_s1_targets.txt` digit-for-digit) and
  contains no check of the envelope against actual finite-m `D_n`, no
  off-grid w, no m > 561, and no negative-lambda probe — V4/V5 re-use the
  very formulas under test, so an error in SOL.5's bookkeeping would have
  passed the recipe as written. All such checks were designed and run here
  (ref1 [E]/[F]/[G], ref4) and PASS. No repair needed in the proof; the
  maths referee should not treat the recipe as self-sufficient.
- **F5 (deferred to maths referee).** SOL.3's justification of the
  `b'(x) > 0` bracket ("after multiplication by sinh y cosh y, two
  differentiations...") differs from the one-differentiation route this
  referee derived (multiply by sinh y; psi' = 3 sinh y (sinh 2y - y) > 0);
  the ASSERTION is true (verified symbolically/numerically), the wording of
  the reduction is for the maths referee to accept or tidy. Same for the
  h3'-logarithmic-derivative identity `3/x - coth(x/2) - 1/sinh x`, which I
  verified analytically (equals `3/x - (cosh x + 2)/sinh x`).

## 6. Verdict

**MINOR_REPAIRS.** All fourteen (S1) constants the re-architected chain
consumes are proved by the draft's argument and are now INDEPENDENTLY
CERTIFIED end-to-end at this referee's maximal bar: exact-symbolic
recurrences, brute-force-validated cumulant engine, rigorous
outward-rounded interval re-certification of every band cell, pointwise
envelope-vs-truth falsification at 104 adversarial probes, and the
truth-under-ceiling sweep at ~170 more — zero violations anywhere. The
chain certificate consuming these constants closes at `C*(m >= 561) =
19.5659 <= 20` (arithmetic re-verified; the plan's row recomputation itself
still owes its separate referee pass, plan §9). Required repairs: F1
(certificate-of-record provenance) and F2 (restore the `lam in (4/m, 0.89]`
range in the statement); both are text-level. This numerics pass finds NO
grounds for refutation. (S1)'s status upgrade further requires the parallel
MATHS referee pass per the two-referee house rule.

*End of referee_numerics_sol_s1.md.*
