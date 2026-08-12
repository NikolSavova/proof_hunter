# Adversarial style/completeness review — F2 upgrade of main.tex (2026-08-12)

*Read-only review pass on `main.tex` (as edited 2026-08-12) and
`change_log_20260812.md`. Reviewed against, in order: `STATUS_wave5.md`
(§4 permitted claim, §3 bottom line), `CL_composition_20260812.md` (§0/§2/§4/§5),
`theoremA_assembly_20260811.md` (§0/§2–§4/§6), and the harness results
(`harness_m560/results_m560.txt`, `wave2_repairs/results_m540.txt`).
Actions run: `git diff` on main.tex (8 hunks), grep audits, and a fresh
Tectonic 0.17.0 compile of a scratchpad copy of main.tex (main.tex and the
change log were not modified by this review).*

## Verdict: MINOR_FINDINGS

Nothing blocks the co-authors' review. All findings below are wording- or
notation-level; none moves a constant, a scope, or a claim.

## 1. Change-log faithfulness (verified against `git diff`)

The working-tree diff of `main.tex` against HEAD (`9b1d053`) has exactly
eight hunks: abstract (~line 72), contribution (iii) (~line 144),
five hunks spanning Section 6 (old lines 633–896), and Discussion item 1
(~line 977). Mapping:

| diff hunk | change-log item | faithful? |
|---|---|---|
| abstract F2 sentence | §1 | yes — old/new quotes match the diff verbatim |
| contribution (iii) | §2 | yes |
| thm:finite560 + harness paragraph | §3a | yes |
| deletion of "What remains open", conj:F2, "How we present this" | §3b | yes — all listed deletions confirmed gone |
| tilt frame + conj:CL + 3-notes remark | §3c | yes |
| thm:F2 | §3d | yes |
| rem:reduction | §3e | yes |
| bands + Table 4 + conj:S | §3f | yes |
| prop:CLred + assembly paragraph | §3g | yes |
| rem:S-evidence + "What is claimed" remark | §3h | yes |
| "Location and explicit constant" rewrite | §3i | yes (see finding F3 on a loose paraphrase) |
| Discussion item 1 | §4 | yes |

Nothing in the diff is unlisted; nothing listed is absent. The §5
"untouched" claim is confirmed by the hunk ranges (no edits outside
abstract / contribution (iii) / Section 6 / Discussion item 1), and the §5
grep claims are all true: zero occurrences of `150`, `conj:F2`, or
"uniformity" anywhere in main.tex.

## 2. Build verification (independent recompile)

- Tectonic 0.17.0 (`tectonic -X compile`) on a scratchpad copy: exit 0,
  no undefined references or citations, **13 pages** (`\@abspage@last{13}`)
  — all as the change log's §6 states.
- Warnings: exactly the four overfull-hbox warnings at lines 363/443/503/517
  (Tables/Examples in Sections 3–5, untouched by the edit) — matches the
  change log's "four pre-existing" claim; the new Table 4 and the new math
  displays introduce no new warnings.
- The shipped `main.pdf` (186,658 bytes, mtime 14:28) is byte-count
  identical to the fresh build — the committed PDF is in sync with the
  edited source.
- Numbering matches the change log §6 exactly (from the aux file):
  Theorem 6.1 (G1), Theorem 6.2 (finite560), Conjecture 6.3 (CL),
  Remark 6.4, Theorem 6.5 (F2), Remark 6.6 (reduction), Conjecture 6.7 (S),
  Proposition 6.8 (CLred), Remark 6.9 (S-evidence), Table 4 (CLbands).
- Label hygiene: no duplicate labels, no dangling `\ref`s, the retired
  `conj:F2` label is gone and unreferenced.

## 3. No-overclaim audit of the new text (all pass)

- The claim structure is exactly STATUS_wave5 §4's permitted sentence:
  conditional theorem on the single stated CL; scope reduced to
  $m\ge561$ by exact computation; reduction complete with explicit
  constants; CL reduced to four explicitly stated open statements; finite
  part ($5\le m\le560$) unconditional. No "F2(a) proved", no "nearly
  proved" (the "What is claimed" remark explicitly disclaims it), the
  (S1) margins 3.7%/3.9% are stated and flagged as the thinnest.
- Constants spot-checked against ground truth, all correct: Table 4 rows
  $R_3/R_4/C_5/J_0$ verbatim from CL_composition §4 (W6b relabeled
  $\mathcal W_6$, same interval, as the change log documents; band
  partition confirmed against wp4_draft_composite §0); 18.23 vs composed
  18.2281 (safe rounding); $C_A=37997.85$ closed flavor, valid $m\ge401$;
  UB $1.8/m^2$, $m\ge180$; region constants $10^5$/1879/79.5/0.72711/
  $\log(17/7)$/1.0293 and $K_c$ per theoremA_assembly §2.3/§4; crossover
  $m^\ast=537$ (closed flavor — consistent with the $C_A$ flavor the paper
  uses); varfit(560)=0.9980725915 and mfit 1.07935 per
  `results_m560.txt` row 560; $91/108$ at $m=4$; (S1) 2.1215/6.3552 vs
  2.2/6.6 with limits 2.1303/6.4113; (S3) 32.6% at $(561,5.0)$ and the
  43% unavoidability point; (S4) 260 indices / 17$\times$ at $m=401/402$
  (source: 17.1x — rounded down, safe); $s^2\ge1122800/7921>141$.
