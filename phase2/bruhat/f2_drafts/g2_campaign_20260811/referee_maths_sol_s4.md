# referee_maths_sol_s4 — adversarial maths referee on `sol_s4_20260812.md` (gpt-5.6-sol's (S4) attempt)

*Wave-6b cross-model refereeing, 2026-08-12. Target: `sol_s4_20260812.md`
(single-model, unrefereed). Bar: maximal, default-to-refutation; a
cross-model draft gets no extra credit for being cross-model. Sources
consulted: `STATUS_wave5.md` (authoritative ledger),
`CL_composition_20260812.md` §2/§4 ((S4) verbatim + how it is consumed),
`referee_maths_sl4p_repaired.md` §M2/§M3 (what the bootstrap seed actually
needs), `wave4_sl4p_repaired_20260812.md` §5.3/§5.4 (Lemma R.1/R.2
statements), `wave4_sl3p_20260812.md` (Theorem SL3' statement),
`wp4_draft_composite.md` (tier-1/tier-2, band floors `c_A`, far floor),
`wave6_s1_plan_20260812.md` §5 ((S4)/bootstrap consistency under the
re-architected chain). `g2_draft_t1_20260803.md` unread. New script (SAVED
and RUN 2026-08-12, output archived beside it, quoted verbatim below):
`referee_maths_sol_s4_scripts/ref_s4_checks.py`
(`out_ref_s4_checks.txt`). Every lemma SOL.1–SOL.6 re-derived by hand;
every displayed constant recomputed.*

## VERDICT: **MAJOR_ISSUES**

The draft's `m >= 700` architecture is genuinely good — a non-circular
C^2-local-CLT chain built ONLY on proved inputs (SL3', tier-2, R.1, far
floor, [A2]/[C.1]), with the tilt-invariance and lattice-curvature
identities exactly right and almost all arithmetic verified. But it does
NOT discharge (S4): the obligation starts at `m = 561`, the draft proves
`m >= 700`, and its coverage of `[561, 699]` is circular as written
(F1). Additionally the load-bearing remainder Lemma SOL.2's fourth-order
estimate is proved by assertion, and its displayed envelope (SOL.15)
cannot be produced by the termwise computation the draft invokes — the
absolute cumulant series violates it at the deep-tilt corner (F2). One
consumed input is mis-cited with a band-scope hole (F3), and one claimed
intermediate numeric bound is false by rounding (F4). Both major gaps have
demonstrated repair paths that keep every downstream constant, so this is
MAJOR_ISSUES, not FATAL — and not better.

---

## 1. The obligation, and finding F1 (scope): (S4) starts at `m = 561`; the draft's `[561, 699]` coverage is circular

**What (S4) requires** (`CL_composition_20260812.md` §4, verbatim scope):
`|s2(r(k) - 1) - 1| <= 0.89` for **`m >= 561`** and `lam(k)` in-band. How
it is consumed (§2 step 1): the seed feeds referee-M2's chord/monotone
iteration closing the INFL/QUADF bootstrap of Lemmas SL4'.6/.7 — and per
`referee_maths_sl4p_repaired.md` M2, SL4'.6/.7 "price EVERY ledger
entry". The ledger rows are consumed at every `m >= 561` (W2–W7 rows plus
the W1 ladder). M3 does NOT remove the seed on `[561, 699]`: M3's own
conclusion is that the surface becomes "SL1'-w + SL4'-E only **(plus M2's
bootstrap seed)**" — M3 closes the W1 rung's X-slot without SL4'-X, not
the bootstrap. The re-architected chain agrees: `wave6_s1_plan_20260812.md`
§5 re-verifies the M2 closure **at rows @ 561** ("W5 @ 561 ... W6b @ 561
... W7 @ 561 ... basins x_seed >= 0.920 > 0.89"). So the task-context
hypothesis "the obligation may start at m >= 700" is REFUTED by the
sources: **the seed is needed at every `m >= 561`.**

**What the draft delivers.** Theorem SOL.6 covers `m >= 700` only. For
`[561, 699]` it claims "the already closed W1 finite rung gives the
stronger CL estimate `|s2(r_m(k)-1)-1| <= 20/m`". That is a misreading:
Fact R.G / M3 close one ROW of the conditional ledger; CL itself on
`[561, 699]` is PROVED-MODULO-(S1)–(S4) — including (S4). Using CL's
conclusion there to supply the seed there is using (S4) to prove (S4).
The unconditional exact-computation closure stops at `m = 560` (Fact
SLV.2, `M_H = 560`; "no interim 555-reading survives"). The draft's own
"WHAT REMAINS" item 2 concedes exactly this risk; the concession is the
correct reading, so the deliverable is short by the 139 integers
`[561, 699]` — precisely the range containing the campaign's worst rows.

**Why not FATAL.** The `m >= 700` proof's constants structurally fail at
561 (script block [E], verbatim):

```
  A_min(561) = 0.28*561 = 157.08 < 196: True  -> (2/7)*sqrt(A) = 3.5809 < 4 (local range |y|<=4 NOT covered)
  s2_min(561) = 198.3083;  eps(561) <= 0.071012 > 0.06358
  E_cross[2](561) = 0.06887  (vs 0.00832 at 700: 8.3x bigger)
```

so no verbatim extension exists — but a referee-side feasibility sketch
(same machinery, split at `y* = (2/7)sqrt(A)`, honest remainder constant,
recomputed budgets; block [E]) gives

```
    H_min=0.4318 H_max=1.7093 -> deviation bound 0.7241 < 0.89: True
```

i.e. the same architecture closes `[561, 699]` with ~19% room against the
0.89 seed. This is a REPAIR ESTIMATE, not a proof; the prover must execute
it (the draft itself names this fallback and did not run it).

## 2. Finding F2 (load-bearing): Lemma SOL.2's (SOL.14) is proved by assertion, and (SOL.15) cannot come from the invoked termwise computation

(SOL.14) — `|log Phi(t) + s2 t^2/2 - i kappa_3 t^3/6| <= 0.0021 sigma^4
t^4` on `|t| <= (2/7) lam` — is the input to the entire local range of
Lemma SOL.4. Its "proof" is one sentence: "the same termwise calculation
applied from order four onwards gives ... the left side divided by
`sigma^4 t^4` is bounded by (SOL.15)", with no derivation of the
constants `6.72`/`0.72`. I computed the exact model quantities (script
block [B]; `env := |R4| * 24 lam^2/(s2 t^4)`, so (SOL.15) claims
`env <= 6.72 + 0.72u/(1-u)`, `u = |t|/lam`; exact cumulants via
`kappa_n = sum_j [Li_{-(n-1)}(e^{-lam}) - j^n Li_{-(n-1)}(e^{-j lam})]`,
`log Phi` summed directly, dps 40, `m = 700`):

```
  w=    623 u=0.2857: env_true=  6.2079 env_absseries=  8.2900 | (SOL.15) claim=7.0080 [true fits: True; abs-series fits: False] | (SOL.14) cap=  32.880 [fits: True]
  w=    120 u=0.2000: env_true=  5.7688 env_absseries=  6.9497 | (SOL.15) claim=6.9000 [true fits: True; abs-series fits: False] | (SOL.14) cap=  34.252 [fits: True]
```

Three facts follow. (i) **The claimed derivation is unsound**: the
absolute cumulant series `sum_{n>=4} |kappa_n| t^n/n!` — the best any
"termwise calculation from order four onwards" can bound — exceeds the
(SOL.15) envelope at the deep-tilt corner (8.2900 > 7.0080); the `n = 5`
slot alone needs coefficient `(24/120)|kappa_5| lam^3/s2 ~ 5.13`, not
`0.72`. (ii) (SOL.15) happens to hold for the TRUE remainder at all 12
probes (max `env_true = 6.36`, min margin ~7% at `(w, u) = (623, 0.1)`)
— but only via phase cancellation the draft never analyzes. (iii) The
final (SOL.14) constant is comfortable: `env_true <= 6.36` everywhere vs
the cap `0.0504 A >= 9.88`. **Repair path (keeps 0.0021 and everything
downstream):** prove `|kappa_n| <= 1.07 (n-1)! s2 / lam^{n-2}` for
`n >= 5` (my block [A] data and the F(x)=log(1-e^{-x}) derivative
structure support it; the `n = 3` analogue I verified analytically via
the monotone comparison `x^3 csch^2 x coth x` decreasing) plus
`|kappa_4| <= 6.72 s2/lam^2` (block [A]: max `c4 = 6.3793` at the deep
corner, matching the campaign's 6.4113 geometric limit); then
`env_abs <= 6.72 + 5.136 u/(1-u) <= 8.47` for `u <= 2/7`, and
`8.47/(24*196) = 0.0018 < 0.0021`. As WRITTEN, the lemma is unproved and
the displayed (SOL.15) is unobtainable by the stated means — a
plausible-but-wrong proof step of exactly the kind this campaign must not
absorb.

## 3. Finding F3 (mis-citation with a real scope hole): (SOL.5)'s crossover bound cites Lemma R.1 outside its stated scope

(SOL.5) claims `|Phi(t)| <= e^{-0.0176 m}` on `0.8 lam <= |t| <= t_0`
for the WHOLE tilt range `4/m < lam <= 0.89`, citing "[W.6] together
with Lemma R.1". But Lemma R.1 (`wave4_sl4p_repaired_20260812.md` §5.3)
is stated **only for `w in (4, 5]`** (band W1). For `w > 5` the citation
supports nothing. The bound is nevertheless TRUE from citable inputs: the
PROVED tier-2 estimate (`wp4_draft_composite.md`:
`|phi_lam(t)| <= exp(-c2 s2 t^2)`, `c2 = 0.0871`, on `0 < t <=
1.074|lam|`) plus the [A2] band floors `A >= c_A(W) m` give, at
`t >= 0.8 lam`, exponent `>= 0.0871 * 0.64 * c_A(W) * m`; script block
[D], verbatim:

```
  W2: 0.0871*0.64*0.35 = 0.019510 >= 0.0176: True
  W7: 0.0871*0.64*0.80 = 0.044595 >= 0.0176: True
```

(all of W2–W7 pass; W1 is exactly R.1's scope). Repair: one paragraph,
no constant moves. Until it is written, (SOL.5) as cited is unsupported
on six of the seven bands. I also confirm the independence claim: SL3',
tier-2, R.1, the far floor, and [A2]/[C.1] are all proved WITHOUT the
INFL/QUADF bootstrap or (S4) — the draft's non-circularity assertion
survives (this referee attacked it specifically; R.1 is a pointwise
elementary-bracket floor, no ledger input).

## 4. Finding F4 (numeric hygiene): one claimed bound is false; three margins are knife-edge

Recomputation of V1–V8 (script block [C], dps 40, verbatim):

```
  E_mid[0] = 0.000710591  < 0.00071: False
```

**The V3 claim `E_mid[0] < 0.00071` is FALSE** (true value
`0.000710591`). The error is absorbed downstream — the totals still hold
(`E0 = 0.023994719 < 0.02401 < 0.04: True`) — but under house exactness a
displayed strict bound that fails must be corrected (print `< 0.00072`
and re-add). Knife-edge but TRUE margins the numerics referee must pin at
higher dps: `E_loc[1] = 0.044819971 < 0.04482` (margin `2.87e-08`),
`g(eps0) = 0.398136966 > 0.39813` (margin `6.97e-06`), `-g''` bracket
margins `~7.7e-06`. Everything else in blocks [C] passes as claimed:
`E1 = 0.048191529 < 0.04820`, `E2 = 0.119122843 < 0.11916 < 0.13`,
`H_min = 0.607176 > 0.607`, `H_max = 1.533735 < 1.535`,
`X_max = 1.544552 < 1.545`, final deviation `0.544552 < 0.545 < 0.89`.

## 5. What I verified as SOUND (hand re-derivation, lemma by lemma)

- **(SOL.0)** tilt invariance of the adjacent ratio: exact
  (`e^{-lam}`-factors cancel; re-derived).
- **(SOL.1)–(SOL.3)**: `A in [0.28m, m]` is legitimately [A2](iii)
  (`c_A` row, min 0.28) + [C.1]; `0.28*700 = 196` exact;
  `s20 = 1960000/7921 = 247.443505 > 247.44`;
  `eps0 = 0.06357143 < 0.06358` (block [C]). Empirical `A/m` at 10
  probes stayed in `[0.2988, 0.9746]` (block [A]).
- **(SOL.4)**: Theorem SL3' (`wave4_sl3p_20260812.md`) is stated for ALL
  seven bands, `m >= 401`, `t in (0, 0.8 lam]`, `gamma* >= 0.32` — the
  uniform 0.32 is a correct consumption (two-referee input, no
  circularity).
- **(SOL.6)**: far floor `0.0741` on `[t_0, pi]` is the composite/A3
  citable input (consumed identically by R.2); `t_0 <= 1.074 lam` is
  Lemma SL3.C/Cor X.2. Not re-derived here (established inventory).
- **(SOL.9)/(SOL.10)**: both csch-forms re-derived from
  `F(x) = log(1 - e^{-x})` — exact.
- **(SOL.12)/(SOL.13)**: `lam|kappa_3| <= (5/2) s2` is TRUE — I proved
  it termwise myself (the comparison `psi(x) = (x csch x)^2 (5/2 - 2x
  coth x)` decreasing on the relevant range plus the sign argument via
  `x^3 csch^2 x coth x` decreasing), and block [A] confirms: max
  `lam k3/s2 = 2.1253` at the deep corner (consistent with the
  campaign's 2.1215/2.1303 W7 numbers). `5/168 = 0.029762 < 0.0298`
  exact. Caveat: the draft's own two-line route via (SOL.11) is a sketch
  — the written-out comparison should be added, but the mechanism named
  is the right one.
- **Corollary SOL.3**: the split `|e^{i a}(e^R - 1)| + |e^{i a} - 1|`
  with real `alpha` — correct.
- **Lemma SOL.4 structure**: `f` is real (conjugate-symmetry checked);
  (SOL.20) is the exact lattice inversion; the local/mid/crossover/far
  accounting is complete and single-counts the Gaussian tail; the range
  orderings `4 <= (2/7)sqrt(A)` (exact at `A = 196`), `4 < 0.8 sqrt(A)`,
  `t_0 <= 1.074 lam < pi` all hold at `m >= 700`. All E-table entries
  verified (block [C]) except the F4 item. Crossover/far `m`-monotonicity
  derivatives checked (`(j+1)/2m < 0.0176`; `1.5(j+1)/m < 0.0741`).
- **Lemma SOL.5**: interval arithmetic (SOL.38)–(SOL.45) all verified
  (block [C]); the `-(log f)'' = -f''/f + (f'/f)^2` bounds are used in
  the correct directions.
- **SOL.6 conversion**: (SOL.47) is the exact integral-remainder
  identity (re-derived); `sigma^2(e^{L/sigma^2} - 1)` bracketing via
  `x <= e^x - 1 <= x e^x` correct; `1.535 * e^{1.535/247.44} =
  1.544552 < 1.545`; the boxed `0.545 < 0.89` follows.
- **Interface**: the delivered form `|s2(r(k)-1) - 1| < 0.545` matches
  (S4)'s statement form exactly (same `s2`, same `r`, mirror handled);
  `0.545` sits far inside every quoted basin (block [F]:
  `0.545 < 0.89 < 0.89412`; wave6 basins `>= 0.920`).

## 6. Required repairs (in order of weight)

1. **(R1 = F1)** Extend the theorem to `m in [561, 699]` by executing the
   draft's own named fallback (re-run the C^2 chain at `m >= 561` with
   re-derived budgets; the local/mid split must move to
   `y* = (2/7)sqrt(A)` and every E-entry be recomputed — my block [E]
   sketch, deviation `0.7241 < 0.89`, says it closes). DELETE the
   "already closed W1 finite rung" paragraph — it is circular as
   written. Until then the draft does not discharge (S4) as consumed by
   `CL_composition_20260812.md` §2 step 1.
2. **(R2 = F2)** Prove (SOL.14): replace (SOL.15) by an honest envelope
   (`6.72 + 5.136 u/(1-u)` works and still yields `0.0018 < 0.0021`),
   with a real lemma for `|kappa_4| <= 6.72 s2/lam^2` and
   `|kappa_n| <= 1.07 (n-1)! s2/lam^{n-2}` (`n >= 5`) — the negative-side
   (uniform-regime) terms need explicit treatment. The current (SOL.15)
   display must not survive: it is unobtainable by the stated means.
3. **(R3 = F3)** Re-cite (SOL.5): "Lemma R.1 on W1; tier-2
   `c2 = 0.0871` + [A2] `c_A >= 0.35` on W2–W7
   (`0.0871*0.64*0.35 = 0.019510 >= 0.0176`)".
4. **(R4 = F4)** Fix `E_mid[0]` (`< 0.00072`), re-verify the total (it
   holds), and flag the three knife-edge margins for the numerics
   referee.
5. (minor) Write out the (SOL.12) comparison argument; state explicitly
   that `alpha` is real in Cor SOL.3; note that the `[561, 699]`
   sentence "This proves (S4) on precisely the range where the analytic
   INFL/QUADF bootstrap is needed" is false as stated (the bootstrap is
   consumed from `m = 561`; wave6 §5 re-verifies the basins at rows
   @ 561).

## 7. Script table (this referee's own; SAVED and RUN 2026-08-12)

| # | script (`referee_maths_sol_s4_scripts/`) | validates | key output (verbatim) |
|---|---|---|---|
| [S4R] | `ref_s4_checks.py` (`out_ref_s4_checks.txt`) | [A] exact cumulant checks (SOL.12, c4 <= 6.72, A/m window) at 10 (m, w) probes; [B] true-vs-abs-series remainder at 12 probes vs (SOL.14)/(SOL.15); [C] all V1–V8 constants at dps 40; [D] tier-2 crossover fix on W2–W7; [E] m = 561 structural failure + repair feasibility; [F] seed/basin interface | `max lam*k3/s2 = 2.12528 (OK)`; `w=623 u=0.2857: env_true=6.2079 env_absseries=8.2900 | (SOL.15) claim=7.0080 [abs-series fits: False]`; `E_mid[0] = 0.000710591 < 0.00071: False`; `E0/E1/E2 totals: True`; `X_max = 1.544552 < 1.545: True`; `W2: 0.019510 >= 0.0176: True`; `561: deviation bound 0.7241 < 0.89: True` |

*Class: mpmath dps-40 point evaluations and quadrature (house point-
evaluation class); the [B]/[A] blocks are exact closed-form cumulant sums
(negative-order polylogs are rational functions). Nothing here is a
certificate — findings F1–F4 are logical/textual and stand independent of
the numerics.*

## 8. Bottom line

The draft contains the first credible architecture for (S4) the campaign
has seen, and its `m >= 700` core survived a genuinely adversarial pass
on everything EXCEPT the two load-bearing gaps: the missing 139 integers
`[561, 699]` (claimed via a circular reading of the ledger) and the
asserted-not-proved remainder lemma with a refutable displayed envelope.
Verdict **MAJOR_ISSUES**: do NOT mark (S4) discharged on any range; a
revision executing R1–R4 is plausibly one focused session from a
SURVIVES-class artifact, with every downstream constant unchanged.

*End of referee_maths_sol_s4.md.*
