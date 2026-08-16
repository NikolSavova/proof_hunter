# Opposite singleton return, and the rooted-profile anti-alignment gate

**Date:** 2026-08-15.  All logarithms are base two.  This continues
`SOURCE_REUSE_BALANCED_ONE_ENDED_PROFILE_BARRIER.md`.

## Verdict

The balanced Boolean source does have an exact two-ended return identity,
but only before a common root/base is retained.  If \(Q\) is a convex
\(q\)-gon and \(z_L,z_R\) lie in opposite exterior tangent chambers, then the
two singleton compatibility profiles satisfy

\[
                         P_{z_L}P_{z_R}\ge 2^q=V(Q).     \tag{1}
\]

Consequently, if left and right endpoint children export \(K_L,K_R\)
ordinary faces which coexist with the corresponding half-source cubes,
then the two load-one mixed banks give the genuine return

\[
                         V\ge\sqrt{2^qK_LK_R}.           \tag{2}
\]

To improve the already present Boolean source bank by \(s^\theta\), (2)
needs

\[
                         K_LK_R\ge 2^q s^{2\theta}.      \tag{3}
\]

This does **not** extend to arbitrary endpoint children in the actual
rooted context.  There is a scalable rational convex child \(X_m\) with
\(V(X_m)=2^m\) and a common retained root \(c\) for which the two opposite
rooted export capacities are both only \(O(m^2)\):

\[
 \#\{F:F\cup\{a,c\}\text{ ordinary}\},\quad
 \#\{F:F\cup\{b,c\}\text{ ordinary}\}
       \le 1+m+{m\choose2}.                             \tag{4}
\]

Their product is \(o(2^m)\).  This is an exact **profile-state
anti-alignment barrier**: the child state is

\[
                  (H,C,U)=(2^m,O(m^2),O(m^2)),           \tag{5}
\]

and any common-root recursion sees only \(C,U\) in its mixed terms while
\(H\) remains additive.  The construction is projectively composable as an
arbitrary child of the common-guard wrapper.  It is not, by itself, a
recursive sub-half construction: realizing a whole low-face hierarchy of
such states remains the heterogeneous cap/cup problem.

Thus the Boolean source can be charged globally only if one also proves a
**root-release** or **rooted export** theorem.  Least-counterexample
induction on the child face count alone supplies neither.  The missing
return is not endpoint decoder load; it is physical coexistence with the
retained root.

## 1. Exact opposite-singleton product

Let \(Q\) be a strictly convex finite set and \(z\) an exterior point.  Write

\[
 D(z)=Q\cap\operatorname{vert}\operatorname{conv}(Q\cup\{z\}).       \tag{6}
\]

The set \(D(z)\) is the far boundary chain between the two tangency
vertices.  Since \(D(z)\cup\{z\}\) is itself in convex position, every
subset \(A\subseteq D(z)\) satisfies \(A\cup\{z\}\) ordinary.  Therefore

\[
                    P_z\ge 2^{|D(z)|}.                  \tag{7}
\]

Suppose \(z_L,z_R\) are in opposite chambers for which
\(D(z_L)\cup D(z_R)=Q\).  Choose a disjoint partition

\[
                  Q=S_L\mathbin{\dot\cup}S_R,
            \qquad S_L\subseteq D(z_L),\quad
                   S_R\subseteq D(z_R).                 \tag{8}
\]

Equations (7)--(8) give

\[
            P_{z_L}P_{z_R}
              \ge2^{|S_L|}2^{|S_R|}=2^q,               \tag{9}
\]

proving (1).  A centrally symmetric \(q=2m\)-gon and two sufficiently far
antipodal generic chambers satisfy (8): their tangent vertices are
antipodal and the two far chains cover the boundary.  The property is
open, so the finite rational chambers used in the source-reuse barrier
also satisfy it.

Notice that (1) is quantitatively sharp at exponential scale.  In the
balanced cage, each profile has only
\(q^{O(1)}2^{q/2}\) members.  Multiplying them merely regenerates the
Boolean source; it does not produce a new factor.

## 2. Conditional child-return theorem

Let the ambient labels be split into the source \(Q\) and two disjoint
endpoint children.  Assume (8).  Suppose there are ordinary-face families
\(\mathcal G_L,\mathcal G_R\), of sizes \(K_L,K_R\), such that

