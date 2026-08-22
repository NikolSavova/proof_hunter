# Dense K2,4 footprint collisions are metric-transverse or two-line

## 1. Outcome

The dense branch of the canonical cross-footprint dichotomy contains two
common chords.  Retaining the norms of the literal first and second tracks
turns those chords into an exact rank-two metric map.

For two owner cells write their centres and first colours as `(c,z)` and
`(c',z')`.  A footprint collision has parameter cross differences

\[
 A=f-f',\qquad B=g-g',
\]

and

\[
 \Delta z+(I-J)\Delta c=A-JB.                   \tag{1.1}
\]

Put

\[
 u=\Delta c-A.
\]

Suppose `A` has two representations whose first components differ by
`alpha ne0`, and `B` has two representations whose first components differ
by `beta ne0`.  Then two exact differences of squared-distance gaps are

\[
 \boxed{G_0=-2u\cdot\alpha,
 \qquad G_1=-2u\cdot J\beta.}                    \tag{1.2}
\]

The affine map `u -> (G_0,G_1)` has determinant

\[
 \boxed{4\det(\alpha,J\beta)=4\alpha\cdot\beta.} \tag{1.3}
\]

Consequently every dense collision has an exact alternative.

* **Metric-transverse:** some common `A`-chord `alpha` and common `B`-chord
  `beta` satisfy `alpha dot beta ne0`.  The two metric coordinates recover
  `u` uniquely and occupy a rank-two integer lattice of covolume at least
  `4|alpha dot beta|`.
* **Two-line:** every `A`-chord is perpendicular to every `B`-chord.  Then
  all representations of `A` lie on one affine line in each parameter set,
  and all representations of `B` lie on an affine line in the perpendicular
  direction.

This is a real gain over the bare dense K2,2: the generic branch has a
determinant weight, while failure of transversality has an exact geometric
line structure.  It does not yet sum the determinant-weighted cells at the
target scale; endpoint ownership must still be retained in that sum.

## 2. Literal track calculation

For the first parameter coordinate define the literal first tracks

\[
 X_i=c-f_i,\qquad X'_i=c'-f'_i.
\]

Two representations of `A` satisfy

\[
 f_1-f'_1=f_2-f'_2=A,
 \qquad
 \alpha=f_1-f_2=f'_1-f'_2\ne0.                  \tag{2.1}
\]

Thus

\[
 X_1=X_2-\alpha,qquad X'_1=X'_2-\alpha,
 \qquad X_2-X'_2=\Delta c-A=u.                  \tag{2.2}
\]

Every `X` is a literal member of `D`.  Subtracting the two squared-norm
gaps gives

\[
\begin{aligned}
 G_0&=(|X_1|^2-|X_2|^2)-(|X'_1|^2-|X'_2|^2)\\
    &=-2u\cdot\alpha.                            \tag{2.3}
\end{aligned}
\]

For the second coordinate use

\[
 T_i=z-J(c-g_i),\qquad T'_i=z'-J(c'-g'_i).       \tag{2.4}
\]

Two representations of `B` with common chord `beta` give

\[
 T_1=T_2+J\beta,qquad T'_1=T'_2+J\beta.         \tag{2.5}
\]

The collision equation (1.1) is exactly

\[
 T_2-T'_2=\Delta z-J\Delta c+JB=-u.              \tag{2.6}
\]

Therefore

\[
\begin{aligned}
 G_1&=(|T_1|^2-|T_2|^2)-(|T'_1|^2-|T'_2|^2)\\
    &=-2u\cdot J\beta,                           \tag{2.7}
\end{aligned}
\]

which proves (1.2)--(1.3).  These are differences of four actual squared
edge lengths in each coordinate, not formal parameter norms.

## 3. Exact two-line alternative

Let `C_A` be the nonzero differences between first components of distinct
representations of `A`; define `C_B` similarly.  Both are nonempty in the
dense branch.

If there is no transverse pair, then

\[
 \alpha\cdot\beta=0
 \quad\hbox{for all }\alpha\in C_A,\ \beta\in C_B. \tag{3.1}
\]

Fix `alpha_0 in C_A` and `beta_0 in C_B`.  Every element of `C_B` lies on
the one-dimensional line perpendicular to `alpha_0`; every element of
`C_A` lies on the line perpendicular to `beta_0`.  Hence each chord family
is one-dimensional and the two directions are perpendicular.

Choose one representation `(f_0,f'_0)` of `A`.  Every other first
component differs from `f_0` by an element of the span of `C_A`; the same
holds for the primed components.  Thus the two representation sets lie on
parallel affine lines.  The `B` representations obey the perpendicular
statement.  This proves the alternative without a regularity or inverse
theorem.

The line branch should be attacked with the existing directional
Golomb/height budgets.  The transverse branch should be summed with the
full determinant weight before either endpoint owner is discarded.

## 4. Scope and next gate

The metric pair `(G_0,G_1)` alone does not recover all four parameter pairs;
it recovers the two-dimensional displacement `u` for fixed owners and
chosen chords.  Radial uniqueness can recover individual literal tracks
once their norm labels are retained, but counting all such labels
independently gives an `m^4` ambient box and loses the target.

The exact remaining theorem is therefore a **joint** packing:

1. sum transverse dense collisions with weight supplied by
   `|alpha dot beta|` and the two physical owners; and
2. sum the perpendicular two-line cells using their primitive directions,
   line lengths and nested-core loads.

The finite Costas-31 top band is entirely in one resonance class
`e=b-a`; `80/82` support collisions are dense, so this dichotomy acts on
the genuine dominant stress rather than a negligible residue.

The exact analyzer gives a stronger metric profile.

* Costas 23, load three: of `93` dense collisions, `90` are transverse and
  `3` are two-line.  Every nonzero selected maximum chord dot product is at
  least `529=23^2`.
* Costas 31, top load six: all `80` dense collisions are transverse and
  none is two-line.  The maximum-dot histogram is

  \[
   31^2:2,\quad2\cdot31^2:8,\quad3\cdot31^2:10,
   \quad4\cdot31^2:26,\quad5\cdot31^2:34.        \tag{4.1}
  \]

Thus the equality model does not merely avoid the exceptional line branch;
it supplies a determinant growing quadratically in its natural scale.  A
successful global theorem should be sharp on this determinant-weighted
population rather than treating it as an error term.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_k24_dense_collision_metric_chords.py
```

The verifier checks the literal track formulas, the determinant, recovery
of `u`, and the all-pairs orthogonality implication for the two-line branch.
