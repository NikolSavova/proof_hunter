# Dense source--release rectangles and the actual-gap fan gate

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

The actual-gap theorem in
`MULTIROLE_ENDPOINT_POCKET_TRANSFER.md` gives an exact positive splice for
a dense `A by C` source--release rectangle, but only after a genuine extra
compatibility is supplied.  A rectangle record

\[
 A_i=B\cup G_i,\qquad C_j=B\cup F_j                    \tag{1}
\]

does **not** by itself say that a guard label is an ear of `C_j`, or that a
pocket label is an ear of `A_i`.  On a cross-compatible subrectangle where
those unions are convex, the actual-gap rooted complexes give ordinary
column and row banks with exact global decoder load.  A role-free common-
base version gives the mixed entropy bound

\[
 \boxed{\displaystyle
 R(B;X,Y)\ge
    \left(\prod_{g\in E(B)}H_g^XH_g^Y\right)^{1/6}.}    \tag{2}
\]

Thus rooted entropy at least
`6 log M + 6 sigma (log n)loglog n` over a fibre of marked mass `M`
supplies the missing `n^(sigma loglog n)` multiplier, subject only to the
actual global output load.

The dense rectangle does not force that entropy.  There is a scalable
rational rectangle with two `m`-point clouds on **adjacent actual gaps**
of one triangular base such that

* every source `A_i`, release `C_j`, detached targets `W_j,Q`, and old
  pair ear `E_i` are ordinary;
* every cross union `B union {g_i,x_j}` is convex, so both row and column
  actual-gap fan theorems really apply;
* every two guards are root-incompatible and every two pocket labels are
  root-incompatible; hence both rooted complexes contain only the empty
  set and singletons; and
* a base-retaining subset of the two clouds is convex exactly when it uses
  at most one label from each cloud.  The full mixed bank therefore has
  exactly `(m+1)^2` faces, only the scale of the `m^2` records.

This is stronger than a failure of a proof technique: it rules out any
unconditional base-retaining fan multiplier from dense rectangular
incidence, even with all real marks and all singleton cross compatibilities
preserved.  The two detached clouds happen to be convex chains and expose
`2^m` faces, so the construction is not a global low-face counterexample.
Charging that detached bank across many source histories requires exactly
the additional global history/container information absent from the local
rectangle.

## 1. Common-base two-cloud rooted composition

Let `B` be a strictly convex polygon.  Let `X,Y` be disjoint role-colored
alphabets such that `B union {z}` is convex for every `z in X union Y`.
Every label is therefore a singleton ear at a unique boundary edge of
`B`.  Write `X_g,Y_g` for the labels at edge `g`, and define

\[
\begin{aligned}
 \mathcal K_g^X(B)&=\{S\subseteq X_g:
     B\cup S\text{ is convex and expands }g\},\\
 \mathcal K_g^Y(B)&=\{T\subseteq Y_g:
     B\cup T\text{ is convex and expands }g\},\\
 H_g^X&=|\mathcal K_g^X(B)|,\qquad
 H_g^Y=|\mathcal K_g^Y(B)|.                            \tag{3}
\end{aligned}
\]

Empty sets are included.  Choose canonically at each edge the richer of
the two complexes, with deterministic tie breaking, and call it
`mathcal L_g`; put `L_g=max(H_g^X,H_g^Y)`.  Properly 3-color the boundary
edge cycle of `B` and choose the color `a` maximizing

\[
                              R_a=\prod_{g:\gamma(g)=a}L_g.        \tag{4}
\]

> **Theorem 1 (two-cloud actual-gap bank).**  Every independent selection
> `S_g in mathcal L_g` over the chosen color class gives a distinct
> ordinary face
>
> \[
>                            B\cup\bigcup_gS_g.           \tag{5}
> \]
>
> Consequently
>
> \[
> R:=\max_aR_a\ge
>     \left(\prod_gL_g\right)^{1/3}
>     \ge\left(\prod_gH_g^XH_g^Y\right)^{1/6}.           \tag{6}
> \]

