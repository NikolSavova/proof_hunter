# Visible-chain flips and the half-weight target

**Date:** 2026-08-13
**Verdict:** the direct half-weight target

\[
 H(P):=\frac{nZ_P(1/2)}{Z_P(1)}\le 2                 \tag{HW}
\]

survives every exact test, but the natural local visible-chain charges do
not prove it.  There are three rigorous negative results: the stronger
half-activity mean bound is false on exact rational configurations; the
canonical post-flip map has exponentially large weighted fibres; and even a
fractional source/target charge with all cover slack available fails on the
saved twenty-point record.  A proof of (HW) must therefore be nonlocal or use
global-minimizer status essentially.

The empty face is included throughout.

## 1. Exact flip transport

Let `A` be a convex-position subset and let `p` lie strictly outside
`conv(A)`.  The two tangents from `p` cut out a unique (possibly empty) open
boundary chain `C=C(A,p)` of vertices hidden when `p` is inserted.  Therefore

\[
 \Phi(A,p)=\operatorname{ext}(A\cup\{p\})
           =(A\setminus C)\cup\{p\}                 \tag{1}
\]

is another convex-position subset.  The point is addable exactly when
`C` is empty and is a blocked exterior point otherwise.

For fixed `(B,p)` with `p in B`, the inverse fibre consists of sets

\[
 A=(B\setminus\{p\})\cup C,
 \qquad \operatorname{ext}(A\cup\{p\})=B.           \tag{2}
\]

The admissible hidden sets `C` form a down-set: if `C` is admissible, every
subset `D subset C` is also admissible.  Consequently the exact exterior-pair
mass transport at activity `z` has local fibre polynomial

\[
 z^{|B|-1}\sum_{C\in\mathcal D_{B,p}}z^{|C|}.        \tag{3}
\]

This is the correct visible-chain identity.  It also exposes why forgetting
the chain is too lossy.

## 2. Exponential rational fibre obstruction

For `m>=1`, put `L=m+1` and take

\[
 q_i=(i,i(L-i))\quad(0\le i\le L),\qquad
 p=(-1,(L+1)^2).                                     \tag{4}
\]

These integral points are in general position.  The `q_i` form a strict
convex chain.  Every internal `q_i` lies inside the triangle
`p q_0 q_L`.  More strongly, for every `i<j<k`, `q_j` lies inside
`p q_i q_k`; hence a set containing `p` and chain points is convex-position
exactly when it uses at most two chain points.

For every nonempty subset `C` of the `m` internal points,

\[
 A_C=\{q_0,q_L\}\cup C
\]

is convex and insertion of `p` hides exactly `C`, with the common target
`B={p,q_0,q_L}`.  Thus this single inverse fibre has

\[
 2^m-1\quad\hbox{members},\qquad
 \sum_{C\ne\varnothing}2^{-|A_C|}
   ={1\over4}\bigl((3/2)^m-1\bigr).                 \tag{5}
\]

The canonical post-flip fibre is therefore exponential even in half weight,
not bounded, polynomial, or subpolynomial.  The example does not refute
(HW): its many pre-flip chain faces make `Z_P(1)` exponential.  It proves
that a successful charge must retain those faces as capacity rather than
collapse them all onto `B`.

It also kills the most direct hull-vertex induction.  At the apex,

\[
 Z_{P-p}(1/2)=(3/2)^{m+2},
\]

whereas its link has polynomial

\[
 G_p(z)=1+(m+2)z+\binom{m+2}{2}z^2.                 \tag{6}
\]

Hence the sufficient induction step

\[
 Z_{P-p}(1/2)+{n\over2}G_p(1/2)\le2G_p(1)           \tag{7}
\]

fails exponentially for this legitimate hull vertex.  One would have to
select or amortize hull vertices globally.

## 3. The stronger half-activity mean statement is false

Under the activity-`1/2` face law let

\[
 \mu_{1/2}={\sum_A|A|2^{-|A|}\over Z_P(1/2)}.
\]

