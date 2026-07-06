# Referee report — draft_pro.md (F2, blind draft by gpt-5.5-pro)

Referee: adversarial pass, Claude (Fable 5). Every NUMERIC CHECK line was run against
`mahonian.py` (exact integer/Fraction arithmetic, extended to m=100/120 where useful);
each lemma was attacked for hidden assumptions, circularity, wrong constants, and
illegal o(1) work. Honest `GAP:` markers are noted but not counted as flaws;
**unmarked** gaps are counted.

## Verdict

**Major gaps — theorem not proven, but the architecture is sound and no numeric claim
is wrong.** All 8 NUMERIC CHECK lines pass. Lemmas 1, 2, 5 are complete and correct
(Lemma 5 is genuinely nice). The draft is honest about three gaps (6.1, 7.1, 8.1),
but it contains **two unmarked defects in load-bearing steps** (Lemma 3 eq. (3.2);
Lemma 6's log-B uniformity claim, which is demonstrably FALSE in the tail) and **one
unmarked logic gap** (the intermediate regime of Lemma 7 / part (b)). Part (a) is
"complete modulo GAP 6.1" only if one also grants the unproven (3.2). Part (b) is
not established. Part (c) is honestly declared not achieved, and the draft correctly
falsifies the spec's own suggested constant c = 7/8 (fails at m=6) — a real catch.

---

## 1. Numeric checks (8 run, 0 failed)

| # | Where | Check | Result |
|---|-------|-------|--------|
| 1 | Lemma 1 | all r_m(k) >= 1; `central?` = YES for m=4..40 | **PASS** (verified to m=100; strict log-concavity in the interior also confirmed) |
| 2 | Lemma 2 | sigma^2(m=5) = 25/6, sigma^2(m=6) = 85/12 | **PASS**; bonus: the kappa_4 closed form -m(6m^4+15m^3+10m^2-31)/3600 matches the direct sum exactly for m = 2, 5, 10, 40, 100 |
| 3 | Lemma 3 | E_m(2)/sigma^{-2} -> 0; m^5 E_m(2) bounded | **PASS**: E/sigma^{-2} = 0.111, 0.020, 0.0047, 0.0020 at m = 10, 20, 40, 60; m^5 E_m(2) = 354, 272, 259, 257 (bounded, slowly drifting down) |
| 4 | Lemma 4 | `rc-1` agrees with 1/sigma^2 to relative error O(1/m); varfit -> 1, ~0.9734 at m=40 | **PASS**: varfit(40) = 0.973381; m·(1 - varfit) = 0.953, 1.038, 1.065, 1.075 at m = 10, 20, 40, 100 — consistent with the claimed limit 27/25 = 1.08 in (4.3) |
| 5 | Lemma 5 | B_m(t)/sigma^2 < 1 for t > 0, max at t = 0 | **PASS** on t in (0, 10/m] (2000 pts) and (0, 5] for m = 10, 40; sup = 0.999999 attained only as t -> 0 |
| 6 | Lemma 6 | min attained centrally, no tail competitor; min_k sigma^2 D_m(k) -> 1 from below | **PASS**: min sigma^2 D = 0.794 (m=5) -> 0.973 (m=40), always at k = floor(N/2), runner-up is the adjacent central index, never a tail k |
| 7 | Lemma 7 | table exact; m >= 5: min = central; m = 4: first minimizer k = 2 | **PASS**: argmin = floor(N/2) exactly for all 5 <= m <= 120; m = 4 argmin = 2 = N/2 - 1 (row 1,3,5,6,5,3,1; r(2) = r(4) = 25/18 tie) |
| 8 | Part (c) | min of sigma^2(r_m - 1) over m >= 5 is at m = 6, ~0.8657; c = 43/50 consistent, c = 7/8 fails | **PASS**: exact minimum 187/216 = 0.865741 at m = 6 (I_6(6) = 90, I_6(7) = I_6(8) = 101, r_6 = 101/90 — all exact values in the draft are correct); 187/216 >= 43/50 but < 7/8 |

Auxiliary referee checks (also all consistent with the draft): the product formula for
the characteristic function matches the exact polynomial (m=6, t=0.3, 10 digits); the
Edgeworth profile sigma^2 D_m(k) = 1 + (kappa_4/2 sigma^4)(1 - y^2) matches the exact
ratios to 3-4 decimals across |y| <= 2 at m = 80; the pointwise (3.1) relative error is
~0.71/m^2 for m = 20..80, confirming the O_C(m^{-2}) claim.

---

## 2. Lemma-by-lemma findings

### Lemma 1 (symmetry + log-concavity) — sound.
Correct citations (Bóna; Hoggar product-closure). No issues.

### Lemma 2 (char. function + cumulants) — sound and verified.
MGF product formula verified numerically against the exact polynomial. Per-factor
kappa_4 = -(j^4-1)/120 verified (e.g. j = 6: -1295/120 = -10.7917, matches direct
moment computation). Closed form verified exactly. kappa_{2r} = O(m^{2r+1}) is
immediate. No issues.

### Lemma 3 (central Edgeworth) — statement numerically true; **proof of (3.2) invalid as written → UNMARKED GAP (Flaw F1, major).**
- (3.1) is fine as a sketch and numerically confirmed (rel. error ~0.71/m^2 uniformly
  in |k - mu| <= 2 sigma).
- **The failing step** is the derivation of (3.2):

  > "For (3.2) ... Equivalently, take the discrete second difference of the logarithm
  > of (3.1), using one additional Petrov term to control the differentiated remainder."

  This is not a proof, and the arithmetic shows it cannot be one: the pointwise error
  in (3.1) is Theta(m^{-2}) (measured: 0.71/m^2), while D_m(k) itself is ~ sigma^{-2}
  ~ 36 m^{-3}. Second-differencing three quantities each carrying an unstructured
  O(m^{-2}) error yields an O(m^{-2}) bound on D_m(k) — **10x larger than the entire
  quantity being estimated** already at m = 40, and infinitely far from the claimed
  O_C(m^{-5}).  To get (3.2) one must either (i) expand the second difference directly
  via the Fourier representation
  2p(k) - p(k-1) - p(k+1) = (1/2pi) ∫ e^{-itx} phi(t) (2 - 2cos t) dt
  (this is the actual CJZ mechanism, and it works because the (2 - 2cos t) factor is
  differenced *inside* the integral), or (ii) push the pointwise expansion to error
  O(m^{-5}) — three more Edgeworth orders with all smooth terms differenced
  analytically. Neither is done or stated. The phrase "one additional Petrov term"
  does not name a theorem and would not suffice (one more term gives pointwise
  O(m^{-3}), still >= the target O(m^{-5}) after differencing).
- Consequence: Lemma 4, the in-window part of Lemma 7, and the upper bound in part (a)
  all rest on an unproven (though numerically correct — NC3 passes) estimate. This gap
  carries **no GAP marker**, and part (a)'s "complete modulo GAP 6.1" is therefore
  overstated.
- Minor (F4): "The complementary range is exponentially small by the standard Petrov
  bound" — no precise statement for this non-iid triangular array. It is true (measured
  log|phi| <= -82 for t >= 0.5 at m = 40) and provable in two lines from the product
  formula (e.g. keep only the j = 2, 3 factors), but as written it is an appeal to an
  unnamed theorem. Borderline; flagged as minor since the spec itself blesses "Petrov"
  for this purpose.

