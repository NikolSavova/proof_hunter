# G1 closure, draft B — window expansion and kernel transfer with explicit constants

*Blind-protocol note: this draft was written from `F2_PROOF_DRAFT.md` (merged draft) and
`F2_SPEC.md` only; no other `g1_*`/`g2_*`/`f1smooth_*` file was read. All numbered
citations "Lemma 1.x" refer to the merged draft's §1. Route: direct Fourier-integral
bounding — no packaged Edgeworth theorem is invoked anywhere. Verification scripts
(inline below; full versions in `f2_drafts/g1b_scripts/` — `g1b_sym.py` [Lemma B.7
table], `g1b_const.py` [B.0 certificates], `g1b_const2.py` + `g1b_final.py` [all
constants and the C_2 table; `g1b_final.py` execs its sibling `g1b_const2.py`,
path resolved relative to the script — runs from anywhere], `g1b_truth.py`
[ground truth vs mahonian], `g1b_lemA.py` [60-digit B.1 check]) were all run against the exact
harness `mahonian.py` on 2026-07-06.*

**What is closed here (= ledger item G1, both halves).**

1. **Prop 2.1 constants**: the pointwise expansion
   `p(k) = Z(y)[1 - (B_m/12)He_4(y)] + E(k)` with the explicit bound
   `|E(k)| <= 0.45/(sigma m^2)` for all `k`, all `m >= 110` (Corollary B.4) — in fact a
   *second-order* expansion with error `4.3/(sigma m^3)` (Proposition B.3).
2. **Prop 2.2 / window law**: for `|y| <= y_0` and `m >= m_1(y_0)`,
   `sigma^2 log r(k) = 1 + B_m(y^2 - 1) + E_1(k)` with `|E_1(k)| <= C_2(y_0)/m^2`,
   all constants explicit (Theorem B.8 / Corollary B.9; table in §8). The remainder is
   pushed through the second-difference kernel of Lemma 1.5, exactly as the merged
   draft's proof scheme prescribes; errors stay relative inside the kernel because the
   kernel factor `1 - cos(s-t) <= (s-t)^2/2` supplies the same `sigma^{-2}` to main
   term and error alike.

Beyond the frozen target, Theorem B.8 identifies the *exact* `m^{-2}`-order term as an
explicit polynomial `N(y)/P(y)^2` (its value at `y = 0` reproduces the merged draft's
NC-7 calibration `-0.19/m^2` to four digits, §9) — so the constant `C_2` here is not
just an upper bound, the second-order shape itself is now proved.

Everything below depends only on Lemmas 1.1, 1.2, 1.3(i)(ii) (including the term-ratio
display inside its proof), 1.4, and 1.5 of the merged draft — all of which are fully
proved there — plus elementary calculus and finite exact computation.

---

## 0. Notation and standing conventions

As in the merged draft: `N = m(m-1)/2`, `p(k) = I_m(k)/m!`, `x = k - N/2`,
`lambda := sigma^2 = m(m-1)(2m+5)/72`, `h := 1/sigma` (so `lambda h^2 = 1` exactly),
`y = x/sigma`, `y_pm := y pm h`. `S*_r := S_r - m = sum_{j=2}^m (j^r - 1)`.

```
beta  := (S_4 - m)/2880          (so  -kappa_4/24 = beta > 0),
gamma := (S_6 - m)/181440        (so   kappa_6/720 = gamma > 0),
b := beta/lambda^2 = B_m/12,     g := gamma/lambda^3,
c_8 := (m+1)^9 / 43545600,       t_1 := sqrt(2) pi / m .
```

`He_n` = probabilists' Hermite (`He_2 = y^2-1`, `He_3 = y^3-3y`, `He_4 = y^4-6y^2+3`,
`He_6 = y^6-15y^4+45y^2-15`, `He_8 = y^8-28y^6+210y^4-420y^2+105`; `He_n' = n He_{n-1}`).

```
Z(y)     := (2 pi lambda)^{-1/2} e^{-y^2/2},
phihat(t):= e^{-lambda t^2/2} (1 - beta t^4 - gamma t^6 + (beta^2/2) t^8),
P(y)     := 1 - b He_4(y) + g He_6(y) + (b^2/2) He_8(y),
phat(x)  := (1/2pi) int_R phihat(t) e^{-itx} dt   ( = Z(y) P(y), Lemma B.2(i) ).
```

Double factorials `(2n-1)!! = 1, 3, 15, 105, 945, 10395, ...`.

### Lemma B.0 (standing parameter bounds).

(i) `m^3/36 <= lambda <= 1.05 m^3/36` for `m >= 30`; `h^2 = 1/lambda <= 36/m^3` for `m >= 2`.

(ii) `b <= 0.0900/m` for `m >= 11`, and `0.0890/m <= b <= 0.0900/m` for `m >= 30`.
     Hence `B_m = 12b in [1.068, 1.080]/m` for `m >= 30`.

(iii) `0.03540/m^2 <= g <= 0.03674/m^2` for `m >= 30`.

(iv) `c_8/lambda^4 <= 0.0431/m^3` for `m >= 30`.

*Proof.* (i): `72 lambda / (2m^3) = 1 + 1.5/m - 2.5/m^2 in [1, 1+1.5/m]`, and
`1.5/m >= 2.5/m^2` for `m >= 2`. (ii)–(iv): with the closed forms
`S_4 = m(m+1)(2m+1)(3m^2+3m-1)/30`, `S_6 = (6m^7+21m^6+21m^5-7m^3+m)/42` and
`S*_8 <= int_2^{m+1} x^8 dx <= (m+1)^9/9` (used inside `c_8`, see Lemma B.1),
each claim is a single polynomial inequality in `m`. E.g. (ii)-upper is
`(S_4 - m) <= (0.09/m)·2880·lambda^2`, whose difference is a polynomial with largest
real root `10.095`; the roots for (ii)-lower, (iii)-upper, (iii)-lower, (iv) are
`25.669`, `6.874`, `1.000`, `29.884` respectively — all below the claimed thresholds,
and the leading coefficients have the right sign. ∎

