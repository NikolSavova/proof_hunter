# Prior-art sweep — seymour (gpt-5.6-sol, effort=max, 2026-08-13 08:29)

> Counterexample-shaped target, selected after the Jacobian conjecture
> counterexample (Alpoge/Fable 5, 2026-07-20). Sweep asks BOTH whether the
> problem is already resolved AND where counterexample search is already dead.

# Bottom line

**1. STATUS as of August 13, 2026: OPEN.**

I found one 2024–2026 arXiv manuscript claiming a complete proof—Charles N. Glover, arXiv:2501.00614—but it is not an accepted resolution and contains invalid BFS-layer arguments on which the main theorem depends. In particular, its “degree partition” treats every same-layer out-neighbor of a child as also an out-neighbor of that child’s chosen parent, and a later reduction assumes an arbitrary out-neighbor of a vertex in layer \(R_i\) must lie in \(R_{i+1}\); neither is true for directed BFS layers. Subsequent papers dated March 31, June 29, and August 12, 2026 continue to call the conjecture open and prove only special cases. ([arxiv.org](https://arxiv.org/abs/2501.00614))

**Immediate computational consequence:** if the June 29 minimum-outdegree-\(7\) preprint and the August 12 dense-case preprint are correct, then a counterexample has

\[
n\ge 19,\qquad \delta^+\ge 8,
\]

and at \(n=19\) it must have **minimum outdegree exactly \(8\)**. The first degree slice to attack is therefore plausibly

\[
\boxed{\delta^+=8,\quad 19\le n\le 36},
\]

where the upper endpoint uses the published degree-parametrized reduction quoted below. ([arxiv.org](https://arxiv.org/abs/2608.11530))

The largest explicit whole-space brute-force enumeration I located is only **\(n=7\)**, in an archived but subsequently withdrawn 2026 preprint. It is analytically superseded by much stronger theorems and has not been independently audited here. ([arxiv.org](https://arxiv.org/abs/2601.21563v1))

## Axis checked

I checked the exact target:

- finite oriented simple graphs;
- no loops or digons;
- unweighted cardinalities;
- \(N^{++}(v)\) means vertices at exact positive distance two, excluding \(v\) and first out-neighbors.

I did **not** conflate this with:

- tournaments or near-tournaments;
- Sullivan’s in-neighborhood variants;
- arbitrary digraphs allowing digons;
- infinite or locally finite digraphs;
- weighted tournament theorems;
- counting length-two walks with multiplicity;
- minimum total degree or underlying degree, where a theorem only concerns minimum **outdegree**.

---

# 2. Where counterexample search is already dead

## 2.1 The quantitative order floor

Let \(\delta=\delta^+(D)\). Since an \(n\)-vertex oriented graph has at most \(\binom n2\) arcs,

\[
n\delta\le \binom n2,\qquad n\ge 2\delta+1.
\]

The equality case is a regular tournament.

| Evidence used | Orders ruled out | First possible order |
|---|---:|---:|
| Fisher’s tournament theorem + Kaneko–Locke \(\delta\le6\) | \(n\le15\) | \(n=16\) |
| Add Brukhman’s August 12, 2026 theorem \(n\le2\delta+2\) | \(n\le16\) | \(n=17\) |
| Add only Sadhukhan–Sandeep–Sen’s June 29, 2026 theorem \(\delta=7\) | \(n\le17\) | \(n=18\) |
| Add **both** 2026 preprints | \(n\le18\) | **\(n=19\)** |

The last line follows because a counterexample would have \(\delta\ge8\), while Brukhman rules out \(n\le2\delta+2\). At \(n=19\), \(\delta\ge9\) would force all \(171=\binom{19}{2}\) possible arcs and hence a regular tournament, so the only live degree is \(\delta=8\). ([arxiv.org](https://arxiv.org/abs/2608.11530))

**Reliability warning:** the \(n\ge19\) floor relies on two very recent, unrefereed preprints—one submitted June 29 and the other August 12, 2026. For a production search, I would first independently check Brukhman’s five-page counting proof and rerun the Sadhukhan–Sandeep–Sen CP-SAT models.

## 2.2 Minimum outdegree

- **Peer-reviewed/classical:** Kaneko and Locke proved that every oriented graph with \(\delta^+\le6\) has a Seymour vertex. Therefore every counterexample has \(\delta^+\ge7\). ([doi.org](https://doi.org/10.1007/S00373-026-03014-Y))
- **Current preprint frontier:** Sadhukhan, Sandeep and Sen claim the case \(\delta^+=7\), using structural reductions followed by OR-Tools CP-SAT infeasibility checks. Thus, conditional on this preprint, every counterexample has \(\delta^+\ge8\). ([arxiv.org](https://arxiv.org/abs/2606.30588))
- Their computer-assisted part is **not** an exhaustive search over all graphs of a given order. It eliminates local obstruction models in the difficult \(|A|=7,\ |B|=6,\ |A_1|=2\) branch, further divided into \(r=5\) and \(r=6\) cases. ([arxiv.org](https://arxiv.org/html/2606.30588v1))

## 2.3 Degree-parametrized finite reduction

Guo, Kang and Zwaneveld quote the following result of Zelenskyi, Darmosiuk and Nalivayko:

> If there is a counterexample of minimum outdegree \(\delta\), then there is one on at most  
> \[
> \binom{\delta+1}{2}
> \]
> vertices.

They also report that a vertex-minimal counterexample satisfies \(\delta^+\ge\sqrt n\), while Espuny Díaz et al. show that if the conjecture is false, arbitrarily large strongly connected counterexamples exist with bounded minimum outdegree. These statements concern different axes: the former constrains a minimal seed; the latter says a seed can be amplified to arbitrarily large examples. ([arxiv.org](https://arxiv.org/html/2603.29626))

Combining the recent order theorem with that finite reduction gives degree slices:

| Minimum outdegree | Necessary order range for a seed |
|---:|---:|
| \(8\) | \(19\le n\le36\) |
| \(9\) | \(21\le n\le45\) |
| \(10\) | \(23\le n\le55\) |
| general \(\delta\) | \(2\delta+3\le n\le\binom{\delta+1}{2}\) |

The upper bound is important enough that I recommend checking the original 2021 proof before making it foundational to a large compute campaign; in this pass I verified the statement through the 2026 primary preprint that cites it, not by independently reconstructing the original argument.

## 2.4 Exhaustive enumeration

The archived version 1 of Halkiewicz’s 2026 preprint claims exhaustive enumeration of every labeled oriented graph on at most seven vertices:

- total \(n=7\) space: \(3^{21}\approx1.046\times10^{10}\);
- about \(5.2\times10^9\) graphs remained after filtering graphs with minimum outdegree zero;
- Julia bitmask implementation;
- claimed throughput approximately \(1.5\times10^6\) graphs/second;
- source code linked at `https://github.com/profsms/snc`. ([arxiv.org](https://arxiv.org/pdf/2601.21563v1))

However:

1. The whole arXiv submission was withdrawn on July 23, 2026.
2. I did not rerun or audit the code.
3. The computation has no published SAT/DRAT/LRAT certificate.
4. The range \(n\le7\) was already trivial from \(\delta^+\le6\), so it does not move the practical search floor.

Thus:

\[
\boxed{N_{\rm enum}=7\text{ claimed in a withdrawn preprint; no peer-reviewed larger enumeration found.}}
\]

I found **no published whole-space SAT verification through \(n=8\), \(9\), …, \(18\)**. The useful floor is theorem-based, not enumeration-based.

## 2.5 Tournaments and weighted tournament versions

- Fisher proved Dean’s conjecture for all tournaments in 1996.
- Correction to the question’s parenthetical: **Fisher used Farkas’ lemma, not median orders**.
- Havet and Thomassé supplied the later median-order/feed-vertex proof in 2000.
- Weighted median-order formulations prove the vertex-weighted tournament version.
- Seacrest proved an **arc-weighted tournament** version in 2015. This does not solve the arc-weighted conjecture for arbitrary oriented graphs. ([arxiv.org](https://arxiv.org/html/2412.20234v1))

The arbitrary vertex-weighted version is essentially equivalent to the unweighted problem for nonnegative rational weights by replacing each vertex with an independent twin class of the corresponding size. The arc-weighted formulation is genuinely different.

## 2.6 Missing-edge and structural classes

The “missing graph” here is the graph of nonadjacent vertex pairs, not the oriented graph itself.

Proved regions include:

- tournaments missing a **matching**, **star**, or **clique** — Fidler and Yuster;
- tournaments missing a **generalized star** — Ghazal;
- missing edges partitionable into a **matching and a star** — Dara, Francis, Jacob and Narayanan;
- tournaments missing **two stars** — Daamouch, Ghazal and Al-Mniny;
- partial results for tournaments missing disjoint paths, particularly paths of length two;
- oriented graphs missing a **comb**, hence oriented combs and threshold graphs;
- the class where the missing graph is  
  \(\{C_4,\overline{C_4},S_3,\text{chair},\text{co-chair}\}\)-free;
- classes \(\mathcal D_{0,2}\), and more recently \(\mathcal D_{0,3}\cup\mathcal D_{1,1}\), where \(\mathcal D_{s,t}\) means the vertex set partitions into an \(s\)-degenerate and a \(t\)-degenerate induced subgraph. ([arxiv.org](https://arxiv.org/abs/2608.11530))

The latest peer-reviewed contribution in this direction is Haozhe Wang and Mei Lu, published February 8, 2026, proving the \(\mathcal D_{0,3}\) and \(\mathcal D_{1,1}\) cases and giving new median-order proofs for tournaments missing a matching or star. ([doi.org](https://doi.org/10.1007/S00373-026-03014-Y))

## 2.7 Girth, transitivity and degree-type constraints

Two axes must be distinguished:

- **Underlying triangle-free graph:** the conjecture is elementary. Choose a minimum-outdegree vertex \(v\). If \(v\to u\), then triangle-freeness forces every out-neighbor of \(u\) outside \(N^+(v)\), hence into \(N^{++}(v)\). Therefore  
  \[
  |N^{++}(v)|\ge d^+(u)\ge d^+(v).
  \]
- **Directed girth/anti-transitivity:** an online 2026 article proves that every \(k\)-anti-transitive digraph with directed girth greater than \(k-4\) has a Seymour vertex. It is assigned to *Discrete Applied Mathematics* 389, issue date August 15, 2026, DOI `10.1016/j.dam.2026.04.014`. As of August 13, the issue date is still two days in the future, though the article is online. ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0166218X26002337))
- Acyclic oriented graphs are trivial because they have a sink.

I located additional papers on \(m\)-free, \(k\)-transitive and highly connected regular digraphs, but I could not retrieve sufficiently precise full theorem hypotheses from the accessible publisher pages. I therefore do **not** count those abstract-level records as additional quantitative dead zones.

## 2.8 Cayley and random families

- Hamidoune’s result rules out **all Cayley digraphs** as counterexamples.
- In the abelian Cayley case, Guo–Kang–Zwaneveld completely classify the tight examples via additive-combinatorial critical pairs. ([arxiv.org](https://arxiv.org/html/2603.29626))
- For every fixed \(p<1/2\), asymptotically almost surely **every orientation** of \(G(n,p)\) satisfies Seymour’s conjecture.
- For fixed \(p>1/2\), the assertion that every orientation of \(G(n,p)\) satisfies the conjecture with probability bounded away from zero is equivalent to the full conjecture. Thus \(p=1/2\) is a genuine barrier in that representation. ([arxiv.org](https://arxiv.org/abs/2403.02842))
- Botler, Moura and Naia previously proved the all-orientations random result for \(p<1/4\), along with results for random orientations of pseudorandom graphs. ([arxiv.org](https://arxiv.org/abs/2211.06540))

These random results are structural/probabilistic evidence, not a finite exhaustive bound.

## 2.9 Best constant factor

Chen, Shen and Yuster proved that every oriented graph has a vertex satisfying

\[
|N^{++}(v)|\ge\lambda |N^+(v)|,
\]

where

\[
\lambda=0.657298\ldots
\]

is the real root of \(2x^3+x^2-1=0\). Their paper also mentioned \(0.67815\ldots\) as obtainable by similar methods, but did not supply it as the main fully developed theorem. ([arxiv.org](https://arxiv.org/html/2412.20234v1))

The current best public result is the 2024 preprint of Hao Huang and Fei Peng:

\[
\boxed{\gamma=0.715538\ldots},
\]

the unique root in \([0,1]\) of

\[
8x^5+4x^4-12x^3-7x^2+2x+4=0.
\]

It reduces a hypothetical \(\gamma\)-counterexample to an eleven-variable quadratic constraint satisfaction problem and proves that CSP infeasible. I found no later improvement through August 13, 2026. I also found no journal publication for this result, so \(0.657298\ldots\) remains the clearly peer-reviewed benchmark while \(0.715538\ldots\) is the best current preprint bound. ([arxiv.org](https://arxiv.org/abs/2412.20234))

---

# 3. Why is it believed?

## Structural evidence — type (a)

The belief is primarily structural, not primarily computational:

1. **The extremal dense case works.** All tournaments satisfy the conjecture, including weighted variants.
2. **A substantial universal margin is known.** The ratio has been pushed from the trivial \(1/2\) to \(0.715538\ldots\), substantially toward \(1\). ([arxiv.org](https://arxiv.org/html/2412.20234v1))
3. **Minimal counterexamples are constrained.** They can be taken strongly connected; vertex-minimal ones have high minimum outdegree; degree slices admit finite upper-order bounds. ([arxiv.org](https://arxiv.org/abs/2403.02842))
4. **Many structured dense classes work.** Missing matchings, stars, cliques, generalized stars, combs and several degeneracy classes are settled.
5. **Highly symmetric candidates work.** There are no Cayley counterexamples, and the abelian tight cases have an additive-combinatorial classification. ([arxiv.org](https://arxiv.org/html/2603.29626))
6. **Generic underlying graphs work.** For \(p<1/2\), almost every \(G(n,p)\) has the property that every orientation satisfies the conjecture. ([arxiv.org](https://arxiv.org/abs/2403.02842))

None of these is a near-proof of the general statement, but they are genuine structural reasons.

## Computational evidence — type (b)

The direct computational evidence is weak:

- the only whole-space enumeration found stops at \(n=7\);
- it is in a withdrawn preprint;
- \(n\le7\) was already covered analytically;
- the recent CP-SAT proof handles local \(\delta=7\) obstructions, not all graphs of an order;
- I found no certified SAT sweep at the live frontier \(n\ge19\).

So this is **not** a conjecture whose reputation rests on a heroic absence-of-counterexamples computation. If anything, the empirical side is surprisingly underdeveloped. The belief is predominantly type (a), although the broad structural evidence may still be compatible with a very special counterexample.

---

# 4. Reformulations and representation shifts

## 4.1 Square-of-a-digraph formulation

Let \(D^2\) add an arc \(v\to w\) whenever \(w\) is reachable from \(v\) in one or two steps. Then

\[
d^+_{D^2}(v)=|N^+(v)|+|N^{++}(v)|.
\]

The conjecture is equivalent to the existence of a vertex satisfying

\[
d^+_{D^2}(v)\ge2d^+_D(v).
\]

This is the “degree-doubling vertex” formulation used in the tournament literature.

## 4.2 Direct SAT/PB/CP-SAT encoding

For fixed \(n\), use Boolean variables \(a_{ij}\) for \(i\ne j\), with

\[
\neg(a_{ij}\land a_{ji})
\]

for every unordered pair. Introduce \(s_{ik}\) with

\[
s_{ik}\iff
\neg a_{ik}\ \land\ 
\bigvee_j(a_{ij}\land a_{jk}),
\qquad i\ne k.
\]

A counterexample is exactly a satisfying assignment of

\[
\sum_{k\ne i}s_{ik}\le
\sum_{j\ne i}a_{ij}-1
\quad\text{for every }i.
\]

Useful additional constraints are:

- \(\delta^+\ge8\);
- a distinguished minimum-degree root with degree \(d\);
- \(n\ge2d+3\);
- strong connectivity;
- degree-sequence and lexicographic symmetry breaking;
- exclusion of tournaments and known missing-edge classes;
- modular or twin reduction when searching for a smallest seed.

This is a compact encoding: at \(n=19\), there are only \(342\) directional arc variables and at most \(19\cdot18\cdot17=5814\) path-witness triples. The formula size is modest; proving UNSAT in a highly symmetric space is the difficult part.

I found **no published standard DIMACS SAT encoding or certified all-\(n\) SAT sweep**. The closest prior art is the local OR-Tools CP-SAT model in the \(\delta=7\) preprint. ([arxiv.org](https://arxiv.org/abs/2606.30588))

## 4.3 Minimum-outdegree neighborhood model

For a minimum-outdegree root \(v\), put

\[
A=N^+(v),\qquad B=N^{++}(v).
\]

In a counterexample,

\[
|A|=\delta,\qquad |B|\le\delta-1.
\]

This is the representation used by minimum-degree proofs. For the first live slice:

\[
|A|=8,\qquad |B|\le7.
\]

Instead of encoding all pairs uniformly, a CP-SAT model can encode:

- the orientation inside \(A\);
- arcs \(A\to B\);
- arcs from \(A\cup B\) to outside-signature classes;
- exact second-neighbor witnesses;
- minimum-degree constraints;
- non-Seymour inequalities for the root and selected local vertices.

The Sadhukhan–Sandeep–Sen work demonstrates that this local-obstruction approach is viable, though it becomes intricate already at degree seven.

## 4.4 Finite search by degree

The quoted \(\binom{\delta+1}{2}\) theorem is the closest thing to a finite parametrization:

> Fix \(\delta\). If a counterexample of minimum outdegree \(\delta\) exists, then a bounded-order one exists.

Thus a degree-by-degree exhaustive program can, in principle, settle one slice completely. It cannot settle the whole conjecture unless it also proves a global upper bound on the minimum outdegree of a counterexample.

## 4.5 Huang–Peng quadratic CSP

Huang and Peng show that a \(\mu\)-counterexample implies feasibility of a particular CSP in eleven real variables \(x_{ij}\), consisting of:

- neighborhood-size inequalities;
- nonnegativity constraints;
- minimum-degree constraints;
- one quadratic inequality \(F>0\).

For their \(\gamma=0.715538\ldots\), the CSP is infeasible. This is a one-way relaxation: a graph counterexample produces a CSP solution, but a CSP solution need not reconstruct a graph. At \(\mu=1\), the relaxation is not strong enough to settle the conjecture. ([arxiv.org](https://arxiv.org/html/2412.20234v1))

## 4.6 Tight-orientation matrix kernel

Guo, Kang and Zwaneveld define

\[
S_D(v,w)=
\begin{cases}
1,&w\in N^+(v),\\
-1,&w\in N^{++}(v),\\
0,&\text{otherwise}.
\end{cases}
\]

Then

\[
D\text{ is Seymour-tight}\iff S_D\mathbf1=0.
\]

More generally, if \(\mathbf x\in\mathbb Z_{\ge0}^n\) satisfies

\[
S_D\mathbf x=0,
\]

then replacing vertex \(i\) by a tight orientation of size \(x_i\) produces another tight orientation. This is a genuine integer-kernel/blow-up parametrization and suggests using Hilbert-basis or integer-kernel methods to classify tight modules. ([arxiv.org](https://arxiv.org/html/2603.29626))

## 4.7 Lexicographic products and minimal seeds

Tight orientations are closed under ordinary and generalized lexicographic products. Moreover, if \(C\) is a counterexample and \(T\) is tight, then both \(C[T]\) and \(T[C]\) are counterexamples. ([arxiv.org](https://arxiv.org/abs/2603.29626))

Therefore a smallest counterexample should be sought after eliminating obvious nontrivial tight-product decompositions. A good search representation is:

\[
\boxed{\text{strongly connected, vertex-minimal, modularly prime, fixed }\delta.}
\]

Raw large counterexamples would contain many artificial blow-up directions that do not help discover the seed.

## 4.8 Random-graph representation

For \(p>1/2\), the full conjecture is equivalent to a positive-probability assertion about every orientation of \(G(n,p)\). This is an interesting theoretical coordinate change but not currently an efficient finite search representation. ([arxiv.org](https://arxiv.org/abs/2403.02842))

## Best representation for a search

The best practical formulation is **not** raw enumeration of ternary adjacency matrices. It is:

1. fixed minimum outdegree \(d\), beginning with \(d=8\);
2. \(2d+3\le n\le\binom{d+1}{2}\);
3. a distinguished minimum-degree root \(v\);
4. explicit \(A=N^+(v)\), \(B=N^{++}(v)\);
5. local outside-signature classes;
6. strong-connectivity and modular-primality constraints;
7. incremental PB/SAT with independently checkable UNSAT certificates.

---

# 5. Near misses and hard cases

## 5.1 Seymour-tight orientations

Guo–Kang–Zwaneveld call an orientation **Seymour-tight** when

\[
|N^{++}(v)|=|N^+(v)|
\quad\text{for every }v.
\]

Known tight families include:

- every directed cycle;
- the \(k\)-th power of a directed \(n\)-cycle when \(2k<n\);
- regular tournaments;
- empty graphs and disjoint unions of tight components;
- ordinary and generalized lexicographic products of tight orientations. ([arxiv.org](https://arxiv.org/html/2603.29626))

For abelian Cayley orientations, these are completely classified as repeated lexicographic products of empty graphs, powers of directed cycles and regular tournaments. ([arxiv.org](https://arxiv.org/html/2603.29626))

These are not merely curiosities: they are exactly neutral directions along which a counterexample seed could be blown up.

## 5.2 Tight graphs are extremely diverse

Every oriented graph occurs as an induced subgraph of a strongly connected tight orientation. If a counterexample exists, every oriented graph also occurs as an induced subgraph of a strongly connected counterexample. ([arxiv.org](https://arxiv.org/html/2603.29626))

Consequences:

- local forbidden induced subgraphs cannot characterize all counterexamples;
- motif-based machine learning without global constraints is unlikely to be decisive;
- a counterexample can be made close to a regular tournament;
- search should focus on minimal seeds, not arbitrary large examples.

## 5.3 The degree-seven hard branch

The recent \(\delta=7\) proof needed machine assistance precisely in a highly constrained local configuration:

\[
|A|=7,\qquad |B|=6,\qquad |A_1|=2,
\]

with separate \(r=5\) and \(r=6\) obstruction models. This is the clearest published indication of where local counting starts to fail and where a degree-eight search should begin. ([arxiv.org](https://arxiv.org/html/2606.30588v1))

## 5.4 The \(p=1/2\) barrier

Sparse random underlying graphs are easy in the strong sense that every orientation works a.a.s. The point \(p=1/2\) is where the probabilistic reduction changes character, and \(p>1/2\) becomes equivalent to the full problem. Thus difficult examples need not be sparse; they may instead be dense but have missing edges in globally unstructured positions. ([arxiv.org](https://arxiv.org/abs/2403.02842))

## 5.5 False analogue when digons are allowed

The no-digons hypothesis is essential. In the complete bidirected digraph, every other vertex is already a first out-neighbor, so every exact second neighborhood is empty:

\[
|N^{++}(v)|=0<n-1=|N^+(v)|.
\]

Thus the unrestricted-digraph analogue is false for the simplest possible reason.

## 5.6 A withdrawn tight-classification conjecture

Halkiewicz’s later version conjectured that small strongly connected tight graphs had underlying graph either a cycle or a complete graph minus a matching. The paper was withdrawn after four independent researchers found counterexamples to that **classification conjecture**, not to Seymour’s conjecture itself. This is useful negative evidence: tight families are richer than the simplest cycle/near-complete models. ([arxiv.org](https://arxiv.org/abs/2601.21563))

---

# 6. Who is actively working on it?

Public activity during 2024–August 2026 includes:

| Researchers | Public work |
|---|---|
| Hao Huang, Fei Peng | Best constant factor \(0.715538\ldots\); quadratic CSP |
| Alberto Espuny Díaz, António Girão, Bertille Granet, Gal Kronenberg | Random graphs, minimum-degree reductions |
| Krystal Guo, Ross J. Kang, Gabriëlle Zwaneveld | Tight orientations, lexicographic products, Cayley/additive structure |
| Arpan Sadhukhan, R. B. Sandeep, Sagnik Sen | Minimum outdegree seven; OR-Tools CP-SAT |
| Jake Brukhman | Dense theorem \(n\le2\delta+2\), submitted August 12, 2026 |
| Haozhe Wang, Mei Lu | Degeneracy classes and near-tournaments |
| Moussa Daamouch, Salman Ghazal, Darine Al-Mniny | Tournaments with structured missing edges |
| Stanisław Halkiewicz | Small enumeration and tight-family computation; preprint withdrawn |
| Charles N. Glover | Claimed general proof, currently invalid/unaccepted |

The associated papers establish that this is an actively moving target in 2026. ([arxiv.org](https://arxiv.org/abs/2412.20234))

### Automated or AI-assisted efforts

I found:

- one reproducible **CP-SAT-assisted proof** for local degree-seven obstructions;
- one claimed brute-force Julia enumeration through \(n=7\);
- exploratory public code associated with that withdrawn enumeration.

I found **no disclosed LLM/AI-assisted proof or counterexample program**, no public whole-space SAT campaign at \(n\ge19\), and no announced institutional HPC enumeration with a larger certified range. This is only a statement about public records; private computations would not be discoverable.

---

# 7. Tractability call

## Verification complexity

Excellent. Given an adjacency matrix, a counterexample can be verified with bitsets in approximately \(O(n^3/w)\), or \(O(n^3)\) naively. There is no numerical instability and no difficult certificate.

## Raw search size

Terrible:

\[
\#\{\text{labeled oriented graphs on }n\text{ vertices}\}
=3^{\binom n2}.
\]

At the first live order,

\[
3^{\binom{19}{2}}=3^{171}\approx3.9\times10^{81}.
\]

At the upper end of the degree-eight finite slice,

\[
3^{\binom{36}{2}}=3^{630}\approx3.9\times10^{300}.
\]

Isomorphism reduction alone does not remotely make this enumerable.

## Why SAT may still work

The encoding itself is small, and the live \(n=19\) case has unusually sharp structure:

- \(\delta=8\) exactly;
- strongly connected;
- not a tournament;
- every vertex has strict negative margin;
- \(n>2\delta+2\);
- local root has only eight first and at most seven second neighbors.

A solver could find a counterexample quickly if one exists in that slice. The expensive outcome is an UNSAT proof, especially because of vertex-label symmetry and the many equivalent tight/blow-up structures.

## Recommended campaign

1. **Audit the two 2026 preprints first.**
2. Reproduce the degree-seven CP-SAT infeasibility computations.
3. Encode \(n=19,\delta=8\) in PB/SAT with proof logging.
4. Add strong connectivity, minimum-root and canonical-degree constraints.
5. Add modular decomposition/twin exclusions appropriate to a smallest seed.
6. Search incrementally through \(n=36\) for \(\delta=8\).
7. If the slice is UNSAT, move to \(\delta=9,\ 21\le n\le45\).
8. Store LRAT/DRAT or VeriPB certificates; an unverifiable solver log is not a durable mathematical result.

## Honest classification

**MARGINAL.**

The object is genuinely cheap to verify, the first live slice is concrete, and the recent degree-seven work shows that constraint programming can penetrate meaningful cases. But there is no reason currently known that the smallest counterexample, if one exists, must have \(\delta=8\) or remotely small order; the lack of a global upper bound on its minimum outdegree is the single biggest obstacle.

---

# Search coverage and limitations

I explicitly searched arXiv title/abstract records and recent indexed listings covering the last 24 months through **August 12, 2026**, using both American and British spellings of “neighborhood/neighbourhood,” “distance two,” “proof,” “counterexample,” “minimum outdegree,” and “Seymour-tight.” I also checked publisher metadata, recent reference lists, DOI pages, and the publicly linked computational record.

Limitations:

- Springer’s full Wang–Lu paper was paywalled; its abstract and references were accessible.
- Several Elsevier/Wiley pages exposed abstracts but not full text.
- I did not have closed MathSciNet, zbMATH, Scopus or Web of Science access.
- I did not execute the Halkiewicz Julia code or the Sadhukhan–Sandeep–Sen CP-SAT code.
- Some older Congressus Numerantium and journal papers have no readily recoverable DOI or open URL; I do not guess missing identifiers.
- No conclusion here covers work posted after August 13, 2026.

# Core bibliographic references

1. **David C. Fisher**, “Squaring a Tournament: A Proof of Dean’s Conjecture,” *Journal of Graph Theory* **23**(1), 43–48 (1996). arXiv: none found. DOI/open URL: not confirmed in accessible metadata. Bibliographic data reproduced in Wang–Lu. ([doi.org](https://doi.org/10.1007/S00373-026-03014-Y))  
2. **Frédéric Havet and Stéphan Thomassé**, “Median Orders of Tournaments: A Tool for the Second Neighborhood Problem and Sumner’s Conjecture,” *Journal of Graph Theory* **35**(4), 244–256 (2000). arXiv: none found. DOI not confirmed. ([doi.org](https://doi.org/10.1007/S00373-026-03014-Y))  
3. **Guantao Chen, Jian Shen and Raphael Yuster**, “Second Neighborhood via First Neighborhood in Digraphs,” *Annals of Combinatorics* **7**, 15–20 (2003). PDF: `https://math.haifa.ac.il/raphy/papers/seymconj.pdf`. DOI not confirmed. ([arxiv.org](https://arxiv.org/html/2412.20234v1))  
4. **Y. Kaneko and S. C. Locke**, “The Minimum Degree Approach for Paul Seymour’s Distance 2 Conjecture,” *Congressus Numerantium* **148**, 201–206 (2001). DOI: none located. ([doi.org](https://doi.org/10.1007/S00373-026-03014-Y))  
5. **D. Fidler and R. Yuster**, “Remarks on the Second Neighborhood Problem,” *Journal of Graph Theory* **55**(3), 208–220 (2007). DOI not confirmed. ([doi.org](https://doi.org/10.1007/S00373-026-03014-Y))  
6. **Tyler Seacrest**, “The Arc-Weighted Version of the Second Neighborhood Conjecture,” *Journal of Graph Theory* **78**, 219–228 (2015); arXiv:1212.1883; DOI `10.1002/jgt.21800`; `https://arxiv.org/abs/1212.1883`. ([onlinelibrary.wiley.com](https://onlinelibrary.wiley.com/doi/abs/10.1002/jgt.21800))  
7. **Fábio Botler, Phablo F. S. Moura and Tássio Naia**, “Seymour’s Second Neighborhood Conjecture for Orientations of (Pseudo)random Graphs,” *Discrete Mathematics* **346**(12), 113583 (2023); arXiv:2211.06540; DOI `10.1016/j.disc.2023.113583`; `https://arxiv.org/abs/2211.06540`. ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0012365X23002698))  
8. **Alberto Espuny Díaz, António Girão, Bertille Granet and Gal Kronenberg**, “Seymour’s Second Neighbourhood Conjecture: Random Graphs and Reductions,” *Random Structures & Algorithms* (online 2024/2025); arXiv:2403.02842; DOI `10.1002/rsa.21251`; `https://arxiv.org/abs/2403.02842`. ([arxiv.org](https://arxiv.org/abs/2403.02842))  
9. **Hao Huang and Fei Peng**, “An Improved Bound on Seymour’s Second Neighborhood Conjecture” (2024), arXiv:2412.20234; DOI `10.48550/arXiv.2412.20234`; `https://arxiv.org/abs/2412.20234`. ([arxiv.org](https://arxiv.org/abs/2412.20234))  
10. **Charles N. Glover**, “A Minimum Counterexample Proof of the Seymour Second Neighborhood Conjecture via the Graph Level Order,” latest v14, May 30, 2026; arXiv:2501.00614; DOI `10.48550/arXiv.2501.00614`; `https://arxiv.org/abs/2501.00614`. ([arxiv.org](https://arxiv.org/abs/2501.00614))  
11. **Krystal Guo, Ross J. Kang and Gabriëlle Zwaneveld**, “Seymour-Tight Orientations” (2026), arXiv:2603.29626; DOI `10.48550/arXiv.2603.29626`; `https://arxiv.org/abs/2603.29626`. ([arxiv.org](https://arxiv.org/abs/2603.29626))  
12. **Arpan Sadhukhan, R. B. Sandeep and Sagnik Sen**, “A Proof of Seymour’s Second Neighborhood Conjecture for Oriented Graphs with Minimum Out-Degree Equal to 7” (2026), arXiv:2606.30588; DOI `10.48550/arXiv.2606.30588`; `https://arxiv.org/abs/2606.30588`. ([arxiv.org](https://arxiv.org/abs/2606.30588))  
13. **Jake Brukhman**, “A Dense-Case Theorem for Seymour’s Second Neighborhood Conjecture” (August 12, 2026), arXiv:2608.11530; DOI `10.48550/arXiv.2608.11530`; `https://arxiv.org/abs/2608.11530`. ([arxiv.org](https://arxiv.org/abs/2608.11530))  
14. **Haozhe Wang and Mei Lu**, “Seymour’s Second Neighborhood Conjecture for Some Oriented Graphs,” *Graphs and Combinatorics* **42**, article 19 (2026); DOI `10.1007/s00373-026-03014-y`; `https://doi.org/10.1007/s00373-026-03014-y`. ([doi.org](https://doi.org/10.1007/S00373-026-03014-Y))  
15. **Stanisław M. S. Halkiewicz**, archived v1 “Seymour’s Second Neighbourhood Conjecture for Oriented Graphs of Order at Most Seven and Split-Twin Extensions”; current withdrawn title “Split-Twin Extensions Preserving Seymour Vertices,” arXiv:2601.21563; DOI `10.48550/arXiv.2601.21563`; `https://arxiv.org/abs/2601.21563`. ([arxiv.org](https://arxiv.org/abs/2601.21563v1))  
16. **Moussa Daamouch, Salman Ghazal and Darine Al-Mniny**, “About the Second Neighborhood Conjecture for Tournaments Missing Two Stars or Disjoint Paths,” *Contributions to Discrete Mathematics* **20**(2), 363–383 (2025); arXiv:2406.03635; `https://arxiv.org/abs/2406.03635`. ([arxiv.org](https://arxiv.org/abs/2406.03635))  
17. **S. Dara, M. C. Francis, D. Jacob and N. Narayanan**, “Extending Some Results on the Second Neighborhood Conjecture,” *Discrete Applied Mathematics* **311**, 1–17 (2022). DOI/arXiv not confirmed. ([doi.org](https://doi.org/10.1007/S00373-026-03014-Y))  
18. **Darine A. Mniny and Salman Ghazal**, “The Second Neighborhood Conjecture for Oriented Graphs Missing \(\{C_4,\overline C_4,S_3,\text{chair},\text{co-chair}\}\)-Free Graph,” *Australasian Journal of Combinatorics* **81**(1), 58–88 (2021). DOI not located. ([doi.org](https://doi.org/10.1007/S00373-026-03014-Y))  
19. **Salman Ghazal**, “The Second Neighborhood Conjecture for Oriented Graphs Missing Combs” (2016), arXiv:1602.08631; `https://arxiv.org/abs/1602.08631`. ([arxiv.org](https://arxiv.org/abs/1602.08631))  
20. **James Brantner, Greg Brockman, Bill Kay and Emma Snively**, “Contributions to Seymour’s Second Neighborhood Conjecture,” *Involve* **2**, 387–394 (2009); arXiv:0808.0946; DOI `10.2140/involve.2009.2.387`; `https://arxiv.org/abs/0808.0946`. ([arxiv.org](https://arxiv.org/abs/0808.0946))  
21. **Oleksiy Zelenskyi, Valentyna Darmosiuk and Illia Nalivayko**, “A Note on Possible Density and Diameter of Counterexamples to Seymour’s Second Neighborhood Conjecture,” *Opuscula Mathematica* **41**(4), 601–605 (2021). DOI not independently confirmed. ([arxiv.org](https://arxiv.org/pdf/2601.21563v1))  
22. **“A Note on the Second Neighborhood Problem for \(k\)-Anti-Transitive Digraphs with Large Girth,”** *Discrete Applied Mathematics* **389**, 301–307, issue dated August 15, 2026; DOI `10.1016/j.dam.2026.04.014`. The accessible index did not expose the author list, so I am not guessing it. ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0166218X26002337))

**VERDICT: OPEN | MARGINAL**

The exact conjecture remains open, and the best currently supportable search floor is \(n=19\), conditional on independently validating two very recent 2026 preprints. A counterexample is cheaply verifiable and the \(\delta=8,\ 19\le n\le36\) slice is a concrete SAT target, but the absence of any global bound on the minimum degree or order of a smallest seed is the central obstacle.