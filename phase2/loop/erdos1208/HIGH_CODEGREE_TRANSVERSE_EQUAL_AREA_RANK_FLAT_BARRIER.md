# A literal high-codegree scalar rank-flat barrier to pairwise area extraction

## 1. Outcome

There is a genuine integral distance-Sidon set with all of the following
properties simultaneously:

\[
 k=48,\qquad c(p)=49\ge k,\qquad V(p)=V(p^{\rm op})=1, \tag{1.1}
\]

one one-role base record has 36 fully transverse third translations, but
the entire set has only 24 unordered six-distinct equal-area triangle
pairs.  More sharply:

* 31 of the 36 individual transverse endpoint systems expose no such area
  pair, even after adjoining all five endpoints of the physical scalar
  wedge;
* among the `binom(36,2)=630` unions of two transverse third-translation
  systems, 404 expose no such area pair; and
* the five metric endpoints create no new equal-area pair at all.

Thus the failure of the local scalar-to-area bridge is not an artefact of
the earlier below-threshold certificate.  Literal `c(p)>=k`, both scalar
orientations, the adaptive determinant cutoff, and pairs `q_0,q_0'` do not
force a recordwise or pairwise six-label special-affine witness.

This does not refute every aggregate reduction: the 24 geometric pairs give
432 equal-signed ordered pairs, and a many-to-one global charge could in
principle use them.  It does refute the recordwise and pairwise-local
supersaturation claim that each of the `binom(T(C),2)` pairs of transverse
extensions exposes an equal-area record in its own endpoint union.
Any surviving bridge must pool three or more translations, or use the
eight-endpoint four-sum parallelograms directly rather than first extracting
an area equality.

## 2. The exact two-translation identities

Fix a source pair `p=(s,t)`.  For every `q in Q_p`, write its ordered anchor
as

\[
 q=A_q-B_q,                                             \tag{2.1}
\]

and write the two target edges as

\[
 G_q=\{E_q,F_q\}=E(s+q),\qquad
 H_q=\{I_q,J_q\}=E(t+q).                               \tag{2.2}
\]

Here the same letters also denote pair sums when no confusion can arise.
The two clean rows are exactly

\[
\begin{aligned}
 A_q+C+D&=B_q+E_q+F_q,\qquad E(s)=\{C,D\},\\
 A_q+C'+D'&=B_q+I_q+J_q,\qquad E(t)=\{C',D'\}.
\end{aligned}                                          \tag{2.3}
\]

For `q,r in Q_p`, subtraction gives the complete collective affine system

\[
\begin{aligned}
 G_q-G_r&=H_q-H_r=q-r,\\
 G_q+H_r&=G_r+H_q,                                     \tag{2.4}\\
 G_q+B_q+A_r&=G_r+A_q+B_r,\\
 H_q+B_q+A_r&=H_r+A_q+B_r.
\end{aligned}
\]

The last three lines are endpoint-realized eight-point four-sum
parallelograms.  They preserve `p,q,r` exactly and occur for every pair of
common translations.  They remain affine-linear.  The certificate below
shows that they do not individually contain the missing determinant-one
condition.

## 3. Rank-flat construction

Start with the 43-label finite-parabola incidence template used in the
scalar stresses.  It has a source pair with 90 common clean translations.
For each translation take the two six-sparse rows in (2.3).  The verifier
stores 49 translations for which the resulting `98 by 43` rational matrix
has exact rank 36.  Its seven-dimensional kernel contains integral planar
realizations not affinely equivalent to the original parabola.

A generic integral point in two copies of this kernel was selected, then
scaled by 12.  The resulting 43-point core has unique pair sums, unique
nonzero squared distances, no collinear triple, and exactly 24
six-distinct equal-area pairs.  Every one of the 49 selected clean
translations survives, and no extra common translation appears.

The rank count explains why high codegree by itself does not rigidify this
subsystem.  At the literal threshold, a large family of clean rows can
still leave four nonlinear deformation directions in addition to the
three affine ones.

## 4. Installing the scalar weight inside the point budget

Let

\[
 Z=\delta(s)-\delta(t)=450646926180300144,qquad
 r=-Z/18=-25035940343350008.                            \tag{4.1}
\]

