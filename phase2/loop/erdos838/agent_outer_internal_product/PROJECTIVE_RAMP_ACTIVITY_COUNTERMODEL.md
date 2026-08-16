# A stationary projective ramp defeats endpoint variation at mean rank `Theta(q)`

**Date:** 2026-08-15.  All counts include the empty face and logarithms are
base two.

## Verdict

The stationary continuum condition in
`CONTINUUM_PROFILE_COHERENCE_GATE.md` cannot be closed using only

1. the endpoint product `C(theta)U(theta)>=V`,
2. factor-two change across one projection-chamber wall,
3. cross-ratio coherence of one `PGL_2` map per child, and
4. the `O(mu V)` total directional-activity bound supplied by mean face
   rank `mu`.

For every `q>=2` and `D=2^L` there is an explicit integer step-function
model on the oriented projective line with

\[
                         V=D^q,\qquad \mu<2q,                 \tag{1}
\]

and `q` affine projectivities `phi_i` such that, at common calibration
directions `theta_s`,

\[
 C(\phi_i\theta_s)=D^s,\qquad
 U(\phi_i\theta_s)=D^{q-s}\quad(0\le s\le q)                \tag{2}
\]

for **every** `i`, while at one common assembly direction `xi`,

\[
 C(\phi_i\xi)=D^i,\qquad
 U(\phi_i\xi)=D^{q-i}\quad(0\le i<q).                       \tag{3}
\]

Thus the maps agree perfectly on the entire calibrated ramp but spread
through the full width at assembly--exactly the phenomenon a stationary
single-order-type quarter construction would need.

The model is stronger than an arbitrary list of counts.  It has

\[
                         C(t)U(t)=V                            \tag{4}
\]

at every direction, neighboring chambers change each endpoint count by a
factor at most two, and `C` is the coverage function of `V` formal face
activities.  Every nonempty formal activity is a union of exactly `2q-1`
direction intervals.  This saturates the genuine planar inequality

\[
                    \operatorname {TV} C\le2\mu V.            \tag{5}
\]

Consequently the live scale `q=Theta(log n)`, `mu=Theta(log n)` leaves no
variation surplus.

This is **not** a planar order-type construction.  It is also not a model
of the general branching recursion, which may use a different completed
order type for each reset level and never imposes all calibrations (2) on
one type.  The missing condition within the stationary subclass is
simultaneous realizability of all the formal activity intervals by one
downward-closed convex-face complex on one ground set.  In a real point set,
activities of a face and all its subfaces are strongly coupled.  The model
proves that any positive rigidity theorem must use precisely that coupling
(or an equivalent planar circuit constraint); endpoint variation, mean rank,
and projective cross ratios alone are sharp.

## 1. The genuine planar activity inequality

Let `P` be a planar general-position set.  For an ordinary face `F`, let
`A_F` be the set of oriented projection directions in which `F` is a cap.
If `|F|>=3`, a cap direction makes the minimum and maximum projected
vertices adjacent on the boundary polygon of `F`.  Fixing that boundary
edge gives one direction interval, and there are `|F|` edges.  Hence

\[
               A_F\text{ is a union of at most }|F|
               \text{ intervals}.                            \tag{6}
\]

The same conclusion is immediate for ranks zero, one, and two.  Since a
cap is automatically an ordinary face,

\[
              C(t)=\sum_{F\in\mathcal F(P)}1_{A_F}(t).        \tag{7}
\]

Each interval indicator has cyclic total variation two.  If `V` counts the
empty face and `mu=V^{-1}sum_F|F|`, then

\[
             \boxed{\operatorname {TV}C
                    \le2\sum_F|F|=2\mu V.}                   \tag{8}
\]

Cup activity is the antipodal cap activity, so the same bound holds for
`U`.  Equation (8) is stronger than the factor-two adjacent-wall bound, but
the construction below attains equality with its formal rank budget.

## 2. Exact scalable countermodel

Fix integers `q>=2`, `L>=1` and put

\[
                  D=2^L,\qquad V=2^{qL}.                     \tag{9}
\]

Use an affine coordinate `t` on one oriented semicircle.  Define

