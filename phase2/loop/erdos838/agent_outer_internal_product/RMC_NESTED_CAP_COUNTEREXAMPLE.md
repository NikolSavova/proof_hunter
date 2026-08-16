# Radial multiplicity capture fails on two vertically separated caps

**Date:** 2026-08-15  
**Verdict:** the pointwise radial multiplicity statement `RMC(C,b)` is
false for every pair of absolute constants `C,b`.  The counterexample is a
rational planar point configuration in general position, and the violating
face can have rank four.  Thus neither a larger constant than `8` nor a
fixed polynomial loss repairs the conjecture.

This does **not** disprove the averaged activity-weighted tangent-pocket
target in
`../agent_kl_radial_high_tail/KL_RADIAL_BUCKET_REDUCTION.md`.  The bad face
below has exponentially small half-Gibbs mass.  What it proves is that the
pointwise bucket-to-capture comparison cannot be the route to that averaged
target.

All logarithms are base two.  A finite set is called a face when all of its
points are vertices of its convex hull.

## 1. The rational configuration

Fix `m>=3`.  Put six high points

\[
 u_{-a}=(-a,-a^2),\qquad u_a=(a,-a^2)
 \quad(a\in\{2,4,6\})                                      \tag{1}
\]

and put `m` low points

\[
 x_i=-1+{2i\over m+1},\qquad
 w_i=(x_i,-100-x_i^2)\quad(1\le i\le m).                  \tag{2}
\]

Let

\[
 P_m=\{u_{-6},u_{-4},u_{-2},w_1,\ldots,w_m,
                         u_2,u_4,u_6\}                    \tag{3}
\]

in increasing `x`-order, and let

\[
                   U=\{u_{-6},u_{-4},u_{-2},u_2,u_4,u_6\}.
                                                                    \tag{4}
\]

Both `U` and `W={w_1,...,w_m}` lie on strictly concave parabolas, so they
are convex faces and every subset of `W` is a face.  The whole configuration
is in general position.  Three points on either parabola are never
collinear.  If two high abscissae are `a,b` and one low abscissa is `x`,
collinearity would give

\[
                     100=-(x-a)(x-b),                     \tag{5}
\]

while one high abscissa `a` and two low abscissae `x,y`
would give

\[
                     100=(a-x)(a-y).                      \tag{6}
\]

Both right sides have absolute value less than `49`.  Thus (5)--(6) are
impossible.  In particular this is a stretchable, rational, general-position
family rather than an abstract four-local complex.

## 2. Symmetric warm-up: one low cap is charged at three peels

The three canonical endpoint pairs of `U` are

\[
             e_a=\{u_{-a},u_a\},\qquad a=6,4,2.           \tag{7}
\]

Every open `x`-interval of (7) contains all of `W`.  The chord of `e_a` is
the horizontal line `y=-a^2`, strictly above `W`.

> **Lemma 1 (two-low-point cap).**  If a trace `T` satisfies
> `e_a union T` convex, then `|T intersection W|<=2`.

**Proof.**  Suppose the trace contains three low points
`w_i,w_j,w_k` with `i<j<k`.  Strict concavity puts `w_j` strictly above the
chord `w_iw_k`.  It is strictly below the horizontal chord of `e_a`.
Because `x_i<x_j<x_k` and `-a<x_i<x_k<a`, the point `w_j` is in the
interior of the quadrilateral

\[
                    \operatorname{conv}(e_a\cup\{w_i,w_k\}).
\]

It is therefore non-extreme already in this four-point subhull and remains
non-extreme after the other trace points are added.  This contradicts
convexity.  QED.

Let `F_I(1/2)` be the half-weighted face polynomial of the open interval of
an endpoint pair, and let `Z_a` be the half-weight of the traces compatible
with `e_a`.  Every interval contains the full Boolean face family on `W`,
so

\[
                         F_I(1/2)\ge(3/2)^m.              \tag{8}
\]

The intervals for `a=6,4,2` contain respectively `h_a=4,2,0` other high
labels.  Lemma 1 therefore gives

