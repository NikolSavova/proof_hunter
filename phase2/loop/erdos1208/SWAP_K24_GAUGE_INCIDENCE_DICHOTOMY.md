# Gauge-incidence dichotomy for selected K2,4 fibres

> **Status update.**  The incidence sets `S_C` below are not arbitrary.
> They are intersections of the bare `K_{2,4}` fibre with translates of one
> fourfold adaptive-popular selector.  The exact three-factor tensor in
> `SWAP_K24_ADAPTIVE_POPULAR_THREE_FACTOR_GATE.md` strictly sharpens this
> low/high degree split; the inequalities here remain a valid fallback.

## 1. Outcome

The endpoint-coloured `K_{2,4}` key in
`SWAP_SELECTED_CORE_K24_CROSS_SUM_NORMAL_FORM.md` reindexes the physical
rich-cell mass exactly.  If the physical endpoint is deleted, different
gauge translates can acquire the same four-colour key.  This note gives the
lossless low/high split for that merger.

For one bare four-colour key `kappa`, let `C_kappa` be its selected physical
owner cells.  Each cell `C` has a set

\[
 S_C\subset D
\]

of first-track values `F_0`, and `r_C=|S_C|`.  Put

\[
 \mu_\kappa(f)=|\{C\in\mathcal C_\kappa:f\in S_C\}|. \tag{1.1}
\]

The complete-invariant theorem says that fixed `(kappa,f)` fixes all six
literal directed tracks.  Thus `mu_kappa(f)` is not an anonymous overlap:
it is precisely the number of physical wedge gauges carrying one fixed
six-track occurrence.

For every threshold `Delta>=2`, the selected third mass splits into

\[
\boxed{\begin{aligned}
 3\sum_{\kappa,C}{r_C\choose3}
 &\le 3(\Delta-1)\sum_\kappa{\lambda_\kappa\choose3}
      +\mathcal G_\Delta,\\
 \mathcal G_\Delta
 &=3\sum_{\substack{\kappa,f:\mu_\kappa(f)\ge\Delta}}
       \sum_{C\ni f}{r_C-1\choose2},
\end{aligned}}                                      \tag{1.2}
\]

where

\[
 \lambda_\kappa=\left|\bigcup_{C\in\mathcal C_\kappa}S_C\right|. \tag{1.3}
\]

The first term is a subpolynomial multiple of the *unique-track* ambient
K2,4 third energy.  The second is an explicit gauge-rich physical-wedge
pencil with all six tracks fixed.  No endpoint multiplicity remains hidden
between these two terms.

## 2. Proof

Call `f` high when `mu_kappa(f)>=Delta`.  For one cell write

\[
 h_C=|S_C\cap H_\kappa|,
 \qquad \ell_C=r_C-h_C.                            \tag{2.1}
\]

Every all-low triple of first tracks is contained in at most `Delta-1`
cells: its cell codegree is at most the degree of each of its three
vertices.  Therefore

\[
 \sum_{C\in\mathcal C_\kappa}{\ell_C\choose3}
 \le(\Delta-1){\lambda_\kappa\choose3}.           \tag{2.2}
\]

Every remaining triple contains at least one high first track.  Marking
one such member and forgetting which of the other two was marked gives

\[
 {r_C\choose3}-{\ell_C\choose3}
 \le h_C{r_C-1\choose2}.                         \tag{2.3}
\]

Summing (2.2)--(2.3) proves (1.2).

The factor `Delta-1` is power-sharp.  If `mu` gauge cells all contain the
same `r` first tracks, their selected mass is

\[
 3\mu{r\choose3},                                  \tag{2.4}
\]

while the unique-track ambient mass is only `3 binom(r,3)`.  Below the
threshold `mu+1`, equality holds in the multiplicity factor.  At threshold
`mu`, the whole block moves into `G_Delta`.  Consequently neither term of
(1.2) may simply be discarded.

## 3. Geometric meaning of the high term

Fix `(kappa,f)`.  Equations (3.2)--(3.3) of the normal-form note recover
`(R,a,b,e)` and all six tracks.  A gauge occurrence is therefore determined
only by a physical wedge

\[
 R=JV+W                                             \tag{3.1}
\]

whose two directed edges share the recorded physical endpoint.  For fixed
endpoint roles, distance-Sidonicity gives at most one such wedge through
each point of `A`; hence

\[
 \mu_\kappa(f)\le4k.                               \tag{3.2}
\]

This linear cap is sharp for the known polynomial planting and cannot close
the aggregate by itself.  The gain in (1.2) is that the difficult branch is
now a *full-track gauge pencil*: the parameter, the six directed edges,
the cross-sum colours, and the invariant `R` are all fixed.  Only the
three-point physical wedge moves.

Thus a sufficient pair of theorems for the rich-cell gate is

\[
 \sum_\kappa{\lambda_\kappa\choose3}
 \le N^{o(1)}(k^3+m^2)                             \tag{3.3}
\]

and, for one subpolynomial `Delta`,

\[
 \mathcal G_\Delta\le N^{o(1)}(k^3+m^2).          \tag{3.4}
\]

Equation (3.3) is the coloured diagonal correlation (5.7) of the K2,4
normal form.  Equation (3.4) is narrower than the previous endpoint-pencil
gate because a high column fixes the complete track tuple rather than one
endpoint-labelled track.

## 4. Genuine stress and strategic verdict

The optimal-core analyzer now reconstructs both keys.  On transformed
Costas `23` it reports

\[
\begin{array}{c|c|c|c|c}
 &\#\text{ keys}&\max r&3\sum\binom r3&
   \text{load histogram}\\ \hline
\text{endpoint-coloured}&68&3&204&(3:68)\\
\text{bare}&64&6&420&(3:60,\ 6:4).
\end{array}                                        \tag{4.1}
\]

Thus (4.1) verifies two points at once.

1. The endpoint-coloured reindexing is exactly lossless on the first
   nonzero genuine selected core.
2. Deleting the physical endpoint is already non-lossless: four pairs of
   cells merge into load-six bare keys, more than doubling the cubic mass.

Accordingly, an attack on (3.3) alone is unsafe unless it is accompanied by
the gauge split (1.2).  The immediate proof target is now binary: bound the
unique-track coloured correlation, or construct a selected-core
counterexample; independently, Carleson-pack the much smaller fixed-track
gauge pencils in (3.4).

## 5. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_k24_gauge_incidence_dichotomy.py
python3 phase2/loop/erdos1208/analyze_swap_optimal_nested_cores.py --extended
```

The first verifier exhausts every `3 x 3` incidence matrix, tests seeded
multi-key systems, and checks the sharp complete-rectangle and disjoint
models.  The analyzer independently reconstructs the physical cells and
all cross-sum representations from genuine distance-Sidon endpoints and
asserts the lossless endpoint-coloured identity before printing (4.1).
