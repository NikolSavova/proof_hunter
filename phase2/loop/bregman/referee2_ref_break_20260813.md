# Wave 3 — ref_break (gpt-5.6-sol, effort=max, 2026-08-13 00:49)

> Adversarial lane on the claim that hypothesis (b) is removable.

I could not construct a counterexample. The strongest suggested attack—finite but discontinuous \(f^*\) at a boundary ghost—can be realized explicitly, but right-Chebyshev existence then fails exactly under the outward perturbation.

## 1. A genuine finite, discontinuous boundary point

Work in \(\mathbb R^2\), with dual coordinates \(p=(u,v)\). Define
\[
g(u,v)=
\begin{cases}
\dfrac{v^2}{u}-\sqrt{u}+u^2,&u>0,\\[1ex]
0,&(u,v)=(0,0),\\
+\infty,&\text{otherwise}.
\end{cases}
\]
Let
\[
f:=g^*.
\]

On \(\Omega:=\{u>0\}\),
\[
\nabla^2 g(u,v)=
\begin{pmatrix}
\dfrac{2v^2}{u^3}+\dfrac1{4u^{3/2}}+2&
-\dfrac{2v}{u^2}\\[1.2ex]
-\dfrac{2v}{u^2}&\dfrac2u
\end{pmatrix},
\]
whose determinant is
\[
\frac1{2u^{5/2}}+\frac4u>0.
\]
Thus \(g\) is strictly convex on \(\Omega\). Its extension at \((0,0)\) is closed and convex; for \(0<t<1\),
\[
g(tu,tv)-t g(u,v)
=(t-\sqrt t)\sqrt u+(t^2-t)u^2<0.
\]

Moreover,
\[
\frac{\partial g}{\partial u}
=-\frac{v^2}{u^2}-\frac1{2\sqrt u}+2u\longrightarrow-\infty
\qquad(u\downarrow0),
\]
so \(g\) is essentially smooth. It is Legendre.

It is also supercoercive. Indeed, if \(r=\sqrt{u^2+v^2}\to\infty\), then either \(u\ge r^{2/3}\), in which case \(u^2/r\ge r^{1/3}\), or \(u<r^{2/3}\), in which case \(v^2/u\gtrsim r^{4/3}\). Hence
\[
\frac{g(u,v)}{\sqrt{u^2+v^2}}\to+\infty.
\]
Consequently
\[
\operatorname{dom}f=\mathbb R^2,
\]
and Legendre duality gives that \(f\) is Legendre and \(f^*=g\).

At
\[
q=(0,0)\in\operatorname{bd}\Omega,
\]
\(g\) is finite but not continuous:
\[
g(\varepsilon,0)\to0,\qquad
g(\varepsilon,\sqrt\varepsilon)\to1,\qquad
g(\varepsilon,\varepsilon^{1/4})\to+\infty.
\]
Thus the proposed discontinuous-boundary attack surface is real.

## 2. The resulting near-counterexample still loses existence

Let \(\alpha>1\) be the unique solution of
\[
\alpha^4-\alpha=1,
\]
and define
\[
S=
\{(r^2,r):r>0\}\cup\{p_0\},
\qquad
p_0=(\alpha^2,0).
\]
This set is closed relative to \(\Omega\). Set
\[
C:=\nabla g(S).
\]
Because \(\nabla g:\Omega\to\mathbb R^2\) is a homeomorphism, \(C\) is closed and nonempty, and
\[
\nabla f(C)=S.
\]

The set \(S\) is nonconvex. For example,
\[
(1,1),(4,2)\in S,
\]
but
\[
\frac12(1,1)+\frac12(4,2)
=\left(\frac52,\frac32\right)\notin S.
\]

Now take
\[
x_0=(0,-2).
\]
Along \(p(r)=(r^2,r)\),
\[
g(p(r))=1-r+r^4,
\]
and therefore
\[
g(p(r))-\langle x_0,p(r)\rangle
=1+r+r^4>1.
\]
At \(p_0\),
\[
g(p_0)-\langle x_0,p_0\rangle
=\alpha^4-\alpha=1.
\]
Thus \(p_0\) is the unique minimizer at \(x_0\).

However, the lower-semicontinuous hull
\[
k:=\operatorname{cl}(g+\iota_S)
\]
satisfies
\[
k(q)=1,
\]
even though \(g(q)=0\). Hence \(q\) is a genuine hull ghost tied with \(p_0\) at height \(1\).

The outward normal to \(\Omega=\{u>0\}\) at \(q\) is
\[
n=(-1,0).
\]
For \(t>0\), put
\[
x_t=x_0+tn=(-t,-2).
\]
Then
\[
g(p(r))-\langle x_t,p(r)\rangle
=1+r+r^4+tr^2>1,
\]
with limit \(1\) as \(r\downarrow0\), while
\[
g(p_0)-\langle x_t,p_0\rangle
=1+t\alpha^2>1.
\]
Therefore
\[
\inf_{p\in S}\bigl(g(p)-\langle x_t,p\rangle\bigr)=1
\]
and the infimum is not attained. Thus
\[
P_C^\to(x_t)=\varnothing.
\]

