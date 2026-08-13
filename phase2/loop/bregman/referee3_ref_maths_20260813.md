# Wave 5 — ref_maths (gpt-5.6-sol, effort=max, 2026-08-13 02:25)

> Adversarial lane on the claim that hypothesis (b) is removable.

The continuity-based version of the key step is false, but the consolidated proof has genuinely repaired it. I do not find a counterexample to Theorem 1 or a fatal gap in the ghost reduction.

## Core audit

### 1. Exact duality is correct

For \(p=\nabla f(y)\), Fenchel equality gives
\[
g(p)=\langle p,y\rangle-f(y),
\]
and hence
\[
D_f(x,y)
=f(x)+g(p)-\langle x,p\rangle.
\]
Because full-domain Legendre duality makes
\[
\nabla f:X\to\Omega
\]
a bijection, its restriction \(C\to S=\nabla f(C)\) is also a bijection. Therefore
\[
\nabla f\!\left(\arg\min_{y\in C}D_f(x,y)\right)
=
\arg\min_{p\in S}\bigl(g(p)-\langle x,p\rangle\bigr)
\]
as sets, not merely at the level of minimum values. Emptiness, uniqueness and multiplicity are all preserved.

The direction is also correct: varying the second Bregman argument produces a tilt by the primal query \(x\), not by \(\nabla f(x)\).

### 2. Lemma 4 is valid even for arbitrary \(C\)

If projections exist anywhere, then \(C\neq\varnothing\). If \(z\in\overline C\) and \(y_j\in C\) tends to \(z\), full domain gives continuity of \(f\) and \(\nabla f\), so
\[
D_f(z,y_j)\to0.
\]
Thus the attained minimum of \(D_f(z,\cdot)\) over \(C\) is zero. Since full-domain Legendre \(f\) is strictly convex,
\[
D_f(z,y)=0\iff z=y.
\]
Consequently \(z\in C\). No hidden boundedness or compactness assumption is needed.

### 3. The arbitrary-slope estimate is correct

For \(\|x\|\le R\), choose
\[
z=(R+L)\frac p{\|p\|}.
\]
Then
\[
g(p)-\langle x,p\rangle
\ge (R+L)\|p\|-f(z)-R\|p\|
\ge L\|p\|-A_{R,L}.
\]
Since \(f\) is finite convex on \(X\), it is continuous and \(A_{R,L}<\infty\). Taking \(R=0\) and then arbitrary \(L\) indeed proves
\[
g(p)/\|p\|\to+\infty.
\]
The quantifiers are in the correct order.

### 4. The ghost lemma survives scrutiny

The important scope condition is respected: the identity
\[
S=\operatorname{dom}\partial k^{**}
\]
is derived only under the assumption that every tilt of \(k\) has the unique minimizer \(p_x\in S\). It is not asserted for arbitrary \(S\).

Under that assumption:

1. \(F=k^*\) is finite everywhere because \(k\) is proper, lsc and supercoercive.
2. Unique maximizers plus the uniform boundedness argument imply continuity of \(x\mapsto p_x\).
3. Hence \(F\in C^1\) and \(\nabla F(x)=p_x\).
4. The reverse range inclusion is valid: for \(p\in S\), putting \(x=\nabla g(p)\), Fenchel equality shows that \(p\) is the unique minimizer of \(g-\langle x,\cdot\rangle\) on all of \(X\). Since \(k\ge g\) and \(k(p)=g(p)\), it is also the unique minimizer for \(k\). Thus
   \[
   \nabla F(X)=S.
   \]
5. With \(H=F^*=k^{**}\), subgradient inversion yields
   \[
   \operatorname{dom}\partial H=S.
   \]
6. The relative-interior chord argument is sound even when \(\operatorname{dom}H\) is lower-dimensional. For chord point \(r\in\Omega\), points obtained by moving \(r\) toward \(a\in\operatorname{ri}\operatorname{dom}H\) lie in \(S\) and converge to \(r\); relative closedness of \(S\) in \(\Omega\) then gives \(r\in S\).

Thus, if \(S\) is nonconvex, some tilt of \(k\) must have an additional minimizer. Lemma 7 correctly localizes every such additional minimizer to
\[
\overline S\setminus\Omega\subset\operatorname{bd}\Omega.
\]

### 5. Supporting normals exist and are strict on the interior

