# Dense fixed rows: core pruning and orthogonal-array rigidity

## Status

This note isolates two exact facts about a dense fixed row

\[
 d=(u-v)+J(x-y).                                      \tag{0.1}
\]

The first is a pruning lemma: a superlinear row contains a four-partite
pair-linear core in which every surviving role-label is used many times.  The
second is a genuinely Euclidean obstruction: that core can never become a
full transversal design.  More generally, the centered coordinate functions
of the four roles certify a large pairwise correlation in at least one of the
six projection graphs.

These facts do **not** yet prove the desired `k^(3/2+o(1))` fixed-row bound or
the global fourth-moment theorem.  Their value is that they formally separate
the sparse/fresh-endpoint examples from the dense endpoint-reuse branch and
identify a quantitative inverse target: a dense core must remain strongly
non-quasirandom in one of its six two-role projections.

## 1. Pair-linear row hypergraph

Let `A` be a distance-Sidon set of `k` planar points.  Give four disjoint role
copies of `A` the names `U,V,X,Y`, and let `H_d` have one hyperedge
`(u,v,x,y)` for every solution of (0.1), with the usual nonzero and transverse
conditions.  As proved in `TRANSVERSE_FIXED_ROW_C4_GATE.md`, every pair of
roles determines the entire relation.  Thus `H_d` is a four-partite linear
four-graph and all six pair projections are simple bipartite graphs.

Write

\[
 r=|H_d|.                                             \tag{1.1}
\]

### Dense-core pruning lemma

There is a subhypergraph `H'_d` with at least `r/2` edges such that every
nonisolated role-vertex of `H'_d` has degree at least

\[
 \tau={r\over 8k}.                                   \tag{1.2}
\]

Indeed, repeatedly delete a role-vertex whose current degree is less than
`tau`, together with its incident edges.  There are at most `4k` deletion
events.  At each event fewer than `tau` previously surviving edges disappear,
so fewer than

\[
 4k\tau=r/2                                          \tag{1.3}
\]

edges are deleted in total.  When the process stops, every remaining
nonisolated vertex has the required degree.

Consequently, if `r>=k^(1+epsilon)`, the surviving core has minimum role-degree
at least `k^epsilon/8`.  The six-biclique obstruction from
`FIXED_ROW_LONGEST_BOOK_GATE.md` lies outside this branch: its intended
relations use fresh auxiliary labels of degree one and its row size is only
linear in the total number of points.

## 2. Full transversal designs are impossible

The natural dense model for a four-partite linear four-graph is a transversal
design.  Let the four role sets have the same size `q>1`, and suppose `H_d`
has `q^2` edges and every projection to two roles is the complete bipartite
graph.  Equivalently, a uniformly random edge

\[
 (U,V,X,Y)                                           \tag{2.1}
\]

is an orthogonal array of strength two: each of the six pairs of role labels
is independent and uniform.

Regard `U,V,X,Y` now as their actual vectors in the plane.  Taking expectations
in (0.1) and subtracting gives

\[
 U_0-V_0+JX_0-JY_0=0,                               \tag{2.2}
\]

where each subscript-zero variable is centered.  Square (2.2) and average.
Every mixed inner product vanishes because the corresponding two role labels
are independent and centered.  Since `J` is orthogonal,

\[
 0=\mathbb E|U_0|^2+\mathbb E|V_0|^2
   +\mathbb E|X_0|^2+\mathbb E|Y_0|^2.              \tag{2.3}
\]

All four variances are therefore zero.  Every role set is a single repeated
point, contradicting `q>1`.  Hence:

\[
 \boxed{\text{No nontrivial full four-role transversal design can occur in a
 fixed row.}}                                        \tag{2.4}
\]

This obstruction uses the planar vector equation itself; pair-linearity alone
allows arbitrarily large transversal designs.

As a concrete subfamily, for a finite abelian group `G` and an automorphism
`lambda` with `lambda-1` invertible, the table

\[
 (U_a,V_b,X_{a+b},Y_{a+\lambda b}),\qquad a,b\in G,  \tag{2.5}
\]

