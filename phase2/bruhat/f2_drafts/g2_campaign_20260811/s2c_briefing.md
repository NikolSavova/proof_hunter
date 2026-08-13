# (S2) attempt 3 — closure briefing (the maths lane)

*Brief handed to gpt-5.6-sol at `effort=max` for the third (S2) run. Kept as a reviewable
artifact. Attempt 2 (`sol_s2b_20260812.md`) reached all seven band constants and its
**entire numerical spine has now been independently reproduced** by a cross-model replay
(`referee_replay_sol_s2b_20260812.md`, Claude Opus 5, scripts under
`g2_scripts/campaign_20260811/wave6_sol/s2b_replay/`). What is missing is not numbers —
it is the DERIVATIONS. This run must close that.*

---

## STATUS: what is already verified (do not redo, do cite)

Every one of these reproduced from attempt 2's stated formulas alone, with no number
copied from it, under `mpmath.iv` directed-rounding interval arithmetic:

- the tilted model identity `s2 = m A_1(lam) - sum_j j^2 A_1(j lam)` against a
  brute-force truncated-geometric variance sum (12+ digits, three `(m, lam)`);
- `sup_{y>0} y^5 A_4(y) = 24.854113 < 25`; `F_1(8) = 11.0515 < 12`,
  `F_1(10) = 4.5433 < 5`, `F_1(14) = 0.4472 < 1`; `40000/81960 = 0.488042948`;
- the whole `H(w)` table (`w = 4,5,6,8,10,20`) and `T(w)` table (`w = 8,10,14,20,40`);
- the W1–W3 cell certificate (at the corrected width, see item 1) and the W4/W5/W6b
  monotonicity chain and W7 chain, scalar criterion by scalar criterion;
- the finite-`m` assembly, giving all seven: `U_b <= 0.0258 / 0.0188 / 0.0377 / 0.0909 /
  0.1436 / 0.1757 / 0.4877` against targets `0.05 / 0.06 / 0.08 / 0.10 / 0.15 / 0.25 / 0.50`.

**The mathematics of attempt 2 is very likely correct.** Your job is to make it
*checkable*, and to fix the five specific defects below.

---

## WHAT THIS RUN MUST DELIVER

Produce a **complete, self-contained, rigorous proof of (S2)** — every lemma stated with
its hypotheses, every derivation shown, nothing left to "directed rational arithmetic
gives". Specifically:

### 1. Cell width: the prescribed resolution does not certify W1

Attempt 2 (SOL.6, RECIPE §4) prescribes 64 cells on `[4,5]`, 64 on `[5,6]`, 128 on
`[6,8]` — all width `1/64` — and asserts `max_I V(I) < 0.030 / 0.040 / 0.065`. Replayed at
that width, **W1 gives `0.037828957`, failing its own `0.030`**. This is interval-
dependency inflation, not a false claim: refinement converges cleanly
(`1/64: 0.0378 | 1/128: 0.0242 | 1/256: 0.0173 | 1/512: 0.0140`), so the asserted bound is
TRUE and only the stated resolution is too coarse. **Either** restate at width `1/128`
(128/128/256 cells — verified to pass: `0.0242 / 0.0176 / 0.0365`), **or**, if you
intended an unstated monotonicity refinement at `1/64` (you use exactly such a trick for
the `F < 25` grid: "on `[a,b]` check `b^5 A_4(a) < 25`"), state and prove it.

### 2. SOL.7.8's numerator — a step that does not follow as written

You assert
`B_infinity(w,x) <= (|C - 24w| + 2w + T(w)) / (120 H(w))`
"using `sqrt(A^2 + B^2 y^2) <= |A| + B|y|`, `y = ux`, and `x <= 1/2`", with `B = 24w`.
With `|y| <= 1/2` that route gives `B|y| <= 12w`, and even using
`max_{|y|<=1/2} |y|/(1+y^2)^3 = 0.256` it gives `~6.14w` — **not `2w`**. The replay could
not re-derive the `2w`, and could not settle it because `u` and `B_infinity` are defined
only in SOL.2. Either derive `2w` explicitly from SOL.2's definitions, or correct it and
re-run the affected W4/W5/W6b numerics. (Note the downstream margins are thin — see item
4 — so a correction here may not be absorbable in silence.)

