# The matching swap-cell four-cycle gate

## 1. Outcome

The matching-wedge reduction can be sharpened once more.  A failure of the
matching-core estimate produces a component of high weighted degeneracy.
After parallel copies are separated, a high-degeneracy simple graph with
small components must have a pair of vertices with many common neighbours,
equivalently many four-cycles.  This turns the previously proposed
two-level fork into one exact collision object: a matching swap-cell `C_4`.

Let `H_z` be the underlying simple matching graph in one affine component,
let

\[
 h_z=|V(H_z)|,\qquad
 r_z=\max_{u\ne v}|N(u)\cap N(v)|,\qquad
 \mu_z=\max_{e\in E(H_z)}m_e.                    \tag{1.1}
\]

Then the weighted degeneracy of the corresponding multigraph is at most

\[
 \boxed{mu_z\bigl(1+\sqrt{r_zh_z}\bigr).}       \tag{1.2}
\]

Consequently the matching branch of Erdős 1208 follows from

\[
 \boxed{
 \max_z\mu_z\bigl(1+\sqrt{r_zh_z}\bigr)
 \le K N^{o(1)}.}                                \tag{1.3}
\]

This is a strictly smaller geometric target than the raw component product
`h_z mu_z`.  It asks for three coupled facts: a support-scale component
bound, a parallel-fibre bound, and a common-neighbour bound.  The last is
the new load-bearing theorem.

## 2. Exact symmetric edge normal form

Put `L=I+J`.  Every cell in component `z` has the form

\[
 C_z(b)=(b,z+Lb),\qquad b,z+Lb\in D.             \tag{2.1}
\]

An edge copy between `C_z(b)` and `C_z(c)` has an ordinary-sum label
`s in D+D`.  Its base is forced by

\[
 \boxed{a=J(s-z-Lb-Lc).}                        \tag{2.2}
\]

The seven complete-difference roles are exactly

\[
 \boxed{
 a,\ b,\ c,\ s-b,\ s-c,\ z+Lc,\ z+Lb\in D.}  \tag{2.3}
\]

The two adaptive shifts are

\[
 q=b-a,\qquad p=c-a,                             \tag{2.4}
\]

and both must belong to the support-adaptive popular set, with `p!=q`.
Conversely (2.2)--(2.4) reconstruct the original record.  Therefore

\[
 m_z(b,c)=\#\{s:\text{(2.2)--(2.4) hold}\}.      \tag{2.5}
\]

This symmetric form is preferable to the earlier `e`-parameterization: a
parallel edge is literally a family of compatible ordinary sums, and a
four-cycle consists of four cells and four such sum labels.

## 3. Codegree-to-degeneracy theorem

Let a nonempty induced subgraph of `H_z` have `n` vertices and minimum
degree `delta`.  Counting unordered length-two paths by their centre and by
their endpoint pair gives

\[
 n{\delta\choose2}
 \le\sum_x{d(x)\choose2}
 =\sum_{u<v}|N(u)\cap N(v)|
 \le r_z{n\choose2}.                             \tag{3.1}
\]

Hence

\[
 \delta(\delta-1)\le r_z(n-1)\le r_zh_z,        \tag{3.2}
\]

so the simple degeneracy is at most `1+sqrt(r_z h_z)`.  Orient a degeneracy
ordering and replace every simple edge by its at most `mu_z` parallel
copies.  This proves (1.2).

Now return to a dyadic optimal core `U_t`.  Its nonisolated vertex count is
at most `E/t`, where `E` is the total swap edge mass.  If (1.3) holds, orient
the matching subgraph componentwise with maximum weighted outdegree
`K N^{o(1)}`.  Therefore

\[
 M_t\le K N^{o(1)}|U_t|
 \le {K N^{o(1)}E\over t},                      \tag{3.3}
\]

which is the required `tM_t` estimate.  Dyadic summation costs only another
subpolynomial factor.

## 4. The exact four-cycle object

Take four distinct cell parameters `b_0,b_1,b_2,b_3` in one component and
the cycle

