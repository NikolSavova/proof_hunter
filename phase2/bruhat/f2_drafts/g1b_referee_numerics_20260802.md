# Computational audit — `g1_draft_b.md` (G1 closure) — NUMERICS PASS
> Date: 2026-08-02. Auditor: independent agent (Claude Fable 5), separate from the maths referee
> (`g1b_referee_maths_20260802.md`). Task: re-run every shipped script, verify code matches the
> draft's claims, and independently recompute central constants with exact arithmetic.

**Environment note:** `sympy` and `mpmath` were not installed on the audit machine (installs
disallowed). Two scripts therefore could not run as-is; each was replaced by a faithful — in fact
*stronger* (exact-arithmetic) — stdlib reimplementation, stated per-row below. `numpy`/`scipy` present.

## (i) Script-by-script table

| Script | Claim it checks | Ran? | Matches draft? |
|---|---|---|---|
| `g1b_const.py` | Lemma B.0 coefficient bounds: `b·m ∈ [0.0890, 0.0900]`, `g·m² ∈ [0.03540, 0.03674]`, `c8·λ⁻⁴·m³ ≤ 0.0431`, plus sympy root certificates | Numeric half: YES. Sympy half: NO (no sympy) — replaced by exact-integer proof (see iii) | YES: `b·m max 0.090000 / min 0.089057`, `g·m² ∈ [0.035842, 0.036734]`, `c8s·m³ ≤ 0.043080` — all exactly the numbers quoted in NC-B0 |
| `g1b_const2.py` | W/V scaled tables, `C1''`, `KB`, He-sup values, C2-table assembly | YES | YES: `sup e^{-y²/2}\|He6\| = 15.0000`, `\|He8\| = 105.0000`; `C1''(150)=3.7484`, `KB(180)=106.519` (draft rounds to 106.6); W-table coefficients identical to draft §1 table |
| `g1b_final.py` | Pointwise threshold (m ≥ 110) and the final C2 table + measured truth | YES (needed `PYTHONPATH` fix — see ii.3) | YES: `σ·Θ_pt·m³ = 0.3057` at m=110 (draft: ≤ 0.31); `C1''(110)=3.8256` (draft 3.826); C1 total `0.4279 < 0.45`; C2 = **1.073 / 1.564 / 3.023 / 37.601 / 3934.255 / 474.576** vs draft's rounded-up **1.1 / 1.6 / 3.1 / 38 / 3940 / 475**; box/denom/superpoly/Taylor columns all match; measured m=60: 0.527/0.922/7.032/58.848 = draft's column verbatim |
| `g1b_lemA.py` | NC-B1: 60-digit check `\|φ−φ̂\| ≤ e^{-λt²/2}W(t)` on `(0, t₁]` | NO as-is (no mpmath) — reimplemented in stdlib `decimal` at 80-digit precision, same grid | YES: max ratios **0.320103 / 0.399643 / 0.446891 / 0.463897 / 0.477976** at m = 10/20/40/60/100 — draft claims 0.320/0.400/0.447/0.464/0.478, all ≤ 1 |
| `g1b_sym.py` | Lemma B.7: exact monomial table of N(y); b-linear cancellation; b² quartic collapse | NO as-is (no sympy) — reimplemented with exact integer/Fraction polynomial arithmetic from the He-recurrence | YES: **all 10 monomial coefficient vectors match the draft's table exactly**; b-linear term vanishes identically; b² coeff = 16He₃²+12He₂He₄−28He₆ = 240y⁴−1008y²+384 confirmed exactly |
| `g1b_truth.py` | NC-B9/NC-7 ground truth vs exact Mahonian rows; NC-B3 pointwise; float Lemma-A; NC-B5 factorization identity | YES | Mostly YES: NC-B3 `σm³max\|E2\|` = 0.1145/0.1120/0.1109/0.1099 (draft verbatim; bound 4.3, ~39× slack); NC-7 measured −0.1679/−0.1846/−0.1897/−0.1923/−0.1936 vs predicted −0.1751/−0.1867/−0.1903/−0.1923/−0.1932 (draft verbatim, 4-digit agreement by m=50); NC-B5 ratio −5.68e-14 (draft: 5.7e-14). **BUT its "Lemma A" float section fails its own printed criterion** — ratios ~10⁵⁰ against "(must be <= 1)" — see (ii.1) |
| Inline NC-B9 snippet (draft §6) | end-to-end `m²\|E1\|` windows | YES, verbatim | YES: converges to 0.527/0.922/7.032/58.848 at m=60 for y₀=0.5/1/2/3 (draft: ~0.53/0.92/7.0/59) |

