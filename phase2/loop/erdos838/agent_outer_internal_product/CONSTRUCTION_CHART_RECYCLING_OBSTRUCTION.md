# A low-face ramp cannot recycle its construction chart twice

**Date:** 2026-08-15.  Counts with hats include the empty set and all
logarithms are base two.

## Verdict

The abstract recycled-`Pi_2` escape in
`BRANCHING_PROFILE_QUERY_DEPTH_GATE.md` is unavailable in the exact
first-cap/last-cup quarter ramp unless the construction chart is used in at
most one role of the next wrapper.

Let `P` be a `q`-role ordered wrapper with equal `D`-point child blocks.
Assume every child has

\[
                         Z_i\ge D^{q-\delta q}             \tag{1}
\]

ordinary faces including the empty set, while

\[
                         Z(P)\le D^{q+\delta q}.            \tag{2}
\]

Then in the chart in which the first/last recurrence constructs `P`,

\[
\begin{aligned}
 \log_D\widehat C(P)&\ge q-2\delta q-2-\log_D8,\\
 \log_D\widehat U(P)&\ge q-4\delta q-2-\log_D16.
                                                               \tag{3}
\end{aligned}
\]

Thus

\[
             \widehat C(P)\widehat U(P)
                    \ge D^{2q-6\delta q-4}/128.           \tag{4}
\]

If two child roles in the next ordered wrapper reuse such construction
charts, their forward cap--cup term gives

\[
                  W_{\rm next}\ge D^{2q-6\delta q-4}/512. \tag{5}
\]

At `delta=o(1)`, `q=(1/4+o(1))log D`, and next child size
`N=(q+o(q))D`, equation (5) has coefficient `1/2-o(1)`.  Hence a next
wrapper obeying the quarter budget can recycle the construction chart in
at most one of its `q` roles.  The other `q-1` roles must use genuinely
different reset charts.

This does not close the lower bound.  It restores pathwise query novelty
for the exact ramp, but the recursion depth is only
`Theta(log N/log log N)`, and the known coherent-itinerary entropy along a
path is still `o((log N)^2)`.  Endpoint activity alone is also insufficient:
`PROJECTIVE_RAMP_ACTIVITY_COUNTERMODEL.md` survives even the stronger
stationary `Theta(log N)`-query pattern.  The remaining target is a planar,
downward-closed multi-chart rigidity theorem.

The result is specific to a low-face ordered first/last recurrence with
macroscopic rich children.  It is not a theorem that every conceivable
recursive wrapper has a fresh chart.

## 1. Exact construction-chart endpoint bounds

Write

\[
 a_i=\log_D\widehat C_i,\qquad
 b_i=\log_D\widehat U_i,\qquad
 p=q+\delta q+\log_D2.                                  \tag{6}
\]

Every ordinary child face is recovered from its lower and upper boundary
chains, so (1) gives

\[
                              a_i+b_i\ge q-\delta q.      \tag{7}
\]

Every child cap or cup is an ordinary child face and every child face is
an ambient face.  Hence

\[
                       a_i,b_i\le\log_DZ(P)\le p.         \tag{8}
\]

The exact first/last recurrence contains the end-to-end bank

\[
  (\widehat C_1-1)(\widehat U_q-1)(D+1)^{q-2}.            \tag{9}
\]

Every nonempty `D`-point block has at least two cap and two cup chains, so
`\hat C_i-1>=\hat C_i/2` and similarly for cups.  Since
`log_D(D+1)>=1`, equations (2), (7), and (9) imply

\[
\begin{aligned}
 p&\ge a_1+b_q+(q-2)-\log_D4\\
  &\ge a_1+q-\delta q-a_q+(q-2)-\log_D4.
                                                               \tag{10}
\end{aligned}
\]

Therefore

\[
                a_q-a_1\ge q-2\delta q-2-\log_D8.        \tag{11}
\]

Using `a_1>=0`, equation (11) gives the first line of (3), because every
cap chain in the last child remains a parent cap chain.  On the other hand,
(8) and (11) give

\[
                       a_1\le3\delta q+2+\log_D16.        \tag{12}
\]

