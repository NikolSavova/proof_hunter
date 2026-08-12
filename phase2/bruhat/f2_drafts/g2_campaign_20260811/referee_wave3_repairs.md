# referee_wave3_repairs — single-verifier pass on `wave3_repairs_20260812.md` (2026-08-12)

*Verifier report on `wave3_repairs_20260812.md` (the wave-4 housekeeping file
applying the STATUS_wave3 §2a/§2b repair lists plus the harness C5 scope
erratum). Single-verifier class, mirroring `referee_repairs_20260811.md` and
`referee_wave2_repairs.md`, per STATUS_wave4 §3 item 3 / §5 item 4. Protocol:
re-run every script under `g2_scripts/campaign_20260811/wave3_repairs/` and
diff against the archived outputs; trace every erratum to (i) the defective
display in its host file, (ii) the referee finding it discharges, and
(iii) the script or archived output certifying every numeric claim; verify
the two mathematical items (MR-1, MR-2/N-F2) independently with different
machinery; confirm the §D no-drift claim by source-level diff of the two
"fixed copy" scripts against their originals. `g2_draft_t1_20260803.md` not
read. No existing file modified; this file is new.*

**VERDICT: SURVIVES.** The mandate is fully discharged: every item of
STATUS_wave3 §2a (1–8) and §2b (1–7), plus the C5 erratum, is applied,
correctly attributed, and certified; all three scripts re-run
**byte-identical** to their archives; the two content repairs (B1 = MR-1,
B2 = MR-2/N-F2) are independently re-proved here (B2 by strictly weaker,
elementary machinery — the certificate is even more robust than claimed);
the no-drift claim is verified at source level — no certified constant,
threshold, scope, or verdict moves. Findings V-F1–V-F3 are record-only
trivia; none forces a text change in `wave3_repairs_20260812.md` itself.

## 1. Script re-runs (all three: byte-identical)

Re-run 2026-08-12 from a clean scratch directory
(`python3`, absolute paths into
`g2_scripts/campaign_20260811/wave3_repairs/`), then `diff` against the
archived `out_*.txt`:

| script | exit | diff vs archive |
|---|---|---|
| `w3r_mr12_checks.py` | 0 | **BYTE-IDENTICAL** |
| `w3r_f1_sl5_nc1_fixed.py` | 0 | **BYTE-IDENTICAL** |
| `w3r_f1_wp4asm_fixed.py` | 0 | **BYTE-IDENTICAL** |

Every displayed block in `wave3_repairs_20260812.md` (§A2, §A5 both row
blocks, §B1, §B2, §C, §B5) was checked verbatim against the corresponding
archived output: **all match byte-for-byte** (including the four quoted
assembler rows W2/W3/W7 + headline, the SL5 W1 row + two tail lines, and
the `[R2 repair check]` line).

## 2. Fixed-copy audit (§A5's "arithmetic identical" claim) — VERIFIED

Source-level `diff` of the fixed copies against their originals:

- `w3r_f1_sl5_nc1_fixed.py` vs `wp4_SL5/sl5_nc1_ledger_exact.py`: the only
  executable changes are (i) new `ceil_p`/`floor_p` display helpers,
  (ii) `float(...)` -> `ceil_p(...)`/`floor_p(...)` in the three print
  slots (`I1u<=`, `total<=`, `margin>=`), (iii) capture + 5/7-digit floor
  print of the W1 margin, (iv) original sections [2]–[5] dropped (not part
  of finding F1; documented in the header). All band constants, `exp_lower`
  (N = 120), `sqrt_upper`, the row formula, and the exact-Fraction
  PASS comparisons are identical.
- `w3r_f1_wp4asm_fixed.py` vs `wp4_assembly/wp4asm_chain.py`: identical
  arithmetic for tables [1]/[2]/[3] and [1b] (`exp_lb` N = 140,
  `sqrt_ub`/`sqrt_lbv` digits = 8, `r5_ub` — two DEAD lines `lo, hi` /
  `r = F(1)` deleted, provably without effect since `r` was immediately
  reassigned); display-only ceil/floor changes; per-row W1-margin floor
  print and the `[R2 repair check]` block added; the float-labeled
  ESTIMATES block [4] dropped (documented, not proof-bearing).

**Old->new cell map verified against the ORIGINAL archives**
(`out_sl5_nc1.txt`, `out_wp4asm_chain.txt`): every one of the 8 + 12
repaired cells listed in §A5 matches (assembler: W2 `4.4335->4.4336`, W3
`4.8790->4.8791`, W7 `8.8231->8.8232` + margins; W1/W4/W5/W6b confirmed
unchanged; SL5: totals W1/W3/W4/W7, margins W1/W3/W4/W7, I1u W1/W3/W4/W7
all as listed). The three exact effective-C* fractions
(`4734473/280000`, `458360713/28000000`, `201619/20000`) and the D1 delta
`+0.000634` appear unchanged in both original and fixed outputs — the §D
no-drift claim is TRUE. Independent mpmath (dps 50) cross-check of the SL5
W1 row: true `I1u = 1.0118383...`, true total `4.7338042...`, true margin
`0.86619576...` — the ceil prints `1.0119`/`4.7339` sit above the script's
certified upper bounds and the floor print `0.86615` below the certified
margin: directions correct.

