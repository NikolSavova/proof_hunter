# Prior-art sweep — kaplansky (gpt-5.6-sol, effort=max, 2026-08-13 08:33)

> Counterexample-shaped target, selected after the Jacobian conjecture
> counterexample (Alpoge/Fable 5, 2026-07-20). Sweep asks BOTH whether the
> problem is already resolved AND where counterexample search is already dead.

# Executive finding

## 1. STATUS as of August 13, 2026: **OPEN**

I found **no proof and no torsion-free counterexample** to the Kaplansky zero-divisor conjecture.

More importantly for this project:

> **Do not search in \(P\).**  
> The Promislow/Hantzsche–Wendt group \(P\) satisfies the zero-divisor conjecture over **every field**. In particular, \(\mathbb F_2[P]\) is a domain, so zero divisors of **every finite support size** are ruled out—not merely up to some computational bound.

Indeed, \(P\) is torsion-free virtually abelian, hence polycyclic-by-finite and elementary amenable. Characteristic-zero results of Brown/Farkas–Snider and Cliff’s positive-characteristic theorem cover it; Gardam explicitly uses the fact that \(P\) satisfies the zero-divisor conjecture in his proof. The 2025 Garg–Mineyev paper likewise states directly that \(P\) satisfies it. ([gilesgardam.com](https://www.gilesgardam.com/papers/unit-conjecture-counterexamplev3.pdf))

The same applies to **every torsion-free crystallographic/Bieberbach group**: it is virtually \(\mathbb Z^n\), hence zero-divisor-dead over every field. Thus the crystallographic aspect of Gardam’s precedent does **not** transfer to this search.

---

## Axis audit

I separately checked:

1. **Global zero-divisor conjecture:** all fields, all torsion-free groups.
2. **Fixed case \(\mathbb F_2[P]\):** completely settled positively.
3. **Related unit conjecture:** false, but logically distinct.
4. **Idempotent conjecture:** still open globally, although settled for many classes.
5. **General support bounds** versus bounds in the **special Garg–Mineyev CAT(0)/taiko ansatz**.
6. Ordinary **Baum–Connes/Farrell–Jones** versus the stronger **Atiyah/division-ring** hypothesis.

I did **not** conflate “the unit conjecture fails for \(P\)” with “the zero-divisor conjecture might fail for \(P\).” In fact the latter is impossible.

---

## Recent-arXiv check

I explicitly searched arXiv, newest first, for both `"Kaplansky Zero Divisor"` and `"zero divisor conjecture"`, including the period **August 13, 2024–August 13, 2026**. The recent relevant results were:

- **Moe Tabei, July 20, 2026:** computational non-unique-product minima in \(P\), not a zero divisor. ([arxiv.org](https://arxiv.org/abs/2607.18346))
- **Sam P. Fisher–Andrew Ng, June 17, 2026:** new finite-index classes satisfying the zero-divisor conjecture, not a global resolution. ([arxiv.org](https://arxiv.org/abs/2606.19606))
- **Dietrich–Lee–Nies–Vinyals, March 2026:** computational work on units and unique products, not zero divisors. ([arxiv.org](https://arxiv.org/abs/2603.22640))
- **Garg–Mineyev, revised September 8, 2025:** a restricted combinatorial/CAT(0) search, explicitly saying the conjecture remains open. ([arxiv.org](https://arxiv.org/abs/2501.07646))
- **Fisher–Sánchez-Peralta, published 2026:** says the conjecture is “still wide open” while proving large new classes. ([ems.press](https://ems.press/content/serial-article-files/52395))

The exact arXiv search result pages are themselves useful evidence of coverage. ([arxiv.org](https://arxiv.org/search/?abstracts=show&order=-announced_date_first&query=%22Kaplansky+Zero+Divisor%22&searchtype=all&size=200))

---

# Related conjectures and the post-Gardam work

The implication chain for each individual group ring is

\[
\text{unit conjecture}\Longrightarrow
\text{zero-divisor conjecture}\Longrightarrow
\text{idempotent conjecture}.
\]

The failure of the first statement supplies no implication in the reverse direction. ([arxiv.org](https://arxiv.org/abs/2102.11818))

### Unit-conjecture chronology

- **Giles Gardam, 2021:** explicit nontrivial unit of support \(21\) in \(\mathbb F_2[P]\). Published in *Annals of Mathematics*. ([arxiv.org](https://arxiv.org/abs/2102.11818))
- **Alan G. Murray, 2021:** counterexamples in every prime characteristic. Hence, for every positive characteristic, there is a field/group-ring counterexample to the unit conjecture. ([arxiv.org](https://arxiv.org/abs/2106.02147))
- **Giles Gardam, 2023:** characteristic-zero counterexample over a complex group ring. ([arxiv.org](https://arxiv.org/abs/2312.05240))
- **Dietrich–Lee–Nies–Vinyals, 2026:** further computational classification of certain units in \(\mathbb F_2[P]\) and work on separating unique-product and trivial-unit properties. ([arxiv.org](https://arxiv.org/abs/2603.22640))

These results now make the unit conjecture false in every characteristic in the existence sense. They do **not** produce, suggest, or leave open zero divisors in \(\mathbb F_2[P]\).

### Direct answer about \(P\)

- Nontrivial units in \(\mathbb F_2[P]\): **yes**.
- Nontrivial zero divisors in \(\mathbb F_2[P]\): **no**.
- Nontrivial idempotents in \(\mathbb F_2[P]\): **no**, since it is a domain.
- Smallest zero-divisor support ruled out in \(\mathbb F_2[P]\): **all support sizes are ruled out**.

---

# 2. WHERE COUNTEREXAMPLE SEARCH IS ALREADY DEAD

## A. Entire group classes

| Class of torsion-free groups | Zero-divisor status | Field scope | Comments |
|---|---:|---:|---|
| One-sided orderable, hence left-/right-/bi-orderable | **Proved** | Any domain coefficients | Leading-term argument; one-sided orderability suffices. ([mathdept.byu.edu](https://mathdept.byu.edu/~pace/KaplanskyConjecture_web.pdf)) |
| Unique-product groups | **Proved** | Any domain | A uniquely represented product cannot have its nonzero coefficient cancelled. Cohen’s theorem is the standard reference. ([arxiv.org](https://arxiv.org/html/2501.07646v2)) |
| Torsion-free elementary amenable groups | **Proved** | Every field; stronger skew-field versions exist | Kropholler–Linnell–Moody. ([arxiv.org](https://arxiv.org/abs/2102.11818)) |
| Torsion-free polycyclic-by-finite groups | **Proved** | Every field | Characteristic zero: Brown/Farkas–Snider; positive characteristic: Cliff. ([cambridge.org](https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/zero-divisors-and-idempotents-in-group-rings/CA75D92676C7DF45DDC06553A7E637A8)) |
| Torsion-free virtually abelian/crystallographic groups | **Proved** | Every field | Subclass of the preceding rows. This kills \(P\) and every similar crystallographic candidate. |
| Residually torsion-free nilpotent groups | **Proved** | Any domain | Such groups are bi-orderable via their torsion-free nilpotent quotients. |
| Residually torsion-free elementary amenable groups | **Proved** | Every field | Standard residual consequence of the Kropholler–Linnell–Moody embedding result. ([mathoverflow.net](https://mathoverflow.net/questions/79559/what-is-the-current-status-of-the-kaplansky-zero-divisor-conjecture-for-group-ri)) |
| Torsion-free groups satisfying the strong Atiyah conjecture | **Proved over \(\mathbb C\)** | \(\mathbb C\), or the corresponding coefficient field for which strong Atiyah is known | The division closure becomes a skew field. ([ems.press](https://ems.press/content/serial-article-files/52395)) |
| Torsion-free one-relator groups | **Proved** | All division-ring coefficients | Lewin–Lewin division-ring embedding; reviewed and strengthened by Fisher–Sánchez-Peralta. ([ems.press](https://ems.press/content/serial-article-files/52395)) |
| Torsion-free virtually compact special groups | **Proved** | All division-ring coefficients | Fisher–Sánchez-Peralta. This covers many—but not all—hyperbolic groups. ([ems.press](https://ems.press/content/serial-article-files/52395)) |
| Finitely generated torsion-free 3-manifold groups | **Proved** | All division-ring coefficients | Fisher–Sánchez-Peralta, extending the earlier complex-coefficient result of Kielak–Linton. ([ems.press](https://ems.press/content/serial-article-files/52395)) |
| Certain finite-index subgroups of \(\operatorname{Out}(G)\), for \(G\) a RAAG/free/surface group | **Proved** | Every field | Fisher–Ng, 2026. ([arxiv.org](https://arxiv.org/abs/2606.19606)) |

### Where \(P\) sits

\(P\) is covered several times over:

- torsion-free virtually abelian;
- polycyclic-by-finite;
- elementary amenable;
- virtually compact special, since it has finite-index subgroup \(\mathbb Z^3\);
- a torsion-free flat 3-manifold group.

It is **not** unique-product or one-sided orderable, but those failures are irrelevant because the stronger domain theorems above apply.

---

## B. Baum–Connes and Farrell–Jones: the commonly confused axis

Ordinary Baum–Connes or Farrell–Jones is **not presently a general zero-divisor theorem**.

What they yield in the present context is the **idempotent conjecture**, particularly over \(\mathbb C\). The zero-divisor implication instead comes from the **strong Atiyah conjecture** or an actual division-ring embedding. Gardam makes precisely this distinction and also notes that \(P\) satisfies Farrell–Jones even though its unit conjecture fails. ([arxiv.org](https://arxiv.org/abs/2102.11818))

Therefore:

- “\(G\) satisfies Baum–Connes/Farrell–Jones”  
  does **not** close the zero-divisor axis by itself.
- “\(G\) satisfies strong Atiyah”  
  closes it over the relevant characteristic-zero coefficient field.

This distinction matters especially for general hyperbolic groups.

---

## C. Hyperbolic and CAT(0) groups

- **All torsion-free hyperbolic groups:** still **open** as a class.
- **Hyperbolic virtually compact special groups:** proved, all coefficient division rings.
- **Various small-cancellation/Linnell-class groups:** proved, often at least over \(\mathbb C\).
- **All torsion-free CAT(0) groups:** still **open**.
- The Garg–Mineyev paper does **not** prove the conjecture for all CAT(0) groups; it excludes a special family built from oriented product structures satisfying their conditions \(\mathsf T_1-\mathsf T_4\). ([arxiv.org](https://arxiv.org/html/2501.07646v2))

Thus a theorem-live search should focus on a torsion-free non-UP hyperbolic/CAT(0) group that is **not** already virtually special, elementary amenable, one-relator, strong-Atiyah, or otherwise division-ring embeddable.

---

## D. General support bounds

Let

\[
m=|\operatorname{supp}\alpha|,\qquad
n=|\operatorname{supp}\beta|,
\qquad \alpha\beta=0.
\]

### Universal non-UP lower bound

The supports \(A,B\) cannot have a uniquely represented element in \(AB\). Nielsen–Soelberg computed:

\[
|A|+|B|\ge 16,
\]

and this is sharp at the level of non-unique products: there are torsion-free examples with \(|A|=|B|=8\). These examples are not zero divisors. ([mathdept.byu.edu](https://mathdept.byu.edu/~pace/KaplanskyConjecture_web.pdf))

**Do not search total support below \(16\).**

For square-zero elements, \(\alpha^2=0\), one gets

\[
|\operatorname{supp}\alpha|\ge 8.
\]

([mathdept.byu.edu](https://mathdept.byu.edu/~pace/KaplanskyConjecture_web.pdf))

### Support \(3\)

Abdollahi–Taheri prove:

- arbitrary field: if \(m=3\), then \(n\ge 10\);
- over \(\mathbb F_2\): if \(m=3\), then \(n\ge 20\).

Thus, over \(\mathbb F_2\), all \(3\times n\) searches for \(n\le 19\) are dead. ([arxiv.org](https://arxiv.org/search/?abstracts=show&order=-announced_date_first&query=%22Kaplansky+Zero+Divisor%22&searchtype=all&size=200))

For rational coefficients, Schweitzer’s exhaustive matched-rectangle computation rules out the stronger range \(m\le3,\ n\le16\). ([arxiv.org](https://arxiv.org/abs/1202.6645))

### Support \(4\)

Abdollahi–Jafari prove:

- arbitrary field: \(m=4\Rightarrow n\ge7\);
- over \(\mathbb F_2\): \(m=4\Rightarrow n\ge9\).

The newer total-support bound \(m+n\ge16\) gives the stronger universal necessary condition \(n\ge12\) when \(m=4\). ([arxiv.org](https://arxiv.org/abs/1709.08204))

Schweitzer’s rational computation separately rules out \(m\le4,\ n\le7\). ([arxiv.org](https://arxiv.org/abs/1202.6645))

### Support \(1\) or \(2\)

These are structurally impossible for a torsion-free group. For example, after normalization a support-two factor has the form \(1-\lambda g\) with \(g\) of infinite order; a finite-support annihilator would force an impossible finite recurrence along a coset of \(\langle g\rangle\).

---

## E. Exhaustive combinatorial and computer searches

### Schweitzer: matched rectangles

Pascal Schweitzer translates a proposed zero divisor into a “matched rectangle,” i.e. a pairing/collision pattern on the \(m\times n\) product table. Every such rectangle gives a finitely presented universal group. His computer enumeration established the rational bounds:

- \((3,16)\);
- \((4,7)\).

The construction is universal in the sense that the rational conjecture is equivalent to the absence of a valid torsion-free associated group across all matched rectangles. ([arxiv.org](https://arxiv.org/abs/1202.6645))

### Bondarenko–Juschenko: pairing matrices and Mealy automata

They associate a Mealy automaton to the collision pairing and show that the zero-divisor conjecture holds for groups arising from invertible three-state automata. In particular, support-three candidates coming from invertible pairings are excluded. This is **not** a general support-three theorem; it checks the invertible-pairing axis only. ([arxiv.org](https://arxiv.org/abs/2402.08625))

### Garg–Mineyev: oriented product structures/taikos

They prove:

- no special “counterexample of type \((m,n)\)” with \(m\le5\), any \(n\);
- computer-assisted: no such type for \(m,n\le13\);
- computer-assisted: no such type for \(m\in\{6,7\}\), \(n\le200\), including transposed pairs.

([arxiv.org](https://arxiv.org/html/2501.07646v2))

**Critical limitation:** these are exclusions within their sufficient CAT(0)/origami construction, not exclusions of all zero divisors with those support sizes. It would be wrong to report “all \(13\times13\) zero divisors are ruled out.”

### Tabei 2026: non-UP computations in \(P\)

This is precursor geometry, not zero-divisor enumeration:

- inside balls of radii \(3,\dots,6\), the least symmetric non-UP set in \(P\) has size \(14\);
- inside the radius-three ball, the two-sided minimum \(|A|+|B|\) is \(24\);
- the paper supplies code and exact certificates.

([arxiv.org](https://arxiv.org/abs/2607.18346))

Because \(P\) is already known to be a domain, these data cannot lead to a zero divisor in \(P\).

---

# 3. WHY IS THE CONJECTURE BELIEVED?

## Structural evidence — type (a)

There are genuine structural reasons in large regions:

1. **Orderings:** leading terms cannot cancel.
2. **Unique products:** a uniquely represented product has an uncancellable nonzero coefficient.
3. **Mal’cev–Neumann and other skew-field embeddings:** the whole group algebra embeds in a domain.
4. **Strong Atiyah methods:** the division closure in affiliated operators is a skew field.
5. **Elementary amenable/polycyclic structure:** localization and \(K\)-theoretic methods force the domain property.
6. **Recent division-ring embeddings:** virtually compact special, 3-manifold, one-relator, and related groups.

The stronger conjecture that every torsion-free group algebra embeds in a division ring also remains without a counterexample. ([ems.press](https://ems.press/content/serial-article-files/52395))

## Search evidence — type (b)

There is also negative experimental evidence:

- no small matched rectangles yielding torsion-free counterexamples;
- support bounds through several low-dimensional ranges;
- no valid Garg–Mineyev structures in their computed ranges;
- decades of non-UP constructions without a zero divisor.

But this evidence is much weaker than it sounds. The universal search space grows explosively, and most computation has covered only tiny or specially structured regions.

## Overall diagnosis

The belief is **mixed**:

- within proved classes, it is strongly type **(a)**;
- outside them, it is partly extrapolation and type **(b)**.

It is not simply “we searched and found nothing,” but there is also no known universal structural principle remotely covering all torsion-free groups. Gardam himself observed that the zero-divisor and idempotent conjectures had originally been posed with little evidence. ([arxiv.org](https://arxiv.org/abs/2102.11818))

The unit counterexample weakens faith in the historical cluster of conjectures, but \(P\) demonstrates the exact limitation of that analogy: a torsion-free group algebra may be a domain and nevertheless have highly nontrivial units.

---

# 4. REFORMULATIONS AND REPRESENTATION SHIFTS

## A. Finite bilinear system

For fixed finite supports

\[
A=\{a_1,\ldots,a_m\},\qquad
B=\{b_1,\ldots,b_n\},
\]

write

\[
\alpha=\sum_i x_i a_i,\qquad
\beta=\sum_j y_j b_j.
\]

Then \(\alpha\beta=0\) is exactly the finite system

\[
\sum_{\substack{i,j\\a_i b_j=g}}x_i y_j=0
\qquad(g\in AB).
\]

Thus, once a group and finite search window are fixed, the problem is a finite system of bilinear equations.

Over \(\mathbb F_2\), if \(A,B\) are the exact supports, every fiber of

\[
A\times B\longrightarrow G,\qquad (a,b)\mapsto ab
\]

must have even cardinality.

That is substantially stronger than merely being non-UP: “no singleton fiber” allows multiplicity \(3\), whereas an \(\mathbb F_2\) zero divisor requires even parity.

---

## B. Gardam’s exact SAT formulation

Gardam’s published SAT description calls the encoding **“completely naive.”** The structured piecewise symmetry in the final proof was recognized **after** the solver found the unit; it was not the principal search constraint. ([satcompetition.github.io](https://satcompetition.github.io/2022/downloads/sc2022-proceedings-DRAFT.pdf))

### Candidate universe

Enumerate group elements in shortlex order

\[
g_1=1,g_2,g_3,\ldots
\]

and choose the first \(N\) elements as possible support for both factors:

\[
\alpha=\sum_{i=1}^N a_i g_i,\qquad
\beta=\sum_{j=1}^N b_j g_j,
\]

with Boolean variables \(a_i,b_j\).

### Product encoding

Introduce

\[
c_{ij}\leftrightarrow a_i\land b_j.
\]

For every product value \(g_k\), impose the parity condition

\[
\bigoplus_{\{(i,j):g_i g_j=g_k\}}c_{ij}
=
\begin{cases}
1,&g_k=1,\\
0,&g_k\ne1,
\end{cases}
\]

which says \(\alpha\beta=1\).

Long XORs were broken into XORs of at most four variables; an \(\ell\)-variable parity equation was encoded by \(2^{\ell-1}\) CNF clauses. The encoding uses \(N^2\) product variables before parity auxiliaries. ([satcompetition.github.io](https://satcompetition.github.io/2022/downloads/sc2022-proceedings-DRAFT.pdf))

### Symmetry breaking

Translation symmetry was used to force the identity into the selected supports, and disjunctions asserted that both factors were nontrivial. No fixed support cardinality was imposed.

### Exact reported thresholds in \(P\)

For Gardam’s shortlex ordering:

- radius-four ball: \(83\) elements;
- largest unsatisfiable initial segment: \(N=92\);
- smallest satisfiable initial segment: \(N=93\);
- radius-five ball: \(147\) elements.

The first whole Cayley ball that works is radius \(5\). ([satcompetition.github.io](https://satcompetition.github.io/2022/downloads/sc2022-proceedings-DRAFT.pdf))

### Actual output support

The resulting unit has support \(21\):

\[
u=p+qa+rb+sab,
\]

where \(x=a^2,\ y=b^2,\ z=(ab)^2\) and

\[
\begin{aligned}
p&=(1+x)(1+y)(1+z^{-1}),\\
q&=x^{-1}y^{-1}+x+y^{-1}z+z,\\
r&=1+x+y^{-1}z+xyz,\\
s&=1+(x+x^{-1}+y+y^{-1})z^{-1}.
\end{aligned}
\]

The four cosets contribute \(8+4+4+5=21\) terms. ([cs.cmu.edu](https://www.cs.cmu.edu/~mheule/MSS/04-collatz.pdf))

### Analogous zero-divisor SAT encoding

The zero-divisor encoding differs at exactly the right-hand side:

\[
\bigoplus_{g_i g_j=g_k}c_{ij}=0
\quad\text{for every }k,
\]

with separate constraints that both \(\alpha\) and \(\beta\) are nonzero.

Gardam explicitly described this as differing from the unit formula in “only one bit.” ([gilesgardam.com](https://www.gilesgardam.com/slides/smri.pdf))

So the analogous formulation is very much written down. What is missing is not the SAT encoding but a good theorem-live candidate group.

---

## C. Universal collision presentations

A collision pattern such as

\[
a_i b_j=a_{i'}b_{j'}
\]

can be turned into a finitely presented universal group. A valid counterexample requires:

1. the resulting group to be torsion-free;
2. all designated support elements to remain distinct;
3. the required product coincidences;
4. coefficient equations to cancel in the selected field.

This is the matched-rectangle/pairing-matrix viewpoint of Schweitzer and Bondarenko–Juschenko. It changes the problem from “search words in a group” to:

> enumerate finite collision structures, then decide which universal groups are torsion-free and nondegenerate.

That last step is the bottleneck.

---

## D. Mealy automata

Bondarenko–Juschenko turn the product pairing into a Mealy automaton, allowing:

- invertibility tests;
- Helix-graph invariants;
- systematic classification of pairing matrices;
- group-theoretic deductions from automaton structure.

This is a genuine representation shift, not merely faster brute force. ([arxiv.org](https://arxiv.org/abs/2402.08625))

---

## E. Taikos/origami/CAT(0) complexes

Mineyev’s origami construction and Garg–Mineyev’s oriented product structures encode a collision pattern as a finite cell complex. Combinatorial local-link and girth conditions can then certify that the associated group is torsion-free CAT(0). ([arxiv.org](https://arxiv.org/html/2501.07646v2))

This directly addresses the hardest part of universal-presentation searches—torsion-freeness—but only within a restricted geometric ansatz.

---

## Best formulation for a new search

I would use a **two-level search**:

1. **Collision-pattern level:**  
   Enumerate pairings/even partitions of \(A\times B\), modulo \(S_m\times S_n\), and apply all known non-UP, girth, orientability, automaton, and small-support filters.

2. **Instantiation level:**  
   Either:
   - realize the pattern in a known theorem-live torsion-free group with an efficient normal form; or
   - generate a small-cancellation/CAT(0) presentation with a machine-checkable torsion-freeness certificate.

Only after this should one solve the field-coefficient equations by XOR-SAT, finite-field Gröbner methods, or SMT.

Searching coefficients first in a crystallographic or virtually solvable group is wasted compute.

---

# 5. NEAR MISSES

## A. The strongest direct near miss: explicit \(3\times14\) zero-divisor identities

Two finitely presented two-generator, three-relator groups were isolated for which an explicit identity of the form

\[
(1+a+b)\beta=0
\]

holds over \(\mathbb F_2\), with \(|\operatorname{supp}\beta|=14\). If either group were torsion-free and the displayed supports remained nondegenerate, it would disprove the conjecture.

For example,

\[
\begin{aligned}
G_1=\langle a,b\mid\;&(ab)^2=a^{-1}ba^{-1},\\
&(a^{-1}ba^{-1})^2=b^{-2}a,\\
&(ba^{-1})^2=a^{-2}b^2\rangle,
\end{aligned}
\]

with a second similar presentation \(G_2\). The outstanding issue is torsion-freeness, not finding the zero-divisor identity. ([mathoverflow.net](https://mathoverflow.net/questions/231922/torsion-freeness-of-two-groups-with-2-generators-and-3-relators-and-kaplansky-ze))

These derive from the computational world surrounding Dykema–Heister–Juschenko’s work. I found no 2024–2026 paper resolving the torsion-freeness of these two specific groups. That negative should be treated as search coverage, not proof that no resolution exists.

**This is a better immediate target than \(\mathbb F_2[P]\): automate the torsion analysis of the existing universal-pairing groups.**

## B. Rips–Segev and graphical small-cancellation groups

Rips and Segev constructed the first torsion-free non-UP groups, originally motivated in part by the zero-divisor problem. Subsequent work produced more explicit and finite-index non-UP examples. None is known to yield a zero divisor. Some modern small-cancellation candidates are now dead because they fall into virtually special or strong-Atiyah classes; this must be checked group by group. ([mathdept.byu.edu](https://mathdept.byu.edu/~pace/KaplanskyConjecture_web.pdf))

## C. Minimal non-UP sets

Nielsen–Soelberg’s sharp \(8+8\) examples are extremal combinatorial precursors. Their universal example does not immediately produce a zero divisor. ([mathdept.byu.edu](https://mathdept.byu.edu/~pace/KaplanskyConjecture_web.pdf))

At the balanced \(8\times8\) threshold, even restricting an \(\mathbb F_2\) collision pattern to pairings gives

\[
63!!=\frac{64!}{2^{32}32!}\approx 1.1\times10^{44}
\]

raw pairings before support relabelling. Thus “the lower bound is only eight” does not mean the finite search is small.

## D. Soelberg’s virtually Heisenberg example

Gardam reported nontrivial units, including one of support \(29\), in a torsion-free virtually nilpotent group introduced by Soelberg. It also has very small non-UP sets. But virtually nilpotent groups are elementary amenable, so its group algebra is zero-divisor-free. ([gilesgardam.com](https://www.gilesgardam.com/slides/smri.pdf))

This is another unit/UPP near miss that is completely dead for zero divisors.

## E. Torsion groups

If \(g^n=1\), then

\[
(1-g)(1+g+\cdots+g^{n-1})=0.
\]

Thus zero divisors are immediate once torsion is allowed. The conjecture is exactly about whether the absence of group torsion is enough to prevent all more subtle cancellations.

---

# 6. WHO IS ACTIVELY WORKING ON IT?

| Researchers | Current visible activity | Relevance |
|---|---|---|
| **Manisha Garg, Igor Mineyev** | 2025 oriented-product/taiko search with public code | Most direct current computer search for special zero-divisor constructions. ([arxiv.org](https://arxiv.org/abs/2501.07646)) |
| **Ievgen Bondarenko, Kate Juschenko** | Pairing matrices and Mealy automata | Structural finite parametrization, especially support-three cases. ([arxiv.org](https://arxiv.org/abs/2402.08625)) |
| **Moe Tabei** | July 2026 exact constraint solving with code and certificates for \(P\) and a Fibonacci-group companion | Non-UP precursor search, not zero divisors. ([arxiv.org](https://arxiv.org/abs/2607.18346)) |
| **Heiko Dietrich, Melissa Lee, André Nies, Marc Vinyals** | March 2026 computational units/UPP paper | Follow-up to Gardam and search methodology; not a zero-divisor result. ([arxiv.org](https://arxiv.org/abs/2603.22640)) |
| **Giles Gardam** | SAT formulations, 2025 Simons/SLMath AI-for-math workshop talk | Publicly explains automated search; no public zero-divisor run of comparable scale found. ([simons.berkeley.edu](https://simons.berkeley.edu/news/solving-semidecidable-problems-group-theory)) |
| **Sam Fisher, Pablo Sánchez-Peralta; Sam Fisher, Andrew Ng** | 2026 division-ring/Atiyah results | Expanding the regions in which counterexample search is dead. ([ems.press](https://ems.press/content/serial-article-files/52395)) |

I found **automated SAT, exact constraint, GAP, and combinatorial-enumeration efforts**, but no public project describing an LLM-, reinforcement-learning-, or otherwise explicitly AI-guided zero-divisor counterexample hunt.

Gardam’s 2025 talk occurred at an AI-for-mathematics workshop, but the actual method described is classical SAT solving, not an AI conjecture-search system. I also found no public announcement that a team is currently running a large undisclosed zero-divisor sweep. Private efforts cannot be ruled out.

---

# 7. TRACTABILITY CALL

## Verification complexity

If \(G\) has a reliable normal form, an explicit candidate is cheap to verify:

1. compute the \(mn\) products \(a_i b_j\);
2. collect equal group elements;
3. add coefficients in \(K\);
4. check both factors are nonzero.

A \(20\times20\) candidate is trivial to verify computationally.

The hard certificate is usually:

> **Why is the ambient finitely presented group torsion-free, and why are all designated support elements distinct?**

That can be vastly harder than checking \(\alpha\beta=0\).

## Fixed-ball search size

For Gardam’s radius-five \(P\)-window, \(N=147\):

- coefficient choices for one element: \(2^{147}\approx1.8\times10^{44}\);
- raw choices for a pair: \(2^{294}\approx3.1\times10^{88}\);
- \(N^2=21{,}609\) product variables before XOR auxiliaries.

SAT solves such instances only because product multiplicities create strong propagation. But the zero-divisor search lacks a plausible group analogous to \(P\): \(P\) and every similarly small crystallographic group are theorem-dead.

## Biggest obstacle

**The single largest obstacle is candidate-group selection and torsion-freeness certification, not SAT scale.**

Known groups divide awkwardly into:

- groups with excellent normal forms and small non-UP sets, but whose group rings are already proved domains; or
- theorem-live non-UP groups with complicated presentations, large relation scale, and difficult word/torsion problems.

## Recommended compute allocation

1. **Spend zero compute on \(P\), crystallographic groups, virtually nilpotent groups, or other elementary amenable groups.**
2. Revisit the explicit \(3\times14\) pairing groups: automate torsion detection, small-cancellation recognition, actions on CAT(0) complexes, and finite-quotient diagnostics.
3. Build a database of explicit torsion-free non-UP groups and eliminate every one covered by:
   - virtually special;
   - one-relator;
   - elementary amenable;
   - strong Atiyah;
   - 3-manifold;
   - known division-ring embedding.
4. On the survivors, enumerate collision patterns rather than arbitrary support subsets.
5. Produce DRAT/LRAT-style UNSAT certificates for negative SAT ranges, so exclusions are independently auditable.
6. Search several small finite fields, not only \(\mathbb F_2\); the parity formulation is exceptionally convenient but not universal.

## Verdict on feasibility: **MARGINAL**

Why not hopeless:

- a discovered object would be finite, explicit, and cheaply checkable;
- SAT has already killed the unit conjecture;
- matched rectangles, Mealy automata, and taikos offer finite parametrizations;
- there are existing formal \(3\times14\) identities awaiting group-theoretic certification.

Why not promising:

- the exact Gardam group is completely dead;
- all similar crystallographic/virtually solvable groups are dead;
- total support below \(16\) is dead;
- the first balanced collision space is already around \(10^{44}\) before serious group constraints;
- no convincing theorem-live group with a demonstrably small collision geometry is currently known.

---

# Search-coverage limitations

I used:

- exact arXiv searches sorted by newest announcement;
- recent arXiv abstracts and full HTML/PDF where available;
- EMS, Cambridge, Annals-related author copies;
- the SAT Competition proceedings;
- author-hosted slides, code links, and ancillary certificates;
- citation chains through the 2025–2026 papers.

I could not exhaustively query closed portions of **MathSciNet, zbMATH, Scopus, or Web of Science**, and I cannot inspect private computations. Some recent results—especially the 2025 Garg–Mineyev and 2026 Tabei/Dietrich/Fisher–Ng papers—are preprints and should not be treated as independently refereed unless a journal version is identified.

---

# Core references

1. **Giles Gardam**, “A counterexample to the unit conjecture for group rings,” *Annals of Mathematics* 194(3), 2021, 967–979. arXiv:2102.11818. DOI: 10.4007/annals.2021.194.3.9.  
   URL: https://arxiv.org/abs/2102.11818 ([arxiv.org](https://arxiv.org/abs/2102.11818))

2. **Alan G. Murray**, “More Counterexamples to the Unit Conjecture for Group Rings,” 2021, arXiv preprint. arXiv:2106.02147. DOI: 10.48550/arXiv.2106.02147.  
   URL: https://arxiv.org/abs/2106.02147 ([arxiv.org](https://arxiv.org/abs/2106.02147))

3. **Giles Gardam**, “Non-trivial units of complex group rings,” 2023, arXiv preprint. arXiv:2312.05240. DOI: 10.48550/arXiv.2312.05240.  
   URL: https://arxiv.org/abs/2312.05240 ([arxiv.org](https://arxiv.org/abs/2312.05240))

4. **Giles Gardam**, “Group ring units in SAT,” *Proceedings of SAT Competition 2022: Solver and Benchmark Descriptions*, 2022.  
   URL: https://satcompetition.github.io/2022/downloads/sc2022-proceedings-DRAFT.pdf ([satcompetition.github.io](https://satcompetition.github.io/2022/downloads/sc2022-proceedings-DRAFT.pdf))

5. **Gerald H. Cliff**, “Zero Divisors and Idempotents in Group Rings,” *Canadian Journal of Mathematics* 32(3), 1980, 596–602. DOI: 10.4153/CJM-1980-046-3.  
   URL: https://doi.org/10.4153/CJM-1980-046-3 ([cambridge.org](https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/zero-divisors-and-idempotents-in-group-rings/CA75D92676C7DF45DDC06553A7E637A8))

6. **P. H. Kropholler, P. A. Linnell, J. A. Moody**, “Applications of a new K-theoretic theorem to soluble group rings,” *Proceedings of the AMS* 104(3), 1988, 675–684. No arXiv; DOI not identified in the accessible sources.

7. **Joel Cohen**, “Zero divisors in group rings,” *Communications in Algebra* 2, 1974, 1–14. DOI: 10.1080/00927877408822001. ([arxiv.org](https://arxiv.org/html/2501.07646v2))

8. **Pascal Schweitzer**, “On Zero Divisors with Small Support in Group Rings of Torsion-Free Groups,” *Journal of Group Theory* 16(5), 2013, 667–693; arXiv:1202.6645. DOI for the journal version not identified here.  
   URL: https://arxiv.org/abs/1202.6645 ([arxiv.org](https://arxiv.org/abs/1202.6645))

9. **Alireza Abdollahi, Zahra Taheri**, “Kaplansky’s zero divisor and unit conjectures on elements with supports of size 3,” 2016, arXiv:1612.00934. DOI: 10.48550/arXiv.1612.00934.  
   URL: https://arxiv.org/abs/1612.00934 ([arxiv.org](https://arxiv.org/abs/1612.00934))

10. **Alireza Abdollahi, Fatemeh Jafari**, “Zero divisor and unit elements with support of size 4 in group algebras of torsion free groups,” 2017, arXiv:1709.08204. DOI: 10.48550/arXiv.1709.08204.  
    URL: https://arxiv.org/abs/1709.08204 ([arxiv.org](https://arxiv.org/abs/1709.08204))

11. **Ievgen Bondarenko, Kate Juschenko**, “The zero divisor conjecture and Mealy automata,” 2024, arXiv:2402.08625. DOI: 10.48550/arXiv.2402.08625.  
    URL: https://arxiv.org/abs/2402.08625 ([arxiv.org](https://arxiv.org/abs/2402.08625))

12. **Manisha Garg, Igor Mineyev**, “On zero-divisors and units in group rings of torsion-free CAT(0) groups,” 2025, arXiv:2501.07646v2. DOI: 10.48550/arXiv.2501.07646.  
    URL: https://arxiv.org/abs/2501.07646 ([arxiv.org](https://arxiv.org/abs/2501.07646))

13. **Sam P. Fisher, Pablo Sánchez-Peralta**, “Division rings for group algebras of virtually compact special groups and 3-manifold groups,” *Journal of Combinatorial Algebra* 10, 2026, 153–193. arXiv:2303.08165. DOI: 10.4171/JCA/89.  
    URL: https://doi.org/10.4171/JCA/89 ([ems.press](https://ems.press/content/serial-article-files/52395))

14. **Sam P. Fisher, Andrew Ng**, “Outer automorphism groups and the Atiyah Conjecture,” 2026, arXiv:2606.19606. DOI: 10.48550/arXiv.2606.19606.  
    URL: https://arxiv.org/abs/2606.19606 ([arxiv.org](https://arxiv.org/abs/2606.19606))

15. **Heiko Dietrich, Melissa Lee, André Nies, Marc Vinyals**, “On the trivial units property and the unique product property,” 2026, arXiv:2603.22640. DOI: 10.48550/arXiv.2603.22640.  
    URL: https://arxiv.org/abs/2603.22640 ([arxiv.org](https://arxiv.org/abs/2603.22640))

16. **Moe Tabei**, “Least sizes of non-unique-product sets: the Promislow group and a Heisenberg-type candidate,” 2026, arXiv:2607.18346, with code and certificates. DOI: 10.48550/arXiv.2607.18346.  
    URL: https://arxiv.org/abs/2607.18346 ([arxiv.org](https://arxiv.org/abs/2607.18346))

17. **Ken Dykema, Timo Heister, Kate Juschenko**, “Finitely presented groups related to Kaplansky’s direct finiteness conjecture,” *Experimental Mathematics* 24(3), 2015, 326–338. DOI: 10.1080/10586458.2014.993051. ([arxiv.org](https://arxiv.org/html/2501.07646v2))

---

# VERDICT: OPEN | MARGINAL

The global zero-divisor conjecture remains open, but \(\mathbb F_2[P]\)—and every torsion-free crystallographic analogue—is completely ruled out by theorem, at every support size. A machine hunt remains conceivable because a counterexample would be finite and cheaply verifiable, but the real unsolved search problem is finding and certifying a small, theorem-live torsion-free ambient group; SAT itself is not the limiting factor.