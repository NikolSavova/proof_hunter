# referee_numerics_sol_s3 — adversarial NUMERICS referee on `sol_s3_20260812.md` (wave 6b)

*Cross-model refereeing, F2 campaign, 2026-08-12. Target: gpt-5.6-sol's attempt at
**(S3)** = (E3) = SL4'-E-J (`J = r31^2 - r42/2 <= J0(W)` on the deep-tilt band,
`m >= 561`). Mandate: maximal bar, default to refutation; script the draft's
VERIFICATION RECIPE; exact arithmetic where feasible; add the adversarial checks
the recipe omits; confirm no Prop E.3 smuggling; check the J0(W) thresholds
against the wave-6 scout's recomputed (grown) values. Sources read:
`sol_s3_20260812.md`, `STATUS_wave5.md`, `CL_composition_20260812.md` (§4 (S3)),
`wave5_sl4pe_20260812.md` (Lemma E.2, Prop E.3, §6 roadmap) + its archived
`out_e1_pricing_certificate.txt` (exact J0 fractions),
`wave6_s1_plan_20260812.md` + `wave6_scout/out_scout_s1_targets.txt` (new exact
J0 fractions), `wave6_sol/run_sol.py` (provenance). NOT read:
`g2_draft_t1_20260803.md`. No existing file modified; this file and the scripts
below are new.*

**Scripts (all SAVED and RUN, outputs archived beside them, quoted verbatim
below), in `g2_scripts/campaign_20260811/wave6b_ref_s3/`:**

| # | script | what it checks | output |
|---|---|---|---|
| 1 | `ref1_identities.py` | SOL.1/SOL.2 identities, series coefficients, EM constants, zeta(2) enclosure, P_n, brute-force cumulants, reflection, G_n, EM remainder audit, true size of h^(8) | `out_ref1_identities.txt` |
| 2 | `ref2_bands.py` | SOL.7 band-bound truth attack (W1–W6b), binding point | `out_ref2_bands.txt` |
| 3 | `ref3_w7.py` | W7 lemma: exact lam->0 limits, U7/floor scans at the draft's own cell counts, h_3 monotonicity, real-corner chains, SOL.15/SOL.13 spot checks | `out_ref3_w7.txt` |
| 4 | `ref4_floors.py` | exact-Fraction floor checks, REM* recovery, stale-vs-grown J0, final comparisons, box count | `out_ref4_floors.txt` |
| 5 | `ref5_gapcontrol.py` | scan-gap control (max sampled derivatives vs headrooms) — the check the recipe omits | `out_ref5_gapcontrol.txt` |

## VERDICT: **MAJOR_ISSUES**

