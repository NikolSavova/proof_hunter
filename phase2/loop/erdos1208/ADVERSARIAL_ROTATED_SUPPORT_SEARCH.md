# Adversarial rotated-support search — 2026-08-17

## Plain-language summary

The first optimizer aimed directly at the proposed full-resolution invariant,
rather than sampling convenient constructions.  It repeatedly replaces one
point while preserving every squared-distance constraint and minimizes
`|A+JA-JA|`.  Through `k=28`, it lowers the friendly-family constants but finds
no declining power law: the best support remains between `0.626k^3` and
`0.703k^3`.  The optimized sets are wide—at most four tested points collinear—
and their transverse translate-collision counts remain a constant multiple of
`k^3`.  This is a passed viability test, not proof of the asymptotic theorem.

## 1. Pre-registered question

The conjectural lemma

\[
 |A+JA-JA|\ge |A|^{3-o(1)}                       \tag{1.1}
\]

would resolve the power-law order of Erdős #1208.  Before another proof lane,
the search was required to minimize

\[
 \rho(A)=\frac{|A+JA-JA|}{|A|^3}                 \tag{1.2}
\]

over lattice distance-Sidon sets.  A trend `rho(A)<=k^{-epsilon}` would kill
(1.1); a constant lower envelope merely licenses further proof work.

## 2. Method

`search_rotated_support.py` uses exact integer arithmetic.  Its state contains
the unique squared-distance set and the full representation counter for
`a+Jb-Jc`.  A proposed one-point replacement is rejected unless all new
distances are mutually new.  For a valid move, only the `O(k^2)` triples using
the replaced index are updated.  Simulated annealing accepts some uphill moves;
every final witness is independently rechecked from scratch.

The run recorded here used

```bash
python3 phase2/loop/erdos1208/search_rotated_support.py \
  --sizes 12,16,20,24,28 --steps 40000 --restarts 8 \
  --side-factor 5 --seed 1208
```

The search boxes were intentionally wider than the final witnesses.  Random
greedy sets and two-arm Mian--Chowla perpendicular rulers supplied the cheap
baselines.

## 3. Exact results

| `k` | baseline support | optimized support | support / `k^3` | parallel collisions | transverse collisions / `k^3` | largest line |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 1,446 | 1,083 | 0.626736111 | 13 | 0.379629630 | 3 |
| 16 | 3,408 | 2,669 | 0.651611328 | 15 | 0.377441406 | 4 |
| 20 | 6,716 | 5,216 | 0.652000000 | 7 | 0.402500000 | 3 |
| 24 | 11,578 | 9,468 | 0.684895833 | 12 | 0.357349537 | 3 |
| 28 | 18,202 | 15,411 | 0.702031706 | 23 | 0.337190233 | 2 |

The rising tail is not evidence of monotonicity: valid one-point moves become
scarcer with `k`, so the larger instances are less thoroughly optimized.  The
important negative observation is that no decaying ratio appears.

`verify_adversarial_support_witnesses.py` stores the five witnesses and checks
their distance uniqueness, exact support, line bound, line richness, and
parallel/transverse collision counts independently of the annealing loop.

## 4. Structural signal and controls

The optimizer sometimes creates short collinear clusters, motivating the
parallel-line theorem in `PARALLEL_LINE_SUPPORT_LEMMA.md`.  Those clusters do
not explain most of the observed support: the theorem's restricted-support
bounds are only `108,184,200,244,220` in the five rows above.  The remaining
mass is genuinely transverse.

The control experiment is sharp.  Unstretched Welch Costas arrays are
vector-Sidon but repeat Euclidean norms; their normalized transverse collision
count grows from roughly `0.33` at `k=6` to `5.41` at `k=40`.  Applying the
smallest tested integral shear/stretch that separates all squared norms drops
the ratio below `0.07`, and it trends toward zero in the tested range.  Thus
ordinary vector Sidonicity does not control transverse collisions, while the
quadratic norm condition has exactly the predicted experimental effect.

## 5. Decision

The support target survives its first adversarial optimization, so proof work
may continue.  The next claim is not (1.1) under a new name.  It is the
strictly stronger, falsifiable wide-case sufficient condition

\[
 E_{\mathrm{trans}}(A)\le k^{3+o(1)},            \tag{5.1}
\]

combined with Elekes's prior-art trapezoid bound for the parallel part.  Its
kill condition is a distance-Sidon family with subpolynomial maximum line
occupancy and `E_trans>=k^{3+epsilon}`.  No such family is currently known.
