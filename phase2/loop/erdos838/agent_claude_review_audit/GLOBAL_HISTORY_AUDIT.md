# Global hinged-history compression: exact recurrence and current verdict

**Date:** 2026-08-13.  All logarithms are base two.  For an `x`-ordered
point set `P`, let `H_q(P)` be the number of `q`-point subsets
`x_1<...<x_q` such that, for every `i<=q-2`, all later points have the same
orientation with respect to `(x_i,x_{i+1})`.

The target inequality was

\[
 H_q(P)\le 2^{O(q\log q)}V(P).                                    \tag{1}
\]

The inequality is **false**.  The paper's six-point Pascal template, under
its own directional iteration, gives a rigorous quadratic separation
between `H_q` and `V` at `q=floor(log |P|)`.  Thus no choice of the hidden
constant in (1) works.  The same family also gives a small exact failure of
the natural `q! V(P)` strengthening.

## 1. Exact history substitution

Let `S[Q]` be the directional vertical composition from the paper.  Write
`h_Q(z)` for the generating polynomial of nonempty hinged subsets of `Q`,
and `c_Q(z)` for the cap polynomial.  Fix occupied template indices

\[
 I=(i_1<\cdots<i_j)
\]

and a bit vector `e=(e_1,...,e_j)`, where `e_s=1` means that the selected
part of block `i_s` has at least two points.  Call `(I,e)` admissible when,
for every `s<=j-2`,

\[
 \begin{cases}
 \chi_S(i_s,i_{s+1},i_t)\text{ is independent of }t>s+1,
      &e_{s+1}=0,\\
 \chi_S(i_s,i_{s+1},i_t)=+\text{ for every }t>s+1,
      &e_{s+1}=1.
 \end{cases}                                                       \tag{2}
\]

Put

\[
 C_0(z)=|Q|z,\quad C_1(z)=c_Q(z)-|Q|z,
 \qquad
 H_0(z)=|Q|z,\quad H_1(z)=h_Q(z)-|Q|z.                            \tag{3}
\]

> **Proposition 1 (exact hinged-profile recurrence).**
> \[
> h_{S[Q]}(z)=
> \sum_{(I,e)\text{ admissible}}
> \left(\prod_{s<j}C_{e_s}(z)\right)H_{e_j}(z).                   \tag{4}
> \]

**Proof.**  Consider a hinged subset meeting at least two blocks.  If a
nonfinal occupied block contains two selected points, those two points and
any later-block point form a mixed triple with negative sign.  Hence the
selected portion of every nonfinal block must be a cap.  The final block
has no future block to constrain it and can be an arbitrary hinged subset.

At a macro hinge `(i_s,i_{s+1})`, if block `i_{s+1}` is a singleton, only
future macro points are tested, giving the first line of (2).  If it has at
least two selected points, the next point inside that block already has
positive mixed orientation relative to the macro hinge, so every future
macro point must also have positive sign, giving the second line.  These
conditions are visibly sufficient as well.  Multiplying the independent
block choices and summing gives (4). `square`

This recurrence uses the full template order type, not just its cap/cup
profile, and is exact coefficient by coefficient.

## 2. The global inequality fails asymptotically

Take the six-point central Pascal template `S=T_{4,2}` and iterate the
directional composition:

\[
 Q_1=S,\qquad Q_d=S[Q_{d-1}].                                    \tag{5}
\]

Write `c_{d,k}` for the number of `k`-caps in `Q_d`.  The template cap
profile is `(6,15,10)`, so the exact profile version of the composition
identity gives

\[
 c_{Q_d}(z)=z\prod_{\ell=0}^{d-1}
 \left(6+15\,6^\ell z+10\,6^{2\ell}z^2\right).                   \tag{6}
\]

Taking the linear term in the last `k-1` factors and the constant term in
all preceding factors proves, whenever `1<=k<=d+1`,

\[
 c_{d,k}\ge
 6^{d-k+1}15^{k-1}
 6^{\sum_{\ell=d-k+1}^{d-1}\ell},                               \tag{7}
\]
and hence

\[
 \log c_{d,k}\ge kd\log6-O(k^2).                                \tag{8}
\]

There is an especially simple consequence of Proposition 1.  Fix any two
template blocks, the first to the left of the second.  The union of a cap
of size `k` in the first block and a hinged history of size `l` in the
second block is hinged.  Therefore

\[
 H_{k+l}(Q_d)\ge c_{d-1,k}H_l(Q_{d-1}).                           \tag{9}
\]

> **Theorem 2 (quadratic global-history obstruction).**  Put
> `q_d=floor(d log 6)`.  Then
> \[
>  \log H_{q_d}(Q_d)
>   =(\log6)^2d^2+O(d^{3/2}),                                    \tag{10}
> \]
> while
> \[
>  \log V(Q_d)=2(\log6)d^2+O(d).                                 \tag{11}
> \]
> Consequently, for every constant `C`, all sufficiently large `d` satisfy
> \[
> H_{q_d}(Q_d)>2^{Cq_d\log q_d}V(Q_d).                            \tag{12}
> \]

