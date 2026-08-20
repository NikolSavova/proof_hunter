# Arbitrary prime assignment in the bounded-inertia tower

## 1. Verdict

Allowing noncontiguous choices of the rational primes assigned to the
ramified slots and the useful Frobenius slots does **not** improve the
rank-221 bounded-inertia certificate.  This is not merely the result of a
swap search: an all-depth fractional-knapsack dual proves that the prefix
assignment

\[
 \begin{split}
 T_0&=\{\text{first 222 odd primes}\},\\
 Q_0&=\{\text{next 11,767 odd primes}\}
 \end{split}                                      \tag{1.1}
\]

maximizes each of the two exact positive-disk endpoint margins, even in the
optimistic relaxation in which **every** odd unramified prime is declared
useful.  The actual prefix `Q_0` is useful prime by prime, so the relaxation
is tight there.

Consequently the verified bound remains

\[
 \boxed{F_2(n)\ll n^{0.493714}}.                  \tag{1.2}
\]

The certificate for the exchange hypotheses and finite arithmetic is
`verify_arbitrary_prime_assignment_dominance.py`.

This note concerns the safe presentation with every base relator charged at
Zassenhaus degree two.  Possible linking-matrix improvements to the degrees
of the old tame relators are a separate refinement and are not assumed here.

## 2. Not every unramified prime is automatically useful

Let `T` contain at least one prime congruent to 3 modulo 4.  Write

\[
 A=\{p\in T:p\equiv1\pmod4\},\qquad
 B=\{p\in T:p\equiv3\pmod4\}.
\]

The positive odd squareclasses supported on `T` are

\[
 V_T=\left\{x\in\mathbb F_2^T:
          \sum_{p\in B}x_p=0\right\}.             \tag{2.1}
\]

For an unramified `q=3 mod 4`, let `epsilon_p(q)` be zero or one according
as `(p/q)=+1` or `-1`.  Its Frattini Frobenius is trivial precisely when the
linear functional

\[
 x\longmapsto\sum_{p\in T}\epsilon_p(q)x_p       \tag{2.2}
\]

vanishes on `V_T`.  Since

\[
 V_T^\perp=\operatorname{span}(1_B),              \tag{2.3}
\]

this happens exactly when

* `(p/q)=+1` for every `p in A`; and
* the symbols `(p/q)` are all equal as `p` ranges over `B`.

Thus automatic usefulness is false.  For the explicit example

\[
 T=\{7,13\},\qquad q=3,                            \tag{2.4}
\]

the positive Frattini field is `Q(sqrt(13))`, and 3 splits because
`(13/3)=+1`.  Since `-1` is nonsquare modulo 3, this `q` does not supply the
required local factorization.  More conceptually, the positive Frattini
field is totally real and disjoint from `Q(i)`, so Chebotarev produces
infinitely many primes that split in the former and are 3 modulo 4.

For `q=1 mod 4`, no nontrivial Frobenius condition is needed: `-1` is
already a square in the base residue field.  For `q=3 mod 4`, the exact
useful condition is nontrivial Frattini Frobenius; its square cap then makes
the retained residue degree exactly two.

## 3. Exact all-depth assignment problem

Fix a generator rank `d`, put `R=d+1`, and let `N` be the number of useful
Frobenius-square caps left by the relation budget.  Assign disjoint sets of
odd rational primes

\[
 |T|=R,\qquad |Q|=N.                               \tag{3.1}
\]

The inertia-square caps give

\[
 x_T:=\log D_T=\frac12\sum_{p\in T}\log p.        \tag{3.2}
\]

For a useful prime `q`, the depth-`k` marginal item is

\[
 c(q)=\log q,qquad
 g_k(q)=\frac12\log A_k(q^{-2}),                  \tag{3.3}
\]

where

\[
 A_k(t)=\frac{k+1}{k}\frac{1-t^k}{1-t^{k+1}}.
\]

The exact all-depth frontier is

\[
 F_Q(L)=\max
 \left\{\sum_{q,k}z_{q,k}g_k(q):
 \sum_{q,k}z_{q,k}\log q\le L,\quad
 1\ge z_{q,1}\ge z_{q,2}\ge\cdots\ge0\right\}. \tag{3.4}
\]

The prefix constraints are automatic under slope sorting because the
marginal gains decrease with `k`.  At target exponent `alpha` and dyadic
scale `w`, the positive-disk endpoint margin is

\[
 F_Q(2\alpha w)-\mathcal R_w(x_T),                \tag{3.5}
\]

up to the assignment-independent linear term, where, with `C=4/pi`,

\[
 \mathcal R_w(x)=
  \log C+x+
  \log\left(1+\frac{e^{2(2\alpha-1)w-x}}C\right)
 =\log\left(Ce^x+e^{2(2\alpha-1)w}\right).       \tag{3.6}
\]

Equations (3.2)--(3.6), plus the usefulness criterion of Section 2, are the
complete assignment problem.  They retain every local depth and the small
root-discriminant correction.

## 4. All-depth prefix-dominance theorem

For `lambda>0`, define the one-prime dual value

\[
 V_\lambda(p)=
 \sum_{k\ge1}\bigl(g_k(p)-\lambda\log p\bigr)_+. \tag{4.1}
\]

Only finitely many summands are nonzero.  Fractional-knapsack duality gives

\[
 F_Q(L)=\min_{\lambda\ge0}
 \left(\lambda L+\sum_{q\in Q}V_\lambda(q)\right).\tag{4.2}
\]

