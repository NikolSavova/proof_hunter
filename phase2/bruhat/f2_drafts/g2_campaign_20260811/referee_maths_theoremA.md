# Adversarial MATHS referee report — `theoremA_assembly_20260811.md`

*Wave-3 referee pass, 2026-08-12. Target: the merged Theorem A note
(`theoremA_assembly_20260811.md` + its script
`g2_scripts/campaign_20260811/theoremA_assembly/assembly_checks.py`), the
designated referee unit for the cross-package plug. Brief: verify (i) the
dependency graph is complete and acyclic, (ii) every citation matches its
source verbatim with true hypotheses, (iii) the plug arithmetic, (iv) the
end-to-end constant ledger. `CL(79, 20, 0.89)` is the note's single NAMED
conditional; per brief, conditionality is not penalized — the REDUCTION is
what is verified. Blind rule respected: `g2_draft_t1_20260803.md` not read;
no wp4 content consumed (the wp4 files now present in the directory were not
opened for any verification step below — the assembly is refereed exactly as
written, against the frozen spec in `wp3_draft_a2.md` §6.1). No existing
file modified. Every numeric claim in this report is from the SAVED and RUN
referee script*
`g2_scripts/campaign_20260811/referee_theoremA/referee_checks_theoremA.py`
*(new file; output archived beside it as `out_referee_checks_theoremA.txt`),
or from the byte-level diff in §1.*

## VERDICT: MINOR_REPAIRS

