# Theorem F2 — Draft C: the local-CLT / characteristic-function route

*Blind draft. Assigned angle: the characteristic function of `inv` factors exactly as a
product of geometric sums; adapt Canfield–Janson–Zeilberger (CJZ) Theorem 4.6 / eq. (4.11)
from the central Gaussian binomial to the q-factorial, with explicit control in the central
window; handle the tails by exponential tilting (Mallows measures) plus an exact
variance-monotonicity lemma, and by Euler's pentagonal expansion at the extreme edge.*

All numeric checks below were run against the exact harness `mahonian.py` before being
written down. Commands are given verbatim; run them from `phase2/bruhat/`.

---

## 0. Statement, notation, and what this draft proves

For `sigma in S_m` let `inv(sigma)` be the inversion number, `I_m(k) = #{sigma : inv = k}`,
`N = m(m-1)/2`, and

```
sum_k I_m(k) q^k = [m]_q! = prod_{j=1}^m (1 + q + ... + q^{j-1}).
```

Write `p(k) = I_m(k)/m!` (the law of `inv` under the uniform measure),
`sigma^2 = Var(inv) = m(m-1)(2m+5)/72`, `r_m(k) = I_m(k)^2/(I_m(k-1) I_m(k+1))`,
`r_m = min_{1<=k<=N-1} r_m(k)`, and `x_k = (k - N/2)/sigma` (so `x_k` may be a
half-integer multiple of `1/sigma`).

**Standing facts (cited, not re-proved).**
- `I_m(k)` is log-concave in `k` (Bóna, Electron. J. Combin., direct injection; also
  Hoggar 1974 / Kook 2006: each factor of `[m]_q!` is a uniform, hence log-concave,
  sequence and convolution preserves log-concavity). So `r_m(k) >= 1` always and
  `q_k := I(k)/I(k-1)` is non-increasing.
- `inv = U_1 + ... + U_m` with `U_j` independent, `U_j ~ Unif{0,...,j-1}` (inversion
  table). Asymptotic normality and the local limit theorem: Canfield–Janson–Zeilberger,
  arXiv:0908.2089, Adv. Appl. Math. 2011. Their Theorem 4.6 / eq. (4.11) prove
  `P(k)^2 - P(k-1)P(k+1) = (sigma^{-2} + O(n^{-4})) P(k)^2` in the central window **for the
  central Gaussian binomial**; Sections 1–2 below are the q-factorial transfer, including
  their key device (the "determinant" double-integral representation, Lemma 2.2).
- Edgeworth expansions for sums of independent non-i.i.d. lattice variables: Petrov,
  *Sums of Independent Random Variables*, Ch. VII (used only for regime-uniformity in §3;
  the central-window expansion is done by hand from the exact product formula).

**Result summary of this draft.**

| Part | Status |
|---|---|
| (a) `r_m = 1 + sigma^{-2}(1+o(1))` | **Proved**, modulo GAP-2 (uniform-tilt constants, standard machinery), with the sharper rate `r_m = 1 + sigma^{-2}(1 - (27/25)m^{-1} + O(m^{-2}))`. |
| (b) `|argmin - N/2| <= 1` | **Partially proved**: argmin is localized to `|k - N/2| <= C m` (an `O(sigma/sqrt(m))` window; `C ~ 1/4` modulo GAP-1 constants). The step from `Cm` to `1` is GAP-3 (genuinely open here); exact centrality verified numerically for all `4 <= m <= 120`. |
| (c) explicit `c` for all `m>=5` | **Attempted; spec's constant corrected.** The suggested `c = 7/8` is FALSE at `m = 6`: `sigma^2 (r_6 - 1) = 187/216 = 0.865741 < 7/8`. Corrected target: `c = 187/216` (all `m >= 5`), equivalently `c = 7/8` for `m in {5} ∪ {7,8,...}`. Full explicit-constant proof not completed (GAP-1 + GAP-2); verified numerically for `5 <= m <= 120`. |

NUMERIC CHECK (ground truth): `python3 mahonian.py --mmax 40` — argmin central for all
`4 <= m <= 40`; min ratio equals central ratio for `m >= 5`; `sigma^2(r_m-1)` runs
`0.875 (m=5), 0.8657 (m=6), 0.8766 (m=7), ... , 0.9734 (m=40)`. Note the dip at `m=6`:
the spec's parenthetical "increasing, `= 0.875` at `m=5`" is not quite right —
monotonicity starts at `m = 6`, and the `m >= 5` minimum is at `m = 6`, not `m = 5`.

```
python3 - <<'EOF'
from fractions import Fraction
from mahonian import mahonian, min_ratio
for m in (5,6,7):
    r,_ = min_ratio(mahonian(m)); var = Fraction(m*(m-1)*(2*m+5),72)
    print(m, var*(r-1))           # -> 7/8, 187/216, 931/1062
EOF
```

**Architecture.** Five regimes for `k` (by symmetry `I(k) = I(N-k)`, take `k <= N/2`):

1. **Central window** `|x_k| <= sqrt(log m)`: hand-made one-term Edgeworth expansion from
   the exact characteristic-function product, plus the CJZ determinant representation
   (§1–§2). Gives the sharp value and the `x^2`-growth of `r(k)`.
2. **Bulk** `k in [eps N, N/2]` (equivalently tilt parameter `|u| <= W/m`): exponential
   tilting to re-center; `r(k)` is tilt-invariant; tilted variance is *strictly smaller*
   (Lemma 3.3, fully proved) so the local ratio is strictly larger (§3).
