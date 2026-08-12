# referee_maths_wp4 — adversarial MATHS referee report on `wp4_draft_composite.md`

*Wave-3 referee (maths half, house rule), F2 campaign, 2026-08-12. Target:
`wp4_draft_composite.md` (the CL(79, 20, 0.89) assembled state). Also read in
full: `wp4_plan_20260811.md`, `wp4_sl_SL2.md`, `wp4_sl_SL3.md`,
`wp4_sl_SL5.md`, every script + archived output under
`g2_scripts/campaign_20260811/wp4_*/` (including the orphaned
`wp4_SL4/sl4_nc1.py` + `out_sl4_nc1.txt`), and the cited interfaces in
`wp1_draft_c.md` (W.3, W.5, W.6), `referee_t2_maths.md` (M2),
`wp3_draft_a2.md` (§5 CL definition, Theorem S R2/R3, §6.1 spec),
`F2_PROOF_DRAFT.md` (Lemma 3.1 frame, mirror), STATUS_wave2.md.
`g2_draft_t1_20260803.md` not read (house rule). Default posture: refutation.
My own checks: every wave-3 script re-run and diffed against its archived
output (all byte-identical), plus an independent adversarial script
(saved and run; §5 below). No existing file modified; this file is new.*

## Verdict: **MINOR_REPAIRS**

**on the composite's claims AS STATED** — which are, explicitly: (a) Theorems
A2 (= SL2), A3 (= SL3), Lemma C.1 PROVED; (b) Theorem CL-composite =
"(H1) & (H4) ==> CL(79, 20, 0.89) with `C*_eff = 16.91 <= 20`" PROVED as a
conditional; (c) status of the CL target itself: **PARTIAL** (two named
hypotheses missing, the architected route to (H4) refuted by the orphaned SL4
evidence, honest bridge restated in §5.3). All of (a)–(c) survive adversarial
checking; the repairs below are wording/display-level. **To be unmistakable:
this verdict does NOT certify CL(79, 20, 0.89). CL remains OPEN, exactly as
the composite itself says.** The composite's PARTIAL self-report is accurate,
its honesty apparatus (§5.2–5.3) checks out against the orphaned artifact
line by line, and nothing in it inflates the delivered state.

## 1. What I verified, layer by layer

### 1.1 Theorem A2 (= SL2) — hand re-derivation: CORRECT, fully

- **Lemma SL2.0** (closed form): re-derived from the cgf identity
  `(log Z_j)'' = Var`; `psi'(x) = 1/(e^x - 1)`, `psi'' = -e^x/(e^x-1)^2`,
  `Var(U_j) = j^2 psi''(j lam) - psi''(lam)` — sign and both branches
  (`lam < 0` via sign cancellation in the quotient) correct; the
  `h`/`v`-form and the `lam -> 0` limit `(j^2-1)/12` correct.
- **Lemma SL2.1** (`h` strictly decreasing on `(0, oo)`, even): the
  `sinh(y)/y` power-series argument is airtight.
- **Corollary SL2.2** (= A2(i), strict, all real `lam`): correct.
- **Lemma SL2.3** (master inequality): (a) exact; (b) the right-endpoint
  Riemann comparison for increasing `v` is exactly right — the
  zero-discreteness claim is genuine (the discrete sum dominates the
  integral with no correction term; the only loss is the subtracted
  `v(lam)`); (c) `V` increasing via `v(w) >= V(w)`: correct.
- **Proposition SL2.4 + Theorem SL2.5**: the certificate construction is
  safe-direction at every step (checked in the script source
  `sl2_e2_band_certificate.py`: `e^{1/8}` bracket with explicit Taylor-tail
  cap; `g(E) = E/(E-1)^2` decreasing; `h(a) <= a^2 g(lo^k)` rounded UP;
  `h(cap) >= cap^2 g(hi)` rounded DOWN; exact `Fraction` comparisons).
  Independent re-derivation (my script, §5): the step-1/8 left Riemann sums
  match the LBV column to 1e-6 from above, `LBV <= Riemann <= V(w0)` at all
  seven `w0`; `v(cap) <= UBv` at all seven caps. The `m`-uniformity
  argument (only `m`-dependence is `w1/m <= w1/401`, safe direction) is
  correct; SL2's own observation 1 (truth decreases in `m`, so a pointwise
  401-measurement could not have certified this) is a correct and important
  remark.
