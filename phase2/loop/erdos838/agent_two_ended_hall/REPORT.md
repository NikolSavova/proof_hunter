# Two-ended Hall attack: exact local dichotomy and product discharge

**Date:** 2026-08-14  
**Verdict:** the unrestricted capped-Hall theorem is not proved here.  Two
useful parts of the proposed route are now rigorous.

1. Exterior blockers have an exact cyclic-interval packing dichotomy.  A
   disjoint batch can be repaired simultaneously and supplies a Boolean
   family of blocker-containing convex targets; otherwise one support edge
   is hit by a large fraction of the blockers and gives the desired rooted
   pocket restart.
2. The entropy-rich product obstruction is completely harmless at the
   **capped** Hall scale, for an arbitrary number and arbitrary order type of
   common apex blockers.  Up to blocker-cloud size `M^3`, the missing
   capacity is exactly the two-ended pool
   `binom(M,2)^2 M^(r-4)`.  Beyond `M^3`, the established universal
   coefficient-`1/4` bound inside the blocker cloud is already much larger
   than the capped demand.

There is also a sharp warning.  Simultaneous repair does not by itself give a
low-congestion global map.  In the same product geometry a maximal disjoint
batch erases independent source coordinates, and one target has inverse
fibre `(M-1)^Theta(r)`.  Thus the interval packing/rooted-pocket recursion
must be coupled to a genuine two-ended face count.  An endpoint word or the
Boolean repair cube alone cannot telescope.

All logarithms below are base two.  A convex face is a subset in convex
position.  The capped Hall demand at rank `r` is

\[
 D_r=2^{\ell-r},\qquad \ell=\lceil\log n\rceil.       \tag{1}
\]

Only `D_r` exterior labels per hard source need be selected.  Bounding all
exterior incidences, as in the stronger proposed EIC statement, is
unnecessary and can throw away the decisive freedom to discard surplus
labels.

## 1. Violated support intervals

Let `A=(a_0,...,a_(r-1))` be counterclockwise.  Orient each edge so that `A`
lies in its open left half-plane.  For an exterior point `p`, put

\[
 W_A(p)=\{i:\operatorname{orient}(a_i,a_{i+1},p)<0\}. \tag{2}
\]

The set `W_A(p)` is a nonempty cyclic interval of support edges.  Its first
and last edges end at the two tangency vertices from `p`.  In particular,
`p` is addable exactly in the one-edge case; an exterior blocked label has a
longer visible interval and hides the intervening chain.

> **Lemma 1 (simultaneous disjoint-window repair).**  Let `X` be a set of
> exterior points for `A`.  If the cyclic intervals
> `{W_A(p):p in X}` are pairwise disjoint, then every `p in X` is a vertex of
> `conv(A union X)`.  Consequently
> \[
>  \Phi_A(Y)=\operatorname{ext}(A\cup Y),\qquad Y\subseteq X, \tag{3}
> \]
> are `2^|X|` distinct convex faces, and every `Phi_A(Y)` contains `Y`.

**Proof.**  Fix `p in X` and choose an edge `i in W_A(p)`.  Every other
`q in X-p` satisfies the support inequality at edge `i`, because its
violated interval is disjoint from `W_A(p)`.  The line through
`a_i a_(i+1)` therefore strictly separates `p` from
`A union (X-p)`, so `p` is extreme.  This holds for every `p`.  Applied to
each `Y subset X`, it proves the containment assertion.  Distinct `Y` give
distinct point-set targets because the target contains exactly the selected
members of `X`.  QED.

The old vertices which survive can also be read from the gaps between the
violated intervals.  Adjacent intervals may jointly hide their separator
vertex, which is why the statement only claims what is needed: all new
labels survive and the resulting hull is an ordinary convex target.

There is a completely exact packing alternative.

> **Lemma 2 (cyclic interval batch or root).**  Let `d` exterior blockers of
> one source be represented by the intervals (2), and let `R>=1`.  Then
> either
>
> * there are `R` labels with pairwise disjoint violated intervals; or
> * some set of at most `R` support edges meets every violated interval.
>
> In the second case one support edge belongs to at least `d/R` blocker
> intervals.

**Proof.**  Let `nu` be the maximum number of disjoint cyclic intervals.  If
`nu>=R`, use Lemma 1.  Otherwise choose any support edge `e`.  All intervals
containing `e` are pierced by `e`.  Cutting the cycle at `e` turns the
remaining intervals into ordinary intervals on a line.  The greedy rule
"take the right endpoint of the interval with smallest right endpoint"
shows that a line-interval family has a piercing set whose size is its
maximum disjoint matching number.  That number is at most `nu`.  Thus all
cyclic intervals have a piercing set of size at most `nu+1<=R`.  Pigeonhole
gives the final assertion.  QED.

Taking `R=sqrt(r)` gives precisely the hoped-for local state reduction:
either `sqrt(r)` simultaneous exterior repairs, or a root edge shared by a
`1/sqrt(r)` fraction of the selected blockers.  Repeating only the second
alternative for `sqrt(r)` levels would cost at most
`r^O(sqrt(r))=2^O(sqrt(r) log r)=2^o(r)` endpoint states.  The geometric
localization needed for that batching idea is therefore sound.

For completeness, blocker pairs have an equivalent inclusion-poset
description.  Put `H_p=conv(A+p)` and order exterior labels by inclusion of
`H_p`.  Two labels are incomparable exactly when both are extreme in
`conv(A+p+q)`; if `H_p subsetneq H_q`, then `p` is hidden after `q` is
inserted.  Thus every blocker family has a chain or antichain of size at
least `sqrt(d)`.  The interval version is stronger for the intended rooted
recursion because it identifies an actual support edge.

