# Author decisions before submission — consolidated checklist

*One place for everything that needs Nikol's or Sihao's judgement. Assembled 2026-08-12 from
the three ship reviews, the copyedit pass, and the campaign ledger. Nothing here can be
settled by a model: each item is a data reconciliation, a factual confirmation, or a
scope/venue call.*

## A. Blocking — must be resolved before submission

1. **Read `main.pdf` end to end.** Still owed from 2026-08-06 and more so now: the F2 section
   was rewritten three times on 08-12. This is the one step no review pass replaces.
2. **Repository URL** — two `[repository URL to be added on submission]` placeholders remain.
   Requires the public-artifact decision (a `phase2/bruhat`-only public repo, or opening the
   whole repo after a scrub). Licence is settled: MIT at repo root, arXiv non-exclusive for
   the preprint.
3. **"...independently checked the disclosed constants and counterexamples"** (disclosure
   section) — confirm this sentence is literally true of you both, or soften it.
4. **Fresh pre-submission kill-search** (house rule, Erdősgate). The 2026-08-06 sweep does
   not substitute if submission is weeks later.

## B. Data reconciliations — flagged by the accuracy/consistency reviews

5. **W4/W5 band boundaries**: the paper uses `(8,10]` / `(10,20]`; `sol_comprepair` uses
   `(8,12]` / `(12,20]`. The paper matches every other artifact, so the composition document
   is the likely outlier — but reconcile before print.
6. **W7 margin pair**: paper states `2.2 / 6.6`; the referee-adopted values are `2.71 / 8.17`
   (or `2.42 / 7.28`). Confirm which pair the current composition consumes.
7. **Tie list (Table 1 vs prose)**: the table annotates `D_4`, `D_5` as ties while the two
   prose lists say only `A_5, A_6, A_7, D_6`; the `A_3` row's `[e,12321]` carries no tie tag
   although the reviewer computed `rho([e,w_0(A_3)]) = 25/18` at `k=2`. Recommended: add
   `A_3, D_4, D_5` to both lists and tag the `A_3` row.
8. **The `m >= 561` splice** ("needed only for `m >= 561`", three sites) is not yet citable —
   the hygiene-overlay verifier has not landed. Land it or add the qualifier.

## C. Claims to confirm or soften — flagged by the overclaim review

9. **Observation 7.1's "therefore"** (rank sequence ⟹ parabolic structure) and **Prop 4.7's
   "uniformly"** — each asserts more than the recorded data. Reword unless the stronger
   checks were in fact performed.
10. **The `m <= 17` clause of Theorem F1-smooth** — now correctly attributed to Gasharov 1998
    (the earlier Carrell 1994 attribution was wrong: Carrell–Peterson gives palindromicity,
    not `q`-integer factorization). Confirm the cited theorem yields exactly the stated
    factorization and equality conclusion through `m <= 17`; the working notes verify it
    directly only through `m <= 7`.
11. **Abstract framing of the classical leading term** and the scope of the "alarming trend"
    paragraph — optional rhetorical hedges.

## D. Style items the copyedit declined to touch (would graze mathematics)

12. Notation drift `\sigma_m^2` vs `\sigma^2`; witness-column format mixing in the exhaustive
    table; the unattributed "earlier guess 7/8"; the near-verbatim abstract/introduction
    frontier echo; an unpunctuated decimal-ending sentence in the irreducibility example.

## E. Then

13. **Venue call** — EJC / Sém. Lothar. / Experimental Math. per the paper's own Discussion.
14. Post to **arXiv first** (non-exclusive licence, per the 08-12 decision).

---

## Not author decisions, but open work (no cost, whenever wanted)

- Referee lanes are owed on four campaign documents: `sol_comprepair`, `sol_s3consol`,
  `sol_s5cont`, `sol_s6boot` (all currently zero lanes, all unciteable until they land).
- (S2)'s maths-lane MINOR_REPAIRS are not yet applied to `sol_s2c_20260812.md`.
- The exact-rational redo of the interval certificates — the last standing methodological
  objection; margins are wide enough that a coarse rational envelope would clear it.
