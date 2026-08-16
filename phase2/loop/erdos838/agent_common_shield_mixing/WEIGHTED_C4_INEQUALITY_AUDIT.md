# Weighted `C4` inequality audit

## Status

The proposed universal inequality survives every exact and numerical test in this
audit, but I do **not** have a proof.  Nor did the audit find a counterexample.
The useful output is an exact normalization, a sharper spectral atom, a scalable
near-extremal family, and the precise consequence for the ACP repair graph.

Throughout, `A` is the `0,1` biadjacency matrix of a finite simple bipartite
graph.  Put

\[
 d_i=\sum_j A_{ij},\qquad e_j=\sum_i A_{ij},\qquad
 m=\sum_{ij}A_{ij}.
\]

Repeated vertices are allowed in all homomorphism counts.  Thus

\[
 C=\sum_{i,k,j,l}A_{ij}A_{il}A_{kj}A_{kl}
   =\operatorname {tr}(AA^*)^2=\|A\|_{S_4}^4
\]

is the ordered `C4` hom-count, and

\[
 W=\sum_{i,k,j,l}A_{ij}A_{il}A_{kj}A_{kl}d_i d_k e_j e_l
   =\|D^{1/2}AE^{1/2}\|_{S_4}^4 .
\]

The conjecture is

\[
 \boxed{W\le m^2C.}\tag{1}
\]

Equivalently, if `S_4` is the four-sunlet (one pendant edge at each
vertex of a four-cycle), then in oriented bipartite hom notation

\[
 \operatorname{hom}(S_4,G)
 \le \operatorname{hom}(C_4,G)\operatorname{hom}(K_2,G)^2.
\]

## 1. Exact probability formulation

Let `P` be the uniform law on the `m` edges.  Its left and right
marginals are `p_i=d_i/m` and `q_j=e_j/m`.  Then

\[
 \frac{C}{m^2}
 =\Pr\{(I,L),(K,J)\in E\},
\]

when `(I,J)` and `(K,L)` are independent uniform edges, whereas

\[
 \frac{W}{m^4}
 =\Pr\{(I,J),(I,L),(K,J),(K,L)\in E\},
\]

when `I,K` are iid from `p` and `J,L` are iid from `q`.
Consequently (1) says that the latter rectangle probability is at
most the former cross-edge probability.

The likelihood ratio on an existing edge between the product-marginal
law and the uniform-edge law is

\[
 x_{ij}=\frac{d_i e_j}{m}.
\]

If `R` is the symmetric compatibility matrix on the edge set,
`R_{(i,j),(k,l)}=A_{il}A_{kj}`, then

\[
 C={\bf1}^TR{\bf1},\qquad W=m^2x^TRx.
\]

Thus (1) is also the exact statement that the `R`-weighted mean of
`x_e x_f` is at most one.  Pointwise bounds cannot prove this: some
existing edges have `d_i e_j>m`.

## 2. The tempting Ky--Fan strengthening is false

Put `T=D^{1/2}AE^{1/2}`.  A plausible strengthening was

\[
 \big(s_r(T)^2\big)_r\ \prec_w\
 m\big(s_r(A)^2\big)_r.                                      \tag{2}
\]

It is false already in its first prefix.  Let `A_n` be the `n x n`
double-star matrix with one universal row and one universal column,
sharing their central entry.  In block form, with `r=n-1`,

\[
 A_n=\begin{pmatrix}0_{r\times r}&\mathbf1_r\\
 \mathbf1_r^T&1\end{pmatrix},\qquad m=2n-1.
\]

Its nonzero eigenvalues solve `lambda^2-lambda-r=0`.  All leaf degrees
are one and the central degrees are `n`, so

\[
 T_n=\begin{pmatrix}0_{r\times r}&\sqrt n\,\mathbf1_r\\
 \sqrt n\,\mathbf1_r^T&n\end{pmatrix},
\]

whose nonzero eigenvalues solve `mu^2-n mu-nr=0`.  At `n=7`,
`lambda_+=3` and `mu_+=(7+sqrt(217))/2`.  Hence

\[
 s_1(T_7)^2=\frac{133+7\sqrt{217}}2>117
 =13s_1(A_7)^2,
\]

because `49*217=10633>10201=101^2`.  This is an exact counterexample
to (2), including in the edge-incidence formulation with `P circ Q=I`.

It does not refute the original trace inequality: direct calculation gives

