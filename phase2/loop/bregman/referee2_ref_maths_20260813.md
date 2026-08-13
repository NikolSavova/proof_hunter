# Wave 3 — ref_maths (gpt-5.6-sol, effort=max, 2026-08-13 01:56)

> Adversarial lane on the claim that hypothesis (b) is removable.

The quoted key step is not valid as written, but the two wave-2 proofs contain a valid repair. I do not find a counterexample to the theorem.

## 1. Duality is correct, including argmin cardinality

For \(p=\nabla f(y)\), Fenchel equality gives
\[
f^*(p)=\langle p,y\rangle-f(y),
\]
and hence
\[
D_f(x,y)=f(x)+f^*(p)-\langle x,p\rangle.
\]
Since \(f\) is Legendre and \(\operatorname{dom}f=X\),
\[
\nabla f:X\to U^*
\]
is a bijection with inverse \(\nabla f^*\). Consequently,
\[
\nabla f\!\left(\arg\min_{y\in C}D_f(x,y)\right)
=
\arg\min_{p\in S}\bigl(f^*(p)-\langle x,p\rangle\bigr),
\qquad S=\nabla f(C).
\]
This is an equality of argmin sets, not merely an equality of minimum values. Empty sets, singletons, and multiplicities are all preserved. The use of the second Bregman argument is therefore in the correct direction.

## 2. What nonconvexity actually forces

Put
\[
g=f^*,\qquad h=g+\iota_S,\qquad k=\operatorname{cl}_{\mathrm{lsc}}h.
\]
The correct ghost statement is:

\[
k(q)-\langle x_0,q\rangle
=
g(p_0)-\langle x_0,p_0\rangle=m_0,
\]
not necessarily
\[
g(q)-\langle x_0,q\rangle=m_0.
\]

The implication “\(S\) nonconvex \(\Rightarrow\) some ghost exists” is valid, but it requires the full convexification argument:

1. Every original tilt of \(h\) has a unique minimizer \(p_x\in S\).
2. The same \(p_x\) minimizes \(k-\langle x,\cdot\rangle\).
3. Any additional \(k\)-minimizer in \(U^*\) would belong to \(S\), by relative closedness, and contradict uniqueness. Thus extras are boundary ghosts.
4. If no boundary ghosts existed, every tilt of \(k\) would have the unique minimizer \(p_x\).
5. Let \(F=k^*\) and \(H=F^*=k^{**}\). Unique locally bounded maximizers imply
   \[
   F\in C^1(X),\qquad \nabla F(x)=p_x.
   \]
6. The range is exactly \(S\). Indeed, \(\nabla F(X)\subset S\), while for \(p\in S\), taking \(x=\nabla g(p)\) makes \(p\) the unique minimizer of both the \(g\)-tilt and the \(k\)-tilt.
7. Fenchel inversion gives
   \[
   S=\nabla F(X)=\operatorname{dom}\partial H.
   \]
8. Since \(\operatorname{ri}(\operatorname{dom}H)\subset\operatorname{dom}\partial H\), relative closedness of \(S\) inside the open convex set \(U^*\) fills every segment between points of \(S\).

Thus the contrapositive does supply a finite boundary ghost. There is no circularity in the wave-2 ordering. It would, however, be circular to assert
\[
S=\operatorname{dom}\partial k^{**}
\]
before uniqueness of all \(k\)-tilts had been established.

## 3. The supporting normal exists and is strict on \(U^*\)

Let \(\Omega=U^*\) and \(q\in\operatorname{bd}\Omega\). Since \(\Omega\) is nonempty, open, and convex, the closed convex set \(\overline\Omega\) has a nonzero supporting normal \(n\) at \(q\):
\[
\langle n,z-q\rangle\le 0
\qquad(z\in\overline\Omega).
\]
Moreover,
\[
\langle n,p-q\rangle<0
\qquad(p\in\Omega).
\]
Indeed, equality at an interior point \(p\) would be contradicted by \(p+\varepsilon n\in\Omega\) for sufficiently small \(\varepsilon>0\).

Unboundedness of \(\Omega\) causes no problem. A flat boundary face only means that other boundary points may satisfy equality; no interior point does. If \(\Omega=X\), there is no boundary ghost to consider.

## 4. Boundary continuity of \(f^*\) is false

This is the genuine defect in the quoted key paragraph. Finiteness of \(f^*(q)\), or even bounded \(f^*\)-height along a sequence approaching \(q\), does not imply continuity at \(q\).

