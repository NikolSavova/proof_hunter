# numerics referee (gpt-5.6-sol, effort=max) — sol_s3w7cert_20260812.md — 2026-08-12 19:56

> Cross-model referee report (Sol on the reviewed draft). Numeric checks are
> DERIVED, not executed — script them before trusting.

# Numerics-referee report

## Executive finding

I could not break the load-bearing W7 arithmetic. The exact-rational checks behind SOL.9–SOL.17 all pass:

\[
L_2=L_{2,0}\approx0.0827365808568<0.09,
\qquad
L_4=L_{4,0}\approx0.987755102836<0.99,
\]

and hence

\[
U_7\approx2.180398736<2.4,
\qquad
J_{\rm cert}\approx2.248016201<2.25.
\]

The latter comparison has margin only about

\[
\frac94-J_{\rm cert}\approx1.9838\times10^{-3},
\]

so it must remain exact-rational. The weaker, load-bearing \(J<3.31<4.5\) chain has much more slack.

However, the submission is not yet citable: the exact archived value of \(J_0(W7)\) is absent, SOL.3 and SOL.5 are unsupported external numerical assertions, and the stated Euler–Maclaurin remainder kernel has its sign reversed. The sign error does not affect the absolute-value bound.

---

## 1. Kernel, Bernoulli, and Euler–Maclaurin checks

### 1.1 Corrected constant

Exactly,

\[
\frac{17}{10321920}
=\frac{17/256}{8!}
=\frac{(2-2^{-7})|B_8|}{8!}.
\]

Numerically,

\[
\mathfrak c_8=1.6469804\ldots\times10^{-6}.
\]

The Bernoulli extremum can be derived without a numerical root finder. With
\(u=t(1-t)\in[0,1/4]\),

\[
B_8(t)-B_8
=u^2\left(u^2+\frac43u+\frac23\right).
\]

The right side is increasing in \(u\), so its maximum occurs at \(u=1/4\):

\[
\max_{0\le t\le1}(B_8(t)-B_8)
=\frac1{16}\left(\frac1{16}+\frac13+\frac23\right)
=\frac{17}{256}.
\]

Thus the numerical constant is valid.

### 1.2 Remainder-kernel sign error

For the displayed convention \(R_8=\text{LHS}-\text{displayed EM terms}\), the no-\(B_8\)-endpoint kernel is

\[
\frac{B_8-B_8(\{x/\lambda\})}{8!},
\]

not its negative.

Exact sentinel: set \(m=\lambda=1\) and \(f(x)=x^8\). The terms through \(B_6\) give

\[
\frac19+\frac12+\frac{8}{12}-\frac{336}{720}
+\frac{6720}{30240}
=\frac{31}{30}.
\]

Since the left side is \(f(1)=1\),

\[
R_8=-\frac1{30}.
\]

But integrating the draft’s stated kernel
\((B_8(x)-B_8)/8!\) against \(f^{(8)}=8!\) gives \(+1/30\).
The absolute bound using \(17/256\) remains correct.

### 1.3 Kernel series checks

Symbolic expansion gives

\[
h_2(x)=1-\frac{x^2}{12}+\frac{x^4}{240}
-\frac{x^6}{6048}+\frac{x^8}{172800}
-\frac{x^{10}}{5322240}+\cdots,
\]

\[
h_3(x)=2-\frac{x^4}{120}+\frac{x^6}{1512}
-\frac{x^8}{28800}+\frac{x^{10}}{665280}+\cdots,
\]

\[
h_4(x)=6+\frac{x^4}{120}-\frac{x^6}{504}
+\frac{x^8}{5760}-\frac{x^{10}}{95040}+\cdots.
\]

These confirm the endpoint values and vanishing odd derivatives. Also,

\[
h_4=x^2h_2+6h_2^2
\]

is an exact algebraic identity.

A useful exact cumulant sign/index sentinel is \(m=2\), for which the law is Bernoulli with \(q=e^{-\lambda}\). SOL.2 must reproduce

\[
\kappa_2=\frac q{(1+q)^2},\qquad
\kappa_3=\frac{q(1-q)}{(1+q)^3},\qquad
\kappa_4=\frac{q(1-4q+q^2)}{(1+q)^4}.
\]

It does.

---

## 2. Eulerian sums and derivative-integral bounds

Using the draft’s Eulerian-polynomial formula, I obtain:

\[
F_9(1/3)=\frac{145083648}{1024}=141683.25,
\]

\[
F_{10}(1/3)=\frac{2641216512}{2048}=1289656.5,
\]

\[
F_{11}(1/3)=\frac{52891055616}{4096}
=12912855.375.
\]

Hence the actual local bounds produced by the proof are

\[
\frac{F_9(1/3)}{32}=4427.6015625<4500,
\]

