# Erdős 838 lower-bound campaign — round 1 synthesis

*2026-08-13. Seven Sol lanes at effort=max, all returned. Runner `scripts/campaign_lower.py`;
raw outputs `campaign_lower_<lane>_20260813.md`.*

## Headline: the campaign target was wrong, and two lanes caught it independently

I briefed every lane that proving

> `log C(P) + log U(P) ≥ (1/2 − o(1))(log N)²`  for arbitrary order types

would resolve the problem. **It would not.** The conversion I asserted loses a factor of two:

`C ≤ N·X ≤ N²M` and `U ≤ N²M`, so `log C + log U ≤ 4 log N + 2 log M`. A product bound of
`(1/2)(log N)²` therefore yields only `log M ≥ (1/4)(log N)² − O(log N)`, and `W ≥ M` gives
**exactly the already-published coefficient 1/4**. I have re-derived this by hand; the lanes are
right and the brief was wrong.

- `break_lemma` states it directly and adds a clean algebraic witness: if cap mass `H` sits at one
  endpoint pair and cup mass `H` at another, with the opposite statistic equal to 1, then
  `CU ≍ H²` while `Σ_e c_e u_e ≍ H`. Algebraic only — no claim of geometric realizability — but it
  kills the inequality route regardless.
- `verify51` reaches the same conclusion from the other side: *"A universal cap–cup product bound
  would provide the local radial mass, but not the crossing compatibility needed to convert that
  mass into W with no factor-of-two loss."* That is exactly why Theorem 5.1 needs the multiscale
  machine: many caps and many cups is not enough, they must **share endpoints**.

**Corrected target.** The quantity to bound is the endpoint-localized product

> `max_{p<q} c(p,q)·u(p,q) ≥ 2^{(1/2 − o(1))(log N)²}`.

(`check_candidate.py` already reports this separately — the diagnostic was right while the stated
goal was wrong.)

## The bigger finding: the standard method class is now provably exhausted at 1/4

`attack_direct` did not prove the lemma, and instead produced a **barrier**. For
`2 ≤ a,b ≤ t ≤ N` with `C(a+b−4, a−2) < t`, every `t`-subset contains an `a`-cap or a `b`-cup, so
double-counting incidences gives

```
1 ≤ C_a(P)·C(t,a)/C(N,a) + U_b(P)·C(t,b)/C(N,b)
```

and the lane shows the optimal consequence of **all** such asymmetric cup–cap double counts is

> `(c+u)·H( c/(c+u) ) ≥ 1/4`,  where `c = lim log C/(log N)²`, `u = lim log U/(log N)²`, `H` binary entropy.

At `c = u` this gives `c + u ≥ 1/4`. So the entire black-box double-counting route — the method
that produces the published bound — **cannot exceed 1/4 even for the product**, let alone for the
endpoint-localized quantity. Escaping it "requires extension/overlap information not contained in
those inequalities."

That is a genuine, if negative, result: it maps the barrier precisely.

## Two of the three reasons to believe 1/2 is the answer have weakened

1. **Székely was never evidence.** `attack_szekely`: his normalized *lower* coefficient is ≈ 0.1577,
   not 1/2. Our `prior_art_20260812.md` had converted his **random-graph upper** coefficient — the
   analogue of our upper bound, not a matching lower bound. I treated the numerical agreement as a
   signal that 1/2 is structural. It is not one. Verdict OBSTRUCTED; the graph multiplicity step
   uses induced-neighbourhood closure, while cap/cup continuation is an ordered-pair-state weighted
   recursion.
2. **The tree bridge is closed.** `attack_tree`: the canonical module tree stops at arbitrarily
   large *indecomposable* nodes, so there is no reduction of general order types to the
   decomposable class. Verdict OBSTRUCTED.
3. **Still standing:** Theorem 5.1 (1/2 sharp on the decomposable class), modulo the audit, and
   Proposition 4.4 (1/2 optimal for fixed-template iteration).

## The premise survived its first attack

`break_target` failed to construct anything beating coefficient 1/2, and proved a partial converse:
every level-dependent *uniform* directional blow-up with `max_i log|S_i| = o(log N)` satisfies
`log v(P) ≥ (1/2 − o(1))(log N)²`. It also derived the exact identities for **non-uniform**
blow-ups and localized where any improvement must come from — "macroscopic nondecomposable
templates with persistent left–right cap/cup anti-correlation."

So `1/2` remains the best candidate for the upper truth, now for a better reason than before.

## Prior art: AMBER, no prior solution

`priorart`: must cite Holmsen–Nassajian Mojarrad–Pach–Tardos's fixed-size double-counting theorem,
plus Bárány–Valtr and the ordered monotone-path literature. **None gives the target lemma or
improves the 1/4 universal lower coefficient.** Its summary is the useful line: *"fixed-size convex
-set multiplicity and monotone-path threshold theory exist; all-sizes cap–cup product multiplicity
apparently does not."*

## Independent verification of a lane

`break_lemma` supplied an exact dyadic Horton family `p_i = (i, y_i)`, `y_{2j} = ε_m y_j`,
`y_{2j+1} = 1 + ε_m y_j`, `ε_m = 2^{−m−4}`, and claimed cap–cup product coefficient ≥ 1. Checked
with `check_candidate.py` in exact arithmetic:

| m | N | (log C + log U)/(log N)² | log W/(log N)² | log max c·u /(log N)² |
|---|---|---|---|---|
| 2 | 4 | 1.792 | 0.977 | 0.500 |
| 3 | 8 | 1.376 | 0.827 | 0.516 |
| 4 | 16 | 1.197 | 0.779 | 0.573 |
| 5 | 32 | 1.113 | 0.767 | 0.624 |
| 6 | 64 | 1.073 | 0.654 → see note | 0.654 |

The product ratio converges to 1 from above exactly as claimed. Horton is far from extremal, which
is consistent — `f(N)` is a minimum and our blow-up construction achieves 0.5 where Horton sits
near 0.77.

## Honest status

Round 1 closed the two routes I was most optimistic about, removed one of my three reasons to
believe the target value, and proved that the standard method cannot reach it. The campaign is not
refuted — nothing showed `1/2` is the wrong answer, and the premise survived a real attack — but
**it is materially harder than I represented when recommending it.**

What a proof must now do, stated as sharply as the round allows:

1. Bound the **endpoint-localized** product, not the global one.
2. Use **extension/overlap** structure, since `attack_direct` proves size-by-size double counting is
   capped at 1/4.
3. Handle **indecomposable** order types directly, since no canonical decomposition reduces them.

That is a much more specific programme than we started with, and every item is a consequence of a
lane doing its job. It is also a fair description of why the problem has been open since 1978.
