# The swap-cell component gate

## 1. Outcome

This note gives a new exact decomposition of the fixed cross-pair charge in
`ADAPTIVE_CROSS_PAIR_D2_CHARGE_GATE.md`.  It does **not** prove the remaining
load estimate.

Every ordered record occurs with its `p<->q` swap.  Regard the two fixed
charge cells as the endpoints of an undirected multiedge.  The resulting
swap multigraph has three useful properties:

1. its weighted vertex degrees are exactly the fixed-charge loads;
2. every connected component has the affine invariant
   `ell-(I+J)b`; and
3. every parallel-edge multiplicity is exactly a three-copy intersection
   with both adaptive-popular shifts retained.

An elementary componentwise Cauchy inequality then majorizes the missing
second moment by

\[
 \boxed{
 \mathcal B_{\rm sw}
 =2\sum_z(h_z-1)\sum_{e\in E_z}m_e^2.}            \tag{1.1}
\]

Here `h_z` is the number of active vertices in component `z` and `m_e` is
an edge multiplicity.  Therefore the size-biased estimate

\[
 \boxed{
 \mathcal B_{\rm sw}\le K N^{o(1)}\mathcal O_K,
 \qquad K={|D+D|\over |D|},}                     \tag{1.2}
\]

proves the adaptive tail and hence the cube-root upper bound in Erdős 1208.
The stronger pointwise condition

\[
 (h_z-1)\max_{e\in E_z}m_e\le K N^{o(1)}         \tag{1.3}
\]

also suffices.  The value of the decomposition is that (1.3) couples two
different kinds of concentration.  A counterexample must simultaneously
have a large affine `(I+J)` overlap and a large three-copy parallel fibre;
neither concentration alone is now the target.

## 2. The swap multigraph

Let `D=A-A`, `N=|D|`, `S=|D+D|`, `K=S/N`, and put `L=I+J`.  A record in the
adaptive fibre `(u,s)`, with `w=s-u`, consists of distinct popular shifts
`q,p` and the seven members

\[
 u,\ u+q,\ u+p,\ w-q,\ w-p,\ w-Lq,\ w-Lp\in D.  \tag{2.1}
\]

The fixed cross-pair charge of the ordered record `(q,p)` is

\[
 C_0=(b,\ell)=(u+q,w-Lp)\in D^2.                 \tag{2.2}
\]

Its swapped record `(p,q)` has cell

\[
 C_1=(u+p,w-Lq).                                  \tag{2.3}
\]

Put `t=p-q`.  Equations (2.2)--(2.3) give

\[
 \boxed{C_1=(b+t,\ell+Lt).}                      \tag{2.4}
\]

Define `G_sw` to have the active charge cells as vertices and one undirected
edge for every unordered pair `{p,q}` in every adaptive fibre.  Different
fibre records can produce the same two cells, so this is a multigraph; write
`m_xy` for the multiplicity of the edge `{x,y}`.

### Proposition 2.1: exact degree identity

If `d(C)` is the weighted degree of a cell, then

\[
 d(C)=\lambda(C),                                \tag{2.5}
\]

where `lambda` is the fixed-route load.  Indeed, every ordered record is
incident to its own cell, while the swapped ordered record is incident to
the other endpoint of the same undirected edge.  Consequently

\[
 \mathcal O_K=\sum_Cd(C)=2\sum_{\{x,y\}}m_{xy},  \tag{2.6}
\]

and the missing moment is exactly

\[
 M=\sum_Cd(C)^2.                                 \tag{2.7}
\]

## 3. The affine component invariant

For a cell `C=(b,ell)`, define

\[
 z(C)=\ell-Lb.                                   \tag{3.1}
\]

Equation (2.4) gives

\[
 z(C_1)=\ell+Lt-L(b+t)=\ell-Lb=z(C_0).           \tag{3.2}
\]

Thus every edge, and hence every connected component, lies in one level
set of `z`.  A vertex in component `z` has the form

\[
 (b,z+Lb),\qquad b\in D,\quad z+Lb\in D.          \tag{3.3}
\]

In particular its active vertex count `h_z` is bounded by the affine overlap

\[
 H_z=|D\cap L^{-1}(D-z)|.                         \tag{3.4}
\]

The qualification "active" matters.  A generic segment construction can
make (3.4) large while making the global support `S`, and therefore `K`, so
large that no associated adaptive edge survives.  The gate concerns the
component after both popular-shift conditions and all seven incidences have
been imposed.

## 4. Exact parallel-edge normal form

Fix an oriented edge from `(b,ell)` to `(b+t,ell+Lt)`.  For a record on this
edge put

\[
 e=Jp.                                            \tag{4.1}
\]

Since `Je=-p`, the seven `D`-members split into four fixed and three moving
members:

\[
 \boxed{
 b,\ b+t,\ \ell,\ \ell+Lt,\quad
 b+t+Je,\ \ell+e,\ \ell+e+t\in D.}              \tag{4.2}
\]

The two adaptive-popular shifts are recovered as

\[
 p=-Je,\qquad q=-Je-t.                            \tag{4.3}
\]

Conversely, every `e` satisfying (4.2)--(4.3) reconstructs the record.
Hence the parallel multiplicity is exactly

\[
 m_{b,\ell,t}=
 \#\{e:\ b+t+Je,\ell+e,\ell+e+t\in D,
             -Je,-Je-t\in\mathcal P_K\}.          \tag{4.4}
\]

The two factors in (1.3) are now geometrically distinct:

* `h_z` counts an affine overlap between `D` and a translate of `LD`;
* `m_{b,ell,t}` counts a three-copy intersection inside that active
  overlap, with the bidirectional popularity conditions retained.

The sparse-shear and generic-row barriers show that either quantity can be
large in a weakened model.  They do not presently supply a genuine complete
difference with their product large relative to `K`.

## 5. Componentwise Cauchy theorem

Let `E_z` denote the set of distinct multiedges in component `z`.  A vertex
`x` has at most `h_z-1` distinct neighbours.  Therefore

\[
 d(x)^2
 =\left(\sum_y m_{xy}\right)^2
 \le(h_z-1)\sum_y m_{xy}^2.                      \tag{5.1}
\]

Summing over the component counts each undirected parallel class twice and
gives

\[
 \sum_{x\in V_z}d(x)^2
 \le2(h_z-1)\sum_{e\in E_z}m_e^2.                \tag{5.2}
\]

Summing (5.2) proves

\[
 \boxed{M\le\mathcal B_{\rm sw}.}                \tag{5.3}
\]

If `r_z=max_e m_e`, then

\[
 \mathcal B_{\rm sw}
 \le2\sum_z(h_z-1)r_z\sum_{e\in E_z}m_e.         \tag{5.4}
\]

Equations (2.6), (5.3), and (5.4) prove both sufficient statements
(1.2)--(1.3).  This is an unconditional graph reduction; the only unproved
part is the endpoint-sensitive estimate of its final right-hand side.

## 6. Exact calibration

The verifier reports

\[
 (N,S,\mathcal O_K,|V|,\#\text{components},h_{\max},m_{\max},
 M,\sum m_e^2,\mathcal B_{\rm sw}).
\]

Selected profiles are:

| family | profile | `M/(K O_K)` | `B_sw/(K O_K)` |
|---|---:|---:|---:|
| closure 40 | `(1561,156057,370516,216909,41293,47,6,1139274,212806,5602992)` | `0.03076` | `0.15126` |
| Costas 11 | `(91,707,2264,1558,648,6,4,4348,1432,6188)` | `0.24719` | `0.35180` |
| Costas 17 | `(241,2299,20014,12397,5057,7,5,46212,14343,62000)` | `0.24205` | `0.32474` |
| Costas 23 | `(463,4513,498674,133927,41481,11,7,3020644,547433,4087164)` | `0.62144` | `0.84085` |
| radial 4 | `(29,121,8330,773,177,9,6,111622,15213,136252)` | `3.21157` | `3.92022` |
| radial 5 | `(39,181,24716,1437,283,12,9,562304,56274,686344)` | `4.90206` | `5.98342` |
| radial 6 | `(53,253,93290,2715,423,16,12,4120768,304937,4861720)` | `9.25334` | `10.91717` |

The exact envelope remains below the target normalization on every genuine
complete-difference stress in the table and separates increasingly strongly
from the abstract radial transversals.  This is finite evidence, not a proof
of (1.2).  Notably, the coarse product `hmax*mmax` is much less sharp than
the size-biased envelope; the latter should remain the primary target.

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_cell_component_gate.py
```

The script checks the swap involution, component invariant, exact
three-copy parameterization, multiplicities, degree identity, Cauchy
envelope, and all stored profiles using integer arithmetic.

## 7. Next mathematical step

The live theorem is (1.2), not separate pointwise bounds for (3.4) and
(4.4).  A viable proof should dyadically restrict to components with
`h_z about H` and parallel classes with `m_e about R`, then show that

\[
 HR\gg K N^{o(1)}
\]

forces either:

1. enough ordinary sums to raise `S=|D+D|`; or
2. a structured subset of `D` whose negative Fourier mass violates
   `widehat(1_D)>=-(|A|-1)` unless the complement supplies the missing
   support.

The product formulation is designed to retain both load-bearing pieces:
large affine overlap and repeated three-copy reuse.  Proving a theorem about
either piece in isolation is ruled out by the existing barriers.
