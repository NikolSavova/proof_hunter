# Exact structure of planar repair deletions

**Date:** 2026-08-14.  This note classifies the repair incidences used in the
rank-extension attack.  All point sets are in planar general position.

For a nonconvex set `S`, write

\[
 B=\operatorname{ext}(S),\qquad I=S\setminus B,
\]

and call `x in S` a **repair** if `S-x` is in convex position.

## 1. The exact dichotomy

> **Theorem 1 (interior singleton or ear replacement).**  Let `S` be
> nonconvex and let `x` repair `S`.
>
> 1. If `x in I`, then `I={x}` and `S-x=B`.
> 2. If `x in B`, let `u,v` be the two neighbours of `x` in the cyclic
>    order of the convex polygon `B`.  Then every point of `I` lies in the
>    open ear triangle `conv{u,x,v}` and outside `conv(B-x)`.  In the cyclic
>    order of the convex polygon `S-x`, the points of `I` form one
>    consecutive interval between `u` and `v`; the complementary interval
>    is `B-x`.
>
> Conversely, if `B` is convex, `x in B`, and a disjoint set `I` in the
> open ear at `x` is a convex replacement chain for which `(B-x) union I`
> is in convex position, then `x` repairs `B union I` and `B` is its hull.

### Proof

If `x` is interior, deleting it does not change `conv(S)=conv(B)`.  Every
other member of `I` would remain nonextreme, whereas `S-x` is convex.
Therefore `I={x}`.

Now suppose `x in B`.  Removing a vertex of a convex polygon changes its
hull only in the ear at that vertex:

\[
 \operatorname{conv}(B)setminus\operatorname{conv}(B-x)
 \subset \operatorname{conv}\{u,x,v\}.                         \tag{1}
\]

If some `y in I` belonged to `conv(B-x)`, it would remain nonextreme in
`S-x`, contradiction.  Thus every `y in I` lies outside `conv(B-x)` and,
by (1), in the open ear triangle.  General position excludes its boundary.

All points of `S-x` are vertices.  The old vertices `B-x` preserve their
cyclic order.  The boundary arc from `u` to `v` which formerly used `x` is
therefore replaced by all points of `I`, in their boundary order; no member
of `B-x` can occur on this arc.  Hence `I` is one consecutive cyclic
interval and `B-x` is the complementary one.  The converse is immediate
from the stated hull and convexity conditions. `square`

This is the exact cyclic interlacing sought in the pocket route.  There is
no arbitrary interleaving: a hull repair performs a single interval
substitution.

## 2. Canonical hidden-interval tag from the target face

The same statement can be read from the repaired face.  Let `A` be a
convex `k`-set and let `x` be bad for `A`, so `S=A+x` is nonconvex.  Put

\[
 I_x=A\setminus\operatorname{ext}(A+x).                         \tag{2}
\]

If `x` is interior to `conv(A)`, then `I_x` is empty and `x` is the unique
interior repair.  Otherwise `I_x` is a nonempty consecutive interval in
the cyclic order of `A`, and

\[
 \operatorname{ext}(A+x)=(A\setminus I_x)\cup\{x\}.             \tag{3}
\]

Thus every exterior boundary incidence has a canonical tag consisting of
two interval endpoints (or, more redundantly, the `k`-bit indicator of
`I_x`).  There are only `k(k-1)` oriented nonempty proper cyclic intervals,
not `2^k` arbitrary hidden sets.  What this tag does **not** recover is the
identity of `x`: arbitrarily many ambient points can occupy the same
replacement cone.  Any injection must charge that remaining multiplicity
to convex mass among those points, or spend `log n` further bits.

## 3. Exact repair-incidence counts

Let `v_k` be the number of convex `k`-sets in an ambient `n`-point set, and
let

\[
 b(A)=|\{x\notin A:A+x\text{ is nonconvex}\}|,
 \qquad B_k=\sum_{|A|=k,\ A\text{ convex}}b(A).
\]

Let `R_(k+1)` be the number of repair incidences `(S,x)` with
`|S|=k+1`.  The maps

\[
 (S,x)\longmapsto(S-x,x),\qquad (A,x)\longmapsto(A+x,x)
\]

are inverse bijections, and the ordinary cover double count gives

