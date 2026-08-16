# Erdős 838: pocket restart, exact positive lemma and obstructions

**Date:** 2026-08-14  
**Verdict:** a precise abstract laminar pocket-flow lemma is true, and the
exponential visible-pocket family from the one-step attack admits an exact
congestion-one restart once the incoming history is encoded in the selected
inner face.  Thus that family is not an obstruction to a multistep proof.
However, the visible pockets of even one fixed maximal convex face need not
be laminar, while the canonical laminar replacement (successive convex-hull
interiors) can have linear depth at activity one-half.  The universal
history-preserving Hall estimate needed to close the half-weight proof remains
open.

No solution of Erdős 838 is claimed here.  All face families include the
empty face unless a superscript `+` explicitly removes it.

## 1. The normalization a restart must satisfy

Write

\[
 Z_P(z)=\sum_{A\in\mathcal F(P)}z^{|A|}.
\]

In the local-flow normalization for

\[
 nZ_P(1/2)\leq 2Z_P(1),                              \tag{HW2}
\]

the membership and addable-point incidences associated with simplicial
covers can be charged first.  A rank-`k` target face then has residual
capacity

\[
 c_k=2-\frac{3k}{2^k}\geq\frac12.                    \tag{1}
\]

Every remaining bad incidence `(A,p)` has demand `2^{-|A|}`.  In particular,
a bad incidence of a maximal triangle has demand `1/8`.  The maximal-face
restart problem is to send these demands to residual face capacities without
polynomial congestion.

The stronger tilted-prefix formulation has different source weights.  The
geometric results below apply to both formulations, but the explicit decoder
in Section 4 is stated in the half-activity flow normalization (1).

## 2. A true abstract laminar pocket-flow lemma

There is a clean theorem behind the proposed recursion.  It also identifies
exactly which geometric premise fails.

Let `Q` range over a rooted laminar family of point subsets: any two members
are nested or disjoint.  Attach demand `d(Q)>=0` to node `Q`.  Demand attached
to `Q` is allowed to use every nonempty convex face supported in `Q`.  Give a
face `B` capacity `c(B)>=0`, consistently across all pockets, and put

\[
 C(Q)=\sum_{\varnothing\ne B\in\mathcal F(P),\ B\subseteq Q}c(B).
\]

> **Lemma 1 (laminar pocket flow).**  A fractional route exists whenever,
> for every node `Q`,
> \[
>   \sum_{R\text{ in the subtree of }Q}d(R)\leq C(Q).             \tag{2}
> \]
> If demands and capacities are integral, there is an integral route.

**Proof.**  Process the tree bottom-up.  By induction, all proper descendant
demands have been assigned inside their own face pools.  Pools belonging to
disjoint children are disjoint after the empty face is removed.  Their total
used capacity is precisely the already assigned descendant demand.  Condition
(2) leaves at least `d(Q)` unused capacity in the full pool of `Q`, to which
the demand at `Q` has unrestricted access.  Assign it there.  The same greedy
argument with indivisible unit slots proves the integral statement.  QED.

Thus laminarity plus the scalar subtree inequalities really would remove the
global Hall problem.  The issue is not the flow theorem; it is that the
natural visible pockets are not laminar and the canonical laminar pockets do
not automatically satisfy (2).

## 3. The geometry has a canonical nested hull path

For any finite set `S`, let `ext(S)` be the vertex set of its convex hull.

> **Lemma 2 (order-independent hull expansion).**  For every `S` and point
> `p`,
> \[
>  \operatorname{ext}(\operatorname{ext}(S)\cup\{p\})
>    =\operatorname{ext}(S\cup\{p\}).                            \tag{3}
> \]
> Consequently, starting with a convex face `A` and repeatedly replacing
> \[
> A\longmapsto\operatorname{ext}(A\cup\{p\})                    \tag{4}
> \]
> makes the convex hulls nested by inclusion, and after every point of `P`
> has been scanned the state is exactly `ext(P)`, independent of scan order.

**Proof.**  `S` and `ext(S)` have the same convex hull.  Adjoining `p`
preserves equality of the two hulls, hence their vertex sets agree.  Iterating
(3) proves the rest.  QED.

This gives a genuine well-founded geometric restart.  Exterior blocked
points strictly enlarge the hull; interior points leave it unchanged.  After
reaching `ext(P)`, recurse on

\[
 P_1=P\setminus\operatorname{ext}(P),\qquad
 P_{i+1}=P_i\setminus\operatorname{ext}(P_i).                    \tag{5}
\]

