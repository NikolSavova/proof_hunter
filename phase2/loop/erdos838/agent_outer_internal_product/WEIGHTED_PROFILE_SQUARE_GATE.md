# Weighted profile square gate under the low-rank source cutoff

**Date:** 2026-08-14.  All logarithms are base two and the empty convex
subset is counted.

## Verdict

Adding the external profile-entropy variable gives a genuine global positive
branch.  A rooted completion profile has two different ordinary-face banks:

1. a **carrier bank** which restores the missing root label and varies the
   remaining guard downset;
2. a **completion bank** which deletes the guard and inserts one label of the
   actual role-pocket.

The carrier output contains the whole root, so its overlap costs only root
choices *inside* a rank-`R` face.  The completion output retains a root edge
and costs one missing label.  Cauchy across the two banks yields

\[
 \boxed{
 W\sqrt{2^{g-1}m}
 \le \mathcal K
       \sqrt{{R\choose3}\,n{R\choose2}}\;V(P),}             \tag{1}
\]

where `W` is the number of weighted marked source occurrences in the slice,
`g` is minimum guard size, `m` is minimum singleton completion alphabet, and
`mathcal K` is the maximum number of canonical profiles listed for one root.

Thus if `W>=beta V`, `g>=gamma log n`, `m>=n/polylog(n)`, and
`R=polylog(n)`, then

\[
                    \mathcal K\ge n^{\gamma/2-o(1)}.         \tag{2}
\]

Equivalently, profile lists smaller than
`n^(gamma/2-epsilon)` give a fixed-power ordinary-face gain and close that
branch.  The `sqrt(m)` factor exactly cancels the `sqrt(n)` missing-root loss;
the surviving `sqrt(2^g)` is the gain unavailable to either bank alone.

The low-rank cutoff also kills the quadratic-entropy version of the common
cage regression.  If retained sources have rank at most `h=O(log n)` and a
fixed cage profile is supported inside a common convex carrier of rank
`R=O((log n)^2)`, then it has at most

\[
                 \sum_{j\le h}{R\choose j}
                 =2^{O((\log n)\log\log n)}                 \tag{3}
\]

source contexts.  It cannot carry `Theta(V)` mass when
`log V=Theta((log n)^2)`.  Therefore the earlier reinforced cage remains a
sharp local regression but not a heavy weighted regression in the live
bounded-rank slice.

The unresolved branch is now precise: a positive fraction of weighted mass
must be distributed over roots with `n^{Omega(1)}` distinct canonical guard
profiles.  These profiles already give fixed-power guard/root face reservoirs,
but no theorem here multiplies that absolute reservoir by `V`.  The result is
conditional, not a closure of EIC'.

## 1. Canonical rooted singleton profiles

Fix the marked incidence family from
`GLOBAL_MARKED_POCKET_RELEASE.md`.  A **rooted singleton profile** is labelled

\[
                         \pi=(T,z,G,X),                      \tag{4}
\]

where:

* `T` is a marked canonical triple and `z in T`;
* `G` is a convex-source guard satisfying `G cap T={z}`;
* `X subseteq X_T` is a nonempty completion alphabet;
* `mathscr S_pi` is a family of marked source faces `A` containing `G` such
  that

\[
                       (A\setminus G)\cup\{x\}              \tag{5}
\]

  is convex for every `x in X`.

Write `w_pi=|mathscr S_pi|`, `g_pi=|G|`, and `m_pi=|X|`.  Profiles are
canonical: for each root `T`, the decoder has a fixed list of at most
`mathcal K` tuples `(z,G,X)`.  A marked occurrence assigned to a profile is
counted once.  Let

\[
                         W=\sum_\pi w_\pi.                   \tag{6}
\]

This formulation preserves the actual root, role-pocket alphabet, source
face, and guard; it does not project any of them away.

## 2. The two profile banks

For a profile `pi`, put `e=T setminus {z}` and `B=A setminus G`.

### Carrier bank

For every source `A` and every `D subseteq G` containing `z`, output

\[
                              C_A=B\cup D.                   \tag{7}
\]

This is a subset of the convex source `A`, hence a face.  There are exactly

\[
                           |\mathcal A_\pi|=w_\pi2^{g_\pi-1}
                                                               \tag{8}
\]

records.  Given the profile and output, `D=C_A cap G` and
`A=(C_A setminus D) union G`, so the bank is injective within the profile.

Most importantly, `C_A` contains all of `T`: the retained edge `e` lies in
`B` and `z` lies in `D`.  A rank-`R` output belongs to at most

