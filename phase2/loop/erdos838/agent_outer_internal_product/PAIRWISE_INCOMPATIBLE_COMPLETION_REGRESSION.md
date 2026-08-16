# Pairwise-incompatible completions: a circuit container and planar regression

**Date:** 2026-08-14.  All logarithms are base two.  This note attacks the
last residue of `COMMON_BASE_COMPLETION_SHADOW.md`: a quadratic-entropy
rank-`q` completion family over a common face, with only polynomially many
compatible partners per completion.

## Verdict

The compatibility residue admits two exact reductions.

1. Deleting only a fixed-power fraction of the family produces a
   **pairwise-incompatible** subfamily.  Every pair then has a four-circuit
   crossing its two petals.
2. Erdős--Rado gives a fixed-power sunflower inside any remaining
   quadratic-entropy rank-`O(log D)` family.  The sunflower core joins the
   common base, its petals are disjoint, all `D` one-point extension labels
   survive, and every pair of petals has a crossing four-circuit.

Neither conclusion closes the proof.  There is a scalable rational planar
regression with

\[
                         M=L^q                              \tag{1}
\]

pairwise-incompatible rank-`q` completions, all sharing the same `D`
one-point extensions.  It uses `q` pairwise nonadjacent ear pockets, each
containing an `L`-point nested chain, and chooses one point per pocket.
Only

\[
                         q{L\choose2}                       \tag{2}
\]

local four-circuits witness every one of the `Theta(M^2)` bad pairs.
Moreover the completion-trace transversal must delete at least `L-1`
labels from every pocket before the common base joins the remaining
support.

This does not refute the desired fixed-power theorem.  Each nested ear
chain is itself in convex position, so its detached Boolean bank has
`2^L` ordinary faces.  At `L=D` and `q=Theta(log D)`, this pays the
quadratic-entropy record family with enormous room.  The construction
does refute the overstrong claims that almost-pairwise incompatibility
forces few completions, many distinct circuit witnesses, a small trace
transversal, or a large **joined** common-base shield.  The remaining
theorem must find a detached/unrestricted outer shield, or an equivalent
global surplus, from the repeated local circuit containers.

## 1. From sparse compatibility to a bad-pair clique

Fix an ordinary face `F` and a family `\mathcal Q` of distinct rank-`q`
sets disjoint from it.  Assume

\[
 F\cup Q\in\mathcal F(P),\qquad
 F\cup Q\cup\{y\}\in\mathcal F(P)\quad(y\in Y_Q),           \tag{3}
\]

where `|Y_Q|=D`.  Put an edge between `Q,Q'` when
`F union Q union Q'` is ordinary; this is the compatibility graph.

> **Lemma 1 (polynomial thinning to pairwise incompatibility).**  If the
> compatibility graph has maximum degree at most `T`, then it has an
> independent set of size at least
> \[
>                       {|\mathcal Q|\over T+1}.             \tag{4}
> \]
> In particular, after Theorem 6 of the preceding report fails, one can
> retain a pairwise-incompatible family of size at least
> \[
>       {M\over 2\,3^{2q}D^{1+\epsilon}+1}.                 \tag{5}
> \]

**Proof.**  Greedily choose a vertex and delete it together with its at
most `T` neighbors.  Every choice removes at most `T+1` vertices.  Apply
this with the maximum-degree subfamily furnished by Theorem 6.  QED.

When `M=2^{Omega((log D)^2)}` and `q=O(log D)`, the denominator in (5) is
only `D^(O(1))`.  Thus the thinning preserves quadratic entropy.

For two members of the independent set, choose a bad four-subset `C` of
their union with `F`.  It necessarily satisfies

