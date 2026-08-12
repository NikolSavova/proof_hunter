# Wave-4 hygiene batch: recorded errata and inserts (2026-08-12, wave 5)

*Wave-5 hygiene deliverable, executing STATUS_wave4.md §3 item 1 ("the
hygiene batch") as RECORDED ERRATA/INSERTS — per the campaign's no-erasing
rule, no existing file is modified; this file is the authoritative overlay
and consumers of the four target files must read them THROUGH this file.
Targets: (1) `wave4_sliver_20260812.md` (repair m1, the pending §3.1
final-audit insert; plus the m2–m6 text errata recorded for completeness);
(2) `harness_m560_20260812.md` (its §2/§3 "[TO BE FILLED]" sections, filled
here as an addendum from the actual on-disk results file); (3)
`wave4_sl3p_20260812.md` (the full §2b repair list R1–R5, R1 being the
1.30x worst-certified-margin correction); (4) `wave2_repairs_20260811.md`
(the W-F1 relabel from `referee_wave2_repairs.md`). Every numeric claim
below is verified by the SAVED + RUN script
`g2_scripts/campaign_20260811/wave5_hygiene/hygiene_checks.py` (outputs
archived alongside: `out_hygiene_checks_fast.txt` blocks [A]–[D],
`out_hygiene_checks.txt` adds the exact block [E]); output quoted verbatim
in §5. No constant, threshold, band, coverage bound, or verdict of any
refereed file is moved by anything in this batch — every item is
text-level, an insert of an already-computed fact, or a relabel demanded
by a referee.*

**Scope discipline.** This file applies exactly the four hygiene items of
STATUS_wave4 §3 item 1 (with §2a's m2–m6 recorded alongside m1, since they
are one-line and their omission would leave the sliver file teaching a
wrong band edge). It does NOT touch SL4' (§2c is a repair-agent task, not
hygiene), does not add mathematics, and does not re-litigate `gamma = 1/8`.
The fifth §3-item-1 entry — "let the from-scratch fresh harness re-run
finish (record-only)" — is a wait, not an edit; its current state is
recorded in §2.3.

## 1. Item (1): `wave4_sliver_20260812.md` — repair m1 (the §3.1 final-audit insert)

**The issue, quoted.** `referee_maths_wave4_sliver.md` §5 finding m1
(= numerics F3; "the one that must be done before citation"):

> The note is self-declared "(pending §3.1 final-audit insert)" and
> internally mixes three coverage snapshots: abstract "`M_H >= 536` ...
> and `M_H = 560` on run completion", Fact SLV.2 "`M_H = 554` at final
> audit", SLV.3 "`m >= M_H + 1 = 561`" — while the honestly-certified
> fallback at writing time was `m >= 555` (§3.1). ... Required: execute
> the note's own §3.1 refresh — ... quote the `# OVERALL: PASS` tail
> verbatim, restate Fact SLV.2 with `M_H = 560` as CERTIFIED (not
> anticipated), and delete the 554/555 interim scaffolding or mark it
> superseded. Until this edit, every consumer must read the certified
> threshold as `m >= 555`, not 561.

**The fix (the insert, now executed).** The run HAS completed and the
completed-run audit is re-verified here from scratch (script block [A],
exact parse of BOTH results files, §5): zero FAIL rows anywhere, union
coverage contiguous `m in [4, 560]` with empty gap list, and the results
file ends with the OVERALL line. The following text is the recorded
final form of the sliver note's pending pieces:

- **Fact SLV.2 (final form, superseding the note's §3/§3.1 interim
  text).** The exact integer Mahonian harness (certificates C1–C6, exact
  Fractions in every verdict) PASSES for every integer `m in [4, M_H]`
  with **`M_H = 560` CERTIFIED** (zero FAIL rows, zero gaps; rows
  `4..481` per `wave2_repairs/results_m540.txt`, rows `482..560` per
  `harness_m560/results_m560.txt`). In particular the full sliver
  m-extent `[401, 450]` — and 110 rows beyond it — is exactly verified.
