# Change log for main.tex — F2 upgrade, 2026-08-12

Integrator session, upgrading the paper's F2 content per the G2 campaign
results. Ground truth, in authority order:

- `phase2/bruhat/f2_drafts/g2_campaign_20260811/STATUS_wave5.md` (final
  ledger; §4 = the exact permitted claim, §3 = the bottom line)
- `phase2/bruhat/f2_drafts/g2_campaign_20260811/CL_composition_20260812.md`
  (Theorem CL-C: CL(79,20,0.89) at m >= 561 proved modulo (S1)–(S4);
  chain-verified composed constant C* = 18.2281 <= 20; §4 = the verbatim
  (S1)–(S4) statements and constants)
- `phase2/bruhat/f2_drafts/g2_campaign_20260811/theoremA_assembly_20260811.md`
  (the refereed Theorem A reduction: regions, constants, frozen CL spec,
  C_A, the unconditional upper bound)
- `phase2/bruhat/f2_drafts/g2_scripts/campaign_20260811/harness_m560/results_m560.txt`
  and `.../wave2_repairs/results_m540.txt` (exact harness, ALL PASS,
  4 <= m <= 560; the two files jointly carry all 557 rows)
- `phase2/bruhat/f2_drafts/g2_campaign_20260811/wp4_draft_composite.md` §0
  (band partition W1–W7 and tilt-frame notation, needed to state
  (S1)–(S4) self-containedly in paper notation)

Design constraints obeyed (STATUS_wave5 §4 prohibitions): the paper does
NOT say F2(a) is proved; does NOT call CL nearly proved; states (S1)–(S4)
explicitly as open with measured margins (including the thin 3.7%/3.9%
(S1) margins); all mathematical statements are self-contained in paper
notation (no pointers to internal campaign files); no internal process
jargon (waves, referees-by-name, agents) appears in mathematical
statements. Everything outside the F2 thread (title, authors, sections
1–5, F1, F3, verification tables, acknowledgments, bibliography) is
untouched.

---

## 1. Abstract — F2 sentence

**Old:**
> "...we prove an unconditional local limit theorem pinning its value near
> the center for every $m$, and state the resulting sharp asymptotic
> $\sigma_m^2(r_m-1) = 1-\tfrac{27}{25}m^{-1}+O(m^{-2})$ as a conjecture,
> one further uniformity lemma short of a full proof."

**New:**
> "...we prove an unconditional local limit theorem pinning its value near
> the center for every $m$, determine the global minimum exactly, in
> integer arithmetic, for every $m\le560$, and prove the sharp asymptotic
> $\sigma_m^2(r_m-1) = 1-\tfrac{27}{25}m^{-1}+O(m^{-2})$ conditional on a
> single explicitly stated core lemma on the exponentially tilted Mahonian
> distribution --- needed only for $m\ge561$, and itself reduced, with
> explicit constants throughout, to four explicitly stated open cumulant
> statements."

**Why:** STATUS_wave5 §4 (the permitted one-sentence claim: conditional
theorem, scope reduced to m >= 561 by exact computation, reduction to four
open statements); harness_m560 (the m <= 560 exact part).

## 2. Introduction, contribution (iii)

**Old:** "an asymptotic determination ... We state the exact asymptotic
order as a conjecture: a local limit theorem pinning the ratio near the
center is unconditionally proved for every $m$, and the resulting sharp
asymptotic is additionally supported by exact verification up to $m=150$."

**New:** "a determination --- conditional on a single explicitly stated
open lemma --- of how the minimum ... approaches 1 ...: a local limit
theorem near the center unconditionally for every m; the minimum
determined exactly in integer arithmetic for every m <= 560; the sharp
asymptotic proved conditional on one explicitly stated lemma
(Conjecture~\ref{conj:CL}), needed only for m >= 561, reduction complete
with every constant explicit; the lemma in turn reduced to four
explicitly stated open cumulant statements."

**Why:** same as item 1. Also removes the stale "m = 150" (superseded by
m <= 560; STATUS_wave5 §2/§3, harness_m560).

## 3. Section 6 (sec:F2) — the main upgrade

### 3a. NEW Theorem 6.2 (`thm:finite560`), "Exact finite-range theorem",
placed at the end of the "What is proved unconditionally" subsection,
with a following paragraph describing the harness factually.

