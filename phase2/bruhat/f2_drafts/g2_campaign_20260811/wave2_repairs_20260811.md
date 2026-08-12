# wave2_repairs_20260811 — wave-3 repair-application session (2026-08-11/12)

*Applies EVERY repair in `STATUS_wave2.md` §2a (wp2-a2), §2b (wp3-a2) and
§2c (T2 maths-referee list) as errata, mirroring `repairs_20260811.md`'s
format. No existing file is modified (no-erasing rule): each erratum below
states the defective display in its host file and the replacement text; the
host drafts remain as shipped and must be read together with this file.
New/copied scripts live in `g2_scripts/campaign_20260811/wave2_repairs/`
(inventory §E), every one SAVED and RUN with output archived beside it
(`out_*.txt`). All new verdict arithmetic is exact integer/Fraction; floats
appear only where a shipped library is re-used unmodified (flagged inline).
This file also records the harness extension to `m = 540` (§D — the
STATUS_wave2 §5.2 optional item pre-clearing G4's `[401, 534]` part-(c)
band). Statuses: every repair here is text/label/rounding-level except the
three with mathematical content — B1 (P.7 rescope), C1 (T.10(2)
restatement), C3 (T.8'' proof route) — whose replacement proofs were
already supplied and script-verified by the referees; applying them moves
NO certified constant, threshold, lemma scope (beyond the stated rescopes),
or verdict (§E check).*

Sources applied: `referee_maths_wp2_a2.md` §4 (F1–F5),
`referee_numerics_wp2_a2.md` §4 (R-F1–R-F7), `referee_maths_wp3_a2.md` §4
(R1–R8), `referee_numerics_wp3_a2.md` §3 (F1–F8), `referee_t2_maths.md` §5
(items 1–8, findings M1–M8). Item numbering below follows STATUS_wave2's
consolidated lists.

---

## §A. wp2-a2 repairs (STATUS_wave2 §2a, items 1–11) — host `wp2_draft_a2.md`

**A1 [= maths F1 = numerics R-F1; the shared substantive one].** §0 item 1's
parenthetical "certified DECREASING in `m` on the stated range (unit-step to
3000, spot-checked to 10^4)" misdescribes the shipped NC-A3(3) grid.
*Erratum:* read "certified DECREASING in `m` on `[M(K), 3000]` (unit step to
1000, step 10 on (1000, 3000], NC-A3(3)) and at 10^4 (NC-A5(3));
independently extended by the numerics referee (report R1) at unit step on
[1000, 3000], step 20 on [3000, 10^4], and spot-decrease through
`m = 10^6`, no violation." This matches the draft's own §6 scope note and
§10 item 2; the stronger unit-step-to-3000 claim is TRUE (referee R1) but
was not what NC-A3(3) ran. No number moves.

**A2 [= maths F2].** The D.5 scope-note's exponent-audit parenthetical
"every row has a NEGATIVE net exponent except the pure-`alpha` quartic rows
(`ZI^4`-class), whose exponent is 0" is incomplete. *Erratum:* the
exponent-0 set (counting rule `2 + n_c + n_q - (p+q)/2`) is: the
`ZI^4`-class rows, AND the `ZR·ZI^2`-against-constant rows of WR (e.g.
`A4 A3^2`, `c = 3`, `T = 10`), AND WI's bare `A3^3` through the `|t|`-shift
in the pointwise bucket (`2 + 3 - (9+1)/2 = 0`). Conclusion unchanged — no
positive row anywhere, every row decreasing-to-limit
(`referee_maths_wp2_a2.md` §2.3 re-audit) — but any future Sturm pass for
the `m > 3000` tail must target THIS list, not the shorter one.

**A3 [= maths F3].** Theorem D.5 consumes `v > 0` (D.4(iii), clause
"`LFlow > 0`") for every `m >= M(K)`, verified pointwise only at
`m in {180, 181, 367, 400, 1000}` (NC-A4(3)). *Erratum (one sentence, add
to the §6 scope note / §10 item 2):* "`LFlow > 0` holds at every grid point
of NC-A3(3)'s monotonicity scan (the library returns None when
`LFlow <= 0`, so any violation would have aborted the scan) — i.e. its
certification status is the SAME grid class as the monotone-decrease
certificate, with worst margin `LFlow = 0.92237` (at the non-theorem point
`(K, m) = (4, 180)`); over theorem-used pairs the minimum is 0.96388."
Script: `w2r_rep3_wp2a2_rows.py` (R-F6 block) re-certifies