\[
 C\cap(Q-Q')\ne\varnothing,
 \qquad C\cap(Q'-Q)\ne\varnothing.                         \tag{6}
\]

Indeed, if the first intersection were empty, `C` would be contained in
the face `F union Q'`; the other assertion is symmetric.

## 2. An exact rank-one common-prefix descent

The pairwise-bad family supports a simple container descent which retains
the extension labels.

> **Lemma 2 (witness-label descent).**  Let `\mathcal Q` be pairwise
> incompatible, of rank `q>=1`, on an ambient `n`-label set.  There are a
> label `x` and a subfamily `\mathcal Q'` of size at least
> \[
>                        {|\mathcal Q|-1\over n}             \tag{7}
> \]
> such that every `Q in \mathcal Q'` contains `x`.  With
> \[
>        F'=F\cup\{x\},\qquad \widetilde Q=Q-\{x\},         \tag{8}
> \]
> the sets `\widetilde Q` are distinct rank-`q-1` pairwise-incompatible
> completions over `F'`, and all extensions in `Y_Q` from (3) survive.

**Proof.**  Fix `Q_0`.  For every other `Q`, choose a circuit from (6) and
one label `x(Q)` in its nonempty intersection with `Q-Q_0`.  Pigeonhole
the at most `n` possible labels.  For the resulting fibre, (8) gives

\[
 F'\cup\widetilde Q\cup\{y\}=F\cup Q\cup\{y\}\in\mathcal F(P).
                                                                    \tag{9}
\]

Pairwise incompatibility is unchanged because the pair unions in (8)
equal the old pair unions.  Distinctness and the rank assertion are
immediate.  QED.

Iteration gives the elementary container bound

\[
                   |\mathcal Q|\le1+n+\cdots+n^q.           \tag{10}
\]

This is sharp at quadratic-entropy scale when `n=D^Theta(1)` and
`q=Theta(log D)`.  Selecting one child at each step can spend
`n^q=2^{Theta((log D)^2)}`, so Lemma 2 is structural rather than a
fixed-power payment.

## 3. A fixed-power sunflower is unavoidable

The classical elementary sunflower bound says that a rank-`q` family with
more than

\[
                         q!(k-1)^q                          \tag{11}
\]

members contains a `k`-sunflower.  Apply it to the pairwise-incompatible
family from Lemma 1.

> **Theorem 3 (pairwise-bad sunflower child).**  There are a common core
> `R` and pairwise disjoint nonempty petals `P_1,...,P_k` such that
> `Q_i=R disjoint_union P_i` and
> \[
>       k\ge\left\lfloor
>             \left({|\mathcal Q|\over q!}\right)^{1/q}
>             \right\rfloor.                               \tag{12}
> \]
> whenever the displayed lower bound is at least two.
> The enlarged base `F'=F union R` is ordinary, every
> \[
>                  F'\cup P_i\cup\{y\}\quad(y\in Y_{Q_i})  \tag{13}
> \]
> is ordinary, and every pair `P_i,P_j` has a bad four-circuit meeting
> both petals.

**Proof.**  Choose the integer `k` in (12); then
`q!(k-1)^q<|\mathcal Q|`, so the sunflower theorem applies.  Its petals
have one common rank and are nonempty because the `Q_i` are distinct.
Equations (3) and deletion prove the base and extension assertions.
Pairwise incompatibility is inherited, and (6) now says that every witness
meets both disjoint petals.  QED.

If `log|\mathcal Q|>=a(log D)^2` and `q<=beta log D`, then

\[
                  k\ge D^{a/\beta-o(1)}.                   \tag{14}
\]

Thus the residue contains a fixed-power disjoint-petal fan.  The next
construction shows why even this is not a contradiction.

## 4. A scalable planar pairwise-incompatible product

> **Proposition 4 (nested-ear product regression).**  For every positive
> integers `q,L,D`, there is a planar general-position configuration with:
>
> * a convex base `F` of size `2q+3`;
> * pairwise disjoint `L`-point clouds `X_1,...,X_q`;
> * a `D`-point label cloud `Y`;
> * `L^q` rank-`q` completions
>   \[
>       Q_{t_1,...,t_q}=\{x_{1,t_1},...,x_{q,t_q}\};        \tag{15}
>   \]
>
> such that:
>
> 1. `F union Q_t union {y}` is ordinary for every `t` and every
>    `y in Y`;
> 2. `F union Q_t union Q_u` is nonconvex whenever `t!=u`;
> 3. every `X_j` is in convex position;
> 4. the bad pairs in item 2 have witnesses from a set of only
>    `q binom(L,2)` four-circuits; and
> 5. the trace clutter on `W=union_j X_j` has transversal number at least
>    `q(L-1)`.

**Construction and proof.**  Start with a strictly convex polygon `F`
having `2q+3` vertices.  Select `q+1` pairwise nonadjacent boundary edges.
The first `q` are active and the last is reserved for `Y`.

Normalize one selected edge to

\[
                         b=(-1,0),\qquad c=(1,0),            \tag{16}
\]

with the polygon locally above it.  Fix a large integer `K`.  For
`t=1,...,L`, put

\[
 \ell_t={1\over K+t},\quad r_t={1\over K+2t},\quad
 s_t={\ell_t-r_t\over\ell_t+r_t},\quad
 h_t={2\over\ell_t+r_t},\quad
 x_t=(s_t,-\delta h_t),                                    \tag{17}
\]

where `delta>0` is sufficiently small.  Apply an affine copy of this chain
in every active ear.  Put an analogous `D`-point chain in the reserved
ear.

The standard tangent coordinates are

\[
 L(x)={1+s\over -y},\qquad R(x)={1-s\over -y}.              \tag{18}
\]

Up to the common factor `1/delta`, they equal `ell_t,r_t`.  Both decrease
strictly with `t`; hence for `t<u`,

\[
                  x_t\in\operatorname{int}\operatorname{conv}
                            \{b,c,x_u\}.                    \tag{19}
\]

Thus two points from one active chain make the four-set
`{b,c,x_t,x_u}` nonconvex.  On the other hand, insertions in pairwise
nonadjacent sufficiently small ear pockets commute, so any choice of at
most one point per selected edge keeps the whole set convex.  This proves
items 1--2.

The chain itself lies on the strictly concave graph

\[
             y=-\delta K{1-s^2\over1-3s},\qquad 0<s<1/3,   \tag{20}
\]

because the second derivative of the expression without `-delta K` is
`16/(1-3s)^3>0`.  Hence all chain points are vertices of their convex
hull, proving item 3.

For every unordered pair in `X_j`, equation (19) gives the circuit formed
with the two endpoints of the `j`th base edge.  The first coordinate at
which two words `t,u` differ supplies one of these circuits, proving item
4.  Consequently the trace clutter contains a complete graph on each
`X_j`.  A transversal of a complete graph on `L` vertices has size
`L-1`; the clouds are disjoint, which proves item 5.

All inequalities used above are strict.  Choosing sufficiently small
rational `delta`, followed if necessary by a generic rational perturbation
inside the same open order-type cells, gives general position.  QED.

There is also a completely explicit rational realization used by the
verifier.  Take

\[
                  F=\{(j,j^2):0\le j<2q+3\},               \tag{21}
\]

use the lower-hull edges with indices `0,2,...,2q`, and map (16)--(17)
affinely into those ears.  A sufficiently small rational `delta` satisfies
all the preceding conditions.

## 5. Quantitative meaning of the regression

Set `L=D` and `q=floor(beta log D)` in Proposition 4.  Then

\[
 |\mathcal Q|=D^q=2^{(\beta+o(1))(\log D)^2},\qquad
 |P|=(q+1)D+O(q).                                          \tag{22}
\]

Thus the example has exactly the quadratic source entropy and logarithmic
completion rank of the live residue.  Its compatibility graph is empty,
its circuit palette (2) is only `D^(2+o(1))`, and its minimum joined-shield
guard has linear size `q(D-1)`.

Nevertheless any one `X_j` gives the unrestricted bank

\[
                         V(P)\ge2^D,                        \tag{23}
\]

which dwarfs `D^2|\mathcal Q|`.  Therefore Proposition 4 is not a
counterexample to EIC' or to the desired fixed-power saving.  It is a
counterexample to completing the proof using only the common-base joined
complex or the number/matching structure of crossing circuits.

There is a second, more relevant payment.  The follow-up
`DETACHED_SHIELD_TWO_ENDED_PRODUCT.md` proves that every cyclic gap in this
explicit model has a `2+1+...+1+2` bank of size
`binom(L,2)^2L^(q-2)`.  At `L=D` it pays the complete record family with
asymptotic congestion four.  That theorem also explains why replacing the
local chains by arbitrary projective-universal order types is not automatic:
universality preserves nesting but may destroy the compatible cyclic
endpoint profiles.

The rigorous remaining target is consequently sharper than before:

> **Detached-shield extraction target.**  Sum over the circuit-container
> descent so that a repeatedly used one-pocket chain is charged to its
> unrestricted Boolean face bank, even though those chain faces erase the
> common base and are reused across other completion cells.

That is the same global nonlocal-bank issue isolated by the sparse
guard-pair example, now realized inside the exact almost-pairwise-
incompatible completion residue.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_pairwise_incompatible_completion_regression.py
```

The checker constructs the rational parabola-ear configurations with exact
fractions, verifies general position, all completion and extension faces,
all pairwise incompatibilities, the detached convex chain shields, the
`q binom(L,2)` witness palette, and the trace matching/transversal numbers.
It also audits the graph thinning and rank-one descent identities.
