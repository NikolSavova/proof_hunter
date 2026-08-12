# Adversarial MATHS referee report — `g2_draft_t2_20260803.md` (finalized 2026-08-05)

*Referee pass 2026-08-11 (wave 2) — the missing half of the house-rule pass
(STATUS.md §3, §5.2). Scope per assignment: the draft's PROVED inventory —
T.1, T.2, T.3, T.4, T.4', T.5, T.6(i)(ii)(iii-final), T.7b-final, T.7c,
(T.8a), T.8'', T.9'', T.10 — plus the F1 repair chain flagged by the numerics
referee. Every proof re-derived by hand; every constant chain recomputed
independently (mpmath dps 40–50 / exact Fractions, NOT the draft's scripts);
every stated scope checked against its proof; circularity with G2 itself and
untracked small-tilt assumptions hunted explicitly. The draft's own §8 items
1–5 were NOT re-litigated (known open, per assignment). Default-to-refutation
stance throughout.*

*Read in the required order: STATUS.md, `F2_PROOF_DRAFT.md`, `g1_draft_b.md`
(B.0–B.9 citable), the target draft, `referee_t2_numerics.md` (its F1–F9 are
built on below), `wp1_draft_c.md` + `wp2_draft_b.md` (both double-refereed
MINOR_REPAIRS; cited only as marked, with their §2a/§2b caveats flagged at
each use). Blind protocol maintained: `g2_draft_t1_20260803.md` untouched.
No existing file modified.*

*Referee scripts (new files, saved and run 2026-08-11, CPython 3, mpmath /
stdlib Fractions): `g2_campaign_20260811/referee_t2_maths_scripts/`
`refm_a_t8pp_t10.py` (T.8'' route failure + rescue; T.10(2) disjointness +
repair; F1-repair range check), `refm_b_chains.py` (all constant chains),
`refm_c_identities.py` (independent exact-pmf cumulant check of (2.2)–(2.5);
T.5 staircase in exact Fractions; T.4 kernel partial fractions). Every number
quoted below is from a real run of one of these; verbatim output excerpts in
§6.*

---

## VERDICT: MINOR_REPAIRS

**The analytic core of the PROVED inventory survives.** T.1, T.2, T.3, T.4,
T.4', T.5, T.6(i)(ii)(iii-final), T.7b-final, T.7c, (T.8a) and T.9'' are
correct as scoped: I re-derived every proof by hand, found no circularity, no
untracked small-tilt assumption, and every load-bearing constant chain closes
(several by margins under 1e-6 — itemized). The corrected constants the
assignment named — `c_mu = 1/38`, `C_mu = 1.05/36`, `c = 1/6` — all verify.
Lemma T.9'', the draft's centerpiece, is fully sound (partial-fraction
mechanism, radius, term-ratio, and both displayed constants independently
recomputed). I also close the numerics referee's F9 by supplying the complete
constant chase for (T.6iii-final): the stated `1/6` is provable with ~1.9x
headroom (§2.6).

**Two PROVED-stamped items do not survive as written** (both repairable
without new mathematics, repairs supplied and script-verified):

