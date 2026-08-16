# Marked nested shields: a global Carleson theorem and the common-alphabet barrier

**Date:** 2026-08-14.  All logarithms are base two.  A marked face is a
pair `(p,F)` with `F` an ordinary convex-position face and `p in F`; the
mark is bookkeeping, not an extra geometric object.

## Verdict

Retaining the repair mark gives an exact global theorem, but it stops at a
strictly sharper and realizable obstruction.

Let a weighted repaired-star occurrence `e` have its injective ordinary
star `S_e=Q_e union {p_e}` and a family `H_e` of shield faces containing
the same mark `p_e`, all of rank at most `h`.  Put

\[
 I=\sum_e w_e|\mathcal H_e|,
 \qquad
 d(p,F)=\sum_{e:p_e=p,\ F\in\mathcal H_e}w_e,
 \qquad \Lambda=\max_{p,F}d(p,F).                          \tag{1}
\]

There are at most `hV(P)` marked ordinary faces, so

\[
 \boxed{I=\sum_{p,F}d(p,F)\le \Lambda hV(P).}              \tag{2}
\]

In particular, if every one of `R=DM` injective repair stars has at least
`K` marked shield faces, then

\[
                 V(P)\ge {DMK\over\Lambda h}.              \tag{3}
\]

Thus `K/(Lambda h)>=D^epsilon` supplies exactly the missing fixed-power
gain beyond the free `DM` stars.  This is a genuine global weighted
statement: arbitrary repetition of geometric targets and nonuniform
history weights are already included in `d(p,F)`.

There is also a marked collision upgrade.  If a positive fraction of the
second moment at a common `(p,F)` splices to one ordinary face with load
`L`, then, writing `Delta=sum_e w_e^2<=alpha I` and allowing exceptional
mass `beta I`,

\[
 {I\over V(P)}\le
 {ha+\sqrt{h^2a^2+8hL/\theta}\over2},
 \qquad a=\alpha+{2\beta\over\theta}.                      \tag{4}
\]

Failure of (2)--(4) therefore localizes to one heavy **common marked
shield** `(p,F)` whose source stars are joined by cross-base bad circuits.
This retains the repair mark all the way through the component descent.

The localized obstruction is real.  The radial repair-star clique admits a
common repair alphabet `Y`, and `Y` may be replaced by a projectively
universal, internally arbitrary order type while remaining totally nested
relative every completion root edge.  For its `M` completions:

* all `DM` marked stars `Q union {p}` are distinct, maximal ordinary faces;
* every nontrivial attempted union of a star with a shield face of `Y` is
  nonconvex;
* for every marked shield `(p,F)`, its occurrence overlap is **exactly
  `M`**, even though the mark is retained; and
* the bad-circuit graph of the completion and repair blocks is connected.

Hence no theorem of the form “the repair mark makes unrestricted shield
overlap summable” is true.  The exact final obstruction is a common
alphabet fibre in which the same marked face `(p,F)` repairs all `M`
pairwise-incompatible completions.  A closure theorem must use more than
the mark itself: the source edge/tangent orientation, repair depth, or a
second face carrying completion information.  The construction is not an
EIC' counterexample because its completion and repair blocks have large
other unrestricted banks.

## 1. Weighted marked-face Carleson theorem

Let `mathcal E` be any finite family of histories, with nonnegative weights
`w_e`.  History `e` has a mark `p_e` and supplies a family

\[
 \mathcal H_e\subseteq
   \{F\in\mathcal F(P):p_e\in F,\ |F|\le h\}.              \tag{5}
\]

No compatibility between different histories is assumed.

> **Theorem 1 (marked shield Carleson bound).**  Definitions (1) imply
> (2).  More generally,
> \[
> \sum_{p,F:d(p,F)\ge T}d(p,F)
>       \le {1\over T}\sum_{p,F}d(p,F)^2.                  \tag{6}
> \]

**Proof.**  Double-count weighted incidences:

\[
 \sum_e w_e|\mathcal H_e|=\sum_{p,F}d(p,F).                \tag{7}
\]

A rank-`k` ordinary face has exactly `k` possible contained marks.  Hence
there are at most