For example, define \(g:\mathbb R^2\to(-\infty,+\infty]\) by
\[
g(u,v)=
\begin{cases}
u^2-\sqrt u+\dfrac{v^2}{u},&u>0,\\[1ex]
0,&(u,v)=(0,0),\\
+\infty,&\text{otherwise}.
\end{cases}
\]
Then:

- \(g\) is proper, closed, and convex;
- on \(\Omega=(0,\infty)\times\mathbb R\), its Hessian is positive definite:
  \[
  \det\nabla^2g(u,v)
  =\frac4u+\frac1{2u^{5/2}}>0;
  \]
- its gradient blows up as \(u\downarrow0\), so \(g\) is Legendre;
- \(g\) is supercoercive, so \(f:=g^*\) is Legendre with \(\operatorname{dom}f=\mathbb R^2\);
- \(f^*=g\).

The conjugate can be written as
\[
f(a,b)=
\sup_{u>0}
\left[
\left(a+\frac{b^2}{4}\right)u-u^2+\sqrt u
\right],
\]
which is finite for every \((a,b)\).

At \(q=(0,0)\),
\[
g(q)=0,
\]
but along \(p_u=(u,\sqrt u)\),
\[
g(p_u)=u^2-\sqrt u+1\longrightarrow1.
\]
Thus \(g=f^*\) is finite but discontinuous at \(q\).

There is an even sharper illustration of the ghost-height problem. Let
\[
S=\{(1,1)\}
\cup
\left\{
\left(u,\sqrt{u(1+\sqrt u)}\right):u>0
\right\}.
\]
Along the curve,
\[
g\left(u,\sqrt{u(1+\sqrt u)}\right)=1+u^2.
\]
For \(h=g+\iota_S\), at \(x_0=0\):

- \(p_0=(1,1)\) is the unique actual minimizer, with value \(1\);
- \(q=(0,0)\) is a lower-hull ghost with
  \[
  k(q)=1;
  \]
- but
  \[
  g(q)=0.
  \]

Hence the ghost is tied at height \(k(q)\), not at height \(g(q)\). The displayed identity using \(\phi_t(q)=g(q)-\langle x_t,q\rangle\) is simply wrong in this example.

This is not a counterexample to the theorem: the outward perturbation produces nonattainment, exactly as the corrected proof predicts.

## 5. The recovery-sequence repair is valid

The wave-2 proofs correctly avoid boundary continuity. Since \(k(q)<+\infty\), the definition of the lower-semicontinuous hull supplies
\[
s_j\in S,\qquad s_j\to q,\qquad g(s_j)=h(s_j)\to k(q).
\]
Let
\[
m_0=k(q)-\langle x_0,q\rangle
\]
and choose an outward supporting normal \(n\). For \(x_t=x_0+tn\), define
\[
L_t=k(q)-\langle x_t,q\rangle.
\]
Then for every \(s\in S\),
\[
\begin{aligned}
g(s)-\langle x_t,s\rangle-L_t
&=
\bigl(g(s)-\langle x_0,s\rangle-m_0\bigr)
+t\langle n,q-s\rangle\\
&>0.
\end{aligned}
\]
Meanwhile,
\[
g(s_j)-\langle x_t,s_j\rangle\to L_t.
\]
Therefore the infimum over \(S\) is \(L_t\) and is not attained.

This repair works even when
\[
k(q)>g(q).
\]
It is the decisive reason the false continuity assertion is not fatal to the wave-2 proofs.

## 6. No small-\(t\) restriction and no perturbed-ghost problem

No smallness is needed. Every \(t>0\) works:

- \(\operatorname{dom}f=X\) ensures \(x_0+tn\in U\);
- the global lower bound above prevents any “jumping” point of \(S\) from beating \(L_t\);
- the recovery sequence forces the infimum to equal \(L_t\).

It is not necessary that \(q\) minimize the entire perturbed lower-hull tilt. It only has to supply the limiting value of the optimization over \(S\).

## 7. Infinite-height accumulation is covered

A boundary point with only infinite-height approaches cannot be a ghost minimizer. If every \(s_j\in S\) approaching \(q\) satisfies
\[
g(s_j)\to+\infty,
\]
then
\[
k(q)=+\infty,
\]
whereas the minimum at \(p_x\in S\) is finite.

Conversely, if \(S\) were nonconvex, the convexification argument forces an additional minimizer of some \(k\)-tilt. Such a minimizer automatically has finite \(k\)-height and therefore has a finite-height recovery sequence. Thus the wave-2 arguments do not silently assume that every boundary accumulation has finite height.

