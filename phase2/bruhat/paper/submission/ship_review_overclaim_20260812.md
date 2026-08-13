# Ship review — lens: OVERCLAIM AND ATTRIBUTION

*Read-only pass, 2026-08-12. Target: `paper/submission/main.tex` (1243 lines, 14 pp).
Ground truth read in full: `CLOSURE_PLAN_v2_20260812.md`, `sol_comprepair_20260812.md`
(including the reader's note), and the prior `review_overclaim_20260812.md`.
Every `\cite` key was resolved against the live literature (arXiv/journal), including a
full-text extraction of Brenti arXiv:2410.09897. No file other than this report was
created or modified.*

## Verdict: **DO_NOT_SHIP**

Not because the paper oversells its headline results — on the contrary, the abstract,
the contributions list, the status-by-logical-strength discussion, and the
significance framing added today are all **clean**. Brenti's conjecture is never
implied proved or near-resolution; the extremal conjecture is never implied
established; the sharp asymptotic is conditional everywhere it appears; Bóna,
Hoggar/Kook and Canfield–Janson–Zeilberger are credited correctly and explicitly
not absorbed.

The blocker is narrower and worse: **the paper states three times, in three
different sections, that (S1)–(S4) imply the core lemma CL.** That is the exact claim
today's adversarial review refuted, and one instance sits under the heading
*"Proved unconditionally."* The `\begin{proposition}` itself was corrected to
(S1)–(S6); the downstream prose was not. There is also one load-bearing citation
attributed to the wrong paper, and three bibliography entries with wrong author
initials. Every blocker is a one-line edit — this is a 20-minute fix, not a
re-draft — but shipping as-is puts a known-false logical claim in print.

---

# BLOCKERS

## B1 (critical) — The retracted "(S1)–(S4) ⟹ CL" claim survives in three places, one of them under "Proved unconditionally"

**Ground truth.** `sol_comprepair_20260812.md`, final line: *"CL(79, 20, 0.89) for
m ≥ 561 is proved conditionally on six atomic open statements (S1)–(S6). **Closing the
old statements (S1)–(S4) alone would not close CL.**"* `CLOSURE_PLAN_v2` §A: (S5) and
(S6) are *"the only genuinely open mathematics"* and were *"split out as their own named
atomic obligations rather than being absorbed silently."*

The paper's Proposition was updated (line 886: *"Statements (S1)--(S6) ... imply"*), but
three restatements of it were not:

| line | quoted text | why wrong |
|---|---|---|
| **957–958** (Remark *"What is claimed, and what is not"*) | `Proposition~\ref{prop:CLred} proves that (S1)--(S4) imply Conjecture~\ref{conj:CL}. Five of the six remain open.` | False, and self-contradicting two words later ("six"). This is the paper's *honesty remark* — the one place a referee looks to check the authors know their own scope. |
| **1058–1059** (Discussion, **`\item[Proved unconditionally.]`**) | `Proposition~\ref{prop:CLred} proves that (S1)--(S4) imply Conjecture~\ref{conj:CL}.` | A statement known to be false, printed under the heading "Proved unconditionally." Worst single line in the paper. |
| **1101–1104** (Open problems, item 1) | `\textbf{Prove statements (S1)--(S4) of Conjecture~\ref{conj:S}, and hence Conjecture~\ref{conj:CL}.} Proposition~\ref{prop:CLred} gives this implication` | Wrong twice: the implication is false, **and** (S1) is already proved (line 860), so it does not belong on a to-prove list at all. |

**Fix:** `(S1)--(S4)` → `(S1)--(S6)` at 957 and 1058; at 1101 → *"Prove statements
(S2)–(S6) of Conjecture~\ref{conj:S}, and hence Conjecture~\ref{conj:CL}."* At 957,
also rewrite `Five of the six remain open` → `Statement (S1) is proved; (S2)--(S6)
remain open.`

**Same defect, two more sites (stale headings/counts):**

- **line 816**, subsection heading: `\subsection*{Reduction of the core lemma to four cumulant statements}` — contradicted by line 818 two lines below (*"six statements ... five of which remain open"*), and doubly wrong because (S5) is a continuum certificate and (S6) a bootstrap closure, neither of which is a cumulant statement. Headings are what a skimming referee indexes on. → *"Reduction of the core lemma to six statements about the tilted law"*.
- **line 904**, remark title: `\begin{remark}[Status and evidence for (S1)--(S4)]` — the body enumerates (S1) through (S6). → `[(S1)--(S6)]`.
- **line 1108**: `The smallest computed margins occur in the cumulant bounds of (S1) in the deepest band, where they are under 4%. A proof or counterexample search should begin there.` — (S1) **is proved**; directing future work to hunt a counterexample there contradicts line 860 and re-opens a closed statement. → point the reader at (S6) instead, which `CLOSURE_PLAN_v2` calls *"the riskier one ... If a seventh obligation appears anywhere, this is where."*

## B2 (critical) — Proposition~\ref{prop:CLred} is asserted with no proof in the paper and no citable support behind it

Line 884–889 states the (S1)–(S6) ⟹ CL implication as a **Proposition**. Its proof is
not in the paper: lines 891–902 are a prose sketch ending *"The repository contains the
complete chain and a machine re-verification of the resulting constant."*

What the ledger says about that chain, as of tonight:

- `CLOSURE_PLAN_v2` §C: *"`sol_comprepair_20260812.md` is single-model and unrefereed; **it is now the document that defines the obligation list, so it needs two lanes before anything may cite it**."*
- `sol_comprepair` WHAT REMAINS §7: *"The repaired composition requires two referee passes."*
- The prior version of this same document produced the false implication in B1. Its base rate is not good.

So the paper's only genuinely *new* mathematical assertion in Section 5 is a Proposition
whose proof is (a) absent from the manuscript, (b) supported by a same-day,
single-model, unrefereed note, and (c) the successor to a document that was wrong about
this exact statement. That is an overclaim of epistemic status, independent of whether
the implication turns out to be true.

The prior review (`review_overclaim_20260812.md`, Finding 3) flagged this as "not an
overclaim under the mandate" — that judgement was made when the composition was v1 and
two-referee-verified inputs were claimed. It no longer holds: the composition has been
*repaired today* and is unrefereed.

**Fix (pick one):** (i) get the two referee lanes to land before submitting; or
(ii) demote to a stated claim with disclosed status, e.g. append to line 902: *"The
reduction argument is not reproduced here; it is recorded in the repository and has not
yet been independently verified."* Option (ii) costs one sentence and is consistent with
the register the rest of the paper already keeps.

## B3 (critical) — (S1) is declared **proved** with no proof and no pointer

Line 860: `(S1) ... (banded cumulant scales; \textbf{proved}, see Remark~\ref{rem:S-evidence})`.
Line 906: `Statement (S1) has since been proved, by a bandwise argument with a rigorous interval certificate`.

Neither location gives the argument, cites a reference, or points at a repository
artifact. A reader is told a statement is proved and given nowhere to check. (It *is*
proved — `sol_s1_20260812.md`, both referee lanes MINOR_REPAIRS — but the paper does not
say so.) Note also the structural oddity: a statement labelled "proved" living inside a
`conjecture` environment.

**Fix:** either extract (S1) as a `\lemma` with its proof (or a proof sketch plus a
repository pointer), or add to line 906: *"...; the argument and its interval certificate
are in the repository."* Same treatment as B2's option (ii).

## B4 (critical) — Misattributed load-bearing citation: Carrell 1994 credited with Gasharov's factorization theorem

**Line 599–604 (Theorem~\ref{thm:F1-smooth}):**

> `every rationally smooth $v$, i.e.\ every $v$ for which the Poincar\'e polynomial $P_{[e,v]}(q)$ factors as a product of $q$-integers~\cite{carrell1994}`
>
> `Granting the classical rational-smoothness factorization result cited above, the same conclusion holds in type $A_{m-1}$ for $m\le17$.`

Two problems, and the second is load-bearing:

1. **Wrong equivalence.** Carrell (PSPUM 56, 1994) is the Carrell–Peterson criterion: *rationally smooth ⟺ Poincaré polynomial is **palindromic***. It does not characterise rational smoothness by factorization into $q$-integers, and that characterisation is false as a definition in general type.
2. **Wrong author.** The $q$-integer factorization $P_w(q)=[e_1+1]_q\cdots[e_n+1]_q$ for smooth $w\in S_n$ (equivalently 3412/4231-avoiding) is **Gasharov, *Factoring the Poincaré polynomials for the Bruhat order on $S_n$*, JCTA 83 (1998), 159–164**. The general-type refinement is Akyildiz–Carrell (arXiv:1009.2895, 2010) — still not Carrell 1994.

This matters beyond bibliographic hygiene: the type-$A$ $m\le17$ clause is *explicitly*
declared to rest on "the cited result" rather than on the paper's own computation (which
the disclosure at line 605–608 says reaches only $m\le7$). If the cited result is the
wrong paper, the $m\le17$ clause currently rests on nothing the reader can follow — and
that clause is what the abstract (line 78–80) and the Discussion (line 1055–1058) both
advertise as **proved**.