- **Verbatim tail of `results_m560.txt`** (the note's §3.1 promised
  quote; re-read from disk by script [A]):

  ```
   560 156520  78260  78260   2.0405e-07 0.9980725915  1.07935   PASS
  #
  # elapsed this run: 429.6 s; new rows: 65; prior rows honored: 492; failures (new rows): 0
  # OVERALL: PASS -- all of C1..C6 hold exactly for 4 <= m <= 560 (C2/C3 with the known m=4 exception; rows split across this file and the honored prior file(s)).
  ```

- **Corollary SLV.3 (final form).** CL's proof obligation restates as
  **`CL(79, 20, 0.89) for m >= 561`**, with `m in [401, 560]` covered by
  Fact SLV.2 at consumer level. The interim scaffolding — "`M_H = 554`
  at final audit", "certified shifted threshold is `m >= 555`", "a
  waiter is armed" — is **RETIRED/SUPERSEDED**: the certified threshold
  is now `m >= 561`, unconditionally on any pending run.
- Lemma SLV.1 is untouched (it was final already): W1 far entry
  `<= 0.05` for all integers `m >= 451`, all `w >= 4`, boundary exact at
  `m0 = 450`; at the operative threshold `m = 561` the float headroom is
  the 1097x-class figure (script [C] of the sliver note, display-only).

**Independent corroboration added by this batch (beyond the referee's).**
Script block [E] rebuilt the exact Mahonian polynomial through `m = 560`
with the verbatim running-sum recurrence and recomputed the central-ratio
varfit as an exact Fraction at all six footer checkpoints: all six match
the results-file footer to all 12 printed digits (§5, block [E] output).

**m2–m6, recorded as one-line errata (completeness; all text-level, none
load-bearing):**

- (m2 = F2) Fact SLV.2's coverage citation splits as: `[401, M_H]`
  certified by sliver script [B]'s contiguity walk; `[4, 400]` per
  part I's existing citation (`harness_m200_20260811.md`) and by the
  gapless `results_m540.txt` rows `4..400`. Block [A] of THIS batch
  independently walks the full `[4, 560]` range with no 401 seam: gap
  list empty. The Fact is true as stated; the scope note is now on
  record.
- (m3 = F1) Read `W1 = (4, 5]` (composite §0), not `(4, 6]`, wherever
  the sliver note says "all of W1 `(4, 6]`"; the certificate quantifies
  over all `w >= 4`, so nothing else changes.
- (m4) The "~560-class" sizing quote re-attributes to the ORPHAN Part C
  grid (`w >= 4.05` by `m = 560`), not ASM-5 (whose own output is
  "closes at m = 432 / 450").
- (m5) SLV.3 item 2's "`<= 4.56e-5`-class" carries the label "(script
  [C], float, display-only)"; Lemma SLV.1 itself certifies `<= 0.05`.
- (m6 = F4) Flag f1 updates: `referee_wave2_repairs.md` EXISTS
  (single-verifier MINOR_REPAIRS); the residual debt is only "no
  COMPLETE from-scratch re-run of rows 4..481" — see §2.3 below for the
  fresh-run state, which now covers rows `4..441` byte-identically.

**Effect.** With m1 executed, the SL-sliver piece stands at its
two-referee grade with no pending insert: **SL-sliver CLOSED (PROVED,
finite closure) per composite §5.3(b)**, and the CL target statement is
`CL(79, 20, 0.89) for m >= 561`.

## 2. Item (2): `harness_m560_20260812.md` — §2 and §3 filled (addendum)

