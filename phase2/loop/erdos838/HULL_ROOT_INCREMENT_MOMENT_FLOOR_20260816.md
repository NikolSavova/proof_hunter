# A rank-moment floor for the exact hull-root increment

**Date:** 2026-08-16. Face counts are nonempty and logarithms are base two.

## Verdict

Let

\[
 f(n)=\min_{|P|=n}V(P),
 \qquad
 K_{n,1}=f(n+1)-f(n)-1.                                 \tag{1}
\]

For \(1\le t\le2^n-1\), let \(m_n(t)\) be the least possible total
cardinality of \(t\) distinct nonempty subsets of an \(n\)-set. Then

\[
 \boxed{
 K_{n,1}\ge
       \left\lceil{m_n(f(n))\over n}\right\rceil+n-1.
 }                                                       \tag{2}
\]

More precisely, if \((Q,\theta)\) attains the hull-root envelope and

\[
 E=V(Q)-f(n),\qquad C=C_\theta(Q),                       \tag{3}
\]

then \(K_{n,1}=E+C\) and

\[
 n(E+C)\ge M_F(Q)+M_C(Q)-n,                             \tag{4}
\]

where \(M_F\) and \(M_C\) are the ordinary-face and cap rank sums.
Equation (2) follows from

\[
 M_F(Q)\ge m_n(f(n)),
 \qquad M_C(Q)\ge n^2.                                  \tag{5}
\]

The theorem is an exact positive consequence of global minimality for every
\(n\); it does not assume that the envelope child \(Q\) is itself an
ordinary-face minimizer.

Its asymptotic strength is also exact enough to expose the remaining gap.
If

\[
              \log f(n)=c(\log n)^2+o((\log n)^2),      \tag{6}
\]

then Boolean-layer inversion gives

\[
 {m_n(f(n))\over f(n)}=(c+o(1))\log n.                  \tag{7}
\]

Thus (2) supplies

\[
 {K_{n,1}\over f(n)}ge(c+o(1)){\log n\over n}.         \tag{8}
\]

The exact cumulative half criterion needs coefficient one on the right of
(8), at almost every logarithmic scale. At the currently known
\(c=1/4\), (2) supplies only one quarter of that sharp-scale increment.
Therefore (2) is a real minimizer theorem but not a coefficient improvement.
It isolates the missing input as a rank/profile correlation beyond summed
one-point restoration.

## 1. Proof

Choose a realizable pair \((Q,\theta)\) attaining the minimum in the exact
hull-root recurrence

\[
 f(n+1)=1+V(Q)+C_\theta(Q).                              \tag{9}
\]

With (3), equation (9) gives \(K_{n,1}=E+C\).

Fix a label \(x\in Q\) and put \(R=Q-x\), retaining the inherited chart.
Add a new point on the cap side of \(R\). The exact one-point strong-glue
formula produces an \(n\)-point configuration with

\[
                         V(R)+1+C_\theta(R)              \tag{10}
\]

ordinary faces. By the definition of \(f(n)\), (10) is at least \(f(n)\).
Since \(V(Q)=f(n)+E\), rearrangement gives

\[
 V(Q)-V(Q-x)\le E+1+C_\theta(Q-x).                      \tag{11}
\]

Sum (11) over \(x\). The exact deletion identities are

\[
 \sum_x[V(Q)-V(Q-x)]=M_F(Q),
 \qquad
 \sum_xC_\theta(Q-x)=nC-M_C(Q).                        \tag{12}
\]

Therefore

\[
 M_F(Q)\le nE+n+nC-M_C(Q),                              \tag{13}
\]

which is (4).

The face family of \(Q\) has at least \(f(n)\) distinct members, proving
the first inequality in (5). Every singleton and every pair is a cap in
every generic chart. Their rank sum is

\[
                 n+2\binom n2=n^2,                      \tag{14}
\]

which proves the second inequality in (5). Substitution into (4) gives

\[
 nK_{n,1}\ge m_n(f(n))+n^2-n.                           \tag{15}
\]

Since \(K_{n,1}\) is integral, (15) is exactly (2).

## 2. Boolean rank function

If

\[
 B_{r-1}(n)<t\le B_r(n),
 \qquad B_r(n)=\sum_{j=1}^r\binom nj,                   \tag{16}
\]

then filling the Boolean lattice from the lowest ranks gives

\[
 m_n(t)=\sum_{j<r}j\binom nj
        +r\{t-B_{r-1}(n)\}.                             \tag{17}
\]

This proves both the exact computability used in (2) and the asymptotic
inversion (7).

## 3. Finite calibration

For the known exact values through nine points, the increment bound reads

\[
\begin{array}{c|c|c|c|c}
n&f(n)&m_n(f(n))&\text{bound in (2)}&K_{n,1}\\ \hline
1&1&1&1&1\\
2&3&4&3&3\\
3&7&12&6&6\\
4&14&28&10&11\\
5&26&59&16&17\\
6&44&108&23&27\\
7&72&190&34&40\\
8&113&316&47&54
\end{array}                                               \tag{18}
\]

At \(n=8\), the envelope optimizer has \((V,C)=(114,53)\), hence
\(E=1\) and \(E+C=54\). This confirms that (2) applies to the genuinely
nonminimal weighted child selected by the true nine-point minimizer.

## 4. Scope and next gate

Equation (2) uses all ordinary-face rank mass but only the unavoidable
singleton/pair portion of the cap rank mass. Keeping the full \(M_C\) in
(4) is potentially stronger, but a new theorem must correlate \(M_C\) with
the excess \(E\) or with \(M_F\). Scalar deletion identities alone permit
the two terms to anti-align. The exact finite frontier
\((V,C)=(113,55)\to(114,53)\) already demonstrates such anti-alignment.

Accordingly, the next coefficient-bearing statement is not another
one-point moment sum. It must prove either:

1. a stronger integrated inequality
   \(M_F+M_C-n\ge(1-o(1))n f(n)\log n/n\) at coefficient-one scale for the
   envelope optimizer; or
2. a multi-chart/shelling code that counts ordinary outputs omitted by the
   single selected root in (11).

The first display in item 1 simplifies to the sharp target
\(M_F+M_C\ge(1-o(1))f(n)\log n\); it is written in increment form to keep
its provenance clear.

## 5. Verification

Run

~~~text
python3 phase2/loop/erdos838/verify_hull_root_increment_moment_floor.py
~~~

The verifier evaluates (17), checks the finite table, exhausts the exact
integer form of (4)--(15) on broad abstract ledgers, and verifies the
asymptotic cutoff arithmetic. It does not attempt to re-prove the geometric
hull-root recurrence, which is independently reconstructed in
`V3_INDEPENDENT_AUDIT_20260816.md`.
