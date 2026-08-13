# Erdős 838 lower-bound campaign — attack_tree (gpt-5.6-sol, effort=max, 2026-08-13 14:30)

> Target: log C + log U >= (1/2 - o(1))(log N)^2 for ARBITRARY point sets.
> With Theorem 1.1 already proved, this resolves Erdős 838 outright.

## Bottom line

The canonical-tree route is **sharply obstructed**. The obstruction is not merely that a modular split is weaker than a deep-below split. The decomposition stops at arbitrarily large **indecomposable nodes**, and the class on which it stops immediately is already asymptotically as hard as the full problem:

> Every point set with exactly three convex-hull vertices has a one-node canonical tree. Moreover, proving the target cap–cup bound only for such triangular-hull sets would imply it for every point set, with an additive loss of at most \(6+o(1)\) bits.

Thus the canonical decomposition does not bridge the gap from decomposable to arbitrary order types. It delegates the entire unresolved problem to its prime nodes.

---

## 1. What the cited decompositions actually produce

### Balko–Kynčl–Langerman–Pilz

Their decomposable sets have a recursively ordered binary split \(P=P_1\cup P_2\) satisfying:

1. every point of \(P_1\) is left of every point of \(P_2\);
2. \(P_1\) lies deep below \(P_2\);
3. both children are recursively decomposable, down to singletons.

Hence all mixed orientations are the two fixed signs needed in your Lemma 5.2. ([combinatorics.org](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i4p24/pdf/))

### Bouvel–Féray–Goaoc–Koechlin

