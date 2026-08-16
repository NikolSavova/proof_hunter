# Planar lattice rectangles: an exact two-ended conversion theorem

**Date:** 2026-08-14  
**Verdict:** there is a rigorous rectangle-to-face theorem at the missing
geometric interface, but only after the rectangle has been localized to a
common directed chord and to the two correct tangent orders.  In that
state, every **tangent-comparable** lower-by-upper pair is a distinct
convex-position set; equivalently it is a distinct element of the affine
closure lattice.
The map is injective with the chord fixed and has fibre at most `r(r-1)`
when the chord is forgotten.  Thus any upstream description loss of
`2^{o(r)}` remains `2^{o(r)}` after geometric conversion.

This does **not** finish the residual after Theorem 23 of
`../../agent_acp_proof/REPORT.md`.  Near-product stability supplies dense
weighted `C_4`s in the repair support, but it does not force their four
corners to cross the tangent-compatibility boundary.  A rectangle trapped
in one replacement cell may have zero two-ended spend.  The theorem below
removes target recovery and closure-lattice multiplicity once compatible
cross-cell mass is present; producing that mass remains the hierarchical
tangent-reset gate.

The planar qualification is load-bearing.  A two-level poset convex
geometry has a complete lower-by-upper comparability rectangle of size
`2^r` but only `2^{r/2+1}-1` closed sets.  Its lattice is distributive, hence
meet-distributive.  Therefore no theorem with a `2^{o(r)}` loss follows
from abstract closure comparability, meet-distributivity, or a dense `C_4`
alone.

All point sets below are in planar general position.  `cl` means affine
closure in the fixed ambient set `P`:

\[
                  \operatorname{cl}_P X=P\cap\operatorname{conv}X.
\]

## 1. Rooted arcs and the rank-three compatibility order

Fix distinct `u,v in P`, orient the line from `u` to `v`, and let `H^+`
and `H^-` be its two open half-planes.  A **positive rooted arc** is a
convex-position set `C^+` containing `u,v`, with at least one further
point, all of whose further points lie in `H^+`.  Define a negative rooted
arc `C^-` similarly in `H^-`.

The chord `uv` is a hull edge of each individual arc.  Write
`c_u^+,c_v^+` for the neighbours of `u,v` other than each other in
`C^+`, and use `c_u^-,c_v^-` for `C^-`.  Concatenating the negative arc
from `u` to `v` and the positive arc from `v` to `u` gives the only possible
cyclic boundary of their union.  Call the two arcs **tangent-comparable**
when

\[
 \chi(c_u^+,u,c_u^-)>0,
 \qquad
 \chi(c_v^-,v,c_v^+)>0,                           \tag{1}
\]

where `chi(a,b,c)=sign orient(a,b,c)` is the rank-three chirotope.

After ordering the rays at each endpoint, (1) is exactly a two-coordinate
dominance condition

\[
             \lambda(C^+) > \lambda(C^-),
 \qquad      \rho(C^+) < \rho(C^-),               \tag{2}
\]

up to the harmless choice of which endpoint order is reversed.  This is
the same compatibility order as the two-root tangent criterion in the
two-ended and all-interval reports.  It depends on two cyclic-boundary
signs, not on abstract lattice comparability.

> **Theorem 1 (two-ended affine-lattice rectangle theorem).**
> Let `X` be a family of positive rooted arcs and `Y` a family of negative
> rooted arcs for one directed chord `uv`.  Suppose every pair in
> `X times Y` is tangent-comparable.  Then:
>
> 1. every `C^+ union C^-` is in convex position;
> 2. the map
>    \[
>       (C^+,C^-)\longmapsto
>       \operatorname{cl}_P(C^+\cup C^-)           \tag{3}
>    \]
>    is injective; and
> 3. if every arc is contained in a carrier `Q subseteq P`, all the closed
>    sets in (3) are distinct members of the single lattice interval
>    \[
>       [\operatorname{cl}_P\{u,v\},
>        \operatorname{cl}_P Q].                  \tag{4}
>    \]
>
> Consequently that interval contains at least `|X||Y|` closed sets, whose
> extreme sets are `|X||Y|` distinct two-ended convex faces.

**Proof.**  Every internal turn of either rooted arc has the correct strict
sign.  The arcs lie in opposite open half-planes, so their concatenation is
a simple polygonal cycle.  Its only turns not already certified inside one
arc are the turns at `u` and `v`; these are precisely the two signs in
(1).  Hence all turns of the simple cycle have one strict sign, so it is the
boundary of a strictly convex polygon.  This proves the first assertion.

For fixed `uv`, the two open half-planes recover the factors from their
union:

\[
 C^+=(C^+\cup C^-)\cap(H^+\cup\{u,v\}),\qquad
 C^-=(C^+\cup C^-)\cap(H^-\cup\{u,v\}).           \tag{5}
\]

