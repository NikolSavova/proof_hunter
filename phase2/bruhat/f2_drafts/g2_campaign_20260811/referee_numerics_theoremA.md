# Adversarial NUMERICS referee report — `theoremA_assembly_20260811.md`

*Wave-3 numerics referee pass (2026-08-12). Target: the merged Theorem A
assembly note (the designated referee unit for the cross-package plug).
Protocol: (1) re-run the document's saved script byte-for-byte against its
archived output; (2) independently re-derive the plug arithmetic and every
§4/§6 number in exact `Fraction` arithmetic with DIFFERENT code (separate
script, separate harness algorithm); (3) full re-run of the cited harness
`run_m200.py --mmax 400` against its archived results; (4) spot-check the
§6 constant ledger line-by-line against the cited source files. Per the
campaign brief, CL's conditionality is NOT penalized — the reduction is
what is verified. Blind rule respected: `g2_draft_t1_20260803.md` and all
wp4 files unread by this referee. No existing file modified; this report
and `referee_numerics_theoremA_scripts/` are new.*

**VERDICT: MINOR_REPAIRS** — every load-bearing number reproduces exactly
(the document's script byte-identical; the full m = 400 harness re-run
byte-identical modulo the timing line; an independent exact re-derivation
with different code confirms every §4 block, all three H(K, M(K)) values,
and both crossovers, and extends several scans beyond the document's);
the constant ledger traces row-for-row to sources with all roundings in
the safe direction; the plug is verified as a unit. The repair list
(§5: N-F1–N-F3) is display/text-level only — no constant, threshold,
verdict, or conditional moves. Citable modulo those repairs, per the
campaign house rule.

## 1. Script reproduction (the document's own script)

`f2_drafts/g2_scripts/campaign_20260811/theoremA_assembly/assembly_checks.py`
re-run 2026-08-12 (python3, this machine): **stdout is byte-identical to the
archived `out_assembly_checks.txt`** (`diff` empty). All `True` verdicts
reproduce; no float drift anywhere (verdict path is exact
`Fraction`/integer as claimed).

**However, the §4 block labeled "Verbatim script output" is NOT verbatim** —
it is a condensed excerpt of the archived output. Diff against the real
output: (i) A1's second line (`D.5 band |w| <= 4 == R3 band ... True by
statement`) dropped; (ii) block C5's concluding line (`=> Lambda* = 0.89
covers every residual-band tilt (Lemma P.8): True`) dropped; (iii) block D's
header parenthetical (`(positivity => w^2 term discardable)`) and its limit
line (`limit 6.85*E(4) = 0.017056 ...`) dropped; (iv) block E's `m= 4
argmin= 2` and `m=60 argmin= 885` rows dropped; (v) block F's `m = 30` and
`m = 1581` rows dropped and the surviving two rows merged onto one line;
(vi) A3 reflowed onto two lines. Every number that IS shown matches the
archive exactly, and nothing dropped changes any claim (the dropped lines
are all additional PASSes). This is the same display class as wp3-a2's
repair F7 ("verbatim excerpts are condensed") — finding N-F1, §5.

## 2. Independent re-derivation of the plug and §4 blocks

Script: `referee_numerics_theoremA_scripts/ref_indep_checks.py` (SAVED, RUN;
output archived beside it as `out_ref_indep_checks.txt`). Deliberately
different code paths: `S_4` from a raw exact power sum (cross-checked
against the closed formula the assembly uses — equal at
m = 4/30/180/367/401/1581); Mahonian polynomials via a prefix-sum window
recurrence (not the assembly's in-place running sum); crossover scans from
`m = 5`; `e^0.89` recoded at 25 terms; constants re-transcribed from the
SOURCE files, not from the assembly. Exact `Fraction` arithmetic in every
verdict. Results, block by block against the target's §4:

| target claim | independent result | match |
|---|---|---|
| A1 `M(4) = 367 <= 401` | True (wp2-a2 D.5 threshold table re-read) | YES |
| A2 grid `C_A = 37815.3642`, R3 bound at 401 `= 0.762141 > 0` | exact rational `4434031708853/5817860580...` (script-truncated print) = 0.762141 | YES |
| A2 closed `C_A = 37997.8442`, bound `0.761006 > 0` | 0.761006 | YES |
| A3 bound increases to 1 | STRONGER check: `1 - B_m - C_A/m^2` itself strictly increasing on [401, 3001], exact | YES |
| B crossovers `m* = 535 / 537 / 22` | scans from m = 5 (not 30/6): 535 / 537 / 22, each with `m*-1` strictly below and 500-wide persistence | YES |
| B footnote (STATUS_wave2 printed 30 for K=1) | `status_wave2_checks.py` line 45 indeed starts its scan at 30 — the assembly's explanation is correct | YES |
| C1 `v(7/10)*401 = 47719/600 = 79.5317 >= 79`; `v(1)*1581 = 527` | exact, `v(7/10) = 119/600` confirmed | YES |
| C2 `eps* = 1291739/5000000 = 0.2583478` | exact match | YES |
| C3 budgets `20/79.5 = 0.251572 <= eps*`; `136/527 = 0.2580645 <= eps*`, margin `2.833e-4` | exact; PLUS `137/527 = 0.2599620 > eps*` (136 is genuinely the max integer C* on band 2, matching wp3-a2's table); actual spec `C* = 20` gives `20/527 = 0.038` — 6.8x slack on band 2 | YES |
| C4 R2 conclusion `1.029318 >= 1.02` | exact | YES |
| C5 `e^{0.89} > 2.4351 > 17/7 > 2` | 25-term exact partial sum, same digits `2.435129651`; both cap inequalities True (positive-series lower bound is a valid one-sided proof) | YES |
| D bracket `0.009575 / 0.009556` at 401, positive on [401, 2000] | exact; PLUS strictly increasing on the scan, `br(3000) = 0.016520`, `br(5000) = 0.016752`, limit `6.85 E(4) = 0.017056` — comfortably clear of 0 beyond the scan | YES |
| F `H(4, 367) = 0.3321 <= 1/2` | ALL THREE recomputed from wp2-a2's exact assembled `C_R` closed values (41.1647/230.0864/37997.4722): `H = 0.0097 / 0.0241 / 0.3321` | YES |
| F `B_m m -> 1.08` | reproduced; PLUS `(27/25 - B_m m) m in (0.34, 0.54]` exactly on `[30, 2000] + {3e3, 5e3, 1e4, 1e5}` — so `B_m m < 1.08` throughout (g1_b B.0(ii) direction) and the §0 recentering remainder is `<= 0.54/m^2` (finding N-F2) | YES |

**Plug-chain algebra re-derived by hand** (not just the numbers): with
T.9-final at `K = 4` (`c_w(4) = 1`), `s2(r-1) >= 1 - B_m(1 + w^2) -
[PW + T + Lin + C_ker]/m^2 = 1 - B_m(1 + w^2) - C_A/m^2` — `Lin` enters
exactly once since `C_A := C_R^PT(4) + C_ker(4)` and `C_R^PT = PW + T + Lin`
(repair F3 correctly applied; cross-check `C_R(4) = PW + T + C_ker =
37997.4722` exact vs `C_A closed = 37997.8442 = that + 0.372`). Then
`lambda(r-1) = (lambda/s2) s2(r-1) >= (1 + D) X` with `X = 1 - B_m(1 + w^2)
- C_A/m^2 > 0` at `m >= 401` (X ~ 0.72 at the w-edge) and `D = 1 - s2/lambda
>= 6.85 E(4) w^2 >= 0`, giving `>= 1 - B_m - C_A/m^2 + w^2 [6.85 E(4)(1 -
17 B_m - C_A/m^2) - B_m]`, discardable once the bracket is positive (block
D). Algebra checks out; the `>= 0` requirement on the inner factor
`1 - 17 B_m - C_A/m^2` (0.719 at m = 401) is implied by the bracket scan.

R1a/R1b margins re-checked (`ref_r1_margins.py`, exact Fractions):
`lambda(401) = 5393450/3` exactly; R1a `lambda (m-1)/(2(m+1)) = 894436.2
>= 10^5` (doc row: `>= 10^5`, safe); R1b worst case at continuous
`k = cm = 280.7`: `1879.06 >= 1879` -> doc's floor 1879 is the safe
continuous-k value; integer `k <= 280` gives 1885.7. Consistent with
wp3-a2 NC-P4's "1879x".

## 3. Harness re-run and independent rebuild

**Full re-run of Part I's citation.** `run_m200.py --mmax 400` re-run in
full by this referee (2026-08-12, 303.9 s; re-run results archived as
`referee_numerics_theoremA_scripts/results_m200_rerun_referee.txt` — the
original `results_m200.txt` untouched): the results file is
**byte-identical to the archive except the `# elapsed:` line** (320.9 ->
303.9 s; timing, not mathematics). Verbatim summary of the re-run:

```
# rows: 397, failures: 0
# OVERALL: PASS -- all of C1..C6 hold exactly for 4 <= m <= 400 (C2/C3 with the known m=4 exception).
#   varfit(6) = 0.865740740741
#   varfit(40) = 0.973380789453
#   varfit(400) = 0.997302329987
```

All thirteen checkpoint varfit values (6/40/143/150/151/189/190/200/266/
267/378/379/400) match the harness report's quoted digits exactly,
including the assembly's §2.1 citation `varfit(400) = 0.997302329987`.

**Independent rebuild (different algorithm).** `ref_indep_checks.py` block
R7 rebuilds the Mahonian coefficients by a prefix-sum window recurrence
(not the runner's running-sum convolution) and re-certifies
argmin-centrality, min = central, C5 (with the m = 4 exemption and the
m = 6 equality case), and strict increase, on `4 <= m <= 80` — beyond the
assembly's own re-anchor range (m <= 60): 0 failures, `varfit(4) = 91/108`
and `varfit(5) = 7/8` exact, `varfit(6) = 187/216` exact,
`varfit(40) = 0.973381`, `varfit(60) = 0.982146`, `varfit(80) = 0.986575`.
The assembly's §2.1 numbers all confirm.

## 4. Constant-ledger spot-checks against sources (§6 of the target)

Every §6 row was traced to its cited source file (line-level grep/read, this
session). Verdict per row:

| §6 row | source check | verdict |
|---|---|---|
| `B_m = (S_4 - m)/(240 lambda^2)`, `-> 27/25` | `F2_PROOF_DRAFT.md` line 17, identical display | OK |
| `187/216` attained m = 6, scope m >= 5; `varfit(4) = 91/108`; `varfit(5) = 7/8` | F2 correction 1 (lines 41–44) + independent rebuild (§2, R7: both fractions exact) | OK |
| Cor 2.3 error `1.1 / 1.2 / 1.8`, `m >= 180` | `g1_draft_b.md` §7 item 3 (lines 605–611): `|E| <= 1.1/m^2 + B_m y_c^2 <= 1.2/m^2`, `1.2 + 0.6 = 1.8`, `m >= 180` — verbatim | OK |
| `B_m in [1.068, 1.080]/m`, m >= 30 (B.0(ii)) | `g1_draft_b.md` line 69 verbatim; independently confirmed `B_m m < 1.08` on scan (§2) | OK |
| `c_1(K) = 0.2259/0.1802/0.1019` | `wp1_draft_c.md` lines 122–123 (W.4(i) display) | OK |
| far floor `0.0372 m` all `|lam| <= 1.7627`; `0.0373` on W.5(ii) | `wp1_draft_c.md` lines 136–142: `c_V = q(1.5700, 1.00183) = 0.0372` unified floor; `q(pi/2, 1) = 0.0373` on (ii) — both as quoted | OK |
| `m_2(K)` proxies `143/190/267/379` retired | matches wp1-c §6 / `run_m200.py` header; superseded by `M(K)` | OK |
| `c_1/c_2/c_4` floors `0.967/0.868/0.60` | `wp2_draft_b.md` line 133 verbatim | OK |
| `c_w = 0.407/0.466/1` | wp2-b's original display has `c_w(4) = 0.951` (line 349); repair B2 (`repairs_20260811.md` §B2) replaces it by the safe `c_w(4) = 1` — the assembly quotes the REPAIRED value, correctly | OK |
| `PW` grid `1.5491/4.0889/4.9126`, closed `10.278/21.063/187.414` | wp2-b lines 416–418/531–534 verbatim | OK |
| `C_R^PT(4)` grid `5.32 = 4.93 + 0.01402 + 0.3719` | `repairs_20260811.md` §B3 (lines 177–179) verbatim; sum = 5.31592, round-up safe | OK |
| `C_ker(K) = 30.89/209.03/37811` at `M(K) = 180/181/367`; table value `37810.0442` | `wp2_draft_a2.md` Theorem D.5 (line 61) + NC-A5 table (line 696–698) | OK |
| `C_R(K)` closed `41.17/230.09/37998`, grid `32.44/213.12/37815` | wp2-a2 NC-A5 exact assembled values `41.1647/230.0864/37997.4722` and `32.4358/213.1123/37814.9708` — every display is a round-UP (safe). (My earlier concern that `21.063 + 0.001 + 209.03 = 230.094 > 230.09` is an artifact of summing already-rounded displays; the exact assembled 230.0864 governs.) | OK |
| `m^2 Lin(K, 180) = 0.2308/0.2571/0.3719` | wp2-b table lines 416–418 | OK |
| `H(K, M(K)) = 0.0097/0.0241/0.3321` | wp2-a2 NC-A5(2) + all three independently recomputed (§2) | OK |
| T.9-Step2' `0.362 / 0.452 < 0.5` | `repairs_20260811.md` §T1 (lines 302–326) | OK |
| `C_P(c) = 12.34/36.17/83.61/263.23`; `m_p = 30/83/300/1581`; P.5 slack 2.0002 | wp3-a2 NC-P2/NC-P1 verbatim excerpts | OK |
| `E(w0)` decimals as REPAIRED | `referee_maths_wp3_a2.md` R2 / `referee_numerics_wp3_a2.md` (60-digit truths): `E(1) >= .00400692` (true .0040069275), `E(2) >= .00358718` (.0035871871), `E(3) >= .00304035` (.0030403586), `E(6) >= .00161240` (.0016124067), `E(4) = .00248992` safe (true .0024899244), `E(5)` safe — all six now round-DOWN as the assembly prints them | OK |
| `rho(4) <= 0.72711`, deficit `>= 0.27289` | repaired values (true deficit 0.2728957; `6.85*16*E(4)lower = 0.2728952 >= 0.27289` safe) | OK |
| truncation note `< 2e-15` | assembly quotes the F2-REPAIRED value, not wp3-a2's false `< 2e-21` | OK |
| tilt caps via `e^{0.89} > 2.4351 > 17/7 > 2` | independent 25-term exact partial sum (§2); one-sided proof valid | OK |
| `eps*`, budgets, R2 conclusion, brackets, `C_A`, R3 value, crossovers | all independently re-derived (§2), exact | OK |
| size honesty `7500x` | wp2-a2 line 673: `bound/truth = 7502.0x` | OK |
| caveat 8 (harness display erratum) | CONFIRMED REAL: `harness_m200_20260811.md` §3 header + C5 display say `4 <= m <= 400` with no C5 exemption, while `run_m200.py` line 106 exempts m = 4 (`# m=4 predates the sharp bound's range (5 <= m); record only`) and `varfit(4) = 91/108 < 187/216` exactly. The assembly's flag is accurate and the erratum is the harness REPORT's, not the assembly's | OK |
| caveat 5/§5.1 row 11 (zero referees) | accurate at the time of writing; this report is the numerics half | OK |

No ledger row failed. Two rows deserve remarks (not failures): (a) the
`C_ker` "closed" class marker carries the honest parenthetical that the
constant flavor's `m > 3000` monotonicity is grid-class — consistent with
caveat 2(d); (b) `C_A` grid `= 5.32 + 37810.0442` uses B3's inflated
working figure 4.93 for PW (not 4.9126), so the grid `C_A` is safe even
against the +0.22% extended-range caveat. Both are the safe direction.

## 5. Findings and verdict

**What survives outright (the load-bearing content).** The plug (§4 of the
target) is CORRECT as a unit: all five compatibility checks re-derive
independently in exact arithmetic; the chain algebra (T.9-final at K = 4
into Theorem S's R3, Lin counted once, w^2-bracket positive with the
ACTUAL plugged constant) is verified by hand and by script; the R2 budget
arithmetic, tilt-cap proofs, crossovers, H-discharges, and the independent
harness re-anchor all reproduce exactly. The constant ledger (§6) traces
row-for-row to the cited sources with every rounding in the safe direction,
and it correctly quotes REPAIRED values (c_w(4) = 1, rho(4) = 0.72711, the
six E-decimals, `< 2e-15`, Lin-no-double-count) rather than the drafts'
originals. The document's single-conditional accounting is numerically
honest: `[WP4-CITATION]` is load-bearing exactly once (§2.3 R2 row), and
no other unproved number is consumed anywhere. Caveat 8's harness-report
erratum is real and correctly described (runner exempts m = 4; report
display does not say so).

**Findings (all display/text-level; no constant, threshold, verdict, or
conditional moves):**

- **N-F1 (the one repair that must be made).** §4's block labeled
  "Verbatim script output" is a CONDENSED excerpt, not verbatim: ~7 lines
  of the archived output are dropped (A1's band line, C5's conclusion
  line, D's header parenthetical + limit line, E's m = 4 and m = 60 rows,
  F's m = 30 and m = 1581 rows) and F's two surviving rows are merged onto
  one line. Everything shown matches the archive byte-for-byte and every
  dropped line is an additional PASS — but the campaign has already
  established this exact repair class (wp3-a2 F7). Relabel to "condensed
  excerpt (full output archived as `out_assembly_checks.txt`, re-run
  byte-identical by this referee)" or reprint in full.
- **N-F2.** §0 states the (27/25)-centered form "the two-sided O(m^{-2})
  carrying the explicit constant C_A of §2.4". As displayed, §2.4 proves
  the two-sided constant C_A for the `1 - B_m`-centered form; recentring
  to `1 - (27/25)/m` additionally consumes `|B_m - (27/25)/m| <=
  0.54/m^2` (this referee's exact scan, `(27/25 - B_m m) m in (0.34,
  0.54]` on `[30, 2000] + {3e3, 5e3, 1e4, 1e5}`, monotone toward 1/2) plus
  the UB's 1.8 — both absorbed since `0.54 + 1.8 << C_A`, but the
  absorption is implicit. Add one sentence to §2.4 (or soften §0 to "an
  explicit constant"). Nothing moves.
- **N-F3.** §3's "Measured truth margin at the spec point: 6.7x ... vs
  the `0.2516` budget" mixes pairs: `6.7x = eps*/0.0385 =
  0.2583478/0.0385 = 6.71`, while the stated `0.2516` budget gives
  `6.5x`. Inherited verbatim from STATUS_wave2 §2. Say "6.5x against the
  20/79.5 budget (6.7x against eps*)" or drop one of the two numbers.
- **Observation O-1 (no action).** The script-path citations
  (`g2_scripts/campaign_20260811/...`) are relative to `f2_drafts/`, per
  the standing campaign convention — consistent with every other campaign
  file.
- **Observation O-2 (no action).** This referee's persistence checks are
  strictly wider than the document's: crossover scans from m = 5 with
  500-wide persistence (doc: 300), bracket positivity spot-checked to
  m = 5000 with exact monotone increase on [401, 2000] (doc: scan to
  2000), R3-bound monotonicity checked directly (doc: two-piece
  argument). No violations anywhere.

**On conditionality (per the campaign brief, not penalized):** the
reduction is verified — with CL(79, 20, 0.89) granted for m >= 401, the
displayed chain closes numerically at every step this referee can reach,
and the flip instruction (§3) is well-posed: the weaker-spec re-check rule
correctly names block C as the thing to re-run, and the tight margin it
warns about (band 2, 2.83e-4) is real and exactly reproduced.

**Final verdict: MINOR_REPAIRS** (repairs N-F1–N-F3, all text-level;
citable modulo that list under the house rule). This is the numerics half
of the two-referee unit the assembly requests in its §5.1 row 11 / caveat
5; the maths half remains to be commissioned.

*Scripts (SAVED and RUN, outputs archived beside them):
`referee_numerics_theoremA_scripts/ref_indep_checks.py`
(`out_ref_indep_checks.txt`), `ref_r1_margins.py`
(`out_ref_r1_margins.txt`), plus the harness re-run archive
`results_m200_rerun_referee.txt`. Blind protocol respected:
`g2_draft_t1_20260803.md` and every wp4 file unread by this referee. No
existing file modified.*

*End of referee_numerics_theoremA.md.*