## 2. Why the local Boolean cube does not telescope

Lemma 1 is not a global Hall map.  Here is an exact scalable regression
inside the product-block construction.

Take `b=r-2` ordered internal microblocks of size `M`, between two singleton
endpoints on a strictly concave macro chain.  A source chooses one point in
every internal block and both singleton endpoints.  In each odd internal
block fix its top micro-point as a blocker and let the source choose any of
the other `M-1` points.  Fix the source choices in the even blocks.

The fixed blockers are exterior ear replacements.  Their violated edge
intervals are pairwise disjoint: each consists of the two support edges at
its own selected macro vertex, and the intervening even blocks separate the
windows.  Adding the whole batch simply replaces every chosen odd-block
point by the fixed top point.  Hence all

\[
 (M-1)^{\lceil b/2\rceil}                          \tag{4}
\]

sources have the same simultaneous target.  At `M=2^r`, (4) has
`Theta(r^2)` bits.  This rules out any claim that the disjoint-window batch,
even with its full Boolean target cube, has `2^o(r)` global inverse load.

The exact rational audit uses `r=8,M=3`.  Three pairwise disjoint windows
have eight sources with the same final target.  It also checks all eight
sub-batch targets for a fixed source.  The scalable formula (4), rather than
the small instance, is the obstruction.

This is the same information deficit seen in the common-apex product
example: repair labels write their own identities into the target but erase
the source coordinates they replace.  Capacity must come from faces which
retain the source word in a different orientation.

## 3. The exact two-ended multiplication theorem

The needed capacity is present in the product geometry.  Let `Q_i` be the
microconfiguration in internal block `i`, of size `m_i`.  Write `C(Q_i)`
and `U(Q_i)` for the numbers of nonempty caps and cups.  The exact vertical
composition classification gives the following.

> **Theorem 3 (two-ended cell count).**  For every interval of internal
> blocks `i<j`, the faces whose first occupied block is `i`, whose last
> occupied block is `j`, and which occupy every block between them number
> exactly
> \[
>  C(Q_i)U(Q_j)\prod_{i<k<j}m_k.                  \tag{5}
> \]
> These families are disjoint for different `(i,j)`.  Consequently the
> product cell contains at least
> \[
>  \sum_{i<j}C(Q_i)U(Q_j)\prod_{i<k<j}m_k          \tag{6}
> \]
> ordinary convex faces.

**Proof.**  A convex set spanning at least two vertical blocks intersects
its first occupied block in a cap, its last occupied block in a cup, and
every intermediate occupied block in exactly one point.  Conversely every
such choice is convex.  This is the exact mixed-triple classification of a
vertical composition.  Formula (5) follows by multiplication, and the first
and last occupied blocks distinguish the families.  QED.

For `b=r-2` identical `M`-point blocks `Q`, the full-span term is

\[
 C(Q)U(Q)M^{b-2}.                                  \tag{7}
\]

Restricting each endpoint block to a two-point subset gives the completely
order-type-free rank-`r` slice

\[
 \boxed{\binom M2^2M^{r-4}}.                       \tag{8}
\]

This proves, rather than assumes, the multiplication suggested by the
product obstruction.  Formula (7) is the sharper recursive form: the full
two-ended credit is the cap--cup product of the pocket order type.  It also
exposes the remaining difficulty outside product cells.  Heterogeneous
pockets can anti-align the forward terms `C(Q_i)U(Q_j)`; separate cap and
cup marginals are insufficient.  A universal proof must preserve the
forward two-ended orientation through the rooted recursion.

## 4. Capped Hall is proved for the product obstruction, for every cloud

Now add an arbitrary `T`-point cloud in the common apex neighbourhood.  Its
internal order type is unrestricted.  Every cloud point hides all internal
source vertices, so it is an exterior blocker for every source.  There are

\[
 |\mathcal S|=M^{r-2},\qquad
 n=(r-2)M+2+T.                                     \tag{9}
\]

The previous report took `T=M`.  The following removes that restriction and
uses only the capped demand (1).

> **Theorem 4 (complete product-obstruction discharge).**  Put `M=2^r`.
> For all sufficiently large `r`, for every `T>=1` and every order type of
> the apex cloud, the configuration in (9) satisfies
> \[
>  \boxed{V(P)\ge D_r|\mathcal S|}.                \tag{10}
> \]

**Proof.**  First suppose `T<=M^3/64`.  Since
`2^ceil(log n)<=2n`,

\[
 D_r\le {2n\over M}
      \le 2r+{M^2\over32}+{4\over M}.             \tag{11}
\]

For `r>=6`, the last expression is at most `(M-1)^2/4`.  Dividing (8) by
`|S|=M^(r-2)` gives exactly

\[
 {\binom M2^2M^{r-4}\over |\mathcal S|}
 ={(M-1)^2\over4},                                \tag{12}
\]

so the rank-`r` two-ended faces alone prove (10).

Now suppose `T>M^3/64` and put `t=log T`.  Then `t>=3r-6`.  The blocker
cloud is a subconfiguration of `P`.  The established universal
Erdos--Szekeres double-counting bound gives

\[
 \log V(P)\ge\log V(X)
 \ge {t^2\over4}-o(t^2).                          \tag{13}
\]

In this range `n<=2T` for large `r`, hence

