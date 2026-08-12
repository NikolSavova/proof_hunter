# wave3_repairs_20260812 — wave-4 housekeeping: application of the wave-3 repair lists

*Applies EVERY repair in `STATUS_wave3.md` §2a (the `wp4_draft_composite.md`
list, union of `referee_maths_wp4.md` R1–R4 and `referee_numerics_wp4.md`
F1–F7) and §2b (the `theoremA_assembly_20260811.md` list, union of
`referee_maths_theoremA.md` MR-1–MR-4 and `referee_numerics_theoremA.md`
N-F1–N-F3) as errata, plus the harness-report C5 scope erratum (STATUS_wave3
§2b item 7 / assembly §7 item 8), mirroring the format of
`repairs_20260811.md` / `wave2_repairs_20260811.md`. No existing file is
modified (no-erasing rule): each erratum states the defective display in its
host file and the replacement text; the host drafts remain as shipped and
must be read together with this file. New/fixed-copy scripts live in
`g2_scripts/campaign_20260811/wave3_repairs/` (inventory §D), every one
SAVED and RUN 2026-08-12 with output archived beside it (`out_*.txt`). All
new verdict arithmetic is exact integer/Fraction; sympy is used once, for an
exact polynomial real-root certificate (§B2), the same certificate class as
g1_b Lemma B.0(ii).*

*Statuses: every repair here is text/label/rounding-level except the two
with mathematical content — **MR-1** (the R3 `w^2`-bracket positivity beyond
the scanned range) and **MR-2/N-F2** (the `27/25`-form's `O(m^{-2})`
constant) — whose fixes were supplied AND script-verified by the maths
referee (`referee_checks_theoremA.py` sections 3/7); this file transcribes
them and, for MR-2, upgrades the referee's measured certificate to
proof-grade (§B2). Applying everything moves NO certified constant,
threshold, region boundary, PASS/FAIL verdict, or conditional structure
(§D check). CL(79, 20, 0.89) remains OPEN; Theorem A remains PROVED
CONDITIONAL on exactly CL — nothing here changes STATUS_wave3 §3.*

Sources applied: `referee_maths_wp4.md` §2 (R1–R4), `referee_numerics_wp4.md`
§4 (F1–F7), `referee_maths_theoremA.md` §6 (MR-1–MR-4, O1–O3),
`referee_numerics_theoremA.md` §5 (N-F1–N-F3). Item numbering follows
STATUS_wave3's consolidated lists §2a (items 1–8) and §2b (items 1–7).

---

## §A. Composite repairs (STATUS_wave3 §2a, items 1–8) — host `wp4_draft_composite.md`

