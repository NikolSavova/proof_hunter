# Ferrers rectangles do not yet trigger the upper-jump theorem

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

Quadratic profile entropy plus a large Ferrers carrier rectangle does not,
by itself, satisfy the hypotheses of the upper-jump coefficient theorem.
There are two exact mismatches.

First, the planar three-arc rectangle is an **additive three-cluster
wrapper**.  If its three clusters have comparable cardinality `Theta(N)`,
then the macro has only three positions.  In the notation of
`agent_upper_jump/REPORT.md`,

\[
 \ell=\log3=O(1),\qquad t=\log N+O(1),\qquad L=\ell+t,    \tag{1}
\]

so the fixed-point gain

\[
                         (1-2c){\ell t\over L^2}           \tag{2}
\]

is `o(1)`, even for `c<1/2`.  Macroscopic cluster cardinality is not a
macroscopic **multiplicative log-size split**.

Second, the `2^{Theta(L^2)}` objects in the live residue are overlapping
profile faces, not disjoint macro positions.  A quadratic-entropy family
can live on one common label set and reuse one common Ferrers rectangle.
Profile thinning by `2^{o(L^2)}` does not turn those faces into
`N^{alpha}` disjoint child blocks.  Treating profiles as macro positions
would double-count their shared labels and invalidates the composition
recurrence.

There is also an exact skew regression.  Ferrers signs only inspect one
endpoint from each side.  Tiny projective substitution lets every endpoint
position carry an arbitrary child order type; reflecting a child swaps its
cap and cup counts while preserving its size and total face count.  Hence
the children can be ordered with quadratic forward anti-alignment without
changing any carrier--root incidence.  Ferrers data alone gives no bound on
the skew losses `Delta_I` or `D_I` required by the heterogeneous upper-jump
theorem.

Therefore the detached **convex** three-arc shield does close the
coefficient route directly, but arbitrary low-face order types embedded in
the endpoint pockets do not fall under equation `(32a)` without an
additional structural theorem.  That theorem must extract, after only
`2^{o(L^2)}` profile loss,

1. `N^{alpha+o(1)}` genuinely disjoint macro blocks of size
   `N^{beta+o(1)}`, with `alpha,beta>0`;
2. a scale-covering induced macro core;
3. high mean rank and subquadratic common-skew loss on that core.

No such extraction follows from the current Ferrers or entropy statements.
This is an applicability barrier, not a counterexample to the coefficient
`1/2` lower bound.

## 1. Additive clusters versus multiplicative substitution

The upper-jump recurrence concerns a macro `S` of `r` positions, each
replaced by a child of size about `n`.  Its total size is `rn`, so

\[
                         \log(rn)=\log r+\log n.           \tag{3}
\]

A genuine coefficient jump needs

\[
 {\log r\over\log(rn)}\longrightarrow\alpha>0,qquad
 {\log n\over\log(rn)}\longrightarrow\beta>0.            \tag{4}
\]

By contrast, a separated carrier/root realization partitions its labels
into `L,R,Z` (and possibly an interior pocket), with

\[
                         |L|+|R|+|Z|=N.                   \tag{5}
\]

Viewing these as three child blocks gives macro size `r=3`, not
`r=Theta(N)`.  If every child has size `Theta(N)`, then (1) holds and the
right side of the fixed-point identity is only

\[
 c+(1-2c){\log3\over L}+O(L^{-2}).                        \tag{6}
\]

Thus the strict finite-`L` increase vanishes after normalization by `L^2`.
This arithmetic issue cannot be repaired by discarding profiles: profiles
do not add points to the macro.

## 2. Exact quadratic-entropy overlap regression

Let the ambient label count be `N=2^L` and take

\[
                         q=\lfloor\theta L\rfloor.         \tag{7}
\]

The family of all `q`-subsets has

\[
 \log{N\choose q}=\theta L^2-O(L\log L).                 \tag{8}
\]

It has the exact entropy scale of the heavy profile residue, but all its
members live on the same `N` labels.  The subfamily containing a fixed
`q/2`-set still has

\[
 \log{N-q/2\choose q/2}={\theta\over2}L^2-O(L\log L),    \tag{9}
\]

while every pair of profiles shares that fixed core.  Removing a factor
`2^{o(L^2)}` preserves the leading coefficients in (8)--(9).  Neither
entropy statement supplies even two disjoint supports, much less the
partition into `N^alpha` comparable blocks required by (4).

Even without the common core, a pairwise disjoint subfamily of the full
`q`-uniform family has size at most

\[
                         \left\lfloor{N\over q}\right\rfloor,
 \qquad \log\left\lfloor{N\over q}\right\rfloor=O(L).     \tag{9a}
\]

Thus extracting genuinely disjoint profiles destroys a quadratic amount
of profile entropy; it is not a `2^{o(L^2)}` thinning.

This is a set-system regression only.  In the live planar problem the
profiles are ordinary faces and hence carry additional circuit structure;
extracting a multiplicative block system from that structure is precisely
the missing theorem.

## 3. Ferrers incidence is invariant under child skew

Fix a three-arc carrier--root macro satisfying all strict transversal
triangle conditions.  Replace any macro endpoint `p` by a sufficiently
small generic similarity copy of an arbitrary child `Q_p`.  Openness of
the strict orientation inequalities preserves every transversal Ferrers
incidence.  It imposes no condition on triples contained in one child.

For a vertically presented child write `(C_p,U_p,W_p)` for its cap, cup,
and total nonempty face counts.  Reflection in a horizontal line replaces

\[
                         (C_p,U_p,W_p)\quad\hbox{by}\quad
                         (U_p,C_p,W_p).                    \tag{10}
\]

Take an abstract extremal profile with

\[
                         (C,U,W)=(1,W,W)                  \tag{11}
\]

and its reflection `(W,1,W)`.  Put all copies of the first orientation
before all copies of the second.  Every forward endpoint product across
the cut is

\[
                         C_iU_j=1,                         \tag{12}
\]

although both children have total count `W`.  In the notation of the
upper-jump report, if `log W=c t^2`, the common-skew loss is at least

\[
                         \Delta_I\ge {c\over2}t^2,         \tag{13}
\]

which is quadratic and violates the required `o(L^2)` hypothesis.

Equation (11) is the exact counting extremum illustrating the inference
failure; it is not asserted to be a new planar low-count order type.  What
is planar and exact is the independence: projective substitution and
reflection preserve the carrier--root signs.  Consequently Ferrers
incidence cannot, without another geometric/history condition, control the
child skew used by `(32a)`.

## 4. Sharp coefficient-scale residual

Combining the external-alphabet trichotomy, the carrier square gate, and
this audit leaves two honest coefficient branches.

* If a common endpoint/root union is convex, its Boolean detached shield
  is already far stronger than a coefficient-scale gain.
* Otherwise the rectangle localizes to endpoint/root child order types.
  One must either multiply their unrestricted face reservoirs or prove
  that the live canonical history forces a positive-log-scale block core
  with high mean and controlled skew.

Quadratic profile entropy is necessary for the hard branch, but it is not a
substitute for that block-core theorem.  In particular equation `(32a)`
must not be applied with profile count in place of macro point count.

## 5. Verification artifact

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_ferrers_upper_jump_applicability.py
```

The verifier checks the vanishing fixed-three wrapper gain, the quadratic
subset/profile entropy (including a common-core family), stability under
`2^{o(L^2)}` thinning, and the exact reflected anti-alignment calculation.
