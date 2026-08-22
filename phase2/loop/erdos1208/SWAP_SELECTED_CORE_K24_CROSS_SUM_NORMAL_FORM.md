# Selected-core K2,4 cross-sum normal form

> **Continuation.**  The optimal-core weight left abstract here is now
> explicit.  Each owner intersects the bare first-track fibre with a
> translate of a fourfold adaptive-popular set.  The resulting three-factor
> tensor in `SWAP_K24_ADAPTIVE_POPULAR_THREE_FACTOR_GATE.md` is the live
> closing gate.

## 1. Outcome

The rich physical-wedge cell has a lossless four-colour normalization in
the direct cross sum

\[
 P=A+JA.
\]

It is substantially stronger than saying that six independent directions
have many representations.  Every occurrence supplies a synchronized
`K_{2,4}` table of differences in `P-P`; the first row of four colours is a
complete invariant of the six literal `D` tracks.  After adjoining the
common physical endpoint and its two endpoint roles, this four-colour key
determines the owner cell.  Consequently the remaining rich-cell third
moment can be reindexed *exactly* by endpoint-coloured four-stars in
`P-P`.

The reduction also exposes a load-bearing colour.  The full ambient second
and third moments are coloured diagonal correlations, not products of six
anonymous `D-D` overlaps.  Dropping the colour already overcounts by a
factor `3688/196` on a four-point genuine distance-Sidon certificate.

This does not yet prove the Carleson gate.  It gives a smaller and sharper
object for the attack: a selected third moment of aligned four-stars with
one physical endpoint, rather than an unstructured cross-sum energy.

## 2. Six tracks and the K2,4 table

Identify the plane with the Gaussian integers, let `J` be multiplication by
`i`, and put `L=I+J`.  One occurrence over a physical wedge has variables

\[
 (V,W,a,b,e,q)
\]

and six nonzero directed tracks

\[
\begin{aligned}
 F_0&=V-a-q, &
 F_1&=W-Lb+Jq+Ja, &
 F_2&=W-Lb+Jq+La,\\
 F_3&=V-a-q+e, &
 F_4&=W-b+Jq-Je, &
 F_5&=W+Jq-Je.
\end{aligned}                                      \tag{2.1}
\]

Put

\[
 R=JV+W.
\]

For `i in {0,3}` and `j in {1,2,4,5}`, define

\[
 Z_{ij}=F_j+JF_i.                                  \tag{2.2}
\]

The parameter `q` cancels.  In column order `1,2,4,5`, the two rows are

\[
\begin{array}{c|cccc}
 &1&2&4&5\\ \hline
0&R-Lb&R-Lb+a&R-b-J(a+e)&R-J(a+e)\\
3&R-Lb+Je&R-Lb+a+Je&R-b-Ja&R-Ja.
\end{array}                                        \tag{2.3}
\]

Thus the second row is the first row translated by `Je`.  Every parameter
in the cell gives the same table.

The entries are literal differences in `P-P`.  If
`F_i=h_i-t_i` and `F_j=h_j-t_j`, then

\[
 Z_{ij}=(h_j+Jh_i)-(t_j+Jt_i).                    \tag{2.4}
\]

Distance-Sidonicity makes `A+JA` direct.  Hence each endpoint in (2.4)
recovers its ordered pair of `A`-points, and a representation of `Z_{ij}`
recovers the two directed tracks `F_i,F_j`.  The four representations in
row zero share the same literal track `F_0`; the four in row three share
`F_3`.  This synchronization is absent from ordinary additive energy.

## 3. Four colours are a complete invariant

Write

\[
 \kappa=(Z_{01},Z_{02},Z_{04},Z_{05})=(z_1,z_2,z_4,z_5).
                                                               \tag{3.1}
\]

Then

\[
\boxed{\begin{aligned}
 a&=z_2-z_1,\\
 b&=z_5-z_4,\\
 e&=b-a+J(z_4-z_1),\\
 R&=z_1+Lb.
\end{aligned}}                                    \tag{3.2}
\]