**The issue, quoted.** `harness_m560_20260812.md` §2 ("Verbatim run
output (tail of results_m560.txt)") and §3 ("Consequences") both read,
verbatim:

> [TO BE FILLED ON COMPLETION]

STATUS_wave4 §1 row 1 records this as "its agent's debt — the run is
done". The run completed on 2026-08-12; this section is the addendum
that fills both sections from the actual on-disk results file
(`harness_m560/results_m560.txt`, 96 lines; re-parsed exactly by script
block [A], §5).

### 2.1 §2 as filled — verbatim run output

Run shape (from the file's own comment lines): the first launch honored
478 prior PASS rows (`# prior PASS rows honored (skipped here): 478 from
['../wave2_repairs/results_m540.txt']`, line 5) and appended fresh rows
from 482; a mid-run death and relaunch is recorded verbatim at line 21:

```
# --- resume 2026-08-12 08:07:47: 492 m already certified, continuing to 560 ---
```

(492 = 478 honored + 14 checkpointed rows `482..495` from the first
launch — checkpointing worked exactly as designed.) The file carries 79
data rows `m = 482..560`, ALL PASS, zero FAIL. Verbatim tail, including
the OVERALL line and the full checkpoint-varfit footer:

```
 559 155961  77980  77980   2.0515e-07 0.9980691459  1.07935   PASS
 560 156520  78260  78260   2.0405e-07 0.9980725915  1.07935   PASS
#
# elapsed this run: 429.6 s; new rows: 65; prior rows honored: 492; failures (new rows): 0
# OVERALL: PASS -- all of C1..C6 hold exactly for 4 <= m <= 560 (C2/C3 with the known m=4 exception; rows split across this file and the honored prior file(s)).
# checkpoint varfit values (exact Fraction -> 12 digits):
#   varfit(534) = 0.997978810615
#   varfit(535) = 0.997982586007
#   varfit(536) = 0.997986347205
#   varfit(537) = 0.997990094521
#   varfit(540) = 0.998001253256
#   varfit(560) = 0.998072591511
```

Coverage audit (this batch, script block [A], exact parse of both
files): `results_m540.txt` = 478 data rows `m in [4, 481]`, 0 FAIL, no
OVERALL line; `results_m560.txt` = 79 data rows `m in [482, 560]`, 0
FAIL, 1 OVERALL line; union contiguous `m in [4, 560]`, gap list `[]`.
All six footer varfit values independently recomputed EXACTLY (block
[E]): 12/12 digits match on every line.

### 2.2 §3 as filled — consequences

1. **SL-sliver harness option (b) executed to completion.** The sliver
   trapezoid `w in (4, 4.51], m in [401, 450]` lies 110 rows inside the
   certified coverage `[4, 560]`; per Cor SLV.3 (composite §5.3(b)
   mechanism) **CL's proof obligation restates as `CL(79, 20, 0.89) for
   m >= 561`**. This is a consumer-level discharge on `[401, 560]`, not
   a lemma-level proof of CL there.
2. **G4 part-(c) band CLOSED by computation.** The crude-`C_A` crossover
   `m* = 535/537` sits inside exact coverage; the band `[401, 536]` is
   closed, and the footer's checkpoint varfit values at
   `m = 534/535/536/537` (quoted above, exactly recomputed here) are the
   record for the crossover neighborhood. G4's remaining work is the
   constant chase only (STATUS_wave4 §5 item 6).
3. **Part I finite companions extend to 560.** The finite theorems
   (argmin centrality, min = central, `sigma^2(r_m - 1) >= 187/216` with
   equality iff `m = 6`, strict increase) are unconditional for
   `5 <= m <= 560` (C5 scope `5 <= m` per the standing erratum; the
   known `m = 4` C2/C3 exception is unchanged), citable as
   `harness_m200_20260811.md` + `harness_m560_20260812.md` (read
   through this addendum) + the sliver audit.
4. **Trend record.** `varfit(560) = 0.998072591511` (exact Fraction,
   12 digits) and `mfit(560) = 1.07935`, consistent with the predicted
   `m(1 - varfit) -> 27/25 = 1.08` from below; C6 strict increase held
   exactly across both resume boundaries (the exact-Fraction C6 chain
   described in §1 change 2 of the harness note).
5. **Flip-time note (unchanged from sliver flag f3).** At flip time,
   re-run `assembly_checks.py` block C with the landed threshold
   `m >= 561` (band-2 margin `2.83e-4` is the tight one).

### 2.3 The fresh from-scratch re-run (record-only; STATUS §3 item 1's fifth entry)

State at this batch's writing (script block [B], §5): the sliver-numerics
referee's from-scratch re-run file `referee_fresh_results_m560.txt`
holds 438 data rows, `m in [4, 441]`, gapless, 0 FAIL, NO OVERALL line —
still incomplete (stalled at the same `m = 441` the STATUS editor saw;
its process appears to have died and would need a relaunch, which is that
referee's call, not this batch's). Every one of its 438 rows is
**byte-identical** to the corresponding primary row (mismatch list `[]`),
so the honored-rows provenance debt (sliver flag f1 / m6) is now
discharged by from-scratch recomputation for rows `4..441` and by
referee spot-checks beyond. Record-only: nothing in the ledger
load-bears on this file.

## 3. Item (3): `wave4_sl3p_20260812.md` — the §2b repair list applied (R1–R5)

All five repairs of STATUS_wave4 §2b (union of `referee_maths_wave4_sl3p.md`
R1–R5 and `referee_numerics_wave4_sl3p.md` F1–F3), applied as recorded
errata. All are text-level; no constant, band, `gamma*`, threshold, or
verdict moves. Theorem SL3' remains PROVED modulo the flagged
finite-certificate class, two-referee MINOR_REPAIRS — with these errata,
the repairs are discharged.

### 3.1 R1 — the worst-certified-margin correction (consumer-facing; THE substantive one)

**The issue, quoted.** The draft's Bottom line (§0) and §8 both say:

> All certificates PASS with worst headroom **7.96x** (E.5.3, W7)

and §4.2/§4.3's chain closes "by Lemma E.5.2 for `tau <= tau_start(W)`
and Certificate E.5.3 for `tau in [tau_start(W), 0.8]` (§4.3 table;
worst headroom 7.96x)". Referee finding R1: 7.96x is the margin of the
CELL part only; the certificate also rests, for every
`tau <= tau_start(W)`, on the E.5.2 analytic floor
`q(W) (1/(1+tau^2) - 2 gamma*)`, whose certified margin over `b(W)` at
`tau = tau_start` is far thinner.

**The fix (recorded rewording of both headline sentences).** Read every
"worst headroom 7.96x" headline as:

> All certificates PASS. Worst CELL headroom **7.96x** (E.5.3, W7);
> the thinnest certified link of the WHOLE certificate is the analytic
> floor at the crossover `tau_start`, **1.30x (W7, at
> `tau_start = 0.7275`; 1.43x at W1)** — downstream consumers and
> repair sessions must budget off THESE crossover margins, not off
> 7.96x. The TRUTH at the W7 crossover is comfortable
> (`delta_norm(40, 0.7275) = 0.1615 ~ 16x b(W7)`): the bound is thin
> there, not the fact.

(For precision: W7's cell table row has `tau_c' = 0.7326`,
`tau_start = 0.7275` — the two numbers STATUS_wave4 prints as
"0.7326/0.7275". The 1.30x margin is at `tau_start = 0.7275`.)

**Verification (this batch, EXACT rational — stronger than the
referee's dps-30).** Script block [C] recomputes
`ratio(W) = q(W) (1/(1+tau_start^2) - 2 gamma*) / b(W)` as an exact
Fraction from the draft's own §7.2 table constants, all seven bands:

```
W1 1.4288x  W2 1.4409x  W3 1.7068x  W4 1.7735x  W5 1.9243x  W6b 1.8653x  W7 1.2971x
```

worst = **1.2971x at W7** — confirming the referee's dps-30 list
(agreement <= 3e-4 on every band; the tiny fourth-digit differences are
in the referee's favor of caution and do not move the 1.30x/1.43x
headline). The 7.96x cell figure itself is unchanged and correct AS the
cell-part margin (draft §4.3/§7.2 table, verified by both referees).

### 3.2 R2 — "(verbatim table)" relabel

**Issue:** §7.2 heads its table "(verbatim table)" but the archived
`out_sl3p_s2b.txt` rows carry a trailing `worst cell (w1c,t1,t2)=(...)`
field the draft drops. **Fix (recorded):** read the §7.2 header as
"(condensed; full rows archived in `out_sl3p_s2b.txt`, referee re-run
byte-identical)". Established repair class wp3-a2-F7 / assembly MR-3.

### 3.3 R3 = numerics F1 — the E.6.B corner decomposition numbers

**Issue, quoted (draft §5.2 and §8):** "the true corner slack is
`~0.004`; the cell bound concedes `~0.0026`" and "(A first pass at
`d lam = 0.002` FAILED — the `sinh^2(l2/2)` edge loss `~coth(lam/2)
d lam` exceeds the true slack `~0.004` near `lam = 0.30` ...)". Both
referees measured the truth independently: the TRUE slack at the regime
corner `(lam, tau) = (0.30, 0.58)` is **`~0.0027`** (`0.002673`,
two-resolution referee measurement; the route file's own NC3 normalized
floor `0.007921 x 0.3364 = 0.00266` agrees), so the cell bound
`0.001448` concedes **`~0.0012`**, not `~0.0026`. **Fix (recorded):**
in §5.2 and §8 read "true slack ~0.0027; the cell bound concedes
~0.0012"; in §5.2's mechanism sentence read "exceeds the true slack
~0.0027" (note the coarse edge loss `~0.0033` exceeds 0.0027 but would
NOT exceed 0.004 — the correction makes the recorded coarse-grid FAIL
story consistent, as the numerics referee observed). Verified here as
arithmetic (block [D]): `0.002673 - 0.001448 = 0.001225`. The certified
`+1.448e-3`, the PASS, and the safe direction (truth > certificate) are
unaffected.