**A1 [= §2a item 1 = maths R1; the load-bearing scope clarification].**
§3's Theorem CL-composite statement says "`s2 >= 141.749 > 79` for every
such `k`, so this is the full `CL(C_0* = 79, C* = 20, Lambda* = 0.89)` of
`wp3_draft_a2.md` §6.1 — two-sided form, lower-bound form included, both
tilt signs." *Erratum (add the following scope note to §3, and mirror it in
Remark C.3):* "Scope note: the hypothesis band actually delivered is
`|lam(k)| in (4/m, 0.89]` (equivalently `|w| > 4`), matching the plan's
spec block and §6.1's support item 1 (`only 4/m < lam <= 0.89 ever
arises`). wp3-a2 §5's bare parameter form `CL(C_0*, C*, Lambda*)` carries
no `4/m` lower cut; nothing breaks — Theorem S's R2 row, the sole consumer,
is `{k > K_c, |w(k)| > 4}` BY DEFINITION, and `|w| <= 4` is R3's regime,
closed by T.9-final machinery — but no future session may plug a
`|w| <= 4` case into CL-composite." No number moves.

**A2 [= §2a item 2 = maths R2; rounding direction].** §7's "`10.08 <= 136`
at `m >= 1581`" prints the certified UPPER bound `C*_eff` (variant [3])
rounded DOWN. *Erratum:* read "`10.081 <= 136`". The exact certified value
is `201619/20000 = 10.08095`; verified in the fixed-display re-run
(`w3r_f1_wp4asm_fixed.py`, archived output):

```
[R2 repair check] variant [3] exact effective C* = 201619/20000 ; == 201619/20000: True ; CEIL 3-decimal display = 10.081  (composite §7 must print 10.081, not 10.08)
```

§0's "`10.09`" and §4's "`10.0809`" are already safe-direction and stand.

**A3 [= §2a item 3 = maths R3; citation pointer].** §3's proof line
"(mirror: `r(N-k) = r(k)`, `lam(N-k) = -lam(k)`, `s2` invariant — §0
frame; ...)". *Erratum:* the §0 frame merely asserts the convention; the
PROOF of `s2(-lam) = s2(lam)` is SL2 §5.3 (evenness of `h`, via Lemma
SL2.0), imported by Theorem A2(i)'s "for every real `lam`". Read "— Theorem
A2(i)/SL2 §5.3 (evenness of `h`)" in place of "— §0 frame".

**A4 [= §2a item 4 = maths R4; qualifier].** §5's "What is NOT in doubt"
paragraph supports CL's truth only by NC-PL3 at `m = 120/200` (below the
`m >= 401` scope). *Erratum (one qualifying clause):* read "... ground
truth (NC-PL3, deep-band `m = 120/200`): `max eps * min(m, s2) = 1.1696
(m = 120), 1.1710 (m = 200)` vs the asked 20 — a 17x margin; at-scope
support: NC-PL1's `m = 401` budget column, wp3-a2 NC-P3d, and — new,
referee-grade — the numerics referee's exact-integer ground truth AT the
operating threshold (`referee_numerics_wp4.md` REF-B): `m = 401` and
`402`, 260 adversarial `k` at 401, violations all zero, `max eps *
min(m, s2) = 1.17187` vs 20 (17.1x margin, max at `w ~ 4.9`)." This also
records finding F3 (positive observation) as the referee recommends.

**A5 [= §2a item 5 = numerics F1; the recurring ceil/floor display class].**
The `total<=` / `margin` columns of the assembler's table [1] (quoted
verbatim in composite §4 from `out_wp4asm_chain.txt`) and the `total<=` /
`margin>=` / `I1u<=` columns of SL5's NC-SL5-1 table (`out_sl5_nc1.txt`,
quoted in `wp4_sl_SL5.md` §3 and §5, margins re-quoted in its §6) are `%.4f` NEAREST-rounded prints of exact
Fractions; rows W2/W3/W7 (assembler) and W1/W3/W4/W7 (SL5) print certified
upper bounds BELOW (and margins ABOVE) their exact values (worst gap
`< 5e-5`; every PASS/FAIL comparison is exact-Fraction and unaffected).
*Erratum:* those columns are re-printed in ceil/floor direction by the two
FIXED COPIES `w3r_f1_wp4asm_fixed.py` / `w3r_f1_sl5_nc1_fixed.py`
(arithmetic identical, display direction only; outputs archived). The
repaired cells, old -> new:

- assembler table [1] (composite §4): `total<=` W2 `4.4335 -> 4.4336`,
  W3 `4.8790 -> 4.8791`, W7 `8.8231 -> 8.8232`; `margin` W2
  `2.5665 -> 2.5664`, W3 `3.5210 -> 3.5209`, W7 `7.1769 -> 7.1768`.
  (W1/W4/W5/W6b unchanged. The headline `effective C* = 16.9088 (exact
  4734473/280000)` stands via its exact fraction; the safe ceil display is
  `<= 16.9089`.) Verbatim fixed rows:

```
 W2 (5,6]      0.35   140.35  0.700   0.432   1.6207 0.470848 0.200000  1.0     0.01   4.4336    7.00   2.5664 12.6673 PASS
 W3 (6,8]      0.42   168.42  1.300   0.675   1.4795 0.214543 0.200000  1.0     0.01   4.8791    8.40   3.5209 11.6168 PASS
 W7 (40,inf)   0.80   320.80  3.300   1.452   2.8586 0.002532 0.200000  1.0     0.01   8.8232   16.00   7.1768 11.0290 PASS
  all rows PASS: True;  effective C* = max_W T(W)/c_A(W) <= 16.9089 (exact 4734473/280000)  vs budget 20
