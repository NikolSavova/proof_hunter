# referee_maths_sl4p_repaired — adversarial MATHS referee report on `wave4_sl4p_repaired_20260812.md`

*Wave-5 referee pass, F2 campaign, 2026-08-12. Target:
`wave4_sl4p_repaired_20260812.md` (the repaired SL4' kernel-weighted honest
ledger) together with everything it consumes or cites: the original
`wave4_sl4p_20260812.md` (Lemmas SL4'.1–.8, unchanged by reference — this is
the FIRST maths referee pass SL4' has ever had, so the whole document was
attacked, not just the wave-5 repairs), `referee_numerics_wave4_sl4p.md`
(F1–F8 and their §4 repair list), the §0 inputs ([A2]/[A3]/[C.1]/[W.6] via
`wp4_draft_composite.md`; Theorem SL3' via `wave4_sl3p_20260812.md`;
Fact SLV.2/Cor SLV.3 via `wave4_sliver_20260812.md`), the five wave-5 repair
scripts + outputs under `g2_scripts/campaign_20260811/wave5_sl4prepair/`,
and the harness results files. Protocol: maximal bar, DEFAULT TO REFUTATION;
every repair-map row checked one-to-one against the numerics referee's §4;
every new lemma (R.1, R.2, Fact R.G, Cor R.3, Lemma SL4'.8') re-derived by
hand; the original's slot pricings (Lemmas SL4'.1–.5, .8) re-derived by hand
from the inversion-integral algebra; the W1 row re-implemented from the
draft texts' closed forms (own code, no import of the prover's machinery)
and every theorem-statement constant re-bracketed. `g2_draft_t1_20260803.md`
not read; `gamma = 1/8` not re-litigated. New referee scripts (SAVED and
RUN 2026-08-12, outputs archived beside them) in
`g2_scripts/campaign_20260811/referee_maths_sl4p_repaired/`:
`ref_msr_a_row_indep.py`, `ref_msr_b_r1r2.py`, `ref_msr_c_bootstrap.py`
(outputs `out_ref_msr_{a,b,c}.txt`). No existing file modified.*

## VERDICT: **MINOR_REPAIRS**

The repair mandate is FULLY DISCHARGED: every finding F1–F7 of
`referee_numerics_wave4_sl4p.md` is resolved exactly as its §4 required
(F1 by route (a) with the hypothesis genuinely DISCHARGED by Theorem SL3',
not merely restated), every corrected constant re-verified independently
here, and no theorem-statement constant moves under this pass. The three
new closing pieces are sound: **Lemma R.1 is correct as proved** (epsilon
chain re-derived by hand; independently re-certified at 2x finer cells;
truth-side sweep consistent), **Lemma R.2's algebra is exact** (the
`w`-cancellation is checked by hand; the `m = 700` bound reproduces to all
printed digits), and **Corollary R.3's mootness and threshold logic are
valid as scoped**. Two substantive defects survive, both text-level (no
number moves): **M1** — Lemma R.2's stated hypothesis list omits Theorem
SL3', which my script shows is LOAD-BEARING there (with only PROVED tier-1
in the mid slot the m = 700 bound is 2.45, first closure m = 819); **M2** —
the inherited INFL/QUADF self-consistency bootstrap (Lemmas SL4'.6/.7,
consumed unchanged) is a fixed-point ansatz with NO closure argument, and
the repaired file's "CONJECTURED items consumed: none silently — exactly
the three named hypotheses" undercounts it; I quantify the missing piece
exactly (a crude a-priori seed bound `|s2(r-1)-1| <= 0.89`; given ANY such
seed the closure is a two-line monotone-iteration argument, computed in
§2.M2). Plus one constructive finding in the closing direction: **M3** —
Lemma R.1's own cell floors, used as pointwise per-cell upper sums, close
the ENTIRE grid rung `[561, 699]` analytically with NO SL4'-X and NO
`w`-grid (worst bound `0.4165` at `m = 561`, verified for every integer in
the range) — the CL assembly's conditional surface can drop SL4'-X
entirely.

