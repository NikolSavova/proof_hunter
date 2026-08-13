# Bregman Problem 2, Part II attempt 2 — part2a (gpt-5.6-sol, effort=max, 2026-08-13 00:28)

> SINGLE-MODEL, UNREFEREED. Attacks the ghost-face obstruction isolated by
> attempt 1's Lemma SOL.6. part2a tries to CONSTRUCT it, part2b to EXCLUDE it.

# Status

\[
\boxed{\text{Alternative (B) holds.}}
\]

Under hypotheses (a) and (c), \(C^*=\nabla f(C)\) is convex; hypothesis (b) is unnecessary.

The missing observation is that a finite-height ghost minimizer cannot coexist with **existence** at all nearby tilts. If \(q\in\operatorname{bd}U^*\) is a ghost tied with the actual minimizer at \(x_0\), and \(n\) is an outward supporting normal to \(U^*\) at \(q\), then the perturbed tilt \(x_0+tn\) strictly prefers \(q\) to every point of \(C^*\). A recovery sequence approaches the ghost value, so the infimum is not attained. This contradicts right \(D\)-Chebyshevness.

I found no error in the cited parts of Attempt 1 needed below. There is, however, one important correction to the proposed box heuristic:

> **On a flat face of the box, the box-kernel tilt is not affine in the tangential coordinates.**

It remains strictly convex tangentially. Flatness only makes the normal linear functional constant on the face.

---

## Lemma SOL.1 — Dual formulation, relative closedness, and quantitative coercivity

**Hypotheses.** Let \(X=\mathbb R^n\). Let \(f\) be Legendre with
\[
\operatorname{dom}f=X.
\]
Let \(C\subset X\) be closed and nonempty. Put
\[
g:=f^*,\qquad \Omega:=U^*=\operatorname{int}\operatorname{dom}g,
\qquad S:=\nabla f(C),
\]
and
\[
h:=g+\iota_S.
\]

**Conclusions.**

1. \(\nabla f:X\to\Omega\) and \(\nabla g:\Omega\to X\) are mutually inverse homeomorphisms.
2. \(S\) is closed relative to \(\Omega\).
3. For \(y\in C\), \(p=\nabla f(y)\),
   \[
   D_f(x,y)=f(x)+g(p)-\langle x,p\rangle.
   \]
4. Thus \(C\) is right \(D\)-Chebyshev iff, for every \(x\in X\),
   \[
   \arg\min_{p\in S}\bigl(g(p)-\langle x,p\rangle\bigr)
   \]
   exists and is a singleton.
5. For every \(x\in X\), define
   \[
   A_x:=\max_{\|z\|=\|x\|+2}f(z)<+\infty.
   \]
   Then, for every \(p\neq0\),
   \[
   g(p)-\langle x,p\rangle\ge 2\|p\|-A_x.
   \tag{SOL.1.1}
   \]

**Proof.**

Items 1–4 are the standard Legendre duality calculation. For relative closedness, if
\[
p_k\in S,\qquad p_k\to p\in\Omega,
\]
then
\[
\nabla g(p_k)\in C,\qquad \nabla g(p_k)\to\nabla g(p).
\]
Since \(C\) is closed, \(\nabla g(p)\in C\), hence \(p\in S\).

For (SOL.1.1), choose
\[
z=(\|x\|+2)\frac p{\|p\|}.
\]
Then
\[
g(p)\ge \langle z,p\rangle-f(z)
\ge(\|x\|+2)\|p\|-A_x.
\]
Since \(\langle x,p\rangle\le\|x\|\|p\|\),
\[
g(p)-\langle x,p\rangle\ge2\|p\|-A_x.
\]
∎

---

## Lemma SOL.2 — Verification of the spherical arithmetic

**Hypotheses.** Let
\[
f_{\mathrm{sph}}(x)=\sqrt{1+\|x\|^2}.
\]

**Conclusions.**

1. \(f_{\mathrm{sph}}\) is Legendre and
   \[
   \operatorname{dom}f_{\mathrm{sph}}=X.
   \]