### Lemma 4 (central ratio) — correct **given (3.2)**; constants verified.
The k_c parity discussion (y = 0 or -1/(2 sigma)) is right; e^D expansion is right;
the second-order constant in (4.3), sigma^2(r_c - 1) = 1 - 27/(25m) + O(m^{-2}), is
strongly confirmed (m·(1 - varfit) -> 1.075 at m = 100 vs 27/25 = 1.08). CJZ is used
only as a named precedent here, not as a cited theorem doing work — so no illegal
transfer of their central-Gaussian-binomial result. The load is entirely on Lemma 3,
i.e. on Flaw F1.

### Lemma 5 (tilted variance maximal at 0) — **complete and correct; the strongest piece of the draft.**
Every step verified: v_j' formula (checked numerically to 8 digits), h'/h =
3/u + tanh u - 3 coth u (checked), the clearing of denominators to
F(u) = 3u + 2u sinh^2 u - 3 sinh u cosh u (algebra re-derived: multiply
3 coth u - 3/u - tanh u > 0 by u sinh u cosh u and use cosh^2 = 1 + sinh^2),
F(0) = 0, F'(u) = 4 sinh u (u cosh u - sinh u) > 0 (checked). Note h(js) < h(s)
needs j >= 2 and h strictly decreasing — both in place (v_1 = 0 identically). This
lemma is publishable as-is.