The sets in (5) are the canonical nested onion pockets.  What (3) does **not**
retain is the starting maximal face or the tangent history.  All such
histories can merge at the same global hull, so that information must either
be encoded in a target face or paid for fractionally by the inner capacity.

## 4. The exponential visible-pocket family is exactly restartable

The main one-step counterfamily has a much better multistep behavior than its
collapsed fibre suggests.  Put `N>=3`, `L=N-1`,

\[
 q_i=(i,i(L-i))\quad(0\leq i<N),\qquad p=(-1,N^2).                \tag{6}
\]

The `q_i` form a strict concave convex chain.  A direct orientation
calculation shows that whenever `i<j<k`, `q_j` lies strictly inside the
triangle `p q_i q_k`.  Hence

\[
 T_{ik}=\{p,q_i,q_k\}\qquad(i<k)                                \tag{7}
\]

is a maximal convex face: every third chain point is bad.

The visible-flip transitions are exact:

\[
 \operatorname{ext}(T_{ik}+q_j)=
 \begin{cases}
  T_{jk},&j<i,\\
  T_{ik},&i<j<k,\\
  T_{ij},&j>k.
 \end{cases}                                                     \tag{8}
\]

Thus at most two exterior flips expand every `T_{ik}` to the common full cage
`T_{0,N-1}`.  Its strict pocket is

\[
 Q=\{q_1,\ldots,q_{N-2}\},                                     \tag{9}
\]

and every subset of `Q` is a convex face.

> **Theorem 3 (congestion-one pocket decoder).**  For every `N>=11`, all
> \[
>  {N\choose2}(N-2)                                             \tag{10}
> \]
> bad incidences of all maximal triangles (7) can be injected into convex
> faces supported strictly inside the final pocket (9).  Under (1), the
> relative load at every used target is at most `1/4`.

**Proof.**  Lexicographically enumerate the triples `(i,k,j)` with `i<k` and
`j` different from both endpoints, and encode the enumeration rank as a
binary subset of the `N-2` points in (9).  At `N=11`,

\[
 {11\choose2}9=495\leq512=2^9.                                  \tag{11}
\]

The ratio of the left side of (11) at `N+1` to that at `N` is
`(N+1)/(N-2)<2` for `N>=6`, so (11) holds for every `N>=11`.  The map is an
injection and every target is convex.  Each source has demand `1/8`, whereas
(1) leaves at least `1/2` at every target.  QED.

This is not merely a cardinality check: (8) certifies a visible-flip path to
the cage, while the selected inner face stores the complete source identity.
The exact `N=11` verifier routes 495 incidences into 512 strict-pocket faces.

There is also a more geometric endpoint tag.  For fixed `i<k`, put

\[
 \mathcal R_{ik}=
 \{\{q_i,q_k\}\cup C:C\subseteq\{q_{i+1},\ldots,q_{k-1}\}\}.    \tag{12}
\]

The families in (12) are pairwise disjoint, since the least and greatest
chain indices recover `(i,k)`, and

\[
 |\mathcal R_{ik}|=2^{k-i-1},\qquad
 \sum_{B\in\mathcal R_{ik}}2^{-|B|}
   ={1\over4}\left({3\over2}\right)^{k-i-1}.                    \tag{13}
\]

So long intervals already restart locally with their tangent endpoints as
the identity tag; the binary decoder handles all short intervals together.
In particular, the exponential one-step fibre
`((3/2)^m-1)/4` is capacity, not a counterexample, once it is not collapsed.

## 5. Two rigorous obstructions to the naive recursion

### 5.1 Visible pockets of a fixed maximal face can cross

Take the nine-point convex face

\[
 A=\{(x,x^2):-4\leq x\leq4\}
\]

and add

\[
 p=(-8,-5),\qquad q=(-8,17).                                    \tag{14}
\]

The eleven points are in general position.  Adding `p` hides face vertices
with indices `{1,2,3}`, while adding `q` hides `{0,1,2}` (indices follow
increasing `x`).  Neither extension is convex, so `A` is maximal in this
eleven-point set.  The two hidden visible chains intersect but neither
contains the other.  Therefore:

> **Proposition 4.**  The visible-chain pockets attached to even one fixed
> maximal planar convex face need not form a laminar family.

This kills a direct application of Lemma 1 to tangent intervals.  Replacing
arbitrary intervals by dyadic intervals does not by itself fix congestion:
a central dyadic block can lie in quadratically many endpoint intervals unless
the endpoint identity is retained.

