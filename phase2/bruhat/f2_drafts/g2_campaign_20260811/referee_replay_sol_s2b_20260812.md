# Independent replay + partial referee pass on `sol_s2b_20260812.md` ((S2), attempt 2)

*2026-08-12. Reviewer: Claude Opus 5 (cross-model against the draft's gpt-5.6-sol),
running local compute only — the Fable referee fleet is unavailable (credits exhausted;
standing budget policy). This discharges the draft's own WHAT REMAINS item 2, which
required the SOL.6 cell calculation and the SOL.3 scalar grid to be "transcribed into an
archived exact-interval script and independently rerun".*

**Script:** `g2_scripts/campaign_20260811/wave6_sol/s2b_replay/s2b_replay.py`
**Outputs:** `out_s2b_replay.txt` (as-specified), `out_s2b_replay_refined.txt` (repaired)
Written from the draft's stated formulas only; no number was copied from the draft.
`mpmath.iv` directed-rounding intervals, dps 30, r-sums truncated at `r = 200` with a
`1e-100` slop interval (the `r = 201` term has log-magnitude `~ -579`).

## VERDICT: **MINOR_REPAIRS** — one reproducible spec error; every mathematical claim
## I could check reproduces, and the seven target constants survive

## 1. What reproduces (independent of the draft)

| Check | Draft's claim | Replay | |
|---|---|---|---|
| `s2` closed form vs brute-force truncated-geometric variance sum, `(m,lam)` = (7,0.37), (11,0.9), (23,0.13) | agreement, `s2 > 0` | agrees to 12+ digits, `s2 > 0` | PASS |
| `sup_{y>0} y^5 A_4(y) < 25` | `< 25` | `24.854113` at `y ~ 3.72` (0.58% slack) | PASS |
| `F(8) < 12`, `F(10) < 5`, `F(14) < 1` | as stated | `11.0515`, `4.5433`, `0.4472` | PASS |
| `40000/81960 < 0.50` | `0.48804...` | `0.488042948` | PASS |
| `H(w)`, `w = 4,5,6,8,10,20` | six narrow windows | all inside, e.g. `H(4) = 1.193334 in (1.193, 1.194)` | PASS |
| `T(w)`, `w = 8,10,14,20,40` | five ceilings | all under, e.g. `T(8) = 22.98988 < 23.01` | PASS |

Several of these are **tight** — `sup y^5 A_4` clears its bound by 0.58%, `T(8)` by 0.09%.
Constants that sharp are not reproduced by accident; the draft's analytic work behind them
is doing real labour.

## 2. The one discrepancy — a RESOLUTION spec error, not a mathematical error

The draft (SOL.6, and VERIFICATION RECIPE §4) prescribes **64 cells on `[4,5]`, 64 on
`[5,6]`, 128 on `[6,8]`, all of width `1/64`**, and asserts the resulting
`max_I V(I) < 0.030 / 0.040 / 0.065`.

**At the prescribed width `1/64`, W1 fails its own ceiling:**

```
W1: max V(I) = 0.037828957  vs stated 0.030   -> FAIL   (worst cell [4, 257/64])
W2: max V(I) = 0.023946430  vs stated 0.040   -> PASS
W3: max V(I) = 0.037651258  vs stated 0.065   -> PASS
```

This is **interval-dependency overestimation, not a false claim**: evaluating the heavily
cancelling bracket `(n+5)c - w - (n+5) sum_r ...` over a wide cell inflates the enclosure.
Refining shows clean convergence, so the asserted bound is TRUE and only the stated
resolution is insufficient:

```
W1, 64 cells  (1/64) : 0.037828957   FAIL
W1, 128 cells (1/128): 0.024174220   PASS
W1, 256 cells (1/256): 0.017349285   PASS
W1, 512 cells (1/512): 0.013995815   PASS
```

**Repair (adopted here): halve the cell width to `1/128` throughout** — i.e. 128 cells on
`[4,5]`, 128 on `[5,6]`, 256 on `[6,8]`. At that resolution the full certificate passes:

```
W1: max V(I) = 0.024174220 < 0.030      (worst cell [4, 513/128], inf H = 1.189518)
W2: max V(I) = 0.017550592 < 0.040      (worst cell [5, 641/128], inf H = 1.958868)
W3: max V(I) = 0.036526655 < 0.065      (worst cell [1023/128, 8], inf H = 4.729788)
```

*Caveat in the draft's favour:* it may intend an unstated monotonicity refinement at
width `1/64` (it does use exactly such an argument for the `F < 25` grid, "on `[a,b]`
check `b^5 A_4(a) < 25`"). If so the fix is to state it. Either way the text as written
does not certify W1 at the resolution it prescribes.

## 3. Final constants — the thing that actually matters — all survive

Propagating the **replayed** continuum bounds through the finite-`m` assembly
(SOL.5.6: `U_b = L/(L-e_b) B + E_b/(120(L-e_b))`, `L = inf_band H`):

| band | `L` | `e_b` | `E_b` | `U_b <=` | target `C5*` | margin |
|---|---|---|---|---|---|---|
| W1 | 1.193334 | 1.2577e-4 | 0.238219 | **0.025840** | 0.05 | 1.94x |
| W2 | 1.960829 | 1.9065e-4 | 0.290629 | **0.018788** | 0.06 | 3.19x |
| W3 | 2.834331 | 3.7282e-4 | 0.400215 | **0.037708** | 0.08 | 2.12x |

These are **better than the draft's own stated** `0.0318 / 0.0413 / 0.0663`, because the
refined cells give tighter `B`. Note also that even the *pessimistic* width-`1/64` values
still clear the targets (W1: `U_b <= 0.039497 < 0.05`), so the spec error of §2 never
threatened the (S2) constants — only the intermediate lemma as stated.

## 4. ⚠️ Scope — what this pass does NOT cover

1. **Bands W4, W5, W6b (SOL.7) and W7 (SOL.4) were not replayed.** Their arguments are
   analytic rather than cell-based; my script covers W1–W3 only. The draft's claimed
   `W7: 40000/81960 < 0.4881 < 0.50` scalar reproduces (§1), but the derivation that
   *reduces* W7 to that scalar was not audited.
2. **No line-by-line maths audit** of SOL.1–SOL.8. I verified the model identity, the
   scalar constants, the H/T tables, the W1–W3 certificate, and the W1–W3 assembly. The
   analytic derivations — SOL.2's dimensionless reduction, SOL.3's scalar-bound structure,
   SOL.5's uniform finite-`m` reduction, SOL.6's Cauchy `n`-tail (`M_C < 1010000`,
   `3 M_C (2/3)^65 < 11e-6`), SOL.7's analytic bounds — are **unaudited**. A full maths
   lane is still owed.
3. **Interval-library standard.** As with the (S3) certificate, this replay is rigorous
   *modulo* `mpmath.iv` (1.4.1, CPython 3.12.2) providing outward rounding; it is not the
   exact-rational computation the draft advertises ("All 256 interval comparisons are
   rational"). The margins are large enough that this is unlikely to bite, but it is not
   proved here.
4. The `r`-sum truncation at `r = 200` and the `n <= 64` cut are inherited from the
   draft's own design; the `n >= 65` Cauchy tail `11e-6` was **used, not verified**.

## 5. Bottom line

**(S2) attempt 2 is materially stronger than attempt 1 and nothing I checked contradicts
it.** Attempt 1 was FATAL for proving none of the seven bounds, with a measured 23x
deficit on W1 from cancellation-free bounding; attempt 2 retains the cancellation and its
W1 constant reproduces at `0.0258` against the `0.05` target — a genuine ~45x improvement
in the binding quantity, independently confirmed here.

**But (S2) is NOT closed.** Under the house rule it needs a full maths referee lane
(§4.2) and a pass over W4–W7 (§4.1), plus the §2 repair applied to the draft text. What
is established is that the draft's numerical spine, where I could check it, is real: it
reproduces from the stated formulas alone, its tight constants hold, and its one
reproducible defect is a cell-count spec error that costs nothing downstream.
