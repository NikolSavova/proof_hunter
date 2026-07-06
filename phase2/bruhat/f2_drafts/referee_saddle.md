# Referee report — `draft_saddle.md` (Theorem F2, saddle-point/tilting route)

Adversarial referee pass, 2026-07-06. Every NUMERIC CHECK line was re-run against the
exact harness `mahonian.py` (plus independent adversarial computations). Verdict at the
end. Honest author-marked GAPs (GAP-1..5) are noted but not counted as flaws; unmarked
defects are.

**Bottom line.** The framework is genuinely strong — the tilt-invariance observation
(Lemma 4.1) plus the two fully-proved hyperbolic inequalities (Lemmas 4.2, 4.3) are the
best ideas I have seen for the global part of F2, and the numerics are almost all
impeccable (18 of 22 checks reproduce to the stated precision). The part-(c) finding
that the spec's suggested constant c = 7/8 is **false** (exactly 187/216 at m = 6) is
verified and correct. However, the proof of the headline Theorem 5.1 has an **unmarked
coverage hole** in the global synthesis (step 3): even granting GAP-2 and GAP-3 as
stated, an annulus of k (λ ∈ [1/m, ≈3.7/m]; 61 values of k at m = 30) is covered by
neither Lemma 4.5(i) nor Lemma 4.5(ii), and the draft's "overlap verified numerically"
claim rests on a quantitative confusion (details in Flaw F2). Lemma 2.2's stated
remainder bound is false for 6 ≤ m ≤ 29 (Flaw F1). So (a) is not "proved modulo GAP-2,
GAP-3" as the status summary claims; it is proved modulo GAP-2, GAP-3 **and** two
repairable but unflagged holes.

---

## 1. Numeric checks (all re-run; pass/fail)