```
    LFlow(K=1, m=180) = 0.99248
    LFlow(K=2, m=181) = 0.98704
    LFlow(K=4, m=367) = 0.96388
    LFlow(K=4, m=180) = 0.92237
    min over theorem-used pairs = 0.96388 >= 0.9638: True
```

**A4 [= maths F4].** §5 Lemma D.4(ii) sign typo: "`phat(+-1) = Z(-+h)
P(-+h)`". *Erratum:* with `y = x h` the display is
`phat(+-1) = Z(+-h) P(+-h)`. Harmless (`Z` even, both `P(+-h) >= Pmin`).

**A5 [= maths F5, bookkeeping].** (i) NC-A6 (`wp2a2_nc6_zbar.py`), quoted
in §8 and load-bearing for D.5's `zbar < 1e-6` step, is added to the header
script list and the §8 script table. (ii) NC-A4(2)'s `(m, K) = (60, 4)`
row: the refined bound does not assemble there (lib returns None; printed
bound `inf`), so "measured <= bound" is vacuous at that point — consistent
with `M(4) = 367`, now stated. (iii) §2's NC-A3(1) wording: NC-A3 uses
`w in {K/2, K}`, not NC-A1's `{K/4, K/2, K}` — "on the same grids" is
corrected accordingly. (iv) §6's mixed-`m` table rows: superseded by the
genuine full rows in A6 below. (v) §0 item 4 now carries, at first use, §10
item 4's caveat: below `M(K)` the coverage is the harness's exact GROUND
TRUTH, not the analytic law.

**A6 [= numerics R-F2].** Theorem D.5's per-piece table rows "`181 2`" and
"`367 4`" silently mix m-values (box/far carry "(at 180)"/"(at 379)"
parentheticals but tail/den are ALSO borrowed — den 17.65 is the m = 180
value, den 1380.63 the m = 379 value — while only C_ker is the true M(K)
value). *Erratum:* replace those rows by the genuine full rows at the
theorem thresholds (`w2r_rep3_wp2a2_rows.py`, shipped lib unmodified):

```
      m  K    m2*box    m2*tail     m2*far      dbar    m2*den     m2*Cker2
    180  1   27.3882   1.66e-10   5.23e-05  5.35e-05    3.4951     30.8863
    181  2  191.1309   4.42e-08   1.81e-01  2.65e-04   17.6086    209.0224
    367  4  36059.3053   6.09e-13   1.93e-01  4.92e-03  1391.0887  37810.0442
    Cker(row) <= displayed headline 30.89/209.03/37811: True
```

The C_ker column reproduces NC-A3(5)'s 30.8863 / 209.0224 / 37810.0442
exactly; headline constants unchanged.

**A7 [= numerics R-F3].** §6's "`m^2 |Delta_ker|` is measured FLAT at
`1.374–1.386` over `m = 30..140` (wp2-b NC-W4(6))". *Erratum:* read
"1.374–1.391" (wp2-b's table has 1.391 at `m = 100`, `K = 1`; verified on
disk, `wp2_draft_b.md` line 552). No consequence (headline bound 30.89).

**A8 [= numerics R-F4; wrong-number class].** §7's aside "`C' = 42` moves
the center-margin crossover only to `m ~ 27 << 400`" was un-scripted.
*Erratum:* the exact solve (`w2r_rep2_crossovers.py`(b), NC-13's criterion
`1 - B_m - C'/m^2 >= 187/216`, exact `B_m` and the 1.08/m display flavor
both) gives:

```
    C'=  1: m0 =  9 (1.08/m flavor),  9 (exact B_m flavor)
    C'=  5: m0 = 12 (1.08/m flavor), 12 (exact B_m flavor)
    C'= 20: m0 = 17 (1.08/m flavor), 17 (exact B_m flavor)
    C'= 42: m0 = 23 (1.08/m flavor), 23 (exact B_m flavor)
```

