# CL_composition_v2 — CL(79, 20, 0.89) at m >= 561, reassembled at the wave-6 re-architected constants with (S1) discharged (wave 6b)

*Wave-6b composition deliverable, F2 campaign, 2026-08-12. This note
reassembles Theorem CL-C — the statement CL(79, 20, 0.89) for `m >= 561` —
at the RE-ARCHITECTED band constants of `wave6_s1_plan_20260812.md`, folding
in the wave-6b cross-model referee outcomes on the four Sol drafts
(`sol_s1..s4_20260812.md`, OpenAI gpt-5.6-sol, single-model as drafted):*

| piece | draft | referee verdicts | counts under house rules? |
|---|---|---|---|
| (S1) | `sol_s1_20260812.md` | maths **MINOR_REPAIRS** (`referee_maths_sol_s1.md`) + numerics **MINOR_REPAIRS** (`referee_numerics_sol_s1.md`) | **YES — (S1) is DISCHARGED** (both referees at MINOR_REPAIRS-or-better; repair lists copied into §5) |
| (S2) | `sol_s2_20260812.md` | maths **FATAL** (`referee_maths_sol_s2.md`) | NO — (S2) remains open |
| (S3) | `sol_s3_20260812.md` | numerics **MAJOR_ISSUES** (`referee_numerics_sol_s3.md`) | NO — (S3) remains open |
| (S4) | `sol_s4_20260812.md` | maths **MAJOR_ISSUES** + numerics **MAJOR_ISSUES** (`referee_maths_sol_s4.md`, `referee_numerics_sol_s4.md`) | NO — (S4) remains open |

*House rule applied strictly: an (S_i) input counts ONLY if both its
referees gave SURVIVES or MINOR_REPAIRS. A cross-model draft gets no extra
credit for being cross-model — the bar above is the campaign's standard
two-referee bar. Sources consumed: everything `CL_composition_20260812.md`
consumed (I1–I7, statuses unchanged), plus `wave6_s1_plan_20260812.md`
(the re-architecture, including its §6 (S2)-adjustment note), the four Sol
drafts and their six referee reports, `STATUS_wave5.md` (governing ledger).
Disk check (this editor, 2026-08-12): `referee_composition.md` and
`referee_hygiene.md` do NOT exist in the campaign directory — the wave-5
referee debts on the composition note and the hygiene overlay were never
discharged; see §6. `g2_draft_t1_20260803.md` remains unread; `gamma = 1/8`
not re-litigated; no existing file modified (new files only). New script
(SAVED and RUN 2026-08-12, output archived beside it, quoted in §3):
`g2_scripts/campaign_20260811/wave6b_composition/compose_chain_v2.py`
(`out_compose_chain_v2.txt`; final line `ALL CHECKS PASS: True`).*

**Bottom-line status: PARTIAL — ONE HYPOTHESIS DOWN, THREE REMAIN. NO
FLIP.** Wave 6b discharged **(S1)**: Theorem SOL.9 proves the re-architected
banded cumulant scales (`R31* = 1.19/1.44/1.82/2.04/2.38/2.56/2.71`,
`R42* = 0.87/1.62/3.11/4.27/6.38/7.33/8.17`) for all `m >= 561`,
`0 < |lam| <= 0.89`, two-referee MINOR_REPAIRS, with the numerics referee's
rigorous outward-rounded interval re-certification
(`wave6b_ref_s1/ref3_band_certificate_iv.py` + `ref2_mn_bounds.py`) adopted
as the certificate of record (§5). The composed chain at the new constants
closes at **`C*(m >= 561) = 19.5659 <= 20`** (worst row `0.978293`, the W6b
ledger row at `m = 561`) and **`C*(m >= 1581) = 15.1678 <= 136`** (8.97x) —
re-verified end-to-end in §3, including the `[401, 560]` exact-harness
discharge (5th independent parse, 557/557 PASS). The (S2)-fallback chain
(`C5*(W7) = 0.80` kept, W7 (S1) constants read as `2.42/7.28`) ALSO closes
(`19.5803 <= 20`), and Theorem SOL.9's W7 geometric bound covers both
readings — so the composition survives either resolution of the plan's §6
adjustment. The other three attacks FAILED at the bar: (S2) FATAL (the
draft proves none of the seven band bounds — "not for error — for
absence"), (S3) MAJOR_ISSUES (sound architecture, verified constants, but
the central 18.9M-box certificate was never executed), (S4) MAJOR_ISSUES
twice (the `m >= 700` core is credible; the `[561, 699]` coverage is
circular as written and a load-bearing remainder lemma is proved by
assertion). **Therefore CL(79, 20, 0.89) — and with it Theorem A — is now
PROVED CONDITIONAL on exactly the three named open statements (S2'), (S3'),
(S4) of §4, none with a proof artifact.** The conditional surface shrank
from four statements to three; every implication node is two-referee except
the process debts plainly listed in §6.

