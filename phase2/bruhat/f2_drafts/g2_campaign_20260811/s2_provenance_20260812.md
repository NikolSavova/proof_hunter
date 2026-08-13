# (S2) — certificate provenance record

*Written 2026-08-12 to discharge the standing provenance finding against (S2). The Sol
numerics referee on `sol_s2c_20260812.md` returned MAJOR_ISSUES whose first four items were
all of one kind: the load-bearing certificates are "asserted but not archived", their quoted
maxima "FABRICATED-until-sourced", and — its sharpest point — "the cited replay is for
`sol_s2b`, while the reviewed object is `sol_s2c`; no hash or output proves that the
corrected width and 1/8 coefficient were rerun."*

**All of those artifacts exist, are committed, and are listed here with their outputs.**
This is a recording task, not mathematics; no claim below is new.

## Archived scripts and outputs

All under `g2_scripts/campaign_20260811/wave6_sol/s2b_replay/`:

| file | what it certifies |
|---|---|
| `s2b_replay.py` | blocks [A]-[E]: model identity, scalar constants, `H`/`T` tables, the 256/512-cell W1-W3 certificate, finite-`m` assembly |
| `out_s2b_replay.txt` | output at the draft's **as-specified** width `1/64` (records the W1 failure) |
| `out_s2b_replay_refined.txt` | output at the **repaired** width `1/128` (all bands pass) |
| `s2b_replay_w4w7.py` | bands W4, W5, W6b (SOL.7 monotonicity chain) and W7 (SOL.4), plus the `G`/`F_1` identification checks |
| `out_s2b_replay_w4w7.txt` | its archived output |

Environment: `mpmath 1.4.1`, CPython 3.12.2, `mpmath.iv` directed-rounding intervals at
dps 30, `r`-sums truncated at `r = 200` with a `1e-100` slop interval. Every script was
written from the draft's stated formulas alone; **no number was copied from the draft.**

## The specific objection about `s2b` vs `s2c`

Correct, and answered. Attempt 3 changed the `L^1` trapezoid constant from `1/12` to `1/8`
(a correction attempt 3 made to its own attempt 2, and one this session independently
verified: `sup|K| = h^2/8` governs the `L^1` form, while `1/12 = int|K|` belongs to the
`L^infinity` form). That changes `e_b` and `E_b`, hence the assembly. **The assembly was
re-run with attempt 3's constants**, and the result is recorded in
`referee_replay_sol_s2b_20260812.md` §6:

```
e_b = h^2(w/12 + 7/4)      E_b = 49h/2 + 375 h^2 + w h^6/200      [375 <- the 1/8 form]
W1 : U_b <= 0.025937 < 0.05   W4 : U_b <= 0.090994 < 0.10
W2 : U_b <= 0.018898 < 0.06   W5 : U_b <= 0.143768 < 0.15
W3 : U_b <= 0.037858 < 0.08   W6b: U_b <= 0.176094 < 0.25
```

All six reproduce attempt 3's stated bounds; margins are essentially unchanged from the
`1/12` run (W5 remains tightest, 4.3%). The invalid constant never threatened a target.

## What this record does NOT claim

1. It does not make (S2) closed. The maths lane returned MINOR_REPAIRS and those repairs
   are not yet applied to `sol_s2c_20260812.md`; the numerics lane's remaining items
   (cryptographic hashes, an exhaustive rather than sampled boundary scan) are unaddressed.
2. The computations remain rigorous **modulo the interval library** — they are not the
   exact-rational computations the draft's prose advertises. Closing that means a `Fraction`
   rerun with rational envelopes for `exp`/`cos`/`sin`, or a port to an audited package such
   as Arb. The margins (worst 0.058% on `sup y^5 A_4`, 0.056% on `G(0.89)`) are wide enough
   that this is unlikely to bite, but it is not proved.
3. No SHA-256 chain-of-custody is supplied. A referee wanting it should hash the listed
   files and re-run.
