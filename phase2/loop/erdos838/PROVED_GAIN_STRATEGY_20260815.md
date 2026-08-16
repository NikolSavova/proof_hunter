# Erdős 838: one proved-gain target and stop rule

## Decision

The next primary target is not the full half-weight conjecture, peak mean, or
another unrestricted decoder reformulation.  It is a fixed-size
supersaturation theorem that would move the unconditional coefficient.

Let `v_k(P)` be the number of convex `k`-subsets.  At the canonical size
`|P|=4^k`, prove, for one explicit constant `eta>0`,

\[
       v_k(P)\ge 2^{(1+\eta-o(1))k^2}.                 \tag{P1}
\]

The standard hereditary double count then improves the unrestricted lower
coefficient from `1/4` to

\[
                       \frac{1+\eta}{4}.
\]

The aspirational value `eta=1/2` gives `3/8`, but **any fixed positive eta is
a publishable theorem gain**.  This target is quantitatively and logically
strictly weaker than proving the full `1/2` lower coefficient.

## Why this target

1. It has an immediate numerical success criterion; a route cannot disguise
   an equivalent reformulation as progress.
2. It uses the campaign's strongest positive tools: rank-sensitive deletion,
   pooled Hall allocation, global rank-three ES replacement, and exact
   construction-side stress tests.
3. It focuses attention on the remaining intermediate literal-history ranks
   instead of the entire face complex.
4. A failure can still yield a clean rank-range theorem or an explicit
   counter-regression suitable for the barrier note.

## Bounded attack plan

### Stage A: verify the bridge

The implication `(P1) => liminf >= (1+eta)/4`, including all rounding and
`o(k)` losses, is proved in `FIXED_SIZE_GAIN_BRIDGE_20260815.md` and checked
by `verify_fixed_size_gain_bridge.py`.  The canonical size `4^k` avoids the
uniformity trap in the earlier shorthand `2^{2k+o(k)}`.

### Stage B: isolate one rank window

Use the existing literal-history results only after V5 is audited:

- `r=o(sqrt(log n))`: global ES replacement;
- at the canonical size `n=4^k`, every literal
  `r<=(1/2-delta)k=(1/4-delta/2)log n` is now jointly replaceable with
  load/fibre one by `FIXED_SIZE_LITERAL_QUARTER_LOG_POOLING_GATE_20260815.md`;
- `r>=log n`: identity/no replacement;
- focus exclusively on
  `(1/4-o(1))log n <= r < log n` in the fixed-size attack.

No unrestricted recursive call on a comparably sized arbitrary child is
allowed; that would be marked `EQUIVALENT` in the difficulty ledger.

The first construction-side reduction is now proved in
`STRONG_TREE_FIXED_RANK_COMB_OR_SEAM_GATE.md`: every diffuse heavy-path
branch gives `2^{2k^2-o(k^2)}` rank-`k` faces, so a strong-tree survivor has
one seam with both children of size `4^k/poly(k)`.  The next strong-tree
subtarget is only the graded profile alignment at that seam.

There is now an exact prior-art translation of that subtarget.  As recorded
in `FIXED_RANK_STRONG_TREE_CATERPILLAR_AUDIT_20260815.md`, strong-tree faces
are plane caterpillar leaf sets whose spine has at most one turn.  The known
minimum-density theorem for unordered rooted caterpillars has exactly the
desired `3k^2/2` main exponent, but it fixes `k`, has an error that dominates
when `|T|=4^k`, and forgets the left/right itinerary.  Only a uniform,
orientation-sensitive strengthening is relevant; fixed-`k` inducibility is
not to be cited as closure.

### Stage C: one promotion dichotomy

Seek a theorem of the following ordinary combinatorial form, stated without
new geometric nomenclature:

> A rank-`r` selected history family either has a pooled ordinary-face code
> with total load `2^{o(k^2)}`, or its failure supplies enough additional
> rank-`k` convex subsets to prove `(P1)`.

The theorem must be tested on the saved Pascal, matching-star, nested-cage,
one-exception, and vertical-substitution regressions before promotion.

### Stage D: independent audit before recursion

If a candidate lemma survives exact tests, send its complete statement,
proof, and artifacts to the other model.  Do not build a second reduction
layer until the verdict is `PASS` or `MINOR_REPAIR` and repaired.

## Kill criterion

Stop this attack and return to the publishable upper/barrier package if any of
the following occurs:

1. the target is reduced to the unrestricted lower bound on a comparable
   arbitrary point set;
2. three successive reductions produce no explicit positive `eta` or new
   proved rank range;
3. two independent candidate lemmas are killed by existing saved
   regressions;
4. the proof requires an unaudited load-bearing lemma outside V1--V5;
5. after two bounded attack/audit cycles there is no theorem implying
   `eta>0`.

At that point the correct deliverable is the existing `1/2` upper theorem,
the sharp strong-tree theorem, and a curated barrier/construction-closure
note.  The 13,000-line attack remains archived evidence, not the paper.