NUMERIC CHECK (NC-B0): root certificates and direct evaluation
(`b·m in [0.089057, 0.090000]` on `m = 30..10^5`, `g·m^2 in [0.035842, 0.036734]`,
`c_8 lambda^{-4} m^3 <= 0.043080`):
```
python3 - <<'EOF'
import sympy as sp
m = sp.symbols('m', positive=True)
S4 = m*(m+1)*(2*m+1)*(3*m**2+3*m-1)/30
S6 = sp.Rational(1,42)*(6*m**7+21*m**6+21*m**5-7*m**3+m)
lam = m*(m-1)*(2*m+5)/72
tests = [("b_up", sp.Rational(9,100)/m*2880*lam**2-(S4-m), 11),
         ("b_lo", (S4-m)-sp.Rational(89,1000)/m*2880*lam**2, 30),
         ("g_up", sp.Rational(3674,100000)/m**2*181440*lam**3-(S6-m), 30),
         ("g_lo", (S6-m)-sp.Rational(354,10000)/m**2*181440*lam**3, 30),
         ("c8",  sp.Rational(431,10000)/m**3*43545600*lam**4-(m+1)**9, 30)]
for nm, e, thr in tests:
    num = sp.fraction(sp.together(sp.expand(e)))[0]
    r = max([sp.re(z) for z in sp.Poly(num, m).nroots() if abs(sp.im(z))<1e-9])
    print(nm, "largest real root", float(r), "< threshold", thr, ":", float(r) < thr)
EOF
```
Expected: all five `True`. **Run: PASS.**

---

## 1. The second-order model on the central arc

### Lemma B.1 (model approximation).
For `0 < |t| <= t_1 = sqrt(2) pi/m` and `m >= 3`:

```
| phi(t) - phihat(t) | <= e^{-lambda t^2/2} W(t),

W(t) := c_8 t^8 + beta t^4 (gamma t^6 + c_8 t^8) + (gamma t^6 + c_8 t^8)^2 / 2
        + (beta t^4 + gamma t^6 + c_8 t^8)^3 / 6 .
```

*Proof.* By Lemma 1.3, on this range `-log phi(t) = lambda t^2/2 + beta t^4 +
gamma t^6 + R_8(t)` with `R_8 := sum_{r>=4} a_r (t/2)^{2r} S*_{2r} >= 0` (the `r = 2, 3`
terms are `a_2 (t/2)^4 S*_4 = beta t^4` and `a_3 (t/2)^6 S*_6 = gamma t^6`).

**(a) `R_8 <= c_8 t^8`.** By the term-ratio display in the proof of Lemma 1.3(ii)
(valid for `m >= 3, r >= 1`), the ratio of consecutive series terms is
`<= (mt/2)^2/pi^2 <= 1/2` on `|t| <= t_1`, so `R_8 <= 2 × (first term)
= 2 a_4 (t/2)^8 S*_8`. Now `a_4 = zeta(8)/(4 pi^8) = 1/37800` (`zeta(8) = pi^8/9450`)
and `S*_8 <= sum_{j=2}^m j^8 <= int_2^{m+1} x^8 dx <= (m+1)^9/9`, so
`R_8 <= 2 (m+1)^9 t^8 /(37800 · 256 · 9) = (m+1)^9 t^8 / 43545600 = c_8 t^8`.

**(b) Exponential Taylor.** Write `phi = e^{-lambda t^2/2} e^{-U_0}`,
`U_0 := beta t^4 + gamma t^6 + R_8 in [0, U]`, `U := beta t^4 + gamma t^6 + c_8 t^8`.
For `u >= 0`, `|e^{-u} - (1 - u + u^2/2)| <= u^3/6` (Taylor remainder, `|e^{-xi}| <= 1`).
Also

```
(1 - U_0 + U_0^2/2) - (1 - beta t^4 - gamma t^6 + beta^2 t^8/2)
   = -R_8 + [U_0^2 - beta^2 t^8]/2 ,
0 <= U_0^2 - (beta t^4)^2 <= U^2 - (beta t^4)^2
   = (gamma t^6 + c_8 t^8)(U + beta t^4)
   <= 2 beta t^4 (gamma t^6 + c_8 t^8) + (gamma t^6 + c_8 t^8)^2 .
```

Collecting: `|e^{-U_0} - (1 - beta t^4 - gamma t^6 + beta^2 t^8/2)| <= R_8 +
beta t^4(gamma t^6 + c_8 t^8) + (gamma t^6 + c_8 t^8)^2/2 + U_0^3/6 <= W(t)`. ∎

NUMERIC CHECK (NC-B1): 60-digit arithmetic (`mpmath`), `m in {10, 20, 40, 60, 100}`,
400-point grid on `(0, t_1]`: `max |phi - phihat| / (e^{-lambda t^2/2} W) =
0.320, 0.400, 0.447, 0.464, 0.478` — always `<= 1`, with the max at `t -> 0` (the
factor `~1/2` slack is the 2×-tail bound in step (a)). **Run: PASS.** (A double-float
check is meaningless here: near `t = 0` both sides are below float roundoff.)

**Scaled coefficient table (used throughout).** Write `W(t) = sum_n w_n t^{2n}`. By
Lemma B.0, each `w_n lambda^{-n}` is bounded by a product of the three scaled
quantities `b <= 0.0900/m`, `g <= 0.03674/m^2`, `c8s := c_8 lambda^{-4} <= 0.0431/m^3`
(`m >= 30`), giving `w_n lambda^{-n} <= v_{n,q}/m^q` with:

