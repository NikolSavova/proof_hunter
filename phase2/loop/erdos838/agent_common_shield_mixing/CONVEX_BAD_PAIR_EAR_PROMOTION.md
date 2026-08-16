# Convex bad pairs are genuine commuting ears

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The convex branch of `BAD_PAIR_RANK4_PIQ_CLASSIFICATION.md` is stronger
geometrically than the earlier report claimed.  In a complete same-type
macro product, a pair whose two canonical neighboring representatives form
a convex four-set is a genuine two-point boundary ear.  Ears in any
independent set of macro roles commute, even when their boundary edges
share an inactive anchor.  Thus polylogarithmic pair menus in
`Theta(log n)` roles give the absolute ordinary-face bank

\[
                  (\log n)^{\Theta(\log n)}
                    = n^{\Theta(\log\log n)}             \tag{1}
\]

with an injective pair decoder.

This count is **not automatically a new multiplier over the source or
pocket bank**.  Choosing one canonical endpoint of every matching pair
already gives the same `K^q` singleton-transversal bank, for all five
circuit classes.  Ear promotion becomes a genuine multiplier only when an
independent context `c` supplies a retained convex base `B_c`, every pair
is insertable relative to that base, and the output recovers `c` with
controlled load.  The exact conditional global formula is

\[
 V(P)\ \ge\ {1\over\Lambda}
       \sum_c\prod_{i\in I_c}K_{c,i}.                    \tag{1a}
\]

If the context already includes the endpoint choice, it must not be
counted again in the product.  This is the exact live pocket/coexistence
interface; complete same-type singleton transversals alone do not provide
it.

Consequently the linear matching residue has an exact geometric fork.
After a constant-loss five-way pigeonhole, either the `2+2` circuit class
promotes to commuting ears, or a common rooted `1+3` circuit class remains
on a linear number of roles.  Formula (1a) closes the first branch only in
a context-compatible atom.  Without that extra hypothesis, its `K^q`
count is the already available singleton scale.  The pair mark and both
canonical neighboring representatives are retained; there is no hidden
rank loss, but there can still be a context-coexistence or overlap loss.

This does **not** revive the false broad-cluster profile product.  A rich
multi-point local face need not be a boundary ear.  The result here uses
both labels of an actual pair and the convexity of its four-set with the two
adjacent macro representatives.

## 1. The local insertion lemma

Let `B` be a strictly convex polygon and let `l,r` be consecutive vertices
in its positive cyclic order.  Suppose `a,b` lie beyond the edge `lr`, both

\[
             B\cup\{a\},\qquad B\cup\{b\}               \tag{2}
\]

are strictly convex with `a` or `b` inserted between `l,r`, and
`l,a,b,r` is a strictly convex quadrilateral in that order.

> **Lemma 1 (two-point ear insertion).**  Then
> `B union {a,b}` is strictly convex in the order obtained by replacing
> the edge `lr` with the path `l,a,b,r`.

**Proof.**  Apply an orientation-preserving affine map taking

\[
 l=(0,0),\quad r=(1,0),\quad
 a=(\alpha,-s),\quad b=(\beta,-t),\qquad s,t>0.          \tag{3}
\]

Every other vertex of `B` has the form `z=(xi,Z)` with `Z>0`.  Put

\[
 D=s\beta-t\alpha,\qquad E=D+t-s.                       \tag{4}
\]

The two supporting-edge inequalities of the local quadrilateral are
exactly `D>0` and `E>0`.  Individual insertability of `a` gives

\[
       \alpha Z+s\xi>0,\qquad
       (1-\alpha)Z+s(1-\xi)>0.                          \tag{5}
\]

Finally

\[
 \chi(a,b,z)=D+(\beta-\alpha)Z+(t-s)\xi.                \tag{6}
\]

If `t>=s`, the first inequality in (5) gives

\[
                 \chi(a,b,z)\ge D(1+Z/s)>0.             \tag{7}
\]

If `t<s`, the second gives

\[
                 \chi(a,b,z)>E(1+Z/s)>0.                \tag{8}
\]

Thus every old vertex is on the interior side of the new edge `ab`.
The old vertices are on the interior sides of `la` and `br` by (2), while
the other new label is on the correct side by local quadrilateral
convexity.  All remaining old edges were already supporting edges in both
sets in (2).  Hence every edge of the asserted cyclic word supports the
whole set strictly.  QED.