- **Part (iii) + bonus**: `A/min(m,s2) >= A/m >= c_A` (case-split-free) —
  correct; `s2 >= 1122800/7921 = 141.7498` exact; `min(m,s2) = m` on the
  band with the W7 margin `8000/7921 = 1.00997` (1.0%) — I confirmed
  `s2/m = 1.1723 > 1` at the deepest point `lam = 0.89`, `m = 401` by
  direct summation. The prover's caution (do not spend the 1.0%) is
  correctly propagated by the composite (Remark C.2).
- **§5.3 evenness** (`Var(U_j^{-lam}) = Var(U_j^{lam})`): correct (h even);
  this is what actually carries the mirror step of the composite's §3 proof
  (see repair R3).
- **Truth spot-checks** (mine, direct `s2` summation at `m = 401`, band
  edges `w0 + 1e-6` and `lam = 0.89`): truth `>= certified floor >= c_A`
  at all seven bands. R8 (the plan's W1-headroom grid artifact; true W1
  infimum `~0.2992` at `w -> 4+`, not `0.3189`) — confirmed:
  `A/m = 0.299193` at `w = 4 + 1e-6`.

### 1.2 Theorem A3 (= SL3) — hand re-derivation: CORRECT, fully

- **Lemma SL3.B / C.1**: M2-mixture proof correct (law of total variance,
  dropped `Var(E[.])` term); the identity `(1-q)^2/q = 4 sinh^2(lam/2)`
  exact; `A <= m h(lam) < m`. All three proofs of C.1 check out; SL2's
  identity route is indeed the shortest.
- **Lemma SL3.D**: Step 1's difference law re-derived
  (`P(D=d) = c_j^2 q^d (1-q^{2(j-d)})/(1-q^2)`, `g_j` nonincreasing —
  correct incl. the clip at `d >= j`). Step 2's Chebyshev-pairing
  cross-multiplication: I re-derived the double-sum identity; the `d2 > b`
  block vanishes by antisymmetry, the `d2 <= b` block is termwise `<= 0`.
  Correct. Step 3: the tail closed form `T(n)` verified at `n = 1` against
  `q(1+q)/(1-q)^3`; the nonincreasing-on-`{lam n >= 2}` derivative argument
  correct (each of the three bracket terms separately dominated); the
  real-argument extension to `T(x0/lam)` legitimate since
  `x0 >= x2 = 2.9251 > 2`.
- **Lemma SL3.A**: `Eps` decomposition into `phi1^2 psi`, `phi1 chi`
  monotone factors correct (`phi1 = int_0^1 e^{-lam u} du` decreasing; `psi`,
  `chi` increasing); the 890-interval certificate in
  `sl3_nc1_certificates.py` is a genuine per-interval monotone bound
  (verified in source: `phi1(a_lo)`, `q(a_hi)` — correct directions), i.e.
  point-evaluation class, NOT grid sampling. My independent dense scan:
  sup `Eps(., x1) = 0.32236 <= 0.35`, sup `Eps(., x2) = 0.54856 <= 0.57`
  (their interval bounds 0.32257/0.54890 sit correctly above). Continuum
  values 0.2490/0.4402 re-derived by hand from
  `e^{-x}(x^2 + 2x + 2)/2`.
- **Theorem SL3.1**: the per-factor skeleton
  (`|nu_j|^2 = 1 - 2 E sin^2(tD/2)`, concavity `sin u >= 2u/pi` on
  `[0, pi/2]`, truncation at `b = pi/t`) is correct; the range conditions
  `x1 <= pi/0.8`, `x2 <= pi/1.074` verified; `c1 = 0.1317175 >= 1/8`,
  `c2 = 0.0871362 >= 1/11.5` verified; `j = 1` factor trivial. Truth
  spot-checks (mine, direct `|phi|` product at `m = 401`,
  `w in {4.05, 7, 356.89}`, six `t`-points per `w`): both tiers hold
  pointwise.
- **Lemma SL3.C**: convex-composition argument correct
  (`arcsin` convex increasing on `[0,1)`, `sinh` convex increasing,
  `f(0) = 0` so `f(y)/y` nondecreasing); `t_0(0.89)/0.89 = 1.0737238 <=
  1.074` independently confirmed (margin 2.76e-4 — thin but real, single
  endpoint evaluation, house-approved class).
