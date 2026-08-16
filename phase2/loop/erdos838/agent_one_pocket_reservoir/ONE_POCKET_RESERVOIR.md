# The universal one-pocket branch has a quadratic shield reservoir

**Date:** 2026-08-14.  All logarithms are base two.  A blocker set below
means the *selected* blocker neighbourhood of an actual source; histories
which traverse the same repair incidence are not counted again.

## Verdict

There is a fixed-power dichotomy in the last projectively universal
one-pocket branch which does not use comparability of the blockers.

Let `S` be rank-`r` convex sources and choose exactly `D` exterior blocked
labels above each source.  For every source `A`, look at the ordinary convex
faces lying wholly in its selected blocker neighbourhood `N(A)`.  The
established coefficient-`1/4` lower bound, applied to the `D`-point set
`N(A)`, supplies

\[
 B=2^{(1/5+o(1))(\log D)^2}                         \tag{1}
\]

canonical faces of rank at least `(1/8-o(1))log D`.  If no such face is
reused by more than `B D^{-epsilon}` sources, duplicated Hall sends all
selected repairs to ordinary faces with load at most `D^(1-epsilon)`:

\[
                    D|S|\le D^{1-\epsilon}V(P).      \tag{2}
\]

If this fails, one ordinary convex face `J`, of rank at least
`(1/8-o(1))log D`, consists entirely of selected blockers for more than

\[
                 B D^{-\epsilon}
       =2^{(1/5-o(1))(\log D)^2}                    \tag{3}
\]

actual sources.  Hence all `2^|J|>=D^(1/8-o(1))` subfaces of `J` are a
common unguarded shield bank for those sources.  This is the requested
**second reservoir or internal shield-bank theorem**.

There is a stronger minimizer-hard-slice consequence.  The low-mean and
optimized-hull reductions produce `|S|>=cV(P)` actual low-addable sources.
Then all but at most `D^{-epsilon}V(P)` sources contain in their selected
blocker neighbourhood a high-rank shield face which is shared by more than
`BD^{-epsilon}` sources.  In particular some shield face is shared by at
least `cB` sources.  Moreover there are `(1-o(1))B` distinct high-overlap
shield faces on the hard slice.  Thus the last branch is not merely one
nested chain: it is a quadratic-entropy **source-correlated complete
shield**.

At the seam `D=n^(1/2+o(1))`, the common shield has rank at least
`(1/16-o(1))log n`, its Boolean bank has size `n^(1/16-o(1))`, and its
common-source fibre in (3) has size

\[
                       2^{(1/20-o(1))(\log n)^2}.    \tag{4}
\]

This is genuine progress over the earlier common blocker pair or
`sqrt(D)` nested-chain alternatives, whose forced common-source entropy was
only linear in `log D`.

It is not yet a proof of EIC'.  The high-shield cells can reuse the same
standalone Boolean bank.  What remains is a mixed theorem coupling the
quadratic-entropy source family to one of these unguarded shield banks.
Projective universality shows that nesting alone cannot provide that
coupling.  Trying instead to improve the standalone face count of an
arbitrary blocker cloud from coefficient `1/4` to `1/2` is just Erdős 838
recursively, and is not claimed here.

## 1. Selected neighbourhood face banks

Let `P` be a planar general-position point set, let `F(P)` be its ordinary
convex-face complex, and put `V=|F(P)|`.  Let `S subset F(P)` be any family
of distinct sources.  A simple capped selection consists of sets

\[
                    N(A)\subseteq P-A,\qquad |N(A)|=D,       \tag{5}
\]

such that every `p in N(A)` is exterior blocked for `A`.  The selected
repair mass is `|E|=D|S|`.

Fix integers `k,B>=1` such that every `D`-point planar set contains at
least `B` convex subsets of rank at least `k`.  For every `A`, use the
ambient label order to choose a canonical family

\[
 \mathcal C_A\subseteq
 \{J\in F(P):J\subseteq N(A),\ |J|\ge k\},
 \qquad |\mathcal C_A|=B.                              \tag{6}
\]

