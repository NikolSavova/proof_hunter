# Same-parent projection product gate: MDS anti-modules and the ambient cross bank

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

Endpoint-baseline scarcity is not the remaining obstruction.  If a
rank-`r` parent `T` supports `N/C` canonical histories, its Boolean downset
gives `2^rN/C` ordinary faces.  This is exact, but `r=O(log n)` contributes
only `O(log n)` bits and therefore cannot improve a quadratic coefficient.

The hoped-for next statement, “quadratically many histories over one parent
contain a positive-log-scale Cartesian module product”, is **false even in
an exact planar radial cell**.  A length-`2j`, dimension-`j` Reed--Solomon
code selects

\[
                         N=q^j                                      \tag{1}
\]

convex sources over one five-point parent, but its distance `j+1` permits
at most one disjoint nontrivial varying module.  The parent already fixes
the genuine repair cell `(a,u,p,v,b)`, the insertion mark `p`, and the
blocked marked shield.  Thus source-internal product extraction is not a
valid unconditional gate even after the live role data are retained.

The same example exhibits the correct alternative.  The left and right
projection alphabets have size `q^j` each, and **every** cross-combination
is an ordinary planar face.  Hence the ambient bank has `q^(2j)=N^2`
faces.  Sparse anti-alignment is therefore favorable once ambient
cross-completion is proved.

There is an exact restricted extraction theorem.  For any fixed compatible
two-tangent profile in `ROOTED_DIAGONAL_AMALGAMATION.md`, all left--right
cross-combinations are ordinary, and their outputs have aggregate rank-`k`
load at most `k-1`.  More generally, any fixed-core cell with a complete
cross-completion relation has a projection-times-Boolean bank.  The gap is
proving that an arbitrary same-parent radial cell admits such a complete
profile after only coefficient-free localization.  The rooted theorem
does this when the common core is the two-point trace and the sides lie in
the required opposite halfplanes; it does **not** justify adding an
arbitrary larger parent.

Consequently this pass proves no unconditional coefficient above `1/4`.
It does validate the conditional coefficient jump: if a full radial
product/cross-completion profile of entropy coefficient `a` is extracted,
the existing one-gap theorem gives

\[
                    a+c_0(a/\kappa)^2,                            \tag{2}
\]

and the conservative values `a=kappa=1/4`, `c_0=1/8` give `3/8`.
In the MDS regression itself the ambient cross bank is stronger, raising
selected coefficient `1/4` directly to `1/2-o(1)`.

The exact verifier is

```text
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_same_parent_projection_product_gate.py
```

It checks a 48-point rational general-position instance, all `7^3`
selected sources, all `7^6` ambient cross-completions, the MDS distance,
canonical peeling, the blocked common interval tag, the exact endpoint
baseline, and the fixed marked tangent cell.

## 1. The projection-times-Boolean bank

Let `X_L`, `T`, and `X_R` be fixed disjoint label regions, with `T` one
fixed ordinary parent.  Let `mathcal L subseteq 2^(X_L)` and
`mathcal R subseteq 2^(X_R)`.  Suppose

\[
       L\mathbin{\dot\cup}T\mathbin{\dot\cup}R
       \quad\hbox{is in convex position for every }(L,R)
       \in\mathcal L\times\mathcal R.                  \tag{3}
\]

Let `E subset mathcal L times mathcal R` be any selected source family and
write

\[
 A=|\operatorname{proj}_{\mathcal L}E|,\qquad
 B=|\operatorname{proj}_{\mathcal R}E|,\qquad N=|E|.   \tag{4}
\]

> **Theorem 1 (complete-profile bank).**  Under (3), the ordinary faces
> 
> \[
>                   L\cup S\cup R,qquad
> L\in\operatorname{proj}_{\mathcal L}E,\quad
> R\in\operatorname{proj}_{\mathcal R}E,\quad S\subseteq T       \tag{5}
> \]
> 
> are all distinct.  Thus
> 
> \[
>                         V(P)\ge AB\,2^{|T|}.           \tag{6}
> \]

