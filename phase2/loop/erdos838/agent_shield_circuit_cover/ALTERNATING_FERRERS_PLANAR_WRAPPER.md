# Alternating Ferrers ears are planar, but the lexicographic wrapper cannot go below one half

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The alternating Ferrers regression from
`agent_common_shield_mixing/CYCLIC_FERRERS_PROFILE_TRANSFER.md` has a
literal planar singleton-ear realization.  This remains true after every
macro label is replaced by an arbitrarily small projectively universal
child.  Thus planarity alone does not align the rich profiles on the
**original** adjacent seams.

However, the natural lexicographic child realization cannot suppress all
one-gap banks.  Alternation itself makes the obstruction disappear after
one cell is omitted: the two new gap endpoints have the same parity and
their rich halves align.  If the alphabet size is `A`, the even cycle has
length `q`, every anchor child has `s` points, and a rich child has `H`
ordinary faces, then the recoverable one-gap bank satisfies

\[
 \boxed{\quad
 V(W(S))\ \ge\
 \max\left\{
       (As/2)^q,
       (A/4)^{q-1}s^{q-3}H
 \right\}.\quad}                                        \tag{1}
\]

The first term is the singleton-transversal layer.  The second is a
genuine one-face, one-gap profile bank with load one.  It is not the
adjacent marked seam bank, which is indeed zero in the alternating
regression.

Consequently this construction is not a sub-one-half recursive wrapper.
Put `q=log A=d`, `log s=beta d`, and suppose the child has face coefficient
`c`, so `log H=(c-o(1))(log s)^2`.  Since
`log |W(S)|=(1+beta+o(1))d`, (1) gives

\[
 c_W\ge
 \max\left\{
 {1\over1+\beta},
 {1+\beta+c\beta^2\over(1+\beta)^2}
 \right\}.                                               \tag{2}
\]

At a recursive fixed point `c_W<=c`, the second inequality forces

\[
                 c\ge {1+\beta\over1+2\beta}>{1\over2}. \tag{3}
\]

The right side decreases to `1/2` as `beta` tends to infinity.  Hence this
lane is coefficient-sharp: it supplies no uniform epsilon above one half,
but it cannot produce a coefficient below one half.

There is an important scope boundary.  The proof of the second term in
(1) uses **lexicographic exposure**: a right child profile at one endpoint
and a left child profile at the other really splice after the intervening
cell is omitted.  Broad cyclic-ear/Ferrers data without this hypothesis do
not imply the splice; the rational directional obstruction in
`DOMINANCE_CELL_SEPARATED_ONE_GAP.md` remains valid.  Thus the result kills
the proposed projectively-universal lexicographic recursive construction,
not every conceivable nonseparated ear realization.

The exact verifier is

```text
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_alternating_ferrers_planar_wrapper.py
```

It checks a 20-point rational `q=4,A=4` realization, all 64 adjacent
compatibility entries, general position, the four nonconvex child order
types, all `2^20` subsets by exact four-circuit zeta closure, the detached
one-gap and opposite-product tables, and the coefficient algebra.

## 1. Tangent coordinates realize the alternating cycle

Normalize an oriented parent edge to

\[
                         u=(-1,0),\qquad v=(1,0).         \tag{4}
\]

For positive tangent coordinates `L,R`, put

\[
 p(L,R)=\left({L-R\over L+R},-{2\over L+R}\right).       \tag{5}
\]

This is the inverse tangent map from
`DETACHED_RADIAL_LEXICOGRAPHIC_PROFILE.md`.  It is a bijection from the
positive quadrant to the open exterior pocket below `uv`.  In particular
the two endpoint tangent coordinates of one ear point can be prescribed
independently.

At two adjacent edges of the square, direct determinants give

\[
 B\cup\{p_i(L_i,R_i),p_{i+1}(L_{i+1},R_{i+1})\}
 \text{ convex}
 \quad\Longleftrightarrow\quad
                         R_iL_{i+1}>1.                   \tag{6}
\]

For a general strictly convex rational parent the right side is
`R_iL_(i+1)>kappa_i` for a positive rational corner constant.  Rescaling
one tangent coordinate absorbs `kappa_i`; nothing below depends on it.

Let the labels be `x in[A]`, with `A` even, and let `1<c<rho`.  At an even
seam prescribe

\[
                         R_i(x)=\rho^{-x},\qquad
                         L_{i+1}(y)=c\rho^y,              \tag{7}
\]

and at an odd seam prescribe

\[
                         R_i(x)=\rho^x,\qquad
                         L_{i+1}(y)=c\rho^{-y}.           \tag{8}
\]

Equations (6)--(8) say exactly

