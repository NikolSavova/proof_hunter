# Terminal entropy in the role-monotone mixed-face forest

**Date:** 2026-08-15.  All logarithms are base two.  This refines
`ROLE_MONOTONE_MIXED_FACE_FOREST.md`.

## Verdict

The role forest has an exact terminal potential which separates the desired
quasipolynomial multiplier from one sharply described residual.

At a forest node and a currently eligible role \(i\), let

\[
 a(v,i)=\#\{z\in X_i:\text{the }(i,z)\text{ record class is nonempty}\}.
                                                               \tag{1}
\]

The forest retains a heaviest class, so it loses at most \(a(v,i)\), not the
full alphabet size \(d_i=|X_i|\).  For a terminal output \(O\), let

\[
 C(O)=\prod_{(v,i)\text{ on its path}}a(v,i),
 \qquad
 Q(O)={P_0\over C(O)},qquad P_0=\prod_i d_i.          \tag{2}
\]

If \(\mu(O)\) is the routed terminal record weight, then

\[
 \boxed{\quad
                    \sum_O\mu(O)C(O)\ge M,
 \qquad \mu(O)\le\delta.
 \quad}                                                \tag{3}
\]

Thus for every threshold \(Q_0\ge1\),

\[
 \boxed{\quad
   \sum_{O:Q(O)\ge Q_0}\mu(O)C(O)
                      \le {\delta V(P)P_0\over Q_0}.
 \quad}                                                \tag{4}
\]

If the high-\(Q\) terminals carry at least a \(\theta\)-fraction of the
potential in (3), then

\[
                         M\le {\delta V(P)P_0\over\theta Q_0}. \tag{5}
\]

Choosing \(Q_0=n^{B\log\log n}=2^{B L\log L}\) recovers exactly a
quasipolynomial multiplier.  Hence this branch closes whenever \(B\) exceeds
the accumulated description/load constant in the live normalization.

The complementary branch is equally rigid.  The identity

\[
 Q(O)=
  \prod_{i\text{ undeleted}}d_i
  \prod_{(v,i)\text{ deleted}}{d_i\over a(v,i)}        \tag{6}
\]

shows that \(Q(O)<Q_0\) means simultaneously:

1. almost all large-alphabet completion roles were deleted; and
2. the deleted roles had almost complete actual label branching.

For example, if every \(d_i\ge n^\alpha\) and
\(Q_0=n^{B\log L}\), at most

\[
                         {B\over\alpha}\log L          \tag{7}
\]

roles remain.  Moreover

\[
          \sum_{(v,i)\text{ deleted}}\log{d_i\over a(v,i)}
                            <B L\log L.                \tag{8}
\]

If \(s=\Theta(L)\), all but an \(\varepsilon\)-fraction of the deleted
levels obey

