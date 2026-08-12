# referee_maths_wave5_sl4px — adversarial maths referee report on `wave5_sl4px_20260812.md`

*Wave-5 referee pass, F2 campaign, 2026-08-12. Target:
`wave5_sl4px_20260812.md` (Hypothesis SL4'-X: W1 crossover monotonicity —
Theorem X.1, Corollaries X.2/X.3) and its script
`g2_scripts/campaign_20260811/wave5_sl4px/x_constants_and_scan.py`
(`out_x_constants_and_scan.txt`). Protocol: maximal bar, DEFAULT TO
REFUTATION (this chain flips the paper's main conjecture to a theorem).
Every lemma re-derived by hand; every named constant recomputed; the
statement proved checked verbatim against what `STATUS_wave4.md` §2 item 3
and `wave4_sl4p_20260812.md` §3 record and against the exact consumer code
(`sl4p_nc1_ledger.py` `w6_x`/`X_w6`); [W.6] provenance checked against
`wp1_draft_c.md` §5; independent from-scratch verification script (own
closed-form derivative, NOT copied from the prover) run at dps 50,
including the extreme domain corner the prover did not scan. Sources read:
the target, `STATUS_wave4.md`, `wave4_sl4p_20260812.md`,
`referee_numerics_wave4_sl4p.md`, `wp1_draft_c.md` §5–§6, both scripts.
`g2_draft_t1_20260803.md` NOT read; no other wave-5 draft read. New files
only. Referee script (SAVED and RUN, output archived beside it):
`g2_scripts/campaign_20260811/referee_maths_wave5_sl4px/ref_mw5x_verify.py`
(`out_ref_mw5x_verify.txt`; directory name carries the `maths_` prefix —
a parallel `referee_wave5_sl4px/` script directory by another referee
exists and was NOT read beyond its directory listing).*

## VERDICT: **MINOR_REPAIRS**

**Theorem X.1 is CORRECT and Hypothesis SL4'-X is PROVED as recorded** — I
tried to refute it and failed. The proof is genuinely elementary calculus:
I re-derived every display by hand (the substitution, the product rule,
all three lemmas, both corollaries), independently re-implemented the
closed-form derivative `dx/dtau` and confirmed it against `mp.diff` to ~50
digits, recomputed all nine NX certificate checks, and attacked the one
domain corner the prover's own scan omitted (`w = 4` AND `lam = 0.89`
simultaneously — smallest `M` and largest `X` at once): everything holds,
with the margins the proof says it has. The statement proved matches
`STATUS_wave4.md` §2 item 3 and `wave4_sl4p_20260812.md` §3 VERBATIM (and
is strictly stronger); Corollary X.3's identification of the consumer sums
is byte-faithful to `sl4p_nc1_ledger.py` (`totn`/`totd`, weight at right
endpoint, exponential at left endpoint, uniform `n = 60`, the script's
`tau0` = `tau_0(lam)/lam`); the [W.6] provenance quote matches
`wp1_draft_c.md` Clause W.6 exactly (`1/r = s/S` in (W.3d)); the prover's
script re-runs BYTE-IDENTICAL and both quoted output blocks are verbatim.
No circularity: nothing downstream of [W.6] is consumed. The four findings
below are wording/scope-level only (m1 is the one consumers must see: the
"certified upper bound" sentence should carry its sl4p-pricing qualifier);
none moves a constant, a domain edge, or the PROVED status. Subject to the
m1 one-clause repair, the status flip SL4'-X: CONJECTURED -> PROVED is
endorsed, and the conditional surface of Theorem SL4' shrinks to
SL1'-w + SL3'-w + SL4'-E exactly as the note's §7 states.

## 1. Hand re-derivation of the proof (every step)

All checks below were done by hand first, then confirmed in my script
(§3); notation as in the target's §1 (`y = tau lam/2`, `h = sin y`,
`M = m h`, `s = h^2`, `S = sinh^2(lam/2)`, `X = s/S`).

