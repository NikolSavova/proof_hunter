# Three-class pair-circuit triangle gate

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

There is an exact bounded-history composition theorem for the reused-pair
branch.  Encode a bad \(2+2\) cross-class four-circuit as an edge between
the physical two-label nodes in its two classes.  A triangle of such edges
uses six points.  The three pair-union four-sets are nonconvex, but every
five planar points contain a convex four-set.  A double count forces at
least three convex \(2+1+1\) seams among the six points.  When the
class-pair circuit families are matchings, each seam recovers the entire
triangle, so the decoder load is one.

This closes high actual-pair reuse.  It does **not** close high label reuse.
The sharp escape is pair reset: the same physical label is used against
many neighbouring classes, but with a different partner every time.  An
exact rational 12-point configuration realizes the three-class reset
planarly, even with a directed circuit cycle and a Boolean internal bank
in every class.  Edge-disjoint one-factorizations scale the incidence
pattern to \(t\) classes, matching size \(g/2\) for every class pair,
label load \(t-1\), and zero pair-node triangles.

The 12-point reset can be projectively nested into the common-\(uv\)
pocket while preserving its full order type.  Thus the fixed-edge
endpoint-XOR structure does not remove the reset.  The next genuinely
missing coordinate is the partner itinerary of each reused physical
label; this is stronger than a label chronology and weaker than repeated
physical-pair reuse.

## 1. The auxiliary pair graph

Let \(Y_1,\ldots,Y_t\) be disjoint child classes.  In the \(2+2\) branch,
select for every class pair \(i,j\) a family \(\mathcal M_{ij}\) of
nonconvex four-sets, each containing two labels of \(Y_i\) and two labels
of \(Y_j\).

Define a \(t\)-partite graph \(\mathcal G\).  Its vertices in part \(i\)
are physical pairs \(p\in\binom{Y_i}{2}\), and

\[
          pq\in E(\mathcal G)
 \quad\Longleftrightarrow\quad
          p\cup q\in\mathcal M_{ij}.                  \tag{1}
\]

If \(\mathcal M_{ij}\) is a label-disjoint circuit matching, its edges in
the \(ij\) bipartite graph form a matching of pair nodes.  This is the
actual situation after the vertex-cover/matching pruning in
PLANAR_CROSS_CLASS_PRODUCT_AND_CAGE_ELIMINATION.

## 2. Six-point seam theorem

> **Theorem 1 (pair-circuit triangle).**  Let
> \(p_i\in\binom{Y_i}{2}\), \(i=1,2,3\), form a triangle of
> \(\mathcal G\).  Among the six labels in
> \(p_1\cup p_2\cup p_3\), at least three four-sets are convex and meet all
> three classes.  Each has occupancy \(2+1+1\).

**Proof.**  Every five-point set in general position contains a convex
four-set.  Apply this to the six five-subsets of the six labels.  Every
convex four-set is counted in exactly two five-subsets, so there are at
least three convex four-sets.

There are only three four-sets using labels from exactly two of the
two-label classes, namely

\[
                         p_1\cup p_2,\quad
                         p_2\cup p_3,\quad
                         p_3\cup p_1.
\]

All three are nonconvex by (1).  Every other four-set meets all three
classes and has occupancy \(2+1+1\). \(\square\)

The proof is purely rank-three and extends to uniform acyclic rank-three
oriented matroids.

The lower bound three is sharp.  The verifier's exact cyclic example is

\[
\begin{array}{c|cc}
Y_1&(138,679)&(505,820)\\
Y_2&(269,337)&(293,733)\\
Y_3&(528,847)&(378,590).
\end{array}                                           \tag{2}
\]

All triples are noncollinear.  The three pair unions are nonconvex, with
the interior-point classes cycling through \(Y_2,Y_1,Y_3\).  The only
convex four-sets are

\[
 \{0,1,3,4\},\qquad \{0,2,3,5\},\qquad \{1,2,4,5\}.   \tag{3}
\]

Thus a directed \(1+3\) circuit cycle is not itself forbidden; its forced
payment is exactly the three seams in (3).

## 3. Decoder and bounded-load theorem

Let \(\Delta\) bound the degree of a physical pair node within each
class-pair bipartite graph.

> **Theorem 2 (triangle-to-face decoder).**  If \(\mathcal G\) contains
> \(T\) tripartite triangles, then the seams supplied by Theorem 1 give
> \[
>                         V(P)\ge {3T\over\Delta^2}.   \tag{4}
> \]
> In particular, for selected class-pair matchings,
> \[
>                         V(P)\ge3T.                  \tag{5}
> \]

**Proof.**  Emit every convex seam from Theorem 1.  An output seam doubles
one physical pair node, say \(p_1\), and retains one physical label from
each of \(p_2,p_3\).  It also retains the three class colors.  Given
\(p_1\), there are at most \(\Delta\) possible incident \(Y_1Y_2\) edges
and at most \(\Delta\) possible incident \(Y_1Y_3\) edges.  These determine
at most \(\Delta^2\) source triangles.  Each triangle emits at least three
seams, proving (4).  When both incident edge families are matchings, the
doubled pair determines its two neighbours uniquely, so the load is one.
\(\square\)

This decoder retains actual physical labels.  It has no context or
metadata quotient.  If the circuit matching and class coloring are
recoverable from the live carrier description, no additional load appears.

