# Erdős 838: the half-weight attack

**Date:** 2026-08-13
**Status:** the unrestricted problem remains open.  This note records the
cleanest surviving route, the exact reductions proved in this campaign, and
the local approaches that have now been ruled out.

All logarithms in asymptotic coefficients are base two.  Throughout this note
`V(P)` includes the empty convex subset.

## 1. Current rigorous window

For

\[
 f(n)=\min_{|P|=n}\#\{A\subseteq P:A\text{ is in convex position}\},
\]

the current result is

\[
 \frac14\leq
 \liminf\frac{\log_2f(n)}{(\log_2n)^2}
 \leq
 \limsup\frac{\log_2f(n)}{(\log_2n)^2}
 \leq\frac12.
\]

The upper coefficient `1/2` is attained by the iterated ordered blow-ups in
`paper/main.tex`.  The same coefficient is the exact asymptotic minimum over
the whole mirror-decomposable class.  The remaining task is the unrestricted
lower bound.

## 2. The primary target

Let

\[
 Z_P(z)=\sum_{A\text{ convex}}z^{|A|},\qquad
 H(P)=\frac{nZ_P(1/2)}{Z_P(1)}.
\]

The principal conjectural inequality is

\[
 \boxed{H(P)=n^{o(1)}.}                                      \tag{HW}
\]

The attractive finite strengthening is `H(P)<=2`; it survives every exact
and heuristic test, but is not required.  Jensen under the uniform measure on
convex subsets gives

\[
 \frac{Z_P(1/2)}{Z_P(1)}=\mathbb E2^{-|A|}
 \geq2^{-\mathbb E|A|}.
\]

Thus (HW) implies

\[
 \mathbb E|A|\geq(1-o(1))\log_2n.                            \tag{MS}
\]

For a minimum-count `n`-point configuration, omitted-point double counting
then gives

\[
 (n-\mathbb E|A|)f(n)\geq nf(n-1).
\]

Summing its logarithm proves the missing lower coefficient `1/2`.  Therefore
(HW), even only for minimizers, solves Erdős 838 and proves that the normalized
limit exists and equals `1/2`.

Equivalently, since

