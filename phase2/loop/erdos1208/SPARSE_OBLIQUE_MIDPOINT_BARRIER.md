# Sparse stability of the oblique modular-midpoint theorem

## 1. Audit of the complete-patch theorem

The proof of Theorem 7.1 in `OBLIQUE_LATTICE_GAUSSIAN_CORE.md` is sound.
Here are the points at which a hidden divisibility or boundary loss could
have occurred.

* The diameter estimate really gives
  `B<=2 sqrt(2) M/(r-1)<=6M/r`.
* Under `M<r^(3/2)/100`, it gives
  `0<|det L|<=B^2<0.0036r`.  Thus every prime
  `r/100<q<r/40` is automatically coprime to `det L`, and `L^TL` is
  invertible modulo `q`.
* A central interval of length `r/3` contains many representatives of the
  unique midpoint residue modulo `q`.  At most one has physical midpoint
  zero.
* For every remaining representative, `a=L^T(t+Lm)` is a nonzero vector in
  `q Z^2`, so `n=J(a/q)` is a nonzero integral direction.  The displayed
  constants give `||n||_infinity<0.085r`, which leaves both endpoints in the
  coefficient box.
* The two endpoints are distinct because `L` is nonsingular and are
  non-antipodal because their physical midpoint is nonzero.

For a completely explicit invocation of Bertrand's postulate, apply it to
`floor(r/80)`: for sufficiently large `r` the resulting prime lies between
`r/100` and `r/40`.  This only expands a detail already valid in the proof.

The natural next question is whether density can replace completeness.  The
answer is essentially no.  There is a weak near-complete stability statement,
but a matching construction shows that its codimension-one scale is sharp.

## 2. What modular averaging actually proves

Let `V={0,...,r-1}^2`, and join `x,y in V` when the two physical points
`t+Lx,t+Ly` are distinct, non-antipodal, and have the same norm.

### Proposition 2.1 (codimension-one stability)

There is an absolute constant `c>0` such that, if

\[
 M<r^{3/2}/100,\qquad \mathcal P=t+LV\subset[-M,M]^2,
\]

then the collision graph contains a matching of size at least

\[
 \frac{c r}{\log r\,T(M)},\qquad
 T(M):=4\max_{1\le m\le 2M^2}\tau(m).           \tag{2.1}
\]

Consequently every radially unique subset `Q subset V` satisfies

\[
 |V\setminus Q|\ge {c r\over\log r\,T(M)}.
                                                               \tag{2.2}
\]

In the polynomial-height regime, the standard maximal-order divisor bound
gives `T(M)=r^(o(1))`, so (2.2) is `r^(1-o(1))`.

### Proof

Run the proof of Theorem 7.1 separately for every prime
`r/100<q<r/40`.  It produces at least one collision edge for every such
prime.  Edges obtained from distinct primes are distinct: an edge determines
its integral coefficient midpoint `m` and its direction `n` up to sign,
while

\[
 n=J\left({L^T(t+Lm)\over q}\right)             \tag{2.3}
\]

determines the positive prime `q` because the numerator is nonzero.  The
prime number theorem (a fixed-interval Chebyshev estimate is enough) therefore
gives `Omega(r/log r)` distinct edges.

A physical lattice point of squared norm `k` has at most
`r_2(k)<=4 tau(k)` integral equal-norm partners.  Hence the maximum degree of
the collision graph is at most `T(M)`.  Greedy matching gives (2.1), and an
independent set must omit one endpoint from every matching edge.  This proves
(2.2).  QED.

This is far weaker than a fixed-density theorem: it only detects subsets
missing fewer than `r^(1-o(1))` of the `r^2` coefficient points.

## 3. A near-complete counterexample below every critical constant

The weakness in Proposition 2.1 is real, not an artefact of the proof.

### Proposition 3.1

Fix an integer `T>=2`.  For every integer `B>=2`, put `r=TB^2` and define

\[
 P_{B,T}=\{(B(a+b)+b,a+b):0\le a,b<r\}.          \tag{3.1}
\]

There is a subset `Q_{B,T}` of its coefficient box such that all physical
points indexed by `Q_{B,T}` have different squared norms and

\[
 |Q_{B,T}|\ge r^2-T^2r.                          \tag{3.2}
\]

Moreover `P_{B,T}` lies in `[0,M]^2`, where

\[
 M=(2B+1)(r-1),\qquad
 {M\over r^{3/2}}\le {2+1/B\over\sqrt T}.       \tag{3.3}
\]