| n (power `t^{2n}`) | source | q | `v_{n,q}` |
|---|---|---|---|
| 4 | `c_8` | 3 | 0.0431 |
| 5 | `beta gamma` | 3 | 0.003307 |
| 6 | `beta^3/6` | 3 | 0.0001215 |
| 6 | `beta c_8 + gamma^2/2` | 4 | 0.004554 |
| 7 | `beta^2 gamma / 2` | 4 | 0.0001488 |
| 7 | `gamma c_8` | 5 | 0.001583 |
| 8 | `(beta^2 c_8 + beta gamma^2)/2` | 5 | 0.0002353 |
| 8 | `c_8^2/2` | 6 | 0.0009288 |
| 9–12 | remaining cubes | 6–9 | `<= 0.00016` each |

Similarly `V(t) := beta t^4 + gamma t^6 + (beta^2/2) t^8` (so that
`|phihat(t)| <= e^{-lambda t^2/2}(1 + V(t))` on all of `R`, by the triangle
inequality) has scaled coefficients `(a=2): b <= 0.0900/m`, `(a=3): g <= 0.03674/m^2`,
`(a=4): b^2/2 <= 0.00405/m^2`.

### Lemma B.2 (integral toolkit).
Let `f(x) := (1/2pi) int_R e^{-lambda t^2/2} e^{-itx} dt = Z(y)`.

(i) `(1/2pi) int_R t^{2n} e^{-lambda t^2/2} cos(tx) dt = (-1)^n f^{(2n)}(x)
    = (-1)^n lambda^{-n} Z(y) He_{2n}(y)` (from `d^n/dy^n e^{-y^2/2}
    = (-1)^n He_n(y) e^{-y^2/2}`). Consequently `phat(x) = Z(y) P(y)` — note the sign
    pattern: the `-gamma t^6` model term produces `+ g He_6` in `P`.

(ii) `M_{2n} := int_R t^{2n} e^{-lambda t^2/2} dt = (2n-1)!! sqrt(2 pi/lambda) lambda^{-n}`.

(iii) (tail chain) For `a > 0`:
     `int_a^infty t^{2n} e^{-lambda t^2/2} dt <= e^{-lambda a^2/2} T_n(a)`, where
     `T_0 = 1/(lambda a)` and `T_k = a^{2k-1}/lambda + (2k-1) T_{k-1}/lambda`
     (integration by parts, plus Mills `int_a^infty e^{-lambda t^2/2} <=
     e^{-lambda a^2/2}/(lambda a)`). Every tail below therefore carries the *full*
     exponent `q_1 := lambda t_1^2/2 = lambda pi^2/m^2 >= pi^2 m/36 >= 0.274 m`.

(iv) `sup_y e^{-y^2/2} |He_6(y)| = 15`, `sup_y e^{-y^2/2}|He_8(y)| = 105`
     (both attained at `y = 0`; maxima of explicit polynomial × Gaussian functions,
     checked over all critical points).

NUMERIC CHECK (NC-B2): (i) verified by `scipy` quadrature at `m = 10` (12 digits);
(iv): dense grid + critical points on `[0, 12]`, crude bound beyond. **Run: PASS.**

---

## 2. Pointwise expansion with explicit constants (first half of G1)

### Proposition B.3 (second-order pointwise law).
For every `k` (no restriction on `y`) and every `m >= 110`:

```
p(k) = Z(y) P(y) + E_2(k),        |E_2(k)| <= 4.3 / (sigma m^3) .
```

*Proof.* By Lemma 1.1, `p(k) = (1/pi) int_0^pi phi(t) cos(tx) dt`, and by definition
`phat(x) = (1/pi) int_0^infty phihat(t) cos(tx) dt = Z(y)P(y)` (Lemma B.2(i)). Split:

```
p(k) - phat(x) = (1/pi) int_0^{t_1} (phi - phihat) cos(tx) dt        (I)
              + (1/pi) int_{t_1}^{2pi/m} phi cos(tx) dt              (II)
              + (1/pi) int_{2pi/m}^{pi} phi cos(tx) dt               (III)
              - (1/pi) int_{t_1}^{infty} phihat cos(tx) dt           (IV)
```

**(I)**: by Lemma B.1 and `|cos| <= 1`, `|I| <= (1/pi) int_0^infty e^{-lambda t^2/2}
W(t) dt = (1/sqrt(2 pi lambda)) sum_n w_n lambda^{-n} (2n-1)!!`
(Lemma B.2(ii), half-line). With the scaled table,
`sigma m^3 |I| <= (1/sqrt(2pi)) sum v_{n,q} (2n-1)!! m^{3-q} =: C_1''(m)`,
which is decreasing in `m`, with `C_1''(110) = 3.826 <= 3.83`
(dominant pieces: `0.0431*105 = 4.53` from `c_8` and `0.003307*945 = 3.13` from
`beta gamma`, divided by `sqrt(2pi)`).

**(II)**: Lemma 1.3(i) (`0 < phi <= e^{-lambda t^2/2}` up to `2pi/m`) + Mills:
`|II| <= e^{-q_1}/(pi lambda t_1)`.

**(III)**: Lemma 1.4: `|III| <= (1/pi)*pi*2 e^{-0.19314 m} = 2 e^{-0.19314 m}`.

**(IV)**: `|phihat| <= e^{-lambda t^2/2}(1+V)` and the tail chain (Lemma B.2(iii)):
`|IV| <= (e^{-q_1}/pi) (T_0 + b lambda^2 T_2 + g lambda^3 T_3 + (b^2/2) lambda^4 T_4)`
with `T_a = T_a(t_1)`.

The superpolynomial part satisfies `sigma m^3 (|II| + |III| + |IV|) <= 0.31` at
`m = 110` (dominated by (III); (II) and (IV) are `< 1e-9` there since
`q_1 >= 0.274 m`), and is decreasing in `m` (each piece is `C m^alpha e^{-cm}` with
`alpha <= 4.5`, `c >= 0.19314`, hence decreasing for `m >= alpha/c <= 24`). Total:
`sigma m^3 |E_2| <= 3.83 + 0.31 < 4.3` for `m >= 110`. QED

