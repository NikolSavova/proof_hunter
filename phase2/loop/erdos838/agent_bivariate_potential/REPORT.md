# Bivariate tangent potential and averaged arbitrary-point deletion

**Date:** 2026-08-14  
**Verdict:** no proof of unrestricted Erdős 838 is claimed.  This lane finds
one substantially cleaner sufficient theorem, rewrites it as the exact
integrated blocked-incidence inequality, and isolates the sole term that a
QuickHull Bellman potential must pay.  The most direct four-corner mixed
potential is false on an exact stretchable twenty-point set.  A stronger
two-rooted inequality survived exact countersearch, but I do not have the
global charging theorem needed to turn it into the sufficient theorem.

Throughout, `h=1/2`, `Z=Z_P`, and all convex-face polynomials include the
empty face.

## 1. The averaged arbitrary-point theorem would close the problem

For any point `e`, whether extreme or not, write

\[
 Z_P(t)=Z_{P-e}(t)+tR_e(t).
\]

The rooted amortization inequality

\[
 2Z_{P-e}(h)+nR_e(h)\leq4R_e(1)                         \tag{RA_e}
\]

has the same deletion-induction algebra for an arbitrary `e` as for a hull
point.  Summing over all `e` and using

\[
 \sum_e Z_{P-e}(t)=nZ(t)-tZ'(t),\qquad
 \sum_eR_e(t)=Z'(t)
\]

shows that the average of `(RA_e)` is precisely

\[
 \boxed{nZ(h)+(n-1)hZ'(h)\leq2Z'(1).}                    \tag{APA}
\]

Thus `(APA)` implies that some point satisfies `(RA_e)`; induction from the
empty set gives `nZ(h)<=2Z(1)`, proving the finite half-weight conjecture and
therefore the coefficient-one-half lower bound.

This target survives every test performed in the parallel arbitrary-root
lane, including the 63- and 131-point wrappers that kill every hull choice.
It also survives exact type-A annealing from the best stretchable records.
The closest value found here is `0.930921...` times the right side at `n=30`.
This is evidence only.

## 2. Exact boundary form: maximal faces remain the gate

Put

\[
 B_r=(n-r)v_r-(r+1)v_{r+1}
     =\sum_{A\in F_r}b(A).
\]

Using

\[
 nZ(t)-tZ'(t)=Z'(t)+\sum_rB_rt^r
\]

at `t=h` gives the exact equivalence

\[
 \boxed{
 \sum_r2^{-r}B_r
 \leq2Z'(1)-(1+n/2)Z'(1/2).}                              \tag{BAPA}
\]

So `(APA)` has not bypassed the known obstruction: it is an integrated
blocked-incidence inequality.  The first-switch theorem controls the part
with `u(A)>0`; the uncharged contribution is again the maximal-face reset.
The advantage of `(BAPA)` is that all ranks are already amortized with the
correct half weights, matching the block compensation seen in Pascal towers.

## 3. The smallest genuine bivariate state

For endpoints `u<v`, let `R^+_{uv}(x)` and `R^-_{uv}(y)` count rooted convex
chains on the two sides of `uv`.  Define

\[
 K_P(x,y)=\sum_{u<v}R^+_{uv}(x)R^-_{uv}(y).
\]

With the empty-path diagonal removed, the endpoint decomposition is exact:

\[
 Z_P(z)=1+nz+K_P(z,z).                                    \tag{1}
\]

The mixed corners contain information absent from `Z` alone.  They have the
universal positive interaction

\[
 K(1,1)+K(h,h)-K(1,h)-K(h,1)
 =\sum_{u<v}(R^+_1-R^+_h)(R^-_1-R^-_h)\geq0.              \tag{2}
\]

The simplest attempted use of (2),

\[
 nK(h,h)\leq2\{K(1,h)+K(h,1)\},                           \tag{3}
\]

is false.  On the exact fixed-`x` integer twenty-point record used by the
half-weight search, `RHS/LHS=0.7725845...`.  Hence merely keeping the four
scalar corner evaluations does not pay the tangent restart.  The dynamic
rooted state, or derivatives/graded data, are essential.

## 4. Exact QuickHull Bellman recurrence and excluded-pivot debt

For a rooted instance `(u,v;Q)`, let

\[
 R_t=R_{uv}(Q;t),\qquad V=Z_Q(1),\qquad m=|Q|,
\]

and consider the experimentally stronger rooted target

\[
 \boxed{mR_{1/2}\leq R_1+V.}                               \tag{RT}
\]

This is the parent lane's proposed inequality with constant `C=1` rather
than `C=2`.  It passed the exact random audit through `m=12`; a broader
earlier scan through `m=14` had maximum ratio below `0.689`, and exhaustive
fixed-`x`, permutation-height configurations through `m=8` had maximum below
`0.653`.  These are finite tests, not a proof.

A tempting reduction of `(RT)` to a perfect-graph inequality is unavailable.
If two pocket points are declared adjacent when they form a rooted convex
quadrilateral with `u,v`, rooted chains are **not** the clique complex.  With

```text
u=(0,0), v=(100000,0),
Q={(110597,138659),(16176,148701),(87080,127172)},
```

all three pairs are compatible, but the full rooted five-point set is
nonconvex.  All determinants are nonzero.  Thus the rooted obstruction is
genuinely ternary (the consistent-turn/cap condition), and a graph
clique--antichain argument loses essential geometry.

