# Three root-to-infinity charts: exact compatibility and a deletion-shield barrier

**Date:** 2026-08-15. This continues
`CRITICAL_EDGE_DISPERSION_RECHART_LEDGER.md`.

## Verdict

Root-to-infinity charts have a rigid synchronization law. A projective
chart has one preimage of the line at infinity. Therefore three prescribed
root/tangent charts can be used simultaneously if and only if their three
separating lines are the same physical projective line. If the tangent
line is not prescribed and only the three roots must go to infinity, this
is possible if and only if the roots are collinear.

Consequently three distinct physical roots in general position **never**
admit one common root-to-infinity chart. The large endpoint surplus exposed
separately by each root cannot simply be inserted into a cyclic three-cloud
product. This is an actual projective obstruction, not a polynomial chart
label.

There is a scalable stretchable regression realizing the obstruction at
the critical carrier interface. Start with the complete cap-by-cup carrier
rectangle from the preceding report. Replace its omitted upper role by an
arbitrary low-rank general-position order type `Q`, affinely squeezed into
one universal dominance cage, and partition `Q` into three macroscopic
named root clouds. Then:

* every carrier plus every singleton root is ordinary, with load one;
* every carrier plus any two roots is nonordinary, including cross-cloud
  pairs;
* every physical cage-edge fibre has relative density `D^{-2}`;
* any three roots, one from each named cloud, have incompatible charts;
* the intrinsic order type and face bank of `Q` are unchanged; and
* every ordinary face using at least two roots and outside carrier labels
  must delete one of the two complete neighbouring role clouds.

The last item is an exact global two-shield cover, not a selected-word
heuristic. At the carrier-word level each deletion loses a factor `D`, and
the remaining mixed traces are precisely one-ended cap/cup profiles of
`Q`. Thus all detached escapes are exposed as actual deletion/profile
banks. They may pay in a minimizer; they do not follow merely from chart
incompatibility.

This kills the proposed unconditional implication

```text
incompatible root charts => cyclic profile bank.
```

The correct next implication must be

```text
incompatible charts => profile-change bank OR a weighted deletion-shield
descent that preserves the physical (B,z) history mass.
```

No coefficient-half closure is claimed.

## 1. Compatibility of projective tangent charts

A projective affine chart is specified by its line at infinity. If `T` is
a projective transformation, write

\[
                         L_T=T^{-1}(L_\infty).                    \tag{1}
\]

> **Theorem 1 (chart synchronization).** For `i=1,2,3`, let `z_i` be a
> root and let $\ell_i$ be the separating tangent line through `z_i` used
> by its root-to-infinity normalization.
>
> 1. One projective map realizes all three prescribed normalizations if
>    and only if
>    \[
>                              \ell_1=\ell_2=\ell_3.              \tag{2}
>    \]
> 2. If the lines may be chosen freely, one projective map sends all three
>    roots to infinity if and only if `z_1,z_2,z_3` are collinear.
> 3. Allowing a different affine postcomposition after the common map does
>    not weaken either condition.

**Proof.** A projective map has exactly one preimage line `L_T` of
$L_\infty$. A prescribed root normalization sends $\ell_i$ to
$L_\infty$, so all three can occur precisely when each $\ell_i=L_T$.
This proves (1). Without prescribed lines, all roots go to infinity
precisely when they all lie on `L_T`, proving (2). An affine
postcomposition fixes $L_\infty$ setwise and therefore leaves `L_T`
unchanged. QED.

For two roots the line joining them is the only candidate common tangent
line. It is usable only if the two carrier union supports lie in their
required affine sides. For three general-position roots there is no
candidate at all.

This theorem concerns simultaneous *profile composition*. Each separate
projective map still preserves the ordinary-face complex of its own cloud.
The error is to multiply profiles exposed in three different affine charts
as though their cap/cup directions described one common exterior seam.

## 2. Weighted physical-incidence scope

Keep the weighted notation of the preceding ledger. For root cloud `i`,
let

\[
 I_i=\{(B,z):z\in X_i,\ B\cup\{z\}\text{ ordinary}\}.           \tag{3}
\]

After physical colouring, the map $(B,z)\mapsto B\cup\{z\}$ is injective,
so

\[
                 V(P)\ge\left|\bigcup_i I_i\right|.              \tag{4}
\]

For weighted histories put

\[
 \Lambda_i=\max_{B,z\in X_i}
       \sum_{\omega:(B_\omega,z_\omega)=(B,z)}w_\omega.         \tag{5}
\]

Then the contribution of cloud `i` is at least $W_i/\Lambda_i$. No chart
argument changes this exact load. In particular, the regression below has
$\Lambda_i=1$; its obstruction is not duplicate metadata.

If a positive proof produces a profile-change output, it must likewise
retain enough physical information to recover `(B,z)` or state its actual
aggregate load. A direction/chamber identifier alone is not a face and
cannot serve as the missing decoder.

## 3. Three-cloud universal-cage regression

Use the macro construction of the critical-dispersion report. There are
fixed endpoint roles `l,r`, upper carrier roles with immediate neighbours
`Y,W` around one omitted role, and lower carrier roles. Every carrier word
`B` is the union of a cap and cup with common endpoints `l,r`.

