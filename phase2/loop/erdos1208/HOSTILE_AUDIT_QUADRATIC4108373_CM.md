# Hostile audit of the quadratic-4108373 CM record

## 1. Verdict

The record survives a fully independent reconstruction.  In the
bounded-inertia Eisenstein-CM construction, take

\[
 E=\mathbb Q(\sqrt{4108373}),\qquad
 T=217,qquad d=215,qquad N=11123.                  \tag{1.1}
\]

The resulting certified upper bound is

\[
 \boxed{F_2(n)\ll n^{0.49368647}}.                   \tag{1.2}
\]

With the safe rational geometric constant, the optimized continuous
threshold is

```text
0.493686459809675808859062866082...
```

The hostile verifier is

```text
python3 phase2/loop/erdos1208/verify_hostile_quadratic4108373_cm.py
```

It uses PARI/GP only for certified BNF and exact principal-generator data.
Python independently reconstructs the safe Kummer kernel, performs the full
CM useful-prime scan, checks the relation budget and root discriminant, and
recomputes the all-depth endpoint at 100 and 150 digits.

## 2. Exact field and S-unit basis

The fundamental discriminant is

\[
 4108373=17\cdot67\cdot3607,qquad4108373\equiv5\pmod8. \tag{2.1}
\]

Writing

\[
 \omega={1+\sqrt{4108373}\over2},\qquad
 \omega^2=\omega+1027093,                            \tag{2.2}
\]

PARI's certified BNF gives

\[
 \operatorname {Cl}(E)\simeq C_2,qquad
 \operatorname {Cl}^+(E)\simeq(C_2)^2.              \tag{2.3}
\]

Order odd prime ideals by norm, retaining both ideals over a split rational
prime.  The first 217 kill the ordinary class group and end at

\[
 (1117,1117,\text{split root }1020).                 \tag{2.4}
\]

The second ideal in norm order,

\[
 R=(11,11,\text{split root }4),                      \tag{2.5}
\]

is nonprincipal and generates `Cl(E)=C_2`.

The verifier constructs the 219 independent S-unit squareclasses directly:

1. the two global unit squareclasses;
2. a generator of `R^2`;
3. a generator of every principal selected ideal `P`; and
4. a generator of `PR` for every other nonprincipal selected ideal `P`.

Their valuation vectors, together with the class-torsion generator from
`R^2`, prove independence through the exact Kummer sequence.  This avoids
depending on a reduced black-box S-unit basis.

## 3. Independent local-kernel audit

For modulus `(4 O_E; both real places)`, PARI gives local quotient `(C_2)^4`
and image rank four.  The verifier separately reconstructs

- both real-embedding signs by exact integer comparisons; and
- all unit-square cosets in `O_E/4 O_E` using the multiplication law in the
  integral basis `(1,omega)`.

The independent four-row space agrees exactly with PARI's row space.  The
verifier then constructs an explicit nullspace basis of dimension

\[
 219-4=215.                                          \tag{3.1}
\]

Thus every retained class is totally positive and square modulo four.  The
corresponding elementary quadratic extension is totally real, dyadically
unramified, and ramified only at the selected 217 odd ideals.

## 4. CM usefulness and Golod--Shafarevich budget

At an outside ideal of norm `Q=2 mod 3`, the verifier evaluates the exact
quadratic-residue functional on all 219 basis elements.  It checks usefulness
in two equivalent ways: the functional must raise the four-row rank, and it
must have nonzero dot product with the explicit safe-kernel basis.  Norms
`Q=1 mod 3` are automatically CM-useful.

The exact result is

\[
 \boxed{11123\text{ useful ideals and }0\text{ rejections}}, \tag{4.1}
\]

with last useful ideal

\[
 (121367,121367,\text{split root }69978).             \tag{4.2}
\]

The safe real-quadratic Shafarevich charge is `d+1=216`.  Adding one
inertia-square relation per member of `T` and one Frobenius-square relation
per useful ideal gives

\[
 r\le216+217+11123=11556,
 \qquad4r=46224=215^2-1<215^2.                       \tag{4.3}
\]

The strict quadratic Golod--Shafarevich inequality therefore proves an
infinite quotient.

## 5. Root discriminant and endpoint

The exact prime-ideal prefix gives

\[
 \log D_L={1\over2}\log4108373
 +{1\over4}\sum_{\mathfrak p\in T}\log N\mathfrak p
 =317.6510581919590472759259853116048\ldots .         \tag{5.1}
\]

The verifier uses the rigorous geometric upper bound

\[
 {2\sqrt3\over\pi}<{71603\over64935}                \tag{5.2}
\]

and the complete active local frontier

\[
 c(Q)={\log Q\over2},\qquad
 g_j(Q)={1\over4}\log A_j(Q^{-2}).                   \tag{5.3}
\]

The equal-endpoint anchor is

```text
39963.8976671829913854190301638...
```

At the advertised exponent `0.49368647`, the two endpoint margins are

```text
0.0016539510883490886500713317251...
0.0032890914979972110365601016208...
```

at both 100 and 150 digits.  Their active slopes are

```text
0.03065819246627363055528920230...
0.01911067480415899490699020243...
```

while the largest omitted slope is only
`0.00999981994839345639249736015...`.  Hence no deeper local role is active.
The scale-one derivative is positive and the scale-two derivative is
negative.  The fixed-anchor roots are bracketed at

```text
0.4936864598096758088590630059200...
0.4936864598096758088590604643483...
```

both strictly below the advertised exponent.

## 6. Scope

This hostile audit certifies the displayed norm-prefix construction and the
new upper exponent.  It does not assert optimality over nonprefix assignments,
mixed inertia orders, other fields, or other pro-2 presentations.  Every
class, kernel, CM, relation-count, root-discriminant, and endpoint gate needed
for the record has been independently rechecked.