2.
   \[
   \nabla f_{\mathrm{sph}}(x)
   =\frac{x}{\sqrt{1+\|x\|^2}}.
   \]
3.
   \[
   f_{\mathrm{sph}}^*(p)=
   \begin{cases}
   -\sqrt{1-\|p\|^2},&\|p\|\le1,\\
   +\infty,&\|p\|>1.
   \end{cases}
   \]
4. For
   \[
   \phi_x(p):=-\sqrt{1-\|p\|^2}-\langle x,p\rangle,
   \]
   the minimizer over the closed unit ball is
   \[
   p_x^*=\frac{x}{\sqrt{1+\|x\|^2}},
   \]
   with value
   \[
   \phi_x(p_x^*)=-\sqrt{1+\|x\|^2}.
   \]
5. The minimum over the unit sphere is
   \[
   -\|x\|,
   \]
   and the exact interior-boundary gap is
   \[
   \sqrt{1+\|x\|^2}-\|x\|
   =\frac1{\sqrt{1+\|x\|^2}+\|x\|}>0.
   \tag{SOL.2.1}
   \]

**Proof.**

For \(\|p\|<1\), the stationary equation is
\[
\frac p{\sqrt{1-\|p\|^2}}=x,
\]
which gives
\[
p=p_x^*.
\]
At this point,
\[
\sqrt{1-\|p_x^*\|^2}
=\frac1{\sqrt{1+\|x\|^2}},
\]
and
\[
\langle x,p_x^*\rangle
=\frac{\|x\|^2}{\sqrt{1+\|x\|^2}}.
\]
Hence
\[
\phi_x(p_x^*)
=-\frac{1+\|x\|^2}{\sqrt{1+\|x\|^2}}
=-\sqrt{1+\|x\|^2}.
\]

On \(\|p\|=1\),
\[
\phi_x(p)=-\langle x,p\rangle,
\]
whose minimum is \(-\|x\|\). Formula (SOL.2.1) follows by rationalization. ∎

Thus the spherical computation in the question is correct.

---

## Lemma SOL.3 — Verification and correction for the box kernel

**Hypotheses.** Let
\[
f_{\Box}(x)=\sum_{j=1}^n\sqrt{1+x_j^2}.
\]

**Conclusions.**

1. \(f_{\Box}\) is Legendre and
   \[
   \operatorname{dom}f_{\Box}=X.
   \]
2.
   \[
   \nabla f_{\Box}(x)_j
   =\frac{x_j}{\sqrt{1+x_j^2}}.
   \]
3.
   \[
   f_{\Box}^*(p)=
   \begin{cases}
   -\displaystyle\sum_{j=1}^n\sqrt{1-p_j^2},
      &p\in[-1,1]^n,\\[1ex]
   +\infty,&p\notin[-1,1]^n.
   \end{cases}
   \]
4.
   \[
   U^*=(-1,1)^n.
   \]
5. On the face \(p_1=1\),
   \[
   \phi_x(p)
   =-x_1-\sum_{j=2}^n
     \left(\sqrt{1-p_j^2}+x_jp_j\right).
   \tag{SOL.3.1}
   \]
   In particular, the tilt is not affine in \(p_2,\dots,p_n\). Its tangential Hessian is
   \[
   \frac{\partial^2\phi_x}{\partial p_j^2}
   =(1-p_j^2)^{-3/2}>0,
   \qquad 2\le j\le n.
   \tag{SOL.3.2}
   \]

**Proof.**

Everything is coordinatewise. For
\[
a(t)=\sqrt{1+t^2},
\]
one has
\[
a^*(p)=
\begin{cases}
-\sqrt{1-p^2},&|p|\le1,\\
+\infty,&|p|>1.
\end{cases}
\]
Summation gives the stated conjugate.

On \(p_1=1\), the first square-root term vanishes, giving (SOL.3.1). Finally,
\[
\frac{d^2}{dp^2}\left(-\sqrt{1-p^2}\right)
=(1-p^2)^{-3/2}.
\]
∎

