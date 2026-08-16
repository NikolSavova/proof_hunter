# Literal interval loads: common-face localization and a circuit trichotomy

**Date:** 2026-08-15  
**Verdict:** the global Hall allocation is not closed, but the literal
parent-times-interval demand now has an exact common-face localization and a
rigorous bounded-rank trichotomy.  The useful localization is for the
**blocked excess** `sum_j S_j-M`, not for the total demand: the empty face is
always a maximizer candidate for total load and makes that statement alone
vacuous.  A fixed-power blocked excess instead localizes to a genuine rank at
least two interval face.  At that face, either one endpoint fibre has large
aggregate radial tilt or fixed-power many distinct endpoint pairs share one
canonical planar four-circuit profile.  Compatible records separately give
ordinary mixed outputs which retain and recover their interval tags.

No scalable planar low-mean counterexample is constructed, and the final
common-circuit fibre is not allocated here.

All logarithms are base two.  Use the notation of
`TWO_REFERENCE_HALL_DEMAND_GATE.md`.  In particular

\[
 S_j=\sum_e{q_{j,e}\over\lambda_e},\qquad
 h_{j,e}={q_{j,e}\over p_e},\qquad Z_e=4G_e.              \tag{1}
\]

## 1. Exact load of one ordinary interval face

The literal depth-`j` record attached to an endpoint cell `e` and an
interval face `W subset I_e` has weight

\[
                         q_{j,e}{2^{-|W|}\over Z_e}.      \tag{2}
\]

The ordinary half-Gibbs capacity of `W` is

\[
                         \pi(W)={2^{-|W|}\over F}.        \tag{3}
\]

Thus its normalized cumulative load is

\[
 \ell(W):={1\over\pi(W)}
 \sum_{j,e:\,W\subset I_e}q_{j,e}{2^{-|W|}\over Z_e}.
                                                                    \tag{4}
\]

> **Theorem 1 (literal-load identity).**
>
> \[
> \boxed{
> \ell(W)={1\over4}\sum_{j,e:\,W\subset I_e}h_{j,e},
> \qquad
> \sum_jS_j=\mathbb E_{W\sim\pi}\ell(W).}               \tag{5}
> \]

**Proof.**  Since `p_e=G_e/F`,

\[
 F{q_{j,e}\over Z_e}
 =F{p_eh_{j,e}\over4G_e}={h_{j,e}\over4},               \tag{6}
\]

which proves the first formula.  Multiply it by `pi(W)`, sum over all
ordinary faces, and interchange `W` with `(j,e)`.  The inner sum is

\[
 \sum_{W\subset I_e}\pi(W){h_{j,e}\over4}
 ={F_e\over F}{h_{j,e}\over4}
 ={q_{j,e}\over\lambda_e}.                              \tag{7}
\]

Summing gives the second formula.  QED.

Consequently

\[
 \boxed{\max_W\ell(W)\ge\sum_jS_j.}                     \tag{8}
\]

Combined with the Jensen bridge, if

\[
 M\le c_0\log n,\qquad D\ge\delta(\log n)^2,             \tag{9}
\]

then one actual ordinary face satisfies

\[
                         \ell(W)\ge M n^{\delta/c_0}.     \tag{10}
\]

There is no union bound or interval multiplicity loss in (10).

There is, however, a load-bearing warning: `W=emptyset` is contained in
every interval and `ell(emptyset)>=ell(W)` for every `W`.  Thus (8)--(10) by
themselves do **not** force a nontrivial interval tag.  The blocked-excess
identity below is the correct repair.

### Compatible records account for exactly the base radial mass

Split (4) according to whether `e union W` is convex.  Write the two loads
as `ell_+(W)` and `ell_-(W)`.  Since the compatible interval traces have
half-weight `Z_e`, another interchange gives

\[
 \boxed{
 \mathbb E_\pi\ell_+(W)=\sum_j\tau_j=M,
 \qquad
 \mathbb E_\pi\ell_-(W)=\sum_jS_j-M.}                   \tag{11}
\]

Thus all excess inverse-capture demand is literally the load of blocked
parent-times-interval records.

In particular,

\[
 \boxed{\max_W\ell_-(W)\ge\sum_jS_j-M.}                 \tag{11a}
\]