**Proof.**  Let `M=floor(sqrt d)` and distribute `q_d-1` as evenly as
possible among positive integers `k_1,...,k_M`.  For large `d`, every
`k_i>=2` and `k_i<=d-i+1`.  Apply (9) at the top `M` levels, always
continuing in the second block, and finish with an arbitrary singleton in
`Q_{d-M}`.  This constructs distinct histories and gives

\[
 H_{q_d}(Q_d)\ge 6^{d-M}\prod_{i=1}^M c_{d-i,k_i}.                \tag{13}
\]

By (8), `sum k_i=q_d-1`, and balancedness,

\[
\begin{aligned}
 \log H_{q_d}(Q_d)
 &\ge \log6\sum_{i=1}^M k_i(d-i)-O\left(\sum_i k_i^2+d\right)\\
 &=d(q_d-1)\log6-O(Mq_d+q_d^2/M+d)\\
 &=(\log6)^2d^2-O(d^{3/2}),
\end{aligned}                                                     \tag{14}
\]
which is the lower half of (10).

For the reverse bound, simply use
`H_{q_d}(Q_d)<=binom(6^d,q_d)<=(6^d)^{q_d}`.  Its logarithm is at most
`dq_d log6=(log6)^2d^2+O(d)`, completing (10).

For this template, the largest cap and cup both have size three.  The
paper's exact composition recurrence (or its fixed-template proposition)
therefore gives (11).  Subtraction yields

\[
 \log\frac{H_{q_d}(Q_d)}{V(Q_d)}
 \ge \log6(\log6-2)d^2-O(d^{3/2}).                               \tag{15}
\]

The leading constant is positive because `log 6>2`, whereas
`q_d log q_d=O(d log d)`.  This proves (12). `square`

This counterexample is fully realizable by the rational directional
composition in the paper.  It also shows why a nonlocal output map does not
automatically solve the problem: the history mass itself has leading
coefficient one on this family, while its convex-subset mass has coefficient
`2/log6<1`.

## 3. Exact finite failure of the factorial fibre

The paper's exact convex recurrence and (4), both in integer arithmetic,
give at depth `d=18`

\[
 |Q_{18}|=6^{18},\qquad q=47,
\]

\[
 \log H_{47}(Q_{18})=1829.783018\ldots,
 \qquad \log V(Q_{18})=1614.313497\ldots .                       \tag{16}
\]

Thus

\[
 \log\frac{H_{47}(Q_{18})}{V(Q_{18})}=215.469521\ldots
   >\log(47!)=197.364610\ldots,                                  \tag{17}
\]

and therefore

\[
 H_{47}(Q_{18})>47!\,V(Q_{18}).                                  \tag{18}
\]

This is a rigorous finite counterexample to the graph-analogue fibre
`H_q<=q!V`.

The leading-scale diagnostic is more concerning.  At `q` equal to the
nearest integer to `log |Q_d|`, exact recurrence gives

\[
\begin{array}{c|c|c|c}
d&q&\log(H_q/V)/q^2&\log H_q/(\log|Q_d|)^2\\ \hline
18&47&0.09754&0.84517\\
20&52&0.09987&0.84925\\
25&65&0.10965&0.86390
\end{array}                                                       \tag{19}
\]

Meanwhile `log V/(log |Q_d|)^2` is tending to the known value

\[
 \frac{2}{\log 6}=0.773705\ldots .                               \tag{20}
\]

The explicit spine proof above gives a limiting lower gap of
`1-2/log6=0.226294...` after normalization by `(log |Q_d|)^2`; the full
recurrence is already moving toward that value in this finite range.

## 4. The endpoint-product identity is false

For endpoint pairs `u<v`, define monochromatic path counts

\[
 R_{uv}=1+\sum_{t<u:\chi(t,u,v)=+}R_{tu},\qquad
 B_{uv}=1+\sum_{t<u:\chi(t,u,v)=-}B_{tu}.                         \tag{21}
\]

The suggested identity

\[
 V(P)\stackrel?=|P|+\sum_{u<v}R_{uv}B_{uv}                        \tag{22}
\]

already fails on the realizable six-point set `T_{4,2}`.  Exact orientation
enumeration gives

\[
 |P|+\sum_{u<v}R_{uv}B_{uv}=44,
 \qquad V(P)=50.                                                   \tag{23}
\]

The product in (22) counts opposite-color monotone paths sharing their
*final endpoint pair*, i.e. split-type objects.  General convex hull chains
share their leftmost and rightmost points instead, so neither equality nor
a useful constant comparison follows automatically.  In fact, on the
realizable alternating least-index family the left side of (22) is
`2^n-1`, whereas `V(P)` is only exponential with strictly smaller base; the
ratio is exponentially unbounded.

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_claude_review_audit/history_global_test.py
```

The checker derives the six-point orientation table from the exact Pascal
decomposition, exhaustively verifies its cap/cup/convex/history profiles,
checks the exact recurrence, and reports integer counts through depth 25.
