# Hierarchical planar products: the Gram-rank no-go and the surviving polynomial gate

## 1. Outcome

Consider a Cartesian product

\[
 X=P_1\times\cdots\times P_r
\]

and a planar hierarchical embedding

\[
 \Phi(x_1,\ldots,x_r)=\sum_{j=1}^r B^{e_j}p_j(x_j), \qquad
 p_j(x_j)\in\mathbb Z^2.                             \tag{1.1}
\]

Rotations and rational linear maps can be absorbed into the digit maps
after clearing denominators.  This note proves a rigorous no-go for the
most natural attempt to make the scales algebraically independent.

### Theorem A (full coefficient separation gives one global isometry)

Suppose all unordered sums `e_i+e_j`, `i<=j`, are distinct, and `B` is
larger than the total possible coefficient carry.  For two product edges
with digit differences

\[
 v_j=p_j(x_j)-p_j(y_j),\qquad
 w_j=p_j(x'_j)-p_j(y'_j),                            \tag{1.2}
\]

one has

\[
 \|\Phi(x)-\Phi(y)\|^2=\|\Phi(x')-\Phi(y')\|^2
\]

if and only if their full Gram matrices agree:

\[
 \boxed{\langle v_i,v_j\rangle=\langle w_i,w_j\rangle
        \quad(1\le i,j\le r).}                      \tag{1.3}
\]

Equivalently, there is one `O in O(2)` such that

\[
 w_j=Ov_j\qquad\text{for every }j.                  \tag{1.4}
\]

Thus digit-level norm collisions do not tensor.  Every level must use the
same planar isometry.  Once the image of one nonzero digit difference is
chosen there are at most two candidate isometries, and all remaining digit
differences are forced.

### Theorem B (a square-root subcode in the scalar-digit model)

Let `q` be an odd prime and `r=2s`.  Take

\[
 P_j=\{0,u_j,2u_j,\ldots,(q-1)u_j\},                \tag{1.5}
\]

where every `u_i dot u_j` is nonzero.  Under the hypotheses of Theorem A,
the `q^r`-point product image contains a distance-Sidon subset of size

\[
 \boxed{q^s=(q^r)^{1/2}.}                           \tag{1.6}
\]

Consequently this broad fully separated product model cannot be an upper
construction for Erdős #1208 below exponent `1/2`, let alone at the desired
`1/3` exponent.  Algebraic genericity makes the distance coloring *finer*;
it does not amplify the base anti-Ramsey obstruction.

The theorem does not rule out deliberately colliding exponent sums.  That
remaining lane has a different exact form: equality of two sums of squares
of coefficient polynomials.  It is recorded in Section 5 as the only
surviving hierarchical product gate.

## 2. Expansion and carry separation

For `d=x-y`, write `v_j=p_j(x_j)-p_j(y_j)`.  Then

\[
 \|\Phi(x)-\Phi(y)\|^2
 =\sum_jB^{2e_j}\|v_j\|^2
  +2\sum_{i<j}B^{e_i+e_j}\langle v_i,v_j\rangle.    \tag{2.1}
\]

Let `C` bound the absolute difference between corresponding coefficients
of two expansions.  If `B-1>C`, a nonzero top coefficient cannot be
cancelled by all lower powers:

\[
 B^h>C\sum_{a<h}B^a.                                \tag{2.2}
\]

Thus equality at the integer `B` implies coefficientwise equality.  Unique
unordered pair sums then turn (2.1) into (1.3).  Conversely (1.3) plainly
implies equality.

One may take `e_j=3^j`; ternary uniqueness makes every `e_i+e_j`, including
the diagonal sums, distinct.  The scales are enormous, but coordinate
height is irrelevant for an upper construction for `F_2(n)`.

## 3. Why Gram equality is rank-rigid

Define a map on the span of the `v_j` by

\[
 T\left(\sum_ja_jv_j\right)=\sum_ja_jw_j.           \tag{3.1}
\]

It is well-defined: if the first sum is zero, (1.3) says that the squared
norm of the second sum is also zero.  The same calculation shows that `T`
preserves every inner product.  It therefore extends from its at-most
two-dimensional domain to an orthogonal map of the plane.  This proves
(1.4).

This gives a useful fibre bound.  If all digit differences belong to finite
sets `Delta_j` and `M=max_j |Delta_j|`, then every nonzero full-Gram fibre
contains at most

\[
 2M                                                     \tag{3.2}
\]