Thus, for every `epsilon>0` and every `c>0`, there are arbitrarily large
oblique patches of height `M<c r^(3/2)` having a radially unique subset of
density at least `1-epsilon`.

### Proof

Write

\[
 s=a+b,\qquad x=Bs+b.
\]

Count unordered pairs of distinct coefficient points with equal norm.
If their `s` coordinates agree, equality of norms forces their `x`
coordinates, and hence both coefficient points, to agree.  Otherwise orient
the pair so that

\[
 k=s'-s>0,\qquad h=x-x'>0.                       \tag{3.4}
\]

The coefficient difference and the factorization of equal squares give

\[
 b-b'=h+Bk,\qquad h(x+x')=k(s+s').              \tag{3.5}
\]

Put `j=k-Bh`.  Since

\[
 x+x'=B(s+s')+(b+b'),
\]

equation (3.5) becomes

\[
 h(b+b')=j(s+s').                               \tag{3.6}
\]

We have `1<=j<=h-1`.  Indeed, `j=0` would force `b=b'=0`, contradicting
the first equation in (3.5).  Since `b+b'<=s+s'`, (3.6) gives `j<=h`;
equality would force `a=a'=0`, and then `b-b'=s-s'=-k`, again a
contradiction.

Also

\[
 r-1\ge b-b'=h(B^2+1)+Bj,                       \tag{3.7}
\]

so `h<T`.  There are fewer than `T^2/2` possible pairs `(h,j)`.  Once
`(h,j)` and `s` are fixed, equations (3.4)--(3.6) determine `k,b,b'`
uniquely.  There are fewer than `2r` choices for `s`.  Hence the total number
of equal-norm pairs is less than `T^2r`.

Choose one coefficient point for each represented squared norm.  The number
deleted is at most the number of equal-norm pairs, which proves (3.2).
The coordinate maximum in (3.1) is `(2B+1)(r-1)`, giving (3.3).  Finally
choose fixed `T>(3/c)^2` and let `B` tend to infinity; then (3.2) has density
tending to one while (3.3) is smaller than `c`.  QED.

The same family rules out even a power-saving dense extension.  Given
`0<eta<1/4`, take

\[
 T=B^{\theta+o(1)},\qquad
 \theta={4\eta\over1-2\eta}<2.                  \tag{3.8}
\]

Then `r=B^(2+theta+o(1))`, while

\[
 M=r^{3/2-\eta+o(1)},\qquad
 {T^2r\over r^2}={T\over B^2}=o(1).             \tag{3.9}
\]

Thus density `1-o(1)` does not force height `r^(3/2-o(1))`: it is compatible
with every exponent strictly above `5/4`.  At the endpoint, taking
`T=lambda B^2` with fixed `0<lambda<1` gives a radially unique subset of
density at least `1-lambda` and height `O_lambda(r^(5/4))`.  These conclusions
use only the proved pair-count bound; the finite examples are substantially
sparser in collisions than that worst-case estimate.

## 4. Consequence for the seven-incidence route

The counterexample is already an **exact injective linear/Freiman image** of
a subset of a two-dimensional box.  It therefore rules out every proposed
lemma of the following form, even if “dense” means density `1-o(1)`:

> A dense radially unique subset of a subcritical exact or approximate
> rank-two lattice patch must contain a modular-midpoint collision.

For a fixed modulus, the modular-midpoint edges form a matching.  Averaging
over all critical-size primes produces only `r^(1+o(1))` useful edges on
`r^2` vertices.  This is why Varnavides averaging, dependent random choice,
and common-neighbour arguments cannot upgrade Proposition 2.1 to fixed
density: the relevant graph has vanishing average degree, and Proposition
3.1 supplies an explicit near-complete independent set.

Therefore a sparse/approximate extension usable for Erdős 1208 must retain
structure absent from an arbitrary dense lattice subset.  In the current
notation the indispensable candidates are

\[
 u+Q,\quad w-Q,\quad w-(I+J)Q\subset D,          \tag{4.1}
\]

the popularity of both `q` and `Jq`, the unique endpoint decoration of the
complete difference set, and aggregation over the off-diagonal shift `r`.
Merely applying BSG/Freiman modelling and then recording the model density
cannot close the gate.

`verify_sparse_oblique_midpoint_barrier.py` enumerates (3.1), checks the
collision parametrization (3.4)--(3.7), verifies the `T^2r` bound, and
constructs the one-point-per-radius transversal.
