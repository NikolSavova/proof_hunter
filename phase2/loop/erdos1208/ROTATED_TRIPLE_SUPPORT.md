# Rotated triple support: the surviving full-resolution target

Let `A` be a distance-Sidon subset of the integer square `[m]^2`, let
`k=|A|`, and put

\[
  J(x,y)=(-y,x),\qquad D=A-A.
\]

This note isolates the cleanest statement still capable of proving the
conjectural square-grid upper bound.  Unlike the corresponding energy and
pointwise-overlap conjectures, it survives every presently known exact
obstruction.

## 1. Exact reduction

Distance uniqueness implies oriented vector uniqueness: every nonzero
element of `D` has exactly one representation as `a-b`.  It also implies

\[
  D\cap JD=\{0\}.                                      \tag{1.1}
\]

Indeed, a nonzero equality `a-b=J(c-d)` gives two internal segments of the
same length; distance uniqueness identifies their unordered endpoint pairs,
after which a nonzero vector cannot equal its own quarter-turn or its
negative quarter-turn.

Consider

\[
  \Phi(a,b,c)=a+J(b-c),\qquad (a,b,c)\in A^3.           \tag{1.2}
\]

The desired support theorem is

\[
  \boxed{|A+JA-JA|\ge k^{3-o(1)}}.                    \tag{1.3}
\]

The left side lies in a square of side `O(m)`, hence has `O(m^2)` lattice
points.  Thus (1.3) gives

\[
  k\le m^{2/3+o(1)}.                                  \tag{1.4}
\]

Applied to the full `m`-by-`m` grid, (1.4) is
`F_2(m^2)\le m^{2/3+o(1)}`.  Standard interpolation handles arbitrary `n`,
and the Clemen--Fuehrer--Roche-Newton lower bound then yields

\[
  F_2(n)=n^{1/3+o(1)}.
\]

So (1.3), by itself, resolves the power-law order in Erdos problem 1208.

## 2. Why support survives the perpendicular-ruler obstruction

Take a dense `2s`-mark Golomb ruler `R` of length `s^{2+o(1)}`, split it
into `R_1,R_2` of size `s`, and form

\[
 A=H\cup V,
 \quad H=\{(u,0):u\in R_1\},
 \quad V=\{(0,C+v):v\in R_2\},                         \tag{2.1}
\]

with a good integer offset `C`.  The construction is distance-Sidon in a
square of side `k^{2+o(1)}`, where `k=2s`; see
`PERPENDICULAR_RULER_OBSTRUCTION.md`.

This family has rotated triple energy `Omega(k^4)`, cross-sum energy
`Omega(k^6)`, and quadratic translated-difference overlap.  It therefore
falsifies all earlier size-only energy and overlap targets.  But it does not
falsify (1.3).  Restrict (1.2) to

\[
 a=(u,0)\in H,\quad b=(u_2,0)\in H,
 \quad c=(0,C+v)\in V.
\]

Then

\[
  \Phi(a,b,c)=(u+C+v,u_2).                             \tag{2.2}
\]

The map `(u,v) -> u+v` is injective on `R_1 x R_2`: an equality of two
cross-sums gives an equality between two differences of the full Golomb
ruler, and is therefore trivial.  The second coordinate in (2.2) recovers
`u_2`.  Hence these restricted triples alone give exactly `s^3=(k/2)^3`
different outputs.

The obstruction is instructive.  One arm-type compresses and creates the
large energy, while a complementary mixed arm-type supplies cubic support.
Any proof based on an untruncated second moment misses this compensation.

## 3. Translation-incidence formulation

For each `d in D`, let

\[
  L_d=A+Jd.                                           \tag{3.1}
\]

Then `|L_d|=k` and

\[
  A+JD=\bigcup_{d\in D}L_d.                           \tag{3.2}
\]

Two different translates meet in at most one point.  If

\[
  a+Jd=a'+Jd',
\]

then `a-a'=J(d'-d)`, and oriented vector uniqueness gives at most one
ordered pair `(a,a')` for the fixed right side.  Thus the bipartite incidence
graph whose right vertices are `d in D`, whose left vertices are support
points, and whose edges are membership in `L_d`, is `C_4`-free.  It has

\[
  |D|=k^2-k+1,\qquad e=k|D|=k^3+O(k^2).               \tag{3.3}
\]

This observation alone only gives a quadratic support bound.  A projective
plane has the same degree and `C_4` profile.  The missing information is that
the blocks are translates of one set, their translation parameters form the
rotated realized difference set `JD`, and every norm in `D` is unique up to
sign.

## 4. The short-cycle attempt and its failure

Put a graph `G` on the columns `D`, joining distinct `d,d'` when their
translates meet.  Equivalently,

\[
  d\sim d'\quad\Longleftrightarrow\quad J(d'-d)\in D.  \tag{4.1}
\]

A triangle of `G` is a `6`-cycle in the bipartite incidence graph, unless
the three intersections coincide.  Its edge labels are vectors
`e_1,e_2,e_3 in D` with

\[
  e_1+e_2+e_3=0.                                     \tag{4.2}
\]

If the support were `k^{3-delta}`, convexity and graph supersaturation would
force many such cycles.  An upper bound of `k^{3+o(1)}` for the number of
triangles of `G` would therefore prove (1.3).

