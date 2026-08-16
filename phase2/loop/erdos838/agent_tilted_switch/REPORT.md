# Erdős 838: the tilted first-failure switch

**Date:** 2026-08-13  
**Verdict:** the first rooted-circuit switch admits a sharp, rigorous planar
counting lemma, but its natural multistep completion does not close the
half-weight bound.  The switch is nearly regular away from maximal convex
faces.  Maximal faces are the genuine obstruction: stable postponement around
them has linear (not subpolynomial) congestion under the exact `S_R(1)` tilt.

The empty face is included throughout.  No unrestricted solution of Erdős
838 is claimed here.

## 1. Boundary notation and the exact prefix measure

For a convex-position face `A` of an `n`-point set, put

\[
 u(A)=|\{q\notin A:A\cup\{q\}\text{ is convex}\}|,
 \qquad b(A)=n-|A|-u(A).
\]

Thus `u` is the number of addable points and `b` the number of bad
extensions.  Write

\[
 v_r=|\{A:|A|=r,\ A\text{ convex}\}|,
 \qquad B_r=\sum_{|A|=r}b(A).
\]

Double-counting covers gives

\[
 B_r=(n-r)v_r-(r+1)v_{r+1}.                         \tag{1}
\]

For a uniform permutation, `R` is the last convex prefix rank.  A stopped
permutation of rank `r` consists of an ordering of a convex `A`, a bad point
immediately after it, and an arbitrary tail.  Therefore

\[
 \Pr(R=r)=\frac{r!(n-r-1)!}{n!}B_r.                 \tag{2}
\]

Under the half-weight attack's exact tilt, its rank-`r` mass is (2) times

\[
 S_r(1)=\sum_{k=0}^r\binom nk.                       \tag{3}
\]

Equations (1)--(3) are useful because a switching proof must control `B_r`
with this precise tilt; raw permutation fibres are not the right quantity.

## 2. A planar repair-degree lemma

For a nonconvex set `S`, define

\[
 D(S)=\{x\in S:S\setminus\{x\}\text{ is convex}\}.
\]

> **Lemma 1 (at most three repairs).**  If `S` is a planar general-position
> set, is not in convex position, and `|S|>=5`, then
> \[
> |D(S)|\le3.                                          \tag{4}
> \]
> For `|S|=4`, the sharp bound is four.

**Proof.**  Let `H` be the vertices of `conv(S)` and `I=S\H`.  If an interior
point `x` belongs to `D(S)`, then `I={x}`; otherwise another member of `I`
remains nonextreme after deleting `x`.  Thus there is at most one interior
repair.

Suppose a hull vertex `x` is a repair, and fix `y in I`.  The point `y` must
lie outside `conv(H\{x})`; otherwise it is still nonextreme in `S\{x}`.
When `H` has at least four vertices, this puts `y` in the open ear triangle
at `x`, bounded by `x` and its two hull neighbours.

View the hull vertices radially around `y`, and let their successive angular
gaps be `delta_1,...,delta_h`.  They are positive, sum to `2 pi`, and no
relevant sum equals `pi` by general position.  Membership of `y` in the ear
at vertex `x_i` implies

\[
 \delta_{i-1}+\delta_i>\pi.                            \tag{5}
\]

Two disjoint adjacent-gap pairs satisfying (5) would already have sum more
than `2 pi`.  Hence all such pairs intersect.  In a cycle of length at least
four, a pairwise-intersecting family of edges has size at most two.  There
are consequently at most two hull repairs.  Together with the possible
single interior repair this proves (4).  If the hull is a triangle and
`|S|>=5`, there are at least two interior points, hence no interior repair
and at most its three hull vertices can repair.  Finally, a triangle plus one
interior point shows that all four deletions can repair when `|S|=4`.  QED.

The bound is attained in the finite certificates: repair degree four occurs
at rank four, while degree three occurs at larger ranks.

## 3. The nearly regular first-failure switch

The most local useful switch is now exact.  Count triples `(A,p,q)` such that

* `A` is a convex `r`-face;
* `p` is bad for `A`; and
* `q` is addable to `A`.

Move `q` immediately before the first bad point `p`.  Then `B=A+q` is a
convex `(r+1)`-face, while `p` remains bad for `B` by heredity.

> **Theorem 2 (rank-one boundary switch).**  For every `r>=3`,
> \[
> \boxed{
> (r-1)B_{r+1}
> \ \le\ \sum_{|A|=r}b(A)u(A)
> \ \le\ (r+1)B_{r+1}.}                              \tag{6}
> \]

**Proof.**  Fix a target boundary incidence `(B,p)`, where `|B|=r+1`, `B`
is convex, and `p` is bad for `B`.  Put `S=B+p`.  A point `q in B` is an
inverse choice precisely when `p` is still bad for `B-q`, or equivalently
when `S-q` is nonconvex.  Since `S-p=B` is convex, `p in D(S)`.  Lemma 1
says that at most two further members of `B` lie in `D(S)`.  Thus between
`r-1` and `r+1` choices of `q` are inverse choices.  Sum over `(B,p)`.  QED.

This is stronger than a bounded-fibre statement: after marking the addable
point, the switch is asymptotically regular with relative error `O(1/r)`.
Equivalently, under the uniform law on rank-`r` boundary incidences,

\[
 \mathbb E_\partial u(A)
   =\frac{\sum b(A)u(A)}{B_r}
   =(r+O(1))\frac{B_{r+1}}{B_r}.                       \tag{7}
\]