**Fix:** add a `\bibitem{gasharov1998}` (V. Gasharov, *Factoring the Poincaré polynomials
for the Bruhat order on $S_n$*, J. Combin. Theory Ser. A **83** (1998), 159–164) and cite
it for the $m\le17$ clause; keep `carrell1994` only where the Carrell–Peterson
palindromicity criterion is meant, and reword the definition at line 599–601 accordingly.

## B5 (major) — Three bibliography entries carry wrong author initials

Verified against the live arXiv records. Given this paper's history of fabricated
bibliography entries, initials that do not match are exactly the signal a referee will
read as fabrication.

| bibitem | paper says | actual (verified) |
|---|---|---|
| `chapelier-fromentin` (line 1237) | `L.~Chapelier-Laget and G.~Fromentin` | **N**athan Chapelier-Laget and **J**ean Fromentin (arXiv:2412.19593) |
| `kessouri2024` (line 1233) | `K.~Kessouri, M.~Ahmia, A.~Arslan, and A.~Mesbahi` | **A**li Kessouri, Moussa Ahmia, **H**asan Arslan, **S**alim Mesbahi (arXiv:2408.02424) — three of four initials wrong |
| `kook2006` (line 1183) | `W.~Kook, \emph{On the product of log-concave polynomials} (elementary note on product-closure of log-concavity), 2006.` | Paper is **real** (W. Kook, *On the product of log-concave polynomials*), but the entry has no venue and substitutes a parenthetical self-description for one. Reads as a placeholder a referee will assume is invented. |

