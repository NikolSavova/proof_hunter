# Singleton-terminal cloud rectangles: two-cell localization and a universal cage

**Date:** 2026-08-15. All logarithms are base two. This continues
`../agent_outer_internal_product/DENSE_CLOUD_CROSS_CIRCUIT_DELETION_FOREST.md`.

## Verdict

The strong all-delete branch has a genuinely planar normal form. Fix an
opposite convex face `B`. If every singleton of a row face `A` can be
inserted into `B`, but no two labels of `A` survive together, then all
labels of `A` lie in at most two adjacent insertion cells of `B` (three
cells only when `B` is a triangle).

This has a quantitative consequence at the live density threshold. Let
`X` have `R` labels and let a rank-`q` terminal family have density

\[
              \delta={|\mathcal A|\over\binom Rq}.                 \tag{1}
\]

After fixing one adjacent-cell container, its two-shadow consists entirely
of actual bad pairs. If

\[
 q=(\theta+o(1))\log N,\qquad
 \delta\ge N^{-(2-\log_2 3)+\varepsilon},               \tag{2}
\]

then that container has macroscopic support and its bad-pair graph has
`N^{2-o(1)}` edges (and `Omega(N^2)` when `R=Omega(N)`). Hence a positive
mass of strong singleton-terminal
columns produces a literal dense same-edge/adjacent-edge circuit tensor,
not an arbitrary face-alphabet obstruction.

This still does not close the fixed gap. The common-edge part of the
normal form is projectively universal. Every finite planar order type can
be placed, by an orientation-preserving affine map, in one ear cell so
that its tangent coordinates form a strict dominance chain. Its intrinsic
ordinary faces are unchanged, yet adjoining any two of its labels to the
carrier is nonconvex and every deletion forest is forced down to a
singleton.

There is an exact dense face-alphabet amplification: a lower convex carrier
chain supplies `2^h` different carrier faces, all sharing the same closing
edge, and the universal child is singleton-terminal against every one of
them. This is a stretchable, metadata-free saturation of the two-cell
normal form. Its carrier chain has endpoint surplus `Theta(h^2)`, so at
macroscopic scale it is caught by alternative (a) in the proposed
trichotomy:

\[
                     h^2\gg h^{\log_2 3}.                         \tag{3}
\]

Thus the result is a sharp planar reduction, not a counterexample to the
whole endpoint-surplus/survival/mixed-bank trichotomy. It proves that
circuit elimination alone cannot force two-label survival or a mixed bank;
a successful proof must use the carrier endpoint profile or
minimizer-specific balance to exclude the universal cage. The dense
common-physical-edge case is now handled exactly in
`FIXED_EDGE_CARRIER_ENDPOINT_DILUTION_GATE.md`; the surviving issue is
edge dispersion or critical density.

This qualification is essential in view of
`../agent_shield_circuit_cover/ENDPOINT_SURPLUS_BALANCED_SHELL_BARRIER.md`:
endpoint surplus is not universally large. That construction escapes by a
detached Boolean shell, so the still-plausible input is specifically a
*live, rank-safe, low-surplus* exclusion, not an order-type inequality.

The scope is the **strong** terminal branch: every two-label subtrace of
the row remains bad with `B`. A deterministic deletion path which happens
to end at a singleton does not imply that hypothesis for unvisited pairs.

## 1. Insertion-cell localization

Let `B` be a strictly convex polygon. If `B union {x}` is convex, there is
a unique boundary edge `g_B(x)` which is replaced by the two new edges
through `x`; call it the insertion edge of `x`.

> **Lemma 1 (two-cell terminal localization).** Suppose `A` is an ordinary
> face disjoint from `B` and
> 
> \[
> B\cup\{x\}\in\mathcal F(P)\quad(x\in A),\qquad
> B\cup\{x,y\}\notin\mathcal F(P)\quad(x\ne y\in A).    \tag{4}
> \]
> 
> If `|B|>=4`, there are two equal or adjacent boundary edges `g,g'` of
> `B` such that every label of `A` lies in the union of their insertion
> cells. If `|B|=3`, the same holds with its three edges.

**Proof.** Singleton convexity gives the unique edge `g_B(x)`. Ears on
nonadjacent boundary edges commute, so (4) implies that every pair of
edges in `{g_B(x):x in A}` is equal or adjacent. A pairwise-adjacent set
of edges in a cycle of length at least four has size at most two, and the
two edges are adjacent. A triangle has three pairwise-adjacent edges. QED.

The conclusion is physical: `g,g'` are actual consecutive edges of the
actual opposite face `B`. No circuit-root pigeonhole has yet occurred.

