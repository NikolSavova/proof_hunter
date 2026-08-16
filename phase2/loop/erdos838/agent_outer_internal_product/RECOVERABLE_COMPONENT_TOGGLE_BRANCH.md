# Recoverable root-deleted circuit components give an exact toggle product

**Date:** 2026-08-14.  All logarithms are base two and the empty convex
subset is counted.

## Verdict

There is an exact positive branch beyond outer-trace matching.  Delete one
label of the marked root, and suppose the residual cross-circuit system
splits into **private, recoverably described cells**.  A cell may then be put
in its outer source state or replaced by an arbitrary convex face of its
internal subpocket.  Choices in different cells multiply, every resulting
set is an ordinary convex face, and the original weighted source context is
recoverable.

For a family `mathscr J` of weighted marked incidences `(A,T)`, the resulting
exact inequality is

\[
 \boxed{
   \sum_{(A,T)\in\mathscr J}M(A,T)
       \le n{R\choose2}K\,V(P),}                            \tag{1}
\]

where `K` is the number of allowed cell descriptions per root, `R` is maximum
face rank, and

\[
 M(A,T)=
 \prod_{j:O_j\ne\varnothing}(1+V(X_j))
 \prod_{j:O_j=\varnothing}V(X_j).                           \tag{2}
\]

Here `O_j` is the outer side and `X_j` the internal side of cell `j`.  Thus:

* two pure internal components give the full product `V(X_1)V(X_2)`;
* `k` nonempty mixed singleton cells give the toggle bank `3^k`;
* if `|mathscr J|>=beta V`, any uniform lower bound `M` yields

\[
                     \beta M\le n{R\choose2}K.              \tag{3}
\]

Consequently two large private subpockets immediately give much more than a
fixed-power gain.  The theorem retains the actual marked root and loses only
one missing-root label, one retained root edge, and the description index.

The hypothesis cannot be inferred from the internal order type of `X_T`.
The common-cage regression is projectively universal: an arbitrarily scaled
copy of **any** general-position child can be placed in its common disk.  All
outer shields still form circuits with every child label, so after root
deletion the external circuit graph can join every internal component into
one giant mixed cell.  Thus internal order-type diversity alone is circular;
the genuinely new datum is shield-specific privacy or alternation.

This theorem is conditional and does not close EIC'.  It precisely identifies
the strongest positive component branch and why the current matched-shield
obstruction does not automatically enter it.

## 1. Recoverable private-cell profile

Fix a marked incidence `(A,T)` from
`WEIGHTED_ROOT_STAR_MINIMIZER_OBSTRUCTION.md`.  Thus `T` is a canonical triple
of the convex source `A`, and its deterministic role-pocket `X_T` is disjoint
from `A`.

A **root-deleted private-cell description** consists of:

1. a distinguished root label `z in T`, leaving the retained edge
   `e=T setminus {z}`;
2. pairwise disjoint outer blocks
   `O_1,...,O_k subseteq A setminus T`;
3. pairwise disjoint nonempty internal blocks
   `X_1,...,X_k subseteq X_T`;
4. the following circuit privacy condition.  Put

\[
 B=A\setminus\left(\{z\}\cup\bigcup_jO_j\right),\qquad
 U=B\cup\bigcup_j(O_j\cup X_j).                             \tag{4}
\]

Every bad four-circuit in `U` which meets an internal block is contained in
`O_j union X_j` for one index `j`.

The description is **`K`-recoverable** if, for each root `T`, it belongs to a
fixed decoder list of at most `K` labelled block systems.  The list depends
on `P` and `T`, but not on the unknown source face.

The privacy condition has a concrete component interpretation.  In the
bad-circuit co-occurrence hypergraph after deleting `z`, every used internal
block and its possible outer partners form their own component; there is no
circuit joining it to the retained base or to a different used block.  Pure
internal cells have `O_j=emptyset`.

## 2. Local toggle lemma

> **Lemma 1 (private components multiply).**  Given a description above,
> form a set `C` by independently making the following choice in each cell:
>
> * if `O_j` is nonempty, choose either the complete outer state `O_j` or an
>   arbitrary convex face `F_j subseteq X_j`;
> * if `O_j` is empty, choose an arbitrary convex face `F_j subseteq X_j`.
>
> Adjoin every chosen state to the retained base `B`.  Then `C` is convex,
> and the number of choices is exactly (2).

**Proof.**  Suppose `C` were nonconvex.  Planar Caratheodory gives a bad
four-subset `Q subseteq C`.  If `Q` meets no internal block, then it is a
subset of `A setminus {z}`, which is convex.  Otherwise privacy puts `Q`
inside one cell `O_j union X_j`.  The selected state in that cell is either
the outer set `O_j`, a subset of the convex source `A`, or a convex face
`F_j` of `X_j`.  Neither contains a bad circuit, a contradiction.

