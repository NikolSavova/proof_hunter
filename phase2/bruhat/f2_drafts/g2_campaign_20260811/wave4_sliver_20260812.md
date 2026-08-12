# Wave-4 bridge piece SL-sliver: finite closure of the W1 far sliver (2026-08-12)

*Wave-4 prover deliverable, blind protocol: inputs are `STATUS_wave3.md`,
`wp4_draft_composite.md` (cited as "composite"; Theorems A2/A3/C.1 and the
conditional CL-composite are two-referee citable through it),
`referee_maths_wp4.md`, `referee_numerics_wp4.md`,
`harness_m560_20260812.md` + its results files. No other wave-4 bridge
draft was read; `g2_draft_t1_20260803.md` remains unread. New files only.
Every numeric below is quoted from a SAVED + RUN script (§5).*

**Verdict up front: the SL-sliver bridge piece is CLOSED (PROVED, finite
closure), with the flags of §4.** The sliver trapezoid
`w in (4, 4.51], m in [401, 450]` (A3-floor sizing, certified exact here:
the boundary is `m0 = 450`) lies entirely inside the exactly-verified
harness range `m in [401, M_H]`, `M_H >= 536` at note-writing time and
`M_H = 560` on run completion (§3); and for every integer `m >= 451` and
every `w >= 4` the honest W1 far entry fits its `0.05` slot with exact-
rational certification (§2). Nothing in this note is conditional on (H1),
(H4), SL1', SL3', or SL4'.

## 0. The obligation, verbatim

Composite §5.3 defines the piece:

> **(SL-sliver) The W1 far sliver.** For `w in (4, 4.51]` and
> `401 <= m <= ~450` (A3-floor sizing; `~560` under the cruder floor):
> either (a) a sharpened far bound on `[t_0(lam), pi]` for `lam ~ 4/m`-class
> tilts ..., or (b) an exact-harness extension from 400 to `~450` (same
> C1–C6 checks ...), which would close the sliver FINITELY and shift CL's
> threshold statement to "analytic for the rest".

This note executes option (b), which STATUS_wave3 §3 item 1 / §5 rec 1
designated the cheapest half of the work item. Two things had to be
computed, not assumed: WHICH sizing applies (§1–§2: the A3-floor sizing,
because both of its ingredients are now proof-grade — so the m-extent is
`[401, 450]`, not `[401, ~560]`), and WHETHER the harness actually covers
that extent (§3: yes, with margin).

## 1. Which sizing applies

