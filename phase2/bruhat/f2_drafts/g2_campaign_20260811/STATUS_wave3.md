# STATUS_wave3 — G2 closure campaign, wave-3 synthesis (2026-08-12)

*Synthesis editor pass, wave 3 (read-everything role; blind protocol lifted
for this file only). Sources: everything new under `g2_campaign_20260811/` —
`wp4_plan_20260811.md`, the prover deliverables `wp4_sl_SL2.md` /
`wp4_sl_SL3.md` / `wp4_sl_SL5.md`, `wp4_draft_composite.md`,
`theoremA_assembly_20260811.md`, `wave2_repairs_20260811.md`, and the four
wave-3 referee reports (`referee_maths_wp4.md`, `referee_numerics_wp4.md`,
`referee_maths_theoremA.md`, `referee_numerics_theoremA.md`) — plus
`STATUS_wave2.md` as the governing prior ledger. `g2_draft_t1_20260803.md`
remains unread by every wave-3 agent and by this editor. No existing file
modified; this file is new (no-erasing rule). House rules applied: an item is
CLOSED only when the draft(s) closing it hold SURVIVES or MINOR_REPAIRS from
BOTH referees; MINOR_REPAIRS = closed-modulo-listed-repairs; every NEW repair
list is copied in below (§2a–§2b). Two facts in this file come from this
editor's own disk checks (2026-08-12 02:2x): the `results_m540.txt`
completion status (§1 row 7, §4) and the absence of any
`referee_wave2_repairs*` file (§1 row 7). No new mathematics is asserted
here; no new scripts were needed.*

