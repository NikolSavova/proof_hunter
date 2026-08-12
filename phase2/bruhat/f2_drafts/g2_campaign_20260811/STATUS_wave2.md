# STATUS_wave2 — G2 closure campaign, wave-2 synthesis (2026-08-11/12)

*Synthesis editor pass, wave 2 (read-everything role; blind protocol lifted
for this file only). Sources: every file under `g2_campaign_20260811/` —
wave-1 drafts `wp1_draft_c.md` / `wp2_draft_b.md` and their four referee
reports, wave-2 drafts `wp2_draft_a2.md` / `wp3_draft_a2.md` and their four
referee reports, `referee_t2_maths.md`, `referee_t2_numerics.md`,
`repairs_20260811.md` + `referee_repairs_20260811.md`,
`harness_m200_20260811.md`, `CAMPAIGN_NOTES.md`, wave-1 `STATUS.md` — plus
the four standing context documents (`F2_PROOF_DRAFT.md`, `g1_draft_b.md`,
`g2_draft_t2_20260803.md`, the diagnostic notes). `g2_draft_t1_20260803.md`
remains unread by every wave-2 agent and by this editor. No existing file
modified; this file is new (no-erasing rule). House rules applied: an item
is CLOSED only if the draft(s) closing it hold SURVIVES or MINOR_REPAIRS
from BOTH referees; MINOR_REPAIRS = closed-modulo-listed-repairs, and every
NEW repair list is copied in below (§2a–§2c). Synthesis-level numeric claims
new to this file come from the saved, run script
`g2_scripts/campaign_20260811/status_wave2/status_wave2_checks.py`
(output archived as `out_status_wave2_checks.txt` beside it).*

**Executive summary.** Wave 2 closed T2 §8 item 4 (wp2-a2: the `Delta_ker`
bucket + the T.9-final merge ⇒ Prop 3.5(ii) closed modulo repairs) and item
2 (wp3-a2: pentagonal extension + gap-free stitch), discharged the T2
house-rule debt (maths referee landed: MINOR_REPAIRS; two PROVED stamps —
T.10(2), T.8'' — require supplied repairs), verified all wave-1 repairs
applied (SURVIVES), and extended the exact harness to `m = 400`. **Exactly
one open mathematical statement now separates the campaign from Theorem A =
F2(a): the deep-tilt core lemma at spec `CL(79, 20, 0.89)` (wp4).** Details
and no-inflation accounting below.

## 1. Wave-2 verdict table

Wave 2 delivered everything wave-1 STATUS §5 asked for except the wp4 core
model (deliberately deferred there to "only then"). Every wave-2 package that
required two referees got two; both passed.

