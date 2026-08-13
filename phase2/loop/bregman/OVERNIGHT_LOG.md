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