\[
 \log(D_r|\mathcal S|)
 \le t-r+2+r(r-2)
 =r^2-3r+t+2.                                     \tag{14}
\]

For `t>=3r-6`, the difference between the main term in (13) and (14) is
at least

\[
 {5\over4}r^2-O(r).                               \tag{15}
\]

It absorbs the lower-order error in (13), proving (10).  QED.

The threshold `M^3` is not mysterious.  The blocker demand contributes
roughly `T/M` labels per source, while the elementary two-ended pool gives
an `M^2` multiplier.  Exactly when `T/M` outgrows `M^2`, the cloud has
`log T about 3r`, and its coefficient-`1/4` lower bound is already of order
`9r^2/4`, far above the source entropy `r^2`.

Thus the product family is not merely non-counterexample for the originally
tested `T=M`; it is discharged for every cloud size, without any assumption
on the cloud order type.  This is concrete evidence for the proposed
two-ended-or-recurse strategy.

## 5. What remains

The exact local skeleton is now:

1. cap every source at `D_r` selected exterior blockers;
2. apply Lemma 2 with a batch threshold such as `sqrt(r)`;
3. in the concentrated case, enter the common rooted tangent pocket;
4. in the dispersed case, charge source entropy to a forward two-ended pool,
   as Theorem 3 does exactly for a product cell.

Steps 1--3 are locally rigorous.  Step 4 is the remaining global theorem.
The counterexample (4) shows why it cannot be replaced by a bounded-fibre
claim for the simultaneous repaired hull.  Theorem 3 suggests the right
recursive state: one must retain two oriented endpoint partition functions
(cap credit on the left and cup credit on the right), not just a root edge
and a Boolean batch word.  The unresolved assertion is an amortized
forward-alignment inequality across arbitrary overlapping rooted pockets.

A plausible batching target is to show that every `sqrt(r)` consecutive
rooted descents either release a two-ended face pool of the form (5), or
reduce the active source rank by `sqrt(r)`.  Endpoint naming would then cost
only `2^O(sqrt(r) log r)=2^o(r)`.  The present work validates the scale and
the local alternatives, but does not prove the required global
forward-alignment/telescoping statement.

### 5.1 The batching statement needs a weight correction

There is an important sign issue in the preceding informal target.  A rank
drop by itself is not progress for capped Hall.  If a family `G` of active
rank-`m` histories is projected to a family `H` of rank `m-s`, with maximum
projection fibre `F`, then

\[
 2^{\ell-m}|G|
 \le F2^{-s}\,2^{\ell-(m-s)}|H|.                  \tag{16}
\]

Thus the descent is usable with loss `K` if and only if

\[
 F\le K2^s.                                       \tag{17}
\]

The new rank has a `2^s` *larger* cap.  The only credit supplied by dropping
`s` vertices is permission for a fibre of size `2^s`, not an automatic
gain.  This is the correct weighted batching invariant.

The product regression in Section 2 violates (17) maximally.  Erasing `s`
independent microblock coordinates has fibre `(M-1)^s`, not `2^s`.  At
`M=2^r`, even `s=sqrt(r)` loses `2^{Theta(r^(3/2))}` histories.  The endpoint
record `2^O(sqrt(r)log r)` is negligible compared with this geometric
projection fibre.  Therefore the literal two-way statement

> "release a forward pool, or merely lower the active rank by `sqrt(r)`"

is false as a Hall-completion principle.  The second alternative must say
"lower the rank **and** prove (17)," or charge the excess `F/2^s` to a
two-ended/unrooted face pool.

This identifies the exact connection with the rooted marked-omission state.
For a rooted pocket `Q`,

\[
 D_Q=\sum_{C\text{ rooted}}(m-|C|)2^{-|C|}         \tag{18}
\]

is precisely the aggregate of the normalized fibres in (16).  The proposed
inequality `D_Q<=V(Q)` proves (17) after summing within one fixed frame.  Its
multi-frame Hall strengthening `(RPH)` is exactly what is needed when the
same pocket faces are reused by many boundary frames.  In other words, a
rank-only batch potential cannot bypass `(MO)/(RPH)`; (18) is the correct
scalar state before global overlap is addressed.

### 5.2 The exact forward potential, and the anti-alignment test

For an ordered sequence of vertical pockets, Theorem 3 has a minimal
two-scalar scan.  Define

\[
 P_1=C(Q_1),\quad F_1=0,
\]

and for `j>=2`

\[
 \boxed{
 P_j=C(Q_j)+m_jP_{j-1},\qquad
 F_j=F_{j-1}+P_{j-1}U(Q_j).}                       \tag{19}
\]

Then `F_b` is exactly the sum in (6).  The first coordinate is left-cap
credit transported through singleton middle choices; the second spends it
only when a right cup appears.  Formula (19), or its rooted QuickHull
analogue, is the smallest plausible forward two-ended potential.  Replacing
it by unordered cap/cup marginals is invalid.

Indeed, take cup-heavy pockets first and cap-heavy pockets last.  The large
cup mass is then to the **left** of the large cap mass, while (19) can spend
only cap-left/cup-right credit.  The forward cross terms can be exponentially
smaller than the reverse ones.  This is a valid vertical order type, not an
abstract sequence.  A correct batch theorem must therefore have a third
payment mechanism: a pocket whose large endpoint mass is stranded in the
wrong orientation must pay through its own unrooted face count, or be
entered recursively with that orientation flag retained.  The state cannot
be only `(active rank, root edge)`.

