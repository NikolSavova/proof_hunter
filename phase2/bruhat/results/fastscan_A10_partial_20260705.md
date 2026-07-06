# fast.py --scan A10 --cogap 2 — PARTIAL (killed mid-sweep, 2026-07-05)

- [e, w0] evaluated: **min ratio 1.022102 (k=27) — all pass.**
- Mahonian check: predicted 1/sigma^2 = 36/(11*10*27/72... ) = 0.024242;
  actual 0.022102 — the ~0.91x offset consistent with A7 (.0542/.0612),
  A8 (.0389/.0435), A9 (.0290/.0320). Decay law 1 + Theta(1/m^3) holds A4-A10.
- Slab sweep (65 cogap<=2 candidates): TWO runs killed by an unidentified
  external signal (not OOM — 22GB free; not sleep — caffeinate held).
  Progress before the second kill: several candidates evaluated, bests
  1.022162 -> 1.022103 -> 1.022102 — i.e. a proper near-top interval
  EXACTLY TIES [e,w0], the same tie phenomenon as A6/D6. Consistent with F1
  ("proper intervals tie but never beat").
- FINAL STATUS (2026-07-06): sweep STOPPED DELIBERATELY at ~11/65 candidates
  (8 from the killed runs + 3 more detached). The remaining cogap-2 candidates
  in S11 have complements ~10-100x larger than estimated (3 workers spent 2+
  CPU-hours each on single candidates, memory-thrashing) — out of scope for
  pure Python. Everything checked passes; a proper interval EXACTLY TIES
  [e,w0] at 1.022102 (F1-consistent, same as A6/D6).
- TO RESUME LATER: `fast.py --scan A10 --cogap 2 --skip 4` — but first either
  (a) port the complement-BFS hot loop to C/Rust (HANDOFF-sanctioned), or
  (b) run in 6h resumable chunks on the bruhat-scan CI workflow.
- F1 stands verified by completed sweeps in A7, A8, A9, D7, D8, E7.
