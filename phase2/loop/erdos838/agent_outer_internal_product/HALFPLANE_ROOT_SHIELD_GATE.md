# Half-plane release for high-overlap root shields

**Date:** 2026-08-15.  All logarithms are base two and the empty convex
subset is counted.

## Verdict

A high-`rho` root-shield star has two exact ordinary-face banks.  First, the
root-marked downset of a convex rank-`q` top has `2^(q-1)` records.  Second,
for a pocket point `x` inside the root triangle, the line `xz` splits the
other top vertices; on the richer side, every subset together with `{x,z}`
is convex.  This pocket-retaining bank has at least

\[
                         2^{\lceil(q-1)/2\rceil}             \tag{1}
\]

`x`-compatible faces for each root.

For a globally assigned family of disjoint root-shield stars, let `omega_D`
and `omega_H` be the maximum cross-star overlaps of the downset and
half-plane banks.  If every star has top rank `q`, root multiplicity `k`, and
marked mass `hk`, then

\[
 \boxed{
 M\le\min\left\{
 {qk\omega_D\over2^{q-1}},
 {qk\omega_H\over2^{\lceil(q-1)/2\rceil}}
 \right\}V(P).}                                            \tag{2}
\]

This is a **linear** bank bound, not a square-root estimate, and uses the
ambient `V` only once over all stars.  In the central complete layer,

\[
 q=b+1+2r,qquad k={2r\choose r}.                           \tag{3}
\]

If `b=beta log n`, `r=gamma log n`, and the corresponding overlap is
`n^{delta+o(1)}`, the downset bank gives a fixed-power gain when
`beta>delta`.  The pocket-retaining half-plane bank gives one whenever

\[
                         \beta>2\gamma+2\delta.             \tag{4}
\]

Thus subpower downset reuse closes every linear-rank carrier.  Although the
half-plane bank is smaller, it retains the actual pocket label: high reuse
there extracts many distinct retained-edge/carrier/top profiles with one
common pair `(x,z)`.  The remaining central residue is consequently a
small-carrier star, or fixed-power reuse of one of these two banks.

The multi-root parabola regression is an exact sharp warning.  It has
`b=2`, `q=2r+3`, and only polynomial marked mass.  The downset gives only a
polylogarithmic ratio, while the half-plane bank has bank-to-mass ratio
`2^{-r+o(r)}`.  Hence neither gives a fixed power, and the theorem does not
falsely close the synchronized small-carrier model.  No `Theta(V)` regression
for the remaining high-overlap branch is constructed, and EIC' is not
closed.

## 1. The geometric release lemma

> **Lemma 1 (one-sided root release).**  Let `Q` be a `q`-label planar
> convex face in general position.  Let `z in Q`, and let `x` lie strictly
> inside `conv(Q)`.  The line through `x,z` partitions `Q setminus {z}` into
> two open sides.  Let `H` be either side.  Then for every `S subseteq H`,
>
> \[
>                              \{x,z\}\cup S                \tag{5}
> \]
>
> is convex.

**Proof.**  Give the line `xz` a signed affine functional `ell` which is
positive on `H` and zero at `x,z`.  If `S` is nonempty, every convex
combination using a point of `S` with positive weight has positive `ell`, so
it cannot equal `x`; using only `z` also cannot give `x`.  Thus `x` is
outside `conv(S union {z})` and is extreme in (5).  The empty case is
immediate.

Every `v in S union {z}` is a vertex of `Q`, so it has a strict supporting
functional `phi_v` on `Q`.  Since `x` is interior to `conv(Q)`,
`phi_v(x)<phi_v(v)`.  Hence `v` remains the unique maximizer of `phi_v` after
`x` is added.  All labels in (5) are extreme.  QED.

In the root-shield setting, `Q=Q_z` contains the root triangle
`T=e union {z}` and `x` is strictly inside that triangle.  Therefore `x` is
interior to `Q`, so Lemma 1 applies.  General position puts no other
`Q`-label on `xz`.  The richer of the two sides has size

\[
                         t_z\ge\left\lceil{q-1\over2}\right\rceil.
                                                                    \tag{6}
\]

Choose it canonically, breaking a tie by the label order, and define

\[
 \mathcal H_z=
 \{\{x,z\}\cup S:S\subseteq H_z\}.                        \tag{7}
\]

Then `|mathcal H_z|=2^{t_z}`.

## 2. Root-marked top downsets

Before using `x`, every root has the larger bank

\[
 \mathcal D_z=\{F\subseteq Q_z:z\in F\},\qquad
 |\mathcal D_z|=2^{q-1}.                                  \tag{7a}
\]

All its members are ordinary faces because `Q_z` is convex.

> **Lemma 2a (downset load in one star).**  For a star with `h` distinct
> roots,
>
> \[
> \left|\bigcup_z\mathcal D_z\right|\ge {h2^{q-1}\over q}.
>                                                                    \tag{7b}
> \]

**Proof.**  Every record retains its root mark `z`.  An output has rank at
most `q`, so it is charged by at most `q` distinct roots in the star.  QED.

For a disjoint global family of stars, define

\[
 \omega_D=\max_F
 |\{\sigma:F\in\bigcup_{z\in Z_\sigma}\mathcal D_z\}|.    \tag{7c}
\]

Summing (7b) over all stars immediately gives

\[
                         M\le {qk\omega_D\over2^{q-1}}V(P).
                                                                    \tag{7d}
\]

Since `q=b+1+2r` and `log k=2r-o(r)`, its leading coefficient exponent is
`-b+log omega_D+o(log n)`.  This proves the first alternative in (2) and
closes `b=beta log n` whenever `omega_D=n^(delta+o(1))` with `beta>delta`.
The limitation is that (7a) forgets the completion label `x`; many different
pocket stars can reuse the same downset bank.