NC-13's published `m0 = 9/12/17` at `C' = 1/5/20` reproduce exactly; the
aside should read "`m = 23` (script-checked)". The draft's "~27" erred in
the safe direction (23 <= 27 << 400); the aside's conclusion (finite side
already done by the harness) stands a fortiori.

**A9 [= numerics R-F5].** NC-A4(1)'s "PW = 187.265 (187.414, port -0.08%,
safe)" documentation. *Erratum (one sentence, into §5/lib docstring):* the
wp2a2 port's `P0_min` legitimately differs from wp2-b's because it uses the
valid, sharper h-term-free floor at `y = 0`; verified not a bug
(`referee_numerics_wp2_a2.md` §3.1).

**A10 [= numerics R-F6; unsafe-rounding class].** §5's "(NC-A4(3):
`LFlow >= 0.9224` at every `(K, m)` the theorem uses)": 0.9224 is the
NON-theorem point `(4, 180)`'s value 0.92237 rounded UP. *Erratum:* read
"`LFlow >= 0.9223` at every point printed, and `>= 0.96388` at every
`(K, m)` the theorem uses (`M(K)` thresholds)". Certified by
`w2r_rep3_wp2a2_rows.py`: "every value > 0.9223 (safe restatement): True ;
LFlow(4, 180) < 0.9224 (the draft's rounding was UP/unsafe): True".

**A11 [= numerics R-F7, hygiene, no text change].** NC-A4's `lam_solve`
Newton residual: to be asserted (`< 1e-20`) on any future re-run; the
referee's R4 re-ran the m = 60 scans with asserted residuals and reproduced
1.3863/4.0702/5.0216, so the shipped numbers stand. NC-A2(2)'s dead
`first_ok` branch noted, left as the historical FAIL-record.

---

## §B. wp3-a2 repairs (STATUS_wave2 §2b, items 1–10) — host `wp3_draft_a2.md`

**B1 [= maths R1; the only §B mathematical-content item].** Lemma P.7
clause 1 is over-scoped: as displayed the bracket argument does not deliver
the constant 6.85 for arbitrarily large `|w|` at fixed `m` (e.g.
`m = 30, |w| >~ 57`, where `1/(48 E(w) m^4)` is no longer `<= 0.0004`).
*Erratum (statement rescope):* Lemma P.7 clause 1 reads "for `m >= 30` and
`|w| <= 8`: `1 - s2/lambda >= 6.85 w^2 E(w)`" (equivalently, keep general
`w` but add the hypothesis `48 E(w) m^4 >= 1000`). The draft's own proof
already notes `E(w) >= 0.001` on `|w| <= 8` makes the bracket `>= 0.9996`;
clause 2 (the monotone floor `1 - s2/lambda >= 6.85 w0^2 E(w0)` for
`|w| >= w0`, via Lemma 3.3) is UNCHANGED and is the only clause consumed
downstream — everything consumed lives at `w0 <= 6`. No constant moves.

**B2 [= maths R2 = numerics F1; unsafe-rounding class, the E-decimal
reprints].** Four of the six "certified lower decimals" for `E(w0)` in the
P.7 table were `%.8f`-NEAREST rounded, i.e. rounded UP — not lower bounds.
*Erratum (reprint, certified):* the P.7 table's `E`-row reads

```
E(1) >= 0.00400692 , E(2) >= 0.00358718 , E(3) >= 0.00304035 ,
E(4) >= 0.00248992 , E(5) >= 0.00200652 , E(6) >= 0.00161240
```

(E(4), E(5) as originally printed). Certification is now EXACT-INTEGER, not
float: `w2r_rep1_e_decimals.py` brackets each `E(u)` between certified
rationals using integer arithmetic with rational pi bounds
(`314159265358979323846/10^20 < pi < .../847/10^20`), min/max over both pi
endpoints per term (no monotonicity assumption), plus a rigorous
integral tail bound:

```
E(1): 0.004006927541 <= E <= 0.004006927542 ; corrected print 0.00400692 is lower bound: True ; original print 0.00400693 NOT a lower bound (> E_hi)
E(2): 0.003587187143 <= E <= 0.003587187144 ; corrected print 0.00358718 is lower bound: True ; original print 0.00358719 NOT a lower bound (> E_hi)
E(3): 0.003040358636 <= E <= 0.003040358637 ; corrected print 0.00304035 is lower bound: True ; original print 0.00304036 NOT a lower bound (> E_hi)
E(4): 0.002489924424 <= E <= 0.002489924425 ; corrected print 0.00248992 is lower bound: True ; original print safe
E(5): 0.002006520248 <= E <= 0.002006520249 ; corrected print 0.00200652 is lower bound: True ; original print safe
E(6): 0.001612406722 <= E <= 0.001612406723 ; corrected print 0.00161240 is lower bound: True ; original print 0.00161241 NOT a lower bound (> E_hi)
```

*Propagation (all re-certified exact, same script):* the P.7 table's
deficit/rho rows read `deficit(1) >= 0.0274, deficit(2) >= 0.0982,
deficit(3) >= 0.1874, deficit(4) >= 0.27289, deficit(5) >= 0.3436,
deficit(6) >= 0.3976` and `rho(2) <= 0.9018`, **`rho(4) <= 0.72711`**
(certified `0.7271043`; the old print 0.7271 was unsafe by 4.8e-6) — the
`rho(4)` correction applies wherever it appears: the P.7 box, §0 item
"rho-side input", Theorem S's operating point and derivation note 1
(`0.7484/0.72711`), and the R2-row value, which reads `>= 1.0292` (was
1.0294):

```
deficit(2) >= 0.0982: True ; rho(2) <= 0.9018: True ; deficit(4) >= 0.27289: True ; rho(4) <= 0.72711: True
R2 chain: eps* = 1 - 1.02 rho = 0.258353 >= 20/79.5 = 0.251573 : True ;
R2 value (1 - 20/79.5)/rho = 1.029326 >= 1.0292: True ; >= 1.02: True
```

All downstream inequalities re-close (referee cross-checks 1.02928 and
1.029462 bracket the certified 1.029326). Note-2's first term reads
`>= 0.01627` (was 0.01628): "note-2 at m=401: 6.85 E(4)_lo (1 - 17 B_m -
C/m^2) = 0.016274 >= 0.01627: True ; full bracket = 0.013584 > 0: True".

**B3 [= maths R3 = numerics F4; the "~68" WRONG NUMBER].** Derivation note
2's "(NC-P4 prints the crossover: `m >= 63.3` ignoring the `(1 - 17B_m)`
factor, `m >= ~68` with it)" — "~68" came from no saved script and is
false. *Erratum:* read "`m = 82` (script-checked)". Exact scan
(`w2r_rep2_crossovers.py`(a), Fraction `B_m`, certified `E(4)` lower bound,
`C = 10.71`):

```
first positive m = 82 (draft said '~68'; repair value 82)
positive for all 82 <= m <= 5000: True
consumed claims: m=100: 0.003168 > 0: True ; m=401: 0.013585 > 0: True
companion (no (1-17B_m-C/m^2) factor): first m = 63
```

The consumed claims ("valid `m >= 100`"; positivity at 401) are true as
drafted; only the aside's number moves.

**B4 [= numerics F2].** P.7/§7's truncation claim "`< 2e-21`" for the
E-series partial sums is false by ~4 orders (the "3x first term" tail
heuristic is wrong for an `~n^-4` series). *Erratum:* in the shipped float
script's terms, read "truncation `< 2e-15` (float-summation dominated)".
Under this session's exact-integer replacement the point is moot: the
rigorous tail bound is `1.369e-17 < 2e-15` (and `< 2e-17`), with NO float
summation error (`w2r_rep1_e_decimals.py`(2)). Nothing downstream moves
(the corrected 8th-decimal prints of B2 already absorb every effect).

**B5 [= numerics F3 = maths R8-part; Lin double-count, safe direction].**
Theorem S's R3 row and §6.2 conclude
`>= 1 - B_m - [C_R^PT(4) + C_ker + Lin]/m^2`, but wp2-b defines
`C_R^PT = PW + T + Lin` (its 5.2985 = 4.9126 + 0.01402 + 0.3719), so `Lin`
is counted twice. *Erratum:* read `[C_R^PT(4) + C_ker]/m^2` with
`C_R^PT(4) = 5.30`, or equivalently spell out
`[PW + T + Lin + C_ker]/m^2 = [4.93 + 0.37 + C_ker]/m^2`. Safe direction
(the displayed budget merely over-charged by `0.37/m^2`); the bracket stays
positive either way (referee-verified exact with `C = 10.71`).

**B6 [= maths R4; one lattice point].** Theorem S's R3 row cites W.7, whose
hypothesis is `0 < |lam(k)| <= K/m`; at `N` even, `k = N/2` has `lam = 0`,
formally outside. *Erratum (one line, add to the R3 row):* "the exact
center `k = N/2` (`N` even) is covered by g1_draft_b Cor B.9 / Cor 2.3
(`m >= 180`) or by W.7's untilted limit." (Same note propagates to Prop
3.5(ii)'s closure statement — STATUS_wave2 §2 already carries it.)

**B7 [= maths R5].** "`eps(k) <= 0.0385` over EVERY interior `k`" (§0
item 2, §6.1.2): NC-P3(d)'s scan is `2 <= k <= N/2` (`k = 1` untested;
symmetric side implied). *Erratum:* read "over every `2 <= k <= N - 2`"
(by symmetry `a_k = a_{N-k}`); the numerics referee's independent
implementation confirmed the full-interior fact at m = 30/60/140 anyway
(`referee_numerics_wp3_a2.md` F6: eps <= 0.0385/0.0194/0.0084).

**B8 [= maths R6].** Theorem S's summary line "no condition other than
those two named open packages remains" is mildly stronger than §6.3's own
caveat (the R3 far bucket's `m_2(4) = 379` was a proxy-criterion number).
*Erratum (mirror the qualifier in the statement):* append to Theorem S's
statement: "— where the wp2-a condition includes its merged assembly
landing at threshold `<= 400` (or the harness being extended)".
*Synthesis discharge note (STATUS_wave2 §2b item 8):* substantively
discharged by the wp2-a2 merge — Theorem T.9-final's real threshold
`M(4) = 367 <= 400 < 401` replaces the proxy (no proxy criterion anywhere;
`referee_maths_wp2_a2.md` §1.6) — but this text repair applies to wp3-a2 as
written.

**B9 [= maths R7].** P.4(iii) uses the P.3(ii) floor at `j = 1` when
`k = 2`, outside P.3's stated range `2 <= k <= m`. *Erratum:* add "and
trivially at `k = 1`, where `Phi(1) = 1 - 1/m`."

**B10 [= maths R8 + numerics F5/F6/F7/F8; display trivia].**
(i) NC-P4's/Theorem S table's `c = 1` tilt-cap print "0.6931" is `log 2`
rounded DOWN — wrong direction for a cap; the text's 0.6932 is correct and
is the display to use (`0.69315 > 0.6931`). (ii) "17364x" reads "17363x"
(or ">= 1.7e4 x"): exact margin at `(1581, 1)` is
`1580^2 * 3167/(144*2*1581) = 17363 + 14921/28458 = 17363.524`
(`w2r_rep2_crossovers.py`(c): "17363 <= margin < 17364: True"); the
`(401, 7/10)` companion "1879x" is safe (exact 1879.056, referee F5).
(iii) §7's "Key verbatim excerpts" are relabeled "condensed excerpts", and
the editorial line "(eps never exceeds 0.25 at ANY interior k on the tested
range)" moves out of the quoted code block into prose (the fact itself is
true — referee F6's independent check). (iv) §2's constants table carries
the sentence: "table entries are nearest-rounded displays of exact
Fractions; all verdicts use the exact values" (referee F7's list: `C_A(1/4)`
5.923067, `C_d(1/2)` 1.805309, `C_A(7/10)` 20.649186, `C_A(1)` 34.920037,
`C_P(1)` 263.230377, `Phimin(1/4)` true 0.721956 — the last printed HIGH),
plus: "the omitted `sigma_1'` tail is ~1e-118, certified harmless."
(v) [F8, observation, no text change forced] §7's "82–90% capture" is
`w0 <= 4`-scoped (74.7% at `w0 = 6`); P.7's own text states the scope
correctly.

