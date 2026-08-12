# STATUS_wave5 — G2 closure campaign, wave-5 synthesis (2026-08-12)

*Synthesis editor pass, wave 5 (read-everything role; blind protocol lifted
for this file only). Sources: everything new under `g2_campaign_20260811/`
since STATUS_wave4 — the hygiene overlay `wave4_hygiene_20260812.md`, the
wave3-repairs verifier `referee_wave3_repairs.md`, the repaired SL4'
`wave4_sl4p_repaired_20260812.md` + its two referees
(`referee_maths_sl4p_repaired.md`, `referee_numerics_sl4p_repaired.md`),
the SL4'-X deliverable `wave5_sl4px_20260812.md` + its two referees, the
SL4'-E deliverable `wave5_sl4pe_20260812.md` + its two referees, and the
composition note `CL_composition_20260812.md` — plus `STATUS_wave4.md` as
the governing prior ledger. `g2_draft_t1_20260803.md` remains unread by
every wave-5 agent and by this editor. No existing file modified; this
file is new (no-erasing rule). House rules applied: an item is CLOSED only
when BOTH referees hold SURVIVES or MINOR_REPAIRS; recorded-not-applied
repairs are inventoried in §2a. Facts from this editor's own disk checks
(2026-08-12, ~13:4x): (i) NO file matching `*sl1*` or `*flip*` exists in
the campaign directory — the SL1' slot produced NO artifact for the third
wave running, and NO flip artifact exists; (ii)
`wave5_composition/out_compose_chain.txt` ends `ALL CHECKS PASS: True`
followed by the explicit note that CL at `m >= 561` "remains CONDITIONAL
on the named open hypotheses (S1)-(S4)"; (iii)
`harness_m560/results_m560.txt` carries exactly ONE `# OVERALL` line,
verbatim `# OVERALL: PASS -- all of C1..C6 hold exactly for 4 <= m <= 560
(C2/C3 with the known m=4 exception; rows split across this file and the
honored prior file(s)).`; (iv) `wave5_hygiene/out_hygiene_checks.txt` ends
`OVERALL (blocks A/C/D/E): PASS`; (v) the sliver referee's from-scratch
fresh harness re-run (`referee_fresh_results_m560.txt`) still stops at
last data row `m = 441`, zero OVERALL lines — stalled, record-only,
unchanged since wave 4. No new mathematics is asserted here; no new
scripts were needed.*

**Executive summary.** Wave 5 was the closing wave and it closed
EVERYTHING EXCEPT the SL1'-class mathematics. Delivered, all two-referee:
(a) **SL4'-X is PROVED outright** (Theorem X.1 — strict monotonicity, all
`w >= 4`, elementary calculus, no grid certificate; maths MINOR_REPAIRS,
numerics SURVIVES) — one of the four wave-4 hypotheses is simply GONE;
(b) the **repaired SL4' is now citable** (Theorem SL4'-R, two-referee
MINOR_REPAIRS; every wave-4 F1–F8 finding verified resolved; new Lemmas
R.1/R.2 + Fact R.G close the W1 ladder; its first-ever maths pass also
SURFACED a previously uncounted conditional item — the INFL/QUADF
bootstrap seed, now (S4)); (c) the **SL4'-E pricing machinery is PROVED**
(Theorem E, exact-rational certificate, two-referee MINOR_REPAIRS) — but
with a genuine and refereed interface DELTA: Prop E.3 proves the recorded
proof plan ("qhat algebra + kappa_4 sign lemma") CANNOT work, and a NEW
cumulant hypothesis **(E3) = SL4'-E-J** (worst measured margin 32.6% at
`(m, w) = (561, 5.0)`) replaces it in the conjectural surface; (d) the
**hygiene batch** executed sliver repair m1 (`M_H = 560` CERTIFIED,
threshold `m >= 561` unconditionally), filled the harness note, and
recorded the SL3' §2b errata (1.30x worst-certified-margin headline); (e)
`wave3_repairs_20260812.md` got its verifier — **SURVIVES**, now citable
single-verifier; (f) the **composition note** assembles Theorem CL-C =
CL(79, 20, 0.89) at `m >= 561` from citable inputs only, chain-verified
end-to-end (`C*(m >= 561) = 18.2281 <= 20`; `ALL CHECKS PASS`). What did
NOT happen: the **SL1' prover slot produced NO artifact for the third
wave running** — hypotheses (S1) = SL1'-w(i) and (S2) = SL1'-w(ii) still
have no proof artifact, (S3) = (E3) is new and CONJECTURED, and (S4) is
newly surfaced; and the **flip was not executed** (correctly — its
preconditions are not met). **CL itself remains OPEN; Theorem A remains
PROVED CONDITIONAL on exactly (S1)–(S4).** No grade inflation: the bottom
line is §3.

