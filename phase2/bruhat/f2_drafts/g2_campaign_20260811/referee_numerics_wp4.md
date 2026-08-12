# referee_numerics_wp4 — adversarial numerics referee report on `wp4_draft_composite.md`

*Wave-3 NUMERICS referee (house rule, second chair = maths referee, pending).
Target: `wp4_draft_composite.md` (the CL(79, 20, 0.89) deep-tilt composite),
its sources `wp4_plan_20260811.md`, `wp4_sl_SL2.md`, `wp4_sl_SL3.md`,
`wp4_sl_SL5.md`, the orphaned `wp4_SL4/sl4_nc1.py` evidence, and every script
under `g2_scripts/campaign_20260811/wp4_*/`. Protocol: default to refutation;
re-run EVERY script and byte-diff against the archived outputs; audit every
quoted number back to an archived output; independently re-implement the
certified arithmetic (mpmath dps 60, code shared with nothing under wp4);
adversarial off-grid attacks including exact ground truth at `m = 401` — a
computation no wp4 file performed. Referee scripts (all SAVED and RUN
2026-08-12, outputs archived beside them) in `referee_numerics_wp4_scripts/`:
`ref_nw4_a_indep_ledger.py` (`out_ref_nw4_a.txt`),
`ref_nw4_b_truth_m401.py` (`out_ref_nw4_b.txt`),
`ref_nw4_c_offgrid.py` (`out_ref_nw4_c.txt`),
`ref_nw4_d_display.py` (`out_ref_nw4_d_display.txt`).
No existing file modified. Date: 2026-08-12.*

**VERDICT: MINOR_REPAIRS** — *on the draft AS THE CONDITIONAL, PARTIAL
document it declares itself to be.* Every one of the 13 scripts under the five
wp4 directories re-runs and reproduces its archived output **byte-identically**;
every certified constant survives independent dps-60 re-derivation; the
assembled `C*_eff = 16.9088` chain is arithmetically sound; the truth side of
CL is verified by this referee with exact integer arithmetic at `m = 401` and
`m = 402` (zero violations, 17.1x margin, 260 adversarial `k` at 401); and the
draft's honest §5 accounting (two missing hypotheses; the orphaned refutation
of the architected normalization) is faithful to the archived evidence — I
additionally verified the refutation sizing is robust to replacing the
orphan's `gamma = 1/8` by SL3's actually-proven `0.1317` (finding F5). The
repairs (§4) are display/prose-level except F2: the "(H1) clears with 8–23%
headroom" line (plan NC-PL1, repeated in composite §5.1) is wrong — the
measured-grid worst headroom is 6.0%, and NC-PL1's own `m = 401` grid MISSES
the W7 deep corner `lam -> 0.89` (its `w = 356.9` sample point violates
`lam <= 0.89` and is silently skipped), where this referee measures R42
headroom of only **3.9%** (R31: 3.7%). (H1) is NOT refuted — but any wave-4
prover budgeting off the advertised margin would be misled by 2x. Nothing
found moves a constant, a PASS/FAIL verdict, the conditional structure, or
the draft's own PARTIAL status.

## 1. Reproduction: every wp4 script re-run, byte-diffed vs archived output

All 13 scripts under `g2_scripts/campaign_20260811/wp4_{plan,SL2,SL3,SL4,SL5,assembly}/`
re-run (python3, this machine, 2026-08-12) and diffed against the archived
`out_*.txt`:

| script | archived output | diff | wall time |
|---|---|---|---|
| `wp4_plan/wp4plan_nc1_profiles.py` | `out_wp4plan_nc1.txt` | **IDENTICAL** | 173.4 s |
| `wp4_plan/wp4plan_nc2_model_tail.py` | `out_wp4plan_nc2.txt` | **IDENTICAL** | 7.3 s |
| `wp4_plan/wp4plan_nc3_truth.py` | `out_wp4plan_nc3.txt` | **IDENTICAL** | 26.0 s |
| `wp4_plan/wp4plan_nc4_geometry_ledger.py` | `out_wp4plan_nc4.txt` | **IDENTICAL** | 6.6 s |
| `wp4_SL2/sl2_e1_identity_monotone.py` | `out_sl2_e1.txt` | **IDENTICAL** | 0.1 s |
| `wp4_SL2/sl2_e2_band_certificate.py` | `out_sl2_e2.txt` | **IDENTICAL** | 0.6 s |
| `wp4_SL2/sl2_e3_truth_m401.py` | `out_sl2_e3.txt` | **IDENTICAL** | 0.2 s |
| `wp4_SL3/sl3_nc1_certificates.py` | `out_sl3_nc1.txt` | **IDENTICAL** | 0.1 s |
| `wp4_SL3/sl3_nc2_sanity.py` | `out_sl3_nc2.txt` | **IDENTICAL** | 1.6 s |
| `wp4_SL4/sl4_nc1.py` (orphan) | `out_sl4_nc1.txt` | **IDENTICAL** | 7.8 s |
| `wp4_SL5/sl5_nc1_ledger_exact.py` | `out_sl5_nc1.txt` | **IDENTICAL** | 0.0 s |
| `wp4_SL5/sl5_nc2_consistency.py` | `out_sl5_nc2.txt` | **IDENTICAL** | 21.2 s |
| `wp4_assembly/wp4asm_chain.py` | `out_wp4asm_chain.txt` | **IDENTICAL** | 0.0 s |

