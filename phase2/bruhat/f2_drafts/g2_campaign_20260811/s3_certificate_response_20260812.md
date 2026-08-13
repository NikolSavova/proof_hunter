# Response to the Sol review of the (S3) compact-band certificate — MAJOR_ISSUES

*2026-08-12. `solref_maths_s3_certificate_20260812.md` is a cross-model (gpt-5.6-sol)
adversarial review of my own `s3_certificate_20260812.md`, commissioned because that
note was single-author and unrefereed — the exact thing this project's rules say not
to trust. Verdict **MAJOR_ISSUES**, 8 items. This note records what the review
confirmed, repairs what is cheaply repairable, and states plainly what is not.*

## 0. What the review CONFIRMED (independent, hand-recomputed)

- The substitution `z = 561/m`, `lam = w z/561 = w/m`; `m >= 561 <=> 0 < z <= 1`;
  and `0 < lam <= 40/561 ~ 0.0713` on the six bands.
- The six rectangles cover exactly `4 <= w <= 40`; shared endpoints are harmless
  (both neighbours certify them); `w = 40` sits in W6b.
- Both counts: `36 * 2048 * 256 = 18,874,368` and `1310+199+32+15+18+17 = 1591`.
- **The F2 repair is valid**: `(2 - 2^-7)|B_8|/8! = 17/10321920 = (255/128)/1209600`,
  so the draft understated by `255/128 = 1.9921875` and "replacing it by `2/1209600`
  is safe, with only the factor `256/255` of extra slack." (Matches my own exact-
  rational check: `sup|B_8({x}) - B_8| = 17/256`.)
- **A closed form for my Cauchy sum**, agreeing with the computed value to every
  quoted digit:
  `SUM8 = 8!/(2 * 6^8) [ (1 - 1/6)^-9 + (1 + 1/6)^-9 ] ~ 0.064929`.
- The F3 implication direction (proving `J <= J0^(5)` gives `J <= J0^(6)` when
  `J0^(5) <= J0^(6)` band by band).

**No mathematical error was found in the certificate.** Every issue below concerns
the artifact's *evidence standard* — what a referee can reconstruct from the note.

## 1. REPAIRED — the per-band evidence the note failed to expose (issues 1, 3)

The script now reports, and `out_s3_certificate.txt` now archives, the quantities
the review asked for. Re-run 2026-08-12 (full, from a cleared checkpoint):

| Band | target | max `J_upper` over leaves | worst leaf (exact rationals) | min `F2_lower` (predicate: `> 1/10`) |
|---|---|---|---|---|
| W1 | 1/2 = 0.5 | 0.499999729 | `w in [629/128, 315/64], z in [5/16, 3/8]` | 0.886221379 |
| W2 | 13/20 = 0.65 | 0.649941242 | `w in [173/32, 87/16], z in [3/4, 1]` | 1.801976152 |
| W3 | 9/10 | 0.824957912 | `w in [127/16, 8], z in [0, 1]` | 2.726773720 |
| W4 | 11/10 | 1.098154878 | `w in [39/4, 10], z in [0, 1]` | 4.713589760 |
| W5 | 3/2 | 1.493300186 | `w in [45/4, 95/8], z in [0, 1]` | 6.707927493 |
| W6b | 17/10 | 1.671614346 | `w in [85/4, 45/2], z in [0, 1]` | 16.649009994 |

Two readings this table forces, both worth stating:

- **The `F2 > 1/10` predicate is never close** — the tightest is W1 at 0.886, an
  8.9x margin. That predicate is not where risk lives.
- **`max J_upper` is an artifact of the stopping rule, not a measurement.**
  Adaptive refinement halts the instant a box clears its target, so W1's
  `0.499999729` means only "some leaf cleared 1/2 by 2.7e-7 and was not refined
  further" — it does NOT mean `sup J ~ 0.5`. The truth on W1 is the Claude
  referee's measured `max J = 0.46031849` (7.94% below target). Termination with
  zero hard failures is the whole content of the certificate.

`M_n(6)` from `out_sol5_certificate.txt`, also previously unreported (issue 3):
`M_2(6) <= 467.982`, `M_3(6) <= 20954.6`, `M_4(6) <= 1.44485e6`; the worst arcs sit
near `theta ~ 4.71 ~ 3pi/2`, i.e. adjacent to the pole at `-2 pi i`, as expected.
Arc coverage: `[0, 2pi]` is partitioned into 4000 closed arcs whose union is the
whole circle, and each arc's `(cos, sin)` interval box *contains* its arc, so the
union of the evaluated boxes contains `|z| = 6`. Pole avoidance is implied by the
returned enclosures being finite (a box enclosing a zero of `sinh(z/2)` would
produce a division by an interval containing 0).

## 2. REPAIRED — the [1,40] tail derivation, written out (issue 4)

Summand `a_k = k^p e^(-k x)` with `p = n - 1 + r <= 11`. Then
`a_(k+1)/a_k = (1 + 1/k)^p e^(-x) <= e^(p/k) e^(-x)`, and for `k >= K >= 2p/x` this
is `<= e^(x/2) e^(-x) = e^(-x/2) < 1`. Hence
`sum_(k>K) a_k <= a_K * e^(-x/2)/(1 - e^(-x/2)) <= K^p e^(-Kx)/(1 - e^(-x/2))`,
which is the formula the code uses (it takes the un-discounted `a_K` numerator, so
it is the weaker, safe direction). The hypothesis `K >= 2p/x` is enforced by a
runtime assertion with `K = 400`, `p <= 11`, `x >= 1` (so `2p/x <= 22 << 400`).
Monotonicity in `x` justifies evaluating at the left endpoint of each `x`-interval.