difference words: choose the first nonzero `v_i`, choose its possible image
`w_i in Delta_i`, and choose one of the at most two orthogonal maps sending
`v_i` to `w_i`.  All later coordinates are forced.  The naive product of
local fibre sizes is therefore wrong by an exponential factor.

For example, two local pairs can have the same individual squared norms
but fail the cross coefficient:

\[
 v_1=(1,0),\quad w_1=(0,1),\qquad
 v_2=(1,1),\quad w_2=(1,-1).                        \tag{3.3}
\]

The two diagonal Gram entries agree, but
`v_1 dot v_2=1` and `w_1 dot w_2=-1`.  Hence a base distance collision in
each of two coordinates does not produce a product distance collision.

## 4. Proof of the square-root subcode

In the scalar-digit model, (1.3) first gives

\[
 |d_j|=|d'_j|\qquad(1\le j\le r).                   \tag{4.1}
\]

On the common nonzero support write `d'_j=sigma_j d_j`.  Since every
`u_i dot u_j` is nonzero, the off-diagonal entries give

\[
 \sigma_i\sigma_j=1.                                \tag{4.2}
\]

All signs on the support are equal, so

\[
 d'=d\quad\text{or}\quad d'=-d.                    \tag{4.3}
\]

It remains to choose a vector-Sidon code in `[0,q-1]^(2s)`.  Identify the
first and second blocks of `s` coordinates with the finite field
`K=F_(q^s)` and take

\[
 \mathcal C=\{(z,z^2):z\in K\}.                     \tag{4.4}
\]

If

\[
 (z,z^2)-(y,y^2)=(z',z'^2)-(y',y'^2)               \tag{4.5}
\]

with nonzero first coordinate `h`, then
`h(z+y)=h(z'+y')`.  Since `q` is odd, the difference and sum determine both
endpoints, so `(z,y)=(z',y')`.  Thus (4.4) is directed-difference Sidon in
the additive group.  Writing field coordinates as least residues preserves
this property over the integers: an integer difference equality implies the
same equality modulo `q`.

Equations (4.3)--(4.5) show that the image of `C` is distance-Sidon and has
the size asserted in (1.6).

The zero-digit cylinder obstruction remains present in the *full* product:
two words differing in only one coordinate have the same displacement when
their common tail is changed.  The code (4.4) is exactly the kind of global
restriction needed to remove those endpoint multiplicities.  It does so
without losing more than the square-root factor.

## 5. The only surviving scale-collision lane

If pair sums `e_i+e_j` are deliberately allowed to collide, (1.3) is
replaced by grouped anti-diagonal sums.  For the consecutive choice
`e_j=j`, put

\[
 X_d(z)=\sum_j(v_j)_1z^j,\qquad
 Y_d(z)=\sum_j(v_j)_2z^j.                            \tag{5.1}
\]

With `B` beyond the carry range, two squared distances are equal exactly
when

\[
 \boxed{X_d(z)^2+Y_d(z)^2
       =X_{d'}(z)^2+Y_{d'}(z)^2}                    \tag{5.2}
\]

as integer polynomials.  Over the Gaussian polynomial ring this is

\[
 (X_d+iY_d)(X_d-iY_d)
 =(X_{d'}+iY_{d'})(X_{d'}-iY_{d'}).                 \tag{5.3}
\]

For collinear digits `Y=0`, the integral-domain identity immediately gives
`X_d=+/-X_d'`; the square-root code above survives unchanged.  Therefore
non-collinear digits and nontrivial Gaussian factor reallocations are both
necessary for any improvement.

Equation (5.3), not a Cartesian product of base color classes, is the exact
residual construction problem.  It has only two conjugate factor channels,
reflecting planar rank two.  No argument is currently known that turns its
factor reallocations into a recursive rainbow upper bound below `n^(1/2)`.
In particular, it does not justify multiplying independent base collision
counts.  A genuine new construction would need an explicit family of
bounded-coefficient polynomial pairs whose norm fibres are exponentially
large *and* whose endpoint-realized edge coloring has no large rainbow
clique.

## 6. Verification

Run

```text
python3 phase2/loop/erdos1208/verify_hierarchical_planar_gram_rank_no_go.py
```

The exact verifier checks pair-sum separation, the coefficient expansion,
the global-sign Gram fibres, the cross-term split (3.3), the zero-cylinder
collision, and a concrete instance of Theorem B with `q=5`, `r=4`:
`625` product vertices contain a verified `25`-point distance-Sidon code.
