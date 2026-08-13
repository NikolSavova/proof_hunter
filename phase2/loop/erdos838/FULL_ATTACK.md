# Erdős 838: current full-solution attack

> Status, 2026-08-13. There is now a self-contained candidate proof of the
> unconditional upper coefficient \(1/2\), with two independent exact
> rational-coordinate audits. The original limit problem remains open. The
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

The fixed-template obstruction extends to nonstationary homogeneous
compositions. If \(Q_t=S_t[Q_{t-1}]\), put
\(\ell_t=\log|S_t|\) and \(L_t=\sum_{i\leq t}\ell_i\). The unavoidable
two-block terms and the cap--cup theorem give

\[
 \log W(Q_d)\geq
 \frac12\left(L_{d-1}^2-\sum_{t<d}\ell_t^2\right). \tag{10a}
\]

Consequently no stationary, periodic, finite-menu, or slowly growing
template schedule can beat \(1/2\). Polynomial random thinning preserves
the same coefficient as well. A better construction would have to use a
macroscopic scale jump or heterogeneous clusters with deliberate directional
cap/cup anti-alignment.

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

Exact Pareto dynamic programming through \(N=19\) finds no counterexample
and gives decreasing normalized minima, but finite sizes are too small to
distinguish \(1/2\) from larger constants.

There is nevertheless a new unconditional result in this class:

\[
\boxed{\quad
\log W(T)\ge {1\over3}(\log N)^2-O(\log N\log\log N).
\quad}                                             \tag{11c}
\]

The proof follows a larger child until the current subtree has lost a
factor \((\log N)^4\).  If a discarded sibling has relative size at least
\(1/(\log N)^2\), the two child product bounds and a one-node directional
minimax give (11c).  Otherwise the path has more than
\(2(\log N)^2\log\log N\) levels; a majority of the discarded siblings lie
on one side, and arbitrary subchoices of fixed leaves from those siblings
form distinct pure caps or cups.  Full constants are in
`agent_geometry/TREE_AMORTIZED_AUDIT.md`.

An exact max-endpoint reduction makes the remaining \(1/2\) target smaller.
Let \(X\) be the largest number of caps with one fixed left endpoint, \(Y\)
the reflected cup quantity, and \(M=\max_{s<t}c(s,t)u(s,t)\).  Then

\[
\begin{aligned}
X_T&=\max\{(b+1)X_A,X_B\},\\
Y_T&=\max\{Y_A,(a+1)Y_B\},\\
M_T&=\max\{M_A,M_B,X_AY_B\},                       \tag{11d}
\end{aligned}
\]

and \(M\le W\le N^2M\) for \(N\ge2\).  Thus tree alignment is exactly a
weighted one-turn-path theorem for the three max-plus recurrences (11d).
The imbalance function \(\phi(x,y)=(x-y)^2/(x+y)\) is quasiconvex under
coordinatewise maximum, but the required multiscale inequality is not yet
proved.

There is now a sharp theorem for the *unoriented* product. Put
\(R(T)=\sqrt{C(T)U(T)}\). Cauchy--Schwarz in (11) gives, when
\(|A|=a,|B|=b\),

\[
 R(T)\geq\sqrt{b+1}R(A)+\sqrt{a+1}R(B).
\]

Following the larger child and summing its discarded-sibling weights proves

\[
 C(T)U(T)\geq
 2^{\frac12(\log N)^2-\log N}.                    \tag{11a}
\]

The coefficient is sharp, but \(W\geq\sqrt{CU}\) recovers only \(1/4\).
The exact Cauchy--Schwarz remainder identifies what is missing:

\[
\begin{split}
C(T)U(T)={}&
\left(\sqrt{b+1}R(A)+\sqrt{a+1}R(B)\right)^2\\
&+\left(\sqrt{C(B)U(A)}-
\sqrt{(a+1)(b+1)C(A)U(B)}\right)^2.               \tag{11b}
\end{split}
\]

Thus every suppressed forward term in \(W\) creates explicit reverse-
alignment slack in the product recurrence. Charging that slack across the
tree is the cleanest current route to the matching decomposable theorem;
`lower_bound_frontier.md` gives the proof of (11a) and the exact conjecture.

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
bound has coefficient \(1/2\) in the same base-\(2\) normalization. The best
current graph lower coefficient located in this attack is \(1/4\), due to
Feige--Kenyon--Kogan (2020). Bal--Cutler--Pebody (2025) package its core as a
product count for nested monochromatic-neighborhood histories, with only a
factorial fibre loss. There is no known reduction between that problem and
Erdős 838, but the structural analogy is close: both ask for total
multiplicity rather than the size of one Ramsey witness.

This makes a quick matching lower bound unlikely. It also suggests that the
right tools may be Ramsey--Turán stability, weighted containers, or entropy
of path-count profiles rather than another application of the existence
theorem.

There is nevertheless an exact geometric analogue of the *history-counting*
half of the graph proof. A nested endpoint-pair process produces

\[
 2^{\frac12(\log N)^2-O(\log N\log\log N)}       \tag{14}
\]

hinged orientation histories in every ordered point set. The finite bound
and proof are in `agent_geometry/HISTORY_ATTACK.md`. What fails is the
compression half: vertices carrying the same history sign need not be a cap
or cup, and a hinged history need not even be a split polygon. Both failures
have exact rational witnesses. An infinite rational family is simultaneously
hinged and split but has largest convex subset only about half its points.
Thus (14) has precisely the right mass, but converting it to shared-endpoint
cap--cup pairs remains a genuine theorem rather than a transcription of the
graph argument.

There is also an exact ordered-tree reformulation of the decomposable lane.
In a strong-decomposition tree, a leaf subset is a cap exactly when its
reduced induced ordered tree is a left comb; cups give right combs; convex
subsets give a left-comb branch joined to a right-comb branch. Hence the
tree-alignment conjecture is equivalently:

> Every ordered full binary tree with \(N\) leaves has
> \(2^{(1/2-o(1))(\log N)^2}\) leaf subsets whose reduced induced tree is a
> one-turn left--right comb.

This transfer is exact. The search in
`agent_killsearch/RECURRENCE_TRANSFER.md` found no growing-pattern theorem
that implies it. Fixed-pattern caterpillar inducibility is nearby, but its
available error is vacuous at pattern size \(\Theta(\log N)\), and it counts
a different rooted shape.

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

1. use the proved tree product bound (11a) and exact slack (11b) to prove
   the tree-alignment conjecture;
2. build a weighted endpoint-history analogue of the graph good-sequence
   count, with a \(2^{O(k\log k)}\) fibre bound;
3. in parallel, run the general Baek--Balko blow-up operation through a
   weighted convex-subset partition function, looking for a construction
   below \(1/2\);
4. treat any claimed matching lower bound as a major theorem and subject it
   to an independent proof audit before calling Erdős 838 solved.

The upper theorem is complete enough for external review. The full problem
is not solved.
