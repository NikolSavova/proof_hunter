# Mixed projected support switches to same-key reuse

## 1. Outcome

The dominant mixed `V`--`W` block is mostly distinct projected-key support,
so a pointwise codegree estimate does not address it.  Its support graph has
an exact coloured-rectangle switch which reduces every dense core to two
already geometric populations.

Let `H=(mathcal V,mathcal W,E)` be the simple bipartite graph whose vertices
are oriented projected completion keys and whose edge `vw` means that the
two keys occur together in at least one endpoint group `(C,x,u)`.  Choose
canonically one such group and colour the edge by it:

\[
 \kappa:E(H)\longrightarrow\mathfrak G.                  \tag{1.1}
\]

A four-cycle has either:

1. one colour on all four edges, in which case four projected keys coexist
   in one literal endpoint group; or
2. at least two vertices whose incident cycle edges have different colours,
   in which case the projected key at each such vertex is reused in two
   distinct groups.

There is no third case.  Thus a rectangle-rich mixed-support core switches
losslessly to either a monochromatic four-record group block or the
cross-group same-key reuse controlled by the four-norm inversion.

## 2. Exact quantitative form

Write

\[
 n=|\mathcal V|,\qquad m=|\mathcal W|,\qquad E=|E(H)|.
\]

Let

\[
 S_{\mathcal V}=\sum_{v\in\mathcal V}{d(v)\choose2},
 \qquad
 S_{\mathcal W}=\sum_{w\in\mathcal W}{d(w)\choose2}.     \tag{2.1}
\]

If `Q` is the number of support four-cycles, then

