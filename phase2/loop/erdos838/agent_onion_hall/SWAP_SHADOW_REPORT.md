# Swap graphs and shadows at the final Hall gate

**Date:** 2026-08-14  
**Verdict:** the proposed one-swap degree estimate is true (for the relevant
ranks `r>=4`), but source-local swap sparsity does not supply the rankwise
Hall gain.  An exact planar family
has exponentially many near-maximal rank-`r` sources, contains an
exponential one-swap-independent constant-weight code, and has full source
swap degree exactly `4r^2`, unchanged when arbitrarily many blocked points
are inserted.  Hence a swap/shadow proof which does not enter the blocked
pockets cannot produce the required `n/2^r` gain.

## 1. The exact one-swap theorem

Let `A` be a convex `r`-face of an `n`-point planar general-position set.
Write `u(A)` for its number of addable points.  A one-swap neighbor is a
convex face

\[
 B=(A\setminus\{a\})\cup\{p\},\qquad a\in A,\ p\notin A.
\]

> **Theorem 1 (sparse Johnson neighborhood).**  If `r>=4`, then the number
> `d_J(A)` of distinct one-swap convex neighbors satisfies
> \[
> \boxed{d_J(A)\le r u(A)+2(n-r-u(A)).}               \tag{1}
> \]

**Proof.**  Split the outside point `p` into two cases.  If `p` is addable,
then `A+p` is convex and all its subsets are convex.  There are at most `r`
choices of the deleted point `a`, contributing at most `r u(A)` neighbors.

If `p` is blocked, put `S=A+p`.  This is a nonconvex set of size `r+1>=5`.
The planar repair-degree theorem says that at most three points `x in S`
have `S-x` convex.  One of them is `p`, since `S-p=A`.  Consequently at
most two points `a in A` give a convex swap `S-a`.  There are
`n-r-u(A)` blocked points, proving (1).  Different pairs `(a,p)` give
different neighbors because `p=B\setminus A` and `a=A\setminus B`.  QED.

The restriction `r>=4` is necessary.  A triangle together with one interior
point is a nonface with four repairs; taking the triangle as `A` gives three
swaps through one blocked point, whereas the coefficient two in (1) would
allow only two.

The coefficient two for blocked points is sharp already at `r=4`.  In the
ordered five-point set

```text
(19,-13), (-3,20), (-7,-6), (5,-6), (19,-20)
```

take `A` to have labels `0,1,2,4` and insert label `3`.  The insertion is
blocked, and exactly the deletions of labels `1` and `2` repair it.  The
verifier checks this certificate exactly.

For a near-maximal source `u(A)<=4(r+1)`, (1) gives

\[
 d_J(A)\le2n+4r^2-6r-8\le2n+4r^2.                   \tag{2}
\]

This is a factor `Theta(r)` below the ambient Johnson degree `r(n-r)` in
the critical regime.  The next construction shows that this sparsity can be
genuine without yielding the desired Hall expansion.

## 2. An arbitrarily large exterior cloud which freezes every swap

Fix `r>=4`, put `M=5r`, `L=M-1`, and use the exact concave chain

\[
 q_i=(i,i(L-i))\quad(0\le i\le L).                  \tag{3}
\]

For the apex `p_0=(-1,M^2)` and every `i<j<k`, direct orientation gives

\[
 q_j\in\operatorname{int}\operatorname{conv}\{p_0,q_i,q_k\}. \tag{4}
\]

There are finitely many strict containments in (4), so they persist on an
open neighborhood `U` of `p_0`.  Choose an arbitrarily large rational
general-position set `E\subset U`, avoiding all lines determined by the
chain and by earlier choices.  Every member of `E` is exterior to every
chain face and hides the middle member of every selected chain triple.  Let
the source family be all rank-`r` chain faces
`A\subset\{q_0,\ldots,q_L\}`.

