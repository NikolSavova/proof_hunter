# High detached load routes through the source-ear graph

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

A large pointwise detached load `Lambda_det` is not yet a hard branch when
the convex bad-pair ear from the old source context is retained.  Every
detached record has two ordinary one-face targets:

\[
                  W_r=F_r\cup\{v_r\},\qquad
                  E_r=A_r\cup e_r,                       \tag{1}
\]

where `e_r={v_r,u_r}` and `A_r union e_r` is the original source-ear face.
Route each record fractionally to either endpoint of the incidence graph
`W_r--E_r`.  The exact optimal load is

\[
 \boxed{\displaystyle
 \lambda_*=max_{\varnothing\ne\mathcal R'\subseteq\mathcal R}
 {\sum_{r\in\mathcal R'}w_r
  \over|\{W_r,E_r:r\in\mathcal R'\}|}.}                 \tag{2}
\]

Consequently

\[
                         \sum_rw_r\le\lambda_*V(P).       \tag{3}
\]

This is stronger than charging every record to its detached output.  A
fixed detached face shared by arbitrarily many different bases or partner
endpoints is harmless if the corresponding source ears are distinct: the
star routes with load at most one (and has exact fractional load
`m/(m+1)`).

There is an exact residual.  If `lambda_*>K`, some weighted subgraph has,
after pruning, weighted degree greater than `K` at **every** surviving
ordinary face.  If the actual multiplicity of one ordered pair `(W,E)` is
at most `Delta`, every surviving face has more than `K/Delta` distinct
neighbors.  Thus failure of the source-ear routing is not a high detached
star; it is a dense two-sided detached-face by source-ear core.

The geometric pair decoder is exact after role coloring.  From `(W,E)` one
recovers `v=W cap e`, the partner `u=e-v`, the pocket trace `F=W-v`, and the
old source base `A=E-e`.  Any remaining ambiguity is precisely the actual
root/guard/context multiplicity `Delta`; it must not be silently removed.

A scalable rational cage shows the theorem is sharp in form.  One fixed
detached face `W={x,a}` can be shared by arbitrarily many convex old-base
ears `B union {a,b_j}`, while every attached face `B union {x,a}` remains
nonconvex.  The raw detached load tends to infinity, no attached mixed
output appears, but the varying source-ear faces give an exact load-one
star.  Hence the correct positive operation is Hall routing, not forced
local mixing.

This theorem is conditional on `A_r union e_r` being an actual ordinary
source face.  If the live matching supplies only individual endpoint faces
and not convex pair ears, the one-face target `E_r` is unavailable and the
statement does not apply.

## 1. Weighted source-ear routing

Let `mathcal R` be a finite family of canonical records with nonnegative
weights `w_r`.  Record `r` contains:

* an old convex source base `A_r`;
* a convex pair ear `e_r={v_r,u_r}` such that `E_r=A_r union e_r` is an
  ordinary face;
* a retained convex pocket trace `F_r`, disjoint from the endpoint roles;
  and
* a chosen endpoint `v_r` such that `W_r=F_r union {v_r}` is an ordinary
  detached face.

Let

\[
 \mathcal B_r=\{W_r,E_r\}\subseteq\mathcal F(P).          \tag{4}
\]

A fractional routing consists of `a_(r,X)>=0`, supported on
`X in mathcal B_r`, with

\[
                            \sum_{X\in\mathcal B_r}a_{r,X}=w_r.       \tag{5}
\]

Define

\[
                       \lambda_*=min_a\max_X\sum_ra_{r,X}.          \tag{6}
\]

> **Theorem 1 (detached/source-ear Hall routing).**  Equations (2)--(3)
> hold.

**Proof.**  Build a flow network in which the source sends `w_r` to record
`r`, record `r` sends to its one or two distinct targets in (4) with
infinite capacity, and every ordinary face sends capacity `lambda` to the
sink.  Max-flow/min-cut says all demand is routable exactly when

\[
       \sum_{r\in\mathcal R'}w_r
          \le\lambda|\bigcup_{r\in\mathcal R'}\mathcal B_r|          \tag{7}
\]

for every record subfamily.  Minimizing `lambda` proves (2).  For an
optimal routing,

\[
 \sum_rw_r=\sum_X\sum_ra_{r,X}
       \le V(P)\max_X\sum_ra_{r,X}=\lambda_*V(P),          \tag{8}
\]

which proves (3).  QED.

The formula is the two-target specialization of the global fractional
rectangle--shield telescope.  Its value is not bounded by the maximum raw
detached load.  For a star with one common `W` and pairwise distinct
`E_1,...,E_m`, send record `j` entirely to `E_j`; this gives load one,
while balancing against the center gives the exact optimum

\[
                 \Lambda_{\rm det}=m,\qquad
                 \lambda_*={m\over m+1}<1.                          \tag{9}
\]

This is exactly the high-load configuration in the rational example below.

## 2. Exact decoder and the true multiplicity

Assume the endpoint role and the pocket/source supports have been fixed by
a canonical role coloring.  Then `E_r cap X_endpoint=e_r` and
`W_r cap X_endpoint={v_r}`.  Therefore

\[
\begin{aligned}
 v_r&=W_r\cap e_r,&u_r&=e_r\setminus\{v_r\},\\
 F_r&=W_r\setminus\{v_r\},&A_r&=E_r\setminus e_r.        \tag{10}
\end{aligned}
\]

The ordered pair `(W_r,E_r)` recovers all geometric labels in the record.
Define the actual residual context load

\[
 \Delta=\max_{W,E}
       \sum_{r:(W_r,E_r)=(W,E)}w_r.                       \tag{11}
\]

This is where an omitted root, deleted guard, carrier description, or
duplicated canonical history lives.  If the context is a function of the
recovered labels, `Delta` is the maximum record weight; for unit canonical
records it is one.

In particular, for a fixed detached output `W`, grouping by its source-ear
neighbors gives

\[
 \sum_{r:W_r=W}w_r
       \le\Delta\,|\{E_r:W_r=W\}|
       \le\Delta V(P).                                    \tag{12}
\]

Thus varying bases or partner endpoints force literal source-face
expansion.  A genuinely high fixed-`W` fibre must instead reuse the same
source ear with high context multiplicity, and (11) records that obstruction
exactly.

## 3. Failure localizes to a dense two-sided core

Regard the targets as vertices of a weighted multigraph and the records as
edges; an edge of the form `W=E` may be treated as a loop with one target.

> **Corollary 2 (dense-core alternative).**  If `lambda_*>K`, there is a
> nonempty record subfamily whose induced target graph can be pruned so
> that every surviving target face has incident record weight greater than
> `K`.  If (11) is at most `Delta`, every surviving target has more than
> `K/Delta` distinct neighbors.

Choose a subfamily violating (7) at `lambda=K`.  Repeatedly delete any
target vertex with incident weight at most `K`, together with its incident
records.  If all vertices were deleted, each record weight would be charged
at its first deleted endpoint and the total removed weight would be at most
`K` times the number of original target vertices, contradicting the chosen
violation.  Hence a nonempty core remains and has the asserted weighted
minimum degree.  One neighbor contributes at most `Delta` by (11), proving
the distinct-degree statement.

This is the exact high-`Lambda_det` localization requested by the endpoint
trichotomy.  A positive planar theorem may now assume simultaneous high
reuse on both axes.  The known three-arc carrier--root rectangle shows that
such two-sided cores are not forbidden by planarity; in its natural
realization a detached outer shield pays.  Proving that every live dense
core exposes an analogous shield remains the geometric step.

## 4. A scalable fixed-detached-face cage

Put

\[
\begin{aligned}
 l&=(-3,0),&r&=(3,0),&t&=(0,5),\\
 a&=(-2,-1),&x&=(0,-4),&b&=(2,-1),                       \tag{13}
\end{aligned}
\]

and `B={l,r,t}`.  The six-point cage in
`ENDPOINT_POCKET_CODEGREE_DICHOTOMY.md` has

\[
 B\cup\{a,b\}\text{ convex},\qquad
 a\in\operatorname{int}\triangle(l,x,r).                \tag{14}
\]

Both properties are strict and open.  For every `m`, choose distinct
rational general-position points `b_1,...,b_m` in a sufficiently small
neighborhood of `b`, avoiding the finitely many lines determined by
earlier labels.  Then simultaneously

\[
\begin{aligned}
 E_j&=B\cup\{a,b_j\}\text{ is convex for every }j,\\
 W&=\{x,a\}\text{ is convex},\\
 B\cup\{x,a\}&\text{ is nonconvex}.                      \tag{15}
\end{aligned}
\]

Use one context for each pair ear `e_j={a,b_j}`, with pocket trace
`F={x}` and detached endpoint `v=a`.  All `m` records output the same `W`,
so their raw detached load is `m`.  Their source-ear outputs `E_j` are
distinct, so (9) routes with load at most one.  The third line of (15) rules out
the tempting attached mixed output in every context.

This example is scalable but harmless.  It proves that high detached load
need not cause local coexistence; the varying source ears are the correct
payment.  It does not model the dense-core residue of Corollary 2, because
its source-ear degree is one.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_detached_load_source_ear_hall.py
```

Expected output:

```text
PASS: exact Hall loads; fixed-W stars route through source ears; rational cages retain bad attachment
```

The verifier solves the routing LP by exact max-flow/min-cut enumeration on
weighted graphs, checks (2) and the dense-core pruning alternative, and
uses exact rational orientation arithmetic to verify the cage star through
fifty partner endpoints.

## Scope

This theorem controls high detached overlap whenever the original convex
pair-ear face survives as an admissible source target with bounded context
multiplicity.  It does not prove the remaining dense-core shield theorem,
and it does not apply to matching classes lacking pair-ear convexity.
