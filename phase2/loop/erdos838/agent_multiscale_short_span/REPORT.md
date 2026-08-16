# Erdős 838: multiscale short-span escape

**Date:** 2026-08-14  
**Verdict:** every conjectural positive-power endpoint-marker inequality is
false.  An exact planar family has a full-span endpoint cell which is a
constant fraction of all mass retaining either endpoint, so no inequality
`s^a F_ij(1/2)<=O(E_ij)` can hold for any `a>0`.  The full-interval
compensation survives because the same family has `2^Theta(s)` unmarked
faces, but full-interval counts aggregate with an extra factor `s` and give
no decaying long-span tail.

The surviving full-interval span-squared inequality remains unresolved.  Its
sharp constant-one form is false on exact 16-, 20-, and 24-point
configurations (ratios up to `1.9529...`), but no infinite super-polylogarithmic
counterfamily was found.  It is proved below whenever
`V(P)>=2^{2(log n)^2}`.  If it holds in the remaining low-count regime, its
near-full-span aggregation combines naturally with a pocket restart.

For calibration, I also derive the global theorem that a hypothetical marker
exponent would have supplied.  Even if the now-refuted exponent `5/3` were
available, it would imply only

\[
 H(P)\le n^{1-1/\sqrt6+o(1)}
\]

for every minimum-count configuration.  Even after feeding this into the
deletion recurrence, it gives coefficient `1/(2 sqrt 6)=0.2041...`, less
than `1/4`.  More strongly, the marker method needs an exponent strictly
above `2` to bootstrap the present lower bound at all, and exponent `3` to
bootstrap all the way to `1/2`.

The aggregation, multiscale split, optimization, and bootstrap below are
unconditional consequences of the stated hypothetical inequality.  Together
with the counterfamily, they give a method barrier: dyadic interval recursion,
rotations, disjoint interval capacity, and ordinary smoothing of `f(n)` do
not repair the endpoint ladder.  A completion needs a charge allowed to
abandon both markers while retaining enough history to avoid congestion.

All logarithms are base two.  Put `h=1/2`, let

\[
 V(P)=Z_P(1),\qquad H(P)=\frac{nZ_P(h)}{V(P)},
\]

and order the points by a generic horizontal projection.  A nonsingleton
convex face with exact endpoint indices `i<j` is counted by

\[
 F_{ij}(z)=U_{ij}(z)C_{ij}(z).
\]

## 1. Exact counterexample to every positive marker exponent

Fix `M>=1`, put `B=(M+1)^2`, and take

\[
 \ell=(-1,-B),\qquad q_t=(t,t^2)\ (1\le t\le M),\qquad
 r=(M+1,-B).                                                  \tag{CF1}
\]

These integral points are in general position.  Let

\[
 A_M(z)=1+Mz+{M\choose2}z^2.                                 \tag{CF2}
\]

The face classification is exact:

* every subset of the parabola points is convex;
* a face containing `ell` but not `r` can use at most two `q_t`, and every
  such choice is convex;
* the reflected statement holds for `r`;
* a face containing both deep endpoints can again use at most two `q_t`,
  and every such choice is convex.

For `a<b<c`, direct expansion gives

\[
 \operatorname{orient}(q_a,q_b,q_c)
 =(b-a)(c-b)(c-a)>0,
\]

whereas

\[
 \operatorname{orient}(\ell,q_a,q_b)
 =(b-a)(ab+a+b-B)<0                                      \tag{CF2a}
\]

and

\[
 \operatorname{orient}(q_a,q_b,r)
 =(b-a)\{-B-a^2-(a+b)(M+1-a)\}<0.                        \tag{CF2b}
\]

All remaining triple types are also visibly nonzero.  The turn signs show
that among selected parabola points only the least and greatest can remain
vertices once either deep endpoint is present.  Conversely either endpoint
together with at most two parabola points is convex; with both endpoints and
two parabola points, the cyclic order `ell,r,q_b,q_a` has four strict turns
of the same sign.  This proves the classification for every `M`; the verifier
also checks every subset through `M=12`.  Consequently the full-span endpoint
cell is

\[
 F_{\ell r}(z)=z^2A_M(z),                                     \tag{CF3}
\]

