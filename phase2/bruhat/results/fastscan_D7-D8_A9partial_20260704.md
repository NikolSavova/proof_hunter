# fast.py --scan — D7 D8 complete, A9 partial (cogap<=3, procs=4, 2026-07-04)

> Salvaged from the run log: the process was killed at A9 candidate 200/209
> (worker death, suspected memory spike; ~2.9h into A9). D7 and D8 sweeps
> COMPLETED before the kill. Witness words below are as printed by
> fast.word_of (roundtrip-verified in-process).

## D7  (all 112 cogap<=3 candidates, 91s)
- verdict: **all pass**
- min ratio: 1.025574 (margin 11292231) at k=21
- witness: [e, 657456345723456123457123456123451234123121]  — i.e. [e, w0]
- NOTHING in the cogap<=3 slab beats the full group (F1 holds in D7).

## D8  (all 156 cogap<=3 candidates, 2269s)
- verdict: **all pass**
- min ratio: 1.017122 (margin 1298979344) at k=28 — NEW PROJECT RECORD LOW
- witness: [e, 86756845673456823456712345681234567123456123451234123121] = [e, w0]
- NOTHING in the cogap<=3 slab beats the full group (F1 holds in D8).

## A9  — ✅ NOW COMPLETE (2026-07-05, two runs stitched)
- run 1 (killed): candidates 1-200 of the deterministic sorted slab, all pass,
  best 1.028950 at [e, w0] (k=22).
- tail run (`fast.py --scan A9 --cogap 3 --skip 200`, results/fastscan_A9_51808.md):
  candidates 201-209, all pass, best among tail 1.031382 (k=21).
- verdict: **all 209 cogap<=3 candidates pass; nothing beats [e, w0] = 1.028950.
  F1 holds in A9.**
