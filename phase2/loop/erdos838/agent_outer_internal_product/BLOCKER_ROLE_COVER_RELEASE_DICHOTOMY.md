# Blocker-role covers: exact whole-face release or a disjoint circuit matching

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

There is an exact positive replacement for the false strong-separation
profile lemma.

Fix one role `X_0` in a complete cyclic same-type product and one ordinary
local face `F subseteq X_0`.  Its incompatibilities with external
singleton roles form a graph with loops:

* a loop at role `r` records a bad `3+1` circuit using three points of `F`;
* an edge `rs` records a bad `2+2` circuit using two points of `F`.

A set `J` of macro roles may be deleted so that `F` coexists with
**every** transversal of the remaining roles if and only if `J` is a
vertex cover of this blocker graph.  This is an immediate but powerful
consequence of planar four-locality.

For a local reservoir `mathcal H`, if a positive fraction of its faces
have covers of size at most `t`, one fixed cover `J` releases at least

\[
 { |\mathcal H_{\le t}|\over
        \sum_{s=0}^t {q-1\choose s}}                  \tag{1}
\]

whole local faces.  Crossing them with all singleton choices outside `J`
is an injective one-face bank.  If `q=O(log D)` and the deleted alphabet
entropy is `o((log D)^2)`, this bank adds the full local coefficient to the
outer-product coefficient.  In particular, outer coefficient `1/4` plus
local coefficient `1/4` gives `1/2`.

The synthesis-ready form is stronger and weighted.  Give role `r` the
cost `s_r=log|X_r|` and assign each face its canonical minimum-cost cover.
There is no need to pigeonhole the cover: different covers give disjoint
banks because the output occupancy mask recovers exactly which roles were
deleted.  If `sigma(F)` is the deleted cost and `F` is uniform in the
reservoir, the exact union and Jensen give

\[
 |\mathcal B|=P_{\rm ext}\sum_F2^{-\sigma(F)}
       \ge P_{\rm ext}|\mathcal H|,2^{-\mathbb E\sigma(F)}.           \tag{1a}
\]

Thus it is the **average** cover entropy, not the worst cover or number of
cover patterns, which controls whole-face release.

If the small-cover branch fails, every surviving blocker graph has a
matching of more than `t/2` pairwise disjoint role traces.  This is exact,
but it does not by itself produce a two-ended face bank.  A scalable
planar regression has quadratic local and outer product entropy while all
matched traces are singleton `3+1` loops.  Hence a closure based only on
crossing `2+2` witnesses is false.  The live high-cover residue must use a
many-root/outer-shield theorem which also handles repeated `3+1` blockers.

This report closes the whole-face release branch.  It does not close the
high-cover matching branch or cross-base summation, and makes no EIC'
closure claim.

## 1. Complete cyclic products and blocker graphs

Let `X_0,X_1,...,X_(q-1)` be pairwise disjoint planar supports in general
position.  Assume every transversal in

\[
                         \prod_{r=0}^{q-1}X_r          \tag{2}
\]

is a convex set.  A fixed cyclic type is more than enough, but the theorem
below uses only convexity of every partial transversal.

Fix a nonempty ordinary face `F subseteq X_0`.  Define a graph with loops
`G_F` on the external role set `[q-1]={1,...,q-1}` as follows.

* Put a loop `{r}` in `G_F` if there are distinct `u,v,w in F` and
  `x_r in X_r` for which `{u,v,w,x_r}` is nonconvex.
* Put an edge `{r,s}`, `r ne s`, in `G_F` if there are distinct `u,v in F`
  and labels `x_r in X_r,x_s in X_s` for which
  `{u,v,x_r,x_s}` is nonconvex.

A vertex cover must contain the endpoint of every loop and at least one
endpoint of every ordinary edge.  Write `tau(F)` for its minimum size.

> **Theorem 1 (exact blocker-cover criterion).**  For
> `J subseteq[q-1]`, the following are equivalent.
>
> 1. `J` is a vertex cover of `G_F`.
> 2. For every choice `x_r in X_r`, `r notin J`, the set
>
>    \[
>                     F\cup\{x_r:r\notin J\}           \tag{3}
>    \]
>
>    is an ordinary face.

**Proof.**  If `J` misses a loop or an edge, its defining bad four-set is
contained in one output (3), so (2) fails.

