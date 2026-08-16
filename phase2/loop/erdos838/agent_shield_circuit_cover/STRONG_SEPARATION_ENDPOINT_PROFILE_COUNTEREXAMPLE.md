# Strong separation does not force endpoint-profile multiplication

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The proposed strong-separation bridge is false, even with four cyclic
blocks, three singleton blocks, rational coordinates, and a convex-position
nontrivial block.

For every `m>=14` there are strongly separated planar blocks
`X_1,X_2,X_3,X_4`, all in general position, such that every transversal is
convex in the common cyclic order, while no two endpoint-profile families
for `X_1` can satisfy both

\[
       |\mathcal L_1|\,|\mathcal R_1|\ge V(X_1)-1                 \tag{1}
\]

and the two omitted-gap convexity requirements.  In fact

\[
 |\mathcal L_1|,|\mathcal R_1|
       \le m+{m\choose2},
 \qquad
 \left(m+{m\choose2}\right)^2<2^m-1=V(X_1)-1.          \tag{2}
\]

The obstruction pinpoints the logical gap in a common-tangent proof:
strong separation controls determinants using points from three distinct
blocks.  An endpoint chain of rank at least three also uses determinants
with two or three points from one block.  Those signs can make an internal
chain vertex hidden even though every singleton transversal has one fixed
cyclic type.

This is a sharp kill of the **geometric implication**, not a low-face global
construction.  The block `X_1` itself has the detached Boolean bank of
`2^m-1` nonempty faces.  Thus the example does not refute a theorem which
allows that absolute local shield to pay; it refutes the claimed
multiplication of that shield through the two cyclic endpoint profiles.

## 1. Rational construction

Fix `m>=14` and put

\[
             \delta={1\over100m^2},\qquad
 P_t=\left(2-\delta t^2,-{1\over5}+\delta t\right),
             \quad 1\le t\le m.                         \tag{3}
\]

Take the cyclic blocks

\[
 \begin{aligned}
 X_1&=\{P_1,\ldots,P_m\},&
 X_2&=\{b\},& b&=(4,0),\\
 X_3&=\{c\},& c&=(0,4),&
 X_4&=\{a\},& a&=(0,0).
 \end{aligned}                                          \tag{4}
\]

All points `P_t` lie in the open wedge

\[
                         x>0,\qquad y<0,\qquad x+y<4.    \tag{5}
\]

Indeed `delta t^2<=1/100`, `delta t<=1/(100m)`, so
`x>=199/100`, `y<-19/100`, and `x+y<2`.  Therefore

\[
 \operatorname{orient}(P_t,b,c)>0,\qquad
 \operatorname{orient}(P_t,b,a)>0,\qquad
 \operatorname{orient}(P_t,c,a)>0.                     \tag{6}
\]

Every transversal has the positive rank-three sign vector on the four
role triples.  It is consequently a strictly convex quadrilateral in role
order `(1,2,3,4)`.  Equivalently, all transversals have the same type, so
Bárány--Pach, Proposition 3.3, says that the four blocks are strongly
separated.

For completeness, the union is in general position.  Three `P` points
are noncollinear because they lie on a strict parabola.  For `i<k` and a
guard `g=(g_x,g_y)`, direct calculation gives

\[
 \operatorname{orient}(P_i,P_k,g)
  =\delta(k-i)\left[
      2-g_x-(i+k)\left(g_y+{1\over5}\right)+\delta ik
    \right].                                             \tag{7}
\]

For `g=c` the bracket is negative; for `g=b` it is negative;
for `g=a` it is nonzero (the only vanishing integer part is `i+k=10`,
where the remaining term is `delta ik>0`).  Equations (6)--(7), together
with the noncollinearity of `a,b,c`, cover every triple.

The points `P_t` lie on the strictly concave graph

\[
                    x=2-{(y+1/5)^2\over\delta}.          \tag{8}
\]

They are in convex position.  Every nonempty subset is therefore an
ordinary local face, and

\[
                         V(X_1)-1=2^m-1.                 \tag{9}
\]

