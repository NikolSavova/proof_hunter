# A planar pair reset with no colorful endpoint transversal

**Date:** 2026-08-15. This is a finite exact barrier complementing
`THREE_CLASS_PAIR_CIRCUIT_TRIANGLE_GATE.md` and
`FIRST_INCOHERENT_SIBLING_NESTED_TRIANGLE_BARRIER.md`.

## Verdict

A directed three-class reset of bad \(2+2\) circuit edges need not admit
even one convex transversal obtained by choosing one endpoint from every
physical pair node. The following general-position twelve-point order type
has six partner pairs, three designated pair-union circuits, and convex
four-point internal classes, but all \(2^6=64\) colorful six-sets are
nonconvex.

The obstruction is stronger than failure of the full six-role word. After
omitting pair node \(r\), the numbers of convex one-endpoint transversals of
the remaining five nodes are

\[
                         (0,0,8,8,0,0).                    \tag{1}
\]

Thus four of the six possible one-gap banks are empty. A cyclic
pair-reset argument cannot be repaired merely by selecting one endpoint
from every circuit pair or by dropping an arbitrary first bad seam.

This is finite evidence, not a scalable low-face construction. The full
configuration has \(709\) nonempty ordinary faces, so other ranks pay
substantially. The exact remaining operation must use those non-colorful
faces, retain fewer partner nodes, or exploit global repetition of the
same physical pair.

## 1. Coordinates and class structure

In pair-node order, take

\[
\begin{array}{c|rr}
p_0&(-11000,-11)&(-7797,629)\\
p_1&(-9971,1975)&(-10004,505)\\
p_2&(-1006,9987)&(999,10011)\\
p_3&(-30,12020)&(-254,13159)\\
p_4&(9005,-24)&(15883,-1249)\\
p_5&(9980,2008)&(9984,500).
\end{array}                                                \tag{2}
\]

The three physical classes are

\[
                  Y_1=p_0\cup p_5,\qquad
                  Y_2=p_1\cup p_2,\qquad
                  Y_3=p_3\cup p_4.                         \tag{3}
\]

Every class is a convex four-set. All triples among the twelve labels are
noncollinear. The designated cross-class circuit edges are

\[
                         p_0p_1,\qquad p_2p_3,\qquad p_4p_5. \tag{4}
\]

Their hidden labels, in the coordinate ordering of (2), are respectively
the second endpoint of \(p_1\), the first endpoint of \(p_3\), and the
second endpoint of \(p_5\). Hence the same pair-reset incidence nodes as in
the three-class report are present, with one fresh pair at each class
incidence.

## 2. Exact transversal failure

For \(\epsilon\in\{0,1\}^6\), define the colorful trace

\[
                         X_\epsilon=\{p_r(\epsilon_r):0\le r<6\}. \tag{5}
\]

Exact hull enumeration gives

\[
\begin{array}{c|rrrr}
|\operatorname{ext}X_\epsilon|&3&4&5&6\\ \hline
\#\epsilon&16&32&16&0.
\end{array}                                                \tag{6}
\]

In particular no \(X_\epsilon\) is in convex position. This is a statement
about the complete planar order type, not just the three selected circuit
signs.

The one-gap audit is also exact. Omitting \(p_r\) and checking the
\(2^5\) endpoint choices gives (1). In the four zero columns, every proposed
rank-five colorful repair still hides at least one selected label.

## 3. What the example kills and what survives

The example refutes the implication

> convex local class banks + a directed cycle of disjoint bad pair circuits
> \(\Longrightarrow\) a convex one-endpoint transversal of the six pair
> nodes.

It also refutes a uniform one-gap version. It does not refute the exact
six-point seam theorem: that theorem applies when three bad edges form a
triangle on **reused physical pair nodes**, while (4) consists of three
disjoint edges. Nor does it suppress the ambient bank. Exhaustive face
enumeration gives the rank vector

\[
             (f_1,\ldots,f_7)=(12,66,220,253,125,30,3),
             \qquad V(P)=709.                              \tag{7}
\]

Therefore a global proof may still charge rank-four or rank-five seams.
What fails is the proposed decoder that represents every partner pair by
one chosen endpoint and expects all six representatives to coexist.

At the stable-tournament core, this means a partial-trace continuation must
retain the actual tangent/hull state of each chosen endpoint. Pair color and
endpoint bit alone are insufficient: all 64 bit words occur here and all
fail.

## 4. Verification

Run

~~~text
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_colorful_pair_endpoint_transversal_barrier.py
~~~

The verifier uses exact integer determinants. It checks general position,
the three convex classes, the three hidden-point circuits, all 64 colorful
words, all 192 one-gap words, and all \(4095\) nonempty subsets for the face
vector (7).

