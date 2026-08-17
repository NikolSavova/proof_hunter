# Placewise prime-power depths for the Minkowski-grid sieve

## Status

This note records a strengthening of the prime-power refinement used for
Erdos #1208.  The algebraic counting argument below is self-contained up to
the same two inputs as `proof_prime_power.md`: the bounded-root-discriminant
tower with specified completely split primes, and the elementary Minkowski
box estimates.  The floating-point optimization in
`search_placewise_depths.py` is exploratory; a numerical exponent becomes a
theorem only after the rounding and interval certificate described below.

## Setup

Let \(K\) be totally real of degree \(d\).  Suppose the distinct rational
primes \(q_i\equiv1\pmod4\) split completely:

\[
 (q_i)=\prod_{j=1}^d\mathfrak p_{i,j}.
\]

For every pair \((i,j)\), choose a depth \(K_{i,j}\geq0\), not necessarily
constant in \(j\), and define

\[
 \mathfrak M=\prod_{i,j}\mathfrak p_{i,j}^{K_{i,j}},\qquad
 \mathcal M=N(\mathfrak M)^{1/d},
\]

\[
 H=\prod_{i,j}(K_{i,j}+1),\qquad
 \Lambda=\prod_{i,j}\left(\sum_{e=0}^{K_{i,j}}q_i^{-e}\right).
\]

Choose, for every \(i\), a Hensel lift \(x_i\) of a square root of \(-1\)
to all powers needed below.  A global valuation pattern is a tuple
\(\mathbf a=(a_{i,j})\) with \(0\leq a_{i,j}\leq K_{i,j}\).  Put

\[
 L_{\mathbf a}=\left\{(u,v)\in\mathcal O_K^2:
 \begin{array}{l}
 u-x_iv\in\mathfrak p_{i,j}^{a_{i,j}},\\
 u+x_iv\in\mathfrak p_{i,j}^{K_{i,j}-a_{i,j}}
 \end{array}
 \text{ for every }i,j\right\}.
\]

Because \(2x_i\) is a unit at every odd \(\mathfrak p_{i,j}\), CRT gives

\[
 [\mathcal O_K^2:L_{\mathbf a}]=N(\mathfrak M)
\]

for every pattern, and there are exactly \(H\) patterns.

## Pair lower bound

Let \(A\subset\mathcal O_K^2\) be finite.  For a pattern \(\mathbf a\), let
\(S_{\mathbf a}\) be the ordered pairs \((x,y)\in A^2\), \(x\ne y\), with
\(x-y\in L_{\mathbf a}\).  Cauchy--Schwarz over the cosets gives

\[
 |S_{\mathbf a}|\geq
 \frac{|A|(|A|-N(\mathfrak M))}{N(\mathfrak M)}.
\]

Consequently

\[
 \sum_{\mathbf a}|S_{\mathbf a}|\geq
 H\frac{|A|(|A|-N(\mathfrak M))}{N(\mathfrak M)}. \tag{1}
\]

No Galois invariance of \(\mathfrak M\) is used here.

## Multiplicity and divisor switching

Write a difference as \((u,v)\) and put \(\eta=u^2+v^2\).  Membership in any
\(L_{\mathbf a}\) implies \(\eta\in\mathfrak M\).  At a fixed place, set

\[
 \alpha=v_{\mathfrak p}(u-x_iv),\qquad
 \beta=v_{\mathfrak p}(u+x_iv),\qquad K=K_{i,j}.
\]

The admissible values of \(a\) lie in

\[
 [K-\beta,\alpha]\cap[0,K].
\]

As in the uniform-depth proof, if there are \(h+1\) admissible values then
\(v_{\mathfrak p}(\eta)\geq K+h\).  Thus the number of global patterns which
can contain a fixed ordered pair is at most the number of ideals
\(\mathfrak b\) such that

\[
\mathfrak b\mid\mathfrak M,\qquad
 \mathfrak M\mathfrak b\mid(\eta),
\]

where the exponent of \(\mathfrak p_{i,j}\) in \(\mathfrak b\) ranges
independently from \(0\) to \(K_{i,j}\).