\[
\begin{aligned}
 B&=qL+2,\\
 H&=L+2,\\
 T&=B+qH+qL+4.                                               \tag{10}
\end{aligned}
\]

For `0<=i<q`, prescribe an integer exponent function `e(t)` at the
landmarks

\[
                e(iT)=Li,\qquad
                e(iT+B+sH)=Ls\quad(0\le s\le q).             \tag{11}
\]

Between consecutive landmarks, move by steps in `{-1,0,1}` until the next
prescribed value is reached and then stay constant.  The slack in (10)
makes this possible: `B>=iL`, `H>=L`, and the gap after one ramp is at least
`qL`, enough to reach the next assembly value.

The first exponent is zero and the last is `qL`.  Copy this finite sequence
to the antipodal semicircle by

\[
                         e(-t)=qL-e(t).                       \tag{12}
\]

The endpoint values make (12) cyclic with adjacent exponent changes at most
one.  Define

\[
                         C(t)=2^{e(t)},\qquad U(t)=C(-t).      \tag{13}
\]

Equations (4) and the factor-two wall condition are immediate.

Take

\[
             \xi=0,\qquad \theta_s=B+sH,\qquad
             \phi_i(t)=t+iT.                                \tag{14}
\]

Every `phi_i` is an affine, hence projective, transformation.  Substitution
of (14) into (11)--(13) proves (2) and (3) exactly.  In particular all cross
ratios are automatically coherent; the construction is not assembling
independent pair or triple states.

## 3. Formal face activities and exact saturation

For `1<=h<=V`, define the formal cap-active set

\[
                         A_h=\{t:C(t)\ge h\}.                  \tag{15}
\]

Then

\[
                         C(t)=\sum_{h=1}^V1_{A_h}(t).         \tag{16}
\]

The set `A_1` is the whole circle and represents the empty face.  For
`h>1`, put `r=ceil(log_2 h)`.  The set `A_h` is `{e>=r}`.  The exponent path
has one assembly excursion and one full ramp in each translated block;
direct inspection of (10)--(12) gives

\[
                 A_h\text{ has exactly }2q-1
                 \text{ connected components}.              \tag{17}
\]

Assign formal rank `2q-1` to every `h>1` and rank zero to `h=1`.  The mean
formal rank is

\[
               \mu={(V-1)(2q-1)\over V}<2q.                 \tag{18}
\]

Moreover every change of `e` is monotone by one at that wall, so no interval
endpoint cancellation occurs.  Therefore

\[
 \operatorname {TV}C
   =2(2q-1)(V-1)=2\mu V.                                    \tag{19}
\]

The planar activity inequality (8) is exactly saturated.

## 4. The remaining geometric question

The formal labels `h` are not asserted to be subsets of a common `D`-point
ground set.  Even if they are assigned distinct rank-`2q-1` subsets, their
downsets overlap and must themselves have cap-activity sets containing the
parent activities.  An arbitrary union of `2q-1` direction intervals is not
automatically the cap-direction set of one convex polygon, and arbitrary
choices for many faces need not arise from one chirotope.

Thus the exact survivor is:

> **Downward-closed activity rigidity.**  Can a planar convex-face complex
> with mean rank `O(q)` realize the translated ramp pattern (2)--(3), or do
> subface/circuit compatibilities force additional ordinary faces or a
> common projective localization?

A negative answer would be the missing rigidity theorem for the stationary
subclass and, through `CONTINUUM_PROFILE_COHERENCE_GATE.md`, would force its
coefficient-half jump.  A positive rational realization would give a
credible stationary sub-half construction.  Neither conclusion addresses
the live branching `Pi_2` menu by itself.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_projective_ramp_activity_countermodel.py
```

Expected output:

```text
PASS: translated ramps calibrate and spread; CU=V; wall ratio<=2; components=2q-1; TV=2 mu V
```

The verifier checks every displayed identity for `2<=q<=9`, `1<=L<=5`
using exact integers.  It constructs the full cyclic exponent word, verifies
all landmarks and translated projectivities, counts every superlevel-set
component, and checks the exact total-variation equality (19).