If `A` is a convex-position subset of a general-position planar set, the
extreme points of `cl_P A` are exactly `A`.  Thus the closed set in (3)
recovers the union, and (5) recovers the ordered pair.  This proves
injectivity.  Finally monotonicity of closure and containment of `u,v`
give (4).  QED.

The proof uses only the cyclic order and the two rank-three signs (1).
Equivalently, a failed sign creates the local rooted circuit which prevents
the corresponding endpoint from lying on the concatenated convex boundary.
This is the exact planar circuit input missing from a generic
meet-distributive lattice.

### Dense support version

Let `G subseteq X times Y` be any nonempty support relation of density

\[
                 \delta={|G|\over |X||Y|}.         \tag{6}
\]

The whole comparability rectangle completes, regardless of which pairs
were initially in `G`, so Theorem 1 gives

\[
 \boxed{
 |[\operatorname{cl}\{u,v\},\operatorname{cl}Q]|
 \ge |X||Y|={|G|\over\delta}.}                    \tag{7}
\]

In particular a support with `delta >= 2^{-o(r)}` loses no exponential
information when converted to intermediate closed sets.  Notice that (7)
requires **all cross pairs to satisfy (1)**.  Density of `G` without this
comparability hypothesis is not enough.

## 2. Forgetting the chord costs only a quadratic factor

The fixed-chord hypothesis is a localization, not an expensive decoder.

> **Theorem 2 (global recovery bound).**  Let `D_r` be any collection of
> descriptions
> \[
>                  (u,v,C^+,C^-)                 \tag{8}
> \]
> satisfying Theorem 1 and having union rank at most `r`.  The map from
> descriptions to `cl_P(C^+ union C^-)` has fibre at most
> \[
>                         r(r-1).                 \tag{9}
> \]
> If an additional state tag belongs to a set `Sigma`, the fibre is at most
> `|Sigma|r(r-1)`.

**Proof.**  A target closed set recovers its extreme set `A`.  The ordered
chord `(u,v)` must be an ordered pair of distinct vertices of `A`, giving at
most `|A|(|A|-1)<=r(r-1)` choices.  Once it is chosen, (5) uniquely recovers
the two arcs.  A state tag contributes the displayed extra factor.  QED.

This gives an exact capped-Hall interface.  Suppose a family of demand
tokens has been assigned compatible descriptions (8), each complete
description including its state tag is used by at most `kappa` tokens, and
the union face is an allowed target for every token assigned to it.  Sending
each token to that union face has congestion at most

\[
             \boxed{\kappa |\Sigma|r(r-1).}       \tag{10}
\]

Therefore

\[
       \kappa|\Sigma|=2^{o(r)}
       \quad\Longrightarrow\quad
       \text{a capped routing with congestion }2^{o(r)}.    \tag{11}
\]

The same conclusion holds for a partial spend containing a
`2^{-o(r)}` fraction of the tokens, with an additional `2^{o(r)}` loss.
If the partial-spend hypothesis holds hereditarily for every token
subfamily and its allowed target neighbourhood, (10) is precisely the
capped Hall inequality; cloning each target (10) times and applying Hall's
theorem gives a simultaneous assignment.

The point of (9)--(11) is that a compatible two-ended target retains both
outer components as vertices.  There is no ambient `n`-fold root guess.
This is stronger than a one-ended repair target, which may forget its
blocker and can have unbounded cone fibre.

## 3. Canonical dyadic localization has subexponential cost

The dominance condition (2) can be localized without paying at every
recursive depth.  Pad each endpoint rank order to a complete binary tree.
Assign a strict comparison to the lowest dyadic node separating its two
ranks.  Doing this at both endpoints assigns every compatible pair to one
pair of depths

\[
              (d_\lambda,d_\rho),
 \qquad 0\le d_\lambda,d_\rho<\lceil\log_2 n\rceil.          \tag{12}
\]

At a fixed depth pair, the compatible relation is an edge-disjoint union
of complete separated lower-by-upper rectangles.  Hence one depth pair
carries at least a

\[
                   {1\over\lceil\log_2 n\rceil^2}            \tag{13}
\]

fraction of any nonnegative compatible weight.  At the critical ranks
`r=Theta(log n)`, (13) is `2^{-o(r)}`.  The target itself recovers both
arcs and hence its dyadic boxes, so rectangles at different nodes do not
create a new collision factor.

Indeed, for ranks `a>b`, their lowest common dyadic node puts `a` in its
right child and `b` in its left child.  For a compatible pair, do this for
the first inequality in (2), and reverse the child roles for the second.
After fixing the two lowest common nodes, every object in the resulting
positive-side box is comparable with every object in the negative-side
box.  Each compatible pair has a unique pair of lowest common nodes, so
these complete rectangles partition the edges.  Grouping by the two node
depths gives at most `ceil(log_2 n)^2` layers and proves (13).

