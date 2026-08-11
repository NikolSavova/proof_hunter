# WP1-c — Lemma W: a sharpened tilted far-region bound (tilted Lemma-1.4 analogue) from the exact sinh/sin factor identity

*Blind-protocol note: written from `F2_PROOF_DRAFT.md` (merged draft),
`g1_draft_b.md` (refereed, SURVIVES WITH MINOR REPAIRS; B.0–B.9 citable),
`g2_draft_t2_20260803.md` (finalized T2 draft; its T.1–T.10 citable as scoped
there), `g2_item1_deep_tilt_notes_20260805.md` (diagnostic), and the harness
`mahonian.py` / the T2 verification script `g2_scripts/t2/t2_nc10_far.py`
(read only to replicate its threshold criterion verbatim). Nothing under
`g2_campaign_undefined/`, `g2_campaign_20260811/`, or `g2_draft_t1_*` was read.
All scripts for this draft live in
`f2_drafts/g2_scripts/campaign_undefined/wp1_c/` and were each run on
2026-08-11 (CPython 3, stdlib + mpmath); every number quoted below is from a
real run, outputs quoted in §7.*

**What this work package delivers (one paragraph).** The T2 draft's §8 names
one binding obstruction twice: item 5 (the proved tilted far-region exponents
`exp(-m_*/4730)` (T.7b-final) and `exp(-0.06 e^{-2K} m)` (T.7c) force refined-law
thresholds `m_2(1) ~ 7.3e3`, `m_2(4) ~ 5.1e6` against measured `e^{-0.19 m}`-class
truth) and item 1 (the band `lam in (pi/m, 1/2]` — and, per the diagnostic, up
to `lam ~ 1` and beyond — has NO proved far bound at all). This draft proves a
single master far-region bound (Lemma W.3) from the exact sinh/sin factor
identity (T.6(i)): with `M := m sin(t/2)` and `r := sinh^2(lam/2)/sin^2(t/2)`,

```
-log |phi_lam(t)|  >=  m * q(M, r) ,      q an explicit elementary function,
```

valid for ALL real `lam` and all `t in (0, pi]` with `M > 1`, monotone in both
arguments, with closed form and a one-page fully elementary proof (no grid
certificates anywhere — the Dirichlet-kernel certificates (T.7b-cert),
(T.7c-cert) are not needed and are superseded). Its corner evaluations give:
small tilt `|lam| <= K/m` on `[sqrt2 pi/m, pi]`: exponent `c_1(K) m` with
`c_1(1) = 0.2259`, `c_1(4) = 0.1019` (vs T.7c's `0.0081`, `0.00002`: 28x and
5067x); the thresholds become `m_2(1) = 143`, `m_2(2) = 190`, `m_2(3) = 267`,
`m_2(4) = 379` under the campaign's standing criterion (NC-T10d, replicated
verbatim) — the requested "hundreds", and for `K = 1` inside the exact-harness
range `m <= 150`, leaving no gap at all. Deep tilt: for `pi/m <= |lam| <= 1.7627`
the bound gives `exp(-c(lam, m) m)` on `[t_0(lam), pi]`, `t_0(lam) :=
2 arcsin(sinh(|lam|/2))`, with `c >= 0.0372` always and `c -> 0.3466` as
`m sinh(|lam|/2)` grows — the far bound item 1 was missing, in the
`t_0(lam)`-moving form the diagnostic PROVED is necessary. At `lam = 0` the
master bound reproduces Lemma 1.4's constant exactly (`q(2,0) = log 2 - 1/2`)
and improves it to `0.4617` on Lemma 1.4's own range. The crossover zone
`[pi/m, t_0(lam)]` gets an explicit partial-variance-Gaussian bound (Clause
W.6) — the "clean inequality" the diagnostic asked for. Status: **Lemmas
W.1–W.3 and Corollaries W.4–W.6: PROVED** (elementary, self-contained,
constants explicit and named). What is NOT closed here: T.9's mechanical
bucket table (T2 §8 item 4) and the deep-tilt CORE model for T.8 (a
non-far-region matter); both scoped honestly in §9.

---

## Contents

- §0 Notation; statement summary with status markers.
- §1 Lemma W.1: exact modulus factorization (self-contained rederivation).
- §2 Lemma W.2: the per-factor envelope.
- §3 Lemma W.3: the master far-region bound (proof; closed form; monotonicity;
  the crossover display W.3d).
- §4 Corollary W.4: small tilt (`|lam| <= K/m`) — named constants, kills §8
  item 5's binding exponent.
- §5 Corollary W.5 + Clause W.6: deep tilt and crossover — kills §8 item 1's
  missing far bound; optimality of the `t_0(lam)` shape.
- §6 Coverage map, handoffs, and restored thresholds.
- §7 Numeric checks NC-W1..NC-W5 (scripts, real quoted output).
- §8 Sharpness: measured slack against the true `|phi_lam|`.
- §9 What remains / honest markers.

---

## 0. Notation and statement summary

As in the merged draft and the T2 draft: `N = m(m-1)/2`,
`lambda = sigma^2 = m(m-1)(2m+5)/72`. Tilt `lam in R`, `theta = e^{-lam}`;
`X = sum_{j=1}^m U_j^{lam}` with independent truncated geometrics `U_j^{lam}`
on `{0,...,j-1}` (weights `e^{-lam i}`), `mu(lam) = E_lam X`,
`sigma_lam^2 = Var_lam X`. The centered tilted cf is
`phi_lam(t) := E_lam e^{it(X - mu(lam))}`; centering is a phase, so
`|phi_lam(t)| = |E_lam e^{itX}| = prod_{j=1}^m |nu_j(t)|` with
`nu_j(t) := E e^{it U_j^{lam}}`. `|phi_lam|` is even and `2pi`-periodic in `t`
and even in `lam`; throughout WLOG `lam >= 0`, `t in (0, pi]`.

Standing shorthand (fixed throughout):