**Proof.**  Each set in (5) is a subset of the convex face in (3), hence is
ordinary.  Intersecting the output with the fixed disjoint regions
`union mathcal L`, `T`, and `union mathcal R` recovers `L,S,R`, so the map
is injective.  QED.

Put `theta=N/(AB)`.  The cross-completion part of (6) gains the exact factor

\[
                              {AB\over N}={1\over\theta}.           \tag{7}
\]

This is useful precisely when the selected histories are anti-aligned.
If `log(1/theta)>=delta(log n)^2`, it gives a `delta` coefficient gain.
If `log(1/theta)=o((log n)^2)`, the cell is entropy-near-product, but it
need not contain any large exact Cartesian subfamily: dense or coded
bipartite graphs already forbid that inference.  A component-surplus or
one-gap argument must use the ambient bank, not an asserted rectangle
inside `E`.

The Boolean factor `2^|T|` in (6) is also exact.  At bounded parent rank it
is coefficient-free.  It can still be a fixed-power EIC gain when
`|T|>=epsilon log D`, but no such lower rank bound is available in the
central scarcity residue.

## 2. Exact rooted-diagonal corollary and its boundary

Fix a trace `jl`, a side sign, a left tangent pair `(p,q)`, and a right
tangent pair `(r,s)`.  In the notation of
`agent_one_sided_reflection/ROOTED_DIAGONAL_AMALGAMATION.md`, suppose

\[
                         t(p,r)>0,\qquad t(q,s)<1.        \tag{8}
\]

Let `mathcal L_(p,q)` be all left rooted side faces with tangent pair
`(p,q)` and define `mathcal R_(r,s)` analogously.  The two-tangent theorem
says that (3) holds with `T={j,l}`.  Theorem 1 therefore gives

\[
                4|\mathcal L_{p,q}|\,|\mathcal R_{r,s}|            \tag{9}
\]

ordinary faces after allowing every subset of the root trace.  If the
trace is retained, the mixed bank itself has the exact product size.

The **trace-retaining** part of this bank sums globally.  From such an
output the two side faces and their tangent pairs are recovered.  Summing
over all traces, a rank-`k` output occurs at most once for each
consecutive-x diagonal, hence at most `k-1` times.  This is exactly the
overlap theorem already proved in the rooted-diagonal report; no factor for
the potentially `n^4` tangent states is incurred.  The three variants in
(9) which delete at least one root label are only a local Boolean bonus and
are not assigned this global load bound.  Even if one first pigeonholes a
state, its label description costs only `O(log n)` bits and no leading
coefficient.

The qualification is structural.  A radial depth-`j` source has a larger
remaining parent `T_j`, and its left and right petals need not form rooted
faces on opposite sides of one trace line.  Convexity of
`L union {j,l} union R` does not imply convexity after the other points of
`T_j` are restored.  Therefore (8) is a rigorous restricted extraction,
not a proof that all fixed-parent histories cross-complete.

## 3. Fixed-parent edge localization

There is nevertheless an exact parent-preserving reduction.  Let `T` be a
strictly convex parent, let every label of `L` lie strictly to the left of
every label of `T`, and every label of `R` strictly to its right.  Assume
both `T union L` and `T union R` are convex.

In the cyclic hull order of `T union L`, the labels of `L` form one
contiguous block: a vertical line separating `L` from `T` cuts the boundary
in two points, and its left boundary cap is connected.  Deleting that block
from the cyclic order leaves the cyclic order of `T`; hence its two parent
neighbours form one hull edge `g_L` of `T`.  Define `g_R` analogously.

> **Theorem 2 (edge-splice trichotomy).**
>
> 1. If `g_L` and `g_R` are vertex-disjoint, then
>    `T union L union R` is convex.
> 2. If they are distinct and share one parent vertex `z`, every turn in
>    the spliced cyclic order is already a turn of `T union L` or
>    `T union R`, except the turn at `z`.  Thus the union is convex if and
>    only if that one turn, between the two petal neighbours of `z`, has
>    the parent orientation.  After those two tangent labels are fixed,
>    every cross-combination is ordinary.
> 3. If `g_L=g_R=g`, then
>    
>    \[
>       T\cup L\cup R\text{ is convex}
>       \iff g\cup L\cup R\text{ is convex}.             \tag{9a}
>    \]
>    
>    All interaction has localized to the one-edge rooted child on `g`.