the counts retaining the left or right marker are each `2A_M(1)`, and their
union is `3A_M(1)`.  In the notation of the endpoint report,

\[
 L_{\ell r}=R_{\ell r}=2A_M(1),\qquad
 E_{\ell r}=3A_M(1).                                         \tag{CF4}
\]

Since

\[
 \frac{F_{\ell r}(1/2)}{\max(L_{\ell r},R_{\ell r})}
 \longrightarrow\frac1{32},\qquad
 \frac{F_{\ell r}(1/2)}{E_{\ell r}}
 \longrightarrow\frac1{48},                                \tag{CF5}
\]

we obtain:

> **Proposition 1 (marker-power obstruction).**  For every `a>0` and every
> constant `C`, the inequality
> \[
>  s^aF_{ij}(1/2)\le C E_{ij}
> \]
> fails on planar general-position point sets.  The same is true with
> `max(L_ij,R_ij)` on the right.

The compensation abandons both markers.  The complete count is

\[
 V(P_M)=2^M+3A_M(1),                                         \tag{CF6}
\]

so the full-interval mass is exponentially larger than the bad endpoint
cell.  This is the localization phenomenon from the earlier one-deep-endpoint
parabola family, now symmetrized so that retaining either marker is still
insufficient.

## 2. The unconditional global activity bound

There is a baseline bound which uses only the known count theorem and is
therefore fully rigorous.

> **Proposition 2 (rank split).**  Every minimum-count `n`-point
> configuration satisfies
> \[
>  \boxed{H(P)\le n^{3/4+o(1)}.}                              \tag{U1}
> \]

**Proof.**  For an integer `r`, split the half-partition function by face
size.  The large faces contribute at most `2^{-r}V(P)`, while the small faces
contribute at most

\[
 \sum_{k<r}{n\choose k}.
\]

The established lower bound is
`V(P)=f(n)>=2^{(1/4-o(1))(log n)^2}`.  Taking
`r=(1/4-o(1))log n`, with the secondary `o(1)` chosen slowly enough to
dominate the error in the count lower bound, makes the small-face term
`o(V(P))` on the same polynomial scale and gives
`Z_P(1/2)/V(P)<=n^{-1/4+o(1)}`.  Multiplication by `n` proves (U1).  QED.

Jensen gives only `mu>= (1/4-o(1))log n`, so feeding (U1) back through
deletion yields coefficient `1/8`, weaker than the already known `1/4`.
This is nevertheless the strongest unconditional `H` estimate obtained in
this lane once the marker inputs are removed.

## 3. Hypothetical marker input and its exact aggregation

For the interval `I=[i,j]`, of length `s=j-i+1`, let `E_I` count convex
faces in `P[I]` which retain at least one of the two interval markers.  The
strongest marker candidate suggested by the finite census was

\[
 \boxed{s^aF_{ij}(h)\le C E_I,\qquad a=5/3.}                 \tag{M_a}
\]

Proposition 1 refutes this for every positive `a`; we retain `(M_a)` below
only to quantify the strength a replacement charge would need.  The
one-marker candidate had `a=3/2`; the full-interval candidate has
exponent `2`, but its right side is `V(P[I])`, not `E_I`.  This distinction
is decisive.

> **Lemma 1 (fixed-span marker aggregation).**  If `(M_a)` holds, then for
> every `s>=2`,
> \[
>  \sum_{j-i+1=s}F_{ij}(h)\le \frac{4C}{s^a}V(P).            \tag{1}
> \]
> Consequently, for every `S>=2` and `a>1`,
> \[
>  \sum_{j-i+1\ge S}F_{ij}(h)
>  \le \frac{4C}{a-1}(S-1)^{1-a}V(P).                       \tag{2}
> \]

**Proof.**  At a fixed length `s`, a nonempty face can occur in a left-marker
sum only for the interval whose left marker is its exact left endpoint, and
in a right-marker sum only for the interval whose right marker is its exact
right endpoint.  It is therefore charged at most twice.  The harmless
constant terms in the definitions of the marker enumerators contribute at
most `2n<=2V(P)`.  Hence

\[
 \sum_{|I|=s}E_I\le4V(P).
\]

Sum `(M_a)` and then sum the convergent tail.  QED.

By comparison, if the right side is the whole interval count, then