```

- SL5 NC-SL5-1: `total<=` W1 `4.7338 -> 4.7339`, W3 `4.8789 -> 4.8790`,
  W4 `5.2248 -> 5.2249`, W7 `8.8231 -> 8.8232`; `margin>=` W1
  `0.8662 -> 0.8661`, W3 `3.5211 -> 3.5210`, W4 `5.1752 -> 5.1751`, W7
  `7.1769 -> 7.1768`; `I1u<=` W1 `1.0118 -> 1.0119`, W3 `0.2144 -> 0.2145`,
  W4 `0.0681 -> 0.0682`, W7 `0.0025 -> 0.0026`. Verbatim fixed W1 row:

```
(4,5]      0.28    112.28  0.400    0.300  1.8120  1.0119  0.2  1.0  0.01   4.7339    5.6   0.8661  PASS
all 7 rows PASS (exact Fraction comparison): True
W1 margin, 5-digit FLOOR (text repair '0.8662' ->): 0.86615  (exact value = 0.8661546..., 7-digit floor 0.8661545)
```

- Knock-on text: SL5 §3/§5's "minimal margin 0.8662" and composite §2 R3's
  "worst margin `0.8662 -> 0.8655`" read "`0.86615 -> 0.86552`" (5-digit
  floors; the assembler-side floor is printed by the fixed script:
  `W1 margin, 5-digit FLOOR: 0.86552; exact 865527/1000000 = 0.8655270`).
  The composite's headline `0.8655` was already safe and stands.
- Variants [2]/[3] re-printed the same way (archived): all rows PASS, exact
  effective-C* fractions unchanged (`458360713/28000000`, `201619/20000`).

**A6 [= §2a item 6 = numerics F2; the one substantive item].** §5.1's
(H1) status line "*(plan-level, numerics-verified: NC-PL1 band sups clear
(i) with 8–23% headroom; ...)*" repeats plan NC-PL1's headroom claim,
which is wrong twice: (a) on NC-PL1's own archived grid the W7 headrooms
are already 7.3% (R31) and 6.0% (R42); (b) NC-PL1's `m = 401` grid MISSES
the W7 deep corner — its `w = 356.9` sample has `lam = 0.890025 > 0.89`
and is silently skipped by the band guard. *Erratum:* read "NC-PL1 band
sups clear (i) with 8–23% headroom on W1–W6b only; at the W7 deep corner
`lam -> 0.89` (missed by NC-PL1's own grid) the referee measures
`R31 = 2.1215` vs 2.2 (3.7%) and `R42 = 6.3552` vs 6.6 (3.9%), with
geometric limits `2.1303 / 6.4113` — any wave-4 (SL1') budget must be set
off THESE margins." (H1) is NOT refuted — every measured point clears.
Source (archived, `referee_numerics_wp4_scripts/out_ref_nw4_c.txt`):

```
   lam = 0.89 (w =  356.9): R31 = 2.1215 (vs 2.2), R42 = 6.3552 (vs 6.6)  headroom R42: 3.9%
   geometric limits at lam=0.89: R31_G = 2.1303, R42_G = 6.4113
