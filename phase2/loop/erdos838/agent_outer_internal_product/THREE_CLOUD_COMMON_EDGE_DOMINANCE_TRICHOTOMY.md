# Three-cloud terminal rectangles: mixed faces or a common-edge dominance cage

**Date:** 2026-08-15.  All logarithms are base two.  This continues
`RANK_HEAVY_GENERALIZED_KK_AND_FOUR_LOCAL_BARRIER.md` and uses the
two-cell localization in
`../agent_common_shield_mixing/PLANAR_SINGLETON_TERMINAL_TWO_CELL_UNIVERSAL_CAGE.md`.
Put

\[
 a=\log_2 3,
 \qquad \theta_*=2-a=0.415037499\ldots .                 \tag{1}
\]

## Verdict

There is an exact signed-planar replacement for the abstract all-delete
rectangle in the common-edge branch.  Fix a convex carrier face `B` with
exposed edge `g=uv`, and put two trace supports `X,Y` in the insertion
cell of `g`.  In the two tangent coordinates at `u,v`,

\[
 B\cup\{x,y\}\text{ is convex}
 \quad\Longleftrightarrow\quad
 x,y\text{ are incomparable in the product order}.      \tag{2}
\]

Thus a three-cloud mixed bank is exactly an incomparability bank.  Its
outputs retain the carrier and both physical trace labels, so the decoder
load is one.  At the nested-cloud scale, carrier mass `H` and two
macroscopic supports give `HR^2` candidates.  Since the target is

\[
                         K=H R^{a+o(1)},                 \tag{3}
\]

an incomparability density `R^{-theta_*+o(1)}` closes.  Failure forces
`1-R^{-theta_*+o(1)}` of the weighted records to be comparable; after one
orientation bit, at least half of this mass is one coherent fixed-edge
dominance direction.  This is precisely the common-edge carrier cage/profile
state requested by the terminal trichotomy.

Together with insertion-cell localization this gives the following exact
strong-terminal reduction.  After a constant cell loss, two trace clouds
against the same carrier are in one of three states:

1. their chosen cells are nonadjacent, and every cross pair is a good
   commuting-ear union;
2. their chosen cells agree, and (2) gives either the target mixed bank or
   a common-edge dominance cage; or
3. their chosen cells are distinct and adjacent, which is a literal
   adjacent two-cell/common-vertex carrier cage.

The last two concentrated states are real.  The affine universal cage
puts an arbitrary labelled order type, partitioned into any three named
clouds, into one total tangent-dominance chain.  Every cross-cloud pair is
then bad with every face of an exponential common-edge carrier alphabet.
This is a stretchable, metadata-free saturation with incomparability
density zero.  Its known lower-parabola carrier has endpoint surplus
`Theta(h^2)`, which exceeds `h^a`; hence it is the concentrated endpoint
alternative, not a counterexample to a low-surplus trichotomy.

The result does **not** close coefficient one half.  It proves that signed
circuit elimination removes the arbitrary four-local regression but
cannot eliminate the common-edge cage.  The exact remaining theorem is a
live, rank-safe, low-endpoint-surplus exclusion of that cage (and its
adjacent-cell/`1+3` analogues), or a minimizer mutation decreasing the
carrier profile.

## 1. Tangent dominance is exactly the signed circuit

Let `B` be a strictly convex face and let `g=uv` be one of its boundary
edges.  Its open insertion cell consists of the points `x` for which
`B union {x}` is convex and `g` is the edge replaced by the two new edges
through `x`.  Apply a projective chart sending

\[
                         u=(-1,0),\qquad v=(1,0),         \tag{4}
\]

with the carrier below `uv` and the insertion cell above it.  Define the
two positive tangent coordinates

\[
             L(x)={x_y\over1+x_x},\qquad
             R(x)={x_y\over1-x_x}.                      \tag{5}
\]

Their invariant meaning is the ordered pair of slopes/distances of the
two rays `ux,vx`; changing the normalized chart applies monotone
reparametrizations and does not change comparability.

### Lemma 1 (same-edge signed compatibility)

For distinct `x,y` in the insertion cell of `g`, exactly one of the
following occurs.

* If `L(x)<L(y)` and `R(x)<R(y)`, then
  `x in int conv{u,v,y}` and `B union {x,y}` is nonconvex.
* If both inequalities are reversed, `y` is hidden by `uvx` and the union
  is nonconvex.
* If the two coordinate orders disagree, both points are vertices of the
  completed hull and `B union {x,y}` is convex.

Equivalently, (2) holds.

**Proof.**  The strict fixed-edge containment criterion says

\[
 x\in\operatorname{int}\operatorname{conv}\{u,v,y\}
 \quad\Longleftrightarrow\quad L(x)<L(y),\ R(x)<R(y).    \tag{6}
\]

It follows either by solving the three barycentric coordinates in (4),
or by intersecting the rays from `u` and `v` with the two sides of the ear
triangle.  In the two comparable cases (6) gives the unique hidden point.
If the orders disagree, the upper boundary from `u` to `v` visits both
points, in the order selected by either tangent coordinate.  All old
carrier support inequalities except the one at `uv` are unchanged, so
every old carrier vertex and both new points remain extreme. `square`

This is signed rank-three information.  An arbitrary bad-four hypergraph
has no product order and is not subject to (2).

## 2. Global weighted mixed-bank/cage dichotomy

Let `C` be a family of canonical carrier contexts.  A context `c` retains

\[
             (B_c,g_c,X_c,Y_c,w_c),                     \tag{7}
\]

where `B_c` is an ordinary carrier face, `g_c` is an exposed edge,
`X_c,Y_c` lie in its insertion cell, and `w_c>=0`.  The two trace supports
belong to disjoint physical clouds.  Put