**Proof.**  Insert the cyclic `L`-block into edge `g_L` of the parent order
and the cyclic `R`-block into `g_R`.  When the edges are distinct, the
resulting polygonal sequence is simple: its two arcs from the global
leftmost to global rightmost vertex are the corresponding x-monotone hull
chains inherited from `T union L` and `T union R`.  If the edges are
vertex-disjoint, every consecutive turn is inherited from one of those two
convex polygons or from `T`, so every turn is strict and has the same sign.
The splice is convex.  If the edges share `z`, precisely the two incident
edges at `z` have both changed, proving part 2 by the same turn test.

For part 3, necessity follows by deletion.  Conversely put
`Z=g union L union R`.  The polygons `T` and `Z` lie in opposite closed
halfplanes of the line through `g` and share that edge.  Concatenate their
non-root boundary paths.  Internal turns are convex.  At either endpoint
of `g`, the neighbour supplied by `Z` belongs to `L` or `R`; the same turn
already occurs in the convex polygon `T union L` or `T union R`.
Consequently the concatenated boundary is strictly convex.  QED.

For a rank-`r` parent there are at most `r^2` ordered gap pairs.  On the
bounded-rank slice this is only polylogarithmic.  In the adjacent case,
fixing the two petal neighbours costs at most `n^2`, or `O(log n)` bits.
Thus every quadratic same-parent family either enters a complete
cross-profile at coefficient-free localization cost, or concentrates in
the same-edge child (9a) with its source mass intact.

This reduction also preserves the global decoder in a fixed depth/rank
cell.  A trace-retaining cross output has exactly `j` labels to either side
of `T`; peeling the `j` extreme pairs recovers the parent.  The theorem does
not solve the same-edge child: arbitrary one-sided rooted order types and
pair-valued anti-alignment remain possible there.  It does sharpen the
larger-parent gap to that single rooted lane.

## 4. Scalable marked planar MDS anti-module family

Fix `j>=3` and a prime power `q>=2j`.  Take `2j` tiny pairwise disjoint
rational arcs on one conic, `j` on either side in x-order, and put `q`
labelled points in each arc.  Add five further conic points in one empty
central arc, in cyclic order

\[
                         T=\{a,u,p,v,b\}.                \tag{10}
\]

Choose the arc so that `e={b,a}` is the endpoint pair in x-order, every
left cluster lies to the left of `b`, and every right cluster to the right
of `a`.  Choose a rational point `x` strictly inside the triangle
`{b,p,a}`, avoiding the finitely many collinearities.  The only labels in
the open x-interval of `e` are then `u,p,v,x`.

This construction scales for every admissible `j,q`.  Start with the fixed
rational core used by the verifier and choose the cluster parameters
successively in the same disjoint rational intervals.  The x-order,
endpoint interval, and cyclic repair cell are strict open conditions.
At each choice only finitely many rational parameters cause a collinearity
with `x` and one already chosen point, so they can be avoided.  All chosen
conic points remain extreme, independently of their number.

Every set consisting of `T` and one point from each cluster lies on the
conic and is therefore in convex position.  Peeling its leftmost and
rightmost labels `j` times leaves exactly `T`.  Put

\[
              W=F=\{p,x\}.                              \tag{11}
\]

This is an ordinary marked shield containing `p`, while `e union W` is
nonconvex because `x` lies inside `conv{b,p,a}`.  For every source `S`,
deleting `p` makes `uv` a hull edge and adding `p` is an exterior insertion
into that edge.  The local cyclic repair cell is exactly
`(a,u,p,v,b)`, independent of the codeword.  Also `S union F` is nonconvex,
since it contains the same interior point `x`.  Thus the construction
retains the actual repair mark, tangent neighbours, shield, common interval
tag, parent, endpoint, and depth.

