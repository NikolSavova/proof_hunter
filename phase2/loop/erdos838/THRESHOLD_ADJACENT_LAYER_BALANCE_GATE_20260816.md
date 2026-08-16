# Near-threshold adjacent-layer balance: a one-lemma coefficient gate

**Date:** 2026-08-16. All logarithms are base two.

## Verdict

For a planar point set $P$, let $v_j(P)$ be the number of its $j$-point
subsets in convex position.  Fix once and for all a **certified upper-bound
sequence**

\[
        ES(j+1)\le q_j=2^{j+o(j)}.                              \tag{1}
\]

The following near-threshold statement at those particular sizes would
already improve the unconditional lower coefficient in Erd\H{o}s 838.

> **Adjacent-layer balance target.**  There are a constant
> $\lambda<1$ such that every $q_j$-point set $Q$ in general position
> satisfies
> \[
>             v_j(Q)\le 2^{(\lambda+o(1))j}v_{j+1}(Q).             \tag{2}
> \]

The $o(j)$ terms are uniform in $Q$.  One may take $q_j$ to be any one
explicit currently known upper bound for $ES(j+1)$, so the right side of
(2) is nonzero.  If (2) holds, then for every fixed $0<\alpha<1$ the unrestricted
coefficient is at least

\[
 \boxed{
 {1\over4}+{(1-\lambda)(1-\alpha^2)\over8}>{1\over4}.}            \tag{3}
\]

Thus (2) is a single, quantitative geometric lemma with a direct route to
a publishable gain.  It is not proved here.  This note proves the reduction,
gives its exact coefficient, and records the main construction stress tests.

The target has a sharp kill criterion only **after the sampling sequence is
fixed**: a stretchable sequence $Q_j$ with $|Q_j|=q_j$ and

\[
        \log {v_j(Q_j)\over v_{j+1}(Q_j)}\ge(1-o(1))j             \tag{4}
\]

would kill it.  A counterexample at some other size
$2^{j+o(j)}$ does not refute the existential choice of $q_j$.  This
quantifier distinction is essential; Section 3.3 gives an exact scalable
family showing that the uniform-in-size version is dramatically false.

## 1. The exact averaging theorem

The reduction does not use any geometric structure beyond the hypothesis
(2).

**Theorem 1.**  Let $j<q\le N$.  If every induced $q$-point subset $Q$ of
an $N$-point set $P$ satisfies

\[
                         v_j(Q)\le L_jv_{j+1}(Q),                 \tag{5}
\]

then

\[
 {v_{j+1}(P)\over v_j(P)}
       \ge {N-j\over L_j(q-j)},                                  \tag{6}
\]

and, for the convex-set densities
$p_i(P)=v_i(P)/\binom Ni$,

\[
 \boxed{
 {p_{j+1}(P)\over p_j(P)}
       \ge {j+1\over L_j(q-j)}.}                                 \tag{7}
\]

**Proof.**  Sum (5) over all $q$-subsets of $P$.  Every convex $j$-set is
counted $\binom{N-j}{q-j}$ times and every convex $(j+1)$-set is counted
$\binom{N-j-1}{q-j-1}$ times.  Therefore

\[
 v_j(P)\binom{N-j}{q-j}
 \le L_jv_{j+1}(P)\binom{N-j-1}{q-j-1}.
\]

The quotient of the two binomial coefficients is $(N-j)/(q-j)$, proving
(6).  Multiplying (6) by $(j+1)/(N-j)$ proves (7). $\square$

Now take $q=q_j=2^{j+o(j)}$ and
$L_j=2^{\lambda j+o(j)}$.  Equation (7) gives, uniformly for
$\alpha k\le j<k$,

\[
             {p_{j+1}\over p_j}\ge
             2^{-(1+\lambda)j-o(k)}.                             \tag{8}
\]

The successive-rank gate in
`SUCCESSIVE_RANK_DENSITY_GAIN_GATE_20260816.md` therefore applies with

\[
                         c=1+\lambda<2.                           \tag{9}
\]

Its gain parameter is

\[
 \eta=(1-c/2)(1-\alpha^2)
      ={1-\lambda\over2}(1-\alpha^2),                            \tag{10}
\]

and the fixed-size bridge gives (3).

Notice that subexponential balance, $L_j=2^{o(j)}$, would give $c=1$.
It is more than is needed: **any exponential balance exponent strictly
below one suffices.**

## 2. Why this is the right threshold formulation

The exact no-slack inequality

\[
 p_{j+1}\ge2^{-j}p_j                                      \tag{11}
\]

is false at $N=2^j$.  The rational double chain with eight points on each
side has

\[
          (v_4,v_5)=(924,112),\qquad {p_5\over p_4}={5\over99}
          <{1\over16}.                                           \tag{12}
\]

This does not threaten (2): it is a constant loss at one finite row.  For
the double chain with $m$ points on each side,

