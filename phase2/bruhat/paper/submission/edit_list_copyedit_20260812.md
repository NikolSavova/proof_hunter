# Copyedit list — main.tex — 2026-08-12

Prose-only edits per `style_references_20260812.md`. No mathematical content, constants,
numerals, labels, or status claims are altered. OLD strings are exact (including line
breaks) and unique in `main.tex`. Ordered best-first. Flags for changes that would have
touched mathematics are at the end.

---

EDIT 1  [Abstract]
OLD: $D_4$--$D_6$, $E_6$, $F_4$, and $G_2$. We checked
$1{,}079{,}490{,}991$ Bruhat intervals
NEW: $D_4$--$D_6$, $E_6$, $F_4$, and $G_2$: we checked
$1{,}079{,}490{,}991$ Bruhat intervals
WHY: Smooths the seam between two "We ..." sentences; the count is the substance of the verification claim, not a new topic (rulebook 16, repeated openers).

EDIT 2  [Abstract]
OLD: with explicit constants throughout, to six explicitly stated statements
about the tilted law
NEW: with explicit constants throughout, to six statements
about the tilted law
WHY: Three "explicit(ly)" in one sentence; "explicitly stated statements" jangles (Halmos rule 4); matches the Section 6 phrasing "six statements about the tilted law".

EDIT 3  [Introduction, definition paragraph]
OLD: Brenti's Conjecture 2.11 in his 2024 survey of open problems on Coxeter
groups and unimodality~\cite{brenti2024open} asks whether this holds for
NEW: Conjecture~2.11 of Brenti's 2024 survey~\cite{brenti2024open} asks whether this holds for
WHY: The survey title lives in the bibliography and reappears in full in Example~\ref{ex:H3}; trimming reduces reader resistance (Halmos rules 3, 4).

EDIT 4  [Introduction, trend paragraph]
OLD: Taken alone, this can suggest that log-concavity
NEW: Taken alone, this might suggest that log-concavity
WHY: Calm graded hedging ("might suggest") over the awkward "can suggest" (rulebook 18).

EDIT 5  [Introduction, type-A paragraph]
OLD: which is what makes the candidate extremal
ratio tractable in type $A$.
NEW: which is what makes the candidate extremal ratio tractable.
WHY: "In type $A$" opens the paragraph and the next sentence opens "The type-$A$ analysis"; three occurrences in three sentences (repeated openers/doubled words).

EDIT 6  [Introduction, trend paragraph]
OLD: Along the full type-$A$ intervals, the central
ratio instead approaches $1$ from above
NEW: For the full type-$A$ intervals, the central ratio instead approaches $1$ from above
WHY: "Along ... intervals" is a spatial preposition misapplied to a family of intervals; plain idiom.

EDIT 7  [Introduction, extremal-conjecture paragraph]
OLD: The extremal conjecture is the structural proposal behind the paper. It
NEW: The extremal conjecture is the structural proposal of this paper. It
WHY: "Behind the paper" reads as concealed rather than central; plain English (rule 14).

EDIT 8  [Contributions preamble]
OLD: \subsection*{Contributions} Our contributions have four parts. We
NEW: \subsection*{Contributions} Our contributions fall into four parts. We
WHY: Idiom; contributions do not "have" parts.

EDIT 9  [Contributions (iii)]
OLD: explicit, and reduce the lemma in turn to six explicitly stated
statements about the tilted law
NEW: explicit, and reduce the lemma in turn to six statements about the tilted law
WHY: "Explicitly stated statements" doubling; "explicit" already appears earlier in the sentence (Halmos rule 4).

EDIT 10  [Preliminaries, ratio definition]
OLD: All $a_k([u,v])>0$ for Bruhat intervals, so we may define the
NEW: For a Bruhat interval, each $a_k([u,v])$ is positive, so we may define the
WHY: Readable mathspeak — the clause has no English verb; "$>0$" was serving as the verb (Bertsekas rule 8).

EDIT 11  [Example ex:H3]
OLD: arXiv:2410.09897 PDF. The source gives the Coxeter parameters
$m(s_1,s_2)=5,\,m(s_2,s_3)=3$, and $7^2=49<5\cdot10=50$. The rank-2
NEW: arXiv:2410.09897 PDF. The rank-2
WHY: The deleted sentence repeats verbatim the parameters and the failing comparison already displayed earlier in this example, and the example's first sentence already records the primary-source check (Halmos rule 4; seam from a mechanical accuracy edit).

