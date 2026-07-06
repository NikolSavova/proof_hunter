# Theorem F2 — draft via the generating-function / saddle-point (tilting) route

**Angle.** Fourier–Edgeworth expansion of `I_m(k) = [q^k] prod_{i=1}^m (1-q^i)/(1-q)`
with explicit error terms in the central window, plus an **exponential-tilting
(saddle-point) argument** for the tails: the log-concavity ratio is invariant under
tilting, and the tilted variance is *strictly smaller* than the untilted one, which
forces the minimum ratio to the center. All quantitative claims below were checked
against the exact harness `mahonian.py` (commands in the NUMERIC CHECK lines; run from
`phase2/bruhat/`).

**Status summary (honest).**
- (a) Proved modulo two GAP-flagged remainder-bookkeeping lemmas (GAP-2, GAP-3), with a
  *sharper* form than the target: `sigma^2 (r_m - 1) = 1 - 27/(25 m) + O(m^{-2})`.
- (b) Proved in the weakened form `|argmin - N/2| = O(sigma m^{-1/2}) = O(m)`;
  the exact `<= 1` statement reduces to unimodality of `k -> r_m(k)` (verified exactly
  for `5 <= m <= 56`), which is GAP-4.
- (c) **Not achieved**; moreover the spec's suggested constant is **false**: `c = 7/8`
  fails at `m = 6`, where `sigma^2 (r_6 - 1) = 187/216 = 0.865740...` exactly. The
  corrected sharp target is `c = 187/216` (attained at `m=6`); we give a reduction of
  `c = 5/6` to GAP-1 + a finite computation, and record the corrected conjecture.

Throughout: `N = m(m-1)/2`, `sigma^2 = m(m-1)(2m+5)/72`, `P(k) = I_m(k)/m!`,
`x = k - N/2`, `y = x/sigma`, `r(k) = P(k)^2/(P(k-1)P(k+1))`,
`log r(k) = -Delta^2 log P(k)` (second difference in `k`).

---

## 1. Exact representations

**Lemma 1.1 (characteristic function; exact inversion).**
`inv = sum_{j=2}^m U_j` with `U_j` independent, uniform on `{0,...,j-1}`
(insertion encoding; standard). Hence with `phi_j(t) = sin(jt/2)/(j sin(t/2))`
(the centered characteristic function of `U_j`) and `phi(t) = prod_{j=2}^m phi_j(t)`
(real, even, `phi(0)=1`),

```
P(k) = (1/pi) * Int_0^pi phi(t) cos(t x) dt ,   x = k - N/2 .
```

*Proof.* `E e^{it(U_j - (j-1)/2)} = e^{-it(j-1)/2}(e^{ijt}-1)/(j(e^{it}-1)) = phi_j(t)`;
inversion on the lattice `Z + N/2` (if `N` odd, `x` is a half-integer; the formula is
unchanged since `phi` is supported on `[-pi,pi]` as the cf of an integer shift of `x`). ∎

**Lemma 1.2 (second-difference kernel).** With `D(k) = P(k)^2 - P(k-1)P(k+1)`,

```
D(k) = (2pi)^{-2} * IntInt_{[-pi,pi]^2} phi(s) phi(t) cos((s+t)x) (1 - cos(s-t)) ds dt .
```

*Proof.* Write each `P` by Lemma 1.1 as `(2pi)^{-1} Int phi e^{-itx}`, expand the product,
and symmetrize the factor `1 - e^{i(s-t)}` in `(s,t)` to `1 - cos(s-t)`. ∎

This is the exact analogue of the device Canfield–Janson–Zeilberger use for the central
Gaussian binomial coefficient (arXiv:0908.2089, Thm 4.6 / eq. (4.11)); Lemma 3.2 below is
the `[m]_q!` transfer of their central estimate. The point of Lemma 1.2 is that the
second difference is computed *inside* the integral (kernel `1-cos(s-t)`), so no
catastrophic cancellation of pointwise errors occurs: relative accuracy `O(1/m)` in
`phi` yields relative accuracy `O(1/m)` in `D`, even though `D ~ P^2/sigma^2`.