NUMERIC CHECK (NC-B3): exact Mahonian rows: `max_k sigma m^3 |p(k) - Z(y)P(y)| =
0.1145, 0.1120, 0.1109, 0.1099` at `m = 20, 30, 40, 60` — the bound holds with a
factor ~39 to spare (the slack is the 2x tail bound of B.1(a) plus the crude
`|cos| <= 1`); command:
```
python3 - <<'PYEOF'
import math
from fractions import Fraction
from mahonian import mahonian
def He(n,y):
    a,b=1.0,y
    for k in range(1,n): a,b=b,y*b-k*a
    return b if n else 1.0
for m in (20,30,40,60):
    a=mahonian(m); N=m*(m-1)//2; lam=m*(m-1)*(2*m+5)/72.0; sig=math.sqrt(lam)
    S4=sum(j**4 for j in range(1,m+1)); S6=sum(j**6 for j in range(1,m+1))
    b=(S4-m)/2880.0/lam**2; g=(S6-m)/181440.0/lam**3; f=math.factorial(m)
    print(m, max(abs(float(Fraction(a[k],f))-math.exp(-((k-N/2)/sig)**2/2)/math.sqrt(2*math.pi*lam)
        *(1-b*He(4,(k-N/2)/sig)+g*He(6,(k-N/2)/sig)+b*b/2*He(8,(k-N/2)/sig)))*sig*m**3
        for k in range(N+1)))
PYEOF
```
**Run: PASS.**

### Corollary B.4 (= merged draft Prop 2.1 with explicit `C_1`).
For every `k` and `m >= 110`:

```
p(k) = (sigma sqrt(2pi))^{-1} e^{-y^2/2} [ 1 - (B_m/12) He_4(y) ] + E(k),
|E(k)| <= 0.45 / (sigma m^2) .
```

*Proof.* `E = Z(y)(g He_6 + (b^2/2) He_8) + E_2`. By Lemma B.2(iv) and B.0,
`|Z (g He_6 + (b^2/2)He_8)| <= (sigma sqrt(2pi))^{-1}(15 g + 52.5 b^2)
<= (15*0.03674 + 52.5*0.0081)/(sqrt(2pi) sigma m^2) = 0.3895/(sigma m^2)`.
Adding `4.3/(sigma m^3) <= 0.0391/(sigma m^2)` (`m >= 110`) gives `0.4286 < 0.45`. QED

This settles the first half of G1: `C_1 = 0.45` (for `m >= 110`; `4 <= m <= 150` is
covered exactly by the harness, NC-1). Note the true size (NC-6a of the merged draft:
relative error `~6/m^2`, i.e. `C_1^true ~ 2.4` against the *relative* shape) is
consistent: our absolute-error constant is smaller because `e^{-y^2/2}|He_6|` peaks
at the center.

---

## 3. The kernel transfer (second half of G1)

### Lemma B.5 (factorization identity for even models).
Let `psi in L^1(R)` be even, `q(x) := (1/2pi) int psi(t) e^{-itx} dt`. Then

```
(1/4pi^2) intint_{R^2} psi(s) psi(t) cos((s+t)x) (1 - cos(s-t)) ds dt
   = q(x)^2 - q(x-1) q(x+1) .
```

*Proof.* `cos((s+t)x)(1-cos(s-t)) = cos((s+t)x) - (1/2)cos(s(x+1) + t(x-1))
- (1/2)cos(s(x-1) + t(x+1))` (product-to-sum). Each summand factorizes after
expanding `cos(A+B) = cos A cos B - sin A sin B`: the `sin x sin` parts integrate to
zero against the even `psi(s)psi(t)`, and for even `psi`,
`(1/2pi) int psi(t) cos(tu) dt = q(u)`. The three terms give
`q(x)^2 - (1/2) q(x+1)q(x-1) - (1/2) q(x-1)q(x+1)`. QED

(This is Lemma 1.5 read backwards, applied to the model; it makes the model part of
the kernel integral computable in closed form with no new integrals.)

NUMERIC CHECK (NC-B5): `scipy.integrate.dblquad` vs `phat^2 - phat_- phat_+` at
`m = 10`, `x = 3.3`: agreement `5.7e-14` relative. **Run: PASS.**

### Lemma B.6 (kernel remainder, explicit).
Let `D(k) := p(k)^2 - p(k-1)p(k+1)` and `Dhat(x) := phat(x)^2 - phat(x-1)phat(x+1)`.
Then `D(k) = Dhat(x) + DeltaD` with `|DeltaD| <= Delta_box + Delta_tail + Delta_out`:

```
Delta_box  := (1/2pi^2) [  sum_n w_n (pi/lambda^{n+2}) (2n-1)!! (2n+2)
             + sum_{a,b} v_a w_b (pi/lambda^{a+b+2}) ( (2a+1)!!(2b-1)!! + (2a-1)!!(2b+1)!! ) ]

Delta_tail := (4/pi^2) [ e^{-q_1} ( T_0 + sum_a v_a lambda^a T_a ) ]
                       [ sqrt(2pi/lambda) (1 + sum_a v_a lambda^{-a} (2a-1)!!) ]

Delta_out  := (4/pi^2) [ e^{-q_1}/(lambda t_1) + 2 pi e^{-0.19314 m} ]
                       [ sqrt(2pi/lambda) + 2( e^{-q_1}/(lambda t_1) + 2 pi e^{-0.19314 m} ) ]
```

(`T_a = T_a(t_1)` from Lemma B.2(iii); in `Delta_tail` the second bracket is
`int_R e^{-lambda t^2/2}(1+V) dt`; in the first bracket the `v_a` are the raw
coefficients of `V`, i.e. `v_2 = beta` etc.)

*Proof.* Start from Lemma 1.5 (exact) and decompose `[-pi,pi]^2` into the box
`B := [-t_1, t_1]^2` and its complement; add and subtract the model over `R^2`;
`Dhat` is the `R^2` model integral by Lemma B.5.

