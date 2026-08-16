# Detached shields: a cyclic two-ended product theorem

**Date:** 2026-08-14.  All logarithms are base two.  This note answers the
local detached-shield question raised by
`PAIRWISE_INCOMPATIBLE_COMPLETION_REGRESSION.md`.

## Verdict

The explicit nested-ear product regression is not merely paid by the
Boolean face bank of its local convex chains.  It has an exact
**two-ended product bank**.  The counting uses only endpoint pairs once a
cyclic strong-separation law is available; that separation law itself is a
real geometric hypothesis and is not preserved by an arbitrary
projective-universal replacement of the local chains.

Let `X_1,...,X_q` be cyclically separated containers of sizes `L_i>=2`.
For every cyclic gap, take two labels in each adjacent endpoint container
and one label in every other container.  All these sets are ordinary.  If
`M` rank-`q` completions draw one label from every container, then

\[
                         V(P)\ge {1\over16}M^{1+2/q}.        \tag{1}
\]

Thus `D^2M` records satisfy the desired fixed-power estimate whenever

\[
                         M^{2/q}\ge16D^{1+\epsilon}.         \tag{2}
\]

For the uniform nested-ear product `M=L^q`, the sharper exact bank gives

\[
          V(P)\ge { (L-1)^2\over4}M,qquad
          D^2M\le {4D^2\over(L-1)^2}V(P).                   \tag{3}
\]

At `L=D`, the explicit quadratic-entropy regression pays with asymptotic
congestion four.

There is a profile-strengthened cyclic identity.  If a gap bank uses a
right endpoint family of size `R_i` in `X_i` and a left endpoint family of
size `A_(i+1)` in `X_(i+1)`, then

\[
 \max_i {|\mathcal B_i|\over\prod_jL_j}
 \ge
 \left(\prod_i{A_iR_i\over L_i^2}\right)^{1/q}.             \tag{4}
\]

This is the requested decision-tree/Kraft analogue: the cyclic shift in
the endpoint products cancels after multiplication, so cap/cup mass cannot
anti-align at every cut.

The theorem does not finish the arbitrary completion family.  What remains
is a **localization and global recovery** problem: show that a
quadratic-entropy pairwise-incompatible family either admits such a cyclic
container coordinate on a fixed-power fraction of its mass, or releases a
one-pocket shield whose erased container identity is paid across all common
bases.  Neither pairwise incompatibility nor the sunflower theorem alone
provides this coordinate system.

For cyclic cells there is nevertheless an exact global hybrid: pair
the detached bank with the base-retaining source-face bank.  If their global
overlaps are `Lambda_det,Lambda_src`, recoverable-cell Cauchy closes whenever

\[
       M_0^{2/q}\ge16\Lambda_{\rm det}\Lambda_{\rm src}
                         D^{1+2\epsilon}.                    \tag{G}
\]

where every cell has at least `M_0` completions.

## 1. Cyclic two-ended separation

Call disjoint label sets `X_1,...,X_q` **cyclically two-ended separated** if,
for every `i` modulo `q`, every set

\[
 A\cup B\cup\{x_k:k\ne i,i+1\},\qquad
 A\in{X_i\choose2},\quad B\in{X_{i+1}\choose2},
 \quad x_k\in X_k,                                         \tag{5}
\]

is in convex position.

This is the elementary boundary law of a cyclic strong-glue blow-up.  Cut
the macro convex cycle at the gap `(i,i+1)` and apply a projective
normalization sending that gap to infinity.  The blocks occur in a
sequential strong-glue order.  A two-set is simultaneously a cap and a cup,
so the standard cap-first/cup-last hull argument keeps both endpoint pairs
and every intermediate singleton.  Projective inversion gives (5).

The last condition is load-bearing.  A projective-universal strict nesting
chain can carry an arbitrary internal order type.  Shrinking it preserves
cross-block orientations, but does not guarantee that the rooted endpoint
profile required at *both* neighboring cyclic cuts is the full family of
two-sets.  Thus cyclic separation must be proved for the localized child;
it cannot be inferred from nesting alone.