\[
 \sum_{|I|=s}V(P[I])\le sV(P)+O(n).                         \tag{3}
\]

Indeed a face of horizontal span `d<=s` lies in at most `s-d+1<=s`
intervals of length `s`.  Thus the conjectural full-interval inequality
`s^2F_I(h)<=CV(P[I])` gives only `O(V(P)/s)` at fixed span and a logarithmic,
not decaying, tail.  Its nominal exponent `2` cannot be substituted for a
marker exponent `2`.

## 4. The short-span/cardinality split

The obstruction in (2) is the mass recursively trapped at spans below `S`.
There is a sharp elementary way to isolate it.

> **Lemma 2 (two-parameter split).**  Under `(M_a)`, for integers
> `3<=r<=S<=n`,
> \[
> \frac{Z_P(h)}{V(P)}
> \le 2^{-r}
> +O_a(CS^{1-a})
> +\frac{n(r+1)(eS/r)^r+O(n^2)}{V(P)}.                      \tag{4}
> \]

**Proof.**  Faces of size at least `r` have total half-weight at most
`2^{-r}V(P)`.  Nonsingleton faces of horizontal span at least `S` are bounded
by (2).  Every remaining face has exact span below `S` and size below `r`.
For each possible left endpoint it is a subset of at most `S` consecutive
points, so their number is at most

\[
 n\sum_{k<r}{S\choose k}
 \le n(r+1)(eS/r)^r.
\]

Weights are at most one.  Empty sets, singletons, pairs, and boundary
conventions are absorbed in `O(n^2)`.  QED.

This split explicitly resolves recursive trapping: a trapped face either
eventually accumulates `r` vertices, at which point activity supplies
`2^{-r}`, or it remains a low-cardinality object in a short interval, whose
total number is the last term of (4).  No fixed loss is multiplied down an
onion or dyadic depth.

## 5. The optimized global bound

Suppose a class of configurations satisfies

\[
 V(P)\ge2^{(c-o(1))(\log n)^2}.                              \tag{5}
\]

For the minimizers in Erdős 838 we may take `c=1/4`, by the established
unrestricted lower bound.  In (4), set

\[
 S=n^{\theta+o(1)},\qquad r=(x+o(1))\log n.
\]

The logarithm of the last numerator in (4) is

\[
 (x\theta+o(1))(\log n)^2.
\]

It is negligible relative to `V(P)` whenever `x theta<c`.  The first two
terms of (4) are then `n^{-x+o(1)}` and
`n^{-theta(a-1)+o(1)}`.

> **Theorem 3 (conditional marker-to-activity transfer).**  Assume `(M_a)`
> with `C=n^{o(1)}` and (5).  Then
> \[
>  H(P)\le n^{1-\delta(c,a)+o(1)},                            \tag{6}
> \]
> where
> \[
> \boxed{
> \delta(c,a)=\max_{0<\theta\le1}
>       \min\{\theta(a-1),c/\theta\}
> =\begin{cases}
>   \sqrt{c(a-1)},&c\le a-1,\\
>   a-1,&c>a-1.
>  \end{cases}}                                             \tag{7}
> \]

The equality follows by balancing `theta(a-1)=c/theta`, unless the
balancing point exceeds one.

For the currently relevant values `c=1/4`, this gives

\[
\begin{array}{c|c|c}
 a&\delta(1/4,a)&H(P)\text{ exponent}\\ \hline
 3/2&1/(2\sqrt2)=0.353553\ldots&0.646446\ldots\\
 5/3&1/\sqrt6=0.408248\ldots&0.591751\ldots\\
 2&1/2&1/2.
\end{array}                                                  \tag{8}
\]

Again, the `a=2` row would require a marker inequality of exponent two.  The
observed full-interval exponent two does not have the aggregation (1).

## 6. Deletion smoothing and the exact bootstrap threshold

Jensen turns (6) into

\[
 \mathbb E_{A\text{ uniform convex}}|A|
 \ge(\delta(c,a)-o(1))\log n.                                \tag{9}
\]

For a minimum-count configuration, omitted-point double counting gives

\[
 (n-\mu_n)f(n)\ge nf(n-1).                                  \tag{10}
\]

Summing `-log(1-mu_n/n)` shows that (9) upgrades the counting coefficient
from `c` to at least

