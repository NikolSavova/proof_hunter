# Counting the Baek--Balko new `x`-blow-up: a `1/2` barrier for the
# canonical Pascal instantiation

All logarithms are base two.  This note analyzes Definition 17 and Theorem 19
of the SoCG version of Baek--Balko (the same construction is in Section 6 of
the full JCTA article).  Put
\[
 m=k-2x,\qquad d=m-3=k-2x-3,
 \qquad \theta={x\over k},\quad \mu=1-2\theta.
\]
Their construction has exactly
\(N=2^{k-2}\) points and no \(k\) in convex position.

The conclusion is:

* for every fixed `theta<1/2`, the realization in which every ordinary `P'`
  cluster is the canonical Erdős--Szekeres Pascal cell cannot improve
  coefficient `1/2`; the fully canonical special endpoint clusters also
  cover the degenerate `m=3` sequence, as explained after the theorem;
* for arbitrary, noncanonical extremal `P'(a,u)` clusters, the same argument
  is unconditionally above `1/2` up to the conservative split
  `theta=0.21` (the numerical root of `T(theta)=1/2` is
  `0.21616144...`); beyond that point, evaluating the construction requires
  new convex-subset lower bounds for arbitrary extremal cap--cup
  configurations.  The notation `P'` in
  Baek--Balko deliberately permits that freedom.

Thus the new macro order type `M` does not produce a sub-`1/2` candidate with
the Pascal-cell enumerators requested here.  The only remaining loophole in
this construction is not `M`; it is replacing its internal Pascal cells by
presently uncontrolled nondecomposable extremal cap--cup sets.

## 1. Exact all-subset identity

Let the points of `M`, in horizontal order, be `p_1,...,p_R`, and let `Q_i`
be the cluster replacing `p_i`.  Write `n_i=|Q_i|`.  Let `L_i` count the
nonempty left convex chains in `Q_i` and `R_i` the nonempty right convex
chains.  Under Baek--Balko's clockwise rotation these are respectively the
cap and cup enumerators of the unrotated `P'` configuration (with the names
interchanged if the opposite orientation convention is used).

The endpoint-cluster classification underlying their Lemma 14 gives the
following exact count of **all** nonempty convex subsets:
\[
\boxed{
 W(b_{x,k,L}(M))=
 \sum_i W(Q_i)+
 \sum_{\substack{B\subseteq M\text{ convex}\\|B|\ge2}}
 L_{\min B}R_{\max B}
 \prod_{p_i\in B\setminus\{\min B,\max B\}}n_i.} \tag{1}
\]
Indeed, the support `B` of occupied clusters is uniquely determined.  Only
its first and last clusters can have multiple selected points; they form a
left and right chain, while every intermediate occupied cluster contributes
one arbitrary point.  Conversely, those choices form the two hull chains.

Formula (1) is the appropriate exact DP target.  It also isolates the hard
part: one needs the endpoint-resolved convex-subset enumerator of `M`, not
just the score distribution `v_{j,L}(M)` used in the Baek--Balko cardinality
calculation.  Sections 2--4 extract enough of (1) to settle the canonical
sub-`1/2` question without evaluating the remaining terms.

## 2. Exact order-type labeling of `M`

Definition 17 builds `M=P' union P''`, where each half is a full
Erdős--Szekeres Pascal row of depth `d`.  More explicitly, the left layer at
`ell_(h+2)` is
\[
 P(m-h-1,h+2),\qquad h=0,\ldots,d,
\]
and has `binom(d,h)` points.  The right layers have the reflected indexing.
Thus the points in either half can be labeled by subsets
\(A\subseteq[d]\), with layer \(|A|=h\).

The endpoint-rank induction in the proof of Baek--Balko's Lemma 18 refines
as follows.  Within the cell `T_(d,h)`, the longest right-hull chain ending
at a label `A` has length

```
r(A)=max(A)-h+1.                                  (2a)
```

This follows by induction over the Pascal split: a label in the left child
inherits its terminal chain, while a label in the right child may prepend
exactly one point from the left child.  The same induction bounds a convex
subset contained in `T_(d,h)` and ending at nonempty `A` by `max(A)` points.

Now consider a convex set in the full row ending at `A` and first meeting an
earlier layer `a`.  The endpoint-cluster classification gives a cap of size
at most `a+1` in its first layer, at most one point in each intermediate
layer, and a terminal chain of size at most `r(A)`.  Its total size is at
most

```
(a+1)+(h-a-1)+r(A)=1+max(A).                     (2b)
```