- The (S1)–(S4) statements are mathematically identical to
  CL_composition §4 under the declared renaming
  ($\tilde\kappa_3,\tilde\kappa_4$ for r31/r42; the (S2) one-inequality
  form is exactly the R5-form; sign conventions of the cumulant expansion
  check out).
- The mathematical statements are fully self-contained (tilt frame,
  bands, constants all defined in-paper); no campaign file, wave, or
  referee jargon appears in any mathematical statement. ("referee-audited"
  at lines 601–602 is pre-existing text in the G1 preamble, outside this
  diff and outside this review's scope.)

## 4. Findings (all minor)

**F1 — notation collision $S_\lambda$ vs $S_r$ (main.tex:594 vs 687–689).**
The Section 6 preamble (pre-existing, line 594) defines power sums
$S_r=\sum_{j=1}^m j^r$ and uses $S_4$ in the definition of $B_m$; the new
tilt-frame paragraph (line 687) defines $S_\lambda=\sum_j U^\lambda_j$ and
uses $\Pr(S_0=k)=I_m(k)/m!$ (line 689), where $S_0$ under the power-sum
reading would be $m$. Context disambiguates (Greek vs integer subscript,
probability context), but two distinct $S$-families now live in one
section. Suggested fix (co-author's call): rename the power sums (e.g.
$p_r$, touching only line 594) or add "(not to be confused with the power
sums $S_r$)" to the frame paragraph.

**F2 — scope-of-statement nit in rem:S-evidence, (S4) bullet
(main.tex:876–878).** "Exact verification of Conjecture~\ref{conj:CL}
itself at $m=401$ and $m=402$" — Conjecture 6.3 as stated is scoped
$m\ge561$, so these are verifications of its *inequality* at points
formally outside its stated range (they are inside the reduction's
original $m\ge401$ range, as Remark 6.4(c) explains). Suggested one-word
fix: "Exact verification of the inequality of Conjecture~\ref{conj:CL} at
$m=401$ and $m=402$…".

**F3 — change-log paraphrase looseness (change_log §3i, cosmetic).** The
old text read "the minimizing index satisfies $|\mathrm{argmin}-N/2|\le1$
for every $4\le m\le150$ (exact check)"; the change log paraphrases this
as "argmin central for 4 <= m <= 150 (exact check)". The transformation
described is accurate, but the paraphrase of the *old* text drops the
$\le1$ form (which is what made $m=4$, $|2-3|=1$, pass). Record-only; the
diff itself is the authority and is correctly summarized.

**F4 — change-log §6 environment list incomplete (cosmetic).** The "new
environments" list omits the three new numbered remarks (6.4, 6.6, 6.9)
and the two renumbered trailing remarks (6.10, 6.11). Every number it
does list is correct.

**F5 — unstated fact behind one parenthetical (main.tex:874–875,
record-only).** "(constant $0.89$ where Conjecture~\ref{conj:CL}
concludes $20/\min(m,s^2)\le0.036$)" silently uses the proved fact
$\min(m,s^2)=m$ on the band (CL_composition §2 step 5, "[A2](iii)-bonus");
a reader computing from the paper's stated floor $s^2>141$ would get
$0.14$. The number is correct per ground truth; if desired, add "(since
$s^2\ge m$ on this range)". Deep inside an evidence remark — acceptable
as is.

**F6 — already flagged, recorded here for completeness.** Proposition 6.8
presents (S1)–(S4) $\Rightarrow$ CL as established. This is within
STATUS_wave5 §4's permitted claim ("whose proof is assembled, with every
input verified by two independent adversarial referees, as an implication
from exactly four explicitly-stated open statements"), and the change log
(§7.2) already flags the residual unit-referee debt on the composition
note for co-author ratification, with a concrete demotion option. No
action from this review; the co-authors should ratify per STATUS_wave5 §5
item 1.

**Cosmetic (no action needed):** "Theorem 6.2 (Exact finite-range
theorem)" prints "theorem" twice; "(Exact finite range)" would read more
cleanly.

## 5. Style/tone assessment

The new text reads as written with the rest of the paper: same understated
register ("We therefore report the numerical evidence with its margins
rather than with optimism"), same honesty devices as Sections 3–5 (scope
disclaimers inside theorem titles, "not exhaustive" style caveats), same
`\subsection*` sectioning, amsart conventions, and en-route
cross-referencing. Forward references (Remark 6.4 to thm:F2 and
rem:reduction) resolve. No duplicated statements: CL and (S1)–(S4) are
each stated exactly once; the old conjecture's asymptotic display now
lives only inside Theorem 6.5.

*End of review_style_20260812.md.*