- **The factorization** `x = P(h) g(h)` (§2 display): `(M-1)/(2M) =
  (1/2)(1 - 1/(mh)) = P(h)` ✓; `s/(SM) = h^2/(S m h) = h/(mS)`, so the
  bracket is `g(h) = log(1 + h^2/S) - h/(mS)` ✓. `P'(h) = 1/(2 m h^2)` ✓;
  `g'(h) = (2h/S)/(1 + h^2/S) - 1/(mS) = 2h/(S + h^2) - 1/(mS)` ✓.
- **Lemma X.a.** `sin y >= y(1 - y^2/6)`: the auxiliary
  `f(y) = sin y - y + y^3/6` has `f(0) = 0`, `f'(y) = cos y - 1 + y^2/2
  >= 0` (the cosine quadratic lower bound) ✓. Cap: `y = tau lam/2 <=
  (1.074)(0.89)/2 = 0.47793` — exact decimal, `1074 * 89 = 95586` checked
  by hand ✓; `1 - 0.47793^2/6 = 1 - 0.2284171.../6 = 0.9619304... >=
  0.96193` (I recomputed `0.47793^2 = 0.22841714...` by hand) ✓. Chain:
  `M = m sin y >= 0.96193 m y = 0.96193 (w tau)/2 >= 1.92386 tau >=
  1.9238 tau` at `w >= 4`, `>= 1.53904` at `tau >= 0.8` ✓. Uses `w >= 4`
  exactly where Remark R1 says.
- **Lemma X.b.** `X <= tau^2` from `sin y <= y`, `sinh(lam/2) >= lam/2` ✓.
  `phi(X) = X/log(1+X)` strictly increasing: `phi'` has the sign of
  `log(1+X) - X/(1+X) > 0` ✓. The reduction `g > 0 <=> M > phi(X)` ✓
  (all quantities positive). `psi(tau) = 1.9238 log(1+tau^2) - tau > 0`
  on `[0.8, 1.074]`: `psi(0.8) = 1.9238 log(1.64) - 0.8`; I recomputed
  `log(1.64) = 0.4946966...` by hand (via `log 1.6 + log 1.025`), giving
  `0.1516966 >= 0.1516` ✓; `psi'(tau) = 1.9238 * 2tau/(1+tau^2) - 1`,
  and `2tau/(1+tau^2)` has derivative `2(1-tau^2)/(1+tau^2)^2` (unimodal,
  peak at `tau = 1`), so its interval minimum is at an endpoint:
  `f(0.8) = 1.6/1.64 = 40/41 = 0.9756097...` (exact rational, checked),
  `f(1.074) = 2.148/2.153476 = 0.9974571...` (I verified `1.074^2 =
  1.153476` by hand), min `= 40/41 >= 0.9756`, so `psi' >= 1.87685928 - 1
  = 0.87685928 > 0` ✓. Hence `psi > 0` throughout, and
  `M >= 1.9238 tau > tau^2/log(1+tau^2) >= phi(X)` gives `g > 0` ✓.
  Margin note: at the worst endpoint the log-unit margin is `psi(0.8) =
  0.1517` and the `M`-vs-`phi` gap is `1.539 vs 1.294` (19%) — real room,
  nothing knife-edge.
- **Lemma X.c.** `g' > 0 <=> 2mSh > S + h^2 <=> Q(h) = h^2 - 2mSh + S < 0`
  ✓ (all denominators positive). Discriminant `4m^2S^2 - 4S = 4S(m^2S-1)
  > 0` since `m sqrt(S) = m sinh(lam/2) >= w/2 >= 2` ✓; roots
  `h_± = mS ± sqrt(m^2S^2 - S)` with product `S` (monic constant term) ✓.
  Placement: `h_- = S/h_+ <= S/(mS) = 1/m < h` (last step is `M > 1`,
  Lemma X.a) ✓; `h <= tau lam/2 <= 0.537 lam < lam <= (w/4) lam <=
  m (lam/2)^2 <= mS <= h_+` ✓ — both inclusions STRICT, so `Q(h) < 0`
  strictly ✓. Second use of `w >= 4`, again exactly per Remark R1.
