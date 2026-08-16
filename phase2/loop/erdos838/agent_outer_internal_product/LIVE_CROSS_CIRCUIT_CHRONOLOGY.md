# Live completion--release rectangles force a cross-circuit chronology

**Date:** 2026-08-15.  All logarithms are base two.  This report continues
`LIVE_DENSE_COMPLETION_PROFILE_GATE.md`.

## Verdict

There are two exact weighted two-family theorems at the live
completion--release interface.  The stronger quantitative theorem replaces
the featureless incompatible rectangle by a long chronology of fixed
physical completion labels, each certified record-by-record by a possibly
varying cross-circuit.  A shorter refinement fixes the entire actual
four-circuit at every step.  This distinction is essential: the first
theorem reaches the excess-rank threshold, while only the second carries a
common signed circuit profile.

Let \(P\) be an \(n\)-point planar configuration in general position and let
\(V=V(P)\) be its number of ordinary convex faces.  Let \(\mathcal R\) be a
weighted family of records with two ordinary face targets

\[
                         (A_\omega,U_\omega),          \tag{1}
\]

on disjoint, fixed role grounds.  Assume that the ordered pair in (1)
recovers the literal record up to weight at most \(\delta\).  Thus every
fixed pair has total record weight at most \(\delta\).  Put

\[
             M=\sum_{\omega\in\mathcal R}w_\omega,
 \qquad C_4=\binom n4,\quad \Lambda_1=2n,
 \quad \Lambda_4=2C_4.                                \tag{2}
\]

For every integer \(q\ge1\) satisfying

\[
                         {M\over\Lambda_1^{q-1}}>2\delta V, \tag{3}
\]

there is a nested positive-weight subfamily and a sequence of distinct
physical completion labels

\[
                         z_1,\ldots,z_q.               \tag{4}
\]

with the following properties.

* Every retained record before step \(j\) has a canonical actual cross-
  circuit containing \(z_j\).  The other three labels of this witness are
  allowed to vary with the record.
* The \(z_j\) are pairwise distinct and all lie on the completion side.
  Delete \(z_j\) from that endpoint on every retained record.  Both reduced
  endpoints remain ordinary faces.
* The retained weight after step \(j\) is at least

  \[
                              M/\Lambda_1^j.           \tag{5}
  \]

* At every step the reduced ordered pair still recovers the original
  ordered pair: reattach the fixed, side-coloured labels
  \(z_1,\ldots,z_j\).  Consequently literal completion data are never
  discarded.

The alternative hidden in the proof is an ordinary mixed-face bank.  If a
reduced union becomes convex, its two factors are recovered by intersecting
with the fixed role grounds and the original pair is then recovered by
reattaching the chronology.  Hence all good records at any stage have total
weight at most \(\delta V\).  Condition (3) says that this bank is too small,
so a common completion-side witness label can be selected and peeling
continues.

There is also a fixed-circuit refinement.  Replace \(\Lambda_1\) by
\(\Lambda_4\) in (3)--(5).  Then one may retain actual circuits
\(\mathsf C_1,\ldots,\mathsf C_q\) such that every record at level \(j\)
has the same \(\mathsf C_j\), with \(z_j\in\mathsf C_j\) chosen on the
completion side.  The variable-witness theorem must not be quoted as if it
gave these fixed triples for free.

For the fixed-label completion core, set

\[
                         A_\omega=D_\omega-\{x\}.      \tag{6}
\]

The label \(x\) is fixed before the theorem is applied.  A good mixed output
recovers \(A_\omega,U_\omega\); reattaching \(x\) and the side-coloured
chronology recovers the **literal full completion** \(D_\omega\).  Thus (6)
does not make the invalid replacement of \(D\) by \(B\cup\{x\}\).

On the live slice the fixed-\(x\) record mass has the form

\[
                         M\ge {V^2\over K},
 \qquad K=2^{O(L\log L)},\qquad L=\log n,              \tag{7}
\]

after absorbing the rank bucket, source normalization and pair cap into
\(K\).  If

\[
                         \log V\ge cL^2-o(L^2),        \tag{8}
\]

then (3) holds for every

\[
                         q\le (c-o(1))L.               \tag{9}
\]

Indeed \(\log\Lambda_1\le L+1\).  The fixed-circuit refinement separately
gives \(q\le(c/4-o(1))L\), since \(\log\Lambda_4\le4L+1\).  In particular a
surviving dense rectangle contains a common chronology of \(\Theta(L)\)
completion labels, each with an actual cross-circuit witness.  It also
contains a shorter common chronology of fixed actual four-circuits.

This is the strongest unconditional conclusion obtained here.  A chronology
is not yet a composition bank.  The fixed labels cost \(n^q\), while
retaining all their witness triples costs up to \(n^{4q}\).  Anti-aligned
convex clouds realize precisely this gap locally: repeated variable \(1+3\)
witnesses can force the chosen cloud to be peeled all the way to empty (or to
rank two only when the opposite trace also has rank at most two).
Their detached Boolean reservoirs make them non-live, but the example proves
that the label chronology alone cannot be declared a cap/cup product.  The
remaining theorem must use simultaneous live normalization to charge either
witness-triple spread or a long rooted chronology to a detached or
strong-glue profile bank.
No fixed-power or coefficient-half closure is claimed.

## 1. The weighted circuit-peeling theorem

At an intermediate stage let \(\mathcal R'\) have total weight \(M'\), and
let \(A'_\omega,U'_\omega\) be the endpoints after deleting the already
fixed side-coloured chronology.

Call a record *good* when

\[
                         A'_\omega\cup U'_\omega       \tag{10}
\]

