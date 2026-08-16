# Robust weighted one-turn alignment for approximate strong trees

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

The coefficient-half strong-tree theorem is stable under weighted decoder
losses. The exact error is a directional **one-turn Carleson norm**, not the
sum of losses over all tree nodes.

At every ordered seam \(v=A\prec B\), allow separate decoder factors on the
two endpoint recurrences, on inherited ordinary banks, and on the forward
cap--cup bank. Define the directed loss potentials \(G_X,G_Y,G_M\) by
(4)--(6) below. Then the approximate weighted banks satisfy

\[
 \boxed{\quad
 \log M_{\rm app}(T)
 \ge {1\over2}(\log |T|)^2-O((\log |T|)^{3/2})-G_M(T).
 \quad}                                                            \tag{1}
\]

The term \(G_M(T)\) is sharp for this comparison: it is the largest total
loss along one inherited ordinary branch or along one cap arm, one cup arm,
and their turning seam. If every node loss is at most \(\gamma_v\), then

\[
 G_M(T)\le2\max_{\pi}\sum_{v\in\pi}\gamma_v,                       \tag{2}
\]

where \(\pi\) ranges over root-to-leaf paths.

Thus an induced approximate strong tree on \(m=n^{1-o(1)}\) physical labels
closes every fixed sub-half gap provided \(G_M=o((\log n)^2)\). More
generally, against a \((1/2-\delta)\)-target it is enough that

\[
 G_M<
 \left[{1\over2}\left({\log m\over\log n}\right)^2
                -\left({1\over2}-\delta\right)\right](\log n)^2
 -O((\log n)^{3/2}).                                               \tag{3}
\]

This theorem makes the remaining promotion gap precise. The common-core
forest and the stable circuit tournament have affordable *known*
description losses, but neither supplies the ordered endpoint recurrences.
The canonical Pascal geometry supplies a lossless unmarked strong tree, but
its marked all-delete release has a single decoder load
\(2^{\Theta((\log n)^2)}\), which exhausts (3). The missing parameter is
therefore a same-chart approximate strong-tree certificate together with
its one-turn Carleson norm; bounded branch arity or low rank alone is not
such a certificate.

## 1. The weighted approximate recurrence

Let \(T\) be an ordered full binary tree. At a node \(v=A\prec B\), put
\(a=|A|\) and \(b=|B|\). Let \(X^0,Y^0,M^0\) be the exact max-plus
strong-tree quantities:

\[
 \begin{aligned}
 X^0_v&=\max\{X^0_B,(b+1)X^0_A\},\\
 Y^0_v&=\max\{Y^0_A,(a+1)Y^0_B\},\\
 M^0_v&=\max\{M^0_A,M^0_B,X^0_AY^0_B\}.
                                                                    \tag{4}
 \end{aligned}
\]

All leaf values are one. Now let positive real weighted bank capacities
\(X_v,Y_v,M_v\) satisfy

\[
 \begin{aligned}
 X_v&\ge\max\left\{
       {X_B\over\lambda^X_{v,B}},
       {(b+1)X_A\over\lambda^X_{v,A}}\right\},\\
 Y_v&\ge\max\left\{
       {Y_A\over\lambda^Y_{v,A}},
       {(a+1)Y_B\over\lambda^Y_{v,B}}\right\},\\
 M_v&\ge\max\left\{
       {M_A\over\lambda^M_{v,A}},
       {M_B\over\lambda^M_{v,B}},
       {X_AY_B\over\lambda^M_{v,\times}}\right\},
                                                                    \tag{5}
 \end{aligned}
\]

where every \(\lambda\ge1\). The factors may include output overlap,
description multiplicity, fractional Hall congestion, or the density loss
from retaining a compatible local subbank.

The intended normalization is that each displayed quotient is a certified
ordinary-output capacity after dividing by its actual load. Then
\(V(P)\ge M_T\). The comparison theorem itself is purely algebraic and
continues to hold for arbitrary positive real capacities satisfying (5).

Write \(\ell=\log\lambda\). Define \(G_X=G_Y=G_M=0\) at leaves and

\[
 \begin{aligned}
 G_X(v)&=\max\{
      G_X(B)+\ell^X_{v,B},\
      G_X(A)+\ell^X_{v,A}\},\\
 G_Y(v)&=\max\{
      G_Y(A)+\ell^Y_{v,A},\
      G_Y(B)+\ell^Y_{v,B}\},                                     \tag{6}\\
 G_M(v)&=\max\{
      G_M(A)+\ell^M_{v,A},\
      G_M(B)+\ell^M_{v,B},\
      G_X(A)+G_Y(B)+\ell^M_{v,\times}\}.
 \end{aligned}
\]

