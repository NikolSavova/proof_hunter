# Radial universal wrappers: the three-class face recurrence is false

**Date:** 2026-08-14.  All logarithms are base two.

## Verdict

The proposed radial wrapper classification

1. single-block faces;
2. two-block directional faces; and
3. transversals whenever at least three blocks are occupied

is geometrically false, even under the two properties intended to make it
work:

* every full transversal is convex; and
* the detached union of two distinct full transversals is nonconvex.

There is an eight-point rational example with four **equal two-point chain
blocks**.  All sixteen full transversals are convex, while the union of
every two distinct full transversals is nonconvex.  Nevertheless, after
one macro block is omitted, the two points of one chain and one point from
each of two other blocks form a convex `2+1+1` face.  Thus deleting a macro
guard changes the rooted profile exposed in a cluster.  Taking the common
child to be the two-point order type also meets the homogeneous-copy and
projective-universality requirements (the latter is vacuous in this
minimal order type).

The correct state is mask- and direction-dependent.  For every occupied
macro support `I`, the local face profile in block `i in I` depends on the
predecessor and successor of `i` *inside `I`*.  Projective universality can
preserve an arbitrary collection of such rooted profiles.  Hence no exact
full-face recurrence in the three scalar classes above exists.

This kills the proposed route to a sub-half construction.  A single wrapper
with `q=Theta(log m)` also cannot lower an existing coefficient-`1/2`
child, since one cluster is an induced copy and

\[
             V(\operatorname{Wrap}_q(Q_m))\ge V(Q_m),
             \qquad \log(qm)=\log m+o(\log m).               \tag{1}
\]

For indefinitely iterated wrappers, (1) alone is not a complete barrier;
the rooted mask recurrence must be controlled.  The false three-class
recurrence supplies no certified upper bound, so it proves neither a
sub-half construction nor an all-depth barrier.

## 1. Exact rational counterexample

Use four equal macro blocks

\[
 X_0=\{a,a'\},\quad X_1=\{b,b'\},\quad
 X_2=\{c,c'\},\quad X_3=\{d,d'\},                         \tag{2}
\]

with

\[
 \begin{aligned}
 a&=(-2,-2),&a'&=(-9/5,-3/2),\\
 b&=(2,-2),&b'&=(17/10,-9/5),\\
 c&=(2,2),&c'&=(9/5,17/10),\\
 d&=(-2,2),&d'&=(-17/10,9/5).
 \end{aligned}                                             \tag{3}
\]

All eight points are in general position.

> **Proposition 1 (guard-sensitive radial face).**  The configuration
> (2)--(3) satisfies:
>
> 1. all `2^4=16` full transversals are convex;
> 2. the union of every two distinct full transversals is nonconvex;
> 3. for each block `X_i`, its inner point lies strictly inside the
>    triangle formed by its outer point and **any** choice of one point
>    from each adjacent block; and
> 4. the four-set `a a' b c`, which meets three macro blocks and uses two
>    points in `X_0`, is convex.

**Proof.**  Exact monotone-hull evaluation over the sixteen choices proves
the first assertion.  For the third assertion, exact triangle-side tests
are strict for all four blocks and all four choices of the two neighboring
representatives.  Now two distinct transversals differ in some block.
Their union contains both points of that block and at least one point from
each adjacent block.  The inner point is strictly inside the triangle of
the other three, so the union is nonconvex.  Finally exact hull evaluation
gives the cyclic order `a,a',b,c` for the claimed four-face.  All
`C(8,3)` determinants are nonzero.  QED.

The example is exactly the local behavior of a radial insertion wrapper.
In each block the two members form a strict fixed-edge chain, either member
can replace the macro vertex, and the inner member is hidden when both
adjacent macro guards are present.  In `X_0`, removing the `d`-block
changes the right tangent from the `d` direction to the `c` direction and
releases both `a,a'`.

The complete convex-subset profile is

\[
 (v_0,\ldots,v_8)=(1,8,28,56,38,0,0,0,0),\qquad V=131.      \tag{5}
\]

More revealingly, every three-block support mask has twelve faces: its
eight transversals and four released `2+1+1` faces.  The full mask has only
the sixteen transversals.  Thus the profile of a block cannot be assigned
before the occupied macro mask is known.

This kills the proposed **full** scalar recurrence numerically, with no
ambiguity in its one- or two-block terms.  Every one-block mask has three
faces and every two-block mask has nine.  The claimed classification would
therefore give

