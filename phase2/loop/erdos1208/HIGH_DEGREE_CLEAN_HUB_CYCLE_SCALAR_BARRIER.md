# High-degree clean hubs: exact algebra and a cycle/scalar barrier

## 1. Verdict

The high-source-degree branch has a sharp exact description, but it does
not by itself force a repeated distance.  If a clean `q`-fibre contains a
source star of degree `r`, then its target edges form a matching, so

\[
 r\le {k-3\over2}.
\]

The four cross distances between any two target edges give three exact
Walsh coefficients (three dot products).  Nevertheless, the upper bound
is asymptotically attainable in genuine integral distance-Sidon sets, even
under all of the following simultaneous strengthenings:

* the same clean fibre has quadratic size `h_q=Omega(k^2)`;
* every hub leaf occurs in another target edge, and the resulting overlap
  digraph is one directed cycle;
* all `2r` controlled source and target edge vectors have pairwise nonzero
  determinants; and
* the same fibre carries a linear-sized fibre of the positive scalar
  charge `delta(s)+18delta(t)`.

Thus a high-degree/matching dichotomy does not close the scalar gate.  A
successful high-degree inverse must couple the scalar repetitions to the
hub spokes (or to their cross-distance Walsh spectrum).  Merely having a
large hub and a heavy scalar bucket in the same `q`-fibre is insufficient.

## 2. Exact star-to-matching lemma

Let `A` be distance-Sidon, fix distinct anchors `alpha,beta`, and put

\[
 q=\alpha-\beta.
\]

A clean start is a pair sum `s=c+d` for which

\[
 c+d+q=e+f,                                                \tag{2.1}
\]

and `alpha,beta,c,d,e,f` are six distinct points of `A`.  Fix `c` and
suppose that the source edges

\[
 S_i=\{c,d_i\},\qquad 1\le i\le r,                         \tag{2.2}
\]

are clean `q`-starts.  Write the corresponding target edge as
`T_i={e_i,f_i}`.

### Lemma 2.1 (target matching)

The edges `T_1,...,T_r` are pairwise vertex-disjoint.  In particular,
all their vertices lie in `A\{alpha,beta,c}`, and

\[
 2r\le k-3.                                                \tag{2.3}
\]

### Proof

Suppose `T_i` and `T_j` share `e`.  Relabel so that
`T_i={e,f_i}` and `T_j={e,f_j}`.  Subtracting their instances of
(2.1) gives

\[
 f_i-f_j=d_i-d_j.                                         \tag{2.4}
\]

Hence the two edges `{f_i,f_j}` and `{d_i,d_j}` have the same squared
distance.  Distance-Sidonicity says that they must be the same unordered
edge.  The identification `f_i=d_i,f_j=d_j` contradicts cleanliness in
row `i`; the swapped identification, combined with (2.4), gives
`2(d_i-d_j)=0`, also impossible.  This proves disjointness.  Cleanliness
excludes the three points `alpha,beta,c` from every target edge, yielding
(2.3).  QED.

There is also an exact endpoint-overlap count.  Let

\[
 D=\{d_1,\ldots,d_r\},\qquad U=\bigcup_iT_i.
\]

Both are contained in a set of size `k-3`, while `|D|=r` and `|U|=2r`.
Consequently

\[
 |D\cap U|\ge 3r-(k-3).                                   \tag{2.5}
\]

Draw an arc `i -> j` when `d_j in T_i`.  It has no loop, indegree at
most one, and outdegree at most two.  Near the extremal value in (2.3),
(2.5) forces many leaf-target incidences, but, as Section 4 shows, even a
single cycle through every leaf is harmless.

## 3. The four-cross-distance Walsh algebra

Orient `T_i` and put

\[
 w_i=e_i-f_i,\qquad \Delta=d_i-d_j.
\]

The target midpoints differ by `Delta/2`.  Therefore the four squared
cross distances between `T_i` and `T_j` are

\[
 L_{\sigma\tau}
 ={1\over4}\lVert\Delta+\sigma w_i+\tau w_j\rVert^2,
 \qquad \sigma,\tau\in\{-1,1\}.                           \tag{3.1}
\]

Their Walsh transform is

\[
\begin{aligned}
 \sum_{\sigma,\tau}L_{\sigma\tau}
   &=\lVert\Delta\rVert^2+\lVert w_i\rVert^2+\lVert w_j\rVert^2,\\
 \sum_{\sigma,\tau}\sigma L_{\sigma\tau}
   &=2\Delta\mathbin\cdot w_i,\\
 \sum_{\sigma,\tau}\tau L_{\sigma\tau}
   &=2\Delta\mathbin\cdot w_j,\\
 \sum_{\sigma,\tau}\sigma\tau L_{\sigma\tau}
   &=2w_i\mathbin\cdot w_j.                              \tag{3.2}
\end{aligned}
\]

The four underlying cross edges are distinct, so all four `L` values are
distinct.  Comparing the six pairs gives the six necessary conditions