\[
 T_a(c)=\frac12\delta(c,a).                                  \tag{11}
\]

This summation is the needed jump smoothing.  It requires no pointwise
regularity assumption on `f(n)`: upward jumps only help, while (10) supplies
the lower logarithmic increment at every intervening integer.

In the relevant branch `c<=a-1`, repeated use of the marker theorem would
therefore update

\[
 c\longmapsto\max\left\{c,\frac12\sqrt{c(a-1)}\right\}.       \tag{12}
\]

Its positive fixed point is

\[
 \boxed{c_*=(a-1)/4.}                                       \tag{13}
\]

This yields the exact exponent thresholds:

* `a<2`: the fixed point lies below `1/4`, so the marker argument cannot
  improve the existing result;
* `a=2`: it merely reproduces `1/4`;
* `2<a<3`: it can improve `1/4`, but saturates below `1/2`;
* `a=3`: iteration tends to the desired `1/2`;
* `a>3`: the upper construction caps the conclusion at `1/2`.

For `a=5/3`, (11) is only

\[
 \frac1{2\sqrt6}=0.204124\ldots<\frac14.                    \tag{14}
\]

Thus the strongest current marker candidate does not create even a strict
coefficient improvement by this route.

There is a useful regular-model check.  If
`log f(n)=c(log n)^2+o(log^2 n)`, then

\[
 \log f(n)-\log f(n-1)
   =(2c+o(1))\frac{\log n}{n\ln2}.                            \tag{15}
\]

Equation (10) is compatible with every mean coefficient at most `2c`.
The marker transfer forces coefficient `delta(c,a)`, so it improves the
quadratic count exactly when `delta(c,a)>2c`, equivalently `c<(a-1)/4`.
The barrier is therefore present already for a perfectly smooth `f`; it is
not caused by exceptional jumps.

## 7. Dyadic intervals do not add a hidden contraction

For completeness, short intervals do possess a clean two-grid cover.  Fix
`m`.  The windows

\[
 B_q=[qm+1,(q+2)m]
\]

contain every interval of length at most `m`.  Even and odd `q` form two
families of pairwise disjoint windows.  Therefore

\[
 Z_P(h;\operatorname{span}\le m)
 \le\sum_q Z_{P[B_q]}(h).                                    \tag{16}
\]

Within either parity, nonempty face sets are disjoint and

\[
 \sum_{q\equiv\epsilon(2)}V(P[B_q])\le V(P)+O(n/m).          \tag{17}
\]

Equations (16)--(17) are exactly the hoped-for disjoint-interval capacity
statement.  But they have coefficient one rather than a strict contraction.
All the mass is allowed to lie in one nested child window at every scale.
Iterating (16) therefore transfers the same unresolved ratio
`Z(h)/V` to a shorter interval; it does not decrease it.  Lemma 2 is sharper:
it follows the trap to its terminal span and charges it either by cardinality
or by the total number of available subsets.  Its optimization is (7).

This also explains why ordinary laminar recursion and `f`-jump selection do
not beat Theorem 3.  A scalar mass can follow a single nested chain, so the
disjoint-sibling inequality never fires.  At the terminal interval the
capacity exponent is precisely `x theta`, the last term in (4).  A proof
beyond (7) must use a geometric fact which makes a trapped parent create
mass outside that one child, not merely the fact that its children are
disjoint.

## 8. What rotations can and cannot buy

Here is an intentionally optimistic audit.  Suppose there are
`R=n^{rho+o(1)}` generic projection directions such that every relevant
convex face has span at least `n^{theta-o(1)}` in at least one direction;
suppose the exceptional half-weight is negligible.  Apply (2) in each
direction and add.  Since `V(P)` is rotation invariant,

\[
 H(P)\le n^{1+\rho-\theta(a-1)+o(1)}.                         \tag{18}
\]

Even the impossible best case `rho=0, theta=1` gives, for `a=5/3`, only

\[
 H(P)\le n^{1/3+o(1)},\qquad \mu\ge(2/3-o(1))\log n,          \tag{19}
\]

and hence counting coefficient `1/3`, not `1/2`.  A perfect rotation cover
would be a real coefficient improvement, but still would not close #838.
To obtain `H=n^{o(1)}` from (18), one needs

