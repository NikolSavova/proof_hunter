# Ship review — internal consistency and shippability

**File:** `/Users/sihaohuang/Desktop/Coding/proof_hunter/phase2/bruhat/paper/submission/main.tex`
**Compiled:** `main.pdf`, 14 pp.
**Reviewer lens:** internal consistency after the 2026-08-12 edit passes.
**Date:** 2026-08-12.
**Verdict: MINOR_FIXES** — B1–B6 below are blocking (each is a one-line textual repair, but as
printed the paper asserts, twice and verbatim, the exact false claim that adversarial review
retracted today). Everything else is polish.

---

## 0. Build state — clean

* Rebuilt `main.tex` from scratch with `tectonic`. Two passes, converged. **No undefined
  references, no multiply-defined labels, no `??` in the output.** Every `\ref` resolves.
* The extracted text layer of my fresh build is **byte-identical** to the shipped `main.pdf`
  (modulo the `\date{\today}` stamp). **The shipped PDF is current with the source** — the edits
  made today are in the compiled artifact.
* Only warnings: three Overfull \hbox (see P9) and three cosmetic hyperref "Token not allowed in a
  PDF string" notices from math in section titles. No meaningful LaTeX warnings.
* **No `TODO` / `FIXME` / `XXX` / `\textcolor` marker survives in the rendered text.** (One dead
  macro definition remains in the source — see P8.)
* Numbering is coherent throughout. Shared `theorem` counter, `[section]` reset: Thm 4.1, 4.3,
  Prop 4.7, Conj 5.1, Ex 5.2/5.3, Thm 5.5, Conj 5.6, Thm 6.1/6.2, Conj 6.3, Thm 6.5, Conj 6.7,
  Prop 6.8, Obs 7.1 — all sequential, no gaps, no duplicates.
* **Numbers independently re-verified and all correct:** Table 1's `#intervals` column sums to
  exactly 1,079,490,991 (matches abstract, intro, Thm 4.1, Discussion); Table 3 sums to 64,944
  seeded and 60,000 random = 124,944 (matches Prop 4.7 and the abstract); every `|W|` in Tables 1–2
  is right; **every min-ratio and minimizing index in Tables 1 and 2 matches an independent
  computation of ρ([e,w₀]) from the degree products** (A₇ 1.054250@14, A₈ 1.038942@18,
  A₉ 1.028950@22, A₁₀ 1.022102@27, D₇ 1.025574@21, D₈ 1.017122@28, E₇ 1.011829@31, D₄ 392/345@5,
  D₅ 1.069459@10, D₆ 1.040703@15, E₆ 1.028446@18); Remark 4.4's 919681/872356 and 65523/64757
  confirmed; Example 5.2's 8/7 and 968/897 confirmed; Example 5.3's 392/345, 58/51 and gap 2/1955
  confirmed.

---

## 1. BLOCKING — the (S1)–(S6) correction did not reach four places

### B1. The retracted "(S1)–(S4) imply CL" claim is still printed, twice, verbatim

