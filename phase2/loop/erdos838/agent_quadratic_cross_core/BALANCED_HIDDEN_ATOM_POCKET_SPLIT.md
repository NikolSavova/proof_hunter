# Balanced hidden fibres: a common-face pocket split

**Date:** 2026-08-14  
**Status:** exact local theorem.  This proves the geometric half of the
balanced hidden-fibre atom after localization to a common convex base.  It
does not assert that the resulting contextual bases have small overlap at
later recursive levels.

## 1. Verdict

There is a simple way to avoid the fatal `2^q` split ambiguity noted after
the balanced entropy rectangle theorem.  Do not output the bare union of two
residual sets.  Relative to their common convex base, first put each residual
in its canonical tangent pocket.  Two nonadjacent pockets coexist, and the
two directed tangent chords then recover the two factors from the output.

Completion multiplicity is not silently discarded.  It is aggregated as a
weight on the rooted pocket atom.  If that weight is polynomial, the
two-ended output has polynomial global overlap.  If it is not polynomial,
fixing the atom leaves a contextual completion family of free rank at most
half the parent rank.  A second obstruction, concentration in three
consecutive pockets, also gives a rooted rank-half child.  Thus the exact
common-base alternative is

\[
 \boxed{\text{polynomial-overlap separated-pocket bank, or a
 polynomial-loss contextual rank-half descent.}}               \tag{1}
\]

This is precisely the local alternative needed in Section 6 of
`COMMON_ROOT_FAN_SUM.md`.  The remaining global issue is stated in Section
6 below.

All weights below are nonnegative integers.  The same proof works for
nonnegative real weights.

## 2. Canonical pocket atoms

Let

\[
                 F=(a_0,\ldots,a_{m-1})                         \tag{2}
\]

be a counterclockwise convex polygon in a planar general-position set.  Its
edge pocket `R_i(F)` consists of the points which violate precisely the
support inequality of the directed edge `a_i a_(i+1)`.

Consider a weighted occurrence `omega` carrying a nonempty set `C_omega`
of at most `k` new points such that

\[
                     F\cup C_\omega\quad\hbox{is convex}.       \tag{3}
\]

The occurrence may also carry a blocker, the opposite half of a hidden
interval, and an outer tangent history.  These are called its **completion
data** and are not assumed to be recoverable from `C_omega`.

Every `x in C_omega` is individually addable to `F`, because
`F+x` is a subset of the convex-position set (3).  An individually addable
point sees exactly one edge of `F`: seeing two consecutive edges would hide
their common old vertex.  Hence `x` lies in a unique pocket.  Put

\[
             C_{\omega,i}=C_\omega\cap R_i(F).                  \tag{4}
\]

Every nonempty `C_{omega,i}` is a rooted convex chain, since
`F union C_(omega,i)` is again a subset of (3).  Choose one nonempty
component canonically, for example by maximum size and then the first cyclic
edge, and write

