# PROBLEM — Bregman right-Chebyshev sets: is full domain necessary?

*Frozen statement, win condition, and kill criteria. Written 2026-08-13 BEFORE any proof
drafting, per the Tier-2 loop design (`HANDOFF.md` §3, 2026-07-09): PROBLEM.md and verify.py
come first; provers run against a frozen target. **Do not edit the statement below to match
what we manage to prove** — if the target changes, add a dated amendment section.*

**Source.** Bauschke, Macklem, Wang, *Chebyshev Sets, Klee Sets, and Chebyshev Centers with
respect to Bregman Distances: Recent Results and Open Problems*, [arXiv:1003.3127](https://arxiv.org/abs/1003.3127)
(2010), the open problem attached to its Fact 3.2. Corpus id
`arxiv-openproblem:1003.3127v1#2` — the pipeline's **first and only GREEN** across 96
finalists, and one of two STRONG survivors of the Tier-2 adversarial re-tag.

## Definitions (fixed)

`X = R^n`; `f: X -> ]-inf, +inf]` Legendre; `U = int dom f`; `U* = int dom f*`;
`D_f(x,y) = f(x) - f(y) - <grad f(y), x - y>`.

**Right** Bregman projection: `P^->_C(x) = argmin_{y in C} D_f(x, y)` (the SECOND argument
varies). `C` is **right D-Chebyshev** if `P^->_C(x)` is a singleton for every `x in U`.
`C* := grad f(C)`.

## The theorem under test

> **Fact 3.2.** If `dom f = X`, `C subset U` is closed nonempty with `cl C* subset U*`, and
> `C` is right D-Chebyshev, then `C*` is convex.

## The open problem (frozen)

**Is the hypothesis `dom f = X` necessary?** Either exhibit a Legendre `f` with
`dom f != X` and a closed nonempty `C subset U` that is right D-Chebyshev with `C*`
nonconvex; or prove the conclusion survives without full domain.

## Win condition (frozen — from the corpus DB, unedited)

An explicit Legendre `f` with `dom f != X` and explicit closed nonempty `C subset int dom f`
such that **(i)** `P^->_C(x)` is a singleton for every `x in int dom f`, and **(ii)**
`C* = grad f(C)` is nonconvex — with closed-form `f` and `C`, computations verifying the
singleton property (analytic proof or certified numerics), and an explicit nonconvexity
witness (two points of `C*` whose midpoint is not in `C*`). Alternatively a short formalizable
theorem removing the hypothesis.

## Candidate answer

**Provenance:** this construction was built by a Fable *skeptic* agent on 2026-07-09 during the
Tier-2 re-tag — an agent tasked with refuting the problem's tractability, which failed to refute
it and produced the counterexample instead. It supplied the reduced formula and the `h''` bound.
This session reconstructed the explicit curve `c(t)` from that formula and verified everything
numerically. **Neither step is a proof**; that is what the Part I run is for.

`f` = negative entropy on `R^2`: `f(x) = sum_j (x_j ln x_j - x_j)`, `dom f = R^2_+ != R^2`
— **full domain fails, which is the hypothesis under test**. Then `U = R^2_++`,
`grad f(x) = (ln x_1, ln x_2)`, `U* = R^2`, and `D_f` is the generalized KL divergence.

`C = {(e^t, e^{-t^2}) : t in [1,2]}` — compact, contained in `U`.

- `D(x, c(t)) = const(x) + e^t + e^{-t^2} - x_1 t + x_2 t^2 =: h_x(t)`.
- `h_x''(t) = e^t + (4t^2 - 2) e^{-t^2} + 2 x_2 > e + 2/e > 17/5 > 0` on `[1,2]` for every
  `x in R^2_++` (infimum at `t = 1`, `x_2 -> 0+`).
  ⚠️ **Erratum 2026-08-13** (maths referee, finding 1): this file previously claimed
  `>= 3.454041`, which is FALSE — `e + 2/e = 3.454040710802...`, so the stated bound was
  rounded the WRONG WAY and fails at `t = 1` as `x_2 -> 0+`. Use the exact form `e + 2/e`,
  or the safe decimal `> 3.45404`. Proof `proof_part1_20260813.md` (Lemma SOL.2) never made
  this error: it states `inf q = e + 2/e > 41/12 > 17/5`.
- Strict convexity on a compact interval ⇒ **unique** minimizer ⇒ `C` is right D-Chebyshev.
- `C* = {(t, -t^2) : t in [1,2]}`, a strictly concave arc ⇒ **nonconvex**.
- `cl C* = C* subset U* = R^2` holds, so **only** the full-domain hypothesis is dropped.

Nonconvexity witness: `(1,-1), (2,-4) in C*`; midpoint `(1.5, -2.5)`; the arc at `t = 1.5`
gives `(1.5, -2.25) != (1.5, -2.5)`.

## Kill criteria — abandon or rescope if ANY of these fires

0. ~~Luo et al. (2019) resolves it~~ — **CLEARED**, see above.
1. **The sweep comes back RED** (`scripts/sweep.py` → `sweep_20260813.md`): the problem is
   resolved in the literature. The construction is a small variation on the survey's own
   Example 3.3, so this is the live risk.
2. A published **characterization of right D-Chebyshev sets for the negative entropy** exists
   (that is the survey's Problem 4) — it would subsume this counterexample and destroy its
   novelty.
3. Fact 3.2 has been **superseded** by a theorem with weaker hypotheses.
4. The uniqueness argument fails at a boundary case we have not checked — e.g. minimizers
   escaping to an endpoint in a way that breaks singleton-ness, or `x` approaching `bd U`.
5. A referee lane finds the `U*` computation wrong (if `cl C* subset U*` failed, we would be
   dropping two hypotheses, not one, and the counterexample would not isolate full domain).

## Scope note — RESOLVED 2026-08-13

The Tier-2 skeptic flagged that Part I settles only the full-domain half, and that a
referee-proof note must also address the second hypothesis `cl C* subset U*`. **It now does,
and in the opposite direction to what was expected:** no second counterexample was needed
because hypothesis (b) turns out to be redundant outright (Part II). The paper's shape is
therefore a complete analysis of Fact 3.2's hypotheses — **(a) shown necessary by explicit
counterexample, (b) shown removable by theorem** — rather than a counterexample plus a gap.

## Status

- [x] Statement frozen; candidate verified independently (this file)
- [x] Prior-art sweep — **AMBER** (`sweep_20260813.md`): no published resolution found.
  Laude-Ochs-Cremers (JOTA 184, 2020) independently confirm Problem 2 was still open in 2019.
  **Two conditions carried forward:** (i) *Optimization* 68(8) 1599-1624, Luo-Meng-Wen-Yao,
  "Bregman distances without coercive condition: suns, Chebyshev sets and Klee sets" is
  paywalled and UNREAD — full domain of `f` corresponds by duality to supercoercivity of `f*`,
  so it aims near this target; **a hard gate on submission** — **CLEARED 2026-08-13**, see
  `luo2019_clearance_20260813.md`: their right-projection Theorem 3.12 carries `U = X`, which IS
  the full-domain hypothesis, so they relax 1-coercivity and not full domain. Their Theorem
  3.12(3) even applies to our example (its hypotheses `grad f(U) = U*`, `f*` strictly convex on
  `U*` both hold), and predicts that our nonconvex `C*` forces their condition (i) to fail —
  consistent, and it makes our example an illustration of their theorem rather than a
  contradiction of it. (ii) The novelty claim must be
  stated narrowly: NOT the first nonconvex right KL-Chebyshev set (the survey has those), NOT
  the first nonconvex entropy-Bregman example (Laude-Ochs-Cremers have a local one), but an
  explicit **globally** right D_f-Chebyshev set with nonconvex gradient image, showing (a) is
  not removable even when (b) holds.
- [x] `verify.py` numeric harness written before any prover runs; strengthened per referee
- [x] Part I **proof** — `proof_part1_20260813.md`, rigorous, no numerics load-bearing
  (Lemma SOL.2 proves `inf q = e + 2/e > 41/12 > 17/5` from exponential series with explicit
  rational constants; independently audited step by step this session)
 - [x] **Part II — mathematically SETTLED (hypothesis (b) is redundant), but ⚠️ NOT NOVEL.**
  Prior-art sweep #2 + a focused adjudication with Luo et al.'s theorem statements attached
  conclude our theorem is a **short corollary of Luo–Meng–Wen–Yao (2019)**, via the chain
  `Chebyshev => closed => boundedly compact (free in R^n) => (Thm 3.13) sun => (Thm 3.12(2),(3))
  grad f(C) convex`, with 3.12(3)'s and 3.13's extra hypotheses all automatic for a Legendre `f`
  with `dom f = X` in finite dimensions. **Do not claim Part II as a new theorem.** Details:
  `sweep2_theorem_20260813.md`, `adjudication_luo_20260813.md`. Original claim retained below
  for the record: `proof_part2_consolidated_20260813.md` Theorem 1: for Legendre `f` with
  `dom f = X` and **arbitrary** `C subset X`, a singleton right projection at every `x` forces
  `C` nonempty and closed AND `C*` convex. So Fact 3.2 holds with (b) deleted, and with
  closedness/nonemptiness derived rather than assumed. Route: dualise to tilt minimisation over
  `S = C*`; a nonconvex `S` yields a hull ghost on `bd U*`; perturbing along an outward
  supporting normal empties the argmin, contradicting attainment under (c).
  Provenance: attempt 1 isolated the obstruction; two independent agents (one told to CONSTRUCT
  a counterexample) converged on the proof; a dedicated break-agent failed on three routes;
  consolidated with four referee repairs.
- [x] **Two adversarial referee lanes on Part I — BOTH MINOR_REPAIRS, all findings applied**
  (`referee_maths_part1_20260813.md`, `referee_numerics_part1_20260813.md`). Neither found an
  error in the PROOF; all seven findings were against the supporting artifacts:
  a rounding-direction error in this file (`>= 3.454041` was false, since `e + 2/e =
  3.454040710802`), a mislabelled interval enclosure, an over-claimed uniqueness block, three
  weak harness blocks, and one unsourced "verified to 30 digits" claim. All fixed.
  **Part I therefore clears the house bar.**
- [x] **Part I VERIFICATION GATE, 2026-08-13** — three fresh Sol lanes at effort=max
  (`scripts/verify_part1.py`), on top of the two lanes of 2026-08-12. This is the gate the Luo
  clearance memo asked for and the gate the Part II post-mortem demands: the same reader wrote
  both clearances, so Part I's novelty was re-derived from the paper text by a reader briefed on
  exactly how the Part II clearance failed.
  - `verify1_v1_maths_20260813.md` — **SURVIVES**, no defects. Re-derived every rational
    certificate in Lemma SOL.2 and confirmed each series truncation is used in the correct
    direction. Names Lemma SOL.2 as the most fragile step (uniqueness rests on positivity of `q`
    as `x_2 -> 0+`). Useful aside: supercoercivity of `f*` is equivalent to `dom f = X` for
    closed convex `f`, so it cannot be read in as a standing assumption without making the
    problem vacuous.
  - `verify1_v2_sun_20260813.md` — **CONFIRMED**, sharper claim stands, with two proof-writing
    repairs (total convexity should be claimed on `U` only, not on `dom f`; the locally uniform
    modulus needs JOINT compactness in `(u,v)`, not a bound for each fixed `u`) and two scope
    repairs (say "cannot be deleted without replacement", not "necessary"; the prior-art
    conclusion is text-internal to the attachment). Both scope repairs applied in the paper.
  - **THE FRAGILE STEP IS NOW GONE.** Verifying Part I showed Lemma SOL.2 is unnecessary: on
    `[1,2]`, `4t^2 - 2 >= 2 > 0`, so BOTH terms of `q(t) = e^t + (4t^2-2)e^{-t^2}` are positive
    and `h_x'' > 0` is immediate. The three-interval monotonicity argument, the truncated
    exponential series, and the rational certificates — the entire apparatus where the
    2026-08-13 rounding error lived — are all deleted from the paper. The sharp constant
    `e + 2/e` survives only as a remark. The construction also generalises for free: it works
    for `C = {(e^t, e^{-t^2}) : t in [a,b]}` for ANY `1/sqrt(2) <= a < b`.
  - **The Luo corollary is now self-contained**, which is a bigger change than it sounds. Lane
    v2 supplied a DIRECT proof that `C` is a right `D_f`-sun: `h_w'(t)` is affine in `w` and
    vanishes at `t = s` when `w = c(s)`, so `h'_{z_lambda}(s) = lambda * h_x'(s)` and the
    endpoint trichotomy closes it in three lines. It also supplied an EXPLICIT witness that
    Luo's condition (i) fails, with the closed form `<grad f(y) - grad f(c(t)), y - x> =
    (s-t)^2 (e^{-s^2} - x_2) > 0`. So the corollary no longer depends on Theorem 3.13, on
    Theorem 3.12(3), or on any total-convexity verification — only on the STATEMENT of Theorem
    3.12(2), which is what it contradicts. Verified locally: `sun_check.py`.
  - `verify1_v3_novelty_20260813.md` — **AMBER, no kill.** No published source has the decisive
    combination (globally right-Chebyshev, `cl C* subset U*` retained, `C*` NONCONVEX), and no
    solution of Problem 4 exists. But it found a **mandatory citation the draft was missing
    entirely**: Bauschke–Wang–Ye–Yuan, *Bregman distances and Chebyshev sets*, J. Approx. Theory
    159 (2009) 3–25, **Example 7.5** — reproduced as the survey's Example 3.3. That is the
    closest prior art and it uses the SAME duality template: dual set `A = {(lambda, 2lambda)}`,
    a convex segment, giving a nonconvex right-Chebyshev `C = exp(A)` for negative entropy whose
    gradient image `C* = A` is CONVEX. So the broad claim "first nonconvex right-Chebyshev set
    for entropy" is false and already published; the narrow claim survives. Our change is to
    swap the convex segment for a nonconvex parabolic arc while keeping global Chebyshevness.
    A comparison table is now in the paper's introduction, and the priority language is
    "we are not aware of an earlier example with this combination".
    Also flagged: by duality the example shows a supercoercivity hypothesis cannot be deleted
    from the corresponding left-projection statement (`dom f = X` is dual to supercoercivity of
    `f*`). Recorded in the paper without naming the survey's Fact 3.1, which we have not read.
  - **Luo et al. re-checked directly, 2026-08-13.** The lane called the paywalled full text its
    highest-risk unchecked source. We have the PDF and searched the extraction: ZERO occurrences
    of *nonconvex*, *entropy*, or *exponential*; the only examples (3.15, 3.16) are `l^p`/Banach
    constructions; no remark claims `U = X` is essential. Remark 3.1 is about strict convexity in
    the LEFT case and does not touch our corollary. The residual is to read the TYPESET Theorems
    3.12/3.13 rather than the `pdftotext` rendering.
- [x] **Write-up** — `paper/main.tex` (8pp, compiles clean, 0 unresolved refs) plus
  `paper/DECISIONS.md` (14 human decisions, 4 blocking). Structure: Theorem 3.1 is the
  counterexample, Corollary 4.4 is the Luo consequence, Proposition 5.1 records hypothesis (b)
  as removable WITH ATTRIBUTION to Luo et al., and Section 6 states what remains open.
- [ ] Lean statement stub