---

## §C. T2 maths-referee repairs (STATUS_wave2 §2c, items 1–8) — host `g2_draft_t2_20260803.md`

*This section is the pending "t2_repairs" application (STATUS_wave2 §3
"Remaining T2 bookkeeping"). With it, T.10(2) and T.8'' may be cited IN
THEIR REPAIRED FORMS below (never as displayed in the host). Verification:
the three referee scripts were COPIED unmodified into `wave2_repairs/`
(`refm_a_t8pp_t10.py`, `refm_b_chains.py`, `refm_c_identities.py`) and
RE-RUN this session (`out_refm_{a,b,c}_rerun.txt`); every quoted number
below reproduces the report's §6 excerpts.*

**C1 [M1 + M5-part + M7; T.10(2) — the FALSE-as-displayed clause].**
*Erratum (replacement statement, verified two-inclusion form):* in T.10(2)
replace `rho := 1 - 0.04 w_0^2` by **`rho := 1 - 0.022 w_0^2`**, and the
clause by: "for every `w_0 <= 1`, `m >= 30`: (i) `{sigma_lam^2 >= rho
lambda} subset {|w| <= w_0}` (so T.9's hypothesis holds on all of region 3
with `K = w_0`), and (ii) `{|w| >= 0.9 w_0} subset {sigma_lam^2 <= rho
lambda}` — the two hypothesis sets overlap in the annulus
`[0.9 w_0, w_0]`, relative width 0.1." Proof: one line from (T.4)'s two
proved sides — `deficit(w_0) >= 0.0270 w_0^2 > 0.022 w_0^2` and
`deficit(0.9 w_0) >= 0.0221 w_0^2 > 0.022 w_0^2`, plus deficit monotone
nondecreasing in `|w|` (merged draft Lemma 3.3). Re-run:

```
== (f) repair: rho := 1 - 0.022 w0^2 ==
  deficit(w0)  >= 0.02700 w0^2 > 0.022 w0^2 : True
  deficit(.9w0)>= 0.02210 w0^2 > 0.022 w0^2 : True
