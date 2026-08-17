# Weighted hinge is false; the square mesh survives

**Date:** 2026-08-15. All logarithms are base two. This note does not edit
the master attack.

## Verdict

The weighted-hinge conjecture

\[
 \sum_i p_iR_i\geq\sum_i p_i\ell_i\Delta_i,
 \qquad
 p_i={n_i\over N},\quad \ell_i=\log n_i,\quad
 \Delta_i=\log{N\over n_i},                              \tag{WH}
\]

is false for a generic, integral, stretchable five-point chart. The
counterexample has only two child scales:

\[
                       (n_0,n_1,n_2,n_3,n_4)
                       =(4250,1000,1000,1000,1000).        \tag{1}
\]

Its rigorously certified defect is

\[
 \sum_i p_i\ell_i\Delta_i-\sum_i p_iR_i
 \in(0.00803,0.00804).                                   \tag{2}
\]

Thus neither ordinary hinged Kraft nor the exact weighted predecessor
forests force zero average defect. The failure is not a nonstretchable
edge-order artifact.

The same node satisfies the proposed square-mesh inequality

\[
 \max_i\left\{{1\over2}\ell_i^2+R_i\right\}
 \geq {1\over2}(\log N)^2-{1\over2}(\log m)^2             \tag{SM}
\]

with margin greater than \(0.67\). Hence (WH) is strictly stronger than the
local statement actually needed for the \(q^2\)-loss Bellman step.

A useful averaged target also survives every regression:

\[
 \boxed{
 \sum_i p_i\left({1\over2}\ell_i^2+R_i\right)
 \geq {1\over2}(\log N)^2-{1\over2}(\log m)^2.}           \tag{ASM}
\]

It implies (SM) immediately and is equivalent to the weakened hinge bound

\[
 \sum_i p_iR_i-\sum_i p_i\ell_i\Delta_i
 \geq {1\over2}\left(\sum_i p_i\Delta_i^2-(\log m)^2\right).
                                                                    \tag{3}
\]

This report records (ASM) as a conjecture, not a theorem. It isolates a
plausible proof target that remains valid after (WH) fails and explicitly
credits the information-variance term that the false entropy surrogate
discarded.

There is now a proved approximate substitute.  If \(B\) is the number of
nonempty dyadic child-size buckets, then every row satisfies

\[
 \boxed{
 \max_i\left\{\frac12\ell_i^2+R_i\right\}
 \geq
 \frac12\bigl(L-1-\log B\bigr)_+^2
 -\frac12(\log m)^2.}                                  \tag{3a}
\]

Thus the exact square mesh loses at most \(O(L\log B)\).  Since
\(B\leq\min\{m,1+\lfloor L\rfloor\}\), the loss is
\(O(L\log L)\) at an arbitrary single node.  This is enough for every
bounded-depth or macroscopic-jump application, but it can accumulate
quadratically along a long heterogeneous path.  Consequently (3a) is a
real partial closure of the local gate, not a proof of (SM) or (ASM).

There is a stronger closure when every row is size-balanced.  If

\[
                  \max_i n_i\leq2\min_i n_i,
\]

then the averaged square inequality holds with only the explicit row loss

\[
 \boxed{
 \sum_i p_i\left(\frac12\ell_i^2+R_i\right)
 \geq\frac12L^2-\frac12q^2-q,
 \qquad q=\log m.}                                      \tag{3b}
\]

Consequently, in an arbitrary-depth heterogeneous substitution tree whose
siblings are factor-two balanced, the exact same-target endpoint recurrence
and a same-chart final splice give

\[
 \boxed{
 \log V\geq\frac12L^2-(q_*+2)L,
 \qquad q_*:=\max_v\log m_v.}                            \tag{3c}
\]

Thus factor-two heterogeneity, arbitrary changing charts, and arbitrary
depth still cannot produce a sub-half construction when
\(q_*=o(L)\).  The remaining construction-side escape must contain either
a macroscopic-arity row, an unbounded sibling-size ratio, a failure of the
same-target endpoint recurrence, or a failure of the final splice.

The factor-two assumption can be weakened by a full polynomial range.  Fix
\(\delta>0\).  If every row with \(m\) children satisfies

\[
 {\max_i n_i\over\min_i n_i}\le m^{1-\delta},
\]

then the same recursion obeys

\[
 \boxed{
 \log V\geq {1\over2}L^2-
 {3/2-\delta\over\delta}\,q_*L.}                       \tag{3d}
\]

It still has coefficient at least one half whenever \(q_*=o(L)\).  Thus a
surviving bounded-row construction needs near-total scale separation: on
some relevant rows the largest/smallest ratio is \(m^{1-o(1)}\), not merely
a large constant or a fixed power below \(m\).

