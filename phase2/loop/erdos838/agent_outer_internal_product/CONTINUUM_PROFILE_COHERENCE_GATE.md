# A stationary quarter ramp needs a projectively coherent full profile word

**Date:** 2026-08-15.  Counts with a hat include the empty set and all
logarithms are base two.

## Verdict

For a **stationary, single-completed-order-type recursion**, the
two-direction state `Pi_2` is not enough.  If the same completed child must
expose all `q=Theta(log D)` profiles used at the next level, each embedded
copy acts on the whole direction line by one element of `PGL_2`; it cannot
choose those `q` profiles independently.

This hypothesis is not automatic in the general recursive construction.
A branching menu may build a different completed parent type `P_s` for
each desired next-ramp level `s`.  Inside `P_s`, each physical child copy
services only its current assembly direction and the one designated reset
direction of `P_s`.  Ordered-pair transitivity then makes `Pi_2` the correct
local state, and no one copy is forced to satisfy all calibrations below.

Accordingly, this report is an exact conditional theorem for stationary
recursion.  It is **not** the final gate for the live branching menu.

There is an exact quantitative reduction.  Suppose a `D`-point child `Q`
has

\[
                 W(Q)\ge D^{q-\varepsilon q},                 \tag{1}
\]

and a `q`-role first-cap/last-cup wrapper is required to have

\[
                 W(P)\le D^{q+\varepsilon q}.                 \tag{2}
\]

Then the child profiles used at the two end roles must differ in cap
exponent by

\[
        \log_D\widehat C_q-\log_D\widehat C_1
          \ge q-2-2\varepsilon q-o(1).                        \tag{3}
\]

Thus a quarter-scale wrapper really needs the whole scalar ramp, not one
cheap reset pair.

Now impose the stationary hypothesis that one completed parent is intended
to supply the whole next ramp at directions `theta_s`, `0<=s<=q`.  If

\[
 \widehat C_P(\theta_s)\le D^{s+\varepsilon q},\qquad
 \widehat U_P(\theta_s)\le D^{q-s+\varepsilon q},              \tag{4}
\]

then **every** embedded child map `phi_i in PGL_2` is pinned at every
calibration direction:

\[
\begin{aligned}
 s-2\varepsilon q
 &\le\log_D\widehat C_Q(\phi_i\theta_s)
 \le s+\varepsilon q,\\
 q-s-2\varepsilon q
 &\le\log_D\widehat U_Q(\phi_i\theta_s)
 \le q-s+\varepsilon q.                                  \tag{5}
\end{aligned}
\]

At the old assembly direction, however, the same `q` projective maps must
spread through essentially all `q` levels by (3).  Consequently any
sub-half stationary recursive construction must exhibit the following
genuinely continuum phenomenon:

> `q` projective reparameterizations of one profile function agree, to
> `o(q)`, on `q` prescribed ramp levels, but at one additional direction
> their profile values spread by `q-o(q)`.

This is much stronger than a cheap member of `Pi_2`.  It is a full
profile-word/cross-ratio coherence problem when one physical order type is
reused for all levels.  A branching type menu evades the simultaneous
requirement.

There is also an exact obstruction to replacing that problem by any local
pair or triple test.  Four source directions can be chosen so that every
three prescribed target chambers are simultaneously reachable by a
projectivity, while no one projectivity reaches all four.  Thus even
`Pi_3`-wise feasibility does not imply a coherent `Pi_q` itinerary.

This report does **not** prove the required profile rigidity and does not
construct a sub-half family.  In the stationary subclass it identifies a
sufficient positive theorem:
if three or more calibrated ramp levels projectively localize all admissible
maps enough that their assembly values have width `o(q)`, the end-to-end
wrapper term is `D^{2q-o(q)}` and the coefficient jumps from `1/4` to
`1/2`.  Conversely, a stationary quarter construction must explicitly
defeat this localization at every scale.  A branching construction may
instead change order type with `s`.

The half-scale inductive pocket does not remove this gate.  It raises the
average blocker-cover entropy from one quarter to one half, but it supplies
neither a common projective parameter nor the cross-ratio-coherent profile
word required in (5).

