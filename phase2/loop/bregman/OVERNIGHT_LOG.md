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

### Wave 3 — the BREAK lane failed to break it: **SURVIVES**. Maths lane hit a server error, relaunched.

`referee2_ref_break_20260813.md`. Tasked not with critique but with actually CONSTRUCTING a
counterexample. It tried three distinct routes and all three failed:

1. **Discontinuity attack.** It DID find a real flaw — but in my informal summary, not in the
   proofs. It constructed an explicit Legendre `g`, finite at a boundary point `q` yet
   **discontinuous** there (`g(q) = 0` while the relevant hull height is `k(q) = 1`). So
   "finite height ⟹ `f*` continuous at `q`" is **FALSE**, and my wave-2 log entry and my own
   audit both used that phrasing. **Correction of record:** the ghost relation must be stated
   via `k = cl(f* + iota_S)` with a recovery sequence satisfying `f*(s_j) -> k(q)`, not via
   continuity of `f*`. The break lane confirms **the full wave-2 proofs already do this**; only
   the informal restatement (mine, and the brief I wrote) was loose.
2. **Does discontinuity save a counterexample?** No. It prevents convergence to `f*(q)` but not
   to the lower-hull value `k(q)`, and the perturbation argument runs on `k(q)`. Its own
   candidate has an EMPTY argmin at every `x_0 + t(-1,0)`, `t > 0` — i.e. the attack reproduces
   the contradiction rather than escaping it.
3. **Infinite-height attack.** Also fails, for a clean reason: infinite height gives
   `k(q) = +infinity`, so such a `q` cannot be a minimising ghost at all; and if EVERY boundary
   accumulation has infinite height then `f* + iota_S` is lsc and the convexification argument
   forces `S` convex regardless. So attempt 1's finite-height restriction was not a gap.

Its own summary of where a counterexample would have to live: *"None under (a) and (c); one
would have to relax full tilt admissibility or attainment."*

**Status of the claim after wave 3:** one construct-agent failed to build a counterexample and
proved the impossibility instead; one prove-agent proved it; one dedicated break-agent attacked
three ways and failed. The maths lane is the remaining check — it server-errored
(`wfr_019ffa12a42f76ac96af5f8a5ed51c0b`) and has been relaunched with its journal entry cleared.

### Wave 3 complete — maths lane **MINOR_REPAIRS**. The question is settled; proving stops.

`referee2_ref_maths_20260813.md`. Its findings 5-7 are not repairs but CERTIFICATIONS of the
three most load-bearing steps:

- **5. The duality** (right projection over `C` <-> tilt minimisation over `S = C*`): *"Correct;
  argmin sets and their cardinalities are preserved."* This is what makes the contradiction bite.
- **6. The supporting normal**: *"Correct in finite dimensions; unboundedness and flat faces do
  not affect strictness for interior points."* — which also retires my flat-face worry entirely.
- **7. Perturbation admissibility and infinite height**: *"Correct once the ghost height is k(q)
  and recovery sequences are used."*

Four repairs demanded (R1-R4):
1. Drop the false "finite height => `f*` continuous at `q`" (referee's own Legendre counterexample
   `g(u,v) = u^2 - sqrt(u) + v^2/u`); benchmark against `k = cl_lsc(f* + iota_S)` with a recovery
   sequence. *(This was MY imprecision, propagated into both briefs — see wave 3 above.)*
2. State the tie at the HULL height: `k(q) - <x_0,q> = m_0`, since SOL.6 yields an epigraph ghost
   at height `k(q)` which may strictly EXCEED `f*(q)`.
3. The written theorems still assume `C` closed and nonempty, so the headline "under (a) and (c)
   alone" overstates. Either prove attainment forces those, or state hypotheses honestly.
4. `part2b`'s SOL.2 unit-slope bound gives coercivity, not supercoercivity; use an
   arbitrary-slope bound via a sphere of radius `R + L`.

**Scoreboard:** construct-agent failed and proved impossibility instead; prove-agent proved it;
break-agent attacked three ways and failed (SURVIVES); maths lane MINOR_REPAIRS with the three
dangerous steps certified. Under the standing stopping rules this counts as SETTLED, so no
further proving waves are being launched.

### Wave 4 — CONSOLIDATION, launched (`resp_06d50561...`). Not a proving run.

`scripts/consolidate.py` -> `proof_part2_consolidated_20260813.md`. Merges both wave-2 proofs,
applies R1-R4, and must be SELF-CONTAINED — carrying the duality and ghost reduction rather than
citing them (the `s3consol` lesson from the Bruhat campaign: a document that cites its evidence
gets rejected, one that carries it does not). It will still need its own referee lane afterwards.

*(Ops note: two launches tonight failed because the shell cwd had drifted into the bregman
directory and relative paths broke. Use absolute paths in every launch command.)*
