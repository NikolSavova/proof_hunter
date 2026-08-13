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

## 8. A positive structural lemma: low count forces deep convex cages

There is one useful exact consequence of counting **all** subsets by their
convex hull.  For a convex subset `K` of `P`, let

\[
 \iota_P(K)=|P\cap\operatorname{int}\operatorname{conv}K|.
\]

> **Proposition 6 (hull-partition identity).**  Every `n`-point set in
> general position satisfies
> \[
>  2^n=1+n+\binom n2+
>  \sum_{\substack{K\subseteq P\text{ convex}\\|K|\geq3}}
>       2^{\iota_P(K)}.                            \tag{23}
> \]

**Proof.**  Given a subset `A` with at least three points, let `K` be the
vertex set of `conv A`.  Then `K` is convex and every point of `A\K` is one
of the `iota_P(K)` ambient points strictly inside `conv K`.  Conversely, for
every convex `K` and every subset `B` of those interior points, the vertex
set of \(\operatorname{conv}(K\cup B)\) is exactly `K`.  This is a bijection.  The first
three terms account for subsets of size zero, one, and two. `square`

This is also the `x=1` specialization of the weighted polygon identity of
Huemer--Oliveros--Pérez-Lantero--Torra--Vogtenhuber, but the direct hull
partition above is all that is needed here.

For `n>=6`, the first three terms in (23) total at most `2^{n-1}`.  Since
the sum has at most `V(P)` terms, some convex `K` satisfies

\[
 \iota_P(K)\geq n-1-\log V(P).                    \tag{24}
\]

Iterating (24) inside the enclosed point set gives a strong near-extremal
regularization.

> **Corollary 7 (nested-cage decomposition).**  Put `w=log V(P)`.  The set
> `P` contains pairwise disjoint convex subsets
> `K_1,...,K_D`, where
> \[
>  D\geq\left\lfloor\frac{n-5}{w+1}\right\rfloor,\qquad
>  |K_i|\leq w+1,                                  \tag{25}
> \]
> and
> \[
>  \operatorname{conv}K_{i+1}
>   \subset\operatorname{int}\operatorname{conv}K_i
>  \quad(1\leq i<D).                               \tag{26}
> \]

**Proof.**  Start with `P_0=P`.  While `|P_i|>=6`, apply (24) to `P_i` and
let `K_i` be the resulting convex set.  Put
\(P_{i+1}=P_i\cap\operatorname{int}\operatorname{conv}K_i\).  Since
`V(P_i)<=V(P)`, each step discards at most `w+1` points, including all
vertices of `K_i`.  This proves the lower bound for `D`, disjointness, and
`|K_i|<=w+1`.  Every point of `K_{i+1}` lies strictly inside `conv K_i`, so
convexity of the open interior gives (26). `square`

Consequently, any putative near-extremal family with

\[
 \log V(P)=O((\log n)^2)
\]

contains `n/O((log n)^2)` strictly nested convex cages, each with only
`O((log n)^2)` vertices.  This does not alone beat (1): taking one
representative per cage and applying a hereditary bound merely returns to
the fixed-point barrier, and the identity gives no rule for combining
vertices from different cages into one convex set.  A viable next argument
would have to exploit **multiple choices within many nested cages** with a
subquadratic fibre loss.  Unlike uniform restriction, the cage hierarchy is
geometrically canonical enough that such a gain is not ruled out by
Proposition 1.

## 9. Random-subset onion entropy: an exact decomposition and its ceiling

For a subset `A` of `P`, repeatedly delete all vertices of its convex hull;
write `K_1(A),...,K_{D(A)}(A)` for the nonempty layers.  Layers of size one
or two can occur only at the end.

> **Proposition 8 (onion-sequence bijection and entropy bound).**  Subsets
> `A` of `P` are in bijection with finite sequences of pairwise disjoint
> convex subsets `K_1,...,K_d` such that
> \[
>  \operatorname{conv}K_{i+1}
>   \subset\operatorname{int}\operatorname{conv}K_i                 \tag{27}
> \]
> whenever `i<d`; only `K_d` may have fewer than three points.  Consequently,
> if `A` is a uniform random subset, `W=V(P)`, and
> `\bar d=\mathbb E D(A)`, then
> \[
>  n\leq \log(n+1)+\bar d\log W,                                  \tag{28}
> \]
> and, more sharply,
> \[
>  n\leq \log(n+1)+\mathbb E\log {W\choose D(A)}
>   \leq \log(n+1)+\bar d\log\frac{eW}{\bar d}.                    \tag{29}
> \]

**Proof.**  The deletion procedure gives (27).  Conversely, the union of
any sequence satisfying (27) has exactly those onion layers: the points of
every later layer lie strictly inside the preceding hull and hence cannot
be vertices before that layer is deleted.  Thus the sequence determines
`A` and the correspondence is bijective.

Now `H(A)=n`.  Encoding first `D(A)` and then each layer, with at most `W`
possibilities per layer, proves (28).  Conditional on `D=d`, the layers are
`d` distinct convex subsets.  Their strict containment relation uniquely
determines their order, so there are at most `{W\choose d}` possible
sequences.  This gives the first inequality in (29).  The standard bound
`{W\choose d}\leq(eW/d)^d` and concavity of
`x\log(eW/x)` give the second. `square`