**Fix:** correct the six initials; give `kook2006` a real venue/preprint locator or mark it
explicitly as a preprint/note with a URL.

---

# NON-BLOCKING FINDINGS

## N1 (major) — "All computations use exact integer arithmetic" is contradicted 580 lines later

**Line 316–317 (Section 3, opening sentence):**
> `All computations use exact integer (arbitrary-precision) arithmetic; no claim labeled a theorem uses floating point.`

**Line 899–902:**
> `Those computations use directed-rounding interval arithmetic together with exact integer and rational arithmetic where stated; they are rigorous modulo the interval library, and we do not claim they are exact-rational throughout.`

Line 899–902 is today's correction and is exactly right. Line 316–317 is the old
unqualified claim and it is stated globally, in the methodology section, where a referee
will take it as covering the whole paper. It is contradicted by:

- the CL-reduction certificates (line 899–902, by the authors' own admission);
- (S1)'s proof, which line 906 says uses "a rigorous **interval** certificate" — and (S1) is claimed proved, i.e. theorem-grade;
- Theorem~\ref{thm:G1}'s verification claims at **line 676–678** (`we verified (a), with the same displayed constant, directly in exact arithmetic for every $4\le m\le109$`; likewise (b) to $m\le229$). Part (a) bounds $|p(k) - Z(y)[1-\tfrac{B_m}{12}\mathrm{He}_4(y)]|$ where $Z(y)=(2\pi\sigma^2)^{-1/2}e^{-y^2/2}$, and (b) bounds $\sigma^2\log r_m(k)$. Neither quantity is rational. These checks cannot have been "exact"; they were directed-rounding interval checks.

Same issue, weaker form, at **line 653–654** (`The proof combines an analytic argument with exact finite checks`), **line 934–936** (`Exact checks of the inequality in Conjecture~\ref{conj:CL} at $m=401$ and $m=402$`), **line 238–239** and **line 1093** (`exact-arithmetic logs`).

**Fix:** scope line 316–317 to the tier it actually describes — *"The Bruhat-interval
enumeration and every verdict in Tables 1–3 use exact integer (arbitrary-precision)
arithmetic. The analytic certificates of Section~\ref{sec:F2} use directed-rounding
interval arithmetic together with exact integer and rational arithmetic where stated; see
the note following Proposition~\ref{prop:CLred}."* Then replace "exact arithmetic" with
"directed-rounding interval arithmetic" at 654, 676–678, and 934–936 wherever the checked
quantity is transcendental. (Theorem~\ref{thm:finite560}'s integer/rational claim at
line 716–718 appears genuinely exact and can stand.)

## N2 (major) — The $m\ge561$ scope boundary rests on a verifier the ledger says has not landed

**Line 764–766:**
> `The reduction for Theorem~\ref{thm:F2} requires this statement for every $m\ge401$. The exact computation in Theorem~\ref{thm:finite560} handles $401\le m\le560$, so the conjecture is stated and needed only for $m\ge561$.`

`CLOSURE_PLAN_v2` §D: *"**The hygiene overlay verifier.** Still owed. Input I3 consumes
its `M_H = 560` repair, so **the finite-range splice and the claim that `m >= 561` is the
entire residual obligation are not citable until it lands.**"*

This is not a small scope detail: `m\ge561` is the scope of Conjecture~\ref{conj:CL}, of
the two-sided bound in Theorem~\ref{thm:F2}, of Proposition~\ref{prop:CLred}, and of the
`187/216` claim at line 977–981. If the splice is off, all four scopes are wrong.

**Fix:** land the verifier before submitting, or state the splice as a claim rather than a
settled fact. Flagging for author confirmation rather than calling it a blocker, since
Theorem~\ref{thm:finite560} itself is independently verified on disk (prior review, and
the arithmetic re-checks below).

## N3 (major) — "independent review passes" reads as human peer review; they were automated referee agents

**Line 653–654:** `two independent review passes examined the mathematics and numerics separately.`
**Line 1145–1147 (Acknowledgments):** `We subjected the draft proofs and numerical results to independent review passes, including a from-scratch numerical audit.`

These were the campaign's automated adversarial referee lanes (`referee_maths_*`,
`referee_numerics_*`). In a paper whose credibility rests substantially on the accuracy of
its own AI-disclosure section, describing automated lanes as "independent review passes"
without saying they were automated is the one place where the disclosure understates the
machine's role — the opposite direction from every other sentence in that section, and
therefore the one a referee will notice.