- **T.10(2) is FALSE as displayed** (finding M1): with the draft's own
  `rho := 1 - 0.04 w_0^2`, the two regime sets it claims "overlap" are
  provably DISJOINT — separated by an annulus of relative width >= 7% — by
  the draft's own Lemma (T.4); the true boundary sits at `w* ~ 1.15–1.17 w_0`
  (measured against exact `sigma_lam^2`). The clause also rests on a wrong
  constant (0.0332; the proved (T.4)-upper at `w <= 1, m >= 30` is 0.0347,
  as the draft's own §6 example row correctly uses). Repair (verified):
  `rho := 1 - 0.022 w_0^2`, giving a genuine overlap annulus `[0.9 w_0, w_0]`
  of relative width 0.1 from (T.4)-lower alone. T.10(1) survives, but its
  parenthetical misidentifies the historical band (pi < 3.7, M3).
- **T.8''s displayed proof is broken** (finding M2): its route bounds
  `Var U_j` by the untruncated geometric's SECOND MOMENT, which exceeds the
  claimed `(1+1/lam)^2` for every `lam <= 0.31` (at `lam = 0.1`: 190.3 vs
  121). The statement is TRUE and I supply the one-line correct proof
  (memorylessness mixture identity => truncation lowers the VARIANCE, and
  `Var(Geom) = q/(1-q)^2 <= (1+1/lam)^2`); the final display's `-1` must
  also read `-2` (floor slop). Nothing downstream consumes T.8''.

The numerics referee's F1 is confirmed and sharpened (the false display fails
already for `delta > 0.0319`, exact root); its proposed inline repair
inequality is itself out of range as stated (M8) — the safe repair is either
the corrected small-`w` restatement given here or citing wp2-b Prop W.6 (with
wp2-b's §2b relabeling caveats). Full findings list in §3; consolidated
repair list in §5.

---

## 1. Method

Every item on the target list was (i) re-derived by hand from the merged
draft's Lemmas 1.1–1.5 / 3.1–3.4, g1_draft_b's B.0, and the draft's own §1–§2,
with each algebraic identity recomputed; (ii) checked statement-vs-proof for
scope mismatches; (iii) checked for circular dependence (on G2's own gapped
propositions, on T.8/T.9, and on any unproved small-tilt restriction); and
(iv) where a constant chain ends in a numeric display, the chain was
recomputed at dps 40–50 with the rounding direction audited. Structural
identities were additionally re-verified by an INDEPENDENT implementation
(exact-pmf convolution for the cumulant formulas — not the draft's per-factor
moment recursion; exact Fractions for the T.5 staircase; raw partial-fraction
sums for the T.4 kernel). Where a proof was found broken I attempted first to
refute the STATEMENT (adversarial search), and only after failing to break it
did I record a repair.

## 2. Item-by-item verification of the PROVED inventory

### 2.1 T.1 (exact identities; tilt invariance) — CORRECT.
Hand check: the ratio exponent `-2 lam k + lam(k-1) + lam(k+1) = 0` and `Z^2`
cancellation are exact; the generating-function factorization is the harness's
defining identity. Nothing to repair.

### 2.2 T.2 + summed forms (2.2)–(2.5) — CORRECT (independently re-verified).
Sign conventions re-derived: `E e^{theta U} = z_j(lam-theta)/z_j(lam)` gives
`kappa_r(U_j) = (-1)^r (d/dlam)^r log z_j(lam)`; with `log z_j = log j +
f(lam j) - f(lam)`, `f' = -g`, this yields exactly (2.2)–(2.5) with the
2026-08-05-corrected signs of `g''`, `g'''`. **Independent check** (script
`refm_c_identities.py`(a), NOT the draft's route): cumulants from the exact
convolved pmf of `X` at `(m, lam) = (8, 0.3), (12, 0.05)` agree with the
closed forms to rel. dev. `<= 8.1e-49`. The untilted limits reproduce Lemma
1.2. The g''-series fifth-order coefficient in the T.4' prose is 1/28800
(numerics F8(i)), confirmed by differentiating the Bernoulli series by hand.

### 2.3 T.3 (mean displacement, `1/38` and `1.05/36`) — CORRECT.
`mu' = -sigma_lam^2` re-derived from (2.2)/(2.3); MVT gives `N/2 - mu(lam) =
lam sigma_s^2`, `s in (0, lam)`. Upper: Lemma 3.2 (merged, proved) +
B.0(i) upper (`m >= 30`) give `(1.05/36) w m^2`. Lower: (T.4)-upper at
`w_s <= 1, m >= 30` is `0.0300(1+3/30+1/18) = 0.034667 <= 0.04`, so
`sigma_s^2 >= 0.9653 lambda >= 0.96 lambda`, and `0.96/36 = 1/37.5 >= 1/38`
(`refm_b_chains.py`(g)). **No circularity**: T.4's proof uses only (2.3), the
kernel `E(u)`, the `S*_4` bracket and B.0(i) — verified by inspection that it
nowhere invokes T.3.

### 2.4 T.4 (variance deficit, two-sided) — CORRECT as finally stated; two display-level defects.
The whole partial-fraction mechanism re-derived by hand:
`(1/4)csch^2(u/2) = sum_{n in Z} (u - 2 pi i n)^{-2}` (checked from the
standard csch expansion), the pair-sum `2(u^2-v_n^2)/(u^2+v_n^2)^2`, the
summand identity `2u^2(3v_n^2+u^2)/(v_n^2(v_n^2+u^2)^2)` (algebra recomputed),
`E(0) = 6 sum v_n^{-4} = 1/240` exactly, the DECREASING sign
(`d/ds` numerator `= -5v^2 - s < 0` — recomputed), and the lower-bound chain
`summand(u)/summand(0) >= (1+u^2/v_1^2)^{-2} >= 1 - u^2/(2 pi^2)`,
`2 pi^2 = 19.74`. Independent raw partial-fraction sums match the direct
`(1/12 - q(u))/u^2` to 5.4e-17 and the `1 - u^2/19.7` floor holds on
`(0, pi]` (`refm_c_identities.py`(c)). Step 2's assembly and both divisions
(via `S*_4/lambda in [6.857 m^2, 7.2 m^2(1+3/m)]`, recomputed) are correct;
numerics-F7's dropped `-m w^2/19` term is relative size `<= 6.7e-6` at
`m >= 30`, absorbed by the 0.02857 -> 0.0285 rounding (margin 2.5e-3) —
confirmed. The crude clauses: `0.0300 pi^2 (1.1 + pi^2/18) = 0.4880 < 1/2`
so `sigma_lam^2 >= lambda/2` on `|w| <= pi, m >= 30` — verified; the
`w^2/20` clause's m-scope is numerics-F6 (chain reaches m >= 3), confirmed.
Defects (display only): **(d1)** the numbered display (T.4a'') carries lower
coefficient `1 - u^2/25`, but the proof establishes (and the table + all
downstream uses take) `1 - u^2/19` — the /25 form is unproved; align the
display. **(d2)** the prose line "For |w| <= 1, m >= 30 this is
[0.0270 w^2, 0.0332 w^2]" is wrong arithmetic: the proved upper evaluates to
`0.034667 w^2` (the draft's OWN §6 example row prints `.034667`). Harmless
here, but T.10(2) imported the wrong 0.0332 (finding M1).

### 2.5 T.4' (kappa_3 / kappa_4 boxes) — statements TRUE; two rounding-margin defects.
Chain re-derived: `|g''| <= (|u|/120)(1 + u^2/12.5) <= 1.79|u|/120` on
`|u| <= pi` (the pointwise `|g'' - u/120| <= |u|^3/1500` is now proof-grade
via the numerics referee's alternating-series argument, ratio 1500/1512);
summing gives `1.79 * 1.18 |w| m^4/600 + 1.79|w|/120`. **Margin audit**
(`refm_b_chains.py`(b)): the total is `0.00352035 m^4 |w|` vs `1/284 =
0.00352113` — TRUE but with relative margin 2.2e-4; safe, worth a note since
the true ratio (NC-T3: 0.51) has 2x headroom the display does not show.
Recentred `kappa_4`: `(lam^2/500)(S_6+m) <= w^2 m^5/2200` re-derived
(via `(m+1)^7 <= 1.2621 m^7` at `m >= 30`, giving /2773 — safe). **Absolute
clause defect (M4):** the displayed rounding `(1+1/m)^5 <= 1.18` yields
`(1.18/600 + pi^2/2200) m^5 = 0.0064529 m^5 > m^5/155 = 0.0064516 m^5` — the
display MISSES its own target by 1.2e-6. The exact chain at `m = 30`
(`S*_4/120 <= 0.0019640 m^5`) lands at `0.0062948 m^5 <= m^5/155`, so the
CLAIM is true; fix the display (use 1.178, or state `m^5/154`). Nothing
downstream uses the absolute clause. (wp2-b's Lemma W.3 now supersedes both
boxes with wider scope `|w| <= 4` — modulo wp2-b's own §2b list.)

### 2.6 T.5 (variance lower bound, `c = 1/6`) — CORRECT, fully.
The staircase decomposition `p_i = sum_{s>i} c_s/s`, `c_s = s(p_{s-1}-p_s)`:
nonnegativity, normalization (`sum c_s = sum p_i = 1`, telescoping recomputed)
and the reconstruction identity verified in EXACT Fractions on 500 random
nonincreasing vectors (`refm_c_identities.py`(b): all exact, (**) min margin
exactly 0 at the uniform case). The (**) chain (`E U = ET/2`,
`E U^2 = (1/3)ET^2 + (1/6)ET`, Jensen, `(ET)^2/12 + ET/6 = (EU)^2/3 + EU/3`)
recomputed by hand — correct, including the degenerate `j = 1` factor.
`lam(k) >= 0` for `k <= N/2` (mu decreasing, mu(0) = N/2) makes the weights
nonincreasing exactly where used. (T.5-a) `k/3`, the Cauchy–Schwarz
enhancement `k^2/(3m)`, and `max(A,B) >= (A+B)/2` give `(k/6)(1+k/m)` — clean.
The downstream arithmetic (`k >= 12000` or `k >= sqrt(12000 m)`;
`(24 C_0)^2 = 2.3e9`) checks. This is the strongest item in the inventory:
elementary, unconditional (`m >= 2`, every interior `k <= N/2`), no scope
caveats. **PROVED confirmed.**

### 2.7 T.6 (cf identities and domination) — CORRECT; F9 CLOSED by this report.
(i) modulus identity re-derived (it is wp1-c's W.1 in pre-factored form;
independently hand-checked there and here). (ii) the
`|E e^{itV}|^2 = E cos(t(V-V'))` route, `sin^2(x/2) >= x^2/pi^2` on
`|x| <= pi`, `|V-V'| <= j-1 < m`: gives `exp(-(2/pi^2) s2 t^2)` on
`|t| <= pi/m`, and `2/pi^2 > 1/5` — correct, genuinely distribution-free and
lam-uniform (mechanism checked: nothing hides a tilt restriction).
(iii-final): the draft's displayed derivation is loose (numerics F9). **I
completed the constant chase** (`refm_b_chains.py`(f)): with `|t| <= 1/(2m)`,
`|z_j| <= v_j t^2 (1/2 + (j-1)|t|/6 + (j-1)^2 t^2/24) <= 0.5938 v_j t^2` and
`|z_j| <= 0.5938/16 = 0.0372`; `|log(1+z)-z| <= |z|^2/(2(1-|z|))
<= 0.5193|z|^2`; `sum_j E|V_j|^4 <= (m-1)^2 s2` and `sum_j |z_j|^2 <=
0.5938^2 t^4 (m-1)^2 s2/4`; total coefficient `1/24 + 0.0458 = 0.0874 <=
1/6`. The sign `+ i kappa_3 t^3/6` re-derived (`(it)^3 = -i t^3`). So
**(T.6iii-final) is PROVED with the stated constant and ~1.9x chain headroom**
— F9 can be retired once this chain (5 lines) is transcribed.

### 2.8 T.7b-final — CORRECT as scoped.
Chain re-verified: `p_i >= e^{-1}/j` on `J_*`; the pair-sum identity
`(1/j^2) sum sin^2 = (1/2)(1-|F_j|^2)` (recomputed from `sin^2 = (1-cos)/2`);
the count of `j in (m_*/2, m_*]` is `>= m_*/2 > m_*/2 - 1 >= m_*/4` at
`m_* >= 4` (and `m >= 32` gives `m_* >= 9.2`); `j|t| >= (1/2)(1-pi/m) =
0.4509 >= 0.45` at `m = 32`; all chosen `j >= 3 >= 2` so (T.7b-cert) applies.
(T.7b-cert) itself is now proof-grade (numerics §3; I re-checked the
j-monotonicity kernel `sin u - u cos u > 0` and the endpoint
`sin^2(0.1125) = 0.012603 >= 1/80` — sound, including the `c/2 < pi` domain
detail). Assembly: `80 e^2 = 591.12`, factor count `m_*/4`, doubling gives
exponent `m_*/4729` — the displayed `/4730` is the SAFE direction
(`refm_b_chains.py`(d)). Scope `0 <= lam <= pi/m` is used exactly where
stated (`m_* >= m/pi - 1`). No hidden assumptions.

### 2.9 T.7c — CORRECT as scoped.
The pairwise tilt comparison `p_i^{lam} >= e^{-lam(j-1)} p_i^0` (via
`z_j(lam) <= j`) re-derived — this is the step that RETIRES tilted analysis,
and it is airtight for `lam >= 0` (symmetry handles the rest). Count:
`2.8/(sqrt2 pi) = 0.6302`; `m(1-0.6302) - 1 >= 0.35m` from `m >= 50.5`
(draft: 51; lemma scope 64 — safe), and the `j = 1` exclusion is absorbed by
the `-1` (checked both branches `2.8/t >= 2` and `< 2`). (T.7c-cert) is
proof-grade (numerics §3; endpoint `sin^2(0.7) = 0.4150 >= 0.35`). Assembly:
`0.35 * 0.35 = 0.1225`, square root, `0.06 <= 0.06125` — safe direction
(`refm_b_chains.py`(e)). The lemma is honest about its weakness (the
`e^{-2K}`), which wp1-c's W.4 has since superseded (both its referees
MINOR_REPAIRS): none of my checks disturbs that supersession.

### 2.10 (T.8a) (complex kernel identity at the tilted mean) — CORRECT.
Re-derived from lattice inversion: at `x = 0` the three phases are `1`,
`e^{i(s-t)}`, symmetrization kills the odd part `i sin(s-t)` under the
symmetric measure `phi(s)phi(t)` (swap argument recomputed; `D` real). Exact;
machine-verified by NC-T6 (numerics D1 covers the roundoff quote). The
adjacent claim that Lemma 1.5's proof is pure Fourier algebra and applies to
complex `phi_lam` — confirmed by the rederivation.

### 2.11 T.8'' — statement TRUE, displayed proof BROKEN (finding M2, repair supplied).
See §3 M2. Verified: the rescue proof is one line, and the statement (with
`-2` in place of `-1`) then follows; numerically the stated `-1` form has no
counterexample on a 44-point `(m, lam)` grid against exact `sigma_lam^2`
(`refm_a_t8pp_t10.py`(c)) — but as PROVED it must carry `-2`.

### 2.12 T.9'' — CORRECT, fully verified (the draft's centerpiece survives adversarial review).
(a) The partial-fraction bound `|g^{(r)}(u)| <= 2 r! zeta(r+1)/(2pi)^{r+1}`
for ALL real `u`: re-derived (differentiate the pole expansion; `|u + 2 pi
i n| >= 2 pi n` on the real line — this is exactly where lam-uniformity
enters, and it is complete). The summed form `(S_r+m) 2(r-1)! zeta(r)/(2pi)^r`
recomputed; at `r = 4` the constant `2*3! zeta(4)/(2pi)^4 = 1/120` EXACTLY
(`refm_b_chains.py`(c)) — consistent with NC-T9a's sharpness ratio 0.9974.
(b) Radius: zeros of `z_j(lam - it)` in complex `t` sit at
`t = -2 pi l/j - i lam` (`l` not divisible by `j`; the `u = 0` and
`u = 2 pi i l'` points are removable since `z_j -> j != 0` — checked), so
`|t| >= 2pi/m > t_1` uniformly in `lam`: the cumulant series of each factor
converges on `|t| <= t_1` and sums to a continuous branch of `log phi_lam^c`.
Term ratio: recomputed as `[r/(r+2)][zeta(r+1)/zeta(r)] (m+1)|t|/(2 pi)
<= sqrt2 (m+1)/(2m) = 0.73068` at `m = 30` vs displayed 0.7314 — safe.
First-term chains: `r = 7`: `1/1.0629e7`, `/0.2686 -> 1/2.8549e6 >= 1/2.8e6`
— SAFE; `r = 4`: `7.014e-5 -> 2.6113e-4` — confirms numerics F2 (print
2.62e-4). One presentational note: "principal branch" should read "the
continuous branch with value 0 at t = 0" (they can differ in principle; the
bound concerns the series, so nothing breaks). **PROVED confirmed** — with
F2's one-digit fix and F5's `m >= 6` parenthetical fix.

### 2.13 T.10 — (1) survives with a band-label repair; (2) FALSE as displayed (finding M1).
See §3. Verified for (1): `lambda/2 >= m^3/72 >= 2000` first at `m = 53`
exactly (52 gives 1952.9), and the crude (T.4) clause it rests on is proved
for `m >= 30` — consistent. The claim "the band is covered TWICE over" is
proved only for `[1/m, pi/m]`; the parenthetical identifies this with the
historical `[1/m, 3.7/m]` band, but `pi < 3.7` (M3).

---

## 3. Findings (ranked; each verified by a saved, run script)

**M1 (moderate — the substantive maths finding of this pass). T.10(2) is
false as displayed; the "PROVED" stamp on T.10 must be qualified.**
Statement under review: *"choosing `rho := 1 - 0.04 w_0^2` makes the two
regimes overlap in a `w`-annulus of relative width >= 0.1 for every
`w_0 <= 1`"*, where the two regimes are `{|w| <= w_0}` (T.9's set) and
`{sigma_lam^2 <= rho lambda}` (T.8's rho-set). Refutation: `{sigma_lam^2 <=
rho lambda} = {deficit >= 0.04 w_0^2}` and, by (T.4)-UPPER (the correct
constant `0.0347`, not the quoted `0.0332`), `deficit(w_0) <= 0.0347 w_0^2 <
0.04 w_0^2` — so the rho-set requires `w^2 >= (0.04/0.0347) w_0^2`, i.e.
`|w| >= 1.074 w_0`: the two sets are DISJOINT, separated by a gap annulus of
relative width >= 7.4%. This is not bound-slack: against the TRUE deficit
(exact `sigma_lam^2` from (2.3), `refm_a_t8pp_t10.py`(d)) the rho-set
boundary sits at `w* = 1.150–1.174 w_0` across `m = 60/100/200`,
`w_0 = 0.5/1`. The draft's own two displayed implications already exhibit the
disjointness — the sentence draws the opposite conclusion from its own
arithmetic. **Repair (verified, (f)): set `rho := 1 - 0.022 w_0^2`.** Then by
(T.4)-LOWER: `deficit(w_0) >= 0.0270 w_0^2 > 0.022 w_0^2`, and deficit
nondecreasing in `|w|` (merged draft Lemma 3.3, fully proved), gives
`{sigma_lam^2 >= rho lambda} subset {|w| <= w_0}` for ALL `w` (contrapositive
— T.9's hypothesis holds on all of region 3 with `K = w_0`), and `deficit(0.9 w_0) >= 0.0221 w_0^2 >
0.022 w_0^2` gives `{|w| >= 0.9 w_0} subset {sigma_lam^2 <= rho lambda}`:
the two hypothesis sets genuinely overlap in the annulus `[0.9 w_0, w_0]`,
relative width 0.1, for every `w_0 <= 1`, `m >= 30`. Same conclusion shape,
different constant, one-line proof from (T.4) as it stands. T.10(1) is
unaffected. Downstream exposure: nothing in the campaign has yet consumed
(2)'s specific `rho` (Theorem A's assembly is not yet run), so this is a
repair, not a retraction of any dependent result — but §8's "T.10
(hypothesis-set overlap) PROVED" and the ledger rows quoting it must carry
the corrected clause.

**M2 (moderate proof-defect, statement survives). T.8''s displayed proof does
not prove its statement; corrected proof supplied; final display off by one.**
The route "`Var U_j^{lam} <= E_lam U_j^2 <=` untruncated `E X^2`" cannot
reach `min(j, 1+1/lam)^2`: for `X ~ Geom(e^{-lam})`,
`E X^2 = q(1+q)/(1-q)^2 > (1+1/lam)^2` for every `lam <= 0.31`
(`refm_a_t8pp_t10.py`(a): at `lam = 0.1`, `190.3 > 121`; 30 violations on
the grid `lam = 0.02..0.59`). Repair (one line, script-verified to 7e-38 on
a 42-point grid): memorylessness gives the exact mixture
`law(X) = alpha law(U_j) + (1-alpha) law(j + X)`, `alpha = 1 - q^j`, whence
`Var X = alpha Var U_j + (1-alpha) Var X + alpha(EU_j - EX)^2-terms >=
alpha Var U_j + (1-alpha) Var X`, i.e. **`Var U_j <= Var X = q/(1-q)^2 <=
(1+1/lam)^2`** (via `1-q >= lam/(1+lam)`, `q <= 1`) — truncation lowers the
VARIANCE, which is what the chain needed (it does NOT lower the second-moment
bound far enough). Separately, the conclusion `m_* >= sqrt(s2/m) - 1`
overstates: `m_* = min(m, floor(1/lam))` can sit 2 below `min(m, 1+1/lam)`,
so the chain proves `m_* >= sqrt(s2/m) - 2` (no counterexample to `-1` found
against exact `sigma_lam^2` on a 44-point grid, but `-1` is unproved).
Downstream exposure: NONE found — T.8-final's (V) uses `m_* >= m/pi - 1`
directly from its `|lam| <= pi/m` hypothesis, not T.8''. Fix the proof text
and the constant; the PROVED stamp then stands.

**M3 (minor, statement-level). T.10(1)'s band label overstates coverage.**
The proved double-coverage is for `1/m <= |lam| <= pi/m`; the historical
draft-S hole (merged draft §6 item 4) is `[1/m, ~3.7/m]`, and `3.7 > pi`.
The sliver `(pi/m, 3.7/m]` IS in T.9's hypothesis set (any `K >= 3.7`), but
its membership in T.8's variance set is NOT derivable from T2's own (T.4)
(scope `|w| <= pi`). Repair: either reword ("the band `[1/m, pi/m]`, the
bulk of the historical hole"), or cite wp2-b Lemma W.1(i) —
`1 - s2/lambda <= 0.0330 w^2` for ALL real `w`, PROVED there (flag: wp2-b is
MINOR_REPAIRS-citable, §2b) — which gives `s2 >= 0.548 lambda` at `w = 3.7`
and closes the sliver at hypothesis level. §8 item 6's repetition of the
claim needs the same edit.

**M4 (minor, display). T.4' absolute-kappa_4 clause: the displayed rounding
fails its own target.** With the displayed `(1+1/m)^5 <= 1.18`:
`(1.18/600 + pi^2/2200) m^5 = 0.0064529 m^5 > m^5/155 = 0.0064516 m^5`
(`refm_b_chains.py`(a), miss 1.2e-6). The exact chain at `m = 30` gives
`0.0062948 m^5 <= m^5/155`, so the CLAIM is true — replace 1.18 by 1.178 (or
state `m^5/154`). Cousin note: the kappa_3 `/284` chain closes with relative
margin only 2.2e-4 (`refm_b_chains.py`(b)) — true, but any future rounding
touch will break it; consider printing `/283`.

**M5 (minor, display/prose). (T.4a'') carries an unproved `1 - u^2/25` lower
coefficient.** The proof (and the constants table, and every downstream use)
establishes and uses `1 - u^2/19`; the numbered display still says `/25`,
and the surrounding proof text retains two abandoned false starts (the
"increasing in u^2" paragraph later corrected mid-page). Align the display
with the proved `/19` and strike the dead text. Same class: the prose line
"[0.0270 w^2, 0.0332 w^2]" after (T.4) must read `0.0347` (see M1 — this is
where T.10(2)'s wrong constant came from; the draft's own §6 quote
`.034667` is correct).

**M6 (observation, positive). (T.6iii-final) is provable as stated —
numerics F9 discharged.** Complete chain in §2.7 above: total coefficient
`1/24 + 0.0458 = 0.0874 <= 1/6` with every step displayed
(`refm_b_chains.py`(f)). Transcribing five lines into the draft retires the
"least rigorous PROVED item" flag.

**M7 (trivial). T.10's statement header** "for `m >= max(180, m_0(i))`" uses
an undefined symbol `m_0(i)`; the body proves (1) for `m >= 53` and (2)
needs only `m >= 30`. Fix the header.

**M8 (repair-of-a-repair; affects the F1 fix, not the draft directly). The
numerics referee's proposed F1 inequality is out of range as stated.**
F1 itself is CONFIRMED and sharpened: `(1-d)^{-2} <= 1 + 2.1 d` fails
exactly for `d > 0.0319` (root of `2.1d^2 - 3.2d + 0.1`,
`refm_b_chains.py`(j)) — well below the used `delta <= 0.35`. But the
proposed replacement "`(1-d)^{-2} <= 1 + 2d + 3.5d^2` for `d <= 0.4`" is
ITSELF false for `d > ~0.107` (`refm_a_t8pp_t10.py`(g): at `d = 0.2`,
`1.5625 > 1.54`; at `d = 0.4`, `2.778 > 2.36`). The repair still works where
it is needed — at `|w| <= 1`, `delta <= 0.0347` (correct constant, per M5)
gives `(1-delta)^{-2} <= 1 + 2 delta + 3.5 delta^2` and total
`|B_lam/B_m - 1| <= (1 + 0.273 w^2)(1 + 0.0736 w^2) - 1 <= 0.37 w^2` —
but the restated inequality must carry `d <= 0.1`, not `d <= 0.4`. The
CLEANER repair remains citing wp2-b Prop W.6 (`|B_lam - B_m| + 36 a^2/P_0^2
<= B_m c_w(K) w^2`, `c_w(1) = 0.407`, `c_w(2) = 0.466`, `c_w(4) = 0.951 ->
carry 1`), with wp2-b's §2b caveats: W.6 must be relabeled grid-certified,
and `c_w(4) = 1` — i.e. T.9's `c_w = 1/2` then holds for `K <= 2` only.
Either way, §5's "load-bearing pieces fully proved here" list must drop or
re-derive the `B_lam/B_m = 1 + theta 0.35 w^2` line (it is true — measured
max `0.1134 w^2` — but has no valid pi-range derivation in any current
document; the multiplicative-chain shape provably cannot reach `w = pi`, as
the numerics referee showed via `1.198 w^2`).

---

## 4. Circularity and scope audit (assignment-specific)

**No circularity with G2 found.** Dependency map of the PROVED inventory,
established by line-level inspection: T.1, T.2, T.5, T.6, T.7b, T.7c,
(T.8a), T.9'' are self-contained (merged-draft Lemma 1.1/3.1-class facts +
elementary analysis only). T.3 uses T.4 (declared; T.4's proof verified free
of T.3) + B.0(i) (g1_draft_b, double-refereed) + Lemma 3.2 (merged, proved).
T.4 uses (2.3) + B.0(i) + an exact `S*_4` polynomial bracket (hand-checked:
holds from `m = 4`). T.10 uses T.4 only. **Nothing in the PROVED list invokes
T.8, T.9, Prop 3.5, or any calibration-grade numeric.** The one dependency of
a PARTIAL item on a PROVED one (T.8's core bucket citing (T.9''c)) runs in
the safe direction.

**No untracked small-tilt assumption found.** The historical failure mode
(silent `w <= pi`) was hunted at each item: T.6(ii) and T.9'' are genuinely
lam-uniform — in both, uniformity has an identifiable mechanism (per-factor
distribution-free inequality; real-axis distance to the pole lattice) that I
verified rather than trusted. (T.6iii-final)'s header carries `w <= pi,
m >= 30` which its proof never needs (over-restriction, safe). T.4/T.4'
carry `|w| <= pi` explicitly and use it; T.7b-final's `w <= pi` enters via
`m_*` exactly as stated (the first pass's error here is already corrected in
the target draft); T.7c's `|w| <= K` enters only through `e^{-2K}`. T.3's
`0 <= w <= 1` is used (via T.4 at `w_s <= 1`). Scope table (constants table
rows) checked row-by-row against the proofs: all consistent except the M4/M5
display items.

**Statement-vs-proof mismatches found:** exactly those listed (M1, M2's
`-1`, M4, M5, M7) — plus the two the numerics referee had already found
(F5, F6), which I confirm.

## 5. Consolidated repair list (what must change before §8's PROVED list stands)

Text/label-level unless marked. In the draft's own §8 status terms: after
these repairs, every item of the PROVED inventory stands; without them,
T.10(2) and T.8'' are not proved as displayed.

1. **T.10(2)** [maths]: replace `rho := 1 - 0.04 w_0^2` by
   `rho := 1 - 0.022 w_0^2` and the clause by the verified two-inclusion
   form (M1); correct `0.0332 -> 0.0347` in both places (M5); fix the
   `m_0(i)` header (M7).
2. **T.10(1)/§8-6** [statement]: band label `[1/m, 3.7/m] -> [1/m, pi/m]`,
   or close the `(pi/m, 3.7/m]` sliver by citing wp2-b W.1(i) (M3).
3. **T.8''** [maths]: replace the `E U^2` route by the memorylessness
   mixture identity (M2, one line, supplied); `-1 -> -2`.
4. **T.9 §5 "fully proved" list** [maths]: drop/re-derive the
   `B_lam/B_m = 1 + theta 0.35 w^2` line per F1 + M8 — either the small-`w`
   restatement (`|w| <= 1`, `(1-d)^{-2} <= 1+2d+3.5d^2` with the corrected
   range `d <= 0.1`, yielding `0.37 w^2`) or cite wp2-b Prop W.6 with its
   §2b caveats (grid-certified label; `c_w(4) = 1`).
5. **T.4'** [display]: `1.18 -> 1.178` (or `/155 -> /154`) in the absolute
   clause (M4); note the `/284` margin (2.2e-4).
6. **(T.4a'')** [display]: lower coefficient `/25 -> /19`; strike the two
   superseded false-start paragraphs; fix the `[.., 0.0332]` prose line (M5).
7. **(T.6iii-final)** [upgrade]: transcribe the five-line constant chase of
   §2.7 — this RETIRES numerics F9.
8. Apply the numerics referee's F2 (2.62e-4), F5 (`m >= 6`), F6 (`m >= 3` +
   direct `m = 2` check), F7 (display), F8 (typos) — all confirmed by this
   pass where they touch mathematics.

Per the no-erasing rule these belong in a new `t2_repairs_2026xxxx.md`
(STATUS §5.3's planned repair-application session), not in the target file.

## 6. Key script output (verbatim excerpts, runs of 2026-08-11)

`refm_a_t8pp_t10.py`:
```
(a) violations of EX2 <= (1+1/lam)^2 ... 30 found; at lam=0.1: EX2 = 190.3251  (1+1/lam)^2 = 121.0000  Var(Geom) = 99.9167
(b) mixture identity max rel dev over grid: 7.116e-38   VarU<=VarX everywhere: True
(c) violations of stated -1 form on grid: none (chain as displayed gives only -2)
(d) m= 60 w0=1.0 : w* (deficit = 0.04 w0^2) = 1.1671 = 1.1671*w0  -> sets DISJOINT (w*>w0)
    m= 200 w0=1.0 : w* = 1.1742*w0 -> DISJOINT   [all 6 rows DISJOINT]
(e) 0.0300(1+3/30+1/18) = 0.034667   (prose claims 0.0332)
(f) deficit(w0)  >= 0.02700 w0^2 > 0.022 : True ; deficit(.9w0) >= 0.02210 w0^2 > 0.022 : True
(g) d=0.120: (1-d)^-2 = 1.29132 vs 1+2d+3.5d^2 = 1.29040 -> FALSE  [also d=0.2, 0.4 FALSE]
```

`refm_b_chains.py`:
```
(a) exact  S*_4/120/m^5 + pi^2/2200 = 0.0062948 <= 1/155 : True
    displayed (1.18/600) + pi^2/2200 = 0.0064529 <= 1/155: False  (miss 1.24e-06)
(b) kappa_3 chain 0.00352035 vs 1/284 = 0.00352113 : holds True (margin 7.8e-07)
(c) term ratio at m=30 = 0.73068 <= 0.7314 ; r=7: 1/1.0629e7 -> 1/2.8549e6 >= 1/2.8e6 True
    r=4: 2.611277e-04 (F2 confirmed) ; 2*3!*zeta(4)/(2pi)^4 = 1/120 exactly: True
(d) 80 e^2 = 591.124 ; (1/2)(1-pi/32) = 0.4509 >= 0.45 True
(f) T.6iii total coeff: 1/24 + 0.0458 = 0.0874 <= 1/6 : True
(g) sigma_s^2 >= 0.9653 lambda ; 0.96/36 = 1/37.50 >= 1/38 : True
(h) m^3/72: m=52: 1952.9, m=53: 2067.7 ; pi = 3.14159 < 3.7
(i) crude clause 0.4880 < 0.5 : True
(j) (1-d)^{-2} <= 1+2.1d fails for d > 0.0319
```

`refm_c_identities.py`:
```
(a) (2.2)-(2.5) vs exact-pmf cumulants: max rel dev 8.1e-49  [8 rows, 2 (m,lam) pairs]
(b) staircase exact on 500 Fraction vectors: True ; (**) min margin = 0.0
(c) E(u) partial-fraction vs direct: 5.4e-17 ; 240E >= 1-u^2/19.7 on (0,pi]: True ; E decreasing: True ; E(pi)*240 = 0.71049
```

## 7. What remains

1. **The repairs of §5** (one session, new file per the no-erasing rule).
   Items 1–4 have mathematical content (constants/proof text); 5–8 are
   display-level. After them, the house rule's both-referee bar is met for
   the T2 PROVED inventory: **T.1–T.7c, (T.8a), T.8'' (repaired), T.9'',
   T.10 (repaired) stand at MINOR_REPAIRS from both referees**, and the
   campaign drafts' citations of them are on two-referee footing.
2. **Unchanged and NOT re-litigated here** (per assignment; the draft's own
   §8 items 1–5, restated by STATUS §2): the deep-tilt core model (item 1
   non-far half), region-2 handoff (item 2), T.9's `Delta_ker` bucket
   (item 4, = missing wp2-a), T.8's `C = 600` assembly, and the `m_2(K)`
   thresholds (item 5 — closed at exponent level by wp1-c, pending its
   prefactor caveat). My findings change none of their statuses.
3. **Status corrections this report forces in the ledger**: T.10's row in
   T2 §8 and in any downstream citation should read "PROVED modulo M1/M3
   repairs (clause (2) restated with rho = 1 - 0.022 w_0^2)"; T.8''s row
   "PROVED modulo M2 repair (`-2`)". No other PROVED stamp changes.
4. **Positive deltas usable downstream**: the completed (T.6iii-final)
   constant chase (§2.7); the memorylessness variance-domination lemma
   (M2's rescue — `Var(trunc geom) <= Var(geom)`, exact mixture identity),
   which is independently useful for any future `lam > 1/2` far-bound work
   (T2 §8 item 1's sliver); the corrected T.10(2) constants, ready for
   Theorem A's assembly.

**Verdict: MINOR_REPAIRS** — every load-bearing analytic lemma in the PROVED
inventory survives hand re-derivation; two stamped items (T.10(2), T.8'')
fail as displayed and are repaired here with script-verified replacements;
the remaining defects are rounding/display-level. Nothing found that changes
the status of T.8/T.9 (PARTIAL) or reopens any closed item.

*End of report. Blind protocol maintained: `g2_draft_t1_20260803.md` was not
read at any point.*


