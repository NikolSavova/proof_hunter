# wave4_sl4p_repaired — SL4' repaired: the kernel-weighted honest ledger, referee-corrected (wave 5)

*Wave-5 repair deliverable, F2 campaign, 2026-08-12. This file is the
corrected, self-contained replacement text for `wave4_sl4p_20260812.md`
("the original"), executing STATUS_wave4 §2c in full: every finding F1–F7 of
`referee_numerics_wave4_sl4p.md` ("the referee") is resolved here, F1 by the
referee's route (a) as STATUS_wave4 §2c.1 directs, and the two
theorem-statement defects (F1/F2) are additionally PROVED MOOT in the CL
assembly at the shifted threshold `m >= 561` (§6). Unchanged material
(Lemmas SL4'.1–.7 and their proofs, the seven-row ledger, the INFL/QUADF
budget) is cited to the original rather than re-typed; everything the
referee flagged is restated here in corrected form, so a consumer needs the
original only for the unchanged proofs. Blind protocol: per STATUS_wave4
this wave may consume the now-citable wave-4 outputs — Theorem SL3'
(`wave4_sl3p_20260812.md` + `wave4_sl3p_ROUTE_20260812.md`, two-referee
MINOR_REPAIRS) and the SL-sliver closure (`wave4_sliver_20260812.md`,
two-referee MINOR_REPAIRS) — and this file does so; `g2_draft_t1_20260803.md`
remains unread; `gamma = 1/8` is not re-litigated. New scripts (SAVED and
RUN 2026-08-12, outputs archived beside them, quoted verbatim in §7):
`g2_scripts/campaign_20260811/wave5_sl4prepair/sl4pr_common.py` (byte-
faithful copy of the prover's referee-validated row machinery),
`sl4pr_a_trapezoid.py`, `sl4pr_b_grid.py`, `sl4pr_c_xtail.py`,
`sl4pr_d_misc.py` (outputs `out_sl4pr_{a,b,c,d}.txt`). No existing file
modified.*

**Bottom-line status: PARTIAL — Theorem SL4'-R (§4) is PROVED MODULO THREE
named hypotheses (SL1'-w, SL4'-E, SL4'-X), one fewer than the original's
four: the original's SL3'-w is DISCHARGED by Theorem SL3' (two-referee,
flagged-certificate class), which delivers `gamma*(W1–W4) =
0.42/0.42/0.40/0.40` — exactly the levels the certified ledger was computed
at, which is what resolves F1 (route (a)).** The corrected W1 trapezoid is
`w in (4, w†(m))`, `m in [401, 462]` with `w†(401) = 4.095`, `w†(462) =
4.00021` (F2 resolved; script [A]). Three further things are new here, all
in the closing direction: (i) **mootness with proof** — the corrected
trapezoid (under EITHER F1 repair route) lies strictly inside the exact
harness coverage `[401, 560]`, so at the CL assembly's operative threshold
`m >= 561` (Cor SLV.3) the sliver exception is EMPTY (§6); (ii) a **new
analytic W1 tail** (Lemmas R.1/R.2, script [C]): for ALL `m >= 700` and ALL
`w in (4, 5]` the W1 row closes by closed-form bounds consuming NO SL4'-X —
so SL4'-X's load-bearing scope in the CL assembly shrinks to the finite
grid range `m in [561, 699]`; (iii) the grid closure of that range (Fact
R.G, script [B]: 25,122 probes, 0 failures, 0 SL4'-X violations). The
conditional surface of CL(79, 20, 0.89) at `m >= 561` is now exactly:
SL1'-w + SL4'-E + SL4'-X(`m <= 699`), plus this file's own referee debt
(§8).

## 0. Inputs, spec, and referee status of this file

Notation, target spec CL(79, 20, 0.89), frame, and the kernel decomposition
are the original's §0–§1 verbatim (composite §0 notation; `w = m lam`,
`A = lam^2 s2`, `u = 1/A`, bands W1–W7, split core/mid/crossover/far).

Consumed as PROVED at two-referee MINOR_REPAIRS:

- **[A2], [A3], [C.1], [W.6]** — via `wp4_draft_composite.md`, exactly as
  the original's §0 lists them (banded `c_A` floors incl. W7's certified
  `0.852716`; tier-1 `c1 = 0.1317` / tier-2 `c2 = 0.0871`; far floor
  `0.0741`; `t_0 <= 1.074 lam` (Lemma SL3.C); `s2 <= m/(4 sinh^2(lam/2))`;
  the W.6 crossover exponent `x(w, tau)` used pointwise on W1).