Convexity is intrinsic to a labelled subset, so a convex subset of `N(A)`
is an ordinary face of the whole set `P`; no coexistence with `A` is being
asserted.  Put

\[
 d(J)=|\{A\in S:J\in\mathcal C_A\}|,
 \qquad \Lambda=\max_Jd(J).                            \tag{7}
\]

> **Theorem 1 (selected-neighbourhood reservoir dichotomy).**
> With the preceding notation,
> \[
>          B|S|=\sum_Jd(J)\le\Lambda V,
> \qquad
>          |E|\le {D\Lambda\over B}V.                \tag{8}
> \]
> More strongly, the selected repair records admit an integral map to
> ordinary faces with maximum fibre
> \[
>                    \left\lceil{D\Lambda\over B}\right\rceil. \tag{9}
> \]
> Consequently, for every `epsilon>0`, either (2) holds, or one face `J`
> of rank at least `k` lies in the selected blocker neighbourhoods of more
> than `BD^{-epsilon}` actual sources.  Every subface of `J` is then a
> common selected-blocker codeword for those sources.

**Proof.**  Equation (8) double counts the pairs `(A,J)` with
`J in C_A`.  For (9), join every one of the `D` records above `A` to all
`B` faces in `C_A`.  Every record has degree `B`, while an output has degree
at most `D d(J)<=D Lambda`.  The usual duplicated-Hall argument gives an
integral assignment of maximum load `ceil(D Lambda/B)`.  If
`Lambda<=BD^{-epsilon}`, this is (2).  Otherwise a maximizing `J` gives the
second alternative.  Since `J` is convex, every subset of it is an ordinary
face, and since `J subset N(A)`, every one of its labels is an actually
selected blocker at every source in the fibre.  QED.

The theorem is insensitive to whether `N(A)` is an antichain, a dominance
grid, or one strict insertion chain.  This is important: a strict chain can
carry an arbitrary planar order type, but it cannot erase the ordinary
standalone faces of that order type.

## 2. Almost-everywhere heavy shields on the hard slice

The maximum in Theorem 1 is not the only usable conclusion.  Put

\[
 \mathcal H=\{J:d(J)>BD^{-\epsilon}\},
 \quad
 S_0=\{A:\mathcal C_A\cap\mathcal H=\varnothing\}.        \tag{10}
\]

> **Theorem 2 (heavy-shield cover).**
> \[
>                         |S_0|\le D^{-\epsilon}V.          \tag{11}
> \]
> If `|S|>=cV`, then at least `(c-D^{-epsilon})V` actual
> sources carry a member of `H`.  Also
> \[
>                         \Lambda\ge {|S|B\over V}\ge cB.  \tag{12}
> \]
> In addition,
> \[
> \sum_{J\in\mathcal H}d(J)
>    \ge B(|S|-D^{-\epsilon}V),\qquad
> |\mathcal H|\ge
> B\left(1-{D^{-\epsilon}V\over |S|}\right).       \tag{12a}
> \]
> Hence on the hard slice
> `|H|>=B(1-D^{-epsilon}/c)=(1-o(1))B`.

**Proof.**  Every bank incidence from a source in `S_0` lands on a face of
degree at most `BD^{-epsilon}`.  Therefore

\[
 B|S_0|
 \le\sum_{J\notin\mathcal H}d(J)
 \le BD^{-\epsilon}V,
\]

which proves (11).  The first consequence follows by subtraction.  The
average-degree bound (12) is (8) rearranged.  For (12a), the total
incidence mass on faces outside `H` is at most
`BD^{-epsilon}V`, so subtract it from `B|S|`.  Finally every face has
degree at most `|S|`; dividing the remaining incidence mass by `|S|`
gives the cardinality bound.  QED.

