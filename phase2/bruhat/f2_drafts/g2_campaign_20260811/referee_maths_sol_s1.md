# referee_maths_sol_s1 — adversarial MATHS referee on `sol_s1_20260812.md` (2026-08-12)

*Wave-6b cross-model refereeing, F2 campaign. Target: gpt-5.6-sol's (S1)
attempt against the RE-ARCHITECTED band targets of
`wave6_s1_plan_20260812.md`. Referee posture: maximal bar, default to
refutation — this chain flips the paper's main conjecture to a theorem,
and the cross-model provenance earns NO extra credit. Sources read:
`sol_s1_20260812.md` (the target), `wave6_s1_plan_20260812.md` (including
its §6 (S2)-adjustment note), `STATUS_wave5.md`, `CL_composition_20260812.md`
§3–§4, `wave5_sl4pe_20260812.md` (band-partition line only).
NOT read: `g2_draft_t1_20260803.md`. `gamma = 1/8` untouched.
Every numeric below is from the SAVED+RUN script
`g2_scripts/campaign_20260811/wave6_referees/referee_sol_s1_checks.py`
(archived output `out_referee_sol_s1_checks.txt` beside it, blocks
[A]–[K]; final line `ALL CHECKS OK: True`) or is exact arithmetic shown
inline. Every SOL lemma was ALSO re-derived by hand; the hand derivations
are recorded in §3.*

## 1. VERDICT: **MINOR_REPAIRS**

The mathematics is correct, complete in structure, and interface-exact.
Every lemma SOL.1–SOL.9 re-derives cleanly by hand; every quoted constant
I could attack independently survived; the proof strategy (exact cumulant
representation -> trapezoid enclosure with explicit second-derivative
constants -> finite rational band certificate on `4 <= w <= 40` -> global
geometric-envelope bound on W7 -> reflection for `lam < 0`) reduces
(S1-new) to (i) four one-variable calculus facts, all verified by hand
here, and (ii) ONE finite, fully specified, rational interval computation.

**The single blocking repair (R1):** that finite certificate — the SOL.6
band table AND the derivative bounds (17) — is *claimed, not executed*:
no script or archived output accompanies the draft, so under the
campaign's house rule its numbers currently have the status of a precise
specification plus my corroboration, not a certificate. The draft itself
concedes this (WHAT REMAINS item 1). My independent dense-scan
falsification attack (script block [G], §6 below) FAILED TO FALSIFY any
of the 18 claimed floors/ceilings — observed extrema sit 1.49%–4.46%
inside the claimed ceilings, and the claimed M-constants are generous by
factors 6x/22x/38x — so the certificate is near-certain to execute
cleanly, but it must actually be run and archived (numerics-referee
lane) before (S1) counts. If any table entry fails the interval rerun,
this verdict escalates; nothing in my scan suggests it will.

Remaining repairs R2–R5 are one-line textual items (§5). No circularity,
no scope drift, no hidden small-tilt hypothesis, no interface mismatch
was found — and I hunted for each specifically (§2, §4).

## 2. Interface audit: does it prove EXACTLY what the re-architected chain consumes?

**Yes, and slightly more.** Checked item by item (script block [J]):

1. **Constants.** Draft targets `R31* = (1.19, 1.44, 1.82, 2.04, 2.38,
   2.56, 2.71)`, `R42* = (0.87, 1.62, 3.11, 4.27, 6.38, 7.33, 8.17)` —
   digit-identical to the plan's §2 table (the adopted, non-fallback
   architecture). All 14 proved ceilings are strictly below their
   targets (block [J], seven `OK` rows).
2. **Statement form.** `|kappa_3| <= R31*(W) s2/|lam|`,
   `kappa_4 <= R42*(W) s2/lam^2` — same normalization as composition §4
   (S1) (`r31 = |kappa_3| lam/s2 <= R31*`, `r42 = kappa_4 lam^2/s2 <=
   R42*`; the `kappa_4` bound one-sided, as consumed).
3. **Scope.** Composition/plan scope is `m >= 561`, `lam in (4/m, 0.89]`
   (positive tilt). Draft proves `m >= 561`, `0 < |lam| <= 0.89`,
   `w = m|lam| > 4` — a superset (both tilt signs, all lam, not only the
   mean-matching one). Scope drift is in the SAFE direction only.
