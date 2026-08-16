# Weighted path-pair spend or bottleneck

**Date:** 2026-08-14  
**Verdict:** a fixed-root pocket recursion has an exact weighted DAG
dichotomy with subexponential one-step loss.  Give every hidden-ear history
a directed path through its non-forced edge states.  For two independent
histories, any suitably nonnested pair or internally disjoint lens may be
spent through the two-record switch into two-ended faces.  If the
resource-disjoint pair mass is smaller than `delta`, then a set of at most

\[
                         L/\sqrt\delta                         \tag{1}
\]

vertices or edges meets all but `2\sqrt\delta` of the path mass, where `L`
is the maximum number of recorded choice states on one path.  For
`delta=2^{-2b}` with `b=o(r)`, this is a `2^{o(r)}` bottleneck state set
retaining `1-o(1)` mass.

The exact zero case is Menger: for the full `s`--`t` path set of a support
subgraph, absence of two internally disjoint paths gives one common
vertex/edge cut.  The weighted approximate statement cannot in general be
strengthened to one common vertex; a subexponential bottleneck set is the
correct robust version.

Combining the theorem over `h` batched descents costs at most

\[
                       (L2^b)^h                                  \tag{2}
\]

states and discards at most `h2^{1-b}` mass.  Thus
`h(b+log L)=o(r)` gives subexponential total loss.  Consecutive short
descents need not be batched individually: if their discarded prefixes are
nested, the chain-complex release from the dynamic pair theorem terminates
them at constant cost.

This is a rigorous path-DAG advance, not a proof of Erdős 838.  The remaining
geometric assertion is that a positive fraction of the graph-theoretic
spend pairs have the two planar tangent signs needed by the cross-union
map, and that face-pair reuse across different support subgraphs is
`2^{o(r)}`.

## 1. Choice-resource path laws

Let `G` be a finite DAG, and let `mathcal P` be a finite family of directed
paths.  Assign nonnegative weights summing to one.  Fix a set `R` of
**choice resources**, either vertices or edges, and assume every path uses
at most `L` members of `R`.

Mandatory root chords, common sources/sinks, and deterministic spine edges
must first be contracted or excluded from `R`.  Otherwise every pair would
intersect for a vacuous reason.  For a path `P`, write

\[
                     R(P)=R\cap P.                           \tag{3}
\]

For independent paths `P,Q`, define the disjoint-lens mass

