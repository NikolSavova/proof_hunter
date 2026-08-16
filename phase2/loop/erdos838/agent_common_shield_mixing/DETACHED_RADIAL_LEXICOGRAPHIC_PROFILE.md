# Detached radial clusters: projective universality and the one-gap profile shield

**Date:** 2026-08-14.  All logarithms are base two.

## Verdict

Convex-cluster rigidity is false.  A cluster can have an arbitrary planar
order type while remaining totally nested behind one fixed guard edge.  In
particular there is an exact four-point nested cluster with one point inside
the triangle of the other three.  Putting projectively universal copies in
the radial-cluster regression preserves both:

1. every transversal (one point per macro cluster) is convex; and
2. every two distinct transversals have a detached bad circuit using the two
   differing points and the selected points in the adjacent clusters.

Nevertheless this does **not** produce a low-face detached counterexample.
The full lexicographic face recurrence has a one-gap term.  If cluster `i`
has size `L_i`, nonempty face count `H_i`, and its two directional chain
profiles have sizes `A_i,R_i`, then

\[
                         A_iR_i\ge H_i.                     \tag{1}
\]

Deleting one macro cluster `j`, use a right chain in cluster `j-1`, a left
chain in cluster `j+1`, and one point in every other cluster.  This gives an
ordinary detached bank of size

\[
 B_j=R_{j-1}A_{j+1}
             \prod_{i\notin\{j-1,j,j+1\}}L_i.             \tag{2}
\]

Writing `P_0=product_i L_i`, cyclic multiplication gives the exact Kraft
identity

\[
 \prod_j{B_j\over P_0}
       =\prod_i{A_iR_i\over L_i^3}
       \ge\prod_i{H_i\over L_i^3}.                         \tag{3}
\]

Consequently

\[
 \boxed{\max_j B_j\ge
     P_0\left(\prod_i{H_i\over L_i^3}\right)^{1/q}.}       \tag{4}
\]

For any transversal family of size `M<=P_0`, the universal planar reservoir
`log H_i >= (1/8-o(1))(log L_i)^2` and Jensen imply that quadratic entropy
`log M=Omega((log D)^2)`, `q=O(log D)`, makes the multiplier in (4)
`2^{Omega((log D)^2)}`.  It therefore pays `D^2M` with enormous room.

Thus an arbitrary/projectively universal replacement exists, but the
**radial lexicographic product is still automatically discharged**.  The
strict detached residue must fail to admit this recoverable cyclic
containerization, or must merge the same untagged one-gap bank across many
different common bases.  Low local face count alone is not an obstruction.

## 1. Every order type is a totally nested cluster

Normalize a guard edge to

\[
                         u=(-1,0),\qquad v=(1,0).           \tag{5}
\]

For a point `z=(s,y)` below the edge, put

\[
             L(z)={1+s\over-y},\qquad
             R(z)={1-s\over-y}.                            \tag{6}
\]

The inverse map is

\[
        (L,R)\longmapsto
        \left({L-R\over L+R},-{2\over L+R}\right).         \tag{7}
\]

For two points in the edge pocket,