This is also a reduction barrier.  In a homogeneous cell the full-span term
is `C(Q)U(Q)M^(b-2)`.  Any universal quantitative assertion that this term
is always large enough, without a recursive/unrooted alternative, contains
as its two-block case the still-open cap--cup product problem for an
arbitrary planar order type `Q`.  The product obstruction is solved by the
elementary pair slice because its capped demand is smaller; the general
batch cannot silently assume the stronger endpoint product conjecture.

## 6. Exact tangent types on a fixed root chord

The forward orientation has a completely local description for two rooted
chains on opposite sides of a fixed chord.  Normalize the roots to

\[
 u=(0,0),\qquad v=(1,0).
\]

Let `A` be a rooted convex chain above `uv` and `B` one below it.  Denote by
`a_u,a_v` the neighbors of the two roots on the non-`uv` boundary arc of
`{u,v} union A`, and define `b_u,b_v` similarly.  Put

\[
 L_A={x(a_u)\over y(a_u)},\quad
 R_A={x(a_v)-1\over y(a_v)},
 \qquad
 L_B={x(b_u)\over y(b_u)},\quad
 R_B={x(b_v)-1\over y(b_v)}.                     \tag{20}
\]

> **Lemma 5 (two-root tangent criterion).**
> \[
> \boxed{
>  \{u,v\}\cup A\cup B\text{ is convex}
>  \quad\Longleftrightarrow\quad
>  L_A>L_B\ \text{ and }\ R_A<R_B.}              \tag{21}
> \]

**Proof.**  Concatenate the upper and lower boundary arcs.  They lie in
opposite open half-planes of `uv`, so the resulting polygonal boundary is
simple.  Every turn except the two root turns is inherited from one of the
two rooted convex polygons.  The remaining conditions are exactly

\[
 \operatorname{orient}(a_u,u,b_u)>0,qquad
 \operatorname{orient}(b_v,v,a_v)>0.              \tag{22}
\]

Since `y(a)>0>y(b)`, the first determinant has the required sign exactly
when `L_A>L_B`, and the second exactly when `R_A<R_B`.  A simple polygon
with all strict turns positive is convex, proving both directions. `QED`

Thus fixed-root compatibility is southeast dominance in a two-dimensional
tangent-type poset.  This is the precise rooted analogue of the forward
cap--cup product.  It also gives a cheap way to localize every failure.

> **Lemma 6 (dyadic tangent-failure decomposition).**  Give two finite
> families of opposite rooted chains arbitrary nonnegative weights, and
> rank all tangent-neighbor rays at one root in their strict angular order.
> If the rank set has size at most `n`, the weighted set of pairs which fail
> that root condition is a disjoint union over at most
> `ceil(log_2 n)` levels.  At each level it is a union of disjoint separated
> rank rectangles.  Consequently one level carries at least a
> `1/ceil(log_2 n)` fraction of the failed-pair weight.

**Proof.**  Pad the ranks to the leaves of a complete binary interval tree.
Assign a failed ordered pair `a<b` to the lowest common ancestor of its two
leaves.  It then lies in the product of the left and right child intervals
of that node.  This assignment is unique.  Nodes at one depth have disjoint
leaf intervals, and there are only `ceil(log_2 n)` depths.  Sum the product
weights and pigeonhole over the depths. `QED`

Apply Lemma 6 first to pairs failing the `u` inequality in (21), and then to
the remaining incompatible pairs, which fail the `v` inequality.  We obtain
the rigorous local trichotomy

\[
 \boxed{\text{compatible full-root pool}\quad\text{or}\quad
        \text{one dyadic level of uniformly `u`-bad rectangles}
        \quad\text{or}\quad
        \text{one such `v`-bad level}.}            \tag{23}
\]

Choosing the endpoint and level costs only `O(log log n)=O(log r)` bits at
the critical scale.  Over `sqrt(r)` batched descents this is
`O(sqrt(r)log r)=o(r)`, exactly the acceptable endpoint-state loss.  Unlike
fixing the two tangent-neighbor names, it does not cost `Theta(r)` bits per
descent.

There is, however, no free target theorem inside a bad rectangle.  Both
endpoint inequalities in (21) can fail simultaneously, and deleting one or
both roots need not repair the union.  An exact integer example is

\[
 u=(0,0),\ v=(1,0),\quad A=\{(-7,5)\},
\]

\[
 B=\{(-4,-2),(5,-3),(7,-3),(-3,-1)\}.             \tag{24}
\]

Both rooted sets are convex with root edge `uv`; their two cross-root turns
are `-22` and `-6`.  The union has five non-root points but hull size four,
and after adjoining `u`, `v`, or both its hull still has size four.  Thus the
next statement really must be a weighted root descent or an unrooted-face
charge.  It cannot say merely "delete the bad root."

## 7. The scalar `F+W` Bellman is still insufficient

The global cap does kill every presently known realizable anti-alignment,
but it does not turn the existing scalar inequalities into a proof.  Here is
an exact max-plus countercycle showing the missing strength.

Write

\[
 x_i=\log m_i,\quad c_i=\log C(Q_i),\quad
 u_i=\log U(Q_i),\quad w_i=\log W(Q_i).            \tag{25}
\]

The scalar information currently available, after harmless constant
rounding, is

\[
 c_i,u_i\ge2x_i,qquad w_i\ge c_i,u_i,qquad
 c_i+u_i\ge w_i,qquad w_i\ge{x_i^2\over4}.       \tag{26}
\]

For a product source word the max-plus forward capacity is