4. **Band partition.** `W1..W7 = (4,5]/(5,6]/(6,8]/(8,10]/(10,20]/
   (20,40]/(40,oo)` — byte-matches `wave5_sl4pe_20260812.md` line 66 and
   the plan; the draft's closed certificate intervals `[4,5]..[20,40]`
   are supersets of the half-open bands (edge assignments covered both
   ways).
5. **`m >= 561` arithmetic.** `lam_max(w) = w/561` is exactly
   `lam = w/m <= w/561` for integer `m >= 561`; cell enclosure
   `lam in [0, B/561]` on `w in [A, B]` is a superset of the reachable
   pairs. For `w <= 40`, `lam <= 40/561 = 0.0713 < 0.89`, so the 0.89
   cap never binds on W1–W6b; on W7 it is the only cap used. No gap.
6. **Chain closure.** The plan's own certificate at these exact
   constants: worst row `0.978293` -> `C*(m >= 561) = 19.56586 -> 19.5659
   <= 20` (recomputed, block [J] `OK`), and `0.75839*20 = 15.1678 <= 136`
   at `m >= 1581`. The draft moves NO chain constant itself.
7. **The (S2)-adjustment note (plan §6), checked as instructed.** The
   19.5659 closure presupposes `C5*(W7): 0.80 -> 0.50`, which is (S2)
   business and remains OPEN; the draft correctly disclaims it (WHAT
   REMAINS item 3). Materially: the draft's proved W7 ceilings are the
   geometric values `2.13031/6.41126`, which clear BOTH the adopted W7
   targets `2.71/8.17` AND the plan's no-(S2)-change fallback targets
   `2.42/7.28` (block [J], last `OK`). **This (S1) proof therefore
   survives either resolution of the C5*(W7) question** — worth a ledger
   line when adopted.
8. **Circularity hunt.** SOL.1–SOL.9 consume nothing from the campaign:
   no (S2)/(S3)/(S4), no CL, no ledger row, no Theorem E/SL4' constant.
   The only shared object is the tilted-factor model itself; identity of
   conventions with the campaign engine is confirmed by the sentinel
   audit (block [I]): all six `(m=561, w)` truth pairs AND the
   `(561, lam=0.89)` W7 point reproduce the plan's block-[T] values to
   every quoted digit (e.g. `r31(w=5) = 0.8863645` vs `0.88636`;
   `r42(lam=0.89) = 6.371301` vs `6.3713`).

## 3. Lemma-by-lemma hand audit

**SOL.1 (exact cumulant representation) — CORRECT.** Hand derivation:
`log Z_j(lam) = phi(lam) - phi(j lam)` with `phi(x) = -log(1 - e^{-x}) =
sum_nu e^{-nu x}/nu`; `d^n/dlam^n phi(lam) = (-1)^n g_n(lam)` and the
chain rule gives the `j^n` factor, so `kappa_n = (-1)^n (log Z_j)^{(n)}
= g_n(lam) - j^n g_n(j lam)`, summed over `j = 1..m` — equations
(1)–(3) exact. The closed forms `g_2 = q/(1-q)^2`, `g_3 = q(1+q)/(1-q)^3`,
`g_4 = q(1+4q+q^2)/(1-q)^4` are the standard Eulerian sums (script [A],
rel err `< 1e-27` incl. the delicate small-`x` point `x = 0.008913`).
Removable values `h_2(0), h_3(0), h_4(0) = 1, 2, 6 = (n-1)!` confirmed
by limits. `D_n = w h_n(lam) - lam sum_j h_n(j lam) = lam^{n+1} kappa_n`
is a two-line substitution, and was ALSO verified to rel err `< 1e-28`
at `(561, w = 5)` against the factor sums, and the whole representation
verified against a BRUTE-FORCE convolution of the discrete tilted law at
`(m, lam) = (7, 0.3)` (script [B], errs `< 1e-27`) — so the formulas are
right about the actual probability law, not merely internally consistent.

**SOL.2 (kappa_3 >= 0 for lam > 0) — CORRECT.** `h_2 = (x / (2 sinh(x/2)))^2`
decreasing since `sinh(y)/y` increases. For `h_3 = x^3 cosh(x/2) /
(4 sinh^3(x/2))`: the stated logarithmic derivative `3/x - coth(x/2) -
1/sinh x` is right — by hand, `(1/2)tanh(x/2) - (3/2)coth(x/2) =
-(cosh x + 2)/sinh x` via `tanh(x/2) = (cosh x - 1)/sinh x`,
`coth(x/2) = (cosh x + 1)/sinh x` — and `h_3' < 0` becomes
`F(x) = x cosh x + 2x - 3 sinh x > 0`, which follows exactly as claimed:
`F(0) = F'(0) = F''(0) = 0` and `(x cosh x - sinh x)' = x sinh x > 0`.
Hence every `j >= 2` term of `D_3` is positive; `D_2 > 0`,
`D_3 >= 0` (needs `m >= 2` — moot at 561). Grid attack (script [C]):
0 violations.

