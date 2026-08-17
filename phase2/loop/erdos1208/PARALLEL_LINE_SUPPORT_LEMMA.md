# Parallel-line support lemma for Erdős #1208

## Plain-language summary

The rotated-support conjecture is already true whenever the point set is
concentrated on only subpolynomially many parallel lines.  More precisely, if
a distance-Sidon set of `k` points is contained in `r` parallel lines, then
`|A+JA-JA| >= k^3/r^2-O(k^2/r)`.  The proof is elementary but uses the full
distance condition: all directed differences occurring within the parallel
lines are globally distinct.  This closes the line-structured branch that was
left informal in `ROTATED_TRIPLE_SUPPORT.md`; the unresolved branch is now
genuinely transverse.

## 1. Exact direction-sensitive statement

Let `A` be a finite distance-Sidon subset of the Euclidean plane, let
`k=|A|`, and let `J` be rotation through 90 degrees.  Fix a direction `v` and
write the lines parallel to `v` as `L_h`.  Put

\[
 k_h=|A\cap L_h|,
 \qquad Q_v=\sum_h k_h(k_h-1).
\]

Let `p_v` be the number of distinct orthogonal projections of the points of
`A` onto a line parallel to `v`.  Then

\[
 \boxed{|A+JA-JA|\ge k+p_vQ_v.}                 \tag{1.1}
\]

This statement does not require `A` to be a lattice set.

## 2. Proof

Choose orthonormal coordinates in which `v` is horizontal, so a point of `A`
has coordinates `(x,h)` and `L_h` is the horizontal line at height `h`.
Consider the set of directed within-line differences

\[
 \Delta_v=\{x_b-x_c:(x_b,h),(x_c,h)\in A
              \text{ for some }h\}.
\]

The zero difference occurs once as a value.  Every nonzero directed
difference in this display occurs for exactly one ordered pair.  Indeed, two
different pairs giving the same directed difference would determine equal
positive Euclidean distances, contrary to the distance-Sidon property.
Consequently

\[
 |\Delta_v|=1+Q_v.                                \tag{2.1}
\]

Restrict the triples in `A+J(A-A)` to those for which `b,c` lie on a common
line parallel to `v`.  Since

\[
 J(b-c)=(0,x_b-x_c),
\]

their outputs form

\[
 S_v=\{(x,h+d):(x,h)\in A,\ d\in\Delta_v\}
       \subseteq A+JA-JA.                         \tag{2.2}
\]

For each occupied horizontal coordinate `x`, let

\[
 H_x=\{h:(x,h)\in A\}.
\]

The fibres in (2.2) having different first coordinate are disjoint.  The
one-dimensional sumset inequality for finite subsets of the real line gives

\[
 |H_x+\Delta_v|\ge |H_x|+|\Delta_v|-1
                  =|H_x|+Q_v.                    \tag{2.3}
\]

Summing (2.3) over the `p_v` occupied first coordinates proves

\[
 |S_v|\ge\sum_x|H_x|+p_vQ_v=k+p_vQ_v,
\]

which is (1.1).

## 3. Parallel-cover consequence

Suppose `A` is contained in `r` lines parallel to `v`, empty lines omitted.
By Cauchy--Schwarz,

\[
 Q_v=\sum_h k_h^2-k\ge \frac{k^2}{r}-k.          \tag{3.1}
\]

Every one of those lines contains at most `p_v` points, so

\[
 p_v\ge\max_h k_h\ge \frac{k}{r}.                \tag{3.2}
\]

Substitution in (1.1) yields the explicit bound

\[
 \boxed{|A+JA-JA|
  \ge \frac{k^3}{r^2}-\frac{k^2}{r}+k.}          \tag{3.3}
\]

In particular, if `r=k^{o(1)}`, then

\[
 |A+JA-JA|\ge k^{3-o(1)}.                        \tag{3.4}
\]

Thus any counterexample to the rotated-support conjecture with a fixed power
loss must occupy a fixed positive power of `k` parallel lines in every
direction used to cover it.  A single line containing `L` points also gives
the useful special case

\[
 |A+JA-JA|\ge k+L^2(L-1),                        \tag{3.5}
\]

by choosing its direction in (1.1).

## 4. Scope and next gate

This lemma rigorously handles the perpendicular-ruler obstruction: choosing
the direction of either arm recovers a constant multiple of `k^3` from the
restricted triples.  It also handles any union of `k^{o(1)}` parallel layers.

It does **not** resolve the transverse case.  A set may occupy many parallel
lines while still having only small line occupancies, and (1.1) then becomes
subcubic.  The exact remaining collision gate is as follows.

