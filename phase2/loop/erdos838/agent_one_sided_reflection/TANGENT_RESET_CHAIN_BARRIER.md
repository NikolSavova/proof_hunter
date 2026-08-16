# Linear-depth tangent reset: exact barrier and the missing cross-level bank

## Verdict

Strict progress of the two endpoint tangent ranks does not by itself produce
a multiplicative spend along a reset chain. There is a scalable rational
wrapper around an arbitrary child order type with the following properties:

* every reset removes one new rooted singleton ear and passes to a pocket of
  codimension one;
* both tangent coordinates progress strictly at every level;
* the new rooted ear is incompatible with every nonempty child face, so the
  parent-child coexistence product is identically zero;
* the rooted polynomial grows only linearly with the reset depth.

Thus no potential which assigns a positive multiplicative credit merely from
strict tangent-rank progress and the one-level Kraft identity can telescope.
The missing credit is genuinely cross-level: in the explicit regression the
discarded ear tips themselves form a convex chain, giving a detached Boolean
bank of size \(2^L\). A valid iteration theorem must retain the ordinary
convex-face complex of the union of discarded hull layers, or find compatible
parent-child unions. Recording only the current pocket and its two tangent
ranks is insufficient.

The exact verifier also runs greedy deepest-pocket resets on the central
Pascal cell, the perfect-matching star, and the alternating family:

    python3 phase2/loop/erdos838/agent_one_sided_reflection/verify_tangent_reset_chain_barrier.py

No coefficient-half closure is claimed.

## 1. An arbitrary-core ear wrapper

Fix roots

\[
                         u=(0,0),\qquad v=(1,0).          \tag{1}
\]