## 3. REPAIRED — the `z = 0` endpoint (issue 5)

The recursion's boxes include `z = 0`, which is outside the original parameter set
(`z = 561/m > 0`). This is a *superset*, so certifying it is stronger, provided the
formulas are valid there — which they are: `z = 0` means `lam = 0`, and every term
of the enclosure is continuous at `lam = 0` by construction, because `h_n` is
implemented in the even form `h_2 = 1/s(lam/2)^2`, `h_3 = 2 cosh(lam/2)/s^3`,
`h_4 = (2 cosh lam + 4)/s^4` with `s(y) = sinh(y)/y` evaluated by its Taylor series
(`s(0) = 1`), never as `x^n phi_n(x)`. At `lam = 0` the expansion collapses to
`F_n = G_n(w)`, which is exactly the `m -> infinity` limit row the Claude numerics
referee computed independently. So the `z = 0` face is the correct closure of the
parameter set, not an extrapolation.

## 4. REPAIRED — the exact `J0` interface vector (issue 6)

The certified targets are, exactly:
`J0 = (1/2, 13/20, 9/10, 11/10, 3/2, 17/10)` on `(W1, W2, W3, W4, W5, W6b)`.
This is the wave-5 row, reproduced verbatim from `sol_s3_20260812.md` (SOL.7). Any
consumer must check this vector against what it actually consumes; the scout's
wave-6 row is uniformly larger and is therefore implied, but a certificate should
name its own vector, which is what this paragraph does.

## 5. REPAIRED — the corrected remainder as a formally restated lemma (issue 7)

The review is right that "the old formulas must carry a factor two" is prose, and
that leaving (SOL.4)/(SOL.6)/(SOL.13) unrestated risks two incompatible remainder
versions in the composition. Restated formally, for citation:

> **Lemma EM' (replaces (SOL.4)/(SOL.6)).** With the expansion of (SOL.3) retaining
> endpoint corrections through the `B_6` term and NO `B_8` endpoint term,
> `|E_{n,8}| <= (17/10321920) * lam^8 * int_0^w |h_n^(8)(x)| dx`
> `<= 2 * lam^8 /1209600 * int_0^w |h_n^(8)|`, and under (SOL.5)
> `<= 2 * 10^12 * w * lam^8 / 1209600`.
> *Proof.* One integration by parts carries `-int B_7({x})/7! f^(7)` to
> `int (B_8({x}) - B_8)/8! f^(8)`; `sup_x |B_8({x}) - B_8| = 17/256 = (2 - 2^-7)|B_8|`
> (exact, verified in rational arithmetic and on a 2000-point grid), giving the
> kernel constant `17/10321920`. The stated `1/1209600` is the `B_8`-endpoint-term
> form and is NOT available here. ∎

**Everything certified in `s3_certificate_20260812.md` uses Lemma EM', not (SOL.4).**
The still-unrun W7 argument must cite Lemma EM' too — flagged for whoever takes W7.

## 6. NOT REPAIRED — the interval-arithmetic proof standard (issue 2)

The review is correct that "directed-rounding interval arithmetic is rigorous" is
*assumed* here, not proved, and that dual-precision agreement (dps 30/40/50) is a
stability test rather than a rounding theorem. Recorded for the record:
**mpmath 1.4.1, `mpmath.iv` context, CPython 3.12.2**; real operations used are
`+ - * /`, `exp`, `cos`, `sin`, `sqrt`, integer powers; complex operations are built
from those by hand (`csinh`, `ccosh`, complex `* /`, `abs2` in `s3_certificate`'s §6
companion). mpmath's `iv` context documents outward rounding for these, but this note
does not prove it, and no independent audit of the backend was done.

**Consequence, stated plainly: this artifact does not meet the draft's own
"all operations are rational" standard.** Closing that gap means either re-running
the enclosure in `Fraction` arithmetic with explicit rational bounds for `exp`/`cos`/
`sin` (a real but bounded piece of work — the margins in §1 are enormous, so a coarse
rational envelope would suffice), or amending the standard. Until then the certificate
is "rigorous modulo the interval library", which is the ordinary standard for
computer-assisted proofs but is *not* what the draft advertised.

## 7. ACCEPTED — scope and naming (issue 8)

The review is right that "(S3) certificate" risks interface drift: at `m = 561` the
W7 band runs to `0.89m = 499.29`, and nothing here touches `w > 40`. **The proved
object is the W1–W6b component of Lemma SOL.3, and nothing more.** The parent note's
title has been amended accordingly; no consumer may cite it as (S3), nor as the full
joint-cancellation statement.

## 8. Net status

The certificate's mathematics survived cross-model review with no error found, and
five of eight issues are repaired above. What remains is one genuine standard
question (§6) and the unchanged fact that (S3) is blocked in W7 — where the Sol
maths pass on the draft itself found an *unproved sign hypothesis* (`B >= 0`), a
mathematical gap rather than a computational one (`s3_maths_referee_response_20260812.md` §4).

**(S3) remains OPEN.** Its compact-band half is now executed, corrected, and
adversarially reviewed cross-model; its W7 half is not.
