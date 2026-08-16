# Cyclic Ferrers transfer: a one-face gap bank or a heavy seam rectangle

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

There is an exact cyclic transfer theorem once local detached faces are
restricted to the profiles which are genuine ears at their assigned base
edge.

Let `B` be a fixed convex base and let each occupied boundary edge carry
one disjoint rooted-ear container.  Nonadjacent ears commute.  Two ears on
adjacent edges are compatible exactly when their new turn at the common
base vertex has the parent sign; after ordering the two tangent rays, this
is a Ferrers relation.

Let `E` be any family of `M` valid full words.  At cell `g`, let `m_g` be
the size of its selected trace projection and let `H_g` be the number of
nonempty detached profiles which are themselves admissible ears at edge
`g`.  Put

\[
                           K=\max_g {H_g\over m_g}.       \tag{1}
\]

Then, for a maximizing gap `g`, one of the following holds.

1. There is an injective **one-face** gap bank of size at least
   
   \[
                              {KM\over2}.                \tag{2}
   \]

2. At one of the two seams incident with `g`, there is a complete Ferrers
   rectangle of incompatible tangent profiles, all rooted at the same base
   vertex, whose contextual incidence mass is at least
   
   \[
                    {KM\over4(1+\lfloor\log M\rfloor)}. \tag{3}
   \]

Every incidence in the second branch makes the corresponding spliced set
nonconvex and hence contains a planar four-circuit.  Thus a quadratic local
reservoir surplus cannot disappear: it becomes either an ordinary mixed
face bank with no square loss, or a fixed heavy seam/circuit cell with only
a polylogarithmic loss.

Deleting the shared bad base vertex does **not** always turn the circuit
branch into a face bank.  It does so for all singleton pairs in the finite
audit, but a strict rational two-vertex ear already leaves another ear
vertex hidden.  The exact release condition is a second two-turn,
four-label seam test recorded in Section 3.  Thus the circuit branch is a
genuine residual rather than a disguised automatic bank.

This is sharp in its dependence on `K`.  If the selected alphabet in every
container already equals its entire admissible local face reservoir, then
`K=1`.  A scalable interleaved-conic construction has every adjacent seam
compatible, the one-gap bank has size exactly `M`, and there is no bad
seam.  Therefore no unconditional “quadratic gain or circuit” theorem can
omit the local reservoir-surplus hypothesis.

The exact verifier is

```text
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_cyclic_ferrers_one_gap.py
```

It checks the transfer identities and both alternatives on exact finite
Ferrers cycles, exhausts a strict rational adjacent-ear matrix, verifies
the weighted Ferrers rectangle lemma, checks guard release on all 24 bad
singleton pairs, verifies the six-point multi-ear obstruction, and
constructs the saturation regression on a rational conic.

## 1. Oriented ear-container model

Orient the boundary of the strictly convex base

\[
                         B=(b_1,\ldots,b_r)              \tag{4}

\]

counterclockwise.  An **admissible ear profile** at the oriented edge
`e_i=b_i b_(i+1)` is a nonempty ordinary face `F` in a support `X_i` such
that `B union F` is convex and the cyclic boundary is obtained from (4) by
replacing `e_i` with one path

\[
                         b_i,F,b_{i+1}.                  \tag{5}

\]

The path may have arbitrary internal order type.  Only its first and last
tangent neighbours are visible to adjacent containers.

The container system is **oriented** if simultaneous insertion paths give
a simple cyclic word.  This is the exact setting left after
`PARENT_SEAM_JET_COMPLETION.md`: distinct nonadjacent gap edges commute,
and adjacent gaps can create only their shared-vertex turn.  Consequently:

> **Lemma 1 (local-to-cyclic compatibility).**  A word of admissible ears
> is an ordinary face with `B` if and only if every pair of ears on
> adjacent occupied edges has the correct turn at their shared base vertex.

**Proof.**  Insert all paths (5) into the cyclic base word.  Every turn
inside a path or at an endpoint not shared by two occupied edges occurs in
one individually convex ear.  A turn at a base vertex incident with two
occupied edges is the only new turn.  The oriented-container word is
simple, so it is strictly convex exactly when every such turn has the
parent sign.  QED.

