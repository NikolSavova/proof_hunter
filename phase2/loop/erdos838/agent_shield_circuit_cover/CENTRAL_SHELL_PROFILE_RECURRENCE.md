# Central shells force an endpoint-profile bank

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The linear guard-depth construction from
`CENTRAL_ROOT_DEPTH_GUARD_BARRIER.md` cannot be a low-face recursive
wrapper.  Its compensation is a detached endpoint-profile bank which does
not use the root or the external contexts.

Let `t` cyclic macro roles have `A` singleton labels each, and suppose all
one-point-per-role transversals are ordinary.  Fix one role `g`, replace
its label set by an arbitrary `A`-point child `Q`, and write

\[
                         H=V(Q)-1                       \tag{1}
\]


for its nonempty ordinary face count.  In the separated central-shell
realization there is a load-one ordinary bank of size

\[
                         \boxed{B\ge A^{t-2}\sqrt H.}   \tag{2}
\]


Indeed, every child face decomposes into its two directional boundary
profiles, so their counts `L,R` satisfy `LR>=H`.  Omitting the macro role
immediately before or after `g` exposes the corresponding profile as the
endpoint of the remaining macro chain.  Choose the richer side and one
arbitrary singleton in every other retained role.

If every macro role `i` has a child with face count `H_i`, the two endpoint
profiles at one omitted gap give the stronger cyclic theorem

\[
\boxed{
   \max_j B_j\ge
      A^{t-3}\left(\prod_{i=1}^tH_i\right)^{1/t}.}       \tag{3}
\]

This is exactly Theorem 4 of
`agent_common_shield_mixing/DETACHED_RADIAL_LEXICOGRAPHIC_PROFILE.md`:

\[
 \max_jB_j\ge P_0
       \left(\prod_i{H_i\over A^3}\right)^{1/t},
 \qquad P_0=A^t.                                       \tag{3a}
\]

The denominator is `A^3`, not `A^2`: a role is omitted once and serves as
each of the two endpoint profiles once in the cyclic product.  Replacing
`A^3` by `A^2` changes only one factor `A=2^{O(L)}` and not the quadratic
coefficient, but (3a) is the exact finite identity.


The central root, its `1+3` circuits, and any family of external contexts
are absent from these outputs.  Thus no root-context overlap is incurred.

Put `A=2^L`, `t=(alpha+o(1))L`, and

\[
                         \log H=(c+o(1))L^2.            \tag{4}
\]


Equation (2) gives the exact recurrence

\[
                         c_{parent}\ge\alpha+{c\over2}.\tag{5}
\]


At the live source value `alpha=1/4`:

* the universal child bound `c>=1/4-o(1)` already gives `3/8-o(1)` from
  one rich role;
* a coefficient-half projective child gives `1/2-o(1)`; and
* any self-similar fixed point of (5) satisfies `c>=1/2`.

If all roles contain arbitrary `A`-point children, the universal quarter
bound in every child and (3) give directly

\[
                         \boxed{c_{parent}\ge1/2-o(1)}. \tag{6}
\]


Therefore the projective-child version of the central-depth barrier forces
the coefficient-half bank requested in the parent task.  The only version
which lacks this bank is the literal singleton-alphabet model, where each
role has no quadratic internal face reservoir.

For `K=2^{(beta+o(1))L^2}` distinct actual external context faces, the
unmixed context bank gives coefficient `beta`, while (2) gives
`alpha+c/2` independently.  Hence

\[
 {\log V(P)\over L^2}
   \ge\max\left\{\beta,\alpha+{c\over2}\right\}-o(1).  \tag{7}
\]


The separated two-face bank `(context,outer face)` and the formal Cauchy
bound contribute only `(alpha+beta)/2`, never more than
`max{alpha,beta}`.  Thus Hall-dense context entropy alone does not create a
coefficient gain.  What closes the scalable central-shell regression is
the ordinary endpoint-profile bank.

## 1. Directional profile factorization

Fix a generic oriented line through the small child cluster `Q`.  Every
nonempty ordinary child face `F` has two extreme points in that direction.
Its boundary is the union of two directed convex chains with those common
endpoints.  Let `mathcal L` and `mathcal R` be the sets of all chains which
occur on the two sides, counting singletons and pairs with the usual
degenerate convention.

The map

\[
                         F\longmapsto(L(F),R(F))        \tag{8}
\]


is injective: the union of the two chains recovers `F`.  Consequently

\[
                         H\le |\mathcal L||\mathcal R|,
 \qquad
                         \max\{|\mathcal L|,|\mathcal R|\}\ge\sqrt H.  \tag{9}
\]


No cap/cup theorem or regularity input is used here.  The inequality is
exact for every planar order type and every generic direction.

## 2. One-rich-role endpoint bank

Place the child `Q` in a sufficiently small neighbourhood of macro vertex
`g` of a strictly convex `t`-gon.  All other macro roles have disjoint
`A`-point supports and contribute one selected point.

Omit role `g-1`.  In the cyclic order cut at that gap, role `g` is the
first endpoint block.  The lexicographic orientation rules say that every
profile on one side—call it `mathcal L`—together with one point in each of
the other `t-2` occupied singleton roles is an ordinary face.  Omitting
`g+1` exposes `mathcal R` in the reflected way.  Therefore the two banks
have sizes

\[
                   |\mathcal L|A^{t-2},\qquad
                   |\mathcal R|A^{t-2}.                 \tag{10}
\]


Equation (9) proves (2).

