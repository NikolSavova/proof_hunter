# Stretchable fresh-partner resets: exact load/chronology dichotomy

**Date:** 2026-08-15. All point sets are in general position and all faces
are nonempty ordinary convex subsets.

## Verdict

The matching, pair-node, and stretchability hypotheses alone do **not**
force the natural global cup/cap candidate obtained by choosing one
endpoint from every pair node. There is a scalable rational
counter-regression obtained by putting one copy of the exact twelve-point
colorful obstruction on every class triple. It has a size-`m` bad-circuit
matching on every class pair, global pair-node degree one, no pair-node
triangles, and physical-label load one, yet no such full endpoint
transversal is ordinary. By shrinking the gadgets around a classical
Erdos--Szekeres extremal macro set, every ordinary partial endpoint
transversal has rank only `O(log G)`, where `G` is the number of gadgets.

What is forced is an exact source-size/chronology alternative and an
injective mixed-face bank. Let `Y_1,...,Y_t` be the classes, let every
`M_ij` be a label-disjoint matching of `m` bad `2+2` circuits, let every
physical pair node have global degree one, and let every physical label
occur in at most `lambda` selected circuits. Then

\[
 |Y_i|\ge {2m(t-1)\over\lambda},                       \tag{1}
\]

and the canonical five-point releases over all third classes give

\[
 \boxed{\quad
 B_4=m\sum_{i<j}\sum_{k\notin\{i,j\}}|Y_k|
 \quad}                                                \tag{2}
\]

distinct ordinary `2+1+1` faces, with physical decoder load one. For equal
class size `g`, this is

\[
                  B_4=m\binom t2(t-2)g.                \tag{3}
\]

The counter-regression attains equality in (1) with `lambda=1`. Thus it
escapes global synchronization by paying a factor `t-1` in physical source
support, and its circuit identity is completely decoder-visible. At the
opposite full-support endpoint `g=2m`, every label must have load `t-1`;
then each class contains exactly

\[
                         2m\binom{t-1}{2}              \tag{4}
\]

two-neighbour partner-turn records. The tangent construction lies at this
high-reuse endpoint and pays the much larger all-lower cup bank
`D^(m(t+1))` after substitution.

Consequently the broad Ramsey/allowable-sequence implication is false even
for partial petal traces of linear rank.
The exact remaining geometric problem is narrower: **perfect or near-perfect
class-pair matchings on a common `2m`-label support, with load near `t-1`.**
The present theorem does not decide whether every such high-reuse
stretchable reset has a tangent-like global bank. The twelve-point example
does not satisfy that full-support condition, and no global closure is
claimed.

## 1. Universal source-size and itinerary ledger

For a label `x in Y_i`, let `d_i(x)` be the number of selected circuit
edges containing it. A matching `M_ij` uses exactly `2m` labels of `Y_i`,
so

\[
              \sum_{x\in Y_i}d_i(x)=2m(t-1).           \tag{5}
\]

Since `d_i(x)<=lambda`, (1) follows. This is sharp, not an averaging
artifact.

The number of visible two-neighbour turns through labels of class `i` is

\[
                   K_i=\sum_{x\in Y_i}\binom{d_i(x)}2. \tag{6}
\]

Each record retains the physical label and its two distinct physical
partner pairs. Pair-node degree one recovers the two neighbouring circuit
edges, so (6) is a literal chronology count. If `S=2m(t-1)`, convexity of
`binom(d,2)` gives, with `S=q|Y_i|+r`, `0<=r<|Y_i|`,

\[
 K_i\ge (|Y_i|-r)\binom q2+r\binom{q+1}2.              \tag{7}
\]

At `|Y_i|=2m`, the matching condition also gives `d_i(x)<=t-1`, while
the average in (5) is `t-1`; hence every load is exactly `t-1` and (4)
follows. At the load-one endpoint `|Y_i|=2m(t-1)`, (7) permits `K_i=0`.
This is the exact support-inflation versus partner-chronology ramp.

The records in (6) are not asserted to be faces. The twelve-point
obstruction shows why two circuit incidences cannot simply be composed by
choosing one endpoint from every pair. The ordinary payment that always
survives is (2).

## 2. A global injective `2+1+1` release bank

Fix `Q in M_ij` and `y in Y_k`, where `k` is different from `i,j`.
Every five planar points contain four in convex position. Since `Q` itself
is bad, a convex four-subset of `Q union {y}` contains `y` and deletes one
label of `Q`. Choose the first successful deletion in a fixed physical
label order and call the output `R(Q,y)`.

The output has class occupancy `2+1+1`. Its doubled class trace is one of
the two physical pair nodes of `Q`. Global pair-node degree one recovers
the unique circuit edge `Q`. The class outside the two endpoints of `Q`
then identifies `y`. Therefore

\[
                    (Q,y)\longmapsto R(Q,y)            \tag{8}
\]

is injective even while all class triples and all circuit matchings vary.
There are `m` choices of `Q` for each pair `i<j` and `|Y_k|` external
labels for each third class, proving (2). If global pair-node degree is
at most `Delta` instead, the same decoder has load at most `Delta`.

This improves the fixed-three-class load-three ledger to load one under
the actual global fresh-pair hypothesis. It is still only a polynomial
bank. It neither retains a rich internal child face nor supplies the
half-coefficient target by itself.

## 3. Scalable stretchable colorful counter-regression

Let `T` be the exact twelve-point configuration from
`COLORFUL_PAIR_ENDPOINT_TRANSVERSAL_BARRIER.md`. It has three four-point
classes, two physical pair nodes in each class, and one bad circuit on
each class pair. The three circuits use six distinct pair nodes. Every one
of the `2^6` choices of one endpoint from each node is nonordinary.