Conversely suppose some output (3) is nonconvex.  A finite planar set in
general position is convex if and only if all of its four-subsets are
convex: if a point is hidden, Caratheodory supplies three points whose
triangle contains it.  A bad four-subset of (3) cannot use four points of
`F`, because `F` is a face.  It cannot use at most one point of `F`,
because then it is a partial transversal of (2).  It therefore uses either
three points of `F` and one external role, or two points of `F` and two
external roles.  This is a loop or edge of `G_F` wholly outside `J`,
contradicting the cover property.  QED.

The theorem retains the actual role tag.  It does not replace a bad
circuit by an abstract unlabelled witness, so it is stable under arbitrary
alphabet sizes and arbitrary choices in all undeleted roles.

## 2. A family version and the injective release bank

Let `mathcal H` be any family of nonempty ordinary faces in `X_0`, and put
`H=|mathcal H|`.  For every `F` with `tau(F)<=t`, choose the
lexicographically first minimum cover and call it `J(F)`.  There are at
most

\[
                         N_t=\sum_{s=0}^t{q-1\choose s} \tag{4}
\]

possible values.  Pigeonholing proves (1): some fixed `J`, `|J|<=t`, is
assigned to a family `mathcal H_J` of size at least
`|mathcal H_(<=t)|/N_t`.

Theorem 1 gives the ordinary bank

\[
 \mathcal B_J=
 \left\{F\cup\{x_r:r\notin J\cup\{0\}\}:
       F\in\mathcal H_J, x_r\in X_r\right\}.          \tag{5}
\]

Since the supports are disjoint, an output recovers `F` and every external
label.  Thus the load is one and

\[
 \boxed{
 |\mathcal B_J|=|\mathcal H_J|
              \prod_{r\notin J\cup\{0\}}|X_r|.}       \tag{6}
\]

This release uses a whole local face rather than one directional chain.
It is precisely the branch suggested by the single-blocker regression.

### 2.1 Exact entropy-weighted partition

Assign every external role the nonnegative cost

\[
                              s_r=\log L_r.             \tag{6a}
\]

For a cover `J`, write `s(J)=sum_(r in J)s_r`, and let

\[
                w(F)=\min\{s(J):J\text{ covers }G_F\}. \tag{6b}
\]

Choose the lexicographically first minimum-cost cover `J_*(F)`.  For any
subfamily `mathcal A subseteq mathcal H`, its exact partition

\[
                  \mathcal A=\bigsqcup_{J\subseteq[q-1]}
                       \{F\in\mathcal A:J_*(F)=J\}      \tag{6c}
\]

has at most `2^(q-1)` cells.  Therefore, if

\[
              \mathcal H_{\le\sigma}
                   =\{F\in\mathcal H:w(F)\le\sigma\}, \tag{6d}
\]

some fixed cover `J` satisfies

\[
 s(J)\le\sigma,qquad
 |\{F:J_*(F)=J\}|\ge
                   2^{-(q-1)}|\mathcal H_{\le\sigma}|.\tag{6e}
\]

Using this exact cell as `mathcal H_J` in (5)--(6) gives the weighted
release directly.  No rank bound or estimate `t log q` is needed.

In fact the cells in (6c) should be kept together.  Put

\[
                 P_{\rm ext}=\prod_{r=1}^{q-1}L_r.      \tag{6f}
\]

For each `F in mathcal H`, use its canonical cover `J_*(F)` and all labels
in every role outside that cover.  Outputs arising from two different
faces recover their distinct intersection with `X_0`.  Outputs arising
from two different covers have different external occupancy masks.  The
union is therefore load one, with exact size

\[
\begin{aligned}
 |\mathcal B|
 &=\sum_{F\in\mathcal H}
        \prod_{r\notin J_*(F)\cup\{0\}}L_r\\
 &=P_{\rm ext}\sum_{F\in\mathcal H}2^{-w(F)}.           \tag{6g}
\end{aligned}
\]

Since `x mapsto 2^{-x}` is convex, Jensen gives

\[
 \boxed{
 |\mathcal B|\ge
 P_{\rm ext}H\,2^{-\overline w},\qquad
 \overline w={1\over H}\sum_{F\in\mathcal H}w(F).}    \tag{6h}
\]

This strictly strengthens (6e): no `2^(q-1)` loss occurs and faces with
different optimal covers all contribute.

## 3. Coefficient-half corollary

Put `L_r=|X_r|`, `P_0=prod_rL_r`, and `d=log D`, with every `L_r<=D`.
Suppose

\[
\begin{aligned}
 \log P_0&\ge(a-o(1))d^2,\\
 \log H&\ge(c-o(1))d^2,\\
 q&=O(d),\qquad \overline w=o(d^2)                     \tag{7}
\end{aligned}
\]