Every load-bearing claim survives. The dependency graph is complete and
acyclic; every citation I traced (§3 — all of them) matches its source with
true hypotheses, quoting the REPAIRED values where repairs exist; the plug
arithmetic reproduces exactly in an independently coded exact-Fraction
script; the constant ledger is accurate row by row. The reduction to
`CL(79, 20, 0.89)` is correctly and completely executed: `[WP4-CITATION]` is
load-bearing in exactly one place (§2.3's R2 row), and I confirm no other
step consumes CL or any unproved statement. Four repairs (§6): one small
genuine proof gap with a supplied one-line fix (the R3 `w^2`-bracket's
positivity beyond the scanned range, MR-1), one statement-level overclaim in
§0 (the `27/25`-form's `O(m^{-2})` constant attributed to `C_A`, MR-2), and
two display items. None moves a constant, a threshold, a region boundary,
or the conditional's spec.

---

## 1. Reproduction and independent re-derivation

- **`assembly_checks.py` re-run (2026-08-12): byte-identical** to the
  archived `out_assembly_checks.txt` (plain `diff`, zero differences).
- **Independent script** (`referee_checks_theoremA.py`, own code paths,
  exact `Fraction` arithmetic, including an independently shaped Mahonian
  row-recurrence for the harness re-anchor): every printed verdict `True`,
  every value matches the assembly's to all displayed digits. Key lines:
  `C_A` grid `= 189076821/5000 = 37815.3642` exactly; closed `37997.8442`
  exactly; `R3(401)` = `0.762141` / `0.761006`; `eps* = 1291739/5000000 =
  0.2583478` exactly; band budgets `0.251572` / `0.2580645` (margin
  `2.83e-04`); R2 conclusion `1.029318 >= 1.02`; `e^{0.89}` 22-term exact
  partial sum `> 2.435129651 > 17/7 > 2` (so both tilt caps `< 0.89`,
  independent of the doc's 18-term sum); bracket(401) `0.009575` (grid) /
  `0.009556` (closed); R1a `894436.2 >= 10^5`; R1b `1879.1`; `H(4, 367) =
  0.3321 <= 1/2`; `B_m·m` at `401`/`10^5` = `1.078693`/`1.079995`;
  `varfit(6) = 187/216` exactly, `varfit(40) = 0.973381`, argmins central;
  G4 crossovers `m* = 535`/`537` replicated.
- **Harness cross-check**: `run_m200.py` line 106 confirms the `m = 4`
  C5-exemption with the exact comment the assembly quotes ("predates the
  sharp bound's range"); harness report §3's header does display
  `4 <= m <= 400` over C5 — the assembly's erratum note (§7 item 8) is
  correct and correctly scoped (`5 <= m`, matching F2_PROOF_DRAFT
  statement-correction 1 and its line "`r_m >= 1 + (187/216)/sigma_m^2` for
  all `m >= 5`, equality iff `m = 6`").

## 2. Dependency graph: COMPLETE and ACYCLIC — verified

**Acyclicity.** The file-level order
`F2_PROOF_DRAFT -> g1_draft_b -> g2_draft_t2 -> wp1_c -> wp2_b ->
{repairs_20260811, wp2_a2, wp3_a2} -> assembly`, with `harness_m200`
depending on nothing and `wp2_a2`/`wp3_a2` mutually blind (verified: neither
cites the other; their union is consumed only by the assembly's plug), is a
topological order — every edge in §5.2 of the assembly points forward in it.
No cycle exists. In particular the one place a cycle could hide — Theorem S
naming "wp2-a's `C_ker`" while T.9-final could conceivably have leaned on
Theorem S — is clean: `wp2_draft_a2.md` nowhere references wp3-a2 or any
stitch object.

**Completeness.** I enumerated everything the §2 proof consumes and checked
each appears in §5.1/§5.2 or is an explicitly flagged ambient citation:
Lemmas 3.1/3.3/3.6 + Cor 2.3 statement (F2 frame — L3.3, used inside P.7's
second clause, is covered by the frame node; the per-lemma arrows are
illustrative and the P.7 arrow is drawn from (T.4)-Step2, which is the
substantive input); B.0(i)(ii)/B.8/B.9 (g1_b); T.1(ii), (T.4)-Step2 +
(T.4a'')-kernel, T.5, (T.6ii), (T.8a), T.9'' (T2 — all inside the
two-referee inventory; the pending §2c repair to (T.4a'')'s LOWER
coefficient `/25 -> /19` touches nothing P.7 uses: P.7 consumes the kernel
`E` and the Step-2 identity, both "confirmed correct" in
`referee_t2_maths.md`, and wp3-a2 §4 explicitly records why the (T.4)-lower
factor is NOT used); W.3–W.6 (wp1-c); W.0–W.7 (wp2-b); D.5/T.9-final
(wp2-a2); P.5–P.8/Theorem S (wp3-a2); harness C1–C6; Lemma T.9-Step2'
(repairs). Ambient: Bona `r(k) >= 1` — flagged (§7 item 3), consumed only in
wp2-b's W.5/Lin bucket (the assembly's exact-center LB needs no Bona:
`e^x - 1 >= x` suffices, see §6 MR-4). **Nothing consumed is missing from
the graph; `g2_draft_t1` and every wp4 file are consumed nowhere**
(grep-verified: T.10/T.8'' appear in the assembly only inside
do-not-cite caveats).

## 3. Citation audit — every source claim traced (all verbatim-true)

| assembly claim | source, checked verbatim | status |
|---|---|---|
| CL spec text + `(79, 20, 0.89)`, `m >= 401`, lower-bound variant | `wp3_draft_a2.md` §5 (lines 510–516) + §6.1 | **verbatim** |
| Theorem S partition `K_c = min(cm, m-1)`, R1a/R1b/R2/R3, c-clauses `7/10`/`1` at `1581` | wp3-a2 §5 | verbatim |
| R1a row: L3.6 `r(1)-1 >= (m-1)/(2(m+1))`, `>= 10^5` | F2 Lemma 3.6 (`k <= sqrt(m)/4`, `m >= 16` — satisfied at `k=1, m >= 401`); value re-derived `8.94e5` | true |
| R1b row: P.5 `r-1 >= (m-1)/(2k(m+k))`, `m_p = 300/1581`, `>= 1879` | wp3-a2 P.5 + table; formula `(m-1)^2(2m+5)/(144c(1+c)m)` re-derived `1879.1` | true |
| R2 row: `v(7/10)·401 = 79.53 >= 79`; `rho(4) <= 0.72711` (REPAIRED); caps `log(17/7), log2 < 0.89`; budgets; `>= 1.0293` | wp3-a2 §5 + `wave2_repairs_20260811.md` (rho/E reprints confirmed applied there); caps proved exactly here | true, repaired values |
| `136/527` band-2 line | wp3-a2 threshold table (`C* max = 136` at `[1581, inf)`) — re-checked against the REPAIRED `eps*`, margin `2.83e-4` | true |
| T.9-final display (both forms, `c_w`, `C_R` both flavors, `Lin` entries, `M(K)`) | `wp2_draft_a2.md` §7, lines 559–579 | **verbatim** |
| `H(K, M(K)) = 0.0097/0.0241/0.3321 <= 1/2`, decreasing | wp2-a2 NC-A5(2); recomputed exactly | true |
| D.5: `C_ker = 30.89/209.03/37811`, `M(K) = 180/181/367`, table value `37810.0442`, `w`-uniformity | wp2-a2 §6 + §7 envelope note (lines 609–614) | verbatim |
| `C_R^PT(4)`: grid `5.32 = 4.93 + 0.01402 + 0.3719` (B3), closed `187.8` | `repairs_20260811.md` §B3 + wp2-b NC-W4 (`187.414 + 0.01402 + 0.3719`) | true |
| Lin/Bona: `m^2 Lin = 0.2308/0.2571/0.3719` at 180, decreasing; `r >= 1` ambient | wp2-b W.5 (proof cites Bona explicitly) | true, flagged |
| wp1-c: `c_1(K) = 0.2259/0.1802/0.1019`; floor `0.0372 m` on `|lam| <= 1.7627`; `0.0373` on W.5(ii); margins `9.1e-6` | wp1-c W.4(i)/W.5 + repairs §A1/§A3 | verbatim |
| wp2-b floors `0.967/0.868/0.60`; `c_w = 0.407/0.466/1` grid class | wp2-b W.1/W.6 + repairs B2/B4/B5 | verbatim, class as marked |
| Cor 2.3/UB: `|E| <= 1.2/m^2` log, `1.8/m^2` `(r-1)`, `m >= 180`, `C_2(0.1) = 1.1` | `g1_draft_b.md` §7 item 3 (`1.2 + 0.6 = 1.8`) + `m_1 = 180` | **verbatim** |
| `B_m in [1.068, 1.080]/m` (`m >= 30`) | g1_b Lemma B.0(ii), polynomial-root certificate (proof-grade) | verbatim |
| E-decimal reprints (`E(1) >= .00400692` … `E(6) >= .00161240`; E(4)/E(5) as printed) | referee R2/F1 list = `wave2_repairs` applied values; wp3-a2's originals confirmed round-to-nearest | repaired values quoted |
| truncation "`< 2e-15`" (not the draft's false `2e-21`) | numerics-F2 repair | repaired value quoted |
| `C_P(c) = 12.34/36.17/83.61/263.23`; P.5 slack `2.0002`; `m_p` formula | wp3-a2 §3 | verbatim |
| harness: 320.9 s, 397 rows, C1–C6, `varfit(400) = 0.997302329987`, checkpoint rows | `harness_m200_20260811.md` §2–§3 | verbatim (+ the C5 scope erratum, correctly recorded) |
| `m_2(K)` proxies `143/190/267/379` retired for real `M(4) = 367` | wp1-c §6/NC-T10d; wp2-a2 §6 | true |
| T2 inventory two-referee; T.10(2)/T.8'' consumed nowhere | `referee_t2_maths.md` (T.5 "CORRECT, fully"; T.9'' "fully verified"; verdict MINOR_REPAIRS) + grep of assembly | true |
| Block-B footnote (`m* = 22` vs STATUS's 30) | `status_wave2_checks.py` line 45 scans from `m = 30` — the assembly's explanation is exactly right | true |

**Hypothesis checks at every application point** (the part a citation table
cannot show): T.9-final needs `m >= 367`, interior `k`, `0 < |lam| <= 4/m` —
R3 supplies all three, the excluded `lam = 0` point handled by B.8/B.9 with
the note's constant safely `<= C_A` (see MR-4); Cor B.9 needs `m >= 180`,
`|y| <= 0.1` — satisfied at `k_c` for `m >= 401`; P.7 clause 1 is consumed
only at `|w| <= 4` and clause 2 only at `w0 = 4` — both inside the
referee-R1 rescope `|w| <= 8`; P.8 needs `k >= cm` — R2's `k > K_c` gives
it; L3.6 needs `k <= sqrt(m)/4, m >= 16` — `k = 1, m >= 401`; W.5's
`|s2 log r - 1| <= 1/2` — discharged via `H(4, 367) = 0.3321`, recomputed;
CL (as spec'd) needs `s2 >= 79`, `|lam| <= 0.89` — `79.53` and the exact
cap proofs supply them, and the note-1 monotonicity ("budget largest at the
band's left edge") is verified: `min(m, s2) >= v(c)m` is increasing along
each clause and jumps favorably at the switch. The note-2 chain's two silent
positivity requirements — the multiplier `X - B_m w^2 > 0` (`= 0.719` at
`m = 401`, plugged grid `C`) and `lambda/s2 = 1/(1-D) >= 1+D` — both hold;
re-derived by hand and in script.

## 4. The plug (§4 of the assembly) — CONFIRMED on all five checks

1. *Threshold*: `M(4) = 367 <= 401` — true (D.5 statement).
2. *Band/uniformity*: D.5's bound is `w`-uniform on `|w| <= 4` — wp2-a2's
   §7 envelope note states exactly this (resolving wp2-b referee-F5 in the
   clean direction), and R3's band is identical.
3. *Arithmetic*: `1 - B_401 - C_A/401^2 = 0.762141` (grid) / `0.761006`
   (closed) — reproduced independently, exact `Fraction`s; matches
   STATUS_wave2's plug note digits.
4. *`w^2`-discard*: bracket `0.009575`/`0.009556` at 401, positive — this
   check is genuinely NEW (neither draft could run it) and is the right
   check to have invented. One repair on its tail, MR-1 below.
5. *No double count*: `C_A = C_R^PT(4) + C_ker(4)` with `C_R^PT = PW + T +
   Lin` — decomposition verified from wp2-b's NC-W4 table and repairs §B3;
   this equals exactly what T.9-final's `(r-1)` form charges
   (`theta_2 C_R + theta_3 Lin` with `C_R = PW + T + C_ker`), so repair F3
   is correctly applied, not merely echoed.

## 5. Constant ledger (§6 of the assembly)

Every row traced to its source and class marker checked (§3 above covers
all of them). The class markers are honest: the four grid-certificate
inputs are exactly the ones STATUS_wave2 flags, `C_A`'s two flavors carry
their scopes (`m <= 2000` grid / all-`m` closed) consistently everywhere
they appear (§2.3, §2.4, §4, §6), and the "size honesty" paragraph
(7500x inflation of `C_ker(4)` vs truth anchor `5.04`) matches wp2-a2's
own honesty table (`bound/truth = 7502x`). No constant is used outside its
certified scope anywhere in the chain. The single scope subtlety —
`PW`-grid's `m <= 2000` inside a theorem quantified over all `m >= 401` —
is handled correctly: the closed flavor `37997.85` is the all-`m` constant,
the grid flavor is offered only as the sharper sub-`2000` value, and both
are fixed constants so the `O(m^{-2})` claim is unaffected either way.

## 6. Repairs required (none moves a constant, threshold, spec, or verdict)

**MR-1 (the one genuine proof gap; one-line fix supplied and verified).**
The R3 `w^2`-bracket's positivity is load-bearing for ALL `m >= 401` (it is
what lets §2.3 discard the `w^2` term), but the displayed support is: exact
scan `401..2000`, plus "monotone increasing" justified by `B_m` decreasing
— which is itself only scan-certified on `[401, 3001]` (block A3). For
`m > 3001` the claim as displayed has no proof. Fix (verified in my script,
section 3): by g1_b Lemma B.0(ii) (`B_m <= 1.080/m`, `m >= 30`, proof-grade),
`bracket(m) >= 6.85·E(4)·(1 - 18.36/m - C_A/m^2) - 1.080/m`, which is
term-by-term increasing in `m` and equals `0.009571` (grid) / `0.009551`
(closed) at `m = 401` — positive for all `m >= 401`, no scan needed. Insert
this line in §2.3's R3 row (or §4 item 4) and, in §4-A3, ground the
"increasing `-> 1`" tail the same way (`-> 1` needs only `B_m <= 1.080/m ->
0`; "increasing" beyond 3001 is unproved and should be dropped or
B.0(ii)-bounded). Same fix repairs the identical appeal in the script's
block-D parenthetical.

**MR-2 (statement-level overclaim in §0).** §0 says the two-sided
`O(m^{-2})` in `sigma^2(r_m - 1) = 1 - (27/25)m^{-1} + O(m^{-2})` carries
"the explicit constant `C_A`". Not as displayed: `C_A` is the explicit
constant of the `1 - B_m` form (§2.4's first display, which is correct);
passing to `(27/25)/m` adds the error `B_m - (27/25)/m`, which is genuinely
`O(m^{-2})` but with its own constant — measured `(1.08/m - B_m)·m^2 in
[0.524, 0.540]` on `m in [401, 10^5]` (script section 7) — and NO displayed
bound at that order exists anywhere in the chain (B.0(ii) gives only
`0.012/m`, one order short). Fix, either flavor: (a) scope §0's
explicit-constant clause to the `1 - B_m` form and mark the `27/25` form's
constant "explicit after one elementary polynomial certificate, same class
as B.0"; or (b) add that certificate (one line, e.g. `0 <= 1.08/m - B_m <=
0.55/m^2` for `m >= 30`, provable exactly as B.0(ii) was) and state the
two-sided constant as `C_A + 0.55`. Theorem A's truth is unaffected; only
the attribution sentence is wrong.

**MR-3 (display).** §4's block is labeled "Verbatim script output" but is a
condensed excerpt: it omits six archived lines (A1's band line, C5's
final cap-conclusion line, D's limit parenthetical, E's `m=4`/`m=60` rows,
F's `m=30`/`m=1581` rows, `DONE`) and reflows/merges others (A3 wrapped;
F's two quoted rows joined on one line). Every number shown does match the
archive byte-for-byte, and §2.1's `varfit(60)` quote is backed by the
archived (omitted) row. Relabel "condensed excerpt; full output archived" or
reprint verbatim — the identical repair class as wp3-a2's F7.

**MR-4 (one-clause precision, exact-center note).** §2.3's note says B.8/B.9
give "the same bound with constant `1.1 <= C_A`" at `lam = 0`. The clean
justification deserves its clause: at the center `s2 = lambda`, so
`lambda(r-1) >= lambda·log r = sigma^2 log r >= 1 - B_m - 1.1/m^2` via
`e^x - 1 >= x` — no linearization constant and no Bona needed for this
direction. As written, a reader may object that the `(r-1)` form needs
`1.1 + 0.6 = 1.7` (also `<= C_A`, so nothing breaks either way). State one
of the two.

**Observations (no action required in this document).**
- O1: `wave2_repairs_20260811.md` now exists and applies §2a/§2b — §7 item
  4's "pending" is stale in the safe direction for those two lists (the
  assembly already quotes the applied values, verified here against that
  file); the `t2_repairs` file remains genuinely pending, and nothing here
  cites the two affected T2 items.
- O2: wp4 files (draft + two referee reports) now sit in the campaign
  directory. Per the assembly's own protocol they were not consumed by it
  nor by this review; §3's flip instruction (including the re-run-block-C
  clause for a weaker landed spec) is the correct interface and its
  weaker-spec arithmetic (`C'/max(...) <= eps*`, band-2 tight at `2.8e-4`)
  is verified.
- O3: the harness-report C5 scope erratum (assembly §7 item 8) should be
  folded into the next repairs file exactly as the assembly proposes; I
  confirm the runner's exemption and that no consumer uses C5 at `m = 4`.

## 7. Bottom line

The assembly does what it claims: Theorem A = F2(a) is **PROVED CONDITIONAL
on exactly `CL(79, 20, 0.89)`**, with parts I/III/IV unconditional, the
plug sound and now independently re-verified twice, and the one-citation
flip well-defined. With MR-1–MR-4 applied (MR-1 and MR-2 have supplied,
script-verified fixes; MR-3/MR-4 are text), this referee's half is
discharged. House rule reminder: the unit still needs its numerics referee.

*End of referee_maths_theoremA.md.*