\[
            \sum_{F\in\mathcal F(P),\ |F|\le h}|F|
                         \le hV(P)                         \tag{8}

nonempty marked bins `(p,F)`.  Bounding each by `Lambda` proves (2).
On `d>=T`, one has `d<=d^2/T`, which proves (6).  QED.

For the live nested-chain shield, it is important that (5) counts the mark
as an actual vertex.  If the local shield family is uniform of rank `k`
inside a repair alphabet `Y_e`, then summing over all possible repair marks
gives exactly

\[
 \sum_{p\in Y_e}|\{F\in\mathcal H_e:p\in F\}|=k|\mathcal H_e|.
                                                                    \tag{9}
\]

There is no fictitious factor `D`: a rank-`k` shield retains only `k`
marks.  Omitted marks give `(D-k)|mathcal H_e|` incidences, but the ordinary
face no longer records the mark; charging those incidences to `hV(P)` is
invalid.  They require the already-injective star as a second output.

Equation (3) follows from (2) when `|mathcal H_e|>=K`.  It cleanly closes
every mark-diverse branch.  The only failure is a large codegree
`d(p,F)`, which fixes both the repair label and an ordinary shield face.

## 2. Marked collision energy

The mark also improves the collision localization.  Index the marked bins
by `z=(p,F)` and put

\[
 s_z=\sum_{e:z\in\mathcal H_e}w_e,qquad
 I=\sum_zs_z,qquad \Delta=\sum_{e,z\in\mathcal H_e}w_e^2. \tag{10}
\]

Here it is harmless to regard each incidence `(e,z)` as a separate
weighted occurrence; thus `Delta` is its diagonal mass.  Since the number
of bins is at most `hV`, Cauchy gives collision energy

\[
 \mathcal C={1\over2}\left(\sum_zs_z^2-\Delta\right)
       \ge {1\over2}\left({I^2\over hV}-\Delta\right).     \tag{11}

Suppose a collection of good same-bin collision pairs maps to ordinary
faces with total output weight at most `L` per face, and its weight `G`
satisfies

\[
                         G\ge\theta\mathcal C-\beta I,
                  \qquad 0<\theta\le1.                    \tag{12}

Then `G<=LV`.  If `Delta<=alpha I`, substitute (11) into (12), put
`x=I/V`, and obtain

\[
 x^2-h\left(\alpha+{2\beta\over\theta}\right)x
             -{2hL\over\theta}\le0.                      \tag{13}

Solving the quadratic proves (4).

For unit incidences `alpha=1`.  If every collision is good and `beta=0`,

\[
 {I\over V}\le{h+\sqrt{h^2+8hL}\over2}.                  \tag{14}

If (14) fails badly, a positive share of the collision energy remains at
one common `(p,F)` and has no splice output.  Two histories in that bin
have the same actual repair label and the same actual ordinary shield.  As
in the unmarked one-gap theorem, after circuit-transversal release their
bases either splice with `F`, or a bad four-circuit meets both released
base differences.  The circuit-component join identity pays distinct
components exactly.  Thus the strict descendant is one circuit-connected
common-`(p,F)` child, with no loss of the repair mark.

## 3. Why the injective stars do not by themselves multiply the shield

Let the pairwise detached-incompatible completions be `Q_1,...,Q_M`, and
let `p in Y_i` repair `Q_i`.  The stars

\[
                              S_(i,p)=Q_i\cup\{p\}          \tag{15}

are distinct ordinary faces.  Therefore a triple `(i,p,F)`, with `F` an
ordinary shield face, is injectively encoded by the **pair**

\[
                              (S_(i,p),F).                  \tag{16}

This only gives a `V(P)^2` capacity statement.  To use the shield in a
linear `V(P)` bound one needs either bounded overlap of its one-face output,
as in Theorem 1, or an ordinary mixed union/splice.  The next construction
kills both possibilities while retaining the mark.

## 4. Projectively universal common-alphabet barrier

Start with the radial construction of
`agent_outer_internal_product/REPAIR_STAR_CLIQUE_BARRIER.md`.  There are
active blocks `X_0,...,X_(q-1)`, a common repair block `Y`, and

\[
 Q_t=\{x_(0,t_0),...,x_(q-1,t_(q-1))\},
                 \qquad |\mathcal Q|=M=L^q.                \tag{17}
\]

Every transversal `Q_t` is convex and distinct transversals have detached-
incompatible unions.  The repair block lies in the insertion pocket of the
edge between `X_0` and `X_1`.

> **Theorem 2 (marked common-alphabet barrier).**  The block `Y` can have
> any prescribed planar general-position order type, while the realization
> still satisfies:
>
> 1. every `S_(t,p)=Q_t union {p}`, `p in Y`, is convex and all `DM` stars
>    are distinct and maximal;
> 2. `Q_t union {p,p'}` is nonconvex for every `p ne p'` in `Y`;
> 3. for every internal face `F of Y` and `p in F`, the marked shield
>    occurrence `(t,p,F)` maps to `(p,F)` with fibre exactly `M`;
> 4. if `F ne {p}`, then `S_(t,p) union F` is nonconvex; and
> 5. the block bad-circuit graph is connected.

**Proof.**  In tangent coordinates for the repair edge, projectively embed
the prescribed order type with both coordinates increasing in one common
order.  Choose the first-order nesting direction inside the intersection
of the finitely many strict dominance cones determined by the possible
representatives of `X_0,X_1`; encode the arbitrary order type at a smaller
transverse scale.  This is the projective-universality construction from
`DETACHED_RADIAL_LEXICOGRAPHIC_PROFILE.md`, and all the required inequalities
are open.  Consequently every pair of repair labels is totally nested
relative every completion root edge, while the intrinsic order type of
`Y` is unchanged.

One repair label is an exterior insertion, proving the star assertion.
Two repair labels contain the fixed bad circuit made from the two labels
and the selected representatives in `X_0,X_1`, proving item 2.  Detached
incompatibility of the active transversals and the repair circuit make
every star maximal and all stars distinct.

The family `Y` is common to every completion, so a fixed actual `(p,F)` has
one occurrence for each of the `M` choices of `t`; its fibre is exactly
`M`.  If `F ne {p}` it contains a second repair label `p'`, and the circuit
from item 2 is contained in `S_(t,p) union F`, proving item 4.  The active
radial circuits connect the active blocks, and the repair circuits connect
`Y` to `X_0,X_1`, proving item 5.  QED.

Let

\[
 H=V(Y),\qquad J=\sum_{F\in\mathcal F(Y)}|F|.              \tag{18}
\]

Using the full internal shield in every completion gives exactly `MJ`
marked occurrences but only `J` distinct marked outputs.  Thus

\[
                             \Lambda=M                    \tag{19}

in Theorem 1, with equality in the overlap step.  Keeping the mark has not
recovered even one bit of the completion word `t`.  For omitted marks the
same statement holds: `(p,F)` still has `M` histories, but `p` is no longer
present in the ordinary shield output and must be read from the star in
(16).

This is stronger than the unmarked outer-triangle barrier for the present
interface.  It simultaneously has the full `DM` injective star bank, the
live repair mark, an arbitrary unrestricted shield order type, pairwise
detached incompatibility, and circuit connectedness.  What it does not do
is suppress the other radial one-gap banks; those pay the global EIC count.
Accordingly it is an exact obstruction to marked **overlap/mixed-union**
arguments, not a counterexample to EIC'.

## 5. Exact rational audit

The verifier uses the four active two-point blocks of the repair-star
barrier and the following four repair labels:

\[
 \begin{split}
 Y=\{&(0,-16/7),\ (-1/295,-134/59),\\
     &(1/150,-34/15),\ (-3/160,-9/4)\}.                    \tag{20}
 \end{split}
\]

The second point is strictly inside the triangle of the other three, so
`Y` itself is not convex.  Nevertheless it is totally nested relative all
sixteen completion root choices.  Exact enumeration gives

\[
 \begin{array}{c|c}
 M&16\\
 D&4\\
 \text{maximal marked stars}&64\\
 V(Y)&15\\
 J=\sum_F|F|&28\\
 \text{marked occurrences}&MJ=448\\
 \text{load of every }(p,F)&16=M\\
 V(P)&785.
 \end{array}                                               \tag{21}
\]

The full face profile is

\[
             (1,12,66,220,318,168,0,0,0,0,0,0,0).         \tag{22}

There are exactly `64=DM` faces meeting all five blocks.  Every nontrivial
star--shield union fails, and the block circuit graph is connected.

## 6. Exact remaining obstruction

Theorems 1--2 leave a narrower target than `(EIC'o9)`:

> **Common-marked-shield target.**  In one circuit-connected child, fix a
> repair label `p` and a low-rank ordinary shield face `F` containing `p`.
> A quadratic-entropy family of pairwise detached-incompatible completions
> all has the same marked shield occurrence `(p,F)` and one-point star
> `Q union {p}`.  Prove a fixed-power bank using the completion-dependent
> insertion edge/tangent history, or extract a recoverable cyclic component;
> the mark and unrestricted shield alone are insufficient.

The radial barrier realizes this atom but exits through its other cyclic
banks.  Therefore a final theorem may assume the absence of such a
recoverable radial cycle.  The missing information must be a relation
between the common mark `p`, the varying insertion edges of the completions,
and the cross-base circuit witnesses.  Any descent which projects only to
`(p,F)` necessarily pays the sharp multiplicity `M` in (19).