So one row already determines the entire table and `(R,a,b,e)`.  Given in
addition the first track `f=F_0`, all six tracks are recovered as

\[
\boxed{
 (F_0,F_1,F_2,F_3,F_4,F_5)
 =\bigl(f,z_1-Jf,z_2-Jf,f+e,z_4-Jf,z_5-Jf\bigr).} \tag{3.3}
\]

It follows immediately that two occurrences have the same key `kappa` if
and only if their track differences have the synchronized form

\[
 \Delta F_0=\Delta F_3=h,qquad
 \Delta F_j=-Jh\quad(j=1,2,4,5).                 \tag{3.4}
\]

This is precisely a parameter translation.  There is no hidden quotient.
In particular, a key fibre injects into the possible values of `F_0`.

For completeness, the full eight-row system has complex rank four.  Of its
`70` four-subsets, `63` recover `(R,a,b,e)`.  The seven dependent subsets
are the six complete `2 x 2` rectangles and

\[
 \{01,02,34,35\}.                                 \tag{3.5}
\]

The unusually large family of bases may be useful for a future fractional
cover, but (3.1) is the canonical key because its four representations all
share one literal directed edge.

## 4. The physical endpoint removes the gauge

The four-colour key recovers `R=JV+W`, but not `V,W` separately.  This is
exactly the one-dimensional gauge previously found in the six-track rank
calculation.  The physical-wedge population supplies the missing datum.

Fix a common endpoint `x in A` and the head/tail role of `x` on each of the
two directed physical edges `V,W`.  Then `R=JV+W` determines `V,W`
uniquely.  Indeed, if two choices give the same `R`, the differences of
their opposite endpoints are nonzero perpendicular vectors of equal
length.  Distance-Sidonicity says the two unordered endpoint pairs must be
equal, after which a nonzero real vector would have to equal its own
quarter-turn, a contradiction.

Once `V,W` are known, (3.2) recovers the owner centre, its two neighbour
offsets and the cross shift.  Finally (3.3) recovers `q` from `F_0`.
Therefore

> **endpoint-star injectivity.**  The common endpoint, its two roles, the
> four-colour key `kappa`, and `F_0` determine one selected occurrence.

More strongly, the common endpoint, its roles and `kappa` determine its
owner cell; the `F_0` values in the fibre are exactly its selected
parameters.  Applied to the lossless physical-wedge indexing, this gives

\[
\boxed{
 C_{\rm center}
 =3\sum_{x,\epsilon_V,\epsilon_W,\kappa}
       {r(x,\epsilon_V,\epsilon_W;\kappa)\choose3}.} \tag{4.1}
\]

Here `r` is the selected-core fibre load.  Equation (4.1) is an identity,
not an ambient upper bound.

## 5. Sixfold intersection and the exact coloured correlation

For a bare key `kappa`, recover `e` from (3.2) and define

\[
 \Lambda(\kappa)=\{f\in D:
 f+e\in D,\ z_j-Jf\in D\ (j=1,2,4,5)\}.          \tag{5.1}
\]

Every selected fibre in (4.1) is a subset of `Lambda(kappa)`.  The
physical endpoint equation and the optimal nested-core selection are the
remaining weights; deleting them produces a much larger ambient object.

There is a sharper exact description of that ambient object.  Put

\[
 S_e=D\cap(D-e)                                    \tag{5.2}
\]

and, for fixed `a,b,e`, put

\[
 d=J(b-a-e),\qquad
 P_{a,b,e}=D\cap(D-a)\cap(D-d)\cap(D-d-b).       \tag{5.3}
\]

Thus `y in P_{a,b,e}` is exactly the four-track pattern

\[
 (F_1,F_2,F_4,F_5)=(y,y+a,y+d,y+d+b).            \tag{5.4}
\]

Writing `z=Z_{01}`, the complete key is

\[
 \kappa=(z,z+a,z+d,z+d+b),
\]

and its ambient first-track load is the ordinary cross-correlation