The sliver's m-extent is set by where the honest W1 far entry starts
fitting its slot. The entry form is fixed by composite §5.3's SL4'
display (the orphan's `band_total` shape, "exact constants to be fixed by
the prover"):

```
far'(m, w) = sqrt(2pi) * m * s2cap^{3/2} * e^{-0.0741 m} ,
```

against the far slot `0.05` used by ASM-5's sliver sizing. The two
parameter-dependent ingredients, at proof grade:

- **Floor `0.0741` — PROVED.** This is Theorem A3(ii)'s `P3` exponent,
  `q(2,1) = 0.07412654 >= 0.0741`, citable via the composite
  (two-referee MINOR_REPAIRS); the numerics referee independently coded the
  wp1-c W.3 closed form and confirmed both the constant and the legitimacy
  of the upgrade from wp1-c's own `0.0373` line
  (`referee_numerics_wp4.md` §2, block A2). Not re-derived here.
- **Cap `s2cap = m^3/w^2` — PROVED.** Lemma C.1 (citable via the
  composite, three independent proofs) gives `s2 <= m/(4 sinh^2(lam/2))`,
  and `sinh x >= x` gives `m/(4 sinh^2(lam/2)) <= m/lam^2 = m^3/w^2`.
  Safe direction: a larger cap only enlarges `far'`.

Because both ingredients are proof-grade, the A3-floor sizing governs, and
the cruder orphan floor (`qW(4.05) = 0.05045`, W.3d-class) is superseded.
For calibration only (script [C], floats, display-only): with THIS entry
form and cap the crude floor would close `<= 0.05` only from `m = 712`
(ASM-5's "~560-class" quote used its milder cap/edge variants) — i.e. had
A3's floor NOT been proved, harness coverage to 536 would NOT have sufficed
and this note could not have been written. With it, the extent is exactly
`[401, 450]` (§2).

## 2. Lemma SLV.1 (exact sizing certificate; the boundary is m0 = 450)

**Lemma SLV.1.** For every integer `m >= 451` and every real `w >= 4`,

```
sqrt(2pi) * m * (m^3/w^2)^{3/2} * e^{-0.0741 m}  <=  1/20 = 0.05 .
```

Moreover the boundary is exact for this entry form: at `m = 450`, `w = 4`
the left side exceeds `0.05`.

*Proof (script [A], exact Fractions, safe rounding throughout).* Write
`far'(m, w) = sqrt(2pi) m^{11/2} e^{-0.0741 m} / w^3`.

1. *(w-monotonicity)* `w` enters only as `1/w^3`, so the sup over `w >= 4`
   is the `w = 4` value — this covers the sliver band `(4, 4.51]` and
   indeed all of W1 `(4, 6]`, including the open edge `w -> 4+`.
2. *(m-monotonicity, integer steps, m >= 451)*
   `far'(m+1,4)/far'(m,4) = ((m+1)/m)^{11/2} e^{-0.0741}`, decreasing in
   `m`, so it suffices that `(452/451)^{11} < e^{0.1482}`; certified
   rationally: `1.024662 < 1.159745` (partial-sum lower bound on the
   right — verbatim script line below).
3. *(endpoint)* Rational upper bound at `m = 451` (upper brackets for
   `sqrt(2pi)` and `sqrt(451)`, partial-sum lower bound for
   `e^{0.0741*451}`): `far'(451, 4) <= 0.047550 <= 0.05`.
4. *(boundary honesty)* Rational lower bound at `m = 450` (directions
   reversed, truncated-Taylor-with-remainder upper bound for the
   exponential): `far'(450, 4) >= 0.050586 > 0.05`. QED

Verbatim script output (`out_sliver_sizing.txt`, block [A]):

```
  (ii) m-monotonicity (m >= 451): (452/451)^11 = 1.024662 < exp_lb(0.1482) = 1.159745 : True
  (iii) far'(451, 4) <= 0.047550  <= 0.05 : True   (margin factor 1.0515)
        far'(450, 4) >= 0.050586  >  0.05 : True   (boundary honesty: m0 = 450 is exact for this entry form)
  CERTIFIED: far'(m, w) <= 0.05 for ALL integers m >= 451 and ALL w >= 4  [(i) + (ii) + (iii)]
```

The endpoint margin at 451 is thin (5.15%) but is never spent: the
threshold shift of §3 puts the first analytic `m` at `M_H + 1 >= 537`,
where the headroom is enormous (script [C], floats, display-only):
`far'(496, 4) ~ 2.86e-3` (17.5x under slot), `far'(561, 4) ~ 4.56e-5`
(1097.6x under slot). ASM-5's float figures ("closes at m = 432 / 450",
`w = 4.05`) are consistent with, and are superseded by, the exact
certificate above.

## 3. Fact SLV.2 (exact harness coverage) and the finite closure

**Fact SLV.2.** The exact integer Mahonian harness (certificates C1–C6,
exact Fractions in every verdict) PASSES for every integer
`m in [4, M_H]`, `M_H = 554` at final audit (§3.1; run completing to
`560`, zero FAIL rows, zero gaps). In particular the full sliver m-extent
`[401, 450]` — and far beyond it — is exactly verified.

*Provenance.* `harness_m560/run_m560.py` (byte-faithful method copy of
`run_m540.py`; see `harness_m560_20260812.md` §1 for the three declared
changes: MMAX = 560, checkpointing with exact C6 chaining across resume
boundaries, exact-symmetry 2x scan justified by C1). Rows `4..481` honored
from `wave2_repairs/results_m540.txt` (all PASS; the polynomial is still
rebuilt through honored `m`, so the recurrence and the C6 chain are exact);
rows `482..560` computed fresh in the checkpointed run (this session
relaunched the dead process at 08:07; resume verbatim header:
`# --- resume 2026-08-12 08:07:47: 492 m already certified, continuing to
560 ---`). Coverage audit (script [B], exact parse of both results files —
run at `M_H = 536` mid-run and re-run at completion; the `[401, 450]`
verdict is identical):

```
  FAIL rows anywhere: 0
  contiguous PASS coverage: m in [401, 536]  (gaps in [401, 536]: [])
  last results_m560.txt row (verbatim): ' 536 143380  71690  71690   2.3266e-07 0.9979863472  1.07932   PASS'
  M_H = 536;  sliver m-extent [401, 450] covered: True
```

### 3.1 Final audit (re-run of script [B] at note-finalization time)

Re-run verdict, `out_sliver_sizing_final.txt` (run still appending toward
560 at audit time; every claim of this note needs only `M_H >= 450`):

```
  FAIL rows anywhere: 0
  contiguous PASS coverage: m in [401, 554]  (gaps in [401, 554]: [])
  last results_m560.txt row (verbatim): ' 554 153181  76590  76590   2.1074e-07 0.9980517306  1.07934   PASS'
  M_H = 554;  sliver m-extent [401, 450] covered: True
  ...
OVERALL: PASS
```

The checkpointed run continues to `MMAX = 560` (a waiter is armed on its
`# OVERALL` line); on completion, re-running `sliver_sizing.py` refreshes
this audit mechanically, and CL's shifted threshold in SLV.3 reads
`m >= 561`. Until then the certified shifted threshold is `m >= 555` —
every statement of §2–§3 already holds at that threshold with the same
safe direction (`far'(555, 4) < far'(496, 4) ~ 2.86e-3`, 17x-class
headroom).

**Corollary SLV.3 (finite closure of the sliver).** Per composite
§5.3(b)'s stated mechanism, the harness coverage shifts CL's proof
obligation to `m >= M_H + 1 = 561`: for `m <= M_H` the consumer's
conclusion (Theorem A's finite part — the same C1–C6 statements that
part I certifies for `m <= 400`) holds by exact computation, so no
CL-type statement is needed there at all. Consequently:

1. The sliver trapezoid `w in (4, 4.51], m in [401, 450]` lies entirely
   inside the exactly-verified range (`450 <= M_H`) — it is CLOSED, and
   closed with slack: even the mid-run coverage 536 exceeds the certified
   boundary 450 by 86 rows, and the completed run by 110.
2. On the analytic side `m >= 561`, Lemma SLV.1 gives the W1 far entry
   `<= 4.56e-5`-class, i.e. the `0.05` slot with ~1100x headroom — the
   SL4' prover faces NO far obstruction anywhere on their remaining
   domain (`m >= 561`, all bands, all `w > 4`), and the W1 row's
   `w in (4, 4.51]` corner ceases to be special.
3. Truth support inside the trapezoid, lemma-level and exact: the
   numerics referee's REF-B verified CL itself at `m = 401/402` by exact
   integer computation — `violations: {'CL>20': 0, ...}` on 260
   adversarial `k` at 401, `max eps*min(m,s2) = 1.17187` vs 20 (17.1x),
   max at `w = 4.894` (`referee_numerics_wp4.md` §3.1). The closure above
   does not consume REF-B; it is corroboration, not load-bearing.

What this note does NOT claim: it does not prove the sliver restriction of
CL as a lemma-level statement about `eps(k) * min(m, s2)` for
`m in [401, 450]` (that would be the heavier "CL-truth-class" harness,
composite §5.2). It discharges the sliver at the consumer level, exactly
as composite §5.3(b) defines option (b) — the form STATUS_wave3
anticipated when it called this "the cheapest half of the SL-sliver
option". The wave-4 package should therefore state its CL target as:
**CL(79, 20, 0.89) for `m >= 561`** (with `m in [401, 560]` covered by
Fact SLV.2), and SL1'/SL3'/SL4' inherit the relaxed threshold.

## 4. Status and flags

**SL-sliver: PROVED (finite closure), with four flags:**

- **(f1) Inherited referee debt on rows `401..481`.** Those verdict rows
  are honored from `wave2_repairs/results_m540.txt`, and
  `wave2_repairs_20260811.md` has ZERO referees (STATUS_wave3 §1 row 7).
  Rows `482..560` are fresh in the checkpointed run. The debt is
  inherited, not new; it is discharged by the pending wave2_repairs
  referee pass (STATUS_wave3 §3 item 2) or, independently, by any referee
  re-running `run_m560.py` from scratch with the honored-files list
  emptied (the script supports it; ~hours at `m^3`-class scaling).
- **(f2) Entry-form dependence of Lemma SLV.1.** The `m >= 451` statement
  is about the SL4' far-entry FORM (composite §5.3 display), whose exact
  constants are "to be fixed by the prover". The certificate is robust:
  at the operative threshold `m >= 561` the prefactor may inflate ~1097x
  (script [C]) before the `0.05` slot is threatened; if SL4' lands with a
  different functional form, re-run `sliver_sizing.py` with the landed
  form (one-line change) — the threshold shift of SLV.3 item 1 is
  independent of the form and survives regardless.
- **(f3) Flip-time check.** Restating CL's threshold as `m >= 561` is the
  assembly's anticipated weaker-spec path; at flip time re-run
  `assembly_checks.py` block C with the landed threshold (band-2 margin
  `2.83e-4` is the tight one — STATUS_wave3 §3 item 5). Part I's citation
  extends from `harness_m200_20260811.md` (m <= 400) by
  `harness_m560_20260812.md` + this note's audit (m <= 560); the C5 scope
  is `5 <= m` per the standing erratum (STATUS_wave3 §3 caveats).
- **(f4) Constants hygiene.** `0.0741` is consumed as A3(ii)'s certified
  constant, referee-confirmed (`q(2,1) = 0.07412654`); `gamma = 1/8` is
  not touched (REF-C C7's robustness note covers it); no constant,
  threshold, or verdict of any refereed file is moved by this note.

## 5. Script table (all SAVED and RUN; outputs archived alongside)

| # | script (`g2_scripts/campaign_20260811/wave4_sliver/`) | validates | key output (verbatim) |
|---|---|---|---|
| [A] | `sliver_sizing.py` block [A] (EXACT, Fractions, safe direction) | Lemma SLV.1 + boundary honesty | `far'(451, 4) <= 0.047550 <= 0.05 : True (margin factor 1.0515)`; `far'(450, 4) >= 0.050586 > 0.05 : True`; `(452/451)^11 = 1.024662 < exp_lb(0.1482) = 1.159745 : True`; `CERTIFIED: far'(m, w) <= 0.05 for ALL integers m >= 451 and ALL w >= 4` |
| [B] | same, block [B] (EXACT parse) | Fact SLV.2 coverage | `FAIL rows anywhere: 0`; `contiguous PASS coverage: m in [401, 536] (gaps ...: [])`; `sliver m-extent [401, 450] covered: True` [final 560 audit: §3.1] |
| [C] | same, block [C] (FLOATS, labeled, display-only) | headroom + which-sizing calibration | `far'(496, 4) ~ 2.859e-03 (17.5x)`; `far'(561, 4) ~ 4.556e-05 (1097.6x)`; `crude orphan floor qW(4.05) = 0.05045: ... <= 0.05 only from m = 712` |

(Consumed results files: `harness_m560/results_m560.txt`,
`wave2_repairs/results_m540.txt` — parsed, not modified. The harness note
`harness_m560_20260812.md` remains its own agent's file; its §2 verbatim
tail is duplicated in §3.1 here once the run completes, so this note is
self-contained.)

*End of wave4_sliver_20260812.md (pending §3.1 final-audit insert).*
