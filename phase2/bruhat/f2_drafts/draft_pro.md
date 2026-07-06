# F2 blind draft — gpt-5.5-pro, high effort

Below is a blind draft. I isolate the genuinely unfinished parts with explicit `GAP:` markers, as requested.

---

# Draft proof of Theorem F2

Let  
\[
p_m(k):=\frac{I_m(k)}{m!}=\mathbb P(S_m=k),\qquad 
S_m=\sum_{j=1}^m U_j,\quad U_j\sim{\rm Unif}\{0,\dots,j-1\},
\]
independently. Put
\[
N=\frac{m(m-1)}2,\qquad \mu=\frac N2,\qquad 
\sigma^2=\sigma_m^2=\frac{m(m-1)(2m+5)}{72},
\]
and
\[
D_m(k):=\log r_m(k)=2\log p_m(k)-\log p_m(k-1)-\log p_m(k+1).
\]

We use without reproving: log-concavity of Mahonian numbers by Bóna, Electron. J. Combin.; equivalently via Hoggar’s convolution theorem / Kook’s product-closure route. We also use Petrov’s local Edgeworth expansions for triangular arrays of lattice sums, and we follow the adjacent-coefficient transfer already used by Canfield–Janson–Zeilberger, Adv. Appl. Math. 2011, Theorem 4.6 / eq. (4.11), for the central Gaussian-binomial case.

---

## Lemma 1. Symmetry and log-concavity.

**Dependencies:** Bóna; alternatively Hoggar–Kook.

The sequence \(I_m(k)\) is symmetric:
\[
I_m(k)=I_m(N-k),
\]
and log-concave:
\[
I_m(k)^2\ge I_m(k-1)I_m(k+1).
\]
Hence \(D_m(k)\ge0\), and \(r_m(k)\ge1\).

**Proof.** Symmetry follows from
\[
q^N [m]_{q^{-1}}! = [m]_q!.
\]
Log-concavity is the cited theorem of Bóna, or follows by convolving the log-concave uniform factors \((1,\dots,1)\), using Hoggar’s product-closure theorem. ∎

**NUMERIC CHECK:** Run `python3 mahonian.py --mmax 40`. Expected: all printed ratios satisfy \(r_m(k)\ge1\); the table’s `central?` column is `YES` throughout.

---

## Lemma 2. Exact characteristic function and cumulants.

**Dependencies:** none.

For the centered variable \(X_m=S_m-\mu\),
\[
\mathbb E e^{zX_m}
=\prod_{j=1}^m \frac{\sinh(jz/2)}{j\sinh(z/2)}.
\]
Therefore the cumulant generating function is
\[
K_m(z):=\log \mathbb E e^{zX_m}
=\sum_{j=1}^m \log \frac{\sinh(jz/2)}{j\sinh(z/2)}.
\]
In particular,
\[
\kappa_2=\sigma^2,
\]
and
\[
\kappa_4
=-\frac1{120}\sum_{j=1}^m (j^4-1)
=-\frac{m(6m^4+15m^3+10m^2-31)}{3600}.
\]
Moreover, for every fixed \(r\ge1\),
\[
\kappa_{2r}=O_r(m^{2r+1}).
\]

**Proof.** For one summand,
\[
\mathbb E e^{z(U_j-(j-1)/2)}
=\frac1j\sum_{a=0}^{j-1}e^{z(a-(j-1)/2)}
=\frac{\sinh(jz/2)}{j\sinh(z/2)}.
\]
Multiplying over \(j\) gives the formula. The cumulants follow from
\[
\log\frac{\sinh w}{w}
=\frac{w^2}{6}-\frac{w^4}{180}+\frac{w^6}{2835}+O(w^8).
\]
Thus the fourth cumulant contribution of the \(j\)-th factor is
\[
-\frac{j^4-1}{120}.
\]
Summing gives the displayed formula. ∎

**NUMERIC CHECK:** For \(m=5\), the formula gives \(\sigma^2=25/6\); for \(m=6\), \(\sigma^2=85/12\). These are the variances used in the `varfit` column of `mahonian.py --mmax 40`.

---

## Lemma 3. Central local Edgeworth expansion.

**Dependencies:** Lemma 2; Petrov local Edgeworth expansion for lattice triangular arrays.

Fix \(C>0\). Uniformly for integers \(k\) with
\[
x:=k-\mu,\qquad |x|\le C\sigma,\qquad y:=x/\sigma,
\]
one has
\[
p_m(k)
=\frac{e^{-y^2/2}}{\sqrt{2\pi}\sigma}
\left[
1+\frac{\kappa_4}{24\sigma^4}H_4(y)
+O_C(m^{-2})
\right],
\tag{3.1}
\]
where
\[
H_4(y)=y^4-6y^2+3.
\]
Moreover the adjacent log-concavity ratio satisfies
\[
D_m(k)
=\sigma^{-2}
+\frac{\kappa_4}{2\sigma^6}(1-y^2)
+O_C(m^{-5}).
\tag{3.2}
\]

