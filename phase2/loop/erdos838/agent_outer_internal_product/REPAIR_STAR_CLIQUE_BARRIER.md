# Repair stars: exact injection, overlap cutoff, and a maximal-clique barrier

**Date:** 2026-08-14.  All logarithms are base two.

## Verdict

Let `B` be a common base, let `Q_1,...,Q_M` be distinct rank-`q`
completions whose pairwise unions are nonconvex even after `B` is deleted,
and suppose every `Q_i` has `D` one-point repairs `Y_i`:

\[
             B\cup Q_i\cup\{y\}\in\mathcal F(P)
             \qquad(y\in Y_i).                            \tag{1}
\]

The repaired stars `Q_i union {y}` are automatically distinct, so (1)
gives exactly `DM` recoverable ordinary faces.  This is one honest factor
of `D`.

Circuit connectivity alone cannot force a second factor while the output
retains the whole completion support.  There are scalable planar
configurations with `M=L^q`, a **common** repair alphabet `Y` of size `D`,
and the following strongest possible obstruction:

* all `DM` repaired stars are maximal convex faces;
* the union of every two distinct repaired stars is nonconvex; and
* the only convex faces meeting every active completion block and the
  repair block are the `DM` stars themselves.

Thus the incompatibility graph on repaired stars is a clique, yet its
full-support convex capacity is exactly `DM`.  Star links, pair circuits,
maximality, or a Bollobas-pair argument cannot by themselves manufacture a
fixed-power gain beyond `D` in a base/support-retaining bank.

This is **not** a counterexample to global EIC'.  In the displayed
realization each radial cluster, including the repair alphabet, is itself
in convex position and supplies a huge unrestricted Boolean shield.  Such
faces erase the completion support and may be reused across many
common-base cells.  Summing that nonlocal capacity with controlled overlap,
not finding additional local repaired stars, remains the global problem.

## 1. The exact repaired-star injection

Call two completions detached-incompatible if `Q_i union Q_j` is not in
convex position.

> **Lemma 1 (repair-star injection).**  Under (1), if the completions are
> pairwise detached-incompatible, then the `DM` sets
> \[
>                    Q_i\cup\{y\},\qquad y\in Y_i,          \tag{2}
> \]
> are pairwise distinct ordinary faces.

**Proof.**  They are ordinary by deletion from (1).  Sets with the same
`Q_i` are distinct because the repairs are distinct and disjoint from the
completion.  If

\[
                    Q_i\cup\{y\}=Q_j\cup\{z\},             \tag{3}
\]

then `Q_i union Q_j` is a subset of the ordinary face in (3), hence is
ordinary.  This contradicts detached incompatibility.  QED.

No assumption about overlap among the alphabets is needed.  In particular,
all completions may use the same `D` labels.

## 2. What alphabet diversity does pay

Let

\[
 U=\bigcup_iY_i,\qquad
 \rho=\max_{y\in U}|\{i:y\in Y_i\}|.                       \tag{4}
\]

Write `h(N)` for the minimum number of ordinary convex subsets of an
`N`-point planar general-position set.

> **Lemma 2 (repair-overlap cutoff).**  Every cell as above satisfies
> \[
> V(P)\ge\max\left\{DM,
>                   h\left(\left\lceil{DM\over\rho}\right\rceil\right)
>             \right\}.                                   \tag{5}
> \]

**Proof.**  Lemma 1 gives the first term.  Double-counting the incidences
`(i,y)` gives `|U|>=DM/rho`.  Every convex subset of the induced point set
`U` is an ordinary face of `P`, proving the second term.  QED.

Using the established safe reservoir estimate

\[
                        h(N)\ge2^{(\log N)^2/8}             \tag{6}
\]

for sufficiently large `N`, (5) closes a local target
`V(P)>=D^(1+epsilon)M` whenever

\[
 {1\over8}\left(\log{DM\over\rho}\right)^2
       \ge \log M+(1+\epsilon)\log D.                      \tag{7}
\]

The hard case is the opposite extreme `rho=M`: one common alphabet is
reused by every completion, and (5) reduces to `max{DM,h(D)}`.  The next
construction realizes exactly this extreme together with complete circuit
connectivity.

Lemma 2 is local.  Across EIC' cells, the same induced shield `U` can occur
in many bases, so the second term in (5) cannot be summed without a global
overlap or recoverability theorem.

## 3. A scalable repair-star clique