**Proof.**  Edges in one color class are pairwise nonadjacent.  Lemma 1a
of `MULTIROLE_ENDPOINT_POCKET_TRANSFER.md` says their rooted expansions
commute, proving convexity in (5).  Disjoint role supports recover every
chosen subset, so the outputs are distinct.  The richest of three color
products is at least the geometric mean.  Finally
`max(H_g^X,H_g^Y)>=sqrt(H_g^XH_g^Y)` edge by edge.  QED.

For a weighted global family of base/profile fibres `f`, choose the bank
canonically and define its actual output load

\[
 \Lambda_{\rm gap}=\max_W
  \sum_{f,\mathbf S:\,B_f\cup\bigcup_gS_g=W}w_f.         \tag{7}
\]

Grouping the generated ordinary faces by output gives the exact global
form

\[
                       \sum_fw_fR_f\le\Lambda_{\rm gap}V(P).       \tag{8}
\]

The base role is retained in (5), so the output recovers `B_f`; guard and
pocket role colors recover the selected labels.  What it may erase is the
unused alphabet, root, or chronology, and that is precisely the actual
load (7).  No per-base copy of `V(P)` is used.

Put

\[
       E_f=\sum_g(\log H_{f,g}^X+\log H_{f,g}^Y).         \tag{9}
\]

Then `R_f>=2^(E_f/6)`.  If a fibre has marked demand `M_f` and

\[
             E_f\ge6\log M_f+6\sigma(\log n)\log\log n, \tag{10}
\]

its one-face bank has size at least
`M_f n^(sigma loglog n)`.  Equations (8)--(10) are the exact conditional
closure at the requested scale.

## 2. What the row/column rectangle actually supplies

Suppose first that every guard singleton `g_i` is compatible with a fixed
released column `C_j`.  Partition the guard alphabet by its unique actual
insertion edge of `C_j`, form its full rooted complexes, and let `R_G(j)`
be the canonical three-color bank from (3d) of the multirole report.  Then

\[
                  \{C_j\cup S:S\text{ is a selected guard fan face}\}
                                                                    \tag{11}
\]

has exactly `R_G(j)` ordinary faces.  Across different `j`, the pocket
role in `C_j` makes the outputs disjoint.  Hence one fixed rectangular
fibre has the exact column bank

\[
                               \sum_jR_G(j).             \tag{12}
\]

There is a symmetric row bank `sum_i R_X(i)` when every pocket singleton
is compatible with `A_i`.  Globally, (12) again uses the actual output load
rather than multiplying `V(P)` once per row or column.

For `m_Gm_X` rectangular records, (12) gives the desired multiplier only
if the average rooted guard bank is larger than `m_G` by that multiplier
(or symmetrically on the pocket side).  Merely having all singleton cross
unions gives `R_G(j)>=m_G+1`, which only recovers the original rectangular
scale.

Most importantly, convexity of the four targets `A_i,C_j,W_j,Q` and even
of the pair ear `E_i` does not imply the singleton cross compatibility
needed for (11).  Thus the dense Hall rectangle reaches the multirole
theorem only after this additional cell condition or a further thinning.

## 3. Adjacent double-dominance regression

Let

\[
 B=\{l=(-3,0),r=(3,0),t=(0,5)\},\qquad
 v=(-2,-1),\quad u=(2,-1).                              \tag{13}
\]

For a positive integer `m`, put `delta=1/(10000m^2)` and define the pocket
chain

\[
                    x_j=(\delta j,-4-\delta j^2),\qquad1\le j\le m. \tag{14}
\]

For the guard chain write `d=t-r=(-3,5)`, `n=(5,3)` (the exterior normal
to the oriented edge `rt`), and set

\[
 g_i=r+(1/2+\delta i)d+(1/10+\delta i^2)n,\qquad1\le i\le m.       \tag{15}
\]