Also verified: the `min(2d̄+d̄², 0.5)` denominator cap never engages (d̄ ≤ 6.9e-5 at every table
row, consistent with the draft's "|δ| < 1e-3").

## (ii) Discrepancies between code and draft (all minor; none affects a proved constant)

1. **`g1b_truth.py` ships a failing check.** Its "Lemma A" section prints ratios like `6.09e51 (must be <= 1)` at m=20/40/60. This is the double-float roundoff artifact the draft itself disclaims in NC-B1 ("a double-float check is meaningless here"), and the real check (`g1b_lemA.py`, 60-digit) passes — but the script gives no in-file warning, so a naive re-runner sees a blatant FAIL. Add a warning or remove the section.
2. **C2-table column mislabeled.** The draft column headed "`m² sup N/P²`" (0.284/0.575/1.010/7.156/56.5/55.4) is actually `A2N/P_min` (ONE power of P); the quantity actually entering C2 in the code is `A2N/P_min²` (= 57.2 at y₀=3, m₁=230). The C2 totals are computed with the correct two powers, so this is display-only (~1% at y₀≤2).
3. **Hardcoded collaborator path.** `g1b_truth.py` and `g1b_final.py` do `sys.path.insert(0, "/Users/sihaohuang/Desktop/Coding/proof_hunter/phase2/bruhat")` — they do not run on other machines without an external `PYTHONPATH` pointing at the real `mahonian.py`.
4. **Measured entry for y₀=0.1.** Draft's "0.194 (center)" is the center-point value; the actual window sup over |y| ≤ 0.1 at m=60 is **0.206** (verbatim NC-B9 rerun). Labeled "(center)" so arguably honest; both ≪ C2 = 1.1.
5. **Dead code:** `g1b_const2.py` line 83 is garbled but immediately overwritten by the correct line 84 — harmless.
6. Rounding of C2 at (3.0, 230): computed 3934.3, draft states 3940 — a safe over-round (fine for an upper bound); similarly 37.601 → 38.

## (iii) Independent spot-checks (fresh code, exact arithmetic, scratchpad only — not in repo)

1. **Cumulants from the Mahonian generating function** (exact `Fraction` arithmetic, m = 6, 10, 20, 35): κ₂ = m(m−1)(2m+5)/72 **exactly**; κ₄ = −(S₄−m)/120 **exactly**; κ₆ = (S₆−m)/252 **exactly** — so β = −κ₄/24 = (S₄−m)/2880 and γ = κ₆/720 = (S₆−m)/181440 as the draft defines. B_m·m inside the claimed [1.068, 1.080].
2. **Lemma B.0 certificates, exact-integer proof** (stronger than the draft's numeric root certificates): each inequality converted to an integer polynomial, checked exactly at every integer from the threshold up to the coefficient-dominance bound (up to m = 445,455 for the g-upper bound), with strict positivity beyond by dominance. **All five hold for all m ≥ threshold.** Below-threshold failure sets ({2..10}, {18..25}, {2..6}, ∅, {2..29}) corroborate the claimed largest roots 10.095 / 25.669 / 6.874 / 1.000 / 29.884. Bonus: b·m < 0.09 strictly with sup attained only as m→∞ (the 0.0900 bound is sharp); g·m² → 0.0367347; c8s·m³ max = 0.043080 at m=30.
3. **Exact N(y) table** (independent of sympy): full match, b-linear cancellation, quartic collapse — as in (i).
4. **Asymptotic center coefficient:** m²(−90g+384b²) → **−0.19572**, confirming the draft's "−0.195/m²" derivation of the NC-7 calibration −0.19/m².

## (iv) Verdict

**NUMERICS CONFIRMED (with caveats).** Every checkable numerical claim in the draft — Lemma B.0
bounds, the NC-B1 ratio table, C1'' = 3.826 and the m ≥ 110 pointwise constants (0.4279 < 0.45,
4.13 < 4.3), the exact N(y) monomial table with both structural cancellations, the full C2 table
(columns and totals), the measured ground-truth values, and the exact m⁻² center coefficient
−90g+384b² ≈ −0.1957/m² — reproduces on re-run or under independent exact recomputation.
Caveats: (1) `g1b_truth.py`'s float Lemma-A section fails as printed (known artifact, disclaimed
in the draft — should carry an in-script warning or be removed); (2) the C2 table's "m² sup N/P²"
column shows A2N/P_min instead of the A2N/P_min² actually used (display-only, ~1%); (3) two
scripts need sympy/mpmath and two hardcode an absolute path — the shipped verification suite is
not reproducible as-is on other machines; (4) the draft's own caveat stands: the window law is
proved only for m ≥ m₁(y₀) ≥ 180 while the exact harness covers m ≤ 150, leaving the
150 < m < m₁ band to the planned harness extension.
