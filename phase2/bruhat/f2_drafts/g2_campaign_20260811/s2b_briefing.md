# (S2) attempt 2 — prover briefing

*The brief handed to gpt-5.6-sol for the second (S2) attempt, kept as a reviewable
artifact. Attempt 1 (`sol_s2_20260812.md`) was judged **FATAL** by its adversarial
maths referee — "not for error, for absence": internally correct at every line
checked, but it proved **zero of the seven band bounds that (S2) IS**, and its stated
blocker (that the bands were undefined) was false at the corpus level. That blocker
was **the prompt's fault** — attempt 1 was given one terse sentence and no attachments,
so it never saw the band table. This briefing fixes that and adds the referee's own
strategic findings.*

---

## THE EXACT STATEMENT TO PROVE

(Consumer interface, verbatim from `CL_composition_20260812.md` §4, re-verified by the
adversarial referee in `referee_maths_sol_s2.md` §1.)

For `m >= 561`, `lam in (4/m, 0.89]`, with `w = m lam` in band `W`, and

```
log phi(t) = -s2 t^2/2 - i kappa_3 t^3/6 + kappa_4 t^4/24 + R5(t),
```

prove the bandwise remainder bound

```
|R5(t)| <= C5*(W) * s2 * t^5 / lam^3        for all t in [0, lam/2],
```

with bands and target constants:

| band | `w = m lam` | `C5*` |
|---|---|---|
| W1 | (4, 5] | 0.05 |
| W2 | (5, 6] | 0.06 |
| W3 | (6, 8] | 0.08 |
| W4 | (8, 10] | 0.10 |
| W5 | (10, 20] | 0.15 |
| W6b | (20, 40] | 0.25 |
| W7 | (40, 0.89 m] | **0.50** |

**W7 = 0.50** is the wave-6 scout adjustment (`wave6_s1_plan_20260812.md` §6); the
superseded value is 0.80. If only 0.80 is reachable, say so explicitly — that is the
documented fallback and costs the (S1) worst-band margin `27.21% -> 13.55%`.

## THE MODEL (referee-verified — use, do not re-derive)

```
Z_m(z) = prod_{j=1..m} (1 - e^{-jz})/(1 - e^{-z}),   E_lam e^{itX} = Z_m(lam - it)/Z_m(lam)
K(u) = L_m(lam - u) - L_m(lam);   s2 = L''(lam),  kappa_3 = -L'''(lam),  kappa_4 = L^(4)(lam)
L^(n)(lam) = (-1)^n ( m A_{n-1}(lam) - sum_{j=1..m} j^n A_{n-1}(j lam) )
   (A_4 numerator = Eulerian row 1 + 11q + 11q^2 + q^3)
s2 = sum_j Var(U_j),  Var(U_j) = A_1(lam) - j^2 A_1(j lam) > 0 for j >= 2, = 0 at j = 1
```

## THE DECISIVE STRATEGIC FACT — why attempt 1 failed mathematically

**A cancellation-free bound CANNOT work on W1–W6b.** The referee measured the deficit:
attempt 1's only quantitative bound gave `C_abs = 1.15907` against W1's target `0.05` —
a factor ~23 — and diagnosed the cause as **structural**: in `L^(5)` the `m`-term and
the `j`-sum nearly cancel at small `lam`, and a triangle-inequality bound adds their
magnitudes instead of retaining the cancellation.

**The proof must retain that cancellation.** Recommended starting point: attempt 1's
exact remainder identity **SOL.3.1** with its `E_4` structure, which the referee
verified as correct and named "the correct starting point for a cancellation-retaining
bandwise bound" (dual form SOL.3.2 is referee-friendly).

Two further binding referee facts:

- **W7 is the EASIEST band, not the hardest.** The referee's sample gave
  `C_abs <= ~0.263` on W7, so a cancellation-free argument plus a sup argument may close
  W7 at 0.50 outright.
- **Hard floor:** any band containing `w -> oo` has `liminf`-of-sup `>= 0.184013`. So
  `0.50` on W7 is safe, but **no constant below ~0.19 is ever achievable there** — do
  not propose one.

## REUSABLE FROM ATTEMPT 1 (referee salvage inventory, §3-F6)

Lemmas SOL.1, SOL.2 (tilted partition function, derivative formulas — hand-verified,
brute-force checked to `<1e-57`), SOL.3.1/SOL.3.2 (the exact remainder identity),
SOL.5.2 (stable `t -> 0` evaluation, cross-validated against the scout's `kappa_5`),
SOL.5.3 (interface-exact criterion, W7 constant re-pointed to 0.50), and SOL.4 as the
W7 closer candidate.

## FRAMING ERRORS NOT TO REPEAT

1. Do **not** claim the bands are undefined — they are defined above and in
   `wave5_sl4pe_20260812.md` §0.
2. Do **not** use the stale `C5*(W7) = 0.80` without invoking the fallback explicitly.
3. Do **not** treat a cancellation-free bound as progress on W1–W6b.