## 1. Exact stretchable counterexample

Take the five points

~~~text
(0,    -3)
(1, -9003)
(2, -8003)
(3, -9003)
(4,    -2).
~~~

All ten slopes are distinct, every triple determinant is nonzero, and the
minimum absolute triple determinant is \(2000\). Their increasing slope
order is

~~~text
01 02 03 23 13 04 12 14 24 34.
~~~

It is the reflection root sequence of the reduced word

~~~text
0 1 2 1 0 3 1 2 1 0.
~~~

Put

\[
             a=\log4250,\quad b=\log1000,\quad
             c=\log4251,\quad d=\log1001.                 \tag{4}
\]

The weighted endpoint sweep, with a sibling of size \(n_j\) contributing
\(\log(1+n_j)\), gives

\[
 \begin{aligned}
 A&=(d,2d,d,d,0),\\
 B&=(0,c,c+d,c+d,c+2d),\\
 R&=(d,c+2d,c+2d,c+2d,c+2d).
 \end{aligned}                                           \tag{5}
\]

Since \(N=8250\), exact substitution into (WH) gives

\[
 \begin{aligned}
 \sum_i p_iR_i
   &={4250d+4000(c+2d)\over8250},\\
 \sum_i p_i\ell_i\Delta_i
   &={4250a\log(33/17)+4000b\log(33/4)\over8250}.
                                                               \tag{6}
 \end{aligned}
\]

The verifier bounds every logarithm by a rational interval and proves
(2). In particular, no floating-point decision enters the counterexample.

The large child already violates the pointwise hinge inequality:

\[
                   R_0=d<a\log(33/17)=\ell_0\Delta_0.      \tag{7}
\]

The four smaller children have enough surplus that the average failure is
small, but not enough to cancel (7).

## 2. Why the square mesh is not killed

At the large child, the left side of (SM) is at least

\[
                         {1\over2}a^2+d.                   \tag{8}
\]

The target is

\[
                         {1\over2}(\log8250)^2
                         -{1\over2}(\log5)^2.              \tag{9}
\]

Rational interval arithmetic certifies that (8) minus (9) exceeds
\(0.67\). Algebraically, testing a child \(i\) in (SM) asks only for

\[
 R_i\geq \ell_i\Delta_i
       +{1\over2}\left(\Delta_i^2-(\log m)^2\right).       \tag{10}
\]

For a heavy child, \(\Delta_i\leq\log m\), so (10) permits a genuine hinge
defect. Here that negative square correction absorbs the failure in (7).
This is why a proof of (ASM) or (SM) need not repair (WH).

The averaged identity behind (3) is

\[
 \sum_i p_i\left({1\over2}\ell_i^2+R_i\right)
 ={1\over2}(\log N)^2-{1\over2}\sum_i p_i\Delta_i^2
  +\sum_i p_i(R_i-\ell_i\Delta_i).                       \tag{11}
\]

Thus the exact second moment supplies precisely the slack missing from
zero-defect weighted hinge.

## 3. Proved dyadic-bucket square mesh

For every integer \(t\geq0\), put

\[
 I_t=\{i:2^t\leq n_i<2^{t+1}\},\qquad
 s_t=|I_t|,\qquad a_t=\log s_t,                         \tag{14}
\]

and omit empty buckets.  Restrict the ordered macro to \(I_t\).  The exact
hinged Kraft theorem in HINGED_DIAGONAL_FLOOR_LOG.md supplies a position
\(i\in I_t\) whose induced cap-start and cup-end lengths have sum at least
\(\lceil a_t\rceil\).  These paths remain valid in the full macro.  Every
nonanchor vertex on them has

\[
                         \log(1+n_j)\geq t,              \tag{15}
\]

so

\[
                         R_i\geq t a_t,\qquad \ell_i\geq t.
                                                                  \tag{16}
\]

It follows that

\[
 \frac12\ell_i^2+R_i
 \geq\frac12t^2+ta_t
 =\frac12(t+a_t)^2-\frac12a_t^2
 \geq\frac12(t+a_t)^2-\frac12(\log m)^2.                \tag{17}
\]

Let \(B=|\{t:s_t>0\}|\) and \(X=\max_t(t+a_t)\).  The bucket definition
gives

\[
 N=\sum_i n_i
 <2\sum_t s_t2^t
 \leq2B\,2^X.                                           \tag{18}
\]

Therefore \(X\geq L-1-\log B\).  Select a bucket attaining \(X\) in
(17); replacing a negative lower bound for \(X\) by zero proves (3a).
The bounds on \(B\) are immediate from \(B\leq m\) and
\(0\leq t\leq\lfloor L\rfloor\).

