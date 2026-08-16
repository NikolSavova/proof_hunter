# Central root depth: bounded guards cannot release a homogeneous bad product

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

A fixed `1+3` root circuit can have linear deletion depth.  Consequently
no theorem saying that one bounded guard, one bounded downshadow, or one
bounded Hall tag releases a positive fraction of a root-bad homogeneous
product is true.

There is an exact scalable central-shell family with `t=2m+1` disjoint
role supports of size `A` and a root `z` such that:

* all `M=A^t` full transversals are ordinary convex faces;
* every transversal has the same prescribed consecutive signs and the
  same `1+3` root-circuit role pattern;
* deleting fewer than `m` role guards leaves `z` hidden; and
* rooted release first occurs after deleting `m=(1/2-o(1))t` roles.

The complete detached partial-transversal shield has exactly

\[
                         (A+1)^t=M(1+1/A)^t             \tag{1}
\]

faces.  For `A>>t` this is only `(1+o(1))M`, so the visible omission mask
does not encode an independent context alphabet.  The complete rooted
partial-transversal bank has size between

\[
                    tA^{m+1}\quad\hbox{and}\quad
                    t(A+1)^{m+1}.                       \tag{2}
\]

Thus its logarithm is

\[
          (m+1)\log A+O(t)=\left({1\over2}+o(1)\right)\log M.           \tag{3}
\]

For a `K`-element actual root alphabet in the common central disk, any
one-face decoder restricted to detached or one-root partial transversals
has congestion at least

\[
 \boxed{
 {KM\over (A+1)^t+Kt(A+1)^{m+1}}
  \ge {1\over2}\min\left\{
       K\left({A\over A+1}\right)^t,
       {A^t\over t(A+1)^{m+1}}
       \right\}.}                                      \tag{4}
\]


For `A>>t`, the right side is
`(1-o(1))min{K,A^m/t}/2`.  The two elementary decoders—forget the root, or retain it and keep one
semicircle block—match the two regimes in (4) up to `2^{O(t)}`.  This is
the exact product/context overlap for all bounded-guard and downshadow-tag
decoders in the model.

There is nevertheless a recoverable outer shield: the `M` full detached
transversals themselves form a load-one ordinary bank.  If

\[
                         A=2^L,\qquad t=(\alpha+o(1))L,  \tag{5}
\]


then the outer bank has coefficient `alpha`, while the first rooted
release has coefficient `alpha/2`.  In particular the most dangerous
choice `alpha=1/2` already contains an absolute coefficient-half face bank.
The construction therefore kills the proposed bounded-release theorem but
does not give a sub-half planar construction.

Arbitrary projective order types may be shrunk into the role clusters.
They do not affect the singleton-transversal depth argument, and any extra
child faces only enlarge the ambient bank.  Hence projective universality
does not repair bounded guard release, but it also does not suppress the
outer/circuit shield which pays at coefficient `alpha`.

For genuinely quadratic families of **multi-point** external contexts,
the load-one object remains the separated pair `(context face, detached
outer face)`.  Equation (4) does not turn that pair into one mixed face.
Analyzing all mixed inner/outer faces is a new wrapper recurrence; the
central-shell construction alone supplies neither a one-face theorem nor a
sub-half counterexample.

## 1. The central-shell construction

Let `t=2m+1`.  Start with the vertices

\[
 c_j=(\cos(2\pi j/t),\sin(2\pi j/t)),\qquad 0\le j<t,  \tag{6}
\]


and the root `z=0`.  Replace each `c_j` by an `A`-point cluster `X_j` in a
sufficiently small neighbourhood.  All strict statements below are open,
so the clusters may be rational, in general position, and may realize
arbitrary prescribed rational order types after an affine shrinking.

There are two elementary facts about the regular odd polygon.

1. A set of its vertices is contained in an open semicircle if and only if
   it is contained in some block of `m+1` consecutive roles.
2. The origin is outside their convex hull exactly in that case.  If the
   active roles are not contained in such a block, the origin is in the
   interior of their convex hull.

The margin is uniform for the finitely many role masks, so both facts
remain strict after sufficiently small cluster perturbations.  Therefore,
for every partial transversal `F_S` with active role mask `S`,

\[
 \boxed{
 \{z\}\cup F_S\text{ is convex}
 \quad\Longleftrightarrow\quad
 S\text{ is contained in an }(m+1)\text{-role cyclic block}.}          \tag{7}
\]


Every detached partial transversal is convex, because it is a subset of a
convex macrotransversal.  Every full transversal surrounds `z` and is
root-bad.

Choose three well-spaced roles whose macro triangle contains a small disk
around `z`.  After shrinking, every choice of labels in those roles still
contains `z` in its triangle.  Thus every word has the same strict `1+3`
circuit role pattern.  If an actual fixed boundary jet and actual fixed
circuit anchors are required, make the four jet roles and these three
roles singleton supports.  The remaining `t-O(1)` supports still give

\[
                         A^{t-O(1)}                     \tag{8}
\]


