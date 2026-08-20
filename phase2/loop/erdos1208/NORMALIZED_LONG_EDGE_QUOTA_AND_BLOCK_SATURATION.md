# Normalized long-edge quota, matching-block saturation, and a sharp lift

## 1. Outcome

Let `A subset Z^2` be a `k`-point Euclidean distance-Sidon set of
coordinate height `m`.  Let `H_A` be the clean six-endpoint zero-sum
directed-edge hypergraph.  For a hyperedge `h`, put

\[
 t(h)=\gcd(c(u_1),c(u_2),c(u_3)),\qquad
 \lambda_{\min}(h)={\min_i|u_i|^2\over t(h)^2}.       \tag{1.1}
\]

Define the adaptive quota

\[
 \mathcal B=k^3+m^2,qquad
 Q=\left\lceil{\mathcal B\over k^2}\right\rceil.     \tag{1.2}
\]

This note proves two new endpoint-retaining deletions.

### Theorem A (normalized short-edge quota)

\[
 \boxed{
 |\{h\in\mathcal H_A:\lambda_{\min}(h)\le Q\}|
 \le m^{o(1)}\mathcal B.}                            \tag{1.3}
\]

### Theorem B (sparse common-scale quota)

Let `n_t` be the number of unordered endpoint edges whose displacement
content is divisible by `t`.  Then

\[
 \boxed{
 \sum_{t:n_t\le Q}|\{h:t(h)=t\}|
 \le m^{o(1)}\mathcal B.}                            \tag{1.4}
\]

The key gain is not a pointwise estimate: it comes from summing exact
content layers against the divisor budget of every realized endpoint edge.

There is also an exact switching consequence.  A pair of disjoint
three-subsets having the same centroid produces one **matching block** of
12 directed hyperedges.  Saturating any already-paid hyperedge family by
whole matching blocks costs a factor of at most 12.  Hence, after combining
(1.3)--(1.4) with the prior collinear, high-common-scale, and low-Gaussian-
product theorems, every surviving block has all of the following properties
for every one of its 12 matchings:

\[
 \begin{gathered}
 \det(u_1,u_2)\ne0,\qquad
 t<T=\left({m^4\over k^3+m^2}\right)^{1/3},\\
 |a x|>m^{4/3},\qquad
 \lambda_{\min}>Q,\qquad n_t>Q.                    \tag{1.5}
 \end{gathered}
\]

Moreover **all nine** cross-endpoint edges between the two triples have
raw squared length greater than `Q`.  Since

\[
 Q\gg m^{2/3},                                      \tag{1.6}
\]

all three normalized edge lengths in every surviving matching are
`Omega(m^(1/3))`.

This strictly narrows the gate, but does not close it.  The explicit lifted
modular parabola has `Omega(m^2)` hyperedges deep inside (1.5): very small
common scale, normalized lengths polynomially beyond `Q`, and Gaussian
product polynomially beyond `m^(4/3)`.  Thus no further cutoff decay in
`t`, edge length, determinant, or `|ax|` can prove the theorem.  The
remaining estimate must make the flat `m^2` payment by globally packing
the endpoint blocks.

## 2. Divisor bookkeeping for endpoint edges

For an unordered endpoint edge `e={a,b}`, write

\[
 u_e=b-a,qquad c(e)=\gcd(|(u_e)_1|,|(u_e)_2|),
 \qquad L(e)=|u_e|^2.                               \tag{2.1}
\]

Let

\[
 E_t=\{e:t\mid c(e)\},\qquad n_t=|E_t|.             \tag{2.2}
\]

There are `N=binom(k,2)` unordered edges.  Since every edge contributes to
`E_t` once for each divisor of its content,

\[
 \boxed{
 \sum_{t\ge1}n_t
 =\sum_{e\in\binom A2}\tau(c(e))
 \le N\max_{d\le m}\tau(d)
 =m^{o(1)}k^2.}                                     \tag{2.3}
\]

This is where retaining the exact common content matters.  Treating all
low values of `t` independently would lose a polynomial factor.

## 3. Proof of the normalized short-edge theorem

For fixed `t`, put

\[
 S_t(Q)=\{e\in E_t:L(e)/t^2\le Q\},
 \qquad s_t=|S_t(Q)|.                               \tag{3.1}
\]