- **Theorem SL3.2**: Mills applications re-derived (mid: `ac^2 = A/32`,
  prefactor `8/sqrt(2pi) <= 3.192`; crossover: `ac^2 = 0.64A/11.5 >=
  0.0556A`, prefactor `11.5/(1.6 sqrt(2pi)) <= 2.87` — extending the
  GAUSSIAN integral beyond `t_0` is legitimate since the `|phi|`-bound is
  only used on `[0.8 lam, t_0] c (0, 1.074 lam]`). Far piece: the
  **cross-file citation is verbatim-correct** — wp1-c Corollary W.5(ii)'s
  scope is `pi/m <= |lam| <= 1.7627`, `t in [t_0(lam), pi]`, which contains
  `4/m < lam <= 0.89` (`4 > pi`); W.3(i) gives `q(., 1)` nondecreasing;
  `M_1 = m sinh(lam/2) >= w/2 > 2`; and I re-computed
  `q(2, 1) = I(2,1)/4 = (2 log(8/5) - 2(arctan 2 - arctan 1))/4 =
  0.0741265` by hand from W.3's closed form. Normalization algebra
  (`A sqrt(s2) = A^{3/2}/lam`, `1/lam < m/4`, `A <= m`) correct;
  `P3(401) = 1.257e-7 <= 1.3e-7` confirmed. Monotonicity thresholds
  (16 / 8.99 / 33.74) re-derived. Band table values re-computed
  independently (P1 = 1.0125, P2 = 0.0592 at `A0 = 112.28` etc.).
  True `T_u` at `m = 401` measured (mine): `2.2e-6` at `w = 4.05` —
  bound-side by 5+ orders, as SL3 says.
- **D2 is a genuine architect-route defect, correctly documented**: the
  plan's W.6-slot arithmetic evaluates an `A`-increasing prefactor at the
  band's LOWER `A`-floor; with the only available cap (`A <= m`) the needed
  corner exponent is 8.4-class vs the provable 4.9. SL3's tier-(i')
  replacement is strictly stronger than the `0.2` slot on the whole scope
  (`P2 <= 0.0592` worst band, `<= 0.2` for `A >= 90`, and
  `c_A(401)-floors >= 112.28`). D3 (far display missing `1/lam`) is also a
  real plan defect, correctly repaired.

### 1.3 Theorem A5 (= SL5) and the composite's §3–§4 — CORRECT

