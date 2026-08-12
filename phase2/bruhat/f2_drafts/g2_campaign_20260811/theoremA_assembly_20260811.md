# Theorem A — assembly document (merged statement, single named conditional)

*Wave-3 assembly session, campaign 2026-08-11 (STATUS_wave2.md §5.3). This is
the document a human co-author reads to ratify Theorem A = F2(a). Written
from: `STATUS_wave2.md` (the governing ledger), `wp3_draft_a2.md` (Theorem S),
`wp2_draft_a2.md` (Theorem D.5, Theorem T.9-final), `wp2_draft_b.md` (W.0–W.7),
`wp1_draft_c.md` (W.3–W.6), `g1_draft_b.md` (B.0–B.9), `F2_PROOF_DRAFT.md`
(frame, Cor 2.3, Lemma 3.6), `g2_draft_t2_20260803.md` restricted to its
two-referee inventory, `repairs_20260811.md`, `harness_m200_20260811.md`, and
the referee reports listed in §5. NOT read: `g2_draft_t1_20260803.md` (blind
rule); every wp4 file (the wp4 mini-campaign runs concurrently — its spec is
consumed ONLY in the frozen form recorded in `wp3_draft_a2.md` §6.1). No
existing file modified; this file and its script directory are new. Every
synthesis-level number below is re-verified by the SAVED and RUN script
`g2_scripts/campaign_20260811/theoremA_assembly/assembly_checks.py` (output
archived beside it as `out_assembly_checks.txt`, run 2026-08-11/12); verbatim
excerpts in §4. House-rule status of THIS document: zero referees until its
own pass runs — it is the designated referee unit for the cross-package plug
(STATUS_wave2 §2, "checked here, not yet refereed as a unit").*

## Contents

- §0 The theorem, its status, and the one-citation flip to unconditional.
- §1 Notation and standing objects.
- §2 The assembled proof (m <= 400 exact; m >= 401 lower bound via Theorem S
  with the T.9-final plug; upper bound via Cor 2.3; conclusion).
- §3 The single named conditional: `CL(79, 20, 0.89)` (frozen spec, verbatim).
- §4 The T.9-final plug into R3 — independently re-verified (script output).
- §5 Dependency graph: which file proves what, with referee status.
- §6 The constant ledger, end to end.
- §7 Standing caveats (honest, none hidden).
- §8 Ratification checklist for the human co-author.

---

## 0. The theorem and its status

> **Theorem A (= F2(a), sharp form).** Let `I_m(k)` be the Mahonian numbers
> (inversions of `S_m`), `N = m(m-1)/2`, `sigma^2 = m(m-1)(2m+5)/72`,
> `r_m(k) = I_m(k)^2/(I_m(k-1) I_m(k+1))`, `r_m = min_{1 <= k <= N-1} r_m(k)`.
> Then
>
> ```
> sigma^2 (r_m - 1) = 1 - (27/25) m^{-1} + O(m^{-2}) ,
> ```
>
> in particular `sigma^2 (r_m - 1) -> 1` (equivalently `r_m - 1 ~ 36/m^3`),
> the two-sided `O(m^{-2})` carrying the explicit constant `C_A` of §2.4.
> Finite companions (exact, `4 <= m <= 400`): argmin central, min = central
> ratio (`m >= 5`), `sigma^2(r_m - 1) >= 187/216` for `m >= 5` with equality
> only at `m = 6`, strict increase from `m = 6`.

**Status: PROVED CONDITIONAL on exactly ONE named mathematical statement** —
the deep-tilt core lemma

```
CL(C_0* = 79, C* = 20, Lambda* = 0.89)      for all m >= 401     (§3, verbatim spec)
```

