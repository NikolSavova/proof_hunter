# Adversarial NUMERICS referee report — `g2_draft_t2_20260803.md` (finalized 2026-08-05)

*Referee pass 2026-08-11. Scope per assignment: re-run all scripts under
`g2_scripts/t2/` plus `g2_scripts/t2_item1/`, `g2_scripts/t2_item4/`; verify every
quoted number in the draft against real output; re-implement float-dependent
certificates exactly where feasible; flag anything quoted-but-not-produced.
NOT in scope (per assignment): re-litigating the draft's own Section 8 open items 1–5,
which the draft honestly lists as open. Blind protocol maintained: no other file under
`g2_campaign_undefined/` was read; `g2_draft_t1` untouched.*

*Environment of this re-run: CPython 3.12.2, numpy 1.26.4, sympy, mpmath, macOS
(the draft quotes "CPython 3.14"; every deterministic figure nevertheless reproduced
to the printed digits — see D1 for the two roundoff-level exceptions).
Referee scripts (new files, saved and run):
`g2_campaign_undefined/referee_t2_scripts/ref_cert_dirichlet.py`,
`ref_misc_recheck.py`, `ref_kernel_smallu.py` (v1, superseded — see §5),
`ref_kernel_smallu2.py`.*

**VERDICT: MINOR_REPAIRS.**

The draft's numerics are genuine. All 12 scripts exist on disk, run to completion
(exit 0), self-report PASS, and their outputs match the draft's quoted figures to the
printed digits, with two roundoff-level exceptions and one slack-range misquote (both
in the conservative direction). No fabricated PASS was found — a sharp contrast with
the first-pass history the draft itself documents. The two grid-only Dirichlet
certificates were re-implemented at proof grade and hold (§3). The one substantive
finding is a false inequality display inside Theorem T.9's Step 2 supporting a
sub-claim the draft lists as "fully proved" (§4, F1); the sub-claim itself is
numerically true with a 3x margin, so this is a repair, not a retraction.

---

## 1. Script re-runs (all 2026-08-11)

| script | exit | self-verdict | draft §6 row reproduced? |
|---|---|---|---|
| `t2/t2_nc1_cumulants.py` | 0 | PASS | yes — max rel discrepancy **4.135e-45** (draft: 4.1e-45); untilted limits O(lam); tilt invariance exact at every k (m=12, θ=3/5) |
| `t2/t2_nc2_kernel.py` | 0 | PASS | yes — E(1)=.00400693, E(2)=.00358719, E(pi)=.00296038 identical; all 15 deficit rows identical to 6 digits; s2/λ at w=π = .7625/.7660/.7676 (draft: [.762,.768]) |
| `t2/t2_nc3_kappa34.py` | 0 | PASS | yes — ratios .9921/.9921/.5134/.6983/.8681, all identical |
| `t2/t2_nc4_varlower.py` | 0 | PASS | yes — 2015 vectors, min margin exactly 0; T.5 slack 2.6376 (m=30), 2.6455 (m=60) identical |
| `t2/t2_nc5_cf.py` | 0 | PASS | yes — (a) 1.03e-13; (T.6ii) .9999; (T.6iii) max .0167 (draft ".017"); first-pass cert FALSE at j=2,t=1/4 (0.015544 < 1/60); corrected cert min .012603 at j=2,t=.225; (T.7b) slack 28.8x–6650x (draft "29x–6600x") |
| `t2/t2_nc6_kernel_id.py` | 0 | PASS | mostly — rel dev max 7.4e-16 (consistent with draft "≤ 9.2e-16"); **imag parts up to 8.2e-19 vs draft "≤ 1.1e-19"** — see D1 |
| `t2/t2_nc7_flat.py` | 0 | PASS | yes — NC-9 reproduction .9648 .9647 .9646 .9631 .9615 .9669 .9677 identical; bands [.9617,.9648]/[.9711,.9734]/[.9768,.9786], widths .0031/.0023/.0018 identical |
| `t2/t2_nc8_refined.py` | 0 | PASS | yes — needed C_R = .343/.089/.022/.070 identical; resid/(B_m w²) = .007–.009 (draft "~.01") |
| `t2/t2_nc9_t9pp.py` | 0 | PASS | yes — (a) .9974 at (m,lam,r)=(10,.01,4); (b) .2121; (c) .3215 (draft .9974/.212/.322) |
| `t2/t2_nc10_far.py` | 0 | PASS | mostly — cert min .4150 at j=2,t=1.4 identical; counts OK; m_2 = 7338/66010/5076022 (draft 7.3e3/6.6e4/5.1e6) identical; **slack range 789x–4.25e7x vs draft's "24x–4e7x"** — see D2 |
| `t2_item1/diag1_deep_tilt.py` | 0 | (diagnostic) | yes — all three findings' tables identical to printed digits (e.g. \|phi(pi/m)\| rows .0347/.0388/.2325/.6207; worst ratio 1.925e+228 at t=1.87) |
| `t2_item4/t2i4_nc1_model.py` | 0 | PASS | yes — P_lam imag ≡ 0; untilted N(0) cross-check True; bare coeff −36/s2³; pointwise bucket 1.5491/4.0889/4.9126 (draft 1.55/4.09/4.91) |

