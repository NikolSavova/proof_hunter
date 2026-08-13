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

## 3b. Bands W4, W5, W6b (SOL.7) and W7 (SOL.4) — ALSO REPLAYED, all pass

*(Added after the first version of this report; script
`s2b_replay/s2b_replay_w4w7.py`, output `out_s2b_replay_w4w7.txt`.)*

These four bands are monotonicity arguments rather than cell sweeps. The draft uses `G`
and `F_1` without ever restating them, so the identifications were **derived and then
checked, not assumed**: from `H(w) = w - pi^2/3 + 2 sum_r e^{-rw}S_2(rw)/r^2` one gets
`H'(w) = 1 - w^2 A_1(w)`, so `G(w) = w^2 A_1(w)` (= `h_2(w)` of the (S3) work) and
`F_1(w) = w^5 A_4(w)`. Numerical differentiation of `H` matches `1 - G` to 9 digits at
`w = 4, 10, 20`; `int_0^oo G = pi^2/3 = 3.2898681 < 3.29` as the draft asserts; `G` is
decreasing (analytically, `G = 1/s(w/2)^2` with `s(y) = sinh(y)/y` increasing).

```
[W7]  G(0.89)          = 0.936525975  vs required 117/125 = 0.936    (margin 1.000562x)
      D_m/m > G(0.89) - 3.29/40 = 0.854275975  vs claimed 683/800    PASS
      50/(120 D_m/m)  <= 0.487742461  vs 40000/81960 = 0.488042948   PASS
[W4]  at w=8: (C-192+16+T(8))/(120 H(8)) = 0.078066 < 0.079          PASS
      max J'(w) on [w_0,10] = -5.267860 < -3.2 ; J(10) = 1.868860 > 1.7   PASS
[W5]  max J_5'(w) on [10,14] = -4.732987 < -4.2 ; J_5(14) = 12.661611 > 12  PASS
      B^2 = 112896.000 < 6A^2 = 115272.920 at w=14   (margin 1.0211x) PASS
      monotonicity on [14,40]: min[(24-F_1)H - (24w-C+T)(1-G) - (121-w)] = 6.0087 > 0  PASS
      value at w=20 = 0.140941 < 0.142                                PASS
[W6b] value at w=40 = 0.173115 < 0.174                                PASS
```

Finite-`m` assembly for these bands (SOL.5.6), completing the seven:

| band | `L` | `B` | `U_b <=` | target `C5*` | margin |
|---|---|---|---|---|---|
| W4 | 4.737648 | 0.09 | 0.090920 | 0.10 | 1.100x |
| W5 | 6.715671 | 0.142 | 0.143555 | 0.15 | **1.045x** |
| W6b | 16.710133 | 0.174 | 0.175746 | 0.25 | 1.423x |
| W7 | — | — | 0.487742 | 0.50 | 1.025x |

**All seven band constants are now independently reproduced.**

### ⚠️ Margin observation (the main risk this replay surfaces)

Several load-bearing constants are *very* tight, and they were not flagged as such in the
draft:

- **`G(0.89) = 0.9365260` against the required `0.936` — 0.056% of slack.** The entire
  W7 band rests on this one evaluation. Had the draft rounded `117/125` even slightly
  differently, W7 would fail.
- `B^2 < 6A^2` at `w = 14`: 2.1% slack.
- W5's assembled constant: 4.5% slack. W7's: 2.5%.

Nothing here is wrong, but the chain has little room. Any later revision to an upstream
constant (`sup y^5 A_4 < 25`, the `H`/`T` tables, the scout's `C5*(W7) = 0.50`) must be
re-checked against these four points specifically, not assumed absorbed.

## 4. ⚠️ Scope — what this pass does NOT cover

1. ~~Bands W4–W7 were not replayed.~~ **DISCHARGED — see §3b.** Residual: the derivation
   *reducing* each band to its scalar criterion (notably SOL.7.8's numerator `|C-24w| +
   2w + T(w)`, whose `2w` term I could not re-derive from the stated `sqrt(A^2+B^2y^2) <=
   |A| + B|y|`, `y = ux`, `x <= 1/2` without SOL.2's definitions of `u` and
   `B_infinity`) remains unaudited. The scalar criteria themselves all reproduce.
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

**All seven band constants of (S2) now reproduce independently, and nothing I checked
contradicts the draft.** Attempt 1 was FATAL for proving none of the seven bounds, with a measured 23x
deficit on W1 from cancellation-free bounding; attempt 2 retains the cancellation and its
W1 constant reproduces at `0.0258` against the `0.05` target — a genuine ~45x improvement
in the binding quantity, independently confirmed here.

**But (S2) is NOT closed.** Under the house rule it still needs a full lemma-by-lemma
maths lane (§4.2) — the derivations connecting the verified numbers are unaudited, and
§4.1 records one step (SOL.7.8's numerator) I could not re-derive from the text as
written. The §2 cell-width repair must also be applied to the draft. What IS established:
the draft's numerical spine reproduces end to end from its stated formulas alone, across
all seven bands, with no number taken from it; its tight constants hold; and its only
reproducible defect is a resolution spec error that costs nothing downstream.

**Recommended status: (S2) = PARTIAL, numerics independently confirmed, maths lane owed.**
That is a strictly better position than any other open statement in the campaign — (S3)
has a known unproved sign hypothesis in W7, and (S4) has a circular sub-argument — but it
is not closure.
