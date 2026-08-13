# Prior-art sweep — union_closed (gpt-5.6-sol, effort=max, 2026-08-13 08:39)

> Counterexample-shaped target, selected after the Jacobian conjecture
> counterexample (Alpoge/Fable 5, 2026-07-20). Sweep asks BOTH whether the
> problem is already resolved AND where counterexample search is already dead.

# Executive finding

## 1. STATUS as of August 13, 2026: **OPEN**

I searched arXiv by the exact phrases **“union-closed”**, **“union-closed sets conjecture”**, and **“Frankl’s conjecture”**, sorted by newest announcement and submission dates, and separately searched titles claiming a proof. The newest directly relevant work I found includes Bouchard’s July 28, 2026 supersaturation paper, DeFranco’s June 24, 2026 Boolean-polynomial reformulation, and Ho’s January 27, 2026 entropy-inequality paper; all treat Frankl’s conjecture as unresolved or work on partial/reformulated questions. ([arxiv.org](https://arxiv.org/search/?abstracts=show&order=-announced_date_first&query=%22union-closed%22&searchtype=all&size=100))

There are recent **claimed proofs**, but none is accepted as resolving the problem:

- Roberto Demontis, *The union-closed set conjecture is true*, arXiv:2405.03731, 2024, also appeared in *Current Research in Statistics & Mathematics*. I found no independent validation; primary research from 2025–2026 continues to call the statement a conjecture and studies necessary conditions for counterexamples. ([arxiv.org](https://arxiv.org/search/?abstracts=show&order=-submitted_date&query=%22union-closed+set+conjecture+is+true%22&searchtype=title&size=100))
- Theophilus Agama’s 2017 claimed proof was reformatted and resubmitted in March 2026 with its ideas unchanged, but has not been recognized as a resolution. ([arxiv.org](https://arxiv.org/search/?abstracts=show&order=-submitted_date&query=%22proof+of+the+union-closed%22&searchtype=title&size=100))
- Raffaele Scandone’s 2023 claimed proof explicitly carries the arXiv comment that Proposition 1.2 contains a mistake. ([arxiv.org](https://arxiv.org/search/?abstracts=show&order=-submitted_date&query=%22proof+of+the+union-closed%22&searchtype=title&size=100))
- Blinovsky–Speranca’s older claimed proof was revised again in 2024, but the first version has a documented gap and the revision has not produced expert consensus or changed later literature’s status. ([arxiv.org](https://arxiv.org/search/?abstracts=show&order=-announced_date_first&query=%22union-closed+sets+conjecture%22&searchtype=all&size=100))

**Axis checked:** the exact finite, uniformly counted union-closed conjecture.  
**Axes not claimed checked by this status determination:** weighted/non-uniform variants, infinite variants, or approximate union closure; some of those have different answers.

---

# 2. THE CONSTANT AND THE ENTROPY BARRIER

Put
\[
c_{\rm UC}
=\inf_{\mathcal F\ne\{\varnothing\}}
\max_{x\in\bigcup\mathcal F}
\frac{|\{A\in\mathcal F:x\in A\}|}{|\mathcal F|}.
\]
Frankl’s conjecture says \(c_{\rm UC}=1/2\).

## Current record: there is an important certification distinction

| Result | Constant | Audit |
|---|---:|---|
| Gilmer, 2022 | \(0.01\) | Fully explicit first dimension-free constant. |
| Alweiss–Huang–Sellke; Chase–Lovett; Pebody; Sawin, 2022 | \(\psi=(3-\sqrt5)/2=0.381966011\ldots\) | Explicit and accepted. |
| Yu, 2023 | \(0.38234\) | Explicit theorem in a peer-reviewed paper. |
| Cambie, updated 2025 | \(0.382345533366\ldots\) | Sharper optimization of Sawin’s mixed-coupling scheme; latest version reduces the numerical verification to two parameters. |
| Liu, 2023/2024 | strictly greater than \(0.382345533\ldots\) | Unconditional qualitative strict improvement via conditionally-i.i.d. coupling. |
| Liu numerical value | \(0.382709087918741\ldots\) | **Conditional in the paper** on a positive-semidefiniteness hypothesis and on the proposed global-minimizer structure of a nine-dimensional optimization. |

Gilmer’s breakthrough and the rapid \(\psi\)-improvements are documented in the original papers. ([arxiv.org](https://arxiv.org/search/?abstracts=show&order=-announced_date_first&query=%22union-closed+sets+conjecture%22&searchtype=all&size=100)) Yu obtained \(0.38234\), while Cambie computed the relevant Sawin-coupling optimum as approximately \(0.382345533366\). ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC10217025/))

Liu’s paper rigorously shows that conditionally-i.i.d. coupling gives some strict improvement over the Sawin/Cambie value. However, its displayed \(0.382709087918741\) theorem is expressly conditional: the paper numerically checks positive semidefiniteness on a grid and conjectures that the best local optimizer found from \(10^5\) random starts is global. ([arxiv.org](https://arxiv.org/pdf/2306.08824))

**Therefore:**

- **Commonly quoted current numerical record:** \(0.38271\).
- **Best explicit peer-reviewed number I would use without qualification in a certified search:** \(0.38234\).
- **If accepting Cambie’s documented computer optimization:** \(0.382345533366\ldots\).
- **Liu proves an unconditional but non-numerically-explicit strict improvement beyond that.**

For the first live search point \(m=51\), all these versions give the same integer constraint: some element must occur in at least
\[
\lceil0.38234\cdot51\rceil=20
\]
sets.

## Is \(0.381966\) a barrier?

**Yes, but only on a narrow axis. No, it is not a ceiling for entropy methods in general.**

1. For Gilmer’s original two **independent, identically distributed** samples and the associated one-coordinate entropy inequality, \(\psi=(3-\sqrt5)/2\) is the optimal constant.
2. Chase–Lovett construct approximately union-closed systems where every coordinate has frequency only \(\psi+o(1)\). Thus \(\psi\) is genuinely optimal for their approximate relaxation. ([arxiv.org](https://arxiv.org/pdf/2211.11689))
3. Sawin’s dependent coupling, then Yu/Cambie and Liu, already exceed \(\psi\). Thus any statement that “\(0.38\) is the ceiling of the entropy method” is false unless “entropy method” is restricted to the original i.i.d. scheme.
4. Cambie’s \(0.382345533\ldots\) is itself an optimum for a particular convex combination of coupling protocols, not for every possible entropy argument. Liu’s different protocol exceeds it. ([arxiv.org](https://arxiv.org/pdf/2212.12500))

This barrier is **not evidence that \(1/2\) is false**. It says that approximate closure or a restricted entropy protocol loses information that exact union closure may encode. Cambie explicitly concludes that essential new ideas are probably needed for the exact conjecture. ([arxiv.org](https://arxiv.org/pdf/2306.12351))

**Axis checked:** i.i.d. entropy, specified dependent couplings, and approximate union closure.  
**Axis not checked:** all possible entropy inequalities or the exact \(1/2\) statement.

---

# 3. WHERE COUNTEREXAMPLE SEARCH IS ALREADY DEAD

Let
\[
n=\left|\bigcup\mathcal F\right|,\qquad m=|\mathcal F|.
\]

## A. Exact global ranges

### Ground-set size

**No counterexample exists for \(n\le 12\).**

Bojan Vučković and Miodrag Živković gave a computer-assisted proof for every union-closed family on at most twelve ground elements. This superseded the earlier \(n\le11\) result of Bošnjak–Marković. ([ipsitransactions.org](https://ipsitransactions.org/journals/papers/tir/2017jan/p9.pdf))

> B. Vučković and M. Živković, “The 12-Element Case of Frankl’s Conjecture,” *IPSI BgD Transactions on Internet Research* 13(1), 2017, pp. 9–15. DOI: none located.  
> URL: https://ipsitransactions.org/journals/papers/tir/2017jan/p9.pdf

I found **no credible \(n=13\) verification**, exhaustive enumeration, SAT certificate, or 2024–2026 preprint extending \(12\) to \(13\).

### Family size

**No counterexample exists for \(m\le50\).**

This is not a second independent enumeration. Lo Faro proved that a minimum counterexample must satisfy
\[
m\ge 4n-1.
\]
Since the \(n\le12\) case is known, a counterexample has \(n\ge13\), hence \(m\ge51\). ([cambridge.org](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7CC969B92322D8B79888D2C2AA50B057/S1446788700037526a.pdf/note_on_the_unionclosed_sets_conjecture.pdf))

> Giovanni Lo Faro, “A Note on the Union-Closed Sets Conjecture,” *Journal of the Australian Mathematical Society, Series A* 57 (1994), 230–236.  
> DOI: https://doi.org/10.1017/S1446788700037526

Thus the first numerical corner not ruled out is:

\[
\boxed{n=13,\quad m=51.}
\]

I found **no credible exhaustive verification for \(m=51\)** or higher.

### Dense families

Published density results eliminate the dense end of the Boolean cube. Balla–Bollobás–Eccles first handled families containing at least two-thirds of all \(2^n\) subsets; Karpas subsequently proved the conjecture at density at least \(1/2\). A stronger \((1/2-\varepsilon)2^n\) statement is often cited as an unpublished preprint, but I did not locate a stable public manuscript with a usable value of \(\varepsilon\), so I would not use that stronger version as a certified search cutoff.

> I. Balla, B. Bollobás and T. Eccles, “Union-Closed Families of Sets,” *Journal of Combinatorial Theory, Series A* 120 (2013), 531–544.  
> DOI: https://doi.org/10.1016/j.jcta.2012.10.003  
> I. Karpas, “Two Results on Union-Closed Families,” 2017; publication metadata/DOI not recovered in this search.

At the very least, a counterexample satisfies \(m<2^n\), already following from Reimer’s average-set-size theorem together with the fact that every counterexample has average set size below \(n/2\).

## B. Local configurations and structural classes

### Sets of size one or two

If \(\mathcal F\) contains a singleton, that singleton’s element is abundant. If it contains a two-element set, at least one of those two elements is abundant. Therefore every nonempty member of a counterexample has size at least three. ([arxiv.org](https://arxiv.org/pdf/1309.3297))

> D. G. Sarvate and J.-C. Renaud, “On the Union-Closed Sets Conjecture,” *Ars Combinatoria* 27 (1989), 149–154. DOI: none located.

### Separating families and small \(m/n\)

Two ground elements having identical incidence columns can be identified without changing the family size or the frequency ratios. Thus a minimum-ground-set counterexample can be assumed **separating**: for each pair \(x\ne y\), some member contains exactly one of them.

Falgas-Ravry proved the conjecture for separating families with \(m\le2n\). Maßberg strengthened the safe range to
\[
m\le
2\left(n+\frac{n}{\log_2n-\log_2\log_2n}\right).
\]
Hence a separating counterexample lies above this curve. ([arxiv.org](https://arxiv.org/search/?abstracts=show&order=-announced_date_first&query=%22union-closed+sets+conjecture%22&searchtype=all&size=100))

> Jens Maßberg, “The Union-Closed Sets Conjecture for Small Families,” 2015, arXiv:1508.05718.  
> DOI: https://doi.org/10.48550/arXiv.1508.05718  
> URL: https://arxiv.org/abs/1508.05718

For a globally minimum counterexample, Lo Faro’s stronger \(m\ge4n-1\) constraint is the relevant one.

### Chain height

Using the convention in Tian’s paper, the conjecture holds when the family’s height is at most \(3\), and also when its height is at least \(n-1\). Colbert later extended the short-chain argument to appropriate infinite/generalized families. Therefore a finite counterexample must occupy the intermediate-height regime. ([arxiv.org](https://arxiv.org/search/?abstracts=show&order=-announced_date_first&query=%22union-closed%22&searchtype=all&size=100))

> Chenxiao Tian, “Union-Closed Sets Conjecture Holds for Height \(H(\mathcal F)\le3\) and \(H(\mathcal F)\ge n-1\),” publication metadata/DOI not recovered.  
> Cory H. Colbert, “Chain Conditions and Optimal Elements in Generalized Union-Closed Families of Sets,” arXiv:2412.18740, 2024/2025.  
> URL: https://arxiv.org/abs/2412.18740

### Lattice classes

In the lattice formulation, Frankl asks for a join-irreducible \(j\) whose principal filter has size at most half the lattice. The result is known for lower semimodular lattices and even lower quasi-semimodular lattices; this eliminates broad structured lattice classes. ([arxiv.org](https://arxiv.org/pdf/1309.3297))

> J. Reinhold, “Frankl’s Conjecture Is True for Lower Semimodular Lattices,” *Graphs and Combinatorics* 16 (2000), 115–116.  
> T. Abe, “Strong Semimodular Lattices and Frankl’s Conjecture,” *Algebra Universalis* 44 (2000), 379–382.

Bouchard’s 2025 paper, published in 2026, adds necessary deletion/interval conditions for a lattice counterexample of minimum size. These conditions are genuine prior art, but they do not currently yield a simple stronger numerical cutoff than \(n\ge13,m\ge51\). ([arxiv.org](https://arxiv.org/pdf/2503.00277))

> Christopher Bouchard, “On the Lattice Formulation of the Union-Closed Sets Conjecture,” *Le Matematiche* 81(1), 2026, 153–165; arXiv:2503.00277.  
> URL: https://arxiv.org/abs/2503.00277

### Graph classes

Frankl is equivalent to the following graph statement: every nontrivial graph has adjacent vertices each lying in at most half its maximal independent sets. A counterexample can be reduced to the bipartite case. The conjecture is proved for chordal bipartite graphs, subcubic bipartite graphs, bipartite series-parallel graphs, and bipartitioned circular-interval graphs. ([arxiv.org](https://arxiv.org/search/?abstracts=show&order=-announced_date_first&query=%22union-closed+sets+conjecture%22&searchtype=all&size=100))

> H. Bruhn, P. Charbit, O. Schaudt and J. A. Telle, “The Graph Formulation of the Union-Closed Sets Conjecture,” *European Journal of Combinatorics* 43 (2015), 210–219; arXiv:1212.4175.  
> DOI: https://doi.org/10.48550/arXiv.1212.4175  
> URL: https://arxiv.org/abs/1212.4175

## C. FC-family and automated local pruning

A seed family \(\mathcal A\) is **Frankl-complete (FC)** if every union-closed extension of \(\mathcal A\) satisfies Frankl. Poonen’s theorem characterizes FC seeds by a finite linear weighting condition: there must be nonnegative weights \(c_i\), summing to one, such that every relevant union-closed extension on the seed universe satisfies a weighted half-frequency inequality. ([arxiv.org](https://arxiv.org/pdf/1309.3297))

> Bjorn Poonen, “Union-Closed Families,” *Journal of Combinatorial Theory, Series A* 59 (1992), 253–268.  
> DOI: https://doi.org/10.1016/0097-3165(92)90068-6

This is the basis of cutting-plane and integer-programming searches. In particular:

- Marić, Živković and Vučković produced a fully automatic, formally verified classification of FC families on a six-element universe.
- Pulaj’s *Characterizing 3-Sets in Union-Closed Families*, arXiv:1903.02317, classifies three-set seed configurations on universes \(n\le9\) using exact rational integer programming. ([researchgate.net](https://www.researchgate.net/publication/331343208_Fully_Automatic_Verified_Classification_of_all_Frankl-Complete_FC6_Set_Families))
- Pulaj–Wood obtained new values and bounds for \(FC(k,n)\), and generalized Poonen’s criterion to additional local configurations. ([arxiv.org](https://arxiv.org/abs/2301.01331))

> Jonad Pulaj and Kenan Wood, “Local Configurations in Union-Closed Families,” *Experimental Mathematics*, accepted 2024; arXiv:2301.01331.  
> DOI: https://doi.org/10.1080/10586458.2024.2410964  
> URL: https://arxiv.org/abs/2301.01331

These are **local pruning results**, not a global verification beyond \(n=12\). A counterexample must avoid every known FC seed.

## D. Concrete specification of the first possible counterexample

For the first live slice \(n=13,m=51\), a counterexample must satisfy at least:

1. It is separating/twin-free.
2. Its union, the full thirteen-element ground set, is a member.
3. Its common intersection is empty.
4. It contains no nonempty set of size \(1\) or \(2\).
5. Every element degree is at most \(25\).
6. At least one element degree is at least \(20\).
7. Its total incidence is at most \(13\cdot25=325\), so its average set size is at most \(325/51\approx6.373<6.5\).
8. It avoids all known FC local configurations.
9. It is outside the proven chain, lattice and graph classes above.
10. One may add \(\varnothing\) to any counterexample and retain a counterexample, but this raises \(m\) by one; therefore forcing \(\varnothing\) while searching a fixed \(m=51\) slice could miss a 51-set witness whose normalized version has 52 sets.

That is the minimum credible starting point. Searching \(n\le12\) or \(m\le50\) is dead on arrival.

---

# 4. WHY IS IT BELIEVED?

The evidence is **mixed**, not purely computational.

## (a) Genuine structural evidence

- Reimer’s theorem forces average set size at least \(\tfrac12\log_2m\), showing that union closure creates substantial aggregate incidence.
- Gilmer’s entropy argument and its successors prove the dimension-free lower bound \(>0.3823\). This is a real universal structural phenomenon, not a finite enumeration.
- Poonen’s theorem explains many local configurations through duality and linear weights.
- The conjecture survives broad lattice, graph, chain, dense-family and local-generator classes. ([arxiv.org](https://arxiv.org/abs/2306.08824))

The Boolean algebra \(2^{[n]}\) has every element in exactly half its sets, so \(1/2\) is the natural sharp endpoint rather than an arbitrary guessed constant.

## (b) Search evidence

- No counterexample for \(n\le12\).
- No counterexample for \(m\le50\).
- Extensive FC-family, integer-programming and exact local-configuration searches have found none.
- The problem has generated many plausible but erroneous short proofs, indicating that superficial averaging arguments systematically overestimate what union closure supplies.

## Assessment

The **weakened \(0.382+\) statement is supported by type (a)**. The final jump from \(0.382+\) to \(1/2\), however, is supported by a combination of special-case structure, equality examples and extensive failure to find a counterexample. There is no known stability theorem saying that every exact union-closed family must resemble an equality object closely enough to force \(1/2\).

So this is not merely type (b) dressed up as structure—but the exact \(1/2\) endpoint remains much less structurally compelled than the post-Gilmer constant bound.

---

# 5. REFORMULATIONS AND REPRESENTATION SHIFTS

## Equivalent formulations

| Formulation | Statement/object | Search value |
|---|---|---|
| Intersection-closed dual | Complement every set; seek an element occurring in at most half the members. | Same raw complexity; sometimes more natural for Horn closure. |
| Boolean OR-closed relation | Encode sets as \(0/1\)-vectors closed under coordinatewise OR. | Best direct bit-vector representation. |
| Horn/dual-Horn Boolean functions | Intersection-closed families are Horn model sets; union-closed families are dual-Horn model sets. | Compact for some structured instances, but worst-case formulas remain exponential/nonunique. |
| Finite lattice | Seek a finite lattice where every join-irreducible has a principal filter larger than half. | Removes irrelevant duplicate incidence columns and exposes structure; lattice enumeration at 51 elements is still enormous. |
| Bipartite/maximal-independent-set graph | Seek a bipartite graph violating the rare-vertex maximal-stable-set statement. | Useful structurally, poor for direct search because maximal-independent-set enumeration is itself exponential. |
| FC/Poonen weights | Test whether a partial seed forces Frankl through a linear feasibility problem. | Excellent as a pruning oracle. |
| Entropy/distributions | Uniform random member \(X\), compare \(H(X)\) and \(H(X\lor Y)\). | Best for global proofs, not witness generation. |
| Boolean polynomial | For fixed \(m,n\), DeFranco constructs a Boolean polynomial that vanishes identically iff the conjecture holds for that pair. | Exact algebraic reformulation, but no demonstrated computational compression yet. |

The lattice and graph equivalences are established in the cited papers. ([arxiv.org](https://arxiv.org/search/?abstracts=show&order=-announced_date_first&query=%22union-closed%22&searchtype=all&size=100)) Union-closed families have also been explicitly connected to Horn Boolean functions. ([wrap.warwick.ac.uk](https://wrap.warwick.ac.uk/id/eprint/180696/))

DeFranco’s 2026 construction gives a polynomial
\[
\mathrm{ICC}_{m,n}(X)
\]
over Boolean variables whose being the zero Boolean polynomial is equivalent to the fixed-\((m,n)\) conjecture. This is mathematically exact, but expanding or identity-testing the polynomial appears essentially to repackage the same combinatorial explosion. ([arxiv.org](https://arxiv.org/pdf/2606.26191))

> Mario DeFranco, “On Boolean Polynomials and the Union-Closed Conjecture,” 2026, arXiv:2606.26191.  
> DOI: https://doi.org/10.48550/arXiv.2606.26191  
> URL: https://arxiv.org/abs/2606.26191

## Best representation for an actual counterexample search

For a fixed first slice such as \((n,m)=(13,51)\), I would use a **row-incidence SAT/CP-SAT model**, not the lattice, graph or expanded-polynomial representation.

Use membership bits
\[
r_{a,i}\in\{0,1\},\qquad
1\le a\le51,\;1\le i\le13,
\]
with:

- lexicographically sorted distinct rows;
- lexicographically sorted distinct columns, enforcing separation;
- one all-ones row;
- for every row pair \(a,b\), a witness row \(c\) satisfying
  \[
  r_{c,i}=r_{a,i}\lor r_{b,i}\quad\forall i;
  \]
- degree constraints
  \[
  \sum_a r_{a,i}\le25;
  \]
- exclusion of rows of Hamming weight \(1\) or \(2\);
- learned Poonen/FC cuts when a partial configuration becomes Frankl-complete;
- canonical augmentation or graph-isomorphism symmetry breaking.

This needs only \(51\cdot13=663\) primary membership bits, although union witnesses and symmetry breaking add substantially more.

The alternative subset-variable formulation has one bit \(x_S\) for each \(S\subseteq[13]\), hence 8192 primary variables, with closure clauses
\[
\neg x_A\lor\neg x_B\lor x_{A\cup B}.
\]
There are about
\[
\frac{4^{13}-2\cdot3^{13}+2^{13}}2
=31{,}964{,}205
\]
nontrivial unordered closure clauses before reductions. It is canonical and suitable for lazy clause generation, but proving UNSAT is likely difficult.

---

# 6. NEAR MISSES AND FALSE ANALOGUES

## The exact constant is tight

The full power set has every element in exactly half its members. Thus even if true, Frankl cannot be strengthened beyond \(1/2\) without additional hypotheses.

## Approximate union closure stops at \(0.381966\)

Chase–Lovett’s two-layer construction is approximately union-closed while every element appears in only \(\psi+o(1)\) of the sets. This is probably the most relevant false analogue: a search based on “almost union-closed, low-frequency” candidates may converge toward these objects, but taking exact union closure can add many sets and destroy the low frequencies. ([arxiv.org](https://arxiv.org/pdf/2211.11689))

## The obvious three-set extension is false

A singleton forces its element to be abundant and a two-set forces one of its elements to be abundant. The analogous assertion for a particular three-set is false: there are union-closed families containing a three-set none of whose three elements is abundant, even though some element outside it satisfies Frankl. Thus “find a small set and average over it” is exhausted at size two.

## Small members can be extremely misleading

Ellis–Ivan–Leader construct union-closed families whose smallest member has size \(k\), but no element of that member occurs in more than
\[
(1+o(1))\frac{\log_2k}{2k}
\]
of the family. Their examples show that a small member need not contain anything remotely close to an abundant element. ([arxiv.org](https://arxiv.org/abs/2201.11484))

> David Ellis, Maria-Romina Ivan and Imre Leader, “Small Sets in Union-Closed Families,” 2022, arXiv:2201.11484.  
> DOI: https://doi.org/10.48550/arXiv.2201.11484  
> URL: https://arxiv.org/abs/2201.11484

## Reimer’s structural condition alone is insufficient

Raz constructed families satisfying the intermediate conditions used in Reimer’s average-size proof but violating the abundance conclusion. Lu–Raz later gave infinite families of such examples with arbitrarily large minimum member size and analyzed how far they are from being union-closed. Therefore Reimer’s average-size mechanism cannot by itself prove Frankl. ([arxiv.org](https://arxiv.org/abs/1704.07022))

> Abigail Raz, “Note on the Union-Closed Sets Conjecture,” 2017, arXiv:1704.07022.  
> URL: https://arxiv.org/abs/1704.07022  
> Kengbo Lu and Abigail Raz, “Note on the Union-Closed Sets Conjecture and Reimer’s Average Set Size Theorem,” 2024, arXiv:2405.10639.  
> URL: https://arxiv.org/abs/2405.10639

## Stronger entropy and LP simplifications have failed

Sawin disproved a strengthening conjectured by Gilmer that would have implied the full conjecture. Pulaj disproved Morris’s suggestion that only a narrow subcollection of Poonen inequalities need be checked. These failures say that both the entropy and FC-weight spaces have genuine higher-order obstructions. ([arxiv.org](https://arxiv.org/search/?abstracts=show&order=-announced_date_first&query=%22union-closed+sets+conjecture%22&searchtype=all&size=100))

## Infinite analogue

The unrestricted infinite version is false; short-chain or descending-chain hypotheses can recover positive statements. This is a category change, not direct evidence for a finite counterexample. ([arxiv.org](https://arxiv.org/search/?abstracts=show&order=-announced_date_first&query=%22union-closed%22&searchtype=all&size=100))

---

# 7. WHO IS ACTIVELY WORKING ON IT? AUTOMATION AND AI

Recent publicly visible activity includes:

- **Christopher Bouchard:** lattice conditions, averaging results, upper bounds and July 2026 supersaturation. ([arxiv.org](https://arxiv.org/search/?abstracts=show&order=-announced_date_first&query=%22union-closed%22&searchtype=all&size=100))
- **Mario DeFranco:** Boolean-polynomial formulation, June 2026. ([arxiv.org](https://arxiv.org/search/?abstracts=show&order=-announced_date_first&query=%22union-closed%22&searchtype=all&size=100))
- **Boon Suan Ho:** generalized Boppana entropy inequality, with a Lean 4 formalization, January 2026. ([arxiv.org](https://arxiv.org/search/?abstracts=show&order=-announced_date_first&query=%22union-closed+sets+conjecture%22&searchtype=all&size=100))
- **Shagnik Das and Saintan Wu:** frequencies of the second, third and subsequent most-popular elements, with LP computations and public code. ([arxiv.org](https://arxiv.org/search/?abstracts=show&order=-announced_date_first&query=%22union-closed%22&searchtype=all&size=100))
- **Jonad Pulaj and Kenan Wood:** FC thresholds and local configurations. ([arxiv.org](https://arxiv.org/abs/2301.01331))
- **Jingbo Liu, Lei Yu and Stijn Cambie:** optimization of entropy/coupling constants.
- **Masahiro Hachimori and Kenji Kashiwabara:** Lean-verified averaging theorem for ideal families. ([arxiv.org](https://arxiv.org/search/?abstracts=show&order=-announced_date_first&query=%22union-closed+sets+conjecture%22&searchtype=all&size=100))

There is substantial **automated mathematics** prior art:

- exact integer programming and cutting planes for FC families;
- formally verified FC(6) classification;
- public Maple, Sage and Matlab optimization code;
- recent Lean proofs of restricted results and entropy inequalities.

I found **no publicly documented LLM/AI-assisted project whose objective is to search globally for an explicit Frankl counterexample**, and no announced distributed SAT campaign at \(n=13\) or \(m=51\). My searches included “AI,” “LLM,” “machine learning,” “SAT,” “automated,” “Lean,” “counterexample,” and recent arXiv listings. This negative does not cover private projects, unpublished solver runs, or closed grant/internal repositories.

---

# TRACTABILITY CALL

## Verification

A proposed witness is extremely cheap to verify:

1. hash all sets;
2. compute all \(m(m+1)/2\) pairwise unions and check membership;
3. count each element’s degree;
4. verify every degree is \(<m/2\).

For \(n=13,m=51\), this is essentially instantaneous. The certificate is only a few hundred bytes to a few kilobytes.

## Search

The raw number of 51-member subfamilies of \(2^{[13]}\) is
\[
\binom{8192}{51}\approx 2\times10^{133}.
\]
Quotienting by the \(13!\) ground-set permutations removes only about ten decimal orders of magnitude. Union closure cuts this sharply, but no parametrization is known that turns the remaining space into anything remotely polynomial or even moderately enumerable.

More importantly:

- there is no upper bound on the size of a smallest counterexample if one exists;
- \(n=13,m=51\) is merely the first permitted point, not a theoretically likely point;
- the exact conjecture has survived all complete searches through \(n=12\) and \(m=50\);
- approximate low-frequency constructions do not survive exact closure in an obvious way;
- FC cuts and structural constraints prune many branches but have not produced a compact classification of the remaining families.

The **single biggest obstacle is not witness verification but the absence of a compact, symmetry-free parametrization—or any reason to expect the smallest counterexample near the current boundary**.

If compute must be spent, the only defensible experiment is a tightly bounded SAT/CP-SAT attack on \((13,51)\), followed by nearby \(m\), using separating incidence matrices, canonical labeling, lazy union witnesses and FC cuts. An UNSAT certificate would be a useful incremental result, but it would not materially raise the probability of finding a counterexample elsewhere.

## Coverage limitations

- I searched public arXiv listings through August 13, 2026 and publicly indexed journal/repository pages.
- I could not query closed MathSciNet or Zentralblatt records directly.
- Some older papers have incomplete public DOI metadata; I have said “not located” rather than guessing.
- I did not recover the complete numerical \(FC(k,n)\) tables from Pulaj–Wood’s paper; those should be imported before implementing a local-configuration search.
- I found no formal published audit of the latest Demontis, Agama, or revised Blinovsky–Speranca claimed proofs; their non-acceptance is inferred from the absence of independent validation and from later primary literature continuing to treat Frankl as open.

**VERDICT: OPEN | HOPELESS**

The first genuinely live exact slice is \(n=13,m=51\), but even that slice sits inside an enormous, highly symmetric search space with no reason to contain a witness. Verification is trivial, yet the accumulated structural evidence, exhaustive dead zones and lack of any bound on the smallest counterexample make a broad AI-assisted counterexample hunt a poor use of serious compute.