### Lemma 6 (global curvature) — mechanism elegant; **one honest GAP + one FALSE unmarked uniformity claim (Flaw F2, moderate).**
- The clean part is correct: Phi''(x) = -1/B(t_x) and
  2Phi(x) - Phi(x-1) - Phi(x+1) = ∫_{-1}^{1} (1-|u|)/B(t_{x+u}) du >= sigma^{-2}
  by Lemma 5. Nice.
- GAP 6.1 (saddlepoint error E_m) is honestly marked. Not counted.
- **Unmarked flaw**: the sentence

  > "and similarly the discrete second difference of -1/2 log B_m(t_x) should be
  > o(sigma^{-2}) uniformly in x"

  is **false as a uniform statement**. Referee computation (m = 20, saddle solved by
  bisection): the second difference of -1/2 log B(t_x) equals **-3759·sigma^{-2}** at
  k = 1, -34·sigma^{-2} at k = 2, -5·sigma^{-2} at k = 5, and is still -1.3·sigma^{-2}
  at k = 10; it only becomes o(sigma^{-2}) well inside the bulk. Worse, it is
  *negative* throughout the tail, i.e. it fights the desired inequality; (6.1) survives
  there only because the Phi-term ∫(1-|u|)/B du blows up faster (B(t_x) -> 0 at the
  edge). So the draft's bookkeeping "main term >= sigma^{-2} + two corrections both
  o(sigma^{-2})" cannot be repaired uniformly: the extreme tail k = O(1) (where, e.g.,
  r_m(1) -> ~1.9, r_m(2) -> ~1.44) must be split off and handled by direct
  combinatorics. GAP 6.1's text gestures at the tail transition but attaches the gap
  only to E_m; the log-B claim is asserted with "should be" and no marker. Counted as
  an unmarked flaw (the fix is routine but genuinely necessary).
- Minor (F5): at k = 1 and k = N-1 the identity needs Phi at the boundary x = ±N/2
  where t_x = ±infinity; finite limits exist but this is never addressed — subsumed by
  the same tail split.

### Lemma 7 (centrality) — honest GAP 7.1 in the microscopic range; **unmarked logic gap in the intermediate regime (Flaw F3, moderate).**
- In-window: "for |y| >= c the gain is >>_c m^{-4} which dominates O_C(m^{-5})" —
  correct arithmetic (kappa_4/sigma^6 ~ m^{-4}), *given (3.2)* (Flaw F1 again).
