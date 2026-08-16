# Unordered injective colouring removes the quasipolynomial release loss

**Date:** 2026-08-15.  All logarithms are base two.  This sharpens the
entrance of `WEIGHTED_POSITION_RELEASE_ENTROPY.md` for every argument which
does not yet use oriented seam profiles.

## Verdict

The adaptive release entropy decoder, four-local completion theorem, fixed-
label chronology, and role-monotone forest do **not** require source labels
to receive their cyclic positions as colours.  They require only one label
in each of a collection of disjoint physical colour classes.

Let all rank-\(r\) sources contain one fixed root \(T\) of rank \(t\le3\),
and put \(s=r-t\).  Colour the nonroot physical labels independently and
uniformly by \([s]\), retaining a source when its nonroot labels receive
distinct colours.  Some colouring retains weight

\[
 \boxed{
              W\ge {s!\over s^s}W_0\ge e^{-s}W_0.}     \tag{1}
\]

There is no extra root-position factor: the actual root labels are fixed
singleton roles.  With \(s=O(\log n)\), (1) costs only \(2^{O(L)}=n^{O(1)}\),
not \(s^s=2^{\Theta(L\log L)}\).

The one-face adaptive release inequality becomes

\[
 \boxed{
       \mathbb E\sigma(A,F)
          \ge\log W+\log H-\log V(P).}                \tag{2}
\]

On the canonical rank-safe marked slice, fixing the root and rank costs only
a polynomial factor, so (1) gives

\[
                         W\ge V(P)n^{-O(1)},           \tag{3}
\]

and hence

\[
                         \mathbb E\sigma(A,F)
                              \ge\log H-O(L).          \tag{4}
\]

This is an exact improvement over the positional \(O(L\log L)\) loss.
It also preserves the live atom floor: colouring only discards complete
source atoms.

The refinement applies through the all-loop role forest.  The forest's
strictly increasing role order may be any fixed order of the colour classes;
its proof uses only that deletion cannot create a bad four-circuit.  The
four-local and unordered projection theorems already have the same
\(e^{-s}\) colouring cost.

This does **not** close the final rectangle.  A complete unit-weight
\(M_D\times H\) all-deletion core still returns only the \(H\) released
faces, as proved in `LIVE_ATOM_FLOOR_ROLE_FOREST_AUDIT.md`.  The gain removes
a spurious \(n^{\Theta(\log\log n)}\) entrance/description loss; it does not
create a mixed bank.

Nor may (1) be used for an oriented seam/profile theorem.  If a later step
needs the colour order to agree with the cyclic polar order of every source,
one must then fix the permutation of the \(s\) colours, potentially losing
\(s!=2^{\Theta(L\log L)}\).  The exact safe scope of (1) is:

* adaptive guard entropy and its redundancy identity;
* unordered four-local/projection alternatives;
* Hall pruning, fixed-label circuit chronology, and the role forest; and
* every decoder depending only on occupied versus empty colour classes.

The refinement stops immediately before polar local-to-global convexity,
cap/cup seam profiles, or any operation whose statement names the cyclic
position of a colour.

## 1. Weighted injective colouring

Give the distinct sources weights \(0<w_A\le1\), total \(W_0\).  Under a
uniform random colouring of nonroot physical labels by \([s]\), the \(s\)
nonroot labels of a fixed source receive distinct colours with probability

\[
                              {s!\over s^s}.            \tag{5}
\]

Therefore the expected retained weight is \((s!/s^s)W_0\), and a
deterministically first maximizing colouring proves the first inequality in
(1).  The elementary Stirling bound \(s!\ge(s/e)^s\) proves the second.

For a retained source, colour is now its coordinate.  Let
\(X_1,\ldots,X_s\) be the corresponding disjoint colour supports, and add
the labels of \(T\) as singleton roles.  Every retained source occupies
exactly one label in every role.  No common cyclic order is asserted or
needed.

## 2. The entropy decoder is order-free

Let \(F\) range over a pocket face family of size \(H\), disjoint from all
source roles.  For each \((A,F)\), choose any deterministic deletion set
\(G(A,F)\subseteq A\) for which

\[
                         U=(A\setminus G)\cup F        \tag{6}
\]

is ordinary.  The output reveals \(F\), all retained source labels, and the
set \(J\) of empty colour classes.  Given the deleted coordinate values
\(A_J\), it reconstructs the unordered source set \(A\).  Thus

\[
 H(A,F)\le H(U)+H(A_J\mid U)
       \le\log V(P)+\mathbb E\sum_{i\in J}\log|X_i|.  \tag{7}
\]

Since every raw source weight is at most one, \(H(A)\ge\log W\).  Independence
of the pocket choice gives \(H(A,F)=H(A)+\log H\), and (7) proves (2).
Nothing in this decoder refers to the boundary order of \(A\).

The exact redundancy identity likewise remains valid:

\[
 \mathbb E\sigma
    =H(A,F)-H(U)+\mathbb E R_U,                        \tag{8}
\]

where the completion word is indexed by the empty colour roles.

## 3. Live normalization

The rank-safe marking supplies \(\Theta(V(P))\) weight at rank \(O(L)\).
Fixing one actual root and rank costs at most \(n^3O(L)\).  Applying (1)
costs at most \(e^{O(L)}=n^{O(1)}\).  This proves (3), and substitution in
(2) gives (4).

If desired, the source weights may first be dyadically equalized as in
`LIVE_ATOM_FLOOR_ROLE_FOREST_AUDIT.md`; this costs only \(O(L)\) bins and
commutes with colouring because both operations merely restrict sources.

## 4. Why arbitrary role order suffices for the forest

At a bad forest node, choose the smallest colour role participating in a bad
four-circuit.  After deleting its fixed selected label, a later bad circuit
using a smaller surviving role would already have existed before the
deletion, contradicting minimality.  This proof is combinatorial heredity:
the numerical order on colours need not be their geometric cyclic order.

The empty roles in a terminal output recover the increasing colour-role
history.  The forest associated with the actual released trace is
deterministic, so reattaching its selected labels reconstructs the source.
The decoder is unchanged.

By contrast, a statement that a first trace is a cap, a last trace is a cup,
or consecutive polar turns are positive explicitly depends on cyclic order.
Such a statement must pay for or geometrically recover the colour
permutation.  Equation (1) does not waive that later cost.

## 5. Verification

Run

```text
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_unordered_colour_live_release_refinement.py
```

The verifier exhausts all colourings of several weighted set families and
checks the exact \(s!/s^s\) weighted retention average.  It then exhausts
adaptive deletion masks on a retained unordered-colour family and verifies
the entropy decoder and redundancy identity independently of any cyclic
position order.