## 1. Wave-5 verdict table

| Package | Deliverable | Draft self-reported status | Maths referee | Numerics referee |
|---|---|---|---|---|
| **Hygiene batch** `wave4_hygiene_20260812.md` | STATUS_wave4 §3 item 1 executed as recorded errata/inserts: sliver m1 (Fact SLV.2 `M_H = 560` CERTIFIED, Cor SLV.3 final form `m >= 561`, interim 554/555 scaffolding RETIRED) + m2–m6; harness note §2/§3 filled from disk; SL3' §2b R1–R5 recorded (R1: worst certified margin **1.30x** at W7 `tau_start = 0.7275`, exact-rational re-derivation `1.2971x`); wave2_repairs W-F1 relabel in completed form | script `hygiene_checks.py` blocks [A]–[E] ALL PASS (exact parses; six footer varfit checkpoints recomputed exactly, 12/12 digits); editor disk-check (iv) confirms | **ZERO referees** (single-verifier class debt, same as the earlier repairs files before their passes) | — |
| **Wave3-repairs verifier** `referee_wave3_repairs.md` | (is itself the owed single-verifier pass on `wave3_repairs_20260812.md`) | **SURVIVES**: all three scripts byte-identical; 8/8 §2a + 7/7 §2b + §C items verified applied; MR-1 logic independently audited; MR-2 re-proved with strictly weaker elementary machinery; V-F1–V-F3 record-only | — (single-verifier class) |
| **Repaired SL4'** `wave4_sl4p_repaired_20260812.md` | **PARTIAL — Theorem SL4'-R PROVED MODULO three named hypotheses** (SL1'-w, SL4'-E, SL4'-X; SL3'-w DISCHARGED by consuming Theorem SL3' at `gamma*(W1–W4) = 0.42/0.42/0.40/0.40`); corrected trapezoid `(4, w†(m)] x [401, 462]`, `w†(401) = 4.095`, `w†(462) = 4.00021`; NEW: Lemma R.1 (crossover floor `0.0176`, epsilon-rigorous), Lemma R.2 (W1 analytic tail `m >= 700`, row `<= 0.9115`), Fact R.G (grid `[463, 699]`, 25,122 probes, 0 fails), Cor R.3 (F1/F2 MOOT at `m >= 561`; assembled CL statement, empty exception set) | **MINOR_REPAIRS** (first-ever SL4' maths pass; entire slot algebra re-derived by hand — ALL CORRECT; **M1**: Lemma R.2's hypothesis list must name Theorem SL3' — load-bearing (tier-1-only bound `2.45` at 700, first closure 819); **M2**: the INFL/QUADF bootstrap of SL4'.6/.7 is a fixed-point ansatz with NO closure — needs an a-priori seed `\|s2(r-1)-1\| <= 0.89`; given ANY seed, referee's chord/monotone-iteration closes it (`G(20/m) < 20/m`, margins 1.4%/2.5%, seed basins 0.902/0.894) — a FOURTH conditional item all prior statements undercounted; **M3** (constructive): R.1's cell floors close `[561, 699]` with NO SL4'-X and no `w`-grid, worst `0.416537` at 561; m4–m7 minor) | **MINOR_REPAIRS** (every wave-4 F1–F8 finding verified RESOLVED, not just re-quoted; 62 bisected true crossings all safe-direction; 2,790 + 3,594 off-grid probes, 0 failures; R.1 rebuilt at 2,740 cells (floor RISES to `0.017735`) + 11,256-point truth attack (min `0.0177554` at the predicted corner); RF-1 efac display rounding, RF-2 provenance clause — text-level) |
| **SL4'-X** `wave5_sl4px_20260812.md` | **PROVED, strengthened** (Theorem X.1: `x(w, tau)` STRICTLY increasing on `[0.8, 1.074]` for ALL `w >= 4`, `lam in (0, 0.89]`; Cor X.2 (`tau_0(lam)/lam <= 1.07372378 < 1.074`), Cor X.3 (partition-free left-endpoint certificate = the ledger's `totn`/`totd` verbatim); elementary calculus, NO grid certificate, six named constants NX-1..6) | **MINOR_REPAIRS** (every lemma re-derived by hand; independent closed-form derivative matches `mp.diff` to ~50 digits; the unprobed extreme corner `(w, lam) = (4, 0.89)` attacked — clean; m1 one-clause scope fix on the "certified upper bound" sentence; m2/m4 trivia, m3 record-only) | **SURVIVES** (nothing to repair: NX constants re-derived in EXACT rationals + sign-safe reformulations; all 55 block-[B] values rebuilt string-identical; 3,091-point adversarial attack + 8,001-point strictness scans, 0 violations; consumer `X_w6` code-shape and `X = 1.0363` decomposition verified; O1/O2 record-only) |
| **SL4'-E** `wave5_sl4pe_20260812.md` | **PARTIAL with a load-bearing DELTA: Theorem E (the pricing machinery) PROVED** at `m >= 561` from (E-A2)+(E1)+(E2)+**(E3)** by an exact-rational certificate (`REM*(W)`/`J0(W)` archived as fractions; only transcendental `e^x <= 1/(1-x)`); **Prop E.3 PROVED**: the recorded plan (algebra + `kappa_4 >= 0` sign lemma + SL1'-w(i)) CANNOT prove the pricing (hypothesis-consistent point fails by 43%; truth at the W1/W2 right edges independently forces the joint form); **Lemma E.4 PROVED** (limit `kappa_4 > 0` for `w >= 4`; sign boundary `w* = 3.3672 < 4`); **(E3) = SL4'-E-J CONJECTURED** (`J = r31^2 - r42/2 <= J0(W)`; worst measured margin 32.6% at `(561, 5.0)`; roadmap + dead routes recorded) | **MINOR_REPAIRS** (E.1 identities proved SYMBOLICALLY; E.2 certificate re-derived exactly — all 7 `J0` fractions EQUAL; E.3 point + truth forcing confirmed by hand and dps-50; E.4 reconfirmed at K = 800; interface byte-identical to STATUS_wave4/original/REPAIRED consumers, `1/(2 s2) = (lam^2/2)u` reconciled; R1–R6 wording/comment-level; merged-surface coordination note for this editor) | **MINOR_REPAIRS** (all three scripts byte-identical; Lemma E.2 recertified from draft text, fractions EXACTLY equal; **1,764-case hypothesis-boundary attack, 0 violations** (worst engineered ratio 0.9766); truth reproduced by a different cumulant route to 5e-38; 62 off-grid probes 0 FAILs; E.4 at dps 60/K = 1200, tail bound valid; F1–F4 commentary-level, F1 the one a downstream prover must heed) |
| **SL1' deliverable** (S1)+(S2)( + (S3)/(S4) per the composition) | **— NO ARTIFACT — third wave running** (editor disk check (i): no `*sl1*` file exists) | — | — |
| **Composition note** `CL_composition_20260812.md` | **Theorem CL-C ASSEMBLED: CL(79, 20, 0.89) at `m >= 561` PROVED MODULO (S1)–(S4)**, every consumed input two-referee citable (I1–I7); composed constant `C*(m >= 561) = 18.2281 <= 20` (worst row `0.911407` = Lemma R.2 at `m = 700`); `C*(m >= 1581) = 13.0594 <= 136` (10.41x); `[401, 560]` consumer-discharged by exact computation (557/557 PASS, 4th independent parse); adopts M1 (SL3' named in R.2), M2 (seed = (S4)), M3 (X-free rung) explicitly; honesty register §5; **NO FLIP claimed** | **ZERO referees** (new file; the composed statement must be refereed as a unit before the paper cites it — its own §5.4 says so) | — |
| **Flip** | **NOT EXECUTED — correctly.** Editor disk check (i): no flip artifact. Preconditions unmet: (S1)–(S4) unproved; flip-time `assembly_checks.py` block C re-run at the landed spec (band-2 margin `2.83e-4`) and assembly §8 human ratification still owed | — | — |

House-rule reading: **newly citable at two-referee MINOR_REPAIRS-or-better
after wave 5:** the repaired SL4' (`wave4_sl4p_repaired_20260812.md` —
supersedes the never-citable `wave4_sl4p_20260812.md` as the citable SL4'
text), Theorem X.1/SL4'-X (`wave5_sl4px_20260812.md`), and Theorem E /
Prop E.3 / Lemma E.4 (`wave5_sl4pe_20260812.md`). Newly citable
single-verifier: `wave3_repairs_20260812.md` (via
`referee_wave3_repairs.md`, SURVIVES). **NOT yet citable:**
`CL_composition_20260812.md` and `wave4_hygiene_20260812.md` (zero
referees each — both are interface/errata documents whose heavy content
lives in refereed sources, but house rules still owe them passes).

