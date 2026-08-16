# Realized chamber transitions: a decoded cycle telescope or a role forest

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

Diffuse boundary-chain chambers do not by themselves force a profile cycle.
The missing distinction is between a **one-ended chamber query** and an
actual **two-ended transition module**.

A projected tag \(A_\sigma(D)\cup\{z\}\) certifies that chamber \(\sigma\)
was queried and physically retains \(z\).  It uses cap information at one
chamber.  The endpoint-potential telescope, however, requires an ordinary
face bank which simultaneously contains a cap profile at its tail chamber
and a cup profile at its head chamber.  Only such a bank is an edge in the
energy graph.

This yields an exact theorem.  For one physical child \(Q\), let the
vertices be realized projection chambers.  An edge \(e:\sigma\to\tau\) is
admitted only when the same ambient configuration contains a decoded
ordinary-face bank of size

\[
 |\mathcal B_e|
 \ge {C_\sigma(Q)U_\tau(Q)S_e\over\Lambda_e},          \tag{1}
\]

where \(S_e\) is a recoverable carrier/context reservoir and
\(\Lambda_e\) is the full output load, including the edge and branch tags.
If this directed graph contains a cycle \(\mathcal C\), then one actual edge
bank on the cycle satisfies

\[
\boxed{
 \log|\mathcal B_e|
 \ge {1\over|\mathcal C|}
 \left(
 2\sum_{\sigma\in\mathcal C}E_\sigma
 +\sum_{e\in\mathcal C}\log S_e
 -\sum_{e\in\mathcal C}\log\Lambda_e
 \right),
}                                                       \tag{2}
\]

where

\[
 E_\sigma={\log C_\sigma+\log U_\sigma\over2}
      \ge {1\over2}\log V(Q).                          \tag{3}
\]

All banks in (2) are faces of the same configuration; no reflection or
alternative embedding is used.  Decoder losses are explicitly subtracted.

Equivalently, repeatedly prune chamber vertices with no incoming or no
outgoing realized two-ended edge.  If a nonempty directed core remains,
(2) applies to a cycle in that core.  If the core is empty, the transition
graph is a DAG and admits a topological rank.  The exact surviving state is
therefore a **role forest**, not an unquantified failure of cyclicity.

There is a scalable rational planar warning: one convex source polygon can
be queried from linearly many distinct visibility chambers, with every
projected tag an actual decoded face and every full tag bad, while the
query graph is an out-star.  Thus even genuinely realized chamber
diffuseness does not imply a return edge.  In that example the exterior
query labels themselves are in convex position, so their Boolean face bank
pays exponentially; it is not a live-normalized counterexample.

Consequently the remaining live statement is sharper than “diffuse
chambers make a cycle”:

> near-complete physical-label branching must either upgrade enough
> one-ended projected tags to two-ended transition modules with a nonempty
> directed core, or the resulting chamber-ranked role forest must expose an
> ambient face bank while retaining the carrier/context mark.

The cycle branch is closed here with exact loads.  The forest-to-ambient
promotion is still open.  This aligns with the independent role-forest
entropy reduction: excess rank and near-complete all-deletion can live
entirely in an acyclic chamber hierarchy unless planarity supplies the
missing ambient bank.

## 1. Query graph versus energy graph

Fix an actual planar configuration \(P\) containing a physical child \(Q\).
Let \(\Sigma(Q)\) be the finite set of generic projection chambers of \(Q\).

A **one-ended query edge** records an actual family of projected tag faces

\[
                     A_\sigma(D)\cup T,                \tag{4}
\]

where \(A_\sigma(D)\) is a cap/boundary chain in chamber \(\sigma\) and the
trace \(T\) recovers the branch label.  This is the output of
PROJECTED_SOURCE_CROSS_BRANCH_STORAGE_GATE.  Its count is controlled by a
cap projection and its source-fibre load.

A **two-ended transition edge** \(e:\sigma\to\tau\) is stronger.  It
consists of an actual same-configuration bank indexed by

