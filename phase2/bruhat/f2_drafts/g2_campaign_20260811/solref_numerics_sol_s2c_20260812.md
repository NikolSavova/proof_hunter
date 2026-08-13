# numerics referee (gpt-5.6-sol, effort=max) — sol_s2c_20260812.md — 2026-08-12 19:14

> Cross-model referee report (Sol on the reviewed draft). Numeric checks are
> DERIVED, not executed — script them before trusting.

# Numerics referee report

I cannot pass the draft numerically. The hand-auditable arithmetic is largely consistent, and I found no explicit numerical counterexample. However, the load-bearing \(W_1\)–\(W_3\) certificate and the \(F_1<25\) grid certificate are asserted without executable artifacts, exact output fractions, or enough implementation detail to reproduce the quoted maxima. Under the requested convention, those outputs are **FABRICATED-until-sourced**.

## 1. Algebraic normalization checks

The following identities check out.

Let
\[
q=e^{-z}.
\]
Then
\[
A_1(z)=\frac{q}{(1-q)^2},
\qquad
A_4(z)=\frac{q(1+11q+11q^2+q^3)}{(1-q)^5}.
\]

The variance can independently be checked from the truncated-geometric factors
\[
Z_j=\sum_{r=0}^{j-1}q^r=\frac{1-q^j}{1-q}.
\]
If
\[
\mu_j=\frac{\sum_{r=0}^{j-1}r q^r}{Z_j},
\qquad
v_j=\frac{\sum_{r=0}^{j-1}r^2q^r}{Z_j}-\mu_j^2,
\]
then
\[
\sum_{j=1}^m v_j
=
mA_1(\lambda)-\sum_{j=1}^m j^2A_1(j\lambda)=s_2.
\]

A stable direct check of the normalized remainder is obtained without dividing by \(t^5\). For \(h=\lambda\), \(x=t/h\), define
\[
D_m(h)=mG(h)-\sum_{j=1}^mG(jh),
\]
\[
N_m(h,a)=\sum_{j=1}^mF_a(jh)-mF_a(h).
\]
Then
\[
\boxed{
Q(m,h,x):=
\frac{h^3|R_5(xh)|}{s_2(xh)^5}
=
\frac1{24D_m(h)}
\left|
\int_0^1(1-u)^4N_m(h,1-iux)\,du
\right|.
}
\]
This is the preferred formula for all direct truth probes. At \(x=0\), use the continuous limit
\[
Q(m,h,0)=\frac{|N_m(h,1)|}{120D_m(h)}.
\]

The scaling, signs, and factor \(1/24\) in SOL.1–SOL.2 are correct.

---

## 2. Exact arithmetic I could verify

### 2.1 The \(G(0.89)\) certificate

A human can check this entirely with rational arithmetic:

```python
from fractions import Fraction as F

x = F(89,200)
U = x + x**3/F(6) + x**5/F(120) \
      + (x**7/F(5040))/(1-x*x/F(72))

assert U < F(5748,12500)
assert F(11125,11496)**2 > F(93649,100000)
assert F(93649,100000) > F(117,125)
```

The displayed square comparison is correct:
\[
11125^2=123765625,\qquad 11496^2=132158016,
\]
and
\[
123765625\cdot100000
-132158016\cdot93649
=96459616>0.
\]
Also,
\[
93649\cdot125-117\cdot100000=6125>0.
\]

Numerically,
\[
G(0.89)=\left(\frac{0.445}{\sinh 0.445}\right)^2
\approx0.936525975,
\]
consistent with the draft.

**Result:** PASS.

### 2.2 The local Mittag–Leffler constant

The numerical coefficient used in SOL.3.15 is exactly
\[
K=
240\frac98\frac{509}{500}\left(\frac5{31}\right)^6
=
\frac{8589375}{1775007362}
\approx0.0048391.
\]
The required comparison is
\[
200\cdot8589375=1717875000
<
1775007362,
\]
so
\[
K<\frac1{200}.
\]

The auxiliary corner bound is also exact:
\[
\frac{20\sqrt5}{561}<\frac2{25},
\]
because after squaring,
\[
500^2\cdot5=1250000<1122^2=1258884.
\]

**Result:** PASS.

### 2.3 \(F_a''\) and \(G''\) integral arithmetic

Using the rational bounds from SOL.3.18, the three contributions on \([1,\infty)\) are

\[
20\left(\frac{13}{2}+3\frac{53}{25}
+6\frac{24}{25}+6\frac35\right)
=444.4,
\]

\[
\frac{45}{4}\left(
\frac{53}{2}+4\frac{13}{2}
+12\frac{53}{25}+24\frac{24}{25}+24\frac35
\right)
=1298.025,
\]

