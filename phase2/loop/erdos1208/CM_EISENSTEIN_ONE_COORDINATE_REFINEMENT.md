# CM/Eisenstein one-coordinate refinement of the rank-221 tower

## 1. Verdict

The proposed replacement is sound.  Let `L` be a totally real layer and put

\[
 K=L(\omega),\qquad \omega^2+\omega+1=0.
\]

Using one coordinate in `O_K`, instead of two coordinates in `O_L`, changes
the effective geometric constant from `4/pi` to

\[
 \boxed{C_{\rm Eis}={2\sqrt3\over\pi}}.                 \tag{1.1}
\]

The factor `sqrt(3)` from the relative discriminant is real, but the
`2^{-m}` in the complex Minkowski covolume more than pays for it.  No factor
is lost in projection, in the divisor switch, or in the prime-power local
construction.

Inserted into the bounded-inertia rank-221 tower, this proves

\[
 \boxed{F_2(n)\ll n^{0.49371364}}.                       \tag{1.2}
\]

The improvement over `0.49371397` is small but strict.  The floating-point
threshold for the certified arithmetic data and the safe rational geometric
constant is about `0.49371362999`; the rounded theorem (1.2) is checked by
`verify_cm_eisenstein_disk_rank221.py`.

## 2. Covolume and the effective constant

Let `L` be totally real of degree `m`, let `D_L=Disc(L)^(1/m)`, and let
`K=L(omega)`.  Since `L` is totally real, `K/L` is quadratic and CM.  Choose
one complex embedding of `K` above each real embedding of `L`.  In the
unscaled embedding

\[
 \Sigma_K:O_K\longrightarrow \mathbb C^m,
\]

the lattice covolume is

\[
 \operatorname {covol}(\Sigma_K(O_K))
 =2^{-m}\sqrt{|Disc(K)|}.                               \tag{2.1}
\]

The order `O_L[omega]` has relative discriminant `-3O_L`.  The discriminant
of the maximal order divides the discriminant of this order, so

\[
 \mathfrak d_{K/L}\mid3O_L,qquad
 N_{L/\mathbb Q}(\mathfrak d_{K/L})\le3^m.              \tag{2.2}
\]

The relative discriminant formula now gives

\[
 |Disc(K)|=Disc(L)^2N(\mathfrak d_{K/L})
 \le Disc(L)^2 3^m.                                    \tag{2.3}
\]

Combining (2.1)--(2.3),

\[
 \operatorname {covol}(\Sigma_K(O_K))
 \le \left({\sqrt3\over2}D_L\right)^m.                 \tag{2.4}
\]

Let `Delta_R` be a planar disk of area `R^2`.  Averaging translates of
`Delta_R^m` over a fundamental domain of the lattice produces a translate
containing at least

\[
 {R^{2m}\over\operatorname {covol}(\Sigma_K(O_K))}
 \ge\left({2R^2\over\sqrt3D_L}\right)^m                \tag{2.5}
\]

lattice points.  Thus it suffices to take

\[
 R^2={\sqrt3\over2}D_L n^{1/m}.                         \tag{2.6}
\]

Every disk has squared diameter `4R^2/pi`.  Relative to the usual scale
`D_L n^(1/m)`, (2.6) therefore gives

\[
 {4\over\pi}{\sqrt3\over2}={2\sqrt3\over\pi},          \tag{2.7}
\]

which proves (1.1).  Equivalently, one may work in the explicit suborder
`O_L[omega]`: its covolume is exactly
`(sqrt(3)/2)^m Disc(L)`, so the same safe constant follows without using
maximal-order index savings.

## 3. Projection and total positivity

Let `tau:K -> C` be the distinguished complex embedding used for the planar
projection.  It is injective, so distinct lattice elements give distinct
planar points.  For a nonzero difference `z in O_K`, put

\[
 \eta=z\bar z=N_{K/L}(z)\in O_L.                        \tag{3.1}
\]

