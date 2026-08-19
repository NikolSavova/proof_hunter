# The swap-cell degeneracy charge

## 1. Outcome

This note gives the cleanest current sufficient theorem for the adaptive
off-diagonal tail in Erdős problem 1208.  It is an exact charge reduction,
not a proof of its final density estimate.

Let `G_sw` be the swap multigraph from `SWAP_CELL_COMPONENT_GATE.md`.  Its
vertices are fixed `D^2` charge cells, and every unordered pair `{p,q}` in
an adaptive rich fibre gives one multiedge between the cells of the ordered
records `(q,p)` and `(p,q)`.

Orient the edge copies so that every vertex has outdegree at most `d_sw`,
where `d_sw` is the weighted degeneracy of the multigraph.  Charge both
ordered records belonging to an edge copy to its tail, using one bit to
distinguish their orientations.  The charge lands in `2N^2` cells and its
second moment is at most

\[
 \boxed{Q_{\rm sw}\le d_{\rm sw}\mathcal O_K.}    \tag{1.1}
\]

Consequently the single local-density theorem

\[
 \boxed{d_{\rm sw}\le K N^{o(1)},
 \qquad K={|D+D|\over |D|}}                       \tag{1.2}
\]

implies

\[
 \mathcal O_K\le N^{1+o(1)}|D+D|,                \tag{1.3}
\]

and hence proves the cube-root upper bound for Erdős 1208.

The new gate has two advantages over the fixed-route moment:

1. stars are harmless, because all their edges can be oriented away from
   distinct leaves; and
2. a failure of (1.2) is exactly a genuinely dense endpoint-realizable
   multigraph core, not a large fibre or a one-sided charge concentration.

The normalized weighted degeneracy is between `0.028` and `1.743` on the
stored genuine stresses, while it grows from `3.835` to `23.302` on radial
controls of sides 4 through 8.  This is evidence only; (1.2) is not proved.

## 2. Definitions and the swap involution

Keep

\[
 D=A-A,\quad N=|D|,\quad S=|D+D|,\quad K=S/N,
\]

and write `L=I+J`.  A record in the fibre `(u,s)`, with `w=s-u`, consists
of distinct adaptive-popular shifts `(q,p)` and

\[
 u,\ u+q,\ u+p,\ w-q,\ w-p,\ w-Lq,\ w-Lp\in D.   \tag{2.1}
\]

Its fixed cross-pair cell is

\[
 C(q,p)=(u+q,w-Lp)\in D^2.                       \tag{2.2}
\]

Swapping the two shifts gives

\[
 C(p,q)=(u+p,w-Lq).                              \tag{2.3}
\]

The multigraph `G_sw` has these active cells as vertices and one undirected
edge copy between (2.2) and (2.3) for every unordered pair `{p,q}` in every
adaptive fibre.  There are no loops because `p!=q`.  If `m_xy` is a
parallel multiplicity, then

\[
 |E(G_{\rm sw})|=\sum_{\{x,y\}}m_{xy}
 ={1\over2}\mathcal O_K.                         \tag{2.4}
\]

The affine component invariant proved in the preceding note remains
available:

\[
 C(q,p)=(b,\ell),\quad C(p,q)=(b+t,\ell+Lt),
 \quad t=p-q,                                    \tag{2.5}
\]

so both endpoints have the same value

\[
 z=\ell-Lb.                                      \tag{2.6}
\]

## 3. Weighted degeneracy orientation

For a multigraph `G`, define its weighted degeneracy by

\[
 d(G)=\max_{H\subseteq G,\ H\ne\varnothing}\delta(H),         \tag{3.1}
\]

where degrees count edge copies.  Repeatedly remove a current
minimum-degree vertex.  Orient every edge copy from the endpoint removed
first to the endpoint removed later.  At the moment a vertex is removed,
its remaining weighted degree is its final outdegree.  Therefore

\[
 \max_v d^+(v)\le d(G).                           \tag{3.2}
\]

This is the standard degeneracy orientation and works verbatim for parallel
edges.  Equivalently, `d(G)` is within a constant factor of the multigraph
arboricity.  The local-density meaning is explicit: if `d(G)>d`, then some
nonempty subgraph has minimum weighted degree greater than `d`, and hence
more than `d|V|/2` edge copies.

## 4. The adaptive orientation charge

Fix an orientation satisfying (3.2).  An edge copy represents two ordered
records, one whose original fixed cell is each endpoint.  Charge both to
the tail of the oriented edge and append one bit recording which of the two
ordered records is being charged.  Thus the target is

\[
 \{0,1\}\times D^2,                              \tag{4.1}
\]

of size at most `2N^2`.

For a fixed bit and vertex `v`, the load is exactly `d^+(v)`.  The bit also
preserves fibrewise injectivity: within a fixed fibre, a fixed cell uniquely
recovers the ordered pair `(q,p)`, and the bit records whether that cell was
the record's original or swapped cell.

The total charge mass is

