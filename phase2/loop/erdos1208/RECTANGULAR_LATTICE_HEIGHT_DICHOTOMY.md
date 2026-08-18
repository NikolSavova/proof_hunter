# Sharp aspect-ratio dichotomy for unit-lattice fibres

## 1. The tempting area bound is false

After `UNIT_LATTICE_RICH_FIBRE_HEIGHT.md`, the natural extension would say
that a translated `r`-by-`s` unit rectangle with unique radii needs height
`Omega(rs)`.  Thin rectangles disprove this by an arbitrary factor.

For `r>=s`, put

\[
 P_{r,s}=\{(s^2+i,j):0\le i<r, 0\le j<s\}.      \tag{1.1}
\]

All `rs` squared norms in (1.1) are distinct.  If two are equal, then

\[
 (s^2+i)^2-(s^2+i')^2=j'^2-j^2.                 \tag{1.2}
\]

If `i!=i'`, the nonzero left side has magnitude at least `2s^2+1`, whereas
the right side has magnitude at most `(s-1)^2`; this is impossible.  Hence
`i=i'`, after which nonnegativity gives `j=j'`.

The translation height is only `s^2`, independently of `r`.  In particular,
no lower bound of the form

\[
 \max(|U|,|V|)\gg (rs)^\epsilon s^{2-2\epsilon}
\]

can hold uniformly for any fixed `epsilon>0` as `r/s` tends to infinity.

## 2. The correct parameter is the shorter side

### Proposition 2.1

There are absolute constants `c,C>0` such that, for all sufficiently large
`r>=s`, the least translation height of a radially unique translated unit
`r`-by-`s` rectangle lies between

\[
 \boxed{c s^2\quad\hbox{and}\quad C s^2.}       \tag{2.1}
\]

Here radial uniqueness permits the same squared norm only for an antipodal
pair.

### Proof

The upper bound is (1.1), with `C=1`.

For the lower bound, any `r`-by-`s` rectangle contains an `s`-by-`s` unit
subpatch with the same translation.  Proposition 1.1 of
`UNIT_LATTICE_RICH_FIBRE_HEIGHT.md` applies to that square and gives
`max(|U|,|V|)>=c s^2`.  QED.

The containing coordinate box, rather than merely the translation, must
therefore have side at least

\[
 \Omega(r+s^2),                                 \tag{2.2}
\]

and the construction (1.1) shows that this is sharp up to constants.

## 3. Meaning for the adaptive rich-fibre problem

The counterexample does not create a new uncontrolled geometry.  A thin
`r`-by-`s` rectangle is the union of `s` parallel lines.  The algebraic-curve
branch already gives, for such a fibre `Q`,

\[
 |Q|\le s\sqrt{|D+D|}.                           \tag{3.1}
\]

The height theorem controls the balanced part through `s^2=O(m)`, while
(3.1) records the cost of the thin part in ordinary support.  Thus the next
rank-two theorem must couple aspect ratio to the line-cover budget.  It
cannot depend only on the number `|Q|=rs` of lattice points.

This identifies the precise shape of the remaining obstruction:

1. balanced dense patches pay quadratic ambient height;
2. highly eccentric patches escape the height bound, but are low-degree
   unions of parallel lines; and
3. sparse or oblique approximate progressions can still interpolate between
   these two regimes and are not yet controlled in aggregate.

The exact quarter-turn-stable version of the third item is treated in
`GAUSSIAN_PRIME_COSET_HEIGHT.md`.  Such a lattice is a Gaussian ideal rather
than an arbitrary oblique lattice.  A nonzero coset of an odd prime-norm
ideal pays the weaker but cube-root-critical height `Omega(s^(3/2))` on an
`s`-by-`s` subpatch.  Composite-index and approximate-module versions remain
open.

## 4. Verification

`verify_rectangular_lattice_height_dichotomy.py` checks the explicit family
(1.1) for aspect ratios up to `200:2`, exhaustively computes small optimum
translations when both coordinate placements are allowed, and confirms
that the earlier one-sided search would have missed the thin construction.