\[
\frac54\left(
135+5\frac{53}{2}+20\frac{13}{2}
+60\frac{53}{25}+120\frac{24}{25}+120\frac35
\right)
=889.875.
\]

Thus
\[
444.4+1298.025+889.875=2632.3.
\]
Adding the stated \(<0.61\) contribution gives
\[
\int_0^{40}|F_a''(v)|\,dv<2632.91<2633<3000.
\]

Similarly,
\[
2\frac35+4\left(\frac35+\frac{24}{25}\right)
+\left(\frac{53}{25}+2\frac{24}{25}+2\frac35\right)
=12.68.
\]
Adding the \(<0.68\) contribution gives
\[
\int_0^{40}|G''(v)|\,dv<13.36<14.
\]

**Result:** PASS.

### 2.4 Cauchy bound and tail

Using only \(\pi^2<9.87\),
\[
M_C
<
197.4\cdot4^6+192\cdot4^5
=1005158.4<1010000.
\]

The final Cauchy-tail comparison can be checked as the single integer inequality
\[
3030000\cdot347^6\cdot32\cdot10^6
<
11\cdot20000^6\cdot243.
\]
Numerically the displayed majorant is approximately
\[
1.088\times10^{-5}<1.1\times10^{-5}.
\]

**Result:** PASS.

### 2.5 Tail factor in SOL.6.9

The constants combine correctly:
\[
\frac{260}{191}\cdot\frac1{1-3/50}
=
\frac{260}{191}\cdot\frac{50}{47}
=
\frac{13000}{8977}.
\]

The inequalities
\[
e^{-4}<\frac1{50},
\qquad
\left(\frac{66}{65}\right)^{67}<3
\]
are also true. The first follows already from the Taylor polynomial for \(e^4\) through degree seven.

**Result:** PASS.

### 2.6 \(W_7\)

The lower variance fraction is correct:
\[
\frac{93649}{100000}-\frac{3.29}{40}
=
\frac{93649-8225}{100000}
=
\frac{5339}{6250}.
\]

Consequently,
\[
\frac{50}{120(5339/6250)}
=
\frac{15625}{32034}
\approx0.487763002<0.4878<0.5.
\]

**Result:** PASS.

### 2.7 Trapezoid correction

The \(1/8\) constant is correct:
\[
\left|T_h-\int f\right|
\le
\frac{h^2}{8}\int|f''|.
\]
The prior \(1/12\) claim would not be valid for a universal \(L^1\)-bound on \(f''\).

**Result:** PASS.

---

## 3. Scalar values independently corroborated

From
\[
H(w)=w-\frac{\pi^2}{3}
+2\sum_{r\ge1}\frac{e^{-rw}}{r^2}S_2(rw),
\]
I obtain, to the precision needed here,

\[
\begin{array}{c|c}
w&H(w)\text{ approximately}\\ \hline
4&1.1933336\\
5&1.9608294\\
6&2.8343312\\
8&4.7376480\\
10&6.7156710\\
20&16.7101328\\
40&36.7101319
\end{array}
\]

These support every interval in SOL.3.28.

Likewise,
\[
T(w)=120\sum_{r\ge1}\frac{e^{-rw}}{r^2}S_5(rw)
\]
gives approximately
\[
\begin{array}{c|c}
w&T(w)\\ \hline
8&22.989883\\
10&8.052473\\
14&0.663850\\
20&0.008629061\\
40&4.95\times10^{-10}
\end{array}
\]
so all bounds in SOL.3.29 appear numerically true.

Using
\[
F_1(y)
=
y^5\frac{q(1+11q+11q^2+q^3)}{(1-q)^5},
\qquad q=e^{-y},
\]
gives
\[
F_1(8)\approx11.0515,\qquad
F_1(10)\approx4.5433,\qquad
F_1(14)\approx0.44722.
\]

For an independent global-maximization check, solve
\[
\frac5y=\frac{A_5(y)}{A_4(y)},
\]
where
\[
\frac{A_5(y)}{A_4(y)}
=
\frac{1+26q+66q^2+26q^3+q^4}
{(1-q)(1+11q+11q^2+q^3)}.
\]
This gives an interior maximizer near \(y=3.7\) and a maximum consistent with
\[
24.854113\ldots.
\]

These are high-precision corroborations only. The assertion that exact rational certificates were actually run is not sourced by an output artifact.

---

## 4. \(W_4\)–\(W_{6b}\) numerical arithmetic

The proof-safe coarse calculations are correct.

At \(w=8\),
\[
\frac{197.4-192+16+23.01}{120\cdot4.73}
=
\frac{44.41}{567.6}
\approx0.078242<0.079.
\]
Using the sharper actual values gives the quoted \(0.078066\ldots\).

