# Cross-anchor completion telescope

**Date:** 2026-08-15.  All logarithms are base two and the empty convex
subset is counted.

## Verdict

Grouping central cube cells by their **top face** gives a genuine global
Cauchy telescope: the top faces form a collision-free anchor bank, so the
conditional completion estimate can be summed without spending one copy of
`V` per anchor.

In a uniform central bin, put

\[
 s=2r,\qquad k={2r\choose r},\qquad |X_c|=m.               \tag{1}
\]

Let `R` be the maximum number of cells having one top face, let `lambda` be
the maximum multiplicity of a completion output **within** one top group,
and let `rho` be the maximum number of distinct top groups whose completion
sets contain the same ordinary face.  Then

\[
 \boxed{
             M\le k\sqrt{{\lambda R\rho\over m}}\;V(P).}   \tag{2}
\]

All roots, carriers, anchors, and completion collisions are charged in (2).
In particular, if

\[
 k=n^{\kappa+o(1)},\quad m=n^{1-o(1)},\quad
 R=n^{\alpha+o(1)},\quad \rho=n^{\beta+o(1)},              \tag{3}
\]

while `lambda=n^o(1)`, the bin closes with a fixed power whenever

\[
                         2\kappa+\alpha+\beta<1.            \tag{4}
\]

For `r=gamma log n`, `k=n^(2gamma+o(1))`, so the condition is
`4gamma+alpha+beta<1`.

There is also an exact first-divergence reduction.  A completion face shared
by `rho` distinct top groups contains a subfamily of
`rho/polylog(n)` groups with the same carrier, pocket label, and retained
root edge, but distinct missing root labels and distinct ordinary top-shield
faces.  This is a recoverable root-shield star.

The theorem does not close the high-`rho` star.  The multi-root parabola
regression lies in one top group (`R=Theta(log n)`, `rho=1`) and has only
polynomial marked mass.  A two-group version makes the cell-to-bank
comparison and the Cauchy step sharp before the final comparison with the
ambient `V`.  It is correctly discharged by global entropy whenever (4)
holds; it is not falsely declared locally impossible.  The remaining case
is now explicit: fixed-power cross-top completion overlap, or a central
entropy constant violating (4), together with `Theta(V)` marked mass.  No
such planar global regression is constructed here, and EIC' is not closed.

## 1. Top groups

For a complete central cell `c=(T_c,z_c,B_c)`, let `U_c` be its `2r`-label
core and

\[
 Q_c=B_c\cup\{z_c\}\cup U_c                              \tag{5}
\]

its top cube output.  The complete-layer union lift says `Q_c` is an ordinary
face.  Group cells by equality of the labelled face `Q_c`.  Let `mathcal Q`
be the set of nonempty groups and

\[
 N_Q=|\{c:Q_c=Q\}|,\qquad R=\max_QN_Q.                   \tag{6}
\]

The group keys themselves form the anchor bank

\[
                          \mathcal A=\{Q:Q\in\mathcal Q\}. \tag{7}
\]

It has exact overlap one and `|mathcal Q|<=V(P)`.

For each cell let

\[
 \mathcal P_c=\{B_c\cup\{x\}:x\in X_c\},                 \tag{8}
\]

and let `mathcal P_Q=union_(c:Q_c=Q) mathcal P_c` be the set
of distinct completion outputs in the group.  Define the actual overlaps

\[
\begin{aligned}
 \lambda&=\max_{Q,Y}
   |\{c:Q_c=Q,\ Y\in\mathcal P_c\}|,\\
 \rho&=\max_Y|\{Q:Y\in\mathcal P_Q\}|.                    \tag{9}
\end{aligned}
\]

Since every cell contributes `m` records,

\[
                         |\mathcal P_Q|\ge {mN_Q\over\lambda}.
                                                                    \tag{10}
\]

## 2. Exact decoder caps

Assume top and completion outputs have ranks at most `q` and `b+1`,
respectively.

> **Lemma 1 (within-anchor decoder).**
>
> \[
> \lambda\le q{b+1\choose2}.                               \tag{11}
> \]

**Proof.**  Fix `Q` and a completion output `Y`.  Guess the retained root
edge inside `Y` and the missing root label `z` inside `Q`.  This determines
`T`.  Actual pocket disjointness gives `{x}=Y cap X_T` and
`B=Y setminus {x}`.  The tuple `(T,z,B)` determines the cell.  QED.

> **Lemma 2 (cross-anchor decoder).**
>
> \[
> \rho\le n{b+1\choose2}.                                  \tag{12}
> \]

**Proof.**  Each membership `Y in mathcal P_Q` has at least one incident
cell.  Choose its canonical first cell.  The ordinary completion decoder,
which guesses the retained edge in `Y` and the missing label among all `n`
labels, recovers that cell and hence its top group.  QED.

The value in (12) is only a worst-case cap.  The point of (2) is to expose
the actual cross-top overlap `rho`; replacing it immediately by the
missing-root `n` loses the gain.