### 3. Supply the unaudited derivations

These were used but never derived in checkable form. Each needs a full proof:
- **SOL.2**'s dimensionless cancellation-preserving reduction (and explicit definitions of
  `u`, `x`, `B_infinity` — the replay had to infer their roles);
- **SOL.3**'s scalar-bound structure, including the paired Mittag-Leffler bound on
  `0 <= y <= 1/4` and the `F'(y) < 0` claim for `y >= 6`;
- **SOL.5**'s uniform finite-`m` reduction (SOL.5.2/5.3/5.6) — where `e_b`, `E_b` come from;
- **SOL.6**'s Cauchy `n`-tail: `|P(a,w)| <= 20 pi^2 4^6 + 192 * 4^5 < 1010000 =: M_C` and
  `3 M_C (2/3)^65 < 11e-6`, including why `Re a >= 1/4`, `|a| >= 1/4` on `|y| = 3/4`;
- **SOL.7**'s reductions to each scalar criterion (see item 2).

### 4. The margins are thinner than you stated — address them explicitly

The replay found four load-bearing constants with almost no room, none flagged in
attempt 2:

| quantity | value | requirement | slack |
|---|---|---|---|
| **`G(0.89)`** | 0.936525975 | `> 117/125 = 0.936` | **0.056%** |
| `B^2 < 6A^2` at `w = 14` | 112896 vs 115272.92 | `<` | 2.1% |
| W7 assembled | 0.487742 | `< 0.50` | 2.5% |
| W5 assembled | 0.143555 | `< 0.15` | 4.5% |

**The entire W7 band rests on the single evaluation `G(0.89) > 0.936`, with 0.056% of
slack.** Give that one an exact-rational certification (it is a single explicit value:
`G(y) = y^2 e^{-y}/(1 - e^{-y})^2` at `y = 89/100`), or restructure so W7 does not depend
on so sharp a threshold. State every margin honestly in the final text.

### 5. Define what you use

`G` and `F_1` are used throughout attempt 2 and never defined. The replay derived them
from `H'(w) = 1 - w^2 A_1(w)`, giving `G(w) = w^2 A_1(w)` and `F_1(w) = w^5 A_4(w)`, then
checked the identification numerically (9 digits at `w = 4, 10, 20`), and confirmed
`int_0^oo G = pi^2/3` and `G` decreasing (`G(w) = 1/s(w/2)^2`, `s(y) = sinh(y)/y`
increasing). **Confirm or correct these identifications and state them up front.**

---

## THE STATEMENT (unchanged)

For `m >= 561`, `lam in (4/m, 0.89]`, `w = m lam` in band `W`, and
`log phi(t) = -s2 t^2/2 - i kappa_3 t^3/6 + kappa_4 t^4/24 + R5(t)`:

```
|R5(t)| <= C5*(W) * s2 * t^5 / lam^3    for all t in [0, lam/2]
W1 (4,5]:0.05  W2 (5,6]:0.06  W3 (6,8]:0.08  W4 (8,10]:0.10
W5 (10,20]:0.15  W6b (20,40]:0.25  W7 (40,0.89m]:0.50
```

Model (verified): `Z_m(z) = prod_j (1-e^{-jz})/(1-e^{-z})`,
`E_lam e^{itX} = Z_m(lam-it)/Z_m(lam)`, `s2 = L''(lam)`, `kappa_3 = -L'''(lam)`,
`kappa_4 = L^(4)(lam)`, `L^(n)(lam) = (-1)^n (m A_{n-1}(lam) - sum_j j^n A_{n-1}(j lam))`.

## OUTPUT REQUIREMENTS

A single self-contained proof document. Every lemma numbered and proved. A final
**MARGIN TABLE** listing each load-bearing constant with its slack. A final
**WHAT REMAINS** section that is honest — if a step still rests on an unproved claim, say
so rather than papering over it. If any of items 1–5 reveals that (S2) is FALSE as stated
for some band, say that plainly and prove the best true variant.