| Package | Deliverable | Draft self-reported status | Maths referee | Numerics referee |
|---|---|---|---|---|
| **wp2-a2** `wp2_draft_a2.md` | The never-landed wp2-a: `Delta_ker` bounded in closed form (Theorem D.5: `C_ker(1/2/4) = 30.89 / 209.03 / 37811` at `m >= M(K) = 180/181/367`); the odd-cube bucket-placement trap found and fixed (real/imaginary split, Lemma D.1'); the merge Theorem T.9-final (`C_R(K)` explicit, Lin conditionality discharged, coverage gap-free vs harness-400) | item 4 CLOSED (with wp2-b) modulo referee; Prop 3.5(ii) closed modulo referee + inherited grid-cert flags; 3.5(i) untouched | **MINOR_REPAIRS** (`referee_maths_wp2_a2.md`: every load-bearing claim survives; independent re-assembly of all constants to <3e-6; the D.1' split stress-tested at 200k points, max ratio 0.9996; repairs F1–F5, all text-level) | **MINOR_REPAIRS** (`referee_numerics_wp2_a2.md`: all 6 scripts reproduce verbatim; independent dps-60 rebuild to 1e-15; monotonicity survives off-grid attack to m = 10^6; independent ground truth reproduces; repairs R-F1–R-F7, prose/table-level) |
| **wp3-a2** `wp3_draft_a2.md` | The never-landed wp3-a: pentagonal region extended to `k = Theta(m)` (Theorem P.5, thresholds 30/83/300/1581); linear `C_0` arithmetic (P.6); all-`w` deficit floor (P.7); tilt cap `lam(k) <= log(1+1/c)` (P.8); Theorem S gap-free stitching table with the crude law as a named parameter `CL(79, 20, 0.89)` | item 2 CLOSED in its original arithmetic form; deep-tilt core isolated, capped, and spec'd (NOT closed); Theorem S = PROVED AS A REDUCTION with exactly two named conditions (wp4's CL; wp2-a's `C_ker`) | **MINOR_REPAIRS** (`referee_maths_wp3_a2.md`: P.1–P.8/P.5/Theorem S all verified, partition gap-free, no circularity; repairs R1–R8; R1 = rescope P.7 to `\|w\| <= 8`, R2 = four unsafe E-decimals, R3 = wrong unscripted "~68" -> 82) | **MINOR_REPAIRS** (`referee_numerics_wp3_a2.md`: all 4 scripts reproduce; P.5 truth extended off-grid to m = 400 (0 violations); stitch arithmetic re-done exact; repairs F1–F8; F1 = same unsafe-rounding class as maths R2; F3 = Lin double-count, safe direction) |
| **T2 maths referee** `referee_t2_maths.md` (on `g2_draft_t2_20260803.md`) | The missing house-rule half (wave-1 STATUS §3 debt) | (T2's own §8 statuses) | **MINOR_REPAIRS**: T.1–T.7c, (T.8a), T.9'' all survive hand re-derivation (T.5 "CORRECT, fully"; T.9'' "fully verified"); **T.10(2) FALSE as displayed** (M1; repair `rho = 1 - 0.022 w_0^2` supplied + verified); **T.8'' proof BROKEN, statement true** (M2; one-line memorylessness repair supplied; `-1` -> `-2`); F9 discharged (M6); no circularity, no untracked small-tilt assumption | (numerics half = `referee_t2_numerics.md`, wave 1, MINOR_REPAIRS — see §3) |
| **Repairs session** `repairs_20260811.md` | Wave-1 STATUS §2a (A1–A5), §2b (B1–B8), §3 (T1–T9 = T2-numerics F1–F9) all applied as errata + fixed script copies; T2-F1 closed by new Lemma T.9-Step2' (`\|B_lam/B_m - 1\| <= 0.362 w^2` on `\|w\| <= 1`, `m >= 30`; `0.362 + 0.09 = 0.452 < 0.5` so T.9 Step 2's `c_w = 1/2` sub-claim closes) | all discharged; no certified digit moved (§D verified) | — (single verifier role) | **SURVIVES** (`referee_repairs_20260811.md`: every script re-run byte-identical vs archived outputs; T.9-Step2' chain verified end to end incl. hand-checked exact rationals; no-erasing rule verified; 3 non-blocking observations O1–O3) |
| **Harness extension** `harness_m200_20260811.md` | Exact harness `4 <= m <= 400` (target was 200; 320.9 s): C1–C6 all PASS, 397 rows, 0 failures — argmin central, min = central ratio, `varfit >= 187/216` (equality only m = 6), strict increase | PROVED (exact finite computation) | — (exact-arithmetic deliverable; consumed and independently spot-verified by three wave-2 referees, incl. the results file on disk) | — |

Under the house rule: **wp2-a2 and wp3-a2 are both citable modulo their §2a/§2b
repair lists below**; the repairs doc is citable outright (SURVIVES); the T2
draft now has BOTH referee halves (see §3).

## 2. Full updated G2 ledger, both waves (T2 §8 items 1–5; Prop 3.5(i)/(ii))

### Item 1 — T.8 far region / deep tilt. **PARTIALLY CLOSED** (unchanged verdict, sharper residue).
- *Far-region half: CLOSED* (wave 1, wp1-c W.3–W.6, both referees
  MINOR_REPAIRS, repair list §2a of STATUS.md now DISCHARGED by
  `repairs_20260811.md` §A + `referee_repairs_20260811.md` SURVIVES).
  Explicit far bound on `t in [t_0(lam), pi]` for `\|lam\| <= 1.7627`, floor
  `exp(-0.0372 m)`, crossover clause W.6. Pointers: `wp1_draft_c.md` §5–§6;
  restated case-wise W.5(iii') in `repairs_20260811.md` §A3.
- *Deep-tilt CORE model: still OPEN — but transformed.* wp3-a2 caps the tilt
  on the residual band (`lam(k) <= log(1+1/c) <= 0.89` at the operating
  point, Lemma P.8) and turns the need into the quantified spec
  `CL(C_0* = 79, C* = 20, Lambda* = 0.89)` for `m >= 401`, lower-bound form
  sufficing (`wp3_draft_a2.md` §6.1; both its referees verified the spec
  arithmetic). All decay bounds the core lemma needs are already proved
  (wp1-c W.5(ii)/W.6 + T2's (T.6ii), the latter now two-referee); measured
  truth margin at the spec point is 6.7x (NC-P3d, referee-reproduced).
  The identified route is unchanged: cumulant model with radius `~ c·lam`
  from strip analyticity. **This is the ONLY open mathematics left for
  Theorem A** (see §4). T.8's own `C = 600` bucket assembly is now MOOT for
  Theorem A: Theorem S uses T.8/T.8-final NOWHERE (verified by its maths
  referee, §1.9).

### Item 2 — Region-2 handoff arithmetic (`C_0 = 2000` mismatch). **CLOSED (modulo §2b repairs).**
Closed by wp3-a2 (both referees MINOR_REPAIRS). Theorem P.5 extends region 1
from `k ~ sqrt(m)/4` to `k = c·m` (`c` up to 1; thresholds
`m_p = 30/83/300/1581`; exact-harness truth check 0 violations to m = 400
including the referee's off-grid extension); Lemma P.6 then gives
`s2 >= c(1+c)m/6` on the residual band — the `C_0` arithmetic is LINEAR, not
quadratic (`m >= 6000` even at `C_0 = 2000` intact, vs the old `2.3e9`), and
Theorem S's stitch uses neither `C_0 = 2000` nor `C = 600` anywhere. What
item 2 concealed — that the residual band's tilts are constants, so the crude
law there needs the deep-tilt core — is isolated into item 1's residue (the
CL spec), not left diffuse. Pointers: `wp3_draft_a2.md` §1–§5;
`referee_maths_wp3_a2.md` §1.9 (partition verified gap-free);
`referee_numerics_wp3_a2.md` §2.5 (stitch arithmetic exact).

### Item 3 — Finite certificates ((T.7b-cert)/(T.7c-cert)). **CLOSED** (wave 1, unchanged).
wp1-c supersession + `referee_t2_numerics.md` §3 proof-grade upgrades; the
one-line `tan x > tanh x` proof demanded by repair R4/A4 is now recorded and
certified (`repairs_20260811.md` §A4), so wp1-c's "no grid certificates
anywhere" claim is true. The T2 maths referee re-confirmed both cert chains
analytically (§2.8–2.9).

### Item 4 — T.9's mechanical bucket table / explicit `C_R(K)`. **CLOSED (modulo §2a repairs + flagged grid-certificate inputs).**
The missing `Delta_ker` bucket landed (wp2-a2 Theorem D.5, both referees
MINOR_REPAIRS): `|Delta_ker| <= C_ker(K)/m^2`, `C_ker = 30.89 / 209.03 /
37811` for `m >= 180/181/367`, built as box (real-part split) + far (wp1-c
W.4(i)) + model tail + denominator buckets; truth anchors 1.39/4.07/5.04
independently reproduced; the crude modulus route's failure (`K^3 sqrt(m)`
growth from the bare `alpha^3 t^9` row) documented and provably avoided via
the real/imaginary split — both referees confirm the split is sound and
essentially sharp. Merge done: **Theorem T.9-final** (`wp2_draft_a2.md` §7)
= W.7 + D.5 + repaired W.6 envelope, `C_R(K) = 41.17 / 230.09 / 37998`
(closed flavor; grid flavor 32.44 / 213.12 / 37815), `c_w = (0.407, 0.466,
1)`, W.5's conditionality discharged (`H(K, M(K)) <= 0.34 <= 1/2`), no proxy
criterion anywhere. Carried flags (honest, propagate into any consumer):
wp2-b's `c_4 = 0.60` floor and `c_w` envelope and PW grid flavor are
grid-certified (repairs B2/B3/B4); wp2-a2's own constant-flavor monotonicity
beyond `m = 3000` is grid-class (referee extended it to `m = 10^6`, no
violation). Pointers: `wp2_draft_a2.md` §6–§7; `wp2_draft_b.md` §2–§6;
`repairs_20260811.md` §B.

### Item 5 — Binding far exponent / `m_2(K)` thresholds. **CLOSED** (wave 1) — and both wave-1 caveats now DISCHARGED.
`c_1(1/2/4) = 0.2259 / 0.1802 / 0.1019` stand (repairs §A1 re-certifies all
13 constants, min margin 9.1e-6, all safe-direction). The two caveats wave-1
STATUS carried: (a) *bands 151..189/266/378 need the harness extension* —
DONE, exact to m = 400 (`harness_m200_20260811.md`); (b) *the `m_2(K)`
proxy-criterion numbers must be replaced by real assembly thresholds* —
DONE at `K <= 4` for Prop 3.5(ii): Theorem T.9-final's actual thresholds are
`M(K) = 180/181/367 <= 400`, derived from its own prefactors with no proxy
(wp2-a2 §6; its maths referee §1.6 confirms the coverage argument). No
uncovered `m` remains for any `K <= 4`.

### Prop 3.5(ii) — the refined small-tilt law [T.9]. **CLOSED (modulo listed repairs + flagged grid-certificate inputs).**
Constituted by: wp2-b Theorem W.7 (exact decomposition) + Prop W.6 envelope
(repaired: grid-certified, `c_w(4) = 1`) + Lemma W.4 + wp2-a2 Theorem D.5 +
wp1-c W.4(i) + T2's T.9''/(T.8a)/T.1(ii) (now two-referee) + g1_draft_b
B.0(ii) ⇒ **Theorem T.9-final** (`wp2_draft_a2.md` §7): for `m >= M(K)`,
`0 < |lam(k)| <= K/m`, `s2 log r(k) = 1 - B_m(1 + theta_1 c_w(K) w^2) +
theta_2 C_R(K)/m^2`, plus the `(r-1)` form with `Lin(K)`. Every `m >= 4` is
covered by the exact harness (`m <= 400`) or the analytic law
(`m >= M(K) <= 400`), with overlap. Both wave-2 referees of wp2-a2 endorse
exactly this closure claim at exactly this status. The exact center
`lam = 0` (N even) sits formally outside the `0 < |lam|` hypothesis — covered
by g1_draft_b B.8/Cor B.9 (wp3-a2 maths referee R4's one-line note).

### Prop 3.5(i) — the crude uniform law [T.8]. **PARTIALLY CLOSED (reduced to one lemma).**
Theorem S (wp3-a2, both referees MINOR_REPAIRS) proves: for `m >= 401` the
interior splits R1a/R1b/R2/R3 gap-free; R1a/R1b unconditional (P.5 + Lemma
3.6); R3 needs only Prop 3.5(ii)-machinery at `K = 4` (now closed, see the
plug note below); **R2 is conditional on exactly `CL(79, 20, 0.89)` — the
deep-tilt core lemma, the single open piece.** For `m <= 400` everything is
exact (harness). Prop 3.5(i) in its ORIGINAL full generality (`all
sigma_lam^2 >= C_0`) is not needed for Theorem A in this architecture; what
remains open is the CL spec instance.

**The cross-package plug (new, synthesis-level — checked here, not yet
refereed as a unit).** wp2-a2 and wp3-a2 were blind to each other; Theorem S
names "wp2-a's `C_ker`" as its R3 condition, and wp2-a2 supplies exactly
that object (`C_ker(4) = 37810.05`, valid `m >= M(4) = 367 <= 401`, scope
`|w| <= 4` = R3's band, `w`-uniform). Script check
(`status_wave2_checks.py`, run 2026-08-12, output archived):
`M(4) = 367 <= 401` TRUE; plugged R3 line at `m = 401`:
`1 - B_401 - (5.32 + 37810.04)/401^2 = 0.762141 > 0` (closed flavor
0.761006), increasing to 1. **Theorem S's R3 condition is therefore MET; its
only remaining condition is wp4's CL.** Caveat for G4 (NOT for F2(a)): with
the crude `C_ker(4)`, the plugged part-(c) bound first reaches `187/216` at
`m* = 535` (grid flavor; 537 closed) — leaving a band `[401, 534]` above the
harness's 400 that part (c) would need covered by either a harness run to
`~540` (minutes at the measured `~m^3` scaling) or the flagged mechanical
`C_ker(4)` sharpenings (wp2-a2 §10 item 3). Theorem A = F2(a) is unaffected:
its `O(m^{-2})` error term absorbs any fixed constant.

### §2a. wp2-a2 repair list (union of both referees; none touches a constant, lemma, threshold, or verdict)

From `referee_maths_wp2_a2.md` §4:
1. (F1 maths / R-F1 numerics — the shared substantive one) §0 item 1
   misdescribes the monotonicity-certificate grid as "unit-step to 3000":
   the shipped scan is unit-step to 1000, step 10 on (1000, 3000],
   endpoints-only beyond (§6/§10 state it correctly). Reword §0 to match —
   or cite the numerics referee's R1, which HAS now verified unit-step
   [1000, 3000], step-20 [3000, 10^4], and decrease through `m = 10^6`.
2. (F2) The D.5 scope-note's exponent-0 row classification is incomplete:
   besides the `ZI^4`-class add the `ZR·ZI^2`-against-constant class and
   WI's `A3^3` via the pointwise `|t|`-shift (referee's §2.3 re-audit
   confirms the conclusion — no positive row — but the parenthetical is the
   target list for the promised Sturm upgrade and must be right).
3. (F3) Add the one-sentence certification-status note for `LFlow > 0`
   (same grid class as the monotone-decrease certificate; worst 0.92237).
4. (F4) Sign typo in D.4(ii): `phat(+-1) = Z(+-h) P(+-h)` (not `-+`).
5. (F5) Trivia: NC-A6 into both script lists; the (60, 4) `inf` clause in
   NC-A4(2); NC-A3(1) grid wording; split the §6 mixed-m table rows; move
   the ground-truth-vs-analytic-law coverage caveat up to §0 item 4.

From `referee_numerics_wp2_a2.md` §4 (beyond the shared R-F1):
6. (R-F2) Theorem D.5's per-piece table rows `181 2` / `367 4` silently mix
   m-values in the tail/den columns; print genuine full rows at 181/367 or
   extend the parentheticals.
7. (R-F3) "1.374–1.386 over m = 30..140" -> "1.374–1.391" (wp2-b's table
   has 1.391 at m = 100, K = 1).
8. (R-F4) §7's aside "moves the crossover only to m ~ 27" is un-scripted;
   add the two-line solve to a script or soften.
9. (R-F5) One sentence documenting why the wp2a2 port's `P0_min` differs
   from wp2-b's (valid, sharper h-term-free floor at y = 0 — verified, not
   a bug).
10. (R-F6) "LFlow >= 0.9224" is an unsafe rounding of a non-theorem point;
    restate ">= 0.9223" or quote 0.96388 (the min over theorem-used pairs).
11. (R-F7, optional) Assert the Newton residual in NC-A4's `lam_solve` on
    any future re-run.

### §2b. wp3-a2 repair list (union of both referees; no constant, threshold, region boundary, or conditional moves)

From `referee_maths_wp3_a2.md` §4 (R1–R8) and `referee_numerics_wp3_a2.md`
§3 (F1–F8); overlapping items merged:
1. (R1 maths — the only mathematical-content item) Rescope Lemma P.7
   clause 1 to `|w| <= 8` (or add `48 E(w) m^4 >= 1000`): as displayed the
   proof does not deliver 6.85 for arbitrarily large `|w|` at fixed m.
   Everything consumed lives at `w0 <= 6`.
2. (R2 maths = F1 numerics — wave-1-R1 class) Four of six "certified lower
   decimals" for `E(w0)` are round-to-NEAREST, not down: reprint
   `E(1) >= 0.00400692`, `E(2) >= 0.00358718`, `E(3) >= 0.00304035`,
   `E(6) >= 0.00161240` (E(4), E(5) safe as printed) and propagate:
   `deficit(4) >= 0.27289`, `rho(4) <= 0.72711` (the P.7 box, §0, and
   Theorem S's operating point), `deficit(2) >= 0.0982`, R2-row value
   `>= 1.0292`, note-2's `>= 0.01627`. All downstream inequalities re-close
   (both referees re-ran the chain: 1.02928–1.029462 >= 1.02).
3. (R3 maths = F4 numerics) Derivation note 2's unscripted "~68" is wrong;
   the exact bracket crossover is `m = 82`. The consumed claims ("valid
   m >= 100"; positivity at 401) are true.
4. (F2 numerics) The E-series truncation claim "< 2e-21" is false by ~4
   orders; restate "< 2e-15 (float-summation dominated)". Nothing moves.
5. (F3 numerics = R8-part maths) Theorem S's R3 line double-counts `Lin`
   (wp2-b's `C_R^PT` already contains it) — safe direction; write
   `[C_R^PT(4) + C_ker]/m^2` or spell out `[PW + T + Lin + C_ker]/m^2`.
6. (R4 maths) `N` even, `k = N/2` has `lam = 0`, formally outside W.7's
   hypothesis; add the one-line note (covered by B.8/Cor B.9 or W.7's
   untilted limit).
7. (R5 maths) "eps <= 0.0385 over EVERY interior k" — the scan is
   `2 <= k <= N/2`; say so (the numerics referee independently confirmed
   the full-interior claim is in fact true at m = 30/60/140).
8. (R6 maths) Mirror §6.3's `m_2(4)`-proxy qualifier inside Theorem S's
   statement. [Synthesis note: substantively discharged by the wp2-a2
   merge, whose real threshold M(4) = 367 replaces the proxy — but the
   text repair still applies to wp3-a2 as written.]
9. (R7 maths) P.4(iii) uses the P.3(ii) floor at `j = 1` when `k = 2`;
   add "trivially `Phi(1) = 1 - 1/m`".
10. (R8 maths + F5/F6/F7 numerics) Display trivia: NC-P4's `0.6931` cap
    print (round-down of log 2 — wrong direction; text's 0.6932 correct);
    "17364x" -> 17363x; §7's "verbatim excerpts" are condensed and contain
    one editorial line inside a code block — relabel or add the print to
    the script; §2 constants table is nearest-rounded displays of exact
    Fractions (one sentence; note the omitted `sigma_1'` tail ~1e-118,
    certified harmless); (F8, observation) "82–90% capture" is w0 <= 4
    scoped.

### §2c. T2 maths-referee repair list (consolidated `referee_t2_maths.md` §5; NOT yet applied — the pending `t2_repairs` file)

Items 1–4 have mathematical content; 5–8 are display-level. All replacement
proofs/constants are already supplied and script-verified inside the report.
1. **T.10(2)**: replace `rho := 1 - 0.04 w_0^2` by `rho := 1 - 0.022 w_0^2`
   with the verified two-inclusion form (M1); correct `0.0332 -> 0.0347`
   in both places (M5); fix the undefined `m_0(i)` header (M7).
2. **T.10(1)/§8-6**: band label `[1/m, 3.7/m] -> [1/m, pi/m]`, or close the
   `(pi/m, 3.7/m]` sliver by citing wp2-b W.1(i) (M3).
3. **T.8''**: replace the `E U^2` route by the memorylessness mixture
   identity (M2, one line, supplied); conclusion `-1 -> -2`.
4. **T.9 §5 "fully proved" list**: the `B_lam/B_m` line — already replaced
   by Lemma T.9-Step2' in `repairs_20260811.md` §T1; M8's caveat: the
   corrected inequality must carry `d <= 0.1` (the repairs doc's version
   uses `d <= 0.033` — compliant; verified SURVIVES).
5. **T.4'**: `1.18 -> 1.178` (or `/155 -> /154`) (M4); note the `/284`
   margin 2.2e-4.
6. **(T.4a'')**: lower coefficient `/25 -> /19`; strike the two false-start
   paragraphs; fix the `[.., 0.0332]` prose line (M5).
7. **(T.6iii-final)**: transcribe the referee's five-line constant chase
   (§2.7) — retires numerics F9.
8. Apply numerics F2/F5/F6/F7/F8 where they touch mathematics — already
   done in `repairs_20260811.md` §C (verified); fold at paper-assembly.

## 3. T2 house-rule status

**The house-rule debt is DISCHARGED: both referee halves now exist.**
`referee_t2_numerics.md` (wave 1, MINOR_REPAIRS; its F1–F9 repairs are
APPLIED in `repairs_20260811.md` §C and verified SURVIVES) +
`referee_t2_maths.md` (wave 2, MINOR_REPAIRS). Net status of the T2 PROVED
inventory:

- **T.1, T.2, T.3, T.4, T.4', T.5, T.6(i)(ii)(iii-final), T.7b-final, T.7c,
  (T.8a), T.9''**: stand at MINOR_REPAIRS from both referees — citable, and
  every wave-1/wave-2 citation of them is now on two-referee footing (both
  wave-2 drafts and all four wave-2 referees verified this per item at each
  use).
- **T.10**: "PROVED modulo M1/M3 repairs" — clause (2) must be restated with
  `rho = 1 - 0.022 w_0^2` (the displayed form is FALSE). Consumed nowhere in
  the campaign chain (verified by both wave-2 maths referees); wp3-a2's P.7
  independently supplies the stronger `1 - 0.0274 w_0^2` at `w_0 = 1`.
- **T.8''**: "PROVED modulo M2 repair" (statement true, displayed proof
  broken; one-line memorylessness rescue supplied, `-1 -> -2`). Consumed
  nowhere in the campaign chain.
- **T.8, T.9**: remain PARTIAL as self-reported — but see §2: T.9's residue
  is now Theorem T.9-final (closed modulo repairs), and T.8's residue is
  reduced to the CL spec.

**Remaining T2 bookkeeping**: apply §2c above to a new `t2_repairs_2026xxxx`
file (the maths referee's M-items; the numerics F-items are already applied).
Until then, T.10(2) and T.8'' specifically must not be cited as displayed —
nothing currently cites them.

## 4. Bottom line: is Theorem A = F2(a) fully proved?

**NO — but exactly ONE mathematical statement now stands between here and
Theorem A**, down from four at wave-1 STATUS §4. Everything else is applied
repairs, one assembly write-up, and referees for that write-up.

**What remains, smallest first:**

1. **Apply the wave-2 repair lists** (§2a, §2b, §2c above) to new files,
   mirroring `repairs_20260811.md`. Text/label/rounding-level throughout;
   the only items with mathematical content are wp3-a2's P.7 rescope
   (`|w| <= 8` — the draft never uses more) and the T2 M1/M2 restatements
   (replacement proofs already supplied and script-verified in
   `referee_t2_maths.md`). Half a session.
2. **wp4 — the deep-tilt core model lemma**, delivering
   `CL(C_0* = 79, C* = 20, Lambda* = 0.89)` for `m >= 401` (lower-bound
   form suffices). **This is the last genuinely open mathematics in G2.**
   The spec, its feasibility margins (6.7x measured), the tilt cap that
   bounds its scope (`4/m < lam <= 0.89`, all inside proved far-bound
   coverage), and the identified strip-analyticity route are in
   `wp3_draft_a2.md` §6.1; the constant-lam regime analysis in wp1-c §9
   item 2. Then two referees on it (house rule).
3. **Theorem A assembly session**: Theorem S's table (`wp3_draft_a2.md` §5)
   + the plug of Theorem T.9-final/`C_ker(4)` into R3 (checked here,
   §2 plug note — needs its referee) + wp4's CL into R2 + Cor 2.3's central
   value + the harness (`m <= 400` exact). Per wp3-a2 §8 item 6 "no further
   stitching session is required" — the assembly is a write-up, not new
   mathematics. Then two referees on the assembly.

**If (2) lands, the dependency chain constituting the proof of Theorem A
= F2(a) is:**
`F2_PROOF_DRAFT.md` (frame, Lemmas 1.x/3.x, Cor 2.3, Lemma 3.6) +
`g1_draft_b.md` (B.0–B.9; two referees + `g1b_repairs_20260802.md`) +
`g2_draft_t2_20260803.md` restricted to its two-referee inventory (§3 above;
+ pending §2c repairs file) + `wp1_draft_c.md` (far bounds W.3–W.6) +
`wp2_draft_b.md` (W.0–W.7) + `repairs_20260811.md` (discharged wave-1
lists + Lemma T.9-Step2') + `wp2_draft_a2.md` (Theorem D.5 + Theorem
T.9-final = Prop 3.5(ii)) + `wp3_draft_a2.md` (Theorem P.5/P.6/P.7/P.8 +
Theorem S) + `harness_m200_20260811.md` (exact `m <= 400`) + [wp4's CL
lemma] + [the assembly note], with the §2a/§2b/§2c repairs folded in at
paper-assembly.

**Standing caveats inside that chain (all flagged, none hidden):** the
grid-certificate-class inputs (wp2-b's `c_4` floor and `c_w` envelope, PW
grid flavor, wp2-a2's `m > 3000` monotonicity tail — each Sturm-able, each
attacked off-grid by referees without violation); Bona's `r(k) >= 1`
(ambient citation); and, for G4 only (not F2(a)), the `[401, 534]` part-(c)
band noted in §2 (harness-to-540 or the `C_ker(4)` sharpening).

**Independently of G2**: G3 (part (b) fine scale) and G4 (part (c) constant
chase) remain open; wave 2 helps both (harness ground truth to 400; the
explicit region-3 constants; item 5's exponents) but touches neither's core.

## 5. Recommended next session

1. **wp4, as its own blind mini-campaign (the priority).** Target: the CL
   spec of `wp3_draft_a2.md` §6.1, verbatim. Give the drafter: that spec;
   wp1-c §5–§6 + §9 item 2 (the proved far/crossover bounds and the
   strip-analyticity route — `log phi_lam` analytic in `|Im t| < lam`, and
   on the residual band `lam in [4/m, 0.89]` is effectively constant, so
   the cumulant-model radius `~ c·lam` beats the Gaussian width
   `1/sqrt(s2)`); T2's (T.6ii) Gaussian domination on `[0, pi/m]`
   (two-referee); the M2 rescue lemma (`Var(truncated geometric) <=
   Var(geometric)` — flagged by the T2 maths referee as independently
   useful exactly here); and g1_draft_b B.6–B.8 as the kernel-bucket
   pattern. Two referees. Budget: this is the campaign's one remaining
   piece of new mathematics — expect iteration.
2. **Repair-application session** for §2a/§2b/§2c (new files;
   `wave2_repairs_2026xxxx.md` + `t2_repairs_2026xxxx.md`), including the
   two wrong-number fixes (82 for "~68"; the E-decimal reprints) and the
   optional harness run to `m ~ 540` (minutes) that pre-clears G4's
   part-(c) band.
3. **Assembly session** (can run concurrently with 1): write the merged
   Theorem A note = Theorem S + T.9-final plug (§2's plug note gives the
   arithmetic) + Cor 2.3 + harness citations, with wp4's CL as the single
   named conditional — so that when wp4 lands the document flips to
   unconditional by inserting one citation. Send it to two referees
   together with the plug.
4. Only after Theorem A closes: G4 (constants; the part-(c) band above) and
   G3 (fine scale), in that order — G4 is mechanical-in-principle with the
   new exponents; G3 remains research.

*End of STATUS_wave2.md.*

*End of STATUS_wave2.md.*