There is also an exact capacity bound on a top group:

\[
 R\le L_Q:=3{q\choose3}\sum_{i=0}^{b-2}{q-3\choose i}.     \tag{13}
\]

Indeed, inside a fixed `Q`, guess `T`, `z in T`, and the at most `b-2`
carrier labels outside `T`.  No core or cell count remains after
`(T,z,B)` is known.

## 3. One global Cauchy step

> **Theorem 3 (cross-anchor completion telescope).**  Equation (2) holds.

**Proof.**  The marked mass in group `Q` is `M_Q=kN_Q`.  By (10),

\[
 M_Q^2=k^2N_Q^2
 \le {k^2\lambda N_Q\over m}|\mathcal P_Q|
 \le {k^2\lambda R\over m}
       |\{Q\}|\,|\mathcal P_Q|.                            \tag{14}
\]

Put `K=k^2 lambda R/m`, sum square roots over all top groups, and apply
Cauchy:

\[
\begin{aligned}
 M
 &\le\sqrt K\sum_Q\sqrt{|\{Q\}|\,|\mathcal P_Q|}\\
 &\le\sqrt{K
       \left(\sum_Q|\{Q\}|\right)
       \left(\sum_Q|\mathcal P_Q|\right)}\\
 &\le\sqrt{K\,V(P)\,\rho V(P)}.
\end{aligned}                                               \tag{15}
\]

This is (2).  The same `V(P)` is used once in each of the two banks, globally
over all anchors.  QED.

For nonuniform central bins, dyadically split `r,k,m,q,b,N_Q` and the two
overlap variables.  On the live logarithmic-rank slice this costs
`n^o(1)` and leaves the exponent condition (4) unchanged.

## 4. High cross-anchor overlap gives a root-shield star

> **Lemma 4 (completion first divergence).**  Fix a completion face `Y`
> belonging to `h` distinct top groups.  There are at least
>
> \[
>             {h\over (b+1){b+1\choose2}}                  \tag{16}
> \]
>
> distinct groups with a common pocket label `x in Y`, common retained edge
> `e subseteq Y setminus {x}`, common carrier `B=Y setminus {x}`, and
> pairwise distinct missing root labels `z`.  Their top faces `Q_z` are
> distinct ordinary faces containing `B union {z}`.

**Proof.**  For each incident top group, choose its canonical first cell
emitting `Y`.  A cell specifies a pocket label `x in Y` and a retained edge
`e subseteq Y setminus {x}`.  There are at most the denominator in (16) such
pairs, so pigeonhole fixes `(x,e)` and therefore `B`.

If two remaining groups had the same `z`, then they would have the same
`T=e union {z}` and the same tuple `(T,z,B)`.  Canonicality would give the
same cell and hence the same top group, a contradiction.  Thus the `z` and
the labelled top faces are distinct.  QED.

In the planar root-pocket role, `{e,z,x}` is a bad `3+1` circuit: `x` is
inside the root triangle.  Hence (16) is an oriented root-shield star, not
merely a list of set-system anchors.  Its shield outputs `Q_z` have overlap
one as group keys.  What is still missing is a second ordinary-face bank
whose size grows with the star while retaining bounded global overlap.

## 5. Mandatory parabola regression

The multi-root construction from `GLOBAL_CUBE_PREVALENCE_GATE.md` has one
top face

\[
                         Q=B\cup W,\qquad |W|=2r+1.        \tag{17}
\]

There is one cell for every `z in W`, so

\[
 R=2r+1,\qquad \lambda=2r+1,\qquad \rho=1.               \tag{18}
\]

All cells have the same `m` singleton completion outputs, and no completion
mixes with any nonempty core choice.  Equation (2) becomes

\[
 M\le {k(2r+1)\over\sqrt m}V(P),                           \tag{19}
\]

using the actual overlaps.  This is not a local contradiction: the actual
marked mass is only `(2r+1)k=n^O(1)`.  In a live `Theta(V)` slice, (19)
would instead discharge this profile whenever `4gamma<1`, up to
`n^o(1)` factors.  For larger central entropy constant it honestly remains.

The verifier also uses two disjoint outer chains with two distinct top
faces, the same carrier, and the same completion bank.  Each group contains
nine root cells.  Then `R=lambda=9`, `rho=2`; the local square comparison and
the Cauchy step are equalities when actual overlaps replace the decoder caps.
Thus the pre-`V` telescope has the correct multiplicities and does not
secretly spend one ambient face count per top group.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_cross_anchor_completion_telescope.py
```

The exact rational checker constructs two top groups on disjoint nine-point
parabola chains.  It verifies 18 canonical cells and 1,260 marked source
occurrences, the common five-output pocket bank, actual overlaps
`R=lambda=9`, `rho=2`, the conditioned decoder cap, and the sharp identity

\[
 1260^2=
 \left({70^2\cdot9\cdot9\over5}\right)(2)(10).             \tag{20}
\]

It also checks the first-divergence root-shield star and rejects every
carrier/core/pocket mixed output.