For every real embedding `sigma_j:L -> R`, and either complex extension
`tau_j` to `K`,

\[
 \sigma_j(\eta)=|\tau_j(z)|^2>0.                        \tag{3.2}
\]

If the two points lie in one translate of `Delta_R^m`, then

\[
 0<\sigma_j(\eta)\le {4\over\pi}R^2                   \tag{3.3}
\]

for every `j`.  Moreover the ordinary squared distance after distinguished
projection is `tau|_L(eta)`.  Equality of two projected squared distances
therefore implies equality of the corresponding elements of `L`, because
`tau|_L` is injective.  A distance-Sidon subset consequently realizes each
nonzero algebraic norm value in (3.1) by at most two ordered pairs, exactly
as in the two-coordinate real construction.

The one-sided ideal-packing lemma in `L` applies unchanged:

\[
 \#\{\eta\in\mathfrak a:
 0<\sigma_j(\eta)\le Y\ \hbox{for all }j\}
 \le\left(1+{Y\over N(\mathfrak a)^{1/m}}\right)^m.    \tag{3.4}
\]

Thus the divisor switch still takes place in the degree-`m` totally real
field.  Passing to the degree-`2m` CM field does not double its exponent.

## 4. Exact split-prime pattern and divisor switch

Let `q` be an odd prime ideal of `O_L`, unramified and split in `K/L`:

\[
 \mathfrak qO_K=\mathfrak P\bar{\mathfrak P}.           \tag{4.1}
\]

For a local depth `k` and a pattern `0<=a<=k`, define the additive lattice

\[
 I_a=\mathfrak P^a\bar{\mathfrak P}^{\,k-a}\subset O_K.
                                                                    \tag{4.2}
\]

Since both relative residue degrees are one,

\[
 [O_K:I_a]=N_L(\mathfrak q)^k.                         \tag{4.3}
\]

Taking products over all selected prime ideals and depths, every global
pattern lattice has index `N_L(M)`, and there are

\[
 H=\prod_{\mathfrak q}(k_{\mathfrak q}+1)              \tag{4.4}
\]

patterns.  Cauchy--Schwarz over its cosets therefore gives exactly the old
same-coset pair lower bound, with direct term `N_L(M)` rather than its
square.

For a fixed difference `z`, write

\[
 \alpha=v_{\mathfrak P}(z),\qquad
 \beta=v_{\bar{\mathfrak P}}(z).
\]

The admissible patterns are precisely

\[
 [k-\beta,\alpha]\cap[0,k].                             \tag{4.5}
\]

If (4.5) contains `h+1` integers, then

\[
 v_{\mathfrak q}(z\bar z)=\alpha+\beta\ge k+h.         \tag{4.6}
\]

Consequently the pattern multiplicity is bounded by the same switched
divisor count

\[
 \#\{\mathfrak b\mid\mathfrak M:
       \mathfrak M\mathfrak b\mid(\eta)\}.             \tag{4.7}
\]

Equations (4.3)--(4.7) are the ideal-theoretic version of the factorization
of the Eisenstein norm.  They show that `H`, `Lambda`, the local marginal
gains, and every orientation factor in the established master inequality
are unchanged.

In particular, with `Mcal=N(M)^(1/m)`, the exact geometric inequality is

\[
 |A|\le \mathcal M^m+\sqrt2R^m
 \left[(\Lambda/H)^{1/m}
 \left({4\over\pi}+{\mathcal M^2\over R^2}\right)
 \right]^{m/2}.                                        \tag{4.8}
\]

## 5. Normalized master inequality

Put

\[
 w={\log n\over2m},\qquad L_0=\log\mathcal M,
 \qquad G={1\over m}\log(H/\Lambda),
 \qquad c_0={\sqrt3\over2}.
\]

Using `R^2=c_0D_L exp(2w)` from (2.6), the second exponent in (4.8) is