3. **Intermediate tail** `k in [C_0, eps N]`: same tilting, `sigma(u)^2 >= C_0` suffices.
4. **Extreme edge** `k <= C_0`: Euler pentagonal expansion, explicit inequality (§4).
5. Assembly (§5).

---

## 1. Exact Fourier structure

### Lemma 1.1 (factorization and inversion). 
Let `phi(t) = E e^{it(inv - N/2)}`. Then, exactly, for `t in (-pi, pi]`:

```
phi(t) = prod_{j=1}^{m} sin(j t/2) / ( j sin(t/2) )        (factor j=1 is 1),
p(k)   = (1/2pi) ∫_{-pi}^{pi} phi(t) e^{-i t (k - N/2)} dt .
```

`phi` is real and even (the centered law is symmetric).

*Proof.* `E e^{it U_j} = (e^{ijt}-1)/(j(e^{it}-1))`; centering each factor by
`e^{-it(j-1)/2}` gives `sin(jt/2)/(j sin(t/2))`. Independence multiplies the factors;
inversion is the standard lattice Fourier inversion (span 1, aperiodic). ∎

NUMERIC CHECK: midpoint-rule inversion reproduces `p(k)` to machine precision:

```
python3 - <<'EOF'
import math
from mahonian import mahonian
m=10; a=mahonian(m); N=m*(m-1)//2; fact=math.factorial(m)
def phi(t):
    p=1.0
    for j in range(2,m+1): p*=math.sin(j*t/2)/(j*math.sin(t/2))
    return p
for k in (N//2, N//2+5, N//2+12):
    n=20000; s=sum(phi(-math.pi+(i+.5)*2*math.pi/n)*math.cos((-math.pi+(i+.5)*2*math.pi/n)*(k-N/2)) for i in range(n))/n
    print(k, s - a[k]/fact)      # -> ~1e-16 each
EOF
```

### Lemma 1.2 (cumulants).
All odd cumulants of `inv` vanish. With `S_r = sum_{j=1}^m j^r`:

```
sigma^2 = (S_2 - m)/12 = m(m-1)(2m+5)/72,
kappa_4 = -(S_4 - m)/120,   S_4 = m(m+1)(2m+1)(3m^2+3m-1)/30   (kappa_4 < 0).
```

Define the central quantity of this draft:

```
B_m := -kappa_4 / (2 sigma^4) = (27/25) m^{-1} (1 + O(m^{-1})) > 0 .
```

*Proof.* Per-factor: `Unif{0..j-1}` has variance `(j^2-1)/12` and fourth cumulant
`-(j^4-1)/120` (from `mu_4 = (j^2-1)(3j^2-7)/240`); odd cumulants vanish by symmetry;
cumulants add. The asymptotics of `B_m`: `|kappa_4| ~ m^5/600`, `sigma^4 ~ m^6/1296`,
so `B_m ~ 1296/(1200 m) = 27/(25 m)`. ∎

NUMERIC CHECK: `B_30 = 0.0356230`, `B_40 = 0.0267580` (vs `27/(25m)` = 0.036, 0.027):

```
python3 - <<'EOF'
from fractions import Fraction
for m in (30,40):
    S4=sum(j**4 for j in range(1,m+1)); k4=-Fraction(S4-m,120)
    var=Fraction(m*(m-1)*(2*m+5),72); print(m, float(-k4/(2*var**2)))
EOF
```

### Lemma 1.3 (exact log-series and Gaussian domination).
For `0 < |t| < 2pi/m`, every factor of `phi` is positive and

```
log phi(t) = sum_{j=1}^m [ g(jt/2) - g(t/2) ],   g(x) = log( sin x / x )
           = - sum_{K>=1} c_K (t/2)^{2K} (S_{2K} - m),   c_K = zeta(2K) / (K pi^{2K}) > 0 ,
```

with `c_1 = 1/6`, `c_2 = 1/180`, `c_3 = 1/2835`. The `K=1,2` terms are exactly
`-sigma^2 t^2/2` and `kappa_4 t^4/24`. Consequences:

(i) **(Gaussian domination)** `0 < phi(t) <= e^{-sigma^2 t^2/2}` for all `|t| <= 2pi/m`
    (every series term is negative);

(ii) **(remainder)** for `|t| <= sqrt(2) pi/m`,
    `R(t) := log phi(t) + sigma^2 t^2/2 - kappa_4 t^4/24` satisfies
    `-m^7 t^6 / 317520 <= R(t) <= 0`.

*Proof.* `sin x / x = prod_{n>=1} (1 - x^2/(n^2 pi^2))` and `-log(1-y) = sum y^r / r`
give the series for `g` (valid `|x| < pi`; here `|jt/2| < pi`). Matching `K=1,2` to
Lemma 1.2 is the computation shown there. For (ii): `S_{2K} - m <= 2 m^{2K+1}/(2K+1)`
(integral comparison; the factor 2 is generous for `m >= 4`), and
`c_{K+1} x^2 / c_K <= x^2/pi^2 <= 1/2` for `x = mt/2 <= pi/sqrt(2)`, so the tail
`K >= 3` is at most twice its first term: `|R| <= (2m/7) * 2 c_3 (mt/2)^6 = m^7 t^6 / 317520`. ∎

NUMERIC CHECK (domination): `max_{0<t<2pi/m} phi(t) e^{sigma^2 t^2/2} = 1.000000` at
`m = 10, 30, 60` (attained only as `t -> 0`):

