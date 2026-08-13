# numerics referee (gpt-5.6-sol, effort=max) — sol_s3w7sign_20260812.md — 2026-08-12 19:52

> Cross-model referee report (Sol on the reviewed draft). Numeric checks are
> DERIVED, not executed — script them before trusting.

# Numerics referee report

## Bottom line

The standalone W7 argument in Lemma SOL.4 is numerically sound: I checked the rational arithmetic, the Bernoulli constant, the \(h_4\)-sum majorant, both \(U_c\) evaluations, and representative boundary points. I found no numerical counterexample to \(J<4\) on W7.

The claimed closure of all of (S3), however, rests on an “established exact-arithmetic certificate” for W1–W6b that is not supplied, named, hashed, summarized, or even specified well enough to reconstruct. The derivative bound \(M_8=10^{12}\) is likewise asserted rather than certified on the crucial interval \([0,1]\). Thus Theorem SOL.6 and “no mathematical gap remains” do not survive as a proof artifact.

---

## 1. Closed forms and cumulant identities

For scripting, avoid the infinite sums. With \(q=e^{-x}\) and \(d=1-q=-\operatorname{expm1}(-x)\),
\[
h_2(x)=x^2\frac{q}{d^2},
\]
\[
h_3(x)=x^3\frac{q(1+q)}{d^3},
\]
\[
h_4(x)=x^4\frac{q(1+4q+q^2)}{d^4}.
\]

Equivalently, with \(y=x/2\) and \(S(y)=\sinh(y)/y\),
\[
h_2=S^{-2},\qquad
h_3=2\cosh(y)S^{-3},\qquad
h_4=2(\cosh(2y)+2)S^{-4}.
\]
These formulas check exactly.

A direct independent cumulant oracle is
\[
L_m(\lambda)
 =\sum_{j=1}^m\log(1-e^{-j\lambda})
   -m\log(1-e^{-\lambda}).
\]
Then one must obtain
\[
L_m''(\lambda)=\frac A{\lambda^2},\qquad
-L_m'''(\lambda)=\frac B{\lambda^3},\qquad
L_m^{(4)}(\lambda)=\frac C{\lambda^4}.
\]
Automatic differentiation at, for example, \(m=7,\lambda=0.37\), should agree to the working precision.

There is one scope error: the opening assertion \(A>0\) is false for \(m=1\), because then \(A=0\) exactly. It is true for \(m\ge2\), and hence harmless in the advertised \(m\ge561\) application.

Useful exact endpoint data are
\[
h_2(0)=1,\qquad h_3(0)=2,\qquad h_4(0)=6.
\]

---

## 2. Lemmas SOL.1–SOL.2

For
\[
F(t)=t\cosh t+2t-3\sinh t,
\]
direct differentiation gives
\[
F'(t)=t\sinh t+2-2\cosh t,
\]
\[
F''(t)=t\cosh t-\sinh t,
\qquad
F'''(t)=t\sinh t.
\]
Thus
\[
F(0)=F'(0)=F''(0)=0.
\]

The claimed identity is exact:
\[
3\left(\coth y-\frac1y\right)-\tanh y
 =\frac{F(2y)}{y\sinh(2y)}.
\]

Near the cancellation-prone endpoint,
\[
F(t)=\frac{t^5}{60}+O(t^7),
\]
and hence
\[
3\left(\coth y-\frac1y\right)-\tanh y
 =\frac{4}{15}y^3+O(y^5)>0.
\]
A floating-point checker should use this series for very small \(y\), rather than subtracting three nearly equal terms.

The logarithmic derivative
\[
\frac d{dy}\log h_3(2y)
 =-\left[3\left(\coth y-\frac1y\right)-\tanh y\right]
\]
is therefore strictly negative. Consequently
\[
0<B<mh_3(\lambda)\qquad(m\ge2),
\]
so the repaired squaring step is valid.

---

## 3. Euler–Maclaurin constant

Let \(\widetilde B_8(t)=B_8(\{t\})\). For the right sum
\[
R_\lambda(f)=\lambda\sum_{j=1}^m f(j\lambda),\qquad w=m\lambda,
\]
the no-\(B_8\)-endpoint identity should be implemented, up to the sign convention used to define \(E_{8}\), with kernel
\[
\widetilde B_8(x/\lambda)-B_8.
\]

