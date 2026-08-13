# Part I verification gate — v3_novelty (gpt-5.6-sol, effort=max, 2026-08-13 07:42)

> Independent re-verification of Part I before write-up. The prior-art lane
> was briefed on how the Part II clearance failed, so it looks for the
> analogous wrong question rather than repeating the same check.

## Prior-art verdict: **AMBER**

### Bottom line

I found **no published source that contains the decisive feature of your construction**:

\[
C\text{ globally right-}D_f\text{-Chebyshev},\qquad
\overline{\nabla f(C)}\subset U^*,\qquad
\nabla f(C)\text{ nonconvex},
\]

for negative entropy or, equivalently, a **nonconvex globally left-\(D_h\)-Chebyshev set** for

\[
h(u)=e^{u_1}+e^{u_2}.
\]

I also found **no claimed solution of the survey’s Problem 4**, i.e. no characterization of all right-Chebyshev sets for negative entropy.

However, the construction is very close to—and must be expressly distinguished from—Bauschke–Wang–Ye–Yuan’s 2009 Example 7.5, restated as Example 3.3 in the 2010 survey. That example already establishes that a **nonconvex set \(C\)** can be globally right-Chebyshev for negative entropy. What it does **not** establish is your load-bearing point: its gradient image \(C^*\) is a convex line segment. ([arxiv.org](https://arxiv.org/pdf/1003.3127))

Thus:

- **Broad claim:** “first nonconvex right-Chebyshev set for negative entropy” — **already published and false as a novelty claim**.
- **Narrow claim:** “first example with the retained closure condition and nonconvex \(C^*\), disproving deletion of full domain in Fact 3.2” — **no prior publication found**.
- Given inaccessible full text and citation indexes, particularly for Luo et al. and the monographs, I would not issue unconditional GREEN yet.

---

# 1. The closest prior art: Bauschke–Wang–Ye–Yuan (2009)

**Heinz H. Bauschke, Xianfu Wang, Jane Ye, Xiaoming Yuan**,  
“Bregman distances and Chebyshev sets,”  
*Journal of Approximation Theory* **159**(1), 3–25 (2009).  
DOI: `10.1016/j.jat.2008.08.014`  
arXiv: `0712.4030`  
URL: `https://arxiv.org/abs/0712.4030` ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0021904508001652))

### What Example 7.5 actually does

It starts on the **exponential side** with

\[
h(u_1,u_2)=e^{u_1}+e^{u_2}
\]

and the convex line segment

\[
A=\{(\lambda,2\lambda):0\leq \lambda\leq1\}.
\]

Its gradient image is

\[
\nabla h(A)=\{(e^\lambda,e^{2\lambda}):0\leq\lambda\leq1\},
\]

