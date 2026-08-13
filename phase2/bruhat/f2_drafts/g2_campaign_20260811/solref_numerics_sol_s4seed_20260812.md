# numerics referee (gpt-5.6-sol, effort=max) — sol_s4seed_20260812.md — 2026-08-12 19:51

> Cross-model referee report (Sol on the reviewed draft). Numeric checks are
> DERIVED, not executed — script them before trusting.

## Numerical referee report

### Executive finding

I independently reconstructed the displayed scalar chain. Interpreting every decimal as an exact terminating rational, I find:

- No displayed scalar inequality in the \(m\ge700\) argument is numerically false.
- The final bounds recompute to approximately
  \[
  0.137179<\sigma^2(r(k)-1)<1.87789,
  \]
  so the claimed \(0.88\)-seed follows on the stated \(m\ge700\) range.
- One verification value is misstated: at \(\lambda=0.89\),
  \[
  \lambda^2R_4(e^{-\lambda})\approx12.0304117,
  \]
  which rounds to \(12.0304\), not \(12.0305\).
- The claimed closure for the operative range \(m\ge561\) does **not** follow from this draft. The proof covers only \(m\ge700\). The cited M3 result is recorded in the campaign ledger as an SL4′-X-free grid-rung replacement, not as a discharge of the bootstrap seed on \(561\le m\le699\). That interface is presently unsupported and appears contrary to the governing ledger.
- The numerical recipe checks envelope constants only. It contains no actual computation of a mean-matched Mahonian ratio, no off-grid characteristic-function attack, and no archived directed-interval output.

Thus the \(m\ge700\) scalar arithmetic is promising, but the submitted “no seed input remains for \(m\ge561\)” conclusion does not survive.

---

# 1. Algebraic checks

## 1.1 The \(D,C,B\) identity

With
\[
p_{-1}=p_0-C+B,\qquad p_1=p_0-C-B,
\]
one gets exactly
\[
p_{-1}p_1=(p_0-C)^2-B^2,
\]
hence
\[
D=p_0^2-p_{-1}p_1=2p_0C-C^2+B^2.
\]
This passes.

## 1.2 Fourier bound for \(D\)

Using
\[
p_\ell=\frac1{2\pi}\int_{-\pi}^{\pi}\phi(t)e^{-i\ell t}\,dt,
\]
one obtains
\[
D=\frac1{4\pi^2}\iint \phi(t)\phi(s)\bigl(1-\cos(t-s)\bigr)\,dt\,ds.
\]
Since \(|\phi|\) is even,
\[
\begin{aligned}
|D|
&\le \frac1{8\pi^2}\iint |\phi(t)||\phi(s)|(t-s)^2\,dt\,ds\\
&=\frac{I_0I_2}{4\pi^2},
\end{aligned}
\]
because the mixed first-moment term vanishes. This normalization passes.

---

# 2. Variance-scale checks

Write
\[
G(y)=\frac{y^2e^{-y}}{(1-e^{-y})^2}.
\]
The two “established” facts can in fact be checked directly:

