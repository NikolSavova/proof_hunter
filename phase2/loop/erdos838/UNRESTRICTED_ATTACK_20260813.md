# Erdős 838: unrestricted attack after the coefficient-one-half theorem

> Status, 2026-08-13.  The unrestricted problem remains open.  The rigorous
> base-two window is
> \[
>   \frac14\leq\liminf_{N\to\infty}
>   \frac{\log f(N)}{(\log N)^2}
>   \leq\limsup_{N\to\infty}
>   \frac{\log f(N)}{(\log N)^2}\leq\frac12.
> \]
> This note records the next full-problem attack: what was proved, what was
> falsified, and the two statements that now look capable of moving the
> window.

All logarithms are base two.  We count nonempty convex-position subsets;
changing the convention for sets of size at most two has no asymptotic
effect.

## 1. The exact unrestricted object

After a generic rotation, write the points as
`p_1<...<p_N` in horizontal order.  Let `c(s,t)` and `u(s,t)` be the numbers
of caps and cups whose common left and right endpoints are `p_s,p_t`.
The upper and lower hull chains give the exact identity

\[
  V(P)=N+\sum_{s<t}c(s,t)u(s,t).                 \tag{1}
\]

Thus a matching lower bound is precisely the common-endpoint inequality

\[
  \sum_{s<t}c(s,t)u(s,t)
  \geq 2^{(1/2-o(1))(\log N)^2}.                 \tag{2}
\]

Retaining both endpoints is essential.  If `R(u,v)` and `B(u,v)` count
monochromatic monotone paths ending with the edge `(u,v)`, then
`N+sum R(u,v)B(u,v)` counts split path pairs, not convex subsets.  On the
six-point Pascal cell `T_(4,2)` the two values are respectively `44` and
`50`.  This exact counterexample kills a tempting weighted version of the
usual one-endpoint down-set proof.

## 2. A broad upper-construction barrier

The paper proves coefficient `1/2` by iterating a fixed vertical template.
The natural reaction is to use several recursively interacting templates,
reflect some of them to anti-align cap and cup mass, and allow unequal child
sizes.  This still cannot work if the system has finitely many states.

### The finite-state theorem

Let every state `p` have a fixed macro order type whose positions are
labelled by child states, and recursively replace each macro point by its
labelled depth-`d-1` child.  Macro sizes, labels, and order types may depend
on `p`.  The mixed triples use the almost-vertical blow-up rule.  Then, for
every initial state,

\[
 \liminf_{d\to\infty}
 \frac{\log V(Q_p(d))}{(\log |Q_p(d)|)^2}\geq\frac12. \tag{3}
\]

Here is the mechanism.  Restrict the substitution matrix to a reachable
strongly connected component of maximal Perron growth `Lambda`.  Its
retained depth-`d` constructions have size `Theta(Lambda^d)` at every depth,
including in the periodic case.  Maximum-cycle-mean recurrences give

\[
 \log C_q(d)=\frac{\rho_C\log\Lambda}{2}d^2+O(d),
 \qquad
 \log U_q(d)=\frac{\rho_U\log\Lambda}{2}d^2+O(d). \tag{4}
\]

The cup--cap theorem forces `rho_C+rho_U>=log Lambda`.  Since `Lambda>1`,
some macro row has two recurrent child positions.  Choosing a cap in the
left one and a cup in the right one is convex, so its two-block term and
(4) give (3).  A fixed descendant path transfers the estimate back to the
initial state.

This closes stationary, periodic, finite-menu, reflected, and every other
finite-automaton vertical scheme.  To beat `1/2` by this geometry requires
growing state complexity, genuinely depth-dependent macroscopic changes, or
a different mixed-triple signature.

### The newer Baek--Balko blow-up

The new `x`-blow-up is not covered by simply calling it a finite-state
iteration, so we counted two explicit convex families inside it.  Put

\[
  \theta=x/k,\qquad m=k-2x,qquad N=2^{k-2}.
\]

For the canonical Pascal-cell realization with `m>=4`, the resulting lower certificate
has coefficient

\[
 \max\{T(\theta),I(\theta)\},                    \tag{5}
\]

where

\[
\begin{aligned}
T(\theta)&=\int_\theta^{1/2}H_2(s)\,ds
 +\frac{(1-2\theta)^2}{4\ln2}+\theta(1-2\theta),\\
I(\theta)&=H_2(\theta)-\frac{\theta(1-\theta)}{\ln2}.
\end{aligned}                                    \tag{6}
\]

The first term counts one-point-per-layer transversals in one Pascal-row
half of the macro set; the second counts all convex subsets inside a
score-two canonical Pascal cluster.  For every fixed `theta<1/2`, splitting
at `theta=0.21` gives

\[
 \max\{T(\theta),I(\theta)\}\geq
 I(0.21)=0.5021396326\ldots>\frac12.             \tag{7}
\]