At \(w=10\), the displayed coarse lower bound is
\[
10.8(6.71)-(260-197.39+8.06)
=72.468-70.67
=1.798>1.7.
\]
The quoted sharper value \(1.86886\ldots\) is consistent.

At \(w=14\),
\[
16.8(10.71)-(364-197.39+0.665)
=179.928-167.275
=12.653>12.
\]
The quoted sharper value \(12.66161\ldots\) is consistent.

The rational \(B^2<6A^2\) check is
\[
B^2=336^2=112896,
\]
\[
6A^2>6(138.6)^2=115259.76.
\]
With the actual \(C=20\pi^2\),
\[
6A^2\approx115272.92.
\]

The endpoint estimates are also consistent:
\[
\frac{480-20\pi^2+T(20)}{120H(20)}
\approx0.140941<0.142,
\]
\[
\frac{960-20\pi^2+T(40)}{120H(40)}
\approx0.173115<0.174.
\]

**Result:** PASS.

---

## 5. Exact finite-\(m\) assembly

This can be checked with no floating-point arithmetic:

```python
from fractions import Fraction as F

rows = [
    ("W1",  5, F(119,100), F(121,5000), F(261,10000)),
    ("W2",  6, F(49,25),   F(11,625),   F(191,10000)),
    ("W3",  8, F(283,100), F(183,5000), F(381,10000)),
    ("W4", 10, F(473,100), F(9,100),    F(57,625)),
    ("W5", 20, F(671,100), F(71,500),   F(18,125)),
    ("W6", 40, F(167,10),  F(87,500),   F(1763,10000)),
]

for name,b,L,B,cap in rows:
    h = F(b,561)
    e = h*h*(F(b,12)+F(7,4))
    E = F(49,2)*h + 375*h*h + F(b,200)*h**6
    U = L*B/(L-e) + E/(120*(L-e))
    print(name, float(U), U < cap)
```

Expected output, modulo final decimal rounding:
\[
\begin{array}{c|c}
W_1&0.02594\ldots\\
W_2&0.01890\ldots\\
W_3&0.03786\ldots\\
W_4&0.090995\ldots\\
W_5&0.143770\ldots\\
W_{6b}&0.176096\ldots
\end{array}
\]
and every exact comparison with the corresponding cap returns `True`.

Thus the final assembly arithmetic is correct **conditional on the continuum bounds \(B\)**.

---

## 6. The load-bearing certificate that is not actually supplied

The essential claims
\[
\max_{I\subset[4,5]}V(I)=0.024174220\ldots,
\]
\[
\max_{I\subset[5,6]}V(I)=0.017550592\ldots,
\]
\[
\max_{I\subset[6,8]}V(I)=0.036526655\ldots,
\]
and
\[
\max V_{\text{old }1/64}=0.037828957\ldots
\]
cannot be verified from the draft.

A deterministic exact implementation must form, for each cell
\(I=[\alpha,\beta]\) and \(N=n+5\),
\[
p^-_{n,I}
=
Q_n\left[
N\frac{\pi_L^2}{6}-\beta
-N\left(
\sum_{r=1}^{64}f_{r,N}(\alpha)^+
+R_N
\right)
\right],
\]
\[
p^+_{n,I}
=
Q_n\left[
N\frac{\pi_U^2}{6}-\alpha
-N\sum_{r=1}^{64}f_{r,N}(\beta)^-
\right],
\]
where
\[
f_{r,N}(w)=\frac{e^{-rw}}{r^2}S_N(rw)
\]
and \(R_N\) is the SOL.6.9 tail bound. Then
\[
\sup_I|p_n|
=
\max(|p^-_{n,I}|,|p^+_{n,I}|).
\]

A valid lower bound for \(H\) is, for example,
\[
H_I^-=
\alpha-\frac{\pi_U^2}{3}
+
2\sum_{r=1}^{R}
\frac{e^{-r\alpha,-}}{r^2}S_2(r\alpha),
\]
where the omitted tail is positive. Finally compute
\[
V(I)=
\frac1{H_I^-}
\sum_{n=0}^{64}
\frac{\sup_I|p_n|\,n!}{2^n(n+5)!}
+
\frac{11}{10^6\,120H_I^-}.
\]

The draft does not provide:

- the exponential truncation \(K\) used for each rational enclosure;
- the scalar-tail cutoff used for \(H_I^-\);
- any exact numerator/denominator for the claimed maxima;
- the maximizing cell indices in machine-readable output;
- source code, stdout, or hashes.

Because the margins are only \(0.107\%\), \(0.281\%\), and \(0.201\%\), approximate agreement is not sufficient.

Therefore the four quoted cell maxima are **FABRICATED-until-sourced**.

