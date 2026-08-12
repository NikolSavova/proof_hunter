# referee_maths_wave4_sliver — adversarial MATHS referee report on `wave4_sliver_20260812.md`

*Wave-4 referee (maths half, house rule), F2 campaign, 2026-08-12. Target:
`wave4_sliver_20260812.md` (SL-sliver bridge piece, finite closure) + its
script `g2_scripts/campaign_20260811/wave4_sliver/sliver_sizing.py` and both
archived outputs. Also read in full: `wp4_draft_composite.md` (§5.2/§5.3, §0
band table, SL4' display, Lemma C.1, Theorem A3), `STATUS_wave3.md`,
`referee_maths_wp4.md`, `referee_numerics_wp4.md` (§2 A2, §3.1 REF-B),
`harness_m560_20260812.md`, `harness_m560/run_m560.py` (full source),
`referee_wave2_repairs.md` (bears on flag f1), the relevant sections of
`theoremA_assembly_20260811.md` (§2.1–§2.5 part structure, flip instruction),
and both harness results files on disk. `g2_draft_t1_20260803.md` not read
(house rule). Default posture: REFUTATION — this chain flips a paper's main
conjecture to a theorem, so the bar is maximal. My own checks: every quoted
number re-traced; Lemma SLV.1 re-derived by hand AND re-certified by an
independent exact script with differently-built brackets; the harness runner
audited at source level; honored rows attacked by from-scratch recomputation;
the note's script re-run and diffed. Referee script (SAVED and RUN
2026-08-12, output archived beside it):
`/private/tmp/claude-501/-Users-sihaohuang-Desktop/0c711691-81ac-42b2-8712-819b1ee08f6b/scratchpad/ref_slv_indep.py`
(+ `out_ref_slv_indep.txt`, `out_sliver_rerun.txt`). No existing file
modified; this file is new.*

## Verdict: **MINOR_REPAIRS**

The piece's two load-bearing claims both SURVIVE adversarial checking:

- **Lemma SLV.1 (exact sizing certificate)** is correct. I re-derived every
  step by hand (w-direction, integer-step m-monotonicity, both endpoint
  brackets, all rounding directions) and re-certified the whole chain with
  an independent exact-rational implementation using differently-built
  brackets (14-digit mpmath-sourced 2pi interval, isqrt-based sqrt brackets,
  N = 320 exponential partial sums, 4-term Taylor lower bound for
  `e^{0.1482}`). Same verdicts, same digits (§2 below).
- **Fact SLV.2 / the finite closure** is correct and is now — at referee
  time — backed by a COMPLETED run: `results_m560.txt` ends with
  `# OVERALL: PASS -- all of C1..C6 hold exactly for 4 <= m <= 560`, rows
  `482..560` contiguous and PASS (my own gap/FAIL audit, independent of
  script [B]), `results_m540.txt` rows `4..481` contiguous and PASS. The
  sliver trapezoid `[401, 450]` is covered with 110 rows of slack. I
  additionally attacked flag f1's honored rows directly: a from-scratch
  independent reimplementation (different loop structure, sanity-anchored at
  `m = 4` and coefficient sums `= m!`) reproduces rows 449, 450 (honored)
  and 482 (fresh) exactly — C1/C2/C3/C4/C5 all re-certified, printed varfit
  displays matched digit-for-digit, and the C6 chain across the resume
  boundary `481 -> 482` re-verified exact (§3).

The repairs (§5) are finalization/hygiene-level: the note is still in its
self-declared "pending §3.1 final-audit insert" state (its headline `M_H =
560` / threshold `m >= 561` were ANTICIPATED values at writing time, with
the certified fallback `m >= 555` honestly stated); one band mislabel
(`W1 = (4, 6]`); one scope mismatch between Fact SLV.2's `[4, M_H]` and what
script [B] actually certifies; two attribution slips. Nothing moves a
constant, a verdict, or the piece's PROVED (finite closure) status. **To be
unmistakable about what this verdict covers: the SL-sliver piece is a
consumer-level finite closure, exactly as composite §5.3(b) defines option
(b). It does NOT prove CL on `[401, 450]` as a lemma about
`eps(k) min(m, s2)` — and the note says so explicitly. CL itself remains
OPEN for `m >= 561`; SL1'/SL3'/SL4' remain the outstanding bridge.**

## 1. The obligation and the interfaces (historical failure mode) — ALL CLEAN

- **§0's quote of composite §5.3 (SL-sliver)**: verbatim-true, ellipses
  correctly marked. Option (b) is quoted with its own closure semantics
  ("close the sliver FINITELY and shift CL's threshold statement"), and the
  note executes exactly that — the discharge form is pre-authorized by the
  refereed composite, not invented here.
