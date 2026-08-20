# Independent hostile audit of the `D=11235917` quadratic-CM construction

## Verdict

The `10--12` million screen hit survives exact arithmetic and gives a new
upper-bound record.  The certified parameters are

\[
K=\mathbf Q(\sqrt{11235917}),\qquad
T=217,\qquad d=215,\qquad N=11123.
\]

The bounded-inertia Eisenstein-CM construction proves

\[
\boxed{F_2(n)\ll n^{0.49368323}}.
\]

The safe-constant continuous threshold is

\[
0.4936832199308881880151091959337007719\ldots,
\]

so the advertised decimal has genuine room.  This improves the previous
`0.49368416` record.

The independent verifier is

```bash
python3 phase2/loop/erdos1208/verify_independent_hostile_quadratic11235917_cm.py
```

It uses a certified PARI/GP BNF and direct S-unit basis, independently rebuilds
the safe sign/mod-4 kernel with integer arithmetic, tests every required CM
prime, checks the exact Golod--Shafarevich budget, repeats the endpoint at 100
and 150 digits, and performs a high-precision nearby-count rescore.

## Exact field and localization arithmetic

The fundamental discriminant factors as

\[
11235917=7\cdot11\cdot337\cdot433,
\qquad11235917\equiv5\pmod8.
\]

In the integral basis `(1,omega)`,

\[
\omega^2=\omega+2808979.
\]

PARI's certified BNF gives

\[
\operatorname{Cl}(K)\simeq C_{14}\times C_2,
\qquad
\operatorname{Cl}^+(K)\simeq C_{14}\times C_2\times C_2.
\]

For the 217 smallest odd prime ideals, the localized S-class group is trivial.
The exact S-unit squareclass basis returned by `bnfunits` therefore has

\[
217+2=219
\]

elements.  The last ramified ideal is

\[
(1063,1063,\text{split root }963).
\]

The full sign/mod-4 ray quotient has type `(C_2)^4`, and the 219 basis
columns have rank four.  Thus

\[
d=219-4=215.
\]

This exact computation is important because the discriminant has several
genus classes; no optimistic genus dimension is inserted by hand.

## Independent safe-kernel reconstruction

The verifier expands every factorized PARI S-unit to an exact algebraic
integer.  Some coordinates have more than seven thousand decimal digits.
It independently computes:

- both real-embedding signs;
- the unit square coset modulo `4 O_K` using the exact multiplication law in
  `(1,omega)`; and
- the resulting four binary constraint rows.

The independently reconstructed row space has rank four and agrees exactly
with PARI's ray-log row space.  Its nullspace has dimension 215.  Hence every
kernel squareclass is totally positive, dyadically unramified, and ramified
only at the selected odd ideals.

## Exact CM usefulness and relation budget

For candidate prime-ideal norm `Q=2 mod 3`, the verifier evaluates the exact
quadratic-residue functional on all 219 S-unit basis elements.  It accepts the
ideal precisely when that functional is nonzero on the safe kernel, checking
both a row-rank test and an explicit kernel test.  Norms `Q=1 mod 3` are
automatically useful.

The result is

\[
\boxed{11123\text{ useful ideals and }0\text{ rejections}}.
\]

The list ends at

\[
(121951,121951,\text{split root }70091).
\]

The conservative Shafarevich charge is `d+1=216`.  With 217 inertia-square
relations and 11,123 Frobenius-square relations,

\[
r\le216+217+11123=11556,
\qquad
4r=46224=215^2-1<215^2.
\]

At `x=2/215`, the exact quadratic Golod--Shafarevich polynomial is strictly
negative, proving that the resulting pro-2 quotient is infinite.

## Nearby count rescore

The all-useful thresholds for the independently rescored nearby counts are:

| `T` | `d` | `N` | threshold |
|---:|---:|---:|---:|
| 213 | 211 | 10705 | `0.4936835079472985` |
| 215 | 213 | 10913 | `0.4936833245059648` |
| 216 | 214 | 11017 | `0.4936833319835373` |
| **217** | **215** | **11123** | **`0.4936832199308882`** |
| 218 | 216 | 11228 | `0.4936833352666570` |
| 219 | 217 | 11335 | `0.4936833271161279` |
| 221 | 219 | 11549 | `0.4936835267434065` |
| 223 | 221 | 11765 | `0.4936837496375711` |

The exact winner's first 11,123 post-prefix ideals all pass the usefulness
test, so its all-useful threshold is realized rather than merely optimistic.

This table is a dense local audit, not a broad all-count theorem.  Its purpose
is to eliminate count-rounding and nearby-window false positives before
certifying the construction.

## Root discriminant and all-depth endpoint

For the winning prefix,

\[
\log\operatorname{rd}(L)
=\frac12\log11235917
 +\frac14\sum_{\mathfrak p\in T}\log N\mathfrak p
=318.9527585916460414427765165\ldots.
\]

The verifier uses the rigorous adverse bound

\[
\frac{2\sqrt3}{\pi}<\frac{71603}{64935}.
\]

The equal-threshold anchor is

\[
w_*=39928.00429278135001166535408\ldots.
\]

At the safe exponent `0.49368323`, the two endpoint margins evaluated at this
anchor are

```text
0.0016328170368155722502190593...
0.0032470752120377069950298337...
```

The corresponding anchor derivatives have signs

```text
+0.00501271449326...
-0.0127638686643...
```

and the active frontier slopes are

```text
0.03066723017233...
0.01912678466700....
```

The maximum omitted local slope is

```text
0.0099999734338455...,
```

strictly below both active slopes.  Thus no deeper local role is missing.
The complete calculation agrees at 100 and 150 decimal digits.

## Scope

This certifies the displayed norm-prefix, all-square construction and the
new exponent `0.49368323`.  It does not claim fixed-field optimality over
arbitrary nonprefix ramification assignments, mixed inertia orders, all
ramified counts, or other base fields.  Those are robustness questions for
separate structural and broad-count locks; they are not needed for the stated
upper bound.
