# The adaptive cross-pair transpose graph

## 1. Status and outcome

This note sharpens the remaining cross-pair gate for Erdős problem 1208.
It does **not** prove the missing moment estimate.  It gives three exact
reductions:

1. every record in a fixed `D^2` charge cell is a seven-point affine pattern
   in two vector variables;
2. the missing charge moment is exactly the left-degree second moment of a
   simple bipartite graph; and
3. every four-cycle in that graph forces an additive parallelogram of
   adaptive-popular shifts, with all seven endpoint decorations retained.

The four-cycle theorem is a real structural gain, but the first natural
completion is false: charging a four-cycle only to its popular-shift
parallelogram has polynomially growing multiplicity on the stored Costas
families.  Thus any successful use of the transpose graph must retain the
canonical endpoint decorations coming from `D=A-A`.

Throughout, let

\[
 D=A-A,\qquad N=|D|,\qquad S=|D+D|,\qquad K=S/N,
\]

let `J(x,y)=(-y,x)`, and put `L=I+J`.  For an adaptive rich fibre
`F=(u,s)`, write `w=s-u` and

\[
 Q_F=\{q:\ u+q,\ w-q,\ w-Lq\in D\}.
\]

The shifts in `Q_F` also obey `R_D(q)>K` and `R_D(Jq)>K`.  The ordered
off-diagonal mass is

\[
 \mathcal O_K=\sum_F |Q_F|(|Q_F|-1).
\]

The fixed route from `ADAPTIVE_CROSS_PAIR_D2_CHARGE_GATE.md` charges
`(F,q,p)`, `q!=p`, to

\[
 \Psi_{02}(F,q,p)=(u+q,w-Lp)\in D^2.                 \tag{1.1}
\]

If `lambda` is its load, the still-missing sufficient estimate is

\[
 \sum_{b,\ell}\lambda(b,\ell)^2
 \le K N^{o(1)}\mathcal O_K.                        \tag{1.2}
\]

Together with fibrewise injectivity and Cauchy--Schwarz, (1.2) gives
`O_K<=NSN^(o(1))`, hence the cube-root upper bound.

## 2. Fixed-cell seven-point normal form

Fix a charge cell

\[
 b=u+q,\qquad \ell=w-Lp.                            \tag{2.1}
\]

Introduce

\[
 t=p-q,\qquad e=Jp.                                 \tag{2.2}
\]

Then the seven `D`-members in the record become

\[
 \boxed{
 b,\ b+t,\ b+t+Je,\quad
 \ell,\ \ell+e,\ \ell+e+t,\ \ell+Lt
 }\subset D.                                        \tag{2.3}
\]

Indeed, since `Je=-p`, the first three entries are

\[
 u+q,\quad u+p,\quad u,
\]

and the last four are

\[
 w-Lp,\quad w-p,\quad w-q,\quad w-Lq.
\]

The adaptive-popular shifts are recovered without loss:

\[
 p=-Je,\qquad q=-Je-t.                              \tag{2.4}
\]

Thus a large fixed-cell load is exactly a large family of pairs `(t,e)`
satisfying the seven simultaneous translates (2.3), with the two prescribed
popular shifts (2.4).  This is a more economical normal form than the
earlier collision-displacement list: it describes every preimage in the
cell, not merely the difference of two preimages.

## 3. The transpose graph

Define a bipartite graph `G` as follows.  Its left vertices lie in `D^2`,
its right vertices lie in `(D+D)^2`, and a record `(u,s,q,p)` gives the edge

\[
 (b,\ell)=(u+q,w-Lp)
 \quad\longleftrightarrow\quad
 (s,r)=(s,s-q).                                     \tag{3.1}
\]

### Theorem 3.1: simplicity and exact inversion

The graph `G` is simple.  Given its two endpoints, the full record is
recovered by

\[
 \begin{aligned}
 q&=s-r,\\
 u&=b-s+r,\\
 w&=2s-b-r,\\
 p&=L^{-1}(2s-b-r-\ell).
 \end{aligned}                                      \tag{3.2}
\]

Here `L^{-1}` is integral on every actual edge.  Formula (3.2) proves both
simplicity and the equivalence between edge validity and the original seven
`D`-incidences plus adaptive popularity.

### Corollary 3.2: the missing moment is a degree moment

The degree of the left vertex `(b,ell)` is exactly the fixed-route load
`lambda(b,ell)`.  Consequently

\[
 \boxed{
 \sum_{b,\ell}\lambda(b,\ell)^2
 =\sum_{x\in V_L(G)}d_G(x)^2.
 }                                                    \tag{3.3}
\]

The right vertex `(s,r)` is equivalently `(s,q)`, because `q=s-r`.  Its
degree is

\[
 \mu(s,q)=\sum_{u:\ q\in Q(u,s)}(|Q(u,s)|-1).        \tag{3.4}
\]