\[
 \begin{aligned}
 P&=\sum_c w_c|X_c||Y_c|,\\
 G&=\sum_c w_c\,|\{(x,y)\in X_c\times Y_c:
                       x\parallel y\}|,                 \tag{8}
 \end{aligned}
\]

where `x parallel y` means tangent-incomparable.  Let `Lambda` be the
maximum total weight of contexts producing one physical triple
`(B_c,x,y)`.  (For one canonical context per physical carrier face,
`Lambda=1`.)

### Theorem 2 (mixed bank or oriented dominance tensor)

The good unions in (8) obey

\[
                         G\le\Lambda V(P),               \tag{9}
\]

and hence `V(P)>=G/Lambda`.  If `G<rho P`, then comparable records have
weight greater than `(1-rho)P`; one of the two orientations

\[
       L(x)<L(y),R(x)<R(y),\qquad
       L(y)<L(x),R(y)<R(x)                               \tag{10}
\]

has weight greater than `(1-rho)P/2`.

**Proof.**  By Lemma 1, every incomparable record maps to the ordinary
face `B_c union {x,y}`.  The physical cloud partition recovers `B_c,x,y`
from this output; all remaining context reuse is exactly `Lambda`.  This
proves (9).  The complement of incomparability is comparability, and the
two strict orientations in (10) partition it. `square`

At the live scale, suppose

\[
 P\ge H R^{2-o(1)},\qquad \Lambda=R^{o(1)},qquad
 K=H R^{a+o(1)}.                                        \tag{11}
\]

If `V(P)<K`, (9) forces

\[
 {G\over P}<R^{-(2-a)+o(1)}=R^{-\theta_*+o(1)}.          \tag{12}
\]

Thus more than `1-R^{-theta_*+o(1)}` of the literal carrier--trace
records lie in a signed dominance tensor, and one direction carries
asymptotically at least half.  Equation (12) is the exact place where the
three-cloud constant `2-log_2 3` enters; there is no polynomial decoder
loss hidden in it.

## 3. Splice to terminal `1+3/2+2` circuits

Run the fixed-label deletion forest on one bad trace--carrier pair and
look at its last bad residual.

* If the next residual is empty, the last circuit has one trace label and
  three carrier labels.  This is a literal signed `1+3` carrier-triangle
  cage.
* If the last bad residual is `{x,y}` and deletion of `y` leaves the good
  singleton `{x}`, its chosen circuit either uses only `y` on the trace
  side, again a `1+3` cage, or uses both `x,y` and two carrier labels, a
  `2+2` circuit.  If `B union {y}` is bad, `y` also has a `1+3` circuit;
  otherwise both endpoints are insertion ears and the `2+2` relation is
  strong.

Hence, after charging every bad singleton to the `1+3` branch, the
remaining pair branch has both singleton completions ordinary.  Ears on
nonadjacent edges commute.  Therefore every bad pair uses equal or
adjacent insertion edges.

For a strong terminal support (all its relevant singleton completions are
good and all selected pairs are bad), the insertion-edge set is contained
in two equal/adjacent cells (`three` only for a triangular carrier).
Choose the heavier cell in each of two trace clouds.  This costs at most
four (nine for a triangle).  If the chosen cells are nonadjacent, all
cross-cloud pairs commute and give good mixed unions.  If they agree,
Theorem 2 applies.  If they are distinct and adjacent, the records have
already localized to one physical common-vertex/two-cell carrier cage.

This exhausts the signed strong-terminal geometry.  A mere deterministic
path ending at a singleton does not assert that every unvisited pair is
strong; the theorem must be applied after the usual strong/weak terminal
split.

## 4. Sharp stretchable saturation

The common-edge dominance conclusion cannot be improved using planarity
alone.  Start with any finite general-position order type `Q`, with any
partition into named trace clouds.  After a generic affine preprocessing,
write its points as `(a_i,b_i)` with distinct `a_i`, and set

\[
 p_i=(\varepsilon a_i,
       1+3\varepsilon a_i+\varepsilon^2b_i)              \tag{13}
\]

for sufficiently small positive rational `epsilon`.  The determinant of
the linear part is `epsilon^3>0`, so all signs internal to `Q` are
preserved.  With `u,v` as in (4), all `p_i` lie in the same insertion cell,
and for `a_i<a_j`,

\[
                         L(p_i)<L(p_j),\qquad R(p_i)<R(p_j).      \tag{14}
\]

Thus the entire union of all named trace clouds is one strict dominance
chain.  By Lemma 1, for every two different named clouds and every cross
pair `(p_i,p_j)`, the carrier completion is bad.

Put any convex carrier alphabet below `uv` whose faces retain `uv` as an
exposed edge.  In particular, `h` points on a lower parabola give `2^h`
different carrier faces.  Equation (14) holds against every one of them,
so the candidate mass in (11) can have **zero** good mixed pairs with no
metadata duplication and with arbitrary intrinsic child order types.

For that explicit carrier, the two endpoint profile counts obey

\[
 H=2^{h+2}-1,\qquad
 U=H,\qquad C=(h+2)+{h+2\choose2},\qquad {CU\over H}=\Theta(h^2). \tag{15}
\]

Since `2>a`, this saturation is paid by the carrier endpoint-surplus
alternative.  What remains open is whether a live carrier with surplus
below `R^{theta_*-o(1)}` can sustain (12) at `H`-scale mass.

## 5. Verification

`verify_three_cloud_common_edge_dominance.py` uses exact rational
arithmetic to check:

1. the equivalence (2) on a general-position sample containing both
   comparable and incomparable tangent pairs;
2. exact load-one recovery of all good three-cloud outputs;
3. the affine universal construction, including preservation of every
   child orientation sign and zero cross-cloud incomparability; and
4. all carrier faces in a finite lower-parabola alphabet.
