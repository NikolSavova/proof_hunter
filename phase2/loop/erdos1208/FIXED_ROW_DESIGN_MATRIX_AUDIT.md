# Fixed-row design matrices: a valid compression lemma and a sharp rank barrier

## Status

Fix a transverse row

\[
 d=(u-v)+J(x-y)                                      \tag{0.1}
\]

of a distance-Sidon set `A`, with `|A|=k`, and suppose that the row has
`r` relations.  Dense-core pruning and pair-linearity make the coefficient
matrix of (0.1) a genuine sparse design matrix.  The improved rank theorem of
Dvir--Saraf--Wigderson then gives a useful, rigorous conclusion: a row of size
`r` has a core whose Gaussian-linear realization space has dimension

\[
 O(k^2/r).                                           \tag{0.2}
\]

In particular, a hypothetical row of size `k^(3/2+epsilon)` would be
algebraically rigid up to only `O(k^(1/2-epsilon))` parameters.

This does **not** prove `r<=k^(3/2+o(1))`.  The affine fixed-difference term
supplies only one additional kernel direction after row-centering, whereas
the rank theorem permits `O(k^2/r)` directions.  More decisively, the exact
120-point distance-Sidon stress witness already attains the maximum possible
actual-label ranks: `k-1` before centering and `k-2` after centering.  Thus a
support-only rank argument cannot distinguish that legal critical-scale row
from a forbidden supercritical row.

The exact finite assertions in this note are checked by
`verify_fixed_row_design_matrix_audit.py`.

## 1. The primary rank theorem

An `m` by `n` complex matrix is a `(q,kappa,t)` design matrix if every row
has at most `q` nonzero entries, every column has at least `kappa` nonzero
entries, and two columns have simultaneous nonzero entries in at most `t`
rows.  Theorem 1.3 of Dvir--Saraf--Wigderson, *Improved rank bounds for design
matrices and a new proof of Kelly's theorem*, arXiv:1211.0330, states

\[
 \operatorname{rank} M
 \ge {n\over 1+q(q-1)mt/(n\kappa^2)}
 \ge n-{mtq(q-1)\over\kappa^2}.                   \tag{1.1}
\]

The second inequality is the form used below.  This is stronger than the
older Barak--Dvir--Wigderson--Yehudayoff squared-deficiency estimate and is
the correct theorem to test here.

Primary source:
<https://arxiv.org/abs/1211.0330>.

## 2. Applying it to the pruned role-copy matrix

Use four disjoint role copies `U,V,X,Y` of `A`.  By the pruning lemma in
`DENSE_CORE_ORTHOGONAL_ARRAY_GATE.md`, there is a subrow with

\[
 m\ge r/2,
 \qquad
 \deg(a)\ge \tau:={r\over8k}                       \tag{2.1}
\]

for every active role-label.  Form its `m` by `N` coefficient matrix `C`,
putting coefficients `1,-1,i,-i` in the four role columns of each relation.
Then:

* every row has exactly four nonzeros, so `q=4`;
* every active column has at least `tau` nonzeros;
* two columns in the same role never meet;
* two columns in different roles meet in at most one row, because every two
  roles determine the whole relation.

Thus `C` is a `(4,tau,1)` design matrix.  Since `m<=r`, (1.1) gives

\[
 \boxed{\operatorname{corank} C
        \le {12m\over\tau^2}
        \le {768k^2\over r}.}                     \tag{2.2}
\]

This is the promised compression lemma.

There is a three-dimensional space of role-constant kernel vectors:

\[
 c_U-c_V+i c_X-i c_Y=0.                            \tag{2.3}
\]

The actual coordinate vector `Z`, repeated in the four roles, is not in the
kernel; it satisfies

\[
 CZ=d\mathbf 1.                                    \tag{2.4}
\]

Let `P` be any rank-`m-1` row operator with kernel spanned by the all-ones
vector.  Then `PCZ=0`, while

