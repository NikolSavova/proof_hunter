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
- `h_x''(t) = e^t + (4t^2 - 2) e^{-t^2} + 2 x_2 >= 3.454041 > 0` on `[1,2]` for every
  `x in R^2_++` (minimum at `t = 1`, verified to 30 digits this session).
- Strict convexity on a compact interval ⇒ **unique** minimizer ⇒ `C` is right D-Chebyshev.
- `C* = {(t, -t^2) : t in [1,2]}`, a strictly concave arc ⇒ **nonconvex**.
- `cl C* = C* subset U* = R^2` holds, so **only** the full-domain hypothesis is dropped.

Nonconvexity witness: `(1,-1), (2,-4) in C*`; midpoint `(1.5, -2.5)`; the arc at `t = 1.5`
gives `(1.5, -2.25) != (1.5, -2.5)`.

## Kill criteria — abandon or rescope if ANY of these fires

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

## Scope note — what a COMPLETE note needs

The Tier-2 skeptic flagged that this settles only the full-domain half. Fact 3.2 carries a
second hypothesis, `cl C* subset U*`. A referee-proof note should also address whether THAT
is necessary — requiring a second construction where `cl C*` escapes `U*` (compactness is
lost, so the uniqueness argument must be redone). Treat as **Part II**, not optional polish.

## Status

- [x] Statement frozen; candidate verified independently (this file)
- [x] Prior-art sweep — **AMBER** (`sweep_20260813.md`): no published resolution found.
  Laude-Ochs-Cremers (JOTA 184, 2020) independently confirm Problem 2 was still open in 2019.
  **Two conditions carried forward:** (i) *Optimization* 68(8) 1599-1624, Luo-Meng-Wen-Yao,
  "Bregman distances without coercive condition: suns, Chebyshev sets and Klee sets" is
  paywalled and UNREAD — full domain of `f` corresponds by duality to supercoercivity of `f*`,
  so it aims near this target; **a hard gate on submission**. (ii) The novelty claim must be
  stated narrowly: NOT the first nonconvex right KL-Chebyshev set (the survey has those), NOT
  the first nonconvex entropy-Bregman example (Laude-Ochs-Cremers have a local one), but an
  explicit **globally** right D_f-Chebyshev set with nonconvex gradient image, showing (a) is
  not removable even when (b) holds.
- [ ] `verify.py` numeric harness written before any prover runs
- [ ] Part I **proof** (rigorous, no numerics load-bearing) — Sol running
- [ ] Part II — is `cl C* subset U*` necessary? — Sol running
- [ ] Two adversarial referee lanes
- [ ] Lean statement stub
