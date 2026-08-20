# The quadratic-1949 tower with CM/Eisenstein packing

## 1. Result

The CM/Eisenstein one-coordinate refinement combines cleanly with the
certified bounded-inertia tower over

\[
 E=\mathbb Q(\sqrt{1949}).
\]

The combined construction proves the strict new upper bound

\[
 \boxed{F_2(n)\ll n^{0.49371148}}.                       \tag{1.1}
\]

This improves the quadratic-base product-disk exponent `0.49371211`.  The
optimized continuous threshold for the certified 227-ideal data is
approximately

\[
 \alpha_*=0.49371147915679,\qquad w_*=43932.44289,       \tag{1.2}
\]

and the exact certificate uses the safely rounded values

\[
 \alpha=0.49371148,\qquad w_0=43932.44.                 \tag{1.3}
\]

Run `verify_cm_eisenstein_real_quadratic_1949.py` for the canonical finite
certificate.  The independently written
`verify_quadratic1949_cm_eisenstein.py` checks the neighboring 229-ideal
configuration and the ramified-base-ideal edge case.

## 2. Arithmetic tower retained from the quadratic record

Write

\[
 \varpi={1+\sqrt{1949}\over2},\qquad
 O_E=\mathbb Z[\varpi].
\]

The field has discriminant 1,949, class number one, a norm-minus-one unit

\[
 \epsilon=81333+3770\varpi,
\]

and two independent unit signatures.  Let `T` be the first 227 odd prime
ideals in the exact norm/tie ordering of the verifier.  Its last ideal has
norm 1,297.

The `T`-supported squareclass space has 229 explicit generators: `-1`,
`epsilon`, and one principal generator for every ideal in `T`.  Two real
signature constraints and two square-modulo-4 constraints have exact rank
four.  Their kernel therefore has dimension

\[
 229-4=225.                                             \tag{2.1}
\]

It is an explicit Kummer subspace of totally positive classes whose
quadratic extensions are unramified at the dyadic prime.  Thus the maximal
totally real pro-2 group unramified outside `T` has generator rank at least
225.  The conservative Shafarevich relation bound is `r_0<=226`.

Square-capping inertia at all 227 ideals and Frobenius at 12,203 useful
ideals gives

\[
 r\le226+227+12203=12656,\qquad
 4r=225^2-1.                                           \tag{2.2}
\]

The quotient is therefore infinite.  The bounded-inertia real-tower root
discriminant is

\[
 D_L=\sqrt{1949}\prod_{\mathfrak p\in T}
          N_E(\mathfrak p)^{1/4},                      \tag{2.3}
\]

with

\[
 \log D_L=342.3225986272674925544177328313\ldots.      \tag{2.4}
\]

Here `L/E` denotes a finite totally real layer and
`m=[L:Q]` its absolute degree.

## 3. CM compositum and discriminant audit

For every layer put

\[
 K=L(\zeta_3),\qquad \zeta_3^2+\zeta_3+1=0.            \tag{3.1}
\]

Since `L` is totally real, `zeta_3` is not in `L`, so `[K:L]=2` and `K` is
CM with real subfield `L`.  The possible overlap of ramification above 3
causes no loss.  The order `O_L[zeta_3]` has relative discriminant
`-3O_L`, hence the maximal-order relative discriminant satisfies

\[
 \mathfrak d_{K/L}\mid3O_L,\qquad
 N_{L/\mathbb Q}(\mathfrak d_{K/L})\le3^m.             \tag{3.2}
\]

The absolute discriminant formula gives

\[
 |Disc(K)|=Disc(L)^2N(\mathfrak d_{K/L})
 \le Disc(L)^2 3^m.                                    \tag{3.3}
\]

In the unscaled complex Minkowski embedding

\[
 O_K\hookrightarrow\mathbb C^m,
\]

the covolume is `2^{-m}sqrt(|Disc(K)|)`.  Therefore

\[
 \operatorname {covol}(O_K)\le
 \left({\sqrt3\over2}D_L\right)^m.                    \tag{3.4}
\]