## 1. Universal endpoint product

For a generic projection direction `xi`, let
`C_hat_Q(xi),U_hat_Q(xi)` count cap and cup chains including the empty
chain.  Every ordinary face has a unique lower and upper boundary chain in
that projection.  The pair of chains recovers the face, hence

\[
                  W(Q)+1\le
           \widehat C_Q(\xi)\widehat U_Q(\xi).                \tag{6}
\]

This statement is direction-by-direction and survives arbitrary affine or
projective recharting inside one convex affine patch.

## 2. Quarter budget forces full assembly width

Put

\[
       a_i=\log_D\widehat C_i,\qquad
       b_i=\log_D\widehat U_i,
       \qquad \lambda_D=\log_D(D+1).                         \tag{7}
\]

By (1) and (6),

\[
                         a_i+b_i\ge q-\varepsilon q.          \tag{8}
\]

The exact first-cap/last-cup recurrence contains, for every `i<j`, the
ordinary-face bank

\[
 (\widehat C_i-1)(\widehat U_j-1)(D+1)^{j-i-1}.               \tag{9}
\]

Since every nonempty role has nonempty cap and cup chains,
`C_hat-1>=C_hat/2` and `U_hat-1>=U_hat/2`.  Put
`kappa_D=log_D 4`.  At the two end roles, (2), (8), and (9) give

\[
\begin{aligned}
 q+\varepsilon q
 &\ge a_1+b_q+(q-2)\lambda_D-\kappa_D\\
 &\ge a_1+q-\varepsilon q-a_q
          +(q-2)\lambda_D-\kappa_D.
\end{aligned}                                               \tag{10}
\]

Since `lambda_D>=1`, this proves (3).  In the zero-error exponent model the
only possibility is the familiar slope-one ramp

\[
                         a_i=i+O(1),\qquad b_i=q-i+O(1).       \tag{11}
\]

This explains the exact finite searches: minimizing one reset product does
not certify bootstrap.  The completed child must regenerate essentially
the full width in (3).

There is a useful converse coefficient audit.  If some geometric theorem
forces

\[
                         a_q-a_1\le\rho q,                    \tag{12}
\]

then the end-to-end term alone gives

\[
 \log_D W(P)
 \ge 2q-(\varepsilon+\rho)q-2-\kappa_D.                     \tag{13}
\]

For `q=(1/4+o(1))log D`, `epsilon,rho=o(1)`, equation (13) is the
coefficient-one-half lower bound.

## 3. Every child is pinned at every next-ramp direction

Let `phi_i` be the projective action on directions induced by the affine
embedding of child `i`.  A cap or cup lying entirely in that child is also
a cap or cup of the parent.  Therefore (4) implies

\[
\begin{aligned}
 \log_D\widehat C_Q(\phi_i\theta_s)&\le s+\varepsilon q,\\
 \log_D\widehat U_Q(\phi_i\theta_s)&\le q-s+\varepsilon q.
                                                               \tag{14}
\end{aligned}
\]

Apply (1) and (6) in the child chamber `phi_i theta_s`.  Subtracting the
second upper bound in (14) from the product lower bound gives the first
lower bound in (5); subtracting the first gives the second.  No seam
classification is used.  This is merely ambient inheritance of endpoint
chains, so it remains valid for the nonlinear common-pocket realization.

Equation (5) is the sharp continuum-state condition **under the stationary
multi-reset hypothesis**.  At every reset level all copies must follow the
same ramp value, while at the assembly direction their values must be
separated by (3).  One `PGL_2` map per copy has to do both jobs
simultaneously.  If reset level `s` uses a separately built type `P_s`, this
paragraph does not apply.

Here is a clean conditional closure.

> **Profile-calibration rigidity hypothesis.**  For the child family, any
> collection of orientation-preserving projective maps `phi_i` satisfying
> (5) on the chosen calibration directions also satisfies
>
> \[
>  \max_i\log_D\widehat C_Q(\phi_i\xi)
>  -\min_i\log_D\widehat C_Q(\phi_i\xi)=o(q)                 \tag{15}
> \]
>
> at the assembly direction `xi`.