Fix `t>=3` and `r>=1`, and put `G=r binom(t,3)`. The classical cup--cap
lower construction gives rational `x`-ordered center sets

\[
 |E_{a,b}|=\binom{a+b-4}{a-2}                         \tag{8a}
\]

with no `a`-cup and no `b`-cap. It follows by the standard two-separated-
block recursion and the binomial recurrence. Every convex subset is the
union of its lower cup and upper cap, sharing their endpoints. Choosing
`a=b=h` and then taking a `G`-point subset gives a rational center set whose
maximum convex rank is at most

\[
                         H=2h-4=O(\log G).             \tag{8b}
\]

For every unordered class triple `{i,j,k}` and every copy index
`a in [r]`, assign one center and place a sufficiently small,
orientation-preserving rational affine copy of `T` around it, identifying
its class colours with `i,j,k`. Use generic distinct rational shears and
then choose a small rational common scale. Every triple using three
different gadget cells has the center-set sign, while every local colorful
sign is preserved. The finitely many remaining collinearities are avoided
by the generic shears/scale. This produces one global rational
general-position configuration.

For a fixed class pair `{i,j}`, there is one circuit for every third class
and every copy. Therefore

\[
              m=r(t-2),\qquad
              |Y_i|=4r\binom{t-1}{2}=2m(t-1).          \tag{9}
\]

The circuits of a fixed pair are label-disjoint. In fact every physical
label and every physical pair node occurs in exactly one selected circuit,
so label load and pair-node degree are both one and the auxiliary pair
graph is a matching.

Any global choice of one endpoint from every selected physical pair node
restricts on each copy of `T` to one of its 64 bad colorful six-sets. That
six-set remains a subset of the global choice, so heredity makes the global
choice nonordinary. This proves the promised scalable stretchable failure.
Because the example is realized by rational straight lines, passing to its
allowable sequence cannot restore the missing transversal.

The complete local partial-endpoint rank vector, allowing a node to be
omitted or represented by one endpoint, is

\[
                  (1,12,60,160,114,16,0).              \tag{9a}
\]

In particular, if there are `G=r binom(t,3)` gadgets, any ordinary global
partial endpoint trace activates a convex set of macro centers: otherwise
one selected endpoint from each cell of a bad macro four-set would be a
bad physical four-set. Hence at most `H` gadgets are active. Equation
(9a) says an active gadget contributes at most five endpoint labels, so

\[
       \operatorname{rank}(F)\le5H=O(\log G)           \tag{9b}
\]

out of `6G` pair nodes. Moreover the number of possible endpoint traces is
at most

\[
             \sum_{q=0}^{H}\binom Gq362^q
                       =2^{O((\log G)^2)},             \tag{9c}
\]

versus `729^G` unrestricted empty/endpoint words. These are upper bounds;
some locally admissible traces can still fail across gadgets.

The construction is sharp for the load ledger: (9) is equality in (1)
at `lambda=1`. It also pays the load-one bank (2), namely

\[
  r(t-2)\binom t2(t-2)\,2r(t-1)(t-2)                  \tag{10}
\]

distinct rank-four faces. Each local twelve-point copy has `709` ordinary
faces, giving the separate ambient lower bound
`709 r binom(t,3)`. Thus this is not presented as a low-face construction.
Its exact role is to rule out full global endpoint synchronization in the
source-inflated branch.

This construction only realizes matching sizes divisible by `t-2`; that
is enough for an unbounded scalable regression. Padding can change finite
sizes, but no padding claim is needed here.

## 4. Audit of the two boundary models

### Tangent reset

The tangent construction has `|Y_i|=2m` and `d_i(x)=t-1` for every label.
It saturates the high-reuse end of (5)--(7). Its global pair nodes still
have degree one, so (2) is injective. In addition, its transitive tangent
signs make all lower `L`-cells plus the full top class a cup. After
arbitrary `D`-point substitution this gives `D^(m(t+1))` ordinary faces.
That extra bank is geometric; it is not a consequence of the incidence
ledger alone.

### Twelve-point colorful reset

For `t=3,r=1`, (9) gives `m=1`, class size four, and label load one: this
is exactly the twelve-point example. It has no colorful six-face, and its
one-gap counts are `(0,0,8,8,0,0)`. Nevertheless it has `709` total faces
and the universal bank (2) gives 12 distinct rank-four releases. Thus it
kills endpoint composition, not the canonical mixed-face payment.

The contrast isolates the missing hypothesis. Tangent uses every label in
every neighbouring matching; the colorful example partitions fresh labels
among neighbours. A future Ramsey theorem must quantitatively assume or
derive near-full common support/high label reuse. Stretchability, matching
size, pair-node degree, and absence of triangles do not supply it.

## 5. Exact verification

Run

```text
python3 phase2/loop/erdos838/agent_many_class_partner_reset/verify_stretchable_reset_chronology_barrier.py
```

The verifier uses exact integer/rational arithmetic. It rechecks the
twelve-point `64/64` colorful failures and one-gap vector, constructs the
`t=5,r=1` blow-up with 120 points around ten macro centers of maximum
convex rank five and checks global general position, 30 selected bad
circuits, all matching/load/degree claims, 640 local colorful failures, the
global partial-endpoint rank bound `25<60/2`, and all 2,160 injective
canonical releases. It also
checks the high-reuse `t=5,m=4` tangent endpoint, its 24-role all-lower cup,
48 partner-turns per class (240 total), and 960 injective releases.

The coordinate construction and proof scale for every `t,r`; the finite
instances are exact regression tests, not exhaustive evidence for the
uniform theorem.
