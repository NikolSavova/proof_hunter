# A mean-size/lattice route to Erdős 838

> **Date:** 2026-08-13
> **Status:** exact reductions and conditional targets; no claimed unrestricted
> lower bound beyond the known one.

All logarithms are base two.  For a general-position planar point set `P`, let

\[
 \mathcal I(P)=\{A\subseteq P:A\text{ is in convex position}\},\qquad
 Z_P(z)=\sum_{A\in\mathcal I(P)}z^{|A|}.
\]

Here the empty set may be included.  This changes all logarithmic estimates by
`O(1)` and makes the closure-lattice formulation exact.  Put

\[
 V(P)=Z_P(1),\qquad
 \mu(P)=\frac{Z'_P(1)}{Z_P(1)}
       =\mathbb E_{A\text{ uniform in }\mathcal I(P)}|A|.
\]

The point of this note is that a sharp lower bound on `mu(P)` would solve the
problem by deletion, while a slightly more intrinsic quadratic relation between
`log V(P)` and `mu(P)` would do the same.  Both statements are compatible with
the known coefficient-`1/2` constructions.  Neither is currently proved for
arbitrary point sets.

## 1. Exact affine-convexity reformulation

Define the closure operator

\[
 \operatorname{cl}(A)=P\cap\operatorname{conv}(A).
\]

Its closed sets form the affine convex geometry of `P`.  The maps

\[
 A\longmapsto\operatorname{cl}(A),\qquad
 K\longmapsto\operatorname{ext}(K)
\]

are inverse bijections between `mathcal I(P)` and the closed sets.  Indeed, if
`A` is in convex position, the extreme points of `cl(A)` are exactly `A`; and a
finite closed set is the convex hull of its extreme points.  Consequently,

\[
 V(P)=\#\{K\subseteq P:K=P\cap\operatorname{conv}(K)\}.                 \tag{1}
\]

Moreover, deleting an extreme point from a closed set leaves a closed set, and
these are precisely its lower covers in the closure lattice.  Therefore

\[
 \mu(P)=\frac{\#\{\text{edges in the Hasse diagram, directed downward}\}}
                   {\#\{\text{closed sets}\}}.                         \tag{2}
\]

Thus the desired lower bound may be viewed as an average down-degree theorem
for rank-three realizable affine convex geometries.  General convex geometries
cannot satisfy such a theorem: their closure lattices can be essentially
chain-like.  Planar realizability and general position are load-bearing.

There is also an exact bivariate identity worth retaining.  The Boolean
intervals

\[
 [\operatorname{ext}(K),K]
\]

over closed `K` partition `2^P`.  If `h(K)=|ext(K)|` and
`i(K)=|K|-h(K)`, then weighting every subset by `t` per point gives

\[
 \boxed{(1+t)^n=\sum_{K\text{ closed}}
        t^{h(K)}(1+t)^{i(K)}.}                         \tag{BI}
\]

At `t=1` this is the hull-partition identity
`2^n=sum_K 2^{i(K)}`.  Its derivative says that under the *hull-weighted*
law proportional to `2^{i(K)}`, the mean of `h(K)+i(K)/2` is `n/2`.
This does not directly control the uniform mean `mu(P)`—the two measures can
be exponentially different—but it is an exact interface for any successful
change-of-measure argument.

## 2. The deletion lemma

Let `f(n)` be the minimum of `V(P)` over `n`-point general-position sets.  If
`P` is a minimizer and `I_p` is the number of convex subsets containing `p`,
then

\[
 \sum_{p\in P}I_p=\mu(P)V(P).
\]

Choose `p` with `I_p>=mu(P)V(P)/n`.  Since the convex subsets of `P-p` are
exactly those convex subsets of `P` not containing `p`,

\[
 f(n-1)\le V(P-p)=V(P)-I_p
 \le f(n)\left(1-\frac{\mu(P)}n\right).                                 \tag{3}
\]

This proves the following conditional theorem.

**Mean-size criterion.**  If every `n`-point general-position planar set
satisfies

\[
 \mu(P)\ge (1-o(1))\log n,                                               \tag{MS}
\]

then

\[
 \log f(n)\ge\left(\frac12-o(1)\right)(\log n)^2.
\]

In fact `mu(P)>=log n-O(1)` gives
`log f(n)>=.5 log^2 n-O(log n)`.  To see this, take base-two logarithms in
(3), use `-log_2(1-x)=x/ln 2+O(x^2)`, and sum.  Since

\[
 \sum_{m\le n}\frac{\log_2m}{m\ln2}
   =\frac12(\log_2n)^2+O(1),
\]

the coefficient is exactly `1/2`.

The same argument only needs (MS) for minimizers, or more generally whenever
`V(P)` is below the target lower bound.

## 3. The natural quadratic inequality is false

A stronger-looking but scale-natural target would have been

\[
 \log V(P)\le\left(\frac12+o(1)\right)\mu(P)^2.                          \tag{QMS}
\]

If (QMS) held uniformly in the regime `mu(P)->infinity`, (3) would yield, in
the continuous variable `L=log n`,

\[
 \frac{d}{dL}\log f(2^L)\gtrsim\sqrt{2\log f(2^L)}.
\]

Equivalently, the derivative of `sqrt(2 log f(2^L))` is asymptotically at
least one, and hence `log f(n)>=.5 log^2 n-o(log^2 n)`.  A rigorous discrete
version follows by retaining an `o(mu^2)` error modulus and using blocks of
`L` on which it is uniform.

But the second-wave audit disproved (QMS) even for rational
mirror-decomposable point sets.  For the balanced Pascal cell
`Q_m=T_(m,m/2)`, every convex subset has at most `m` points, whereas

\[
 \log V(Q_m)=\left(1-\frac1{4\ln2}\right)m^2+O(m\log m).
\]

Thus

\[
 \liminf_m\frac{\log V(Q_m)}{\mu(Q_m)^2/2}
 \ge 2-\frac1{2\ln2}=1.278652\ldots>1.
\]

Universal QMS must therefore not be used.  A weaker target still suffices:
for minimizers of `f(n)`, prove that either (MS) holds or QMS holds only in
the complementary low-mean branch.  Either branch gives
`mu(P_n)>=(1-o(1))sqrt(2 log f(n))`; the exact deletion recurrence then
integrates to coefficient `1/2`.  This **low-mean minimizer dichotomy** is
compatible with the Pascal cells, which lie in the high-mean branch, but it
is currently conjectural.

## 4. Exact weak bounds and why they are insufficient

Entropy gives, for every down-set on `n` vertices with uniform random face of
mean size `mu`,

\[
 \log V\le nH_2(\mu/n)
          \le\mu\log\frac{en}{\mu}.                                     \tag{4}
\]

The same estimate follows from Jensen: for `0<p<1`,

\[
 \frac{Z_P(p)}{V(P)}=\mathbb E p^{|A|}\ge p^{\mu(P)},
\]

and `Z_P(1/n)<=(1+1/n)^n<e`.  These bounds force only
`mu(P)>=log V(P)/(log n+O(loglog n))`.  At the conjectural scale this is about
`(.5 log n)`, not `log n`; feeding it into (3) does not bootstrap the known
coefficient.  Therefore an entropy-only proof cannot close the gap.

Likewise, the existence of a convex `r`-set does not control `mu`: an arbitrary
down-set may contain one `r`-simplex while being dominated by its many edges.
Any proof must use multiplicity or extension structure.

## 5. Evidence and sharpness checks

The exact reduced-word census in `root_order_exhaust.py` gives the following
minimum-mean data over all type-A reflection orders (not only stretchable
ones):

| `n` | exhausted words | minimum `V` at `n` | smallest observed `mu-log n` |
|---:|---:|---:|---:|
| 2 | 1 | 3 | positive |
| 3 | 2 | 7 | positive |
| 4 | 16 | 14 | positive |
| 5 | 768 | 26 | positive |
| 6 | 292864 | 44 | `-0.130417...` |

Thus the zero-error inequality `mu>=log n` is already false, while
`mu>=log n-O(1)` remains plausible.  Random reduced words through `n=16` had
minimum sampled deficits between about `-0.09` and `+0.39`; this is evidence,
not a certificate about minima.

The fixed-template vertical blow-ups attaining the upper coefficient `1/2`
also predict sharpness of (MS).  If a template has `r` blocks, largest cap
size `a`, and largest cup size `b`, then its depth-`d` iterate has
`log N=d log r`.  The graded cap and cup recurrences show that their typical
sizes are respectively

\[
 (a-1)d+O(1),\qquad (b-1)d+O(1),
\]

and the crossing term dominating `V` has typical size

\[
 (a+b-2)d+O(1).
\]

The cup--cap bound gives `log r<=a+b-2`.  Hence these constructions have
`mu(P)>=log N+O(1)`, with asymptotic equality in the balanced extremal
templates.  So an (MS) theorem would be both sufficient and sharp on the known
upper family.

## 6. Concrete attack questions

1. **Closure-lattice expansion.**  Prove that every realizable rank-three
   affine convex geometry on `n` elements has average down-degree at least
   `log n-O(1)`.  The exact input should be the rooted four-point circuits of a
   planar order type, not generic meet-distributivity.
2. **Low-mean minimizer dichotomy.**  Universal QMS is false.  Prove it only
   for minimizers that fail (MS), using the interior statistic in (BI).
3. **Counterexample search.**  Minimize `mu-log n` under braid moves and test
   stretchability of records.  A deficit tending to `-infinity` kills (MS).
4. **Local-to-global version.**  It suffices to prove (MS) for minimizers.  A
   structural dichotomy may be easier: either the average down-degree is
   large, or interior-weight anti-concentration forces the sharp quadratic
   relation in that low-mean branch.
5. **Literature gate.**  The relevant language is the complex of independent
   sets of an affine convex geometry (equivalently, an antimatroid), not the
   ``free complex'': in standard convex-geometry terminology a free set is
   additionally closed and corresponds to an *empty* convex polygon.  The
   bijection between closed sets and independent sets via `ex` and `cl`, and
   the Boolean-interval partition of the Boolean lattice, are standard; no
   average-down-degree theorem of the required strength was found in the
   initial narrow search.  This needs a proper convex-geometry/antimatroid
   prior-art sweep before novelty is asserted.

The route is attractive because it converts the coefficient into a first
moment and makes deletion exact.  Its current weakness is equally clear: the
needed first-moment inequality is essentially a geometric expansion theorem,
and arbitrary antimatroids or down-sets do not possess it.
