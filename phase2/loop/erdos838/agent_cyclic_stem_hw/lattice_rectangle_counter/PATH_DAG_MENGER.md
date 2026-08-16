# Weighted path DAGs: the Menger dichotomy is valid only for intersection

**Date:** 2026-08-14  
**Verdict:** the weighted vertex-intersection version of the proposed path
dichotomy is universally true, with a polynomial rather than merely
subexponential bottleneck.  If every path has at most `r` nontrivial states,
then either a chosen fraction `delta` of ordered path pairs are internally
vertex-disjoint, or one internal state carries at least
`(1-delta)/r` of the total path mass.  This is an elementary second-moment
inequality; Menger's theorem is not needed.

Two strengthenings are false.

1. Replacing "internally disjoint" by "geometrically nonnested" is false
   unless the common tangent cell/core or the nested-prefix Boolean release
   is admitted as the bottleneck alternative.  An exact nested parabolic fan
   has zero nonnested-pair mass and arbitrarily small mass on every varying
   label-state.
2. An **edge-only** bottleneck is false.  Pairwise vertex-intersecting convex
   chains can be given path-specific connector edges, making every edge mass
   exponentially small while a vertex bottleneck remains.

The product endpoint and ramp--plateau DAGs pass the safe vertex theorem and
have abundant nonnested/forward pair mass.  The result is therefore useful
as a local recursion lemma, but it does not control global terminal target
reuse `kappa,rho` in the dynamic pair-Kraft theorem.

## 1. Exact conjectures tested

Let `mu` be a probability measure on a finite family of directed paths in a
DAG.  Universal roots and sinks, which every record carries for syntactic
reasons, are omitted from the internal state sets.  Put

\[
 \mu(v)=\Pr_{P\sim\mu}\{v\in P\},
 \qquad
 I=\Pr_{P,Q\sim\mu}\{P\cap Q\ne\varnothing\}.     \tag{1}
\]

The safe weighted Menger claim is:

> **`(WD)_delta`.**  If every path has at most `r` internal vertices, then
> either
> \[
>      \Pr(P\cap Q=\varnothing)\ge\delta,          \tag{2}
> \]
> or some internal vertex satisfies
> \[
>                         \mu(v)\ge{1-\delta\over r}. \tag{3}
> \]

The stronger geometric claim replaces (2) by a requirement that the two
one-sided convex chains be nonnested/crossing in the tangent order.  That
replacement is not equivalent: two paths can be internally disjoint while
their convex hulls are strictly nested.

## 2. Universal weighted vertex theorem

> **Theorem 1 (weighted intersection bottleneck).**  For paths with at most
> `r` internal vertices,
> \[
> \boxed{
> I\le\sum_v\mu(v)^2
>   \le r\max_v\mu(v).}                           \tag{4}
> \]
> Consequently `(WD)_delta` holds for every `0<=delta<=1`.

**Proof.**  If two paths intersect, at least one vertex belongs to both, so
the union bound gives the first inequality.  Also

\[
 \sum_v\mu(v)
 =\mathbb E|P|\le r.
\]

Therefore

\[
 \sum_v\mu(v)^2
 \le(\max_v\mu(v))\sum_v\mu(v)
 \le r\max_v\mu(v),
\]

proving (4).  If (2) fails, `I>1-delta`, and (3) follows. QED.

In particular, with `delta=1/2`, either half the ordered pair mass is
internally disjoint or one state retains at least `1/(2r)` path mass.  Since

\[
                         {1\over2r}=2^{-O(\log r)}=2^{-o(r)}, \tag{5}
\]

this is stronger than the desired subexponential local recursion fraction.
It works for arbitrary rational path weights, not only uniform path counts.

The identical edge statement holds if `I` in (1) means **sharing an edge**
and `r` bounds the number of internal edges.  Vertex intersection cannot be
used to infer a heavy edge.

## 3. Sharp planar one-sided path systems

The order of magnitude `1/r` in (3) cannot be improved from path incidence
alone.  Take the projective plane `PG(2,q)`.  Its