The one-layer version is an exact entropy restatement of Proposition 6.
If `K(A)` is the hull-vertex set (with `K(A)=A` for `|A|<3`), then,
conditional on `K(A)=K`, the interior points are independent fair bits.
Therefore
\[
 n=H(K(A))+\mathbb E\,\iota_P(K(A)).                               \tag{30}
\]
This independently checks both the hull partition and its powers of two.

Unfortunately (29) cannot approach the quasipolynomial scale by itself.
Since every nonfinal layer has at least three vertices,
\[
 D(A)\leq\frac{|A|+2}{3},\qquad
 \mathbb E D(A)\leq\frac n6+\frac23.                              \tag{31}
\]
At this natural linear depth, (28)--(29) force only a polynomial lower
bound on `W`.

## 10. A sharp obstruction: nested triangles have linear random onion depth

The linear scale in (31) is genuine even for the strongest possible small
cages.

> **Proposition 9 (nested-triangle depth barrier).**  For every `r` there is
> a general-position set `P` of `n=3r` points partitioned into triangles
> `T_1,...,T_r` with
> \[
>  \operatorname{conv}T_{i+1}
>   \subset\operatorname{int}\operatorname{conv}T_i.                \tag{32}
> \]
> If `A` is a uniform random subset of `P`, then
> \[
>  \mathbb E D(A)\geq r/8=n/24.                                    \tag{33}
> \]

**Proof.**  Such configurations can be chosen inductively: put the next
triangle strictly inside the preceding one and avoid the finitely many
lines through pairs of points already chosen.  Let `Z` be the number of
triangles all three of whose vertices belong to `A`.  Then
`\mathbb E Z=r/8`.

For every fully selected `T_i`, consider the first onion layer that removes
one of its vertices.  Immediately before that layer all three vertices of
`T_i` remain.  Every point of every deeper triangle lies strictly inside
their convex hull, so no vertex of a deeper fully selected triangle can be
removed in the same layer or an earlier layer.  Thus the first-removal
layers of the fully selected triangles are all distinct, and
`D(A)\geq Z`.  Taking expectations proves (33). `square`

This disproves any universal `\mathbb E D(A)=o(n)` input to the onion
entropy method.  In particular, *many nested constant-size cages do not by
themselves force a short random onion code*.

For exact falsification tests, the checker uses the rational family
\[
 10^{-i}R^i\{(-3,-2),(3,-2),(0,4)\},\qquad
 R=\frac15\begin{pmatrix}3&-4\\4&3\end{pmatrix}.                  \tag{34}
\]
It verifies strict nesting and general position through eight layers and
exhausts all subsets through five layers.  The exact expected depths for
`r=1,...,5` are
\[
 \frac78,\ \frac{79}{64},\ \frac{53}{32},\ \frac{521}{256},\
 \frac{39523}{16384},
\]
all comfortably above `r/8`.

## 11. Two further barriers to extracting mass from cages

### 11.1 Convex-subset counts do not multiply across a cage

A tempting recurrence is
\[
 V(K\cup Q)\stackrel{?}{\geq}V(K)V(Q)                              \tag{35}
\]
when `Q` lies strictly inside the convex polygon `K`.  It is false already
for two triangles.  The exact general-position example
\[
 K=\{(-3,-2),(3,-2),(0,4)\},\qquad
 Q=\{(-1/50,-9/25),(17/50,3/25),(-8/25,6/25)\}
\]
has `V(K)=V(Q)=7`, but exhaustive exact arithmetic gives
\[
 V(K\cup Q)=47<49.                                                  \tag{36}
\]
Its convex-subset profile in sizes one through four is `(6,15,20,6)`;
there are no convex subsets of size at least five.  Thus even a perfect
constant-size cage recurrence needs a compatibility correction.

For the rational nested-triangle test family, the exact `(C,U,V)` values
for `r=1,...,5`, where `C` and `U` are total cap and cup counts, are
\[
 (7,6,7),\ (35,28,47),\ (106,82,190),\ (262,203,586),\
 (589,440,1511).                                                     \tag{37}
\]
These finite data are diagnostic only; Proposition 9, not the table, is
the rigorous asymptotic obstruction.

### 11.2 One representative per cage has zero coefficient surplus

Suppose the nested-cage corollary supplies `q=n^{1-o(1)}` cages, each of
size at most `s=n^{o(1)}`.  Even under the unrealistically favorable
assumption that every choice of one representative from each chosen cage
preserves the same order type, a convex `k`-subset of cage indices expands
into at most `s^k` point subsets.  At the relevant `k=Theta(log n)`,
\[
 \log(s^k)=k\log s=o((\log n)^2).                                  \tag{38}
\]
So this contributes no positive coefficient to the leading
`(log n)^2` exponent.  Any genuine improvement from the cage hierarchy
must use multiple occupancy of many cages, or a new nonlocal statement
forcing aligned cap/cup endpoints across cages.  Neither follows from hull
partition or onion entropy alone.
