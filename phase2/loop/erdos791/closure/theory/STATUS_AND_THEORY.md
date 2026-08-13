# Erdős 791: status, exact asymptotic reductions, and composition barriers

Date: 2026-08-13

This note deliberately separates statements proved below from proposed routes and
failed routes.  It does **not** claim to solve the open asymptotic problem.

## 1. Exact statement and kill-search verdict

Let

\[
 g(n)=\min\{|A|:A\subseteq\{0,1,\ldots,n\},\ [0,n]\subseteq A+A\}.
\]

[Erdős problem 791](https://www.erdosproblems.com/791) asks to estimate
`g(n)` and, in particular, asked whether `g(n) ~ 2 sqrt(n)`.  The latter
specific conjecture is false: Mrose's 1979 construction already implies
`g(n)^2 <= (7/2+o(1))n`.  The broader estimation problem remains open.

It is convenient to use the inverse range function

\[
 R(k)=\max\{r:\exists A\subseteq\{0,\ldots,r\},\ |A|\leq k,
                    \ [0,r]\subseteq A+A\}.
\]

The best published asymptotic bounds found in the primary-source search are

\[
 \frac{85}{294}\leq \liminf_{k\to\infty}\frac{R(k)}{k^2}
 \leq \limsup_{k\to\infty}\frac{R(k)}{k^2}\leq 0.4585\ldots .
\]

The construction bound is Kohonen's
[2017 paper](https://arxiv.org/abs/1606.04770); the analytic upper bound is
Yu's [2015 paper](https://doi.org/10.1016/j.jnt.2015.04.007).  Equivalently,

\[
 2.1810\ldots\leq\liminf\frac{g(n)^2}{n}
 \leq\limsup\frac{g(n)^2}{n}\leq\frac{294}{85}=3.458823\ldots .
\]

### Literature audit

The following were checked specifically to avoid mistaking the old conjecture
for the current open problem.

* Rohrbach's original finite-basis paper is available through
  [EuDML](https://eudml.org/doc/168701).  Erdős's cited 1973 problem is
  *Problems and results on combinatorial number theory*, pp. 117--138.
* Güntürk--Nathanson's
  [2005/2006 paper](https://arxiv.org/abs/math/0503241) explicitly separates
  the lower and upper normalized limits.  Yu and Kohonen improve the two
  numerical sides, but do not prove the limits equal.
* Habsieger's 2014 survey/advance
  ([DOI](https://doi.org/10.1090/S0002-9947-2014-06357-5)) says the exact
  asymptotics are unknown and explains why bare generalized-Fourier weighting
  needs an extra structural ingredient.
* Faust--Tait's 2025 paper
  [states that equality of the lower and upper asymptotic constants remains
  open](https://arxiv.org/abs/2507.23627) (their Conjecture 1.5).  This includes
  order two.
* Nathanson's May 2026 structural paper
  [again describes the asymptotic attempts as unsuccessful](https://arxiv.org/abs/2605.26425).
  The May 2026 Weltge--Zyhalko paper
  [counts finite additive 2-bases](https://arxiv.org/abs/2605.19449) but does
  not close the extremal constant.
* Alzahrani's official
  [2016 master's thesis](https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=kent1479595346428957&disposition=inline)
  claims `0.4550452314`, but this is not an established improvement.  The
  repository's exact replay `phase2/loop/erdos791/audit_alzahrani_kernel.py`
  gives `u(0)=-4` and autocorrelation
  `W(1/2)=-1009/4032`, contradicting the nonnegativity used in the thesis's
  key inference.  I reran that replay successfully.  This is a qualified audit
  finding, not an author- or journal-endorsed correction.

**Kill-search verdict.** As of the search date, the existence of
`lim R(k)/k^2` (equivalently `lim g(n)^2/n`) is itself still open.  Thus a
claim merely refuting `g(n) ~ 2 sqrt(n)` would reproduce a 1979 result, while a
proof that the two normalized limits agree would be genuinely stronger than
the cited state of the art.  This is a search verdict, not a proof that no
unindexed result exists.

## 2. Established: exact inversion of the two asymptotic limits

Put

\[
 \alpha_- = \liminf_k R(k)/k^2,\qquad
 \alpha_+ = \limsup_k R(k)/k^2.
\]

Then

\[
 \boxed{\liminf_n\frac{g(n)^2}{n}=\frac1{\alpha_+},\qquad
 \limsup_n\frac{g(n)^2}{n}=\frac1{\alpha_-}.}
\]

In particular, either normalized limit exists if and only if the other one
exists, and their values are reciprocal.

**Proof.** For each sufficiently large `k`,

\[
 R(k-1)<n\leq R(k)\quad\Longleftrightarrow\quad g(n)=k.
\]

There are no empty blocks: every range basis contains `0`, so adjoining
`R(k)+1` to an extremal basis proves `R(k+1)>=R(k)+1`.
On this block `k^2/n` decreases with `n`.  Its minimum is `k^2/R(k)`,
whose liminf is `1/alpha_+`.  Its maximum is
`k^2/(R(k-1)+1)`.  Since the elementary pair count and any quadratic
construction give `R(k)=Theta(k^2)`, replacing `k-1` by `k` and `R(k-1)+1`
by `R(k-1)` changes the ratio by `1+o(1)`.  The limsup is therefore
`1/alpha_-`.  (Using `|A|<=k` avoids irrelevant padding issues.)

This reduction is important strategically: proving only a good subsequential
construction controls `alpha_-`, not the existence of the limit.

## 3. Established: when a scalable finite certificate is enough

### Bounded-gap interpolation lemma

Suppose bases `A_t` have sizes and ranges

\[
 K_t=\ell t+O(1),\qquad N_t=m t^2+O(t),
\]

and `K_{t+1}-K_t=O(1)`.  Then

\[
 \liminf_{k\to\infty}R(k)/k^2\geq m/\ell^2.
\]

**Proof.** Given `k`, choose the largest `t` with `K_t<=k`.  Monotonicity
gives `R(k)>=N_t`, while bounded gaps give `t=k/ell+O(1)`.  Divide by `k^2`.

Consequently, a finite, mechanically verified parametric template whose ratio
`m/ell^2` equals a universal analytic upper bound `U` would force

\[
 \alpha_- = \alpha_+ = U
\]

and close the full asymptotic problem.  Kohonen's family has
`K_t=42t+7` and `N_t>=510t^2`, producing `510/42^2=85/294`; it does not match
Yu's universal upper bound.

A slightly more general version needs only a sequence `K_j` with
`K_{j+1}/K_j -> 1` and `N_j/K_j^2 -> U`.  A very sparse sequence with
macroscopic relative gaps does not interpolate to a liminf statement.

## 4. Established: why the obvious product does not amplify one certificate

Let $A\subseteq[0,r]$ cover `[0,r]` and $C\subseteq[0,s]$ cover `[0,s]`.
Put `M=r+1` and

\[
 D=A+MC=\{a+Mc:a\in A,c\in C\}.
\]

Then

\[
 |D|=|A||C|,\qquad [0,(r+1)(s+1)-1]\subseteq D+D.
\]

Indeed, write the target uniquely as `qM+u` with `0<=q<=s` and
`0<=u<=r`, and represent `q` by `C+C` and `u` by `A+A`.

For the efficiency

\[
 \eta(A)=\frac{r+1}{|A|^2},
\]

this construction satisfies the exact identity

\[
 \eta(D)=\eta(A)\eta(C).
\]

But the unordered-pair count gives
`r+1<=|A|(|A|+1)/2`, hence every nontrivial basis has `eta(A)<1`.
Repeated Cartesian digit products therefore drive efficiency exponentially to
zero.  They preserve additive order two, but they cannot turn one finite
object into a positive asymptotic quadratic constant.

## 5. Established: why the small-cardinality digit construction changes order

Faust--Tait's [Lemma 2.3](https://arxiv.org/abs/2507.23627) is a precise
finite-cyclic amplification theorem.  In their notation, iterating `t` digits
of a cyclic basis of additive order `h` makes the resulting interval basis
have additive order `th+g` after the boundary correction.  Cardinalities add,
rather than multiply, but additive order adds as well.

For Erdős 791 the additive order must remain exactly two, so `t` cannot grow.
This exposes a useful dichotomy for the two standard mixed-radix mechanisms:

* Cartesian digit products keep order two, but cardinalities multiply and
  normalized efficiency collapses.
* Unions of digit layers let cardinalities grow additively, but the number of
  summands grows with the number of layers.

This is **not** a no-go theorem for every conceivable composition.  It does
rule out treating an ordinary cyclic 2-basis as a black-box seed for the known
digit iteration.

There is also an elementary carry obstruction.  A cyclic basis need not be an
integer interval basis: `{0,2}` is a 2-basis of `Z/3Z`, because its integer
sums have residues `0,1,2`, but its integer sumset `{0,2,4}` misses `1`.
Any useful fixed-order lift must encode boundary/carry states in addition to
cyclic coverage.

## 6. Established: weak-limit convolution relaxation

This gives a nonlocal analytic target, although not yet the answer.

Let `A_j` be bases of size `k_j` and range `R_j`, with
`R_j/k_j^2 -> c>0`.  Scale `A_j` by `R_j` and let

\[
 \mu_j=\frac1{k_j}\sum_{a\in A_j}\delta_{a/R_j}.
\]

If a basis initially has fewer than `k_j` elements, pad it inside its range;
this is possible for all large `j` and does not affect coverage.
After a subsequence, `mu_j` converges weakly to a probability measure `mu` on
`[0,1]`.  Then, as measures on `(0,1)`,

\[
 \boxed{\mu*\mu\ \geq\ 2c\,\lambda.}
\]

**Proof.** Consider an interval `I` compactly inside `(0,1)`.  Every integer
sum in `R_j I` has an unordered representation.  A nondiagonal representation
contributes two ordered pairs to `mu_j*mu_j`; only the at most `k_j` diagonal
sums can contribute one.  Hence

\[
 (\mu_j*\mu_j)(I)\geq
 \frac{2\,\#(R_jI\cap\mathbb Z)-k_j}{k_j^2}
 =2c|I|+o(1).
\]

Weak convergence of convolution and approximation at continuity endpoints
give the measure inequality.

Thus, defining

\[
 C_{\rm conv}=\frac12\sup\{q:\exists\hbox{ probability }\mu\hbox{ on }[0,1],
                         \ \mu*\mu\geq q\lambda|_{[0,1]}\},
\]

we obtain the rigorous universal relaxation

\[
 \limsup R(k)/k^2\leq C_{\rm conv}\leq 1/2.
\]

The elementary family
`A_t={0,1,...,t-1} union {t,2t,...,t^2}` has size `2t` and covers through
`t^2+t-1`, so its coefficient tends to `1/4`.  Its scaled empirical measures
converge to

\[
 \mu=\tfrac12\delta_0+\tfrac12\lambda|_{[0,1]}.
\]

On `(0,1)`, the convolution density is `1/2+x/4`, which indeed dominates
`(1/2)lambda=2(1/4)lambda`.  Thus the relaxation is nonvacuous and
`1/4<=C_conv<=1/2`, but it is much too loose on its own to recover the current
best upper bound.

This reframes analytic upper bounds as a convolution-domination problem.  It
also suggests a verifiable finite route: partition `[0,1]`, retain bin masses
and carry-aware sub-bin constraints, and certify a universal quadratic bound
by exact rational interval arithmetic or a copositive/SOS certificate.

### Barrier inside the naive one-weight dual

A proof scheme that uses only one nonnegative test function and the fact that
`mu` is a probability measure cannot improve the counting constant.
Indeed, if `phi>=0` and `int_0^1 phi=1`, domination would imply

\[
 q\leq\iint_{x+y\leq1}\phi(x+y)\,d\mu(x)d\mu(y).
\]

But the supremum of the right side over probability measures is at least
`sup phi>=1`, by choosing point masses approaching half a maximizer.  Therefore a
one-weight dual proof can give at best `q<=1`, i.e. `c<=1/2`.  Any genuinely
improved finite dual certificate must couple several constraints or exploit
additional discrete structure (collisions, differences, carries, or Fourier
information).  This explains why merely optimizing a nonnegative weighting of
the covered sums cannot approach Yu's bound.

## 7. Established dead end: restricted-basis concatenation

If $A\subseteq[0,a]$ covers `[0,2a]` and $B\subseteq[0,b]$ covers `[0,2b]`, then

\[
 A\cup(a+B)
\]

covers `[0,2a+2b]` and has size at most `|A|+|B|-1`.  This is a valid
additive composition, but iterating a fixed block makes range and size both
linear in the number of copies.  Its normalized range divided by size squared
tends to zero.  Ordinary concatenation therefore cannot establish a positive
quadratic asymptotic constant without substantial cross-block coverage.

## 8. Plausible route (not proved): carry-state convolution hierarchy

The most concrete nonlocal route left by the audit is a finite hierarchy that
combines the weak-limit inequality with the discrete information it discards.
At level `m`:

1. partition the scaled basis into `m` intervals and introduce exact rational
   upper/lower variables for bin masses;
2. distinguish diagonal/off-diagonal pair mass and whether a pair lands below
   or above the range boundary;
3. impose coverage lower bounds on every target bin, plus consistency of the
   same variables under one dyadic refinement;
4. upper-bound the resulting quadratic feasibility problem with a rational
   copositive/SOS or exhaustive branch certificate.

A certificate proving `c<=85/294` would match Kohonen and resolve the
asymptotic constant.  A certificate merely reproducing `0.4585` would still be
valuable as an independently checkable version of the analytic upper bound.

The missing lemma is convergence/completeness of this hierarchy at the sharp
discrete constant.  Weak convergence alone cannot supply it: the coverage of
individual lattice points and carry information are lost in the limit.
Accordingly this is a **research program**, not an established reduction to a
finite calculation.

## 9. Other dead ends / cautions

* Lev's [continuous postage stamp problem](https://arxiv.org/abs/0911.5289)
  concerns a semigroup generated using an unbounded number of summands and a
  Frobenius threshold.  It is not the fixed-two-summand continuum relaxation
  above and does not transfer directly.
* A finite search at one cardinality, even a globally certified optimum, says
  nothing by itself about equality of `alpha_-` and `alpha_+`.  It needs a
  scalable family and bounded relative gaps, or a new composition theorem.
* The two standard composition laws above point in the wrong normalization.
  Invoking “subadditivity” without an explicit inequality at quadratic scale is
  not enough for Fekete's lemma.

## Bottom line

The exact old conjecture is long dead, but the full normalized-limit problem is
open.  A one-object closure theorem is possible in principle only if the
object includes a scalable/carry-state structure: ordinary interval products,
ordinary concatenation, and the known cyclic digit lemma each fail for a
proved structural reason.  The strongest concrete theory output here is (i)
the exact inverse-limit identity and interpolation criterion, and (ii) the
weak-limit convolution domination theorem, together with the proof that its
naive one-weight dual cannot beat elementary counting.
