# Rooted fans force complementary faces or a homogeneous bank

**Date:** 2026-08-15
**Verdict:** the exact payment behind the one-exception fan extends to every
sign-coherent rooted fan.  If \(W\) is a set of \(m\) vertices seen in one
temporal direction from a root \(p\), then every complementary triple of the
same sign is a distinct rooted four-face.  If there are few such triples,
the opposite-sign triples have a large homogeneous subset, and that subset
generates a Boolean ordinary-face bank entirely outside the rooted fan.

For every integer \(1\le L\le m/2\), the exact alternative is

\[
 \boxed{
 \text{at least }\frac{m^3}{8L^2}\text{ rooted four-faces}
 \quad\text{or}\quad
 \text{an external Boolean bank of size }2^L.}          \tag{1}
\]

The strict whisker fan has no rooted four-faces and therefore forces the
whole complementary set to be a cap or cup, recovering its \(2^m\) external
payment.

There is a sharp scope barrier.  Adjoin a coherent root to the classical
Erdős--Szekeres set \(E(k,k)\), of size
\(m=\binom{2k-4}{k-2}\).  The four-face branch then has at least half of all
triples, while every homogeneous complementary bank has rank below \(k\),
every complementary convex-face bank has rank at most \(2k-4\), and every
rooted cell bank has rank at most \(2k-5\).  Thus the half mass of the
certified rooted four-faces is \(\Omega(m^3)\), whereas every individual
bank supplied by a single homogeneous or convex set is only
\(m\,\mathrm{polylog}(m)\).

Consequently (1) is a real cross-endpoint theorem, but it does not prove
\(H=n^{o(1)}\).  The dense-four-face branch needs a Hall decoder combining
many complementary banks, or a higher-rank iteration with controlled
overlap.  A single Ramsey/same-type bank is quantitatively insufficient.

## 1. Coherent rooted fans

Let

\[
 p<w_1<\cdots<w_m                                      \tag{2}
\]

be the label order of a stretchable type-A reflection order.  Fix a sign
\(\sigma\in\{+,-\}\), and assume the root star is coherent:

\[
 \chi(p,w_i,w_j)=\sigma\qquad(i<j).                    \tag{3}
\]

Equivalently, every two-edge path \(p,w_i,w_j\) is temporal in the
\(\sigma\) direction.  Define

\[
 T_\sigma(W)=
 \#\{i<j<k:\chi(w_i,w_j,w_k)=\sigma\}.                 \tag{4}
\]

> **Theorem 1 (rooted triple promotion).**  The
> \(T_\sigma(W)\) triples in (4) give distinct convex four-faces
> \[
>  \{p,w_i,w_j,w_k\}.                                  \tag{5}
> \]
> They lie in the rooted endpoint cells \((p,w_k)\) and contribute exactly
> \(T_\sigma(W)/16\) to \(F_R(1/2)\).

**Proof.**  In a slope reflection order, a three-edge path is temporal in
direction \(\sigma\) precisely when both consecutive packet signs equal
\(\sigma\).  For

\[
 p,w_i,w_j,w_k,
\]

the first sign is \(\chi(p,w_i,w_j)=\sigma\) by (3), and the second is
\(\chi(w_i,w_j,w_k)\).  Thus (4) is exactly the set of two-internal temporal
supports across the rooted fan.  Pair each with the direct root--\(w_k\)
path in the reverse temporal direction.  The path-pair/face bijection gives
(5).  The vertex set recovers the triple, so the faces are distinct, and a
four-face has half weight \(2^{-4}=1/16\).  \(\square\)

This is the first exact cross-endpoint promotion: pair supports in different
rooted cells are not treated separately; together they are the signed
triple profile of the common complementary set \(W\).

## 2. Sparse promotion forces an external bank

Regard the \(\sigma\)-triples as the edges of a 3-uniform hypergraph
\(\mathcal H_\sigma\) on \(W\).  An independent set in this hypergraph has
all triples of sign \(-\sigma\).  In an ordered point set this is a strict
cap or cup, so every one of its subsets is an ordinary face.

> **Lemma 2 (sampling/deletion).**  A 3-uniform hypergraph with \(m\)
> vertices and \(T\) edges has an independent set of size at least
> \[
>  \max_{0\le q\le1}\{qm-q^3T\}.                       \tag{6}
> \]

**Proof.**  Retain each vertex independently with probability \(q\).  The
expected number of retained vertices minus retained edges is
\(qm-q^3T\).  For one realization attaining at least this value, delete one
vertex from each remaining edge.  The result is independent and loses at
most one vertex per edge.  \(\square\)

Taking \(q=2L/m\) proves the advertised exact alternative.