A decisive normalization oracle is \(f(x)=x^8\). If terms only through \(B_6\) are retained, the omitted contribution has magnitude
\[
\frac{\lambda^8}{30}w.
\]
Any implementation failing this polynomial test has the wrong sign, scaling, or endpoint convention.

The Bernoulli arithmetic checks exactly:
\[
B_8(0)=-\frac1{30}=-\frac{128}{3840},
\]
\[
B_8(1/2)=\frac{127}{3840},
\]
\[
\sup_{0\le u\le1}|B_8(u)-B_8|
 =\frac{255}{3840}
 =\frac{17}{256}.
\]
Therefore
\[
K_{\rm EM}
 =\frac{17}{256\cdot8!}
 =\frac{17}{10321920}
 =1.6469804067460317\ldots\times10^{-6}.
\]
Also
\[
\frac{K_{\rm EM}}{1/1209600}
 =\frac{255}{128}
 =1.9921875.
\]
Thus the corrected error allowance is almost twice the old one.

If W1–W6b means \(4<w<40\), \(m\ge561\), and the advertised global \(M_8=10^{12}\) is used, the worst raw remainder bound per \(h_n\) has supremum
\[
R_{\max}
 =\frac{17\cdot10^{12}\cdot40^9}
 {10321920\cdot561^8}
 \approx 0.0440074.
\]
The old coefficient would give approximately \(0.0220900\). This is too large a change to accept a statement that the previous certificate was “corrected” without an actual rerun report and post-correction minimum slack.

---

## 4. Status of the \(M_8=10^{12}\) derivative claim

The formula in SOL.5 does permit a partial independent check. From
\[
e>\frac{1957}{720}
\]
one has
\[
1-e^{-1}>\frac{1237}{1957}.
\]
For \(p=8\), define the exact rational upper bound
\[
\widehat C_{n,8}
 =
 \sum_{r=0}^n
 \binom8r\frac{n!}{(n-r)!}
 (n+7-r)!
 \left(\frac{1957}{1237}\right)^{n+8-r}.
\]
Exact `Fraction` arithmetic gives the safe comparisons
\[
\widehat C_{2,8}<10^8,\qquad
\widehat C_{3,8}<2\cdot10^9,\qquad
\widehat C_{4,8}<5\cdot10^{10}.
\]
Hence \(10^{12}\) is justified by the draft's own argument for \(x\ge1\).

It is not justified on \(0\le x\le1\). At \(x=0\), the exact series are
\[
h_2(x)=1-\frac{x^2}{12}+\frac{x^4}{240}
       -\frac{x^6}{6048}+\frac{x^8}{172800}+O(x^{10}),
\]
\[
h_3(x)=2-\frac{x^4}{120}+\frac{x^6}{1512}
       -\frac{x^8}{28800}+O(x^{10}),
\]
\[
h_4(x)=6+\frac{x^4}{120}-\frac{x^6}{504}
       +\frac{x^8}{5760}+O(x^{10}),
\]
and therefore
\[
h_2^{(8)}(0)=\frac7{30},\qquad
h_3^{(8)}(0)=-\frac75,\qquad
h_4^{(8)}(0)=7.
\]
These endpoint values strongly suggest that \(10^{12}\) is safe, but they do not certify the whole interval. An Arb/MPFI interval subdivision or a rigorous Taylor remainder is still required.

Accordingly, the claim
\[
|h_n^{(8)}(x)|\le10^{12}\quad(0\le x\le40)
\]
is **FABRICATED-until-sourced** on \([0,1]\).

A script for the \(x\ge1\) part is:

```python
from fractions import Fraction as Q
from math import comb, factorial

def Cup(n, p=8):
    ans = Q(0)
    for r in range(n+1):
        ans += (comb(p,r)
                * factorial(n)//factorial(n-r)
                * factorial(n+p-1-r)
                * Q(1957,1237)**(n+p-r))
    return ans

assert Cup(2) < 10**8
assert Cup(3) < 2*10**9
assert Cup(4) < 5*10**10
```

---

## 5. Exact audit of the W7 constants