### 3.4 R4 = numerics F2 — the ~1e-14 `tau = 0.8` float-edge sliver

**Issue:** §4.3/§5.2 say the cells "tile `[band] x [tau_start, 0.8]`"
(resp. the E.6.B box), but the fp-`arange` top `tau`-edges land at
`0.8 - 5.3e-15` (W5), `0.8 - 2.7e-15` (W6b), `0.8 - 1.6e-15` (W7) in
script B and `0.8 - 2.4e-14` in script C — read as exact real
intervals, the run certificates stop an `O(1e-14)`-wide sliver short of
`4/5`, while Theorem SL3' claims the closed endpoint. **Fix (recorded,
the referees' one-sentence route):** the certificate-class flag of §7
is read as including the float-edge convention — the certified
functions are `C^1` with `O(1)` `tau`-derivatives, so continuity
against the certified top-cell margins (`>= 2.86e-2` script B,
`>= 1.45e-3` script C) closes the `O(1e-14)` sliver with ~11 orders of
magnitude to spare; W1–W4 and both `lam`-grids overshoot their
endpoints (no sliver). The word "tile" must not be quoted against exact
endpoints without this remark. (The alternative repair — append-0.8 and
re-run — remains available to any future re-run; not needed for
citability per both referees.)

### 3.5 R5 = numerics F3 + trivia — display corrections