\[
                         L_A={R\choose3}\mathcal K           \tag{9}

carrier banks.  Guess `T subseteq C_A`, then its canonical profile.

### Completion bank

For every source `A` and `x in X`, output (5).  There are exactly

\[
                           |\mathcal B_\pi|=w_\pi m_\pi       \tag{10}

records.  It contains `e`.  Guessing `e subseteq C_B`, the missing label `z`,
and the profile determines `T`; then

\[
             \{x\}=C_B\cap X,qquad A=(C_B\setminus\{x\})\cup G.
                                                               \tag{11}
\]

Thus

\[
                         L_B=n{R\choose2}\mathcal K.         \tag{12}

\]

The role-pocket disjointness `A cap X_T=emptyset` makes (11) exact.

## 3. Cross-bank Cauchy theorem

> **Theorem 1 (weighted profile square gate).**  For arbitrary profile sizes,
>
> \[
> \sum_\pi w_\pi\sqrt{2^{g_\pi-1}m_\pi}
> \le \mathcal K
> \sqrt{{R\choose3}\,n{R\choose2}}\;V(P).                  \tag{13}
> \]
>
> In particular, uniform bounds `g_pi>=g`, `m_pi>=m` imply (1).

**Proof.**  Equations (8) and (10) give the exact identity

\[
 w_\pi\sqrt{2^{g_\pi-1}m_\pi}
       =\sqrt{|\mathcal A_\pi||\mathcal B_\pi|}.             \tag{14}
\]

By (9)--(12),

\[
 \sum_\pi|\mathcal A_\pi|\le L_AV,
 \qquad
 \sum_\pi|\mathcal B_\pi|\le L_BV.                        \tag{15}
\]

Sum (14) and apply Cauchy.  Substituting `L_A,L_B` proves (13).  QED.

If `W>=beta V`, equation (1) rearranges to

\[
 \mathcal K\ge
 {\beta\sqrt{2^{g-1}m}
  \over\sqrt{n\binom R3\binom R2}}.                         \tag{16}
\]

For `g>=gamma L`, `m>=n/L^a`, and `R<=L^b`, the right side is

\[
                         n^{\gamma/2}/L^{a/2+5b/2+O(1)},    \tag{17}
\]

which proves (2).

This is the requested light-profile half of the heavy/light split.  More
generally, apply (13) only to roots whose canonical lists have size at most
`K_0`.  Unless their weighted mass is negligible, (16) forces
`K_0>=n^(gamma/2-o(1))`; hence the hard mass must lie on high-profile-entropy
roots.

## 4. What heavy profile entropy supplies

Normalize a profile by `(T,z,G)`; the alphabet is then the canonical maximal
set of labels released by that guard.  For a fixed root, map the profile to

\[
                              H_\pi=G\cup(T\setminus\{z\}).  \tag{18}
\]

This is an ordinary face because it is a subset of every source supporting
the profile.  Given `T` and `H_pi`, guessing `z in T` recovers
`G=H_pi setminus (T setminus {z})`.  Therefore a root with `mathcal K_T`
profiles supplies at least `mathcal K_T/3` distinct ordinary profile faces.
Each guard separately also supplies its full downset of size `2^{g_pi}`.

Equation (2) consequently forces a fixed-power absolute face reservoir in the
heavy branch.  What is not proved is a recoverable multiplication of this
reservoir by the ambient weighted source mass.  The common-cage geometry
shows why the naive multiplication fails: restoring even one deleted shield
label can immediately destroy every singleton completion.

## 5. Bounded-rank carrier capacity

The live minimizer slice has uniform mean `mu=O(L)`.  After the stipulated
constant-loss cutoff, take source rank

\[
                              |A|\le h=C_0L.                 \tag{19}
\]

Suppose a fixed cage/profile has a common convex outer carrier `Q` containing
all its source faces.  Since every subset of `Q` is an ordinary face,
`|Q|<=R`, and the number of possible retained sources is at most

\[
 \sum_{j=0}^{h}{|Q|\choose j}
 \le\left({eR\over h}\right)^h
 =2^{O_{C_0}(L\log L)}                                    \tag{20}
\]

when `R=O(L^2)`.

In particular, the earlier cage with a single common carrier cannot realize
`2^{Theta(L^2)}` weighted source entropy while respecting (19).  To carry a
positive fraction of `V=2^{Theta(L^2)}`, one needs
`2^{Theta(L^2)}` distinct carrier/profile contexts up to the subquadratic
loss in (20).  That is exactly the high-profile-entropy residual isolated by
(16), rather than a scalable one-cage counterexample.

## 6. Exact sharpness of using two banks

The carrier and completion banks generally cannot be multiplied pointwise.
In the three-arc cage, let `G` be one complete arc.  The base `B=A setminus G`
retains the other two arcs.  Every `B union D` with `D subseteq G` is an outer
face, and every `B union {x}` is a singleton completion.  But for every
nonempty `D` and every central `x`,

\[
                              B\cup D\cup\{x\}               \tag{21}
\]

contains a transversal triangle around `x` and is nonconvex.  The local
state space is the cross `2^G union X`, of size `2^g+m`, not the rectangle
`2^g times m`.

Theorem 1 is therefore the exact safe use of both banks: combine their
cardinalities by Cauchy across contexts, without claiming mixed faces.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_weighted_profile_square.py
```

The exact rational checker uses the reinforced cage from
`PREVALENCE_COMMON_CAGE_REGRESSION.md`.  It constructs the three canonical
arc profiles, all weighted sources, both banks, and both decoders.  It audits
the exact Cauchy identity and confirms that every forbidden pointwise product
(21) is nonconvex.
