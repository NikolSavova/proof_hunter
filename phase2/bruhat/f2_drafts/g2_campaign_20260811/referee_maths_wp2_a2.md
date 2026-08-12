# Adversarial maths referee report — wp2_draft_a2 (Delta_ker bucket + merged T.9-final)

*Referee pass 2026-08-11 (wave 2). Target: `g2_campaign_20260811/wp2_draft_a2.md`
+ its seven scripts under `g2_scripts/campaign_20260811/wp2_a2/` (including the
three inherited first-pass files the draft discloses). Read in the required
order: STATUS.md, `F2_PROOF_DRAFT.md`, `g1_draft_b.md`, `g2_draft_t2_20260803.md`,
`wp1_draft_c.md` + `wp2_draft_b.md` and all four wave-1 referee reports; the
draft's three wave-2 support citations (`referee_t2_maths.md`,
`repairs_20260811.md`, `harness_m200_20260811.md`) were each opened and their
claimed contents verified against what the draft says of them. Blind protocol:
`g2_draft_t1_20260803.md` untouched; no other wave-2 draft read. No existing
file modified. Default-to-refutation stance: every lemma re-derived by hand,
every script re-run, the headline constants re-assembled from the DRAFT'S
DISPLAYED FORMULAS in a from-scratch referee implementation (no import of the
draft's libraries), and the one genuinely new analytic ingredient (the Lemma
D.1' real/imaginary split) stress-tested at 200,000 random points off any grid
the draft uses.*

*Referee script (saved and run 2026-08-11, CPython 3, mpmath/sympy/stdlib):
session scratchpad `ref_wp2a2_indep.py` (six parts, output quoted in §2.3).
Every number quoted below is from a real run.*

## VERDICT: MINOR_REPAIRS

**Every load-bearing mathematical claim survives.** Theorem D.5's chain
(Lemmas D.1, D.1', D.2, D.3, D.4) is correct as displayed; my independent
re-assembly of `C_ker(K, m)` from the draft's formulas alone reproduces
30.8863 / 209.0224 / 37810.0442 (and the 400/2000 spot values) to relative
deviation < 3e-6. The real/imaginary split — the draft's only new analytic
content, and the step that rescues the odd-cube order — is sound: I re-derived
the integral-remainder split by hand and confirmed the resulting inequalities
are TRUE and nearly sharp (max ratio 0.9996 over 200k random `z`, i.e. no
slack was available to hide an error). The kernel identity for non-even
complex `psi` at `x = 0` (Lemma D.2(ii)) is correct and was verified against
an adversarially non-even test function. No circularity exists: Prop 3.5 is
nowhere assumed, no T2 §8 OPEN item is consumed, and every input is quoted
with its true hypotheses and correct two-referee/grid status — including the
three wave-2 support files, whose contents I verified on disk (the T2 maths
referee report really exists, really says MINOR_REPAIRS, and really confirms
T.9''(b) and (T.8a), the two T2 items this draft leans on; the harness really
is exact to m = 400 with a saved results file). All seven scripts run and
reproduce the draft's quoted outputs exactly, including NC-A2's deliberate
FAIL. The repairs needed are text-level: one certification-scope
misdescription in §0, one incomplete classification inside the exponent
audit, one certification-status sentence for `LFlow > 0`, one sign typo, and
bookkeeping trivia. None touches a constant, lemma, threshold, or the
verdict-relevant structure. List in §3; required repairs in §4.

---

## 1. What was verified and how (hand re-derivations)

### 1.1 Lemma D.1 (Gaussian domination + crude majorant) — CORRECT.

Rederived from T.9''(b): `log phi = -s2 t^2/2 - U_0 + R_7` with
`U_0 = i alpha t^3 + beta t^4 - i delta t^5 + gamma t^6` — checked the sign
dictionary against `sum_{r=3}^6 kappa_r (it)^r/r!` term by term (`(it)^3 =
-it^3` etc.); `phi = e^{-s2 t^2/2} e^{-z}`, `z = U_0 - R_7` is exact on
`|t| <= t_1`. The `eps` mechanism: each of `A4 t^4, A6 t^6, A7 t^7` is `t^2`
times a nondecreasing function, so `Re z >= -eps (s2min/2) t^2` on the box —
correct, and correct REGARDLESS of the signs of `beta, gamma` (it uses moduli,
so wp2-b's `kappa_4` sign-flip at `w ~ 3.3` is harmless here; checked). The
D.1(ii) decomposition `e^{-z} - Q = [cube remainder] + [R_7 - U_0 R_7 +
R_7^2/2] + D_2` was expanded by hand (the middle bracket from `z = U_0 - R_7`
substitution: exact). Hand-checked `eps(1, 180)`: my slide-rule value 0.1737
vs the quoted 0.1735 (my S_4/S_6 roundings) — confirmed exactly by the
independent script.

### 1.2 Lemma D.1' (the real/imaginary split) — CORRECT, and essentially sharp.

This is the draft's new mathematics and got the heaviest attack:

1. *Taylor remainder in integral form.* `e^{-z} - (1 - z + z^2/2) =
   -(z^3/2) int_0^1 (1-tau)^2 e^{-tau z} dtau` — standard, re-derived.
2. *The split.* `z^3 = (zR^3 - 3 zR zI^2) + i(3 zR^2 zI - zI^3)`,
   `e^{-tau z} = e^{-tau zR}(cos(tau zI) - i sin(tau zI))`: the displayed
   `Re[.]` is exactly right. Bounding `|cos| <= 1` on the even-family term
   (`int (1-tau)^2 = 1/3`) and `|sin(tau zI)| <= tau|zI|` on the odd-family
   term (`int (1-tau)^2 tau = 1/12`) gives
   `|Re rem3| <= EE[(ZR^3 + 3 ZR ZI^2)/6 + (3 ZR^2 ZI^2 + ZI^4)/24]` — the
   odd cube `zI^3` picks up the extra `|zI|` and becomes `ZI^4`. Re-derived;
   the `/6` and `/24` denominators and the `sup_tau e^{-tau zR} <= EE`
   absorption all check. **Stress test** (referee script part 2): 200,000
   random `z` with `zR, zI in [-2, 2]`: max `|Re rem3|/bound = 0.999601`,
   max `|Im rem3|/bound = 0.997895` — the inequalities hold with essentially
   ZERO slack, i.e. they are the true envelope of the mechanism, and any
   algebra error would have produced a violation.
3. *Q's parts.* Sympy re-derivation (script part 3): `Re Q - 1 = -beta t^4
   - (gamma + alpha^2/2) t^6 + (beta^2/2 + alpha delta) t^8` (majorant VE ✓),
   `Im Q = -alpha t^3 + delta t^5 + alpha beta t^7` (VO ✓), `Re D_2 =
   (beta gamma - delta^2/2) t^10 + (gamma^2/2) t^12` (ReD2b ✓), `Im D_2 =
   (alpha gamma - beta delta) t^9 - delta gamma t^11` (ImD2b ✓). All four
   identities confirmed symbolically; the draft's sign-flipped display of
   `D_2` is immaterial exactly as it claims (only moduli are consumed).
4. *The parity claim.* "Every monomial of WR and VE has even total degree in
   (A3, A5) or carries A7" — verified monomial-by-monomial (ZR is
   A3/A5-free; ZI^2, ZI^4 contribute even degrees except A7-crosses, which
   carry A7). The bare `A3^3` indeed lives only in WI, and in the assembly WI
   only ever multiplies ZI, VO (kernel bucket) or `|t|` (pointwise bucket) —
   confirmed against both the displayed formulas and the code.

### 1.3 Lemma D.2 (kernel identities) — CORRECT.

(i) is (T.8a), cited within its scope (tilted mean, `x = 0`), now two-referee
(referee_t2_maths §2.10 — verified on disk). (ii): re-derived the three-line
symmetrization; the point that NO evenness of `psi` is needed at `x = 0` is
right (the `sin(s-t)` part is antisymmetric under the swap regardless of
`psi`'s symmetry). **Adversarial check** (script part 5): took a deliberately
non-even, non-Hermitian-symmetric `psi(t) = e^{-t^2}(1 + 0.3 i t^3 + 0.2 t)`
— the identity `q(0)^2 - q(1)q(-1) = (1/4pi^2) intint psi psi (1-cos(s-t))`
holds to 2.1e-16 relative. The "consequently" chain (`u = (v + w~)/(1+delta)`,
`zeta = (w~ - delta v)/((1+delta)(1+v))`) was verified symbolically (script
part 6: sympy `simplify == 0`).

### 1.4 Lemma D.3 (the three DeltaD pieces) — CORRECT.

*Reality bookkeeping (the subtle point):* `D` and `Dhat` are both real, so
`DeltaD = Re[box piece] + Re[out] - Re[tail]`, and taking `|Re[.]|` of the
box integrand while bounding out/tail in modulus is legitimate — checked.
*Box:* the telescoping `A(s)A(t) - Ahat(s)Ahat(t)` real part reproduces the
draft's four-term bracket exactly (re-derived); each term carries at most ONE
EE-factor per variable, and `e^{-s2 t^2/2} EE(t) <= e^{-a t^2}` per variable
(`a = (1-eps) s2min/2`) — the "EE absorbed into a" bookkeeping the draft's
§10 invites attention to is sound (I looked specifically for a term with two
EE-factors on one variable: none exists). Kernel `1 - cos(s-t) <=
(s^2+t^2)/2 - st` with the `st`-cross vanishing by oddness against
even-in-each-variable majorants: correct; extension of the (nonnegative)
majorant integral from B to R^2: safe direction. `pair(p, q)` is the exact
Gaussian moment value (checked against `J(n, a) = Gamma((n+1)/2)/a^{(n+1)/2}`,
itself verified). *Out:* W.4(i) is applied strictly inside its hypotheses
(`|lam| <= K/m`, `K <= m/4`, `m >= 30`, `t in [t_1, pi]` — all hold on the
theorem's range; the historical silent-hypothesis failure mode was hunted and
is absent); the two-strip cover double-counts corners in the safe direction.
*Tail:* `|Q(t)| <= 1 + VQ(t)` is a coefficient-wise triangle inequality,
valid for ALL t (not just the box) — checked, so the model tail majorant is
global as required; the `tail(n, t0, c)` bounds (exact for odd n, `t^n <=
t^{n+1}/t_0` for even) were verified against mpmath quadrature (script part
4: ratios 1.0000–1.043, always >= truth).

### 1.5 Lemma D.4 (pointwise, denominators, v > 0) — CORRECT.

(i): `P_j - phat(j)` is real; the box part's `Re[(DC + iDS)(cos(tj) -
i sin(tj))] = DC cos(tj) + DS sin(tj)` with `|sin(tj)| <= |t|` at `j = +-1`
— this is where the bare `A3^3` (sitting in WI = the DS-majorant) picks up
its extra power; re-derived, correct. (ii): `phat(+-1) >= (2 pi lambda)^{-1/2}
e^{-1/(2 s2min)} Pmin` via `s2 <= lambda` (merged L.3.2, PROVED) and
`h^2 <= 1/s2min`; `|delta| <= 2 dbar + dbar^2` from the product of two
relative errors — correct. (One sign typo in the display, F4 below.)
(iii): the `v > 0` certificate `LFlow = 1 - core > 0 => log F(0) > 0` and
`s2 v <= (1+core) e^{(1+core)/s2min}` — both re-derived (`e^x - 1 <= x e^x`;
`s2 log F <= 1 + core` from W.4's two-sided form with box values, which
upper-bound the true scaled coefficients). This closes wp2-b's F6 `v > 0`
item as claimed. Certification-scope caveat: F3 below.

### 1.6 Theorem D.5 and Theorem T.9-final — CORRECT as scoped.

The assembly `|Delta_ker| <= s2|zeta|/(1-|zeta|)` with `zeta`'s numerator
split into `s2wf` (via `s2 <= lambda`, the phat-floor, and DeltaD) and the
`delta v` piece (via D.4(ii)+(iii)): every inequality re-derived; `zbar` is a
valid `|zeta|`-majorant (each factor bounded with `s2 >= s2min`); the
`1/(1-zbar)` correction is justified by NC-A6's `zbar <= 3.4e-7` (re-run,
reproduces). The merge (§7): W.7 (exact decomposition) + repaired W.6
envelope + D.5 + triangle — checked; the Lin discharge `H(K, M(K)) =
0.0097/0.0241/0.3321 <= 1/2` recomputed by hand (e.g. K=4:
`(1.080/367)(17) + 37997.5/367^2 = 0.0500 + 0.2821 = 0.3321` ✓), and H's
pieces are manifestly decreasing (B.0(ii) + fixed constants over m^2). The
`K = 3 subset K = 4` device is valid. The referee-F5 resolution claim is
right: D.5's bound is w-uniform on `|w| <= K`, so the merged envelope is
W.6's unchanged — no hidden `w^2/m` term can re-enter through Delta_ker.
Coverage: `M(K) <= 400` against the harness's certified `4 <= m <= 400`
(results file on disk, `# rows: 397, failures: 0`) — the overlap argument is
correct, with the honest §10-item-4 caveat that below `M(K)` it is the
harness's GROUND TRUTH, not the analytic law, that covers (correctly flagged).

### 1.7 Input-status audit (the assignment's specific hunting list)

- **Prop 3.5 is nowhere assumed** (the conclusion is built from the kernel
  identity + model + buckets; the only ambient citation is Bona `r >= 1`
  inside wp2-b's W.5, as in wave 1).
- **No T2 §8 OPEN item is consumed**: T.7b/T.7c/T.8/(V)/deep-tilt/region-2
  appear nowhere in the chain; the far bucket runs entirely on wp1-c W.4(i).
- **T2 single-referee flag**: moot in the stated direction — the draft's
  claim that `referee_t2_maths.md` now exists with MINOR_REPAIRS and confirms
  T.9'' ("chain gives 2.8549e6", §2.12) and (T.8a) (§2.10) is TRUE (verified
  on disk, including the quoted §2.12 constant). The two items that referee
  found broken (T.10(2), T.8'') are not inputs here — the draft says so
  (§10 item 5) and I confirmed neither is consumed.
- **Wave-1 inputs quoted with their repairs**: c_w(4) = 1 (repair B2), PW
  grid K=4 scoped m <= 2000 (repair B3), c_4 exhaustive-[30,400] grid (B4),
  W.1(i)/NC-W2(f) tails closed (B5) — all match `repairs_20260811.md` as
  read; wp1-c's c_1(K) margins ">= 9.1e-6" match STATUS §2a R1.
- **Grid-certified inputs are all flagged** in the input table and §10 item
  2, and propagate into T.9-final's stated status. Correct labeling
  discipline throughout (one §0 slip: F1).

---

## 2. Verification record

### 2.1 Script re-runs (all seven; every quoted number reproduces)

| script | re-run result | draft quote check |
|---|---|---|
| `wp2a2_nc1_model_err.py` (inherited) | PASS | (A.1a) 0.999312, (A.1b) 0.191026, cumulant dev 1.33e-12, kernel identity 3.21e-38/6.19e-38, `q(0)` vs `Z P` 1.25e-41/5.01e-41 — all identical |
| `wp2a2_nc2_buckets.py` (inherited) | FAIL (by design) | crude table row (180,1): eps 0.1735, box 47.4418, Cker 53.4047; (180,4): 449739.9956, far 3.62e+05; non-monotone at m = 787/256/368 — all identical to §6/§8 |
| `wp2a2_nc3_refined.py` | PASS | split ratios WR 0.085347 / WI 0.191037 / ZI 0.943412; per-piece rows (180,1) 30.8863, (180,2) 209.5757, (379,4) 37514.9161, (400,1) 21.0810, (2000,1) 14.0048; mker 136/181/367; monotone True x3; headline 30.8863/209.0224/37810.0442 with ratios 22.2x/51.4x/7502.0x — all identical |
| `wp2a2_nc4_truth.py` | PASS | ports match; full-scan truths 1.386/4.070/5.022 (m=60) and 1.354/4.054/5.038 (m=140); min v 1.288e-05; LFlow table — all identical |
| `wp2a2_nc5_merge.py` | PASS | C_R tables 32.4358/213.1123/37814.9708 and 41.1647/230.0864/37997.4722; H 0.0097/0.0241/0.3321; 3000-vs-10^4 rows; coverage — all identical |
| `wp2a2_nc6_zbar.py` | PASS | max zbar 3.394e-07 — identical |

The three support files check out: `referee_t2_maths.md` (verdict
MINOR_REPAIRS; §2.10 (T.8a) CORRECT; §2.12 T.9'' CORRECT with the
`1/2.8549e6 >= 1/2.8e6` chain), `repairs_20260811.md` (B2/B3/B4/B5 exactly
as the draft's input table describes), `harness_m200_20260811.md` +
`g2_scripts/campaign_20260811/harness_m200/results_m200.txt` (exact to
m = 400, zero failures, checkpoint varfits present).

### 2.2 Independent referee implementation (`ref_wp2a2_indep.py`)

Re-implemented the entire Theorem-D.5 assembly from the draft's DISPLAYED
formulas — own exact `S_r` sums, own sympy regeneration of wp2-b's
`N0_resid` monomial table (from the closed-form `P`, a different derivation
path), own polynomial/moment/tail code; zero imports from the draft's libs.
Key output (verbatim):

```
(1) independent C_ker re-assembly (vs draft values):
    K=1 m= 180: C_ker = 30.8863  (draft 30.8863, rel dev 8.9e-07)  eps=0.1735 LFlow=0.99248  match: True
    K=2 m= 181: C_ker = 209.0224  (draft 209.0224, rel dev 4.2e-08)  match: True
    K=4 m= 367: C_ker = 37810.0442  (draft 37810.0442, rel dev 6.2e-10)  match: True
    K=1 m= 400: C_ker = 21.0810  (rel dev 2.1e-06)  match: True
    K=1 m=2000: C_ker = 14.0048  (rel dev 2.9e-06)  match: True
(2) random-z stress of the D.1' cube-remainder split bounds:
    max |Re rem3|/bound = 0.999601   max |Im rem3|/bound = 0.997895  (PASS iff <= 1)
(3) sympy: Re Q - 1, Im Q, Re D_2, Im D_2 == the draft's four displays: True x4
(4) tail(n, t0, c) >= mpmath truth at 5 (n, t0, c) points: True x5 (ratios 1.0000-1.043)
(5) D.2(ii) for NON-even psi = e^{-t^2}(1 + 0.3 i t^3 + 0.2 t): rel dev 2.10e-16
(6) sympy: (1+u)/(1+v) - (1 + zeta) == 0 : True
REFEREE INDEP VERDICT: ALL PASS
```

The sub-3e-6 residuals in (1) are float-order differences between my exact
integer `S_r` route and the lib's; every printed digit of every headline
constant agrees.

### 2.3 The exponent audit, re-done from scratch

For a box row with `c` coefficient factors (`deg_m(A_i) = t\_power + 1`) and
total t-degree `T` (kernel `+2` and the `lambda^2 / a^{...}` scalings
included), the net power of `m` in `m^2 C_ker`-units is `net = 2 + c - T/2`
— I confirmed the draft's counting rule and then classified EVERY row of
`WR, WI, VE, VO, ZI` as combined by `pair(...)` and by `E_pt`:

- `c >= 4`: `net <= 2 - c/2 <= 0` always (since `T >= 3c`).
- `c = 3`: only `T = 9` (the bare `A3^3`) could go positive (`+1/2`), and it
  occurs ONLY inside WI, which in the kernel bucket always meets an
  odd-family partner (`ZI` or `VO`: `c -> 4`, `net <= 0`) and in the
  pointwise bucket always meets the `|t|`-shift (`net = 2 + 3 - 10/2 = 0`).
  All other `c = 3` rows have `T >= 10`, `net <= 0`.
- `c <= 2`: every such row either carries `A7` (`net <= -1/2`) or has
  `T >= 10` (`ReD2b`, `ImD2b + partner`: `net <= -1`).

So **no positive-exponent row exists** — the refined route's order really is
restored, exactly as the draft's mechanism claims, and the crude route's
`A3^3`-against-constant row (`net = +1/2`, i.e. `K^3 sqrt(m)`) is exactly
the NC-A2 failure. However the draft's PARENTHETICAL classification of the
exponent-0 set is incomplete — finding F2.

---

## 3. Findings (ranked; none load-bearing)

**F1 (certification-scope misdescription in the headline).** §0 item 1 says
`C_ker(K, m)` is "certified DECREASING in `m` on the stated range (unit-step
to 3000, spot-checked to 10^4)". The actual scan (NC-A3(3), re-run) is
unit-step on `[M(K), 1000]`, step 10 on `[1010, 3000]`, and endpoints-only on
`(3000, 10^4]` — which §6's scope note and §10 item 2 state correctly. The
§0 headline overstates the grid by a factor of 10 on `[1000, 3000]`. Repair:
align §0's parenthetical with §6/§10 (or actually run unit-step to 3000 —
minutes).

**F2 (exponent-audit classification incomplete — matters for the promised
Sturm route).** The D.5 scope note asserts "every row has a NEGATIVE net
exponent except the pure-alpha quartic rows (`ZI^4`-class), whose exponent is
0". By the draft's own counting rule (`2 + n_c + n_q - (p+q)/2`), the
exponent-0 set is larger: the `ZR·ZI^2` rows of WR against the constant slot
(e.g. `A4 A3^2`, `c = 3`, `T = 10`: net 0 — an alpha^2-class row, not
quartic) and WI's bare `A3^3` through the `|t|`-shift in the pointwise bucket
(`2 + 3 - (9+1)/2 = 0`) also sit at exponent 0. My §2.3 re-audit confirms the
CONCLUSION (no positive row anywhere; every row decreasing-to-limit), so
nothing numeric changes; but the parenthetical must be corrected, because it
is offered as the target list for the flagged Sturm upgrade of the
`m > 3000` tail — a Sturm pass built on the stated (incomplete) row set would
miss limit-positive rows. Repair: one sentence.

**F3 (certification status of `LFlow > 0`).** Theorem D.5 consumes
`v > 0` (D.4(iii)) for EVERY `m >= M(K)`, but `LFlow > 0` is explicitly
verified only at `m in {180, 181, 367, 400, 1000}` (NC-A4(3)). Implicitly it
also holds at every grid point of NC-A3(3)'s monotonicity scan (the lib
returns None when `LFlow <= 0`, so a violation would have crashed the scan) —
i.e. its true status is the SAME grid-certificate class as the
monotone-decrease claim, with enormous margin (worst `LFlow = 0.92237`, every
`core`-piece decreasing at wp2-b's certified grid resolution). The draft
should say so explicitly rather than let D.4(iii)'s "If LFlow > 0" read as
discharged outright; fold it into the §6 scope note / §10 item 2 sentence.
Repair: one sentence, no mathematics.

**F4 (sign typo).** §5 D.4(ii): "`phat(+-1) = Z(-+h) P(-+h)`" — with
`y = x h` the correct display is `phat(+-1) = Z(+-h) P(+-h)`. Harmless
(`Z` is even and both `P(+-h) >= Pmin`), but fix.

**F5 (bookkeeping trivia).**
- NC-A6 (`wp2a2_nc6_zbar.py`) is quoted in §8 and load-bearing for the
  `zbar < 1e-6` step of D.5's proof, but is missing from both the header
  script list and the §8 script table. Add it.
- NC-A4(2)'s (m, K) = (60, 4) row: the refined bound does not assemble there
  (lib returns None; the printed bound is `inf`), so "measured <= bound" is
  vacuous at that point. Consistent with the theorem's scope (M(4) = 367),
  but the draft's trimmed §8 quote hides the inf — add a clarifying clause.
- §2's NC-A3(1) line says the split bounds were checked "on the same grids"
  as NC-A1; NC-A3 actually uses `w in {K/2, K}` (NC-A1 uses {K/4, K/2, K}).
- §6's per-piece table mixes m = 180/181 and m = 367/379 values inside
  single rows with parenthetical annotations — confusing; print two rows.
- §0 item 4 / §7's "no uncovered m" phrasing: correct as consumed, but the
  merge editor should be pointed at §10 item 4's caveat (below M(K) the
  coverage is the harness's exact GROUND TRUTH, not the analytic law) at
  first use, not only in §10.

**Positive findings (attacks that failed).**
(i) Circularity: none — Prop 3.5 not assumed; T2 §8 OPEN items not consumed;
the two T2 items the T2-maths referee broke (T.10(2), T.8'') are genuinely
not inputs. (ii) Silent hypothesis: none — every use of W.3/W.1/W.4(i)/
T.9''(b)/W.4/W.6/W.7 sits inside its stated scope, checked one by one (the
historical `w <= pi` trap is structurally absent: all boxes used are
`|w| <= 4`-valid). (iii) The odd-cube finding is real, correctly diagnosed,
and correctly repaired — the crude route's failure is reproducible (NC-A2
re-run FAILs at the same m-values) and the refined route's split bounds are
true with near-zero slack (200k-point stress). (iv) The three wave-2 support
citations are accurate on disk. (v) The headline constants are
independently reproducible from the displayed mathematics alone — the draft
text, not just its code, contains the proof. (vi) The K = 4 constant's
crudeness (7502x truth) is honestly disclosed with a correct mechanism
diagnosis and does not affect any downstream consumer (K = 1 is what Theorem
A / G4 use, at 22x truth with orders of headroom against the m^2-scaled
margins).

---

## 4. Required repairs (all text-level; no constant, lemma, or threshold moves)

1. Fix §0 item 1's monotonicity-grid description (or run the unit-step scan
   to 3000 and keep the claim). [F1]
2. Correct the D.5 scope-note parenthetical: exponent-0 rows = the
   `ZI^4`-class AND the `ZR·ZI^2`-against-constant class AND WI's `A3^3`
   via the pointwise shift; cite this report's §2.3 re-audit if convenient.
   [F2]
3. Add the one-sentence certification-status note for `LFlow > 0` (same grid
   class as the monotone-decrease certificate; margin 0.92 at worst). [F3]
4. Fix the `Z(-+h) P(-+h)` sign typo in D.4(ii). [F4]
5. F5 trivia: NC-A6 into the script lists; the (60, 4) `inf` clause; the
   NC-A3(1) grid wording; split the §6 mixed rows; move the ground-truth-
   vs-analytic-law caveat pointer up to §0 item 4.

None of these threatens the deliverable. The Delta_ker bucket is bounded in
closed form with the stated constants; the odd-cube trap is correctly
identified and provably avoided; the merge into Theorem T.9-final is exact
bookkeeping over double-refereed inputs with statuses honestly propagated.
With the listed repairs applied, T2 §8 item 4 is closed by wp2-b + this
draft, and Prop 3.5(ii) stands closed modulo the flagged (and inherited)
grid-certificate statuses — exactly as the draft claims.

**Final verdict: MINOR_REPAIRS.**

*End of referee report.*
