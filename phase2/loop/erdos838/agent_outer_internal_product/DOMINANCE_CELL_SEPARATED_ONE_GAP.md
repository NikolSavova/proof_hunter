# Dominance-separated cells: an exact two-face one-gap bank and the one-face circuit barrier

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The geometry half has an exact answer once the two output faces are kept
separate.  Suppose `k` disjoint ordered cells have nonempty local trace
alphabets, and arbitrary choices of one trace per cell cross-complete to an
ordinary face.  If `m_i` is the trace-alphabet size and `H_i` the full
ordinary-face reservoir of the support of cell `i`, then omitting cell `g`
from the cross-complete face and putting an arbitrary cell-`g` reservoir
face in the **second** output gives the injective bank

\[
                B_g=H_g\prod_{i\ne g}m_i.               \tag{1}
\]

No infinitesimal placement, small-cluster assumption, independence of the
selected word family, or additional convex mixing is used.  Cyclic
multiplication gives

\[
 \boxed{
  \max_g B_g\ge P_0
       \left(\prod_i{H_i\over m_i}\right)^{1/k},
       \qquad P_0=\prod_i m_i.}                          \tag{2}
\]

For a sparse selected family `mathcal E`, projection redundancy contributes
the additional exact factor `P_0/|mathcal E|`.  With arbitrary nonuniform
but uniformly bounded local occupancies `t_i<=t_*=O(1)` and the universal
planar face reservoir in each support, (2) has a quadratic-exponential
multiplier **as a pair bank** whenever `k=O(log D)` and
`log|mathcal E|=Omega((log D)^2)`.  This phrase must not be read as a
standalone coefficient gain: if `M=|mathcal E|`, the pair bank gives only
`V>=sqrt(B_g)`, and improves `V>=M` only when `B_g>M^2`.  A fixed-power
ratio `B_g/M` is insufficient.

The analogous **one-face** claim is false, even if the replacement is only
a two-point directional profile.  There are four strictly
reverse-dominance cells in the positive fixed-edge insertion wedge, all
selected traces have occupancy one, and both complete selected words are
ordinary.  After omitting the third cell, however, joining the singleton
profile in the second cell to the two-point profile in the fourth cell and
the singleton in the first cell creates a bad `1+3` circuit.  The failure
persists after deleting the root edge.  Thus neither an arbitrary universal
reservoir nor the formal directional bank
`R_(g-1) A_(g+1) product_(i notin {g-1,g,g+1})m_i` follows from broad
reverse dominance and cross-completion alone.  The radial theorem needs its
strong-separation/lexicographic boundary hypothesis; interval order alone
does not supply it.

Accordingly, the ordered-hypergraph route receives a complete geometry
module at the two-output scale, but not a new single-face radial bank.  As a
standalone ordinary-face count this is only a square bound and often does
not improve the already known source count.  It is directly useful only
when the surrounding argument already has a two-record/square demand, or
when its multiplier is larger than the source family itself.  Global use
also requires the ordered extraction to recover the common base and cell
list, or to bound their description load.

The exact verifier is

```text
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_dominance_cell_separated_one_gap.py
```

It checks a rational four-cell conic bank, the sparse-family and cyclic
identities, and the positive-coordinate rational circuit obstruction.

## 1. Cross-complete trace cells

Let `B` be a fixed ordinary base and let `X_1,...,X_k` be pairwise disjoint
supports, disjoint also from `B`.  In cell `i`, let

\[
             \mathcal A_i\subseteq\mathcal F(X_i)\setminus\{\varnothing\}
                                                                    \tag{3}
\]

be a nonempty family of local traces.  Assume the complete cross property

\[
 B\cup T_1\cup\cdots\cup T_k\in\mathcal F(P)
       \quad\hbox{for every }(T_1,\ldots,T_k)
       \in\prod_i\mathcal A_i.                           \tag{4}
\]

This abstracts the output of the twice-interval-partite/reverse-dominance
extraction.  The dominance geometry is used to establish (4); the theorem
below needs nothing further from the realization.

Put

\[
 m_i=|\mathcal A_i|,\qquad
 H_i=|\mathcal F(X_i)|,\qquad P_0=\prod_i m_i.           \tag{5}
\]

The empty local face is included in `H_i`.

## 2. Separated one-gap bank

For a gap `g`, define a family of ordered face pairs

\[
 \mathcal B_g=\left\{
  \left(B\cup\bigcup_{i\ne g}T_i,\ F\right):
  T_i\in\mathcal A_i\ (i\ne g),\quad
  F\in\mathcal F(X_g)
  \right\}.                                             \tag{6}
\]

> **Theorem 1 (exact separated one-gap bank).**  Every member of (6) is an
> ordered pair of ordinary faces, the representation in (6) is unique
> inside the fixed cell system, and (1)--(2) hold.

**Proof.**  Choose any trace in the nonempty alphabet `mathcal A_g` and
complete the first coordinate to a face using (4).  Deleting that trace
shows that the first coordinate in (6) is ordinary.  The second coordinate
is ordinary by definition.