(wp4's package; lower-bound form suffices). Every other ingredient is proved
at the referee statuses itemized in §5, with the standing caveats of §7
(grid-certificate-class inputs; the Bona citation; pending text-level repair
files). No other conditional, hypothesis, or unproved threshold appears
anywhere in the chain.

**The one-citation flip.** This document is structured so that when wp4 lands
with two-referee status, Theorem A becomes unconditional by a single edit:
replace the bracket `[WP4-CITATION]` in §2.3 (region R2's row — its only
occurrence in the proof) by the citation of wp4's theorem, and delete §3's
"open" marker. Nothing else changes: no constant, no threshold, no other step
consumes CL.

## 1. Notation and standing objects

All notation is the merged draft's (`F2_PROOF_DRAFT.md`), as used by every
campaign file:

- `I_m(k)`, `N = m(m-1)/2`, `a_k := I_m(k)` (palindromic, `a_k = a_{N-k}`);
  WLOG `k <= N/2` throughout.
- `lambda = sigma^2 = m(m-1)(2m+5)/72`; `S_r = sum_{j=1}^m j^r`;
  `B_m = (S_4 - m)/(240 lambda^2) = (27/25) m^{-1} (1 + O(m^{-1})) > 0`.
- Tilt: `lam(k)` the unique solution of `mu(lam) = k` (Lemma 3.1,
  `mu' = -sigma_lam^2 < 0`); `s2 := sigma_{lam(k)}^2`; `w := lam m`;
  central index `k_c = floor(N/2)`.
- `r(k) - 1` is compared against `1/lambda`; "varfit" `:= sigma^2 (r_m - 1)`.
- The refined law (Prop 3.5(ii), now Theorem T.9-final) and the crude law
  (Prop 3.5(i), whose only remaining instance is CL) are as in §2.3.
- Citation tags: `B.x` = `g1_draft_b.md`; `T.x` = `g2_draft_t2_20260803.md`;
  `W.x` = `wp1_draft_c.md`; `W2b-x`/`W.0–W.7` = `wp2_draft_b.md`; `D.x`,
  `T.9-final` = `wp2_draft_a2.md`; `P.x`, `Theorem S` = `wp3_draft_a2.md`;
  Lemmas `1.x/2.x/3.x`, Prop 3.5, Cor 2.3 = `F2_PROOF_DRAFT.md`. Referee
  status per file: §5.

## 2. The assembled proof

The proof has four parts: (I) the exact range `m <= 400`; (II) the lower
bound for `m >= 401` (Theorem S's partition, with the T.9-final plug closing
R3 and CL closing R2); (III) the upper bound (Cor 2.3, unconditional); (IV)
the conclusion. Parts I, III, IV are unconditional; part II is where the
single `[WP4-CITATION]` sits.

### 2.1 Part I — `4 <= m <= 400`: exact computation (PROVED).

`harness_m200_20260811.md` (script `run_m200.py`, 320.9 s, 397 rows, zero
failures, every verdict exact integer/`Fraction`): for all `4 <= m <= 400`,

- (C1) `I_m` has `N+1` strictly positive palindromic coefficients;
- (C2) `argmin_k r_m(k) = floor(N/2)` for `5 <= m <= 400`; at `m = 4` the
  known exception (argmin `= 2`, `|argmin - N/2| = 1`);
- (C3) `r_m` EQUALS the central ratio `r(floor(N/2))` for `5 <= m <= 400`;
- (C4) `N` odd forces the exact central tie (the G5 flat step);
- (C5) `varfit >= 187/216` for `5 <= m <= 400`, equality only at `m = 6`
  (scope note: the harness REPORT's §3 displays "4 <= m"; the runner
  exempts `m = 4` by design and `varfit(4) = 91/108 < 187/216` — display
  erratum, recorded in §7 item 8, caught by this session's independent
  rebuild);
- (C6) `varfit` strictly increasing on `6 <= m <= 400`
  (`varfit(400) = 0.997302329987`).

Independent re-anchor (this session, script §4, exact rebuild from the
`q`-factorial recurrence): all of C1–C3/C5/C6 re-verified on `4 <= m <= 60`
with 0 failures; `varfit(6) = 187/216` exactly; `varfit(40) = 0.973381`
(= ledger NC-1); `varfit(60) = 0.982146`.

### 2.2 Part II, upper half of the toolkit — the two laws on the small-tilt band.

**(Refined law; PROVED modulo §5 statuses.) Theorem T.9-final**
(`wp2_draft_a2.md` §7 = W.7 + Prop W.6 (repaired) + Lemma W.4 + Theorem D.5 +
W.4(i) + T.9''/(T.8a)/T.1(ii) + B.0(ii)): for `K in {1, 2, 4}`,
`m >= M(K) = 180/181/367`, and every interior `k` with `0 < |lam(k)| <= K/m`:

```
s2 log r(k)   = 1 - B_m (1 + theta_1 c_w(K) w^2) + theta_2 C_R(K)/m^2 ,
s2 (r(k) - 1) = same + theta_3 Lin(K, m) ,          |theta_i| <= 1 ,
c_w = (0.407, 0.466, 1) ,
C_R(K) = 41.17 / 230.09 / 37998   (closed flavor, all m >= M(K))
       = 32.44 / 213.12 / 37815   (PW-grid flavor, m <= 2000) ,
m^2 Lin(K, 180) = 0.2308 / 0.2571 / 0.3719  (decreasing in m) .
```

W.5's hypothesis `|s2 log r - 1| <= 1/2` is discharged unconditionally:
`H(K, M(K)) = 0.0097 / 0.0241 / 0.3321 <= 1/2`, decreasing in `m`
(wp2-a2 NC-A5(2); `H(4, 367) = 0.3321` re-verified exactly this session,
§4 block F). D.5's bound is `w`-uniform on `|w| <= K`, so the merged
envelope is W.6's unchanged (wp2-b referee-F5 question resolved in the clean
direction). This is Prop 3.5(ii), CLOSED modulo the §5 statuses.

**(Deficit floor and tilt cap; PROVED.)** Lemma P.7 (with the referee-R2
repaired decimals): `1 - s2/lambda >= 6.85 w0^2 E(w0)` for `|w| >= w0`,
giving at `w0 = 4`: `deficit >= 0.27289`, i.e. `s2 <= 0.72711 lambda` on
`|w| >= 4`. Lemma P.8: `lam(k) <= log(1 + 1/c)` for `k >= c m`; this
session's script proves `log(17/7) < 0.89` and `log 2 < 0.89` by an exact
positive-series bound (`e^{0.89} > 2.4351 > 17/7 > 2`), so `Lambda* = 0.89`
covers every residual-band tilt.

### 2.3 Part II — the lower bound for `m >= 401` (Theorem S + the plug).

**Theorem S** (`wp3_draft_a2.md` §5) partitions the interior WLOG-range
gap-free — `K_c := min(c m, m-1)` with `c = 7/10` for `401 <= m < 1581`,
`c = 1` for `m >= 1581`:

```
R1a = {k = 1},  R1b = {2 <= k <= K_c},
R2  = {k > K_c, |w(k)| > 4},  R3 = {k > K_c, |w(k)| <= 4} .
```

Row by row, with the statuses as they now stand:

| region | mechanism | conclusion `lambda(r(k)-1)` | condition |
|---|---|---|---|
| R1a | Lemma 3.6 (pentagonal, merged draft; FULLY PROVED): `r(1)-1 >= (m-1)/(2(m+1))` | `>= 10^5` at `m >= 401` | — |
| R1b | Theorem P.5 (PROVED; thresholds `m_p(7/10) = 300 <= 401`, `m_p(1) = 1581` at the switch): `r(k)-1 >= (m-1)/(2k(m+k))` | `>= 1879` at `m = 401` | — |
| R2 | P.6 floor `s2 >= v(c) m` (`v(7/10)*401 = 79.53 >= 79`; `v(1)*1581 = 527`); P.7 `s2 <= 0.72711 lambda`; P.8 + this session's cap proof: `lam <= 0.89`; CL applies with budget `C*/min(m, s2) <= 20/79.5 = 0.2516 <= eps* = 1 - 1.02 * 0.72711 = 0.25835` (band 2: `136/527 = 0.25806 <= eps*`, margin `2.8e-4`) | `>= (1 - 0.2516)/0.72711 = 1.0293 >= 1.02` | **`CL(79, 20, 0.89)` — [WP4-CITATION]** |
| R3 | Theorem T.9-final at `K = 4` (the PLUG, §4): scope `M(4) = 367 <= 401` and band `|w| <= 4` match exactly; P.7's `w^2`-coefficient domination — bracket `6.85 E(4)(1 - 17 B_m - C/m^2) - B_m` re-verified POSITIVE with the actual plugged `C` (`0.009575` at `m = 401`, exact scan to 2000, §4 block D) — lets the nonnegative `w^2` term be discarded | `>= 1 - B_m - C_A/m^2` | — (was "wp2-a's `C_ker`"; MET by Theorem D.5) |

with (repair F3 applied — `C_R^PT(4)` already contains `Lin`, no double
count):

```
C_A := C_R^PT(4) + C_ker(4) = 5.32 + 37810.05 = 37815.37    (grid flavor, m <= 2000)
                            = 187.8 + 37810.05 = 37997.85   (closed flavor, all m >= 401) .
```

Exact-center note (wp3-a2 referee R4): `N` even, `k = N/2` has `lam = 0`,
formally outside T.9-final's `0 < |lam|`; that single point is covered by
Theorem B.8/Cor B.9 (g1_draft_b, fully refereed), whose window law at
`|y| <= 0.1` gives the same bound with constant `1.1 <= C_A`.

Since R1a/R1b/R2 all exceed `1.02 > 1 - B_m`, the global minimum lies in R3:

```
sigma^2 (r_m - 1) >= 1 - B_m - C_A/m^2       for all m >= 401 ,        (LB)
```