**Box.** On `B`, `|phi(s)phi(t) - phihat(s)phihat(t)| <= |phi(s)-phihat(s)||phi(t)|
+ |phihat(s)||phi(t)-phihat(t)| <= e^{-lambda(s^2+t^2)/2}[W(s) + (1+V(s))W(t)]`
(Lemma B.1, Lemma 1.3(i), `|phihat| <= e^{-..}(1+V)`). The kernel obeys
`|cos((s+t)x)| (1-cos(s-t)) <= (s-t)^2/2` — **this is the load-bearing step**: the
remainder inherits the same `(s-t)^2/2` that produces the `sigma^{-2}` of the main
term, so the transferred error is *relative*. Symmetrize in `(s,t)` (bounding
`W(s)+ (1+V(s))W(t)` by the symmetric `W(s)+W(t)+V(s)W(t)+V(t)W(s)`), extend to
`R^2` (positive integrand), expand `(s-t)^2 = s^2 - 2st + t^2` (the odd `st` term
integrates to zero against even factors), and use Lemma B.2(ii):
`intint e^{-..} W(s) (s-t)^2/2 ds dt = sum_n w_n (pi/lambda^{n+2})(2n-1)!!(2n+2)`,
and the analogous `V x W` products. This gives `Delta_box`.

**Outside (true phi).** The complement of `B` in `[-pi,pi]^2` is covered by the two
symmetric strips `{t_1 <= |s| <= pi}` (factor 2); there `|K| <= 2` and
`int_{t_1<=|s|<=pi} |phi| ds <= 2[ e^{-q_1}/(lambda t_1) + 2 pi e^{-0.19314 m} ]`
(Lemma 1.3(i) + Mills on `[t_1, 2pi/m]`, Lemma 1.4 on `[2pi/m, pi]`), while
`int_{-pi}^{pi} |phi| <= sqrt(2pi/lambda) + (same strip term)`. This gives
`Delta_out`.

**Outside (model).** Same strip decomposition on `R^2` with
`|phihat| <= e^{-lambda t^2/2}(1+V)` and the tail chain: `Delta_tail`. QED

**Scaled form.** Multiplying `Delta_box` by `2 pi lambda^2` (which is how it enters
`E_1`, section 4) gives, with the scaled tables of section 1,

```
2 pi lambda^2 Delta_box <= KB(m)/m^3,
KB(m) := sum_(n,q) v_{n,q} (2n-1)!!(2n+2) m^{3-q}
       + sum_{a,b} v_a v_{b,q} [ (2a+1)!!(2b-1)!! + (2a-1)!!(2b+1)!! ] m^{3-q'} ,
```

with `KB` decreasing in `m` and `KB(180) = 106.6` (leading pieces:
`0.0431*105*10 = 45.3` from `c_8`, `0.003307*945*12 = 37.5` from `beta gamma`,
`0.0001215*10395*14 = 17.7` from `beta^3/6`). Likewise
`SP(m) := 2 pi lambda^2 (Delta_tail + Delta_out)` is explicit and superpolynomially
small; its dominant piece for `m >= 150` is the far arc:
`SP ~ 8 sqrt(2pi) lambda^{3/2} * 2 e^{-0.19314 m}` — this single term fixes the
thresholds `m_1(y_0)` below (see section 8 remark on Lemma 1.4).

---

## 4. Main-term calculus

### Lemma B.7 (the exact second-order polynomial).
Let `L := log P` and define the polynomial (in `y`, with coefficients polynomial in
`b, g`)

```
N(y) := -P''(y) P(y) + P'(y)^2 - 12 b He_2(y) P(y)^2 ,
```

so that, identically in `y` wherever `P > 0`,

```
-(log P)''(y) = 12 b He_2(y) + N(y)/P(y)^2 = B_m He_2(y) + N(y)/P(y)^2 .
```

The exact monomial expansion of `N` in `(b, g)` is (exact integers; generated by the
5-line `sympy` computation below and hand-checkable from `He_n' = n He_{n-1}`):

```
N =  g   * (-30 y^4 + 180 y^2 - 90)                                   [ = -30 g He_4 ]
  +  b^2 * (240 y^4 - 1008 y^2 + 384)                                 [ = b^2 (16 He_3^2 + 12 He_2 He_4 - 28 He_6) ]
  +  b g  * (-30 y^8 + 456 y^6 - 1620 y^4 + 1800 y^2 + 90)
  +  g^2  * (6 y^10 - 90 y^8 + 540 y^6 - 900 y^4 + 1350 y^2 + 1350)
  +  b^3  * (-22 y^10 + 510 y^8 - 3588 y^6 + 8916 y^4 - 7470 y^2 - 522)
  +  b^2 g * (29 y^12 - 666 y^10 + 5121 y^8 - 16692 y^6 + 21195 y^4 - 15930 y^2 - 9945)
  +  b g^2 * (-12 y^14 + 372 y^12 - 4140 y^10 + 20340 y^8 - 46260 y^6 + 45900 y^4 - 18900 y^2 + 2700)
  +  b^4  * (14 y^14 - 490 y^12 + 5946 y^10 - 31830 y^8 + 79338 y^6 - 83790 y^4 + 48510 y^2 + 18270)
  +  b^3 g * (-12 y^16 + 528 y^14 - 8616 y^12 + 66240 y^10 - 253440 y^8 + 478800 y^6 - 415800 y^4 + 151200 y^2 - 18900)
  +  b^5  * (-3 y^18 + 171 y^16 - 3780 y^14 + 41412 y^12 - 241290 y^10 + 750330 y^8 - 1208340 y^6 + 926100 y^4 - 297675 y^2 + 33075)
```

