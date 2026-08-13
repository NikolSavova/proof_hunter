# Overnight run — Part II (hypothesis (b)) — 2026-08-13

*Sihao authorised ~6-7 hours of autonomous iteration and went to bed. This file is the
morning briefing: read it top-down, newest wave last. Everything is committed and pushed as
it happens, so nothing depends on this process surviving.*

## Standing decisions for the night (so no one has to guess my reasoning)

- **Target:** settle hypothesis (b) of Fact 3.2 — either (A) construct a counterexample, or
  (B) prove (b) removable. Attempt 1 reduced this to ONE object: the *finite-height ghost
  boundary face* of its Lemma SOL.6. If `C*` is nonconvex then for some `x` the lsc-hull tilt
  must have an extra minimiser on `bd U*`, tying with the genuine minimiser in `C*`.
- **Not load-bearing.** Part I — the actually-posed open problem, "is full domain necessary?"
  — is PROVED, audited, and cleared by two adversarial lanes. Everything tonight is bonus
  scope. If it all fails, the result stands as: a complete answer to the posed question plus
  honest partial progress on the neighbouring hypothesis.
- **Method:** waves of two adversarially opposed Sol agents at `effort=max` (construct vs
  exclude), each wave briefed with the previous wave's findings IN FULL. `max` is the API
  ceiling, so the lever is target sharpness and cross-pollination, not the dial.
- **Stopping rules.** Stop early and write up if: (i) either side settles it and survives a
  referee lane; (ii) three consecutive waves produce no new named structure (diminishing
  returns — record and stop); (iii) ~7 hours elapse. Do not spend past that without a human.
- **Spend:** Sol runs ~$1-5 each; a wave is 2 agents. Budgeting well under $100 for the night.
- **Honesty rule, inherited:** a clean partial result with a named gap beats a fabricated
  closure. Attempt 1's willingness to say "I do not have a proof" is exactly why tonight has
  a sharp target at all.

## Wave log

### Wave 2 — launched 2026-08-13 ~00:1x — RUNNING
- `part2a` (construct): told which four candidates attempt 1 killed; given the verified sphere
  arithmetic (for the full unit ball the interior minimiser always strictly beats the boundary,
  e.g. −10.0499 vs −10.0000 at |x| = 10, so a tie needs a constrained `S`); and pointed at a
  **flat-face kernel**, `f(x) = Σ_j √(1+x_j²)`, whose dual domain is the box `[-1,1]^n` — on a
  flat face the tilt is affine, so ties should be far easier than on the strictly convex sphere.
- `part2b` (exclude): four angles, sharpest flagged first — hypothesis (c) asserts a *singleton*
  hence **attainment for every x**, and a ghost face is precisely a mechanism for losing
  attainment; that tension may be the whole proof.
- ids: `scripts/prove2_ids.json`

*(subsequent waves appended below as they complete)*

### Wave 2 — COMPLETE. **Both agents independently concluded (B): hypothesis (b) IS removable.**

`proof_part2a_20260813.md` (19.5k) and `proof_part2b_20260813.md` (17.2k). Unrefereed.

**This is convergence, not an echo.** `part2a` was told to CONSTRUCT a counterexample; it
failed to and instead proved the impossibility, reaching the same key idea as `part2b`
independently. `part2b` was given "attainment under (c)" as a suggested angle, so its route
was partly primed; `part2a`'s was not.

**The shared missing observation.** The right perturbation direction is NOT `q - p_x`; it is an
**outward supporting normal `n` to `U*` at the ghost `q`**. Perturbing `x0 -> x0 + t n`:

```
for p in S:  phi_t(p) = phi_0(p) - t<n,p> >= m_0 - t<n,p> > m_0 - t<n,q> = phi_t(q)
```

(strict because `S subset U*` is open and `<n,p> < <n,q>` strictly at a supporting hyperplane).
So every point of `S` is strictly worse than the ghost value — yet `q` is a limit of points of
`S` and `f*` is continuous at `q` (finite height IS the ghost regime), so the infimum over `S`
EQUALS the ghost value and is **not attained**. `x0 + t n in U = X` by (a), so (c) demands a
singleton there. Contradiction. Hence no ghost face, hence by attempt 1's SOL.6(3), `S` convex.

**My independent audit: the inequality chain is valid**, step by step (see session transcript;
each of the six steps checked, including that interior points of an OPEN convex set lie
strictly inside a supporting hyperplane at a boundary point).

**`part2a` corrected one of MY briefing errors**, which is worth recording: I suggested the box
kernel `Σ√(1+x_j²)` because a flat face of `[-1,1]^n` would make the tilt affine tangentially
and ties easy. That is **wrong** — on the face `p_1 = 1` the remaining `-√(1-p_j²)` terms are
still strictly convex, so the tilt stays strictly convex tangentially; flatness only makes the
NORMAL functional constant on the face. My heuristic would have sent a prover down a dead end.

**Consequence if this survives refereeing:** the result is no longer "counterexample for (a),
partial progress on (b)". It becomes **Fact 3.2 strengthened — hypothesis (b) deleted outright,
hypothesis (a) shown necessary by explicit counterexample.** That is a materially better paper.

**Next: referee lanes.** Two agents agreeing is suggestive, not decisive — and this project has
been burned by confident drafts all week. Wave 3 = two adversarial lanes, one a maths referee
on the proof, one tasked specifically with CONSTRUCTING a configuration that evades the
argument (the fastest way to find a hole if one exists).
