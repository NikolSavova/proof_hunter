# referee_numerics_sol_s4 — adversarial NUMERICS referee on `sol_s4_20260812.md` (wave 6b, cross-model)

*Adversarial numerics pass, 2026-08-12, on gpt-5.6-sol's (S4) attempt
(`sol_s4_20260812.md`). Bar: maximal, default-to-refutation; a cross-model
draft gets no extra credit. Protocol: every numeric re-derived from SAVED+RUN
scripts (`g2_scripts/campaign_20260811/wave6b_ref_s4/`, outputs archived
beside them and quoted verbatim below); exact rationals where feasible,
mpmath dps 30–60 elsewhere; the draft's VERIFICATION RECIPE was scripted in
full AND augmented with adversarial checks it omits (off-grid band edges,
`w -> 4+`, W2 left edge, `m = 561`, end-to-end truth of `r_m(k)`).
`g2_draft_t1_20260803.md` unread; `gamma = 1/8` not re-litigated. Context
consumed: `STATUS_wave5.md`, `CL_composition_20260812.md` (§4: the (S4)
statement), `referee_maths_sl4p_repaired.md` (M2/M3),
`wave4_sl4p_repaired_20260812.md` (Lemma R.1 statement),
`wp4_draft_composite.md` + `wp4_sl_SL3.md` (Thm A2 `c_A` floors, Lemma C.1,
Thm SL3.1 tiers, Thm A3(ii) far ingredient), `wave4_sl3p_20260812.md`
(Theorem SL3'), `wave6_s1_plan_20260812.md` (block [B] bootstrap
re-verification).*

**VERDICT: MAJOR_ISSUES.** The `m >= 700` pipeline is numerically sound at
every node I could attack (one non-load-bearing display error), and every
un-refereed analytic claim it introduces — (SOL.12), (SOL.8), (SOL.17),
(SOL.11) — is TRUE with real headroom under adversarial testing. But the
deliverable does NOT discharge (S4) as the campaign consumes it: (S4) is
stated and consumed from `m >= 561`, the draft proves `m >= 700` only, and
its two-sentence discharge of `[561, 699]` is wrong as written (circular —
it mistakes ledger-row closures for CL-level closures). The gap is
repairable in the draft's own architecture (my sizing closes `[561, 699]`
against 0.89 with worst bound `0.689` at 561), but that is a missing proof
segment with new constants, not a text repair. Additionally (SOL.5)'s
quoted support covers only band W1; the W2–W7 case is true and derivable
from citable inputs but the derivation is nowhere in the draft.

## 0. Script table (all SAVED and RUN 2026-08-12; outputs archived)

