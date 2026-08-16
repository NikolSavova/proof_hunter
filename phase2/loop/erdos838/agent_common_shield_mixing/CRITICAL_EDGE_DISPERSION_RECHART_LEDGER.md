# Critical cage-edge dispersion: a common-root rechart and frozen-chart barrier

**Date:** 2026-08-15. All logarithms are base two. Put

\[
 a=\log_2 3,
 \qquad \vartheta=2-a.                                         \tag{1}
\]

This continues `FIXED_EDGE_CARRIER_ENDPOINT_DILUTION_GATE.md`.

## Verdict

Face-dependent insertion edges are not by themselves an escape. If the
cages share one physical root `z` and one tangent chamber, a single
projective map sends `z` to infinity. In that chart every carrier face is
a directional chain whose extreme pair is its *own* insertion edge. Thus
the fixed-edge density theorem extends verbatim to a varying-edge family:

\[
 \boxed{\qquad
       \sigma_z={C_zU_z\over V_z}
          \ge {H_z\over V_z}\binom{p_z}{2}.
 \qquad}                                                       \tag{2}
\]

In particular, $H_z/V_z\ge p_z^{-\vartheta+\varepsilon}$ forces the
required $p_z^{a+\varepsilon}/3$ endpoint surplus. The edge fibres `H_g`
may all be as
small as `H_z/p_z^2`; their dispersion does not affect (2).

Across varying roots, the literal faces `B union {z}` form a load-one
mixed bank after physical colouring. For a weighted record ledger its
only loss is the genuine history multiplicity over the same physical pair
`(B,z)`. This gives an exact two-stage ledger: common-root density pays by
(2); root dispersion pays by singleton mixed faces; only duplicate
histories and simultaneous-chart compatibility remain.

The simultaneous-chart qualification is real. There is a scalable
stretchable rank-`O(log n)` configuration with a quadratic-entropy
selected carrier alphabet having:

* a complete cap-by-cup rectangle of carriers in one frozen chart;
* a `D`-label nested root cloud at one omitted upper role;
* every singleton root compatible and every root pair terminal-bad;
* `D^2` face-dependent cage edges, each with relative fibre `D^{-2}`;
* only a factor `D=n^{1-o(1)}` from the literal singleton mixed bank; and
* selected frozen-chart endpoint ratio exactly one.

For each fixed root, recharting does expose all carriers as caps, exactly
as the theorem predicts. But the chart depends on the root/tangent query
and need not be the common chart needed to multiply three exterior cloud
profiles. The regression therefore kills a ledger proof which simply
adds edge fibres or silently rotates each incidence independently.

This is not a global sub-half construction. The induced clouds have
additional ordinary faces, and the recharted endpoint profiles may already
pay unless a genuine outside chronology freezes incompatible directions.
What is proved is the exact geometric ledger and a stretchable critical
interface showing its sharp remaining coordinate.

## 1. A common root simultaneously normalizes varying edges

> **Lemma 1 (root-to-infinity normalization).** Let `z` be a point and
> let `R` be a finite set strictly on one side of a line $\ell$ through
> `z`. Let $\mathcal H_z$ be a family of ordinary subsets `B` of `R` such
> that `B union {z}` is ordinary. Then one projective chart, depending
> only on $(z,\ell)$, makes every $B\in\mathcal H_z$ a cap or makes every
> one a cup. Its extreme pair is precisely the insertion edge of `z` in
> `B`.

**Proof.** Send $\ell$ to the line at infinity, choosing the affine side
which contains `R`. The point `z` becomes one fixed point at infinity, so
the lines through `z` become a parallel family. For every ordinary
`B union {z}`, the two neighbours of `z` on its boundary are the two
supporting parallel lines of `B`; these neighbours are exactly the
endpoints of the edge of `B` replaced by `z`. Hence they are the projection
extrema of `B`. The opposite boundary arc of the polygon is monotone in
that projection and has one constant triple sign. The side of $\ell$ fixes
the sign for the whole family. QED.

