# Erdős 838: an exact hereditary-multiplicity barrier at coefficient `1/4`

**Date:** 2026-08-13.  All logarithms are base two.  For an `n`-point set
`P` in general position, let `v_k(P)` be its number of convex `k`-subsets
and let

\[
 V(P)=\sum_{k\geq1}v_k(P).
\]

This note isolates a sharp obstruction to several plausible attempts to
improve the known lower bound

\[
 \log V(P)\geq \left(\frac14-o(1)\right)(\log n)^2.       \tag{1}
\]

The conclusion is not that coefficient `1/4` is optimal.  Rather, it is
that **hereditary averaging, even at arbitrarily many scales, cannot improve
it unless one first proves a genuinely stronger local multiplicity theorem.**
The cancellation is exact at the level of binomial coefficients, not merely
an artifact of a loose asymptotic estimate.

The final section gives the precise quantitative target which would escape
the barrier.

## 1. Exact telescoping of every fixed-size lifting chain

Write

\[
 \mu_k(n)=\min_{|P|=n}v_k(P).
\]

The usual hereditary double count says that, for `n >= m >= k`,

\[
 \mu_k(n)\geq \mu_k(m)\frac{\binom nk}{\binom mk}.          \tag{2}
\]

Indeed, count pairs `(K,M)` in which `M` is an `m`-subset of `P` and `K` is
a convex `k`-subset of `M`.

The important point is that iterating (2) gives no strengthening whatsoever.

> **Proposition 1 (exact multiscale collapse).**  For any chain
> \[
>  n=m_0\geq m_1\geq\cdots\geq m_r\geq k,
> \]
> repeated application of hereditary double counting gives exactly
> \[
>  \mu_k(n)\geq \mu_k(m_r)\frac{\binom nk}{\binom{m_r}k}.   \tag{3}
> \]
> In particular, all intermediate scales cancel.

**Proof.**  The successive factors telescope:

\[
 \prod_{i=0}^{r-1}\frac{\binom{m_i}k}{\binom{m_{i+1}}k}
 =\frac{\binom nk}{\binom{m_r}k}.
\]

Equivalently, count nested histories

\[
 K\subseteq M_r\subseteq\cdots\subseteq M_1\subseteq P.
\]

Every fixed `K` has the same number

\[
 \binom{n-k}{m_1-k}
 \binom{m_1-k}{m_2-k}\cdots
 \binom{m_{r-1}-k}{m_r-k}
\]

of such histories.  The apparent entropy in choosing the intermediate sets
is therefore exactly an extension fibre and disappears on division. `square`

Thus a multiscale argument can improve (2) only if its history records
additional compatible structure, and that structure has fibres smaller than
the full nested-subset fibre above.  Merely remembering the final convex set
does not suffice.

## 2. The standard growing-`k` profile is a fixed point

The modern Erdős--Szekeres bound gives

\[
 \log ES(k)=k+o(k).                                \tag{4}
\]

Applying (2) at `m=ES(k)` gives, uniformly for
`k=theta log n` with fixed `0<theta<1`,

\[
 \log\mu_k(n)\geq
 \bigl(\theta(1-\theta)-o(1)\bigr)(\log n)^2.     \tag{5}
\]

The parabola `theta(1-theta)` has maximum `1/4`.

There is a useful stronger invariance.  Put `t=n^{alpha+o(1)}` and suppose
we first establish (5) for `j=theta log t` inside every `t`-set, then lift
those `j`-sets to `n`.  The exponent obtained is

\[
 \begin{aligned}
 &\theta(1-\theta)(\log t)^2
       +j(\log n-\log t)+o((\log n)^2)\\
 &\qquad=\left(\theta(1-\theta)\alpha^2
       +\theta\alpha(1-\alpha)+o(1)\right)(\log n)^2\\
 &\qquad=\left(y(1-y)+o(1)\right)(\log n)^2,
 \end{aligned}                                                   \tag{6}
\]

where `y=j/log n=theta alpha`.  This is exactly the direct profile (5) at
the final relative size `y`.

> **Corollary 2 (profile fixed point).**  No finite or growing hierarchy of
> uniform-restriction double counts based only on (4) can improve the
> exponent profile `y(1-y)`.  Optimizing over the final size still gives
> exactly `1/4`.

This also shows why summing the lower bounds over many sizes does not help.
Only `O(log n)` sizes lie in the guaranteed range `k=O(log n)`, so their sum
has the same quadratic exponent as its largest term.

## 3. Even lossless same-type block regularization preserves the barrier

The same cancellation appears in the strongest imaginable version of a
common geometric regularization pipeline.  Suppose, unrealistically
optimistically, that `P` can be partitioned into `m=n^alpha` equal blocks of
size `s=n/m`, with **no loss**, such that all transversals of the blocks have
the same order type.  Choose one representative from every block and call
the resulting macro set `R`.