- **[SL3']** *(new consumption, replaces the original's hypothesis SL3'-w)*
  **Theorem SL3'** (`wave4_sl3p_20260812.md`, with
  `wave4_sl3p_ROUTE_20260812.md` and both its referee reports): for
  `m >= 401`, `|lam| in (4/m, 0.89]`, `0 < t <= 0.8 |lam|`:
  `|phi_lam(t)| <= exp(-gamma*(W) s2 t^2)` with `gamma* =
  0.42/0.42/0.40/0.40/0.38/0.34/0.32` (W1..W7). This file consumes ONLY the
  W1–W4 values `0.42/0.42/0.40/0.40` (the ledger's mid slot on W1–W4; W5–W7
  ride PROVED [A3] tier-1 and never touch SL3'). Class flag inherited
  honestly: SL3' is proved modulo its flagged finite monotone-cell
  certificates (E.5.3, E.6.A/B/C — the campaign's accepted grid-certificate
  class), and its own maths referee's R1 warns the worst certified margin
  of that certificate is 1.30x at W7's crossover — consumers of THIS file
  inherit that class flag but spend none of that margin (the ledger's mid
  entries at `gamma* >= 0.40` have 1e2x–1e6x slack; original table).
- **[SLV]** *(new consumption)* Fact SLV.2 / Cor SLV.3
  (`wave4_sliver_20260812.md` + both its referees): the exact integer
  harness PASSes for every `m in [4, 560]` (C2/C3 with the known `m = 4`
  exception, per the OVERALL line quoted in §6), and CL's proof obligation
  restates as `m >= 561`. Since the sliver note's own §3.1 repair (m1) was
  still pending at its filing, script [D6] here INDEPENDENTLY re-parses
  both results files (`wave2_repairs/results_m540.txt` rows 4..481,
  `harness_m560/results_m560.txt` rows 482..560): 557 data rows, zero
  non-PASS, zero gaps in `[4, 560]`, and quotes the completed run's
  `# OVERALL: PASS` line verbatim (§7) — so nothing here waits on the
  sliver note's mechanical insert. Provenance caveat inherited: rows
  4..481 are the honored `results_m540.txt` rows (wave2_repairs referee
  debt now discharged single-verifier per `referee_wave2_repairs.md`;
  fresh-rerun flag f1 as in STATUS_wave4 §2a.6).

Referee status of THIS file: **zero referees** (new file; maths + numerics
owed under house rules — §8). The original's single numerics referee graded
MAJOR_ISSUES with fully-quantified repairs and re-certified both F1 repair
routes; every number below that overlaps the referee's is quoted against
their archived output and reproduced by this file's own scripts.

## 1. Referee repair map (the whole point of this file)

| Finding | Class | Resolution here | Evidence |
|---|---|---|---|
| **F1** (MAJOR: stated `gamma*(W1) >= 0.25` does not support the quoted trapezoid) | hypothesis/certification mismatch | **Route (a)** + upgrade: the SL3' input is now the PROVED Theorem SL3' at `gamma*(W1) = 0.42` — hypothesis, ledger, and trapezoid are all at 0.42; the "0.25-class suffices" remark is rescoped to W2–W4 (and to `w >= 4.14` on W1) in §2; route (b)'s numbers are kept on record and ALSO mooted (§6) | §2, §5.1; scripts [A1]/[A3]; referee E1–E3 reproduced |
| **F2** (trapezoid m-range `[401, 461]` off by one) | theorem-statement constant | corrected to **`[401, 462]`**; `m = 462` carries the micro-window `(4, 4.00021]`; first sliver-free `m = 463` (verified at `w = 4.0` limit, `4+1e-9`, `4+1e-7`); handoff note: any harness closure must cover `m = 462` — the actual coverage is 560 | §5.1; script [A2]; referee B2/B3 reproduced |
| **F3** (eta "never above 0.65" fails off-sample) | claim scoping | corrected to "**never above 0.66; worst 0.6579 at the W1 right edge `w = 5`**" (`m = 401/402`; `0.65734` at `m = 1000`); measured on the referee's missed corners incl. `w = 4.001` and the band edges; 34% headroom to the actual budget, `kappa_4 > 0` everywhere | §2 (SL4'-E); script [D1] |
| **F4** (C5*-slack remark conditioned on `w = 4.30`) | claim scoping | remark rescoped: W1's `C5* = 0.4` acceptance holds at `w = 4.30` but FAILS at the sliver edge (`row(4.10, 0.4) = 1.4695`); slack range corrected to **1.6x–8x** (W6b = 1.6x); W5's acceptance stated as 0.15 (its ledger value; the 0.10 was the block-[4] grid's next point) | §2 (SL1'-w); script [D5] |
| **F5** (`efac` "iff 0.8464" false) | wrong constant, safe direction | corrected: `efac(C5*) <= e` **iff `C5* <= 4(1 - e^{-1/4}) = 0.88480`**; `0.8464` is kept as the SAFE sufficient cutoff the lemma actually uses (`efac(0.8464) = 2.58829 < e`) | §4 note; script [D2] |
| **F6** (Lemma SL4'.8 display: "A >= 32" false; increasing-entry rule imprecise) | lemma statement | Lemma SL4'.8 restated (§3): dec entries nonincreasing on the USED range `A >= 112.28` (tier-1 mid's true peak `A ~ 36.7`, pure-form sufficient threshold `6/g = 45.56`); increasing entries explicitly require `e_i(A)/A` nondecreasing (far exactly linear; W1's X `~ A^{5/2}`) | §3; script [D3] |
| **F7** ("share 0.68" unreproducible) | diagnostic number | RETIRED and replaced by the decomposition with an explicit convention: at `(w, m) = (4.05, 401)` the row total is `1.3911` with X-share `0.99538`, far-share `0.12144`, dec-share `0.27429`; `m x(4.05, 0.8) = 7.6453`; the crossover-limited diagnosis stands | §5.5; script [D4]; referee D1 matched |
| F8 (record-only) | — | folded in: `w†(401) = 4.095` (3 dp) used directly; far threshold "m >= 75" kept with its `74.224` derivation shown; W5 range clause added; `19.78 <= 20` and `3.57x` conventions unchanged | §5.1, §3; scripts [A1]/[D3]/[D5] |

Nothing else in the original moved: the seven ledger rows, the slot
constants, INFL/QUADF, and the W2–W7 verdicts are unchanged (and were
verified by the referee to `< 5e-5`, thin margins to dps 100).

## 2. The hypotheses consumed (corrected §3 of the original)

**(SL3' input) — DISCHARGED, no longer a hypothesis.** The mid slot on
W1–W4 consumes Theorem SL3' at `gamma* = 0.42/0.42/0.40/0.40` — the exact
values the certified ledger, the `w†(m)` trapezoid, and the block-[1] rows
were computed at (prover script `sl4p_nc1_ledger.py` BANDS table; referee
§2 F1 confirmed the table's W1 mid entry `4.47e-03` is the 0.42 value).
This is referee route (a) with the hypothesis not merely restated but
discharged. W5–W7 use PROVED [A3] tier-1 (`c1 = 0.1317`) — no SL3'
dependence at all. *Robustness remark (F1-rescoped, evidence referee E5 +
original block [4] + script [A3]): the W2–W4 rows would in fact accept
weakened levels `0.25/0.20/0.15`; on W1 the weakened `0.25` suffices only
for `w >= 4.14`-class (referee E1: `row(4.12; g=0.25) = 1.0533` FAIL,
first PASS `w = 4.14`), with trapezoid `(4, 4.135] x [401, 469]` (script
[A3]: `w†(401; 0.25) = 4.135`, first full-closure `m = 470`) — kept on
record because §6's mootness covers BOTH routes.*

**(SL1'-w) Weakened banded core model. CONJECTURED** — statement unchanged
from the original §3(i)/(ii): `|kappa_3| <= R31*(W) s2/lam`, `kappa_4 <=
R42*(W) s2/lam^2` with `R31* = 1.0/1.2/1.5/1.7/2.0/2.1/2.2`, `R42* =
0.8/1.4/2.6/3.5/5.2/6.0/6.6` (truth at the W7 deep corner 2.1215/6.3552,
headroom 3.7%/3.9%, geometric limits 2.1303/6.4113 — the F2-corrected
margins, consumed at face value); `|R5(t)| <= C5*(W) s2 t^5/lam^3` on
`[0, lam/2]`, `C5* = 0.05/0.06/0.08/0.10/0.15/0.25/0.80`. *Acceptance-slack
remark, F4-corrected (scripts [D5], original block [4]): the ledger would
accept `C5*` up to `0.4/0.2/0.4/0.4/0.15/0.4/0.8` band-wise — slack
**1.6x–8x** on W1–W4 and W6b (W6b is the 1.6x: `row(W6b; C5*=0.4) =
0.89301` PASS), W5 and W7 at their ledger values (W5's acceptance is 0.15,
its ledger value — `row(W5; 0.15) = 0.98909` PASS, `row(W5; 0.20) =
1.0095` FAIL; the block-[4] print `0.10` is that grid's next point below).
The W1 slack is NOT uniform down to the sliver edge: `row(w=4.10, C5*=0.4)
= 1.4695` FAIL vs `row(w=4.30, C5*=0.4) = 0.96081` PASS — the `0.4`
acceptance on W1 is a `w = 4.30`-class statement.*

**(SL4'-E) Computed-eta pricing. CONJECTURED (measured; F3-corrected
headline).** Statement unchanged: `|eta| <= [R42*(W)/2 + 0.3 (R31*(W))^2 +
lam^2/2] u`. Measured evidence now includes the band RIGHT edges and
missed corners (script [D1], reproducing referee C2/C3): worst ratio
measured/priced = **`0.6579` at the W1 right edge `w = 5.0`** (`m = 401`
and `402`; `0.65734` at `m = 1000`; the prover's 17-point worst `0.6432`
at `w = 4.9` was an interior sample) — i.e. **never above 0.66 of its
budget** (34% headroom), and `kappa_4 > 0` at every probed point including
all edges. What a proof needs: unchanged (exact `qhat` algebra + SL1'-w(i)
+ the `kappa_4 >= 0` sign lemma; natural home SL1').

**(SL4'-X) W1 crossover certificate. CONJECTURED (grid-verified) — scope
SHRUNK by this file.** Statement unchanged: `x(w, tau)` nondecreasing in
`tau` on `[0.8, tau_0/lam]` (W1 only; it justifies the left-endpoint upper
sums in `X_w6`). Evidence: the orphan's grid + the prover's per-evaluation
flag + the referee's 6000-point audits at 8 adversarial points (0
violations, min increment `>= 1.7e-3`) + this file's script [B] flag at
every one of its 25,122 W1 evaluations (0 violations). NEW: Lemma R.2 (§5.4)
closes W1 for ALL `m >= 700` WITHOUT SL4'-X, so SL4'-X is consumed only by
W1-row evaluations at `m <= 699`; in the CL assembly at the shifted
threshold its load-bearing scope is exactly **`m in [561, 699]`** (§6).
What a proof needs: unchanged (elementary-calculus interval certificate,
half a session).

## 3. Lemma SL4'.8 restated (the SHARE criterion, F6-corrected)

**Lemma SL4'.8' (share criterion).** By [A2]/[C.1] the true `A` of any
in-band `(k, m)` lies in `[c_A†(W) m, m]`. Suppose the u-unit entries split
as (dec) entries `e_i` nonincreasing in `A` on `[c_A†(W) m, m]`, and (inc)
entries `e_j` with **`e_j(A)/A` nondecreasing** on that range. Then the CL
requirement `|s2(r-1) - 1| <= 20/min(m, s2) = 20/m` is implied by

```
share(W, m) := [ sum_dec e_i(c_A† m) ] / (20 c_A†) + [ sum_inc e_j(m) ] / 20  <=  1/(1 + QUADF) .
```

*Proof.* An entry's budget ratio is `e(A) u m/20 = [e(A)/A] (m/20)`. For a
dec entry, `e(A)/A` is a product of two nonincreasing positive factors, so
its max on the range is at `A = c_A† m`, value `e_i(c_A† m)/(20 c_A†)`
after the `m/20`. For an inc entry the hypothesis puts the max at `A = m`,
value `e_j(m)/20`. Sum. ∎

*Classification and validity ranges (F6-corrected; script [D3]):* the dec
entries are main/R5/cube/cross/mid/X-tier-2 and their den partners. The
`1/sqrt(A)` entries (R5/cube/cross and dens) are globally decreasing; the
tier-1 mid entry `A^{3/2} e^{-gA/4}(1 + 2/(gA))/(4g)` at `g = 0.1317`
peaks at `A ~ 36.7` (so the original's "decreasing on `A >= 32`" was
false there — referee F6(i)) and is decreasing for `A > 6/g = 45.5581`
(pure-form threshold; the Mills factor is itself decreasing, so this is
sufficient); the tier-2 X entry (`~ A^{3/2} e^{-0.64 c2 A}` times a
decreasing Mills factor) is likewise decreasing for `A > 1.5/(0.64 c2) =
26.9087` (script [D3]); `main` is `A`-free (trivially admissible). The used range is `A >=
0.28*401 = 112.28`, on which EVERY dec entry is additionally
scan-verified nonincreasing (`[112, 3000]` step 1, script [D3]: all True;
beyond 3000 the analytic thresholds govern). The inc entries are far (EXACTLY linear in `A`:
`e/A` constant, hence nondecreasing) and W1's W.6-crossover
(`~ A^{5/2}`: `e/A ~ A^{3/2}` nondecreasing) — referee F6(ii)'s condition
holds for both, which is what the original's proof line "prefactor `A`
resp. `A^{5/2}`" was gesturing at, now stated as the hypothesis. The far
entry's `m`-decrease: `m^{5.5} e^{-0.0741 m}` decreasing iff `m >
5.5/0.0741 = 74.224` ("for `m >= 75`" safe). ∎

## 4. Theorem SL4'-R (corrected statement) and the unchanged ledger

**Theorem SL4'-R (kernel-weighted honest ledger; conditional;
F1/F2-corrected).** *Assume SL1'-w, SL4'-E, and — for W1 rows with
`m <= 699` only — SL4'-X (§2). Then, consuming Theorem SL3' ([SL3'], §0)
and [A2]/[A3]/[C.1]/[W.6], for every `m >= 401` and every interior `k`
with `lam(k) in (4/m, 0.89]`, `w = m lam(k)`, EXCEPT `(w, m)` in the
trapezoid*

```
T := { (w, m) :  4 < w < w†(m) ,  401 <= m <= 462 } ,
w†(401) = 4.095 ,  w† nonincreasing on the full integer grid ,  w†(462) = 4.00021 ,
T is empty for m >= 463 ,
```

*the CL(79, 20, 0.89) conclusion holds:
`s2(r(k) - 1) = 1 + theta 20/min(m, s2)`, `|theta| <= 1` (both tilt signs
via the mirror; `s2 >= 141.7497 > 79` by [A2](iii)).*

*Proof.* Identical to the original's §4 proof (kernel identity SL4'.1,
honest transfer SL4'.2, slot Lemmas SL4'.3–.5, INFL/QUADF SL4'.6–.7,
share criterion via Lemma SL4'.8' above), with the mid slot on W1–W4 now
priced by Theorem SL3' instead of a hypothesis, and with the W1
`m`-quantifier discharged by the three-piece ladder of §5: trapezoid
complement on `[401, 462]` (script [A]), Fact R.G on `[463, 699]` (script
[B], grid class), Lemma R.2 on `m >= 700` (analytic, no SL4'-X). The
W2–W7 rows are certified at `m = 401` (original block [1], referee-
rebuilt) and every one of their entries is closed-form nonincreasing in
`m` on the used range (§3 + [D3]; referee B4's full integer grid to 2000:
0 violations). ∎

The seven-row ledger, its row values (worst W5 `0.9891`, W7 `0.9808`,
dps-100-robust per the referee), the per-row dependency brackets, and the
effective-constant remark (`20 * 0.9891 = 19.78 <= 20`) are the original's
§4 UNCHANGED — with one relabel: the mid-slot bracket `[SL3']` on W1–W4
now denotes the PROVED input (flagged-certificate class), not a
hypothesis. The updated per-row conditional surface: **W2–W7 rows: SL1'-w
+ SL4'-E; W1 rows: SL1'-w + SL4'-E + (m <= 699 only) SL4'-X.** Note on
Lemma SL4'.3 (F5): its display should read `efac(C5*) <= e iff C5* <=
4(1 - e^{-1/4}) = 0.88480` (script [D2]: `efac(0.8464) = 2.58829 < e`,
`efac(0.88479687) = 2.7182818`); the lemma's working cutoff `C5* <=
0.8464` is kept (safe, sufficient), and W7's `C5* = 0.80` sits under it.

## 5. The W1 closure ladder (corrected sliver + two new rungs)

### 5.1 The corrected trapezoid on `[401, 462]` (F1 + F2; script [A])

`w†(m)` = least `w` on a step-0.001 grid with the W1 row PASS, computed for
EVERY integer `m in [401, 462]` at the ledger's `gamma*(W1) = 0.42`
(script [A1], verbatim):

```
  m=401: w_dagger = 4.095   (row at w_dagger = 0.999182)
  m=410: w_dagger = 4.075   ...   m=430: w_dagger = 4.042   ...   m=450: w_dagger = 4.015
  m=461: w_dagger = 4.002   (row at w_dagger = 0.994158)
  m=462: w_dagger = 4.001   (row at w_dagger = 0.99262)
  w_dagger nonincreasing over the FULL integer grid m = 401..462: True
  w_dagger(462) refined (step 1e-5) = 4.00021  [referee B2b: 4.00021]
```

Since the row PASSes at the grid value, the true crossing sits at or below
it: `T` (defined with these `w†`) is a SUPERSET of the true exception set
— the safe direction for an exception clause. The `m`-range is `[401,
462]`, NOT the original's `[401, 461]` (F2): script [A2], verbatim:

```
  w = 4.0 (limit): first PASS m = 463   [461:1.01282F  462:1.0019F  463:0.991128P  464:0.980515P]
  w = 4+1e-9: first PASS m = 463        w = 4+1e-7: first PASS m = 463
```

`m = 462` carries the nonempty micro-window `(4, 4.00021]`. **Handoff
statement (referee F2's load-bearing point): a finite closure of this
trapezoid must cover `m = 462` — coverage to 461 would NOT close CL.** The
actual harness coverage is 560 (§6), with 98 rows to spare. The referee's
one-crossing scan (B1: no re-failure above `w†` for any `m in [401, 480]`,
full scans to `w = 5.00`) and their B4 full-integer-grid `m`-monotonicity
stand as the shape evidence; `w†(401) = 4.095` is the 3-dp value (their
B2), with the original's `4.10` the 0.01-grid print (safe direction).

Route-(b) record (F1; script [A3], verbatim): `w†(401; gamma* = 0.25) =
4.135`, `first full-closure m at w -> 4+ under gamma* = 0.25: 470` — the
referee's E2/E3 exactly; kept because §6's mootness covers both routes.

### 5.2 Fact R.G (grid closure of `m in [463, 699]`, all `w in (4, 5]`; script [B])

**Fact R.G.** For every integer `m in [463, 699]` and every `w` in the
106-point probe set `{4+1e-9, 4+1e-7, 4+1e-5, 4.0001, 4.001, 4.005} u
{4.01, ..., 5.00 step 0.01}`, the W1 row is `<= 1`; the worst value over
all 25,122 probes is `0.991128` at `(m, w) = (463, 4+1e-9)`; the
SL4'-X monotone-in-tau flag holds at every evaluation; every one of the
106 `w`-columns is nonincreasing in `m` over the full integer range.
Script [B], verbatim:

```
  FAIL count over all 25122 (m, w) probes: 0
  X_w6 monotone-in-tau flag violations (SL4'-X audit, 25122 evaluations x 60 cells): 0
  overall max row on the grid: 0.991128 at (m, w) = (463, 4.0)
  m=463: fails on scan = 0;  max over scan = 0.981966 at w = 4.001;  edge row(4+1e-9) = 0.991128  (margin 0.008872)
  m=561: fails on scan = 0;  max over scan = 0.422318 at w = 4.001;  edge row(4+1e-9) = 0.424939  (margin 0.5751)
  m=699: fails on scan = 0;  max over scan = 0.260946 at w = 4.001;  edge row(4+1e-9) = 0.261345  (margin 0.7387)
  columns: 106;  nonincreasing-in-m violations: 0
```

(The `[B2]` lines are the step-0.001 fine scans at the three sentinels;
the output's argmax print `4.0` is the 8-significant-digit rendering of
the probe `4 + 1e-9` — the open-edge probe, not `w = 4` itself.)
Class: grid certificate over the `w`-continuum (the campaign's accepted
class; the `m`-quantifier is complete — every integer — and the `w`-max
sits at the open edge `w -> 4+`, probed to `4 + 1e-9`, with the fine scans
and the referee's one-crossing shape as interpolation evidence). The
margin at the single thin point `(463, 4+)` is 0.9%; from `m = 470` it
exceeds 8%, and at the CL-operative `m = 561` it is **57.5%**. Consumes
SL1'-w, SL4'-E, [SL3'], and SL4'-X (the left-endpoint sums).

### 5.3 Lemma R.1 (crossover-exponent floor; new; script [C1])

**Lemma R.1.** For all `m >= 561`, `w in (4, 5]`, `tau in [0.8, 1.074]`:
the [W.6] exponent satisfies `x(w, tau) >= 0.0176`, where `x = ((M-1)/(2M))
(log(1+r) - r/M)`, `M = m sin(tau lam/2)`, `r = sin^2(tau lam/2) /
sinh^2(lam/2)`, `lam = w/m`. *(No SL4'-X input — this is a pointwise floor,
not a monotonicity claim.)*

*Proof.* Set `theta = tau lam/2 <= 1.074 * 2.5/561 = 0.0047861`. Elementary
brackets valid there: `sin(theta) >= theta(1 - theta^2/6)` with
`theta^2/6 <= 3.818e-6 <= epsM := 4e-6`; `sinh(x) <= x(1 + x^2/5)` for
`0 < x <= 1` (from `sinh x = x(1 + x^2/6 + x^4/120 + ...) <= x(1 +
(x^2/6)/(1 - x^2/20))` and `x <= 1`) with `(lam/2)^2/5 <= 3.972e-6 <=
epsS := 4e-6`; hence for
`w > 4`: `M >= (tau w/2)(1 - epsM) >= 2 tau (1 - epsM) > 1`, and
`r in [tau^2 (1 - eps_r), tau^2]` with `eps_r := 1.7e-5 >=
1 - (1-epsM)^2/(1+epsS)^2` (script [C1]: `0.9999840001 >= 0.999983`).
Both factors of `x` are positive and increasing in `M` (`(M-1)/(2M) = 1/2
- 1/(2M)`; `-r/M`), and the `r`-interval depends only on `tau`; so on a
tau-cell `[tau1, tau2]`, with `M1 := 2 tau1 (1 - epsM)`,

```
x >= (1/2 - 1/(2 M1)) * ( log(1 + tau1^2 (1 - eps_r)) - tau2^2 / M1 ) ,
```

each factor minimized separately (both positive). Evaluating on 548 cells
of width 5e-4 covering `[0.8, 1.074]` (script [C1], verbatim):

```
  cells: 548 (width 0.0005);  all cell brackets positive: True
  min cell lower bound = 0.0176601 at tau-cell [0.8, 0.8005]
  CERTIFIED: x(w, tau) >= 0.0176 for all m >= 561, w in (4, 5], tau in [0.8, 1.074]: True
```

The floor is tight at the `(w -> 4+, tau = 0.8)` corner (true value there
`0.0177554` at `m = 561`). Class: mpmath dps-40 point evaluations of
elementary closed forms with stated safe epsilons (house `sl3_nc1` class);
every inequality direction is rigorous. ∎

### 5.4 Lemma R.2 (analytic W1 tail: `m >= 700`, ALL `w in (4, 5]`, no SL4'-X; script [C2])

**Lemma R.2.** Assume SL1'-w and SL4'-E. For every `m >= 700` and every
`w in (4, 5]`, the W1 row value is `<= 0.9115`. In particular the W1 band
closes there with `>= 8.8%` margin, consuming NO SL4'-X.

*Proof.* Bound the crossover slot by the TRUE integral (no left-endpoint
sums): on `[0.8 lam, t_0]`, `|phi(t)| <= e^{-m x(w, t/lam)} <= e^{-0.0176 m}`
([W.6] pointwise + Lemma R.1, `t_0 <= 1.074 lam` by Lemma SL3.C), and with
`A = m` (the share worst case; `e/A ~ A^{3/2}` nondecreasing, §3),
`s2 = A/lam^2 <= m^3/w^2`:

```
Xn <= m (sqrt(2pi)/pi) (m^3/w^2)^{3/2} * [(1.074 lam)^3 - (0.8 lam)^3]/3 * e^{-0.0176 m}
    = K_Xn m^{5/2} e^{-0.0176 m} ,   K_Xn = (sqrt(2pi)/pi)(1.074^3 - 0.8^3)/3 = 0.1933097 <= 0.19332 ,
Xd <= K_Xd m^{3/2} e^{-0.0176 m} ,  K_Xd = (sqrt(2pi)/pi)(1.074 - 0.8) = 0.2186204 <= 0.21863 ,
```

both `w`-free (the `w`-powers cancel exactly: `(m^3/w^2)^{3/2} lam^3 =
m^{3/2}`). Set `B(m) := (0.19332 m^{5/2} + 0.21863 m^{3/2}) e^{-0.0176 m}`;
`B` is nonincreasing for `m >= 2.5/0.0176 = 142.05`. The W1 row is then
bounded by `(1+QUADF)[dec(m)/(20*0.28) + INFL (B(m) + Fn + Fd)/20]` with
`dec(m)` the closed-form dec-part at `A0 = 0.28 m` — every piece
nonincreasing in `m` on `m >= 700` (§3; far for `m >= 75`). Script [C2],
verbatim:

```
  m=700: B(m) = 11.1999;  dec_W1 = 1.23288;  W1 row bound = 0.911407  PASS  (margin 0.08859)
  m=750: ... 0.567346  PASS    m=800: ... 0.394535  PASS    m=1000: ... 0.231364  PASS
  CERTIFIED: W1 row <= 0.91141 for ALL m >= 700 and ALL w in (4, 5]  [inputs: W.6 pointwise + Lemma R.1 + C.1 + A2 + SL1'-w + SL4'-E; NO SL4'-X]
```

Sanity ([C3]): the flat-exponent bound dominates the `X_w6` grid values by
32x at `(700, 4+)` (and by >= 4e5x away from the edge) — the tail bound is
crude but sufficient, which is why it cannot replace the grid below 700
(script [C2]: `B(561) = 74.389` vs available X-slot `~ 12.475` — the grid
rung 5.2 is genuinely needed on `[561, 699]`). ∎

### 5.5 The corrected sliver diagnosis (F7; script [D4])

At `(w, m) = (4.05, 401)` (inside `T`), with the convention "contribution
of each slot to the row value `share*(1+q)`" (inc slots:
`slot*(1+QUADF)*INFL/20`; dec part: `dec/(20*0.28)*(1+QUADF)`):

```
  row total = 1.3911 (FAIL, inside the trapezoid);
  X-share = 0.99538;  far-share = 0.12144;  dec-share = 0.27429   [referee D1: 0.9954 / 0.1214 / 0.2743, total 1.3911]
  m*x(4.05, 0.8) = 7.6453
```

The original's "share 0.68" is retired (unreproducible under any natural
convention — referee F7). The qualitative diagnosis STANDS and is now
quantified: the trapezoid is a CROSSOVER-exponent sliver (X-share ~1.0 of
the unit budget at the failing point; the far slot is comfortable at
~0.12) — which is exactly why Lemma R.1's floor (`m x >= 0.0176 m`, i.e.
`9.9` at `m = 561` vs `7.65` at `m = 401`) closes it for large `m` and why
the harness closes it below.

## 6. Corollary R.3: F1/F2 are MOOT in the CL assembly at `m >= 561` (with proof)

**Corollary R.3 (mootness + the assembled CL statement).** Assume SL1'-w,
SL4'-E, and SL4'-X restricted to W1 rows with `m in [561, 699]`; consume
Theorem SL3', [A2]/[A3]/[C.1]/[W.6], and Fact SLV.2/Cor SLV.3. Then:

1. *(Trapezoid inclusion — F1/F2 mootness.)* Under EITHER F1 repair route
   the corrected trapezoid lies strictly inside the exact harness
   coverage: route (a) `T subset (4, 4.095] x [401, 462]` and route (b)
   `T_b subset (4, 4.135] x [401, 469]`, while the harness PASSes every
   integer `m in [4, 560]`. Script [A4] + [D6], verbatim:

   ```
   route (a): gamma*(W1)=0.42: trapezoid m-range [401, 462];  max m = 462 <= M_H = 560: True;  first sliver-free m = 463 <= 561: True
   route (b): gamma*(W1)=0.25: trapezoid m-range [401, 469];  max m = 469 <= M_H = 560: True;  first sliver-free m = 470 <= 561: True
   parsed data rows: 557;  non-PASS rows: 0
   coverage [4, 560]: gaps = NONE;  [401, 560]: gaps = NONE
   OVERALL line (verbatim): # OVERALL: PASS -- all of C1..C6 hold exactly for 4 <= m <= 560 (C2/C3 with the known m=4 exception; rows split across this file and the honored prior file(s)).
   ```

   Per Cor SLV.3 the consumer's conclusion on ALL of `[401, 560]` (hence
   in particular on the trapezoid) holds by exact computation, so the
   referee's moved constants (`4.10 -> 4.135`, `461 -> 462/469`) CANNOT
   affect the CL assembly: any trapezoid with max-`m <= 560` is
   consumer-discharged. (They still had to be — and are — fixed in the
   theorem display: §§4–5.)

2. *(The assembled statement — no sliver exception at the operative
   threshold.)* For every `m >= 561`, every interior `k` with `lam(k) in
   (4/m, 0.89]`: `s2(r(k)-1) = 1 + theta 20/min(m, s2)`, `|theta| <= 1` —
   i.e. **CL(79, 20, 0.89) restricted to `m >= 561`, which is by Cor
   SLV.3 the ENTIRE remaining CL obligation, holds with NO exception set**.
   *Proof:* bands W2–W7 by Theorem SL4'-R (rows certified at 401,
   entries nonincreasing in `m`, §3/§4); band W1 by the ladder — `m in
   [561, 699]`: Fact R.G (§5.2; worst probed row `0.424939`, margin
   57.5%); `m >= 700`: Lemma R.2 (§5.4; row `<= 0.9115`, no SL4'-X). The
   trapezoid `T` (max `m = 462`) does not intersect `m >= 561`. ∎

3. *(Scope honesty.)* Item 1 is a consumer-level discharge (Theorem A's
   finite part by exact computation), NOT a lemma-level proof of CL on
   `[401, 560]` — the same distinction the sliver note and both its
   referees drew for Cor SLV.3. Item 2 IS the lemma-level statement on
   `m >= 561`, conditional on exactly SL1'-w + SL4'-E + SL4'-X(`[561,
   699]`). Within `[463, 560]` the theorem's W1 rows are ALSO certified
   (Fact R.G covers `[463, 699]`), but on that segment the certification
   is belt-and-braces: the harness already discharges the consumer there.

**Consequence for the campaign ledger (STATUS_wave4 §2 updated by this
file):** the conditional surface of unconditional Theorem A is now
exactly (a) SL1'-w, (b) SL4'-E, (c) SL4'-X scoped to the FINITE range
`m in [561, 699]` x `w in (4, 5]` (139 integers; elementary calculus,
referee-audited at 25k+ grid points with 0 violations), plus (d) the
referee cycle owed on THIS file, plus (e) the composition note + flip
(STATUS_wave4 §3 items 2/6). The SL3'-w item is DISCHARGED; the sliver
item was already CLOSED; F1/F2's constants are fixed AND moot.

## 7. Script table (all SAVED and RUN 2026-08-12; outputs archived beside them)

| # | script (`g2_scripts/campaign_20260811/wave5_sl4prepair/`) | validates | key verbatim output |
|---|---|---|---|
| [common] | `sl4pr_common.py` | byte-faithful copy of the prover's row machinery (`sl4p_nc1_ledger.py` lines 12–103; referee-rebuilt to `< 5e-5`), importable; print blocks removed, nothing else changed | (module; no output) |
| [A] | `sl4pr_a_trapezoid.py` (`out_sl4pr_a.txt`) | F1/F2: `w†(m)` full integer grid 401–462 at `gamma* = 0.42`, step 1e-3 (462 at 1e-5); `w -> 4+` closure edge at `4.0`/`4+1e-9`/`4+1e-7`; route-(b) numbers; mootness arithmetic | `w_dagger(401) = 4.095`; `w_dagger nonincreasing ... True`; `w_dagger(462) refined (step 1e-5) = 4.00021`; `first PASS m = 463` (all three edge probes); `w_dagger(401; 0.25) = 4.135`; `first full-closure ... under gamma* = 0.25: 470`; both routes `max m <= M_H = 560: True` |
| [B] | `sl4pr_b_grid.py` (`out_sl4pr_b.txt`) | Fact R.G: every integer `m in [463, 699]` x 106 `w`-probes; fine 1e-3 scans at 463/561/699; column `m`-monotonicity; SL4'-X flag at all 25,122 evaluations | `FAIL count over all 25122 (m, w) probes: 0`; `X_w6 monotone-in-tau flag violations ...: 0`; `overall max row ... 0.991128 at (463, 4.0)`; `m=561: ... edge row(4+1e-9) = 0.424939 (margin 0.5751)`; `columns: 106; nonincreasing-in-m violations: 0` |
| [C] | `sl4pr_c_xtail.py` (`out_sl4pr_c.txt`) | Lemma R.1 (548-cell floor with epsilon audit) + Lemma R.2 (tail constants, `B` monotonicity, row bound 700–5000) + [C3] sanity | `min cell lower bound = 0.0176601 at tau-cell [0.8, 0.8005]`; `CERTIFIED: x(w, tau) >= 0.0176 ... : True`; `K_Xn = 0.1933097 <= 0.19332: True`; `m=700: ... W1 row bound = 0.911407 PASS (margin 0.08859)`; `B(561) = 74.389` vs slot `12.475`; `tau0 ... 1.0000066 <= 1.074 ... True` |
| [D] | `sl4pr_d_misc.py` (`out_sl4pr_d.txt`) | F3 (eta edges, machinery = `sl4p_nc2_eta.py` verbatim), F5 (efac boundary), F6 (A-monotonicity + used-range scan), F7 (decomposition), F4 (C5* scoping), harness parse | `worst ratio = 0.6579 at (m, w) = (401, '5.0')`; `... 'never above 0.66 ...': True`; `4(1-e^(-1/4)) = 0.88479687`; `A ~ 36.7; ... e_midn(32) = 140.965 < e_midn(36) = 142.176: True`; all four dec-entry scans `[112, 3000] ... True`; `X-share = 0.99538; far-share = 0.12144; dec-share = 0.27429`; `W1, m=401, w=4.10, C5*=0.4: row = 1.4695 FAIL`; `W6b ... 0.89301 PASS`; `non-PASS rows: 0`, `gaps = NONE` |

Consumed archived evidence (quoted as its own file's claim): the original
`wave4_sl4p/sl4p_nc1_ledger.py` + `out_sl4p_nc1.txt` (ledger rows, blocks
[0]–[5]) and `sl4p_nc2_eta.py` + `out_sl4p_nc2.txt`; the referee's
`referee_wave4_sl4p/out_ref_nw4p_{a,b,b2,c,d,e}.txt` (independent rebuild,
B1 one-crossing scans, B4 full-grid m-monotonicity, dps-100 margins);
`harness_m560/results_m560.txt` + `wave2_repairs/results_m540.txt`
(parsed, not modified). Numeric-integrity note: scripts [A]/[B]/[D-rows]
are the house-approved mpmath dps-40 point-evaluation class on the
referee-validated machinery; script [C1]'s epsilons make every inequality
direction rigorous; script [D1] is dps-30 (the eta machinery's own class).

## 8. Status recap (prover's own; two referees owed on this file)

- **Theorem SL4'-R: PROVED MODULO SL1'-w + SL4'-E + SL4'-X**, with SL4'-X
  consumed only on W1 at `m <= 699`. Delta vs the original: hypotheses
  4 -> 3 (SL3'-w discharged by Theorem SL3', flagged-certificate class
  inherited); trapezoid corrected `(4, w†(m)) x [401, 462]`, `w†(401) =
  4.095`, `w†(462) = 4.00021`; every referee finding F1–F7 resolved (§1
  map) — F1 by route (a), F2 by `462`, F3 by `0.66/0.6579@w=5`, F4 by
  scoping + `1.6x–8x`, F5 by `0.88480`, F6 by Lemma SL4'.8' + used-range
  scans, F7 by the explicit-convention decomposition.
- **New proved content** (given the §0 citable inputs): Lemma R.1
  (crossover-exponent floor `0.0176`, epsilon-rigorous), Lemma R.2 (W1
  analytic tail `m >= 700`, all `w in (4, 5]`, row `<= 0.9115`, no
  SL4'-X), Corollary R.3 (mootness + the assembled CL(`m >= 561`)
  statement with empty exception set). Fact R.G is grid-certificate class
  (0/25,122 failures, complete integer `m`-quantifier on `[463, 699]`).
- **The CL assembly now reads:** CL(79, 20, 0.89) for `m >= 561` =
  Theorem SL4'-R + Theorem SL3' + Fact SLV.2/Cor SLV.3, conditional on
  exactly SL1'-w + SL4'-E + SL4'-X(`[561, 699]`). No sliver exception
  survives anywhere in the operative range. The composition note
  (STATUS_wave4 §3 item 6) can now be written against THIS file.
- **Honesty ledger:** this file has ZERO referees (maths referee owed —
  the original never had one — plus a numerics re-grade); Fact R.G's
  `w`-continuum and the ledger's `m = 401` row evaluations are the
  campaign's accepted certificate classes, flagged; Theorem SL3''s
  monotone-cell class and 1.30x-margin caveat are inherited (§0); the
  W5/W7 thin margins (1.1%/1.9%) and INFL/QUADF bootstrap margins
  (0.3%/1.8%) are unchanged from the original and referee-confirmed at
  dps 100; truth support (REF-B: CL exact at `m = 401/402`, 17.1x margin)
  untouched and consistent. CONJECTURED items consumed: none silently —
  exactly the three named hypotheses.

*End of wave4_sl4p_repaired_20260812.md.*