> **Corollary 3 (four-faces or complementary bank).**  For every integer
> \(1\le L\le m/2\), either
> \[
>  T_\sigma(W)>\frac{m^3}{8L^2},                       \tag{7}
> \]
> or \(W\) contains an opposite-sign homogeneous subset of size at least
> \(L\).  In the second case its \(2^L\) subsets form an ordinary-face bank
> disjoint from all faces in the rooted fan.

Indeed, if \(T\le m^3/(8L^2)\), (6) at \(q=2L/m\) is at least \(L\).
The bank is external because none of its faces contains \(p\).

A convenient optimized form of (6) is

\[
 |I|\ge
 \begin{cases}
 m-T,&T\le m/3,\\[2mm]
 \displaystyle\frac{2m^{3/2}}{3\sqrt{3T}},&T>m/3,
 \end{cases}                                           \tag{8}
\]

up to taking the integer floor.  At \(T=0\), no loss is needed and
\(I=W\).

## 3. Exact recovery of the one-exception payment

In the one-exception sign order,

\[
 \chi(p,w_i,w_j)=+,\qquad
 \chi(w_i,w_j,w_k)=-.                                  \tag{9}
\]

Thus \(T_+(W)=0\).  The rooted forward support family in each endpoint cell
contains only the empty support and the singletons, while all of \(W\) is a
strict cap.  Corollary 3 gives the full external bank \(2^W\), of size
\(2^m\).  This is exactly the compensation observed in the global endpoint
audit; it is now forced by the packet signs rather than guessed from the
coordinates.

More generally, the implication uses only two local facts:

1. the singleton paths in the root star have one coherent direction; and
2. no rooted cell contains a two-internal path in that direction.

The first fact supplies \(\chi(p,w_i,w_j)=\sigma\); the second then forces
\(\chi(w_i,w_j,w_k)=-\sigma\) for every triple.  Hence exact whisker
saturation of a coherent fan always has a complete complementary Boolean
payment.

## 4. Erdős--Szekeres barrier to a single-bank closure

Let \(E(r,s)\) be the classical rational cup--cap construction with no
\(r\)-cup and no \(s\)-cap.  Recursively place a normalized copy of
\(E(r,s-1)\) high-left of a normalized copy of \(E(r-1,s)\), with all cross
slopes separated.  Then

\[
 |E(r,s)|=\binom{r+s-4}{r-2}.                          \tag{10}
\]

Take \(W=E(k,k)\) and put

\[
 m=\binom{2k-4}{k-2}.                                  \tag{11}
\]

At least one of the two triple signs occurs on at least
\(\binom m3/2\) triples.  Place a new leftmost root sufficiently far above
or below \(W\) so that its star has this majority sign \(\sigma\).  After an
arbitrarily small rational generic perturbation, all pair slopes are
distinct without changing any signs.  Sorting them gives a genuine
stretchable reduced word.  Theorem 1 now certifies at least

\[
 T_\sigma(W)\ge\frac12\binom m3                         \tag{12}
\]

rooted four-faces, of total half mass at least \(\binom m3/32\).

On the other hand, every homogeneous subset of \(W\) has size at most
\(k-1\).  Every convex subset is the union of a lower cup and an upper cap,
sharing its endpoints, and therefore has size at most

\[
 R=2k-4.                                                \tag{13}
\]

It follows that:

* every homogeneous complementary Boolean bank has size at most
  \(2^{k-1}\);
* every Boolean bank generated by one complementary convex face has size at
  most \(2^{2k-4}\); and
* every rooted endpoint-cell bank has size at most \(2^{2k-5}\), because a
  convex face containing the root loses one vertex on restriction to \(W\).

The central-binomial estimate

\[
 2^{2k-4}\le(2k-3)m                                    \tag{14}
\]

shows that all these individual banks have size
\(m\,O(\log m)\), while (12) has half mass \(\Omega(m^3)\).  Thus neither a
single homogeneous bank nor a single maximum-face bank can pay the dense
branch with the missing factor \(m^{1-o(1)}\).

This is a genuine reduced-word barrier, but deliberately not a barrier to a
multi-bank Hall theorem.  The dense family of rooted four-faces may contain
the incidence structure needed to combine many external banks.  That is the
surviving exact gate.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_coxeter_global_half/verify_rooted_fan_complement.py
```

The checker builds the rational \(E(k,k)\) construction through \(k=6\),
applies an exact sign-preserving rational generic perturbation, adds a
coherent majority-sign root, and verifies that sorting all distinct slopes
produces an adjacent-swap reduced word.  It checks the temporal
triple-support promotion, convexity of every promoted four-set, the
cup/cap-rank and bank bounds, and every threshold instance of Corollary 3.
It separately replays the zero-triple one-exception family.  No floating
point geometric predicate is used.