```

**A7 [= §2a item 7 = numerics F4].** Composite §5.1/§5.2/§5.3 (and plan
NC-PL4 quotes) state the measured `C5` truth range as "`0.0083–0.2104`".
*Erratum:* read "`0.0065–0.2104`" — the archived NC-PL4 output
(`wp4_plan/out_wp4plan_nc4.txt` line 4) contains
`w=     5: C5(0.5lam)= 0.0065`. Safe direction (truth even smaller than
advertised); the SL1' target margins in §5.3 only widen.

**A8 [= §2a item 8 = numerics F6].** SL3 §8's script-table quote
"`P3(401) = 1.2568e-7 <= 1.3e-7`" truncates the archived value; the
nearest print is `1.2569e-7` (referee: `P3(401) <= 1.3e-7 = 1.25687e-7`,
`out_ref_nw4_a.txt` line 25). *Erratum:* keep the certified claim
`<= 1.3e-7`; where a decimal is printed, print `1.2569e-7`.

**Record-only (no text forced; F3/F5/F7):** F3 (the REF-B `m = 401/402`
exact ground truth) is folded into A4 above. F5: the §5.2 refutation
sizing is robust to replacing the orphan's `gamma = 1/8` by the proven
`c1 = 0.1317175` — honest W1 mid entry `101.41` vs slot `1.0125` (REF-C
C7); recorded here so the wave-4 SL4' session does not re-litigate the
`gamma` choice. F7: SL2 §6's "diffs all >= +0.0009" is a floor of the
archived minimum `+0.000907` — fine as stated.

## §B. Assembly repairs (STATUS_wave3 §2b, items 1–7) — host `theoremA_assembly_20260811.md`

**B1 [= §2b item 1 = maths MR-1; the one genuine proof gap — fix supplied
by the referee, verified, transcribed here].** The R3 `w^2`-bracket's
positivity is load-bearing for ALL `m >= 401`, but the assembly displays
only an exact scan on `[401, 2000]` plus a monotonicity appeal that is
itself scan-certified only on `[401, 3001]` (§4 block A3); for `m > 3001`
the claim as displayed has no proof. *Erratum (insert in §2.3's R3 row and
§4 item 4):* "By g1_b Lemma B.0(ii) (`B_m <= 1.080/m` for `m >= 30`,
proof-grade), `bracket(m) >= g(m) := 6.85*E(4)*(1 - 18.36/m - C_A/m^2)
- 1.080/m` (`18.36 = 17*1.080`), which is term-by-term increasing in `m`
and positive at `m = 401`: `g(401) = 0.009571` (grid `C_A`) / `0.009551`
(closed). Hence `bracket(m) > 0` for ALL `m >= 401`, no scan." *Erratum
(§4-A3 and the script block-D parenthetical "monotone increasing to
`6.85 E(4) = 0.017056`"):* beyond the scanned range, "increasing" is
grounded the same way — the B.0(ii) floor `g(m)` increases to
`6.85 E(4)`, and `-> 1` (for the R3 bound) needs only `B_m <= 1.080/m ->
0`; the unproved global `B_m`-monotonicity appeal is dropped. Verification
(`w3r_mr12_checks.py` §(1), archived; matches
`referee_checks_theoremA.py` section 3):

```
   grid  : bracket(401) = 0.009575 ; floor g(401) = 0.009571 > 0: True
   closed: bracket(401) = 0.009556 ; floor g(401) = 0.009551 > 0: True
   spot-verified g(m+1) > g(m) at m in {401, 1000, 5000, 10^5}: True
   => bracket(m) >= g(m) >= g(401) > 0 for ALL m >= 401, no scan (MR-1 discharged).