- **Lemma SL5.0** = C.1 (independent proof, M2 reproved inline in three
  lines — correct). **Lemma SL5.1**: (i)/(ii) elementary and correct;
  (iii)'s exact certificate chain (`(402/401)^3 = 1.0075 < 1.0746 <=
  e^{0.0746}`; `far(401) <= 9.229e-4`) verified in the script source —
  all one-sided in the safe direction (`P_N(x) <= e^x` partial sums,
  `sqrt` via exact squaring).
- **SL5's two corrections to the plan are both real and both necessary**:
  the B.0(i) far-fallback arithmetic is false as printed (`0.024 m^3`
  gives `221.3` at `m = 401`, not `0.028`; the plan's numbers trace to
  `0.024 m^2` — I checked the substitution), and the plan's "each entry
  nonincreasing in `A`" quantifier is false for the far entry. The
  corrected quantification `A in [c_A(W) m, m]` with the far entry handled
  by the uniform SL5.1(iii) cap is sound, and every actual `(k, m)` lies
  in the range (lower end A2(ii), upper end C.1).
- **The ledger table**: worst-case reduction (all `A`-dependent entries
  maximized at `A = c_A(W)*401`; domain check `c_A*401 = 112.28 > 32`)
  correct. I recomputed all seven rows independently (both the SL5
  3.19-flavor and the composite's harmonized 3.192-flavor): every entry,
  every total, every margin, and `C*_eff = max T(W)/c_A(W) = 16.9088`
  (exact `4734473/280000`) confirmed; variant [2] (16.3700) and variant
  [3] (`m >= 1581`: 10.0809 vs 136) confirmed. `C5 = 3` on W1–W6b is
  justified (`lam <= 40/401 < 1/2` there); `C5 = 8` is a valid W7 worst
  case. The D1 impact isolation (`+0.000634` at W1, margin
  `0.8662 -> 0.8655`) is exactly right.
- **Theorem CL-composite's proof (§3)**: the chain
  `|theta| L u <= 20 c_A/A <= 20/min(m,s2)` is correct (uses A2(iii)'s
  `A >= c_A min(m,s2)`); the mirror step is carried by SL2 §5.3's evenness
  (see repair R3); `s2 >= 141.7498 > 79` makes the spec's `s2 >= 79`
  clause non-binding, so the delivered hypothesis set contains the spec's.
  Under the harmonized (H4) (far slot = the constant 0.01) the upper cap
  `A <= m` is not even needed for the table — citing C.1 is harmless.
  **Given (H1) and (H4) as stated in §5.1, the conditional theorem is
  proved.** I note (as the composite implicitly does) that this
  conditional is deliberately thin: (H4) already carries the analytic
  content of the ratio law; the delivered value is the closed band
  arithmetic + the floors/caps that make the ledger close with 15.5%
  headroom.

### 1.4 Interfaces (the historical failure mode) — ALL CHECKED, all clean

R1–R9 of the composite's §2 were each re-verified against the source files:
SL3's consumed form of SL2 = delivered (verbatim); SL5's (H2) = SL2(ii)+(iii)
delivered-plus; the D1 mid-constant mismatch (`3.19` unachievable,
`8/sqrt(2pi) = 3.191538`) repaired by recompute with verdicts unchanged; the
R5/R6 far-entry and quantifier corrections adopted coherently; R7's triple
Lemma C.1 legitimately merged; R8/R9 accurate. Cross-file citations checked
verbatim: wp1-c W.3/W.5(ii) (scope inclusion verified — see 1.2), M2
(`referee_t2_maths.md` §3, quoted correctly, reproof matches), merged-draft
Lemma 3.1 + mirror (`F2_PROOF_DRAFT.md` §3, `r(N-k) = r(k)` line 349), the
CL spec (plan header vs `wp3_draft_a2.md` §5/§6.1 — see repair R1),
T.10(2)/T.8'' cited nowhere (grep-verified). B.0(i) consumed nowhere in
proof-bearing material (only inside the labeled ESTIMATES [4], flagged).
W.6 consumed nowhere. **No sub-lemma consumed a form another sub-lemma did
not deliver.**

### 1.5 Circularity — NONE

The delivered proofs (A2, A3, C.1, SL5's arithmetic, the composite chain)
consume only: the tilt frame (Lemma 3.1, upstream, non-circular), M2
(independent, reproved inline), wp1-c W.3/W.5(ii) (far-region decay — no
Prop 3.5/Theorem A content), and elementary analysis. `r(k)` appears in the
delivered material only inside the declared hypothesis (H4) and in the
conditional conclusion. Nothing assumes Prop 3.5(i)/(ii), Theorem A, or any
consequence thereof.

### 1.6 Regime boundaries — checked

`w -> 4+`: open-band floors legitimate (`V(w) > V(4)`, strict monotonicity);
the band-edge is where SL2's W1 margin (0.0075 on the floor) and the ledger's
worst row (margin 0.8655) both sit — verified. `lam = 0.89`: every cap
evaluated at the endpoint exactly (UBv(89/100), Eps sup attained on the top
interval, `t_0(0.89) = 0.9556 < pi`). `s2 >= 79`: never binds
(`s2 >= 141.7498`). `min(m, s2)`: equals `m` on the whole band, W7 margin
1.0% — flagged, not spent. `m >= 401`: enters only through `w1/401` caps,
`c_A*401 > 32`, and the `m = 401` worst-case evaluations, all safe-direction
in `m`. Band partition `(4, 5], ..., (40, oo)` of `{w > 4}`: gap-free.
`lam = 0` (N even): outside CL's hypothesis, correctly delegated upstream.

### 1.7 The honesty apparatus (§5.2–5.3) vs the orphaned artifact — FAITHFUL

I read `sl4_nc1.py` in full and its archived output line by line. Every
number the composite quotes from it is quoted correctly (`129.86`/ratio
`128.3` at W1 `gamma = 1/8`; far `1191` u-units at `w = 4.05` with the
orphan's cruder floor `m qW = 20.23`; R5 transfer `29.47` vs `1.81`, ratio
16.3; Part C totals `3.753–13.678` on W2–W6b; W7 `19.171` vs `16.0` with
crude main-term pricing `8.24` and the computed-eta rebalance to `~15.7`;
sliver `w >= 4.51` at `m = 401` improving to `4.05` by `m = 560`; only W6b
closes under stated SL1–SL3, `M* = 34868`). The assembler's independent
re-sizing under A3's sharper far floor (`0.0741 m`) is in `wp4asm_chain.py`
[4], clearly labeled ESTIMATES/floats/not-proof-bearing, and its
`m = 432/450` sliver-closure figures reproduce. The §5.3 honest-bridge
formulas (SL4' slots) match the orphan's `entry_num_*` functions
(`38.30 = 48 sqrt(2pi)/pi`, `sqrt(2/pi) = sqrt(2pi)/pi` — checked). The
composite's judgment that (H4)-as-architected is "very likely not
assemblable from (H1)+A2+A3 as stated" is the correct reading of this
(unrefereed, but internally coherent) evidence; note carefully — and the
composite does — that this refutes the ROUTE/normalization, not the truth
of CL (the measured truth margin is untouched).

## 2. Findings and repairs (all text-level; no constant, threshold, or verdict moves)

**R1 (wording, the one load-bearing clarification).** §3's "this is the full
`CL(C_0* = 79, C* = 20, Lambda* = 0.89)` of `wp3_draft_a2.md` §6.1 ...
verbatim" — the delivered hypothesis band is `|lam(k)| in (4/m, 0.89]`,
which matches the PLAN's spec block (which carries the `(4/m, .]` cut) and
§6.1's support item 1 ("only `4/m < lam <= 0.89` ever arises"); but
wp3-a2's bare parameter definition of `CL(C_0*, C*, Lambda*)` (§5, "The
future crude law, as a parameter") has NO `4/m` lower cut — it reads "for
interior `k` with `s2 >= C_0*` and `|lam(k)| <= Lambda*`". The delivered
statement does not cover `|w| <= 4` (nor should it: Theorem S's R2 row —
the sole consumer — is `{k > K_c, |w(k)| > 4}` BY DEFINITION, and `|w| <= 4`
is R3's, closed by T.9-final machinery). Add one sentence to §3 or Remark
C.3 recording this scope note, so the future assembly session cannot
mis-plug a `|w| <= 4` case into CL.

**R2 (display, rounding direction).** §7 prints "`10.08 <= 136`" for
variant [3] while §0 says "`10.09`" and §4 says "`10.0809`". The exact
certified upper bound is `201619/20000 = 10.08095`; "10.08" rounds a
certified UPPER bound DOWN. Harmonize to `10.081` (or `10.09`) in §7.
Nothing depends on it (vs budget 136).

**R3 (pointer).** §3's proof line "(mirror: ... `s2` invariant — §0
frame)": the frame merely asserts the convention; the PROOF of
`s2(-lam) = s2(lam)` is SL2 §5.3 (evenness of `h`, via Lemma SL2.0).
Re-point the citation (one word); Theorem A2's statement "(i) ... for every
real `lam`" already imports it.

**R4 (qualifier, optional).** §5's "What is NOT in doubt" quotes NC-PL3's
truth margin (`1.1696/1.1710` vs 20) measured at `m = 120/200` — below the
`m >= 401` scope. The supporting evidence AT scope is NC-PL1's budget
column at `m = 401` and wp3-a2's NC-P3d (`6.7x` at the spec point,
referee-reproduced, STATUS_wave2). One qualifying clause ("deep-band
`m = 120/200`; at-scope support: NC-PL1/NC-P3d") would make the sentence
self-contained. The claim itself is fair.

**Thin margins independently confirmed (carried flags, no action):**
`t_0(0.89)/0.89` vs 1.074: 2.76e-4; `c2` vs `1/11.5`: 0.2% (but consumed
only through Mills with 8x headroom above it); SL2's W7 `min(m,s2) = m`:
1.0% (correctly quarantined); W1 ledger row margin 0.8655; SL3's exact
`eps_j` vs `Eps` slack: 4.4% worst (my own adversarial point at
`lam = 0.89`, `j = 401`, `b = x1/lam`: `0.2355 <= 0.3224`, consistent).
All are single point-evaluation-class certificates in the house-approved
sense; none is grid-sampled.

**Trivia (no repair needed, recorded):** (i) composite §1 A3(ii) states
"`P2` for `A >= 9`" — SL3's threshold is 8.99, fine; (ii) §5.2's "~`s2`
times larger" for the far transfer is order-of-magnitude language inside a
clearly-labeled estimates section (the actual ratio at `w = 4.05` is
`~8.7e6` vs `s2 ~ 1.2e6`) — acceptable as flagged; (iii) SL5's script
banner says "Theorem SL2.4" for its §4 Proposition — internal label slip
in a docstring, not in any .md.

## 3. Script verification summary

All eleven wave-3 scripts re-run 2026-08-12; every output byte-identical to
its archive: `wp4_SL2/sl2_e1|e2|e3`, `wp4_SL3/sl3_nc1|nc2`,
`wp4_SL5/sl5_nc1|nc2`, `wp4_assembly/wp4asm_chain`, plus the orphan
`wp4_SL4/sl4_nc1` output read against its archive (not re-run — consumed as
archived evidence, matching the composite's usage). Proof-bearing scripts
audited at source level for safe-direction arithmetic: `sl2_e2` (exact
Fractions, one-sided exponential brackets — sound), `sl5_nc1` (exact
Fractions, `P_N <= e^x`, sqrt-by-squaring — sound), `wp4asm_chain` [1]–[3]
(same class — sound; [4] labeled non-proof-bearing), `sl3_nc1` (mpmath
dps-40 point evaluations + per-interval monotone bounds — house-approved
class, genuinely interval-based).

## 4. Independent adversarial script (mine)

`/private/tmp/claude-501/-Users-sihaohuang-Desktop/0c711691-81ac-42b2-8712-819b1ee08f6b/scratchpad/ref_wp4_check.py`
(mpmath dps 30, SAVED and RUN 2026-08-12; key verbatim output):

```
 w0=  4: V=0.298333 leftRiem(1/8)=0.287513 tableLBV=0.287512  LBV<=Riem<=V: True   [... all 7 True]
 cap(  4)=0.012469: v(cap)=0.00001296 tableUBv=0.00001296  v<=UBv: True            [... all 7 True]
 w=4+1e-6: A/m=0.299193 certified floor=0.287499 c_A=0.28 truth>=floor: True       [... all 7 True]
 lam=0.89: A/m=0.928555 >= 0.852716? True ; s2/m=1.172270 > 1? True
 dense sup Eps(.,x1) on (0,0.89] = 0.32236 <= 0.35: True
 dense sup Eps(.,x2) on (0,0.89] = 0.54856 <= 0.57: True
 c1=0.1317175 >= 1/8: True ; c2=0.0871362 >= 1/11.5: True
 t0(0.89)/0.89 = 1.0737238 <= 1.074: True
 w=4.05: tier1 holds at sampled t: True ; tier2 holds: True    [also w=7, w=356.89]
 exact eps_401(x1/lam) at lam=0.89: 0.23552 <= Eps=0.32235: True
 w=4.05: A=121.97 T_u(true)=2.234e-06 <= P1+P2+P3=0.8155: True
 W1: total=4.7344 ... pass=True T/cA=16.9087   [... all 7 pass]
 effective C* = 16.9087 (composite claims 16.9088-16.909)
 q(2,1) check: 0.0741265
