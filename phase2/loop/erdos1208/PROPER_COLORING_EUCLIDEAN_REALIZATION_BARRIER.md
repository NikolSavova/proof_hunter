# A Euclidean realization barrier for proper anti-Ramsey colorings

## Status and scope

This note gives a rigorous obstruction on the upper-construction side of
Erdos #1208.  It rules out two of the most economical ways of importing a
proper anti-Ramsey coloring into the planar distance problem:

1. **every** proper coloring of `K_n` with the minimum possible `n-1`
   colors (so `n` is even), regardless of the combinatorics of its
   one-factorization;
2. the standard cyclic sum coloring, even when its `n` color classes are
   allowed.

The first obstruction is geometric and stronger than a dimension count:
any exact Euclidean realization is forced to be concyclic, after which a
one-dimensional Sidon extraction gives a distance-Sidon subset of order
`sqrt(n)`.  The second is an exact low-rank obstruction for the cyclic
Hankel distance matrix.

Thus neither route can improve the already available exponent `0.49815`
(or the later number-field refinements).  This does **not** rule out a
proper coloring using more than `n` colors with nonconstant weighted row
sums, nor a genuinely non-Hankel low-rank Euclidean color matrix.  Those are
the exact survivors.

## 1. Minimum-color proper colorings force a circle

### Theorem 1 (one-factorization circle barrier)

Let `n` be even and let

\[
 \chi:E(K_n)\longrightarrow C,\qquad |C|=n-1,
\]

be a proper edge coloring.  Suppose that there are distinct points
`p_1,...,p_n in R^2` and positive numbers `(lambda_c)_{c in C}` such that

\[
 \lVert p_i-p_j\rVert^2=\lambda_{\chi(ij)}
 \qquad(i\ne j).                                      \tag{1.1}
\]

Then all the points lie on one circle whose center is their centroid.
Consequently the point set contains a distance-Sidon subset of cardinality

\[
 \left(\frac1{6\sqrt3}+o(1)\right)\sqrt n,             \tag{1.2}
\]

and in particular one of cardinality `c sqrt(n)` for an absolute `c>0`.

Here distance-Sidon means that all distances determined by unordered pairs
of distinct selected points are different.

### Proof

At a fixed vertex `i`, properness says that the `n-1` incident edges have
different colors.  There are exactly `n-1` colors, so every color occurs
exactly once at `i`.  Hence every squared-distance row has the same sum:

\[
 \sum_{j=1}^n\lVert p_i-p_j\rVert^2
   =\sum_{c\in C}\lambda_c=:S.                         \tag{1.3}
\]

Put

\[
 \bar p=\frac1n\sum_jp_j,
 \qquad Q=\sum_j\lVert p_j-\bar p\rVert^2.
\]

The centroid identity gives, for every `i`,

\[
 \sum_j\lVert p_i-p_j\rVert^2
   =n\lVert p_i-\bar p\rVert^2+Q.                      \tag{1.4}
\]

Equations (1.3)--(1.4) show that all
`||p_i-bar p||` are equal.  Since the points are distinct, the common radius
is positive, proving concyclicity.

It remains to record why a circle cannot be an anti-Ramsey extremizer at the
cube-root scale.  Partition the circle into four half-open arcs of angular
width `pi/2`.  One arc contains a set `A` of at least `n/4` points.  Regard
their arguments as real numbers in one interval.  The Sidon-subset theorem
for arbitrary finite subsets of the reals gives an additive Sidon subset
`B` of these arguments with

\[
 |B|\ge \left(\frac1{3\sqrt3}+o(1)\right)\sqrt{|A|}
 \ge \left(\frac1{6\sqrt3}+o(1)\right)\sqrt n.         \tag{1.5}
\]