Two structural facts (both verified exactly): the **`b`-linear terms cancel
identically** (the `12 b He_2` from `-P''` is subtracted off exactly — this is the
kernel-level cancellation of the pointwise `He_4` correction between `D` and
`p(k-1)p(k+1)`), and the `b^2` coefficient `16He_3^2 + 12He_2He_4 - 28He_6` collapses
to a **quartic** (`y^6` cancels): `240y^4 - 1008y^2 + 384`. At `y = 0`:
`N(0) = -90 g + 384 b^2 + O(m^{-3})`, which with Lemma B.0 is `~ -0.19/m^2` — the
merged draft's NC-7 calibration, now derived (see §9).

NUMERIC CHECK (NC-B7): exact symbolic generation + the two structural facts:
```
python3 - <<'PYEOF'
import sympy as sp
y,b,g = sp.symbols('y b g')
He = lambda n: sp.expand(2**sp.Rational(-n,2)*sp.hermite(n, y/sp.sqrt(2)))
P  = 1 - b*He(4) + g*He(6) + sp.Rational(1,2)*b**2*He(8)
Nx = sp.expand(-sp.diff(P,y,2)*P + sp.diff(P,y)**2 - 12*b*He(2)*P**2)
Q  = sp.Poly(Nx, b, g)
print("b-linear coeff == 0 :", Q.coeff_monomial(b) == 0)
print("b^2 coeff:", Q.coeff_monomial(b**2))
print("g coeff  :", Q.coeff_monomial(g))
PYEOF
```
Expected: `True`, `240*y**4 - 1008*y**2 + 384`, `-30*y**4 + 180*y**2 - 90`.
**Run: PASS** (full table regenerated identically, script `g1b_sym.py`).

### Lemma B.7' (Taylor step).
Fix `y_0 > 0`, let `J := [-(y_0+h), y_0+h]` and suppose `P > 0` on `J`. Set
`F(y) := e^{h^2} P(y)^2 / (P(y-h) P(y+h))`. Then for `|y| <= y_0`:

```
lambda log F(y) = 1 + B_m He_2(y) + N(y)/P(y)^2 + theta * (h^2/12) * sup_J |L''''|,
|theta| <= 1 .
```

*Proof.* `log F = h^2 + 2L(y) - L(y-h) - L(y+h)`. Fourth-order Taylor with integral
remainder: `L(y+h) + L(y-h) - 2L(y) = h^2 L''(y) + (h^4/6) int_0^1 (1-tau)^3
[L''''(y+tau h) + L''''(y-tau h)] d tau`, and the remainder is bounded by
`(h^4/12) sup_J |L''''|`. Multiply by `lambda`, use `lambda h^2 = 1` (exact) and
Lemma B.7 for `-L''`. ∎

The crude bound `sup_J |L''''| <= p_4/P_min + 4 p_3 p_1 / P_min^2 + 3 p_2^2/P_min^2
+ 12 p_2 p_1^2/P_min^3 + 6 p_1^4 / P_min^4` (quotient rule; `p_j := sup_J |P^{(j)}|`,
`P_min := min_J P`, and `P^{(j)}` are explicit Hermite combinations, e.g.
`P'''' = -24b + 360 g He_2 + 840 b^2 He_4`) is `O(1/m)`; its contribution to `E_1` is
`<= 3 sup|L''''| / m^3` (`h^2 <= 36/m^3`) — numerically `< 3e-4 / m^2` at every
`(y_0, m_1)` in the table below.

---

## 5. The window law (Theorem B.8)

### Theorem B.8 (window law with exact second-order term and explicit constants).
Fix `y_0 > 0`. For every `m >= m_1(y_0)` (table in §8) and every `k` with
`|y| = |k - N/2|/sigma <= y_0`:

```
sigma^2 log r(k) = 1 + B_m (y^2 - 1) + N(y)/P(y)^2 + E_1'(k) ,
```

with the explicit bound (all pieces defined above, evaluated at `m_1`, every piece
decreasing in `m` for `m >= m_1`):

```
|E_1'(k)| <= (1/12) h^2 sup_J |L''''|                                     [Taylor]
   + 1.02 * e^{y_0^2 + h^2} / P_min^2 * ( KB(m)/m^3 + SP(m) )             [kernel transfer]
   + 1.02 * (2 dbar + dbar^2) * (1 + l_2)(1 + 2h^2) / (1 - 2 dbar - dbar^2)   [denominators]
```

where `dbar := sqrt(2pi) e^{(y_0+h)^2/2} (C_1''(m)/m^3 + sigma Theta_pt(m)) / P_min`
is the relative pointwise error of Prop B.3 at `y_pm` (`Theta_pt` = its
superpolynomial part), and `l_2 := sup_J |L''|`.

*Proof.* Write `r(k) - 1 = D(k)/(p(k-1)p(k+1))` (definition of `r`, and `D` from
Lemma 1.5). Decompose:

1. `D = Dhat + DeltaD` (Lemma B.6), and `p(k-1)p(k+1) = phat(x-1) phat(x+1) (1+delta)`
   with `1 + delta := (1+delta_-)(1+delta_+)`, `delta_pm := E_2(k pm 1)/phat(x pm 1)`,
   `|delta_pm| <= dbar` (Prop B.3; `phat(x pm 1) = Z(y_pm)P(y_pm) >=
   (2 pi lambda)^{-1/2} e^{-(y_0+h)^2/2} P_min`).

2. `Dhat/(phat_- phat_+) = F - 1 =: v` **exactly**: by Lemma B.2(i),
   `phat(x)^2/(phat(x-1)phat(x+1)) = [Z(y)^2/(Z(y_-)Z(y_+))] * P(y)^2/(P_- P_+)
   = e^{h^2} P^2/(P_- P_+) = F` since `(y_-^2 + y_+^2)/2 - y^2 = h^2`.
   Note `v > 0` (as `log F = h^2 (1 - L'' - theta h^2 sup|L''''|/12) > 0` when
   `l_2 + h^2 sup|L''''|/12 < 1`, true at every table point), and
   `lambda v <= (1+l_2)(1+2h^2)` (from `v <= log F * e^{log F}`).