Among the four interval labels, the compatible endpoint-rank counts from
rank two through six are

\[
                         (1,4,4,1,0).                    \tag{12}

\]

In particular the same-rank endpoint baseline is exactly `C_(e,5)=1`,
the unique face being `T`.

Let `C` be the `[2j,j,j+1]_q` Reed--Solomon code and select the transversal
with coordinate word `c` for every `c in C`.  There are `N=q^j` selected
sources over the same parent.  The same-rank raw density is `q^j`.
Because the endpoint half-weight is

\[
 p_eF={1\over4}+{4\over8}+{4\over16}+{1\over32}
     ={33\over32},                                      \tag{13}
\]

the fixed-cell likelihood ratio is exactly

\[
                h_{j,e}={q^j\over33\,4^j},\qquad
                4^jh_{j,e}={q^j\over33}.                \tag{14}
\]

Thus both the common blocked tag and high same-rank tilt coexist with a
constant endpoint baseline.

> **Theorem 3 (MDS module obstruction).**  Let a Cartesian subfamily of a
> code be a product over disjoint coordinate blocks, and call a block
> varying if its factor has at least two elements.  In a length-`d` code
> of distance `Delta`, every varying block has size at least `Delta`.
> Hence there are at most `floor(d/Delta)` disjoint varying blocks.

**Proof.**  Hold every other factor fixed and choose two values in the
given factor.  The resulting two codewords differ only on that block, so
the block has size at least the minimum distance.  Disjointness gives the
second assertion.  QED.

For the code above, `d=2j` and `Delta=j+1`, so there is at most one varying
block.  In particular there is no product of `Theta(j)` nontrivial modules
inside the selected histories.

Unlike an unmarked radial wrapper, no shortening is needed to fix the live
tangent state: all five labels `(a,u,p,v,b)` belong to the common parent.
The complete `q^j` code lies in one marked/tangent/shield cell.

## 5. The alternative square bank in the same geometry

Projection of a degree-`<j` polynomial to either set of `j` evaluation
coordinates is bijective.  Hence the unshortened left and right projection
alphabets both have size `q^j`.  Arbitrarily combine one left projection
and one right projection.  The result is still one point from every conic
cluster, so together with `T` it is an ordinary face.  Theorem 1 gives

\[
                    |\mathcal B|=q^{2j}=N^2.            \tag{15}
\]

The output itself recovers all cluster labels, so the bank has load one in
this cell.  No interval face is adjoined: (11) explicitly forbids the
naive common-`W` mixing.  The gain comes from omitted-petal cross-completion,
not from the interval reservoir or endpoint baseline.

Take `j=(kappa+o(1))log n` and `q=n^{1-o(1)}` (the configuration size is
`2jq+O(1)`).  The selected marked family has

\[
             \log N=(\kappa+o(1))(\log n)^2,            \tag{16}
\]

whereas (15) has coefficient `2kappa`.  With `kappa=1/4`, the exact planar
anti-module regression therefore pays coefficient `1/2-o(1)`, rather than
obstructing it.

## 6. What remains exact

The scarcity audit leaves the following clean gate.

1. If a quadratic same-parent family localizes to complete compatible
   left--right profiles and the sum of projection entropies exceeds source
   entropy by `Omega((log n)^2)`, (6) gives the required coefficient jump
   with bounded decoder load.
2. If the profiles are entropy-near-product, no exact product inside the
   selected graph may be assumed.  One must apply the one-gap/component
   surplus to the ambient completion alphabet, or prove a dense-profile
   stability statement which survives pair-valued anti-alignment.
3. Theorem 2 supplies the parent-preserving decomposition: only a same-edge
   one-sided rooted child can still couple the two sides.  The missing
   theorem is a product-or-surplus result in that child, not a lower bound
   on `C_(e,r)` and not interval-reservoir mixing.

This is the precise extraction interface needed for the conditional
`3/8` jump.  The MDS construction kills the stronger internal-module
formulation and simultaneously supplies the mandatory alternative bank.
It does not close EIC' or prove an unconditional coefficient above `1/4`.
