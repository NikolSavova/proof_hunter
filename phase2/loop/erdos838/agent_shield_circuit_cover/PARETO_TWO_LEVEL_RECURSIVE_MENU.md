# Exact Pareto-menu realization and the two-level projection-spectrum rebound

**Date:** 2026-08-15.  Counts are for nonempty ordinary convex subsets, and
all logarithms are base two.

## Verdict

The global reset menu of the 512 rooted four-point common-guard words has an
exact scalar optimum which is genuinely realizable, not merely a formal
recurrence.  After retaining the face count as well as the two endpoint
counts, the exact data are

\[
\begin{array}{c|c}
\text{object}&\text{count}\\ \hline
\text{distinct reset pairs }(C,U)&20671\\
\text{distinct reset states }(C,U,W)&42766\\
\text{coordinatewise-minimal }(C,U,W)\text{ states}&575.
\end{array}                                                   \tag{1}
\]

The exact minimum of the next three-child recurrence is

\[
 \boxed{W_2=747670},                                          \tag{2}
\]

attained by

\[
 (C,U,W)=(183,1975,1992),\quad(342,414,1986),\quad
          (1975,183,1992).                                   \tag{3}
\]

An exact rational strong-comb embedding realizes (3) on 44 points.  Its
full projection spectrum has 1884 oriented chambers and satisfies

\[
 \min_\xi C_\xi U_\xi
     =18275\cdot49645=907262375,
 \qquad
 \min_\xi\max(C_\xi,U_\xi)=39777.                            \tag{4}
\]

Optimizing one more scalar wrapper over the **whole** 44-point profile menu
gives

\[
 \boxed{W_3=11358202734}                                     \tag{5}
\]

on 134 points.  Thus the normalized exponent first drops and then rebounds:

\[
 {\log W_2\over(\log44)^2}=0.654648\ldots,
 \qquad
 {\log W_3\over(\log134)^2}=0.669002\ldots .                \tag{6}
\]

This is an exact finite obstruction to the simplest recursively resetting
quarter ramp.  It is **not** an all-scale lower bound.  The audit also
identifies why a scalar profile menu is insufficient: the reset spectrum
depends on the geometric gauge used to insert a child and on the resulting
cross-child pair directions.

## 1. Exhaustion and the exact Pareto optimum

For each of the `8^3=512` rooted chirotope words from
`TWO_DIRECTION_FOUR_POINT_WRAPPER_AUDIT.md`, split every pair direction by
the certified `10^-30` perturbation.  There are 182 oriented projection
orders, of which the assembly order and its reversal are excluded.  The
verifier evaluates all `512*180` reset records by the last-two-points cap/cup
DP and attaches the exact first-wrapper face count.

The number `20671` in (1) is the number of distinct `(C,U)` pairs.  It must
not be described as the number of full recurrence states: different words
can have the same pair and different `W`, leaving `42766` distinct triples.
A Fenwick minimum scan in increasing `(C,U,W)` order leaves exactly 575
coordinatewise-minimal triples.

For three size-14 child states `s_i=(c_i,u_i,w_i)`, the five-block
first-cap/last-cup recurrence, including the two singleton endpoints, is

\[
\begin{aligned}
\Phi(s_1,s_2,s_3)={}&3377+w_1+w_2+w_3+u_1+15u_2+225u_3\\
 &+c_1u_2+15c_1u_3+225c_1+c_2u_3+15c_2+c_3.          \tag{7}
\end{aligned}
\]

For fixed `s_1,s_2`, dependence on `s_3` is the line

\[
 (w_3+c_3)+(225+15c_1+c_2)u_3.                              \tag{8}
\]

The verifier builds the exact lower envelope of these integer lines and
queries it for all pairs of Pareto states.  This proves (2), rather than
assuming that the three attractive rows can be optimized independently.

The three minimizing rows have unique witnesses in the 512-word menu:

\[
\begin{array}{c|c|c|l}
\text{word}&\text{chamber}&(C,U,W)&\text{increasing point order}\\ \hline
(7,0,0)&43&(183,1975,1992)&5,6,7,8,9,10,11,12,13,4,3,2,1,0\\
(0,1,7)&11&(342,414,1986)&5,6,7,8,9,1,10,2,11,3,12,4,13,0\\
(7,0,0)&42&(1975,183,1992)&0,1,2,3,4,13,12,11,10,9,8,7,6,5.
\end{array}                                                  \tag{9}
\]

Chamber numbers refer to the deterministic enumeration in the verifier,
including both orientations.

## 2. Exact 44-point realization

For each witness in (9), recover a rational functional `f=x+s y` inducing
the displayed order and take the orientation-preserving transverse
functional `g=-s x+y`, with both signs reversed for the opposite oriented
chamber.  Independently normalize `f,g`, then apply a vertical rational
shear so every pair slope is positive.  This preserves the chosen
`(C,U,W)` state.

Starting with a singleton, strongly glue the three recharted children in
order, then glue a final singleton.  At every split `A prec B` the exact
coordinates satisfy

\[
 \chi(a_1,a_2,b)<0,\qquad \chi(a,b_1,b_2)>0,                 \tag{10}
\]

for every legal choice of points.  Hence

\[
\begin{aligned}
C(A\prec B)&=C(B)+(1+|B|)C(A),\\
U(A\prec B)&=U(A)+(1+|A|)U(B),\\
W(A\prec B)&=W(A)+W(B)+C(A)U(B).                    \tag{11}
\end{aligned}
\]

