# A stationary released-side circuit root is globally paid

**Date:** 2026-08-15.  All logarithms are base two.  This is the rooted-star
continuation of `LIVE_CROSS_CIRCUIT_CHRONOLOGY.md`.

## Verdict

The stationary rooted-star endpoint is impossible in the live dense
completion--release core.  The correct invariant is the adaptive **weighted
root dispersion** of the released-side traces of the bad four-circuits.

Let \(P\) have \(V=V(P)\) ordinary faces.  Let \(\mathcal R\) be a weighted
family of records with ordinary endpoints

\[
                         (A_\omega,U_\omega),          \tag{1}
\]

on disjoint fixed role grounds.  The ordered pair recovers the literal
record with pair load at most \(\delta\).  Assume \(|U_\omega|\le R\).
Starting with mass \(M_0=M\), perform the following canonical descent.

At stage \(j\), records whose reduced union is an ordinary face have total
weight at most \(\delta V\).  On every other record choose one canonical bad
four-circuit.  Let \(\mathcal H_j\) be the hypergraph consisting of the
nonempty released-side traces of these circuits.  If their total bad weight
is \(B_j\), define

\[
 \lambda_j(y)=\sum_{\substack{\omega\text{ bad}\cr
                    y\in\operatorname{tr}_U(\mathsf C_\omega)}}w_\omega,
 \qquad
 h_j={B_j\over\max_y\lambda_j(y)}.                    \tag{2}
\]

Retain all records counted by a maximizing \(y\), and delete that one fixed
released-side label from every retained \(U\).  Then the process stops after
some \(t\le R\), and

\[
 \boxed{\quad
   \log {M\over2\delta V}
       \le\sum_{j=0}^{t-1}\bigl(1+\log h_j\bigr).
 \quad}                                                \tag{3}
\]

All deletions are on the released side.  Thus a good mixed output retains
the full completion endpoint \(A\); the fixed deleted labels reconstruct
\(U\).  In the fixed-\(x\) application, reattaching the one globally fixed
\(x\) reconstructs the literal completion \(D\).  No completion coordinate
or source metadata is erased.

There is a sharper stationary-root corollary.  Suppose one fixed set
\(T\) of \(h\) physical released-side labels has the hereditary property

> after deleting any previously selected labels of \(T\), every remaining
> bad cross-circuit meets the undeleted part of \(T\) on its released side.

Then

\[
 \boxed{\quad
                         M\le2\delta V\,2^h h!.
 \quad}                                                \tag{4}
\]

In particular a stationary triangle root costs only a constant factor
\(2^3 3!=48\), in addition to the harmless leading factor two.  It cannot
carry mass \(V^2/2^{O(L\log L)}\).

On the live slice, suppose

\[
 M\ge {V^2\over K},\qquad
 K\delta=2^{O(L\log L)},\qquad
 \log V\ge cL^2-o(L^2),\qquad R\le CL.                \tag{5}
\]

Then (3) forces

\[
 {1\over t}\sum_{j<t}\log h_j
              \ge {c\over C}L-O(\log L),             \tag{6}
\]

after padding by zero-cost terminal levels if necessary.  Since
\(h_j\le n\), a positive fraction of the stages have

\[
                         h_j\ge n^{\varepsilon}       \tag{7}
\]

for some \(\varepsilon=\varepsilon(c,C)>0\).  Moreover every edge of
\(\mathcal H_j\) has size at most three, so a weighted maximal-matching
argument gives

\[
                         \nu(\mathcal H_j)\ge h_j/3.   \tag{8}
\]

Thus the only live survivor has, at a positive density of chronology levels,
a polynomial family of pairwise disjoint released-side circuit traces and no
single physical released root carrying more than an \(n^{-\varepsilon}\)
fraction of the bad weight.  This is a weighted rooted-star versus
first-divergence dichotomy.  Unlike an unweighted transversal number,
\(h_j\) cannot be inflated by negligible outlier records.

Equations (3)--(8) do not yet create the required detached/cyclic profile
bank.  The disjoint traces live on different records, and deleting a varying
singleton trace can erase the branch name.  A final theorem must route these
polynomially many trace branches while retaining a tag, or show that the
singleton-heavy part localizes to another canonical pocket.  The present
report closes the stationary common-cage branch but makes no fixed-power or
coefficient-half claim for the high-transversal branch.

## 1. Proof of the adaptive inequality