\[
\begin{aligned}
 w_i\mathbin\cdot(\Delta+w_j)&\ne0,&
 w_i\mathbin\cdot(\Delta-w_j)&\ne0,\\
 w_j\mathbin\cdot(\Delta+w_i)&\ne0,&
 w_j\mathbin\cdot(\Delta-w_i)&\ne0,\\
 \Delta\mathbin\cdot(w_i+w_j)&\ne0,&
 \Delta\mathbin\cdot(w_i-w_j)&\ne0.                     \tag{3.3}
\end{aligned}
\]

These are real restrictions, but they are inequalities rather than an
equal-distance identity.  Generic cycle hubs satisfy all of them.

## 4. A universal cycle hub

Start with any finite vector-Sidon set `B` containing anchors
`alpha,beta`, and let `q=alpha-beta != 0`.  Introduce free vectors

\[
 C,D_0,\ldots,D_{r-1}
\]

and, with indices read cyclically, define

\[
 X_i=C+q+D_i-D_{i+1}.                                     \tag{4.1}
\]

Adjoin the points `C,D_i,X_i` to `B`.  Then

\[
 \alpha+C+D_i=\beta+D_{i+1}+X_i.                          \tag{4.2}
\]

Thus the source star has spokes `{C,D_i}` and targets

\[
 T_i=\{D_{i+1},X_i\}.                                     \tag{4.3}
\]

The targets are a perfect matching on their `2r` points, and every leaf
`D_j` occurs in exactly `T_{j-1}`.  The overlap digraph is the full
directed cycle.  Telescoping (4.1) only gives

\[
 \sum_iX_i=r(C+q),                                        \tag{4.4}
\]

which has no metric consequence.

### Lemma 4.1 (formal Sidonicity of the cycle gadget)

For `r>=3`, all unordered pair sums among

\[
 B\cup\{C,D_i,X_i:0\le i<r\}                             \tag{4.5}
\]

are distinct as affine forms in the free variables, provided the pair
sums in `B` are distinct.

### Proof

Let `e_i` denote the coefficient vector of `D_i` and put
`b_i=e_i-e_{i+1}`.  First separate pair sums by their coefficient of `C`.

For coefficient zero, the possible `D`-patterns are `0`, `e_i`, and
`e_i+e_j`; these respectively come from `B+B`, `B+D_i`, and
`D_i+D_j`, and are plainly injective.

For coefficient one, the patterns are

\[
 0,\quad b_i,\quad e_j,\quad e_j+b_i,                     \tag{4.6}
\]

coming from `B+C`, `B+X_i`, `C+D_j`, and `D_j+X_i`.
The map `(i,j) -> e_j+e_i-e_{i+1}` is injective: unless `j=i+1`, its
unique negative coordinate recovers `i`, after which the positive
coordinates recover `j`; in the exceptional case its value is `e_i`.
The sole overlap between types in (4.6) is precisely

\[
 e_{i+1}+b_i=e_i.
\]

But the corresponding affine sums are
`D_{i+1}+X_i=C+q+D_i` and `C+D_i`, and differ by the nonzero constant
`q`.

For coefficient two, the patterns are `b_i` and `b_i+b_j`, from
`C+X_i` and `X_i+X_j`.  The boundary map on a directed cycle has kernel
spanned by the all-ones edge vector.  Two edge subsets of sizes one or
two can therefore have the same boundary only when they are the same
subset: their indicator-vector difference cannot be a nonzero multiple
of the all-ones vector.  This also separates the one-edge and two-edge
cases.  The fixed `B`-coefficients distinguish all remaining terms.
QED.

Pair-sum Sidonicity implies that two different formal edge vectors are
never equal up to sign.  Hence every unwanted equation

\[
 \lVert P_i-P_j\rVert^2=\lVert P_u-P_v\rVert^2             \tag{4.7}
\]

is a nonzero quadratic polynomial in the coordinates of `C,D_0,...,D_{r-1}`.
Likewise, the determinants between the controlled vectors

\[
 C-D_i,\qquad D_{i+1}-X_i=-C-q-D_i+2D_{i+1}               \tag{4.8}
\]

are nonzero polynomials for every two distinct vectors.  Finite avoidance
therefore specializes all free vectors to integer vectors so that the
whole set is distance-Sidon, every row (4.2) is clean, and all vectors in
(4.8) are pairwise nonparallel.

There are only `r^O(1)` forbidden polynomials, each of degree at most two.
The elementary grid nonvanishing lemma applies to their product and gives
coordinates of size `r^O(1)` (times the height of `B`).  Thus this is a
polynomial-height construction, not merely an abstract free-module model.

## 5. Making the same fibre quadratic

For completeness, here is a self-contained source of the required core.
For a prime `p`, take the integer lift

\[
 P_p=\{(x,x^2\bmod p):0\le x<p\}\subset[0,p)^2.           \tag{5.1}
\]