- **The failing step**: outside the central window the draft writes

  > "Outside the central window, Lemma 6 plus the strict inequality B_m(t) < sigma^2
  > for t != 0 should give a still larger curvature."

  But Lemma 6 as stated gives only D_m(k) >= (1 - eps_m) sigma^{-2} with an
  *unspecified* eps_m = o(1), while the central value it must beat is
  D_m(k_c) = (1 - (27/25)/m + o(1/m)) sigma^{-2}. Unless eps_m = o(1/m) — which
  nothing in the draft supplies or even claims — Lemma 6 is quantitatively too weak to
  exclude a sub-central tail minimizer. What is needed is D_m(k) >= (1 + delta) sigma^{-2}
  for |k - mu| >= C sigma (available in principle from B(t) <= (1 - delta') sigma^2 for
  |t| >= t_0, by Lemma 5 — but that quantitative statement is neither formulated nor
  proven). GAP 7.1 covers only the microscopic range |k - mu| = O(1), so this
  intermediate-regime hole is **unmarked**. Part (b)'s GAP STATUS understates what is
  missing.
- Also note: "Together with finite verification, this proves Theorem F2(b)" — the
  finite verification is unexecutable because no explicit threshold m_0 exists in the
  draft; the draft concedes this in the GAP STATUS line, so not double-counted.

---

## 3. Parts (a), (b), (c): established or asserted?

- **Part (a)**: NOT fully established. Upper bound r_m <= 1 + sigma^{-2} + O(m^{-4})
  rests on (3.2) (Flaw F1, unmarked). Lower bound rests on Lemma 6 (honest GAP 6.1 +
  Flaw F2). The claim "Part (a) is complete modulo GAP 6.1" is **overstated** — it is
  complete modulo GAP 6.1 *and* F1 *and* F2's tail split.
- **Part (b)**: NOT established. Depends on GAP 7.1 (honest) plus the unmarked
  intermediate-regime gap F3, plus an explicit threshold that does not exist. The
  reduction "symmetry -> consider k <= mu" and the m = 4 edge case (|2 - 3| <= 1) are
  handled correctly.
- **Part (c)**: honestly declared not achieved (GAP 8.1) — allowed by the spec
  ("stretch — attempt, flag if not achieved"). **Credit**: the draft correctly refutes
  the spec's own suggestion c = 7/8, exhibiting sigma_6^2 (r_6 - 1) = 187/216 =
  0.865741 < 7/8 with exact coefficients I_6(6) = 90, I_6(7) = I_6(8) = 101 (referee-
  verified; the spec's "sigma^2(r_m-1) increasing" is itself wrong at m = 5 -> 6).
  The proposed replacement target c = 43/50 is consistent with the exact table through
  m = 40 (referee-verified: the m >= 5 minimum is exactly 187/216 >= 43/50), but c =
  187/216 would be the sharp choice if monotonicity for m >= 6 were proven.

## 4. Flaw list (unmarked; ranked)

1. **F1 (major, Lemma 3 proof of (3.2))**: second-differencing the pointwise expansion
   (3.1) with O(m^{-2}) error cannot give an O(m^{-5}) — or even O(m^{-3}) — bound on
   D_m(k); the entire central analysis (Lemma 4, Lemma 7 in-window, part (a) upper
   bound) rests on this unproven estimate. Numerically true, but not proven, and not
   GAP-marked.
2. **F2 (moderate, Lemma 6)**: the uniform o(sigma^{-2}) claim for the second
   difference of -1/2 log B_m(t_x) is false in the tail (referee measured
   -3759·sigma^{-2} at k = 1, m = 20); extreme tail needs a separate argument; not
   GAP-marked (GAP 6.1 covers only E_m).
3. **F3 (moderate, Lemma 7 / part (b))**: outside the central window, Lemma 6's
   (1 - eps_m) sigma^{-2} with unspecified eps_m does not beat the central value
   (1 - 1.08/m) sigma^{-2}; the needed (1 + delta) sigma^{-2} strengthening is only
   gestured at ("should give"); not covered by GAP 7.1.
4. **F4 (minor, Lemma 3)**: minor-arc / complementary Fourier range bound asserted via
   an unnamed "standard Petrov bound"; true and easy, but not proven.
5. **F5 (minor, Lemma 6)**: boundary cases k = 1, N-1 of the Phi second-difference
   identity (t_x = ±infinity) unaddressed; subsumed by F2's tail split.

Honest gaps (noted, NOT counted): GAP 6.1, GAP 7.1, GAP 8.1, and the two GAP STATUS
lines — though as noted, the GAP STATUS for parts (a) and (b) undercount the missing
steps because of F1–F3.

## 5. What survives / recommendation

Keep verbatim: Lemma 1, Lemma 2 (with verified kappa_4 closed form), Lemma 5, the
Phi''-identity core of Lemma 6, Lemma 4's constants, and the part (c) refutation of
c = 7/8. The single highest-value fix is F1: redo (3.2) via the differenced Fourier
integral with the (2 - 2cos t) kernel — this simultaneously makes Lemma 4 rigorous and
gives the quantitative in-window machinery Lemma 7 needs. Then split k = O(1) off from
Lemma 6 (fixes F2/F5) and state the outside-window bound as D >= (1 + delta) sigma^{-2}
via Lemma 5's strict decay (fixes F3). Part (c) additionally needs every constant made
explicit — currently far away.