Every target with positive blocked load has rank at least two: an endpoint
pair together with zero or one interval point is always convex.  Hence a
fixed-power excess, unlike the total-load maximum, produces a genuine
nonempty common interval tag.

## 2. Bounded-rank common-face trichotomy

Fix an ordinary face `W` of rank `w`, and suppose only depths `0<=j<J` are
active.  Give every cell `(j,e)` containing `W` weight

\[
                         a_{j,e}={h_{j,e}\over4}.         \tag{12}
\]

Its total is `ell(W)`.  Aggregate the depths over one endpoint pair:

\[
 \eta_e(W)=\sum_{j:\,W\subset I_e}h_{j,e},\qquad
 H_W=\sum_e\eta_e(W)=4\ell(W),\qquad
 \eta_*(W)=\max_e\eta_e(W).                            \tag{12a}
\]

A cell is **good** if `e union W` is convex and **bad** otherwise; this
classification depends only on `(e,W)`, not on the depth.

For a bad cell choose the lexicographically first inclusion-minimal
nonconvex subset of `e union W`.  In planar general position this is a
four-circuit.  Since `W` and `e` are separately convex, its intersection
with `W` has size two or three:

* a `2+2` profile is its two-point subset of `W`; or
* a `1+3` profile is its three-point subset of `W` together with whether
  the participating endpoint is the left or right endpoint.

There are at most

\[
                  N(w)=\binom w2+2\binom w3             \tag{13}
\]

profiles.

> **Theorem 2 (aggregate tagged-mixing/circuit split).**  If the good
> endpoint pairs carry at least `H_W/2` of the aggregate tilt, then there
> are at least
>
> \[
>                       {H_W\over2\eta_*}                \tag{14}
> \]
>
> distinct good endpoint pairs `e`.  The ordinary faces `e union W` are
> distinct and recover `e` as their two extreme labels.  Otherwise one
> profile from (13) carries aggregate tilt at least
>
> \[
>                       {H_W\over2N(w)}                  \tag{15}
> \]
>
> on at least
>
> \[
>                       {H_W\over2N(w)\eta_*}            \tag{16}
> \]
>
> distinct bad endpoint pairs.
>
> More directly, if `H_W^-` is the aggregate tilt on bad pairs, then one
> profile carries tilt at least `H_W^-/N(w)` on at least
> `H_W^-/(N(w)eta_*)` distinct pairs.  Finally, an endpoint fibre of tilt
> `eta_e` contains a depth `j` for which some compatible parent `T` obeys
>
> \[
>                        d_j(T)\ge{4^j\eta_e\over J}.     \tag{17}
> \]

**Proof.**  Each endpoint pair carries at most `eta_*`.  If the good tilt is
at least `H_W/2`, division by this maximum proves (14).  For good `e`, all
points of `W` lie strictly between the endpoints in the fixed label order,
so `e` is recovered as the minimum and maximum of `e union W`.

Otherwise the bad tilt exceeds `H_W/2`.  Pigeonhole its canonical circuits
among the at most `N(w)` profiles.  One profile carries at least (15), and
division by `eta_*` proves (16).  The same argument with `H_W^-` gives the
more direct blocked form.  Finally one of the `J` depths in an endpoint
fibre has `h_(j,e)>=eta_e/J`, while

\[
 h_{j,e}={1\over4^jG_e}
     \sum_{T:e(T)=e}d_j(T)2^{-|T|}.                      \tag{17a}
\]

The denominator `G_e` is exactly the half-weight of compatible parents in
that endpoint cell.  Its average `d_j(T)` therefore is at least
`4^j eta_e/J`, proving the last assertion.  QED.

Splitting according to whether `eta_*>=sqrt(H_W)`, if `J` and `w` are
`n^{o(1)}`, fixed-power load yields one of:

* a fixed-power radial degree in one actual endpoint cell;
* `H_W^(1/2)n^{-o(1)}` distinct ordinary mixed faces with exact interval-tag
  recovery; or
* `H_W^(1/2)n^{-o(1)}` distinct endpoint pairs in one fixed common-face,
  fixed-circuit-profile fibre.

This is the requested concentration-versus-spread statement.  It does not
erase the interval tag in the successful mixed branch.