\[
 \operatorname{rank}(PC)\ge\operatorname{rank}(C)-1. \tag{2.5}
\]

Hence

\[
 \operatorname{corank}(PC)
 \le 1+{768k^2\over r}.                            \tag{2.6}
\]

The kernel now contains the three role-constant directions and `Z`.  Comparing
this lower bound of four with (2.6) yields only `r<=256k^2`, weaker than the
trivial pair-linear bound.  At `r=k^(3/2+epsilon)`, (2.6) says only that the
corank is `O(k^(1/2-epsilon))`; it does not make it smaller than four.

## 3. The actual-label matrix and the affine trap

Merge the four role copies belonging to the same actual point and write one
row as

\[
 M_e={\bf e}_u-{\bf e}_v+i{\bf e}_x-i{\bf e}_y.    \tag{3.1}
\]

The valid transverse conditions prevent cancellation of an entire active
role occurrence: `u=v` would make (0.1) perpendicular and hence nontransverse,
and `x=y` is excluded.  Any two distinct actual labels can co-occur in at
most twelve relations, one for each ordered choice of two distinct roles.
So the merged core is a `(4,tau,12)` design matrix and

\[
 \operatorname{corank}M\le {9216k^2\over r}.       \tag{3.2}
\]

But the affine equations are

\[
 M\mathbf1=0,
 \qquad
 Mz=d\mathbf1.                                    \tag{3.3}
\]

Only the constant vector is in `ker M`.  Projecting away the common
right-hand side makes `z` a second kernel vector but can lower the rank by
one.  Equivalently, homogenizing with the fixed endpoints `p,q` of
`d=p-q` adds the common columns `-e_p+e_q`; those columns occur in every row
and destroy the bounded-overlap design hypothesis.  Deleting them returns
exactly to (3.3) and loses the extra kernel direction.  This is the affine
homogenization trap.

## 4. Exact saturation by legal distance-Sidon rows

For the 120-point heavy-row witness and `d=(0,-1)`, exact reduction modulo
the Gaussian prime above `65537`, with `i=256`, gives:

\[
\begin{array}{c|c|c}
\text{matrix}&\text{rank}&\text{nullity}\
\hline
M&119&1\\
PM&118&2\\
\text{homogenized actual-label matrix}&118&2.
\end{array}                                        \tag{4.1}
\]

The row has `r=948` relations and the point set has all pairwise distances
distinct.  Thus all three ranks are maximal given (3.3).  The same witness
already invalidates any proposed theorem saying that many legal relations
must create additional linear freedom.

For the 90-point strict-diameter witness, with `r=266`, the corresponding
actual-label ranks are `86` before centering and `85` after centering.  Its
larger nullity reflects the deliberately less rigid construction, not a
universal phenomenon.

On four disjoint role copies, the 120-point witness uses 478 active columns.
The raw role matrix has rank 473 and its centered version rank 472.  These
figures are also recorded by the verifier; isolated role labels are not
counted in the displayed nullities.

## 5. Correct consequence and next use

The valid conclusion is a rigidity dichotomy:

> A supercritical fixed row, if it exists, has a pruned pair-linear core
> whose full Gaussian-linear realization space has
> `O(k^2/r)` dimensions beyond the unavoidable role constants.

To turn this into a bound on `r`, one needs an input not contained in the
zero--nonzero pattern or ordinary matrix rank.  Plausible additions are:

1. a **radial rigidity theorem** saying that a low-corank Gaussian relation
   system with too many rows forces two non-antipodal realized differences
   to have the same Euclidean norm; or
2. an **ambient height theorem** saying that a collision-free integer
   realization of such a system requires a box too large for the target
   grid scale.

The current heavy witness is compact (all coordinates have magnitude at most
1009 for `k=120`), so any height theorem must be genuinely asymptotic and
cannot follow from a crude determinant estimate.

Do not cite (2.2) as a proof of the fixed-row `k^(3/2)` gate.  It is a useful
compression statement and an exact method barrier, nothing more.
