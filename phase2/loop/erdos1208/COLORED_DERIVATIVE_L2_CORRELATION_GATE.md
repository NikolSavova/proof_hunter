# The colored derivative mass and its sharp support-restricted L2 gate

## 1. Outcome

The scalar shift (h) is not the correct index for the global derivative
mass.  After the canonical affine-line partition, the exact index is the
normalized quotient-line color

\[
 z=(\theta,B),\qquad
 B=A_c-A_d,qquad h=c-d.                            \tag{1.1}
\]

Here \(\lambda_q=\theta q+\eta\),
\(A_q=\alpha_q-\theta q^2/2\), and the child derivative line is

\[
 d_h(t)=\theta ht+B+{\theta h^2\over2}.             \tag{1.2}
\]

Let \(C_h(\theta,B)\) be the number of oriented parent-patch pairs,
summed over affine offsets \(\eta\), which have this color, and let
\(K_h(\theta,B)\) be the full occupancy of (1.2).  Then the dyadic parent
band has the exact mass

\[
 \boxed{
 W_L=\sum_{h\ne0}\sum_{\theta,B}
 C_h(\theta,B){K_h(\theta,B)\choose3}.}             \tag{1.3}
\]

Only colors with \(K_h\ge3\) occur on the right.  Define the
support-restricted parent quotient energy and the child sixth moment by

\[
 \begin{aligned}
  \mathfrak A_h
   &=\sum_{\theta,B:K_h(\theta,B)\ge3}C_h(\theta,B)^2,\\
  \mathfrak B_h
   &=\sum_{\theta,B}{K_h(\theta,B)\choose3}^2.
 \end{aligned}                                      \tag{1.4}
\]

Colorwise Cauchy--Schwarz gives the sharp theorem

\[
 \boxed{W_L\le\sum_{h\ne0}
              \sqrt{\mathfrak A_h\mathfrak B_h}.}  \tag{1.5}
\]

The restriction in \(\mathfrak A_h\) is load-bearing.  Quotient colors
whose child line has at most two points have zero scalar weight and must
not be allowed to inflate the parent energy.

Formula (1.5) is an actual improvement over the uncolored minimum gate.
It is an equality for the integer parabola, shift by shift.  It is also an
equality for the internal colors of the multi-arc construction, and removes
exactly the false factor \(b^2\):

\[
 \mathfrak A_h=b(L-h)^2,\qquad
 \mathfrak B_h=b{2L-h\choose3}^2,qquad
 \sqrt{\mathfrak A_h\mathfrak B_h}
 =b(L-h){2L-h\choose3}.                             \tag{1.6}
\]

Thus the parabola and the multi-arc family, which pull the uncolored
envelopes in opposite directions, are simultaneously paid at their exact
scales by the same colored theorem.

This does not finish Erdős 1208.  It identifies the remaining derivative
problem as a joint moment estimate, rather than a one-dimensional
correlation in \(h\).

## 2. Exact normalization and color aggregation

Write a derivative patch as

\[
 p=(q,\lambda,\alpha),\qquad
 f(r+q)-f(r)=\alpha+\lambda r\quad(r\in S_p),        \tag{2.1}
\]

with \(L\le |S_p|<2L\).  Take two patches at shifts \(c,d\), orient them
so that \(h=c-d\ne0\), and put

\[
 \theta={\lambda_c-\lambda_d\over h},\qquad
 \eta=\lambda_c-\theta c=\lambda_d-\theta d.       \tag{2.2}
\]

Their Heisenberg quotient has slope and intercept

\[
 \mu=\theta h,qquad
 \beta=\alpha_c-\alpha_d-\theta hd.                \tag{2.3}
\]

For \(A_q=\alpha_q-\theta q^2/2\), direct expansion gives

\[
 \begin{aligned}
 A_c-A_d
 &=\alpha_c-\alpha_d-{\theta\over2}(c^2-d^2)\\
 &=\beta-{\theta h^2\over2}.                       \tag{2.4}
 \end{aligned}
\]

