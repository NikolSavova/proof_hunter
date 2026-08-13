# Tree alignment: an audit of the slack-square route

All logarithms in this note are base two.  The conclusion is deliberately
negative but fairly sharp: I did not obtain a proof of the tree alignment
conjecture.  I found a promising strengthened invariant, together with good
finite evidence for it, but also identified exactly why neither the slack
square nor a scalar induction in the three counts can currently prove that
invariant.

## 1. Exact coordinates for the obstruction

For a strong glue `T=A prec B`, put `a=|A|`, `b=|B|` and

\[
 F=C(A)U(B),\qquad G=C(B)U(A),\qquad
 R(X)=\sqrt{C(X)U(X)},\quad
 d(X)={1\over2}\log {C(X)\over U(X)}.
\]

Thus `C(X)=R(X)2^{d(X)}` and `U(X)=R(X)2^{-d(X)}`.  The
two oriented products are

\[
 F=R(A)R(B)2^{d(A)-d(B)},\qquad
 G=R(A)R(B)2^{d(B)-d(A)}.                 \tag{1}
\]

The exact recurrences imply

\[
 C(T)U(T)=G+(a+1)C(B)U(B)+(b+1)C(A)U(A)
            +(a+1)(b+1)F.                 \tag{2}
\]

The square in identity (9) of `lower_bound_frontier.md` is therefore

\[
 \left(\sqrt G-\sqrt{(a+1)(b+1)F}\right)^2.       \tag{3}
\]

In particular the square is **zero** precisely when

\[
 d(A)-d(B)=-{1\over2}\log((a+1)(b+1)),
 \qquad G=(a+1)(b+1)F.                    \tag{4}
\]

This is an important limitation.  Zero slack does not mean that the
forward product is well aligned: the uncounted reverse product can still be
a factor `(a+1)(b+1)`, hence up to order `n^2`, larger.  Equivalently, the
square only detects bad alignment beyond the polynomial allowance in (4).
A proof that iterates (3) independently at each node can consequently lose
`O(log n)` at every relevant glue.  With `Theta(log n)` size scales, that
is exactly quadratic and is not an acceptable error.  The polynomial
allowances have to telescope through the evolution of `d`; the square by
itself does not do so.

## 2. A strengthened invariant suggested by exact enumeration

Define

\[
 H(T):=W(T)2^{-|d(T)|}
      =W(T)\sqrt{{\min(C(T),U(T))\over\max(C(T),U(T))}}.       \tag{5}
\]

Since `H(T)<=W(T)`, the following stronger statement would prove the tree
alignment conjecture, in fact without the conjectured lower-order loss:

\[
 \boxed{H(T)\ \ge\ 2^{\frac12(\log |T|)^2}.}                  \tag{6}
\]

I exhaustively generated all distinct oriented triples `(C,U,W)` for all
binary trees through 13 leaves (no Pareto pruning).  The largest value of

\[
 {1\over2}(\log n)^2+|d(T)|-\log W(T)
   =\log\!\left({2^{(\log n)^2/2}\over H(T)}\right)           \tag{7}
\]

was negative for every `n`.  The worst values by size were

| `n` | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| maximum (7) | -1.085 | -1.440 | -1.614 | -1.734 | -1.805 | -1.866 | -1.923 | -1.967 | -1.984 | -1.990 | -1.999 | -1.992 |

Thus the observed margin is not marginal: near `n=12` the left hand side
of (6) is about four times its target.  One extremal triple at `n=12` is
`(C,U,W)=(735,123,840)` (or its mirror).  A separate randomized generation
of 500 valid recursively glued states at every size through 2,000 leaves
also found no violation; its smallest ratio `H/2^{(log n)^2/2}` was the
two-leaf value `3/sqrt(2)=2.121...`.  Random search is only corroboration,
not a certificate beyond the exhaustive range.

The factor `2^{-|d|}` has the right qualitative behavior.  A node with a
huge one-sided cap/cup mass is not allowed to claim the whole benefit of
that mass.  When a cup-heavy left child is glued to a cap-heavy right child,
the small forward product can coexist with a huge reverse product, but the
parent typically becomes much more balanced; (5) records that imbalance
reset.

## 3. Why the obvious induction on `H` fails

A small-state experiment suggests the attractive local inequality