\[
 v_4=2\binom m4+\binom m2^2,qquad
 v_j=2\binom mj\quad(j\ge5).                                    \tag{13}
\]

Consequently, at the genuine growing threshold $m=2^{j-1}$ and $j\ge5$,

\[
 {v_j\over v_{j+1}}={j+1\over m-j}=2^{-j+O(\log j)},             \tag{14}
\]

which is far stronger than (2).

At the other extreme, heredity alone cannot prove (2).  An abstract
simplicial complex may contain every subset of size at most $j$ and only
one face of size $j+1$.  On $q=2^j$ vertices this has
$v_j/v_{j+1}=\binom qj=2^{\Theta(j^2)}$.  The missing input must therefore
use planar signed circuit elimination or an equivalent order-type fact.

## 3. Exact construction stress tests

The balance target survives the campaign's main low-face geometries.

### 3.1 Central Pascal cells

For the classical central Erdos--Szekeres cell

\[
             T(2h-4,h-2),\qquad
             q=\binom{2h-4}{h-2}=2^{2h-O(\log h)},                \tag{15}
\]

the near-threshold rank is $j=2h-5$.  The exact graded recurrence gives

\[
 {v_j\over v_{j+1}}=
 2.0132,\ 1.6588,\ 1.1349,\ 0.8458,\ 0.3787,\ 0.1488       \tag{16}
\]

at $h=5,6,8,10,20,50$, respectively.  In particular the ratio is bounded,
not $2^{(1-o(1))j}$.

### 3.2 Alternating combs

For the exact ordered alternating comb on $N=2^j$ leaves, the ratios
$v_j/v_{j+1}$ for $4\le j\le10$ decrease from $1.0769$ to $0.0219$.
The construction that killed the naive shifted caterpillar constant is
therefore harmless for adjacent-layer balance.

### 3.3 Exact size-sensitivity barrier

The phrase $2^{j+o(j)}$ cannot be treated as an interchangeable size
window.  Put $j=2h-4$, and let

\[
             P_h=T(2h-4,h-2)
\]

be the central Pascal cell.  At its top rank $j$, its ordinary faces split
at the top seam into a maximum cap of the left child and a maximum cup of
the right child.  If $a_h$ is either one-sided count, then

\[
                         v_j(P_h)=a_h^2.                         \tag{17}
\]

There is a rational one-point extension $P_h^+$ with the following exact
property.  Recursively follow the right child of the left Pascal child down
to the strict-cap boundary, append one point there, and rebuild all strong
seams.  The induced old configuration is $P_h$, while the new point lies in
exactly one promoted maximum cap.  Consequently

\[
 v_{j+1}(P_h^+)=a_h,
 \qquad
 v_j(P_h^+)\ge a_h^2,
 \qquad
 {v_j(P_h^+)\over v_{j+1}(P_h^+)}\ge a_h.             \tag{18}
\]

This is an exact stretchable construction, not a scalar profile.  Its size
is

\[
 |P_h^+|=\binom{j}{j/2}+1=2^{j-o(j)}.                 \tag{19}
\]

For completeness, let $t(m,i)$ be the number of maximum caps in
$T(m,i)$.  The Pascal recurrence gives

\[
 t(m,i)=\binom{m-1}{i}t(m-1,i-1)+t(m-1,i),            \tag{20}
\]

with the evident boundary values, and $a_h=t(2h-5,h-3)$.  Following only
the first summand for the first half of the recursion gives

\[
 a_h\ge 2^{(h-3)^2/4-O(h)}=2^{\Omega(j^2)}.           \tag{21}
\]

Thus (2) is false by a quadratic-exponential margin at another perfectly
valid size $2^{j+o(j)}$.  What remains live is only the statement at the
fixed certified upper sequence in (1).  Any proof must quantitatively use
the extra oversaturation between (19) and that sequence; an argument that
uses only $\log q_j=j+o(j)$ cannot distinguish the two and therefore cannot
work.

The first exact rows are

\[
\begin{array}{c|c|c|c}
h&j&a_h&v_j(P_h^+)/v_{j+1}(P_h^+)\\ \hline
4&4&3&7\\
5&6&46&2713/46\\
6&8&3421&12410783/3421.
\end{array}                                             \tag{22}
\]

### 3.4 The obvious oversaturation padding repairs the cliff

The barrier above cannot simply be enlarged by replacing one of its
singleton leaves with a much larger low-face child.  This is not a theorem
for arbitrary padding, but there is a useful exact stress test.

For every physical leaf of $P_h^+$, replace that leaf by the central Pascal
child

\[
                 T(2h+4,h+2).
\]

The substituted child has $2^{j+O(\log j)}$ points, so the resulting set is
on the oversaturated side of the same exponential scale in the tested
rows.  The verifier performs the exact graded strong-glue substitution at
**every** leaf for $4\le h\le8$, a total of $1277$ distinct substitutions.
In every case

\[
                    {v_j\over v_{j+1}}<1,               \tag{23}
\]