Content: for every 5 <= m <= 560, in exact integer/rational arithmetic:
(i) argmin central at floor(N/2) (N odd: exact mirror tie); (ii)
r_m = r_m(floor(N/2)); (iii) sigma^2(r_m - 1) >= 187/216, equality iff
m = 6; (iv) sigma^2(r_m - 1) strictly increasing on 6 <= m <= 560,
value 0.998072... at m = 560, m(1 - sigma^2(r_m-1)) = 1.07935 there.
Plus the m = 4 exception (argmin = 2, varfit(4) = 91/108).

**Why / sources:** STATUS_wave5 §2 "G2 overall" ("Finite companions ...
unconditional theorems for 5 <= m <= 560 (C5 scope per the standing
erratum; m = 4 C2/C3 exception known)"); `results_m560.txt` line
`# OVERALL: PASS -- all of C1..C6 hold exactly for 4 <= m <= 560 (C2/C3
with the known m=4 exception; ...)` and its checkpoint
`varfit(560) = 0.998072591511`, mfit column 1.07935 at 560;
theoremA_assembly §4 block E (`varfit(4) = 91/108 = 0.842593 <
187/216`), §7 item 8 (C5 scope is 5 <= m, m = 4 exempt by design).

### 3b. DELETED: subsection "What remains open" in its entirety

Removed: the three-regime description with "the tilted middle regime is
the open one"; **Conjecture [F2, sharp asymptotic]** (`conj:F2` — the
label is retired); the "missing ingredient is a single further
uniformity statement" paragraph (including the "draft on file, not yet
independently refereed" clauses — those drafts are now the proved,
consumed machinery); Remark "[How we present this]" (built around the
stale m <= 150 / single-uniformity-lemma framing); Remark "[Location and
explicit constant]" (stale m <= 150 statements; see 3i for its
replacement).

**Why:** superseded wholesale by the conditional theorem and the
completed reduction (STATUS_wave5 §2–§4).

### 3c. NEW subsection "From the center to the global minimum: the
reduction" — tilt frame + Conjecture 6.3 (`conj:CL`)

- Tilt-frame paragraph: independent truncated-geometric variables
  U_j^lambda, S_lambda, mu(lambda), mean-matching tilt lambda(k),
  s^2(k), kappa_3, kappa_4, centered characteristic function phi,
  mirror symmetry, omega = m*lambda. Source: wp4_draft_composite §0
  (notation), restated in the paper's own symbols (omega instead of w to
  avoid collision with Weyl-group elements; \mathcal{W}_i for bands).
