# Bad repeated pairs: rank-four rooted circuits and coherent `Pi_q` itineraries

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The linear bad-pair residue from
`MIXED_SEAM_VERTEX_COVER_PI2_GATE.md` has an exact constant-loss local
classification.  Fix the two canonical neighboring representatives around
a role.  Every label-disjoint bad pair gives either

1. a decoded convex rank-four face; or
2. one of four rooted circuits: a pair endpoint is hidden by the neighbor
   triangle, or a fixed neighboring representative is hidden by the pair
   triangle.

The first circuit class is exactly a common-edge dominance/nesting record.
The second is a rooted fan chord crossing a fixed neighbor ray.  Thus a
linear matching can be pigeonholed into one rooted circuit class with only
a constant loss; no rank or pair mark is erased.  Deleting one canonical
neighbor gives a rank-three ordinary face which still contains the entire
bad pair, so the local decoder load is constant.

The convex class is now promoted in
`CONVEX_BAD_PAIR_EAR_PROMOTION.md`: for actual two-label records under the
complete same-type hypothesis it is a genuine commuting boundary ear and
does give the needed scale multiplier.  The earlier broad-cluster
nonseparated-mask obstruction concerns arbitrary multi-point profiles and
does not refute this pair lemma.  Only the four rooted nonconvex classes
still require a fan/one-gap container.

There is a conditional exact economy when one fixed completed child is
genuinely queried in `q` directions.  Such a child cannot choose `q`
projection profiles independently.  Its coherent chamber itinerary is the
evaluation of one profile function on `RP^1`, modulo one `PGL_2`
transformation.  If the child has `N` points, the number of possible
coherent `q`-direction itineraries is only

\[
                         O\bigl((qN^2)^3\bigr).          \tag{1}
\]

Thus fixing a coherent itinerary costs `O(log N+log q)` bits, not
`Theta(q log N)` bits.  This does **not** constrain the basic recursive
wrapper with `q` independent child copies, each queried only at assembly
and at one future reset: those copies have independent projective maps and
legitimate independent `Pi_2` states.  The bound applies only after an
actual history argument localizes four or more direction queries in the
**same** copy.

The rigorous output is therefore a sharpened fork: convex pairs promote to
a commuting ear bank, while the whole unpaid mass is a constant number of
rooted dominance/fan circuit tensors.  Polynomial coherent `PGL_2`
itineraries are available only in the additional same-copy multiquery
setting, not as an unconditional recursive entropy gate.

## 1. Canonical rank-four records

Let

\[
                 B=(x_1,x_2,\ldots,x_q)                 \tag{2}
\]

be a fixed singleton transversal in cyclic macro order.  For a bad pair
`e={a,b} subset X_i`, use the canonical neighboring representatives

\[
                         l_i=x_{i-1},\qquad r_i=x_{i+1}. \tag{3}
\]

At an endpoint role one uses the fixed guard/anchor supplied by the rooted
chart; the cyclic notation avoids a separate case.

Put

\[
                         Q(e)=\{l_i,a,b,r_i\}.           \tag{4}
\]

General position gives exactly one of the following.

* **Convex:** all four points are vertices.  Refine this into the
  pair-adjacent ear type and the alternating/diagonal type if desired; both
  are ordinary rank-four faces.
* **Pair-inner-left/right:** `a` or `b` is in the interior of the triangle
  formed by the other pair endpoint and `l_i,r_i`.
* **Anchor-inner-left/right:** `l_i` or `r_i` is in the interior of the
  triangle formed by the pair and the other anchor.

These five coarse records (convex plus four interior labels), together with
one bit ordering `a,b`, are canonical and exhaustive.

> **Lemma 1 (constant-load local decoder).**  Let `mathcal M_i` be a
> matching of bad pairs in `X_i`.  One of the five classes above contains
> at least `|mathcal M_i|/5` pairs.  Convex records give that many distinct
> rank-four faces.  Circuit records give that many distinct rank-three
> faces
>
> \[
>                         T(e)=\{a,b,r_i\}               \tag{5}
> \]
>
> retaining both pair labels.  Given `T(e)` and the fixed role chart, the
> pair and omitted anchor are recovered; across disjoint role supports the
> global load is at most the constant number of possible role assignments
> to a three-set.

**Proof.**  A nonconvex four-set in planar general position has a unique
interior point, giving the classification and the factor-five pigeonhole.
Every three-set is convex, so (5) is ordinary.  Since the pairs form a
matching and the two pair labels are retained, different records have
different outputs.  QED.

The rank-three output alone is only linear.  Its purpose is to retain the
actual pair mark for a subsequent product/container argument rather than to
claim the required scale multiplier already.

## 2. The two rooted circuit geometries

The circuit classes have more structure than an arbitrary color.

### 2.1 Pair-inner means common-edge dominance

Suppose

\[
                         a\in\operatorname{int}
                              \operatorname{conv}\{l_i,b,r_i\}.     \tag{6}
\]

After sending the line `l_i r_i` to the line at infinity of the standard
two-tangent pocket, the two positive tangent coordinates of `a,b` satisfy
the usual strict dominance/nesting inequalities.  In invariant language,
`a` is the inner label and `b` the outer label over the fixed guard edge
`l_i r_i`.  A matching of such circuits is therefore a matching in the
two-dimensional dominance order, with the repair mark `(a,b)` retained.

This is precisely the common-guard obstruction, not a generic lost
circuit.  A large antichain of the involved endpoints gives a detached
convex directional profile; a large chain is the projective-universal
nested child and must be handled by its coherent direction spectrum.
The matching hypothesis alone does not decide between them.

