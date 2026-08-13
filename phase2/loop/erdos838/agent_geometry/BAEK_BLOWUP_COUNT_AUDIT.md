# Referee audit: the Baek--Balko `x`-blow-up count

## Verdict

The two lower-bound mechanisms in `BAEK_BLOWUP_COUNT.md` are correct for
every limiting ratio `theta<1/2`, and they do rule out a sub-`1/2`
coefficient for the canonical Pascal instantiation.  The layer weights,
the transversal geometry, the two entropy limits, and the numerical cover
all survive independent reconstruction.

The displayed theorem is **not correct as stated at the endpoint
`theta=1/2`**.  It needs either `theta<1/2`, the additional hypothesis that
`m=k-2x>=4` eventually, or an explicit canonicality assumption on the two
special endpoint configurations `P'(a,u,k)`.  When `m=3` there is no
score-two ordinary cluster, so the proof of the `I(theta)` bound disappears;
moreover, the stated hypothesis only canonicalizes ordinary `P'(a,u)`
clusters and is vacuous in this case.  This is a proof gap, not a
counterexample to the underlying barrier.  If the special endpoint cells
are canonical, the endpoint follows separately from the already-proved
decomposable-class lower bound, as explained below.

There are also two smaller corrections:

1. the arbitrary-microconfiguration transversal bound remains at least
   `1/2` through
   `theta_*=0.216161444245677...`, the root of `T(theta)=1/2`, not merely
   through `0.21`; and
2. the layerwise score formula is true, but its current one-sentence
   justification should be replaced by the short induction below, since
   Baek--Balko's published aggregate `v_j` formula alone does not imply the
   required refinement.

Subject to the endpoint correction and that proof expansion, I accept the
canonical barrier.

## 1. Reconstruction of the layer and score labels

Put `d=m-3`.  The left half `P'` in Definition 17 has blocks

\[
 C_{\ell_{h+2}}=P(m-h-1,h+2)=T_{d,h},\qquad 0\le h\le d,
\]

and therefore block size `binom(d,h)`.  Label the points in `T_{d,h}` by
the `h`-subsets `A` of `[d]` in the usual Pascal recursion.  The claimed
score is

\[
 s(A)=1\quad(A=\varnothing),\qquad
 s(A)=1+\max A\quad(A\ne\varnothing).                 \tag{A}
\]

Here is a direct induction.  Within `T_{d,h}`, the longest right-hull chain
ending at `A` has length

\[
 r(A)=\max A-h+1.                                     \tag{B}
\]

In the Pascal split, a label beginning with `1` stays in the left child and
inherits (B), while a label beginning with `0` lies in the right child and
may prepend exactly one point from the left child.  This proves (B)
inductively.  The same induction shows that a convex subset contained in
`T_{d,h}` and ending at a nonempty label `A` has size at most `max A`: if
the endpoint is in the left child, use induction there; if it is in the
right child, either stay there or combine a cap of size at most `h` from
the left child with a right-child chain of size `max A-h`.

Now consider the full row.  A convex set ending at `A` and meeting an
earlier block has a cap in its first occupied block, at most one point in
each intermediate block, and a right-hull chain ending at `A` in block
`h`.  A cap in block `a` has size at most `a+1`, so its total size is at
most

\[
 (a+1)+(h-a-1)+r(A)=h+r(A)=1+\max A.
\]

The one-block case is already at most `max A`.  Equality in the full row is
obtained by starting with the singleton block zero, taking one
point from every intermediate block, and taking a chain of length `r(A)`
in the last block.  This proves (A).  Consequently the multiplicity of
score `t+1` in layer `h>=1` is exactly

\[
 \#\{A:|A|=h,\max A=t\}=\binom{t-1}{h-1},
\]

and summing over `h` gives `2^(t-1)` in each half, hence Baek--Balko's
aggregate `v_{t+1}=2^t`.

As an independent finite check, I built the exact rational strongly glued
rows of depths `d=1,2,3,4`, exhaustively computed the largest convex subset
ending at every point, and obtained `1+max(A)` for all `2+4+8+16=30`
labels.

## 2. Transversal geometry and exact weights

The centers `ell_2,...,ell_{m-1}` are the block centers of the affine copy
of `P(m-1,m-1,m-1)` and form a convex chain.  A transversal through these
internal blocks is therefore convex.  Replacing each selected macro point
by an arbitrary point of its output cluster preserves every orientation of
triples in distinct output clusters.  Hence every choice counted by
`prod_h Z_h` is indeed convex and different choices give different
subsets.  No property of the output micro order types is used.

For `h>=1`, (A) and the ordinary-cluster size in Definition 13 give