EDIT 12  [Computational methodology, validation]
OLD: order $|\W|$; length $\equiv$ number of inversions (root-system definition)
for every enumerated element; Poincar\'e polynomial $\equiv$ the
degree-product formula $\prod_i[d_i]_q$;
NEW: order $|\W|$; agreement of the length function with the number of inversions (root-system definition) for every enumerated element; agreement of the Poincar\'e polynomial with the degree-product formula $\prod_i[d_i]_q$;
WHY: "$\equiv$" as the verb of a prose clause; English where English is clearer (rules 10, 14).

EDIT 13  [Computational methodology, engines]
OLD: The generic Cartan-matrix engine \texttt{weyl.py} builds any finite
Weyl group directly from its Cartan matrix
NEW: The generic engine \texttt{weyl.py} builds any finite Weyl group directly from its Cartan matrix
WHY: "Cartan-matrix engine ... from its Cartan matrix" doubles the phrase within one sentence.

EDIT 14  [Computational methodology, engines]
OLD: allowing us
to examine thin slabs in groups that cannot be enumerated exhaustively.
NEW: allowing us to examine thin slabs in groups too large to enumerate exhaustively.
WHY: Replaces an agentless passive relative clause with the concrete reason (rule 9).

EDIT 15  [Remark rem:e6segment]
OLD: after an
earlier single-pass process was killed.
NEW: after an earlier single-pass run was terminated prematurely.
WHY: "Killed" is systems jargon; plain English for the combinatorialist reader (Halmos rule 2).

EDIT 16  [Remark rem:e6segment]
OLD: without the interval
$[u,v]$ or rank sequence attaining that minimum.
NEW: without recording the interval $[u,v]$ or the rank sequence that attains that minimum.
WHY: Garden path — the original parses as the interval failing to attain the minimum; the intended meaning is that the witness was not recorded.

EDIT 17  [Theorem thm:V1]
OLD: we enumerated and checked every interval
of length $\ge 2$ in exact integer arithmetic
NEW: we enumerated and checked every interval of length at least $2$ in exact integer arithmetic
WHY: Readable mathspeak in running text (Bertsekas rule 8).

EDIT 18  [Theorem thm:V2]
OLD: In $A_{10}$, $[e,w_0]$ and a partial slab ($11$ of $65$ candidates at
$c=2$) were checked, all log-concave, with one proper interval exactly
tying $\rho([e,w_0])$.
NEW: In $A_{10}$, we checked $[e,w_0]$ and a partial slab ($11$ of $65$ candidates at $c=2$); all are log-concave, and one proper interval exactly ties $\rho([e,w_0])$.
WHY: Active voice with "we"; the trailing absolute construction "with ... tying" dangles (rule 9).

EDIT 19  [Remark after thm:V2]
OLD: confirming that it is the full interval rather
than a shorter proper interval.
NEW: confirming that the witness is the full interval rather than a shorter proper interval.
WHY: "It" has no clean antecedent (the nearest noun is the rank sequence).

EDIT 20  [Conjecture conj:F1]
OLD: \begin{conjecture}[F1]
NEW: \begin{conjecture}[F1: the full interval is extremal]
WHY: Descriptive bracket titles so the reader can navigate by statement (rulebook 17); "F1" alone is an internal code name.

EDIT 21  [Remark, Status: conjectural]
OLD: We verified it exhaustively for every irreducible
simply-laced group in the exhaustive tier
NEW: We verified it for every irreducible simply-laced group in the exhaustive tier
WHY: "Exhaustively ... exhaustive tier" doubling; the tier name carries the information.

EDIT 22  [Example ex:F1-irreducible]
OLD: The extremal principle
therefore fails when reducibility is allowed.
NEW: The extremal principle fails when reducibility is allowed.
WHY: "Thus ... therefore" in consecutive sentences; one connective suffices, and the terse sentence lands harder (rulebook 16).

EDIT 23  [Example ex:F1-irreducible]
OLD: reducible simply-laced types of rank $\le 6$, $A_1\times D_4$ was the
NEW: reducible simply-laced types of rank at most $6$, $A_1\times D_4$ was the
WHY: Readable mathspeak in running text (Bertsekas rule 8).

EDIT 24  [Theorem thm:F1-smooth]
OLD: Let $\W$ be a finite irreducible simply-laced Weyl group of rank $\le 6$
NEW: Let $\W$ be a finite irreducible simply-laced Weyl group of rank at most $6$
WHY: Readable mathspeak — "Let $k$ be a positive integer" pattern (Bertsekas rule 8).

EDIT 25  [Example ex:F1-simplylaced]
OLD: falsifies the conjecture even within the rationally-smooth subclass
NEW: falsifies the conjecture even within the rationally smooth subclass
WHY: -ly adverb compounds are not hyphenated; "rationally smooth" is the paper's dominant form (consistency; Halmos rule 6).