If \(A\) is distance-Sidon, every nonzero algebraic squared distance \(\eta\)
comes from at most two ordered pairs.  If all differences of elements of the
ambient box have \(\eta\in B_K(Y)\), (1) therefore gives

\[
 H\frac{|A|(|A|-N(\mathfrak M))}{N(\mathfrak M)}
 \leq
 2\sum_{\mathfrak b\mid\mathfrak M}
   |\mathfrak M\mathfrak b\cap B_K(Y)|. \tag{2}
\]

This is the key non-uniform master inequality.

## Box estimate

The standard ideal-packing lemma gives

\[
 |\mathfrak M\mathfrak b\cap B_K(Y)|
 \leq
 \left(1+\frac{2Y}{
 \mathcal M N(\mathfrak b)^{1/d}}\right)^d. \tag{3}
\]

Moreover

\[
 N(\mathfrak b)^{1/d}\leq\mathcal M
\]

for every \(\mathfrak b\mid\mathfrak M\), and

\[
 \sum_{\mathfrak b\mid\mathfrak M}\frac1{N(\mathfrak b)}=\Lambda. \tag{4}
\]

Put \(x=N(\mathfrak b)^{1/d}\).  Since \(x\leq\mathcal M\), (3) with
\(Y=2R^2\) gives

\[
 \left(1+\frac{4R^2}{\mathcal Mx}\right)^d
 =\left[\frac{R^2}{\mathcal Mx}
 \left(4+\frac{\mathcal Mx}{R^2}\right)\right]^d
 \leq\left[\frac{R^2}{\mathcal Mx}
 \left(4+\frac{\mathcal M^2}{R^2}\right)\right]^d. \tag{5}
\]

Summing (5) and using (4) yields

\[
 2\sum_{\mathfrak b\mid\mathfrak M}
 |\mathfrak M\mathfrak b\cap B_K(2R^2)|
 \leq 2\left[
 \frac{R^2\Lambda^{1/d}}{\mathcal M}
 \left(4+\frac{\mathcal M^2}{R^2}\right)
 \right]^d. \tag{6}
\]

Comparing (2) and (6), and treating the case
\(|A|<N(\mathfrak M)=\mathcal M^d\) separately, gives the exact
non-uniform analogue of the uniform master bound:

\[
 \boxed{
 |A|\leq \mathcal M^d+\sqrt2R^d
 \left[(\Lambda/H)^{1/d}
 \left(4+\frac{\mathcal M^2}{R^2}\right)\right]^{d/2}.} \tag{7}
\]

Indeed, when \(|A|\geq\mathcal M^d\),
\((|A|-\mathcal M^d)^2\leq |A|(|A|-\mathcal M^d)\); taking square roots
after (2) and (6) gives (7).  Thus the proof depends on the non-rational
modulus only through \(\mathcal M\), \(H\), and \(\Lambda\).  Neither Galois
invariance nor rationality of the modulus is used.

For the exponent normalization used by the optimizer, suppose the tower has
root discriminant at most \(D\), take
\(R=\sqrt D\,n^{1/(2d)}\), and put

\[
 w=\frac{\log n}{2d},\qquad
 z=\frac{\mathcal M^2}{R^2}=\frac{e^{2(L-w)}}D.
\]

Then (7) reads

\[
 |A|\leq n^{E_1}+\sqrt2\,n^{E_2},
 \quad E_1=\frac L{2w},\quad
 E_2=\frac12+\frac{\log D-G+\log(4+z)}{4w}. \tag{8}
\]

The relaxed calculation replaces \(\log D+\log(4+z)\) by
\(\log(4D)\).  This lowers \(E_2\) by the positive but, in the proposed
parameters, extremely small quantity \(\log(1+z/4)/(4w)\).  A rigorous
certificate must retain that term rather than discard it.

## Convexification consequence

Define the per-degree cost and gain

\[
 L=\frac1d\log N(\mathfrak M)
   =\frac1d\sum_{i,j}K_{i,j}\log q_i,
\]