`main.tex:957` (Remark 6.10, PDF p. 11) and `main.tex:1058` (Discussion, "Proved
unconditionally.", PDF p. 12), identical sentence in both:

> "Proposition~\ref{prop:CLred} proves that (S1)--(S4) imply Conjecture~\ref{conj:CL}."

**Why wrong.** Proposition 6.8 as actually stated (`main.tex:886`, PDF p. 10) says
"Statements (S1)–(S6) … imply Conjecture 6.3." These two sentences contradict the proposition they
cite, from one paragraph and one page away respectively. This is precisely the pre-correction claim
that today's adversarial review found FALSE and that `CLOSURE_PLAN_v2_20260812.md` and
`sol_comprepair_20260812.md` retracted ("Thus there are **six atomic open statements**, not four…
Closing the old statements (S1)–(S4) alone would not close CL"). A duplicate-sentence scan finds
this is the *only* exact duplicate pair in the manuscript — it is a single stale sentence that was
propagated twice and missed twice.

The damage is compounded by placement: `main.tex:1058` sits under the heading **"Proved
unconditionally"**, so the Discussion's logical-status breakdown — the one place a referee looks to
audit status — is where the false implication is asserted most confidently.

**Fix.** In both places: `(S1)--(S4)` → `(S1)--(S6)`.

### B2. Further-work item (1) asks the reader to prove the wrong set, including the proved one

`main.tex:1101-1102` (PDF p. 13, item (1)):

> "**Prove statements (S1)--(S4) of Conjecture~\ref{conj:S}, and hence Conjecture~\ref{conj:CL}.**
> Proposition~\ref{prop:CLred} gives this implication…"

**Why wrong.** Two errors in one sentence. (a) (S1)–(S4) does not give the implication (B1).
(b) (S1) is *proved* — Remark 6.9, three pages earlier, says so, and Conjecture 6.7's own title says
"(S1) is now a theorem". The paper's headline research direction therefore instructs the reader to
prove a theorem it has already proved, and omits (S5) and (S6), the two genuinely new obligations.

**Fix.** "**Prove statements (S2)--(S6) of Conjecture~\ref{conj:S}, and hence
Conjecture~\ref{conj:CL}.**"

### B3. Subsection heading says "four"; the sentence under it says "six"

`main.tex:816` (PDF p. 9):

> `\subsection*{Reduction of the core lemma to four cumulant statements}`
> "We reduce Conjecture~\ref{conj:CL}, with explicit constants throughout, to **six** statements
> about the tilted law, five of which remain open."

**Why wrong.** Heading and its first sentence contradict each other on the same rendered line. Also
"cumulant" is no longer accurate: (S5) is an ω-continuum coverage certificate and (S6) is a
fixed-point closure statement; neither is a cumulant bound.

**Fix.** `\subsection*{Reduction of the core lemma to six statements}`.

### B4. Remark 6.9's title still scopes to (S1)–(S4)

`main.tex:904` (PDF p. 10):

> `\begin{remark}[Status and evidence for (S1)--(S4)]`

**Why wrong.** The remark's body runs bullets for (S1), (S2), (S3), (S4), **(S5)** and **(S6)**, and
its own text explains that (S5) and (S6) were added today. The title contradicts the body.

**Fix.** `[Status and evidence for (S1)--(S6)]`.

### B5. Proposition 6.8 claims a composed constant "strictly below 20" — that claim was withdrawn

`main.tex:888` (PDF p. 10):

> "…imply Conjecture~\ref{conj:CL}, **with a composed constant strictly below 20** for every
> $m\ge561$."

**Why wrong.** `sol_comprepair_20260812.md` explicitly withdraws it:

> "The previous full-range effective-constant claim 18.2281 < 20 **is also withdrawn**: under the
> minimal form of (S5) below, the assembled full-range constant is **20, not a certified strict
> improvement**."

and its "Constant accounting" section concludes `C*(m≥561) = 20`. The strict-improvement figure
survives only as corroborative evidence on a sampled W₁ grid and on the m ≥ 700 analytic tail. So
the paper asserts a strengthening that the authoritative composition document retracted in the same
pass that produced (S5) and (S6) — the same edit that this sentence should have been caught by.

**Fix.** Delete the clause, or replace with "…imply Conjecture~\ref{conj:CL} with composed constant
$20$, i.e.\ exactly $\mathrm{CL}(79,20,0.89)$, for every $m\ge561$."

### B6. The "weakest link" is identified as (S1) — the one statement that is proved

Two places point the referee's and the reader's attention at (S1)'s 3.7 %/3.9 % margins as the
paper's most fragile point:

* `main.tex:959-960` (Remark 6.10, PDF p. 11): "the numerical margins in Remark~\ref{rem:S-evidence},
  **one of which is under $4\%$**, do not constitute a proof."
* `main.tex:1107-1109` (Discussion item (1), PDF p. 13): "The smallest computed margins occur in the
  cumulant bounds of **(S1)** in the deepest band, where they are under $4\%$. **A proof or
  counterexample search should begin there.**"

**Why wrong.** The under-4 % margins belong to (S1), which Remark 6.9 states has been proved by a
bandwise argument with a rigorous interval certificate. Directing a *proof or counterexample search*
at a proved statement is incoherent, and framing a proved statement as the reason the evidence "does
not constitute a proof" misdirects the reader away from the statements that actually block the
result. Per Remark 6.9's own bullets, the real soft spots are (S5) (a coverage gap, not a margin
gap: "the available checks are a finite ω-grid") and (S6) (convexity, endpoint bounds and the
extremal-row reduction all still required).

**Fix.** Remark 6.10: "the numerical margins in Remark~\ref{rem:S-evidence} do not constitute a
proof; for (S5) the gap is coverage rather than margin." Discussion item (1): "The tightest
constants in the reduction sit in the now-proved (S1); among the open statements, (S5)'s missing
ω-continuum and (S6)'s uniform closure are where a proof effort should begin."

---

## 2. Table ↔ text mismatches

### T1. The list of groups where a proper interval ties [e,w₀] omits D₄ and D₅ (and A₃)

Table 1 (`main.tex:398-400`) annotates **D₄**, **D₅** and **D₆** as "proper (ties $[e,w_0]$)".
But both places that enumerate the tie cases list only four groups:

* `main.tex:540-541` (Conjecture 5.1, PDF p. 6): "Proper intervals may tie this minimum (observed
  for $A_5,A_6,A_7,D_6$ in the exhaustive tier…)"
