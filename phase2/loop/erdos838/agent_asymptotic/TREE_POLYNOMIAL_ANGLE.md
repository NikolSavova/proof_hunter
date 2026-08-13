# Fixed-size caterpillars from every ordered tree, and the root-position barrier

All logarithms are base two.  This note investigates the proposed
size-polynomial/random-restriction route to the ordered-tree alignment
theorem.  It proves a sharp uniform fixed-size lemma for the nearest larger
pattern family.  The lemma has exactly the desired coefficient `1/2` and
the desired `O(log n log log n)` error.  An explicit ordered tree then shows
why it does not imply the theorem: a one-path caterpillar is rooted at an
endpoint of its spine, whereas a non-pure pattern counted by `W` is rooted
at the interior turn.  Alternating the attachment directions loses half the
quadratic exponent.

## 1. Size-generating polynomials

For a nonempty leaf subset, mark its size by `x`.  If `T=A prec B`, with
`a=|A|` and `b=|B|`, the exact polynomials for left combs, right combs, and
left--right combs are

\[
\begin{aligned}
 C_T(x)&=C_B(x)+(1+bx)C_A(x),\\
 U_T(x)&=U_A(x)+(1+ax)U_B(x),\\
 W_T(x)&=W_A(x)+W_B(x)+C_A(x)U_B(x).       \tag{1}
\end{aligned}
\]

The last product is homogeneous in subset size: its coefficient of `x^k`
is `sum_{r+s=k}c_r(A)u_s(B)`.  Also, if every leaf is retained
independently with probability `p`, then `W_T(p)` is the expected number of
nonempty patterns counted by `W` in the restriction.  Thus polynomial
evaluation is exactly random leaf sampling, not merely an analogy.

Let `E_T(x)` count all leaf subsets whose reduced induced rooted tree is an
**endpoint-rooted binary caterpillar**, with arbitrary left/right attachment
word.  (All one- and two-leaf subsets are included.)  The exact recurrence is

\[
 E_T(x)=(1+bx)E_A(x)+(1+ax)E_B(x)-abx^2.   \tag{2}
\]

Indeed, a crossing caterpillar with at least three leaves has one singleton
root branch and an endpoint-rooted caterpillar in the other branch.  The
subtracted term corrects the double count when both branches contribute one
leaf.

## 2. A uniform growing-pattern theorem

The fixed-pattern caterpillar inducibility results in the literature do not
give useful errors for pattern size proportional to `log n`.  The following
elementary heavy-path argument does.

### Lemma (fixed-size endpoint caterpillars)

Let `T` be any rooted full binary tree with `n>=4` leaves and put
`L=log n`, `epsilon=1/L`, and

\[
 \alpha={1-\epsilon\over2},\qquad
 k=\left\lfloor {L-1\over -\log\alpha}\right\rfloor.          \tag{3}
\]

Then `k=L-O(1)` and `T` has at least

\[
 \epsilon^k n^k\alpha^{k(k-1)/2}
 =2^{\frac12L^2-O(L\log L)}                  \tag{4}
\]

distinct `(k+1)`-leaf subsets inducing endpoint-rooted caterpillars.

### Proof

Starting at the root, repeatedly follow a child with at least as many leaves
as its sibling.  Write `m_i` for the current subtree size and `s_i` for the
discarded sibling size, so

\[
 m_{i+1}=m_i-s_i,\qquad m_{i+1}\ge m_i/2.        \tag{5}
\]

Partition an initial segment of the discarded siblings into consecutive
batches as follows.  If a batch starts when the current size is `M_j`, end
it at the first index for which the sibling sizes accumulated in that batch
have sum `S_j>=epsilon M_j`.  Immediately before its last sibling is
discarded, the current size is greater than `(1-epsilon)M_j`.  By (5), after
that last discard the next batch therefore starts with size

\[
 M_{j+1}>{1-\epsilon\over2}M_j=\alpha M_j.       \tag{6}
\]

Consequently

\[
 M_j>n\alpha^j,qquad S_j\ge\epsilon n\alpha^j.  \tag{7}
\]

The choice of `k` ensures that the first `k` batches exist: before batch
`j<k` the lower bound in (7) is at least two, so the remaining total discard
`M_j-1` reaches `epsilon M_j`.

From every one of these `k` batches choose one discarded sibling, and then
one leaf in that sibling.  Finally choose one fixed leaf below the last
batch on the followed path.  After unary vertices are suppressed, the
chosen leaves induce an endpoint-rooted caterpillar.  Choices made in
different batches give different leaf subsets, and batch `j` offers exactly
`S_j` choices.  Hence their number is at least