Spot checks of in-text (non-§6) quotes, all confirmed against the same outputs:
T.3's spot row (N/2−mu = 7.847 in [7.105, 7.875] at m=30, w=0.3); §3's
sin²(1/8)=0.015544; §3's "NC-T10c measures max|phi| = 1.4e-8 at m=60, w=1 vs bound
0.61" (rerun: 1.447e-08 vs 0.6143); T.9 statement's "needed ≤ 0.35 for m ≤ 140"
(rerun max: 0.343); §7's flatness bands.

## 2. Deviations found in quoted output (both minor, both conservative)

**D1 — NC-T6 imaginary parts.** Draft §6: "imaginary parts <= 1.1e-19". Rerun:
1.5e-19 / 4.4e-19 / 8.2e-19 at k=12/20/28. These are attributable to
platform/numpy summation-order roundoff (the quantities are ~1e-19 against a pass
gate of 1e-12; rel-dev figures agree with the draft's "≤ 9.2e-16"). Not evidence of
fabrication — the same script produces the same qualitative machine-precision result —
but the specific figure does not reproduce on this machine.

**D2 — NC-T10(c) slack range.** Draft §6: "direct bound slack 24x-4e7x". Rerun from
the same script: slacks 789x / 8.06e3x / 5.0e5x / 4.25e7x — minimum 789x, not 24x.
The upper end matches; the "24x" lower end matches nothing in the current script's
output. Misquote in the conservative direction (the bound is safer than claimed).

## 3. Float-dependent certificates re-implemented (both upgraded to proof grade)

**(T.7b-cert) and (T.7c-cert)** — draft status: grid-certified, "Sturm-able on
demand". `ref_cert_dirichlet.py` replaces the grids by an analytic covering
argument, every ingredient verified at 50 digits:

- *Envelope:* sin(t/2) ≥ t/π on (0, π] gives 1−F_j² ≥ 1−π²/(jt)²; so jt ≥ 3.5 ⇒
  ≥ 0.19431 ≥ 1/80, and jt ≥ 3.9 ⇒ ≥ 0.35111 ≥ 0.35.
- *j-monotonicity:* at fixed c = jt, |F_j(c/j)| = sin(c/2)/(j sin(c/(2j))) and
  j sin(c/(2j)) is increasing in j (kernel sin u − u cos u > 0 on (0, π), since its
  derivative is u sin u > 0), so the minimum over j ≥ 2 on each fixed-c slice is at
  j = 2, where 1−F_2² = sin²(c/4).
- *Endpoints:* sin²(0.1125) = 0.0126029... ≥ 1/80 (margin 1.03e-4);
  sin²(0.7) = 0.4150164... ≥ 0.35 (margin 0.065).

These three cover the full regions {j ≥ 2, jt ≥ 0.45, |t| ≤ π} resp. {jt ≥ 2.8}.
A 10x-density rescan of the danger zones reconfirms the draft's minima exactly
(0.012603 at j=2, t=0.225; 0.415016 at j=2, t=1.4). **Both certificates hold; the
"Sturm on demand" caveat in §8 item 3 can be retired for these two.**

**T.4' pointwise kernel bounds** (|g''−u/120| ≤ u³/1500, |g'''−1/120| ≤ u²/500 —
grid-certified at ratio 0.9921, "tight but true"). `ref_kernel_smallu2.py`: the
Bernoulli tails of both series are alternating with consecutive-term ratios ≤ 0.518
(g'') and ≤ 0.864 (g''') at u = π (max over the whole tail, computed to n = 45), so
the alternating remainder bound gives exactly |g''−u/120| ≤ u³/1512 and
|g'''−1/120| ≤ u²/504 on (0, π], i.e. ratios ≤ 1500/1512 = 500/504 = 0.992063 < 1.
The draft's measured 0.9921 is precisely this u→0 limit — **the bounds are now
analytic, not grid-only.** (Corroborating 60-dps grid on [0.1, π]: max ratios
0.99154/0.99120 at u = 0.1.)

**Wrong-sign reproduction (T.6iii).** The draft asserts the first-pass sign fails "with
ratio up to 6.4" but the saved script only tests the corrected sign.
`ref_misc_recheck.py`(c) reproduces the failure: wrong-sign max ratio 5.86 at m=30
(order consistent with 6.4, which presumably included other (m,w)). The sign story
checks out.

**T.9''a adversarial extension.** The saved script stops at r = 10, lam = 3; the lemma
claims all real lam, all r ≥ 3. Extended to r = 11..14, lam ∈ {5, 10} (60-digit
Decimal): max ratio ≈ 0 (large tilt kills the cumulants). No issue.

## 4. Findings (ranked)

**F1 (moderate — the only substantive one). Theorem T.9 Step 2's chain for
"B_lam = B_m(1 + θ·0.35 w²)" is broken; the sub-claim is listed under §5's
"load-bearing pieces fully proved here" but is not proved by the displayed chain.**
The display "(1−delta)^{−2} <= 1 + 2.1 delta for delta <= 0.35" is false for every
delta ≥ ~0.025 (at delta=0.033: 1.06942 > 1.06930; at delta=0.1: 1.2346 > 1.21; at
delta=0.35: 2.367 > 1.735 — `ref_misc_recheck.py`(d)). Repairing the chain
multiplicatively with the draft's own delta-bound gives |B_lam/B_m − 1| ≤ 0.3587 w²
at w = 1 (already above the claimed 0.35) and ≤ 1.198 w² at w = π (far above).
The TRUTH, measured from the exact closed-form cumulants (60-digit Decimal, w-grid to
π, m ∈ {30, 120}): max |B_lam/B_m − 1|/w² = **0.1134** — comfortably inside 0.35. So
the sub-claim is numerically true with 3x margin, and the downstream envelope
c_w = 1/2 survives (NC-T8 measures the true w²-coefficient at ~0.01·B_m, 50x
headroom), but the constant 0.35 currently has no valid derivation, and any chain of
this multiplicative shape fails for w near π. Repair options: restate for |w| ≤ 1
with a corrected inequality ((1−d)^{−2} ≤ 1 + 2d + 3.5d² for d ≤ 0.4 suffices there,
giving ≈ 0.36 w²), or re-derive the w ≤ π range from the exact deficit identity.
Since T.9 is stamped PARTIAL anyway, this is a repair to §5's "fully proved" list,
not a status change of the theorem.

**F2 (minor). (T.9''c)'s constant is rounded in the unsafe direction.** The chain
2.02·zeta(4)/(20·(2π)⁴)/0.2686 evaluates to **2.6113e-4**, slightly above the
displayed 2.61e-4; the intermediate "1/1.063e7" likewise (actual 1/1.0629e7). The
final (T.9''b) denominator 2.8e6 IS safe (actual 2.855e6). Statement (c) as written
remains true with 3x numeric slack (NC-T9c ratio 0.322); fix: print 2.62e-4.

**F3 (minor, quoted-but-not-produced). T.8-final's "(numerically (V) then holds for
m >~ 2.5e5)".** No script computes this. Recomputation (`ref_misc_recheck.py`(e)):
(V) first holds at m ≈ **2.96e5** in the most favorable case (s2 = C_0 = 2000) and at
m ≈ **1.07e6** at s2 = lambda. The "2.5e5" figure is not reproducible under any
reading tried; since (V) is an explicit hypothesis of the honestly-scoped T.8-final,
this only mis-sizes an admitted restriction.