NUMERIC CHECK: (both formulas, `m=8`, `k=10,14`, midpoint quadrature)
`P` exact `0.0618303571` vs integral `0.0618303571`; `D` exact `2.227e-04` vs integral
`2.227e-04` (`k=10`); `9.514e-02 / 4.658e-04` agree likewise at `k=14`. E.g.
```
python3 - <<'EOF'
import math;from mahonian import mahonian
m=8;a=mahonian(m);N=m*(m-1)//2;f=math.factorial(m)
phi=lambda t:math.prod(math.sin(j*t/2)/(j*math.sin(t/2)) for j in range(2,m+1))
n=200000;k=10;x=k-N/2
P=sum(phi(math.pi*(i+.5)/n)*math.cos(math.pi*(i+.5)/n*x) for i in range(n))/n
print(P, a[k]/f)   # both 0.06183035714...
EOF
```

---

## 2. Characteristic-function estimates

**Lemma 2.1 (all-negative log-sinc series).** For `0 <= u < pi`,
`-log(sin u / u) = sum_{r>=1} a_r u^{2r}` with `a_r = zeta(2r)/(r pi^{2r}) > 0`;
in particular `a_1 = 1/6`, `a_2 = 1/180`, `a_3 = 1/2835`, and since
`a_{r+1}/a_r <= (u/pi)^2` termwise, the tail after `r=2` is at most
`u^6/(2835 (1 - (u/pi)^2))`.

*Proof.* Standard expansion of `log(sin u / u)`; the closed form for `a_r` follows from
`|B_{2r}| = 2 (2r)! zeta(2r) / (2pi)^{2r}`. ∎

**Lemma 2.2 (central expansion of `log phi`).** For `|t| <= pi/m`,

```
-log phi(t) = (sigma^2/2) t^2 + c_4 t^4 + R_2(t),
c_4 = sum_{j=2}^m (j^4-1)/2880 = (S_4(m) - m)/2880,  S_4(m)=m(m+1)(2m+1)(3m^2+3m-1)/30,
0 <= R_2(t) <= (4/3) * (m^7/7) * (t/2)^6 / 2835  <=  m^7 t^6 / 952560 .
```

Moreover for all `|t| <= 2pi/m`: `0 <= phi(t) <= exp(-sigma^2 t^2/2)`.

*Proof.* `log phi(t) = sum_{j=2}^m [ L(jt/2) - L(t/2) ]`, `L(u) = log(sin u/u)`.
For `|t| <= 2pi/m` every argument `jt/2 <= pi`, each factor of `phi` is `>= 0`
(`sin(jt/2) >= 0`), and by Lemma 2.1 every Taylor coefficient of `-log phi` is
`>= 0`; keeping only the `t^2` term gives the Gaussian upper bound
(`sum_j (j^2-1)/24 = sigma^2/2`). For `|t| <= pi/m` all `jt/2 <= pi/2`, so the
`r >= 3` tail is at most `sum_j (jt/2)^6/(2835 * (1 - 1/4))`, giving the stated `R_2`. ∎

**Lemma 2.3 (tail of the cf).** For `t in [2pi/m, pi]`,

```
|phi(t)| <= prod_{j=2}^m min(1, pi/(j t))   (nonincreasing in t),
and  |phi(t)| <= 2 exp( -(log 2 - 1/2) m )  =  2 e^{-0.1931... m}.
```

*Proof.* `|sin(jt/2)| <= 1` and `sin(t/2) >= t/pi` on `[0,pi]` give the product bound,
each factor nonincreasing in `t`; at `t = 2pi/m` the factors with `j > m/2` contribute
`log prod <= -Int_{m/2}^m log(2x/m) dx + log 2 = -(log 2 - 1/2) m + log 2`. ∎

*Remark (important for constants).* The truth is far smaller (see check), but even the
true tail is only *barely* negligible at moderate `m`: the central scale of `D(k)` is
`~ e^{-y^2}/(2 pi sigma^4) ~ 10^{-8}` at `m=40`. This is one root cause of the
explicit-`m_0` problem in part (c) — see GAP-5.

NUMERIC CHECK: `m=30`: max of `|phi|` over `[2pi/m, pi]` is `6.3e-13`, the product
bound holds pointwise (no violations on a 20000-point grid), and
`2 e^{-0.1931*30} = 6.1e-3`. The Gaussian bound at `t = 2pi/m` is
`exp(-sigma^2 t^2/2) = 3.3e-8`.

---

## 3. The central window

Let `beta = c_4 / sigma^4`. Exactly:
`12 beta = (S_4(m) - m)/(240 sigma^4) = 27/(25 m) + O(m^{-2})` (`= 1.08/m + ...`).

**Lemma 3.1 (local Edgeworth expansion).** There are constants `C, c > 0` such that for
all `k`,

