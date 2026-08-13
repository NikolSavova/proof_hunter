# Erdős 838: current full-solution attack

> Status, 2026-08-13. There is now a self-contained candidate proof of the
> unconditional upper coefficient \(1/2\), with an exact rational-coordinate
> verification artifact. The original limit problem remains open. The
> missing lower bound is isolated below as an endpoint-alignment theorem.

All logarithms are base \(2\).

## 1. Rigorous window

Let \(f(N)\) be the minimum number of convex-position subsets in an
\(N\)-point planar set in general position. The current candidate theorem in
proof_blowup_half.md gives

\[
 \limsup_{N\to\infty}\frac{\log f(N)}{(\log N)^2}\leq\frac12. \tag{1}
\]

The proof iterates a thin vertical lexicographic blow-up of a balanced
cap--cup extremal configuration. If a fixed template \(S\) has \(r\) points,
largest cap \(a\), and largest cup \(b\), the iteration has the exact
convex-subset coefficient

\[
 \rho(S)=\frac{a+b-2}{2\log r}.                    \tag{2}
\]

The cap--cup theorem gives \(r\leq2^{a+b-2}\), so \(\rho(S)\geq1/2\) for
every fixed template. The balanced Pascal cells make \(\rho(S)\to1/2\).
Thus (1) is sharp within this entire construction class, not just for the
particular templates used in the proof.

The best currently available lower argument remains

\[
 \liminf_{N\to\infty}\frac{\log f(N)}{(\log N)^2}\geq\frac14. \tag{3}
\]

Hence the rigorous base-\(2\) window is

\[
 \boxed{\qquad \frac14\leq\liminf\leq\limsup\leq\frac12.\qquad} \tag{4}
\]

This does not prove that the limit exists.

## 2. Exact endpoint factorization

After a small rotation, label the points
\(p_1,\ldots,p_N\) by increasing \(x\)-coordinate. For \(s<t\), let

* \(c(s,t)\) be the number of caps with endpoints \(p_s,p_t\);
* \(u(s,t)\) be the number of cups with endpoints \(p_s,p_t\).

Pairs count once as both a cap and a cup. Every convex subset of size at
least two has a unique upper cap and lower cup with the same endpoints, and
the union of any such cap/cup pair is convex. Therefore

\[
 \boxed{\quad
 V(P)=1+N+\sum_{1\leq s<t\leq N}c(s,t)u(s,t).
 \quad}                                             \tag{5}
\]

The maps in (5) are inverse: the upper and lower hull chains recover the
convex subset, while their interior vertices lie on opposite sides of the
endpoint line. This identity has been checked against the complete
Aichholzer order-type and convex-\(k\)-gon data through \(N=9\).

For fixed \(s\), the endpoint counts are computed by

\[
\begin{aligned}
C_s(s,j)&=U_s(s,j)=1,\\
C_s(i,j)&=\sum_{\substack{s\leq h<i\\\chi(h,i,j)=-}}C_s(h,i),\\
U_s(i,j)&=\sum_{\substack{s\leq h<i\\\chi(h,i,j)=+}}U_s(h,i), \tag{6}\\
c(s,t)&=\sum_{i=s}^{t-1}C_s(i,t),\qquad
u(s,t)=\sum_{i=s}^{t-1}U_s(i,t).
\end{aligned}
\]

Thus the full lower problem is exactly a weighted endpoint-alignment
problem for realizable rank-three signotopes.

## 3. The matching conjecture

The clean completion of (1) would be

> **Endpoint multiplicity conjecture.** Uniformly over all \(N\)-point sets
> \(P\) in general position,
> \[
> \sum_{s<t}c(s,t)u(s,t)
> \geq2^{(1/2-o(1))(\log N)^2}.                    \tag{EM}
> \]

Equation (EM) and (1) would prove that the limit in Erdős 838 exists and
equals \(1/2\) in base \(2\), or \(1/(2\ln2)\) in the natural-log
normalization.

