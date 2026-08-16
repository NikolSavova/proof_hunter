# Blocker roles are circuit vertex covers; their deletion depth can be linear

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

There is an exact characterization of the roles which must be deleted to
release one local face inside a complete same-type product: they form a
vertex cover of a graph of `3+1` and `2+2` circuits.  This gives a clean
local dichotomy.

* If the circuit graph has a small vertex cover, deleting those roles
  releases the face.
* If its minimum cover has size `tau`, the selected blocker roles themselves
  form a detached Boolean bank of size `2^tau`, because they are a subset of
  an ordinary macrotransversal.

The first alternative cannot be bounded independently of the number of
roles.  There is a scalable rational strongly separated family with one
three-point local face and `k` singleton blocker roles for which the exact
deletion depth is `tau=k`.  Every bad circuit is a `3+1` circuit using the
same three local points and one distinct blocker.  Thus a large hitting set
does **not** force crossing `2+2` circuits, disjoint local witnesses, or a
two-ended mixed product.  It forces only the already visible blocker
Boolean shield, and the example attains that alternative exactly.

More generally, with an `m`-point local cap and `k` blocker roles, the full
face count is

\[
 V=2^m+\left(1+m+{m\choose2}\right)(2^k-1).             \tag{1}
\]

There is no `2^{m+k}` mixed product: once a blocker is present, at most two
local cap points may survive.  This is a sharp scalable anti-multiplication
barrier.  It is not a low-face construction for Erdős 838—the two detached
Boolean banks are exponentially large in their actual ranks—but it shows
exactly what a profile-or-deletion theorem can and cannot assert.

## 1. Exact circuit-cover characterization

Let `X_1,...,X_q` be a complete same-type planar product in one convex
cyclic order.  Fix a nonempty ordinary local face `F subseteq X_i` and a
partial transversal

\[
                         T=\{x_j:j\in J\},
       \qquad x_j\in X_j,\quad i\notin J.                \tag{2}
\]

Both `F` and `T` are in convex position.  Define a looped graph
`Gamma(F,T)` on the role set `J` as follows.  For every nonconvex four-set
`C subseteq F union T`, add the external role trace

\[
                         e(C)=\{j:x_j\in C\cap T\}.       \tag{3}
\]

as a loop or an ordinary edge.

Why does (3) always have size one or two?  A circuit cannot lie wholly in
`F` or wholly in `T`, since both are convex.  It also cannot have one point
of `F` and three points of `T`: that four-set chooses at most one point from
each of four distinct blocks and is a subset of a same-type convex
transversal.  Hence every bad circuit splits `3+1` or `2+2` between `F`
and `T`.

> **Theorem 1 (role deletion equals circuit vertex cover).**  For
> `S subseteq J`,
> 
> \[
>        F\cup\{x_j:j\in J\setminus S\}\text{ is convex}
> \quad\Longleftrightarrow\quad
>        S\text{ is a vertex cover of }\Gamma(F,T).       \tag{4}
> \]

**Proof.**  If `S` misses an edge or loop, the corresponding bad four-set
survives, so the remaining union is nonconvex.  Conversely, a nonconvex
finite planar general-position set contains a point in the convex hull of
the others.  Planar Carathéodory gives three other points containing it,
and hence a surviving bad four-set.  Its role trace is an uncovered edge
of `Gamma(F,T)`.  QED.

Write

\[
              \tau(F,T)=\tau(\Gamma(F,T)).               \tag{5}
\]

If `S` is a minimum cover, the `tau` points `{x_j:j in S}` are a subset of
the convex-position set `T`.  Every one of their `2^tau` subsets is an
ordinary face.  Thus

\[
 \boxed{\text{release cost }\tau
        \quad\text{or a detached blocker bank of size }2^\tau.}       \tag{6}
\]

There is also a useful circuit packing certificate.  Let `L` be the set
of looped vertices and let `nu` be a maximum matching after deleting `L`.
A maximal matching's endpoints cover every remaining edge, so

\[
                         \tau\le |L|+2\nu.                \tag{7}
\]

Large deletion depth therefore gives many distinct singleton blockers or
many role-disjoint `2+2` traces.  The construction below shows that the
first case can carry the entire obstruction; planarity does not force the
second.

## 2. A rational linear-depth family

Fix `m>=3` and `k>=2`.  Put

\[
 \delta={1\over100m^2},\qquad
 P_t=\left(2-\delta t^2,-{1\over5}+\delta t\right),
               \quad 1\le t\le m.                       \tag{8}
\]

Let `X_0={P_1,...,P_m}`.  Put `epsilon=1/(100k)` and, for
`1<=s<=k`, set

\[
 u_s=k+1-2s,\qquad
 C_s=\left(\epsilon u_s,4-\epsilon^2u_s^2\right),
 qquad X_s=\{C_s\}.                                    \tag{9}
\]