The proof deliberately chooses only one size scale.  Its
\(\log B\) loss is precisely the price of not aligning the maximizing
endpoint paths across different thresholds.  The four-point obstruction
below shows why that alignment cannot simply be imposed.

## 4. Bounded-range rows and the global telescope

Suppose that \(D\leq n_i\leq2D\) for all \(i\), and put
\(t=\log D\), \(q=\log m\).  Let

\[
                    h_i=\alpha(i)+\beta(i)               \tag{19}
\]

be the exact hinged code length in the full row.  Every nonanchor sibling
used by either endpoint path has weight
\(\log(1+n_j)\geq t\), and therefore

\[
                         R_i\geq t h_i.                   \tag{20}
\]

The words of length \(h_i\) in the hinged Kraft theorem are prefix-free.
Shannon's source-coding inequality, applied with probabilities
\(p_i=n_i/N\), gives

\[
                    \sum_i p_i h_i\geq H(p),
 \qquad H(p)=\sum_i p_i\Delta_i.                         \tag{21}
\]

Write \(D_0=L-t\).  The size assumption gives
\(q\leq D_0\leq q+1\).  Combining (20)--(21) with
\(\ell_i=L-\Delta_i\) yields

\[
\begin{aligned}
 \sum_i p_i\left(\frac12\ell_i^2+R_i\right)
 &\geq\frac12L^2-D_0H(p)+\frac12\sum_i p_i\Delta_i^2\\
 &\geq\frac12L^2-D_0H(p)+\frac12H(p)^2.                 \tag{22}
\end{aligned}
\]

Since \(H(p)\leq q\) and \(D_0\leq q+1\), the quantity subtracted on
the last line is at most \(q^2/2+q\).  This proves (3b).  Notice that this
is a theorem about the actual weighted sibling rewards, not the false
anchor-weight surrogate ruled out in Section 1.

For completeness, consider a recursive endpoint tree.  At node \(v\), let
\(m_v\) be its number of children, \(q_v=\log m_v\), and choose a uniform
random physical leaf \(X\).  The endpoint recurrence

\[
                         E_v\geq E_{vi}+R_{v,i}           \tag{23}
\]

holds for every child \(i\), with both endpoint terms calling the same
child chart.  Inducting with (3b), or equivalently averaging (23) using the
conditional physical-leaf law, gives

\[
 E_{\rm root}\geq\frac12L^2-
   \mathbb E_X\sum_{v\prec X}\left(\frac12q_v^2+q_v\right).
                                                                  \tag{24}
\]

Factor-two balance implies

\[
 p_{v,\max}\leq\frac2{m_v+1},\qquad
 H(p_v)\geq\log\frac{m_v+1}{2}\geq\frac12q_v.           \tag{25}
\]

The entropy chain rule is exact:

\[
                    \mathbb E_X\sum_{v\prec X}H(p_v)=L. \tag{26}
\]

Hence \(\mathbb E\sum q_v\leq2L\), while
\(q_v^2\leq q_*q_v\).  Substitution into (24) proves
\(E_{\rm root}\geq L^2/2-(q_*+2)L\).  Under the same-chart final-splice
hypothesis, \(V\geq2^{E_{\rm root}}\), proving (3c).

This theorem includes arbitrary changing macros, order types, and chart
menus.  It does not assert that an arbitrary planar point set admits such a
tree.  Its role is construction-side: a surviving recursive half-boundary
candidate must generate genuinely broad sibling scales or a macroscopic
row, rather than merely replacing homogeneous children by mildly unequal
ones.

### Polynomial imbalance below the arity

The same calculation has a useful sharp extension.  Suppose now that

\[
                  D\le n_i\le RD,
 \qquad s=\log R.                                      \tag{27}
\]

The hinged code and reward bound (19)--(21) are unchanged.  This time

\[
       q\le D_0=\log(N/D)\le q+s,
\]

so (22) gives the row inequality

\[
 \boxed{
 \sum_i p_i\left({1\over2}\ell_i^2+R_i\right)
 \ge {1\over2}L^2-{1\over2}q^2-qs.}                  \tag{28}
\]

Indeed, \(H(p)\le q\), and the loss
\(D_0H(p)-H(p)^2/2\) is increasing for \(0\le H(p)\le q\), so it is at
most \(q^2/2+qs\).

Assume uniformly that \(R\le m^{1-\delta}\), hence
\(s\le(1-\delta)q\).  Also

\[
 p_{\max}\le {R\over R+m-1},
 \qquad
 H(p)\ge\log{1\over p_{\max}}
 \ge\delta q.                                         \tag{29}
\]

The last inequality is exact: \(R\le m^{1-\delta}\) and
\(m^{1-\delta}\ge1\) give