Iteration of (11) is exactly (7), so the resulting rational 44-point set
has `W=747670`; no claim that a nonlinear pocket map preserves an arbitrary
rotated middle chart is needed.  Its assembly endpoint profile is

\[
                         (C,U)=(103311,16109).                \tag{12}
\]

The chosen coordinates have 942 distinct unoriented pair directions and
therefore 1884 oriented generic projection chambers.  Enumerating every
one proves (4).  Among its 1880 distinct scalar profiles, 202 are
coordinatewise minimal; the two extreme useful rows are

\[
                  (15121,102449),\qquad(102449,15121).        \tag{13}
\]

## 3. The next menu rebounds

Apply the same exact five-block recurrence to three size-44 children, each
with face count `747670`, and allow every profile in the exhausted
44-point menu.  The optimum is (5), attained at

\[
 (15121,102449),\qquad(44728,21566),\qquad(102449,15121).
                                                                    \tag{14}
\]

Equation (6) is the useful finite conclusion: the best first reset does
not continue the observed downward trend at the very next scalar step.
The 134-point parent's own projection spectrum has not been exhausted, so
(5) is not a proof that all longer itineraries rebound.

## 4. Gauge dependence and the correct recursive state

The scalar count (7) is invariant under every exact realization of the
three strong splits, but the cyclic order of directions of **disjoint**
point pairs is not determined by the planar chirotope.  It can change when
the metric/aspect gauge changes through a parallel-pair event, without a
triple becoming collinear.  Consequently the projection profile menu is
not a function of `(C,U,W)`, or even of the abstract order type alone.

This is visible exactly.  Keeping all child and cross-block triple signs
but using a simple decimal sequence of strong-glue scales changes the
minimum in (4) to

\[
                       (18431,49408),                         \tag{15}
\]

while `W_2` and (12) remain unchanged.  There is further handedness freedom:
reflecting the first and third children, and selecting the reverse chamber
so that their assembly scalar rows remain exactly (3), gives another
legitimate 44-point strong comb with

\[
 \min C_\xi U_\xi=16699\cdot52138=870652462,
 \qquad \min\max(C_\xi,U_\xi)=37295.                         \tag{16}
\]

Thus (4) is a theorem about the fixed explicit realization, not a
direction-uniform invariant of the scalar menu.

For a single future reset, a paired state `Pi_2` records the assembly and
reset profiles, but not enough of the embedding.  The missing information
should **not** be described as an intrinsic `Pi_q` cross-ratio condition.
In a `q`-role wrapper there are `q` independent physical child copies.  At
that **one generation**, copy `i` needs only two marked directions: the
parent assembly direction pulls back to `xi_i`, and the selected parent
reset pulls back to `eta_i`.  The projective action on a direction line is
transitive on ordered pairs of distinct directions, and the sibling copies
can be recharted independently.  Thus a same-generation `Pi_q` requirement
is spurious.

What scalar `Pi_2` omits is the **decorated two-mark insertion state**:

\[
 ((C_{\xi},U_{\xi}),(C_{\eta},U_{\eta});
       \text{admissible seam gauge and pair-direction placement}). \tag{17}
\]

After all children are placed, the cross-child pair directions determine
the completed parent's allowable sequence and cannot be recovered from the
child scalar pairs.  Thus the parent spectrum must be recomputed from the
decorated realization.

Nor is a pathwise `Pi_h` automatically necessary.  A branching construction
may treat each completed parent as a new atom: it is built in one exported
chart, one reset chart is selected, and that ordered pair is transported at
the next edge.  Convex-face count is chart invariant, so profiles of old
descendants in the pullbacks of still later ancestor resets need not remain
target data.  In this atomic/export model a decorated two-mark transition is
recursively closed, although the completed geometry (or enough information
to recompute its next spectrum) remains part of the state.

A pathwise decorated `Pi_h`, with genuine cyclic/cross-ratio constraints,
is required only for an argument which simultaneously retains descendant
profiles from several ancestor resets, or for a node which exports a menu
of several nonconstruction charts.  Such marks can certainly arise in a
proof that expands every ancestor bank back to the same leaves, but they
must not be imposed on an existential recursive construction without that
retention hypothesis.  Thus the exact hierarchy is: scalar `Pi_2` is too
coarse; decorated two-mark geometry suffices for one exported edge; and
pathwise `Pi_h` is a conditional multi-export state, not a universal
requirement.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_pareto_two_level_recursive_menu.py
```

Expected output:

```text
PASS: reset (C,U) pairs=20671, (C,U,W) states=42766, Pareto=575, W2=747670; 44-point chambers=1884, min CU=907262375, Pareto profiles=202, W3=11358202734
```

The default run takes about 40 seconds.  It uses only exact `Fraction`
arithmetic and independently checks all menu records, the Pareto frontier,
the strong-glue construction, all 1884 parent chambers, and the next scalar
optimization.

For the slower exact checks of (15), all eight child-reflection choices,
and (16), run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_pareto_two_level_recursive_menu.py --gauges
```

## Scope

This artifact proves a two-level finite rebound and exposes the missing
coherent-spectrum state.  It neither proves a uniform lower bound for every
common-guard wrapper nor constructs a sub-half recursive family.  In
particular, no arbitrary-atom endpoint theorem and no claim that strong
separation supplies local endpoint profiles is used.
