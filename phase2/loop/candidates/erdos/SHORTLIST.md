# Erdős problems worth attempting — a data-driven shortlist

*2026-08-13. Built from `data/problems.yaml` in [teorth/erdosproblems](https://github.com/teorth/erdosproblems),
the community database behind erdosproblems.com. 1217 problems, 604 currently marked open.*

## The selection principle

Tao's [AI-contributions wiki](https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems)
contains the sentence that should drive our choice:

> "absence of past progress may reflect **obscurity** rather than difficulty."

That is the same lesson as everything else today: **the edge is inversely proportional to
attention.** The problems AI has actually cracked (38, 90, 125, 457, 728, 1051, 1196) are mostly
obscure, not famous. Meanwhile the headline problems are being hit by well-resourced teams within
days.

So the filter is deliberately *anti*-prestige:

| Criterion | Why |
|---|---|
| status = open | obviously |
| construction-shaped tags | the answer is an explicit finite object, cheaply verified |
| **no prize** | Erdős's prize is a fame proxy; no prize ⇒ less attention ⇒ our gap |
| has OEIS sequences | computed data exists ⇒ we can extend it locally, for free |

286 of the 604 open problems are construction-shaped, and all 286 carry OEIS links.

**Explicitly NOT recommended:** #142 ($10,000, additive combinatorics / APs) and #3 ($5,000).
Famous, crowded, and hard for real reasons. Prize size is an anti-signal for us.

## Shortlist

| # | Tags | OEIS | Note |
|---|---|---|---|
| **669** | geometry | A003035, A006065, A008997 | generalized Orchard/rich-lines problem; original identification below was wrong |
| 201 | additive combinatorics, APs | A003002–A003005 | the no-3-term-AP / Szekeres sequences; Behrend-type constructions |
| 82 | graph theory | 14 sequences | most computed data of any open problem here |
| 1208 | geometry, distances | A193838, A271490 | adjacent to the unit-distance world that just moved |
| 91 | geometry, distances | A186704 | same neighbourhood |
| 155 | additive combinatorics, Sidon | A143824, A227590, A003022 | A003022 is Golomb rulers — heavily searched already |
| 545, 555, 87 | graph theory, Ramsey | 2 each | small Ramsey-type, construction-shaped |

## Why #669 — CORRECTION 2026-08-13

**The identification in the original section below was wrong.** Erdős #669 is
not a Heilbronn/fixed-area-triangle problem. It asks for the maximum numbers
\(f_k(n)\) and \(F_k(n)\) of lines containing exactly/at least \(k\) among \(n\)
planar points. The correct attack now lives in `../../erdos669/`. The text below
is retained as an audit trail for how an OEIS-only guess failed; do not use its
Golod--Shafarevich/Heilbronn recommendation.

Two independent lines of evidence converged on it today, which has not happened for anything else
this session.

1. **The filter surfaced it**: open, geometry, no prize, three OEIS sequences of computed data.
2. **The unit-distance sweep named it independently.** When asked where the Golod–Shafarevich
   tower technique might transplant, that lane answered: *Heilbronn / fixed-area triangle
   analogues — the strongest surviving geometric targets with the same "only subpolynomial
   improvement is possible" smell.* A003035 and A006065 appear to be Heilbronn-triangle sequences.

If that identification is right, #669 sits exactly where a freshly-validated technique points and
where the database says nobody has been looking. That is the profile we have been hunting all day.

## Caveats — all three are serious

1. **The database status is stale.** Only 8 entries were updated in July 2026 and none in August,
   so Astra's 1 August additions are not reflected. "Open" in this file means "open as of the last
   edit", not "open today".
2. **I could not read the problem statements.** erdosproblems.com renders them in JavaScript and
   returns 403 to plain fetches; the OEIS API is blocked from this environment. The
   identifications above come from recognising A-numbers — **A003002–A003005 (no-k-term-AP) and
   A003022 (Golomb rulers) I am confident about; the Heilbronn reading of A003035/A006065 is a
   guess and must be checked before any work starts.**
3. **Erdősgate risk is at its maximum in this domain.** Problem 333 was "solved" by GPT-5.2 at
   Christmas 2025 and turned out to be Erdős's own 1977 result. A per-problem kill-search is
   mandatory, not optional.

## Proposed next steps

1. **Read the statements** for #669, #201, #82, #1208 — trivial in a browser, currently blocked
   for me. This also settles caveat 2.
2. **Status-sweep the top three.** They are obscure, so a sweep is cheap and decisive, and it
   addresses caveats 1 and 3 together.
3. **Then attack**, with the construction framing rather than search: what representation makes
   the object natural?