This verifies both the relative-discriminant and complex-covolume factors.
Using the possibly larger maximal order can only improve the point count;
equivalently the explicit suborder `O_L[zeta_3]` has exactly the right-hand
side of (3.4) as covolume.

Let `Delta_R` be a planar disk of area `R^2`.  Averaging translates of
`Delta_R^m` gives at least `n` points once

\[
 R^2={\sqrt3\over2}D_L n^{1/m}.                         \tag{3.5}
\]

The squared diameter in each complex coordinate is `4R^2/pi`.  Thus the
effective constant relative to `D_L n^(1/m)` is

\[
 C_{\rm Eis}={4\over\pi}{\sqrt3\over2}
 ={2\sqrt3\over\pi}.                                   \tag{3.6}
\]

No extra `sqrt(3)` should be placed into (2.3): it has already been combined
with the complex `2^{-m}` covolume in (3.6).

## 4. Projection and the norm divisor switch

Choose one complex embedding `tau:K -> C` for the planar projection.  It is
injective.  If `z` is the difference of two ambient lattice elements, set

\[
 \eta=z\bar z=N_{K/L}(z)\in O_L.                       \tag{4.1}
\]

For every real embedding `sigma:L -> R`,

\[
 \sigma(\eta)=|\tau_\sigma(z)|^2>0,                   \tag{4.2}
\]

and (3.5) gives `sigma(eta)<=4R^2/pi`.  Equality of two
distinguished planar squared distances implies equality of the associated
elements `eta`, since `tau|_L` is injective.  Hence a distance-Sidon subset
realizes every nonzero `eta` by at most two ordered pairs.

At a prime `Q` of `L` which splits in `K/L`, write

\[
 \mathfrak QO_K=\mathfrak P\bar{\mathfrak P}.
\]

For depth `k`, the `k+1` pattern ideals

\[
 I_a=\mathfrak P^a\bar{\mathfrak P}^{\,k-a},
 \qquad0\le a\le k,                                   \tag{4.3}
\]

all have additive index `N_L(Q)^k`.  If
`alpha=v_P(z)` and `beta=v_Pbar(z)`, the admissible `a` form

\[
 [k-\beta,\alpha]\cap[0,k].                            \tag{4.4}
\]

Having `h+1` choices forces

\[
 v_{\mathfrak Q}(z\bar z)=\alpha+\beta\ge k+h.        \tag{4.5}
\]

Thus the pattern index, same-coset lower bound, multiplicity, and switched
divisor count are exactly those of the established two-real-coordinate
construction.  In particular, with `Mcal=N(M)^(1/m)`, `H` the pattern
count, and `Lambda` the divisor sum,

\[
 |A|\le\mathcal M^m+\sqrt2R^m
 \left[(\Lambda/H)^{1/m}
 \left({4\over\pi}+{\mathcal M^2\over R^2}\right)
 \right]^{m/2}.                                        \tag{4.6}
\]

## 5. Exact mod-3 useful-prime criterion

Let `q` be a prime ideal of `E` outside `T`, of norm `Q`, and let `f` be its
relative residue degree in a capped layer `L/E`.  The Frobenius-square
relation gives `f in {1,2}`.  A prime of `L` over `q` splits in the
Eisenstein compositum exactly when its residue field contains a primitive
cube root, equivalently

\[
 Q^f\equiv1\pmod3.                                     \tag{5.1}
\]

Therefore:

* `Q == 1 (mod 3)` is automatically useful;
* `Q == 2 (mod 3)` is useful precisely when the capped Frobenius is forced
  to have exact order two.

The second condition is tested on the exact 225-dimensional Kummer kernel.
Let `C` be the four-row sign/dyadic constraint matrix on the 229 explicit
generators, and let `lambda_q` be the quadratic residue functional at `q`.
Its restriction to `ker(C)` is nonzero exactly when

\[
 \operatorname {rank}\binom C{\lambda_{\mathfrak q}}>4. \tag{5.2}
\]