conditional on exactly `[WP4-CITATION]` (R2's row and nowhere else).
Re-verified this session (§4 block A): the right side at `m = 401` is
`0.762141` (grid; `0.761006` closed), and it increases to 1 (`B_m` strictly
decreasing — exact scan — and `C_A/m^2` decreasing).

### 2.4 Part III — the upper bound (unconditional), and the sharp form.

Cor 2.3 (`F2_PROOF_DRAFT.md`, its G1 gap CLOSED by g1_draft_b — see
g1_draft_b §7 item 3 for exactly this instantiation): for `m >= 180`, at
`k = k_c` (`|y_c| <= 1/(2 sigma)`), Corollary B.9 with `y_0 = 0.1` gives

```
sigma^2 (r(k_c) - 1) = 1 - B_m + theta * 1.8/m^2 ,     |theta| <= 1 .      (UB)
```

Since `r_m <= r(k_c)` always,

```
1 - B_m - C_A/m^2  <=  sigma^2 (r_m - 1)  <=  1 - B_m + 1.8/m^2      (m >= 401) ,
```

i.e. `sigma^2 (r_m - 1) = 1 - B_m + O(m^{-2})` with the explicit two-sided
constant `C_A = 37815.37` (grid; use the closed flavor 37997.85 beyond
`m = 2000` — either is a fixed constant, which is all the sharp form needs).
With `B_m = (27/25) m^{-1}(1 + O(m^{-1}))` (closed forms of `S_4`, `lambda`;
merged-draft header, elementary; `B_m m` re-verified `-> 1.08` in §4 block F):

```
sigma^2 (r_m - 1) = 1 - (27/25) m^{-1} + O(m^{-2})  ->  1 .
```

### 2.5 Part IV — conclusion and finite companions.

For `m >= 401`: §2.4. For `4 <= m <= 400`: part I gives every finite
companion exactly, and the asymptotic statement is vacuous there. The finite
companions for `m <= 400` (argmin centrality, min = central, `187/216`
sharp bound, strict increase) are exactly harness C2/C3/C5/C6. ∎

**Overall status marker: Theorem A is PROVED modulo `[WP4-CITATION]` =
CL(79, 20, 0.89)**, at the referee statuses of §5 and with the caveats of §7.

---

## 3. The single named conditional: `CL(79, 20, 0.89)` — OPEN

Frozen spec, verbatim from `wp3_draft_a2.md` §5/§6.1 (both its referees
verified the spec arithmetic; the wp4 mini-campaign targets it as written —
no wp4 file was read for this assembly):

> **`CL(C_0*, C*, Lambda*)`**: *for interior `k` with `s2 >= C_0*` and
> `|lam(k)| <= Lambda*`,*
> ```
> r(k) - 1 = s2^{-1} (1 + theta C*/min(m, s2)) ,   |theta| <= 1 ,
> ```
> *needed at `(C_0*, C*, Lambda*) = (79, 20, 0.89)` for all `m >= 401`; the
> lower-bound-only variant `r(k) - 1 >= (1 - C*/min(m, s2))/s2` suffices.*

Support already proved around it (so wp4 owes ONLY the core model on the
`1/sqrt(s2)` scale): scope is the compact band `4/m < lam <= 0.89` (P.8 +
this session's exact cap proof; for `m >= 1581` only `lam <= 0.70`), all of
it inside wp1-c's PROVED far machinery — W.5(ii) on `[t_0(lam), pi]`
(exponent floor `0.0373 m`), W.6 on the crossover `[pi/m, t_0(lam)]`, and
T2's (T.6ii) Gaussian domination on `[0, pi/m]` (two-referee). Measured
truth margin at the spec point: 6.7x (wp3-a2 NC-P3d, referee-reproduced:
`eps(k) <= 0.0385` at `m = 30` over EVERY interior `k`, falling `~1.2/m`,
vs the `0.2516` budget). Identified route: strip analyticity of
`log phi_lam` (`|Im t| < lam`), cumulant-model radius `~ c lam` vs Gaussian
width `1/sqrt(s2)` (wp1-c §9 item 2; STATUS_wave2 §5.1's drafting kit).

**Flip instruction (the whole point of this document).** When wp4 lands with
two-referee status at spec `CL(79, 20, 0.89)` (or stronger: any
`C_0* <= 79`, `C* <= 20`, `Lambda* >= 0.89`), edit §2.3's R2 row: replace
`[WP4-CITATION]` with the citation. Theorem A is then UNCONDITIONAL at the
statuses of §5. If wp4 lands at a WEAKER spec `(C_0', C', Lambda')`, the
stitch still closes provided `C'/max(C_0', v(c)m-floor) <= eps* = 0.25835`
on each band (re-run `assembly_checks.py` block C with the landed numbers
before flipping; the band-2 margin is the tight one, `2.8e-4`).

## 4. The T.9-final plug into R3 — independently re-verified

**What the plug is.** wp2-a2 and wp3-a2 were written blind to each other.
Theorem S's R3 row names "wp2-a's `Delta_ker` constant `C_ker`" as its
condition; Theorem D.5 supplies exactly that object. The plug is the
five-fold compatibility check that no draft or referee performed as a unit
(STATUS_wave2 §2 checked it at synthesis level; this session re-derives it
independently — different script, exact `Fraction` arithmetic throughout):

1. *Threshold:* `M(4) = 367 <= 401` — D.5 is in force on all of Theorem S's
   analytic range. TRUE (block A1).
2. *Band:* D.5/T.9-final cover `0 < |lam| <= 4/m`, i.e. `|w| <= 4` —
   exactly R3's band; the bound is `w`-uniform (T.9-final's envelope note),
   so no `w`-dependence leaks into R3's constant. TRUE (by statement;
   A1).
3. *Arithmetic:* the plugged R3 line `1 - B_m - C_A/m^2` at `m = 401` equals
   `0.762141 > 0` (grid flavor; `0.761006` closed) and increases to 1
   (`B_m` exactly decreasing on the scanned range). TRUE (blocks A2–A3);
   matches STATUS_wave2 §2's plug note to all printed digits.
4. *`w^2`-discard:* R3's chain discards a `w^2` term whose bracket was
   checked in wp3-a2 only with the pre-plug `C = 5.32` (its note-2 values
   `0.01628 - 0.00270`); with the ACTUAL `C_A = 37815.37` the bracket is
   still positive — `0.009575` at `m = 401`, exact scan positive through
   `m = 2000`, monotone increasing to `6.85 E(4) = 0.017056`. TRUE (block
   D). *(This check is NEW here — neither draft could have run it.)*
5. *No double count:* `Lin` enters once (`C_R^PT(4)` contains it; repair
   F3 applied in the `C_A` display). TRUE (by the B3 decomposition
   `5.3159 = 4.93 + 0.01402 + 0.3719`).

Verbatim script output (`assembly_checks.py`, archived
`out_assembly_checks.txt`, run 2026-08-11/12; blocks E/F below re-anchor the
harness and the `H`/`B_m` constants):

```
== (A) the plug: C_ker(4) [wp2-a2 D.5] into Theorem S R3 [wp3-a2] ==
  A1. scope: M(4) = 367 <= 401 = Theorem S analytic start: True
  A2. grid   C = 5.32 + 37810.0442 = 37815.3642 ; R3 bound at m=401 = 0.762141 (>0: True)
  A2. closed C = 187.8 + 37810.0442 = 37997.8442 ; R3 bound at m=401 = 0.761006 (>0: True)
  A3. B_m strictly decreasing on [401, 3001] (exact scan): True ; C/m^2 trivially
      decreasing => R3 bound increasing -> 1
== (B) part-(c)/G4 crossovers: smallest m with 1 - B_m - C/m^2 >= 187/216 ==
  K=4 grid   (C = 37815.3642)      m* = 535 (stays beyond: True; harness gap: [401, 534])
  K=4 closed (C = 37997.8442)      m* = 537 (stays beyond: True; harness gap: [401, 536])
  K=1 center (C = 41.17 + 0.2308)  m* = 22 (stays beyond: True; harness gap: NONE)
== (C) Theorem S R2 budget, REPAIRED constants (rho(4) <= 0.72711) ==
  C1. s2 floors: v(7/10)*401 = 47719/600 = 79.5317 >= 79 (C_0* met: True);
      v(1)*1581 = 527 = 527.0 >= 527
  C2. eps* = 1 - 1.02*rho = 1291739/5000000 = 0.2583478
  C3. band-1 budget 20/79.5 = 0.251572  (exact-floor 20/79.5317 = 0.251472)  <= eps*: True / True
      band-2 budget 136/527 = 0.2580645 <= eps*: True  (margin 2.83e-04)
  C4. R2 conclusion (1 - 20/79.5)/rho = 1.029318 >= 1.02: True
  C5. e^0.89 > 2.435129651 (18-term positive partial sum, exact Fractions)
      17/7 = 2.428571429 < e^0.89 => log(17/7) < 0.89 (cap, c=7/10): True
      2 < e^0.89 => log 2 < 0.89 (cap, c=1): True
== (D) R3 w^2-bracket WITH the plugged C ==
  grid   bracket(401) = 0.009575 > 0: True ; exact scan 401..2000 all > 0: True
  closed bracket(401) = 0.009556 > 0: True ; exact scan 401..2000 all > 0: True
== (E) independent exact harness rebuild, 4 <= m <= 60 ==
  [C5 scope check] varfit(4) = 91/108 = 0.842593 < 187/216: True (the m=4 record row)
  m= 6 argmin=   7 (expect 7)  varfit=0.865741  [= 187/216 exactly: True]
  m=40 argmin= 390 (expect 390)  varfit=0.973381
  C1-C3/C5 failures on 4..60: 0 ; C6 varfit strictly increasing 6..60: True
== (F) B_m*m -> 27/25 = 1.08 ; H(4, 367) recompute ==
  m =    401  B_m*m = 1.078693     m = 100000  B_m*m = 1.079995
  H(4, 367) = B_367*(1 + c_w(4)*16) + C_R(4)closed/367^2 = 0.3321 <= 0.5: True
```

(Block B's `K=1` row: `m* = 22` scanning from `m = 6`; the STATUS_wave2
script printed 30 because its scan STARTED at 30 — no discrepancy. Block B
is a G4 note, not part of Theorem A: see §7 item 7.)

## 5. Dependency graph

### 5.1 File-by-file: what it proves, and its referee status

| # | file | proves (as consumed here) | referee status |
|---|---|---|---|
| 1 | `F2_PROOF_DRAFT.md` | frame: notation, ground truth, Lemmas 3.1–3.4 (tilt toolkit, FULLY PROVED there), Lemma 3.6 (pentagonal edge), Prop 3.5 statement, Cor 2.3 statement, Theorem A skeleton | merge-editor synthesis of 4 blind drafts + 4 adversarial referees (2026-07-06); its gap ledger G1–G4 is the campaign's scoreboard |
| 2 | `g1_draft_b.md` | G1 CLOSED: B.0–B.9 (window law Theorem B.8/Cor B.9, explicit `C_2(y_0)`, `m_1 = 180`); Cor 2.3's `O(m^{-2})` constant 1.8 (§7 item 3); exact-center coverage | FULLY REFEREED (maths + numerics, 2026-08-02) + `g1b_repairs_20260802.md` |
| 3 | `g2_draft_t2_20260803.md` | T.x inventory as consumed: T.1(ii), T.4/T.4', T.5-final, (T.6ii), T.7b/c-final, (T.8a), T.9'' | BOTH halves done: `referee_t2_numerics.md` (wave 1, MINOR_REPAIRS; F1–F9 applied in `repairs_20260811.md` §C) + `referee_t2_maths.md` (wave 2, MINOR_REPAIRS; M-repairs pending a `t2_repairs` file — §7 item 4). **T.10(2)/T.8'' NOT citable as displayed; consumed NOWHERE in this chain** (verified by both wave-2 maths referees) |
| 4 | `wp1_draft_c.md` | far bounds W.3–W.6: `c_1(K) = 0.2259/0.1802/0.1019`, far floor `exp(-0.0372 m)` on `|lam| <= 1.7627`, crossover clause W.6, supersession of grid certs | 2 referees MINOR_REPAIRS; repair list DISCHARGED (`repairs_20260811.md` §A, verified SURVIVES) |
| 5 | `wp2_draft_b.md` | W.0–W.7: exact `Delta_ker` decomposition (W.7), buckets PW/T/Lin, envelope `c_w` (W.6, repaired), floors `c_1/c_2/c_4` (W.1) | 2 referees MINOR_REPAIRS; repairs B1–B8 DISCHARGED (`repairs_20260811.md` §B) |
| 6 | `repairs_20260811.md` | all wave-1 repair lists applied; Lemma T.9-Step2' (`0.362 + 0.09 = 0.452 < 0.5` closes T.9 Step 2's `c_w = 1/2` sub-claim) | verified SURVIVES (`referee_repairs_20260811.md`) |
| 7 | `wp2_draft_a2.md` | Theorem D.5 (`C_ker(K) = 30.89/209.03/37811`, `M(K) = 180/181/367`) + **Theorem T.9-final = Prop 3.5(ii)** | 2 referees MINOR_REPAIRS (`referee_maths_wp2_a2.md`, `referee_numerics_wp2_a2.md`); repair list = STATUS_wave2 §2a (text-level; pending application file) |
| 8 | `wp3_draft_a2.md` | Theorems P.5/P.6/P.7/P.8 + **Theorem S** (the stitch; the CL spec §6.1) | 2 referees MINOR_REPAIRS (`referee_maths_wp3_a2.md`, `referee_numerics_wp3_a2.md`); repair list = STATUS_wave2 §2b (this document quotes the REPAIRED values: `rho(4) = 0.72711`, E-decimals, "82" crossover, Lin no-double-count) |
| 9 | `harness_m200_20260811.md` | exact ground truth C1–C6, `4 <= m <= 400` | exact finite computation (proof-grade); consumed + spot-verified by three wave-2 referees; independently re-anchored to `m = 60` here (§4 block E) |
| 10 | **[wp4 — CL(79, 20, 0.89)]** | Prop 3.5(i)'s only needed instance (R2) | **OPEN** — the single conditional |
| 11 | this file + `assembly_checks.py` | the plug (§4) + the assembled statement | ZERO referees yet (the designated referee unit; house rule: two needed) |

