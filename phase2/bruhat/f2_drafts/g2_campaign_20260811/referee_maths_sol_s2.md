# referee_maths_sol_s2 — adversarial maths referee on `sol_s2_20260812.md` (wave 6b, cross-model)

*Adversarial MATHS referee pass, F2 campaign wave 6b, 2026-08-12. Target:
`sol_s2_20260812.md` (OpenAI gpt-5.6-sol, single-model UNREFEREED, attempt
at (S2) = SL1'-w(ii)). Bar: maximal, default to refutation; a cross-model
draft gets NO extra credit for being cross-model. Sources read:
the target, `CL_composition_20260812.md` (§4 (S2) verbatim; the consumer
interface), `STATUS_wave5.md`, `wave6_s1_plan_20260812.md` (the scout's
(S2)-adjustment `C5*(W7): 0.80 -> 0.50` and its fallback),
`wave5_sl4pe_20260812.md` §0 (the band partition, consumed verbatim by the
composition). NOT read: `g2_draft_t1_20260803.md`. `gamma = 1/8`
untouched. New script (SAVED and RUN 2026-08-12, output archived beside
it, quoted verbatim in §4):
`g2_scripts/campaign_20260811/wave6_referees/referee_sol_s2_checks.py`
(`out_referee_sol_s2_checks.txt`), mpmath dps-60, blocks [A]–[G]. Every
lemma's algebra was ALSO re-derived by hand before scripting (§2).*

## VERDICT: **FATAL** (as an (S2) proof artifact)

**Not for error — for absence.** The draft is internally correct at every
line I checked (all six lemmas re-derived by hand; every quoted numeric
reproduced to the printed digits at dps 60), and it is scrupulously honest
about its own status. But it proves **zero of the seven band bounds that
(S2) IS**. Its own closing section says so verbatim: "(S2) is not proved
here… Thus (S2), and hence CL through this route, remains open." Its only
quantitative bound (SOL.4) is cancellation-free and fails the W1 target by
a factor of ~23 (referee block [D]: `C_abs = 1.15907` vs `C5*(W1) = 0.05`
at the (561, w=4.5) corner). The entire mathematical content of (S2) — the
bandwise suprema with the small constants — is not attempted. No
text-level repair can turn this artifact into (S2); hence FATAL under the
house scale, with the salvage inventory of §3-F6 recorded because several
pieces are genuinely reusable by the eventual SL1' prover.

Additionally, the draft's central stated blocker — that the bands
`W1..W7` "are not defined by their `w = m lam` endpoints" in the campaign
statement — is **false at the corpus level** (§3-F2): the partition
`w in (4,5]/(5,6]/(6,8]/(8,10]/(10,20]/(20,40]/(40, 0.89m]` is defined in
`wave5_sl4pe_20260812.md` §0 (lines 66–68), which `CL_composition` §1/I5
consumes and §4 references. And the draft's obligations table is pinned to
the superseded `C5*(W7) = 0.80` with no mention of the wave-6 scout
adjustment `0.80 -> 0.50` that the re-architected (S1) chain
(`19.5659 <= 20`) requires (§3-F3) — an interface staleness that would
mislead any prover following its "verification recipe".

## 1. The consumer interface the draft had to hit

`CL_composition_20260812.md` §4, (S2) [SL1'-w(ii)], verbatim scope: for
`m >= 561`, `lam in (4/m, 0.89]`, band `W` of `w = m lam`:

```
log phi(t) = -s2 t^2/2 - i kappa_3 t^3/6 + kappa_4 t^4/24 + R5(t),
|R5(t)| <= C5*(W) s2 t^5 / lam^3   on  [0, lam/2],
C5* = 0.05/0.06/0.08/0.10/0.15/0.25/0.80  (W1/W2/W3/W4/W5/W6b/W7),
```

with the wave-6 scout (`wave6_s1_plan_20260812.md` §6) proposing the ONE
(S2) adjustment `C5*(W7): 0.80 -> 0.50` (fallback: keep 0.80 at the cost
of the (S1) worst-band margin dropping 27.21% -> 13.55%). Bands per
`wave5_sl4pe` §0: `W1..W7 = w in (4,5]/(5,6]/(6,8]/(8,10]/(10,20]/
(20,40]/(40, 0.89m]`. Interface facts checked: the draft's expansion sign
convention (`- i kappa_3 t^3/6`, `+ kappa_4 t^4/24`) matches the consumed
statement EXACTLY; its normalization `Q = lam^3 |R5|/(s2 t^5)` and domain
(`m >= 561`, `4/m < lam <= 0.89`, `0 <= t <= lam/2`) match EXACTLY; its
constants table matches the composition's ORIGINAL row (not the scout's).

## 2. Lemma-by-lemma verification (all hand-re-derived, then scripted)

- **SOL.1 (tilted partition function).** Correct. `Z_m(z) = prod_j
  (1-e^{-jz})/(1-e^{-z})` is the tilted product law; `E_lam e^{itX} =
  Z_m(lam-it)/Z_m(lam)`; cumulants `kappa_n = (-1)^n L_m^{(n)}(lam)` from
  `K(u) = L_m(lam-u) - L_m(lam)` — so `s2 = L''`, `kappa_3 = -L'''`,
  `kappa_4 = L^{(4)}`, all as stated. The model is the campaign's `S_lam`
  (factor-cumulant shape `kappa_n = m phi_n(lam) - sum_j j^n phi_n(j lam)`
  of `wave5_sl4pe`/scout §8, with `phi_n = A_{n-1}`) — no model mismatch.
  Script [B]: brute-force discrete-law cumulants at `(m, lam) = (7, 0.37)`
  match the formulas to `< 1e-57`.
- **SOL.2 (derivative formulas).** Correct. Hand check: termwise
  differentiation of `L_m(z) = -sum_j sum_r e^{-rjz}/r + m sum_r
  e^{-rz}/r` (locally uniform on `Re z >= delta > 0`) gives
  `L^{(n)}(lam) = (-1)^n (m A_{n-1}(lam) - sum_j j^n A_{n-1}(j lam))`;
  the `A_4` numerator `1 + 11q + 11q^2 + q^3` is the correct Eulerian
  row. Positivity structure of (SOL.2.1): `s2 = sum_j Var(U_j)` with
  `Var(U_j) = A_1(lam) - j^2 A_1(j lam) > 0` for `j >= 2` (and `= 0` at
  `j = 1`, `U_1 == 0`) — consistent. Script [A]: closed forms vs direct
  sums, relerr `< 1e-60` at three abscissae.
- **SOL.3 (exact remainder, two forms).** Correct, and this is the
  draft's one genuinely valuable deliverable. Hand check of the degree
  bookkeeping: the degree-n term of the double series is `(it)^n/n! *
  (-1)^n L^{(n)}(lam) = kappa_n (it)^n/n!`, so subtracting degrees 0–4
  (degree 0 by the `-1`, degree 1 by the centering term `it L'(lam)`)
  leaves exactly (SOL.3.1); (SOL.3.2) is Taylor-with-integral-remainder
  along `lam -> lam - it`, which stays in `Re z = lam > 0` where
  `|e^{-jz}| < 1` — principal branch throughout, no winding issue.
  Script [C]: `R5_direct = R5_series = R5_integral` at `(7, 0.37)` to
  `< 5e-61` and at the campaign-scale `(60, w = 4.5)` point to `< 8e-59`
  (series form to `4e-16`, pure truncation at `R = 600`).
- **SOL.4 (pointwise majorant).** Correct as an inequality: `|A_4(jz)| <=
  A_4(j lam)` on `Re z = lam`, `(1/4!) int_0^1 (1-u)^4 du = 1/120` —
  hand-checked; script [D] confirms `|R5(lam/2)| <= B_5 (lam/2)^5` at all
  three probe corners. But it is USELESS for six of the seven bands, as
  the draft itself half-admits ("too crude to establish the small
  constants 0.05, …, 0.25"): referee block [D] quantifies it —
  `C_abs = 1.15907` (W1 corner, 23.2x over target), `1.02411` (W1 right
  edge, 20.5x). See F4 for the one band where it is NOT too crude.
- **SOL.5 (exact criterion).** Correct and interface-exact: (SOL.5.3) is
  precisely the composition's (S2) row divided by `s2 t^5/lam^3`, over
  precisely the right domain, with the correct continuous extension
  (SOL.5.2) at `t = 0` (from (SOL.3.2), `L^{(5)}` continuous at `lam`).
  Independent cross-validation, script [G]: SOL.5.2 evaluated at the W7
  deep corner `(561, 0.89)` gives `Q(0) = 0.21152994` — matching the
  wave-6 scout's INDEPENDENT kappa_5 leading-order computation `0.21153`
  (block [S2] of `scout_s1_targets.py`) to all printed digits. Two
  different derivations, same number: both are right.
- **SOL.6 (deep-corner limit).** Arithmetic fully verified, script [E]:
  `a = -0.00219677565710487788…`, `b = 0.00531427566747278288…`,
  `32 sqrt(a^2+b^2) = 0.184013492813225`, and the formula (SOL.6.1) at
  `x = 1/2` reproduces the same value exactly. Finite-size corroboration:
  `Q(N^2, 1/N, 1/(2N)) = 0.13268/0.16558/0.17510/0.17963/0.18129` at
  `N = 20/50/100/200/320` — a clean ~1/N approach to `0.18401`. The
  LIMIT ARGUMENT as written is sketch-level (see F5), but the claim is
  true and the consequence is correctly scoped by the draft itself: it
  refutes only a hypothetical unbounded-`w` W1 at `0.05`; since the real
  `W1 = (4, 5]` is bounded, nothing in the campaign is refuted. The
  sequence `(N^2, 1/N)` has `w = N`, i.e. lies in the REAL W7 for
  `N > 40`, where the limit `0.184013` sits BELOW both the old `0.80`
  and the scout-adjusted `0.50` (script [F]: both True) — consistent, no
  alarm.

**Circularity/hidden-hypothesis hunt:** clean. The draft consumes nothing
from the CL chain (no A2 floors, no SL3'/SL4' objects, no eta), assumes
no small-tilt restriction anywhere a bound is claimed (SOL.4 holds for
all `lam > 0`), and promotes no measured value to a proof (its §"WHAT
REMAINS" item 3 states this explicitly, and it is true).

## 3. Findings

- **F1 (FATAL as a discharge of (S2)).** The artifact proves none of the
  seven required suprema. What is actually proved: two exact identities
  (SOL.3.1/3.2), one crude bound (SOL.4) demonstrably 20–23x short on W1
  (script [D]), one equivalence (SOL.5), one limit constant (SOL.6). The
  bound proved is NOT the R5 statement `CL_composition` consumes, for any
  band, and the draft says so. (S2) remains exactly as open as before
  this draft existed. No repair short of doing the actual bandwise
  cancellation-retaining analysis — i.e., a new proof — closes this.
- **F2 (MAJOR, premise error).** The load-bearing excuse — "the seven
  bands are not defined by their `w = m lam` endpoints… so the seven
  required suprema are not defined" — is false of the campaign corpus:
  the endpoints are fixed verbatim in `wave5_sl4pe_20260812.md` §0
  (`(4,5]/(5,6]/(6,8]/(8,10]/(10,20]/(20,40]/(40, 0.89m]`), the file the
  composition consumes as I5 and whose notation §4 inherits. The draft's
  conditional framing ("if, as seems likely, W_1 is a bounded interval
  near 4") shows it could have resolved this and did not. Possibly an
  artifact of the prompt fed to the model — but the artifact on disk
  asserts a falsehood about the campaign statement, and its suprema-
  undefined claim (line "the missing band endpoints are not cosmetic")
  must not be cited as a fact about (S2).
- **F3 (MAJOR, interface staleness).** The obligations table (recipe
  step 6) and the constants range quoted at the top ("0.05 to 0.80") are
  pinned to the pre-scout `C5*(W7) = 0.80`. The wave-6 re-architected
  (S1) targets — the ones the parallel wave-6b (S1) attack was verified
  against (chain constant `19.5659 <= 20`) — REQUIRE `C5*(W7) = 0.50`
  (scout §6; fallback 0.80 exists but costs the (S1) worst-band margin
  27.21% -> 13.55%). A prover executing this draft's recipe would certify
  W7 at 0.80 and leave the adopted chain uncovered. Any reuse of this
  draft must re-point W7 at 0.50 (or explicitly invoke the fallback).
- **F4 (SIGNIFICANT missed result — the draft understates its own
  bound).** The draft dismisses SOL.4 as "too crude to establish the
  small constants 0.05, …, 0.25" — carefully excluding W7's constant,
  then never evaluating `C_abs` anywhere. Referee block [G]: on an
  8-point adversarial sample of W7 (both corners `w -> 40+` at
  `m = 561…100000`, the deep corner `lam = 0.89` at `m = 561/2000`, and
  mid-band), `C_abs in [0.2149, 0.2624]` — comfortably below BOTH the
  old 0.80 AND the scout's 0.50, with the maximum at the `w -> 40+`
  small-`lam` corner (`0.2624`, stable in `m`). On W6b the same bound
  gives `0.2623–0.3378` vs target `0.25` — fails, so W1–W6b genuinely
  need cancellation. **The draft's own machinery plus a one-page sup
  analysis of the explicit smooth function `C_abs(m, lam)` over
  `(40, 0.89m] x [561, oo)` plausibly closes W7 — the single band whose
  (S2) constant the re-architected chain actually tightened.** The draft
  attempted no band and hence delivered no band. (This referee
  observation is a lead for the SL1' prover, NOT a certified result: the
  sample is 8 points + the structural `lam -> 0` limit; a proof needs
  the sup argument.)
- **F5 (minor).** SOL.6's proof is a sketch: the numerator-sum estimate
  "`sum_j log(1-e^{-jz})` is `O(N)`" is actually `O(N log N)` (the
  `j <~ N` terms contribute `~ log N` each), which still suffices
  against the `O(N^2)` main term, and the locally-uniform-in-`u`
  convergence needed to pass the limit through the integral form is
  asserted, not proved. The constant itself is verified (script [E],
  finite-N approach confirms). Harmless here because SOL.6 is a caution,
  not a consumed bound; would need tightening only if anyone ever cites
  (SOL.6.1) as a theorem.
- **F6 (salvage inventory — what the SL1' prover can reuse).** (i) The
  exact remainder identity SOL.3.1 with its `E_4` structure — the
  correct starting point for a cancellation-retaining bandwise bound,
  and the referee-friendly dual form SOL.3.2; (ii) the interface-exact
  criterion SOL.5.3 (with the W7 constant re-pointed per F3); (iii)
  SOL.4 as the W7 closer candidate per F4; (iv) SOL.5.2 as the stable
  `t -> 0` evaluation (now independently cross-validated against the
  scout's kappa_5 number, §2); (v) the SOL.6 warning that any band
  containing `w -> oo` has `liminf`-of-sup at least `0.184013`, so no
  future band redesign may push a `< 0.184` constant onto an unbounded
  band — in particular a hypothetical W7 tightening below `0.19` is
  IMPOSSIBLE (this bounds the scout-style slack-spending from below:
  `C5*(W7) = 0.50` is safe, `0.18` would not be).

## 4. Referee script and verbatim output

Script: `g2_scripts/campaign_20260811/wave6_referees/referee_sol_s2_checks.py`
(mpmath dps 60; brute-force discrete law, three independent `R5` routes,
band scans). Archived output `out_referee_sol_s2_checks.txt`, quoted:

```
[A] SOL.2 scalar identities
  x= 0.30:  relerr A1 = 1.47e-60   relerr A4 = 2.58e-61
  x= 0.89:  relerr A1 = 3.95e-61   relerr A4 = 1.16e-61
  x= 2.00:  relerr A1 = 4.3e-61   relerr A4 = 6.19e-61

[B] SOL.1/SOL.2 cumulants vs brute force  (m=7, lam=0.37)
  mu : brute 6.690635065628285359  formula 6.690635065628285359  diff 6.22e-61
  s2 : brute 8.8948844473341866017  SOL.2.1 8.8948844473341866017  diff 1.49e-59
  k3 : brute 9.7035743059840714753  formula 9.7035743059840714753  diff 6.22e-59
  k4 : brute -7.2103903477682792539  formula -7.2103903477682792539  diff 8.38e-58

[C] SOL.3: R5 three ways
  (m,lam,t)=(7,0.37,0.185):
    R5_direct   = (0.000014865290567799151047 - 0.00018390151515594218542j)
    R5_series   = (0.000014865290567799151047 - 0.00018390151515594218542j)   |d-s| = 4.62e-61
    R5_integral = (0.000014865290567799151047 - 0.00018390151515594218542j)   |d-i| = 4.16e-61
  (m,lam,t)=(60,0.075,0.0375):
    R5_direct   = (0.0021828517822206809928 - 0.0047797447239234667393j)
    R5_series   = (0.0021828517822210855458 - 0.0047797447239235377467j)   |d-s| = 4.11e-16
    R5_integral = (0.0021828517822206809928 - 0.0047797447239234667393j)   |d-i| = 7.19e-59

[D] SOL.4 majorant + size of C_abs vs targets
  W1 corner  (m=561, w=4.5): |R5(lam/2)| = 0.0486954  <= B5 t^5 = 7.06008 : True
      C_abs = 1.15907   vs C5* = 0.05   (ratio 23.181x)
      measured Q(t=lam/2) = 0.00799447
  W1 rt edge (m=561, w=5.0): |R5(lam/2)| = 0.0448876  <= B5 t^5 = 7.0541 : True
      C_abs = 1.02411   vs C5* = 0.05   (ratio 20.482x)
      measured Q(t=lam/2) = 0.00651678
  W7 deep    (m=561, lam=0.89): |R5(lam/2)| = 3.17756  <= B5 t^5 = 3.56113 : True
      C_abs = 0.218226   vs C5* = 0.8   (ratio 0.27278x)
      measured Q(t=lam/2) = 0.194721

[E] SOL.6 constant and convergence
  a = -0.0021967756571048778831   (draft: -0.002196775657104877)
  b = 0.0053142756674727828809   (draft:  0.00531427566747278)
  32 sqrt(a^2+b^2) = 0.184013492813225   (draft: 0.18401349...)
  Q_inf(1/2) via formula = 0.184013492813225   match: True
  N=  20: (m,lam,t)=(400,1/20,1/40)  w=20  Q = 0.1326818484
  N=  50: (m,lam,t)=(2500,1/50,1/100)  w=50  Q = 0.1655819615
  N= 100: (m,lam,t)=(10000,1/100,1/200)  w=100  Q = 0.1751044078
  N= 200: (m,lam,t)=(40000,1/200,1/400)  w=200  Q = 0.1796320505
  N= 320: (m,lam,t)=(102400,1/320,1/640)  w=320  Q = 0.1812918596

[F] W7 C5 comparison: Q_inf(1/2) = 0.184013 vs old C5*(W7)=0.80, scout C5*(W7)=0.50
  0.184013 <= 0.50: True   0.184013 <= 0.80: True
  scout-quoted W7 corner truth 0.2104/0.21153: measured Q at (561, 0.89, lam/2) printed in [D]

[G] supplementary: C_abs over W7/W6b sample + SOL.5.2 Q(0) at the W7 corner
  W7 sample (m=561, w=40.001, lam=0.071303): C_abs = 0.262403
  W7 sample (m=561, w=45.0, lam=0.0802139): C_abs = 0.254922
  W7 sample (m=561, w=100.0, lam=0.178253): C_abs = 0.224034
  W7 sample (m=2000, w=41.0, lam=0.0205): C_abs = 0.260953
  W7 sample (m=10000, w=41.0, lam=0.0041): C_abs = 0.261044
  W7 sample (m=100000, w=41.0, lam=0.00041): C_abs = 0.261066
  W7 sample (m=2000, w=1780.0, lam=0.89): C_abs = 0.214871
  W7 sample (m=561, w=499.29, lam=0.89): C_abs = 0.218226
  W6b sample (m=561, w=20.001, lam=0.0356524): C_abs = 0.337272  (target 0.25)
  W6b sample (m=561, w=40.0, lam=0.0713012): C_abs = 0.262404  (target 0.25)
  W6b sample (m=100000, w=20.001, lam=0.00020001): C_abs = 0.337799  (target 0.25)
  W6b sample (m=100000, w=40.0, lam=0.0004): C_abs = 0.26273  (target 0.25)
  Q(561, 0.89, t=0) per SOL.5.2 = 0.21152994   (scout block [S2] leading order: 0.21153)
```

Referee-numerics note: block [C]'s `4.11e-16` on the series form is pure
`R = 600` truncation (`e^{-600 * 0.075} ~ 3e-20` times polynomial factors),
not a discrepancy — the integral form matches the direct form to `7e-59`
at the same point.

## 5. Ledger consequences

1. **(S2) status: UNCHANGED — CONJECTURED, no proof artifact.** This
   draft must NOT be counted as the SL1'-w(ii) deliverable, and nothing
   in it may be cited as progress on (S2)'s bandwise constants. The
   wave-6b cross-model attempt on (S2) FAILED to engage the target.
2. If any future artifact cites this draft's identities (legitimate per
   F6), it must (a) not cite the "bands undefined" claim (F2 — false),
   (b) re-point the W7 obligation at the scout's `0.50` or explicitly
   invoke the 0.80-fallback chain (F3), and (c) treat SOL.6's proof as a
   sketch pending the F5 tightening.
3. Lead recorded for the SL1' prover (non-binding): F4's `C_abs <= ~0.263`
   sample on W7 suggests SOL.4 + a sup argument closes the W7 band at
   `0.50` outright; W1–W6b need genuine cancellation (the 20–23x deficit
   is structural — the `m`-term and `j`-sum in `L^{(5)}` nearly cancel at
   small `lam` and SOL.4 adds them). Also the SOL.6 constant `0.184013`
   is a hard floor for ANY constant assigned to an unbounded band — the
   scout's `0.50` clears it 2.7x; nothing below `0.19` is ever available
   there.

**VERDICT: FATAL** — the deliverable (S2) is not proved, not partially
proved bandwise, and not reducible to a repair; the artifact's correct
content is scaffolding only, inventoried in F6.

*End of referee_maths_sol_s2.md.*
