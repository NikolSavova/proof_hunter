# The fixed-row six-projection four-cycle gate

## Summary

Fix a realized difference `d in D=A-A`.  Every transverse relation

\[
 d=(u-v)+J(x-y)                                      \tag{0.1}
\]

is represented by one quadruple `(u,v,x,y) in A^4`.  The resulting
four-partite relation system has a useful exact property: **every two
coordinate roles determine the entire relation**.  Consequently each of its
six two-coordinate projections is a simple bipartite graph on two copies of
`A`, and every projection has exactly `r(d)` edges.

This produces a new, strictly local sufficient theorem.  If, for every `d`,
one of the six projection graphs has at most `k^(2+o(1))` four-cycles, then

\[
 r(d)\le k^{3/2+o(1)}.                              \tag{0.2}
\]

Summing over the fewer than `k^2` rows gives the partial global estimate
`T<=k^(7/2+o(1))`.  In the wide regime, where the parallel collision term is
already covered by Elekes's trapezoid theorem, the translate-union argument
then gives

\[
 |A+J(A-A)|\ge k^{5/2-o(1)}.                       \tag{0.3}
\]

For `A subset [m]^2`, this would imply `k<=m^(4/5+o(1))`, or an upper
exponent `2/5` after writing `n=m^2`.  This is not the desired cube-root
bound, and the fixed-row four-cycle estimate is not proved.  It is valuable
because it is the first local strengthening that survives both targeted
`k^(3/2)` row constructions sharply.

The same audit also corrects a tempting simplification of the row--source
four-cycle gate.  Coordinate-degenerate row differences `delta in D union
JD` do carry the largest individual row-pair codegrees, but generic
differences already contribute `67.7%` of all row--source four-cycles at
`k=60`.  The final theorem cannot be reduced to the degenerate differences.

All finite data below are checked exactly by
`verify_transverse_fixed_row_c4.py`.

## 1. Pair-linearity of a fixed row

Put `D=A-A`, and let `J(a,b)=(-b,a)`.  For fixed `d in D`, let

\[
 \mathcal R_d=
 \{(u,v,x,y)\in A^4:
 d=(u-v)+J(x-y),\ x\ne y,\ d\cdot(x-y)\ne0\}.       \tag{1.1}
\]

Distance-Sidonicity implies oriented-difference uniqueness: every nonzero
element of `D` has one ordered endpoint pair.  It also implies that the two maps

\[
 A\times A\longrightarrow A+JA,\quad (a,b)\longmapsto a+Jb,
 \qquad
 A\times A\longrightarrow A-JA,\quad (a,b)\longmapsto a-Jb       \tag{1.2}
\]

are injective.  Indeed, a collision for either sign gives a nonzero equality
between a realized difference and a quarter-turn of another realized
difference; radial uniqueness then identifies the two underlying edges, and
no nonzero vector is equal to its positive or negative quarter-turn.  These
facts show that every pair of roles in (1.1)
determines the other pair.

* `(u,v)` determines `f=u-v`, hence
  `e=-J(d-f)=x-y`, and oriented-difference uniqueness determines `(x,y)`.
* `(x,y)` determines `(u,v)` in the same way.
* `(v,y)` determines the source `v+Jy`; its translate by `d` has at most one
  representation `u+Jx` by (1.2).  The pair `(u,x)` is symmetric.
* Given `(u,y)`, the equation
  `v-Jx=u-Jy-d` has at most one solution by the minus-sign case of (1.2).
  Given `(v,x)`, use `u-Jy=d+v-Jx` in the same way.

For every pair of coordinate positions `ij` among
`uv, ux, uy, vx, vy, xy`, let `G_d^{ij}` be the bipartite graph whose edges
are the corresponding projections of the members of `R_d`.  The preceding
argument proves

\[
 e(G_d^{ij})=|\mathcal R_d|=r(d)                   \tag{1.3}
\]

for all six choices, with no multiple edges.

## 2. Exact four-cycle implication

Let `G` be any bipartite graph with `k` vertices in each class, `E` edges,
and `Q` unlabelled copies of `C_4`.  If the left degrees are `a_i`, put

\[
 W=\sum_i {a_i\choose2}.
\]

Convexity gives

\[
 W\ge {E^2\over2k}-{E\over2}.                    \tag{2.1}
\]

If `c(p,q)` is the common-neighbour count of two right vertices, then

\[
 W=\sum_{p<q}c(p,q),\qquad
 Q=\sum_{p<q}{c(p,q)\choose2}.                   \tag{2.2}
\]

Therefore

\[
 W^2\le {k\choose2}(W+2Q).                       \tag{2.3}
\]

Equations (2.1)--(2.3) show that

\[
 Q\le k^{2+o(1)}\quad\Longrightarrow\quad
 E\le k^{3/2+o(1)}.                              \tag{2.4}
\]

Applied to any one of the six graphs `G_d^{ij}`, this proves (0.2).
The conjectural local input is thus

\[
 \boxed{\min_{ij} C_4(G_d^{ij})\le k^{2+o(1)}
        \quad\hbox{for every }d\in D.}           \tag{2.5}
\]

The minimum makes (2.5) weaker than demanding the estimate in a prescribed
projection.  The exact witnesses below in fact support all six estimates.

## 3. Conditional propagation to the grid

Assume (2.5) uniformly.  Since `|D|<k^2`, (2.4) gives

\[
 T=\sum_{d\in D}r(d)\le k^{7/2+o(1)}.             \tag{3.1}
\]

