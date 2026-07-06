# Theorem F2 — draft via the elementary / exact-recurrence route

**Angle.** Use the product structure `[m]_q! = [m-1]_q! · (1+q+...+q^{m-1})`, i.e. the exact
convolution `I_m = I_{m-1} * u_m` with the length-`m` uniform block, to get *exact identities*
for the log-concavity defect, and run an induction on `m` that tracks how convolving with a
uniform block degrades the minimal second difference of `log I_m`. Fourier/local-CLT input is
used **only** for the upper half of part (a) and for the location statement (b), where it is
genuinely needed (see §6, §7).

**Status summary (honest):** part (c) is reduced to a single one-step convolution lemma
(Theorem 4.2) whose sharp form is verified numerically in three independent ways and matches an
exact fourth-cumulant computation, but whose proof here has two gaps (GAP 1, GAP 2). Part (a)
= (lower half from the same induction) + (upper half by the CJZ characteristic-function
transfer, remainder constants not executed: GAP 3). Part (b) is proved exactly for
`5 ≤ m ≤ 40`, localized to `|k−N/2| = O(√m)` conditionally (GAP 4), and open at full strength
(GAP 5). **One correction to the spec's ground-truth remark is proved exactly in §5.3: the
constant `c = 7/8` in part (c) is false at `m = 6`; the sharp constant for all `m ≥ 5` is
`c = 187/216`, attained at `m = 6`.**

Throughout, `mahonian.py` is the exact ground truth; every NUMERIC CHECK line below has been
run and passes (commands are collected in §8.2).

---

## 1. Setup and exact preliminaries

Write `a_m(k) := I_m(k)`, `N = N_m = m(m−1)/2`, and let
`u_m = (1,1,…,1)` (length `m`). Define

* the **ratio sequence** `ρ_m(k) = a_m(k+1)/a_m(k)`;
* the **curvature** `g_m(k) := log r_m(k) = 2 log a_m(k) − log a_m(k−1) − log a_m(k+1)
  = −Δ² log a_m(k) = log ρ_m(k−1) − log ρ_m(k)`, for `1 ≤ k ≤ N−1`;
* `c_m := r_m − 1 = min_{1≤k≤N−1} r_m(k) − 1`, so `c_m = e^{min_k g_m(k)} − 1`.

**Lemma 1.1 (product structure).** For `m ≥ 2`,
`a_m(k) = Σ_{t=0}^{m−1} a_{m−1}(k−t)` (convolution with `u_m`), hence the exact first-difference
recurrence
```
a_m(k+1) − a_m(k) = a_{m−1}(k+1) − a_{m−1}(k+1−m).            (1.1)
```
*Proof.* `[m]_q! = [m−1]_q! (1+q+…+q^{m−1})`; compare coefficients. ∎

**Lemma 1.2 (symmetry, moments, cumulants).** `a_m(k) = a_m(N−k)`; `a_m` is log-concave with
contiguous support `[0,N]` (Bóna, *Electron. J. Combin.* 11(2) (2004/05), #N2; alternatively
product-closure of log-concavity: Hoggar 1974, Kook 2006), hence unimodal with maximum at
`⌊N/2⌋` (and `⌈N/2⌉`). Writing `inv = Σ_{j=1}^m U_j` with independent `U_j ~ Unif{0,…,j−1}`:
```
σ_m² = Σ_j (j²−1)/12 = m(m−1)(2m+5)/72,
σ_m² − σ_{m−1}² = (m²−1)/12                                    (exact),   (1.2)
κ₄(U_j) = −(j⁴−1)/120,   κ₄,m := κ₄(inv) = −Σ_{j=1}^m (j⁴−1)/120,        (1.3)
|κ₄,m| / (2σ_m⁴) = (27/25) m^{−1} (1 + O(m^{−1})).                        (1.4)
```
*Proof.* Symmetry: `inv(σ) + inv(σ·w₀) = N`. (1.2): direct algebra,
`m(m−1)(2m+5) − (m−1)(m−2)(2m+3) = 6(m−1)(m+1)`. (1.3): for `U ~ Unif{0..n−1}`,
`μ₂ = (n²−1)/12`, `μ₄ = (n²−1)(3n²−7)/240`, so
`κ₄ = μ₄ − 3μ₂² = −(n⁴−1)/120`; cumulants add. (1.4): `|κ₄,m| ~ m⁵/600`,
`2σ⁴ ~ m⁶/648`. ∎

NUMERIC CHECK: `κ₄(U_n) = −(n⁴−1)/120` verified exactly (rational arithmetic) for
`n ≤ 11`; expected: equality. (§8.2, check N7.)

---

## 2. Two exact identities for the defect

