# Orthogonal two-support product for parallel-line covers

## 1. Theorem

Let `A` be a planar distance-Sidon set of size `k`, put

\[
 D=A-A,qquad N=|D|=k(k-1)+1,
\]

and let `J` be a quarter-turn.  Suppose that `A` is contained in `r`
parallel lines.  Then

\[
 \boxed{
 |D+D|\,|D+JD|
 \ge (2N-1)\left(1+{k^2\over r}-k\right)^2.}    \tag{1.1}
\]

In particular, if `r=k^{o(1)}`, then

\[
 |D+D|\,|D+JD|\ge N^{3-o(1)}.                   \tag{1.2}
\]

Thus the full orthogonal product theorem, and hence the cube-root grid upper
bound, already holds for every subpolynomial parallel-line cover.  This is a
direct proof inside the new two-support framework.  It is stronger by one
factor of roughly `k/r` than applying the older
`PARALLEL_LINE_SUPPORT_LEMMA.md` only to `A+J(A-A)`.

## 2. The within-line difference set

Choose orthonormal coordinates in which the covering lines are horizontal.
Let their occupancies be `k_h`, so

\[
 \sum_hk_h=k.
\]

Define the scalar within-line directed-difference set

\[
 H=\{x-x':(x,h),(x',h)\in A\text{ for some }h\}. \tag{2.1}
\]

Every nonzero value in (2.1) has one ordered representation.  Otherwise two
different edges of `A` would have the same vector, and hence the same positive
length.  Therefore

\[
 |H|=1+\sum_hk_h(k_h-1)
     =1+\sum_hk_h^2-k.                           \tag{2.2}
\]

Cauchy--Schwarz across the `r` occupied lines gives

\[
 h_0:=|H|\ge1+{k^2\over r}-k.                   \tag{2.3}
\]

Regarded as horizontal vectors, `H` is a subset of `D`, while `JH` is a
vertical subset of `JD`.

## 3. Fibrewise growth of `D+JD`

For every occupied horizontal coordinate `x` in the vector set `D`, let

\[
 V_x=\{y:(x,y)\in D\}.
\]

The horizontal subset `H subset D` shows that the number `p` of nonempty
fibres `V_x` is at least `h_0`.  Restrict `D+JD` to sums of `D` with the
vertical copy `JH`.  Different horizontal fibres remain disjoint, and the
one-dimensional sumset inequality gives

\[
 \begin{aligned}
 |D+JD|
 &\ge\sum_x|V_x+H|\\
 &\ge\sum_x(|V_x|+h_0-1)\\
 &=N+p(h_0-1)\\
 &\ge N+h_0(h_0-1)\ge h_0^2,                    \tag{3.1}
 \end{aligned}
\]

where the last inequality uses `N>=h_0` because the horizontal copy of `H`
lies inside `D`.

For every nonempty finite subset of a torsion-free abelian group,

\[
 |D+D|\ge2N-1.                                  \tag{3.2}
\]

Multiplying (3.1)--(3.2) and using (2.3) proves (1.1).

## 4. Relation to the remaining case

The theorem handles the exact obstruction which killed the unsplit moment
proof: one or several dense Golomb-ruler layers.  Their ordinary support can
be small, but the entire complete difference set `D`, translated by the
rotated within-line differences, supplies the missing quadratic factor.

It does not settle configurations occupying a fixed positive power of `k`
parallel layers in every direction.  In that regime (2.3) loses the same
power in (1.1).  The live global energy--support theorem from
`ORTHOGONAL_ENERGY_SUPPORT_GATE.md` must either control that wide case or
produce a new direction with a smaller effective cover.

## 5. Verification

`verify_orthogonal_product_parallel_cover.py` checks every identity and
inclusion on two exact distance-Sidon families:

* a ten-point Golomb ruler on one line, where `N=h_0=91` and
  `|D+JD|=91^2` exactly;
* the 40-point dense perpendicular-ruler witness, where `N=1,561`,
  `h_0=381`, and `|D+JD|=1,413,381`.

All computations use integer arithmetic.