Under this hypothesis, (3) and (15) are incompatible with (2); equivalently
(13) gives the half coefficient in the stationary subclass.  This does not
close a branching `Pi_2` menu.

## 4. Exact cross-ratio obstruction to local-state gluing

Work on one affine chart of the direction line and use

\[
 [x_1,x_2;x_3,x_4]
 ={(x_3-x_1)(x_4-x_2)\over(x_4-x_1)(x_3-x_2)}.               \tag{16}
\]

Take source directions

\[
                         (x_1,x_2,x_3,x_4)=(0,1,2,3),         \tag{17}

\]

whose cross ratio is `4/3`.  Let `epsilon=1/100` and prescribe target
chambers

\[
\begin{aligned}
 J_1&=[-\varepsilon,\varepsilon],&
 J_2&=[1-\varepsilon,1+\varepsilon],\\
 J_3&=[2-\varepsilon,2+\varepsilon],&
 J_4&=[4-\varepsilon,4+\varepsilon].                        \tag{18}
\end{aligned}
\]

For every increasing choice `y_i in J_i`, direct monotonicity of (16) in
each coordinate, or evaluation at the sixteen corners, gives

\[
 {5000\over3383}
 \le[y_1,y_2;y_3,y_4]
 \le {5000\over3283}.                                      \tag{19}
\]

The interval in (19) does not contain `4/3`.  Cross-ratio invariance proves
that no projectivity sends all four source directions into their prescribed
chambers.

On the other hand, every ordered triple of source directions can be sent
to the centers of the corresponding three target chambers by the unique
orientation-preserving projectivity.  In particular all pair tests and all
triple tests pass.  This proves exactly why a bank of independently
compatible `Pi_2` or `Pi_3` states is not a common multi-reset construction.
It does not prevent using those states in different branches/order types.

## 5. Activity needed to traverse a ramp

There is one more exact, though not by itself decisive, invariant.  When a
projection direction crosses one critical pair direction, the projection
order changes by one adjacent transposition.  If `C_hat,C_hat'` are the cap
counts on the two sides, then

\[
                  {1\over2}\widehat C
                    \le\widehat C'\le2\widehat C,             \tag{20}

\]

and the same holds for cups.  Indeed, a chain destroyed by swapping labels
`a,b` becomes a chain after deleting `a`; the decoder records whether `a`
was present and has load at most two.  Reverse the swap for the other
inequality.

Thus changing a cap exponent by `q log D-o(q log D)` requires at least that
many critical pair crossings along the direction arc.  A recursive quarter
ramp must not only have the cross-ratio coherence in (5); it must carry
`Theta(q log D)=Theta((log D)^2)` directional activity in the appropriate
projective locations.  The bound is necessary but not sufficient because a
`D`-point child has quadratically many available pair directions.

## 6. Half-scale pocket audit

If an inductive pocket of size `n/polylog(n)` already supplies

\[
          \log H=(1/2-o(1))(\log n)^2,                         \tag{21}

\]

then the exact average cover theorem in
`MINIMIZER_WEIGHTED_LOOP_COVER_GATE.md` upgrades the mean deleted-alphabet
entropy to the same half scale (under its aggregate-load hypothesis).  Its
duality consequence becomes loop entropy at least one quarter or fractional
`2+2` packing at least one eighth.

This does not imply (15).  The common-guard loop regression can store
quadratic entropy in `Theta(log n)` role alphabets while its actual
all-direction repair set has only `Theta(log n)` labels.  Deleting those
labels changes every cap, cup, and ordinary-face count by only
`2^{O(log n)}`.  Hence the half-scale bootstrap localizes the hard branch,
but it neither fixes the projective profile parameter nor prevents the
cross-ratio obstruction in Section 4.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_continuum_profile_coherence_gate.py
```

Expected output:

```text
PASS: scalar ramp width, reset pinning, adjacent-swap factor two, and four-direction cross-ratio obstruction verified
```

The verifier checks the exponent inequalities exhaustively in an integer
model, exhausts the adjacent-swap statement on all eight rooted four-point
chirotopes and all orders, and proves the rational cross-ratio separation in
(19) exactly.
