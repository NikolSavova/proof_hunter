# First-incoherent siblings: a nested-triangle anti-aligned array

**Date:** 2026-08-15. This continues
`STABLE_CROSS_CIRCUIT_TOURNAMENT_CORE.md`. All labels are physical and all
face counts are for nonempty ordinary convex subsets.

## Verdict

The first pair of sibling matchings does not, by planarity alone, force a
common physical edge, a repeated rooted module, or an ordinary face carrying
two complete released traces. There is a scalable exact obstruction in the
uniform signed type

\[
        \text{one central label plus three partner labels, with the
        central label hidden}.                              \tag{1}
\]

For an arbitrary central planar child \(Y=\{y_1,\ldots,y_m\}\) and any
number \(k\) of partner classes, one can construct disjoint triples
\(T_j(a)\subset Z_j\), \(j\in[k]\), \(a\in[m]\), so that

\[
                         y_a\in\operatorname{int}\operatorname{conv}T_j(a)
                                                                  \tag{2}
\]

and all \(km\) triples are strictly totally nested. For fixed \(j\),

\[
                         E_j(a):=\{y_a\}\cup T_j(a)          \tag{3}
\]

is a label-disjoint matching of signed \(1+3\) circuits of exactly type
(1). Yet:

* if \(a\ne b\), the supports of \(E_i(a)\) and \(E_j(b)\) are disjoint;
* if \(a=b\) and \(i\ne j\), they share only the hidden singleton \(y_a\);
* no convex set contains two complete traces \(T_i(a),T_j(b)\); and
* no convex set contains a complete trace \(T_j(a)\) and a nonempty subset
  of \(Y\).

Thus the entire internal face complex of \(Y\) is retained as an induced
ordinary bank, but it has zero one-face compatibility with the complete
released-triangle bank. Each released triangle still decodes its geometric
record \((j,a)\) with load one. This is a sharp barrier to a purely local
first-incoherent-sibling splice.

The construction is not asserted to be a live low-face counterexample.
Partial traces inside the partner triangles remain available and may create
the global bank that pays. Consequently the surviving positive target must
use those partial edge/chain profiles or aggregate context load; complete
released traces and circuit elimination alone are insufficient.

## 1. Scalable construction

### Theorem 1 (nested all-loop array)

Let \(Y\) be any finite planar set in general position and let \(k\ge2\).
There is a general-position extension

\[
             P=Y\ \dot\cup\ Z_1\ \dot\cup\cdots\dot\cup\ Z_k,
             \qquad |Z_j|=3|Y|,                            \tag{4}
\]

and a partition \(Z_j=\dot\bigcup_{a=1}^mT_j(a)\) into triples satisfying
(2) and all four bullets above. If \(Y\) has rational coordinates, the
extension may be chosen rational.

#### Proof

Choose \(km\) triangles

\[
 \operatorname{conv}Y\subset\operatorname{int}\Delta_1,
 \qquad
 \Delta_t\subset\operatorname{int}\Delta_{t+1}
       \quad(1\le t<km).                                   \tag{5}
\]

Their vertices can be made jointly general with \(Y\). Inductively, the
set of triples whose convex hull strictly contains the preceding compact
set is a nonempty open subset of \(\mathbb R^6\). Collinearity with any two
already selected labels, or among three new labels, is a finite union of
proper algebraic hypersurfaces. Avoiding that union preserves a nonempty
open set. If the old coordinates are rational, rational points are dense in
this open set.

Assign the triangles bijectively to pairs \((j,a)\) and call their vertex
sets \(T_j(a)\). Equation (5) implies (2). Since the four labels in (3) are
general and \(y_a\) is strictly inside its partner triangle, (3) is a
signed circuit with the central label as its unique hidden point. For fixed
\(j\), different \(a\)'s use different central labels and disjoint assigned
triangles, proving the matching property.

Two records with different central indices have disjoint supports. Two
records with the same central index and different partner indices share
only that singleton. Hence no pair has a common two-label root.

