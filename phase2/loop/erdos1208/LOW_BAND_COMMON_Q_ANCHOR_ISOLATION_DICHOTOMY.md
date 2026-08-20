# Exact common-q local gate: anchor-isolation dichotomy

## 1. Outcome

Fix one physical target wedge `w` and retain only its determinant-qualified
partner shifts which are target-rich.  The exact common-translation weight
from `LOW_BAND_COMMON_Q_WEDGE_RESTORATION.md` admits a lossless split

\[
 \boxed{
 F^Q_{<k,L,T}(w)
 \le I^Q_{L,T}(w)+2A^Q_{\rm head}(w)+2A^Q_{\rm tail}(w).} \tag{1.1}
\]

Here `I` counts source-pair/translation occurrences whose anchor is isolated
simultaneously at its directed head and tail inside that source pair's anchor
graph.  The two `A` terms count shared-head and shared-tail anchor wedges.
They have exact fibre-intersection expansions, so (1.1) preserves the scalar
predicate, the common translation, the target wedge, and the determinant
cutoff.

The shared-head switch therefore controls the entire nonisolated branch.
But the closure stress shows a decisive barrier: on the maximally weighted
rich physical wedge, between 72% and 84% of the exact weight is already
anchor-isolated for `k=20,30,40,50`.  At `k=50`, 496 of the total weight 662
comes from literal anchor matchings; only 159 comes from graphs with any
shared head or tail.  Thus the shared-head switch cannot prove the restored
local gate by itself.  The precise survivor is the isolated/matching mass
`I`, not an unspecified weighted intersection term.

This note does not disprove the desired bound

\[
 F^Q_{<k,L,T}(w)\le m^{o(1)}(H_Q/k+k^2).                \tag{1.2}
\]

The largest exact closure value currently audited is 7,252 at `k=100`,
while `H_Q/k+k^2=13,228.12`; hence the ratio is 0.548.  No genuine common-`q`
counterexample is known.  The contribution here is a rigorous reduction of
(1.2) to the anchor-isolated branch, plus an exact verifier showing that this
branch is genuinely dominant on the principal stress family.

## 2. The fixed-wedge selector

For a physical wedge

\[
 w=(x;\{x,a_1\},\{x,a_2\}),                              \tag{2.1}
\]

let `R_(L,T)(w)` be the set of shifts obtained from partner pairs
`(f_1,f_2)` satisfying

\[
\begin{aligned}
 \delta(f_1)-\delta(f_2)
   &=\delta(xa_1)-\delta(xa_2),\\
 |2\det(v_{xa_i},v_{f_i})|&>L\quad(i=1,2),\\
 U_L(\delta(xa_1)-\delta(f_1))&\ge T.
\end{aligned}                                           \tag{2.2}
\]

Distance-label injectivity implies that a fixed shift determines both
partner edges, so it occurs at most once in (2.2).  Define the selector on
ordered source pairs

\[
 V_w(s,t)=1_{\{- (\delta(s)-\delta(t))/18\in
                    R_{L,T}(w)\}},                       \tag{2.3}
\]

with value zero unless the quotient is a nonzero integer.  Then

\[
 \boxed{
 F^Q_{<k,L,T}(w)=
 \sum_{p=(s,t):c_Q(p)<k}c_Q(p)V_w(p).}                   \tag{2.4}
\]

Thus the fixed target geometry is now a zero-one predicate on source pairs;
all remaining multiplicity is genuinely the number of common clean
translations.

## 3. Anchor isolation

For a fixed ordered source pair `p`, represent every `q in Q_p` by its
unique directed anchor

\[
 q=a_q-b_q.                                               \tag{3.1}
\]

Let `d^+(a)` and `d^-(b)` be the directed head and tail degrees of this
anchor graph.  Put

\[
\begin{aligned}
 A_{\rm head}(p)&=\sum_a{d^+(a)\choose2},\\
 A_{\rm tail}(p)&=\sum_b{d^-(b)\choose2},                \tag{3.2}\\
 i(p)&=|\{q=a-b\in Q_p:d^+(a)=d^-(b)=1\}|.
\end{aligned}
\]

Every anchor edge not counted by `i(p)` is incident, at its head or tail,
to another edge of the same directed degree type.  For every integer `d>=2`,

\[
 d\le2{d\choose2}.                                      \tag{3.3}
\]

Charging each nonisolated edge at one offending endpoint gives

\[
 \boxed{
 c_Q(p)\le i(p)+2A_{\rm head}(p)+2A_{\rm tail}(p).}      \tag{3.4}
\]

Multiplying by the zero-one weight (2.3) and summing proves (1.1), where

\[
\begin{aligned}
 I^Q_{L,T}(w)&=\sum_pV_w(p)i(p),\\
 A^Q_{\rm head}(w)&=\sum_pV_w(p)A_{\rm head}(p),\\
 A^Q_{\rm tail}(w)&=\sum_pV_w(p)A_{\rm tail}(p).
\end{aligned}                                           \tag{3.5}
\]

This elementary split is sharp on a literal directed matching, where
`i(p)=c_Q(p)` and both wedge counts vanish.  The polynomial-height matching
construction in `LOW_CODEGREE_ANCHOR_MATCHING_TWO_SCALE_BARRIER.md` shows
that this equality case is genuinely realizable with `c_Q(p)=Theta(k)`.