The condition `|S|>=cV` is exactly where the low-count/minimizer input is
used.  The theorem does not manufacture that condition for an arbitrary
point set.  Once the existing peak-rank reduction supplies it, however,
the shield conclusion concerns the actual selected repair graph, not a
syntactic history tree and not all exterior incidences.

There is also a useful hybrid with the proper downshadow.  If every source
has a source-face bank `D_A` of size `Q`, with maximum overlap
`Lambda_src`, while `C_A` has maximum overlap `Lambda_sh`, then multiplying
the two incidence counts gives

\[
 \boxed{
 D|S|\le
 D\sqrt{{\Lambda_{\rm src}\Lambda_{\rm sh}\over QB}}\,V.} \tag{13}
\]

For the central proper downshadow, `Q=binom(r,floor(r/2))`.  Equation (13)
is an exact two-reservoir threshold: normalized source-prefix overlap and
normalized shield overlap enter through their geometric mean.  It can be
used before fixing a heavy prefix; after a prefix is fixed, Theorems 1--2
give the standalone shield descent without another ambient-label
pigeonhole.  Indeed, double counting gives
`Q|S|<=Lambda_src V` and `B|S|<=Lambda_sh V`; multiply these two
inequalities, take square roots, and multiply by `D`.

## 3. The reservoir has quadratic entropy

Let `f(D)` be the minimum number of convex subsets in a `D`-point planar
set.  The established lower bound is

\[
                 f(D)\ge2^{(1/4-o(1))(\log D)^2}.           \tag{14}
\]

Take

\[
                         k=\lfloor(\log D)/8\rfloor.        \tag{15}
\]

The number of labelled subsets of size less than `k` is at most

\[
 \sum_{i<k}{D\choose i}
 \le 2^{(1/8+o(1))(\log D)^2}.                             \tag{16}
\]

Subtracting (16) from (14), every `D`-point set has

\[
 2^{(1/4-o(1))(\log D)^2}
\]

convex faces of rank at least `k`.  In particular, for all sufficiently
large `D` we may take

\[
                         B=\left\lfloor
                         2^{(\log D)^2/5}\right\rfloor.     \tag{17}
\]

Substitution of (15)--(17) in Theorems 1--2 proves (1)--(4).

Only the already-proved coefficient `1/4` theorem is used.  Asking for a
coefficient `1/2` internal reservoir would be circular.  The fixed-power
gain comes instead from the fact that even the coefficient-`1/4` bank is
superpolynomial in `D`; failure to route through it forces quadratic
source--shield correlation.

## 4. Why the high-shield branch is real but not yet fatal

The strict nested-chain construction saturates the overlap alternative.
Take a convex base `B` with edge `uv` and nested apices

\[
 x_i\in\operatorname{int}\operatorname{conv}\{u,v,x_j\}
 \quad(i<j).                                             \tag{18}
\]

Use the first `D` apices as the source tips and the last `D` as the selected
blockers.  Every source has addable degree zero and all blocker
neighbourhoods are the same set `Y`.  Therefore every convex face of `Y`
has overlap exactly `D`.  A projective change may give `Y` any prescribed
planar order type.

This example has only `D` sources, so its source entropy is linear in
`log D` and the global face bank discharges it.  It is not a counterexample
to EIC'.  It proves two boundary points:

1. nesting or low addable degree cannot bound `Lambda` in (7);
2. the new content of the hard residual is the simultaneous combination
   of quadratic source entropy and a quadratically reused internal shield.

The latter is strictly narrower than arbitrary one-pocket universality.
A positive completion must use the correlation between the common shield
and its many actual source faces, producing mixed faces or a first-divergence
guard release.  A theorem about the internal blocker order type alone would
have to solve Erdős 838 for that arbitrary order type and is therefore an
838-equivalent restatement, not a closure.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_one_pocket_reservoir/verify_one_pocket_reservoir.py
```

The checker exhausts small selected-neighbourhood incidence systems,
verifies (8), (11), and the hybrid inequality (13), audits the asymptotic
bank constants with exact integers, and constructs an exact rational
zero-addable nested-chain saturation example.
