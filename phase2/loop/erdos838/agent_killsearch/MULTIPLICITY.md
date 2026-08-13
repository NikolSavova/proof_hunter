# Erdős 838: multiplicity, transitive paths, and split-to-convex conversion

**Sweep date:** 2026-08-13. This is an agent-only literature/idea report. All
logarithms in the asymptotic calculations below are base \(2\), and
\(L=\log_2 n\).

## Bottom line

1. I found **no published multiplicity theorem for convex \(k\)-gons that is
   stronger in the regime \(k=\Theta(\log n)\)** than the elementary uniform
   double count through the Erdős--Szekeres threshold. That count gives

   \[
   \#\{\text{convex }k\text{-subsets}\}
   \geq \frac{\binom nk}{\binom{ES(k)}k}
   =2^{(\beta(1-\beta)+o(1))L^2},\qquad k=\beta L,
   \]

   and hence coefficient \(1/4\) at \(k=(1/2+o(1))L\). The modern
   fixed-\(k\) literature does state the exact supersaturation lemma, but its
   optimized growing-\(k\) consequence does not appear to have been developed
   beyond this.

2. Baek--Balko's exact threshold \(2^{k-2}+1\) implies, by the same double
   count, **\(2^{(1/4-o(1))L^2}\) split \(k\)-gons** for
   \(k=(1/2+o(1))L\). This remains valid for abstract split polygons in a
   transitive two-coloring of ordered triples. I found no paper that states
   this supersaturation corollary explicitly; Baek--Balko prove an existence
   threshold, not a copy-count theorem.

3. For a single monochromatic monotone path, the exact cap--cup threshold is
   about \(2^{2k}\), so the analogous uniform count gives only coefficient
   \(1/8\), optimized at \(k=(1/4+o(1))L\).

4. I found **no theorem converting a split \(k\)-gon to a convex
   \(k-O(1)\)-gon, or even to a nearly same-size convex polygon with a useful
   bounded fibre**. The only unconditional conversion is to the larger of its
   cap and cup, of size at least \((k+2)/2\). Baek--Balko explicitly say that
   making the two left endpoints meet at the exact split threshold would
   resolve the Erdős--Szekeres conjecture. A \(k-O(1)\) extraction theorem
   alone would already improve the general upper bound to
   \(ES(r)\leq 2^{r+O(1)}\), well beyond the current \(2^{r+o(r)}\) theorem.

5. A genuinely actionable 2024 ingredient is Bukh--Vasileuski's polynomial
   same-type lemma. A conservative direct corollary gives \(k\) disjoint
   blocks, every transversal of which is a convex \(k\)-gon, with block size
   at least

   \[
   2^{-400}n\,ES(k)^{-5}.
   \]

   Thus it produces at least
   \(2^{(1/20-o(1))L^2}\) convex polygons of one size when \(k\sim L/10\).
   This is weaker than the unstructured \(1/4\) count, but the complete
   product structure may be useful in an iterative or weighted argument. I
   did not locate this explicit corollary in print.

## 1. What is actually known for the minimum number of convex \(k\)-gons

Mackey--Subercaseaux define \(\mu_k(n)\) as the minimum number of convex
\(k\)-gons among \(n\) planar points in general position. Their Lemma 1 is the
standard supersaturation double count:

> If \(\mu_k(m)\geq r\), then for every \(n\geq m\),
> \[
> \mu_k(n)\geq r\frac{\binom nk}{\binom mk}.
> \]