Let `Q` be any rational general-position order type of size `D` and maximum
ordinary-face rank `O(log D)`. Apply the affine universal-dominance squeeze
inside the omitted role. Since the neighbour clouds are infinitesimal,
for every `y in Y`, `w in W`, and every ordered pair `x<x'` in the
dominance order,

\[
                         x\in\operatorname{int}\triangle(y,w,x'). \tag{6}
\]

The affine map preserves every intrinsic orientation sign of `Q`.
Partition its labels into three sets `X_1,X_2,X_3` of sizes differing by
at most one. Because `Q` is in general position, every colorful root triple
is noncollinear.

For every carrier word `B` and root subset $S\subset Q$, (6) gives

\[
 \boxed{\qquad
 B\cup S\text{ is ordinary}
       \quad\Longleftrightarrow\quad |S|\le1.
 \qquad}                                                       \tag{7}
\]

The implication for `|S|>=2` follows by choosing its inner and outer
dominance labels and the two selected neighbours `y,w`. The singleton
case is the same-type transversal property of the macro roles.

If there are `s` nonroot upper roles and `t` lower roles, all of size `D`,
then

\[
 H=D^{s+t},\qquad H_g=H/D^2,qquad
          |I_1\cup I_2\cup I_3|=D H.                            \tag{8}
\]

Every output in (8) recovers its physical `(B,z)` and has load one. Taking
$s+t=\kappa\log D$ gives rank `O(log n)` and quadratic carrier entropy,
but
the literal mixed multiplier is only `D=n^{1-o(1)}`, below `n^{log_2 3}`.

For a fixed `z`, the line through `z` separating the carrier support sends
`z` to infinity and exposes all `H` carriers as one directional family.
For three colorful roots, Theorem 1 says those charts cannot be made one
chart: the roots are noncollinear.

### Exact deletion-shield cover

The regression does not conceal what happens after carrier deletion.

> **Lemma 2 (two neighbouring shields).** Let `F` be any ordinary face of
> the full configuration with $|F\cap Q|\ge2$. Then
> \[
>                       F\cap Y=\varnothing
>                 \quad\hbox{or}\quad F\cap W=\varnothing.     \tag{9}
> \]
> Consequently the entire multi-root face bank is contained in
> \[
>       \mathcal F(P\setminus Y)\cup\mathcal F(P\setminus W).   \tag{10}
> \]

**Proof.** If `F` met both neighbour clouds, choose $y\in F\cap Y$,
$w\in F\cap W$, and two roots $x,x'\in F\cap Q$.
Equation (6) makes their four-set nonordinary. This contradicts heredity
of an ordinary face. Equation (10) is immediate. QED.

Thus all carrier-retaining multi-root failures route to two actual induced
deletion shields. At the complete-word level, either deletion removes one
`D`-choice role, so its outside reservoir has size `H/D`. In the standard
strong-row first-cap/last-cup decomposition, a non-singleton root trace
which coexists with outside words is an endpoint cap or cup of `Q`.
Writing `C(Q),U(Q)` for those profiles and `R_L,R_R` for the two one-sided
word reservoirs gives the exact selected-interface bound

\[
       V_{\rm root\text{-}mixed}
          \le V(Q)+C(Q)R_R+U(Q)R_L,
 \qquad R_L,R_R\le 2^{O(s+t)}H/D.                              \tag{11}
\]

Formula (11) is the scalar coherent-ramp interface: incompatible charts
do not destroy the profiles; they move the problem into two oppositely
oriented deletion reservoirs. For arbitrary substituted carrier children,
(10), rather than (11), is the unconditional statement.

The induced root bank `V(Q)` is detached and additive in (11), not
multiplied by `H`. At near-ambient scale `D=n/polylog(n)`, least-counterexample
induction on `Q` is short of the parent target by the familiar
$n^{\Theta(\log\log n)}$ factor. Equation (11) identifies exactly where
that
factor must come from: a one-sided root profile times a deletion reservoir.

## 4. Stress against the known barriers

* **Nested `1+3`.** Equation (6) is precisely the scalable nested
  `1+3` circuit. Circuit elimination cannot release a second root while
  both neighbour roles remain.
* **Three-cloud partner barrier.** Partitioning the arbitrary `Q` gives
  three independent named face alphabets without altering the common cage.
  No same-chart conclusion follows from their names or sizes.
* **Detached shields.** They are neither discarded nor claimed harmless:
  (10) is an exact global cover, and (11) is the strong-row profile count.
  Closing them requires weighted deletion descent or endpoint-potential
  growth.
* **History.** All displayed incidences have physical load one. Additional
  histories enter only through the explicit $\Lambda_i$ in (5).

## 5. Verification

Run

```text
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_three_root_rechart_synchronization_barrier.py
```

The exact rational checker uses the 14-point carrier/root realization from
the critical-dispersion verifier, treats its three roots as three named
clouds, verifies chart incompatibility by noncollinearity, checks all 27
carriers and 81 physical singleton incidences, and checks every cross-root
pair failure. It then enumerates all 16,383 nonempty subsets of the full
configuration and verifies the global deletion-shield cover (9)--(10), as
well as the exact weighted history inequality on all small tables.
