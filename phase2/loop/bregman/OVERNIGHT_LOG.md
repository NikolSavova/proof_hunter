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

### Wave 4 COMPLETE — consolidated proof landed (30.4k chars), stronger than expected.

`proof_part2_consolidated_20260813.md`. **Theorem 1** now reads:

> Let `f` be Legendre on `X = R^n` with `dom f = X`. Let `C subset X` be **arbitrary**. If
> `argmin_{y in C} D_f(x,y)` is a singleton for every `x in X`, then (1) `C` is automatically
> nonempty and closed, and (2) `C* = grad f(C)` is convex.

That is stronger than the target: repair R3 was satisfied not by restating hypotheses but by
PROVING (its Lemma 4) that attainment forces nonemptiness and closedness — so `C` is now
arbitrary, and Fact 3.2's hypothesis (b) is gone entirely rather than weakened.

Its §14 repair audit marks R1-R4 all satisfied; §10 gives an example showing exactly why the
hull height `k(q)` is indispensable (and notes it is NOT a counterexample to Theorem 1); §11
reconciles the two source proofs; §15 identifies **no residual mathematical gap** for the stated
finite-dimensional theorem, while listing what is outside scope: infinite dimensions,
`dom f != X`, projections attained only on a proper subset of `U`, and LEFT projections.

**I verified the referee's discontinuity example locally**: `g(u,v) = u^2 - sqrt(u) + v^2/u`
approaches `0` along `v = cu` but `1` along `v = sqrt(u)` — finite yet discontinuous at the
boundary point, confirming R1/R2 were genuinely necessary and not pedantry.

### Wave 5 — final lanes on the CONSOLIDATED document, launched.

`scripts/referee3.py` -> `referee3_ref_maths_*.md`, `referee3_ref_break_*.md`. Retargeted at the
merged proof, with the new surfaces named: Lemma 4 (does attainment really force closedness for
ARBITRARY `C`?), Lemma 6 (arbitrary-slope supercoercivity), §10, and whether the §11
reconciliation is honest or quietly dropped a step in the merge.

### Wave 5 COMPLETE — **BOTH LANES: SURVIVES.** Part II is closed.

`referee3_ref_maths_20260813.md` / `referee3_ref_break_20260813.md`. SURVIVES is the top of the
scale — no repairs demanded. Both engaged substantively rather than rubber-stamping:

- **Maths lane** re-derived the duality from Fenchel equality itself (`g(p) = <p,y> - f(y)`,
  giving `D_f(x,y) = f(x) + g(p) - <x,p>`) and concluded: *"The continuity-based version of the
  key step is false, but the consolidated proof has genuinely repaired it. I do not find a
  counterexample to Theorem 1 or a fatal gap in the ghost reduction."*
- **Break lane**: *"I could not construct the requested counterexample. The strongest
  boundary-discontinuity candidate satisfies full domain, closedness, nonemptiness, and
  nonconvexity of `C*`, but it necessarily fails projection existence. The consolidated proof's
  replacement of boundary continuity by the hull recovery sequence closes the proposed escape
  route."* It pushed the §10 function as hard as it could and it still died on attainment.

**Cumulative adversarial record on Part II:** 1 construct-agent (failed, proved impossibility
instead) + 1 prove-agent (proved it) + 1 break-agent v1 (SURVIVES) + 1 maths lane v1
(MINOR_REPAIRS, three load-bearing steps certified) + consolidation with all repairs + 1 maths
lane v2 (SURVIVES) + 1 break-agent v2 (SURVIVES). **No agent has found an error in the
mathematics at any stage.** Every defect found all night was in a restatement, and several of
those were mine.

### Wave 6 — prior-art sweep on the NEW THEOREM, launched.

`scripts/sweep2.py` -> `sweep2_theorem_20260813.md`. Sweep #1 cleared the Part I
COUNTEREXAMPLE; Part II is a DIFFERENT and stronger claim — it strengthens a published Fact —
so the Erdosgate rule applies to it independently. It is told to check specifically: anyone
stating Fact 3.2 without (b) or calling (b) redundant; later work by the original authors;
whether Luo et al. or its citers remove the DUAL-CLOSURE hypothesis (a different question from
the one we cleared them on); Themelis-Wang's domain-aware framework; whether "attainment forces
closedness" is folklore needing citation rather than claiming; and whether
perturbation-along-a-supporting-normal is a known named device.

## ⚠️ WAVE 6 — PRIOR-ART SWEEP #2 RETURNS **RED**. READ THIS BEFORE ANYTHING ELSE.

`sweep2_theorem_20260813.md`. The sweep names **Luo–Meng–Wen–Yao, Optimization 68(8) (2019),
Theorem 3.12** — the very paper I "cleared" earlier tonight — as already containing the
substantive content of our Part II theorem, because **Theorem 3.12 imposes no dual-closure
hypothesis**. It also finds that "attainment forces closedness" is essentially
**Bauschke–Wang–Ye–Yuan (JAT 2009) Lemma 7.2** in the left orientation, so that half is not new
either.

**The sweep is right about the important thing and I was wrong about it.** My clearance memo
concluded Luo et al. "relax 1-coercivity, not full domain" and stopped there. True — but it is
the wrong axis. Our Part II removes the *dual-closure* hypothesis (b), and **Theorem 3.12 never
assumed (b) in the first place.** I checked the wrong hypothesis.