Recorded errata, each verified in block [D] where numeric:

- (i) §2's "`4.04 (1/4 + 1/401) ... = 1.0202`": the exact value is
  `1.020075`; read "`<= 1.0201`" (or print `1.02008`). Verified exact:
  `4.04 (1/4 + 1/401) = 1.020075` and `<= 1.0201` is True. The consumed
  constant is `<= 1.03`; safe direction throughout.
- (ii) §1/§5.3's "`eps_t = 1/sinh^2(3.925) = 1.5603e-3`": true value
  `1.560224e-3` (nearest print `1.5602e-3`); read the "=" as "`<=`"
  (up-rounded safe bound; the in-lemma comparison uses the exact
  value, and `<= 1.57e-3` holds — verified, block [D]).
- (iii) §7 preamble's "a stated guard (1e-6 ...)": the explicit `1e-6`
  guard exists in script C (Part B) only; script B's effective guard is
  its macroscopic certified margin (`>= 2.86e-2`). Read the flag with
  that half-sentence.
- (iv) Script A's c1/c2 grid endpoint values `0.999645`/`1.000021` are
  small-`v` float-cancellation artifacts in the UNUSED directions
  (draft §1.3); `1.000021 > 1` does not contradict the exact
  `S`-series claim.
- (v) (numerics F5, record) script C's `lam`-edge array has 1192 edges
  (fp `arange` emits an extra `0.40` edge) giving one harmless
  near-degenerate cell; the printed "1191 lam-rows" = len-1 is
  consistent.