\[
 b_0b_1,\quad b_1b_2,\quad b_2b_3,\quad b_3b_0. \tag{4.1}
\]

Choose one ordinary sum `s_ij` on each edge.  Equations (2.2)--(2.4) give
four bases

\[
 a_{ij}=J(s_{ij}-z-Lb_i-Lb_j)                   \tag{4.2}
\]

and four exact seven-role records.  Thus every matching `C_4` retains:

* four physical endpoint cells `C_z(b_i)`;
* four adaptive-popular shift pairs;
* four ordinary sums in `D+D`; and
* all twenty-eight role memberships from (2.3), with the cell roles shared
  around the cycle.

Deleting the sum labels or the popularity conditions permits generic
linear plantings and is not a valid route.  The intended common-neighbour
theorem must use the full system (4.2).

## 5. Endpoint and component stress

The exact optimal matching cores give

| family | `K` | max `h_z` | max `mu_z` | max `r_z` | simple `C_4` count |
|---|---:|---:|---:|---:|---:|
| Costas 23 | 9.747 | 9 | 7 | 4 | 1492 |
| Costas 29 | 9.518 | 10 | 7 | 5 | 14105 |
| Costas 31 | 10.901 | 9 | 7 | 5 | 5224 |
| Costas 37 | 11.036 | 11 | 7 | 7 | 63119 |

The component size tracks `K`, while both parallel multiplicity and
codegree remain tiny.  This is substantially more structured than the raw
swap graph.

Every four-cycle is also classified by the number of distinct physical
endpoints among its four cells and the number of distinct mixed alpha
potentials.  For Costas 37 the nonzero-potential rows are

| physical endpoints | distinct potentials | cycles |
|---:|---:|---:|
| 16 | 4 | 16786 |
| 15 | 4 | 26580 |
| 14 | 4 | 15011 |
| 13 | 4 | 4012 |
| 12 | 4 | 600 |
| 11 | 4 | 60 |
| 10 | 4 | 2 |

There are only 68 cycles involving a zero-vector potential.  Thus passing
from wedges to four-cycles has a useful effect: endpoint-contact branches
now form the majority and can be routed to the existing endpoint remainder,
while the fully sixteen-distinct branch is a concrete `26.59%` residual.
All four potentials remain distinct, so repeated-potential compression is
still unavailable in the clean branch.

## 6. Correct next theorem

The direct target is the support-compensated product estimate (1.3), or
equivalently

\[
 \boxed{\mu_z^2r_zh_z\le K^2N^{o(1)}}             \tag{6.1}
\]

apart from the harmless additive `mu_z` term.  It would be enough, but is
probably unnecessarily strong, to prove the three separate estimates

\[
 h_z\le K^2N^{o(1)},\qquad
 \mu_z,r_z\le N^{o(1)}.                           \tag{6.2}
\]

The stresses suggest the sharper `h_z<=KN^{o(1)}`.  Nevertheless the
product form must remain primary: standard generic planting can make one
of component size, parallel load, or codegree large while simultaneously
increasing `|D+D|`, and the resulting growth of `K` is meant to pay for the
concentration.  It is not valid to conjecture the three factors separately
after deleting activity, endpoint matching, or support compensation.

The main new branch is the fully sixteen-endpoint common-neighbour theorem:
for two opposite cells, the number of common matching neighbours carrying
the complete edge records (2.2)--(2.4) should be `N^{o(1)}` after the
endpoint-contact and high-support branches are removed.  Proving that
statement, together with the analogous parallel-sum bound, would establish
(1.3) and directly close the matching core.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_matching_c4_common_neighbour_gate.py
python3 phase2/loop/erdos1208/analyze_swap_optimal_nested_cores.py --larger
```

The verifier checks (2.2)--(2.4) on every Costas-11 and Costas-17 record,
exhausts the codegree-degeneracy inequality on every simple graph through
six vertices, and reproduces the Costas-17/23 component, codegree,
four-cycle, and endpoint profiles.  The larger analyzer verifies the full
table.