## 2. The final G2 ledger after wave 5

### CL(79, 20, 0.89) — the deep-tilt core lemma. **NOT PROVED. STILL OPEN — but the implication chain to it is now COMPLETE and two-referee at every input node.**

- **Scope (unconditional, hygiene-final):** with sliver repair m1 executed,
  the certified obligation is **`CL(79, 20, 0.89) for m >= 561`** — no
  interim 555-reading survives. `m in [401, 560]` is discharged at
  CONSUMER level by exact computation (557/557 rows PASS, zero gaps,
  `# OVERALL: PASS` on disk — parsed independently by FOUR methods across
  wave 5).
- **The assembled statement:** Theorem CL-C (`CL_composition_20260812.md`
  §2) = CL at `m >= 561` from (S1)–(S4), with composed constant
  `18.2281 <= 20` and NO exception set (the F1/F2 trapezoid, max
  `m = 462`, is moot; the W1 ladder is trapezoid-complement + Fact R.G
  `[561, 699]` + Lemma R.2 `m >= 700`, with M3's per-cell bound as an
  SL4'-X-free analytic alternative on the grid rung). Every input I1–I7
  is two-referee; the composition note itself still owes its unit
  referee.
- **The conditional surface, exactly (verbatim statements in the
  composition note §4) — all CONJECTURED, none with a proof artifact:**
  1. **(S1) [SL1'-w(i)]** banded cumulant scales `|kappa_3| <= R31*(W)
     s2/lam`, `kappa_4 <= R42*(W) s2/lam^2` (R31* = 1.0..2.2, R42* =
     0.8..6.6; truth at the W7 deep corner 2.1215/6.3552 — headroom
     3.7%/3.9%, THE binding truth margins of the campaign).
  2. **(S2) [SL1'-w(ii)]** the R5 core-remainder bound `|R5(t)| <=
     C5*(W) s2 t^5/lam^3` on `[0, lam/2]`, `C5* = 0.05..0.80`
     (acceptance slack 1.6x–8x; W1's slack is `w = 4.30`-class, not
     uniform to the band edge).
  3. **(S3) [(E3) = SL4'-E-J]** the NEW joint cancellation bound
     `J = r31^2 - r42/2 <= J0(W)` (exact rationals archived; worst
     measured margin 32.6% at `(561, 5.0)`; Prop E.3 proves it
     UNAVOIDABLE — the wave-4 "sign lemma" plan is dead, refereed twice).
  4. **(S4) [bootstrap seed]** a-priori `|s2(r(k)-1) - 1| <= 0.89`
     on the deep-tilt band (surfaced by M2, the first SL4' maths pass;
     given ANY seed, the adopted chord/monotone-iteration argument
     closes SL4'.6/.7; weak-CL-shaped; natural home SL1').
- **What wave 5 removed from the wave-4 surface:** SL3'-w (discharged by
  Theorem SL3' consumed in the repaired ledger) and SL4'-X (PROVED —
  Theorem X.1, and independently mooted on `[561, 699]` by M3). What it
  ADDED, honestly: (S3) (split out of SL4'-E by Prop E.3) and (S4)
  (previously hidden inside the "bootstrap" parenthetical). Net: 4
  hypotheses -> 4 statements, but strictly sharper — every one is now a
  cumulant/ratio statement about the tilted Mahonian law, none mentions
  `qhat`/`eta`/tails, and each carries measured margins and a written
  roadmap (limit certificates + one Euler–Maclaurin lemma; W7 needs only
  `r42 >= 0.488` vs truth `>= 5.46`).
- **Truth side (unchanged, corroborative):** CL exactly TRUE at
  `m = 401/402` (REF-B, 17.1x); sl4pe's 27-probe `m = 561` audit + its
  referees' 62 off-grid probes and 1,764-case boundary attack, all PASS;
  SL3' truth attacks to `m = 10^6`, 0 violations.

### Prop 3.5(ii) — refined small-tilt law [T.9]. **CLOSED (modulo listed repairs) — chain fully refereed; unchanged by wave 5** (wave3_repairs now verified SURVIVES, strengthening the T.9-side citations).

### Prop 3.5(i) — crude uniform law [T.8]. **PARTIAL — reduced to CL (reduction two-referee, unchanged); CL's residual scope `m >= 561`; MR-1/MR-2 now citable through the verified `wave3_repairs_20260812.md`.**

R2 remains conditional on exactly CL; part I's finite citation stands at
`m <= 560` (`harness_m200_20260811.md` + `harness_m560_20260812.md` read
through the hygiene overlay + the sliver audit). The flip-time re-run of
`assembly_checks.py` block C at the landed spec is still owed (band-2
margin `2.83e-4` the tight one).

### G2 overall

Theorem A (Mahonian limit `sigma^2(r_m(k) - 1) -> 1`, F2(a)) = the
composite chain + Theorem CL-C: **PROVED CONDITIONAL on exactly
(S1)–(S4)**. Finite companions (argmin centrality, min = central,
`sigma^2(r_m - 1) >= 187/216` iff-`m = 6` equality, strict increase):
unconditional theorems for `5 <= m <= 560` (C5 scope per the standing
erratum; `m = 4` C2/C3 exception known). G4: part-(c) band `[401, 536]`
computation-closed (unchanged); constant chase remains. G3: untouched,
research.

### §2a. Recorded-not-applied repair inventory (all text-level; next hygiene batch)

None moves a constant, bound, threshold, or verdict (both referees, each
file). To be applied as recorded errata in the next hygiene batch, then
that batch verified:

1. **Repaired SL4'** (`wave4_sl4p_repaired_20260812.md`): R1 = M1 (name
   Theorem SL3' in Lemma R.2's hypothesis list + the [C2] inputs bracket
   — the composition already cites R.2 WITH SL3' named); R2 = M2 (carry
   the bootstrap-seed flag in its own §8 status lines; the composition
   already carries it as (S4)); R3 = m4–m6 (provenance clause for the one
   `sl4pr_common.py` comment edit — also numerics RF-2; B4-coverage
   description; 25k-attribution); R4 = m7 or adopt M3 into Cor R.3;
   RF-1 (efac `0.88480` display rounds past the boundary — print
   truncated or "(rounded; safe working cutoff 0.8464)").
2. **SL4'-E** (`wave5_sl4pe_20260812.md`): maths R1–R6 (ratio-sentence
   magnitudes; `0.7857 -> 0.7856`; scope the "safe direction" claim;
   two script comments; E.4(iv) wording) + numerics F1–F4 (F1 the
   load-bearing one for the SL1' prover: the limit-vs-561 gap is
   `<= 5e-4` on W1–W4 edges but `2.2e-3` at the W6b edge — do NOT budget
   a uniform 5e-4; F2/F3/F4 commentary). Note the maths referee's
   calibration warning: (E3) is calibrated to `J0 = J* - REM*` — any
   re-derived envelope must not weaken `REM*` without re-checking `J0`.
3. **SL4'-X** (`wave5_sl4px_20260812.md`): m1 (one clause in Cor X.3 +
   §7(a): "certified upper bound ON THE CROSSOVER INTEGRALS IT SUMS —
   the row's pricing normalization lives in the SL4' cycle"); m2/m4
   trivia; m3 record-only (the `1.9238` floor is spent — do not sharpen
   casually). Plus numerics O1: the WAVE-4 sl4p report's own
   "`>= 1.7e-3`" mis-floors its archive (true min `1.688e-3`) — one-word
   debt on that file.
4. **Standing wave-4 items already discharged by the hygiene overlay**
   (read the four target files THROUGH `wave4_hygiene_20260812.md`):
   sliver m1–m6; harness §2/§3; SL3' R1–R5 (consumers MUST budget off
   the corrected headline: worst certified margin 1.30x at W7
   `tau_start`, worst CELL headroom 7.96x, truth ~16x); wave2_repairs
   W-F1. Residual: the from-scratch fresh harness re-run is still
   stalled at `m = 441` (byte-identical so far; record-only).

## 3. THE BOTTOM LINE: is Theorem A = F2(a) fully proved?

**NO — and the residue is not "minor repairs".** Theorem A = F2(a) is
**PROVED CONDITIONAL on exactly four named open statements (S1)–(S4)**,
all of one kind (core-model cumulant/seed statements about the tilted
Mahonian law), NONE of which has a proof artifact. That conditionality is
REAL MATHEMATICS, not hygiene: (S1)'s binding truth margins are 3.7%/3.9%
at the W7 deep corner, (S3) is a genuinely new obligation that wave 5
itself proved unavoidable (Prop E.3, twice refereed), and (S4) is
weak-CL-shaped. No grade inflation is possible here: a reader who removes
any one of (S1)–(S4) has no theorem.

**What IS fully in place (the complete conditional chain, every node
citable):** for `m in [5, 560]`, Theorem A's finite part holds
UNCONDITIONALLY by exact integer computation
(`harness_m200_20260811.md` + `harness_m560_20260812.md` +
`wave4_hygiene_20260812.md` §2 + the sliver audit). For `m >= 561`,
[(S1)–(S4) ==> CL(79, 20, 0.89)] via Theorem CL-C
(`CL_composition_20260812.md`, consuming: composite A2/A3/C.1/[W.6] +
Theorem SL3' (+ ROUTE + 2 referees) + sliver SLV.1–.3 (+ 2 referees +
hygiene m1) + Theorem SL4'-R/R.G/R.1/R.2/R.3 (+ 2 referees) + Theorem E /
Prop E.3 / Lemma E.4 (+ 2 referees) + Theorem X.1/X.2/X.3 (+ 2
referees)); and [CL ==> Theorem A] via the wave-2/3 assembly
(`theoremA_assembly_20260811.md` + its referees + `repairs`/
`wave2_repairs`/`wave3_repairs` each with their verifier).

**The exact residue, nothing else:**

1. **(S1)+(S2)+(S3)+(S4)** — the SL1'-class deliverable (one prover
   package; roadmap and dead-routes written in `wave5_sl4pe` §6; budget
   off 3.7%/3.9% (S1), 32.6% (S3), and the W6b-edge `2.2e-3`
   discretization gap per sl4pe-numerics F1), then TWO referees on it.
2. **Referee the composition note as a unit** (and give the hygiene
   overlay its single-verifier pass).
3. **Apply the §2a recorded repairs** (text-level; next hygiene batch).
4. **The flip:** re-run `assembly_checks.py` block C at the landed spec
   (band-2 margin `2.83e-4`), then assembly §8's human ratification.

Items 2–4 are mechanical/process; item 1 is the only remaining
mathematics between this campaign and unconditional Theorem A.

**Standing caveats (all flagged, none hidden):** Theorem SL3' and the
E.5.3/E.6 certificates remain the flagged monotone-cell class (worst
certified crossover margin 1.30x at W7, truth ~16x); Fact R.G is
grid-class over the `w`-continuum (M3's cell-floor bound is the stronger
in-class replacement, adopted by the composition as the alternative
rung); Lemma E.4's two point evaluations and the NX-1..6 constants are
the named-constant class (referee-reconfirmed at higher precision);
Theorem E's certificate is exact-rational — STRONGER than the flagged
class; ledger rows are dps-40 on the twice-validated engine, thin margins
W5 `0.98909`@401 (1.1%) / W7 `0.98084`@401 (1.9%) dps-100-robust,
relaxing to `0.70933`/`0.8723` at the operative 561; INFL/QUADF bootstrap
margins 0.3%/1.8% now explicitly conditional on (S4); harness rows
4..481 are honored `results_m540.txt` rows (fresh re-run stalled at 441,
byte-identical so far); thin wave-3 margins unchanged (t_0 cap
`2.76e-4`, c2 0.2%, W7 `min(m, s2) = m` 1.0%); NX-5's `2.76e-4` gap to
1.074 and Lemma X.a's spent `1.9238` floor are flagged do-not-sharpen
points.

## 4. The one-sentence paper claim

**The F2 section may now claim, in one sentence:**

> "Theorem A holds conditional on the single explicitly-stated core lemma
> CL(79, 20, 0.89), whose scope has been reduced by exact integer
> computation to `m >= 561` and whose proof is assembled, with every
> input verified by two independent adversarial referees, as an
> implication from exactly four explicitly-stated open statements about
> the cumulants of the tilted Mahonian law — banded third/fourth-cumulant
> scales, a fifth-order remainder bound, a joint cancellation bound, and
> an a-priori ratio seed — all supported by extensive exact and
> adversarial computation but none yet proved."

The finite companions remain unconditional theorems for `5 <= m <= 560`.
The paper must NOT say F2(a) is proved; must NOT call CL "nearly proved"
(each of (S1)–(S4) is genuinely open, and (S3) was UNAVOIDABLY added this
wave — the surface can grow under scrutiny as well as shrink); must not
cite `CL_composition_20260812.md` or `wave4_hygiene_20260812.md` until
their referee passes land; and must cite SL4' ONLY through
`wave4_sl4p_repaired_20260812.md` (the original `wave4_sl4p_20260812.md`
remains non-citable, superseded).

## 5. Remaining human steps

1. **Ratification (now):** a human should read Theorem CL-C
   (`CL_composition_20260812.md` §2 + §4) and confirm the (S1)–(S4)
   surface is acceptable as the paper's stated conditionality; then walk
   the assembly §8 ratification checklist as far as it goes today
   (everything except the flip items).
2. **Paper integration (now):** merge §4's one-sentence claim + the
   finite-companion theorems (`m <= 560`) into the F2 section; cite per
   the §1 house-rule reading and the §4 prohibitions.
3. **Commission the SL1' package** — (S1)+(S2)+(S3)+(S4), one prover,
   two referees. This is the entire remaining mathematics. If it lands:
   referee the composition as a unit, apply §2a repairs, execute the
   flip (block C re-run at the landed spec + human sign-off), and
   Theorem A is unconditional.
4. **Decide on the stalled fresh harness re-run** (record-only;
   relaunch or retire the flag — the sliver-numerics referee's call).
5. **G4 next** (its `[401, 536]` band is computation-closed; remaining
   work is the `C_ker(4)` constant chase per wp2-a2 §10 item 3, with
   region-3 constants and the 401/402 truth data in hand). **G3 after**
   (untouched; still research).

*End of STATUS_wave5.md.*
