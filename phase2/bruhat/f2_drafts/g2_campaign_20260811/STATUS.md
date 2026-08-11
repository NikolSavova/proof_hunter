# STATUS — G2 closure campaign, synthesis (2026-08-11)

*Synthesis editor pass (read-everything role). Sources: every file under
`g2_campaign_undefined/` (2 drafts, 4 WP referee reports, 1 T2 referee report,
referee scripts), `g2_draft_t2_20260803.md` §8, plus the four required context
documents and `g2_campaign_20260811/CAMPAIGN_NOTES.md`. No file modified; this
file is new. House rule applied throughout: an item counts as CLOSED only if a
draft closing it received SURVIVES or MINOR_REPAIRS from BOTH of its referees;
MINOR_REPAIRS = closed-modulo-listed-repairs, and the repair lists are copied
in full below (§2a, §2b, §3).*

**Campaign-completeness caveat (read first).** The campaign plan
(`CAMPAIGN_NOTES.md`) called for SEVEN drafts (wp1 a–d: four routes at the
deep-tilt far lemma; wp2 a–b: the two remaining bucket pieces; wp3 a: the
region-2/C_0 handoff) plus a two-referee house-rule pass on the T2 draft.
What actually landed on disk: **wp1-c and wp2-b only**, each with both
referees; and **only the numerics half** of the T2 referee pass
(`referee_t2_numerics.md` — no `referee_t2_maths.md` exists). wp1-a/b/d,
wp2-a, wp3-a produced no files. (Run artifact: outputs landed in
`g2_campaign_undefined/` rather than the planned `g2_campaign_20260811/` —
the workflow's date argument evidently failed to substitute; treat
"undefined" = the 2026-08-11 campaign.) Everything below accounts for the
missing packages explicitly.

---

## 1. Verdict table

| Work package | Deliverable | Draft self-reported status | Maths referee | Numerics referee |
|---|---|---|---|---|
| **wp1-c** `wp1_draft_c.md` | Lemma W.1–W.3 master tilted far-region bound; Cor W.4 (small tilt), Cor W.5 (deep tilt), Clause W.6 (crossover); new thresholds m_2(1..4) = 143/190/267/379 | W.1–W.6 PROVED; T2 §8 item 5 closed; far-region half of item 1 closed; item 4 and deep-tilt core NOT touched | **MINOR_REPAIRS** (`referee_maths_wp1_c.md`; every load-bearing claim survives; repairs R1–R5, all text-level) | **MINOR_REPAIRS** (`referee_numerics_wp1_c.md`; all 5 scripts reproduce exactly; 4510 adversarial cases, zero violations; repairs R1–R4, prose-level) |
| **wp2-b** `wp2_draft_b.md` | Tilted model polynomial (W.0); dictionary to \|w\| ≤ 4 (W.1–W.3); Taylor bucket (W.4); Lin bucket (W.5); c_w envelope audit (W.6); exact assembly W.7 with kernel bucket Delta_ker left pending | Two of three item-4 buckets done + assembly; **T.9 still PARTIAL pending wp2-a**; c_w(4)=1/2 FALSE-as-proved (use 1) | **SURVIVES WITH MINOR REPAIRS** (`referee_maths_wp2_b.md`; findings F1–F6; one benign code bug, one status inflation on W.6) | **MINOR_REPAIRS** (`referee_numerics_wp2_b.md`; all scripts reproduce exactly, 0 mismatches; repairs 1–5) |
| wp1-a, wp1-b, wp1-d | (alternate far-region routes) | — never landed | — | — |
| **wp2-a** | kernel-transfer + denominator bucket (Delta_ker) — **the missing piece of item 4** | — never landed | — | — |
| wp3-a | region-2 handoff (item 2, C_0 = 2000 → small) | — never landed | — | — |
| **T2 house-rule pass** `g2_draft_t2_20260803.md` | (target of the overdue referee pass) | its own §8: T.1–T.7c, T.8a, T.8'', T.9'', T.10 PROVED; T.8, T.9 PARTIAL; items 1–5 open | **MISSING — no maths referee report exists** | **MINOR_REPAIRS** (`referee_t2_numerics.md`; all 12 scripts genuine and reproduce; findings F1–F9, F1 moderate) |

Both completed work packages therefore pass the both-referees bar and are
citable modulo their repair lists. The T2 draft itself still carries only ONE
referee (numerics); under the house rule its PROVED inventory is *not yet*
fully refereed — flagged in §4.

---

## 2. Updated G2 residue ledger (T2 §8 items 1–5)

