# Same-centre mixed collisions are exact triple-intersection energy

## 1. Outcome

The twelve-channel repeated-pair normal form has a load-bearing diagonal.
If two endpoint groups have the same centre and differ only in their switch,
then their displacement triple is

\[
 h=0,\qquad a=0,\qquad s=J(u-v).                 \tag{1.1}
\]

This is the largest repeated mixed-pair branch on the exact hard rows.  It
has a simpler lossless description which retains the original parallel
copy fibres.

Fix a centre, a physical endpoint, and one neighbour fibre.  Let `Q` be
the set of its copy parameters `q`.  For a nonzero switch `u`, put

\[
 R_Q(u)=\{r:r,r+u\in Q\}.                         \tag{1.2}
\]

After the role-dependent affine change recorded below, the projected keys
from this neighbour in the group with switch `u` are in bijection with
`R_Q(u)`.  Therefore two switch groups `u\ne v` have exactly

\[
 T_Q(u,v)=|R_Q(u)\cap R_Q(v)|
 =|\{r:r,r+u,r+v\in Q\}|                         \tag{1.3}
\]

common projected keys from this fibre.

Let the moving-`V` neighbour fibres be `Q_i^V` and the moving-`W` fibres
be `Q_j^W`.  Set

\[
 A(u,v)=\sum_iT_{Q_i^V}(u,v),\qquad
 B(u,v)=\sum_jT_{Q_j^W}(u,v).                    \tag{1.4}
\]

Then the repeated mixed-pair collision mass whose two owners have this
fixed centre and endpoint is exactly

\[
\boxed{C_{\rm centre}=\sum_{\{u,v\}}A(u,v)B(u,v).} \tag{1.5}
\]

Thus the dominant coordinate diagonal is not a generic twelve-copy
intersection.  It is a colourwise dot product of two third-order parallel
fibre spectra.  This is the correct object to retain in a global charge.

## 2. Exact role changes

Write the centre cell as `(c,e)`.  For a moving-`W` neighbour the projected
key is

\[
 (q-u,B),                                           \tag{2.1}
\]

where `B` is the fixed physical edge of the neighbour.  Put `r=q-u`.
The occurrence exists precisely when `r,r+u in Q`, and the pair
`(neighbour,r)` recovers the key.

For a moving-`V` neighbour with displacement `t`, the projected key is

\[
 (q+t-u,c-q+u)=(r+t,c-r).                         \tag{2.2}
\]

with the same `r=q-u`.  Again the key is recovered by `(neighbour,r)` and
exists precisely when `r,r+u in Q`.  Distinct neighbour fibres give
distinct physical edges, so their contributions add.  Intersecting the
key sets for switches `u` and `v` proves (1.3)--(1.5).

## 3. Exact first-moment identity and a coarse envelope

Every unordered three-element subset of `Q` contributes once for each of
its three choices of base point.  Hence

\[
\boxed{\sum_{\{u,v\}}T_Q(u,v)=3{|Q|\choose3}.}    \tag{3.1}
\]

Consequently

\[
 \sum_{\{u,v\}}A(u,v)=3\sum_i{|Q_i^V|\choose3},
 \quad
 \sum_{\{u,v\}}B(u,v)=3\sum_j{|Q_j^W|\choose3}. \tag{3.2}
\]

If

\[
 \Theta_V=\max_{u\ne v}A(u,v),\qquad
 \Theta_W=\max_{u\ne v}B(u,v),                   \tag{3.3}
\]

then

\[
 C_{\rm centre}\le
 \min\left\{
 3\Theta_W\sum_i{|Q_i^V|\choose3},
 3\Theta_V\sum_j{|Q_j^W|\choose3}
 \right\}.                                      \tag{3.4}
\]

For comparison, if every fibre has size at most `R`, and `f_V,f_W` are
the numbers of fibres, put

\[
 W_V=\sum_i{|Q_i^V|\choose2},\qquad
 W_W=\sum_j{|Q_j^W|\choose2}.                    \tag{3.5}
\]

Then

\[
\boxed{C_{\rm centre}\le
 R^2\min\{f_W\,W_V,f_V\,W_W\}.}                 \tag{3.6}
\]

