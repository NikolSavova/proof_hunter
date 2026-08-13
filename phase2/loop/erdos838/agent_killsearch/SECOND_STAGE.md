# Erdős 838: second-stage kill-search after the candidate \(1/2\) theorem

**Sweep date:** 2026-08-13.  The novelty searches below were run through
2026-08-12 publications/indexing, with a final check of the Erdős Problems
thread on 2026-08-13.  This is an agent report, not part of the proof draft.

## Bottom line

1. **No indexed or publicly searchable geometric source found the base-2
   upper coefficient \(1/2\)**, an equivalent natural-log coefficient
   \(1/(2\ln 2)=0.721347\ldots\), or the exact cap/cup/convex enumerator used
   in `proof_blowup_half.md`. Literal formula searches and concept searches
   both came back negative. This is encouraging, but of course is not a
   proof of novelty.

2. **The generic blow-up operation is definitely prior art.** Han,
   Kohayakawa, Sales and Stagni (SODA 2019) define \(C\)-blow-ups of order
   types, construct them in small balls, introduce \(B\otimes C\), and
   explicitly iterate the product. Baek and Balko (SoCG 2025; JCTA 2026)
   use an even closer almost-vertical cluster blow-up for the
   Erdős--Szekeres problem. Therefore a paper must not claim that replacing
   every point by a tiny order-type cluster, or iterating this operation, is
   new. The defensible novelty claim is narrower: the **directionally
   prescribed two-in-one-block signs, exact substitution identities for
   total caps/cups/convex subsets, and their asymptotic optimization to
   \(1/2\)**.

3. The closest numerical precedent is the **graph analogue**, not planar
   geometry. Székely's 1984 random-graph upper bound is
   \(\exp((0.7214+o(1))(\ln n)^2)\), i.e. base-2 coefficient \(1/2\).
   Feige--Kenyon--Kogan (2020) proved a base-2 \(1/4\) lower coefficient for
   the total number of homogeneous graph subsets. Thus, after the candidate
   geometric theorem, both graph and convex-position problems have the same
   visible base-2 window \([1/4,1/2]\). This is strong conceptual context and
   an obvious referee comparison, but it does not kill the geometric result.

4. The most actionable lower-bound transfer is a **weighted endpoint-state
   or good-sequence lemma with a factorial fibre bound**. Existing graph
   proofs count nested-neighbourhood histories and divide by at most \(q!\).
   Existing monotone-path/signotope proofs inject vertices into down-sets of
   endpoint path-length states. A geometric synthesis would weight endpoint
   states by path multiplicity and try to map histories to a cap--cup pair
   (equivalently a convex subset) with only \(2^{O(q\log q)}\) overcount.
   There is a real obstruction: graph histories constrain adjacency to
   *every* earlier selected vertex, whereas a cap/cup extension only records
   the latest endpoint pair.

5. Abstract convex-geometry machinery did not supply a hidden quantitative
   theorem. The desired objects are **independent sets**, while much of the
   literature counts **free sets** (closed and independent, hence empty
   convex polygons). Copoint graphs encode independent sets via cliques, but
   non-unique representations and the lack of a useful interpretation for
   independent sets of the copoint graph block a direct Ramsey-multiplicity
   transfer.

## 1. Prior art on point-order-type blow-ups

### 1.1 Han--Kohayakawa--Sales--Stagni: generic iterated blow-ups

