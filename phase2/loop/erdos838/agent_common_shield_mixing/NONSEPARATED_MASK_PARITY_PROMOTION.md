# Nonseparated masks: parity promotion removes every root-good cascade

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The predecessor/successor cascade is not the correct hard operation for a
root-admissible replacement.  Every convex singleton word has a canonical
word-dependent fixed-base presentation: choose an independent parity class
of occupied macro cells containing the replacement cell, retain the
complementary selected points as a convex base, and regard the parity-class
points as ears on distinct base edges.  The base varies with the source
word, but it is retained by the output and hence costs no decoder factor.

If `C` is the set of source--profile incidences for which the inserted
profile is an admissible ear on this word-dependent base, then adaptive
omission of the at most two adjacent ears gives

\[
 \boxed{\qquad V(P)\ \ge\ {|C|\over m_g
                   \prod_{h\in N(g)}m_h}\ \ge\ {|C|\over D^3}.\qquad}       \tag{1}
\]

Thus a rich compatible class preserves its full quadratic coefficient.
No nonseparated cascade remains in this branch.

The independent accounting theorem in
`agent_root_followup/MASK_CASCADE_ENTROPY_DICHOTOMY.md` gives the
complementary mask-entropy dichotomy.  In its fixed-mask core, if an
arbitrary repair rule deletes a mask `D(c)` outside the target cell and
turns every one of `M|J|` source--profile pairs into an ordinary face, some
fixed mask `D` satisfies

\[
 \boxed{\qquad V(P)\ \ge\ {M|J|\over
       2^q m_g\prod_{i\in D}m_i}.\qquad}                  \tag{2}
\]

Consequently the repair is already paid unless its erased support entropy

\[
             E(D)=\log m_g+\sum_{i\in D}\log m_i          \tag{3}
\]

is at least `log|J|-O(q+log D)`.  At the balanced parameters
`a=kappa=1/4`, `c_0=1/8`, one has
`log M=(1/4-o(1))d^2` and `log|J|=(1/8-o(1))d^2`; hence an
unpaid cascade must erase at least half of the source entropy.

That threshold is sharp for the operation.  A scalable rational
parabola-cluster construction forces every output containing a fixed
two-point profile and one retained guard on each side to be nonconvex.  Any
cascade must delete a whole side, of entropy
`(1/2-o(1))log M`.  But the profile is already **root-bad** against the
parity base: the same inner point is in the triangle of the outer profile
point and two retained parity anchors.  The exact `R=0`
`{q},{x},{w},{z,y}` obstruction has the same status.  It does not survive
as a root-good cascade.

The remaining atom is therefore narrower than previously stated:

> after a constant-complexity semialgebraic transcript, either a rich jet
> fibre is root-good and (1) closes it, or a retained homogeneous fibre is
> root-bad and every incidence carries a mixed anchored four-circuit.

Producing a globally summable ordinary circuit/shield bank from the latter
fibre is still necessary.  Fixed jets and support redundancy alone do not
perform that release.

## 1. Word-dependent parity bases

Let the occupied macro cells of a source word be cyclically ordered as
`0,...,q-1`, and suppose

\[
                    W=(x_0,\ldots,x_{q-1})                \tag{4}
\]

is in strictly convex cyclic position.  Fix a target cell `g`.  For
`q>=5`, choose an independent set `S` of the cycle containing `g`; for
example, after rotating `g` to zero, take

\[
                 S=\{0,2,\ldots,2(\lfloor q/2\rfloor-1)\}. \tag{5}
\]

Put `A=[q]\S` and

\[
                         B_W=\{x_i:i\in A\}.              \tag{6}
\]

Since a subset of a convex-position set is again in convex position,
`B_W` is a convex base.  Independence of `S` says that the two cyclic
neighbours of every `i in S` lie in `A`.  They are consecutive after the
other cells of `S` are removed, so `x_i` is a singleton ear replacing one
edge of `B_W`.  Distinct cells of `S` replace distinct base edges.  The
entire original word is the simultaneous insertion of these ears.