## 2. Exact elementary product bank

Let `\mathcal Q` be any family of `M` distinct transversals

\[
                      Q=\{x_1,...,x_q\},\qquad x_i\in X_i.  \tag{6}
\]

It need not be the complete Cartesian product.  Put `L_i=|X_i|` and
`P_0=product_i L_i`; necessarily `M<=P_0`.

For a cyclic gap `i`, let `\mathcal B_i` be the bank in (5).  The container
partition recovers every choice, so

\[
 |\mathcal B_i|
   ={L_i\choose2}{L_{i+1}\choose2}
       \prod_{k\ne i,i+1}L_k
   ={(L_i-1)(L_{i+1}-1)\over4}P_0.                          \tag{7}
\]

> **Theorem 1 (cyclic two-ended product bank).**
> \[
>   \max_i|\mathcal B_i|
>       \ge {1\over16}P_0^{1+2/q}
>       \ge {1\over16}M^{1+2/q}.                            \tag{8}
> \]
> Consequently (2) implies
> `D^2M<=D^(1-epsilon)V(P)`.

**Proof.**  Since `L_i>=2`, `L_i-1>=L_i/2`.  Around the cycle,

\[
 \prod_i (L_i-1)(L_{i+1}-1)
       =\left(\prod_i(L_i-1)\right)^2
       \ge {P_0^2\over4^q}.                                 \tag{9}
\]

Some adjacent product is therefore at least `P_0^(2/q)/4`.
Substitute this in (7) to get the first inequality in (8); the second uses
`P_0>=M`.  Now

\[
 D^2M\le16D^2M^{-2/q}V(P),                                 \tag{10}
\]

and (2) turns the multiplier into `D^(1-epsilon)`.  QED.

For `L_i=L` and the complete product, (7) is exactly (3).  Notice that the
extra `L^2` comes from the two endpoint **pairs**, not from the number of
circuits and not from a full local Boolean cube.

There is a useful entropy form.  If

\[
       \log M\ge a(\log D)^2,qquad q\le\beta\log D,         \tag{11}
\]

then

\[
                         M^{2/q}\ge D^{2a/\beta}.            \tag{12}
\]

Thus every cyclically separated hard cell closes with any
`epsilon<2a/beta-1`, whenever `2a>beta`.  This exposes the exact coefficient
threshold rather than hiding it in an `O(log D)` rank.

## 3. The cyclic endpoint-profile/Kraft identity

The pair bank is the minimum profile version of a more general fact.
Suppose a gap `i` admits endpoint families

\[
          \mathcal R_i\subseteq\mathcal F(X_i),\qquad
          \mathcal A_{i+1}\subseteq\mathcal F(X_{i+1}),     \tag{13}
\]

of sizes `R_i,A_(i+1)`, and every union of one member of each family with
one arbitrary point from every other container is ordinary.  Assume the
container traces make these choices recoverable.  Then

\[
             |\mathcal B_i|=R_iA_{i+1}
                             \prod_{k\ne i,i+1}L_k.          \tag{14}
\]

> **Theorem 2 (cyclic profile alignment).**
> \[
> \max_i {|\mathcal B_i|\over P_0}
>   \ge\left(\prod_i{A_iR_i\over L_i^2}\right)^{1/q}.       \tag{15}
> \]

**Proof.**  Normalize (14):

\[
             {|\mathcal B_i|\over P_0}
                   ={R_i\over L_i}{A_{i+1}\over L_{i+1}}.   \tag{16}
\]

Multiplying (16) over all cyclic gaps gives

\[
 \prod_i {|\mathcal B_i|\over P_0}
       =\prod_i{A_iR_i\over L_i^2}.                         \tag{17}
\]

The maximum is at least the geometric mean.  QED.

