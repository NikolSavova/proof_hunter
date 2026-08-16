# The all-loop wrapper is an exact strong glue, but arbitrary recharting breaks the recursive half theorem

**Date:** 2026-08-15.  Counts below are nonempty unless an empty set is
explicitly added, and all logarithms are base two.

## Verdict

The cap--blocker all-loop regression has an exact and useful description.
Its blocker arc and local arc are two pure-cap combs, and the whole wrapper
is one binary strong glue of those combs.  Consequently arbitrary
multi-point projective children have an **exact** `C,U,W` recurrence; no
multi-cluster face is omitted.

This observation gives a genuine coefficient-half theorem only for a
**compatible chamber itinerary**: if every recursive child is inserted in
a projection chamber in which its previous ordered strong decomposition is
still visible, the completed construction is an ordered strong-decomposition
tree.  `agent_asymptotic/NEXT_ENDPOINT_ATTACK.md`, Theorem (weighted
one-turn alignment), then gives

\[
 \log W(P)\ge {1\over2}(\log |P|)^2-O((\log |P|)^{3/2}).       \tag{1}
\]

Arbitrary recharting is not covered by (1).  In fact it is not prevented by
the common guard: every generic projection chamber of an arbitrary child
can be rationally sheared and nested behind the next guard while preserving
its order type.  The exact six-point Pascal cell `T(4,2)` has 26 projection
chambers, but only two admit *any* ordered strong-decomposition tree.  A bad
one can nevertheless be put behind a fresh exact strong seam, and the
resulting seven-point ordered configuration still admits no ordered strong
tree.  Thus applying (1) after an arbitrary reset is a real logical error,
not a missing coordinate normalization.

The recursive quarter-ramp question is therefore reduced to a sharper
object: the **two-direction projection-profile spectrum** of a completed
wrapper.  The scalar one-chart ramp is exactly realizable whenever its
children exist, but it does not show that a wrapper built from a fixed seed
has a second chamber with the low endpoint energy needed to repeat the
ramp.  The first exact 14-point audit goes the opposite way.  Closing this
two-direction gate, rather than the one-chart recurrence, is the remaining
load-bearing task.

## 1. Exact two-arc recurrence

For an ordered planar set `Q`, write `n(Q)=|Q|` and let `C(Q),U(Q),W(Q)`
denote its nonempty cap, cup, and ordinary-face counts in the displayed
chart.  For a strong glue `A prec B`, with `a=|A|, b=|B|`, the exact
identities are

\[
\begin{aligned}
 C(A\prec B)&=C(B)+(b+1)C(A),\\
 U(A\prec B)&=U(A)+(a+1)U(B),\\
 W(A\prec B)&=W(A)+W(B)+C(A)U(B).                \tag{2}
\end{aligned}
\]

The last identity includes every multi-point trace.  A spanning ordinary
face is uniquely a cap in `A` together with a cup in `B`; conversely every
such pair is ordinary.

Let

\[
        \mathcal A(Q_1,\ldots,Q_s)
          =(((Q_1\prec Q_2)\prec Q_3)\cdots\prec Q_s)          \tag{3}
\]

be a pure-cap comb of arbitrary child blocks.  Iterating (2) gives

\[
\boxed{
\begin{aligned}
C(\mathcal A)&=
 \sum_{i=1}^s C_i\prod_{i<h\le s}(1+n_h),\\
U(\mathcal A)&=
 \sum_{j=1}^s\left(1+\sum_{i<j}n_i\right)U_j,\\
W(\mathcal A)&=
 \sum_{i=1}^sW_i+
 \sum_{1\le i<j\le s}C_iU_j
       \prod_{i<h<j}(1+n_h).
                                                               \tag{4}
\end{aligned}}
\]

Now form a blocker arc `G=A(G_1,...,G_k)` and a local arc
`L=A(L_1,...,L_m)`, where `A` denotes the comb in (3), then make the
all-loop wrapper

\[
                         P=G\prec L.                           \tag{5}
\]

There is one more exact application of (2):