```
s   := sin^2(t/2) ,        S  := sinh^2(lam/2) ,      S_j := sinh^2(lam j / 2) ,
M   := m sin(t/2) ,        r  := S/s ,                t_1 := sqrt(2) pi / m ,
t_0(lam) := 2 arcsin(sinh(|lam|/2))            (defined when sinh(|lam|/2) <= 1,
                                                i.e. |lam| <= 2 asinh(1) = 1.76274...).
```

**Results, with status:**

> **Lemma W.1 (exact modulus factorization) — PROVED.**
> `|phi_lam(t)|^2 = prod_{j=2}^m [ (S_j + sin^2(jt/2)) S ] / [ (S + s) S_j ]`
> (`lam != 0`; the `lam = 0` factor is the Dirichlet form
> `sin^2(jt/2)/(j^2 s)`, its continuity limit).

> **Lemma W.2 (per-factor envelope) — PROVED.** For every `j >= 1`, all real
> `lam, t`:
> `|nu_j(t)|^2 <= (S + min(s, 1/j^2)) / (S + s) = min(1, (S + 1/j^2)/(S + s))`.

> **Lemma W.3 (master far-region bound) — PROVED.** For `m >= 2`, real `lam`,
> `t in (0, pi]` with `M > 1`:
> ```
> -log |phi_lam(t)| >= m q(M, r),      q(M, r) := I(M, r) / (2M),
> I(M, r) = M log[ (1+r) M^2 / (r M^2 + 1) ] - (2/sqrt r) [ arctan(sqrt r M) - arctan(sqrt r) ]
> ```
> (`I(M, 0) = 2(M log M - M + 1)`, the `r -> 0` limit). `q` is nondecreasing in
> `M >= 1`, nonincreasing in `r >= 0`; `q(M, 0) = log M - 1 + 1/M`; and
> ```
> (W.3d)   q(M, r) >= ((M-1)/(2M)) [ log(1 + 1/r) - 1/(r M) ] .
> ```