The transversal bound is independent of the internal order types and
already covers `theta<=0.21`.  The remaining loophole is deliberate in the
Baek--Balko definition: for `theta>0.21` one may replace canonical cells by
arbitrary extremal cap--cup configurations.  Excluding those requires a new
supersaturation theorem for precisely the nondecomposable configurations
that remain uncontrolled in Erdős 838.  Thus the new macro geometry itself
does not currently furnish a sub-`1/2` construction.  The degenerate
sequence `m=3` (so `theta->1/2`) has no ordinary score-two cluster, but the
fully canonical version is still blocked: each of its two special endpoint
clusters is decomposable with `2^(k-3)` points, so the sharp strong-class
theorem supplies coefficient `1/2` inside either one.  Noncanonical special
endpoint clusters remain part of the arbitrary-cell loophole.

## 3. Why the standard lower-bound amplifications are fixed at `1/4`

### Hereditary incidence telescopes

If every `t`-subset contains `A` convex subsets of size at least `h`, then
double-counting pairs `(T,K)` gives the exact lift

\[
 V(P)\geq A\frac{\binom nt}{\binom{n-h}{t-h}}
       =A\frac{\binom nh}{\binom th}.            \tag{8}
\]

Applying (8) through any chain of intermediate subset sizes telescopes to
the one-scale factor.  Likewise, even an ideal lossless same-type partition,
using every convex macro support and every transversal, reproduces the same
quadratic `beta(1-beta)` curve.  Refeeding the total `1/4` bound into induced
subsets cannot bootstrap itself.

More generally, extracting a hereditary structured subset of size
`t^(alpha-o(1))` with internal coefficient `c` gives at best `c alpha^2`
when `alpha>=1/2`, even after running the extractor in every `t`-subset and
retaining all witnesses.  The strong-class value `c=1/2` therefore beats
`1/4` only if `alpha>1/sqrt(2)` and reaches `1/2` only for a near-spanning
extraction.

### Marginal cap and cup abundance does not align

For ordered heterogeneous clusters, the unavoidable two-block term is

\[
 F=\sum_{i<j}C(Q_i)U(Q_j).                       \tag{9}
\]

Place cup-heavy clusters first and cap-heavy clusters last.  Both separate
marginal sums are `Theta(r 2^m)`, while (9) is smaller than their product by
`2^{-m+O(log m)}`.  Reversing the two groups changes (9) by an exponential
factor.  Cluster sizes and separate cap/cup totals therefore cannot replace
forward endpoint alignment.

### Hinged-history mass cannot be globally compressed

Every point set has
`2^((1/2-o(1))(log N)^2)` hinged histories, which had suggested copying the
graph good-sequence argument.  Even a fully nonlocal comparison

```
H_q(P) <= 2^(O(q log q)) V(P)                    (10)
```

is false.  Let `Q_d` be the depth-`d` directional iterate of the six-point
cell `T_(4,2)`, and put `q=floor(d log 6)`.  Its exact cap polynomial is

\[
c_{Q_d}(z)=z\prod_{\ell=0}^{d-1}
 (6+15\,6^\ell z+10\,6^{2\ell}z^2).             \tag{10a}
\]

At each of `floor(sqrt d)` successive top levels, choose a cap in an earlier
block and continue a hinged history in a later block.  Distribute the
`q-1` cap vertices evenly over those levels.  The explicit monomial in
(10a) then gives

\[
 \log H_q(Q_d)\geq(\log6)^2d^2-O(d^{3/2}),       \tag{10b}
\]

whereas the paper's exact convex recurrence gives

\[
 \log V(Q_d)=2(\log6)d^2+O(d).                  \tag{10c}
\]

Because `log 6>2`, their difference is `Omega(d^2)`, while
`q log q=O(d log d)`.  Thus (10) fails for every hidden constant.  At the
finite depth `d=18`, the exact recurrence already gives
`H_47(Q_18)>47! V(Q_18)`.  Hinged histories are therefore not merely hard to
compress by a contained map; their global multiplicity is intrinsically too
large on a realizable extremal family.

## 4. The growing-`k` supersaturation target

Let `mu_k(n)` be the minimum number of convex `k`-subsets in an `n`-point
set.  Suppose that, uniformly at exponential scale,

\[
 \mu_k(2^{\rho k+o(k)})
 \geq 2^{\sigma k^2-o(k^2)}.                    \tag{11}
\]

Lifting these local witnesses to an `N`-point set gives the base-two
coefficient

\[
 \Phi(\rho,\sigma)=
 \max_{0<\beta\leq1/\rho}
   \bigl[\beta-(\rho-\sigma)\beta^2\bigr].       \tag{12}
\]

At `rho=2`, the standard one-witness estimate is `sigma=1` and (11) is
exactly `1/4`.  Any uniform gain

\[
 \mu_k(2^{2k+o(k)})
 \geq2^{(1+\eta-o(1))k^2}                       \tag{13}
\]

would improve the unrestricted lower coefficient to `(1+eta)/4`; the
matching `1/2` corresponds to `eta=1`.