Five new points realize four edges from one common endpoint.  Their
displacement vectors are

\[
\begin{aligned}
 U_1&=(6258985085837501,360740369925080777),\\
 V_1&=(6258985085837503,360740369925080777),\\
 U_2&=(3129492542918749,101266245384587405),\\
 V_2&=(3129492542918753,101266245384587405).
\end{aligned}                                          \tag{4.2}
\]

They obey

\[
 |U_1|^2-|V_1|^2=|U_2|^2-|V_2|^2=r,                   \tag{4.3}
\]

with doubled determinants

\[
 2\det(U_1,V_1)=-1442961479700323108,qquad
 2\det(U_2,V_2)=-810129963076699240.                   \tag{4.4}
\]

The two first edges share their common endpoint, so they give one target
endpoint wedge.  Reversing both representations makes the two partner
edges the first edges, and those also share the same endpoint.  In the
full 48-point set, `N=1128`; the two base fibre sizes are 42 and 40, so the
common integral adaptive cutoff is at most 28.  Exact enumeration gives

\[
 \boxed{W_{r,28}=W_{-r,28}=1.}                          \tag{4.5}
\]

The metric gadget uses five, not six or seven, points because all four
edges share one endpoint.  Its horizontal increments are 2 and 4, avoiding
the equal outer-edge length that would occur if both partner vectors used
the same increment.  Global distance-Sidonicity is checked after the
gadget is installed.

## 5. Exact obstruction profile

Choose the stored one-role base.  Its first source role has disjoint target
edges and its second role has a one-endpoint target wedge.  Among the 49
common translations, exactly 36 are fully transverse to the base in all
anchor, good-target, and bad-target endpoint roles.

Let `Y(q_0)` contain:

* the four source endpoints;
* both base anchors and all four base target edges;
* the anchor and both target edges of `q_0`; and
* all five metric-wedge endpoints.

If `a(q_0)` is the number of the 24 global geometric area pairs supported
inside `Y(q_0)`, then

\[
 \#\{q_0:a(q_0)=0\}=31,qquad
 \#\{q_0:a(q_0)=1\}=5.                                 \tag{5.1}
\]

For two transverse extensions, the distribution of area pairs supported
inside `Y(q_0) union Y(q_0')` is

\[
\begin{array}{c|rrrrr}
\text{supported pairs}&0&1&2&3&4\\ \hline
\text{extension pairs}&404&153&55&16&2.
\end{array}                                             \tag{5.2}
\]

Hence the exact pairwise implication

\[
 (q_0,q_0')\longmapsto
 \text{a six-distinct equal-area pair in their endpoint union} \tag{5.3}
\]

is false on 404 of 630 pairs, despite literal high codegree and positive
scalar weight.  The always-valid collective output is (2.4), not an area
equality.

## 6. Consequence for the surviving proof route

The high-codegree transverse mass cannot be reduced to special-affine
energy by any argument that treats one extension, or even an arbitrary
pair of extensions, independently.  A viable continuation has two options:

1. prove a genuinely higher-order supersaturation theorem in which many
   pairs `(q_0,q_0')` are allowed to charge the same rare area witness, while
   globally controlling that reverse multiplicity together with `V(p)`; or
2. retain the four-sum identities (2.4) as the primary globally chargeable
   objects and couple their size-biased multiplicity directly to the
   determinant-qualified scalar wedge.

The present result is a barrier, not a proof of the required weighted
aggregate estimate.  It narrows the bridge: pairwise special-affine
extraction is unavailable even at the exact live threshold.  Its enormous
height also places the certificate inside the already-controlled
high-height area range; it is a structural no-go for the proposed coupling,
not a counterexample to the corrected ambient equal-area inequality.

## 7. Verification

Run

```bash
python phase2/loop/erdos1208/verify_high_codegree_transverse_equal_area_rank_flat_barrier.py
```

The verifier checks the exact rank-36 relation flat, all 49 common clean
translations and the absence of extras, the one-role base and 36 fully
transverse extensions, both four-sum identities in (2.4), both scalar
wedge orientations, global pair-sum and squared-distance uniqueness, all
17,296 noncollinear triangles, the exact 24-pair area energy, and the local
and pairwise exposure distributions (5.1)--(5.2).
