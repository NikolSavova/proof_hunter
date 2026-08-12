# referee_maths_wave5_sl4pe — adversarial MATHS referee report on `wave5_sl4pe_20260812.md`

*Wave-5 closing-wave referee pass, F2 campaign, 2026-08-12. Target:
`wave5_sl4pe_20260812.md` (hypothesis SL4'-E — the computed-eta pricing
machinery at the shifted CL threshold `m >= 561`). Mandate: maximal bar,
DEFAULT TO REFUTATION — this chain flips the main conjecture of a paper to a
theorem. Protocol executed: (1) key algebra recomputed BY HAND (Lemma E.1
(i)–(iii) re-derived line by line; the W1 and W7 certificate constants of
Lemma E.2 recomputed by hand to 5–6 significant figures; the J*/J0 table for
all seven bands; the Prop E.3 eta value; the W7 geometric limit); (2) the
E.1 identities proven SYMBOLICALLY (sympy — strictly stronger than the
draft's 6-random-tuple check); (3) the ENTIRE Lemma E.2 exact-rational
certificate re-derived independently from the lemma text (formulas re-typed,
not copied) and compared to the archived exact fractions — equality on all
7 bands; (4) every truth-side number re-attacked at dps 50 via a DIFFERENT
route (direct series summation of `phi_n`, not the closed forms); (5)
interface fidelity checked against STATUS_wave4 §2 item 2, the original
consumer `wave4_sl4p_20260812.md` §3/§4, the composite §5.3 display, AND —
beyond the prover's blind horizon — the live repaired consumer
`wave4_sl4p_repaired_20260812.md`; (6) circularity audit; (7) every band
edge, constant, and the `m >= 561` threshold arithmetic checked. Read:
`STATUS_wave4.md`, the target + its three scripts and archived outputs,
`wave4_sl4p_20260812.md`, `referee_numerics_wave4_sl4p.md`,
`wave4_sl4p_repaired_20260812.md` (interface check only),
`wp4_draft_composite.md` (§5.3, Theorem A2), the archived
`out_sl4p_nc2.txt`, `sl4p_nc2_eta.py`. NOT read: `g2_draft_t1_20260803.md`.
No existing file modified. New referee scripts (SAVED and RUN 2026-08-12,
outputs archived beside them) in `referee_maths_wave5_sl4pe_scripts/`:
`ref_mw5e_a_symbolic_exact.py` (`out_ref_mw5e_a.txt`),
`ref_mw5e_b_numeric_attack.py` (`out_ref_mw5e_b.txt`).*

## VERDICT: MINOR_REPAIRS

**Every load-bearing claim verified; refutation attempts failed on all
fronts.** Theorem E (the pricing machinery, conditional on
(E-A2)+(E1)+(E2)+(E3)) is CORRECT as stated at `m >= 561`; the DELTA
(Proposition E.3: the STATUS_wave4-recorded proof plan "exact `qhat` algebra
+ `kappa_4 >= 0` sign lemma + SL1'-w(i)" CANNOT prove the pricing) is
GENUINE — I verified the counterexample independently at dps 50 and by hand
(`eta/u = -1.000964`, ratio `1.4299`), and the truth-side W1/W2 forcing
argument is sound. Lemma E.4 is correct (its two flagged dps-30 point
evaluations reconfirmed at dps 50, K = 800). The statement delivered is
byte-level IDENTICAL to what STATUS_wave4 §2 item 2, the wave-4 SL4'
assembly (original AND repaired — the repair cycle left the SL4'-E display
unchanged), and the composite §5.3 (`1/(2 s2) = (lam^2/2) u` exactly)
consume; the certified constants are exactly the assembly's `main`-row
entries (`J*(W) + lam^2/2`; W7: `4.752 + 0.396 = 5.148` ✓). No circularity.
The repairs below are text/comment-level: none moves a constant, a
hypothesis, a threshold, or a verdict.

## 1. What I verified and how (by claim)

### 1.1 Lemma E.1 (exact algebra) — CONFIRMED, three ways

- **By hand, in full.** (i): `He3(0) = 0`, `He4(0) = 3`, `He6(0) = -15`
  give `qhat_0 = N/sqrt(2 pi s2)`; parity of `He3/He4/He6` at `z = ±eps`
  gives `qhat_± = e^{-eps2/2}(1 ± a h3 + b4 h4 + c6 h6)/sqrt(2 pi s2)`;
  the quotient assembles to `eta = s2(e^{eps2} N^2/D - 1) - 1`. (ii): I
  re-derived the factorization `N^2 - D = (N-1-x)Sig + a^2 h3^2` with
  `x = b4 h4 + c6 h6`, and checked the three key reductions
  `3 - h4 = eps2(6 - eps2)`, `15 + h6 = eps2(45 - 15 eps2 + eps2^2)`,
  `h3^2 = eps2(3 - eps2)^2`; substituting `c6 = a^2/2` collects exactly to
  `eps2[C_b b4 + C_a a^2]` with the displayed `C_b`, `C_a`. (iii): the
  split, the substitutions `s2 eps2 = 1`, `A eps2/2 = lam^2/2`,
  `A b4 = r42/24`, `A a^2 = r31^2/36`, and the termwise series for `rho1`
  all check.
- **Symbolically (my script [A]).** Both (ii) and the FULL (iii) display
  (with `e^{eps2}` as a free symbol `E` and `rho1 := s2(E-1) - 1 - eps2/2`)
  simplify to zero in sympy: `(ii) ... == 0 symbolically: True`,
  `(iii) ... == 0: True`. This upgrades the draft's 6-random-rational-tuple
  guard to a proof-grade identity check.
- The draft's proof text contains no gap I could find.

### 1.2 Lemma E.2 (certified envelope) — CONFIRMED; constants reproduced exactly

- **Hand recomputation.** W1: my by-hand chain (`bb = 3.7136e-4`,
  `aa = 1.7684e-4`, `xb = 2.4404e-3`, `db = 4.8979e-3`, `ph = 0.012062`,
  `e_b = 0.0018066`, `e_a = 0.0059828`, `M0cap = 0.7`) gives
  `REM2 = 0.0170580`, `d1 = 9.36e-8`, `REM*(W1) = 0.0170581` — the archived
  value to all printed digits. W7 likewise: my hand values
  (`ph = 0.017104`, `e_b = 0.0030319`, `e_a = 0.0090421`,
  `d1 = 9.33e-4`) give `REM*(W7) = 0.1560293` vs archived `0.15603`.
- **Independent exact re-derivation (my script [B]).** I re-typed every
  Step 0–5 formula from the LEMMA TEXT into `Fraction` arithmetic and
  compared the resulting EXACT `J0(W)` fractions against the seven archived
  fractions in `out_e1_pricing_certificate.txt` line "exact J0": **equal on
  all 7 bands** (`True`), and the two side conditions
  (`REM* <= 0.3 R31*^2`, positivity of `D`, `qhat_0`, `qhat_±`) hold
  exactly on every band.
- **Step-level soundness.** Each interval bound re-checked: Step 0's
  manufactured two-sided `r42` cap (`|r42| <= max(R42*, 2J*)` — correctly
  uses `2J*`, NOT `2J0`, so there is NO definitional circularity between
  `REM*` and `J0`; the dependency order is `J* -> REM* -> J0`); Step 2's
  elementary caps are valid on `eps2 in (0, E0]` (`E0 = 0.0070547`); the
  `e^x <= 1/(1-x)` input is the only transcendental, as claimed; Step 3's
  four interval endpoints for `C_b`, `C_a` are the correct monotone
  extremes (I checked the sign/direction of each of the eight products);
  Step 5's triangle split `|(e^{eps2}/D)M - M0| <= ph|M0| + (1+ph)|M - M0|`
  is algebraically right; the `rho1` ratio-test bound
  `rho1 A <= eps2 lam^2/(6(1 - eps2/4))` is right (first neglected ratio
  `eps2/4` at `n = 3`), and is monotone in `(eps2, lam)` so the single
  worst-case evaluation at `(E0, Lam(W))` is legitimate. The single-shot
  `m >= 561` uniformity argument (`A0` and `Lam` are the monotone extremes
  over ALL `m >= 561`) is correct: `A >= c_A(W) m >= c_A(W)·561` and
  `lam <= wmax(W)/m <= wmax(W)/561` (W7: `lam <= 0.89` by CL scope).
- **J*/J0 table re-derived by hand** from `R31*/R42*`:
  `J* = 0.7/1.132/1.975/2.617/3.8/4.323/4.752`; subtracting the certified
  `REM*` reproduces the quoted `J0` row digit-for-digit. Derived constants
  spot-checked: `2(R31*^2 - J0(W7)) = 0.48806` ("0.488" ✓),
  `sqrt(J0(W1/W2/W7)) = 0.8264/1.0501/2.1438` ✓, `R31*^2 > J0` on every
  band ✓ (`1/1.44/2.25/2.89/4/4.41/4.84` vs the J0 row).

### 1.3 Theorem E — proof CONFIRMED

Upper side: `(E2) + r31^2 >= 0` then the certified `REM* <= 0.3 R31*^2`;
lower side: `(E3)` gives `eta/u >= lam^2/2 + d1 - J* >= -J*`; both sides
land on `|eta| <= (J* + lam^2/2) u = [R42*/2 + 0.3 R31*^2 + lam^2/2] u`.
The calibration `J0 := J* - REM*` makes (E3) EXACTLY the weakest lower-side
input this envelope supports — the hypothesis is not padded. Each of
(E1)/(E2)/(E3) is genuinely used ((E1) in `aa`/`Mdev`, (E2) upper side,
(E3) lower side + Step 0); (E-A2) feeds `A0`, `E0`. Well-definedness
(`qhat_- qhat_+ > 0`) is Step 2 positivity, checked exactly.

### 1.4 Proposition E.3 (the DELTA) — CONFIRMED; the delta is real and load-bearing

- **The counterexample point.** `(m, w) = (561, 4.5)`, `A = 157.08 =
  c_A(W1)·561` exactly, `s2 = 2.4413e6 >= S0`, `r31 = 1 = R31*(W1)`
  (E1 equality), `kappa_4 = 0` ((E2) + sign conclusion hold). My dps-50
  recomputation: `eta/u = -1.000963731`, `price = 0.7000321714`, ratio
  `1.4298825` — matches the draft's `-1.000964 / 0.700032 / 1.4299`. My
  by-hand Edgeworth estimate at the same point (`(e^{eps2}/D)(C_a/36) ~
  -1.000994` + `lam^2/2`) independently gives `-1.00096`. The point
  satisfies every listed hypothesis; the pricing fails by 43%.
- **The logic.** A proof consuming only the listed interface must hold at
  every triple satisfying it; it fails at this one; hence no such proof.
  Sound. The pricing is a function of `(s2, kappa_3, kappa_4, lam)` only,
  so SL1'-w(ii) (an `R5`/`phi` statement) cannot rescue the recorded plan —
  the draft's scoping of the axiom list is fair.
- **Truth-side forcing.** At `(561, 5.0)` the true `r31 = 0.886365`
  (my independent series route), `r31^2 = 0.78564 > 0.7 = J*(W1)`, so a
  sign-only argument dies at W1 on the TRUTH, not merely on the interface;
  `r42 = 0.650647` rescues (`J = 0.460318 <= 0.682942 = J0(W1)`).
  Confirmed. Block [F]'s dead-route table verified: W1 `0.8864 > 0.8264`
  DEAD, W2 `1.0739 > 1.0501` DEAD, W7 gap 0.9%; the W3–W6b viable margins
  are 2.6%/4.7%/5.8%/6.5% — the draft's "2.6%–6.5%" ✓.
- **Consequence check.** STATUS_wave4 §2 item 2's recorded plan is thereby
  refuted — but NOTHING previously graded PROVED is contradicted: wave-4
  recorded SL4'-E as CONJECTURED with a proof PLAN; the plan (not any
  theorem) is what dies. The ledger surgery the draft proposes (§7) is the
  correct bookkeeping, and "no ledger number moves" is verified (§1.6).

### 1.5 Lemma E.4 — CONFIRMED (flagged class, as declared)

- (i): the per-factor `k_4^{(j)} = phi_4(lam) - j^4 phi_4(j lam)` follows
  from the 4th `lam`-derivative of `log(1 - e^{-j lam}) - log(1 - e^{-lam})`
  (even derivative, sign +): re-derived by hand; the `lam^4` rescaling to
  `h_4` telescopes correctly.
- (ii): `phi_4(x) ~ 6/x^4` gives `h_4(0+) = 6`; the Riemann-sum limit and
  the closed form `G_4(w) = 6w - 4 pi^2 + sum e^{-kw} P(kw)/k^2` re-derived
  by hand — I integrated `int_0^w t^4 k^3 e^{-kt} dt` explicitly and
  recovered `P(y) = y^4 + 4y^3 + 12y^2 + 24y + 24` and the `4 pi^2 =
  24 zeta(2)` constant.
- (iii): `x phi_5 - 4 phi_4 = sum k^3 e^{-kx}(kx - 4)`, termwise `>= 0` for
  `x >= 4` ✓ (checked at the boundary: value `0.01215 > 0` at `x = 4`);
  `h_4' = x^3(4 phi_4 - x phi_5)` ✓; hence `G_4' >= 6 - h_4(4)` on ALL of
  `[4, oo)`, not just the display grid ✓.
- (iv): my dps-50, K = 800 independent evaluation:
  `G_4(4) = 0.232348298890392` (draft: `0.23234829889` ✓),
  `h_4(4) = 5.420211696382` (draft: `5.420211696` ✓), sign bracket
  `G_4(3.3) = -0.011689 < 0 < 0.0292934 = G_4(3.5)` ✓. My by-hand series
  estimate of `G_4(4)` (`~0.23235`) agrees to my hand precision. The e3
  tail bound (`P(y) <= 2y^4` for `y >= 13.3`, geometric ratio
  `e^{-w}((K+2)/(K+1))^2`) is valid — I checked the `y = 13.3` coefficient
  inequality and the ratio-domination step.
- The limit-roadmap anchors: `J_lim(5) = 0.45984382` (independent route) ✓;
  the `m`-direction data `0.4603/0.4601/0.4599 -> 0.45984` ✓ (so `m = 561`
  is the measured W1 worst case, as claimed); the W7 deep-corner geometric
  limit recomputed BY HAND from `phi_n(0.89)` closed forms:
  `r31 -> 2.13024`, `r42 -> 6.41102`, `J -> 1.33241` — confirms the
  draft's "~1.332" AND STATUS_wave4's recorded `2.1303/6.4113`.

### 1.6 Interface fidelity and threshold arithmetic — CONFIRMED (the historical failure mode does NOT recur here)

- **Inequality:** Theorem E's conclusion is character-identical to
  STATUS_wave4 §2 item 2, `wave4_sl4p_20260812.md` §3 (SL4'-E), and —
  checked beyond the prover's blind horizon — the REPAIRED consumer
  `wave4_sl4p_repaired_20260812.md` §2, which says "Statement unchanged"
  and consumes SL4'-E at exactly `m >= 561` scope in its §6/§8 (threshold
  MATCH with Theorem E's `m >= 561`). The composite §5.3's third term
  `1/(2 s2)` equals `(lam^2/2)u` identically — reconciliation correct.
- **Constants:** `R31*/R42*` rows match SL1'-w(i) verbatim (one-sided
  `kappa_4` cap, exactly as STATUS_wave4 records — the draft correctly
  consumes the WEAKER one-sided form and manufactures the lower bound from
  (E3)); `c_A = 0.28/.../0.80` and `S0 = 1122800/7921` match Theorem
  A2(ii)/(iii) in the composite; the assembly's `main` row = `J* + lam^2/2`
  in u-units on every band (W7: `4.752 + 0.89^2/2 = 5.148` = the ledger
  entry; the `0.396` attribution ✓). "No ledger number moves" is TRUE.
- **Threshold arithmetic:** `A0(W) = c_A(W)·561 = 157.08/196.35/235.62/
  291.72/336.60/392.70/448.80` ✓; `Lam(W) = 5/561, ..., 40/561 = 0.0713`,
  `Lam(W7) = 0.89` ✓; the shifted obligation `m >= 561` is exactly
  STATUS_wave4 §2's post-sliver CL target; §7 item 5's up/down-threshold
  remark is correct (only `A0`, `Lam` are `m`-dependent).
- **Model identity:** the `qhat` coefficients (`a = k3/(6 s2^{3/2})`,
  `b4 = k4/(24 s2^2)`, `c6 = k3^2/(72 s2^3)`) are code-identical to the
  wave-4 consumer's `sl4p_nc2_eta.py`; the block-[A] guard values
  (`0.4503/0.6432`, `0.9285/0.1804`) match the archived `out_sl4p_nc2.txt`
  lines verbatim (I read the archive directly), and the wave-4 numerics
  referee's independent `0.6579` (m = 401, w = 5.0) / `0.65734` (m = 1000)
  bracket the draft's `0.6576` (m = 561) monotonically — cross-model
  consistency across THREE independent implementations.
- **Circularity:** consumed-as-proved = [A2](ii)/(iii) only (two-referee
  via composite). `eta` is a model-side object; nothing from SL3', the
  sliver, SL4'-X, or Theorem A enters any proof here. The (E3)/(E1)/(E2)
  hypotheses are consumed, never silently assumed true. NO circularity.
  Internally, `J0`'s definition consumes `REM*` which consumes only `J*` —
  no cycle (checked in the script source, line by line).

### 1.7 Truth-evidence audit (script [2]) — CONFIRMED

All 27 probes re-verified in structure (band edges both sides at
5/6/8/10/20/40, near-left-edge 4.001, exact corner `w = 499.29 = 0.89·561`);
my independent series-route recomputation of the binding probes matches
every printed digit; worst `J/J0 = 0.6740` (W1, right edge), worst pricing
ratio `0.6576`, `REMact <= 9.97e-5` (W1) / `9.59e-4` (W7 corner), truth
satisfies (E1)/(E2) at all probes (`r31 <= 2.1240 <= 2.2`,
`r42 <= 6.3713 <= 6.6`), `r42 >= 5.4654` on W7 ("5.46" ✓). The
(E3)-margin headline `32.6%` is right and is correctly identified as the
number the campaign now rests on.

## 2. Repairs required (all text/comment-level; NONE moves a constant, hypothesis, threshold, or verdict)

1. **(R1, §3 last paragraph — wrong commentary magnitudes)** "still
   30x–100x smaller than the budgets it must fit under" is not right under
   either reading: `REM*` is **9.1x–17.6x** below the `0.3 R31*^2`
   headroom check and **29x–41x** below the full price. Likewise
   "100x–1000x looser than truth" is 163x–171x at the quoted edges but up
   to ~2e4x mid-band. Reword with the actual ranges (the qualitative point
   — nothing is tight — survives unchanged).
2. **(R2, DELTA flag + §5(a))** `r31^2 = 0.7857` is the square of the
   4dp-rounded `0.8864`; the true value is `0.78564` -> print `0.7856`.
   Conclusion (`> 0.7 = J*(W1)`) unaffected.
3. **(R3, §8 integrity note)** "rounded in the safe direction" for script
   [2]'s `REM*`/`J0` float copies is only half-true: the copies are safe
   (conservative) for the load-bearing `J <= J0` checks but
   ANTI-conservative for the `REMact <= REM*` sanity check (e.g.
   `0.0170581 >= exact 0.0170580...`). With 160x+ margins this changes
   nothing; scope the sentence to the `J0`-side checks.
4. **(R4, script comment, `e2_truth_margins.py` line 52)** the truncation
   comment "`j^4 e^{-jl} < 1e-48`" overstates by ~8 orders as an absolute
   bound (true ~1e-40 absolute, ~1e-49 relative to `kappa_4`); truncation
   remains harmless (my independent dps-50 run with a 1e-60 relative cut
   matches every printed digit). Fix the comment.
5. **(R5, script comment, `e1_pricing_certificate.py` line 76)** the `r42`
   lower bound is attributed to "(E1)+(E3)"; it follows from (E3) +
   `r31^2 >= 0` (the lemma text has it right). Comment-only.
6. **(R6, Lemma E.4(iv) wording)** "dps-30 evaluations with the series
   truncated at `K = 300`" describes `G_4(4)` only; `h_4(4)` is a
   closed-form (non-truncated) evaluation. Same flagged class either way;
   half-sentence fix.

Coordination note for the synthesis editor (NOT a defect of this file — the
blind protocol forbade the prover the repaired SL4'): §7 item 2's restated
hypothesis surface ("SL1'-w, SL3'-w, SL4'-X, and now (E3)") is stated
against STATUS_wave4; the repaired assembly has meanwhile dropped SL3'-w
(Theorem SL3' consumed as proved) and scoped SL4'-X to `m in [561, 699]`.
The merged wave-5 surface should read: **SL1'-w + (E3) + SL4'-X([561, 699])**.
Also flag for the (E3)/SL1' prover: (E3) is calibrated to THIS certificate's
`J0 = J* - REM*`; any re-derivation of the envelope must not weaken `REM*`
without re-checking `J0`.

## 3. Status classification audit (house rules)

- **Theorem E: PROVED** (conditional on its stated interface) — AGREED.
  The certificate is exact-rational; the single transcendental input is
  `e^x <= 1/(1-x)`; this is STRONGER than the campaign's flagged
  grid-certificate class (no float corners anywhere in the certificate).
- **Proposition E.3: PROVED** — AGREED (exhibited point + dps-30/50
  evaluation; the evaluation is point-evaluation class but the 43% failure
  dwarfs any conceivable dps concern, and I reproduced it independently).
- **Lemma E.4: PROVED modulo two flagged point evaluations** — AGREED,
  honestly flagged, and both evaluations independently reconfirmed at
  higher precision here.
- **(E3) [SL4'-E-J]: CONJECTURED** — AGREED, and correctly so labeled
  everywhere it is used; the draft consumes no conjectured item silently.
- **Overall SL4'-E: PARTIAL** — AGREED; the honest headline. `gamma = 1/8`
  untouched ✓; no existing file modified ✓; scripts SAVED+RUN with outputs
  archived ✓ (I re-ran nothing of the prover's — all three outputs were
  reproduced through independent code).

## 4. Referee script table

| # | script (`referee_maths_wave5_sl4pe_scripts/`) | what it attacks | key verbatim output |
|---|---|---|---|
| [A] | `ref_mw5e_a_symbolic_exact.py` (`out_ref_mw5e_a.txt`) | E.1(ii)/(iii) as SYMBOLIC identities; full independent exact re-derivation of the E.2 certificate from the lemma text; comparison to archived exact `J0` fractions | `(ii) ... == 0 symbolically: True`; `(iii) ... == 0: True`; per band `upper-slack True positivity True`; `independent exact J0 fractions == archived e1 fractions (all 7 bands): True` |
| [B] | `ref_mw5e_b_numeric_attack.py` (`out_ref_mw5e_b.txt`) | truth probes via SERIES route at dps 50 (not closed forms); Prop E.3 point; E.4 point values at K = 800; limit anchor | `m=561 w=5.0: r31=0.886365 r42=0.650647 J=0.460318 ... ratio=0.657645`; `m=561 w=499.29: ... J=1.32583 ... ratio=0.180795`; `eta/u = -1.000963731 ... |eta|/(price*u) = 1.4298825 (> 1: True)`; `G_4(4) = 0.232348298890392`; `h_4(4) = 5.420211696382`; `J_lim(5) = 0.45984382` |

## 5. Bottom line for the ledger

`wave5_sl4pe_20260812.md` **SURVIVES this maths-referee pass at
MINOR_REPAIRS** (R1–R6, all wording/comment-level). Its central
deliverables stand: (a) the SL4'-E pricing implication is now a THEOREM at
`m >= 561` from (E1)+(E2)+(E3), with an exact-rational certificate whose
every constant I reproduced independently; (b) the interface DELTA is
real — the previously recorded proof plan is refuted by an explicit
hypothesis-consistent counterexample, and the conjectural surface must
carry **(E3) [SL4'-E-J]** (worst measured margin 32.6% at
`(m, w) = (561, 5.0)`) in place of "pricing + sign lemma"; (c) the sign
lemma is correctly downgraded to supporting structure, with its limit-level
form (Lemma E.4) proved. Consumers may cite the pricing SLOT as discharged-
modulo-(E3) once the second (numerics) referee lands, per house two-referee
rule. The one number the campaign now rests on in this slot — `J = 0.4603`
vs `J0 = 0.682942` at the W1 right edge — is verified here by two
independent computational routes and one hand calculation.

*End of referee_maths_wave5_sl4pe.md.*