words and deletion depth `t/2-O(1)`, so every quadratic exponent is
unchanged.

## 2. Exact guard depth

If fewer than `m` roles are deleted from a full word, at least `m+2`
roles remain.  No `m+2` roles fit inside an `(m+1)`-role block, so (7)
says that `z` remains hidden.  This proves the lower bound

\[
                         g_{root}\ge m.                 \tag{9}
\]


Conversely, delete the complementary `m` roles and retain one block of
`m+1` consecutive roles.  Equation (7) makes the root plus every such
partial transversal convex.  Hence

\[
                         \boxed{g_{root}=m.}             \tag{10}
\]


The fixed four-circuit does not reveal this depth.  Deleting one of its
three outer roles destroys that selected witness, but another circuit
still hides the root until half of the macro roles have been removed.
Thus repeated four-circuit elimination can have linear depth even when the
initial circuit role is fixed exactly.

## 3. Downshadow and Hall-tag capacity

A detached partial transversal chooses either no point or one of `A`
points independently in every role.  Hence the complete detached bank has
the exact size (1).  Restricting to at most `g` deleted roles gives

\[
                 B_g=\sum_{d=0}^g{t\choose d}A^{t-d}.   \tag{11}
\]


In particular

\[
 {B_g\over M}\le { (A+1)^t\over A^t}
                  =(1+1/A)^t\le e^{t/A}.               \tag{12}
\]


Suppose there are `K` distinct external contexts and `KM` selected
records.  Any context-free downshadow map has an output in this bank, so
its maximum fibre is at least

\[
                         {KM\over B_g}\ge K e^{-t/A}.    \tag{13}
\]


The omission mask is already visible in the output; (13) proves that even
using it optimally as a Hall tag recovers only `e^{t/A}` context values.
For `A=2^{Theta(t)}` this factor is `1+o(1)`.

Now permit the output to contain one actual root mark.  By (7), its active
outer mask must lie inside some `(m+1)`-role block.  A union bound over the
`t` blocks gives at most

\[
                         t(A+1)^{m+1}                   \tag{14}
\]


rooted partial transversals per root.  Keeping all roles in one block gives
`tA^{m+1}` distinct outputs, proving (2).  Any map from the `M` full words
at one root to rooted partial transversals therefore has load at least

\[
                         {A^t\over t(A+1)^{m+1}}
                    = A^{m-o(m)}2^{-O(t)}.              \tag{15}
\]


Allowing either detached outputs or rooted outputs for `K` roots gives at
most the denominator in (4), and pigeonhole proves (4).

The lower bound is sharp at leading exponent.  Ignoring the context and
outputting the full detached word has load `K`.  Alternatively, retain one
fixed `(m+1)`-role block together with the root; the discarded `m` labels
give load exactly `A^m` at each root.  Choose the better operation.

## 4. The coefficient audit

With the scaling (5), the actual ambient point count of the outer shell is

\[
                         n=tA,\qquad \log n=L+o(L).      \tag{16}
\]


The detached shield (1) satisfies

\[
                 \log (A+1)^t=(\alpha+o(1))L^2,        \tag{17}
\]


while (2) gives

\[
                 \log B_{root}=(\alpha/2+o(1))L^2.    \tag{18}
\]


Thus the root-bad product itself is not invisible: its detached ordinary
faces have exactly the complete product coefficient.  At `alpha=1/2` this
is already the coefficient-half upper/lower scale.  The bounded-release
failure can only obstruct a **relative multiplication by external
contexts**; it cannot reduce the absolute face coefficient contributed by
the outer roles.

For `K<=n` singleton roots, `log K=O(L)` is subquadratic, and (13) loses no
leading coefficient.  To create quadratic actual context entropy one must
use multi-point inner context faces.  The separated pair bank then has
size `K M`, but a one-face mixed bank depends on the inner face's exposed
profile and is not covered by (7).  Treating `K` formal histories as
distinct contexts would be invalid.

## 5. Stress against projective children

At each macro role, replace the `A` points by a sufficiently small affine
copy of any rational order type `Q_j`.  The role clusters can therefore be
coefficient-half upper constructions, alternating/Pascal children, or
projectively universal reset sets.  All one-point-per-role statements,
the depth (10), and the counts (1)--(4) are unchanged.

This is a sharp counterexample to bounded guard release even with the most
adversarial children.  It is not an upper bound on the **entire** ambient
face complex: local child faces and their one-gap profiles can add banks.
In particular, the construction cannot be cited as a sub-half recursive
wrapper.  What it proves is the exact missing condition for a positive
release theorem: some bound on root halfspace depth, or an ambient profile
bank which pays when that depth is linear.

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_central_root_depth_guard_barrier.py
```

The verifier audits an exact rational `t=9,m=4,A=2` instance in general
position.  It checks all 512 full transversals, every six-role downshadow,
all nine five-consecutive-role releases, the fixed `1+3` circuit roles,
all `3^9=19683` partial transversals, and the exact rooted rank vector
`(18,144,432,576,288)`.
