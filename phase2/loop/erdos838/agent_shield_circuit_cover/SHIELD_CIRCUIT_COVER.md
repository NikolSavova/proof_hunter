# Erdős 838: circuit transversals release the mixed shield bank

**Date:** 2026-08-14.  All logarithms are base two.

## Verdict

The concentrated-circuit branch has an exact positive theorem.  If the
outer traces of all bad `2+2` and `1+3` circuits in a contextual cell have
a transversal of size `t`, deleting that transversal makes the *entire*
internal reservoir compatible.  The deleted labels cost only

\[
                         L_t=\sum_{i=0}^t {n\choose i}       \tag{1}
\]

in global overlap.  Thus a common reservoir of size `H` pays `D^2` records
per context whenever

\[
                         H/L_t\ge D^{2+2\epsilon}.           \tag{2}
\]

In particular, at the seam `n=D^(2+o(1))`, the bank
`H=2^((1/5-o(1))(log D)^2)` absorbs every transversal of size at most
`(1/25)log D` with superpolynomial room.

This does not finish the circuit branch.  If the transversal is larger,
the outer traces contain `Omega(log D)` pairwise disjoint members.  This
alternative is real even when all internal points lie in one common
one-point-extension region.  An exact rational double-parabola family has
one bad `1+3` circuit with outer trace `{z}` for every outer carrier vertex
`z`; its minimum transversal is the whole carrier.  Taking rank-`r`
subsets of a `D`-point outer parabola gives

\[
                       {D\choose r}=2^{\Theta(r\log D)}      \tag{3}
\]

contexts with the same phenomenon.  The example is harmless because the
outer parabola is itself in convex position and supplies `2^D` faces.  It
kills the overstrong claim that planarity, one-point compatibility, or a
common insertion side forces a small circuit cover.

There is a second exact reduction in the large-transversal branch: a
matching of outer traces canonically produces a Boolean **outer shield**.
Either its middle layer has low context overlap, or one macroscopic outer
face is shared by many contexts.  What remains is to multiply that outer
shield by the already-banked internal shield without assuming their union
is convex.  This is a narrower two-shield problem, but it is still open.

## 1. The circuit-transversal release theorem

Let the ambient labels have a fixed decoder partition

\[
                              P=O\mathbin{\dot\cup}X.        \tag{4}
\]

For each contextual cell `c`, let `R_c subset O` be a distinct ordinary
convex face.  Let `mathcal H subset F(P)` be a common reservoir of `H`
ordinary faces contained in `X`.  Assume one-point compatibility:

\[
             R_c\cup\{x\}\in F(P)
       \quad\text{for every }c\text{ and }x\in\bigcup\mathcal H. \tag{5}
\]

For a nonconvex four-set `T union S`, with `T subset R_c` and `S subset X`,
call `T` its outer trace.  Under (5), every split circuit relevant to some
`F in mathcal H` has

\[
               (|T|,|S|)=(2,2)\quad\hbox{or}\quad(1,3).     \tag{6}
\]

Let `mathcal T_c` be the family of all such outer traces, and suppose
`G_c subset R_c`, `|G_c|<=t`, meets every member of `mathcal T_c`.

> **Theorem 1 (transversal release).**  Every face in the common reservoir
> becomes compatible after deleting the guard transversal:
> \[
>                  (R_c-G_c)\cup F\in F(P)
>                       \qquad(F\in\mathcal H).              \tag{7}
> \]
> The mixed banks
> \[
>        \mathcal M_c=\{(R_c-G_c)\cup F:F\in\mathcal H\}    \tag{8}
> \]
> have size `H` and maximum global overlap at most `L_t` from (1).

**Proof.**  If the union in (7) were nonconvex, planar Caratheodory would
give a nonconvex four-subset.  It cannot lie on one side of (4), because
both sides used in the union are faces.  It cannot have three outer points
and one internal point, because it is a subset of the face in (5).  Its
outer trace therefore has size one or two and belongs to `mathcal T_c`.
But this trace is contained in `R_c-G_c`, contradicting that `G_c` hits
every member of `mathcal T_c`.

The partition (4) recovers `F=U\cap X` and `R_c-G_c=U\cap O` from a mixed
output `U`.  Recovering `R_c` now requires only the choice of at most `t`
deleted ambient labels.  Since the carriers are distinct, the number of
possible cells is at most (1).  QED.

The theorem plugs directly into a two-bank square telescope.  Suppose cell
`c` has record mass `w_c` and use the singleton first bank `{R_c}`.  The
first banks have overlap one, while (8) has overlap at most `L_t`.  If
`w_c=D^2` for all cells, then

\[
       w_c^2=D^4={D^4\over H}|\{R_c\}|\,|\mathcal M_c|.
\]

Cauchy over all cells gives the exact global estimate

> **Corollary 2 (small-cover discharge).**
> \[
>                  \boxed{\ |G|\le D^2\sqrt{L_t/H}\,V(P).\ } \tag{9}
> \]
> Consequently (2) implies
> `|G|<=D^(1-epsilon)V(P)`.

No context count occurs in (9): the released outer remainder tags the
internal face, and its only reuse is the explicit deleted-label factor
`L_t`.

For the seam calculation, put `ell=log D`, `n=D^(2+o(1))`, and
`t<=ell/25`.  The standard estimate