\[
 (m,C,W)=(13,97,14161),\qquad W/(m^2C)=14161/16393<1.
\]

Thus amplification of the leading singular mode is compensated by the
remaining mode in the Schatten-fourth-power sum.  A proof of (1) cannot
proceed through (2).

Individual singular-value domination also fails.  For example the matrix

```
1 1 1 1 1
1 0 1 1 0
1 1 0 1 1
1 1 1 1 0
1 1 1 0 1
```

violates `s_5(T)^2 <= m s_5(A)^2`.  Likewise the tempting operator estimate
`||T||_op^2 <= C` is false.  A proof must preserve compensation among
singular modes rather than bounding only the top mode.

## 3. Exact near-extremal family

Let `G_{a,b}` have `b` right vertices, one universal left vertex, and
`a` private left leaves adjacent to each right vertex.  Then

\[
 m=b(a+1),\qquad C=b(a^2+2a+b),
\]

and

\[
 W=(a+1)^2\big((a+b^2)^2+(b-1)a^2\big).
\]

Indeed `A^*A` has eigenvalues `a+b` once and `a` with multiplicity
`b-1`; `T^*T` has eigenvalues `(a+1)(a+b^2)` once and `(a+1)a`
with multiplicity `b-1`.

For `a=1`,

\[
 \frac{W}{m^2C}
 =\frac{b^4+2b^2+b}{b^3(b+3)}=1-\Theta(1/b).
\]

Hence no universal improvement `W <= (1-delta)m^2C` is possible.
This family also explains why estimates that discard the lower singular
modes are too weak.

## 4. Failed shortcuts (exact barriers)

Let

\[
 Z=\sum_{ij:A_{ij}=1}d_i e_j=\operatorname{hom}(P_4,G).
\]

Deleting the two cross edges from the sunlet gives the valid injection
`W <= Z^2`.  However `Z^2 <= m^2C` is false already for the three-edge
`L` matrix

```
1 1
1 0
```

where `(m,C,Z,W)=(3,7,8,56)`: `Z^2=64>63=m^2C`, although the desired
inequality still holds (`56<63`).

Other audited false shortcuts include

* the pointwise row-pair bound
  `(sum_{j in N(i) cap N(k)} e_j)sqrt(d_i d_k) <= m c_{ik}`;
* `||T||_op^2 <= C`;
* individual singular-value domination;
* separately bounding the left-weighted and right-weighted factors after
  Cauchy--Schwarz;
* `W <= m C^{3/2}` (also fails on the three-edge `L`, since
  `56>3*7^{3/2}`).

These failures are why a pinching argument must be a genuine trace/Ky--Fan
argument, not an operator-norm interpolation.

## 5. Verification performed

The companion verifier does the following without external packages.

1. Exhaustively enumerates every `p x q` `0,1` matrix for
   `1 <= p,q <= 4` (including all 65,536 `4 x 4` matrices) and checks
   `W <= m^2C` exactly with integers.
2. Checks the exact `L`-shape obstruction to the `Z` shortcut.
3. Checks the displayed formulas for `G_{a,b}` over a grid of parameters
   and checks that its ratio tends upward towards one for `a=1`.
4. Checks tensor multiplicativity:
   `m,C,W` multiply under Kronecker products, so any counterexample would
   automatically be scalable.
5. The separate Ky--Fan verifier checks the `7 x 7` double-star
   counterexample using integer and radical comparisons only.

Run

```
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_weighted_c4_audit.py
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_kyfan_counterexample.py
```

## 6. Exact ACP consequence if (1) is proved

In the ACP near-product regime, the two-Cauchy marginal argument gives

\[
 \frac{W}{m^4}\ge 2^{-4\varepsilon R}.
\]

Inequality (1) would immediately imply

\[
 C\ge m^2 2^{-4\varepsilon R}.                              \tag{3}
\]

For the counted repair graph, each ordered support rectangle gives the
two cross sources.  The existing fibre bound is

\[
 C\le n^2 2^{2r}V(P)^2.
\]

Combining with (3) yields directly

\[
m\le n\,2^r\,2^{2\varepsilon R}V(P).
\]

Thus (1) removes the degree/information bucketing theorem and its losses
from this branch.  The inequality is sharp in constant, so this is the
right quantitative target.  At present this consequence remains
conditional on proving (1).  The proposed Ky--Fan route (2) is false.