**Nothing is FABRICATED**: every number quoted in `wp4_draft_composite.md`
(and in the three SL drafts) that I traced — the §4 tables and both exact
effective-C* fractions, the §5.2 orphan quotes (129.86 / ratio 128.3 / 1191 /
`m*qW = 20.23` / `M* = 34868` / `w >= 4.51`-to-`4.05@560` sliver table /
totals 3.75–13.68 / 19.171 vs 16.0 / `|eta|/u = 0.407/0.617/0.892/0.963` /
qhat rel err `6.6e-31`-class), the §6 script-table quotes, SL2's E1/E2/E3
lines, SL3's NC-SL3-1/2 lines (incl. the D2 gap numbers 8.408 / 4.891), and
SL5's NC-SL5-1/2 lines — exists verbatim in the archived (and now re-run)
outputs. Two trivial transcription notes are in F6/F7.

## 2. Independent re-verification of the certified arithmetic (REF-A)

`ref_nw4_a_indep_ledger.py` (mpmath dps 60; fresh implementation) re-derives,
with archived output `out_ref_nw4_a.txt`:

- **A1 — assembler tables [1]/[2]/[3]** (§4 of the composite): all 21 rows
  recomputed from the raw formulas; every exact value sits at/below the
  printed certified entry columns (`R5<=`, `I1u<=`), every row passes its
  budget, and the effective-C* values reproduce:
  `[1] 16.908709 (raw) vs printed 16.9088 = 4734473/280000 (ceil-entry exact)`;
  `[2] 16.369901 vs 16.3700`; `[3] 10.080768 vs 10.0809`. D1 delta
  `0.0006344 ~ 0.000634` confirmed. The three A1 comparison lines flagged
  FAIL in my output are NOT arithmetic failures — they are the display-
  rounding finding F1 below (printed `total<=` on W2/W3/W7 is a nearest-
  rounded display sitting *below* the exact certified total).
- **A2 — SL3 constants and table**: `8/sqrt(2pi) = 3.191538 in (3.19, 3.192]`
  (so D1 is real: the architected 3.19 is indeed unachievable);
  `11.5/(1.6 sqrt(2pi)) = 2.867398 <= 2.87`; `0.64/11.5 >= 0.0556`;
  `sqrt(pi/2)/4 <= 0.3134`; `c1 = 0.13171754 >= 1/8`;
  `c2 = 0.08713622 >= 1/11.5 = 0.08695652`; `x1 <= pi/0.8`; `x2 <= pi/1.074`;
  `q(2,1) = 0.07412654 >= 0.0741` (wp1-c W.3 closed form independently coded;
  I also confirmed the W.3/W.5(ii) citations against `wp1_draft_c.md` —
  the far floor `0.0373` is wp1-c's own table line 522, and the SL3 upgrade
  to `q(2,1) = 0.0741` legitimately uses `M_1 >= w/2 > 2` + W.3(i));
  `t0(0.89)/0.89 = 1.07372378 <= 1.074`; `P3(401) = 1.25687e-7 <= 1.3e-7`;
  all seven P1/P2 band-table entries `<=` printed. Eps-sup re-checked TWO
  ways: my 89 000-point fine grid gives sup `0.32235` (tier 1) / `0.548542`
  (tier 2) — both below SL3's interval-certificate maxima `0.32258/0.54890`,
  both below `0.35/0.57`.
