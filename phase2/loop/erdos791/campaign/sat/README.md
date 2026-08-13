# Exact-search lane: Erdős #791 campaign

## Outcome

No record placement was found.  The concrete exact advance is a corrected,
proof-producing closure of replacement radii 1, 2, and 3 around Kohonen's
`(8,17,17)` placement for the target `m=511` in coordinates `[0,510]`.
All three DRAT traces were independently accepted by `drat-trim`; radius 3
required 108,746,580 resolution steps in the checker.

The smaller live target was also re-audited.  For the block-family seed
`ell=20,m=115`, counts `(6,7,7)`, the normalized radius-0 instance recovers the
seed and passes the independent verifier.  At target `m=116`, corrected radii
1, 2, 3, and 4 are all UNSAT with independently checked DRAT proofs.  The
radius-4 solver run took 18.30 seconds and its proof check used 35,576,353
resolution steps.  (The old radius-4 CP-SAT attempt was only `UNKNOWN`.)

The coordinate bound is without loss for this fixed target: a nonnegative
coordinate above 510 contributes no pair sum at most 510, and can be moved to
an unused coordinate inside `[0,510]` without removing relevant coverage (or
increasing replacement distance from this seed).

The old `../../cp_sat_search.py` result needs a qualification: it forces
`0 in J`, invoking the `J <-> K` symmetry, but compares membership bits to the
*unswapped* published seed, in which `0 in K`.  Thus its radius was not the
claimed radius around the normalized Kohonen placement.  Both models here
swap the seed labels first.  The corrected radius-2 result remains UNSAT and
now has an independently checked DRAT proof.

The same bug invalidates the *evidentiary value* of the older
`../theory/CP_SAT_20_116_RADIUS3.json`: `sat_lean.py` forced `0 in J` but
measured distance from the unswapped family seed where `0 in K`.  Its stated
radius-3 conclusion did not follow from that run.  The corrected result in
`RESULTS.json` re-establishes radius-3 UNSAT with consistent labels and a DRAT
proof; this is a replacement result, not a rehabilitation of the old run.

An unrestricted proof-producing run at the smaller target, with counts
`(6,7,7)` but no radius constraint, remained `UNKNOWN` after 1,431,127
conflicts.  Its compact statistics are in
`global_ell20_6_7_7_m116.json`; the partial trace was discarded and supports
no negative conclusion.

## Reproduce

Install OR-Tools (the campaign used 9.15.6755) and run the compact
sorted-coordinate model:

```bash
python selector_cp_sat.py --target-m 511 --coordinate-bound 510 \
  --max-replacements-from-seed 3 --seconds 600 --workers 8
```

For proof-producing SAT, build CaDiCaL and `drat-trim`, then:

```bash
python generate_cnf.py --radius 3 --output radius3.cnf \
  --metadata radius3_cnf_metadata.json
cadical --unsat --no-binary radius3.cnf radius3.drat
drat-trim radius3.cnf radius3.drat
```

The generated CNF/DRAT files are intentionally not committed (roughly 28 MB
and 615 MB at radius 3).  Their SHA-256 digests, dimensions, solver statistics,
and check status are recorded in `RESULTS.json`; regenerate them from the
deterministic `generate_cnf.py` when needed.

The SAT encoding was tested in the positive direction too:

```bash
python generate_cnf.py --target-m 510 --coordinate-bound 510 --radius 0 \
  --output smoke.cnf --metadata smoke-metadata.json
cadical -w smoke.sol smoke.cnf
python decode_solution.py smoke-metadata.json smoke.sol --output smoke.json
python ../../verifier.py smoke.json --direct-t 2 3 5 10
```

This recovers the normalized Kohonen placement and the independent verifier
passes both the tile predicate and all literal expansion checks.

## Files

- `selector_cp_sat.py`: exact sorted-coordinate/selectable-witness CP-SAT
  formulation (42 placement integers rather than a full Boolean convolution).
- `generate_cnf.py`: deterministic elementary DIMACS encoding with exact unary
  cardinality circuits and Tseitin pair-sum variables.
- `decode_solution.py`: converts a DIMACS witness into verifier JSON.
- `RESULTS.json`: precise positive, negative, bounded, and proof-check results.
- `selector_*.json`: compact raw CP-SAT results.

Every negative conclusion is local to the model scope stated in
`RESULTS.json`; none resolves Erdős #791.