cannot satisfy (0.1) with distinct labels.  A direct finite-difference proof
also works: mixed differences make the second differences of `X` and `Y`
constant; summing over the finite group makes those constants zero; maps from
the finite group to the torsion-free plane then have no nonconstant affine
part.  The exact rank checks in
`verify_dense_core_orthogonal_array.py` certify the cyclic cases `q=3,5,7`.

## 3. Quantitative covariance certificate

The same calculation survives without exact pairwise independence.  Choose a
uniform random edge of an arbitrary nonempty fixed row and center its four
coordinate vectors.  Put

\[
 S=\mathbb E|U_0|^2+\mathbb E|V_0|^2
   +\mathbb E|X_0|^2+\mathbb E|Y_0|^2.              \tag{3.1}
\]

Expanding (2.2) shows that six signed pair-covariances have total absolute
contribution at least `S/2`.  Therefore at least one pair of roles `P,Q`
satisfies

\[
 \left|\mathbb E\langle P_0,TQ_0\rangle\right|
 \ge {S\over12},                                    \tag{3.2}
\]

where `T` is one of `I,-I,J,-J`, depending only on the pair.  In particular,
unless every role is concentrated at one point, one of the six projection
graphs has a coordinate test function witnessing a large nontrivial
correlation.  A quasirandom projection in every pair is impossible.

Equation (3.2) is only an inverse certificate, not yet a counting theorem.
It has an exact spectral consequence.  Give a pair projection its edge-uniform
joint distribution and its two degree-weighted marginal distributions.  Let
`rho(P,Q)` be its maximal correlation, equivalently the second singular value
of the degree-normalized bipartite adjacency operator.  Vector-valued
functions obey the same operator bound as scalar functions, so

\[
 \left|\mathbb E\langle P_0,TQ_0\rangle\right|
 \le \rho(P,Q)
      \sqrt{\mathbb E|P_0|^2\,\mathbb E|Q_0|^2}.   \tag{3.3}
\]

For the pair supplied by (3.2), the square root on the right is at most
`S/2`.  Hence

\[
 \boxed{\max_{P<Q}\rho(P,Q)\ge {1\over6}}.          \tag{3.4}
\]

Thus every noncollapsed fixed row has a quantitatively non-quasirandom pair
projection.  A full transversal design has `rho=0` in every pair, recovering
(2.4).

There is an exact degree-only version.  If `G` is a simple pair projection,
with endpoint degrees `d(a)` and `d(b)`, the squared Frobenius norm of its
degree-normalized adjacency matrix is

\[
 \sum_{ab\in E(G)}{1\over d(a)d(b)}.                \tag{3.5}
\]

Its top singular value is one.  Consequently (3.4) implies that some pair
projection satisfies

\[
 \boxed{\sum_{ab\in E(G)}{1\over d(a)d(b)}
        \ge 1+{1\over36}.}                         \tag{3.6}
\]

This is the chi-squared divergence of the edge-uniform joint distribution
from the product of its degree marginals.  For a biregular graph of density
`p` it equals `1/p`, so (3.6) gives `p<=36/37`.  In the irregular case the
same formula identifies the low-degree or component concentration that must
carry the non-quasirandomness.  A dyadic almost-regularization followed by a
recursive use of (3.6) is a concrete possible density-increment mechanism;
no power-saving recurrence has yet been proved.

This spectral gap is only an inverse certificate, not yet a counting theorem.
To reach the fixed-row `k^(3/2+o(1))` scale, one needs to turn its large
coordinate correlation into either

1. a density increment on smaller role subsets, iterated until (2.4) applies;
   or
2. a radial collision between two actual edges of `A`.

Generic hypergraph regularity does not automatically give the required power
scale, and exact coordinates can cluster arbitrarily closely outside the
integer-grid specialization.  These are the two unresolved quantitative
steps.

## 4. Correct restart point

For a row with `r<=k^(1+o(1))`, the trivial `C_4<=r^2` estimate is already
globally harmless.  For a row with `r>=k^(1+epsilon)`, first pass to the core
of Section 1.  The next proof should use (3.2) as a density-increment or
radial-inverse input.  Do not return to uniform longest-edge charges, Hall
matchings, or a purely pair-linear forbidden-subgraph claim: the first two are
false, while abstract pair-linear transversal designs exist.