### 5.2 The canonical laminar onion recursion can be linearly deep

Let `T_1,...,T_r` be exact rational triangles with

\[
 \operatorname{conv}T_{i+1}
 \subset\operatorname{int}\operatorname{conv}T_i.               \tag{15}
\]

The verifier uses the shrinking, rotating family

\[
 10^{-i}R^i\{(-3,-2),(3,-2),(0,4)\},\qquad
 R={1\over5}\begin{pmatrix}3&-4\\4&3\end{pmatrix}.             \tag{16}
\]

For any selected subset, every fully selected triangle forces its own onion
layer: a deeper full triangle cannot lose a vertex before a containing full
triangle does.  Hence if `D` is onion depth,

\[
 \mathbb E_{\rm uniform}D\geq r/8.                              \tag{17}
\]

The Boolean activity-`1/2` law is independent inclusion with probability
`1/3`, because normalizing weights `2^{-|S|}` over all subsets gives
`Pr(x in S)=1/3`.  The same proof yields

\[
 \mathbb E_{\rm Boolean,,1/2}D\geq r/27.                       \tag{18}
\]

Thus the canonical nested pockets are not shallow even at the exact activity
of the half-weight attack.  Any proof which loses a fixed factor at every
restart level fails exponentially on (16).  A successful route has to be a
global flow or have per-level losses telescoping to `n^{o(1)}`.

## 6. Large pockets have ample *local* capacity

The established universal lower bound gives, for every `m`-point pocket `Q`,

\[
 V(Q)\geq2^{(1/4-o(1))(\log_2m)^2}.                              \tag{19}
\]

This immediately yields a useful reduction.

> **Lemma 5 (macroscopic pocket capacity).**  Suppose at most `n^C` labeled
> source units enter one pocket `Q`, each unit has demand at most one, and
> every convex target face has capacity at least a fixed positive constant.
> For every fixed `delta>0`, local constant-congestion routing is possible for
> all sufficiently large `n` whenever
> \[
>  \log_2|Q|\geq(2\sqrt C+\delta)\sqrt{\log_2n}.                  \tag{20}
> \]

**Proof.**  Choose the `o(1)` in (19) small relative to `delta`.  Then the
right side of (19) is `n^{C+eta}` for some `eta>0`, so there are more target
faces than source labels.  Inject the labels into faces and use the fixed
capacity lower bound.  QED.

For the residual capacities (1), the fixed constant is `1/2`.  Therefore
polynomially many histories cannot overload a genuinely macroscopic isolated
pocket.  The hard cases are small pockets and, more importantly, simultaneous
use of overlapping pockets.  Lemma 5 is local and does not solve that global
Hall problem.

## 7. The corrected remaining lemma

For each bad maximal-face incidence `s=(A,p)`, let `Gamma(s)` be the convex
faces reachable after hull expansion and recursive pocket restart while
retaining an endpoint/tangent code.  A theorem strong enough for the current
attack is the weighted Hall inequality

\[
 \sum_{s\in X}2^{-|A_s|}
 \leq n^{o(1)}
 \sum_{B\in\bigcup_{s\in X}\Gamma(s)}c_{|B|}                    \tag{21}
\]

for every collection `X` of maximal-face bad incidences.  Lemma 1 proves
(21) from scalar subtree inequalities when the allowed pocket pools are
laminar.  Theorem 3 proves it with constant loss for the visible-pocket
counterfamily.  Proposition 4 shows that arbitrary visible pools are not
laminar, and (18) rules out multiplying a constant loss down the canonical
onion chain.

So the precise unresolved step is no longer “restart somehow inside a
pocket.”  It is:

* construct the allowed sets `Gamma(s)` with a decodable tangent history;
* prove (21) across crossing pockets; and
* make the losses additive/telescoping across a potentially linear onion
  depth.

Any proposed completion can now be tested against the two exact families in
Sections 4 and 5.

## 8. Verification

From the repository root, run

```bash
python3 -m py_compile \
  phase2/loop/erdos838/agent_pocket_restart/pocket_restart_audit.py

python3 \
  phase2/loop/erdos838/agent_pocket_restart/pocket_restart_audit.py \
  > /tmp/pocket_restart_audit.json
```

The checker verifies exact general position and hull identities, the
nonlaminar eleven-point certificate, all 495 maximal-triangle transitions and
the 495-to-512 decoder, 71,680 instances of (3), and the onion-depth
distribution through five nested triangles under both uniform and
activity-half Boolean laws.  It also writes `certificate.json` beside the
script.
