# referee_numerics_wave5_sl4pe — adversarial numerics referee report

*Target: `wave5_sl4pe_20260812.md` (hypothesis SL4'-E of the CL bridge —
Theorem E pricing machinery at `m >= 561`, Prop E.3 interface delta, Lemma
E.4, hypothesis (E3)). Referee mandate: maximal bar, DEFAULT TO REFUTATION —
this chain feeds the flip of the paper's main conjecture to a theorem.
Method: re-run EVERY script under `g2_scripts/campaign_20260811/wave5_sl4pe/`
byte-diffed against archived outputs; independent exact-rational
recertification of Lemma E.2 written from the DRAFT TEXT (not the prover's
code); end-to-end corner/random falsification attack on Theorem E;
truth-side reproduction by a genuinely different cumulant route (direct
tilted-uniform moment sums vs the prover's closed-form `phi_n` identities);
62 adversarial off-grid probes at band edges and near `m = 561`; Lemma E.4
re-certified at dps 60 / K = 1200 (vs the prover's 30/300). Referee scripts
+ archived outputs: `g2_scripts/campaign_20260811/referee_wave5_sl4pe/`
(`ref_e_r1` … `ref_e_r6`, `out_ref_e_r1.txt` … `out_ref_e_r6.txt`,
`rerun_e1/e2/e3.txt`). Files read: the target, `STATUS_wave4.md`,
`wave4_sl4p_20260812.md`, `referee_numerics_wave4_sl4p.md`,
`wp4_draft_composite.md` (§5.3 display + [A2] constants), the archived
`wave4_sl4p/out_sl4p_nc2.txt` + `sl4p_nc2_eta.py`. NOT read:
`g2_draft_t1_20260803.md`. No existing file modified. 2026-08-12.*

**VERDICT: MINOR_REPAIRS.** Every load-bearing number in the draft is
genuine, reproduces byte-identically, and survived independent
re-derivation by different machinery: the seven exact-rational `J0(W)`
fractions match my from-scratch recertification EXACTLY; Theorem E survived
a 1764-case hypothesis-boundary attack with zero violations; Prop E.3's
non-derivability witness point is real (independently: ratio `1.4298825`);
the truth-side table reproduces through direct moment sums to `5e-38`; all
62 off-grid probes PASS; Lemma E.4's point values are correct to every
quoted digit at 2x precision and 4x series depth, and its tail bound is
valid (actual tail `3.05e-516` vs claimed `< 6.08e-516`). NOTHING
FABRICATED; nothing refuted. Four findings, all commentary/label-level
(§7): the roadmap's "limit-vs-561 gap `<= 5e-4`" is band-edge-dependent
(true W1–W4, `6.5e-4` at W5's edge, `2.2e-3` at W6b's edge); the §3
"30x–100x"/"100x–1000x" ratio sentence is imprecise in both halves; the §8
"rounded in the safe direction" claim about e2's float copies is not
literally satisfiable and factually mixed; a "(+ exact fractions)" label
overstates what script [1] archives (J0 yes, REM* only implicitly). No
certified constant, no theorem statement, no margin, and no verdict moves.

## 1. Re-runs: all three scripts byte-identical

Each script re-run 2026-08-12 and diffed against its archived output:

```
e1_pricing_certificate.py -> rerun_e1.txt : E1_BYTE_IDENTICAL
e2_truth_margins.py       -> rerun_e2.txt : E2_BYTE_IDENTICAL  (1.0 s)
e3_limit_sign.py          -> rerun_e3.txt : E3_BYTE_IDENTICAL  (2.1 s)
```

So every verbatim quote in the draft's §3, §5, §6 and script table §8 is
covered by a reproducible archived output. Spot-audit of the quotes against
the outputs: the `REM*(W)`/`J0(W)` rows, `identity holds at all exact
rational tuples: True`, per-band `upper-side ... True positivity ... True`,
`ALL checks PASS at m = 561: True; worst pricing ratio = 0.6576`, the worst
`J/J0` row (0.6740/0.4991/0.3470/0.2853/0.2297/0.2203/0.2885), the Prop E.3
line (`eta/u = -1.000964 price = 0.700032 ratio = 1.4299`), the block [E]/[F]
lines, and all Lemma E.4 values — ALL match verbatim. The probe count "27"
is correct (counted). The block [A] guard values (`0.4503/0.6432` at
`(401, 4.9)`, `0.9285/0.1804` at `(401, 356.8)`) match the archived wave-4
`out_sl4p_nc2.txt` lines 4/13 verbatim, and e2's `qhat`/`eta` formulas match
`sl4p_nc2_eta.py`'s byte-for-byte in substance (checked side by side).

## 2. Independent exact recertification of Lemma E.2 (`ref_e_r1`)

Rewritten from the draft's Lemma E.2 Steps 0–5 text alone, in `Fraction`
arithmetic. Result: **all seven exact `J0(W)` fractions EQUAL the archived
e1 output's fractions** (`J0 == archived fraction: True` per band), all
seven `REM* <= 0.3 R31*^2` checks and all positivity checks re-verified,
and `R42+ = 2J* > R42*` on every band (so Step 0's two-sided cap is the
binding one, as the certificate assumes). Exact values to 12 digits:

```
REM* = 0.017058068129 / 0.029318577604 / 0.059379577439 / 0.080548451464
       / 0.132066143949 / 0.144939416193 / 0.156030179162
J0   = 0.682941931871 / 1.102681422396 / 1.915620422561 / 2.536451548536
       / 3.667933856051 / 4.178060583807 / 4.595969820838
```

The draft's 6-sig-fig displays are correct roundings of these. I also
hand-re-derived every interval bound in Steps 0–5 (the `h`-caps at
`eps2 <= E0 = 0.00705...`, the `C_b`/`C_a` endpoint products, the
`M0cap`/`Mdev` split, the `rho1` ratio-test bound, and the e^x <= 1/(1-x)
use at `x = E0 < 1`): each is a valid monotone interval bound; the single
worst-case evaluation at `(A0(W), E0, Lam(W))` covers all `m >= 561`
because each constant is monotone in its argument in the stated direction.
The Lemma E.1(ii) identity was additionally hand-checked symbolically
(factor `N^2-(1+x)^2`, substitute `c6 = a^2/2`) — it is exact, and §3
below confirms it against direct `qhat` evaluation at 1764 points.

## 3. End-to-end falsification attack on Theorem E (`ref_e_r2`)

For every band, `m in {561, 562, 600, 5000}`, three `w` per band (micro
left edge, interior, right edge), three `A`-levels (floor, 10x, 10^4x):
corners engineered ON the hypothesis boundaries — C1 `(r31^2, r42) =
(R31*^2, 2(R31*^2 - J0))` [(E3) tight from the `r31` side; (E2) verified
satisfiable: `2(R31*^2 - J0) <= R42*` on every band], C2 `(0, -2 J0)`
[(E3) tight, most-negative `r42`], C3 `(0, R42*)` [(E2) tight], C4
`(R31*^2, R42*)` [(E1)+(E2) jointly tight], plus 3 random interior draws
per cell; `eta` computed at dps 60 from the closed forms directly
(independent `qhat` code) AND from the Lemma E.1 algebraic form:

```
cases run: 1764;  VIOLATIONS: 0
worst envelope fraction |eta/u - main|/REM* = 0.117173
worst pricing ratio |eta|/(price u)         = 0.976621
worst E.1(i)-vs-direct eta relative gap     = 9.936e-48
```

Verdict of the attack: **the pricing inequality holds at every
hypothesis-consistent point probed, including corners where it is genuinely
close (0.9766 at an engineered C2-type corner)**; the certified envelope is
~8.5x conservative even at its worst probed corner (expected: the
certificate's `(eps2, A)` extreme corner is not jointly realizable in-band,
which costs slack but never validity); and the exact identity behind
E.1(i)/(iii) holds to 1e-47. Prop E.3's witness reproduces independently
at dps 60: `eta/u = -1.0009637308` (both routes agree), `price =
0.700032171`, ratio `= 1.4298825` — and the point satisfies (E-A2)
(`A = 157.08 = 0.28*561` exactly at the floor, `s2 = 2.4413e6 >= S0`),
(E1) with equality, (E2), and `kappa_4 = 0 >= 0`. **The delta flag is
genuine: the recorded interface provably does not imply the pricing.**

## 4. Truth-side reproduction by a different route (`ref_e_r3`)

Cumulants recomputed by DIRECT tilted-uniform central-moment sums (weights
by iterated multiplication, dps 40) — sharing no code path with e2's
closed-form `phi_n` route — at 8 load-bearing points. Every draft/e2
number reproduces; max relative gap between the two routes over all points
and all three cumulants: **5.11e-38**. Key rows (direct route):

```
m=561 w=5.0    [W1]: r31=0.8864 r42=0.6506 J=0.4603 ratio=0.6576 REMact=9.87e-05
m=561 w=499.29 [W7]: r31=2.1240 r42=6.3713 J=1.3258 ratio=0.1808 REMact=9.59e-04
m=401 w=4.9    [W1]: |eta|/u=0.4503 ratio=0.6432   (archived nc2 guard: match)
m=1000 w=890   [W7]: J=1.3288                       (draft item 2: match)
```

All J <= J0 (exact-12-digit), all ratios <= 1, all REMact <= REM*, all
`k4 > 0`. The draft's W1-right-edge anchor numbers — `r31^2 = 0.7857 >
0.7 = J*(W1)`, rescued by `r42 = 0.6506` to `J = 0.4603 <= 0.6829` — are
confirmed truth.

## 5. Adversarial off-grid probes (`ref_e_r4`): 62 points, 0 FAILs

Points the prover did not run, chosen at the structure's weak spots
(phi route, cross-validated in §4; dps 40; per-point checks: exact-12-digit
`J <= J0`, ratio <= 1, `REMact <= REM*`, `r31 <= R31*`, `r42 <= R42*`,
`k4 > 0`):

- **m-direction, W1 right edge `w = 5.0`** — `m = 561..571` step 1, then
  600/700/1000/2000/20000/100000: `J(w=5.0)` NONINCREASING in `m` over the
  whole scan (confirms the draft's "m = 561 is the measured worst case";
  `J` runs 0.460318 -> 0.459846, all `J/J0 = 0.674...`, ratio 0.6576 ->
  0.6569). Same at the W2 edge `w = 6.0` (`m` = 561..5000, nonincreasing).
- **Deep-tilt corner `lam = 0.89` exactly** — `m = 561, 562, 563, 577,
  601, 700, 1077, 2000, 10000`: `J` INCREASES slowly (1.325832 ->
  1.332198), toward the fixed-`lam` geometric limit computed independently:
  `r31_geom = 2.1303061`, `r42_geom = 6.4112558`, `J_geom = 1.332576` —
  matching STATUS_wave4's quoted 2.1303/6.4113 and the draft's "~1.332";
  all far below `J0(W7) = 4.59597` (`J/J0 <= 0.290`).
- **Micro-edges and off-prover interiors** — `w = 4.00001/4.0001` at
  `m = 561/562/600`; `w = 4.95/4.99/4.999` (right-edge approach); the
  half-integer ladder `w = 5.25 ... 450` at the off-prover `m = 563`; full
  edge set at `m = 600`; `m = 100000, w = 5.0`. All PASS; within-band `J`
  increases toward each right edge, as the draft's block [E] locates.

**TOTALS: 62 probes, 0 FAILs.** The binding measured margin of (E3) is
confirmed to be the W1 right edge: worst `J/J0 = 0.6740` (margin 32.6%) at
`(m, w) = (561, 5.0)`, off-grid probes never exceeding it.

## 6. Lemma E.4 and the limit machinery (`ref_e_r5`)

At dps 60, K = 1200 (prover: dps 30, K = 300):

```
G_4(4)     = 0.23234829889039236846   (draft 0.23234829889: all digits correct)
h_4(4)     = 5.4202116963816995327    (draft 5.420211696: correct; < 6)
6 - h_4(4) = 0.579788303618           (draft 0.5798/0.579788: correct)
w*         = 3.36717501284            (draft 3.367175: correct; < 4)
```

Structural checks beyond point values: `G_4(0+) = -4 pi^2 + 24 zeta(2) = 0`
(sanity, 5e-60); `G_4'(w) = 6 - h_4(w)` confirmed by central differences at
`w = 4, 6, 10` to 1e-25; `int_0^4 (6 - h_4) = G_4(4)` to quad tolerance;
the term-wise inequality `x phi_5 - 4 phi_4 = sum k^3 e^{-kx}(kx-4) >= 0`
for `x >= 4` is exact reasoning (every summand nonneg) and `h_4` is
numerically strictly decreasing on [4, 12]. The truncation-tail bound is
VALID and ~2x conservative: actual tail (k = 301..500) `3.05e-516` vs the
claimed `< 6.08e-516`; the `P(y) <= 2 y^4` cap holds from `y = 13.3`
(ratio 0.6898 there) — and `y = kw >= 1204` where used. The Riemann-limit
claims behind E.4(ii) and the §6 roadmap converge at the claimed O(lam)
rate (gaps at `w = 5`: 1.0e-3/1.4e-3/1.9e-3 at `m = 2000` vs
1.0e-4/1.4e-4/2.0e-4 at `m = 20000`, for `G_2/G_3/G_4` respectively). All
six quoted limit-table `J_lim` spot values reproduce
(0.45984/0.54987/0.66427/0.72327/0.84187/0.91841/0.99671), with
`r31_lim = 0.88544`, `r42_lim = 0.64832` at `w = 5` as quoted.

## 7. Findings (all minor; none moves a constant, margin, or verdict)

1. **(F1 — the one consumers should heed)** §6 roadmap bullet 1: "The
   measured limit-vs-561 gap is `<= 5e-4` in `J` (item 2), i.e. two orders
   below the thinnest margin." The `<= 5e-4` holds at the W1–W4 right
   edges but NOT across all of W1–W6b, which is the bullet's stated scope:
   measured `J(561, w) - J_lim(w)` at the six band edges (`ref_e_r6`) is
   `4.75e-4 / 4.52e-4 / 3.55e-4 / 3.14e-4 / 6.46e-4 / 2.18e-3` (W1..W6b) —
   the W6b edge exceeds the claim 4.4x (the gap is O(lam) and `lam` is 8x
   larger there). The CONCLUSION survives everywhere (2.18e-3 is still
   ~3 orders below W6b's `J0 - J = 3.26`, and the binding W1 number is
   correct), but an SL1' prover budgeting a uniform `5e-4` discretization
   allowance off this sentence would be misled on W5/W6b. Repair: restate
   as "`<= 5e-4` on W1–W4 edges; `<= 2.2e-3` across W1–W6b (worst at the
   W6b edge), in all cases orders below the local margin."
2. **(F2)** §3 truth-side-sanity sentence: "the certified envelope is
   100x–1000x looser than truth and still 30x–100x smaller than the
   budgets it must fit under." Measured (`ref_e_r6`): envelope/truth =
   163x–~2.5e4x by band (W6b 2.5e4x, W4 1.4e3x — beyond the stated 1000x;
   direction favorable); envelope/budget = 28.8x–41.0x against the full
   price, or 9.1x–17.6x against the `0.3 R31*^2` slack term the upper side
   actually spends from. Neither reading gives "30x–100x". The certified
   check itself (`REM* <= 0.3 R31*^2`, True per band) is untouched.
   Repair: replace with the measured ranges (one sentence).
3. **(F3)** §8 numeric-integrity note: "[2] carries 6-significant-figure
   float copies of [1]'s REM*/J0 (rounded in the safe direction)". Not
   literally satisfiable and factually mixed: `REMSTAR` enters e2 in two
   checks with OPPOSITE conservative directions (`REMact <= REM*` wants a
   low copy; `J <= J* - REM*` wants a high copy), and the actual copies are
   round-to-nearest — W1–W4 ABOVE exact (by <= 4.9e-8), W5–W7 BELOW exact
   (by <= 4.2e-7) (`ref_e_r1`, per-band directions printed). All deltas
   are >= 4 orders below every margin involved, and [1]'s fractions are
   declared authoritative, so nothing quotable changes. Repair: one
   clause ("round-to-nearest copies, deltas <= 5e-7, immaterial at the
   measured margins; fractions authoritative").
4. **(F4, nano)** Script-table row [1] and §9 say the exact fractions for
   `REM*(W)` and `J0(W)` are archived; `out_e1_pricing_certificate.txt`
   prints exact fractions for `J0` ONLY (line "exact J0: ..."); `REM*` is
   recoverable exactly as `J* - J0` with `J*` trivial, but is not printed
   as a fraction. Repair: one word ("J0 fractions archived; REM* = J* -
   J0"), or reprint.

Checked and NOT findings: the composite §5.3 third-price-term display
(`1/(2 s2)` vs the wave-4 `(lam^2/2) u` bracket form) — the draft's §1
remark correctly reconciles them and proves the form the consumer
(`wave4_sl4p_20260812.md` §3 "main" row) actually uses; the "27 probes"
count (correct); the (E2)-satisfiability of Prop E.3-adjacent corners
(verified: `2(R31*^2 - J0) <= R42*` on every band); the wave-4 referee-F3
cross-quote (`0.6579` at `m = 401` vs `0.6576` at `m = 561`, decreasing —
confirmed and extended to `m = 100000`); the dead-route table (all five
quoted comparisons and the 2.6%–6.5%/0.9% margins recomputed).

## 8. Referee script table (all under `g2_scripts/campaign_20260811/referee_wave5_sl4pe/`, SAVED + RUN 2026-08-12)

| script | what it does | archived output | headline |
|---|---|---|---|
| (re-runs) | byte-diff all three prover scripts | `rerun_e1/e2/e3.txt` | all `*_BYTE_IDENTICAL` |
| `ref_e_r1_exact_recert.py` | Lemma E.2 recertified from draft text, exact `Fraction`; float-copy rounding audit | `out_ref_e_r1.txt` | all 7 `J0` fractions match archived EXACTLY; all checks True; copy directions mixed (F3) |
| `ref_e_r2_envelope_attack.py` | 1764-case hypothesis-boundary corner + random attack, dps 60; E.1 identity cross-check; Prop E.3 point | `out_ref_e_r2.txt` | `VIOLATIONS: 0`; worst ratio 0.976621; identity gap 9.9e-48; E.3 ratio 1.4298825 |
| `ref_e_r3_truth_direct.py` | direct tilted-uniform moment sums (independent route), 8 load-bearing points | `out_ref_e_r3.txt` | all draft numbers reproduce; route gap <= 5.11e-38 |
| `ref_e_r4_offgrid.py` | 62 off-grid probes: m-scans, micro-edges, `lam = 0.89` corners, off-prover m | `out_ref_e_r4.txt` | `62 off-grid probes, 0 FAILs`; monotonicity claims confirmed; `J_geom = 1.332576` |
| `ref_e_r5_e4_limits.py` | Lemma E.4 at dps 60/K=1200; structural identities; tail bound; Riemann rates; limit table | `out_ref_e_r5.txt` | every quoted digit correct; actual tail 3.05e-516 <= bound; `w* = 3.36717501284` |
| `ref_e_r6_gap_audit.py` | quantify the F1 gap claim and F2 ratio sentence | `out_ref_e_r6.txt` | W6b-edge gap 2.18e-3 (F1); price/REM* = 28.8x–41.0x (F2) |

## 9. Verdict and consumer guidance

**MINOR_REPAIRS.** Under a refutation-first mandate I could not break
anything load-bearing: Theorem E's certificate is arithmetically exact and
its interval logic sound (independently re-derived and corner-attacked);
Prop E.3's interface delta is real and exactly as quantified — the
recorded "algebra + sign lemma + SL1'-w(i)" plan is dead, and the ledger
should adopt (E3)/SL4'-E-J as the draft proposes; Lemma E.4 is correct to
every quoted digit with a valid tail bound; hypothesis (E3) is honestly
CONJECTURED with its worst measured margin (32.6% at `(561, 5.0)`)
confirmed binding under 62 additional adversarial probes. The four repairs
(§7) are text-level; F1 is the only one a downstream prover could be
misled by and should be applied before the SL1' deliverable budgets off
this file. The draft's own PARTIAL status line (machinery PROVED / (E3)
CONJECTURED / delta flagged) is an accurate self-report. A maths referee
is still owed under the house two-referee rule.

*End of referee_numerics_wave5_sl4pe.md.*