\[
 (A,B,s)\in
 \mathcal C_\sigma(Q)\times\mathcal U_\tau(Q)\times\mathcal S_e, \tag{5}
\]

with output decoder load at most \(\Lambda_e\).  Therefore (1) follows.
The output need not reveal the index tuple uniquely; all collisions,
including collisions between branch descriptions or edge labels, belong in
\(\Lambda_e\).

Definition (5) is deliberately strict.  A collection of cap projections in
many chambers is not silently promoted to a Cartesian cap--cup module.
That promotion is the geometric content still missing from the live proof.

If an output does not reveal which of at most \(R\) edges produced it, edge
colouring or guessing increases \(\Lambda_e\) by at most \(R\).  Since one
physical \(N\)-point child has at most
\(\binom N2+1\) projection chambers, this costs at most \(O(\log N)\) bits
for a single chosen edge.  Repeating that guess through a depth-\(\Theta(L)\)
forest is not free; it costs \(\Theta(L^2)\), which is why the whole branch
history must remain explicit.

## 2. Exact directed-cycle telescope

For each chamber define

\[
 \rho_\sigma={\log U_\sigma-\log C_\sigma\over2}.       \tag{6}
\]

Then

\[
 \log C_\sigma=E_\sigma-\rho_\sigma,\qquad
 \log U_\tau=E_\tau+\rho_\tau.
\]

Taking logarithms in (1) gives

\[
 \log|\mathcal B_e|
 \ge E_\sigma+E_\tau+\rho_\tau-\rho_\sigma
       +\log S_e-\log\Lambda_e.                        \tag{7}
\]

Sum (7) around a directed cycle.  Every chamber occurs once as a tail and
once as a head, so the \(\rho\)-terms cancel and the energy terms occur
twice:

\[
 \sum_{e\in\mathcal C}\log|\mathcal B_e|
 \ge 2\sum_{\sigma\in\mathcal C}E_\sigma
       +\sum_{e\in\mathcal C}
          (\log S_e-\log\Lambda_e).                    \tag{8}
\]

At least one summand is at least the average, proving (2).

For every chamber, the upper/lower hull decoder injects ordinary faces of
\(Q\) into cap--cup pairs, so

\[
                         V(Q)\le C_\sigma(Q)U_\sigma(Q). \tag{9}
\]

This proves (3).  If the same physical child occurs at every vertex, (2)
therefore simplifies to

\[
 \log|\mathcal B_e|
 \ge \log V(Q)
   +{1\over|\mathcal C|}\sum_{f\in\mathcal C}
             (\log S_f-\log\Lambda_f).                 \tag{10}
\]

Thus any positive average recoverable carrier surplus becomes a genuine
same-configuration gain over the child bank.

No union over cycle edges is needed.  One edge bank is already large, so
cross-edge overlap is irrelevant.  The only overlap parameter is its
literal decoder load \(\Lambda_e\).

## 3. Directed-core pruning

For a finite directed graph \(G\), repeatedly delete a vertex of indegree
zero or outdegree zero, together with its incident edges.  The final
directed \(1\)-core is independent of deletion order.

* If the core is nonempty, every remaining vertex has an outgoing edge.
  Following outgoing edges eventually repeats a vertex and produces a
  directed cycle.  The cycle consists only of actual two-ended transition
  edges, so Section 2 applies.
* If the core is empty, \(G\) contains no directed cycle.  A topological
  order exists, and every transition strictly increases its rank.

This gives an exact cycle-or-role-forest dichotomy.  High outdegree at many
vertices is insufficient: a layered \(q\)-ary DAG of depth \(s\) has
outdegree \(q\) at every nonterminal state and no directed core.  The
increasing-prefix trie in HIGH_TRANSVERSAL_PASCAL_PREFIX_DAG_BARRIER is
precisely such a ranked object, with remaining face rank as a Lyapunov
function.

For the live near-complete all-deletion branch, the natural topological rank
is the number of deleted physical labels.  Hence cycle closure requires an
actual transition which returns to a previously available chamber state
without consuming another source label.  Mere repetition of a chamber name
on two different prefix branches does not do this: the carrier/context tags
differ and must be included in the decoder load.