Consequently \(B=A_c-A_d\) and (1.2) are equivalent to the full quotient
parameters \((h,\mu,\beta)\).  For fixed \(h\), the pair \((\theta,B)\)
is therefore not a coarse label: it is exactly the child derivative line.

For a fixed affine projection line \((\theta,\eta)\), let

\[
 P_{\theta,\eta}
 =\{(q,A_q):p_q\text{ is a selected patch on that line}\}.
\]

Set

\[
 C_h(\theta,B)
 :=\sum_\eta
 r^+_{P_{\theta,\eta}-P_{\theta,\eta}}(h,B).        \tag{2.5}
\]

The canonical line through every pair \((q,\lambda_q)\) makes (2.5) a
partition: no parent pair occurs for two different \((\theta,\eta)\).
With

\[
 F_\theta(r)=f(r)-{\theta\over2}r^2,
 \qquad B_\theta=\{(r,F_\theta(r)):r\in R\},        \tag{2.6}
\]

the child occupancy is

\[
 K_h(\theta,B)
 =r_{B_\theta-B_\theta}(h,B).                       \tag{2.7}
\]

Equations (2.5)--(2.7) prove (1.3).  Applying Cauchy--Schwarz to the
color vectors

\[
 (C_h(\theta,B))_{K_h\ge3},\qquad
 \left({K_h(\theta,B)\choose3}\right)_{K_h\ge3}
\]

proves (1.5).

## 3. Two rigorous marginal controls

The theorem retains all of the endpoint information already proved in the
two-layer popularity argument.  If

\[
 Q_R(h)=\sum_q n_R(q)n_R(q-h),                       \tag{3.1}
\]

then the nonshared-tail injection gives, color by color,

\[
 \boxed{
 C_h(\theta,B)\le{Q_R(h)\over(L-1)^2}.}             \tag{3.2}
\]

Let

\[
 M_h^*=\sum_{\theta,B:K_h\ge3}C_h(\theta,B)         \tag{3.3}
\]

be the actual number of parent pairs whose quotient color is active.
It is at most the uncolored shift autocorrelation \(M_L(h)\), but can be
smaller by a polynomial factor.  From (3.2),

\[
 \boxed{
 \mathfrak A_h
 \le {Q_R(h)\over(L-1)^2}M_h^*.}                    \tag{3.4}
\]

This is already strictly more faithful than replacing \(M_h^*\) by all
possible parent pairs and then multiplying by all child lines.

There is also a standard incidence bound for the other moment.  Let
\(P_h\) be the derivative cell at shift \(h\), of size \(n_h\), and retain
only colors with

\[
 J\le K_h(\theta,B)<2J.                              \tag{3.5}
\]

Szemerédi--Trotter gives

\[
 \#\{\text{lines in (3.5)}\}
 \ll {n_h^2\over J^3}+{n_h\over J}.                 \tag{3.6}
\]

Since \({K\choose3}^2\ll J^6\) in this band,

\[
 \mathfrak B_{h,J}
 \ll n_h^2J^3+n_hJ^5.                               \tag{3.7}
\]

The exact cell budgets

\[
 \sum_hn_h^2\le k^3,
 \qquad \sum_hn_h=k(k-1)<k^2                       \tag{3.8}
\]

therefore imply

\[
 \boxed{
 \sum_h\mathfrak B_{h,J}
 \ll k^3J^3+k^2J^5.}                                \tag{3.9}
\]

Combining (1.5) once more across \(h\), and writing

\[
 \mathfrak A_{L,J}=\sum_h\mathfrak A_{h,J},
\]

gives the useful dyadic reduction

\[
 \boxed{
 W_{L,J}
 \ll \sqrt{\mathfrak A_{L,J}
                 (k^3J^3+k^2J^5)}.}                \tag{3.10}
\]

This closes every band for which the support-restricted parent quotient
energy is small enough.  It does not replace that energy by the full
Heisenberg energy; doing so would reintroduce inactive component colors.

## 4. Exact remaining moment target

Put