* `main.tex:588-589` (Remark 5.4, PDF p. 7): "in $A_5,A_6,A_7,D_6$, a specific proper interval ties
  it."

**Fix.** Both lists → "$A_3,A_5,A_6,A_7,D_4,D_5,D_6$" (A₃ per T2 below).

### T2. Table 1's A₃ row reports a proper minimizing interval with no "ties" annotation

`main.tex:388` (PDF p. 5):

> `$A_3$ & 24 & 213 & 1.388889 & $[e,12321]$, $k=2$ \\`

**Why wrong.** `12321` has length 5, while ℓ(w₀(A₃)) = 6 — so this is a **proper** interval, and it
is the only proper-witness row in Table 1 carrying no "(ties $[e,w_0]$)" tag (compare A₅, A₆, A₇,
D₄, D₅, D₆). As printed, the A₃ row states that a proper interval attains the global minimum of a
simply-laced irreducible group, which reads as a **counterexample to Conjecture 5.1 on the paper's
own data page** — a referee will stop there. In fact it is a tie: I computed
ρ([e,w₀(A₃)]) = 25/18 = 1.388889 at k = 2 from the Mahonian sequence (1,3,5,6,5,3,1), exactly the
reported value and index.

**Fix.** `$[e,12321]$, proper (ties $[e,w_0]$), $k=2$`, and add A₃ to the T1 lists.

### T3. Table 3's "margins 4–8" is missing its unit

`main.tex:492-493` (PDF p. 6), note column: "margins 4--8". §7 (`main.tex:1015-1016`, PDF p. 12)
states the same quantity as "the closest non-equality margins in the checked cases are $4$--$8\%$".

**Fix.** "margins 4--8\%" in both seeded rows.

### T4. §3's blanket arithmetic claim contradicts §6's interval-arithmetic disclosure

`main.tex:316-317` (PDF p. 4, opening sentence of Computational methodology):

> "**All computations** use exact integer (arbitrary-precision) arithmetic; no claim labeled a
> theorem uses floating point."

`main.tex:899-902` (PDF p. 10):

> "Those computations use **directed-rounding interval arithmetic** together with exact integer and
> rational arithmetic where stated; they are **rigorous modulo the interval library**, and we do not
> claim they are exact-rational throughout."

