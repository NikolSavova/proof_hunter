# Erdős #791 — finite generalized-Mrose placement prototype

This directory independently reproduces the finite certificate in Jukka
Kohonen, *An improved lower bound for finite additive 2-bases*,
[arXiv:1606.04770v2](https://arxiv.org/abs/1606.04770), Theorem 1, and makes a
bounded cheap search for a strict improvement.

## Exact finite rule being checked

For placement sets `I,J,K`, write `IJ=I+J`, `IK=I+K`, and `JK=J+K`.  In
Kohonen's square/parallelogram abstraction, square `q` is certified precisely
when

```text
q in IJ  OR  q in IK  OR  (q-1 in JK AND q in JK).
```

The last offset matters: parallelograms at consecutive positions `q-1,q`
cover square `q`.  Thus the certified set is exactly

```text
(I+J) union (I+K) union {q : {q-1,q} is a subset of J+K}.
```

Here “exactly” describes the finite **tile-certificate language**.  It is a
sufficient condition for coverage in the literal integer sumset `A_t+A_t`,
not a necessary characterization of every integer that might also be covered
accidentally by same-type sums or partial tile overlaps.  `verifier.py`
therefore performs both checks: the exact abstract rule, plus literal expanded
sumset checks at several `t` values.

Kohonen's lists have sizes `(8,17,17)`, hence `ell=42`.  The verifier obtains
the exact tile prefix `[0,509]`, so `m=510` and

```text
m/ell^2 = 510/42^2 = 85/294.
```

For all `t>=2`, the tile lemmas then give a generalized Mrose basis of size at
most `42(t+1)` and range at least `510t^2-1` (Kohonen sharpens the size count to
`42t+7`).

## Reproduce

```bash
python3 -m unittest -v test_verifier.py
python3 verifier.py
python3 search.py --steps 250000 --restarts 10 --seed 791
```

`search.py` first exhausts every single fixed-type coordinate replacement in
`[0,540]`, then every pair of coordinate moves whose individual displacement
is at most 6.  It finally runs a deterministic, seeded simulated anneal that
permits temporary holes and uses the exact rule above for every evaluation.
It keeps the published type counts `(8,17,17)` and asks for `m>=511`.  This is
a cheap baseline/pattern search, not a complete SAT proof: failure cannot
establish that no better placement exists.

The output of the recorded run is in `SEARCH_RESULT.json`.

## Exact CP-SAT model

`cp_sat_search.py` encodes the same sufficient tile rule as an exact Boolean
feasibility problem.  OR-Tools is an optional search dependency:

```bash
python3 -m venv .search-venv
.search-venv/bin/pip install -r requirements-search.txt
.search-venv/bin/python cp_sat_search.py --seconds 300
```

The recorded fixed-count `(8,17,17)`, `ell=42`, `m=511` run searched for three
minutes and returned `UNKNOWN` after 2,613,105 branches; this is neither a
construction nor a nonexistence result (`CP_SAT_42_511_RESULT.json`).  The
original `--max-replacements-from-seed 2` result is **superseded**: that
model normalized `0` into `J` but measured distance from Kohonen's unswapped
`J/K` labels, so it did not encode the claimed radius ball.  The corrected
model in `campaign/sat/` re-establishes radii 1, 2, and 3 as UNSAT and includes
independently checked DRAT-proof hashes and statistics.  See
`campaign/sat/RESULTS.json`.

Finally, `--free-type-counts` (42 total segments, no fixed split) also returned
`UNKNOWN` after three minutes, having explored 66,231,305 branches
(`CP_SAT_FREE_COUNTS_RESULT.json`).

## Lower-bound literature audit

`audit_alzahrani_kernel.py` replays in exact rational arithmetic a defect in the
2016 Alzahrani thesis's claimed analytic improvement.  For its selected
`u(t)=9/4-100(t-1/2)^4`, one has `u(0)=-4` and the intended autocorrelation at
`1/2` is `-1009/4032`; both contradict the nonnegativity hypotheses used in the
proof.  See `ATTACK_20260813.md` for the qualified literature verdict.