The cyclic role order is

\[
                         X_0,X_1,\ldots,X_k.              \tag{10}
\]

The `C_s` occur from right to left on the strictly concave parabola
`y=4-x^2`, within distance `1/100` of `(0,4)`.  Every transversal

\[
                         \{P_t,C_1,\ldots,C_k\}           \tag{11}
\]

is convex in the order (10), and all such transversals have the same type.
Here is a direct sign audit.  If `x>y` are two guard abscissae and
`P=(p,q)` is any `P_t`, then

\[
 \operatorname{orient}\bigl(P,(x,4-x^2),(y,4-y^2)\bigr)
       =(x-y)\,[4-q+xy-p(x+y)]>0.                        \tag{12}
\]

The bracket is positive because `|x|,|y|<1/100`, `p<2`, and
`q<-19/100`.  Three guards in the order (10) have determinant

\[
                         (x-y)(y-z)(x-z)>0.               \tag{13}
\]

Thus every increasing role triple has positive orientation.  The union is
in general position: triples of local points or guards lie on strict
parabolas, (12)--(13) handle the mixed `1+2` triples, and for `i<j`

\[
 \operatorname{orient}(P_i,P_j,(x,4-x^2))
 =\delta(j-i)\left[
   2-x-(i+j)\left({21\over5}-x^2\right)+\delta ij
 \right]<0.                                             \tag{14}
\]

Consequently Bárány--Pach Proposition 3.3 makes the blocks strongly
separated.

## 3. Every guard is a mandatory loop

For `i<j<ell`, the three barycentric numerators which express `P_j`
inside

\[
                         \operatorname{conv}\{P_i,P_\ell,C_s\}        \tag{15}
\]

are all negative.  The two numerators involving `C_s` are instances of
(14), and

\[
 \operatorname{orient}(P_i,P_\ell,P_j)
       =\delta^2(\ell-i)(j-i)(j-\ell)<0.                 \tag{16}
\]

The denominator in (15) is also negative by (14), so all barycentric
coordinates are strictly positive.  Therefore

\[
                         P_j\in\operatorname{int}
                             \operatorname{conv}\{P_i,P_\ell,C_s\}.   \tag{17}
\]

Take the full local face `F=X_0` and transversal
`T={C_1,...,C_k}`.  For every guard role `s`, the four-set
`{P_1,P_2,P_3,C_s}` is a `3+1` circuit, so `s` is a loop of
`Gamma(F,T)`.  Every vertex cover contains all `k` roles.  Conversely,
deleting all guards leaves the convex local cap `F`.  Hence

\[
                         \boxed{\tau(F,T)=k=q-1.}          \tag{18}
\]

The deletion depth is linear, all circuits can share the same local
triple, and there need not be even one `2+2` edge.

## 4. Exact full face recurrence

For `A subseteq X_0` and `B subseteq T`, equations (14)--(17) give

\[
 A\cup B\text{ is convex}
 \quad\Longleftrightarrow\quad
 B=\varnothing\ \text{ or }\ |A|\le2.                  \tag{19}
\]

The forward failure for `B nonempty`, `|A|>=3` is (17).  For the converse,
order two selected local points as `P_ell,P_i` with `i<ell`, followed by
the selected guards in their order (10).  Equation (14) gives the first
seam turns, (12) the `P-C-C` turns, and (13) the guard turns; all are
positive, so the displayed simple polygon is convex.  The cases of zero
or one local point are immediate.

There are `2^m` choices with `B` empty.  With `B` nonempty there are
`1+m+binom(m,2)` allowed local traces.  This proves (1).

The formula shows why a hoped-for two-ended multiplication is false here:
the local Boolean reservoir `2^m` and blocker Boolean reservoir `2^k`
coexist only through the rank-two interface.  A global proof must either
charge one detached reservoir, or add geometric hypotheses beyond complete
same type.

## 5. Quantitative use and limitation

At fixed-power scale, (6) is useful without further geometry: if
`tau>=gamma log D`, the blocker bank has size at least `D^gamma`.  If
`tau<gamma log D`, deleting fewer than `gamma log D` roles releases the
chosen face exactly.

At coefficient scale, `q=O(log n)` makes `2^tau` only
`2^{O(log n)}`.  It cannot by itself contribute a quadratic
`(log n)^2` exponent, and (1) prevents replacing it by the formal product
of the two detached reservoirs.  This is the precise remaining aggregate
load issue: the released face or blocker mask must be paired with a
recoverable outer context without reusing the same output over too many
bases.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_blocker_role_hitting_set_barrier.py
```

The exact checker uses `m=6,k=7`.  It verifies general position, all six
same-type convex transversals, all `20*7=140` strict middle-point
containments, the `k=7` mandatory-loop deletion depth, and exhausts all
`2^(m+k)=8192` subsets to certify the recurrence (1).