- **A3 — SL2 certificates**: independent quadrature `V(w0)` dominates every
  printed `LBV(w0)` (e.g. `V(4) = 0.2983334 >= 0.287512`), every printed
  `UBv(cap)` dominates the true `v(cap)`, every floor exceeds `c_A`; my own
  dps-60 step-1/8 left-Riemann sums match the printed LBVs to `< 5e-6`; the
  exact chains `1122800/7921 = 141.74978` and `8000/7921 > 1` confirmed.
- **A4 — SL5**: `far(401) = 0.00092288 <= 9.229e-4` (sharp to 4 digits —
  the printed bound is honest, not padded); `log(17/7) = 0.8873032 <= 0.8874`;
  `log 2 <= 0.6932`; `(402/401)^3 = 1.0075 < 1.0746`; the 3.19-flavor W1
  `I1u = 1.0118383 <= 1.0119`.

## 3. Adversarial off-grid attacks

### 3.1 REF-B: exact ground truth of CL at `m = 401` and `m = 402` (new computation)

`ref_nw4_b_truth_m401.py`: exact Mahonian coefficients (prefix-sum DP over
Python ints, `N = 80200`), exact `r(k) - 1` from the big integers (converted
at dps 50), `lam(k)` by bisection + mpmath-Newton on `mu(lam) = k`, `s2` by
the closed form. Adversarial `k`-selection: BOTH edges of every `w`-band, the
`w -> 4+` corner (last 46 interior `k`), the `lam -> 0.89` deep corner (first
30 band `k`), the NC-PL3 max loci (`w ~ 4.78/4.84`), plus a stride sweep —
260 values of `k` at `m = 401`, 67 at `m = 402`. Verbatim output:

```
===== m = 401 =====
  N = 80200; band k-range: [278, 24442]  (mu(0.89) = 277.86, mu(4/m) = 24442.78)
  testing 260 adversarial k values
  violations: {'CL>20': 0, 'A<cA*m': 0, 'A>m': 0, 's2<=m': 0, 's2<141.7497': 0, 'r<1': 0, 'bandless': 0}
  max eps*min(m,s2) = 1.17187 at k=21950 (w=4.894, s2=1033340.4, A=153.92)   [CL asks <= 20]
  min (A/m - c_A(band)) = 0.019219 at k=24442 (w=4.000)
  max A/m = 0.967587 at (w=137.722);  min s2/m = 1.1731 at (w=356.771)
===== m = 402 =====
  ... violations all 0 ...  max eps*min(m,s2) = 1.17186 at k=22199 (w=4.841, ...)
```

Readings: (a) **CL(79, 20, 0.89) is TRUE at its own threshold `m = 401`**
on every attacked `k`, with margin 17.1x (`1.17187` vs 20), smoothly
continuing NC-PL3's `1.1696 (m=120) / 1.1710 (m=200)`; the max sits at
`w ~ 4.9`, exactly where the plan said the pressure is. (b) Theorem A2(ii)'s
floor, Lemma C.1's cap, `s2 > m`, and `s2 >= 141.7497` all hold at the
ACTUAL mean-matched `(k, m)` pairs (not just on `lam`-grids): worst
`A/m - c_A = +0.0192` at the `w -> 4+` edge; worst `A/m = 0.9676 < 1`;
worst `s2/m = 1.173 > 1`. (c) `r(k) >= 1` at every tested band `k`
(no log-concavity violation, consistent with the harness).

### 3.2 REF-C: off-grid analytic attacks (`out_ref_nw4_c.txt`)

- **C1 (SL2/A2(ii) floor)**: band-left-edge corners `w = w0 + {1e-9, 1e-4,
  1e-2}` and the W7 deep corner, `m in {401, 402, 403, 407, 499, 1000, 5000,
  1e5}`: minimum truth margin `+0.01834` (at `w -> 4+`, `m = 1e5`),
  decreasing in `m` toward the continuum `V(4) - 0.28 = 0.0183` — exactly
  SL2's honest observation 1; **no violation anywhere**, and the certified
  `m`-uniform floors stay strictly inside truth.
- **C2 (Lemma C.1)**: max `A/(m h(lam)) = 0.999317` (at `m = 5000,
  lam = 0.89`) — the cap holds and is essentially sharp, confirming SL5's
  `0.9978` measurement and the "not spendable" caution.
- **C3 (`min(m,s2) = m` bonus)**: `s2/m` at `m = 401` falls from 92.2
  (`w = 40`) to **1.1723 at `lam = 0.89`** — truth margin 17%, comfortably
  above the certified chain's 1.0%; the bonus survives its thin-margin flag.