The flat face still supplies a common supporting normal \(e_1\). That normal, rather than tangential affine structure, is what matters below.

---

## Lemma SOL.4 — The lower-semicontinuous hull and localization of extra minimizers

**Hypotheses.** Assume the setting of SOL.1 and right \(D\)-Chebyshevness. Let
\[
\bar h(q)
:=\lim_{\varepsilon\downarrow0}
  \inf_{\|z-q\|<\varepsilon}h(z)
\]
be the lower-semicontinuous hull of \(h\). For \(x\in X\), denote the unique minimizer of
\[
h(p)-\langle x,p\rangle
\]
by \(p_x\), and its value by
\[
m_x:=h(p_x)-\langle x,p_x\rangle.
\]

**Conclusions.**

1. \(g\le\bar h\le h\).
2. \(p_x\) minimizes
   \[
   \bar h(p)-\langle x,p\rangle
   \]
   with the same value \(m_x\).
3. Any additional minimizer belongs to
   \[
   \operatorname{cl}S\setminus\Omega
   \subset\operatorname{bd}\Omega.
   \]
4. If \(\bar h(q)<+\infty\), there is a recovery sequence
   \[
   s_k\in S,\qquad s_k\to q,\qquad h(s_k)\to\bar h(q).
   \tag{SOL.4.1}
   \]

**Proof.**

Since \(g\) is lower semicontinuous and \(g\le h\), the maximal lower-semicontinuous minorant satisfies \(g\le\bar h\le h\).

The inequality
\[
h(p)-\langle x,p\rangle\ge m_x
\]
passes to lower limits, hence
\[
\bar h(p)-\langle x,p\rangle\ge m_x.
\]
At \(p_x\in S\),
\[
g(p_x)\le\bar h(p_x)\le h(p_x)=g(p_x),
\]
so equality holds.

If \(q\in\Omega\) and \(\bar h(q)<+\infty\), a recovery sequence lies eventually in \(S\), and relative closedness of \(S\) gives \(q\in S\). Consequently
\[
\bar h(q)=h(q)=g(q).
\]
If \(q\) were an additional minimizer, it would be a second minimizer of the original tilt over \(S\), contradicting uniqueness. Thus every additional minimizer is outside \(\Omega\). Recovery sequences show that it lies in \(\operatorname{cl}S\subset\operatorname{cl}\Omega\), hence on \(\operatorname{bd}\Omega\).

The sequential recovery statement follows directly from the displayed definition of \(\bar h\). ∎

---

## Lemma SOL.5 — Outward perturbation excludes every finite-height ghost

**Hypotheses.**

- \(\Omega\subset X\) is nonempty, open, and convex.
- \(S\subset\Omega\).
- \(h:X\to]-\infty,+\infty]\) is finite precisely on \(S\).
- Every linear tilt of \(h\) over \(S\) attains its infimum.
- For some \(x_0\in X\), \(p_0\in S\), and \(q\in\operatorname{bd}\Omega\),
  \[
  h(s)-\langle x_0,s\rangle\ge m
  \quad(s\in S),
  \tag{SOL.5.1}
  \]
  \[
  h(p_0)-\langle x_0,p_0\rangle=m,
  \tag{SOL.5.2}
  \]
  and
  \[
  \bar h(q)-\langle x_0,q\rangle=m.
  \tag{SOL.5.3}
  \]

**Conclusion.** These hypotheses are inconsistent. More precisely, for a suitable unit vector \(n\) and every \(t>0\),
\[
\arg\min_{s\in S}
\bigl(h(s)-\langle x_0+tn,s\rangle\bigr)=\varnothing.
\tag{SOL.5.4}
\]

**Proof.**

By the supporting-hyperplane theorem, there is a unit vector \(n\neq0\) such that
\[
\langle n,z\rangle\le\langle n,q\rangle
\qquad(z\in\Omega).
\tag{SOL.5.5}
\]