\[
\frac{G'(y)}{G(y)}=\frac2y-\coth(y/2)<0
\]
because \(\tanh(y/2)<y/2\), and
\[
\begin{aligned}
G(y)&=y^2\sum_{n\ge1}ne^{-ny},\\
\int_0^\infty G(y)\,dy
 &=\sum_{n\ge1}n\frac{2}{n^3}
 =2\zeta(2)=\frac{\pi^2}{3}.
\end{aligned}
\]

Thus
\[
\lambda^2\sigma^2
\ge m h(\lambda)-\frac{\pi^2}{3\lambda},
\qquad
h(\lambda)=\left(\frac{\lambda}{2\sinh(\lambda/2)}\right)^2.
\]

The two branch constants are:

\[
1-\frac{0.1^2}{12}-\frac{\pi^2}{12}
=0.1766996332\ldots>0.176,
\]
and
\[
1-\frac{0.89^2}{12}-\frac{\pi^2}{210}
=0.8869935505\ldots>0.886.
\]

Consequently the selected common constant \(c_H=22/125\) is safe.

Exact derived constants:
\[
H_{\min}^2=\frac{22}{125}\,700=\frac{616}{5}=123.2,
\]
\[
S_*=\frac{616/5}{(89/100)^2}
=\frac{1232000}{7921}
=155.53591718\ldots,
\]
\[
\delta_*=\frac1{123.2}=\frac5{616}
=0.00811688311688\ldots,
\]
\[
\sqrt{H_{\min}^2}=11.0995495404\ldots.
\]

All pass.

The auxiliary inequality used later,
\[
h(\lambda)\le1-\frac{\lambda^2}{24},
\]
is true on this range, but the draft should prove it. For example, with \(x=\lambda/2\),
\[
\frac{\sinh x}{x}\ge1+\frac{x^2}{6}
\]
and a short rational comparison gives
\[
\left(\frac{x}{\sinh x}\right)^2\le1-\frac{x^2}{6}
=1-\frac{\lambda^2}{24}
\]
for \(x\le0.445\).

---

# 3. Moment constants

At \(\lambda=0.89\), let \(q=e^{-0.89}\). Direct evaluation gives
\[
q=0.4106557527\ldots.
\]

Then
\[
\lambda R_3(q)
=\lambda\frac{1+4q+q^2}{1-q^2}
=3.0095468\ldots<3.05.
\]

The analytic upper bound used in the proof is actually
\[
3+\frac{7(0.89)^4}{360}
=3.0121998802\ldots<3.05.
\]

For the fourth moment,
\[
\lambda^2R_4(q)
=\lambda^2\frac{1+10q+q^2}{(1-q)^2}
=12.0304117\ldots<12.5.
\]

Thus the recipe’s `≈ 12.0305` should be corrected to `≈ 12.0304`.

The proof-level upper bound is
\[
12+\frac{0.89^2}{2}=12.39605<12.5.
\]

The unproved continuum inequality
\[
\operatorname{csch}y
\le \frac1y-\frac y6+\frac{7y^3}{360}
\]
can be certified without a grid by checking
\[
\left(1-\frac{y^2}{6}+\frac{7y^4}{360}\right)\sinh y-y\ge0.
\]
Its power series starts at
\[
\frac{31}{15120}y^7
\]
and all subsequent coefficients are nonnegative. The draft should include this reduction rather than call all checks fixed evaluations.

---

# 4. Characteristic-function constants

The local constants simplify exactly to
\[
\alpha
=\frac12-\frac{225}{48(616/5)}
=\frac{4553}{9856}
=0.4619521104\ldots,
\]
and
\[
\beta=\frac{71}{192}
=0.3697916667\ldots.
\]

The central integral bounds recompute as
\[
J_0
=\sqrt{\frac{\pi}{\alpha}}
+\frac{e^{-9\beta}}{3\beta}
=2.64014\ldots<2.641,
\]
and
\[
J_2
=\frac{\sqrt\pi}{2\alpha^{3/2}}
+e^{-9\beta}
 \left(\frac3\beta+\frac1{6\beta^2}\right)
=3.15723\ldots<3.160.
\]

## 4.1 Selected-factor constants

\[
C_J=\coth(1.25)=1.1788509797\ldots<1.179.
\]

With
\[
\rho_M=\frac{C_J}{\sqrt{1+0.92^2(0.71)}},
\qquad
\rho_F=\frac{C_J}{\sqrt{1+0.92^2}},
\]
one gets approximately
\[
\rho_M=0.93169\ldots,
\qquad
-\frac38\log\rho_M=0.02653\ldots>0.0264,
\]
and
\[
\rho_F=0.86755\ldots,
\qquad
-\frac38\log\rho_F=0.0532\ldots>0.052.
\]

The integer count should be checked as
\[
N(m,\lambda)
=m-\left\lceil\frac{5}{2\lambda}\right\rceil+1
\ge m-\frac{5}{2\lambda}
\ge\frac{3m}{8}.
\]
This remains safe at discontinuities where \(5/(2\lambda)\) is an integer.

## 4.2 Quartic transition corner

For
\[
f(x)=-\frac{x^2}{2}+\frac{25x^4}{48},
\]
the only interior stationary point on the relevant interval is
\[
x=\sqrt{\frac{12}{25}},
\]
where \(f(x)=-0.12\). The maximum on
\([1/2,\sqrt{0.71}]\) occurs at the two endpoints, where
\[
f(1/2)=f(\sqrt{0.71})=-\frac{71}{768}.
\]
Then
\[
\frac{71}{768}\frac{22}{125}
=\frac{781}{48000}
>\frac{13}{800}.
\]
This off-grid stationary-point check passes.

## 4.3 Tail evaluations at the worst \(m=700\)

The middle-region bounds are
\[
\sqrt{700}\,e^{-(13/800)700}
=0.0003037\ldots<0.00031,
\]
\[
700^{3/2}e^{-(13/800)700}
=0.2126\ldots<0.213.
\]

A valid far-region \(I_0\) majorant is
\[
\frac{\pi}{2}700^{3/2}e^{-0.052(700)}
\approx4.5\times10^{-12}<10^{-8}.
\]

The recipe’s far \(I_2\) majorant is
\[
\frac{\pi^3}{32}700^{9/2}e^{-0.052(700)}
\approx9.57\times10^{-4}<0.001.
\]

All four functions decrease for \(m\ge700\), because for
\(m^a e^{-cm}\),
\[
\frac{d}{dm}\log(m^ae^{-cm})=\frac am-c<0
\]
at \(m=700\) for all \((a,c)\) used here.

Thus
\[
U_0=2.642,\qquad U_2=3.374
\]
are numerically safe, and
\[
K_D=\frac{2.642\cdot3.374}{4\pi^2}
=0.2257970\ldots<0.226.
\]

---

# 5. Point-mass constants

The modulus-loss constant simplifies exactly:
\[
\varepsilon
=\frac{\delta_*}{4(1-\delta_*(5/2)^2)}
=\frac5{2339}
=0.0021376657\ldots<0.00214.
\]

The phase constant is
\[
\gamma
=\frac{6.10}{
6\sqrt{123.2}\left(1-\frac12\delta_*(5/2)^2\right)}
=0.0939791\ldots<0.094.
\]

Hence
\[
\gamma(5/2)^3=1.46842\ldots<1.469<\frac\pi2.
\]

There is a proof-writing issue in (SOL.5.3): near \(z=5/2\),
\(\gamma^2z^6/2>1\), so one cannot blindly multiply lower bounds when
\(1-\gamma^2z^6/2\) is negative. The inequality is repairable:

- where \(1-\gamma^2z^6/2\ge0\), multiply the nonnegative lower bounds;
- where it is negative, use \(\Re\phi\ge0\), which follows from
  \(|\arg\phi|<\pi/2\).

That case split must be stated.

## 5.1 Central \(p_0\) integral

The exact Gaussian central integral is
\[
\sqrt{2\pi}\,\operatorname{erf}(2.5/\sqrt2)
=2.4754976\ldots.
\]

The elementary lower bound is
\[
\sqrt{2\pi}-\frac{2e^{-25/8}}{5/2}
=2.4714787\ldots.
\]

Using the draft’s conservative constants \(0.00214\) and \(0.094\),
\[
\begin{aligned}
L_{p,{\rm cent}}
={}&\sqrt{2\pi}-\frac{2e^{-25/8}}{5/2}\\
&-0.00214\cdot3\sqrt{2\pi}
-\frac{0.094^2}{2}\cdot15\sqrt{2\pi}\\
={}&2.28927\ldots>2.2891.
\end{aligned}
\]

The local complement satisfies
\[
e^{-6.25\alpha}
+\frac{e^{-9\beta}}{3\beta}
=0.08806\ldots<0.0882.
\]

Using only the displayed rounded inequalities gives
\[
2.2891-0.0882-0.00032=2.20058>2.2005.
\]
This is a thin absolute margin of only \(8\times10^{-5}\); directed
rounding is mandatory.

Thus
\[
p_0>\frac{2.2005}{2\pi\sigma}
= \frac{0.35022\ldots}{\sigma},
\]
so \(0.349/\sigma\) is safe. The upper bound is
\[
\frac{2.642}{2\pi\sigma}
=\frac{0.42049\ldots}{\sigma}
<\frac{0.421}{\sigma}.
\]

---

# 6. The \(C\)-integral

The exact truncated Gaussian moments are approximately
\[
\begin{aligned}
M_2&=1.8512348937,\\
M_4&=3.3883401493,\\
M_6&=8.2802426194,\\
M_8&=23.3158658273.
\end{aligned}
\]
Thus all four coarse inequalities in the draft pass.

Using the exact \(M_{2r}\) but the conservative constants
\(0.00214,0.094\),
\[
\begin{aligned}
Q_{\rm cent}
={}&\frac{M_2}{2}
-\frac{0.00214M_6}{2}
-\frac{0.094^2M_8}{4}
-\frac{M_4}{24S_*}\\
={}&0.86435\ldots>0.864.
\end{aligned}
\]

For
\[
F_\alpha(z)=
\frac{\sqrt\pi\,\operatorname{erf}(\sqrt\alpha z)}
{4\alpha^{3/2}}
-\frac{ze^{-\alpha z^2}}{2\alpha},
\]
direct evaluation gives
\[
2(F_\alpha(3)-F_\alpha(2))
\approx0.7235<0.725.
\]

The beta-tail majorant is
\[
e^{-9\beta}
\left(\frac3\beta+\frac1{6\beta^2}\right)
=0.33463\ldots<0.335.
\]

Therefore the displayed coarse chain gives
\[
2\pi\sigma^3C>0.864-\frac{1.274}{2}=0.227.
\]
Since
\[
\frac{0.227}{2\pi}=0.036128\ldots>0.0355,
\]
the lower constant is safe.

The upper constant is also safe:
\[
\frac{U_2}{4\pi}
=\frac{3.374}{4\pi}
=0.26849\ldots<0.269.
\]

---

# 7. Final arithmetic

The upper-bound parameter is
\[
A_*=\frac{0.226}{0.349^2}
=\frac{226000}{121801}
=1.8554856\ldots.
\]
Then
\[
\frac{A_*}{1-A_*/S_*}
=1.87789\ldots<1.879.
\]

For the lower bound,
\[
\begin{aligned}
d_{\rm lo}
&=2(0.349)(0.0355)-\frac{0.269^2}{S_*}\\
&=0.02431376\ldots>0.02431,
\end{aligned}
\]
and
\[
\frac{d_{\rm lo}}{0.421^2}
=0.137179\ldots>0.137.
\]

The scalar conclusion is therefore
\[
0.137179\ldots<X<1.87789\ldots,
\]
which implies
\[
|X-1|<0.87789\ldots<0.879<0.88.
\]

The draft’s scalar endpoint \(1.879\) is safe but not sharp.

---

# 8. Reproducible scalar script

The following is the minimum non-interval prototype a human should port
to Arb/python-flint for directed rounding:

```python
from mpmath import mp
mp.dps = 100

Q = lambda a, b: mp.mpf(a) / mp.mpf(b)

lam = Q(89, 100)
q = mp.exp(-lam)
m = 700

R3 = (1 + 4*q + q*q) / (1 - q*q)
R4 = (1 + 10*q + q*q) / (1 - q)**2

H2 = Q(616, 5)
S = Q(1232000, 7921)
delta = Q(5, 616)
alpha = Q(4553, 9856)
beta = Q(71, 192)

J0 = mp.sqrt(mp.pi/alpha) + mp.exp(-9*beta)/(3*beta)
J2 = (
    mp.sqrt(mp.pi)/(2*alpha**mp.mpf("1.5"))
    + mp.exp(-9*beta)
      * (3/beta + 1/(6*beta**2))
)

CJ = mp.coth(Q(5, 4))
rhoM = CJ / mp.sqrt(1 + Q(92,100)**2 * Q(71,100))
rhoF = CJ / mp.sqrt(1 + Q(92,100)**2)

mid0 = mp.sqrt(m) * mp.exp(-Q(13,800)*m)
mid2 = m**mp.mpf("1.5") * mp.exp(-Q(13,800)*m)
far0 = mp.pi/2 * m**mp.mpf("1.5") * mp.exp(-Q(52,1000)*m)
far2 = mp.pi**3/32 * m**mp.mpf("4.5") * mp.exp(-Q(52,1000)*m)

eps = delta / (4*(1-delta*Q(5,2)**2))
gam = Q(610,100) / (
    6*mp.sqrt(H2)*(1-delta*Q(5,2)**2/2)
)

Lp = (
    mp.sqrt(2*mp.pi)
    - 2*mp.exp(-Q(25,8))/Q(5,2)
    - Q(214,100000)*3*mp.sqrt(2*mp.pi)
    - Q(94,1000)**2/2 * 15*mp.sqrt(2*mp.pi)
)

M0 = mp.sqrt(2*mp.pi)*mp.erf(mp.sqrt(2))
M2 = M0 - 4*mp.exp(-2)
M4 = 3*M2 - 16*mp.exp(-2)
M6 = 5*M4 - 64*mp.exp(-2)
M8 = 7*M6 - 256*mp.exp(-2)

Qc = (
    M2/2
    - Q(214,100000)*M6/2
    - Q(94,1000)**2*M8/4
    - M4/(24*S)
)

def Fa(z):
    return (
        mp.sqrt(mp.pi)*mp.erf(mp.sqrt(alpha)*z)
        /(4*alpha**mp.mpf("1.5"))
        - z*mp.exp(-alpha*z*z)/(2*alpha)
    )

outer23 = 2*(Fa(3)-Fa(2))
beta_tail = mp.exp(-9*beta)*(3/beta + 1/(6*beta**2))

U0 = Q(2642,1000)
U2 = Q(3374,1000)
KD = U0*U2/(4*mp.pi**2)

A = Q(226,1000) / Q(349,1000)**2
upper = A/(1-A/S)

dlo = (
    2*Q(349,1000)*Q(355,10000)
    - Q(269,1000)**2/S
)
lower = dlo/Q(421,1000)**2

assert lam*R3 < Q(305,100)
assert lam**2*R4 < Q(25,2)
assert J0 < Q(2641,1000)
assert J2 < Q(3160,1000)
assert -Q(3,8)*mp.log(rhoM) > Q(13,800)
assert -Q(3,8)*mp.log(rhoF) > Q(52,1000)
assert mid0 < Q(31,100000)
assert mid2 < Q(213,1000)
assert far0 < Q(1,10**8)
assert far2 < Q(1,1000)
assert eps < Q(214,100000)
assert gam < Q(94,1000)
assert Lp > mp.mpf("2.2891")
assert Qc > Q(864,1000)
assert outer23 < Q(725,1000)
assert beta_tail < Q(335,1000)
assert KD < Q(226,1000)
assert upper < Q(1879,1000)
assert lower > Q(137,1000)
```

This is not itself a certificate: `mpmath` does not provide directed
rounding. The archived version must use ball/interval arithmetic.

---

# 9. Required off-grid actual-law probes

The draft tests no actual \(r(k)\). At minimum, an adversarial harness
must perform the following.

For each \(m\), define
\[
\mu_m(\lambda)
=\frac{m}{e^\lambda-1}
-\sum_{j=1}^m\frac{j}{e^{j\lambda}-1}.
\]
Since
\[
\mu_m'(\lambda)=-\sigma^2(\lambda)<0,
\]
solve \(\mu_m(\lambda)=k\) by directed bisection.

Compute exact Mahonian coefficients using
\[
a_j(n)=a_j(n-1)+a_{j-1}(n)
-\mathbf 1_{n\ge j}a_{j-1}(n-j),
\]
and then
\[
r_m(k)-1
=\frac{a_m(k)^2-a_m(k-1)a_m(k+1)}
       {a_m(k-1)a_m(k+1)}.
\]
Multiply this exact rational by an interval evaluation of
\(\sigma^2(\lambda)\).

Required probes:

1. \(m=700\), with actual integer-mean tilts immediately above
   \(\lambda=4/700\).
2. Actual integer-mean tilts immediately below and above \(\lambda=0.1\).
3. The largest integer-mean tilt not exceeding \(0.89\).
4. \(m=701,703,704\), to attack changes in
   \(\lceil2.5/\lambda\rceil\).
5. \(m=1000\) and a large \(m\), with \(m\lambda\) just above \(4\).
6. \(m=561\) and \(m=699\), because these are precisely the unsupported
   claimed-bypass endpoints.
7. Characteristic-function probes at
   \[
   x=\frac12,\quad \sqrt{12/25},\quad\sqrt{0.71},\quad1,
   \]
   and at \(t=\lambda/2,\lambda,\pi\), with
   \(j\lambda=2.5\pm2^{-40}\).

No such output is supplied. Until it exists, the draft has an analytic
constant check, not a numerical validation of the actual tilted law.

---

# 10. FABRICATED-until-sourced register

1. **`0.89412` bootstrap basin:** no formula, theorem number, archived
   output, or directed interval is supplied. The campaign ledger only
   records rounded basins \(0.902/0.894\).  
   **FABRICATED-until-sourced.**

2. **“M3 closure on \(561\le m\le699\) bypasses the seed”:** the
   governing ledger describes M3 as removing SL4′-X/the \(w\)-grid on
   that rung, not as proving or bypassing S4.  
   **FABRICATED-until-sourced and apparently interface-incompatible.**

3. **“128 bits is ample”:** no implementation, conditioning analysis,
   or interval transcript is supplied. This matters because the rounded
   \(p_0\) chain has only about \(8\times10^{-5}\) spare and
   \(d_{\rm lo}>0.02431\) has spare only about \(3.8\times10^{-6}\).  
   **FABRICATED-until-sourced.**

VERDICT: MAJOR_ISSUES

1. The argument proves at most the seed statement for \(m\ge700\); it does not establish the claimed operative closure for \(561\le m\le699\). The cited M3 result does not have the dependency asserted here.
2. The bootstrap-basin constant \(0.89412\) has no derivation or citable certificate.
3. No archived directed-interval execution is supplied, despite several thin rounded margins; the “128 bits” assertion is unsupported.
4. The verification recipe is not solely a list of fixed evaluations: several continuum inequalities and monotonic reductions require proofs or interval certificates.
5. No actual mean-matched Mahonian ratio or off-grid characteristic-function probe is computed.
6. Equation (SOL.5.3) needs an explicit sign case split; its current lower-bound multiplication is not justified near \(z=5/2\).
7. Correct the verification value \(\lambda^2R_4(e^{-0.89})\approx12.0304117\), which rounds to \(12.0304\), not \(12.0305\).