## 4. Item (4): `wave2_repairs_20260811.md` — the W-F1 relabel

**The issue, quoted.** `referee_wave2_repairs.md` W-F1 ("the one
substantive repair — §D status label"):

> §D's header "— PROVED (exact finite computation)" and its sentence "so
> exact coverage through `m = 540` closes BOTH gap bands ... no
> uncovered `m` remains" assert a computation that has not completed:
> `results_m540.txt` has no OVERALL line and stops at `m = 481`.
> Relabel §D "IN PROGRESS — run died at `m = 481`; every completed row
> PASS; claim becomes PROVED when `results_m540.txt` ends with
> `# OVERALL: PASS` ..." (or equivalent), and put the band-closure
> sentence in the conditional.

The offending text (`wave2_repairs_20260811.md` §D header, line 407, and
the band-closure sentence at lines 423–425) is quoted verbatim in §2.3 of
the referee report and re-checked here: script block [A] confirms
`results_m540.txt` indeed carries NO `# OVERALL` line and its last data
row is `m = 481` (verbatim check: `m540 last data row m = 481 (== 481:
True), m540 has NO overall line: True`).

**The fix (recorded relabel).** Read `wave2_repairs_20260811.md` §D's
header as:

> ## §D. Harness extension toward m = 540 — RUN DIED AT m = 481 (every
> completed row `4 <= m <= 481` PASS, exact); COMPLETED BY THE
> SUCCESSOR RUN `harness_m560/run_m560.py` (`# OVERALL: PASS`,
> `4 <= m <= 560`)