The inequality is strict for every \(s\in\Omega\). An explicit strictness constant is available: put
\[
d_s:=\operatorname{dist}(s,X\setminus\Omega)>0.
\]
Then
\[
s+\frac{d_s}{2}n\in\Omega,
\]
so (SOL.5.5) gives
\[
\langle n,q-s\rangle\ge\frac{d_s}{2}>0.
\tag{SOL.5.6}
\]

Fix \(t>0\) and set
\[
x_t:=x_0+tn,\qquad
L_t:=\bar h(q)-\langle x_t,q\rangle=m-t\langle n,q\rangle.
\]
For every \(s\in S\), using (SOL.5.1) and (SOL.5.6),
\[
\begin{aligned}
h(s)-\langle x_t,s\rangle-L_t
&=
\bigl(h(s)-\langle x_0,s\rangle-m\bigr)
+t\langle n,q-s\rangle\\
&\ge t\frac{d_s}{2}>0.
\end{aligned}
\tag{SOL.5.7}
\]
Thus every actual point of \(S\) has value strictly larger than \(L_t\).

On the other hand, let \(s_k\) be a recovery sequence for \(q\). Then
\[
\begin{aligned}
h(s_k)-\langle x_t,s_k\rangle
&\longrightarrow
\bar h(q)-\langle x_t,q\rangle\\
&=L_t.
\end{aligned}
\]
Therefore
\[
\inf_{s\in S}
\bigl(h(s)-\langle x_t,s\rangle\bigr)=L_t,
\]
but (SOL.5.7) shows that no \(s\in S\) attains it. This proves (SOL.5.4). ∎

The proof uses existence, not merely uniqueness.

---

## Lemma SOL.6 — No boundary minimizer survives under (a) and (c)

**Hypotheses.** Assume:

1. \(f\) is Legendre with \(\operatorname{dom}f=X\);
2. \(C\subset X\) is closed and nonempty;
3. \(C\) is right \(D\)-Chebyshev.

Use the notation of SOL.1 and SOL.4.

**Conclusion.** For every \(x\in X\),
\[
\arg\min_{p\in X}
\bigl(\bar h(p)-\langle x,p\rangle\bigr)
=\{p_x\}.
\tag{SOL.6.1}
\]

**Proof.**

SOL.4 shows that \(p_x\) is a minimizer and that any additional minimizer must be a boundary ghost \(q\in\operatorname{bd}\Omega\). Such a \(q\) satisfies the hypotheses of SOL.5 with \(x_0=x\). SOL.5 would then give a tilt \(x+tn\in X\) for which minimization over \(S\) has no solution.

Because \(\operatorname{dom}f=X\), every \(x+tn\) is an allowed right-projection query. This contradicts right \(D\)-Chebyshevness. Hence no additional minimizer exists. ∎

This closes precisely the gap isolated in Attempt 1’s SOL.6.

---

## Lemma SOL.7 — Convexification preserves the unique minimizers

**Hypotheses.** Retain the hypotheses of SOL.6. Put
\[
k:=\bar h,\qquad H:=k^{**}.
\]

**Conclusion.** For every \(x\in X\), \(p_x\) is the unique minimizer of
\[
H(p)-\langle x,p\rangle.
\tag{SOL.7.1}
\]

**Proof.**

Fix \(x\), and abbreviate
\[
p_*=p_x,\qquad
m=k(p_*)-\langle x,p_*\rangle.
\]
Set
\[
a(p):=k(p)-\langle x,p\rangle-m.
\]
By SOL.6,
\[
a\ge0,\qquad a(p)=0\iff p=p_*.
\tag{SOL.7.2}
\]

Because \(k\ge g\), SOL.1 gives
\[
a(p)\ge2\|p\|-A_x-m.
\tag{SOL.7.3}
\]
Define the explicit radius
\[
R_x:=1+\|p_*\|+\lvert A_x+m\rvert.
\]
If \(\|p\|\ge R_x\), then
\[
a(p)\ge\|p-p_*\|.
\tag{SOL.7.4}
\]