```

**B2 [= §2b items 2 + 5 = maths MR-2 + numerics N-F2; statement-level
overclaim, fixed in flavor (b) — certificate now PROOF-GRADE].** §0's
Theorem A display attributes the `(27/25)`-centered form's two-sided
`O(m^{-2})` to "the explicit constant `C_A` of §2.4"; but §2.4 proves
`C_A` for the `1 - B_m`-centered form, and recentring `B_m -> (27/25)/m`
costs an extra term with its own `O(m^{-2})` constant, nowhere displayed.
*Erratum (adopting the referee's flavor (b); replaces §0's clause and adds
one sentence to §2.4):* "the two-sided `O(m^{-2})` of the `1 - B_m` form
carries the explicit constant `C_A`; recentring to `1 - (27/25) m^{-1}`
costs at most `0.55/m^2` by the certificate `0 <= (27/25)/m - B_m <=
0.55/m^2` for all `m >= 30` (lower side = B.0(ii); upper side = the
polynomial-root certificate below), so the `(27/25)`-centered form's
two-sided constant is `C_A + 0.55` (absorption: `0.55 + 1.8 << C_A`, per
N-F2)." The upper side is now proof-grade, same class as B.0(ii): with
`q(m) := (11/20)/m^2 - (27/25)/m + B_m = N(m)/D(m)`,
`D(m) = 100 m^2 (m-1)^2 (2m+5)^2 > 0` and
`N(m) = 4m^4 + 2568m^3 + 2635m^2 - 6582m + 1375` has ZERO real roots in
`[30, oo)` (exact sympy root count) and `q(30) = 515527/2205450000 > 0`,
so `q(m) >= 0` for ALL `m >= 30`. The certificate is honest, not padded:
the exact limit of `((27/25)/m - B_m) m^2` is `27/50 = 0.54 < 0.55`.
Verification (`w3r_mr12_checks.py` §(2), archived; measured values match
the referee scans — maths referee section 7's `[0.524, 0.540]` on
`[401, 10^5]`, numerics referee's `(0.34, 0.54]` class on `[30, 2000]`):

```
   N(m) = 4*m**4 + 2568*m**3 + 2635*m**2 - 6582*m + 1375
   real roots of N in [30, oo): 0 (total real roots: 4)
   q(30) = 515527/2205450000 = 2.338e-04 > 0: True
   => N has no sign change on [30, oo) and is positive at 30: q(m) >= 0 for ALL m >= 30: True
     m=    30  d = 0.3396 ... m=100000  d = 0.5399
   exact limit of d(m) as m -> oo: 27/50 = 0.5400  (< 0.55: certificate is honest, not padded)
```

Theorem A's truth was never affected; only the attribution sentence moves.

**B3 [= §2b item 3 = maths MR-3 = numerics N-F1; display label].** §4's
block labeled "Verbatim script output" is a condensed excerpt (~7 archived
lines dropped — all additional PASSes — and rows merged/reflowed).
*Erratum:* relabel "Condensed excerpt; full output archived as
`g2_scripts/campaign_20260811/theoremA_assembly/out_assembly_checks.txt`,
re-run byte-identical by both wave-3 referees." (The established
wp3-a2-F7 repair class; every number shown matches the archive
byte-for-byte.)

**B4 [= §2b item 4 = maths MR-4; one-clause precision].** §2.3's
exact-center note "... B.8/Cor B.9 ... gives the same bound with constant
`1.1 <= C_A`". *Erratum (state the clean route):* "at the center
`s2 = lambda`, so `lambda(r-1) >= lambda log r = s2 log r >= 1 - B_m -
1.1/m^2` via `e^x - 1 >= x` — no linearization constant and no Bona
needed; (the `(r-1)`-form reading `1.1 + 0.6 = 1.7 <= C_A` is also valid —
either way the constant is `<= C_A`)."

**B5 [= §2b item 6 = numerics N-F3; mixed margin pair].** §3's "Measured
truth margin at the spec point: 6.7x ... vs the `0.2516` budget" mixes
pairs (inherited verbatim from STATUS_wave2 §2; the same fix applies to
any future quote of that line). *Erratum:* read "6.5x against the 20/79.5
budget (6.7x against `eps*`)". Verification (`w3r_mr12_checks.py` §(4)):

```
   budget ratio  (20/79.5)/0.0385 = 6.53  -> '6.5x'
   eps*  ratio   eps*/0.0385      = 6.71  -> '6.7x'
