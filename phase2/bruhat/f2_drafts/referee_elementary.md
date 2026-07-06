# Referee report — `draft_elementary.md` (F2, elementary/exact-recurrence route)

Referee protocol: every NUMERIC CHECK line was independently re-implemented and run against
`mahonian.py`'s exact arithmetic (extended to `m = 45` where the draft requires it); each lemma
was attacked for hidden hypotheses, circularity, and constant errors. Honest `GAP` markers are
noted but not counted as flaws; **unmarked** defects are. Verification scripts: referee's own
(scratchpad `ref_checks.py`, `ref_attack.py`, `ref_attack2.py`, plus one exact integer
counterexample inline); all numeric claims below were reproduced by the referee, not taken from
the draft.

**Verdict: MAJOR GAPS — one central statement (Theorem 4.2) is FALSE as written (referee
counterexample, exact arithmetic), and two of the draft's own numeric-check claims fail as
stated. The exact-identity layer (§1–§2), the finite verification, and the spec correction
`c = 187/216` are correct and valuable. Parts (a) and (c) are NOT established (they rest on the
false-as-stated Theorem 4.2 plus one unmarked circular dependency); part (b) is established only
for `m ≤ 40` (the draft says so honestly).**

---

## 1. Numeric-check ledger (referee runs)