> **Theorem 3 (radial completion/repair barrier).**  For all
> `q>=4`, `L>=2`, and `D>=2`, there is a planar general-position set
> \[
>               P=X_0\mathbin{\dot\cup}\cdots
>                    \mathbin{\dot\cup}X_{q-1}
>                    \mathbin{\dot\cup}Y,
>        \qquad |X_i|=L,\quad |Y|=D,                       \tag{8}
> \]
> with `M=L^q` rank-`q` completions
> \[
>           Q_t=\{x_{0,t_0},\ldots,x_{q-1,t_{q-1}}\},      \tag{9}
> \]
> such that:
>
> 1. the `Q_t` are pairwise detached-incompatible;
> 2. every `Q_t union {y}`, `y in Y`, is convex;
> 3. every two distinct faces in item 2 have nonconvex union;
> 4. every face in item 2 is maximal in `P`; and
> 5. a convex face meeting all `q+1` blocks in (8) contains exactly one
>    point from each block.  Consequently there are exactly `DM`
>    full-support faces.

**Construction and proof.**  Begin with a strictly convex `q`-gon.  In a
sufficiently small inward radial neighborhood of each vertex put an
`L`-point strict nesting chain `X_i`.  Arrange the scales so that every
transversal is strictly convex and, for any two points of `X_i`, the inner
one lies strictly inside the triangle formed by the outer one and arbitrary
representatives of the two neighboring active clusters.  This is the
standard radial-cluster construction: all conditions are finitely many
open strict orientation inequalities.

Next choose an edge between the neighborhoods `X_0,X_1`.  In a sufficiently
small exterior ear beyond that edge put a `D`-point strict nesting chain
`Y`.  Every one-point ear insertion extends every active transversal.
Choose the repair scales so that, for any two repair points, the inner one
lies strictly inside the triangle formed by the outer one and arbitrary
representatives of `X_0,X_1`.

A generic rational perturbation inside the same open orientation cell
makes the whole set general position.  The active nesting certificate
shows that two different `Q_t` have nonconvex union.  Hence two repaired
stars with different completions also have nonconvex union.  If their
completions agree but their repair labels differ, the repair-ear triangle
is a bad four-circuit.  This proves items 1--3.

Adding any unused active point to a repaired star creates the active
four-circuit; adding any unused repair point creates the repair-ear
four-circuit.  Thus every star is maximal.  Finally, a full-support set
with two points from an active block or from the repair block contains the
corresponding bad circuit.  It therefore uses at most one point per block,
which proves item 5 and the exact count `L^qD=MD`.  QED.

One may add any fixed common base `B` by sufficiently small independent
outer-ear insertions and include it in every repaired carrier.  Taking
`B=emptyset`, already allowed by (1), gives the literal maximal-face
statement above.

The theorem is quantitatively on the live scale.  With

\[
          L=\lfloor D^\delta\rfloor,
          \qquad q=\lfloor\kappa\log D\rfloor,             \tag{10}
\]

one has

\[
             \log M=(\delta\kappa+o(1))(\log D)^2,         \tag{11}
\]

while the full-support repaired-star capacity remains exactly `DM`.  Thus
even a quadratic-entropy, circuit-complete child need not contain a second
rooted repair factor.

## 4. Exact rational audit

The verifier uses four active two-point blocks and a three-point repair
block.  Its active coordinates are

\[
\begin{array}{c|cc}
X_0&(-2,-2)&(-9/5,-3/2)\\
X_1&(2,-2)&(17/10,-9/5)\\
X_2&(2,2)&(9/5,17/10)\\
X_3&(-2,2)&(-17/10,9/5),
\end{array}                                                \tag{12}
\]

and

\[
Y=\left\{
 (2/23,-1282/575),
 (2/13,-734/325),
 (6/29,-1658/725)
\right\}.                                                  \tag{13}
\]

There are `M=16` completions and `DM=48` repaired stars.  Exact determinant
checks give:

* all 48 stars convex and maximal;
* all `binom(48,2)=1128` distinct star-pair unions nonconvex;
* exactly 48 full-support convex faces; and
* full ordinary-face profile
  \[
       (1,11,55,165,220,112,0,0,0,0,0,0),\qquad V(P)=564. \tag{14}
  \]

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_repair_star_clique_barrier.py
```

The audit is deliberately finite and exact.  The scalable theorem uses
only the same open strict inequalities.

## 5. Consequence for the live residue

The first `D` factor is real and globally useful because every repaired
star recovers its completion and repair label.  Theorem 3 shows that the
following proposed upgrades are false without an unrooted output:

1. pairwise completion circuits force compatible pairs of repaired stars;
2. connected circuit witnesses force a second extension in a star link;
3. maximal repaired faces admit an additional rooted Bollobas capacity;
4. quadratic completion entropy alone forces more than `DM` faces retaining
   every completion coordinate.

The live global EIC' target must therefore combine the `DM` star bank with
an **unrestricted** shield bank, such as the faces internal to a repeatedly
used radial cluster or repair alphabet, and control the product of their
global overlaps.  The construction is a local-capacity barrier, not a
global counterexample: here `Y` itself is in convex position and already
gives `2^D` ordinary faces.