## 2. Dense layers give a macroscopic bad-pair tensor

Let $\mathcal T_B\subseteq\binom Xq$ be a family satisfying (4) with one
fixed `B`, and put $M_B=|\mathcal T_B|$. Canonically assign every row to
the first edge-pair container supplied by Lemma 1. There are at most
`r=|B|` containers (`r=3` for a triangle), so one container `J` carries a
family $\mathcal G$ of size

\[
                          |\mathcal G|\ge {M_B\over r}.             \tag{5}
\]

Let $S_J\subseteq X$ be the union of the one or two insertion cells in
that container, and write `p=|S_J|`. Since
$\mathcal G\subseteq\binom{S_J}q$, if

\[
                     M_B\ge\eta\delta\binom Rq,                   \tag{6}
\]

then

\[
 \boxed{\quad
 p\ge (R-q+1)\left({\eta\delta\over r}\right)^{1/q}.
 \quad}                                                          \tag{7}
\]

Indeed,

\[
 {\binom pq\over\binom Rq}
   =\prod_{i=0}^{q-1}{p-i\over R-i}
   \le\left({p\over R-q+1}\right)^q,                             \tag{8}
\]

and (5)--(6) prove (7).

Every pair in the two-shadow $\partial_2\mathcal G$ is bad with `B`, by
(4). Write $|\mathcal G|=\binom xq$ for the unique real $x\ge q$. The
Lovasz form of Kruskal--Katona gives

\[
                 |\partial_2\mathcal G|\ge\binom x2.              \tag{9}
\]

At (2), with $R=N^{1-o(1)}$, $r=N^{o(1)}$, and
$\eta=N^{-o(1)}$, equations (5)--(9) give

\[
 x\ge N^{1-o(1)}
       2^{-(2-\log_2 3-\varepsilon)/\theta},\qquad
 |\partial_2\mathcal G|=N^{2-o(1)}.                            \tag{10}
\]

The two cells split these bad pairs into three types: both labels at `g`,
both at `g'`, or one at each. One type contains $N^{2-o(1)}$ pairs.

* In a same-edge type, every bad pair is exactly a fixed-edge strict
  containment circuit `y in int triangle(u,v,x)`. The orientation is the
  two-dimensional tangent dominance order.
* In an adjacent-edge type, planar four-locality gives a circuit containing
  the two row labels and two labels of `B`. Pigeonholing the latter pair
  costs at most `binom(r,2)=N^{o(1)}` on the rank-safe slice.

Thus a strong terminal column at live layer density yields a dense rooted
circuit tensor on a macroscopic physical support. This is stronger than
the abstract statement that its deletion forest happens to have a long
path.

If (6) holds for $H/N^{o(1)}$ different opposite faces, the total literal
pair--carrier incidence mass is $HN^{2-o(1)}$, comfortably above the
$HN^{\log_2 3+o(1)}$ fixed-gap demand. The remaining problem is its
shield/profile load, not the amount of planar circuit incidence.

## 3. Every order type fits in the common-edge cage

The concentrated alternative in Section 2 cannot be eliminated from
planarity alone.

> **Theorem 2 (affine universal dominance cage).** Let `Q` be any finite
> planar general-position set, with its labels partitioned into any number
> of named clouds. There are a triangle `B={u,v,w}` and an
> orientation-preserving affine image `Q'` such that:
> 
> 1. `Q'` has exactly the labelled order type of `Q`;
> 2. every `x in Q'` is a singleton ear of `B` at the same edge `uv`;
> 3. the labels of `Q'` are totally ordered by strict fixed-edge
>    containment; and consequently
> 4. for every `S subseteq Q'`,
>    
>    \[
>         B\cup S\text{ is convex}\quad\Longleftrightarrow\quad |S|\le1.
>                                                                    \tag{11}
>    \]

**Proof.** First apply an orientation-preserving affine change so the
first coordinates `a_i` of the points `(a_i,b_i)` are distinct. Put

\[
 u=(-1,0),\qquad v=(1,0),\qquad w=(0,-3),                       \tag{12}
\]

and, for sufficiently small positive `epsilon`, send

\[
 (a_i,b_i)\longmapsto
 p_i=(\varepsilon a_i,
             1+3\varepsilon a_i+\varepsilon^2b_i).                \tag{13}
\]

The linear part of (13) has determinant `epsilon^3>0`, so every orientation
sign is preserved. All `p_i` lie in the ear cell above `uv` for small
`epsilon`.

Use tangent coordinates

\[
               L(p)={p_y\over1+p_x},\qquad
               R(p)={p_y\over1-p_x}.                            \tag{14}
\]