### 5.1 Small-\(\lambda\) estimates

All displayed cross-products check:

\[
207\cdot232079-200\cdot240000=40353,
\]
\[
100\cdot200^2-93\cdot207^2=15043,
\]
\[
6\cdot200^4-5\cdot207^4=419815995.
\]

The additional unstated check for (5) is
\[
100\cdot2399^2-99\cdot2400^2=5280100>0.
\]

Thus
\[
\left(\frac{200}{207}\right)^2>\frac{93}{100},
\]
\[
6\left(\frac{200}{207}\right)^4>5,
\]
and
\[
\left(\frac{2399}{2400}\right)^2>\frac{99}{100}.
\]

### 5.2 Global \(h_4<7\)

The power-series coefficient test is correct. For \(k\ge3\), positivity is equivalent to
\[
R_k=
\frac{7(4^k-4)}
{(2k)(2k-1)(2k-2)(2k-3)}>1.
\]
The initial values are
\[
R_3=\frac76,\qquad R_4=\frac{21}{20}.
\]
Moreover
\[
\frac{4^{k+1}-4}{4^k-4}>4,
\]
while the denominator's growth ratio is
\[
\frac{(2k+2)(2k+1)}{(2k-2)(2k-3)}\le3
\qquad(k\ge4).
\]
Thus this part checks.

### 5.3 \(h_2\)-sum

Exactly,
\[
\sum_{k=1}^5\frac1{k^2}=\frac{5269}{3600},
\]
and
\[
\sum_{k=6}^{\infty}\frac1{k(k-1)}=\frac15=\frac{720}{3600}.
\]
Hence
\[
\frac{5989}{3600}<\frac53,
\qquad
\frac53-\frac{5989}{3600}=\frac{11}{3600}.
\]
Therefore
\[
\int_0^\infty h_2(x)\,dx
 =2\zeta(2)=\frac{\pi^2}{3}<\frac{10}{3}.
\]

### 5.4 \(h_4\)-sum

The tail integral is correct:
\[
\int_4^\infty x^4e^{-x}\,dx
 =(4^4+4\cdot4^3+12\cdot4^2+24\cdot4+24)e^{-4}
 =824e^{-4}.
\]
Multiplying by \(6\) gives \(4944e^{-4}\).

The exact exponential checks are
\[
2\cdot1957^4-109\cdot720^4
 =42983685602>0,
\]
and the omitted derivation of \(e^5>148\) can be completed by
\[
\frac{109}{2}\frac{1957}{720}
 =\frac{213313}{1440}
 >148,
\]
with integer margin
\[
109\cdot1957-148\cdot1440=193.
\]

The final rational margin checks:
\[
94\cdot109\cdot147^4-9888\cdot148^4
 =40242018918>0.
\]

Numerically,
\[
K_4
 =35+\frac{4944e^{-4}}{(1-e^{-5})^4}
 \in(128.0347,128.0348),
\]
consistent with the stated \(128.0347\).

### 5.5 \(U_c\) envelopes

Differentiation gives
\[
U_c'(w)
 =-\frac{80/3}
 {w^2(c-10/(3w))^3}
 -\frac{129}{2w^2}<0,
\]
on the relevant domains.

The first endpoint checks exactly:
\[
U_{99/100}(40)
 =\left(\frac{75}{34}\right)^2-\frac{71}{80}
 =\frac{91981}{23120}
 =4-\frac{499}{23120}.
\]
Thus
\[
U_{99/100}(40)
 =3.978416955\ldots.
\]

For the second endpoint,
\[
U_{93/100}(561/10)
 =\left(\frac{336600}{146519}\right)^2-\frac{505}{374}
\]
and, exactly,
\[
U_{93/100}(561/10)
 =\frac{31532787672695}{8028963693014}
 =3.927379532\ldots.
\]
The gap to \(4\) is
\[
\frac{583067099361}{8028963693014}>0,
\]
which agrees with
\[
2001\cdot146519^2-374\cdot336600^2
 =583067099361.
\]

Finally,
\[
\frac{459597}{100000}-U_{99/100}(40)
 =\frac{17847283}{28900000}
 =0.61755\ldots>0.
\]

All W7 rational arithmetic therefore passes.