- **Conjecture 6.3 (Core lemma CL(79,20,0.89))**: for every m >= 561 and
  interior k with s^2 >= 79 and 4/m < lambda(k) <= 0.89:
  r_m(k) - 1 = s^{-2}(1 + theta*20/min(m, s^2)), |theta| <= 1.
  Source: the frozen spec, theoremA_assembly §3 (verbatim, both wp3-a2
  referees verified the spec arithmetic), with the scope restricted to
  m >= 561 and to the tilt band (4/m, 0.89] per CL_composition §0/§2
  (the sliver-final obligation) and STATUS_wave5 §2 ("the certified
  obligation is CL(79,20,0.89) for m >= 561").
- Follow-up remark: (a) s^2 >= 79 never binds (s^2 >= 1122800/7921 > 141
  on the band — wp4_composite Theorem A2(iii), quoted in CL_composition
  I1); (b) only the lower-bound half is consumed (theoremA_assembly §3);
  (c) why m >= 561: the reduction needs CL from m >= 401, and
  401 <= m <= 560 is discharged by the exact computation of Theorem
  6.2 (CL_composition §0 split — "no CL-type lemma is needed there at
  all").

### 3d. NEW Theorem 6.5 (`thm:F2`), "F2, sharp asymptotic — conditional"

Replaces old Conjecture [F2]. Statement: assume Conjecture CL; then
sigma^2(r_m - 1) = 1 - (27/25)m^{-1} + O(m^{-2}), equivalently
r_m - 1 ~ 36/m^3, in particular sigma^2(r_m-1) -> 1; explicit two-sided
error for m >= 561: 1 - B_m - C_A/m^2 <= sigma^2(r_m-1) <=
1 - B_m + 1.8/m^2 with C_A = 37997.85; upper bound unconditional for
m >= 180.

**Sources:** theoremA_assembly §0 (Theorem A statement + "PROVED
CONDITIONAL on exactly ONE named mathematical statement"), §2.4 (the
two-sided display; C_A closed flavor 37997.85 valid for all m >= 401,
hence on our stated scope m >= 561; UB constant 1.8/m^2 for m >= 180,
unconditional), STATUS_wave5 §2 "G2 overall" ("Theorem A ... PROVED
CONDITIONAL on exactly (S1)–(S4)" — presented in the paper as
conditional on CL, with CL <= (S1)–(S4) as the separate Proposition 6.8).

### 3e. NEW Remark 6.6 (`rem:reduction`), "Shape of the reduction, and
where the conjecture enters"

The four-region outline: (a) k = 1, pentagonal bound, >= 10^5;
(b) 2 <= k <= K_c, two-term bound, >= 1879; (c) deep tilt: floors
min(m,s^2) >= 79.5, s^2 <= 0.72711 sigma^2, lambda <= log(17/7) < 0.89,
CL consumed here and nowhere else, conclusion >= 1.0293; (d) small-tilt
window |omega| <= 4, window law, >= 1 - B_m - C_A/m^2. Ends with the
C_A size-honesty note (one lossy triangle-inequality step; measured
analogue about 5).

**Sources:** theoremA_assembly §2.3 (the R1a/R1b/R2/R3 table with
exactly these constants; K_c = min(7m/10, m-1) / m-1 per band), §4-C
(re-verified budget arithmetic 20/79.5 = 0.2516, conclusion 1.0293,
cap proof log(17/7) < 0.89), §6 "Size honesty" (truth anchor ~5.04 for
the dominant contribution to C_A).

### 3f. NEW subsection "Reduction of the core lemma to four cumulant
statements": bands, Table 4 (`tab:CLbands`), Conjecture 6.7 (`conj:S`)

- Band partition W_1..W_7 of omega = m*lambda in (4, 0.89m]:
  (4,5], (5,6], (6,8], (8,10], (10,20], (20,40], (40,inf), each
  intersected with {lambda <= 0.89}. Source: wp4_draft_composite §0
  (the campaign's W6b is printed as \mathcal{W}_6 in the paper — pure
  relabeling, same interval (20,40]).
- Normalized cumulants: tilde-kappa_3 = |kappa_3| lambda / s^2,
  tilde-kappa_4 = kappa_4 lambda^2 / s^2 (the composition note's
  r31/r42, renamed to avoid the paper's rho).
- Table 4 constants, copied verbatim from CL_composition §4:
  R_3 = 1.0/1.2/1.5/1.7/2.0/2.1/2.2;
  R_4 = 0.8/1.4/2.6/3.5/5.2/6.0/6.6;
  C_5 = 0.05/0.06/0.08/0.10/0.15/0.25/0.80;
  J_0 = 0.682942/1.10268/1.91562/2.53645/3.66793/4.17806/4.59597
  (caption notes the J_0 entries are six-digit displays of exact
  rationals archived in the repository — per CL_composition §4/I5).
- **Conjecture 6.7** states (S1)–(S4) verbatim in this notation, scope
  m >= 561, lambda in (4/m, 0.89]:
  (S1) tilde-kappa_3 <= R_3(W), tilde-kappa_4 <= R_4(W);
  (S2) |log phi(t) + s^2 t^2/2 + i kappa_3 t^3/6 - kappa_4 t^4/24|
       <= C_5(W) s^2 t^5 / lambda^3 on [0, lambda/2] (stated as one
       inequality — identical content to the composition's R5-form);
  (S3) tilde-kappa_3^2 - tilde-kappa_4/2 <= J_0(W);
  (S4) |s^2 (r_m(k) - 1) - 1| <= 0.89.
  Source: CL_composition §4, statement for statement.

### 3g. NEW Proposition 6.8 (`prop:CLred`), "Reduction of the core lemma"
+ assembly paragraph

Statement: (S1)–(S4) imply Conjecture CL; the composed chain delivers
18.23 in place of 20 for every m >= 561. Following paragraph: what each
statement prices ((S1)+(S3) the main term, (S2) the core remainder, (S4)
the self-consistency seed closing with strict contraction), everything
else proved with explicit constants; end-to-end machine re-verification
of the composed constant archived in the repository.

**Sources:** CL_composition §2 (Theorem CL-C: "CL(79, 20, 0.89)
restricted to m >= 561 ... PROVED MODULO (S1)–(S4)", composed constant
C*(m >= 561) = 18.2281 <= 20), §2 proof steps 1–5 (which hypothesis
feeds which step), §4 "Why the surface is exactly this", and the
chain-verification output
`g2_scripts/campaign_20260811/wave5_composition/out_compose_chain.txt`
("ALL CHECKS PASS: True"; "C*(m >= 561) = 18.2281 <= 20: True").
Per STATUS_wave5 §4 this assembled-implication claim (every input node
two-referee verified) is exactly the permitted paper claim.

### 3h. NEW Remark (`rem:S-evidence`) "Status and evidence for (S1)–(S4)"
and NEW Remark "What is claimed, and what is not"

- Evidence remark: all four open, none has a proof, all four
  load-bearing ("removing any one leaves no theorem" — STATUS_wave5 §3);
  the list moved in both directions under scrutiny (two earlier
  hypotheses proved outright and retired = SL3'-w discharged and SL4'-X
  proved; (S3)/(S4) added — STATUS_wave5 §2 "What wave 5
  removed/ADDED", phrased without campaign jargon). Margins, per
  CL_composition §4: (S1) measured 2.1215/6.3552 vs caps 2.2/6.6,
  headroom 3.7%/3.9%, large-m limits 2.1303/6.4113 — flagged as the
  thinnest margins in the reduction (the mandated honesty item);
  (S2) measured 0.0083–0.2104, slack factor 1.6–8;
  (S3) worst margin 32.6% at (m, omega) = (561, 5.0), plus the
  unavoidability fact (a point consistent with (S1) and kappa_4 >= 0 at
  which the fed estimate fails by 43% — Prop E.3, twice refereed);
  (S4) weak a-priori form of the conclusion (0.89 vs 20/min(m,s^2) <=
  0.036), listed separately "precisely because assuming it silently
  would overstate what is proved"; exact CL verification at m = 401/402
  on 260 adversarially chosen indices, 17x margin (CL_composition §5.5
  — stated with the honest "260 adversarially chosen", not "every").
- Claim-scope remark: unconditional = Theorems 6.1, 6.2, UB half of
  6.5; conditional = 6.5 on CL and nothing else, CL from (S1)–(S4) via
  6.8; open = (S1)–(S4), and the sub-4% margin is explicitly NOT
  treated as grounds for "close to proved" (STATUS_wave5 §3/§4
  prohibitions implemented in-text).

### 3i. REWRITTEN Remark "Location and explicit constant"

- "argmin central for 4 <= m <= 150 (exact check)" -> exactly central
  for 5 <= m <= 560 (Theorem 6.2).
- Old unproved "|argmin - N/2| = O(m) for larger m modulo the same gap"
  -> replaced by what the current reduction actually certifies:
  conditional on CL, the minimizer is localized to the small-tilt
  window |lambda(k)| <= 4/m (region (d) of Remark 6.6). The O(m) claim
  appears in no current ground-truth document and was dropped rather
  than carried.
- Third-difference positivity statement (5 <= m <= 56, no proof
  strategy) kept verbatim — independent of the harness upgrade.
- "r_m >= 1 + (187/216) sigma^{-2} ... exact for 5 <= m <= 150 and
  reduces, for m > 150, to the same gap above plus a constant-chasing
  step we have not carried out" -> exact for 5 <= m <= 560 (Theorem
  6.2(iii)); for m >= 561 conditional on CL, because the explicit lower
  bound of Theorem 6.5 exceeds 187/216 for every m >= 537; hence,
  granting CL, the sharp bound holds for every m >= 5 with equality
  only at m = 6. Sources: theoremA_assembly §4 block B (closed-flavor
  crossover m* = 537, "stays beyond: True") + STATUS_wave5 §2 ("G4:
  part-(c) band [401, 536] computation-closed"). The old
  "constant-chasing step" caveat is obsolete: the harness (to 560) now
  covers past the crossover (537).

## 4. Discussion, item 1

**Old:** "Prove Conjecture [F2] in full. ... this needs exactly one
further uniformity lemma: a bound on the tilted Mahonian characteristic
function's far-region decay ... Everything else needed ... is either
proved here (Theorem G1) or has draft proofs on file awaiting
independent referee review."

**New:** "Prove Conjecture [CL] --- that is, statements (S1)–(S4) of
Conjecture [S]." with: these four statements are the entire distance to
an unconditional theorem (far-region decay, crossover/mid-range bounds,
variance floors/caps, assembly, and m <= 560 all in place with explicit
constants); the measured margins locate the risk at (S1)'s deepest band
(< 4% headroom) — "where a proof attempt --- or a counterexample search
--- should begin."

**Why:** STATUS_wave5 §3 ("item 1 is the only remaining mathematics"),
§2 (the far-region machinery is now proved input, no longer "awaiting
review" — it is consumed by the reduction at two-referee status).

## 5. Untouched (verified)

Title, authors, abstract outside the F2 sentence, sections 1–5 (all
Weyl-group verification content, F1, tables 1–3), Theorem 6.1 (= G1) and
its preamble including the m <= 109 / m <= 229 exact-check ranges (those
concern G1's own verification, not the F2 harness), equation
(central-ratio) and its m = 50 confirmation sentence, section 7 (F3),
Discussion items 2–6 and closing paragraphs, Acknowledgments,
bibliography. Grep-verified: no remaining occurrence of "150",
"conj:F2", or the retired "uniformity lemma" framing anywhere in
main.tex.

## 6. Build

- The 2026-08-06 PDF was produced by pdfTeX 1.40.27 / TeX Live 2025 (per
  the old PDF's /Producer metadata). **No TeX Live installation exists on
  this machine** (pdflatex/latexmk absent from PATH, /usr/local/texlive,
  /Library/TeX, brew, conda — searched); the 08-06 build was evidently
  done elsewhere or the toolchain has since been removed.
- **Toolchain used today (documented difference): Tectonic 0.17.0**
  (installed via `brew install tectonic`), run as
  `tectonic -X compile main.tex` in `paper/submission/`. Tectonic runs
  the needed passes automatically; the compile is clean: exit 0,
  **0 unresolved references/citations**, 13 pages (was 11 — the F2
  section grew by the finite theorem, the conditional theorem, the
  reduction, and the (S1)–(S4) material). The only warnings are four
  pre-existing overfull-hbox warnings (lines ~357–517: Tables/Examples
  in sections 3–5, content untouched by this session).
- New environments render/number as: Theorem 6.2 (finite560),
  Conjecture 6.3 (CL), Theorem 6.5 (F2, conditional), Conjecture 6.7
  ((S1)–(S4)), Proposition 6.8 (reduction), Table 4 (band constants).

## 7. Notes for the co-authors' review

1. Neither of you has read the 2026-08-06 draft end-to-end; this session
   deliberately confined itself to the F2 thread (items 1–4 above) so
   your review of the rest is unaffected.
2. The one judgment call to ratify: Proposition 6.8 presents the
   (S1)–(S4) => CL implication as established. Ground truth: every input
   it consumes is two-referee verified and the composed constant is
   machine-re-verified end-to-end (CL_composition §1/§3), but the
   composition note itself still owes its own unit referee pass
   (CL_composition §5.4, STATUS_wave5 §3 item 2). If you want the paper
   even more conservative until that pass lands, demote Proposition 6.8
   to a claim with proof "archived in the repository" — the surrounding
   text already reads that way.
3. Per STATUS_wave5 §5 item 1, a human should read CL_composition §2 +
   §4 and confirm the (S1)–(S4) surface is acceptable as the paper's
   stated conditionality.
4. The repository-URL placeholders ("[repository URL to be added on
   submission]") are unchanged; the F2 artifacts referenced by the new
   text (harness logs, chain re-verification) live under
   `phase2/bruhat/f2_drafts/g2_scripts/campaign_20260811/` and should be
   included in whatever repository snapshot ships with the paper.

---

## 8. Fixes applied (review fix pass, 2026-08-12)

Three adversarial review reports on the F2 upgrade, all MINOR_FINDINGS:
`review_math_20260812.md`, `review_overclaim_20260812.md`,
`review_style_20260812.md`. Every finding was independently re-verified
against the ground-truth ledger (STATUS_wave5, CL_composition,
theoremA_assembly, harness results on disk) before being applied. Nine
edits to `main.tex`; PDF recompiled. No constant, scope, or claim status
moved.

### 8.1 Range phrasing "every m <= 560" -> "every 4 <= m <= 560"
(math F1 = overclaim Finding 1)

Re-verified on disk: `results_m560.txt` header "m = 4..560", single
`# OVERALL: PASS` line for 4 <= m <= 560, 557 rows; nothing computed for
m <= 3 (r_2 is a min over an empty index set). Applied at all five
occurrences of the phrase class:

- abstract ("determine the global minimum exactly ... for every
  $4\le m\le560$");
- contribution (iii);
- Section 6 preamble ("computed exactly for every $4\le m\le560$");
- reduction preamble ("Theorem 6.2 settles every $4\le m\le560$
  outright") — the overclaim reviewer suggested "5 <= m <= 560" here;
  applied as "4 <= m <= 560" instead, for uniformity and because
  Theorem 6.2's closing sentence fully determines m = 4 as well
  (argmin = 2, varfit(4) = 91/108 — harness row m = 4 and assembly
  block E carry it), so the artifacts back the 4-form;
- Discussion item 1 ("the whole range $4\le m\le560$ ... in place") —
  a fifth instance of the same phrase class not listed by either
  reviewer, fixed identically as part of the same finding.

### 8.2 "Exact verification of Conjecture CL itself at m = 401, 402"
reworded (math F2 = overclaim Finding 4 = style F2)

Re-verified: Conjecture 6.3 is stated for m >= 561; what REF-B verified
at m = 401/402 (260 adversarial interior indices, 0 violations, 17.1x
margin — STATUS_wave5 truth side, CL_composition §5.5) is the CL
inequality below that stated scope. New text in the (S4) bullet of
Remark 6.9: "Exact verification of the inequality of
Conjecture~\ref{conj:CL} at $m=401$ and $m=402$ (below its stated
range), on $260$ adversarially chosen interior indices, passes with a
$17\times$ margin".

### 8.3 (S2) evidence: W1 non-uniformity caveat added
(math F3 = overclaim Finding 2)

Re-verified against CL_composition §4 (S2): "W1's slack is w = 4.30-
class, NOT uniform to the band edge." Appended to the (S2) bullet of
Remark 6.9: "(the lowest band's slack was measured at interior probe
points, not uniformly to its edge)".

### 8.4 (S4) parenthetical: unstated fact made explicit (style F5)

Re-verified: min(m, s^2) = m on the band is proved input
(CL_composition §2 step 5, "[A2](iii)-bonus"), giving 20/561 = 0.0357
<= 0.036. The (S4) bullet now reads "...concludes
$20/\min(m,s^2)\le0.036$, since $s^2\ge m$ on this range".

### 8.5 Notation collision S_lambda vs S_r (style F1)

Re-verified: line-level collision is real ($S_r$ power sums in the
Section 6 preamble vs $S_\lambda$, $S_0$ in the tilt frame). Of the
reviewer's two options, applied the surgical one — a disambiguating
parenthetical inside the (new, this-session) tilt-frame paragraph:
"$S_\lambda:=\sum_{j=1}^m U^\lambda_j$ (not to be confused with the
power sums $S_r$ above)". The pre-existing power-sum notation at the
preamble was left untouched (renaming it is the co-authors' call).

### 8.6 Theorem 6.2 title (style cosmetic)

"[Exact finite-range theorem]" -> "[Exact finite range]" (removes the
"Theorem ... theorem" doubling; flagged as no-action cosmetic, applied
as harmless).

### 8.7 Findings applied with NO text change (recorded per instruction)

- **Proposition 6.8 epistemic status** (math §1 closing note, overclaim
  Finding 3, style F6): all three reviewers independently conclude the
  presentation is within the STATUS_wave5 §4 permitted claim and require
  no text change. No edit made. The open process items stand as before:
  co-author ratification per STATUS_wave5 §5 item 1 (read
  CL_composition §2 + §4), and the composition note's own unit referee
  pass; §7.2's demotion option remains available if the co-authors want
  the paper more conservative.
- **Style F3 (change-log paraphrase looseness, §3i):** recorded, not
  edited in place (the log above is kept as reviewed). For the record,
  the old main.tex text paraphrased in §3i read "the minimizing index
  satisfies $|\mathrm{argmin}-N/2|\le1$ for every $4\le m\le150$ (exact
  check)" — the $\le1$ form is what admitted $m=4$ ($|2-3|=1$). The
  diff summary itself was verified accurate by the style reviewer.
- **Style F4 (change-log §6 environment list incomplete):** completed
  here rather than by editing §6: the full new/renumbered list is
  Theorem 6.2 (finite560), Conjecture 6.3 (CL), Remark 6.4, Theorem 6.5
  (F2), Remark 6.6 (reduction), Conjecture 6.7 (S), Proposition 6.8
  (CLred), Remark 6.9 (S-evidence), Table 4 (CLbands), plus the two
  renumbered trailing remarks 6.10 ("What is claimed, and what is not")
  and 6.11 ("Location and explicit constant").

### 8.8 Build after fixes

Tectonic 0.17.0, `tectonic -X compile main.tex`: exit 0, 13 pages,
0 unresolved references/citations; only the four pre-existing
overfull-hbox warnings (lines 363/443/503/517, sections 3-5, untouched).
Numbering unchanged (aux-verified: 6.2/6.3/6.5/6.6/6.7/6.8/6.9, Table
4). `main.pdf` regenerated in place.