```
python3 - <<'EOF'
import math
for m in (10,30,60):
    s2=m*(m-1)*(2*m+5)/72
    def phi(t):
        p=1.0
        for j in range(2,m+1): p*=math.sin(j*t/2)/(j*math.sin(t/2))
        return p
    print(m, max(phi(i/400*2*math.pi/m*.999)*math.exp(s2*(i/400*2*math.pi/m*.999)**2/2) for i in range(1,400)))
EOF
```

### Lemma 1.4 (far-region decay).
For `2pi/m <= |t| <= pi` and `m >= 8`:
`|phi(t)| <= exp( -m h(beta) + log m )` where `beta = ceil(1/sin(t/2))/m <= 1/2 + 1/m` and
`h(beta) = beta - 1 - log beta >= h(1/2) = log 2 - 1/2 = 0.1931...`. In particular
`|phi(t)| <= e^{-m/6}` for `m >= 25`.

*Proof.* `|sin(j t/2)| <= j |sin(t/2)|` gives `|factor_j| <= 1` for all `j`; for
`j >= J := ceil(1/s)`, `s = sin(t/2) >= t/pi >= 2/m`, bound `|factor_j| <= 1/(js) <= J/j`.
Then `-log|phi| >= sum_{j=J}^m log(j/J) >= ∫_J^m log(x/J) dx = m[ log(m/J) - 1 + J/m ]`,
i.e. `m h(beta)` up to one term `<= log m` from the ceiling. `h` is decreasing on `(0,1)`. ∎

