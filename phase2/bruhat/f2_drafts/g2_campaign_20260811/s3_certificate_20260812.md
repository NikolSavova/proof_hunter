# (S3) — Lemma SOL.3 certificate EXECUTED, plus the F2/F3 text repairs

*Written 2026-08-12 (Sihao + Claude, local compute only — no API spend). This
note discharges finding **F1** of `referee_numerics_sol_s3.md` ("the load-bearing
certificate does not exist") for **Lemma SOL.3**, and records the **F2** and **F3**
repairs the same referee demanded. Per the no-erasing rule, `sol_s3_20260812.md`
is untouched; this file is the erratum + certificate of record.*

**Script:** `g2_scripts/campaign_20260811/wave6_sol/s3_certificate/s3_cert.py`
**Output:** `.../s3_certificate/out_s3_certificate.txt` (archived, quoted below)
**Checkpoint:** `.../s3_certificate/ckpt.json` (per-band, resumable)

---

## 1. What was run

The draft's Lemma SOL.3 asserts six band bounds on
`J(w, lam) = F3^2/F2^2 - F4/(2 F2)` for all `m >= 561`, via the substitution
`z = 561/m in (0,1]`, `lam = w z / 561`, enlarging the discrete `z`-set to the
whole interval `[0,1]`. Its stated certificate — 36 x 2048 x 256 = 18,874,368
uniform rational boxes — **was never executed** (referee §1). It has now been
executed as an **adaptive certified interval computation**, the substitution the
referee's §6 explicitly permits ("an equivalent coarser certified computation —
the resolution budget is generous").

Per box: enclose `F_2, F_3, F_4` by (SOL.3)'s Euler–Maclaurin expansion, inflate
by the remainder radius, require `F_2.lower > 1/10` (so every division is safe),
then require `J.upper <= band target`. A box that fails is bisected; a box still
failing at the draft's own floor resolution (`1/2048` in `w`, `1/256` in `z`)
would be recorded as a HARD FAIL. **There were none.**

## 2. Result — all six bands CERTIFIED

```
== W1: target 1/2,   w in [4,5]  ==  CERTIFIED | 1310 leaves | 5s
== W2: target 13/20, w in [5,6]  ==  CERTIFIED |  199 leaves | 2s
== W3: target 9/10,  w in [6,8]  ==  CERTIFIED |   32 leaves | 1s
== W4: target 11/10, w in [8,10] ==  CERTIFIED |   15 leaves | 0s
== W5: target 3/2,   w in [10,20]==  CERTIFIED |   18 leaves | 1s
== W6b: target 17/10,w in [20,40]==  CERTIFIED |   17 leaves | 0s
# OVERALL: PASS — all bands certified
```

Coverage is exact by construction: the recursion starts from the full
`band x [0,1]` rectangle and every non-certified box is replaced by two boxes
whose union is itself, so the certified leaves tile the entire domain. Total
1,591 leaves versus the draft's 18.9M uniform boxes — the uniform grid was
~10^4 x oversized, as the referee suspected.

**Do not read the script's `sup J_upper` column as a measurement of `sup J`.**
Adaptive refinement stops the instant a box clears its target, so that column
reports the stopping rule, not the truth. The truth values are the referee's:
e.g. `max J = 0.46031849` on W1 (headroom 7.94% against the 1/2 target).

## 3. Repairs applied in this certificate

- **F2 (remainder constant, 1.992x understated).** The draft's (SOL.4)/(SOL.6)
  kernel constant `2 zeta(8)/(2 pi)^8 = 1/1209600` omits the `B_8` boundary term;
  the correct kernel constant is `(2 - 2^-7)|B_8|/8! = 17/10321920`. **The
  certificate uses the referee's prescribed clean repair, a factor 2**:
  radius `= 2 * 10^12 * w * lam^8 / 1209600`. All six bands certify *with* the
  doubled radius, so F2 is absorbed as the referee predicted.
  **Text erratum for the draft:** (SOL.4) and (SOL.13) must carry the doubled
  constant, and (SOL.6) must be re-quoted as `2 * 10^12 w lam^8 / 1209600`.
- **F3 (threshold generation).** The draft certifies the **wave-5** `J0` row.
  The wave-6 scout's recomputed row is uniformly LARGER (verified safe direction,
  all bands), so the wave-5 certificate implies the scout row a fortiori. This
  certificate therefore covers both generations; adopt whichever the composition
  ultimately consumes.