Equality is obtained by starting in the singleton layer zero, taking one
point in every intermediate layer, and using a terminal chain of length
`r(A)`.  The empty label has rank one.  Hence
\[
 s(A)=
 \begin{cases}
 1,&A=\varnothing,\\
 1+\max A,&A\ne\varnothing.
 \end{cases}                                      \tag{2}
\]
Therefore, within layer `h>=1`, the number of points of score `t+1` is
\[
 \binom{t-1}{h-1},\qquad h\le t\le d.             \tag{3}
\]
Summing (3) over `h` gives `2^(t-1)` points of score `t+1` in each half.
Doubling recovers Baek--Balko's displayed formula
`v_(t+1),L(M)=2^t`, while the two empty labels give `v_1=2`.  This is an
independent consistency check on the reconstruction.

For a nonendpoint left point of score `j`, the `x`-blow-up parameters are
\[
 x_i=x,\qquad y_i=k-1-x-j,
\]
so its cluster size is
\[
 n_j=\binom{k-j-1}{x}.                            \tag{4}
\]
The empty-label layer is the extreme point and receives the special cluster
of size
\[
 n_1=\sum_{ell=0}^x\binom{k-2}{ell}.              \tag{5}
\]

## 3. A large transversal family independent of the micro order types

The centers `ell_2,...,ell_(m-1)` form a convex chain.  Choose one point of
`M` from every left layer and then one point from the output cluster attached
to each chosen point.  Every resulting set is convex: the first choice is a
transversal of sufficiently small copies around that center chain, and the
second choice preserves every orientation involving three distinct output
clusters.

Let `Z_h` be the number of choices from layer `h`.  Equations (3)--(5) give
the exact finite formulas
\[
 Z_0=\sum_{ell=0}^x\binom{k-2}{ell},              \tag{6}
\]
and, for `1<=h<=d`,
\[
 Z_h=\sum_{t=h}^d
       \binom{t-1}{h-1}\binom{k-t-2}{x}.          \tag{7}
\]
Consequently
\[
 W(b_{x,k,L}(M))\ge\prod_{h=0}^d Z_h.            \tag{8}
\]
This bound uses only cluster cardinalities and hence holds for every choice
of the arbitrary configurations `P'(a,u)` allowed by Definition 13.
As a finite check on (6)--(7), Vandermonde summation gives
`sum_(h=0)^d Z_h=2^(k-3)`, exactly half of the total cardinality
`2^(k-2)` proved in their Theorem 19.  The companion program asserts this
identity before returning the product.

For `h/k -> eta` and `t/k -> tau`, the largest summand in (7) has exponent
\[
 z_theta(eta)=
 \max_{eta\le tau\le\mu}
 \left[
 tau H_2\!\left({eta\over tau}\right)
 +(1-tau)H_2\!\left({theta\over1-tau}\right)
 \right].                                        \tag{9}
\]
The unrestricted Vandermonde maximizer is
`tau=eta/(eta+theta)`.  It is feasible exactly when `eta<=mu/2`.
When it is feasible, (9) equals `H_2(eta+theta)`; otherwise the maximum is
at `tau=mu`, where the second entropy is `H_2(1/2)=1`.  Thus
\[
 z_theta(eta)=
 \begin{cases}
 H_2(eta+theta),&0\le eta\le\mu/2,\\
 \mu H_2(eta/\mu)+2\theta,&\mu/2\le eta\le\mu.
 \end{cases}                                     \tag{10}
\]
A uniform entropy estimate followed by a Riemann sum in (8) yields
\[
 \log W(b_{x,k,L}(M))\ge(T(\theta)-o(1))k^2,      \tag{11}
\]
where
\[
\boxed{
 T(\theta)=
 \int_\theta^{1/2}H_2(s)\,ds
 +{(1-2\theta)^2\over4\ln2}
 +\theta(1-2\theta).}                            \tag{12}
\]
At `theta=0`, this is `1/(2 ln 2)`, the full-Pascal-row coefficient.
Moreover
\[
 T'(\theta)=
 -H_2(\theta)-{1-2\theta\over\ln2}+1-4\theta<0  \tag{13}
\]
on `[0,1/2]`: the last two nonentropy terms already form a negative,
strictly decreasing affine function.

In particular
\[
 T(0.21)=0.5087955456\ldots,                      \tag{14}
\]
so (11) alone rules out a sub-`1/2` coefficient for every
`theta<=0.21`, without any assumption on the internal order types.

## 4. The canonical score-two Pascal cell covers the remaining range