For even `q`, this is the usual odd/even presentation.  For odd `q`, one
base edge receives no ear; nothing changes.  Small ranks can be absorbed
in a constant loss and are irrelevant at coefficient scale.

## 2. Root-compatible incidence theorem

Let `E` be a family of `M` convex singleton words in common disjoint macro
containers `X_i`, and let

\[
                 m_i=|\pi_i E|\le D.                     \tag{7}
\]

Fix `g`, choose `S` as above, and let `J` be any family of ordinary local
profiles supported in `X_g`.  A pair `(W,F) in E times J` is called
**root-compatible** if `B_W union F` is an admissible ear replacement on
the base edge corresponding to `g`, with the prescribed macro order.  Let
`C` be the set of all such pairs.

Two ear edges are adjacent when they share a base vertex.  Let `N(g)` be
the at most two cells of `S\{g}` whose ear edges are adjacent to the target
edge.  For `(W,F) in C`, omit precisely those `h in N(g)` for which the
selected singleton ear `x_h` has the wrong shared-vertex turn with `F`, and
write

\[
 \Phi(W,F)=B_W\cup F\cup
    \{x_i:i\in S\setminus(\{g\}\cup D(W,F))\}.           \tag{8}
\]

> **Theorem 1 (parity-promoted adaptive omission).**  Every set in (8) is
> an ordinary face.  The map `Phi` has load at most
> 
> \[
>                     m_g\prod_{h\in N(g)}m_h,            \tag{9}
> \]
> 
> and therefore (1) holds.

**Proof.**  Work with the fixed base `B_W` belonging to this input word.
The profile `F` is an individually admissible ear by root compatibility;
every other ear is individually admissible because it comes from the
convex word `W`.  Ears on nonadjacent base edges commute.  All adjacent
seams not involving `F` are inherited from `W`.  A seam involving `F` is
either good or its other ear is omitted.  Omitting an ear restores its
base edge and exposes no farther occupied ear edge.  The fixed-base local
turn criterion therefore makes (8) convex.

The output meets the disjoint support `X_i` in the retained trace of cell
`i`.  It hence recovers `F`, the whole varying base `B_W`, every retained
ear, and the omission mask.  Only the old source value at `g` and the
values at the at most two omitted neighbours can be missing.  Their number
is bounded by (9), independently of how many different bases occur.
Dividing `|C|` by this load proves (1).  QED.

The phrase “root-compatible” includes the full constant-size tangent
state.  In a polygonal ear presentation, admissibility can involve the
predecessor of the first edge endpoint and the successor of the second,
not merely the two endpoints.  All of these anchors lie in `B_W` and are
retained, so this qualification changes neither the proof nor the load.

## 3. Cross-audit of the mask-entropy threshold

We do not duplicate the mask theorem or its 1,297,044-system exhaustive
verifier here.  Taking logarithms in its fixed-mask core gives

\[
 \log V(P)\ge\log M+\log|J|-q-E(D).                     \tag{10}
\]

In particular, a fixed-power gain over `M` follows as soon as

\[
 E(D)\le\log|J|-(1-\epsilon)\log D-q.                    \tag{11}
\]

If `q=O(d)` and `log|J|=Theta(d^2)`, every
`E(D)=o(d^2)` cascade is free at quadratic scale.  More sharply, assume

\[
 \log M=(a-o(1))d^2,\qquad q\le\kappa d,
 \qquad\log|J|=(c_0(a/\kappa)^2-o(1))d^2.               \tag{12}
\]

An unpaid mask must satisfy

\[
 E(D)\ge(c_0(a/\kappa)^2-o(1))d^2.                      \tag{13}
\]

At `a=kappa=1/4`, `c_0=1/8`, the right side is
`(1/8-o(1))d^2=(1/2-o(1))log M`.

For Theorem 1, `D(W,F) subseteq N(g)`, so
`E(D)<=3log D`; equation (10) retains every quadratic contribution of a
compatible jet reservoir.

## 4. Semialgebraic localization of the remaining branch

