# Kruskal--Katona plus four-locality: a fixed-tangent transversal regression

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The proposed dichotomy is false, even after retaining the complete tangent
cell, repair mark, shield, and common prefix.  A scalable planar radial
family gives an `r`-uniform petal system

\[
              \mathcal T_{r,L}=X_1*\cdots*X_r,
              \qquad |X_i|=L,\qquad |\mathcal T_{r,L}|=L^r,       \tag{1}
\]

in which every transversal `D` makes `B union D` convex, while

\[
                 B\cup D\cup D'\quad\hbox{is nonconvex}          \tag{2}
\]

for every two distinct transversals.  Here `B` contains the fixed tangent
guards and the actual marked repair data are held fixed outside the petal.

This family has the smallest possible kind of proper shadow for the
desired conclusion.  At level `k`,

\[
 |\partial_k\mathcal T_{r,L}|={r\choose k}L^k,
 \qquad
 d(I)=L^{r-k},                                             \tag{3}
\]

and its entire proper downclosure has

\[
 |\Delta^*\mathcal T_{r,L}|=(L+1)^r-L^r,qquad
 { |\Delta^*\mathcal T_{r,L}|\over|\mathcal T_{r,L}|}
       =(1+L^{-1})^r-1.                                   \tag{4}
\]

For `r=kappa log n` and `L=n^delta`, (4) is
`n^{-delta+o(1)}`.  Thus the proper shadow contracts by a fixed power; it
does not expand.

Planar four-locality does not supply the other branch.  Call a support
`S` a Boolean shield when `B union S` is convex.  By (2), one Boolean
shield contains at most one member of `mathcal T_(r,L)`.  The same is true
of every source layer on `S` which covers all four-traces: the standard
four-locality lemma would make `B union S` convex.  Consequently every
cover of (1) by complete or four-trace-covering near-complete layers needs
at least

\[
                              L^r                              \tag{5}
\]

support tags.  Its tag entropy is `r log L`.  On the live scaling this is
`delta kappa (log n)^2`, not subquadratic.

The obstruction is globally sharp as an incidence system.  The Boolean
banks of the `L^r` singleton shields have union exactly `(L+1)^r`; at
rank `k` every output is reused by exactly `L^(r-k)` shields.  Repeating
the context with arbitrary weights multiplies incidence and overlap by
the same factor.  Making contexts disjoint multiplies both source mass and
face capacity by the same factor.  Hence neither low nor high cross-context
overlap restores a fixed-power gain from these banks.

This is a kill of **KK stability plus unoriented planar four-locality**, not
an EIC' counterexample.  The radial construction is paid by its oriented
one-gap/container shields.  Any positive theorem must therefore recognize
the first-divergence block and its local directional profile; small shadow
cannot force near-complete four-cover structure.

## 1. Exact set-system calculation

Let `X_1,...,X_r` be disjoint `L`-sets and let `mathcal T_(r,L)` consist of
sets choosing exactly one point from each block.  A `k`-subset lies below a
transversal precisely when it chooses `k` distinct blocks and one value in
each.  There are `binom(r,k)L^k` such subsets, and the remaining `r-k`
coordinates can be filled in `L^(r-k)` ways.  This proves (3), including
the exact first-moment identity

\[
 |\mathcal T_{r,L}|{r\choose k}
   =|\partial_k\mathcal T_{r,L}|L^{r-k}.                  \tag{6}
\]

The full downclosure consists of partial transversals.  Its rank generating
polynomial is `(1+Lz)^r`; deleting the top coefficient gives (4).
If `r/L=o(1)`, then

\[
 (1+L^{-1})^r-1=(1+o(1)){r\over L}.                       \tag{7}
\]

In particular, with `r=kappa log n`, `L=n^delta`,

\[
 \log|\mathcal T_{r,L}|=\delta\kappa(\log n)^2,
 \qquad
 { |\Delta^*\mathcal T_{r,L}|\over|\mathcal T_{r,L}|}
          =n^{-\delta+o(1)}.                              \tag{8}
\]

This simultaneously has quadratic source entropy and fixed-power shadow
contraction.  It is therefore a direct counterexample to any abstract
statement of the form “far from a complete layer implies fixed-power
proper-shadow expansion.”

## 2. Why every four-cover group is a singleton

The planar input can be stated without reference to the construction.

> **Lemma 1 (four-cover union lift).**  Let `B` be convex, let
> `mathcal G subseteq {S choose r}`, `r>=4`, and suppose every
> `B union R`, `R in mathcal G`, is convex.  If every four-subset of `S`
> lies in some `R in mathcal G`, then `B union S` is convex.

**Proof.**  If `B union S` were nonconvex, planar Caratheodory would give a
bad set `C` of at most four points.  Extend `C cap S` to a four-subset
`E subseteq S`, choose `R in mathcal G` with `E subseteq R`, and obtain
`C subseteq B union R`, contradicting convexity.  QED.