Let `T_0` be the first `R` odd primes, let `p_0` be the next odd prime, and
let `Q_0` be the next `N` primes beginning with `p_0`.  Put
`x_0=x_(T_0)`.  Suppose `lambda` is an active dual slope for `Q_0` at `L`,
and put

\[
 \rho=\mathcal R_w'(x_0)
 =\frac{Ce^{x_0}}
 {Ce^{x_0}+e^{2(2\alpha-1)w}}.                    \tag{4.3}
\]

The following two elementary conditions suffice:

\[
 \rho>\frac1{\log3},\qquad
 \lambda>\frac{p_0^{-2}}{(1-p_0^{-2})^2}.         \tag{4.4}
\]

**Theorem.**  Under (4.4), among every pair of disjoint sets satisfying
(3.1), even when every unramified odd prime is optimistically allowed in
`Q`, the prefix pair `(T_0,Q_0)` maximizes (3.5).

### Proof

For a fixed prime `p`, the positive summands in (4.1) form a prefix
`1<=k<=K`.  They telescope:

\[
 \sum_{k=1}^K g_k(p)
 =\frac12\log\frac{K+1}{1+p^{-2}+\cdots+p^{-2K}}.\tag{4.5}
\]

With `y=log p`, its derivative is

\[
 \frac{\sum_{e=0}^K e p^{-2e}}
      {\sum_{e=0}^K p^{-2e}}
 \in\left[0,\frac{p^{-2}}{(1-p^{-2})^2}\right]. \tag{4.6}
\]

Also

\[
 g_K(p)\le\frac12\log(1+1/K)\le\frac1{2K}.
\]

Since the `K`th term is active,

\[
 K\lambda<\frac1{2\log p}\le\frac1{2\log3}.     \tag{4.7}
\]

It follows from (4.5)--(4.7) that the ramification-versus-useful score

\[
 C_{\rho,\lambda}(p)
 :=\frac\rho2\log p+V_\lambda(p)                 \tag{4.8}
\]

is strictly increasing through all odd primes: on an interval of fixed
`K`, its derivative is at least
`rho/2-1/(2 log 3)>0`.  Moreover, for `p>=p_0`, (4.4) and (4.6) show that
`V_lambda(p)` is nonincreasing.

Now `x_T>=x_0`, because `T_0` is the minimum-product `R`-set.  The function
`R_w` is convex, so

\[
 \mathcal R_w(x_T)\ge
 \mathcal R_w(x_0)+\rho(x_T-x_0).                 \tag{4.9}
\]

Apply (4.2) at the prefix active slope `lambda`, then use (4.9).  The
assignment-dependent upper bound is

\[
 \sum_{q\in Q}V_\lambda(q)
 -\frac\rho2\sum_{p\in T}\log p.                 \tag{4.10}

The monotonicity of (4.8) removes every inversion in which a useful smaller
prime precedes a ramified larger prime.  Swapping an unused smaller prime
with a ramified larger prime also improves (4.10).  Therefore its ramified
set must be `T_0`.  Once `T_0` is fixed, the monotonicity of `V_lambda` after
`p_0` makes the next `N` primes the optimal useful set.  Equality holds for
the prefix in both (4.2) and (4.9), proving the theorem.  \(\square\)

This proof is genuinely all-depth; the number `K` is not bounded by three.

## 5. Rank-221 application and broader search

For the certified point

\[
 d=221,\quad R=222,\quad N=11767,\quad
 \alpha=0.493714,\quad w_0=84899,                 \tag{5.1}
\]

the ramified prefix ends at 1,409 and the useful prefix begins at 1,423.
Every one of its 11,767 useful primes passes the exact Legendre criterion;
there are no rejected candidates through the last useful prime 128,047.

At the left and right dyadic endpoints, the active slopes are

\[
 \lambda_L=0.0305175318495\ldots,qquad
 \lambda_R=0.0190267807767\ldots.                 \tag{5.2}
\]

The derivative bound in (4.4) is only

\[
 \frac{1423^{-2}}{(1-1423^{-2})^2}
 =4.9384496329\ldots\times10^{-7}.                \tag{5.3}
\]

The other condition has enormous slack: the correction exponent is below
`-10` at both endpoints, already giving
`rho>0.9999>1/log 3`.  Thus the theorem applies separately to both exact
endpoint margins.  No noncontiguous assignment can improve this
certificate.

A broad prefix-rank search from 50 through 1,000, followed by a unit-rank
scan around the minimum, again placed the optimum at ranks 219--221, with
rank 221 microscopically best in the higher-resolution calculation.  Sample
prefix thresholds were approximately

\[
\begin{array}{c|cccccccc}
d&100&175&200&219&221&250&500&1000\\ \hline
\alpha&.4938782&.4937276&.4937165&.4937140&.4937140&
.4937175&.4938532&.4941461.
\end{array}                                      \tag{5.4}
\]
\]

These decimal search values are orientation data, not extra theorem
claims.  The rigorous headline is the rank-221 certificate (1.2) together
with the exact arbitrary-assignment dominance theorem above.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_arbitrary_prime_assignment_dominance.py
```

It checks the explicit non-useful counterexample, the full rank-221
squareclass basis and useful-prime list, the endpoint slopes, fourth-depth
exclusion for the prefix, conservative lower bounds for `rho`, the two
analytic inequalities (4.4), and a finite adversarial stress of both score
monotonicities through 150,000.

Together with `verify_bounded_inertia_rank221.py`, it certifies both the
numerical bound and the fact that arbitrary prime reassignment cannot
improve its two endpoint inequalities.
