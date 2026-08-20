# Polynomial rich-pencil counterexample to the fixed-wedge scalar gate

## 1. Verdict

The rich-restricted pointwise gate proposed in
`LOW_BAND_FIXED_WEDGE_WEIGHT_GATE.md` is false by a full factor of `k`, even
for genuine integral distance-Sidon sets of polynomial height and with the
sharp determinant cutoff `L=N`.

More precisely, for every sufficiently large `s` there is an integral
distance-Sidon set `A_s` with

\[
 k=11s+1,\qquad m=s^{O(1)},\qquad N={k\choose2},          \tag{1.1}
\]

and a physical endpoint wedge `w` such that

\[
 \boxed{F_{N,k}(w)\ge6s^2=\Omega(k^2).}                 \tag{1.2}
\]

Every displayed contribution in (1.2) has target richness
`U_N(r)>=k`, both fixed-wedge cross determinants exceed `N`, and the source
weight is the exact dilate `R_D(-18r)`.  Therefore neither Gaussian divisor
bounds nor the rich cutoff can prove

\[
 F_{L,T}(w)\le m^{o(1)}k.                                \tag{1.3}
\]

The same construction supplies `binom(6s,2)` such wedges at one endpoint,
so its rich-restricted joint moment satisfies

\[
 \boxed{J_N^{\rm rich}\ge {6s\choose2}6s^2=\Omega(k^4)
       =\Omega(Nk^2).}                                   \tag{1.4}
\]

Thus the desired *global* `m^(o(1))Nk^2` moment remains possible but is
sharp at polynomial height.  What fails decisively is localization followed
by a uniform pointwise bound.  Any viable proof must average over physical
wedges while allowing quadratic exceptional perpendicular pencils.

## 2. The five-mark vertical identity

For every positive integer `t`, put

\[
 y=10t,\quad a=24t,\quad b=26t,\quad c=55t,\quad d=35t.
                                                                    \tag{2.1}
\]

Then the two exact square identities are

\[
 \boxed{a^2-b^2=-y^2,\qquad c^2-d^2=18y^2.}             \tag{2.2}
\]

The six marks

\[
 \{0,10,24,26,35,55\}t                                 \tag{2.3}
\]

form a Golomb ruler: their fifteen positive differences are

\[
 2,9,10,11,14,16,20,24,25,26,29,31,35,45,55             \tag{2.4}
\]

times `t`, and are all distinct.

We require `s` copies of (2.3) sharing zero.  They can be packed into one
polynomial-span Golomb ruler.  Inductively, suppose `O(j)` marks have been
chosen.  Adding the five marks in (2.1) can fail the Golomb property only
when:

* a new mark equals an old mark;
* a new internal difference equals an old difference;
* a new--old difference equals an old or new internal difference; or
* two new--old differences are equal.

After deleting repetitions of the same unordered pair, every such equality
is a nonzero linear equation in `t`.  There are `O(j^3)` equations, hence at
most `O(j^3)` forbidden integer values.  Choosing the first admissible
positive integer gives `t_j=O(j^3)` and a vertical Golomb ruler

\[
 V=\{0\}\cup\bigcup_{j=1}^s
 \{10t_j,24t_j,26t_j,35t_j,55t_j\}                      \tag{2.5}
\]

of size `5s+1` and polynomial span.

## 3. The perpendicular distance-Sidon set

Let `R={rho_1,...,rho_(6s)}` be a `6s`-mark dense Golomb ruler of span
`O(s^2)`.  Choose a positive integer scale `lambda` such that no difference
of `lambda R` equals a difference of `V`.  There are only polynomially many
forbidden integer values of `lambda`, so `lambda=s^{O(1)}` is possible.

For a further integer `Z`, define horizontal marks

\[
 h_i=Z+\lambda\rho_i                                    \tag{3.1}
\]

and the two-axis set

\[
 \boxed{
 A_s=\{(h_i,0):1\le i\le6s\}
       \cup\{(0,v):v\in V\}.}                           \tag{3.2}
\]

It has `k=6s+(5s+1)=11s+1` points.

There is a polynomial-size `Z>N` for which (3.2) is distance-Sidon.  The
horizontal and vertical internal spectra are already separately distinct,
and the choice of `lambda` makes them disjoint.  A cross distance is

\[
 (Z+\lambda\rho_i)^2+v^2.                               \tag{3.3}
\]

For two different cross edges, equality of (3.3) is a nonzero linear
equation in `Z` if their horizontal marks differ; if those marks agree,
distinct nonnegative vertical marks have distinct squares.  Equality of a
cross distance with an internal distance is a nonzero quadratic equation in
`Z`.  There are `O(k^4)` comparisons and at most two roots per comparison,
so one of `O(k^4)` consecutive integers above the polynomial starting point
is admissible.  Hence `m=s^{O(1)}`.

