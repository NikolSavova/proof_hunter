# Internal-shift overlap in the unordered pair-sum set

## 1. Exact reduction

Let `A subset [0,m]^2` be distance-Sidon, `|A|=k`, and let

\[
 \Sigma=A\mathbin{\oplus}A
 =\{a+b:\{a,b\}\in\tbinom A2\}.                 \tag{1.1}
\]

Vector-Sidonicity makes the map from unordered pairs to `Sigma` injective,
so `|Sigma|=binom(k,2)`.  For a nonzero realized difference `q=a-b`, put

\[
 R_\Sigma(q)=|\Sigma\cap(\Sigma+q)|.             \tag{1.2}
\]

There are always exactly `k-2` trivial overlaps:

\[
 b+c+q=a+c,\qquad c\in A\setminus\{a,b\}.       \tag{1.3}
\]

Define the raw excess

\[
 \widetilde h(q)=R_\Sigma(q)-(k-2).              \tag{1.4}
\]

It is nonnegative.  Some arrows counted by `widetilde h(q)` can still use
`a` or `b`, and hence correspond to repeated-label third-energy terms.  Let
`h_6(q)` count only those overlap arrows whose two unordered pairs are
disjoint from one another and from `{a,b}`.  If `C_6(A)` is the ordered
six-distinct third-energy count from `AMBIENT_THIRD_ENERGY_CENTROID_GATE.md`,
then

\[
 \boxed{C_6(A)=4\sum_{q\in(A-A)\setminus\{0\}}h_6(q),
 \qquad 0\le h_6(q)\le\widetilde h(q).}          \tag{1.5}
\]

Thus the full cube-root conclusion would follow from the pointwise theorem

\[
 \boxed{
 \widetilde h(q)\le k^{o(1)}\left(1+{m^2\over k^2}\right)
 \quad(q\in(A-A)^*).}                            \tag{1.6}
\]

Indeed there are `k(k-1)` directed nonzero differences, so (1.5)--(1.6)
give

\[
 C_6(A)\le k^{o(1)}(k^2+m^2),                   \tag{1.7}
\]

which is stronger than the ambient centroid-matching gate.  Repeated-label
third-energy configurations cost only `O(k^3)`, and origin localization then
gives `k<=m^(2/3+o(1))`.

Estimate (1.6) is unproved.  It is, however, a smaller and more concrete
local theorem than the joint Fourier tail: it concerns one internal
translation of the uniquely represented pair-midpoint set.

## 2. Proof of the exact identity

Fix `q=a-b`.  An overlap in (1.2) is a pair of unordered pairs

\[
 P=\{c,d\},\qquad Q=\{e,f\},
 \qquad e+f-(c+d)=q.                             \tag{2.1}
\]

Suppose `P` and `Q` share a point.  After cancelling it, (2.1) becomes an
equality between `q=a-b` and one directed difference of `A`.
Vector-Sidonicity forces that difference to be the ordered edge `(a,b)`.
Thus the overlap is exactly one of (1.3).  Conversely every point
`c notin {a,b}` gives the overlap (1.3), and the pair-sum map is injective.
This proves that the number of overlaps with a shared endpoint is exactly
`k-2`.  After those arrows are removed, a disjoint pair of pairs can still
contain `a` or `b`; these are precisely the repeated-label arrows in
`widetilde h(q)-h_6(q)`.  Removing them leaves the arrows counted by
`h_6(q)`.

For a nontrivial overlap (2.1), put

\[
 T=\{a,c,d\},\qquad U=\{b,e,f\}.
\]

Equation (2.1) is precisely

\[
 \sum_{x\in T}x=\sum_{x\in U}x.                 \tag{2.2}
\]

Because `h_6` excludes all six distinguished endpoints, the two triples are
disjoint, so this is an unordered equal-centroid collision.  The construction
is reversible.  For one unordered collision
`{T,U}`, choosing an ordered direction from one triple to the other and then
one of its `3*3` cross-edges gives 18 directed differences `q`, and hence 18
terms in `sum_q h(q)`.  On the other hand, the same unordered collision
gives

\[
 2(3!)^2=72
\]

ordered six-distinct third-energy configurations.  Therefore
`C_6=72C` and `sum h_6=18C`, which proves (1.5).

## 3. Midpoint-path interpretation

The translation graph of `Sigma` by `q` is a disjoint union of directed
paths.  A vertex `c+d` represents the midpoint `(c+d)/2` of one edge of
`A`; an arrow

\[
 c+d\longmapsto e+f=c+d+q                     \tag{3.1}
\]

says that the two edge midpoints differ by `q/2`, while `q` itself is the
directed vector of the distinguished internal edge `(a,b)`.  The `k-2`
arrows in (1.3) are the stars sharing the third point `c`.  The excess
`h(q)` counts precisely the disjoint-chord arrows.

This form suggests the missing density-sensitive packing theorem: after the
forced star has been deleted, an internal translation should meet the
pair-midpoint set only at the reciprocal-density scale `m^2/k^2`.  Bounding
the raw excess automatically pays for both clean and repeated-label arrows.
The
finite-field parabola shows that no size-only `O(k)` theorem is possible;
its additive structure gives quadratic excess, but every integral metric
separating all of its distances has quadratic geometric height, where the
term `m^2/k^2` pays for it.

## 4. Exact stress profiles

The exact verifier gives

\[
\begin{array}{c|r|r|r|r|c}
\text{family}&k&m&\max h_6(q)&
 \widetilde h(q)\text{ at that shift}&
 {\max h_6(q)\over1+m^2/k^2}\\ \hline
\text{closure }30&30&150&14&15&0.5384\ldots\\
\text{closure }40&40&223&23&26&0.7169\ldots\\
\text{closure }80&80&719&63&69&0.7704\ldots\\
\text{closure }120&120&1514&127&130&0.7928\ldots\\
\text{source }45&45&324&22&24&0.4163\ldots\\
\text{perpendicular ruler }40&40&3202&14&14&0.0021\ldots\\
\text{Costas }22&22&131&34&38&0.9326\ldots\\
\text{parabola image }127&127&20831&1689&1732&0.0627\ldots
\end{array}                                      \tag{4.1}
\]

Every stored family has clean excess at most the right side of (1.6) with
constant one and no subpolynomial loss.  The raw excess is only slightly
larger, but the table does not assert constant one for it.  The Costas stress
is the closest at this size, while the closure sequence rises steadily toward
the same scale.  These are falsification data, not a proof or a justified
sharp constant.

Run

```text
python3 phase2/loop/erdos1208/verify_ambient_third_energy_centroid_gate.py
```

The verifier constructs all common-centroid matchings, forms all 18 directed
cross-edge records, checks (1.5), and directly separates the forced-star,
repeated-label, and clean arrows at the heaviest clean shift of every family.

## 5. Restart target

Prove (1.6), or the weaker clean aggregate substitute

\[
 \sum_{q\in(A-A)^*}h_6(q)
 \le k^{o(1)}(k^2+m^2).                         \tag{5.1}
\]

The exact forced-star subtraction in (1.4) must be retained.  A generic
autocorrelation bound for `Sigma` sees the `k-2` trivial overlaps at every
internal shift and loses a full factor of `k`.  A successful argument must
also use quadratic norm injectivity: the unstretched finite-field parabola
is vector-Sidon and has the same pair-sum path structure at much smaller
height, but repeats Euclidean distances.
