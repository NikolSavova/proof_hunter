# Endpoint pencils reduce the matching gate to clean codegree

## 1. Outcome

The endpoint-contact part of the matching four-cycle gate can be removed
from the maximum-codegree parameter.  In one active matching component
`H_z`, let

\[
 h_z=|V(H_z)|,
 \qquad
 \mu_z=\max_{e\in E(H_z)}m_e.                   \tag{1.1}
\]

Every cell has four distinct physical endpoints.  Define its endpoint-pencil
occupancy by

\[
 \kappa_z=
 \max_{x\in A}\#\{C\in V(H_z):x\text{ is an endpoint of }C\}. \tag{1.2}
\]

Let `r_z^circ` be the largest common-neighbour codegree of two cells whose
eight physical endpoints are all distinct.  Then

\[
 \boxed{
 d_{\rm wt}(H_z)
 \le \mu_z\left(1+\sqrt{(4\kappa_z+r_z^\circ)h_z}\right).} \tag{1.3}
\]

Thus the matching branch follows from the strictly more endpoint-sensitive
product estimate

\[
 \boxed{
 \mu_z^2(\kappa_z+r_z^\circ)h_z
 \le K^2N^{o(1)}.}                              \tag{1.4}
\]

This replaces the old raw factor `r_z` by an endpoint-pencil term and a
clean-pair codegree.  It also makes the preceding common-`r` dichotomy exact:
after the endpoint-pencil term is paid, every surviving repeated-`r`
four-cycle has sixteen distinct physical endpoints.

The theorem is a real branch reduction, not a proof of (1.4).  A later
weighted refinement shows that the maximum product in (1.4) is not the
preferred way to pay endpoint contact: the exact local pencil moment removes
`h_z` and never multiplies unrelated maxima.  The fully clean
common-neighbour packing remains the other load-bearing branch.

## 2. Endpoint incidences in one component

A cell in component `z` is

\[
 C_z(b)=(b,z+Lb),\qquad L=I+J.                  \tag{2.1}
\]

Every nonisolated vertex of the matching graph has two nonzero directed
edge labels in `D=A-A`, and the two edge labels have disjoint physical
endpoint pairs.  Hence the cell has exactly four physical endpoints.

For any vertex subset `W` of size `n`, write `f_x` for the number of cells
in `W` containing `x in A`.  Then

\[
 \sum_xf_x=4n,
 \qquad f_x\le\kappa_z.                         \tag{2.2}
\]

The number `P_W` of unordered cell pairs in `W` sharing at least one
physical endpoint is at most

\[
\begin{aligned}
 P_W
 &\le\sum_x{f_x\choose2}\\
 &\le {\kappa_z-1\over2}\sum_xf_x
 <2\kappa_zn.                                   \tag{2.3}
\end{aligned}
\]

There is also the universal calibration `kappa_z<=4(k-1)`: if a fixed
point is used by the first edge label, there are at most `2(k-1)` possible
directed labels `b`, and `b` determines the cell.  The same bound holds for
the second edge label.  The point of (1.2), however, is to retain the actual
component occupancy rather than replace it by this crude global maximum.

## 3. Contact-aware codegree theorem

Take a nonempty induced subgraph of `H_z` on `n` vertices with minimum
degree `delta`.  Count unordered length-two paths by their centre and by
their endpoint pair:

\[
 n{\delta\choose2}
 \le\sum_x{d(x)\choose2}
 =\sum_{u<v}|N(u)\cap N(v)|.                    \tag{3.1}
\]

Split the last sum according to whether the endpoint cells `u,v` have a
physical endpoint contact.  There are fewer than `2 kappa_z n` contact
pairs by (2.3), and every pair has codegree at most `n`.  Every remaining
pair has codegree at most `r_z^circ`.  Therefore

\[
 n{\delta\choose2}
 \le2\kappa_zn^2+r_z^\circ{n\choose2}.          \tag{3.2}
\]

It follows that

\[
 \delta(\delta-1)
 \le(4\kappa_z+r_z^\circ)n
 \le(4\kappa_z+r_z^\circ)h_z.                  \tag{3.3}
\]

This proves the simple degeneracy bound in (1.3).  Orient a degeneracy
ordering and replace every simple edge by its at most `mu_z` parallel
copies to obtain the weighted statement.  The same dyadic optimal-core
argument as in `SWAP_MATCHING_C4_COMMON_NEIGHBOUR_GATE.md` now proves the
sufficiency of (1.4).

## 4. Repeated `r` is diagonal-invariant

Label the ordinary sums on a matching four-cycle consecutively by

\[
 s_{01},s_{12},s_{23},s_{30}.                   \tag{4.1}
\]

The diagonal `(0,2)` has a repeated-`r` realization using these four edge
copies exactly when

\[
 s_{01}-s_{12}=s_{30}-s_{23}.                   \tag{4.2}
\]

The other diagonal `(1,3)` has a repeated-`r` realization exactly when

\[
 s_{01}-s_{30}=s_{12}-s_{23}.                   \tag{4.3}
\]

Equations (4.2) and (4.3) are equivalent: both say
`s_01+s_23=s_12+s_30`.  Thus repeated-`r` existence is invariant under
switching the diagonal.