**Proof.** Fourier inversion gives
\[
p_m(k)
=\frac1{2\pi}\int_{-\pi}^{\pi}
e^{-itx}
\prod_{j=1}^m
\frac{\sin(jt/2)}{j\sin(t/2)}
\,dt .
\]
After the change \(u=\sigma t\), Lemma 2 gives
\[
K_m(iu/\sigma)
=-\frac{u^2}{2}
+\frac{\kappa_4}{24\sigma^4}u^4
+O_C(m^{-2}(1+|u|^6))
\]
on the central Fourier range. The complementary range is exponentially small by the standard Petrov bound for lattice sums with maximal summand \(O(m)=o(\sigma)\). Integrating termwise yields (3.1).

For (3.2), apply the same Fourier expansion simultaneously to the three adjacent probabilities \(p_m(k-1),p_m(k),p_m(k+1)\). Equivalently, take the discrete second difference of the logarithm of (3.1), using one additional Petrov term to control the differentiated remainder. The Gaussian part contributes exactly \(\sigma^{-2}\). The \(H_4\)-term contributes
\[
\frac{\kappa_4}{24\sigma^4}
\left(2H_4(y)-H_4(y-\sigma^{-1})-H_4(y+\sigma^{-1})\right)
=
\frac{\kappa_4}{2\sigma^6}(1-y^2)+O(m^{-7}).
\]
The remaining Petrov terms contribute \(O_C(m^{-5})\). ∎

**NUMERIC CHECK:** Augment `mahonian.py` to compute  
\[
E_m(C):=\max_{|k-\mu|\le C\sigma}
\left|
D_m(k)-\sigma^{-2}-\frac{\kappa_4}{2\sigma^6}(1-y^2)
\right|.
\]
For \(C=2\), expected outcome: \(E_m(2)/\sigma^{-2}\to0\) visibly as \(m\) increases; \(m^5E_m(2)\) remains bounded for the tested range.

---

## Lemma 4. Central ratio asymptotics.

**Dependencies:** Lemma 3; CJZ adjacent-coefficient transfer.

Let
\[
k_c:=\lfloor \mu\rfloor .
\]
Then
\[
D_m(k_c)
=
\sigma^{-2}
+\frac{\kappa_4}{2\sigma^6}
+O(m^{-5})
=
\sigma^{-2}+O(m^{-4}),
\tag{4.1}
\]
and therefore
\[
r_m(k_c)
=
1+\sigma^{-2}+O(m^{-4}).
\tag{4.2}
\]
Equivalently,
\[
\sigma^2\bigl(r_m(k_c)-1\bigr)
=
1+\frac{\kappa_4}{2\sigma^4}+O(m^{-2})
=
1-\frac{27}{25m}+O(m^{-2}).
\tag{4.3}
\]

**Proof.** In Lemma 3, at \(k=k_c\) we have \(y=0\) if \(N\) is even and \(y=-1/(2\sigma)\) if \(N\) is odd. Thus \(1-y^2=1+O(\sigma^{-2})\), and (3.2) gives (4.1). Since \(D_m(k_c)=O(m^{-3})\),
\[
r_m(k_c)=e^{D_m(k_c)}
=1+D_m(k_c)+O(D_m(k_c)^2),
\]
and \(D_m(k_c)^2=O(m^{-6})\), giving (4.2). Multiplying by \(\sigma^2\) yields (4.3). This is the q-factorial analogue of the CJZ Theorem 4.6 / eq. (4.11) central transfer. ∎

**NUMERIC CHECK:** Run `python3 mahonian.py --mmax 40`. Expected: the column `rc-1` agrees with \(1/\sigma^2\) up to relative error \(O(1/m)\), and the column `varfit = \sigma^2(r_c-1)` tends upward toward \(1\), reaching about \(0.9734\) at \(m=40\).

---

## Lemma 5. Tilted variance is maximized at the center.

**Dependencies:** Lemma 2.

For real \(t\), let
\[
B_m(t):=K_m''(t).
\]
Then
\[
0<B_m(t)\le B_m(0)=\sigma^2,
\]
with equality only at \(t=0\).

