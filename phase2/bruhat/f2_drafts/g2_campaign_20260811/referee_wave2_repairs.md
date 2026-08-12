# Referee report: wave2_repairs_20260811.md (wave-3 repair-application session)

*Verifier session, 2026-08-12. Target: `wave2_repairs_20260811.md` + all
scripts and archived outputs under
`g2_scripts/campaign_20260811/wave2_repairs/` (EXCEPT `run_m540.py`, whose
relaunch/resume is assigned to a separate agent — its §D CLAIMS are still
refereed here against the on-disk record). Method: every script re-run and
diffed byte-for-byte against its archived output; the three `refm_*` copies
diffed byte-for-byte against their `referee_t2_maths_scripts/` originals;
every §A/§B/§C erratum checked off against STATUS_wave2's §2a/§2b/§2c
consolidated lists, against the five source referee reports, and against the
host drafts on disk (defective displays confirmed still present — no-erasing
respected); the load-bearing numbers re-derived by an INDEPENDENT exact/
high-precision script (`referee_wave2_repairs_scripts/w2r_referee_indep.py`,
SAVED + RUN, output archived beside it as `out_w2r_referee_indep.txt`,
VERDICT PASS; method-disjoint from the session's: mpmath dps-50 `nsum` for `E(u)` vs the session's integer fixed
point; independent Fraction re-implementations of the crossovers, the NC-13
table, the margin fraction, the R2 chain; hand checks of the refm_a
identities). No file modified; this report is new. Mirrors
`referee_repairs_20260811.md` (single-verifier role).*

**VERDICT: MINOR_REPAIRS.** The file's actual mandate — applying STATUS_wave2
§2a (A1–A11), §2b (B1–B10), §2c (C1–C8) — is FULLY DISCHARGED: the mapping to
the consolidated lists is one-to-one and complete, no item is skipped or
misapplied, every erratum's "defective display" is verbatim-present in its
host, every replacement is faithful to the referee-supplied content, and every
numeric claim traces to a saved script whose archived output reproduces
byte-identically and whose key values my independent re-derivations confirm.
The §E no-certified-digit-moved classification is accurate. **The one
substantive defect is §D's status header**: "PROVED (exact finite
computation)" for a harness run that is INCOMPLETE on disk (`results_m540.txt`
last row `m = 481`, all 478 rows PASS, zero failures, NO "# OVERALL" line —
the process died; the doc's own body honestly instructs consumers to check for
the OVERALL line, but the header and the "closes BOTH gap bands" sentence
assert completion). Repair W-F1 below; plus five trivia findings, none
touching a constant or verdict.

## Contents
1. Reproduction protocol and results (all scripts)
2. Independent re-derivations (method-disjoint)
3. §A (wp2-a2, items A1–A11) — item-by-item verification
4. §B (wp3-a2, items B1–B10) — item-by-item verification
5. §C (T2, items C1–C8) — item-by-item verification
6. §D and §E — the run record, the inventory, the no-digit-moved check
7. Required repairs (W-F1) and observations (W-F2–W-F6)

---

## 1. Reproduction protocol and results

All runs 2026-08-12, this session, CPython 3, same machine. Each stdout
diffed against the archived output.

| script / artifact | provenance check | re-run result |
|---|---|---|
| `w2r_rep1_e_decimals.py` vs `out_w2r_rep1.txt` | new, exact integer | **byte-identical**; VERDICT PASS |
| `w2r_rep2_crossovers.py` vs `out_w2r_rep2.txt` | new, exact Fraction | **byte-identical**; VERDICT PASS |
| `w2r_rep3_wp2a2_rows.py` vs `out_w2r_rep3.txt` | imports `wp2a2_lib2` unmodified (path checked: `../wp2_a2`) | **byte-identical**; VERDICT PASS |
| `refm_a_t8pp_t10.py` vs `out_refm_a_rerun.txt` | **byte-identical to `referee_t2_maths_scripts/` original** (cmp) | **byte-identical** |
| `refm_b_chains.py` vs `out_refm_b_rerun.txt` | **byte-identical to original** (cmp) | **byte-identical** |
| `refm_c_identities.py` vs `out_refm_c_rerun.txt` | **byte-identical to original** (cmp) | **byte-identical** |
| `run_m540.py` | diff vs `harness_m200/run_m200.py`: 32-line diff = docstring + usage line + MMAX/out defaults + checkpoint tuple `400, 401, 534, 535, 537` — **exactly as §D/§E claim**; verdict path untouched | NOT re-run (separate agent); on-disk `results_m540.txt` state recorded in §6 |

