# Erdos 838 progress bar checkpoint

**Date:** 2026-08-17  
**Comparison:** apples-to-apples with `PROGRESS_BAR_20260816.md`.

## Component bar

| Component | 2026-08-16 | 2026-08-17 | Movement |
|---|---:|---:|---|
| Prior-art/adversarial kill search | 100% | 100% | Complete; no regression |
| Construction-side recursive threats | 95% | 98% | Finite/variable grammars and polynomially imbalanced heterogeneous rows now close at coefficient one half; only near-star scale separation or failure of same-chart inheritance survives |
| Exact minimizer/root reduction | 95% | 97% | Exact two-/three-point and uniform ordered `q`-block mutation formulae obtained; fixed `q>=4` is now a proved barrier rather than an open escape |
| Local cap/cup/history structure | 95% | 98% | Exact hinged Kraft, pooled rank promotion, and label-replacing codes solve several natural and hostile local interfaces |
| Decoder on canonical `E(k,k)` extremals | 100% | 100% | Complete, including coherent-root terminal histories |
| Arbitrary cross-chart/global decoder | 60% | 75% | Global Hall assembly and bounded-overlap pooling are proved once a compatible reservoir exists; arbitrary-minimizer reservoir production remains open |
| Final assembled proof | not yet | not yet | The unrestricted lower bridge is still missing |

The proof-architecture / obstruction-map estimate is now about **88%**.
This percentage measures how completely the possible mechanisms and failure
modes have been classified, not how much of the final theorem is proved.

The conservative completed-proof estimate moves only from about **40% to
45%**.  The movement is deliberately small because the headline theorem has
not improved: the last bridge can still contain most of the mathematical
difficulty.

## Rigorous theorem bar

- Proven upper side: `limsup <= 1/2`.
- Proven lower side: `liminf >= 1/4`.
- New unconditional lower-coefficient gain: **none yet**.
- Current rigorous window: **`[1/4,1/2]`**.

Thus we have **progressed without closing**.  We have not regressed: every
discarded route was killed by an exact theorem or verified counterexample,
and the surviving target is narrower.  But measured solely by the best
unrestricted coefficient, we are still stuck at the same place.

## What moved since the prior checkpoint

1. **Uniform multi-block minimizer mutations are completely accounted for.**
   The exact kernel `Psi_q` is known for every fixed `q`.  Intermediate
   singleton blocks return the apparent Gibbs saving for `q>=4`; `q=3`
   only improves an extreme-rank tail.  This closes an entire proposed
   minimizer route without weakening the theorem.
2. **Heterogeneous recursive constructions are much more tightly fenced.**
   The exact dyadic square mesh has only local `O(L log L)` loss, and an
   arbitrary-depth recursion with sibling ratio at most `m^(1-delta)` still
   has coefficient at least one half.  A construction-side survivor must
   now create near-total scale separation, macroscopic arity, or destroy
   same-target/profile inheritance.
3. **The decoder problem has split cleanly into capacity versus geometry.**
   Pooled label-replacing codes solve `E(k,k)`, matching-star, and bounded
   rank-history stress tests with constant or unit load.  What remains is
   not abstract Hall capacity; it is forcing the compatible mixed reservoir
   inside an arbitrary low-face minimizer.
4. **Several false shortcuts were removed exactly.**  Weighted hinge,
   nested-threshold uncrossing, natural local two-tangent Hall, and uniform
   higher-block Gibbs improvement all have certified counterexamples or
   exact ceilings.  This is conceptual progress but no coefficient gain.

## Current closing target

There are still only two honest coefficient-bearing exits.

1. **Fixed-rank / positive-rank-interval gain.**  At `N=4^k`, prove
   `v_k >= 2^((1+eta-o(1))k^2)` for some fixed `eta>0`, or prove the
   equivalent averaged density improvement on a positive rank interval.
   The strong-tree diffuse branch is already closed; the survivor is a
   near-full seam with anti-aligned graded cap/cup profiles.
2. **Genuinely multi-point minimizer mutation.**  Produce an actual
   decreasing mutation or compatible mixed-face reservoir in the stationary
   all-delete / anti-aligned state.  Scalar deletion moments and uniform
   ordered block averages are now known to be insufficient.

The active micro-target `P1g` is an exact binary drop-charged endpoint floor.
It is useful only if it propagates to a graded rank interval; if it improves
only total endpoint mass, the ledger requires banking it and stopping that
branch.