\[
 Z_h=\sum_{t=h}^d\binom{t-1}{h-1}\binom{k-t-2}{x}.
\]

The unique score-one point in the left half is the global left endpoint, so
its special-cluster mass is

\[
 Z_0=\sum_{j=0}^x\binom{k-2}{j}.
\]

I independently checked `sum_h Z_h=2^(k-3)` and the program's product for
every admissible pair `(k,x)` with `5<=k<=50`.  Formula (1), while not
needed for this lower bound, is also the standard exact endpoint
classification for an almost-vertical blow-up: the support is convex, only
the first and last occupied clusters can be multiple, and their
intersections are the appropriate left and right chains.

## 3. Entropy and Riemann limit

With `h/k->eta`, `t/k->tau`, and `mu=1-2theta`, the logarithm of a summand
has rate

\[
 \tau H_2(\eta/\tau)+(1-\tau)H_2(\theta/(1-\tau)).
\]

The unrestricted Vandermonde maximizer is
`tau=eta/(eta+theta)`.  It obeys `tau<=mu` exactly when
`eta<=mu/2`; otherwise concavity puts the maximum at `tau=mu`.  Thus

\[
 z_\theta(\eta)=
 \begin{cases}
 H_2(\eta+\theta),&0\le\eta\le\mu/2,\\
 \mu H_2(\eta/\mu)+2\theta,&\mu/2\le\eta\le\mu.
 \end{cases}
\]

Integrating gives exactly

\[
 T(\theta)=\int_\theta^{1/2}H_2(s)\,ds
 +\frac{(1-2\theta)^2}{4\ln2}+\theta(1-2\theta).
\]

Uniform binomial-entropy errors cost `O(k log k)` after summing over all
layers, so the triangular limit `x/k->theta` is valid, including
`theta=0`.  Direct midpoint integration of the piecewise function agreed
with the closed form to less than `1.5e-10` at
`theta=0,0.1,0.21,0.3,0.49`.

The score-two cluster is

\[
 P(k-x-1,x+2)=T_{k-3,x}.
\]

The exact Pascal recurrence and its cap--cup cross term give

\[
 \log_2 W(T_{k-3,x})=
 \left(H_2(\theta)-\frac{\theta(1-\theta)}{\ln2}+o(1)\right)k^2,
\]

so the stated `I(theta)` is correct.  I compared the companion recurrence
against the independent cell recurrence through depth 14, for every cell,
with exact integer agreement.

## 4. Coverage and required statement changes

Both monotonicity claims are correct: `T` decreases and `I` increases on
`[0,1/2]`.  Numerically,

\[
 T(0.21)=0.5087955456059\ldots,\qquad
 I(0.21)=0.5021396326478\ldots,
\]

so splitting at `0.21` proves the advertised conservative canonical margin.
The actual crossing is

\[
 \theta=0.212673864150624\ldots,qquad
 T(\theta)=I(\theta)=0.5049925589471\ldots.
\]

For an entirely rigorous paper statement, the strict decimal comparison
should either be weakened to a conservative rational decimal and accompanied
by elementary interval bounds for the logarithms, or computed with directed
interval arithmetic; ordinary binary floating point is a check, not a
certificate.

The theorem should be replaced by one of the following safe versions:

* `x/k -> theta in [0,1/2)`, with the current assumption on ordinary
  clusters; or
* `x/k -> theta in [0,1/2]` **and** `k-2x>=4` eventually; or
* `x/k -> theta in [0,1/2]`, with **all** ordinary and special endpoint
  `P'` configurations instantiated canonically.

For completeness, the last alternative really does cover `m=3`.  Then `M`
has just two points and the output consists of the two special clusters
`P(k,x+2,k)` and `P(x+2,k,k)`, each of size `2^(k-3)`.  The canonical
`P(a,u,k)` is decomposable: Section 4 builds it from the decomposable cells
`P(k+1-j,j+1)` in successive deep-below layers.  Rotation does not change
its convex-subset count.  Reflecting it gives a mirror-decomposable set, so
the strong-class theorem applied to either output cluster gives

\[
 \log W\ge\tfrac12(k-3)^2-O(k^{3/2}).
\]

Since the whole construction has `N=2^(k-2)` points, this has normalized
liminf `1/2`.  Notice that this endpoint repair uses only the count inside
one cluster; it does not claim that the heterogeneous two-cluster union is
itself mirror-decomposable.

Finally, in the arbitrary-microconfiguration summary,
replace `theta<=0.21` by `theta<=theta_*`, where

\[
 \theta_*=0.216161444245677\ldots,\qquad T(\theta_*)=1/2,
\]

and replace “equivalent to” by “requires either a weighted macro-support
count or new lower bounds for arbitrary extremal microconfigurations.”