\[
                x_i\le x_{i+1}\quad(i\text{ even}),
 \qquad         x_i\ge x_{i+1}\quad(i\text{ odd}).      \tag{9}
\]

Every cell receives one positive left and one positive right coordinate,
so (5) realizes all constraints simultaneously.  The strict margin
between `c` and `rho` permits a generic rational perturbation, giving
general position.  Replacing any anchor by a sufficiently small rational
projective copy of an arbitrary order type preserves every sign in (9).
This proves scalable planar realizability, including projectively
universal low-face children.

The anchors may moreover be packed into arbitrarily small macro
neighbourhoods; the exponential spacing in (7)--(8) is only convenient
notation.  For example, take rational `delta=o(A^{-2})` and use

\[
 \begin{array}{ll}
 R_i(x)=1-\delta x,&L_{i+1}(y)=1+\delta(y+1/2)
                                      \quad(i\text{ even}),\\
 R_i(x)=1+\delta x,&L_{i+1}(y)=1-\delta(y-1/2)
                                      \quad(i\text{ odd}).
 \end{array}                                             \tag{9a}
\]

The linear term has the sign of `y-x+1/2` or `x-y+1/2`, while the product
error is `O(delta^2A^2)`, so (9) still holds.  All coordinates tend to one,
and (5) puts every cell into a vanishing neighbourhood of its edge-macro
point.  This is the separated realization used in the wrapper theorem;
the angular exposure state of a generic child is then uniform over every
anchor choice.

The valid singleton words `Omega` obey

\[
                         (A/2)^q\le|\Omega|\le A^q,       \tag{10}
\]

because choosing every even coordinate in the lower half and every odd
coordinate in the upper half gives a complete valid rectangle.  With
`A=2^d,q=d`, this is quadratic entropy.

## 2. Adjacent anti-alignment is genuine

Use zero-based cell parity.  Declare the rich anchors to be

\[
 S_i=\begin{cases}
       (A/2,A],&i\text{ even},\\
       [1,A/2],&i\text{ odd}.
     \end{cases}                                         \tag{11}
\]

At an even seam, a rich left label is larger than a rich right label, so
`x_i<=x_(i+1)` fails.  At an odd seam the reverse inequality fails.  Thus
no original adjacent seam contains two rich anchors.  Arbitrarily many
left and right profiles may be placed over (11) while every marked
adjacent enhanced bank remains empty.  This part of the common abstract
regression is fully planar.

## 3. One deletion changes anti-alignment into alignment

Delete cell `g`.  Its two neighboring cells `g-1,g+1` have the same
parity, hence the same rich half.

If `g` is odd, put every retained even coordinate in the third quarter
`(A/2,3A/4]` and every retained odd coordinate in the top quarter
`(3A/4,A]`.  All surviving inequalities (9) hold and the two gap endpoints
are rich.  If `g` is even, put retained odd coordinates in the second
quarter `(A/4,A/2]` and retained even coordinates in the bottom quarter
`[1,A/4]`.  Again all inequalities hold and both gap endpoints are rich.
Therefore every gap has a rectangular family of

\[
                              (A/4)^{q-1}                 \tag{12}
\]

valid partial anchor words with two rich endpoints.

Now impose the geometric hypothesis actually used by the natural child
construction.

> **Lexicographic exposure hypothesis.**  Every macro anchor is replaced
> by a sufficiently small `s`-point child.  At cell `i`, a rich child has
> `A_i` distinguishable left exposed profiles and `R_i` distinguishable
> right exposed profiles.  After cell `g` is omitted, any right profile at
> `g-1`, any left profile at `g+1`, and one arbitrary point in every other
> retained child form one ordinary face.  The output recovers the partial
> anchor word and every local choice.

This is precisely the one-gap clause of the exact lexicographic recurrence
in `DETACHED_RADIAL_LEXICOGRAPHIC_PROFILE.md`.  It holds for sufficiently
small projective copies of arbitrary child order types.

For the rectangle (12), the gap-`g` bank consequently has size

\[
 B_g\ge(A/4)^{q-1}s^{q-3}R_{g-1}A_{g+1}.                \tag{13}
\]

There is no overlap loss: the disjoint microcluster supports recover every
retained anchor, and the omitted anchor never entered the partial word.

For a generic child direction, every nonempty ordinary child face is
recovered by its left and right boundary profiles.  Hence

\[
                              A_iR_i\ge H_i,              \tag{14}
\]

where `H_i` is its nonempty face count.  Cyclic cancellation gives

\[
 \prod_g(R_{g-1}A_{g+1})=\prod_iA_iR_i\ge\prod_iH_i.    \tag{15}
\]

If `H_i>=H`, some gap has profile factor at least `H`.  Equations
(13)--(15) prove the second term of (1).  Notice why adjacent
anti-alignment is irrelevant: the new profile seam skips exactly one cell
and therefore joins equal parities.