Every convex `j`-subset of `R` then yields exactly `s^j` convex transversals
of `P`; different macro supports yield different point subsets.  Using the
standard macro multiplicity (5) at `j=theta log m`, the resulting exponent is

\[
 \theta(1-\theta)\alpha^2
 +\theta\alpha(1-\alpha),                          \tag{7}
\]

which is again `y(1-y)` by (6).  Consequently:

> **Proposition 3 (lossless block ceiling).**  Even a lossless same-type
> partition, followed by the use of **all** convex macro subsets and all of
> their transversals, cannot improve coefficient `1/4` if the only macro
> input is the standard Erdős--Szekeres multiplicity profile.

Actual same-type lemmas discard points, so the corresponding one-level
pipeline is strictly weaker.  The obstruction is therefore not the current
quantitative constant in the same-type lemma.  It is the lack of a
macro-level multiplicity excess beyond (5).

## 4. A total-count bootstrap also cannot improve its own coefficient

One might try to avoid fixing the witness size.  Averaging the whole convex
set enumerator over all `t`-subsets gives the exact identity

\[
 \frac1{\binom nt}\sum_{|T|=t}V(P[T])
 =\sum_{j\leq t}v_j(P)\frac{\binom tj}{\binom nj}. \tag{8}
\]

The small convex subsets have to be removed before (8) can be useful.  The
following is the strongest conclusion available from a total lower bound
alone.

> **Lemma 4 (truncated hereditary lift).**  For integers `n >= t >= q`,
> \[
>  V(P)\geq
>  \left(f(t)-\sum_{j<q}\binom tj\right)
>  \left(\frac nt\right)^q,                       \tag{9}
> \]
> whenever the parenthesis is positive, where
> `f(t)=min_{|Q|=t}V(Q)`.

**Proof.**  Every induced `t`-set contains at most
`sum_{j<q} binom(t,j)` subsets of size below `q`, convex or otherwise.
Subtract these from `f(t)` and average the remaining convex subsets.  For
`j>=q`,

\[
 \frac{\binom tj}{\binom nj}
 =\prod_{h=0}^{j-1}\frac{t-h}{n-h}
 \leq\left(\frac tn\right)^j
 \leq\left(\frac tn\right)^q.
\]

Bounding the left side of (8), after truncation, by
`V(P)(t/n)^q` proves (9). `square`

Now assume only

\[
 f(t)\geq2^{(c-o(1))(\log t)^2}.                  \tag{10}
\]

For any fixed `delta>0`, one may take

\[
 q=\lfloor(c-\delta)\log t\rfloor,                \tag{11}
\]

because

\[
 \log\sum_{j<q}\binom tj
 \leq q\log\frac{et}{q}+O(\log q)
 =(c-\delta)(\log t)^2-O((\log t)\log\log t),    \tag{12}
\]

which is exponentially below (10).  If `t=n^alpha`, (9) then gives

\[
 \log V(P)\geq
 \left(c\alpha^2+(c-\delta)\alpha(1-\alpha)-o(1)\right)
 (\log n)^2.                                      \tag{13}
\]

Letting `delta` tend to zero, the largest coefficient furnished by this
truncation is `c alpha`, hence no larger than `c`.  A scale `alpha<1`
actually loses at leading order; taking `alpha=1-o(1)` merely recovers the
input bound.

> **Corollary 5 (no total-count self-bootstrapping).**  Heredity and a total
> lower bound with coefficient `c`, without information about its size
> distribution, cannot bootstrap that coefficient above `c`.  In
> particular, feeding the known `c=1/4` bound back into induced subsets does
> not improve `1/4`.

The cutoff in (11) is sharp on the quadratic scale: the number of all
subsets of size about `c log t` already has exponent `c(log t)^2`.  Thus a
larger cutoff requires new information about where the convex subsets in
(10) occur.

## 5. Split and hinged witnesses face the same ceiling

Baek--Balko's exact split-polygon threshold is

\[
 ES_{\rm split}(k)=2^{k-2}+1.                     \tag{14}
\]

The hereditary double count therefore supplies

\[
 2^{(\theta(1-\theta)-o(1))(\log n)^2}            \tag{15}
\]

split `k`-gon supports at `k=theta log n`.  Such a support has size `k` or
`k+1`.  Splitting the incidence count according to these two sizes and
applying the nested-subset calculation to the more numerous class gives the
same quadratic exponent; the one-vertex and factor-two losses are
`o((log n)^2)`.  In particular, even a hypothetical injection from every
counted split support to a convex subset would only reproduce coefficient
`1/4`; it would not improve it.

Thus the split/hinged lane needs more than a bounded-fibre closing map.  It
must establish one of the following:

1. a multiplicity excess of order `2^{Omega(k^2)}` beyond the hereditary
   count (15);
2. `2^{Omega(k^2)}` useful convex outputs per split-history family, with
   overlap smaller by the same quadratic exponent; or
