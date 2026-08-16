# Mean boundary versus one-triple circuit codegree

**Date:** 2026-08-14.  All logarithms are base two.  The empty face is
included.

## Verdict

This note does not prove the minimizer mean conjecture

\[
                  \mu(P_n)\ge(1-o(1))\log n.                \tag{1}
\]

It gives a new exact planar reduction with the correct coefficient scale.
Let `R` be the largest size of a convex subset, and let `Delta` be the
maximum number of bad four-circuits containing one fixed triple.  Then

\[
             \boxed{\displaystyle
             \mu(P)\ge {n\over 2+\Delta(R-2)}.}              \tag{2}
\]

The planar content is a tangent compression: all non-addable points over an
`h`-vertex convex face are covered by at most `h(h-2)` triple stars, rather
than all `binom(h,3)` triples.  Interior points use a fan triangulation;
blocked exterior points use a tangent endpoint, its first hidden neighbor,
and the opposite tangent endpoint.

For a global `V`-minimizer, the known construction upper bound gives

\[
                 R\le\log V(P)\le(1/2+o(1))(\log n)^2.       \tag{3}
\]

Consequently a fixed mean deficit forces an almost-linear one-triple
circuit star.  If `L=log n` and
`mu(P)<=(1-epsilon)L`, then

\[
       \boxed{\displaystyle
       \Delta\ge\left({2\over1-\epsilon}-o(1)\right)
                         {n\over L^3}.}                     \tag{4}
\]

In particular, minimizers with
`Delta<=(2+o(1))n/(log n)^3` satisfy (1).  Thus the minimizer-only mean route
has an exact dichotomy:

1. bounded circuit codegree gives the desired mean and closes the deletion
   recurrence; or
2. one fixed triple participates in `n/polylog(n)` bad four-circuits.

The second alternative is a genuine one-pocket/common-root child.  After
fixing which point is interior in each circuit, a set of at least
`Delta/4` labels lies in one common triangle pocket or one common exterior
root cone.  Its unrestricted convex faces must be used recursively.  The
hull-partition identity does not convert that reservoir into many *uniform*
closed sets automatically: a single three-extreme closed set can carry
Boolean weight `2^m`.

This is a rigorous reduction, not a proof of (1), and it does not use the
false universal QMS inequality or any finite `H<=2` assertion.

## 1. Face covers and non-addable labels

Let `mathcal F(P)` be the convex-position subsets of an `n`-point planar
general-position set.  For `A in mathcal F(P)`, put

\[
 u(A)=|\{p\in P-A:A\cup\{p\}\in\mathcal F(P)\}|,
 \qquad b(A)=n-|A|-u(A).                              \tag{5}
\]

Thus `b(A)` counts all non-addable labels: points inside `conv(A)` and
exterior points which hide at least one old vertex.  Under the uniform face
law, write `H=|A|` and `mu=E H`.  The maps
`A -> cl(A)` and `K -> ext(K)` are inverse, so this is exactly the uniform
closed-set law and `H` is its number of extreme points.

Every cover `A < A union {p}` is counted once from below and once for each
point of the upper face from above.  Hence

\[
                         \mathbb E u(A)=\mu.                \tag{6}
\]

Averaging (5) gives the exact balance

\[
                         \boxed{\mathbb E b(A)=n-2\mu.}     \tag{7}
\]

For a triple `T subset P`, define its bad-circuit degree

\[
 d(T)=|\{p\in P-T:T\cup\{p\}\text{ is nonconvex}\}|,
 \qquad \Delta=\max_{|T|=3}d(T).                    \tag{8}
\]

General position makes every bad four-set a `3+1` circuit with a unique
interior point.

## 2. The planar tangent compression

> **Lemma 1 (quadratic triple cover).**  If `A` is a convex face of size
> `h`, there is a family `mathcal T(A) subseteq binom(A,3)` of size at most
> `h(h-2)` such that every non-addable `p` has
> \[
>                T\cup\{p\}\text{ nonconvex}
>                \quad\text{for some }T\in\mathcal T(A).   \tag{9}
> \]

**Proof.**  There is nothing to prove for `h<=2`.  Write the vertices of
`A` in cyclic order as `v_0,...,v_(h-1)` and take

\[
 \mathcal T(A)=
 \{\{v_i,v_{i+1},v_j\}:0\le i<h,
                 \ j\notin\{i,i+1\}\},                    \tag{10}
\]

where indices are cyclic and repetitions of the same unordered triple are
discarded.  The displayed list has `h(h-2)` entries before repetitions.

If `p` lies inside `conv(A)`, the fan triangulation from `v_0` puts `p`
strictly inside one triangle
`v_0 v_i v_(i+1)`, which belongs to (10).

Otherwise `p` is exterior.  Since it is not addable, insertion of `p`
hides a nonempty consecutive boundary chain of `A`.  Let `v_i,v_j` be the
two tangent endpoints and orient the hidden chain from `v_i` to `v_j`.
Its first hidden vertex is `v_(i+1)`, and convexity puts it strictly inside
the triangle `p v_i v_j`.  Thus
`{v_i,v_(i+1),v_j}` is a member of (10) witnessing (9).  QED.

