# Perpendicular rulers kill size-only rotated-overlap bounds

This note gives a genuine distance-Sidon obstruction to all three proposed
size-only estimates

\[
 \max_t M_A(t)\le |A|^{2-\delta},\qquad
 E^+(A+JA)\le |A|^{6-\delta},\qquad
 \mathcal T_J(A)\le |A|^{4-\delta}.             \tag{1}
\]

The construction is integral and planar.  It does not invalidate an estimate
which also uses the side length of the containing square.

## 1. Construction

For every positive integer \(s\), take a \(2s\)-mark Golomb ruler

\[
 S\subset[0,L],\qquad L=O(s^2).
\]

Such rulers follow, for example, from the classical Bose--Chowla Sidon
construction (and Bertrand's postulate to pass to every \(s\)).  Partition
\(S=R_1\sqcup R_2\) with \(|R_1|=|R_2|=s\).  Because the entire set \(S\) is
a Golomb ruler, the two positive difference spectra

\[
 \{|u-v|:u,v\in R_1,\ u\ne v\},\qquad
 \{|u-v|:u,v\in R_2,\ u\ne v\}                  \tag{2}
\]

are internally unique and disjoint from one another.

For an integer \(C\), put

\[
 A_C=\{(u,0):u\in R_1\}
      \cup\{(0,C+v):v\in R_2\}.                 \tag{3}
\]

There is an integer \(C\) for which \(A_C\) is distance-Sidon.  Indeed, its
internal horizontal and vertical squared distances are distinct constants by
(2).  A cross squared distance is the polynomial

\[
 u^2+(C+v)^2=C^2+2vC+(u^2+v^2).                 \tag{4}
\]

Two different cross edges give different polynomials: equality of their
linear coefficients gives \(v=v'\), and then equality of constants gives
\(u=u'\), since all marks are nonnegative.  A polynomial (4) is also not
identical to any internal constant.  The finite collection of pairwise
differences of these polynomials is nonzero, so only finitely many real
values of \(C\) cause a collision.  Choose any integer outside that finite
set.  Translation if necessary puts (3) inside an integer square.

The offset can be controlled almost optimally.  Take (C>L), so every cross
distance is larger than every internal distance.  If two different cross
edges collide, then for some (u_1,u_2\in R_1) and (v_1,v_2\in R_2),

\[
 u_1^2+(C+v_1)^2=u_2^2+(C+v_2)^2.              \tag{5}
\]

When (v_1\ne v_2), integrality of the resulting value of (C) implies

\[
 |v_1-v_2|\mid |u_2^2-u_1^2|.                  \tag{6}
\]

For a fixed unordered horizontal pair, the integer on the right is at most
(L^2) and has only (L^{o(1)}) divisors.  Since (R_2) is a Golomb ruler,
each positive vertical difference identifies at most one vertical pair.
Thus all cross/cross comparisons exclude only
(O(s^2L^{o(1)})=s^{2+o(1)}) integer values of (C).  One of the first that
many integers above (L) is admissible.  Consequently

\[
 C=s^{2+o(1)},\qquad A_C\subset[0,s^{2+o(1)}]^2. \tag{7}
\]

The standard bound
(\max_{r\le L^2}\tau(r)=\exp(O(\log L/\log\log L))=L^{o(1)}) is the only
number-theoretic input.  Computation with Erdos--Turan rulers usually finds
the very first or second integer above (L), but (7) is the rigorous scale
needed here.

## 2. Quadratic pointwise overlap

Let

\[
 \Delta_i=(R_i-R_i)\setminus\{0\},
 \qquad |\Delta_i|=s(s-1).
\]

The directed difference set \(D_A\) contains

\[
 X=\{(u,0):u\in\Delta_1\},\qquad
 Y=\{(0,v):v\in\Delta_2\}.                      \tag{8}
\]

For every \((u,v)\in\Delta_1\times\Delta_2\),

\[
 (u,0)+J(0,v)=(u-v,0).                           \tag{9}
\]

All \(|\Delta_1||\Delta_2|\) pairs in (9) land at one of at most \(4L+1\)
integer translations.  Moreover none lands at zero, since equality of an
oriented difference from \(R_1\) and one from \(R_2\) would repeat a
difference of the full Golomb ruler.  Hence some nonzero \(t\) satisfies

\[
 M_{A_C}(t)
 \ge \frac{s^2(s-1)^2}{4L+1}
 =\Omega(s^2)=\Omega(|A_C|^2).                  \tag{10}
\]

The reverse inequality \(M_A(t)\le |D_A|<|A|^2\) is trivial, so this is sharp
in its exponent.  Consequently there is no absolute \(\delta>0\) for which
the first estimate in (1) holds for all planar (or all lattice)
distance-Sidon sets.

## 3. Sixth-power cross-sum energy

Put \(B=A_C+JA_C\).  Distance-Sidon implies that this sum is direct.  Its
autocorrelation satisfies \(\rho_B(t)\ge M_{A_C}(t)\).  More strongly, applying
Cauchy--Schwarz to all values in (9) gives

\[
 \begin{split}
 E^+(B)
 &\ge \sum_{w\in\mathbb Z}
   |\{(u,v)\in\Delta_1\times\Delta_2:u-v=w\}|^2\\
 &\ge \frac{|\Delta_1|^2|\Delta_2|^2}{4L+1}
 =\Omega(s^6)=\Omega(|A_C|^6).                  \tag{11}
 \end{split}
\]

Since every set of size \(|B|=|A_C|^2\) has additive energy at most
\(|B|^3=|A_C|^6\), (11) is maximal up to constants.  Thus even the rigid
identity between the summands \(A\) and \(JA\), together with full radial
uniqueness of \(A-A\), does not yield a power saving in the cross-sum energy.

## 4. Fourth-power rotated triple energy

The obstruction also saturates the direct energy of

\[
 \Phi(a,b,c)=a+J(b-c),\qquad b\ne c.
\]

Restrict \(a=(u,0)\) to the horizontal arm and take
\(b=(0,C+v)\), \(c=(0,C+w)\) to be distinct points of the vertical arm.  Then

\[
 \Phi(a,b,c)=(u+w-v,0).                          \tag{12}
\]

There are \(s^2(s-1)\) such ordered triples and their images occupy at most
\(3L+1=O(s^2)\) lattice points.  Cauchy--Schwarz gives

\[
 \mathcal T_J(A_C)
 \ge {s^4(s-1)^2\over 3L+1}
 =\Omega(s^4)=\Omega(|A_C|^4).                  \tag{13}
\]

Every fibre of \(\Phi\) is a matching in each coordinate, so its size is at
most \(|A|\); with \(O(|A|^3)\) inputs this gives the universal upper bound
\(\mathcal T_J(A)=O(|A|^4)\).  Hence (13) is sharp in its exponent.  In
particular, the proposed estimate
\(\mathcal T_J(A)\le |A|^{3+o(1)}\) is false.

## 5. Consequence for the research programme

The support-count implication in `CROSS_TRANSLATION_OVERLAP.md` remains
correct, but its size-only hypothesis is false as strongly as possible.  The
same is true of both the cross-energy sufficient condition and the direct
size-only rotated-triple target in `ROTATED_TRIPLE_ENERGY.md`.  A
density-sensitive estimate remains logically possible.  The raw additive
triple count in the *realized difference set* \(A-A\), discussed in
`RADIAL_ADDITIVE_TRIPLE_AUDIT.md`, is not falsified by this example and is now
the cleaner surviving grid route.

The scale (7) also closes the most natural ambient-monomial escape.  If a
bound

\[
 \max_t M_A(t)\ll m^{\alpha+o(1)}k^{\beta+o(1)}
\]

held with nonnegative \(\alpha,\beta\), this family would force
(2\alpha+\beta\ge2).  But the support argument reaches
(k\le m^{2/3+o(1)}) only when (3\alpha+2\beta\le2).  These two half-planes
are disjoint in the nonnegative quadrant.  Thus no such monomial pointwise
overlap theorem can settle the grid problem.

For the rotated triple energy, a monomial bound
(\mathcal T_J(A)\ll m^{\alpha+o(1)}k^{\beta+o(1)}) is forced by this family
to satisfy (2\alpha+\beta\ge4), while the cube-root implication requires
(3\alpha+2\beta\le6).  The only boundary point with
(\alpha,\beta\ge0) is

\[
 \boxed{\mathcal T_J(A)\ll m^{2+o(1)}}.          \tag{14}
\]

So (14), or a genuinely non-monomial density dichotomy with the same dense
consequence, is the sharp surviving rotated-energy target.  The obstruction
itself saturates (14).