### 2.2 Anchor-inner means a rooted fan chord

Suppose, for example,

\[
                         l_i\in\operatorname{int}
                              \operatorname{conv}\{a,b,r_i\}.       \tag{7}
\]

The ray from `r_i` through `l_i` exits the triangle through the open segment
`ab`.  Hence every such bad pair is a chord crossing one fixed rooted ray.
Ordering the intersection points along that ray and the endpoints on its
two sides turns the family into the standard two-line/permutation fan.
Erdos--Szekeres on the two endpoint orders extracts nested or crossing
subfamilies with square-root loss, far smaller than any polylogarithmic
loss required here.

What is still missing is a theorem that simultaneous fan choices in many
macro roles form one ordinary face.  Pairwise rank-four convexity or fan
monotonicity does not by itself imply that broad nonadjacent ears commute.

## 3. What the linear residue gives immediately

In the fixed-gap hard branch, a linear number of roles each have
`Omega(A)` label-disjoint bad pairs.  Applying Lemma 1 inside every role
loses only a constant.  Pigeonholing the five types once more across the
roles leaves `Theta(log n)` roles of a common type, still with `Omega(A)`
marked pairs per role.

Consequently, for any fixed `K=(log n)^D`, every surviving role contains a
canonical menu of `K` disjoint records of the same rooted type.  If a
global parity/one-gap lemma made those menus commute in `rho log n` roles,
it would produce

\[
                         K^{\rho\log n}
                     =n^{\rho D\loglog n}              \tag{8}
\]

ordinary faces, exactly the requested scale-recovery multiplier.  Thus no
additional local entropy extraction is needed.  The sole missing statement
is cross-role compatibility of the retained rank-four/fan records.

The distinction matters.  The rational sparse-defect wrapper from the
companion report has a circuit record at every internal role, but the union
of the marked pairs from any three roles is nonconvex.  Hence multiplying
the local menus without a container theorem would be false.

## 4. Coherent `Pi_q` rather than independent `Pi_2`

For an `N`-point order type `P`, let `mathcal D(P)` be its set of critical
projection directions.  It has size at most

\[
                              m={N\choose2}.             \tag{9}
\]

The cap/cup profile is constant on every component of
`RP^1-mathcal D(P)`.  Fix `q` query directions
`d_1,...,d_q` in the ambient wrapper.  A projective re-embedding of this
one child induces one element `g in PGL_2(R)` on its direction line, so its
coherent itinerary is

\[
   \bigl(\operatorname{chamber}(g^{-1}d_1),\ldots,
         \operatorname{chamber}(g^{-1}d_q)\bigr).       \tag{10}
\]

> **Theorem 2 (polynomial coherent-itinerary bound).**  As `g` varies over
> `PGL_2(R)`, the number of itineraries (10) is
>
> \[
>                              O((qm)^3)=O((qN^2)^3).    \tag{11}
> \]

**Proof.**  Represent a direction by homogeneous coordinates and `g` by a
nonzero `2 by 2` matrix modulo scale.  For a critical direction `w` and a
query `d_i`, the wall

\[
                              g(w)=d_i                   \tag{12}
\]

is one homogeneous linear equation in the four matrix entries.  There are
`H=qm` such projective hyperplanes in `RP^3`.  The profile itinerary is
constant in every sign cell after the determinant-zero quadric is removed.
The standard dimension-three hyperplane-arrangement/Milnor--Thom bound,
with one fixed degree-two surface added, gives `O(H^3)` cells.  QED.

For `q=Theta(log N)`, fixing the entire coherent itinerary therefore costs

\[
                         3\log(qN^2)+O(1)=O(\log N)     \tag{13}
\]

bits.  This is negligible both at the quadratic coefficient scale and at
the `Theta((log n)log log n)` recovery scale in (8), provided all the
queries really address one fixed child.

`PGL_2` is three-transitive, so up to three direction values can indeed be
prescribed independently.  Starting with four directions, their cross
ratio is invariant.  This is the first place where a product of independent
`Pi_2` menus becomes a fictitious recursive state.

The theorem concerns several directions queried in the **same copy**.
Different role copies have independent projective embeddings and hence
independent `PGL_2` parameters.  In particular, the ordinary `q`-child
recursive wrapper with two chart queries per copy is not restricted by
Theorem 2.  A proof may use it only after first localizing one completed
copy and retaining that copy through at least four descendant queries.

## 5. Exact remaining container statement

After the constant-loss classification and Theorem 2, the desired positive
step can be stated without hidden entropy:

> Given `Theta(log n)` macro roles, each with a polylogarithmic menu of
> one fixed rooted dominance/fan type, prove that a
> positive fraction of one parity of the menus commute as an ordinary
> one-gap face.

A proof yields (8).  A counterexample must be a scalable broad-cluster
wrapper in which all those marked pair menus remain locally admissible but
every polylogarithmic cross-role product is killed.  Independent `Pi_2`
entries remain legitimate across independent copies.  Only a construction
which reuses the same copy in many directions must additionally satisfy the
coherent-itinerary constraint.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_bad_pair_rank4_piq.py
```

The checker verifies the five-way rank-four classification and retained-pair
decoder on the exact sparse-defect wrapper, realizes each rooted circuit
type over the rationals, checks the fan-ray intersection, and exhausts a
rational sample of `PGL_2` matrices.  It verifies cross-ratio invariance and
that every sampled `q`-direction itinerary lies within the cubic
hyperplane-arrangement bound.