\[
\frac{F_{10}(1/3)}{32}=40301.765625<41000,
\]

\[
\frac{F_{11}(1/3)}{32}=403526.73046875<410000.
\]

At \(r=1/7\),

\[
F_8(1/7)=\frac{1015741440}{10077696}
\approx100.791038<102,
\]

\[
F_9(1/7)=\frac{28187212032}{60466176}
\approx466.164952<468,
\]

\[
F_{10}(1/7)=\frac{869113276416}{362797056}
\approx2395.590764<2600.
\]

The tail coefficients recompute exactly as

\[
(Q_0,Q_1,Q_2,Q_3,Q_4)=(1,3,10,38,168),
\]

\[
(C_2,C_3,C_4)=(114,1118,10456).
\]

Therefore the coarse tail bounds are exactly

\[
114\cdot102=11628,
\]

\[
1118\cdot468=523224,
\]

\[
10456\cdot2600=27185600.
\]

The resulting global bounds are

\[
4500+11628=16128<20000,
\]

\[
41000+523224=564224<600000,
\]

\[
410000+27185600=27595600<28000000.
\]

Thus \(K_2,K_3,K_4\) are valid.

---

## 3. Far-endpoint estimate

The displayed rational majorant simplifies exactly to

\[
\frac{2^{-56}}{1-2^{-48}}40^4
\left(\frac{11}{10}\right)^5
=
\frac{161051}{10(2^{48}-1)}
\approx5.72168\times10^{-11}<10^{-9}.
\]

Also,

\[
\frac{\beta}{2}
+\frac{\beta^2}{12}
+\frac{\beta^4}{720}
+\frac{\beta^6}{30240}
\approx0.5118961879<1.
\]

Thus the entire endpoint bracket is actually bounded by about

\[
0.5118962(5.72168\times10^{-11})
<2.93\times10^{-11},
\]

which is much smaller than \(\varepsilon_\infty=10^{-9}\).

There is one omitted logical step: after obtaining a factor \(x^4e^{-x}/(1-256e^{-x})\), the proof must say that this is decreasing for \(x\ge40\). One cannot simply replace \(x^4\) by \(40^4\) because \(x\ge40\).

---

## 4. Intrinsic \(h_4\) floor

The final lower bound in SOL.13 is exactly

\[
\frac1{120}-\frac{4/5}{504}
-\frac{(4/5)^3}{120960}
=
\frac{6371}{945000}
\approx0.00674179894>0.
\]

Thus the proposed polynomial argument really does prove \(h_4(x)\ge6\) on \(0\le x\le0.89\).

---

## 5. Exact-rational W7 certificate

The following standard-library Python script performs all load-bearing rational checks.

```python
from fractions import Fraction as Q
from math import comb, factorial
from decimal import Decimal, getcontext

getcontext().prec = 50

def dec(x):
    return Decimal(x.numerator) / Decimal(x.denominator)

def eulerian(p, k):
    return sum(
        (-1)**j * comb(p + 1, j) * (k + 1 - j)**p
        for j in range(k + 2)
    )

# F_p(1/k)
def F(p, k):
    num = sum(eulerian(p, j) * k**(p-j) for j in range(p))
    den = (k - 1)**(p + 1)
    return Q(num, den)

# Corrected EM constant
c8 = Q(17, 10321920)
assert c8 == (Q(2) - Q(1,128)) * Q(1,30) / factorial(8)

# Eulerian sentinels
assert F(9,3)  == Q(145083648, 1024)
assert F(10,3) == Q(2641216512, 2048)
assert F(11,3) == Q(52891055616, 4096)

assert F(8,7)  == Q(1015741440, 10077696)
assert F(9,7)  == Q(28187212032, 60466176)
assert F(10,7) == Q(869113276416, 362797056)

assert F(9,3)  < 144000
assert F(10,3) < 1312000
assert F(11,3) < 13120000
assert F(8,7)  < 102
assert F(9,7)  < 468
assert F(10,7) < 2600

def Qp(p):
    return factorial(p) * sum(
        Q(2**c, factorial(c)) for c in range(p+1)
    )

assert [Qp(p) for p in range(5)] == [1,3,10,38,168]

def falling(n,a):
    return factorial(n) // factorial(n-a)

def C(n):
    return sum(
        comb(8,a) * falling(n,a) * Qp(n-a)
        for a in range(n+1)
    )

assert [C(2), C(3), C(4)] == [114,1118,10456]

assert 4500   + 114*102    < 20000
assert 41000  + 1118*468   < 600000
assert 410000 + 10456*2600 < 28000000

# Far endpoint
Efar = (
    Q(1,2**56) / (1-Q(1,2**48))
    * 40**4 * Q(11,10)**5
)
assert Efar == Q(161051, 10*(2**48-1))
assert Efar < Q(1,10**9)

beta = Q(89,100)
endpoint_coeff = (
    beta/2 + beta**2/12 + beta**4/720 + beta**6/30240
)
assert endpoint_coeff < 1

# h4 floor sentinel
h4_floor_sentinel = (
    Q(1,120) - Q(4,5)/504 - Q(4,5)**3/120960
)
assert h4_floor_sentinel == Q(6371,945000)
assert h4_floor_sentinel > 0

# W7 losses
eps  = Q(1,10**9)
lam0 = Q(40,561)
Ppi  = Q(484,49)
I2   = Ppi/3
I4   = 4*Ppi
K2   = 20000
K4   = 28000000

L20 = (
    lam0**2/12
    + (I2 + eps + c8*K2*lam0**8)/40
)
L21 = (
    beta**2/12
    + (I2 + eps)/(561*beta)
    + c8*K2*beta**7/561
)

L40 = (I4 + eps + c8*K4*lam0**8)/40
L41 = (
    (I4 + eps)/(561*beta)
    + c8*K4*beta**7/561
)

L2 = max(L20,L21)
L4 = max(L40,L41)

assert L2 == L20
assert L4 == L40
assert L2 < Q(9,100)
assert L4 < Q(99,100)

U7 = Q(2)/(1-L2)
Jcert = U7**2 - (Q(6)-L4)/2

assert U7 < Q(12,5)
assert Jcert < Q(9,4)

# Rounded chain
assert Q(12,5)**2 - Q(49,10)/2 == Q(331,100)
assert Q(331,100) < Q(9,2)

literal_J0 = Q(459597,100000)
assert literal_J0 - Q(9,2) == Q(9597,100000)

for name, value in [
    ("L20",L20), ("L21",L21),
    ("L40",L40), ("L41",L41),
    ("U7",U7), ("Jcert",Jcert)
]:
    print(name, dec(value))
```