Partition a local reservoir by its actual first-two/last-two boundary jet.
There are at most `(L+1)^4` classes, so a rich class retains its quadratic
coefficient.  In a separated oriented-ear container, internal convexity is
already certified and root admissibility is determined by finitely many
orientation signs involving this fixed jet and the constant-size retained
tangent state of `B_W`.

These are bounded-complexity planar semialgebraic predicates.  The
redundancy-charged transcript theorem in
`REDUNDANCY_CHARGED_SEMIALGEBRAIC_RETENTION.md` therefore gives, at cost
`2^{-O(r+R)}`, a product trace on which all of the relevant signs are
homogeneous.  On such a trace exactly one of the following occurs.

1. **Root-good.**  Every retained source--profile incidence belongs to
   `C`; Theorem 1 gives the compatible jet multiplier with only `D^3`
   load.
2. **Root-bad.**  Every `B_W union F` is nonconvex.  Since `B_W` and `F`
   are separately in convex position, a minimal planar dependence meets
   both sides.  In general position it is a mixed `1+3` four-circuit.  Its
   bad seam is marked by the retained tangent state and fixed profile jet,
   although the fourth circuit point need not be constant across the
   fibre.

The transcript theorem only localizes the second alternative; it does not
turn its circuits into distinct ordinary faces.  That circuit/shield
release is the genuinely missing operation.

Quantitatively, if the root-good cell retains
`M|J|2^{-O(r+R)}` incidences, `r=O(d)`, `R=o(d^2)`, and (12) holds, then

\[
 {\log V(P)\over d^2}\ge
       a+c_0(a/\kappa)^2-o(1).                           \tag{14}
\]

At the live values this is `3/8-o(1)`.  Thus the entire conditional
coefficient gain now fails only in the homogeneous root-bad transcript
cell, not because the compatible incidence has a varying base.

## 5. A scalable half-entropy cascade is root-bad immediately

Here is a robust model showing that the threshold (13) cannot be lowered
for an unrestricted deletion cascade.  Let `q=2k+1`, with macro indices
`-k,...,k`, and let every cell have `L` labels.  Before a generic
perturbation put

\[
             p_{i,t}=(i,i^2-\delta_{i,t}),
        \qquad 0<\delta_{i,t}<\eta<1/2.                  \tag{15}
\]

Choose all deltas distinctly.  For every transversal, consecutive slopes
satisfy

\[
 (y_{i+2}-y_{i+1})-(y_{i+1}-y_i)
   =2-\delta_{i+2}+2\delta_{i+1}-\delta_i>2-4\eta>0.     \tag{16}
\]

Hence every transversal is a strictly convex lower chain and therefore a
convex word.  At the central cell choose an outer point
`o=(0,-delta_o)` and an inner point `p=(0,-delta_p)` with
`delta_o>delta_p`.  For a left point
`a=(-s,s^2-delta_a)` and a right point
`b=(t,t^2-delta_b)`, `s,t>=1`, the line `ab` has height at zero

\[
 {t\over s+t}(s^2-\delta_a)+{s\over s+t}(t^2-\delta_b)
       =st-{t\delta_a+s\delta_b\over s+t}>1-\eta>0.     \tag{17}
\]

Both central points have negative height, with `p` strictly above `o`.
Thus `p` lies strictly inside `triangle(o,a,b)`.  Any set containing the
central pair and at least one retained label on each side is nonconvex.
A successful deletion must erase all `k` cells on one side, so

\[
                   E(D)\ge k\log L
                   ={q-1\over2q}\log M.                 \tag{18}
\]

The bound is attained by an actual one-sided cascade.  Replace the central
vertical segment by a very thin convex arc bulging to the right, with `o,p`
as its lower and upper endpoints.  Every subset of this arc containing its
first two and last two labels is one fixed-jet profile, and its union with
the entire left parabola chain is convex.  Select any desired subfamily
`J` of these `2^(L-4)` profiles.  Keeping the left side and deleting the
right side therefore succeeds with equality in (18), while retaining even
a single right guard recreates the triangle witness.