```
P(k) = (sigma sqrt(2pi))^{-1} [ e^{-y^2/2} (1 - beta He4(y)) ] + R_1(k),
|R_1(k)| <= C sigma^{-1} m^{-2} log^3 m + 4 e^{-0.19 m},     He4(y) = y^4 - 6y^2 + 3 .
```

*Proof sketch (mechanical; see GAP-1 for the constant chase).* Split `Int_0^pi` at
`t_2 = sqrt(6 log m)/sigma`, `pi/m`, `2pi/m`. On `[0,t_2]`, Lemma 2.2 gives
`phi = e^{-sigma^2 t^2/2}(1 - c_4 t^4 + theta)` with
`|theta| <= R_2 + (c_4 t^4)^2 e^{c_4 t^4} = O(m^{-2} log^3 m)` uniformly; the Gaussian
moment integrals `Int s^{2r} e^{-s^2/2} cos(sy) ds = (-1)^r sqrt(2pi) He_{2r}(y) e^{-y^2/2}`
produce the stated main terms, and extending `t_2 -> infinity` costs `e^{-3 log m}`-type
terms. On `[t_2, 2pi/m]` use `0 <= phi <= e^{-sigma^2 t^2/2} <= m^{-3}`-decay; on
`[2pi/m, pi]` use Lemma 2.3. ∎

NUMERIC CHECK: `m=40`: `max over |y|<=3 of | P(k) sigma sqrt(2pi) e^{y^2/2} - (1 - beta He4(y)) |
= 3.6e-3` (consistent with the next-order terms `c_6 He6 / sigma^6 + beta^2 He4^2/2 = O(m^{-2} poly(y))`;
here `beta = 0.002230`, `12 beta = 0.02676`).

**Lemma 3.2 (central second difference — the CJZ transfer to `[m]_q!`).**
For `|y| <= sqrt(log m)`,

```
sigma^2 * log r(k) = 1 + 12 beta (y^2 - 1) + E_1(k),
|E_1(k)| <= C (1 + y^6)/m^2 + sigma^2 e^{y^2} * O(e^{-0.19 m}) .
```

*Proof sketch.* Apply Lemma 1.2. Substitute `u = s+t, v = s-t` (Jacobian 1/2), so
`phi(s)phi(t) = exp(-sigma^2 (u^2+v^2)/4) (1 - (c_4/8)(u^4 + 6u^2v^2 + v^4) + theta')`
on the central box, with kernel `cos(ux)(1 - cos v)`. All integrals are Gaussian
moments with effective width `tau^2 = 2/sigma^2` in each of `u, v`; the pure Gaussian
part gives `D/P^2 = 1 - e^{-1/sigma^2}` (which alone already yields `r = e^{1/sigma^2}`,
i.e. the leading claim of (a)); the `c_4` terms contribute exactly the factor
`1 + 12 beta (y^2 - 1)` at first order in `beta` (both the `u^4` term, through
`He_4(y)`, and the cross terms `u^2 v^2`, `v^4` contribute at order `beta` — the
`v`-moments satisfy `<v^2(1-cos v)>/<1-cos v> = 3 tau^2 (1+O(tau^2))`). Division by
`P(k)^2` from Lemma 3.1 and `log r = -log(1 - D/P^2)` finish. Remainders: the analytic
error inside the box is *relative* `O(m^{-2} poly(y))`; only the exponentially small
Lemma 2.3 tail enters additively (whence the `e^{y^2} e^{-0.19m}` term, harmless for
`y^2 <= log m` once `m` is large). Full bookkeeping: GAP-1. ∎

NUMERIC CHECK (center): `sigma^2 log r(floor(N/2))` vs `1 - 12 beta`:
```
m=6 : 0.81679 vs 0.81157   (resid * m^2 = +0.19)
m=10: 0.89185 vs 0.89196   (resid * m^2 = -0.011)
m=20: 0.94620 vs 0.94662   (resid * m^2 = -0.17)
m=40: 0.97312 vs 0.97324   (resid * m^2 = -0.19)
```
i.e. `|E_1| * m^2 <= 0.2` at `y=0` for all `6 <= m <= 40` — the shape `O(m^{-2})` is
exactly right. (At `m=5` the residual is `0.028`, so state Lemma 3.2 for `m >= 6`.)
NUMERIC CHECK (window): `m=40`: `max over |y|<=3 of |sigma^2 log r(k) - (1+12 beta(y^2-1))|
= 3.8e-2 <= 0.4 (1+y^6)/m^2` on the whole range (`0.4*730/1600 = 0.18`).

