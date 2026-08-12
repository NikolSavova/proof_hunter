# CL_composition — the assembled core lemma CL(79, 20, 0.89) at m >= 561: composition note (wave 5)

*Wave-5 composition deliverable, F2 campaign, 2026-08-12 — the single
document that STATUS_wave4 §3 item 6 / §5 item 5 ordered: the statement
CL(79, 20, 0.89) for `m >= 561` assembled as ONE composed theorem from the
refereed pieces, with the composed constant chain re-verified end-to-end by
a fresh script. Sources consumed (each at the referee status listed in §1):
`wp4_draft_composite.md` (Theorems A2/A3/C.1 + the CL-composite frame),
`wave4_sl3p_ROUTE_20260812.md` + `wave4_sl3p_20260812.md` (Theorem SL3'),
`wave4_sliver_20260812.md` (SLV.1/SLV.2/SLV.3) + the hygiene overlay
`wave4_hygiene_20260812.md` (sliver repair m1 executed: `M_H = 560`
CERTIFIED; SL3' §2b errata recorded), `wave4_sl4p_repaired_20260812.md`
(Theorem SL4'-R, Fact R.G, Lemmas R.1/R.2, Cor R.3) + its two wave-5
referees, `wave5_sl4pe_20260812.md` (Theorem E, Prop E.3, Lemma E.4,
hypothesis (E3)) + its two referees, `wave5_sl4px_20260812.md` (Theorem
X.1, Cors X.2/X.3) + its two referees, and the harness results files
(parsed, not modified). `g2_draft_t1_20260803.md` remains unread;
`gamma = 1/8` is not re-litigated; no existing file is modified (new files
only). New script (SAVED and RUN 2026-08-12, output archived beside it,
quoted verbatim in §3):
`g2_scripts/campaign_20260811/wave5_composition/compose_chain.py`
(`out_compose_chain.txt`).*

**Bottom-line status: PARTIAL — NO GRADE INFLATION, NO FLIP.**
Theorem CL-C below assembles **CL(79, 20, 0.89) restricted to `m >= 561`**
— which is, by the sliver closure, the ENTIRE remaining CL obligation —
from inputs that are now EVERY ONE two-referee citable, with the composed
constant chain re-verified end-to-end here (final composed constant
`C*(m >= 561) = 18.2281 <= 20`; at `m >= 1581`, `13.0594 <= 136`,
headroom 10.41x; `[401, 560]` closed by exact integer computation, 557/557
rows PASS, zero gaps). Wave 5 discharged TWO of the four wave-4 hypotheses
outright: **SL4'-X is PROVED** (Theorem X.1, two-referee
MINOR_REPAIRS/SURVIVES — and independently mooted on `[561, 699]` by the
maths referee's M3 construction), and the **SL4'-E pricing machinery is
PROVED** (Theorem E, two-referee MINOR_REPAIRS/MINOR_REPAIRS) — but
Theorem E is conditional on a NEW named hypothesis (E3) = SL4'-E-J that
Prop E.3 shows is unavoidable, and **the SL1' prover slot produced NO
artifact for the third wave running** (statuses at composition time:
sl1pw — no artifact, zero referee verdicts; sl4pe — MINOR_REPAIRS,
MINOR_REPAIRS; sl4px — MINOR_REPAIRS, SURVIVES). Additionally the repaired
SL4's first-ever maths referee exposed the INFL/QUADF bootstrap's missing
seed bound (finding M2), which this note carries into the surface as (S4)
rather than hiding it. **Therefore CL(79, 20, 0.89) — and with it Theorem
A — remains PROVED CONDITIONAL on exactly the four named open statements
(S1)–(S4) of §4, all of one kind (core-model cumulant/seed class), none
with a proof artifact.** The implication [(S1)–(S4) ==> CL at `m >= 561`]
is, after this note, complete and two-referee at every node.

## 0. The target, verbatim, and the split

The target is `wp3_draft_a2.md` §6.1's core lemma, as restated by the
composite §3: for every interior `k` with mean-matching tilt
`|lam(k)| in (4/m, Lambda* = 0.89]`,

```
s2 (r(k) - 1) = 1 + theta * C*/min(m, s2) ,   |theta| <= 1 ,   C* = 20 ,
```

(both tilt signs via the mirror; the `s2 >= C_0* = 79` clause never binds
since `s2 >= 1122800/7921 = 141.7497...` on the whole band, [A2](iii));
relaxed constant `C* = 136` suffices for `m >= 1581` (wp3-a2 §6.1 second
clause). The obligation splits exactly as Cor SLV.3 pre-authorized:

- **`m in [401, 560]`: discharged at CONSUMER level by exact
  computation.** The exact integer harness (C1–C6, exact Fractions)
  PASSes every integer `m in [4, 560]` (§3 block [A]: 557 data rows, zero
  non-PASS, zero gaps; `# OVERALL: PASS` quoted verbatim). This is Theorem
  A's finite part directly — no CL-type lemma is needed there at all. It
  is NOT a lemma-level proof of CL on `[401, 560]` (the distinction the
  sliver note and both its referees drew; inherited here unchanged).
- **`m >= 561`: the lemma-level obligation** — the subject of Theorem
  CL-C (§2).

## 1. Input inventory (referee status of every consumed piece)

| # | Input | File(s) | Referee status | What is consumed |
|---|---|---|---|---|
| I1 | CL-composite frame + Theorems A2/A3/C.1 + [W.6] | `wp4_draft_composite.md` (with `wp1_draft_c.md`, `wp4_sl_SL2/SL3.md`) | two-referee (`referee_maths_wp4.md`, `referee_numerics_wp4.md`) | band floors `c_A(W)` (W7 certified `0.852716`), `s2 >= 141.7497`, tier-1 `c1 = 0.1317` / tier-2 `c2 = 0.0871`, far floor `0.0741`, `t_0 <= 1.074 lam`, Lemma C.1 `A <= m`, the W.6 crossover exponent |
| I2 | **Theorem SL3'** (mid-exponent bands `gamma* = 0.42/0.42/0.40/0.40/0.38/0.34/0.32`, all `m >= 401`, `t in (0, 0.8 lam]`) | `wave4_sl3p_ROUTE_20260812.md` + `wave4_sl3p_20260812.md` | **two-referee MINOR_REPAIRS** (`referee_maths_wave4_sl3p.md`, `referee_numerics_wave4_sl3p.md`); §2b errata recorded in `wave4_hygiene_20260812.md` | the W1–W4 mid-slot exponents `0.42/0.42/0.40/0.40` (W5–W7 ride PROVED tier-1 and never touch SL3'); load-bearing also inside Lemma R.2 (maths-referee M1) |
| I3 | **SL-sliver closure** (Lemma SLV.1, Fact SLV.2 `M_H = 560` CERTIFIED, Cor SLV.3) | `wave4_sliver_20260812.md` + `wave4_hygiene_20260812.md` §1 (repair m1 executed) | **two-referee MINOR_REPAIRS** (`referee_maths_wave4_sliver.md`, `referee_numerics_wave4_sliver.md`) | the threshold shift `m >= 561`; the W1 far entry `<= 0.05` for all `m >= 451`, `w >= 4` (1097x headroom at 561, §3 block [F]) |
| I4 | **Theorem SL4'-R** (kernel-weighted honest ledger, repaired) + Fact R.G + Lemmas R.1/R.2 + Cor R.3 | `wave4_sl4p_repaired_20260812.md` (proofs of SL4'.1–.8 by reference to `wave4_sl4p_20260812.md`) | **two-referee MINOR_REPAIRS** (`referee_maths_sl4p_repaired.md`, `referee_numerics_sl4p_repaired.md`); text repairs R1/R2/RF-1/RF-2 recorded, none moves a constant (§5) | the seven-row ledger and the W1 closure ladder; the trapezoid `(4, w†(m)] x [401, 462]` (moot at `m >= 561`, Cor R.3) |
| I5 | **Theorem E** (eta-pricing machinery at `m >= 561`) + Prop E.3 + Lemma E.4; hypothesis **(E3)** | `wave5_sl4pe_20260812.md` | **two-referee MINOR_REPAIRS** (`referee_maths_wave5_sl4pe.md`, `referee_numerics_wave5_sl4pe.md`) | the `main`-row pricing `|eta| <= [R42*/2 + 0.3 R31*^2 + lam^2/2] u`, now a THEOREM given (E1)+(E2)+(E3); the interface delta (sign-lemma route refuted) |
| I6 | **Theorem X.1** (SL4'-X, strengthened: `x(w, tau)` strictly increasing on `[0.8, 1.074]`, all `w >= 4`) + Cors X.2/X.3 | `wave5_sl4px_20260812.md` | **two-referee** (`referee_maths_wave5_sl4px.md` MINOR_REPAIRS, `referee_numerics_wave5_sl4px.md` SURVIVES) | certifies the ledger's `X_w6` left-endpoint sums (Fact R.G's runtime flag is now a theorem) |
| I7 | exact harness results | `wave2_repairs/results_m540.txt` rows 4..481 (honored), `harness_m560/results_m560.txt` rows 482..560 | coverage certified by both sliver referees + independent parses in I4's [D6], its numerics referee's split-parse, and §3 block [A] here (a fourth method) | the `[4, 560]` finite part |
| — | **SL1' deliverable (SL1'-w + (E3) + seed)** | **— none —** | **NO ARTIFACT, zero verdicts (third wave running)** | nothing — this is the open surface (§4) |

House-rule reading: every input I1–I7 is citable (two-referee
MINOR_REPAIRS-or-better, or better-covered coverage certification). The
single missing node is the SL1'-class deliverable. Supporting single-
verifier items, consistent and discharged: `referee_wave3_repairs.md`
(SURVIVES on `wave3_repairs_20260812.md`) and `referee_wave2_repairs.md`
(MINOR_REPAIRS, W-F1 relabel recorded in the hygiene overlay).

## 2. Theorem CL-C: the composed statement and proof

**The four open hypotheses (statements verbatim in §4):** (S1) =
SL1'-w(i); (S2) = SL1'-w(ii); (S3) = (E3) = SL4'-E-J; (S4) = the
SL4'.6/.7 bootstrap seed.

**Theorem CL-C (the composed core lemma; conditional).** *Assume
(S1)–(S4). Then for every integer `m >= 561` and every interior `k` with
`|lam(k)| in (4/m, 0.89]`:*

```
s2 (r(k) - 1) = 1 + theta * 20/min(m, s2) ,   |theta| <= 1 ,
```

*with NO exception set — i.e. CL(79, 20, 0.89) restricted to `m >= 561`,
which by Fact SLV.2/Cor SLV.3 is the entire remaining CL obligation.
Moreover the constant actually delivered along the composed chain is
`C*(m >= 561) = 18.2281 < 20` (worst certified row bound `0.911407`,
attained by Lemma R.2's W1 tail bound at `m = 700`; §3 block [D]), and
for `m >= 1581` the chain delivers `13.0594 <= 136` against wp3-a2 §6.1's
relaxed clause. Combined with the `[401, 560]` consumer-level discharge
(§0), Theorem A = F2(a) is PROVED CONDITIONAL on exactly (S1)–(S4).*

*Proof (assembly; every citation two-referee per §1).* WLOG
`lam = lam(k) > 0` (mirror frame, composite §0/§3; the exact center is
covered upstream by g1_draft_b B.8). Let `W` be the band of `w = m lam`.

1. *(The ledger applies.)* By (S1)+(S2), the banded cumulant scales
   `R31*/R42*/C5*` hold; by (S1)+(S3) and **Theorem E** [I5], the model
   term is priced: `|eta| <= [R42*(W)/2 + 0.3 R31*(W)^2 + lam^2/2] u` —
   exactly the ledger's `main` entry (§3 block [E]: the W7 entry is
   exactly `J*(W7) + 0.89^2/2 = 5.14805`, and `J0 = J* - REM*` with
   `REM* <= 0.3 R31*^2` re-verified on all seven bands). By (S4) and the
   maths referee's monotone-iteration closure (M2 of
   `referee_maths_sl4p_repaired.md`, adopted here: `G` convex increasing,
   `G(20/m) < 20/m` at both thinnest rows, chord argument on
   `[20/m, 0.89]`), the INFL/QUADF bootstrap of Lemmas SL4'.6/.7 closes,
   so **Theorem SL4'-R** [I4] applies with its exception trapezoid
   `T subset (4, 4.095] x [401, 462]`.
2. *(W2–W7 rows, all `m >= 561`.)* Certified at `m = 401` (worst W5
   `0.98909`, W7 `0.98084` — reproduced in §3 block [B]) and every entry
   closed-form nonincreasing in `m` on the used range (I4 §3 + [D3]
   scans + wave-4 referee B4; spot-verified at 561/601/1581 in block
   [B]). At the operative threshold the worst W2–W7 row is `0.872304`
   (W7 at 561). The mid slot on W2–W4 consumes **Theorem SL3'** [I2];
   W5–W7 consume only PROVED tier-1.
3. *(W1 rows — the three-rung ladder, no exception at `m >= 561`.)* The
   trapezoid `T` has max `m = 462 < 561`: MOOT (Cor R.3 item 1, with the
   harness parse re-verified in block [A]). On `m in [561, 699]`: **Fact
   R.G** [I4] (25,122 probes, 0 failures, worst `0.424939` at
   `(561, 4+1e-9)`; sentinels reproduced in block [C]; plus the numerics
   referee's 3,594 extra off-grid probes, 0 failures) — with the
   left-endpoint sums now CERTIFIED by **Theorem X.1/Cor X.3** [I6]
   (SL4'-X is a theorem, not a hypothesis), and independently the maths
   referee's M3 per-cell construction closes the same rung analytically
   with no `w`-grid and no monotonicity input (worst `0.416537` at 561).
   On `m >= 700`: **Lemma R.2** [I4] (+ Lemma R.1's floor `0.0176`,
   epsilon-rigorous; + Theorem SL3' named per maths-referee M1) gives the
   W1 row `<= 0.911407`, recomputed from its closed form in block [C],
   nonincreasing in `m`.
4. *(Far obstruction absent.)* **Lemma SLV.1** [I3]: the W1 far entry is
   `<= 0.05` for all `m >= 451`, `w >= 4`; at `m = 561` the headroom is
   1097.6x (block [F]). The `tau_0/lam <= 1.074` cap that every crossover
   evaluation needs is Cor X.2's (block [F]: `1.07372378 <= 1.074`).
5. *(Conclusion.)* Every band row is `<= 1` for every `m >= 561`, i.e.
   the share criterion (Lemma SL4'.8') delivers
   `|s2(r(k)-1) - 1| <= 20/min(m, s2)` (`min(m, s2) = m` on the band,
   [A2](iii)-bonus), with worst certified row bound
   `max(0.872304, 0.424939, 0.911407) = 0.911407` — the composed
   `C* = 18.2281 <= 20`. For `m >= 1581` the same chain evaluated there
   gives worst row `max(0.65297, 0.205265) = 0.65297`, i.e.
   `C* = 13.0594 <= 136` a fortiori. The variance floor and mirror close
   the statement as in the composite §3 proof. ∎

*Remark (what moved since wave 4).* The wave-4 conditional surface was
{SL1'-w, SL3'-w, SL4'-E, SL4'-X}. Wave 5: SL3'-w was DISCHARGED by
Theorem SL3' (I2, consumed by the repaired ledger); SL4'-X was PROVED
outright (I6) and separately mooted on the operative range (M3); SL4'-E
was SPLIT — its machinery is now Theorem E (I5), its content the new
cumulant-only hypothesis (E3); and the first maths pass over SL4' surfaced
the bootstrap seed (S4) that all earlier statements undercounted. Net: the
surface is smaller and sharper, but NOT empty.

## 3. The composed constant chain, re-verified end-to-end (script, verbatim)

Script `wave5_composition/compose_chain.py` (row machinery =
`sl4pr_common.py`, the twice-validated engine: referee-rebuilt from the
draft's closed forms to `< 5e-5` in wave 4, byte-audited in wave 5;
harness parse = exact string arithmetic, a FOURTH independent parse
method; mpmath dps-40 point-evaluation class, house-approved). Output
`out_compose_chain.txt`, quoted verbatim:

```
[A] exact harness coverage (threshold shift)
  data rows honored/fresh union: 557;  PASS rows: 557;  non-PASS: 0
  gaps in [4, 560]: NONE;  gaps in [401, 560]: NONE
  OVERALL line (verbatim): # OVERALL: PASS -- all of C1..C6 hold exactly for 4 <= m <= 560 (C2/C3 with the known m=4 exception; rows split across this file and the honored prior file(s)).
  [A] coverage m in [4, 560] exact-PASS, threshold shifts to m >= 561: True
```

```
[B] the seven ledger rows: m = 401 (SL4'-R certification) and m = 561 (operative)
  m= 401:  W2=0.86008  W3=0.65844  W4=0.58993  W5=0.98909  W6b=0.82768  W7=0.98084
  m= 561:  W2=0.35065  W3=0.48309  W4=0.51831  W5=0.70933  W6b=0.69981  W7=0.8723
  m= 601:  W2=0.32987  W3=0.47332  W4=0.50993  W5=0.68992  W6b=0.68614  W7=0.85384
  m=1581:  W2=0.26088  W3=0.38904  W4=0.41952  W5=0.553  W6b=0.55132  W7=0.65297
  reference reproduction at 401: W5 = 0.98909 (~0.9891), W7 = 0.98084 (~0.9808): True
  all W2-W7 rows at m = 561 <= 1: True;  m-monotone spot (561 >= 601 >= 1581): True
  worst W2-W7 row at m = 561: 0.872304 (W7)
```

```
[C] W1 closure ladder on m >= 561
  m=561: worst probe row = 0.424939 at w = 4.000000001  (all <= 1: True)
  m=650: worst probe row = 0.289044 at w = 4.000000001  (all <= 1: True)
  m=699: worst probe row = 0.261345 at w = 4.000000001  (all <= 1: True)
  Fact R.G sentinel reproduction: worst = 0.424939 at (m, w) = (561, '4.000000001');
  X_w6 monotone-in-tau flag (Theorem X.1, now PROVED) at every probe: True
  Lemma R.2 recomputed: m=700: B = 11.1999, dec_W1 = 1.23288, W1 row bound = 0.911407 (<= 0.9115: True)
                        m=1000: 0.231364   m=1581: 0.205265   (B nonincreasing for m >= 142.05)
```

```
[D] the COMPOSED effective constant
  segment worsts: W2-W7@561 = 0.872304 | W1[561,699] = 0.424939 | W1[700,inf) = 0.911407
  composed worst row bound on m >= 561 = 0.911407  ->  C*(m >= 561) = 18.2281 <= 20: True
  m >= 1581: worst W2-W7 row = 0.65297 (W7), W1 tail bound = 0.205265
  C*(m >= 1581) = 13.0594 <= 136: True   (headroom 10.41x)
  (reference: SL4'-R certification at m = 401: C*_eff = 20 x 0.98909 = 19.782 <= 20)
```

```
[E] eta-pricing interface (wave5_sl4pe Theorem E vs the ledger main row)
  W1: J* = 0.7;  J* - REM* = 0.682942 vs quoted J0 = 0.682942 (match: True);  REM* <= 0.3 R31*^2: True
  W7: J* = 4.752;  J* - REM* = 4.59597 vs quoted J0 = 4.59597 (match: True);  REM* <= 0.3 R31*^2: True
  all 7 bands: J0 = J* - REM* consistent AND REM* <= 0.3 R31*^2: True
  ledger main(W7) = R42*/2 + 0.3 R31*^2 + lam_max^2/2 = J*(W7) + 0.89^2/2 = 5.14805 (exact Fraction)
  (exactly 4.752 + 0.39605 = 5.14805: True; the sl4pe maths referee's '5.148' is 3-dp display)
```

```
[F] sliver far-entry headroom at the operative threshold + X.2 cap
  far'(561, 4) = 4.556e-5  (slot 0.05; headroom 1097.6x  [SLV note: 4.556e-05, 1097.6x])
  tau_0(0.89)/0.89 = 1.07372378 <= 1.074 (Cor X.2 edge): True

== COMPOSED-CHAIN VERDICT ==
  [A] harness/threshold: True  [B] rows@561: True  [C] W1 ladder: True  [D] C* budgets: True  [E] eta interface: True  [F] sliver/X.2: True
  ALL CHECKS PASS: True
```

Reading of the chain: the composed constant on the operative range is set
by Lemma R.2's deliberately crude (but sufficient) W1 tail bound at
`m = 700` — `C* = 18.2281`, i.e. 9% assembly headroom against the spec's
20; the thinnest certified point of the whole composed object remains the
SL4'-R theorem-level W5 row at `m = 401` (`0.98909`, dps-100-robust per
its referee) — which at the OPERATIVE threshold relaxes to `0.70933`.
Nothing in the composition spends the sliver's thin 451-endpoint margin
(5.15%), Theorem SL3''s 1.30x crossover-certificate margin (its cited
worst), or the W7 `min(m,s2) = m` 1.0% margin beyond what the source
files already spent.

## 4. The conditional surface: exactly four named statements, none proved

All four are core-model statements about the tilted Mahonian cumulants /
ratio — no tail content, no `qhat`/`eta` content (that is now Theorem E's
job). Statuses: ALL CONJECTURED; the SL1' prover slot has produced no
artifact in waves 3, 4, or 5.

- **(S1) [SL1'-w(i)] Banded cumulant scales.** For `m >= 561`,
  `lam in (4/m, 0.89]`, band `W`:
  `|kappa_3| <= R31*(W) s2/lam`, `kappa_4 <= R42*(W) s2/lam^2`,
  `R31* = 1.0/1.2/1.5/1.7/2.0/2.1/2.2`,
  `R42* = 0.8/1.4/2.6/3.5/5.2/6.0/6.6`. *Evidence:* truth at the W7 deep
  corner `2.1215/6.3552` vs caps (headroom 3.7%/3.9%, geometric limits
  `2.1303/6.4113` — the F2-corrected margins, THE binding truth margins
  of the campaign); sl4pe's 27-point `m = 561` audit: `r31 <= R31*`,
  `r42 <= R42*` at every probe.
- **(S2) [SL1'-w(ii)] Core remainder.** Same scope:
  `log phi(t) = -s2 t^2/2 - i kappa_3 t^3/6 + kappa_4 t^4/24 + R5(t)` with
  `|R5(t)| <= C5*(W) s2 t^5/lam^3` on `[0, lam/2]`,
  `C5* = 0.05/0.06/0.08/0.10/0.15/0.25/0.80`. *Evidence:* measured truth
  `0.0083–0.2104`; ledger acceptance slack 1.6x–8x band-wise (W6b 1.6x;
  W1's slack is `w = 4.30`-class, NOT uniform to the band edge — F4
  scoping inherited).
- **(S3) [(E3) = SL4'-E-J] Joint cancellation bound.** Same scope, with
  `r31 := |kappa_3| lam/s2`, `r42 := kappa_4 lam^2/s2`:
  `J := r31^2 - r42/2 <= J0(W) = 0.682942/1.10268/1.91562/2.53645/
  3.66793/4.17806/4.59597` (exact rationals archived in I5's script [1]).
  *This is wave 5's NEW obligation and it is UNAVOIDABLE:* Prop E.3
  (verified by both I5 referees) exhibits a hypothesis-consistent point
  where SL1'-w(i) + `kappa_4 >= 0` hold and the pricing fails by 43% — the
  wave-4 proof plan ("exact algebra + sign lemma") is DEAD, and the truth
  at the W1/W2 right edges independently forces the joint form
  (`r31^2 = 0.7857 > J* = 0.7` at `(561, w = 5)`). *Evidence:* worst
  measured margin 32.6% at `(m, w) = (561, 5.0)`, per-band maxima at the
  right edges, `m`-direction favorable on W1–W6b, W7 margin 71%; roadmap
  (limit certificates + one Euler–Maclaurin lemma; W7 needs only
  `r42 >= 0.488` vs truth `>= 5.46`) and Lemma E.4's limit-level
  `kappa_4` positivity (`G_4(w) >= 0.2323` for `w >= 4`) are in I5.
- **(S4) [Bootstrap seed] A-priori ratio bound.** For `m >= 561` and
  `lam(k)` in-band: `|s2(r(k) - 1) - 1| <= 0.89`. *Provenance:* finding
  M2 of `referee_maths_sl4p_repaired.md` — the INFL/QUADF
  self-consistency of Lemmas SL4'.6/.7 is a fixed-point ansatz; GIVEN any
  such seed, the referee's chord/monotone-iteration argument (offered
  verbatim, adopted in §2 step 1) closes it, with strict contraction at
  the target (`G(20/m) < 20/m`, margins 1.4%/2.5% at the two thinnest
  rows; seed basins `x_seed = 0.90182/0.89412`). *Evidence:* CL truth
  itself at `m = 401/402` (REF-B, 17.1x margin) and every measured ratio
  in the campaign sit far inside `0.89`; the statement is weak-CL-shaped
  (log-concavity of the tilted law would give the lower side). *Natural
  home:* the SL1' deliverable, alongside (S1)–(S3).

**Why the surface is exactly this.** Theorem E turns (S1)+(S3) into the
`main`-row pricing; (S2) prices the R5 slots; (S4) closes the bootstrap;
everything else in every row of the ledger is PROVED input (I1/I2/I3/I6).
No other unproved statement is consumed anywhere in §2's proof — this was
checked against the honesty ledgers of I4 (as corrected by its maths
referee's M1/M2) and I5/I6, and no CONJECTURED item is consumed silently.

## 5. Honesty register (nothing hidden)

1. **No flip.** This note does NOT flip Theorem A. The flip requires
   (S1)–(S4) proved and refereed, then the flip-time re-run of
   `assembly_checks.py` block C at the landed weaker spec (flag f3;
   band-2 margin `2.83e-4` is the tight one), then assembly §8's human
   ratification. None of that is claimed here.
2. **Pending text repairs on I4, recorded not applied** (no-erasing
   rule): R1 (name Theorem SL3' in Lemma R.2's hypothesis list — this
   note already cites R.2 WITH SL3' named), R2 (carry the bootstrap-seed
   flag in SL4's own status lines — this note carries it as (S4)), RF-1
   (efac 5-dp display rounds past the boundary; the safe cutoff `0.8464`
   is what the lemma uses), RF-2/m4 (one comment line in
   `sl4pr_common.py`'s provenance claim). None moves a constant, bound,
   or verdict (both referees). Similarly I5's four commentary-level and
   I6's wording-level findings (m1: the "certified upper bound" sentence
   carries its sl4p-pricing qualifier — observed here in §2 step 3's
   phrasing).
3. **Certificate classes, inherited flags:** Theorem SL3' is proved
   modulo its flagged finite monotone-cell certificates (E.5.3,
   E.6.A/B/C; worst certified crossover margin 1.30x at W7's
   `tau_start`, truth ~16x); Fact R.G is grid-class over the
   `w`-continuum (complete integer `m`-quantifier; open-edge probed to
   `4 + 1e-9`; one-crossing shape evidence; M3's analytic per-cell
   alternative removes the `w`-grid on the operative rung); Lemma E.4's
   two dps-30 point evaluations (reconfirmed dps-50/60 by referees) and
   the six NX constants are the accepted named-constant class; the
   ledger row evaluations are mpmath dps-40 on the twice-validated
   engine. Rows `4..481` of the harness are honored `results_m540.txt`
   rows (wave2_repairs referee discharged single-verifier; fresh
   from-scratch re-run flag f1/m6 unchanged — record-only).
4. **This note's own referee debt:** ZERO referees (new file). Under
   house rules the composed statement should be refereed as a unit
   before the paper cites it (STATUS_wave4 §3 item 6 anticipated this).
   Its script is deliberately thin — every heavy certificate lives in,
   and is cited to, the refereed source files; the script re-verifies
   interfaces, sentinels, and the two budget comparisons only.
5. **Truth side (unchanged, corroborative only):** CL exactly TRUE at
   `m = 401/402` (REF-B: 260 adversarial `k`, 0 violations, 17.1x
   margin); SL3's 162- and 241-point truth attacks to `m = 10^6`, 0
   violations; sl4pe's 27-probe `m = 561` audit, all PASS. Nothing
   load-bearing consumes these.

## 6. Script table (this note's own; SAVED and RUN 2026-08-12)

| # | script (`g2_scripts/campaign_20260811/wave5_composition/`) | validates | key output (verbatim) |
|---|---|---|---|
| [CC] | `compose_chain.py` (`out_compose_chain.txt`) | §3 blocks [A]–[F]: harness parse (exact, 4th method), ledger rows at 401/561/601/1581, W1 ladder sentinels + R.2 closed-form recomputation, composed `C*` vs both budgets, eta-interface consistency (exact-Fraction main-row identity), sliver/X.2 caps | `ALL CHECKS PASS: True`; `C*(m >= 561) = 18.2281 <= 20: True`; `C*(m >= 1581) = 13.0594 <= 136: True (headroom 10.41x)`; `OVERALL line (verbatim): # OVERALL: PASS -- all of C1..C6 hold exactly for 4 <= m <= 560 ...` |

Consumed archived evidence (quoted as each file's own claim, per source):
I4's `out_sl4pr_{a,b,c,d}.txt` (trapezoid, 25,122-probe grid, R.1/R.2
certificates), I5's `out_e1_pricing_certificate.txt` (exact `REM*`/`J0`
fractions) + `out_e2_truth_margins.txt` (27-probe audit, Prop E.3 point)
+ `out_e3_limit_sign.txt` (Lemma E.4), I6's
`out_x_constants_and_scan.txt` (NX-1..6), both referees' archives for
I4–I6, and the two harness results files.

## 7. Status recap and what remains

- **Theorem CL-C: ASSEMBLED and chain-verified** — CL(79, 20, 0.89) at
  `m >= 561` is **PROVED MODULO (S1)–(S4)**, with `[401, 560]` closed by
  exact computation and every implication node two-referee. Composed
  constants: `18.2281 <= 20` (`m >= 561`), `13.0594 <= 136`
  (`m >= 1581`).
- **CL itself: STILL OPEN.** The failed piece is exactly the SL1'-class
  package: no artifact for (S1)/(S2), (S3) newly isolated by wave 5,
  (S4) newly surfaced by the first SL4' maths pass. **Theorem A remains
  PROVED CONDITIONAL on exactly (S1)–(S4)** — nothing more, nothing
  less. The paper may cite the §0 split and this note's conditional
  form; it must NOT say F2(a) is proved, and must not call CL "nearly
  proved" while (S1)–(S4) have no artifact.
- **Remaining work, in order:** (i) the SL1' deliverable = (S1)+(S2)+
  (S3)+(S4) — one prover, budget off the 3.7%/3.9% W7 cumulant margins
  and the 32.6% (E3) margin, roadmap in I5 §6; (ii) two referees on it;
  (iii) referee THIS note (unit check of the composition); (iv) apply
  the recorded text repairs (§5.2) in the next hygiene batch; (v) the
  flip: `assembly_checks.py` block C at the landed spec + assembly §8
  human ratification. Then G4 (its `[401, 536]` band is already
  computation-closed) and G3.

*End of CL_composition_20260812.md.*