is an ordinary face.  Since the grounds are disjoint, (10) recovers the
reduced ordered pair.  The fixed chronology then recovers the original pair.
Every output therefore has load at most \(\delta\), and

\[
                \sum_{\omega\text{ good}}w_\omega
                                      \le\delta V.     \tag{11}
\]

If \(M'>2\delta V\), the bad records have weight at least \(M'/2\).
Both endpoints of a bad record are faces.  Planar Caratheodory therefore
supplies a nonconvex four-subset of their union, and that four-subset meets
both endpoints.  Choose the lexicographically first such circuit, then the
lexicographically first vertex of that circuit on the completion side.
There are at most \(n\) possible physical labels, so one fixed label \(z\)
occurs on records of total weight at least

\[
                         {M'\over2n}={M'\over\Lambda_1}. \tag{12}
\]

Delete \(z\) from the completion endpoint.  Every retained completion
contains \(z\), so deletion is injective.  Heredity preserves ordinary
convexity.  Previously deleted labels are absent from the current endpoints,
hence \(z\) is new.  This proves one variable-witness step.  Iterating
(11)--(12) under (3) proves (4)--(5).

If instead one pigeonholes the entire canonical circuit, there are at most
\(C_4\) choices and the retained weight is at least \(M'/(2C_4)\).  Choosing
its completion-side vertex proves the fixed-circuit refinement.

The proof uses neither regularity nor an unproved tangent-profile
classification.  It uses exactly three geometric facts: four-locality of
planar convexity, heredity of faces, and disjoint fixed role grounds.

## 2. A rank corollary and its limitation

Suppose every completion endpoint has rank at most \(R\).  The
variable-witness chronology always deletes on that side, so it cannot contain
more than \(R\) labels.  Applying the theorem with \(q=R+1\) gives the exact
bound

\[
             \boxed{\quad M\le2\delta V\,(2n)^R.\quad}           \tag{13}
\]

For bounded rank this is a genuine mixed-face theorem.  Combined with
(7)--(8), it forces

\[
                         R\ge(c-o(1))L.                \tag{13a}
\]

This recovers, with an exact literal decoder, the current excess-rank
threshold.  The live residual assumes more strongly
\(R-c\log N=\Omega(L)\), so (13) does not close that final window.

The estimate also identifies the exact price of insisting on a literal
decoder.  Pigeonholing only the circuit *role type* would cost
\(\operatorname{poly}(L)\) per step, but the deleted physical label would
then vary with the record and could not be reattached from a one-face mixed
output.  Pigeonholing one actual completion label costs \(n\) and makes the
decoder exact; retaining the full actual circuit costs \(\binom n4\).

## 3. Relation to the live Hall normalization

In the notation of `EXCESS_RANK_FIXED_LABEL_DOWNSHADOW_GATE.md`, the rank
bucket has mass \(M_s\ge WH/\Gamma\), and one physical completion label
\(x\) occurs in weight at least \(sM_s/N\).  Therefore the theorem applies
to a fixed-\(x\) family of mass

\[
               M_x\ge {sWH\over N\Gamma}.             \tag{14}
\]

If \(W\ge V/\Xi\), \(H\ge V/\Theta\), and the coalesced pair cap is
\(\delta\), then

\[
 {M_x\over\delta V}
       \ge {sV\over N\Gamma\Xi\Theta\delta}.          \tag{15}
\]

All non-quadratic losses in the current rank-safe slice are
\(2^{O(L\log L)}\).  Substituting (15) into (3) yields

\[
 q< {\log V-O(L\log L)\over\log(2n)}.                 \tag{16}
\]

Equation (16), rather than the separate lower bounds on the two Hall vertex
sets, is the quantitative two-family content.  It preserves record weights,
the fixed released face, the fixed \(x\), and the full completion decoder.

## 4. Exact regression and open interface

Take two sufficiently small anti-aligned rational parabolic clouds.  Every
subset inside one cloud is a face, while a mixed subset is a face exactly
when each cloud contributes at most two points.  Let the left endpoint be a
fixed-\(x\) rank-\(s\) face with \(x\) deleted before mixing, and let the
right endpoint have rank \(s\).  The incompatible rectangle is complete.

Canonical circuit peeling repeatedly selects a completion-side label with a
signed \(3+1\) witness and deletes that common label.  The process
stops when the chosen side is empty; if the opposite trace has rank at most
two it can stop when the chosen side reaches rank two.  At that point every
remaining union is convex and the mixed bank is injective.  Thus the
dichotomy and its literal decoder are sharp even for rational stretchable
configurations.

This regression is not live: the full clouds contribute \(2^p\) ordinary
faces, whereas their rank-\(O(\log p)\) layers have only
\(2^{O((\log p)^2)}\) members.  It nevertheless kills the stronger claim
that a long cross-circuit chronology automatically contains a large facing
profile.  A closure now needs one additional statement:

> in a simultaneously live pair of rank-\(O(L)\) face families, a
> length-\(\Omega(L)\) actual cross-circuit chronology either has a
> globally chargeable rooted star, or its first-divergence circuits generate
> a detached/cyclic profile bank with subquadratic output load.

That statement is not proved here.  The theorem above makes its hypotheses
canonical and weighted.

## Verification

Run

```text
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_live_cross_circuit_chronology.py
```

The verifier checks the exact weighted good-output load inequality, both the
\(2n\) variable-witness and \(2\binom n4\) fixed-circuit recurrences,
injective reconstruction after fixed-label deletion, and a rational
anti-aligned fixed-\(x\) rectangle in which the chosen-side chronology ends
at the exact empty/rank-two threshold.