The same proof handles bad four-sets meeting `B`: covering four variable
labels lets one extend their variable trace before selecting `R`.

Now assume (2), and let a complete or near-complete group on support `S`
meet the four-cover threshold.  Lemma 1 makes `B union S` convex.  If it
contained distinct `D,D' in mathcal T_(r,L)`, deletion would make
`B union D union D'` convex, contradicting (2).  Thus the group covers at
most one transversal.  Equation (5) follows.

Notice that this is stronger than saying the family is far from complete
on its full support.  There is no decomposition into
`2^{o(r log L)}` complete or threshold-near-complete sublayers on smaller
supports.  Even allowing arbitrary convex supports cannot reduce the
cover number.

## 3. Actual fixed-tangent planar realization

Use the radial repair-star configuration from
`TANGENT_MARKED_SHIELD_DESCENT.md`.  Start with `q` cyclic radial blocks,
fix representatives in the four blocks around the repair insertion, fix
the repair point `p`, and fix an internal shield face `F` containing `p`.
Put all fixed tangent guards in `B`.  The remaining `r=q-4` blocks are the
`X_i` above.

The radial nesting inequalities give exactly:

1. every choice of one representative per active block completes `B` to a
   convex carrier and to the same marked repair star; and
2. the union of two distinct choices is nonconvex, witnessed at their
   first differing radial block.

The inequalities are open, so each finite `(r,L)` instance can be put in
general position by sufficiently small rational perturbations.  Taking
`q=Theta(log n)` and `L=n^delta` gives (8) while retaining the same tangent
cell and actual `(p,F)` throughout.  This is the scalable construction
already used for the marked omitted-petal barrier; the present point is
that its complete shadow and four-cover statistics kill the proposed
stability dichotomy as well.

The exact rational audit uses eight two-point blocks.  After fixing blocks
`7,0,1,2`, its four active binary blocks give `r=4`, `L=2`, and sixteen
petals.  Exhaustive orientation tests verify that every carrier is convex,
every pairwise union is nonconvex, and no `B`-convex support contains two
petals.  Exhausting all `2^16-1` nonempty petal subfamilies verifies that
the only four-trace-covering subfamilies are singletons.

## 4. Global overlap is exactly the erased alphabet

For each petal `D`, its Boolean shield is the bank

\[
                     \mathcal B_D=\{B\cup I:I\subseteq D\}.         \tag{9}
\]

Their union consists of all partial transversals and has size `(L+1)^r`.
At rank `k`, the exact load is

\[
 \left|\{D:B\cup I\in\mathcal B_D\}\right|=L^{r-k}.       \tag{10}
\]

Thus double counting the singleton-shield banks gives equality:

\[
 L^r{r\choose k}
   =\bigl({r\choose k}L^k\bigr)L^{r-k}.                   \tag{11}
\]

There is no hidden decoder saving.  The omitted `r-k` block values are
exactly both the support-tag ambiguity and the face overlap.

More generally, give copies of the same context nonnegative weights
`w_c`, and let `W=sum_c w_c`.  Then every rank-`k` output has weighted load
`WL^(r-k)`, while total weighted bank incidence is
`WL^r binom(r,k)`.  Equation (11) remains equality after multiplying by
`W`.  At the opposite extreme of disjoint geometric contexts, both sides
and the number of available ordinary outputs scale by the number of
contexts.  Hence global Cauchy, Hall pruning, or weighted replication
cannot improve this local ratio without using a second, oriented bank.

## 5. Exact boundary

The regression rules out the desired conclusion under each of the proposed
inputs:

* the family is `r`-uniform and has quadratic logarithmic entropy;
* its whole proper downshadow is smaller by a fixed power;
* the full tangent state, repair mark, shield, and base are fixed;
* planar nonconvexity is witnessed by four-circuits; and
* any four-covering or convex-support group contains only one source.

What distinguishes it from a genuine hard EIC' counterexample is cyclic
orientation.  Its first differing block has a large local alphabet and the
radial one-gap theorem converts that alphabet into ordinary shield faces.
Therefore a viable replacement for KK stability is an **oriented
first-divergence dichotomy**:

> either a large subfamily is four-covering on a common support, or a
> canonical uncovered four-trace localizes a first-divergence block whose
> alphabet/profile bank is charged before the downshadow erases it.

Unoriented shadow size, even with planar four-locality and global overlap
bookkeeping, cannot make this distinction.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_kk_four_local_stability_regression.py
```

The checker reuses the exact rational radial order type and verifies the
sixteen-petal fixed-tangent regression, every shadow/load formula, the
four-cover singleton classification, the union of all Boolean banks, and
the scalable fixed-power contraction formula with exact integers.