The values `L(e)` are distinct positive integers by distance-Sidonicity.
For `e in E_t`, `t^2` divides `L(e)`.  Therefore the normalized labels
`L(e)/t^2` are distinct positive integers and

\[
 \boxed{s_t\le Q.}                                  \tag{3.2}
\]

Every hyperedge with exact scale `t` and `lambda_min<=Q` contains a
directed orientation of one edge in `S_t(Q)` and two directed orientations
of edges in `E_t`.  The endpoint hypergraph is linear: two directed edges
belong to at most one hyperedge.  Consequently

\[
 |\{h:t(h)=t,\lambda_{\min}(h)\le Q\}|
 \le 4s_tn_t\le4Qn_t.                               \tag{3.3}
\]

Summing (3.3), then using (2.3), proves

\[
 |\{h:\lambda_{\min}(h)\le Q\}|
 \le4QNk^{o(1)}
 \le m^{o(1)}(k^3+m^2).                             \tag{3.4}
\]

No determinant or Gaussian-cell multiplicity is discarded in this count.

## 4. Proof of the sparse-scale theorem

There are `2n_t` directed hypergraph vertices over `E_t`.  By linearity,
three distinct vertex-pairs are consumed by every hyperedge, whence

\[
 |\{h:t(h)=t\}|
 \le {1\over3}{2n_t\choose2}<2n_t^2.                \tag{4.1}
\]

For `n_t<=Q`, (4.1) is at most `2Qn_t`.  Sum over such `t` and use (2.3)
to obtain (1.4).

Thus the live scales are not merely below `T`; they must also satisfy

\[
 n_t>Q.                                               \tag{4.2}
\]

The elementary metric bound `n_t<=2m^2/t^2` gives the additional necessary
condition

\[
 t<{\sqrt2m\over\sqrt Q}.                            \tag{4.3}
\]

This improves `t<T` in the height-dominated range, although it is not by
itself enough at critical height.

## 5. Saturating by all endpoint matchings

Let `S,T` be disjoint three-subsets of `A` with

\[
 \sum_{s\in S}s=\sum_{t\in T}t.                     \tag{5.1}
\]

Every bijection from `S` to `T` gives a zero-sum matching of three directed
edges; reversing every edge gives the opposite orientation.  Thus the
unordered pair `{S,T}` gives exactly 12 hyperedges.  Conversely, the source
and target endpoints of a clean hyperedge recover `{S,T}`.  The hypergraph
therefore partitions into 12-element matching blocks.

For any family `P subset H_A`, let `Sat(P)` be the union of the blocks
meeting `P`.  Since each member of `P` lies in exactly one block,

\[
 \boxed{|\operatorname{Sat}(P)|\le12|P|.}            \tag{5.2}
\]

All previously paid branches may consequently be saturated without losing
an exponent.  In a block outside the saturation of (1.3), take any one of
the nine cross-endpoint edges `e` between `S` and `T`.  Some matching uses
`e`.  If `L(e)<=Q`, then for that matching

\[
 {L(e)\over t(h)^2}\le L(e)\le Q,                   \tag{5.3}
\]

contradicting nonsaturation.  This proves the nine-edge separation claim.

Finally, writing `k=m^(2/3)y`,

\[
 {k^3+m^2\over k^2}
 =m^{2/3}(y+y^{-2})\gg m^{2/3},                     \tag{5.4}
\]

which proves (1.6).

## 6. A sharp all-long, low-content equality model

Let `p` run through odd primes, put `y_x=[x^2]_p` in `{0,...,p-1}`, and
take

\[
 A_p=\{(x+py_x,y_x):0\le x<p\}.                     \tag{6.1}
\]

As proved in `LARGE_GAUSSIAN_CELL_SUPPORT_TAIL_AUDIT.md`, `A_p` is
Euclidean distance-Sidon and has height `m=Theta(p^2)`.  The interval proof
is exact: an edge with label difference `h` and vertical difference `z`
has squared length

\[
 (h+pz)^2+z^2,                                      \tag{6.2}
\]

and these values are distinct; reduction modulo `p` then recovers the two
parabola endpoints.

There are `Omega(p^4)` clean zero-sum hyperedges.  Indeed the
`binom(p,3)` triple sums occupy `O(p^2)` integer cells, so Cauchy gives
`Omega(p^4)` ordered collisions.  Additive Sidonicity makes two distinct
triples in one cell disjoint.