**Proof.** For the \(j\)-th centered uniform factor,
\[
v_j(t):=\frac{d^2}{dt^2}
\log\frac{\sinh(jt/2)}{j\sinh(t/2)}
=
\frac14\csch^2(t/2)-\frac{j^2}{4}\csch^2(jt/2).
\]
Thus \(B_m(t)=\sum_j v_j(t)\). Each \(v_j\) is even, so it suffices to show \(v_j'(t)<0\) for \(t>0\), \(j\ge2\). Put \(s=t/2\). Then
\[
v_j'(t)
=
\frac14\left[
j^3\coth(js)\csch^2(js)
-\coth(s)\csch^2(s)
\right].
\]
Let
\[
h(u):=u^3\coth(u)\csch^2(u).
\]
Then
\[
\frac{h'(u)}{h(u)}
=
\frac3u+\tanh u-3\coth u.
\]
The inequality \(h'(u)<0\) is equivalent to
\[
3(\coth u-1/u)>\tanh u.
\]
Indeed, after clearing denominators this becomes positivity of
\[
F(u):=3u+2u\sinh^2u-3\sinh u\cosh u.
\]
But \(F(0)=0\) and
\[
F'(u)=4\sinh u\,(u\cosh u-\sinh u)>0
\]
because \(\tanh u<u\) for \(u>0\). Hence \(h\) decreases, so
\[
j^3\coth(js)\csch^2(js)
<
\coth(s)\csch^2(s),
\]
and \(v_j'(t)<0\). Therefore every \(v_j(t)\) is maximized at \(0\), and so is \(B_m(t)\). ∎

**NUMERIC CHECK:** Add to `mahonian.py` a routine computing  
\[
B_m(t)=\sum_{j=1}^m\left(\frac14\csch^2(t/2)-\frac{j^2}{4}\csch^2(jt/2)\right).
\]
On a grid \(t\in[0,10/m]\), expected: the maximum is attained at \(t=0\), and \(B_m(t)/\sigma^2<1\) for \(t>0\).

---

## Lemma 6. Global curvature lower bound.

**Dependencies:** Lemmas 2 and 5; Petrov saddlepoint expansion.

There exists \(\varepsilon_m\to0\) such that, uniformly for all \(1\le k\le N-1\),
\[
D_m(k)\ge (1-\varepsilon_m)\sigma^{-2}.
\tag{6.1}
\]

**Draft proof.** Let \(x=k-\mu\). For \(x\in(-N/2,N/2)\), let \(t_x\) be the real saddlepoint defined by
\[
K_m'(t_x)=x.
\]
Define the Legendre saddle exponent
\[
\Phi_m(x):=K_m(t_x)-t_xx.
\]
Then
\[
\Phi_m''(x)=-\frac1{B_m(t_x)}.
\]
Hence
\[
2\Phi_m(x)-\Phi_m(x-1)-\Phi_m(x+1)
=
\int_{-1}^{1}\frac{1-|u|}{B_m(t_{x+u})}\,du.
\]
By Lemma 5,
\[
B_m(t_{x+u})\le \sigma^2,
\]
so the main saddle exponent contributes at least \(\sigma^{-2}\).

A uniform lattice saddlepoint approximation should give
\[
\log p_m(k)
=
\Phi_m(x)-\frac12\log(2\pi B_m(t_x))+E_m(x),
\tag{6.2}
\]
with
\[
2E_m(x)-E_m(x-1)-E_m(x+1)=o(\sigma^{-2})
\]
uniformly in \(x\), and similarly the discrete second difference of
\(-\frac12\log B_m(t_x)\) should be \(o(\sigma^{-2})\). Combining these estimates with the previous displayed inequality yields (6.1).

**GAP 6.1:** The pointwise saddlepoint approximation (6.2) is standard, but this draft does **not** yet contain a fully uniform bound on the adjacent second difference of the saddlepoint error \(E_m\), especially through the transition to the extreme tails. This is the main global analytic gap.

**NUMERIC CHECK:** Run `python3 mahonian.py --mmax 40`. Expected: the minimum of \(D_m(k)=\log r_m(k)\) is always attained in the central positions listed by the table; no tail value comes close to beating the central value. Also compute  
\[
\min_k \sigma^2 D_m(k);
\]
expected: values approach \(1\) from below.

---

## Lemma 7. Centrality of the minimum.

**Dependencies:** Lemmas 3, 4, 6.

For all sufficiently large \(m\), every minimizer of \(r_m(k)\) satisfies
\[
|k-\mu|\le1.
\tag{7.1}
\]
Together with finite verification, this proves Theorem F2(b).

**Draft proof.** By symmetry, it suffices to consider \(k\le\mu\). Lemma 4 gives the central value. Lemma 3 gives, in the Gaussian window,
\[
D_m(k)
=
\sigma^{-2}
+\frac{\kappa_4}{2\sigma^6}(1-y^2)
+O_C(m^{-5}).
\]
Since \(\kappa_4<0\), the displayed main term is minimized at \(y=0\), i.e. at the center.

For \(|y|\ge c>0\), the gain over the center is \(\gg_c m^{-4}\), which dominates the \(O_C(m^{-5})\) error. Thus no point with \(|k-\mu|\ge c\sigma\) inside the central window beats the center. Outside the central window, Lemma 6 plus the strict inequality \(B_m(t)<\sigma^2\) for \(t\neq0\) should give a still larger curvature.

The remaining microscopic range \(|k-\mu|=O(1)\) requires a higher-order local expansion. The expected expansion is
\[
D_m(k)-D_m(k_c)
=
A_m\bigl((k-\mu)^2-(k_c-\mu)^2\bigr)
+O(m^{-8}),
\tag{7.2}
\]
with
\[
A_m=-\frac{\kappa_4}{2\sigma^8}+O(m^{-8})>0.
\]
This would imply strict centrality for every \(k\) with \(|k-\mu|>1\).

**GAP 7.1:** This draft has not written the required high-order microscopic expansion (7.2) with an error \(o(m^{-7})\). The leading term is clear from Lemma 3, but proving centrality at distance \(1,2,\dots,O(1)\) needs Edgeworth terms beyond those displayed above.

**NUMERIC CHECK:** Run `python3 mahonian.py --mmax 40`. Expected exactly the supplied table: for \(m\ge5\), the minimum ratio equals the central ratio; for \(m=4\), the first minimizer is \(k=2\), still satisfying \(|k-N/2|\le1\). The `central?` column should be `YES` throughout.

---

# Proof of Theorem F2

## Part (a): asymptotic minimum ratio.

By Lemma 4,
\[
r_m\le r_m(k_c)
=
1+\sigma^{-2}+O(m^{-4}).
\]
By Lemma 6,
\[
\log r_m(k)\ge (1-\varepsilon_m)\sigma^{-2}
\]
for every \(k\). Since \(\sigma^{-2}=O(m^{-3})\),
\[
r_m(k)-1\ge (1-o(1))\sigma^{-2}.
\]
Therefore
\[
r_m-1=\sigma^{-2}(1+o(1)),
\]
equivalently
\[
r_m=1+\sigma_m^{-2}(1+o(1)).
\]
Since
\[
\sigma_m^2=\frac{m(m-1)(2m+5)}{72}
\sim \frac{m^3}{36},
\]
this is also
\[
r_m-1\sim \frac{36}{m^3}.
\]

**GAP STATUS:** Part (a) is complete modulo GAP 6.1.

---

## Part (b): central location.

Lemma 7 gives, for all sufficiently large \(m\),
\[
\operatorname*{argmin}_k r_m(k)\subseteq \{k:|k-\mu|\le1\}.
\]
The remaining finite range is checked exactly by `mahonian.py`.

Thus every minimizer is central in the required sense:
\[
|k-N/2|\le1.
\]

**GAP STATUS:** Part (b) is complete modulo GAP 7.1 and the finite exact verification beyond whatever explicit threshold comes from filling GAP 7.1.

---

## Part (c): explicit non-asymptotic constant.

The draft does not achieve a fully explicit all-\(m\) constant.

There is also an important correction forced by the supplied exact table: the suggested value \(c=7/8\) cannot hold for all \(m\ge5\). Indeed, for \(m=6\),
\[
\sigma_6^2=\frac{85}{12},
\]
and the central coefficients are
\[
I_6(6)=90,\qquad I_6(7)=I_6(8)=101.
\]
Hence
\[
r_6=\frac{101}{90},
\qquad
r_6-1=\frac{11}{90},
\]
and therefore
\[
\sigma_6^2(r_6-1)
=
\frac{85}{12}\cdot\frac{11}{90}
=
\frac{187}{216}
\approx0.8657407<\frac78.
\]
So any universal constant valid for all \(m\ge5\) must satisfy
\[
c\le \frac{187}{216}
\]
unless \(m=6\) is excluded.

A plausible corrected explicit target is, for example,
\[
r_m\ge 1+\frac{43}{50}\sigma_m^{-2}\qquad(m\ge5),
\]
which is consistent with the supplied table. To prove it, one needs explicit constants in Lemmas 6 and 7 plus a finite exact check up to the resulting threshold.

**GAP 8.1:** Explicit constants in the global saddlepoint error and the microscopic central comparison are not supplied here.

**NUMERIC CHECK:** Run `python3 mahonian.py --mmax 40`. Expected: the smallest displayed value of \(\sigma^2(r_m-1)\) for \(m\ge5\) occurs at \(m=6\), approximately \(0.8657\). Thus \(c=43/50=0.86\) is consistent through \(m=40\), while \(c=7/8\) fails at \(m=6\). ∎