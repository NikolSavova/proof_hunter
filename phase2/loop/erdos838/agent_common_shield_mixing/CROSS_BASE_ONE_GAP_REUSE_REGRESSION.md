# Cross-base one-gap summation: exact Cauchy gate and radial reuse regression

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

Canonicalizing the petal containers from a detached one-gap output does
**not** give subquadratic cross-base overlap.  There is a scalable planar,
fixed-tangent radial regression in which:

* every base context has the same sparse-family entropy profile and the
  same canonical maximizing gap;
* every one-gap output reveals its active petal pattern and all local
  profile choices exactly;
* nevertheless the bank is reused by every base word, with overlap

  \[
                            C=\prod_{a=1}^t|Y_a|;          \tag{1}
  \]
* `log C=Theta((log D)^2)` is possible while all sources remain convex and
  the complete tangent cell, mark, and shield are fixed; and
* adjoining a one-gap face to a source is generically nonconvex, so a
  source--gap pair decoder does not automatically become a one-face bank.

Thus the requested unconditional subquadratic decoder theorem is false.
The output sees which **petal** cluster is missing, but it contains no point
from any context cluster absorbed into the parent, and therefore cannot
recover their values or even certify how many such clusters were omitted.

There is an exact conditional Cauchy theorem.  If context `c` has a source
bank `mathcal A_c`, a one-gap bank `mathcal G_c`, and demand `m_c` with

\[
 |\mathcal A_c|\ge m_c,qquad
 |\mathcal G_c|\ge K_c m_c,                               \tag{2}
\]

then, writing `Lambda_A,Lambda_G` for their aggregate face overlaps,

\[
 \boxed{
 \sum_cm_c\le
 \sqrt{\Lambda_A\Lambda_G\max_cK_c^{-1}}\;V(P).}         \tag{3}
\]

This is the sharp recoverable-cell interface.  The entropy-chain theorem
provides quadratic-exponential `K_c`; the regression makes
`Lambda_G=C` quadratic-exponential as well, while `Lambda_A=1`.  Hence
the local gain can be cancelled exactly by hidden base entropy.

The same regression identifies the geometric repair.  Promote the varying
base blocks into the recoverable cyclic container list and apply the
oriented entropy-chain theorem to their union with the petals.  The enlarged
one-gap banks contain the base values (except at one cyclic gap), and cyclic
profile multiplication restores the factor (1).  In the exact rational
instance, the common petal bank has nine faces and overlap two, while the
promoted four-block bank has eighteen faces: it recovers the missing factor
exactly.

This is not an EIC' counterexample; the enlarged radial cycle pays.  It is
a sharp kill of any theorem which tries to sum local max-gap banks from the
detached output alone.  The next load-bearing statement is a **container
promotion theorem**:

> high reuse of one canonical petal gap either makes the varying bases into
> recoverable additional radial/profile containers, or creates a bounded-
> load source--gap splice/outer-shield bank.

No such theorem follows merely from active macro-pattern recovery.

## 1. Recoverable-cell Cauchy theorem

Let all banks consist of ordinary faces of the same planar configuration.
Define

\[
 \Lambda_A=\max_F\sum_{c:F\in\mathcal A_c}1,qquad
 \Lambda_G=\max_F\sum_{c:F\in\mathcal G_c}1.             \tag{4}
\]

Weighted versions replace the indicators by the relevant cell weights.

> **Theorem 1 (source--gap Cauchy gate).**  Under (2), equation (3) holds.

**Proof.**  Put `K=min_cK_c`.  For each context,

\[
 m_c\le {1\over\sqrt K}
             \sqrt{|\mathcal A_c||\mathcal G_c|}.         \tag{5}
\]

Sum, apply Cauchy--Schwarz, and use the two overlap bounds:

\[
 \begin{aligned}
 \sum_cm_c
 &\le {1\over\sqrt K}
       \sqrt{\sum_c|\mathcal A_c|\sum_c|\mathcal G_c|}\\
 &\le\sqrt{{\Lambda_A\Lambda_G\over K}}\,V(P).
 \end{aligned}                                            \tag{6}
\]

This proves (3).  QED.

If a canonical one-gap output recovered its entire context with load
`Lambda_G=2^{o((log D)^2)}`, the theorem together with
`ORIENTED_RADIAL_ENTROPY_CHAIN.md` would close the radial atom.  The
regression below shows why that premise is false.

A decoder for the ordered **pair** `(A,U)`, source plus one-gap face, does
not by itself replace (4).  It controls incidences in `F(P)^2`, whose
capacity is `V(P)^2`; summing square roots over many contexts again requires
either separate overlap control or a single ordinary splice face.  Section
3 verifies that the latter fails maximally in the rational regression.

## 2. Scalable cross-base radial family

Take a projectively universal radial blow-up with a common fixed tangent
cell.  Outside its four protected tangent blocks, partition the active
macro clusters cyclically into

\[
               Y_1,\ldots,Y_t
       \quad\hbox{(context blocks)},\qquad
               X_1,\ldots,X_r
       \quad\hbox{(petal blocks)}.                        \tag{7}
\]

For simplicity let every cluster have size `L`; unequal sizes behave
identically.  A context word

\[
                         y\in Y_1\times\cdots\times Y_t  \tag{8}
\]

is absorbed into the base `B_y`.  Within this base take the complete petal
family

\[
                         \mathcal F_y=X_1\times\cdots\times X_r,
 \qquad M=L^r.                                            \tag{9}
\]

