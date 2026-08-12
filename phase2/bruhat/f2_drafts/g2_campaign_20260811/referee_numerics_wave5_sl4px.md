# referee_numerics_wave5_sl4px — adversarial numerics referee report on `wave5_sl4px_20260812.md`

*Wave-5 referee pass, F2 campaign, 2026-08-12. Target:
`wave5_sl4px_20260812.md` (hypothesis SL4'-X, W1 crossover monotonicity,
claimed PROVED) and its script
`g2_scripts/campaign_20260811/wave5_sl4px/x_constants_and_scan.py`
(`out_x_constants_and_scan.txt`). Protocol: maximal bar, DEFAULT TO
REFUTATION (this chain flips the paper's main conjecture to a theorem).
The prover script re-run and diffed byte-for-byte; every constant
re-derived in EXACT rational arithmetic where rational and at dps 80 with
log/asin-free sign-safe reformulations where transcendental; every printed
block-[B] value rebuilt string-identical from an independent code path
(factored form `x = P g`, analytic derivative in place of `mp.diff`);
adversarial off-grid probes at the box corners (including the TRUE extreme
corner `w = 4, lam = 0.89` — absent from the prover's own table), at
`m = 560/561/562`, at `tau = 0.8 + 1e-12` and `1.074 - 1e-12`, and on 3000
random draws with `lam` down to `1e-9` and `m` up to `1e9`. Consumer-side
claims verified against `wave4_sl4p/sl4p_nc1_ledger.py` source and archived
output, and against the wave-4 referee's archived `[A2]` block. Blind
protocol kept (no other wave-5 draft read; `g2_draft_t1_20260803.md` not
read). New referee scripts (all SAVED and RUN, outputs archived beside
them) in `g2_scripts/campaign_20260811/referee_wave5_sl4px/`:
`ref_x5_a_exact.py`, `ref_x5_b_lemmas.py`, `ref_x5_c_scan_rebuild.py`,
`ref_x5_d_consumer.py` (outputs `out_ref_x5_{a,b,c,d}.txt`). No existing
file modified.*

## VERDICT: **SURVIVES**

**Nothing fabricated, nothing wrong of substance, nothing load-bearing to
repair.** The prover script re-runs BYTE-IDENTICAL; all six named
constants NX-1..NX-6 survive exact-rational / dps-80 / reformulated
re-derivation with safe-direction roundings confirmed; every one of the 55
printed block-[B] values reproduces string-identically from an independent
implementation; the three lemma mechanisms (M-floor, bracket positivity,
quadratic-root sign) and the derivative identity hold at all 3091
adversarial probe points with ZERO violations — including corners the
prover never probed; Corollaries X.2 and X.3 verify numerically against
`mp.quad` truth and against the consumer ledger's actual source code; the
quoted consumer entry `X = 1.0363` decomposes exactly as claimed. Two
record-only observations (O1, O2, §6) concern the draft's own
"NOT load-bearing" §6 commentary and force no repair before citation.
On this referee's checks, **the status flip SL4'-X: CONJECTURED -> PROVED
is earned** (modulo the maths referee's independent pass on the calculus,
which is not this report's mandate — though every analytic step was also
re-derived here and found correct).

## 1. Reproduction (clean)

`x_constants_and_scan.py` re-run 2026-08-12: `diff` against the archived
`out_x_constants_and_scan.txt` is empty — **BYTE-IDENTICAL**. Every number
quoted in the draft's §5 and §6 appears verbatim in that output; the §5
and §6 blocks are verbatim copies (checked line-by-line). The 8
adversarial `(w, m)` points claimed to be the wave-4 referee's `[A2]` set
are exactly that set (checked against `referee_numerics_wave4_sl4p.md` §3
item 3). The three added corners are as described (`356.89/401 = 0.89`
exactly; `4.0/5 = 0.8`; `5.0/2000000 = 2.5e-6`).

## 2. Named constants NX-1..NX-6: exact and reformulated re-derivation (all clean)

`ref_x5_a_exact.py` (`out_ref_x5_a.txt`), independent code paths:

- **Exact rational** (Fraction, no floats): NX-1a
  (`1074/1000 * 89/100 = 47793/50000`, `y0 = 47793/100000`); NX-1b as an
  exact-rational comparison `1 - y0^2/6 = 19238609717/20000000000 >=
  96193/100000` — TRUE exactly; NX-1c (`192386/100000 >= 19238/10000`
  exact); NX-3a (`f(0.8) = 40/41` exactly, as the draft states; both
  endpoint values exceed `9756/10000` exactly); NX-3b
  (`19238/10000 * 9756/10000 - 1 = 87685928/100000000 = 0.87685928`
  EXACTLY — the printed value is exact, as claimed); NX-4 left side
  (`153904/100000` exact `>= 1539/1000`); NX-6's geometric bound
  (`(445/1000)/(1 - (445/1000)^2/6) <= 4602/10000` exact).
- **Sign-safe transcendental reformulations** (dps 80): NX-2 recast
  log-free as `1.64 >= exp(0.9516/1.9238) = 1.63991762...` — TRUE; NX-4's
  `1.53904 > 1/log 2` recast as `2 > exp(1/1.53904) = 1.91507...` — TRUE;
  NX-5 recast asin-free as `sinh(0.445) = 0.4598329599 <= sin(0.4778855)
  = 0.4599025938` — TRUE (this is exactly `tau0(0.89)/0.89 <= 1.0739`).
- **Digit strings**: every constant printed in block [A]
  (`0.96193048585`, `0.151696630044`, `0.9756097561`, `0.9974571344`,
  `0.87685928`, `1.53904`, `1.442695041`, `1.07372378042`, `0.4598329599`,
  `0.4601881256`) reproduces at dps 80 to the displayed precision.
- **Endpoint-minimum claim** for `2tau/(1+tau^2)` on `[0.8, 1.074]`
  (Lemma X.b's one calculus fact with numeric content): confirmed by the
  derivative sign argument AND a 5001-point dense scan (min
  `0.975609756098`, at `tau = 0.8`).
- **Series-domination** `(2k+1)! >= 6^k` (Cor X.2's induction): verified
  `k = 0..20`; the induction step `(2k+3)(2k+2) >= 6` is trivially sound.
- **Precision robustness**: the tightest margin anywhere in block [A] is
  NX-5's `1.074 - 1.07372378 = 2.76e-4`, then NX-6's `1.19e-5` and
  NX-1b's `4.86e-7` (exact-rational anyway) — all astronomically above
  dps-50 noise. Every rounding direction checked: all safe.

## 3. Adversarial attack on Theorem X.1 / Lemmas X.a–X.c / Cor X.2 (0 violations)

`ref_x5_b_lemmas.py` (`out_ref_x5_b.txt`), dps 60. At every probe point,
ALL of the following were tested as separate inequalities: the Lemma X.a
chain (`M >= 0.96193 (w tau)/2`, `M >= 1.9238 tau`, `M >= 1.53904`); Lemma
X.b's cap `X <= tau^2`, core `psi(tau) > 0`, and conclusion `g > 0`;
Lemma X.c's conclusion `g' > 0` AND mechanism (`Q(h) < 0` and
`h_- < h < h_+` with the exact roots); the factorization identity
`x = P(h) g(h)` (rel. err. `<= 1e-40`); positivity of the ANALYTIC
derivative `(P'g + Pg')(lam/2)cos(y)`; and (at the 91 corner points)
agreement of that analytic derivative with `mp.diff` to rel. `1e-20`.

- **Corner battery** (13 cases x 7 tau values incl. `0.8 + 1e-12`,
  `1.074 - 1e-12`, both exact endpoints): the TRUE extreme corner
  `(w = 4, lam = 0.89, m = 4/0.89)`, `(4.001, lam = 0.89)`, the draft's
  `(4.0, m=5)`, `w = 356.89`, huge-`w` `(m = 1e9, lam = 0.89)`,
  small-`lam` `(m = 1e9, w = 4)`, the CL-relevant edge `m = 561` at
  `w = 4 / 4.001 / 5`, `m = 560/562` at `w -> 4+`, and the ledger points.
  **0 violations.**
- **Random sweep**: 3000 draws, `lam` log-uniform over `[1e-9, 0.89]`
  (clipped mass at `0.89`), `w` log-uniform over `[4, 1e5]` with 10%
  forced `w = 4` exactly, `tau` uniform. **0 violations.** Total probe
  count 3091.
- **Dense strictness scans** (8001 points, off the prover's 2001-grid):
  at the true extreme corner `(4, 0.89)`: min increment `3.83078e-6 > 0`;
  at `(m = 561, w = 4.001)`: min increment `4.3245e-6 > 0`. Strictly
  increasing throughout — the strengthened (strict) claim holds at the
  corners the prover did not print.
- **Cor X.2 audit**: `r(u) = arcsin(sinh u)/u` on a 4001-point grid of
  `(0, 0.445]`: strictly increasing, all values `> 1`,
  `r(0.445) = 1.07372378042 < 1.074`. Matches the draft's NX-5 and the
  monotonicity claim.
- **Record**: the infimum of `M(tau = 0.8)` over the whole box `D` is
  `4 sin(0.356)/0.89 = 1.5664172` (at the true corner) — Lemma X.a's
  floor `1.53904` sits 1.78% below it. The floor is honest and nearly
  tight, as the draft says (see O2 for the wording nit).

## 4. Block [B] independent rebuild (string-identical) and off-grid scan

`ref_x5_c_scan_rebuild.py` (`out_ref_x5_c.txt`), dps 50, written from the
FACTORED form `x = P(h)g(h)` with the analytic derivative replacing
`mp.diff`: all 11 cases x 5 printed values (`min inc`, `min dx/dtau`,
`min x`, `min g`, `M(0.8)`) rebuilt **string-identical to all 55 archived
6-digit values** (this simultaneously validates the prover's `mp.diff`
usage — the analytic derivative agrees to display precision). A
half-cell-SHIFTED 2000-point grid (every point strictly between the
prover's grid points) re-checked strict increase and positivity of `x`
and `g` at all 11 cases: all pass. The draft's `[B]` consistency notes
(i)/(iii) arithmetic checks out (`1.57283/1.53904 = 1.0220` -> "within
2.2%"; `min g`/`min x` positive everywhere).

## 5. Consumer-side verification (ledger `X_w6`, Cor X.3, Remark R3)

`ref_x5_d_consumer.py` (`out_ref_x5_d.txt`), plus source audit of
`wave4_sl4p/sl4p_nc1_ledger.py`:

- **Code-shape claims verbatim**: `w6_x` guards (`return 0` on `M <= 1`;
  `max(val, 0)`) are at lines 52/54 as described; `X_w6` uses uniform
  `n = 60`, `tau0 = 2 asin(sinh(lam/2))/lam`, exponential at the LEFT
  endpoint (`E = m*w6_x(w, a, m)`), weight at the RIGHT endpoint
  (`((a+h)*lam)**2`), cell measure `h*lam` — exactly the two sums
  displayed in Cor X.3. The `mono` flag is precisely "E nondecreasing
  along left endpoints", which Theorem X.1 (via `E = m x` when guards are
  inactive) turns into a theorem.
- **`X = 1.0363` reproduced and decomposed**: `Xn = 1.03249`
  (matches the wave-4 referee's archived `Xn(60)`), `Xd = 0.00385305`,
  `Xn + Xd = 1.0363` — the ledger's printed W1 row entry
  (`X=(inc_X/INFL) = Xn+Xd` per source line 101). The draft's citation
  sentence is exactly right.
- **Cor X.3 against truth**: at `(4.30, 401)`, `(4.001, 462)`,
  `(5.0, 401)`, `(4.001, 561)`, `(4.0, 5)`: `totn(60) >= totn(6000) >=
  integral` and `totd(60) >= totd(6000) >= integral` (integrals by
  `mp.quad` on the unguarded exponent), `mono` True at both resolutions —
  the certified-upper-bound property holds with the partition-refinement
  ordering Cor X.3 predicts, including at the CL-edge `m = 561` and the
  F2 micro-window case `m = 462`.
- **Remark R3 (guards never fire)**: `w6_x == ` unguarded formula at all
  60 left endpoints of 7 cases spanning `w = 4.0..356.89`,
  `m = 5..561` — TRUE everywhere (no hidden flattening).

## 6. Observations (record-only; no repair required before citation)

- **O1 (inherited mis-floor in a quoted wave-4 phrase).** Draft §6 note
  (ii) reports its scan "matches their reported 'minimum increment
  `>= 1.7e-3`'". The scaling arithmetic in the note is exact — my
  recomputation gives prediction `0.001746` vs the wave-4 referee's
  ARCHIVED `min dE = 0.001746` at `(4.05, 401)`, and the same scaling at
  `(4.001, 401)` gives `0.001688` vs archived `0.001688` — a sharper
  match than the draft claims. But the wave-4 REPORT's own phrase
  "`>= 1.7e-3`" mis-floors its own archive (true per-case minima
  `0.001688..0.002653`; `0.001688 < 0.0017`). That is a wave-4-report
  defect, not a wave-5 one; the wave-5 draft quotes it accurately. A
  half-clause ("archive minima 1.688e-3–2.653e-3") would immunize the
  note, and the wave-4 report owes the one-word fix `1.7e-3 -> 1.68e-3`.
- **O2 (wording nit in §6 note (i)).** `(4.0, 5)` is called
  "`lam = 0.8`, the extreme of the theorem's domain". The extreme corner
  of `D` is `lam = 0.89` at `w = 4` (`m = 4/0.89 = 4.4944`), where
  `M(0.8) = 1.56642` — within 1.78% of the floor, tighter than the
  quoted 2.2%. The numbers printed for `(4.0, 5)` are all correct and my
  §3 battery covers the true corner (clean); only the phrase "the
  extreme" overreaches. Cosmetic, in a section the draft itself labels
  NOT load-bearing.

Neither observation touches §0–§5 or §7; no constant, no lemma, no
verdict, and no consumer-facing claim moves.

## 7. Referee script table (all SAVED and RUN 2026-08-12; outputs archived)

| # | script (`g2_scripts/campaign_20260811/referee_wave5_sl4px/`) | what it does | key output |
|---|---|---|---|
| R-A | `ref_x5_a_exact.py` (`out_ref_x5_a.txt`) | NX-1..NX-6 in exact rationals + dps-80 sign-safe reformulations; digit-string checks; endpoint-min scan; series-domination check | `[RA] ALL OK` (18/18 checks; NX-1b exact: `19238609717/20000000000 >= 96193/100000`) |
| R-B | `ref_x5_b_lemmas.py` (`out_ref_x5_b.txt`) | 3091-point adversarial attack on every lemma ingredient + derivative identity; dense 8001-pt strictness scans at the true corner and `m = 561`; Cor X.2 grid audit | `points tested: 3091; violations: 0`; min inc `3.83078e-6` / `4.3245e-6`; `r(0.445) = 1.07372378042 < 1.074` |
| R-C | `ref_x5_c_scan_rebuild.py` (`out_ref_x5_c.txt`) | block-[B] rebuild from the factored form + analytic derivative; string-compare all 55 printed values; half-cell-shifted off-grid scans | all 11 rows `string-match: True`; all off-grid scans pass; `[RC] OVERALL: ALL OK` |
| R-D | `ref_x5_d_consumer.py` (`out_ref_x5_d.txt`) | verbatim `X_w6` reimplementation; `X = 1.0363` decomposition; Cor X.3 vs `mp.quad` truth at 5 cases incl. `m = 561/462`; guard audit; §6(ii) scaling vs wave-4 archive | `Xn+Xd = 1.0363`, `mono = True`; `sum(60) >= sum(6000) >= integral` at all 5 cases; guards never active; scaling predictions `0.001746`/`0.001688` = archived values |

*End of referee_numerics_wave5_sl4px.md.*