### 5.2 Edge list (what feeds what)

```
F2_PROOF_DRAFT (frame, L3.1-3.4, L3.6, Cor 2.3 stmt)
   |-- g1_draft_b B.0-B.9  ==> Cor 2.3 with constant 1.8/m^2   --> (UB) §2.4
   |-- L3.6 -----------------------------------------------------> R1a row
   |
wp3_a2: P.1-P.4 ==> P.5 (region-1 extension) -------------------> R1b row
        T.5-final (T2) ==> P.6 (s2 floor) --\
        (T.4)-Step2 (T2) ==> P.7 (deficit) --+--> R2 row  <== [WP4: CL] (OPEN)
        L3.1 ==> P.8 (tilt cap) ------------/
   |
wp2_b:  W.0-W.7 (exact decomposition; PW/T/Lin; c_w; c_K floors)
wp1_c:  W.3-W.6 (far bounds; c_1(K)) --\
T2:     T.9''/(T.8a)/T.1(ii) ----------+--> wp2_a2: D.1'-D.4 ==> D.5 (C_ker)
g1_b:   B.0(ii) -----------------------/         |
                                                 v
        W.7 + W.6 + W.4 + D.5 ==> T.9-final (= Prop 3.5(ii)) ---> R3 row [the PLUG, §4]
   |
harness_m200 (exact, m <= 400) ---------------------------------> Part I §2.1
repairs_20260811 (+ T.9-Step2') --- discharges wave-1 lists across wp1_c/wp2_b/T2
   |
Theorem S (partition R1a/R1b/R2/R3) + plug + Cor 2.3 + harness ==> THEOREM A
```