For a fixed generic direction, every convex subset of `X_i` is determined
by its upper and lower hull chains.  Hence its cap/cup endpoint counts obey

\[
                            A_iR_i\ge V(X_i).                \tag{18}
\]

If the two rooted profiles in (18) are precisely the profiles compatible at
the two adjacent cyclic cuts, (15) turns the product of the local
unrestricted reservoirs into one large two-ended global bank.  The cyclic
identity is load-bearing: in a merely linear strong-glue order there is only
the endpoint product `R_1A_q`, which can be anti-aligned while every
`A_iR_i` is large.

## 4. Application to the nested-ear regression

In Proposition 4 of the preceding report, take the active chains as the
containers.  Exact rational orientation checks give (5) for every cyclic
gap.  Therefore the completion family of size `L^q` has, independently of
the common base and extension labels, the bank

\[
                         {L\choose2}^2L^{q-2}.               \tag{19}
\]

With `L=D`, this is `(1-o(1))D^2M/4`, proving (3).  Hence that
quadratic-entropy pairwise-incompatible family is fully discharged locally.

Projective universality does show why the statement cannot be extended by
simply replacing “cyclically separated” with “strictly nested in every
container.”  The latter condition leaves the endpoint profiles arbitrary.
Theorem 2 remains applicable if those actual rooted profiles can be proved
compatible across all cuts, but that is additional geometry.

## 5. Full face recurrence for universal-chain wrappers

There is an exact audit of the proposed construction pivot.  Put arbitrary
blocks `X_1,...,X_q` in one **linear** sequential strong-glue order.  Let
`W_i,C_i,U_i` be their nonempty convex, cap, and cup counts, and let
`L_i=|X_i|`.  Classifying a face by its first and last occupied blocks gives

\[
 W=\sum_iW_i+
   \sum_{i<j}C_iU_j\prod_{i<k<j}(1+L_k).                    \tag{20}
\]

Indeed, a multi-block face has a cap in its first block, a cup in its last,
and at most one point in every intermediate block; the standard hull
argument proves the converse.  This is an equality, not just a bank lower
bound.

For every block, the upper/lower hull map injects its convex faces into a
cap--cup pair, so

\[
                             C_iU_i\ge W_i.                  \tag{21}
\]

If the `q` blocks are identical and equally oriented, the full-span term in
(20) gives

\[
                 W\ge C_1U_q(1+L)^{q-2}
                    =CU(1+L)^{q-2}
                    \ge W_{\rm child}(1+L)^{q-2}.           \tag{22}
\]

Write `d=log L`, `log W_child=(c+o(1))d^2`, and
`q=(kappa+o(1))d`.  Since the final size is `qL` and
`log(qL)=d+o(d)`, (22) has coefficient at least `c+kappa`.
Thus identical universal-chain wrappers make the coefficient worse.

Heterogeneous orientation can anti-align `C_i` and `U_j` and suppress the
full-span term.  It still cannot improve a known child coefficient: every
`X_i` is an induced subset, so

\[
                            W\ge\max_iW_i.                   \tag{23}
\]

For `q=O(log L)`, replacing an `L`-point coefficient-`1/2` child by `q`
such blocks changes its logarithmic size only by `o(log L)` and therefore
retains coefficient at least `1/2`.  Projective universality preserves the
entire child face profile.  Consequently the suggested radial/nonadjacent
wrapper is not a sub-half construction unless one already supplies a
growing sub-half child family; in that form the construction is circular.

This is the exact cap/cup anti-alignment barrier.  Formula (20) permits
anti-alignment in a heterogeneous linear order, while Theorem 2 shows that
a genuinely compatible cyclic family of cuts would eliminate it by the
multiplicative identity (17).

## 6. Exact global residue

Theorem 1 needs actual containers with three properties:

1. every completion selects one label from each container;
2. the container cycle is recoverable from the bank face; and
3. the two-ended unions (5) are ordinary at every cyclic cut.