\[
 {1\over2}+{1\over4w}\left[
 \log(C_{\rm Eis}D_L)-G+
 \log\left(1+{e^{2(L_0-w)}\over C_{\rm Eis}D_L}\right)
 \right].                                             \tag{5.1}
\]

Thus, after setting `L_0=2 alpha w`, the endpoint condition is literally

\[
 F(2\alpha w)\ge
 \log(C_{\rm Eis}D_L)+(2-4\alpha)w+
 \log\left(1+{e^{2(2\alpha-1)w}\over C_{\rm Eis}D_L}\right).
                                                               \tag{5.2}
\]

This is the existing product-disk condition with `4/pi` replaced by
`2sqrt(3)/pi`.  Concavity, dyadic layer selection, and placewise rounding
are unchanged.

## 6. Which rational primes are useful

The polynomial `X^2+X+1` splits over a finite field of odd characteristic
other than three exactly when that field contains a primitive cube root of
unity.  Let a rational prime `q != 2,3` have residue degree `f in {1,2}` in
the capped pro-2 tower.

* If `q == 1 (mod 3)`, then `q^f == 1 (mod 3)` for either value of `f`, so
  every prime over `q` splits in `K/L`.
* If `q == 2 (mod 3)`, splitting requires `f=2`.  It is enough that the
  Frobenius have nonzero Frattini class.  Adding its square relation does
  not change that class, so the Frobenius has exact order two in every
  sufficiently deep chosen layer.  Then `q^2 == 1 (mod 3)` and (4.1)
  holds.

Because only finitely many useful Frobenius elements are involved, one may
start the cofinal normal chain below an open normal subgroup avoiding all of
them.  Hence the second bullet holds simultaneously for the full useful
set.  The worst residue degree remains two, so the certified marginal item

\[
 {1\over2}\log A_k(q^{-2})                              \tag{6.1}
\]

is exactly the one already used by the rank-221 frontier.

For the first 222 odd ramified primes and their explicit 221-dimensional
positive squareclass basis, the verifier accepts a rational prime when

\[
 q\equiv1\pmod3
 \quad\hbox{or}\quad
 \operatorname {Frob}_q\ne0\ \hbox{in the Frattini quotient}. \tag{6.2}
\]

There are no rejections before the required 11,767 primes are collected;
the final useful prime remains 128,047.  Thus the relation budget, local
frontier, and real-tower root discriminant are identical to the previous
rank-221 certificate:

\[
 d=221,\quad r=12210,\quad4r=221^2-1,
 \quad\log D_L=672.4345398746246682\ldots.              \tag{6.3}
\]

## 7. Exact certificate

The verifier proves the rational inequalities

\[
 \sqrt3<{1351\over780},\qquad
 \pi>{333\over106},\qquad
 {2\sqrt3\over\pi}<{71603\over64935}.                  \tag{7.1}
\]

At

\[
 \alpha=0.49371364,qquad w_0=84891.5,                  \tag{7.2}
\]

the two dyadic endpoint margins, after subtracting `10^-25`, are

\[
 0.0034381627968\ldots,qquad
 0.0068914686254\ldots.                                 \tag{7.3}
\]

The right endpoint uses 11,767 first-depth, 4,211 second-depth, and 70
third-depth full items before its fractional item.  Its active slope is
`0.01902686499...`, strictly above the maximum omitted fourth-depth slope
`0.01536690702...`.  The inherited monotonicity lemma excludes every later
depth.

Run

```text
python3 phase2/loop/erdos1208/verify_cm_eisenstein_disk_rank221.py
```

The script reconstructs the squareclass basis, the Eisenstein useful-prime
criterion, the relation and discriminant data, the safe rational constant,
the local frontier, and both endpoint margins.

## 8. Scope

This is a genuine refinement of the current upper construction, not a route
to the conjectural exponent `1/3`.  The gain is only about `3.3e-7` in the
exponent because the geometric constant enters logarithmically and is
divided by the large optimized phase height.  Any substantial further
advance still requires a new arithmetic rank/discriminant trade or a new
global construction principle.