The proof is useful because it is genuinely global: no small-cluster,
infinitesimal-substitution, or tangent-chain hypothesis occurs.

## 2. Simultaneous parity promotion

Partition a planar point set into cyclic roles

\[
                       X_0,X_1,\ldots,X_{q-1}.           \tag{9}
\]

Assume the complete same-type condition:

> every transversal `x_i in X_i` is a strictly convex polygon in the same
> cyclic role order.

Fix representatives `c_i in X_i`.  For a role `i`, call a pair
`e={a,b} subset X_i` a **convex bad-pair ear** if

\[
                       \{c_{i-1},a,b,c_{i+1}\}          \tag{10}
\]

is convex.  The same-type condition forces one of the two orders
`c_(i-1),a,b,c_(i+1)` and `c_(i-1),b,a,c_(i+1)`; use that order.

> **Theorem 2 (commuting pair ears).**  Let `I` be a set of pairwise
> nonadjacent roles.  Choose one convex bad-pair ear `e_i` in every
> `i in I`.  Then
>
> \[
>          W=\{c_j:j\notin I\}\ \cup\ \bigcup_{i\in I}e_i              \tag{11}
> \]
>
> is a strictly convex set in the expanded cyclic word.  If role `i` has
> a menu of `K_i` distinct pairs, the outputs (11) give exactly
> `product_(i in I) K_i` distinct ordinary faces.

**Proof.**  The inactive representatives form a convex base.  Consider an
active role `i`, write its ordered pair as `a_i,b_i`, and let
`l=c_(i-1), r=c_(i+1)`.  The edges `l a_i` and `b_i r` support every label
from every other role because each is an edge of a suitable full singleton
transversal; local four-set convexity handles the other label in `X_i`.

For the edge `a_i b_i`, fix any output label `y` outside `X_i`.  The
inactive base together with `y` is convex, `l,r` are still consecutive,
and its unions with `a_i` and with `b_i` are convex subsets of full
transversals.  Lemma 1 puts `y` on the interior side of `a_i b_i`.  This
works as well when `y` belongs to an ear on an adjacent boundary edge and
the two ears share `l` or `r`.  Every edge of the expanded word is therefore
a strict supporting edge.  Distinct menu choices retain different pair
labels, so the decoder is injective.  QED.

The nonadjacency hypothesis is only used so that the two neighboring
representatives of every active role are retained.  Any subset of roles on
a cycle contains an independent subset of size at least one third of its
cardinality.

### 2.1 Exact context summation

Let `mathcal C` be a family of contexts.  Context `c` consists of a retained
strictly convex base `B_c`, cyclic insertion gaps, an independent active
set `I_c`, and pair menus `M_(c,i)` of sizes `K_(c,i)`.  Assume for every
`e={a,b} in M_(c,i)` that `B_c union {a}` and `B_c union {b}` are convex
single insertions at gap `i`, and that the two gap endpoints together with
`a,b` are convex.  Theorem 2 applies inside each context and gives an
incidence family

\[
 \mathcal W_c=\left\{B_c\cup\bigcup_{i\in I_c}e_i:
                 e_i\in\mathcal M_{c,i}\right\},
 \qquad |\mathcal W_c|=\prod_{i\in I_c}K_{c,i}.          \tag{11a}
\]

Define the actual context load

\[
 \Lambda=\max_W
   \left|\left\{(c,(e_i)_{i\in I_c}):
       W=B_c\cup\bigcup_{i\in I_c}e_i\right\}\right|.  \tag{11b}
\]

Double counting (11a) gives (1a), with no other loss.  A sufficient
load-one condition is that `W` recovers `B_c`, the active role list, and
each disjoint pair trace.  Conversely, a pocket face which is absent from
`B_c`, or is destroyed by an ear insertion, contributes nothing to
(11a).  If `c` itself records the endpoint word `(e_i)`, then the formal
Cartesian product repeats the same source choices and must first be
quotiented; this is why the canonical-endpoint singleton bank already has
the raw cardinality (1).

## 3. Quantitative absolute bad-pair fork

Assume