Fix `m`, write `b = a_{m−1}`, `a = a_m = b * u_m`, and set
```
T(k) := a(k)² − a(k−1)a(k+1)   (so r_m(k) − 1 = T(k)/(a(k−1)a(k+1)) ).
```
For a window position `k` put `q_t := b(k−t)` for `t = −1,0,…,m` (values of `b` on the
convolution window `[k−m+1, k]` plus one value beyond each edge).

**Lemma 2.1 (boundary formula — exact).** With `P := a(k) = Σ_{t=0}^{m−1} q_t`,
```
T(k) = P·E(k) + X(k),
E(k) = (q_0 − q_{−1}) + (q_{m−1} − q_m)
     = [b(k)−b(k+1)] + [b(k−m+1)−b(k−m)],
X(k) = (q_0 − q_m)(q_{−1} − q_{m−1}).                                   (2.1)
```
*Proof.* By (1.1), `a(k−1) = P − q_0 + q_m` and `a(k+1) = P + q_{−1} − q_{m−1}`; expand
`P² − (P − q_0 + q_m)(P + q_{−1} − q_{m−1})`. ∎

So the entire defect of `a` at `k` is carried by the four *edge values* of `b` around the
window: `E(k)` is the sum of the two inward edge increments (the "slope drop seen by the
window") and `X(k)` is a product of the two across-window increments.

NUMERIC CHECK: (2.1) as an integer identity for all `k`, `5 ≤ m ≤ 12`; expected: exact
equality. (§8.2, check N2. Passes.)

**Lemma 2.2 (Cauchy–Binet positivity decomposition).** For every `k`,
```
T(k) = Σ_{t=1}^{m} β_t(k) + Σ_{t=1}^{m−1} γ_t(k),
β_t(k) = b(k)b(k+1−t) − b(k+1)b(k−t),
γ_t(k) = b(k+1−m)b(k−t) − b(k−m)b(k+1−t),                                (2.2)
```
and **every summand is ≥ 0** when `b` is log-concave with contiguous support.

*Proof.* Identity: `Σ_t β_t = b(k)·a(k) − b(k+1)·a(k−1)` and
`Σ_t γ_t = b(k+1−m)·a(k−1) − b(k−m)·a(k)`; summing and using (1.1) twice gives
`a(k)[a(k)−a(k−1)] − a(k−1)[a(k+1)−a(k)] = T(k)`. Positivity: each bracket has the form
`b(i)b(j) − b(i+1)b(j−1)` with `i < j` shifted toward each other, which is ≥ 0 for a
log-concave sequence with no internal zeros (PF₂ two-by-two minors; this is the Toeplitz
Cauchy–Binet decomposition of the 2×2 minor of `M_a = M_b M_{u_m}`, and the `u_m`-minors that
survive are exactly the pairs `(0,t)` and `(t,m)`, each equal to 1). ∎

NUMERIC CHECK: identity (2.2) and term-by-term nonnegativity for all `k`, `5 ≤ m ≤ 12`;
expected: exact equality, all brackets ≥ 0. (§8.2, check N3. Passes.)

**Lemma 2.3 (weighted transfer bound).** Suppose `b` is log-concave and
```
ρ_b(j−1) ≥ (1+c) ρ_b(j)  for all j (curvature ≥ c̃ := log(1+c) everywhere).      (H_c)
```
Then for every `k` (terms with a zero factor read as 0):
```
T(k) ≥ Σ_{t=1}^{m} b(k+1) b(k−t) [(1+c)^t − 1]
     + Σ_{t=1}^{m−1} b(k−m) b(k+1−t) [(1+c)^{m−t} − 1].                  (2.3)
```
*Proof.* Rewrite `β_t = b(k)b(k−t)[ρ_b(k−t) − ρ_b(k)]` and use
`ρ_b(k−t) ≥ (1+c)^t ρ_b(k)`; similarly
`γ_t = b(k−m)b(k−t)[ρ_b(k−m)... ] ≥ b(k−m)b(k+1−t)[(1+c)^{m−t} − 1]` from
`ρ_b(k−m) ≥ (1+c)^{m−t} ρ_b(k−t)`. All discarded terms are ≥ 0 by Lemma 2.2. Moreover (2.3)
holds **with equality** when `log b` is exactly quadratic (all curvature gaps equal to `c̃`)
on the window — the bound is *sharp on the Gaussian-profile family*. ∎

---

## 3. Elementary a priori bounds (no Fourier)

These are used to control the regime of the one-step lemma. `M := a(⌊N/2⌋) = max_k a(k)`,
`S := Σ_k a(k) = m!`, `σ = σ_m`. Constants are deliberately crude; all statements are for
`m ≥ 12` (the harness covers `4 ≤ m ≤ 40` exactly).

**Lemma 3.1 (mass–width).** `S ≥ Mσ/6`.

*Proof.* Let `s* = max{s : a(⌊N/2⌋−s) ≥ M/e}` and `w = s*+1`. Values within `±s*` of the
center are ≥ M/e (unimodality), so `S ≥ (2s*+1)M/e ≥ 0.67 w M` for `w ≥ 5`. Beyond, log-concavity
through the two points `(0, log M)`, `(w, ≤ log M − 1)` forces geometric decay with ratio
`≤ e^{−1/w}`, whence `Σ_{|x|>s*} x² a(⌊N/2⌋+x) ≤ 10 M w³` and `Σ_{|x|≤s*} x² a ≤ (2/3)Mw³`;
so `σ² S ≤ 11 M w³`, i.e. `w ≥ (σ²S/11M)^{1/3}`. Combining, `S ≥ 0.67 M (σ²S/11M)^{1/3}`,
i.e. `S² ≥ (0.67³/11) M²σ² S²/S·…` ⇒ `S ≥ 0.165 Mσ ≥ Mσ/6`. (If `w ≤ 4` then
`σ² S ≤ 11M·125` forces `σ` bounded, excluded for `m ≥ 12`.) ∎

**Lemma 3.2 (central value bound).** With `W := ⌈σ/2⌉`:
`a(⌊N/2⌋ ± W) ≥ e^{−2} M`.

*Proof.* Suppose `a(⌊N/2⌋−W) < e^{−2}M`. Log-concavity forces decay rate ≥ `2/W` per step
beyond distance `W`, so the second moment carried beyond `±W` is at most
`2·e^{−2} M · Σ_{j≥0}(W+j)² e^{−2j/W} ≤ 1.25·2e^{−2} M W³ ≤ 0.05 Mσ³(1+O(1/σ))`.
But `σ²S = Σx²a ≤ W²S + Σ_{|x|>W}x²a` gives
`Σ_{|x|>W}x²a ≥ S(σ² − W²) ≥ 0.7 Sσ²` (as `W ≤ σ/2 + 1`). Hence
`0.7 Sσ² ≤ 0.06 Mσ³`, i.e. `S ≤ 0.09 Mσ`, contradicting Lemma 3.1. The `+W` side is symmetric. ∎

**Lemma 3.3 (elementary upper bound on the minimal curvature).** For `m ≥ 12`,
```
c_m ≤ min_k g_m(k) ·(1+c_m/2) ≤ 18/σ_m².                                   (3.1)
```
*Proof.* The triangular-weight summation-by-parts identity (exact, telescoping twice):
```
Σ_{x=−W+1}^{W−1} (W−|x|) · g_m(⌊N/2⌋+x) = log [ a(⌊N/2⌋)² / (a(⌊N/2⌋−W) a(⌊N/2⌋+W)) ].  (3.2)
```
The weights sum to `W²`, so `min_k g_m(k) ≤ W^{−2} · RHS ≤ W^{−2}·(2·2+slop)` by Lemma 3.2
(with a `O(1/σ)` slop when `N` is odd, since then the two symmetric partners of
`⌊N/2⌋±W` sit one step off; absorbed in the constant). With `W = ⌈σ/2⌉`:
`min g ≤ 17/σ²` for `m ≥ 12`, and `c_m = e^{min g} − 1 ≤ 18/σ²`. ∎

NUMERIC CHECK: identity (3.2) at `m = 12`, `W = 8`; expected: equality to machine precision.
(§8.2, check N4. Passes.) Also the harness `varfit` column shows the *true* value
`c_m σ_m² ≤ 1` for all `4 ≤ m ≤ 40` — (3.1) is crude by a factor ≈ 18 but fully elementary.

GAP 6 (minor): Lemmas 3.1–3.3 are continuous-style arguments transcribed to the lattice; the
`±1` discretization slops are absorbed into generous constants but have not been written out
line-by-line. Routine.

---

## 4. The one-step convolution lemma (core of the elementary route)

### 4.1 What the sharp answer must be (Gaussian model, exact fourth-cumulant match)

Take `b_j = exp(−c̃ j²/2)` (curvature exactly `c̃` everywhere — by Lemma 2.3 this is the
extremal profile for all the inequalities of §2). Convolution with `u_m` adds variance
`(m²−1)/12` **and** fourth cumulant `κ₄(u_m) = −(m⁴−1)/120` (Lemma 1.2). A local expansion of
the convolution around its center gives, for the output minimal curvature `c'`,
```
1/c' = 1/c + (m²−1)/12 + (m⁴−1)/(240 v) + O(c²m⁸/v...) ,  v := 1/c̃ + (m²−1)/12,   (4.1)
```
i.e. the harmonic (variance) law **plus a positive excess ≈ c·m⁴/240** coming from the
platykurtic (`κ₄ < 0`) correction: the fourth-cumulant deficit *flattens the center*, and the
minimum of the curvature sits exactly where the flattening is maximal.

NUMERIC CHECK (three independent confirmations, §8.2 checks N5–N7; all pass):

1. **Gaussian one-step, measured:** for `b_j = exp(−j²/2s²)`, `s² ∈ {½,1,2}·σ_{m−1}²`,
   `m ∈ {8,…,40}`: measured `excess := 1/c' − 1/c − (m²−1)/12` satisfies
   `excess/(c m⁴) ∈ [0.0042, 0.0055]`, drifting to `1/240 = 0.004167` as `cm² → 0`. Expected
   from (4.1): `1/240`.
2. **Actual Mahonian steps:** `ε_m := 1/c_m − 1/c_{m−1} − (m²−1)/12 > 0` for all
   `5 ≤ m ≤ 45`, with `ε_m/m ∈ [0.038, 0.084]` and `ε_m/m → 0.061`. (So the *naive harmonic
   recursion `ε_m ≤ 0` is false* — the excess term in (4.1) is real and unavoidable.)
3. **Center value:** `σ_m²·c_m = 1 + κ₄,m/(2σ_m⁴) + O(m^{−2})`; measured vs. predicted:
   `0.9047 / 0.8920 (m=10)`, `0.9481/0.9466 (m=20)`, `0.9648/0.9644 (m=30)`,
   `0.9734/0.9732 (m=40)`.

### 4.2 The lemma

**Theorem 4.2 (one-step transfer; CONDITIONAL — see GAP 1, GAP 2).**
There are absolute constants `δ₀ ≥ 1` and `A₀` such that: if `b` is log-concave with
contiguous support and satisfies (H_c) with `c m² ≤ δ₀`, then `a = b * u_m` is log-concave,
satisfies (H_{c'}), and
```
1/c' ≤ 1/c + (m²−1)/12 + A·m,  where  A = A(c,m) := A₀ · c m³ .              (4.2)
```
*Sharp values (numerically supported, matching (4.1)):* `A₀ = 1/240·(1+o(1))`; a safe target
for a fully rigorous proof is `A₀ = 1/60` for `cm² ≤ 13` (4× headroom over everything
measured).

**Proof plan and status.**

*(i) Balanced windows (the sharp regime).* Call `k` *balanced* if all window slopes satisfy
`|log ρ_b(j)| ≤ θ/m` on `[k−m, k+1]` (`θ` a small absolute constant). Then with
`q_t = b(k−t) = q̄ e^{h_t}`, `|h| ≤ 2θ`, one expands the exact boundary formula (2.1) and the
denominator `a(k−1)a(k+1)` to second order in the slopes with explicit remainder `O(θ³)`.
At second order the inequality `T(k) ≥ c̃(1 − c̃(m²−1)/12 − A m c̃)·a(k−1)a(k+1)` becomes a
quadratic-form inequality in the slope vector `(λ_1,…,λ_m)`, `λ_t = log ρ_b(k−t)`, constrained
by `λ_t − λ_{t+1} ≥ c̃`. On the *extremal* family (all constraints tight: `log q` quadratic,
arbitrary linear part = window centering) the computation is exact and yields precisely
(4.1); this is where `(m²−1)/12` and `m⁴/240` come from:
`E/(P c̃) = m(1 − c̃m²/8 + …)`, `P²/(a(k−1)a(k+1)) = 1 + …`, `P/(m q̄) = 1 − c̃m²/24 + …`, and
`−1/8 − 1/24 + 1/12 = −1/12`.

GAP 1 (extremality). The reduction "the minimum of `T(k)/(a(k−1)a(k+1))` over all `q`
satisfying the curvature constraints is attained on the exactly-`c̃`-curved (Gaussian-profile)
family" is not proved. The natural route — monotonicity of the objective in each curvature gap
`γ_s = λ_{s−1} − λ_s` at fixed `(q_0, λ_0)` — is plausible (raising `γ_s` raises the exact
bracket weights in (2.3-exact) and lowers the denominator, but also lowers interior `q_t`); I
could not make the sign argument close.
NUMERIC CHECK: 4000 random admissible curvature profiles (`γ_s ≥ c̃`, random centerings) at
`m ∈ {10,20}`, `c̃ = 36/m³`: **none** beats the Gaussian minimum; the Gaussian minimum itself
gives `1/F − 1/c = 9.96` vs `(m²−1)/12 = 8.25` at `m=10` (excess `0.171m`), `36.45` vs `33.25`
at `m=20` (excess `0.160m`) — matching `A₀ ≈ 1/240` on the nose. (§8.2, check N6.)

*(ii) Unbalanced windows.* If some window slope exceeds `θ/m` in modulus, the window sees a
definite slope drop `D_k := log[b(k)/b(k+1)] + log[b(k−m+1)/b(k−m)] ≥ m c̃`, and one needs the
much weaker bound `T(k)/(a(k−1)a(k+1)) ≥ c'` with `c'` as in (4.2), for which there is slack:
* *steep windows* (`|slope|·m ≥ Θ`): the window sums `a(k−1), a(k), a(k+1)` are dominated by a
  boundary segment of length `O(m/Θ)`, and the mediant inequality
  `min_j ρ_b(j) ≤ ρ_a(k) ≤ max_j ρ_b(j)` (over the window) plus (H_c) pushes the curvature of
  `a` up to `≥ c̃(1 − O(e^{−Θ}))` — far above `c'`. Provable by the same boundary formula;
  constants not finalized.
* *moderately sloped, strongly kinked windows*: the kink heuristic `g_a(k) ≈ D_k/m` holds with
  a constant: measured `min_k m·g_a(k)/D_k ∈ [0.16, 0.35]` for `8 ≤ m ≤ 40` (worst at
  `k = m`, i.e. at the partition-like left tail — where `D_k ≫ mc̃`, so the target `c'` is
  still cleared by a wide margin).

GAP 2 (the seam). The two sub-regimes above have been analyzed but the uniform statement
"every unbalanced window satisfies `g_a(k) ≥ c'` with the constants of (4.2)" is not written
down with explicit constants; in particular the matching of the balanced-window remainder
`O(θ³)` against the slack available at the regime boundary `|slope| ≈ θ/m` needs the quadratic
profile growth of §7 and is the technically most delicate seam. **Empirically the global
minimum over `k` is always at the perfectly balanced central window** (§7, exact for
`m ≤ 40`), so the seam carries no actual risk, but it is unproven.

NUMERIC CHECK: window balance at the central window: `b`-values at the window edges over the
window maximum are `0.90` at `m=40` (`0.81` at `m=20`), i.e. the minimizing window is deep
inside the balanced regime. (§8.2, check N8.)

---

## 5. The induction: part (c) and the lower half of part (a)

**Theorem 5.1 (conditional on Theorem 4.2).** Fix `m₀ = 40`. Suppose Theorem 4.2 holds with
`A(c,m) ≤ A₁·m` along the Mahonian family for `m > m₀` (by Lemma 3.3, `c = c_{m−1} ≤ 18/σ_{m−1}²`
gives `A ≤ A₀·18·72m³/((m−1)(m−2)(2m+3)) ≤ 648·A₀·(1+5/m)`; with the *empirical*
`c_{m−1}σ_{m−1}² ≤ 1` it gives `A₁ = 36A₀(1+5/m)`). Set `K := 18 A₁`. Then
```
1/c_m ≤ σ_m² (1 + K/m)   for all m ≥ m₀.                                   (5.1)
```
*Proof.* Induction. Base `m = m₀ = 40`: by the harness, `σ²c_40 = 0.97337`, so
`1/c_40 = σ²/0.97337 ≤ σ²(1+K/40)` whenever `K ≥ 1.1` — true for every variant of `K` below.
Step: assume (5.1) at `m−1`. Theorem 4.2 and (1.2) give
`1/c_m ≤ σ_{m−1}²(1+K/(m−1)) + (m²−1)/12 + A₁ m`. Since
`σ_m²/m − σ_{m−1}²/(m−1) = (4m+1)/72` (exact), the step closes iff
`A₁ m ≤ K(4m+1)/72`, which holds with `K = 18A₁` because `72m/(4m+1) < 18`. ∎

**Corollary 5.2 (part (c)).**
```
r_m ≥ 1 + (187/216)/σ_m²   for all m ≥ 5,                                   (5.2)
```
with equality at `m = 6`; and `r_m ≥ 1 + (7/8)/σ_m²` for all `m ≥ 5` **except `m = 6`**.

*Status.* For `5 ≤ m ≤ 40` this is an exact finite verification (harness): `σ_m²(r_m−1)` equals
`7/8` at `m=5`, `187/216 = 0.86574…` at `m=6`, and is strictly increasing in `m` for
`6 ≤ m ≤ 40` (min over `m ≥ 5` is `187/216`, at `m = 6`). For `m > 40`: Theorem 5.1 gives
`σ²c_m ≥ 1/(1+K/m)`. With the sharp constants (`A₀ = 1/240` ⇒ `A₁ ≈ 0.15–0.2` ⇒ `K ≤ 3.6`):
`σ²c_m ≥ 1/(1+3.6/41) = 0.919 > 187/216` for all `m ≥ 41`, so (5.2) closes **conditionally on
Theorem 4.2 (sharp constants), i.e. on GAP 1–2.** With only the *proven* Lemma 3.3 feeding the
constants (`A₁ = 3`, `K = 54`), the induction still yields `σ²c_m → 1` but clears `187/216`
only for `m ≥ 349`; the range `41 ≤ m ≤ 348` would need a (feasible, exact, ~hours) extension
of the harness run — flagged as part of the conditional status, not done here.

**SPEC CORRECTION (exact).** The spec's ground-truth note "σ²(r_m−1) increasing, `= 0.875` at
`m=5`, so `c = 7/8` plausibly provable" is wrong at one point: the sequence is **not**
monotone at `m=5→6`. Exactly: `r_5 − 1 = 21/100`, `σ_5² = 25/6`, product `= 7/8`; but
`r_6 − 1 = 11/90`, `σ_6² = 85/12`, product `= 187/216 < 7/8`. So `c = 7/8` is **false for
m = 6** and the sharp uniform constant is `187/216`.
NUMERIC CHECK: exact rational computation of `r_5, r_6` and both products; expected:
`7/8`, `187/216`, and `r_6 − 1 < (7/8)/σ_6²`. (§8.2, check N9. Passes.)

**Corollary 5.3 (lower half of part (a)).** Conditionally on Theorem 4.2,
`σ_m²(r_m − 1) ≥ 1 − K/m` for `m ≥ 40`, hence `liminf σ²(r_m−1) ≥ 1`. ∎

Note the matching *upper* direction of the excess: the measured `ε_m/m → 0.061 = (27/25)/18·…`
is exactly what the `κ₄`-drift forces: if `σ²c_m = 1 − (27/25)/m + o(1/m)` (Numeric Check 3 of
§4.1), then `ε_m = (27/25)(σ_m²/m − σ_{m−1}²/(m−1))(1+o(1)) → (27/25)(4m/72) = 0.06m`. The
elementary induction is therefore *sharp to first order in 1/m*; no room is wasted.

---

## 6. Upper half of part (a): the central ratio (Fourier / CJZ transfer)

The elementary route cannot see the central ratio from above better than `O(1/(mσ))` (the
mediant/averaging bounds are lossy by the window width), so here we use the exact
characteristic function, as the spec prescribes.

**Lemma 6.1 (exact integral representation).** With
`F_m(t) := Π_{j=1}^m [ sin(jt/2) / (j sin(t/2)) ]` (real, even, `F_m(0)=1`):
```
a_m(k) = (m!/π) ∫_0^π F_m(t) cos((N/2 − k)t) dt,                          (6.1)
−Δ²a_m(k) = (m!/π) ∫_0^π F_m(t) (2 − 2cos t) cos((N/2 − k)t) dt.          (6.2)
```
*Proof.* `Σ_k a(k)e^{ikt} = m! e^{iNt/2} F_m(t)`; invert on the lattice; symmetrize. ∎

**Proposition 6.2 (central ratio; GAP 3 on remainder constants).**
```
r_m(⌊N/2⌋) − 1 = σ_m^{−2} (1 + O(1/m)),   in fact  = σ^{−2}(1 − (27/25)m^{−1} + O(m^{−2})). (6.3)
```
*Proof sketch.* `log F_m(t) = −σ²t²/2 + κ₄,m t⁴/24 + O(Σ_j j⁶ t⁶)` for `|t| ≤ t₀ := m^{0.6}/σ`.
Laplace evaluation of (6.1)–(6.2) at the center (`cos` factor `= 1` resp. `cos(t/2)` for `N`
odd) gives `−Δ²a/a = σ^{−2}(1 + O(1/m))`; for `N` even the exact algebra
`r(mid) − 1 = [(−Δ²a)·a − (Δ²a)²/4] / a(mid+1)²` (symmetry kills the first-difference term)
transfers this to the ratio, and for `N` odd `r(mid) = a(mid)/a(mid−1)` with
`a(mid)−a(mid−1)` given by (6.2)-type integrals. The tail `t ∈ [t₀, π]` is negligible:
`|F_m(t)| ≤ exp(−t²/24·Σ_{j≤π/t} j²)` gives superpolynomially small contributions relative to
`a(mid) ≍ m!/σ`. This is precisely the `[m]_q!` analogue of Canfield–Janson–Zeilberger
(arXiv:0908.2089), Theorem 4.6 / eq. (4.11), who prove the identical statement for the central
Gaussian binomial; their §4 estimates apply verbatim to `F_m` since `F_m` is a product of the
same Dirichlet-kernel factors.

GAP 3: the uniform explicit remainder (the `O(1/m)` in (6.3) with a named constant, and the
`O(m^{−2})` second term) is standard Edgeworth machinery (Petrov, *Sums of Independent Random
Variables*, Ch. VII, for lattice non-iid uniform summands) but has **not** been executed here
with explicit constants. The two-term form is confirmed numerically to 3–4 decimals
(§4.1, check 3). ∎

**Theorem 6.3 (part (a); conditional).** Combining `r_m ≤ r_m(⌊N/2⌋)` (trivially) with
Proposition 6.2 (upper) and Corollary 5.3 (lower):
```
r_m = 1 + σ_m^{−2}(1 + o(1)),  indeed  σ²(r_m−1) = 1 − Θ(1/m).
```
Status: upper half modulo GAP 3 (routine); lower half modulo GAP 1–2 (substantive). ∎

---

## 7. Part (b): location of the minimum

**Exact statement, verified range.** For every `5 ≤ m ≤ 40`, `argmin_k r_m(k) = ⌊N/2⌋`
exactly (up to the forced tie `⌊N/2⌋ ↔ ⌈N/2⌉` when `N` is odd). Stronger: the curvature
profile `g_m(⌊N/2⌋+x)` is *strictly increasing in x ≥ 0* — zero non-monotone steps — for
every `m ≤ 40`.
NUMERIC CHECK: both statements, exact arithmetic, `5 ≤ m ≤ 40`; expected: argmin `= ⌊N/2⌋`,
0 non-monotone steps. (§8.2, checks N1, N10. Pass.)

**Proposition 7.1 (asymptotic localization; conditional — GAP 4).** With the two-term local
expansion (the same machinery as Prop. 6.2 pushed one Edgeworth order further, remainder
`O(m^{−3})` relative), the curvature profile in the central window satisfies
```
g_m(⌊N/2⌋+x) − g_m(⌊N/2⌋) = σ^{−2} [ (27/25) m^{−1} (x/σ)² (1+o(1)) + O(m^{−3}) ],   (7.1)
```
so the argmin satisfies `|argmin − N/2| = O(√m)`.
NUMERIC CHECK: measured `(g(mid+x)/g(mid) − 1)·m·(σ/x)² ∈ [1.08, 1.25]` for `x ∈ [m, 3m]`,
`m ∈ {20,40}` — the quadratic-rise coefficient matches `27/25 = 1.08`. (§8.2, check N10.)

*Status and limits of the method.* (i) A fixed-order Edgeworth expansion can never resolve the
argmin below `|x| = Θ(σ/m) = Θ(√m)`: the quadratic gain `(27/25)(x/σ)²/m` falls below the
next-order remainder there. So the exact statement `|argmin − N/2| ≤ 1` is beyond this route.
(ii) Excluding the *tails* `|x| ≥ Cσ` as argmin locations requires a global profile lower
bound `g_m(k) > g_m(mid)` there; the conditional one-step machinery gives only the global
minimum value (§5), not its location, and the unbalanced-window analysis (GAP 2) gives
`g ≥ c'` — the right size but not strictly above the central value. A profile-carrying
induction (hypothesis `g_m(mid+x) ≥ c_m(1 + ν min(1, x²/(mσ²)))`) looks feasible with the
same tools but is not carried out.

GAP 4: remainder uniformity in (7.1) (same machinery as GAP 3, one order deeper) **and** the
tail exclusion just described.
GAP 5: part (b) at full strength (`|argmin − N/2| ≤ 1`, empirically exact `= ⌊N/2⌋`) is **not
proved** here for `m > 40`; what is available is: exact for `m ≤ 40`, `O(√m)` localization
modulo GAP 3–4, and the (numerically exact, unproven) profile monotonicity as the natural
target statement — monotonicity of `g_m` away from the center would give (b) immediately and
seems the right lemma to attack with the §2 identities (it is equivalent to single-signedness
of the *third* difference of `log a_m` on each half, a Toeplitz PF₃-flavored statement; the
Cauchy–Binet decomposition of the corresponding 3×3 minors is the natural elementary attack,
not attempted).

---

## 8. Proof-status ledger and numeric-check index

### 8.1 Status by part

| Part | Claim | Status |
|---|---|---|
| (a) upper | `r_m ≤ 1 + σ^{−2}(1+O(1/m))` | Proved modulo GAP 3 (routine Edgeworth constants; CJZ Thm 4.6 analogue) |
| (a) lower | `r_m ≥ 1 + σ^{−2}(1−K/m)` | Proved modulo Theorem 4.2 (GAP 1 substantive, GAP 2 technical) |
| (b) | argmin `= ⌊N/2⌋` (`±1`) | Exact for `m ≤ 40`; `O(√m)` localization modulo GAP 3–4; full claim OPEN (GAP 5) |
| (c) | `r_m ≥ 1 + c/σ²`, `m ≥ 5` | **Spec correction: sharp `c = 187/216`, not `7/8` (fails at `m=6`).** Exact for `m ≤ 40`; `m > 40` modulo Theorem 4.2 with sharp constants (else finite verification to `m = 348`) |

Everything unconditional and new here: Lemmas 1.2 (κ₄ closed form), 2.1, 2.2, 2.3, 3.1–3.3,
Theorem 5.1's mechanism (the `K = 18A` closure and the exact bookkeeping
`σ_m²/m − σ_{m−1}²/(m−1) = (4m+1)/72`), and the identification (4.1) of the sharp one-step law
including the `m⁴/240` excess — which explains *quantitatively* why the naive harmonic
induction fails (Numeric Check 2 of §4.1) and exactly how much room the induction has.

### 8.2 Numeric checks (all run against `mahonian.py`; `python3` from `phase2/bruhat/`)

* **N1** `python3 mahonian.py --mmax 40` — table: argmin central for all m; min ratio = central
  ratio for `m ≥ 5`; varfit column as quoted. PASSES.
* **N2** (Lemma 2.1) exact identity `T(k) = a(k)E(k)+X(k)` for all k, `m = 5..12`, integers. PASSES.
* **N3** (Lemma 2.2) identity + all brackets ≥ 0, `m = 5..12`. PASSES.
* **N4** (Lemma 3.3) triangular identity (3.2) at `m=12, W=8`, machine precision; varfit ≤ 1
  for `m ≤ 40`. PASSES.
* **N5** (Thm 4.2 sharp constants) Gaussian one-step: `excess/(cm⁴) ∈ [0.0042,0.0055] → 1/240`;
  Mahonian steps: `0 < ε_m ≤ 0.084·m` for `5 ≤ m ≤ 45`, `ε_m/m → 0.061`. PASSES.
* **N6** (GAP 1 support) 4000 random admissible curvature profiles at `m ∈ {10,20}`: none
  below the Gaussian minimum; Gaussian excess `= 0.171m, 0.160m`. PASSES.
* **N7** (Lemma 1.2) `κ₄(U_n) = −(n⁴−1)/120` exactly, `n ≤ 11`; varfit vs
  `1+κ₄/(2σ⁴)`: `0.9734` vs `0.9732` at `m=40` (etc.). PASSES.
* **N8** (Thm 4.2 regime) central-window balance `q_edge/q_max = 0.90` at `m=40`. PASSES.
* **N9** (Cor. 5.2) exact: `r_5−1 = 21/100`, `σ_5²(r_5−1) = 7/8`; `r_6−1 = 11/90`,
  `σ_6²(r_6−1) = 187/216 < 7/8`; `min_{5≤m≤40} σ²(r_m−1) = 187/216`; strictly increasing from
  `m=6`. PASSES.
* **N10** (part (b)) argmin `= ⌊N/2⌋` exactly and profile `g_m` strictly monotone away from
  center, `m ≤ 40`; quadratic-rise coefficient `≈ 27/25`. PASSES.

### 8.3 GAP register

* **GAP 1** (substantive): extremality of the exactly-`c̃`-curved profile in the one-step
  lemma (§4.2(i)). Strong numeric support; no proof.
* **GAP 2** (technical): uniform constants for unbalanced windows + the regime seam (§4.2(ii)).
* **GAP 3** (routine): explicit Edgeworth remainder constants in the central expansion (§6).
* **GAP 4** (routine+GAP3): same at one order deeper, plus tail-exclusion, for the `O(√m)`
  localization (§7).
* **GAP 5** (open): part (b) at full strength for `m > 40`; proposed attack: PF₃/3×3
  Cauchy–Binet for third-difference single-signedness.
* **GAP 6** (minor): lattice slops in §3 constants.

### References

* M. Bóna, *A combinatorial proof of the log-concavity of a famous sequence counting
  permutations*, Electron. J. Combin. 11(2) (2004/05), #N2.
* S. G. Hoggar, *Chromatic polynomials and logarithmic concavity*, JCTB 16 (1974). W. Kook
  (2006) for the product-closure route.
* E. R. Canfield, S. Janson, D. Zeilberger, *The Mahonian probability distribution on words is
  asymptotically normal*, Adv. Appl. Math. 46 (2011); arXiv:0908.2089 — Theorem 4.6 & eq. (4.11).
* V. V. Petrov, *Sums of Independent Random Variables*, Springer 1975, Ch. VII (Edgeworth for
  lattice arrays).
