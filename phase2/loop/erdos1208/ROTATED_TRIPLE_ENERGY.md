# The rotated triple-sum reduction for the square grid

This note records a sharp reformulation of the unresolved square-grid upper
bound.  It does not by itself solve the problem, but it couples the additive
and radial parts of the distance-Sidon condition more tightly than the raw
distance-energy formulation.

Let

\[
  A\subset [m]^2\subset\mathbb Z^2,\qquad |A|=k,
\]

and suppose that all unordered distances determined by `A` are different.
Write

\[
  J(x,y)=(-y,x)
\]

for quarter-turn.

## 1. Two exact consequences of distance uniqueness

First, every nonzero oriented vector in \(A-A\) has a unique representation.
Indeed, equality of two oriented differences implies equality of their norms,
and hence the two underlying unordered edges are the same.

Second, the cross-sum map

\[
  A\times A\longrightarrow A+JA,\qquad (a,b)\longmapsto a+Jb
\]

is injective.  If

\[
  a+Jb=a'+Jb',
\]

then \(a-a'=J(b'-b)\), so the two internal segments have the same
length.  Distance uniqueness makes their unordered endpoint pairs equal.
The remaining vector identity would require a nonzero real vector to equal
its positive or negative quarter-turn, which is impossible.  Therefore

\[
  |A+JA|=k^2.                                      \tag{1.1}
\]

Equivalently,

\[
  (A-A)\cap J(A-A)=\{0\}.                         \tag{1.2}
\]

The ordinary vector-Sidon condition alone gives the familiar \(k=O(m)\)
bound.  The point of (1.1)--(1.2) is that they retain the orthogonality which
ordinary additive energy discards.

## 2. A cubic map into a two-dimensional box

For \(b\ne c\), define

\[
  \Phi(a,b,c)=a+J(b-c).
\]

There are exactly \(k^2(k-1)\) ordered input triples.  Every image lies in a
box with fewer than \(9m^2\) lattice points.  If

\[
  r(x)=\#\{(a,b,c)\in A^3:b\ne c,\ \Phi(a,b,c)=x\},
\]

then Cauchy--Schwarz gives the unconditional lower bound

\[
  \mathcal T_J(A):=\sum_x r(x)^2
  \ge \frac{k^4(k-1)^2}{9m^2}.                    \tag{2.1}
\]

The collision equation counted on the left is

\[
  a+J(b-c)=a'+J(b'-c').                           \tag{2.2}
\]

Because nonzero differences have unique oriented representations, (2.2)
can also be read as a right-angled additive-triple count in the difference
set \(D=A-A\):

\[
  a-a'=J\big((b'-c')-(b-c)\big).
\]

Thus the missing upper estimate is not a generic six-variable energy bound;
it is a mixed energy of a Sidon difference set and its quarter-turn.

If diagonal triples \(b=c\) are included, their image is exactly `A`, with
multiplicity `k` at every point.  No off-diagonal triple can land in `A`:
such a triple would give an internal segment congruent to its quarter-turn,
contradicting distance uniqueness.  Hence the full triple energy is exactly

\[
  \mathcal T_J(A)+k^3.                            \tag{2.3}
\]

In a finite torus large enough to avoid wraparound, (2.3) has the Fourier
form

\[
  \frac1{|G|}\sum_{\chi\in\widehat G}
    |\widehat{1_A}(\chi)|^2
    |\widehat{1_A}(J^*\chi)|^4.                  \tag{2.4}
\]

The zero frequency in (2.4) is precisely the source of the cube-root scale.

## 3. A sufficient theorem that would close the exponent

Either of the following statements is sufficient:

\[
  \mathcal T_J(A)\le k^{3+o(1)},                  \tag{3.1}
\]

or, slightly more directly,

\[
  |A+JA-JA|\ge k^{3-o(1)}.                       \tag{3.2}
\]

Combining (3.1) with (2.1), or (3.2) with the fact that the triple sum lies
in a box of `O(m^2)` lattice points, gives

\[
  k\le m^{2/3+o(1)}.                              \tag{3.3}
\]

Since the ambient grid has \(n=m^2\) points, (3.3) would yield

\[
  F_2(n)\le n^{1/3+o(1)}.
\]

Together with the Clemen--Fuehrer--Roche-Newton lower bound, this would
determine the power-law order in Erdős problem 1208.

## 4. What the reduction does *not* prove

Pointwise bounded multiplicity is false.  For a fixed external point `x`,
one may choose disjoint pairs \((b_i,c_i)\) generically and include

\[
  a_i=x+J(b_i-c_i).
\]

No forced equality of internal distances occurs between different triples,
so a generic realization can remain distance-Sidon while `x` has linearly
many representations.  A simple observation does show that the pairs
\((b_i,c_i)\) at one image point form a matching: two representations sharing
`b` (or sharing `c`) would force the corresponding two `a`-points to be at
the same distance as the two remaining endpoints.  This only gives
\(r(x)=O(k)\), and therefore recovers no more than the trivial \(k=O(m)\)
bound.

Nor does (3.2) follow from a standard sumset inequality.  Equation (1.1)
says that \(A+JA\) is a direct sum, but generic direct-sum pairs can have a
small third sumset.  Any proof must use that the two summands are rotations
of the *same* set and that every radial fibre of `A-A` contains only the
antipodal pair belonging to one edge.

Finally, the entropy theorem of Tardos on pair sums of matrix rows does not
close this gap.  The pinned-distance rows of `A` do have the attractive
property that two rows meet in exactly one entry, but there are only `k`
rows.  Tardos's exponent (which tends to \(1/e\) as the row length grows) is
far too small to turn the `O(m^2)` range of pinned pair-sums into (3.3).

## 5. Experimental falsification check

`analyze_rotated_triple_map.py` greedily constructs distance-Sidon subsets
and measures the representation function.  Typical runs for side lengths
20, 40, 80, and 120 found off-diagonal maximum multiplicities 5, 6, 6, and
8, while

\[
  \mathcal T_J(A)/(k^2(k-1))
\]

stayed between about 1.7 and 1.9.  This is consistent with (3.1), but it is
only a sanity check.  The generic construction above shows why maximum
multiplicity is the wrong invariant and why a proof must control the total
mixed energy.

## 6. Next attack

The clean target is now a dichotomy for (2.4):

1. either the mixed sixth moment is \(k^{3+o(1)}\), giving (3.3); or
2. a large mixed moment produces, through an inverse theorem, a substantial
   part of `A-A` that is approximately stable under a perpendicular internal
   translation.

The second branch must then be shown incompatible with radial uniqueness.
Ordinary Balog--Szemerédi--Gowers is insufficient because it may return a
rank-two progression, i.e. the grid itself.  The required inverse conclusion
has to retain the quarter-turn in (1.2), rather than merely assert small
doubling.