- **Theorem X.1 assembly.** `dh/dtau = (lam/2) cos y > 0` since
  `y <= 0.47793 < pi/2` ✓; `dx/dh = P'g + Pg' > 0` (four positive
  factors) ✓; chain rule gives STRICT increase ✓. The stated floors
  restate Lemma X.a ✓.
- **Corollary X.2.** `sinh u <= u/(1 - u^2/6)` from `(2k+1)! >= 6^k`
  (base `k = 0, 1` equality; induction step `(2k+2)(2k+3) >= 6`) ✓;
  `sinh(0.445) <= 0.445/(1 - 0.0330042) = 0.4601881 < 1` so `arcsin` is
  in-domain on `[0, 0.445]` ✓. `D(v) = cosh v / sqrt(1 - sinh^2 v)` is
  the correct derivative of `arcsin(sinh v)` and is increasing (numerator
  up, denominator positive down) ✓, so `arcsin(sinh u) <= u D(u)` and
  `r'(u) = [u D(u) - arcsin(sinh u)]/u^2 >= 0` ✓; `r > 1` from
  `D(v) >= cosh v > 1` ✓. Max at `u = 0.445`: `r(0.445) = 1.07372378...
  <= 1.0739 < 1.074` ✓ (recomputed independently, §3 V4/V6f). So every
  used interval `[0.8, tau_0(lam)/lam]` is a nonempty subinterval of
  `[0.8, 1.074]` ✓.
- **Corollary X.3.** On each cell `[tau_i, tau_{i+1}]`: `(tau lam)^2 <=
  (tau_{i+1} lam)^2` (weight increasing) and `e^{-E(tau)} <= e^{-E(tau_i)}`
  (`E = m x` increasing by X.1) — freeze each monotone factor at its worst
  endpoint, integrate, sum ✓. Partition-free as claimed ✓. Numerically
  confirmed at `n = 60` for three W1 points (§3 V5: integral <= sum, both
  the `t^2`-weighted and unweighted lines).
- **Remarks R1–R3**: R1's usage accounting is exactly right (verified
  against my re-derivation above); R2's `X <= 1` on the actual crossover
  zone (`s <= S` iff `tau <= tau_0(lam)/lam`, `sin` increasing on
  `y < pi/2`) and `phi(1) = 1/log 2 = 1.4427 < 1.53904` ✓; R3's
  guard-never-fires claim follows from `M >= 1.53904 > 1` and `x > 0` ✓
  (and matters: it is what makes the ledger's `E` the honest exponent).

## 2. Interface fidelity (the historical failure mode — checked four ways)

1. **Against the ledger record (`STATUS_wave4.md` §2 item 3).** Recorded:
   "(SL4'-X) W1-only: `[W.6]`'s crossover exponent `x(w, tau)`
   nondecreasing in `tau` on `[0.8, 1.074]`". Theorem X.1 proves STRICT
   increase on exactly `[0.8, 1.074]`, for all `w >= 4`, `lam in
   (0, 0.89]` — a strict superset of the W1 band (`w in (4, 5]`,
   `m >= 401` gives `lam <= 5/401`). Discharged verbatim, no rescoping,
   no weakened interval. ✓
2. **Against the consumer's own hypothesis text (`wave4_sl4p_20260812.md`
   §3 SL4'-X).** The sl4p "what a proof needs" sentence — "monotonicity of
   `tau -> (M-1)/(2M)(log(1 + s/S) - s/(SM))`, `M = m sin(tau lam/2)`,
   `s = sin^2(tau lam/2)`, `S = sinh^2(lam/2)`, on `tau in [0.8, 1.074]`"
   — is character-for-character the function Theorem X.1 treats (the
   target's §1 blockquote reproduces it faithfully; I diffed by eye
   against the sl4p file itself). The target's clarification 1 is right:
   sl4p's "iff" should be "if" (sufficiency is what Corollary X.3
   delivers; necessity was never needed and is false in general for
   endpoint sums), and parking that with the §2c sl4p repair batch is the
   correct disposition. ✓