### Item 1 — T.8 far region / deep tilt. **PARTIALLY CLOSED.**
- **Far-region half: CLOSED (modulo §2a repairs)** by wp1-c Corollary W.5 +
  Clause W.6 (both referees MINOR_REPAIRS). The band `lam in (pi/m, 1/2]` —
  and up to `|lam| <= 1.7627`, plus a rho-family for any fixed tilt — now has
  an explicit far bound `exp(-m q(m sinh(lam/2), 1))` with floor
  `exp(-0.0372 m)` on `t in [t_0(lam), pi]`, in exactly the
  `t_0(lam)`-moving form the diagnostic
  (`g2_item1_deep_tilt_notes_20260805.md`) proved necessary; the crossover
  zone `[pi/m, t_0(lam)]` has the explicit W.6 bound (measured within 2% of
  truth). Pointers: `wp1_draft_c.md` §5–§6; verification
  `g2_scripts/campaign_undefined/wp1_c/`.
- **Still OPEN: the deep-tilt CORE model** (wp1-c §9 item 2, endorsed by both
  its referees): for fixed `lam`, `sigma_lam^2 = Theta(m)`, the Gaussian core
  has width `Theta(m^{-1/2}) >> t_1`, and T.9'''s model radius `~1/m` covers a
  vanishing fraction of it; a T.8 rebuild needs a new core lemma (identified
  route: cumulant model with radius `~ c·lam` from analyticity in the strip
  `|Im t| < lam`). Also still open: T.8's own bucket assembly behind `C = 600`
  (never certified — T2 §8 item 4's second half, T2 §4).

### Item 2 — Region-2 handoff arithmetic (C_0 = 2000 mismatch). **UNTOUCHED.**
wp3-a never landed. Standing state unchanged from T2 §8 item 2: (T.5-final)
`s2 >= (k/6)(1+k/m)` is PROVED, but `s2 >= C_0 = 2000` needs `k >= 12000` (or
`k >= sqrt(12000 m)`), so the band `sqrt(m)/4 <= k < 12000` reaches T.8's
hypothesis only for astronomically large `m`; numerics say the truth is
`C_0 ~ 10`. The diagnostic's check (b) additionally showed `lam*(m)` GROWS
toward 1 (deep tilt is load-bearing across nearly the whole `lam` range), so
item 2 interacts with the item-1 core gap. No new files address it.

### Item 3 — Finite certificates ((T.7b-cert)/(T.7c-cert), Sturm-able). **CLOSED.**
Two independent closures:
1. wp1-c (both referees MINOR_REPAIRS) supersedes both Dirichlet-kernel grid
   certificates on every range the campaign consumes — the Lemma W chain uses
   no grid-certified inequality (after repair R4 adds the one-line
   `tan x > tanh x` proof).
2. `referee_t2_numerics.md` §3 upgrades (T.7b-cert), (T.7c-cert) AND the T.4'
   kernel bounds to proof grade analytically (envelope + j-monotonicity +
   endpoint evaluations; alternating-series bounds giving exactly
   1500/1512 = 0.992063), scripts
   `g2_campaign_undefined/referee_t2_scripts/ref_cert_dirichlet.py`,
   `ref_kernel_smallu2.py`.
Note: wp2-b *introduces* new grid-certified items (its W.1(ii), PW-grid
flavor, Hermite sups) — same status class, honestly labeled, listed in §2b;
so the class is not extinct, but item 3 as stated in T2 §8 is closed.

### Item 4 — T.9's mechanical bucket table / explicit C_R(K). **PARTIALLY CLOSED.**
Done and both-refereed (wp2-b, modulo §2b repairs):
- Pointwise bucket: grid flavor `PW_grid = 1.5491 / 4.0889 / 4.9126`
  (K = 1/2/4; K=4 value exceeded by +0.22% beyond the m ≤ 2000 grid — repair
  1) and a closed-form all-m flavor `10.28 / 21.06 / 187.4` at `m >= 180`.
- Taylor bucket (Lemma W.4, PROVED): `T = 0.00035 / 0.00100 / 0.01402` at
  `m >= 180`.
- Linearization bucket (Lemma W.5, conditional-as-labeled):
  `Lin = 0.231 / 0.257 / 0.372` at `m = 180`.
- `w^2`-envelope audit (Prop W.6, to be relabeled grid-certified): proved
  coefficient `c_w(1) = 0.407`, `c_w(2) = 0.466` (T.9's `c_w = 1/2` OK for
  K ≤ 2); **`c_w(4) = 0.951` — T.9's `c_w = 1/2` is FALSE-as-proved at K = 4;
  statement must carry `c_w(4) = 1`** (true mechanism: `kappa_4(lam)` crosses
  zero near `w ~ 3.3`; the numerics referee measured the signed sum at only
  `+0.005..+0.011 B_m w^2`, so `c_w(4) <= 1/2` is likely recoverable inside
  W.6 with signed two-sided kappa_3 boxes — not yet done).
- Exact assembly (Theorem W.7): `s2 log r(k) = 1 - B_m(1 + theta_1 c_w(K) w^2)
  + theta_2 [PW+T]/m^2 + Delta_ker(k)`, with `Delta_ker` exactly defined.
**Still MISSING: the kernel-transfer + denominator bucket `Delta_ker`** —
wp2-a's package, never landed. Its TRUE size is measured (wp2-b NC-W4(6),
independently re-verified in exact arithmetic by the numerics referee):
`~1.39 / 4.07 / 5.04` in C_R units, stable over `m = 30..140` — i.e. it is
comparable to the whole pointwise bucket and cannot be waved away. **Item 4 is
NOT closed; T.9 remains PARTIAL.**

### Item 5 — The binding far exponent / m_2(K) thresholds. **CLOSED (modulo §2a repairs).**
wp1-c Corollary W.4 (both referees MINOR_REPAIRS): `|phi_lam(t)| <=
exp(-c_1(K) m)` on `[t_1, pi]` for `|lam| <= K/m` (`K <= m/4`, `m >= 30`),
with `c_1(1) = 0.2259`, `c_1(2) = 0.1802`, `c_1(4) = 0.1019` — 28x to 5067x
larger exponents than T.7c's, degradation polynomial in K rather than
`e^{-2K}`. Under the standing NC-T10d criterion (replicated and referee-
reproduced) the refined-law thresholds fall from `m_2(1) ~ 7.3e3`,
`m_2(4) ~ 5.1e6` to **`m_2(1) = 143` (inside the exact-harness range
`m <= 150` — no uncovered m at all for K = 1), `m_2(2) = 190`,
`m_2(3) = 267`, `m_2(4) = 379`**. Untilted corner `c_1'(0) = 0.4617` is a
drop-in strengthening of Lemma 1.4 (would pull g1's far-arc `m_1` from ~180
to ~60; re-evaluating B.8's other buckets at smaller m is flagged, not done).
Caveats carried (wp1-c §9 item 5): the threshold criterion is a proxy — the
eventual T.9/T.8 assemblies must verify their own polynomial prefactors
against the new exponents; and the bands `151..189 / 151..266 / 151..378`
(K = 2/3/4) need the planned harness extension.

### §2a. wp1-c repair list (verbatim union of both referees; none touches a constant, lemma, or threshold)
1. (R1 both) §9 item 3's "margin >= 5e-5" is FALSE for six of thirteen named
   constants (min margin 9.1e-6 at `c_1(0)`; also `c_1(3)` 2.4e-5, `c_1(6)`
   1.3e-5, `c_1(pi)` 4.4e-5, `c_1'(2)` 1.5e-5, `c_1'(4)` 1.8e-5). All
   roundings ARE safe-direction; restate as "margin >= 9e-6".
2. (R2 both) `2 asinh(sqrt 10) = 3.7371...`, not "3.7358" (aside only).
3. (R3 maths) Restate W.5(iii) case-wise (`[pi/m, pi]` for `|lam| <= pi/m`;
   `[t_0(lam), pi]` for `pi/m <= |lam| <= 1.7627`) so statement matches the
   proof's (larger) established range, which §6's coverage table uses.
4. (R4 both) Add the one-line proof that `sinh(x)/sin(x)` is increasing on
   `(0, pi/2)` (`tan x > tanh x`, via `(cosh x sin x - sinh x cos x)' =
   2 sinh x sin x > 0`) — currently grid-only, contradicting the "no grid
   certificates anywhere" claim.
5. (R5 both) Scope "supersedes T.7c everywhere" (W.4 carries `K <= m/4`,
   `m >= 30`); reword the "(V) reproduced: 292672" line ("same convention
   recomputed: 2.9e5; T2 quoted ~2.5e5 — discrepancy in T2's own loop").

### §2b. wp2-b repair list (verbatim union of both referees; none changes a table entry at its printed precision)
1. (both) Fix `wp2b_lib.py` series fallbacks: g4 last term `-u^5/15840` (not
   /22176), g5 `-u^4/3168` (not /4435.2); re-run NC-W2/3/4 (impact <= 2.7e-6,
   no printed digit moves).
2. (maths F2 / numerics 7) Relabel Prop W.6 from "PROVED" to grid-certified;
   state `c_w(4) = 1` (the grid's 0.9506 is not a safe bound — finer grid
   finds 0.9509); note the harmless spurious `+(dir_ratio - 1)` addend in the
   script's upper branch; optionally add the per-piece monotonicity page to
   upgrade K = 1, 2 to fully proved.
3. (numerics 1) PW_grid K=4: the certified 4.9126 (m <= 2000) is exceeded
   beyond the grid — 4.9233 at (m, w) = (20000, 2.725), +0.22%, still rising;
   carry the K=4 grid row as "m <= 2000" or extend and restate ~4.93
   (C_R^PT grid K=4: 5.2985 -> ~5.31).
4. (numerics 2) W.1(ii): all-integer-m max is 0.379644 at (32, 4.0) (mod-4
   bumps), not 0.3789 at (30, 4.0); still <= 0.40, `c_4 = 0.60` stands; run
   the exhaustive sweep (maths F3).
5. (maths F4) Inline the two one-line tail arguments closing W.1(i) for all
   m >= 30 (`6m^4 - 51m^3 - 265m^2 + 10 >= 0`) and NC-W2(f)'s ranges — the
   maths referee's V2 already supplies them.
6. (maths F5) Add: the final T.9 envelope can be fixed only after wp2-a's
   `Delta_ker` lands (it may carry its own `w^2/m` dependence).
7. (numerics 4) Reword §5's Finding/§9 item 2: the cancellation is internal
   to W.6's two parts (measured signed sum +0.005..+0.011 B_m w^2); signed
   two-sided kappa_3 boxes suffice — no bucket-coupling lemma needed for
   `c_w(4) <= 1/2`.
8. (maths F6 / numerics 5) Trivia: "15 monomials" (not 13); 187.414 (not
   187.5); drop numpy from the banner; prove or drop `v > 0` in W.7 (numerics
   referee measured min v = 1.29e-5 > 0 on the used range); one-line Lin
   monotonicity; align the Hermite-sup grid with the stated `|y| <= 1/2`;
   "1.00001" -> "1.000016".

---

## 3. T2 referee outcome (house-rule pass)

**Status: INCOMPLETE — only the numerics referee ran.** `referee_t2_numerics.md`:
**MINOR_REPAIRS**. All 12 scripts under `g2_scripts/t2*/` are genuine, run,
and reproduce the draft's quoted figures (two roundoff-level deviations, one
conservative misquote). No fabricated PASS. The two grid-only certificates and
the T.4' kernel bounds were upgraded to proof grade (§2, item 3 above).

Repairs demanded (must be applied before T2's §5 "fully proved" list stands):
- **F1 (moderate, the only substantive one):** T.9 Step 2's chain for
  `B_lam = B_m(1 + theta·0.35 w^2)` is broken — the display
  `(1-delta)^{-2} <= 1 + 2.1 delta for delta <= 0.35` is FALSE for
  delta >= ~0.025. Truth measured: max `|B_lam/B_m - 1|/w^2 = 0.1134` (3x
  margin), so the sub-claim is true but underived. Repair: restate for
  `|w| <= 1` with `(1-d)^{-2} <= 1 + 2d + 3.5d^2` (gives ~0.36 w^2), or
  re-derive `w <= pi` from the exact deficit identity. (Note: wp2-b's Prop
  W.6 independently supplies valid `B_lam/B_m` bounds on `|w| <= 4` — the
  natural repair is to cite it.)
- F2: (T.9''c)'s constant rounds unsafely — print 2.62e-4 (chain gives
  2.6113e-4).
- F3: T.8-final's "(V) holds for m >~ 2.5e5" is not reproducible; actual
  2.96e5 (s2 = C_0) / 1.07e6 (worst case). Mis-sizes an admitted restriction.
- F4: NC-T10 row's "slack 24x–4e7x" — actual minimum 789x (conservative
  misquote).
- F5: T.9'' step-2 parenthetical false at (m, r) = (4, 3), (5, 3); fix to
  m >= 6 (lemma's scope m >= 30 unaffected).
- F6: T.4's crude clause chain reaches only m >= 3 (clause true at m = 2 by
  direct check; nothing downstream uses m = 2).
- F7: T.4 lower-bound display drops a `-(lam^2/240) m w^2/19` term (absorbed
  by rounding slack; display fix).
- F8: typos — g'' series fifth-order coefficient 1/28800 (not 1/43200);
  `E U^2 = 6.294` (not 6.31); nc5 docstring 0.015544.
- F9: T.6(iii-final)'s displayed derivation is the loosest of the
  PROVED-stamped items (60x measured headroom; safe, flagged).

**Outstanding house-rule debt: the T2 MATHS referee pass.** Until it runs,
T2's proved inventory (T.1–T.7c, T.8a, T.8'', T.9'', T.10) — which BOTH
campaign drafts cite as established — has single-referee status. This is the
same debt g1_draft_b discharged before becoming citable.

---

## 4. Bottom line: is Theorem A = F2(a) fully proved?

**NO.** G2 (= Prop 3.5, the single load-bearing gap for Theorem A) is
substantially narrowed but not closed. What the campaign changed: the
far-region obstruction (T2 §8 items 5 and 1-far) is gone — a single
elementary master bound now covers every `(t, lam)` regime with
`e^{-c m}`-class exponents and practical thresholds — and item 4 is reduced
to exactly one missing bucket. What still stands between here and Theorem A,
**smallest first**:

1. **Apply the listed repairs** (§2a, §2b, §3): all text/label-level; the
   only one with mathematical content is T2-F1 (a valid `B_lam/B_m` chain —
   or cite wp2-b's Prop W.6, whose bounds both referees verified).
2. **Run the T2 maths referee pass** (house-rule debt; no new mathematics,
   but the campaign's citations rest on it).
3. **Prop 3.5(ii) [T.9], remaining piece: the kernel-transfer + denominator
   bucket `Delta_ker` with an explicit constant** (= the never-landed wp2-a;
   the last piece of T2 §8 item 4). Exactly defined in wp2-b Theorem W.7;
   true size measured `~1.4 / 4.1 / 5.0` C_R units; the pattern is
   g1_draft_b's Lemma B.6 in the tilted frame at y = 0 with two odd rows —
   one mechanical session. Then merge W.7 + Delta_ker + wp1-c's W.4(i) far
   bound into a closed-form T.9 with explicit `C_R(K)` and thresholds
   `m_2(1) = 143`-class; extend the exact harness past 150 (to ~200) to
   cover 150 < m < m_2(K)/m_1 bands. **This closes Prop 3.5(ii).**
4. **Prop 3.5(i) [T.8], crude uniform law — the genuinely open mathematics:**
   (a) the deep-tilt CORE model lemma (item 1's non-far half; identified
   route: cumulant model with radius `~ c·lam` from strip analyticity,
   paired with W.6's tail control);
   (b) T.8's bucket assembly behind `C = 600` re-run as a certificate (never
   done in any pass), now with wp1-c's far bounds replacing (V);
   (c) the region-2 handoff (item 2, UNTOUCHED): either prove T.8 at small
   `C_0` (numerics say truth ~10) or extend region 1's coverage — the
   never-landed wp3-a.
5. **Theorem A assembly** (merged draft §4) with the closed 3.5(i)+(ii) and
   explicit constants end to end.

Independently of G2: G3 (part (b) fine scale) and G4 (part (c) constant
chase) remain open as before; nothing in this campaign touched them, though
item 5's new exponents materially help G4's far-region feasibility
(g1 far-arc `m_1` ~180 -> ~60, wp1-c §6).

---

## 5. Recommended next session (concrete)

1. **Re-launch the missing work packages, wp2-a first.** wp2-a (Delta_ker
   bucket) is the highest-value mechanical item: it alone flips item 4 to
   closed (modulo referee) and, with `m_2(1) = 143 < 150`, yields a fully
   closed Prop 3.5(ii) at K = 1 upon merge. Give the drafter wp2-b's Theorem
   W.7 (the exact target object), wp1-c's W.4(i) (the far bound to use), and
   g1_draft_b's B.6 as the pattern. Then wp3-a (item 2), aimed at small
   `C_0` via the W-chain far bounds.
2. **Run the T2 maths referee** (the missing half of the house-rule pass) —
   one referee session, target list = T2's PROVED inventory + the F1 repair.
3. **One repair-application session**: apply §2a/§2b/§3 lists to new files
   (no-erasing rule: as `*_repairs_2026xxxx.md`, mirroring
   `g1b_repairs_20260802.md`), including the two library-coefficient fixes
   and re-runs.
4. **Harness extension** `mahonian.py` to m = 200 in exact rationals
   (minutes, per G4/NC-1) — covers every 150 < m < threshold band now
   quoted (persist per the no-erasing rule as a new script + output file).
5. Only then: the deep-tilt core model lemma (item 4's hard sibling; wp1-c
   §9 item 2's strip-analyticity route) — budget it as its own blind
   mini-campaign; it is the last genuinely new mathematics in G2.

*End of STATUS.md.*