\[
 \boxed{
 R_{k+1}=B_k=(n-k)v_k-(k+1)v_{k+1}.}                         \tag{4}
\]

The dichotomy splits (4) exactly.  With
`iota_P(A)=|P cap int(conv(A))|`, the interior-repair part is

\[
 R_{k+1}^{\rm int}
 =\sum_{|A|=k,\ A\text{ convex}}\iota_P(A).                    \tag{5}
\]

For a convex polygon `B` and `x in B`, let `E_x(B)` be its open ear triangle
at `x`, and let `N_d(B,x)` count `d`-subsets `I` of `P cap E_x(B)` for which
`(B-x) union I` is convex.  The ear-repair part is

\[
 \boxed{
 R_{k+1}^{\rm ear}
 =\sum_{h=3}^{k}\ \sum_{|B|=h,\ B\text{ convex}}\ \sum_{x\in B}
    N_{k-h+1}(B,x).}                                             \tag{6}
\]

Equations (5)--(6) are disjoint and sum to (4).

For `k>=4`, the angular-gap argument in
`agent_tilted_switch/REPORT.md` further says that a fixed nonconvex
`(k+1)`-set has at most three repairs: at most one of type (5), and (when
the hull has at least four vertices) at most two of type (6).  The
triangular-hull case has no interior repair once it has at least two
interior points, but may have three ear repairs.

## 4. The remaining cone fibre is completely unrestricted

The interval classification is sharp, but it does not regularize the points
which share a tag.

> **Lemma 2 (arbitrary replacement-cone fibre).**  Given any finite planar
> point set `Q`, there are a triangle `A={u,a,v}` and an affine copy `Q'` of
> `Q`, disjoint from `A`, such that for every `x in Q'`
> 
> \[
>  A\setminus\operatorname{ext}(A+x)=\{a\}.                       \tag{7}
> \]

**Proof.**  Take `u=(-1,0)`, `a=(0,1)`, `v=(1,0)`.  The set of points `x`
near `(0,3)` for which `a` lies strictly inside `conv{u,x,v}` is open.
Put a sufficiently small affine copy of `Q` in this open neighbourhood and
avoid the finitely many new collinearities.  Then (7) holds for every copy
point, while the internal order type of `Q` is unchanged. `square`

For an exact integer instance, take

```text
A = {(-1000,0), (0,1000), (1000,0)}
Q' = {(-10,2987), (-6,3005), (-2,2987),
      (1,2990), (14,2990), (18,3002)}.
```

The six-point fibre is the indecomposable guard from `REPORT.md`; the nine
points are in general position, and every fibre point hides exactly the
middle vertex of `A`.

Therefore an endpoint/interval tag cannot bound its own inverse fibre:
one replacement cone can contain an arbitrary smaller instance of Erdős
838.  A successful count must recurse into that fibre while preserving the
two tangent endpoints.  This explains precisely why the tag removes cyclic
interlacing entropy but does not by itself complete the maximal-pocket
reset.

## 5. Consequence for the desired encoding

The interval theorem improves the geometric part of a repair tag from an
arbitrary `k`-bit subset to two cyclic endpoints, costing `O(log k)` bits.
For ranks with

\[
 n\le2^{k+o(k)},                                                  \tag{8}
\]

the unrecovered point identity costs at most `k+o(k)` bits, and the trivial
encoding `(A, endpoints, x)` gives

\[
 R_{k+1}^{\rm ear}\le 2^{k+o(k)}k^{O(1)}v_k.                    \tag{9}
\]

In fact (4) already gives `R_(k+1)<=n v_k`; the value of the cyclic theorem
is that the geometric history itself has only polynomial ambiguity.  To
obtain a useful estimate below the near-logarithmic range, where
`n>2^{k+o(k)}`, one must compress the population of points sharing one
replacement cone.  The cyclic/ear classification isolates this as the only
remaining multiplicity; no extra interlacing entropy is hidden in `I_x`.

## 6. Verification

`nested_repair_verify.py` generates deterministic exact integer point sets,
enumerates every subset, checks the two cases of Theorem 1 face by face,
and verifies (4)--(6) at every rank.  It also checks that every exterior
hidden set (2) is a cyclic interval, and validates the exact unrestricted
cone-fibre example above.

Run:

```bash
python3 phase2/loop/erdos838/agent_low_v_structure/nested_repair_verify.py
```