Let \(C\) be any finite rational general-position point set. An
orientation-preserving affine compression puts a copy \(C'\) in a small
open box about \((1/2,-1)\), inside the triangle with apex
\(z_0=(1/2,-4)\). For \(t=0,\ldots,L-1\), choose successively deeper
rational apices \(z_t\) so that

\[
 C'\cup\{z_0,\ldots,z_{t-1}\}
       \subset\operatorname{int}\operatorname{conv}\{u,v,z_t\}. \tag{2}
\]

One explicit unperturbed choice is

\[
 z_t=\left({1\over2}+{t\over100L},-2^{t+2}\right).       \tag{3}
\]

All containments in (2) are strict. A sufficiently small generic rational
perturbation preserves them, makes the total configuration general
position, and keeps the apex sequence a strict convex chain. Finally the
affine shear \((x,y)\mapsto(x+y,y)\) puts every child and apex label to the
left of \(u\), without moving the roots. Hence this is a valid one-side
trace cloud in the original x-order.

Put

\[
 Q_t=C'\cup\{z_0,\ldots,z_{t-1}\},\qquad 0\le t\le L.    \tag{4}
\]

The child order type is unrestricted: the wrapper changes none of the
orientations inside \(C'\).

## 2. Exact linear rooted profile

Let

\[
 R_t(s)=\sum_{\substack{A\subseteq Q_t\\
                  A\cup\{u,v\}\ {\rm convex}}}s^{|A|}   \tag{5}
\]

be the rooted-side polynomial. The wrapper has an exact recurrence.

> **Theorem 1 (linear wrapper profile).**
> \[
> \boxed{R_t(s)=R_0(s)+t\,s.}                            \tag{6}
> \]
> The singleton hull \(\{z_{t-1}\}\) has hidden pocket exactly
> \(Q_{t-1}\), so it realizes a codimension-one deepest reset at every
> wrapper level.

**Proof.** By (2), every point of \(Q_{t-1}\) is strictly inside the
triangle \(uvz_{t-1}\). A rooted convex subset of \(Q_t\) which contains
\(z_{t-1}\) therefore cannot contain any child point: that point would be a
nonvertex. The only new rooted face is the singleton
\(\{z_{t-1}\}\). Rooted faces omitting it are exactly those of
\(Q_{t-1}\). This proves (6). The same strict containment says that the
relative-hull fibre of \(\{z_{t-1}\}\) is its full Boolean pocket
\(Q_{t-1}\). QED.

At half weight,

\[
                         R_t(1/2)=R_0(1/2)+{t\over2}.     \tag{7}
\]

The Kraft reset is sharp at every step: the selected pocket loses one label.
The strict tangent-progress inequalities from the preceding report apply
because every child point lies strictly inside the parent triangle. Thus
the two endpoint ranks move at every level, yet the spend remains linear.

## 3. Exact coexistence failure

For a parent ear define its child coexistence bank

\[
 {\cal C}_t=
 \{S\subseteq Q_{t-1}:S\ {\rm convex},\
       S\cup\{u,v,z_{t-1}\}\ {\rm convex}\}.              \tag{8}
\]

Strict containment (2) gives

\[
 \boxed{{\cal C}_t=\{\varnothing\}.}                     \tag{9}
\]

Indeed every nonempty \(S\) contains a point strictly interior to the
triangle \(uvz_{t-1}\), so the union in (8) is not in convex position.
Consequently every proposed product bank of the form

\[
 \{\hbox{new parent rooted ear}\}\times
       \{\hbox{nonempty child-pocket faces}\}             \tag{10}
\]

has size zero, at all \(L\) levels. The failure is not decoder overlap:
there are literally no convex outputs.

This kills a broad class of tangent-rank potentials. A one-step potential
may correctly record a positive Kraft cost and strict rank motion, but those
credits cannot be multiplied through the child unless it also records an
ordinary face bank which does not contain the parent ear.

## 4. Where the missing mass goes

For the choice (3), the apex set

\[
                         Z_L=\{z_0,\ldots,z_{L-1}\}       \tag{11}
\]

is a strict cap: its consecutive slopes are strictly ordered. Hence every
subset of \(Z_L\) is convex and

\[
                         V(Z_L)=2^L.                     \tag{12}
\]

Thus this regression pays, but only through a detached cross-level bank.
The same ear which destroys parent-child coexistence becomes a useful
ordinary vertex once the fixed roots and deeper parent are omitted.

This identifies the correct missing theorem.

> **Cross-level discarded-layer target.** Along a failed-guard reset chain,
> either sufficiently many parent hulls coexist with child-pocket faces, or
> the union of the discarded visible hulls has a large ordinary convex-face
> complex, with a decoder that remembers only a subpower number of chain
> states.

The wrapper takes the second branch with a Boolean bank. A general reset
chain may discard multi-vertex rooted hulls rather than singleton ears, so
(12) cannot simply be assumed. Proving the target requires planar
interaction between different reset levels; it is absent from the
one-level Kraft and tangent-rank data.

## 5. Global reuse and why a linear chain is not the main problem

If one selects one pocket at every depth for every directed trace state, a
fixed ordinary face can be offered at most once per depth and trace. The
literal bound is \(O(n^3)\): \(O(n^2)\) directed states and depth at most
\(n\). This is polynomial, but it erases the fixed-power gain needed to
amplify the cubic rank-four mass. Merely observing that the chain terminates
therefore does not solve the reflection branch.

The desired cross-level bank must replace depth multiplicity by genuine
faces. In the wrapper, (12) does exactly that. Conversely, the arbitrary
core \(C'\) proves that the terminal pocket can have any stretchable order
type; no terminal scalar profile or universal complete-grid assumption can
supply the missing interaction.

## 6. Stress-test interpretation

The exact audit reports four qualitatively different chains.

* In the central Pascal heavy trace, the deepest pockets shrink in balanced
  two-label steps and compatible opposite parents expose the expected
  complete hidden grid.
* In the perfect-matching star, both first pockets are deep but their parents
  are forced into a failed guard; later pockets shrink rapidly.
* At the terminal alternating trace, each one-side cloud is already fully
  visible, so its rooted halfmass is exactly \((3/2)^m\) and no reset occurs.
* In the arbitrary-core wrapper, the codimension-one chain persists for
  exactly \(L\) levels, rooted halfmass rises only by \(L/2\), and all
  parent-child coexistence banks vanish. The detached apex chain supplies
  \(2^L\) ordinary faces.

These examples rule out a rank-only potential while leaving a crisp planar
cross-level bank as the sole next target.
