# Global cube prevalence: a polylogarithmic heavy branch

**Date:** 2026-08-15.  All logarithms are base two and the empty convex
subset is counted.

## Verdict

The central complete-layer cells admit an exact global heavy/light theorem,
with no copy of `V` spent per cell.  Write

\[
                 s=2r,\qquad a=2^{2r},\qquad
                 k={2r\choose r}.                           \tag{1}
\]

For each canonical cell `c`, let `mathcal A_c` be its released full cube and
let

\[
                 d(F)=|\{c:F\in\mathcal A_c\}|.             \tag{2}
\]

For any integer threshold `Delta>=1`, cells for which at least half of their
cube outputs have degree at most `Delta` carry marked mass at most

\[
                 M_{\rm light}\le {2k\Delta\over a}V
                 =O\!\left({\Delta\over\sqrt r}\right)V.    \tag{3}
\]

Thus taking `Delta=r^(1/3)` makes the light mass `o(V)`.  If the original bin
has `Theta(V)` mass, a positive share lies in cells for which more than half
the cube is shared by more than `r^(1/3)` other cells.  The corresponding
ordered cross-fibre collision energy is at least

\[
 \sum_{c\ne c'}|\mathcal A_c\cap\mathcal A_{c'}|
 \ge {\Delta a\over2k}M_{\rm high}
 =\Omega(\Delta\sqrt r\,M_{\rm high}).                     \tag{4}
\]

This is genuine global progress, but its heavy degree is only
`r^(1/3)=n^o(1)`.  Conditional on one common anchor face, the missing root is
decoded from only `O(log n)` candidates and a fixed-power completion bound
does follow.  Equation (4), however, does not concentrate `Theta(V)` mass at
one anchor.

An exact scalable parabola regression shows this distinction is necessary.
It has `2r+1` distinct root fibres on one outer chain.  More than half of
every cube has degree greater than `r`, all singleton completion banks
coincide, and no carrier-retaining outer/pocket mixed face exists.  Hence a
heavy common cube output does **not** by itself create diverse or recoverable
pocket banks.  The regression has only `n^O(1)` marked mass, not `Theta(V)`;
the remaining open task is a cross-anchor or cross-carrier prevalence
theorem.  EIC' is not closed here.

## 1. Uniform central cells

After the bounded-rank and exact-rank splits, consider a uniform family of
canonical cells.  Every cell has core `U_c` of size `2r`, complete middle
guard layer `{U_c choose r}`, and hence marked weight `k` from (1).  By the
complete-layer union lift,

\[
 \mathcal A_c=
 \{B_c\cup\{z_c\}\cup D:D\subseteq U_c\},qquad
 |\mathcal A_c|=a.                                         \tag{5}
\]

The cells remain indexed by the actual `(T_c,z_c,B_c)` data; there is no
quotient by equal cubes.  Let `mathcal C` be the cell set and

\[
                              M=k|\mathcal C|               \tag{6}
\]

its marked mass.  All outputs in (5) are ordinary faces, so their degree
function (2) satisfies

\[
                    \sum_Fd(F)=a|\mathcal C|.               \tag{7}
\]

The same argument works in a dyadic bin with `a_c/k_c` within a constant
factor.  The uniform statement is the sharp central model and avoids hiding
the `n^o(1)` binning cost.

## 2. Global light-cell bound

Call a cell `Delta`-light if at least `a/2` members of `mathcal A_c` have
degree at most `Delta`; otherwise call it `Delta`-heavy.

> **Theorem 1 (global cube prevalence).**  Equations (3)--(4) hold.

**Proof.**  Count incidences `(c,F)` with `c` light,
`F in mathcal A_c`, and `d(F)<=Delta`.  Every light cell contributes at least
`a/2`, whereas all low-degree faces together contribute at most `Delta V`.
Therefore

\[
          {a\over2}|\mathcal C_{\rm light}|\le\Delta V,
 \qquad
          M_{\rm light}=k|\mathcal C_{\rm light}|
             \le {2k\Delta\over a}V.                       \tag{8}
\]

For the collision statement, use the exact identity

\[
 \sum_{c\ne c'}|\mathcal A_c\cap\mathcal A_{c'}|
                  =\sum_Fd(F)(d(F)-1).                     \tag{9}
\]

Every heavy cell contributes more than `a/2` incidences on faces with
`d(F)>Delta`.  Since `d(F)-1>=Delta` for integer degrees,

\[
 \sum_Fd(F)(d(F)-1)
 \ge\Delta\sum_{F:d(F)>\Delta}d(F)
 \ge {\Delta a\over2}|\mathcal C_{\rm high}|,              \tag{10}
\]

which is (4).  Finally
`k/a=binom(2r,r)/4^r=Theta(r^(-1/2))` by Stirling.  QED.