Intersection of the first output with `X_i` recovers `T_i` for every
`i!=g`; intersection of the second with `X_g` recovers `F`.  Because every
trace is nonempty, the missing active cell recovers `g`.  Thus the map is
injective and

\[
                   |\mathcal B_g|=H_g{P_0\over m_g}.      \tag{7}
\]

Multiplying (7) over all gaps gives

\[
               \prod_g{|\mathcal B_g|\over P_0}
                    =\prod_i{H_i\over m_i}.              \tag{8}
\]

Taking a geometric mean proves (2).  QED.

There is also a single-face deletion bank of size `P_0/m_g`, namely the
first coordinates in (6).  What cannot be done unconditionally is multiply
that bank by `H_g` **inside the same ordinary face**.

The local decoder is exact.  Here is the precise global statement.  Let
`mathcal C` be any family of fixed cell contexts and choose one canonical
gap `g(c)` in every context.  Define the actual pair load

\[
 \Lambda=\max_{(F_1,F_2)\in\mathcal F(P)^2}
   \left|\{c\in\mathcal C:(F_1,F_2)\in
                    \mathcal B_{c,g(c)}\}\right|.        \tag{G1}
\]

Then simple incidence counting gives the exact global inequality

\[
       \boxed{\sum_{c\in\mathcal C}|\mathcal B_{c,g(c)}|
                    \le \Lambda V(P)^2.}                 \tag{G2}
\]

If the ordered pair recovers the canonical base, ordered support list, and
gap, then `Lambda=1`.  More generally any explicit list-decoder with at
most `Lambda` descriptions gives (G2).  If several formal contexts have the
same geometric data, their distinct trace words must first be merged;
counting the same geometric bank repeatedly is not allowed.  If the pair
does not recover the base or cell list, their actual description
multiplicity remains in `Lambda`.  In particular Theorem 1 does **not**
solve cross-base reuse or container promotion.

## 3. Sparse selected words only help

Let

\[
 \mathcal E\subseteq
   \prod_i\left(\mathcal F(X_i)\setminus\{\varnothing\}\right)     \tag{9}
\]

be an arbitrary selected word family for which the problem's hypothesis
says that arbitrary choices from its coordinate projections cross-complete.
Replace `mathcal A_i` in (3) by `proj_i mathcal E`, put `M=|mathcal E|`,
and retain the notation `m_i,P_0`.  Then `P_0>=M`, and Theorem 1 gives

\[
 \boxed{
 \log{\max_gB_g\over M}\ge
   \log{P_0\over M}+{1\over k}\sum_i\log{H_i\over m_i}.} \tag{10}
\]

The first term is the exact projection redundancy.  Thus an MDS code,
diagonal family, or arbitrary correlation cannot obstruct this bank; its
missing rectangles are already present in the ambient cross-completion
alphabet.

## 4. Nonuniform fixed occupancies plus universal reservoirs

Suppose every local trace in cell `i` has rank at most `t_i`, where
`1<=t_i<=t_*` and `t_*` is fixed independently of all asymptotic
parameters.  Write

\[
                  n_i=|X_i|,\qquad h_i=\log m_i.          \tag{11}
\]

Then

\[
 m_i\le\sum_{r=1}^{t_i}\binom{n_i}{r}
                  \le(t_i+1)n_i^{t_i}.                   \tag{12}
\]

Use the established universal planar reservoir in the harmless uniform
form

\[
                 \log H_i\ge c_0(\log n_i)^2-C_0,        \tag{13}
\]

for absolute `c_0>0,C_0`.  Equations (12)--(13) imply, after weakening the
constant and absorbing the finitely many small values, that

\[
        \log{H_i\over m_i}\ge c_* h_i^2-h_i-C_*,
        \qquad c_*>0.                                    \tag{14}
\]

For example one may take any `c_*<c_0/(2t_*^2)` after increasing `C_*`.
Put `x=log P_0=sum_i h_i`.  Substituting (14) in (10) and applying Cauchy
gives

\[
 \log{\max_gB_g\over M}
 \ge x-\log M+c_*{x^2\over k^2}-{x\over k}-C_*.          \tag{15}
\]

For `k>=2` the right side is increasing in `x>=log M`; hence

\[
 \boxed{
 \log{\max_gB_g\over M}
 \ge c_*{(\log M)^2\over k^2}-{\log M\over k}-C_*.}      \tag{16}
\]

Thus `k<=kappa log D` and `log M>=a(log D)^2` give

\[
          \log{\max_gB_g\over M}
             \ge {c_*a^2\over\kappa^2}(\log D)^2-O(\log D).
                                                                    \tag{17}
\]

This multiplier over `M` is far larger than a fixed power.  But the
conclusion is a bank in `mathcal F(P)^2`, so it certifies only

\[
 \log V(P)\ge {1\over2}\left(\log M+
                      \log{\max_gB_g\over M}\right).     \tag{C1}
\]

It must not be quoted as `V(P)>=max_gB_g`.  Equivalently the improvement
over the already known `V(P)>=M` is controlled by