- **C4 ((H1) deep corner)** — see finding **F2** below: at `m = 401`,
  `lam = 0.89`: `R31 = 2.1215` (vs `R31* = 2.2`, 3.7% headroom),
  `R42 = 6.3552` (vs `R42* = 6.6`, **3.9%**); geometric limits
  `2.1303 / 6.4113`. The stated (H1) constants remain TRUE at every point I
  measured, but the advertised "8–23% headroom" is a grid artifact.
- **C5 (SL3.1 scope attack)**: the claimed validity for ALL `m >= 2` holds
  under a direct-complex-sum attack at `m in {2,3,5,10,30} x lam in {0.1,
  0.45, 0.89}`: worst tier-1 ratio `0.3898 >= c1`, worst tier-2 `0.3343 >=
  c2`; **0 violations**.
- **C6 (SL3.D/A attack)**: exact `eps_j` at `b = pi/(0.8 lam)` and
  `pi/(1.074 lam)` over `lam in {0.001..0.89} x j in {2,...,2000}`: maxima
  `0.2643 / 0.4458` — below the certificates `0.35 / 0.57` everywhere
  (including `j = 2000`, which no wp4 grid reached).
- **C7 (refutation robustness — supports composite §5.2)**: the orphan's
  honest W1 mid entry priced at SL3's actually-proven `gamma = c1 =
  0.1317175` (instead of the orphan's `1/8`) is `101.41` — still ~100x the
  architected `1.0125` slot. The §5.2 refutation of the architected
  normalization is NOT an artifact of the `1/8` choice.

## 4. Findings (all repairs; none moves a constant, verdict, or status)

1. **F1 (display rounding, the recurring campaign class — repair).** The
   `total<=` / `margin` columns of the assembler's table [1]
   (`wp4asm_chain.py`, quoted verbatim in composite §4) and the
   `total<=` / `margin>=` / `I1u<=` columns of SL5's NC-SL5-1 table are
   `%.4f` NEAREST-rounded displays of exact Fractions. Exact reconstruction
   (`ref_nw4_d_display.py`, output archived): assembler rows W2/W3/W7 print
   `total<=` BELOW the exact certified total (W2 `4.4335` vs `4.4335480`;
   W3 `4.8790` vs `4.8790430`; W7 `8.8231` vs `8.8231320`) and `margin`
   ABOVE it (W2 `2.5665` vs `2.5664520`); SL5 rows W1/W3/W4/W7 do the same
   in all three columns (W1: `4.7338` vs `4.7338454`, `0.8662` vs
   `0.8661546`, `1.0118` vs `1.0118454`). Worst gap `< 5e-5`; every
   PASS/FAIL and budget comparison is exact-Fraction and unaffected — but
   columns headed `<=`/`>=` must be ceil/floor-printed (the same repair
   class as wp3-a2 R2/F1). Knock-on text repair: SL5's §3/§5 "minimal
   margin 0.8662" and composite §2 R3's "worst margin 0.8662 -> 0.8655"
   should read `0.86615 -> 0.86552` (or floor-prints `0.8661 -> 0.8655`);
   the composite's headline `0.8655` is already safe (exact `0.8655270`).
2. **F2 ((H1) headroom claim — the one substantive repair).** Plan NC-PL1's
   "every stated entry clears its band max with 8–23% headroom", repeated in
   composite §5.1 ("(H1) ... NC-PL1 band sups clear (i) with 8–23%
   headroom"), is wrong twice: (a) on NC-PL1's own archived grid the W7
   headrooms are already 7.3% (R31: 2.2 vs 2.051) and **6.0%** (R42: 6.6 vs
   6.227); (b) NC-PL1's `m = 401` row list stops at `w = 250` — its
   `w = 356.9` sample has `lam = 0.890025 > 0.89` and is silently skipped
   by the script's band guard — so the deep corner `lam -> 0.89` of W7 was
   never measured. Referee measurement (REF-C C4) at `(m, lam) = (401,
   0.89)`: `R31 = 2.1215`, `R42 = 6.3552` — headroom **3.7% / 3.9%**,
   with geometric limits `2.1303 / 6.4113` (2.9–3.2% below the stated
   constants). (H1) is NOT refuted — every measured point still clears — but
   composite §5.1's status line must be reworded (suggest: "8–23% on
   W1–W6b; only ~4% at the W7 deep corner `lam -> 0.89`, geometric limits
   2.1303/6.4113 vs stated 2.2/6.6") so the wave-4 prover does not budget
   off a 2x-overstated margin. Note (H1) is CONJECTURED, so this repairs a
   support-evidence description, not a proof.
3. **F3 (observation, positive — record it).** CL's truth at the spec's own
   threshold `m = 401` (and 402) is now verified by exact integer
   computation (§3.1) — the draft's §5 "What is NOT in doubt" claim rested
   on `m <= 200`; this closes the extrapolation gap and confirms the 17x
   margin AT the operating point. Recommend the composite (or wave-4) cite
   this measurement.
4. **F4 (prose).** Composite §5.2/§5.3 and plan NC-PL4 quote the measured
   `C5` truth range as "0.0083–0.2104"; the archived NC-PL4 output also
   contains `0.0065` at `w = 5`, so the measured range is `0.0065–0.2104`.
   Safe direction (truth even smaller); text-level.
5. **F5 (verification note, supports the draft).** The §5.2 refutation
   sizing survives replacing the orphan's `gamma = 1/8` by the proven
   `c1 = 0.1317175`: honest W1 mid entry `101.41` vs slot `1.0125` (REF-C
   C7). Record it so the wave-4 assignment does not re-litigate the choice.
6. **F6 (trivium).** SL3 §8's quote "P3(401) = 1.2568e-7" truncates the
   archived `1.256869...e-7` (nearest print would be `1.2569e-7`); the
   certified claim `<= 1.3e-7` is unaffected.
7. **F7 (trivium).** SL2 §6 says E3's "spot check diffs all >= +0.0009";
   archived minimum is `+0.000907` — true but the safe print is `+0.0009`
   only because of the floor; fine as stated (no repair; recorded for
   completeness of the audit trail).

**Explicitly checked and clean** (no finding): the `w`-band partition;
`x1/x2` vs `pi/0.8`, `pi/1.074` (margins 9e-5 / 3e-5 — thin but certified);
`t0(0.89)/0.89` margin `2.76e-4`; the P1/P2/P3 monotonicity thresholds
(16 / 8.99 / 33.7); the far-slot double coverage (`9.229e-4` via SL5.1(iii)
and `1.3e-7` via A3, both reproduced); the B.0(i)-fallback failure record
(`221.3` at `m = 401`, first `<= 0.05` at `m = 692` — reproduced); the
`0.024 m^2`-slip diagnosis (`0.0276` reproduced); Remark C.3's tilt-cap
certificates; the 17x truth-margin arithmetic (`20/1.1710 = 17.08`); the
composite's exact fractions `4734473/280000` and `458360713/28000000`; the
orphan-quote provenance of every §5.2 number; wp1-c citation fidelity for
W.3 / W.3d / W.5(ii) / the 0.0373-vs-0.0372 floors (correctly attributed).

## 5. Verdict

**MINOR_REPAIRS.** As a numerics artifact the composite is in excellent
shape: complete reproducibility (13/13 byte-identical), certified arithmetic
that survives independent re-derivation at dps 60, honest safe-direction
certification almost everywhere (F1's display columns are the exception),
scrupulous provenance for every quoted number including the orphaned SL4
evidence, and a truth side that this referee has now pinned down by exact
computation at the operating threshold `m = 401` with zero violations and
17.1x margin. The required repairs are F1 (reprint two tables' totals/margins
in ceil/floor direction), F2 (correct the (H1) headroom sentence and record
the W7 deep-corner measurements — the only finding with quantitative
content), and the F4/F6 one-liners. None of this touches the composite's
central accounting: **CL(79, 20, 0.89) remains PROVED MODULO (H1) + (H4)
exactly as the draft states, with the §5.2 orphan evidence correctly (and,
per REF-C C7, robustly) indicating that the honest wave-4 bridge is §5.3's
package, not the architected (H1)+(H4).** The maths referee should focus on:
the SL3.D/SL3.A proof chain (my checks are consistent with it everywhere,
incl. `j = 2000`), SL2's Lemma SL2.3 Riemann direction (spot-verified
positive), the mirror/`lam = 0` boundary bookkeeping, and the status wording
of §3 (a "Theorem" whose two hypotheses include one the same document
reports as likely-unassemblable-as-stated — the §5.2/§5.3 honesty is
present; a referee should confirm §3's framing cannot be quoted without it).

*End of referee_numerics_wp4.md.*