An explicit affine formula is useful. Put `z=(z_0,h)` and take
$\ell=\{y=h\}$, with $R\subset\{y<h\}$. Then

\[
 \Psi_z(x,y)
   =\left({x-z_0\over h-y},{1\over h-y}\right).                  \tag{3}
\]

The denominators are positive. The corresponding homogeneous projective
matrix is nonsingular, and the omitted point `z` maps to the common point
at infinity.

## 2. Weighted boundary-edge/root ledger

Let $\Omega$ be a finite set of selected records. A record $\omega$ carries

\[
        (B_\omega,z_\omega,g_\omega,\tau_\omega,w_\omega),       \tag{4}
\]

where `B_omega` is a physical carrier face, `z_omega` is an individually
compatible physical root, `g_omega` is its actual insertion edge,
`tau_omega` is the tangent-side chamber, and `w_omega>=0`. Put

\[
 m(B,z)=\sum_{\omega:(B_\omega,z_\omega)=(B,z)}w_\omega,
 \qquad
 W=\sum_\omega w_\omega,
 \qquad
 \Lambda=\max_{B,z}m(B,z).                                    \tag{5}
\]

Let `I` be the number of distinct physical incidences `(B,z)` occurring.

> **Theorem 2 (root--edge ledger).** After carrier/root role colouring:
>
> 1. the faces `B union {z}` are distinct, so
>    \[
>                         V(P)\ge I\ge W/\Lambda;                \tag{6}
>    \]
> 2. for a fixed root/chamber fibre `tau=(z,side)`, if `H_tau` distinct
>    carriers occur on a union support of size `p_tau`, then in the chart
>    of Lemma 1
>    \[
>       {C_\tau U_\tau\over V_\tau}
>           \ge {H_\tau\over V_\tau}\binom{p_\tau}{2};          \tag{7}
>    \]
> 3. consequently, if all chart-compatible fibres have endpoint surplus
>    below `p_tau^{a-o(1)}`, then
>    \[
>              H_\tau/V_\tau\le p_\tau^{-\vartheta+o(1)}.       \tag{8}
>    \]

**Proof.** The physical colours recover `B` and `z` from `B union {z}`,
which proves the first inequality in (6). Since every atom in (5) is at
most `Lambda`, `W<=Lambda I` proves the second. Lemma 1 puts all `H_tau`
carriers in one directional profile. The opposite profile contains every
pair, proving (7) exactly as in the fixed-edge dilution theorem. Equation
(8) is the exponent-scale contrapositive. QED.

This is a genuine edge ledger: `g_omega` is recoverable in each output as
the edge deleted when `z` is removed. No pigeonhole over the `O(p^2)`
possible edges is used. It also states exactly what the ledger cannot see:
if many weighted histories have the same physical `(B,z)`, their excess
mass is `Lambda`, not edge diversity.

For three exterior clouds, (7) is usable in a cyclic profile product only
when their recharted cap/cup directions are simultaneously compatible.
Applying a different projective map to each factor is invalid: each map
preserves ordinary faces within that cloud, but it does not preserve the
common exterior seam direction needed by the cross-cloud product.

## 3. Stretchable cap-by-cup critical-dispersion regression

Fix left and right endpoint labels `l,r`. Along the upper arc from `l` to
`r`, take `s` tiny strongly separated macro clouds of size `D`, omit one
additional root role `X`, and require that the two roles immediately
adjacent to `X` are `Y,W`. Along the lower arc take `t` further size-`D`
clouds. All macro roles are in the cyclic order

\[
                 l,\quad\hbox{upper roles},\quad r,
                    \quad\hbox{lower roles}.                     \tag{9}
\]

Infinitesimal lexicographic substitution gives the following strict
properties for every choice of one label per nonroot role:

1. the selected upper trace is a cap with endpoints `l,r`;
2. the selected lower trace is a cup with the same endpoints;
3. their union `B` is ordinary; and
4. after inserting any singleton `x in X`, the only replaced carrier edge
   is the pair `g={y,w}` selected from the neighbouring roles `Y,W`.

