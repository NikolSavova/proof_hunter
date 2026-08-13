# Exact SAT closure lane for Erdős 791

This directory contains a global (not seed-radius) CNF encoding of the
three-tile placement problem.  For fixed `m` and type counts `(i,j,k)`, it asks
for sets `I,J,K` contained in `[0,m-1]` with those exact cardinalities and with
every `q=0,...,m-1` certified by

```text
q in I+J  OR  q in I+K  OR  (q-1 in J+K AND q in J+K).
```

`exact_cnf.py` channels membership, every pair witness, every represented sum,
direct coverage, and consecutive-`J+K` coverage in both directions.  It uses
only these sound global normalizations:

- `0 in I`, forced by coverage of `q=0` and nonnegative coordinates;
- `0 in J or 0 in K`, also forced at `q=0`;
- when `j=k`, exchange `J,K` to require `0 in J`, then conditionally choose the
  lexicographically greater set when both contain zero.

Coordinates at least `m` can be discarded because they cannot contribute to a
sum below `m`.  No assumptions about proximity to a known construction occur.

## Certified results (2026-08-13)

For the record-beating target

```text
m(ell) = floor(85*ell^2/294) + 1,
```

the elementary capacity inequality

```text
m <= i*(j+k) + j*k - 1
```

eliminates many type splits immediately.  `EXTREMAL_RESULTS.json` gives the
complete census of positive, `J/K`-unordered splits for `ell=18,...,24`.
Zero-cardinality cases are also impossible at these targets: `i=0` cannot
cover zero, while `j=0` or `k=0` leaves at most `i*(j+k) <= ell^2/4` squares.

Every one of the **20 capacity-tight splits** in this range was then encoded
globally and proved UNSAT by CaDiCaL 3.0.1.  Every proof was independently
accepted by `drat-trim`; the JSON records CNF/proof SHA-256 hashes, sizes,
timings, and checker summaries.  This includes all five tight splits at the
priority `ell=20,m=116` target:

```text
(2,9,9), (3,11,6), (6,11,3), (9,9,2), (11,6,3).
```

This result does **not** establish global UNSAT for `ell=20,m=116`: 29 other
capacity-feasible splits remain, including the main balanced split `(6,7,7)`.
Four bounded Kissat runs for `(6,7,7)` are recorded in
`GLOBAL_677_RUNS.json`.  The `K(0)=0` and `K(0)=1` cases exhaust the normalized
global instance, but each returned `UNKNOWN` at its 900-second wall bound.  A
second encoding of `K(0)=0` and a promising exact subcase also returned
`UNKNOWN`.  Across the four runs, Kissat explored 17,115,580 conflicts and
25,488,942,383 propagations.  There was no SAT model and no UNSAT proof, so the
balanced target remains strictly `UNKNOWN`.

As a representative retained proof, `ell20_m116_299.drat.gz` is the full DRAT
certificate for the `(2,9,9)` split:

```text
CNF:                64,483 variables, 274,220 clauses
CNF SHA-256:        22a0fbcc2c58ef2fd26bff35efa2f1037cb73a9ab0e368a99080448b04b340fb
DRAT SHA-256:       a9e47e0fa73f1d5d238b6e88e0adc67acdd3cb427ba1f0d3682dc36f84e79401
compressed SHA-256: fd0cda139fd6fba38f4d8e4a0d6fa64d1cc06b338e00384273c1fce22f9aa122
CaDiCaL time:       0.12 seconds
drat-trim:          VERIFIED, 18,622 resolution steps, 0 RAT lemmas
```

The extremal cuts are logical consequences of equality in the capacity bound:
all pair sums are in-range and collision-free, `I+J` and `I+K` are disjoint,
direct and consecutive coverage are disjoint, and the `J+K` sumset is one
interval.  These cuts only expose consequences already implied by the base CNF.

## Encoding validation

The published `ell=20,m=115`, split `(6,7,7)` construction was fixed as unit
membership clauses in the same encoding and CaDiCaL returned SAT.  The original
certificate independently passes `../verifier.py`, including literal
generalized-Mrose expansions at `t=2,3`.  In addition, all 2,814 unary-counter
cases through six inputs and 159 normalized fixed placements through `m=3`
were exhaustively compared with their direct semantics.  See `VALIDATION.json`.

## Reproduction

Generate and check the representative proof (paths to the solver/checker may
vary):

```bash
python3 exact_cnf.py --ell 20 --m 116 --counts 2 9 9 \
  --output /tmp/ell20_m116_299.cnf
gzip -dc ell20_m116_299.drat.gz > /tmp/ell20_m116_299.drat
drat-trim /tmp/ell20_m116_299.cnf /tmp/ell20_m116_299.drat
```

Regenerate the entire extremal census, solve each tight split, and check every
trace:

```bash
python3 run_extremal_batch.py \
  --solver /path/to/cadical --checker /path/to/drat-trim \
  --work /tmp/erdos791-extremal --output /tmp/EXTREMAL_RESULTS.json
```

Solver revisions used here were CaDiCaL commit
`c60730422e758ef1cebe7aeddf2dda31c996bf04` (version 3.0.1) and Kissat commit
`8af8e56f174b778aef3aa45af9f739b2a5f492c2` (version 4.0.4).

## Files

- `exact_cnf.py`: exact global encoding and sound redundant cuts.
- `decode_model.py`: extracts `I,J,K` from a SAT solver's DIMACS model.
- `run_extremal_batch.py`: census plus proof-producing batch runner.
- `EXTREMAL_RESULTS.json`: all capacity counts and all 20 checked runs.
- `GLOBAL_677_RUNS.json`: exact bounds and `UNKNOWN` status for the main split.
- `VALIDATION.json`: independent positive-control checks.
- `ell20_m116_299.drat.gz`: retained representative global UNSAT proof.