```

(and block (d) re-confirms the ORIGINAL `rho = 1 - 0.04 w_0^2` sets are
DISJOINT at all six `(m, w_0)` test points, `w* = 1.1502..1.1742 w_0`).
Also: correct `0.0332 -> 0.0347` in BOTH places it appears (the (T.4)-upper
constant is `0.0300(1 + 3/30 + 1/18) = 0.034667`, re-run block (e)); and
fix the undefined header symbol `m_0(i)` — the body proves (1) for
`m >= 53` and (2) for `m >= 30` (re-run block (h): `m^3/72 >= 2000` first
at `m = 53`). [Independent consistency: wp3-a2's P.7 gives the stronger
`1 - 0.0274 w_0^2` at `w_0 = 1` — B2's certified `deficit(1) >= 0.0274`.]

**C2 [M3; T.10(1)/§8-6 band label].** *Erratum:* the double-coverage band
label `[1/m, 3.7/m]` reads `[1/m, pi/m]` ("the bulk of the historical
hole"; `pi < 3.7`, re-run block (h)) — OR the sliver `(pi/m, 3.7/m]` is
closed by citing wp2-b Lemma W.1(i) (`1 - s2/lambda <= 0.0330 w^2` for ALL
real `w`; gives `s2 >= 0.548 lambda` at `w = 3.7`), with wp2-b's
MINOR_REPAIRS-citable status flagged. §8 item 6's repetition carries the
same edit.

**C3 [M2; T.8'' — statement true, displayed proof broken].** *Erratum
(replacement proof step, one line):* discard the route "`Var U_j^{lam} <=
E_lam U_j^2 <=` untruncated `E X^2`" (false: `E X^2 = q(1+q)/(1-q)^2 >
(1+1/lam)^2` for every `lam <= 0.31`; re-run block (a), 30 grid violations,
e.g. `lam = 0.1`: `190.3251 > 121`). Instead, by memorylessness the exact
mixture `law(X) = alpha law(U_j) + (1-alpha) law(j + X)`, `alpha = 1 -
q^j`, gives **`Var U_j <= Var X = q/(1-q)^2 <= (1+1/lam)^2`** (via
`1 - q >= lam/(1+lam)`, `q <= 1`): truncation lowers the VARIANCE. Re-run
block (b): "mixture identity max rel dev over grid: 7.116e-38 ;
VarU<=VarX everywhere: True ; 99.9167 <= 121.0000 : True". And the
conclusion display weakens by one: **`m_* >= sqrt(s2/m) - 2`** (the chain
delivers `-2`; `-1` is unproved — no grid counterexample, re-run block
(c), but not derived). Downstream exposure: none (T.8-final's (V) uses
`m_* >= m/pi - 1` from its own hypothesis).

**C4 [M8 + numerics-F1 interaction; T.9 §5 "fully proved" list].** The
`B_lam/B_m = 1 + theta 0.35 w^2` line is dropped from the "fully proved"
list. It is ALREADY replaced by Lemma T.9-Step2' (`repairs_20260811.md`
§T1: `|B_lam/B_m - 1| <= 0.362 w^2` on `|w| <= 1`, `m >= 30`, verified
SURVIVES by `referee_repairs_20260811.md`), which complies with M8's
caveat: the corrected inequality `(1-d)^{-2} <= 1 + 2d + 3.5d^2` must
carry `d <= 0.1` — it fails from `d ~ 0.107` (re-run block (g): FALSE at
`d = 0.120, 0.2, 0.4`; TRUE at `d = 0.05, 0.10, 0.107`), and the repairs
doc's version uses `d <= 0.033` — compliant. Alternative citation: wp2-b
Prop W.6 with its §2b caveats (grid-certified label; `c_w(4) = 1`, so
T.9's `c_w = 1/2` sub-claim holds for `K <= 2` only).

**C5 [M4; T.4' display].** *Erratum:* in the absolute-kappa_4 clause,
`1.18 -> 1.178` (or equivalently `/155 -> /154`): the displayed chain
`(1.18/600 + pi^2/2200) m^5 = 0.0064529 m^5` misses `m^5/155 = 0.0064516
m^5` by 1.24e-06, while the exact chain gives `0.0062948 m^5 <= m^5/155`
(re-run block (a) — claim true, display rounding fails its own target).
Margin note added: the kappa_3 `/284` chain closes with relative margin
only 2.2e-4 (re-run block (b): `0.00352035` vs `1/284 = 0.00352113`,
margin 7.8e-07 absolute); any future rounding touch should print `/283`.

**C6 [M5; (T.4a'') display].** *Erratum:* the numbered display's lower
coefficient `1 - u^2/25` reads **`1 - u^2/19`** (what the proof
establishes and every downstream use consumes; re-run refm_c block (c):
`240 E(u) >= 1 - u^2/19.7` holds on `(0, pi]`, `E` decreasing,
`E(pi)*240 = 0.71049`). The two abandoned false-start paragraphs
("increasing in u^2", corrected mid-page) are struck. The prose line
"[0.0270 w^2, 0.0332 w^2]" after (T.4) reads `0.0347` (per C1; the
draft's own §6 quote `.034667` is correct).

**C7 [M6; (T.6iii-final) upgrade — retires numerics F9].** The referee's
five-line constant chase (`referee_t2_maths.md` §2.7) is transcribed as
the proof: `c1 = 0.5938`, `|z_j| <= 0.0371`, `1/(2(1-z)) = 0.5193`, total
coefficient of `(m-1)^2 sigma^2 t^4` is `1/24 + 0.0458 = 0.0874 <= 1/6`
(re-run block (f): True). (T.6iii-final) is thereby PROVED as stated with
every step displayed; the "least rigorous PROVED item" flag is retired.

**C8 [item 8; numerics F-items].** The T2 numerics referee's F2 (r = 4
coefficient `2.611277e-04`, re-run refm_a/refm_b block (c)), F5
(`m >= 6`), F6 (`m >= 3` + direct `m = 2` check), F7, F8 were already
applied in `repairs_20260811.md` §C and verified SURVIVES; confirmed by
the maths referee where they touch mathematics. Nothing further to apply;
fold at paper-assembly.

---

## §D. Harness extension to m = 540 (STATUS_wave2 §5.2 optional item) — PROVED (exact finite computation)

`run_m540.py` is a copy of `harness_m200/run_m200.py` (same recurrences,
same six exact certificates C1–C6, verdict path byte-identical; only MMAX
default 540, extra checkpoint rows 400/401/534/535/537, and the docstring
changed). Exact integer/Fraction arithmetic in every verdict; floats
display-only. Purpose: with the crude `C_ker(4)` plug, the part-(c)
analytic bound `1 - B_m - C/m^2 >= 187/216` first holds at `m* = 535`
(grid flavor) / `537` (closed flavor) — archived
`status_wave2/out_status_wave2_checks.txt`:

```
    K=4 grid flavor   (37815.36)         m* = 535   (stays >= target beyond: True)   harness covers to 400: gap [401, 534]
    K=4 closed flavor (37997.84)         m* = 537   (stays >= target beyond: True)   harness covers to 400: gap [401, 536]