\[
                         N=q^2+q+1
\]

points are DAG states and its `N` lines are paths, with the points on a line
listed in one fixed global order.  Every path has `q+1` internal states,
every pair of paths meets in exactly one state, and every state lies on
`q+1` paths.  Under the uniform path law,

\[
 I=1,\qquad
 max_v\mu(v)={q+1\over q^2+q+1}=\Theta(1/r).     \tag{6}
\]

This is an exact one-sided planar convex-chain state system: map global
state `i` to `(i,i^2)`.  Every line path is an increasing subset of the
strict parabolic chain, hence is in convex position.  Directed edges always
increase the global index, so the union is a DAG.  The verifier constructs
`PG(2,q)` exactly for `q=3,5,7,11` and checks every incidence and pairwise
intersection.

| `q` | paths | states/path | maximum vertex mass |
|---:|---:|---:|---:|
| 3 | 13 | 4 | `4/13` |
| 5 | 31 | 6 | `6/31` |
| 7 | 57 | 8 | `8/57` |
| 11 | 133 | 12 | `12/133` |

Thus a path argument can promise polynomial mass, but not a constant-mass
single bottleneck.

## 4. Nested parabola kills the nonnested strengthening

Fix `N=2^R`, put `D=100N^2`, and take

\[
 u=(0,0),\qquad v=(D,0),\qquad
 z_j=(D/2+j^2,-D2^{j+1}),\quad0\le j<N.           \tag{7}
\]

For `i<j`, the point `z_i` lies strictly inside the triangle `uvz_j`.
Thus the rooted arcs

\[
                         P_j=(u,z_j,v)             \tag{8}
\]

form a totally nested family.  Their internal label-state paths are
pairwise disjoint, but no pair is geometrically nonnested.  Under the
uniform law,