All square and inertia relators lie in the Frattini subgroup, so a nonzero
class in (5.2) survives.  After the Frobenius square cap it consequently has
exact order two.  A cofinal normal chain can be chosen below an open normal
subgroup avoiding the finitely many selected Frobenius elements, making
this simultaneous at every sufficiently deep layer.

The scan has zero rejections before 12,203 ideals are selected.  One
nontrivial edge case is essential: the unique ideal of `E` above the
rational prime 1,949 is ramified in `E/Q`, lies outside `T`, has norm
`1949 == 2 (mod 3)`, and occurs as useful ideal number 79.  It is unramified
in the relative pro-2 tower, so its Frobenius is defined.  Modulo that ideal,

\[
 \varpi={1+\sqrt{1949}\over2}\longmapsto {1\over2}.    \tag{5.3}
\]

The verifier evaluates all 229 Kummer generators at this residue root and
checks (5.2); the functional is nonzero on the kernel.  Omitting this ideal
or treating it as an ordinary split rational prime would leave a real gap
in the useful-prefix certificate.

The last selected useful ideal has norm 134,129.  For a full orbit of
an ideal of norm `Q`, exact absolute-degree normalization gives the marginal
cost and guaranteed gain

\[
 c_{\mathfrak q,k}={\log Q\over2},\qquad
 g_{\mathfrak q,k}={1\over4}\log A_k(Q^{-2}).           \tag{5.4}
\]

Indeed a relative residue degree `f` orbit contains `[L:E]/f` primes of
norm `Q^f`; division by `[L:Q]=2[L:E]` gives cost `(log Q)/2` and gain
`(1/(2f))log A_k(Q^{-f})`, whose uniform lower value occurs at `f=2`.
There is no prime-ideal multiplicity amplification.

## 6. Master inequality and exact endpoint certificate

Put

\[
 w={\log n\over2m},\qquad L_0=\log\mathcal M,
 \qquad G={1\over m}\log(H/\Lambda).
\]

Substituting (3.5) into (4.6), setting `L_0=2 alpha w`, and using
`C_Eis=2sqrt(3)/pi` gives the endpoint condition

\[
 F(2\alpha w)\ge
 \log(C_{\rm Eis}D_L)+(2-4\alpha)w+
 \log\left(1+{e^{2(2\alpha-1)w}\over C_{\rm Eis}D_L}\right).
                                                               \tag{6.1}
\]

The verifier uses the exact rational upper bound

\[
 \sqrt3<{1351\over780},\qquad
 \pi>{333\over106},\qquad
 C_{\rm Eis}<{71603\over64935}.                        \tag{6.2}
\]

At the certified values (1.3), the dyadic endpoint margins, after
subtracting `10^-25`, are

\[
 0.0001363825807\ldots,\qquad
 0.0003361149849\ldots.                                \tag{6.3}
\]

At the right endpoint, the active slope is
`0.0189913278335...`, above the maximum omitted fourth-depth slope
`0.0155656732466...`.  The inherited marginal monotonicity excludes all
deeper items.  Concavity on `[w_0,2w_0]`, dyadic layer selection, and
placewise rounding prove (1.1).

Run

```text
python3 phase2/loop/erdos1208/verify_cm_eisenstein_real_quadratic_1949.py
```

The verifier reconstructs the field arithmetic, 229 Kummer columns and
four constraints, every mod-3 Frobenius functional including the ramified
base ideal, the relation and root-discriminant budgets, the rational CM
constant, the complete active frontier, and both endpoint margins.

The independently written
`verify_quadratic1949_cm_eisenstein.py` reconstructs the neighboring
229-ideal prime list and all-depth frontier at a different safe anchor and
gives a second finite check of the combined mechanism.

## 7. Scope

The compositum and order issues introduce no hidden loss, and the bound is
a rigorous new record inside the current construction family.  Its
improvement over `0.49371211` is about `6.2e-7`; it does not materially
reduce the remaining gap to the conjectural cube-root exponent.  A major
advance still requires a qualitatively stronger arithmetic trade or a new
global construction.