\[
 \log{V(P)\over M}\ge {1\over2}\left[
       \log{P_0\over M}+{1\over k}\sum_i\log{H_i\over m_i}
       -\log M\right].                                   \tag{C2}
\]

In particular, if

\[
 \log M=(a+o(1))(\log D)^2,\qquad
 \log(\max_gB_g/M)=(\delta+o(1))(\log D)^2,              \tag{C3}
\]

then this standalone bank gives coefficient `(a+delta)/2`, while the
source faces already give coefficient `a`.  It is a strict standalone
improvement exactly when `delta>a`.  At leading order
`delta approximately c_0a^2/(t_*^2 kappa^2)` in the balanced extremal
regime.  Thus the illustrative values `c_0=a=1/4`, `t_*=1` are neutral only
at `kappa=1/4` and are worse for larger `kappa`; no unconditional
coefficient gain follows.  The exact theorem is instead a valid substitute
inside a pre-existing two-record square demand, subject to the global load
(G1), or in the exceptional regime `delta>a`.

The verifier makes the loss visible rather than merely symbolic.  Its
nonuniform-rank sparse family has `M=126`, `P_0=252`, and
`max_g B_g=504`; hence `sqrt(max_g B_g)<M` despite
`max_g B_g/M=4`.  The pair bank is exact but its standalone use is strictly
worse than the original source bank in that instance.

## 5. Exact directional-profile circuit obstruction

Normalize the common root edge to

\[
                         u=(-1,0),\qquad v=(1,0),         \tag{18}
\]

and for a point `(s,y)` above it use tangent coordinates

\[
                         L={s+1\over y},\qquad R={1-s\over y}.       \tag{19}
\]

Take, in addition,

\[
 q=\left(-{19\over20},{1\over20}\right),\qquad
 w=\left(0,{10\over11}\right),                            \tag{20a}
\]

and

\[
 x=\left(-{3\over40},{7\over8}\right),\quad
 z=\left({3\over40},{7\over8}\right),\quad
 y=\left({2\over15},{8\over9}\right).                  \tag{20}
\]

Their tangent coordinates are

\[
 (L_q,R_q)=(1,39),\qquad
 (L_x,R_x)=\left({37\over35},{43\over35}\right),\quad
 (L_w,R_w)=\left({11\over10},{11\over10}\right),\quad
 (L_z,R_z)=\left({43\over35},{37\over35}\right),\quad
 (L_y,R_y)=\left({51\over40},{39\over40}\right).       \tag{21}
\]

Hence all coordinates are positive and

\[
 L_q<L_x<L_w<L_z<L_y,\qquad
 R_q>R_x>R_w>R_z>R_y.                                   \tag{22}
\]

Partition the points into four strictly reverse-dominance interval cells

\[
             X_1=\{q\},\quad X_2=\{x\},\quad
             X_3=\{w\},\quad X_4=\{z,y\}.                \tag{23}
\]

Every selected trace has occupancy one; the only choice is `{z}` or `{y}`
in the fourth cell.  Direct rational hull computation gives that both

\[
 \{u,v,q,x,w,z\},\qquad \{u,v,q,x,w,y\}                 \tag{24}
\]

are convex hexagons.  Thus arbitrary selected trace choices cross-complete.
Now omit the third cell.  The singleton `{x}` is a directional profile of
`X_2`, while the two-point set `{z,y}` is both a left and a right boundary
profile of `X_4`.  The formal one-gap output is

\[
                         \{q,x,z,y\}.                     \tag{25}
\]

But

\[
 z={3\over230}q+{122\over575}x+{891\over1150}y,          \tag{26}
\]

with positive coefficients summing to one.  Hence (25) is nonconvex.  The
failure remains after adjoining the root, and all seven displayed points
are in general position.

This is exactly the failed directional one-gap multiplication

\[
 \underbrace{\{q\}}_{\text{other-cell trace}}
  \quad+\quad
 \underbrace{\{x\}}_{\text{left adjacent profile}}
  \quad+\quad
 \underbrace{\{z,y\}}_{\text{right adjacent profile}}.            \tag{27}
\]

It uses occupancy one, strict interval separation in both dominance
coordinates, and no limiting geometry.  The obstruction is a genuine
three-variable circuit invisible to all pairwise dominance comparisons.
The separated pair `(\{u,v,q,x,w\},\{z,y\})` with gap `X_4`, or the
corresponding pair for any other gap, remains valid exactly as Theorem 1
requires.  What fails is re-mixing a changed local profile into a one-face
output.  Strong radial separation would control the seam turns and forbids
this example; broad dominance order does not.

## 6. Remaining interface

For the ordered-hypergraph route, the exact alternatives are now:

1. if the two output faces remain available, use (6)--(17) directly;
2. if a single ordinary mixed face is required, extract seam-compatible
   directional profiles with their own reservoir lower bound; neither the
   full local `H_i` nor formal left/right profiles can be substituted by
   (27) without this extra compatibility;
3. retain the actual common-base/cell-list overlap in the global telescope.

No infinitesimal cluster assumption is needed in the first alternative.
The rational obstruction shows why removing the second output would require
new geometry rather than a refinement of the dominance ordering.