## 1. Independent verification (what I rebuilt, re-derived, or re-ran)

- **Hand re-derivation of the original's entire slot algebra** (owed since
  the original never had a maths referee): Lemma SL4'.1's kernel identity
  (regrouping checked by expansion); Lemma SL4'.2's weight
  (`2 - 2cos t <= t^2`, two-sidedness via `|phi(-t)| = |phi(t)|`); Lemma
  SL4'.3's R5 chain — the exponent absorption `-(1/2 - C5*/8)`, the moment
  `int_0^inf t^7 e^{-ct^2} = 3/c^4`, and the exact emergence of
  `48 sqrt(2pi)/pi * C5* efac / sqrt(A)` from the §1 normalization (my
  algebra note: the DENOMINATOR entry actually comes out
  `8 sqrt(2pi)/pi * C5* efac^{3/4} / sqrt(A)`, so the printed `efac` power
  is an over-count in the SAFE direction, `efac >= 1`); Lemma SL4'.4's two
  Mills forms (constants `a/(2c)`, `1 + 1/(2ca^2)` with `ca^2 = gA/4` resp.
  `0.64 c2 A` — exact) and the far pricing (`int_0^pi 2(1-cos t) dt = 2pi`
  exactly, hence `K_far = 2 sqrt(2pi)`; the single-`rho` far denominator
  `(1/pi)(pi - t_0) <= 1`); Lemma SL4'.5's cube/cross moments
  (`3840/s2^6`, `384/s2^5` — exact; constants `3840/1296 * sqrt(2pi)/pi =
  2.36410 <= 2.37`, `384/144 * sqrt(2pi)/pi = 2.12769 <= 2.13`); Lemma
  SL4'.8'/R-restated share criterion (`e(A) u m/20 = [e(A)/A](m/20)`; the
  dec/inc endpoint logic is correct AS RESTATED — the F6 repair's
  `e_j(A)/A` nondecreasing condition is exactly what the proof needs, and
  far is exactly linear in `A` while W1's X is `~ A^{5/2}`). ALL CORRECT.
- **Independent W1-row rebuild** (script [MA], dps 50, written from the
  draft texts' displayed closed forms, no prover code): every
  theorem-statement constant re-bracketed — `row(401, 4.095) = 0.9991824`
  PASS vs `row(401, 4.094) = 1.005931` FAIL (so `w†(401) = 4.095` on the
  1e-3 grid); `row(462, 4.00021) = 0.9999377` PASS vs `row(462, 4.00020) =
  1.000031` FAIL (so `w†(462) = 4.00021` at 1e-5); `row(461/462/463/464,
  4+1e-9) = 1.01282 F / 1.001895 F / 0.991128 P / 0.9805154 P` (first
  sliver-free `m = 463`; trapezoid `m`-range `[401, 462]` CONFIRMED);
  Fact R.G sentinels `row(561, 4+1e-9) = 0.4249387`, `row(699, 4+1e-9) =
  0.2613447` — all to the prover's printed digits.
- **Lemma R.1 re-proved independently** (script [MB1]): the epsilon chain
  re-derived by hand — `sin(theta) >= theta(1 - theta^2/6)` (alternating
  series), the `sinh(x) <= x(1 + x^2/5)` chain (term-ratio geometric
  domination by `x^2/20`, then `(x^2/6)/(1 - x^2/20) <= x^2/5` iff
  `x^2 <= 10/3`, spot `sinh(1) = 1.1752 <= 1.2`), `(1-epsM)^2/(1+epsS)^2 =
  0.99998400013 >= 1 - 1.7e-5`, the `M >= 2 tau1 (1-epsM) > 1` guard
  (1.59996 — so wp1-c Clause W.6's `M > 1` hypothesis holds on the whole
  used region, which I checked against wp1-c's verbatim statement), the
  two-factor minimization logic (both factors positive, `r`-interval
  tau-only, `-r_hi/M >= -r_hi/M1`). My OWN cell code: 548 cells min
  `0.0176601` (matches); 1096 cells min `0.017707` (finer only improves —
  the certificate is safe-direction); truth sweep over 120 corners min
  `x = 0.0177554` at `(561, 4+, 0.8)` (floor sits below truth everywhere
  sampled, as it must).
- **Lemma R.2 re-derived** (script [MB2]): the `w`-cancellation
  `(m^3/w^2)^{3/2} lam^3 = m^{3/2}` checked symbolically by hand; `K_Xn =
  0.19330967 <= 0.19332`, `K_Xd = 0.21862037 <= 0.21863` (exact); `B`
  nonincreasing from `2.5/0.0176 = 142.05`; independent row bound at
  `m = 700` = `0.911407` — identical to all printed digits; dec-part
  monotonicity thresholds (`6/g`, `2/g`, far `~74.28` including the
  `coth`-correction I computed — the draft's "m >= 75 safe" holds for the
  TRUE entry, not just the `m^{5.5}` proxy).
- **Repair-map audit**: §1's seven rows checked one-to-one against
  `referee_numerics_wave4_sl4p.md` §2/§4 — F1 route (a) as STATUS §2c.1
  directs, with the upgrade (hypothesis discharged); F2's `[401, 462]` and
  the `m = 462` micro-window `(4, 4.00021]` handoff sentence present; F3's
  `0.66/0.6579@w=5.0` with the `m = 402/1000` values; F4's `1.6x–8x` and
  the `w = 4.30`-class scoping with the `1.4695` FAIL witness; F5 keeping
  `0.8464` as safe-sufficient with the true boundary `0.88480` (I verify
  `4(1 - e^{-1/4}) = 0.884796868`); F6's Lemma SL4'.8' (the restatement is
  now a correct lemma; used-range scan honest); F7's explicit-convention
  decomposition (shares sum: `0.99538 + 0.12144 + 0.27429 = 1.39111` vs
  total `1.3911` — consistent; referee D1 matched). NOTHING in the
  numerics referee's §4 list is unaddressed.
- **Citations verified at source**: Theorem SL3''s statement quoted
  verbatim-consistent with `wave4_sl3p_20260812.md` (bands, `m >= 401`,
  `(4/m, 0.89]`, `(0, 0.8|lam|]` — a SUPERSET of the mid slot
  `[lam/2, 0.8 lam]`; the sl3p referee's `tau = 0.8` fp-endpoint sliver is
  measure-zero, hence harmless under the integral); the composite's
  `c1 = 0.1317` (to `0.8|lam|`), `c2 = 0.0871` (to `1.074|lam|`, covering
  `t_0` by SL3.C), far floor `0.0741`, W7 certified floor `0.852716 >=
  0.85`, `s2 >= 141.7497`; wp1-c Clause W.6 as displayed (with its `M > 1`
  guard). Consumption honesty: W5–W7 genuinely never touch SL3' (their
  `gam` field is `'PROVED'` = tier-1 in the machinery — code inspected).
- **Script/output integrity**: all four wave-5 outputs re-run-consistent
  with the quoted verbatim blocks (every §5/§6/§7 quote traced); the
  claimed "byte-faithful" provenance of `sl4pr_common.py` diffed against
  `sl4p_nc1_ledger.py` lines 12–103 (ONE comment-line difference — finding
  m4); the [D6] harness-parse regex validated against the REAL row format
  of both results files (8-field data rows; header/comment lines cannot
  match; a FAIL row either matches and lands in `bad` or is caught by the
  gap check — the sliver-referee's FAIL-token-detector defect class does
  NOT recur here); counts `557 = |[4, 560]|`, `25122 = 237 x 106`,
  `139 = |[561, 699]|` all checked.

## 2. Findings (ranked; M = substantive, m = minor)

### M1 (substantive, statement-level): Lemma R.2's hypothesis list omits Theorem SL3' — and SL3' is LOAD-BEARING there

§5.4 states "**Lemma R.2.** Assume SL1'-w and SL4'-E. For every `m >= 700`
... the W1 row value is `<= 0.9115`", and script [C2]'s CERTIFIED line
lists inputs "W.6 pointwise + Lemma R.1 + C.1 + A2 + SL1'-w + SL4'-E; NO
SL4'-X". Both lists omit **Theorem SL3'**: the bound's dec-part prices the
W1 mid slot at `gamma* = 0.42` (`e_midn(0.42, 0.28m)` — code and closed
form), which is the [SL3'] input. It is not decorative. Script [MB2]:

```
  row bound(700, g=0.42 [SL3']) = 0.911407  [prover: 0.911407]
  row bound(700, g=0.1317 [PROVED tier-1 only]) = 2.45039  -> SL3' load-bearing in Lemma R.2: True
  first m with tier-1-only R.2 bound <= 1: 819
```

So Lemma R.2 AS DISPLAYED (with only its two stated hypotheses plus the
proved [A2]/[C.1]/[W.6] substrate) has NO certified support at
`m in [700, 818]` — the displayed proof chain does not go through there
without the [SL3'] input (the conclusion happens to be rescuable only
BECAUSE Theorem SL3' is in fact proved, which is precisely why it must be
named). This is the same defect CLASS as the
original's F1 (a certified computation consuming an input the statement
does not name) — but the omitted input is PROVED and is §0-consumed by
this very file, Theorem SL4'-R and Corollary R.3 both DO name it, and no
constant moves; so the repair is one line in two places (the Lemma R.2
statement and the [C2] inputs bracket), not a re-certification.
**Required repair R1.**

### M2 (substantive, inherited — first-maths-pass duty): the INFL/QUADF self-consistency bootstrap has no closure argument; the "exactly three named hypotheses" honesty line undercounts it

Lemmas SL4'.6/.7 (consumed unchanged from the original, which this pass
referees for the first time) price every ledger entry with
`INFL = 1/(1 - Theta - d_He - d_q)` and `QUADF = Theta + d_He + d_q`
evaluated AT the conclusion `Theta = 20/m` ("self-consistently on the
ledger's own conclusion, bootstrap"). As it stands this is a fixed-point
ANSATZ: from `Theta <= G(Theta)` (the honest ledger bound when the true
perturbation is `Theta`) one may NOT conclude `Theta <= 20/m` without
(i) monotonicity of `G` and (ii) an a-priori seed bound placing `Theta`
inside the contraction basin. Neither step is written anywhere in the
original or the repaired file, and no §0 input supplies (ii). I quantify
the gap exactly (script [MC], both thinnest rows — W5 at `m = 401` and W1
at `(463, 4+)`):

```
  G(20/m) = 0.0491712 < 20/m = 0.0498753   (W5; strict contraction at the target)
  G(20/m) = 0.0421217 < 20/m = 0.0431965   (W1 @ 463)
  x_seed = sup{x : G(x) <= x} = 0.90182 (W5) / 0.89412 (W1 @ 463)
```

`G` is convex increasing (`a(1+u) + b(1+u)/(1-u)`, `u = Theta + d`), so
`G < id` on the whole interval `[20/m, 0.89]` follows from the two
endpoint evaluations (chord argument), and the monotone iteration
`x_{n+1} = G(x_n)` descends from any seed to a fixed point `< 20/m`.
**The bootstrap therefore closes GIVEN any a-priori bound
`|s2(r(k)-1) - 1| <= 0.89` on the deep-tilt band — and that seed lemma is
genuinely open** (it is a weak-CL-shaped statement; log-concavity of the
tilted Mahonian law would give the lower side `r >= 1` but not the upper).
Consequences for the file's honesty accounting: §8's "CONJECTURED items
consumed: none silently — exactly the three named hypotheses" and the
bottom-line "conditional surface ... is now exactly: SL1'-w + SL4'-E +
SL4'-X(m <= 699)" UNDERCOUNT — the seed (or any other closure of
SL4'.6/.7) is a fourth unproved ingredient, currently visible only as the
original's "certificate-grade ... flagged" parenthetical and STATUS's
standing caveat. No number moves and the mechanism is fine (the
contraction at the target is strict, margins 1.4%/2.5% in `G`-units), but
the repaired file — which will be the citable SL4' — must carry the flag
in its own status lines, and the composition note must list the seed
lemma in the conditional surface (natural home: the SL1' deliverable,
which already owns the eta algebra). **Required repair R2 (text +
one-item addition to the named conditional surface); the iteration
argument above is offered for adoption verbatim.**

### M3 (constructive, closing direction): Lemma R.1's cell floors already kill SL4'-X on `[561, 699]` — the conditional surface can drop item (c) entirely

The draft consumes SL4'-X only through Fact R.G's left-endpoint sums on
`[561, 699]`. But the X slot can instead be bounded by PER-CELL upper
sums using Lemma R.1's own 548 cell floors POINTWISE — no tau-monotonicity
(no SL4'-X), and after the exact `w`-cancellation (same algebra as R.2)
the bound is `w`-UNIFORM on `(4, 5]`:
`Xn <= (sqrt(2pi)/pi) m^{5/2} sum_i h tau_{2,i}^2 e^{-m fl_i}`,
`Xd <= (sqrt(2pi)/pi) m^{3/2} sum_i h e^{-m fl_i}`. Script [MB3], every
integer `m in [561, 699]`:

```
  m=561: per-cell-floor W1 row bound = 0.416537
  m=699: per-cell-floor W1 row bound = 0.260103
  ALL m in [561, 699]: per-cell-floor row bound <= 1: True  (worst 0.416537 at m = 561)
```

This closes the whole rung analytically in Lemma R.1's own class (cell
floors with rigorous directions) — no `w`-grid, no monotonicity flag, no
SL4'-X. Adopted into Corollary R.3, the CL(`m >= 561`) conditional
surface becomes **SL1'-w + SL4'-E only** (plus M2's bootstrap seed), and
finding m7 below evaporates; SL4'-X remains consumed only on
consumer-moot segments (`m <= 560`). Recommendation, not defect — but it
is a half-page upgrade the composition note should take (record: the same
construction also passes on `[463, 560]`, worst `0.961058` at 463, though
the R.1 epsilon audit would need its `m >= 463` variant `epsM = 6e-6`
there; moot under the harness).

### m4 (minor): `sl4pr_common.py`'s provenance claim is false in one comment line

The module header claims "byte-faithful copy of the prover's ...
lines 12-103 ... the ONLY changes are (a) removal of the prover's print
blocks [0]-[5], (b) nothing else." Diff shows ONE further change: the
`efac` comment `<= e iff C5 <= 0.8464` was rewritten to
`<= e iff C5 <= 4(1-e^{-1/4})` (the F5-corrected boundary). Comment-only,
zero functional effect (all executable lines byte-identical — I diffed),
but under house exactness the provenance note must say so. Repair: one
sentence in §7's [common] row (or the module header).

### m5 (minor): §4 misdescribes referee B4's coverage

"referee B4's full integer grid to 2000: 0 violations" — the numerics
referee's own §3.1 says `m = 401..600` step 1 PLUS `650..2000` step 50.
Integer-complete only to 600. Harmless (the §3 analytic thresholds carry
all `m` anyway), but the description of another referee's audit must be
exact. Repair: half a sentence.

### m6 (minor): §6's "referee-audited at 25k+ grid points" is a mis-attribution

The 25,122-evaluation SL4'-X flag audit is THIS file's script [B]; the
referee's SL4'-X audits were 6000-point fine grids at 8 adversarial
points. §6's consequence line "(c) ... elementary calculus,
referee-audited at 25k+ grid points with 0 violations" conflates the two.
Repair: "prover-audited at 25k+ evaluations (script [B]); referee-audited
at 6000-pt fine grids (8 points)".

### m7 (minor; mooted if M3 is adopted): Corollary R.3 item 2's statement should carry Fact R.G's class flag inline

The corollary is the object the composition note will cite, and its W1
leg on `[561, 699]` rests on the 106-probe `w`-grid + shape evidence
(honestly flagged in §5.2 and §8, but not in the corollary's own display,
which says "holds with NO exception set" without the class marker). Note
the flag's substance: the point-grid-with-interpolation-evidence class is
WEAKER than the monotone-cell corner class of E.5.3/E.6 (where directions
are rigorous per cell); §5.2's "the campaign's accepted class"
parenthetical should not equate them. Repair: one clause in the corollary
statement — or simply adopt M3, which replaces the grid rung by a
cell-floor bound in the STRONGER class and settles both halves of this
finding.

### Record-only (no text forced)

- §0's "1e2x–1e6x slack" for the mid entries: my estimates give
  `~5.6e2x` (W1) to `~2.6e6x` (W4) — order-class accurate, safe
  direction.
- §5.1's "from m = 470 it exceeds 8%": `1 - 0.919951 = 0.080049` — true
  by 5e-5. Fine but brittle phrasing.
- The far entry's TRUE `m`-decrease threshold is `~74.28` (the
  `m^{5.5}` proxy's `74.224` plus the `+4/m^3` coth-correction, my
  derivation); "m >= 75 safe" remains true. The §3 display binds the
  proxy, correctly labeled.
- F5's `= 0.88480` display: computed `0.884796868`; rounds as printed.

## 3. What survived adversarial attack (for balance — all clean)

1. Every theorem-statement constant of SL4'-R independently re-bracketed
   (both sides of `w†(401)`, `w†(462)`, first sliver-free `m = 463`,
   route-(b) record `4.135/470`): the trapezoid display is now RIGHT, and
   `T` is a certified superset of the true exception set (safe
   direction — the §5.1 argument for this is correct).
2. Lemma R.1 in full: hand-re-derived, re-certified with independent code
   at 548 AND 1096 cells, truth-side sanity confirmed. Every inequality
   direction rigorous as claimed; the class label (dps-40 point
   evaluations of elementary closed forms, margin 6e-5 vs rounding
   ~1e-39) is honest.
3. Lemma R.2 in full: exact `w`-cancellation, exact K-constants,
   reproduced bound, correct monotone-tail logic, and the [C3] honesty
   note (why the flat bound cannot reach below 700 — `B(561) = 74.389` vs
   slot `12.475`, which my [MB3] construction confirms from the other
   side).
4. The mootness logic (§6): trapezoid max-`m = 462 <= 560` under route
   (a), `469 <= 560` under route (b); the consumer-level vs lemma-level
   distinction is drawn exactly as the twice-refereed sliver note draws
   it; the [D6] independent harness parse is sound against the real file
   format and the `# OVERALL: PASS` line is quoted verbatim-correct
   (checked against the file on disk).
5. The F1 discharge is real: Theorem SL3' (citable, two-referee) delivers
   `0.42/0.42/0.40/0.40` on W1–W4 for `m >= 401`, `(4/m, 0.89]`, on
   `(0, 0.8|lam|]` — statement checked at source; the ledger's mid slot
   sits strictly inside; the flagged-class inheritance sentence is
   accurate and the "spends none of that margin" claim is fair (mid-entry
   headroom 1e2x-class at worst).
6. The seven-row ledger, INFL/QUADF ARITHMETIC (as arithmetic — see M2
   for the structural gap), tier-routing (W5–W7 SL3'-free — verified in
   code), and the per-row dependency brackets are consistent throughout
   §2/§4/§8; the updated conditional surface is stated identically in
   the bottom line, §4, §6 and §8 (modulo M2's undercount).
7. All four wave-5 scripts: quoted-output integrity verified line by
   line; the [B] grid's bookkeeping (`25122`, argmax rendering `4.0` for
   the `4+1e-9` probe, column monotonicity tolerance) is honest and the
   draft's parenthetical about the argmax print is exactly right.

## 4. Required repairs (to citability; none moves a number)

1. **(R1 = M1)** Add `[SL3']` to Lemma R.2's hypothesis list and to the
   [C2] CERTIFIED inputs bracket (one line, two places). Optionally quote
   [MB2]'s tier-1-only numbers as the reason it is named.
2. **(R2 = M2)** State the INFL/QUADF bootstrap flag in THIS file's §8
   status lines and add the seed lemma (a-priori
   `|s2(r-1)-1| <= 0.89`-class on the deep-tilt band, or any equivalent
   closure of SL4'.6/.7) as a NAMED item of the conditional surface; the
   monotone-iteration closure argument in §2.M2 may be adopted verbatim.
3. **(R3 = m4–m6)** Provenance sentence for the `sl4pr_common.py` comment
   edit; fix the B4-coverage description; fix the 25k attribution.
4. **(R4 = m7, or adopt M3)** Either add the grid-class clause to
   Corollary R.3's statement, or (better) replace Fact R.G's role on
   `[561, 699]` by the per-cell-floor bound of §2.M3 and restate the
   conditional surface as SL1'-w + SL4'-E (+ the R2 seed).

None of these threaten the mechanism, the ledger rows, the corrected
trapezoid, Lemma R.1, Lemma R.2's inequality chain, or the `m >= 561`
assembly; R1/R2 are hypothesis-ACCOUNTING repairs (the underlying inputs
are proved resp. flagged elsewhere), which is what keeps this
MINOR_REPAIRS rather than MAJOR_ISSUES under the house rule (no
theorem-statement constant moves; contrast the original's F1/F2).

## 5. Referee script table (all SAVED and RUN 2026-08-12; outputs archived)

| # | script (`g2_scripts/campaign_20260811/referee_maths_sl4p_repaired/`) | what it does | key output |
|---|---|---|---|
| [MA] | `ref_msr_a_row_indep.py` (`out_ref_msr_a.txt`) | independent dps-50 W1-row rebuild from the draft texts' closed forms (no prover code); brackets every trapezoid constant; R.G sentinels; exact constant roundings | `row(401,4.095)=0.9991824 P / (401,4.094)=1.005931 F`; `row(462,4.00021)=0.9999377 P / 4.00020 F`; `461:1.01282F 462:1.001895F 463:0.991128P`; `row(561,4+)=0.4249387`, `row(699,4+)=0.2613447` |
| [MB] | `ref_msr_b_r1r2.py` (`out_ref_msr_b.txt`) | [B1] R.1 re-certified (own code; 548 + 1096 cells; eps chain; truth sweep); [B2] R.2 constants + bound + SL3'-load-bearing test; [B3] the per-cell-floor SL4'-X-free closure of `[561, 699]` | `ncell=1096: min = 0.017707`; truth min `0.0177554`; `row bound(700, 0.42) = 0.911407`; `row bound(700, 0.1317) = 2.45039`, first tier-1-only closure `m = 819`; `ALL m in [561,699] per-cell-floor <= 1: True (worst 0.416537 at 561)` |
| [MC] | `ref_msr_c_bootstrap.py` (`out_ref_msr_c.txt`) | quantifies the SL4'.6/.7 bootstrap closure: `G(x)` for the two thinnest rows, contraction at the target, seed threshold by bisection | `G(20/m) = 0.0491712 < 0.0498753` (W5) and `0.0421217 < 0.0431965` (W1@463); `x_seed = 0.90182 / 0.89412` |

*End of referee_maths_sl4p_repaired.md.*