The same applies to the claim that all \(23552\) \(F_1\)-cells satisfy
\[
b^5A_4(a)<25.
\]
The mathematical enclosure \(F_1(y)\le b^5A_4(a)\) is valid, but the claimed execution and its “largest upper bound below \(24.90\)” are **FABRICATED-until-sourced** without exact output.

---

## 7. Off-grid attacks required

### 7.1 Claimed worst cells

At a minimum, directly evaluate both \(\mathcal B_\infty\) and \(Q\) at the endpoints, midpoints, and adjacent floating-point values of

\[
[4,513/128],
\qquad
[5,641/128],
\qquad
[1023/128,8].
\]

For each point, optimize over \(x\in[0,1/2]\), rather than checking only \(x=1/2\). The proof majorants are monotone in \(x\), but the actual complex remainder need not be.

### 7.2 All band boundaries

For \(m=561,562,700,1000,5000\), use
\[
w\in
\{4+\varepsilon,\,
5-\varepsilon,5,5+\varepsilon,\,
6-\varepsilon,6,6+\varepsilon,\,
8-\varepsilon,8,8+\varepsilon,
\]
\[
10-\varepsilon,10,10+\varepsilon,\,
14-\varepsilon,14,14+\varepsilon,\,
20-\varepsilon,20,20+\varepsilon,\,
40-\varepsilon,40,40+\varepsilon,\,
0.89m-\varepsilon,0.89m\},
\]
with \(\varepsilon=2^{-40}\), whenever admissible, and
\[
x\in
\{0,2^{-20},1/8,1/4,3/8,1/2-2^{-40},1/2\}.
\]

Every value of \(Q(m,w/m,x)\) must lie below the band target.

### 7.3 W7 feasibility corners

The formal W7 estimate combines the unattainable rectangular corner
\((\lambda,w)=(0.89,40)\). Actual feasible corners are safer:

- At \(m=561,\ w\downarrow40\),
  \[
  \lambda\approx\frac{40}{561},
  \quad
  G(\lambda)\ge1-\frac{\lambda^2}{12},
  \]
  giving
  \[
  \frac{D_m}{m}\gtrsim0.9173,
  \qquad
  \frac{50}{120(D_m/m)}\lesssim0.4543.
  \]

- At \(m=561,\lambda=0.89\), \(w=499.29\), giving
  \[
  \frac{D_m}{m}>
  0.93649-\frac{3.29}{499.29}
  \approx0.92990,
  \]
  and the same crude remainder bound is about \(0.4481\).

Thus I see no W7 corner counterexample, but these do not replace a direct scan.

### 7.4 Direct corroborative values

The draft quotes
\[
Q(561,4.5/561,0.5)\approx0.00799447,
\]
\[
Q(561,0.89,0.5)\approx0.194721.
\]
No output or precision-doubling check is supplied. These two decimals are therefore **FABRICATED-until-sourced**, though both are comfortably below their targets and are plausible.

A proper replay should evaluate the integral at, say, 100 and 160 digits with separately split quadrature intervals and require agreement to at least 50 digits.

---

## 8. Other provenance defects

The reference to `referee_replay_sol_s2b_20260812.md` does not by itself certify this attempt. The current draft changes both the cell width and the trapezoid coefficient. A replay of attempt 2 is usable only if the report identifies the exact current script/input hashes and confirms that it reran:

1. width \(1/128\), not \(1/64\);
2. \(1/8\), not \(1/12\);
3. the exact current definitions of \(V(I),e_b,E_b\).

The Machin assertion also needs explicit truncation orders and the resulting rational endpoints. For example, one can use consecutive alternating partial sums through \(K=20\) for \(\arctan(1/5)\) and \(K=5\) for \(\arctan(1/239)\), then check the displayed decimal fractions exactly.

VERDICT: MAJOR_ISSUES

1. The load-bearing \(512\)-cell \(W_1\)–\(W_3\) certificate has no script, exact fractions, output, or reproducible enclosure parameters. Its quoted maxima are **FABRICATED-until-sourced**.
2. The \(23552\)-cell proof of \(F_1<25\) is likewise asserted but not archived; this affects both W7 and the finite-\(m\) correction.
3. The claimed exact scalar certificates omit exponential truncation orders and tail cutoffs. Their numerical values are corroborated, but their exact-certificate status is **FABRICATED-until-sourced**.
4. The cited replay is for `sol_s2b`, while the reviewed object is `sol_s2c`; no hash or output proves that the corrected width and \(1/8\) coefficient were rerun.
5. The two direct remainder values and all claimed off-grid replay results lack output and precision-doubling evidence; no adversarial boundary/inner-\(x\) scan is supplied.