and its band-closure sentence in the completed form: "exact coverage
through `m = 560` (rows `4..481` from `results_m540.txt`, `482..560`
from `results_m560.txt`) closes BOTH gap bands `[401, 534]` and
`[401, 536]`: no uncovered `m` remains for G4's part (c) at `K = 4`."
This is exactly the referee's demanded relabel, instantiated with the
completion the referee itself anticipated ("now mooted in substance by
the completed m560 run" — STATUS_wave4 §1 row 7); the conditional form
the referee offered is discharged, not merely restated, because the
`# OVERALL: PASS` condition is now verified on disk (block [A], §5).

**Effect (per the referee's own citability paragraph).** With W-F1
applied, the §2a/§2b/§2c discharges and the §C repaired-form citability
of T.10(2)/T.8'' move from "provisional" to refereed (single-verifier).
W-F2–W-F6 are observations/trivia recorded in the referee report; no
action beyond their on-record status is required, and none is taken
here.

## 5. Verification script and outputs

**Script (SAVED + RUN):**
`/Users/sihaohuang/Desktop/Coding/proof_hunter/phase2/bruhat/f2_drafts/g2_scripts/campaign_20260811/wave5_hygiene/hygiene_checks.py`
**Archived outputs:** `out_hygiene_checks_fast.txt` (blocks [A]–[D]),
`out_hygiene_checks.txt` (all blocks incl. [E]). Both runs end
`OVERALL ...: PASS` (exit 0).

| block | mode | validates | key output (verbatim) |
|---|---|---|---|
| [A] | EXACT parse | items (1), (2), (4): coverage + OVERALL + W-F1 support | `union coverage: m in [4, 560]; gaps in [4, 560]: []`; `FAIL rows anywhere: 0`; `W-F1 support: m540 last data row m = 481 (== 481: True), m540 has NO overall line: True`; the m560 OVERALL line quoted in §1/§2 above; `BLOCK A PASS: True` |
| [B] | EXACT parse, record-only | §2.3 fresh-run state | `fresh file: 438 data rows, m in [4, 441], gaps: [], FAIL rows: 0, OVERALL lines: 0 (0 => still incomplete)`; `byte-identity vs primary rows on overlap [4, 441]: mismatches: []` |
| [C] | EXACT Fractions | item (3) R1: crossover margins | `W7: ana(tau_start) = 0.012768 ratio = 1.2971x (referee dps-30: 1.2971x, agree to 5e-4: True)`; `worst certified crossover margin: 1.2971x at W7 (claim: 1.30x-class at W7): True`; `BLOCK C PASS: True` |
| [D] | EXACT (one float, labeled) | item (3) R3/R5 numerics | `4.04*(1/4 + 1/401) = 1.020075 exactly (... <= 1.0201: True ...)`; `eps_t = 1/sinh^2(3.925) = 1.560224e-03 (nearest 1.5602e-3; <= 1.57e-3: True ...)`; `E.6.B corner: true slack 0.002673 - cell bound 0.001448 = 0.001225 concession (~0.0012, NOT ~0.0026: True)`; `BLOCK D PASS: True` |
| [E] | EXACT bigint/Fraction rebuild to m = 560 | item (2): footer varfit checkpoints | `varfit(534) exact -> 0.997978810615 footer: 0.997978810615 match: True` ... `varfit(560) exact -> 0.998072591511 footer: 0.998072591511 match: True` (all six 12/12 digits); `BLOCK E PASS: True` |

Final line of `out_hygiene_checks.txt`, verbatim:

```
OVERALL (blocks A/C/D/E): PASS
```

Notes: block [C] is exact-rational on the draft's §7.2 table constants,
so it does not merely reproduce the referee's dps-30 evaluation — it
certifies the crossover ratios exactly (the referee's four bands that
differ do so only in the 4th digit, `<= 3e-4`, and the worst-band
identity W7/1.2971x is exact agreement). Block [E]'s recurrence is the
verbatim `next_poly` running-sum of the twice-refereed harness family;
its match on all six checkpoints is an independent end-to-end recompute
of the completed run's footer, complementing block [A]'s parse and the
fresh run's byte-identity through 441.

## 6. Ledger effect

With this batch on record (read the four target files THROUGH this
overlay):

1. **SL-sliver:** repair m1 executed (plus m2–m6 recorded); the piece
   stands at its full two-referee grade with no pending insert —
   **CLOSED (PROVED, finite closure)**; certified CL threshold
   **`m >= 561`** (the interim `m >= 555` reading is retired).
2. **Harness m560:** `harness_m560_20260812.md` §2/§3 are filled (§2 of
   this file); the note + this addendum are self-contained and citable
   for `4 <= m <= 560` exact coverage, with the footer varfit
   checkpoints now independently recomputed exactly.
3. **Theorem SL3':** the §2b repair list R1–R5 is applied as recorded
   errata; the two-referee MINOR_REPAIRS grade has its repairs
   discharged. Consumers MUST budget off the corrected margin
   headline: worst certified margin **1.30x** (W7 crossover
   `tau_start = 0.7275`; 1.43x W1), worst CELL headroom 7.96x, truth at
   the W7 crossover ~16x.
4. **wave2_repairs:** W-F1 relabel applied in completed form; per its
   referee, the §2a/§2b/§2c discharges and T.10(2)/T.8'' repaired-form
   citability stand refereed (single-verifier).

**Not changed by this batch (explicitly):** CL(79, 20, 0.89) remains
OPEN for `m >= 561`; Theorem A remains PROVED CONDITIONAL on exactly CL;
SL4' remains NOT citable (its §2c repairs and both referee passes are a
separate wave-5 task); `wave3_repairs_20260812.md` still awaits its
verifier; SL1'-w, SL4'-E, SL4'-X still have no proof artifact;
`gamma = 1/8` untouched. The remaining wave-5 work is exactly
STATUS_wave4 §3 items 2–6.

*Editor's note on the fresh re-run:* record-only state at `m = 441`
(stalled, byte-identical so far); its completion or relaunch changes no
grade in this ledger.

*End of wave4_hygiene_20260812.md.*