The decoder load is one.  The active macro mask identifies which adjacent
gap was used, intersection with the child cluster recovers the directional
profile, and every other cluster intersection recovers its singleton.
The fixed central root and all external-context points are omitted.

This is precisely why the linear root depth is harmless once a rich child
is inserted.  Root release would discard half the macro labels, but the
detached endpoint operation discards one macro role and exposes a square
root of the entire child complex.

## 3. Cyclic two-endpoint theorem

Let child `i` have left and right profile counts `L_i,R_i`, so

\[
                         L_iR_i\ge H_i.                 \tag{11}
\]


Omit macro role `j`.  The two endpoints of the remaining macro chain are
`j-1` and `j+1`.  Taking a right profile in the former, a left profile in
the latter, and one singleton in every other retained role gives a
load-one bank

\[
                         B_j=R_{j-1}L_{j+1}A^{t-3}.      \tag{12}
\]


Multiply (12) over all `j`.  Every `L_i` and every `R_i` appears exactly
once, so

\[
 \prod_jB_j
   =A^{t(t-3)}\prod_iL_iR_i
   \ge A^{t(t-3)}\prod_iH_i.                           \tag{13}
\]


Taking the `t`th root proves (3).  This is a one-face bank, unlike the
separated two-output omit-one-cell construction: both endpoint profiles
belong to the boundary of the same detached macro face.

The geometric hypothesis is genuine lexicographic separation.  An
arbitrary nonseparated occupied-mask system can have the exact `1+3`
profile obstruction from
`DOMINANCE_CELL_SEPARATED_ONE_GAP.md`.  The central-shell barrier is built
from small clusters around a convex macro polygon and therefore is in the
separated regime; it cannot invoke that obstruction.

## 4. Coefficient thresholds

The outer point count is

\[
                         n=tA,\qquad \log n=L+o(L).      \tag{14}
\]


From (2) and (4),

\[
 \log B
   \ge(t-2)L+{1\over2}\log H
   =\left(\alpha+{c\over2}+o(1)\right)L^2,             \tag{15}
\]


which is (5).  The exact thresholds are:

\[
 \begin{array}{c|c}
 \text{target}&\text{sufficient condition}\ \hline
 c_{parent}>1/4&\alpha+c/2>1/4,\\
 c_{parent}\ge1/2&\alpha+c/2\ge1/2.
 \end{array}                                           \tag{16}
\]


At `alpha=1/4`, every fixed positive child coefficient beats the quarter
target; `c=1/4` gives `3/8`, and `c=1/2` gives one half.

For identical child scales in every role, (3) gives

\[
 \log\max_jB_j
     \ge(t-3)L+\log H
     =(\alpha+c+o(1))L^2.                              \tag{17}
\]


The established universal bound `c>=1/4-o(1)` yields (6).  Projectively
universal low-face children therefore make the central shell *more*
expensive, not less.

For a self-similar operation in which only one macro role carries the
recursive child at the quadratic scale, set `c_parent=c_child=c` in (5):

\[
                         c\ge\alpha+c/2,
 \qquad                         c\ge2\alpha.            \tag{18}
\]


This proves the coefficient-half fixed point at `alpha=1/4`.

## 5. Multi-context audit

Let `mathcal C` be `K` distinct actual ordinary context faces in the
central region.  Since `mathcal C` itself is an ambient bank,

\[
                         V(P)\ge K.                     \tag{19}
\]


The detached full-transversal bank gives `V(P)>=A^t`, and (2) gives the
stronger endpoint bank when `H` is quadratic.  These banks are geometric
unions, so they are counted once no matter how many contexts reuse them.

The injection

\[
              \mathcal C\times\mathcal E
                    \longrightarrow\mathcal F(P)^2,
 \qquad       (C,F)\longmapsto(C,F)                    \tag{20}
\]


only implies `V(P)>=sqrt(KM)`.  On the coefficient scale this is
`(alpha+beta)/2<=max{alpha,beta}`, so it adds nothing to the two separate
banks.  A genuine mixed one-face bank would require context directional
profiles compatible with a rooted outer semicircle.  The central-depth
calculation alone does not supply all `K` such profiles.

If the context family is itself one separated child, the same profile
factorization gives at least `sqrt K` compatible chains in one of two
directions.  Combining one such chain with an outer half-shell gives at
most the natural guaranteed coefficient

\[
                         {\alpha+\beta\over2}.           \tag{21}
\]


This is sharp at the level of cap/cup factorization and still equals
`1/4` when `alpha=beta=1/4`.  Thus the context side does not close the
balanced case by itself.  Equations (5)--(6) do.

## 6. Exact finite seam audit

The verifier replaces one role of the exact `t=9` central shell by the
four-point child

\[
 (100001,0),(100002,400),(100003,100),(100004,0).       \tag{22}
\]


It has 14 nonempty ordinary faces.  For either adjacent omitted role,
exact enumeration finds 10 child subsets which splice with **every** one
of the `2^7` choices in the other occupied roles.  Hence each directional
bank has

\[
                         10\cdot2^7=1280                \tag{23}
\]


ordinary faces, exceeding the square-root guarantee
`2^7 sqrt(14)`.  All 21 points including the central root are in general
position.  This directly checks that the central-shell coordinates lie in
the separated endpoint-profile regime.

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_central_shell_profile_recurrence.py
```

The verifier checks the exact 14-face child, both 1280-face adjacent-gap
banks against all singleton completions, general position, the cyclic
product identity on exact integer profile arrays, and the coefficient
thresholds and fixed point.