**However, the sweep's kill is overstated, and the difference decides whether anything survives.**
I have re-read Theorem 3.12 in the PDF. Its hypothesis is that `C` is `->D_f`-**PROXIMINAL**
(nonempty argmin), and its four equivalent statements are:

  (i) the variational characterisation (34);  (ii) `C` is a `->D_f`-sun;
  (iii) the `z_2` condition;                  (iv) `grad f(C)` is convex.

**"Chebyshev" is NOT among (i)–(iv), and is not the hypothesis.** So Theorem 3.12 does not, as
written, give `singleton right projections => grad f(C) convex`. The missing link —
Chebyshev implies one of (i)–(iii) — is supplied by Luo's **Theorem 3.13**, which requires `C`
**boundedly compact**, plus `f` totally convex on `U` and `f*` locally uniformly totally convex
on `U*`.

**So the residual question, which is THE question for the morning:**

> Luo's chain yields "right-Chebyshev => `grad f(C)` convex" for **boundedly compact** `C` under
> extra total-convexity hypotheses. Our Part II yields it for **arbitrary** `C` assuming only
> Legendre + `dom f = X`. Is that delta (a) real and worth stating, (b) an easy exercise given
> their machinery, or (c) already known elsewhere?

I am **not** resolving this autonomously. It is precisely the kind of hypothesis-matching
judgement that has burned this project all week, and it needs a human who can read both papers.

**Status I am recording, and will not overstate in either direction:**
- Part II's mathematics is proved and has survived four adversarial passes. Nothing is retracted.
- Its **novelty is now in serious doubt** and must be treated as unresolved.
- **Part I is unaffected.** The counterexample answers the survey's posed question about full
  domain; Luo et al. retain `U = X` throughout and do not touch it. Sweep #1 cleared it, and this
  sweep re-confirms Luo "later remove the dual-closure condition while retaining full domain".

**Lesson recorded:** I ran the novelty sweep on the counterexample in the morning and only ran
one on the THEOREM after proving it. Had wave 6 run before waves 2–5, the night would have been
aimed differently. **Sweep every claim, not every project — and re-sweep when the claim changes.**

## ADJUDICATION — Part II is TRUE but NOT NOVEL. Final answer, and the night's honest end.

`adjudication_luo_20260813.md` (actual Luo theorem statements attached, not paraphrases).

**My technical objection was correct on the letter and wrong on the substance.** The adjudicator
confirms Chebyshev is genuinely *not* among Theorem 3.12's conditions (i)–(iv), and that the
sweep's attribution "to Theorem 3.12 alone" is **inaccurate**. But it then closes the gap I
thought was open:

- **Theorem 3.13's bounded-compactness hypothesis is free in our setting.** Chebyshevness forces
  `C` closed (the same `D_f(c̄, c_k) -> 0` argument our own proof uses for R3), and in `R^n`
  every closed set is boundedly compact. So the hypothesis I thought was a real restriction
  costs nothing.
- **3.12(3)'s hypotheses are automatic** for Legendre `f`: Rockafellar Thm 26.5 gives
  `grad f: U -> U*` bijective with `f*` Legendre, hence `grad f(U) = U*` and `f*` Gâteaux
  differentiable and strictly convex on `U*`.
- **3.13's total-convexity hypotheses are automatic in `R^n`** by compactness of spheres plus
  strict convexity (though NOT in general Banach spaces).

So the chain is:
`C right Chebyshev => C closed => boundedly compact => (3.13) sun => (3.12(2), U=X) (i) => (3.12(3)) grad f(C) convex.`

**Verdict: our Part II theorem is not strictly stronger than Luo et al.; it is a short corollary
of their machinery.** The sweep's headline was right even though its route was wrong.

### What this means, stated without spin

- **Part II is TRUE, four-times adversarially verified, and NOT PUBLISHABLE as new.** It should
  be cited to Luo et al. (2019), not claimed. Our proof is an independent derivation by a
  different route (ghost/supporting-normal rather than sun-theoretic) — that is a nice sanity
  check on both, and nothing more.
- **Part I is UNAFFECTED and remains the result.** Luo et al. retain `U = X` throughout; the
  survey's posed question — is full domain necessary? — is answered by our counterexample, which
  is proved, independently audited, and cleared by two adversarial lanes. Sweep #1 cleared it and
  sweep #2 re-confirms Luo "remove the dual-closure condition while retaining full domain".
- The paper is therefore back to its pre-midnight shape: **a short note settling hypothesis (a),
  which now must cite Luo et al. prominently and note that (b) was already known to be
  removable.** That framing is stronger than the original plan, which would have presented (b)
  as an open second half.

### Cost of the night, and what it bought

~8 Sol runs at max effort. It bought: a fully proved and quadruply-refereed Part II (worthless
for novelty, valuable as certainty that the surrounding statement is not where the paper is
wrong), a corrected understanding of what Luo et al. actually contains, and the discovery —
BEFORE submission — that a claim we would otherwise have made was already published. That last
item alone justifies the night; it is exactly the Erdősgate failure mode, caught in time.

### The lesson, for the record

I swept the counterexample in the morning, then spent the night proving a *different* claim and
only swept it afterwards. **Sweep every claim, and re-sweep the moment the claim changes.** My
first Luo clearance also asked the wrong question — "did they remove full domain?" — when what
mattered was "did they remove the hypothesis WE are removing?". Read prior art against the claim
you are actually going to make.

**Nothing is running. No further agents launched.**