Indeed `3 binom(m,3)=(m-2)binom(m,2)<=R binom(m,2)`
and `Theta_V<=Rf_V`, `Theta_W<=Rf_W`.

Formula (3.6) is deliberately labelled coarse.  Even with subpolynomial
`R`, replacing `f_V,f_W` by their endpoint bound can lose a factor of
order `k`.  The live theorem should sum the dot product (1.5), or its
dyadic large-`Theta` cores, across centres before taking either marginal.

There is a stronger exact reorganization.  For two fibres `X,Y`, put

\[
 r_{X,Y}(d)=|\{(x,y)\in X\times Y:y-x=d\}|.
\]

Expanding both triple intersections and setting `d=y-x` gives

\[
\boxed{
 \sum_{\{u,v\}}T_X(u,v)T_Y(u,v)
 =3\sum_d{r_{X,Y}(d)\choose3}.}                  \tag{3.7}
\]

Indeed an unordered triple in `X\cap(Y-d)` contributes once for each of
its three choices of base point, and this correspondence is reversible.
Therefore

\[
\boxed{
 C_{\rm centre}
 =3\sum_{i,j,d}{r_{Q_i^V,Q_j^W}(d)\choose3}.}    \tag{3.8}
\]

This identifies the branch with a size-biased version of the exact
cross-difference collision already isolated in
`SWAP_MATCHING_WEIGHTED_ENDPOINT_PENCIL_GATE.md`.  If

\[
 Q_2=\sum_{i,j,d}{r_{Q_i^V,Q_j^W}(d)\choose2},
 \qquad \rho=\max_{i,j,d}r_{Q_i^V,Q_j^W}(d),
\]

then the identity `3 binom(r,3)=(r-2)binom(r,2)` gives

\[
\boxed{C_{\rm centre}\le(\rho-2)_+Q_2.}          \tag{3.9}
\]

The pointwise factor `rho` must not be discarded.  The direct target is
the size-biased collision in (3.8), with the endpoint, both neighbour
fibres, and all popular corners retained.  In the endpoint-pencil notation
each `r_{X,Y}(d)` is already capped by the minimum of the three coupled
`D-D` loads in equation (7.7) of that note.

There is also a lossless one-switch envelope.  Write

\[
 a_i(u)=R_{Q_i^V}(u),\quad b_j(u)=R_{Q_j^W}(u),
\]

\[
 \Lambda_V(u)=\sum_i a_i(u),\quad
 \Lambda_W(u)=\sum_j b_j(u),                     \tag{3.10}
\]

and

\[
 M_V(u)=\sum_i(|Q_i^V|-2)a_i(u),\quad
 M_W(u)=\sum_j(|Q_j^W|-2)b_j(u).                 \tag{3.11}
\]

For one fibre,

\[
 \sum_{v\ne u}T_Q(u,v)=(|Q|-2)R_Q(u).           \tag{3.12}
\]

Indeed each start pair `r,r+u` may choose any of the other `|Q|-2`
points as `r+v`.  Therefore

\[
\boxed{
 2C_{\rm centre}\le
 \sum_{u\ne0}\min\{\Lambda_W(u)M_V(u),
                     \Lambda_V(u)M_W(u)\}.}      \tag{3.13}
\]

This is the size-biased second-generation pencil envelope.  It retains
which side supplies the third point and is strictly sharper than replacing
all fibre sizes by their maximum.  If `R=max_i|Q_i|`, it implies

\[
 2C_{\rm centre}\le(R-2)_+
   \sum_{u\ne0}\Lambda_V(u)\Lambda_W(u).         \tag{3.14}
\]

The last sum is exactly the mixed part of the existing second-generation
endpoint pencil.  The remaining gain must therefore come from paying the
size bias in (3.13), or from routing its high-fibre portion to a two-sided
completion core; merely reproving the unweighted pencil bound is not
enough.

Every individual rich translate also has an exact perpendicular
footprint/density fork.  Let

\[
 S=Q_i^V\cap(Q_j^W-d),\qquad r=|S|,qquad
 R_S(u)=|\{(a,b)\in S^2:a-b=u\}|.                \tag{3.15}
\]