3. **Against the consumer CODE (`sl4p_nc1_ledger.py`, the interface that
   actually matters).** Read line-by-line: `w6_x(w, tau, m)` computes
   `(M-1)/(2M)(log(1+s/S) - s/(SM))` with `lam = w/m`, `t = tau lam`,
   guard-clipped; `X_w6` sets `tau0 = 2 asin(sinh(lam/2))/lam` (already
   divided by `lam` — the target says so, correctly), uniform `n = 60`,
   `h = (tau0 - 0.8)/n`, left endpoints `a = 0.8 + i h`, and accumulates
   `totn += h lam ((a+h) lam)^2 e^{-E}`, `totd += h lam e^{-E}` with
   `E = m * w6_x(w, a, m)` — EXACTLY the two sums displayed in Corollary
   X.3 (weight at the right endpoint `a+h`, exponential at the left
   endpoint `a`). The `mono` runtime flag compares successive `E`s at left
   endpoints; Theorem X.1 subsumes it (full-interval, not grid-point,
   monotonicity — which is what the integral bound actually needs, and
   which the runtime flag alone never certified). All W1 evaluations the
   ledger makes (blocks [1]–[4]: `w in [4.00, 4.60]` and `4.3`; referee
   probes to `w = 5.0`; `m` to 2000) lie inside the theorem's box `D`,
   including block [2]'s `w = 4.0` endpoint (covered because the theorem
   quantifies `w >= 4`, not just the band `(4, 5]`). ✓