## 0. The target and the split (unchanged from v1)

Target: `wp3_draft_a2.md` §6.1's core lemma as restated by the composite
§3 — for every interior `k` with mean-matching tilt `|lam(k)| in
(4/m, 0.89]`: `s2(r(k) - 1) = 1 + theta*C*/min(m, s2)`, `|theta| <= 1`,
`C* = 20` (the `s2 >= 79` clause never binds, [A2](iii)); relaxed `C* = 136`
suffices for `m >= 1581`. Split per Cor SLV.3: `m in [401, 560]` is
discharged at CONSUMER level by exact computation (§3 block [A]: 557 data
rows, 0 non-PASS, 0 gaps, `# OVERALL: PASS` verbatim — a FIFTH independent
parse); `m >= 561` is the lemma-level obligation below.

## 1. Input inventory

Inputs I1–I7 are exactly `CL_composition_20260812.md` §1's (statuses
unchanged; all two-referee citable or coverage-certified): I1 composite
frame A2/A3/C.1/[W.6]; I2 Theorem SL3'; I3 sliver SLV.1–.3 (+ hygiene m1,
threshold `m >= 561`); I4 Theorem SL4'-R + Lemmas R.1/R.2 + Cor R.3 (Fact
R.G is RETIRED from the chain — see below); I5 Theorem E + Prop E.3 +
Lemma E.4; I6 Theorem X.1 + Cors X.2/X.3; I7 exact harness results. New:

| # | Input | File(s) | Referee status | What is consumed |
|---|---|---|---|---|
| I8 | **Theorem SOL.9 = (S1) at the re-architected constants** (`\|kappa_3\| <= R31*(W) s2/\|lam\|`, `kappa_4 <= R42*(W) s2/lam^2`, all `m >= 561`, `0 < \|lam\| <= 0.89` — a superset of the consumed one-sided scope) | `sol_s1_20260812.md` + `referee_maths_sol_s1.md` (MINOR_REPAIRS) + `referee_numerics_sol_s1.md` (MINOR_REPAIRS); **certificate of record:** `wave6b_ref_s1/ref3_band_certificate_iv.py` + `ref2_mn_bounds.py` (rigorous outward-rounded interval arithmetic, every band cell certified, zero bisections) | **two-referee MINOR_REPAIRS — CITABLE; discharges (S1)** | the fourteen band constants consumed by every ledger row's `main`/`e_cube`/`e_cross` entries and by Theorem E's price |
| I9 | **the re-architected chain constants** (band targets, W2–W7 rows certified at `m = 561`, M3 cell rung replacing Fact R.G on `[561, 699]`, R.2 new dec, `REM*`/`J0` new exact fractions, `C5*(W7) = 0.50` adopted with 0.80-fallback priced) | `wave6_s1_plan_20260812.md` (+ archived `wave6_scout/out_scout_s1_targets.txt`) | design note; its closure arithmetic re-verified by BOTH s1 referees (`19.5659 <= 20` each) and recomputed end-to-end in §3 here; the moved pieces still owe their formal re-certification pass (§6 item 3) | the chain architecture of §2 |

Chain deltas vs v1, both in the safe direction and both script-verified
(§3): (i) the W2–W7 rows are certified at `m = 561` (not 401) with the new
constants — the designed reserve is `<= 0.98` per row, 2%; (ii) **Fact R.G
is retired** — the W1 `[561, 699]` rung is the maths referee's M3 per-cell
construction (Lemma R.1's 548 floors, pointwise, `w`-uniform, no SL4'-X,
no `w`-grid; a strictly better certificate class), recomputed at the new
constants for every integer `m` in `[561, 699]`.

## 2. Theorem CL-C v2: the composed statement and proof

**The three open hypotheses (statements verbatim in §4):** (S2') =
SL1'-w(ii) with the W7 adjustment; (S3') = (E3) at the recalibrated
thresholds; (S4) = the SL4'.6/.7 bootstrap seed (unchanged).