The pairwise-incompatible/sunflower reductions in the preceding report do
not establish these.  A sunflower gives disjoint **petals**, but one petal
may contain a long, projectively universal one-pocket history rather than
one atom from each of many separated pockets.  Across varying common bases,
the same untagged container bank can also be reused by many cells.

Consequently the surviving theorem is now:

> **Recoverable cyclic-container target.**  A quadratic-entropy
> pairwise-incompatible completion family either has a fixed-power-mass
> cyclic two-ended coordinate satisfying Theorem 1, or has a one-pocket
> child whose unrestricted reservoir can be summed globally without paying
> the erased common-base multiplicity.

The first branch is proved here, with the exact entropy threshold (12).  The
second branch is the nonlocal detached-shield overlap problem; no local
cap/cup, circuit-color, or transversal assertion resolves it.

## 7. Global recoverable-cell splice

Now allow many common-base cells `c`.  Cell `c` contains `M_c` distinct
completions, each with `D` one-point extension labels, and carries `D^2M_c`
records.  Its base-retaining source bank is

\[
 \mathcal S_c=\{F_c\cup Q\cup\{y\}:
                 Q\in\mathcal Q_c,\ y\in Y_Q\},\qquad
 |\mathcal S_c|=DM_c.                                      \tag{24}
\]

Assume the cell also has a cyclic separated-container representation, and
let `\mathcal D_c` be its largest two-ended bank.  Theorem 1 gives

\[
                         |\mathcal D_c|\ge {M_c^{1+2/q}\over16}.
                                                                    \tag{25}
\]

Let `Lambda_src,Lambda_det` be the maximum global overlaps of these two
bank systems.

> **Theorem 3 (global source/detached Cauchy).**  If `M_c>=M_0` for every
> cell, then
> \[
> \sum_cD^2M_c
>   \le4D^{3/2}M_0^{-1/q}
>       \sqrt{\Lambda_{\rm src}\Lambda_{\rm det}}\,V(P).    \tag{26}
> \]
> In particular, condition `(G)` implies
> \[
>                   \sum_cD^2M_c\le D^{1-\epsilon}V(P).     \tag{27}
> \]

**Proof.**  In one cell, (24)--(25) give

\[
 (D^2M_c)^2
   \le {16D^3\over M_c^{2/q}}
                 |\mathcal S_c||\mathcal D_c|
   \le {16D^3\over M_0^{2/q}}
                 |\mathcal S_c||\mathcal D_c|.              \tag{28}
\]

Sum square roots and apply Cauchy--Schwarz together with

\[
 \sum_c|\mathcal S_c|\le\Lambda_{\rm src}V(P),\qquad
 \sum_c|\mathcal D_c|\le\Lambda_{\rm det}V(P).             \tag{29}
\]

This proves (26), and `(G)` gives (27).  QED.

If the completion decomposition is canonical and the cells partition the
actual source faces, then `Lambda_src=1`.  In that common situation the
only remaining capacity parameter in `(G)` is the overlap of the detached
two-ended banks.

Theorem 3 is genuinely global: the detached faces may erase the common
base, provided their overlap is compensated by recovery in the source
bank.  Failure has a precise meaning--the product of source/base reuse and
detached-container reuse exceeds the threshold in `(G)`.  Separate maximum
overlaps still need not align on one subfamily, as shown by the two-star
barrier in `COMMON_BASE_COMPLETION_SHADOW.md`; an extraction theorem must
use weighted/codegree information, not merely select both maxima.

## 8. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_detached_shield_two_ended_product.py
```

The checker exhausts every cyclic gap in the rational nested-ear models,
verifies all `2+1+...+1+2` faces, checks the exact bank cardinalities, and
audits (8), (15), the uniform `L=D` record inequality, and 117 exact
finite instances of the full strong-glue recurrence (20), together with
the cleared-denominator form of (26).