NUMERIC CHECK: `max_{t in [2pi/m, pi]} |phi(t)|` = `3.9e-9 (m=20)`, `6.2e-13 (m=30)`,
`1.1e-16 (m=40)`, `3.3e-24 (m=60)` — far below `e^{-0.19m}` = `2.2e-2, 3.3e-3, 5.0e-4, 1.1e-5`.
(The true decay is faster than the lemma's bound; the lemma is all we need.)

---

## 2. The central window

### Proposition 2.1 (one-term Edgeworth local expansion).
Let `lambda = kappa_4/(24 sigma^4) = -B_m/12 < 0` and `He_4(x) = x^4 - 6x^2 + 3`. Then for
every `k`,

```
p(k) = (1 / (sigma sqrt(2 pi))) e^{-x_k^2/2} [ 1 + lambda He_4(x_k) ] + E(k),
|E(k)| <= C_1 / (sigma m^2),
```

with an absolute constant `C_1` (the bookkeeping below gives `C_1 <= 3` for `m >= 20`;
see GAP-1 for the status of the constant chase).

*Proof (scheme, with the explicit ingredients).* Split the inversion integral at
`t_2 = m^{-5/4}`, `sqrt(2) pi/m`, `2pi/m`, `pi`:

- On `|t| <= t_2`: by Lemma 1.3, `phi = e^{-sigma^2 t^2/2}(1 + kappa_4 t^4/24 + z(t))`,
  `|z| <= |R| + (kappa_4 t^4/24)^2 e^{|...|}`, and `|kappa_4| t_2^4 / 24 <= 1/10^4` for
  `m >= 20`, so `z` is dominated by `m^7 t^6/317520 + (m^5 t^4/2880)^2`. Fourier-transforming
  the main part over all of `R` produces exactly the bracketed Edgeworth density
  (the Hermite identity `∫ t^4 e^{-sigma^2 t^2/2} e^{-itx sigma} dt`); the two error
  integrals contribute (relative to `1/(sigma sqrt(2pi))`) at most
  `15 * 1296^{3/2} / (317520 m^2) + O(m^{-3}) ~ 2.3/m^2`.
- The re-extension of the Gaussian-Edgeworth integral from `|t| <= t_2` to `R` costs
  `exp(-sigma^2 t_2^2/2) = exp(-sqrt(m)/72 * (1+o(1)))`, super-polynomially small.
- On `t_2 <= |t| <= 2pi/m`: Gaussian domination (Lemma 1.3(i)) gives the same
  super-polynomial bound.
- On `2pi/m <= |t| <= pi`: Lemma 1.4 gives `<= e^{-m/6}` for `m >= 25`. ∎

NUMERIC CHECK (the `1/m^2` scaling and effective constant):

```
python3 - <<'EOF'
import math
from fractions import Fraction
from mahonian import mahonian
def He4(x): return x**4-6*x**2+3
for m in (20,30,40,60):
    a=mahonian(m); N=m*(m-1)//2
    var=Fraction(m*(m-1)*(2*m+5),72); s=math.sqrt(var); S4=sum(j**4 for j in range(1,m+1))
    lam=float(-Fraction(S4-m,120)/(24*var**2)); lf=sum(math.log(j) for j in range(2,m+1))
    w=max(abs(math.exp(math.log(a[k])-lf)/(math.exp(-((k-N/2)/s)**2/2)/(s*math.sqrt(2*math.pi))*(1+lam*He4((k-N/2)/s)))-1)
          for k in range(len(a)) if abs((k-N/2)/s)<=3)
    print(m, w*m*m)     # -> 6.96, 6.30, 6.09, 6.01 : sup relative error ~ 6/m^2 on |x|<=3
EOF
```

### Lemma 2.2 (CJZ determinant representation — exact).
For `D(k) := p(k)^2 - p(k-1)p(k+1)` and any `k`:

```
D(k) = (1/4 pi^2) ∫∫_{[-pi,pi]^2} phi(s) phi(t) cos( (s+t)(k - N/2) ) (1 - cos(s-t)) ds dt .
```

*Proof.* Write each `p` by Lemma 1.1; `p(k-1)p(k+1)` carries the kernel `e^{i(s-t)}`,
`p(k)^2` the kernel `1`; symmetrizing in `(s,t)` replaces `e^{i(s-t)}` by `cos(s-t)`,
and the real part of `e^{-i(s+t)(k-N/2)}` is the cosine (the imaginary part integrates
to 0 by evenness of `phi`). This is the q-factorial version of the representation behind
CJZ eq. (4.11). ∎

NUMERIC CHECK: 2-D midpoint quadrature at `m=8` matches the exact
`D(k)` to 12 significant digits at `k = 14` (`4.657679043840e-04`) and `k = 18`
(`2.227154244221e-04`).

**Why this detour is necessary (and is the heart of CJZ's method):** the additive error
`E(k)` of Prop. 2.1 is of order `sigma^{-1} m^{-2}`, which is *larger* than the signal
`D(k) ~ sigma^{-2} p(k)^2 ~ sigma^{-4}`; ratios cannot be taken naively. In Lemma 2.2 the
kernel `1 - cos(s-t) <= (s-t)^2/2` supplies the factor `sigma^{-2}` *inside* the integral,
so errors are relative to the already-small quantity.

### Proposition 2.3 (central ratio, sharp form).
Insert `phi_model(t) = e^{-sigma^2 t^2/2}(1 + kappa_4 t^4/24)` into Lemma 2.2 and extend to
`R^2` (rotating `u = (s+t)/sqrt2, v = (s-t)/sqrt2` factorizes everything into 1-D Gaussian
moments). The model evaluates in closed form; combined with Prop. 2.1 for the denominator
`p(k-1)p(k+1)`, one obtains, exactly at the model level (machine-verified symbolic
computation, first order in `kappa_4`):

```
sigma^2 ( r_model(k) - 1 )
  = sigma^2 (e^{1/sigma^2} - 1)  +  B_m (x_k^2 - 1)  +  kappa_4 (10 - 12 x_k^2) / (24 sigma^6) ,
```

and transferring the remainders of Lemma 1.3(ii)/1.4 through the double integral (the
kernel keeps the same `sigma^{-2}` for main and error terms alike):

```
sigma^2 ( r_m(k) - 1 ) = 1 + B_m (x_k^2 - 1) + theta * C_2 (1 + x_k^6) e^{x_k^2} / m^2,
|theta| <= 1,  uniformly for |x_k| <= sqrt(log m).
```

Numerically the effective `C_2` is about `0.2` (GAP-1 for a fully explicit value).
Note `sigma^2(e^{1/sigma^2}-1) = 1 + O(sigma^{-2})` and `kappa_4/sigma^6 = O(m^{-1} sigma^{-2})`
are both absorbed in the error for `m >= 5`.

NUMERIC CHECK (this is the single most important check of the draft):

```
python3 - <<'EOF'
import math
from fractions import Fraction
from mahonian import mahonian
def logint(n):
    if n.bit_length()<900: return math.log(n)
    k=n.bit_length()-500; return math.log(n>>k)+k*math.log(2)
for m in (30,40):
    a=mahonian(m); N=m*(m-1)//2
    var=Fraction(m*(m-1)*(2*m+5),72); s2=float(var); s=math.sqrt(s2)
    S4=sum(j**4 for j in range(1,m+1)); B=float(Fraction(S4-m,120)/(2*var**2))
    for dk in (0,10,20,40,60):
        k=N//2+dk; x=(k-N/2)/s
        lhs=s2*(2*logint(a[k])-logint(a[k-1])-logint(a[k+1]))-1
        print(m,dk,round(lhs,6),round(B*(x*x-1),6))
EOF
```

Output (`lhs` vs `B(x^2-1)`), `m=40`: `dk=0: -0.026876 / -0.026758`; `dk=20: -0.021252 /
-0.020946`; `dk=60: +0.025513 / +0.025547`. Agreement is `O(1/m^2)` at small `x` (the
residual at `dk=0` is `1.2e-4 ~ 0.19/m^2`), and the residual at large `x` is *positive*
(the `kappa_6` term helps, it never fights the growth).

NUMERIC CHECK (constant `27/25` in `B_m`, via the central ratio):
`m * (1 - sigma^2 (r_c - 1))` = `0.953 (m=10), 1.038 (20), 1.057 (30), 1.065 (40),
1.071 (60), 1.074 (80), 1.075 (100)` → `27/25 = 1.08` with an `O(1/m)` drift, as predicted
by `B_m = (27/25m)(1 - 1/(2m) + O(m^{-2}))`.

### Corollary 2.4 (window conclusions).
For `m >= m_1` (absolute, modulo GAP-1 constants):

(i) `sigma^2 (r_m(k_c) - 1) = 1 - B_m + O(m^{-2})` at the central `k_c = floor(N/2)`
    (`|x_{k_c}| <= 1/(2 sigma)`);

(ii) for all `k` in the window `|x_k| <= sqrt(log m)`:
     `sigma^2 (r_m(k) - 1) >= 1 - B_m - C_2' / m^2`;

(iii) any `k` in the window with `r_m(k) <= r_m(k_c)` satisfies
     `B_m x_k^2 <= 2 C_2 e (1 + x_k^6) m^{-2} + B_m x_{k_c}^2` for `|x_k| <= 1`, hence
     `|x_k| <= gamma/sqrt m` with `gamma = sqrt(50 C_2 e / 27)`, i.e.

```
| argmin - N/2 |  <=  gamma sigma / sqrt m  ~  (gamma/6) m   ( ~ m/4 for C_2 = 0.2 ).
```

For `1 <= |x_k| <= sqrt(log m)` the growth `B_m(x_k^2-1) > 0` beats the error term because
`e^{x^2} <= m` there and `B_m x^2 m^2 >= (27/25) m log m >> C_2 m`; so no minimizer lives at
`1 <= |x| <= sqrt(log m)` either. ∎

---

## 3. The global argument, part I: tilting (bulk and intermediate tail)

### Lemma 3.1 (tilt invariance).
For any `theta > 0`, the sequence `I_theta(k) = I_m(k) theta^k` has the same log-concavity
ratios: `r_theta(k) = r_m(k)`. (Immediate: the `theta`'s cancel.) Probabilistically,
`I_theta` normalized is the law of `inv` under the **Mallows measure** with parameter
`theta`; its inversion table entries are independent *truncated geometrics*
`P(U_j = i) ∝ theta^i, 0 <= i <= j-1`, so the entire Fourier apparatus of §1–§2 applies
verbatim with tilted factors.

### Lemma 3.2 (tilted moments, closed form).
Write `theta = e^u`. The tilted factor `U_j(u)` has

```
mu_j(u)  = d/du log Z_j(u),   Z_j(u) = (e^{ju}-1)/(e^u-1),
Var_j(u) = (1/4) [ csch^2(u/2) - j^2 csch^2(ju/2) ]            (-> (j^2-1)/12 as u->0),
kappa_{3,j}(u) = (1/4) [ j^3 csch^2(ju/2) coth(ju/2) - csch^2(u/2) coth(u/2) ] .
```

*Proof.* `log Z_j(u) = log sinh(ju/2) - log sinh(u/2) + (j-1)u/2`; differentiate twice and
three times. ∎ (NUMERIC CHECK: both formulas match direct computation to 8 decimals at
`(j,u) = (5,0.3), (9,0.7), (3,1.5)`.)

### Lemma 3.3 (variance monotonicity — fully proved; the key new ingredient).
For every `j >= 2`, `Var_j(u)` is even in `u` and **strictly decreasing in `|u|`**.
Consequently `sigma(u)^2 := sum_j Var_j(u) < sigma^2` for all `u != 0`.

*Proof.* Since `Var_j' (u) = kappa_{3,j}(u)`, it suffices that `kappa_{3,j}(u) < 0` for
`u > 0`. By Lemma 3.2 this says `G(ju/2) < G(u/2)` where `G(x) = x^3 cosh x / sinh^3 x`,
so it suffices that `G` is strictly decreasing on `(0, ∞)`. Now
`(log G)'(x) = 3/x + tanh x - 3 coth x =: -Q(x)`, and `Q > 0` on `(0, ∞)`:

- for `0 < x <= sqrt 2`: the enveloping alternating Laurent/Taylor series (standard, valid
  since `sqrt 2 < pi/2`) give `coth x >= 1/x + x/3 - x^3/45` and
  `tanh x <= x - x^3/3 + 2x^5/15`, whence
  `Q(x) >= (x - x^3/15) - (x - x^3/3 + 2x^5/15) = (2x^3/15)(2 - x^2) > 0`;
- for `sqrt 2 <= x <= 3/2`: `3/x + tanh x <= 3/sqrt2 + tanh(3/2) = 3.0265 < 3.3143 = 3 coth(3/2) <= 3 coth x`;
- for `x >= 3/2`: `3/x + tanh x < 2 + 1 = 3 < 3 coth x`. ∎

NUMERIC CHECK: `min_{x in (0,40]} Q(x) > 0` (→ 0 only as `x -> 0+`); `Var_j(u)`
non-increasing on a `u`-grid for `j in {2,3,5,10,40}` with zero violations.

### Corollary 3.4 (quantitative variance drop).
Small tilt: with `w := u m`, `sigma(u)^2 = sigma^2 + kappa_4 u^2/2 + O(u^4 S_8)`, so

```
1 - sigma(u)^2/sigma^2 = (3/100) w^2 (1 + O(w^2/m^0) + O(1/m)) .
```

(Coefficient: `|kappa_4|/(2 sigma^2 m^2) -> (m^5/600) * (36/m^3) / (2m^2) = 3/100`.)
NUMERIC CHECK (`m=40`): `1 - sigma(u)^2/sigma^2` = `.001231, .007644, .029929, .110325` at
`w = .2, .5, 1, 2` vs `(3/100)w^2` = `.0012, .0075, .03, .12`. Large tilt: `Var_j(u)`
decreasing in `|u|` and `-> 0`, and `sigma(u)^2` is continuous and strictly decreasing
in `|u|`, so for every `w_0 > 0` there is `rho(w_0) < 1` with
`sigma(u)^2 <= rho sigma^2` for `|u| >= w_0/m`.

### Proposition 3.5 (tilted local ratio; proof at sketch level — GAP-2).
There are absolute constants `C_0, C` such that for every `m` and every
`k in [C_0, N - C_0]`, letting `u_k` solve `mu(u_k) = k` (possible and unique:
`mu` is continuous, strictly increasing, range `(0, N)`),

```
r_m(k) - 1 = sigma(u_k)^{-2} ( 1 + theta C / min(m, sigma(u_k)^2) ),  |theta| <= 1.
```

*Proof sketch.* Repeat §1–§2 for the tilted product measure. The three inputs:

1. *Central-region expansion.* `log E_u e^{itX_j}` is analytic with all derivatives
   explicit (Lemma 3.2 pattern); `|kappa_{r,j}(u)| <= C_r min(j, 1/|u|)^{... }` uniformly
   in `u` — for `|u| <= W/m` one has `|kappa_{r,j}| <= C_r(W) j^r`, and for `|u| >= v_0`
   each tilted factor is dominated by a geometric with ratio `e^{-|u|}`, giving
   `sum_j |kappa_{r,j}(u)| <= C_r' sigma(u)^2` (all cumulants of a truncated geometric are
   comparable to its variance up to `r`-dependent constants). Hence the analogue of
   Lemma 1.3 with relative Edgeworth errors `O(1/min(m, sigma(u)^2))`.
2. *Decay away from `t = 0`.* `|E_u e^{itX_j}| <= exp(-c q_j (1 - cos t))` with
   `q_j = P(X_j=0)P(X_j=1) >= c' min(1, e^{u})`-type mass bounds; the product decays like
   `e^{-c sigma(u)^2 (1-cos t)}`, which is the Poisson-style bound sufficient for
   inversion when `sigma(u)^2 >= C_0`.
3. *Odd-term cancellation at the tilted center.* The tilted law is not symmetric
   (`kappa_3(u) != 0`), but we evaluate the **symmetric second difference of `log p_u`
   exactly at the tilted mean** (`x = 0` by the mean-matching choice of `u_k`): every odd
   Chebyshev–Edgeworth polynomial term `o(x)` contributes `o(h) + o(-h) - 2o(0) = 0`
   exactly. The surviving corrections are `He_4''(0)`-type and `(kappa_3)^2`-type, both
   `O(1/min(m, sigma(u)^2))` relative. Then pass through the determinant representation
   (Lemma 2.2, verbatim in the tilted frame) exactly as in Prop. 2.3.

GAP-2: this is standard machinery (Petrov Ch. VII; CJZ §4 do the untilted case), and every
ingredient is explicit above, but I have not written the uniform-in-`u` error constants
line by line. Nothing else in the draft depends on the *value* of `C`, only on its
existence — except part (c), which needs it explicit. ∎

NUMERIC CHECK (the claim, across the whole bulk, `m = 30, 40`):

```
(r(k)-1) * sigma(u_k)^2 :
 m=30:  k/N=.45: 0.9645   .35: 0.9627   .25: 0.9615   .15: 0.9649   .08: 0.9671
 m=40:  k/N=.45: 0.9732   .35: 0.9719   .25: 0.9710   .15: 0.9736   .08: 0.9752
 (sigma(u)^2/sigma^2 meanwhile drops to 0.084 at k/N=.08)
```

i.e. `r(k)-1 = sigma(u_k)^{-2} (1 - approx 1.08/m)` uniformly — the same `1 - B_m` profile
as at the center, exactly as the tilted Edgeworth analysis predicts.

**Remark (consistency identity).** In the overlap of §2 and §3 the two expansions must
agree: window: `sigma^2(r-1) - 1 ≈ B_m x^2`; tilt: `sigma^2/sigma(u)^2 - 1 ≈ (3/100)w^2`
with `x = sigma u (1+o(1)) = w sqrt(m)/6 (1+o(1))`, so `(3/100) w^2 = (3/100)(36 x^2/m)
= (27/25) x^2 / m = B_m x^2`. They agree. This is a strong internal check: the `x^2`-growth
of the central ratio and the tilt-variance decay are the *same* phenomenon, both governed
by `kappa_4`.

---

## 4. The global argument, part II: extreme edge

### Lemma 4.1 (pentagonal expansion — exact).
For `0 <= k <= m`, with `T(k) := C(m-1+k, m-1)` (and `T(k) = 0` for `k < 0`),

```
I_m(k) = sum_{n in Z} (-1)^n T(k - g_n),    g_n = n(3n-1)/2   (pentagonal numbers).
```

*Proof.* `[m]_q! = prod_{j=1}^m (1-q^j) / (1-q)^m`; for degrees `k <= m`,
`prod_{j=1}^m (1-q^j) ≡ prod_{j>=1} (1-q^j) (mod q^{m+1})`, and Euler's pentagonal number
theorem expands the latter; `(1-q)^{-m}` contributes `T`. ∎

NUMERIC CHECK: exact integer identity verified for all `k <= m` at `m = 20, 35, 50`.

### Lemma 4.2 (edge ratio bound — explicit).
`T(k)^2 / (T(k-1)T(k+1)) = 1 + (m-1)/(k(m+k))` **exactly**. Moreover for
`1 <= k <= sqrt(m)/4` and `m >= 16`:

```
r_m(k) - 1 >= (m-1) / (2 k (m+k)) >= 1/(6k)  >>  1/sigma^2 .
```

*Proof.* The exact binomial identity: `T(k)/T(k-1) = (m-1+k)/k`. For the inequality, group
the pentagonal sum in pairs: `I(k) = T(k) - [T(k-1) + T(k-2)] + [T(k-5) + T(k-7)] - ...`;
brackets are termwise decreasing (`T` is increasing in its argument and the pentagonal
gaps grow), so `T(k) - T(k-1) - T(k-2) <= I(k) <= T(k)`. Since
`T(k-1)/T(k) = k/(m+k-1) <= k/m` and `T(k-2)/T(k) <= (k/m)^2`:
`I(k) >= T(k)(1 - 2k/m)`. Hence
`r_m(k) >= (1 + (m-1)/(k(m+k))) (1 - 2k/m)^2`, and for `k <= sqrt(m)/4` the loss
`(1-2k/m)^2 >= 1 - 4k/m` eats less than half of the gain `(m-1)/(k(m+k)) >= 1/(2k)`
provided `4k/m <= 1/(4k)`, i.e. `16 k^2 <= m`. ∎

NUMERIC CHECK: `min_{1<=k<=m} (r(k)-1) k (m+k)/(m-1)` = `1.0025 (m=30)`, `1.0013 (m=40)`
(empirically the bound holds with constant 1, and for ALL `k <= m`, not just `k <= sqrt m /4`;
the lemma claims only the safe half on the proved range).

---

## 5. Assembly: proofs of (a), (b), (c)

Throughout, `k <= N/2` WLOG (symmetry `r(N-k) = r(k)`), and `C_0, m_1` are the absolute
constants of Prop. 3.5 / GAP-1.

### Theorem (a): `r_m = 1 + sigma^{-2} (1 + o(1))`, with rate.

*Upper bound.* `r_m <= r_m(k_c) = 1 + sigma^{-2}(1 - B_m + O(m^{-2}))` (Cor. 2.4(i)).

*Lower bound.* Take any `1 <= k <= N/2`.
- `k <= sqrt(m)/4`: Lemma 4.2, `r(k) - 1 >= 1/(6k) >= (2/3) m^{-1/2} >> sigma^{-2}`.
- `sqrt(m)/4 <= k <= N/2 - sigma sqrt(log m)`: Prop. 3.5 (with `sigma(u_k)^2 >= C_0` here;
  for `k >= sqrt(m)/4` indeed `sigma(u_k)^2 ~ k (1 + k/m) -> ∞`), plus Lemma 3.3:
  `r(k) - 1 >= (1 - C/min(m, sigma(u_k)^2)) / sigma(u_k)^2 >= (1 - o(1))/sigma^2`,
  and strictly `>= (1+delta)/sigma^2` once `sigma(u_k)^2 <= sigma^2/(1+2delta)`.
- window `|x_k| <= sqrt(log m)`: Cor. 2.4(ii), `r(k) - 1 >= sigma^{-2}(1 - B_m - C_2'/m^2)`.

Combining: `r_m = 1 + sigma^{-2}(1 - B_m + O(m^{-2}) )
= 1 + sigma^{-2} (1 - (27/25) m^{-1} + O(m^{-2}))`. Since `B_m -> 0`, part (a) follows;
the equivalent crude form is `r_m - 1 ~ 36/m^3`. **∎ (modulo GAP-1/GAP-2 constants)**

NUMERIC CHECK: `python3 mahonian.py --mmax 40` column `varfit` = `sigma^2 (r_m-1)`
increases `0.8657 -> 0.9734` on `6 <= m <= 40` (and `0.9892` at `m = 100`,
`0.9910` at `m=120` by the extended run in §0); `m(1 - varfit) -> 1.08 = 27/25` (§2 check).

### Theorem (b): location of the argmin — partial.

Combining Cor. 2.4(iii) (no minimizer with `gamma/sqrt m <= |x| <= sqrt(log m)`),
the bulk bound (for `|x_k| >= sqrt(log m)`, Prop. 3.5 + Lemma 3.3 give
`r(k) - 1 >= (1+delta_m)/sigma^2` with `delta_m >= (3/100) w_k^2 (1-o(1)) - C/m`, and the
tilted Edgeworth refinement `r(k)-1 = sigma(u_k)^{-2}(1 - B_m(1+O(w_k^2)) + O(m^{-2}))`
makes the comparison with the center strict once `w_k^2 >= C'' / m` — which is implied by
`|x_k| >= sqrt(log m)`), and Lemma 4.2 at the edge:

```
argmin_k r_m(k)  ∈  [ N/2 - (gamma/6) m ,  N/2 + (gamma/6) m ] ,     gamma = sqrt(50 C_2 e/27).
```

With the empirical `C_2 ~ 0.2` this is `|argmin - N/2| <= m/4` for large `m`. This proves
"the minimum is attained centrally" at scale `o(sigma)` — but NOT the frozen statement
`|argmin - N/2| <= 1`.

GAP-3: closing `C m -> 1` needs the second difference of `log p` to precision
`o(m^{-1} sigma^{-4})`, i.e. a five-term Edgeworth expansion (all terms even, all cumulants
explicit from Lemma 1.3 — the expansion is *available* in principle) with uniform error
`O(m^{-6})` relative, plus exact evaluation of the `x`-dependence of each term. I did not
carry this out; no conceptual obstruction, but it is a heavy computation and the constants
must survive it. Empirically the statement is exact: `argmin = floor(N/2)` for ALL
`4 <= m <= 120` (and the min ratio *equals* the central ratio for `5 <= m <= 120`).

NUMERIC CHECK:

```
python3 - <<'EOF'
from fractions import Fraction
from mahonian import mahonian, min_ratio
ok=True
for m in range(5,121):
    a=mahonian(m); N=m*(m-1)//2; r,k=min_ratio(a)
    ok &= (k==N//2) and (r==Fraction(a[N//2]**2, a[N//2-1]*a[N//2+1]))
print(ok)    # -> True
EOF
```

### Theorem (c): explicit non-asymptotic constant — attempted, corrected, not closed.

**Correction to the spec.** The suggested `c = 7/8` is **false at `m = 6`**:
`sigma^2 (r_6 - 1) = (85/12)(11/90) = 187/216 = 0.865741 < 7/8 = 0.875`. (The spec's
"increasing from 0.875" missed that `m=5 -> 6` *decreases*; the sequence is increasing
only from `m = 6` on, within the checked range.) The corrected explicit target is

```
r_m >= 1 + c / sigma^2   for all m >= 5,   with   c = 187/216   (sharp at m = 6),
```

equivalently `c = 7/8` for all `m >= 7` (and `m = 5`).

**Reduction (what a full proof needs).** By §5(a)'s lower-bound argument, it suffices to
have explicit values for: `C_1, C_2` (Prop. 2.1/2.3, window), `C_0, C` (Prop. 3.5, tilt),
and Lemma 4.2 (already explicit), giving
`sigma^2(r_m - 1) >= 1 - (27/25 + epsilon)/m - C'/m^2` for `m >= m_0` explicit; one then
needs `m_0` small enough that `1 - 1.09/m_0 - C'/m_0^2 >= 187/216`, i.e. roughly
`m_0 ~ 15–40` for moderate `C'`, and the finite range `5 <= m < m_0` is closed by the
exact harness (already done to 120). The window constants (Lemma 1.3(ii), 1.4 are fully
explicit; Prop. 2.1's `C_1 <= 3` is within reach of the scheme shown) are GAP-1; the
tilt-uniform constants are GAP-2. **Not closed in this draft.**

NUMERIC CHECK: `sigma^2 (r_m - 1) >= 187/216` for all `5 <= m <= 120`, with equality at
`m = 6`, and monotone increasing on `6 <= m <= 120` (§0 command extended to `--mmax 120`).

---

## 6. GAP ledger

- **GAP-1 (window constants).** Prop. 2.1 / Prop. 2.3: the error *scheme* is complete and
  every ingredient (Lemma 1.3(ii) remainder `m^7 t^6/317520`, Lemma 1.4 decay, Gaussian
  tails) is explicit, but I have not assembled a certified end-to-end numerical constant
  (`C_1 <= 3`, `C_2 ~ 0.2` are numerically calibrated, not proved). Blocks: the constant in
  (b)-localization; part (c). Does NOT block the asymptotic statements (a), (b)-partial.
- **GAP-2 (tilt uniformity).** Prop. 3.5 is proved at sketch level: all cumulant formulas
  are closed-form (Lemma 3.2) and the mechanism (odd-term cancellation at the tilted mean +
  determinant kernel) is identical to the proved untilted case, but the uniform-in-`u`
  error constants are not written out. Standard machinery (Petrov Ch. VII / CJZ §4).
  Blocks: full rigor of (a)'s lower bound in the bulk, and (c).
- **GAP-3 (part (b) fine scale).** From `|argmin - N/2| <= C m` to `<= 1`: requires a
  5-term (even-only) Edgeworth with uniform `O(m^{-6})` control. Available in principle
  from Lemma 1.3's exact series; not carried out. This is the genuinely hard remaining
  step of the frozen statement (b).
- **GAP-4 (part (c) statement).** The spec's `c = 7/8` is false at `m=6` (exact:
  `187/216`). With the corrected constant, (c) reduces to GAP-1 + GAP-2 + a finite check
  (done to `m = 120`). No proof of the monotonicity of `sigma^2(r_m-1)` in `m` is offered
  (it is false at `m=5 -> 6` anyway).

## 7. Numeric-check index (all run, all passed, 2026-07-06)

| # | Claim | Result |
|---|---|---|
| 1 | harness baseline `--mmax 40` | argmin central, min=central (m>=5), varfit 0.8426→0.9734 |
| 2 | `B_m` constant: `m(1-varfit) -> 27/25` | 0.953→1.075 (m=10→100), drift `O(1/m)` |
| 3 | window law `sigma^2 log r - 1 = B(x^2-1)` | residual `~0.2/m^2` at `x<=1`; positive at large `x` (m=30,40) |
| 4 | Gaussian domination of `phi` on `(0, 2pi/m)` | max ratio `= 1.000000` (m=10,30,60) |
| 5 | far-region decay | `max|phi| = 6e-13 (m=30)` vs bound `3e-3` |
| 6 | Edgeworth accuracy | `sup_{|x|<=3} rel err * m^2 -> 6.0` (m=20..60) |
| 7 | determinant identity (Lemma 2.2) | 12 digits at m=8 |
| 8 | tilted moment formulas | 8+ decimals |
| 9 | `(r(k)-1) sigma(u_k)^2 ≈ 1 - 1.08/m` across bulk | 0.9615–0.9671 (m=30), 0.9710–0.9752 (m=40) |
| 10 | variance drop `(3/100)w^2` | matches to 3% at `w<=1` (m=40) |
| 11 | `Q(x)>0` / `G` decreasing / `Var_j(u)` decreasing | zero violations |
| 12 | pentagonal identity | exact, m=20,35,50, all `k<=m` |
| 13 | edge bound | `(r(k)-1)k(m+k)/(m-1) >= 1.0013`, all `k<=m`, m=30,40 |
| 14 | argmin `= floor(N/2)`, min=central | exact for `4(5) <= m <= 120` |
| 15 | (c) corrected: varfit `>= 187/216`, equality at m=6 | exact for `5 <= m <= 120`; `7/8` FAILS at m=6 |

*End of draft C.*
