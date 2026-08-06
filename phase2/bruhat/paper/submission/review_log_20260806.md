# Review log for main.tex, 2026-08-06

Three independent adversarial review passes (read-only agents, each
explicitly barred from editing files) plus my own follow-up fixes and
independent web verification of every bibliography correction before
applying it.

## Pass 1: mathematical accuracy vs. source material
Found: F1/F2/F3 content generally accurate; one wrong constant traced to
unverified draft material (fixed pre-review, during drafting: variance
bound cited as 1/4, should be the T2-verified 1/6).

## Pass 2: academic style / completeness
Found and fixed: 5 bibliography entries with fabricated/wrong author
attributions (verified independently via WebFetch against arXiv before
fixing); page-overflow bug truncating Theorem V2 and Table 2 in the
compiled PDF; missing MSC classification and keywords; 6 uncited
bibliography entries (now cited or corrected); title omitted the F2
contribution.

## Pass 3: mathematical accuracy (second, independent pass) + attribution/overclaim
Found and fixed:
- **Most serious finding**: the seeded-tier interval counts (204,000 /
  264,000 total) were inflated ~3x. `seeded_probe.py` silently discards
  perturbation attempts that don't form a valid Bruhat up-cover chain;
  the paper had reported the attempt count, not the surviving/actually-
  checked count. Independently re-verified by direct arithmetic on the
  raw result files (not just trusting the reviewing agent): true counts
  are 1,324 / 32,458 / 31,162 (sum 64,944), not 4,000 / 100,000 / 100,000.
  Corrected everywhere (Table 3, Proposition V3, abstract, introduction,
  Discussion) and added an explicit remark explaining the attempt-vs-
  survivor distinction.
- One real overclaim: introduction called the F2 asymptotic "a theorem"
  when the paper's own F2 section and abstract correctly call it a
  conjecture. Fixed to match.
- "confirmed to six significant digits" -> actually four digits per
  source. Fixed.
- Theorem G1's exact-arithmetic range conflated two different verified
  ranges (m<=109 for the pointwise bound, m<=229 for the window law).
  Split out explicitly.
- "only cosmetic repairs required" overstated the referee's own verdict
  ("survives with minor repairs"). Fixed to match the referee's language.
- A fabricated "%" sign on the F3 section's "margins 4-8" figures (these
  are unitless integer margins, not percentages). Fixed.
- F1-smooth theorem's "unconditional for m<=17" omitted a caveat the
  referee explicitly flagged (rests on a classical citation verified only
  through m<=7 in our own working notes). Added.
- A structural gap: the "staircase domination" conjecture was referenced
  only inline, never given its own numbered environment. Split
  Theorem F1-smooth accordingly and added Conjecture (staircase
  domination) as its own environment.
- Confirmed independently (fetched Brenti's actual arXiv PDF): the H3
  counterexample quotation is word-for-word, number-for-number correct,
  including the page reference -- the paper's strongest-verified claim.
- Confirmed independently (re-summed all 17 exhaustive-tier rows from
  source): the abstract's 1,079,490,991 total is exact.
- Acknowledgments section judged well-calibrated (specific about AI's
  role, clear on human final responsibility); added Section F3 to the
  AI-attribution sentence per the reviewer's suggestion.

All bibliography corrections in Pass 2/3 were independently re-verified
by fetching the actual arXiv abstract pages myself before applying any
fix, not merely trusted from the reviewing agent's report.