## 4. A scalable rational diffuse-chamber out-star

This construction proves that realized chamber diversity alone does not
create a return transition.

For \(m\ge8\), take the convex source chain

\[
                         Q_i=(i,i^2),\qquad0\le i<m.    \tag{11}
\]

Put \(q=\lfloor(m-1)/2\rfloor\), and initially take exterior query points

\[
                         z_j=(j+1/2,-7/3),\qquad0\le j<q. \tag{12}
\]

For every \(j\), the convex hull of \(Q\cup\{z_j\}\) omits a nonempty
interval of the parabola vertices.  These omitted intervals are distinct
as \(j\) varies.  Equivalently, the sign vectors

\[
              \bigl(\operatorname{sgn}\chi(Q_a,Q_b,z_j)\bigr)_{a<b}
                                                               \tag{13}
\]

are distinct, so the \(z_j\) lie in distinct cells of the line arrangement
of \(Q\).  The hull vertices

\[
 A_j=\operatorname{vert}\operatorname{conv}(Q\cup\{z_j\})
                         \setminus\{z_j\}               \tag{14}
\]

give an actual projected tag \(A_j\cup\{z_j\}\), while the full tag
\(Q\cup\{z_j\}\) is nonconvex.

Choose a sufficiently small positive rational \(\delta\), avoiding the
finitely many collinearity values, and perturb

\[
 z_j=\left(j+{1\over2},
       -{7\over3}+\delta(j+1)(j+2)\right).              \tag{15}
\]

All strict hull and chamber relations persist, and the total configuration
is in general position.  The query points themselves lie on a strictly
convex quadratic chain.

Let \(v_0\) be the source state and \(v_j\) the chamber containing \(z_j\).
The actual query graph has the \(q\) edges

\[
                              v_0\longrightarrow v_j.  \tag{16}
\]

Each edge tag is decoded by its physical label \(z_j\), and every subset of
\(A_j\cup\{z_j\}\) is an ordinary face.  The graph has \(q\) distinct
realized head chambers but is an out-star, hence its directed core is empty.
There is no actual return module.

This example is intentionally not advertised as live.  The \(z_j\) are in
convex position, so they alone contribute \(2^q\) ordinary faces.  It
calibrates the desired positive theorem: a successful live argument must
show that every diffuse chamber DAG similarly pays through an ambient bank,
or else produces a two-ended return edge.  Graph theory and chamber
diversity alone cannot do so.

## 5. Consequence at the excess-rank role forest

The near-complete all-deletion branch has source rank
\(s>cL\) and a physical-label branch at almost every deletion level.
Form its chamber graph using only actual projected-tag transitions whose
carrier/context marks are retained.

* A nonempty two-ended directed core closes by (10), with the exact average
  carrier surplus and decoder loss.
* If only one-ended queries are known, or the two-ended core is empty, the
  branch remains a ranked DAG.  Positive-density \(n^\varepsilon\)
  outdegree and many distinct chambers do not change that conclusion.

The precise remaining planar lemma is therefore:

> a live, near-complete, excess-rank chamber DAG with retained
> carrier/context marks either contains a two-ended return module, or its
> physical labels contain a decoded ambient ordinary-face bank of the
> missing \(n^{\Theta(\log\log n)}\) scale.

The concentrated nonseparated-carrier branch and the diffuse role-forest
branch are now cleanly disjoint.  This report closes the cycle branch and
leaves only the stated forest-to-ambient promotion.

## 6. Verification

**verify_realized_chamber_cycle_or_forest.py** performs:

1. exhaustive exact exponent checks of (7)--(10) on directed cycles;
2. exhaustive directed-core/cycle equivalence on all loopless digraphs
   through four vertices and explicit high-branching layered DAGs;
3. exact rational construction of (11)--(15) for several scales, checking
   general position, distinct line-arrangement chambers, bad full tags,
   good projected tags, exact edge decoding, and the empty directed core;
   and
4. verification that the query labels form an ambient convex face bank,
   recording why the geometric out-star is not live-normalized.
