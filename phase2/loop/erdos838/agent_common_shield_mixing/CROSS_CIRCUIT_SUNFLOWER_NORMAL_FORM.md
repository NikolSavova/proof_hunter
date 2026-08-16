# Cross-circuit almost-antichains: a sunflower normal form and a planar regression

**Date:** 2026-08-14.  All logarithms are base two.

## Verdict

The last common-base completion residue has an exact global normalization.
After deleting the fixed-power compatible degree, the Erdos--Rado sunflower
lemma turns every quadratic-entropy rank-`O(log D)` family into a
pairwise-incompatible sunflower of fixed-power size.  Its petals are
disjoint, and every bad planar four-circuit between two members meets both
petals.  Quantitatively, if

\[
 |\mathcal C|\ge 2^{a(\log D)^2},\qquad
 q\le\kappa\log D,\qquad \Delta_+(\mathcal C)\le D^c,
\]

then there is such a sunflower of size

\[
                       D^{a/\kappa-o(1)}.                    \tag{1}
\]

This is a substantial simplification of the cross-circuit branch, but it
does not by itself release a shield.  A scalable rational planar family
shows why.  Split a thin annulus around a convex `q`-gon into `q` radial
clusters of size `k`.  Every transversal (one point from every cluster) is
convex, while the union of any two distinct transversals is nonconvex.  Thus

\[
                      M=k^q                                  \tag{2}
\]

rank-`q` completions may have compatible degree zero.  With
`q=Theta(log D)` and `k=D^delta`, this already has quadratic entropy on only
`D^delta O(log D)` labels.  In the sunflower obtained by varying one
coordinate, every incompatibility has a canonical witness using the two
petal points and the same two adjacent root points.  The varying cluster can
itself be chosen in convex position; then every bad circuit meets the root,
so the full-circuit matching number is at most `q-1`.  Hence neither a
compatible-pair density argument nor a large-circuit-matching assertion can
finish the residue.

The construction is not an EIC' counterexample: in the displayed version
each cluster is convex and already carries a huge Boolean reservoir; the
report gives no upper bound on the full face count after replacing the
clusters by low-face order types.  It
does prove that the remaining positive statement must exploit the shield
inside the concentrated root pair (or the repair labels), not merely the
existence of many cross-circuits.

## 1. Independent sunflower extraction

Let `F` be an ordinary face and let
`\mathcal C subseteq {W choose q}` be a family of distinct completions with

\[
                         F\cup C\in\mathcal F(P)
                         \qquad(C\in\mathcal C).             \tag{3}
\]

Join two completions in the compatibility graph when their union with `F`
is ordinary.  Write `M=|\mathcal C|` and let its maximum degree be `Delta`.

> **Theorem 1 (incompatible sunflower normal form).**  Put
> \[
> N=\left\lceil{M\over\Delta+1}\right\rceil,
> \qquad
> k=\left\lceil\left({N\over q!}\right)^{1/q}\right\rceil. \tag{4}
> \]
> There are `k` completions
> \[
>                     C_i=K\mathbin{\dot\cup}P_i            \tag{5}
> \]
> which are pairwise incompatible, where the petals `P_i` are nonempty,
> pairwise disjoint, and all have the same rank `p=q-|K|`.  The enlarged
> root `F'=F union K` is an ordinary face.  For every `i ne j`, every bad
> four-subset of `F' union P_i union P_j` meets both `P_i` and `P_j`.

**Proof.**  Greedy deletion of a vertex and its at most `Delta` neighbours
gives an independent family of size at least `N`.  The Erdos--Rado bound
says that a `q`-uniform family with more than `q!(k-1)^q` members contains a
`k`-sunflower.  The definition (4) gives the required strict inequality,
including when `(N/q!)^(1/q)` is integral.  Distinct sunflower members have
nonempty petals.  Since the sunflower lies in the independent family, its
members are pairwise incompatible.

The set `F'=F union K` is a subset of every face in (3).  If a bad
four-subset of `F' union P_i union P_j` missed `P_i`, it would lie in the
ordinary face `F' union P_j`; symmetrically it cannot miss `P_j`.  QED.

For the asymptotic assertion, (4) gives

\[
 \log k\ge {\log M-\log(\Delta+1)-\log(q!)\over q}-O(1).
                                                                    \tag{6}
\]

If `log M>=a(log D)^2`, `q<=kappa log D`, and
`log(Delta+1)=O(log D)`, then `log(q!)=O(log D log log D)`.
Dividing (6) by `log D` proves (1).

The order of the two operations is load-bearing.  Taking a sunflower first
and only then deleting compatible neighbours could lose the whole
fixed-power sunflower.  Taking an independent set first costs only
`D^{O(1)}`, negligible compared with quadratic entropy.

There is a useful terminal range which does not need incompatibility at all.
Let `W=union_(C in mathcal C) C`, `N=|W|`, and use the established universal
planar reservoir

\[
               V(W)\ge 2^{(\log N)^2/8}                    \tag{6a}
\]

for sufficiently large `N` (weakening the known asymptotic constant to
`1/8`).

> **Corollary 1.1 (support-reservoir cutoff).**  Put `d=log D` and
> `A_d=(log M)/d^2`.  If `q<=kappa d`, then
> \[
>       \log V(P)\ge
>          \left({A_d^2\over8\kappa^2}-o(1)\right)d^2.     \tag{6b}
> \]
> Consequently, if `liminf A_d=a>8kappa^2`, then for every fixed `s`
> \[
>                         D^sM\le V(P)                      \tag{6c}
> \]
> for all sufficiently large `D`.

