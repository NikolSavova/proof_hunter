# Matching wedges and the diffuse twelve-endpoint gate

## 1. Outcome

This note sharpens the direct nested-core route in
`SWAP_OPTIMAL_ORIENTATION_NESTED_CORE_GATE.md`.  It does not prove the
remaining geometric estimate, but it identifies the first genuinely
higher-order object that would do so.

Let `G_sw` be the adaptive swap multigraph, let `E` be its total number of
edge copies, and let `U_t` be a quadratic-optimal load core.  Keep only core
edges whose four fixed directed differences have eight distinct physical
endpoints, and call the resulting multigraph `H_t`.  Write `M_t` for its
edge-copy count and

\[
 W_t=\sum_{v\in U_t}{d_{H_t}(v)\choose2}.            \tag{1.1}
\]

The exact graph calculation below shows that the linear wedge estimate

\[
 \boxed{W_t\le K N^{o(1)}M_t}                       \tag{1.2}
\]

implies

\[
 tM_t\le K N^{o(1)}E,                               \tag{1.3}
\]

and hence proves the matching part of the desired nested-core bound after
dyadic summation.  Here `N=|D|`, `K=|D+D|/|D|`, and `D=A-A`.

The physical endpoint decoration gives a canonical five-way partition of
`W_t`: parallel reuse, missing zero-vector potentials, repeated mixed
potentials, diffuse wedges with a neighbour contact, and diffuse wedges with
all twelve fixed endpoints distinct.  On the largest genuine stress the
last class is the largest one.  Thus the new load-bearing statement is a
linear bound for **diffuse twelve-endpoint wedges**, not another one-cell
load or shared-endpoint theorem.

## 2. Exact wedge reduction

Let `V_t` be the set of nonisolated vertices of `H_t`.  Since
`sum_v x_v=E` for the optimal orientation and every member of `U_t` has
`x_v>=t`,

\[
 |V_t|\le |U_t|\le {E\over t}.                       \tag{2.1}
\]

Also `sum_v d_{H_t}(v)=2M_t`.  Cauchy gives

\[
 \begin{aligned}
 W_t
 &=\frac12\left(\sum_vd_{H_t}(v)^2-2M_t\right)\\
 &\ge {2M_t^2\over |V_t|}-M_t
 \ge {2tM_t^2\over E}-M_t.                         \tag{2.2}
 \end{aligned}
\]

Combining (1.2) and (2.2), then dividing by `M_t`, yields

\[
 tM_t\le {1+K N^{o(1)}\over2}E.                    \tag{2.3}
\]

The logarithmic number of dyadic levels is absorbed by `N^{o(1)}`.  This is
why wedges are the correct next object: a linear estimate for their average
degree proves the required size-biased edge estimate.

## 3. Mixed endpoint potentials

Every nonzero `q in D` has a unique directed physical realization

\[
 q=x_q-y_q,qquad x_q,y_q\in A.                     \tag{3.1}
\]

Put `L=I+J`.  For a nonzero swap cell `C=(b,ell)` define

\[
 \alpha(C)=x_\ell-Lx_b,qquad
 \beta(C)=y_\ell-Ly_b.                             \tag{3.2}
\]

The component invariant has the endpoint factorization

\[
 \alpha(C)-\beta(C)=\ell-Lb=z(C).                  \tag{3.3}
\]

Consequently, inside one component,