Then `P_ext=P_0/L_0`, `L_0<=D`, and (6h) give

\[
\begin{aligned}
 \log V(P)
 &\ge \log P_0+\log H-\log L_0-\overline w\\
 &\ge(a+c-o(1))d^2.                                   \tag{8}
\end{aligned}
\]

Thus `a=c=1/4` gives coefficient `1/2`.  More generally, average deletion
cost `overline w=(theta+o(1))d^2` gives coefficient `a+c-theta`.  This is
local to one fixed complete product.  If many external
bases reuse the same bank, the aggregate output overlap must still be
divided out exactly as in
`STRONG_SEPARATION_ROOT_BAD_INTEGRATION_AUDIT.md`.

## 4. Failure of a small cover forces disjoint circuit traces

> **Lemma 2 (cover--matching dichotomy).**  Let `nu(F)` be the maximum
> number of pairwise vertex-disjoint edges of `G_F`, with a loop using its
> one endpoint.  Then
>
> \[
>                              \tau(F)\le2\nu(F).       \tag{9}
> \]

**Proof.**  Take a maximal matching.  The union of its endpoints meets
every edge; otherwise an edge disjoint from that union could be added.
It is therefore a vertex cover, of size at most twice the matching size.
QED.

Consequently, for every threshold `t`, one of the following holds.

1. At least `H/2` local faces have `tau(F)<=t`, and Sections 2--3 give a
   fixed-cover whole-face bank.
2. At least `H/2` local faces have `nu(F)>t/2`, so each carries more than
   `t/2` disjoint bad `3+1`/`2+2` role traces.

This is the exact circuit-transversal dichotomy.  Importantly, Lemma 2
does not say that many of the matched traces are ordinary edges: they may
all be loops.

### 4.1 Weighted loop-heavy versus edge-heavy certificate

The high branch has an exact entropy-weighted refinement.  Let

\[
 L(F)=\{r:\{r\}\in G_F\},\qquad
 \ell(F)=\sum_{r\in L(F)}s_r.                           \tag{9a}
\]

Every cover contains `L(F)`.  Delete those vertices and all incident
edges, leaving an ordinary graph `G_F^o`.  If `w_o(F)` is its
minimum-cost vertex cover, then

\[
                         w(F)=\ell(F)+w_o(F).           \tag{9b}
\]

Let `nu_s^*(F)` be the maximum fractional matching value in `G_F^o` with
vertex capacities `s_r`:

\[
 \nu_s^*(F)=\max\left\{\sum_e y_e:
   y_e\ge0,\ \sum_{e\ni r}y_e\le s_r\quad\forall r\right\}.           \tag{9c}
\]

LP duality identifies this with the minimum fractional vertex-cover cost.
Rounding every fractional cover coordinate at least `1/2` upward gives an
integral cover of at most twice its cost.  Hence

\[
                          \nu_s^*(F)\ge {w_o(F)\over2}. \tag{9d}
\]

In particular, if `w(F)>sigma`, then exactly one of the following useful
certificates holds:

\[
 \boxed{
 \ell(F)>\sigma/2
 \quad\text{or}\quad
 \nu_s^*(F)>\sigma/4.}                                \tag{9e}
\]

The first is a high-entropy set of mandatory `3+1` blocker roles.  The
second is a capacity-respecting fractional packing of `2+2` blocker
traces.  Across a face family, thinning by the exact loop set `L(F)` costs
at most another `q-1` bits, so a loop-heavy quadratic face family has one
fixed common blocker-role set with the same leading coefficient.

Equation (9e) is the strongest automatic high-cover conclusion.  It does
not turn the common loop alphabet into mixed ordinary faces.

There is also an exact averaged form.  From (9b)--(9d), pointwise,

\[
                         w(F)\le\ell(F)+2\nu_s^*(F).    \tag{9f}
\]

Therefore

\[
 \boxed{
 \overline w>\Sigma
 \quad\Longrightarrow\quad
 \mathbb E\ell(F)>\Sigma/2
 \ \text{or}\
 \mathbb E\nu_s^*(F)>\Sigma/4.}                       \tag{9g}
\]

Together, (6h) and (9g) are the exact average cover-entropy dichotomy:
low mean cost pays through one disjoint union bank; high mean cost becomes
either high mean mandatory-loop entropy or high mean fractional `2+2`
packing.

## 5. Scalable high-cover regression with only `3+1` loops

The loop qualification is geometrically real and persists at quadratic
entropy scale.

Start with the rational parabola points