**Proof.**  Distinct `q`-sets give `M<=N^q`, hence
`log N>=(A_d/kappa)d`.  Every convex subset of the induced set `W` is also
an ordinary face of `P`, so (6a) gives (6b).  The coefficient gap

\[
 {A_d^2\over8\kappa^2}-A_d
   =A_d\left({A_d\over8\kappa^2}-1\right)                 \tag{6d}
\]

is bounded below by a positive constant.  It absorbs the linear term
`s log D`, proving (6c).  QED.

In the hard source-cloud branch one has
`log M>=(1/8-o(1))d^2`.  Therefore every **single** common-base fibre with
`q<=(1/8-eta)d` is paid even if it carries `D^2M` records.  The word
“single” is essential: across many bases the detached reservoirs in (6a)
can be identical, so (6c) is not yet the required global sum.  It does
remove the whole low-rank part of the local cross-circuit atom and leaves
`q>=(1/8-o(1))log D` in any genuinely hard fibre.

## 2. A scalable planar almost-antichain

> **Theorem 2 (radial-cluster regression).**  For every `q>=3` and `k>=2`
> there is a planar general-position set
> \[
>                        Z=Z_0\mathbin{\dot\cup}\cdots
>                              \mathbin{\dot\cup}Z_{q-1},
>                  \qquad |Z_i|=k,                          \tag{7}
> \]
> such that:
>
> 1. every transversal `Q` with `|Q cap Z_i|=1` is in convex position;
> 2. `Q union Q'` is not in convex position for all distinct transversals;
> 3. if all coordinates except `i` are fixed, the resulting `k`-member
>    sunflower has singleton petals in `Z_i`, and the circuit witnessing
>    every pair can be chosen to use the same two fixed points in
>    `Z_(i-1)` and `Z_(i+1)`.

**Proof.**  Start with a strictly convex `q`-gon
`v_0,...,v_(q-1)`.  In the inward ray at `v_i`, choose `k` distinct points
in a sufficiently short segment immediately behind `v_i`.  Choose the
segment so short that:

* one point chosen on every ray is still a strictly convex `q`-gon; and
* for any two levels `z_in,z_out` on ray `i`, with `z_in` farther inward,
  `z_in` lies strictly inside the triangle formed by `z_out` and arbitrary
  points in the chosen short segments at `v_(i-1),v_(i+1)`.

Both assertions are open strict inequalities.  The second holds in the
unperturbed radial model because the inward ray enters the ear triangle
`v_(i-1)v_iv_(i+1)`.  There are finitely many required inequalities, so a
generic sufficiently small rational perturbation, taken along a tiny
strictly convex local arc in each cluster, makes the whole set general
position, makes each `Z_i` convex, and preserves all of them.

The first inequality proves (1).  If two transversals differ at coordinate
`i`, call the farther-inward point `z_in` and the other `z_out`.  Their
union contains points in the two adjacent clusters, so the second strict
inequality puts `z_in` inside a triangle contained in the union.  This
proves (2), and fixing the adjacent transversal coordinates gives the same
two root points in every circuit of the one-coordinate sunflower, proving
(3).  QED.

Taking `k=floor(D^delta)` and `q=floor(kappa log D)` in (2) gives

\[
       \log M=q\log k=(delta kappa+o(1))(\log D)^2,          \tag{8}
\]

while `|Z|=D^(delta+o(1))`.  This meets exactly the entropy and rank scale
of the hard completion child.

## 3. Consequence for the live residue

Theorem 1 reduces the hard branch to disjoint petals, but Theorem 2 shows
that even a power-size pairwise-incompatible sunflower may have canonical
witnesses concentrated on one two-point root.  The canonical witness
subclutter has matching number one.  More robustly, because the petal
cluster itself is convex, every bad circuit in the one-coordinate
sunflower uses at least one of the `q-1` root labels, so the matching number
of the full circuit clutter is at most `q-1`, although the petal traces
form a complete graph.

Therefore a successful global theorem must use at least one of the
following extra inputs:

1. delete/rotate the common root pair and charge the convex subsets exposed
   inside the petal cluster;
2. mix that cluster reservoir with the `D` repair labels; or
3. prove a lexicographic-composition face lower bound showing that a
   quadratic transversal family and all concentrated root-pair clusters
   cannot both have only coefficient-one total capacity.

The radial construction also survives the stricter **detached** test.  Its
certificate triangle is contained in `Q union Q'`, not merely in
`F union Q union Q'`; in a one-coordinate sunflower it is exactly the
common-root circuit `{u,v,z_in,z_out}`.  Thus testing detached convexity
first removes the separated-ear product branch but still leaves this
common-root cluster.

The radial construction is the sparse-guard obstruction in its canonical
completion-family form.  It sharply rules out “many cross-circuits imply a
fixed-power disjoint full-circuit matching” and “quadratic entropy forces
compatible pairs.”  Its convex clusters realize, rather than rule out, the
intended unrestricted-shield alternative.

## 4. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_cross_circuit_sunflower.py
```

The checker exhausts small uniform families for the Erdos--Rado numerical
threshold, audits the fixed-power exponent inequality, and verifies an
exact rational `q=5,k=4` radial-cluster instance: all 1,024 transversals are
convex, every inner/outer pair is certified by the two adjacent clusters,
and no three of the 20 points are collinear.
