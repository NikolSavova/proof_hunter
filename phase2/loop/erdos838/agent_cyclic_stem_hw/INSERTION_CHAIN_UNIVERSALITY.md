# Fixed-edge nesting chains are projectively universal

**Date:** 2026-08-14  
**Verdict:** the antichain side of the endpoint insertion-poset dichotomy is
genuinely useful, but the long-chain side has no intrinsic convex-subset
simplification.  Every finite planar order type can be placed, with every
convex-position subset preserved, inside one strict chain of points inserted
across a fixed edge of a fixed triangle.  Consequently a Kraft/downclosure
bound using only the nesting order would already contain the full difficulty
of Erdős 838.

There is still an exact depth-free quadratic accounting identity for a
recursion carrying fresh tips.  It shows that repeated chain descent itself
does not cost anything: all ordered record pairs are charged exactly at their
first differing tip.  The remaining condition is geometric **tag
absorption**--the two first-difference tips must be incorporated into the two
ordinary output faces without erasing the two inner histories.  Nesting alone
cannot imply this condition, by the universality theorem.

## 1. The insertion cell in tangent coordinates

Put

\[
                         u=(-1,0),\qquad v=(1,0).
\]

For a point `z=(x,y)` with `y>0` and `-1<x<1`, define its two tangent
coordinates

\[
             \ell(z)={x+1\over y},\qquad r(z)={1-x\over y}.       \tag{1}
\]

Both are positive.  A direct barycentric calculation gives

> **Lemma 1 (dominance form of fixed-edge insertion).**  For two points
> `z,w` in the upper wedge,
> \[
> z\in\operatorname{conv}\{u,v,w\}
> \quad\Longleftrightarrow\quad
> \ell(z)\ge\ell(w)\ \text{and}\ r(z)\ge r(w).              \tag{2}
> \]
> If both inequalities are strict, `z` lies in the interior of the
> triangle.

Indeed, if `L=ell(z), R=r(z)` and `L'=ell(w), R'=r(w)`, then