So this candidate has:

1. \(f\) Legendre and \(\operatorname{dom}f=\mathbb R^2\);
2. \(C\) closed and nonempty;
3. \(C^*=\nabla f(C)\) nonconvex;

but it fails hypothesis (c), specifically existence.

The same example extends to every \(n\ge3\) by using
\[
g_n(u,v,w)=g(u,v)+\frac12\|w\|^2
\]
and embedding \(S\) in \(w=0\).

## 3. Why the other attack surfaces cannot produce a counterexample

Let generally
\[
g=f^*,\quad \Omega=U^*,\quad S=\nabla f(C),\quad
h=g+\iota_S,\quad k=\operatorname{cl}h.
\]

Because \(C\) is closed and \(\nabla f:X\to\Omega\) is a homeomorphism, \(S\) is closed relative to \(\Omega\). Hypothesis (c) gives a unique attained minimizer \(p_x\in S\) of every tilt \(h-\langle x,\cdot\rangle\).

If a tilt of \(k\) had an additional minimizer \(q\), then:

- \(k(q)<\infty\), so a recovery sequence \(s_j\in S\) exists with
  \[
  s_j\to q,\qquad h(s_j)\to k(q);
  \]
- relative closedness excludes \(q\in\Omega\), hence \(q\in\operatorname{bd}\Omega\);
- every finite-dimensional boundary point of an open convex set has an outward supporting normal \(n\);
- openness makes
  \[
  \langle n,s\rangle<\langle n,q\rangle
  \qquad(s\in S).
  \]

Writing
\[
m=k(q)-\langle x,q\rangle,
\]
one obtains for every \(s\in S\) and \(t>0\),
\[
\begin{aligned}
h(s)-\langle x+tn,s\rangle
-\bigl(m-t\langle n,q\rangle\bigr)
&=
\underbrace{h(s)-\langle x,s\rangle-m}_{\ge0}\\
&\quad+t\underbrace{\langle n,q-s\rangle}_{>0}
>0.
\end{aligned}
\]
The recovery sequence makes this excess tend to \(0\). Hence the perturbed infimum is not attained. Since \(\operatorname{dom}f=X\), \(x+tn\) is always admissible, contradicting (c).

Thus every tilt of \(k\) has the unique minimizer \(p_x\in S\). Setting
\[
F=k^*,\qquad H=F^*=k^{**},
\]
supercoercivity and uniqueness imply
\[
F\in C^1(X),\qquad \nabla F(x)=p_x.
\]
Every \(p\in S\) occurs as such a minimizer by choosing \(x=\nabla g(p)\), so
\[
S=\nabla F(X)=\operatorname{dom}\partial H.
\]
Finally, \(\operatorname{dom}\partial H\) is nearly convex, and its relative closedness inside the convex open set \(\Omega\) fills every chord. Therefore \(S\) is convex.

Accordingly:

- **Boundary discontinuity can occur**, but it only changes the ghost height from \(g(q)\) to \(k(q)\).
- **Unbounded \(U^*\)** does not remove supporting normals at finite boundary points.
- **Infinite-height accumulation** cannot be a minimizer of \(k\).
- **Higher dimensions** do not weaken strict supporting separation.
- **The recovery sequence** is automatic from finite \(k(q)\), not from continuity of \(g\).

VERDICT: SURVIVES

1. **Location:** Quoted informal key step, “\(f^*\) is continuous at \(q\).”  
   **Claim:** Finite boundary value implies continuity.  
   **Why wrong:** The explicit \(g\) above is Legendre, finite at \(q\), and discontinuous there. In the example \(g(q)=0\) while the relevant hull height is \(k(q)=1\).  
   **Suggested fix:** State the ghost relation using \(k=\operatorname{cl}(f^*+\iota_S)\), and use a recovery sequence satisfying \(f^*(s_j)\to k(q)\). The full wave-2 proofs already make this repair.

2. **Location:** Proposed finite-discontinuity/unbounded-domain construction.  
   **Claim:** Discontinuity might prevent the perturbed infimum from approaching the ghost height.  
   **Why wrong:** It prevents convergence to \(f^*(q)\), but not convergence to the lower-hull value \(k(q)\). The explicit candidate above has an empty argmin at every \(x_0+t(-1,0)\), \(t>0\).  
   **Suggested fix:** None under (a) and (c); one would have to relax full tilt admissibility or attainment.

3. **Location:** Proposed infinite-height attack.  
   **Claim:** Boundary accumulation with \(f^*(p_j)\to+\infty\) may conceal nonconvexity.  
   **Why wrong:** Such a point has \(k(q)=+\infty\) and cannot be a minimizing ghost. If all boundary accumulations have infinite height, \(f^*+\iota_S\) is lower semicontinuous, and the convexification argument forces \(S\) to be convex.  
   **Suggested fix:** None within the stated finite-dimensional hypotheses.