## 4. Exact shared-head and shared-tail expansions

For distinct `a,b,c`, put

\[
 q_1=a-b,\qquad q_2=a-c,qquad
 \mathcal I(a;b,c)=H_{q_1}\cap H_{q_2}.                 \tag{4.1}
\]

Switching the order of summation, without applying the geometric closure
map, gives the exact weighted identity

\[
 \boxed{
 A^Q_{\rm head}(w)=
 \sum_a\sum_{\{b,c\}\subset A\setminus\{a\}}
 \sum_{\substack{s,t\in\mathcal I(a;b,c)\\s\ne t}}
 V_w(s,t),}                                             \tag{4.2}
\]

where only `q_1,q_2 in Q` are retained.  The tail identity is the same with
`q_1=b-a,q_2=c-a`.  Every orientation of `(s,t)` is retained in (4.2).

This is the point at which the shared-head theorem applies.  Dropping the
selector gives the rigorous unweighted upper

\[
 A^Q_{\rm head}(w)
 \le\frac12\sum_{a,b,c}J(a;b,c)(J(a;b,c)-1),             \tag{4.3}
\]

and the existing intersection switch bounds the right side by its explicit
`R_head/2` moment.  More importantly, (4.2) identifies the exact weighted
object a stronger switch would have to control.

The known nonexceptional switch sends one start to
`s+a-c`.  Squared edge length is not invariant under this pair-sum
translation, so `V_w(s,t)` is not preserved.  Applying the unweighted switch
after (4.2) therefore loses the scalar localization.  This is a rigorous
reason the shared-head theorem stops at the nonisolated reduction rather
than proving (1.2).

## 5. What remains after the switch

An anchor counted by `i(p)` has a unique head and a unique tail among the
translations common to that source pair.  This is weaker than a literal
underlying matching: another anchor may use its head as a tail.  Moreover,
an isolated anchor can be a separate component of a graph which also has a
shared-head star elsewhere.  It is therefore useful to distinguish three
stress classes without claiming that they partition `I` itself:

1. source pairs whose whole anchor graph is a literal underlying matching;
2. source pairs with no shared head or tail but with cross-oriented endpoint
   contacts, hence directed paths/cycles; and
3. graphs having a shared head or tail, which may still contain some isolated
   anchor occurrences.

The existing fixed-first/fixed-second anchor lemmas make the clean target
edges disjoint along a literal matching, but do not reduce its scalar
weight.  A genuine matching can carry `Theta(k)` translations for one
source pair.  Hence the next theorem must aggregate matching records over
many scalar-selected source pairs, or exploit the two clean target roles of
each isolated record.  Another shared-head moment cannot see them.

## 6. Exact closure stress

For each prefix, the verifier chooses the physical wedge of maximum exact
rich weight at cutoff `L=floor(N/k)` and threshold `T=k`.  It reports

\[
 (F_{\max},\ I,\ F_{\max}-I,\ A_{\rm head},\ A_{\rm tail},
   F_{\rm literal\ match},F_{\rm cross-only},F_{\rm head/tail}). \tag{6.1}
\]

\[
\begin{array}{c|rrrrrrrr}
k&F_{\max}&I&F-I&A_h&A_t&F_{\rm match}&F_{\rm cross}&F_{h/t}\\ \hline
20&10&8&2&1&0&8&0&2\\
30&69&57&12&6&0&56&0&13\\
40&312&224&88&44&0&210&5&97\\
50&662&523&139&72&2&496&7&159
\end{array}                                               \tag{6.2}
\]

In every row the inequality `F-I<=2(A_h+A_t)` is checked exactly.  The
verifier also computes (4.2) independently from fibre intersections and
requires equality with the anchor-graph count.

The larger direct profiles, whose full physical-wedge enumeration is slower,
are

\[
\begin{array}{c|r|r|r|c}
k&H_Q&F_{\max}&H_Q/k+k^2&F_{\max}/(H_Q/k+k^2)\\ \hline
60&49734&1218&4428.9&0.275\\
80&136134&3220&8101.675&0.397\\
100&322812&7252&13228.12&0.548
\end{array}                                               \tag{6.3}
\]

The ratio is increasing, so the local gate is not proved by finite data;
but it remains below one through the complete 100-point audit.

Run

```text
PYTHONPATH=phase2/loop/erdos1208 \
python3 phase2/loop/erdos1208/verify_low_band_common_q_anchor_isolation.py
```

## 7. Verdict

The determinant-cell cap and shared-head switch do not yet prove the full
local gate.  They give a durable exact reduction:

* fixed source determinant cells have weight at most `m^(o(1))k`;
* every nonisolated anchor occurrence is paid by a shared-head or shared-tail
  fibre-intersection record through (1.1)--(4.2); and
* the dominant survivor is an anchor-isolated, overwhelmingly literal-
  matching mass.

A full proof must now bound `I^Q_(L,T)(w)` at scale
`m^(o(1))(H_Q/k+k^2)`, or construct a common-`q` family in which many
matching-like source pairs align with one determinant-rich target wedge.
The known matching planting supplies only one such pair and stays a factor
`k` below the permitted `k^2` local scale.