Here `T/2` is the transverse part of the block-intersection count for the
translates `A+Jd`.  If `A` is wide in the sense required by Elekes's
trapezoid theorem, the parallel part is `k^(3+o(1))` and is swallowed by
(3.1).  The exact random-thinning/Bonferroni inequality from
`PARALLEL_LINE_SUPPORT_LEMMA.md`, used with `D_0=D`, is

\[
 |A+JD|\ge
 \min\left\{{k|D|\over2},
 {k^2|D|^2\over4E(D)}\right\}.                   \tag{3.2}
\]

Because `|D|=k^2-k+1` and `E(D)<=k^(7/2+o(1))`, the second term is
`k^(5/2-o(1))`; the first is larger.  This proves (0.3) conditionally.
Since `A+JD` lies in a box with `O(m^2)` lattice points when
`A subset [m]^2`, one obtains

\[
 k\le m^{4/5+o(1)}.                               \tag{3.3}
\]

This conditional exponent is only asserted in the wide branch.  The
intermediate line-rich splice remains a separate missing step, just as it
does for the stronger cubic transverse conjecture.

## 4. Exact stress profiles

For the fixed heavy row `d=(0,-1)` in the 120-point relation-closure chain,
the six entries below are `(C_4, maximum pair-codegree)` in the order
`uv, ux, uy, vx, vy, xy`.

| `k` | `r(d)` | six projection profiles |
|---:|---:|:---|
| 30 | 119 | `(100,5), (72,4), (68,3), (63,4), (87,4), (59,4)` |
| 60 | 339 | `(462,7), (476,5), (450,5), (492,6), (433,5), (449,6)` |
| 90 | 614 | `(1015,7), (1058,6), (1088,7), (1068,7), (1225,8), (1081,7)` |
| 120 | 948 | `(1869,7), (1922,7), (1923,7), (2008,8), (2063,8), (2071,8)` |

For the strict-global-diameter construction with `d=(10000,0)`:

| `k` | `r(d)` | six projection profiles |
|---:|---:|:---|
| 35 | 61 | `(56,5), (23,4), (24,3), (24,4), (27,3), (16,3)` |
| 45 | 90 | `(96,5), (54,4), (57,4), (46,4), (38,3), (28,3)` |
| 70 | 180 | `(243,7), (131,4), (158,6), (154,6), (152,4), (108,7)` |
| 90 | 266 | `(473,9), (243,6), (262,6), (312,6), (447,6), (230,7)` |

Thus relation counts follow the sharp `k^(3/2)` scale while every tested
projection has only a constant multiple of `k^2` four-cycles and pair
codegree at most nine.  These are finite calibrations, not a proof of (2.5).

There is also a useful nonredundancy check.  At `k=120`, the six projection
cycle families contain respectively

\[
 1869,1922,1923,2008,2063,2071
\]

cycles.  Their union has `11852` members: `11850` occur in exactly one
projection and only two occur in three projections.  The small counts are
not an artefact of repeatedly viewing the same four relation edges in six
ways.

## 5. Why coordinate-degenerate row differences do not finish the global gate

For the row--source graph of `TRANSVERSE_ROW_SOURCE_C4_GATE.md`, take two
rows `d_1,d_2` with a common source `p`.  Their translated outputs have
difference

\[
 \delta=d_1-d_2=g+Jh,\qquad g,h\in D.             \tag{5.1}
\]

If `g=0`, then `delta in JD`; if `h=0`, then `delta in D`.  These are the two
coordinate-degenerate representation types.  When `g,h` are both nonzero,
their ordered endpoints are unique, and (5.1) is a genuinely transverse
representation of the row difference.

The largest row-pair codegrees in the heavy witness do tend to have
`delta in D union JD`.  Their total share of the four-cycle count, however,
decreases with `k`:

| `k` | generic `delta` | `delta in D` | `delta in JD` | generic fraction |
|---:|---:|---:|---:|---:|
| 20 | 14,257 | 11,443 | 7,367 | 0.4312 |
| 40 | 2,525,415 | 1,009,024 | 749,608 | 0.5895 |
| 60 | 19,883,439 | 5,399,578 | 4,087,094 | 0.6770 |

Here the three columns partition the exact unlabelled row--source `C_4`
count.  Thus an endpoint/coordinate-degeneracy cleanup can remove a
meaningful lower-order branch but leaves the majority generic term.

## 6. Remaining theorem and likely inverse form

The fixed-row conjecture (2.5) is weaker than the global fourth-moment gate
but still nontrivial.  A four-cycle in the `uv` projection is a rectangle of
four relations

\[
 J(u_i-v_j-d)\in D\qquad(i,j\in\{1,2\}).          \tag{6.1}
\]

Equivalently, an affine quarter-turn sends all four cross-differences of two
two-point subsets of `A` back into the complete realized difference set.
Large fixed bicliques can be realized with fresh auxiliary endpoints, so no
bounded forbidden-biclique theorem can prove (2.5).  Such a realization uses
quadratically many points for a balanced biclique and therefore has only the
`k^2` four-cycle scale.  A proof of (2.5) must show that more efficient global
reuse forces a repeated Euclidean norm.

The exact next inverse target is consequently:

> If one of the graphs in (1.3) has `k^(2+epsilon)` four-cycles, extract a
> reused Cartesian relation pattern in (6.1) whose associated edge vectors
> contain two non-antipodal vectors of equal norm.

No such extraction theorem is presently proved.  The main outcome of this
audit is a quantitatively meaningful intermediate gate, exact saturation
data, and a correction eliminating coordinate-degenerate row differences as
the whole explanation.