\[
 H=\max\left\{\max_iw_i,
 \max_{i<j}\left(c_i+u_j+\sum_{i<q<j}x_q\right)\right\}.       \tag{27}
\]

Fix `a=16`, let `M=a2^s`, `t=M/4`, and `H_0=M^2/4`.  Take the block-log
sequence

\[
 a,2a,\ldots,M/2,
 \underbrace{M,\ldots,M}_{t-2\text{ times}},
 M/2,\ldots,2a,a.                                \tag{28}
\]

On the increasing tail put

\[
 w=x^2/4,\quad c=2x,\quad u=w-2x,                 \tag{29}
\]

and use the reflected state on the decreasing tail.  On plateau position
`j=1,...,t-2`, put

\[
 w=H_0,\qquad
 c_j=\begin{cases}2M,&j=1,\\jM,&j\ge2,\end{cases}
 \qquad u_j=H_0-c_j.                              \tag{30}
\]

All inequalities (26) hold.  A direct case split gives

\[
 \max_{i<j}\left(c_i+u_j+\sum_{i<q<j}x_q\right)=H_0.          \tag{31}
\]

For completeness, within the increasing tail the expression is
`x_j^2/4-x_j`; the decreasing tail is its mirror.  Across the central
region, subtracting the entropy outside `[i,j]` shows that each normalized
left and right endpoint credit is at most `a`, while the total source
entropy is `H_0-2a`.  Equality in (31) is attained.

The number of blocks and the source entropy are

\[
 b=t-2+2s,qquad X:=\sum_i x_i=H_0-2a.            \tag{32}
\]

Since the ambient logarithm is at least `M`, capped Hall asks already for
exponent

\[
 X+M-b=H_0+(M-b-2a).                              \tag{33}
\]

The parenthesized gap is `(3/4-o(1))M>0`, while both the local and forward
parts of (27) equal only `H_0`.  Therefore:

> **Proposition 7 (sharp scalar barrier).**  No Bellman theorem using only
> (26) and the exact forward scan (27) can prove capped Hall even with an
> `n^{o(1)}` loss.  It misses the explicit profiles (28)--(30) by
> `2^{Theta(M)}`.

This is deliberately **not** claimed to be a realizable planar
counterconstruction.  Realizing it would require a long continuum of
near-quarter pockets whose cap exponent rises at exactly the rate at which
middle entropy is accumulated.  No known family has that profile.  The
point is a proof barrier: the global cap must be used geometrically in the
uniformly bad tangent rectangles from (23), rather than only through the
quarter-exponent scalar lower bound.

The standard obstruction families support this diagnosis.

* If an all-cup `m`-block precedes an all-cap block, with
  `D=m+binom(m,2)` and `E=2^m-1`, then
  \[
     W=2E+D^2,
  \]
  while the reverse order has `W=2E+E^2`.  This is a fully realizable
  exponential forward/reverse gap, but even the bad order has local mass
  `Theta(2^m)`, far above a total-`W` cap at logarithmic block scale.
* Balanced Pascal and guarded fixed-template towers have local
  `log W=(1/2-o(1))(log m)^2`, not the quarter profile in (29)--(30), so a
  single block pays by a quadratic margin.  The canonical skew Pascal cells
  are separately paid by the transversal/local alternative audited in the
  upper-jump lane.
* The actual common-apex product grid is paid at capped scale by the
  elementary pair-pair pool (8), independently of its cloud order type.

Thus there is no realizable countercycle to capped Hall here.  What is now
sharp is the remaining positive statement: after the `O(log r)` tangent
localization (23), every uniformly bad rectangle must either admit a
weighted rooted descent satisfying (17), or charge its excess fibre to
ordinary faces.  This is the tangent-ordered form of `(RPH)`.

### 7.1 A whole `sqrt(r)` prefix is harmless for one terminal child

The ordered-array recursion in the ACP lane makes a bad marginal pair
canonical: one endpoint is nested in the rooted triangle of the other.  It
may remain nested after many consecutive boundary vertices are peeled.  A
fixed descent path of length `s` discards a consecutive prefix `D` of one
original convex source boundary.  Consequently every subset of `D` is an
ordinary convex face.  This Boolean fact is pointwise exact, but its cubes
can overlap across paths.

There is nevertheless a useful complete bound after fixing the terminal
child.  Let `mathcal D` be the distinct discarded prefixes which reach one
fixed child.  Let `Y` contain their vertices together with all selected
next nested alternatives above them.  Put

\[
 S=|\mathcal D|,\qquad q=|Y|.                                                \tag{34}
\]

and select at most `d` next nested alternatives above each prefix.  Let `e`
be the total selected mass.  Trivially

\[
 e\le S\min\{d,q\}.                              \tag{35}
\]

Every `D` is an ordinary convex face, so `V(P)>=S`.  Also `Y subset P`, and
for every fixed `c<1/4` the established Erdős--Szekeres lower bound gives,
for all sufficiently large `q`,

\[
 V(P)\ge V(Y)\ge2^{c(\log q)^2}.                  \tag{36}
\]

Writing `k=log S` and `y=log q`, (35)--(36) imply

\[
 \log^+{e\over V(P)}
 \le \min\{y,k+y-cy^2\}
 \le \sqrt{k/c}+O_c(1).                          \tag{37}
\]

The last inequality follows by splitting at `y=sqrt(k/c)`; above that
point the quadratic expression is decreasing, apart from a bounded initial
range.  We have proved:

> **Proposition 8 (fixed-child prefix discharge).**
> \[
> \boxed{e\le2^{O(\sqrt{\log S})}V(P).}            \tag{38}
> \]
> If every prefix has length at most `s`, then
> `S<=sum_(j<=s)binom(n,j)<=n^(s+1)`, and hence
> \[
> e\le2^{O(\sqrt{s\log n})}V(P).                  \tag{39}
> \]

At `s=ceil(sqrt(r))` and `log n=Theta(r)`, the loss in (39) is
`2^{O(r^(3/4))}=2^{o(r)}`.  Thus an arbitrarily long rank-one obstruction
inside one batch is not itself the final gate.  The parabolic prefix example
from the ACP lane is paid exactly as (38) predicts.

What prevents summing (38) over all terminal children is now completely
explicit.  For each child `C`, write `Y_C` for its prefix cloud and define

\[
 \mu=\max_{\varnothing\ne X\in F(P)}
       |\{C:X\subseteq Y_C\}|.                    \tag{40}
\]

If `mu=2^{o(r)}`, summing the proof of (38) gives the desired capped
allocation.  Indeed the local proof gives
`e_C<=2^{O(r^(3/4))}(S_C+V(Y_C))`; every nonempty discarded prefix counted
by `S_C` is itself a face of `Y_C`, and

\[
 \sum_CV(Y_C)\le\mu V(P).                        \tag{41}
\]

Therefore a surviving counterfamily must reuse the same ordinary convex
prefix faces in `2^{Omega(r)}` different terminal children.  This is much
sharper than saying merely that child pockets overlap.

The high-multiplicity case cannot be removed by replacing ordinary cloud
faces with boundary-completed faces.  A one-sided all-cup cloud may have
`2^q` ordinary faces while an anti-aligned fixed child accepts only its
small endpoint-cap subfamily.  This is the same realizable
all-cup--all-cap obstruction as above.  Conversely, independent product
prefixes show that the visible Boolean cubes alone can collapse from
`2^sM^s` path units to only `(M+1)^s` distinct subsets.  In the actual
product geometry the neighbouring forward endpoint rectangles pay the
deficit.

Hence the remaining global statement can be isolated as follows:

> **Prefix-cloud reuse gate.**  If `mu` in (40) is exponential, the family
> of terminal children reusing that cloud must either supply, through the
> opposite ordered-array marginal, enough forward two-ended rectangles to
> pay the repeated `V(Y_C)` credit, or pay through the ordinary convex-face
> mass of the child family itself.

This is exactly where the dyadic tangent trichotomy and `(OAI)` meet.  A
proof of the reuse gate would close `sqrt(r)` batches: low multiplicity is
handled by (39)--(41), while high multiplicity is forced back into a forward
array or a child-side unrooted pool rather than another unrecorded scalar
descent.

### 7.2 Nested pairs form a monotone exposure filtration

There is one further exact piece of the desired potential.  Fix one retained
boundary path and peel its vertices in their boundary order, writing `R_j`
for the retained suffix after `j` peels.  For two endpoint alternatives
`a,A`, define

\[
 t(a,A)=\min\{j:R_j\cup\{a,A\}\text{ is convex}\}.              \tag{42}
\]

This threshold always exists if the peeling is continued through the whole
complementary boundary.  More importantly, forwardness is monotone:

\[
 R_j\cup\{a,A\}\in F(P)
 \quad\Longrightarrow\quad
 R_{j+1}\cup\{a,A\}\in F(P),                    \tag{43}
\]

simply because the latter is a subset of the former.  Thus a candidate
cloud `Y` carries an increasing graph filtration

\[
 F_0\subseteq F_1\subseteq\cdots\subseteq F_r=\binom Y2,       \tag{44}
\]

where an edge enters at its exposure depth.  In particular some depth
releases at least `binom(|Y|,2)/(r+1)` new forward pairs.

The parabolic nested-prefix example shows that all release may occur at the
last depth, so the unweighted pigeonhole in (44) does not close Hall: the
target then forgets the whole prefix, and the opposite ordered-array
marginal must be forward at the same state.  Nevertheless (44) rules out a
genuine cyclic trap.  Every nested pair is delayed forward credit, not lost
credit.  A successful global potential should combine its natural
threshold weight `2^(-t(a,A))` with the Boolean prefix capacity and the
opposite-marginal rectangle count.  The sole obstruction to summing that
potential is again the reuse quantified in (40).

### 7.3 An exact threshold-weighted Bellman inequality

The suggested threshold weight does satisfy a clean per-state inequality.
It is useful to state it first without geometry.

> **Lemma 9 (weighted exposure AM--GM).**  Let
> `0<=alpha_i<=1`, let `t_(ij)` be integers in `[0,s]`, and put
> `z=sum_i alpha_i`.  Then
> \[
>  \boxed{
>  z\le2^s+\sum_{i<j}\alpha_i\alpha_j2^{-t_{ij}}.}              \tag{45}
> \]

**Proof.**  Put `A=2^s`.  If `z<=A`, the first term pays.  Otherwise,
among vectors in `[0,1]^q` with fixed sum `z`, the pair sum
`sum_(i<j)alpha_i alpha_j` is minimized by filling coordinates with ones,
then at most one fractional coordinate.  For `z>A` this minimum is at least
`A(z-A)`.  Since every `t_(ij)<=s`, the second term in (45) is at least
`A^(-1)sum_(i<j)alpha_i alpha_j>=z-A`. `QED`