\[
  \log L_t\le t\log(en/t)\le(2/25+o(1))\ell^2             \tag{10}
\]

combined with `log H>=(1/5-o(1))ell^2` makes `H/L_t`
superpolynomial in `D`.  Thus (2) holds for every fixed `epsilon` once
`D` is sufficiently large.

## 2. Failure of a small cover forces an outer shield

Regard `mathcal T_c` as a graph on `R_c`, allowing singleton edges.  Let
`tau_c` be its vertex-cover number.  The endpoints of a maximal matching
form a vertex cover, so

\[
                   \nu_c\ge\tau_c/2,                       \tag{11}
\]

where `nu_c` is the maximum number of pairwise disjoint outer traces.
Thus failure of Theorem 1 at `t=gamma log D` supplies a matching of
`Omega(log D)` disjoint traces.

There is a useful overlap dichotomy which uses no additional geometry.
Fix `s` and a family `mathcal C` of cells with `nu_c>=s`.  Choose the first
`s` traces in a canonical maximum matching and one canonical vertex from
each trace.  Their representatives form an `s`-set `K_c subset R_c`.
Because `R_c` is a face, so is `K_c`, and every subset of `K_c` is an
ordinary face.  Put

\[
       Q_s={s\choose\lfloor s/2\rfloor},\qquad
       \Delta_s=\max_Q|\{c:Q\subset K_c,\ |Q|=\lfloor s/2\rfloor\}|.
                                                                    \tag{12}
\]

> **Theorem 3 (matching-to-outer-shield reduction).**
> \[
>                    Q_s|\mathcal C|\le\Delta_s V(P).       \tag{13}
> \]
> Hence either the middle-layer banks have low overlap, or one ordinary
> outer shield of rank `floor(s/2)` is shared by `Delta_s` actual
> contexts.

This is just double counting the pairs `(c,Q)` with `Q subset K_c`.
For `s=gamma log D`, the bank size is
`Q_s=D^(gamma-o(1))`.  The conclusion is structurally parallel to the
selected-neighbourhood shield theorem, now on the outer side.  Equation
(13) alone does not pay the `D^2` records in a cell; it identifies the
precise object which a completion of the matching branch must couple to
the internal reservoir.

## 3. A rational large-transversal regression

The matching alternative cannot be dismissed geometrically.  Fix `M>=3`,
put `h=10M^2` and `eta=1/10`, and define

\[
 \begin{split}
       z_i&=(i,i^2-M^2),\\
       x_i&=(i,h+\eta i^2),\qquad -M\le i\le M.
                                                               \tag{14}
 \end{split}
\]

The outer set `Z={z_i}` and internal set `X={x_i}` are both in convex
position.  Moreover every `x_i` is a one-point extension of the complete
outer face `Z`, hence of every subface of `Z`.  One way to see the latter
is to support each `z_j` by the tangent to the lower parabola; all internal
points lie strictly above every such tangent, while `x_i` has an upper
supporting line.

For every `-M<i<M`, the point `x_i` lies strictly inside

\[
                         \operatorname{conv}
                         \{z_i,x_{i-1},x_{i+1}\}.            \tag{15}
\]

Indeed the midpoint of `x_(i-1)x_(i+1)` is
`(i,h+eta(i^2+1))`; the point `x_i` lies on the open segment from `z_i`
to that midpoint.  Thus `{z_i}` is a bad `1+3` outer trace.  Any
transversal contains every one of the `2M-1` interior outer labels.

More generally, let a context carrier be any rank-`r` subset of the
interior outer labels.  Its trace hypergraph contains a singleton edge at
every carrier label, so

\[
                  \tau_c=\nu_c=r,qquad
                  C={2M-1\choose r}.                        \tag{16}
\]

Taking `2M-1=D` and `r=Theta(log D)` makes `log C=Theta((log D)^2)`.
All inequalities are strict, so a sufficiently small generic rational
perturbation supplies general position if it is ever needed.  The finite
verifier below already has no collinear triples at its audited values.

The construction is not a counterexample to the desired face bound:
`Z` itself contributes `2^(2M+1)` ordinary faces.  It proves that the
large matching must be converted into such an unrestricted outer shield
by a global low-`V` argument; it cannot be ruled out by a local insertion
lemma.

## 4. Exact remaining statement

Combining Theorems 1 and 3 leaves the following precise target.

> In a low-`V` hard slice with quadratic context entropy, if
> `Omega(log D)` disjoint outer traces occur in most cells, then the
> resulting context-correlated outer Boolean shields and the common
> internal reservoir create enough ordinary mixed faces, or their cross
> circuits generate a third shield with fixed-power surplus.

The double-parabola regression shows why the conclusion must be phrased as
a surplus theorem: the matching itself is possible, but every known dense
realization visibly pays through a large outer convex cloud.  A proof still
has to charge that cloud when the carriers overlap irregularly.  A plain
ambient-label pigeonhole, or an assertion that two common tangent guards
hit all `1+3` circuits, is false.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_shield_circuit_cover.py
```

The checker audits the exact Cauchy inequality in (9), exhausts small
deleted-guard overlap systems, verifies the rational double-parabola hulls
and every singleton witness in (15), computes the exact minimum trace
cover, and checks (13) on exhaustive small matching-shield incidence
systems.