The theorem does not retain a rich internal face \(F_i\).  It supplies
only a rank-four seam.  Its global force therefore comes from a
quasipolynomial number of pair-node triangles, not from multiplying one
triangle by \(|\mathcal F(Y_i)|\).

## 4. Exact planar pair-reset regression

The pair-node triangle hypothesis cannot be replaced by a class-level
cycle or by high label degree.

Use the following twelve integral points:

\[
\begin{array}{c|rrrr}
Y_1&(-11000,-11)&(-8988,22)&(9980,2008)&(9984,500)\\
Y_2&(-9971,1975)&(-10004,505)&(-1006,9987)&(999,10011)\\
Y_3&(-30,12020)&(0,10497)&(9005,-24)&(10983,-19).
\end{array}                                           \tag{6}
\]

All triples are noncollinear.  There are three bad \(2+2\) circuits:

\[
\begin{aligned}
 &\{(-11000,-11),(-8988,22),(-9971,1975),(-10004,505)\},\\
 &\{(-1006,9987),(999,10011),(-30,12020),(0,10497)\},\\
 &\{(9005,-24),(10983,-19),(9980,2008),(9984,500)\}.
                                                               \tag{7}
\end{aligned}
\]

Their interior-point classes form a directed three-cycle.  But each class
uses one physical pair against each neighbour, and the two pairs are
different.  The auxiliary graph is three disjoint edges, so it has no
triangle.  Each \(Y_i\) is itself a convex four-set and hence has the full
16-face Boolean bank.

This is a genuine planar failure of pair-node reuse, not an abstract
hypergraph.  It does not claim a globally subtarget recursive wrapper:
other faces of the twelve-point set may pay.  Its exact scope is that the
hypotheses “rich internal banks + disjoint circuit matching for every
class pair + directed class cycle” do not imply Theorem 2's reusable-pair
triangle.

## 5. Scalable incidence reset

For even \(g\), the complete graph \(K_g\) has \(g-1\) edge-disjoint
one-factors.  Suppose \(t\le g\).  At every class \(Y_i\), assign distinct
one-factors to its \(t-1\) neighbouring classes.  For every pair \(i,j\),
match the \(g/2\) pair nodes in the assigned factor of \(Y_i\) to the
\(g/2\) pair nodes in the assigned factor of \(Y_j\).

Then:

\[
\begin{array}{ll}
\text{class-pair circuit matching size}&g/2,\\
\text{number of circuit occurrences per physical label}&t-1,\\
\text{number of neighbours of each physical pair node}&1,\\
\text{number of pair-node triangles}&0.               \tag{8}
\end{array}
\]

Thus the actual role-forest mass forces \(\Theta(t)\) reuse of every
physical label, but does not combinatorially force any physical pair to be
reused.  Since \(t=\Theta(L)\ll g\), the supply of fresh partners is
overwhelming.

The verifier constructs this reset for \(t=8,g=12\): 168 circuit edges,
label occurrence seven, and no pair-node triangle.

Planar realizability of the full \(t\)-class one-factorization pattern is
not proved.  That is now the geometric content required from a global
argument.

## 6. Compatibility with the common-\(uv\) cage

The finite planar reset does not disappear in the fixed-edge pocket.
Apply the standard projective nesting map to the twelve points in (6).
It preserves their complete convex-face order type and places them in one
nested pocket between fixed

\[
                         u=(-1,0),\qquad v=(1,0).
\]

Then every child pair \(y,z\) satisfies
\(\{u,v,y,z\}\) nonconvex.  An opposite-side point
\(x=(1/7,1)\) satisfies \(\{u,v,x,y\}\) convex for every child label.
Consequently all endpoint-XOR colors from the preceding report are
defined, while the three circuit matchings still reset their physical
partners.

This proves that a common carrier, a common side covector, and endpoint
XOR coherence do not by themselves promote label reuse to pair reuse.

## 7. Remaining bounded-history operation

The high-triangle branch is closed by (4).  The exact remaining branch has
all of:

1. \(\Omega(g)\) label-disjoint cross circuits for each class pair;
2. average physical-label reuse \(\Theta(t)\);
3. low or zero physical-pair reuse, implementable combinatorially by
   one-factorizations;
4. a coherent endpoint-XOR/radial order at each outside direction; and
5. a rich internal face bank which is not retained by the rank-four seam.

A successful continuation must prove that a planar realization of this
many partner resets forces either:

* a repeated pair after a recoverable chronology/coarsening;
* a context-retaining convex seam involving the rich \(F_i\); or
* a same-physical-child radial permutation cycle whose potential pays.

The partner choice is the genuinely missing history coordinate.  Tracking
only the physical label, circuit sign, class direction, or endpoint color
loses it.

The \(3+1\) occupancy branch is separate: its natural nodes are a physical
triple and a singleton, and Theorem 1 does not apply without a further
fan-to-pair reduction.

## 8. Verification

Run

    python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_three_class_pair_circuit_triangle_gate.py

The script checks the sharp six-point cycle and its ES double count, exact
seam decoding, the twelve-point planar reset and its Boolean class banks,
the scalable one-factorization reset, and the projectively nested
common-\(uv\) embedding.  It prints PASS.