| # | Location | Claim | Result |
|---|----------|-------|--------|
| 1 | Lemma 1.2 NC (snippet) | P(10) integral = exact = 0.0618303571 (m=8) | **PASS** (both 0.061830357142857) |
| 2 | Lemma 1.2 NC | exact P/D at k=10,14: 0.0618303571 / 2.227e-4; 9.514e-2 / 4.658e-4 | **PASS** (2.2272e-4, 0.0951388889, 4.6577e-4) |
| 3 | Lemma 1.2 NC | D double-integral matches exact at k=10,14 | **PASS** (rel. diff 3.6e-14, 1.5e-13 on 1200² midpoint grid) |
| 4 | Lemma 2.3 NC | m=30: max |phi| on [2π/m, π] = 6.3e-13 | **PASS** (6.31e-13) |
| 5 | Lemma 2.3 NC | product bound pointwise, 20000-pt grid, 0 violations | **PASS** (0 violations; also 0 violations of the Gaussian bound on [0, 2π/m]) |
| 6 | Lemma 2.3 NC | 2e^{-0.1931·30} = 6.1e-3; exp(-σ²t²/2) at t=2π/m = 3.3e-8 | **PASS** (6.10e-3, 3.30e-8) |
| 7 | Lemma 3.1 NC | m=40: β = 0.002230, 12β = 0.02676 | **PASS** |
| 8 | Lemma 3.1 NC | m=40: max over |y|≤3 of Edgeworth deviation = 3.6e-3 | **PASS** (3.56e-3) |
| 9 | Lemma 3.2 NC (center) | table m=6,10,20,30,40 and m=5 residual 0.028 | **PASS** (all five rows + m=5 reproduce to all printed digits; residual·m² ∈ [-0.19, +0.19]) |
| 10 | Lemma 3.2 NC (window) | m=40: max residual 3.8e-2, and "≤ 0.4(1+y⁶)/m² on the whole range" | **PARTIAL FAIL** — max residual 3.776e-2 confirmed, but the pointwise bound 0.4(1+y⁶)/m² is violated at **56 values of k** (residual ≈ 5.8e-4 vs bound ≈ 3-5.4e-4 near |y| ≈ 0.75–1.03). Needed constant ≈ 0.69, not 0.4. See F4. |
| 11 | Cor 3.3 NC | predicted varfit 0.97338 vs harness 0.973381; 1−27/1000 = 0.973 | **PASS** (predicted 0.973381; harness 0.973381) |
| 12 | Lemma 4.3 NC | grid scans: v increasing, u decreasing on (0,20], step 0.005; both series inequalities nonneg | **PASS** (0 violations, all four scans) |
| 13 | Lemma 4.4 NC | m=30, k=210: λ=0.00956, λσ²=7.51, deficit 1.98 vs 2.01, κ₄(0)=−43949.7 | **PASS** (λ=0.00956, λσ²=7.51, deficit 2.00 exact — the draft's 1.98 is a subtraction of rounded values — vs 2.01; κ₄(0) = −43949.74 = −(S₄(30)−30)/120) |
| 14 | Lemma 4.5 NC (table) | 6 rows at m=30 | **PASS** (all rows reproduce; the "−0.058" at k=120 is the residual s²logr − (1−12β_λ) = 0.96060 − 1.01850, consistent) |
| 15 | Lemma 4.5 NC (inline) | "|E₂| ≤ 2e-3 for k ≥ 200" | **FAIL (marginal)** — max |E₂| over k=200..217 is 2.19e-3, at k=200. 10% over the stated bound. |
| 16 | Lemma 4.5 NC (global min) | min over ALL interior k of σ_λ² log r = 0.668/0.678/0.683/0.685 at m=12/20/30/36, at k=1 | **PASS** (0.668, 0.678, 0.683, 0.685, all at k=1, σ_λ² ≈ 1.03–1.07) |
| 17 | Lemma 4.6 NC | m=40: r(1..12) values and margins over 1+1/(2k); r < (k+1)/k | **PASS** (1.9525, 1.4652, 1.3030, 1.1739, 1.1020, 1.0628; margins +0.453, +0.215, +0.136, +0.074, +0.039, +0.021; all below (k+1)/k) |
| 18 | GAP-4 NC | unimodality of r_m(k), exact, 5 ≤ m ≤ 56: zero violations; m=4: one violation at k=2 | **PASS** (exactly as claimed) |
| 19 | §5.3.1 NC | σ²(r₅−1)=7/8 and σ²(r₆−1)=187/216 exactly; varfit 0.8750/0.8657/0.8766; increasing on 6..56, decreasing at 5→6 | **PASS** (exact rationals confirmed; strictly increasing 6..56; 187/216 < 7/8). **The disproof of the spec's c = 7/8 is correct.** |
| 20 | §6 consolidated script | expected outputs | **PASS** (verbatim run reproduces `5 7/8`, `6 187/216`, the residual table, `unimodal OK 5..56`) |
| 21 | Thm 5.2 (empirical sentence) | "argmin is exactly floor(N/2) for all 4 ≤ m ≤ 56" | **FAIL at m=4** — argmin = 2, floor(N/2) = 3 (harness line: m=4, argmin 2, mid 3). See F5. |
| 22 | Lemma 2.2 (adversarial, statement check) | R₂(t) ≤ m⁷t⁶/952560 on |t| ≤ π/m | **FAIL for 6 ≤ m ≤ 29** — via the exact positive series R₂ = Σ_{r≥3} a_r (t/2)^{2r} Σ_j (j^{2r}−1): max R₂/bound = 1.51 (m=6), 1.34 (m=8), 1.24 (m=10), 1.11 (m=15), 1.05 (m=20), 0.99 (m=30), 0.96 (m=40), worst at t = π/m. See F1. |

Score: 18 clean passes, 4 fails (2 substantive: #10, #22; 2 minor: #15, #21).

---

## 2. Unmarked flaws

### F1 (Lemma 2.2 — stated remainder bound is false for 6 ≤ m ≤ 29). *Wrong constant.*
The failing step is in the proof: "the r ≥ 3 tail is at most sum_j (jt/2)^6/(2835·(1 − 1/4))",
followed by the substitution of `(4/3)·(m^7/7)` for `(4/3)·Σ_{j=2}^m j^6`. But
Σ_{j=2}^m j⁶ = m⁷/7 + m⁶/2 + O(m⁵) > m⁷/7 for every m ≥ 2 (e.g. m=8: 446,957 vs
2,097,152/7 = 299,593). The 4/3 slack absorbs this only for m ≳ 30: computing R₂
through its exact positive series shows the stated bound `R_2(t) <= m^7 t^6 / 952560`
is **violated by up to 51%** at t = π/m for m = 6..29 (table in check #22 above; no
floating cancellation — the series has positive terms). The lemma carries no m₀
restriction, so it is false as stated. Trivial fix: replace m⁷/7 by (m+1)⁷/7 (or by
Σ j⁶ ≤ ((m+1)⁷−1)/7), i.e. bound ≈ (m+1)⁷t⁶/952560. Downstream uses (Lemma 3.1) are
asymptotic, so nothing else breaks — but a stated lemma that fails for 24 values of m
in the harness range is a flaw, and this is exactly the kind of constant that GAP-5
says must eventually be chased for (c).

### F2 (Theorem 5.1, step 3 — coverage hole between Lemma 4.5(i) and 4.5(ii)). *The serious one.*
Lemma 4.5(i) is stated **only for |λ| ≤ 1/m**. The crude bound 4.5(ii),
σ_λ² log r ≥ 2/3, implies log r(k) > log r_c only when σ_λ² ≤ (2/3)/log r_c ≈
(2/3)σ²/(1−12β) ≈ 0.69 σ². But at λ = 1/m the relative variance deficit is only
≈ 12c₄/(m²σ⁴)·σ² ≈ 3% (m=30: σ_λ² = 761 at λ = 0.125·… — see numbers below), nowhere
near 31%. Quantitatively at m = 30 (exact harness + bisection for λ(k)):

- 4.5(i) as stated covers k ≥ 192 (λ ≤ 1/30 = 0.0333);
- 4.5(ii) suffices only for k ≤ 130 (σ_λ² ≤ 543);
- **k = 131..191 (61 values, λ ∈ [0.034, 0.125]) are covered by neither.**

The draft's justification — "the two regimes overlap because 4.5(i) stays valid while
lambda <= 1/m … (Overlap verified numerically above: at m=30 the sharp form is still
accurate at k=200 … and the crude form already has 40% slack there)" — conflates two
different things. At k = 200 the crude bound *holds* with 40% slack
(σ_λ²·log r = 0.964 ≥ 2/3), but it does **not suffice** for the synthesis:
(2/3)/σ_λ² = 8.61e-4 < log r_c = 1.228e-3. The bound that must be exceeded is the
central value, and the crude constant 2/3 is 30% *below* it throughout the annulus.
The λ-window of the hole is [1/m, ≈3.7/m] for every m (both endpoints scale as 1/m),
so it does **not** vanish as m → ∞. This is a genuine gap in the proof of the main
theorem that is not covered by GAP-2 or GAP-3 (those flag the *proofs* of 4.5(i)/(ii),
not the fact that their stated ranges fail to tile the line). Likely repair: restate
4.5(i) for |λ| ≤ K/m with a fixed K ≈ 4–5 (the same machinery works: jλ/2 stays O(1)),
and re-derive Lemma 4.4's deficit bound on the same range; but as written, Theorem 5.1's
step 3 does not close even granting all flagged GAPs.

### F3 (Theorem 5.1, step 2 — inner-edge margin argument is invalid as stated).
The failing sentence: "the margin `12 beta y^2 = 1.08 y^2/m` beats `C(1+y^2)/m^2` for
every such `y` because both scale linearly in `y^2`, with a factor-`m` gap in the
constants." The "+1" in C(1+y²)/m² does **not** scale with y²: at the inner edge
y² = y*² = 1/m the claimed margin is 1.08/m² while the error allowance is
≈ C/m² + C′/m² (window error plus central error). The exclusion therefore requires
C + C′ < 1.08, i.e. precisely the explicit constants that GAP-1/GAP-2 do not provide —
the "factor-m gap" claim is simply false at y ≍ m^{-1/2}. (Empirically it would squeak
through: the needed window constant is ≈ 0.71 and the central one ≈ 0.19, summing to
0.90 < 1.08 — but with ≤ 20% headroom, not a factor of m.) Consequence: as written,
steps 2–4 do not exclude |y| ≤ A m^{-1/2} for a constant A depending on the unchased
constants. The *value* conclusion of Theorem 5.1 survives (inside |y| ≤ A m^{-1/2},
Lemma 3.2 already gives σ² log r = 1 − 12β + O(m^{-2})), and Theorem 5.2 survives with
its constant C reinterpreted — but the draft should have flagged that the region-1/
region-2 boundary only works with a constant-dependent enlargement, not "for every
such y".

### F4 (GAP-1 index — the quoted empirical constant is false).
"numerically `|E_1| <= 0.4 (1+y^6)/m^2` for `6 <= m <= 40`" fails: at m = 40 there are
56 values of k in |y| ≤ 3 violating it (worst ratio ≈ 1.9× at |y| ≈ 0.8–1.0); the
needed constant is ≈ 0.72 (m=10), stabilizing at ≈ 0.69 for m = 20..40. The (1+y⁶)
shape under-weights the mid-window where the true next-order term is y²-dominated. The
y = 0 specialization used in the §5.3.2 reduction ("|E_1(0)| <= 0.4/m^2") **is**
supported (max |E₁(0)|·m² = 0.19 over 6 ≤ m ≤ 40), so the (c)-reduction itself is
numerically consistent — but the GAP-1 index line, which is exactly what a
constant-chaser would take as the target, is wrong as stated.

### F5 (Theorem 5.2 — false empirical sentence at m = 4; internal inconsistency).
"Empirically the argmin is exactly `floor(N/2)` for all `4 <= m <= 56`" is false at
m = 4: argmin = 2, floor(N/2) = 3 (r₄(2) = 25/18 < r₄(3) = 36/25). The draft itself
knows this — GAP-4's check reports "m=4 also has argmin at |k − N/2| = 1" — so this is
an internal inconsistency. (The frozen spec's parenthetical "argmin = floor(N/2) for
all 4 <= m <= 40" has the same error; the |k − N/2| ≤ 1 tolerance of F2(b) is what
actually holds at m = 4. Worth reporting upstream.) Statement should start at m = 5.

### F6 (Lemma 4.3 — sign slip in the displayed equivalence; conclusion unaffected).
"equivalent to `g(x) = x v'(x) - 2 v(x) = -2 x^3 csch^2(x) coth(x)` being
**nonincreasing**, i.e. to `u(x) = x^3 cosh x / sinh^3 x` being **nonincreasing**" —
since g = −2u, these two are opposite conditions; what the deficit-monotonicity
actually needs is g **nondecreasing**, equivalently u nonincreasing. u is indeed
nonincreasing (verified: the reduction to 3 sinh y ≤ y cosh y + 2y and its termwise
proof are correct, and the grid scan passes), so the lemma is true and proved; only
the word "nonincreasing" attached to g is wrong. Typo-level, but in a "fully proved"
lemma it should be exact.

### F7 (Lemma 3.1 sketch — log-power bookkeeping).
The sketch bounds |θ| ≤ R₂ + (c₄t⁴)²e^{c₄t⁴} "= O(m^{-2} log^3 m) uniformly" on
[0, t₂]. At t₂ = √(6 log m)/σ, (c₄t₂⁴)² = (36 β log²m)² ≈ 10.5 log⁴m/m² — the uniform
bound is log⁴, not log³. (A Gaussian-weighted integration of θ gives O(m^{-2}) with no
logs at all, so the *stated* remainder in Lemma 3.1 is true; but the sketch as written
does not deliver it.) Borderline GAP-1 territory; noted because GAP-1 is described as
a "constant chase" while this is a (small) structural repair.

---

## 3. The CJZ transfer (spec's specific worry)

Properly handled. The draft does **not** apply Canfield–Janson–Zeilberger's Theorem
4.6 (which is for the central Gaussian binomial) to the q-factorial; it cites CJZ only
as the source of the kernel device and re-derives the analogue from scratch: Lemma 1.1
(exact inversion, verified to 14 digits), Lemma 1.2 (exact second-difference kernel,
verified to 13 digits), Lemma 2.2 (its own cf expansion for [m]_q!), Lemma 3.2 (its
own Edgeworth transfer). No illegal borrowing. Caveat: Lemma 3.2's proof is a sketch
whose completion is filed under GAP-1, and GAP-1's label ("explicit constants in the
Edgeworth remainders") slightly undersells what is missing — the (u,v) box-splitting,
the v-moment ratio computation `<v^2(1-cos v)>/<1-cos v> = 3 tau^2 (1+O(tau^2))`
(I verified the Gaussian-moment algebra is right at leading order), and the division
bookkeeping are all unproven structure, not just constants. The center-table numerics
(residual·m² ∈ [−0.19, +0.19] for m = 6..40) strongly support the claimed O(m^{-2})
form, including the sign-consistent sharpening 1 − 27/(25m).

## 4. Parts (b) and (c): established vs asserted

- **(a)** Claimed "proved modulo GAP-2, GAP-3". **Not accurate as written**: also
  requires closing F2 (the 4.5(i)/(ii) coverage hole, unflagged) and F3 (inner-edge
  margin, unflagged). Both look repairable with the same machinery, but the honest
  status is "proved modulo GAP-2, GAP-3, an extension of 4.5(i) to |λ| ≤ K/m, and a
  constant-aware region-1/2 boundary". The sharpened constant 1 − 27/(25m) is
  correct (Cor 3.3 check passes to 6 digits, and I verified the 27/25 algebra
  independently: 12β = 12·5184·(m⁵/5)/(2880·4m⁶)·(1+5/(2m))(1−3/m) = (27/25)/m + O(m^{-2})).
- **(b)** The exact |argmin − N/2| ≤ 1 statement is **not established** — honestly
  declared: Theorem 5.2 proves only O(σm^{-1/2}) = O(m) (itself subject to F2/F3), and
  the upgrade is explicitly GAP-4 with an exact verification to m = 56. Honest gap,
  noted, not counted. But the spec's part (b) remains open in this draft.
- **(c)** **Not achieved and honestly said so** (GAP-5). What *is* established under
  (c) is negative and valuable: the exact computation σ²(r₆−1) = 187/216 < 7/8
  (verified in exact rationals) refutes the spec's suggested constant and its implied
  monotonicity-from-m=5; the corrected conjecture (c = 187/216, equality at m = 6) and
  the safe-target reduction (c = 5/6 given GAP-1..3 + finite harness run, with the
  legitimate proviso m₀ ≤ 56 or an extended run) are clearly framed as conditional.
  No overclaim here.

## 5. Honest GAPs (noted, not counted)

GAP-1 (Edgeworth constants — but see F4: its quoted numeric target constant 0.4 is
wrong, and see §3: it hides some structure, not only constants), GAP-2 (tilted-frame
bookkeeping), GAP-3 (uniform crude LCLT bound — note the constant 2/3 is razor-thin
globally: the true min over *all* interior k is 0.668 at m=12, i.e. 0.2% above 2/3;
the σ_λ² ≥ V₀ restriction is what buys room, and any closure must use it), GAP-4
(unimodality of r_m(k)), GAP-5 (explicit m₀ for (c)). All are genuinely flagged where
they are used; the synthesis correctly conditions on them — except at the two points
F2, F3 where unflagged reasoning fills what a GAP should have.

## 6. Things checked and found sound (selection)

- Lemma 1.1/1.2 exact representations: verified numerically to 1e-13; the derivations
  (inversion on the shifted lattice; symmetrization to the 1−cos(s−t) kernel) are
  correct, including the half-integer-x case for N odd.
- Lemma 2.1: a_r = ζ(2r)/(rπ^{2r}), values 1/6, 1/180, 1/2835 and the termwise ratio
  bound — all correct.
- Lemma 2.2's Gaussian upper bound 0 ≤ φ(t) ≤ e^{-σ²t²/2} on |t| ≤ 2π/m: correct
  (all-positive coefficients argument is valid; grid scan clean).
- Lemma 2.3: product bound and 2e^{-0.1931m} derivation: correct (sum-vs-integral for
  the increasing summand gives the claimed direction; grid scan clean).
- Lemma 4.1 (tilt invariance + μ′ = −σ_λ²): correct, and it is the structural heart of
  the paper.
- Lemma 4.2 (tilted variance domination): the reduction to v increasing and the
  termwise power-series verification (3^{2n+1}+9 ≥ 12(2n+1), equality n=0,1) are
  correct in full detail. Fully proved as claimed.
- Lemma 4.3: fully proved modulo the F6 sign typo.
- Lemma 4.4: expansion and both checks verified (κ₄(0) = −(S₄−m)/120 confirmed).
- Lemma 4.6: the Bonferroni cap-count and the binomial-ratio algebra
  (k+1)(m+k−2)/(k(m+k−1)) are correct; r(1) = 2(m−1)²/((m−2)(m+1)) ≥ 3/2 checks out.
- Symmetry r(N−k) = r(k): correct.
- §5.3.2's arithmetic: 1 − 27/200 − 0.4/64 = 0.859 > 5/6 at m = 8: correct, and its
  dependence on GAP-flagged inputs is explicit.

## 7. Verdict

**Major gaps** — but of an unusually reparable kind. The two fully-proved hyperbolic
lemmas (4.2, 4.3) plus tilt invariance (4.1) constitute a real, checkable mechanism
for the global part (the spec's "genuinely new part"), and every quantitative claim
that could be tested against the exact harness passed except four (two of them
substantive: the false Lemma 2.2 constant, valid only for m ≥ 30; and the false
empirical constant in the GAP-1 index). The unmarked coverage hole F2 means Theorem
5.1 is not yet a proof-modulo-flagged-gaps; together with F3 it is
proof-modulo-flagged-gaps-plus-two-unflagged-holes. Part (b) exact and part (c) are
open (honestly). The refutation of the spec's c = 7/8 is a correct and useful
contribution and should be propagated back into the spec regardless of what happens
to the rest of the draft.

Priority repairs, in order:
1. Extend Lemma 4.5(i) + Lemma 4.4 to |λ| ≤ K/m (K ≈ 5) and redo step 3's hand-off
   (fixes F2).
2. Make the region-1/region-2 boundary constant-aware: exclude |y| ≥ A m^{-1/2} and
   absorb |y| ≤ A m^{-1/2} into the center estimate (fixes F3).
3. Restate Lemma 2.2 with (m+1)⁷/7 (fixes F1); restate GAP-1's target constant as
   ≈ 0.75(1+y⁶)/m² or reshape to (1 + y² + y⁶) (fixes F4).
4. Start Theorem 5.2's empirical sentence at m = 5 (fixes F5); fix the g/u sign wording
   in Lemma 4.3 (F6); "log³m" → weighted-integration argument in Lemma 3.1 (F7);
   "2e-3" → "2.2e-3" in Lemma 4.5's NC (check #15).