\[
 \Pr(\text{internally disjoint})=1-{1\over N},qquad
 \Pr(\text{nonnested})=0,qquad
 max_j\mu(z_j)={1\over N}=2^{-R}.                \tag{9}

Therefore the claim

\[
 \text{many nonnested pairs}\quad\text{or}\quad
 \text{a heavy varying label-state}               \tag{10}
\]

is false by an exponential factor.  The verifier checks the exact integer
coordinates for `N=16,64,256`.

This is not an obstruction to the existing dynamic Kraft theorem.  If the
common rooted tangent cell is a DAG state, it has mass one.  If the cell is
opened, the discarded states form one inclusion chain and the nested-prefix
Boolean release pays them with constant pair congestion.  What fails is
trying to use nonnesting/Menger **instead of** those two alternatives.

The conclusion is a required trichotomy:

1. internally disjoint and tangent-nonnested paths yield switch candidates;
2. a heavy full tangent/prefix cell recurses with all multiplicity tags; or
3. a nested/low-width path family releases its Boolean prefix complex.

## 5. Product endpoint DAGs validate the safe route

For a full product

\[
                   \mathcal W=Q_1\times\cdots\times Q_b,
 \qquad |Q_i|=m_i,                                \tag{11}
\]

use the canonical prefix trie.  After the universal root is deleted, two
independent uniform paths intersect exactly when their first letters agree.
Hence

\[
 \Pr(\text{internally disjoint})=1-{1\over m_1},qquad
 \max_v\mu(v)={1\over m_1}.                       \tag{12}
\]

Conditioned on a shared prefix through coordinate `i-1`, the same identity
holds with `m_i`.  Thus at every recursive node either different letters
release `1-1/m_i` of pair mass or one letter-child retains `1/m_i` mass.
There is no accumulated depth loss: first divergences partition the pairs.

The ordered endpoint version is even stronger.  Give every alphabet the
same total order and call a pair nonforward when it is coordinatewise
monotone after its first comparison.  The exact ordered nonforward count,
including the diagonal, is

\[
 N_{nf}=2\prod_i {m_i(m_i+1)\over2}-N.            \tag{13}
\]

Since `m_i>=2`,

\[
 {N_{nf}\over N^2}\le2(3/4)^b.                 \tag{14}

\]

Consequently the homogeneous product endpoint blocks and ACP Proposition 26
have overwhelming nonnested/forward pair mass once several internal
coordinates remain.

## 6. Ramp--plateau also passes

For the ramp--plateau exponent word

\[
 (1,2,4,\ldots,L/2,
   \underbrace{L,\ldots,L}_{L/2\text{ copies}},
   L/2,\ldots,4,2,1),                             \tag{15}
\]

put `m_i=2^(a_i)`.  Its first alphabet has size two, so the root-deleted
prefix DAG has

\[
 \Pr(\text{internally disjoint})={1\over2},qquad
 max_v\mu(v)={1\over2}.                          \tag{16}
\]

At every plateau coordinate the conditional divergence probability is
`1-2^(-L)`.  Moreover (14), with `b=L/2+2log_2L`, gives

\[
 \Pr(\text{nonnested/forward})
 \ge1-2(3/4)^{L/2+2\log_2L}.                     \tag{17}

\]

For the exact `L=64` audit, the logarithm of the nonforward upper bound is
`-17.262...`.  The ramp defeats atomic one-target interval counts, but not
weighted path separation.  Its unresolved issue remains geometric target
recovery and reuse after a forward pair has been found.

## 7. Edge bottlenecks cannot replace vertex bottlenecks

Let `Omega` be all `r`-subsets of a `(2r-1)`-element ordered ground set.
Every two members intersect.  Regard each member as a path through its
selected ground states in increasing order.  Insert a path-specific
connector between each pair of consecutive selected states.  Then:

* all paths still intersect at a ground-state vertex;
* every directed edge belongs to exactly one path;
* the maximum vertex mass is `r/(2r-1)`; but
* the maximum edge mass is
  \[
               {1\over\binom{2r-1}{r}}=2^{-\Theta(r)}.       \tag{18}
  \]

This too has a rational parabolic realization: place ground and connector
states in topological order on `y=x^2`.  Each path is a one-sided convex
chain.  Hence a Menger route may use a heavy vertex, but cannot demand a
heavy transition edge merely because paths intersect.

## 8. Interface with dynamic pair Kraft

The conditional theorem in `../dynamic_pair_kraft/REPORT.md` survives this
audit.  Its switch decoder is injective up to the stated chord/state fibre;
its width-`w` nested release is exact; and its final bound explicitly leaves
global switch and release reuse in `kappa,rho`.  The path theorem supplies a
local mass alternative:

\[
 \boxed{
 \text{constant internally-disjoint pair mass}
 \quad\text{or}\quad
 \text{a }1/O(r)\text{-mass internal state}.}      \tag{19}
\]

It does **not** by itself establish any of the following:

1. internally disjoint paths have the two opposite tangent signs required
   by the planar switch;
2. a heavy vertex can be entered without losing the record multiplicity
   and outside-prefix tags;
3. repeated heavy vertices across different outer contexts have
   `rho=2^o(r)` target-pair reuse.

Thus weighted Menger is a valid local branching lemma, not the missing
global reuse theorem.  The safe next statement must combine (19) with the
tangent comparability test and the low-width Boolean release; "nonnested or
bottleneck" without those qualifications is false.

## 9. Exact verification

Run

```bash
python3 phase2/loop/erdos838/agent_cyclic_stem_hw/lattice_rectangle_counter/verify_path_dag_menger.py
```

The verifier uses exact integer geometry and rational arithmetic.  It:

* checks weighted versions of (4) on explicit nonuniform path laws;
* constructs four projective-plane incidence DAGs and checks all path
  intersections and degrees;
* verifies every strict containment in the nested parabolic fans;
* checks exact first-divergence and nonforward counts for homogeneous,
  Proposition-26, and ramp--plateau product tries;
* constructs the exact intersecting-subset edge obstruction; and
* writes all coordinates and counts to `path_dag_menger_certificate.json`.