It is vector-Sidon: an equality of two ordered differences, reduced
modulo `p`, gives the same two roots from their sum and product.  Its
`p^3` ordered triple sums occupy at most `9p^2` integer bins, so their
energy is at least `p^4/9`.  Equal triples which share a point contribute
only `O(p^3)`, because cancellation leaves an equal pair sum.  Hence there
are `Omega(p^4)` pairs of disjoint equal-sum triples.  Here triples with a
repeated entry are harmless as well: there are only `O(p^2)` such ordered
triples, while pair-sum injectivity bounds every ordered triple-sum fibre
by `O(p)`, so collisions involving them contribute only `O(p^3)`.

Every such pair gives 18 oriented clean records: choose one distinguished
anchor in each triple and choose the direction between the two triples.
A clean record determines its two triples, by vector-Sidonicity, so there
is no uncontrolled multiplicity here.  There are only `O(p^2)` ordered
anchor differences.  Pigeonholing gives a nonzero `q` with

\[
 |H_q|=\Omega(p^2).                                        \tag{5.2}
\]

A generic nonsingular integer linear map preserves all pair/triple-sum
relations and separates all squared edge lengths.  The same polynomial
avoidance argument chooses this map with polynomial entries.  Multiplying
by two makes `q` even.  This yields a polynomial-height integral
distance-Sidon core with (5.2).

Adjoin the cycle gadget with `r=Cp`.  The old `Omega(p^2)` starts survive,
while only `2r+1=O_C(p)` points are added.  Consequently the combined set
still has

\[
 |H_q|=\Omega_C(k^2).                                      \tag{5.3}
\]

## 6. A heavy scalar bucket can coexist

The sum-of-two-squares planting argument supplies, for any prescribed
large `t`, distinct represented integers `(a_i,b_i)` satisfying

\[
 a_i+18b_i=N                                              \tag{6.1}
\]

for `1<=i<=t`, after the standard divisor-bound pruning of the finitely
many signed offset patterns.  With vectors of norms `a_i,b_i`, a common
scale `S`, free centers `P_i`, and the even `q`, put

\[
\begin{aligned}
 c_i&=P_i+Su_i,&d_i&=P_i-Su_i,\\
 e_i&=P_i+q/2+Sv_i,&f_i&=P_i+q/2-Sv_i.                    \tag{6.2}
\end{aligned}
\]

Then `c_i+d_i+q=e_i+f_i`, and the scalar record formed from this clean
start and its target edge has

\[
 \delta(c_id_i)+18\delta(e_if_i)=4S^2N.                   \tag{6.3}
\]

For the quantitative point, let `D_X` be the represented integers at most
`X`.  Landau--Ramanujan gives `|D_X|=X(log X)^{-1/2+o(1)}`.  Pigeonholing
`D_X^2` into the `19X+1` possible values of `a+18b` gives
`X^{1-o(1)}` pairs in one bucket.  They are matchings in both coordinates.
For a fixed signed vector sum, substitution into (6.1) gives a circle
equation with only `X^{o(1)}` integer solutions by the two-squares divisor
bound.  Greedy pruning of the fixed list of signed local patterns therefore
leaves `X^eta` rows for an absolute `eta>0`.  Taking
`X>=p^{1/eta}` supplies the asserted `t=p` rows at polynomial height.

The pruning makes every center-independent distance constraint
nondegenerate.  The free centers, jointly with the cycle variables, then
avoid all cross-gadget repeated distances and unintended pair sums at
polynomial height.

Take `t=p` and then choose `C=C(epsilon)` sufficiently large.  The final
point count is

\[
 k=(5+2C)p+O(1),\qquad r=Cp,                               \tag{6.4}
\]

so for every fixed `epsilon>0`, there are arbitrarily large examples with

\[
 r\ge(1/2-\epsilon)k,\qquad |H_q|\ge c_\epsilon k^2,       \tag{6.5}
\]

and a scalar-charge fibre of size at least `c'_epsilon k` in that same
`H_q`.

This last bucket is deliberately independent of the hub spokes.  It does
not refute the desired global scalar-energy estimate: its energy can be
far below the global allowance.  It does refute the proposed local
principle that a large clean hub plus scalar concentration somewhere in
the same fibre must itself force an equal distance.  The missing input is
a quantitative overlap theorem tying the repeated scalar records to the
hub's controlled edge set.

## 7. Exact finite certificate

Run

```text
PYTHONPATH=phase2/loop/erdos1208 \
python3 phase2/loop/erdos1208/verify_high_degree_clean_hub_cycle_scalar_barrier.py
```

The certificate uses a 61-point transformed parabola core, a 250-spoke
cycle hub, and six same-charge symmetric rows.  It checks exactly:

* 586 distinct integral points and all 171,405 squared distances distinct;
* all 171,405 unordered pair sums distinct;
* at least 592 distinct clean starts in one fibre (`592>586`);
* pairwise-disjoint target edges and one full 250-leaf overlap cycle;
* pairwise nonzero determinants among all 500 controlled hub edge vectors;
* the Walsh identities (3.2); and
* a scalar bucket of load six.

The maximum absolute coordinate in the deterministic certificate is
`910387737655324`.