\[
\boxed{
\begin{aligned}
C(P)&=C(L)+(|L|+1)C(G),\\
U(P)&=U(G)+(|G|+1)U(L),\\
W(P)&=W(G)+W(L)+C(G)U(L).                       \tag{6}
\end{aligned}}
\]

Equations (4)--(6) are both an upper and a lower recurrence.  They remain
valid when every macro point is replaced by an arbitrary planar child in
an independently chosen projection chamber, provided the child is placed
by the exact strong-glue construction in that chart.

For singleton blocks, a length-`s` comb has

\[
 W=C=2^s-1,\qquad U=s+{s\choose2}.                       \tag{7}
\]

Therefore the number `V=W+1` of faces including the empty set in (5) is

\[
 \boxed{V(P)=2^m+\left(1+m+{m\choose2}\right)(2^k-1),} \tag{8}
\]

which is exactly the all-loop recurrence in
`BLOCKER_ROLE_HITTING_SET_BARRIER.md`.  Thus the earlier parabolic
regression is not merely analogous to a strong glue; it is the singleton
specialization of (4)--(6).

## 2. Any chosen child chamber can be used at the next level

The following elementary recharting lemma is the reason a rotated reset
cannot be dismissed geometrically.

> **Lemma 1 (exact chamber rechart).**  Let `Q` be a rational planar
> general-position set and let `f` be any rational generic linear
> functional on `Q`.  There is an orientation-preserving rational affine
> chart in which the `f`-order is the increasing x-order and every pair
> slope is positive.  In that chart `Q` can be used as either child of an
> exact rational strong glue.  It can also be fed into the common-edge
> nesting map without changing its order type.

Choose a linear functional `g` such that `(f,g)` is positively oriented.
Replacing `g` by `g+Kf`, for sufficiently large rational `K`, makes every
pair slope positive without changing the `f`-order or any orientation.
Positive diagonal normalization now puts the child into `[0,1]^2`.  The
explicit construction

\[
 A\mapsto (\varepsilon x,y),\qquad
 B\mapsto(1+\varepsilon x,2+y)                         \tag{9}
\]

with sufficiently small rational `epsilon` gives `A prec B` exactly.

For the common guard `u,v`, use the pocket map from
`COMMON_GUARD_PROFILE_RAMP_BARRIER.md` with

\[
 L=L_0+\delta f+\delta^2g,\qquad
 R=R_0+\delta f-\delta^2g.                             \tag{10}
\]

The first-order `f` term gives total guard nesting and the transverse term
preserves the child order type.  Again only finitely many strict rational
inequalities are required.  Hence any finite recursive itinerary of
prescribed child chambers and wrapper seams has a stretchable rational
realization.  What is not automatic is that the *completed parent* offers
the next desired low-energy chamber.

## 3. Exact failure of compatible-tree closure

Call an itinerary **compatible** if every child is inserted in a chamber
which carries its existing ordered strong-decomposition tree (allowing the
global reflected convention).  Expanding (3) and (5) then gives one
simultaneous ordered full binary strong-decomposition tree on all singleton
leaves.  The weighted one-turn alignment theorem quoted in (1) applies, so
no compatible recursive all-loop wrapper has coefficient below one half.

The word compatible is essential.  Consider the standard exact rational
Pascal cell

\[
                         Q=T(4,2),\qquad |Q|=6.           \tag{11}
\]

Enumerate every generic projection order by the critical values of
`x+t y`.  There are 26 orders over a half-turn (including reversals).  For
each order, run the interval recursion which accepts a split `I=I_L I_R`
exactly when

\[
 \chi(a_1,a_2,b)<0,qquad \chi(a,b_1,b_2)>0             \tag{12}
\]

for all appropriate points and both child intervals recursively accept.
Exactly two of the 26 orders accept.  Thus 24 chambers lose every ordered
strong tree, not merely the original labelled tree.

