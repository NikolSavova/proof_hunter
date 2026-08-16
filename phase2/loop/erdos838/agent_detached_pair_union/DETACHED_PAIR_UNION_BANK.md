# Detached pair unions close the nested-ear product residue

**Date:** 2026-08-14.  All logarithms are base two.

## Verdict

The common-base completion attack was testing the wrong union in one
important branch.  A pair of completions can be incompatible **with the
common base retained** while its detached union is an ordinary convex
face.  Detached-compatible pairs give an exact quadratic bank:

\[
        V(P)\ge {E_{\rm det}\over3^{2q}},                    \tag{1}
\]

where `E_det` is the number of ordered rank-`q` completion pairs whose
detached union is convex.  Since the surviving family has quadratic
entropy while `q=O(log D)`, a constant density of detached-compatible
pairs closes the fixed-power estimate immediately.

This completely disposes of the scalable nested-ear product regression.
In that construction every joined pair is nonconvex, but every detached
pair union is convex.  More precisely, for the `M=L^q` word completions,
the coordinatewise union code has load at most `2^q`, and therefore gives

\[
                         {M(M-1)\over2^q}                    \tag{2}

distinct ordinary detached faces.  Thus the regression pays directly by
a recoverable two-ended/product bank; the much larger individual Boolean
chain shields are not needed.

The remaining local family is strictly narrower: after a polynomial
thinning, it is pairwise incompatible even **after the common base is
deleted**.  Every surviving pair then has a four-circuit contained wholly
in the two completions and meeting both symmetric differences.  This is
no longer a base-guard phenomenon.  It is the exact detached circuit
container which a final summed-shield theorem must handle.

## 1. The detached-compatible pair bank

Let `F` be an ordinary face and let `mathcal Q` be `M` distinct rank-`q`
sets disjoint from `F`, with

\[
                             F\cup Q\in F(P)                \tag{3}

for every `Q in mathcal Q`.  In particular each `Q` is an ordinary face by
deletion.  Call an ordered distinct pair `(Q,Q')` detached-compatible if

\[
                              Q\cup Q'\in F(P).              \tag{4}

Let `E_det` be the number of such pairs.

> **Theorem 1 (detached pair-union bank).**
> \[
>                         \boxed{V(P)\ge E_{\rm det}/3^{2q}.} \tag{5}
> \]

**Proof.**  Map `(Q,Q')` to the ordinary face `Q union Q'`.  Given one
output, each of its at most `2q` labels is in `Q-Q'`, in `Q'-Q`, or in
`Q cap Q'`.  Hence it has at most `3^(2q)` ordered descriptions.  QED.

Suppose the family carries `D^2M` records.  The desired bound

\[
                        D^2M\le D^{1-\epsilon}V(P)           \tag{6}

follows whenever

\[
                     E_{\rm det}\ge3^{2q}D^{1+\epsilon}M.   \tag{7}

In the hard branch `M=2^{Omega((log D)^2)}` and `q=O(log D)`, the right
side of (7) is only `M D^O(1)`, whereas a constant fraction of all ordered
pairs is `Theta(M^2)`.

The same pruning used for joined compatibility gives the exact complement.

> **Corollary 2 (detached-incompatible thinning).**  If (7) fails, a
> subfamily of size at least `M/2` has maximum detached-compatible degree
> below
> \[
>                         2\,3^{2q}D^{1+\epsilon}.           \tag{8}
> \]
> It therefore contains a pairwise detached-incompatible subfamily of
> size at least
> \[
>             {M\over2(2\,3^{2q}D^{1+\epsilon}+1)}.         \tag{9}
> \]

**Proof.**  Failure of (7) bounds the average compatible degree by
`3^(2q)D^(1+epsilon)`.  At least half the vertices have degree below twice
that average.  Greedily selecting a vertex and deleting its closed
neighborhood proves (9).  QED.

Only a fixed power of `D` is lost in (9), so quadratic completion entropy
survives.

## 2. The stricter circuit certificate

The detached residual has a stronger four-circuit than the joined one.

> **Lemma 3 (detached first divergence).**  If `Q,Q'` are detached-
> incompatible, some nonconvex four-set `C subset Q union Q'` satisfies
> \[
>          C\cap(Q-Q')\ne\varnothing,
>          \qquad C\cap(Q'-Q)\ne\varnothing.               \tag{10}
> \]

**Proof.**  Planar Caratheodory gives `C subset Q union Q'`.  If it missed
`Q-Q'`, it would lie in the ordinary face `Q'`; the other assertion is
symmetric.  QED.

Thus no common-base label is present in the new witness.  After (9), every
pair in a quadratic-entropy rank-`O(log D)` family has a bad circuit wholly
inside its two completion petals.  Any further circuit-container descent
must extract an unrestricted completion-label shield; deleting tangent
guards from the old base cannot help.

## 3. A coordinate product decoder

There is a sharper decoder when completions choose one label from each of
several disjoint circuit containers.  Let `X_1,...,X_s` be disjoint label
sets, and let

\[
                  \mathcal W\subseteq X_1\times\cdots\times X_s          \tag{11}

be any set of words, viewed as rank-`s` completion faces.

Call the containers **two-point stable** if every set containing at most
two labels from each `X_j` is an ordinary face.  This condition is detached:
no common base is retained.

> **Theorem 4 (recoverable container-product bank).**  For a two-point
> stable system with `M=|mathcal W|`, all detached unions of two words are
> convex, and
> \[
>          \#\{Q_w\cup Q_{w'}:w\ne w'\}
>                         \ge {M(M-1)\over2^s}.              \tag{12}
> \]

**Proof.**  A word pair selects at most two labels from each container, so
its union is a face.  If exactly `h` coordinates contain two different
labels, a fixed coordinate-union word has exactly `2^h<=2^s` ordered
preimages, obtained by assigning the two labels in each differing
coordinate to the first and second word.  QED.

Consequently every such family with

\[
                       M-1\ge2^sD^{1+\epsilon}              \tag{13}

satisfies (6).  At `s=O(log D)`, every quadratic-entropy word family meets
(13) with enormous room.  Notice that no full Cartesian-product assumption
is used in Theorem 4.

## 4. The nested-ear regression is two-point stable

The construction in
`../agent_outer_internal_product/PAIRWISE_INCOMPATIBLE_COMPLETION_REGRESSION.md`
can be chosen with the following strengthening.

> **Proposition 5 (two-point stability of separated ears).**  Let `F` be a
> strictly convex polygon and choose pairwise nonadjacent active edges.
> In sufficiently small exterior insertion neighborhoods of those edges,
> place finite strict nested chains `X_1,...,X_s`.  The neighborhoods may
> be chosen so that:
>
> 1. one point from every active chain joins `F` convexly;
> 2. two points from one chain are incompatible when `F` is retained; and
> 3. every detached selection using at most two points from each chain is
>    in convex position.

**Proof.**  Replace each selected edge by a tiny exterior convex arc.  At
the macro scale the selected nonadjacent edges occur in strict convex
order.  At the micro scale, any chosen pair in one neighborhood is exposed
by the two limiting support directions of that arc.  Strict separation of
the macro support cones leaves a positive margin between every micro
support and every other active neighborhood.  There are finitely many
one- and two-point local choices, so the neighborhoods can be shrunk until
all their support inequalities hold simultaneously.  Inside each
neighborhood choose the tangent coordinates in strict dominance order;
this gives the base-retaining nesting circuit without changing the open
detached support inequalities.  A final generic rational perturbation
preserves all strict conditions.  QED.

This is also visible in the explicit rational parabola-ear model.  The
verifier exhausts all local choices through four active ears and confirms
item 3 exactly.

For the full word family `[L]^q`, Proposition 5 and Theorem 4 give (2).
The joined pair `F union Q_t union Q_u` remains nonconvex at the first
coordinate where the words differ.  Thus joined incompatibility and
detached compatibility occur simultaneously; inferring the latter from
the former was the missing test in the earlier regression analysis.

## 5. Decision-tree interpretation

Theorem 4 is the desired Kraft-type statement for a separated container
tree.  At a leaf pair, every coordinate records either one common symbol or
an unordered two-symbol set.  The number of orientation bits lost is the
Hamming distance, at most the tree depth `s`.  Hence the Kraft load is
`2^s`, not the product of the alphabet sizes.  Quadratic leaf entropy
therefore beats the decoder loss whenever `s=O(log D)`.

For a general circuit decision tree, the exact question is whether the
first-divergence containers can be made two-point stable after discarding
only a fixed-power fraction of the leaves.  If yes, (12) closes the tree.
If no, the failure itself supplies a detached four-circuit between two
containers.  Lemma 3 shows that this circuit no longer involves the common
base, so it must be charged to the unrestricted completion-label face
complex.

## 6. Exact remaining local atom

The nested-ear product and every two-point-stable container system are now
closed.  The sole local residue is:

\[
 \boxed{\begin{array}{c}
 \text{a quadratic-entropy family of rank-}O(\log D)\text{ ordinary faces,}\\
 \text{pairwise nonconvex even after detaching the common base, with every}\\
 \text{four-circuit meeting both symmetric differences.}
 \end{array}}                                               \tag{14}
\]

A final detached-shield theorem must show that such a family has enough
unrestricted ordinary completion-label faces.  This is strictly stronger
input than the earlier joined-incompatibility statement.  Nested homothetic
polygons show that detached-incompatible pairs exist, so the last line is
not vacuous; what remains unproved is a quadratic-entropy family at the
required rank and fixed-power scale.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_detached_pair_union/verify_detached_pair_union.py
```

The checker exhausts the exact rational nested-ear models, verifies all
joined incompatibilities and all detached pair unions, measures the exact
`2^q` decoder load, audits arbitrary word subfamilies, and constructs a
finite detached-incompatible regression to certify that the final branch
is genuine.