\[
              Delta_R=Pr\{R(P)\cap R(Q)=\varnothing\}.       \tag{4}

In a planar embedded state DAG there is a second useful class.  Decompose
two paths at their common states into maximal lenses.  Give each lens the
left/right sign of its two routes.  If both signs occur, call the pair
**nonnested**.  Such a pair has an upper lens followed by a lower lens (or
the reverse), which is the path analogue of a cap coordinate followed by a
cup coordinate.  After the rank-three tangent signs are checked, it is a
terminal input to the two-record switch theorem.

The resource-disjoint class and the nonnested class are deliberately not
identified.  Parallel routes through one product block can be disjoint but
left/right comparable; binary product words can share some choice edges
while having many sign reversals.  Either type may provide geometric spend.

## 2. The weighted bottleneck theorem

For a resource `x in R`, let

\[
                         p_x=Pr\{x\in P\}.                    \tag{5}

The elementary second-moment estimate is

\[
 \Pr\{R(P)\cap R(Q)\ne\varnothing\}
 \le\sum_xp_x^2
 \le (\max_xp_x)\sum_xp_x
 \le L\max_xp_x.                                           \tag{6}

The useful robust form iteratively removes heavy resources.

> **Theorem 1 (weighted path-pair/bottleneck dichotomy).**  Let
> `0<delta<1`.  At least one of the following holds:
>
> 1. `Delta_R>=delta`; or
> 2. there is a resource set `B subseteq R` with
>    \[
>       |B|\le {L\over\sqrt\delta},\qquad
>       Pr\{P\cap B\ne\varnothing\}\ge1-2\sqrt\delta.       \tag{7}
>    \]
>
> More precisely, conclusion 2 holds whenever `Delta_R<delta`.

**Proof.**  Put `a=\sqrt\delta/L`.  Starting with the full path law, if a
resource has remaining unnormalized load at least `a`, add it to `B` and
delete all remaining paths using it.  Deleted path classes are disjoint and
each has mass at least `a`, so `|B|<=1/a=L/\sqrt\delta`.

Suppose the final remaining path mass is `m`.  Every remaining resource has
unnormalized load less than `a`, while the sum of the loads is at most `Lm`.
Hence the unnormalized mass of intersecting remaining pairs is at most
`aLm=\sqrt\delta\,m`.  Their disjoint-pair mass is therefore at least

\[
                         m^2-\sqrt\delta\,m.                 \tag{8}
\]

This is part of the original disjoint mass and is smaller than `delta`.
If `m>2\sqrt\delta`, (8) is larger than `2\delta`, a contradiction.  Thus
`m<=2\sqrt\delta`, proving (7).  QED.

The theorem is valid for arbitrary weights and for an arbitrary chosen path
family; it does not assume that the weights factor across layers.

### Exact Menger endpoint

Let `mathcal P` be the set of **all** `s`--`t` paths in a support subgraph,
assume `s,t` are nonadjacent (subdivide a direct edge if necessary), and
take internal vertices as resources.  If no two paths are internally
vertex-disjoint, the maximum internally disjoint path packing has size one.
Menger's theorem gives a one-vertex `s`--`t` cut, and that vertex lies on
every path.  The edge version follows from edge-Menger.  This conclusion is
not asserted for an arbitrary non-support-complete subfamily: pairwise
intersection of a selected path family need not have the Helly property.

## 3. LGV converts disjoint path mass to minors

Let a planar acyclic network have ordered boundary sources `a_1<a_2` and
sinks `b_1<b_2`, positive edge weights, and path-sum matrix

\[
                     Z_{ij}=\sum_{P:a_i\to b_j}w(P).          \tag{9}

The Lindström--Gessel--Viennot involution gives

\[
 \det\begin{pmatrix}Z_{11}&Z_{12}\\Z_{21}&Z_{22}\end{pmatrix}
 =\sum_{(P_1,P_2)\ {\rm vertex\!\!-disjoint}}
                  w(P_1)w(P_2),                              \tag{10}

with the boundary order chosen so the crossed disjoint routing is absent.
Thus the first branch of Theorem 1 is exactly positive `2 times 2` minor
mass after the common root/sink is split into its tangent states.

Graph disjointness alone does not prove convexity.  In the planar
convex-geometry application, each surviving minor must also carry the two
endpoint chirotope signs.  When it does, the two routes are opposite rooted
arcs, and Theorem 1 of `../dynamic_pair_kraft/REPORT.md` maps the two path
records to an ordered pair of cross-union faces with forgotten-chord fibre
at most `r(r-1)`.  Therefore a spend mass `delta` yields

\[
             \text{distinct face-pair capacity}
             \ \ge {\delta E^2\over 2^{o(r)}}                \tag{11}

whenever tangent/state recovery is subexponential.

Nonnested mixed-lens pairs contribute additional minors after cutting at
their first sign reversal.  They are essential in product endpoint blocks,
where global resource-disjointness can be unnecessarily strong.

## 4. A weighted nonnested-path lemma

The left/right relation on `s`--`t` paths of a planar embedded `st`-DAG is
a partial order: `P<=Q` when `P` stays weakly to one side of `Q`.  Two paths
are incomparable exactly when their lens-sign word contains both signs.
Let `H` be the maximum size of a chain in the supported path poset, let
`mu` be any probability law, let

\[
 Delta_{\rm nn}=Pr\{P,Q\text{ are distinct and incomparable}\},
 \qquad C=Pr\{P=Q\}.                                      \tag{12}

> **Lemma 2 (weighted nonnested or common-path fibre).**
> \[
>                         \boxed{\Delta_{\rm nn}+C\ge1/H.}   \tag{13}
> \]
> Consequently either `Delta_nn>=1/(2H)`, or some single path has mass at
> least `1/(2H)` and every resource on that path is a common bottleneck for
> that record fibre.

**Proof.**  Rank every supported path by the length of a longest chain
ending there.  There are at most `H` ranks, and each rank class is an
antichain.  If its total mass is `q_j`, two samples in the same class are
either equal or incomparable.  Therefore

\[
        \Delta_{\rm nn}+C\ge\sum_jq_j^2\ge1/H.               \tag{14}
\]

Also `max_P mu(P)>=sum_Pmu(P)^2=C`, proving the last assertion.  QED.

For full ordered word paths with alphabet sizes `m_i`, one can take

\[
                         H\le1+\sum_i(m_i-1),                 \tag{15}

using the coordinate-rank potential.  Lemma 2 is then the weighted path
version of the single-crossing split theorem.  A large common-path fibre is
not discarded: it is precisely a fixed edge-state child on which the
internal core must be exposed recursively.

## 5. Batched recursive bottlenecks have subexponential cost

Choose `delta=2^{-2b}`.  Theorem 1 becomes

\[
 \boxed{
 \Delta_R\ge2^{-2b}\quad\text{or}\quad
 |B|\le L2^b,\quad Pr(P\text{ hits }B)\ge1-2^{1-b}.}          \tag{16}

In the second branch, assign every captured path to its first resource in
`B`.  This partitions rather than pigeonholes the retained mass; the state
cost is `|B|`, not an additional loss of `|B|` in mass.

> **Corollary 3 (batched path Kraft bound).**  Suppose a recursion has at
> most `h` nonterminal bottleneck phases, and at each phase either spends
> the disjoint/nonnested mass or applies (16).  Then the bottleneck branch
> retains mass at least
> \[
>                         1-h2^{1-b}                         \tag{17}
> \]
> and has at most
> \[
>                         (L2^b)^h                           \tag{18}
> \]
> state sequences.  In particular, if
> \[
>               h2^{1-b}=o(1),\qquad h(b+\log_2L)=o(r),      \tag{19}
> \]
> both losses are subexponential at rank `r`.

**Proof.**  Apply the union bound to the discarded conditional mass at the
`h` phases.  Multiply the branch counts in (16).  QED.

For example, with `L=O(r)`, `b=r^(1/3)`, and at most `h=r^(1/3)` batched
phases, the tag exponent is `O(r^(2/3)+r^(1/3)log r)=o(r)`.  A sufficient
geometric batching rule is that every nonrelease bottleneck advances by at
least `r^(2/3)` boundary states.  Shorter repeated descents must instead be
terminated against their discarded prefix complex.  A nested chain has
width one and costs only the sharp `9/4` pair factor from the dynamic Kraft
report, regardless of its depth.

## 6. Equality tests

### 6.1 Nested parabola

Model the successive parabolic prefixes by paths using resource sets

\[
                    \{e_1\},\{e_1,e_2\},\ldots,
                    \{e_1,\ldots,e_s\}.                       \tag{20}

Every pair meets at `e_1`, so `Delta_R=0`; `B={e_1}` captures mass one and
is the exact Menger bottleneck.  Repeating this one edge at a time would be
the wrong accounting.  The discarded states form one inclusion chain, so
the whole family terminates at once through its Boolean prefix pool with
pair congestion at most `9/4`.  The nested parabola therefore passes both
the graph dichotomy and the required prefix release.

### 6.2 Product endpoint blocks

Represent a word in `Q_1 times ... times Q_q` by the `q` choice edges
`(i,x_i)` of a layered multigraph.  For the uniform word law,

\[
                 \Delta_R=\prod_{i=1}^q(1-1/m_i).             \tag{21}

For a large block this is close to one, giving the disjoint-lens branch.
For binary blocks it can be `2^{-q}`, too small for a subexponential spend.
But the left/right nonnested mass is exactly

\[
 1-{2\prod_i m_i(m_i+1)/2-\prod_i m_i\over(\prod_i m_i)^2}
 \ge1-2(3/4)^q.                                             \tag{22}

Thus many small endpoint blocks take the nonnested branch instead.  If
`q=1`, every pair is comparable, but (21) is `1-1/m_1`: two distinct
parallel choices form the local lens/internal block face.  The product
family is therefore paid in every regime; no repeated bottleneck loss is
needed.

The ramp--plateau alphabets obey the same exact formulas.  Their atomic
one-target interval reservoir is small, but their path-pair mass is not:
the two-record switch must retain the complete routes on both sides, which
is precisely why (11) uses ordered **face pairs**.

## 7. Exact residual

The graph-theoretic part is now complete.  A universal planar proof would
follow from these two geometric assertions.

1. After contracting forced spine states, a `2^{-o(r)}` fraction of the
   disjoint or nonnested path-pair mass identified above has opposite-side
   tangent signs, so it spends by the two-record switch with
   `2^{o(r)}` recovery.
2. Every bottleneck sequence which fails the batched progress condition in
   Corollary 3 has discarded cyclic prefixes of effective width and global
   face-pair reuse `2^{o(r)}`, so it terminates by nested release.

The nested parabola proves why the second alternative must admit the common
tangent cell/core as the bottleneck.  Product blocks prove why “disjoint”
must be supplemented by nonnested mixed-lens pairs.  No graph theorem alone
can supply the missing rank-three tangent signs.

## 8. Verification

Run

```bash
python3 \
  phase2/loop/erdos838/agent_cyclic_stem_hw/path_dag_bottleneck/verify_path_bottleneck.py
```

The exact checker:

* exhausts 246 rational weighted path laws and verifies Theorem 1's greedy
  bottleneck construction whenever its disjoint mass is below the chosen
  square threshold;
* verifies the sharp nested-parabola bottleneck and prefix-pair release
  through depth 512;
* checks (21)--(22) against brute-force word pairs in 150 small product
  DAGs; and
* checks the exact formulas on the ramp--plateau profiles through `h=7`.

All probabilities are `Fraction` objects.  The Menger, LGV, and planar path
order statements are symbolic theorems proved or cited through their
standard involution/cut arguments above; no floating computation is used
as a substitute.