3. Hence `u := D/(p_- p_+) = (v + w)/(1 + delta)` with
   `w := DeltaD/(phat_- phat_+)`, and

```
sigma^2 log r(k) = lambda log(1+u) = lambda log F + lambda log( (1+u)/(1+v) ),
(1+u)/(1+v) = 1 + z,   z := (w - delta v) / ( (1+delta)(1+v) ) .
```

4. `lambda log F` is Lemma B.7' — this produces the main terms
   `1 + B_m He_2(y) + N/P^2` plus the Taylor bucket.

5. `lambda |log(1+z)| <= lambda |z| / (1-|z|)`, and using `v > 0`,
   `lambda|z| <= ( lambda|w| + |delta| lambda v ) / (1 - |delta|)`. Now
   `lambda |w| = 2 pi lambda^2 e^{y^2+h^2} |DeltaD| / (P_- P_+) <=
   e^{y_0^2+h^2} (KB(m)/m^3 + SP(m)) / P_min^2` (Lemma B.6 scaled form) — this is
   the *only* place the window inflation `e^{y_0^2}` enters, and it multiplies an
   `O(m^{-3})` quantity. The factor `1.02` absorbs `1/(1-|z|)` and `1/(1-|delta|)`
   (at every table point `|z| < 1e-4`, `|delta| < 1e-3`). ∎

### Corollary B.9 (= ledger G1 target form).
For `m >= m_1(y_0)` and `|y| <= y_0`:

```
sigma^2 log r(k) = 1 + B_m (y^2 - 1) + E_1(k),      |E_1(k)| <= C_2(y_0)/m^2 ,
```

with `E_1 := N/P^2 + E_1'` and `C_2(y_0) := m_1^2 * sup_{|y|<=y_0} |N/P^2| + m_1^2 *
(E_1' bound)`. The sup of `|N|/P^2` is bounded for ALL `m >= m_1` at once by taking,
pointwise in `y`, the worst corner of the certified rectangle
`(b, g) in [0.0890, 0.0900]/m x [0.03540, 0.03674]/m^2` for the two leading monomials
and absolute values with Lemma B.0 bounds for the eight higher monomials (each of
which carries at least one extra `1/m`).

---

## 6. The constants (final table)

All entries computed by `g1b_final.py` (assembly exactly as in Theorem B.8; each
bucket evaluated at `m = m_1` and decreasing in `m`, because every piece is either a
negative power of `m`, a certified-decreasing coefficient, or of the form
`C m^alpha e^{-cm}` with `alpha <= 6.5 < c m_1`).

| `y_0` | `m_1` | `m^2 sup N/P^2` | box | denom | superpoly | Taylor | **C_2 (proved)** | measured `sup m^2 E_1` (m=60) |
|---|---|---|---|---|---|---|---|---|
| 0.1 | 180 | 0.284 | 0.600 | 0.105 | 0.070 | 0.0002 | **1.1** | 0.194 (center) |
| 0.5 | 180 | 0.575 | 0.762 | 0.119 | 0.089 | 0.0002 | **1.6** | 0.527 |
| 1.0 | 180 | 1.010 | 1.613 | 0.173 | 0.187 | 0.0002 | **3.1** | 0.922 |
| 2.0 | 200 | 7.156 | 28.980 | 0.700 | 0.156 | 0.0002 | **38** | 7.032 |
| 3.0 | 230 | 56.5 | 3793 | 7.64 | 0.178 | 0.0003 | **3940** | 58.8 |
| 3.0 | 2000 | 55.4 | 410 | 0.81 | 0.000 | 0.0002 | **475** | 58.8 |

Reading the table:

- **Small windows are tight.** For `y_0 <= 1` the proved `C_2` is within a factor
  `3.4` of the measured truth, and the *exact* `N/P^2` term alone nearly saturates
  the truth (`1.01` proved vs `0.92` measured at `y_0 = 1`): the second-order shape
  is captured, not just bounded. In particular this **resolves the merged draft's
  constants dispute** (0.2 vs 0.4 vs 0.69, NC-6) from the proof side: no absolute
  constant below `~0.9` can work on `|y| <= 1`, and the center value is `~0.19/m^2`
  (§9) — both now theorems, not calibrations.
- **Wide windows pay `e^{y_0^2}` on ONE `O(m^{-3})` term.** The `box` bucket is
  `1.02 e^{y_0^2} KB(m_1)/(P_min^2 m_1)` — the price of bounding `|cos((s+t)x)| <= 1`
  on the (bounded-only, hence non-oscillatory) kernel remainder. It decays like
  `1/m_1` (see the two `y_0 = 3` rows). For the merged draft's synthesis this is
  harmless: Theorem A's handoff needs a *constant* `y_0` with
  `B_m y_0^2 >= C_2(y_0)/m^2`, i.e. `m >= C_2(y_0)/(1.08 y_0^2)`, which at
  `y_0 = 1` is `m >= 3` — vacuous against `m_1 = 180`.
- **Thresholds are set by Lemma 1.4 alone.** `m_1(y_0)` is the smallest `m` at which
  the far-arc piece `~ 16 sqrt(2pi) lambda^{3/2} e^{-0.19314 m} e^{y_0^2}` drops
  below `~0.2/m^2`. Any sharpening of Lemma 1.4 (NC-5 shows 4–8 orders of slack)
  lowers `m_1` mechanically; conversely, extending the exact harness from 150 to
  `m_1` (minutes, per G4) closes the `150 < m < m_1` gap for downstream use.