**SOL.3 (geometric envelopes) — CORRECT; the load-bearing trick is
sound.** `a = h_3/h_2 = x coth(x/2)` and `b = h_4/h_2 = x^2 + 6 h_2`
verified by hand (using `cosh x + 2 = 3 + 2 sinh^2(x/2)`) and by script
[A]. `a' > 0 <=> sinh x > x`: hand-checked. `b' = x csch^2(y)(2 sinh^2 y
+ 3 - 3y coth y)`, `y = x/2`: hand-verified; bracket positivity is true
(script [C], 0 violations), and admits a one-line proof the draft only
gestures at — see R3. The envelope step is exactly right and is the
draft's key structural insight: `a(j lam) >= a(lam)` gives
`h_3(lam) - h_3(j lam) <= a(lam)(h_2(lam) - h_2(j lam))` TERMWISE, so
`D_3 <= a(lam) D_2` — and, critically, the same argument for `h_4`
needs NO sign information on `h_4(lam) - h_4(j lam)` (the draft says so
explicitly, and it matters: by hand, `h_4 = 6 + x^4/120 + O(x^6)` is NOT
monotone near 0 — it rises to ~6.04 near `x = 2` before decaying — so
any route assuming `h_4` decreasing would have been WRONG. The draft
correctly avoids it).

**SOL.4 (integral formula) — CORRECT.** `int_0^w x^n nu^{n-1} e^{-nu x}
dx = nu^{-2}(n! - Gamma(n+1, nu w))` with `Gamma(n+1, z) = n! e^{-z}
E_n(z)`: standard incomplete-gamma identity, hand-checked; termwise
integration is monotone-convergence-safe. Script [E]: series (13) vs
direct quadrature agree to `< 1.3e-29` at six `(n, w)` points, and the
formula reproduces the campaign's independently archived guard value
`G_4(4) = 0.2323483` exactly — a strong cross-engine consistency check.

**SOL.5 (trapezoid enclosure) — CORRECT.** The composite trapezoid
constant `w lam^2/12 sup|f''|` is standard; the endpoint bookkeeping
`lam sum_{j=1}^m f = T_m + (lam/2)(f(w) - f(0))` is hand-verified; (15)
follows by substitution with `h_n(0) = (n-1)!`. `h_n` extends
real-analytically through `x = 0` (removable), so `C^2[0, w]` holds —
see R4 for a one-clause wording repair. The recurrences (18)/(19)
`h_{n+1} = n h_n - x h_n'` are exact (hand: from `g_{n+1} = -g_n'`;
script [A] err `< 1e-30`). The claimed derivative constants (17) are
TRUE WITH ENORMOUS ROOM: observed sups on `[0, 40]` are
`sup|h_2''| = 0.1667` (at 0+; `h_2''(0) = -1/6` confirmed),
`sup|h_3''| = 0.1818` (at `x ~ 2.18`), `sup|h_4''| = 0.5225` (at
`x ~ 3.56`) vs claimed `1/4/20` (script [D]) — but their PROOF is
delegated to the unexecuted recipe, part of R1. Representation residual
check (script [F]): at `(561, w=5)`, `(561, w=40)`, `(1000, w=17)` the
actual `|eps_n|` is 2 to 16 ORDERS below the claimed bound — the
enclosure is valid and very slack, i.e. safe.