Every doc-quoted output block (A3, A6, A8, A10, B2, B3, C1, C3, C4, §D's two
archived `status_wave2` rows, the `m = 476` sample row) was located verbatim
in the corresponding archived file.

## 2. Independent re-derivations (`w2r_referee_indep.py`, VERDICT PASS)

Saved with archived output under `referee_wave2_repairs_scripts/`; every
check below is method-disjoint from the session's scripts.

- **E(u) brackets (B2).** mpmath dps-50 `nsum` of
  `2(3 v_n^2 + u^2)/(v_n^2 (v_n^2+u^2)^2)`, `v_n = 2 pi n`: all six values
  land INSIDE w2r_rep1's certified 12-decimal brackets
  (`E(4) = 0.0024899244245532...` etc.); the four originals
  (.00400693/.00358719/.00304036/.00161241) confirmed NOT lower bounds; the
  six corrected prints confirmed lower bounds; E(4)/E(5) originals confirmed
  safe. The pi bracket `314159265358979323846/10^20 < pi < .../847/10^20`
  confirmed at dps 50.
- **Propagation (B2).** `rho(4) <= 0.72711` re-certified; R2 chain re-built
  independently: `eps* = 0.258353 >= 20/79.5 = 0.251573`, R2 value
  `1.029326 >= 1.0292` — and the doc's claim that the two referee
  cross-checks bracket it is verbatim-true on disk
  (`referee_maths_wp3_a2.md` 1.02928; `referee_numerics_wp3_a2.md`
  1.029462). `deficit(2)`: old 0.0983 confirmed unsafe, 0.0982 confirmed
  safe. Old `rho(4)` print 0.7271 confirmed unsafe by **4.283e-6** (see
  W-F2: the doc says "4.8e-6").
- **Crossovers (A8, B3).** Independent Fraction scan: bracket
  `6.85 E(4)(1 - 17 B_m - C/m^2) - B_m` first positive at **m = 82** exactly
  (negative at 81 and at the draft's "~68"); NC-13 table reproduces
  `m0 = 9/12/17/23` at `C' = 1/5/20/42` in BOTH flavors (so "~27" -> 23
  confirmed); `B_401·401 = 1.0787` sanity-checks the `B_m` implementation
  against the `27/25` law.
- **Margin (B10 ii).** `1580^2·3167/(144·2·1581) = 17363 + 14921/28458`
  exactly; `17363 <= margin < 17364` — "17363x" is the safe print.
- **refm_a identities (C3, C4).** Hand-check at `lam = 0.1`,
  `q = e^{-0.1}`: `E X^2 = q(1+q)/(1-q)^2 = 190.3251 > 121 = (1+1/lam)^2`
  (the displayed T.8'' route is indeed false) while
  `Var = q/(1-q)^2 = 99.9167 <= 121` (the memorylessness rescue closes).
  M8's inequality `(1-d)^{-2} <= 1+2d+3.5d^2`: exact failure root
  `d* = (5 - sqrt(18))/7 = 0.10819` (see W-F6).
- **C2 arithmetic.** `1 - 0.0330·3.7^2 = 0.54823 >= 0.548` exact.
- **Endpoint-validity of the E-certificate (W-F4).** The per-term function is
  strictly decreasing in the pi-numerator `p` (termwise
  `3/(3a+c) < 1/a`, `a = v_n^2 q^2`, `c = u^2 q^2`), verified at spot
  `(u, n)` pairs including the extremes — so w2r_rep1's min/max over the two
  endpoints IS a valid interval bound, though not for the reason its
  docstring gives.

## 3. §A (wp2-a2 repairs A1–A11) — verified applied

Mapping A1–A11 <-> STATUS_wave2 §2a items 1–11: one-to-one, complete.

- **A1 [F1/R-F1]:** host line 64 has the defective "unit-step to 3000,
  spot-checked to 10^4"; the replacement matches the draft's own §6/§10
  scope and the numerics referee's R1 extension (unit step [1000, 3000],
  step 20 to 10^4, spot to 10^6) as reported. APPLIED.
- **A2 [F2]:** the three exponent-0 classes (`ZI^4`; `ZR·ZI^2`-against-
  constant, e.g. `A4 A3^2`; WI's `A3^3` via the `|t|`-shift,
  `2+3-(9+1)/2 = 0`) transcribe `referee_maths_wp2_a2.md` §2.3/§4 item 2
  verbatim (report lines 286–289, 109). APPLIED.
- **A3 [F3]:** LFlow provenance sentence matches the referee's demanded
  content; the four LFlow values (0.99248/0.98704/0.96388/0.92237) re-run
  identical via the unmodified shipped library. APPLIED.