These formulas are the exact decoder ledger. In particular, a loss at a
seam is not charged to an inherited child bank unless that bank really
passes through a new decoder at that seam.

## 2. Exact comparison theorem

> **Theorem 1 (loss-stable max-plus comparison).** Every system satisfying
> (5) obeys
> \[
> \begin{aligned}
> X_v&\ge2^{-G_X(v)}X^0_v,\\
> Y_v&\ge2^{-G_Y(v)}Y^0_v,\\
> M_v&\ge2^{-G_M(v)}M^0_v
> \end{aligned}                                                     \tag{7}
> \]
> at every node \(v\).

**Proof.** The leaf statement is equality. Suppose it holds in both
children. For the first recurrence in (5), its two displayed terms are at
least

\[
 2^{-G_X(B)-\ell^X_{v,B}}X^0_B,\qquad
 2^{-G_X(A)-\ell^X_{v,A}}(b+1)X^0_A.
\]

Both exponents are at most \(G_X(v)\), so their maximum is at least
\(2^{-G_X(v)}X^0_v\). The proof for \(Y\) is identical. For \(M\), the two
inherited terms use the first two entries in the last maximum of (6), while
the cross term is at least

\[
 2^{-G_X(A)-G_Y(B)-\ell^M_{v,\times}}X^0_AY^0_B.
\]

The last entry in (6) completes the induction. \(\square\)

Apply the exact weighted one-turn alignment theorem from
agent_asymptotic/NEXT_ENDPOINT_ATTACK.md to \(M^0_T\):

\[
 \log M^0_T\ge {1\over2}(\log|T|)^2
                         -O((\log|T|)^{3/2}).                      \tag{8}
\]

Combining (7)--(8) proves (1). No part of the reset proof must be rerun,
and no loss outside the one-turn witness is charged.

## 3. Root-path and guard-deletion corollaries

Suppose all seven logarithmic losses at node \(v\) are at most
\(\gamma_v\), and define

\[
 H(v)=\gamma_v+\max\{H(A),H(B)\},\qquad H(\text{leaf})=0.          \tag{9}
\]

Induction in (6) gives

\[
                 G_X(v),G_Y(v)\le H(v),\qquad G_M(v)\le2H(v).
                                                                    \tag{10}
\]

For the cross entry, use

\[
 G_X(A)+G_Y(B)+\gamma_v
 \le H(A)+H(B)+\gamma_v
 \le2H(v).
\]

The inherited entries satisfy the same bound. Since \(H(T)\) is the
root-path sum in (2), this proves (2).

There are two exact ways to account for guard deletion.

1. **Prune physical labels.** If the construction globally deletes guards
   and leaves an induced ordered strong tree on \(m\) labels, apply (1)
   directly with \(m\). This is preferable when all banks use the same
   pruned support.
2. **Lose only opposite singleton choices.** If a cap extension across
   \(A\prec B\) can use only \(b-g+1\) of the original \(b+1\) choices,
   and its decoder load is \(D_v\), put
   \[
       \lambda^X_{v,A}
            =D_v{b+1\over b-g+1}.                              \tag{11}
   \]
   The cup analogue is
   \[
       \lambda^Y_{v,B}
            =D'_v{a+1\over a-g'+1}.                             \tag{12}
   \]
   These are identities, not estimates. If \(g\le b/2\), then
   \[
      \log{b+1\over b-g+1}
          \le {2g\over(b+1)\ln2}.                               \tag{13}
   \]

Deleting \(g\) labels from an arbitrary rich child face family does **not**
by itself justify (11): one must certify the retained endpoint subbank and
include its actual density loss in \(\lambda\).

## 4. Audit of the three live candidates

### 4.1 Common-core deletion forest

At every nonterminal node of
COMMON_CORE_COMPLETION_PRIVATE_PETAL_TRICHOTOMY.md, a canonical uncovered
four-set partitions the carrier mass into at most four children. Selecting
one child costs at most two bits. If a branch has deletion depth \(D\), its
known path-description cost is at most \(2D\).

This is not yet a usable bound in (1). The proved depth is only

\[
                         D\le |U_{\mathcal S}|-q,                  \tag{14}
\]