The sufficient statement `mu_(1/2)>=log_2 n-1` would imply (HW) by Jensen,
but it is false universally.  Exact reflection-order replay of the saved
rational fixed-`x` records gives

| `n` | exact profile | `mu_(1/2)` | `mu_(1/2)-(log_2 n-1)` |
|---:|---|---:|---:|
| 24 | `(1,24,276,2024,5378,2679,413,43,3)` | `3.5623676153` | `-0.0225948854` |
| 30 | `(1,30,435,4060,13975,10607,3158,481,30)` | `3.8243197448` | `-0.0825708508` |

These configurations are not certified global `V`-minimizers, so the
minimizer-only version remains possible.  Direct (HW) also remains true on
both (`H=1.6861...` and `1.7302...`).

## 4. A maximally flexible natural local flow still fails

There is a clean way to test whether the missing chain history can be
recovered by a fractional local charge.  First charge the two incidences on
every simplicial cover `A < B=A union {p}` to `B`.  At half activity their
combined load at a rank-`k` face is

\[
 k(2^{-k}+2^{-(k-1)})={3k\over2^k}.                 \tag{8}
\]

This leaves capacity

\[
 c_k=2-{3k\over2^k}\ge0                             \tag{9}
\]

from the desired two units per face.  Now allow more flexibility than an
orientation:

* each blocked exterior incidence `(A,p)` of demand `2^(-|A|)` may split
  fractionally in any proportions between `A` and `Phi(A,p)`;
* each interior incidence may split between `A` and the singleton `{p}`.

Feasibility is an exact capacitated bipartite max-flow question.  On the
exact integral twenty-point half-weight record the totals are

```text
V                                      4775
blocked exterior incidences           43115
interior incidences                    15033
blocked + interior half-weight         241246/64 = 3769.46875
total residual capacity                364546/64 = 5696.03125
maximum locally routable mass          226958/64 = 3546.21875
exact deficit                          893/4     = 223.25
```

Thus failure is caused by a genuine Hall cut, not by insufficient total
capacity.  Even arbitrary fractional splitting between the two natural
endpoints cannot complete the charge.  In particular, source-only,
target-only, bounded-indegree, and simple greedy flip orientations are all
ruled out by one exact realizable configuration.

## 5. What survives

The direct statement

\[
 nZ_P(1/2)\le 2Z_P(1)                                \tag{HW}
\]

is still compatible with all exact data, as is the weaker
`H(P)=n^{o(1)}` needed for the leading `1/2` coefficient.  The visible-chain
analysis narrows the viable form of a proof:

1. it must preserve enough of the hidden down-set to use the many inverse
   faces as capacity;
2. it must allow charge to travel through more than one flip, since the
   natural two-endpoint Hall condition is false;
3. interior incidences need a genuine radial-chain operation rather than a
   collapse to `{p}`; and
4. alternatively, global `V`-minimality must prohibit the Hall obstructions
   seen in arbitrary realizable configurations.

A precise surviving target is a **multistep flip-flow theorem**: on a global
`V`-minimizer, route each blocked/interior incidence through the down-set of
inverse flips, with congestion `n^{o(1)}` per face.  The pocket example shows
why the down-set cannot be replaced by its root, while the twenty-point cut
shows why one step is insufficient.

## 6. Verification

From the repository root:

```bash
python3 -m py_compile \
  phase2/loop/erdos838/agent_visible_flip_hw/visible_flip_audit.py

python3 \
  phase2/loop/erdos838/agent_visible_flip_hw/visible_flip_audit.py \
  > /tmp/visible_flip_audit.json
```

The verifier uses exact integer orientation/hull tests, exact rational
partition functions, and an integer max flow scaled by `2^20`.  It checks
all subsets of the finite pocket certificate, reconstructs the `n=24,30`
profiles from their rational reflection orders, and enumerates all `2^20`
subsets for the local-flow obstruction.