## 3. Rank-free compression of the blocked branch

The polynomial `N(w)` loss can be removed without assuming that the common
target `W` has small rank, at the price of retaining only the actual circuit
trace rather than all of `W`.

For every bad endpoint pair `e`, let `rho(e)` be its canonical profile from
(13), and put

\[
 B_W=\sum_{e\text{ bad}}\eta_e=4\ell_-(W),\qquad
 b_* =\max_\rho\sum_{e:\rho(e)=\rho}\eta_e.             \tag{18}
\]

> **Theorem 3 (rank-free weighted circuit compression).**  If `B_W>0`,
> then
>
> \[
> |\{\rho(e):e\text{ bad}\}|\ge {B_W\over b_*},\qquad
> \max_\rho|\{e:\rho(e)=\rho\}|\ge {b_*\over\eta_*}.  \tag{19}
> \]
>
> Consequently at least one of the following holds:
>
> 1. `eta_* >= B_W^(1/3)`;
> 2. there are at least `B_W^(1/3)/2` distinct ordinary rank-two or
>    rank-three circuit traces inside `W`; or
> 3. one fixed trace and circuit role is shared by at least `B_W^(1/3)`
>    distinct endpoint pairs.
>
> In alternative 3 the graph formed by those endpoint pairs contains
> either a star of degree at least `sqrt(R)` or a matching of size at least
> `sqrt(R)/2`, where `R` is its number of edges.

**Proof.**  The first inequality in (19) divides total profile weight by
the largest profile weight.  The second divides the largest profile weight
by the largest endpoint weight.  Suppose alternative 1 fails.  If
`b_*<=B_W^(2/3)`, (19) gives at least `B_W^(1/3)` profiles.  A trace has at
most two endpoint roles, so at least half as many traces are distinct.  If
`b_*>B_W^(2/3)`, the second inequality in (19) gives alternative 3.

For the last assertion let `Delta` be the maximum degree of the endpoint
graph.  If `Delta>=sqrt(R)`, take its largest star.  Otherwise any maximal
matching has size at least `R/(2Delta-1)>sqrt(R)/2`, because the endpoints
of a maximal matching cover all edges.  QED.

This theorem converts any high-rank blocked target into a fixed-power
low-rank trace bank, a heavy endpoint fibre, or the same common rooted
circuit atom as the bounded-rank argument.  It is important not to call the
trace bank a completed Hall routing: replacing `W` by its circuit trace
erases the rest of `W`, and many parent records can reuse the same trace.  What it
does prove is that **target rank itself is no longer the obstruction**.

## 4. Rank cutoff and the precise residual

On the rigorously truncated source slice `|U|<4log n`, one has
`J<=2log n`.  If the fixed-power **blocked excess** in (11a) is carried by a
target face of rank `w=O(log n)`, then

\[
                         JN(w)=(\log n)^{O(1)}=n^{o(1)}.  \tag{20}
\]

Theorem 2 therefore preserves a fixed power whenever the full target has
small rank.  For a high-rank target, Theorem 3 preserves a cube-root fixed
power while compressing to rank at most three.  The precise residual is no
longer a rank cutoff: it is the overlap caused by erasing `W-rho(e)`.

Thus the surviving geometric atom is one ordinary two- or three-point
trace, one circuit role, and fixed-power many endpoint pairs, possibly
localized first to a high-radial-history endpoint fibre.  A further planar
first-divergence or guarded-downshadow theorem must retain enough of the
discarded target to turn this atom into tagged mixed faces or a recoverable
shield bank.  The empty-face observation also rules out using the
unqualified maximum in (8) as that theorem's starting point.

## 5. Verification

Run

```bash
python3 \
  phase2/loop/erdos838/agent_outer_internal_product/verify_literal_interval_load_dichotomy.py
```

The verifier uses the exact rational nine-point planar instance from the
two-reference report.  It enumerates every face and radial occurrence,
checks both identities in (5), the good/bad split (11), and the normalized
load formula cell by cell.  It verifies that the maximum blocked target has
rank at least two.  For every loaded target it extracts canonical
four-circuit profiles and checks the aggregate Theorem 2 and the rank-free
compression inequalities (19) with exact rational weights.  It writes
`literal_interval_load_dichotomy_certificate.json`.