If `ell` and `r` are the two ear neighbours of a shared vertex `z`, the
condition is

\[
                         \chi(\ell,z,r)>0               \tag{6}

\]

after fixing the counterclockwise sign.  Ordering rays about `z` turns (6)
into a threshold comparison.  Its nonedges are prefixes in one order
(equivalently suffixes in the reversed order), so the compatibility matrix
is Ferrers.

## 2. Exact cyclic transfer at one gap

For cell `i`, let `mathcal A_i` be the projection of the selected full-word
family `E` to that cell, and put `m_i=|mathcal A_i|`.  Let
`mathcal H_i` be any family of admissible detached ear profiles in `X_i`,
with `H_i=|mathcal H_i|`.

Fix a gap `g`.  Delete coordinate `g` from every selected word and merge
duplicates.  This gives a family `mathcal P_g` of valid partial words, of
size `Q_g`.  Since one partial word has at most `m_g` selected completions,

\[
                       {M\over m_g}\le Q_g\le M.         \tag{7}

For `p in mathcal P_g` and `F in mathcal H_g`, all seams internal to `p`
are already good.  By Lemma 1, the completed set

\[
                   B\cup F\cup\bigcup_{i\ne g}p_i       \tag{8}

is convex if and only if the one or two seams incident with `g` are good.
Let `C_g` be the number of compatible pairs `(p,F)`.  The outputs (8) are
distinct: intersection with the disjoint cell supports recovers `p` and
`F`.  Thus `C_g` is the exact size of a one-face bank.

There are `H_gQ_g` formal substitutions.  If at least half are compatible,
then (7) gives

\[
                  C_g\ge {H_gQ_g\over2}
                     \ge {H_gM\over2m_g}.               \tag{9}

This proves (2) at a cell maximizing (1).

Suppose instead that `C_g<H_gQ_g/2`.  More than half the substitutions fail
at a seam.  Let `R_L` and `R_R` count failures of the left and right seam,
respectively; a substitution failing both is allowed in both counts.  Since
the union of those failure events contains every rejected substitution,

\[
                  \max(R_L,R_R)>{H_gQ_g\over4}.         \tag{10}

It remains to use the Ferrers structure without losing the contextual
partial-word multiplicity.

## 3. Weighted Ferrers rectangles lose only a logarithm

> **Lemma 2 (weighted Ferrers bad rectangle).**  Let rows
> `1,...,s` have nonnegative integer weights `mu_1,...,mu_s`, of positive
> total weight `W`.  Suppose each column `f` has a bad neighborhood which
> is a row prefix.  If
> 
> \[
>                         R=\sum_f\sum_{i\le t_f}\mu_i  \tag{11}
> \]
> 
> is the total weighted bad incidence, then some prefix `I` and some set
> of columns `J` form a complete bad rectangle and satisfy
> 
> \[
>       \left(\sum_{i\in I}\mu_i\right)|J|
>             \ge {R\over1+\lfloor\log W\rfloor}.       \tag{12}
> \]

**Proof.**  Put `S_t=sum_(i<=t)mu_i`.  For every integer
`0<=j<=floor(log W)`, let `i_j` be the first index with `S_(i_j)>=2^j`,
and let `J_j` be the columns whose bad prefix has weight at least `2^j`.
Then `I_j={1,...,i_j}` times `J_j` is a complete bad rectangle of weight at
least `2^j|J_j|`.

For a column whose bad-prefix weight is `s`, the sum of powers `2^j<=s` is
at least `s`.  Therefore

\[
                         R\le\sum_j2^j|J_j|.            \tag{13}
\]

One of the at most `1+floor(log W)` rectangles has weight at least (12).
QED.

Apply the lemma to the heavier seam in (10).  A row is a tangent profile
of the neighboring selected ear; its weight is the number of partial words
having that endpoint profile.  The total row weight is exactly `Q_g`.
Columns are the profiles in `mathcal H_g`.  Reversing the ray order if
needed makes every incompatible neighborhood a prefix.  Equations
(7), (10), and (12) give a complete bad rectangle of contextual mass

\[
 {H_gQ_g\over4(1+\lfloor\log Q_g\rfloor)}
 \ge {H_gM\over4m_g(1+\lfloor\log M\rfloor)}.          \tag{14}

This is (3).

Every pair in the rectangle has the wrong turn at one fixed base vertex.
The spliced union is nonconvex.  Planar four-locality supplies a four-point
circuit inside that union; the entire rectangle is therefore a fixed
weighted seam/circuit cell.  The theorem does not claim that this circuit
branch already pays in ordinary faces.  It preserves the full quadratic
incidence entropy for the subsequent anchor/shield charge.

### 3.1 Deleting the bad base vertex: an exact second seam

Let the two adjacent parent edges be `uz` and `zv`.  Write the two inserted
paths in cyclic order as

\[
 u,\ell_1,\ldots,\ell_p,z,
 r_1,\ldots,r_q,v.                                      \tag{14a}
\]

An incompatible pair has the wrong turn at `z`.  Delete `z`.  The candidate
released boundary word is

\[
 u,\ell_1,\ldots,\ell_p,
 r_1,\ldots,r_q,v.                                      \tag{14b}
\]

Every turn in (14b) is inherited from one of the two individually convex
ears except the turns at `ell_p` and `r_1`.  With `ell_0=u` when `p=1` and
`r_2=v` when `q=1`, the same turning-angle argument as in
`PARENT_SEAM_JET_COMPLETION.md` proves

\[
 \boxed{
 (B\setminus\{z\})\cup L\cup R\text{ is convex}
 \iff
 \chi(\ell_{p-1},\ell_p,r_1)>0
 \text{ and }
 \chi(\ell_p,r_1,r_2)>0.}                              \tag{14c}
\]

Hence any release-good part of the heavy rectangle is immediately an
injective guard-release face bank: the fixed deleted label `z` and the
disjoint supports decode every output.  But release-bad mass is real.  Take

\[
 \begin{aligned}
 B&=\{(-3,0),(3,0),(0,4)\},\qquad z=(3,0),\\
 L&=\{(-10,-16),(-9,-15)\},\qquad R=\{(8,1)\}.
 \end{aligned}                                         \tag{14d}
\]

The six points are in general position.  Both `B union L` and `B union R`
are convex ears on the adjacent edges ending and starting at `z`.
Their union is nonconvex.  After deleting `z`, the point `(-9,-15)` remains
hidden; equivalently the first turn in (14c) equals `-1`.

Thus the bad rectangle may be split once more into release-good and
release-bad four-label jet cells.  Quantitatively, let `Z` be the
contextual incidence mass in (14).  If at least `Z/2` incidences are
release-good, their released outputs form an injective face bank of size
at least

\[
 {H_gM\over8m_g(1+\lfloor\log M\rfloor)}.             \tag{14e}
\]

Otherwise at least `Z/2` incidences are release-bad.  The two new turns in
(14c) depend on only four tangent-neighbour labels.  Among at most `N^4`
joint jet states, one fixed release-defect state therefore has contextual
mass at least

\[
 {H_gM\over8N^4m_g(1+\lfloor\log M\rfloor)}.          \tag{14f}
\]

Fixing such a jet costs only `O(log N)` bits at coefficient scale, but the
release-bad child still requires a further circuit/anchor charge.  At a
fixed-power scale the `N^4` loss is not harmless; no stronger compression
is proved here.  Automatic deletion of `z` is false.

## 4. Coefficient accounting

Let `L=log N`, where `N` is the ambient point count.  Suppose

\[
             \log M=(a+o(1))L^2,qquad
             \log K=(delta+o(1))L^2.                   \tag{15}

In the bank branch, (2) gives

\[
                         \log V(P)\ge(a+delta-o(1))L^2. \tag{16}

In the circuit branch, (3) has the same coefficient `a+delta`: its
denominator contributes only `O(log L)` bits.  Unlike the separated
two-output bank, no square root and no extra `-log M` occurs.

There is a useful sufficient condition for a quadratic `K`.  Suppose there
are `k<=kappa L` occupied containers, every selected local trace has rank at
most a fixed `t`, and every nonempty ordinary face of `X_i` is an admissible
ear profile.  Put `n_i=|X_i|`.  If the universal local reservoir obeys

\[
                     \log H_i\ge c_0(\log n_i)^2-C_0,  \tag{17}

\]

then bounded rank gives, for constants `c_t>0,C_t`,

\[
 \log{H_i\over m_i}
       \ge c_t(\log m_i)^2-\log m_i-C_t.                \tag{18}

Let `x=sum_i log m_i=log product_i m_i`.  Since `E` is contained in the
projection product, `x>=log M`.  Cauchy and (18) yield

\[
 \log K\ge {1\over k}\sum_i\log{H_i\over m_i}
       \ge c_t{x^2\over k^2}-{x\over k}-C_t.            \tag{19}

For large `L`, the final quadratic in `x/k` is increasing throughout
`x/k>=aL/kappa`.  Hence at `log M>=aL^2` and `k<=kappa L`, this gives

\[
               \log K\ge
            \left({c_ta^2\over\kappa^2}-o(1)\right)L^2.\tag{20}

Thus the exact cyclic theorem converts the bounded-rank local reservoir
directly into either a coefficient gain or a same-coefficient heavy seam.

## 5. Arbitrary detached faces: the root-admissibility gate

An arbitrary ordinary face of a detached support need not be an admissible
ear when restored to `B`.  This cannot be hidden in the word “profile”.
For a local detached family `mathcal F_i`, split it into

\[
 \mathcal H_i=\{F:B\cup F\text{ is an ear at }e_i\},
 \qquad \mathcal R_i=\mathcal F_i\setminus\mathcal H_i.\tag{21}

Every member of `mathcal R_i` already gives a nonconvex anchored union with
the fixed base.  If it carries the reservoir mass, this is a fixed
base-edge circuit cell.  Otherwise `mathcal H_i` retains the mass and the
cyclic theorem applies.  Merely interval-partitioning the selected
singletons does not prove that `mathcal H_i` is large: multi-point faces can
change their insertion edge or tangent jet, exactly as in the positive
`1+3` circuit regression of
`DOMINANCE_CELL_SEPARATED_ONE_GAP.md`.

## 6. Sharp saturation regression

The factor `K` is necessary.  For arbitrary integers `k,s>=1`, choose
`k(s+1)` rational points in convex position on one conic.  In cyclic order,
let every `(s+1)`-st point be a base vertex; the `s` points between two
successive base vertices form the container `X_i` on that base edge.

Every subset of the full conic set is ordinary.  In particular every
nonempty subset of `X_i` is an admissible ear, and arbitrary choices in all
containers cross-complete.  Select the entire nonempty local alphabet:

\[
                    m_i=H_i=2^s-1,qquad
                    M=(2^s-1)^k.                       \tag{22}

Every seam is complete, `K=1`, and for every gap

\[
                          C_g=H_g{M\over m_g}=M.         \tag{23}

There is neither a one-face multiplier nor a bad seam.  The construction
is scalable and exact.  To place its selected entropy on a
`Theta((log N)^2)` scale, choose `ks=Theta((log N)^2)` and pad the ambient
configuration to `N` points in general position.  The conic support itself
pays exactly the selected full product, so this is a barrier to a stronger
**local** transfer theorem, not a low-face counterexample to the global
problem.

## 7. What remains

The cyclic parent-coupling step is now exact.  A proof using it must supply
one of two genuinely global inputs:

1. enough root-admissible local reservoir surplus to make `K` quadratic;
   or
2. a summable anchor/shield charge for the heavy bad rectangle in (3) or
   the root-bad family in (21).

Selected-word correlations, MDS constraints, and cyclic transfer matrices
do not create any further loss: they are absorbed by the exact partial-word
projection bound (7).