3. compatibility between histories at different hinges which is not erased
   by the nested-subset fibre in Proposition 1.

This is stricter than the usual observation that closing the second endpoint
of a split polygon is difficult: **perfect closing, by itself, still does not
cross `1/4`.**

## 6. The precise local supersaturation target

The barrier can be expressed as a clean numerical target.  Suppose that for
some fixed `rho>1` and `sigma>=0`, every

\[
 m=2^{(\rho+o(1))k}
\]

point set has at least

\[
 r=2^{(\sigma-o(1))k^2}
\]

convex `k`-subsets.  Lifting this local theorem to an `n`-point set and
putting `k=beta log n` gives

\[
 \log\mu_k(n)\geq
 \left(\beta-(\rho-\sigma)\beta^2-o(1)\right)(\log n)^2,
 \qquad 0<\beta\leq\frac1\rho.                    \tag{16}
\]

The hereditary estimate obtained from one witness at `ES(k)=2^{k+o(k)}`
has exactly

\[
 \sigma=\rho-1.                                   \tag{17}
\]

Substitution into (16) recovers the invariant parabola
`beta(1-beta)`.  Therefore a necessary first departure from the hereditary
profile is a strict quadratic supersaturation gain

\[
 \boxed{\sigma>\rho-1}.                           \tag{18}
\]

For completeness, the best coefficient furnished by (16) is

\[
 \Phi(\rho,\sigma)
 =\max_{0<\beta\leq1/\rho}
   \{\beta-(\rho-\sigma)\beta^2\}
 =\begin{cases}
   1/(4(\rho-\sigma)),&\sigma\leq\rho/2,\\
   \sigma/\rho^2,&\sigma\geq\rho/2.
  \end{cases}                                    \tag{19}
\]

(The second branch also covers `sigma>=rho`.)  Thus the exact sufficient
condition is `Phi(rho,sigma)>1/4`.  Condition (18) says only that the local
input beats the hereditary profile; for large `rho` a small such gain need
not yet beat the globally available `1/4`.

For the most relevant half-scale `rho=2`, the standard count gives
`2^{(1-o(1))k^2}` convex `k`-sets among `2^{2k+o(k)}` points.  A theorem with

\[
 \mu_k(2^{2k+o(k)})\geq2^{(1+\eta-o(1))k^2}       \tag{20}
\]

for any fixed `eta>0` would immediately improve (1) to coefficient at least
`(1+eta)/4` by taking `n=2^{2k+o(k)}`.  Conversely, every route audited in
Sections 1--5 supplies only `eta=0`.

Equation (20), or an endpoint/history statement with the same net excess
after division by fibres, is therefore a concrete next target for the
unrestricted problem.

### 6.1 Equivalent density formulation and the uniformity trap

For fixed `k`, the literature often studies the limiting density

\[
 c_k=\lim_{n\to\infty}\frac{\mu_k(n)}{\binom nk}.
\]

The threshold argument gives

\[
 c_k\geq\binom{ES(k)}k^{-1}=2^{-(1+o(1))k^2}.     \tag{21}
\]

A **uniform finite** improvement

\[
 \mu_k(n)\geq
 2^{-(1-\eta+o(1))k^2}\binom nk                 \tag{22}
\]

for some fixed `eta>0` and throughout a range `n>=2^{rho_0 k}` would give

\[
 \log\mu_k(n)\geq
 \left(\beta-(1-\eta)\beta^2-o(1)\right)(\log n)^2
\]

at `k=beta log n`, and hence a coefficient strictly above `1/4` whenever
the optimizing `beta` lies in the asserted uniform range.

It is essential that (22) be finite and uniform.  A statement only about
the fixed-`k` limit `c_k`, with an unspecified convergence threshold
`N_0(k)`, cannot be used when `k=Theta(log n)`: the value `N_0(k)` may be
larger than `2^{Theta(k)}`.  Any proposed transfer from fixed-parameter
convex-polygon density results must audit this quantifier before optimizing
in `k`.

## 7. What this rules out, and what remains alive

The following strategies cannot beat `1/4` without an additional theorem:

* iterating the standard convex-`k` supersaturation lemma at many subset
  scales;
* summing that same lower bound over all `k=Theta(log n)`;
* feeding a total `1/4` lower bound recursively through random induced
  subsets;
* applying even a lossless same-type block decomposition and counting every
  transversal of every macro convex subset;
* counting split polygons at their exact threshold and then closing each
  split object with bounded fibres.

The live routes are exactly those which create a quadratic multiplicity
excess: stronger local convex-`k` supersaturation, many compatible endpoint
closures per split family, or a history injection whose fibre is
`2^{o(k^2)}` smaller than the full nested-subset fibre.  Those statements use
geometric information absent from the threshold theorem and are not
automatic consequences of heredity.