- **Entry form**: `far'(m, w) = sqrt(2pi) m s2cap^{3/2} e^{-0.0741 m}`
  matches composite §5.3's SL4' display (`far' = sqrt(2pi) m s2max^{3/2}
  e^{-0.0741 m}`) with `s2cap = m^3/w^2 >= m/(4 sinh^2(lam/2)) >= s2max`
  (the display's elided `min(..., ...)` can only shrink `s2max`); since
  `x^{3/2}` is increasing, the note's majorant dominates the display's
  entry, so certifying the majorant `<= 0.05` certifies the display. Safe
  direction verified.
- **Cap chain**: Lemma C.1 is cited verbatim (`s2 <= m/(4 sinh^2(lam/2))`,
  composite §1 — PROVED, three proofs, two-referee via the composite);
  `sinh x >= x` gives `m/(4 sinh^2(lam/2)) <= m/lam^2 = m^3/w^2` — I
  re-derived it: `4 sinh^2(lam/2) >= 4 (lam/2)^2 = lam^2`, and
  `m/lam^2 = m/(w/m)^2 = m^3/w^2`. Correct, and larger-cap-only-enlarges
  is the right direction for an upper certificate.
- **Floor `0.0741`**: consumed as Theorem A3(ii)'s `P3` exponent constant.
  Lineage verified: composite §1 (`P3 = 0.3134 m^{5/2} e^{-0.0741 m}`),
  `referee_maths_wp4.md` §1.2 (hand re-derivation `q(2, 1) = 0.0741265`
  from wp1-c W.3's closed form), `referee_numerics_wp4.md` §2 A2
  (`q(2,1) = 0.07412654 >= 0.0741`, independent coding, plus the
  `0.0373 -> 0.0741` upgrade legitimacy). The note's provenance sentence
  quotes this faithfully. The far' display carries `e^{-0.0741 m}`
  literally, so using exactly `0.0741` is the display's own constant — no
  hidden direction issue.
- **Algebra of the reduction**: `sqrt(2pi) m (m^3/w^2)^{3/2} =
  sqrt(2pi) m^{11/2} / w^3` — checked. `w` enters only as `1/w^3`, so the
  sup over `w >= 4` is at `w = 4` — covers the sliver band `(4, 4.51]` and
  every `w > 4` (but see repair m3: the note's "(all of) W1 `(4, 6]`" is a
  band-table slip; composite §0 has `W1 = (4, 5]`).
- **Consumer mechanism (Corollary SLV.3)**: checked against
  `theoremA_assembly_20260811.md`. Part I (§2.1) certifies EXACTLY the
  C1–C6 statements that `run_m560.py` certifies (same statements, same
  `m = 4` exceptions, same `C5` scope class); part II's R2 row consumes CL
  per-m (the chain `s2 >= v(7/10) m`, `lam <= 0.89`, budget arithmetic is
  pointwise in `m`); the analytic `187/216` crossover (`m* = 535/537`,
  assembly/STATUS_wave3 G4 account) sits BELOW the shifted threshold 561,
  so the `[537, 560]` tail of the old analytic range is harness-covered.
  The finite/analytic boundary at `560/561` is structurally isomorphic to
  the already-two-referee-certified one at `400/401` (in particular, no
  strict-increase claim crosses the boundary in either architecture). The
  note correctly DELEGATES the flip-time re-run (`assembly_checks.py` block
  C, band-2 margin `2.83e-4`) via flag f3 instead of claiming it — the
  correct protocol per STATUS_wave3 §3 item 5.
- **Circularity with Prop 3.5: NONE.** The harness is direct exact integer
  computation on Mahonian coefficients (no analytic input at all); Lemma
  SLV.1 is a free-standing inequality about a display form; its two
  imported ingredients (A3(ii) constant, C.1) are Prop-3.5-free per
  `referee_maths_wp4.md` §1.5. `r(k)` enters nowhere except through the
  harness's own exact ratios.
- **REF-B corroboration quotes** (SLV.3 item 3): verified verbatim against
  `referee_numerics_wp4.md` §3.1 (260 adversarial `k`, violations all zero,
  `max eps*min(m,s2) = 1.17187` at `w = 4.894`, 17.1x). Correctly labeled
  corroboration, not load-bearing.

## 2. Lemma SLV.1 — hand re-derivation + independent exact re-certification

Hand checks (all reproduce): `ln far'(451,4) = 0.9189 + 5.5 ln 451 -
0.0741*451 - ln 64 = -3.0460 -> 0.04755`; `far'(450,4) -> 0.050586`;
`(452/451)^{11} = e^{11 ln(452/451)} = 1.0246625`; `e^{0.1482} = 1.159746`;
step ratio `((m+1)/m)^{11/2} e^{-0.0741} < 1` iff `((m+1)/m)^{11} <
e^{0.1482}`, and `(1 + 1/m)^{11}` is strictly decreasing in `m`, so the
`m = 451` check propagates to all `m >= 451`. Script [A]'s safe directions
audited at source: `exp_lb` = positive-term partial sum `<= e^x` (so
`e^{-x} <= 1/exp_lb` — correct for the UPPER bracket); `exp_ub` = partial
sum + geometric remainder cap, valid for `x < N + 2` (here `x = 33.42 <
202` — I checked the remainder majorization `sum_{n>N} x^n/n! <=
t x/(N+1)/(1 - x/(N+2))`); `sqrt_ub/sqrt_lb` by exact squaring with
while-loop correction — sound; `2pi` bracket `[6.283185306, 6.283185308]`
correct.

Independent re-certification (`ref_slv_indep.py` [R1], different bracket
constructions end-to-end; verbatim output):

```
  (a) far'(451,4) <= 0.04754997  <= 1/20: True
  (b) far'(450,4) >= 0.05058588  >  1/20: True
  (c) (452/451)^11 = 1.0246625 < 4-term e^0.1482 LB = 1.1597241: True
  (d) (452/451)^11 > (453/452)^11: True  (monotone dir ok)
  [R1] CERTIFIED independently: far'(m,w) <= 1/20 for all integer m >= 451,
       all w >= 4; boundary fails at (450, 4).
```

dps-60 truth values ([R2]): `far'(450,4) = 0.050585877`, `far'(451,4) =
0.047549967` (margin factor 1.05153), `far'(496,4) = 0.0028587324` (17.49x),
`far'(561,4) = 4.5555483e-5` (1097.56x) — every float the note quotes from
script [C] is confirmed. The [C] crude-floor calibration reproduces
independently ([R3]): `qW(4.05) = 0.0504452`, first closure at `m = 712` —
so the note's §1 "which sizing applies" logic (A3-floor governs; coverage to
536/560 would NOT have sufficed under the crude floor with this entry form)
is arithmetically right.

*Boundary-honesty nuance (no repair needed, recorded):* the failure point
`(m, w) = (450, 4)` is the INFIMUM edge of the sliver band `(4, 4.51]`, not
an interior point; at `m = 450` the entry still fits the slot for
`w >= 4.016`-class. The lemma's quantifier is over `w >= 4`, for which
`m0 = 450` is exactly right; the trapezoid membership of `m = 450` under
the strict band `(4, 4.51]` also holds (failure on `(4, 4.0156)`), so the
`[401, 450]` extent is honest either way.

## 3. Fact SLV.2 / the coverage — independently audited, honored rows attacked

- **Run state at referee time**: `results_m560.txt` now ends
  `# OVERALL: PASS -- all of C1..C6 hold exactly for 4 <= m <= 560 ...`
  (`elapsed this run: 429.6 s; new rows: 65; prior rows honored: 492;
  failures (new rows): 0`). My own parse, independent of script [B]:
  `results_m540.txt` rows `4..481` contiguous, zero FAIL; `results_m560.txt`
  rows `482..560` contiguous, zero FAIL; resume header verbatim as the note
  quotes (`# --- resume 2026-08-12 08:07:47: 492 m already certified,
  continuing to 560 ---`). **So the completed-run picture the note
  anticipated is TRUE**, and the promised mechanical refresh works: re-run
  of `sliver_sizing.py` reproduces blocks [A]/[C] byte-identically against
  BOTH archived outputs and block [B] refreshes to
  `contiguous PASS coverage: m in [401, 560] (gaps ...: []) ... M_H = 560;
  sliver m-extent [401, 450] covered: True ... OVERALL: PASS`
  (my `out_sliver_rerun.txt`).
- **Runner source audit** (`run_m560.py`): the honored-row logic rebuilds
  the exact polynomial through skipped `m` (the recurrence needs it) and
  recomputes `prev_varfit` at the last honored row as an exact Fraction
  from the central ratio — valid precisely because the skipped row's own C3
  PASS certifies min = central; the C6 chain is therefore exact across
  resume boundaries. The 2x symmetry scan is justified: I re-derived that
  for any `k > mid` the mirror `N - k <= mid` (both parities), so the
  min over `1 <= k <= N-1` equals the min over `1 <= k <= mid` AND the
  smallest-attaining `k` lies in `[1, mid]` — the tie-break is preserved,
  not just the value. `ROW_RE` honors only PASS rows (FAIL rows would be
  recomputed). Certificate statements C1–C6 match `run_m540.py` /
  `run_m200.py` and assembly §2.1's part-I list.
- **Flag f1 attacked directly** ([R4]): fresh implementation (different
  window-convolution code, anchored at `m = 4 -> [1,3,5,6,5,3,1]` and
  `sum = m!`), rebuilt to `m = 482` in 3.5 s; verbatim output:

```
  m=449: C1=True C4(N odd=False)=True C5(varfit>187/216)=True varfit=0.9975964887 matches printed row: True
  m=450: C1=True C4(N odd=True)=True C5(varfit>187/216)=True varfit=0.9976018257 matches printed row: True
  m=481: C1=True C4(N odd=False)=True C5(varfit>187/216)=True varfit=0.9977562685 matches printed row: True
  m=482: C1=True C4(N odd=True)=True C5(varfit>187/216)=True varfit=0.9977609202 matches printed row: True
  m=450: argmin(half-scan)=50512 == mid=50512: True; min ratio == central: True
  m=482: argmin(half-scan)=57960 == mid=57960: True; min ratio == central: True
  C6: varfit(449)>varfit(448): True; varfit(450)>varfit(449): True; varfit(482)>varfit(481): True
```

  The honored rows 449/450 (the sliver boundary!) and the resume-boundary
  pair 481/482 are thus re-derived from scratch and match the printed
  displays digit-for-digit. This does not RETIRE f1 (a full from-scratch
  re-run of `4..481` remains the gold standard the note itself offers), but
  it means the inherited rows survive targeted adversarial recomputation at
  exactly the points this piece leans on.
- **f1 is also staler than the note knows (safe direction)**:
  `referee_wave2_repairs.md` (2026-08-12 08:12, two minutes before the
  note's mtime) now exists — single-verifier MINOR_REPAIRS on
  `wave2_repairs_20260811.md`, which (i) verified `run_m540.py`'s diff
  against the twice-refereed `run_m200.py` is docstring/MMAX/checkpoint
  only, verdict path untouched, and (ii) recorded exactly one substantive
  defect (W-F1: §D's completion label), which the completed m560 run has
  now mooted in substance. The debt f1 describes is therefore already
  half-discharged; see repair m6.

## 4. What the piece does NOT claim — checked for grade inflation

The note's closing paragraph explicitly disclaims the lemma-level CL-truth
statement on `[401, 450]`; SLV.3's threshold restatement is presented as a
TARGET restatement for the wave-4 package, not as a proof of CL at 561;
REF-B is labeled corroboration, not load-bearing; flags f1–f4 are honest and
none hides a dependency. The "PROVED (finite closure)" self-grade is
accurate FOR THE PIECE AS DEFINED BY composite §5.3(b) — I attacked the
definition-fit first (§1) precisely because a consumer-level discharge
gradable as PROVED is only legitimate if the refereed composite itself
defines the piece that way. It does, verbatim.

## 5. Findings and repairs (none moves a constant, coverage bound, or verdict)

1. **m1 (the one that must be done before citation — finalize the pending
   state).** The note is self-declared "(pending §3.1 final-audit insert)"
   and internally mixes three coverage snapshots: abstract "`M_H >= 536` ...
   and `M_H = 560` on run completion", Fact SLV.2 "`M_H = 554` at final
   audit", SLV.3 "`m >= M_H + 1 = 561`" — while the honestly-certified
   fallback at writing time was `m >= 555` (§3.1). The run HAS now
   completed (`# OVERALL: PASS`, `4 <= m <= 560`; verified independently
   here and by the mechanical script-[B] re-run giving `M_H = 560`,
   gapless). Required: execute the note's own §3.1 refresh — archive the
   completed-run re-run of `sliver_sizing.py` (or adopt my
   `out_sliver_rerun.txt` figures), quote the `# OVERALL: PASS` tail
   verbatim, restate Fact SLV.2 with `M_H = 560` as CERTIFIED (not
   anticipated), and delete the 554/555 interim scaffolding or mark it
   superseded. Until this edit, every consumer must read the certified
   threshold as `m >= 555`, not 561. (The harness note's own §2/§3
   "[TO BE FILLED]" is its agent's debt, not this note's — but the note's
   self-containedness sentence about duplicating that tail becomes true
   only after this same insert.)
2. **m2 (scope of Fact SLV.2 vs what script [B] certifies).** [B] certifies
   no-FAIL-anywhere plus CONTIGUOUS PASS on `[401, M_H]` only (its `mh`
   walk starts at 401; `setdefault` takes first-occurrence verdicts and
   uniqueness is not checked — conflicting duplicates would surface only
   via the FAIL collector, which suffices, but gaps below 401 would not
   surface at all). Fact SLV.2 asserts `[4, M_H]`. The `[4, 400]` part in
   fact rests on `results_m540.txt` rows `4..400` (gapless — verified by
   this referee, not by [B]) and independently on part I's
   `harness_m200_20260811.md`. Either rescope the Fact to "`[401, M_H]`
   certified by [B]; `[4, 400]` per part I's existing citation" (flag f3
   already gestures at this) or extend [B]'s gap check to start at 4.
   One-line either way.
3. **m3 (band-table slip).** §2 step 1 says the `w = 4` sup "covers the
   sliver band `(4, 4.51]` and indeed all of W1 `(4, 6]`" (script comment
   likewise): composite §0 has `W1 = (4, 5]` (and `W2 = (5, 6]`). The
   certificate quantifies over all `w >= 4`, so nothing breaks — but this
   file must not enter the record teaching a wrong band edge. Print
   `W1 = (4, 5]` (or "all of `w > 4`").
4. **m4 (attribution).** §1's "(ASM-5's '~560-class' quote used its milder
   cap/edge variants)" — the `~560` figure is the ORPHAN Part C grid figure
   (`w >= 4.05` by `m = 560`), quoted through composite §5.2/§5.3; ASM-5's
   own output says `closes at m = 432 / 450`. Re-attribute (the
   mathematical point — that the crude floor with THIS entry form closes
   only at 712 — is correct and independently reproduced here).