\[
                         a(v,i)\ge {d_i\over L^{B'/\varepsilon}} \tag{9}
\]

for the corresponding absolute constant \(B'\).  This is the exact
all-roles-deleted, near-complete guard layer left after the capacity split.

The residual is real at the present hypotheses.  The anti-aligned complete
role product has \(a(v,i)=d_i\) at every level and deletes every completion
role, so \(C=P_0\), \(Q=1\), and the terminal output is only \(U\).  More
importantly, the central Pascal prefix-DAG construction is a genuine
live-normalized analogue: both fixed-rank child banks are
\(V2^{-O(L\log L)}\), the prefix branching product equals the whole released
family, and every leaf erases its full tag.  Its coefficient is greater than
one half, so it is not a minimizer counterexample; it proves that live
normalization alone does not pay the low-\(Q\) branch.

There is nevertheless an exact coefficient threshold.  Since the role
supports are disjoint and have total size at most \(N\), AM--GM gives

\[
                         P_0\le\left({N\over s}\right)^s. \tag{9a}
\]

Write \(\log V=cL^2+o(L^2)\), \(\log N=L+o(L)\), and
\(s=\alpha L+o(L)\).  Then

\[
 \log{P_0\over V}
   \le(\alpha-c)L^2-\alpha L\log L+O(L).              \tag{9b}
\]

Thus the forest already gives a fixed quadratic-exponent saving when
\(\alpha<c\).  At the critical rank \(\alpha=c\), it gives the explicit
quasipolynomial saving

\[
                         {P_0\over V}
                    \le n^{-c\log L+O(1)}.             \tag{9c}
\]

Only the excess-rank window \(\alpha>c\) can absorb this multiplier.  This
matches the independently isolated condition
\(s-c\log N=\Omega(L)\); the all-deleted analysis does not remove that final
linear excess.

Consequently the next theorem is now precise: on the coefficient-below-half
or minimizer slice, rule out terminal potential concentrated on paths which
delete all but \(O(\log L)\) completion roles with aggregate branching
defect only \(O(L\log L)\), or charge those paths to an ambient completion/
directional-profile bank.  No such coefficient-specific theorem is proved
here, and no EIC' closure is claimed.

## 1. Proof of the terminal-potential identity

For a forest node \(v\), measure descendant path cost relative to \(v\), and
let

\[
 \Phi(v)=\sum_{O\text{ below }v}\mu(O)
          \prod_{e\in[v,O]}a(e).                      \tag{10}
\]

We prove \(\Phi(v)\ge m(v)\), where \(m(v)\) is the record mass at \(v\).
The good mass \(g(v)\) terminates immediately and contributes \(g(v)\).
Partition the bad mass by its smallest eligible role \(i\).  If that role
has nonempty label classes of total mass \(b_i\), the selected child has
mass at least \(b_i/a(v,i)\).  By induction its relative descendant
potential is at least its mass; multiplying by the edge cost \(a(v,i)\)
contributes at least \(b_i\).  Therefore

\[
                         \Phi(v)\ge g(v)+\sum_i b_i=m(v). \tag{11}
\]

At the root, the relative path cost is \(C(O)\), proving the first half of
(3).  The empty-role decoder from the preceding report says that \(O\)
recovers the literal endpoint pair, proving \(\mu(O)\le\delta\).

## 2. Capacity split

For \(Q(O)\ge Q_0\), equations (2)--(3) give

\[
 \mu(O)C(O)=\mu(O){P_0\over Q(O)}
                      \le\delta {P_0\over Q_0}.        \tag{12}
\]

There are at most \(V(P)\) ordinary terminal outputs.  Summing (12) proves
(4), and the \(\theta\)-heavy implication is (5).

For a deleted role, \(a(v,i)\le d_i\).  Separate the deleted and undeleted
factors of \(P_0/C(O)\) to obtain (6).  Every factor is at least one.  Taking
logs proves (7)--(8).  Markov's inequality applied to the nonnegative
defects \(\log(d_i/a(v,i))\) gives (9).

Finally, (9a) is ordinary AM--GM applied to \(d_1,\ldots,d_s\), since
\(\sum_i d_i\le N\).  Substituting \(s=\alpha L+o(L)\) and
\(\log N=L+o(L)\) yields

\[
 \log P_0\le s(\log N-\log s)
   =\alpha L^2-\alpha L\log L+O(L),                  \tag{12a}
\]

which proves (9b)--(9c).

## 3. Exact all-deletion saturation

In the rational anti-aligned verifier, the completion cloud is partitioned
into \(s\) roles of size \(d\), and every transversal is present.  The
released trace has rank greater than two.  At each node every value of the
smallest eligible role occurs, so

\[
                         a(v,i)=d.                     \tag{13}
\]

The selected completion side can remain incompatible until it is empty.
Every terminal path then has

\[
                         C=d^s=P_0,qquad Q=1.          \tag{14}
\]

The terminal potential in (3) exactly restores the discarded completion
word count, but produces no more than the released bank.  The example is
non-live because its Boolean cloud reservoirs dominate the bounded-rank
layers.

`HIGH_TRANSVERSAL_PASCAL_PREFIX_DAG_BARRIER.md` supplies the scalable live
calibration.  Its exact verifier checks that the product of successive
weighted dispersions is the entire fixed-rank released family and that all
leaves collide after the prefix is erased.  It blocks a general live-only
promotion of (14) to an ambient mixed profile bank.  A coefficient-specific
promotion remains open.

## Verification

Run

```text
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_role_forest_terminal_entropy_split.py
```

The verifier builds the rational weighted role forest, checks (3) exactly,
checks (4) at every attained threshold, verifies the factorization (6), and
confirms the full-branching/all-deletion equality \(C=P_0,Q=1\).  The live
Pascal calibration has the independent passing verifier
`verify_high_transversal_pascal_prefix_dag.py`.