---

## 6. Direct W7 corner probes

A stable direct-sum oracle is:

```python
import mpmath as mp
mp.mp.dps = 80

def hs(x):
    q = mp.exp(-x)
    d = -mp.expm1(-x)
    return (
        x*x*q/d**2,
        x**3*q*(1+q)/d**3,
        x**4*q*(1+4*q+q*q)/d**4
    )

def scaled_ABC_J(m, lam):
    w = m*lam
    h0 = hs(lam)
    sums = [mp.fsum(hs(j*lam)[r] for j in range(1,m+1))
            for r in range(3)]
    a = w*h0[0] - lam*sums[0]  # lambda*A
    b = w*h0[1] - lam*sums[1]  # lambda*B
    c = w*h0[2] - lam*sums[2]  # lambda*C
    J = (b/a)**2 - c/(2*a)
    return a,b,c,J
```

Representative outputs should be:

1. At the exact W7 seam
   \[
   (m,\lambda)=\left(561,\frac{40}{561}\right):
   \]
   \[
   \lambda A\approx36.7288405705,
   \]
   \[
   \lambda B\approx70.2016882349,
   \]
   \[
   \lambda C\approx200.7354947438,
   \]
   \[
   J\approx0.920592234.
   \]

2. At the branch point
   \[
   (m,\lambda)=(561,0.1):
   \]
   \[
   \lambda A\approx52.8134052320,
   \]
   \[
   \lambda B\approx102.4303488860,
   \]
   \[
   \lambda C\approx297.4216290344,
   \]
   \[
   J\approx0.945790590.
   \]

Both are far below \(4\).

The following off-grid attacks are mandatory:

```python
eps = mp.mpf(2)**-40
tests = [
    (561, (40-eps)/561),  # compact-certificate side
    (561, mp.mpf(40)/561),
    (561, (40+eps)/561),  # W7 side
    (562, mp.mpf(40)/562),
    (561, mp.mpf('0.1')-eps),
    (561, mp.mpf('0.1')),
    (561, mp.mpf('0.1')+eps),
    (561, mp.mpf('0.89')),
    (561, (4+eps)/561),   # lower compact edge
    (10000, mp.mpf(40)/10000),
]
```

For every test with \(w\ge40\), direct computation must give \(J<4\). The first and penultimate tests lie in the purported compact certificate and cannot be compared to the correct \(J_0(W)\) because the W1–W6b band table is absent.

At \((m,\lambda)=(561,0.89)\), the analytic envelope itself gives
\[
U_{93/100}(499.29)
 =
 \left(\frac{29957400}{13830191}\right)^2
 -\frac12\left(5-\frac{12900}{49929}\right)
 \approx2.3211<4.
\]

The certificate must also test every band boundary and every mesh edge
\[
w=\frac{k}{128}\pm2^{-50},
\]
not merely cell centers. If the compact range is exactly \(4<w<40\) and \(\Delta\) refers only to a one-dimensional \(w\)-mesh, there are
\[
(40-4)\cdot128=4608
\]
base \(w\)-cells. The draft reports no cell count at all.

---

## 7. Endpoint term checks

The evenness argument is correct:
\[
h_n^{(7)}(0)=0,\qquad n=2,3,4.
\]

For the \(k=1\) term,
\[
e^x\frac{d^7}{dx^7}(x^ne^{-x})
 =
 \sum_{r=0}^n
 \binom7r\frac{n!}{(n-r)!}
 (-1)^{7-r}x^{n-r}.
\]
After division by \(x^n\), the limit is \(-1\). Contributions with \(k\ge2\) are exponentially smaller, so
\[
\lim_{x\to\infty}\frac{e^xh_n^{(7)}(x)}{x^n}=-1.
\]

At the finite endpoint \(x=40\), the leading \(k=1\) polynomials are
\[
-40^2+14\cdot40-42=-1082,
\]
\[
-40^3+21\cdot40^2-126\cdot40+210=-35230,
\]
\[
-40^4+28\cdot40^3-252\cdot40^2+840\cdot40-840
 =-1138440.
\]
Thus all three seventh derivatives are already negative and nonzero at \(40\), confirming that finite-\(w\) endpoint cancellation is unavailable.