J. Han, Y. Kohayakawa, M. T. Sales and H. Stagni,
“Extremal and probabilistic results for order types,” SODA 2019,
pp. 426--435, [publisher/DOI](https://epubs.siam.org/doi/10.1137/1.9781611975482.27),
[author-uploaded full text](https://www.researchgate.net/publication/330100547_Extremal_and_probabilistic_results_for_order_types).

Their Section 3.3 makes the collision precise.

* A \(k\)-blow-up of an \(n\)-point configuration \(B\) is partitioned into
  \(n\) clusters of size \(k\), with every transversal isomorphic to \(B\).
* A \(C\)-blow-up additionally requires every cluster to be isomorphic to
  \(C\).
* Existence is obtained by putting a copy of \(C\) in a sufficiently small
  open ball about every point of \(B\).
* They denote the set of all such order types by \(B\otimes C\) and extend
  the notation explicitly to \(\bigotimes_{i=1}^d X_i\).

This product is intentionally non-unique. It prescribes orientations for
triples within a cluster and triples meeting three different clusters, but
does **not** prescribe the mixed triples having two points in one cluster.
Consequently it does not yield the four sign rules or any of the exact
enumerator recurrences in the candidate proof. Their applications are
order-type density, hereditary properties, grid realization and
supersaturation, not counting all convex-position subsets.

**Novelty risk: high for terminology/operation, low for the enumerator.**
Call the construction a special or directional realization of a standard
order-type blow-up; do not present “iterated lexicographic blow-up” alone as
the invention.

### 1.2 Baek--Balko: almost-vertical Erdős--Szekeres blow-ups

J. Baek and M. Balko, “The Erdős--Szekeres Conjecture Revisited,” SoCG
2025, [primary conference PDF](https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/LIPIcs.SoCG.2025.13/LIPIcs.SoCG.2025.13.pdf),
later JCTA 222 (2026),
[journal DOI](https://doi.org/10.1016/j.jcta.2026.106195).

They replace skeleton points by rotated, **almost-vertical** copies of
Pascal-type cap/cup configurations. Their general \((X,Y)\)-blow-up has
endpoint-specific constraints

\[
 x_i+y_i\le k-1,\qquad x_i+y_j\le k-1-s_{i,j}\quad(i<j),
\]

where \(s_{i,j}\) is the maximum relevant macro convex-chain size; Lemma 14
then gives a construction with no \(k\)-gon and an exact formula for its
number of points. They show that all previously known \(2^{k-2}\)-point
constructions are special cases.

This is geometrically closer to `proof_blowup_half.md` than the general SODA
product, but it optimizes **construction size under a forbidden largest
convex subset**, not the total number of convex subsets, and it does not
state an iteration enumerator.

**Novelty risk: high for “almost-vertical clusters”; no located collision
with the total-count recurrence or coefficient \(1/2\).**

### 1.3 Negative exact-formula search

No relevant result was returned by combinations of the following strings
across Google/web indexing, arXiv, Crossref/OpenAlex-style metadata, the
Erdős Problems page/thread, and citation trails of the papers above:

* `"convex subsets" "1/2" "log_2"`,
  `"convex position" "1/2+o(1)"`;
* `n^{(1/2+o(1)) log_2 n}` together with convex polygon/point-set terms;
* `"1/(2 ln 2)" convex subsets`, `0.721347 convex subsets`,
  `0.639326 convex subsets`;
* `order type blow-up convex subsets count`, `iterated blow-up convex
  polygons`, and `lexicographic product signotope convex position`.

The 2026 Erdős Problems discussion located the public base-2 lower bound
\(1/4\), but the indexed thread contained no \(1/2\) upper claim or blow-up
enumerator:
[Problem/thread 838](https://www.erdosproblems.com/forum/thread/838).

## 2. Graph total-homogeneous-subgraph methods

### 2.1 Exact normalization and the numerical precedent

L. A. Székely, “On the number of homogeneous subgraphs of a graph,”
Combinatorica 4 (1984), 363--372,
[DOI/abstract](https://doi.org/10.1007/BF02579149), states

\[
 \exp(0.7214(\ln n)^2)\ \gtrsim\ G(n)\ \gtrsim\
 \exp(0.2275(\ln n)^2),
\]

where \(G(n)\) is the minimum total number of complete plus independent
subgraphs. The upper number \(0.7214\) is the rounded random-graph constant

\[
 \frac1{2\ln 2}=0.7213475204\ldots .
\]

For the normalization used in `proof_blowup_half.md`,

\[
 \frac{\log_2 \exp(c(\ln n)^2)}{(\log_2 n)^2}=c\ln2.
\]

Thus Székely's graph upper coefficient is exactly \(1/2\) in base 2; his
displayed lower coefficient \(0.2275\) becomes approximately \(0.1577\).

U. Feige, A. Kenyon and S. Kogan, “On the Profile of Multiplicities of
Complete Subgraphs,” SIAM J. Discrete Math. 34 (2020), 950--971,
[primary arXiv text](https://arxiv.org/abs/1703.09682), improve the graph
lower bound: for \(n=2^t\), every red/blue complete graph contains

\[
 2^{(1/4-o(1))t^2}
\]

monochromatic complete subgraphs of one size \(r\) with
\(0.3t<r<0.7t\). Random graphs have at most
\(2^{(1/2+o(1))t^2}\) in total.

So the graph window is exactly

\[
 2^{(1/4-o(1))(\log_2 n)^2}
 \ \le\ G(n)\ \le\
 2^{(1/2+o(1))(\log_2 n)^2}.
\]

### 2.2 Ramsey trees: the transferable counting skeleton

The Feige--Kenyon--Kogan proof introduces General, Biased and Restricted
Ramsey Trees. At a node carrying vertex \(v\) and a “bag” \(B\), the two
children restrict the next bag to the red or blue neighborhood of \(v\).
Two exact fibre estimates are the useful part.

* Their Lemma 2.1: if level \(l\) of a General Ramsey Tree has at least
  \(m\) nodes, the graph has at least \(m/(l+1)!\) homogeneous subgraphs.
  The factorial is the maximum number of path orders representing the same
  vertex set.
* Their Lemma 2.9: if \(S\) is a set of same-colour levels in a Restricted
  Ramsey Tree whose last level is \(l\), and \(s(i)\) is the common bag size
  at level \(i\), then there are at least

  \[
    \frac{1}{2^{l+1}(l+1)!}\prod_{i\in S}s(i-1)
  \]

  monochromatic cliques of size \(|S|\).

**Candidate geometric lemma.** Build a tree whose states are ordered
endpoint pairs and whose branches retain points extending the current cap
or cup. Count full histories from the successive bag sizes, then prove that
the map from histories to cap/cup chains, or to a shared-endpoint cap--cup
pair, has fibre \(2^{O(q\log q)}\). Such a loss is negligible at the
\((\log n)^2\) scale.

**Why the graph proof does not transfer verbatim.** In a Ramsey tree, a
later bag is simultaneously monochromatically adjacent to every earlier
chosen vertex of the appropriate colour. A cap/cup extension only certifies
an orientation relative to the current last two vertices. Picking
nonconsecutive same-colour levels need not form a monotone tight path.
Any valid geometric tree has to use the signotope four-point axiom, or carry
enough endpoint-chain state to repair this loss of memory.

### 2.3 A sharper 2025 product-count formulation

D. Bal, J. Cutler and L. Pebody, “On the Number of Monochromatic Cliques in
a Graph,” EJC 32(3) (2025), #P3.16,
[primary PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i3p16/pdf/),
[DOI](https://doi.org/10.37236/13158), prove

\[
 i(G)k(G)\ge n^{(1/2+o(1))\log_2 n},
 \qquad i(G)k(G)\le(n+1)2^n.
\]

The lower proof packages the Ramsey-tree idea particularly cleanly. For an
\(r\)-edge-colouring, a sequence \((v_1,\ldots,v_q)\) is *good* when for
each \(i\), all later vertices lie in one monochromatic neighborhood of
\(v_i\). If

\[
 a_1=n,\qquad a_{j+1}=\left\lceil\frac{a_j-1}{r}\right\rceil,
\]

then their proof of Theorem 16 gives

\[
 \prod_{j=1}^q a_j
 \ \le\ |\mathcal X(G,q)|\ \le\
 q!\prod_{c=1}^r k(G_c).
\]

With \(r^m\le n<r^{m+1}\) and \(q=m\), this yields

\[
 \prod_{c=1}^r k(G_c)
 \ge r^{m^2/2-O(m\log m)}.
\]

This suggests a precise target rather than a vague analogy:

> Define a geometric good history with a multiplicative lower count from
> nested extension bags; map each history to one cap and one cup (preferably
> sharing endpoints); and prove a \(q!\,2^{O(q)}\) fibre bound.

For \(r=2\), an AM--GM step halves the product exponent and recovers the
base-2 sum coefficient \(1/4\). To improve the existing geometric lower
constant, extra planar/signotope constraints would have to make either the
history count larger or the fibre smaller in a way visible at order
\(q^2\).

Their upper-product proof also uses vertex compression. Each compression
does not decrease the independent-set count in the graph or its complement;
iteration reduces to threshold graphs with nested neighborhoods. A
realizability-preserving order-type compression that monotonicizes endpoint
states would be powerful, but no such operation was found. Arbitrary graph
compression need not preserve rank-3 realizability or signotope axioms.

## 3. Signotopes and weighted cap/cup path states

The Baek--Balko paper is the closest established bridge. With triples
ordered by increasing \(x\)-coordinate, red/blue monotone tight paths are
caps/cups. It records the exact ordered Ramsey number

\[
 R(P_a^3,P_u^3)={a+u-4\choose a-2}+1
\]

(their Theorem 5), and a more general exact split-gon threshold

\[
 C_{\rm split}(a,u,k)
 =1+\sum_{i=k-a+2}^{u}{k-2\choose i-2}.
\]

The proof labels every endpoint pair \(p<q\) by

\[
 D(p,q)=(r(p,q)-1,b(p,q)-1),
\]

where \(r,b\) are the longest red/blue monotone paths ending at \(p,q\).
It sends a vertex \(q\) to the down-set generated by all \(D(p,q)\), and
proves that the vertex-to-down-set map is injective. This is the most
natural finite-state framework in which to attempt a weighted theorem.

For a rank-3 signotope, every four ordered vertices \(a<b<c<d\) have at
most one sign change in

\[
 (\chi(a,b,c),\chi(a,b,d),\chi(a,c,d),\chi(b,c,d)).
\]

In particular, equality of the first and last signs forces all four signs
equal. Hence a monochromatic tight path in a signotope is a genuinely
monochromatic vertex set (a cap or cup), and a weak polygon is strong.

### Actionable weighted-state questions

1. Replace the longest-path pair (D(p,q)) by the two path partition
   functions

   \[
   C(p,q)=\#\{\text{caps ending at }p,q\},\qquad
   U(p,q)=\#\{\text{cups ending at }p,q\}.
   \]

   Seek a weighted down-set injection, log-supermodularity inequality, or
   entropy inequality forcing a lower bound on
   \(\sum_{p<q}C(p,q)U(p,q)\), the exact endpoint expression for total
   convex subsets.

2. Prove a weighted analogue of Baek--Balko's vertex injection: many
   endpoint histories cannot collapse to the same pair of path partition
   functions unless the four-point axiom forces additional paths. Even a
   (2^{O(q\log q)}) multiplicity theorem would match the precision of the
   Ramsey-tree method.

3. Try a two-sided history grown outward from a fixed endpoint pair. This
   avoids the main failure of resetting the latest pair and may output a cap
   on one side and a cup on the other with the endpoints already shared.

Searches for `signotope path multiplicity`, `number of monotone tight paths
signotope`, `cups caps supersaturation`, and `weighted cups caps` found
threshold and saturation papers, but no total-copy theorem. Relevant
threshold background includes Fox--Pach--Sudakov--Suk,
[J. London Math. Soc. 2012](https://doi.org/10.1112/plms/pds018), and the
exact monotone-path/down-set work cited by Baek--Balko; neither counts total
paths in a fixed coloring.

An adjacent two-uniform supersaturation result is W. Samotij and B. Sudakov,
“On the number of monotone sequences,” JCTB 115 (2015), 132--163,
[primary PDF](https://people.math.ethz.ch/~sudakovb/monotone-sequences.pdf),
[DOI](https://doi.org/10.1016/j.jctb.2015.05.008). It determines the minimum
number of length-\(k+1\) monotone subsequences near the \(k^2\) threshold.
This may inform stability/weighting, but it is a permutation (rank-2)
problem and does not solve the shared-endpoint cap--cup count.

## 4. Convex geometries, copoints, and why “free set” is a trap

For a planar point set \(P\),

\[
 \operatorname{cl}(A)=P\cap\operatorname{conv}(A)
\]

defines a finite convex geometry. A subset is independent exactly when all
of its points are extreme, hence exactly when it is in convex position.

K. Kashiwabara and M. Nakamura,
“Brylawski's Decomposition of NBC Complexes of Abstract Convex Geometries
and Their Associated Algebras,” EuroComb 2005,
[primary PDF](https://dmtcs.episciences.org/3412/pdf), distinguish:

* independent: \(\operatorname{Ex}(A)=A\);
* free: independent **and closed**.

They prove that the free complex is the NBC complex and obtain
Whitney--Rota/Möbius identities. For point sets, free sets are empty convex
polygons. They are only a subclass of the subsets counted by Erdős 838.
Alternating free-set identities do not give a positive lower bound for all
independent sets.

### Copoint graph route

W. Morris, “Coloring copoints of a planar point set,” Discrete Applied
Mathematics 154 (2006), 1742--1752,
[author PDF](https://math.gmu.edu/~wmorris/copointsx.pdf),
[DOI](https://doi.org/10.1016/j.dam.2006.02.007), associates to an
\(n\)-point set a graph with fewer than \(n^2\) vertices. Its vertices are
copoints (maximal closed sets missing one attached point), and cliques
correspond to convexly independent subsets.

J. Beagley, “Properties of the Copoint Graph of Convex Geometries,”
Congressus Numerantium 217 (2013),
[author-uploaded text](https://www.researchgate.net/publication/260933833_Properties_of_the_Copoint_Graph_of_Convex_Geometries),
states the correspondence explicitly: \(A\subseteq P\) is independent iff
there exists a clique of copoints whose distinct attachments are the
elements of \(A\).

This is tempting but currently not a counting reduction.

* A single independent set can have multiple copoint-clique
  representations; no subexponential fibre bound was found.
* Feige--Kenyon--Kogan counts **cliques plus independent sets** of the
  copoint graph. Only the cliques have the desired geometric meaning.
* Morris's chromatic-number theorem and the low chromatic number of the
  classical Erdős--Szekeres examples concern largest cliques/coloring, not
  total clique multiplicity.

An actionable subproblem is therefore: choose a canonical copoint attached
to each vertex of every independent set and bound how many copoint cliques
have the same attachment set. Without such a bound, applying graph Ramsey
multiplicity to the \(<n^2\)-vertex copoint graph is invalid.

No abstract convex-geometry theorem was found that forces
\(\exp(c(\log n)^2)\) independent sets under planar realizability. The
anti-exchange axiom alone is substantially weaker than the rank-3
orientation/signotope constraints used in all effective point-set bounds.

## 5. Adjacent exact polygon-count identities

C. Huemer, D. Oliveros, P. Pérez-Lantero, F. Torra and
B. Vogtenhuber, “On Weighted Sums of Numbers of Convex Polygons in Point
Sets,” DCG 68 (2022), 448--476,
[open primary article](https://link.springer.com/article/10.1007/s00454-022-00395-8),
[DOI](https://doi.org/10.1007/s00454-022-00395-8), let \(X_{k,\ell}(P)\)
be the number of convex \(k\)-gons containing exactly \(\ell\) other points
of \(P\). They prove, among other universal identities,

\[
 \sum_{k=3}^{n}\sum_{\ell=0}^{n-3}2^\ell X_{k,\ell}(P)
 =2^n-\frac{n^2}{2}-\frac n2-1
\]

and, for every fixed \(3\le m\le n\),

\[
 \sum_{k=3}^{m}\sum_{\ell=m-k}^{n-k}
 {\ell\choose m-k}X_{k,\ell}(P)={n\choose m}.
\]

This is important nearby total-count prior art and should be cited if a
paper discusses polygon enumerators broadly. It does not determine the
unweighted sum \(\sum X_{k,\ell}\): the weight \(2^\ell\) can be carried by
polygons enclosing many points. No blow-up recurrence or log-squared
constant appears. The identities are useful as independent checks for
finite enumeration code.

## 6. A direct but weak block-product lower bound

The positive-fraction literature gives an independent sanity-check lower
bound, though not a competitive one. D. Conlon, J. Fox, X. He, D. Mubayi,
A. Suk and J. Verstraëte, “Big line or big convex polygon,” 2024/2025,
[primary PDF](https://homepages.math.uic.edu/~mubayi/papers/BigLine.pdf),
[arXiv](https://arxiv.org/abs/2405.03455), prove the following explicit
version (Theorem 3.1): if \(P\) has \(N>C\ell 2^{32k}\) points and no
\(\ell\) collinear points, there are \(k-1\) disjoint regions containing
sets \(P_i\) of size at least \(N/2^{32k}\), and every transversal
\(p_i\in P_i\) is in convex position.

For general position set \(\ell=3\), write \(L=\log_2N\), and take
\(k=\lfloor L/64\rfloor\). Distinct transversals give distinct convex
subsets, so directly

\[
 f(N)\ge
 \left(\frac{N}{2^{32k}}\right)^{k-1}
 =2^{(1/128-o(1))L^2}.
\]

This is far below the known \(1/4\) lower coefficient on the Erdős Problems
thread, but it is a clean geometric block-counting certificate and a useful
test case for any proposed weighted-clustering argument. Earlier
positive-fraction constants are also too weak for improvement: for example,
Pór--Valtr's convex-body form gives a cluster fraction only
\(2^{-37.8k-o(k)}\).

## 7. Base-normalization table

Let \(L=\log_2 n\). Then

| statement | base-2 form | natural-log coefficient |
|---|---:|---:|
| candidate convex upper | \(2^{(1/2+o(1))L^2}\) | \(1/(2\ln2)=0.7213475204\ldots\) |
| convex/thread lower | \(2^{(1/4-o(1))L^2}\) | \(1/(4\ln2)=0.3606737602\ldots\) |
| FKK graph lower | \(2^{(1/4-o(1))L^2}\) | \(1/(4\ln2)\) |
| random-graph/Székely upper | \(2^{(1/2+o(1))L^2}\) | \(1/(2\ln2)\) |
| explicit positive-fraction block bound above | \(2^{(1/128-o(1))L^2}\) | \(1/(128\ln2)\) |

Do not mix the two common displays:

\[
 2^{\kappa(\log_2n)^2}
 =n^{\kappa\log_2n}
 =\exp\!\left(\frac{\kappa}{\ln2}(\ln n)^2\right).
\]

## 8. Recommended claims and next checks

### Safe wording now

> We use a particular directional realization of the standard order-type
> blow-up. Unlike the general blow-up product, its mixed triple orientations
> are fixed, which permits exact substitution formulas for the total cap,
> cup and convex-subset enumerators. We are not aware of a previous use of
> these formulas, or of the resulting base-2 \(1/2\) upper coefficient for
> Erdős problem 838.

### Claims to avoid

* “We introduce iterated blow-ups of point order types.”
* “Almost-vertical cluster replacement is new.”
* “The constant \(1/2\) has no precedent.” It is the classical random-graph
  coefficient; say no **geometric** precedent was located.
* Calling every convex-position subset a “free set” in the convex-geometry
  sense.

### Highest-value follow-ups

1. Have a human/MathSciNet reviewer check citations **to** Han et al. 2019,
   Morris 2006, and Baek--Balko 2025/2026 for unpublished enumeration
   variants that keyword search may miss.
2. State and attack a formal weighted endpoint-history lemma with an
   explicit fibre target \(2^{O(q\log q)}\); test it exhaustively on small
   realizable order types and on abstract signotopes to locate the exact
   realizability input.
3. Test whether a canonical copoint choice has polynomial or factorial
   multiplicity on small order types. A single superfactorial family would
   kill the copoint-graph route quickly.
4. Cite the Han and Baek--Balko blow-ups proactively in any draft. This
   turns the principal prior-art collision into a clean distinction rather
   than a referee surprise.

## Novelty verdict

**Defensible but qualified.** The focused second-stage search found strong
prior art for generic and almost-vertical iterated cluster blow-ups, and an
exact numerical \(1/2\) analogue in graph Ramsey multiplicity. It found no
published exact total-count recurrence for convex subsets under such a
blow-up and no geometric base-2 \(1/2\) upper theorem. Subject to a
MathSciNet/full-citation-graph check, the likely publishable novelty is the
special mixed-orientation composition lemma plus its exact enumerator and
the optimization to \(1/2\), not the existence of a blow-up construction.
