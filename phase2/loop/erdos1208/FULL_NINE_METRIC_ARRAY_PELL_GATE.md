# The full nine-entry metric array: Pell-small cells but no ambient compression

## 1. Verdict

Let `T,U` be disjoint triples in an integral distance-Sidon set, with the
same sum.  Order the three squared side lengths of each triangle increasingly:

\[
 \ell_1<\ell_2<\ell_3,
 \qquad r_1<r_2<r_3.                                    \tag{1.1}
\]

The full nine-anchor metric array is

\[
 \Phi(T,U)=(\phi_{ij})_{1\le i,j\le3},
 \qquad \phi_{ij}=\ell_i+18r_j.                          \tag{1.2}
\]

Keeping all nine entries produces a genuine arithmetic gain:

\[
 \boxed{
 \max_\Phi|\{(T,U):\Phi(T,U)=\Phi\}|\le m^{o(1)}.}       \tag{1.3}
\]

More explicitly, every cell injects into the integer solutions in an
`O(m^2)` box of one generalized Pell equation

\[
 X^2-3Y^2=K,                                             \tag{1.4}
\]

where `0<K=O(m^4)` is fixed by the row differences of the array.  Ideal
factorization in `Z[sqrt(3)]` gives a bound

\[
 O\!\left(\tau(K^2)^2\log(2m)\right).                   \tag{1.5}
\]

This is the first uniform multiplicity theorem for the nine-anchor metric
repair.  Exact injectivity is false: a 12-point distance-Sidon set in
general position has two different equal-centroid records with exactly the
same full array.

However, (1.3) does **not** prove the ambient centroid theorem.  The array
has five effective scalar degrees: it is determined by `phi_11`, two row
differences, and two column differences.  The resulting a priori support is
`O(m^10)`, not `O(m^2)`.  In fact,
there are polynomial-height distance-Sidon sets carrying `Omega(k^4)`
ordered equal-centroid records; by (1.3), these occupy
`k^(4-o(1))` distinct full arrays.  Thus pointwise joint-array rigidity and
global distance-label injectivity do not supply the missing compression.

The exact remaining gate is a projection/entropy inequality which charges
the many different Pell parameters back to an `O(m^2)` universe.  Without
such an inequality, the full array is an excellent decoder but not an
ambient charge.

## 2. Why the full array has Pell-small cells

Fix one valid array (1.2), and write

\[
 x=\ell_1,
 \qquad a=\ell_2-\ell_1,
 \qquad b=\ell_3-\ell_1.                                 \tag{2.1}
\]

The array fixes `a,b`, since

\[
 a=\phi_{21}-\phi_{11},
 \qquad b=\phi_{31}-\phi_{11}.                           \tag{2.2}
\]

Only the common shift `x` remains unknown on the first triangle.  Let `D`
be its signed doubled area.  Heron's identity in squared-side variables is

\[
 4D^2
 =2\sum_{i<j}\ell_i\ell_j-\sum_i\ell_i^2.              \tag{2.3}
\]

Substituting `(x,x+a,x+b)` and completing the square gives the exact norm
equation

\[
 \boxed{
 (3x+a+b)^2-12D^2=4(a^2-ab+b^2).}                        \tag{2.4}
\]

Thus (1.4) holds with

\[
 X=3x+a+b,
 \qquad Y=2D,
 \qquad K=4(a^2-ab+b^2).                                 \tag{2.5}
\]

All side lengths in a distance-Sidon triangle are distinct, so `a,b` are
positive and unequal and hence `K>0`.  Also `K=O(m^4)` and
`|X|,|Y|=O(m^2)`.

It remains to count (1.4).  In the quadratic integer ring
`O=Z[sqrt(3)]`, every solution gives

\[
 (X+Y\sqrt3)(X-Y\sqrt3)=K.                               \tag{2.6}
\]

The principal ideal `(X+Y sqrt(3))` is an ideal divisor of `(K)`.  The
number of ideal divisors is at most `tau(K^2)^2`.  For a fixed principal
ideal, all generators of norm `K` differ by a norm-one unit.  These units
are \(\pm(2+\sqrt3)^n\); only `O(log(2m))` exponents can keep both
coefficients in the box `O(m^2)`.  This proves (1.5).

Finally, a value of `x` fixes all three `ell_i`.  Global distance
injectivity identifies the three underlying edges, and they determine `T`
if they form a triangle.  The fixed array then gives

\[
 r_j={\phi_{1j}-x\over18},                                \tag{2.7}
\]

so distance injectivity likewise determines `U`.  Hence every Pell solution
produces at most one ordered record.  This proves (1.3).

The argument is insensitive to vertex names: ordering by the three distinct
opposite-side lengths is the canonical quotient by the \(S_3\times S_3\)
symmetry.

## 3. Exact injectivity is false

The following twelve points form a distance-Sidon set with maximum
collinearity two:

\[
\begin{aligned}
&(-12,-3),(5,5),(7,-2),(9,-12),(-11,2),(2,10),\\
&(-26,-29),(-13,-9),(-3,-22),(-4,-31),(-24,-20),(-14,-9).
\end{aligned}                                             \tag{3.1}
\]

A common translation places them in a square of side `41`.  Put

\[
\begin{aligned}
 T_0&=\{0,1,2\},&U_1&=\{3,4,5\},\\
 T_1&=\{6,7,8\},&U_0&=\{9,10,11\},
\end{aligned}                                             \tag{3.2}
\]

using the order in (3.1).  The first pair has common sum `(0,0)` and the
second common sum `(-42,-60)`.  Their sorted squared side labels are

\[
\begin{array}{c|ccc}
T_0&53&353&362\\
T_1&269&569&578\\
U_0&221&521&584\\
U_1&233&533&596
\end{array}.                                               \tag{3.3}
\]

The shifts are

\[
 \ell(T_1)=\ell(T_0)+216(1,1,1),
 \qquad
 r(U_1)=r(U_0)+12(1,1,1),                                \tag{3.4}
\]

and `216=18*12`.  Therefore

\[
 \Phi(T_0,U_1)=\Phi(T_1,U_0)                             \tag{3.5}
\]

with common flattened array

\[
 (4247,9647,10781, 4547,9947,11081,
  4556,9956,11090).                                      \tag{3.6}
\]

The full set has three unordered equal-centroid pairs.  After orienting
them there are six records, five arrays, joint energy eight, and maximum
load two.  This is a genuine metric collision, not a formal side-label
model.

## 4. A fourth-order consistent array patch

The Pell theorem controls one cell, but not the number of occupied cells.
The distinction is genuine.  For an odd prime `p`, let

\[
 P_p=\{(x,[x^2]_p):0\le x<p\}.                            \tag{4.1}
\]

As in `EQUAL_AREA_TRIANGLE_ENERGY_BARRIER.md`, this is vector-Sidon and has
no collinear triple.  There are `T=binom(p,3)` unordered triangles, while
their exact vector sums occupy fewer than `9p^2` values.  If `t_s` is the
number of triangles of sum `s`, then

\[
 \sum_s\binom{t_s}{2}
 \ge {1\over2}\left({T^2\over9p^2}-T\right)
 =\Omega(p^4).                                            \tag{4.2}
\]

The last equality holds for all sufficiently large `p`.  Equal-sum
triangles are automatically disjoint: if they shared a point, pair-sum
injectivity would identify their remaining two points.

Apply the polynomial-height unimodular Euclideanization lemma from the same
note.  It produces a distance-Sidon image `A_p` of height `O(p^5)`, while
preserving all triple sums.  Hence `A_p` has `Omega(p^4)` ordered disjoint
equal-centroid records.  By (1.3), these records occupy

\[
 \boxed{p^{4-o(1)}}                                      \tag{4.3}
\]

different full metric arrays.

This is the promised consistent multi-coordinate patch.  It does not
disprove the ambient centroid conjecture: the polynomial height pays for
it.  It does prove that near-injectivity of the full array cannot by itself
yield the conjecture.  An entropy argument must use the actual ambient
sizes of the varying shape parameters, not just the cell loads.

## 5. Stress audit

With canonical side ordering, the exact profiles

\[
 (k,m,C,\text{oriented mass},|\operatorname{supp}\Phi|,
   \mathcal E_\Phi,\max\nu)
\]

are

\[
\begin{array}{c|rrrrrrr}
\text{closure-40}&40&223&690&1380&1380&1380&1\\
\text{Costas-22}&22&131&519&1038&1038&1038&1\\
\text{parabola-43}&43&2586&10571&21142&21142&21142&1\\
\text{planted-14}&14&87631682&3&6&6&6&1\\
\text{collision-12}&12&41&3&6&5&8&2
\end{array}.                                               \tag{5.1}
\]

Every record in the audit satisfies the Pell identity (2.4) exactly.  Run

```text
python3 phase2/loop/erdos1208/verify_full_nine_metric_array_pell_gate.py
```

for all distance, centroid, canonical-array, collision, side-shift, Heron,
Pell, collinearity, and profile checks.

## 6. Research consequence

The full `3 by 3` repair succeeds at its narrowest intended job: it reduces
every charge cell to divisor multiplicity.  It fails at the next step
because its occupied support can be fourth-order.  Therefore neither
"choose one scalar entry" nor "keep all nine entries" resolves the ambient
centroid theorem:

* one entry has genuine polynomially heavy fibres;
* all nine entries have Pell-small fibres but too many distinct keys.

The remaining viable statement must interpolate between them: a
size-biased projection theorem bounding the number of occupied shape
parameters over each `O(m^2)` scalar charge, or an endpoint theorem showing
that the fourth-order modular patch necessarily incurs enough geometric
height.  The pointwise nine-array multiplicity problem itself is now closed.