**F4 (minor). §6 NC-T10 row slack misquote** — see D2 above.

**F5 (minor). T.9'' step-2 side condition "m <= 0.01(m+1)^{r+1}/(r+1) for r >= 3,
m >= 4" is false at (m,r) = (4,3) and (5,3)** (0.01·5⁴/4 = 1.56 < 4; 3.24 < 5).
True from m = 6 at r = 3 and everywhere in the lemma's actual scope m ≥ 30. Fix the
parenthetical to m ≥ 6.

**F6 (minor). T.4's crude clause "deficit <= w²/20 (all m >= 2)": the displayed
chain proves it only for m ≥ 3.** The chain needs S_4/(m² lambda) ≤ 12; the value at
m = 2 is 17.00 (m=3: 11.88 ✓). Direct check at m = 2, w = π: deficit = 0.4301 ≤
π²/20 = 0.4935 — the clause is TRUE at m = 2, the chain just doesn't reach it.
Nothing downstream uses m = 2 (T.10 needs m ≥ 53).

**F7 (minor). T.4 lower-bound intermediate step drops a term.** "≥ (lam²/240)
S*_4 (1−w²/19)" does not follow from the preceding line: S_4(1−x) − m =
(S_4−m)(1−x) − mx, so a −(lam²/240)·m w²/19 term is discarded without comment. Its
relative size is ≤ 5w²/(19 m⁴) ≤ 3.3e-6 at m ≥ 30, absorbed by the 0.02857→0.0285
rounding slack; the final (T.4) is verified two-sided at all 15 (m,w) points. Display
fix only.