**Why wrong.** §3's sentence is unqualified and is the first statement about arithmetic rigour a
referee meets; the correcting disclosure lands 580 lines and six pages later. Two intermediate
sentences also advertise the strong reading without the caveat: `main.tex:238-239` ("exact-arithmetic
result logs, and machine-checked numerical certificates for the proved claims") and `main.tex:788`
(Remark 6.6: "machine-verified certificates for each step"). The (S1) proof itself rests on "a
rigorous interval certificate" (`main.tex:907`). This is the residue of the "exact rational
certificates" wording corrected today: the correction landed in one place but the global claim was
left standing.

**Fix.** Scope §3: "All computations reported in this section and in Section~\ref{sec:results} use
exact integer (arbitrary-precision) arithmetic… The interval-arithmetic certificates supporting the
Section~\ref{sec:F2} reduction are described separately there." Add "(see
Section~\ref{sec:F2})" to the Introduction sentence at `main.tex:238`.

---

## 3. Edit-pass residue and polish

**P1. Comma-then-new-sentence after four displayed equations.** Each display ends with `,` and the
next word starts a new sentence with a capital, rendering as a broken sentence:

| Location | Ends | Next word |
|---|---|---|
| `main.tex:299-300` | `…+5t^6+t^7,\]` | "Thus the rank sequence is…" |
| `main.tex:572-574` | `…\approx0.00102,\]` | "Thus a proper Bruhat interval…" |
| `main.tex:687-689` (eq. (1)) | `…+O(m^{-2}),\]` | "Exact Mahonian data at $m=50$…" |
| `main.tex:995-997` | `…(m-1\text{ interior 2's},\ m\ge4),\]` | "Each observed interval…" |

**Fix.** Trailing `,` → `.` in all four.

**P2. Semicolon followed by a capitalized sentence, with a doubled space.** `main.tex:801-802`
(PDF p. 9, region (c)): "…$\lambda(k)\le\log(17/7)<0.89$, all proved; **This** is the only point at
which we use Conjecture~\ref{conj:CL}; it gives…". **Fix.** "…all proved. This is the only point at
which we use Conjecture~\ref{conj:CL}; it gives…".

**P3. Double punctuation on all four Discussion labels.** PDF p. 12 renders "Proved
unconditionally**.:**", "Proved conditionally**.:**", "Conjectured or empirical**.:**",
"Open**.:**" — the description style appends a colon to a label that already ends in a period. §3's
description list (`main.tex:344-353`) has no such artifact because its labels have no trailing
period, so the paper is inconsistent with itself. **Fix.** Drop the periods inside `\item[...]` at
`main.tex:1046, 1061, 1067, 1075`.

**P4. Three uncited bibliography entries.** `butler1990` **[7]**, `sagan1992` **[8]**,
`suwangyeh2011` **[9]** (`main.tex:1187-1198`) appear in the reference list but are cited nowhere —
references [7]–[9] never occur in the body. Almost certainly orphaned when the Related-work
paragraph on q-log-concavity was rewritten. **Fix.** Cite them where q-log-concavity is discussed
(`main.tex:211-222`), or delete.

**P5. "the $m=17$ restriction" should be "$m\le17$".** `main.tex:1111` (PDF p. 13, item (2)):
"Proving Conjecture~\ref{conj:staircase} would also remove **the $m=17$ restriction** in type $A$."
Theorem 5.5 and Remark 5.7 both state the restriction as $m\le17$.

**P6. Theorem 5.5 includes $A_1$, where ρ is undefined.** `main.tex:596-598`: "rank $\le 6$
($A_1,\dots,A_6,D_4,D_5,D_6,E_6$)". ρ is defined only for ℓ(u,v) ≥ 2 (`main.tex:266-269`) and
ℓ(w₀(A₁)) = 1, so the A₁ clause is vacuous at best. **Fix.** Start the list at $A_2$.

**P7. Theorem 6.2 range vs. how it is cited.** Theorem 6.2 is stated "For every $5\le m\le560$",
with m = 4 handled in a trailing sentence; three places cite it as covering $4\le m\le560$
(`main.tex:84, 194, 693, 1054`). Not false, but a referee checking the theorem statement against the
abstract will bounce. **Fix.** Either fold m = 4 into the theorem hypothesis with the stated
exception, or write "for every $4\le m\le560$ (Theorem~\ref{thm:finite560} and the remark
following)".