\[
\begin{aligned}
 Z_a
 &\le (3/2)^{h_a} A_m,\\
 A_m
 &:=\sum_{j=0}^2 {\binom mj\over2^j}
   =1+{m\over2}+{m(m-1)\over8}.                          \tag{9}
\end{aligned}
\]

The canonical capture factor is `lambda_a=Z_a/F_I(1/2)`.  Hence the
three-peel product of (4) obeys

\[
 L(U)=\lambda_6\lambda_4\lambda_2
 \le {(3/2)^6A_m^3\over(3/2)^{3m}}.                      \tag{10}
\]

This is the key synchronization.  The same Boolean reservoir is visible in
all three nested denominators, while the high horizontal chord hides all but
two of its labels in every compatible numerator.

The symmetric face already disproves every `RMC(C,b)`, as the first version
of this note recorded.  There is, however, a stronger asymmetric rank-four
face.  We use that form for the final theorem.

## 3. The asymmetric rank-four kill

Put

\[
             V_m=\{u_{-4},u_{-2},w_{m-1},w_m\}.           \tag{10a}
\]

Its two canonical endpoint pairs are

\[
 f_0=\{u_{-4},w_m\},\qquad
 f_1=\{u_{-2},w_{m-1}\}.                                 \tag{10b}
\]

The open interval of `f_0` contains `u_-2` and
`w_1,...,w_(m-1)`; that of `f_1` contains
`w_1,...,w_(m-2)`.

> **Lemma 2 (one-prefix-point cap).**  A trace compatible with `f_0`
> contains at most one of `w_1,...,w_(m-1)`.  A trace compatible with `f_1`
> contains at most one of `w_1,...,w_(m-2)`.

**Proof.**  Consider an endpoint pair `f={u_a,w_k}` of either type and
suppose its trace contains `w_i,w_j` with `i<j<k`.  The chord `u_aw_k` lies
strictly above every intervening low point.  One exact way to see this is
to compare it with the low parabola.  At an abscissa `x in (a,x_k)`, the
vertical gap between the chord and `y=-100-x^2` is

\[
 (x_k-x)\left({100\over x_k-a}-(x-a)\right)>0,            \tag{10c}
\]

because `x_k-a<5` and `x-a<5`.  Strict concavity puts `w_j` above the chord
`w_iw_k`.  Hence `w_j` lies in the interior of the triangle
`conv{u_a,w_i,w_k}` and is non-extreme.  QED.

Put

\[
                         B_t=1+{t\over2}.                 \tag{10d}
\]

The optional high point in the first interval and Lemma 2 give compatible
trace half-weights

\[
 Z(f_0)\le(3/2)B_{m-1},\qquad Z(f_1)\le B_{m-2}.          \tag{10e}
\]

The full interval denominators contain the Boolean low prefixes, so

\[
 F_{I(f_0)}(1/2)\ge(3/2)^{m-1},\qquad
 F_{I(f_1)}(1/2)\ge(3/2)^{m-2}.                           \tag{10f}
\]

Consequently the rank-four capture product satisfies

\[
 L(V_m)\le {B_{m-1}B_{m-2}\over(3/2)^{2m-4}}.            \tag{10g}
\]

Write `F_{P_m}=F(P_m;1/2)`.  The universal Boolean upper bound is

\[
                         F_{P_m}\le(3/2)^{m+6}.           \tag{11}
\]

The terminal bucket of `V_m` is `(4,empty)` and contains `V_m` itself.
Thus

\[
 \pi(B(V_m))\ge\pi(V_m)={2^{-4}\over F_{P_m}}
              \ge 2^{-4}(3/2)^{-(m+6)}.                  \tag{12}
\]

Combining (10g) and (12) gives

\[
 \boxed{
 {\pi(B(V_m))\over L(V_m)}
 \ge {1\over16}{(3/2)^{m-10}\over B_{m-1}B_{m-2}}.}     \tag{13}
\]

The right side is `Omega((3/2)^m/m^2)`.  For any fixed `C>0` and fixed real
`b`, it eventually exceeds

