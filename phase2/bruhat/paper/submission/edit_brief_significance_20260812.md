# Second edit brief — make the case for the paper, without overselling

*2026-08-12, from the corresponding author. The style pass is done; this is about
significance. The paper currently reads as a competent report of things that were done. It
does not tell the reader why any of it matters. Fix that — in the abstract's framing, the
introduction, and the Discussion — while keeping the measured register of the first pass.*

## Same absolute constraint as before

**Change no mathematics.** No theorem, constant, numeral, table entry, equation, label,
citation key, or scope condition. This is framing only. Where the significance depends on
a statement's strength, describe the strength accurately rather than inflating it.

## The case that is actually available (use this; do not invent more)

1. **A real frontier extension, stated concretely.** 1,079,490,991 intervals in exact
   integer arithmetic, roughly an order of magnitude past the previously recorded frontier,
   and it settles specific cases left open in Brenti's own list ($A_6$, $A_7$, the full
   range of $B_5$, $B_6$, $D_6$, $E_6$). Concrete and checkable beats adjectives.

2. **The extremal conjecture is the structurally interesting idea, and the paper
   undersells it badly.** If true, it collapses the problem: instead of checking
   exponentially many Bruhat intervals in a group, one checks a *single* interval,
   $[e,w_0]$, whose rank sequence is the Poincare polynomial's coefficient sequence. That
   is a reduction from an intractable verification to a tractable one, and it is why the
   type-$A$ analysis is possible at all. Say this plainly, and say equally plainly that it
   is a conjecture, proved here only for rationally smooth lower intervals in the stated
   finite ranges.

3. **The conjecture also explains an alarming-looking pattern in the data.** Minimum
   ratios decay toward 1 as rank grows, which reads like a counterexample waiting a few
   ranks out. The type-$A$ analysis says why that never happens: along the extremal family
   the ratio approaches 1 at a determined rate and stays above it. Explaining away an
   apparent impending failure is worth a sentence.

4. **A bridge between two literatures.** The extremal ratio in type $A$ is the central
   ratio of the Mahonian distribution, which puts a question about Bruhat order into
   contact with classical local-limit and log-concavity analysis. Note honestly what is new
   versus known: log-concavity of the Mahonian numbers is classical (Bona; Hoggar/Kook),
   and Canfield--Janson--Zeilberger already give the $1+\sigma^{-2}$ central ratio for the
   Gaussian binomial; the paper's contribution is the $S_m$ case with the *global* minimum
   statement and explicit constants. Do not let the reader think the classical part is ours.

5. **A structural reason for the crystallographic boundary.** The conjecture holds for Weyl
   groups but fails for $H_3$. The paper's equality analysis finds equality only in
   rank-two dihedral patterns of order $m \in \{4,6\}$ --- both crystallographic --- while
   Brenti's $H_3$ counterexample sits on a dihedral core of order $5$, which is not. That
   is a candidate explanation for *why* the crystallographic restriction is the right
   dividing line, and it is more interesting than "we also classified equality cases."

6. **Reusability.** The verification is exact-arithmetic and reproducible, and the
   conditional asymptotic is reduced to explicitly stated cumulant statements with explicit
   constants --- so a later reader can attack a named, self-contained target rather than
   reconstruct the reduction.

## What must NOT happen

- No claim that Brenti's conjecture is proved, nearly proved, or close to resolution.
- No suggestion that the extremal conjecture is established; it is a conjecture with a
  proved subclass.
- No suggestion that the sharp asymptotic is unconditional; it rests on one stated lemma
  which itself reduces to open statements.
- No "we are the first to", "for the first time", "long-standing open problem", "major
  advance", "breakthrough", "sheds new light", "opens the door to".
- No adjective doing work a number could do. If the frontier moved by an order of
  magnitude, say the numbers.
- Keep the first pass's register: plain, direct, first person plural, no salesmanship. The
  goal is that a knowledgeable reader finishes the introduction understanding why they
  should care --- not that they feel sold to.

## Where to put it

- **Abstract**: one or two sentences of framing, no more. The reduction idea (item 2) is
  the one worth the space.
- **Introduction**: this is the main target. It should open with why the problem is
  interesting and what changes here, before the contribution list. The contribution list
  itself can stay factual.
- **Discussion**: the status-by-logical-strength structure from the first pass stays. Add,
  after it, a short paragraph on what this buys a future reader --- items 2, 5, 6.

## Output format

Numbered edit list, exactly as before:

```
EDIT n  [section context]
OLD: <exact text from main.tex, unique>
NEW: <replacement>
WHY: <one line>
```

Flag separately any place where making the case honestly would require a mathematical
claim the paper does not currently support.