\[
 \alpha(C)=\alpha(C')\quad\Longleftrightarrow\quad
 \beta(C)=\beta(C').                               \tag{3.4}
\]

This is stronger than an arbitrary coloring of the component: both colors
are physical affine endpoint coordinates, and their difference is exactly
the stored invariant.

### Clean potential-collision theorem

Let `C_i=(b_i,ell_i)`, `i=0,1`, lie in one component and have the same
mixed potential.  Assume the four directed vectors
`b_0,ell_0,b_1,ell_1` have eight distinct physical endpoints.  Define

\[
 d_X=x_{b_1}-x_{b_0},\qquad
 d_Y=y_{b_1}-y_{b_0}.                               \tag{3.5}
\]

Then

\[
 d_X,d_Y,Ld_X,Ld_Y\in D.                           \tag{3.6}
\]

Indeed equality of the two alpha coordinates and of the two beta
coordinates gives

\[
 x_{\ell_1}-x_{\ell_0}=Ld_X,qquad
 y_{\ell_1}-y_{\ell_0}=Ld_Y.                       \tag{3.7}
\]

Let

\[
 P_L=\{d\in D\setminus\{0\}:Ld\in D\}.            \tag{3.8}
\]

The map `(C_0,C_1) -> (d_X,d_Y)` is injective on ordered clean
same-potential pairs.  The vector `d_X` uniquely recovers the ordered pair
`(x_{b_1},x_{b_0})`, and `d_Y` recovers
`(y_{b_1},y_{b_0})`; alternatively `Ld_X,Ld_Y` recover both `ell` labels.
Thus

\[
 \boxed{
 \#\{\text{ordered clean same-potential cell pairs}\}
 \le |P_L|^2\le N^2.}                              \tag{3.9}
\]

Equation (3.9) is an exact distinct-pair bound.  It does not by itself
control parallel edge-copy weights or the number of common swap neighbours;
those multiplicities must remain in the wedge problem.

## 4. Five moving roles in one cell

For a fixed cell `C=(b,ell)`, an incident record may be written using a base
`a` and the head `c` of the neighbouring cell.  Its five moving members of
`D` are

\[
 \boxed{
 a,\quad c,\quad
 e=\ell-b+Lc-Ja,\quad
 d=\ell+J(c-a),\quad
 f=\ell+L(c-b).}                                   \tag{4.1}
\]

The last role is affine-bijective with `c`, so there are four genuinely
different projections.  On the highest-load genuine cells none of these
projections is injective, but every observed fibre remains small.  For the
largest cell in each stored core, the analyzer reports

| family | load | incident copies | distinct values in `(a,c,e,d,f)` | maximum multiplicities |
|---|---:|---:|---:|---:|
| Costas 29 | 12 | 31 | `(13,8,16,11,8)` | `(6,6,4,5,6)` |
| Costas 31 | 13 | 28 | `(14,5,17,11,5)` | `(4,7,3,5,7)` |
| Costas 37 | 13 | 31 | `(12,9,16,12,9)` | `(5,6,4,4,6)` |

This is a matching-like partial orthogonal array rather than a star.

## 5. Exact wedge partition and stress

At a centre cell, choose two incident matching edge copies.  The analyzer
partitions the pair as follows.

1. `parallel`: the two copies have the same neighbouring cell;
2. `missing-potential`: a fixed vector is zero, so (3.2) is unavailable;
3. `repeated-potential`: the neighbours are distinct but share alpha and
   beta;
4. `diffuse-neighbour-contact`: the potentials differ, but the two
   neighbouring cells share a physical endpoint;
5. `diffuse-twelve-distinct`: the centre and both neighbours together use
   twelve distinct physical endpoints.

These classes partition `W_t` exactly.  Their edge-copy-weighted values are

| family | parallel | repeated | contact | twelve-distinct | missing | total |
|---|---:|---:|---:|---:|---:|---:|
| Costas 17 | 428 | 3 | 120 | 10 | 6 | 567 |
| Costas 29 | 251614 | 1349 | 268373 | 231246 | 366 | 752948 |
| Costas 31 | 119724 | 577 | 95634 | 93615 | 0 | 309550 |
| Costas 37 | 661754 | 0 | 617368 | 839929 | 654 | 2119705 |

For Costas 37, the twelve-distinct branch is `39.62%` of all matching
wedges and is the largest class.  Every nonzero mixed-potential fibre in
that core has size one.  The hard configuration is therefore genuinely
diffuse: neither a repeated affine potential nor a shared physical endpoint
carries it.

## 6. The exact remaining theorem

The wedge reduction routes the direct cube-root attack into four geometric
estimates, each linear in the matching edge mass:

\[
 W_t^{\rm parallel},\quad W_t^{\rm repeated},\quad
 W_t^{\rm contact},\quad W_t^{12}
 \ \le\ K N^{o(1)}M_t.                            \tag{6.1}
\]

The first is a size-biased parallel-fibre theorem in the exact normal form
of `SWAP_CELL_COMPONENT_GATE.md`.  The second has the distinct-pair
compression (3.9).  The third belongs to the endpoint-contact remainder.
The new main gate is

\[
 \boxed{W_t^{12}\le K N^{o(1)}M_t.}               \tag{6.2}
\]

A twelve-distinct wedge consists of a centre `(b,ell)` and two branches

\[
 (b+t,\ell+Lt),\qquad (b+s,\ell+Ls),               \tag{6.3}
\]

together with one exact three-moving-member completion on each branch.
Any proof of (6.2) must retain both completions and the physical endpoint
realization.  Dropping either returns to the radial and abstract affine
countermodels already known to be too large.

The next useful calculation is therefore not another global moment.  It is
an exact normal form for a diffuse twelve-endpoint wedge plus one further
high-core extension at each neighbouring cell.  That decorated three-edge
configuration is the first place where the optimal-core density and the
Euclidean distance uniqueness are simultaneously present.

This calculation is carried out in
`SWAP_MATCHING_C4_COMMON_NEIGHBOUR_GATE.md`.  A high-degeneracy extension
forces two outer branches to meet, so the correct decorated object is a
matching swap-cell four-cycle.  The resulting codegree--component product is
now the preferred continuation of (6.2).

## 7. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_matching_wedge_potential_gate.py
python3 phase2/loop/erdos1208/analyze_swap_optimal_nested_cores.py --larger
```

The verifier exhaustively checks the mixed-potential injection on a genuine
eight-point integral distance-Sidon set, including a nonvacuous clean fibre,
checks the graph wedge inequality, and reproduces the smaller genuine wedge
profiles.  The larger analyzer verifies the full table above.