That proposed triangle bound is false.  Dense perpendicular-ruler examples
already have a growing super-cubic number of `G`-triangles.  They also have
many `4`-cycles in `G` (equivalently `8`-cycles in the incidence graph).
The source is a large supply of additive relations among one-dimensional
Golomb-ruler differences.  Those cycles coexist with cubic support because
they are concentrated in the compressing arm-type from Section 2.

Consequently, neither `C_4`-freeness, bounded girth, nor a fixed short-cycle
supersaturation theorem can prove (1.3).  A successful argument must retain
which portions of `A` generate the high-multiplicity fibres and recover the
complementary expanding triples.

## 5. Exact fibre structure

For an output `x`, write

\[
  F_x=\{(a,b,c)\in A^3:a+Jb-Jc=x,\ b\ne c\}.           \tag{5.1}
\]

Each coordinate projection is injective on `F_x`.  More strongly, if
`(a_i,b_i,c_i)` list the representations, then

\[
  a_i+Jb_j-Jc_l=x
\]

holds only for `i=j=l`.  Indeed, comparison with the representation having
first coordinate `a_i` gives

\[
  b_j-b_i=c_l-c_i,
\]

and oriented-difference uniqueness makes a non-diagonal equality impossible.
Thus every fibre is an induced tri-coloured matching and has size at most
`k`.

This is still insufficient in the abstract.  The map
`(a,b,c) -> (a+b,a+c)` over a finite group partitions all `k^3` triples into
`k^2` induced perfect matchings.  The load-bearing facts here are torsion-free
planar realization, the fixed quarter-turn, and radial uniqueness.

## 6. Computational falsification audit

`analyze_rotated_triple_map.py` now reports both the support and the short
cycle profile.  Random-greedy distance-Sidon subsets at sides `20,40,80,120`
used respectively about

\[
  0.669,\ 0.659,\ 0.672,\ 0.655
\]

of the full `k^3` support scale (the script excludes the diagonal triples in
one of its two displays, accounting for the harmless `O(k)` discrepancy).

Anisotropically stretched Welch Costas sets are even closer to injective:
for sizes from `6` to `60`, the measured ratios
`|A+JA-JA|/k^3` rise from about `0.79` to about `0.983`.

Exhaustive enumeration in grids of side at most four gives minimum ratios
`0.75, 0.704, 0.656` for `k=2,3,4`.  The eight-point perpendicular-ruler
certificate has support `417` out of `512` possible triples.  No tested
family gives a sub-cubic trend.

These computations are only falsification checks.  Their value is that the
support target passes examples that decisively refute the energy target.

### Vector-Sidon alone is not enough

There is a sharp counterfactual control.  An unstretched Welch Costas set

\[
  W_p=\{(j,g^j\bmod p):0\le j<p-1\}
\]

has unique directed difference vectors, so it is an additive/vector Sidon
set.  Nevertheless its modular origin compresses the integer set
`W_p+JW_p-JW_p` to `O(p^2)` points (only constantly many carry states lie
over each residue of `F_p^2`).  Exact computations for `p` from `7` to `127`
show `|W_p+JW_p-JW_p|/|W_p|^3` decaying from `0.53` to `0.054`, consistent
with a quadratic image.  These sets are not distance-Sidon: distinct Costas
displacements can have the same Euclidean norm.

After applying the smallest integral shear/stretch found by
`analyze_affine_costas_energy.py` that separates all squared norms, the same
families have support ratios rising toward one (about `0.983` at size `60`).
Thus neither ordinary Sidonicity nor `C_4`-freeness can imply (1.3).  A proof
must use the injectivity of the *quadratic norm* on `D/{+-1}`.  The Costas
comparison also suggests an uncertainty principle: preserving modular
three-term compression and separating all quadratic norms cannot both occur
at low geometric height.

## 7. What a proof now has to do

There are three credible formulations of the missing structural step.

1. **Heavy-fibre compensation.**  Prove that triples lying in fibres of
   polynomial multiplicity use only a structured portion of `A`, while
   complementary coordinate types contribute `k^{3-o(1)}` distinct outputs.
   Section 2 is the exact model.
2. **Translate-union stability.**  Classify a family of the translates
   `A+Jd`, `d in D`, whose union has a fixed-power deficit from `k^3`.
   The conclusion must be stronger than a projective-plane or ordinary
   additive-energy inverse theorem and must remember the realized difference
   set.
3. **Line-structured versus transverse dichotomy.**  A large collinear
   subset already supplies a cubic sub-support by separating the coordinate
   along the line from the perpendicular difference coordinate.  In the
   absence of rich lines, seek an incidence or polynomial-partitioning bound
   on the high fibres.  The two estimates must be coupled rather than
   optimized independently, or they lose a fixed power.  The line branch is
   now rigorous in `PARALLEL_LINE_SUPPORT_LEMMA.md`: a cover by `r` parallel
   lines gives support at least `k^3/r^2-O(k^2/r)`.  The same note gives the
   exact random-thinning reduction for the remaining transverse collision
   count.
4. **Quadratic-separation versus Freiman compression.**  Small support gives
   a Freiman-order-three model resembling the modular Welch example.  Prove
   that any such low-complexity model necessarily repeats the value of the
   Euclidean norm on two non-antipodal realized differences.  Equivalently,
   quantify the experimentally sharp jump in support when a Costas model is
   stretched just enough to separate its norms.

At present (1.3) is a conjectural lemma, not a proof.  It is nevertheless the
first direct full-resolution target in this project that survives the
square-grid profile, generic direct-sum counterexamples, the Costas tests, and
the sharp perpendicular-ruler construction.
