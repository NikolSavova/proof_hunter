# Heterogeneous threshold square mesh with harmonic loss

**Date:** 2026-08-16. All logarithms are base two.

## Verdict

The conjectural weighted hinge inequality is not needed to obtain a
pointwise square-mesh bound.  The exact hinged Kraft theorem can instead be
applied separately to the largest-child level sets.  The witnesses at
different levels need not nest.

Let an ordered generic macro chart have child sizes

\[
                         n_1,\ldots,n_m\geq1,
 \qquad N=\sum_i n_i,
 \qquad \ell_i=\log n_i.                                \tag{1}
\]

For child \(i\), let \(A_i\) and \(B_i\) be the exact weighted cap and cup
rewards in the substitution recurrence: every sibling \(j\) used by a path
contributes \(b_j=\log(1+n_j)\).  Put

\[
                  R_i=A_i+B_i,
 \qquad
                  \mathcal B=\max_i\left({\ell_i^2\over2}+R_i\right).
                                                                    \tag{2}
\]

If \(H_m=\sum_{j=1}^m1/j\), then

\[
 \boxed{
 \mathcal B\geq {1\over2}(\log N-\log H_m)^2
                  -{1\over2}(\log m)^2.}                \tag{3}
\]

Equivalently,

\[
 \mathcal B\geq {1\over2}(\log N)^2-{1\over2}(\log m)^2
                  -(\log N)\log H_m+{1\over2}(\log H_m)^2. \tag{4}
\]

Thus the surviving square-mesh conjecture is now a theorem up to the
explicit witness-switching loss

\[
                        (\log N)\log H_m
                 =O(\log N\log\log(m+1)).                \tag{5}
\]

This is a genuine local advance, but it does **not** by itself close the
unrestricted Erdős 838 proof.  On a recursive tree, the losses in (5) still
need a depth/entropy charge, and arbitrary point sets have not yet been
promoted to such a substitution chart.  Existing exact strong-tree
arguments already close fully ordered strong decompositions; the value of
(3) is that it removes weighted witness nesting as a local conjectural
input and identifies its precise lower-order cost.

## 1. Thresholded hinged witnesses

Relabel the children so that

\[
                         n_1\geq n_2\geq\cdots\geq n_m.   \tag{6}
\]

For each \(j\), restrict the macro chart to the first \(j\) children and
recompute its unweighted endpoint ranks \(\alpha_j(i),\beta_j(i)\).  The
hinged Kraft theorem gives an anchor \(i\leq j\) with

\[
                  \alpha_j(i)+\beta_j(i)\geq\lceil\log j\rceil. \tag{7}
\]

The two witnessing paths in the induced chart are also paths in the full
chart.  Every nonanchor vertex on them belongs to the first \(j\) children,
so its weighted contribution is at least

\[
                         \log(1+n_j)\geq\ell_j.           \tag{8}
\]

Moreover \(\ell_i\geq\ell_j\).  Consequently the **full-chart** reward at
that anchor satisfies

\[
 \mathcal B
 \geq {\ell_i^2\over2}+R_i
 \geq {\ell_j^2\over2}+\ell_j\lceil\log j\rceil
 \geq {\ell_j^2\over2}+\ell_j\log j.                    \tag{9}
\]

This is the key point: (9) is obtained independently for every threshold.
The maximizing anchor and its cap/cup paths may change arbitrarily with
\(j\).  The false nested-threshold uncrossing statement is never used.

## 2. The harmonic summation

Set

\[
              q=\log m,
 \qquad       T=\sqrt{2\mathcal B+q^2}.                  \tag{10}
\]

Equation (9) implies

\[
  (\ell_j+\log j)^2
       \leq2\mathcal B+(\log j)^2
       \leq2\mathcal B+q^2=T^2.                         \tag{11}
\]

All terms are nonnegative, hence

\[
                         n_j=2^{\ell_j}\leq {2^T\over j}. \tag{12}
\]

Summing (12) over all children gives

\[
                         N\leq2^T H_m.                   \tag{13}
\]

Since \(N\geq m\geq H_m\), equations (10)--(13) give

\[
             \log N-\log H_m\leq T,
\]

and squaring proves (3).

The harmonic factor is the entire price of changing witnesses across
thresholds.  No geometric regularity, stretchability beyond the macro
chart, child homogeneity, or bounded arity is used.

## 3. What this settles and what it does not

The prior local hierarchy was:

1. the zero-defect weighted hinge inequality -- false;
2. a literal nesting of longest threshold paths -- false;
3. the exact square mesh
   \(\mathcal B\geq(\log N)^2/2-(\log m)^2/2\) -- supported by finite
   tests but unproved.

Theorem (3) bypasses the first two and proves the third with only the
explicit term (5).  In particular, if
\(\log m=o(\log N)\), the local loss is \(o((\log N)^2)\).

What remains is not a scalar local inequality.  A complete proof still
needs one of the following global operations:

- charge the harmonic losses along a recoverable recursive history;
- promote an arbitrary least counterexample to a same-chart strong tree or
  mixed seam with controlled history load; or
- obtain the missing gain from the selected-family circuit/profile bank
  without first constructing such a tree.

The unrestricted campaign currently points to the third alternative.
The fixed-size supersaturation audit shows that ordinary double counting,
one positive-fraction transversal box, and scalar hull identities cannot
supply that gain.

## 4. Verification

Run

~~~text
python3 phase2/loop/erdos838/verify_heterogeneous_threshold_square_mesh.py
~~~

The verifier checks the harmonic algebra on exhaustive and randomized
child-size vectors, reconstructs weighted rewards for all edge orders at
arity four, checks every thresholded induced chart against the full reward,
and exercises stretchable reflection-order examples including the known
weighted-hinge counterexample.  The proof of (3) is the exact argument in
Sections 1--2; the finite computation is an independent regression rather
than a substitute for it.