\[
\boxed{
 r_{a,b,e}(z)
 =|\{f\in S_e:z-Jf\in P_{a,b,e}\}|.}            \tag{5.5}
\]

This removes the artificial four-dimensional diagonal set: the positive
half is one fourfold intersection inside the original directed-difference
set `D`.

For a set `X`, write

\[
 R_X(h)=|X\cap(X-h)|,\qquad
 T_X(h,g)=|X\cap(X-h)\cap(X-g)|.
\]

Direct double counting now gives the exact coloured identities

\[
\boxed{
 \sum_z (r_{a,b,e}(z))_2
 =\sum_{h\ne0}R_{S_e}(h)R_{P_{a,b,e}}(-Jh),}     \tag{5.6}
\]

and

\[
\boxed{
 \sum_z (r_{a,b,e}(z))_3
 =\sum_{h,g\ \mathrm{distinct}}
    T_{S_e}(h,g)T_{P_{a,b,e}}(-Jh,-Jg).}         \tag{5.7}
\]

The colours `(a,b,e)` and the coupling inside `P_{a,b,e}` are
load-bearing.  Indeed,

\[
 \sum_e|S_e|=|D|^2,\qquad
 \sum_{a,b,e}|P_{a,b,e}|=|D|^4,                 \tag{5.8}
\]

because an ordered pair, respectively ordered quadruple, of directed
tracks determines its colours uniquely.  These large first moments are
harmless only while the two coloured factors in (5.6)--(5.7) remain
correlated.  If one instead replaces the positive factor by four
independent overlaps of `D`, the resulting six-overlap product is not
lossless and can be far too large.  On the four-point distance-Sidon set

\[
 \{(0,0),(1,0),(0,2),(3,4)\},                    \tag{5.9}
\]

the exact key-load histogram is

\[
 1:14008,\qquad 2:86,\qquad 3:4.
\]

Thus the exact ordered pair and triple masses are `196` and `24`, whereas
the anonymous product

\[
 \sum_{h\ne0}R_D(h)^2R_D(Jh)^4
\]

is `3688`.  The loss occurs before any asymptotics.

## 6. The sharpened closing gate

The direct route may now be stated as the selected, endpoint-coloured
version of (5.7): for a subpolynomial cutoff `R_0`, prove

\[
\boxed{
 \sum_{x,\epsilon_V,\epsilon_W,\kappa:\ r\ge R_0}
 (r-2){r\choose2}
 \le N^{o(1)}(k^3+m^2).}                        \tag{6.1}
\]

Compared with the earlier physical-wedge Carleson gate, (6.1) has three
advantages.

1. Its fibre variable is one literal directed edge `F_0`, not four free
   owner variables.
2. Its four cross-sum representations share `F_0`, and the translated row
   shares `F_0+e`; this alignment survives exactly.
3. The endpoint and two roles remove the gauge, so there is no unrecorded
   owner multiplicity.

An estimate for the anonymous energy `E^+(A+JA)` is neither required nor
sufficient for this step.  What remains is a support-sensitive bound for
the selected coloured correlation (5.7).  The optimal nested-core weight
and the physical endpoint equation must enter before either coloured
factor is replaced by its ambient marginal.

The first of those two inputs is now lossless rather than merely a warning.
If `P` is the global adaptive-popular shift set and `c` is the owner's first
centre coordinate, then the selected first tracks are exactly those for
which

\[
 c-f,\quad c-f+a,\quad c-f-e,\quad c-f-e+b\in\mathcal P.
\]

Consequently (5.7) acquires a third triple-intersection factor coming from
a fourfold translate of `P`; see the continuation note above.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_selected_core_k24_cross_sum.py
```

The verifier checks (2.1)--(3.4) on exact integer samples, classifies all
`70` four-row minors over `Q(i)`, proves directness of `A+JA` on (5.7),
checks endpoint-anchor injectivity exhaustively, reconstructs every
four-star representation through its `A` endpoints, and verifies the
coloured pair/triple identities and the exact `196/24/3688` stress.
