# Three cross-circuit matchings: a quadratic release bank, but no forced triangle

**Date:** 2026-08-15. This continues the dense residue in
*PLANAR_CROSS_CLASS_PRODUCT_AND_CAGE_ELIMINATION*. All face counts below
count nonempty ordinary convex subsets.

## Verdict

There is an exact positive Hall output, but it is only polynomial.

If the three matchings contain an actual **pair-node triangle**—one fixed
physical two-label pair in each class, with all three pair unions
nonconvex—then the six labels force at least three convex
\(2+1+1\) seams. For matching edge families those seams decode the source
triangle with load one. This is the exact positive triangle theorem.

Let \(A,B,C\) be disjoint planar classes and let
\(\mathcal M_{AB}\subseteq\Gamma(A,B)\) be a matching of nonconvex
four-sets. For every \(Q\in\mathcal M_{AB}\) and \(y\in C\), one of the
four sets

\[
                  (Q-\{z\})\cup\{y\},\qquad z\in Q,     \tag{1}
\]

is a convex four-set. Choosing the first successful \(z\) canonically
gives an injective bank of size

\[
                         |\mathcal M_{AB}|\,|C|.         \tag{2}
\]

The output retains the third-class label and three labels of one matching
edge, so it recovers the edge, the deleted label, and the class roles. For
all three pair matchings together, output load is at most three. Hence, if
\(H_A,H_B,H_C\) are the actual induced class-face counts,

\[
\boxed{\quad
 V(P)\ge H_A+H_B+H_C+
 {m_{AB}|C|+m_{BC}|A|+m_{CA}|B|\over3}.
\quad}                                                   \tag{3}
\]

Thus \(m_{ij}=\Omega(g)\) and class sizes \(\Theta(g)\) force
\(\Omega(g^2)\) decoded mixed rank-four faces. This is a genuine ordinary
bank with physical load one for one fixed pair matching.

It is not the required rich profile multiplication. The matching
hypotheses alone do not upgrade (2) to
\(m_{AB}H_C\), nor do three pairwise matchings force a triangle of
physically overlapping circuit edges.

Two exact anti-alignment statements show the obstruction.

1. For every \(m\), there is a rational general-position planar
   configuration with
   \[
        |A|=|B|=|C|=4m,\qquad
        \nu(\Gamma(A,B)),\nu(\Gamma(B,C)),\nu(\Gamma(C,A))\ge m,  \tag{4}
   \]
   in which the two selected matching supports incident with any one
   class are disjoint. The three selected matchings therefore have no
   physical overlap triangle.
2. Even if both incident matchings use **every** label of every class,
   abstract overlap can be a single \(3m\)-cycle rather than a triangle.
   Thus Hall density or support entropy by itself does not synchronize
   the matchings. This second incidence pattern is not asserted to be
   stretchable.
3. A twelve-point integral partner-reset has three convex four-point
   classes and one bad \(2+2\) circuit on every class pair, yet none of
   the \(2^6=64\) transversals choosing one endpoint from each of the six
   physical pair nodes is convex. Thus even the most natural colorful
   six-label cycle repair is false planarly.

The planar construction in (4) satisfies the live
\(\tau,\nu=\Omega(g)\) premise, so a three-class matching triangle cannot
be assumed. It may expose additional geometry-specific shields; the
report does not claim a coefficient-scale counterexample. The exact
remaining theorem must use signed circuit geometry, a shared carrier, or
bounded history—not just three large matching numbers.

## 1. Five-point canonical release

We use the classical planar five-point lemma.

> **Lemma 1.** Every five points in general position contain four in
> convex position.

One proof takes the convex hull. If it has at least four vertices, choose
four hull vertices. If it is a triangle with two interior points \(x,y\),
two triangle vertices \(a,b\) lie on the same side of the line \(xy\).
Meanwhile \(x,y\), being interior, lie on the same side of the hull edge
\(ab\). Thus \(ab\) and \(xy\) are opposite supporting edges of
\(\{a,b,x,y\}\), which is a convex quadrilateral. Strict general position
removes all boundary degeneracies.

Now fix a nonconvex four-set \(Q\) and \(y\notin Q\). Lemma 1 gives a
convex four-subset of \(Q\cup\{y\}\). It cannot be \(Q\), so it has exactly
the form (1). Order the four physical labels of \(Q\) and choose the first
successful deletion. Denote the resulting face by \(R(Q,y)\).

> **Theorem 2 (matching-by-third-class bank).** If
> \(\mathcal M_{AB}\) is a matching in \(\Gamma(A,B)\), then
> \[
>       (Q,y)\longmapsto R(Q,y),\qquad
>       Q\in\mathcal M_{AB},\ y\in C,                  \tag{5}
> \]
> is injective.

