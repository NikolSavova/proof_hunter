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

## 3. Nested-threshold uncrossing also fails

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
                         0>3>1>2.                         \tag{12}
\]

For caps starting at zero, the induced set \(\{0,3\}\) has the two-vertex
cap \((0,3)\). In the full set, however, the unique maximum cap is
\((0,1,2)\). Its intersection with \(\{0,3\}\) is only \(\{0\}\). Therefore
no full maximum cap is simultaneously maximum at both thresholds.

This kills the literal layer-cake interchange

\[
 \max_P\int |P\cap S_t|\,dt
 \stackrel{?}{=}\int\max_P|P\cap S_t|\,dt.               \tag{13}
\]

Any proof of (ASM) must average or charge witness switches; it cannot make
all induced longest paths nested.

## 4. Finite evidence for the surviving target

The verifier checks (ASM), and hence (SM), for:

1. all \(720\) orders of the six edges at arity four and all \(5^4\) child
   vectors from \(\{1,2,4,16,1024\}\);
2. every one of the 62 reflection-order commutation classes at arity five
   and all \(7^5\) power-of-two child vectors with exponents
   \(0,\ldots,6\);
3. the exact counterexample (1), where (WH) fails but (ASM) and (SM) hold.

The first two items are exhaustive finite regressions over the displayed
menus, not a proof for arbitrary weights. Separate evolutionary searches
over arbitrary edge orders through arity \(16\) and fixed-coordinate
stretchable orders through arity \(16\) also found no violation of (ASM) or
(SM); those heuristic searches are not used as certificates.

## 5. Consequence for the heterogeneous program

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

## 6. Verification

Run

~~~bash
python3 phase2/loop/erdos838/agent_nonstrong_ramp_search/verify_weighted_hinge_counterexample.py
~~~

The current output is

~~~text
PASS: stretchable weighted-hinge counterexample; defect=(0.00803411434913715532,0.00803411434913715532); square_margin=(0.670913384686476894,0.670913384686476894); nested_threshold_counter=n4; average_square_arbitrary_n4=450000; average_square_reflection_n5=1042034
~~~

The verifier checks the integral realization, reflection word, determinant
margin, symbolic endpoint profiles, rational logarithmic certificates,
nested-threshold obstruction, and the two exhaustive menus above. The
counterexample and its two displayed margins are certified by exact integer
and rational arithmetic. The finite-menu (ASM) regressions use binary64
logarithms with a \(10^{-10}\) comparison tolerance and remain evidence,
not proof.