## 3. One star has pocket-retaining, root-bounded output load

A root-shield star `sigma` consists of

* one common completion face `Y=B union {x}`;
* one common retained edge `e subseteq B` and pocket label `x`;
* `h_sigma` distinct root labels `z`;
* one distinct convex top shield `Q_z` for every root, containing
  `B union {z}` and having rank exactly `q`;
* one central complete-layer cell of marked weight `k` for every root.

The cells in the star are distinct and canonically assigned; no cell is
counted in two stars when several stars are summed.

> **Lemma 2 (within-star load).**
>
> \[
> \left|\bigcup_{z\in Z_\sigma}\mathcal H_z\right|
> \ge {h_\sigma 2^{\lceil(q-1)/2\rceil}\over q}.            \tag{8}
> \]

**Proof.**  Every record from root `z` contains its mark `z`.  For fixed `z`,
the output recovers `S`, so there is no repeated record.  The two neighbours
of `z` on the boundary of `Q_z` lie on opposite sides of the line from `z`
through the interior point `x`.  Hence neither side contains more than
`q-2` other top vertices, and an output from (7) has rank at most `q`.
It can therefore contain the marks of at most `q` distinct roots in the
star.  Summing the `h_sigma` banks and dividing by this load bound proves
(8).  QED.

This decoder uses no carrier guess and no missing-root `n` loss.  The root
label is physically retained in the ordinary output.

## 4. Global half-plane star bank

Let `mathfrak S` be a disjoint canonical family of stars, and put

\[
 \omega_H=\max_F
 |\{\sigma\in\mathfrak S:
        F\in\bigcup_{z\in Z_\sigma}\mathcal H_z\}|.         \tag{9}
\]

> **Theorem 3 (global half-plane root-shield gate).**  Equation (2) holds.

**Proof.**  Let `mathcal H_sigma` denote the union in (8).  Its marked mass
is `M_sigma=h_sigma k`, whence

\[
 M_\sigma
 \le{qk\over2^{\lceil(q-1)/2\rceil}}
       |\mathcal H_\sigma|.                                \tag{10}
\]

Sum (10) over all stars.  By (9),
`sum_sigma|mathcal H_sigma|<=omega_H V(P)`.  QED.

For nonuniform ranks and weights, dyadically split `q,k,t_z`; the live
logarithmic slice loses only `n^o(1)`.  From Stirling,
`log k=2r-o(r)`.  Substituting (3) into (2) gives leading exponent

\[
             2r-{b+2r\over2}+\log\omega_H
             =r-{b\over2}+\log\omega_H,                    \tag{11}
\]

which proves (4).

## 5. High bank reuse is edge/carrier divergence

> **Lemma 4 (half-face first divergence).**  If one ordinary face `F` lies
> in `w` distinct star banks, then at least
>
> \[
>                              {w\over |F|^2}                \tag{12}
> \]
>
> of those stars have a generating record with the same pocket label `x`
> and the same missing root label `z`.  Their retained-edge/carrier/top
> triples `(e,B,Q_z)` are pairwise distinct.

**Proof.**  Choose the canonical first generating record in every incident
star.  Its distinguished labels `(x,z)` both lie in `F`, so pigeonhole gives
(12).  If two remaining records also had the same `e,B`, then
`T=e union {z}` and the tuple `(T,z,B)` would agree.  It determines the
canonical cell and its top shield, and the common `x` determines
`Y=B union {x}`; the two stars would be identical.  QED.

Thus replacing `omega_H` by its worst possible value is avoidable precisely
unless many different outer edges/carriers synchronize one actual pocket
label and root.  The ordinary face `F` already retains `(x,z)`; the missing
bank must record the divergent carrier edge without reintroducing an `n^2`
guess.  This is the exact next residual.

## 6. Mandatory parabola regression

In the common-chain construction, let `|W|=2r+1`,
`B={a,b}`, and use one top `Q=B union W`.  Fix one pocket label `x`, and make
one root cell for each `z in W`.  Then

\[
 b=2,qquad q=2r+3,qquad h=2r+1,qquad
 t_z\ge r+1.                                               \tag{13}
\]

All stars use the same completion `B union {x}`, and every face retaining
`B,x` and one root/core label is nonconvex.  Nevertheless Lemma 1 releases
the one-sided faces (7).  The guaranteed bank-to-marked-mass ratio is only

\[
 {2^{r+1}\over q{2r\choose r}}=2^{-r+o(r)},               \tag{14}
\]

so (2) correctly gives no gain.  The actual marked mass
`(2r+1)binom(2r,r)` is polynomial in `n` on `r=Theta(log n)` and does not
realize the global hard slice.

The root-marked downset ratio is

\[
 {2^{q-1}\over q{2r\choose r}}=r^{-1/2+o(1)}               \tag{15}
\]

for fixed carrier rank.  It is larger than (14), but still only
polylogarithmic rather than a fixed power.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_halfplane_root_shield_gate.py
```

The exact rational checker uses the nine-root parabola star at `r=4`.  For
each of five pocket labels and every root it constructs the richer-side bank
and verifies every output directly.  Side sizes range from five through
nine.  There are 9,760 records, 7,435 distinct ordinary faces, and actual
maximum record load two, below the theorem's rank bound eleven.  For one
fixed pocket star there are 1,952 records and 1,487 faces.  The checker also
audits the downset bank (9,216 records, 2,044 faces, maximum root load nine)
and the unfavorable half-plane coefficient `qk/2^5=385/16`.