- **A4 [F4]:** host line 437 has `Z(-+h)`; fix is the referee's. APPLIED.
- **A5 [F5, 5 sub-items]:** (i) NC-A6 confirmed ABSENT from the host's
  header list (lines 37–39) and §8 table (631–635) while used at line 706 —
  addition correct; (ii)–(v) all match F5's list. APPLIED.
- **A6 [R-F2]:** host line 526 confirmed carrying borrowed cells (den 17.65
  = the m=180 value 17.6507, line 664; den 1380.63 = the m=379 value, line
  665); the genuine rows at (1,180)/(2,181)/(4,367) re-run identical and the
  `C_ker` column reproduces NC-A3(5)'s 30.8863/209.0224/37810.0442 under the
  displayed headlines. APPLIED.
- **A7 [R-F3]:** wp2-b line 552 confirmed: 1.391 at `m = 100`, `K = 1`;
  range "1.374–1.391" correct. APPLIED.
- **A8 [R-F4]:** host line 620 has "m ~ 27"; exact solve gives 23 (both
  flavors), NC-13's 9/12/17 reproduce — independently confirmed (§2).
  APPLIED.
- **A9 [R-F5]:** the PW-port sentence matches
  `referee_numerics_wp2_a2.md` §3.1/R-F5 (187.265 vs 187.414, h-term-free
  `P0_min` at y = 0, verified-not-a-bug). APPLIED.
- **A10 [R-F6]:** host line 449 has the unsafe "LFlow >= 0.9224"; re-run
  certifies 0.92237 < 0.9224 and theorem-pair min 0.96388. APPLIED.
- **A11 [R-F7]:** hygiene note only, correctly scoped to future re-runs;
  the referee's reproduced 1.3863/4.0702/5.0216 accurately cited. APPLIED.

## 4. §B (wp3-a2 repairs B1–B10) — verified applied

Mapping B1–B10 <-> STATUS_wave2 §2b items 1–10: one-to-one, complete.

- **B1 [R1, mathematical content]:** rescope of P.7 clause 1 to `|w| <= 8`
  (alt. `48 E(w) m^4 >= 1000`) matches the referee's supplied repair
  including the `m = 30, |w| >~ 57` witness; clause 2 untouched; downstream
  use confirmed at `w0 <= 6` only. APPLIED.
- **B2 [R2 = F1, the E-decimal reprints]:** the four unsafe originals
  confirmed in the host's P.7 table (line 440); every corrected print and
  the full propagation chain (deficit row incl. the additionally-unsafe
  0.0983 -> 0.0982; `rho(4) <= 0.72711` in all four host locations, lines
  94/442/507/535/554; R2-row 1.0294 -> `>= 1.0292`; note-2 0.01628 ->
  `>= 0.01627`) certified by exact integer arithmetic, re-run identical,
  and independently confirmed (§2). The upgrade from the shipped float
  script to exact-integer certification is genuine added value. APPLIED.
- **B3 [R3 = F4]:** host line 566 has "~68"; first-positive `m = 82`
  independently confirmed; consumed claims (`m >= 100`; positivity at 401)
  re-verified true. APPLIED.
- **B4 [F2]:** host lines 436/686/727 have "< 2e-21"; the rigorous tail
  bound 1.369e-17 makes the restatement moot-safe as claimed (the tail
  logic itself checked: `term <= 8/(2 pi n)^4`, integral comparison, PI_LO
  in the denominator = safe direction). APPLIED.
- **B5 [F3 = R8-part]:** host lines 536/542 confirmed double-counting `Lin`
  inside `C_R^PT(4) + C_ker + Lin`; both replacement spellings match the
  referee's; safe direction correctly stated. APPLIED.
- **B6 [R4]:** the `k = N/2, lam = 0` one-liner matches R4, with the
  correct alternative citations. APPLIED.
- **B7 [R5]:** scan-scope restatement matches R5; the quoted independent
  full-interior confirmation (0.0385/0.0194/0.0084 at m = 30/60/140) is
  verbatim in `referee_numerics_wp3_a2.md` F6. APPLIED.
- **B8 [R6]:** the statement-qualifier matches R6; the synthesis discharge
  note (M(4) = 367 replaces the proxy) is consistent with STATUS_wave2's own
  bracketed note and correctly does not delete the text repair. APPLIED.