```

so exact coverage through `m = 540` closes BOTH gap bands `[401, 534]` and
`[401, 536]` with overlap: no uncovered `m` remains for G4's part (c) at
`K = 4` (this pre-clears the STATUS_wave2 §2 plug-note caveat; Theorem A =
F2(a) was never affected).

**Run record** (`results_m540.txt` beside the script): launched this
session; at this file's last edit the run had certified `4 <= m <= 476`,
every row PASS (C1 symmetry/positivity, C2 argmin central with the known
`m = 4` exception, C3 min = central ratio, C4 odd-`N` exact tie, C5
`varfit >= 187/216` with equality only at `m = 6`, C6 strict increase),
zero failures — sample tail row: `476 113050 56525 56525 3.3200e-07
0.9977327178 1.07923 PASS`. The completion block (rows through 540, the
"# OVERALL" line, and the checkpoint varfit list including
400/401/534/535/537) is written by the run into `results_m540.txt`; the
session-close summary reports the final OVERALL verdict. Any consumer of
the `[401, 540]` band must check that `results_m540.txt` ends with
"# OVERALL: PASS" (rows: 537, failures: 0).

---

## §E. Session verification: scripts, outputs, and the no-digit-moved check

**Script inventory** (all under
`g2_scripts/campaign_20260811/wave2_repairs/`, each with archived output):

| script | new/copy | verifies | output | verdict |
|---|---|---|---|---|
| `w2r_rep1_e_decimals.py` | new (exact integer) | B2 (E-decimal reprints + full propagation chain), B4 (truncation restatement) | `out_w2r_rep1.txt` | PASS |
| `w2r_rep2_crossovers.py` | new (exact Fraction) | B3 (the "~68" -> 82 fix), A8 (the "m ~ 27" -> 23 fix + NC-13 9/12/17 reproduction), B10(ii) (17363x) | `out_w2r_rep2.txt` | PASS |
| `w2r_rep3_wp2a2_rows.py` | new (imports shipped `wp2a2_lib2` unmodified — library floats are the draft's own certified-display convention) | A6 (genuine full rows at 181/367), A3 + A10 (LFlow provenance) | `out_w2r_rep3.txt` | PASS |
| `refm_a_t8pp_t10.py` | copy of `referee_t2_maths_scripts/` | C1, C2, C3, C4 (M1/M2/M3/M8 blocks) | `out_refm_a_rerun.txt` | reproduces report §6 |
| `refm_b_chains.py` | copy of `referee_t2_maths_scripts/` | C5, C7, C1-part (M4/M6, 0.034667, m=53, pi<3.7) | `out_refm_b_rerun.txt` | reproduces report §6 |
| `refm_c_identities.py` | copy of `referee_t2_maths_scripts/` | C6 (`/19` kernel bound), T2 identity re-checks | `out_refm_c_rerun.txt` | reproduces report §6 |
| `run_m540.py` | copy of `harness_m200/run_m200.py` (MMAX 540, extra checkpoints; verdict path unchanged) | §D | `results_m540.txt` | see §D |

**No-certified-digit-moved check.** Every repair applied above is one of:
(i) a text/label/scope alignment (A1–A5, A9, A11, B1, B6–B9, B10(iii)(iv),
C2, C4, C6-strikes, C8); (ii) a SAFE-direction reprint of an unsafe
rounding, certified by exact arithmetic this session (A10, B2, B4, B10(i)
(ii), C5); (iii) a wrong un-scripted aside number replaced by a scripted
exact value, with the consumed claims re-verified true (A8: 27 -> 23; B3:
~68 -> 82; A7: 1.386 -> 1.391); (iv) a supplied-and-verified replacement
statement/proof for an item consumed NOWHERE in the campaign chain (C1:
`rho = 1 - 0.022 w_0^2`; C3: memorylessness route, `-1 -> -2`); or (v) a
genuine-data replacement for borrowed table cells with the HEADLINE
constants unchanged (A6: C_ker 30.8863/209.0224/37810.0442 reproduce). No
theorem constant, threshold `M(K)`/`m_p`/`m_2(K)`, region boundary,
conditional, or verdict moved. The two theorem-statement rescopes (B1:
P.7 clause 1 to `|w| <= 8`; C3: `-2`) strictly contain every downstream
use (P.7 consumed at `w0 <= 6`; T.8'' consumed nowhere).

**Citability effect.** With this file: wp2-a2 and wp3-a2's §2a/§2b repair
lists are DISCHARGED (pending a referee pass on this file, mirroring
`referee_repairs_20260811.md`); the T2 §2c list is APPLIED, so T.10(2) and
T.8'' are citable in their §C repaired forms (still: never as displayed in
the host); STATUS_wave2 §4 item 1 ("apply the wave-2 repair lists") is
done. The single open mathematical statement for Theorem A remains wp4's
`CL(79, 20, 0.89)` — untouched by this session, as intended.

*End of wave2_repairs_20260811.md.*