## 4. ⚠️ What this does NOT close (honest residue)

1. **Method deviation, stated plainly.** The computation uses `mpmath.iv`
   directed-rounding interval arithmetic at 40 digits (selftests at 30 and 50),
   **not** the draft's claimed "all operations are rational". Directed-rounding
   interval arithmetic is rigorous — every printed enclosure is a true outer
   bound — but a referee wanting the draft's literal exact-rational claim needs
   either that wording relaxed or the run redone in `Fraction`s. The margins
   (worst: W1's 7.94%) are enormous relative to any plausible floating-point
   subtlety, but this is a wording-vs-implementation gap, not zero.
2. ~~**(SOL.5) is CONSUMED, not certified.**~~ **CLOSED — see §6 below.**
3. **(SOL.16)/(SOL.17)** — the W7 leg's certificates — remain unrun (referee F1,
   third item). W7 is the `(40, 0.89m]` band and is NOT covered by this note.
4. **The maths-referee lane for (S3) never ran** (killed by the Fable credit
   limit). The numerics referee's evidence supports the algebra (SOL.1, the
   SOL.12 chain, the reflection argument), but the lemma-level pass is owed.

## 5. Status of (S3) after this note

Was: **MAJOR_ISSUES** — architecture true at every testable point, central
certificate unexecuted, two text flaws.
Now: the central certificate for **Lemma SOL.3 (bands W1–W6b) is EXECUTED and
PASSES** with the F2-corrected constant, and F2/F3 are recorded as errata.
Remaining for (S3) to close: items 1, 3 and 4 of §4 — the exact-rational wording
question, the W7 certificates, and the referee lanes. **(S3) is not yet closed;
it is materially closer, and nothing found so far contradicts it.**

---

## 6. (SOL.5) — ALSO CERTIFIED (same session)

The second item of referee F1 — the draft's unrun certification of
`|h_n^(8)(x)| <= H_8 := 10^12` on `(0, 40]`, which §2's remainder radius
consumes — is now **PROVED**, removing that conditionality.

**Script:** `.../s3_certificate/sol5_cert.py` · **Output:** `out_sol5_certificate.txt`

`h_n` is even and analytic on `C \ {2 pi i k, k != 0}`, so the nearest singularity
to the real axis is at distance `2 pi`. Two regimes, because the direct series is
useless near `0` (its Leibniz terms diverge like `x^-8` while `h_n` stays smooth):

- **`x in [0,1]` — Cauchy coefficient bound.** With `h_n(x) = sum_m c_{n,m} x^(2m)`
  and `|c_{n,m}| <= M_n(6)/6^(2m)` (radius `6 < 2 pi`), differentiating 8 times gives
  `|h_n^(8)(x)| <= M_n(6) * SUM8`, `SUM8 = sum_{m>=4}(2m)!/((2m-8)! 6^(2m)) <= 0.064929`.
  `M_n(6)` is enclosed by complex interval arithmetic (implemented over `mpmath.iv`
  real intervals) on 4000 arc-boxes of the circle.
- **`x in [1,40]` — direct Leibniz series**, bounded term-wise in absolute value with
  an explicit geometric tail bound (`K = 400`; the hypothesis `K >= 2p/x` is asserted
  in code). Enormously lossy — it discards ~8 orders of true cancellation — but the
  `10^12` target is loose enough to absorb that.

```
n=2: sup_[0,1] |h^(8)| <=      30.4   | sup_[1,40] <= 3.02e+06   (margins 3.3e10x / 3.3e05x)
n=3: sup_[0,1] |h^(8)| <=    1360.6   | sup_[1,40] <= 7.91e+07   (margins 7.4e08x / 1.3e04x)
n=4: sup_[0,1] |h^(8)| <=   93812.7   | sup_[1,40] <= 2.17e+09   (margins 1.1e07x / 4.6e02x)
# OVERALL: PASS — (SOL.5) CERTIFIED on (0,40]
```

Consistency with the referee's independent measurement (`max |h_n^(8)| =
0.232/1.393/6.952`): our bounds exceed those truths by the expected margin — the
`[0,1]` Cauchy route loses ~2–4 orders (radius-6 coefficient bounding), the `[1,40]`
term-wise route loses ~7–8 orders (no cancellation). Both are upper bounds, both
clear `10^12` comfortably, and neither contradicts the truth. Same method caveat as
§4 item 1: directed-rounding intervals, not exact rationals.