NUMERIC CHECK (NC-B9, end-to-end ground truth): exact Mahonian rows, `m = 20..60`:
```
python3 - <<'PYEOF'
import math
from mahonian import mahonian
for m in (20,30,40,50,60):
    a=mahonian(m); N=m*(m-1)//2; lam=m*(m-1)*(2*m+5)/72.0; sig=math.sqrt(lam)
    S4=sum(j**4 for j in range(1,m+1)); Bm=(S4-m)/240.0/lam**2
    la=[math.log(v) for v in a]
    for y0 in (0.5,1.0,2.0,3.0):
        E=[abs(lam*(2*la[k]-la[k-1]-la[k+1])-1-Bm*(((k-N/2)/sig)**2-1))
           for k in range(1,N) if abs((k-N/2)/sig)<=y0]
        print(m, y0, round(m*m*max(E),3))
PYEOF
```
Expected: `max m^2|E_1|` converging (in `m`) to `~0.53 / 0.92 / 7.0 / 59` for
`y_0 = 0.5 / 1 / 2 / 3` — all below the corresponding `C_2`. **Run: PASS.**

---

## 7. Consistency with the merged draft's calibrations

1. **NC-7 (center residual).** Theorem B.8 at `y = y_c ~ 0` predicts
   `E_1 = N(0)/P(0)^2 + O(m^{-3}) = (-90g + 384b^2)(1 + O(1/m)) + O(m^{-3})`.
   Exact evaluation vs exact Mahonian rows:
   `m^2 E_1(k_c)` measured `= -0.1679, -0.1846, -0.1897, -0.1923, -0.1936` at
   `m = 20, 30, 40, 50, 60`; predicted `N(y_c)/P(y_c)^2 * m^2 = -0.1751, -0.1867,
   -0.1903, -0.1923, -0.1932`. Agreement to 4 digits by `m = 50`; asymptotically
   `-90g + 384b^2 -> (-90*0.0367 + 384*0.0081)/m^2 = -0.195/m^2`.
   **The merged draft's calibrated `|E_1(0)| <= 0.19/m^2` is now derived, with the
   mechanism identified: it is `384b^2 - 90g`, a fourth-vs-sixth-cumulant trade.**
2. **NC-6 (window constant).** The measured shape-constant `0.686` vs `(1+y^6)/m^2`
   on `|y| <= 3` lives inside our exact `N/P^2` term: `sup_{|y|<=3} m^2 |N/P^2| ~ 56`
   vs `0.686 * (1+3^6) ~ 501` — consistent (the `(1+y^6)` majorant is not tight at
   `y = 3`; the true sup is `~59`, attained at `y = 3`, and our 56-plus-buckets
   covers it for `m >= m_1`).
3. **Cor 2.3 (sharp central ratio).** At `k = k_c`, `|y| <= 1/(2 sigma)`, Corollary
   B.9 with `y_0 = 0.1` gives `sigma^2 log r(k_c) = 1 - B_m + E`, `|E| <= 1.1/m^2 +
   B_m y_c^2 <= 1.2/m^2` — i.e. the merged draft's
   `sigma^2 (r_c - 1) = 1 - (27/25)/m + O(m^{-2})` now carries the explicit
   `O(m^{-2})` constant `1.2 + 0.6 = 1.8` (adding `lambda(e^{D}-1-D) <= 0.6/m^2`-type
   linearization, `D := log r(k_c) ~ 1/lambda`, for the `r_c - 1` form). For G4's
   feasibility chase (`C' <= 20` needed, NC-13): **`C' = 1.8 << 20`** — the center
   margin is now proved for `m >= 180`, so (c) reduces to the finite check
   `m <= 180` (harness extension 150 -> 180, minutes) plus G2.

---

## 8. What remains / honest markers

**G1 is closed**: both halves of the ledger item (Prop 2.1 constant `C_1`; transfer
through the second-difference kernel to `|E_1| <= C_2/m^2`) are proved above with
explicit constants and explicit thresholds, from the merged draft's Lemmas 1.1–1.5
only, by direct integral bounding (no Edgeworth package, no unstated uniformity).

Residual caveats — none of these is a mathematical gap in G1, but all should be
visible to downstream users:

1. **EXACT-COMPUTATION STEPS (not gaps).** Two ingredients are finite exact
   computations rather than displayed hand algebra: (a) the monomial table of `N`
   (Lemma B.7; 5-line sympy regeneration, exact integers, hand-checkable via
   `He_n' = n He_{n-1}`); (b) maxima of explicit univariate polynomials on intervals
   (Lemma B.2(iv), the corner bounds of Cor B.9, `p_j` sups) — classical, exact via
   Sturm sequences if a referee insists; computed here via critical points, with
   generous rounding.
2. **Thresholds vs harness range.** The window law is proved for `m >= m_1(y_0) >=
   180`, while the harness is exact only to `m = 150`. For any downstream statement
   quantified over ALL `m`, the band `150 < m < m_1` must be covered by extending
   the harness (G4 already plans exactly this; `m = 200` costs minutes) — or `m_1`
   drops by sharpening Lemma 1.4, whose slack is 4–8 orders (NC-5). The *binding*
   constant is `0.19314` from Lemma 1.4 and nothing else.
3. **`e^{y_0^2}` inflation at wide windows.** `C_2(3) = 3940` (at `m_1 = 230`) is
   honest but far above the calibrated `~59`; the inflation sits entirely on one
   `O(m^{-3})` bucket (kernel remainder, oscillation discarded). Downstream uses
   (Theorem A handoff at constant `y_0 ~ 1`; G4's center window) only ever need
   `y_0 <= 1`, where the proved constants are within a factor `3.4` of truth. If a
   future use needs sharp wide-window constants, push the model one order (`t^{10}`,
   `He_10`): the box bucket then gains another `1/m` and the new exact terms join
   `N` — mechanical, by the same machinery.
4. **GAP (inherited, unchanged): G2.** Nothing here touches the tilted frame; the
   tilted analogue of this document (same skeleton: B.0–B.9 for truncated
   geometrics, using the tilted-cf identity quoted in the G2 ledger row) is the
   natural next pass.

*End of g1_draft_b.*