There is no decoder loss in (3): degrees are the **actual aggregate** cube
overlaps over every root and carrier.  Choosing `Delta=o(sqrt r)` yields an
`o(V)` light bound, enough to eliminate a positive-mass light slice.  It does
not yield a fixed power of `n`, because every such `Delta` is `n^o(1)` on
`r=Theta(log n)`.

## 3. What one genuinely heavy anchor would give

Fix one ordinary face `F` of rank at most `q` and let

\[
                    \mathcal C(F)=\{c:F\in\mathcal A_c\}.  \tag{11}
\]

Every `F` contains the full root and carrier of every incident cell.  Let
`mathcal P_c={B_c union {x}:x in X_c}` be its singleton completion bank, with
`|X_c|=m_c`.

> **Lemma 2 (anchor-conditioned completion decoder).**
>
> \[
> \sum_{c\in\mathcal C(F)}m_c
>       \le L_{P|F}V,qquad
> L_{P|F}=q{b+1\choose2}.                                  \tag{12}
> \]

**Proof.**  Given a completion output `Y` and the fixed anchor `F`, guess the
retained root edge inside `Y` and the missing root label `z` inside `F`, not
among all `n` labels.  This determines `T`.  Actual role-pocket disjointness
then gives `{x}=Y cap X_T` and `B=Y setminus {x}`, hence the cell.  QED.

If `k_c=k` and `m_c>=m` on this anchor group, (12) yields

\[
       \sum_{c\in\mathcal C(F)}k
             \le {k\over m}q{b+1\choose2}V.                \tag{13}
\]

For `k=n^(kappa+o(1))`, `m=n^(1-o(1))`, and `q,b=O(log n)`, this is a
fixed-power gain whenever `kappa<1`.  The missing-root `n` loss has really
disappeared.

The quantifier is essential: (13) is for one fixed anchor.  Summing it over
all anchor faces would spend one copy of `V` per anchor.  The global theorem
forces many incidences of polylogarithmic degree, not one anchor supporting a
positive fraction of `V`.

## 4. Exact multi-root common-chain regression

Use the parabola cage from
`CIRCUIT_TRANSVERSAL_CENTRAL_LAYER_BARRIER.md`.  Let

\[
 p(t)=(t,1-t^2),\quad B=\{p(-1),p(1)\},                    \tag{14}
\]

and take a set `W` of `p=2r+1` rational points `p(t)` with
`|t|<=1/2`.  Put a general-position pocket `X` inside the common open
rectangle contained in every triangle `B union {w}`, `w in W`.

For every `z in W`, make a distinct cell

\[
 T_z=B\cup\{z\},\qquad U_z=W\setminus\{z\},qquad
 \mathcal F_z={U_z\choose r}.                              \tag{15}
\]

Every source is convex and every `T_z` is canonical.  The released cube is

\[
 \mathcal A_z=
 \{B\cup S:\varnothing\ne S\subseteq W,\ z\in S\}.        \tag{16}
\]

Consequently the exact aggregate degree is

\[
                         d(B\cup S)=|S|,                    \tag{17}
\]

and

\[
 \sum_Fd(F)=p2^{p-1},\qquad
 \sum_Fd(F)(d(F)-1)=p(p-1)2^{p-2}.                         \tag{18}
\]

For a fixed cell, more than half its outputs have
`|S|>r`; hence every cell is `r`-heavy.  This realizes the heavy side of
Theorem 1 with overlap `Theta(r)=n^o(1)`.

All cells have the **same** completion bank

\[
                         \mathcal P_z=\{B\cup\{x\}:x\in X\},
                                                               \tag{19}
\]

so its actual overlap is `2r+1`.  Moreover every `x in X` lies inside every
triangle `B union {w}`.  Thus any set retaining `B`, one pocket label, and
one outer label is nonconvex.  The shared cube outputs cannot be fused with
completion outputs, and distinct roots create no completion diversity.

For `r=Theta(log n)`, the total marked mass in this regression is only

\[
                         (2r+1){2r\choose r}=n^{O(1)}.       \tag{20}

It is therefore not the forbidden global `Theta(V)` configuration.  It does
prove that neither `n^o(1)` cube degree, many distinct roots inside a common
anchor, nor exact anchor-conditioned recovery alone implies the missing
fixed-power bank.  A successful global theorem must couple **different
anchors/carriers**, or use the fact that `Theta(V)` mass requires
`2^{Theta((log n)^2)}` such local groups.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_global_cube_prevalence_gate.py
```

The exact rational checker uses `|W|=9`, `r=4`, and five common pocket
labels.  It verifies all 630 marked source occurrences, 2,304 cube records,
the exact degree law `d(B union S)=|S|`, 511 distinct cube faces, and ordered
collision energy 9,216.  Every cell has 163 of its 256 outputs of degree
greater than four.  All 45 completion records collapse to five faces, and
every carrier/core/pocket mixed output is rejected by an explicit bad
four-subset.

