# fast.py --scan A10 --cogap 2 — PARTIAL (killed mid-sweep, 2026-07-05)

- [e, w0] evaluated: **min ratio 1.022102 (k=27) — all pass.**
- Mahonian check: predicted 1/sigma^2 = 36/(11*10*27/72... ) = 0.024242;
  actual 0.022102 — the ~0.91x offset consistent with A7 (.0542/.0612),
  A8 (.0389/.0435), A9 (.0290/.0320). Decay law 1 + Theta(1/m^3) holds A4-A10.
- Slab sweep (65 cogap<=2 candidates): killed after candidate 1; resume with
  `fast.py --scan A10 --cogap 2 --skip 1`.