Thus transposition exchanges a fixed endpoint/opposite-endpoint charge cell
with a fixed fibre sum and primary popular shift.  This is the first exact
formulation in which both moment directions remain visible in one simple
graph.

## 4. Four-cycle rectangle theorem

Take a four-cycle with left vertices

\[
 L_i=(b_i,\ell_i),\qquad i\in\{0,1\},
\]

and right vertices

\[
 H_j=(s_j,r_j),\qquad j\in\{0,1\}.
\]

Let `(u_ij,s_j,q_j,p_ij)` be the record at corner `(i,j)`.  Put

\[
 \begin{aligned}
 \beta&=b_1-b_0,&
 \lambda_0&=\ell_1-\ell_0,&
 \alpha&=L^{-1}(-\beta-\lambda_0),\\
 \sigma&=s_1-s_0,&
 \rho&=r_1-r_0,&
 \eta&=L^{-1}(2\sigma-\rho).
 \end{aligned}                                      \tag{4.1}
\]

Applying (3.2) at the four corners gives the exact affine rectangle

\[
 \boxed{p_{ij}=p_{00}+i\alpha+j\eta.}                \tag{4.2}
\]

In particular, the four secondary adaptive-popular shifts form an additive
parallelogram.  The primary shift depends only on the right vertex:

\[
 q_j=s_j-r_j.                                        \tag{4.3}
\]

The other parameters also form affine rectangles; for example

\[
 u_{ij}=u_{00}+i\beta-j(\sigma-\rho).                \tag{4.4}
\]

Most importantly, (4.2) is not a projection of an arbitrary graph cycle.
Every corner still carries the full seven-point pattern (2.3) inside the
same complete difference set `D=A-A`, and all six shifts in (4.2)--(4.3)
remain adaptive-popular.

## 5. Exact calibration and the first barrier

The verifier reports graph profiles

\[
 (N,|E|,|V_L|,|V_R|,\sum d_L^2,\sum d_R^2,\max d_R)
\]

and four-cycle profiles

\[
 (C_4,\Delta_{LL},\Delta_{RR},
 C_{00},C_{10},C_{01},C_{11},\#P,\max m_P).
\]

Here `Delta_LL` is the maximum number of common right neighbours of a left
pair, `Delta_RR` is its transpose, `C_ab` counts cycles according as
`alpha=0` and/or `eta=0`, and `m_P` is the multiplicity of the unordered
popular-shift quadruple in (4.2).

Selected exact rows are:

| family | graph profile | `C4` | `(C00,C10,C01,C11)` | max shift-quad multiplicity |
|---|---:|---:|---:|---:|
| closure 40 | `(1561,370516,216909,219180,1139274,1443180,156)` | `22980` | `(10512,1601,10491,376)` | `172` |
| Costas 11 | `(91,2264,1558,1340,4348,6612,18)` | `61` | `(34,23,2,2)` | `8` |
| Costas 17 | `(241,20014,12397,7750,46212,96798,33)` | `2100` | `(1320,396,302,82)` | `50` |
| Costas 23 | `(463,498674,133927,62350,3020644,11782418,230)` | `676822` | `(547140,55340,67846,6496)` | `1959` |

The first entry in each degeneracy tuple is the genuinely two-dimensional
case `alpha!=0`, `eta!=0`; it is the majority in every Costas row.  Hence
the cycle mass cannot be dismissed as zero-direction stars.

On the other hand, the last column grows rapidly.  Therefore the map

\[
 \text{four-cycle}\longmapsto
 \{p_{00},p_{10},p_{01},p_{11}\}
\]

is far from bounded-to-one.  An additive-energy estimate for the popular
shift set alone discards precisely the endpoint variables that distinguish
the genuine complete-difference examples from the radial countermodels.
This closes the most immediate `C4 -> popular additive energy` shortcut.

Run

```bash
python3 phase2/loop/erdos1208/verify_adaptive_cross_pair_transpose_graph.py
python3 phase2/loop/erdos1208/verify_adaptive_cross_pair_transpose_graph.py --extended
```

The default run checks closure sizes 30 and 40 and Costas primes 11 and 17.
The extended run adds the substantially larger Costas-23 cycle census.

## 6. Remaining endpoint-sensitive target

The graph formulation suggests two viable, equivalent styles of next lemma:

1. a size-biased two-sided degree theorem controlling
   `sum_x d_L(x)^2` at the natural factor `K`; or
2. a lift-multiplicity theorem for the parallelogram (4.2) which retains
   `(q_0,q_1)` and enough of the seven canonical endpoint decorations to
   charge every additional lift to `|D+D|`.

Neither theorem is proved here.  The regression data show why the endpoint
condition must remain load-bearing.  The next proof should use either the
positive-definite identity

\[
 \widehat{1_D}=|\widehat{1_A}|^2-(|A|-1)
\]

or an equivalent combinatorial switch among the actual `A`-endpoints of the
seven differences.  Pure graph supersaturation, additive energy of the
popular shifts, and the affine rectangle identities alone are insufficient.