Apply (7) at child `1`:

\[
                       b_1\ge q-4\delta q-2-\log_D16.     \tag{13}
\]

Every cup chain in the first child remains a parent cup chain, so (13)
proves the second line of (3).  Adding the two lines proves (4).

The argument is the finite version of the assembly-width lemma in
`CONTINUUM_PROFILE_COHERENCE_GATE.md`, with the additional observation
that the two extreme child profiles are inherited by the completed parent.

## 2. Two recycled roles force the forward square

Take two completed wrappers `P_i,P_j` satisfying (3), placed in roles
`i<j` of the next ordered recurrence and viewed in their construction
charts.  Its ordinary-face count contains

\[
  (\widehat C(P_i)-1)(\widehat U(P_j)-1)
        \prod_{i<k<j}(1+|P_k|).                           \tag{14}
\]

Discard the intermediate product and use the factor-two bounds once more.
Equations (3)--(4) give (5).  The active role mask and the traces in the
two child supports recover every output, so this is a one-face bank, not a
two-record square estimate.

Since any two recycled roles are ordered one before the other, (5) proves
the at-most-one assertion.  In a quarter-scale next wrapper, every other
role must be viewed in a chart where at least one endpoint count has fallen
by `D^{q-o(q)}` relative to (3).  Such a chart is necessarily distinct
from the construction chart.

There is a useful stronger formulation.  Any exported chart intended to
be a tight next-ramp input satisfies

\[
               \widehat C(\xi)\widehat U(\xi)
                         \le D^{q+o(q)}.                  \tag{15}
\]

Equation (4) shows that the construction chart is not among these exported
charts.  Therefore a recursive type which exports only tight ramp profiles
must add its construction chart as a genuinely fresh query to its children.

## 3. Query novelty on the recursion tree

At a node with `q_k` children, mark the at most one role which recycles the
construction chart.  Every other edge is fresh.  A uniformly chosen
root-to-leaf path uses a recycled edge at level `k` with conditional
probability at most `1/q_k`.  Consequently

\[
 \mathbb E R_h\le\sum_{k<h}{1\over q_k},\qquad
 \mathbb E(h-R_h)\ge h-\sum_{k<h}{1\over q_k},            \tag{16}
\]

where `R_h` is the number of recycled edges.

For balanced recursion,

\[
 L_{k+1}=L_k+\log L_k+O(1),\qquad q_k=\Theta(L_k).        \tag{17}
\]

The integral test gives

\[
 h=\Theta\left({L_h\over\log L_h}\right),\qquad
 \sum_{k<h}{1\over q_k}=O(\log\log L_h).              \tag{18}
\]

Thus a random branch has `h-O(log log L_h)` fresh edges in expectation.
Also the exact fraction of leaves whose every edge is fresh is at least

\[
                    \prod_{k<h}\left(1-{1\over q_k}\right)
                         =(\log L_h)^{-O(1)}.             \tag{19}
\]

So a polylogarithmic fraction of the physical leaves carries a genuinely
growing chart itinerary.

Equations (18)--(19) restore the pathwise coherence question but do not
solve it.  The polynomial `PGL_2` itinerary bound costs only

\[
                   O\left(\sum_{k<h}L_k\right)
                       =O\left({L_h^2\over\log L_h}\right)             \tag{20}
\]

bits along one branch.  This is subquadratic.  A coefficient-half theorem
must convert simultaneous novelty across the many leaves in (19) into
ordinary faces or prove a stronger all-direction endpoint-energy invariant.

## 4. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_construction_chart_recycling.py
```

Expected output:

```text
PASS: low-W ramp forces high construction endpoints; two recycled roles force the forward square; fresh paths have polylog density
```

The verifier checks the cleared finite inequalities over a grid of
`D,q,delta`, evaluates the exact integral ramp recurrence and its completed
construction-chart endpoint counts, checks the two-role forward bank, and
audits (16)--(19) on balanced trees.

## Scope

This is a rigorous obstruction to the recycled-mark escape **inside the
exact low-face common-guard/strong-comb ramp**.  It proves no universal
multi-chart rigidity theorem and makes no EIC' closure claim.
