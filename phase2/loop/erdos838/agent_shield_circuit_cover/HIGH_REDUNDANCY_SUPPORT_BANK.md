# Quadratic support redundancy: the exact ambient-bank discharge

**Date:** 2026-08-15.  All logarithms are base two, and the empty face is
counted.

## Verdict

Quadratic coordinate-support redundancy has an unconditional ambient-face
discharge.  The sharp elementary statement is a rank-tax inequality.

Let `E` be a family of `M` distinct ordinary convex faces, each encoded by
an ordered word of length `r`, and let `X_i` be the support of coordinate
`i`.  Put

\[
 P_0=\prod_{i=1}^r|X_i|,\qquad
 R=\log(P_0/M),\qquad N=\left|\bigcup_iX_i\right|.       \tag{1}
\]

If `f(N)` is the minimum number of ordinary convex faces in an `N`-point
planar set, then the induced point set on `union_i X_i` is an ordinary
ambient bank and

\[
 \boxed{
 {V(P)\over M}\ge
 \max\left\{1,{f(N)2^R\over P_0}\right\}.}              \tag{2}
\]

Consequently

\[
 \log{V(P)\over M}
 \ge\left[R+\log f(N)-r\log N\right]_+.                \tag{3}
\]

If the coordinate supports are disjoint, AM--GM improves this to

\[
 \boxed{
 \log{V(P)\over M}
 \ge\left[R+\log f(N)-r\log(N/r)\right]_+.}             \tag{4}
\]

Using the established universal planar bound

\[
                  \log f(N)\ge(1/4-o(1))(\log N)^2,     \tag{5}
\]

equation (4) exactly closes the high-redundancy branch at the critical
source rank.  If

\[
 r=(1/4+o(1))\log N,\qquad R\ge\rho r^2                 \tag{6}
\]

for a fixed `rho>0`, then

\[
             \boxed{V(P)\ge M\,2^{(1-o(1))R}.}          \tag{7}
\]

Together with the entropy-sensitive transcript theorem, this gives a
complete support-redundancy split in that rank window: `R=o(r^2)` permits
homogeneous-product retention at `2^{-o(r^2)}` cost, whereas
`R=Omega(r^2)` is discharged by (7).  This conclusion still presumes the
ordered/simple-chain implication that the selected words are actual
ordinary faces.

More generally, writing `r=(kappa+o(1))log N`,

\[
 \log{V(P)\over M}
 \ge\left[R-(\kappa-1/4+o(1))(\log N)^2\right]_+.       \tag{8}
\]

Thus any quadratic redundancy exceeding the explicit rank tax
`(kappa-1/4)(log N)^2` gives a fixed quadratic, hence fixed-power, gain.
No semialgebraic rectangle extraction is needed in this branch: the entire
induced face complex is used once as a common reservoir.

Even without the critical-rank hypothesis, quadratic redundancy always
gives the requested absolute quadratic bank.  If

\[
                         R\ge\rho r^2,                   \tag{9}
\]

then `P_0>=2^R` and `P_0<=N^r`, so `log N>=rho r`.  Hence

\[
                \boxed{V(P)\ge2^{(\rho^2/4-o(1))r^2}.}  \tag{10}
\]

For disjoint nonempty supports, `P_0<=(N/r)^r`, and the slightly stronger
input `log(N/r)>=rho r` is available.

The theorem is coefficient-sharp as a **support-budget reduction**.  Above
the critical rank, support statistics and the universal quarter reservoir
alone leave the tax in (8).  Removing it requires actual planar
cross-completion, a one-gap/profile bank, or a circuit shield.  The three
named stress families all provide exactly such extra geometry: the
diagonal parabola has a Boolean ambient bank, the MDS radial code has the
complete transversal bank of size `M2^R`, and alternating Ferrers
thresholds release one-gap/opposite-side faces.  No stretchable regression
suppressing all three payments was found.

## 1. Exact support-bank theorem

Let

\[
                         Q=\bigcup_iX_i\subseteq P.      \tag{11}
\]

Every ordinary convex face of the induced order type `Q` is also an
ordinary convex face of `P`: convexity of a subset depends only on that
subset.  Therefore

\[
                         V(P)\ge V(Q)\ge f(N).           \tag{12}
\]

The selected words are distinct ordinary faces, so independently

\[
                         V(P)\ge M.                      \tag{13}
\]

From the definition of support redundancy,

\[
                         M=P_0,2^{-R}.                  \tag{14}
\]

Dividing (12) and (13) by (14) gives (2).  Since every `|X_i|<=N`,
`P_0<=N^r`, which proves (3).  If the `X_i` are disjoint, then
`sum_i|X_i|=N`, and AM--GM gives

\[
                         P_0\le(N/r)^r.                  \tag{15}
\]

This proves (4).

There is no decoder congestion hidden in this argument.  The bank is the
single geometric object `F(Q)`, not one copy for every selected word,
prefix, transcript, or history.  If several selected subfamilies use the
same support union, first merge their distinct words and charge `F(Q)`
once.  Across genuinely different support unions, (2) is only a local
inequality; the usual Hall consolidation is still required.

## 2. Asymptotic consequences

Write `L=log N`.  Substituting (5) into (4) gives

\[
 \log{V(P)\over M}
 \ge\left[R+{L^2\over4}-r(L-\log r)-o(L^2)\right]_+.    \tag{16}
\]

Dropping the favorable `r log r` term yields

