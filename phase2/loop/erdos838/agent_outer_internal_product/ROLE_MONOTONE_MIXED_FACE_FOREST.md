# Empty completion roles give an exact global branch decoder

**Date:** 2026-08-15.  All logarithms are base two.  This continues
`LIVE_ROOT_TRANSVERSAL_ENTROPY_GATE.md` at its high-dispersion endpoint.

## Verdict

The first-divergence branch-tag problem has an exact solution at the level of
the coloured completion box.  No released trace, matching edge, or chronology
word has to be stored in the output.  The empty completion roles themselves
decode a monotone deletion forest.

Let the completion ground be partitioned into ordered physical role supports

\[
                         X_1,\ldots,X_s,
 \qquad d_i=|X_i|,qquad P_0=\prod_{i=1}^s d_i.        \tag{1}
\]

Every completion endpoint \(A_\omega\) is a transversal, with one label in
each role.  Let \(U_\omega\) be an ordinary released face on a disjoint
ground.  Suppose the ordered pair \((A_\omega,U_\omega)\) recovers record
weight with load at most \(\delta\), and let the total record mass be \(M\).
Then there is an explicit weighted family of ordinary mixed outputs with
total routed weight at least

\[
                              {M\over P_0},             \tag{2}
\]

and global output load at most \(\delta\).  Consequently

\[
 \boxed{\quad
                              M\le\delta V(P)P_0.
 \quad}                                                \tag{3}
\]

The routing preserves the released endpoint and has a literal completion
decoder.  In the fixed-\(x\) core, first set \(A=D-\{x\}\); after decoding
\(A\), reattach the one globally fixed \(x\) to recover \(D\).

The construction applies to all bad-circuit types, including singleton
released traces.  Thus the high-transversal branch does not fail for lack of
a branch tag.  What remains is capacity: (3) spends the complete role-box
volume \(P_0\).  In the anti-aligned product regression every completion role
must be deleted before the mixed union becomes convex, and (2) is attained
at the correct operation scale.  Therefore high released-trace diversity by
itself does not improve \(P_0\) to the selected completion-family size.

Writing \(M_D\) for the coloured completion family and

\[
                         R_D=\log(P_0/M_D),             \tag{4}
\]

the theorem turns a rectangular mass \(M\asymp M_DH\) into a mixed bank of
size at least \(H2^{-R_D}\).  In the low-redundancy live branch this is a
second live-normalized copy of the released bank, with only
\(2^{O(L\log L)}\) loss.  It is not a product multiplier.  In the
quadratic-redundancy branch it is weak, and the established four-local
physical-box alternative remains necessary.

This is an unconditional global decoder theorem, not an EIC' closure.  A
further argument must either exploit the fact that many terminal outputs
retain a nonempty completion suffix, or prove that the all-roles-deleted
mass exposes an ambient child/profile bank.  No fixed-power or coefficient-
half conclusion is claimed.

## 1. The role-monotone deletion forest

At a node of the forest, some fixed earlier completion labels have been
deleted from every record at that node.  For a bad record, consider **all**
bad four-circuits in its current mixed union.  Since the two endpoint traces
are individually faces, every such circuit crosses the two grounds.  Define

\[
 i(\omega)=\min\{i:\text{the label of }A_\omega\cap X_i
                       \text{ belongs to a bad circuit}\}.       \tag{5}
\]

For each role \(i\), partition its bad records by their actual label
\(z=A_\omega\cap X_i\).  Retain a heaviest label class and delete that fixed
\(z\) from all its completion endpoints.  This creates one child for every
nonempty role class.  If the bad mass assigned to role \(i\) is \(b_i\), the
child has mass at least

\[
                              {b_i\over d_i}.           \tag{6}
\]

All good records at the node terminate and are routed to their current mixed
union.

The role indices on every root-to-leaf path are strictly increasing.  Indeed,
deletion cannot create a new nonconvex four-subset.  If a later circuit used
a surviving completion role \(j<i\), the same circuit already existed before
role \(i\) was deleted, contradicting (5).  The deleted role itself is empty,
so it cannot recur.

After at most \(s\) deletions, strict role monotonicity leaves no possible bad
circuit, so every surviving record reaches an ordinary mixed output.  Some
earlier passed roles may remain; in the worst-case anti-aligned product every
completion role is deleted and the terminal output is just the released
endpoint.

