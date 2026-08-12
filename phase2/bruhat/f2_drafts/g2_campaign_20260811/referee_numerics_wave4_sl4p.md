# referee_numerics_wave4_sl4p — adversarial numerics referee report on `wave4_sl4p_20260812.md`

*Wave-4 referee pass, F2 campaign, 2026-08-12. Target:
`wave4_sl4p_20260812.md` (bridge piece SL4', kernel-weighted honest ledger)
and its scripts `g2_scripts/campaign_20260811/wave4_sl4p/sl4p_nc1_ledger.py`
(`out_sl4p_nc1.txt`), `sl4p_nc2_eta.py` (`out_sl4p_nc2.txt`). Protocol:
maximal bar, default to refutation (this chain flips the paper's main
conjecture to a theorem). Every prover script re-run and diffed; every seven
ledger rows independently re-implemented from the DRAFT TEXT's closed forms
(not the prover's code) at dps 60 and dps 100; off-grid adversarial probes at
the band edges, the sliver boundary, `m = 401/402/461/462/463`, the
`w ~ 4.9` eta-max locus, and the exact `lam = 0.89` corner. Blind protocol
kept (no other wave-4 draft read; `g2_draft_t1_20260803.md` not read). New
referee scripts (all SAVED and RUN, outputs archived beside them) in
`g2_scripts/campaign_20260811/referee_wave4_sl4p/`: `ref_nw4p_a_rebuild.py`,
`ref_nw4p_b_sliver.py`, `ref_nw4p_b2_boundary.py`, `ref_nw4p_c_eta_edges.py`,
`ref_nw4p_d_margins.py`, `ref_nw4p_e_gamma_sliver.py` (outputs
`out_ref_nw4p_{a,b,b2,c,d,e}.txt`). No existing file modified.*

## VERDICT: **MAJOR_ISSUES**

The assembly MECHANISM is sound and everything the prover computed
reproduces exactly — but the deliverable's headline quantification is
internally inconsistent: **Theorem SL4' as stated (hypothesis SL3'-w at
`gamma* >= 0.25` on W1) does not have certified support for its own quoted
sliver boundary `w†(401) = 4.10`, `m in [401, 461]`; under the STATED
hypothesis the correct trapezoid is `(4, 4.135] x [401, 469]` (finding F1),
and even under the ledger's actual `gamma* = 0.42` the trapezoid's `m`-range
is `[401, 462]`, not `[401, 461]` (finding F2).** Both repairs are fully
quantified below and nothing else in the file moves; but because the
repairs change constants in the theorem statement (the trapezoid — exactly
the object handed off to the SL-sliver piece), this exceeds
MINOR_REPAIRS-class under house rules. With F1's repair (either route) and
F2's `461 -> 462` applied, everything else in the file survived every attack
I ran.

## 1. Reproduction and independent rebuild (all clean)

- **Byte-identity.** Both prover scripts re-run byte-identical to their
  archived outputs (`diff` exact: "NC1 BYTE-IDENTICAL", "NC2
  BYTE-IDENTICAL"). Every number quoted in the draft's §4 ledger block, §5
  sliver block, §7 table, and the §2/§3 inline values traces verbatim to
  those outputs (the §7 "key verbatim output" column is condensed but
  faithful). Nothing fabricated.
- **Independent ledger rebuild** (`ref_nw4p_a_rebuild.py` [A1], dps 60,
  written from the draft's displayed closed forms): all seven
  `share*(1+q)` values agree with the quoted 4-dp values to `< 5e-5`
  (W1 `0.4578515`, W2 `0.8600829`, W3 `0.6584392`, W4 `0.5899293`,
  W5 `0.9890876`, W6b `0.8276761`, W7 `0.9808361`). Re-certified at
  **dps 100** ([D2]): W5 margin `0.0109124`, W7 margin `0.0191639` —
  the thin margins are real, not float artifacts.
- **Named constants** ([A6], exact): `48 sqrt(2pi)/pi = 38.29845892 <=
  38.2985`; `8 sqrt(2pi)/pi = 6.383076 <= 6.3831`; cube exact
  `3840/1296 * sqrt(2pi)/pi = 2.364102 <= 2.37`; cross exact
  `384/144 * sqrt(2pi)/pi = 2.127692 <= 2.13`; `k4^2` exact coefficient
  `945/1152 = 0.8203125`, dominated by `0.56/sqrt(A)` for `A >= 2.146`
  (draft's "A >= 3" safe); `2 sqrt(2pi) = 5.013257 <= 5.01326`. I re-derived
  by hand the full normalization chain for R5/cube/cross/mid/X-tier2/far
  entries (`int t^7 e^{-ct^2} = 3/c^4`, `int t^11 e^{-s2t^2/2} = 3840/s2^6`,
  `int t^9 = 384/s2^5`, both Mills forms, `int_0^pi 2(1-cos t) dt = 2pi`)
  — every stated closed form is exactly what the algebra gives, and the
  W2-row arithmetic reproduces by hand to 4 digits.
- **Block [5] budget** re-done with EXACT closed forms for the Hermite
  averages ([A3]): `E|He3| = 2 phi(0) + 8 phi(sqrt 3) = 1.510013`,
  `E|He4| = 4[He3(z2)phi(z2) - He3(z1)phi(z1)] = 2.800600`
  (`z_{1,2}^2 = 3 -+ sqrt6`) — the prover's mp.quad values 1.510/2.801
  confirmed by antiderivative identities; exact budget
  `Theta + dHe + dq = 0.08837444 <= 0.09` (margin 1.8%) and
  `1/(1-.) = 1.0969416 <= 1.10` (margin 0.28%): TRUE, tight as flagged.
- **W.6 formula fidelity**: `w6_x` is byte-level identical to the orphan
  `wp4_SL4/sl4_nc1.py` (checked); the orphan's archived
  "monotone-in-tau violations ... 0" line exists as quoted.

## 2. Findings (ranked most-severe first)

### F1 (MAJOR — hypothesis/certification mismatch on W1; the theorem's quoted sliver is not supported by its own stated hypothesis)

Theorem SL4' (§4) assumes "SL1'-w, SL3'-w, SL4'-E, SL4'-X of §3", and §3's
SL3'-w displays the hypothesis levels **`gamma* >= 0.25/0.25/0.20/0.15`**
(W1–W4). But the certified ledger (script [1] block [1]) and the sliver
boundary `w†(m)` (block [2]) were computed at the DEFAULT
`gamma* = 0.42/0.42/0.40/0.40` (the table's W1 row prints
`mid=4.47e-03`, which is the 0.42 value), and block [4]'s "W1 accepts
`gamma* = 0.25`" was evaluated at `w = 4.30` ONLY — where the W.6 crossover
entry is ~16x smaller than at the sliver edge. Referee measurement
(`ref_nw4p_e_gamma_sliver.py`):

```
[E1] m=401: w=4.095: row(g=0.25)=1.1998 FAIL  (row(g=0.42)=0.9992 PASS)
           w=4.10 : row(g=0.25)=1.1671 FAIL  (row(g=0.42)=0.9665 PASS)
           w=4.12 : row(g=0.25)=1.0533 FAIL  ... first PASS at w=4.14
[E2] w_dagger(401) = 4.135 / 4.105 / 4.100 / 4.095  at gamma* = 0.25 / 0.30 / 0.35 / 0.42
[E3] full-band closure at w->4+ under gamma*=0.25: first m = 470  (vs 463 at 0.42)
```

So **under the stated hypothesis set, the residual trapezoid is
`(4, 4.135] x [401, 469]`**, not the quoted `(4, 4.10] x [401, 461]`; the
draft's §0/§6.3/§8 headline "SL3' is now ... `gamma* >= 0.25` suffices" and
the §5 sliver table are jointly inconsistent. W2–W4 are NOT affected: their
rows are `w`-independent and genuinely pass at the weakened
0.25/0.20/0.15 for all probed `m` ([E5]: W2 `0.8983`, W3 `0.7326`,
W4 `0.7908` at `m = 401`, decreasing in `m`) — the mismatch is confined to
W1. Two one-line repairs, either of which restores full consistency
(both re-certified by my scripts):

- *(Route a)* State SL3'-w as `gamma* >= 0.42/0.25/0.20/0.15` (W1 kept at
  the §5.3/table level; still strictly weaker than composite §5.3, which
  asked 0.42/0.42/0.40/0.40 on W1–W4 PLUS 0.38/0.34/0.32 on W5–W7) — then
  every quoted number stands except F2's off-by-one. The "0.25 suffices"
  remark survives only band-scoped to W2 and `w >= 4.14` on W1.
- *(Route b)* Keep `gamma*(W1) = 0.25` and restate the trapezoid as
  `(4, 4.135] x [401, 469]`, `w†(401; 0.25) = 4.135` — the SL-sliver
  handoff then needs `m` to 469.

### F2 (SUBSTANTIVE — trapezoid `m`-range off-by-one, even at `gamma* = 0.42`)

The draft's §0/§5/§8 claim the trapezoid is `m in [401, 461]`, because
block [2] found "first m with W1 PASS = 462" **at `w = 4.001`** — but the
sliver is `w in (4, w†(m))`, and the prover never probed `w in (4, 4.001)`.
Referee probe (`ref_nw4p_b_sliver.py` [B3], `ref_nw4p_b2_boundary.py`):

```
row(462, w=4.0000001) = 1.0019 FAIL ;  w_dagger(462) = 4.00021
row(m, w->4+): 461: 1.012820 FAIL | 462: 1.001895 FAIL | 463: 0.991128 PASS
first m with row(m, 4.0) <= 1  =  463   ->  trapezoid m-range = [401, 462]
```

So at `m = 462` the sliver `(4, 4.00021]` is NONEMPTY: **the corrected
trapezoid is `m in [401, 462]`** (at the table's `gamma* = 0.42`; `[401,
469]` under route (b) of F1). Load-bearing for the handoff: an SL-sliver
harness extension to 461 would NOT close CL — it must cover 462 (resp.
469). (The §4 theorem's own phrasing "`w†(m) = 4.001`-level from `m = 462`"
is literally satisfiable — `4.00021 <= 4.001` — but §0's "(4, 4.10],
m in [401, 461]", §5's "[401, 461]" and §8's recap are wrong as displayed.)

### F3 (claim-scoping — SL4'-E "never above 0.65 of its budget" fails off the 17-point sample)

The 17 measured points reproduce exactly (independent re-implementation,
dps 35: `w = 4.9`: ratio `0.6432`; `w = 356.8`: `0.1804` — byte-consistent
with `out_sl4p_nc2.txt`). But the prover's set contains no band RIGHT edge,
where `|eta|/u` is largest against a fixed banded price. Referee probe
(`ref_nw4p_c_eta_edges.py` [C2]/[C3]), `m = 401` unless noted:

```
w=5.0 (W1 edge): |eta|/u=0.4606  ratio=0.6579  ** > 0.65 **   (m=402: 0.6579; m=1000: 0.6573)
w=6/8/10/20/40/356.89:  ratios 0.4863/0.3365/0.2764/0.2215/0.2120/0.1803  (all <= 0.65)
w=4.001: 0.4983
```

The SL4'-E HYPOTHESIS itself is untouched (worst measured ratio anywhere =
`0.6579 <= 1`, 34% headroom; `kappa_4 > 0` at every probed point,
including all edges) — but §0/§3's "never above 0.65 of its budget" must be
scoped to the 17 points or corrected to "never above 0.66; worst at the
W1 right edge `w = 5`". The true W1 in-band worst is at `w = 5.0`
(edge), not the `w ~ 4.9` sample.

### F4 (claim-scoping — block [4]'s acceptance-slack table is conditioned on W1 at `w = 4.30`)

§3 SL1'-w's remark "the ledger would in fact accept `C5*` up to
`0.4/0.2/0.4/0.4/...` — the SL1' prover has 2x–8x slack on every band
except W5/W7": (i) the W1 entry `0.4` holds ONLY away from the sliver edge
([E4]: `row(w=4.10, C5*=0.4) = 1.4695` **FAIL**; `row(w=4.30, C5*=0.4) =
0.9608` PASS) — same conditioning defect as F1, this time in a remark, not
a hypothesis; (ii) W6b's slack is `0.4/0.25 = 1.6x`, outside the quoted
"2x–8x". Repair: scope the remark ("at `w = 4.30`; the W1 slack does not
hold uniformly down to the sliver edge") and fix the W6b range.

### F5 (minor — wrong constant in the `efac` "iff" boundary; safe direction)

Lemma SL4'.3 and script comment claim `efac(C5*) <= e  iff  C5* <= 0.8464`.
The true boundary is `4(1 - e^{-1/4}) = 0.88479687` ([A4]:
`efac(0.8464) = 2.5883 < e`; `efac(0.8848) = 2.71829 ~ e`). The stated
cutoff is SAFE (0.8464 < 0.8848) and only ever binds against the unused
CGRID values 3/1.5, but the "iff" is false as printed. Repair: print
`0.8848` (or drop the "iff").

### F6 (minor — Lemma SL4'.8's proof parenthetical)

(i) "mid/X-tier-2/R5/cube/cross decreasing in `A` on `A >= 32`" is FALSE
for the tier-1 mid entry on `[32, 45.6)` (true threshold `6/g = 45.558` at
`g = 0.1317`; [A5]) — harmless in application since the minimum `A0` used
is `0.28*401 = 112.28`, but the display should say "on the used range
`A >= 112`" (or per-entry thresholds). (ii) The lemma's stated rule "an
increasing entry's worst budget ratio is at `A = m`" needs `e_i(A)/A`
nondecreasing, not mere monotonicity; it holds for the actual increasing
entries (far is exactly linear in `A`; W1's X is `~A^{5/2}`) — the proof
line "prefactor `A` resp. `A^{5/2}`" already contains the right reason, but
the lemma statement should say so.

### F7 (minor — unreproduced diagnostic number in §5)

"the binding entry throughout is W1's W.6-crossover `X` (share 0.68 at
`w = 4.05, m = 401`), not the far slot (share 0.11)": my decomposition
([D1]) gives X-share `0.9954` of the unit budget (`0.716` of the failing
total `1.3911`), far-share `0.1214`, dec-share `0.2743`. The QUALITATIVE
diagnosis (crossover-limited, far comfortable) is CONFIRMED, and
`m x(4.05, 0.8) = 7.6453` (draft "7.65" — nearest-rounds fine), but I could
not reproduce "0.68" under any natural convention (with/without INFL,
QUADF, Xd, or as a fraction of the total). Repair: reprint the number with
its convention, or drop it.

### F8 (record-only observations; no text forced)

- `w†(401)` at 3 dp is `4.095` ([B2], step 0.001; one-crossing in `w`, no
  re-failure above) — the draft's `4.10` from its 0.01 grid is
  safe-direction (claims PASS on a subset).
- The far-entry `m`-decrease threshold is `5.5/0.0741 = 74.22`; draft's
  "for m >= 75" safe.
- `FAREXP = 0.0741 <= q(2,1) = 0.0741265` safe direction; `c_A†(W7) = 0.85
  <= 0.852716` (SL2's certified floor, verified present in the composite).
- `20 * 0.9891 = 19.782` (draft "19.78 <= 20" floor-printed, fine);
  `1/0.28 = 3.5714` ("up to 3.57x", fine).
- Draft §3's W5 `C5*` acceptance "0.10–0.15": block [4]'s grid value is
  `0.10`; the `0.15` end is justified only by the default W5 row passing at
  `C5* = 0.15`. Accurate as a range, worth a clause.

## 3. What survived adversarial attack (for balance — all clean)

1. **Full-integer-grid `m`-monotonicity** of all seven shares,
   `m = 401..600` step 1 plus `650..2000` step 50 ([B4]): **0 violations**
   (draft's block [3] used 5 points; the claim is real).
2. **`w`-monotonicity / one-crossing** of the W1 row: full `w`-scans at
   step 0.01 for EVERY integer `m in [401, 480]` scanning all the way to
   `w = 5.00` ([B1]): **0 re-failures above `w†(m)`**, and `w†(m)`
   nonincreasing across the full integer grid (the draft sampled 10 `m`
   values; the shape is real, modulo F2's endpoint).
3. **SL4'-X (W.6 exponent monotone in `tau`)**: 6000-point fine-grid audits
   at 8 adversarial `(w, m)` — `(4.001, 401)`, `(4.05, 401)`, `(4.10,
   401)`, `(4.30, 401)`, `(4.90, 401)`, `(5.0, 401)`, `(4.001, 462)`,
   `(4.05, 461)` ([A2]): **0 violations**, minimum increment strictly
   positive (`>= 1.7e-3`) — materially strengthens the grid evidence; and
   coarse(60) >= fine(6000) throughout, confirming the left-endpoint sum is
   behaving as an upper bound on these instances.
4. **SL4'-E at the missed corners**: all band right edges, `w -> 4+`, exact
   `lam = 0.89` corner (`w = 356.89`), `m = 402` and `m = 1000`: pricing
   holds everywhere with `>= 34%` headroom, `kappa_4 > 0` everywhere
   (modulo F3's 0.65 -> 0.66 rewording).
5. **Thin margins are precision-robust**: W5 `0.9890876` and W7 `0.9808361`
   at dps 100 ([D2]); block [5]'s `0.0883744 <= 0.09` and
   `1.0969416 <= 1.10` with exact Hermite-average closed forms ([A3]).
6. **W2–W4 at the weakened gammas** (the part of SL3'-w that is genuinely
   `w`-independent): certified at 0.25/0.20/0.15 for `m = 401/500/1000`
   ([E5]) — the tier-routing claim (SL3' needed on W1–W4 only) is sound.
7. The consumed-inventory numbers check against their sources: `R31*/R42*`
   scales and `c_A` floors match the composite; the F2-corrected deep-corner
   truths (`2.1215/6.3552` vs consumed `2.2/6.6`) match
   `referee_numerics_wp4.md`; the `ptwise` column at `w = 356.8`
   (`4.9235`) is arithmetically consistent with those truths.

## 4. Required repairs (to reach MINOR_REPAIRS-class)

1. **(F1)** Pick route (a) or (b) and make §3 SL3'-w, §4's theorem
   statement + table annotation, and §0/§5/§6/§8 consistent. Route (a)
   (state `gamma*(W1) = 0.42`, keep the quoted sliver) changes the least;
   the "0.25-class" headline then applies to W2–W4 only.
2. **(F2)** `[401, 461] -> [401, 462]` in §0, §5, §8 (or `[401, 469]`
   under route (b)); tell the SL-sliver piece explicitly that `m = 462`
   carries the micro-window `(4, 4.00021]`.
3. **(F3)** Scope or correct the "never above 0.65" sentence (true off-grid
   worst `0.6579` at the W1 right edge, still `<= 1` with 34% headroom).
4. **(F4)** Scope the `C5*`-slack remark to `w = 4.30`-class on W1; fix
   "2x–8x" (W6b is 1.6x).
5. **(F5–F7)** Text-level: `0.8464 -> 0.8848` (or drop "iff"); fix the
   "A >= 32" parenthetical; reprint or drop the "share 0.68" diagnostic.

None of these threaten the assembly mechanism, the slot constants, the
INFL/QUADF budget, or the W2–W7 rows; F1/F2 do move theorem-statement
constants, which is what forces the MAJOR_ISSUES grade under house rules.

## 5. Referee script table (all SAVED and RUN 2026-08-12; outputs archived)

| # | script (`g2_scripts/campaign_20260811/referee_wave4_sl4p/`) | what it does | key output |
|---|---|---|---|
| R-A | `ref_nw4p_a_rebuild.py` (`out_ref_nw4p_a.txt`) | independent dps-60 rebuild of all 7 rows from the draft's closed forms; 6000-pt W.6 audits; exact `E|He|` closed forms; efac boundary; A-monotonicity thresholds; constant roundings | all 7 rows agree `< 5e-5`; 0 W.6 violations; `E|He3| = 1.510013`, `E|He4| = 2.800600`; boundary `= 0.88479687` |
| R-B | `ref_nw4p_b_sliver.py` (`out_ref_nw4p_b.txt`) | `w†(m)` on the FULL integer grid 401–480 with re-failure scan to `w = 5`; fine `w`-scan at 401; `w -> 4+` probe 462–500; full-grid m-monotonicity | 0 re-failures; `w†` nonincreasing; `w†(401) = 4.095`; **`row(462, 4+) = 1.0019` FAIL**; 0 m-monotonicity violations |
| R-B2 | `ref_nw4p_b2_boundary.py` (`out_ref_nw4p_b2.txt`) | pins F2 | `w†(462) = 4.00021`; first full-closure `m = 463` |
| R-C | `ref_nw4p_c_eta_edges.py` (`out_ref_nw4p_c.txt`) | independent eta re-implementation; band right edges, `lam = 0.89` corner, `m = 402/1000` | prover's points reproduced (0.6432/0.1804); **`w = 5.0`: ratio `0.6579 > 0.65`**; all `<= 1`; `k4 > 0` everywhere |
| R-D | `ref_nw4p_d_margins.py` (`out_ref_nw4p_d.txt`) | dps-100 thin-margin rows; §5 share decomposition; misc arithmetic | W5 `0.989087631`, W7 `0.980836120`; X-share `0.9954` / far `0.1214` at (4.05, 401) |
| R-E | `ref_nw4p_e_gamma_sliver.py` (`out_ref_nw4p_e.txt`) | F1 quantification: sliver vs assumed `gamma*`; C5-slack edge probe; W2–W4 weakened-gamma certification | `w†(401; 0.25) = 4.135`; closure `m = 470`; `row(4.10, C5=0.4) = 1.4695` FAIL; W2–W4 weakened PASS |

*End of referee_numerics_wave4_sl4p.md.*