At stage \(j\), let the retained mass be \(M_j\).  The previously deleted
released labels are fixed globally on this branch.  If a reduced union
\(A_\omega\cup U^{(j)}_\omega\) is a face, it recovers the reduced ordered
pair by the fixed role partition.  Reattaching the deleted released labels
recovers \(U_\omega\), while \(A_\omega\) was never changed.  Hence

\[
              \sum_{\omega\text{ good at }j}w_\omega
                                           \le\delta V. \tag{9}
\]

If \(M_j\le2\delta V\), stop.  Otherwise the bad records have mass
\(B_j\ge M_j/2\).  Their canonical bad circuits cross the two endpoint
faces, so their released traces are nonempty.  By (2), one physical released
label is contained in traces of total record weight

\[
                         {B_j\over h_j}ge {M_j\over2h_j}. \tag{10}
\]

Retain this class and delete the fixed assigned label from every released
endpoint.  Deletion is injective because every retained endpoint contains
the label; heredity preserves convexity.  Thus

\[
                         M_{j+1}\ge {M_j\over2h_j}.    \tag{11}
\]

The deleted labels are distinct.  After at most \(R\) deletions the released
endpoint is empty, so every remaining union is the completion face and is
good.  Combining the stopping inequality with (11) proves (3).

## 2. Fixed-root payment

Under the hereditary fixed-root hypothesis, let \(T_j\) be the undeleted
part of \(T\).  Every bad trace meets \(T_j\), so

\[
 B_j\le\sum_{y\in T_j}\lambda_j(y),
 \qquad h_j\le|T_j|.                                  \tag{12}
\]

The successive upper bounds on the dispersions are therefore

\[
                         h,h-1,\ldots,1.               \tag{12a}
\]

Once all \(h\) labels are deleted, no bad circuit remains.  Iterating (11)
and then applying (9), or stopping earlier at \(2\delta V\), gives

\[
                         M\le2\delta V\prod_{k=1}^h2k
                           =2\delta V\,2^h h!,         \tag{13}
\]

which is (4).  This is an actual one-face mixed bank: the decoder knows the
fixed root labels deleted along the retained branch.  It does not spend a
separate copy of \(V\) for each root or source.

## 3. Live entropy and disjoint traces

Take logarithms in (3) and insert (5):

\[
 \sum_{j<t}(1+\log h_j)
       \ge \log V-O(L\log L)
       \ge cL^2-O(L\log L).                           \tag{14}
\]

There are at most \(CL\) summands and each \(1\le h_j\le n\).  This proves
(6); the elementary bounded-average argument gives (7) on a positive
fraction of stages.

For (8), take a maximal matching in \(\mathcal H_j\), and let \(G\) be the
union of its edges.  The set \(G\) meets every trace, because a trace
disjoint from it could be added to the matching.  Every bad record is
therefore counted in \(\lambda_j(y)\) for at least one \(y\in G\).  Since
\(|G|\le3\nu(\mathcal H_j)\),

\[
 B_j\le\sum_{y\in G}\lambda_j(y)
     \le3\nu(\mathcal H_j){B_j\over h_j}.             \tag{15}
\]

This proves (8) and establishes polynomial actual-trace diversity with
weighted root spread, not merely entropy in metadata or role names.

## 4. Sharpness and the surviving decoder issue

In the anti-aligned two-cloud regression, choose canonical \(3+1\) bad
circuits.  If the released endpoint is one fixed three-label root, that root
is a hereditary transversal until it is exhausted; the mixed union then
equals the untouched completion face.  This is the stationary-root case of
(4).  Merely requiring a common three-label prefix is not enough: after the
prefix is deleted, variable released labels can support new circuits.  That
distinction is why the hereditary qualifier in (4) is necessary.

If instead the released rank layer ranges over all subsets, the canonical
released traces have large weighted dispersion as well as large transversal
number.  The traces can be chosen pairwise disjoint, but they belong to
different released endpoints.  A one-point trace provides no retained tag
after it is deleted, so summing all branches can have large decoder load.
This exact regression explains why (8) is a gate rather than the final
profile bank.  It is non-live because of the full Boolean cloud reservoirs.

## Verification

Run

```text
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_live_root_transversal_entropy_gate.py
```

The verifier computes the exact weighted root dispersions of the canonical
released-side circuit hypergraphs, checks (9)--(11) with rational weights,
verifies the weighted rank-three maximal-matching bound, and realizes both a
fixed-root and a spread-root descent in the exact rational anti-aligned
configuration.