\[
 G=\frac1d\log\frac H\Lambda
  =\frac1d\sum_{i,j}
    \log\left(\frac{K_{i,j}+1}
    {\sum_{e=0}^{K_{i,j}}q_i^{-e}}\right).
\]

For each rational prime \(q_i\), the pair \((L,G)\) may therefore use an
arbitrary empirical distribution of depths across its \(d\) split places.
As \(d\to\infty\), this realizes the convex hull of the integer-depth points

\[
 \left(K\log q_i,
 \log\frac{K+1}{\sum_{e=0}^Kq_i^{-e}}\right),\qquad K=0,1,2,\ldots,
\]

with rounding error \(O(1/d)\).  The existing uniform-depth argument uses
only vertices of these convex hulls.

This convexification is not a route through the binary entropy barrier: it
cannot improve the best local gain-to-cost slope.  It can, however, remove a
genuine integer-depth/degree-phase loss.

For a field degree \(d\), a point on one frontier segment with mixing
parameter \(\theta\) is implemented by assigning the deeper depth to
\(\lfloor\theta d\rfloor\) of the \(d\) prime ideals above the relevant
rational prime and the shallower depth to the rest.  Hence the errors in
\(L\) and \(G\) are at most one local cost and one local gain divided by
\(d\).  Along the tower \(d\to\infty\), these errors are \(O(1/d)\), while
\(w\) stays in a fixed compact interval.  Consequently any strict exponent
inequality proved for the continuous frontier survives, with a slightly
smaller fixed margin, for all sufficiently large \(n\); finitely many smaller
\(n\) are absorbed by the implied constant.  This is the required
continuous-to-integral rounding lemma.

## Concave-envelope lemma

For a split rational prime \(q\), write

\[
 g_q(k)=\log\left(\frac{k+1}{1+q^{-1}+\cdots+q^{-k}}\right),
 \qquad \Delta g_q(k)=g_q(k)-g_q(k-1).
\]

Think of the passage from depth \(k-1\) to depth \(k\) at one prime ideal
above \(q\) as an item of cost \(\log q\) and gain \(\Delta g_q(k)\).  Sort
all such items by decreasing gain-to-cost ratio.  The finite certificate
checks that, in the range used below, an item of depth \(k\) never precedes
the depth-\(k-1\) item for the same \(q\).  Fractional knapsack is therefore
compatible with the depth-prefix constraint.  Let \(F(L)\) be its maximum
gain at total cost \(L\).  Then \(F\) is increasing, concave, and piecewise
linear.

Fix \(\alpha<1/2\).  In (8), set the target cost to \(L=2\alpha w\), so the
first exponent is exactly \(\alpha\).  The condition that the second exponent
is at most \(\alpha\) is

\[
 F(2\alpha w)\geq
 \log(4D)+(2-4\alpha)w+
 \log\left(1+\frac{e^{2(2\alpha-1)w}}{4D}\right). \tag{9}
\]

The left side minus the right side of (9) is concave in \(w\).  Indeed,
\(F(2\alpha w)\) is concave, the middle term is affine, and

\[
 -\log(1+ae^{-cw})
\]

is concave for \(a,c>0\).  It follows that (9) on a whole interval
\([w_0,2w_0]\) is certified by its two endpoints.

For an actual field degree \(d\), take every item preceding the one fractional
item at full multiplicity across the \(d\) places, and take that last item at
\(\lfloor\theta d\rfloor\) places.  The resulting cost is no larger than
\(2\alpha w\), its gain is at least \(F(2\alpha w)-\Delta g/d\), and its
\(z\)-term is no larger than the one in (9).  Thus any fixed positive endpoint
margin survives for all sufficiently large \(d\).

## Rank-20 numerical theorem

Take the ramification set

\[
 \mathcal T=\{3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,
 61,67,71,73,79\}.
\]

The following 20 positive square classes form a basis of the totally real
Frattini field:

\[
 5,13,17,29,37,41,53,61,73,
 21,33,57,69,93,129,141,177,201,213,237. \tag{10}
\]

