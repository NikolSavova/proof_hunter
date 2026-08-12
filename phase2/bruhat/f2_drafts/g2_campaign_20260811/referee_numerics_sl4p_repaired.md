# referee_numerics_sl4p_repaired — adversarial numerics referee report on `wave4_sl4p_repaired_20260812.md`

*Wave-5 referee pass, F2 campaign, 2026-08-12. Target:
`wave4_sl4p_repaired_20260812.md` (the repaired SL4' kernel-weighted
assembly) and its scripts
`g2_scripts/campaign_20260811/wave5_sl4prepair/sl4pr_common.py`,
`sl4pr_a_trapezoid.py`, `sl4pr_b_grid.py`, `sl4pr_c_xtail.py`,
`sl4pr_d_misc.py` (outputs `out_sl4pr_{a,b,c,d}.txt`). Mandate: verify
every finding F1–F8 of `referee_numerics_wave4_sl4p.md` is actually
resolved or rigorously mooted; re-run all scripts; off-grid adversarial
probes on the previously-broken trapezoid region. Protocol: maximal bar,
DEFAULT TO REFUTATION. Also read: `STATUS_wave4.md` (ledger),
`wave4_sl4p_20260812.md` (the original), the original referee report and
its archived outputs (`referee_wave4_sl4p/out_ref_nw4p_{a,b,b2,c,d,e}.txt`),
`wave4_sl3p_20260812.md` (the consumed Theorem SL3'),
`wave4_sliver_20260812.md` (the consumed SLV.2/SLV.3), harness results
files (parsed, not modified). `g2_draft_t1_20260803.md` NOT read; blind to
any other wave-5 deliverable's content beyond what STATUS_wave4 licenses.
New referee scripts (all SAVED and RUN 2026-08-12, outputs archived beside
them) in `g2_scripts/campaign_20260811/referee_sl4p_repaired/`:
`ref_rp_a_offgrid_trap.py`, `ref_rp_b_gridgaps.py`, `ref_rp_c_R1R2.py`,
`ref_rp_d_misc.py` (outputs `out_ref_rp_{a,b,c,d}.txt`). No existing file
modified.*

## VERDICT: **MINOR_REPAIRS**

**Every original finding F1–F8 of `referee_numerics_wave4_sl4p.md` is
actually resolved in the repaired file — verified independently, not just
re-quoted — and the two theorem-statement defects (F1/F2) are additionally
mooted in the CL assembly exactly as Corollary R.3 claims (parse
re-verified by a second method).** All four repair scripts re-run
byte-identical; the previously-broken trapezoid region survived 2,790
off-grid probes above the true (bisected) crossings with ZERO failures;
Fact R.G's range survived 3,594 additional off-grid/gap/random probes with
ZERO failures; the new Lemma R.1 floor was rebuilt independently at dps 60
with denser cells (min bound RISES to 0.01773513 at 2,740 cells) and
attacked with an 11,256-point direct-truth minimization (global min
0.01775542 >= 0.0176, at the predicted corner); Lemma R.2's constants,
cancelation, and monotonicity all re-derive exactly (my independent
rowbound(700) = 0.91140651 vs the prover's 0.911407). Nothing I found
moves a constant, a bound, or a verdict. Two text-level defects (RF-1
display-rounding of the efac boundary in the unsafe direction, RF-2 an
inexact "byte-faithful" provenance claim) plus trivia keep this at
MINOR_REPAIRS rather than SURVIVES. The remaining honesty surface
(SL1'-w, SL4'-E, SL4'-X on `[561, 699]`, grid-certificate classes, zero
referees at filing, the missing maths referee) is declared correctly in
the file itself.

## 1. Reproduction (re-run everything)

- **Byte-identity of outputs.** All four repair scripts re-run
  byte-identical to their archived outputs (`diff` exact):
  `sl4pr_a_trapezoid.py`, `sl4pr_b_grid.py` (the full 25,122-probe grid),
  `sl4pr_c_xtail.py`, `sl4pr_d_misc.py` — "A/B/C/D BYTE-IDENTICAL".
  Every §5/§6/§7 number quoted in the draft traces verbatim to those
  outputs (checked line-by-line for the §7 "key verbatim output" column
  and the §5.1/§5.2/§5.3/§5.4/§5.5/§6 code blocks; the §5.1 block's
  ellipses are visible condensation of real lines). Nothing fabricated.
- **Provenance of `sl4pr_common.py`.** Diffed against the prover's
  `sl4p_nc1_ledger.py` lines 12–103: ONE line differs — the `efac`
  comment was silently updated from "`<= e iff C5 <= 0.8464`" to
  "`<= e iff C5 <= 4(1-e^{-1/4})`" (the F5-corrected text). Zero
  functional difference (a comment), but the header's claim "byte-faithful
  copy ... the ONLY changes are (a) removal of the prover's print blocks
  [0]-[5], (b) nothing else" is inexact — finding RF-2. The functional
  code (constants, BANDS, all entry functions, `w6_x`, `X_w6`, `far_ent`,
  `row`) is character-identical, and this machinery was independently
  rebuilt from the draft's closed forms to `< 5e-5` in the wave-4 pass
  (`ref_nw4p_a_rebuild.py`, archived) — so all rows here stand on a
  twice-validated engine.
- **Consumed statements verified at source.** Theorem SL3'
  (`wave4_sl3p_20260812.md` header block): `gamma* = 0.42/0.42/0.40/0.40/
  0.38/0.34/0.32`, `m >= 401`, `|lam| in (4/m, 0.89]`, `0 < t <= 0.8
  |lam|` — exactly the levels and domain the repaired file consumes (the
  ledger's mid slot needs `[lam/2, 0.8 lam]`, a subset). Cor SLV.3
  (`wave4_sliver_20260812.md`): CL obligation shifts to `m >= M_H + 1 =
  561` — as consumed in §6. Both are citable at two-referee MINOR_REPAIRS
  per STATUS_wave4 §1.

## 2. F1–F8 resolution audit (finding-by-finding)

| Finding | Required repair (wave-4 report §4) | Resolution in the repaired file | Referee verification | Status |
|---|---|---|---|---|
| **F1** (MAJOR) | route (a) or (b); make everything consistent | Route (a)+: the SL3' input is now the PROVED Theorem SL3' at `gamma*(W1) = 0.42` — hypothesis DISCHARGED, not merely restated; "0.25 suffices" rescoped to W2–W4 and `w >= 4.14` on W1; route (b) kept on record | Consumption levels match the SL3' source verbatim (§1); the certified ledger/trapezoid/blocks were already at 0.42 (wave-4 [E1] confirmed); route-(b) numbers 4.135/470 re-run byte-identical and match my wave-4 E2/E3; full-text scan: NO surviving instance of an unscoped "0.25 suffices on W1" | **RESOLVED** |
| **F2** (substantive) | `[401, 461] -> [401, 462]`; tell the handoff `m = 462` carries `(4, 4.00021]` | Corrected everywhere (§0/§1/§4/§5.1/§6/§8): trapezoid `[401, 462]`, `w†(462) = 4.00021`, first sliver-free `m = 463`, explicit handoff sentence | Sharpest probes: `row(461, 4+1e-15) = 1.01282` FAIL, `row(462, 4+1e-15) = 1.0019` FAIL, `row(463, 4+1e-15) = 0.991128` PASS — first PASS at the open edge is 463 ([A4]); true crossing `wc(462) = 4.00020331 in (4.0002, 4.00021]` by bisection, `row(462, 4.00019)` FAILs, `row(462, 4.00021)` PASSes ([A3]) | **RESOLVED** |
| **F3** | scope/correct "never above 0.65" | Corrected to "never above 0.66; worst 0.6579 at the W1 right edge `w = 5`" with the edge/corner probe set | [D-repair] re-run byte-identical (worst 0.6579 at (401, 5.0)); MY new probes at Fact R.G's load-bearing `m` (463/561/699, incl. right edges): worst `0.65778` at (463, 5.0) — still `<= 0.66`, pricing holds with `>= 34%` headroom, `kappa_4 > 0` at all 7 new points ([my D1]) | **RESOLVED** (and robust off-sample) |
| **F4** | scope the C5*-slack remark; fix "2x–8x" | Rescoped: W1's 0.4 is `w = 4.30`-class (FAILs at 4.10: 1.4695), slack "1.6x–8x on W1–W4 and W6b", W5 acceptance = 0.15 with the 0.10 grid-artifact explained | Repair [D5] re-run byte-identical; MY spot-checks of the OTHER bands' acceptance claims: W2@0.2 = 0.977534 PASS, W3@0.4 = 0.915428 PASS, W4@0.4 = 0.76794 PASS (and W3/W4 @ 0.8 FAIL — the stated ceilings are honest) ([my D4]); slack arithmetic 0.4/0.25 = 1.6x, 0.4/0.05 = 8x correct | **RESOLVED** |
| **F5** | print the true boundary or drop "iff" | §4 note: "`efac(C5*) <= e iff C5* <= 4(1 - e^{-1/4}) = 0.88480`"; 0.8464 kept as the safe working cutoff | Exact boundary re-derived: `4(1-e^{-1/4}) = 0.884796867714`; `efac(0.8464) = 2.58829 < e` confirmed. Residual nit: the 5-dp display `0.88480` rounds UP past the boundary — `efac(0.88480) = 2.71829276 > e` ([my D2]) — see RF-1 | **RESOLVED** (display nit RF-1) |
| **F6** | fix "A >= 32"; state the `e(A)/A` rule | Lemma SL4'.8' restated: inc entries require `e_j(A)/A` nondecreasing (far exactly linear, X `~ A^{5/2}`); dec entries per-entry thresholds (mid tier-1 peak `~36.7`, pure-form `6/g = 45.5581`; tier-2 X `26.9087`) + used-range scan `[112, 3000]` | Repair [D3] re-run byte-identical (all four scans True); MY finer scan: peak at `A = 36.66`, `e_midn(0.1317, ·)` strictly nonincreasing on `[45.5581, 200]` step 0.01, thresholds `45.558087`/`74.224022` re-derived ([my D3]) | **RESOLVED** |
| **F7** | reprint with convention or drop "share 0.68" | RETIRED; replaced by the explicit-convention decomposition X/far/dec = 0.99538/0.12144/0.27429, total 1.3911, `m x(4.05, 0.8) = 7.6453` | Matches my wave-4 [D1] values (0.9954/0.1214/0.2743, 1.3911) to print precision; re-run byte-identical | **RESOLVED** |
| F8 (record-only) | none forced | `4.095` (3 dp) used directly; `74.224` derivation shown; W5 range clause added; `19.78`/`3.57x` conventions unchanged | `w†(401)` true crossing = `4.0948783` by bisection — 4.095 is its 3-dp value, safe direction ([A1]) | **FOLDED IN** |

**Mootness of F1/F2 (Cor R.3 item 1) — verified, not just re-quoted.** My
independent split-based parse (different method from the repair's regex,
[my D5]): `results_m540.txt` = 478 data rows `m in [4, 481]`,
`results_m560.txt` = 79 data rows `m in [482, 560]`, overlap EMPTY, union
557 rows, ZERO non-PASS, ZERO gaps in `[4, 560]` (a fortiori `[401,
560]`); rows `m = 461/462/463` printed verbatim, all PASS; the
`# OVERALL: PASS ... 4 <= m <= 560` line is present verbatim. Both
corrected trapezoids (max `m` = 462 route (a), 469 route (b)) lie inside
`[401, 560]`; the first sliver-free `m` (463 / 470) is `< 561`. The
draft's scope-honesty clause (item 3: consumer-level discharge, not
lemma-level CL on `[401, 560]`) is stated correctly.

## 3. Off-grid adversarial probes on the previously-broken trapezoid region

All via `ref_rp_a_offgrid_trap.py` / `ref_rp_b_gridgaps.py` (outputs
archived; key lines quoted verbatim):

1. **True crossings by bisection (tol < 1e-13), EVERY `m in [401, 462]`.**
   `wc(401) = 4.0948783`, `wc(430) = 4.0411603`, `wc(461) = 4.0013685`,
   `wc(462) = 4.00020331`; every crossing genuine (FAIL at `wc - 1e-6`,
   PASS at `wc + 1e-6`; 0 exceptions); `wc` nonincreasing; and the
   theorem's grid `w†` is SAFE-DIRECTION at every single `m`:
   `wc(m) <= w†_grid(m)` for ALL 62 values, with gap `< 0.001` (the grid
   step) — so the displayed `T` is a superset of the true exception set,
   exactly as §5.1 claims.
2. **One-crossing attack, off-grid (the F1/F2 failure mode).** 2,790
   probes strictly above the true crossing (5 adversarial offsets
   `wc + {1e-6, 3.7e-4, 6.3e-4, 1.7e-3, 0.0505}` plus 40 seeded random
   `w in (wc, 5]` per `m`): **0 failures**; the largest row above a
   crossing is `0.999993` at `(401, wc + 1e-6)` — i.e. the boundary is
   exactly where it should be and nothing re-fails above it, at any
   off-grid point probed.
3. **Edge ladders.** `w = 4 + eps`, `eps = 1e-15 .. 1e-3`: `m = 461`
   all-FAIL, `m = 462` FAIL until its micro-crossing (PASS at `4.001`),
   `m = 463` all-PASS with the ladder nonincreasing in `w` — the open-edge
   max claim of Fact R.G is real, and the first `m` passing at
   `w = 4 + 1e-15` is **463**.
4. **Fact R.G gap probes, EVERY `m in [463, 699]`.** 12 off-grid `w`
   strictly between the repair's 106 probe points near the edge
   (`4 + 3e-10` … `4 + 7e-3`): 2,844 probes, **0 failures**, max
   `0.991128` at `(463, 4+3e-10)` (the known thin point). Plus 500 seeded
   log-scaled random `(m, w)`: **0 failures**, max `0.970703` at
   `(464, 4.0010848)`. Plus a dense 250-point edge scan at `m = 463`
   (`w = 4 + k·2e-6`): **0 failures**, strictly nonincreasing. The
   SL4'-X monotone-in-tau flag held at ALL 3,594 of these additional
   evaluations (plus the 2,790 of item 2 via the same `row` engine).

**Conclusion:** the previously-broken region is now correctly quantified;
the corrected constants (`4.095`, `[401, 462]`, `4.00021`, first-free
463) survive off-grid attack in every direction I could construct.

## 3b. Attack surface note (what a FAIL would have meant)

A single `row > 1` above a bisected crossing (item 2), in a gap (item 4),
or at an edge-ladder point of `m >= 463` (item 3) would have refuted the
theorem's exception clause or Fact R.G outright and forced MAJOR_ISSUES
again. None occurred.

## 4. The new content: Lemma R.1 / Lemma R.2 / Fact R.G / Corollary R.3

All via `ref_rp_c_R1R2.py` (independent code written from the DRAFT TEXT
of §5.3/§5.4, dps 60) plus §2/§3 above.

- **Lemma R.1 epsilon audit (re-derived):** `theta_max^2/6 = 3.8177862e-6
  <= 4e-6` TRUE; `(lam/2)_max^2/5 = 3.9717718e-6 <= 4e-6` TRUE;
  `(1-epsM)^2/(1+epsS)^2 = 0.999984000128 >= 0.999983` TRUE. The two
  elementary brackets checked on 1000-point grids: `sin(th) >=
  th(1 - th^2/6)` on the used range and `sinh(x) <= x(1 + x^2/5)` on the
  FULL claimed range `(0, 1]` — no violation. The bracket logic itself is
  sound as displayed: the cell bound needs only `log(1+r)` increasing in
  `r`, `r/M <= r_hi/M1`, and `(M-1)/(2M)` increasing in `M` with
  `M1 = 1.5999936 > 1` — it does NOT need (and does not claim) `d/dr` of
  the second factor to have a sign, which is good because `1/(1+r) - 1/M`
  changes sign on the domain.
- **Lemma R.1 cell certificate (independent rebuild):** at the prover's
  548 cells my minimum cell bound is `0.0176601` at `tau1 = 0.8` —
  matches; at 2,740 cells (width 1e-4) the minimum RISES to `0.01773513`
  — the 0.0176 floor is real with `>= 0.9%` certificate headroom and
  `>= 0.75%` grid-refinement stability. Direct truth attack: 11,256-point
  minimization of the true `x(w, tau; m)` over `m in {561, 562, 600, 699,
  700, 1000, 1e4, 1e6}` x 7 `w`-values (incl. `4 + 1e-12`) x 201-point
  `tau` grids: global min `0.01775542` at `(561, 4+1e-12, 0.8)` — above
  the floor, at the predicted corner, matching the draft's `0.0177554`.
- **Lemma R.2 (re-derived, own code):** `K_Xn = 0.1933096692 <= 0.19332`,
  `K_Xd = 0.2186203697 <= 0.21863` (dps 60); the `w`-power cancelation
  `m (m^3/w^2)^{3/2} lam^3 = m^{5/2}` verified EXACT (to 1e-50 relative)
  at 3 samples; `B(m)` strictly decreasing on `[700, 3000]` step 1; my
  independent `rowbound(700) = 0.91140651` (prover 0.911407, lemma bound
  0.9115 — holds); rowbound strictly decreasing on `[700, 1500]` step 1;
  and the crude bound dominates the actual `X_w6` slot at off-sample
  points (`(750, 4.2)`: 0.0028 vs 5.52; `(700, 4.000003)`: 0.3498 vs
  11.20). The "grid rung genuinely needed below 700" arithmetic
  (`B(561) = 74.389` vs slot `~12.475`) reproduces byte-identical in the
  re-run.
- **Fact R.G:** grid-certificate class, correctly flagged as such;
  strengthened by my §3 item 4 (3,594 additional probes, 0 failures, 0
  SL4'-X flag violations). The complete-integer `m`-quantifier claim is
  real (every `m in [463, 699]` probed by both the prover and me).
- **Corollary R.3:** parse independently verified (§2 bottom); the
  assembled-statement arithmetic (trapezoid max-`m` vs 560; `[561, 699]`
  grid rung margin 57.5%; `m >= 700` analytic rung margin 8.8%) all
  re-derives. Scope-honesty item 3 correctly mirrors the sliver note's
  consumer-vs-lemma distinction.

## 5. Findings (ranked; none moves a constant, bound, or verdict)

### RF-1 (minor — efac boundary display rounds past the boundary in the unsafe direction)

§4's note states "`efac(C5*) <= e iff C5* <= 4(1 - e^{-1/4}) = 0.88480`".
The exact closed form makes the "iff" TRUE, but the displayed decimal
rounds UP: `4(1 - e^{-1/4}) = 0.884796867714` and `efac(0.88480) =
2.71829276 > e` ([my D2]) — a consumer who reads the 5-dp decimal as the
cutoff crosses the boundary by `~3.1e-6` (efac excess `~4e-6` relative).
Zero load anywhere (the lemma's working cutoff is 0.8464, W7 sits at
0.80), but the wave-4 F5 defect was precisely a wrong "iff" constant, so
the repair should not reintroduce a rounding of the same flavor. Repair
(one word): display `0.884796...` truncated, or write "`= 0.88480`
(rounded; the safe working cutoff remains 0.8464)".

### RF-2 (minor — provenance claim of `sl4pr_common.py` is inexact)

The module header (and draft §7 [common] row) claims a "byte-faithful
copy of the prover's ... lines 12–103; the ONLY changes are (a) removal
of the prover's print blocks, (b) nothing else". Diff shows one
additional change: the `efac` comment line was updated to the
F5-corrected boundary text. Functionally irrelevant (comment only; all
code character-identical), but under house no-silent-edits discipline the
provenance sentence must list it. Repair: one clause.

### RF-3 (trivia, record-only)

- Script [B]'s output label "25122 evaluations x 60 cells" for the
  SL4'-X flag: each evaluation compares 59 consecutive left-endpoint
  pairs (60 points), so "x 59 comparisons" (or "60 points") is the
  precise phrasing. No number affected.
- §5.2's argmax note is correct (`4.0` is the 8-significant-digit
  rendering of the probe `4 + 1e-9`) — verified by reproducing the
  `mp.nstr` behavior; keeping the parenthetical is the right call.
- The true micro-window at `m = 462` is `(4, 4.00020331]` (bisection);
  the displayed `(4, 4.00021]` is its 1e-5-grid superset — safe
  direction, consistent with the draft's own "at or below" sentence.
  No text change needed.

## 6. What survived adversarial attack (for balance — all clean)

1. The corrected trapezoid boundary: 62 bisected true crossings, all
   `<= w†_grid` with gap `< 0.001`; 2,790 off-grid probes above the
   crossings, 0 failures ([A1]/[A2]).
2. F2's off-by-one at the sharpest possible probe (`w = 4 + 1e-15`):
   461 FAIL / 462 FAIL / 463 PASS ([A4]).
3. Fact R.G under gap/random/dense-edge attack: 3,594 probes, 0
   failures, 0 SL4'-X flag violations; worst point confirmed at
   `(463, 4+)` with margin 0.9% ([B1]–[B4]).
4. Lemma R.1 under independent rebuild (dps 60, 5x denser cells) and an
   11,256-point truth minimization: floor holds with headroom; corner
   truth `0.0177554` reproduced ([C3]/[C4]).
5. Lemma R.2's constants, exact cancelation, `B`/rowbound monotonicity,
   and the 0.9115 tail bound, re-derived from the draft text alone
   ([C5]).
6. SL4'-E pricing at seven NEW W1 points in the load-bearing range
   `m in {463, 561, 699}` incl. right edges: all `<= 1`, worst `0.65778
   <= 0.66`, `kappa_4 > 0` everywhere ([my D1]) — the F3-corrected
   sentence is robust off-sample.
7. The §2 acceptance-slack claims for the bands the repair scripts did
   NOT re-check (W2@0.2, W3@0.4, W4@0.4 PASS; W3/W4@0.8 FAIL — ceilings
   honest) ([my D4]).
8. The harness parse by a second method: 478 + 79 rows, no overlap, no
   gaps, no non-PASS, OVERALL line verbatim ([my D5]).
9. All four repair scripts byte-identical on re-run; every draft quote
   traced.

## 7. Referee script table (all SAVED and RUN 2026-08-12; outputs archived beside them)

| # | script (`g2_scripts/campaign_20260811/referee_sl4p_repaired/`) | what it does | key output |
|---|---|---|---|
| RP-A | `ref_rp_a_offgrid_trap.py` (`out_ref_rp_a.txt`) | bisected true crossings all `m in [401, 462]`; safe-direction + grid-gap checks; 2,790 off-grid one-crossing probes; `m = 462` micro-window; edge ladders 461/462/463 | `SAFE DIRECTION ... ALL m: True`; `probes above the true crossing: 2790; FAILs: 0`; `wc(462) = 4.00020331`; `first m with PASS at w = 4+1e-15: 463` |
| RP-B | `ref_rp_b_gridgaps.py` (`out_ref_rp_b.txt`) | Fact R.G gap probes (12 x 237), 500 random log-scaled `(m, w)`, dense edge scan at 463; SL4'-X flag audit | `probes: 2844; FAILs: 0`; `max ... 0.991128 at (463, '4+3e-10')`; random `FAILs: 0`; dense scan `FAILs: 0`, nonincreasing True; flag violations `0` |
| RP-C | `ref_rp_c_R1R2.py` (`out_ref_rp_c.txt`) | independent (from-text) R.1 epsilon audit + cell certificate at 548 and 2,740 cells + 11,256-point truth attack; R.2 constants/cancelation/monotonicity/rowbound re-derivation | `548: min bound = 0.0176601`; `2740: min bound = 0.01773513`; `global min x = 0.01775542 at (561, '4.0', '0.8')`; `rowbound(700) = 0.91140651 <= 0.9115: True`; both monotonicity scans True |
| RP-D | `ref_rp_d_misc.py` (`out_ref_rp_d.txt`) | eta at 7 new W1 points; efac display-rounding probe; e_midn peak/threshold; W2–W4 C5* acceptance; independent split-based harness parse | `worst = 0.65778 at (463, '5.0') ... <= 0.66: True`; `efac(0.88480) > e: True`; `peak ... A = 36.66`; W2/W3/W4 acceptance PASS; `union rows: 557 ... gaps ... NONE`; OVERALL line verbatim |

Re-run verification (no new script): `diff` of each freshly-generated
output of `sl4pr_{a,b,c,d}` against its archive — all four byte-identical;
`diff` of `sl4pr_common.py` vs `sl4p_nc1_ledger.py` lines 12–103 — one
comment line (RF-2).

## 8. Required repairs (to reach citable-with-maths-referee state)

1. (RF-1) One-word display fix on the efac boundary (§4 note).
2. (RF-2) One clause in the `sl4pr_common.py` provenance sentence (§7
   [common] row and the module header's claim as quoted in the draft).
3. (RF-3) Optional trivia; no obligation.

House-rule reminder (unchanged from the draft's own §8): this file still
owes its MATHS referee — this report is the numerics re-grade only, and
MINOR_REPAIRS here does NOT by itself make the file citable.

*End of referee_numerics_sl4p_repaired.md.*