## 3. Item-by-item application audit (nothing skipped, nothing uncertified)

### §2a (composite list, items 1–8 -> A1–A8): ALL APPLIED

| item | erratum | defective display located in host | certification | verdict |
|---|---|---|---|---|
| 1 (R1) | A1 scope note `(4/m, 0.89]` | composite lines 240–242 (statement as quoted) | text-level; content matches `referee_maths_wp4.md` R1 | APPLIED |
| 2 (R2) | A2 `10.08 -> 10.081` | composite line 495 `10.08 <= 136` | `w3r_f1_wp4asm_fixed.py` `[R2 repair check]`: exact `201619/20000`, ceil display `10.081` — re-run identical | APPLIED |
| 3 (R3) | A3 re-point mirror step | composite line 247 `— §0 frame` | target verified: `wp4_sl_SL2.md` Lemma SL2.1 proves `h` even (§5.3 route) | APPLIED |
| 4 (R4) | A4 qualify truth support + fold F3 | composite line 470 (NC-PL3 `1.1696/1.1710`) | REF-B numbers verified in `referee_numerics_wp4.md` (260 adversarial `k`, 0 violations, 17.1x, its §-B verbatim block) | APPLIED |
| 5 (F1) | A5 ceil/floor reprints | original archives show the nearest-rounded cells exactly as claimed | two fixed scripts, byte-identical re-runs; §2 above | APPLIED |
| 6 (F2) | A6 corrected headroom sentence | composite line 334 `8–23% headroom` | quoted lines verified verbatim at `referee_numerics_wp4_scripts/out_ref_nw4_c.txt` lines 26–27 (`R31 = 2.1215`, `R42 = 6.3552`, limits `2.1303/6.4113`) | APPLIED |
| 7 (F4) | A7 `0.0083 -> 0.0065` | composite lines 335/391/425 | verified at `wp4_plan/out_wp4plan_nc4.txt` line 4: `w=     5: C5(0.5lam)= 0.0065` | APPLIED |
| 8 (F6) | A8 `1.2568e-7 -> 1.2569e-7` | `wp4_sl_SL3.md` line 457 | verified at `out_ref_nw4_a.txt` line 25: `P3(401) <= 1.3e-7 = 1.25687e-7` (nearest 4-digit print is 1.2569e-7) | APPLIED |

F3/F5/F7 record-only entries present as required (F3 folded into A4; F5's
`gamma = 1/8` no-relitigation note recorded; F7 floor confirmed fine).

### §2b (assembly list, items 1–7 -> B1–B6) + §C: ALL APPLIED

- **item 1 = B1 (MR-1, content).** Defective displays located (assembly
  lines 174/294–296/311: exact scan to 2000/3001 + unproved monotonicity
  appeal). Transcribed fix matches `referee_checks_theoremA.py` archived
  output section (3) to every digit (`0.009575/0.009571` grid,
  `0.009556/0.009551` closed, "g term-by-term increasing: True").
  **Independent logic audit (this verifier):** `bracket(m) = 6.85*E4*(1 -
  17 B_m - C_A/m^2) - B_m` has `B_m` entering with negative coefficient in
  both occurrences, so substituting the B.0(ii) upper bound `B_m <=
  1.080/m` (valid `m >= 30 <= 401`) yields a genuine lower bound `g(m)`;
  `g` is a constant minus positive multiples of `1/m` and `1/m^2`, hence
  increasing — the "no scan" conclusion is sound. Constants verified
  against the assembly's ledger (`E(4) >= .00248992` line 441, safe
  direction; `C_A` grid `37815.3642` / closed `37997.8442` lines 309–310;
  `18.36 = 17*1.080` exact). DISCHARGED.
- **items 2 + 5 = B2 (MR-2/N-F2, content; the proof-grade upgrade).**
  **Independently re-proved here with weaker machinery:** (i) the
  numerator identity `q(m) = N(m)/D(m)` with
  `N(m) = 4m^4 + 2568m^3 + 2635m^2 - 6582m + 1375`,
  `D(m) = 100 m^2(m-1)^2(2m+5)^2` verified by exact Fraction
  cross-multiplication at 62 values of `m` (2..59, 401, 2000, 1e5, 1e6):
  all equal; (ii) positivity WITHOUT sympy: the quadratic part
  `2635m^2 - 6582m + 1375` has vertex `6582/5270 = 1.249 < 3` and value
  `5344 > 0` at `m = 3`, so `N(m) > 0` for ALL `m >= 3` elementarily — the
  sympy zero-root-count on `[30, oo)` is therefore correct a fortiori;
  (iii) `q(30) = 515527/2205450000` reproduced exactly; (iv) honesty:
  `d(10^7) = 0.5399994`, `|d(10^7) - 27/50| < 1e-6`, and `d(m) < 0.55` at
  35 test points — the exact limit `27/50` stands. The lower side
  `B_m <= (27/25)/m` re-verified exactly at 94 values `m >= 30`.
  DISCHARGED, proof-grade confirmed.