All properties used above are finitely many open strict inequalities.
Sufficiently small generic rational perturbations of every cell remove all
collinearities while preserving every transversal, containment, and
one-sided face.  If a chosen realization does not put `o,p` among the four
fixed jet labels, require them as two additional labels; this still leaves
at least `2^(L-6)` profiles.  In particular one may select a fixed-jet
subfamily with `log|J|=(1/8-o(1))d^2`, so (18) exactly meets the live
half-entropy threshold rather than merely exhibiting a long deletion path.

This is a quadratic erased-alphabet cascade when `q=Theta(log D)` and
`log L=Theta(log D)`.  Nevertheless it is root-bad before any deletion:
the parity base contains anchors on both sides of zero, and (17) is already
a circuit in `B_W union {o,p}`.  Parity promotion has correctly sent it to
branch 2 of Section 4.

An exact seven-cell, two-label rational instance used by the verifier is

\[
\begin{array}{c|cc}
i&\delta_{i,0}&\delta_{i,1}\\ \hline
-3&7/500&14/625\\
-2&23/2500&11/625\\
-1&19/1000&59/2500\\
0&29/10000&13/1250\\
1&61/5000&41/2000\\
2&12/625&63/2500\\
3&21/1250&213/10000.
\end{array}                                             \tag{19}
\]

All `2^7` transversals are convex and the central upper point lies inside
the required triangle for all `36` choices of a left and right macro cell
and all four label pairs.

## 6. The exact `R=0` reset obstruction is also root-bad

For the rational points from
`DOMINANCE_CELL_SEPARATED_ONE_GAP.md`,

\[
\begin{aligned}
q&=(-19/20,1/20),&x&=(-3/40,7/8),\\
w&=(0,10/11),&z&=(3/40,7/8),&y&=(2/15,8/9),
\end{aligned}                                           \tag{20}
\]

both singleton words `{q,x,w,z}` and `{q,x,w,y}` are convex.  The profile
`F={z,y}` has one fixed jet.  Put the target in the parity ear whose two
retained anchors are `q,w`.  Then `B_W union F={q,w,z,y}` is nonconvex,
because

\[
 z={15\over662}q+{671\over2648}w+{1917\over2648}y.       \tag{21}
\]

All coefficients are positive and sum to one.  Thus the old failure after
omitting `w` was not evidence for a root-good cascade: the same profile is
already forbidden by its word-dependent parity base.

Projective singleton-reset universality does not affect Theorem 1, which
uses only the convexity of each selected word and recoverable macro
supports.  Conversely, it prevents one from dismissing branch 2 by an
individual-cluster rigidity claim: arbitrary order types can be nested
behind the same anchor circuit.

## 7. Why this is not a subhalf construction

The scalable model is an operation barrier, not a low-face upper
construction.  With convex local arcs, one cell alone has `2^L` faces,
far more than the target quadratic-logarithmic scale.  Replacing convex
arcs by projectively universal low-face clusters does not fix this globally:
the detached radial lexicographic recurrence gives the one-gap bank

\[
 \max_j B_j\ge P_0
      \left(\prod_i{H_i\over L_i^3}\right)^{1/q}.         \tag{22}
\]

The universal local reservoir and cyclic multiplication make the factor in
(22) `2^{Omega((log D)^2)}` whenever the source entropy is quadratic and
`q=O(log D)`.  Hence the standard radial product pays through detached
profiles even though a single central cascade erases half the coordinates.

Any remaining proof must sum the homogeneous root-bad circuit fibres over
their actual bases, or identify their released shields with the already
recoverable one-gap banks.  It need not control predecessor/successor
cascades in the root-good branch.

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_nonseparated_mask_parity_promotion.py
```

The checker verifies independent parity bases for every target through
rank 30, exhausts a varying-base decoder with the `D^3` load, checks the
exact rational root-good replacement, all 128 transversals and all central
triangle witnesses in (19), the half-entropy threshold, and the exact
root-bad barycentric identity (21).