| # | script (`wave6b_ref_s4/`) | what it checks | key output (verbatim) |
|---|---|---|---|
| [A] | `s4ref_a_recipe.py` (`out_s4ref_a.txt`) | recipe V1–V8 + every displayed constant of SOL.2/3/13/15/16/25/27/30/32/35/36/38–45/49–52; exact Fractions + dps 60 | `[FAIL] E_mid[0] < 0.00071 computed 0.000710590935 (margin -5.91e-7)`; all 37 other checks PASS; `E0 ... computed 0.0239947194`; `H_min ... 0.607176216`; `H_max ... 1.53373475`; `X_max ... 1.54455201`; `max(...) = 0.544552007` |
| [B] | `s4ref_b_kappa3.py` (`out_s4ref_b.txt`) | (SOL.12) `lam\|kappa_3\| <= 2.5 s2`: identities (SOL.9)/(SOL.10) vs `mp.diff`; termwise scan (19 lam x 23 j + refinement); positivity; sum-level at 8 corners | `refined sup rho = 2.130306058` (= `lam coth(lam/2)` at 0.89, the campaign's W7 `r31geo`); `CHECK termwise sup <= 2.5: PASS (headroom 14.79%)`; `any negative kappa_3 term: False`; sum-level worst `2.1285519` |
| [C] | `s4ref_c_remainder.py` (`out_s4ref_c.txt`) | (SOL.8) `\|R(y)\| <= 0.0021 y^4`, `\|alpha\| <= 0.0298`, (SOL.17) direct, (SOL.1) truth `A/m in [0.28, 1]` — exact per-factor `log Phi`, 10 corners x 31 y-points incl. `w = 4.001`, W2/W7 left edges, deep 0.89, m = 561/700/1000 | all corners PASS; worst in-scope `max \|R(y)\|/y^4 = 0.00040743` at (700, deep W7) — 5.15x under cap; `\|alpha\|` worst `0.013868` — 2.15x under cap; `A/m` range observed `[0.298927, 0.93196]` |
| [D] | `s4ref_d_phifacts.py` (`out_s4ref_d.txt`) | truth of the three consumed Phi-facts on adversarial grids; exact coverage chain for (SOL.5) on W2–W7 (`c2*0.64*c_A >= 0.0176`); Cor X.2 cap | all spot grids PASS ((SOL.4) worst `0.379088` vs 0.32; (SOL.5) worst `0.0942649` vs 0.0176; (SOL.6) worst `0.145562` vs 0.0741); chain margins `10.9% / 33.08% / 64.77% / 90.12% / 121.8% / 153.5%` (W2..W7); `W1 ... 0.015615 < 0.0176 -- it needs Lemma R.1` |
| [E] | `s4ref_e_truth.py` (`out_s4ref_e.txt`) | end-to-end truth of `s2(r_m(k)-1)` via the tilted lattice-DFT identity (float64 FFT), machinery validated against exact big-integer `a_m(n)` at m = 30; 8 mean-matched corners incl. the gap range | validation `rel err = 2.21e-16 PASS`; all corners: `s2(r-1)` in `[0.997920, 0.999001]` — inside `(0.607, 1.545)` and `\|.-1\| < 0.545` everywhere, including m = 561/650/699 |
| [F] | `s4ref_f_gap561.py` (`out_s4ref_f.txt`) | REFEREE'S OWN sizing of the `[561, 699]` scope gap in the draft's architecture (`y_max = (2/7) sqrt(0.28 m)`, same cited inputs; R.1 is stated for `m >= 561`) | `worst bound on the gap range: 0.689148 at m = 561 (the gap is repairable-in-kind)`; consistency row `m=700: ... bound 0.39797` |
| [G] | inline (`out_s4ref_g_sol11.txt`) | (SOL.11) hyperbolic inequality on `(0, 0.445]`, 44,500 points | `violations = 0 (PASS)`; endpoint `0.065153029 <= 0.066891411` |

One referee-side bug for the record: the first run of [E] used numpy's
`ifft` (wrong sign convention — support-reversed indices); the built-in
m = 30 exact-integer validation caught it (`rel err = 1.31e-02 FAIL`), the
fix (`fft(P)/L`) validates to `2.21e-16`, and only the fixed run is quoted.

## 1. FINDING N1 (MAJOR — scope): the delivered theorem does not cover the range (S4) is consumed on

- **What (S4) requires** (`CL_composition_20260812.md` §4, verbatim scope):
  "For `m >= 561` and `lam(k)` in-band: `|s2(r(k) - 1) - 1| <= 0.89`."
  Consumption is real from 561: the composed proof (§2 step 1) invokes
  (S4) before Theorem SL4'-R is applied at ANY `m >= 561` — the M2 finding
  says the INFL/QUADF factors "price every ledger entry" at
  `Theta = 20/m`, and its `G`-contractions were computed at the thinnest
  rows `m = 401` (W5) and `m = 463` (W1); `wave6_s1_plan_20260812.md`
  block [B] re-verifies the bootstrap AT `m = 561` rows ("W5 @ 561:
  G(20/m) margin 4.745%; x_seed = 0.92147"). Nothing in the ledger
  restricts the seed's consumption to `m >= 700`.
- **What the draft delivers:** Theorem SOL.6 for `m >= 700` only.
- **The draft's `[561, 699]` discharge is wrong as written.** It asserts
  "the already closed W1 finite rung gives the stronger CL estimate
  `|s2(r_m(k)-1)-1| <= 20/m`" and "W2–W7 are likewise already closed by
  their certified rows". Fact R.G / the M3 per-cell construction close
  LEDGER ROW bounds (inputs to SL4'-R's share criterion) — and those very
  rows are priced by the INFL/QUADF bootstrap whose closure needs the
  seed. Reading them as CL-level closures of `[561, 699]` is exactly the
  circularity the draft's own WHAT-REMAINS item 2 concedes would be fatal
  ("If that closure were interpreted as itself conditional on (S4), it
  could not be used circularly"). The M3 note removes SL4'-X from
  `[561, 699]`, not the seed. So the premise the draft leans on does not
  exist in the record, and (S4) on `[561, 699]` is NOT discharged.
- **Repairability, quantified (script [F], referee's own — NOT a
  certified lemma):** the draft's architecture ports to `[561, 699]` with
  the single modification `y_max = (2/7) sqrt(0.28 m)` (preserving the
  (SOL.14) Taylor domain `|t|/lam <= 2/7`), using only inputs the draft
  already cites (Lemma R.1's floor is stated for `m >= 561`; SL3' and
  A3(ii) hold from 401). Result: closes against 0.89 at every probe,
  worst `|s2(r-1)-1| < 0.689148` at `m = 561` (E2 there `0.2033`,
  `H in (0.45276, 1.6749)`). Truth is corroborative on the gap range
  (script [E]: `s2(r-1) = 0.997920 .. 0.998571` at 561/650/699). So the
  gap is repairable-in-kind — but it is a missing proof segment with its
  own constants and verification, not a wording fix. Note the repaired
  seed constant on `[561, 699]` would be ~0.69, still inside every
  recorded basin (0.89412 composition / 0.92147 wave6 plan).

## 2. The `m >= 700` pipeline: every displayed number re-verified (script [A])

All of V1–V8 and every constant in SOL.2/3/13/15/16/25/27/30/32/35/36/
38–45/49–52 were recomputed (exact Fractions for V1, the (SOL.15/16)
coefficient `876/588000 = 73/49000 = 0.00148980`, and the monotonicity
log-derivative checks; dps-60 for erfc/moment integrals). 37 of 38 checks
PASS as displayed, including the tight ones:

- `H_min = 0.607176216 > 0.607`; `H_max = 1.53373475 < 1.535`;
  `X_max = 1.54455201 < 1.545`; final `0.544552007 < 0.545 < 0.89`.
- True totals `E0 = 0.0239947 < 0.02401`, `E1 = 0.0481915 < 0.04820`,
  `E2 = 0.1191228 < 0.11916` — the displayed totals are honest caps.

**FINDING N3 (MINOR — display, recipe-visible):** `E_mid[0]`'s true value
is `0.000710590935`, EXCEEDING the draft's displayed cap `0.00071` by
`5.91e-7` — an inward rounding that violates the draft's own
"outward-rounded rationals" instruction, and the recipe's V3 expected-check
fails as scripted. Non-load-bearing: `E_loc[0]`'s display slack
(`+6.17e-6`) absorbs it, so the displayed total `E0 < 0.02401` remains a
true outward bound and nothing downstream moves. Repair: print `0.000711`.

**FINDING N4 (record — fragile displays):** two further margins are
razor-thin but valid at dps 60: `E_loc[1] < 0.04482` by `2.87e-8`, and
`E_cross[0] < 1.04e-5` by `1.05e-7`. Do not sharpen casually.

## 3. Adversarial checks the recipe omits — all TRUE (scripts [B], [C], [D], [E], [G])

The draft's recipe only re-runs its own arithmetic (friendly points); it
never tests the two new analytic claims, the three consumed Phi-facts, or
any actual `r_m(k)`. That omission is itself a finding (**N5**, record):
V1–V8 would pass even if (SOL.12) or (SOL.5)-on-W7 were false. I supplied
the missing checks; the draft SURVIVES all of them:

1. **(SOL.12)** `lam|kappa_3| <= 2.5 s2`: identities (SOL.9)/(SOL.10)
   match `mp.diff` to `< 1e-25`; every term `kappa_{3,j} >= 0`; termwise
   sup `= 2.130306` (attained in the `j -> inf` limit at `lam = 0.89` —
   exactly the campaign's `r31geo(0.89) = 2.13031`, a strong consistency
   anchor); sum-level worst `2.1285519`. Headroom under 2.5: **14.79%**.
2. **(SOL.8)/(SOL.17)/alpha-cap/(SOL.1)**: at 10 corners x 31 y-points
   (including `w = 4.001` where `A/m = 0.298927` sits closest to the 0.28
   floor, both W2/W7 left edges, and the deep corner): worst
   `|R(y)|/y^4 = 4.07e-4` in scope (cap 0.0021, 5.15x); worst
   `|alpha| = 0.013868` (cap 0.0298, 2.15x); (SOL.17) holds pointwise
   everywhere; `A/m` observed within `[0.28, 1]` at every corner.
3. **The three consumed Phi-facts** hold in truth on adversarial grids
   (six (m, w) cases x 25–41 t-points each): worst
   `-log|Phi|/(s2 t^2) = 0.379088 >= 0.32` on the mid arc; worst
   `-log|Phi|/m = 0.0942649 >= 0.0176` on the crossover; worst
   `0.145562 >= 0.0741` on the far arc; `t0(0.89)/0.89 = 1.07372378`
   re-confirmed against Cor X.2's cap.
4. **End-to-end truth**: via the tilted-DFT identity (machinery validated
   to `2.21e-16` against exact integer `a_m(n)` at m = 30 — which also
   verifies (SOL.0) tilt-invariance exactly), all 8 mean-matched corners
   give `s2(r-1) in [0.997920, 0.999001]` — deep inside the theorem's
   `(0.607, 1.545)`.
5. **(SOL.11)**: 44,500-point grid on `(0, 0.445]`, 0 violations.

## 4. FINDING N2 (MODERATE — citation support for (SOL.5) on W2–W7)

The draft supports (SOL.5) (`|Phi| <= e^{-0.0176 m}` on the crossover) by
"[W.6] together with Lemma R.1". Lemma R.1's certificate is stated ONLY
for `w in (4, 5]` (`wave4_sl4p_repaired_20260812.md` §5.3: "For all
`m >= 561`, `w in (4, 5]`, `tau in [0.8, 1.074]`"), i.e. band W1. The
draft's Theorem SOL.6 ranges over ALL `lam in (4/m, 0.89]`, so bands
W2–W7 consume (SOL.5) with NO support written in the draft. The
inequality IS derivable from citable inputs — Thm SL3.1(i') (tier-2,
`c2 = 0.0871362`, valid to `1.074 lam`, no lam floor) + Thm A2(ii)'s
`c_A` floors give, in exact arithmetic (script [D] block [1]):
`c2 * 0.64 * c_A(W) = 0.0195185 / 0.0234222 / 0.0289989 / 0.0334603 /
0.039037 / 0.0446137 >= 0.0176` for W2..W7 (worst margin **10.9%** at
W2), while W1 genuinely needs R.1 (`0.015615 < 0.0176`). Repair: one
written paragraph adding this chain (or an equivalent) with the W2 margin
stated; until then (SOL.5) as cited covers only W1. The maths referee
should also make the draft name its sources for (SOL.4) (= Theorem SL3',
whose min band exponent is `gamma*(W7) = 0.32`) and (SOL.6) (= Theorem
A3(ii)'s P3 far ingredient) instead of "already established estimates".

## 5. Findings register

| # | severity | finding | load-bearing? | repair |
|---|---|---|---|---|
| N1 | **MAJOR** | scope gap: proves `m >= 700`; (S4) consumed from `m >= 561`; the `[561, 699]` discharge paragraph is circular/wrong | YES — (S4) not discharged as stated | new proof segment on `[561, 699]` (referee sizing: architecture closes there, worst 0.689 at 561, script [F]) |
| N2 | MODERATE | (SOL.5) support covers W1 only; W2–W7 chain (tier-2 + `c_A`, worst margin 10.9%) not written | YES for the citation graph; the inequality itself is true and derivable | add the one-paragraph W2–W7 derivation; name SL3'/A3(ii) for (SOL.4)/(SOL.6) |
| N3 | MINOR | `E_mid[0]` displayed `0.00071` < true `0.000710591` (inward rounding; recipe V3 fails as scripted) | no (absorbed by `E_loc[0]` slack; totals honest) | display `0.000711` |
| N4 | record | fragile display margins: `E_loc[1]` (+2.87e-8), `E_cross[0]` (+1.05e-7) | no | do-not-sharpen note |
| N5 | record | recipe checks only the draft's own arithmetic; no test of (SOL.12)/(SOL.8)/Phi-facts/truth, no domain-corner probes | — | referee scripts [B]–[E] supply them; all pass |
| N6 | record (positive) | (SOL.12) true, 14.8% headroom, termwise sup = `r31geo(0.89)`; (SOL.8) true, 5.15x; (SOL.0) verified exactly; truth `s2(r-1) ~ 0.998` at all corners incl. gap range | — | — |
| N7 | record (interface) | delivered constant 0.545 sits inside every recorded seed basin (0.89412 composition; 0.92147 wave6-plan re-verification); commissioning note's "basin 0.920" traces to the wave6 plan's 561-row re-verification, the composition's own figures are 0.90182/0.89412 | — | — |

## 6. Verdict and what would change it

**MAJOR_ISSUES.** Not FATAL: no false load-bearing numeric anywhere in the
proved `m >= 700` range, all new analytic claims survived adversarial
attack with real headroom, truth corroborates on the full `m >= 561`
range, and both genuine gaps (N1, N2) are repairable inside the draft's
own architecture with margins quantified here. Not MINOR_REPAIRS: as
submitted, the deliverable does not prove the statement the campaign
consumes — `[561, 699]` (139 integer values of `m` on which the M2
bootstrap demonstrably runs) is uncovered, and its claimed discharge is
circular; plus a band-coverage hole in (SOL.5)'s support. Upgrade path to
MINOR_REPAIRS/citable: (i) add the `[561, 699]` segment (script [F]'s
`y_max = (2/7) sqrt(0.28 m)` variant, with its own outward-rounded budget
table — expect a seed constant ~0.69 there); (ii) write the W2–W7
crossover chain of §4 and name SL3'/A3(ii); (iii) fix N3's display. All
three are within one revision's reach; none is done in the submitted text.
The maths referee should additionally rule on Lemma SOL.2's proof
SKETCH for (SOL.14)/(SOL.15) ("the same termwise calculation applied from
order four onwards") — numerically its conclusion is true with 5x slack,
but as written it is a sketch, not a proof.

*End of referee_numerics_sol_s4.md.*