\[
                         C^{|V_m|}|P_m|^b=C^4(m+6)^b.     \tag{14}
\]

Consequently

\[
                    \pi(B(V_m))>C^{|V_m|}|P_m|^bL(V_m), \tag{15}
\]

which is the negation of `RMC(C,b)`.

The definition-only bound (13) first certifies `RMC(8,0)` failure at
`m=54` (`n=60`).  Exact matrix evaluation is substantially sharper:
already at `m=21` (`n=27`) the face (10a) has

\[
 \log {\pi(B(V_m))\over L(V_m)}=12.148992\ldots,
 \qquad
 \left({\pi(B(V_m))\over L(V_m)}\right)^{1/4}
 =8.209236\ldots>8.                                      \tag{15a}
\]

At `m=22` the per-vertex constant is `9.314447...`.

> **Theorem 3 (pointwise RMC is false).**  There are no absolute constants
> `C,b` for which radial multiplicity capture holds for all planar affine
> convex geometries.  This already fails on rank-four faces.

The earlier symmetric calculation remains useful as a transparent
three-charge model.  For completeness, its quotient satisfies

\[
 {\pi(B(U))\over L(U)}
 \ge {1\over64}{(3/2)^{2m-12}\over A_m^3}
 =\Omega((9/4)^m/m^6).                                   \tag{15b}
\]

Notice that radial multiplicity is not needed for either lower bound:
(12) uses only the selected bucket member.  The failure is repeated
conditioning on nested copies of the same large interval reservoir.

## 4. What this says about the first-failure geometry

The first-crossing criterion (18) in the radial-bucket report remains exact,
but a proof cannot hope to discharge it pointwise.  In this family the
three selected parents are nested tangent parents around a common low cap.
Planarity does not force successive endpoint chords to expose complementary
sides of the reservoir.  The asymmetric rank-four face (10a) follows the
same tangent direction twice through two nested low prefixes.  Each selected
low endpoint supplies the third point that hides all but one earlier prefix
point.  Thus even two peels can overpay one Boolean reservoir after the
global normalizer has paid it once.

The construction survives all requested regressions:

* **singleton-reset/projective universality:** no regularity of the low cap
  is used beyond strict concavity.  Arbitrary small rational perturbations
  preserve the witness, so a projectively encoded child cannot repair a
  pointwise theorem;
* **alternating family:** its uniform lower bound on every capture factor is
  a special one-sided-history property.  Our separated double cap has
  `lambda_a=O(m^2(3/2)^{-m})`, so that calculation does not extend;
* **n58 and Pascal:** those are valid finite audits of different order
  types.  The first exact failure here has only `27` points, so finite
  success on those particular order types was not universal; and
* **common cages:** the low cap is precisely a common cage shared by three
  nested parents.  Its unrestricted bank has only one global copy, whereas
  the pointwise capture product places the same partition function in three
  denominators.

The averaged activity-weighted target can still survive.  Since
`F_{P_m}>=(3/2)^m`, the particular bad face has probability at most the
scale `(3/2)^{-m}` up to a constant, while its capture cost is only `O(m)`.
Thus its direct
contribution to the KL expectation is exponentially small.  Any successful
replacement for RMC must aggregate parent activity before charging a common
cage, as in (23f2)--(23f8) of the radial-bucket report.

## 5. Verification

Run

```bash
python3 \
  phase2/loop/erdos838/agent_outer_internal_product/verify_rmc_nested_cap_counterexample.py
```

The verifier uses exact rational arithmetic.  It checks general position,
the convexity of both caps, every quadrilateral/triangle witness in Lemmas
1--2, the asymptotic bounds (13) and (15b), and the exact `m=21,22`
violations of `RMC(8,0)`.  A separate exhaustive `m=8` audit enumerates every subset and
reconstructs the interval denominators, compatible-trace numerators,
terminal bucket probability, and all normalization factors from their
definitions.  The verifier writes
`rmc_nested_cap_counterexample_certificate.json`.