For \(\varepsilon>0\), let
\[
K_\varepsilon
=\{p:\|p\|\le R_x,\ \|p-p_*\|\ge\varepsilon\}.
\]
Since \(a\) is lower semicontinuous and has the unique zero \(p_*\),
\[
\delta_\varepsilon
:=
\min\left\{1,\inf_{K_\varepsilon}a\right\}>0,
\]
where the infimum over the empty set is \(+\infty\). Put
\[
M_x:=R_x+\|p_*\|,
\qquad
\kappa_\varepsilon
:=\min\left\{1,\frac{\delta_\varepsilon}{M_x}\right\}>0.
\]
Combining the compact and tail estimates gives
\[
a(p)\ge\kappa_\varepsilon\|p-p_*\|
\quad\text{whenever }\|p-p_*\|\ge\varepsilon.
\tag{SOL.7.5}
\]

The affine function
\[
p\mapsto m+\langle x,p\rangle
\]
is a minorant of \(k\), hence also of \(H=k^{**}\). Therefore
\[
H(p)-\langle x,p\rangle\ge m.
\]
Since \(H\le k\),
\[
H(p_*)-\langle x,p_*\rangle=m.
\]
Thus \(p_*\) minimizes the \(H\)-tilt.

Let \(q\) be another minimizer. Since
\[
\operatorname{epi}H
=\overline{\operatorname{conv}}(\operatorname{epi}k),
\]
there are finite convex combinations
\[
q_j=\sum_i\lambda_{ji}p_{ji}\to q
\]
and numbers \(r_{ji}\ge k(p_{ji})\) such that
\[
\sum_i\lambda_{ji}r_{ji}\to H(q).
\]
Because \(q\) has tilted value \(m\),
\[
\sum_i\lambda_{ji}a(p_{ji})\longrightarrow0.
\tag{SOL.7.6}
\]

Using (SOL.7.5),
\[
\begin{aligned}
\|q_j-p_*\|
&\le\sum_i\lambda_{ji}\|p_{ji}-p_*\|\\
&\le
\varepsilon+
\frac1{\kappa_\varepsilon}
\sum_i\lambda_{ji}a(p_{ji}).
\end{aligned}
\]
Letting \(j\to\infty\),
\[
\|q-p_*\|\le\varepsilon.
\]
Since \(\varepsilon>0\) is arbitrary, \(q=p_*\). ∎

---

## Lemma SOL.8 — Identification of \(S\) with a subdifferential domain

**Hypotheses.** Retain the hypotheses and notation of SOL.7.

**Conclusion.**
\[
S=\operatorname{dom}\partial H.
\tag{SOL.8.1}
\]

**Proof.**

First let \(p\in S\), and put
\[
x:=\nabla g(p).
\]
Because \(g\) is strictly convex on \(\Omega\),
\[
g(s)>g(p)+\langle\nabla g(p),s-p\rangle
\qquad(s\in S,\ s\neq p).
\]
Thus \(p\) is the unique minimizer of
\[
h(s)-\langle x,s\rangle.
\]
By SOL.6 and SOL.7, \(p\) is also the unique minimizer of
\[
H(s)-\langle x,s\rangle.
\]
Consequently
\[
x\in\partial H(p),
\]
so
\[
S\subset\operatorname{dom}\partial H.
\]

Conversely, let \(q\in\operatorname{dom}\partial H\), and choose
\[
x\in\partial H(q).
\]
Then \(q\) minimizes \(H-\langle x,\cdot\rangle\). By SOL.7 its unique minimizer is \(p_x\in S\). Hence \(q=p_x\in S\). ∎

---

## Lemma SOL.9 — Relative closedness forces convexity

**Hypotheses.**

- \(H\) is the proper lower-semicontinuous convex function from SOL.7.
- \(S=\operatorname{dom}\partial H\).
- \(S\subset\Omega\), where \(\Omega\) is open and convex.
- \(S\) is closed relative to \(\Omega\).

**Conclusion.** \(S\) is convex.