Blind-protocol note: `g2_draft_t1_20260803.md` is consumed NOWHERE (unread by
every wave-2/wave-3 agent and by both synthesis editors).

---

## 6. The constant ledger, end to end

Every named constant in the Theorem A chain, its value as consumed here
(post-repair), where it is proved, and its certification class. "exact" =
integer/`Fraction` arithmetic end-to-end; "closed" = displayed algebra with
safe-rounded evaluation; "grid" = grid-certificate class (§7 item 2).

**Frame and targets:**

| constant | value | source | class |
|---|---|---|---|
| `lambda = sigma^2` | `m(m-1)(2m+5)/72` | definition | exact |
| `B_m` | `(S_4 - m)/(240 lambda^2)`; `B_m m -> 27/25 = 1.08`, `B_m <= 1.080/m` (`m >= 30`, B.0(ii)) | merged draft / g1_b | closed |
| sharp constant, part (c) | `187/216`, attained `m = 6`, scope `m >= 5` (`varfit(4) = 91/108`) | F2 correction 1 + harness C5 | exact |
| harness range | `4 <= m <= 400`, C1–C6, 0 failures | harness_m200 | exact |
| Cor 2.3 center error | `|E| <= 1.2/m^2` (log form), `1.8/m^2` (`r-1` form), `m >= 180` | g1_b §7.3 (C_2(0.1) = 1.1, m_1 = 180) | closed |

**Far/decay machinery (wp1-c, T2):**

| constant | value | source | class |
|---|---|---|---|
| `c_1(K)`, `K = 1/2/4` | `0.2259 / 0.1802 / 0.1019` (margins `>= 9.1e-6`) | W.4(i), repair A1 | closed |
| far floor, all `|lam| <= 1.7627` | exponent `>= 0.0372 m` (`0.0373 m` on W.5(ii)) | W.5, repair A3 | closed |
| `m_2(K)` proxies | `143 / 190 / 267 / 379` (superseded: real `M(K)` below; kept for the record) | wp1-c §6, NC-T10d | proxy (retired) |
| Gaussian domination on `[0, pi/m]` | (T.6ii) | T2, two-referee | closed |

**Refined law (wp2-b + wp2-a2 = Theorem T.9-final):**