There are two useful intermediate targets. Write

\[
 C(P)=N+\sum_{s<t}c(s,t),\qquad
 U(P)=N+\sum_{s<t}u(s,t).
\]

A possible two-lemma route is

\[
 \log C(P)+\log U(P)
 \geq(1/2-o(1))(\log N)^2,                         \tag{7}
\]

together with the conditional alignment statement

\[
 \log V(P)\geq\log C(P)+\log U(P)-o((\log N)^2)    \tag{8}
\]

whenever \(\log V(P)=O((\log N)^2)\). The condition in (8) is necessary:
one can strongly glue a cup-heavy set on the left to a cap-heavy set on the
right, making the reverse cap/cup masses badly anti-aligned, but that example
already has exponentially many convex subsets and is harmless for (EM).

Neither (7) nor (8) is currently proved.

## 4. Why black-box Erdős--Szekeres stops at \(1/4\)

The modern Erdős--Szekeres theorem says

\[
 ES(k)=2^{k+o(k)}.                                 \tag{9}
\]

Take \(T=N^\alpha\). Every \(T\)-subset contains a convex
\((\alpha-o(1))\log N\)-subset. Double-counting the pairs consisting of a
\(T\)-set and one selected witness gives

\[
 \log f(N)\geq
 \bigl(\alpha(1-\alpha)-o(1)\bigr)(\log N)^2.
\]

The maximum is \(1/4\), at \(\alpha=1/2\). Recursively inserting the same
bound at the smaller scale does not amplify the coefficient: the entropy
gained inside the sample is exactly offset by the reduced number of
extensions back to \(P\).

Positive-fraction Erdős--Szekeres theorems do not currently help. The best
known quantitative constants lose \(2^{\Theta(k)}\) in cluster size; even an
idealized loss \(2^k\) merely reproduces \(1/4\). A matching proof must count
many compatible witnesses or exploit endpoint sharing.

## 5. Construction theorem and audit

For point sets \(S,Q\) whose two coordinates increase, replace every point
of \(S\) by a sufficiently thin almost-vertical copy of \(Q\). Write the
composition as \(S[Q]\). If \(c_j(S),u_j(S),v_j(S)\) are the cap, cup, and
convex profiles of \(S\), and \(n=|Q|\), the exact formulas are

\[
\begin{aligned}
C(S[Q])&=C(Q)\sum_{j\geq1}c_j(S)n^{j-1},\\
U(S[Q])&=U(Q)\sum_{j\geq1}u_j(S)n^{j-1},           \tag{10}\\
W(S[Q])&=|S|W(Q)+C(Q)U(Q)\sum_{j\geq2}v_j(S)n^{j-2}.
\end{aligned}
\]

A spanning cap can expand only its first macro-block; a spanning cup only
its last. A spanning convex subset expands its first block to a cap and its
last to a cup, while every intermediate occupied block contributes exactly
one point. Its occupied macro-blocks form a convex subset of \(S\).

The independent script lexicographic_blowup.py:

1. constructs the abstract composition signs;
2. realizes them with exact rational coordinates;
3. evaluates (10);
4. independently counts caps/cups by last-edge dynamic programming;
5. independently counts convex subsets by (5).

For \(S=Q=T_{4,2}\), a 36-point configuration, both routes return

\[
 (C,U,W)=(14136,14136,441399).
\]

## 6. Lower-bound lanes that still look viable

### 6.1 Weighted down-set/signotope induction

The orientation signs satisfy the one-change axiom: for every
\(a<b<c<d\), the four signs

\[
 \chi(a,b,c),\ \chi(a,b,d),\ \chi(a,c,d),\ \chi(b,c,d)
\]

have at most one sign change. Existing cap--cup proofs label vertices by
down-sets generated from pairs of longest red/blue path lengths. The desired
upgrade is to replace longest lengths by the full path-count vectors in
(6), then prove a nesting or majorization statement strong enough for
(7)--(8).