**Corollary 3.3 (central ratio).** `sigma^2 log r_c = 1 - 12 beta + O(m^{-2})`, hence

```
sigma^2 ( r_c - 1 ) = 1 - 27/(25 m) + O(m^{-2}) .
```

NUMERIC CHECK: `m=40`: predicted `sigma^2 log r_c + (sigma^2 log r_c)^2/(2 sigma^2)
= 0.97312 + 0.00026 = 0.97338`; harness `varfit = 0.973381`. Agreement to `6` digits.
Run `python3 mahonian.py --mmax 40` and compare the `varfit` column with
`1 - 27/(25m)`: `m=40: 0.97338 vs 0.973`.

---

## 4. Tilting: the global mechanism

For `lambda in R` set `q = e^{-lambda}` and let `P_lambda(k) ∝ P(k) e^{-lambda k}`
(normalizer `Z(lambda) = [m]_q!/m!` evaluated at `q`). This is precisely the
*q-Mahonian* measure; the tilted `inv` is again a sum of independent variables (the
`q`-deformed uniforms, i.e. truncated geometrics on `{0,...,j-1}` with ratio `q`).
Write `mu(lambda), sigma_lambda^2, kappa_r(lambda)` for its mean, variance, cumulants;
`kappa_j(lambda) = log( sinh(j lambda/2)/sinh(lambda/2) ) - (j-1)lambda/2 + const` per factor.

**Lemma 4.1 (tilt invariance of the ratio).** For every `k` and `lambda`,
`r(k) = P_lambda(k)^2 / (P_lambda(k-1) P_lambda(k+1))`. Consequently, choosing
`lambda = lambda(k)` with `mu(lambda) = k` (possible for every interior `k`: `mu` is a
continuous strictly decreasing bijection onto `(0, N)`), **the log-concavity ratio at
`k` equals the central ratio of a tilted measure sitting at its own mean.**

*Proof.* The factors `e^{-lambda k}` cancel in the ratio. Monotonicity of `mu`:
`mu'(lambda) = -sigma_lambda^2 < 0`. ∎

**Lemma 4.2 (tilted variance domination — fully proved).** For every `j >= 2` and every
`lambda != 0`: `Var_lambda(U_j) < (j^2-1)/12`. Hence `sigma_lambda^2 < sigma^2`.

*Proof.* Per factor, `Var_lambda(U_j) = (1/4) csch^2(lambda/2) - (j^2/4) csch^2(j lambda/2)
= (j^2-1)/12 - [ v(j lambda/2) - v(lambda/2) ] / lambda^2`, where
`v(x) = x^2 csch^2 x + x^2/3`. So the claim is `v` strictly increasing on `(0, inf)`.
Compute `v'(x) >= 0  <=>  sinh^3(x)/3 + sinh(x) >= x cosh(x)
<=> sinh(3x)/12 + (3/4) sinh(x) >= x cosh(x)` (using `sinh^3 = (sinh 3x - 3 sinh x)/4`).
Comparing power series coefficients of `x^{2n+1}`: need `(3^{2n+1} + 9)/12 >= (2n+1)`,
which holds for all `n >= 0` (equality at `n = 0, 1`; strict for `n >= 2`). ∎

**Lemma 4.3 (deficit monotonicity — fully proved).** `lambda -> sigma_lambda^2` is even
and nonincreasing in `|lambda|`; equivalently the deficit `sigma^2 - sigma_lambda^2` is
nondecreasing in `|lambda|`.

*Proof.* By the same reduction, this is: for `0 < a < b`,
`(v(b lambda) - v(a lambda))/lambda^2` nondecreasing in `lambda > 0`, which is
equivalent to `g(x) = x v'(x) - 2 v(x) = -2 x^3 csch^2(x) coth(x)` being nonincreasing,
i.e. to `u(x) = x^3 cosh x / sinh^3 x` being nonincreasing. And
`u'(x) <= 0 <=> 3 sinh y <= y cosh y + 2y` (`y = 2x`), which holds termwise:
`3/(2n+1)! <= 1/(2n)! <=> 2n+1 >= 3` for `n >= 1`, the `n=0` term being covered by `2y`. ∎

NUMERIC CHECK: grid scan of `v` (increasing) and `u` (decreasing) on `(0, 20]` at step
`0.005`: zero violations; the two series inequalities are nonnegative on `(0, 20]`.