**Proof.** The output has exactly one \(C\)-label, namely \(y\), because
\(Q\subseteq A\cup B\). The remaining three labels belong to \(Q\).
Distinct edges of the matching are label-disjoint, so at most one selected
edge contains any of these labels. This recovers \(Q\), after which the
missing fourth label and the canonical deletion are known. \(\square\)

For a fixed class triple, apply Theorem 2 to the three pair matchings.
Within each pair family the load is one. A physical face has at most one
representation from each of the three families, so the combined load is
at most three. Every output is mixed and therefore is disjoint from the
three internal class banks. This proves (3).

If a later argument must fix the circuit occupancy/sign type or the
deleted role, a constant pigeonhole loses at most a constant factor.
Nothing of rank \(g\) is erased.

## 2. Global history load

For varying source or carrier contexts \(c\), let
\(\mathcal M_c\) be the selected physical matching and \(C_c\) the third
class. Put

\[
 \mathscr R=\{(c,Q,y):Q\in\mathcal M_c,\ y\in C_c\}     \tag{6}
\]

and let

\[
 \Lambda_{\rm hist}:=
 \max_F|\{(c,Q,y)\in\mathscr R:R_c(Q,y)=F\}|.           \tag{7}
\]

The literal Hall inequality is

\[
        V(P)\ge {|\mathscr R|\over\Lambda_{\rm hist}}
        ={\,\sum_c|\mathcal M_c||C_c|\,\over
          \Lambda_{\rm hist}}.                         \tag{8}
\]

For one fixed physical class triple and canonical matchings,
\(\Lambda_{\rm hist}\le3\). Repeating the same physical records under
\(h\) indistinguishable histories multiplies (7) by \(h\) and creates no
new face. Therefore the pairwise matching hypothesis does not control the
global history load; a carrier or chronology decoder remains necessary.

Equation (8) is the strongest automatic Hall payment. Replacing \(|C_c|\)
by the actual face count \(H_{C_c}\) would require a new four-local
compatibility theorem: singleton compatibility (1) does not control the
\(2+2\) and \(1+3\) four-subsets created by a large third-class face.

At the live scale, \(H_C\) is quasipolynomial in \(g\), whereas (2) is only
quadratic. Hence this theorem is useful for retaining physical marks and
pruning low-load histories, but it does not supply the missing
\(n^{\Theta(\log\log\log n)}\) multiplier.

### Actual pair-node triangles do pay

Let \(p_A,p_B,p_C\) be disjoint physical two-label pairs in the three
classes and suppose

\[
              p_A\cup p_B,\quad p_B\cup p_C,\quad
              p_C\cup p_A
\]

are all nonconvex. Apply Lemma 1 to each of the six five-subsets of
\(p_A\cup p_B\cup p_C\). Every convex four-set is counted in exactly two
of those five-subsets, so there are at least three convex four-sets.
The only four-sets meeting exactly two classes are the three displayed
pair unions, and they are bad. Thus all the forced faces meet all three
classes with occupancy \(2+1+1\).

If the class-pair circuit families are matchings of physical pair nodes,
an output seam doubles one pair, say \(p_A\). That pair has at most one
neighbour in each of the other two matching families, so it recovers
\(p_B,p_C\) and the source triangle. Therefore \(T\) pair-node triangles
give at least \(3T\) distinct ordinary seams.

The bound three is sharp: the verifier includes a six-point integral
example with exactly three convex four-subsets. The reset constructions
below evade this theorem by changing the physical partner pair at the next
class, not by hiding the payment of a genuine pair-node triangle.

## 3. Scalable planar support anti-alignment

> **Theorem 3.** For every \(m\ge1\), there is a rational
> general-position planar configuration partitioned into
> \(A,B,C\), each of size \(4m\), and selected matchings
> \(\mathcal M_{AB},\mathcal M_{BC},\mathcal M_{CA}\), each of size \(m\),
> such that the two matching supports incident with each class are
> disjoint.

**Construction.** Choose \(3m\) pairwise disjoint rational open disks,
\(m\) marked \(AB\), \(m\) marked \(BC\), and \(m\) marked \(CA\). In each
disk put a nonconvex rational four-set: three outer vertices and one point
strictly inside their triangle. Assign two labels to each of the two
classes marking the disk. For a fixed class pair the \(m\) four-sets are
label-disjoint, so they form a matching.

The labels of, say, \(A\) used in the \(AB\) disks are distinct from those
used in the \(CA\) disks. Hence every class has \(2m+2m=4m\) labels and its
two incident supports are disjoint. All containment conditions are open.
Choose the disk points successively from the dense rational points while
avoiding the finitely many lines determined by earlier pairs. This gives
global general position without changing any selected circuit.

The selected circuits themselves prove

\[
 \nu(\Gamma(A,B))\ge m,\qquad \tau(\Gamma(A,B))\ge m,   \tag{9}
\]