| Check | Claim | Referee result |
|---|---|---|
| N1 | argmin central, min = central ratio (m ≥ 5), varfit table, `σ²c₄₀ = 0.97337` | **PASS** (referee gets 0.973381; argmin = ⌊N/2⌋ also verified for 41 ≤ m ≤ 45) |
| N2 (Lem 2.1) | `T(k) = P·E(k)+X(k)` exact, m = 5..12, all k | **PASS** (exact integers) |
| N3 (Lem 2.2) | identity (2.2) + every `β_t, γ_t ≥ 0`, m = 5..12 | **PASS** (exact integers) |
| N4 (Lem 3.3) | triangular identity (3.2), m=12, W=8; varfit ≤ 1 for m ≤ 40 | **PASS** (referee checked (3.2) as an *exact rational* product identity, stronger than "machine precision") |
| N5.1 | Gaussian one-step `excess/(cm⁴) ∈ [0.0042, 0.0055]`, drift → 1/240 | **PASS** (referee range [0.00424, 0.00550] over m ∈ {8..40}, mult ∈ {½,1,2}) |
| N5.2 | `ε_m > 0` for 5 ≤ m ≤ 45; `ε_m/m ∈ [0.038, 0.084]` → 0.061 | **PASS** (referee: [0.0381, 0.0839], ε₄₅/45 = 0.0608) |
| N6 | Gaussian window minimum `1/F − 1/c = 9.96 / 36.45`; **4000 random admissible profiles: none beats Gaussian** | numbers **PASS** (referee: 9.957, 36.452, with `c = e^{c̃}−1`); the "none beats" claim **FAILS** — see Finding F3 (17/4000 violators at m=10 under honest sampling of the *stated* constraint set; 0/4000 only after restricting to balanced windows) |
| N7 (Lem 1.2) | `κ₄(U_n) = −(n⁴−1)/120` exact n ≤ 11; varfit vs `1+κ₄/2σ⁴` quotes | **PASS** (exact; 0.9047/0.8920, 0.9481/0.9466, 0.9648/0.9644, 0.9734/0.9732 all reproduced) |
| N8 | central-window balance 0.81 (m=20), 0.90 (m=40) | **PASS** (0.812, 0.897) |
| N9 (Cor 5.2) | `r₅−1 = 21/100`, product `7/8`; `r₆−1 = 11/90`, product `187/216 < 7/8`; min over 5..40 = 187/216; strictly increasing 6..40 | **PASS** (all exact rationals confirmed; **the spec-correction is right** — the spec's "σ²(r_m−1) increasing" is false at m=5→6: 0.8750 → 0.86574) |
| N10 (part b) | argmin = ⌊N/2⌋ exactly, m ≤ 40; profile `g_m` **strictly increasing** in x ≥ 0, "zero non-monotone steps" | argmin **PASS**; zero strict *decreases* **PASS**; but "strictly increasing" is **false as stated** — see F8 (one forced *tie* `g(mid)=g(mid+1)` whenever N is odd; 18 of the 36 values of m) |
| N10b (Prop 7.1) | quadratic-rise coeff `∈ [1.08, 1.25]` for x ∈ [m,3m], m ∈ {20,40} | **FAIL at m=20** — see F9 (referee range [1.117, **2.239**]; only m=40 gives [1.078, 1.245]) |
| unnumbered §4.2(ii) | `min_k m·g_a(k)/D_k ∈ [0.16, 0.35]` for 8 ≤ m ≤ 40 | **PASS** ([0.162, 0.349]) |
| Lem 6.1 | integral representation (6.1) | **PASS** (spot-check m=6: integral reproduces a₆(3)=29, a₆(7)=101 to 6 decimals) |

Score: 16 distinct check items run; **2 fail as stated** (N6 "none beats", N10b coefficient range
at m=20), 1 further has a wording error (N10 "strictly increasing"). Every *quoted number* in
the draft that the referee recomputed was accurate — the failures are in the *claimed ranges /
universality*, not fabricated data.

---

## 2. MAJOR FINDINGS

### F1 (MAJOR, unmarked): Theorem 4.2 is FALSE as stated — not merely unproven

The theorem asserts: absolute constants `δ₀ ≥ 1, A₀` exist such that log-concave `b` with
contiguous support satisfying `(H_c)` with `cm² ≤ δ₀` yields `1/c' ≤ 1/c + (m²−1)/12 + A₀cm⁴`.
This is false under **both** readings of the hypothesis:

* **Literal reading** (`(H_c)` holds for the stated `c`; note `(H_c)` *weakens* as `c` decreases,
  so any log-concave `b` qualifies with `c` small): take `b = I₆` (Mahonian m=6, support width
  16, log-concave), `m = 18`, `c = 0.9/18²` (so `cm² = 0.9 ≤ δ₀`). Exact integer computation:
  `a = b * u₁₈` has `a(15..17) = 720, 720, 720` and `T(16) = 0`, i.e. `r_a(16) = 1` **exactly**,
  `c' = 0`, `1/c' = ∞`. (Mechanism: when `supp b` fits strictly inside the convolution window,
  Lemma 2.1's four edge values vanish, so the defect is exactly zero — the convolution has a flat
  plateau.) This defeats (4.2) for *every* `δ₀, A₀`.
* **Strict reading** (`c` = the exact minimal curvature of `b`): referee built smooth `b` with
  curvature exactly `c̃ = 0.9/m²` in the tails (so min curvature = `c̃`, `cm² = 0.9`) and a sharp
  interior peak (curvature `K` on `|j| ≤ 3`). Measured at m=10: `c' = 5.0e−3, 1.3e−4, 6.3e−8,
  2.6e−11` for `K = 0.5, 1, 2, 3` — while (4.2) with the draft's "safe" `A₀ = 1/60` demands
  `c' ≥ 8.3e−3`, and even `A₀ = 1000` demands `c' ≥ 1.1e−5`. As `K → ∞` at fixed `(m, c̃)`,
  `c' → 0`, so **no** absolute constants can exist. Same at m=20 (violated already at K=0.5).

Consequence: Theorem 5.1, Corollary 5.2 (m > 40), and Corollary 5.3 are "conditional on
Theorem 4.2" — i.e., conditional on a **false** statement. The lemma needs an additional
anti-concentration hypothesis on `b` (e.g. a curvature *upper* bound `O(1/m²)` on a central
region, or `Var(b) ≥ C m²`, or "the minimizing window is balanced"), which the Mahonian family
does satisfy — but then that hypothesis must be *carried through the induction* of §5 (proved
for `a_m` from properties of `a_{m−1}`), which the draft does not do or mention. GAP 1/GAP 2
mark the *proof* as missing; they do not disclose that the *statement* is false, so this is an
unmarked flaw. The failing step, quoted: "if `b` is log-concave with contiguous support and
satisfies (H_c) with `cm² ≤ δ₀`, then `a = b*u_m` … satisfies (H_{c'}) and (4.2)."

### F2 (MAJOR, unmarked): the §4.2(ii) "steep windows" sub-claim is false

Quoted: "*steep windows* (`|slope|·m ≥ Θ`): … the mediant inequality … plus (H_c) pushes the
curvature of `a` up to `≥ c̃(1 − O(e^{−Θ}))` — far above `c'`. Provable by the same boundary
formula; constants not finalized." The F1 counterexamples live exactly in this regime (window
slopes ≫ Θ/m) and have output curvature `≈ 0 ≪ c̃`, so the claim is not "provable with
constants not finalized" — it is **false** as formulated. (The mediant inequality bounds the
*slope* of `a` between the extreme slopes of `b`; it says nothing that prevents the *curvature*
of `a` from collapsing on a plateau.) GAP 2 honestly flags the seam as unwritten, but asserts
the sub-regime statements are established-modulo-constants; they are not.

### F3 (MODERATE, unmarked): GAP 1's extremality claim is false as phrased; N6 is a sampling artifact

GAP 1 states the conjecture as: "the minimum of `T(k)/(a(k−1)a(k+1))` over **all** `q`
satisfying the curvature constraints is attained on the exactly-`c̃`-curved family." False:
referee sampling of the stated constraint set (`γ_s ≥ c̃`, random centerings) found **17/4000
profiles strictly below the Gaussian minimum at m=10** (worst `F = 0.0164` vs Gaussian
`0.0269`); all violators are steep/peaked windows (`max|λ| ≥ 1.17 ≈ 12/m`, gaps up to 20×`c̃`).
The draft's N6 "none beats the Gaussian minimum" holds only because its sampler evidently never
left the balanced regime. The referee confirms the *balanced* version is numerically solid:
restricting to `max_t |λ_t| ≤ 1.5 ×` the Gaussian's own maximal window slope, 0/4000 violators
at m ∈ {10, 20} and the Gaussian is the exact worst case. So the correct conjecture must carry
the balance restriction explicitly; as written both GAP 1's statement and NUMERIC CHECK N6's
universality claim are wrong.

### F4 (MODERATE, unmarked): hidden dependency in Corollary 5.2's "sharp constants" path

The chain "`A₀ = 1/240` ⇒ `A₁ ≈ 0.15–0.2` ⇒ `K ≤ 3.6` ⇒ (5.2) closes for m ≥ 41
**conditionally on GAP 1–2**" uses `A₁ = 36A₀(1+5/m)`, which per Theorem 5.1's own parenthesis
requires the *empirical* bound `c_{m−1}σ_{m−1}² ≤ 1` — exact only for `m−1 ≤ 40`. For
`m−1 > 40` inside the induction, the induction hypothesis (5.1) provides only a **lower** bound
on `c_m` (upper on `1/c_m`); the needed **upper** bound `c_mσ² ≤ 1` is exactly the unproven
direction (it would follow from Prop 6.2, i.e. GAP 3, since `c_m ≤ r_m(mid)−1`). So the honest
conditionality of the sharp-constant route is **GAP 1–2 AND GAP 3**, not "GAP 1–2" as stated in
§5 and in the §8.1 ledger. (The proven-only route `A₁ = 3, K = 54` avoids this but, as the
draft does admit, leaves `41 ≤ m ≤ 348` to an unperformed finite verification.)

### F5 (MODERATE, unmarked): regime certification fails at the induction's base

Theorem 4.2's "safe target" is stated for `cm² ≤ 13`. Feeding the only *proven* upper bound
(Lemma 3.3: `c_{m−1} ≤ 18/σ_{m−1}²`) gives `c_{m−1}m² = 18m²/σ_{m−1}² = 16.4` at `m = 41`,
and `> 13` for all `41 ≤ m ≤ 51` (referee computation; first OK at m = 52). So even granting
Theorem 4.2 (repaired), the induction as launched from `m₀ = 40` invokes it outside its own
declared regime for the first 11 steps; one needs `m₀ ≈ 52` plus exact verification of
41–51 (easy, but neither done nor acknowledged).

---

## 3. Minor findings

### F6 (minor): Lemma 3.3's final constant is wrong on part of its stated range
The proof derives `min g ≤ 17/σ²` and concludes `c_m = e^{min g} − 1 ≤ 18/σ²` "for m ≥ 12".
Referee: `e^{17/σ²} − 1 > 18/σ²` for **m = 12..17** (e.g. m=12: 0.3768 vs 0.3386), so the
final step is unjustified there; it holds from m = 18. (The *statement* is true for 12 ≤ m ≤ 40
by the harness, and the lemma is only consumed at m > 40, so this is repairable by citing the
harness for m ≤ 40 — but as written the constant chain is broken, and this is arithmetic, not
the "lattice slop" that GAP 6 discloses.) Similarly the interpolated display (3.1)
`c_m ≤ min g·(1+c_m/2)` needs `c_m ≤ 2/17`, again false for small m in the stated range.

### F7 (minor): two broken steps inside Lemma 3.1's proof
(i) "`(2s*+1)M/e ≥ 0.67wM` for `w ≥ 5`" fails at w = 5: `9/e = 3.311 < 3.35`. (ii) The
exclusion "(If `w ≤ 4` then `σ²S ≤ 11M·125` forces σ bounded, excluded for `m ≥ 12`)" is a
non sequitur: with `M ≤ S` it forces only `σ² ≤ 1375`, which excludes nothing until `m ≥ 37`
(σ²₃₆ = 1347.5 < 1375 < σ²₃₇). As written the proof of `S ≥ Mσ/6` is incomplete for
12 ≤ m ≤ 36. The statement itself is comfortably true (referee: `min_{12≤m≤45} S/(Mσ) = 2.52`),
and it is consumed only at m > 40, but the stated range is not delivered by the stated proof.
GAP 6 ("routine lattice slops") does not cover (ii), which is a wrong deduction.

### F8 (minor): part (b) "strictly increasing … zero non-monotone steps" is overstated
For N odd, symmetry forces `r(⌊N/2⌋) = r(⌈N/2⌉)` exactly, i.e. one *flat* step at the center.
Referee: exactly one tie for each of the 18 values `m ∈ {6,7,10,11,…,39}` (N odd), zero strict
decreases anywhere for 5 ≤ m ≤ 40. "Strictly increasing in x ≥ 0" is therefore false as
stated; correct is "non-decreasing, strictly increasing after the forced central tie."

### F9 (numeric-check failure): Prop 7.1's quadratic-coefficient window claim is wrong at m=20
Claimed: `(g(mid+x)/g(mid) − 1)·m·(σ/x)² ∈ [1.08, 1.25]` for `x ∈ [m, 3m]`, `m ∈ {20, 40}`.
Referee at m=20: values 1.117 (x=20), 1.222 (x=30), 1.400 (x=40), 1.701 (x=50), **2.239**
(x=60). The claim holds only for m=40 ([1.078, 1.245]) — at m=20, `3m ≈ 3.9σ` is far outside
the quadratic regime. This does not kill Prop 7.1 (asymptotic, and itself GAP-4-flagged), but a
NUMERIC CHECK line that "passes" per the draft in fact fails on half its stated range.

### F10 (minor, inside a GAP-3-flagged sketch, but qualitatively wrong): the tail bound in Prop 6.2 cannot deliver its stated conclusion
Quoted: "The tail `t ∈ [t₀, π]` is negligible: `|F_m(t)| ≤ exp(−t²/24·Σ_{j≤π/t} j²)` gives
superpolynomially small contributions." For `t` of order 1 the displayed bound is `O(1)`, not
small: at t = 1 it gives `exp(−14/24) = e^{−0.58}`; at t = 2, `e^{−1/6}`. It is effective only
for `t ≲ const`. The regime `t ∈ [const, π]` (where `|F_m|` *is* genuinely tiny, via
`Π_j |sin(jt/2)|/(j sin(t/2)) ≲ (C/t)^m/m!`) needs a separate standard estimate that the draft
does not state. GAP 3 is scoped as "explicit remainder constants"; this hole is structural, not
a constant. Repair is easy, but as written the tail argument does not prove negligibility.

### F11 (observation): the CJZ transfer is asserted, not justified
The spec warns CJZ Thm 4.6/eq. (4.11) is proved for the **central Gaussian binomial** only.
The draft's transfer sentence is: "their §4 estimates apply verbatim to `F_m` since `F_m` is a
product of the same Dirichlet-kernel factors." No verification is given that the estimates are
factor-count-uniform in the way needed (the q-factorial has m distinct factors
`sin(jt/2)/(j sin(t/2))`, j = 1..m, vs the binomial's structure; the tail behavior near t ≈ π
differs — cf. F10). Since the entire upper half of part (a) routes through this sentence, and
GAP 3 as declared covers only "remainder constants," the transfer justification itself is an
undeclared gap. (The referee agrees the statement is *true* — the two-term prediction matches
the harness to 3–4 decimals — but true-and-unproven is precisely what needs marking.)

---

## 4. What is solid (verified positively)

* **Lemma 1.1, Lemma 1.2** — exact; referee verified `κ₄(U_n) = −(n⁴−1)/120` in rationals and
  re-derived (1.2), (1.4) by hand ((1.4)'s 27/25 constant checks: `648/600 = 27/25`).
* **Lemma 2.1, Lemma 2.2** — both identities verified as exact integer identities for all k,
  5 ≤ m ≤ 12, with all `β_t, γ_t ≥ 0`; referee re-derived both proofs symbolically. These, plus
  Lemma 2.3 (algebra re-checked; equality on the quadratic family confirmed), are genuinely
  nice, correct, reusable tools — the strongest part of the draft.
* **The spec correction (§5.3)** — fully correct and exact: `σ₅²(r₅−1) = 7/8`,
  `σ₆²(r₆−1) = 187/216 < 7/8`; the sharp uniform constant for part (c) on 5 ≤ m ≤ 40 is
  `187/216`, attained at m = 6, and `σ²(r_m−1)` is strictly increasing only from m = 6. Any
  competing draft that "proves" `c = 7/8` for all m ≥ 5 is wrong.
* **Theorem 5.1's bookkeeping** — the exact identity `σ_m²/m − σ_{m−1}²/(m−1) = (4m+1)/72`, the
  `K = 18A₁` closure, and the base case (`K ≥ 1.094` needed; referee confirms) are all correct
  *given* a repaired one-step lemma.
* **§4.1's sharp-law identification** — the three-way numeric confirmation is real and referee-
  reproduced, including `ε_m > 0` for all 5 ≤ m ≤ 45 (so the naive harmonic induction is indeed
  impossible, an important structural fact) and the `1/240` excess constant.
* **Prop 6.2's central algebra** — the N-even and N-odd ratio-to-second-difference reductions
  are correct (referee re-derived), and (6.1) is numerically exact.

---

## 5. Are (a), (b), (c) actually established?

* **(a)**: No. Upper half: correct-looking sketch, but rests on F10/F11 plus GAP 3 (marked).
  Lower half: rests on Theorem 4.2, which is false as stated (F1) — the conditional structure
  survives only after the lemma is reformulated with a width hypothesis and the induction is
  amended to propagate it. Status honestly summarized by the draft *except* for F1/F2.
* **(b)**: Established exactly for 5 ≤ m ≤ 40 only (referee reconfirmed, and extended: argmin
  = ⌊N/2⌋ also at 41 ≤ m ≤ 45). For m > 40 the draft openly says OPEN (GAP 5) — honest, not a
  hidden flaw; but note the spec asked for a proof, so F2's target (b) is simply not met. The
  "strictly increasing profile" claim needs the F8 correction.
* **(c)**: The finite part (5 ≤ m ≤ 40, constant 187/216) is exact and correct, and the spec
  correction is a real contribution. For m > 40 the claim is conditional on the false-as-stated
  Theorem 4.2 (F1), with the additional undisclosed dependencies F4 (GAP 3 for sharp constants)
  and F5 (regime start), and the acknowledged 41–348 verification hole on the proven-constants
  route. Not established.

## 6. Summary for the editors

The draft's empirical program and exact-identity toolkit are excellent, its numbers are honest
(every quoted figure reproduced), and its GAP registry is mostly candid. But the load-bearing
one-step lemma is false as stated (exact counterexample: `I₆ * u₁₈` has a flat plateau,
`r = 1`), its unbalanced-window repair plan asserts a false sub-claim, and two NUMERIC CHECK
lines fail on part of their stated ranges. The correct headline for this draft is: *parts
(a)/(c) reduced to a plausible but currently false-as-formulated convolution lemma that must be
restated with an anti-concentration hypothesis and re-fed through the induction; part (b) open
beyond m = 40; sharp constant for (c) corrected to 187/216.*