Every cycle edge already joins two physically disjoint cells.  Therefore
every endpoint contact among the four cells lies on a diagonal.  If a
repeated-`r` four-cycle has any contact, switch to that diagonal; (4.2)--
(4.3) preserve the repeated-`r` witness, and (3.2) charges it to the
endpoint-pencil term.  Consequently the repeated-`r` branch left after
(3.2) consists only of fully sixteen-endpoint cycles.  This rigorously
justifies the routing assertion that was only heuristic in the preceding
four-cycle note.

## 5. Fixed clean cell: exact eight-corner form

The clean residual has a useful lossless normal form.  Fix opposite cells

\[
 B=C_z(b),\qquad C=C_z(c),\qquad d=c-b,          \tag{5.1}
\]

and a common-neighbour extension with centre `U=C_z(u)`.  Let `s_C` be the
ordinary sum on `CU`, put

\[
 y=s_C-u,qquad r=s_B-s_C,
 \qquad R=J(r+Ld),                               \tag{5.2}
\]

and define

\[
 \phi=J(y-z-Lc).                                \tag{5.3}
\]

The two bases are exactly

\[
 a_C=u+\phi,qquad a_B=u+\phi+R.                \tag{5.4}
\]

Thus extension copies are in bijection with pairs `(u,y)` satisfying the
eight complete-difference memberships

\[
\boxed{
\begin{gathered}
u,\quad z+Lu,\quad y,\quad y+r,\\
u+y-c,\quad u+y+r-b,\\
u+\phi,\quad u+\phi+R\in D,
\end{gathered}}                                 \tag{5.5}
\]

and the four adaptive-popular conditions

\[
\boxed{
-\phi,\quad-\phi-R,\quad c-u-\phi,
\quad b-u-\phi-R\in\mathcal P_K.}              \tag{5.6}
\]

After fixed translations are removed, the four genuinely different linear
projections in (5.5) are

\[
 u,\qquad y,\qquad u+y,\qquad u+Jy.             \tag{5.7}
\]

Any two determine `(u,y)` because every corresponding two-by-two Gaussian
linear system is nonsingular (`J-I` has determinant two in the last case).
Hence a fixed clean `(B,C,r)` fibre is a pair-linear four-projection system,
not an arbitrary common-neighbour family.  The next clean packing theorem
must exploit this pair-linearity together with the physical endpoint
decoration and (5.6).

## 6. Exact stress

The endpoint-aware component parameters are:

| family | `K` | max `h_z` | max `kappa_z` | max `kappa_z h_z` | max clean codegree |
|---|---:|---:|---:|---:|---:|
| Costas 23 | 9.747 | 9 | 5 | 45 | 3 |
| Costas 29 | 9.518 | 10 | 5 | 45 | 5 |
| Costas 31 | 10.901 | 9 | 5 | 36 | 5 |
| Costas 37 | 11.036 | 11 | 6 | 55 | 6 |

In particular `kappa_z h_z/K^2` is below `0.50` in all four rows.  This is
evidence for the endpoint-pencil part of (1.4), not a proof.

On Costas 37, the 63,119 four-cycles split as follows:

| contact diagonals | repeated `r` on a contact diagonal | cycles |
|---:|:---:|---:|
| 0 | no | 8,016 |
| 0 | n/a (clean repeated `r`) | 8,796 |
| 1 | no | 15,192 |
| 1 | yes | 17,016 |
| 2 | no | 6,603 |
| 2 | yes | 7,496 |

Whenever exactly one diagonal has contact, repeated-`r` occurs on that
diagonal if and only if it occurs on the clean diagonal, exactly as (4.2)--
(4.3) require.

The lifted modular parabola at prime 43 has `K=11.747...`, maximum component
size three, maximum endpoint pencil two, product six, clean codegree one,
and no four-cycle.  The endpoint-pencil formulation therefore continues to
separate the known ambient equality model.

## 7. Verification and remaining theorem

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_matching_endpoint_pencil_clean_codegree.py
python3 phase2/loop/erdos1208/verify_swap_matching_endpoint_pencil_clean_codegree.py --larger
```

The verifier exhausts all subgraphs of a six-cell endpoint system, checks
(1.3), proves the diagonal equivalence (4.2)--(4.3), verifies (5.2)--(5.7),
and reproduces the Costas-17/23 profiles.  The optional run checks every
displayed Costas-37 count.

Estimate (1.4) remains sufficient, but its endpoint-pencil half has now
been superseded by the sharper aggregate gate

\[
 \sum_{C,x}\sum_{B<B':x\in E(B)\cap E(B')}
 m(C,B)m(C,B')\le K N^{o(1)}M.
\]

Read `SWAP_MATCHING_WEIGHTED_ENDPOINT_PENCIL_GATE.md`.  The direct attack
should therefore proceed in two pieces:

1. prove the weighted endpoint-pencil moment above, using its exact
   two-copy collision normal form;
2. apply the common-`r` support/collision dichotomy only to endpoint-clean
   opposite pairs, using the pair-linear system (5.5)--(5.7) for the
   repeated branch.

No raw common-endpoint count, unweighted `D-D` energy, or pointwise
fixed-cell uniqueness statement captures these two remaining products.