\[
 P_t=\left(2-\delta t^2,-{1\over5}+\delta t\right),
 \qquad 1\le t\le h,\qquad \delta={1\over100h^2}.      \tag{10}
\]

As proved in `STRONG_SEPARATION_ROOT_BAD_INTEGRATION_AUDIT.md`, for every
`i<j<k`,

\[
                         P_j\in\operatorname{int}
                              \operatorname{conv}\{P_i,P_k,c\},
 \qquad c=(0,4).                                       \tag{11}
\]

Replace the upper vertex `c` of the convex quadrilateral
`P_t,b=(4,0),c,a=(0,0)` by `k` rational vertices
`c_1,...,c_k` on a sufficiently small strictly convex cap around `c`.
All containments (11) are strict, so the cap may be chosen so that

\[
 P_j\in\operatorname{int}
       \operatorname{conv}\{P_i,P_k,c_s\}
 \quad\text{for every }i<j<k\text{ and every }s.       \tag{12}
\]

The sets `{P_t,b,c_1,...,c_k,a}` are convex in one fixed cyclic order for
every `t`.  Hence the role supports

\[
 X_0=\{P_1,\ldots,P_h\},\quad
 X_s=\{c_s\}\ (1\le s\le k),\quad \{a\},\{b\}        \tag{13}
\]

form a complete same-type, strongly separated product.

Every local face `F subseteq X_0` of rank at least three has a loop at
every blocker role `s`: choose three of its points in parameter order and
use (12).  Therefore

\[
                              \tau(F)\ge k.             \tag{14}
\]

This construction can carry two independent quadratic alphabets.  For a
large integer `A`, replace each `P_t` by an `A`-point cluster in a tiny
neighbourhood and each `c_s` by an `A`-point cluster.  Shrink successively
so all transversal convexities and containments (12) hold uniformly.
Choose

\[
                    h=\lfloor\alpha\log A\rfloor,
 \qquad            k=\lfloor\beta\log A\rfloor.       \tag{15}
\]

The local block has an ordinary transversal family of size `A^h`, while
the outer blocker roles have a complete transversal product of size
`A^k`.  With `D=Theta((h+k)A)`,

\[
 \log A^h=(\alpha+o(1))(\log D)^2,qquad
 \log A^k=(\beta+o(1))(\log D)^2.                      \tag{16}
\]

Every local transversal has all `k` blocker loops.  Thus quadratic local
mass can live entirely in the high-cover branch, and its disjoint matching
need contain no `2+2` edge at all.

The blocker product in (16) is an ordinary outer shield, but simply
placing it next to the local bank does not multiply their sizes; a
two-output code pays only through `V(P)^2`.  The construction may have
additional one-gap/profile faces and is not claimed to be a low-face or
subhalf configuration.  It is a sharp regression against the implication

\[
 \text{large blocker matching}
     \Longrightarrow\text{many crossing/two-ended }2+2\text{ witnesses}.
                                                               \tag{17}
\]

The high-cover branch therefore needs a theorem that uses the common
`3+1` blocker shield itself, or proves a recoverable first-divergence
between many such blocker roles.

There is an even sharper exact singleton recurrence in
`agent_shield_circuit_cover/BLOCKER_ROLE_HITTING_SET_BARRIER.md`.  For an
`m`-point local parabola cap and `k` blocker vertices it proves

\[
       V=2^m+\left(1+m+{m\choose2}\right)(2^k-1).       \tag{18}
\]

Every mixed face containing a blocker has local rank at most two, and all
such rank-at-most-two traces occur.  Thus the detached Boolean reservoirs
`2^m` and `2^k` provably do not multiply in this geometry.

This still is not a scalable low-face counterexample to EIC': the local
cap itself has the full Boolean bank.  Blowing the cap positions up by
arbitrary low-face children introduces separated-chain one-gap faces which
may pay.  The precise unsolved loop-heavy tradeoff is therefore:

> a common high-entropy `3+1` blocker alphabet across a quadratic
> low-face reservoir either forces a cap/first-divergence profile bank, or
> admits a genuinely low-face substitution preserving the rank-two mixed
> interface (18).

No proof of the first alternative and no genuine low-face realization of
the second is claimed here.

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_blocker_role_cover_release.py
```

The checker uses seven exact parabola labels, three rational cap blockers,
and two endpoint roles.  It verifies general position, the fixed cyclic
type, every strict containment (12), constructs every blocker graph for
all `127` nonempty local faces, exhausts all role deletions to verify
Theorem 1 in both directions, checks (9), and confirms that every rank-at-
least-three face has all three blocker loops.
