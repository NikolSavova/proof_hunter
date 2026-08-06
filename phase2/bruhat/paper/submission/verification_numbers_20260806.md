# Verified exact numbers for the paper's Tables 1-2 (agent-confirmed 2026-08-06)

Source-verified against the actual result files (not HANDOFF.md prose). Every
number below is cited with its exact source path.

## Table 1 additions (exhaustive tier)

| Group | \|W\| | #intervals | min ratio | witness [u,v], k | ranks |
|---|---:|---:|---:|---|---|
| A7 | 40,320 | 170,288,585 | 1.054250 = 919681/872356 | proper interval, len 27 (ties [e,w0]), k=14 | `[1,7,27,76,174,343,602,961,1415,1940,2493,3017,3450,3736,3836,3736,3449,3011,2474,1898,1344,865,496,247,103,34,8,1]` |
| B6 | 46,080 | 350,676,009 | 1.000000 (F3 pattern) | [e, 5656], k=2 | (1,2,2,2,1) |
| E6 | 51,840 | 466,250,713 | 1.028446 (decimal only) | **NOT RECOVERABLE — witness/rank-seq lost, see caveat** | — |

Sources: `run_A7_2253.md` + `run_A7_64099.md` (two independent full runs,
byte-identical); `run_B6_2311.md` + `run_B6-E6_segment_coverage.md` +
`run_B6_from9000_70875.md` (segment union 193,249,546 + 157,426,463 =
350,676,009, exact match); `run_B6-E6_segment_coverage.md` +
`run_E6_from6000_70876.md` + `logs/E6_from6000.log` for E6.

**E6 CAVEAT (must appear in the paper — do not silently omit):** E6 ran in two
segments after a process kill. Segment 1 (u<6000) survived only as a checkpoint
stream (running min_ratio logged, but not [u,v] or rank sequence). Segment 1's
min (1.028446, stable u=1000..6000) is strictly LOWER than segment 2's own min
(1.038373 = 4656964/4484865, witness [42354234654, 12314231454231435426542314354265431],
k=13 — this witness IS recoverable, just not the global one). **The paper
cannot print an exact witness/rank-sequence for the E6 row** — state the
decimal min ratio only, with an explicit note that the witness requires a
re-scan of u<6000 (documented as a known follow-up, not silently dropped).
B6 has NO such gap (independent non-segmented cross-check exists).

## Table 2 (near-top slab) — E7 confirmed, no changes needed

`fastscan_E7_2317.md`: min ratio 1.011829 = 65523/64757, k=31, witness = [e,w0]
— verified two ways: fraction matches decimal exactly; sum of the 64 rank
entries = 2,903,040 = |W(E7)| exactly (weyl.py:70), confirming this is the
FULL interval [e,w0] (ell(w0)=63). Minor documentation gap (no explicit
"N/M candidates" completeness line, unlike A10's row) — not a numeric
discrepancy, just worth noting in methodology as a minor asymmetry in how
thoroughly each run logged its own completeness.

## Spot-checks (all exact matches, zero discrepancies)

A6, D6, B5, and (while reading the same source file) A2-A5, B2-B4, D4-D5, F4,
G2 — every existing skeleton Table-1 row matches its source file exactly.

## GRAND TOTAL for the abstract

92,275,684 (previously-summed skeleton rows) + 170,288,585 (A7) + 350,676,009
(B6) + 466,250,713 (E6) = **1,079,490,991 intervals, zero violations.**

**HEADLINE CHANGE:** the old skeleton draft says "over 9x10^7" — the true
figure is ~1.08x10^9, a ~12x jump (order of magnitude 10^8 -> 10^9). Use the
new figure everywhere; this is a materially stronger number for the abstract,
not a rounding correction.

## Methodology caveats to disclose (§3/§7 of the paper)

1. "Exhaustive" = enumerate every u in 0..|W|-1, BFS all v>=u, exact integer
   rank counts. E6 and B6 ran as two complementary non-overlapping segments
   after process kills; segment boundaries are documented and complementary
   (`run_B6-E6_segment_coverage.md`) — genuine full cover, but E6 lost its
   witness data as above.
2. A7's witness is a length-27 proper interval (not [e,w0] itself, which
   would need length 28) that ties rho([e,w0]) exactly (919681/872356, same
   fraction as the Table 2 A7 row) — word this identically to the existing
   A5/A6/D6 "proper interval ties [e,w0]" pattern in the skeleton, for
   consistency.
