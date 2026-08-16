# Erdős 838: autopsy of the bounded fixed-size attack

**Date:** 2026-08-16. This note applies the stop rule in
`PROVED_GAIN_STRATEGY_20260815.md`. It preserves the proved components of the
fixed-size campaign and closes only its current reduction chain.

## Verdict

The fixed-size target

\[
 \min_{|P|=4^k}v_k(P)\ge 2^{(1+\eta-o(1))k^2}
 \tag{P1}
\]

remains a valid strict route to an unconditional coefficient gain, but the
bounded attack selected on 2026-08-15 has reached its precommitted stop rule.
It produced genuine range and construction-class theorems, then failed to
produce any fixed $\eta>0$ after two candidate promotion lemmas were killed.
The chain is therefore parked rather than renamed.

The unconditional theorem remains

\[
 {1\over4}\le\liminf {\log f(n)\over(\log n)^2}
 \le\limsup {\log f(n)\over(\log n)^2}\le {1\over2}.
 \tag{1}
\]

## What the attack proved

1. `FIXED_SIZE_GAIN_BRIDGE_20260815.md` proves exactly that (P1) would raise
   the unrestricted lower coefficient to $(1+\eta)/4$.
2. `FIXED_SIZE_LITERAL_EXPLICIT_BOUNDARY_20260816.md` gives a joint
   load-one, fibre-one code for literal histories through
   \[
   r\le {1\over4}\log n-O(\sqrt{\log n\log\log n}).
   \]
3. `STRONG_TREE_FIXED_RANK_COMB_OR_SEAM_GATE.md` removes the diffuse
   strong-tree branch: it either supplies $2^{2k^2-o(k^2)}$ rank-$k$ faces
   or exposes one large two-child seam.
4. `UNIFORM_GROWING_RANK_ROOTED_CATERPILLAR_THEOREM_20260816.md` removes the
   nonuniform finite-size error from growing-rank unordered caterpillar
   counts. The remaining ordered orientation comparison is isolated and
   its naive same-constant form is false.
5. `FIXED_SIZE_SUPERSATURATION_PRIOR_ART_AUDIT_20260816.md` proves that the
   standard fixed-$k$ counts, a single positive-fraction transversal box,
   and scalar polygon identities cannot cross the coefficient-one boundary.
6. `SUCCESSIVE_RANK_DENSITY_GAIN_GATE_20260816.md` gives an exact alternative
   sufficient condition: any average density-decay constant $c<2$ on a
   positive fraction of the ranks would yield an explicit gain.

These statements remain useful. None is being retracted.

## The two killed promotion lemmas

The first candidate was the no-slack adjacent inequality

\[
 p_{j+1}\ge 2^{-j}p_j.
 \tag{2}
\]

The rational $16$-point double chain has
$p_5/p_4=5/99<1/16$. Although this finite failure did not kill the averaged
asymptotic target, it ruled out the proposed local theorem.

The replacement candidate P1e asked for a weakened adjacent balance at one
fixed certified sequence $q_j\ge ES(j+1)$ with $\log q_j=j+o(j)$. The exact
quantifier-safe construction in
`FIXED_THRESHOLD_ADJACENT_LAYER_COUNTEREXAMPLE_20260816.md` now gives, at
the prescribed size $q_j$,

\[
 \log {v_j(Q_j)\over v_{j+1}(Q_j)}
 \ge\left(1-{1\over4\ln2}-{41\over70}-o(1)\right)j^2,
 \tag{3}
\]

where the constant is $0.053611954\ldots>0$. This kills P1e by a quadratic,
not marginal, gap. The construction is rational and stretchable.

## Why no third reduction is opened

The averaged density statement P1d is still mathematically possible and all
audited recursive extremal families lie comfortably on its good side. But
after (2)--(3), replacing P1e by a further one-layer, short-window, or
"cliff-charging" statement would be a third reduction without a coefficient
gain. That is exactly the behavior the difficulty ledger forbids.

Any future return to (P1) must begin with a genuinely new planar theorem
that already averages a positive fraction of the ranks or directly creates
rank-$k$ faces. It must not use another threshold-layer surrogate.

## Consequence for the research program

The next deliverable is the independently checkable upper/construction-class
and barrier package already identified by the external critique. Continued
work on the full conjecture should use a different direct state, such as a
strict minimizer mean-size gain, and must again begin with a written
coefficient implication and kill criterion.

The fixed-size route is parked, not disproved: (P1), P1d, and the original
Erdős problem all remain open.