**Proof.**

Put
\[
D:=\operatorname{dom}H.
\]
Choose
\[
a\in\operatorname{ri}D.
\]
For a proper closed convex function in finite dimensions,
\[
\operatorname{ri}D\subset\operatorname{dom}\partial H=S.
\tag{SOL.9.1}
\]

Take \(p_0,p_1\in S\), \(0<t<1\), and define
\[
r=(1-t)p_0+tp_1.
\]
Since \(D\) is convex and contains \(p_0,p_1\), one has \(r\in D\). Since \(\Omega\) is convex,
\[
r\in\Omega.
\]

For \(0<\varepsilon<1\), put
\[
r_\varepsilon=(1-\varepsilon)r+\varepsilon a.
\]
The standard relative-interior segment property gives
\[
r_\varepsilon\in\operatorname{ri}D.
\]
For completeness, if \(A=\operatorname{aff}D\) and
\[
B_A(a,\rho)\subset D,
\]
then
\[
B_A(r_\varepsilon,\varepsilon\rho)\subset D,
\]
because
\[
r_\varepsilon+\varepsilon u
=(1-\varepsilon)r+\varepsilon(a+u).
\]
Hence, by (SOL.9.1),
\[
r_\varepsilon\in S.
\]
Now
\[
r_\varepsilon\to r\in\Omega.
\]
Relative closedness of \(S\) in \(\Omega\) gives \(r\in S\). Thus every open segment between points of \(S\) lies in \(S\), proving convexity. ∎

---

# Theorem SOL.10 — Hypothesis (b) is removable

**Hypotheses.** Let \(X=\mathbb R^n\). Let \(f\) be Legendre with
\[
\operatorname{dom}f=X.
\]
Let \(C\subset X\) be closed and nonempty. Assume that, for every \(x\in X\),
\[
P_C^\to(x)
=\arg\min_{y\in C}D_f(x,y)
\]
exists and is a singleton.

**Conclusion.**
\[
\boxed{\nabla f(C)\text{ is convex}.}
\]

No assumption on
\[
\overline{\nabla f(C)}\subset U^*
\]
is required.

**Proof.**

By SOL.1, \(S=\nabla f(C)\) is relatively closed in \(U^*\), and every linear tilt of \(h=f^*+\iota_S\) has a unique attained minimizer.

SOL.4 localizes every possible extra lower-hull minimizer to \(\operatorname{bd}U^*\). SOL.5 shows that such a ghost would force nonattainment at an outwardly perturbed tilt. Since \(\operatorname{dom}f=X\), that perturbed tilt is always an admissible query. Therefore SOL.6 gives uniqueness for every tilt of the lower-semicontinuous hull.

SOL.7–SOL.9 then imply that \(S\) is convex. ∎

Consequently, construction (A) is impossible under the stated hypotheses.

---

## Corollary SOL.11 — Exact failure mechanism on a box face

Suppose, for the box kernel, that a proposed construction has a ghost
\[
q=(1,q_2,\dots,q_n)
\]
tied with the actual minimizer at \(x_0\), with common tilted value \(m\).

For every actual \(s\in S\), \(s_1<1\), and for every \(t>0\),
\[
\begin{aligned}
&h(s)-\langle x_0+te_1,s\rangle
-\bigl(\bar h(q)-\langle x_0+te_1,q\rangle\bigr)\\
&\qquad=
\bigl(h(s)-\langle x_0,s\rangle-m\bigr)
+t(1-s_1)\\
&\qquad>0.
\end{aligned}
\tag{SOL.11.1}
\]
A recovery sequence converging to \(q\) makes the left-hand side tend to \(0\). Hence the infimum at \(x_0+te_1\) is not attained.

Thus flat faces do not rescue existence: they provide an especially simple supporting normal that certifies its failure.

For the sphere, the same argument uses \(n=q\):
\[
\langle q,q-s\rangle
=1-\langle q,s\rangle
\ge1-\|s\|>0.
\]

---

# Hypothesis audit

