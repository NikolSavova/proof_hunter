# The convex-face f-vector is not log-concave

**Date:** 2026-08-14  
**Verdict:** ultra-log-concavity and ordinary adjacent log-concavity both
fail, even for exact integral planar point sets in general position.  Thus a
Mason-style theorem cannot be the missing lower-bound argument for Erdős
838.  A weaker block-doubling property survives every saved exact profile and
would be quantitatively sufficient: a block length
`b=O(log log n)` forces the uniform mean rank to be
`log n-O(log log n)`.  This block statement is not proved here and should be
viewed as the exact surviving gate, not as a consequence of a known
log-concavity theorem.

All logarithms are base two.  For a general-position planar point set `P`, put

\[
 v_k(P)=|\{A\subseteq P:|A|=k,\ A\text{ is in convex position}\}|,
 \qquad V(P)=\sum_kv_k(P),
\]

and let

\[
 \mu(P)={\sum_k k v_k(P)\over V(P)}
\]

be the rank of a uniformly random convex subset.  The empty set is included.

## 1. Exact stretchable counterexample to ordinary log-concavity

Take `P={(i,y_i):0<=i<=13}`, where

```text
(y_0,...,y_13) =
(-4015, 2780, 8170, 5429, -4867, -2452, -5229,
 -5102, 7389, -596, -8841, -8375, -8464, -8566).
```

All coordinates are integral and every orientation determinant is nonzero.
Exact enumeration gives

\[
 (v_0,\ldots,v_{14})
 =(1,14,91,364,668,606,253,15,2,0,0,0,0,0,0).
\]

At rank seven,

\[
 v_7^2=15^2=225
 <253\cdot2=v_6v_8=506.                         \tag{1}
\]

So the f-vector need not be log-concave.  This is not a nonstretchable
or floating-point artifact.  The verifier below checks general position with
integer determinants and recomputes the profile in two independent ways:

1. direct monotone-chain convex-hull enumeration of all `2^14` subsets;
2. enumeration of all nonconvex four-circuits followed by Boolean upward
   closure.

The two exact profiles agree.

## 2. A six-point counterexample to ultra-log-concavity

Take

\[
 P_6=\{(i,i^2):0\le i\le4\}\cup\{(5,0)\}.
\]

It is in general position and has exact profile

\[
 (v_0,\ldots,v_6)=(1,6,15,20,5,1,0).
\]

This profile is ordinarily log-concave, but the normalized sequence
`v_k/binom(6,k)` is not.  At rank four the cross-multiplied ULC inequality
would require

\[
 v_4^2\binom63\binom65
 \ge v_3v_5\binom64^2.
\]

Instead its two sides are respectively `3000` and `4500`, a ratio of `2/3`.
The verifier again certifies both the coordinates and the profile exactly.

## 3. Census of the saved exact data

The audit recursively scanned every JSON certificate below `erdos838/` and
deduplicated every integer array having the necessary exact profile prefix

\[
 (1,n,\binom n2,\binom n3).
\]

It found 59 distinct saved profiles.  The result is:

| shape test | saved failures |
|---|---:|
| ordinary adjacent LC, `v_k^2 >= v_(k-1)v_(k+1)` | 0 / 59 |
| ULC, LC of `v_k/binom(n,k)` | 14 / 59 |
| two-step LC, `v_k^2 >= v_(k-2)v_(k+2)` | 0 / 59 |

Thus the saved corpus by itself made ordinary LC look plausible; the
14-point configuration above is an adversarial kill found outside it.
Two-step LC remains alive only as an experimental observation.  It also
survives the new ordinary-LC counterexample, but there is no proof and no
claim of universality.

The corpus includes the central Pascal profiles at parameters 16, 32, and
64 and the saved hard profiles at `n=44` and `n=58`.  The block test in
Section 5 holds with `b=1` on 55 of the 59 profiles and with `b=2` on the
remaining four.  The latter are one `n=17` profile, the `n=44` hard record,
and two distinct saved `n=58` arrays.  All 24 guarded fixed-template
directional iterates in the rankwise certificate pass with `b=1`.

These are exhaustive statements about the saved certificate corpus, not
about all order types.

## 4. Why the nearby literature does not rescue LC

A targeted literature search found powerful log-concavity results nearby,
but none that applies to this rank sequence.