and the largest observed ratio is less than $0.0112$.  Thus the new child's
mixed $(j+1)$-layer does not merely weaken the cap-promotion cliff; it
overwhelms it in all tested rows.

Equation (23) is finite evidence only.  Its value is diagnostic: a proof at
the certified sequence should try to formalize precisely this phenomenon,
namely that the extra support required to move from (19) to the certified
threshold must create enough mixed extensions.  A size-only embedding of
the cap-promoted core is not a counterexample.

### 3.5 Asymmetric padding shows the same threshold split

The symmetric substitution above might conceal the real obstruction: the
new child could have a large cap profile exactly where the promoted core
needs it.  The verifier therefore also glues **every** Pascal cell
$T(m,i)$ in a finite triangle to the left of the promoted core.  These
include strongly asymmetric cells whose facing cap rank is much smaller
than their cup rank.

For $4\le h\le12$, $j=2h-4$, and $1\le m<2j+12$, it exhausts every
$0\le i\le m$ for which the resulting support has the exact integer lower
bound

\[
                       |T(m,i)\prec P_h^+|
                         \ge 2^{j+\lfloor\sqrt j\rfloor}.       \tag{24}
\]

Every one of these exact graded substitutions satisfies

\[
                         v_j<v_{j+1}.                           \tag{25}
\]

The largest ratio in the whole finite audit is reported by the verifier.
Below (24), asymmetric paddings can preserve or amplify the original
cliff.  Thus the experiment separates the two regimes in the direction
needed by (2): the dangerous profile is real, but in this construction
class it disappears precisely after genuine oversaturation.

Again, (25) is a finite construction audit, not a theorem about arbitrary
point sets.  It motivates a more economical target than a size-blind
extension bound: a proof should charge a large $j$-face basin either to
support below the certified threshold or to mixed extensions created by
the extra support.

### 3.6 What the tests do not prove

The internal-layer checks exclude the currently known recursive and
threshold obstructions at the selected rows.  They do not imply (2) for
arbitrary planar point sets.  The cap-promoted family shows in addition
that the exact sampling size, not merely its leading exponent, must enter.

There is already an exact warning inside the strong-decomposition class.
Exhausting every ordered binary strong tree on nine leaves gives

\[
             \max {v_4\over v_5}=66,
             \qquad (v_4,v_5)=(66,1)\text{ at a maximizer}.      \tag{26}
\]

Thus the bare threshold information $v_{j+1}>0$ is wholly insufficient,
even in a recursively structured planar class.  The conjectural content
is an **oversaturation theorem** at the particular sequence $q_j$ in
(1).  A proof must use the quantitative gap between a forcing threshold
and $q_j$; if that gap is not present in the chosen upper-bound sequence,
then (2) needs a different formulation.

In particular, fixed-$j$ supersaturation theorems do not provide uniform
constants when $j\to\infty$, and the scalar weighted-polygon identities
admit fake truncated rank shelves.  A proof must use genuine cross-rank
geometry.

## 4. The remaining geometric problem

For a convex $j$-set $A$ and a point $x\notin A$, the hull of $A\cup\{x\}$
hides a contiguous chain of vertices of $A$.

- If no vertex is hidden, $A\cup\{x\}$ is a convex $(j+1)$-set.
- If one vertex is hidden, replacing it by $x$ gives another convex
  $j$-set whose hull has strictly changed.
- If two or more vertices are hidden, the operation falls to a lower-rank
  trace.

The plausible route to (2) is a bounded-congestion routing theorem for
this extension/flip graph: either enough incidences extend directly to
rank $j+1$, or repeated one-hidden-vertex flips expose a large pocket whose
lower-rank faces pay for the basin.  The present missing statement is a
strict $2^j$ saving in the maximum basin size.  A bound
$2^{(1-\varepsilon)j+o(j)}$ for any fixed $\varepsilon>0$ would suffice.

This is the campaign's active Stage-C lemma **at a fixed certified sequence
$q_j$**.  If the hull-flip analysis
requires another quantitatively equivalent conjecture without a saving,
the branch should be parked rather than renamed.

## 5. Verification

Run

~~~text
python3 phase2/loop/erdos838/verify_threshold_adjacent_layer_balance.py
~~~

The verifier checks Theorem 1's binomial multiplicities and coefficient
algebra with exact rational arithmetic; reconstructs the rational
double-chain formulas; evaluates the exact graded central-Pascal profiles
through $h=50$; checks the alternating comb through $1024$ leaves; and
reconstructs the cap-promoted Pascal extension and recurrence through
$h=20$, including exact rational coordinates in the first nontrivial row.
It also substitutes an oversaturated central-Pascal child at every physical
leaf in the five rows $4\le h\le8$ and checks (23) exactly.
It exhausts all ordered binary strong trees on nine leaves and checks the
bare-threshold cliff (26).
It verifies the reduction and the stated regressions, not the conjectural
balance inequality (2) at the certified upper sequence.