The 79 primes in `rank20_split_primes.txt` are prime, are \(1\pmod4\), and
every class in (10) is a square modulo each of them.  Hence their Frobenius
elements lie in the Frattini subgroup.  The standard tame totally-real
Shafarevich presentation has generator rank 20 and relation rank at most 20.
Killing all 79 Frobenius elements therefore preserves
generator rank 20 and gives

\[
 r\leq20+79=99<20^2/4=100.
\]

Golod--Shafarevich supplies an infinite totally real pro-2 tower in which all
79 primes split completely.  Its root discriminants are bounded by

\[
 D=\prod_{p\in\mathcal T}p
  =1608822383670336453949542277065. \tag{11}
\]

The exact arithmetic in `verify_placewise_rank20.py` checks primality, the
rank of (10), all \(79\cdot20=1580\) residue conditions, (11), and the strict
Golod--Shafarevich inequality.  It then builds the placewise frontier from
the first 20 depth increments at each split prime.  The independent script
`verify_placewise_rank20_intervals.py` replaces all floating-point sign
decisions by exact rational intervals for the logarithms, proves the ordering
of all 534 frontier increments used, and certifies the endpoint inequalities.
With

\[
 \alpha=0.49806,\qquad w_0=5815.2,
\]

the two sides of (9) have margins greater than \(0.24\) at \(w_0\) and
greater than \(0.48\) at \(2w_0\); the exact finite-packing corrections are
included.  The concave-envelope lemma proves (9) throughout the interval.

Given sufficiently large \(n\), choose a layer of dyadic degree \(d=2^j\)
such that

\[
 w=\frac{\log n}{2d}\in[w_0,2w_0).
\]

Such layers exist in the infinite pro-2 tower, and every selected split prime
still splits completely in every subfield.  Implement the fractional frontier
point by the rounding construction above.  Since \(d\to\infty\) with \(n\),
the endpoint margin absorbs the \(O(1/d)\) loss.  Equation (8) gives

\[
 |A|\leq(1+\sqrt2)n^{0.49806}
\]

for every distance-Sidon subset of the constructed \(n\)-point set.  The
finitely many smaller \(n\) are absorbed in the implied constant.  Therefore

\[
 \boxed{F_2(n)\ll n^{0.49806}.} \tag{12}
\]

This is a quantitative improvement of the rank-17 uniform-depth certificate
in `proof_prime_power.md`.  It remains an upper-bound improvement, not a
resolution of the order of magnitude in Erdos #1208.

## Rank-22 upgrade: a clean 0.498 exponent

The same argument with rank 22 crosses the decimal target \(0.498\).  Take

\[
 \mathcal T_{22}=\{3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,
 61,67,71,73,79,83,89\}.
\]

A basis of its totally real Frattini square classes is

\[
 5,13,17,29,37,41,53,61,73,89,
 21,33,57,69,93,129,141,177,201,213,237,249.
\]

The 98 primes in `rank22_split_primes.txt` split in this Frattini field and
in \(\mathbb Q(i)\).  Killing their Frobenius elements gives generator rank
22 and relation-rank bound

\[
 22+98=120<22^2/4=121.
\]

The root-discriminant bound is

\[
 D_{22}=11884370948172775385325268800679155.
\]

Set

\[
 \alpha=0.498,\qquad w_0=6826.7.
\]

`verify_placewise_rank22.py` checks all primality, square-class-rank, and
\(98\cdot22=2156\) residue assertions exactly.  The rational interval
certificate `verify_placewise_rank22_intervals.py` proves that the 580 used
frontier slopes decrease, and gives lower bounds \(0.138\) and \(0.275\) for
the two endpoint margins in (9), including the exact packing correction.
The concavity and rounding argument therefore yields the stronger theorem

\[
 \boxed{F_2(n)\ll n^{0.498}.} \tag{13}
\]

As before, the implied constant absorbs the finite initial range before the
field degrees are large enough to round the one fractional place layer.

## Remaining verification checklist

1. Obtain an independent expert audit of the placewise modulus and the
   concavity/rounding lemma.
2. Continue the structural attack on the square grid; (13) does not address
   the cube-root versus square-root exponent gap.