\[
 z=\alpha u+\beta v+\lambda w,
\quad
 \alpha={y(z)\over2}(R-R'),\quad
 \beta ={y(z)\over2}(L-L'),\quad
 \lambda={y(z)\over2}(L'+R').                              \tag{3}
\]

The three coefficients sum to one.  Thus the endpoint insertion poset in a
fixed edge cell is exactly a two-dimensional dominance order.  Incomparable
pairs are precisely the pairs compatible over the base, as in Lemma 3 of
`../agent_all_interval_isoperimetry/TWO_RECORD_UNCROSSING.md`.

## 2. Universality of one strict nesting chain

> **Theorem 2 (projective universality).**  Let `P` be any finite planar
> point set in general position.  There are a triangle `B`, an edge `uv` of
> `B`, and a labelled set
> \[
>                         X=\{x_1,\ldots,x_n\}
> \]
> in the insertion cell of `uv` such that:
>
> 1. `x_i` is strictly inside `conv(B+x_j)` whenever `i<j`; hence the
>    insertion poset induced on `X` is one strict chain;
> 2. the labelled order type of `X` is projectively equivalent to that of
>    `P`, up to a global orientation reversal; and
> 3. for every labelled subset `S`,
>    \[
>       S\text{ is in convex position in }P
>       \quad\Longleftrightarrow\quad
>       X_S\text{ is in convex position}.                    \tag{4}
>    \]

**Proof.**  Choose an affine coordinate direction giving distinct first
coordinates and list the points as `p_i=(a_i,b_i)` with
`a_1<...<a_n`.  Choose `M` so large that

\[
                         c_i=b_i+Ma_i
\]

is also strictly increasing.  For sufficiently large `C,D`, put

\[
                  L_i=C-a_i>0,\qquad R_i=D-c_i>0.             \tag{5}
\]

Both sequences are strictly decreasing.  The affine map
`(a,b) -> (L,R)` has determinant one, so it preserves the order type.

Now apply

\[
 \Phi(L,R)=\left({L-R\over L+R},{2\over L+R}\right).          \tag{6}
\]

In homogeneous coordinates this is the nonsingular linear map

\[
 [L:R:1]\longmapsto[L-R:2:L+R],                              \tag{7}
\]

whose determinant is `-4`.  The denominator `L+R` is positive on the whole
convex hull of the transformed input.  Therefore `Phi` maps convex hulls to
convex hulls and preserves membership in the convex hull of every labelled
subset.  In particular it preserves extremality of every member of every
subset, proving (4).  Its negative determinant accounts for the harmless
global orientation reversal.

Equation (1) recovers exactly `ell(Phi(L_i,R_i))=L_i` and
`r(Phi(L_i,R_i))=R_i`.  Hence (2) and the strict decrease in (5) show that
the images form one strict nesting chain.  A sufficiently small horizontal
shear avoids equal output first coordinates without changing either tangent
order.  Finally take `B` to consist of `u,v` and a generic point below the
line `uv`.  Every `B+x_i` is a convex quadrilateral inserted through the
same edge, and the generic lower vertex makes the whole ambient set general
position.  QED.

The positivity of the projective denominator is load-bearing.  Explicitly,
if `q=sum lambda_i p_i`, projective barycentric weights are obtained by
reweighting `lambda_i` by the positive denominators.  Applying the same
argument to the inverse proves both directions of convex-hull membership.

> **Corollary 3 (profile transfer).**  If
> \[
>                         v_k(P)=\#\{k\text{-point convex subsets of }P\},
> \]
> then the strict insertion chain `X` in Theorem 2 satisfies
> `v_k(X)=v_k(P)` for every `k`.  The full hull polynomial, its mean rank,
> and `n Z(1/2)/Z(1)` are all unchanged.

Thus a lower bound for convex faces derived solely from “the endpoint poset
is a long chain” is not a reduction in complexity.  Applied to the image in
Theorem 2, it is already the same lower bound for an arbitrary planar order
type.

## 3. Exact first-difference Kraft identity with fresh tips

The obstruction above does **not** mean that a dynamic chain descent pays a
factor per level.  Let a rooted tree have the repair records as singleton
leaves.  Write `e_v` for the number of records below a node `v`.  Children
partition their parent's records.  The ordered pairs which first choose
different children at `v` number

\[
                         e_v^2-\sum_{w\text{ child of }v}e_w^2.    \tag{8}
\]

> **Lemma 4 (quadratic prefix Kraft equality).**
> \[
> \boxed{
>   |\mathcal R|^2
>    =|\mathcal R|+
>      \sum_{v\text{ internal}}
>       \left(e_v^2-\sum_{w\text{ child of }v}e_w^2\right).}      \tag{9}
> \]

This is just telescoping: every internal square occurs once positively and
once negatively, while the singleton leaf squares sum to `|R|`.  Equivalently,
each off-diagonal ordered pair is charged exactly once, at its first
divergence.  The identity is valid for an arbitrarily deep, unbalanced tree
and is the integral counterpart of the collision identity in
`DYNAMIC_COLLISION_KERNEL.md`.

If child transitions carry globally fresh tip labels, the unordered
two-point face consisting of the first differing tips determines the
divergence node and its two child branches, up to order.  Consequently there
is no combinatorial depth or decoder-state loss.  But that tip-pair already
uses one of the two allowed output faces.  A proof of the desired quadratic
bound still needs the following geometric merge.

> **Tag-absorption gate.**  At every positive-mass first divergence, merge
> the two fresh tips into one of the two descendant face outputs--or merge
> the two inner histories into one ordinary face--with total global
> face-pair reuse `2^{o(r)}`.

Opposite-side tangent pairs satisfy this gate by the cross-union decoder.
Balanced two-ended product cells satisfy it by Theorem 2 of
`../agent_all_interval_isoperimetry/TWO_RECORD_UNCROSSING.md`.  A comparable
chain, by itself, does not: Theorem 2 above lets the two inner histories have
an arbitrary planar order type.

This cleanly separates the two facts which were previously conflated:

* the **Kraft accounting** across a long nested chain is exact and free;
* the **geometric two-face realization** of its first-difference charges is
  the remaining hard theorem.

## 4. Adversarial audit

The verifier transfers five exact configurations into one strict insertion
chain and checks every chirotope sign, every nesting relation, ambient general
position, and the full graded profile by the independent reflection-order
evaluator.

| input family | `n` | profile `v_0,v_1,...` | `V` |
|---|---:|---|---:|
| central Pascal `T_(6,3)` | 20 | `1,20,190,1140,3225,4260,2116` | 10,952 |
| saved half-weight record | 20 | `1,20,190,1140,2415,866,135,8` | 4,775 |
| saved half-weight record | 24 | `1,24,276,2024,5378,2679,413,43,3` | 10,841 |
| saved half-weight record | 30 | `1,30,435,4060,13975,10607,3158,481,30` | 32,777 |
| exact finite `H>2` record | 58 | `1,58,1653,30856,220958,428915,284982,76995,15100,2179,210` | 1,061,907 |

The last row has

\[
             58Z(1/2)/Z(1)={33,994,061\over16,990,512}>2.
\]

It therefore also rules out any constant-two assertion that tries to use
fixed-edge nesting as an extra hypothesis.  The central Pascal row confirms
that the high-mean/QMS obstruction survives the same transformation, while
the `n=20,24,30` records confirm that the low-face hard profiles do too.

Run

```bash
python3 phase2/loop/erdos838/agent_cyclic_stem_hw/verify_insertion_chain_universality.py
```

The checker uses exact `Fraction` arithmetic.  Its certificate is
`insertion_chain_universality_certificate.json`.

## 5. Consequence for the attack

The endpoint-poset regularization now has a sharp interpretation.

1. **Small height:** Mirsky partitions the insertion cell into few
   antichains; two nonadjacent endpoint antichains supply the two-ended face
   reservoir, and the existing product-cell decoder applies.
2. **Long chain:** do not expect a chain/downclosure face surplus.  Contract
   forced unary stretches, retain every entropy-bearing tip, and use (9) to
   send first-difference pairs either to an opposite-side switch or to a
   recursively exposed internal face bank.
3. **Remaining exact gate:** prove a planar tag-absorption/Carleson theorem
   for those first-difference banks.  It must use how the nested tips repair
   the varying sources, not merely their fixed-edge containment order.

This kills a tempting but circular route and leaves a more precise target:
the missing theorem is a relation between the outer nesting chain and the
two hidden source histories, rather than an isoperimetric theorem about the
chain itself.