5. **m5 (labeling).** SLV.3 item 2 attributes "`<= 4.56e-5`-class" to
   Lemma SLV.1; the LEMMA certifies `<= 0.05`, and `4.56e-5` is script
   [C]'s float diagnostic (display-only, as §2 itself labels it). Add the
   two words ("script [C], float") at that spot so the exact/float boundary
   stays clean inside a corollary statement.
6. **m6 (observation, safe direction — update f1).** Flag f1's "ZERO
   referees" description of `wave2_repairs_20260811.md` is now stale:
   `referee_wave2_repairs.md` exists (single-verifier MINOR_REPAIRS; its
   only substantive finding is mooted by the completed run; `run_m540.py`'s
   verdict path verified unmodified from the twice-refereed
   `run_m200.py`). Cite it in f1 and shrink the stated debt to what
   actually remains: no from-scratch recomputation of rows `4..481` by any
   referee (this report's [R4] covers 448–450/481 only).

**Thin margins, checked and accepted:** endpoint margin at `m = 451` is
5.15% (certified exactly; and genuinely never spent — the first analytic `m`
is `>= 555/561`, where the true entry is `2.9e-3`/`4.6e-5`-class); the
`(452/451)^{11}` monotonicity gap is enormous (1.025 vs 1.160); the
coverage slack over the trapezoid is 110 rows. No grid-sampled certificate
anywhere in the piece: [A] is exact-rational, [B] is an exact parse, [C] is
labeled float/display-only and consumed nowhere load-bearing.

## 6. Bottom line for the campaign ledger

- `wave4_sliver_20260812.md`: **MINOR_REPAIRS** — m1 (finalize the pending
  audit; mechanical, the completed run verifies), m2–m5 (text-level), m6
  (observation). With m1 applied, the piece stands as: **SL-sliver CLOSED
  (PROVED, finite closure) per composite §5.3(b)**, sliver trapezoid
  `w in (4, 4.51], m in [401, 450]` inside the exactly-verified
  `m in [401, 560]`, Lemma SLV.1 giving the SL4' far entry `<= 0.05` for
  all `m >= 451`, `w >= 4` (boundary exact at 450), and CL's target
  statement legitimately restated as `CL(79, 20, 0.89) for m >= 561`.
- What this does NOT change: CL remains OPEN (`m >= 561`); SL1'/SL3'/SL4'
  are still owed; the flip-time re-run of `assembly_checks.py` block C with
  the landed threshold is still owed (f3, correct protocol); the second
  (numerics) referee on this piece is still owed under the house rule —
  their heaviest remaining surface is a from-scratch re-run of the harness
  with the honored-files list emptied (the one thing neither this report
  nor any prior referee has done in full).

*End of referee_maths_wave4_sliver.md.*