The precise induction obstruction is now explicit.  Let `x` be the
outermost QuickHull pivot, let `L,R,D` be its left, right, and discarded
middle regions, and put `R_0(t)=R_{uv}(Q-x;t)`.  The exact rooted recurrence
is

\[
 R_t=R_0(t)+tR_{ux}(L;t)R_{xv}(R;t).                       \tag{4}
\]

Define the Bellman slack

\[
 S_m(Q)=R_1+Z_Q(1)-mR_{1/2}.
\]

Writing `Delta_x V=Z_Q(1)-Z_{Q-x}(1)`, direct substitution into (4) gives

\[
\begin{aligned}
 S_m(Q)=S_{m-1}(Q-x)&-R_0(h)+R_L(1)R_R(1)\\
 &-\frac m2R_L(h)R_R(h)+\Delta_xV.                         \tag{5}
\end{aligned}
\]

Every selected product face through `x`, after deleting the fixed roots
`u,v`, is an unrooted convex face of `Q` containing `x`.  Consequently

\[
 \Delta_xV\geq R_L(1)R_R(1),                              \tag{6}
\]

and

\[
 S_m(Q)\geq S_{m-1}(Q-x)-R_0(h)
       +2R_L(1)R_R(1)-\frac m2R_L(h)R_R(h).                \tag{7}
\]

Equation (7) is the cleanest form of the remaining tangent obstruction.  An
include pivot creates two-orientation product credit.  Each preceding
exclude pivot charges the full surviving half-weight `R_0(h)`.  The 63-point
outer-triangle example is exactly the regime in which a long sequence of
exclude charges cannot be paid by a scalar onion increment.

The natural attempt to make the slack monotone at each pivot is false.  It
would suffice to have

\[
 \Delta_xV+R_L(1)R_R(1)
 \geq R_0(h)+\frac m2R_L(h)R_R(h).                          \tag{8}
\]

This passed thousands of random instances but fails exactly on the
apex/concave-chain family.  Take roots `q_0,q_11`, put the high apex `p`
together with `q_1,...,q_10` in `Q`, and pivot first at `p`.  Then `m=11`,
`L=R=empty`, and

\[
 \Delta_pV=56,\qquad R_0(h)=(3/2)^{10}=59049/1024.
\]

The left side minus the right side of (8) is exactly

\[
 56+1-59049/1024-11/2=-6313/1024<0.                       \tag{9}
\]

The global rooted target `(RT)` nevertheless has large slack on the same
example: its ratio `mR_h/(R_1+V)` is
`655171/2155520=0.3039...`.  Hence the debt is genuinely amortized across
later exclude pivots; a pointwise Bellman monotonicity proof cannot work.

## 5. What remains to prove

There are now two tightly related live options.

1. Prove `(APA)`, equivalently `(BAPA)`, by routing the half-weighted maximal
   boundary through the two-orientation QuickHull stack.
2. Prove `(RT)` by showing that the cumulative excluded-pivot debts in (7)
   are paid by the unrooted increments `Delta_x V`, and then establish a
   bounded-multiplicity endpoint sum that converts `(RT)` into `(APA)`.

The first option is closer to the final theorem.  The second has the cleaner
local recurrence, but its global endpoint sum contains additional terms of
the form `Z(Q^+)R^-(h)` and cannot simply be discarded.  Any successful
potential must retain those terms; the failed inequality (3) shows why the
four corner scalars are insufficient.

There is also an important endpoint-normalization distinction.  In the
matrix polynomial (1), `u,v` are the leftmost and rightmost selected points;
the rooted ground set contains only the points with `x`-coordinate between
them.  Summing `(RT)` therefore weights `K(h,h)` by the endpoint span, not by
`n-2`; the points outside the span form another endpoint-extension debt.

Alternatively, sum over every unordered chord `{u,v}` and put every other
point into one of its two open half-planes.  If `C(x,y)` is the resulting
two-side rooted product sum, then exactly

\[
 C(t,t)=\frac12Z''(t),                                    \tag{10}
\]

because a `k`-face is counted once for each of its `binom(k,2)` chords.
Applying `(RT)` to both sides of every chord gives

\[
 (n-2)C(h,h)\leq C(1,h)+C(h,1)+T,                         \tag{11}
\]

where the exact leftover is

\[
 T=\sum_{\{u,v\}}
 \bigl[Z_{Q^+}(1)R^-_{uv}(h)+Z_{Q^-}(1)R^+_{uv}(h)\bigr]. \tag{12}
\]

Four-corner positivity only improves (11) to
`(n-3)C(h,h)<=C(1,1)+T`.  This is a second-derivative inequality, while
`(APA)` is first-derivative.  Thus even a proof of `(RT)` still needs both a
bound for `T` and an endpoint/integration argument converting `Z''` credit
to the `Z'` credit in `(APA)`.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_bivariate_potential/bivariate_potential_audit.py
```

The audit exactly verifies (1)--(7), the stretchability of the twenty-point
corner counterexample, the three-clique barrier, the visible-chain failure
of (8), the equivalence
`(APA)<->(BAPA)` on the exact graded profile, and 200 deterministic rooted
QuickHull instances.  It writes `certificate.json` beside the script.
