# Successive-rank density: the exact fixed-size gain gate

**Date:** 2026-08-16. All logarithms are base two.

## Verdict

For an $N$-point set $P$, write

\[
 v_j=v_j(P),\qquad p_j={v_j\over\binom Nj}.
                                                               \tag{1}
\]

Thus $p_j$ is the probability that a uniformly random $j$-set is in
convex position.  Fix constants $0<\alpha<1$ and $c<2$, put $N=4^k$ and
$r=\lfloor\alpha k\rfloor$.  The following **average density-decay bound**
is sufficient for a strict improvement to Erd\H{o}s 838:

\[
 \log {p_r\over p_k}
 \le {c\over2}(k^2-r^2)+o(k^2).                         \tag{2}
\]

Indeed, (2) implies

\[
 \boxed{
 \log v_k\ge
 \left[1+(1-c/2)(1-\alpha^2)-o(1)\right]k^2.}
                                                               \tag{3}
\]

Combining (3) with the fixed-size bridge proves the unrestricted lower
coefficient

\[
 {1\over4}+{(1-c/2)(1-\alpha^2)\over4}.                 \tag{4}
\]

This gives a particularly sharp formulation of the fixed-size Stage-C
target.  The ordinary Erd\H{o}s--Szekeres double count has decay constant
$c=2$ and gives no gain.  **Any fixed saving below two**, even on one fixed
positive fraction of the rank interval, gives a publishable coefficient
improvement.

A convenient stronger pointwise condition is

\[
 {p_{j+1}\over p_j}\ge 2^{-cj-o(k)}
 \quad(r\le j<k),                                      \tag{5}
\]

but only the product (2) is needed.  Neither (2) nor (5) is proved here.
The point of this note is to isolate their exact quantitative strength,
record the threshold obstruction, and prevent a full-strength extension
conjecture from being mistaken for an easy local lemma.

## 1. Proof of the bridge

Let $t_r=ES(r)$.  Double counting gives

\[
 v_r\ge {\binom Nr\over\binom{t_r}r},
 \qquad
 p_r\ge\binom{t_r}r^{-1}.                              \tag{6}
\]

The best current Erd\H{o}s--Szekeres bound has
$\log t_r=r+o(r)$.  Hence, for $r=\alpha k+O(1)$,

\[
                       \log p_r\ge-r^2-o(k^2).          \tag{7}
\]

Equations (2) and (7) give

\[
 \log p_k\ge-r^2-{c\over2}(k^2-r^2)-o(k^2).           \tag{8}
\]

Since $N=4^k$,

\[
 \log\binom Nk=2k^2-o(k^2).                            \tag{9}
\]

Adding (8) and (9), and using $r/k\to\alpha$, gives

\[
\begin{aligned}
 \log v_k
 &\ge\left\{2-\alpha^2-{c\over2}(1-\alpha^2)-o(1)\right\}k^2\\
 &=\left\{1+(1-c/2)(1-\alpha^2)-o(1)\right\}k^2,
\end{aligned}                                           \tag{10}
\]

which is (3).  The fixed-size bridge then gives (4).

For example, $c=1$ and $\alpha=1/2$ would give
$\log v_k\ge(11/8-o(1))k^2$ and unrestricted coefficient $11/32$.
Letting $\alpha\downarrow0$ at $c=1$ approaches the aspirational
$3k^2/2$ fixed-size exponent and coefficient $3/8$.

## 2. Why the unrestricted pointwise version is too strong

The tempting inequality

\[
 (j+1)v_{j+1}\stackrel{?}{\ge}
 {N-j\over2^j}v_j,
 \qquad\text{equivalently}\qquad
 p_{j+1}\stackrel{?}{\ge}2^{-j}p_j,                    \tag{11}
\]

cannot hold without a size hypothesis.  A five-point minimizer has profile

\[
                  (v_1,v_2,v_3,v_4,v_5)=(5,10,10,1,0), \tag{12}
\]

so (11) fails at $j=4$.

More importantly, if (11) held whenever $N\ge2^j$, then starting from
$v_3=\binom N3$ would force a convex $k$-set already at essentially
$N=2^{k-1}$.  This would itself be a major improvement to the classical
Erd\H{o}s--Szekeres bound.  Therefore (11) near its natural threshold is a
full-strength geometric conjecture, not a suitable next reduction.

The strict target is instead (2) only at the highly supersaturated ambient
scale $N=4^k$ and only over $\alpha k\le j<k$.  It neither asserts nor
requires a new near-threshold Erd\H{o}s--Szekeres theorem.

## 3. Exact evidence and scope

The pointwise $c=1$ inequality survives the following exact regressions in
its admissible range $N\ge2^j$:

1. the stored globally minimizing order types at $N=8,9$;
2. every ordered full binary strong-decomposition tree through eleven
   leaves;
3. deterministic random ordered strong trees at sizes through $256$; and
4. the vertically iterated balanced Pascal cell $T(4,2)$ through depth
   fourteen, at every $j\le\lfloor\log N\rfloor$.

These are tests, not a proof.  The inequality would imply a substantial
part of the desired theorem, so finite survival should not be treated as
evidence that a short argument exists.  The useful conclusion is the exact
constant in (4): a future promotion or circuit argument need only beat the
decay coefficient two on a fixed rank interval.  A statement that merely
reproduces $c=2$, or that hides an unrestricted fixed-size lower bound in
its hypothesis, is not progress.

## 4. Verification

Run

~~~text
python3 phase2/loop/erdos838/verify_successive_rank_density_gain.py
~~~

The verifier checks (3)--(4) with exact rational arithmetic on a grid of
$(\alpha,c)$, verifies the five-point threshold counterexample from exact
rational coordinates, checks the stored $N=8,9$ minimizers, exhausts all
ordered binary trees through eleven leaves, and checks the vertical Pascal
hierarchy.  It does not claim to verify (2) for arbitrary point sets.