```

**B6 [= §2b item 7, observations O1/O3].** O1 (record): §7 item 4's
"pending" is stale in the safe direction — `wave2_repairs_20260811.md`
exists and applies STATUS_wave2 §2a/§2b/§2c; its own single-referee pass
is still owed (STATUS_wave3 §3 item 2, NOT discharged by this file). O3 is
discharged as §C below.

## §C. Harness-report C5 scope erratum (STATUS_wave3 §2b item 7 O3 / assembly §7 item 8) — host `harness_m200_20260811.md`

§3's header and C5 display say the sharp lower bound C5
(`r_m >= 1 + (187/216)/sigma_m^2`) is certified for "`4 <= m <= 400`",
with no C5 exemption shown. *Erratum:* C5's certified scope is
"`5 <= m <= 400`, equality iff `m = 6`" — the runner `run_m200.py` line
106 exempts `m = 4` by design ("`m=4 predates the sharp bound's range
(5 <= m); record only`"), the display simply failed to say so; this
matches F2_PROOF_DRAFT statement-correction 1 ("for all `m >= 5`"). The
bound is genuinely FALSE at `m = 4` and the exemption is necessary;
exact arithmetic (`w3r_mr12_checks.py` §(3), archived):

```
   varfit(4) = 91/108 ; == 91/108: True ; < 187/216: True
   varfit(5) = 7/8 ; == 7/8: True ; >= 187/216: True
   varfit(6) = 187/216 ; == 187/216 (equality case): True
```

C1–C4/C6 scopes are untouched (`4 <= m <= 400` stands for them, with the
known documented `m = 4` exceptions in C2/C3). No consumer anywhere in
the Theorem A chain uses C5 at `m = 4` (both theoremA referees confirm).

## §D. Script inventory and no-drift check

All under `g2_scripts/campaign_20260811/wave3_repairs/`, SAVED and RUN
2026-08-12, output archived beside each:

| script | applies | output |
|---|---|---|
| `w3r_f1_sl5_nc1_fixed.py` | A5 (fixed copy of `wp4_SL5/sl5_nc1_ledger_exact.py` [1], ceil/floor display; arithmetic identical) | `out_w3r_f1_sl5_nc1_fixed.txt` |
| `w3r_f1_wp4asm_fixed.py` | A5, A2 (fixed copy of `wp4_assembly/wp4asm_chain.py` [1][2][3][1b], ceil/floor display; arithmetic identical; [4] ESTIMATES block not copied — float-labeled, unaffected by F1) | `out_w3r_f1_wp4asm_fixed.txt` |
| `w3r_mr12_checks.py` | B1 (MR-1 floor), B2 (MR-2/N-F2 polynomial certificate, sympy exact root count), §C (C5 arithmetic), B5 (N-F3 ratios) | `out_w3r_mr12_checks.txt` |

**No-drift check.** The two fixed-display re-runs reproduce every exact
Fraction of the originals: all 7 + 7 + 7 ledger rows PASS exactly as
before; the three effective-C* fractions are unchanged
(`4734473/280000`, `458360713/28000000`, `201619/20000`); the D1 delta
`+0.000634` unchanged. `w3r_mr12_checks.py` only ADDS lower-bound floors
and certificates (g(401) sits below the true brackets `0.009575/0.009556`;
the 0.55 certificate sits above the true limit 27/50). Therefore: **no
certified constant, threshold, scope (beyond the stated C5 rescope to
`5 <= m`, which is the runner's actual behavior), or verdict moved by this
file.**

**Standing after this file:** STATUS_wave3 §3 item 3 (apply the wave-3
repair lists) is DISCHARGED. Still pending, unchanged: the `m = 540`
harness relaunch (§3 item 1), the referee pass on
`wave2_repairs_20260811.md` (§3 item 2), the wave-4 CL bridge itself
(§3 item 4), and — house-rule debt — a referee pass on THIS file
(single-verifier class, mirroring `referee_repairs_20260811.md`).

*End of wave3_repairs_20260812.md.*
