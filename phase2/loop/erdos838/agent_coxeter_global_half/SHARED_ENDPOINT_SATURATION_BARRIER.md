# Shared-endpoint and nested-cell saturation

**Date:** 2026-08-15
**Verdict:** the sharp path-downset exponent

\[
 \alpha=\log_2(3/2)
\]

cannot be improved by grouping all cells with one endpoint, or by grouping a
chain of nested endpoint intervals.  A strict cup gives a stretchable type-A
reduced word in which the per-cell inequality

\[
 G_{uv}(1/2)\ge\frac14
   \bigl(R_{uv}(1)B_{uv}(1)\bigr)^\alpha                 \tag{1}
\]

is equality for every cell simultaneously.  Its vertex Ferrers rectangles
are totally nested.  Consequently every proposed bound with exponent
\(\beta>\alpha\), or with a factor tending to infinity over the sum of the
cellwise right sides, fails exponentially on genuine reduced words.

This family is not a counterexample to the live target
\(H(R)=n^{o(1)}\): it has the Boolean compensation
\(F(1)=2^n\) and \(H=n(3/4)^n\).  The barrier says that a proof must detect
that compensating unweighted mass; it cannot extract additional half-mass
from the shared or nested endpoint cells themselves.

## 1. A generic rational strict-cup realization

For each \(n\), put

\[
 \delta_n=\frac1{10n^4},\qquad
 q_i=(i,i^2+\delta_ni^3),\quad 0\le i<n.             \tag{2}
\]

The function \(x^2+\delta_nx^3\) is strictly convex on the relevant range,
so every ordered triple has positive orientation.  The slope of \(q_iq_j\)
is

\[
 s_{ij}=i+j+\delta_n(i^2+ij+j^2).                    \tag{3}
\]

All these slopes are distinct.  If two pairs have different values of
\(i+j\), their integer parts differ by at least one while the total cubic
correction varies by less than one.  If their sums agree, equality of the
quadratic corrections forces equality of their products and hence the same
unordered pair.  Sorting (3) therefore gives a generic allowable sequence,
and the associated adjacent swaps form a reduced word for \(w_0\).

The small perturbation is included only to make the certificate literally a
reduced word with no simultaneous disjoint crossings.  The path and face
formulas below depend only on the all-positive triple signs.

## 2. Every cell is an equality case

Fix \(u<v\) and put \(d=v-u-1\).  In one temporal direction every subset of
the \(d\) internal labels is a path; in the reverse direction only the
direct edge is a path.  Therefore, after possibly exchanging the two names,

\[
 R_{uv}(t)=t(1+t)^d,\qquad B_{uv}(t)=t.             \tag{4}
\]

It follows that

\[
 X_{uv}:=R_{uv}(1)B_{uv}(1)=2^d                    \tag{5}
\]

and

\[
 G_{uv}(1/2)=\frac14(3/2)^d
 =\frac14(2^d)^{\log_2(3/2)}
 =\frac14X_{uv}^{\alpha}.                          \tag{6}
\]

Thus (1) is equality in every cell, not just asymptotically and not just in
an abstract downset.

There is an immediate obstruction to a shared-cell gain.  For any collection
\(\mathcal C\) of cells in this order,

\[
 \sum_{e\in\mathcal C}G_e(1/2)
 =\frac14\sum_{e\in\mathcal C}X_e^\alpha.           \tag{7}
\]

No universal inequality can replace the right side of (7) by a quantity
which is an unbounded factor larger on these collections.

## 3. Cells sharing one right endpoint

Fix the right endpoint \(v\).  As \(u\) runs from \(v-1\) down to zero, the
activity-one rectangles are

\[
 (R_{uv}(1),B_{uv}(1))=(2^{v-u-1},1).               \tag{8}
\]

They are totally nested, so their Ferrers union \(D_v\) has exact area

\[
 |D_v|=2^{v-1}.                                      \tag{9}
\]

The total incoming half mass is

\[
\begin{aligned}
 M_v(1/2)
 &=\sum_{u<v}G_{uv}(1/2)\\
 &=\frac14\sum_{d=0}^{v-1}(3/2)^d
 =\frac12\bigl((3/2)^v-1\bigr).                    \tag{10}
\end{aligned}
\]

For every fixed \(\beta>\alpha\), therefore,

\[
 \frac{M_v(1/2)}{|D_v|^\beta}
 =\frac{(3/2)^v-1}{2^{1+\beta(v-1)}}
 \longrightarrow0                                      \tag{11}
\]

exponentially.  Hence no shared-endpoint theorem of the form

\[
 M_v(1/2)\ge C^{-1}|D_v|^\beta                       \tag{12}
\]

can hold with \(\beta>\alpha\) and an absolute or subexponential \(C\).
At \(\beta=\alpha\), the ratio in (11) tends to \(3/4\), confirming the
sharp scale of the existing vertex inequality.

The same obstruction holds after summing over every right endpoint.  The
off-diagonal half mass is

\[
 Q_n(1/2)=\sum_{v=1}^{n-1}M_v(1/2)
 =(3/2)^n-1-\frac n2,                                \tag{13}
\]

whereas

\[
 \sum_{v=1}^{n-1}|D_v|^\beta
 =\frac{2^{\beta(n-1)}-1}{2^\beta-1}.                \tag{14}
\]

The ratio of (13) to (14) tends to zero exponentially for every
\(\beta>\alpha\).

## 4. A nested-interval chain also saturates

Now take the cells with fixed left endpoint zero and right endpoints
\(v=1,\ldots,n-1\).  Their ambient intervals

\[
 [0,1]\subset[0,2]\subset\cdots\subset[0,n-1]       \tag{15}
\]

are a single strict nesting chain.  Nevertheless (6) holds at every level,
and hence

\[
 \sum_{v=1}^{n-1}G_{0v}(1/2)
 =\frac14\sum_{v=1}^{n-1}X_{0v}^{\alpha}
 =\frac12\bigl((3/2)^{n-1}-1\bigr).                \tag{16}
\]

Thus nesting, laminarity, a common endpoint, and exact recoverability of the
level do not create any extra activity interpolation.  In particular, an
entropy proof which conditions only on the nested cell address can do no
better than the exponent \(\alpha\).

## 5. Where the compensation lives

Every subset of a strict cup is in convex position, so

\[
 F_n(t)=(1+t)^n.                                      \tag{17}
\]

Consequently

\[
 \frac{F_n(1)}{F_n(1/2)}=(4/3)^n,\qquad
 H(P_n)=n(3/4)^n.                                    \tag{18}
\]

The family is extremely favorable for the asymptotic half-weight target,
despite saturating every local, shared-endpoint, and nested-cell inequality
above.  The missing credit is exactly the unweighted Boolean face bank
\(2^n\), not additional half-weight endpoint mass.

This leaves a sharply delimited cross-cell gate.  A useful theorem must have
an alternative of the following form:

* either the endpoint rectangles exhibit more than Boolean-cup saturation;
* or a saturation chain decodes a large unweighted face bank outside the
  charged endpoint state.

A one-sided inequality which insists on improving the half-mass side in both
branches is impossible.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_coxeter_global_half/verify_shared_endpoint_saturation.py
```

The checker constructs the rational coordinates (2), verifies general
position and pairwise-distinct slopes, reconstructs the reduced word by
adjacent swaps, evaluates the forward and reverse transvection products at
activities one and one-half, and checks (4)--(18) with exact rational
arithmetic through 48 wires.