EDIT 26  [Conjecture conj:staircase]
OLD: In type $A_{m-1}$, the exponent multiset of the rationally-smooth
Poincar\'e polynomial
NEW: In type $A_{m-1}$, the exponent multiset of the rationally smooth Poincar\'e polynomial
WHY: Same hyphenation consistency as Edit 25.

EDIT 27  [Section sec:F2, unconditional preamble]
OLD: We prove the following local limit theorem for the log-concavity ratio, in
the classical style of~\cite{petrov1975}, near the center for \emph{every}
$m$.
NEW: In the classical style of~\cite{petrov1975}, we prove the following local limit theorem for the log-concavity ratio near the center, valid for \emph{every} $m$.
WHY: Modifier pile-up separated "ratio" from "near the center"; fronting the style reference restores the natural order (2-3-4 spirit).

EDIT 28  [Section sec:F2, unconditional preamble]
OLD: and two independent automated review
passes (an adversarial mathematics lane and a numerics lane) examined the
mathematics and numerics separately.
NEW: and two independent automated review passes examined the mathematics and the numerics separately.
WHY: The parenthetical restates the clause it sits in; the full lane details are preserved in the Acknowledgments, so no disclosure is lost.

EDIT 29  [Theorem thm:G1(b)]
OLD: (e.g.\ $C_2(1)=3.1$, $m_1(1)=180$; the
constant grows with $y_0$, e.g.\ $C_2(3)=3940$)
NEW: (e.g.\ $C_2(1)=3.1$, $m_1(1)=180$; the constant grows with $y_0$, reaching $C_2(3)=3940$)
WHY: Doubled "e.g." inside one parenthesis.

EDIT 30  [Section sec:F2, reduction subsection]
OLD: and Theorem~\ref{thm:finite560} settles every $4\le m\le560$.
NEW: and Theorem~\ref{thm:finite560} settles every $m$ with $4\le m\le560$.
WHY: The inequality was serving as a noun; readable mathspeak (Bertsekas rule 8).

EDIT 31  [Conjecture conj:S, (S4)]
OLD: \item[(S4)] \emph{(a-priori ratio seed)}
NEW: \item[(S4)] \emph{(a priori ratio seed)}
WHY: "A priori" is not hyphenated in standard mathematical usage.

EDIT 32  [Remark rem:S-evidence, (S4) bullet]
OLD: This is a weak a-priori form of the conclusion
NEW: This is a weak a priori form of the conclusion
WHY: Same as Edit 31.

EDIT 33  [After Proposition prop:CLred]
OLD: The reduction argument is not reproduced here.
NEW: We do not reproduce the reduction argument here.
WHY: Active voice, "we" over the agentless passive (rule 9).

EDIT 34  [After Proposition prop:CLred]
OLD: composition document; the bootstrap map of (S6) is not yet specified in
closed form there, which is part of why (S6) remains open, and the
assembled composition has not yet been independently refereed.
NEW: composition document. The bootstrap map of (S6) is not yet specified there in closed form, which is part of why (S6) remains open, and the assembled composition has not yet been independently refereed.
WHY: 2-3-4 rule — the three-clause semicolon chain buries two distinct honesty points; splitting keeps both, weakening neither.

EDIT 35  [Remark rem:S-evidence, opening]
OLD: We record it here as part of the reduction
because the remaining statements are stated relative to the same bands and
constants.
NEW: We keep it in the list because the remaining statements are formulated relative to the same bands and constants.
WHY: "Recorded ... record" and "statements ... stated" doublings within two sentences.

EDIT 36  [Remark rem:S-evidence, (S5) bullet]
OLD: the available checks are a finite
$\omega$-grid, and the monotonicity available to us runs in a different
variable
NEW: the existing checks form a finite $\omega$-grid, and the monotonicity available to us runs in a different variable
WHY: "Available ... available" doubling; checks "form" a grid rather than "are" one.

EDIT 37  [Remark rem:S-evidence, (S6) bullet]
OLD: so a domination argument to the stated
range is among what is missing.
NEW: so a domination argument reaching the stated range is still needed.
WHY: "Among what is missing" is contorted; the replacement states the same gap plainly (honesty preserved).

EDIT 38  [Section sec:F3, subsection heading]
OLD: \subsection*{Why Weyl groups escape the $H_3$ failure}
NEW: \subsection*{Why Weyl groups may escape the $H_3$ failure}
WHY: The body immediately hedges ("a possible mechanism, not a theorem"); the heading should carry the same graded confidence (rulebook 18, and strengthens the honesty framing).