\[
 E\cup A\text{ is ordinary for every }
 \begin{cases}
 E\in\mathcal G_L,\ A\subseteq S_L,\\
 E\in\mathcal G_R,\ A\subseteq S_R.
 \end{cases}                                            \tag{10}
\]

The left unions in (10) form a load-one bank of size
\(K_L2^{|S_L|}\): intersecting an output with the two labelled blocks
recovers \(E,A\).  The right bank similarly has size
\(K_R2^{|S_R|}\).  Hence

\[
 \begin{aligned}
 V&\ge\max\{K_L2^{|S_L|},K_R2^{|S_R|}\}\\
  &\ge\sqrt{K_LK_R2^{|S_L|+|S_R|}}
   =\sqrt{2^qK_LK_R},
 \end{aligned}                                         \tag{11}
\]

which proves (2), with no Hall or history loss.

The same proof permits a retained base \(B\) only if every union in (10)
remains ordinary after adjoining \(B\).  That extra phrase is precisely the
live gap.  It cannot be inferred from the separate ordinary-face banks of
the endpoint children.

## 3. Exact rooted anti-alignment

For \(m\ge14\), take the rational child

\[
 P_t=\left(2-\delta t^2,-{1\over5}+\delta t\right),
       \qquad \delta={1\over100m^2},\quad1\le t\le m,   \tag{12}
\]

and roots

\[
                       a=(0,0),\qquad b=(4,0),
                       \qquad c=(0,4).                  \tag{13}
\]

The \(P_t\) form a convex-position child, so all \(2^m\) traces are ordinary.
Every singleton transversal \(\{P_t,b,c,a\}\) is a convex quadrilateral in
one common cyclic order.  Nevertheless, for every \(i<j<k\),

\[
 P_j\in\operatorname{int}\operatorname{conv}
                    \{P_i,P_k,c\}.                     \tag{14}
\]

Thus adjoining \(c\) and either \(a\) or \(b\) kills every child trace of rank
at least three.  Including the empty trace gives (4).  At \(m=14\) the exact
rooted profile counts are

\[
                       C=86,\qquad U=106,
             \qquad CU=9116<16384=2^{14}.               \tag{15}
\]

Even the weaker nonempty counts are \(85,105\).  Therefore the natural
rooted analogue of (1) is false despite rational stretchability, complete
singleton transversals, and a Boolean child.

Projective transformations preserve every assertion above.  Hence this
state may be placed in an arbitrarily small endpoint pocket of a larger
common-root wrapper.  What cannot currently be asserted is that repeated
wrapping preserves a low total face count; that is why (5) is an exact
recursion-interface barrier rather than a claimed construction resolving
the global problem.

## 4. Minimizer consequence and remaining gate

Replacing \(Q\) by an induced least-counterexample child does not repair the
logic of (11): one still needs its ordinary faces to export through the
same retained base.  Deletion minimality gives a lower bound for the
absolute child bank \(H\); it gives no lower bound for the rooted directional
capacities \(C,U\).  Example (12)--(15) already separates those quantities
exponentially for the easiest possible child, a convex polygon.

A global proof can now proceed through exactly one of the following
additional statements.

1. **Root release:** delete/encode the common root or base with
   \(2^{o(q)}\) aggregate load, reducing to Theorem 1.
2. **Rooted export:** prove \(CU\ge H/s^{o(1)}\) on a positive-mass
   minimizer slice, excluding (12)--(15) by a mutation or history
   constraint.
3. **External return:** retain source information in a different physical
   component, so the two one-ended banks are not squared against each
   other.

Without one of these inputs, the source-reuse barrier is stable **inside
one all-rank carrier cell**.  It is not yet a global positive-mass
regression: a canonical fixed-rank slice has an additional
\(\Theta(\sqrt q)\) Boolean-capacity surplus.  The exact global correction
and its middle-face overlap residual are proved in
`FIXED_RANK_BOOLEAN_SOURCE_MIDSHADOW_GATE.md`.

## 5. Verification

`verify_opposite_singleton_return_rooted_antialignment.py` uses exact
rational arithmetic.  It verifies the `q=8` balanced source instance,
including opposite profile product `82^2>=2^8`, and the `m=14` rooted
anti-alignment instance, including all `2^14` child traces and the exact
counts `(86,106)` with product below `2^14`.
