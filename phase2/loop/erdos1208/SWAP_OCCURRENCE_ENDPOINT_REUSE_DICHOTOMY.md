# Endpoint reuse pays the low branch of the physical-wedge gate

## 1. Outcome

The local fixed-invariant equations are flexible enough to plant linearly
many owner blocks.  The missing restriction is not local algebra: it is
reuse of the actual endpoints of the six directed-difference tracks.

This note gives an exact dichotomy.  For every contributing owner cell
`C`, let `S_C` be its parameter set and put `r_C=|S_C|`.  Every occurrence
`(C,q)`, `q in S_C`, has six nonzero directed-difference tracks in `D`.
Let `E(C,q) subset A` be the union of their physical endpoints; then

\[
 2\le |E(C,q)|\le12.                              \tag{1.1}
\]

If no point of `A` belongs to more than `Delta` occurrence footprints,
then

\[
 \boxed{\displaystyle
 C_{\rm center}=3\sum_C{r_C\choose3}
 \le108\Delta^3 k^3.}                            \tag{1.2}
\]

Thus subpolynomial endpoint reuse pays the whole branch from the `k^3`
allowance.  The direct height theorem may assume that many occurrences
reuse one actual point of `A`; it is an endpoint-pencil theorem, not a
pointwise fixed-`R` theorem.

There is also a thresholded form which does not discard the high-reuse
mass.  It isolates one explicit endpoint-weighted Carleson sum as the only
survivor.

## 2. Conflict colouring

Let `O={(C,q):q in S_C}` be the occurrence set, and define

\[
 d(x)=|\{o\in O:x\in E(o)\}|,
 \qquad \Delta=\max_{x\in A}d(x).                \tag{2.1}
\]

Join two occurrences when their endpoint footprints meet.  One occurrence
has at most twelve endpoints, and every endpoint is contained in at most
`Delta` occurrences.  Hence the conflict graph has maximum degree at most

\[
 12(\Delta-1).                                    \tag{2.2}
\]

It therefore has a proper colouring with

\[
 c\le12\Delta-11\le12\Delta                     \tag{2.3}
\]

colours.  Occurrences of one colour have pairwise disjoint endpoint
footprints.  Since every footprint contains at least two points, each
colour contains at most `k/2` occurrences.

Write `r_{C,a}` for the number of occurrences of cell `C` with colour `a`.
Convexity gives

\[
 r_C^3=\left(\sum_a r_{C,a}\right)^3
 \le c^2\sum_a r_{C,a}^3.                        \tag{2.4}
\]

For a fixed colour,

\[
 \sum_C r_{C,a}^3
 \le\left(\sum_C r_{C,a}\right)^3
 \le(k/2)^3.                                     \tag{2.5}
\]

Finally `3 binom(r,3)<=r^3/2`.  Summing (2.4)--(2.5) yields

\[
 C_{\rm center}
 \le {c^3k^3\over16}
 \le108\Delta^3k^3,                              \tag{2.6}
\]

which proves (1.2).

## 3. Lossless low/high restart

Fix an integer threshold `Lambda>=2` and call `x` high when
`d(x)>=Lambda`.  Call an occurrence high when its footprint contains a
high endpoint.  For a cell `C`, let `h_C` be its number of high
occurrences and put `ell_C=r_C-h_C`.

The all-low triples contribute

\[
 C_{\rm low}=3\sum_C{\ell_C\choose3}
 \le108(\Lambda-1)^3k^3,                         \tag{3.1}
\]

by the preceding colouring theorem.  Every other parameter triple contains
at least one high occurrence, so a union bound over its distinguished high
member gives

\[
 3\sum_C\left({r_C\choose3}-{\ell_C\choose3}\right)
 \le3\sum_C h_C{r_C-1\choose2}.                  \tag{3.2}
\]

Moreover

\[
 h_C=
 \sum_{q\in S_C}{\bf1}_{E(C,q)\cap A_{\rm hi}\ne\varnothing},
 \qquad A_{\rm hi}=\{x:d(x)\ge\Lambda\}.        \tag{3.3}
\]

For every high occurrence choose the least high endpoint in its footprint
under one fixed ordering of `A`, and call it `chi(C,q)`.  Consequently

\[
\boxed{\displaystyle
 C_{\rm center}
 \le108(\Lambda-1)^3k^3+\mathcal P_\Lambda,}
                                                               \tag{3.4}
\]

where the exact endpoint-pencil envelope is

\[
 \mathcal P_\Lambda=
 3\sum_{x:d(x)\ge\Lambda}
   \sum_{\substack{C,\ q\in S_C\\\chi(C,q)=x}}
        {r_C-1\choose2}.                          \tag{3.5}
\]

For `Lambda=N^{o(1)}`, the first term is already target-scale.  It is
therefore sufficient to prove

\[
 \boxed{\mathcal P_\Lambda
       \le N^{o(1)}m^2.}                          \tag{3.6}
\]

This is the direct remaining height gate.  It retains the physical point
`x`, one of twelve track endpoint roles, the owner cell, and its rich
parameter set.  Pigeonholing the role costs only a constant.  Unlike the
dead fixed-`R` shortcut, a large value in (3.5) is a genuine synchronized
endpoint pencil in the selected nested core.

## 4. Scope and next move

The theorem is purely combinatorial once the six tracks have been lifted
to their unique physical endpoint pairs.  Distance-Sidonicity is used in
that lift: every nonzero directed difference has one ordered endpoint pair.

The remaining task is no longer to bound all occupied `(R,T)` keys at
once.  It is to prove (3.6), preferably after choosing canonically one high
endpoint and one of the twelve track slots for each high occurrence.  The
metric transversality theorem can then be applied inside an actual endpoint
pencil rather than to an ambient lattice box.  A failure of (3.6) must
produce either

1. many metrically transverse records through one physical endpoint, to be
   paid by height; or
2. repeated use of the same endpoint-labelled track, which is a smaller
   completion/owner collision and should feed the existing six-direction
   recursion.

The local planting in
`COARSE_INVARIANT_POINTWISE_OWNER_SUPPORT_BARRIER.md` lies entirely in the
low-reuse branch when its track endpoints are chosen fresh, and (1.2) pays
it by `k^3`.  This is exactly why that barrier does not threaten the new
restart.

The first genuine stress confirms that the new high branch is substantive.
For transformed Costas `23`, the contributing cells have `204` occurrences,
maximum endpoint degree `118`, and footprint-size histogram

\[
 (6:14,\ 7:50,\ 8:50,\ 9:62,\ 10:24,\ 11:4).
\]

Even at `Lambda=64`, all `204` units of third mass lie in the high branch;
the canonical envelope (3.5) is `612`.  Thus endpoint reuse is not a small
error term on the first nonzero row.  The gain is conceptual: the whole
direct obstruction has become one actual-point pencil with a constant track
role, rather than an ambient support count.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_occurrence_endpoint_reuse_dichotomy.py
```

The verifier checks the greedy conflict colouring, the constant in (1.2),
and the lossless threshold split (3.1)--(3.5) on exhaustive small and seeded
random endpoint-footprint systems.  The optimal-core analyzer independently
reconstructs all six endpoint pairs and records the genuine threshold
profiles.