**Executive summary.** Wave 3 delivered (a) the Theorem A assembly note,
now TWO-REFEREE MINOR_REPAIRS — **Theorem A = F2(a) is PROVED CONDITIONAL
on exactly one named statement, `CL(79, 20, 0.89)`, and that reduction is
now fully refereed**; (b) three of wp4's five sub-lemmas PROVED and
referee-verified (Theorems A2, A3, Lemma C.1 — real, reusable analysis);
(c) an honest negative result: the ARCHITECTED route to CL's assembly step
is numerically refuted (orphaned SL4 evidence, robustness-checked by the
numerics referee), so **CL itself remains OPEN** with a precisely restated
smaller bridge (SL1' + SL3' + SL4' + SL-sliver); (d) the wave-2 repair
lists §2a/§2b/§2c APPLIED (`wave2_repairs_20260811.md`) — but that file has
ZERO referees yet, and its §D harness-to-540 run DIED INCOMPLETE at
`m = 481` (no OVERALL line). No grade inflation: Theorem A is NOT
unconditional; the bottom line is §3.

## 1. Wave-3 verdict table

| Package | Deliverable | Draft self-reported status | Maths referee | Numerics referee |
|---|---|---|---|---|
| **wp4 plan** `wp4_plan_20260811.md` | Architect decomposition of CL into SL1–SL5, band geometry, ledger targets | SL1–SL5 all CONJECTURED-with-verified-numerics (a plan) | (refereed via the composite) route defects found and documented: D2 (W.6-slot arithmetic needs an unavailable `A`-cap), D3 (far display drops `1/lam`), B.0(i)-fallback arithmetic slip (`0.024 m^3` gives 221.3, not 0.028), false far-entry monotonicity quantifier — all repaired downstream; **the ledger NORMALIZATION of SL4 is refuted** (§2 below) | headroom claims corrected: NC-PL1's "8–23%" is a grid artifact — W7 deep corner (`lam -> 0.89`, missed by its own grid) has only ~3.7–3.9% (H1)-headroom (finding F2); NC-PL1's W1 min 0.3189 also a grid artifact (true ~0.2992, composite R8) |
| **SL2** `wp4_sl_SL2.md` | Band floor `A = lam^2 s2 >= c_A(w) m` (Theorem A2), exact identity `lam^2 Var(U_j) = h(lam) - h(j lam)`, zero-discreteness certificates, `s2 >= 141.7498 > 79`, `min(m, s2) = m` bonus | **PROVED** | verified "CORRECT, fully" (hand re-derivation of every lemma, `referee_maths_wp4.md` §1.1) | all scripts byte-identical; independent dps-60 rebuild; off-grid corner attacks (`w -> 4+`, `lam = 0.89`, `m` to 1e5): 0 violations |
| **SL3** `wp4_sl_SL3.md` | Two-tier extended Gaussian domination (`c1 = 0.1317 >= 1/8` on `t <= 0.8 lam`; `c2 = 0.0871 >= 1/11.5` to `1.074 lam`, ALL `m >= 2`), tail bucket P1/P2/P3, Lemma C.1 (= SL3.B), `t_0 <= 1.074 lam` | **PROVED** (deviations D1–D3 from plan, flagged) | verified "CORRECT, fully" (§1.2; incl. the wp1-c W.3/W.5(ii) cross-citations verbatim, `q(2,1) = 0.0741265` re-derived by hand) | scripts byte-identical; direct-complex-sum scope attack at `m in {2..30}`: 0 violations; exact `eps_j` attacked to `j = 2000`: clean |
| **SL5** `wp4_sl_SL5.md` | Band-arithmetic ledger => CL, conditional on (H1)–(H4); Lemmas SL5.0/SL5.1; two real corrections to the plan (far-entry quantifier; B.0(i) fallback) | **PROVED modulo (H1)–(H4)** | verified (§1.3); both plan-corrections confirmed real and necessary | exact-Fraction certificate chain audited at source level; `far(401) <= 9.229e-4` sharp to 4 digits |
| **SL4** | — no deliverable (session died) — | — | orphaned `sl4_nc1.py` + archived output read line-by-line; its Part B REFUTES the architected slot normalization (mid transfer ~`A`x, far ~`s2`x, R5 ~16x larger than priced); Part A SUPPORTS the model algebra (`|eta|/u <= 0.963`) | refutation robustness-checked: replacing the orphan's `gamma = 1/8` by the proven `0.1317` still gives honest W1 mid entry 101.41 vs slot 1.0125 (REF-C C7) — not an artifact |
| **SL1** | — NO artifact of any kind — | — | (H1) remains CONJECTURED; and under the honest normalization its architected `C5 = 3/8` is ~16x too weak at W1 | (H1) constants TRUE at every measured point, but W7 deep-corner headroom only ~4% (F2) — wave-4 prover must budget off the corrected margins |
| **Composite** `wp4_draft_composite.md` | Assembled state: Theorems A2/A3/C.1 + conditional Theorem CL-composite ((H1) & (H4) => CL, `C*_eff = 16.9088 <= 20`); §5.2 refutation account; §5.3 honest bridge | **PARTIAL** — CL PROVED MODULO (H1)+(H4); architected (H1)+(H4) likely not assemblable as stated | **MINOR_REPAIRS** (`referee_maths_wp4.md`: R1–R4, all text-level; "this verdict does NOT certify CL — CL remains OPEN") | **MINOR_REPAIRS** (`referee_numerics_wp4.md`: F1–F7; 13/13 scripts byte-identical; NEW exact ground truth at `m = 401/402`: CL TRUE, 0 violations on 260 adversarial `k`, 17.1x margin) |
| **Assembly** `theoremA_assembly_20260811.md` | The merged Theorem A note: parts I/III/IV unconditional, part II via Theorem S + the T.9-final plug (5 checks) + `[WP4-CITATION]` in exactly one place; constant ledger; flip instruction | Theorem A PROVED CONDITIONAL on CL | **MINOR_REPAIRS** (`referee_maths_theoremA.md`: MR-1–MR-4; graph complete + acyclic; every citation traced verbatim-true; plug confirmed on all five checks) | **MINOR_REPAIRS** (`referee_numerics_theoremA.md`: N-F1–N-F3; script byte-identical; full harness re-run byte-identical mod timing; independent exact re-derivation of every block; ledger traced row-for-row) |
| **Repairs application** `wave2_repairs_20260811.md` | STATUS_wave2 §2a (A1–A11), §2b (B1–B10), §2c (C1–C8 = the pending t2_repairs) all applied as errata; no certified digit moved (§E check); §D harness extension to 540 | all applied; three content repairs (B1/C1/C3) use referee-supplied verified proofs | **ZERO referees** (house-rule debt — the wave-2 analogue `repairs_20260811.md` got a SURVIVES pass; this one has none yet) | — ; and its §D run is **INCOMPLETE**: `results_m540.txt` last row `m = 481` (all PASS through 481), process dead, NO "# OVERALL" line — the `[401, 534/536]` G4 band is NOT yet pre-cleared (481 covers only `[401, 481]`) |

House-rule reading of the SL files: the designated referee UNIT was the
composite; both wave-3 wp4 referees read `wp4_sl_SL2/SL3/SL5.md` in full,
re-ran their scripts, and verified their content (maths: hand
re-derivation; numerics: independent rebuild + off-grid attack). So
**Theorems A2, A3, Lemma C.1, and conditional Theorem CL-composite, AS
RESTATED IN `wp4_draft_composite.md`, are citable at two-referee
MINOR_REPAIRS**; cite them through the composite, not the bare SL files.

## 2. The final G2 ledger

### CL(79, 20, 0.89) — the deep-tilt core lemma. **NOT PROVED. STILL OPEN.**

Both wave-3 referees are explicit ("this verdict does NOT certify CL";
"CL remains PROVED MODULO (H1) + (H4) exactly as the draft states"). What
wave 3 changed, honestly itemized:

- **Delivered and two-referee-verified (via the composite):**
  - *Theorem A2* (= SL2): `A = lam^2 s2 >= c_A(w) m` with banded
    `c_A = 0.28/0.35/0.42/0.52/0.60/0.70/0.80`, exact-rational certificates,
    zero discreteness loss; `s2 >= 1122800/7921 = 141.7498 > 79` on the whole
    band (CL's `s2 >= 79` hypothesis never binds); `min(m, s2) = m` (W7
    margin 1.0%, flagged not-spendable).
  - *Theorem A3* (= SL3): two-tier Gaussian domination on the `lam`-scale
    (`exp(-s2 t^2/8)` to `0.8 lam`; `exp(-s2 t^2/11.5)` to `1.074 lam`; ALL
    `m >= 2`, `0 < |lam| <= 0.89`) + the tail bucket
    `T_u <= 3.192 sqrt(A) e^{-A/32} + 2.87 sqrt(A) e^{-0.0556 A} + P3`,
    `P3(401) <= 1.3e-7`. New mathematics, independently reusable.
  - *Lemma C.1*: `A <= m h(lam) < m`, `h(x) = (x/2)^2/sinh^2(x/2)` — three
    independent proofs; retires B.0(i)-class crude caps inside wp4.
  - *Conditional Theorem CL-composite*: (H1) & (H4) ==> CL(79, 20, 0.89)
    with `C*_eff = 16.9088 = 4734473/280000 <= 20` (15.5% assembly headroom;
    `10.081 <= 136` at `m >= 1581`).
- **Still missing:** (H1) = SL1 (core cumulant model — NO artifact) and
  (H4) = SL4 (kernel/inversion assembly — orphaned script only). AND the
  architected (H1)+(H4) pair is the WRONG target: the orphan's Part B
  (verified faithful by the maths referee, robustness-checked by the
  numerics referee) shows the honest numerator transfer prices the tail/R5
  slots ~`A`x to ~`s2`x above the plan's normalization — with (H1)'s
  `C5 = 3/8` and A3's proven `gamma = 0.1317` the honest W1 row is ~130 vs
  budget 5.6. **The real remaining bridge is composite §5.3:**
  - *(SL1')* banded core-remainder `C5* = 0.05/0.06/0.08/0.10/0.15/0.25/0.80`
    (measured truth 0.0065–0.2104, 3.8x–6x headroom);
  - *(SL3')* mid-exponent upgrade `gamma* = 0.42/0.42/0.40/0.40/0.38/0.34/0.32`
    (truth 0.38–0.49; the per-factor loss `eps <= 0.35` must drop to
    ~0.10-class — the genuinely new analysis);
  - *(SL4')* kernel-weighted assembly with the honest slots (orphan Part C:
    closes W2–W6b at `m = 401`; W7 closes with computed-eta pricing ~15.7 <
    16.0; needs the real write-up);
  - *(SL-sliver)* the W1 far sliver `w in (4, ~4.51]`, `m in [401, ~450]`
    (A3-floor sizing; ~560 under the orphan's cruder floor): closable by a
    sharpened small-tilt far bound OR a finite harness extension to ~450–560.
- **Truth side (new, referee-grade evidence, not proof):** CL is TRUE at its
  own threshold — exact integer computation at `m = 401` and `402`
  (`referee_numerics_wp4.md` REF-B): 260 adversarial `k` at 401, violations
  all zero, `max eps*min(m, s2) = 1.17187` vs the asked 20 (17.1x margin,
  max at `w ~ 4.9` exactly where the plan predicted). A2's floor, C.1's cap,
  `s2 > m`, `r(k) >= 1` all verified at the actual mean-matched pairs.

### Prop 3.5(ii) — refined small-tilt law [T.9]. **CLOSED (modulo listed repairs) — unchanged, and its repair lists are now APPLIED.**

Theorem T.9-final's status is exactly STATUS_wave2 §2's; wave 3 added:
`wave2_repairs_20260811.md` §A/§B applies every §2a/§2b item (the E-decimal
reprints, `rho(4) <= 0.72711`, the "~68"->82 and "~27"->23 wrong-number
fixes, Lin no-double-count, P.7 rescope to `|w| <= 8`, LFlow provenance,
genuine D.5 table rows at 181/367). Pending: the referee pass on
`wave2_repairs_20260811.md` itself (§1 row 7).

### Prop 3.5(i) — crude uniform law [T.8]. **PARTIAL — reduced to CL; the reduction is now TWO-REFEREE.**

Unchanged mathematical content (Theorem S: R1a/R1b unconditional, R3 closed
by the T.9-final plug, R2 conditional on exactly CL), but upgraded
certification: the plug and the whole stitch are now refereed AS A UNIT
(both `referee_*_theoremA.md`, MINOR_REPAIRS), including the genuinely new
`w^2`-bracket check with the actual plugged `C_A` (positive, exact scan +
MR-1's supplied all-`m` fix).

### T2 bookkeeping. **§2c APPLIED** (`wave2_repairs_20260811.md` §C = the
pending t2_repairs file): T.10(2) citable as `rho = 1 - 0.022 w_0^2`
(repaired form ONLY), T.8'' citable with the memorylessness route and
`m_* >= sqrt(s2/m) - 2` — both still consumed nowhere in the Theorem A
chain. Pending the wave2_repairs referee pass.

### §2a. Wave-3 repair list: `wp4_draft_composite.md` (union of both referees; none moves a constant, threshold, or verdict)

1. (maths R1, load-bearing clarification) Record in §3/Remark C.3 that the
   delivered CL band is `|lam| in (4/m, 0.89]` while wp3-a2 §5's bare
   parameter form has no `4/m` cut — R2 (the sole consumer) is `|w| > 4` by
   definition, so nothing breaks, but the scope note must exist so no future
   session mis-plugs a `|w| <= 4` case into CL.
2. (maths R2) §7's "10.08 <= 136" rounds a certified UPPER bound DOWN; print
   10.081 (exact 201619/20000).
3. (maths R3) §3's mirror step: re-point `s2(-lam) = s2(lam)` to SL2 §5.3
   (evenness of `h`), not the §0 frame.
4. (maths R4, optional) Qualify §5's truth-margin sentence: NC-PL3 is
   `m = 120/200` (below scope); at-scope support is NC-PL1's budget column +
   NC-P3d — and now the numerics referee's REF-B at `m = 401/402` (cite it).
5. (numerics F1) Reprint the `total<=`/`margin` columns of asm table [1] and
   SL5's NC-SL5-1 in ceil/floor direction (nearest-rounded now; worst gap
   < 5e-5; W1 margin prints `0.86615 -> 0.86552`).
6. (numerics F2 — the one substantive item) Correct the (H1) headroom
   sentence: "8–23%" holds on W1–W6b only; the W7 deep corner
   (`lam -> 0.89`, missed by NC-PL1's own grid — its `w = 356.9` point has
   `lam > 0.89` and is silently skipped) has `R31 = 2.1215` vs 2.2 (3.7%)
   and `R42 = 6.3552` vs 6.6 (3.9%); geometric limits 2.1303/6.4113. The
   wave-4 prover must budget off THESE margins.
7. (numerics F4) Measured `C5` truth range is "0.0065–0.2104" (not
   "0.0083–..."); safe direction.
8. (numerics F6) "P3(401) = 1.2568e-7" -> `1.2569e-7` (nearest) or keep
   `<= 1.3e-7`. (F3/F5/F7 are record-only observations, no text forced.)

### §2b. Wave-3 repair list: `theoremA_assembly_20260811.md` (union of both referees)

1. (maths MR-1 — the one genuine proof gap; fix supplied AND verified) The
   R3 `w^2`-bracket's positivity beyond the scanned range `[401, 2000/3001]`
   has no displayed proof. Fix: via g1_b B.0(ii) (`B_m <= 1.080/m`,
   proof-grade), `bracket(m) >= 6.85 E(4)(1 - 18.36/m - C_A/m^2) - 1.080/m`,
   term-by-term increasing, `= 0.009571/0.009551 > 0` at `m = 401` — all
   `m >= 401`, no scan. Insert in §2.3 R3 / §4 item 4; ground §4-A3's
   "increasing -> 1" tail the same way.
2. (maths MR-2 — statement-level overclaim; fix supplied) §0 attributes the
   `27/25`-form's `O(m^{-2})` constant to `C_A`; recentring `B_m ->
   (27/25)/m` costs an extra `<= 0.55/m^2` (numerics: exact scan
   `(27/25 - B_m m) m in (0.34, 0.54]`). Either scope §0's clause to the
   `1 - B_m` form, or add the one-line certificate and state `C_A + 0.55`.
3. (maths MR-3 = numerics N-F1) §4's "Verbatim script output" is a condensed
   excerpt (~7 archived lines dropped, all extra PASSes; rows merged).
   Relabel "condensed excerpt; full output archived, re-run byte-identical
   by both referees" — the established wp3-a2-F7 repair class.
4. (maths MR-4) Exact-center note: state the clean route (`s2 = lambda` at
   center, `e^x - 1 >= x`, so `lambda(r-1) >= 1 - B_m - 1.1/m^2`, no Bona)
   or the `1.1 + 0.6 = 1.7 <= C_A` form — one of the two.
5. (numerics N-F2) Add the one-sentence absorption note for the recentring
   error (`0.54 + 1.8 << C_A`) — same substance as MR-2.
6. (numerics N-F3) "6.7x" margin at the spec point mixes pairs: 6.5x vs the
   20/79.5 budget, 6.7x vs eps*. Print one or both correctly (inherited
   verbatim from STATUS_wave2 §2 — the same fix applies to any future quote
   of that line).
7. (referee observations, no action in the assembly) O1: §7 item 4's
   "pending" is stale in the safe direction for §2a/§2b (wave2_repairs now
   exists); the t2 list is §C of the same file. O3: fold the harness-report
   C5 scope erratum (`5 <= m`, not `4 <= m`) into the next repairs file.

## 3. THE BOTTOM LINE: is Theorem A = F2(a) fully proved?

**NO.** Theorem A is **PROVED CONDITIONAL on exactly one named open
statement — `CL(79, 20, 0.89)` for `m >= 401` (lower-bound form suffices)—
and, new in wave 3, that reduction is now TWO-REFEREE CERTIFIED**
(`theoremA_assembly_20260811.md` + `referee_maths_theoremA.md` +
`referee_numerics_theoremA.md`, both MINOR_REPAIRS): parts I (exact
`m <= 400`), III (upper bound), IV (conclusion) are unconditional;
`[WP4-CITATION]` is load-bearing in exactly one place (Theorem S's R2 row);
the dependency graph is verified complete and acyclic; every citation
traced verbatim-true; the plug confirmed five-for-five. CL itself remains
open mathematics: wave 3 proved three of its five sub-lemmas plus the
conditional assembly, refuted the architected route for the other two, and
verified CL's truth exactly at the operating threshold (17.1x margin). The
distance to unconditional Theorem A is the §5.3 bridge, nothing else.

**What remains, smallest first:**

1. **Finish the m = 540 harness run** (`run_m540.py` died at `m = 481`,
   all rows PASS, no OVERALL line — relaunch or resume; ~minutes-to-hours).
   Needed for G4's part-(c) band `[401, 536]`, NOT for Theorem A — but also
   the cheapest half of the SL-sliver option (b) if extended to ~560.
2. **Referee pass on `wave2_repairs_20260811.md`** (single verifier,
   mirroring `referee_repairs_20260811.md`) — until then the §2a/§2b/§2c
   discharges and the repaired-form citability of T.10(2)/T.8'' are
   provisional.
3. **Apply the wave-3 repair lists** (§2a/§2b above) to a new
   `wave3_repairs` file; MR-1/MR-2 carry supplied, script-verified fixes;
   everything else is text-level. Half a session.
4. **The wave-4 CL bridge** (the only remaining new mathematics), per
   composite §5.3 with the numerics referee's corrected budgets: (SL-sliver)
   — see item 1 option — then (SL1') banded `C5*`, (SL3') mid-exponent
   `gamma*` (the hard part: per-factor loss 0.35 -> ~0.10), (SL4')
   kernel-weighted honest ledger. Substrate: Theorems A2/A3/C.1 as
   delivered. Then two referees on the wave-4 package (house rule).
5. **Flip**: execute assembly §3's one-citation flip (re-run
   `assembly_checks.py` block C if the landed spec is weaker; band-2 margin
   2.83e-4 is the tight one), then apply the assembly's own referee repairs
   if not already folded.

**If (4) lands, the complete file-level dependency chain for unconditional
Theorem A = F2(a) is** (updating STATUS_wave2 §4):
`F2_PROOF_DRAFT.md` + `g1_draft_b.md` (+ `g1b_repairs_20260802.md`) +
`g2_draft_t2_20260803.md` (two-referee inventory; §2c repairs now in
`wave2_repairs_20260811.md` §C) + `wp1_draft_c.md` + `wp2_draft_b.md` +
`repairs_20260811.md` + `wp2_draft_a2.md` + `wp3_draft_a2.md` +
`harness_m200_20260811.md` + `wave2_repairs_20260811.md` (+ its pending
referee) + `wp4_draft_composite.md` (Theorems A2/A3/C.1 + CL-composite) +
[the wave-4 bridge package + its two referees] +
`theoremA_assembly_20260811.md` (+ `referee_maths_theoremA.md`,
`referee_numerics_theoremA.md`) + [the `wave3_repairs` file], with §2a/§2b
folded at paper-assembly.

**Standing caveats inside that chain (all flagged, none hidden; unchanged
from STATUS_wave2 §4 except as noted):** the four grid-certificate-class
inputs (wp2-b `c_4` floor, `c_w` envelope, PW grid flavor, wp2-a2
`m > 3000` monotonicity tail — each Sturm-able, each referee-attacked
off-grid without violation); Bona's `r(k) >= 1` (ambient citation, wp2-b
W.5/Lin only; the exact-center LB needs no Bona per MR-4); thin certified
margins in wp4 (t_0 cap 2.76e-4; `c2` 0.2%; W7 `min(m,s2) = m` 1.0%; W1
ledger row 0.8655 — all point-evaluation class, all flagged); the
harness-report C5 scope erratum (display says `4 <= m`, runner exempts
`m = 4` — fold into wave3_repairs).

## 4. What this means for the submitted paper draft, and for G4/G3

**The paper's F2 section (currently an honest conjecture) can now be
upgraded — but only to "conditional theorem", not "theorem".** The
defensible upgrade, fully backed by the two-referee assembly unit:

- State **Theorem A modulo one explicitly named lemma**: "Theorem A holds
  conditional on CL(79, 20, 0.89) [statement displayed in full]; the
  reduction is complete and refereed" — with `theoremA_assembly_20260811.md`
  §2 as the proof skeleton, its §5 dependency table as the citation
  apparatus, and the assembly's §8 ratification checklist for the human
  co-author (half a day, per the assembly's own estimate).
- The **finite companions are unconditional and exact** and can be stated
  as theorems outright: argmin centrality, min = central, `sigma^2(r_m - 1)
  >= 187/216` (equality iff `m = 6`), strict increase — for `5 <= m <= 400`
  (harness, exact integer arithmetic; scope `5 <= m`, per the C5 erratum).
- Honest support sentence available: CL's truth is verified by exact
  computation at `m = 401/402` (0 violations, 17.1x margin) and its five
  sub-lemma decomposition is three-fifths proved (Theorems A2/A3/C.1).
- What the paper must NOT say: that F2(a) is proved; that CL is "nearly
  proved" (the architected route is refuted — the remaining bridge is
  precisely stated but genuinely open, and SL3' needs new analysis); or any
  citation of T.10(2)/T.8'' as displayed.

**For G4 (part-(c) constant chase):** the crude `C_A ~ 3.8e4` puts the
analytic `187/216` crossover at `m* = 535/537`; the harness-to-540 run that
would pre-clear the `[401, 536]` band DIED at `m = 481` — so G4's band is
currently only narrowed to `[482, 536]`. Finish the run (item 1 of §3);
alternatively the flagged mechanical `C_ker(4)` sharpenings (wp2-a2 §10
item 3) shrink `C_A`. G4 otherwise gains: all region-3 constants explicit,
item-5 exponents, the wave-3 exact truth data at 401/402.

**For G3 (part-(b) fine scale):** untouched by wave 3; still research.

## 5. Recommended next session

1. **Relaunch/resume `run_m540.py`** first (background, cheap): closes G4's
   band and, if pushed to ~560, finitely closes the SL-sliver's harness
   option — removing one of the four wave-4 work items before wave 4 starts.
2. **Wave-4 CL bridge, as its own blind mini-campaign (the priority).**
   Assignments per composite §5.3, with the corrected numbers in the
   drafting kit: (a) SL1' with banded `C5*` targets and the TRUE margins
   (truth 0.0065–0.2104; W7-deep-corner (H1) headroom ~4%, geometric limits
   2.1303/6.4113 — numerics F2); (b) SL3' (`gamma*` bands; route must cut
   the per-factor loss 0.35 -> ~0.10 — keep the `sin^2` mass beyond the
   first truncation point, or log-convexity of the factor product); (c) SL4'
   (kernel-weighted ledger; orphan Part A's computed-eta machinery + REF-C
   C7's robustness note so nobody re-litigates `gamma = 1/8`); (d) SL-sliver
   if not already closed by item 1. Substrate: Theorems A2/A3/C.1 (cite via
   the composite). Two referees per deliverable.
3. **Housekeeping session (can run concurrently):** referee pass on
   `wave2_repairs_20260811.md`; write `wave3_repairs` applying §2a/§2b
   (MR-1/MR-2 fixes are supplied and verified — transcription only); fold
   the harness C5 erratum.
4. **On CL landing:** execute the assembly's flip instruction, commission
   nothing further for F2(a) — the refereeing of the flipped document is
   already done modulo the flip itself — then move to G4 (mechanical) and
   G3 (research), in that order.

*End of STATUS_wave3.md.*
