# Cross-examination of the theory probe (Claude agent + web, 2026-07-04)

> Second independent read attacking the three "apparently new" claims from
> `theory_probe_gpt55_39009.md` (house rule: never trust a single-model
> literature read). Verdict: **all three stand**, with one serious near-miss
> on F2 that changes how it must be positioned in any writeup.

## CLAIM 1 — extremal interval is [e,w0] in simply-laced Weyl groups: **STANDS**

Searches: Brenti OPAC full text (arXiv:2410.09897 IS the OPAC survey);
Bjorner-Ekedahl (10.4007/annals.2009.170.799) full citation trail;
Burrull-Gui-Hu (2311.17980) + its citers; direct queries on extremal/minimum
ratio statements. Brenti states Conj 2.11 + the H3 counterexample
(u=s3, v=s1s2s3s2s1s2s1s3, ranks 1,3,5,7,10,10,5,1) but NOTHING about which
interval minimizes the ratio. Citation-trail citers (2309.08539 interval
sizes, 2501.03037 Lehmer complex, 2504.06161 Soergel) don't touch it.
Red herrings cleared: 2606.11776 proves Brenti's 2003 R-polynomial
conjecture (not 2.11); 2507.14033 is geometric.
Closest near-miss: 2205.05408 (equivariant log-concavity of flag-variety
cohomology) concerns exactly the [e,w0] polynomial but says nothing about
minimality over intervals.

## CLAIM 2 — Mahonian min ratio 1+Theta(1/m^3): **STANDS, with a MUST-CITE near-miss**

**Canfield-Janson-Zeilberger (arXiv:0908.2089, Adv. Appl. Math. 2011),
eq. (4.11) + Theorem 4.6** already prove, for the CENTRAL GAUSSIAN BINOMIAL
c_j = [q^j] binom(2n,n)_q in the central window k = mu + O(sigma):

    P(k)^2 - P(k-1)P(k+1) = (sigma^-2 + O(n^-4)) P(k)^2

i.e. central log-concavity ratio = 1 + sigma^-2 (1+o(1)) — the ratio-form
asymptotic, by a generic Gaussian-transfer argument (their Remark 4.7).
BUT: (i) only for the two-letter/q-binomial case, NOT the q-factorial
(S_m Mahonian); (ii) only the central window, no global-minimum claim;
(iii) the constant 36/m^3 appears nowhere.
=> F2 must be framed as: "explicit constant + global minimum + S_m case,
via CJZ's technique (Thm 4.6 / eq. 4.11)". A short corollary of published
technique, not an independent discovery.

Other checks negative: Margolius (JIS 2001), Louchard-Prodinger (JIS),
OEIS A008302, 2408.02424, Annals of Comb. 2022 type-B analogue —
qualitative log-concavity only; no ratio statements; "36/m^3"/"n^3/36"
nowhere.

## CLAIM 3 — equality only via rank-two dihedral patterns: **STANDS**

No published characterization of equality cases of a_k^2 = a_{k-1}a_{k+1}
for Bruhat rank sequences found. Near-misses are all about DIFFERENT
inequalities: Stanley-Yan matroid equality (2407.19608), Kahn-Saks extremals
(2309.13434), Stanley poset inequality equality (2211.14252), rank-symmetric
intervals via 3412/4231-avoidance (2003.06710), Marietti dihedral-interval
work (KL/R-polynomials, not rank sequences), 2110.00862 (interval
classification, no log-concavity).

## Caveats
- No MathSciNet/zbMATH access; MathOverflow blocked to the fetcher — only MO
  threads ranking in general web results would have surfaced (none did).
- The equality-cases area is ACTIVE (Stanley-Yan 2024, Kahn-Saks 2023,
  Alexandrov-Fenchel 2023) — re-sweep arXiv immediately before submission.

## Bottom line
All three findings survive two independent literature reads. F1 and F3 appear
genuinely new. F2 is a corollary-with-new-constant of CJZ and must cite their
Theorem 4.6/eq. (4.11) prominently.