> **Corollary W.4 (small tilt; collapses T2 §8 item 5's binding exponent) —
> PROVED.** For `m >= 30`, `0 <= K <= m/4`, `|lam| <= K/m`:
> ```
> (i)  |phi_lam(t)| <= exp(-c_1(K) m)   for  t_1 <= |t| <= pi ,      c_1(K) := q(2.2194, 0.05156 K^2) ,
> (ii) |phi_lam(t)| <= exp(-c_1'(K) m)  for  2pi/m <= |t| <= pi ,    c_1'(K) := q(3.1358, 0.02583 K^2) ,
> ```
> with (rounded down; 50-digit evaluations in NC-W3):
> `c_1(0) = 0.2478, c_1(1) = 0.2259, c_1(2) = 0.1802, c_1(3) = 0.1361,
> c_1(4) = 0.1019, c_1(5) = 0.0773, c_1(6) = 0.0598, c_1(pi) = 0.1306`;
> `c_1'(0) = 0.4617, c_1'(1) = 0.4323, c_1'(2) = 0.3669, c_1'(4) = 0.2374`.
> At `K = 0` this strictly improves the untilted Lemma 1.4
> (`0.4617 > 0.19314` on Lemma 1.4's own range, no prefactor 2, plus coverage
> of `[t_1, 2pi/m]` at `0.2478`). Supersedes Lemma T.7c everywhere.

> **Corollary W.5 (deep tilt; supplies T2 §8 item 1's missing far bound) —
> PROVED.**
> (i) *(rho-family)* For any `rho >= 1` and real `lam` with
> `sinh(|lam|/2) <= sqrt(rho)`, on
> `t in [2 arcsin(min(1, sinh(|lam|/2)/sqrt rho)), pi]`:
> `|phi_lam(t)| <= exp(-m q(m sinh(|lam|/2)/sqrt rho, rho))` (nonvacuous iff
> `m sinh(|lam|/2) > sqrt rho`).
> (ii) *(rho = 1, named)* For `pi/m <= |lam| <= 1.7627` and `t in [t_0(lam), pi]`:
> `|phi_lam(t)| <= exp(-m q(m sinh(|lam|/2), 1))`, and
> `q(m sinh(|lam|/2), 1) >= q(pi/2, 1) = 0.0373...` always, increasing to
> `(1/2) log 2 = 0.3466...` as `m sinh(|lam|/2) -> infty`.
> (iii) *(unified floor)* For `m >= 30` and ALL `|lam| <= 1.7627`, on
> `t in [max(pi/m, t_0(lam)), pi]`:
> `|phi_lam(t)| <= exp(-c_V m)`, `c_V := q(1.5700, 1.00183) = 0.0372`.
> In particular the previously uncovered band `lam in (pi/m, 1/2]` (and up to
> `1.7627`) now has an explicit far bound. Supersedes (T.7b-final) on its whole
> scope with a 554x larger exponent.

> **Clause W.6 (crossover) — PROVED** (it is (W.3d) read in `(t, lam)`):
> for any `lam != 0` and `t` with `M > 1`,
> `-log|phi_lam(t)| >= m ((M-1)/(2M)) [ log(1 + s/S) - s/(S M) ]`.
> Interpretation: `(1/2) log(1 + s/S)` is EXACTLY `-log` of the modulus of the
> cf of the untruncated geometric `Geom(e^{-lam})` at `t`; W.6 says the
> `m`-factor tilted product decays at least like `~m` copies of its limiting
> geometric factor, with explicit early-factor corrections. Since
> `Var(Geom(e^{-lam})) = 1/(4S)` and `log(1 + s/S) ~ t^2/(4S)` as `t -> 0`,
> this is the diagnostic's "genuine local-CLT statement restricted to the
> near-uniform factors" as a clean inequality with the correct leading
> Gaussian constant. (Checked pointwise on the crossover zone: NC-W5(d), min
> margin ratio 1.018 — nearly sharp.)

Every constant above is explicit and named; the constants' provenance is a
finite chain of elementary inequalities plus point evaluations of
`log`/`arctan` at explicitly displayed arguments (§4–§5; evaluations at 50
digits in NC-W3, rounded in the safe direction; no grid-certified inequality
appears anywhere in this draft).

---

## 1. Lemma W.1: the exact modulus factorization

**Lemma W.1.** For `m >= 1`, real `lam != 0`, and real `t`:

```
|phi_lam(t)|^2 = prod_{j=2}^m F_j(lam, t),
F_j := [ (S_j + sin^2(jt/2)) * S ] / [ (S + s) * S_j ] .
```

For `lam = 0`, `F_j = sin^2(jt/2)/(j^2 s)` (continuity limit; this is Lemma
1.1's Dirichlet factor squared).

*Proof.* By Lemma T.2's weight formula, `nu_j(t) = z_j(lam - it)/z_j(lam)`
with `z_j(u) = (1 - e^{-ju})/(1 - e^{-u})` (`j = 1` gives `nu_1 = 1`: the
product may start at `j = 2`). For real `a` and `b`:

```
|1 - e^{-(a+ib)}|^2 = 1 - 2 e^{-a} cos b + e^{-2a}
                    = (1 - e^{-a})^2 + 4 e^{-a} sin^2(b/2)
                    = 4 e^{-a} [ sinh^2(a/2) + sin^2(b/2) ] ,
```

using `(1 - e^{-a})^2 = 4 e^{-a} sinh^2(a/2)`. Apply with `(a, b) = (lam j, -jt)`
(numerator of `z_j(lam - it)`), `(a, b) = (lam, -t)` (denominator), and the
real values at `lam`:

```
|nu_j|^2 = [ 4 e^{-lam j}(S_j + sin^2(jt/2)) / (4 e^{-lam}(S + s)) ]
           * [ 4 e^{-lam} S / (4 e^{-lam j} S_j) ]
         = (S_j + sin^2(jt/2)) S / ( (S + s) S_j ) .
```

All exponential prefactors cancel exactly. Multiply over `j`. (Equivalently:
`|sinh(x + iy)|^2 = sinh^2 x + sin^2 y`, applied at `x + iy = j(lam + it)/2` —
this is the ledger's "exact sinh/sin factor identity", the modulus form of
T.6(i).) The `lam -> 0` limit: `S/S_j -> 1/j^2`. ∎

NUMERIC CHECK (NC-W1(a), (b)): the per-factor identity vs the direct weight
sum at 400 random `(j, lam, t)` (mpmath dps = 40): max rel. deviation
`5.94e-40`; the full product vs the tilted Mahonian sum
`|sum_k a_k e^{-lam k} e^{itk}|/Z` at `m = 12` (exact integer `a_k`), six
`(lam, t)` points: max rel. deviation `5.84e-32`. **Run 2026-08-11: PASS.**

---

## 2. Lemma W.2: the per-factor envelope

**Lemma W.2.** For every integer `j >= 1` and all real `lam, t`:

```
|nu_j(t)|^2  <=  (S + min(s, 1/j^2)) / (S + s)  =  min( 1, (S + 1/j^2)/(S + s) ) .
```

*Proof.* Two classical inequalities, both by induction on `j`:

(a) `|sin(jv)| <= j |sin v|` for all real `v`: `|sin((j+1)v)| =
|sin(jv) cos v + cos(jv) sin v| <= |sin(jv)| + |sin v|`.

(b) `sinh(ju) >= j sinh(u)` for `u >= 0`: `sinh((j+1)u) = sinh(ju) cosh(u) +
cosh(ju) sinh(u) >= sinh(ju) + sinh(u)` (`cosh >= 1`, all terms nonnegative);
both sides even in `u`, so `S_j >= j^2 S` for all real `lam`.

By (a), `sin^2(jt/2) <= min(1, j^2 s)`; with (b),

```
|nu_j|^2 = [S/(S+s)] * (1 + sin^2(jt/2)/S_j)
        <= [S/(S+s)] * (1 + min(1, j^2 s)/(j^2 S))
         = (S + min(1/j^2, s)) / (S + s) .
```

When the min is `s` this equals 1; when it is `1/j^2` it is
`(S + 1/j^2)/(S+s) <= 1` — hence the stated `min(1, ...)` form. At `lam = 0`:
`|nu_j|^2 = sin^2(jt/2)/(j^2 s) <= min(1, j^2 s)/(j^2 s)`, the same formula
with `S = 0`. ∎

Two remarks. (1) At `lam = 0` the envelope is the squared Fejér-type bound
`min(1, 1/(j^2 s))`; since `sin(t/2) >= t/pi` on `[0, pi]`, it is at least as
strong as the SQUARE of Lemma 1.4's envelope `min(1, pi/(jt))` — strictly
stronger wherever `t < pi`. (2) At `j -> infty` with `lam > 0` fixed, the
envelope tends to `S/(S+s) = 1/(1 + s/S)`, which is EXACTLY `|cf|^2` of the
untruncated geometric `Geom(e^{-lam})` — the envelope is tight for deep
factors, which is why the deep-tilt constants of §5 come out near-sharp
(NC-W5(c): within `e^{0.8}` of truth at `lam = 1, m = 300`).

NUMERIC CHECK (NC-W1(c)): envelope vs the exact factor value on 2780
random-plus-adversarial cases (including `t` within `1e-6` of every zero of
`sin(jt/2)`): min margin `+8.36e-8 >= 0` (attained where the envelope is
nearly exact). **Run 2026-08-11: PASS.**

---

## 3. Lemma W.3: the master far-region bound

**Lemma W.3.** Let `m >= 2`, `lam` real, `t in (0, pi]`, and set
`h := sin(t/2) = sqrt s in (0, 1]`, `M := mh`, `r := S/s`. If `M > 1`, then

```
-log |phi_lam(t)|  >=  m q(M, r) ,     q(M, r) := I(M, r)/(2M) ,
```

where

```
I(M, r) := integral_1^M log[ (1+r) u^2 / (r u^2 + 1) ] du
         = M log[ (1+r) M^2 / (r M^2 + 1) ] - (2/sqrt r) [ arctan(sqrt r M) - arctan(sqrt r) ]
```

(for `r = 0`: `I(M, 0) = 2 (M log M - M + 1)`, the limit — note
`(2/sqrt r)[arctan(sqrt r M) - arctan(sqrt r)] -> 2(M - 1)`). Moreover:

(i) `q` is nondecreasing in `M` on `[1, infty)` and nonincreasing in
`r on [0, infty)`; `q(M, 0) = log M - 1 + 1/M`;

(ii) `(W.3d)`: `q(M, r) >= ((M-1)/(2M)) [ log(1 + 1/r) - 1/(rM) ]` for `r > 0`.

*Proof.* By Lemma W.2,

```
-2 log|phi_lam(t)| = sum_{j=2}^m ( -log |nu_j(t)|^2 )
                  >= sum_{j=2}^m log [ (S+s) / (S + min(s, 1/j^2)) ] .
```

Dividing numerator and denominator by `s`, the `j`-th term is `f(jh)` where

```
f(u) := log [ (1+r) / (r + min(1, 1/u^2)) ]
      = log [ (1+r) u^2 / (r u^2 + 1) ]   for u >= 1 ;      f(u) = 0  for 0 <= u <= 1 .
```

`f` is continuous, nonnegative, and nondecreasing on `[0, infty)`: on `u >= 1`,
`(d/du) log[u^2/(ru^2+1)] = 2/u - 2ru/(ru^2+1) = 2/[u(ru^2+1)] > 0`, and
`f(1) = 0` matches the flat part. Since `f` is nondecreasing,
`f(jh) >= (1/h) integral_{(j-1)h}^{jh} f(u) du` for every `j >= 2`; summing
over `j = 2, ..., m` (the intervals tile `[h, mh]`):

```
sum_{j=2}^m f(jh) >= (1/h) integral_h^{mh} f(u) du = (1/h) integral_1^M f(u) du = (1/h) I(M, r) ,
```

where the middle equality uses `f = 0` on `[h, 1]` (valid since `h <= 1`; if
`M <= 1` the integral is empty and the bound is the trivial `0`). Hence
`-log|phi_lam(t)| >= I(M, r)/(2h) = (m/(2M)) I(M, r) = m q(M, r)`.

*Closed form.* `integral 2 log u du = 2(u log u - u)` and
`integral log(ru^2+1) du = u log(ru^2+1) - 2u + (2/sqrt r) arctan(sqrt r u)`
(differentiate to check); assembling over `[1, M]`, the constant terms cancel
and the displayed form results.

*(i) Monotonicity.* In `M`: `(d/dM) [I/(2M)] = [M f(M) - I]/(2M^2) >= 0`
because `I = integral_1^M f <= (M-1) f(M) <= M f(M)` (`f` nondecreasing). In
`r`: at fixed `u >= 1`, `(d/dr) f = 1/(1+r) - u^2/(ru^2+1)
= (1 - u^2)/[(1+r)(ru^2+1)] <= 0`, so `I` and `q` are nonincreasing in `r`.
The `r = 0` value: `I(M,0)/(2M) = log M - 1 + 1/M`.

*(ii).* Write `f(u) = log(1 + 1/r) - log(1 + 1/(ru^2)) >= log(1+1/r) - 1/(ru^2)`
(`log(1+x) <= x`); integrate: `I >= (M-1) log(1+1/r) - (1/r)(1 - 1/M)`;
divide by `2M`. ∎

**Remark (Lemma 1.4 is the `(M, r) = (2, 0)` corner).** `q(2, 0) =
log 2 - 1/2 = 0.19314...` — exactly the constant of the merged draft's Lemma
1.4 (verified symbolically: `I(2,0)/4 = (2(2 log 2 - 1))/4 = log 2 - 1/2`;
NC-W3 confirms to 50 digits). Lemma 1.4's proof integrates the same logarithm
over the top half of the factors at `t = 2pi/m`; the master bound improves it
twice over — the squared (Fejér) envelope replaces `pi/(jt)`, and ALL factors
`j > 1/sin(t/2)` are counted, not only `j > m/2` — giving `q(M, 0)` with
`M = m sin(pi/m) >= 3.1358`, i.e. `0.4617` (Corollary W.4(ii) at `K = 0`),
on Lemma 1.4's own range, with no prefactor.

NUMERIC CHECK (NC-W2): (a) closed form vs `mpmath.quad` on a `5 x 7` grid of
`(M, r)`: max rel. deviation `3.76e-14`. (b) the master bound vs the true
`-log|phi_lam(t)|` (exact modulus factorization, log-space product):
`m in {30, 60, 100}`, `lam in {0, 0.5/m, 1/m, pi/m, 4/m, 0.05, 0.1, 0.3, 0.5,
1.0, 1.5, 2.5}`, 1199-point `t`-grids: `max m q/(-log|phi|) = 0.988902 <= 1`
(global, at `m = 100, lam = 2.5, t = pi` — the deep-factor-tight corner);
every `(m, lam)` row `<= 1`. (c) monotonicity spot grids: PASS.
**Run 2026-08-11: PASS.**

---

## 4. Corollary W.4: small tilt (kills §8 item 5's binding exponent)

**Corollary W.4.** Let `m >= 30`, `0 <= K <= m/4`, `|lam| <= K/m`. Then

```
(i)   |phi_lam(t)| <= exp( - c_1(K) m )    for  t_1 = sqrt2 pi/m <= |t| <= pi ,
      c_1(K) := q(2.2194, 0.05156 K^2) ;
(ii)  |phi_lam(t)| <= exp( - c_1'(K) m )   for  2pi/m <= |t| <= pi ,
      c_1'(K) := q(3.1358, 0.02583 K^2) .
```

*Proof.* All of (a)–(e) below are certified in NC-W3 (each is a two-line
elementary inequality plus a monotone-in-`m` evaluation at `m = 30`):

(a) `x -> sin(x)/x` is decreasing on `(0, pi/2]` (since `tan x > x`), so
`m -> m sin(c/m)` is increasing; hence for `m >= 30`:
`M >= m sin(t_1/2) = m sin(sqrt2 pi/(2m)) >= 30 sin(sqrt2 pi/60) = 2.21941... >= 2.2194`
on range (i), and `M >= m sin(pi/m) >= 30 sin(pi/30) = 3.13585... >= 3.1358`
on range (ii). (On both ranges `sin(t/2)` is increasing in `t`, so the worst
`t` is the left endpoint; `t/2 <= pi/2` throughout.)

(b) Consequently `s >= (2.2194/m)^2 >= 4.9257/m^2` on (i) and
`s >= (3.1358/m)^2 >= 9.8332/m^2` on (ii) (`2.2194^2 = 4.92573... >= 4.9257`,
`3.1358^2 = 9.83324... >= 9.8332`).

(c) `sinh x <= x cosh x` for `x >= 0` (`(x cosh x - sinh x)' = x sinh x >= 0`),
so with `x = |lam|/2 <= K/(2m) <= 1/8` (from `K <= m/4`):
`S <= (K/(2m))^2 cosh^2(1/8) <= (K^2/(4m^2)) * 1.0157066 <= 0.253927 K^2/m^2`.

(d) Hence `r = S/s <= 0.253927 K^2/4.9257 <= 0.05156 K^2` on (i) and
`r <= 0.253927 K^2/9.8332 <= 0.02583 K^2` on (ii).

(e) By Lemma W.3(i) (`q` nondecreasing in `M`, nonincreasing in `r`),
`q(M(t), r(t)) >= q(2.2194, 0.05156 K^2)` on (i) and
`>= q(3.1358, 0.02583 K^2)` on (ii), for every `t` in the stated range. Apply
Lemma W.3. ∎

**Values** (NC-W3, mpmath dps = 50; quoted constants are the values rounded
DOWN, safe direction for a decay exponent):

| K | `c_1(K)` (from `t_1`) | `c_1'(K)` (from `2pi/m`) | T.7c's proved `0.06 e^{-2K}` | improvement (from `t_1`) |
|---|---|---|---|---|
| 0 | 0.2478 | **0.4617** | — (Lemma 1.4: 0.19314 from `2pi/m`) | 2.39x vs L1.4, on L1.4's range |
| 1 | **0.2259** | 0.4323 | 8.120e-3 | 28x |
| 2 | **0.1802** | 0.3669 | 1.099e-3 | 164x |
| 3 | **0.1361** | — | 1.487e-4 | 915x |
| 4 | **0.1019** | 0.2374 | 2.013e-5 | 5067x |
| 5 | 0.0773 | — | 2.7e-6 | ~28000x |
| 6 | 0.0598 | — | 3.7e-7 | ~163000x |
| pi | 0.1306 | — | — | (used for T.8's `|lam| <= pi/m` scope) |

Notes. (1) Range (i) is exactly the far region consumed by T.9's kernel (its
core, via Lemma T.9'', is `|t| <= t_1`): **no gap** between core and far.
(2) Range (ii) matches Lemma 1.4's and g1_draft_b's far arc; `c_1'(0) = 0.4617`
is the drop-in replacement for `2 e^{-0.19314 m}` in B.3/B.6/B.8 (and it has
no prefactor). (3) The `K`-degradation is polynomial (`r ~ 0.05 K^2` feeding a
smooth `q`), not the catastrophic `e^{-2K}` of the pairwise-comparison
mechanism — this is what moves `m_2(4)` from `5.1e6` to the hundreds. (4) For
`K <= 1.7` one has `c_1(K) > 0.19314` (`c_1(1.7) = 0.194627... >
0.19314 > c_1(1.75) = 0.192233...`, NC-W3): the tilted far bound on
`[t_1, pi]` is then stronger than the proved UNTILTED Lemma 1.4 was on its
smaller range.

---

## 5. Corollary W.5 and Clause W.6: deep tilt and crossover (kills §8 item 1's missing far bound)

**Corollary W.5.**

(i) *(rho-family)* Let `rho >= 1` and let `lam` be real with
`sinh(|lam|/2) <= sqrt rho`. Set
`t_rho(lam) := 2 arcsin( sinh(|lam|/2)/sqrt rho )`. Then for
`t in [t_rho(lam), pi]`, provided `M_rho := m sinh(|lam|/2)/sqrt rho > 1`:

```
|phi_lam(t)| <= exp( - m q( M_rho, rho ) ) .
```

(ii) *(rho = 1, named clause)* For `pi/m <= |lam| <= 2 asinh(1) = 1.76274...`
and `t in [t_0(lam), pi]` (`t_0 = t_1(lam)` of the family, i.e.
`2 arcsin(sinh(|lam|/2))`):

```
|phi_lam(t)| <= exp( - m q( m sinh(|lam|/2), 1 ) ) ,
q( m sinh(|lam|/2), 1 ) >= q(pi/2, 1) = 0.03736... ,
```

and `q(m sinh(|lam|/2), 1)` increases to `(1/2) log 2 = 0.34657...` as
`m sinh(|lam|/2)` grows (values: NC-W3's deep-tilt table; e.g. at
`lam = 0.3`: `0.2966` for `m = 100`, `0.3294` for `m = 300`).

(iii) *(unified floor)* For `m >= 30` and every real `lam` with
`|lam| <= 1.7627`, on `t in [max(pi/m, t_0(lam)), pi]`
(read `t_0(lam) = 0` for `lam = 0`):

```
|phi_lam(t)| <= exp( - c_V m ) ,      c_V := q(1.5700, 1.00183) = 0.0372 .
```

*Proof.* (i) On the stated range, `sin(t/2) >= sinh(|lam|/2)/sqrt rho` (by
definition of `t_rho`; `arcsin` is defined by the hypothesis), hence
`r = S/sin^2(t/2) <= rho` and `M = m sin(t/2) >= M_rho`. Lemma W.3 plus its
monotonicity gives the display. (ii) is (i) at `rho = 1`; the floor:
`M_1 = m sinh(|lam|/2) >= m |lam|/2 >= pi/2` (`sinh x >= x`, `|lam| >= pi/m`),
so `q(M_1, 1) >= q(pi/2, 1)`, evaluated in NC-W3; the large-`M` limit of
`q(M, 1)` is `(1/2) log 2` (directly from the closed form). (iii) Two cases.
If `|lam| <= pi/m`: on `t >= pi/m`, `sin(t/2) >= sin(pi/(2m))`, so
`M >= m sin(pi/(2m)) >= 30 sin(pi/60) = 1.57007... >= 1.5700` (`m >= 30`,
monotone as in W.4(a)), and
`r <= [ sinh(pi/(2m)) / sin(pi/(2m)) ]^2 <= [ sinh(pi/60)/sin(pi/60) ]^2
= 1.0018293... <= 1.00183` (`sinh(x)/sin(x)` is increasing on `(0, pi/2)`,
worst case `m = 30`; certified NC-W3). If `pi/m <= |lam| <= 1.7627`: on
`t >= t_0(lam)` (note `t_0(lam) >= 2 sinh(|lam|/2) >= |lam| >= pi/m`, so the
`max` is `t_0`), case (ii) gives `q >= q(pi/2, 1) = q(1.5708, 1) >=
q(1.5700, 1.00183)` by monotonicity. In both cases
`q >= q(1.5700, 1.00183) = 0.037251... >= 0.0372`. ∎

**Why the `t_0(lam)`-moving range is the correct target shape (not a defect).**
The diagnostic (`g2_item1_deep_tilt_notes_20260805.md`, finding (1)) proved
empirically that `|phi_lam(pi/m)| -> 1` as `m -> infty` for fixed `lam` —
NO bound `exp(-c(lam) m)` can hold on the closed interval `[pi/m, pi]` for
`lam` bounded away from 0. More precisely, for fixed `lam` the true decay at
`t` is `~ sigma_lam^2 t^2/2` with `sigma_lam^2 = Theta(m)`, so
`exp(-c m)`-strength REQUIRES `t` of order a constant — and `t_0(lam) ~ lam`
(as `lam -> 0`: `t_0(lam) = |lam| (1 + O(lam^2))`, cf. NC-W3's table) is
exactly the scale at which `sin^2(t/2)` overtakes `sinh^2(lam/2)`. W.5's
range is therefore order-optimal; the handoff at the small-`lam` end is
seamless: `t_0(lam) <= t_1` iff `sinh(|lam|/2) <= sin(t_1/2)`, which holds for
`|lam| <= 4.4/m`-class, and Corollary W.4 owns that regime anyway.

**Clause W.6 (crossover bound).** For any `lam != 0` and any `t in (0, pi]`
with `M > 1`:

```
-log|phi_lam(t)| >= m ((M-1)/(2M)) [ log(1 + s/S) - s/(S M) ] .
```

*Proof.* (W.3d) with `1/r = s/S`. ∎

This is the explicit-partial-Gaussian control on the crossover zone
`[pi/m, t_0(lam)]` for deep tilt (the diagnostic's stalling point 2): per
factor it is the exact geometric-limit decay `(1/2) log(1 + s/S)` (see the
remark after W.2), whose small-`t` expansion `t^2/(8S) = Var(Geom(e^{-lam}))
t^2/2` carries the true per-factor Gaussian constant; the two explicit
correction factors `((M-1)/M)` and `-s/(SM)` quantify the loss from the first
`~1/sin(t/2)` factors. NC-W5(d) checks it pointwise across the crossover zone
(`m in {100, 300}`, `lam in {0.1, 0.3, 0.5}`): min ratio
`(-log|phi|)/(bound) = 1.018` — the clause is nearly sharp, so nothing
substantially stronger of this shape is available; a deep-tilt LCLT will need
a genuine model here, not just decay (§9 item 2).

**Beyond `|lam| = 1.7627`.** The rho-family covers any fixed tilt: e.g.
`rho = 10` covers `|lam| <= 2 asinh(sqrt 10) = 3.7358` with
`c = q(m sinh(|lam|/2)/3.163, 10) -> (1/2) log(1.1) = 0.0476...`. As
`lam -> infty` every factor's law degenerates to `delta_0` and
`phi_lam -> 1` pointwise, so ANY far bound must degenerate; quantitatively
`q(infty, r) = (1/2) log(1 + 1/r)` with `1/r = s/S ~ 4 s e^{-lam}`, i.e. the
inevitable `e^{-lam}` envelope. For the campaign this is moot: the diagnostic's
own check (b) has the working range `lam* <= ~1` for `C_0 = 2000` up to
`m ~ 3000` (its search cap), inside W.5(ii)'s scope, and the family covers
whatever a future T.8 rebuild needs, with stated degradation.

---

## 6. Coverage map, handoffs, restored thresholds

**Exact `(t, lam)` coverage** (all clauses are instances of Lemma W.3, which
itself covers every `(t, lam)` with `m sin(t/2) > 1`; WLOG `lam >= 0`,
`t in (0, pi]`):

| tilt range | `t` range | proved bound | replaces |
|---|---|---|---|
| `lam <= K/m`, `K <= m/4`, `m >= 30` | `[t_1, pi]` | `exp(-c_1(K) m)`, `c_1(1) = 0.2259` .. `c_1(4) = 0.1019` | T.7c `exp(-0.06 e^{-2K} m)` |
| same | `[2pi/m, pi]` | `exp(-c_1'(K) m)`, `c_1'(0) = 0.4617` | Lemma 1.4 `2 e^{-0.19314 m}` (untilted case) |
| `lam <= pi/m`, `m >= 30` | `[pi/m, pi]` | `exp(-0.0372 m)` (unified floor) | T.7b-final `exp(-m_*/4730)` |
| `pi/m <= lam <= 1.7627` | `[t_0(lam), pi]` | `exp(-m q(m sinh(lam/2), 1))`, floor `exp(-0.0373 m)` | nothing existed (item 1) |
| `lam <= 1.7627`, `m >= 30` | `[max(pi/m, t_0(lam)), pi]` | `exp(-0.0372 m)` (single constant) | — |
| any `lam`, crossover `[pi/m, t_0(lam)]` | pointwise | `m ((M-1)/(2M))[log(1+s/S) - s/(SM)]` (W.6) | nothing existed (diagnostic point 2) |
| any `lam` (e.g. `> 1.7627`) | `[t_rho(lam), pi]` | rho-family W.5(i) | nothing existed |

**Handoff to the proved small-tilt/core bounds (no gaps):**

1. *T.9 (refined law).* Core `|t| <= t_1`: Lemma T.9'' (proved, uniform in
   `lam`). Far `[t_1, pi]`: Corollary W.4(i). The two ranges share the single
   split point `t_1` — the far bucket of T.9's kernel should now be quoted as
   `<= poly * exp(-c_1(K) m)`.
2. *T.8-final (crude law, `|lam| <= pi/m` scope).* Core `|t| <= pi/m`:
   (T.6ii). Far `[pi/m, pi]`: unified floor `c_V = 0.0372`; or, cutting the
   core at `t_1` (legitimate: T.9''c covers `|t| <= t_1` uniformly in `lam`),
   far `[t_1, pi]` at `c_1(pi) = 0.1306`. Condition (V) is re-evaluated below.
3. *Deep tilt (item 1).* `[t_0(lam), pi]`: W.5. `[pi/m, t_0(lam)]`: W.6
   (decay of the true partial-Gaussian order). `[0, pi/m]`: (T.6ii) — which
   for fixed `lam` is a genuine CORE, not a far region (diagnostic finding
   (1)); the deep-tilt crude law still needs a model there (§9 item 2). The
   far-region half of item 1 — the missing bound — is supplied.
4. *g1_draft_b (G1).* Its every use of Lemma 1.4 (`2 e^{-0.19314 m}` in B.3
   (III), B.6 `Delta_out`, B.8's `SP`) accepts `exp(-0.4617 m)` as a drop-in
   on the same interval `[2pi/m, pi]` (untilted = `K = 0`).

**Restored thresholds** (NC-W4; criterion identical to NC-T10d:
`16 sqrt(2pi) (1.05 m^3/36)^{3/2} e^{-cm} <= 0.2/m^2`):

| K | old `m_2(K)` (T.7c exponent, T10d loop) | new `m_2(K)` (`c_1(K)`, unit-step scan) |
|---|---|---|
| 1 | 7338 | **143** |
| 2 | 66010 | **190** |
| 3 | 593181 | **267** |
| 4 | 5076022 | **379** |

The exact harness certifies the refined law itself for `m <= 150` (NC-1,
NC-T8). Under the standing criterion, for `K = 1` the far bucket is viable for
`m >= 143`: **the far-region obstruction leaves no uncovered `m` at all for
`K = 1`**, and bands `151..189 / 151..266 / 151..378` for `K = 2/3/4` —
coverable by the planned harness extension (G4: exact `m = 200` costs minutes)
and/or by the eventual bucket assembly's own sharper prefactor.

T.8-final's viability condition (V), worst case over its hypothesis set
(`s2 <= 1.05 m^3/36`): old exponent `(m/pi - 1)/4730` needs `m >= 1065849`
(the T2 draft's `~2.5e5` corresponds to evaluating at `s2 = C_0 = 2000`, the
easiest point — reproduced: `292672`); new: `m >= 879` with the `pi/m` cut
(`c_V`), `m >= 185` with the `t_1` cut (`c_1(pi)`).

g1_draft_b's far-arc threshold (its `m_1`-setting piece, `y_0 = 1`): old
`c = 0.19314` gives `m_1 ~ 180` (exactly reproducing B.8's table value — a
strong consistency check on the criterion); new `c = 0.4617` gives
`m_1-far ~ 60`. (Lowering B.8's `m_1` below 180 additionally requires
re-evaluating its box/denominator buckets at the smaller `m`; they are
decreasing in `m` and were evaluated at 180, so this is mechanical — flagged,
not done here.)

---

## 7. Numeric checks (all scripts in `g2_scripts/campaign_undefined/wp1_c/`, run 2026-08-11)

| # | script | validates | real result |
|---|---|---|---|
| NC-W1 | `wp1c_nc1_identity.py` | W.1 identity (400 random, dps=40); product vs tilted-Mahonian sum (m=12, exact `a_k`); W.2 envelope (2780 cases incl. adversarial); induction inequalities spot grids | **PASS** — max rel dev 5.94e-40 (identity), 5.84e-32 (product); envelope min margin +8.36e-8 |
| NC-W2 | `wp1c_nc2_master.py` | closed form `I(M,r)` vs quadrature; master bound vs true `-log|phi|` (36 `(m, lam)` rows, 1199-pt t-grids); `q` monotonicity | **PASS** — quad dev 3.76e-14; global max ratio 0.988902 <= 1 (at m=100, lam=2.5, t=pi); monotone |
| NC-W3 | `wp1c_nc3_constants.py` | chain certificates (M-floors, `cosh^2(1/8) <= 1.0157066`, r-coefficients, `r_V`); named constants at dps=50; `q(2,0) = log2 - 1/2` exactly; comparison table; deep-tilt `t_0/c` table | **PASS** — all certificates true; `c_1(1) = 0.225989...`, `c_1(4) = 0.101983...`, `c_V = 0.037251...`, `|q(2,0)-(log2-1/2)| = 0.0` |
| NC-W4 | `wp1c_nc4_thresholds.py` | NC-T10d criterion, old vs new; (V) thresholds (both `s2` conventions); g1 far-arc note | **PASS** — table in §6; old-criterion reproduction: `m_2(1) = 7338` (ledger: ~7.3e3), g1 `m_1 ~ 180` (ledger: 180) |
| NC-W5 | `wp1c_nc5_sharpness.py` | W.4 slack (9 rows); untilted clause vs ledger NC-5; W.5 deep-tilt slack (8 rows); W.6 pointwise on crossover | **PASS** — see §8; measured m=40 untilted max = 1.141e-16 (ledger NC-5: 1.1e-16) |

Key quoted output (verbatim excerpts):

```
NC-W1(a) per-factor identity: max rel dev = 5.94e-40 at (j, lam, t) = (13, 0.01, 2.899...)
NC-W1(b) product vs tilted-Mahonian sum (m=12): max rel dev = 5.84e-32
NC-W1(c) envelope: min (bound - value) = 8.36e-8 ... over 2780 cases
NC-W2(b) ... GLOBAL max ratio = 0.988902 at (m, lam, t) = (100, 2.50000, 3.14159)  (PASS iff <= 1)
NC-W3 ... c_1(1) = 0.225989909281 ... c_1(4) = 0.101983937137 ... c_V = 0.0372513232987
       ... |q(2,0) - (log2 - 1/2)| = 0.0
NC-W4(a)  K=1: old 7338  new 143 | K=2: old 66010 new 190 | K=3: old 593181 new 267 | K=4: old 5076022 new 379
NC-W4(b)  old (T.7b-final): m >= 1065849 (worst case) / 292672 (s2 = C_0)
          new: m >= 879 (pi/m cut) / 185 (t_1 cut)
NC-W4(c)  old (Lemma 1.4, c = 0.19314): m_1 ~ 180    new (c = 0.4617): m_1-far ~ 60
NC-W5(d)  min (-log|phi|)/(W.6 lower bound) = 1.0182 (PASS iff >= 1)
```

---

## 8. Sharpness: measured slack (NC-W5)

Corollary W.4(i), `lam = K/m`, measured `max_{[t_1, pi]} |phi_lam|` vs
`exp(-c_1(K) m)`:

| m | K=1 measured / bound | K=2 | K=4 |
|---|---|---|---|
| 30 | `e^-9.24` / `e^-6.78` | `e^-8.01` / `e^-5.41` | `e^-5.49` / `e^-3.06` |
| 60 | `e^-18.05` / `e^-13.55` | `e^-15.70` / `e^-10.81` | `e^-10.84` / `e^-6.11` |
| 100 | `e^-29.79` / `e^-22.59` | `e^-25.95` / `e^-18.02` | `e^-17.95` / `e^-10.19` |

Slack `e^{2.4}` to `e^{7.9}` — i.e. the proved exponent captures 73–76% (K=1)
and 55–57% (K=4) of the true one on the tested range, versus T.7c's factors
of `24x` to `4e7x` and the untilted Lemma 1.4's 4–8 orders of magnitude
(NC-5). Deep tilt is tighter still: at `m = 300` the bound is within `e^{7.0}`
(`lam = 0.1`), `e^{2.6}` (`0.3`), `e^{1.6}` (`0.5`), `e^{0.8}` (`1.0`) of the
measured max — the envelope is exact in the deep-factor limit (§2 remark).
The crossover clause W.6 has min margin ratio 1.018. The residual small-tilt
slack is the discarded oscillation of `sin^2(jt/2)` (the envelope takes its
sup, 1, where the average is 1/2); an averaged version would need
Dirichlet-type certificates again and is NOT needed at the new thresholds.

---

## 9. What remains / honest markers

**Status recap: Lemmas W.1–W.3, Corollaries W.4–W.5, Clause W.6 — PROVED**,
self-contained, elementary, every constant named and certified by the
NC-W1..W5 scripts; no grid-certified inequality is used ((T.7b-cert)/(T.7c-cert)
retirable). The threshold numbers of §6 are reported facts under the
campaign's standing criterion, not new theorems. Residue:

1. **T.9's mechanical bucket table (T2 §8 item 4) — UNCHANGED, still open.**
   This draft replaces the far bucket's exponent only. The B.6-analogue table
   for the 6-term tilted model (with the two odd rows) remains the one
   mechanical session standing between T.9 and a full `C_R(K)`; with
   `m_2(1) = 143 < 150 =` exact-harness range, that assembly is now the ONLY
   obstruction for `K = 1`.
2. **Deep-tilt CORE model (the non-far half of §8 item 1) — OPEN.** For fixed
   `lam`, `sigma_lam^2 = Theta(m)`, the Gaussian core has width
   `Theta(1/sqrt m) >> t_1`, and T.9''s model radius `~ t_1` covers a
   vanishing fraction of it; (T.6ii) gives domination but not a two-sided
   model. A T.8 rebuild for deep tilt therefore needs a new core lemma. The
   identified route (recorded for the successor package): for `lam > 0` the
   factor zeros `1 - e^{-(lam - it) j} = 0` sit at distance `lam` from the
   real `t`-axis, so `log phi_lam` is analytic in the strip `|Im t| < lam` —
   a cumulant-series model with radius `~ c lam` (replacing T.9''s `~ c/m`),
   which matches the Gaussian width whenever `lam >> 1/sqrt m`. W.6 supplies
   the tail control such a rebuild would pair with. Note this is beyond a
   "far-region bound" — item 1's far-region half (the part this work package
   was scoped to) is closed by W.5.
3. **Finite-computation steps (not gaps, listed for transparency).** The named
   constants are point evaluations of `log`/`arctan`/`sin`/`sinh` at
   explicitly displayed arguments, computed in double precision and confirmed
   at 50 significant digits (mpmath, NC-W3), then rounded in the safe
   direction with margin `>= 5e-5` — eleven orders above the evaluation
   error. Interval arithmetic on demand; no Sturm sequences needed anywhere.
4. **Scope `m >= 30`** (for W.4 and W.5(iii); W.3 and W.5(i)-(ii) need only
   `m >= 2`). `m < 30` is inside the exact harness range (NC-1), so no
   downstream statement loses coverage.
5. **The threshold criterion is a proxy.** NC-T10d's
   `16 sqrt(2pi) lambda^{3/2} e^{-cm} <= 0.2/m^2` is the campaign's standing
   comparison shape (inherited from B.8's SP piece); the eventual T.9/T.8
   assemblies must verify their own polynomial prefactors against the new
   exponents. Given `e^{-0.10 m}`-to-`e^{-0.23 m}` far bounds, any
   `poly(m)`-prefactor variant lands at the same order of threshold
   (the criterion's `m^{6.5}`-prefactor is already generous).
6. **(V)-convention discrepancy documented** (§6): the T2 draft's "~2.5e5"
   for old-(V) was the `s2 = C_0` best case; the uniform worst case is
   `1.07e6`. Both are computed and quoted; the new numbers (879 / 185) are
   worst-case.
7. **Lowering g1's `m_1` via `c_1'(0) = 0.4617`** requires re-evaluating
   B.8's remaining buckets at the smaller `m` (they were tabulated at
   `m_1 = 180`; each is decreasing in `m`) — mechanical, one short session,
   not done here.

*End of wp1_draft_c. Blind protocol maintained.*