See J. Mackey and B. Subercaseaux, “Pentagon Minimization without
Computation,” lines 67--111 of the
[primary arXiv PDF](https://arxiv.org/pdf/2409.17098). The paper uses the
lemma mainly for fixed \(k\), defines
\(c_k=\lim_{n\to\infty}\mu_k(n)/\binom nk\), and observes
\(c_k\geq 1/\binom{ES(k)}k\). Its main new theorem concerns \(k=5\).

Taking \(m=ES(k)\) and \(r=1\), and using

\[
\log_2 ES(k)=k+O(\sqrt{k\log k}),
\]

gives, uniformly for \(k=\beta L+O(1)\),

\[
\begin{aligned}
\log_2\mu_k(n)
&\geq \log_2\frac{\binom nk}{\binom{ES(k)}k}\\
&=k\bigl(L-\log_2 ES(k)\bigr)+o(L^2)\\
&=\bigl(\beta-\beta^2-o(1)\bigr)L^2.
\end{aligned}
\]

The current \(ES(k)\) estimate is due to Holmsen--Mojarrad--Pach--Tardos;
it is also quoted with the displayed error term in the Mackey--Subercaseaux
introduction. The exponent is maximized by \(\beta=1/2\), giving \(1/4\).

The broader counting literature I found is fixed-parameter: rectilinear
crossings for \(k=4\), flag-algebra/SAT and planar-point equations for \(k=5\),
and \(\Theta(n^k)\) statements with \(k\) fixed. Aichholzer et al.'s survey
table explicitly labels its convex-\(k\)-gon results as “constant \(k\)”:
[primary arXiv paper, arXiv:1409.0081](https://arxiv.org/pdf/1409.0081).
Empty-polygon results in which \(k\) can grow like
\(O(\log n/\log\log n)\) concern the **maximum** number of holes and do not
give a minimum count of ordinary convex \(k\)-subsets.

**Prior-art verdict.** The \(1/4\) lower coefficient is an immediate and now
public consequence of a standard published lemma, and it also appears in the
2026 discussion of [Erdős Problem 838](https://www.erdosproblems.com/forum/thread/838).
It should not be presented as a new theorem. I found no stronger published
uniform coefficient.

## 2. Positive-fraction/cluster theorems do not beat the uniform double count

### 2.1 Earlier positive-fraction theorem

Bárány--Valtr prove that for each fixed \(k\) there are \(k\) linear-size
blocks such that every transversal is in convex position:
[primary 1998 PDF](https://www.renyi.hu/~barany/cikkek/72.pdf). Pór--Valtr
later obtain exponentially small dependence on \(k\); for planar point sets
the frequently quoted explicit form is block size at least
\(k2^{-32k}n\), while their more general convex-body theorem gives
\(2^{-37.8k-o(k)}n\):
[journal page and full theorem](https://www.sciencedirect.com/science/article/pii/S019566980600117X),
[DOI](https://doi.org/10.1016/j.ejc.2006.06.015).

Even the \(2^{-32k}\) point-set form yields only

\[
\log_2( (2^{-32k}n)^k )\geq kL-32k^2-O(k\log k),
\]

whose optimized coefficient is \(1/128\). Thus this classical structured
theorem is far weaker for total multiplicity than the direct \(1/4\) double
count.

### 2.2 A 2024 polynomial same-type lemma gives a better structured corollary

Bukh--Vasileuski prove, for disjoint \(X_1,\dots,X_m\subset\mathbb R^d\),
that one can retain \(Y_i\subset X_i\) with all transversals having the same
order type and

\[
c(m,d)\geq d^{-50d^3}m^{-d^2}.
\]

See Theorem 1 of B. Bukh and A. Vasileuski, “New bounds for the same-type
lemma,” EJC 31(2) (2024), #P2.60,
[primary PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v31i2p60/pdf),
[DOI](https://doi.org/10.37236/12414). In the plane this is

\[
c(m,2)\geq 2^{-400}m^{-4}.
\]

Here is a direct corollary worth retaining.

**Structured growing-\(k\) lemma.** Partition an \(n\)-point set into
\(m=ES(k)\) disjoint parts of size at least \(\lfloor n/m\rfloor\). Apply the
same-type lemma, choose one representative from each resulting block, and
apply Erdős--Szekeres to the \(m\) representatives. For the selected \(k\)
indices, every transversal is convex and every block has size at least

\[
s\geq 2^{-400}m^{-4}\lfloor n/m\rfloor
  =2^{-400}n\,ES(k)^{-5}-O(1).
\]

Consequently there are at least \(s^k\) convex \(k\)-gons with a complete
\(k\)-partite product structure. With \(k=\beta L\),

\[
\log_2 s^k\geq (\beta-5\beta^2-o(1))L^2,
\]

maximized at \(\beta=1/10\) with coefficient \(1/20\).

This still cannot improve the total-count lower bound, but unlike the raw
double count it supplies independently choosable blocks. It is a plausible
ingredient for a recursive weighted construction. The factor \(ES(k)^{-5}\)
above is deliberately conservative: four powers come from the published
same-type constant and one from partitioning into \(m\) disjoint input sets.

## 3. Monochromatic monotone paths in transitive rank-3 colorings

Let an ordered triple coloring be *transitive* when each color class has the
property that two same-color consecutive triples on a four-set force all
four triples to have that color. Moshkovitz--Shapira prove that, in a
transitive coloring, a monochromatic monotone path on \(k\) vertices induces
a monochromatic complete 3-graph on those vertices (their Lemmas 6.1--6.2):
[primary paper](https://arxiv.org/pdf/1105.2097), pp. 18--19. Their paper
studies Ramsey, online-Ramsey, and size-Ramsey thresholds; its \(S_k(q,n)\)
is a minimum **number of host edges**, not a number of path copies. I found no
path-copy supersaturation theorem there.

For two colors, the exact cap--cup/monotone-path threshold is

\[
M_k=\binom{2k-4}{k-2}+1=2^{2k-O(\log k)}.
\]

Double-counting \(M_k\)-subsets therefore gives at least

\[
\frac{\binom nk}{\binom{M_k}k}
=2^{(\beta(1-2\beta)+o(1))L^2}
\]

monochromatic monotone \(k\)-paths in every ordered triple coloring, hence
also in every transitive one. The optimum is \(\beta=1/4\), coefficient
\(1/8\). Transitivity upgrades each counted path to a homogeneous \(k\)-set,
but does not increase this guaranteed count.

Suk--Zeng prove a powerful **rank-2** block-monotone-path theorem: in a
\(q\)-coloring of the pairs of \([N]\), they find a block-monotone path with
linear-size interchangeable vertex blocks; see Theorem 2.3 and the
introduction of [their primary paper](https://arxiv.org/pdf/2112.01750).
Their proof starts by counting monochromatic length-3 graph paths, but I
found no rank-3/transitive analogue that supplies interchangeable blocks for
tight paths. The obstruction is the familiar one: a tight-path extension
remembers the last two vertices, not adjacency/orientation to the whole
previous history.

## 4. Split polygons are abundant, but the abundance is not convex abundance

Baek--Balko prove exactly

\[
ES_{\rm split}(k)=C_{\rm split}(k,k,k)=2^{k-2}+1.
\]

Here \(C_{\rm split}\) is the corresponding threshold for arbitrary
two-colorings of the ordered complete 3-graph. See Theorems 3 and 6 of
[the primary SoCG 2025 paper](https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/LIPIcs.SoCG.2025.13/LIPIcs.SoCG.2025.13.pdf),
later published as JCTA 222 (2026), 106195,
[journal DOI](https://doi.org/10.1016/j.jcta.2026.106195).

In a geometric coloring, the constituent red and blue paths of a split
\(k\)-gon share either one or two vertices, so its vertex support has size
\(k+1\) or \(k\). The same conclusion holds in a transitive coloring: each
path is a monochromatic clique by Moshkovitz--Shapira, and opposite-color
cliques cannot share three vertices.

Let \(M=2^{k-2}+1\), and let \(s_k(P)\) be the number of distinct split
\(k\)-gon supports in an \(n\)-point set (or a transitive triple-coloring).
Every \(M\)-subset contains one. A support of size \(k\) is contained in
\(\binom{n-k}{M-k}\) such subsets, and a support of size \(k+1\) is contained
in fewer. Hence

\[
s_k(P)\binom{n-k}{M-k}\geq\binom nM,
\qquad
s_k(P)\geq\frac{\binom nk}{\binom Mk}.
\]

For \(k=\beta L\), this is

\[
\log_2s_k(P)\geq(\beta(1-\beta)-o(1))L^2,
\]

again optimized at coefficient \(1/4\). This is a clean supersaturation
corollary of the exact threshold, but it counts relaxed objects.

## 5. Why no bounded-fibre conversion was found

A split \(k\)-gon is an \(a\)-cap and a \(u\)-cup sharing their rightmost
point, with \(a+u=k+2\). It is convex precisely in the favorable case in
which the two paths also share their leftmost point. Baek--Balko say
explicitly (Section 2.3, pp. 4--5) that enforcing this second common endpoint
without raising the threshold would resolve the Erdős--Szekeres conjecture,
and that their down-set structure is not strong enough to do it.

The unconditional extraction is only

\[
h=\max\{a,u\}\geq\left\lceil\frac{k+2}{2}\right\rceil,
\]

because either constituent path is itself in convex position. If one maps a
split object to its larger path \(H\), a crude fibre bound for fixed
\(|H|=h\) is

\[
O\!\left(\binom{n-1}{k+1-h}\right),
\]

obtained by choosing the other path's vertices besides the shared right
endpoint. In the balanced case this permits a loss \(n^{k/2+O(1)}\), which is
of order \(2^{\Theta(L^2)}\) and destroys the useful split multiplicity.
The fibre is genuinely not bounded independently of \(n\) for this natural
map: put all points on a strict cup, fix a \(k\)-cup \(H\), and pair it with a
2-cap consisting of its right endpoint and any point outside \(H\) to the
left. This gives \(\Omega(n-k)\) distinct split supports mapping to \(H\).

No paper located in the split-polygon citation/search trail proves a
\(k-o(k)\), \(k-O(1)\), or bounded-fibre extraction. Indeed, a theorem saying
that every split \(k\)-gon contains a convex \((k-C)\)-gon would imply

\[
ES(r)\leq 2^{r+C-2}+1,
\]

by taking \(k=r+C\), a major improvement over the current upper bound.
Accordingly this is a high-risk proof target, not a hidden standard lemma.

## 6. Actionable takeaways

* For an unconditional lower bound, use the published supersaturation lemma
  directly; it already gives the base-2 \(1/4\) coefficient uniformly.
* If split polygons enter a proof, record their parameter pair \((a,u)\) and
  both endpoint states. Merely mapping to the larger path has a potentially
  \(n^{\Theta(k)}\) fibre.
* The exact split threshold does give a strong \(1/4\)-coefficient supply of
  relaxed certificates. A useful new lemma would have to force a common
  left endpoint on a large subfamily, or map those certificates to convex
  sets with fibre \(2^{o(L^2)}\); no such result was found.
* Bukh--Vasileuski's polynomial same-type lemma is the strongest located
  source of product structure. It is numerically weaker for raw counting,
  but it may support an iteration in which a convex index set is replaced by
  an entire Cartesian product of choices.

## Novelty/risk verdict

* **Prior art:** fixed-\(k\) supersaturation and its \(1/4\) uniform
  consequence; exact existence thresholds for monotone paths and split
  polygons; positive-fraction convex clusters.
* **Not found:** any uniform growing-\(k\) convex-copy theorem exceeding
  \(1/4\); any multiplicity theorem specialized to transitive rank-3 split
  paths; any near-size bounded-fibre split-to-convex conversion.
* **Main risk:** a purported split-to-convex lemma is likely as hard as a
  substantial strengthening of the Erdős--Szekeres theorem. It needs an
  independent proof, not a citation placeholder.