The following stronger statement places that mass deep in the new core.

### Theorem C (sharp deep-core lift)

For all sufficiently large odd primes, `Omega(p^4)` clean noncollinear
hyperedges of `A_p` satisfy

\[
 \boxed{
 t\le p^{1/20},\qquad
 \lambda_{\min}\gg p^{21/10}>Q,\qquad
 |ax|\gg p^{29/10}>m^{4/3},\qquad t<T.}             \tag{6.3}
\]

### Proof

Write each of the three edge vectors before/after the shear as

\[
 (h_i,z_i),\qquad u_i=(h_i+pz_i,z_i),                \tag{6.4}
\]

so `sum h_i=sum z_i=0`, `|h_i|,|z_i|<p`, and

\[
 t\mid\gcd(h_i,z_i),\qquad
 D=|\det(u_1,u_2)|=|h_1z_2-z_1h_2|.                 \tag{6.5}
\]

Discard records in the following three families.

1. Some `|z_i|<p^(1/10)`.  For fixed signed `z` and nonzero `h`, the
   congruence `z=h(x+x') mod p`, together with `h=x-x'`, determines the
   directed endpoint pair.  There are `O(p^(11/10))` such edges, and each
   has hypergraph degree `O(p^2)`.  This discards `O(p^(31/10))` records.
2. `D=0` or `0<D<=p^(9/10)`.  The collinear direction count applied before
   the shear gives `O(p^2 log p)`: the modular parabola is already integer
   vector-Sidon, which is the only uniqueness input that collinear count
   needs.  The low-determinant lattice-coset
   theorem gives at worst `O(p^(39/10))` for the positive range.  This is
   `o(p^4)`.
3. `t>p^(1/20)`.  If `d` divides an edge content then `d|h`, so the number
   of directed eligible edges is `O(p^2/d)`.  Two determine the third.
   Hence this tail has size

   \[
    O\left(\sum_{d>p^{1/20}}{p^4\over d^2}\right)
    =O(p^{79/20})=o(p^4).                            \tag{6.6}
   \]

There remain `Omega(p^4)` records.  Their three nonzero `z_i` sum to zero.
The vector with the lone sign has `|z|` equal to the sum of the other two;
because every `|z_i|>=p^(1/10)`, the leading `p^2z_i^2` term in (6.2)
shows that this is the longest vector.  The two shortest vectors therefore
have same-sign vertical differences.  Their dot product obeys

\[
 u_i\mathbin\cdot u_j
 \ge p^2|z_i z_j|-p^2(|z_i|+|z_j|+1)
 \gg p^{11/5}.                                      \tag{6.7}
\]

Also every edge has squared norm `gg p^(11/5)`.  Divide (6.7), the norm,
and `D>p^(9/10)` by the appropriate powers of `t<=p^(1/20)`:

\[
 \lambda_{\min}\gg p^{11/5-1/10}=p^{21/10},
 \qquad
 |ax|={D|u_i\cdot u_j|\over t^4}
 \gg p^{9/10+11/5-1/5}=p^{29/10}.                  \tag{6.8}
\]

Since `Q=Theta(p^2)`, `m^(4/3)=Theta(p^(8/3))`, and
`T=Theta(p^(4/3))`, (6.8) proves (6.3).

The exponents are deliberately nonoptimized.  Their purpose is to show a
fixed polynomial margin inside every surviving cutoff.

## 7. Exact status

The new theorem closes two natural failure modes:

* one short normalized edge hidden beside a very long edge;
* many individually small common-content layers.

Block saturation upgrades this to a nine-cross-edge separation statement.
Theorem C shows the remaining all-long/dense-scale system is real and
sharp at the allowed ambient term.  The exact unresolved statement is now:

> Globally pack matching blocks for which all nine cross edges are long and
> every matching lies in a dense low-content Gaussian cell, paying their
> total mass by `m^(o(1))(k^3+m^2)` without any cutoff decay.

That is strictly narrower than the product gate, but still exponent-
equivalent to the hard ambient endpoint theorem on the equality model.

## 8. Verification

Run

    python3 phase2/loop/erdos1208/verify_normalized_long_edge_quota_and_block_saturation.py

The verifier checks exact divisor incidence, both quota inequalities,
12-record block decomposition and saturation, nine-edge separation, all
normalized Gaussian identities, and the deep-core profiles for `p=23,43`.