Inside the omitted macro cell, use the affine universal dominance cage
from `PLANAR_SINGLETON_TERMINAL_TWO_CELL_UNIVERSAL_CAGE.md`. The strict
containment inequalities persist uniformly under sufficiently small
perturbations of `Y,W`. Thus, for every carrier `B`,

\[
 B\cup\{x\}\text{ is ordinary for every }x\in X,
 \qquad
 B\cup\{x,x'\}\text{ is nonordinary for }x\ne x'.              \tag{10}
\]

All conditions are open strict determinant inequalities, so rational
general-position realizations exist for every finite `(D,s,t)`. Choose the
order type substituted into each size-`D` cloud from a standard rational
Erdos--Szekeres/Pascal cell whose maximum ordinary-face rank is
`r_0=O(log D)`. The universal affine squeeze used in the root role
preserves that intrinsic rank.

The exact selected counts are

\[
 \begin{aligned}
 C_0&=D^s, &U_0&=D^t, &H&=C_0U_0=D^{s+t},\\
 H_g&=D^{s+t-2}=H/D^2,&&
 M_1&=D H .                                                     \tag{11}
 \end{aligned}
\]

Here `H_g` is the number of carriers with a prescribed physical neighbour
edge `g={y,w}`, and `M_1` is the number of distinct singleton mixed faces
`B union {x}`. Thus

\[
       {H_g\over H}=D^{-2}=n^{-2+o(1)},
       \qquad {C_0U_0\over H}=1,\qquad {M_1\over H}=D=n^{1-o(1)}. \tag{12}
\]

Choose $s+t=\kappa\log D$. The carrier rank is
`s+t+2=O(log n)`, while

\[
                  \log H=(\kappa+o(1))(\log n)^2.               \tag{13}
\]

The whole substituted configuration, not only the displayed carriers,
has maximum ordinary-face rank `O(log n)`. Indeed, split any ordinary face
into its two directional boundary chains. On either chain the sequential
strong-block rule permits more than one label in at most one macro cloud;
all intervening clouds contribute at most a singleton. Hence each boundary
chain has rank at most

\[
                         (s+t+1)+r_0+O(1),                       \tag{14}
\]

and the union of the two chains has rank `O(s+t+r_0)=O(log n)`. The same
argument covers a face concentrated in the root cloud, whose intrinsic
rank is at most `r_0`.

The edge fibres lie far below the critical $n^{-\vartheta}$ density, and
the literal singleton bank is short of the `n^a` profile multiplier by
`n^{a-1-o(1)}`. Nevertheless each fixed `x` is a common root. Applying
Lemma 1 to that root makes all `H` carriers caps in a different projective
chart. This is not a contradiction to the frozen ratio in (12): `C_0,U_0`
are the on-word profiles in the original exterior chart, whereas the
rechart exposes additional directional faces.

The construction is therefore an exact test for any proposed proof:

* an order-type-only proof may use the root-to-infinity chart and (7);
* a cyclic exterior composition must prove that this chart is compatible
  with the other two clouds, or pay a chronology/profile-change bank;
* summing `H_g` or the literal faces `B union {x}` alone is insufficient.

The rank statement uses the indicated low-rank child order types. For
arbitrary substituted children the selected carrier alphabet still has
rank `O(log n)`, but the maximum ambient rank need not.

## 4. Verification

Run

```text
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_critical_edge_dispersion_rechart_ledger.py
```

The exact rational checker uses `D=3`, two upper neighbour roles and one
lower role. It enumerates all 27 carriers and all 81 root incidences,
checks the complete cap-by-cup rectangle, all 81 root-pair failures, the
nine varying insertion edges with fibre three, and the projective
root-to-infinity normalization for every root. It also verifies the
weighted ledger inequalities on exhaustive small integer tables and the
asymptotic identities in (11)--(13).