\[
 S=k^3+m^2,
 \qquad \mathcal T={S^2\over k^3}.                  \tag{4.1}
\]

After the logarithmically many dyadic decompositions in parent and child
richness, (3.10) proves the desired derivative estimate provided

\[
 \boxed{
 \mathfrak A_{L,J}
 \le m^{o(1)}
 {S^4\over
  k^6\bigl(k^3J^3+k^2J^5\bigr)}.}                  \tag{4.2}
\]

On the cube-root critical line \(m^2\le k^3\), this becomes

\[
 \mathfrak A_{L,J}\le m^{o(1)}
 \begin{cases}
  k^3/J^3,&J\le\sqrt{k},\\
  k^4/J^5,&J\ge\sqrt{k}.
 \end{cases}                                        \tag{4.3}
\]

The first range is the ordinary incidence range.  The hard residual is
the second line of (4.3): rich child colors must have very little *active*
parent quotient energy unless quadratic height pays.

Equivalently, if

\[
 N_{L}(C,J)
 =\#\{(h,\theta,B):
       C\le C_h(\theta,B)<2C,\ J\le K_h(\theta,B)<2J\},
\]

then the exact dyadic mass is

\[
 W_L\asymp_{\log}
 \sum_{C,J}CJ^3N_L(C,J),                            \tag{4.4}
\]

and the sharp joint-tail statement is

\[
 \boxed{
 N_L(C,J)
 \le m^{o(1)}{S^2\over k^3CJ^3}.}                  \tag{4.5}
\]

Neither marginal alone implies (4.5).  The surviving task is to prove
that large reverse color multiplicity \(C\) and large child occupancy
\(J\) cannot align on many *identical normalized colors*.  This is the
precise endpoint at which a support-sensitive Heisenberg incidence theorem,
or a quadratic-height inverse theorem, is still needed.

## 5. Equality and barrier audits

### 5.1 Integer parabola

For \(f(r)=r^2\), \(0\le r<2L\), take parent shifts
\(1\le q\le L\).  There is one active color for each
\(1\le h<L\):

\[
 \theta=2,qquad B=0,qquad
 C_h=L-h,qquad K_h=2L-h.                            \tag{5.1}
\]

Thus (1.5) is an equality term by term and gives the exact
\(\Theta(L^5)\) mass.  Here \(m=\Theta(L^2)\), so (4.2) is sharp in total
scale, up to divisor logarithms.

### 5.2 Multi-arc component colors

For block \(i\),

\[
 f(2Li+s)=s^2+\gamma_i s+C_i,
 \qquad A_{i,q}=q(\gamma_i-4iL).                    \tag{5.2}
\]

At parent-shift difference \(h\), the active internal color is

\[
 (\theta,B_i)=
 \bigl(2,h(\gamma_i-4iL)\bigr).                    \tag{5.3}
\]

Genericity makes these \(b\) colors distinct and makes every cross-block
quotient color have \(K\le2\).  Therefore those \(b^2-b\) cross colors
are absent from \(\mathfrak A_h\), and (1.6) follows.  In contrast, the
uncolored product first sums all parent colors and all child colors and
then multiplies them, creating its false \(b^2\) factor.

This audit explains why the word "active" in (3.3)--(4.3) cannot be
removed.

## 6. Verification

Run

    python phase2/loop/erdos1208/verify_colored_derivative_l2_correlation_gate.py

The verifier checks with exact rational arithmetic:

1. the signs in (2.2)--(2.4) on arbitrary sample patches;
2. the exact colorwise identity (1.3);
3. the support-restricted Cauchy theorem (1.5);
4. equality on integer parabolas through size 64;
5. the stored 24-point, four-arc integral distance-Sidon certificate;
6. all cross-arc quotient colors have occupancy at most two, the active
   moments are exactly those in (1.6), and the colored bound is 96 while
   the discarded-color gate is 1536.

The theorem is a rigorous reduction, not a proof of Erdős 1208.  The exact
remaining object is the active parent color energy in (4.2), not the
uncolored shift autocorrelation.