- **B9 [R7]:** `Phi(1) = 1 - 1/m` one-liner matches R7. APPLIED.
- **B10 [R8 + F5–F8, 5 sub-items]:** (i) host line 585 confirmed printing
  the round-DOWN cap 0.6931 (log 2 = 0.693147; a cap must round UP — 0.6932
  correct); (ii) 17363x independently confirmed exact (§2), the 1879.056
  companion verbatim in F5; (iii) relabel-and-move matches F6; (iv) the F7
  constants list (5.923067 / 1.805309 / 20.649186 / 34.920037 / 263.230377
  / 0.721956-printed-high) and the `sigma_1'` ~1e-118 note are verbatim
  from `referee_numerics_wp3_a2.md`; (v) F8 correctly recorded as
  no-text-forced. APPLIED.

## 5. §C (T2 repairs C1–C8) — verified applied

Mapping C1–C8 <-> STATUS_wave2 §2c items 1–8: one-to-one, complete. The
three referee scripts confirmed byte-identical copies, re-run identical;
every quoted block located verbatim in the rerun outputs.

- **C1 [M1+M5-part+M7]:** host line 1211 confirmed carrying the FALSE
  `rho := 1 - 0.04 w_0^2`; the replacement two-inclusion statement with
  `rho := 1 - 0.022 w_0^2` transcribes `referee_t2_maths.md` §2.4/§5 item 1
  faithfully (incl. the overlap annulus, the deficit-monotonicity cite, the
  (d)-block disjointness record `w* = 1.1502..1.1742 w_0`); `0.0332 ->
  0.0347` covers both host occurrences (lines 421 and 1210–1211; certified
  0.034667, refm block (e)); the `m_0(i)` header fix (`m >= 53` via
  `m^3/72 >= 2000`, refm_b block (h)) confirmed; the P.7 cross-consistency
  note (`0.0274` at `w_0 = 1`) matches B2's certified 0.0274474. APPLIED.
- **C2 [M3]:** `[1/m, 3.7/m] -> [1/m, pi/m]` with the W.1(i) sliver
  alternative; `pi < 3.7` in refm_b (h); the sliver arithmetic
  `1 - 0.0330·3.7^2 = 0.54823 >= 0.548` independently exact (§2); wp2-b's
  citable-status flag correctly carried. APPLIED.
- **C3 [M2, mathematical content]:** the displayed route's falseness
  re-confirmed independently (EX^2 = 190.33 > 121 at `lam = 0.1`, §2); the
  memorylessness mixture rescue and the `-1 -> -2` weakening transcribe M2
  exactly; "downstream exposure: none" re-checked — T.8-final's (V) uses
  `m_* >= m/pi - 1` from its own hypothesis (host line 716/739), and
  nothing in the campaign chain cites T.8'' (consistent with both
  STATUS files). APPLIED.
- **C4 [M8+F1 interaction]:** correctly records that the `B_lam/B_m` line is
  already superseded by Lemma T.9-Step2' (verified SURVIVES in
  `referee_repairs_20260811.md`) and that the repaired inequality's
  `d <= 0.1` caveat is met at `d <= 0.033`; block (g)'s TRUE/FALSE split
  reproduces. APPLIED (see W-F6 on the "~0.107" phrasing).
- **C5 [M4]:** host lines 462/473 confirmed; `1.18 -> 1.178` (display
  misses `1/155` by 1.24e-6 while the exact chain gives 0.0062948 <=
  0.0064516) and the `/284` margin note (7.8e-7 abs = 2.2e-4 rel — ratio
  checked) reproduce refm_b (a)/(b). APPLIED.
- **C6 [M5]:** host line 377 confirmed displaying `1 - u^2/25` while the
  proof (line 385) and table (line 162) establish/use `1 - u^2/19`; refm_c
  (c) certifies the stronger `>= 1 - u^2/19.7` numerically (which implies
  the /19 display); strikes and the 0.0347 prose fix consistent with C1.
  APPLIED.
- **C7 [M6]:** the five-line constant chase (0.5938/0.0371/0.5193;
  `1/24 + 0.0458 = 0.0874 <= 1/6`) transcribed exactly; refm_b (f)
  reproduces. APPLIED.