The constant quoted here is Theorem 2.1 of Bailleul--Riblet,
*On the largest Sidon subset in a finite subset of* `R^N`,
[arXiv:2605.03181](https://arxiv.org/abs/2605.03181).  The older
Komlos--Sulyok--Szemeredi theorem `|B| >= c sqrt(|A|)` is already enough for
the exponent barrier.

For two points of arguments `alpha,beta` on a circle of radius `R`,

\[
 \lVert p(\alpha)-p(\beta)\rVert^2
   =4R^2\sin^2\frac{|\alpha-\beta|}{2}.                \tag{1.6}
\]

On an arc of width `pi/2`, the right side is strictly increasing in
`|alpha-beta|`.  Equal chord lengths therefore give

\[
 |\alpha-\beta|=|\gamma-\delta|.
\]

After orienting the two differences this becomes, for example,
`alpha+delta=gamma+beta`.  Additive Sidonicity says that the two unordered
summand pairs agree, and nonzero differences leave only the original
unordered chord pair.  Thus all chord lengths determined by `B` are
different.  This proves (1.2).  QED

### Consequence for the anti-Ramsey route

For even `n`, a proper coloring of `K_n` with `n-1` colors is precisely a
one-factorization.  Abstract one-factorizations can have rainbow clique
number at the generic cube-root scale, but Theorem 1 says that **no exact
planar distance realization of any such coloring can retain that behavior**:
the realized point set always has a rainbow/distance-Sidon subset of order
at least `sqrt(n)`.

Notice that (1.1) only asks every color class to have one common Euclidean
length.  It does not require different colors to have different lengths.
Allowing further coincidences between colors therefore does not evade the
circle conclusion.

## 2. The cyclic sum coloring has large Euclidean minrank

The one-factorization argument uses exactly `n-1` colors.  A natural attempt
to evade it is the proper cyclic sum coloring

\[
 \chi(\{i,j\})=i+j\pmod n,
\]

which has `n` available colors.  The following exact rank calculation rules
out this realization too.

### Theorem 2 (cyclic Hankel displacement barrier)

Let `a_0,...,a_{n-1}` be nonzero real numbers and define the symmetric
`n by n` matrix (indices are modulo `n`)

\[
 D_{ii}=0,\qquad D_{ij}=a_{i+j}\quad(i\ne j).           \tag{2.1}
\]

Then

\[
 \operatorname{rank}D\ge
 \frac{n-\gcd(n,2)}2.                                  \tag{2.2}
\]

In particular, (2.1) cannot be the squared-distance matrix of planar points
when `n` is odd and `n>=11`, or when `n` is even and `n>=12`.

### Proof

Let

\[
 H_{ij}=a_{i+j},\qquad
 \Delta=\operatorname{diag}(a_{2i}),
\]

so `D=H-Delta`.  Let `S e_j=e_{j+1}` be the cyclic shift.  The Hankel form
gives the exact displacement identity

\[
 SH=HS^{-1}.
\]

Consequently

\[
 SD-DS^{-1}=-S\Delta+\Delta S^{-1}=:K.                \tag{2.3}
\]

The equation `Kx=0` is

\[
 a_{2i}x_{i+1}=a_{2(i-1)}x_{i-1},
\]

or, on setting `j=i-1`,

\[
 x_{j+2}=\frac{a_{2j}}{a_{2j+2}}x_j.                  \tag{2.4}
\]

Because all `a_j` are nonzero, this step-two recurrence has at most one free
initial value on each orbit of addition by `2`.  Hence

\[
 \dim\ker K\le\gcd(n,2),
 \qquad \operatorname{rank}K\ge n-\gcd(n,2).          \tag{2.5}
\]

For odd `n` the single recurrence cycle is consistent and equality holds.
For even `n` the two cycles can instead be inconsistent, which only makes
the rank larger.

On the other hand, (2.3) and rank subadditivity give

\[
 \operatorname{rank}K
 \le \operatorname{rank}(SD)+\operatorname{rank}(DS^{-1})
 =2\operatorname{rank}D,
\]

which proves (2.2).  Every squared Euclidean distance matrix in `R^2` has
rank at most `2+2=4`, giving the stated thresholds.  QED

This proof permits repeated values among the `a_c`; only positivity/nonzero
values are needed in a distance realization.

## 3. Exact survivor

The two theorems sharply narrow the proper-coloring construction program.
A route that could improve the current exponent must avoid both mechanisms,
for example by producing a proper coloring with strictly more than `n`
colors such that

* the weighted color multiset incident to a vertex is not row-regular (so
  the centroid identity does not force a circle), and
* the resulting color-equality matrix has Euclidean minrank at most four
  without a low-displacement Hankel/Toeplitz presentation.

This is a genuine non-Cayley, non-one-factorization realization problem.
Dimension counting alone is not a proof because the color-equality equations
can be highly dependent; Theorems 1--2 identify two exact dependencies and
show that both land on the wrong side of the `1/2` barrier.

## 4. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_proper_coloring_euclidean_realization_barrier.py
```

The verifier checks over exact rational arithmetic:

1. the centroid row-sum identity on several deterministic point sets;
2. the cyclic displacement identity `SH=HS^{-1}`;
3. `rank(K)>=n-gcd(n,2)` and the claimed rank inequality for deterministic
   nonzero weight vectors through `n=20`;
4. a finite additive-Sidon angle set and the induced uniqueness of chord
   lengths inside an arc shorter than `pi/2`.