## 8. The literal “under (a) and (c) alone” statement needs one preliminary lemma

Both wave-2 theorem statements still assume that \(C\) is closed and nonempty, even though these properties were included in hypothesis (b). Thus, as written, they only directly remove the closure-inside condition
\[
\overline{\nabla f(C)}\subset U^*.
\]

This is easily repaired because (a) and existence in (c) already force \(C\) to be nonempty and closed. Indeed, if \(z\in\overline C\), choose \(y_j\in C\) with \(y_j\to z\). Since \(f\) is \(C^1\) on \(X\),
\[
D_f(z,y_j)\to0.
\]
The right projection at \(z\) exists, so its minimum is \(0\). Strict convexity of the full-domain Legendre function gives
\[
D_f(z,y)=0\iff y=z.
\]
Therefore \(z\in C\). Hence \(C\) is closed. Nonemptiness follows from the existence of any projection.

After inserting this lemma, the proof genuinely uses only (a) and (c).

## 9. Comparison of the two wave proofs

There is no substantive disagreement:

- part2a proves uniqueness after convexification via quantitative epigraph estimates;
- part2b proves differentiability of \(k^*\) and identifies its gradient range;
- both use the correct lower-hull recovery sequence;
- both use the same strict supporting-normal perturbation.

One minor exposition issue occurs in part2b SOL.2: the displayed estimate
\[
g(p)-\langle x,p\rangle\ge \|p\|-A_R
\]
by itself proves coercivity, not supercoercivity. The stronger fact follows by choosing, for arbitrary \(L>0\),
\[
z=(R+L)\frac p{\|p\|},
\]
which gives
\[
g(p)-\langle x,p\rangle
\ge L\|p\|-\max_{\|z\|=R+L}f(z).
\]
This is only a minor repair, and the needed boundedness/coercivity arguments are unaffected.

VERDICT: MINOR_REPAIRS

1. **Location:** Quoted key perturbation step.  
   **Claim:** Finite \(f^*(q)\) or finite-height accumulation implies continuity of \(f^*\) at \(q\).  
   **Why wrong:** Closed convex functions can be finite and discontinuous at boundary points; the explicit \(g(u,v)=u^2-\sqrt u+v^2/u\) example demonstrates this.  
   **Suggested fix:** Benchmark the perturbation with \(k(q)\), where \(k=\operatorname{cl}_{\mathrm{lsc}}(f^*+\iota_S)\), and use a recovery sequence.

2. **Location:** Description of the ghost supplied by SOL.6.  
   **Claim:** The ghost is tied under the actual value \(f^*(q)-\langle x_0,q\rangle\).  
   **Why wrong:** SOL.6 only yields an epigraph ghost at height \(k(q)\), which may strictly exceed \(f^*(q)\).  
   **Suggested fix:** State the tie as \(k(q)-\langle x_0,q\rangle=m_0\).

3. **Location:** Theorems SOL.10 and SOL.7 versus the headline “under (a) and (c) alone.”  
   **Claim:** The written theorem already removes all of hypothesis (b).  
   **Why wrong:** Both written theorems retain closedness and nonemptiness of \(C\).  
   **Suggested fix:** Add the short lemma that full-domain right-projection attainment forces \(C\) to be nonempty and closed.

4. **Location:** part2b SOL.2.  
   **Claim:** The displayed unit-slope bound alone implies supercoercivity.  
   **Why wrong:** It directly implies coercivity only.  
   **Suggested fix:** State the arbitrary-slope bound obtained by choosing a sphere of radius \(R+L\).

5. **Location:** Duality SOL.1.  
   **Claim checked:** Right projection corresponds bijectively to minimization of \(f^*(p)-\langle x,p\rangle\) over \(S\).  
   **Assessment:** Correct; argmin sets and their cardinalities are preserved.  
   **Suggested fix:** None.

6. **Location:** Supporting-normal lemmas.  
   **Claim checked:** Every boundary ghost has a normal strict on all of \(U^*\).  
   **Assessment:** Correct in finite dimensions; unboundedness and flat faces do not affect strictness for interior points.  
   **Suggested fix:** None.

7. **Location:** Perturbation and infinite-height cases.  
   **Claim checked:** Every \(t>0\) is admissible, and infinite-height accumulations do not leave a gap.  
   **Assessment:** Correct once the ghost height is \(k(q)\) and recovery sequences are used.  
   **Suggested fix:** None.