**Theorem CL-C v2 (the composed core lemma; conditional).** *Assume (S2'),
(S3'), (S4). Then for every integer `m >= 561` and every interior `k` with
`|lam(k)| in (4/m, 0.89]`:*

```
s2 (r(k) - 1) = 1 + theta * 20/min(m, s2) ,   |theta| <= 1 ,
```

*with NO exception set — i.e. CL(79, 20, 0.89) restricted to `m >= 561`,
the entire remaining CL obligation (Fact SLV.2/Cor SLV.3). The constant
delivered along the composed chain is `C*(m >= 561) = 19.5659 < 20` (worst
certified row bound `0.978293`, the W6b row at `m = 561`; §3 blocks
[B]/[D]) — in particular `<= 20` on all of `[561, 1580]` — and for
`m >= 1581` the chain delivers `15.1678 <= 136` (8.97x headroom). The same
conclusion holds under the (S2)-FALLBACK reading (`C5*(W7) = 0.80`
retained, W7 (S1) constants `2.42/7.28`), with `C*(m >= 561) = 19.5803 <=
20` (§3 block [FB]). Combined with the `[401, 560]` consumer-level
discharge (§0), Theorem A = F2(a) is PROVED CONDITIONAL on exactly (S2'),
(S3'), (S4).*

*Proof (assembly; every citation two-referee per §1, except the process
debts of §6).* WLOG `lam = lam(k) > 0` (mirror frame; the exact center is
covered upstream by g1_draft_b B.8). Let `W` be the band of `w = m lam`.

1. *(The cumulant scales hold — no longer hypothetical.)* By **Theorem
   SOL.9** [I8], the banded scales `R31*(W)/R42*(W)` of §1 hold for all
   `m >= 561`, `lam in (4/m, 0.89]` — every ledger occurrence of
   `R31*/R42*` is now PROVED input. (Under the fallback reading the W7
   constants are `2.42/7.28`; SOL.8's geometric bound `a(0.89) < 2.1304`,
   `b(0.89) < 6.4114` covers both, §3 block [S1].)
2. *(The ledger applies.)* By (S2'), the R5 slots are priced at
   `C5* = 0.05/0.06/0.08/0.10/0.15/0.25/0.50` (fallback: `0.80` on W7); by
   I8 + (S3') and **Theorem E** [I5] re-certified at the new targets (§3
   block [E]: exact-Fraction `REM*` re-derived per the sl4pe calibration
   warning, `REM* <= 0.3 R31*^2` and positivity on all seven bands), the
   model term is priced: `|eta| <= [R42*(W)/2 + 0.3 R31*(W)^2 + lam^2/2] u`
   — the ledger's `main` entry. By (S4) and the referee-M2
   chord/monotone-iteration closure (adopted as in v1), the INFL/QUADF
   bootstrap of Lemmas SL4'.6/.7 closes at every consumed row — §3 block
   [B2]: `G(20/m) < 20/m` with margin `>= 4.55%` and seed basin
   `x_seed >= 0.92007 > 0.89` at every new worst row INCLUDING the
   fallback W7 row. So **Theorem SL4'-R** [I4] applies; its exception
   trapezoid (max `m = 462`) is moot at `m >= 561` (Cor R.3).
3. *(W2–W7 rows, all `m >= 561`.)* Certified at the operative threshold
   `m = 561` with the new constants: worst `0.978293` (W6b), all `<= 0.98`
   (§3 block [B]). m-monotonicity is structural — every entry is the same
   closed form the wave-4/5 referees certified nonincreasing on the used
   range; the new constants only rescale terms (spot-verified at
   561/601/1581). The mid slot on W2–W4 consumes **Theorem SL3'** [I2];
   W5–W7 consume only PROVED tier-1.
4. *(W1 rows — the three-rung ladder.)* On `m in [561, 699]`: the **M3
   per-cell-floor bound** (Lemma R.1's floors [I4], min `0.0176601`;
   left-endpoint sums certified by **Theorem X.1/Cor X.3** [I6]),
   recomputed at the new constants for EVERY integer `m`: worst `0.485067`
   at 561 (§3 block [C]) — analytic, no `w`-grid, no monotonicity input;
   Fact R.G's stale grid is not consumed. On `m >= 700`: **Lemma R.2**
   [I4] (same `K_Xn/K_Xd/0.0176/B(m)` machinery, Theorem SL3' named per
   M1) with the new dec evaluation: `0.976016` at 700, nonincreasing.
5. *(Far obstruction absent.)* **Lemma SLV.1** [I3]: the W1 far entry is
   `<= 0.05` for all `m >= 451`, `w >= 4` (headroom 1097.6x at 561, §3
   block [F]); the `tau_0/lam <= 1.074` cap is Cor X.2's
   (`1.07372378 <= 1.074`).
6. *(Conclusion.)* Every band row is `<= 1` (indeed `<= 0.978293`) for
   every `m >= 561`, so the share criterion (Lemma SL4'.8') delivers
   `|s2(r(k)-1) - 1| <= 20/min(m, s2)` with composed
   `C* = 19.5659 <= 20`; for `m >= 1581` the chain evaluated there gives
   worst row `0.75839`, i.e. `15.1678 <= 136` a fortiori. The variance
   floor and mirror close the statement as in the composite §3 proof. ∎

*Remark (what moved since wave 5).* The wave-5 conditional surface was
(S1)–(S4). Wave 6 re-architected the targets (worst-band (S1) proof margin
2.94% -> 27.21%); wave 6b then DISCHARGED (S1) at the new constants
(Theorem SOL.9 — whose W7 argument, a global geometric-envelope bound, is
cleaner than the plan's roadmap and needs no monotonicity-in-m). The
composed constant moved `18.2281 -> 19.5659` — that is the wave-6 design
spending chain slack to buy (S1) provability, exactly as priced. (S3)'s
thresholds GREW under the re-architecture (safe direction, §3 block [E]),
so (S3') is strictly easier than wave-5 (S3). (S2) and (S4) are unchanged
in content; their wave-6b attempts failed the bar and are inventoried in
§4. Net: the surface is 4 -> 3, and every survivor carries wider measured
margins than its wave-5 predecessor.

## 3. The composed constant chain, re-verified end-to-end (script, verbatim extracts)

Script `wave6b_composition/compose_chain_v2.py` (row machinery =
`sl4pr_common.py`, twice-validated, imported unmodified; W1-ladder and
Theorem-E-Fraction machinery ported verbatim from the scout, whose guard
block [G] reproduces the wave-5 sentinels byte-consistently — re-run here:
`ALL GUARDS OK: True`). Output `out_compose_chain_v2.txt`, key blocks:

```
[A] exact harness coverage (threshold shift) -- 5th independent parse
  data rows honored/fresh union: 557;  PASS rows: 557;  non-PASS: 0
  gaps in [4, 560]: NONE;  gaps in [401, 560]: NONE
  OVERALL line (verbatim): # OVERALL: PASS -- all of C1..C6 hold exactly for 4 <= m <= 560 (C2/C3 with the known m=4 exception; rows split across this file and the honored prior file(s)).
```

```
[B] W2-W7 ledger rows at the NEW targets (certification point m = 561)
  m= 561:  W2=0.455366  W3=0.666046  W4=0.718169  W5=0.976193  W6b=0.978293  W7=0.977247
  m= 601:  W2=0.432621  W3=0.652598  W4=0.705742  W5=0.951104  W6b=0.958647  W7=0.958568
  m=1581:  W2=0.342146  W3=0.528123  W4=0.571056  W5=0.751978  W6b=0.75839  W7=0.755307
  all W2-W7 rows at 561 <= 0.98 (designed reserve): True;  m-monotone spot (561 >= 601 >= 1581): True
[C] W1 closure ladder at the NEW targets
  M3 cell rung ... EVERY integer m in [561, 699]: worst = 0.485067 at m = 561;  all <= 1: True  (<= 0.98: True)
  Lemma R.2 tail (new dec): m=700: 0.976016  m=750: 0.630819  m=1000: 0.290501  m=1581: 0.258665
[D] the COMPOSED effective constant (ADOPTED architecture)
  composed worst row bound on m >= 561 = 0.978293  ->  C*(m >= 561) = 19.5659 <= 20: True
  m >= 1581: worst row = 0.75839  ->  C*(m >= 1581) = 15.1678 <= 136: True  (headroom 8.966x)
```

```
[E] Theorem E re-certification at the new targets (exact Fractions; REM* re-derived)
  W1 : J* = 0.85983  REM* = 0.0256747 J0_new = 0.834155  ... J0_new > J0_old(0.682942): True
  W7 : J* = 6.28823  REM* = 0.273469  J0_new = 6.01476   ... J0_new > J0_old(4.59597): True
  ALL Theorem-E side conditions at the new targets: True;  J0 grows bandwise (safe direction, s3-ref F3): True
[S1] the DISCHARGED (S1) input (Theorem SOL.9, two-referee MINOR_REPAIRS)
  W7 : geometric enclosures a(0.89) < 2.1304, b(0.89) < 6.4114 clear ADOPTED targets 2.71/8.17: True
       ... and the (S2)-FALLBACK targets 2.42/7.28: True  (S1 survives either (S2) resolution)
  [S1] all 14 adopted constants strictly dominated by refereed certificates: True
[FB] the (S2)-FALLBACK chain (C5*(W7) = 0.80 kept; W7 targets 2.42/7.28)
  fallback W7 row: m=561: 0.979015  m=601: 0.958342  m=1581: 0.733254
  FALLBACK composed C*(m >= 561) = 19.5803 <= 20: True;  C*(m >= 1581) = 15.1678 <= 136: True
[B2] (S4)/bootstrap ... at every NEW worst row
  W6b @ m=561: ... margin 4.552%;  x_seed = 0.92147 >= 0.89: True     [thinnest of 9 rows checked]
  W7 @ m=561 (FALLBACK): ... margin 4.602%;  x_seed = 0.92147 >= 0.89: True
  BOOTSTRAP closes from the (S4) seed 0.89 at every worst row (incl. fallback): True
== COMPOSED-CHAIN v2 VERDICT ==
  ALL CHECKS PASS: True
```

Reading: the composed constant is now set by the **W6b ledger row at the
certification point `m = 561`** (`0.978293`; v1's was Lemma R.2's tail at
700, `0.911407`) — the 2% row reserve is the designed cushion, thinner than
v1's 9% because the wave-6 re-architecture deliberately spent that slack on
(S1) provability (27.21% worst-band proof margin, vs 2.94% before, is what
made Theorem SOL.9 possible). Both budget clauses hold with the reserve
intact under BOTH (S2) readings.

## 4. The conditional surface: exactly three named statements, none proved

Scope for all three: `m >= 561`, `lam(k) in (4/m, 0.89]` (mirror covers
the negative sign), band `W` of `w = m lam`. All CONJECTURED — each wave-6b
attempt failed the two-referee bar; the verdicts and residues are recorded
per statement.

- **(S2') [SL1'-w(ii), W7-adjusted] Core remainder.**
  `log phi(t) = -s2 t^2/2 - i kappa_3 t^3/6 + kappa_4 t^4/24 + R5(t)` with
  `|R5(t)| <= C5*(W) s2 t^5/lam^3` on `[0, lam/2]`,
  `C5* = 0.05/0.06/0.08/0.10/0.15/0.25/0.50`.
  *Adjustment provenance:* the plan's §6 single (S2) change
  (`C5*(W7): 0.80 -> 0.50`), adopted here on the strength of the s2
  referee's DIRECT R5 measurements at the W7 corner (the plan's stated
  precondition): measured `Q(t = lam/2) = 0.194721` and `Q(0) = 0.21152994`
  at `(561, lam = 0.89)`, cancellation-free `C_abs` sample sup `0.2624`
  over W7 — all `<= 0.50` with `>= 1.9x` room — plus the SOL.6 hard floor:
  `0.184013` is the liminf-of-sup for any unbounded band, so `0.50` clears
  the structural floor 2.7x while nothing below `0.19` is ever available.
  **Fallback, fully priced (§3 [FB]):** if the eventual prover lands only
  `C5*(W7) = 0.80`, read W7's (S1) constants as `2.42/7.28` (covered by
  Theorem SOL.9) — the chain closes at `19.5803 <= 20` and nothing else
  moves. *Wave-6b attempt:* **FATAL** (`referee_maths_sol_s2.md` — "not for
  error — for absence": zero of the seven band bounds attempted; its only
  bound is 20–23x short on W1). *Salvage for the next prover* (referee F6):
  the exact remainder identities SOL.3.1/3.2, the interface-exact criterion
  SOL.5.3 (W7 re-pointed at 0.50), SOL.4 as the W7-closer candidate (F4: a
  one-page sup argument over `C_abs(m, lam)` plausibly closes W7 outright;
  W1–W6b need genuine cancellation), and the SOL.6 floor. The referee's F2
  stands: the bands ARE endpoint-defined (`wave5_sl4pe` §0) — the draft's
  "bands undefined" premise must not be cited.
- **(S3') [(E3) = SL4'-E-J at the recalibrated thresholds] Joint
  cancellation bound.** With `r31 := |kappa_3| lam/s2`,
  `r42 := kappa_4 lam^2/s2`:
  `J := r31^2 - r42/2 <= J0(W) = 0.834155/1.38585/2.44993/3.25094/4.67285/
  5.38338/6.01476` (exact fractions archived in
  `wave6_scout/out_scout_s1_targets.txt`; re-derived independently in §3
  block [E]). The thresholds GREW from wave-5's row on every band (verified
  exactly; s3-referee finding F3) — so any proof against the OLD row
  discharges (S3') a fortiori, and Prop E.3's unavoidability argument [I5]
  carries over unchanged. *Measured margins:* 44.8/60.3/72.9/77.7/82.0/
  82.9/78.0% per band (worst W1; was 32.6% at wave 5); W7's geometric-limit
  `J -> 1.3326` clears `6.01476` by 77.8%. *Wave-6b attempt:*
  **MAJOR_ISSUES** (`referee_numerics_sol_s3.md`): every testable claim
  TRUE (band sups 7.9–46% above truth, W7 legs verified incl. the exact
  `lam -> 0+` closed forms `1 - zeta2/20` / `U7(0+) = 2.2425449`, exact
  floors valid, no Prop E.3 smuggling) — but the central 18,874,368-box
  interval certificate and the SOL.16/SOL.17 evaluations were NEVER
  EXECUTED (F1), and two text flaws are exactly characterized: F2 (the
  Euler–Maclaurin remainder constant understated by factor 1.992 — missing
  B_8 boundary term; numerically absorbed everywhere, ~11 orders of slack)
  and F3 (threshold-generation paragraph owed). *Path to closure*
  (referee §9): run the certificate with the corrected constant, apply
  F2/F3 in text, re-referee — the resolution budget is verified generous
  (28x worst gap-control ratio).
- **(S4) [Bootstrap seed] A-priori ratio bound.** `|s2(r(k) - 1) - 1| <=
  0.89` on the deep-tilt band, `m >= 561` — statement and constant
  UNCHANGED from v1 §4. Consumed via referee-M2's chord/monotone-iteration
  closure, re-quantified at the new worst rows in §3 block [B2]:
  contraction margin `>= 4.55%`, seed basins `x_seed >= 0.92007 > 0.89` at
  all nine rows checked (including the fallback W7 row). *Wave-6b attempt:*
  **MAJOR_ISSUES x2** (`referee_maths_sol_s4.md`,
  `referee_numerics_sol_s4.md`, independently concordant): the `m >= 700`
  C^2-local-CLT architecture is sound and non-circular (delivered constant
  `0.545` there, every V-constant re-verified except one display rounding
  `E_mid[0]`), but (i) the `[561, 699]` coverage is CIRCULAR as written
  (it reads ledger-row closures as CL-level closures; the seed is consumed
  from `m = 561` — both referees refute the draft's premise from the
  sources), and (ii) Lemma SOL.2's (SOL.14)/(SOL.15) is proved by
  assertion, with the displayed envelope unobtainable by the stated
  termwise route (maths F2 — the abs-series violates it at the deep
  corner, `8.29 > 7.008`). *Both referees quantified in-kind repairs:*
  the same machinery closes `[561, 699]` against 0.89 (independent sizings
  `0.7241` and `0.689148` at 561), and an honest envelope
  `6.72 + 5.136 u/(1-u)` still yields `0.0018 < 0.0021` — a revision
  executing repairs R1–R4/N1–N3 is plausibly one focused session from
  citable. Until then (S4) has no artifact on any range.

**Why the surface is exactly this.** Theorem SOL.9 [I8] supplies every
cumulant-scale input; Theorem E [I5] (re-certified at the new targets, §3
[E]) turns I8 + (S3') into the `main`-row pricing; (S2') prices the R5
slots; (S4) closes the bootstrap; everything else in every ledger row is
PROVED input (I1/I2/I3/I4/I6). No other unproved statement is consumed —
re-checked against the v1 audit and the six wave-6b referee reports; no
CONJECTURED item is consumed silently.

## 5. The discharged (S1): repair lists copied in (house rule)

**Statement consumed** (= Theorem SOL.9, restated at the adopted
constants): for `m >= 561`, `lam in (4/m, 0.89]`, band `W`:
`|kappa_3| <= R31*(W) s2/lam`, `kappa_4 <= R42*(W) s2/lam^2`, with
`R31* = 1.19/1.44/1.82/2.04/2.38/2.56/2.71`,
`R42* = 0.87/1.62/3.11/4.27/6.38/7.33/8.17`. The draft proves the
two-sided-`lam` superset; certified per-band ceilings sit 1.49–4.46%
inside the claimed table, which sits strictly below the targets
(§3 [S1]).

**Maths referee repairs (R1–R5, `referee_maths_sol_s1.md` §5):**

1. **R1 (was BLOCKING; now DISCHARGED by the numerics lane):** execute and
   archive the SOL.6 interval certificate + the (17) derivative bounds.
   Discharged per the numerics referee's own F1 repair option: the
   certificate of record is `wave6b_ref_s1/ref3_band_certificate_iv.py`
   (mpmath.iv, 100 bits, outward-rounded; every cell of every band passes)
   + `ref2_mn_bounds.py` (symbolic recurrences exact; certified sups
   0.1686/0.1845/0.5301 vs claimed 1/4/20). W7's (26)/(27) enclosures
   re-verified in interval arithmetic (folds in R2).
2. **R2 (one line):** cite an interval evaluation for SOL.8's (26)/(27) —
   covered by ref3/ref1 (dps-50 + interval); text line still owed.
3. **R3 (one line):** display the `b' > 0` proof — adopt the referee's
   one-differentiation route (`P(y) = 2 sinh^3 y + 3 sinh y - 3y cosh y`,
   `P' = 3 sinh y (sinh 2y - y) > 0`).
4. **R4 (one clause):** state `h_n in C^2[0, w]` (removable singularity)
   so the trapezoid remainder applies on the first cell.
5. **R5 (wording):** state SOL.7's chain sign-free
   (`D_3 <= U_3 <= c_31 L_2 <= c_31 D_2`), not as a ratio inequality.

**Numerics referee repairs (F1–F2, `referee_numerics_sol_s1.md` §5):**

1. **F1 (provenance):** the draft shipped its central certificate as an
   unexecuted claim; the ledger must record the certificate artifact as
   the REFEREE's (`ref3` + `ref2`), not the prover's — adopted, so
   recorded here and in §6.
2. **F2 (statement hygiene):** Theorem SOL.9 must restore the
   `lam in (4/m, 0.89]` range clause (`w > 4`) and note the two-sided
   version is a superset of the consumed one-sided statement.
3. Records, no action: F3 (derivative constants generous 5.9–38x), F4
   (the draft's recipe is not self-sufficient — the referee's ref1/ref4
   adversarial layers supplied the missing checks, all pass), F5 (wording
   of the `b'` reduction, folded into maths R3).

None of R2–R5/F2 moves a constant, bound, or verdict; they go to the next
hygiene batch. Observations worth their ledger line (both referees): the
proof covers both tilt signs (safe-direction strength), and the W7
geometric bound survives the plan's (S2) fallback — consumed in §2 step 1
and §3 [S1]/[FB].

## 6. Referee-debt ledger (all process, stated plainly)

1. **`referee_composition.md` and `referee_hygiene.md` DO NOT EXIST**
   (disk check, this editor): STATUS_wave5 §3 item 2's debts — the unit
   referee on `CL_composition_20260812.md` and the single-verifier pass
   on `wave4_hygiene_20260812.md` — were never discharged. v1 is now
   SUPERSEDED by this note as the operative composition; its unit-referee
   debt transfers here rather than lapsing.
2. **This note has ZERO referees** (new file). Under house rules the
   composed statement must be refereed as a unit before the paper cites
   it. Its script is deliberately thin — heavy certificates live in the
   refereed sources and in `wave6b_ref_s1/`; the script re-verifies
   interfaces, sentinels, rows, and the budget comparisons.
3. **The moved-piece re-certification of the plan's §9 items 1–2 is
   FOLDED INTO but not replaced by this note:** the SL4'-R row
   re-certification at `m = 561` (new constant table, same closed forms)
   and Theorem E's `REM*`/`J0` table replacement are recomputed here (§3
   [B]/[C]/[E]) and were arithmetic-checked by both s1 referees, but the
   formal referee pass on those one-page deltas is part of this note's
   unit referee, not yet done. Fact R.G's retirement (in favor of the M3
   rung) should be ratified in the same pass.
4. **§2a recorded repairs of STATUS_wave5** (I4 R1–R4/RF-1, I5 R1–R6 +
   F1–F4, I6 m1–m4/O1) remain recorded-not-applied; add §5's R2–R5/F2
   and the s3/s4 text repairs (if those drafts are revived) to the same
   hygiene batch.
5. **The stalled fresh harness re-run** (record-only, `m = 441`) is
   unchanged; rows 4..481 remain honored `results_m540.txt` rows.

## 7. Honesty register (nothing hidden)

1. **No flip.** (S2'), (S3'), (S4) have no proof artifacts; the flip
   preconditions (all statements proved + refereed, `assembly_checks.py`
   block C re-run at the landed spec — band-2 margin `2.83e-4` — and
   assembly §8 human ratification) are not met and nothing here claims
   them.
2. **The composed reserve is 2%, by design.** The worst row `0.978293`
   is deliberately thinner than v1's `0.911407` — the slack was spent on
   (S1) provability (that trade is the entire content of the wave-6 plan,
   and it PAID: (S1) is now a theorem). The old chain's accepted worst
   rows were 0.98909/0.991128; the new reserve is tighter than those, but
   the do-not-sharpen flags of STATUS_wave5 §3 (NX-5's `2.76e-4`, X.a's
   spent floor, the [B2] 4.55% bootstrap margins) all still hold.
3. **(S2') adoption is a design choice backed by measurement, not proof:**
   the 0.50 rests on the s2 referee's direct R5/W7 measurements
   (`0.1947/0.2115/0.2624`-class, `>= 1.9x` room) and the SOL.6 floor
   `0.184013 < 0.50`; the fully-priced 0.80-fallback (§3 [FB]) is the
   hedge, and Theorem SOL.9 covers both. The eventual (S2) prover should
   still confirm by its own R5 measurement per the plan's §6 caveat.
4. **Certificate classes, inherited:** Theorem SL3' monotone-cell
   (1.30x/truth ~16x); Lemma E.4 + NX constants named-constant class; the
   (S1) certificate of record is rigorous outward-rounded interval
   arithmetic (ref3, STRONGER than the flagged classes); ledger rows are
   mpmath dps-40 on the twice-validated engine; harness parse exact; the
   Theorem-E block exact Fractions. m-monotonicity of the new rows rests
   on the structural argument (same closed forms, referee-certified
   nonincreasing) + 561/601/1581 spot checks — the unit referee should
   re-scan if desired ([D3]-style).
5. **Truth side (corroborative only):** CL exactly TRUE at 401/402
   (17.1x); the s1 referees' ~170-point truth-under-ceiling sweep and
   90-probe (S1) truth attack, 0 violations; s3 referee's band scans (J
   inside every claimed sup, 7.9–46%); s4 referees' end-to-end
   `s2(r-1) in [0.99792, 0.999001]` at all corners including `[561, 699]`.
   Nothing load-bearing consumes these.

## 8. Status recap and what remains

- **Theorem CL-C v2: ASSEMBLED and chain-verified** — CL(79, 20, 0.89) at
  `m >= 561` is **PROVED MODULO (S2'), (S3'), (S4)** — three statements,
  down from four — with `[401, 560]` closed by exact computation,
  `C*(m >= 561) = 19.5659 <= 20` (and `<= 20` on `[561, 1580]` in
  particular), `C*(m >= 1581) = 15.1678 <= 136`, and the (S2)-fallback
  chain closing at `19.5803 <= 20`.
- **(S1): DISCHARGED** (Theorem SOL.9, two-referee MINOR_REPAIRS;
  certificate of record `wave6b_ref_s1/ref2+ref3`; repairs listed in §5,
  none constant-moving).
- **CL itself: STILL OPEN. Theorem A remains PROVED CONDITIONAL on
  exactly (S2'), (S3'), (S4)** — nothing more, nothing less. The paper
  must NOT say F2(a) is proved; must not call CL "nearly proved"; must
  not cite this note, v1, or the hygiene overlay until their referee
  passes land; and must cite (S1) only through `sol_s1_20260812.md` WITH
  its two referee reports and the certificate-of-record provenance.
- **Remaining work, in order:** (i) **(S3)** — closest to closure: run
  the sol_s3 certificate with the F2-corrected constant, apply F2/F3,
  re-referee (the s3 referee judges the resolution budget generous);
  (ii) **(S4)** — revise sol_s4 per R1–R4/N1–N3 (both referees' in-kind
  repair sizings close `[561, 699]` at `~0.69–0.73` vs 0.89), two
  referees; (iii) **(S2')** — new prover artifact (salvage inventory in
  §4; W7 plausibly closes via SOL.4 + a sup argument; W1–W6b need real
  cancellation), two referees; (iv) unit-referee THIS note (folding in
  §6 item 3's moved-piece deltas) and give the hygiene overlay its pass;
  (v) apply the recorded text repairs; (vi) the flip: block C re-run at
  the landed spec + assembly §8 human ratification. Items (i)–(iii) are
  the only remaining mathematics.

*End of CL_composition_v2_20260812.md.*
