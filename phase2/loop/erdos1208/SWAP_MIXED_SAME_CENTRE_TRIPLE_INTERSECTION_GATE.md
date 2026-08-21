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
the envelopes (3.4)--(3.6).

The exact geometric stress rows are reproduced by

```bash
python3 phase2/loop/erdos1208/analyze_swap_optimal_nested_cores.py \
  --large-costas-only
```