\[
 \theta(a-1)\ge1+\rho.                                      \tag{20}
\]

Thus a constant-size full-span cover requires marker exponent at least two.
The actual geometric premise is itself false without a recursive exception:
a face supported in a tiny, far-separated cluster can have short projection
span in every direction.  Such faces must be paid for by cross-cluster convex
mass.  Neither rotation invariance nor (17) supplies that payment.

### A sharper live route using full-interval localization

The surviving (but unproved) candidate

\[
 s^2F_{ij}(1/2)\le C V(P[i,j])                              \tag{FI2}
\]

has no marker and therefore escapes Proposition 1.  Its usual harmonic
aggregation is weak, but at *near-full* span there is an extra boundary
factor which is worth recording.  At fixed length `s`, there are only
`n-s+1` intervals, so

\[
 \sum_{|I|=s}V(P[I])
 \le \min\{s+1,n-s+1\}V(P).                                \tag{21}
\]

Consequently `(FI2)` gives, for `1<=T<=n/2`,

\[
 \boxed{
 \sum_{j-i+1\ge n-T}F_{ij}(1/2)
 \le O(C)\frac{T^2}{n^2}V(P).}                              \tag{22}
\]

This changes the rotation threshold substantially.  If
`R=n^{rho+o(1)}` directions cover every relevant face with projection-span
deficit at most `T=n^{theta+o(1)}` in at least one direction, then (22) gives

\[
 H(P)\le n^{\rho+2\theta-1+o(1)}.                           \tag{23}
\]

Thus `(FI2)` plus a subpolynomial family of directions giving deficit
`n^{1/2+o(1)}` would prove `H=n^{o(1)}`.  This is much more economical than
the false marker ladder.  The geometric cover is not true literally for
faces trapped in a small separated cluster.  The viable replacement is a
**near-full-span-or-restart lemma**: every face must either have (22) in one
of few directions, or enter a decodable strict pocket, with pocket exceptions
obeying the same statement recursively and with only subpolynomial total
congestion.  This couples exactly to the pocket-restart report.

## 9. The exact remaining multiscale lemma

The exponent audit leaves a narrow target.  One needs a **superlinear escape
from a trapped interval**, for example a statement of one of the following
forms.

1. A history-retaining charge which may abandon both markers and has
   effective exponent above two; exponent three, together with the bootstrap
   above, closes the theorem.  Proposition 1 shows that a literal marker
   inequality cannot be this charge.
2. A recursive compensation theorem saying that if a fraction `eta` of
   half-weight remains in one short child, then the parent has at least
   `n^{gamma}` times as much *new* count mass outside the child, with the
   losses telescoping along a nested chain.
3. A cross-direction theorem which treats a face short in every projection
   as belonging to a separated cluster and charges it to endpoint-compatible
   cross-cluster faces with subpolynomial congestion.
4. Most concretely, prove `(FI2)` and the near-full-span-or-restart lemma
   following (23).  Their numerical threshold is sharp enough to close the
   half-weight theorem without any positive marker exponent.

The key word is *new*: lower bounds on the child's own `V`, disjointness of
sibling intervals, and smoothness of `f` are already fully represented by
(4), (16), and (10), and have the ceiling (13).

## 10. Direct audit of full-interval span-squared localization

The targeted surviving conjecture is