| constant | value | source | class |
|---|---|---|---|
| `c_1, c_2` variance floors | `s2 >= 0.967 / 0.868 * lambda` (`K = 1/2`) | W.1(i), repair B5 | closed |
| `c_4` floor | `s2 >= 0.60 lambda` (`K = 4`) | W.1(ii), repair B4 | **grid** |
| `c_w(K)` envelope | `0.407 / 0.466 / 1` | W.6, repair B2 | **grid** |
| `PW(K)` grid / closed | `1.5491/4.0889/4.9126` (`m <= 2000`; +0.22% caveat B3) / `10.278/21.063/187.414` | wp2-b | grid / closed |
| `C_R^PT(4)` (PW+T+Lin) | grid `5.32` (`= 4.93 + 0.01402 + 0.3719`, B3); closed `187.8` | repairs §B3 / wp3-a2 §5 | grid / closed |
| `C_ker(K)` | `30.89 / 209.03 / 37811` at `M(K) = 180 / 181 / 367` (table value `37810.0442` at 367) | wp2-a2 Theorem D.5 | closed (constant flavor `m > 3000`: **grid**) |
| `C_R(K) = PW + T + C_ker` | closed `41.17 / 230.09 / 37998`; grid `32.44 / 213.12 / 37815` | wp2-a2 T.9-final | mixed as marked |
| `m^2 Lin(K, 180)` | `0.2308 / 0.2571 / 0.3719`, decreasing | wp2-b W.5 | closed (uses Bona `r >= 1`) |
| `H(K, M(K))` (W.5 discharge) | `0.0097 / 0.0241 / 0.3321 <= 1/2` | wp2-a2 NC-A5(2); re-verified §4-F | exact recompute |
| T.9-Step2' | `|B_lam/B_m - 1| <= 0.362 w^2` (`|w| <= 1`, `m >= 30`); `0.362 + 0.09 = 0.452 < 0.5` | repairs §T1 | closed |

**Stitch (wp3-a2 Theorem S, repaired values):**

| constant | value | source | class |
|---|---|---|---|
| `C_P(c)` pentagonal correction | `12.34 / 36.17 / 83.61 / 263.23` (`c = 1/4, 1/2, 7/10, 1`) | P.4, NC-P2 | exact Fractions |
| `m_p(c)` P.5 thresholds | `30 / 83 / 300 / 1581` | P.5 | exact |
| P.5 truth check | 0 violations, all `2 <= k <= m-1`, `8 <= m <= 200` (+referee to 400); min slack 2.0002 | NC-P1 | exact |
| `v(c) = c(1+c)/6` | `v(7/10) = 119/600`; floors `79.53` (at 401), `527` (at 1581) | P.6; re-verified §4-C1 | exact |
| `E(w0)` lower decimals (REPAIRED) | `E(1) >= .00400692, E(2) >= .00358718, E(3) >= .00304035, E(4) >= .00248992, E(5) >= .00200652, E(6) >= .00161240` | P.7 + repair R2 | closed (positive partial sums, truncation `< 2e-15`) |
| `rho(4)` (REPAIRED) | `s2 <= 0.72711 lambda` on `|w| >= 4` (deficit `>= 0.27289`) | P.7 + repair R2 | closed |
| tilt caps | `lam <= log(17/7) < 0.89` (`c = 7/10`), `log 2 < 0.89` (`c = 1`), `log 3 <= 1.0987` (`c = 1/2`, unused) | P.8; exact cap proof §4-C5 | exact |
| CL spec | `(C_0*, C*, Lambda*) = (79, 20, 0.89)`, `m >= 401` | §3 (frozen) | — (OPEN) |
| `eps*` R2 tolerance | `1 - 1.02 * 0.72711 = 0.2583478` | Theorem S; re-verified §4-C2 | exact |
| R2 budgets | band 1: `20/79.5 = 0.251572`; band 2: `136/527 = 0.2580645` (margin `2.8e-4`) | re-verified §4-C3 | exact |
| R2 conclusion | `(1 - 20/79.5)/0.72711 = 1.0293 >= 1.02` | re-verified §4-C4 | exact |
| R3 `w^2` bracket at plugged `C` | `0.009575` (grid) / `0.009556` (closed) at `m = 401`, positive to 2000+ | NEW, §4-D | exact |
| **`C_A` (the Theorem A `O(m^{-2})` constant)** | **grid `37815.37` (`m <= 2000`); closed `37997.85` (all `m >= 401`)** | §2.3; re-verified §4-A | mixed as marked |
| plugged R3 value at `m = 401` | `0.762141` (grid) / `0.761006` (closed), increasing to 1 | §4-A2/A3 | exact |
| G4 crossovers (NOT Theorem A) | `m* = 535` (grid) / `537` (closed); K=1 center flavor `m* = 22` | §4-B | exact |

**Size honesty.** `C_A ~ 3.8e4` is dominated by `C_ker(4)`, whose truth
anchor is `~5.04` (wp2-b NC-W4(6)) — a 7500x triangle-inequality inflation,
documented mechanism (the K = 4 real-part split at the box bucket, wp2-a2
§9), with the flagged mechanical sharpenings in wp2-a2 §10 item 3. For
Theorem A the size is irrelevant (any fixed constant is absorbed by
`O(m^{-2})`); it matters only for the G4 band, §7 item 7.

## 7. Standing caveats (complete, none hidden)

1. **The single conditional.** R2's row rests on `CL(79, 20, 0.89)` — open
   mathematics until wp4 lands (§3). Nothing else in the chain is
   conditional on unproved mathematics.