**SOL.6 (rational band certificate) — LOGIC CORRECT; EXECUTION OWED
(R1).** The certificate logic is airtight and even avoids the usual
ratio-of-bounds trap: the cell test `U_3 - c_31 L_2 < 0` with `L_2 > 0`
yields the clean chain `D_3 <= U_3 <= c_31 L_2 <= c_31 D_2`, valid
regardless of the sign of `U_3`/`U_4` (see R5 for the one wording nit in
SOL.7's display). Directions all safe: `L_2` subtracts its error term,
`U_3/U_4` add theirs with `M_3/12 = 1/3`, `M_4/12 = 5/3` exactly; the
`zeta(2)` enclosure (24) is valid (`zeta(2) = 1.6449340668482264365...`,
script [J]); `e^{-4} < 1/54` since `e^4 = 54.598...`; the `nu >= 33`
tail is `5.75e-54` (script [E]) — truncation harmless; the tail-bound
monotonicity in `w` holds since `(e^{-z}E_n(z))' = -e^{-z} z^n/n! < 0`.
The claimed table values themselves: see §4.

**SOL.7 (bands W1–W6b) — CORRECT modulo SOL.6's table.** All 12
comparisons `ceiling < target` are strict (script [J]).

**SOL.8 (W7) — CORRECT, and cleaner than the plan's roadmap.** The bound
`D_3/D_2 <= a(lam) <= a(0.89)`, `D_4/D_2 <= b(lam) <= b(0.89)` holds for
EVERY finite `m` and every `w` — no monotonicity-in-`m`, no limit
interchange, exactly as the draft notes. dps-50 evaluation (script [H]):
`a(0.89) = 2.1303060576...`, `b(0.89) = 6.4112558488...` — enclosures
(26)/(27) both TRUE, both values match the plan's geometric limits
`2.13031/6.41126`, and both clear the targets `2.71/8.17` (27.2%/27.4%,
the plan's advertised worst-band margins). The finite-`m` point
`(561, 0.89)` sits below both (block [I]) — consistent with domination.

**SOL.9 (assembly + negative tilt) — CORRECT.** Per factor,
`a -> (j-1) - a` maps the `lam`-tilted uniform to the `(-lam)`-tilted
one; reflection negates `kappa_3` and preserves `kappa_2, kappa_4`
(cumulants of `-X` are `(-1)^n kappa_n`, and the deterministic shift
drops out for `n >= 2`); convolution preserves this factorwise. So the
`|lam|` form of (S1-new) follows from the `lam > 0` case. Hand-checked;
no gap.

## 4. Status of the numeric certificate (the R1 substance)

The draft presents the SOL.6 table ("Exact outward-rounded rational
interval evaluation gives: ...") and (17) as computation OUTPUTS, but
ships no script and no archived output; the VERIFICATION RECIPE is a
complete and correct spec (cells `2^{-12}`, `lam in [0, B/561]`,
rational `zeta(2)` enclosure, `nu <= 32` + tail (25), interval AD off
`h_2` and (18)/(19), positive-coefficient series at the `x = 0` cell),
but under the house rule a spec is not a certificate. My adversarial
dense-scan (script [G]; grids `1/512`–`1/64` in `w`, 4 `lam` values per
`w` incl. both endpoints, dps 25, per-band):

| band | claimed floor / obs. min `L_2` | claimed `U_3/L_2` ceiling / obs. max (margin) | claimed `U_4/L_2` ceiling / obs. max (margin) |
|---|---|---|---|
| [4,5]   | 1.15 / **1.1933** | 0.900 / **0.88645** (1.53%) | 0.680 / **0.65099** (4.46%) |
| [5,6]   | 1.90 / **1.9608** | 1.090 / **1.07397** (1.49%) | 1.250 / **1.20619** (3.63%) |
| [6,8]   | 2.75 / **2.8343** | 1.370 / **1.34863** (1.58%) | 2.400 / **2.30818** (3.98%) |
| [8,10]  | 4.65 / **4.7376** | 1.550 / **1.51857** (2.07%) | 3.260 / **3.16455** (3.02%) |
| [10,20] | 6.60 / **6.7157** | 1.850 / **1.80430** (2.53%) | 4.980 / **4.82376** (3.24%) |
| [20,40] | 16.50 / **16.7101** | 1.970 / **1.91408** (2.92%) | 5.650 / **5.47709** (3.16%) |

Zero falsifications; every claimed ceiling carries >= 1.49% headroom
over the observed supremum, and the `U/L` functions vary by only
`O(1e-4)` across a `2^{-12}` cell, so interval slop cannot plausibly eat
those margins. The suprema sit at the band right edges at `lam =
lam_max`, as expected. Conclusion: the table is almost certainly
certifiable exactly as printed — but the certificate must be RUN and its
output archived (numerics referee) before SOL.6/SOL.7 count as proved.
(17) is in the same debt class and is even safer (observed sups 6x–38x
below the claimed constants).

## 5. Findings (repairs R1–R5; none touches a constant except via R1's rerun)

- **R1 (BLOCKING; numerics-referee lane).** Execute and archive the
  SOL.6 interval certificate and the (17) interval verification exactly
  per the draft's own recipe (or any outward-rounded equivalent), and
  quote the output in/beside the draft. Until then (S1) remains
  UNPROVED under house rules. My block-[G]/[D] scans predict a clean
  pass with >= 1.49% ceiling headroom and 6x–38x derivative headroom.
- **R2 (one line).** SOL.8's "Direct rigorous evaluation gives
  (26)/(27)" — two point evaluations of elementary functions; cite an
  interval evaluation or the numerics referee's rerun (my dps-50 values
  confirm both enclosures). Fold into R1's run.
- **R3 (one line).** SOL.3's `b' > 0`: the asserted route ("after
  multiplication by sinh y cosh y, two differentiations...") is not
  displayed. Cleaner complete proof, offered verbatim: multiply the
  bracket by `sinh y` to get `P(y) = 2 sinh^3 y + 3 sinh y - 3y cosh y`;
  then `P(0) = 0` and `P'(y) = 6 sinh^2 y cosh y - 3y sinh y =
  3 sinh y (sinh 2y - y) > 0`. Adopt either this or the displayed
  two-differentiation computation.
- **R4 (one clause).** SOL.5 should state explicitly that `h_n` extends
  to `C^2[0, w]` (real-analytic; removable singularity at 0) so the
  trapezoid remainder applies on the first cell — the fact is true and
  the V3 recipe already handles the endpoint numerically.
- **R5 (wording).** SOL.7's display `D_3/D_2 <= U_3/L_2` silently uses
  `U_3 >= 0`; the certificate's own cell test already gives the sign-free
  chain `D_3 <= U_3 <= c_31 L_2 <= c_31 D_2` — state it that way (or add
  `U_3, U_4 >= 0 on the verified cells`, which the run will show anyway).

**Observations (no repair owed):** (i) the proof covers both tilt signs
and all `lam`, not only mean-matching tilts — safe-direction strength;
(ii) the W7 argument survives the plan's (S2) fallback (`C5*(W7) = 0.80`
kept, targets `2.42/7.28`) since `2.13031 < 2.42`, `6.41126 < 7.28` —
record in the ledger on adoption; (iii) the draft's WHAT REMAINS list is
honest and correctly scoped ((S2)/(S3)/(S4) untouched; downstream
SL4'-rows/`REM*`/`J0` re-certification correctly assigned to the plan's
§9, not to (S1)); (iv) the truth attack on (S1-new) itself (script [K]:
90 probes, `m` up to 3000, all bands incl. edges `4.001..40` and W7 deep
corner) found 0 violations.

## 6. Numerical evidence (verbatim from `out_referee_sol_s1_checks.txt`)

```
[D] SOL.5 (17): sup |h_n''| on [0, 40] (dense scan)
  observed sup|h2''| = 0.16664667 at x = 0.02
  observed sup|h3''| = 0.18181968 at x = 2.18
  observed sup|h4''| = 0.52251029 at x = 3.56
[H] SOL.8: a(0.89), b(0.89) enclosures
  a(0.89) = 2.1303060576444510159
  b(0.89) = 6.4112558488549645817
[I] V1 sentinels at m = 561 (exact factor sums, dps 30)
  w= 5: r31 = 0.8863645 (table 0.88636), r42 = 0.6506471 (table 0.65065)
  w=40: r31 = 1.911351 (table 1.9114), r42 = 5.465337 (table 5.4653)
  (561, lam=0.89): r31 = 2.124025 (plan 2.12402), r42 = 6.371301 (plan 6.3713)
[J] ... OK  chain: 0.978293 * 20 = 19.56586 -> 19.5659 <= 20
    ... OK  (S2)-fallback W7 targets 2.42/7.28 ALSO cleared by geometric bound
[K] ... OK  (S1-new) truth attack: 0 violations in 90 probes
ALL CHECKS OK: True
```

(Full output archived beside the script.)

## 7. Verdict restated

**MINOR_REPAIRS.** The proof architecture is correct end-to-end and the
constants are exactly the re-architected chain's; conditional on R1 (the
one-shot execution + archival of the draft's own fully specified finite
certificate, predicted to pass with quantified headroom) and the R2–R5
one-liners, `sol_s1_20260812.md` proves Theorem SOL.9 = (S1) at the
wave-6 constants, and the plan's chain certificate then closes at
`C*(m >= 561) = 19.5659 <= 20`. Per house rules (S1) counts only when
the numerics referee's independent rerun (which discharges R1) also
passes. This maths pass found NO error of substance.

*End of referee_maths_sol_s1.md.*