**Lemma 4.4 (quantitative deficit and mean shift).** As `lambda -> 0`,
`kappa_4(0) = -sum_{j=2}^m (j^4-1)/120 = -24 c_4`, and for `0 <= lambda <= 1/m`:

```
sigma^2 - sigma_lambda^2 >= (|kappa_4(0)|/2) lambda^2 (1 - C m^2 lambda^2),
x(lambda) := mu(lambda) - N/2 = -Int_0^lambda sigma_s^2 ds,  so |x| <= lambda sigma^2 .
```

*Proof.* Expand `v(x) = 1 + x^4/15 - 2x^6/189 + ...` (alternating, from the `csch^2`
Bernoulli series); per factor the deficit is `((j lambda/2)^4 - (lambda/2)^4)/(15 lambda^2)`
minus a controlled `x^6` term; summing gives `sum_j (j^4-1) lambda^2 / 240 = |kappa_4| lambda^2 / 2`
to leading order. The `x(lambda)` identity is `mu' = -sigma_lambda^2` integrated. ∎

NUMERIC CHECK: `m=30`, `k=210` (so `x = -7.5`): bisection gives `lambda = 0.00956`;
`lambda sigma^2 = 7.51` (vs `|x| = 7.5`); deficit `sigma^2 - sigma_lambda^2 = 785.4 - 783.4 = 1.98`
vs `|kappa_4| lambda^2/2 = 43950 * (0.00956)^2/2 = 2.01`. (`kappa_4(0) = -43949.7` exactly
`= -(S_4(30)-30)/120`.)

**Lemma 4.5 (tilted second difference — the tail engine).** Let `lambda = lambda(k)` as
in Lemma 4.1, and `beta_lambda = -kappa_4(lambda) / (24 sigma_lambda^4)`.

(i) *(small tilt)* For `|lambda| <= 1/m`:
`sigma_lambda^2 log r(k) = 1 - 12 beta_lambda + E_2(k)`, `|E_2| <= C (1 + y^2)/m^2`.
The mechanism: repeat §3 in the tilted frame; since `k` **is** the tilted mean, the
skewness term enters only through `He_3''(0) = 0` at first order, so the first surviving
corrections are `O(gamma_3^2 + gamma_4-next) = O((1+y^2)/m^2)`.
**GAP-2**: the uniform-in-`lambda` remainder bookkeeping (same machinery as Lemma 3.1/3.2
with the tilted cf `phi_lambda`; the needed tilted cf bounds follow from
`|1 - e^{it-lambda}|^2 = (1-e^{-lambda})^2 + 2 e^{-lambda}(1-cos t)` exactly as in
Lemma 2.3). Not written out.

(ii) *(crude uniform bound)* There exist `V_0` and `m_1` such that for all `m >= m_1`
and all interior `k` with `sigma_lambda(k)^2 >= V_0`:
`sigma_lambda^2 log r(k) >= 2/3`.
**GAP-3**: this is a uniform second-difference local-CLT lower bound over the whole
tilt family (truncated geometrics); provable in principle by the Fourier method of §2–3
uniformly in `lambda` (all summands are log-concave lattice variables; standard
Petrov-style machinery), but the uniform constants are not chased here.

NUMERIC CHECK (both parts), `m=30` (`sigma^2 = 785.4`), `lambda(k)` by bisection:
```
k=216: lam=0.0019 s_lam^2=785.3  s_lam^2*logr=0.96417  1-12beta_lam=0.96439
k=210: lam=0.0096 s_lam^2=783.4  s_lam^2*logr=0.96414  1-12beta_lam=0.96471
k=200: lam=0.0224 s_lam^2=774.6  s_lam^2*logr=0.96399  1-12beta_lam=0.96618
k=120: lam=0.146  s_lam^2=487.0  s_lam^2*logr=0.96060  (1-12beta_lam fails: -0.058)
k=40 : lam=0.507  s_lam^2=91.0   s_lam^2*logr=0.96178
k=5  : lam=1.907  s_lam^2=5.8    s_lam^2*logr=0.89507
```
The sharp form (i) is accurate for small `lambda` (`|E_2| <= 2e-3` for `k >= 200`) and
degrades exactly as predicted once `lambda m` is large, where only (ii) is claimed; the
crude bound (ii) holds with huge slack: `min over ALL interior k` of
`sigma_lambda^2 log r(k)` is `0.668 (m=12), 0.678 (m=20), 0.683 (m=30), 0.685 (m=36)`,
always attained at `k=1` (where `r(1) -> 2`, `sigma_lambda^2 -> 1`, `log 2 = 0.693`).