## 2. Exact decoder and load

Let \(O\) be one terminal output.  The fixed ground partition gives

\[
                         U=O\cap\operatorname{ground}(U),
 \qquad A'=O\cap\bigcup_iX_i.                           \tag{7}
\]

Because the original completion occupied every role, the set

\[
                         J(O)=\{i:A'\cap X_i=\varnothing\}       \tag{8}
\]

is exactly the set of deleted roles.  Its increasing order is the unique
root-to-leaf role history.  Starting at the root, follow those role children;
the forest stores one fixed selected label \(z\in X_i\) at each child.
Reattaching these labels reconstructs \(A\), while \(U\) was never altered.

Thus a terminal output recovers its ordered endpoint pair.  All records with
that pair have total weight at most \(\delta\), proving the global load
claim.  Notice that this decoder sums all role branches before spending the
one global face budget.  It incurs neither an \(s!\) ordering loss nor an
\(|U|^s\) released-tag loss.

## 3. Weighted mass induction

For a node \(v\), let \(m(v)\) be its record mass and let \(T(v)\) be the
total terminal weight in its descendant forest.  Put

\[
                         P(v)=\prod_{i\text{ not yet passed}}d_i. \tag{9}
\]

We prove \(T(v)\ge m(v)/P(v)\) by reverse induction.  Good mass \(g\) stays
terminal.  If \(b_i\) is the bad mass assigned to role \(i\), (6) and the
induction hypothesis give descendant terminal mass at least

\[
 {b_i\over d_i\prod_{j>i}d_j}
                  \ge {b_i\over P(v)}.                \tag{10}
\]

The roles below \(i\) need not be deleted later; omitting their factors only
improves (10).  Also \(g\ge g/P(v)\).  Summing over the disjoint good class
and all role classes proves the induction.  At the root, \(P(v)=P_0\), which
is (2).  The load bound then proves (3).

## 4. Exact saturation and the live-normalization gap

Take two anti-aligned rational parabolic clouds.  Partition the first cloud
into \(s\) role cells of size \(d\), and let the completion family be all
\(d^s\) transversals.  Let every released endpoint have rank greater than
two.  A mixed subset is ordinary only if both nonempty cloud traces have
rank at most two.  With the lexicographically least eligible completion role
rule, the forest may have to delete every completion role; its terminal
output is then just \(U\).  The loss is exactly the completion word count

\[
                              P_0=d^s.                 \tag{11}
\]

The example is rational and stretchable and includes singleton released-side
circuit traces.  It is not a live bounded-rank counterfamily: the full convex
cloud Boolean banks dominate its rank-\(O(\log n)\) layers.  Replacing the
clouds by arbitrary low-face children while preserving the all-role deletion
property is precisely the unresolved ambient profile-composition problem.

The scalable arbitrary-child two-cloud construction in
`DENSE_HALL_TWO_CLOUD_PROFILE_BARRIER.md` shows why local signed circuits do
not prevent such anti-alignment.  It does not supply the missing bounded-rank
live ambient upper bound.  Hence (11) is a sharp operation-level regression,
not a claimed construction for Erdős 838.

There is, however, a genuine live-normalized barrier to the stronger claim
that high released-trace dispersion itself creates a direction cycle:
`HIGH_TRANSVERSAL_PASCAL_PREFIX_DAG_BARRIER.md`.  In a central Pascal seam,
both fixed-rank sides are within \(2^{O(L\log L)}\) of the ambient face
count, the released traces are polynomially many disjoint singletons at a
positive density of levels, and the chronology is an acyclic increasing
prefix trie whose leaves erase the whole tag.  Its exact verifier passes.
That example has coefficient strictly above one half, so it is an
applicability barrier rather than a minimizer obstruction.  Together with
(3), it shows that the next theorem must use a coefficient/minimizer input or
an additional physical storage role; neither high transversal dispersion nor
the completion role mask alone supplies a surplus over \(P_0\).

## Verification

Run

```text
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_role_monotone_mixed_face_forest.py
```

The verifier builds the entire branching forest with rational weights,
checks that deletion roles strictly increase, reconstructs every literal
endpoint pair from each terminal mixed face, verifies load \(\delta\) and
the mass lower bound \(M/P_0\), and realizes exact all-role deletion in an
anti-aligned rational role product.
