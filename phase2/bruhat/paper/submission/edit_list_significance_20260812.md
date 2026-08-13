# Sol copy-edit list (gpt-5.6-sol, effort=max) — 2026-08-12 19:44

> Proposed edits ONLY. Not yet applied to main.tex. Prose/framing pass per
> edit_brief_significance_20260812.md; the editor was instructed to change no mathematics.

EDIT 1  [Abstract: extremal conjecture]
OLD: These computations support, but do not prove, an extremal conjecture that in every irreducible,
simply-laced Weyl group the global minimum of the
log-concavity ratio over all Bruhat intervals is attained by the full
interval $[e,w_0]$. We show that both irreducibility and the simply-laced
restriction are necessary. We prove the corresponding statement for
rationally smooth lower intervals in the finite ranges stated in
Theorem~\ref{thm:F1-smooth}.
NEW: These computations support, but do not prove, an extremal conjecture that in every irreducible,
simply-laced Weyl group the global minimum of the
log-concavity ratio over all Bruhat intervals is attained by the full
interval $[e,w_0]$. If true, this would reduce verification of Brenti's
conjecture for each such group from exponentially many Bruhat intervals to
the single interval $[e,w_0]$, whose rank sequence is the coefficient
sequence of the Poincar\'e polynomial. We show that both irreducibility and
the simply-laced restriction are necessary. We prove the corresponding
statement for rationally smooth lower intervals in the finite ranges stated
in Theorem~\ref{thm:F1-smooth}.
WHY: States the conjecture’s practical consequence while preserving its scope and unproved status.

EDIT 2  [Introduction: opening]
OLD: \section{Introduction}
\label{sec:intro}

Let $\W$ be a finite Weyl group with simple reflections $S$, length function
NEW: \section{Introduction}
\label{sec:intro}

Brenti's conjecture quantifies over every Bruhat interval of every finite
Weyl group. This creates a computational obstacle and a structural
question: direct verification requires an exponentially large family of
interval checks, while the counterexample in $H_3$ shows that finiteness
alone does not explain the Weyl-group case.

We checked $1{,}079{,}490{,}991$ intervals in exact integer arithmetic.
This is roughly an order of magnitude beyond the previously recorded
frontier and completes the cases $A_6$, $A_7$, the full range of $B_5$,
$B_6$, $D_6$, and $E_6$ left open in Brenti's list. We also formulate, for
irreducible simply-laced Weyl groups, a conjectural reduction from all
Bruhat intervals to the single interval $[e,w_0]$.

Let $\W$ be a finite Weyl group with simple reflections $S$, length function
WHY: Opens with the problem’s scale, the crystallographic issue, and the concrete change in the verification frontier.

EDIT 3  [Introduction: significance before Contributions]
OLD: It does not compare
the ratios $a_k^2/(a_{k-1}a_{k+1})$ across intervals or identify where the
log-concavity ratio is smallest.

\subsection*{Contributions} Our contributions have four parts. We
distinguish computational theorems, conditional results, and conjectural or
empirical statements.
NEW: It does not compare
the ratios $a_k^2/(a_{k-1}a_{k+1})$ across intervals or identify where the
log-concavity ratio is smallest.

The extremal conjecture is the structural proposal behind the paper. It
predicts that, in each irreducible simply-laced Weyl group, the smallest
ratio over all intervals already occurs at $[e,w_0]$. The statement remains
conjectural for arbitrary intervals. If true, it replaces an exponentially
large verification by a single check of the coefficient sequence of the
Poincar\'e polynomial. We prove the comparison only for rationally smooth
lower intervals in the finite ranges stated in
Theorem~\ref{thm:F1-smooth}.

In type $A$, that coefficient sequence is the Mahonian distribution. Under
the proposed reduction, a Bruhat-order question becomes a question about
one classical distribution, which is what makes the candidate extremal
ratio tractable in type $A$. The type-$A$ analysis also explains a trend in
the data: the recorded minima in the type-$A$ and type-$D$ rows decrease
toward $1$ as rank grows. Taken alone, this can suggest that log-concavity
will fail at a larger rank. Along the full type-$A$ intervals, the central
ratio instead approaches $1$ from above at the rate determined in
Section~\ref{sec:F2}. We determine the global minimum over the Mahonian
ratios exactly for every $4\le m\le560$; the sharp asymptotic for that
global minimum beyond this finite range is conditional on
Conjecture~\ref{conj:CL}.

