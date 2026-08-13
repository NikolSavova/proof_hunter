# Decisions a human must make before this note is submitted

*Companion to `main.tex`. Same role as `AUTHOR_DECISIONS.md` in the Bruhat paper: everything
below is a judgement call that should not be made by an automated system, or a fact that needs
eyes on a physical source. Written 2026-08-13.*

## Blocking

1. **Both authors read `main.pdf` end to end.** The note is 7 pages and the mathematics is
   elementary; this is a short read and there is no excuse for skipping it. Nikol in particular
   should check Lemma 2.1 (the Legendre verification) and the proof of Corollary 4.2, which is
   the only place we lean on another paper's hypotheses rather than on our own computation.

2. **Confirm the published venue of the Bauschke–Macklem–Wang survey.** We cite the arXiv
   version, `arXiv:1003.3127`. It also appeared as a chapter in a Springer volume
   (*Fixed-Point Algorithms for Inverse Problems in Science and Engineering*, Springer
   Optimization and Its Applications, around 2011). **Neither the volume number nor the page
   range has been verified against the physical source.** Either verify and cite the chapter, or
   deliberately cite only the arXiv version. Do not guess the pages.

3. **Confirm the numbering "Problem 2" and "Fact 3.2" against the survey PDF.** Our entire
   framing is "we answer Problem 2 attached to Fact 3.2". The problem statement in
   `../PROBLEM.md` was frozen from a corpus record, not read off the paper. If the survey
   numbers its open problems differently, every reference to Problem 2 in the note is wrong.
   This is cheap to check and embarrassing to get wrong.

4. **Read Example 3.3 of the survey.** The note's "What is not claimed" paragraph asserts that
   the survey already contains nonconvex Chebyshev examples and that ours is distinguished by
   being *globally* Chebyshev with (b) holding. If Example 3.3 is already global and already
   satisfies (b), our contribution shrinks to almost nothing and the note should be withdrawn or
   substantially reframed. This is the single highest-risk unverified statement in the paper.

## Verification carried out, and its limits

5. **Three independent Sol lanes at effort=max re-checked Part I on 2026-08-13**
   (`../verify1_v1_maths_20260813.md`, `../verify1_v2_sun_20260813.md`,
   `../verify1_v3_novelty_20260813.md`), on top of the two lanes of 2026-08-12. Read the
   verdicts before submitting; do not take this file's summary for them.

6. **The prior-art lane was briefed on how the Part II clearance failed.** Part II of this
   project died because its clearance asked "did Luo remove full domain?" (no) instead of "did
   Luo remove the hypothesis *we* remove?" (yes). The Part I lane was told this explicitly and
   asked to find the analogous wrong question. That is a mitigation, not a guarantee.

7. **What the numerics do and do not establish.** `../verify.py` and `../sun_check.py` are
   finite checks. They would have caught a false claim cheaply and did not; they certify no
   universal quantifier. Every quantified statement in the note is carried by a hand proof.

## Claims to confirm before submission

8. **Corollary 4.2 is the second payload and it rests on someone else's hypotheses.** We claim
   our example satisfies the hypotheses of `[LMWY2019, Thm 3.13]` and `[LMWY2019, Thm 3.12(3)]`.
   The total-convexity verifications are ours and are in the proof; the theorem statements are
   quoted from a `pdftotext` extraction of a paywalled paper. **Someone should read the actual
   typeset Theorems 3.12 and 3.13 in the PDF** and confirm the hypothesis lists match what the
   corollary claims. Extraction artefacts around the over-arrow notation are a real risk.

9. **Decide whether Corollary 4.2 stays.** It strengthens the note considerably — the example
   then bears on two papers rather than one — but it is also the part most likely to draw a
   referee objection, since it interprets another group's theorem. The conservative option is to
   demote it to a remark. Recommendation: keep it, because it is the difference between "here is
   a counterexample" and "here is why the hypothesis is structural".

10. **Proposition 5.1 must stay attributed.** It says hypothesis (b) is redundant. We proved this
    independently and it survived four adversarial passes, and it is *not ours* — it follows from
    Luo et al. in a few lines. It is in the note for completeness of the account of Fact 3.2, and
    the attribution in its statement and proof must not be softened.

## Style and framing

11. **Title.** Currently "Full domain cannot be dropped from a theorem on right
    Bregman–Chebyshev sets" — declarative, colon-free, narrow. Alternatives considered and
    rejected as overclaiming: anything containing "necessary" (the result is about deleting a
    hypothesis from a universal statement, not about necessity in each instance).

12. **Byline.** Mirrors the Bruhat paper: empty `\author{}` with the names in a first-page
    footnote, because the work was substantially AI-assisted. Keep the two conventions
    identical across both papers or change both.

13. **Venue.** This is a short note settling one open problem from a survey. Plausible homes:
    *Journal of Convex Analysis*, *Optimization Letters*, *Journal of Optimization Theory and
    Applications*, or arXiv only. Given the size of the result, arXiv plus a short-note journal
    seems right. Not a decision for an automated system.

14. **Lean statement stub** — still unwritten, still optional. Theorem 3.1 is elementary enough
    that a formalisation is realistic, and would be a genuine differentiator for a note this
    small.