Chan and Pak's
[*Log-concave poset inequalities*](https://arxiv.org/abs/2110.10740)
proves weighted feasible-word inequalities for several classes including
poset antimatroids and interval greedoids.  Our `v_k` counts unordered
convexly independent subsets of the point convexity; it is not the
feasible-word statistic asserted there.  The explicit configuration in
Section 1 rules out any interpretation that would imply adjacent LC for
these `v_k`.

The convex-geometry **free complex** is also a different object.  Its free
sets are both closed and independent, whereas an Erdős-838 face need only be
convexly independent: it may omit ambient points lying inside its hull.
For example, the work on
[*Local topology of the free complex of a two-dimensional generalized
convex shelling*](https://doi.org/10.1016/j.disc.2007.07.078)
therefore does not give an f-vector theorem for the present complex.

The search conclusion is deliberately narrow: no directly applicable
published LC theorem was found, and in any event ordinary LC and ULC are now
refuted by exact stretchable examples.

## 5. A weaker block property that would be enough

Put

\[
 \ell=\lceil\log n\rceil.
\]

Consider the following property for a positive integer `b`:

\[
 \boxed{v_{k+b}\ge2v_k\quad(0\le k\le\ell-2b).}     \tag{BD}_b
\]

This is substantially weaker than demanding monotone adjacent ratios.  It
allows local collapses such as (1), provided a short block still gains a
factor two.

> **Proposition (block doubling implies near-maximal mean).**  If
> `(BD)_b` holds, then
> \[
>  \boxed{\mu(P)\ge\ell-4b.}                       \tag{2}
> \]

**Proof.**  If `ell<4b`, the conclusion follows from `mu>=0`, so suppose
`ell>=4b`.  Partition the ranks at most `ell-b` by their residue modulo `b`.
For each nonempty residue chain let `t` be its largest rank at most
`ell-b`.  Then `t>ell-2b`, and repeated use of `(BD)_b` gives

\[
 v_{t-qb}\le2^{-q}v_t\qquad(q\ge0).                \tag{3}
\]

Relative to `ell`, the total deficit on this chain is at most

\[
 \begin{aligned}
 \sum_{q\ge0}(\ell-t+qb)v_{t-qb}
 &\le (\ell-t)\sum_{q\ge0}v_{t-qb}
       +bv_t\sum_{q\ge0}{q\over2^q}\\
 &<2b\sum_{q\ge0}v_{t-qb}+2bv_t\\
 &\le4b\sum_{q\ge0}v_{t-qb}.                     \tag{4}
 \end{aligned}
\]

Every rank above `ell-b` has deficit `ell-k<b<4b` (and ranks above `ell`
have negative deficit).  Summing (4) over the residue chains therefore gives
`ell-mu<=4b`, proving (2).  QED.

Consequently, a universal proof of `(BD)_b` with

\[
 b=O(\log\ell)=O(\log\log n)                       \tag{5}
\]

would give

\[
 \mu(P)\ge\log n-O(\log\log n).                   \tag{6}

This is stronger than the `log n-o(log n)` mean estimate sufficient for the
coefficient-one-half lower bound in Erdős 838.  It is therefore a clean
replacement target for false global LC.  The empirical `b<=2` phenomenon is
encouraging, but the range `k<=ell-2b`, especially around the hard
continuation ranks, contains the real content.

## 6. Even true LC would not by itself close 838

There is a second obstruction: the combination of LC with the currently
known quarter-scale mass lower bound is quantitatively insufficient.

Let `n=2^L`, `m=L/4`, and define an abstract positive sequence through rank
`L` by

\[
 w_k=\binom nk\quad(0\le k\le m),\qquad
 w_{m+j}=\binom nm2^{-j}\quad(1\le j\le L-m).       \tag{7}
\]

This is not asserted to be geometrically realizable.  It is an exact
logical countermodel to a shape-only deduction.  Both adjacent and two-step
log-concavity hold: binomial ratios decrease up to `m`, the ratio at the
junction drops to `1/2`, and every later ratio equals `1/2`.  On the other
hand,

\[
 \log\sum_kw_k\ge\log\binom n{L/4}
 ={L^2\over4}-O(L\log L),                           \tag{8}
\]

while its mean is only

\[
 {\sum_kkw_k\over\sum_kw_k}=L/4+O(1).              \tag{9}
\]

The verifier checks (7) with exact rational arithmetic at `L=64`, including
both LC systems; its mean is `17+o(1)` rather than near `64`.  Thus even if
two-step LC were eventually proved, it would need a genuinely geometric
growth input such as `(BD)_b` to affect Erdős 838.

## 7. Verification and next attack

Run

```bash
python3 phase2/loop/erdos838/agent_cyclic_stem_hw/verify_fvector_shape.py
```

The script writes `fvector_shape_certificate.json`.  It uses only integer
geometry and exact rational arithmetic for finite claims.

The most useful next question is no longer log-concavity.  It is the
following bounded-window continuation statement:

> Does every planar convex-independence profile satisfy `(BD)_b` for some
> `b=O(log log n)`, at least for `k<=ell-2b`?

A direct combinatorial route is to route two tokens from every rank-`k` face
to distinct rank-`k+b` extensions, with global target capacity one; more
generally, `2C` tokens with target capacity `C` would suffice.  This would
imply `(BD)_b`.  It interfaces directly with the capped Hall / cyclic-stem
route: a block can absorb local low-up-degree failures, while the factor two
is precisely the geometric growth needed by the residue-chain proof above.