Put `D=A-A`.  For any `D_0 subset D`, consider the blocks

\[
 L_d=A+Jd,\qquad d\in D_0,
\]

and let

\[
 E(D_0)=\#\big\{\{d,d'\}\subset D_0:
                    J(d'-d)\in D\big\}.          \tag{4.1}
\]

Two different blocks meet in at most one point, and they meet exactly under
the condition in (4.1).  Retain every block independently with probability
`rho`.  The first two Bonferroni terms give

\[
 |A+JD|\ge \rho k|D_0|-\rho^2E(D_0)              \tag{4.2}
\]

for at least one retained family.  Optimizing `rho` proves

\[
 |A+JD|\ge
 \min\left\{\frac{k|D_0|}{2},
             \frac{k^2|D_0|^2}{4E(D_0)}\right\}, \tag{4.3}
\]

where the second term is omitted when `E(D_0)=0`.  In particular,

\[
 |D_0|=k^{2-o(1)},\qquad E(D_0)\le k^{3+o(1)}     \tag{4.4}
\]

imply the full `k^{3-o(1)}` support theorem.

There is a useful exact split of (4.1).  Call a collision *parallel* if
`d,d'` lie on the same line through the origin, and *transverse* otherwise.
If `L` is the largest number of collinear points of `A`, then every direction
contains at most `k(L-1)` nonzero oriented differences.  Since the total
number of such differences is `k(k-1)`, the number of parallel collision
pairs is at most

\[
 \frac12\sum_v |D\cap v|^2
 \le \frac12 k^2(k-1)(L-1).                     \tag{4.5}
\]

Thus parallel collisions already have the desired `k^{3+o(1)}` scale when
`L=k^{o(1)}`.  The genuinely new statement is the transverse estimate

\[
E_{\mathrm{trans}}(A)\le k^{3+o(1)}.            \tag{4.6}
\]

`TRANSVERSE_LOCAL_GATE.md` sharpens (4.6) to a local overlap problem.  For

\[
 m_{\rm tr}(d)=\#\{e\in D\setminus\{0\}:d-Je\in D,\ d\cdot e\ne0\},
\]

there is the exact identity

\[
 2E_{\rm trans}(A)=\sum_{d\in D}m_{\rm tr}(d).   \tag{4.6a}
\]

Since `|D|=k^2-k+1`, the sufficient local gate
`max_d m_tr(d)<=k^(1+o(1))` implies (4.6).  The dot-product restriction is
essential: it deletes exactly the quadratic local overlaps in the
perpendicular-ruler obstruction.  The note supplies an exact verifier, a
targeted falsification search, and the secondary sufficient condition that
the transverse graph have at most `k^(4+o(1))` four-cycles.

For wide point sets, (4.5) can be replaced by a much stronger existing
theorem.  Elekes, *Trapezoids and Deltoids in Wide Planar Point Sets*, Graphs
and Combinatorics 35 (2019), Theorem 1, proves that the number of trapezoids is
`O(k^3 log^2 k)` whenever at most `sqrt(k) log k` points are collinear.  A pair
of parallel segments is precisely the choice defining a trapezoid, up to
harmless degeneracies and constant multiplicities.  Parallel collision pairs
are a subfamily of these pairs.  Therefore

\[
 E_{\mathrm{parallel}}(A)=O(k^3\log^2 k)
 \quad\text{when}\quad L\le\sqrt{k}\log k.       \tag{4.7}
\]

Consequently, (4.6) would prove the full rotated-support theorem throughout
the wide regime `L<=sqrt(k)log k`, without any additional parallel-direction
work.  This use of the trapezoid theorem is prior art plus the present
reduction, not a new trapezoid bound.

The current computations support (4.6): compact annealed witnesses have
`E_trans/k^3` between roughly `0.38` and `0.41`, while the perpendicular-ruler
stress witnesses tested here have only parallel collisions.  Unstretched Welch Costas arrays violate
(4.6) by a growing factor, but they repeat Euclidean norms; the smallest
integral stretch separating all norms collapses their transverse collision
ratio toward zero.  This is a viability check, not a proof.

Equation (4.6) plus (4.7) would finish the wide case.  Larger polynomial line
richness still requires coupling (4.6) to the line bound (1.1), rather than
taking the better of two independent estimates.  No such coupling and no
proof of (4.6) are currently known.  A kill family for this
route is now pre-registered: distance-Sidon sets with `L=k^{o(1)}` and
`E_trans >= k^{3+epsilon}` for a fixed `epsilon>0`.