and the union support may be near ambient even though \(q=O(\log n)\).
Thus (14) need not be \(o((\log n)^2)\). Alternatively one may retain all
leaves and charge the terminal Boolean-bank overlap once, but the theorem
currently gives no subquadratic bound on
\(\log\Lambda_{\rm leaf}\).

More fundamentally, a forest edge deletes one absent support label. It
does not produce a physical bipartition \(A\prec B\), the cap and cup
endpoint recurrences in (5), or one common projection chart. Even when its
branch/leaf decoder cost is affordable, the forest is not an approximate
strong tree.

The balanced-template equality family from
MINIMIZER_COHERENT_OVERLAP_STRONG_TREE_GATE.md is a useful calibration:
there \(\log\Lambda_{\rm leaf}=O(q)=O(\log n)\), fully affordable in (1),
but the strong tree comes from the external lexicographic construction,
not from the deletion forest.

### 4.2 Stable cross-circuit tournament core

STABLE_CROSS_CIRCUIT_TOURNAMENT_CORE.md retains
\(k=\Theta(\log\log n)\) partner classes and a common central core of size
\(n^{1-o(1)}\). Its uniform-type thinning costs

\[
                  \log\!\bigl(12\cdot24^k\bigr)=O(\log\log n),    \tag{15}
\]

and the preceding polynomial state fixing costs only \(O(\log n)\).
Even a polynomial decoder at each of the \(k\) levels would cost
\(O((\log n)(\log\log n))=o((\log n)^2)\). Numerically, this branch is
comfortably inside the Carleson budget.

It fails the geometric hypothesis. The theorem supplies label-disjoint
signed circuit matchings, not cap/cup endpoint extensions. The exact nested
triangle array in
FIRST_INCOHERENT_SIBLING_NESTED_TRIANGLE_BARRIER.md has the same uniform
signed type and zero compatibility between a complete partner trace and
any nonempty central face. Hence no recurrence in (5), with any finite
useful \(\lambda^M_{v,\times}\), follows from the tournament core alone.

### 4.3 Canonical Pascal marks

The unmarked Pascal cell is already a genuine ordered strong tree, so its
geometric recurrence has \(\lambda=1\). The canonical source fibre and
unordered role colouring in
CANONICAL_SOURCE_ROLE_DELETION_PASCAL_DENSITY_BARRIER.md lose only
\(N^{14}\) at entrance, i.e. \(14\log N=o((\log N)^2)\). These losses meet
the robust budget.

The marked source--release recurrence does not. For a terminal released
face \(U\), the exact all-delete load is

\[
          \Lambda(U)=\sum_{D\in\mathcal E}\omega(D,T)
                    \ge {V(P)\over4N^{14}}.                       \tag{16}
\]

Since the central Pascal coefficient is
\(\beta=1-1/(4\ln2)\),

\[
                   \log\Lambda(U)
                     =(\beta+o(1))(\log N)^2.                     \tag{17}
\]

Putting (17) into one forward decoder factor erases the half-scale return.
This is exactly the distinction between the lossless **unmarked** ambient
strong tree and the quadratically loaded **marked** release bank. Canonical
mark density and polynomial entrance descriptions do not solve it.

## 5. The missing promotion parameter

A future extraction theorem can now state the exact object it must return:

1. an induced set of \(m\) physical labels and one common chart;
2. an ordered binary tree on those labels;
3. weighted endpoint and ordinary banks satisfying (5) at every seam; and
4. a certified one-turn loss
   \[
                              \Gamma_{\rm turn}:=G_M(T).           \tag{18}
   \]

For a fixed \((1/2-\delta)\) counterexample, the sufficient quantitative
condition is exactly (3). Bounded circuit arity, logarithmic carrier rank,
polynomial entrance loss, and a large central support control only pieces
of this certificate. The two presently absent quantities are:

* **seam realization:** how many deletion/tournament nodes become actual
  same-chart endpoint recurrences; and
* **marked turn load:** the decoder factor on the cap--cup bank at the one
  turn.

The common-core forest lacks the first, the stable tournament lacks the
first despite an excellent loss budget, and the canonical Pascal marked
bank fails the second by (17). This is the sharp current barrier.

## 6. Verification

The exact verifier
verify_robust_weighted_approximate_strong_tree_gate.py enumerates all
ordered binary trees through seven leaves and many integer decoder-loss
assignments. Using exact rational capacities, it checks all three
comparisons in (7), the recursive one-turn budget (6), the root-path bound
(10), the guard-factor identities (11)--(13), and the fixed-gap threshold
(3).