The first term of (1) follows independently from (10): choose one of the
`s` points in every selected child of a valid word.  Sufficient shrinking
makes every such transversal an ordinary face, and its support decodes the
word.

## 4. Exact coefficient recurrence

Let

\[
 q=d+O(1),\qquad A=2^d,\qquad s=2^{\beta d+o(d)}.         \tag{16}
\]

The wrapper has

\[
 |W(S)|=qAs+q,qquad
 \log|W(S)|=(1+\beta+o(1))d.                             \tag{17}
\]

If

\[
                         \log H=(c-o(1))\beta^2d^2,      \tag{18}
\]

the two terms of (1) have logarithms at least

\[
 (1+\beta-o(1))d^2,qquad
 (1+\beta+c\beta^2-o(1))d^2,                            \tag{19}
\]

respectively.  Division by (17) squared proves (2).

If this operation were a recursive construction with the same limiting
coefficient `c` at parent and child, then `c_W<=c`.  The one-gap term gives

\[
 c(1+\beta)^2\ge1+\beta+c\beta^2,
 \quad\text{so}\quad
 c(1+2\beta)\ge1+\beta,                                 \tag{20}
\]

which is (3).  In particular, for every `c<=1/2`,

\[
 {1+\beta+c\beta^2\over(1+\beta)^2}-c
 ={1+\beta-c(1+2\beta)\over(1+\beta)^2}>0.             \tag{21}
\]

The wrapper strictly increases every sub-one-half coefficient.  The
thresholds for `beta=1,2,4,8` are respectively
`2/3,3/5,5/9,9/17`; their infimum is exactly one half.

## 5. Exact four-cell rational audit

Take the square

\[
 B=((-1,-1),(1,-1),(1,1),(-1,1))                       \tag{22}
\]

and start from the four-point order type

\[
                         (1,0),(2,4),(3,1),(4,0),        \tag{23}
\]

whose third point lies inside the triangle of the other three.  Put
`epsilon=1/100`.  In cells `0,2`, use

\[
 L=1-\epsilon(f-1/2)+a_i\epsilon^2g,qquad
 R=1-\epsilon f+b_i\epsilon^2g,                         \tag{24}
\]

and in cells `1,3`, use

\[
 L=1+\epsilon(f+1/2)+a_i\epsilon^2g,qquad
 R=1+\epsilon f+b_i\epsilon^2g,                         \tag{25}
\]

with

\[
                   (a_i,b_i)=(8,2),(1,-7),(8,6),(4,-1). \tag{26}
\]

Map (24)--(25) into the four edge pockets by (5).  All 20 points are in
general position.  Each cell retains the nonconvex order type (23), every
single point is an admissible ear, and all 64 adjacent pairs satisfy (9)
exactly.  There are 70 valid full singleton words.  No compatible seam has
two rich labels.

Exact four-circuit closure of all `2^20` subsets gives

\[
                         V(P)=9722.                      \tag{27}
\]

The rank vector is

\[
 (1,20,190,1140,2945,3108,1716,528,74).                 \tag{28}
\]

Among the 16 ear points alone there are 2047 ordinary faces.  Their counts
by exact active-cell mask `0,...,15` are

\[
 (1,14,14,143,14,169,143,196,
       14,143,169,216,143,196,216,256).                  \tag{29}
\]

Thus the four exact one-gap layers have sizes `196,216,196,216`.  More
sharply, each opposite pair of cells has a complete `13 by 13` detached
profile rectangle, giving the two entries `169` in (29).  The attempted
anti-alignment is visible on the original seams, but it has already
reappeared as an ordinary detached product across one omitted cell.

## 6. Remaining nonlexicographic boundary

The following statements are now separated rigorously.

1. Alternating Ferrers singleton words are planarly realizable at
   quadratic entropy, even with projectively universal children.
2. Their original adjacent rich-profile banks can all be zero.
3. In a sufficiently separated lexicographic realization, every omitted
   cell joins equal-parity rich supports; (1) and the coefficient reset
   (2)--(3) are unavoidable.

What is not proved is that an arbitrary long, nonseparated ear system must
satisfy the lexicographic exposure hypothesis.  Indeed, broad tangent
dominance alone does not: the exact five-point obstruction in
`DOMINANCE_CELL_SEPARATED_ONE_GAP.md` makes a nominal directional gap
profile nonconvex.  Any surviving anti-aligned construction must exploit
that failure at a positive share of gaps.  It then lies in the heavy
seam/release-defect branch of `CYCLIC_FERRERS_ONE_GAP.md`, rather than being
a recursive projectively-universal lexicographic wrapper.
