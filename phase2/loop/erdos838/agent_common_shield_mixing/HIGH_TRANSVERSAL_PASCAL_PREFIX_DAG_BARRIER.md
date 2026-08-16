# A live high-transversal descent can be an acyclic prefix tree

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The high-transversal conclusion of
LIVE_ROOT_TRANSVERSAL_ENTROPY_GATE does not by itself produce an actual
same-configuration profile cycle or reset.  The central Pascal strong seam
gives a scalable live-normalized obstruction in which

* the source and released fixed-rank alphabets are both
  \(V(P)2^{-O(L\log L)}\);
* the record relation is their complete Cartesian product with pair load
  one;
* at a positive density of \(\Theta(L)\) chronology levels there are
  \(n^\varepsilon\) pairwise disjoint released-side traces;
* the branch tag is an increasing physical-label prefix and every selected
  branch has an exact decoder; but
* the full branch graph is a rooted DAG, every leaf erases its whole tag,
  and no deleted trace label can coexist with the retained source.

The construction is the top split \(P=Y\prec Z\) of a central Pascal cell.
Choose a fixed noncap triple \(T\subset Y\), a fixed-rank source family
\(\mathcal D\) containing \(T\), and a fixed-rank noncup pocket family
\(\mathcal H\subset\mathcal F(Z)\).  For every nonempty reduced pocket
trace \(U'\), the canonical circuit

\[
                         T\cup\{\min U'\}               \tag{1}
\]

is bad.  Its released trace is the singleton \(\{\min U'\}\).

The adaptive maximum-weight descent for these traces is exactly the
maximum-child descent in the increasing-prefix trie of \(\mathcal H\).  If
its dispersions are \(h_0,\ldots,h_{s-1}\), where every
\(U\in\mathcal H\) has rank \(s\), then the identity

\[
                         \prod_{j<s}h_j=|\mathcal H|    \tag{2}
\]

is exact.  Since \(\log|\mathcal H|=(\beta-o(1))L^2\) and
\(s\le(1+o(1))L\), a positive density of levels has
\(h_j\ge n^\varepsilon\).  At every such level the trace hypergraph consists
of disjoint singletons and therefore has an actual matching of size at least
\(h_j\).

Nevertheless the chronology edges strictly increase both prefix length and
the last deleted physical label.  There is no directed cycle.  More
decisively, every leaf \(U\) ends at the same reduced output \(D\) for a
fixed source \(D\), so summing all leaves has decoder load
\(|\mathcal H|\).  Retaining any erased edge label \(z\) is impossible:
\(T\cup\{z\}\subseteq D\cup\{z\}\) is nonconvex.  Thus the branch name
cannot be turned into a source-retaining face tag.

This is not a sub-half minimizer; its coefficient is
\(\beta=1-1/(4\ln2)>1/2\).  It is an exact applicability barrier.  A
positive theorem must use geometry coupling **different prefix branches**,
or a third physical role which stores a deleted label in an ordinary face.
High transversal number, even with live normalization and exact
per-branch decoding, is insufficient.

## 1. The fixed-rank live rectangle

Let

\[
 P_n=T(n,h),\qquad n=2h,
\]

with top split

\[
 Y=T(n-1,h-1),\qquad Z=T(n-1,h).
\]

Write \(W=V(Y)=V(Z)\), \(C=C(Y)=U(Z)\), and
\(\beta=1-1/(4\ln2)\).  The exact recurrence and uniform cap asymptotics
give

\[
 V(P_n)=2W+C^2,\qquad
 W=V(P_n)2^{-O(L\log L)},\qquad L=\log|P_n|.           \tag{3}
\]

The noncap and noncup complements satisfy

\[
 |\mathcal F(Y)\setminus\mathcal C(Y)|
 =|\mathcal F(Z)\setminus\mathcal U(Z)|
 =(1-o(1))W.                                          \tag{4}
\]

Every face in a Pascal cell has rank at most \(n-1\).  Partition the left
complement first by rank and then by its canonical first noncap triple.
Partition the right complement by rank.  There are choices \(r,s\le n-1\),
a physical triple \(T\), and families

\[
\begin{aligned}
 \mathcal D&=\{D\in\mathcal F(Y)\setminus\mathcal C(Y):
                    |D|=r,\ T(D)=T\},\\
 \mathcal H&=\{U\in\mathcal F(Z)\setminus\mathcal U(Z):
                    |U|=s\}
\end{aligned}                                         \tag{5}
\]

such that

\[
 |\mathcal D|,|\mathcal H|
        \ge V(P_n)2^{-O(L\log L)}.                     \tag{6}
\]

In fact the rank/triple loss is only polynomial in \(|P_n|\); the displayed
weaker form matches the live gate.  Since a rank-\(k\) family on at most
\(|P_n|\) labels has size at most \(|P_n|^k\), (6) also gives

\[
 r,s\ge(\beta-o(1))L,\qquad r,s\le(1+o(1))L.           \tag{7}
\]

Use all unit-weight records

\[
                         \mathcal R=\mathcal D\times\mathcal H. \tag{8}
\]

The ordered ordinary endpoints \((D,U)\) recover the literal record, so
the pair load is one, and

\[
 |\mathcal R|\ge {V(P_n)^2\over2^{O(L\log L)}}.         \tag{9}
\]

If source-dominated normalization is desired instead, give every pair
weight \(1/|\mathcal H|\).  This changes the total record mass, but none of
the prefix-tree or decoder statements below.  Equation (9) is the unit
release-bank normalization used in the high-transversal gate.

## 2. Canonical singleton circuit traces

Fix the increasing physical-label order inherited from the strong-glue
chart.  For \(D\in\mathcal D\) and a nonempty \(U'\subseteq U\), let
\(z=\min U'\).  Because \(T\) is a noncap triple in the left child, the
four-set \(T\cup\{z\}\) is nonconvex by the exact strong-glue
classification.  It is therefore a canonical bad circuit for
\(D\cup U'\), with released-side trace \(\{z\}\).

This rule is independent of the remaining labels of \(D\).  Consequently
the trace weights factor by \(|\mathcal D|\), and the adaptive descent on
records is exactly the following descent on the set family \(\mathcal H\).

At a node with deleted prefix

\[
                         K=(z_0<\cdots<z_{j-1}),        \tag{10}
\]

let \(\mathcal H_K\) be the original members whose first \(j\) labels are
exactly \(K\).  Partition \(\mathcal H_K\) by the next label
\(z=\min(U\setminus K)\), choose a largest class, append its label to \(K\),
and continue.

All members have the same rank \(s\).  Hence no record becomes good before
level \(s\), and at level \(s\) the reduced pocket is empty.  If
\(m_j=|\mathcal H_K|\) and the chosen child has size \(m_{j+1}\), the
weighted root dispersion is exactly

\[
                         h_j={m_j\over m_{j+1}}.         \tag{11}
\]

Telescoping, with \(m_0=|\mathcal H|\) and \(m_s=1\), proves (2).

At level \(j\), let \(q_j\) be the number of nonempty next-label classes.
The released trace hypergraph is

\[
                         \{\{z\}:z\text{ is a next label}\}. \tag{12}
\]

Its matching number is \(q_j\).  Since the largest class has size at least
\(m_j/q_j\), (11) gives

\[
                              q_j\ge h_j.               \tag{13}
\]

Thus the matching promised abstractly by the high-transversal theorem is
literal and singleton-disjoint in this example.

## 3. Positive-density polynomial branching

From (2), (6), and (7),

\[
 \sum_{j<s}\log h_j
     =\log|\mathcal H|
     \ge(\beta-o(1))L^2,\qquad s\le(1+o(1))L.           \tag{14}
\]

Also \(h_j\le|Z|\le 2^L\).  Fix any
\(0<\varepsilon<\beta\), and let \(k\) be the number of stages with
\(\log h_j\ge\varepsilon L\).  Then

\[
 (\beta-o(1))L^2
 \le kL+(s-k)\varepsilon L,
\]

so

\[
 k\ge\left({\beta-\varepsilon\over1-\varepsilon}
              -o(1)\right)L.                          \tag{15}
\]

Taking \(\varepsilon=\beta/2\) proves that a positive density of chronology
levels has at least

\[
                         q_j\ge h_j\ge |P_n|^{\beta/2}  \tag{16}
\]

pairwise disjoint actual traces.

This is stronger than merely invoking the entropy inequality: the exact
product identity (2) locates all the branching entropy in a concrete
decoder-tagged prefix tree.

## 4. Why the branches do not make a reset

The node state \(K\) is a literal increasing sequence of deleted physical
labels.  Every chronology edge

\[
                         K\longrightarrow K\cup\{z\}    \tag{17}
\]

increases \(|K|\), and \(z\) is larger than the preceding label.  Hence the
full branch graph is a rooted DAG.  The alternative traces at one level are
siblings, not edges returning to an earlier physical profile state.

For one selected branch, the tag \(K\) is fixed globally.  The reduced
ordered pair \((D,U\setminus K)\), together with \(K\), reconstructs
\((D,U)\), exactly as required by the live descent decoder.  Across all
branches, however, the terminal reduced pair is

\[
                              (D,\varnothing).          \tag{18}
\]

For fixed \(D\), all \(|\mathcal H|\) leaves collide.  The deleted-prefix
history is the entire released endpoint.

Nor can one retain an edge label as an ordinary source tag.  For every
\(z\in Z\),

\[
             T\cup\{z\}\subseteq D\cup\{z\}
             \quad\Longrightarrow\quad
             D\cup\{z\}\notin\mathcal F(P_n).           \tag{19}
\]

More generally no ordinary mixed face can retain the noncap source \(D\)
and a nonempty right trace.  The only mixed banks in this strong seam are
cap traces from \(Y\) times cup traces from \(Z\); using them projects away
the source/root tag and returns to the endpoint-potential gate.

Therefore the disjoint singleton traces cannot be routed into a
source-retaining directed profile cycle by chronology alone.  A successful
route must add a third physical face which stores the deleted label, or use
cross-branch planar relations not present in the hypotheses of the
high-transversal theorem.

## 5. Scope

This is a scalable, exactly realizable, live-normalized regression, but not
a counterexample to a minimizer-specific cycle theorem.  Its coefficient
\(\beta\) exceeds one half.  It proves that the following **direct
chronology-routing** implication is false without an additional hypothesis:

\[
\begin{gathered}
\text{live record mass + fixed rank/root + polynomial disjoint traces}\\
\Longrightarrow
\text{a cycle made from those trace edges while retaining the full source}.
\end{gathered}
\]

The report does not exclude a subtler cycle which first projects the source,
uses additional Pascal subcells, and controls the resulting decoder load;
that would be a genuinely new cross-branch geometric theorem.  The minimal
missing invariant for such a theorem is cross-branch storage: an ordinary face
whose decoder contains both the retained source identity and one deleted
prefix label, or a third/cyclic role which provides the same information.
The direct Pascal prefix descent has neither.

## 6. Verification

**verify_high_transversal_pascal_prefix_dag.py** performs:

1. an exact rational \(T(6,3)=T(5,2)\prec T(5,3)\) audit, including fixed
   source triple/rank, fixed pocket rank, every circuit, every prefix node,
   the exact dispersion product, terminal collisions, and the impossibility
   of retaining a trace label with a source;
2. an independent rank-refined integer dynamic program for cap, cup, and
   ordinary-face counts in all Pascal cells through \(n=56\), checking the
   fixed-rank live pigeonhole bounds and the total recurrences; and
3. exhaustive abstract prefix-family checks, verifying (2), (11), and (13)
   for every nonempty uniform family on up to five labels.