\subsection*{Contributions} Our contributions have four parts. We
distinguish computational theorems, conditional results, and conjectural or
empirical statements.
WHY: Explains the extremal reduction, the type-$A$ bridge, and the near-$1$ data without making either conjectural statement unconditional.

EDIT 4  [Introduction: Related work]
OLD: \subsection*{Related work} Several recent papers study related questions.
Burrull, Gui, and Hu~\cite{burrull-gui-hu} prove asymptotic
NEW: \subsection*{Related work} In type $A$, the ratio for $[e,w_0]$ is a
Mahonian ratio, linking the Bruhat-order question to a classical
probability distribution. Log-concavity of the Mahonian numbers is
classical: B\'ona~\cite{bona2004} proved it, and it also follows from the
product-closure results of~\cite{hoggar1974,kook2006}. We do not claim that
result here. Canfield, Janson, and Zeilberger~\cite{cjz2011} already obtain
the central-ratio leading term $1+\sigma^{-2}$ for Gaussian binomial
coefficients. Our contribution is the $S_m$ case: exact determination of
the global minimum over the Mahonian ratios for every $4\le m\le560$, an
unconditional local estimate for every $m\ge4$, and, conditional on
Conjecture~\ref{conj:CL}, the sharp global asymptotic with explicit
constants.

Several recent papers study related questions.
Burrull, Gui, and Hu~\cite{burrull-gui-hu} prove asymptotic
WHY: Makes the bridge between Bruhat order and Mahonian analysis explicit while separating classical results from this paper’s contribution.

EDIT 5  [Introduction: reproducibility]
OLD: Source code, exact-arithmetic result logs, and machine-checked numerical
certificates for the proved claims are available at
[repository URL to be added on submission].
NEW: Source code, exact-arithmetic result logs, and machine-checked numerical
certificates for the proved claims are available at
[repository URL to be added on submission]. These records make the finite
verification reproducible. On the analytic side,
Conjecture~\ref{conj:CL} isolates the single explicitly quantified input on
which the sharp asymptotic depends, so future work can address that
statement directly.
WHY: Identifies the reusable outputs of both the computational and conditional analytic parts.

EDIT 6  [Discussion: after logical-status summary]
OLD: \end{description}

We next list several directions for further work.
NEW: \end{description}

For future work, these results provide reductions as well as data. If
Conjecture~\ref{conj:F1} holds, verification of rank log-concavity in each
irreducible, simply-laced Weyl group reduces from exponentially many
intervals to the single Poincar\'e coefficient sequence of $[e,w_0]$;
Theorem~\ref{thm:F1-smooth} establishes this comparison only for
rationally smooth lower intervals in the stated finite ranges. In type
$A$, that sequence is Mahonian, making classical local-limit methods
available for the candidate extremal ratio. The equality data give a
second structural target: the observed cores have
$m\in\{4,6\}$, both crystallographic, whereas Brenti's $H_3$
counterexample uses $m=5$. This is a candidate explanation for the
crystallographic boundary, not a proof. Finally, the exact-arithmetic logs
make the finite computations reproducible, and
Conjecture~\ref{conj:CL} is a named, explicitly quantified target for
removing the condition from Theorem~\ref{thm:F2}.

We next list several directions for further work.
WHY: Adds the requested account of what the reductions, boundary pattern, and reproducible artifacts give a future reader.

FLAGS REQUIRING AUTHOR ACTION

FLAG 1  [Theorem~\ref{thm:F1-smooth} and its summaries]
The embedded TODO says that the type-$A$ clause through $m\le17$ has been checked directly only through $m\le7$ and still requires confirmation that \cite{carrell1994} supplies the stated factorization and equality conclusion. Until that check is complete, the manuscript cannot safely describe the $m\le17$ clause as proved; resolving this may require a mathematical scope or status change.

FLAG 2  [Conjecture~\ref{conj:S}, Proposition~\ref{prop:CLred}, and all “four open statements” summaries]
The embedded TODO says that (S1) has since been proved, that the per-band constants have changed, and that the composition may require an additional $w$-continuum hypothesis. This conflicts with the abstract, Contribution (iii), Remarks~\ref{rem:S-evidence} and “What is claimed,” and the Discussion/Open lists. No prose-only edit can honestly retain the claim that the asymptotic has been reduced to exactly four open cumulant statements until the mathematical apparatus is updated.

FLAG 3  [Repository availability]
The reproducibility framing requires the placeholder repository URL to be replaced and the cited code, logs, and certificates to be deposited before submission.