and likewise for the other two pairs: every cover must meet each member of
the selected disjoint matching. Since \(g=4m\), this is exactly a
constant-density planar instance of the dense premise.

There is no three-way circuit elimination among the selected edges because
the incident supports are disjoint. Any union retaining an entire selected
circuit is nonconvex by heredity. The canonical releases of Theorem 2
still give the quadratic bank; Theorem 3 does not refute that bank or other
geometry-specific faces.

The verifier's \(m=3\) rational instance has \(g=12\) and actual induced
class-face counts

\[
                         H_A=H_B=H_C=1161.              \tag{10}
\]

The three extension families contain \(108\) records and \(108\) distinct
faces, so their realized combined load is one in this anti-aligned
instance.

### A sharper finite partner-reset

The disjoint-sector construction is scalable but deliberately separates
the pair supports. The following integral configuration shows that a
class-level circuit cycle still need not admit a colorful pair-node
transversal. Put

\[
\begin{array}{c|rrrr}
A&(-11000,-11)&(-7797,629)&(9980,2008)&(9984,500)\\
B&(-9971,1975)&(-10004,505)&(-1006,9987)&(999,10011)\\
C&(-30,12020)&(-254,13159)&(9005,-24)&(15883,-1249).
\end{array}                                             \tag{11}
\]

All triples are noncollinear and every displayed class is a convex
four-set, with \(15\) nonempty internal faces. Split each row into its
first and last physical pair. The three four-sets

\[
\begin{aligned}
 &(A_{\rm first}\cup B_{\rm first}),\\
 &(B_{\rm last}\cup C_{\rm first}),\\
 &(C_{\rm last}\cup A_{\rm last})                       \tag{12}
\end{aligned}
\]

are nonconvex \(2+2\) circuits. Nevertheless, exhaustive exact hull tests
give

\[
\#\{S:S\text{ chooses one endpoint from each of the six pairs and is
convex}\}=0.                                             \tag{13}
\]

This kills a constant-load strategy which tries to repair the class cycle
by choosing one endpoint from every participating pair. It does not kill
the rank-four release bank (5): the latter uses one whole three-label
circuit trace and one external label, not a colorful six-transversal.
The twelve-point example is a finite planar gate, not a scalable subtarget
family.

## 4. Full-overlap abstract anti-alignment

The disjoint-support construction uses matching density \(1/4\). A simple
incidence model shows that even density one on the used support does not
force a triangle combinatorially.

Give each class labels \(a_{i,\epsilon},b_{i,\epsilon},c_{i,\epsilon}\),
where \(i\in\mathbb Z/m\mathbb Z\) and \(\epsilon\in\{0,1\}\). Define

\[
\begin{aligned}
 Q^{AB}_i&=\{a_{i-1,0},a_{i-1,1},b_{i,0},b_{i,1}\},\\
 Q^{BC}_i&=\{b_{i,0},b_{i,1},c_{i,0},c_{i,1}\},\\
 Q^{CA}_i&=\{c_{i,0},c_{i,1},a_{i,0},a_{i,1}\}.         \tag{14}
\end{aligned}
\]

Every family is a matching and both matchings incident with a class cover
all of its labels. The overlap graph on the circuit edges is the cycle

\[
 Q^{AB}_i-Q^{BC}_i-Q^{CA}_i-Q^{AB}_{i+1},              \tag{15}
\]

of length \(3m\), with doubled physical-label adjacencies. For \(m>1\)
it has no triangle. Thus even perfect support overlap plus Hall matching
does not force synchronized circuit triples. Whether a signed version of
(11) is stretchable is deliberately left open; Theorem 3 already gives
the required scalable planar barrier at constant density.

## 5. Consequence for the dense-circuit gate

The exact three-class outcome is:

* low aggregate output load closes a polynomial piece through (8);
* high load localizes many histories onto the same physical released
  rank-four faces;
* three pair matchings need not share labels or form circuit triangles;
* even full abstract support overlap can be cyclically anti-aligned; and
* the actual rich class banks remain additive, not multiplicative.

A coefficient-scale continuation must therefore add at least one of:

1. a bounded-history decoder which makes the quadratic bank summable;
2. a signed circuit-elimination hypothesis on genuinely shared labels;
3. a common carrier forcing the third-class face bank to coexist with one
   release trace; or
4. a geometric theorem ruling out repeated cyclic anti-alignment in rank
   three.

No synthesis closure is claimed.

## 6. Verification

Run

~~~text
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_three_class_circuit_matching_extension.py
~~~

The verifier constructs the \(m=3\) rational planar instance, checks
general position, all selected circuits, support disjointness, every
five-point canonical release, the exact decoder loads, the actual induced
class-face banks, artificial history duplication, and the full-overlap
triangle-free \(3m\)-cycle.