Now return to one ordered-array marginal.  Let `G subset A times B` be its
support graph, put `m=|E(G)|`, let `w_a=d_G(a)`, and let
`Delta_A=max_a w_a`.  Give each left endpoint pair an exposure depth
`t(a,a')<=s`.  Scaling (45) by `Delta_A` gives

\[
 \boxed{
 m\le2^s\Delta_A+{1\over\Delta_A}
       \sum_{a<a'}w_aw_{a'}2^{-t(a,a')}.}          \tag{46}
\]

This has exactly the desired interpretation.  The first term is the
`2^s` Boolean prefix cube over a maximum-degree endpoint fibre, or
equivalently that fibre sent to its depth-`s` child with the cap multiplied
by `2^s`.  The second term is delayed forward-pair credit with precisely the
inverse cap multiplier at its exposure depth.

There is one graph correction: `w_aw_(a')` also counts the pairs of support
edges sharing their right endpoint.  Let

\[
 P_A=\sum_{a<a'}
   |\{(ab,a'b'):b\ne b'\}|\,2^{-t(a,a')}          \tag{47}
\]

be the genuinely disjoint weighted pair mass.  The omitted corner mass is
at most

\[
 \sum_b\binom{d_G(b)}2\le {m(\Delta_B-1)\over2}. \tag{48}
\]

Choose the marginal with `Delta_A>=Delta_B`.  Substitution in (46) yields

\[
 \boxed{
 m\le2^{s+1}\Delta_A+{2P_A\over\Delta_A}.}        \tag{49}
\]

This is a rigorous threshold-weighted version of the ordered-array
dichotomy.  If the opposite endpoint pair of every disjoint edge pair is
already forward, the second term is represented by genuine two-ended
targets.  Their within-state fibre is at most two, and their global recovery
fibre is polynomial by the ordered-array target decoder.  Grouping by
exposure depth, the factor `2^{-t}` is exactly the cap-doubling discount.

In the unrestricted array, (49) is a one-marginal Bellman step: `P_A` must
be passed to the analogous right-marginal filtration when its right pair is
nested.  Thus (49) closes the fully forward case and proves that there is no
additional scalar loss from heterogeneous exposure depths.  What it does
**not** prove is bounded global recovery for the first term.  The targets in
one maximum-degree prefix cube are distinct, but omitted prefix labels are
invisible across different outer states.  The exact product-prefix
regression has fibre `M^s` and Boolean union only `(M+1)^s`; hence any claim
that the first terms of (49) sum with polynomial overlap is false.

The viable global statement is consequently very narrow: sum (49) while
retaining its `2^{-t}` forward credit, and whenever the Boolean first term
has high global reuse, invoke Proposition 8 or the child-side unrooted pool
in the prefix-cloud reuse gate.  No stronger pointwise Bellman inequality is
needed, and no weaker recovery assertion can survive the product regression.

### 7.4 What the crude full-batch decoder can and cannot prove

There is a conditional global consequence once the reuse of one *full*
prefix face is sufficiently large.  Auditing its parameter range exposes
an important obstruction to using it as the desired closure.

Let `mathcal X` be a family of full prefix faces of size at most `s`.  For
each `X`, encode its `M_X` terminal children by words of length `b` in
tangent-ordered coordinate pools `Q_i`.  Put

\[
 B=1+\sum_i(|Q_i|-1)\le n+1.                     \tag{50}
\]

The split-sequence theorem in the ACP lane says that the forward graph on
one word family has at least

\[
 F_X\ge {M_X\over2}\left({M_X\over B}-1\right). \tag{51}
\]

Suppose we use the canonical first forward interval.  A deliberately crude
global decoder for its target guesses the interval, the prefix face `X`,
and every word coordinate which the target forgets.  Even if it must guess
two complete outside words, its fibre is at most

\[
 K_{\rm rec}=2b^2(s+1)n^{2b+s}.                  \tag{52}
\]

The factor two orders the pair, `b^2` chooses its interval, there are at
most `(s+1)n^s` possible prefix faces, and the two outside words cost at
most `n^(2b)`.  The actual rooted decoder is better; (52) is recorded
because it requires no product or independence assumption.

Let each child carry at most `d` selected continuations.  For any collection
`mathcal H` of prefix rows satisfying

\[
 M_X\ge K_0:=4dB K_{\rm rec},                    \tag{53}
\]

(51) gives `F_X>=M_X^2/(4B)`, and bounded recovery gives

\[
 |\{\hbox{distinct forward targets from }\mathcal H\}|
 \ge {1\over K_{\rm rec}}\sum_{X\in\mathcal H}F_X
 \ge d\sum_{X\in\mathcal H}M_X.                 \tag{54}
\]

Thus any row which really satisfies (53) is paid, even after target
collisions across different prefixes.  At batch length
`b,s<=ceil(sqrt(r))`, with `log n=Theta(r)` and `log d=O(r)`,

\[
                     \log K_0=O(r^{3/2})=o(r^2). \tag{55}
\]

However, (53) is **vacuous** if the length-`b` point word uniquely encodes
the terminal child.  Indeed

\[
 M_X\le\prod_i|Q_i|\le n^b,
 \qquad K_0>n^{2b+s}>n^b.                         \tag{56}
\]

If instead quadratically many terminal cores can carry the same batch word,
then those copies are not distinct vertices of the split-sequence graph and
create no new forward pairs.  Encoding the cores as extra coordinates makes
`b=Theta(r)` (or enlarges the alphabets), and the decoder in (52) again has
quadratic entropy.  Therefore (54) is a correct conditional estimate but
does not by itself discharge a quadratic terminal-child family.  This is
the exact distinction between a length-`sqrt(r)` left/right **type word**
and a full word which identifies the retained core.

There remains a genuine summation obstruction below (53).  The fixed-prefix
source-cloud theorem says that one row with `log M_X=o(r^2)` is harmless,
but every such row is bounded using the same global number `V(P)`.  Summing
that estimate over `H` distinct prefixes can therefore lose a factor `H`.
Equivalently, the elementary estimate on the residual rows is only

\[
 d\sum_{X\notin\mathcal H}M_X
 \le dK_0|\mathcal X|\le dK_0V(P),               \tag{57}
\]

whose loss is `2^{Theta(r^(3/2))}`, not `2^{o(r)}`.  Common-pocket examples
show that one cannot erase this factor by asserting bounded overlap of
ordinary child faces.

Consequently the last gate is now bipartite rather than one-row: a large
family of medium prefix rows reusing essentially the same terminal-child
cloud.  It must be charged by the *prefix-side* split sequence or by the
ordinary convex mass of that prefix family.  Equation (49) closes
heterogeneous exposure depths, but a symmetric two-marginal cancellation or
all-interval recovery theorem is still required.  Treating the fixed-prefix
theorem as summable, or conflating the batch type word with the full child
signature, would be an invalid proof.

### 7.5 Even a common suffix cannot be retained in a forward target

One possible way around the decoder loss would be to choose the first cap
coordinate and the last later cup coordinate.  The comparison suffix then
has no further reversal.  Unfortunately, even an *equal* suffix cannot in
general remain in the same convex target.

The vertical product gives an exact five-point regression.  In three
successive blocks take

\[
 p_1=(1,22),\quad p_2=(1025/1024,705/32),
\]

\[
 q_1=(2,42),\quad q_2=(2049/1024,1345/32),
 \qquad z=(3,60).                                 \tag{58}
\]

The interval target `{p_1,p_2,q_1,q_2}` is convex.  But after retaining the
single common suffix coordinate `z`, its hull is

\[
             \{p_1,p_2,q_2,z\}.                  \tag{59}
\]

The point `q_1` is hidden.  Structurally, the two-point cup in the `q` block
was convex because that block was the last occupied block.  Adding any
later point makes it an intermediate occupied block, while the exact
vertical-composition classification permits only one point in every
intermediate block.

Thus monotonicity of the comparison suffix does not make it retainable;
the forward interval target really does forget outside coordinates.  This
also shows why a polynomial decoder cannot be recovered merely by a
canonical first/last inversion rule.  The missing result has to sum over
all intervals with prefix/ordinary-face credit, rather than put the entire
signature into one convex target.

### 7.6 A sharp countercycle to naive global weighted projection

The product-prefix regression also kills the most direct globalization of
Lemma 9.  Take all `N=M^s` words which choose one of `M` labels in each of
`s` discarded coordinates.  Let them reach one common terminal child, and
let a common set of `q=M` alternative labels become exposed only at depth
`s`.  If histories are projected away, the union of their Boolean prefix
cubes has exactly `(M+1)^s` visible partial words, while the unique delayed
pair pool has threshold-weighted capacity only

\[
                         2^{-s}\binom M2.          \tag{60}
\]

On the other hand the selected source--alternative mass is

\[
                         Nq=M^{s+1}.              \tag{61}
\]

Consequently

\[
 {M^{s+1}\over (M+1)^s+2^{-s}\binom M2}
                         =M^{1-o(1)}              \tag{62}
\]

when `M=2^r` and `s=ceil(sqrt(r))`.  Therefore no global theorem can simply
add the **distinct** Boolean prefix faces to the **distinct**
threshold-weighted terminal pairs.  The missing factor is a full cap at the
critical scale.

This is a counterexample to that proposed projection inequality, not to
capped Hall.  The vertical product geometry realizes the prefix collapse
but also contains the all-interval two-ended faces (5)--(8), which are
precisely the capacity omitted by (60).  Any successful exposure potential
must retain an interval or outside signature long enough to count those
faces; the terminal pair alone is insufficient.

## 8. Verification

Run from the repository root:

```bash
python3 phase2/loop/erdos838/agent_two_ended_hall/two_ended_hall_audit.py
python3 phase2/loop/erdos838/agent_two_ended_hall/forward_bellman_audit.py
```

The script writes `certificate.json`.  It checks, with exact rational
orientation predicates:

* the full count `C(Q)U(Q)M^(r-4)` in a finite vertical cell;
* all rank-`r` pair-pair faces in (8);
* the exact common-suffix retention failure (58)--(59);
* pairwise disjoint violated support windows for a simultaneous batch;
* the full Boolean target cube for one source;
* the exponential common-target fibre in (4); and
* exact capped-demand arithmetic below `M^3/64`, together with the quadratic
  quarter-exponent margin above that threshold for `r=16,24,32,48,64`.

The second script writes `forward_bellman_certificate.json`.  It checks the
integer determinant criterion (21), the both-bad regression (24), an exact
weighted dyadic-LCA partition, the all-cup/all-cap order gap, and five
instances of the scalable abstract countercycle through `M=2048`.  It also
audits the `sqrt(r)` fixed-child loss in (39) and the exact `(M+1)^s`
Boolean-prefix collapse.  Finally it checks Lemma 9 on 292,950 rational
weight/depth instances and (46), (49) on every nonempty `3 by 3` support
graph at depths zero through three.  It also audits the high-row decoder's
vacuity for point words and the weighted projection gap (60)--(62).