There is an exact flag reformulation.  A point subset is convex if and only
if all of its four-subsets are convex, by planar Caratheodory.  Hence convex
`k`-sets are cliques in the four-uniform hypergraph of convex quadruples.
But fixed-order densities cannot prove (12): a random abstract four-graph
has well-behaved hereditary densities for every fixed list of orders and
still has clique number only `O((log n)^(1/3))`.  Any successful clique
argument must use oriented-matroid constraints at order growing with `k`,
not merely the density of convex quadrilaterals or any fixed flag list.

As a stress test, exact triangular fixed-point recurrences compute the
limiting density of convex `k`-sets in infinitely iterated balanced Pascal
templates.  Optimizing the tested row gives

\[
 -\frac1{k^2}\log\Pr(\text{random `k`-set is convex})
 =0.1679,0.2472,0.3129,0.3794,0.3897
\]

at `k=10,20,40,100,120`, respectively.  The rising trend has no proved
limit, but these natural extremal families do not currently falsify a fixed
positive gain in (12).

## 5. Convex closure gives structure, not multiplication

There is an exact hull-fibre identity

\[
 2^N=1+N+\binom N2+
 \sum_{\substack{K\text{ convex}\\|K|\geq3}}
 2^{|P\cap\operatorname{int}\operatorname{conv}K|}. \tag{14}
\]

If `w=log V(P)`, (13) yields a convex cage containing at least
`N-1-w` other points.  Iteration produces at least
`floor((N-5)/(w+1))` pairwise disjoint cages of size at most `w+1` with
strictly nested hulls.  Thus any quasipolynomially extremal configuration
has `N/O(log^2 N)` small nested cages.

The cages cannot simply be multiplied.  Exact rational nested triangles
already have fewer convex subsets than the product of their individual
counts.  More decisively, the coefficient-`1/2` blow-up construction itself
has `N/polylog N` such cages but only `2^{O(log^2 N)}` convex subsets.  No
universal factor per cage, nor even `2^{Omega(D^epsilon)}` for `D` cages,
is possible at the relevant polylogarithmic cage size.

One positive two-cage inequality survives.  If `A` is an outer cage and
`B` an inner cage, expose the subsets `F_x` of inner vertices that remain
extreme in `conv(B union {x})`.  The sets `F_x` cover `B` and have size at
least two, giving at least

\[
 |A|\bigl(2^{\max(2,|B|/|A|)}-1\bigr)            \tag{15}
\]

convex subsets using one point of `A` and points of `B`.  The bound is too
weak in the many-small-cage regime, but it is a concrete geometric input for
a future nonlocal charging argument.

## 6. The live routes

The attack has narrowed to two credible lower routes and two much narrower
upper escapes.

1. **Common-endpoint entropy.**  Prove (2) directly from the rank-three
   one-change axioms while retaining both endpoints.  The strong-tree reset
   theorem is a model of the required multiscale charging.  Hinged histories
   cannot serve even as a nonlocal intermediary, by (10b)--(10c).
2. **Growing-order supersaturation.**  Prove (11) with `sigma>rho-1`, or
   equivalently obtain a quadratic multiplicity excess over the ordinary
   Erdős--Szekeres witness count.  Intermediate-scale averaging and all
   fixed flag densities have now been eliminated as sources of that excess.
3. **Growing-state upper construction.**  Use infinitely many genuinely
   new states or macroscopic depth-dependent changes.  Finite automata and
   finite menus are blocked by (3).
4. **Noncanonical extremal cells or new mixed geometry.**  The only live
   Baek--Balko `x`-blow-up window uses arbitrary nondecomposable cap--cup
   extremal cells for `theta>0.21`; otherwise a construction must leave the
   vertical endpoint-cluster rule altogether.

The first two statements are both strong enough to move the problem.  The
second offers an incremental target---any `eta>0` in (12) improves the
published lower coefficient---while the first is the clean route to the
full value `1/2`.

## 7. Verification map

The claims above are supported by the following independent artifacts.

* `agent_upper_multitype/FINITE_STATE_BARRIER.md` and
  `agent_asymptotic/FINITE_STATE_BARRIER_AUDIT.md`;
* `agent_asymptotic/BAEK_BLOWUP_COUNT.md` and
  `agent_asymptotic/bb_xblowup_barrier.py`;
* `agent_claude_review_audit/HEREDITARY_MULTIPLICITY_BARRIER.md` and
  `agent_claude_review_audit/multiplicity_barrier_check.py`, together with
  `GLOBAL_HISTORY_AUDIT.md` and `history_global_test.py`;
* `agent_upper_multitype/FOUR_CLIQUE_SUPERSATURATION.md`,
  `fixed_k_density.py`, and `pascal_vk_probe.py`;
* `agent_upper_multitype/NESTED_CAGE_MULTIPLICITY.md` and
  `nested_cage_search.py`.

The unrestricted limit is not claimed solved.
