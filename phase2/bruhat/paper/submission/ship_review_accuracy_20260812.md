# Ship review — lens: ACCURACY VS THE CAMPAIGN FINDINGS

**Target:** `/Users/sihaohuang/Desktop/Coding/proof_hunter/phase2/bruhat/paper/submission/main.tex` (14pp)
**Authorities read:**
`f2_drafts/g2_campaign_20260811/CLOSURE_PLAN_v2_20260812.md` (ledger),
`sol_comprepair_20260812.md` (+ reader's note), `sol_s6boot_20260812.md`,
`sol_s5cont_20260812.md`, `referee_maths_sol_s1.md`, `referee_numerics_sol_s1.md`,
`solref_numerics_wave4_hygiene_20260812.md`, `sol_s1/s2b/s3/s3consol`, `harness_m560_20260812.md`.
**Reviewer was read-only. No file under `submission/` or `f2_drafts/` was modified.**

## Verdict: DO_NOT_SHIP (in current form)

Findings A1–A3 are one-line edits, but until they are made the manuscript asserts, three
times and in exactly the places a referee reads for honesty (the "What is claimed, and what
is not" remark, the Discussion's *Proved unconditionally* bullet, and open problem 1), the
precise implication that adversarial review withdrew today. A4 restates a constant claim
that `sol_comprepair` explicitly withdrew. Fix A1–A5 and the paper is shippable; B-items
should be resolved or re-worded before submission; C-items are polish.

---

## A. Blocking — status claims that contradict the ledger

### A1. Three sentences still say (S1)–(S4) imply CL. This is the withdrawn false claim.

**`main.tex:957–958`** (Remark *What is claimed, and what is not*):
> "Proposition~\ref{prop:CLred} proves that (S1)--(S4) imply Conjecture~\ref{conj:CL}. Five of the six remain open."

**`main.tex:1058–1059`** (Discussion, *Proved unconditionally*):
> "Proposition~\ref{prop:CLred} proves that (S1)--(S4) imply Conjecture~\ref{conj:CL}."

**`main.tex:1101–1104`** (Open problems, item 1):
> "\textbf{Prove statements (S1)--(S4) of Conjecture~\ref{conj:S}, and hence Conjecture~\ref{conj:CL}.} Proposition~\ref{prop:CLred} gives this implication..."

**Why wrong.** `sol_comprepair_20260812.md` §Status: *"The former assertion (S1)∧(S2)∧(S3)∧(S4) ⟹ CL(79,20,0.89) (m≥561) is **withdrawn**"*; the honest implication is the boxed `(S1)∧…∧(S6) ⟹ CL`, and its closing line is *"Closing the old statements (S1)-(S4) alone would not close CL."* The reader's note confirms this finding is unaffected by the stale `(S1): OPEN` row. Prop. `prop:CLred` in the paper itself (line 886) correctly says (S1)–(S6) — so A1 also makes the paper self-contradictory. Additionally, in `main.tex:1101` the instruction to "prove (S1)" is stale: (S1) is proved (wave 6b, `sol_s1_20260812.md`, both referee lanes MINOR_REPAIRS).

**Fix.** Lines 957 and 1058: `(S1)--(S4)` → `(S1)--(S6)`. Line 1101: retitle to
"**Prove statements (S2)--(S6) of Conjecture~\ref{conj:S}, and hence Conjecture~\ref{conj:CL}**".

### A2. Open problem 1 sends readers to hunt a counterexample to a proved statement.

**`main.tex:1107–1109`:**
> "The smallest computed margins occur in the cumulant bounds of (S1) in the deepest band, where they are under $4\%$. A proof or counterexample search should begin there."

**Why wrong.** (S1) is PROVED with a rigorous interval certificate (referee's own computation
is the certificate of record). No counterexample can exist, and no proof is owed. Per
`referee_maths_sol_s1.md` §SOL.8 the certified W7 ceilings are `2.13031 / 6.41126`, and the
truth attack (`script [K]`, 90 probes, m up to 3000, band edges and the W7 deep corner)
found 0 violations.

**Fix.** Redirect the item: the smallest *remaining* risk is (S6) (per the ledger's own
"Honest read on difficulty": "(S6) is the riskier one… If a seventh obligation appears
anywhere, this is where"), and (S5)/(S4)'s `[561,699]` range. Delete "or counterexample".

### A3. Two headings/titles still carry the four-statement count.

**`main.tex:816`:** `\subsection*{Reduction of the core lemma to four cumulant statements}`
— the first line of that very subsection says *six*. Also "cumulant statements" is wrong:
(S4) is a ratio seed, (S5) a coverage certificate, (S6) a bootstrap closure; none is a
cumulant statement.

**`main.tex:904`:** `\begin{remark}[Status and evidence for (S1)--(S4)]` — the itemize
underneath covers (S1) through (S6).

**Fix.** → "Reduction of the core lemma to six statements"; → "Status and evidence for (S1)--(S6)".

### A4. The composed-constant claim is overstated; `< 20` was withdrawn today.

**`main.tex:886–888`** (Proposition `prop:CLred`):
> "Statements (S1)--(S6) of Conjecture~\ref{conj:S} imply Conjecture~\ref{conj:CL}, with a composed constant **strictly below 20** for every $m\ge561$."

**Why wrong.** `sol_comprepair` §Status: *"The previous full-range effective-constant claim
18.2281 < 20 is also withdrawn"*; §Constant accounting: *"the assembled theorem-level
constant is C\*(m≥561) = 20"*, reinstatable only if a landed (S5) certifies a strictly
stronger directed bound than `Row_W1 ≤ 1`. The landed candidate `sol_s5cont_20260812.md`
certifies exactly `Row_W1 ≤ 1` and states *"It does not claim the sampled value 0.416537."*

**Fix.** "…imply Conjecture~\ref{conj:CL}, with composed constant $20$ for every $m\ge561$."
Do not say "strictly below". (CL as displayed uses $\theta\in[-1,1]$ closed, so the
Proposition still delivers CL as stated.)

### A5. "The repository contains the complete chain" is not supportable for (S6).

**`main.tex:898–899`:**
> "The repository contains the complete chain and a machine re-verification of the resulting constant."

combined with **`main.tex:878–880`**, which defines (S6) as a property of
*"the self-consistency map used in the proof of Proposition~\ref{prop:CLred}"*.

**Why wrong.** `sol_s6boot_20260812.md` §SOL.2 (*"The exact bootstrap function is absent"*):
the intended `G` is not defined in any attached file — `d_He`, `d_q`, the branch numerators,
the branch-selection rule and the parameter cells are nowhere stated, and §SOL.3 exhibits
two exact convex functions matching every archived datum yet with *opposite* signs at the
seed endpoint `b = 89/100`. So (S6) as printed names an object the record does not contain,
and the "complete chain" claim (and the "machine re-verification of the resulting constant",
which re-verified the now-withdrawn 18.2281) overstates the archive. Separately, closure-plan
item **C** states `sol_comprepair` — the document that defines Prop. `prop:CLred` — is
"single-model and unrefereed… it needs two lanes before anything may cite it", which sits
badly with presenting `prop:CLred` as a Proposition.

**Fix.** Soften to what is archived, e.g. "The repository contains the band constants, the
per-band certificates, and the composition document; the bootstrap map of (S6) is not yet
specified in closed form there, which is part of why (S6) is open." And either downgrade
`prop:CLred` to a stated reduction pending its two referee lanes, or disclose the referee
status in a footnote.

---

## B. Should be fixed before submission

### B1. The (S6) evidence numbers are from parameter rows outside (S6)'s own domain.

**`main.tex:945–949`:**
> "(S6): The map satisfies $G(20/m)<20/m$ at the two thinnest rows ($0.0492<0.0499$ and $0.0421<0.0432$)…"

Those are $20/401 = 0.049875$ and $20/463 = 0.043197$ — i.e. the **W5 row at $m=401$** and
the **W1 row at $m=463$** (`sol_s6boot` §V1 transcribes exactly these:
`g401 = 0.0491712`, `g463 = 0.0421217`). `sol_s6boot` §SOL.7 and §V5:
*"the quoted W5 row at m=401 and W1 row at m=463 are not direct checks of (S6): both lie
outside its domain, m≥561 for W2–W7, m≥700 for W1"* and *"A check only at m=401 or m=463
fails this item unless accompanied by a proved domination theorem."*

**Fix.** State the provenance: "…at two rows ($m=401$ in $\mathcal W_5$, $m=463$ in
$\mathcal W_1$) that lie below the range in which (S6) is needed; a domination argument to
the stated range is among what is missing." Otherwise the sentence reads as in-range evidence.

### B2. "one of which we prove here" — no proof of (S1) appears in the manuscript.

Abstract `main.tex:90`, Contributions `main.tex:201`, Related work `main.tex:221–222`, and
`main.tex:818` all say the paper proves one of the six. Section `sec:F2` contains only
`main.tex:906–907` ("Statement (S1) has since been proved, by a bandwise argument with a
rigorous interval certificate") — an assertion, not a proof, inside a `conjecture`
environment. A referee will read "we prove here" as "in this paper".

**Fix.** "…one of which we have since proved (recorded in the accompanying repository)", or
add a short proof sketch / theorem environment for (S1).

### B3. Interval-arithmetic provenance is disclosed in one place only; two other claims still say "exact".

The corrected sentence at **`main.tex:899–902`** is accurate and well phrased, but it is
scoped to the Prop. `prop:CLred` chain. Two earlier claims are not covered:

- **`main.tex:676–679`:** "We also verified (a), with the same displayed constant, directly
  in **exact arithmetic** for every $4\le m\le109$. We verified the window law in (b)… for
  every $4\le m\le229$." Part (a) compares $p(k)$ against
  $Z(y)[1-\tfrac{B_m}{12}\mathrm{He}_4(y)]$ with $Z(y)=(2\pi\sigma^2)^{-1/2}e^{-y^2/2}$ —
  transcendental, so this cannot be exact-rational; it is directed-rounding interval work
  (the exact-integer part is the Mahonian coefficients only). Same for the window law, whose
  statement contains $\log r_m(k)$.
- **`main.tex:788`:** "the repository contains the explicit constants and **machine-verified
  certificates** for each step" (Remark `rem:reduction`, regions (a)–(d)) — same provenance
  question, no interval disclosure attached.

**Fix.** Replace "exact arithmetic" at 676–679 with "directed-rounding interval arithmetic
over exact integer Mahonian coefficients", and either move the 899–902 provenance sentence
earlier (start of §`sec:F2`) so it governs the whole section, or repeat it at 788.
Contrast: `main.tex:698` ("exact integer or rational arithmetic", Thm `finite560`) and
`main.tex:836–838` ("six-digit displays of exact rational constants") are correct as written.

### B4. The $m\ge561$ / $m\le560$ splice is asserted as citable; the ledger says it is not.

**`main.tex:764–766`:** "The exact computation in Theorem~\ref{thm:finite560} handles
$401\le m\le560$, so the conjecture is stated and needed only for $m\ge561$." Same claim in
the abstract (`main.tex:87–88`, "needed only for $m\ge561$") and Thm `thm:F2`.

`sol_comprepair` §3: the stronger campaign statement *"m ≥ 561 is the entire residual CL
obligation, because all smaller m have been discharged"* still depends on the **zero-referee**
hygiene overlay implementing $M_H = 560$; *"the finite/infinite splice must not be advertised
as a fully citable chain until the hygiene verifier lands."* Closure-plan item **D** repeats
this ("Still owed").

**Note in mitigation:** `solref_numerics_wave4_hygiene_20260812.md` exists (one lane) and
independently reproduces the union $\{4,\dots,560\}$ = 557 rows, $F_6 = 187/216$,
$F_{560} = 0.998072591511$, $\sigma_{560}^2 = 4\,891\,250$, and
$560(1-F_{560}) = 1.07934875384$ — every one of which the paper quotes correctly
(`main.tex:707–709`), and it is what forced the correct qualifier "strictly increasing for
$6\le m\le560$" (`main.tex:706`; $F_5 = 7/8 > 187/216 = F_6$). So the *numbers* are sound;
what the ledger says is missing is the second lane and the formal splice verifier.

**Fix.** Either land the verifier before submission, or add half a sentence to the
`conj:CL` remark: "the finite range is discharged by Theorem~\ref{thm:finite560} itself; we
do not rely on any further overlay for the splice." (If that is true it closes the gap; if
the splice consumes anything beyond `thm:finite560`, it must be disclosed.)

### B5. Band table W4/W5 boundary disagrees with the composition document.

**`main.tex:822–824` and Table `tab:CLbands`:** $\mathcal W_4=(8,10]$, $\mathcal W_5=(10,20]$.
**`sol_comprepair` §SOL.1 and §V1:** `W4 = 8<w≤12`, `W5 = 12<w≤20`.

The paper matches *every other* artifact (`sol_s1_20260812.md:14–17`, `sol_s3_20260812.md:27`,
`sol_s2b:837–838`, `sol_s3consol:1097–1104`, `referee_maths_sol_s1.md:65`,
`referee_numerics_sol_s1.md:50`, `s2c_briefing.md:108`), all of which use `(8,10]/(10,20]`.
So `sol_comprepair` is the outlier and the paper is very likely right — but since
`sol_comprepair` is the document that defines the six-statement list and the constant
accounting, the disagreement must be resolved before the table is printed. All of
$R_3, R_4, C_5, J_0$ in the paper's table match `sol_comprepair` exactly
($341471/500000 = 0.682942$, …, $459597/100000 = 4.59597$).

**Fix.** Confirm with the (S3)/(S2) certificate authors, then correct whichever document is
wrong. Also note `\mathcal W_7=(40,\infty)$ in the paper vs `(40, 89m/100]` in SOL.1 —
harmless given the $\lambda\le0.89$ intersection stated in the text, but worth aligning.

### B6. The "(S1) margins are the smallest in the reduction" framing needs reconciling.

**`main.tex:918–922`** quotes suprema $2.1215 / 6.3552$ (limits $2.1303 / 6.4113$) against
bounds $2.2 / 6.6$, margins "only 3.7% and 3.9%… the smallest in the reduction". These trace
to `CL_composition_20260812.md:267–268`. But `referee_maths_sol_s1.md:83, 190, 264` records
the *adopted* W7 targets as `2.71 / 8.17` (27.2% / 27.4% headroom) with an
(S2)-fallback pair `2.42 / 7.28` (~12%), and states the (S1) proof "survives either
resolution of the C5\*(W7) question". Which pair is operative depends on whether
$C_5(\mathcal W_7)$ is $0.80$ (the paper's table) or $0.50$.

**Fix.** Verify that $2.2/6.6$ is the pair the current composition consumes; if so, the
sentence is fine but should no longer be the paper's headline risk (A2). If `2.42/7.28` is
operative, both the table row and the margin percentages need updating.

---

## C. Nits

- **`main.tex:1111`:** "would also remove the $m=17$ restriction" — it is an $m\le17$
  restriction (`main.tex:624` gets this right).
- **`main.tex:878–880`:** the paper's (S6) is stated uniformly in $m$, band, and $\lambda$,
  whereas `sol_comprepair` (S6) is stated on $\Omega_B$ = {W2–W7, all $m\ge561$} ∪
  {W1, $m\ge700$}, the W1/$m\le699$ region being carried by (S5). The paper's version is
  strictly stronger (safe direction) but makes (S5) look redundant; consider matching $\Omega_B$.
- **`main.tex:794`:** region (c) uses $\min(m,s^2)\ge79.5$ while the (S4) bullet
  (`main.tex:934–935`) uses $s^2\ge m$, giving $20/\min(m,s^2)\le0.036$. Both true (SOL.3
  proves $s^2\ge m\ge561$); the weaker constant in (c) is merely conservative, but the
  inconsistency invites a referee question.
- **`main.tex:598`:** Theorem `thm:F1-smooth` lists $A_1$ among the groups; $A_1$ has no
  interval of length $\ge2$, so $\rho$ is undefined there. Vacuous, but drop it or say so.
- **Not an error, recorded for the authors:** the paper treats **(S2) as open**. The ledger's
  trajectory paragraph says "(S2) proved and replayed", but its table row records
  maths-lane MINOR_REPAIRS / numerics-lane MAJOR_ISSUES (provenance), and item **B** calls the
  remaining work "a recording task". The paper is therefore *conservative* on (S2), which is
  the safe direction — no change needed, but if (S2)'s provenance lands before submission the
  count "one of which we prove here" could become "two".

---

## What checked out clean

- Six-statement count is correct in the abstract (`:89–90`), Contributions (`:200–201`),
  §F2 lead (`:818`), Prop. `prop:CLred` (`:886`), Remark `rem:S-evidence` (`:909`),
  Remark *What is claimed* (`:958`, "Five of the six remain open"), and Discussion *Open*
  (`:1075`, "(S2)--(S6) remain open") — **only** the five A1/A3 locations are stale.
- (S1) is described as proved (`:853`, `:860–861`, `:906–907`) with the correct provenance
  ("bandwise argument with a rigorous interval certificate").
- The (S5)/(S6) origin story (`:911–916`) matches `sol_comprepair` §4 findings 1 and 2 verbatim
  in substance, including "the composition step had been relying on a finite sample of $\omega$
  and on a fixed-point ansatz".
- (S5) evidence figures: $0.4165$ at $m=561$ (`sol_s5cont:18`, `0.416537`) and $0.2601$ at
  $m=699$ (`referee_maths_sl4p_repaired.md:229`, `0.260103`), threshold $1$, direction correct.
- CL's hypotheses ($m\ge561$, $s^2\ge79$, $4/m<\lambda\le0.89$, constant 20, $\theta\in[-1,1]$),
  the $s^2\ge1122800/7921>141$ floor, and $20/561\le0.036$ all match the artifacts.
- (S3)'s sign convention ($\tilde\kappa_3^2-\tilde\kappa_4/2\le J_0$) and (S1)'s signed
  $\tilde\kappa_4$ (not $|\kappa_4|$) match `sol_comprepair` §SOL.2 clauses E2/E3.
- Theorem `thm:F1-smooth`'s $m\le17$ disclosure (`:602–608`) is exactly the disclosure the
  brief requires, and the $m\le7$ limit of the working notes is stated.
- Classical attributions are correctly not claimed: Mahonian log-concavity to Bóna /
  Hoggar–Kook with "We do not claim that result here" (`:213–216`, `:284–288`), and the
  Gaussian-binomial central ratio to Canfield–Janson–Zeilberger (`:216–219`).
- `thm:finite560` figures ($187/216$, equality iff $m=6$, strict increase for $6\le m\le560$,
  $0.998072\ldots$, $1.07935$, $m=4$ exception $91/108$) match the hygiene referee exactly.
