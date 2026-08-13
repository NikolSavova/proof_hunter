# Wave 5 — ref_break (gpt-5.6-sol, effort=max, 2026-08-13 02:25)

> Adversarial lane on the claim that hypothesis (b) is removable.

I could not construct the requested counterexample. The strongest boundary-discontinuity candidate satisfies full domain, closedness, nonemptiness, and nonconvexity of \(C^*\), but it necessarily fails projection existence. The consolidated proof’s replacement of boundary continuity by the hull recovery sequence closes the proposed escape route.

## Strongest concrete construction attempt

Use the function from §10:
\[
g(u,v)=
\begin{cases}
u^2-\sqrt u+\dfrac{v^2}{u},&u>0,\\[1ex]
0,&(u,v)=(0,0),\\
+\infty,&\text{otherwise}.
\end{cases}
\]
Its Hessian on
\[
\Omega=(0,\infty)\times\mathbb R
\]
is positive definite, with
\[
\det\nabla^2g(u,v)
=\frac4u+\frac1{2u^{5/2}}>0.
\]
The closed extension is strictly convex and essentially smooth, and \(g\) is supercoercive. Hence
\[
f:=g^*
\]
is Legendre with
\[
\operatorname{dom}f=\mathbb R^2,
\]
and \(\nabla f:\mathbb R^2\to\Omega\) is a homeomorphism.

Set
\[
p_0=(1,1),\qquad
\Gamma=
\left\{
\left(u,\sqrt{u(1+\sqrt u)}\right):u>0
\right\},
\qquad
S=\{p_0\}\cup\Gamma,
\]
and define
\[
C:=\nabla g(S).
\]
The set \(S\) is closed relative to \(\Omega\), so \(C\) is closed and nonempty, and
\[
\nabla f(C)=S.
\]

Checking the requested properties in order:

1. **Full domain (a): satisfied.**
   \[
   \operatorname{dom}f=\mathbb R^2.
   \]

2. **Right Chebyshevness (c): fails.**  
   For
   \[
   x_t=(-t,0),\qquad t>0,
   \]
   points on \(\Gamma\) satisfy
   \[
   g\left(u,\sqrt{u(1+\sqrt u)}\right)=1+u^2,
   \]
   and therefore
   \[
   g(p)-\langle x_t,p\rangle
   =1+u^2+tu>1,
   \]
   with limit \(1\) as \(u\downarrow0\). At \(p_0\),
   \[
   g(p_0)-\langle x_t,p_0\rangle=1+t>1.
   \]
   Consequently
   \[
   \inf_{p\in S}\bigl(g(p)-\langle x_t,p\rangle\bigr)=1
   \]
   is not attained. By exact dual correspondence,
   \[
   P_C^\to(x_t)=\varnothing.
   \]

3. **Nonconvexity: satisfied.**  
   Both
   \[
   (1,1),\quad (1,\sqrt2)
   \]
   belong to \(S\), while
   \[
   \left(1,\frac{1+\sqrt2}{2}\right)\notin S.
   \]

Thus this candidate passes every desired feature except the decisive one: projection existence.

It already combines several suggested attack surfaces:

- \(g\) is discontinuous at the finite boundary point \(q=(0,0)\);
- \(\Omega\) is unbounded;
- its boundary is flat;
- \(g(q)=0\), whereas the relevant hull height is \(k(q)=1\).

For \(n\ge3\), taking
\[
g_n(u,v,w)=g(u,v)+\frac12\|w\|^2,
\qquad
S_n=S\times\mathbb R^{n-2}
\]
produces the same failure at \(x_t=(-t,0,0)\). Extra dimensions do not help.

## Why the candidate cannot be repaired