All coordinates are rational.  The displayed configuration is in general
position for the audited range; at arbitrary scale, if a cross-cloud
collinearity occurs, make an arbitrarily small generic rational
perturbation.  Every property below is a strict orientation condition and
therefore persists.  The pocket points are singleton ears at the base edge `lr`;
the guard points are singleton ears at `rt`.  These two edges are adjacent
at `r`.

Affine normalization of either root edge sends its chain to points
`(delta i,-4-delta i^2)` up to positive rescaling and translation.  The
two tangent coordinates are strictly dominance ordered.  Equivalently,
direct orientation calculation gives

\[
\begin{aligned}
 B\cup\{x_j\},\ B\cup\{g_i\},\ B\cup\{g_i,x_j\}
     &\text{ convex for every }i,j,\\
 B\cup\{x_j,x_k\},\ B\cup\{g_i,g_h\}
     &\text{ nonconvex whenever }j\ne k,\ i\ne h.       \tag{16}
\end{aligned}
\]

Since a hidden vertex stays hidden after more points are added, (16)
implies the exact classification

\[
 B\cup S_G\cup S_X\text{ is convex}
       \quad\Longleftrightarrow\quad |S_G|\le1, |S_X|\le1.       \tag{17}
\]

Therefore both single-gap rooted reservoirs have size exactly `m+1`, and
the **entire** base-retaining two-cloud bank has size

\[
                              (m+1)^2.                  \tag{18}
\]

Now take `A_i=B\cup\{g_i\}`, `G_i=\{g_i\}`, and
`F_j=\{x_j\}`.  In addition to (16), the construction satisfies

\[
\begin{aligned}
 Q&=B\cup\{v\}\text{ convex},&W_j&=\{x_j,v\}\text{ convex},\\
 E_i&=B\cup\{g_i,v,u\}\text{ convex},&
 B\cup\{g_i,x_j,v\}&\text{ nonconvex}.                 \tag{19}
\end{aligned}
\]

The last failure holds because `v` lies in the interior of
`triangle(l,x_j,r)`.  Thus all actual targets and decoders of the dense
detached rectangle survive.  Moreover, every guard is an actual ear of
every `C_j` at `rt`, and every pocket point is an actual ear of every
`A_i` at `lr`.  The multirole row and column banks each have exactly
`m(m+1)` outputs, and their union cannot exceed the exact mixed
classification (18) by a superconstant factor.

The detached sets `\{g_i\}` and `\{x_j\}` are themselves convex chains,
so each has a Boolean face bank.  Removing the retained base therefore
escapes (17).  But that output erases the source base and can be reused by
arbitrarily many histories.  A theorem using the detached escape must
carry an external base/root decoder or prove a global container bound;
the dense rectangle and actual-gap fans contain neither.

## 4. Consequence for the multirole fan branch

The regression lands exactly in the dominance-chain alternative of
Lemma 1b, simultaneously on both adjacent gaps.  Hence the cup--cap fan
result is correct but does not create compatible fan *products* here:
there is no large antichain to trigger the good-cap/bad-cup split, and the
two dominance cages meet at a common base vertex.  Independent-ear
commutation deliberately excludes adjacent edges.

The strongest rigorous dichotomy currently available is therefore:

1. cross compatibility plus rooted entropy satisfying (10) closes by the
   bounded-load bank (8), or a large average row/column reservoir closes
   through (12);
2. low rooted entropy localizes, by the multirole cup--cap theorem, to
   dominance chains or homogeneous fixed-edge bad cups; and
3. adjacent double dominance is a realizable residual with only the
   baseline `(m+1)^2` base-retaining faces.

Closing case 3 requires information external to the rectangle: a
recoverable detached-cloud container, a nonadjacent third actual gap, or
chronology which prevents the same detached bank from being reused.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_dense_rectangle_actual_gap_fan.py
```

Expected output:

```text
PASS: two-cloud entropy bank and scalable adjacent double-dominance rectangle
```
