# Fixed-size supersaturation: prior-art audit and algebraic ceiling

**Date:** 2026-08-16. All logarithms are base two.

## Verdict

The standard counting literature does not currently supply the fixed-size
gain requested in `PROVED_GAIN_STRATEGY_20260815.md`.  Three superficially
relevant inputs were checked against the live scale

\[
                    N=4^k,
 \qquad
 v_k(P)\stackrel{?}{\ge}2^{(1+\eta-o(1))k^2}.          \tag{1}
\]

1. The usual Erdős--Szekeres double count gives only
   \(2^{k^2-o(k^2)}\).
2. Positive-fraction Erdős--Szekeres theorems give complete
   \(k\)-partite transversal banks, but this route would need a guaranteed
   block fraction \(2^{-(1-\eta)k+o(k)}\).  The universal positive-fraction
   parameter is known to be at most \(2^{-k+o(k)}\), so this entire
   homogeneous-block mechanism has the same coefficient-one ceiling as the
   ordinary double count.
3. The exact weighted convex-polygon identities of Huemer--Oliveros--
   Pérez-Lantero--Torra--Vogtenhuber are hull-decomposition identities.
   Algebraically they cannot force the next rank at **any** cutoff: for every
   \(3\le r\le N\) they admit a nonnegative integral solution with

   \[
       v_j=\binom Nj\quad(3\le j\le r),
       \qquad v_j=0\quad(j>r).                          \tag{2}
   \]

Thus the fixed-size target remains a genuinely new growing-rank
supersaturation problem.  It needs geometric compatibility across ranks,
selected-family sparsity, or a mixed/profile bank; fixed-\(k\) asymptotics,
one complete transversal box, and scalar hull identities are now excluded
as standalone closure routes.

## 1. What the fixed-\(k\) literature actually says

Aichholzer et al. summarize the minimum number of convex \(k\)-gons as
\(\Theta(N^k)\) **for constant \(k\)**.  That statement ultimately follows
from a positive-fraction Erdős--Szekeres theorem: for each fixed \(k\), one
can find disjoint blocks \(Y_1,\ldots,Y_k\), each of size at least
\(c_kN\), such that every transversal is convex.

The dependence on \(k\) is decisive here.  If

\[
                         c_k=2^{-a k+o(k)},              \tag{3}
\]

then one such box contains

\[
                   \prod_i|Y_i|
             \ge 2^{(2-a)k^2+o(k^2)}                   \tag{4}
\]

convex \(k\)-gons at \(N=4^k\).  To prove (1), this mechanism requires
\(a\le1-\eta\).  But the best possible universal positive-fraction
constant satisfies \(c_k<2^{-k+o(k)}\); in particular a uniform
\(a<1\) is impossible.  The complete-transversal box can reach the
coefficient-one boundary but cannot cross it by a fixed amount.

Primary sources:

- I. Bárány and P. Valtr,
  [A Positive Fraction Erdős--Szekeres Theorem](https://www.renyi.hu/~barany/cikkek/72.pdf),
  *Discrete Comput. Geom.* **19** (1998), 335--342.
- O. Aichholzer et al.,
  [On \(k\)-Gons and \(k\)-Holes in Point Sets](https://arxiv.org/abs/1409.0081),
  especially its tables' explicit constant-\(k\) scope.
- The quantitative upper limitation on the optimal cluster fraction is
  recorded in A. Pór and P. Valtr,
  [On the positive fraction Erdős--Szekeres theorem for convex sets](https://doi.org/10.1016/j.ejc.2006.06.015),
  which states \(\epsilon_k<2^{-k+o(k)}\).

## 2. The ordinary double-count ceiling

Let \(t=ES(k)\).  Counting pairs consisting of a \(t\)-set and a convex
\(k\)-set contained in it gives

\[
                         v_k(P)\ge
                 {\binom Nk\over\binom tk}.             \tag{5}
\]

The best current estimate \(t=2^{k+o(k)}\) and \(N=2^{2k}\) yield

\[
                 \log v_k(P)\ge k^2-o(k^2).             \tag{6}
\]

More generally, first finding \(r\ge k\) convex vertices in every
\(ES(r)\)-set and counting its \(k\)-subsets gives

\[
 v_k(P)\ge
 {\binom Nk\binom rk\over\binom{ES(r)}k}.               \tag{7}
\]

With \(ES(r)=2^{r+o(r)}\), the quadratic main exponent is
\(2k^2-kr\), maximized at the smallest choice \(r=k\).  Passing through a
larger forced polygon therefore cannot improve (6).

## 3. Exact weighted identities are algebraically rank-blind

For an \(N\)-point set \(S\), let \(X_{j,\ell}\) count convex
\(j\)-gons containing exactly \(\ell\) points of \(S\) in their interior.
The weighted identity is

\[
 \sum_{j=3}^{N}\sum_{\ell=0}^{N-j}
       x^j(1+x)^\ell X_{j,\ell}
   =(1+x)^N-1-Nx-\binom N2x^2.                          \tag{8}
\]

It simply classifies every subset of size at least three by its hull
vertices and the selected points lying inside that hull.

For every cutoff \(3\le r\le N\), the following integral ledger satisfies
(8):

\[
 \begin{aligned}
 X_{j,0}&=\binom Nj &&(3\le j<r),\\
 X_{r,\ell}&=\binom{N-\ell-1}{r-1}
       &&(0\le\ell\le N-r),\\
 X_{j,\ell}&=0&&\text{otherwise}.
 \end{aligned}                                         \tag{9}
\]

Indeed, with \(y=1+x\), the elementary telescoping identity

\[
 x^ry^\ell=x^{r-1}(y^{\ell+1}-y^\ell)                  \tag{10}
\]

and the hockey-stick identity give

\[
 \begin{aligned}
&\sum_{j=3}^{r-1}\binom Njx^j+
   \sum_{\ell=0}^{N-r}\binom{N-\ell-1}{r-1}x^ry^\ell\\
 &\hspace{25mm}=(1+x)^N-1-Nx-\binom N2x^2.             \tag{11}
 \end{aligned}
\]

Moreover, for every \(3\le j\le r\),

\[
       \sum_\ell X_{j,\ell}=\binom Nj,                 \tag{12}
\]

where the \(j=r\) case is the hockey-stick identity. Thus the scalar
equations tolerate the *maximum possible count at every rank through an
arbitrary cutoff* while assigning zero mass above it. The ledger is not
claimed to be stretchable; indeed the Erdős--Szekeres theorem excludes it
geometrically for large \(N\) at fixed \(r\). Its point is exactly that (8),
positivity, integrality, and even perfect information at every lower rank do
not encode the cross-rank geometric compatibility that the proof needs.

Primary source for (8): C. Huemer, D. Oliveros, P. Pérez-Lantero,
F. Torra, and B. Vogtenhuber,
[On weighted sums of numbers of convex polygons in point sets](https://arxiv.org/abs/1910.08736),
*Discrete Comput. Geom.* **68** (2022), 1344--1363, Corollary 7.

## 4. Updated proof target

The viable fixed-size statement is still (1), but a proof must use at
least one ingredient absent from all three mechanisms above.  A useful
minimal formulation is:

> At \(N=4^k\), show that the convex-four-set hypergraph together with its
> planar circuit elimination forces either
> \(2^{(1+\eta-o(1))k^2}\) convex \(k\)-sets, or a mixed/profile bank of
> the same size.

The second alternative is included because the campaign's exact barriers
show that a low count in one prescribed rank can be paid by endpoint or
recursive faces in other ranks.  Any next attempt that sees only the
numbers \(X_{j,\ell}\), or extracts only one homogeneous transversal box,
should be stopped immediately.

## 5. Verification

Run

~~~text
python3 phase2/loop/erdos838/verify_fixed_size_supersaturation_prior_art_audit.py
~~~

The verifier checks (8)--(12) coefficientwise for every cutoff in a wide
range of \(N\),
reconstructs (8) directly from exact rational point configurations, and
audits the double-count and positive-fraction exponent ledgers.  External
literature theorems and their parameter ranges are cited rather than
computationally re-proved.