The prompt’s continuity premise is not load-bearing in the consolidated proof. If
\[
h=g+\iota_S,\qquad k=\operatorname{cl}_{\mathrm{lsc}}h,
\]
and \(k(q)<\infty\), the definition of \(k\) supplies a recovery sequence
\[
s_j\in S,\qquad s_j\to q,\qquad g(s_j)\to k(q).
\]
This remains true when
\[
g(q)<k(q)
\]
and \(g\) is discontinuous at \(q\).

Moreover, a nonconvex \(S\) really must produce such a finite ghost. If every tilt of \(k\) had only the actual minimizer \(p_x\in S\), then:

- \(F=k^*\) would be finite and \(C^1\);
- \(\nabla F(\mathbb R^n)=S\);
- for \(H=F^*=k^{**}\),
  \[
  S=\operatorname{dom}\partial H;
  \]
- since
  \[
  \operatorname{ri}(\operatorname{dom}H)
  \subset\operatorname{dom}\partial H
  \subset\operatorname{dom}H,
  \]
  and \(S\) is closed relative to \(\Omega\), every chord between two points of \(S\) would be filled.

Hence \(S\) would be convex. Therefore nonconvexity forces an additional finite hull minimizer
\[
q\in\operatorname{bd}\Omega
\]
with
\[
k(q)-\langle x_0,q\rangle=m_0.
\]

At every such boundary point, finite-dimensional convex geometry supplies a nonzero outward normal \(n\) satisfying
\[
\langle n,q-s\rangle>0\qquad(s\in\Omega).
\]
Unboundedness and flat faces do not affect this strict inequality: equality at an interior point would allow a small ball to cross the supporting hyperplane.

For \(x_t=x_0+tn\) and \(s\in S\),
\[
\begin{aligned}
&g(s)-\langle x_t,s\rangle
-\bigl(k(q)-\langle x_t,q\rangle\bigr)\\
&\quad=
\underbrace{g(s)-\langle x_0,s\rangle-m_0}_{\ge0}
+t\underbrace{\langle n,q-s\rangle}_{>0}>0.
\end{aligned}
\]
The recovery sequence converges to the benchmark value, so the perturbed infimum is not attained. Since \(\operatorname{dom}f=\mathbb R^n\), \(x_t\) is always an admissible query.

## Other proposed escape routes

- **Infinite-height accumulation:** If every \(S\)-sequence approaching \(q\) has \(g(s_j)\to+\infty\), then \(k(q)=+\infty\); such a point cannot tie the finite value \(m_0\). Escape to norm infinity is separately excluded by supercoercivity.
- **Failure of a recovery sequence:** Impossible for a finite value of the lsc hull; recovery is built into its definition.
- **No supporting normal:** Impossible at a finite boundary point of a nonempty open convex set in finite dimensions.
- **Tilt leaves the query domain:** Impossible because \(U=\operatorname{dom}f=\mathbb R^n\).
- **Arbitrary nonclosed \(C\):** Lemma 4 is valid. For \(z\in\overline C\), continuity gives \(D_f(z,y_j)\to0\); attainment at \(z\) and strict convexity force the minimizer to equal \(z\), hence \(z\in C\).
- **Failure of supercoercivity:** Lemma 6’s arbitrary-slope estimate is valid:
  \[
  g(p)-\langle x,p\rangle
  \ge L\|p\|-A_{R,L}.
  \]
  Since \(L>0\) is arbitrary, it excludes bounded-slope escape to infinity.

The most robust components are therefore the hull recovery sequence and the strict supporting-normal perturbation, with full primal domain making every perturbation admissible. Section 10 correctly demonstrates why \(k(q)\), rather than \(g(q)\), is indispensable, and the construction-relevant reconciliation in §11 does not silently retain boundary continuity.

VERDICT: SURVIVES

1. **Location:** None. **Claim:** No theorem-level claim was falsified in the construction lane. **Why wrong:** Not applicable; the strongest finite-discontinuity, unbounded-domain, flat-boundary, and higher-dimensional candidates all fail hypothesis (c) by nonattainment. **Suggested fix:** None.