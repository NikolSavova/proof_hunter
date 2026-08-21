# Low cell weight collapses before endpoint scheduling

## 1. Outcome

The balanced-row and capacitated-flow reductions are exact, but their
low-weight repeated-track term is not a second closing gate.  It is already
paid by the same-centre pair reservoir before any endpoint scheduling.

Let a same-centre translate cell `C` have load `r_C>=3`.  It contributes

\[
 p_C=r_C{r_C-1\choose2}=3{r_C\choose3}           \tag{1.1}
\]

pointed records and

\[
 q_C={r_C\choose2}                               \tag{1.2}
\]

units to the physical second moment `Q_phys`.  The exact identity

\[
 \boxed{p_C=(r_C-2)q_C}                          \tag{1.3}
\]

implies, for every integer `R>=3`,

\[
 \boxed{
 \sum_{C:r_C<R}p_C\le(R-3)Q_{phys}
 \le(R-3)W_{parallel}.}                          \tag{1.4}
\]

The same statement remains true after retaining an arbitrary subset of the
`r_C` pointed occurrences in each cell.  In particular it applies to the
high-endpoint population used by the Hall reduction.

Hence, for a subpolynomial `R`, every cell below load `R` is already at the
target scale.  The normalized repeated-track energy is a useful diagnostic
for Hall cores, but no bound for it is needed to close the direct argument.
The only surviving term is

\[
 \boxed{
 M_{\ge R}=\sum_{C:r_C\ge R}(r_C-2){r_C\choose2}.} \tag{1.5}
\]

This is exactly the rich-cell mass in the physical-wedge Carleson gate.

## 2. Dyadic form of the remaining theorem

For `j>=0`, let

\[
 Q_j=\sum_{C:2^jR\le r_C<2^{j+1}R}{r_C\choose2}.
\]

Then

\[
 M_{\ge R}<2R\sum_{j\ge0}2^jQ_j.                \tag{2.1}
\]

Thus the missing input is not another unweighted second-moment estimate:
`sum_j Q_j<=Q_phys` is already known and loses the cell-load factor.  The
sharp target is the reciprocal tail

\[
 \boxed{
 Q_j\le N^{o(1)}{k^3+m^2\over 2^jR}}            \tag{2.2}
\]

in aggregate, or the slightly narrower physical-wedge version

\[
 H_{P,R}\le N^{o(1)}m^2                         \tag{2.3}
\]

from `SWAP_PHYSICAL_WEDGE_DYADIC_CARLESON_GATE.md`.

Every cell in this tail is a synchronized four-line completion block.  It
has a common physical endpoint, two incident directed edges, six literal
`D`-tracks, and the perpendicular footprint `JS-S`.  These decorations are
exactly what must be used to obtain the reciprocal factor in (2.2).

## 3. Relation to the Hall work

If `w(o)=binom(r_C-1,2)<=W`, then

\[
 r_C\le R(W):=\left\lfloor{3+\sqrt{1+8W}\over2}\right\rfloor . \tag{3.1}
\]

Therefore the total low-weight occurrence mass satisfies directly

\[
 \sum_{o:w(o)\le W}w(o)
 \le (R(W)-2)Q_{phys}.                           \tag{3.2}
\]

This is stronger than passing through the Hall deficiency and normalized
repeated-track energy.  The flow theorem remains informative: all stored
Costas stresses route at unit capacity, confirming that endpoint-track
congestion is not the observed obstruction.  But the proof target is now
unambiguously the rich-cell tail (1.5), not a separate fixed-track energy.

## 4. Strategic consequence

The direct `1/3` programme has one major remaining lemma:

> Carleson-pack the high-load physical-wedge cells, with their endpoint and
> six synchronized tracks retained, at scale `N^{o(1)}(k^3+m^2)`.

The resonant subfamily (one of the three coupled directions vanishes) has
decorated quadratic footprints and should be attacked first.  The fully
transverse subfamily must use determinant/height packing or a genuine
density increment.  Pointwise representation depth, anonymous additive
energy, and unweighted repeated-track counts have already been ruled out.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_low_weight_first_moment_collapse.py
```

The verifier exhausts small cell-load multisets and all retained occurrence
subsets, checks (1.1)--(1.4), the exact cutoff (3.1), and the dyadic envelope
(2.1).