which is nonconvex. By Bregman duality, that exponential curve is a nonconvex right-Chebyshev set for negative entropy. But its negative-entropy gradient image is exactly \(A\), hence convex. ([arxiv.org](https://arxiv.org/pdf/0712.4030))

The exact comparison is therefore:

| 2009 Example 7.5 | Your construction |
|---|---|
| Dual set \(A=\{(\lambda,2\lambda)\}\) | Dual set \(A=\{(t,-t^2)\}\) |
| \(A\) convex | \(A\) nonconvex |
| Entropy-side \(C=\exp(A)\) nonconvex and right-Chebyshev | Entropy-side \(C=\exp(A)\) nonconvex and right-Chebyshev |
| \(\nabla f(C)=A\) convex | \(\nabla f(C)=A\) nonconvex |
| Does not refute Fact 3.2 without full domain | Does refute Fact 3.2 without full domain |

### Assessment

Your example is unquestionably a **variation on the duality template** of Example 7.5. It is not merely a reparametrization, however: replacing the convex line segment by a nonconvex parabolic arc while preserving global left-Chebyshevness is precisely the missing step needed to answer the full-domain question negatively.

**This work is mandatory to cite.**

---

# 2. Bauschke–Macklem–Wang survey and Problem 4

**Heinz H. Bauschke, Mason S. Macklem, Xianfu Wang**,  
“Chebyshev Sets, Klee Sets, and Chebyshev Centers with respect to Bregman Distances: Recent Results and Open Problems,” 2010.  
arXiv: `1003.3127`  
URL: `https://arxiv.org/abs/1003.3127` ([arxiv.org](https://arxiv.org/abs/1003.3127))

The survey records:

- Fact 3.2 with full domain and the dual-closure condition;
- the question whether full domain is essential;
- Example 3.3, copied from the 2009 Example 7.5;
- Problem 4 asking for a characterization of negative-entropy right-Chebyshev subsets. ([arxiv.org](https://arxiv.org/pdf/1003.3127))

The survey itself expressly observes that Example 3.3 has a non-full-domain generator but nevertheless retains the conclusion \(C^*\) convex. It therefore does **not** anticipate your counterexample. ([arxiv.org](https://arxiv.org/pdf/1003.3127))

### Problem 4 search result

I found no later article claiming to characterize all right-Chebyshev subsets of the positive orthant for negative entropy. In particular:

- no exact-title or exact-problem search produced a purported solution;
- no formula search for \((e^t,e^{-t^2})\), \((t,-t^2)\), “parabolic arc,” or “sum of exponentials Chebyshev set” found a relevant mathematical source;
- the later domain-aware Bregman-operator papers examined below do not provide an entropy-specific classification.

Your construction therefore **does not appear to have been subsumed by a solution of Problem 4**. It also should not be presented as solving Problem 4: it only adds another explicit member to the class Problem 4 asks to characterize.

**The survey is mandatory to cite, including Example 3.3 and Problems 1, 2, and 4.**

---

# 3. Luo–Meng–Wen–Yao (2019)

**Xian-Fa Luo, Li Meng, Ching-Feng Wen, Jen-Chih Yao**,  
“Bregman distances without coercive condition: suns, Chebyshev sets and Klee sets,”  
*Optimization* **68**(8), 1599–1624 (2019).  
DOI: `10.1080/02331934.2019.1625898`  
URL: `https://doi.org/10.1080/02331934.2019.1625898` ([openurl.ebsco.com](https://openurl.ebsco.com/results?bquery=AU+Luo%2C+Fa&page=1&sid=ebsco%3Aocu_results%3Acache))

### What I could verify

The accessible abstract describes:

- Bregman suns and their relation to convexity;
- Chebyshev and Klee sets without the usual coercivity assumptions;
- necessary and sufficient conditions in the Banach-space setting. ([researchgate.net](https://www.researchgate.net/publication/255637485_BREGMAN_DISTANCES_AND_KLEE_SETS_IN_BANACH_SPACES))

According to the theorem information in your supplied post-mortem, Theorem 3.12 removes the dual-closure assumption relevant to your former Part II, but **retains \(U=X\)** in the part corresponding to the right projection. That does not settle Part I.

### Remaining novelty risk

I could not retrieve the complete publisher text, so I could not independently inspect:

- every example following Theorem 3.12;
- remarks concerning necessity of full domain;
- whether the authors exhibit a nonconvex Chebyshev-but-not-sun set for a noncoercive exponential-type generator.

The title “without coercive condition” makes this the **highest-risk unchecked source**, particularly because your dual formulation also shows:

\[
A=\{(t,-t^2):1\le t\le2\}
\]

is nonconvex and left-\(D_h\)-Chebyshev for a non-supercoercive \(h=\sum e^{u_i}\). In other words, your construction also demonstrates that the supercoercivity assumption in the survey’s Fact 3.1 cannot simply be deleted. Luo et al. is exactly where a referee will look for that issue.

### Assessment

- No accessible evidence that Luo et al. already contain your example or implication.
- Nevertheless, **full manual inspection of all examples and remarks in the paper is a pre-submission requirement**.
- Luo et al. must be cited both for Part II history and to distinguish Chebyshev sets from Bregman suns.

---

# 4. Laude–Ochs–Cremers (2020)

**Emanuel Laude, Peter Ochs, Daniel Cremers**,  
“Bregman Proximal Mappings and Bregman–Moreau Envelopes under Relative Prox-Regularity,”  
*Journal of Optimization Theory and Applications* **184** (2020).  
arXiv: `1907.04306`  
URL: `https://arxiv.org/abs/1907.04306`

### Relevance and distinction

This work belongs to the nonconvex Bregman proximal-mapping literature and studies single-valuedness and regularity under relative prox-regularity. Its relevance is principally **local**:

- relative prox-regularity can yield local single-valuedness near suitable graph points or for suitable parameters;
- it does not, merely from prox-regularity, establish that a nonconvex curve has a unique Bregman projection from **every** point of the whole natural domain.

Your curvature argument supplies that much stronger global property directly.

I did not recover the complete text in this pass, so the theorem-level distinction should be page-checked. I found no indication that it contains the entropy parabola, an entropy-specific characterization, or a counterexample to Fact 3.2.

### Assessment

**AMBER-adjacent, not presently a kill.** It should be cited if the paper discusses nonconvex Bregman projection mappings or global versus local uniqueness.

---

# 5. Themelis–Wang (2025)

**Andreas Themelis, Ziyuan Wang**,  
“On the natural domain of Bregman operators,”  
arXiv: `2506.00465`, v2 dated October 11, 2025.  
URL: `https://arxiv.org/abs/2506.00465` ([arxiv.org](https://arxiv.org/pdf/2506.00465))

### What it does

The paper develops left and right Bregman proximal mappings and envelopes on their natural domains, emphasizing that functions need not be artificially extended to all of \(\mathbb R^n\). It cites the 2009 Chebyshev paper as motivation, then develops general proximal and conjugacy representations. ([arxiv.org](https://arxiv.org/pdf/2506.00465))

A full-text search produced no occurrence of “entropy,” and “Chebyshev” appears only in the motivational/reference context rather than as an entropy classification or a new global Chebyshev theorem. ([arxiv.org](https://arxiv.org/pdf/2506.00465))

### Assessment

It may provide modern language in which to express your construction—as a globally single-valued right proximal map of an indicator—but it does **not** appear to contain or imply the specific counterexample without adding your global curvature calculation.

**Recommended citation**, especially if discussing natural-domain conventions.

---

# 6. Other works screened

## Bauschke–Macklem–Sewell–Wang (2010)

**Heinz H. Bauschke, Mason S. Macklem, Jason B. Sewell, Xianfu Wang**,  
“Klee sets and Chebyshev centers for the right Bregman distance,”  
*Journal of Approximation Theory* **162**, 1225–1244 (2010).  
DOI: `10.1016/j.jat.2010.01.001`  
arXiv: `0908.2013`  
URL: `https://arxiv.org/abs/0908.2013`

This is about farthest-point/Klee sets and Chebyshev centers, not characterization of nearest-point Chebyshev sets. No target example was found. ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0021904510000195))

## Li–Song–Yao (2010)

**Chong Li, Wen Song, Jen-Chih Yao**,  
“The Bregman distance, approximate compactness and convexity of Chebyshev sets in Banach spaces,”  
*Journal of Approximation Theory* **162**(6), 1128–1149 (2010). ([m.mathnet.ru](https://m.mathnet.ru/php/archive.phtml?WHATTOSHOW=FORWARDLINKS&jrnid=rm&option_lang=eng&paperid=4976&wshow=paper_refs))

This is directly adjacent on Banach-space convexity and approximate compactness, but I did not obtain full text. Nothing in the accessible record identifies a right-negative-entropy example or a characterization of Problem 4.

## Burachik–Dao–Lindstrom

- “The Generalized Bregman Distance,” arXiv: `1909.08206`;
- “Generalized Bregman Envelopes and Proximity Operators,” *JOTA* **190**(3), 744–778 (2021), DOI `10.1007/s10957-021-01895-y`, arXiv: `2102.10730`.

These develop generalized Bregman distances, coercivity, envelopes, and proximity operators. Their accessible abstracts do not address global D-Chebyshev-set classification or the entropy parabola. ([arxiv.org](https://arxiv.org/abs/1909.08206))

## 2026 Kostecki manuscripts

Open-web citation searching located 2026 Vainberg–Bregman manuscripts whose bibliographies include Luo et al., but I found no substantive treatment of the survey’s full-domain question or your example. ([fuw.edu.pl](https://www.fuw.edu.pl/~kostecki/bregman_operations.pdf))

---

# 7. Is the construction “folklore” or routine?

I found no evidence that the exact parabolic construction is written down.

Nevertheless, a referee may reasonably view its **method** as elementary once the 2009 duality framework is recognized:

1. Work on the exponential side.
2. Choose a nonconvex one-dimensional arc \(a(t)\).
3. Show that
   \[
   t\longmapsto D_h(a(t),y)
   \]
   is strictly convex for every \(y\).
4. Transfer through \(\nabla f=\log\).

That is not enough to destroy novelty: the 2010 survey expressly left the corresponding assumption question open. But it means the contribution should be positioned as a **small explicit counterexample resolving a precise hypothesis question**, not as a broad new theory of Bregman Chebyshev sets.

The honest characterization is:

> **Small but apparently new, when stated narrowly.**

---

# 8. Narrowest defensible novelty statement

I recommend language along these lines:

> Bauschke–Wang–Ye–Yuan previously exhibited nonconvex right-Chebyshev sets for negative entropy, but their examples have convex gradient image. We construct a compact right-Chebyshev set \(C\subset\mathbb R_{++}^2\) for which \(\nabla f(C)\) is nonconvex. Thus, even while retaining \(\overline{\nabla f(C)}\subset U^*\), the full-domain assumption in Theorem 7.3/Fact 3.2 cannot simply be omitted.

Add immediately:

> Equivalently, the parabolic arc \(\{(t,-t^2):1\le t\le2\}\) is a compact nonconvex globally left-\(D_h\)-Chebyshev set for \(h(u)=e^{u_1}+e^{u_2}\).

Avoid:

- “the first nonconvex right-Chebyshev set for entropy”;
- “a characterization of entropy right-Chebyshev sets”;
- “full domain is necessary” without the qualification “cannot simply be deleted from the universal implication”;
- an unconditional priority claim until Luo et al. and closed citation databases have been manually checked.

---

# 9. Works that must be cited

## Mandatory

1. **Bauschke–Wang–Ye–Yuan (2009)** — Proposition 7.1, Theorem 7.3, Example 7.5.
2. **Bauschke–Macklem–Wang (2010)** — Fact 3.2, Example 3.3, Problems 1, 2, and 4.
3. **Luo–Meng–Wen–Yao (2019)** — especially Theorem 3.12 and the sun/Chebyshev distinction.

## Strongly recommended

4. **Laude–Ochs–Cremers (2020)** — to distinguish local nonconvex proximal regularity from global Chebyshevness.
5. **Themelis–Wang (2025)** — modern natural-domain treatment of left/right Bregman operators.
6. **Li–Song–Yao (2010)** — Banach-space Chebyshev convexity without relying solely on the finite-dimensional literature.

---

# 10. What I could not check

The following prevent an unconditional GREEN clearance:

- The complete paywalled text of **Luo et al. (2019)**, particularly all examples and remarks surrounding Theorem 3.12.
- Complete citation graphs in **MathSciNet, zbMATH, Scopus, Web of Science, and Google Scholar cited-by**.
- Dissertations and non-English literature not indexed by ordinary web search.
- Page-level searches of:
  - Bauschke–Combettes;
  - Butnariu–Iusem;
  - Censor–Zenios;
  - Borwein–Vanderwerff.
- Complete full-text verification of **Laude–Ochs–Cremers (2020)** and **Li–Song–Yao (2010)**.
- Any 2026 paper not yet indexed as of **August 13, 2026**.

No accessible source among those actually examined yielded a RED hit.

---

## VERDICT: AMBER

1. **Location:** Opening claim, “Our answer: yes.”  
   **Claim:** Full-domain necessity is newly settled.  
   **Why problematic:** The precise result appears new, but the broader phenomenon “nonconvex right entropy-Chebyshev set” was already published in 2009.  
   **Suggested fix:** State the novelty specifically as nonconvexity of \(C^*=\nabla f(C)\) while retaining the closure condition.

2. **Location:** Related-work discussion around Theorem SOL.8.  
   **Claim:** The construction stands independently of existing examples.  
   **Why problematic:** It uses exactly the duality architecture of Bauschke–Wang–Ye–Yuan Example 7.5.  
   **Suggested fix:** Cite Example 7.5 and include the convex-dual-set versus nonconvex-dual-set comparison.

3. **Location:** Prior-art treatment of Luo et al.  
   **Claim:** Luo et al. does not affect Part I.  
   **Why not fully cleared:** Theorem 3.12 apparently retains full domain, but all examples and remarks were not independently inspected here.  
   **Suggested fix:** Manually inspect the complete paper, searching for “nonconvex,” “Chebyshev but not sun,” “exponential,” “entropy,” “coercive,” and every example after Theorem 3.12.

4. **Location:** Discussion of the 2010 open problems.  
   **Claim:** Only the full-domain portion of Fact 3.2 is affected.  
   **Why incomplete:** By duality, the example also shows that supercoercivity cannot simply be deleted from Fact 3.1.  
   **Suggested fix:** Record this as a corollary, but make no priority claim until the no-coercivity literature is fully checked.

5. **Location:** Any reference to Problem 4.  
   **Claim:** The entropy problem is answered.  
   **Why wrong if stated:** The construction provides one further example, not a characterization.  
   **Suggested fix:** Say explicitly that Problem 4 remains open on the evidence located.

6. **Location:** Priority language throughout.  
   **Claim:** Absolute first publication.  
   **Why unsupported:** Several paywalled sources, monographs, and closed citation indexes remain unchecked.  
   **Suggested fix:** Use “we are unaware of an earlier example” and limit the claim to the compact global counterexample with nonconvex gradient image.