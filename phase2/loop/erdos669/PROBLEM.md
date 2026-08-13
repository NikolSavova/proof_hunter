# Erdős #669 — rich lines in planar point sets

## Correct statement

For a set \(P\) of \(n\) points in \(\mathbb R^2\), write

- \(f_k(P)\) for the number of lines containing exactly \(k\) points of \(P\);
- \(F_k(P)\) for the number of lines containing at least \(k\) points of \(P\);
- \(f_k(n)=\max_{|P|=n} f_k(P)\) and \(F_k(n)=\max_{|P|=n}F_k(P)\).

Estimate these functions and, in particular, determine the limits of
\(f_k(n)/n^2\) and \(F_k(n)/n^2\).

The problem page records the pair-counting upper bound

\[
F_k(n)\le \frac{\binom n2}{\binom k2},
\]

and the solved \(k=3\) asymptotic \(f_3(n),F_3(n)=n^2/6-O(n)\).

Source: [Erdős Problems #669](https://www.erdosproblems.com/669).

## Important correction to the repo shortlist

`../candidates/erdos/SHORTLIST.md` guessed from the linked OEIS sequences that
#669 was a Heilbronn/fixed-area-triangle problem. That guess is false. The
durable pipeline database had the correct statement all along. None of the
Heilbronn or Golod--Shafarevich material applies here.

## Result of the 2026-08-13 attack

The attack did not settle the existence or value of either requested limit for
any \(k\geq4\).  It did produce a general exact lower construction.

Let \(A(r)\) be the minimum area of a convex lattice \(r\)-gon.  For every
fixed \(k\geq3\),

\[
f_k(n),F_k(n)\geq \frac{n^2}{4A(2k)}-O_k(n).
\]

The proof uses \(k\) primitive lattice directions and the lattice points of
their Minkowski-sum zonotope.  For an associated determinant sum \(D\), the
line arrangement has the exact parameters

\[
n_q=2Dq+k,\qquad t_k^{\mathrm{fin}}=Dq^2+kq+1.
\]

The construction, its sublattice correction, its optimality within the whole
lattice parallel-strip scheme, and the exact verifier are in
ZONOTOPE_CONSTRUCTION.md and verify_zonotope_construction.py.

Simpson's published minimum-area values give the coefficients

\[
\frac1{28},\frac1{56},\frac1{96},\frac1{160},\frac1{236},
\frac1{348},\frac1{484},\frac1{656}
\]

for \(k=4,\ldots,11\), respectively.  The values for \(k=5,6,7,8,11\)
exceed the corresponding coefficients in Palásti's 1986 table.  Direct
searches did not locate these orchard deductions, but novelty is not yet
cleared; Simpson's direction optimization is prior art, and the \(k=4\)
instance was hidden in a 2019 non-English web source.

Together with the Szemerédi--Trotter bound
\(F_k(n)=O(n^2/k^3+n/k)\) and the classical estimate
\(A(2k)=\Theta(k^3)\), the theorem determines the correct
order \(k^{-3}\) of the quadratic coefficient as \(k\to\infty\).  It does not
determine the fixed-\(k\) constants.

For \(k=4\), this specializes to

\[
f_4(n)\ge \frac{n^2}{28}-O(n),
\qquad
F_4(n)\ge \frac{n^2}{28}-O(n).
\]

For every \(q\ge2\), an explicit arrangement of \(14q\) real projective lines
has exactly \(7q^2\) finite vertices of multiplicity four. Projective duality
therefore gives \(14q\) planar points with at least \(7q^2\) lines containing
exactly four points. Adding generic points handles arbitrary \(n\).

This coefficient \(1/28=0.0357142857\ldots\) strictly exceeds the
\(7/200=0.035\) coefficient printed in Palásti's 1986 paper. However, a late
kill-search found that Zhao Hui Du's 2019 Chinese orchard-problem page had
already described an octagonal pruning with \(14m+O(1)\) lines and
\(7m^2+O(m)\) fourfold points. Those counts imply the same \(1/28\) coefficient,
although the page accidentally prints \(1/24\). Thus the asymptotic lower bound
is prior art, not a new result. The construction and exact count are in
`FOUR_DIRECTION_BOUND.md`; the independent exact verifier is
`verify_four_direction.py`.

Combining pair counting with Melchior's inequality also gives, for every fixed
\(k\ge4\),

\[
F_k(n)\le
\max\left\{1,\frac{\binom n2-3}{\binom k2+k-3}\right\}
=\frac{n^2}{(k-2)(k+3)}+O(n).
\]

Thus the present \(k=4\) window is

\[
\boxed{
\frac1{28}
\le \liminf_{n\to\infty}\frac{f_4(n)}{n^2}
\le \limsup_{n\to\infty}\frac{F_4(n)}{n^2}
\le \frac1{14}.}
\]

## Status discipline

- The mathematics above has an exact enumeration artifact and is being
  adversarially cross-checked.
- The upper bound is a standard immediate consequence of Melchior and should
  not be advertised as novel.
- **Prior-art kill:** Zhao Hui Du committed the asymptotic
  \(14m+O(1),7m^2+O(m)\) octagonal construction to the emathgroup repository on
  2019-10-20. The displayed \(1/24\) on that page is inconsistent with its own
  counts; the implied coefficient is \(1/28\). Our exact formula and verifier are
  useful clarifications, not a novelty claim.
- This is a partial bound for \(k=4\), not a solution of #669 and not a proof
  that either requested limit exists.
- The zonotope theorem is a general partial result, not a universal quadratic
  amplifier.  It cannot transfer an arbitrary limsup witness and therefore
  does not prove convergence.
- The apparent \(k=5,6,7,8,11\) improvements must remain “unrecorded in the
  sources checked” pending specialist citation clearance.