**One sentence:** every number, identity, constant, and bound in the draft that
CAN be tested tests TRUE — the architecture is sound, the claimed sup bounds
hold at truth level with 7.9–46% headroom, the thin W7 margins are real but
positive, no Prop E.3 smuggling, and the stale J0 table is exactly the safe
direction — but the draft's central certificate (Lemma SOL.3's 18,874,368-box
exact interval computation and the SOL.16/SOL.17 interval evaluations) **was
never executed anywhere** (F1): the draft asserts its outputs ("the six
resulting exact checks are … True") as accomplished facts with no script and no
archive, which is precisely the artifact class the house rules exist to reject.
(S3) therefore remains OPEN; the draft is a strong, likely-certifiable proof
PLAN with verified constants, not a proof.

## 1. Provenance finding (load-bearing): the certificate does not exist

`wave6_sol/run_sol.py` is an API driver; it generated the draft text and ran
nothing else. There is no checker script and no output archive anywhere in the
campaign tree for: the SOL.5 certification ("certified in exact rational
interval arithmetic … on each of the 39*256 intervals"), the Lemma SOL.3 table
("The six resulting exact checks are … True", 18,874,368 boxes), or the Lemma
SOL.4 certificate ("Exact rational interval evaluation gives (SOL.16) …
(SOL.17)"). Every "True" in the draft's body and every "expected output" block
in its recipe is a prediction, not a result. House rule (every numeric from a
SAVED+RUN script with output quoted) is violated by the draft's own load-bearing
lemmas. Where those predictions were testable at truth level, they all came out
TRUE (below) — which is evidence the plan will certify, and is why this verdict
is MAJOR_ISSUES rather than FATAL — but a numerics referee cannot pass an
unexecuted computation, and the missing piece is the proof's core, not a
side-check.

## 2. Identity- and lemma-level checks (script 1) — ALL PASS, one constant flaw

Verbatim from `out_ref1_identities.txt` (dps 30–60 mpmath + exact sympy):

- **[A1]** the three phi_n closed forms match `sum k^{n-1} q^k` to q^30
  (exact coefficient comparison): `True/True/True`.
- **[A2/A3]** `h_2(0)=1, h_3(0)=2, h_4(0)=6`; **every** SOL.2 series
  coefficient (through x^10, all three functions) matches the exact
  Bernoulli-formula values; odd coefficients vanish (so the omitted
  odd-derivative endpoint terms in SOL.13 are exactly zero):
  `all printed SOL.2 coeffs match: True` (x3).
- **[A5]** the recipe's zeta(2) enclosure `1644934066848226/10^15 < zeta(2) <
  …227/10^15`: `True` (zeta(2) = 1.644934066848226436…).
- **[A6]** P_2/P_3/P_4 match; the tail identity `int_w^inf h_n = sum_k
  e^{-kw} P_n(kw)/k^2` reproduces quadrature to `rel.err = 0.0` at dps 30
  (w = 4, 7.5; n = 2, 3, 4).
- **[A7] Lemma SOL.1 is CORRECT:** brute-force tilted-Mahonian cumulants
  (exact Mahonian coefficient lists, m = 6 and 9) match
  `lam^n kappa_n = m h_n(lam) - sum_j h_n(j lam)` to rel. err `<= 1.4e-47`.
- **[A8]** the reflection claim (negative tilt: kappa_3 flips, kappa_2/kappa_4
  invariant) verified to `~1e-49` at m = 6.
- **[A9]** G_n via (SOL.2) vs direct quadrature: rel. err `<= 7.9e-40` at
  w = 4/5/20/40; `G_4(4) = 0.2323482989` (scout guard `0.2323483` — match).
- **[A11] the (SOL.5)/(SOL.14) bound 10^12 is TRUE with ~11 orders of slack:**
  true `max |h_n^(8)|` on (0, 40] = `0.232 / 1.393 / 6.952` (n = 2/3/4);
  `int_0^60 |h_n^(8)| = 0.401 / 2.357 / 12.53`.

**[A4]+[A10] — FINDING F2 (lemma-level constant flaw, numerically absorbed).**
The draft's remainder constant `2 zeta(8)/(2 pi)^8 = 1/1209600` is exactly
`|B_8|/8!` (confirmed symbolically). But (SOL.3) stops at the B_6 boundary term;
the Euler–Maclaurin remainder in the f^(8)-kernel form WITHOUT the B_8 boundary
term carries the kernel constant `(2 - 2^{-7})|B_8|/8! = 17/10321920`, i.e.
**1.992x the stated one** — as stated, SOL.4's (and SOL.13's) proof does not
establish its own inequality. Numerically immaterial here: at all 12 audit
points (m, w, n) the ACTUAL remainder satisfies even the draft's stated bound
with the TRUE `int|h^(8)|` (because `int|h^(8)| >= |Delta h^(7)|` with slack —
measured `|E|` equals the omitted-B_8-boundary-term size to 3 digits at every
point, e.g. `|E| = 8.319e-27` vs term `8.32e-27` at (561, 5, n=2)), and the
practical bound (SOL.6) with `H_8 = 10^12` has ~11 orders of headroom. Repair:
double the constant (or add the B_8 boundary term) in SOL.4 AND SOL.13 and
re-quote (SOL.6) as `2 * 10^12 w lam^8/1209600` — every downstream budget
absorbs 2x trivially (worst case W6b: bound contribution `4.4e-2` vs 0.78
headroom; on (0, L] in SOL.13: `~3e-14` vs the 0.0177 floor margin).

## 3. The SOL.7 band bounds (script 2) — TRUE at truth level, never certified

Verbatim from `out_ref2_bands.txt` (dps 30; exact integer-m sums for
m in {561, 562, 563, 570, 600, 750, 1000, 2500}, the m->infinity limit row,
w-grid step 1/128 + ~1/2050 near right edges + off-grid points
`edge - 1/3000`, `edge - pi/10000`):

```
  W1: max J = 0.46031849 at (w, m) = (5.0, 561); claimed sup 0.5; J <= sup: True (headroom 7.936%); min F2 = 1.19878 > 1/10: True
  W2: max J = 0.55031731 at (w, m) = (6.0, 561); claimed sup 0.65; J <= sup: True (headroom 15.34%); min F2 = 1.96731 > 1/10: True
  W3: max J = 0.66462617 at (w, m) = (8.0, 561); claimed sup 0.9; J <= sup: True (headroom 26.15%); min F2 = 2.84144 > 1/10: True
  W4: max J = 0.7235812 at (w, m) = (10.0, 561); claimed sup 1.1; J <= sup: True (headroom 34.22%); min F2 = 4.74529 > 1/10: True
  W5: max J = 0.84252011 at (w, m) = (20.0, 561); claimed sup 1.5; J <= sup: True (headroom 43.83%); min F2 = 6.72345 > 1/10: True
  W6b: max J = 0.92059223 at (w, m) = (40.0, 561); claimed sup 1.7; J <= sup: True (headroom 45.85%); min F2 = 16.7179 > 1/10: True
```

Every per-band max sits at the right edge at m = 561 (matching sl4pe's archived
worst `J/J0` row: 0.4603/0.5503/0.6646/0.7236/0.8425/0.9206) — the truth is
comfortably inside the claimed sup bounds, W1 the thinnest at 7.94%. The
binding point reproduces the draft's non-load-bearing truth check exactly:

```
  r31 = 0.88636451   (draft 0.8864, scout 0.88636)
  r42 = 0.6506471    (draft 0.6506, scout 0.65065)
  J   = 0.46031849   (draft 0.4603)
  J/J0(W1) = 0.67402288   (draft 0.6740)
```

The draft's joint-form remark is confirmed: at (561, 5), `r31^2 = 0.7856 >
1/2`, so dropping the `-F_4/(2F_2)` term indeed could NOT certify W1 —
consistent with (and not smuggling around) Prop E.3's truth-forcing.

**But:** these are scans. The draft's claim is an INTERVAL certificate over the
continuum `(w, z) in band x [0,1]` — that computation (18,874,368 boxes,
centered degree-6 Taylor models, exact rational comparisons) does not exist
(§1). Truth scans + gap control (§6) make its success very likely; they are not
it.

## 4. The W7 lemma SOL.4/SOL.16/SOL.17 (script 3) — TRUE, thin at lam -> 0+, never certified

Verbatim from `out_ref3_w7.txt`:

- **[B1] exact endpoint analysis (the check the draft never does):** the infima
  of both (SOL.16) floors and the supremum of U7 live at `lam -> 0+` and are
  closed forms in zeta(2):
  ```
  lim (h2 - dT2) = 1 - zeta2/20 = 0.917753296658  (> 9/10: True, margin 1.934%)
  lim (h4 - dT4) = 6 - 3*zeta2/5 = 5.01303955989  (> 49/10: True, margin 2.255%)
  lim U7 = 2.24254490453  (<= 12/5: True, margin 6.561%)
  ```
- **[B2] 20,493-point scan on (0, 0.89]** at the draft's own cell structure
  (4096 cells on (0, L], 16384 on [L, 0.89], L = 40/561) plus adversarial
  extras (log-spaced tiny lam, `L +/- 1e-9`, exact 0.89): the scan minima/
  maximum match the [B1] limits (monotone approach, no interior bump):
  `min(h2 - dT2) = 0.9177533 > 9/10: True`, `min(h4 - dT4) = 5.0130396 >
  49/10: True`, `max U7 = 2.2425447 <= 12/5: True`. So all four of the
  recipe's §5 "expected output" lines are TRUE — as predictions.
- **[B3] the monotonicity input SOL.4 needs but never states as a check:**
  `0 <= B <= m h_3` requires h_3 decreasing; verified `max h_3' on (0, 80] =
  -8.9e-30 < 0` (and termwise `h_3' < 0` for x >= 3 is elementary); also
  `h_2' < 0`.
- **[B4] 18 real-point corner chains** (m = 561 at w = 40+1/2048 … 499.29 =
  0.89*561; m = 562/1000/5000 incl. every lam = 0.89 corner): `J <= U7(lam)
  <= 12/5 <= 9/2` holds at every point; the campaign's binding deep corner
  gives `J = 1.32583` vs `U7(0.89) = 1.42766` — the draft's chain is not just
  true but tracks the truth closely there.
- **[B5]** the (SOL.15) tail bound is valid at all 9 spot checks (bound/truth
  ratios 1.04–8.7x), and the (SOL.13) representation is accurate to `~1e-28`
  at lam = 0.01/0.05/L (consistent with the odd-derivative endpoint terms
  vanishing exactly, [A2/A3]).

**Reading:** Lemma SOL.4's numeric content is fully TRUE, but its certificate
was never run (§1), its stated remainder constant in (SOL.13) inherits F2's
factor-2 flaw, and its margins are thin exactly where the draft is silent: the
9/10 floor clears by 1.93% with the infimum AT the open endpoint lam -> 0+
(the draft's 4096-cell partition of [0, L] must resolve a 0.0177-wide margin
near lam = 0 — cell width 1.74e-5 makes that easy, per §6, but the draft never
budgets it).

## 5. Exact floors, and the stale-vs-grown J0 table (script 4) — ALL EXACT CHECKS PASS

Verbatim highlights from `out_ref4_floors.txt` (pure `Fraction` arithmetic on
the ARCHIVED exact fractions, both generations):

- **[C1]** the draft's SOL.18 decimals match the archived wave-5 exact J0
  fractions (all 7 bands, e.g. W1 = 0.6829419319…).
- **[C2]** the draft's rational floors are valid: `17/25 <= J0(W1)` (slack
  0.002942), …, `9/2 <= J0(W7)` (slack 0.095970) — `ALL FLOORS VALID: True`.
  The W1/W2 floor slacks (0.0029/0.0027) are the thin ones — they hold, but any
  future REM* growth of ~0.003 would break the 17/25 floor; floors are pinned
  to the wave-5 REM* generation (see F3).
- **[C3]** the draft's "recovery" REM* list dominates the exact
  `REM* = J* - J0` on every band and `J* - ub` still clears every floor:
  `REM* recovery route valid: True`.
- **[C4] FINDING F3 (stale thresholds, SAFE direction — verified exactly):**
  the draft certifies against the WAVE-5 J0 row; the wave-6 scout recomputed
  (S3)'s thresholds at the re-architected targets and they GROW on every band
  (0.682942 -> 0.834155, …, 4.59597 -> 6.014761). Exact bandwise comparison of
  the two archived fraction rows: `old < new` on all seven — so a proof of
  `J <= J0_old` discharges (S3) under BOTH threshold generations, a fortiori.
  The draft nowhere says which generation it targets (it quotes the old row as
  "the exact quantities from Lemma E.2" with no version awareness — it was not
  shown the scout file); the repair is one paragraph, but without it the
  composition's (S3) statement and this proof's (S3) statement will silently
  diverge the moment the scout plan is adopted.
- **[C5]** the seven final comparisons (claimed sup vs floor) all strict, exact:
  `1/2 < 17/25`, …, `12/5 < 9/2`: `ALL SEVEN STRICT: True`.
- **[C6]** the box count `36*2048*256 = 18874368` is arithmetically right for
  the stated partition (36 w-units).

## 6. Scan-gap control (script 5) — the check the recipe omits

Sampled-derivative bounds (central differences, 2x safety) convert the §3/§4
scans into "no spike hides between grid points" evidence (scan-class, not
certificate-class). Verbatim from `out_ref5_gapcontrol.txt`:

```
  W1: max|dJ/dw| ~= 0.1202; m-spread <= 0.00047467; worst unsampled excursion (2x safety) = 0.0014137 vs headroom 0.039682; spike-proof at scan resolution: True
  W2: max|dJ/dw| ~= 0.10182; ... = 0.0012701 vs headroom 0.099683; True
  W3: max|dJ/dw| ~= 0.078001; ... = 0.0016702 vs headroom 0.23537; True
  W4: max|dJ/dw| ~= 0.039824; ... = 0.00097708 vs headroom 0.37642; True
  W5: max|dJ/dw| ~= 0.021854; ... = 0.0023531 vs headroom 0.65748; True
  W6b: max|dJ/dw| ~= 0.0071872; ... = 0.0033014 vs headroom 0.77941; True
  W7: max|dU7/dlam| ~= 13.332; excursion = 0.00066619 vs margin 0.156: True
      max|d(h2-dT2)/dlam| ~= 0.82845; excursion = 4.1397e-5 vs floor margin 0.0177: True
      max|d(h4-dT4)/dlam| ~= 10.108; excursion = 0.0005051 vs floor margin 0.11: True
```

Worst ratio anywhere: W1, excursion 0.0014 vs headroom 0.0397 (28x). This
also says the draft's certificate resolution (1/2048 in w, 1/256 in z; 4096 +
16384 cells on W7) is generously sufficient IF the interval arithmetic is
implemented as specified — the failure mode for the unexecuted certificate is
implementation, not resolution.

## 7. Prop E.3 smuggling audit — CLEAN

Prop E.3 (twice-refereed) kills the route "(E1)+(E2)+`kappa_4 >= 0` ==>
pricing/J-bound" — hypothesis-level magnitudes plus the bare sign allow
`J` up to `R31*^2 > J0` on every band. The draft does not touch that route: it
never assumes (E1)/(E2); it bounds `J` directly from the exact factor-cumulant
model (Lemma SOL.1, verified [A7]). On W1–W6b it keeps the joint form
throughout (and NEEDS to — §3: `r31^2 = 0.7856 > 1/2` at the binding point).
On W7 it uses a QUANTITATIVE fourth-cumulant floor (`h_4 - d T_4 > 49/10`,
i.e. `r42/2 >= (h_4 - dT_4)/(2 h_2) ~ 2.45`), which is exactly the
"quantitative descendant" route sl4pe §6 prescribes for W7 (needs only
`r42 >= 0.488`; the draft certifies ~10x that). No smuggling under any
notation I could construct.

## 8. Findings (ranked)

- **F1 (MAJOR / blocks acceptance).** The load-bearing certificates (Lemma
  SOL.3's 18.9M-box computation; SOL.5's derivative-bound certification;
  SOL.16/SOL.17) were never run; their results are asserted as facts. §1.
  Repair: implement, run, archive the exact checker + output (the draft's own
  "WHAT REMAINS" §1–2 concedes this, yet its lemma statements do not carry the
  conditionality — Lemma SOL.3's proof block says "the six resulting exact
  checks are True", which is, today, false as a statement about the world).
- **F2 (MINOR / must fix in text, numerically absorbed).** SOL.4 + SOL.13
  remainder constant understated by factor `(2 - 2^{-7}) = 1.992` (missing B_8
  boundary term in the stated kernel form). §2 [A4]/[A10]. No counterexample
  at 12/12 audit points; 2x absorbed everywhere by measured slack.
- **F3 (MINOR / one-paragraph fix).** Threshold-generation ambiguity: proof
  certifies the wave-5 J0 row; scout's grown row supersedes it if adopted.
  Exactly verified safe direction (old < new, all bands) — state it. §5 [C4].
- **F4 (record).** W7's certificate legs are thin where the draft never says
  so: floor 9/10 margin 1.934% and sup U7 margin 6.56%, both attained in the
  lam -> 0+ limit (exact closed forms: `1 - zeta2/20 = 0.9177533`,
  `U7(0+) = 2.2425449`); the (0, L] leg leans on SOL.13, so F2's corrected
  constant must be carried there (it absorbs: ~3e-14 vs 0.0177). §4.
- **F5 (record, in the draft's favor).** Every testable "expected value" in
  the recipe reproduces exactly: binding point (4 values), J0 decimals, G_4(4),
  h_n(0), zeta(2) enclosure, the seven comparisons, the box count. §§2–5.
- **F6 (record).** The recipe's own check set contains no adversarial points
  (single friendly truth-point w = 5; no off-grid edges, no m-scans, no
  lam -> 0 endpoint analysis for W7 where its own margins are thinnest). This
  referee added them (ref2/ref3/ref5); all pass. A recipe that only samples
  friendly points is itself a finding under this campaign's rules.
- **F7 (trivial).** "F_2 > 1/10 throughout" is true but loose (true min
  1.19878 on W1, growing per band); harmless.

## 9. What must happen for (S3) to close via this draft

1. Build and RUN the exact-rational interval checker of the recipe (or an
   equivalent coarser certified computation — §6 suggests the resolution
   budget is generous), with F2's corrected remainder constant, and archive
   script + output (two files). This is a prover deliverable, not a referee
   patch.
2. Apply F2 (constant 2x in SOL.4/SOL.13 + re-quoted SOL.6) and F3 (threshold
   generation paragraph) in the draft text.
3. Then re-referee: numerics can go to MINOR_REPAIRS/SURVIVES quickly on the
   strength of §§2–6 here; the maths referee still owes the lemma-level pass
   (SOL.1 algebra, the SOL.12 inequality chain, the reflection argument —
   all of which this referee's numeric evidence supports).

*Verdict: MAJOR_ISSUES — architecture verified true at every testable point;
central certificate unexecuted; two text-level flaws (F2, F3) found and
characterized exactly.*

*End of referee_numerics_sol_s3.md.*