The use of consecutive vertices is load-bearing.  A generic Caratheodory
cover by every triple would cost `Theta(h^3)` and would weaken the
minimizer conclusion from `n/(log n)^3` to `n/(log n)^5`.

## 3. The codegree--mean inequality

> **Theorem 2 (circuit codegree controls mean boundary).**  If `R>=3` is
> the maximum face rank, then (2) holds.

**Proof.**  Lemma 1 and (8) give, pointwise,

\[
                  b(A)\le\sum_{T\in\mathcal T(A)}d(T)
                       \le\Delta H(H-2)                    \tag{11}
\]

for `H>=3`; both sides are zero for `H<=2`.  Since `H<=R`, averaging gives

\[
          n-2\mu=\mathbb E b(A)
             \le\Delta\mathbb E[H(H-2)_+]
             \le\Delta(R-2)\mu.                           \tag{12}
\]

Rearranging proves (2).  QED.

There is also a useful rooted form of the obstruction.

> **Corollary 2.1 (one rooted circuit star).**  Some triple `T` has
> `d(T)=Delta`.  Among its circuit neighbors, at least `Delta/4` have the
> same interior-point role.  Hence one of the following holds for a fixed
> ordered triple `(a,b,c)`:
>
> * at least `Delta/4` points lie in `int conv{a,b,c}`; or
> * at least `Delta/4` points `p` satisfy
>   `b in int conv{a,c,p}`.

**Proof.**  A bad four-set has exactly one of its four points in the convex
hull of the other three.  Partition the `Delta` neighbors by that role and
pigeonhole.  QED.

## 4. The minimizer consequence

Let `P_n` attain `f(n)`, put `L=log n`, and suppose
`mu(P_n)<=(1-epsilon)L`.  Every subset of a largest `R`-face is a face, so

\[
                         2^R\le V(P_n)=f(n).                \tag{13}
\]

The proved construction upper bound for Erdős 838 is

\[
                         \log f(n)\le(1/2+o(1))L^2.         \tag{14}
\]

Solving (12) for `Delta` and using (13)--(14) gives

\[
 \begin{aligned}
 \Delta
 &\ge {n-2\mu\over(R-2)\mu}\\
 &\ge \left({2\over1-\epsilon}-o(1)\right){n\over L^3},   \tag{15}
 \end{aligned}

which is (4).  Notice that the minimizer hypothesis is used only at the
sharp point (14); inequality (2) is universal.

The usual deletion-minimality identity remains the coefficient interface.
If `I_p` is the number of faces containing `p`, then

\[
 \sum_p I_p=\mu f(n),\qquad
 f(n-1)\le f(n)\left(1-\frac\mu n\right).                  \tag{16}
\]

Thus the low-codegree branch of Theorem 2 gives
`mu>=(1-o(1))L`, and summing (16) yields
`log f(n)>=(1/2-o(1))L^2`.  The only branch not discharged by this route is
the rooted star in Corollary 2.1.

## 5. What the hull partition does and does not add

For the closed set `K=cl(A)`, let

\[
 h(K)=|ext(K)|,qquad i(K)=|K|-h(K).
\]

The exact Boolean-interval partition is

\[
 (1+t)^n=\sum_{K\text{ closed}}t^{h(K)}(1+t)^{i(K)}.       \tag{17}
\]

It identifies the dense interior-star obstruction exactly.  If a triangle
`T` contains `m` other labels and `K=cl(T)`, then one term of (17) is

\[
                         t^3(1+t)^m,                       \tag{18}
\]

so at `t=1` this **single** closed set has Boolean weight `2^m`.  Such
examples are scalable and rational: take the outer triangle

\[
 (0,0),\quad (M,0),\quad(0,M),\qquad M=(m+1)^3,            \tag{19}
\]

and the interior parabola points `(j,j^2)`, `1<=j<=m`.
They are in general position and all lie strictly inside the triangle.
Indeed, no three parabola points are collinear; slopes from `(0,0)` are
distinct; equality of slopes from `(M,0)` would give
`ij=M(i+j)`, impossible for `i,j<=m`; and equality from `(0,M)` would give
`(i-j)(1+M/(ij))=0`.  The three boundary-line cases are immediate from
`0<j,j^2` and `j+j^2<M`.

Therefore (17) alone cannot turn a high-codegree interior pocket into many
uniform closed sets or a large uniform mean `h`.  The unrestricted faces of
the pocket must be retained as a separate bank and summed with controlled
overlap.  This is the same nonlocal reservoir issue isolated in the final
common-base completion child, now derived directly from minimizer mean
failure.

The example in (19) is not a counterexample to (1): its interior parabola is
itself in convex position.  It is an exact obstruction only to an immediate
change of measure from (17).

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_minimizer_circuit_codegree.py
```

The checker uses exact integer/rational orientation tests on the certified
nine-point minimizer and the eleven-point repair-star configuration.  It
enumerates every face and every non-addable incidence, constructs the
quadratic canonical triple cover, and verifies (7), (11), and (12) as exact
integer inequalities.  It also verifies the scalable triangle/parabola
certificate for `m=2,...,40`.
