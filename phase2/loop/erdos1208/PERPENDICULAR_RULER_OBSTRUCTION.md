# Perpendicular rulers kill size-only rotated-overlap bounds

This note gives a genuine distance-Sidon obstruction to both proposed
size-only estimates

\[
 \max_t M_A(t)\le |A|^{2-\delta}
 \quad\text{and}\quad
 E^+(A+JA)\le |A|^{6-\delta}.                    \tag{1}
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

## 2. Quadratic pointwise overlap

Let

\[
 \Delta_i=(R_i-R_i)\setminus\{0\},
 \qquad |\Delta_i|=s(s-1).
\]

The directed difference set \(D_A\) contains

\[
 X=\{(u,0):u\in\Delta_1\},\qquad
 Y=\{(0,v):v\in\Delta_2\}.                      \tag{5}
\]

For every \((u,v)\in\Delta_1\times\Delta_2\),

\[
 (u,0)+J(0,v)=(u-v,0).                           \tag{6}
\]

All \(|\Delta_1||\Delta_2|\) pairs in (6) land at one of at most \(4L+1\)
integer translations.  Moreover none lands at zero, since equality of an
oriented difference from \(R_1\) and one from \(R_2\) would repeat a
difference of the full Golomb ruler.  Hence some nonzero \(t\) satisfies

\[
 M_{A_C}(t)
 \ge \frac{s^2(s-1)^2}{4L+1}
 =\Omega(s^2)=\Omega(|A_C|^2).                  \tag{7}
\]

The reverse inequality \(M_A(t)\le |D_A|<|A|^2\) is trivial, so this is sharp
in its exponent.  Consequently there is no absolute \(\delta>0\) for which
the first estimate in (1) holds for all planar (or all lattice)
distance-Sidon sets.

## 3. Sixth-power cross-sum energy

Put \(B=A_C+JA_C\).  Distance-Sidon implies that this sum is direct.  Its
autocorrelation satisfies \(\rho_B(t)\ge M_{A_C}(t)\).  More strongly, applying
Cauchy--Schwarz to all values in (6) gives

\[
 \begin{split}
 E^+(B)
 &\ge \sum_{w\in\mathbb Z}
   |\{(u,v)\in\Delta_1\times\Delta_2:u-v=w\}|^2\\
 &\ge \frac{|\Delta_1|^2|\Delta_2|^2}{4L+1}
 =\Omega(s^6)=\Omega(|A_C|^6).                  \tag{8}
 \end{split}
\]

Since every set of size \(|B|=|A_C|^2\) has additive energy at most
\(|B|^3=|A_C|^6\), (8) is maximal up to constants.  Thus even the rigid
identity between the summands \(A\) and \(JA\), together with full radial
uniqueness of \(A-A\), does not yield a power saving in the cross-sum energy.

## 4. Consequence for the research programme

The support-count implication in `CROSS_TRANSLATION_OVERLAP.md` remains
correct, but its size-only hypothesis is false as strongly as possible.  The
same is true of the cross-energy sufficient conditions in
`ROTATED_TRIPLE_ENERGY.md`.  The perpendicular-ruler construction can be very
sparse in its containing square because the collision-avoiding offset \(C\)
is not controlled at the critical scale.  Therefore a bound involving both
\(k=|A|\) and the ambient side length \(m\), or a direct estimate of the
rotated triple energy which is not routed through \(E^+(A+JA)\), remains
possible.