2. **Grid-certificate-class inputs** (finite exact scans standing in for a
   displayed-algebra proof on part of a range; each Sturm-able, each
   attacked off-grid by referees without violation): (a) wp2-b's `c_4 =
   0.60` floor (integer `m in [30, 400]` x 200-pt `w`-grid, max 0.3796);
   (b) wp2-b's `c_w` envelope constants (repair B2 relabel; worst-at-180
   confirmed by fine scan + limit); (c) the `PW_grid` flavor (`m <= 2000`,
   +0.22% caveat B3 — the closed flavor 187.8 is fully proved and is what
   the all-`m` `C_A` uses); (d) wp2-a2's constant-flavor `C_ker(K, m)`
   monotonicity for `m > 3000` (unit-step to 1000, step 10 to 3000,
   referee-extended to `10^6`, no violation; the `m`-dependent form is a
   theorem for every `m` outright). A Sturm pass upgrading (a)–(d) is
   flagged mechanical in wp2-a2 §10 / STATUS_wave2 §4.
3. **Bona citation.** `r(k) >= 1` (log-concavity of the Mahonian row in the
   weak sense needed, i.e. `u = r(k) - 1 >= 0`) is consumed as an ambient
   literature citation (Bona) by wp2-b's W.5/Lin bucket. It is not
   re-proved in the campaign chain.
4. **Pending repair-application files** (all text/display-level; no
   constant, threshold, or verdict moves): STATUS_wave2 §2a (wp2-a2, items
   F1–F5/R-F1–R-F7), §2b (wp3-a2, R1–R8/F1–F8 — the repaired VALUES are
   already quoted throughout this document), §2c (T2 maths M-items — the
   two content repairs T.10(2)/T.8'' are consumed nowhere here). Until the
   `t2_repairs` file exists, T.10(2) and T.8'' must not be cited as
   displayed — this document does not cite them.
5. **Referee status of this document.** The plug (§4) and the assembled
   statement are synthesis-level: checked by STATUS_wave2's editor and
   independently re-verified here, but NOT yet two-refereed as a unit.
   House rule: this file + `assembly_checks.py` is the referee unit, to be
   sent together with wp4's draft when it lands.
6. **Proxy threshold retired, for the record.** Theorem S's text names
   `m_2(4) = 379` (proxy criterion, wp3-a2 §6.3); the binding threshold is
   now Theorem D.5's real `M(4) = 367 <= 401` (repair R6's qualifier is
   thereby substantively discharged; the wp3-a2 text repair still applies
   to that draft as written).
7. **G4-only band (NOT Theorem A).** With the crude `C_A`, the plugged
   lower bound first reaches `187/216` at `m* = 535` (grid; 537 closed) —
   for the part-(c) CONSTANT chase this leaves `[401, 534]` above the
   harness's 400, to be closed by either a harness run to `~540` (minutes
   at the measured `~m^3` scaling) or the flagged `C_ker(4)` sharpenings.
   Theorem A's `O(m^{-2})` absorbs any fixed constant and is unaffected;
   part (c) as stated in §0's finite companions is exact-harness territory
   (`m <= 400`) plus the same `[401, 534]` caveat under G4.
8. **Harness report display erratum (found this session).** The harness
   REPORT (`harness_m200_20260811.md` §3, C5) displays scope "4 <= m <=
   400"; the runner exempts `m = 4` by design (`varfit(4) = 91/108 =
   0.8426 < 187/216`; comment: "predates the sharp bound's range, 5 <= m").
   Correct scope: `5 <= m <= 400`, equality only at `m = 6` — consistent
   with F2_PROOF_DRAFT statement-correction 1. Fold into the next repairs
   file; no consumer of C5 uses `m = 4`.
9. **Exact center.** `N` even, `k = N/2` (`lam = 0`) sits formally outside
   T.9-final's `0 < |lam|` hypothesis; covered by B.8/Cor B.9 (§2.3's
   center note). The UB side (§2.4) is B.9-based and unaffected.
10. **What Theorem A does NOT claim.** Part (b)'s fine scale beyond
    `m = 400` (G3) and part (c)'s all-`m` constant chase (G4) remain open
    ledger items; wave-2 materially helps both (harness 400; explicit
    region-3 constants) but this document closes neither.

## 8. Ratification checklist for the human co-author

To ratify Theorem A as PROVED (conditional), verify in order — estimated
half a day with the files open:

1. **Statement** (§0) against `F2_PROOF_DRAFT.md` Theorem A + statement
   corrections 1–2 (the `187/216`/`m = 6` and `m = 4` facts).
2. **Part I**: skim `harness_m200_20260811.md` §2–§3; optionally re-run
   `run_m200.py --mmax 100` (seconds) and `assembly_checks.py` (block E is
   an independent rebuild).
3. **The partition** (§2.3): Theorem S's four regions are exhaustive and
   disjoint by definition (`K_c` split + `|w| <> 4` split); check the four
   rows' citations exist at the claimed statuses (§5.1 table).
4. **The plug** (§4): five compatibility checks; re-run
   `assembly_checks.py` and diff against `out_assembly_checks.txt`.
5. **The UB** (§2.4): g1_draft_b §7 item 3 (one paragraph) + `r_m <= r(k_c)`.
6. **The conditional** (§3): confirm the spec here is verbatim wp3-a2
   §5/§6.1 and that `[WP4-CITATION]` occurs exactly once as a load-bearing
   condition (the R2 row of §2.3; every other occurrence is a reference to
   that row or a flip instruction).
7. **Caveats** (§7): accept or escalate each of items 2 (grid class), 3
   (Bona), 4 (pending text repairs) as publication-acceptable.
8. When wp4 lands two-refereed: execute §3's flip instruction; commission
   the two referees for THIS document (house rule) if not already run.

*End of theoremA_assembly_20260811.md. Blind protocol maintained
(`g2_draft_t1_20260803.md` unread; no wp4 file read beyond the frozen spec
as recorded in wp3-a2); no existing file modified; scripts saved and run
with output archived (`g2_scripts/campaign_20260811/theoremA_assembly/`).*