For \(q\in\operatorname{bd}\Omega\), where \(\Omega\) is nonempty, open and convex, the closed convex set \(K=\overline\Omega\) has a nonzero supporting normal at \(q\):
\[
\langle n,z-q\rangle\le0\qquad(z\in K).
\]
If equality held at \(s\in\Omega\), then a small displacement \(s+\varepsilon n\in\Omega\) would violate the supporting inequality. Therefore
\[
\langle n,s-q\rangle<0\qquad(s\in\Omega).
\]
Flat faces only allow equality at other boundary points; unboundedness is irrelevant.

### 6. Boundary continuity is false, but no longer used

The literal Attempt-1 step
\[
q\in\overline S,\quad g(q)<\infty
\quad\Longrightarrow\quad
g(s_j)\to g(q)
\]
is false.

The example in §10 supplies a valid certificate:
\[
g(0,0)=0,\qquad
g(u,\sqrt u)=u^2-\sqrt u+1\to1.
\]
Thus finite boundary value does not imply continuity.

The consolidated proof instead obtains a recovery sequence from the lsc hull:
\[
s_j\to q,\qquad g(s_j)\to k(q),
\]
and uses the correct tie
\[
k(q)-\langle x_0,q\rangle=m_0.
\]
That is enough:
\[
g(s_j)-\langle x_t,s_j\rangle
\to k(q)-\langle x_t,q\rangle.
\]
No continuity of \(g\) at \(q\) remains anywhere in the main proof.

### 7. The outward perturbation works for every \(t>0\)

For \(x_t=x_0+tn\),
\[
\begin{aligned}
g(s)-\langle x_t,s\rangle
-\bigl(k(q)-\langle x_t,q\rangle\bigr)
&=
\bigl(g(s)-\langle x_0,s\rangle-m_0\bigr)
+t\langle n,q-s\rangle\\
&>0
\end{aligned}
\]
for every \(s\in S\). The recovery sequence converges to the benchmark, so it is exactly the unattained infimum.

There is no need for \(q\) to remain a minimizer of the perturbed hull tilt. The displayed lower bound and recovery sequence alone identify the infimum over \(S\).

Because \(U=X\), every \(x_0+tn\) is an admissible query. No small-\(t\) restriction exists.

### 8. Infinite-height accumulation is not omitted

Every ghost furnished by Lemma 9 automatically has finite hull height:
\[
k(q)=m_0+\langle x_0,q\rangle<\infty.
\]
If all \(S\)-sequences approaching a boundary point have \(g(s_j)\to+\infty\), then \(k(q)=+\infty\), so that point cannot minimize a finite tilt of \(k\). The no-ghost convexification argument then rules out nonconvexity without needing to perturb such a point.

Thus infinite-height accumulation is not a missing branch of the argument.

### 9. Reconciliation

The actual theorem proof uses only the \(k^*\in C^1\), subdifferential-domain route. It does not silently rely on the other convexification proof. Therefore even if the separate “part2a” route were deleted, the main proof would remain complete.

The reconciliation is substantively honest about the important differences: unit-slope versus arbitrary-slope coercivity, \(g(q)\) versus \(k(q)\), and boundary continuity versus recovery sequences.

VERDICT: SURVIVES

1. **Location:** The continuity-based “key step” quoted from Attempt 1.  
   **Claim:** Finite \(g(q)\) at a boundary ghost implies \(g(s_j)\to g(q)\).  
   **Why wrong:** Convex lsc functions can be discontinuous at finite boundary points; §10 gives such an example.  
   **Suggested fix:** Use the hull tie and recovery sequence. This is already correctly implemented in Lemmas 9 and 11.

2. **Location:** §10, verification that the illustrative \(g\) is closed and supercoercive.  
   **Claim:** These properties are asserted somewhat tersely.  
   **Why wrong:** The claims are true, but two routine checks are omitted: lsc at \((0,v_0)\) for \(v_0\neq0\), and an explicit supercoercivity estimate.  
   **Suggested fix:** Add that \(v^2/u\to\infty\) near \((0,v_0\neq0)\); for \(r=\sqrt{u^2+v^2}\), split into \(u\ge r^{2/3}\) and \(u<r^{2/3}\) to obtain \(g(u,v)\ge c r^{4/3}-\sqrt r\).

3. **Location:** §11, statement that the omitted part2a route is also valid.  
   **Claim:** Both independent routes are valid.  
   **Why wrong:** This is not established by the consolidated text alone, although it is irrelevant to the theorem proved there.  
   **Suggested fix:** Either attach the complete part2a argument or phrase §11 only as a provenance summary.