\[
 Q=\sum_{\{w,w'\}\subset\mathcal W}
       { |N(w)\cap N(w')|\choose2}                        \tag{2.2}
\]

and symmetrically on the other side.  Cauchy gives the exact real-valued
lower bounds

\[
 S_{\mathcal V}\ge {E^2\over2n}-{E\over2},\qquad
 S_{\mathcal W}\ge {E^2\over2m}-{E\over2},               \tag{2.3}
\]

\[
 Q\ge {S_{\mathcal V}^2\over2{m\choose2}}
          -{S_{\mathcal V}\over2},\qquad
 Q\ge {S_{\mathcal W}^2\over2{n\choose2}}
          -{S_{\mathcal W}\over2},                       \tag{2.4}
\]

whenever the displayed denominator is nonzero.

Let `Q_0` be the monochromatic four-cycle count.  Let `R_cross` be the
number of wedges at a projected key whose two incident support edges have
different chosen groups.  Finally put

\[
 \Delta=max\{|N(a)\cap N(b)|:a\ne b
          \text{ lie on the same side of }H\}.             \tag{2.5}
\]

Then

\[
\boxed{
 2(Q-Q_0)\le(\Delta-1)R_{\rm cross}.}                     \tag{2.6}
\]

Indeed, every nonmonochromatic cycle has at least two colour-changing
vertices.  A fixed colour-changing wedge extends to at most `Delta-1`
four-cycles.  Double counting these incidences proves (2.6).

Combining (2.3)--(2.6) is the exact density split:

* small `E` is paid from the projected-key vertex reservoir;
* large `E` forces many rectangles;
* those rectangles force large `Q_0`, large cross-group same-key reuse, or
  a large same-side common-neighbour fibre `Delta`.

All three survivors retain their endpoint group, physical role, adaptive
popular keys, and full completion coordinates.  No unlabelled graph
relaxation has been introduced.

There is also an exact normalization against the projected-key reservoir.
Each oriented projected key has one of two moving roles and one of four
physical endpoint orientations, so

\[
 |V(H)|\le 8\mathcal W_{\parallel}.                       \tag{2.7}
\]

If `d(H)` is the degeneracy of the simple support graph, peeling a
minimum-degree vertex gives

\[
 |E(H)|\le d(H)|V(H)|\le 8d(H)\mathcal W_{\parallel}.     \tag{2.8}
\]

Finally, if `c(e)` is the number of endpoint groups witnessing one support
edge, then the elementary pointwise inequality

\[
 c(e)\le 1+{c(e)\choose2}                                \tag{2.9}
\]

gives

\[
 \sum_{e\in E(H)}c(e)
 \le |E(H)|+\sum_{e\in E(H)}{c(e)\choose2}.              \tag{2.10}
\]

Thus subpolynomial support degeneracy together with a target-scale
same-pair collision bound would close the mixed incidence mass.  This is a
sufficient criterion, not yet the desired theorem: an `O(K)` degeneracy
bound may lose exactly the adaptive factor which the projected reservoir is
supposed to save.  The live target is therefore a weighted version of
(2.8), coupled losslessly to the factor-`K` reservoir, rather than an
unweighted maximum-degeneracy estimate.

## 3. Geometric meaning of the two branches

Every connected component of `H` is localized at one oriented physical
endpoint.  If the canonical endpoint orientations are represented by signs
`sigma_V,sigma_W`, each support edge has

\[
 \sigma_WB-\sigma_VC\in D.                              \tag{3.1}
\]

For a monochromatic rectangle, one group contains two moving-`V` and two
moving-`W` records.  It therefore retains one centre `(C,x,u)`, four
projected keys, the associated completion corners, and all adaptive-popular
constraints.  This is a local four-record endpoint block, not an abstract
`K_{2,2}`.

At a colour-changing vertex, two distinct groups contain occurrences of
the same projected key.  The key plus four squared norms recovers each
occurrence with load at most sixteen by
`SWAP_PROJECTED_KEY_FOUR_NORM_INVERSION_GATE.md`.  Hence the second branch
is exactly the cross-group metric-cell reuse already isolated by the
Carleson program.

The large common-neighbour alternative `Delta` is itself a two-sided
completion core: two fixed half-completion keys coexist with many keys of
the opposite type at one physical endpoint.  It should be retained as the
density-increment object rather than bounded by an unlabelled KST estimate.

## 4. Exact stress

The augmented optimal-core analyzer reports, for Costas sizes `29,31,37`,
the mixed support graph rows

\[
\begin{array}{c|rrrrrrr}
 &E&|\operatorname{supp}E|&|V(H)|&d_{\max}&d(H)&\Delta&Q\\ \hline
29&38128&31830&12719&57&9&34&93378\\
31&18984&13006& 5633&62&10&38&94333\\
37&54560&47660&19724&59&8&22&114090.
\end{array}                                               \tag{4.1}
\]

Here the first column is incidence mass and the second is the number of
simple support edges.  The canonical-owner transition profiles are

\[
\begin{array}{c|rrrr}
 &0&2&3&4\\ \hline
29&430&4120&17809&71019\\
31&262&3732&17305&73034\\
37&353&3741&16389&93607.
\end{array}                                               \tag{4.2}
\]

The column is the number of colour-changing vertices on a four-cycle.
Thus only `0.46%,0.28%,0.31%` of the rectangles are monochromatic.  More
than `99.5%` of the genuine stress switches to cross-group same-key reuse,
usually at three or four vertices.  This is decisive evidence that the
rectangle switch targets the load-bearing branch.

The exact degeneracies `9,10,8` are much smaller than the maximum degrees,
but they are finite calibration only.  In the live normalization even a
degeneracy of order `K` can be one power too large unless the peeling charge
retains the factor-`K` projected reservoir.

Run

```bash
python3 phase2/loop/erdos1208/analyze_swap_optimal_nested_cores.py \
  --large-costas-only
```

to reproduce the rows.

## 5. Verification and remaining theorem

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_mixed_support_rectangle_switch.py
```

The verifier exhausts 5,000 random finite coloured bipartite graphs and
checks the wedge identities, both Cauchy lower bounds, the owner transition
dichotomy, and (2.6).  It also checks the monochromatic complete-block and
proper-colouring extremes exactly.

The remaining global input is now a normalized charge for the right side
of (2.6): after dyadic pruning, bound colour-changing same-key wedges by the
four-norm metric-cell reservoir, and bound the much smaller monochromatic
blocks directly inside one endpoint group.  Together with the same-role
three-channel sums, this would give the required `G_2` estimate.  No mixed
role inversion or support classification remains open.