\[
 H(T)\stackrel{?}{\ge}{3\over2}
 \sqrt{(a+1)(b+1)H(A)H(B)}.                       \tag{8}
\]

It is true for all exhaustive states in the small computation and is an
equality at the glue of two leaves.  It is nevertheless false for actual
strong-decomposition states.  A randomized recursive generator produced,
for a valid split `a=268`, `b=192`, child triples

\[
 (C_A,U_A,W_A)=(7704663634,4336842420,1523921008784810),
\]

\[
 (C_B,U_B,W_B)=(208321330076475,2748081,45077975819899871).
\]

The exact glue recurrences give

\[
 (C_T,U_T,W_T)=
 (209808330157837,5076076209,67774936572671035),
\]

and the ratio of the two sides of (8), omitting the proposed factor `3/2`,
is about `0.0190`.  Hence even the same inequality with constant one is
false.  This is not an abstract fake triple: both children were produced
recursively from leaves by (3).

Other natural scalar recurrences fail for the same reason.  Exhaustive
small-state tests already give

\[
 {H(T)\over (b+1)H(A)+(a+1)H(B)}<0.415,
\]

and randomized larger trees drive one-sided or geometric-mean ratios much
lower.  Thus (6), if true, is a genuinely global statement; `H(A),H(B)` and
the sizes do not retain enough directional information for a local Bellman
inequality.

There is an even stronger warning about an induction that forgets
realisability and keeps only the already-proved product lower bound (8) of
the frontier note.  Treating child `(C,U)` values as arbitrary subject to
their individual size and product lower bounds produces numerical local
counterexamples to (6) with arbitrarily large margins.  Such triples need
not be realizable.  Therefore the product theorem plus a one-node algebraic
inequality cannot establish alignment: one needs a hereditary constraint
on which imbalances can be carried by a subtree.

## 4. The precise missing telescoping lemma

Write the forward-to-reverse log discrepancy at a node as

\[
 q=d(B)-d(A)={1\over2}\log(G/F),
 \qquad p={1\over2}\log((a+1)(b+1)).               \tag{9}
\]

The square (3) is small exactly when `q` is close to `p`.  Hence every bad
node has one of two forms:

1. `q-p` is large, in which case (3) supplies quantitative product slack;
2. `q=p+O(1)`, in which case the uncounted reverse/forward gap is only the
   size-polynomial factor, but a change of about `p` units of imbalance is
   being matched across the two children.

A sufficient next lemma would charge the second kind of node to variation
of imbalance along heavy paths.  One concrete formulation is: for some
choice of one child at every internal node, the sum over the selected
root-to-leaf paths of the allowances

\[
 \min\{p,\,|d(A)-d(B)|\}                           \tag{10}
\]

at nodes whose forward term is below the target is
`O(log n log log n)`, after nodes with large square slack are charged to
the excess in `log R`.  Proving any equivalent amortized statement would
turn the sharp product theorem into

\[
 \log W(T)\ge {1\over2}(\log n)^2-O(\log n\log\log n).
\]

What is missing is exactly the hereditary mechanism ensuring this
telescoping.  Parent imbalance is the difference of logarithms of two sums,

\[
 d(T)={1\over2}\log{C(B)+(b+1)C(A)
                         \over U(A)+(a+1)U(B)},                 \tag{11}
\]

so it is not an additive cocycle of `d(A),d(B)`.  In an anti-aligned merge
the dominating summands can switch sides, resetting rather than adding
imbalance.  That reset is exactly what the successful potential (5) seems
to exploit, and exactly what the scalar child recurrences above discard.

## 5. Verdict

I found no counterexample to the tree alignment conjecture and no
asymptotic variational obstruction realized by strong-decomposition trees.
The best new candidate is the stronger invariant (6), with exhaustive
evidence through 13 leaves and broad randomized evidence through 2,000.
But it does not admit the tempting one-step induction, and the exact square
(9) alone is insufficient because of the zero-slack polynomial gap (4).
The proof gap is now precise: establish an amortized imbalance-reset lemma
retaining at least one extra piece of hereditary profile information beyond
`(|T|,C,U,W)`, or find a realizable multiscale tree that repeatedly spends
the allowance (4) without paying either `W` or accumulated product slack.