The same choice can ensure unique unordered pair sums.  Within either axis
this follows from the Golomb property; cross sums are coordinatewise unique.
The only remaining possible collision uses the vertical mark zero and a
horizontal pair sum, and excludes one further value of `Z` per comparison.

## 4. Every planted shift is rich

Write `O=(0,0)` and `Y_j=(0,10t_j)`.  For every horizontal point
`H_i=(h_i,0)`, the two cross-edge pairs

\[
 (H_iO,H_iY_j),\qquad
 \bigl(H_i(0,24t_j),H_i(0,26t_j)\bigr)                  \tag{4.1}
\]

have the same squared-distance gap

\[
 r_j=-(10t_j)^2.                                         \tag{4.2}
\]

The first doubled determinant in (4.1) has magnitude `20h_i t_j`; the
second has magnitude `4h_i t_j`.  Since `Z>N`, all exceed `N`.  Therefore

\[
 \boxed{U_N(r_j)\ge2(6s)=12s\ge11s+1=k.}                \tag{4.3}
\]

Likewise (2.2) gives, for every horizontal point, the source pair

\[
 \bigl(H_i(0,55t_j),H_i(0,35t_j)\bigr)                  \tag{4.4}
\]

with gap

\[
 -18r_j=18(10t_j)^2.                                    \tag{4.5}
\]

Thus

\[
 \boxed{R_D(-18r_j)\ge6s.}                              \tag{4.6}
\]

This is the exact place where fixed-cell Gaussian factorization is
insufficient: the `6s` records in (4.4) occupy changing determinant cells
along one perpendicular pencil.

## 5. Quadratic fixed-wedge weight

Fix two horizontal points `H_1,H_2` and let `w` be the physical wedge
`(O;OH_1,OH_2)`.  For each `j`, use the partner edges

\[
 H_1Y_j,\qquad H_2Y_j.                                   \tag{5.1}
\]

Their norm difference equals

\[
 (h_1^2+y_j^2)-(h_2^2+y_j^2)=h_1^2-h_2^2,              \tag{5.2}
\]

which is the norm difference of the two fixed edges.  Their common shift is
`r_j=-y_j^2`, and both fixed/partner doubled determinants are larger than
`N`.  Equations (4.3)--(4.6) show that every `j` survives the rich cutoff
`T=k` and contributes at least `6s` to `F_(N,k)(w)`.  Hence

\[
 F_{N,k}(w)\ge\sum_{j=1}^sR_D(-18r_j)\ge6s^2,           \tag{5.3}
\]

proving (1.2).  The same argument applies independently to every unordered
pair of the `6s` horizontal points, proving (1.4).

## 6. Exact finite certificate

The verifier uses `s=3`.  Its greedy vertical parameters are

\[
 (t_1,t_2,t_3)=(1,14,33),                                \tag{6.1}
\]

and it constructs

\[
 k=34,\quad N=561,\quad \lambda=17,\quad Z=11051,
 \quad m=22101.                                          \tag{6.2}
\]

All 561 squared distances and all 561 unordered pair sums are distinct.
For each planted shift it finds

\[
 U_N(r_j)=36,\qquad R_D(-18r_j)=19.                      \tag{6.3}
\]

The selected wedge has exact rich-restricted weight `57`, versus the
planted lower bound `54`.  The full rich joint moment is `36936`, versus the
certified planted lower bound `8262` from the horizontal wedges at `O`.

Run

```text
PYTHONPATH=phase2/loop/erdos1208 \
python3 phase2/loop/erdos1208/verify_low_band_fixed_wedge_rich_pencil_counterexample.py
```

## 7. Consequence for the low band

The exact localization

\[
 J_L^{\rm rich}=\sum_wF_{L,T}(w)                         \tag{7.1}
\]

remains useful bookkeeping, but the proposed uniform estimate for its
summands is closed.  Polynomial height, distance-Sidonicity, high
determinant, exact `-18` dilation, and target richness can all coexist with
`F_(N,k)(w)=Omega(k^2)`.

The surviving statement has to be genuinely averaged.  At the exponent
level the construction saturates, rather than contradicts,

\[
 \sum_wF_{L,T}(w)\le m^{o(1)}Nk^2.                       \tag{7.2}
\]

Accordingly the next useful target is a classification/charge theorem for
quadratic perpendicular pencils, or a global bound which pays their
`Omega(k^2)` local weights using the fact that only `O(k^2)` physical wedges
can lie in one such pencil.