\[
        \alpha(\omega)=(F,i,Q),\qquad Q=C_{\omega,i}.           \tag{5}

For an atom `alpha=(F,i,Q)`, let

\[
        \beta_\alpha=\sum_{\omega:\alpha(\omega)=\alpha}w_\omega
                                                                    \tag{6}
\]

be its full completion/blocker multiplicity.  Thus

\[
                   \sum_\alpha\beta_\alpha=W                  \tag{7}
\]

exactly.  This is the mass-preserving contextual projection; no completion
fibre has been replaced by an unrecorded ambient tag.

If `F` has fewer than three vertices, or if no new component exists, the
whole occurrence is already declared a contextual child.  Its free rank is
at most `k`; the nontrivial case is therefore (2)--(5).

## 3. The weighted pocket theorem

Call two edge indices **separated** when they are distinct and not cyclically
adjacent.  Fix a threshold `T>=1` and `0<eta<1`.

> **Theorem 1 (weighted common-face pocket split).**  Suppose every
> occurrence in Section 2 has free rank at most `k`.  At least one of the
> following holds.
>
> 1. **Heavy-completion descent.**  Atoms with `beta_alpha>T` carry total
>    mass at least `W/2`.  Fix each such rooted atom and pass its completion
>    family to the base `F union Q`.  The total passed mass is unchanged,
>    and every child has free rank at most `k-1`.
> 2. **Separated-pocket bank.**  There is a family of ordered pairs of
>    light atoms in separated pockets of total weighted mass at least
>    `eta W^2/4`.  Sending
>    \[
>                    (F,i,Q),(F,j,Q')
>                 \longmapsto F\cup Q\cup Q'                  \tag{8}
>    
>    gives ordinary convex faces.  A target of rank at most `s` receives
>    weighted load less than
>    \[
>                           s^4T^2.                            \tag{9}
>    \]
> 3. **Three-pocket descent.**  Up to three consecutive rooted pocket
>    contexts carry total mass greater than
>    \[
>                         {(1-\eta)W\over2}.                   \tag{10}
>    \]
>    Their atoms, with their exact conditional completion weights, form at
>    most three contextual child families, each of free rank at most `k`.

**Proof.**  Let `H` be the mass on atoms with `beta_alpha>T`.  If
`H>=W/2`, fix `F,i,Q`.  The remaining new points of an occurrence form a
subset of `C_omega-Q`, of size at most `k-|Q|<=k-1`, and

\[
                  (F\cup Q)\cup(C_\omega-Q)                   \tag{11}
\]

is convex.  Carrying the conditional completion law proves alternative 1.

Suppose now that `H<W/2`, and let `S=W-H>W/2`.  For each cyclic pocket put

\[
       p_i=\sum_{\substack{\alpha=(F,i,Q)\\\beta_\alpha\le T}}
                 \beta_\alpha,
 \qquad
       M=\max_i(p_{i-1}+p_i+p_{i+1}).                          \tag{12}
\]

The total weighted mass `B` of ordered separated pairs satisfies

\[
\begin{aligned}
 B&=S^2-\sum_i p_i(p_{i-1}+p_i+p_{i+1})\\
  &\ge S^2-MS=S(S-M).                                         \tag{13}
\end{aligned}
\]

If `B>=eta S^2`, then `B>eta W^2/4`.  The matching-pocket
compatibility theorem says that (8) is convex: each rooted chain separately
replaces one edge of `F`, and the two edges have disjoint endpoint pairs.

It remains to prove recovery.  From a target `U` of rank at most `s`, guess
the two directed old edges `(a_i,a_(i+1))` and `(a_j,a_(j+1))`.  There are
fewer than `s^4` ordered choices.  Once they are fixed, `Q` is exactly the
set of target vertices strictly beyond the first directed support line,
and `Q'` is exactly the analogous set for the second line; the other pocket
chain lies in the retained half-plane because the pockets are nonadjacent.
Then

\[
                         F=U-(Q\cup Q')                         \tag{14}
\]

with the four roots restored, so the atom pair is recovered.  Each light
atom pair represents weighted completion mass at most `T^2`.  This proves
(9) and alternative 2.

Finally, if `B<eta S^2`, (13) gives `M>(1-eta)S`.  The maximizing
three-window therefore carries more than
`(1-eta)W/2`.  Keep the three rooted laws separately, including their
conditional completion weights.  Every selected rooted chain `Q` is a
subset of some `C_omega`, so its free rank is at most `k`.  This proves
alternative 3.  QED.

The proof explains why the bare collision map is quantitatively useless.
For two rank-half residuals, forgetting their split can cost `2^q`.  In
(8), the two tangent chords recover the split with fewer than `s^4`
guesses.  If the omitted completion data still have a large fibre, that
fibre is exactly `beta_alpha`, and the theorem takes the descent branch
instead of pretending that it was decoded.

## 4. Balanced rank and polynomial telescope

In the balanced hidden-fibre split, each prefix or suffix has free rank

\[
                    k\le\left\lceil{q\over2}\right\rceil.      \tag{15}
\]

Take `eta=1/2` and `T=r^C` for a fixed `C`.  The bank branch then has
global weighted overlap at most `r^(2C+4)`.  Either descent branch keeps at
least `W/4` total mass in contextual states of free rank at most
`ceil(q/2)` (and the heavy branch actually keeps at least `W/2`).

Repeating only after a new balanced split has depth at most
`ceil(log_2 r)`.  A factor four at each descent costs

\[
                    4^{\lceil\log_2r\rceil}\le4r^2,            \tag{16}
\]

and a fixed polynomial recovery factor at the terminal spend remains
polynomial.  Thus this local recursion has the required polynomial, not
`r^(Theta(r))`, overhead.

## 5. Interface with the dense prefix--suffix rectangle

The balanced entropy theorem in `COMMON_ROOT_FAN_SUM.md` supplies a weighted
law on compatible prefix--suffix rectangles.  After a collision has been
localized to one common retained face `F`, apply (5)--(7) to either marginal
half law, with all opposite-half choices and blockers included in
`beta_alpha`.

* Light mass dispersed around the tangent cycle gives the recoverable
  forward two-ended bank (8).
* A large completion fibre fixes an actual rooted chain and descends into
  its conditional completion family.
* Cyclic concentration retains three adjacent tangent contexts and descends
  into rooted chains of rank at most half.

No ambient edge or midpoint is pigeonholed.  In the bank branch the output
recovers both tangent edges; in the descent branch their identities are part
of the child contexts, whose total mass is counted rather than replaced by
the number of possible ambient labels.

## 6. Exact residual after this theorem

Theorem 1 settles the **common-base atom**.  Two issues are outside its
hypotheses and must not be hidden in the word “contextual.”

1. An upstream argument must localize the dense rectangle to occurrences
   whose half-chain extensions share an actual convex base `F`, or pass to
   such a base with only polynomial loss.  Pairwise intersections alone do
   not provide a globally fixed base.
2. In the heavy branch the new base is `F union Q`.  The theorem preserves
   mass exactly, but does not prove that many different ancestor bases have
   polynomial overlap when their descendant targets later merge.  This is
   the retained-outer/stacked-pocket obstruction, now isolated from the
   local balanced split.

Consequently this report is a rigorous attack on the requested atom, not a
claim that Erdős 838 is closed.  A scalable counterexample to the local
common-base statement is impossible by Theorem 1; any counterexample to the
full contextual recursion must exploit failure of common-base localization
or merging of different contextual bases.

## 7. Exact verification

Run

```bash
python3 phase2/loop/erdos838/agent_quadratic_cross_core/verify_balanced_hidden_atom_pocket_split.py
```

The verifier exhausts the cyclic inequality (13) on small integer weight
vectors, checks the three alternatives with exact rational arithmetic,
constructs exact rational edge-pocket points around a convex octagon,
checks every nonadjacent two-pocket union by integer orientation predicates,
audits the atom-pair output loads, and checks the polynomial telescope (16).