The defining `D` tracks of the first fibre contain translates of `-S` and
`JS`.  Hence

\[
 \boxed{JS-S\quad\hbox{has a translate inside }D+D.} \tag{3.16}
\]

Moreover its additive representation energy is exactly

\[
 \boxed{
 E_+(JS,-S)=\sum_u R_S(u)R_S(Ju).}               \tag{3.17}
\]

Indeed equality between `Jb-a` and `Jd-c` is equivalent to
`a-c=J(b-d)`.  Consequently

\[
 |JS-S|\ge {r^4\over\sum_uR_S(u)R_S(Ju)}.        \tag{3.18}
\]

For a threshold `T>=1`, put

\[
 H_T(S)=\{u\ne0:R_S(u)\ge T, R_S(Ju)\ge T\}.
\]

Splitting the sum in (3.17) gives the exact safe envelope

\[
 \boxed{
 \sum_uR_S(u)R_S(Ju)
 \le r^2+2Tr(r-1)
   +\sum_{u\in H_T(S)}R_S(u)R_S(Ju).}            \tag{3.19}
\]

If `T>K`, then `H_T(S)\subseteq\mathcal P_K`: the `-S` track gives at
least `R_S(u)` representations of `u` in `D-D`, and the `JS` track gives
at least `R_S(Ju)` representations of `Ju`.  Thus a rich cell has only two
possibilities.  Either it exposes a large literal footprint in `D+D`, or
its internal difference set creates a new adaptive-popular perpendicular
core.  This is the label-preserving density increment missing from a bare
cross-energy estimate.

## 4. Exact stress and the failed uniform twelve-channel sum

The augmented optimal-core analyzer gives the following repeated mixed
collision split:

\[
\begin{array}{c|r|r|r|r}
k&C_{VW}&C_{h=a=0}&\text{share}&
 \sum_{\text{occupied key/difference cells}}\Upsilon\\ \hline
29&7724&4857&62.88\%&290091145355\\
31&10658&5058&47.46\%&395266391216
\end{array}                                             \tag{4.1}
\]

On the same rows, respectively `7404/7550` and `8482/9496` occupied
key/difference cells contain exactly one group pair.  The maximum cell
loads are only four and five.  In contrast the uniform local overlap
upper sum from the twelve-channel theorem exceeds the true collision by
factors about `3.76e7` and `3.71e7`.

The sharper cross-difference and one-switch profiles are

\[
\begin{array}{c|r|r|r|r|r}
k&Q_2&C_{h=a=0}&\rho&
 \sum_u\Lambda_V(u)\Lambda_W(u)&\text{envelope (3.13)}\\ \hline
29&19064&4857&5&38128&47938\\
31& 9492&5058&6&18984&28072
\end{array}                                             \tag{4.2}
\]

The fourth column is exactly the full mixed incidence mass on these rows.
Thus (3.13) is a realistic constant-scale envelope, unlike the ambient
twelve-channel products, but it is not itself a saving over the quantity
being bounded.

There is a second decisive split.  In (3.8), write

\[
 s=q_1-q_2,qquad d=t_1-t_2.
\]

The three coupled `D-D` directions are

\[
 s,qquad J(s+d),qquad Js+Ld.                    \tag{4.3}
\]

Cells in which one of these directions is zero contribute `3402/4857`
and `3774/5058`, or `70.04%` and `74.61%`, of the same-centre mass at
sizes `29,31`.  These are exactly the universal versions of the three
metric resonances:

* `s=0`, the two copies have the same `q`;
* `s+d=0`, they have the same `p=q+t`; and
* `Js+Ld=0`, the complete-difference displacement vanishes.

They should be routed to the quadratic line footprints in
`SWAP_RESONANT_LINE_FOOTPRINT_PACKING_GATE.md`.  The remaining nonzero
cells belong to the rank-two/rank-six metric lattice packing in
`SWAP_DECORATED_KEY_METRIC_TRANSVERSAL_GATE.md`.  The new issue in both
branches is precisely the extra size bias `(r-2)` in (3.9).

