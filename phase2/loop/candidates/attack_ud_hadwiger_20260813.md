# ud_hadwiger (gpt-5.6-sol, effort=max, 2026-08-13 09:45)

## Bottom line

The literal inference

\[
\text{more unit distances}\quad\Longrightarrow\quad\text{plausibly }\chi\ge 6
\]

does **not** survive. Objections **(a)** and especially **(b)** kill that rationale, while **(d)** shows that essentially this exact question was raised on May 23, 2026 and a preliminary attempt stalled. Objection **(c)** is not a problem: the constructions really do give exact unit distances at one common scale.

A narrower algebraic-Cayley-graph search survives, but it is substantially different from exploiting the asymptotic density theorem.

One status correction: Sawin’s published theorem gives exponent \(1.014114\ldots\). Subsequent computational claims reached roughly \(1.0357\)–\(1.0358\), with corrections and some values still marked unverified. As of August 13, 2026, the Hadwiger–Nelson bounds remain \(5\leq\chi(\mathbb R^2)\leq7\); the August 5 Haugland preprint constructs another 5-chromatic graph, not a 6-chromatic one. ([arxiv.org](https://arxiv.org/html/2605.20579v1))

## The useful reformulation

For Sawin’s version, fix a CM extension \(K/F\), fractional ideal \(I\), conjugation \(c\), and \(\alpha\in F\). The relevant infinite graph is essentially

\[
X(K,I,\alpha)
=
\operatorname{Cay}\!\left(
I,\,
S_\alpha
\right),
\qquad
S_\alpha=\{\beta\in I:\beta c(\beta)=\alpha\}.
\]

Under one complex embedding, scaled once by \(\sqrt{|\alpha|}\), every vector in \(S_\alpha\) has Euclidean length exactly one. The finite examples are windows in this additive Cayley graph. Conversely, a unit-length difference between two points in the same embedded ideal satisfies the same norm equation, so this is not merely a selected subgraph with arbitrary hidden geometry. ([arxiv.org](https://arxiv.org/html/2605.20579v1))

This gives the correct chromatic question:

> Is one of these algebraic Cayley graphs non-5-colourable?

If yes, de Bruijn–Erdős supplies a finite non-5-colourable subgraph. If an entire Cayley graph has a 5-colouring—particularly a modular or homomorphic one—then every asymptotic window from it is automatically harmless.

That question is meaningful. The edge exponent itself is not.

## (a) Asymptotic versus finite

**Verdict: fatal to the proposed inference, though not a logical impossibility.**

Every member of the family is finite, so asymptoticity does not logically prevent one member from being 6-chromatic. But the theorem proves only

\[
e(G_n)\ge n^{1+\delta}.
\]

It says nothing about \(\chi(G_n)\), independence numbers, critical subgraphs, or failure of 5-colourings. All members could conceivably be 5-, 4-, or even 2-colourable.

There is also a severe practical obstruction. Sawin estimated that the smallest example guaranteed by one optimized version has on the order of

\[
10^{1{,}957{,}151}
\]

points. Thus “extract the graph and run a colouring solver” is not a strategy. The original simplified construction is much larger still. ([reddit.com](https://www.reddit.com/r/math/comments/1tj534d/openais_internal_model_disproves_unit_distance/))

So:

- **Not fatal:** studying the associated infinite Cayley graph algebraically.
- **Fatal:** expecting the asymptotic theorem to hand over a usable finite candidate.

## (b) Density is the wrong invariant

**Verdict: this is the principal killer.**

An edge-count-only argument would need near-quadratic density. A 5-colourable graph may have as many as

\[
\left(1-\frac15\right)\frac{n^2}{2}=0.4n^2
\]

edges. Hence the general density threshold forcing \(\chi\ge6\) is quadratic, while \(n^{1.014}\) is \(o(n^2)\). The exponent improvement is revolutionary for the Erdős extremal problem but almost invisible to ordinary chromatic extremal theory.

More structurally, the new edges arise by taking many norm-shell vectors and translating them from many interior lattice points. That produces high repeated degree. It does not automatically produce the overlapping odd cycles, incompatible colour propagations, or critical gadgets used by de Grey, Heule, Parts, and related constructions. A large generator set in a Cayley graph can still admit a very simple quotient colouring.

The right quantities would be one of:

1. an explicit 6-critical subgraph;
2. proof that the infinite Cayley graph has no 5-colouring;
3. an independence bound such as \(\alpha(G)<|V(G)|/5\);
4. a spectral or additive-expansion argument strong enough to imply such an independence bound;
5. failure of every suitable homomorphic/modular 5-colouring.

None of these is supplied by the unit-distance disproof. Known 5-chromatic examples are comparatively sparse and were discovered through colour-forcing structure, confirming that raw edge count is neither necessary nor a good predictor. ([mathworld.wolfram.com](https://mathworld.wolfram.com/PartsGraphs.html?utm_source=openai))

## (c) Scale and realizability

**Verdict: passes. This objection does not kill the idea.**

The constructions genuinely operate at one scale:

- In the simplified OpenAI construction, selected difference vectors have modulus one in every complex embedding.
- In Sawin’s construction, vectors satisfy \(\beta c(\beta)=\alpha\), and one global division by \(\sqrt{|\alpha_v|}\) makes all their selected projections exactly unit length.

There is no pair-dependent rescaling and no approximate geometry. Projection is injective, so distinct lattice points remain distinct planar points. ([arxiv.org](https://arxiv.org/html/2605.20695v1))

Nor are these points in generic position. They are highly algebraic and contain many exact relations. The problem is instead that the relations were selected to maximize the number of equal norm representations, not to force colouring contradictions. Euclidean rigidity and colouring rigidity are different resources.

## (d) Has this already been tried?

**Yes—at least preliminarily, and the exact question was publicly asked.**

On the Erdős Problems discussion thread, Gil Kalai asked whether the new unit-distance constructions were relevant to colouring unit-distance graphs. Nat Sothanaphan reported a preliminary GPT-5.5 investigation:

- the original OpenAI construction and the human simplification appeared unsuitable;
- Sawin’s added flexibility initially looked more promising;
- after trying modifications, the approach stalled without a clear route.

Thomas Bloom’s stated heuristic was that these are algebraic Cayley graphs and may therefore have low chromatic number, while explicitly acknowledging that this is not a theorem. Sothanaphan then pointed out that the broader number-theoretic ring direction remains plausible: Polymath16’s homomorphic-colouring work produced rings of chromatic numbers \(2,3,4,5\), and the Moser ring computationally supports a particularly structured route to 5-chromatic graphs. ([erdosproblems.com](https://www.erdosproblems.com/forum/thread/90?utm_source=openai))

Kalai also noted in his comments that number-field constructions had already appeared in Polymath16’s colouring work. Thus the broad “algebraic fields might help Hadwiger–Nelson” insight predates the 2026 disproof; what is new is the particular high-degree tower machinery. ([gilkalai.wordpress.com](https://gilkalai.wordpress.com/2026/05/21/amazing-erdos-unit-distance-problem-was-disproved-it-was-achieved-by-ai/))

I found no arXiv claim through August 13, 2026 connecting the Golod–Shafarevich construction to a 6-chromatic planar unit-distance graph. The targeted recent search instead found continuing work on new or smaller **5**-chromatic graphs, including Haugland’s August 5 construction. The de Grey–Parts paper surfaced by the search concerns minimum orders of \(k\)-chromatic unit-distance graphs, not the new towers. ([arxiv.org](https://arxiv.org/abs/2608.04542?utm_source=openai))

So the idea has not been formally disproved, but it has already received the obvious first pass and did not pay out.

## (e) Upper bounds and measurable/Borel variants

### Ordinary upper bound

The constructions offer essentially nothing toward \(\chi(\mathbb R^2)\le6\) or even the existing \(\le7\). A finite configuration is an obstruction and therefore naturally supplies **lower** bounds. An upper bound requires a colouring of every point of the plane—normally a global tiling, partition, or graph homomorphism. A colouring of one countable algebraic subgroup does not automatically extend to \(\mathbb R^2\).

### Measurable and Borel colourings

A finite 6-chromatic unit-distance graph would, of course, also force the measurable and Borel chromatic numbers to be at least six. But mere superlinear edge count provides no extra measurable leverage: every finite configuration, and indeed the whole countable algebraic subgroup, has Lebesgue measure zero. These constructions do not produce positive-density measurable colour obstructions.

### Fractional chromatic number

This is the one variant with a plausible surviving connection. Finite graphs give bounds through

\[
\chi_f(G)\ge \frac{|V(G)|}{\alpha(G)}.
\]

The Cayley structure may permit Fourier, spectral, or weighted-independence analysis. But this requires control of \(\alpha(G)\), not control of \(e(G)\). Current plane-fractional work is likewise organized around independence ratios rather than unit-distance counts. ([erdosproblems.com](https://www.erdosproblems.com/forum/thread/508?embed=1&utm_source=openai))

## Strongest defensible surviving version

The defensible claim is:

> The disproof identifies a structured family of algebraic unit-distance Cayley graphs whose chromatic and independence properties deserve testing; it gives no evidence that the asymptotically dense members are 6-chromatic.

The Golod–Shafarevich tower itself is probably overhead for Hadwiger–Nelson. Its purpose is to make field degree tend to infinity while controlling discriminants and splitting, exactly what the edge-exponent problem needs. Hadwiger–Nelson needs one obstruction, so the appropriate search should use low-degree CM fields and rich norm-one shells.

### Concrete next step

Run a bounded adversarial pilot, not a tower construction:

1. Start with a low-degree field containing the established Moser-ring coordinates, for example
   \[
   K_0=\mathbb Q(i,\sqrt3,\sqrt{11}),
   \]
   or directly the corresponding order.
2. Add norm-one directions using Sawin-style choices of split primes and denominators, but without requiring an infinite tower.
3. Before building large windows, search for:
   - residue or quotient colourings with at most five colours;
   - homomorphisms into known 5-colourable finite graphs;
   - periodic 5-colourings of the additive Cayley graph.
   
   Any such colouring kills the entire parameter choice.
4. Only candidates resisting those tests should be expanded into exact finite windows and sent to a 5-colour SAT solver.
5. A successful result must end with a small unsatisfiable core or independently checkable colouring certificate—not merely a graph with unusually many edges.
6. In parallel, compute spectral/independence bounds; these may be more informative for fractional chromatic questions.

This is worth one tightly scoped computational experiment. It is not yet worth building theory around the asymptotic family.

**VERDICT: MARGINAL.** The literal proposal is killed by **(a)** and **(b)**: the first guaranteed configurations are astronomically large, and their superlinear edge count supplies no chromatic obstruction. **(d)** further shows that the exact connection was already proposed and preliminarily explored without success. **(c)** is fine—the geometry is exact and single-scale—but that only establishes realizability, not colour forcing. What survives is a narrower, already partly established Polymath-style program: study low-degree algebraic norm-shell Cayley graphs, attack them first with homomorphic 5-colourings, and use SAT or independence bounds only on candidates that resist.