| Requirement | Used where |
|---|---|
| \(X=\mathbb R^n\) | Supporting hyperplanes, compactness, epigraph convexification |
| \(f\) Legendre | Gradient homeomorphism and strict convexity of \(f^*\) on \(U^*\) |
| \(\operatorname{dom}f=X\) | All linear tilts, especially \(x_0+tn\), are admissible |
| \(C\) closed | \(S=\nabla f(C)\) is relatively closed in \(U^*\) |
| Existence for every right projection | Contradicted directly by SOL.5 |
| Uniqueness for every right projection | Gives unique original tilt minimizers |
| \(\overline S\subset U^*\) | Not used |
| Boundary blow-up of \(f^*\) | Not used |
| Strict convexity of the dual-domain boundary | Not used |

---

# VERIFICATION RECIPE

## 1. Spherical arithmetic

```python
import sympy as sp

R = sp.symbols('R', nonnegative=True)

p_norm = R/sp.sqrt(1 + R**2)
sqrt_term = sp.sqrt(1 - p_norm**2)
value = -sqrt_term - R*p_norm

assert sp.simplify(value + sp.sqrt(1 + R**2)) == 0

gap = sp.sqrt(1 + R**2) - R
assert sp.simplify(
    gap - 1/(sp.sqrt(1 + R**2) + R)
) == 0
```

## 2. Tangential curvature on a box face

```python
p = sp.symbols('p', real=True)
a = -sp.sqrt(1 - p**2)

assert sp.simplify(
    sp.diff(a, p, 2) - (1 - p**2)**sp.Rational(-3, 2)
) == 0
```

Thus the face restriction is strictly convex in every tangential coordinate.

## 3. Exact ghost test

For any proposed candidate:

1. Compute
   \[
   h=f^*+\iota_S,\qquad \bar h=\operatorname{cl}h.
   \]
2. If a claimed ghost \(q\in\operatorname{bd}U^*\) minimizes at \(x_0\), find a supporting unit normal \(n\):
   \[
   \langle n,p\rangle\le\langle n,q\rangle
   \quad(p\in U^*).
   \]
3. For an actual \(s\in S\), calculate
   \[
   E(s):=h(s)-\langle x_0,s\rangle-m\ge0.
   \]
4. At \(x_t=x_0+tn\), verify the exact identity
   \[
   \begin{aligned}
   &h(s)-\langle x_t,s\rangle
   -\bigl(\bar h(q)-\langle x_t,q\rangle\bigr)\\
   &\qquad=E(s)+t\langle n,q-s\rangle>0.
   \end{aligned}
   \]
5. Verify along a recovery sequence \(s_k\to q\) that the same expression tends to \(0\).
6. Conclude exactly—not numerically—that the infimum at \(x_t\) is finite but unattained.

For a box face \(q_1=1\), take \(n=e_1\); the positive term is exactly
\[
t(1-s_1).
\]

## 4. Convexification check

The only standard epigraph identity used is
\[
\operatorname{epi}(k^{**})
=\overline{\operatorname{conv}}(\operatorname{epi}k).
\]
Finite-dimensional Carathéodory reduction permits each approximating convex combination to use at most \(n+2\) epigraph points.

---

# WHAT REMAINS

1. **For the stated finite-dimensional problem, no mathematical gap remains in this argument:** (B) holds and therefore (A) is impossible.

2. The key new step requiring adversarial checking is SOL.5, especially the sign in
   \[
   E(s)+t\langle n,q-s\rangle>0.
   \]
   The sign is consistent with minimization of \(h-\langle x,p\rangle\): moving \(x\) outward favors the missing boundary point.

3. The conclusion is not asserted for:
   - infinite-dimensional spaces;
   - kernels with \(\operatorname{dom}f\neq X\);
   - projection requirements imposed only on a proper subset of \(U\).

4. The box-face statement in the proposed structural idea should be corrected: the face is geometrically flat, but the restriction of \(f^*\) to it is generally not affine. This correction does not affect the ghost-exclusion proof.