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
| Arbitrary cross-chart/global decoder | 60% | 79% | Global Hall assembly and bounded-overlap pooling are proved once a compatible reservoir exists; every strict-subhalf counterexample now supplies a scale-matched linear common-circuit core, and exact minimizer/cascade audits isolate positive-mass release as the remaining conversion |
| Final assembled proof | not yet | not yet | The unrestricted lower bridge is still missing |

The proof-architecture / obstruction-map estimate is now about **91%**.
This percentage measures how completely the possible mechanisms and failure
modes have been classified, not how much of the final theorem is proved.

The conservative completed-proof estimate moves only from about **40% to
46%**.  The movement is deliberately small because the headline theorem has
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
5. **The fixed-block mutation evidence was narrowed correctly.**  Exact
   coordinate-annealed configurations through twenty points are stable
   under the stated two-/three-block audits after a short descent.  They are
   all above the coefficient-one-half scale, so they kill an unconditioned
   selector but do not kill a theorem conditioned on a strict sub-half
   deficit.
6. **The strict-subhalf condition now has a scale-matched physical
   consequence.**  A pocket of size `n^(1-delta^2)`, the known quarter
   lower bound, and the rank-half source bank force a bad rectangle larger
   than `V(P)` by `2^((eta_delta-o(1))L^2)`.  After paying all literal
   localization costs, a subrectangle still has quadratic excess and
   shares `Omega_delta(L)` vertex-disjoint bad four-circuits.  This is a
   genuine narrowing, but the circuits are not known to hit all residual
   badness.
7. **The naive common-deletion completion is now closed exactly.** In the
   true nine-point global minimizer, 1,569 of 10,800 induced fixed-circuit
   rectangles have no common-label deletion releasing every record. The
   exact replacement is a residual-circuit cascade with cost
   `(2*binom(n,4))^q`; at live rank this is still quadratic. Finite
   minimizers release at least 25/28 after deleting the full circuit, so a
   quantitative minimizer-specific release theorem remains viable.

## Current closing target

There are still only two honest coefficient-bearing exits.

1. **Fixed-rank / positive-rank-interval gain.**  At `N=4^k`, prove
   `v_k >= 2^((1+eta-o(1))k^2)` for some fixed `eta>0`, or prove the
   equivalent averaged density improvement on a positive rank interval.
   The strong-tree diffuse branch is already closed; the survivor is a
   near-full seam with anti-aligned graded cap/cup profiles.
2. **Strict-deficit positive-mass release or mutation.** Starting from the
   new linear common-circuit rectangle, prove that deleting the common core
   releases a `2^(-o((log n)^2))` fraction, amortize the residual-circuit
   cascade below four fresh labels per step, or produce an actual decreasing
   mutation. A universal common deletion, scalar moments, fixed-core
   toggles, and uniform ordered-block averages are insufficient.

The former micro-target `P1g` is no longer active.  Its exact binary
drop-charged endpoint floor is true, but a verified low-degree spine shows
that it need not put any mass in the target rank.  The next admissible
fixed-rank attack must therefore begin with a genuinely rank-averaged planar
theorem, not another total endpoint inequality or one-layer surrogate.

The strict-sub-half route is now an active **bounded** target rather than a
bare hope, because the linear-pocket theorem provides the written fixed-gap
implication.  It is not yet a gain theorem: no common-core converter or
decreasing mutation is known.  If the bounded repair audit reduces back to
unrestricted two-sided profile composition, this route is to be parked and
the rank-averaged target resumes priority.
