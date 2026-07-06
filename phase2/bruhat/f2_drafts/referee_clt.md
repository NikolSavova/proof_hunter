# Referee report — draft_clt.md (Draft C: local-CLT / characteristic-function route)

Adversarial referee pass, 2026-07-06. All computations rerun against the exact harness
`mahonian.py` (extended to `m = 120`); referee scripts in the session scratchpad
(`quick_checks.py`, `mid_checks.py`, `heavy_checks.py`).

## Verdict (one paragraph)

This is a serious, largely honest draft with a genuinely strong analytic core. **All 18 of
the draft's NUMERIC CHECK lines pass**, most to the exact quoted digits. The CJZ transfer
is done the honest way: nothing is cited from CJZ beyond method — the factorization,
log-series, and determinant representation are re-derived for the q-factorial and verified
(so the spec's "CJZ is central-Gaussian-binomial only" trap is avoided). Lemma 3.3
(tilted-variance monotonicity) is fully correct — I checked the enveloping-series case
analysis line by line. However, I found **four unmarked flaws** in proofs the draft
presents as complete: the `e^{-m/6}` deduction in Lemma 1.4 is false from its own bound;
the tail-sum step in Lemma 1.3(ii) is false as stated; the window-edge comparison in
Cor. 2.4(ii)/(iii) is arithmetically wrong for every `m` (verified to `m = 10^6`); and
§5(b) silently uses a "tilted Edgeworth refinement" that is stronger than anything stated
or gapped. All four are repairable without new ideas, but as written they puncture the
claimed proofs of Cor. 2.4, the sharp rate in (a), and the `Cm`-localization in
(b)-partial. Judged against the frozen theorem: (a) survives (modulo declared GAP-2 plus
the repairs below); (b) at scale 1 and (c) are open — but the draft declares that honestly
(GAP-3, GAP-1/2/4), and its correction of the spec's `c = 7/8` to `c = 187/216` is right
and verified exactly.

---

## Part 1 — Every NUMERIC CHECK line, rerun

| # | Location / claim | Result |
|---|---|---|
| 1 | §0 harness baseline `--mmax 40` | **PASS.** argmin central all `4<=m<=40`; min = central for `m>=5`; varfit `0.8426 (m=4), 0.875 (5), 0.8657 (6), 0.8766 (7), ..., 0.9734 (40)`. The claimed dip at `m=6` is real; the spec's "increasing from 0.875 at m=5" is indeed wrong. |
| 2 | §0 exact fractions `7/8, 187/216, 931/1062` (m=5,6,7) | **PASS.** Exact match, including the unreduced-looking `931/1062` (it is in lowest terms). |
| 3 | Lemma 1.1 Fourier inversion, m=10 | **PASS.** Errors `0.0, 6.9e-18, 0.0` at k=22,27,34. |
| 4 | Lemma 1.2 `B_30, B_40` | **PASS** (trivial last-digit slip: actual `B_30 = 0.0356226`, draft quotes `0.0356230`; `B_40 = 0.0267578` vs quoted `0.0267580`). Cumulant algebra `kappa_4 = -(j^4-1)/120` independently verified from `mu_4 = (j^2-1)(3j^2-7)/240`. |
| 5 | Lemma 1.3(i) Gaussian domination, m=10,30,60 | **PASS.** Max of `phi(t) e^{sigma^2 t^2/2}` = 0.99999999987–0.9999999997, attained as `t -> 0+`. |
| 6 | Lemma 1.4 far-region decay | **PASS** on the numbers: max `|phi|` on `[2pi/m, pi]` = `3.88e-9 (20), 6.31e-13 (30), 1.15e-16 (40), 4.4e-24 (60)` (draft's `3.3e-24` at m=60 is grid-coarseness; same order). But see Flaw F1: the lemma's *stated bound* does not deliver the "in particular" clause. |
| 7 | Prop 2.1 Edgeworth accuracy | **PASS.** `sup_{|x|<=3} relerr * m^2 = 6.955, 6.303, 6.088, 6.010` (m=20,30,40,60) — exact match to quoted `6.96, 6.30, 6.09, 6.01`. |
| 8 | Lemma 2.2 determinant identity, m=8 | **PASS.** Exact `D(14) = 4.657679043840e-04`, `D(18) = 2.227154244221e-04` (both match the quoted 12 digits); my independent separable quadrature agrees to `<= 1.6e-12` relative. Identity algebra also verified by hand (symmetrization argument is correct). |
| 9 | Prop 2.3 window law (the "single most important check") | **PASS.** All ten `(m, dk)` values reproduce; m=40: `dk=0: -0.026876/-0.026758`, `dk=20: -0.021252/-0.020946`, `dk=60: +0.025513/+0.025547` — exact match. Residual at dk=0 is `1.18e-4 ≈ 0.19/m^2` as claimed; large-`x` residual is positive as claimed. |
| 10 | Prop 2.3 constant `27/25` | **PASS.** `m(1 - varfit_central) = 0.953 (10), 1.038 (20), 1.057 (30), 1.065 (40), 1.071 (60), 1.074 (80), 1.075 (100)` — exact match; `27/25 = 1.08` with `O(1/m)` drift. |
| 11 | Lemma 3.2 tilted moment formulas | **PASS.** Formulas match direct truncated-geometric sums to `<= 6e-15` at `(5,0.3), (9,0.7), (3,1.5)`. Derivatives of `log Z_j` independently verified. |
| 12 | Lemma 3.3 `Q > 0`, `Var_j(u)` decreasing | **PASS.** `min Q > 2.7e-10` on a 200k grid of `(0,40]`; zero monotonicity violations for `j in {2,3,5,10,40}`. |
| 13 | Cor 3.4 variance drop, m=40 | **PASS.** `1 - sigma(u)^2/sigma^2 = .001231, .007644, .029929, .110325` at `w=.2,.5,1,2` — exact match. Coefficient `3/100` algebra verified. |
| 14 | Prop 3.5 bulk check, m=30,40 | **PASS.** `(r(k)-1) sigma(u_k)^2` = `0.9645/.9627/.9615/.9649/.9671` (m=30) and `0.9732/.9719/.9710/.9736/.9752` (m=40) at `k/N = .45/.35/.25/.15/.08` — exact match, and `sigma(u)^2/sigma^2 = 0.084` at `k/N=.08, m=40` as quoted. |
| 15 | Lemma 4.1 pentagonal identity | **PASS.** Exact integer identity for all `k <= m` at `m = 20, 35, 50`. (First run "failed" at m=35,50 — that was a float bug in *my* checker, `(-1)**-n` returning float; exact-arithmetic rerun passes.) |
| 16 | Lemma 4.2 edge bound | **PASS.** `min_{1<=k<=m} (r(k)-1)k(m+k)/(m-1) = 1.0025 (30), 1.0013 (40)` — exact match. The exact identity `T(k)^2/(T(k-1)T(k+1)) = 1 + (m-1)/(k(m+k))` verified algebraically. |
| 17 | Thm (b) check: argmin `= N//2` and min = central, `5<=m<=120` | **PASS.** True for every `m` in 5..120. |
| 18 | Thm (c) check: varfit `>= 187/216`, equality at m=6, increasing on 6..120 | **PASS.** Exact equality at m=6; strictly increasing 6..120; `varfit(100) = 0.9892`, `varfit(120) = 0.9910` as quoted in §0/§5. |

**Score: 18/18 pass.** The draft's empirics are impeccable; the numbers were clearly
actually run, not fabricated.

---

## Part 2 — Flaws (unmarked; these count)

### F1 (WRONG DEDUCTION, Lemma 1.4): "In particular `|phi(t)| <= e^{-m/6}` for `m >= 25`" does not follow from the lemma's own bound.

The lemma proves `|phi| <= exp(-m h(beta) + log m)` with worst case
`beta = 1/2 + 1/m`, `h(1/2) = 0.1931`. Referee computation of the *stated bound* at the
worst `beta`:

- `m = 20`: bound `= 1.04` — **vacuous** (exceeds 1);
- `m = 25`: bound `= 0.504` vs `e^{-25/6} = 0.0155` — off by a factor 32;
- `m = 100`: `1.09e-6` vs `5.8e-8`; `m = 200`: `9.0e-15` vs `3.3e-15` — still fails.

The inequality `m h(1/2 + 1/m) - log m >= m/6` first holds around `m ≈ 280`, not 25.
The *truth* `|phi| <= e^{-m/6}` is confirmed numerically with huge slack (check #6), but
the proof given does not establish it. **Downstream damage:** Prop 2.1's proof invokes
"Lemma 1.4 gives `<= e^{-m/6}` for `m >= 25`", so the claimed `C_1 <= 3 for m >= 20`
constant chain is broken at both ends (`m=20` is below the lemma's own `m>=8`+vacuity
threshold, and the `e^{-m/6}` clause is unproved). Also: for the determinant analysis the
far region must beat the *signal* `D(k) ~ sigma^{-4} ~ 1300/m^6`; with the actual proved
bound `exp(-m h(beta) + log m)` this happens only for `m ≳ 140`. That silently invalidates
the (c)-reduction's estimate "`m_0 ~ 15–40` for moderate `C'`" (§5(c)): with the *proved*
far-region constant, `m_0` lands near or beyond the verified range `m <= 120`. Repair:
prove a stronger far-region bound (easy — the true decay is `~ (2/pi)^{cm}`-type; e.g.
keep the product bound `prod_{j>=J} J/j` instead of integral-comparing it away) or extend
the finite check. As written, unmarked.

### F2 (WRONG PROOF STEP, Lemma 1.3(ii)): "`S_{2K} - m <= 2 m^{2K+1}/(2K+1)` (the factor 2 is generous for `m >= 4`)" is false.

Referee counterexamples: `m=4, K=3`: `S_6 - 4 = 4886 > 2*4^7/7 = 4681.1`; also
`(m,K) = (4,4), (4,5), (5,4), (5,5), (6,5)` fail, and for **every** fixed `m` the bound
fails once `2K+1 > 2m` (the `j=m` term alone, `m^{2K}`, exceeds `2m^{2K+1}/(2K+1)`). So
the "tail is at most twice its first term" argument, which applies this bound termwise for
all `K >= 3`, collapses. The *conclusion* `-m^7 t^6/317520 <= R(t) <= 0` is nevertheless
numerically true (referee grid check on `(0, sqrt(2)pi/m]` at `m = 4,5,6,10,20,40`: max
violation `<= 3e-15`, and `R <= 0` throughout), and the proof is repairable: use the ratio
`(S_{2K+2}-m) <= m^2 (S_{2K}-m)` together with `c_{K+1}/c_K <= 1/pi^2`, which gives
term-ratio `<= (mt/2)^2/pi^2 <= 1/2` needing the `2m^{2K+1}/(2K+1)` bound only at `K = 3`
(valid for `m >= 5`; at `m = 4` it fails even there and needs the exact `S_6`). Unmarked
wrong step in a lemma labeled fully proved.

### F3 (WRONG COMPARISON, Cor. 2.4(ii)/(iii)): the window-edge argument "growth beats the error" is false for every `m`.

Quoted step (end of Cor. 2.4): "For `1 <= |x_k| <= sqrt(log m)` the growth `B_m(x_k^2-1) > 0`
beats the error term because `e^{x^2} <= m` there and
`B_m x^2 m^2 >= (27/25) m log m >> C_2 m`."

Two errors. (i) On that range `B_m x^2 m^2 >= (27/25) m x^2`, which at `x = 1` is
`(27/25)m` — the claimed `(27/25) m log m` requires `x^2 = log m`, the opposite endpoint.
(ii) The relevant comparison is pointwise `B_m x^2` vs `C_2 (1+x^6) e^{x^2}/m^2`, and near
the window edge the error **wins for every m**. Referee computation at `x = sqrt(log m)`,
`C_2 = 0.2`:

| m | `B_m x^2` | error term | growth beats error? |
|---|---|---|---|
| 30 | 1.22e-1 | 2.69e-1 | NO |
| 100 | 4.97e-2 | 1.97e-1 | NO |
| 1000 | 7.46e-3 | 6.61e-2 | NO |
| 10^6 | 1.49e-5 | 5.28e-4 | NO |

(At `x^2 = log m` the error is `~ C_2 log^3 m / m` vs growth `~ (27/25) log m / m`; the
error is larger by `~ log^2 m` — asymptotically, not just at small `m`.) Consequently
**Cor. 2.4(ii) (the window lower bound `sigma^2(r-1) >= 1 - B_m - C_2'/m^2` on the full
window) and Cor. 2.4(iii) ("no minimizer lives at `1 <= |x| <= sqrt(log m)`") are not
established by the given argument** on `x^2 ∈ [log m - O(log log m), log m]`. This
propagates: §5(a)'s window bullet cites 2.4(ii); §5(b)'s localization cites 2.4(iii).
Repair (available, but not in the draft): split at a *constant* `x_0` instead of
`sqrt(log m)` — for `|x| <= x_0` the error is honestly `O((1+x_0^6)e^{x_0^2}/m^2) =
O(1/m^2)` and the window argument is fine; for `|x| >= x_0` use the tilt regime, where
Prop. 3.5 + Cor. 3.4 beat the center once `(3/100)w^2 > (C - 27/25)/m`, i.e. `x^2 >=
(25/27)(C - 27/25)` — a constant. Note the repair (its second half) leans on GAP-2's
unproven Prop. 3.5; the frozen part (a) needs only `1+o(1)` and survives, and the sharper
rate `1 - (27/25)/m + O(m^{-2})` also survives *after* this repair — but the proof as
written is broken at the regime hand-off, and this is nowhere marked GAP.

### F4 (UNSTATED ESTIMATE, §5(b)): the `Cm`-localization uses a "tilted Edgeworth refinement" that appears in no lemma and no GAP.

Quoted (§5, Theorem (b)): "...and the tilted Edgeworth refinement
`r(k)-1 = sigma(u_k)^{-2}(1 - B_m(1+O(w_k^2)) + O(m^{-2}))` makes the comparison with the
center strict once `w_k^2 >= C''/m`..."

Prop. 3.5 (itself GAP-2, sketch-level) asserts only the cruder
`r(k)-1 = sigma(u_k)^{-2}(1 + theta C/min(m, sigma(u_k)^2))` — an `O(1/m)` relative error
with an unspecified constant `C` that may well exceed `B_m·m = 27/25`. With Prop. 3.5
alone one can exclude minimizers only for `w^2 ≳ (C - 27/25)/m`, i.e. `|x| ≳ const`, which
localizes the argmin to `O(sigma)`, **not** `O(m)`. The `1 - B_m(1+O(w^2))` refinement —
which is exactly what's needed to push exclusion down to `w^2 ~ C''/m` and to make the
`|argmin - N/2| <= Cm` claim true — is never stated as a proposition, never proved, and
GAP-2's ledger entry ("uniform-in-u error constants... not written out") does not cover
the *form* of this refinement, only Prop. 3.5's constants. So the headline of the result
summary, "(b) Partially proved: argmin is localized to `|k - N/2| <= Cm`", is not
established even modulo the declared GAPs; what is established (modulo GAP-1/2 and the F3
repair) is localization to `O(sigma) = O(m^{3/2})`, with `Cm` requiring this extra
unproved estimate. Should have been GAP-marked.

### F5 (FALSE EMPIRICAL CLAIM at m=4): "argmin = floor(N/2) for ALL `4 <= m <= 120`."

Stated twice (§0 result summary: "exact centrality verified numerically for all
`4 <= m <= 120`"; GAP-3: "Empirically the statement is exact: `argmin = floor(N/2)` for
ALL `4 <= m <= 120`"). False at `m = 4`: the ratio sequence is
`9/5, 25/18, 36/25, 25/18, 9/5`, so the min `25/18` is attained at `k = 2` and `k = 4`,
not at `floor(N/2) = 3` (where the ratio is `36/25 > 25/18`). `|argmin - N/2| = 1`, so the
frozen statement (b) is fine at m=4, but "argmin = floor(N/2)" is not. Tellingly, the
draft's own §5(b) check code starts at `m = 5`. (The spec's parenthetical has the same
slip; the draft corrected the spec's m=6 monotonicity error but propagated this one.)
Correct statement: `argmin = floor(N/2)` for `5 <= m <= 120`; at `m = 4` the argmin is
off-center by exactly 1 (tied pair).

### F6 (minor, constants/consistency — cosmetic, listed for completeness)

- Cor. 2.4(iii): `gamma = sqrt(50 C_2 e/27)` silently drops the `(1+x^6) <= 2` factor its
  own display carries; with it, `gamma = sqrt(100 C_2 e/27)`. And with `C_2 = 0.2`,
  `gamma ≈ 1.0`, so `(gamma/6)m ≈ m/6` — the quoted "`~ m/4`" (and §0's "`C ~ 1/4`")
  doesn't match the draft's own formula.
- Lemma 1.2 check: `B_30` quoted `0.0356230`, actual `0.0356226` (last digit).
- Prop. 2.3: the error *shape* `C_2 (1 + x^6) e^{x^2}/m^2` is asserted ("transferring the
  remainders... through the double integral"), never derived; GAP-1 flags only the
  constant's value, but the `x`-dependence is load-bearing (it is exactly what F3 exploits)
  and its derivation is also missing. Half-shielded by GAP-1's wording; noted.
- Lemma 4.2 is correct but tighter than it looks: at `m = 16, k = 1` the chain
  `(1+g)(1-4k/m) >= 1+g/2` holds with exact *equality* (`49/34 = 49/34`); only the
  discarded `4k^2/m^2` term makes the lemma strict. Worth a remark in revision — no slack
  is left at the stated threshold.

---

## Part 3 — Lemma-by-lemma assessment (what holds)

- **Lemma 1.1** (factorization + inversion): correct, standard, verified. Sound.
- **Lemma 1.2** (cumulants): algebra independently verified (`kappa_4` per-factor formula
  checks out; `B_m ~ 27/(25m)` arithmetic correct). Sound.
- **Lemma 1.3**: statement (i) correct and verified; series derivation and `c_1, c_2, c_3`
  values verified. Statement (ii) *true* (referee-verified numerically) but its proof has
  the false step F2. 
- **Lemma 1.4**: main bound's proof is essentially fine (the `sin(jx) <= j sin x` and
  integral-comparison steps check out; `s >= 2/m` via `sin x >= 2x/pi` is right), but the
  "in particular" clause is F1.
- **Prop. 2.1**: scheme is the right one; split points and the super-polynomial-tail
  arithmetic (`sigma^2 t_2^2/2 = sqrt(m)/72`, `|kappa_4| t_2^4/24 <= 6.9e-5`,
  `15·1296^{3/2}/317520 = 2.20`) all verified. Constant claims inherit F1/F2; honestly
  GAP-1-shielded *except* the `m >= 25` far-region invocation.
- **Lemma 2.2**: exact, verified algebraically and to 12 digits numerically. The
  accompanying remark on why the determinant detour is necessary (additive Edgeworth error
  `sigma^{-1}m^{-2}` exceeds the signal `sigma^{-4}`) is correct and important. **This +
  Lemma 1.3 is the legitimate q-factorial replacement for CJZ (4.11); no illegal transfer
  of their central-binomial result occurs anywhere in the draft.** Sound.
- **Prop. 2.3**: the model identity is plausible (its `x=0` and `x^2`-slope consequences
  are confirmed by the data to `O(1/m^2)`), but "machine-verified symbolic computation" is
  not exhibited; error shape underived (F6). Empirically the window law is superbly
  confirmed (check #9).
- **Cor. 2.4**: (i) fine; (ii)/(iii) broken at the window edge (F3).
- **Lemma 3.1**: trivial and correct.
- **Lemma 3.2**: verified symbolically and numerically. Sound.
- **Lemma 3.3**: **fully correct.** Referee re-derived: `kappa_3 < 0 ⟺ G(jx) < G(x)`,
  `G(x) = x^3 cosh x/sinh^3 x`; `(log G)' = 3/x + tanh x - 3coth x`; the three-interval
  case analysis checks out exactly (the enveloping bounds `coth x >= 1/x + x/3 - x^3/45`,
  `tanh x <= x - x^3/3 + 2x^5/15` are valid on the stated ranges and yield
  `(2x^3/15)(2-x^2) > 0`; the endpoint arithmetic `3.0265 < 3.3143` is right). The
  strongest genuinely new fully-proved ingredient of the draft.
- **Cor. 3.4**: coefficient `3/100` verified both symbolically and numerically. Sound
  (small-`w`; the large-`w` claim is soft-compactness, fine).
- **Prop. 3.5**: honestly GAP-2. The sketch's three ingredients are the right ones; the
  odd-cancellation-at-the-tilted-mean device is correct in principle. Note §5(a)'s side
  claim `sigma(u_k)^2 ~ k(1+k/m)` is itself unproved (order-plausible; used only to argue
  `sigma(u_k)^2 -> infinity`, which is what matters).
- **Lemma 4.1**: exact, verified. Sound.
- **Lemma 4.2**: exact identity and chain verified (see F6 re tightness). Sound.

## Part 4 — Are (b) and (c) actually established?

**(b) as frozen (`|argmin - N/2| <= 1`): NOT established — honestly declared (GAP-3), so
not counted as a hidden flaw.** But the *claimed partial* result (`|argmin - N/2| <= Cm`)
is also not established as written: it needs Cor. 2.4(iii) (broken at the window edge, F3)
plus the unstated tilted refinement (F4). What genuinely survives modulo the declared
GAPs, after the F3 repair, is localization at scale `O(sigma) = O(m^{3/2})` — i.e.
`argmin/N -> 1/2` — which is strictly weaker than what the summary table advertises. The
result-summary row for (b) should be downgraded accordingly.

**(c): NOT established — honestly declared (GAP-1/2/4).** The draft's contribution here is
real and verified: the spec's `c = 7/8` is indeed false at `m = 6`
(`sigma^2(r_6-1) = 187/216 = 0.865741 < 0.875`, exact), the corrected sharp constant is
`c = 187/216`, and `varfit >= 187/216` with equality exactly at `m = 6` and strict
increase on `6 <= m <= 120` all verify. However the reduction's feasibility estimate
("`m_0 ~ 15–40`") is undermined by F1: with the constants the draft actually *proves*
(Lemma 1.4), the far-region error beats the `sigma^{-4}` signal only for `m ≳ 140`, so the
finite check would have to be pushed past 120 or Lemma 1.4 strengthened. Not fatal
(both are easy), but the reader is given a materially over-optimistic account of how close
(c) is.

**(a): established as `1 + sigma^{-2}(1+o(1))` modulo declared GAP-2 and the F3 repair**
(the repair is routine: window at constant `x_0`, tilt beyond). The advertised sharper
rate `1 - (27/25)m^{-1} + O(m^{-2})` also survives the repair in principle but its written
proof passes through the broken Cor. 2.4(ii). GAP-1's claim that it "does NOT block the
asymptotic statements" is fair for the constants, but F1 and F3 are not constant issues —
they are wrong steps, and they are in the (a) chain as written.

## Part 5 — Summary tallies

- NUMERIC CHECK lines in the draft: **18 run, 18 pass, 0 fail** (two trivial last-digit /
  grid-resolution discrepancies noted at #4, #6).
- Referee adversarial probes: 4 run; 3 exposed false *prose* claims (F1, F2, F3); 1
  (remainder bound of Lemma 1.3(ii)) confirmed the *statement* despite the broken proof.
- Unmarked flaws: **F1–F5** (F6 cosmetic). Declared GAPs (1–4) are consistent with the
  rules and are not counted, except where the text overreaches beyond them (F3, F4, and
  the (c) feasibility estimate).
- Recommendation: **major revision.** The skeleton (exact Fourier structure, determinant
  representation, tilt + variance monotonicity, pentagonal edge) is the right proof and
  most of it is verified; fix F1–F4, restate the regime split at constant `x_0`, state and
  either prove or GAP the tilted refinement, downgrade the (b) summary row, and correct
  the two m=4-adjacent misstatements.

*End of referee report.*