```

(The float `16.9087` vs the exact upper bound `16.9088` differ in my
float truncation direction only; the exact Fraction `4734473/280000`
= 16.90883 is the certified value.)

## 5. Bottom line for the campaign ledger

- `wp4_draft_composite.md`: **MINOR_REPAIRS** (R1–R4 above, all
  text-level). Its conditional Theorem CL-composite, its three delivered
  PROVED components (A2, A3, C.1 — each also independently reusable), its
  recertified constant chain (`C*_eff = 16.9088 <= 20`), and its honest
  §5 account of the missing (H1)/(H4) and the refuted architected
  normalization are all verified.
- **CL(79, 20, 0.89) itself: still OPEN** — nothing in this report or in
  the composite changes STATUS_wave2 §4's bottom line. The next wave should
  target §5.3's honest bridge (SL1' banded `C5*`, SL3' mid-exponent
  `gamma*`, SL4' kernel-weighted ledger, plus the W1 far sliver by
  sharpened small-tilt far bound or harness extension to `~450`), for which
  the delivered A2/A3/C.1 remain exactly the right substrate.
- Note for the numerics referee (house-rule second half): the heaviest
  outstanding numeric surface is SL3's NC-SL3-1 interval certificate and
  SL2's E2 Fraction chain — both audited here at source level and
  independently cross-checked, but a full independent re-build (different
  code path, higher dps) of the two would complete the two-referee pattern
  used in waves 1–2.

*End of referee_maths_wp4.md.*