\[
 q\ge \kappa L,\quad L=\log n,\quad |X_i|\le Cn/q,       \tag{12}
\]

and let `M_i` be pair matchings with

\[
                         \sum_i |M_i|\ge\eta n.          \tag{13}
\]

Classify each pair using its two fixed neighboring representatives.  Four
points in affine general position have one of the following signed-circuit
types.

* They are convex.  Their Radon partition is `2+2`, and the set is an
  ordinary rank-four face.
* One of the four points is inside the triangle of the other three.  This
  is one of four rooted `1+3` types: either pair endpoint is the root, or
  either fixed neighboring representative is the root.

One of these five types contains at least `eta n/5` records.  At least

\[
                         \eta q/(10C)                    \tag{14}
\]

roles then contain at least `eta n/(10q)` records of that same type: the
roles below this threshold carry at most `eta n/10`, and any one role
carries at most `Cn/q` records.

If the common type is convex, take an independent set of at least
`eta q/(30C)` such roles.  For any

\[
                  K\le \eta n/(10q),                    \tag{15}
\]

Theorem 2 gives

\[
               \#\{\hbox{decoded faces}\}
                   \ge K^{\eta q/(30C)}.                \tag{16}
\]

In particular, for `K=L^D` and all sufficiently large `n`, the absolute
bank satisfies

\[
 \log \#\{\hbox{faces}\}
       \ge {\eta\kappa D\over30C}L\log L,               \tag{17}
\]

which is the `n^{Theta(log log n)}` numerical scale.  It is the required
**relative** recovery multiplier only after (11a)--(11b) supplies an
independent retained context bank.  Otherwise the canonical-endpoint
singleton transversals already have this cardinality.

If the common type is nonconvex, (14) instead gives a rooted circuit menu
of size `Omega(n/q)` on `Omega(q)` roles.  Deleting either fixed anchor
from the four-record leaves a convex rank-three set containing both pair
labels, so the pair decoder has constant load.  In the anchor-inner cases
all chords cross the fixed ray from the other anchor through the inner
anchor; in the pair-inner cases the records are the fixed-edge
dominance/nesting obstruction.  This is now the sole geometric branch that
still requires a fan/one-gap/circuit release theorem.

Equations (16)--(17) are for one fixed representative skeleton and are
absolute counts.  For several contexts the only valid multiplier statement
is (1a) with the actual load (11b).  The theorem does not silently assume
that omitted active-role representatives or a separate pocket face are
recoverable, and it does not count the same endpoint word once as a context
and again as a menu choice.

## 4. Coherent `Pi_q` accounting

If one fixed completed child is genuinely queried at `q` later directions,
those queries cannot be encoded by independent `Pi_2` charts.
`BAD_PAIR_RANK4_PIQ_CLASSIFICATION.md` proves that one projective rechart
of an `N`-point child has only

\[
                         O((qN^2)^3)                     \tag{18}
\]

possible coherent itineraries.  It is one profile function on `RP^1`
precomposed by one element of `PGL_2`; from four queries onward the cross
ratio prevents independent prescriptions.

At `q=Theta(log n)` the cost of fixing the whole itinerary of that one
multiply queried child is only `O(log n)` bits, or a factor `n^{O(1)}`.
This is negligible compared with the `Theta(L log L)` exponent in (17).
It does not itself turn rooted circuits into faces.  More importantly, it
does **not** constrain the basic recursive wrapper with `q` independent
child copies, each queried only in its assembly chart and one future reset
chart; those copies have independent projective parameters and legitimate
independent `Pi_2` states.  The coherent bound matters only after an actual
history argument retains the same copy through four or more direction
queries.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_convex_bad_pair_ear_promotion.py
```

The checker exhausts integer instances of Lemma 1 in both depth cases,
checks the displayed determinant identities exactly, verifies a complete
same-type product on integer parabola blocks, multiplies simultaneous ears
on three roles, checks injectivity and the exact context-load summation,
and exhausts the cycle independent-set constant used in (16).  It also
reruns the exact five-type and coherent `PGL_2` verifier from the preceding
report.  The verifier deliberately confirms that canonical singleton
endpoints and doubled ears have the same raw menu cardinality; it does not
assert an untagged pocket multiplier.
