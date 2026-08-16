# Erdős 838: planar lattice rectangles, exact theorem and exact barrier

**Date:** 2026-08-14  
**Status:** the closure-lattice route is now resolved up to one sharply
identified dynamic mass dichotomy.  It does not by itself solve Erdős 838.

## Headline

There are two complementary exact facts.

1. **Opposite-side tangent-compatible rectangles multiply perfectly.**  If
   two rooted convex arcs lie on opposite sides of one directed chord and
   the two endpoint tangent signs agree, every cross-union is a distinct
   two-ended convex face.  With the chord forgotten, target recovery costs
   at most `r(r-1)`.
2. **Closure comparability and Theorem-23 product support do not force those
   signs.**  A same-side nested repair cell can satisfy Theorem 23 with
   `epsilon=0`, zero mutual information, support probability one, and
   weighted-`C_4` probability one, while all common-frame closed hulls form
   a single chain.

Thus the missing statement is not a static lattice interval theorem.  It is
a dynamic assertion that enough near-product mass must either cross into an
opposite-side tangent-compatible state, or pay through a discarded child
face complex before the old tangent frame disappears.

## 1. The exact positive theorem

Fix a directed chord `uv`.  Let `C+` be a rooted convex arc above `uv` and
`C-` a rooted convex arc below it.  The only turns not already certified
inside the two arcs are the turns at `u` and `v`.  Hence the union is in
convex position exactly when the two tangent signs at those endpoints have
the convex orientation.

For families `X,Y` such that every pair satisfies those signs, the map

\[
 (C^+,C^-)\longmapsto \operatorname{cl}(C^+\cup C^-)
\]

is injective.  The extreme set of the target closure recovers the union,
and the two open half-planes recover the two factors.  Therefore one obtains
exactly `|X||Y|` distinct two-ended faces in a single closure interval.

If the chord is not stored, a rank-`r` target has at most `r(r-1)` ordered
chords.  A canonical two-endpoint dyadic localization loses only
`ceil(log n)^2`; at `r=Theta(log n)` both losses are `2^{o(r)}`.  This
completely resolves geometric conversion and target reconstruction once a
`2^{-o(r)}` fraction of the repair mass has the compatible opposite-side
signature.

Full proof and exact checker:

* `lattice_rectangle_theorem/REPORT.md`
* `lattice_rectangle_theorem/verify_lattice_rectangle.py`

## 2. Why abstract and planar comparability are insufficient

The universal lattice inequality

\[
 |\downarrow K|\,|\uparrow K|\le |\mathcal C(P)|
\]

is false already for a four-point planar configuration consisting of a
triangle and one interior point: the two sides are `2` and `8`, while the
closure lattice has `15` elements.  Nested inner/outer pockets make the gap
exponential; an exact 18-point instance has `262144` comparable pairs and
only `9841` closed hulls.

Abstract meet-distributivity is even weaker.  A two-level poset-ideal convex
geometry has a complete rectangle of size `2^r` but only
`2^(r/2+1)-1` closed sets.  Thus neither anti-exchange nor
meet-distributivity contains the two cyclic tangent signs used by the
positive theorem.

Exact planar countersearch and certificates:

* `lattice_rectangle_counter/REPORT.md`
* `lattice_rectangle_counter/verify_lattice_rectangle_counter.py`
* `lattice_rectangle_counter/certificate.json`

## 3. The exact Theorem-23 equality obstruction

Take a common convex lower chain `R` of size `r-1` and a totally nested
same-side sequence

\[
 y_1,\ldots,y_{a+a^r}.
\]

The first `a` points are singleton hidden ears and the last `a^r` points
are blockers.  For every earlier ear `x_i` and later blocker `p_j`, insertion
of `p_j` into `R+x_i` hides exactly `x_i` and leaves `R+p_j` extreme.  Thus
the support is a full rectangle of size `a^(r+1)`.

For the uniform record law,

\[
 \kappa=1,\quad \tau=r,\quad \rho=\log_2a,
\]

and both marginal density bounds of ACP Theorem 23 are equalities:

\[
 H(I)=\rho\kappa,\qquad H(T)=\rho\tau.
\]

Nevertheless the common-frame closure interval is the chain

\[
 K_0\subset K_1\subset\cdots\subset K_{a+a^r},
\]

and every convex face containing `R` contains at most one `y_t`.  There are
only `a+a^r+1` common-frame hulls/faces.  No two-ended target is present,
because all variation is on the same side and every later point hides every
earlier point.

An explicit general-r integer realization is

\[
 R=\{(z,z^2-B^2):z\in\{-B,1,\ldots,r-3,B\}\},
 \qquad y_t=(t^2,t),
\]

with `B=10(a+a^r+r)^3`.  Exact determinant and interval audits are in:

* `LATTICE_RECTANGLE_BARRIER.md`
* `lattice_rectangle_barrier.py`
* `lattice_rectangle_barrier_certificate.json`

The independent counter verifier checks the density-equality cases
`r=3`, `a=2,3` by a second coordinate construction.

## 4. The remaining gate after ACP Theorem 23

Theorem 23 already gives the entropy alternative:

* a marginal has surplus density, in which case rank slicing supplies a
  recursive child family; or
* the support contains `2^{-o(r)}` weighted product/`C_4` mass.

The positive rectangle theorem discharges the second branch if a
`2^{-o(r)}` fraction of that mass reaches opposite rooted arcs with the two
tangent signs.  The equality counterexample proves that this need not happen
inside one static cell.

The exact residual is therefore:

> Along the prefix-correlated outward-successor recursion, every
> entropy-balanced near-product rectangle must either (i) spend
> `2^{-o(r)}` mass in tangent-compatible opposite-side chord cells, or
> (ii) release the convex-face complex of a discarded cyclic prefix/child,
> with total child reuse `2^{o(r)}`.

Alternative (i) now has a complete proof with polynomial recovery loss.
Alternative (ii), including global reuse across repeated same-side resets,
is still open.  Closure-lattice cardinalities cannot prove this dichotomy;
the proof must retain the ordered cyclic boundary history.