EDIT 39  [Section sec:F3, after the mechanism]
OLD: Because it relies on the empirical
Observation~\ref{obs:F3}, it does not prove
NEW: Because the mechanism relies on the empirical Observation~\ref{obs:F3}, it does not prove
WHY: Two "it"s with different antecedents (the pattern vs. the mechanism).

EDIT 40  [Section sec:F3, evidence paragraph]
OLD: In that probe, every perturbation of an $m=4$
dihedral core by extra cover steps that breaks the pure pattern strictly
raises the ratio;
NEW: In that probe, every cover-step perturbation of an $m=4$ dihedral core that breaks the pure pattern strictly raises the ratio;
WHY: The relative clause "that breaks" attaches most naturally to "steps"; reordering removes the garden path.

EDIT 41  [Discussion, proved-unconditionally item]
OLD: groups of rank $\le6$, and in type $A_{m-1}$ for $m\le17$ using the cited
NEW: groups of rank at most $6$, and in type $A_{m-1}$ for $m\le17$ using the cited
WHY: Readable mathspeak, consistent with Edits 23-24.

EDIT 42  [Discussion, future-work paragraph]
OLD: For future work, these results provide reductions as well as data. If
NEW: These results provide reductions as well as data for future work. If
WHY: "For future work" dangles — the results, not the sentence's subject, serve future work.

EDIT 43  [Discussion, direction 1]
OLD: The far-region decay, crossover and mid-range
bounds, variance floors and caps, reduction, and the whole range
$4\le m\le560$ are already proved with explicit constants.
NEW: The far-region decay, the crossover and mid-range bounds, the variance floors and caps, and the reduction itself are already proved with explicit constants, and the whole range $4\le m\le560$ is settled exactly.
WHY: Subject-verb slip ("the whole range ... are ... proved" — a range is not proved) and non-parallel list; content unchanged.

EDIT 44  [Discussion, closing paragraph]
OLD: Several related questions do not address Conjecture 2.11 itself. These
NEW: Several related lines of work do not address Conjecture~2.11 itself. These
WHY: The listed items are results and papers, not questions.

EDIT 45  [Discussion, direction 2]
OLD: open even under the rationally-smooth restriction.
NEW: open even under the rationally smooth restriction.
WHY: Same hyphenation consistency as Edits 25-26.

EDIT 46  [Related work]
OLD: Our literature search, last
updated on 2026-08-06, found no paper
NEW: Our literature search, last updated on August 6, 2026, found no paper
WHY: ISO date is log format, not prose; precision is retained.

EDIT 47  [Theorem thm:finite560]
OLD: \begin{theorem}[Exact finite range]
NEW: \begin{theorem}[Exact finite range $4\le m\le560$]
WHY: Descriptive bracket title — the range is what a navigating reader needs (rulebook 17); matches the statement's scope including the $m=4$ clause.

---

## Flagged — wanted to change, but not without touching mathematics or settled structure

- **Theorem thm:G1(b)**: the verification sentences ("We also verified (a) ... The
  analytic argument covers all remaining values of $m$.") sit inside enumerate item (b)
  but concern both (a) and (b). Moving them out of the theorem environment would change
  what is asserted *as the theorem*, i.e. its scope — left untouched.
- **Example ex:F1-irreducible**: "$=58/51=1.1372549\ldots$ Since ..." — the sentence ends
  on a decimal expansion with no terminal punctuation. Fixing it cleanly means
  restructuring around frozen numerals; left untouched.
- **Notation**: the abstract writes $\sigma_m^2(r_m-1)$ while Section 6 writes
  $\sigma^2(r_m-1)$. Harmonizing is a notational (mathematical) change; flagged only.
- **Table tab:exhaustive**: the witness column mixes formats ("proper (ties $[e,w_0]$),
  $k=1$" vs. "proper, $\ell=27$ (ties $[e,w_0]$), $k=14$"). Harmonizing risks altering
  what data each cell records; flagged only.
- **Remark [Location and explicit constant]**: "the earlier guess $7/8$" has no
  attribution. Adding one would introduce a claim I cannot source from the paper;
  flagged for the authors (specific-credit rule 19).
- **Source-only inconsistencies** (no printed effect, so out of copyedit scope):
  Example ex:H3 declares "$(W,S)$" while the paper macro is `\W`; the sampling-tier
  Proposition carries the label `thm:V3`.
- **Abstract/intro echo**: the intro's second paragraph repeats the abstract's frontier
  sentence nearly verbatim ("roughly an order of magnitude ... left open in Brenti's
  list"). Varying it is possible but every rewording brushes against settled status
  claims; left for the authors to decide.