\[
 \log{V(P)\over M}
 \ge\left[R+{L^2\over4}-rL-o(L^2)\right]_+,             \tag{17}
\]

which is (8).  Under (6), `r=Theta(L)` and `R=Omega(L^2)`, so the
`o(L^2)` error is `o(R)` and (7) follows.  If instead
`r<=(1/4-delta)L`, the bank gains at least

\[
                   R+\delta L^2-o(L^2),                 \tag{18}
\]

which is stronger than merely paying the redundancy.

For the absolute statement, (14) and `M>=1` give `2^R<=P_0`.  In the
overlapping-support case `P_0<=N^r`, and therefore `L>=R/r`.  Equations
(5) and (9) imply

\[
 \log V(P)\ge(1/4-o(1))L^2
             \ge(\rho^2/4-o(1))r^2,                    \tag{19}
\]

which proves (10).  Notice that (10) is absolute; it need not multiply a
selected family which already occupies most of the ambient face complex.

## 3. The exact rank-tax boundary

The following table records what (17) proves when
`r=(kappa+o(1))L` and `R=(eta+o(1))L^2`.

| regime | guaranteed `log(V/M)/L^2` |
|---|---:|
| `kappa<1/4` | `eta+1/4-kappa-o(1)` |
| `kappa=1/4` | `eta-o(1)` |
| `kappa>1/4` | `[eta-(kappa-1/4)]_+-o(1)` |

This is the honest boundary of the support-only argument.  For example,
the formal data

\[
 r=L/2,\quad \log P_0=L^2/2,\quad
 R=L^2/8,\quad \log M=3L^2/8                         \tag{20}
\]

are compatible with `M<=P_0` and with the quarter lower bound while
leaving no forced multiplicative gain over `M`.  This is not asserted to
be a planar construction.  It proves only that support entropy plus (5)
cannot remove the rank tax.  A theorem beyond (8) must use the prescribed
orientation signs geometrically.

The coefficient-half recursive configurations do not presently furnish a
counterexample.  Their dominant cap/cup choices are nearly Cartesian; the
ambient cross terms in the exact substitution recurrence pay the support
surplus at the same leading scale.  Thus they stress (8) but do not kill a
genuine planar redundancy-to-face theorem.

## 4. Three exact stress tests

### 4.1 Diagonal parabola

Take `r=3d` separated coordinate intervals on the parabola
`p(t)=(t,t^2)`, each containing `N_0` points.  In each consecutive triple
of coordinates require the same local label, independently between the
`d` triples.  Then

\[
 M=N_0^d,\qquad P_0=N_0^{3d}=M^3,\qquad R=2\log M.       \tag{21}
\]

Every increasing triple has positive orientation.  More importantly,
every subset of the `3dN_0` parabola points is an ordinary face, so

\[
                         V=2^{3dN_0}.                    \tag{22}
\]

The maximally correlated selected family is therefore paid by an enormous
ambient Boolean bank.  It is a barrier to product-cell **retention**, not
to support-bank discharge.

### 4.2 MDS radial code

Let `E` be a length-`q`, dimension-`k` Reed--Solomon code over
`F_p`, realized by one point in each of `q` separated convex macroclusters.
Every coordinate projection is all of `F_p`, so

\[
 M=p^k,\qquad P_0=p^q,\qquad R=(q-k)\log p.              \tag{23}
\]

All `p^q` ambient transversals are ordinary.  Thus the most elementary
ambient bank already has

\[
                         P_0=M2^R                        \tag{24}
\]

members.  Minimum distance can destroy selected Cartesian modules, but it
cannot destroy the ambient redundancy payment.

### 4.3 Alternating Ferrers thresholds

In the exact four-cell rational configuration from
`ALTERNATING_FERRERS_PLANAR_WRAPPER.md`, the four constant words

\[
                   (1,1,1,1),\ldots,(4,4,4,4)           \tag{25}
\]

are all valid ordinary singleton-ear faces and cover every label in every
coordinate.  Hence `M=4`, `P_0=4^4`, and `R=6=(3/8)r^2`.  There are only
70 valid full singleton words, so the missing support box is not recovered
as positive transversals.  Exact circuit closure nevertheless gives

\[
 V(P)=9722>4\cdot2^6,                                  \tag{26}
\]

with detached one-gap layers `216,196,216,196` and two complete opposite
`13 by 13` rectangles.  This is the finite model of the required
one-gap/local-profile payment when consecutive Ferrers signs anti-align.

## 5. Scope

The conclusion needed from high support redundancy should be stated in two
levels.

1. **Unconditional:** `R=Omega(r^2)` forces an ordinary induced ambient
   bank of size `2^{Omega(r^2)}` by (10).
2. **Multiplicative at critical rank:** if the branch has
   `r=(1/4+o(1))log N`, the same bank has size
   `M2^{(1-o(1))R}` by (7).

For `r>(1/4+Omega(1))log N` and redundancy below the threshold in (8), the
support theorem alone does not close a relative Hall demand.  The live
geometric target there is exactly an ambient positive-transversal,
one-gap/profile, or circuit-shield theorem.  The named scalable tests all
pay through one of those mechanisms, so they provide no counterexample.

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_high_redundancy_support_bank.py
```

The verifier checks the exact support identities and AM--GM inequality,
the rank-tax coefficient table, the diagonal parabola construction, a
small Reed--Solomon code and its complete transversal bank, and the exact
four-cell alternating-Ferrers geometry and face count.