**Lemma 4.6 (extreme tail, `k = O(m^{1/3})`).** For `2 <= k <= (m/C_0)^{1/3}`:
`r(k) >= 1 + 1/(2k)`, and `r(1) >= 3/2`.

*Proof sketch.* `I_m(k)` counts `(c_2,...,c_m)`, `0 <= c_j <= j-1`, `sum c_j = k`.
Without the caps the count is `binom(m-2+k, k)`; cap violations require some `c_j >= j`
with `j <= k`, so `0 <= binom(m-2+k,k) - I_m(k) <= sum_{j=2}^k binom(m-2+k-j, k-j)
= O((k^2/m) binom(m-2+k,k))`. Hence
`r(k) = [(k+1)/k] * [(m+k-2)/(m+k-1)] * (1 + O(k^2/m)) >= 1 + 1/(2k)` for `m >= C_0 k^3`. ∎

NUMERIC CHECK: `m=40`: `r(1)=1.9525, r(2)=1.4652, r(3)=1.3030, r(5)=1.1739, r(8)=1.1020,
r(12)=1.0628`; in every case `r(k) - 1 - 1/(2k) > 0` (margins `+0.45, +0.22, +0.14,
+0.07, +0.04, +0.02`) and `r(k) < (k+1)/k` (limit approached from below).

---

## 5. Synthesis

**Theorem 5.1 (= F2(a), sharpened; modulo GAP-2, GAP-3).**

```
r_m = 1 + sigma_m^{-2} (1 + o(1));   more precisely
sigma^2 ( r_m - 1 ) = 1 - 27/(25 m) + O(m^{-2}) .
```

*Proof (architecture).* Fix `m` large. Split interior `k` by `y = (k - N/2)/sigma`:

1. **Center** `|y| <= y_* := m^{-1/2}`: Lemma 3.2 gives
   `sigma^2 log r(k) = 1 - 12 beta + O(m^{-2})` (the `12 beta y^2` term is `O(m^{-2})`
   here). This region contains the global minimum by steps 2–4, and its minimum value is
   the stated one by Corollary 3.3.
2. **Window** `y_* <= |y| <= m^{1/4}`: by Lemma 4.5(i) with Lemma 4.4,
   `log r(k) >= (1 - 12 beta_lambda - C(1+y^2)/m^2) / sigma_lambda^2` and
   `1/sigma_lambda^2 >= (1 + 12 beta y^2 (1 - o(1)))/sigma^2`; since
   `beta_lambda = beta (1 + o(1))` here, `sigma^2 log r(k) >= 1 - 12 beta + 12 beta y^2 (1-o(1))
   - C(1+y^2)/m^2 > sigma^2 log r_c` as soon as `y^2 >= y_*^2 = 1/m`
   (the margin `12 beta y^2 = 1.08 y^2/m` beats `C(1+y^2)/m^2` for every such `y`
   because both scale linearly in `y^2`, with a factor-`m` gap in the constants).
3. **Bulk tails** `m^{1/4} <= |y|`, but `sigma_lambda^2 >= V_0`: here the deficit is
   macroscopic — by Lemmas 4.3–4.4 the deficit is nondecreasing in `|lambda|` and already
   `>= 12 beta y^2 sigma^2 * (1-o(1)) >= (c/sqrt(m)) sigma^2` at the region's edge — so the
   crude bound 4.5(ii) suffices: `log r(k) >= (2/3)/sigma_lambda^2 >= (2/3)(1 + c m^{-1/2})/sigma^2
   ... ` and in fact once `sigma_lambda^2 <= (2/3) sigma^2 / (1 - 12beta + o(1)) ` the bound
   `(2/3)/sigma_lambda^2 > log r_c` is immediate; for the remaining thin range interpolate
   with 4.5(i) — the two regimes overlap because 4.5(i) stays valid while `lambda <= 1/m`,
   i.e. `|x| <= sigma^2/m ~ m^2/36 ~ 0.75 N/12...`, which covers all `|y| <= sigma/m^{...}`
   well past `m^{1/4}`. (Overlap verified numerically above: at `m=30` the sharp form is
   still accurate at `k=200`, i.e. `y = -0.62`, and the crude form already has 40% slack
   there.)
