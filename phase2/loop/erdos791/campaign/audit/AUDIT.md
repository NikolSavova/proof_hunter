# Adversarial audit of the Erdős #791 campaign

Date: 2026-08-13

## Verdict

The block-family coverage theorem and universal `85/294` ratio bound are
correct; Kohonen's `(h,b,n,r)=(5,6,17,2)` is the unique equality case in this
family.  The reflected-diagonal fourth-tile lemma is also correct for even
`t` and gives a genuinely larger sufficient certificate language, though no
quantitative improvement was found.

One negative result in `theory/THEORY_NOTES.md` is not established: the
`(ell,m)=(20,116)` radius-three CP-SAT model uses a symmetry condition in an
orientation inconsistent with the seed used by its radius constraint.  The
separate proof-producing `(42,511)` SAT lane normalizes its seed correctly;
all three of its DRAT traces verified.

**Post-audit disposition.**  The invalid theory artifact remains retracted.
After this audit, `sat/generate_cnf.py` was instantiated with a consistently
swapped `(20,115)` seed.  Its positive radius-zero control recovered the seed,
and target `m=116` at replacement radii 1, 2, 3, and 4 was UNSAT; every DRAT
trace was accepted independently by `drat-trim`.  Thus the corrected SAT lane
re-establishes and strengthens the local conclusion without rehabilitating the
flawed model.  Exact hashes and checker statistics are in `sat/RESULTS.json`.

## Ranked issues

### P1: the small-family radius-three exclusion is overconstrained

`theory/sat_lean.py` imposes `J[0]=1`, while
`family_placement(3,4,7,1)` has `0` in `K` and not in `J`.  Its radius is then
computed against this unswapped seed.  Although `J` and `K` are globally
interchangeable when their counts agree, swapping a candidate does not
preserve distance to a fixed unswapped seed.  Thus the model only excludes
radius-three candidates which additionally contain `0` in `J`, not the full
radius-three ball claimed.

A decisive sanity check is that the known valid `(20,115)` family seed is
reported `INFEASIBLE` by the same model at radius zero:

```text
sat_lean.py --m 115 --counts 6 7 7 --h 3 --n 7 --r 1 --radius 0
status: INFEASIBLE
```

Fix this with `J[0] OR K[0]`, or swap the seed's `J,K` labels before adding
both hints and radius constraints, then regenerate the result.  This flaw does
not affect `sat/generate_cnf.py`, which explicitly normalizes the `(42,511)`
seed first.

### P2: the bounded-coin proof omits its key coefficient argument

The lemma is true, but “canonical representation + reflection” does not by
itself bound both coefficients in one representation.  A repair is short.
Choose `x=hi+(h+1)j` with `0<=i<=h`.  If `j<n`, it is already in the box.
Otherwise choose the least `k` with `j-hk<=n-1`.  Then
`j-hk>=n-h>=0`; if `i+(h+1)k>=b`, the represented value is at least
`hb+(h+1)(n-h)`, one beyond the asserted upper endpoint in the worst case.
This contradiction bounds the shifted representation.  The theorem survives,
but the proof should include this step.

### P2: the mixed-radix density argument needs disjointness

Section 3 says the composition uses “at most `ell*s`” segments, then claims
the density is multiplied by exactly `(R+1)/s^2`.  That denominator bound alone
has the wrong direction for the no-go.  Normalize all useful macro coordinates
to `[0,m-1]`; translates by distinct multiples of `m` are then disjoint within
each type, the macro count is exactly `ell*s`, and the intended Kohonen
argument goes through.  Without this hypothesis, translated sets may collide.

### P3: fourth-tile novelty has not been literature-audited

The reflected segment and phase lemma are mathematically genuine and useful,
but this audit did not run a prior-art search for that exact four-direction
construction.  Call it new to this campaign unless a literature search
supports a stronger claim.

## Independently verified

- 38,990 bounded-coin parameter triples: no counterexample.
- 186,600 block-family tuples: every claimed `m` was the exact tile prefix;
  every ratio was at most `85/294`; equality occurred only at
  `(5,6,17,2,42,510)`.
- Independent formula sweep through `ell<=201`: the same unique equality.
- `template_exhaust.cpp` replay: byte-identical output, all 9,453,780 layouts,
  final `NO_TARGET`.
- Parameter reduction and rational optimization: algebra, exceptional ranges,
  stationary point, integer checks, and equality uniqueness all correct.
- Fourth-tile identities through `t=100`, naive hole formula through `t=500`,
  and 12,994 randomly certified macro squares checked by literal expansion for
  even `t<=20`: no false certificate.
- Fourth-tile CP-SAT encoding reviewed as exact.  Its all-split ledgers report
  210/210 and 330/330 `INFEASIBLE` at `(7,15)` and `(8,19)`; these are
  rerunnable OR-Tools conclusions, not portable proof certificates.
- Corrected `(42,511)` radius-1, radius-2, and radius-3 DIMACS/DRAT pairs all
  returned `s VERIFIED` under `drat-trim`.  Radius 3 used 108,746,580
  resolution steps, matching `sat/RESULTS.json`.

Executable checks are in `audit/independent_audit.py`; the template replay and
DRAT checker transcripts are in this directory.