Every `B_y union D` is a convex radial transversal.  The actual repaired
star and the common blocker shield can be fixed exactly as in the marked
omitted-petal construction.

Apply the entropy-chain theorem only to the petal containers.  Their
supports, local directional profiles, conditional entropies, and canonical
maximizing gap are independent of `y`.  Hence

\[
                         \mathcal G_y=\mathcal G_{y'}      \tag{10}
\]

for all contexts, and every gap face has load

\[
                         \Lambda_G=L^t=C.                 \tag{11}
\]

The sources are distinct across context words, so `Lambda_A=1`.  Choose

\[
                 t=\tau\log D,qquad \log L=\delta\log D. \tag{12}
\]

Then

\[
                         \log C=\tau\delta(\log D)^2.     \tag{13}
\]

Thus (11) is not a polynomial bookkeeping loss and not a prefix-count
artifact.  It has the same leading scale as the local entropy-chain gain.
More explicitly, if `s=log L`, the guaranteed symmetric local multiplier
has logarithm `s^2/9-O(s)`, while the overlap has logarithm `ts`.  Taking
`t=ceil(s/9)` matches the two leading terms.  Both `t` and the petal rank
remain `O(log D)` when `s=Theta(log D)`.

The active macro pattern of `U in mathcal G_y` still recovers its missing
petal cluster and every retained local trace.  It contains no point of any
`Y_a`, so these data cannot distinguish the `C` values of `y`.  Any
geometry-only decoder from `U` has fibre at least `C` on this family.

## 3. Exact fixed-tangent rational regression

Use the eight two-point radial blocks from
`TANGENT_MARKED_SHIELD_DESCENT.md`.  Fix outer representatives in blocks
`7,0,1,2`, the actual repair label `p`, and an actual three-label shield
face `F` containing `p`.  Let block `3` be the context block and let blocks
`4,5,6` be the petal blocks.

There are two bases, one for each point of block `3`.  Over either base the
eight petal transversals are convex repaired sources.  For the petal cycle,
each gap leaves two active binary blocks.  Every nonempty subset of either
block may be used, so each of the three one-gap banks has

\[
                              3\cdot3=9                   \tag{14}
\]

ordinary faces.  All three tie; choose the first gap canonically.  The two
contexts then have literally the same nine outputs, each of load two.

The source banks contain eight faces each and are disjoint.  Among the
`8*9=72` source--gap pairs in either context, exactly eight unions are
convex: those in which the gap face is already contained in the source.
There are no new splice faces at all.

Now promote block `3` into the radial cycle.  Omitting it leaves the three
petal blocks active.  Exact enumeration gives eighteen profile faces:

\[
                    18=2\cdot9=C|\mathcal G_y|.           \tag{15}
\]

This is the smallest exact instance of container promotion paying the full
cross-base reuse.

## 4. Why promotion is the exact missing geometry

The full active radial product in Section 2 has `t+r` macro containers.
Applying the cyclic identity globally gives

\[
 \max_j B_j^{\rm full}\ge
 P_{\rm full}
 \left(\prod_i{H_i\over L_i^3}\right)^{1/(t+r)},
 \qquad P_{\rm full}=C M.                                \tag{16}
\]

The context factor `C` is now part of the transversal baseline rather than
an overlap.  Gaps in a petal block retain every context-block singleton;
gaps in a context block retain the others, and cyclic multiplication
prevents all of these promoted banks from being simultaneously small.

This proves that the regression is globally favorable once promotion is
known.  But an arbitrary family of varying bases need not arrive already
partitioned into recoverable macro clusters.  A detached output cannot see
points absent from it, so no canonicalization based on that output alone
can manufacture (7).

The required positive theorem must use pairs of contexts or their first bad
cross-base circuits.  A plausible exact dichotomy is:

1. cross-base circuits admit a cyclic/Ferrers ordering whose first-
   divergence blocks are promoted into (7), with subquadratic description
   loss; or
2. a positive share of source--gap collisions splice to ordinary faces
   with subquadratic load, so Theorem 1 is replaced by the one-face
   collision bound.

The outer-triangle wrapper in `GLOBAL_ONE_GAP_COLLISION_RELEASE.md` shows
that arbitrary circuit-connected bases do not suffice.  The promotion must
retain the actual radial/tangent history which determines their ordering.

## 5. Exact scope and consequence

The regression proves all of the following simultaneously:

* local sparse-family entropy is not the issue;
* local active-pattern and profile recovery can be exact;
* source faces can be globally injective;
* the max-gap bank can still have quadratic-exponential cross-base load;
* source--gap pairing need not create any nontrivial ordinary union; and
* the missing capacity is present in the enlarged radial cycle.

Therefore one cannot finish by inserting the local multiplier from (4) of
the entropy-chain report into a global Cauchy inequality and declaring the
decoder polynomial.  The decoder exponent is a genuine leading-order term.

What remains is narrower than generic Hall expansion: prove container
promotion from the fixed-tangent base histories, or charge the failure of
promotion to an already-listed outer/Ferrers/circuit-splice bank.  The
regression supplies the exact calibration any such theorem must attain:
it must turn overlap `C` into `C` additional ordinary outputs, as in (15),
without paying a context tag.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_cross_base_one_gap_reuse.py
```

The exact checker uses rational coordinates and verifies the fixed tangent,
actual repair mark/shield, two disjoint eight-source context banks, three
nine-face petal-gap banks identical across the two contexts, exact output
load two, failure of all
64 nontrivial source--gap splices per context, and the promoted eighteen-
face bank.  It also audits (3) on exhaustive random integer bank systems and
the scalable exponent (13).
