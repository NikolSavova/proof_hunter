# Critical height for arbitrary Gaussian-ideal coset patches

## 1. Result

The prime-norm restriction in `GAUSSIAN_PRIME_COSET_HEIGHT.md` is not
essential.  Reducing the translate to its true rational denominator and
doubling a primitive pair of coordinate gaps removes both the composite-
modulus and parity obstructions.

### Theorem 1.1

There are absolute constants `c>0` and `r_0` with the following property.
Let `z` be a nonzero Gaussian integer, let

\[
 t\in\mathbb Z[i]\setminus z\mathbb Z[i],
\]

and put

\[
 \mathcal G=\{t+z(a+ib):0\le a,b<r\}.           \tag{1.1}
\]

If `r>=r_0`, `mathcal G subset [-M,M]^2`, and no two distinct
non-antipodal points of `mathcal G` have the same norm, then

\[
 \boxed{M\ge c r^{3/2}}.                         \tag{1.2}
\]

Consequently every balanced coset patch of an arbitrary exact
quarter-turn-stable lattice in a radially unique complete difference set
satisfies

\[
 \boxed{|\mathcal G|=r^2\ll M^{4/3}}.            \tag{1.3}
\]

This closes the exact Gaussian-ideal patch branch at the cube-root-critical
local exponent.  The later modular-midpoint theorem in
`OBLIQUE_LATTICE_GAUSSIAN_CORE.md` closes all complete exact integral
oblique patches at the same exponent.  Neither result extracts such a patch
from a general rich fibre, controls approximate modules, or proves the
aggregate seven-incidence bound.

## 2. Composite-denominator shifted-square lemma

### Lemma 2.1

Let `h>=2` and let `p,s` be integers satisfying

\[
 \gcd(p,s,h)=1.
\]

Suppose

\[
 U={p\over h},\qquad V={s\over h},\qquad
 0\le U\le V.                                   \tag{2.1}
\]

For an integer `R`, define

\[
 A=2U+R-1,\qquad B=2V+R-1,
 \qquad \alpha={B\over A}\ge1.                 \tag{2.2}
\]

There is an absolute `R_0` such that, if `R>=R_0` and

\[
 {hB\over R^2}\le10^{-8},                       \tag{2.3}
\]

then the rational patch

\[
 \{(U+a,V+b):0\le a,b<R\}                       \tag{2.4}
\]

contains two distinct points of equal norm.

### Proof

Put

\[
 a_0=\gcd(p,h),\qquad b_0={h\over a_0}.
\]

Then `p/a_0` is invertible modulo `b_0`, and `s` is coprime to
`a_0`.  Set

\[
 X={R\over128\alpha a_0}.
\]

Since `A>=R-1`, condition (2.3) gives

\[
 X\ge {b_0\over256\cdot10^{-8}}                 \tag{2.5}
\]

for large `R`.  Bertrand's postulate therefore supplies an odd prime `E`
with

\[
 X\le E\le4X,
 \qquad E>b_0.                                  \tag{2.6}
\]

Define the primitive second gap

\[
 e_0=a_0E.                                      \tag{2.7}
\]

The congruence

\[
 p d_0\equiv s e_0\pmod h                       \tag{2.8}
\]

reduces to the single residue class

\[
 d_0\equiv sE(p/a_0)^{-1}\pmod {b_0}.           \tag{2.9}
\]

We can choose a representative near `alpha e_0` which is coprime to
`e_0`.  Here is the exact elementary argument.  Let

\[
 c_0=\prod_{\substack{\ell\mid a_0\\ \ell\nmid b_0}}\ell,
 \qquad m=b_0c_0\le h,                          \tag{2.10}
\]

where the product is over distinct rational primes.  Add the compatible
conditions `d_0=1 (mod ell)` for the primes in `c_0`.  The resulting
solutions form one residue class modulo `m`.  They are automatically
coprime to `a_0`: at primes common to `a_0` and `b_0`, (2.9) is a unit,
while (2.10) handles the remaining primes.

Choose a member of this class nearest `alpha e_0`.  If it is divisible by
`E`, take an adjacent member.  When `E` divides `m`, it must divide `c_0`
because `E>b_0`, and the condition `d_0=1 (mod E)` already prevents this.
Otherwise adjacent members cannot both be divisible by `E`.  Thus one can
arrange

\[
 \gcd(d_0,e_0)=1,
 \qquad |d_0-\alpha e_0|\le2h.                 \tag{2.11}
\]

Now double both primitive gaps:

\[
 d=2d_0,qquad e=2e_0.                          \tag{2.12}
\]

This doubling is what makes the argument uniform for even `h`.  Equations
(2.6), (2.7), (2.11), and (2.3) imply

\[
 {R\over80}<d<{R\over12},
 \qquad {R\over64\alpha}\le e\le{R\over16\alpha},
 \qquad |d-\alpha e|\le4h.                    \tag{2.13}
\]

Multiply squared norms in (2.4) by `h`.  First-coordinate differences at
gap `d` form the progression

\[
 \mathcal F_d=
 \{d(2p+hd+2hj):0\le j\le R-1-d\},             \tag{2.14}
\]

