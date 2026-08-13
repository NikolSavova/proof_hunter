# Copy-edit brief for `main.tex` — hedging, authorship, and de-AI-ing the prose

*Instructions to the editing pass, 2026-08-12, from the corresponding author (Sihao).
Kept as a reviewable artifact alongside the change log.*

## Absolute constraint

**Do not change any mathematics.** No theorem, lemma, conjecture, hypothesis, constant,
numeral, table entry, equation, label, citation key, or scope condition may be altered.
This is a prose and framing edit only. If a sentence cannot be improved without touching a
mathematical claim, leave it alone and say so. Where a claim's *strength* is at issue
(item 1), the fix is hedging language around an unchanged statement, never a changed
statement.

## 1. Hedge the framing, and sharpen the conclusions

- **The title is over-assertive.** Current:
  `Log-concavity of Bruhat intervals in Weyl groups: extended verification, an extremal
  conjecture, Mahonian asymptotics, and equality cases`
  It reads as a list of delivered goods, two of which are conjectural or conditional.
  Propose 2-3 alternatives that are accurate about what is proved versus conjectured
  versus conditional. Shorter is better. Avoid the four-item subtitle pile-up.
- **The abstract and introduction should be more measured** about what the paper
  establishes. In particular the F2/Mahonian material is a theorem *conditional* on an
  explicitly stated lemma, with four (now three-plus) open supporting statements; the
  extremal conjecture (F1) is a conjecture supported by exhaustive computation in low rank
  plus a proved subclass. Say so plainly and early rather than letting the reader infer it
  from a later section.
- **Frame the conclusions more clearly.** The Discussion should state, in order and
  without hedging *language* obscuring the content: what is proved unconditionally, what
  is proved conditionally and on what, what is conjectured, and what is open. A reader
  should be able to answer "what did this paper actually establish?" from that section
  alone.

## 2. Authorship moves to a footnote

Remove the two `\author{}`/`\address{}`/`\email{}` blocks from the title page as displayed
authors, and instead record authorship in a footnote on the first page. The reason, which
the footnote should convey without melodrama: **the work was substantially AI-assisted**,
and the named humans do not want the conventional byline to overstate their personal
contribution. Draft the footnote text; keep it factual, brief, and unapologetic — one or
two sentences, stating that the investigation was carried out with substantial assistance
from automated systems and naming the people who directed and take responsibility for it.
Use the `amsart` mechanism that actually compiles (e.g. `\thanks` on the title, or
`\footnotetext`), and keep both names and emails discoverable so the paper remains
citable and correspondence works.

## 3. Remove the AI tics — write like a mathematician

The prose has a recognizable machine register. Fix it throughout. Concrete examples the
author flagged:

| current | problem | direction |
|---|---|---|
| "with zero violations found" | telemetry-speak, not mathematics | "no interval violated log-concavity", or simply state the result |
| "every Bruhat interval is checked" | agentless passive that hides who did what | "we checked every Bruhat interval" |
| "An extremal conjecture, apparently new" | hedge-as-decoration; "apparently" is doing no work | state the conjecture; if novelty is a claim, make it once, in prose, with the literature check behind it |

The general faults to hunt:

- **Nominalizations and passive agentlessness.** Mathematicians write "we prove", "we
  verify", "we do not know". Restore the first person plural where the paper is reporting
  its own work.
- **Inflated qualifiers**: "apparently", "notably", "importantly", "it is worth noting
  that", "crucially", "remarkably". Delete or replace with the substance.
- **Triplet/parallel-list padding** and sentences whose clauses restate each other.
- **Résumé verbs applied to mathematics**: "leverages", "showcases", "highlights",
  "underscores", "delivers", "provides insight into".
- **Em-dash asides used as a default connective**, and paragraph-opening transitions
  ("Moreover", "Furthermore", "Additionally") used to stitch unrelated points.
- **Over-signposting**: "In this section we will", "As we shall see", "It is important to
  note". Mathematicians signpost sparingly.
- **Numbers dressed up**: prefer "1,079,490,991 intervals" plainly stated once to repeated
  restatement with adjectives.

Target register: a working combinatorialist writing for *Electronic J. Combinatorics* or
*Experimental Mathematics*. Plain, direct, unshowy. Short declarative sentences. Technical
terms spelled out. No salesmanship.

## Output format

Return a **numbered edit list**, not a rewritten file. Each entry:

```
EDIT n  [section/line context]
OLD: <exact text as it appears in main.tex, long enough to be unique>
NEW: <replacement>
WHY: <one line>
```

Plus a short preamble with your 2-3 title proposals and the drafted authorship footnote.
Exact `OLD` strings matter — they will be applied mechanically. Do not propose edits inside
displayed mathematics. Flag separately, at the end, any place where the prose seems to
overstate a mathematical claim and the fix requires an author decision rather than a
wording change.
