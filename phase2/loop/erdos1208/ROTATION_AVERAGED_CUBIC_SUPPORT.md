# Rotation-averaged cubic support

## Status

For one prescribed quarter-turn, the conjectural estimate

\[
 |A+J(A-A)|\ge |A|^{3-o(1)}
\]

is still open.  There is, however, an exact averaged theorem: among any
`|A|` distinct rotations of the plane, one rotation has a constant fraction
of full cubic support.  The proof uses distance uniqueness only once, in its
sharpest form: a nonzero vector has the same length as at most two directed
differences of `A`.

This does **not** solve the square-grid problem, because the ordinary lattice
has only four integral rotations.  It gives a precise cube-root criterion for
the separate number-field unit-rotation construction: a hostile additive box
with `k` exact low-expansion rotations forces every distance-Sidon subset to
have size `O(M^(1/3))`, where `M` is the common ambient support size.

The finite calculations are checked by
`verify_rotation_averaged_support.py`.

## 1. The averaged energy theorem

Let `A` be a distance-Sidon set of `k` points in the Euclidean plane.  For a
rotation `R in SO(2)`, put

\[
 \Phi_R(a,b,c)=a+R(b-c),
 \qquad
 \mathcal E_R(A)
   =\#\{(a,b,c,a',b',c')\in A^6:
               \Phi_R(a,b,c)=\Phi_R(a',b',c')\}.
\]

If `mathcal R` is any finite set of `r` distinct rotations, then

\[
 \boxed{
 \sum_{R\in\mathcal R}\mathcal E_R(A)
 \le r(2k^3-k^2)+2k^4.}                         \tag{1.1}
\]

Consequently some `R in mathcal R` satisfies

\[
 \mathcal E_R(A)
 \le 2k^3-k^2+\frac{2k^4}{r},                  \tag{1.2}
\]

and Cauchy--Schwarz gives

\[
 \boxed{
 |A+R(A-A)|
 \ge \frac{k^6}{2k^3-k^2+2k^4/r}.}             \tag{1.3}
\]

In particular, if `r>=k`, then

\[
 |A+R(A-A)|\ge \frac14 k^3.                    \tag{1.4}
\]

The constant `1/4` is merely a convenient uniform value; (1.3) is the exact
statement used below.

## 2. Proof

A distance-Sidon set is vector-Sidon.  Hence every nonzero directed
difference has one ordered representation, and every unordered pair sum has
one unordered representation.  It follows that the ordered pair-sum energy
is

\[
 \#\{(b,c',b',c)\in A^4:b+c'=b'+c\}
 = k+4{k\choose2}=2k^2-k.                       \tag{2.1}
\]

A collision of `Phi_R` is exactly

\[
 a-a'=R\big((b'-b)+(c-c')\big).                 \tag{2.2}
\]

First suppose `a=a'`.  Equation (2.2) then says
`b+c'=b'+c`.  By (2.1), these collisions contribute exactly

\[
 k(2k^2-k)=2k^3-k^2                            \tag{2.3}
\]

for every rotation `R`.

Now suppose `a!=a'`.  Fix the ordered quadruple `(b,c,b',c')` and put

\[
 w=(b'-b)+(c-c').
\]

If `w=0`, (2.2) has no solution with `a!=a'`.  If `w!=0`, a solution must
satisfy

\[
 |a-a'|=|w|.                                    \tag{2.4}
\]

Distance uniqueness permits at most two ordered pairs `(a,a')` satisfying
(2.4): the two orientations of the unique unordered edge of that length.
For each fixed nonzero pair of vectors `w` and `a-a'` of equal length, there
is exactly one orientation-preserving rotation taking `w` to `a-a'`.
Therefore the fixed quadruple contributes to at most two pairs
`(R,a,a')` as `R` ranges over `mathcal R`.  There are `k^4` ordered
quadruples, so all non-diagonal collisions contribute at most `2k^4` after
summing over the rotations.  Together with (2.3), this proves (1.1).

Finally, `Phi_R` has `k^3` inputs.  If its fibre sizes are `m_x`, then

\[
 k^6=\left(\sum_xm_x\right)^2
 \le |A+R(A-A)|\sum_xm_x^2
 =|A+R(A-A)|\mathcal E_R(A),
\]

which proves (1.3).

## 3. An exact hostile-box criterion

Let `P` be a finite planar point set and let `mathcal R` be `r` distinct
rotations.  Suppose that for every `R in mathcal R` there is a finite set
`Omega_R` with

\[
 P+R(P-P)\subseteq\Omega_R,
 \qquad |\Omega_R|\le M.                         \tag{3.1}
\]

If `A subseteq P` is distance-Sidon and `k=|A|`, then (1.3) and (3.1) imply

\[
 M\ge \frac{k^6}{2k^3-k^2+2k^4/r}.             \tag{3.2}
\]

Two convenient consequences are

\[
 r\ge k\quad\Longrightarrow\quad k\le(4M)^{1/3},       \tag{3.3}
\]

and, when `r<=k`,

\[
 k\le 2\sqrt{M/r}.                              \tag{3.4}
\]

Thus a family of additive boxes with `M=n^{1+o(1)}` and at least
`n^{1/3-o(1)}` exact rotations satisfying (3.1) would prove the desired
upper bound `F_2(n)<=n^(1/3+o(1))`.

This criterion is essentially the cubic-support counterpart of the disjoint
rotation lemma in `UNIMODULAR_UNIT_ROTATIONS.md`.  In a number field, a
unimodular unit is an exact planar rotation without a denominator at the
chosen embedding.  The unresolved arithmetic requirement is still that the
other embeddings of enough independent units expand the Minkowski box by
only a subpolynomial factor.  The relative-regulator threshold recorded in
that note remains load-bearing.

## 4. Why this does not average away the fixed-quarter-turn problem

The theorem says that a bad rotation is exceptional, not that no bad
rotation exists.  The perpendicular-ruler construction makes the fixed
quarter-turn energy of `a+J(b-c)` of fourth-power order, while (1.1) forces
most other rotations to have cubic energy.  The ordinary integer lattice
only preserves the rotations `+-I,+-J`, so one cannot select the good
rotation while retaining an `O(m^2)` lattice support.

Rational Pythagorean rotations give arbitrarily many choices, but clearing a
denominator `q` enlarges the lattice support by `q^2`.  The number of
available rotations and this denominator cost cancel before reaching the
cube-root exponent.  Exact small algebraic rotations remain the only known
way to make (3.3) useful for a hostile construction.

## 5. Calibration

The verifier uses the exact 12-point adversarial support witness and twelve
distinct rational rotations.  It checks distance uniqueness, computes every
fibre of every `Phi_R` with rational arithmetic, verifies (1.1), and checks
the Cauchy support bound.  It also recomputes the fixed-quarter-turn support
ratios on the stored adversarial and heavy-row witnesses.  Those ratios stay
on a constant cubic scale; this is evidence only, not part of the theorem.