\[
 V_{\rm claimed}=1+4\cdot3+\binom42 9+\binom43 2^3+2^4
                 =115,                                    \tag{5a}
\]

whereas the exact value is 131.  The discrepancy is precisely the four
extra `2+1+1` faces on each of the four three-block masks.

## 2. Why the detached-pair hypothesis is insufficient

Let a full transversal choose one point from every macro block.  If the
union of any two distinct full transversals is nonconvex, then a convex
face which meets **every** block indeed uses at most one point per block:
otherwise it contains two full transversals as subsets.

That argument says nothing about a face whose occupied support is a proper
subset `I` of the macro blocks.  Adding the missing macro labels is not a
hereditary operation; it can hide a previously exposed chain point.  The
counterexample does exactly this:

\[
       \{a,a',b,c\}\in\mathcal F(P),\qquad
       \{a,a',b,c,d\}\notin\mathcal F(P).                   \tag{6}
\]

Therefore “full pair unions are bad” controls only the full-support term of
the recurrence.  It does not turn all `|I|>=3` terms into transversals.

## 3. The state required by an exact radial recurrence

For a cyclic macro support `I` and `i in I`, let
`p_I(i),n_I(i)` be the preceding and following occupied macro blocks.  A
shrunk radial composition needs a rooted profile

\[
        R_i^{a,b}=#\{S\subseteq X_i:S\text{ is exposed between the
                       directions to macro blocks }a,b\}.  \tag{7}
\]

For one occupied block, `R_i` is the full convex-face count.  For two
occupied blocks, the two local choices can have a coupled directional
condition.  For at least three well-separated occupied blocks, the usual
radial substitution law, when proved for the chosen realization, has the
form

\[
 V=1+\sum_{\varnothing\ne I\subseteq[q]}
       \prod_{i\in I}R_i^{p_I(i),n_I(i)},                    \tag{8}
\]

with the one- and two-block terms interpreted by their actual kernels.
Equation (8) is a state description, not a universal scalar formula: its
validity requires the cross-block orientation/separation hypotheses of the
specific wrapper.

The failed recurrence replaces every factor in (8) for `|I|>=3` by
`|X_i|`, i.e. it assumes only singleton choices.  Proposition 1 shows

\[
                         R_0^{1,2}\ge3,qquad
                         R_0^{1,3}=2,                        \tag{9}
\]

even though the underlying block is unchanged.  The neighboring occupied
directions are indispensable state.

Fixed-edge projective universality makes this more serious, not less.  A
strict dominance chain can carry an arbitrary planar order type while
preserving every intrinsic convex subset.  Its rooted arrays (7) therefore
cannot be reconstructed from the block size, its full face count, or the
fact that it is nested.  A valid upper recurrence must carry the directional
arrays themselves, or prove a new inequality controlling their complete
mask sum.

## 4. Coefficient audit

Let the child have `m` points and

\[
                 \log V(Q_m)=(c+o(1))(\log m)^2.             \tag{10}
\]

A single radial wrapper using `q=Theta(log m)` copies has `N=qm` points and
contains each copy as an induced subset.  Hence

\[
 {\log V(\operatorname{Wrap}_q(Q_m))\over(\log N)^2}
       \ge c-o(1).                                          \tag{11}
\]

In particular a known coefficient-`1/2` child cannot be improved by one
such wrapper, regardless of how favorable the cross-block terms are.

The transversal bank gives the independent lower bound

\[
                  V(\operatorname{Wrap}_q(Q_m))\ge m^q.     \tag{12}
\]

For `q=(kappa+o(1))log m`, equations (11)--(12) give only

\[
              c_{\rm out}\ge\max(c,\kappa)-o(1).            \tag{13}
\]

They do not rule out coefficient decay under an unbounded sequence of
wrappers, because the logarithmic size increases slightly at every level.
Conversely, the three-class proposal cannot prove such decay: Proposition
1 invalidates its claimed full-face upper recurrence at the first wrapper.

The exact iterated question is therefore a rooted-profile problem for (8).
It is the same cap/cup anti-alignment issue encountered in heterogeneous
strong-glue blow-ups, now with a cyclic occupied-mask state.  No sub-half
construction follows from the radial wrapper as presently specified.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_radial_universal_wrapper_audit.py
```

The checker uses exact fractions to verify general position, all sixteen
convex transversals, all 120 detached-pair unions, strict nesting against
all neighboring representatives, the released `2+1+1` face, the full
profile (5), and every support-mask count.