If `a_i<a_j`, direct subtraction in (14) has leading terms
`2 epsilon(a_j-a_i)` and `4 epsilon(a_j-a_i)`, respectively. The finitely
many higher-order terms are dominated for small enough `epsilon`, so both
coordinates strictly increase with `a_i`. The fixed-edge containment
criterion therefore gives

\[
                        p_i\in\operatorname{int}\triangle uvp_j. \tag{15}
\]

For a nonempty `S`, its maximum label in this order hides every other
label inside its ear triangle. This proves (11). QED.

The theorem preserves arbitrary intrinsic child faces and arbitrary named
cloud partitions. Hence neither a child reflection, an intrinsic
order-type mutation, nor signed-circuit elimination can by itself release
two labels from the cage. The missing input must compare the child to its
actual directional profile in the completed carrier.

## 4. Dense face-alphabet amplification and endpoint calibration

The universal cage can be paired with exponentially many actual carrier
faces. Keep `u=(-1,0),v=(1,0)` and take `h` rational points on the lower
parabola

\[
                       c_t=(s_t,s_t^2-1),\qquad -1<s_t<1.          \tag{16}
\]

For every `J subseteq [h]`, put

\[
                       B_J=\{u,v\}\cup\{c_t:t\in J\}.             \tag{17}
\]

All `2^h` sets in (17) are convex and have `uv` as their closing edge.
Use (13) in the common ear cell above `uv`. For every intrinsic ordinary
face `A` of `Q'` with `|A|>=2` and every `J`,

\[
 B_J\cup\{x\}\text{ is convex for every }x\in A,
 \qquad B_J\cup A\text{ is nonconvex}.                            \tag{18}
\]

More strongly, every residual of `A` of rank at least two remains bad;
the deletion forest stops exactly at a singleton. The output carrier and
surviving singleton recover `(J,x)` with load one, but all other labels of
`A` have genuinely disappeared. There is no chronology artefact.

The parabola is only a transparent calibration, not a necessary part of
the interface. More generally, place any carrier set `R` below `uv` and
let $\mathcal B_{uv}$ be any family of its ordinary faces for which
$\{u,v\}\cup F$ is convex with exposed edge `uv`. The same cage above
`uv` is singleton-terminal against every $F\in\mathcal B_{uv}$. Thus the
construction can amplify an arbitrary fixed-edge directional face
alphabet. The opposite alphabet always contains all pairs. As proved in
`FIXED_EDGE_CARRIER_ENDPOINT_DILUTION_GATE.md`, this already forces the
required endpoint surplus when the common-edge alphabet has relative
density above $p^{-(2-\log_2 3)+o(1)}$. It does not handle a fibre at or
below that critical dilution.

Partitioning `Q'` into three named arbitrary children makes (18) hold
simultaneously for all three child face alphabets against the same carrier
alphabet. This is the exact common-root saturation relevant after the
two-cell localization. It does not assert pairwise anti-alignment among
the three child alphabets themselves, nor does it upper-bound all
unselected mixed faces of the combined configuration. Consequently it is
an exact interface regression, not yet a global low-face construction.

Finally, the carrier payment is explicit. The `p=h+2` parabola labels are
in convex position. In the horizontal chart every nonempty subset is a
cup, whereas only singletons and pairs are caps. Thus

\[
 H=2^p-1,\qquad U=H,\qquad C=p+\binom p2,qquad
 {CU\over H}=p+\binom p2=\Theta(p^2).                            \tag{19}
\]

Since `2>log_2 3`, (19) supplies alternative (a) at the macroscopic
fixed-power scale. The known planar saturation therefore explains, rather
than refutes, the proposed trichotomy: all-delete can be projectively
universal, but its presently known rich carrier has more than enough
endpoint surplus.

The exact next theorem is now narrower: either retain a common physical
edge above the critical density (the cited dilution gate then closes), or
turn face-dependent edge dispersion into a two-label/mixed bank. Neither
circuit elimination nor the least-counterexample mean-rank scalar alone
performs that localization.

## 5. Verification

Run

```text
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_planar_singleton_terminal_two_cell_universal_cage.py
```

The checker uses exact rational arithmetic. It starts from a nonconvex
ten-point child, verifies preservation of every orientation sign under
(13), partitions it into three named clouds, enumerates all intrinsic child
faces and all `2^6` carrier faces, and checks every singleton-compatible,
rank-at-least-two-bad incidence in (18). It also verifies common-edge
containment, general position, the exact endpoint counts in (19), and the
finite support/two-shadow inequalities behind (7)--(10).