- **C8 [item 8]:** the F2/F5/F6/F7/F8 items confirmed already applied in
  `repairs_20260811.md` §C (SURVIVES report on disk); the r = 4 coefficient
  2.611277e-04 reproduces in refm_b block (c) (see W-F5 on the "refm_a/
  refm_b" attribution). APPLIED.

## 6. §D and §E

**§D (harness to 540).** The two quoted `m* = 535/537` rows are verbatim in
the archived `status_wave2/out_status_wave2_checks.txt`; `run_m540.py`'s
diff against `run_m200.py` is exactly the claimed docstring/MMAX/
checkpoint changes (32 diff lines; certificates and verdict path
untouched); the `m = 476` sample row is verbatim in `results_m540.txt`.
**But the on-disk run record is INCOMPLETE**: `results_m540.txt` ends at
row `m = 481` (478 PASS rows `m = 4..481`, zero FAIL, empty stderr, no
"# OVERALL" line — the process died after the file's last edit at 476).
The doc's body is honest about this (it quotes only through 476 and
mandates the OVERALL-line check on any consumer), and STATUS_wave3 §1 row 7
/ §3 item 1 record the death accurately. The defect is purely the section's
STATUS LABEL and completion-asserting sentence — see W-F1. Coverage
arithmetic as such is correct: rows through 481 close `[401, 481]` of the
`[401, 536]` band; the remainder `[482, 536]` awaits the relaunch (separate
agent).

**§E.** Inventory table accurate (modulo W-F5's two attribution slips); the
five-way classification (i)–(v) of the repairs is correct on inspection —
in particular the two theorem-statement rescopes (B1, C3) strictly contain
every downstream use (P.7 consumed at `w0 <= 6`; T.8'' consumed nowhere),
and NO certified constant, threshold, region boundary, conditional, or
verdict moved (checked item-by-item against §§3–5 above). The citability
paragraph correctly leaves CL untouched and correctly marks this file's own
referee pass as the pending gate — discharged by this report, modulo W-F1.

## 7. Required repairs and observations

**W-F1 (the one substantive repair — §D status label).** §D's header
"— PROVED (exact finite computation)" and its sentence "so exact coverage
through `m = 540` closes BOTH gap bands ... no uncovered `m` remains" assert
a computation that has not completed: `results_m540.txt` has no OVERALL
line and stops at `m = 481`. Relabel §D "IN PROGRESS — run died at
`m = 481`; every completed row PASS; claim becomes PROVED when
`results_m540.txt` ends with `# OVERALL: PASS` (rows: 537, failures: 0)"
(or equivalent), and put the band-closure sentence in the conditional. The
body's consumer caveat already says the right thing; the label must match
it. No other §D change needed.

**W-F2 (wrong digit, descriptive only).** §B B2: "the old print 0.7271 was
unsafe by 4.8e-6" — the certified gap is 4.283e-6; print "4.3e-6" (or
"~4e-6"). No inequality is affected (the reprint 0.72711 is what's
consumed, and it is certified).

**W-F3 (docstring typo in `w2r_rep1_e_decimals.py`).** Its header says
"rho(4) <= 0.72711 (0.7271048 certified)"; the script's own output (and the
truth) is 0.7271043. Output and doc text are correct; fix the docstring on
any future copy.

**W-F4 (certificate justification, record-only — certificate itself
VALID).** `w2r_rep1`'s docstring claims min/max over the two pi endpoints
needs "no monotonicity-in-v^2 claim". Endpoint evaluation bounds a function
over an interval only if its extremes sit at the endpoints; the actual
justification is that each term is strictly decreasing in the pi-numerator
`p` (termwise `3/(3a+c) < 1/a — one line), which I verified (§2). The
computed brackets are therefore correct as shipped; only the dismissive
sentence is wrong. Fold the one-line monotonicity remark into any future
edit.

**W-F5 (inventory attribution trivia).** §E's `refm_a` row lists C2, but
the C2-supporting check (`pi < 3.7`) lives in refm_b block (h) (refm_a has
blocks (a)–(g) only); likewise C8's "re-run refm_a/refm_b block (c)" — the
r = 4 coefficient is in refm_b block (c) only (refm_a's block (c) is the
`m_*` search). Cosmetic; every claimed fact IS in the archived outputs.

**W-F6 (record-only).** C4's "it fails from d ~ 0.107": the exact failure
root of `(1-d)^{-2} = 1 + 2d + 3.5d^2` is `d* = (5 - sqrt 18)/7 = 0.10819`,
and block (g) itself shows the inequality still TRUE at d = 0.107. The "~"
makes the sentence defensible; "fails beyond d* = 0.1082" would be exact.
The consumed fact (the repairs doc's version sits at `d <= 0.033`,
compliant) is unaffected.

**Citability effect of this report.** With W-F1's relabel applied (a
one-line text edit), the §2a/§2b/§2c discharges and the §C repaired-form
citability of T.10(2)/T.8'' move from "provisional" to refereed
(single-verifier, mirroring `referee_repairs_20260811.md`). §D's band
closure remains pending the relaunched run regardless of the relabel.

*End of referee_wave2_repairs.md.*