\[
 \log_2\frac{Z_P(1)}{Z_P(1/2)}
 =\int_{1/2}^1\mu_t\,d\log_2t,
 \qquad \mu_t=t\frac{Z'_P(t)}{Z_P(t)},
\]

the exact constant-two conjecture is the integrated activity inequality

\[
 \int_{1/2}^1\mu_t\,d\log_2t\geq\log_2(n/2).             \tag{IA}
\]

The integral, rather than either endpoint mean alone, is load-bearing.

## 3. Exact random-prefix reduction

Let `F` be any simplicial complex on `[n]`.  Choose a uniform random
permutation `pi` and put

\[
 R(\pi)=\max\{r:\{\pi_1,\ldots,\pi_r\}\in F\}.
\]

If `v_k` is the number of `k`-faces, heredity gives

\[
 \Pr(R\geq k)=\frac{v_k}{\binom nk}.
\]

Writing `S_r(z)=sum_{k<=r} binom(n,k)z^k` and comparing coefficients yields
the exact mixture

\[
 \boxed{Z_F(z)=\mathbb E S_R(z).}                            \tag{RP}
\]

Tilt the law of `R` by `S_R(1)`.  Then

\[
 \frac{H(F)}n=\mathbb E_*\rho_n(R),\qquad
 \rho_n(r)=\frac{S_r(1/2)}{S_r(1)}.
\]

Uniformly for `r=o(n)`, elementary top-term estimates give

\[
 \rho_n(r)=(1+O(r/n))2^{-r}.
\]

Consequently the concrete stopping-time target is

\[
 \boxed{\mathbb E_*2^{-R}\leq n^{-1+o(1)}.}                 \tag{PST}
\]

For planar convexity, the first failed prefix contains a rooted four-circuit
and the arriving point belongs to that circuit.  This is the best local handle
currently known: switch the first circuit while retaining the global
`S_R(1)` tilt.

## 4. Other exact interfaces

For a uniformly random convex subset, write `mu` and `sigma^2` for its size
mean and variance.  If a deletion is sampled with probability proportional to
`V(P-p)`, then

\[
 \mathbb E\mu(P-p)=\mu(P)-\frac{\sigma^2(P)}{n-\mu(P)}.       \tag{D1}
\]

At activity `z`, omitted-point double counting gives

\[
 \sum_pZ_{P-p}(z)=(n-\mu_z)Z_P(z).
\]

Therefore

\[
 \mathbb E_{p\propto V(P-p)}H(P-p)
 =\frac{n-1}{n}\frac{n-\mu_{1/2}}{n-\mu_1}H(P).             \tag{D2}
\]

This is the exact deletion induction interface.  A proof must exploit slack
among the children or add a second potential; its scalar factor alone allows
polynomial growth.

For a type-A reflection order, if

\[
 B(z)=\prod_{\alpha\in R}(I+zE_\alpha),\qquad
 A(z)=\prod_{\alpha\in R^{\rm rev}}(I+zE_\alpha),
\]

then nilpotence gives

\[
 A(z)=B(-z)^{-1},\qquad
 Z_P(z)=1+nz+\langle A(z),B(z)\rangle_F-n.                   \tag{M}
\]

Thus (HW) is also a reverse-product dilation inequality.  A single long braid
need not improve it, so any Coxeter proof must amortize full boundary states.

Finally, endpoint factorization gives

\[
 Z_P(z)=1+nz+\sum_{i<j}U_{ij}(z)C_{ij}(z).                  \tag{E}
\]

A live intermediate lemma is the constant-loss weighted cup--cap estimate

\[
 \mu_{1/2}(U_{ij})+\mu_{1/2}(C_{ij})
 \geq\log_2(j-i+1)-O(1).                                  \tag{WES}
\]

It must be paired with a localization charge, because short endpoint spans can
carry significant mass.

## 5. What this campaign ruled out

1. **The half-activity endpoint shortcut is false.**  The sufficient claim
   `mu_(1/2)>=log_2n-1` fails for exact integer planar configurations:

   | `n` | `H` | `mu_(1/2)-(log_2n-1)` |
   |---:|---:|---:|
   | 24 | `1.686142...` | `-0.022595...` |
   | 30 | `1.730215...` | `-0.082571...` |

   The integrated target (IA) and `H<=2` survive.

2. **Packetwise braid descent is false.**  An exact realizable ten-wire long
   braid decreases `(V,M)` but increases `Z(1/2)`.  Earlier exposure paths also
   reverse a packet's preference without flipping that packet.

3. **One-step visible flips are insufficient.**  Canonical inverse fibres are
   down-sets and can have half-weight `((3/2)^m-1)/4`.  Even a permissive
   fractional one-step flip flow is infeasible on the exact twenty-point
   record, with deficit `893/4`.  Any flip proof must be multistep.

4. **The factor-one endpoint span bound is false.**  An exact span-seven pair
   has product polynomial `z^2+5z^3`, whose activity ratio is `48/7<7`.
   Constant loss in (WES) remains viable.

5. **The cyclic three-cluster construction is dead.**  The natural recursive
   continuation of the exact nine-point minimizer contains a certified binary
   subsystem forming a convex chain of size `2^r` at depth `2r+1`.  Hence

   \[
   V(P_{2r+1})\geq2^{2^r}=2^{(N/3)^{\log_9 2}},
   \]

   which is stretched-exponential rather than quasipolynomial.

## 6. Exact finite data

Complete enumeration and independent realizable-order-type scans give

\[
 f(8)=114,\qquad f(9)=169,
\]

including the empty set.  Their profiles are

\[
 1+8z+28z^2+56z^3+21z^4
\]

and

\[
 1+9z+36z^2+84z^3+36z^4+3z^5.
\]

The exact `n=9` minimizer has six minimum-count deletions and three deletions
one count above minimum, but no lexicographically minimum child.  This kills a
naive hereditary lex-minimizer induction.

A new exact `n=20` point set has profile

\[
 (1,20,190,1140,2415,866,135,8),
\]

so `V=4775`, improving the previous saved finite record `5156`.  Direct exact
hull enumeration checks all `2^20` subsets.

## 7. Attack order

The next proof pass should use the following gates.

1. **Primary: tilted first-circuit switching.**  Work directly with (PST).
   Preserve the `S_R(1)` tilt, allow multistep switches, and exploit the
   down-set structure of inverse fibres.  A successful subpolynomial-fibre
   switch proves the full theorem.
2. **Parallel: integrated deletion potential.**  Strengthen (D2) with a second
   potential measuring the activity-variance integral.  Pointwise variance and
   endpoint-mean bounds are already falsified.
3. **Intermediate: prove (WES).**  Use weighted cup--cap recursion, then prove a
   span-localization dichotomy.  This is a credible route to a strict lower
   improvement even if it does not immediately reach `1/2`.
4. **Adversarial gate:** continue searching for `H>2` and, more importantly, a
   nested family with `H=n^{\Omega(1)}`.  Isolated finite records below `1.8`
   are not asymptotic evidence.

## 8. Verification map

- `agent_half_weight/`: random-prefix identity, deletion recursion, endpoint
  obstruction, planar half-mean records.
- `agent_visible_flip_hw/`: exponential flip fibres and exact max-flow
  obstruction.
- `agent_coxeter_half_weight/`: matrix/integrated-activity audit and braid
  searches.
- `agent_dual_number_amortization/`: packet obstructions, full profiles, and
  direct `n=20` hull verifier.
- `agent_lex_minimizer_search/`: complete `n=8` reflection sweep and complete
  realizable order-type scans through `n=9`.
- `agent_cyclic_ifs_kill/`: all-depth slope-cone proof for the stretched-
  exponential cyclic subsystem.
- `agent_planar_lattice_mean/` and `agent_root_variance/`: closure-lattice and
  variance identities.

The principal exact commands are listed in each directory's report.  All were
replayed successfully on 2026-08-13.