**F8 (minor typos).** (i) T.4' proof text prints the g'' series as
"u/120 − u³/1512 + u⁵/43200 − ...": the true fifth-order coefficient is **1/28800**
(`ref_misc_recheck.py`(b): series limit 3.4722e-5 = 1/28800; the item-4 script's
`g2()` already uses 28800). (ii) Step 0's "E U² = 6.31" at lam = 1/2: actual
q(1+q)/(1−q)² = **6.294**; forcing threshold 2000/6.294 = 317.8, so "for m <= 316,
s2 >= 2000 forces lam < 1/2" remains true a fortiori. (iii) `t2_nc5_cf.py`'s
docstring says sin²(1/8) = 0.015549; true value 0.015544 (draft text has it right).

**F9 (observation). T.6(iii-final)'s proof display is loose** ("constant 1/24 → 1/6
to be safe", unverified "|z| ≤ 0.19" chain). The constant carries 60x measured
headroom (NC-T5c max ratio 0.017), so the statement is safe, but of the items stamped
PROVED this one has the least rigorous displayed derivation.

**Confirmed non-issues** (checked because they looked wrong at first glance):
§4's "b2 ≤ 27/m for s2 ≥ lambda/2" holds with the exact lambda (m·b2 = 26.16/25.39/24.86
at m = 30/50/100); T.10's overlap statement is correct under its stated
hypothesis-sets reading; T.9''(b)'s displayed constants 1/1.063e7 → 1/2.8e6 chain is
arithmetically right (0.7308 ≤ 0.7314 term ratio at m = 30; final constant safe);
the kappa_3² dimensional constant "4.6" is 4.628 ✓; NC-T8's `nan` column at K=1 is
just an empty |w| ≥ 2 subset, not a bug.

## 5. Referee-side errata (for the record, per honesty rules)

My first two attempts at re-checking the T.4' kernel bounds contained bugs of my own:
`ref_misc_recheck.py` item (a) evaluated the g''/g''' closed forms at u ~ 1e-4 with
30 dps, where catastrophic cancellation (≈25 digits) produced spurious ratios up to
1.079 — NOT a real violation; and `ref_kernel_smallu.py` (v1) had a sign error in its
series spot-evaluation and compared the g''' tail against the constant term in its
ratio audit. Both are superseded by `ref_kernel_smallu2.py`, whose analytic
alternating-series argument closes the question (§3). The draft's own grid (starting
at u = π/300) never entered the unstable zone; its 0.9921 figure is correct.

## 6. What remains

1. The draft's §8 items 1–5 (deep-tilt far region; region-2 handoff constants;
   T.9's bucket-table assembly incl. C_R(K) and T.8's C = 600; the far-exponent
   thresholds m_2(K)) — all honestly declared open there, all confirmed still open
   here; not re-litigated per assignment. The `g2_item1` diagnostic's negative
   findings were reproduced exactly.
2. **F1's repair**: a valid derivation of the "0.35 w²" (or a restated small-w
   version) for B_lam/B_m, before §5's "fully proved" list can stand as written.
3. The cosmetic fixes F2–F8 (constants re-rounded the safe way, two scope
   parentheticals, three typos, two §6 quote corrections).
4. Now DISCHARGED relative to the draft's own ledger: (T.7b-cert)/(T.7c-cert) and
   the T.4' kernel bounds no longer need Sturm certificates — analytic arguments are
   in §3's referee scripts and can be transcribed into the draft.
5. Everything in this report derives from saved, run scripts: the 12 originals plus
   `referee_t2_scripts/ref_cert_dirichlet.py`, `ref_misc_recheck.py`,
   `ref_kernel_smallu2.py` (and the superseded `ref_kernel_smallu.py`, kept for the
   audit trail). Raw outputs quoted above are from the 2026-08-11 runs.

**Verdict: MINOR_REPAIRS** — every PROVED-stamped numeric claim reproduces; the two
formerly grid-only certificates now hold at proof grade; one derivation chain inside
T.9 (F1) and a handful of display-level constants need repair; nothing found that
changes any theorem's stated status.

*End of report.*