## 2. Every triple is killed by the same guard

Let `1<=i<j<k<=m`.  Write

\[
             D=\operatorname{orient}(P_i,P_k,c).
\]

Equation (7) gives

\[
 D=\delta(k-i)left[
       2-{21\over5}(i+k)+\delta ik
     \right]<0.                                         \tag{10}
\]

Also

\[
 \operatorname{orient}(P_i,P_k,P_j)
       =\delta^2(k-i)(j-i)(j-k)<0.                       \tag{11}
\]

The other two barycentric numerators are
`orient(P_j,P_k,c)<0` and `orient(P_i,P_j,c)<0`, by the
same formula (10).  Dividing these three negative numerators by `D`
shows that all three barycentric coordinates are positive.  Hence

\[
                    P_j\in\operatorname{int}
                       \operatorname{conv}\{P_i,P_k,c\}. \tag{12}
\]

It follows that, for every trace `G subseteq X_1` with `|G|>=3`,

\[
                         G\cup\{c\}\quad\text{is not convex}.        \tag{13}
\]

Adding more points cannot make the hidden `P_j` extreme, so both
`G union {a,c}` and `G union {b,c}` are nonconvex as well.

## 3. Failure of the omitted-gap bridge

Use indices modulo four.  In the proposed bridge, omit block `X_2`.
The endpoints are `X_1` and `X_3`, and the only other retained block is
`X_4`.  Since the latter two are singletons, every
`R in mathcal R_1` would have to satisfy

\[
                         R\cup\{c,a\}\quad\text{convex}.              \tag{14}
\]

Equation (13) forces `|R|<=2`.

Next omit `X_4`.  The endpoints are `X_3` and `X_1`, while `X_2` is the
other retained block.  Every `L in mathcal L_1` would have to satisfy

\[
                         L\cup\{c,b\}\quad\text{convex},              \tag{15}
\]

so again `|L|<=2`.  Therefore

\[
 |\mathcal L_1|,|\mathcal R_1|
       \le S_m:=m+{m\choose2}={m(m+1)\over2}.            \tag{16}
\]

At `m=14`,

\[
                 S_m^2=105^2=11025<16383=2^{14}-1.      \tag{17}
\]

Moreover `(S_(m+1)/S_m)^2=((m+2)/m)^2<2` for `m>=14`,
whereas the right side doubles up to the harmless `-1`; thus the strict
inequality persists for every `m>=14`.  Equations (9), (16), and (17)
contradict (1).

Even if an endpoint formalism permits the empty trace, the upper bound is
`(S_m+1)^2`; at `m=14` this is `11236<16383`, and the same argument still
kills the bridge.

## 4. Exact scope and consequence

The same-type/strong-separation reduction remains valid:

\[
 \text{all transversals convex in one labelled cyclic order}
 \quad\Longrightarrow\quad
 \text{strong separation}.                              \tag{18}
\]

What fails is the next arrow

\[
 \text{strong separation}
 \quad\not\Longrightarrow\quad
 \text{two endpoint profile families multiplying }V(X_i)-1.          \tag{19}
\]

The common-tangent fan does provide macro supporting directions, but an
edge of a local face need not support the macro block or the other blocks.
In this construction the fixed guard `c` sees every three-point local
chain as nonconvex, despite the complete singleton product having one
order type.  Sending a macro tangent to infinity therefore does not turn
an arbitrary child into a cap-first/cup-last strong glue.

Any coefficient-half argument using endpoint multiplication needs an
additional hypothesis, for example an actual lexicographic/radial
containerization whose directional profile recurrence is already known.
Strong separation alone cannot supply it.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_strong_separation_endpoint_profile_counterexample.py
```

The checker uses exact `Fraction` arithmetic at `m=14`.  It verifies full
general position, the common positive type and convexity of all 14
transversals, all `2^14-1` local faces, all 364 strict middle-point
containments, the failure of every rank-at-least-three endpoint trace in
both omitted-gap contexts, and the numerical profile deficit.

