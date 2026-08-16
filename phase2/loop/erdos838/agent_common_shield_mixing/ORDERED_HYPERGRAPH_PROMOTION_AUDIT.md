# Ordered-hypergraph partitioning does not by itself promote radial containers

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The explicit constants in Furedi--Jiang--Kostochka--Mubayi--Verstraete,
*Partitioning ordered hypergraphs* ([arXiv:1906.03342](https://arxiv.org/abs/1906.03342)),
are harmless at the E838 logarithmic-rank scale.  One application, or two
successive applications in the two tangent-coordinate orders, costs only

\[
                         2^{O(r\log r)}=2^{O(L\log L)}.       \tag{1}
\]

This does **not** give the missing oriented container promotion.  There are
three separate, rigorously verified failures.

1. The extracted part size `m` is uncontrolled.  The retained edge count is
   `cM(m/n)^alpha`; preserving a `2^{Theta(L^2)}` family up to the loss in
   (1) requires `m>=n/L^{O(1)}`, while the theorem permits much smaller `m`
   and explicitly says this can be necessary.
2. At the live rank, interval `r`-partite extraction is unavailable.  If
   `r=kappa L`, then eventually `r!>n`, whence
   `binom(n,r)<n^(r-1)`.  Thus no `r`-uniform family has density exponent
   `alpha>=r-1`, the threshold for taking `k=r`.
3. More decisively, even simultaneous interval `r`-partiteness in increasing
   left-tangent order and decreasing right-tangent order does not imply that
   every ambient transversal is a rooted convex face.  It excludes pairwise
   nesting, but convexity also has a three-point cup/cap condition.  Section
   4 gives an exact rational general-position counterexample at `r=3`.

There is one useful positive interface.  If every produced face retains at
least one point from every selected dyadic interval part, its canonical
partition-component ID has load at most `L+1`, or `(L+1)^2` after the two
orders.  Hence all such component banks may be summed, rather than
pigeonholed.  If even one linear number of interval witnesses is erased,
the load can be `n^{Theta(k)}`.  A planar convex-position example realizes
this exactly.  Therefore a weighted Cauchy recursion does not repair the
theorem in general: it works precisely for **part-covering** output banks.

Finally, when `k<r`, all quadratic entropy may lie inside one multiply
occupied part.  A scalable rooted convex example is already interval
`k`-partite in both orders, has `binom(N,k)=2^{Theta(L^2)}` sources, but only
`N` one-per-part projections.  Its large cell is itself a Boolean convex
shield, so this is not an EIC counterexample.  It identifies the missing
input exactly: after the FJKMV macro partition one still needs the local
cup/cap/profile reservoir theorem, with witnesses from every macro part
retained so that the macro component can be decoded.

## 1. Exact uniform form of the partition theorem

For `2<=k<=r`, put

\[
 C_{k,r}=\sum_{j=k}^{r}\binom{2k-2}{j},\qquad
 A_{k,r}={C_{k,r}\over(k-1)!}.                            \tag{2}
\]

Theorem 1.1 of the paper partitions the edges by scales
`0<=i<=floor(log n)`.  At scale `i`, the class is a union of at most

\[
                         A_{k,r}2^{i(k-1)}                 \tag{3}
\]

interval `k`-partite `r`-graphs, whose interval parts have size at most
`ceil(n/2^i)`.  Equal part-tuples can be merged, and then the components
may be made edge-disjoint by assigning an edge to its first eligible tuple.

Let `H` have

\[
                  M=d n^\alpha,\qquad k-1<\alpha\le r.    \tag{4}
\]

The proof of Theorem 1.2, rather than its fixed-parameter `Omega` notation,
gives a component with parts of size at most some `m<=n` and

\[
 e(H')\ge c(\alpha,k,r)d m^\alpha,
 \quad
 c(\alpha,k,r)=
 { (k-1)!\bigl(1-2^{k-1-\alpha}\bigr)\over C_{k,r}}.     \tag{5}
\]

At the boundary `alpha=k-1`, an additional factor `1/(1+log n)` is
necessary.  We do not use the boundary case.

In the live substitution

\[
 n=2^L,\quad r=\kappa L,\quad M=2^{aL^2}=n^{aL},
 \quad k=\lfloor aL\rfloor,                              \tag{6}
\]

we have `alpha-(k-1) in [1,2)`.  Therefore the parenthesis in (5) is
between `1/2` and `3/4`.  Since

\[
 C_{k,r}\le 2^{2k-2},\qquad 1\le(k-1)!\le k^k,           \tag{7}
\]

it follows uniformly that

\[
                         |\log c|=O(k\log k)=O(L\log L). \tag{8}
\]

The fact that `c` can exceed one for large `k` is not a contradiction:
the normalization `d=M/n^alpha` can be much smaller than one.  Only the
logarithmic magnitude of `c` is relevant here.

## 2. The exact double-order extraction

Apply (5) first in the left-tangent order and let its part size be `m_1`.
The surviving vertex support has size

\[
                              N_1\le r m_1.               \tag{9}
\]

Writing `e(H_1)=d_1N_1^alpha`, (5) and (9) give

\[
                       d_1\ge {c d\over r^\alpha}.        \tag{10}
\]

Apply the same theorem to `H_1` in the right-tangent order.  The second
subgraph still has the first interval-partite property, and for some second
part size `m_2` it satisfies

\[
 \boxed{
 e(H_2)\ge c^2r^{-\alpha}d m_2^\alpha
          =c^2r^{-\alpha}M\left({m_2\over n}\right)^\alpha.}
                                                                    \tag{11}
\]

For `alpha,r=Theta(L)`,

\[
                |\log(c^2r^{-\alpha})|=O(L\log L).       \tag{12}
\]

Thus simultaneous reverse-order refinement really does lose only
`2^{O(L log L)}` **apart from the final scale factor**.  Formula (11) is
the exact statement that should be used; omitting `(m_2/n)^alpha` is the
fatal parameter error.  Retaining an `M/2^{O(L log L)}` fraction requires

\[
 \alpha\log(n/m_2)=O(L\log L),\quad	ext{hence}\quad
                         m_2\ge n/L^{O(1)}.               \tag{13}
\]

There is no such conclusion in the theorem.  Its own discussion notes
examples in which `m=O(n^{1-1/alpha})` is necessary.

For comparison, summing the raw component bound (3) gives

\[
 T\le A_{k,r}\sum_{i=0}^{L}2^{i(k-1)}.                  \tag{14}
\]

In the exact calibration `alpha=k`, `r=2k`, `k=Theta(L)`, and `M=n^k`,

\[
 \log {M\over T}
 =L+\log (k-1)!-\log C_{k,r}+O(1)
 =\Theta(L\log L).                                      \tag{15}
\]

Consequently direct pigeonholing among every Theorem 1.1 component only
guarantees a component of absolute size `2^{Theta(L log L)}`, not a
`2^{-O(L log L)}` fraction of `M`.  These are very different assertions.

## 3. Why the favorable `k=r` case is absent

Taking `k=r` in Theorem 1.2 requires `alpha>=r-1`.  But

\[
                  M\le\binom nr < {n^r\over r!}.          \tag{16}
\]

For `r=kappa L`, Stirling gives `log(r!)=Theta(L log L)>L=log n`, so
`r!>n` eventually.  Equation (16) then gives `M<n^{r-1}` and
`alpha<r-1`.  This obstruction is intrinsic, not a loss in the theorem's
constant.

Even if an external argument somehow supplied an interval `r`-partite
family, the geometric promotion proposed in the prompt would still be
false, as follows.

## 4. Exact cup/cap obstruction after both tangent orders

Fix the root edge

\[
                         u=(-1,0),\qquad v=(1,0).          \tag{17}
\]

For positive tangent coordinates `(L,R)`, use the inverse map

\[
             p(L,R)=\left({L-R\over L+R},-{2\over L+R}\right).       \tag{18}
\]

Take the two triples

\[
\begin{aligned}
 A&=(p(2,22),p(9,13),p(17,4)),\\
 B&=(p(3,23),p(10,14),p(18,5)).                           \tag{19}
\end{aligned}
\]

The six points lie in three cells whose `L`-intervals are strictly
increasing and whose `R`-intervals are strictly decreasing:

\[
 [2,3]\times[22,23],\quad [9,10]\times[13,14],\quad
 [17,18]\times[4,5].                                     \tag{20}
\]

All eight points `u,v,A,B` are in general position.  Direct rational
orientation tests give

\[
          u\cup A\cup v\text{ convex},\qquad
          u\cup B\cup v\text{ convex},                  \tag{21}
\]

but the mixed transversal

\[
                 (p(2,22),p(10,14),p(17,4))              \tag{22}
\]

is not convex with `u,v`.  Thus the two-edge hypergraph `{A,B}` is
simultaneously interval `3`-partite in the `L` order and the reverse `R`
order, with the same three occupancy cells and one point in every cell,
yet its ambient Cartesian transversal closure contains a nonface.

The conceptual error is precise.  Reverse cell order makes points in
different cells incomparable under the two-point nesting order.  A rooted
set of three or more pocket points must additionally form the correct
lower cup.  That condition is ternary and is not implied by the two linear
orders.  Fixing the occupancy composition or its monotone cell path, at a
cost at most `2^{O(r log r)}`, does not fix the cup/cap signs: (19) already
has the unique occupancy vector `(1,1,1)`.

## 5. Summing all dyadic components: the exact cover criterion

The proof of Theorem 1.1 uses the dyadic interval partitions `I_i`.  An
edge is placed at the least scale `i` at which it meets at least `k` cells,
and a component is indexed by the exact cells of `I_i` met by its edges.
Merge components with equal part-tuples and choose a canonical assignment
when necessary.

> **Lemma 1 (part-cover component decoder).**  Suppose an output face `W`
> from a scale-`i` component meets every selected interval part of that
> component.  For fixed `i`, `W` determines the component: its selected
> parts are exactly the cells of `I_i` met by `W`.  Across all scales the
> decoder load is at most `L+1`.  After independent canonical
> decompositions in two vertex orders, an output meeting every part in
> both decompositions has load at most `(L+1)^2`.

Therefore, if `B_gamma` is an injectively described output bank for every
component and all its outputs cover all component parts, then

\[
 \left|\bigcup_\gamma B_\gamma\right|
       \ge {\sum_\gamma|B_\gamma|\over L+1},             \tag{23}
\]

or the same bound with `(L+1)^2` in the double-order setting.  This is the
correct weighted recursive escape.  The interval endpoints do not need to
be appended as artificial tags; retained witnesses decode them.

There is no analogous theorem for an erased-part bank.  At the finest
dyadic scale, group the `n` ordered vertices into `P=n/2` consecutive
parent pairs.  Fix the first pair `{x,y}`.  For every choice of `k-2` other
parent pairs, take the `k`-edge consisting of `x,y` and one prescribed
vertex from each chosen pair.  It meets `k-1` parent cells but `k` child
cells, so its minimum scale is the finest one, and distinct choices have
distinct component part-tuples.  There are

\[
                         \binom{n/2-1}{k-2}               \tag{24}

such components.  If every local bank erases all but the common face
`{x}`, then every incidence has the identical output.  Placing all vertices
in convex position makes this a planar ordinary-face example.

For `k=Theta(L)`, (24) is `n^{Theta(k)}=2^{Theta(L^2)}`.  The Cauchy energy
is sharp: if `T` components all output `{x}`, then the total incidence is
`T`, the sole output has degree `T`, and the degree-square sum is `T^2`.
No averaging or component-ID bookkeeping recovers any mass.  A bank which
erases `h` unconstrained part witnesses can similarly have `n^{Omega(h)}`
load.  Thus interval IDs make summation free only under the explicit
part-cover hypothesis.

## 6. The multiply occupied residual can contain all entropy

The `k<r` issue is not merely a counting technicality.  Take `k` strict
reverse tangent cells.  Put `N` points in the first cell on a rational
lower circular arc and one anchor in each of the other `k-1` cells, all on
the same arc.  Set

\[
                      s=k,qquad r=s+k-1=2k-1.            \tag{25}
\]

Let the source family consist of every choice of `s` points from the first
cell together with every anchor.  Every source, and indeed every subset of
the whole support, is a rooted convex face.  The family is interval
`k`-partite in each reverse tangent order and has

\[
                            M=\binom Ns.                  \tag{26}

Fix `N=2^L` and `k=s=Theta(L)`.  The actual host size is
`n=N+k+1` after including the anchors and the root edge.  For all
sufficiently large `L`, `n^{k-1}<M<n^k`, so the density exponent lies in
`(k-1,k)`, exactly the legal FJKMV range, and `log M=Theta(L^2)`.
Nevertheless the bank retaining only one point from every macro part has
at most `N` outputs, a loss

\[
                         {M\over N}=2^{Theta(L^2)}.        \tag{27}

No occupancy-pattern refinement helps: every edge has the same vector
`(k,1,...,1)`.  The example pays through the full Boolean bank in the first
cell, so it is not an EIC obstruction.  It proves exactly that the ordered
partition theorem supplies only macro intervals.  Promoting them to a
recoverable radial/profile container still requires a local theorem which
uses the full trace in every multiply occupied cell and enforces the
cup/cap orientations missing from Section 4.

## 7. Consequence for the current proof attack

FJKMV is valid as a coefficient-free preprocessing step under the following
strict interface:

* use its explicit varying-parameter constant, not fixed-`r` `Omega`;
* retain one genuine face witness in every macro interval so component
  summation has only `(L+1)^2` load;
* inside multiply occupied cells, invoke an independent radial
  entropy/profile bank; and
* certify the cup/cap signs, not merely reverse dominance.

It cannot by itself create the missing oriented containers, even with two
orders and even in the formally favorable `k=r` regime.  The next genuine
coordinate is the **local cup/cap profile inside each occupancy cell**.
That coordinate must remain visible in the output bank; otherwise either
the single-cell entropy collapse (27) or the erased-component reuse (24)
is quadratic-exponential.

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_ordered_hypergraph_promotion_audit.py
```

The checker uses only integer and rational arithmetic.  It verifies the
uniform constants, raw component scale, impossibility of `k=r`, the exact
general-position cup/cap counterexample, the dyadic erased-part load, and
the scalable multiply occupied family.