\[
 z\in\operatorname{int}\operatorname{conv}\{u,v,z'\}
       \quad\Longleftrightarrow\quad
                 L(z)>L(z'),\ R(z)>R(z').                  \tag{8}
\]

> **Theorem 1 (projectively universal nested cluster).**  Let `S` be any
> finite planar general-position order type.  There is a projective image
> `Z` of `S` below `uv` such that both `L` and `R` strictly increase in one
> common ordering of `Z`.  The image can be placed in an arbitrarily small
> prescribed neighbourhood inside the pocket.

**Proof.**  Choose independent affine linear functionals `f,g` on the
original realization, with the values of `f` distinct.  After relabelling,
`f(z_1)<...<f(z_k)`.  Fix positive `L_0,R_0` for a point in the desired
neighbourhood and put

\[
 \begin{split}
 L_i&=L_0+\epsilon f(z_i)+\epsilon^2g(z_i),\\
 R_i&=R_0+\epsilon f(z_i)-\epsilon^2g(z_i).                 \tag{9}
 \end{split}
\]

For sufficiently small positive `epsilon`, all coordinates are positive
and both sequences are strictly increasing.  The map from the original
affine coordinates to `(L_i,R_i)` is invertible affine, and (7) is
projective.  All projective denominators have one sign, so the labelled
order type and all of its convex subsets are preserved.  Letting `epsilon`
tend to zero places the image arbitrarily close to the point corresponding
to `(L_0,R_0)`.  Equations (8)--(9) prove total nesting.  QED.

The following exact instance already kills convex-cluster rigidity:

\[
 (L_i)=(92,61,22,11),\qquad (R_i)=(80,52,35,5).             \tag{10}
\]

Both coordinates decrease, so the four points from (7) are totally nested.
They are in general position, but the second point is strictly inside the
triangle of the other three.

## 2. Projectively universal radial regression

Take a strictly convex macro `q`-gon `v_0,...,v_(q-1)`.  Around every
`v_i`, use Theorem 1 to place an arbitrary order type `S_i` in a sufficiently
small neighbourhood, with nesting measured against the adjacent macro
vertices `v_(i-1),v_(i+1)`.  Shrink successively so that the same strict
containment remains true when those two vertices are replaced by arbitrary
points of their neighbouring clusters.

> **Theorem 2 (arbitrary-order-type radial blow-up).**  The clusters can be
> chosen in rational general position so that every transversal is convex.
> If two transversals differ in cluster `i`, their union is nonconvex: the
> inner of the two differing points lies strictly inside the triangle made
> by the outer point and the two selected adjacent-cluster points.

**Proof.**  A singleton chosen in every sufficiently small macro
neighbourhood is a perturbation of the strictly convex macro polygon, so it
is convex.  Total nesting and the successive shrinking make the stated
triangle containment uniform over all choices in the adjacent clusters.
All conditions are finitely many open strict orientation inequalities;
hence a generic rational perturbation preserves them and gives general
position.  QED.

The circuit is wholly contained in the two transversals.  Thus this is an
exact regression against any claim that detached pairwise incompatibility
forces an individual cluster to be convex or to have a large Boolean bank.

## 3. The full lexicographic face recurrence

The regression has more faces than its transversal layer.  Here is the
exact bookkeeping in the infinitesimal blow-up.  For a nonempty active
macro-index set `I`, write `i^-` and `i^+` for the preceding and succeeding
members of `I` in cyclic order.  Let

\[
              E_i(i^-,i^+)                                \tag{11}
\]

be the number of nonempty local subsets of `S_i` exposed as a convex
boundary chain between the two limiting support directions from
`v_(i^-)` and `v_(i^+)`.  For `I={i}`, interpret this number as the complete
nonempty face count `H_i=V(S_i)-1`.

> **Theorem 3 (lexicographic recurrence).**  For a sufficiently separated
> rational blow-up,
> \[
> V(P)=1+\sum_{\varnothing\ne I\subseteq[q]}
>       \prod_{i\in I}E_i(i^-,i^+).                        \tag{12}
> \]

**Proof.**  The set of occupied macro clusters is recovered from a face.
Fix it as `I`.  At the infinitesimal scale, the two intercluster supporting
lines incident with cluster `i` converge to the directions from its two
cyclic neighbours in `I`.  Every selected local point remains a global hull
vertex exactly when the local trace is one of the exposed chains counted by
(11).  These conditions are independent between the disjoint clusters.
Thus the faces with active set `I` are the Cartesian product of the local
profile families, giving the product in (12).  There are finitely many
subsets and orientation signs, so the limiting equivalence holds for all
sufficiently separated positive rational scales.  Summing the disjoint
active-set classes and adding the empty face proves (12).  QED.

This is a genuine recurrence, not merely an upper bound.  It explains why
replacing one cluster by a low-face order type is not the end of the count:
the directional boundary profiles multiply across macro gaps.

## 4. One missing cluster forces profile alignment

Fix a generic local direction.  Every nonempty convex face `C` of `S_i`
is recovered from its two directed boundary chains between the two extreme
vertices.  Let `mathcal A_i,mathcal R_i` be the families of chains which can
occur on the two sides, and put `A_i=|mathcal A_i|`,
`R_i=|mathcal R_i|`.  The boundary-pair encoding is injective, hence (1).

In the radial blow-up, omit macro cluster `j`.  A member of
`mathcal R_(j-1)` and a member of `mathcal A_(j+1)` face the resulting gap;
one arbitrary point is retained in every other cluster.  The
lexicographic recurrence, or directly the two support chains around the
macro hull, shows that all these sets are ordinary and their traces recover
every choice.  This proves (2).

Multiplying (2) after division by `P_0` proves (3), because every `L_i`
appears exactly three times in the cyclic denominators: once as the omitted
cluster and once as each endpoint.  Taking a geometric mean proves (4).

For the asymptotic consequence, put `d=log D`, assume

\[
             \log M\ge a d^2,qquad q\le\kappa d,           \tag{13}
\]

and delete unused container labels, so `P_0>=M`.  Write
`s_i=log L_i` and `bar s=q^{-1}sum_i s_i`.  Then

\[
                     \bar s={\log P_0\over q}
                         \ge {a\over\kappa}d.               \tag{14}
\]

The universal planar reservoir, with a harmless weakening of its constant,
gives for every `L_i>=2`

\[
        \log(H_i/L_i^3)\ge {s_i^2\over9}-3s_i-O(1).        \tag{15}
\]

Jensen and (14) turn the logarithm of the multiplier in (4) into

\[
 {1\over q}\sum_i\log(H_i/L_i^3)
      \ge {\bar s^2\over9}-3\bar s-O(1)
      =\Omega(d^2).                                        \tag{16}
\]

It dominates every fixed power of `D`, including the `D^2` record factor.
This proves the claimed automatic payment of every recoverable radial
container product.

## 5. Exact remaining boundary

Theorem 1 proves that fixed-edge nesting itself is projectively universal;
there is no individual-cluster rigidity theorem.  Theorems 3--4 prove that
the **cyclic radial product** is rigid at the profile level: deleting one
macro coordinate aligns the two directional profiles, and cyclic
multiplication prevents every gap from being simultaneously small.

Therefore a surviving detached family must lack at least one of:

1. a common recoverable cyclic list of containers;
2. the lexicographic separation which makes (12) factor; or
3. global recoverability of the one-gap bank after the common base is
   erased.

The third item is still the cross-base summation issue.  Within one radial
completion fibre, arbitrary low-face replacements do not survive.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_detached_radial_lexicographic.py
```

The checker constructs a rational `q=5`, four-point-per-cluster blow-up.
Each local cluster has one nonconvex four-set, all 1,024 transversals are
convex, and every distinct-level pair has the required detached adjacent-root
circuit.  Exhausting all `2^20` subsets gives `V=7,605` and verifies the
Cartesian factorization in (12) for all 31 nonempty active patterns.  The
five one-gap banks have size 400 and audit (1)--(4) exactly.