\[
 \sum_{\epsilon,v}\lambda(\epsilon,v)
 =2\sum_vd^+(v)=2|E(G_{\rm sw})|=\mathcal O_K.    \tag{4.2}
\]

Its second moment is

\[
 \begin{aligned}
 Q_{\rm sw}
 &=2\sum_vd^+(v)^2\\
 &\le2d_{\rm sw}\sum_vd^+(v)\\
 &=d_{\rm sw}\mathcal O_K,
 \end{aligned}                                   \tag{4.3}
\]

which proves (1.1).

Cauchy--Schwarz in the target (4.1) now gives

\[
 \mathcal O_K^2
 \le2N^2Q_{\rm sw}
 \le2N^2d_{\rm sw}\mathcal O_K.                 \tag{4.4}
\]

After cancelling a nonzero `O_K`, assumption (1.2) yields

\[
 \mathcal O_K\le2N^2K N^{o(1)}
 =2NSN^{o(1)},                                    \tag{4.5}
\]

which is the required adaptive-tail estimate.

The factor two and the orientation bit are immaterial.  They are kept to
make the charge literally injective within each fibre and the verification
identity exact.

## 5. Relation to the component-product gate

Let component `z` have `h_z` active vertices and maximum parallel
multiplicity `r_z`.  Every induced subgraph of this component has weighted
minimum degree at most `(h_z-1)r_z`; hence

\[
 d_{\rm sw}\le\max_z(h_z-1)r_z.                  \tag{5.1}
\]

Thus the pointwise component-product condition from
`SWAP_CELL_COMPONENT_GATE.md` implies (1.2).  The converse is false: a
component may have many vertices or one large parallel class while still
admitting a sparse peeling order.  Weighted degeneracy is therefore a
strictly more adaptive pointwise target.

The size-biased component envelope remains weaker still and should be used
if one exceptional dense core makes the maximum in (3.1) too strong.  The
logical hierarchy is

\[
 \text{component max product}
 \Longrightarrow \text{degeneracy gate}
 \Longrightarrow \text{orientation charge},      \tag{5.2}
\]

while the already-proved component envelope is an independent
size-biased majorant for the original fixed-route moment.

## 6. Exact calibration

The verifier reports

\[
 (N,S,\mathcal O_K,|V|,|E_{\rm simple}|,
 d_{\rm sw},Q_{\rm sw}).                         \tag{6.1}
\]

Selected exact profiles are:

| family | profile | `d_sw/K` | `Q_sw/(K O_K)` |
|---|---:|---:|---:|
| closure 40 | `(1561,156057,370516,216909,173240,9,565440)` | `0.0900` | `0.0153` |
| Costas 11 | `(91,707,2264,1558,992,4,3264)` | `0.5149` | `0.1856` |
| Costas 17 | `(241,2299,20014,12397,8089,6,34234)` | `0.6290` | `0.1793` |
| Costas 23 | `(463,4513,498674,133927,145055,12,1873578)` | `1.2311` | `0.3855` |
| Costas 31 | `(871,9495,765102,286810,249531,19,2509386)` | `1.7429` | `0.3009` |
| radial 4 | `(29,121,8330,773,1417,16,67646)` | `3.8347` | `1.9463` |
| radial 5 | `(39,181,24716,1437,3416,26,329356)` | `5.6022` | `2.8713` |
| radial 6 | `(53,253,93290,2715,8881,51,2377470)` | `10.6838` | `5.3387` |
| radial 8 | `(83,431,555948,6769,33522,121,33414416)` | `23.3016` | `11.5745` |

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_cell_degeneracy_charge.py
```

The script checks the multigraph multiplicities, peeling orientation,
outdegrees, two-bit fibrewise injectivity, exact charge loads, second-moment
identity, and every profile above.

## 7. Remaining theorem

The live statement is now a dense-core prohibition:

> Every nonempty submultigraph of `G_sw` has a vertex of weighted degree at
> most `K N^(o(1))`.

A black-box graph theorem cannot prove this: abstract radial transversals
produce swap graphs whose normalized degeneracy grows rapidly.  A proof
must use the complete endpoint realization `D=A-A`.  In the component
coordinates of the preceding note, a hypothetical dense core simultaneously
contains

\[
 (b,z+Lb),\quad (b+t,z+L(b+t))in D^2            \tag{7.1}
\]

and, for every parallel record,

\[
 b+t+Je,\quad z+Lb+e,\quad z+Lb+e+t\in D.        \tag{7.2}
\]

with `-Je` and `-Je-t` adaptive-popular.  The next proof must show that a
subgraph with minimum weighted degree much larger than `K` forces enough
ordinary sums to increase `S`, or else a negative Fourier component
incompatible with

\[
 \widehat{1_D}=|\widehat{1_A}|^2-(|A|-1).
\]

Unlike a maximum-fibre statement, minimum degree guarantees that this
structure persists after arbitrary vertex deletions.  That robustness is
the main reason the degeneracy gate is a plausible density-increment entry
point.