For a bipartition \(X\sqcup Y\), the relevant operation is the bowtie
\[
\kappa=\chi\;{}_{x^*}\!\bowtie_{y^*}\;\xi ,
\]
where
\[
\kappa(x_1,x_2,y)=\chi(x_1,x_2,x^*),\qquad
\kappa(x,y_1,y_2)=\xi(y^*,y_1,y_2).
\]
Thus the sign of a mixed triple generally depends on the pair inside the majority side. A bipartition is a module precisely when such a bowtie representation exists. Geometrically, the two parts are mutually avoiding, but this is weaker than a fixed-sign deep-below split. ([arxiv.org](https://arxiv.org/pdf/2403.10311))

Their original chirotope tree is:

- unrooted and unordered;
- each node is decorated by a chirotope on a disjoint ground set of size at least three;
- every edge selects one extreme **proxy** at each endpoint;
- a proxy is used by only one edge;
- actual elements are the nonproxy labels of the node decorations—not necessarily graph-theoretic leaves;
- removing an edge gives a bowtie decomposition of the represented chirotope.

With all decorations retained, nothing is lost: the full chirotope is reconstructed exactly. What is not supplied is an \(x\)-order, an affine realization, balanced cuts, or fixed mixed signs. ([arxiv.org](https://arxiv.org/pdf/2403.10311))

The canonical normal form has exactly two node classes:

- **convex decorations**;
- **indecomposable decorations**, meaning no nontrivial modular bipartition;

and no edge joins two convex nodes. It is unique up to the irrelevant proxy labels. Convex–convex contractions remove the nonuniqueness of decomposing a convex chirotope. ([arxiv.org](https://arxiv.org/pdf/2403.10311))

The authors explicitly distinguish this from BKLP: the BKLP notion also controls \(x\)-coordinates, is more restrictive, and is fully decomposable down to one-point blocks. ([arxiv.org](https://arxiv.org/pdf/2403.10311))

### Follow-up

Gioan and Marin reformulate the same decomposition using the tree representation of the family of mutually avoiding bipartitions. In that equivalent convention, ground-set elements occur as leaves and internal nodes carry convex or indecomposable quotient oriented matroids. Their contribution is an \(O(n^3)\) algorithm for computing the same canonical decomposition; it does not introduce separators through indecomposable nodes. ([hal-lirmm.ccsd.cnrs.fr](https://hal-lirmm.ccsd.cnrs.fr/lirmm-04905101v1/preview/DecompositionTreev07-Emeric.pdf))

### Quasi-modules do not provide the missing tree

Section 6 of the full paper defines a quasi-module \(W\) by requiring every pair in \(W\) to induce the same **nontrivial** bipartition of the outside. This notion is asymmetric and is used to control multiplicity in a “substitution along a segment” counting argument. The paper proves an upper bound on the number of large quasi-modules, not that every chirotope has one, nor that they form a recursive or canonical tree. ([arxiv.org](https://arxiv.org/pdf/2403.10311))

---

## 2. Exact cap–cup classification across a bowtie edge

Here is the correct replacement for the strong-separation identities.

Assume a bowtie decomposition is displayed in an order with all elements of \(X\) before all elements of \(Y\). Append \(x^*\) after \(X\), and prepend \(y^*\) before \(Y\). Define
\[
\begin{aligned}
C_X^\to&=\#\{\emptyset\ne S\subseteq X:S\cup\{x^*\}\text{ is a cap}\},\\
U_X^\to&=\#\{\emptyset\ne S\subseteq X:S\cup\{x^*\}\text{ is a cup}\},\\
C_Y^\leftarrow&=\#\{\emptyset\ne T\subseteq Y:\{y^*\}\cup T\text{ is a cap}\},\\
U_Y^\leftarrow&=\#\{\emptyset\ne T\subseteq Y:\{y^*\}\cup T\text{ is a cup}\}.
\end{aligned}
\]

### Proposition: bowtie edge identities
For \(P=X\sqcup Y\),
\[
\boxed{
C(P)=C(X)+C(Y)+C_X^\to C_Y^\leftarrow
}
\]
and
\[
\boxed{
U(P)=U(X)+U(Y)+U_X^\to U_Y^\leftarrow .
}
\]

### Proof

Let \(K\) be a cap meeting both sides, and put
\[
S=K\cap X,\qquad T=K\cap Y.
\]
Both are nonempty.

- Triples contained in \(X\) say that \(S\) is a cap.
- Triples \(x_1<x_2<y\), with \(x_1,x_2\in S\), \(y\in T\), have sign
  \[
  \kappa(x_1,x_2,y)=\chi(x_1,x_2,x^*).
  \]
  Thus all these signs are negative exactly when \(S\cup\{x^*\}\) is a cap.
- Triples \(x<y_1<y_2\) have sign
  \[
  \kappa(x,y_1,y_2)=\xi(y^*,y_1,y_2).
  \]
  Thus they are all negative exactly when \(\{y^*\}\cup T\) is a cap.

These conditions are also sufficient, and the decomposition \(K=S\sqcup T\) is unique. Hence crossing caps are in bijection with pairs counted by \(C_X^\to C_Y^\leftarrow\). The cup identity is identical with signs reversed. ∎

This uses exactly the bowtie mixed-orientation rule from the canonical-decomposition paper. ([arxiv.org](https://arxiv.org/pdf/2403.10311))

### Strong separation is a special boundary state

For \(X\prec Y\), writing \(a=|X|\), \(b=|Y|\),
\[
C_X^\to=C(X),\qquad C_Y^\leftarrow=b,
\]
because every cap of \(X\) extends through the right proxy, while a cap using the left proxy of \(Y\) can contain only one actual point of \(Y\). Similarly,
\[
U_X^\to=a,\qquad U_Y^\leftarrow=U(Y).
\]
Therefore
\[
C(P)=C(Y)+(b+1)C(X),\qquad
U(P)=U(X)+(a+1)U(Y),
\]
which is precisely the input to Lemma 5.2.

For a general module, these four marked quantities are additional data. The universal bounds are only
\[
a\le C_X^\to\le C(X),\qquad a\le U_X^\to\le U(X),
\]
and similarly on \(Y\), since every singleton together with the proxy is a two-point cap and cup.

Putting \(R(P)=\sqrt{C(P)U(P)}\), Cauchy–Schwarz gives the always-valid but much weaker recurrence
\[
R(P)\ge R(X)+R(Y)
  +\sqrt{C_X^\to U_X^\to C_Y^\leftarrow U_Y^\leftarrow}
\ge R(X)+R(Y)+ab.
\]
What disappears are the sibling-mass coefficients
\[
\sqrt{b+1}\,R(X),\qquad \sqrt{a+1}\,R(Y).
\]
Thus even at a favorable left–right display of a canonical edge, a scalar state \(R\) is insufficient; one must carry proxy-marked cap and cup statistics. In an arbitrary realization, the module parts need not even be \(x\)-contiguous.

I am **not** claiming here that the desired strong scalar inequality is false for every module. The point is that it is not a consequence of the canonical module axioms; the exact edge formula shows the missing information.

---

## 3. Assessment of the two canonical node types

### Convex nodes

A convex decoration is not intrinsically troublesome. If it contains \(q\) actual nonproxy elements, those elements are extreme in the global chirotope and hence form a convex \(q\)-set.

For any convex \(q\)-set, let its upper and lower hull chains have \(r\) and \(s\) vertices, including their common endpoints. Then
\[
r+s=q+2.
\]
Every nonempty subset of the upper chain is a cap, and every nonempty subset of the lower chain is a cup, so
\[
C\ge 2^r-1,\qquad U\ge2^s-1,
\]
and consequently
\[
\log C+\log U\ge(r-1)+(s-1)=q.
\]
Thus a convex node containing many actual elements already gives far more than the target.

When most of the node labels are proxies leading to large attached subtrees, however, a multi-proxy state is required. The canonical construction intentionally contracts the many possible binary decompositions of a convex node, so it does not select a simultaneous sequence of strong ordered splits.

### Indecomposable nodes

This is the fatal node type. By definition, no canonical edge can split it. Its size is unrestricted. Indeed, the full paper proves that a uniformly random labeled realizable chirotope is indecomposable with probability \(1-O(n^{-3})\). ([arxiv.org](https://arxiv.org/pdf/2403.10311))

There is also a much sharper deterministic obstruction.

### Lemma: the number of canonical nodes is controlled by hull size

If the canonical tree has \(k\) nodes and the represented point set has \(h\) extreme points, then
\[
\boxed{k\le h-2.}
\]

#### Proof

Every node decoration has at least three extreme elements. The \(k-1\) tree edges use \(2(k-1)\) distinct extreme proxies. The remaining nonproxy extreme labels are precisely the extreme elements of the represented chirotope. Hence
\[
h\ge 3k-2(k-1)=k+2.
\]
∎

This is the counting observation made in the canonical-tree paper. ([arxiv.org](https://arxiv.org/pdf/2403.10311))

In particular:

\[
\boxed{h(P)=3\quad\Longrightarrow\quad\text{the canonical tree has one node}.}
\]

For \(|P|>3\), that node is nonconvex and therefore indecomposable. Equivalently, every nontrivial bowtie has at least four surviving extreme elements—at least two from each factor after deleting the two proxies.

So an arbitrary \(N\)-point configuration with triangular convex hull admits **no canonical decomposition step at all**.

---

## 4. Triangular-hull sets are already the whole problem

This is the sharpest obstruction.

### Proposition: outer-triangle reduction

Let \(P\) be any \(N\)-point set. Choose three generic points \(O=\{o_1,o_2,o_3\}\) forming a triangle whose interior contains \(P\), and put
\[
Q=P\cup O.
\]
The points can be chosen so that \(Q\) remains in general position and has distinct \(x\)-coordinates. Then \(Q\) has exactly three extreme points and hence a one-node indecomposable canonical tree.

Define counts including the empty set:
\[
\widehat C(P)=C(P)+1,\qquad \widehat U(P)=U(P)+1.
\]
Then
\[
\boxed{\widehat C(Q)\le 8\widehat C(P),\qquad
       \widehat U(Q)\le 8\widehat U(P).}
\]

#### Proof

If \(K\) is a cap of \(Q\), then \(K\cap P\) is a cap of \(P\), possibly empty, because being a cap is hereditary. For each fixed \(S=K\cap P\), there are at most
\[
2^{|O|}=8
\]
possible choices for \(K\cap O\). Hence
\[
\widehat C(Q)\le8\widehat C(P).
\]
The cup inequality is identical. ∎

Therefore, setting
\[
L(P)=\log\widehat C(P)+\log\widehat U(P),
\]
we have
\[
\boxed{L(P)\ge L(Q)-6.}
\]
Since \(C(P),U(P)\ge N\), replacing \(C,U\) by \(C+1,U+1\) changes the logarithms by \(o(1)\).

Consequently, if the target estimate were known only for point sets with triangular convex hull,
\[
\log C(Q)+\log U(Q)
\ge \left(\frac12-o(1)\right)(\log|Q|)^2,
\]
then it would follow for every \(P\), because \(|Q|=|P|+3\) and the transfer loses only \(6+o(1)\) bits.

Thus:

> **The target lemma restricted to module-indecomposable order types is asymptotically equivalent to the unrestricted target lemma.**

This rules out the hoped-for bridge in the strongest possible sense. Any canonical-tree proof must insert a base-case theorem for arbitrary indecomposable nodes; but that base case alone already solves the original problem.

---

## Decisive answer

1. **Does every order type admit enough strong-separation-like internal nodes?**  
   No. Every triangular-hull order type has no nontrivial module and hence no internal decomposition edge.

2. **What survives at a general module edge?**  
   The exact four-state bowtie identities above. The strong recurrence is recovered only at the special state
   \[
   (C_X^\to,C_Y^\leftarrow,U_X^\to,U_Y^\leftarrow)
   =(C(X),|Y|,|X|,U(Y)).
   \]

3. **Which node breaks the recurrence?**  
   An arbitrarily large nonconvex indecomposable node.

4. **What is the worst case?**  
   An arbitrary point set enclosed by three new outer points. The resulting triangular-hull set has a one-node canonical tree, while its cap and cup logarithms differ from those of the original set by at most six bits in total.

**VERDICT: OBSTRUCTED — the canonical module tree stops at arbitrarily large indecomposable nodes, and the one-node triangular-hull subclass is already asymptotically complete for the target problem.**

**Cleanest statement established:** For every planar point set \(P\), there is a module-indecomposable triangular-hull superset \(Q\) with \(|Q|=|P|+3\) such that
\[
\log(C(P)+1)+\log(U(P)+1)
\ge
\log(C(Q)+1)+\log(U(Q)+1)-6.
\]
Hence proving the target cap–cup product bound for indecomposable order types alone is equivalent, up to \(O(1)\), to proving it for all order types.