\[
 \prod_{j=0}^{k-1}S_j
 \ge \epsilon^k n^k\alpha^{k(k-1)/2}.            \tag{8}
\]

Since `-log alpha=1-log(1-1/L)=1+O(1/L)`, (3) gives `k=L-O(1)`.
Taking logarithms in (8) gives

\[
 kL-k\log L-{k(k-1)\over2}\bigl(1+O(1/L)\bigr)
 ={1\over2}L^2-O(L\log L),                       \tag{9}
\]

as required.  \(\square\)

This is a finite, uniform version of the formal growing-`k` optimization
behind fixed-pattern caterpillar density.  It also supplies an explicit
coefficient of the polynomial (2), rather than only a bound on `E_T(1)`.

## 3. Why this sharp lemma does not count `W`

The distinction is the position of the root on the induced internal spine.
Every caterpillar constructed in the proof follows one downward path and
attaches singleton leaves along it.  Its root is therefore an **endpoint**
of the internal spine.  In contrast, a pattern counted by `W` has form

\[
 L_p\mathbin\wedge R_q.                            \tag{10}
\]

When `p,q>1`, its root is the **interior turn** of the spine and both root
branches are nontrivial.  An endpoint-rooted caterpillar is in the family
(10) only in the endpoint cases `p=1` or `q=1`, namely when it is a pure
right or pure left comb.  A change of attachment direction along a single
root-to-leaf path does not create the interior-root pattern (10).

This invalidates the tempting statement that an arbitrary attachment word
contains a large one-turn subsequence which is automatically counted by
`W`.  Along one downward path, the usable subsequence must actually be
**monochromatic**.

## 4. A precise alternating-spine obstruction

The loss is quadratic, not a harmless factor exponential in the pattern
size.  For integer `L`, make a `2^L`-leaf tree with a designated path as
follows.  At a path node of current size `2^j`, give the continuation and
the discarded sibling `2^{j-1}` leaves each.  Alternate whether the
continuation is the left or the right child.  The internal structures of the
discarded sibling subtrees may be arbitrary.

The designated path has sibling weights

\[
 2^{L-1},2^{L-2},\ldots,2,1.                      \tag{11}
\]

Choosing one sibling leaf at every level and one terminal leaf produces

\[
 \prod_{j=0}^{L-1}2^j=2^{L(L-1)/2}                \tag{12}
\]

distinct `(L+1)`-leaf endpoint-rooted caterpillars.  This realizes the
quadratic scale in (4).  But their attachment word alternates, independently
of which leaves were selected.  None of the full-size witnesses in (12) is
a pure comb once `L>=2`.

Even allowing arbitrary subchoices from the path does not repair the
coefficient.  The total number of pure-left witnesses is at most

\[
 \prod_{j\text{ of one parity}}(1+2^j),
\]

and the analogous formula holds for pure-right witnesses.  Therefore the
number of path witnesses that are counted by `W` is at most

\[
 2^{L^2/4+O(L)},                                   \tag{13}
\]

only half the exponent in (12).  Equation (13) concerns the canonical
single-path witness family; the whole ambient tree can of course contain
many additional `W`-patterns inside or between the sibling subtrees.  Thus
this is a rigorous obstruction to the proof method, not a counterexample to
the ordered-tree theorem.

## 5. Consequences for random restriction and the remaining gap

Random sampling does not change the root-position problem.  Evaluating
`E_T(p)` discounts (12) by `p^{L+1}`, while evaluating `W_T(p)` retains only
the monochromatic subfamilies (13) from this path.  For any
`p=2^{-o(L)}`, the gap between their logarithms remains
`L^2/4-o(L^2)`.  Pigeonholing (4) by subset size likewise cannot turn an
endpoint-rooted restriction into an interior-rooted one.

Accordingly, a uniform caterpillar-density induction can prove the desired
coefficient for `E`, but not for `W`.  To finish the ordered-tree theorem it
must become a genuinely **two-arm** argument: find an internal node `v`
whose left arm supplies many left combs and whose right arm supplies many
right combs, so that

\[
 [x^r]C_{A_v}(x)\,[x^s]U_{B_v}(x)                \tag{14}
\]

is large for some `r+s=Theta(log n)`.  Summing (14) over `v` is exactly
`W_T(x)-nx`; no one-path polynomial contains this alignment information.

The new rigorous result is therefore (4), and the exact unresolved step is
the passage from one-arm endpoint-rooted caterpillar mass to two-arm
interior-root mass.  The alternating dyadic spine proves that any passage
which only extracts a monochromatic subsequence from one heavy path is
limited to coefficient `1/4`.
