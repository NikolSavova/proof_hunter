# Height barrier for a unit-lattice rich fibre

## 1. Result

The algebraic-curve branch leaves a rank-two lattice patch as the canonical
hard model.  The first height-sensitive part of that model can be closed.

### Proposition 1.1

There are absolute constants `c>0` and `r_0` such that the following holds.
Let

\[
 P_{U,V,r}=\{(U+i,V+j):0\le i,j<r\}\subset\mathbb Z^2. \tag{1.1}
\]

Suppose no two distinct non-antipodal points of `P_(U,V,r)` have the same
squared norm.  Then

\[
 \boxed{\max(|U|,|V|)\ge c r^2}                 \tag{1.2}
\]

for `r>=r_0`.  One may take, very conservatively, `c=10^(-6)`.

Consequently, if a complete difference set `D=A-A subseteq [-m,m]^2`
contains a translated unit `r`-by-`r` patch, distance-Sidonicity gives

\[
 \boxed{r^2\ll m.}                              \tag{1.3}
\]

Thus a rich fibre cannot hide an arbitrarily large dense unit Gaussian-
lattice patch at low height.  This is a genuine part of the surviving
rank-two branch, although (1.3) alone is not yet the cube-root theorem.

## 2. Shifted squares and their differences

If one coordinate interval crossed zero on both sides, it would contain
`a` and `-a` for some nonzero integer `a`.  Holding a nonzero value in the
other coordinate fixed gives two equal-norm points which are not antipodal.
Reflecting coordinate axes if necessary, it is therefore enough to take

\[
 0\le U\le V.                                   \tag{2.1}
\]

For a positive gap `d<r`, the differences between squares in the first
coordinate form the arithmetic progression

\[
 \Delta_U(d)
 =\{d(2U+d+2i):0\le i\le r-1-d\}.              \tag{2.2}
\]

Its common difference is `2d`, its centre is

\[
 dA,\qquad A=2U+r-1,                            \tag{2.3}
\]

and its half-width is `d(r-1-d)`.  The analogous progression
`Delta_V(e)` has centre `eB`, where `B=2V+r-1`.

An intersection

\[
 \Delta_U(d)\cap\Delta_V(e)\ne\varnothing       \tag{2.4}
\]

produces two distinct points of (1.1) with the same squared norm.  Indeed,

\[
 (U+i+d)^2-(U+i)^2
 =(V+j+e)^2-(V+j)^2
\]

rearranges to

\[
 (U+i+d)^2+(V+j)^2
 =(U+i)^2+(V+j+e)^2.                             \tag{2.5}
\]

## 3. Choosing the two gaps

Assume for contradiction that

\[
 V\le c r^2,qquad c=10^{-6}.                   \tag{3.1}
\]

Put `alpha=B/A`.  Choose `e` to be the largest positive odd integer not
exceeding

\[
 {r\over16\alpha},                              \tag{3.2}
\]

and choose the positive odd integer `d` nearest to `alpha e`.  For all
sufficiently large `r`, the elementary bounds following from (3.1) are

\[
 {r\over17}<d<{r\over15},
 \qquad
 {r\over32\alpha}<e<{r\over16},                \tag{3.3}
\]

and

\[
 |dA-eB|\le A.                                  \tag{3.4}
\]

Let `h_U=d(r-1-d)` and `h_V=e(r-1-e)` be the two half-widths.  Equations
(3.1)--(3.4) give

\[
 A<{1\over4}\min(h_U,h_V).                      \tag{3.5}
\]

For example,

\[
 h_U>{r^2\over20},
 \qquad
 h_V>{r^2\over35\alpha},
\]

whereas `A<=B<=2cr^2+r`; this proves (3.5) once `r` is large.
Therefore the real intervals underlying the two progressions overlap in an
interval longer than

\[
 2de.                                           \tag{3.6}
\]

Because `d,e` are odd, their two residue conditions

\[
 x\equiv d^2\pmod {2d},
 \qquad
 x\equiv e^2\pmod {2e}                          \tag{3.7}

are compatible: if `g=gcd(d,e)`, then
`2g` divides `d^2-e^2`.  The generalized Chinese remainder theorem gives
one common residue class of period

\[
 \operatorname{lcm}(2d,2e)\le2de.              \tag{3.8}

The overlap (3.6) consequently contains a common term of the two
progressions, proving (2.4) and contradicting radial uniqueness.  This
proves Proposition 1.1.

## 4. Exact scope

The proposition treats a full unit square-lattice patch.  It does not yet
cover a sparse generalized arithmetic progression, a patch in an arbitrary
oblique lattice, or the weighted aggregate of many smaller adaptive fibres.
Those extensions are needed before the height argument can replace the
seven-incidence estimate.

The important gain is conceptual and quantitative: the generic-translation
escape used by the fixed-fibre counterexamples is not free for a dense
rank-two patch.  Separating its radii consumes quadratic coordinate height,
which is visible in the ambient grid.

## 5. Verification

`verify_unit_lattice_rich_fibre_height.py` performs two independent exact
checks:

1. exhaustive minimization after the reflection reduction, for `2<=r<=15`,
   whose optima are already a constant multiple of `r^2`; and
2. direct CRT certificates from the proof for large random triples
   satisfying `0<=U<=V<=10^(-6)r^2`.

Every returned certificate is expanded back into the two distinct lattice
points in (2.5), and their squared norms are checked exactly.