There is an exact low-load/high-load restart.  For any threshold `R>=3`,
write `C_{\rm centre}^{<R}` for the part of (3.8) supported on cells of
load below `R`.  Then

\[
 \boxed{
 C_{\rm centre}^{<R}
 \le (R-3)Q_2.}                                  \tag{4.4}
\]

This is just `3 binom(r,3)=(r-2)binom(r,2)`.  Hence a subpolynomial
threshold reduces the whole low-load population to the existing
second-generation endpoint-pencil energy.  The only genuinely new
population consists of rich cross-fibre translates

\[
 |Q_i^V\cap(Q_j^W-d)|\ge R,                       \tag{4.5}
\]

weighted by `(r-2)binom(r,2)`.  It must be split by the three directions
in (4.3): a zero direction goes to the quadratic line-footprint theorem,
while three nonzero directions go to the rank-six metric-lattice theorem.
This is the direct Carleson gate; proving another unweighted second-energy
bound cannot remove the size bias.

The richest fully nonzero Costas-31 cells have load four and mass twelve.
Every one of them has all three directions in (4.3) represented in `D-D`
and all three associated shifts popular; their four `q`-pairs form small
affine grids in the `31`-lattice.  Thus even the transverse branch is not
locally sparse.  Its saving, if true, must come from global endpoint reuse
and determinant-weighted packing, not a pointwise fibre cap.

For a representative richest nonzero cell, the four-point set `S` has
`|JS-S|=12` and energy `24`, so (3.18) gives `|JS-S|>=32/3`.  The
footprint is already close to quadratic; the unresolved issue is its depth
when the cells are summed over centres.

The exact global footprint audit is

\[
\begin{array}{c|r|r|r|c|c}
k&\sum|\Phi|&|\bigcup\Phi|&\max\operatorname{depth}&
 \max\operatorname{depth}_{\rm wt}&
 \max_z\operatorname{depth}_{\rm wt}(z)/R_{D+D}(z)\\ \hline
23&540&391&6&18/7&3/28\\
29&11577&2147&98&22993/462&1/3\\
31&8618&1171&212&1343/11&40721/118272
\end{array}                                             \tag{4.6}
\]

Here a cell distributes its mass `3 binom(r,3)` uniformly over its
footprint.  The weighted depths are much smaller than the raw depths, and
their sum is exactly `C_centre`, but they are not subpolynomial on the
stored rows.  The last-column inequality is encouraging finite evidence,
not a viable abstract theorem.  Take
`S={(i,i^2):0<=i<r}` and a symmetric set containing two widely separated
copies of `-S` and `JS`.  Then the relevant footprint has size `r^2`, its
uniform weight is `3 binom(r,3)/r^2=Theta(r)`, while every footprint point
has exactly two representations in the ambient sumset.  Thus pointwise
domination by `R_{D+D}` fails by a full factor `r` before the adaptive and
endpoint decorations are imposed.

This sharpens the target once more: the global depth theorem must retain
the popularity of every member of `S` and the common physical endpoint (or
the equivalent four completion corners).  Footprint containment alone is
not enough.

This is a decisive scale diagnosis.  The twelve-channel normal form is
lossless and useful for localization, but its unweighted product of three
`D`-overlaps is not summable.  The same-centre half must use (1.5); the
remaining non-axis cells must retain key-specific support and group-pair
endpoint data.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_mixed_same_centre_triple_intersection.py
```

The verifier exhausts all pairs of subsets of a four-point universe and
tests hundreds of random multi-fibre systems.  It checks the key-set
intersection identity, (1.5), the exact third-moment identity (3.1), and
the envelopes (3.4)--(3.6).  It also verifies the cross-third-energy
identity (3.7)--(3.8), its size-biased second-energy bound (3.9), and the
one-switch envelope (3.12)--(3.14).  Finally it checks the perpendicular
energy identity, footprint containment, and threshold decomposition
(3.15)--(3.19) exhaustively and on random fibre systems.  It also verifies
the affine-copy obstruction to ambient pointwise representation domination.

The exact geometric stress rows are reproduced by

```bash
python3 phase2/loop/erdos1208/analyze_swap_optimal_nested_cores.py \
  --large-costas-only
```
