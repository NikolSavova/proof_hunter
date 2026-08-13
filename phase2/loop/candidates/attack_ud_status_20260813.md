# ud_status (gpt-5.6-sol, effort=max, 2026-08-13 09:58)

## Bottom line

As of **August 13, 2026**, the obvious downstream prizes are mostly gone:

- **Real sum-product:** gone.
- **Many sums and products:** gone.
- **Near-quadratic Elekes–Rónyai expansion:** gone.
- **Robust repeated-distance/subset consequences:** gone.
- **Naive numerical optimization of Sawin’s exponent:** crowded and largely gone.

The surprise is item 1: **there is not a large graveyard of theorems conditional on the unit-distance conjecture.** I found one important explicit conditional consequence—the pinned-distance conjecture—and the classical distinct-distance implication. Most incidence and additive-combinatorics arrows ran **toward** unit distances, not out of them.

**Status convention:** TAKEN means a public preprint or proof artifact exists, not necessarily journal publication or completed peer review.

## TAKEN / IN PROGRESS / UNCLAIMED

| Target | Status | Blunt assessment |
|---|---|---|
| Comprehensive audit of results conditional on \(u(n)=n^{1+o(1)}\) | **UNCLAIMED** | I found no published post-May dependency list. The list appears short, however—not a major mathematical bonanza. |
| Unit-distance conjecture \(\Rightarrow\) near-linear distinct distances | **TAKEN** | Classical pigeonhole implication; now unusable, but Guth–Katz already proves the conclusion unconditionally up to logarithms. ([cdn.openai.com](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-remarks.pdf)) |
| Unit-distance conjecture \(\Rightarrow\) pinned-distance conjecture | **TAKEN — May 2025** | Explicitly stated in *Generalised Erdős distance theory on graphs*. The conditional route is now dead; the pinned conjecture itself is not disproved. ([arxiv.org](https://arxiv.org/abs/2505.06590?utm_source=openai)) |
| Real Erdős–Szemerédi sum-product conjecture | **TAKEN — May 27, 2026** | Bloom–Sawin–Schildkraut–Zhelezov; this was the biggest obvious transplant and fell in seven days. ([arxiv.org](https://arxiv.org/abs/2605.28781)) |
| Many sums/products; analogous constructions over other fields; unit equations | **TAKEN — May 27, 2026** | All included in the same paper. Do not pitch these as follow-ups. ([arxiv.org](https://arxiv.org/abs/2605.28781)) |
| Near-quadratic Elekes–Rónyai expander conjecture over \(\mathbb R\) | **TAKEN — June 15, 2026** | Jihao Liu: fixed nonspecial quadratic polynomial, polynomial saving from quadratic expansion; explicitly relies on the OpenAI tower. ([arxiv.org](https://arxiv.org/abs/2606.16738)) |
| Robust repeated distances in every large subset | **TAKEN — July 6, 2026** | Lee–Pohoata–Zhu’s Minkowski grid. It also settles an Erdős 1980 conjecture and negatively answers a question of Conlon–Fox–Gasarch–Harris–Ulrich–Zbarsky. ([arxiv.org](https://arxiv.org/abs/2607.05374)) |
| Computational-geometry transplant | **TAKEN — June 24, 2026** | Saha–Xu–Ye use the techniques for SETH hardness of Furthest Pair in every superconstant efficiently constructible dimension. ([arxiv.org](https://arxiv.org/abs/2606.25887)) |
| Optimizing the unit-distance exponent | **IN PROGRESS — crowded** | Sawin’s \(1.014\) is obsolete as the numerical frontier. Multiple optimization codes, proof packages, and modified estimates appeared almost immediately. ([arxiv.org](https://arxiv.org/abs/2606.03419)) |
| Sharp ceiling for the number-field method | **IN PROGRESS** | Sawin proved a \(1.24295\ldots\) ceiling for his precise displayed framework, but not for all class-field-tower variants. No sharp paradigm-wide ceiling is known. ([arxiv.org](https://arxiv.org/abs/2605.20579)) |
| Interaction with Guth–Katz/ST/polynomial partitioning | **TAKEN as discussion; no new theorem** | The companion remarks discuss distinct distances and explain the obstacle. There is no collapse of Guth–Katz, Szemerédi–Trotter, or the polynomial method. ([cdn.openai.com](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-remarks.pdf)) |
| Unit distances in \(\mathbb R^3\) | **IN PROGRESS** | The companion paper explicitly examines the number-field approach and finds serious parameter obstacles. No corresponding conjecture has fallen. ([cdn.openai.com](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-remarks.pdf)) |
| Dimensions \(d\ge4\) | **TAKEN, pre-existing** | Quadratic Lenz-type constructions were already known, so there was no planar-style near-linear conjecture left to kill. ([arxiv.org](https://arxiv.org/abs/2202.05359)) |
| Arbitrary strictly convex or \(\ell_p\) norms | **UNCLAIMED beyond trivial cases** | Ellipsoidal norms inherit the Euclidean counterexample by linear transformation. No wholesale extension to non-Euclidean smooth norms was found. |
| Rigidity conjectures implying the Erdős bound | **UNCLAIMED cleanup** | A SoCG 2026 paper states that its Conjecture 7 implies the now-false Erdős bound. Unless another hypothesis intervenes, Conjecture 7 is therefore false by contrapositive. I found no erratum or follow-up. ([drops.dagstuhl.de](https://drops.dagstuhl.de/storage/00lipics/lipics-vol367-socg2026/html/LIPIcs.SoCG.2026.83/LIPIcs.SoCG.2026.83.html?utm_source=openai)) |
| Heilbronn / fixed-area triangle analogues | **UNCLAIMED** | These are the strongest surviving geometric targets with the same “only subpolynomial improvement is possible” smell. ([londmathsoc.onlinelibrary.wiley.com](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms.70447?utm_source=openai)) |

---

## 1. What was actually conditional on the unit-distance bound?

### A. Distinct distances: the classical implication

For an \(n\)-point set \(P\), let \(D(P)\) be its number of distinct nonzero distances. Every individual distance occurs at most \(u(n)\) times after rescaling, so

\[
D(P)\ge \frac{\binom n2}{u(n)}.
\]

Thus the conjectural \(u(n)=n^{1+o(1)}\) would have implied

\[
D(P)\ge n^{1-o(1)}.
\]

That route is dead. But the conclusion is not: Guth–Katz already gives \(\Omega(n/\log n)\), which is stronger than anything presently recoverable merely from an upper bound on \(u(n)\). The new construction does **not** produce a counterexample to distinct distances; one very frequent distance says almost nothing about the total number of other distances. ([cdn.openai.com](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-remarks.pdf))

### B. Pinned distances: the genuine conditional casualty

The 2025 preprint *Generalised Erdős distance theory on graphs* explicitly advertises a short proof that the unit-distance conjecture implies the pinned-distance conjecture. That proof route is now unusable. The pinned-distance conjecture itself remains a live problem: global multiplicity of one distance does not imply that every point sees few distances. ([arxiv.org](https://arxiv.org/abs/2505.06590?utm_source=openai))

This is the main item that genuinely needs a postscript or restatement.

### C. Incidence geometry and additive combinatorics

I found **no substantial family** of published theorems taking \(u(n)=n^{1+o(1)}\) as a hypothesis. Usually:

- incidence theory supplies upper bounds for unit distances;
- Szemerédi–Trotter supplies sum-product estimates;
- Guth–Katz supplies distinct-distance bounds.

The arrows mostly point the opposite way.

So: **no, nobody appears to have published the comprehensive list—but the list is probably short.** This lane is open, but lower-value than the prompt anticipates.

### D. A reverse implication that actually dies

The SoCG 2026 paper *Erdős’s Unit Distance Problem and Rigidity* states that its Conjecture 7 implies the Erdős unit-distance upper bound. The OpenAI construction therefore refutes that rigidity conjecture by contrapositive. This looks like an unclaimed but nearly automatic downstream correction. ([drops.dagstuhl.de](https://drops.dagstuhl.de/storage/00lipics/lipics-vol367-socg2026/html/LIPIcs.SoCG.2026.83/LIPIcs.SoCG.2026.83.html?utm_source=openai))

---

## 2. Did the technique transplant?

**Yes, spectacularly. The main transplant lane is already mined.**

1. **Real sum-product:** Bloom–Sawin–Schildkraut–Zhelezov use high-degree number fields and bounded root discriminant to construct real sets with both sumset and product set of size \(|A|^{2-c}\). They also kill the many-sums-and-products conjecture and derive variants in other fields and for unit equations. May 27. ([arxiv.org](https://arxiv.org/abs/2605.28781))

2. **Elekes–Rónyai expansion:** Liu gives a fixed nonspecial quadratic polynomial that fails near-quadratic expansion on algebraic-integer sets. June 15. ([arxiv.org](https://arxiv.org/abs/2606.16738))

3. **Robust repeated distances:** the Minkowski-grid paper builds point sets where every subset has a polynomially frequent distance. This is substantially stronger structurally than merely constructing one dense unit-distance graph. July 6. ([arxiv.org](https://arxiv.org/abs/2607.05374))

4. **Fine-grained computational geometry:** Furthest Pair hardness uses the same style of arithmetic/high-dimensional construction. June 24. ([arxiv.org](https://arxiv.org/abs/2606.25887))

The first two are exactly the kind of “algebraic constructions cannot be polynomially denser” conjectures you identified. **They are gone.**

The surviving transplant targets are determinant/volume problems, pinned variants, higher-arity polynomial expansion, dimension three, and exceptional smooth norms.

---

## 3. The exponent: current state

There are now three different answers, depending on the evidentiary standard and quantifier.

### Clean original theorem

Sawin proves

\[
u(n)>n^{1.014}
\]

for arbitrarily large \(n\), with the displayed certificate actually giving

\[
\delta=0.014114428\ldots.
\]

([arxiv.org](https://arxiv.org/abs/2605.20579))

### Reproducible pointwise package

Tseng posted a proof-and-verification package claiming that **for every sufficiently large \(n\)**,

\[
u(n)\gg n^{1.03158935}.
\]

That has a stronger quantifier than Sawin’s original infinitely-many-\(n\) formulation, but it is a GitHub/Zenodo/MathOverflow proof package rather than a standard refereed paper. ([mathoverflow.net](https://mathoverflow.net/questions/511514/what-is-the-unit-distance-exponent))

### Strongest publicly inspectable asymptotic claim

Eric Naslund’s MathOverflow argument claims

\[
\delta>0.03583,
\qquad
u(n)>n^{1.03583}
\]

along a suitable infinite family. It uses more than parameter search: improved relative-class-number estimates, narrow class groups, a better overlap geometry, a covolume bound, and a refined Golod–Shafarevich calculation. The answer was posted May 23 and substantially edited through June 9. Sawin described the central ideas as essentially right but under-explained. ([mathoverflow.net](https://mathoverflow.net/questions/511514/what-is-the-unit-distance-exponent))

Emmerich’s latest arXiv abstract reports community certificates beyond \(0.035\), and reports of values beyond \(0.036\), but I did not find a stable full proof artifact establishing the latter. ([arxiv.org](https://arxiv.org/abs/2606.03419))

**My citation recommendation:**

- **Best clean paper:** \(1.014\), Sawin.
- **Best packaged all-\(n\) claim:** \(1.03158935\), Tseng.
- **Best public asymptotic argument:** approximately \(1.03583\), Naslund.
- **Do not yet cite \(1.036+\) as settled.**

### Is there a ceiling?

For Sawin’s precise Lemma 5 + Lemma 7/formula (12) architecture, he proves an exponent ceiling of

\[
1+\frac1{4.116}=1.24295\ldots.
\]

That ceiling is below the global Spencer–Szemerédi–Trotter exponent \(4/3\), but Naslund’s alterations change parts of the architecture, so \(1.24295\) is **not** a no-go theorem for the broader number-field paradigm. The sharp ceiling is open; relative class-number lower bounds and possible exceptional zeros are central obstructions. ([arxiv.org](https://arxiv.org/abs/2605.20579))

**Raw parameter optimization is taken.** The remaining valuable exponent problem is analytic: identify the true asymptotic tradeoff among root discriminant, split primes, relative class numbers, and the geometry-of-numbers window.

---

## 4. Distinct distances, Szemerédi–Trotter and the polynomial method

There is no destructive interaction.

- **Guth–Katz survives untouched.**
- **Szemerédi–Trotter survives untouched.**
- **Polynomial partitioning survives untouched.**
- The \(O(n^{4/3})\) unit-distance upper bound remains the best general upper bound, while the new lower exponent is only around \(1.036\).

The disproof establishes that no argument—polynomial or otherwise—can prove the formerly conjectured near-linear upper bound. It does not reveal a flaw in existing incidence machinery.

The companion remarks already examine whether the number-field construction can reduce the number of distinct distances and identify an unfavorable prime-splitting tradeoff. ([cdn.openai.com](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-remarks.pdf))

The one real follow-up is the Minkowski-grid paper: it shows robust high multiplicity in every subset, with consequences for isosceles triangles and repeated-distance-free subsets. But that is not an improvement or counterexample to Guth–Katz. ([arxiv.org](https://arxiv.org/abs/2607.05374))

---

## 5. Higher dimensions and other norms

### \(\mathbb R^3\)

**Not fallen.** The expected scale is near \(n^{4/3}\), and three-dimensional lattice constructions already operate near that scale. The companion remarks consider replacing the CM norm form by positive-definite ternary quadratic forms over totally real fields, but the splitting gain is too expensive under the presently available Golod–Shafarevich parameters. ([cdn.openai.com](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-remarks.pdf))

Embedding the planar construction in a plane inside \(\mathbb R^3\) gives nothing competitive with existing three-dimensional lower constructions.

### \(d\ge4\)

There is no analogous near-linear conjecture to disprove: Lenz-type constructions already give quadratically many unit distances. ([arxiv.org](https://arxiv.org/abs/2202.05359))

### Other norms

- **Ellipsoidal/inner-product norms:** already fall trivially. If \(\|x\|_Q=|Lx|_2\), apply \(L^{-1}\) to the Euclidean counterexample.
- **Norms with flat pieces:** quadratic constructions were already known.
- **General strictly convex norms:** no uniform conjecture falls. Some exceptional strictly convex norms attain the \(n^{4/3}\) scale, while generic norms have substantially sparser unit-distance graphs. ([cdn.openai.com](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-proof.pdf))
- **Specific \(\ell_p\), smooth algebraic, or analytic norms:** I found no public Golod–Shafarevich transplant.

The right unclaimed formulation is probably not “all norms,” but: **which algebraic unit curves admit high-degree number-field parametrizations producing polynomially dense unit graphs?**

---

## 6. Other downstream consequences

### The rigidity casualty

The Conjecture 7 issue in the SoCG rigidity paper is the cleanest overlooked formal corollary. It is probably worth an erratum, not a standalone major paper. ([drops.dagstuhl.de](https://drops.dagstuhl.de/storage/00lipics/lipics-vol367-socg2026/html/LIPIcs.SoCG.2026.83/LIPIcs.SoCG.2026.83.html?utm_source=openai))

### Second-order fallout from sum-product

The unit-distance conjecture itself has few conditional dependents. The **real sum-product conjecture probably has more**. A serious downstream audit should now pivot to theorems stated conditionally on the real exponent \(2-o(1)\), carefully separating:

- real/algebraic-number formulations, now false;
- integer formulations, which the real counterexample does not settle;
- applications using only proven weaker sum-product bounds, which remain valid.

### Source correction

I could not verify the stated official Anthropic follow-up. The public autonomous re-disproof I found is Yichen Huang’s July 9 paper using **GPT-5.5 Pro**, not an Anthropic system. It reports seven successful autonomous sum-product disproofs in eight runs, including constructions not using units. I would not cite the Anthropic attribution without a primary artifact. ([arxiv.org](https://arxiv.org/abs/2607.20525))

---

# Ranking of apparently unclaimed items

The timing estimates are my judgment from how rapidly May’s obvious follow-ups were taken.

| Rank | Unclaimed target | Value | Likely capture speed | Assessment |
|---:|---|---:|---|---|
| 1 | **Heilbronn’s near-\(N^{-2}\) triangle problem via number-field towers** | 10/10 | **1–3 months** | Closest surviving analogue: the known construction beats \(N^{-2}\) only logarithmically, while the surviving conjecture forbids a fixed polynomial improvement. Product-formula lower bounds on determinants make the representation shift plausible. ([londmathsoc.onlinelibrary.wiley.com](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms.70447?utm_source=openai)) |
| 2 | **Superquadratically many equal-area triangles / equal-volume simplices** | 9.5/10 | **Weeks** | Replace the norm equation by a determinant equation. The published planar benchmark has a substantial gap between quadratic constructions and superquadratic upper bounds. ([arxiv.org](https://arxiv.org/abs/1501.00379?utm_source=openai)) |
| 3 | **Higher-arity Elekes–Szabó-type expansion failures** | 9/10 | **Days to weeks** | Liu has already killed the binary Elekes–Rónyai target. The obvious next step is fixed non-group-like maps in more variables. Assume people are already privately running this. |
| 4 | **Pinned-distance behavior of the Minkowski grids** | 8.5/10 | **Days to weeks** | The old conditional proof is dead, and robust global repetition does not answer the pinned question. Determine whether the new grids are counterexamples, near-counterexamples, or actually have many pinned distances. |
| 5 | **Exceptional smooth norms beyond ellipsoids** | 8/10 | **1–4 months** | Seek algebraic unit circles carrying norm-one groups or low-height parametrizations. A result for a natural \(\ell_p\) norm would be much more valuable than an artificially designed norm. |
| 6 | **Explicit coordinates and height/complexity bounds** | 7.5/10 | **2–6 months** | Convert tower existence and asymptotic counting into actual finite coordinate sets, with degree, height and construction-time bounds. Numerically useless at present, mathematically clean. |
| 7 | **Falconer/uniform-distribution compatibility** | 7/10 | **Months** | Test whether these point sets can satisfy the regularity assumptions used in discrete-to-continuous distance theory. The present construction is likely too arithmetically concentrated, but proving the obstruction would clarify the boundary. ([arxiv.org](https://arxiv.org/abs/2202.05359)) |
| 8 | **Formal refutation/update of SoCG Rigidity Conjecture 7** | 4/10 | **Hours to days** | Almost free, but correspondingly low-value. It is an erratum-sized observation. |
| 9 | **Full unit-distance conditional-dependency audit** | 5/10 | **One to two weeks** | Unclaimed, but probably short. Expect pinned distances plus historical distinct-distance implications, not a large incidence/additive-combinatorics collapse. |

## Do not spend time claiming these

- “Apply number fields to real sum-product.”
- “Disprove many sums and products.”
- “Apply the tower to Elekes–Rónyai.”
- “Strengthen to robust repeated distances in subsets.”
- “Run a basic optimizer on Sawin’s original prime parameters.”
- “Show that Guth–Katz or Szemerédi–Trotter is affected.”
- “Extend the result to ellipsoidal norms.”

Those are gone or trivial. The genuine high-value race is now **determinant/volume equations, Heilbronn, higher-arity expansion, pinned distances, and the analytic ceiling of the tower method**.