Expected intervals are:

\[
0.08273658085<L_{2,0}<0.08273658087,
\]

\[
0.07262870<L_{2,1}<0.07262871,
\]

\[
0.98775510283<L_{4,0}<0.98775510285,
\]

\[
0.1154919<L_{4,1}<0.1154920.
\]

Hence

\[
1-L_2\approx0.917263419143,
\qquad
6-L_4\approx5.012244897164,
\]

\[
U_7\approx2.180398736,
\qquad
J_{\rm cert}\approx2.248016201.
\]

The exact margins are approximately

\[
0.09-L_2\approx7.26342\times10^{-3},
\]

\[
0.99-L_4\approx2.24490\times10^{-3},
\]

\[
\frac94-J_{\rm cert}\approx1.98380\times10^{-3}.
\]

Using actual \(\pi^2\) instead of \(484/49\) gives approximately

\[
L_2=0.0826703590\ldots,\qquad
L_4=0.9869604409\ldots,
\]

so the draft’s optional sharper sentinels are consistent.

---

## 6. Off-grid and corner attacks

Use stable kernel identities rather than the raw \(q/(1-q)^r\) forms:

\[
h_2(x)=\left(\frac{x/2}{\sinh(x/2)}\right)^2,
\]

\[
h_3(x)=x\coth(x/2)h_2(x),
\]

\[
h_4(x)=x^2h_2(x)+6h_2(x)^2.
\]

A direct high-precision attack should compare the \(H_n\)-sum route with the independent polylog-rational cumulant route:

```python
import mpmath as mp
mp.mp.dps = 100

def hvals(x):
    y = x/2
    h2 = (y/mp.sinh(y))**2
    h3 = x/mp.tanh(y) * h2
    h4 = x*x*h2 + 6*h2*h2
    return h2,h3,h4

def ell(z,n):
    if n == 2:
        return z/(1-z)**2
    if n == 3:
        return z*(1+z)/(1-z)**3
    if n == 4:
        return z*(1+4*z+z*z)/(1-z)**4
    raise ValueError

def evaluate(m,lam):
    rows = [hvals(j*lam) for j in range(1,m+1)]
    hl = hvals(lam)

    A = hl[0] - mp.fsum(r[0] for r in rows)/m
    B = hl[1] - mp.fsum(r[1] for r in rows)/m
    C = hl[2] - mp.fsum(r[2] for r in rows)/m

    q = mp.exp(-lam)
    H_alt = []
    for n in (2,3,4):
        kap = m*ell(q,n) - mp.fsum(
            (j**n)*ell(mp.exp(-j*lam),n)
            for j in range(1,m+1)
        )
        H_alt.append(lam**n * kap/m)

    assert abs(A-H_alt[0]) < mp.mpf("1e-70")
    assert abs(B-H_alt[1]) < mp.mpf("1e-70")
    assert abs(C-H_alt[2]) < mp.mpf("1e-70")

    r31 = abs(B)/A
    r42 = C/A
    J = r31*r31-r42/2

    assert A > mp.mpf(".91") and A < 1
    assert B >= 0 and B < 2
    assert C > mp.mpf("5.01")
    assert r31 < mp.mpf("2.4")
    assert r42 > mp.mpf("4.9")
    assert J < mp.mpf("2.25")
    return A,B,C,r31,r42,J

beta = mp.mpf(89)/100
lam0 = mp.mpf(40)/561
tiny = mp.mpf("1e-30")

probes = [
    # Just inside the strict w>40 boundary
    (561, (40+tiny)/561),

    # On both sides of the artificial lambda_0 case split
    (562, lam0-tiny),
    (562, lam0+tiny),

    # Upper corners, including just off-grid
    (561, beta),
    (562, beta-tiny),
    (10007, beta),

    # Interior non-cell points
    (997, mp.mpf(137)/1000),
    (809, mp.sqrt(2)/10),
]

for m,lam in probes:
    assert 40 < m*lam <= beta*m
    print(m, mp.nstr(lam,25),
          [mp.nstr(x,20) for x in evaluate(m,lam)])
```

Useful independent corner sentinels are:

| Corner | \(A\) | \(B\) | \(C\) | \(J\) |
|---|---:|---:|---:|---:|
| \(m\to\infty,\ w\downarrow40\) | \(0.9177533\) | \(1.7532599\) | \(5.0130396\) | \(0.918414\) |
| \(m=561,\ w\downarrow40\) | \(0.9182210\) | \(1.7550422\) | \(5.0183874\) | \(0.920592\) |
| \(m=561,\lambda=0.89\) | \(0.9308281\) | \(1.9771022\) | \(5.9305861\) | \(1.32583\) |
| \(m\to\infty,\lambda=0.89\) | \(0.9365260\) | \(1.9950870\) | \(6.0043076\) | \(1.332576\) |

The first limiting row has the exact formulas

\[
A=1-\frac{\pi^2}{120},\quad
B=2-\frac{\pi^2}{40},\quad
C=6-\frac{\pi^2}{10}.
\]

These attacks show no hidden corner close to the analytic bound \(2.248\); the certificate is very conservative relative to truth.

---

## 7. FABRICATED-until-sourced register

The following claims are not supported by an included derivation or identified artifact:

1. **\(J_0(W7)=4.59597\ldots\): FABRICATED-until-sourced.**  
   This is load-bearing. The literal rational \(459597/100000\) passes, but an ellipsis is not an exact theorem interface. Supply the archived \(p_7/q_7\), file/hash, and check
   \[
   2p_7>9q_7.
   \]

2. **SOL.3: width \(1/128\), all W1–W6b cells certified: FABRICATED-until-sourced.**  
   No script, output, cell count, minimum margin, or hash is supplied. It is not used in the W7 proof and can simply be removed from this replacement.

3. **SOL.5: pointwise \(\lvert h_n^{(8)}\rvert\le10^{12}\): FABRICATED-until-sourced.**  
   The newly proved integral bound does not imply a pointwise bound. Again, SOL.5 is not used in the W7 proof.

4. **\(\pi^2<484/49\): unsourced as submitted.**  
   The inequality is true because \(\pi<22/7\), but that classical inequality should be cited or proved. Numerically,
   \[
   \frac{484}{49}-\pi^2\approx0.007946619319>0.
   \]

5. **The scope \(m\ge561,\ 40<w\le0.89m\): interface-only until cited.**  
   These are legitimate assumptions if copied exactly from the archived W7 band table, but the draft should identify that source.

VERDICT: MINOR_REPAIRS

1. Insert the exact archived fraction \(J_0(W7)=p_7/q_7\), its provenance, and the exact check \(2p_7>9q_7\). Until then, the final implication to the campaign’s actual S3 target is unverified.
2. Remove or source SOL.3 and SOL.5. Their numerical claims are presently FABRICATED-until-sourced, although neither is needed for the W7 argument.
3. Reverse the stated Euler–Maclaurin remainder-kernel sign to \(B_8-B_8(\{x/\lambda\})\). The absolute remainder bound and every downstream number survive.
4. Add the missing monotonicity step justifying replacement of \(x\ge40\) by \(x=40\) in the far-endpoint estimate, and define \((n)_a\) explicitly as a falling factorial.
5. Cite or prove \(\pi<22/7\), and cite the exact source of the W7 scope constants \(561,40,89/100\).
6. Replace “No occurrence of `1/1209600` should remain”: that literal string occurs in the draft itself. The intended check should be “no operational formula uses the obsolete constant.”