\[
 1+{m-1\over R}\ge m^\delta.
\]

Therefore the entropy chain rule (26) yields

\[
             \mathbb E\sum_{v\prec X}q_v\le {L\over\delta}.
                                                               \tag{30}
\]

The row loss in (28) is at most
\((3/2-\delta)q_v^2\), and \(q_v^2\le q_*q_v\).  Summing
(28) down the random address and applying (30) proves (3d).

The exponent \(1-\delta\) is the genuine boundary of this argument.  When
\(R\) is comparable with \(m\), (29) need not retain a fixed fraction of
the row entropy, and the number of such low-entropy rows is no longer
charged by the leaf entropy chain rule.  Thus the remaining imbalance gate
has been narrowed to a quantitatively explicit near-star regime.

## 5. Nested-threshold uncrossing also fails

A natural attempt to prove a weighted statement is to put
\(S_t=\{j:\ell_j\geq t\}\), choose a longest endpoint path in every induced
chart \(S_t\), and uncross those paths into one path realizing all layers.
This nesting lemma is false even for a four-point stretchable cap forest.

Take

~~~text
(0,  0)
(1, -1)
(2, -3)
(3,  0).
~~~

The increasing slope order is

~~~text
12 02 01 03 13 23,
~~~

the reflection sequence of \(1,0,1,2,1,0\). Order the weight layers by

\[
                         0>3>1>2.                         \tag{31}
\]

For caps starting at zero, the induced set \(\{0,3\}\) has the two-vertex
cap \((0,3)\). In the full set, however, the unique maximum cap is
\((0,1,2)\). Its intersection with \(\{0,3\}\) is only \(\{0\}\). Therefore
no full maximum cap is simultaneously maximum at both thresholds.

This kills the literal layer-cake interchange

\[
 \max_P\int |P\cap S_t|\,dt
 \stackrel{?}{=}\int\max_P|P\cap S_t|\,dt.               \tag{32}
\]

Any proof of (ASM) must average or charge witness switches; it cannot make
all induced longest paths nested.

## 6. Finite evidence for the surviving target

The verifier checks (ASM), and hence (SM), for:

1. all \(720\) orders of the six edges at arity four and all \(5^4\) child
   vectors from \(\{1,2,4,16,1024\}\);
2. every one of the 62 reflection-order commutation classes at arity five
   and all \(7^5\) power-of-two child vectors with exponents
   \(0,\ldots,6\);
3. the factor-two theorem on all 23,760 balanced arity-four rows and all
   11,594 balanced arity-five reflection rows occurring in those menus;
4. the exact counterexample (1), where (WH) fails but (ASM) and (SM) hold.

The first two items are exhaustive finite regressions over the displayed
menus, not a proof for arbitrary weights. Separate evolutionary searches
over arbitrary edge orders through arity \(16\) and fixed-coordinate
stretchable orders through arity \(16\) also found no violation of (ASM) or
(SM); those heuristic searches are not used as certificates.

## 7. Consequence for the heterogeneous program

The defect-free martingale route is closed: one must retain the signed local
defects in the exact theorem from the preceding report. The counterexample
shows that even reflection-order incidence can make their average positive.

The deterministic square route remains open. If (SM) holds at every node,
then a Bellman choice gives

\[
 E_v\geq {1\over2}(\log N_v)^2-{1\over2}(\log m_v)^2
\]

relative to the selected child's half-square bank. Iteration loses the sum
of \((\log m_v)^2/2\) along the chosen address, so a separate depth or
square-loss hypothesis is still required. The immediate local residue is
now (ASM)/(SM), not (WH).

## 8. Verification

Run

~~~bash
python3 phase2/loop/erdos838/agent_nonstrong_ramp_search/verify_weighted_hinge_counterexample.py
~~~

The current output is

~~~text
PASS: stretchable weighted-hinge counterexample; defect=(0.00803411434913715532,0.00803411434913715532); square_margin=(0.670913384686476894,0.670913384686476894); nested_threshold_counter=n4; dyadic_bucket_square=PASS; factor_two_telescope=PASS; average_square_arbitrary_n4=450000 (balanced=23760); average_square_reflection_n5=1042034 (balanced=11594)
~~~

The verifier checks the integral realization, reflection word, determinant
margin, symbolic endpoint profiles, rational logarithmic certificates,
nested-threshold obstruction, the factor-two entropy/telescope inequalities,
and the two exhaustive menus above. The
counterexample and its two displayed margins are certified by exact integer
and rational arithmetic. The finite-menu (ASM) regressions use binary64
logarithms with a \(10^{-10}\) comparison tolerance and remain evidence,
not proof.