whose centre and half-width are

\[
 hdA,\qquad hd(R-1-d).                          \tag{2.15}
\]

The corresponding second-coordinate quantities are

\[
 heB,\qquad he(R-1-e).                          \tag{2.16}
\]

The centres differ by at most

\[
 hA|d-\alpha e|\le4h^2A.                       \tag{2.17}
\]

Using (2.3) and (2.13), this is less than one thousandth of the
smaller half-width.  Hence the two underlying intervals overlap by much
more than

\[
 hde.                                           \tag{2.18}
\]

Their residue classes are compatible.  Indeed, `gcd(d_0,e_0)=1` gives

\[
 \gcd(2hd,2he)=4h,                              \tag{2.19}
\]

and the difference of the two residues is

\[
\begin{aligned}
 d(2p+hd)-e(2s+he)
 &=4\{pd_0-se_0+h(d_0^2-e_0^2)\},
\end{aligned}                                   \tag{2.20}
\]

which is divisible by `4h` by (2.8).  Their common CRT period is therefore

\[
 \operatorname{lcm}(2hd,2he)=hde.              \tag{2.21}
\]

The interval overlap contains a common term.  For suitable admissible
indices `j,k`,

\[
 (U+j+d)^2+(V+k)^2
 =(U+j)^2+(V+k+e)^2.                            \tag{2.22}
\]

The two points are distinct, proving the lemma.

## 3. Proof of Theorem 1.1

Write `z=x+iy`, `q=|z|^2`, and identify `t` with its vector in
`Z^2`.  Division by `z` turns (1.1) into a translated unit grid.  Its
translation coordinates are

\[
 {t\over z}=U+iV,
 \qquad U={P\over q},\quad V={Q\over q},        \tag{3.1}
\]

where

\[
 P=t\mathbin\cdot z,qquad Q=t\mathbin\cdot iz.
\]

Let

\[
 g=\gcd(P,Q,q),\qquad h={q\over g},
 \qquad p={P\over g},\quad s={Q\over g}.       \tag{3.2}
\]

Then `gcd(p,s,h)=1`.  Moreover `h>=2`: if `h=1`, both coordinates in
(3.1) are integers, which says exactly that `t in zZ[i]`.

The diameter of (1.1) gives

\[
 M\gg r\sqrt q.                                 \tag{3.3}
\]

Thus (1.2) follows when `q>=eta r`, for any sufficiently small fixed
absolute `eta>0`.

Suppose instead that `q<eta r`.  In each normalized coordinate, at least
half of the `r` consecutive values lie on one side of zero.  Restricting in
both coordinates leaves a consecutive square subpatch of side `R>=r/2`.
Reflect, interchange, and reindex its coordinates so that its translation
obeys `0<=U<=V`.  These operations preserve the reduced denominator and
norms.

Every normalized point has modulus at most `sqrt(2)M/sqrt(q)`, so the
quantity `B` in Lemma 2.1 satisfies

\[
 B\ll {M\over\sqrt q}+R.                        \tag{3.4}
\]

Assume for contradiction that `M<c r^(3/2)`.  Since `h<=q`, equations
(3.4), `R>=r/2`, and `q<eta r` give

\[
 {hB\over R^2}
 \ll {\sqrt q\,M\over r^2}+{q\over r}
 \ll c\sqrt\eta+\eta.                          \tag{3.5}
\]

Choose `eta` and then `c` so that (3.5) is at most `10^(-8)`.
Lemma 2.1 produces two equal-norm points in the one-quadrant subpatch.
They are distinct and cannot be antipodal there, contradicting the
hypothesis.  This proves (1.2).

## 4. Rectangular corollary and exact scope

If an exact Gaussian-ideal rich-fibre patch has side lengths `r>=s`, its
`s`-by-`s` subpatch gives

\[
 s\ll M^{2/3}.                                   \tag{4.1}
\]

It is also the union of `s` parallel lines.  The collinear rich-fibre
theorem gives `r<=sqrt(S)`, where `S=|D+D|`.  Therefore

\[
 \boxed{|\mathcal G|=rs\ll M^{2/3}\sqrt S}.     \tag{4.2}
\]

The remaining lattice-like branch is no longer exact *ideal* arithmetic, but
it may still be an exact non-`J`-stable oblique lattice.  The universal
`r^(6/5)` Gaussian-core bound for that case is in
`OBLIQUE_LATTICE_GAUSSIAN_CORE.md`.  A full solution must improve it to the
critical exponent or show that supercritical adaptive seven-incidence mass
yields a sufficiently stable Gaussian patch, and then aggregate the fibres
within `N^(1+o(1))S`.

## 5. Verification

`verify_gaussian_ideal_coset_height.py` checks the entire reduced-denominator
construction with exact integer and rational arithmetic.  Its examples
include inert rational steps, split composite norms, powers of `1+i`, mixed
even norms, nonprimitive steps, and reductions in which neither original
coordinate numerator is invertible modulo the unreduced norm.  It verifies
the primitive congruence, coprimality, full CRT modulus, recovered grid
indices, and equality of the corresponding physical Gaussian-integer norms.