For a mixed cell, the outer state is nonempty and disjoint from every internal
state, including the empty face, so its `1+V(X_j)` states are distinct.  Pure
cells have exactly `V(X_j)` states.  Label-disjointness makes the product map
injective.  QED.

Notice that the condition is stated only in terms of bad four-circuits.  It
does not assume the desired convex unions.

## 3. Global source recovery

> **Theorem 2 (recoverable component toggle).**  Equation (1) holds for any
> collection of marked incidences equipped with `K`-recoverable private-cell
> descriptions.

**Proof.**  Output every ordinary face `C` from Lemma 1.  It contains the
retained root edge `e`.  To decode a record from `C`:

1. choose `e subseteq C` and the missing root label `z`, costing at most
   `n binom(R,2)` possibilities and determining `T`;
2. choose one of the at most `K` cell descriptions for `T`;
3. in each mixed cell, the outer state is recognized by
   `O_j subseteq C`; otherwise its internal face is `C cap X_j`.

All pure internal faces are also `C cap X_j`.  Remove these internal labels,
restore `z`, and restore `O_j` precisely in the mixed cells which used an
internal state.  This uniquely reconstructs `A`.  Hence every output has at
most `n binom(R,2)K` preimages.  Summing the exact local bank sizes proves
(1).  QED.

The theorem preserves the source multiplicity `w(T)`: common roots and
diffuse roots are both absorbed by the decoder, with no division by the
number of source faces.

## 4. Quantitative positive branches

Assume `|mathscr J|>=beta V`.

### Two private subpockets

If every incidence has two pure cells with

\[
                         V(X_1)V(X_2)\ge H_1H_2,             \tag{5}
\]

then (1) gives

\[
                         \beta H_1H_2
                         \le n{R\choose2}K.                 \tag{6}
\]

Thus a branch with `beta H_1H_2>n binom(R,2)K` cannot occur in a minimizer;
the constructed ordinary-face bank already exceeds `V`.  More generally the
bank gives a factor

\[
                 {\beta H_1H_2\over n\binom R2K}            \tag{7}
\]

over the ambient source count.  If this ratio is at least `n^eta`, it is the
requested fixed-power EIC' gain.

For subpockets of polynomial size and any reservoir bound
`f(s)>=2^{c(log s)^2-o((log s)^2)}`, the numerator in (7) is
quasipolynomially larger than the decoder loss whenever `log K=o((log n)^2)`.

### Private singleton toggles

If there are `k` mixed cells with `X_j={x_j}`, then `V(X_j)=2` and

\[
                              M(A,T)\ge3^k.                  \tag{8}
\]

This is an exact toggle theorem.  It yields a fixed-power gain once

\[
 k\log 3\ge(1+\eta)\log n+2\log R+\log(K/\beta).            \tag{9}
\]

The matching supplied by `GLOBAL_MARKED_POCKET_RELEASE.md` is only a matching
of outer traces and does not imply these private singleton cells.  Moreover,
at its currently guaranteed constant in front of `log n`, (9) would still
not pay even the missing-root decoder.  Large internal reservoirs are the
quantitatively stronger branch.

## 5. Universality barrier

The construction in `DISJOINT_SHIELD_COMMON_POCKET_REGRESSION.md` did not
need a convex pocket for its circuit rectangle.  Let `Q` be any finite planar
general-position configuration.  Apply a sufficiently small positive
similarity and a generic translation so that its image lies inside the common
disk `D`.  This preserves the order type and all convex faces of `Q`.  Strict
containment in every transversal shield triangle is open, and the finitely
many outer--inner collinearities are avoided generically.

For the resulting copy `X` one still has

\[
 N(T)=X,qquad S_i\cup\{x\}\text{ bad for every }i,x.        \tag{10}
\]

For `q>=2`, the complete transversal version of (10) consequently puts every
surviving core shield vertex and every child label in one connected component
of the root-deleted external bad-circuit co-occurrence hypergraph.  This
remains true whether `Q` is convex, has very few faces, or has rich internal
circuit structure.  Thus no invariant of the induced order type `P|X_T`
alone can force the private-cell hypothesis.  One needs an external incidence
condition: private neighborhoods, low codegree between cells, or geometric
alternation which actually separates their shields.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_recoverable_component_toggle.py
```

The exact rational checker builds a weighted positive instance.  Its marked
root encloses a pocket on one arc of a convex oval, while optional source
vertices lie on the opposite arc.  Deleting one root vertex makes the source
residue and both pocket blocks a convex-position set, so the circuit privacy
condition holds.  It audits every source and every two-block state, verifies
the decoder, and checks the exact product count.