**P8. Dead editorial scaffolding in the shipped source.** `main.tex:33` defines
`\newcommand{\TODO}[1]{\textcolor{red}{\textbf{[TODO: #1]}}}`, now unused — `xcolor` is loaded only
for it. `main.tex:1157` carries the comment "% Add acknowledgment of specific colleagues/advisors if
applicable." Neither shows in the PDF, but both ship in an arXiv source bundle. **Fix.** Delete both
lines (and `\usepackage{xcolor}` if nothing else needs it).

**P9. Overfull boxes.** Table 3 overruns the text block by **33.36 pt ≈ 0.46 in**
(`main.tex:484-496`); on PDF p. 6 the "(1,2,2,2,1) pattern" note visibly runs past the right margin,
past the running-header rule. Two smaller ones: `main.tex:410-416` (7.84 pt) and
`main.tex:549-556` (14.59 pt). **Fix.** Table 3 to `\footnotesize` or shorten the design/note column
strings; the other two will resolve with minor rewording.

**P10 (optional, ledger completeness).** The (S6) evidence bullet (`main.tex:945-949`) lists
convexity of the branches, directed endpoint bounds, and the extremal-row reduction as outstanding.
`sol_comprepair_20260812.md` records one more: "**No exact bootstrap function**, seed-endpoint sign
certificate, or uniform extremal-row reduction has landed." The paper's (S6) statement — "the
self-consistency map used in the proof of Proposition~\ref{prop:CLred}" — implies the map is pinned
down, which the ledger does not support. Consider adding "an explicit form for $G$" to the list of
what is still required.

---

## 4. What I checked and found consistent

Recorded so these are not re-checked downstream.

* Abstract, Introduction contribution (iii), the §6 reduction paragraph, Remark 6.10 and the
  Discussion "Open" item all agree on **six statements, one proved, five open** — the count is right
  everywhere; only the four scoping errors in §1 above are stale.
* Theorem 6.5 (F2) is labelled conditional in its own title, in the abstract, in contribution (iii),
  in the Introduction, and in the Discussion's "Proved conditionally" item; the unconditional
  upper-bound half is consistently qualified at m ≥ 180, matching m₁(1) = 180 in Theorem 6.1(b).
* Conjecture 6.3's parameters CL(79, 20, 0.89) match its hypotheses (s² ≥ 79, constant 20,
  λ ≤ 0.89) and Conjecture 6.7's preamble λ ∈ (4/m, 0.89].
* The m ≥ 561 / m ≥ 401 / 401 ≤ m ≤ 560 splice in Remark 6.4 is self-consistent, and the four
  regions (a)–(d) in Remark 6.6 match "four regions" in its own text.
* Theorem 5.5's reliance on the cited classical factorization for the type-A m ≤ 17 clause **is**
  disclosed in the theorem itself ("Our working notes verify that factorization computationally only
  through $m\le7$") and again in the Discussion.
* Classical attributions are correctly not claimed: Mahonian log-concavity credited to Bóna and to
  Hoggar/Kook with an explicit "We do not claim that result here" (`main.tex:216`, `main.tex:286-288`);
  the Gaussian-binomial central ratio credited to Canfield–Janson–Zeilberger (`main.tex:216-218`).
* Table 2's footnote markers (* and †) both resolve; Theorem 4.3's A₁₀ prose matches the "11/65"
  cell; Remark 4.6's discarded-attempt accounting matches Prop 4.7's "#intervals counts only …
  actually checked".
* Observation 7.1's "(m − 1 interior 2's, m ≥ 4)" is arithmetically correct for I₂(m), and its
  m ∈ {4,6} conclusion matches the witnesses listed in the following paragraph and in Table 1.
* Remark 3.1's E₆ missing-witness disclosure is consistent with Table 1's E₆ cell and does not
  undercut Thm 4.1; Remark 5.4's "in each case [e,w₀] attains the minimum" holds for E₆ because the
  recorded 1.028446 equals ρ([e,w₀(E₆)]) (verified).