The obstacle is precise: unweighted labels prove that some long paths
exist, but they forget how much red and blue path mass reaches the same
left/right endpoint pair.

### 6.2 Strongly decomposable sets

For a strong glue \(P=A\prec B\), exact nonempty counts satisfy

\[
\begin{aligned}
C(P)&=C(B)+(1+|B|)C(A),\\
U(P)&=U(A)+(1+|A|)U(B),                            \tag{11}\\
W(P)&=W(A)+W(B)+C(A)U(B).
\end{aligned}
\]

The new \(1/2\) construction lies inside this class: replace every leaf of
a large balanced Pascal-cell decomposition tree by the preceding iterate.
So the earlier \(0.639326\ldots\) decomposable-extremality guess was false.

A matching lower bound for every decomposition tree is now a sharply posed
intermediate theorem. Equation (11) says that \(W\) is a sum, over internal
tree nodes, of a cap mass from the left child times a cup mass from the
right child. A proof must show that either one subtree already has
\(2^{(1/2-o(1))(\log N)^2}\) convex subsets, or one of these forward products
is large. The reverse product \(C(B)U(A)\) is the only obstruction to a
naive induction.

Exact Pareto dynamic programming through \(N=21\) finds no counterexample
and gives decreasing normalized minima, but finite sizes are too small to
distinguish \(1/2\) from larger constants.

### 6.3 Convex-closure entropy

The closure operator

\[
 \operatorname{cl}(X)=P\cap\operatorname{conv}(X)
\]

makes \(P\) a finite convex geometry. Every closed set has a unique set of
extreme generators, and those generators form a convex-position subset.
Conversely every convex-position subset is the extreme generator of its
closure. Hence

\[
 V(P)=\#\{\text{closed sets of this planar convex geometry}\}. \tag{12}
\]

There is also the exact fiber identity

\[
 2^N=\sum_{S\text{ convex}}2^{\,|P\cap\operatorname{int}\operatorname{conv}S|}.
                                                               \tag{13}
\]

Equations (12)--(13) offer an entropy route, but general abstract convex
geometries can have only \(N+1\) closed sets. Any useful argument must use
planar realizability and general position, not anti-exchange alone.

## 7. A warning from the graph analogue

Székely's 1984 problem asks for the minimum total number of complete and
independent vertex subsets in an arbitrary graph. Its random-graph upper
bound has coefficient \(1/2\) in the same base-\(2\) normalization, while
the best lower bound in that paper is substantially smaller. There is no
known reduction between that problem and Erdős 838, but the structural
analogy is close: both ask for total multiplicity rather than the size of
one Ramsey witness.

This makes a quick matching lower bound unlikely. It also suggests that the
right tools may be Ramsey--Turán stability, weighted containers, or entropy
of path-count profiles rather than another application of the existence
theorem.

## 8. Falsification data

The complete order-type census gives the exact minima below; the empty set
is included.

| \(N\) | 6 | 7 | 8 | 9 |
|---:|---:|---:|---:|---:|
| all order types | 45 | 73 | 114 | 169 |
| decomposable order types | 46 | 76 | 121 | 185 |

Thus decomposable sets cease to be exactly extremal already at \(N=6\), but
the discrepancy is far too small to diagnose the asymptotic constant.
Simple Horton/double-chain monotonicity conjectures also fail on these
records.

## 9. Current next move

The best proof attempt is now:

1. prove the cap/cup product bound (7) for realizable signotopes;
2. prove conditional endpoint alignment (8), first under the recursive
   decomposition law (11);
3. in parallel, run the general Baek--Balko blow-up operation through a
   weighted convex-subset partition function, looking for a construction
   below \(1/2\);
4. treat any claimed matching lower bound as a major theorem and subject it
   to an independent proof audit before calling Erdős 838 solved.

The upper theorem is complete enough for external review. The full problem
is not solved.