Finally, every central label lies strictly inside every triangle. A set
containing a full \(T_j(a)\) and a central label therefore hides that label.
If it contains two full released triangles, all vertices of the earlier
triangle in the nesting order lie strictly inside the later one. Either
way the set is not in convex position. \(\square\)

## 2. Exact first-sibling classification in this type

Fix two partner roles \(i\ne j\). The independent-index pair
\(E_i(a),E_j(b)\) has only two cases.

### Different central indices

When \(a\ne b\), the two signed circuit supports are disjoint. The signed
circuit elimination axiom has no common element on which to eliminate.
Nothing in rank three forces their record-specific triangle vertices to
acquire a common physical root.

### Equal central index

When \(a=b\), the circuits share \(y_a\), with the same hidden sign in the
normalization (1). Reversing one signed circuit permits elimination at
\(y_a\), but the resulting circuit is supported inside

\[
                         T_i(a)\cup T_j(a).                 \tag{6}
\]

Those six labels occur in no other record of either matching. In the nested
construction their union is already nonconvex because the inner triple is
hidden by the outer triple. Elimination therefore gives a pair-specific
outer circuit, not a repeated edge or a bounded physical guard shared over
many central indices.

This explains precisely why the tournament core's common index set does
not itself provide sibling coherence: the matching condition deliberately
removes the label repetition that a common-root conclusion would need.

## 3. Central retention and decoder ledger

Let \(\mathcal F(Y)\) be the nonempty ordinary face complex induced by the
central class. Every \(F\in\mathcal F(Y)\) remains the identical ordinary
subset of \(P\), so

\[
                         |\mathcal F(Y)|=V(Y)               \tag{7}
\]

is retained with decoder load one. The complete-release map

\[
                         (j,a)\longmapsto T_j(a)             \tag{8}
\]

is also injective and has load one. Likewise the separated pair
\((\{y_a\},T_j(a))\) decodes the geometric circuit record exactly.

There is nevertheless no mixed one-face product between (7) and (8):

\[
 \{F\cup T_j(a):F\in\mathcal F(Y),\ F\ne\varnothing\}
                \cap\mathcal F(P)=\varnothing.             \tag{9}
\]

Nor can a one-face output store two records by retaining their two complete
released traces. Thus the exact geometric record load is one but the
available complete-trace output count is only \(km\), not quadratic in the
number of records. If several omitted-carrier histories project to the same
geometric pair \((j,a)\), their additional decoder load is exactly that
history multiplicity; geometry does not distinguish it.

At the tournament-core scale, \(m=|Y'|\) may be near ambient and
\(k=\Theta(\log\log n)\). The construction therefore realizes the full
\(mk\)-record signed incidence array with arbitrary central order type. It
rules out any promotion theorem whose only inputs are:

1. a rich induced central face complex;
2. label-disjoint uniform circuit matchings; and
3. two independently chosen central indices.

## 4. What remains available globally

The obstruction deliberately controls only **complete** released triples.
A convex output may still use one or two vertices from many nested
triangles. These partial traces have tangent directions and can support
one-sided chains, endpoint modules, or long-run banks. The construction
does not give an upper recurrence for the full ambient face complex of
\(P\), and therefore is not a sub-half recursive example.

A valid continuation of the tournament-core proof must exploit at least one
of the following extra inputs:

* a bounded-load bank of partial partner traces, tagged by their actual
  first/last tangent vertices;
* repetition of a physical edge or guard not supplied by matching alone;
* aggregate Hall load across many partner roles; or
* a minimizer-specific restriction excluding the all-loop nesting (1).

The most promising sharp split is by partial-trace rank: if many records
release compatible edges, use their tangent modules; if almost every usable
release is a singleton, the surviving object is a directional profile
ramp rather than a complete-triangle circuit bank.

## 5. Verification

Run

~~~text
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_first_incoherent_sibling_nested_triangle_barrier.py
~~~

The verifier constructs 15 strictly nested rational/integer triangles for
five central labels and three partner classes. The central child has a
genuine interior point. It checks general position, all signed containment
circuits, fixed-partner matching disjointness, exact sibling intersections,
strict nesting, all central-face/complete-release incompatibilities, and the
load-one release decoder.