Choose one rejected chamber, apply Lemma 1, and glue the recharted six
points to a new singleton.  The top split satisfies (12) exactly, and its
`C,U,W` counts satisfy (2), but neither the six-point child nor the whole
seven-point order admits an ordered strong tree in the parent chart.  This
is a scalable mechanism--Lemma 1 works for every child--and it pinpoints why
`NEXT_ENDPOINT_ATTACK.md` cannot simply be invoked after an arbitrary
rotation.

This does **not** construct a sub-half family.  It proves only that the
known half theorem does not control the proposed reset operation.

## 4. The exact recursive state which remains

For an order type `Q`, define its one-direction profile spectrum

\[
 \Pi(Q)=\{(C_\xi(Q),U_\xi(Q)):\xi
                 \text{ is a generic projection chamber}\}.          \tag{13}
\]

The common-guard scalar ramp chooses one element of `Pi(Q_i)` independently
for each role and substitutes it into (4).  With equal block size
`A=2^L`, `q=(alpha+o(1))L`, where `alpha` is the normalized number of
roles, and

\[
 \log C_i=(t_i+s+o(1))L^2,\qquad
 \log U_i=(c-t_i-s+o(1))L^2,                            \tag{14}
\]

the forward terms in (4) all have exponent `c+o(1)`.  This is the exact
formal quarter ramp already audited in
`COMMON_GUARD_PROFILE_RAMP_BARRIER.md`.

To iterate from a fixed seed, however, one needs more than (13).  The child
is first viewed in an assembly direction and the completed parent is then
viewed in a reset direction.  The relevant state is therefore

\[
 \Pi_2(Q)=\{(C_\xi,U_\xi;C_\eta,U_\eta):
                         \xi\ne\eta\}.                    \tag{15}
\]

An invertible affine map acts projectively on the line of directions.  It
can send any prescribed ordered pair of distinct directions to any other
ordered pair.  Hence independently re-embedded copies can synchronize two
chosen entries of (15); nesting itself supplies no further obstruction.
But a one-direction profile word such as (14) says nothing about the second
entry of (15).

The first exact reset audit is
`agent_root_followup/COMMON_GUARD_ALL_DIRECTION_AUDIT.md`.  Its 14-point
wrapper has `W=1914` and, over all 174 projection chambers,

\[
 \min_\xi C_\xi U_\xi=549\cdot286=157014,
 \qquad \min_\xi\max(C_\xi,U_\xi)=412.                 \tag{16}
\]

Thus its endpoint energy does not reset to the 64 atomic transversals.
Equation (16) is only finite evidence.  A proof preventing the recursive
quarter ramp needs an all-scale inequality on (15), for example a
direction-uniform endpoint-energy gain for the actual common-guard
wrapper.  Conversely, a counterconstruction must specify and verify the
two-direction states (15) at every scale; the scalar values (14) alone are
not a recursive construction.

## 5. Imported primitive children

There is one unconditional inheritance statement, but it does not settle a
deep recharted recursion.  If a final `N`-point wrapper contains `h=N^{o(1)}`
primitive child blocks and subpolynomially many anchors, some child has size
at least `N^{1-o(1)}`.  Projective recharting does not change its ordinary
faces, so

\[
                         W(P)\ge\max_i W(Q_i).            \tag{17}
\]

Consequently a coefficient-half lower bound for every macroscopic imported
primitive is inherited by the wrapper.  A claimed sub-half construction
must therefore use either an already-sub-half primitive or a genuinely deep
reset recursion with many nonmacroscopic leaves.  The latter is precisely
why (17) cannot replace the two-direction analysis in Section 4.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_recharted_all_loop_wrapper_gate.py
```

Expected output:

```text
PASS: singleton wrapper n=11 V=746 C=280 U=141; heterogeneous wrapper n=13 profile=(378, 258, 1402); Pascal T(4,2) chambers=26 compatible=2; bad chamber profile=(31, 31) and exact top re-glue verified
```

The verifier uses exact `Fraction` arithmetic.  It exhausts all subsets in
both wrappers, checks (4)--(8) independently, enumerates all 26 projection
chambers of `T(4,2)`, runs the exact ordered-tree interval decoder, and
constructs the rational bad-chamber re-glue.