This is a useful sharpening of the one-coordinate spend/reset partition:
once mass is known to satisfy both tangent inequalities, localization and
target recovery together cost only `poly(r)`.  What remains hard is forcing
enough mass to satisfy both inequalities before a nested descent deletes
the old tangent markers.

## 4. Why general meet-distributive lattices cannot replace planarity

Let the ground set be the disjoint union `L dotcup U`, with `|L|=k` and
`|U|=l`.  Put a partial order in which every member of `L` is below every
member of `U`, with no other comparabilities, and let closure be downward
closure.  This is a finite convex geometry: if

\[
 x\in\operatorname{cl}(A+y)\setminus\operatorname{cl}(A),
\]

then `x<y`, so antisymmetry prevents
`y in cl(A+x)`.  Its closed-set lattice is the ideal lattice of the poset,
which is distributive and therefore meet-distributive.

The closed sets are exactly

\[
 \{S:S\subseteq L\}
 \quad\text{and}\quad
 \{L\cup T:T\subseteq U\},                       \tag{14}
\]

with `L` counted in both displays.  Thus there are

\[
                         2^k+2^l-1                \tag{15}
\]

closed sets.  Take every first-display set as a lower element and every
second-display set as an upper element.  Every lower is below every upper,
so the comparability relation is a complete rectangle of size

\[
                            2^{k+l}.               \tag{16}
\]

For `k=l=r/2`, the ratio of (16) to (15) is
`2^{r/2-1+o(1)}`.  Hence even a **complete** comparability rectangle in a
distributive convex-geometry lattice need not yield its product number of
intermediate closed sets within a `2^{o(r)}` factor.

This counterexample does not conflict with Theorem 1.  Its two Boolean
wings have no common planar chord, no opposite cyclic boundary arcs, and
no rank-three tangent signs.  Abstract meet-distributivity remembers
accessibility of extreme deletions but not the planar gluing operation (5).

## 5. Interface with Theorem 23 and the exact residual

Theorem 23 gives the following alternative for an entropy-critical repair
family:

1. one marginal has surplus entropy density and can be rank-sliced for
   recursion; or
2. the repair support is a `2^{-o(r)}`-dense near-product and contains
   weighted `C_4` mass `2^{-o(r)}`.

Theorems 1--2 prove that the second branch is discharged with only
`2^{o(r)}` congestion **provided** a `2^{-o(r)}` fraction of that mass can
be represented by opposite rooted arcs in one of `2^{o(r)}` common
chord/signature states satisfying (1).  The dyadic refinement in Section 3
then costs only `poly(r)`.

The proviso cannot be deleted.  In the singleton product cell of Theorem
23, `T=(R,p)` and `I={x}` are independent and the support rectangle is
complete, but `T union I` is nonconvex: the blocker `p` hides `x`.  The
missing factor occurs between neighbouring endpoint cells, where two
blockers/ears appear as opposite boundary arcs.  Likewise, the nested
parabolic example may stay in one cell for many deletions and instead pays
through the Boolean complex of the discarded prefix.

Thus the rigorous new residual is not a generic lattice rectangle theorem.
It is the following planar mass statement:

\[
 \boxed{
 \begin{minipage}{0.84\linewidth}
 Along the prefix-correlated outward-successor recursion, weighted
 near-product rectangles must either cross into tangent-comparable
 two-ended chord states with `2^{-o(r)}` mass, or release the ordinary
 convex-face complex of a discarded cyclic interval before the old chord
 is deleted.
 \end{minipage}}                                             \tag{17}
\]

Once the first alternative of (17) occurs, this report proves the exact
face conversion and capped recovery.  The second alternative is the
already isolated long-prefix reset.  No proof of their universal
dichotomy is claimed here, so Erdős 838 remains open.

## 6. Exact verification

Run

```bash
python3 \
  phase2/loop/erdos838/agent_cyclic_stem_hw/lattice_rectangle_theorem/verify_lattice_rectangle.py
```

The checker uses integer orientation predicates and exact finite closure
enumeration.  On a deterministic nine-point configuration it enumerates
every directed chord and every rooted arc, and checks:

* the equivalence between the two endpoint signs (1) and convexity of the
  cross-union;
* injectivity for a fixed chord and the global fibre bound (9);
* recovery of every convex face as the extreme set of its affine closure;
* containment of every target in its advertised closed-lattice interval;
  and
* exact partition of compatible tangent-rank pairs by two dyadic depths.

It then exhausts the `k=l=4` two-level poset example, checks the closure
axioms and anti-exchange, verifies both distributive laws, and confirms the
counts `16 times 16=256` versus `16+16-1=31`.  The symbolic families in
(14)--(16) scale these exact checks to every `k,l`.