The exact minimizer audits give

```text
n=8: B = (0,0,0,196,84,...),   sum b*u = (0,0,0,252,0,...)
n=9: B = (0,0,0,360,165,12,...), sum b*u = (0,0,0,534,60,0,...)
n=20: B ranks 3..7 = (9720,34310,12180,1834,104),
      sum b*u = (78224,53460,10394,706,0)
```

and verify (6) face by face.

## 4. Why (6) does not yet iterate

The factor `u(A)` on the middle term of (6) is load-bearing.  A maximal
convex face has `u(A)=0` and contributes `(n-|A|)` to `B_r`, but contributes
nothing to the switch.  This is not a small exceptional class in the exact
minimizers:

```text
n=8 maximal faces by rank: 8 at rank 3, 21 at rank 4
n=9 maximal faces by rank: 14 at rank 3, 21 at rank 4, 3 at rank 5
n=20 maximal faces by rank: 789 at rank 4, 402 at rank 5,
                            87 at rank 6, 8 at rank 7
```

A convex hull triangle containing all remaining points is the simplest
example.  Every permutation beginning with that triangle stops at rank
three, and no reordering of the remaining points can extend this particular
face.  Any complete proof must restart inside a pocket or replace part of the
maximal face; merely postponing bad arrivals cannot work.

## 5. Exact failure of stable postponement under the tilt

There is a canonical multistep version of the switch.  Preserve the initial
convex prefix `A`, scan the rest of the permutation, accept a point if it
keeps the current set convex, and stably postpone it otherwise.  Once a point
is rejected it stays bad after every later acceptance, so the output has the
form

\[
 A\;G\;D,                                               \tag{8}
\]

with convex prefix `A+G` and all points of `D` bad.  This map can raise `R`
many steps at once.  Unfortunately, its exact tilted congestion is
polynomial.

Take a convex `h`-gon `H`, choose three of its vertices forming a triangle
`A`, and put `d=n-h` general-position points `D` inside that triangle.  Let
`G=H\A`, so `|G|=h-3`.  Fix the internal orders of `A,G,D`.  Every shuffle of
`G` and `D` after `A` maps under stable postponement to the one image
`A G D`, whose stopping rank is `h`.  If the first inner point occurs after
exactly `k` members of `G`, the source stopping rank is `3+k`, and the number
of such shuffles is

\[
 \binom{n-k-4}{h-k-3}.                                  \tag{9}
\]

Consequently the total exact tilted load on this one image is

\[
 L(n,h)=\sum_{k=0}^{h-3}
 \binom{n-k-4}{h-k-3}S_{k+3}(1),                         \tag{10}
\]

whereas the image has tilt `S_h(1)`.  Uniformly for `h=o(n)`, top-term
comparison and the exact identity

\[
 \frac{\binom{n-k-4}{h-k-3}\binom n{k+3}}{\binom nh}
 =\binom h{k+3}\frac{n-h}{n-k-3}                         \tag{11}
\]

give

\[
 \frac{L(n,h)}{S_h(1)}
 =(1-o(1))\sum_{j=3}^h\binom hj
 =(1-o(1))\left(2^h-1-h-\binom h2\right).               \tag{12}
\]

For `h=floor(log_2 n)`, this is `Theta(n)`, not `n^{o(1)}`.  The exact
checker obtains ratios `39.96`, `462.03`, and `4007.47` at `n=100,1000,5000`,
respectively; divided by `2^h` they tend rapidly to one.  A nine-point
integer realization checks all fifteen shuffles geometrically and has tilted
congestion `1353/191`.

This family does not disprove the half-weight conjecture.  It shows exactly
what the map forgot: the many convex subsets supported inside `D`.  Those
faces are the capacity to which a successful restart must route the stopped
outer-triangle trajectories.

## 6. Surviving proof target

The first-circuit attack is therefore reduced to a more precise two-part
statement.

1. Use Theorem 2 to transport all nonmaximal boundary mass upward.  This
   portion loses only `1+O(1/r)` per rank after the addable point is marked.
2. Prove a **pocket restart lemma** for the maximal-face portion.  It must
   route a stopped maximal face into convex faces supported in its excluded
   pockets, while retaining enough pocket identity that the nested-triangle
   family in Section 5 has bounded or subpolynomial congestion.

Any restart that records only the final extended face, only the first rooted
four-circuit, or only the accepted/rejected word is ruled out by (12).  The
state must include a recursively selected convex face inside the obstructing
pocket (or an equivalent endpoint/tangent history).  Establishing such a
restart with `n^{o(1)}` total congestion would complete (PST), hence the
half-weight inequality and Erdős 838.  No such restart theorem is proved
here.

## 7. Reproduction

Run

```bash
python3 -m py_compile \
  phase2/loop/erdos838/agent_tilted_switch/tilted_switch_audit.py

python3 \
  phase2/loop/erdos838/agent_tilted_switch/tilted_switch_audit.py \
  > /tmp/tilted_switch_audit.json
```

The script uses exact integer orientations.  It reconstructs the `n=8,9`
minimizer and `n=20` record face tables from their saved coordinates, exhausts
all their subsets, exhausts the `n=8,9` permutations, checks repair degrees
and (6), verifies the finite nested-triangle geometry, and writes all exact
arithmetic to `certificate.json`.