---

## 8. Exact checker for the displayed arithmetic

```python
from fractions import Fraction as Q

assert 207*232079 - 200*240000 == 40353
assert 100*200**2 - 93*207**2 == 15043
assert 6*200**4 - 5*207**4 == 419815995
assert 100*2399**2 - 99*2400**2 == 5280100

assert 2*1957**4 - 109*720**4 == 42983685602
assert 109*1957 - 148*1440 == 193
assert 94*109*147**4 - 9888*148**4 == 40242018918

K = Q(17,10321920)
assert K / Q(1,1209600) == Q(255,128)

U1 = Q(75,34)**2 - Q(71,80)
assert U1 == Q(91981,23120)
assert 4-U1 == Q(499,23120)

U2 = Q(336600,146519)**2 - Q(505,374)
assert U2 == Q(31532787672695,8028963693014)
assert 4-U2 == Q(583067099361,8028963693014)

assert Q(459597,100000)-U1 == Q(17847283,28900000)

Rmax = Q(17*10**12*40**9, 10321920*561**8)
assert 0.0440 < float(Rmax) < 0.0441
```

---

## 9. FABRICATED-until-sourced register

Under the requested provenance rule, the following are **FABRICATED-until-sourced**:

1. The claim that an exact-arithmetic W1–W6b certificate exists and passes.
2. “Zero failed cells.” This appears only as an expected output in the recipe, not as an actual output.
3. The global derivative certificate \(M_8=10^{12}\) on \([0,1]\).
4. The assertion that the corrected coefficient \(17/10321920\) was actually used in a rerun.
5. The claimed mesh width \(1/128\) as an execution fact. It is declared, but no checker output confirms it.
6. Every W1–W6b endpoint and every corresponding exact \(J_0(W)\), because none is listed.
7. The imported constants \(m_0=561\), \(\Lambda=0.89\), \(w_7=40\), and \(J_{0,7}=459597/100000\) lack direct artifact citations in this draft. They are plausible campaign constants, not internally derived facts.
8. “Exact arithmetic” itself: the certificate necessarily handles exponentials or certified replacements for them, but no rational enclosure method, code, or archive is identified.

A valid certificate report must include at least:

- exact band endpoints and all exact \(J_0(W)\);
- variables being subdivided, not merely a cell width;
- total cell count and complete coverage proof;
- exact formulas for interval bounds on \(A,B,C,J\);
- proof that every lower bound for \(A\) is positive;
- directed rational enclosures for every transcendental quantity;
- the exact remainder coefficient as parsed by the checker;
- minimum post-correction slack and its cell/location;
- zero-failure output;
- code path, command line, immutable hash, and stdout artifact.

VERDICT: FATAL

1. **[FATAL]** The load-bearing W1–W6b “established exact-arithmetic certificate” is absent. No file, code, output, hash, cell count, minimum margin, or exact band table is supplied. Therefore Theorem SOL.6 does not establish (S3).
2. **[FATAL]** W1–W6b and their \(J_0(W)\) values are not defined in the draft, so continuum coverage, band seams, and even the inequalities allegedly certified cannot be reconstructed.
3. **[MAJOR]** The global bound \(M_8=10^{12}\) is unsupported on \(0\le x\le1\). The draft's own \(C_{n,8}\) argument handles \(x\ge1\), but no rigorous compact-interval calculation is provided.
4. **[MAJOR]** Replacing \(1/1209600\) by \(17/10321920\) multiplies the remainder allowance by \(255/128\). The worst advertised raw bound is about \(0.0440074\), yet no corrected rerun or post-correction minimum slack is shown.
5. **[MAJOR]** \(E_{n,8}\) is never fully defined by an Euler–Maclaurin identity, so a checker cannot verify endpoint signs or normalization. The \(f(x)=x^8\) polynomial oracle must be added.
6. **[MAJOR]** “Zero failed cells,” \(\Delta=1/128\) as an executed mesh, and “exact arithmetic” are FABRICATED-until-sourced; the verification recipe states desired outputs rather than reporting obtained outputs.
7. **[MINOR]** The unqualified assertion \(A>0\) is false at \(m=1\); it must be scoped to \(m\ge2\).