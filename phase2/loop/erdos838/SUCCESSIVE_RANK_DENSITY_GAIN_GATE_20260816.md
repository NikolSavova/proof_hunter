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

## 3. The exact no-slack form is false at its natural threshold

The exact inequality (11) is false, not merely when $N<2^j$.  Consider the
rational double-chain family with $m$ upper and $m$ lower points, so
$N=2m$.  Its first two relevant layer counts are

\[
 v_4=2\binom m4+\binom m2^2,
 \qquad
 v_5=2\binom m5.                                      \tag{13}
\]

At $m=8$, hence $N=16=2^4$, this gives

\[
 (v_4,v_5)=(924,112),
 \qquad {p_5\over p_4}={5\over99}<{1\over16}.          \tag{14}
\]

Equivalently, the normalized left side of (11) is $80/99<1$.  Thus the
first nontrivial threshold row already kills the exact no-slack conjecture.

This counterexample does **not** kill either the strict gate (2) or the
asymptotic pointwise condition (5).  Its effective one-row exponent is

\[
 {1\over4}\log {99\over5}=1.076\ldots<2,              \tag{15}
\]

and it even satisfies the weaker pointwise bound with $c=3/2$.  Moreover,
every convex set of rank $j\ge5$ in this family lies wholly in one chain,
so

\[
 v_j=2\binom mj,
 \qquad {p_{j+1}\over p_j}={m-j\over2m-j}\qquad(j\ge5).
                                                               \tag{16}
\]

The bad drop is therefore concentrated at the entry $4\to5$, rather than
persisting across a positive fraction of the growing-rank interval.  Also,
this example is at the natural threshold $N=2^j$: when the campaign uses
$N=4^k$ and $j\le k$, the offending $N=16,j=4$ row is outside the active
interval.  A constant factor such as $80/99$ is in any case absorbed by the
$2^{-o(k)}$ allowance in (5).  The durable targets are therefore the
averaged condition (2) and, as a convenient still-live strengthening, the
supersaturated asymptotic form of (5); only the exact universal form (11)
is refuted.

The exact inequality (11) nevertheless survives the following regressions
in their admissible range $N\ge2^j$:

1. the stored globally minimizing order types at $N=8,9$;
2. every ordered full binary strong-decomposition tree through eleven
   leaves;
3. deterministic random ordered strong trees at sizes through $256$; and
4. the vertically iterated balanced Pascal cell $T(4,2)$ through depth
   fourteen, at every $j\le\lfloor\log N\rfloor$.

They are now retained only as regression tests showing where the failure
does *not* occur.  The useful conclusion is still the exact constant in
(4): a future promotion or circuit argument need only beat the decay
coefficient two on a fixed rank interval.  A statement that merely
reproduces $c=2$, or that hides an unrestricted fixed-size lower bound in
its hypothesis, is not progress.

## 4. Verification

Run

~~~text
python3 phase2/loop/erdos838/verify_successive_rank_density_gain.py
~~~

The verifier checks (3)--(4) with exact rational arithmetic on a grid of
$(\alpha,c)$, verifies both the five-point threshold counterexample and the
$16$-point admissible double-chain counterexample from exact rational
coordinates, checks (13) on a finite family, checks the stored $N=8,9$
minimizers, exhausts all ordered binary trees through eleven leaves, and
checks the vertical Pascal hierarchy.  It does not claim to verify (2) for
arbitrary point sets.