\[
 \boxed{m^2F_{ij}(1/2)\le (\log m)^{O(1)}V(P[i,j]).}          \tag{FI2'}
\]

I found neither a proof nor an infinite counterfamily.  Two rigorous pieces
substantially narrow its status.

### 10.1 Constant one is false

There are exact integral, general-position configurations for which
`m^2 F/V>1`.  Take `p_i=(i,M pi_i+i^2)` with `M=10^6` and the following
permutations:

\[
\begin{array}{c|c|c|c}
m&\pi&F_{0,m-1}(1/2)&m^2F/V\\ \hline
16&(0,3,4,5,6,7,8,9,10,2,1,12,13,14,15,11)
  &75/4&960/611=1.57119\ldots\\
20&(18,0,19,3,10,17,16,9,15,8,14,7,13,5,12,4,11,2,1,6)
  &2773/64&69325/38632=1.79449\ldots\\
24&(19,23,22,21,20,3,9,18,17,8,16,15,7,14,6,13,5,11,12,10,2,1,0,4)
  &23511/256&70533/36116=1.95295\ldots
\end{array}                                                  \tag{24}
\]

The verifier orders every edge by its exact rational slope, forms the forward
and reverse transvection products at activities one and one-half, and checks
every orientation determinant.  Thus (24) is stretchable evidence, not an
allowable-sequence artifact.  The ratios rise across these finite examples,
so any proof needs a genuine constant or polylogarithmic loss.  I did not
find a scalable version: extending the long almost-linear runs creates
exponentially many unmarked convex subsets and makes the ratio fall.

### 10.2 The high-count regime is proved

> **Proposition 3 (high-count FI2).**  Let `Q` have `m` points.  If
> \[
>  V(Q)\ge2^{2(\log m)^2},                                    \tag{25}
> \]
> then, uniformly over every endpoint pair,
> \[
>  m^2F_{ij}(1/2)\le(1+o(1))V(Q).                            \tag{26}
> \]

**Proof.**  Put `L=log m` and `r=ceil(2L)`.  All faces of size at least `r`
have total half-weight at most `2^{-r}V(Q)<=m^{-2}V(Q)`.  The total number
of smaller faces, without using geometry, is at most

\[
 r(em/r)^r
 =2^{2L^2-2L\log L+O(L)}=o(m^{-2}V(Q))
\]

under (25).  Since one endpoint cell is bounded by the whole half-partition
function, (26) follows.  QED.

Thus a counterfamily to `(FI2')` must live in the low-count regime
`log V<2log^2m`; Boolean pockets, large convex layers, and the two-deep
wrapper are automatically harmless.  The hard regime still includes all
known minimizers, whose count exponent lies between `1/4` and `1/2`.

### 10.3 Strongest exact substitute: activity or dilution

Put `R_ij=F_ij(1)` and let `mu_ij` be the endpoint-cell mean at half
activity.  Jensen gives

\[
 \frac{R_{ij}}{F_{ij}(1/2)}\ge2^{\mu_{ij}}.
\]

Writing `d_ij=log(V(P[i,j])/R_ij)`, we obtain the exact sufficient estimate

\[
 \boxed{
 \frac{m^2F_{ij}(1/2)}{V(P[i,j])}
 \le2^{\,2\log m-\mu_{ij}-d_{ij}}.}                         \tag{27}
\]

Hence `(FI2')` follows from the corrected local dichotomy

\[
 \mu_{ij}+d_{ij}\ge2\log m-O(\log\log m).                   \tag{AD2}
\]

This is the strongest viable pointwise substitute isolated here.  It permits
both markers to be abandoned through `d_ij`, so the exact counterfamily in
Section 1 has exponential slack.  Unlike the false marker ladder, `(AD2)`
matches both known compensation mechanisms.  Proving it appears to require a
weighted cup--cap supersaturation theorem; generic downsets with a complete
three-skeleton do not satisfy it.

Combining `(AD2)`/`(FI2')` with the near-full estimate (22) gives a concrete
two-lemma route to the theorem: prove activity-or-dilution, then prove the
near-full-span-or-restart cover with square-root span deficit and decodable
pocket history.  The first lemma is pointwise and the second is precisely the
global bounded-congestion step.

## 11. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_multiscale_short_span/verify_multiscale.py
```

The script:

* verifies the exact deep-endpoint parabola counterfamily through `M=12`;
* verifies the three exact stretchable `(FI2)` certificates in (24), including
  all determinant signs and rational forward/reverse products;
* exhaustively checks the fixed-span endpoint-marker incidence bound on all
  downsets on up to four labeled vertices;
* checks the two shifted dyadic-window cover;
* evaluates the optimizer (7), the bootstrap fixed points, and the rotation
  ceiling using exact rational arithmetic where possible;
* verifies numerically that the finite differences of the smooth model
  `2^{c(log n)^2}` approach the coefficient `2c` in (15).

No solution of Erdős 838 is claimed.  The positive theorem is the conditional
transfer (6); the main conclusion is that the marker exponent ladder is not
merely too weak but false.  The surviving full-interval compensation must be
converted into a history-retaining, bounded-congestion escape by a genuinely
new geometric argument.