4. **Against the [W.6] source (`wp1_draft_c.md` §5).** Clause W.6 reads
   `-log|phi_lam(t)| >= m ((M-1)/(2M))[log(1 + s/S) - s/(SM)]` for
   `lam != 0`, `t in (0, pi]`, `M > 1`, with `M := m sin(t/2)` (T.6(i)
   notation) and `1/r = s/S`, `S = sinh^2(lam/2)` — the target's §1
   provenance paragraph quotes it exactly, and Remark R3's `M > 1.539`
   confirms the W.6 applicability hypothesis `M > 1` on all of `D` (so
   the exponent the ledger certifies is the honest W.6 exponent, never
   the guard's flattened `0`). ✓ No circularity anywhere: the proof
   consumes NOTHING except elementary inequalities proved inline plus
   point evaluations of `log`/`arcsin`/`sinh` (NX-1..6); [W.6] enters as
   provenance only; no CL, no `r(k)`, no SL4' row, no harness number is
   used. The `m >= 561` threshold is only referenced, not touched — and
   the reference is consistent with STATUS_wave4 (`M_H = 560`, CL
   restated for `m >= M_H + 1 = 561`).

## 3. Independent verification (own implementation; the unprobed corner)

Script `referee_wave5_sl4px/ref_mw5x_verify.py` (dps 50; from-scratch
implementation — my `x` and my closed-form `dx/dtau` were written from the
target's DISPLAYS, not from either prover script; a bug in my own first
draft of `x` (a dropped factor of `h`) was caught precisely because the
closed-form derivative disagreed — after the fix everything agrees, which
is itself evidence the displayed algebra is the algebra being run). Key
verbatim output (`out_ref_mw5x_verify.txt`):

```
[V1] closed-form dx/dtau vs mp.diff (independent derivation check)
  V1: m=401.0 lam=0.0100998 tau=0.9: closed=0.158353599 vs diff=0.158353599, rel=2.11e-51 : True
  V1: m=4.494382 lam=0.89 tau=1.074: closed=0.1579927888 vs diff=0.1579927888, rel=2.11e-51 : True
[V2] EXTREME corner w=4, lam=0.89 (m=4/0.89=4.4944, unprobed by prover): full 4001-pt scan of [0.8, 1.074]
  V2: min dx/dtau=0.111843, min g=0.0871773, min x=0.0157617, min M=1.5664172 ... : True
  V2b: min over grid of [M - 1.9238 tau] = 0.000994342 > 0 : True
[V3] random-box scan of D: 3000 quasirandom (w, lam, tau), w in [4, 400], ...
  V3: violations = 0; min dx/dtau over sample = 0.154377 : True
[V4] Cor X.2: r(u) = arcsin(sinh u)/u on (0, 0.445] -- monotone? >1? max?
  V4: nondecreasing=True, min r=1.000000017 > 1, r(0.445)=1.07372378042 < 1.074 : True
[V5] Cor X.3 numeric: left-endpoint sums vs true integrals (n=60, three W1 points)
  V5: w=4.001: integral_n=1.0066112e-11 <= totn=1.1026295e-11; integral_d=1.5096746e-7 <= totd=1.6465281e-7 : True
[V7] hypothesis boundaries are REAL (out-of-domain sanity; record-only)
  V7a: w=1.6, m=401: M(0.8) = 0.63999973 < 1 (x-formula P<0: floor needed) : True
  V7b: w=4, m=5, tau in [4.5,6] (outside [0.8,1.074]): min dx/dtau = -0.13423 < 0 : True
OVERALL: PASS
```

Readings:

- **[V1]** my hand-derived `dx/dtau = [P'g + Pg'](lam/2)cos y` matches
  `mp.diff` of the raw formula to ~50 digits at four points including
  both extreme corners — the §2 product-rule algebra is exactly right.
  (My value `0.1262565634` at `(4.001, 462, 0.8)` also matches the
  prover's independently-computed block [B] `min dx/dtau = 0.126257` row.)
- **[V2]** the one corner of `D` the prover's 11-case block [B] does NOT
  contain — `w = 4` AND `lam = 0.89` simultaneously (`m = 4/0.89 =
  4.4944`, non-integer, allowed since the theorem only uses `m lam >= 4`)
  — is where `M` is smallest and `X` largest at once. Full 4001-point
  scan: strict monotonicity, `g > 0`, `x > 0`, `M > 1.53904` all hold;
  `g' > 0` at every grid point (loop aborts on first failure; none).
- **[V2b]** at that corner the per-tau floor `M >= 1.9238 tau` is
  VALID but nearly exact: minimum slack `9.9e-4` (at `tau = 1.074`;
  hand-check `M = 4.494382 * sin(0.47793) = 2.06719` vs floor
  `2.06616`). See finding m3 — the floor cannot be strengthened without
  redoing NX-1b, but nothing downstream needs it stronger (the X.b
  comparison `1.539 > 1.294` and the X.a threshold `> 1` both have wide
  margins).
- **[V3]** 3000-point quasirandom (Weyl-sequence) sweep of the FULL box
  `D` (`w` to 400, `lam` to 0.89, all `tau`): 0 violations of
  `dx/dtau > 0`, `g > 0`, `M > 1`.
- **[V4]/[V6]** Corollary X.2 and all NX constants re-derived
  independently (`r` nondecreasing on a 2000-point grid of `(0, 0.445]`,
  `min r = 1.000000017 > 1` at the small-`u` end — consistent with
  `r(0+) = 1`, approached from above as the corollary's `D(v) > 1`
  argument predicts; `r(0.445) = 1.07372378042`; every NX rounding
  re-verified in its safe direction: NX-1b/2/3a/3b round DOWN where used
  as floors, NX-5/6 round UP where used as caps).
- **[V5]** Corollary X.3's conclusion checked numerically against
  `mp.quad` at `n = 60` for `w = 4.001/4.05/5.0`, `m = 401`: the true
  integrals are `<=` the ledger's `totn`/`totd` sums, both lines (ratios
  ~1.10-1.15, i.e. the certificate has visible slack — the endpoint sum
  genuinely over-covers).
- **[V7]** record-only: the hypotheses do real work. At `w = 1.6` the
  `M > 1` region already fails inside `[0.8, 1.074]` (so SOME `w`-floor
  is genuinely needed for the theorem's shape), and far outside the `tau`
  interval (`tau ~ 4.5`, same `(m, lam)`) `dx/dtau` really does go
  negative — the theorem is not vacuously robust; its domain edges are
  meaningful.
- Separately: the prover's script re-run is **BYTE-IDENTICAL** to
  `out_x_constants_and_scan.txt` (diff empty, 1.1 s), and a mechanical
  check confirms every line of the note's §5 and §6 quoted blocks appears
  verbatim in the archived output. NX-1a's exactness claim verified:
  `Fraction(1074,1000) * Fraction(89,100) = 95586/100000` and
  `y0 = 47793/100000` exactly.

## 4. Findings (ranked; none moves a constant or the verdict of the theorem)

### m1 (the one repair consumers must see — scope the "certified upper bound" sentence)

Corollary X.3's closing sentence ("Consequently the W1 `X` row entry of
the sl4p ledger is a certified upper bound, no longer conditional on
SL4'-X") and §7's consumer item (a) ("...as a certified upper bound — its
`mono` flag is now a theorem") certify more than this note proves if read
quickly. What IS now certified end-to-end: (i) `|phi| <= e^{-m x}` on the
crossover zone ([W.6], PROVED, two-refereed wp1-c), and (ii)
`totn`/`totd` upper-bound the corresponding integrals (Corollary X.3,
this note). What is NOT yet refereed: the pricing that turns those
integrals into the row entry `X` (`Xn = A sqrt(2pi)/pi s2^{3/2} totn`
etc. — Lemmas SL4'.2/.4/.6 of `wave4_sl4p_20260812.md`, a file still at
MAJOR_ISSUES with NO maths referee). The note's own §7 dependency
paragraph states this debt honestly, so this is an internal wording
inconsistency, not a false claim — but interface fidelity is the
campaign's historical failure mode, and this sentence is the interface.
Repair: one clause in both places, e.g. "certified upper bound *on the
crossover integrals it sums* — the row's pricing normalization remains
part of the sl4p repair-and-referee cycle".

### m2 (trivia — notation collision in Corollary X.3's display)

The partition is written `0.8 = tau_0 < tau_1 < ... < tau_n =
tau_0(lam)/lam`: the symbol `tau_0` is both the first partition point
(`= 0.8`) and the crossover split (`tau_0(lam)`), in the same line.
Rename the partition points (`sigma_i`, or start the index at 1).

### m3 (record-only — the Lemma X.a floor is near-exact at the far corner; do not sharpen casually)

`M >= 1.9238 tau` has slack only `9.9e-4` in `M`-units (~0.05%) at the
full-domain corner `(w, lam, tau) = (4, 0.89, 1.074)` ([V2b]; the note's
§6 consistency note (i) reports the looser 2.2% at the OTHER corner
`(4.0, 5)`, `tau = 0.8`). The floor is valid — my scan proves the sign —
but any future consumer wanting `c > 1.9238` must redo NX-1b with a
higher-order sin bound; at `c`-level the constant is essentially spent.
Nothing downstream needs it stronger (X.b's comparison has 19% margin at
its binding point, X.a's `> 1` has 54%). Half a sentence would
future-proof it; no text forced.

### m4 (trivia — "six named-constant evaluations")

§0 and §5 say "six named-constant evaluations (NX-1..NX-6)"; the block
contains nine checks under six labels (NX-1a/1b/1c, NX-3a/3b). Cosmetic;
"six named constants (nine checks)" if anyone cares.

No other defect found. In particular I looked for and did NOT find:
hidden strictness failures (both X.c inclusions are strict, with the
strictness sources named); a `w = 4.0` vs `w > 4` boundary gap (the
theorem quantifies `w >= 4`, covering block [2]'s `w = 4.00` endpoint
evaluations); a `tau_0(lam)/lam > 1.074` escape for any in-scope `lam`
(Corollary X.2 is airtight and my V4 confirms the max at `0.89` with
`4e-4` to spare against `1.074`); an `arcsin` domain violation
(`sinh(0.445) < 1` proved by an honest elementary bound, not just
evaluated); a guard-clipping loophole in the consumer (`Remark R3` +
`M >= 1.539` closes it); or any use of `m` integrality, `m >= 401`, or
band membership beyond `w >= 4` (Remark R1's accounting is exact).

## 5. What survived adversarial attack (all clean)

1. **The whole §2 calculus chain, by hand** — substitution, product rule,
   the cubic sin floor, the `phi(X)` comparison, the `psi` chain with its
   endpoint-minimum argument, the quadratic-root placement — every step
   re-derived independently; no gaps, all strictness claims genuine.
2. **The strengthening is real**: strict increase, all `w >= 4`, all
   `lam in (0, 0.89]`, `m` non-integer allowed — verified on a 3000-point
   sweep of the full box plus a 4001-point scan of the worst corner the
   prover never probed. The recorded W1-only hypothesis is a small corner
   of what is now proved.
3. **Corollary X.3 is the right statement for the consumer**: it is
   partition-free (covers the ledger's 60, the numerics referee's 6000,
   and any future refinement), and its two displayed sums are
   character-faithful to `X_w6`'s accumulation lines. The upper-bound
   property holds numerically with ~10-15% visible slack at the probed
   W1 points.
4. **The NX table is honest**: all nine checks reproduce at dps 50 from
   my own evaluations; every rounding is in the direction the proof
   consumes; NX-1a is genuinely exact-rational; the only two constants
   whose tightness matters (`0.96193`, `1.9238`) are flagged accurately
   by the note's own consistency note (and see m3).
5. **The §6 record-only block is consistent** with the wave-4 numerics
   referee's [A2] audit: same 8 adversarial points, and the note's
   cross-scan increment arithmetic (`7.2e-3 / 4.1 = 1.75e-3` vs the
   referee's `>= 1.7e-3`) checks out (`401 * 1.78994e-5 = 7.178e-3`,
   cell-width ratio `1.37e-4/3.33e-5 = 4.11`).
6. **Process hygiene**: byte-identical re-run; quoted blocks verbatim;
   new files only (the wave4 script directory untouched); blind protocol
   respected on its face (files-read list is the permitted set);
   PROVED/flagged-class labels used honestly (this piece needs NO grid
   certificate, and says so).

## 6. Referee script table

| # | script (`g2_scripts/campaign_20260811/referee_maths_wave5_sl4px/`) | what it does | key output |
|---|---|---|---|
| R-V | `ref_mw5x_verify.py` (`out_ref_mw5x_verify.txt`) | from-scratch `x` + hand-derived closed-form `dx/dtau` vs `mp.diff` (V1); 4001-pt scan of the unprobed corner `(w, lam) = (4, 0.89)` incl. per-tau floor slack (V2/V2b); 3000-pt quasirandom sweep of the full box `D` (V3); Cor X.2 `r(u)` audit (V4); Cor X.3 sums-vs-`mp.quad` integrals at `n = 60` (V5); all NX constants re-derived (V6); out-of-domain reality checks (V7) | `OVERALL: PASS` — V1 rel err `~2e-51`; V2 `min dx/dtau = 0.111843 > 0`; V2b floor slack `9.9e-4`; V3 `0` violations; V4 `r(0.445) = 1.07372378042 < 1.074`; V5 integrals `<=` sums at all three points |

Also run: byte-identity re-run of the prover's
`wave5_sl4px/x_constants_and_scan.py` (diff empty) and a mechanical
verbatim check of the note's §5/§6 quoted blocks against
`out_x_constants_and_scan.txt` (every line present).

**Bottom line for the ledger.** SL4'-X: **CONJECTURED -> PROVED,
maths-referee MINOR_REPAIRS** (m1 one-clause scope fix before citation;
m2/m4 trivia; m3 record-only). Together with the numerics-referee-grade
evidence already on file (the wave-4 [A2] audits, now instances of a
theorem), the SL4' conditional surface reduces to SL1'-w + SL3'-w +
SL4'-E exactly as the note states; the sl4p §2c repair cycle and its
missing maths referee remain owed and are NOT discharged by this piece
(nor claimed to be).

*End of referee_maths_wave5_sl4px.md.*