There are ordinary points of score two.  A left score-two cluster is a
clockwise rotation of
\[
 P'(k-x-1,x+2).
\]
Choose the canonical Pascal configuration `P(k-x-1,x+2)`.  It is the
Pascal cell of depth `k-3` and density `theta+o(1)`.  The exact cell
enumerator from the main Erdős 838 work gives
\[
 \log W(P(k-x-1,x+2))=(I(\theta)-o(1))k^2,        \tag{15}
\]
where
\[
\boxed{
 I(\theta)=H_2(\theta)-{\theta(1-\theta)\over\ln2}.} \tag{16}
\]
Every one of these subsets remains convex in the full blow-up.  The function
`I` is increasing on `[0,1/2]`, since
\[
 I'(\theta)={1\over\ln2}
 \left(\ln{1-\theta\over\theta}-(1-2\theta)\right)>0. \tag{17}
\]
The last inequality follows, for example, by differentiating the bracket
from its value zero at `theta=1/2` toward the left.  Numerically,
\[
 I(0.21)=0.5021396326\ldots.                      \tag{18}
\]

Combining (11) and (15)--(18) proves the promised barrier.

> **Theorem (canonical Baek--Balko blow-up barrier).**  If
> `x/k -> theta in [0,1/2)` and every ordinary `P'(a,u)` used in the new
> Baek--Balko `x`-blow-up is instantiated by the canonical Pascal
> configuration `P(a,u)`, then
> \[
> \liminf_{k\to\infty}
> {\log W(b_{x,k,L}(M))\over(\log N)^2}
> \ge\max\{T(\theta),I(\theta)\}
> \ge0.5021396326\ldots>{1\over2},                \tag{19}
> \]
> where `N=2^(k-2)`.

The exclusion of the endpoint `theta=1/2` is substantive in this particular
argument: when `m=k-2x=3` eventually, there is no ordinary score-two cluster,
so (15) is unavailable and canonicality of the ordinary clusters is vacuous.
The fully canonical construction is nevertheless covered.  Its two special
endpoint clusters are rotated copies of `P(k,x+2,k)` and `P(x+2,k,k)`, each
of size `2^(k-3)`.  The standard Section-4 realization of every `P(a,u,k)` is
decomposable, being a successive deep-below composition of decomposable
Pascal cells.  Reflection and the proved mirror-decomposable lower theorem
therefore give, inside either endpoint cluster,

```
log W >= (1/2)(k-3)^2-O(k^(3/2)).                (19a)
```

Since the full construction has `log N=k-2`, (19a) gives coefficient at
least `1/2`.  This endpoint conclusion requires canonicality of the special
`P'(a,u,k)` endpoint clusters, an extra hypothesis not implied merely by
canonicalizing the ordinary `P'(a,u)` cells.  If `m>=4` eventually, the
score-two cluster exists; in particular, (19) also applies to sequences
`theta->1/2` with `m>=4`, by the same formulas and their endpoint limits.

The harmless replacement of `k^2` by `(k-2)^2=(log N)^2` does not change
the limit.  The constant in (19) is a convenient certified cover obtained
by splitting at `theta=0.21`, not the optimum; the two curves cross near
`theta=0.2126`, where their maximum is about `0.505`.

## 5. Exact computation and the remaining obstacle

The companion script `bb_xblowup_barrier.py` computes (8) and the exact
Pascal-cell recurrence in (15) with arbitrary-precision integers.  For
example:

```text
python3 bb_xblowup_barrier.py --k 120
```

prints the finite coefficients together with their limits.  Finite
convergence is slow because both constructions have `O(k log k)` lower-order
entropy corrections, but the values move toward (12) and (16).

Formula (1) explains why this is not yet an exact asymptotic evaluation of
the entire blow-up.  The published statistic `v_(j,L)(M)` records only one
endpoint rank per macro point.  It does not give, for every endpoint pair,
the number of convex supports and their intermediate score profile, which is
the weighted quantity in (1).  The two Pascal-row halves are individually
recursive, but their cross-half triples in Definition 17 are not a strong
binary glue, so the three-state `(C,U,W)` recurrence does not close across
their union.

For arbitrary `P'(a,u)`, there is a second and more fundamental obstacle.
Replacing (15) by an equally strong statement would require proving that
every extremal `binom(a+u-4,a-2)`-point configuration with no `a`-cap and no
`u`-cup already has
`2^((I(theta)-o(1))k^2)` convex subsets.  That is a new unrestricted
supersaturation theorem of essentially the same nature as Erdős 838, and it
does not follow from the cap--cup theorem or from Baek--Balko's size lemma.

Accordingly:

* **fully canonical construction:** rigorously not below `1/2`, by (19) for
  `m>=4` and by (19a) for `m=3`;
* **arbitrary clusters, `theta<=0.21`:** rigorously not below `1/2`, by the
  transversal family alone;
* **arbitrary clusters, `theta>0.21` (including noncanonical special
  endpoints when `m=3`):** unresolved by the present certificates,
  with the precise missing input being either the weighted endpoint DP in
  (1) for `M` or a lower bound for arbitrary extremal `P'(a,u)` cells.