4. **Extreme tails** `sigma_lambda^2 < V_0` (equivalently `k` or `N-k` below a fixed
   multiple of `V_0`): Lemma 4.6 gives `r(k) >= 1 + 1/(2k) >> 1 + 1/sigma^2`; the
   matching zone `(m/C_0)^{1/3} <= k <= C V_0`-to-bulk is covered by 4.5(ii) since
   `sigma_lambda^2 ~ k -> infinity` there.

By symmetry (`r(N-k) = r(k)`) the same covers `k > N/2`. Hence the global minimum is
attained in region 1 and equals the central value up to `O(m^{-2})`. ∎

**Theorem 5.2 (= F2(b), weakened form; modulo GAP-2, GAP-3).** The argmin satisfies

```
| argmin_k - N/2 |  <=  C sigma m^{-1/2}  =  O(m) .
```

Empirically the argmin is exactly `floor(N/2)` for all `4 <= m <= 56` (for odd `N` the
values `k = floor(N/2)` and `k = ceil(N/2)` tie by symmetry, and the harness reports the
smaller).

*Proof.* Steps 2–4 above exclude `|y| > y_* = m^{-1/2}`, i.e. `|x| > sigma/sqrt(m) ~ m/6`. ∎

**GAP-4 (the exact `<= 1` statement).** The full F2(b) claim follows from the symmetric
unimodality statement: *`k -> r_m(k)` is nonincreasing on `[1, floor(N/2)]`* (then, with
`r(N-k) = r(k)`, the min is at the central one or two values). This is a strict
"2-log-concavity at the ratio level" statement that our expansion cannot resolve below
scale `|x| = O(m)` (adjacent-`k` differences of `log r` near the center are
`~ 24 beta / sigma^4 = O(m^{-7})`, far below any fixed-order Edgeworth error). We record
it as a verified conjecture:
NUMERIC CHECK: exact integer arithmetic, all `5 <= m <= 56`: **zero** violations of
`r(k) >= r(k+1)` on `1 <= k < floor(N/2)`; for `m = 4` exactly one violation (at `k=2`;
`m=4` also has argmin at `|k - N/2| = 1`, still within F2(b)'s tolerance). Command:
```
python3 - <<'EOF'
from mahonian import mahonian
for m in range(5,57):
    a=mahonian(m); N=m*(m-1)//2
    assert all(a[k]**3*a[k+2] >= a[k+1]**3*a[k-1] for k in range(1,N//2)), m
print("unimodal for all 5<=m<=56")
EOF
```

**Theorem/Status 5.3 (= F2(c): not achieved; corrected target).**

1. **The spec's suggested constant is false.** Exactly:
   `sigma^2 (r_5 - 1) = 7/8` and `sigma^2 (r_6 - 1) = 187/216 = 0.8657... < 7/8`.
   So no proof of `c = 7/8` for all `m >= 5` can exist. The sequence
   `m -> sigma^2 (r_m - 1)` is **not** monotone at `m = 5 -> 6`; it is monotone
   increasing on `6 <= m <= 56` (checked exactly). Corrected sharp conjecture:

   ```
   r_m >= 1 + (187/216) / sigma_m^2   for all m >= 5,  with equality iff m = 6.
   ```

   NUMERIC CHECK: `python3 mahonian.py --mmax 40` — `varfit` column: `0.8750 (m=5),
   0.8657 (m=6), 0.8766 (m=7)`, increasing thereafter; exact values `7/8` and `187/216`
   from `fractions` (script in §6).

2. **Reduction.** If GAP-1 is closed with the (numerically supported) constant
   `|E_1(0)| <= 0.4/m^2` for `m >= 6`, and GAP-2/GAP-3 are closed with any explicit
   `m_0`, then for `m >= max(8, m_0)`:
   `sigma^2 (r_m - 1) >= 1 - 27/(25 m) - 0.4/m^2 - o(1) >= 5/6`, and the finitely many
   `5 <= m < max(8, m_0)` are verified by the exact harness (already done to `m = 56`;
   the harness is exact rational arithmetic, so this is a legitimate proof step
   **provided `m_0 <= 56`**, or after extending the run). Conclusion would be
   **`c = 5/6` for all `m >= 5`.**

3. **GAP-5 (why we stop).** Our Lemma 2.3-type tail constants make `m_0` of order
   150–200 rather than `<= 56`, and GAP-2/3 constants are not chased at all. Closing (c)
   along this route requires: (i) the sharper cf tail bound (true size `e^{-cm log m}`,
   cf. the `6e-13` at `m=30`), (ii) explicit Edgeworth remainders (GAP-1), and (iii) a
   harness run to the resulting `m_0` (cheap: exact `mahonian.py` scales past `m = 150`).
   None of these is conceptually hard, but none is done here. **(c) is honestly open in
   this draft.**

---

## 6. Consolidated numeric checks (referee script)

All from `phase2/bruhat/`. Ground truth: `python3 mahonian.py --mmax 40`.

```
python3 - <<'EOF'
import math
from fractions import Fraction
from mahonian import mahonian

# (1) exact constants at m=5,6  -> 7/8 and 187/216
for m in (5,6):
    a=mahonian(m); N=m*(m-1)//2; mid=N//2
    r=Fraction(a[mid]*a[mid], a[mid-1]*a[mid+1]); var=Fraction(m*(m-1)*(2*m+5),72)
    print(m, (r-1)*var)

# (2) central formula: sigma^2 log r_c  vs  1 - 12 beta ; residual * m^2 in [-0.2, 0.2]
for m in (6,10,20,30,40):
    a=mahonian(m); N=m*(m-1)//2; mid=N//2
    s2=m*(m-1)*(2*m+5)/72; c4=sum(j**4-1 for j in range(2,m+1))/2880
    logrc=2*math.log(a[mid])-math.log(a[mid-1])-math.log(a[mid+1])
    print(m, round(s2*logrc,5), round(1-12*c4/s2**2,5), round((s2*logrc-(1-12*c4/s2**2))*m*m,3))

# (3) unimodality (=> exact F2(b)) for 5<=m<=56 : no violations
for m in range(5,57):
    a=mahonian(m); N=m*(m-1)//2
    assert all(a[k]**3*a[k+2] >= a[k+1]**3*a[k-1] for k in range(1,N//2)), m
print("unimodal OK 5..56")
EOF
```
Expected: `5 7/8`, `6 187/216`; the table of §3 (Cor 3.3 check); `unimodal OK 5..56`.

---

## 7. Relation to the literature (as required by the spec)

- Log-concavity of `I_m(k)` itself: Bóna (Electron. J. Combin.); product-closure route
  Hoggar 1974 / Kook 2006. We use only the *strict quantitative* refinements, all proved
  or GAP-flagged above; plain log-concavity is not an ingredient of our route.
- Local CLT / central second difference for the *Gaussian binomial*:
  Canfield–Janson–Zeilberger, arXiv:0908.2089 (Adv. Appl. Math. 2011), Thm 4.6 /
  eq. (4.11). Our Lemma 3.2 is the `[m]_q!` analogue via the identical kernel device
  (Lemma 1.2); §4–5 (tilting, variance domination, deficit monotonicity, global min)
  are the parts they do not prove.
- Edgeworth remainders for sums of independent non-iid bounded lattice variables:
  Petrov, *Sums of Independent Random Variables*, Ch. VII (for GAP-1/GAP-2 closure).
- The hyperbolic inequalities in Lemmas 4.2–4.3 (`v` increasing, `u` decreasing) are
  elementary; we are not aware of a reference stating the consequences
  `Var_q(U_j) <= Var_1(U_j)` and monotonicity in `|log q|` for `q`-uniforms, which may
  be independently useful (they say: *among all exponential tilts of a discrete uniform,
  the uniform itself has maximal variance, monotonically in the tilt*).

## GAP index

- **GAP-1** (Lemmas 3.1/3.2): explicit constants in the Edgeworth remainders
  (structure complete; numerically `|E_1| <= 0.4 (1+y^6)/m^2` for `6 <= m <= 40`).
- **GAP-2** (Lemma 4.5(i)): uniform-in-`lambda` remainder bookkeeping for the tilted
  central expansion (mechanical repetition of §2–3 in the tilted frame).
- **GAP-3** (Lemma 4.5(ii)): uniform crude lower bound `sigma_lambda^2 log r >= 2/3`
  for the tilt family (a uniform LCLT second-difference bound; numerically the constant
  is `0.668+` with min at `k=1`).
- **GAP-4** (Theorem 5.2): unimodality of `k -> r_m(k)` (would upgrade (b) to the exact
  `<= 1` statement; verified exactly for `5 <= m <= 56`).
- **GAP-5** (Status 5.3): explicit-`m_0` constant chase for (c); note the spec's
  `c = 7/8` is disproved at `m = 6`; corrected sharp target `c = 187/216`, safe target
  `c = 5/6` reduced to GAP-1..3 + finite harness run.