- **item 3 = B3 (MR-3/N-F1).** Defective label located (assembly line 302
  "Verbatim script output"); the relabel's archive pointer
  `theoremA_assembly/out_assembly_checks.txt` EXISTS on disk. APPLIED.
- **item 4 = B4 (MR-4).** Defective display located (assembly lines
  186–187 `1.1 <= C_A` via B.8/Cor B.9); replacement is the referee's
  clean route (`e^x - 1 >= x` at `x = log r`, no linearization, no Bona),
  stated with the alternative reading — matches
  `referee_maths_theoremA.md` §6 MR-4. APPLIED (text-level).
- **item 6 = B5 (N-F3).** Defective display located (assembly line 258
  "6.7x"). Ratios recomputed from scratch by this verifier:
  `(20/79.5)/0.0385 = 6.5343 -> 6.5x`, `eps*/0.0385 = 6.7103 -> 6.7x`
  with `eps* = 1291739/5000000` traced to assembly line 320 and both
  theoremA referees. APPLIED.
- **item 7 = B6 (O1/O3).** O1 recorded correctly (and its statement that
  the wave2_repairs referee pass was "still owed" was accurate at filing
  time; it has since landed as `referee_wave2_repairs.md` — no text change
  needed, the file explicitly says it does NOT discharge that debt). O3
  discharged as §C. APPLIED.
- **§C (C5 erratum).** The defective display located
  (`harness_m200_20260811.md` §3: header `4 <= m <= 400`, C5 listed with
  no exemption). `run_m200.py` line 106 verified verbatim: `if m == 4:
  # m=4 predates the sharp bound's range (5 <= m); record only`.
  **Independent Mahonian rebuild by this verifier** (polynomial-product
  route `prod_{j<=m}(1 + q + ... + q^{j-1})`, different from both the
  harness's and the script's convolutions): `varfit(4) = 91/108 <
  187/216`, `varfit(5) = 7/8 > 187/216`, `varfit(6) = 187/216` exactly —
  the bound is genuinely false at `m = 4`, the rescope to `5 <= m` is
  correct and necessary. APPLIED.

**Coverage:** 8/8 §2a items, 7/7 §2b items, 1/1 §C. Nothing skipped; no
numeric claim in the file lacks a saved+run script or a verified archived
source. The §D inventory (3 scripts) matches the directory exactly.

## 4. Findings (all record-only; none forces a repair)

- **V-F1 (trivia, endpoint of a quoted interval).** §B2 says the measured
  `d(m)` values "match the referee scans — ... numerics referee's
  `(0.34, 0.54]` class on `[30, 2000]`". The file's own (correct) value
  `d(30) = 0.3396` lies just BELOW that interval's lower endpoint. The
  defect originates in `referee_numerics_theoremA.md` line 76 (its
  `(0.34, ...` should be `(0.33, ...` or `[0.3396, ...`), not in
  wave3_repairs; the maths referee's `[0.524, 0.540]` on `[401, 10^5]`
  matches exactly, and the certificate `0 <= d(m) <= 0.55` is unaffected.
  Optional one-word softening ("consistent with") if the file is ever
  errata'd; NO action required.
- **V-F2 (positive observation).** The §B2 certificate is over-engineered
  in the harmless direction: `N(m) > 0` for all `m >= 3` by elementary
  quadratic comparison (§3 above), so the statement does not even depend
  on the sympy root-count machinery — the certificate class could be
  stated as fully elementary. Record for the paper-assembly pass.
- **V-F3 (trivia).** §A7 cites `out_wp4plan_nc4.txt` "line 4"; verified —
  the `w= 5` row is indeed physical line 4. §A6's two quoted lines are at
  physical lines 26–27 of `out_ref_nw4_c.txt` (the file quotes them
  without line numbers; verbatim match). No action.

## 5. Standing after this report

`wave3_repairs_20260812.md` moves from ZERO referees to
**single-verifier SURVIVES** — the same certification class as
`repairs_20260811.md` (+ `referee_repairs_20260811.md`) and
`wave2_repairs_20260811.md` (+ `referee_wave2_repairs.md`). Consequences
for the STATUS_wave4 ledger: §1 row 6's "ZERO referees" is discharged;
§3 item 3 and §5 item 4 (referee this file) are DONE; the citability note
in §1 ("NOT citable: ... `wave3_repairs_20260812.md` (zero referees)")
lifts for this file — MR-1's all-`m >= 401` bracket positivity and the
proof-grade `C_A + 0.55` recentring certificate are now citable through
`wave3_repairs_20260812.md` + this report. Nothing here changes CL's
status: CL(79, 20, 0.89) remains OPEN (residual scope `m >= 561` per
STATUS_wave4), and Theorem A remains PROVED CONDITIONAL on exactly CL.

*End of referee_wave3_repairs.md.*