**Fix:** *"two independent **automated** review passes (an adversarial mathematics lane and
a numerics lane) examined..."*, and the same qualifier in the Acknowledgments. Also
consider moving line 653–654 out of the theorem lead-in: internal process claims sitting
immediately before a theorem statement read as credibility-padding regardless of accuracy.

## N4 (major — needs author confirmation, not a text fix)

**Line 1151–1155:** `Nikol Panayotova Savova and Sihao Huang selected the research
questions and strategies, determined which statements were presented as theorems or
conjectures, and **independently checked the disclosed constants and counterexamples**.`

The prior review's Finding 3 records that the human ratification step *"should be
completed before submission"* — i.e. it was outstanding as of this morning. If it has
not been completed, this sentence is false, and a false statement about human
verification in the disclosure section of an AI-assisted paper is the single most
damaging error the paper could ship. Confirm it is literally true; if partially true,
narrow it (*"checked the constants and counterexamples reported in
Section~\ref{sec:F1} and Table~\ref{tab:exhaustive}"*).

## N5 (moderate) — Observation~\ref{obs:F3}: a rank-sequence observation is inflated into a structural classification by "therefore"

**Line 997–999:**
> `Each observed interval is therefore poset-isomorphic to the full Bruhat interval of the dihedral group $I_2(m)$ and arises from a rank-two dihedral standard parabolic of braid order $m$.`

The premise is a statement about the **rank sequence** $(1,2,\dots,2,1)$. That does not
imply poset-isomorphism to a dihedral interval, and it certainly does not imply the
interval *arises from a rank-two dihedral **standard parabolic*** — a claim about
generators, not about counts. "Therefore" asserts a deduction the data do not supply.
(If each case was in fact checked for the parabolic structure, say that instead.)

**Fix:** `therefore` → *"In each case we checked directly that the interval is
poset-isomorphic to ... and arises from ..."*, or drop the structural half of the
sentence. The surrounding paragraph (line 1008 *"This is an empirical observation, not a
theorem"*) is correctly hedged; this one word is not.

## N6 (moderate) — "uniformly" overstates the sampling design

**Line 507–510 (Proposition~\ref{thm:V3}(i)):** `We sampled $60{,}000$ Bruhat intervals
... **uniformly** from a random-walk ensemble with $4\le\ell(u,v)\le 12$.`

"Uniformly" invites the reading *uniform over Bruhat intervals*, which would be a far
stronger coverage claim than a random-walk ensemble supports. **Fix:** drop "uniformly",
or *"drawn from a random-walk ensemble (not uniform over intervals)"*.

Related, same proposition, line 513–515: `every perturbation that destroys the pure
dihedral pattern strictly raises the ratio` — true of the checked set; add *"among those
checked"* to prevent a universal reading.

## N7 (minor) — Abstract does not signal that the leading term of the sharp asymptotic is classical

**Line 85–87:** `The sharp asymptotic $\sigma_m^2(r_m-1) = 1-\tfrac{27}{25}m^{-1}+O(m^{-2})$ is conditional on...`

I verified the credit in the body is **accurate**: Canfield–Janson–Zeilberger
(arXiv:0908.2089, eq. 4.11 and Thm 4.6) do obtain $P(k)^2-P(k-1)P(k+1) = (\sigma^{-2}+O(n^{-4}))P(k)^2$
for the Gaussian binomial in the central window — precisely the leading `1`. The Related
Work paragraph (line 214–222) credits this properly and delimits the contribution
correctly. But a referee reading only the abstract sees the whole expansion presented as
new; the delta is the $-\tfrac{27}{25}m^{-1}$ term, the $S_m$ case, and the *global*
(not central) minimum.

**Fix:** one clause — *"...refining the known leading term to
$1-\tfrac{27}{25}m^{-1}+O(m^{-2})$ and extending it from the central index to the global
minimum, conditional on..."*

## N8 (minor) — The "explains away the alarming trend" framing is scoped narrower than it reads

**Line 158–162:** `Taken alone, this can suggest that log-concavity will fail at a larger
rank. Along the full type-$A$ intervals, the central ratio instead approaches $1$ from
above at the rate determined in Section~\ref{sec:F2}.`

Literally correct (the *central* ratio result is unconditional via Theorem~\ref{thm:G1}),
but the rhetorical setup implies the worry has been dispelled. It has been dispelled only
for the $[e,w_0]$ family, only in type $A$, and only at the central index; the type-$D$
row of the same trend is untouched, and the global-minimum version is conditional on
Conjecture~\ref{conj:CL}. **Fix:** append *"in type $A$; the corresponding statement for
the global minimum is conditional (Theorem~\ref{thm:F2}), and the type-$D$ trend is not
addressed."*

## N9 (minor) — Three uncited bibliography entries print in the reference list

`butler1990`, `sagan1992`, `suwangyeh2011` have no `\cite` anywhere in the text but appear
as **[7], [8], [9]** in the compiled PDF (confirmed in `main.pdf`). All three are real
papers, but an uncited trio reads as citation padding — an unwelcome look in a paper that
has to survive scrutiny of its bibliography. **Fix:** cite them where relevant
(natural home: the Related Work $q$-log-concavity sentence) or remove them.

## N10 (minor) — Bóna is credited with priority he does not have

**Line 215–217:** `Log-concavity of the Mahonian numbers is classical: B\'ona~\cite{bona2004} proved it, and it also follows from the product-closure results of~\cite{hoggar1974,kook2006}.`

Bóna 2004 gives a *combinatorial* proof; the result follows immediately from the
$[m]_q!$ product formula plus Hoggar (1974) and predates him. The sentence's second half
already says so, so the fix is cosmetic: *"B\'ona~\cite{bona2004} gave a combinatorial
proof, and it also follows from..."*. Direction of error is over-crediting, so this is
harmless — noted only because attribution precision is in scope.

## N11 (housekeeping, outside lens)

- `\author{}` (line 38) is **empty**; the authors appear only inside `\thanks`. Most journals' editorial systems will reject or mangle this. The footnote's rationale is defensible, but confirm the target venue accepts it.
- Two `[repository URL to be added on submission]` placeholders remain live in the compiled PDF (p. 4 and p. 6). Several claims in this review's recommended fixes (B2, B3) point at that repository; it must exist and be reachable at submission.

---

# WHAT I VERIFIED AS CORRECT

Recording this so the fixes above are not read as a broader indictment.

**Primary source, checked by full-text extraction of arXiv:2410.09897 (p. 10):**
Brenti's Conjecture 2.11 is stated verbatim as the paper reports it (*"Let W be a Weyl
group, and u, v ∈ W. Then [u, v] is rank log-concave"*); the recorded verification list
($A_n,D_n$ for $n\le5$; $B_n$ for $n\le4$; $B_5$ with $\ell(u,v)\ge20$; $F_4$; dihedral
groups) matches line 136–138 exactly; the $H_3$ example — $u=s_3$,
$v=s_1s_2s_3s_2s_1s_2s_1s_3$, $m(s_1,s_2)=5$, $m(s_2,s_3)=3$, rank generating function
$1+3t+5t^2+7t^3+10t^4+10t^5+5t^6+t^7$ — matches Example~\ref{ex:H3} character for
character, and it is on **page 10**, as claimed. Example~\ref{ex:H3}'s "We checked the
following example against the primary source" is true.

**Citations resolved and content-verified:** `brenti2024open`, `bjorner-ekedahl`,
`cjz2011` (incl. the $1+\sigma^{-2}$ central-ratio credit — verified in the source text),
`bona2004`, `hoggar1974`, `kook2006` (real, entry format aside), `burrull-gui-hu`
(**including the specific "non-unimodal example due to Stanton" claim at line 231–232** —
confirmed at their §1.3.2, citing Stanton, *Unimodality and Young's lattice*, JCTA 54),
`short-intervals` (Evgeniya Akhmedova, arXiv:2110.00862 — real, initial correct),
`petrov1975`, `gaetzgao2020` (Gaetz–Gao, Selecta Math. — does classify self-dual
intervals, as described), `stanley-yan` (Chan–Pak, arXiv:2407.19608), `kahn-saks`
(van Handel–Yan–Zeng, arXiv:2309.13434), `equivariant-logconcave` (Gui, arXiv:2205.05408),
`kessouri2024` and `chapelier-fromentin` (real papers; initials wrong, see B5),
`carrell1994` (real paper; wrongly attributed, see B4). **No fabricated entry found.**

**Arithmetic re-checked independently:** Table~\ref{tab:exhaustive}'s 17 interval counts
sum to exactly $1{,}079{,}490{,}991$; the sampling tier sums to $124{,}944$ and the seeded
subtotal to $64{,}944$; $919681/872356=1.054250$, $65523/64757=1.011829$,
$392/345<58/51$ with gap $2/1955$, $91/108<187/216$. All consistent.

**Overclaim checks that came back clean:**
- Brenti's conjecture: never claimed proved, nearly proved, or close to resolution. Line 1067 says plainly *"Brenti's conjecture remains open in general."*
- The extremal conjecture: labelled `\begin{conjecture}`, with a dedicated *"Status: conjectural, not proved"* remark (583–594), a remark stating Theorem~\ref{thm:F1-smooth} is *"a **strictly weaker** statement"* (628–638), and two counterexamples establishing necessity of the hypotheses. Correct throughout.
- The sharp asymptotic: conditional in the abstract, in the contributions list, in the theorem header (`--- conditional`), in the discussion, and in the open-problems list. No unconditional statement of it anywhere.
- The three tiers (exhaustive / near-top / sampling) are never conflated; Theorem~\ref{thm:V2} and Proposition~\ref{thm:V3} both carry "not exhaustive" in their headers, and both are followed by remarks disclaiming coverage.
- Prohibited-language grep (`first to`, `breakthrough`, `major advance`, `long-standing`, `sheds new light`, `opens the door`, `nearly/essentially proved`): **zero hits**.
- The significance framing added today tracks `edit_brief_significance_20260812.md` items 1–6 without exceeding them; each of its "What must NOT happen" prohibitions is respected. N8 is the only place it leans slightly past the evidence, and only rhetorically.
- The honesty disclosures are genuinely unusual and should be kept verbatim: the $E_6$ unrecoverable-witness remark (356–369), the discarded-perturbation accounting (498–504), the $m\le7$ vs $m\le17$ factorization disclosure (605–608), the "we do not claim they are exact-rational throughout" note (899–902), the disclosed sub-4% margin (921), and above all line 909–916 — *"The list has changed as the reduction was scrutinised ... We regard the current list as the honest one, while noting that it has grown under scrutiny before."* That paragraph is the paper's strongest credibility asset. Which is exactly why B1 must be fixed: it sits nine lines above a remark that contradicts it.

---

## Fix order

1. **B1** — six string edits (957, 1058, 1101, 816, 904, 1108). Ten minutes.
2. **B4/B5** — add `gasharov1998`, re-point the $m\le17$ citation, correct six initials, give `kook2006` a venue.
3. **B2/B3** — one disclosure sentence each, or wait for the referee lanes.
4. **N1** — rescope line 316–317 and the three "exact arithmetic" sites.
5. **N2, N4** — author confirmation required before submission.
6. N3, N5–N10 — one-line each.

Re-run the overclaim lens on the diff after B1 lands; five of the six B1 sites were
missed by today's edit pass precisely because they are restatements rather than statements.