> **Theorem 2 (swap-frozen planar code host).**  Every source is a
> convex rank-`r` face satisfying
> \[
> u(A)=4r,
> \qquad d_J(A)=4r^2,
> \qquad e(A)=|E|.                                    \tag{5}
> \]
> The first two quantities and the complete one-swap neighborhood are
> independent of `|E|`, while the exterior blocked count is arbitrary.

**Proof.**  Every chain subset is convex, so precisely the `M-r=4r`
omitted chain points are addable.  Every `p in E` is exterior and blocked by
(4), because `A+p` contains at least three chain vertices.

Every addable chain point gives all `r` swaps, hence `4r^2` neighbors.  No
blocked point gives a swap: after deleting one source vertex, `r-1>=3`
chain vertices remain, and (4) again makes their union with `p` nonconvex.
Thus (5) is exact.  QED.

The construction is an actual rational planar order type, so every planar
rooted-circuit elimination statement holds.  Nevertheless its local swap
data does not even detect how many exterior points have been placed in `E`.
In particular, even an arbitrarily large value of `e(A)` supplies no swap
expansion by itself.

## 3. Realizable constant-weight-code behavior

The sources induce the Johnson graph

\[
 J(5r,r).                                             \tag{6}
\]

It has degree

\[
 r(5r-r)=4r^2.                                       \tag{7}
\]

A greedy independent set therefore gives a family `C` of pairwise
non-one-swap convex sources with

\[
 |C|\ge
 \frac{\binom{5r}{r}}{1+4r^2}
 \ge \frac{5^r}{1+4r^2}.                            \tag{8}
\]

The second inequality uses
`binom(m,k)>=(m/k)^k`.

Because two codewords never share `r-1` points, their immediate downward
shadows are disjoint.  Thus constant-weight-code behavior, including the
usual disjoint-shadow phenomenon, is fully realizable by planar convex
faces; circuit elimination does not forbid it.

More generally, a greedy distance-`t` code in (6) has size at least

\[
 \frac{\binom{5r}{r}}
 {\sum_{i=0}^{t}\binom{r}{i}\binom{4r}{i}},          \tag{9}
\]

and its shadows remain disjoint down through rank `r-t`.  This is useful
expansion, but it is only source-internal: a rank-`r` source has at most
`2^r` downward subfaces.  The Hall normalization needs `Theta(n/2^r)`
target units per source, which can be made arbitrarily larger while
the source swap graph and all its shadows stay fixed by enlarging `E`.

## 4. The precise barrier to a swap/shadow completion

Choose

\[
 |E|=2^{r+g}-5r.
\]

Then the ambient size is `n=2^{r+g}` and the sources lie at rank
`r=ell-g`.  As `g` grows:

* their addable counts remain `4r`;
* their full swap degree remains exactly `4r^2`;
* their induced Johnson graph and every downward shadow remain unchanged;
* all added labels are exterior and blocked for every source;
* the Hall demand per source grows as `2^g=n/2^r`.

Therefore no theorem based only on the source-local consequences of planar
circuit elimination, sparse one-swap neighborhoods, and shadows supported
inside the source vertices can imply `(RNP)`.  Those data are invariant
while the required gain is unbounded.  Full circuit elimination involving
the points of `E` may still expose the missing capacity.  Thus a successful
multilevel proof must cross into faces using the blocked exterior pockets;
once it does so, it is again the target-face encoding and overlapping-pocket Hall
problem isolated in the companion report.

This is a barrier to the proposed route, not a counterexample to `(RNP)`.
The new points in `E` contribute many convex target faces, so the global
inequality may still hold.

## 5. Exact verification

Run

```bash
python3 phase2/loop/erdos838/agent_onion_hall/verify_swap_shadow_barrier.py
```

The exact audit uses `r=4`, 20 chain points and eight rational exterior
apices.  It checks general position and all rooted-triple containments, all
4,845 sources, exact addable count 16, exact swap degree 64 on every source,
a greedy one-swap-independent code, and disjoint immediate shadows.
