# Erdős 838: complete instance handoff

> **Prepared:** 2026-08-13
> **Purpose:** allow a fresh model or human collaborator to resume without
> access to the preceding conversation.  This records durable mathematical
> reasoning, results, counterexamples, audits, commands, claim boundaries,
> and suggested next work.  It does not reproduce private model
> chain-of-thought; it contains the conclusions and proof-relevant arguments
> needed to continue the research.

All logarithms in this file are base two unless explicitly stated otherwise.

---

## 0. Read this first: the one-minute state

For an `N`-point planar set `P` in general position, let `V(P)` be the number
of its subsets in convex position and

\[
 f(N)=\min_{|P|=N}V(P).
\]

Subsets of size one and two are counted; including the empty set changes
nothing asymptotically.

The current rigorous unrestricted window is

\[
 \boxed{
 \frac14\leq\liminf_{N\to\infty}
 \frac{\log f(N)}{(\log N)^2}
 \leq\limsup_{N\to\infty}
 \frac{\log f(N)}{(\log N)^2}
 \leq\frac12.}
\]

What is proved here:

1. **Unrestricted upper bound:** the coefficient is at most `1/2`.
2. **Sharp theorem for mirror-decomposable sets:** every such set has
   `log V(P) >= (1/2)(log N)^2-O((log N)^(3/2))`, and the upper construction
   attains `1/2`.  Hence the exact coefficient within that class is `1/2`.
3. **Broad construction barriers:** fixed templates, nonstationary finite
   menus, all finite-state vertical blow-up systems, and the fully canonical
   Baek--Balko `x`-blow-ups cannot beat `1/2`.
4. **Broad lower-method barriers:** ordinary hereditary double counting,
   ideal same-type transversals, fixed flag densities, naive nested-cage
   multiplication, and local or global hinged-history compression do not
   close the lower gap.

What is **not** proved:

- the existence of the unrestricted limit;
- a lower coefficient above `1/4`;
- that the unrestricted answer equals `1/2`;
- global novelty in the publication sense without human specialist and
  database clearance.

The best current overview is
[UNRESTRICTED_ATTACK_20260813.md](UNRESTRICTED_ATTACK_20260813.md).  The
submission-oriented partial-result paper is [paper/main.tex](paper/main.tex).

---

## 1. Exact problem statement and normalization

Erdős recorded the problem in 1978, attributing the question jointly to
Hammer.  Determine or estimate the minimum total number of convex-position
subsets in an `N`-point general-position planar set; in particular, does

\[
 \frac{\log f(N)}{(\log N)^2}
\]

have a limit?

The paper and all current notes use base-two logarithms.  If a base-two
coefficient is `a`, then the coefficient of
`ln f(N)/(ln N)^2` is `a/ln 2`.  Thus the proposed base-two value `1/2`
would be `1/(2 ln 2)` in natural-log normalization.

The standard lower `1/4` is obtained as follows.  Let `t=N^alpha` and use
the modern Erdős--Szekeres estimate `ES(k)=2^(k+o(k))`.  Every `t`-set has a
convex `k=(alpha-o(1))log N` subset.  Double count pairs `(K,T)` with
`K subset T subset P`, `|T|=t`, to get exponent

\[
 \alpha(1-\alpha),
\]

maximized at `alpha=1/2`.  The value is `1/4`.

The classical upper coefficient `1` comes from taking `N` points from a
`2^(k-2)`-point configuration with no convex `k`-set and summing
`sum_(j<k) binom(N,j)`, with `k=log N+O(1)`.

---

## 2. The paper result: unrestricted upper coefficient `1/2`

### 2.1 Directional composition

After a generic rotation, all coordinates may be assumed to have strict
horizontal order.  For suitable point sets `S,Q`, replace every point of
`S` by a sufficiently small almost-vertical affine copy of `Q`.  The mixed
orientation rule is:

- two points in an earlier block and one later point have negative sign;
- one point in an earlier block and two in a later block have positive sign.

Call the composition `S[Q]`.  The perturbation scale is chosen **afresh at
every finite composition node**.  There is no universal numerical epsilon.
Finitely many strict determinant inequalities give an open interval
`(0,epsilon_0(S,Q))`; rational input sets permit a rational epsilon in that
interval.

This fresh-epsilon quantifier is load-bearing.  Reusing `epsilon=1/97` in a
nested 36-point example creates duplicate points; even `1/1000` is in
general position but has hundreds of wrong mixed signs.  `1/9750`,
`1/10000`, and `1/16384` pass for that unnormalized instance, while the
normalized verifier accepts `1/128`.  See
[agent_killsearch/EPSILON_EMERGENCY_AUDIT.md](agent_killsearch/EPSILON_EMERGENCY_AUDIT.md).

### 2.2 Exact substitution identities

Write `c_j(S),u_j(S),v_j(S)` for the numbers of `j`-point caps, cups, and
convex subsets of `S`.  Let `n=|Q|`, and let `C,U,W` denote nonempty total
cap, cup, and convex-subset counts.  Then

\[
\begin{aligned}
C(S[Q])&=C(Q)\sum_{j\ge1}c_j(S)n^{j-1},\\
U(S[Q])&=U(Q)\sum_{j\ge1}u_j(S)n^{j-1},\\
W(S[Q])&=|S|W(Q)+C(Q)U(Q)
          \sum_{j\ge2}v_j(S)n^{j-2}.
\end{aligned}
\]

Why these are exact:

- a cap meeting multiple macro-blocks expands only its first block, to an
  arbitrary nonempty cap; every later occupied block contributes one point;
- a cup expands only its last occupied block;
- a crossing convex subset has a cap in its first block, a cup in its last,
  and one point in every intermediate occupied block;
- the occupied macro support is respectively a cap, cup, or convex subset
  of `S`;
- conversely, these choices give the two hull chains and hence a convex set.

The same endpoint-cluster phenomenon appears structurally in Baek--Balko's
blow-up lemma, but the exact uniform sum over all choices and the resulting
asymptotics are the contribution here.

### 2.3 Fixed-template asymptotics

Let `S` have `r` points, largest cap size `a`, and largest cup size `b`.
Iterate `Q_0` a singleton and `Q_d=S[Q_(d-1)]`.  The exact recurrences yield

\[
 \log W(Q_d)=\frac{(a+b-2)\log r}{2}d^2+O_S(d),
 \qquad |Q_d|=r^d.
\]

Therefore the normalized coefficient is

\[
 \rho(S)=\frac{a+b-2}{2\log r}.
\]

The cup--cap theorem gives `r<=2^(a+b-2)`, so every fixed template has
`rho(S)>=1/2`.  Balanced classical Pascal cells have

\[
 r_k=\binom{2k-4}{k-2},\qquad a_k=b_k=k-1,
\]

and their coefficients tend to `1/2` from above.  For arbitrary `N`, choose
the least iterate containing at least `N` points and delete points.  Since
the fixed branching ratio is constant, the logarithmic denominator changes
only by lower-order terms.

This proves

\[
 \limsup\frac{\log f(N)}{(\log N)^2}\le\frac12.
\]

### 2.4 Earlier upper bounds that were superseded

The attack first found:

- full Pascal row: coefficient `1/(2 ln 2)=0.7213475...`;
- central Pascal cell: coefficient
  `1-1/(4 ln 2)=0.6393262398...`.

Both arguments were correct, but the iterated balanced-template result
`1/2` is stronger.  Do not present the earlier constants as the main result.
They remain useful sanity checks for the cap/cup recurrences.

---

## 3. Sharp `1/2` theorem for the whole decomposable class

### 3.1 Terminology and geometry

Balko--Kynčl--Langerman--Pilz introduced decomposable point sets via
recursive left/deep-below splits.  The paper uses the mirror convention
under

\[
 \rho(x,y)=(-x,y),
\]

with child order reversed.  A 180-degree rotation is **not** the correct
conversion.  Reflection preserves cap and cup sizes and total convex counts.

For a strong glue `T=A prec B`, let `a=|A|`, `b=|B|`.  Exact nonempty counts
satisfy

\[
\begin{aligned}
C(T)&=C(B)+(b+1)C(A),\\
U(T)&=U(A)+(a+1)U(B),\\
W(T)&=W(A)+W(B)+C(A)U(B).
\end{aligned}
\]

The final crossing identity uses a cap in the left child and a cup in the
right child.  The reverse product is not generally counted.

### 3.2 Endpoint maxima

For a subtree `T`, define:

- `X(T)`: maximum number of caps with a fixed leftmost point;
- `Y(T)`: maximum number of cups with a fixed rightmost point;
- `M(T)=max_(s<t)c(s,t)u(s,t)`, with an auxiliary value at a singleton.

Then

\[
\begin{aligned}
X_T&=\max\{(b+1)X_A,X_B\},\\
Y_T&=\max\{Y_A,(a+1)Y_B\},\\
M_T&=\max\{M_A,M_B,X_AY_B\}.
\end{aligned}
\]

Moreover `M<=W<=N^2M` for `N>=2`.  Thus the quadratic coefficient can be
proved at the max-endpoint level.

The product-mass lemma gives a radial estimate

\[
 \log X(T)+\log Y(T)
 \ge\frac12(\log|T|)^2-O(\log|T|).
\]

### 3.3 Multiscale reset proof

Let `L=log N` and `R=ceil(sqrt L)`.  Follow a heavy child through a window in
which the subtree loses roughly `4R` bits of size.

There are two cases.

1. **Few macroscopic discarded siblings.**  Then there are
   `Omega(R L^2)` tiny sibling levels.  At least half lie on the same side
   of the heavy path.  Choosing arbitrary subsets of those fixed sibling
   leaves, plus a terminal leaf, gives distinct pure caps or cups.  This is
   much larger than the target.
2. **At least `R` macroscopic siblings.**  All selected children have nearly
   full scale and hence a uniform radial endpoint lower bound `F`.  If the
   forward product at the first selected attachment is already large, the
   theorem is done.  If it is hidden below the root maximum `mu=log M`, the
   reverse coordinates are forced to reset: both parent endpoint
   coordinates become at least `2(F-mu)-O(L)`.  At every later nested
   attachment, either the `X` coordinate or the `Y` coordinate gains
   `F-mu`; maxima preserve all earlier gains.  One orientation occurs at
   least `(R-1)/2` times.  The resulting inequality solves to

   \[
   \mu\ge\frac12L^2-O(L^{3/2}).
   \]

Therefore every mirror-decomposable `N`-point set has

\[
 \log W\ge\frac12(\log N)^2-O((\log N)^{3/2}).
\]

The proof was independently reconstructed by two agents and accepted by a
third referee.  Read, in order:

1. [agent_asymptotic/NEXT_ENDPOINT_ATTACK.md](agent_asymptotic/NEXT_ENDPOINT_ATTACK.md)
2. [agent_geometry/NEXT_ENDPOINT_AUDIT.md](agent_geometry/NEXT_ENDPOINT_AUDIT.md)
3. [agent_killsearch/STRONG_TREE_HALF_REFEREE.md](agent_killsearch/STRONG_TREE_HALF_REFEREE.md)

The arithmetic smoke test is
`agent_asymptotic/endpoint_reset_certificate.py`; it does not encode the
entire heavy-path proof.

### 3.4 Historical dead ends inside the tree problem

Before the reset proof, a `1/3` theorem was obtained.  It is correct but
superseded.  Several natural stronger potentials were false:

- the imbalance-corrected `H` potential has an exact enormous iterated-
  Pascal counterexample;
- local scalar Bellman inductions fail on valid recursive states;
- a universal subquadratic comparison between `C(T)U(T)` and `W(T)` is
  false;
- endpoint-rooted caterpillar counts can exceed `W` exponentially;
- one-node slack squares cannot be charged independently because alignment
  can reset across scales.

See
[agent_killsearch/H_COUNTEREXAMPLE.md](agent_killsearch/H_COUNTEREXAMPLE.md),
[agent_killsearch/QUADRATIC_PROFILE.md](agent_killsearch/QUADRATIC_PROFILE.md),
[agent_asymptotic/E_VS_W_COUNTEREXAMPLE.md](agent_asymptotic/E_VS_W_COUNTEREXAMPLE.md),
and [agent_asymptotic/TREE_ALIGNMENT.md](agent_asymptotic/TREE_ALIGNMENT.md).
Do not restart these scalar-potential routes without a genuinely new
hereditary state.

---

## 4. Exact unrestricted reduction

After horizontal ordering, let `c(s,t)` be the number of caps with common
left and right endpoints `p_s,p_t`, and let `u(s,t)` be the analogous cup
count.  Every convex subset of size at least two has unique upper and lower
hull chains with the same two endpoints, and conversely their union is
convex.  Hence, for nonempty counts,

\[
 \boxed{V(P)=N+\sum_{s<t}c(s,t)u(s,t).}
\]

If the empty set is counted, add one.

The exact full-problem target is therefore

\[
 \sum_{s<t}c(s,t)u(s,t)
 \ge 2^{(1/2-o(1))(\log N)^2}.                  \tag{EM}
\]

This is a **common-two-endpoint alignment problem** in realizable rank-three
signotopes.

A crucial correction: if `R_uv,B_uv` count monochromatic monotone paths
ending with the edge `(u,v)`, then

\[
 N+\sum_{u<v}R_{uv}B_{uv}
\]

does **not** equal `V(P)`.  It counts split-type path pairs sharing their
final edge, not hull chains sharing both extreme endpoints.  The six-point
cell `T_(4,2)` gives `44` for this expression and `50` true nonempty convex
subsets.  Do not use a one-endpoint weighted down-set identity.

---

## 5. Unrestricted construction barriers

### 5.1 Nonstationary homogeneous schedules

For `Q_t=S_t[Q_(t-1)]`, put `ell_t=log|S_t|` and
`L_t=sum_(i<=t)ell_i`.  Two-block terms and cup--cap give

\[
 \log W(Q_d)\ge
 \frac12\left(L_{d-1}^2-\sum_{t<d}\ell_t^2\right).
\]

Thus stationary, periodic, finite-menu, and every schedule whose largest
scale is `o(L_d)` has coefficient at least `1/2`.  Polynomial random thinning
preserves the coefficient.  A homogeneous escape needs a macroscopic jump.

### 5.2 General finite-state vertical systems

The stronger theorem allows:

- finitely many recursive states;
- state-dependent macro order types;
- reflected/anti-aligned child types;
- state-dependent branching numbers;
- unequal child sizes at the same depth;
- arbitrary periodic or finite-automaton rules.

Let `M` be the substitution matrix and restrict to a reachable strongly
connected diagonal block `K` with maximal Perron root `Lambda`.  Prune
outgoing children.  A positive Perron vector gives
`|R_q(d)|=Theta(Lambda^d)` at every depth, including periodic components.

Cap and cup maximum-cycle means `rho_C,rho_U` yield

\[
\begin{aligned}
\log C(R_q(d))&=\frac{\rho_C\log\Lambda}{2}d^2+O(d),\\
\log U(R_q(d))&=\frac{\rho_U\log\Lambda}{2}d^2+O(d).
\end{aligned}
\]

Cup--cap forces `rho_C+rho_U>=log Lambda`.  Since `Lambda>1`, some internal
row has two retained child occurrences; their left-cap/right-cup product is
a convex family with coefficient at least `1/2`.  A fixed descendant path
transfers it to the initial state.

The theorem and independent corrected audit are:

- [agent_upper_multitype/FINITE_STATE_BARRIER.md](agent_upper_multitype/FINITE_STATE_BARRIER.md)
- [agent_asymptotic/FINITE_STATE_BARRIER_AUDIT.md](agent_asymptotic/FINITE_STATE_BARRIER_AUDIT.md)

This leaves only growing state complexity, genuinely depth-dependent rules,
macroscopic jumps, or different mixed-triple geometry.

### 5.3 Baek--Balko's newer `x`-blow-up

For their construction, set

\[
 m=k-2x,\qquad \theta=x/k,\qquad N=2^{k-2}.
\]

Two explicit convex families block the fully canonical construction.

1. **Layer transversals.**  Reconstruct a Pascal-row half by subset labels
   `A subseteq [d]`, `d=m-3`.  The endpoint score is
   `s(A)=1+max A` for nonempty `A`.  Choosing one output point from every
   left layer gives coefficient

   \[
   T(\theta)=\int_\theta^{1/2}H_2(s)\,ds
    +\frac{(1-2\theta)^2}{4\ln2}+\theta(1-2\theta).
   \]

   This uses only output-cluster cardinalities, not their order types.
2. **Canonical score-two cell.**  A score-two cluster is the Pascal cell
   `T_(k-3,x)` and contains a convex family with coefficient

   \[
   I(\theta)=H_2(\theta)-\frac{\theta(1-\theta)}{\ln2}.
   \]

`T` decreases and `I` increases.  At the conservative split `theta=0.21`,

\[
 T(0.21)=0.5087955\ldots,
 \qquad I(0.21)=0.5021396\ldots.
\]

Thus every fixed `theta<1/2` in the canonical ordinary-cell realization is
above `1/2`.  For `m=3`, no ordinary score-two cell exists, but in the fully
canonical construction either special endpoint cluster is decomposable and
has `2^(k-3)` points, so the sharp class theorem gives coefficient `1/2`.

The transversal argument alone covers arbitrary internal cells through the
rigorous conservative split `theta=0.21`; the computed root of
`T(theta)=1/2` is `0.21616144...`.  The remaining Baek--Balko loophole is
noncanonical extremal cap--cup microcells above this range, including
noncanonical special endpoints in the degenerate case.

Read:

- [agent_asymptotic/BAEK_BLOWUP_COUNT.md](agent_asymptotic/BAEK_BLOWUP_COUNT.md)
- [agent_geometry/BAEK_BLOWUP_COUNT_AUDIT.md](agent_geometry/BAEK_BLOWUP_COUNT_AUDIT.md)
- `agent_asymptotic/bb_xblowup_barrier.py`

---

## 6. Lower-bound methods that were proved insufficient

### 6.1 Hereditary incidence lifts telescope

If every `t`-subset contains at least `A` convex witnesses of size at least
`h`, then

\[
 V(P)\ge A\frac{\binom nt}{\binom{n-h}{t-h}}
      =A\frac{\binom nh}{\binom th}.
\]

All chains of such fixed-`k` double counts telescope exactly to the one-scale
factor.  Intermediate scales create no quadratic surplus.

Suppose every `t`-set contains a hereditary structured subset of size
`t^(alpha-o(1))`, and every such structured `q`-set has internal coefficient
`c`.  Even applying the extractor in every `t`-set and retaining every
internal witness transfers at best

\[
 c\alpha^2
\]

when `alpha>=1/2`.  For the decomposable value `c=1/2`, beating `1/4`
requires `alpha>1/sqrt 2`; preserving `1/2` requires `alpha=1-o(1)`.

Current mutually-avoiding-pair guarantees are only square-root scale and do
not even directly give a decomposable union of that size.

### 6.2 Same-type transversals stay at `1/4`

If every `t`-set has `k` same-type blocks of size
`s>=t 2^(-gamma k-o(log n))`, incidence lifting gives

\[
 \log v_k(P)\ge k(\log n-\gamma k)-o((\log n)^2),
\]

whose optimized coefficient is `1/(4 gamma)`.  Even perfect retention has
`gamma=1`, hence `1/4`.  The known Bukh--Vasileuski exponent gives only
`1/20` by this direct pipeline.

### 6.3 Separate cap and cup marginals do not align

For ordered heterogeneous clusters, the two-block mass is

\[
 F=\sum_{i<j}C(Q_i)U(Q_j).
\]

Place cup-heavy clusters first and cap-heavy clusters last.  Both marginal
sums are `Theta(r 2^m)`, but the forward sum is smaller than their product
by `2^(-m+O(log m))`.  Reversing the two groups changes the cross term by an
exponential factor.  Any useful theorem must control the forward-aligned
quantity itself, not separate totals.

See
[agent_asymptotic/INCIDENCE_REGULARIZATION_BARRIER.md](agent_asymptotic/INCIDENCE_REGULARIZATION_BARRIER.md)
and
[agent_claude_review_audit/HEREDITARY_MULTIPLICITY_BARRIER.md](agent_claude_review_audit/HEREDITARY_MULTIPLICITY_BARRIER.md).

---

## 7. Hinged histories: exact positive count, decisive compression failure

A nested endpoint-pair process always produces

\[
 2^{(1/2)(\log N)^2-O(\log N\log\log N)}
\]

hinged histories.  This exactly matches the desired raw mass and resembles
the graph good-sequence proof.  The transfer to convex subsets fails much
more strongly than first expected.

### 7.1 Local failures

Exact rational examples show:

- same-sign history levels need not form a cap or cup;
- a hinged history need not be a split polygon;
- a hinged history need not be partitionable into one cap and one cup, even
  with unrelated endpoints;
- there is an eight-point fully alternating hinged set with no convex
  pentagon;
- every contained history-to-convex map can have a
  `2^(Theta((log N)^2))` fibre on a realizable alternating least-index family.

The exact coordinates and checker are in
[agent_geometry/HISTORY_ATTACK.md](agent_geometry/HISTORY_ATTACK.md) and
`agent_geometry/audit_history_obstructions.py`.

### 7.2 Even global compression is false

The tempting hope was

\[
 H_q(P)\le2^{O(q\log q)}V(P).
\]

It is false on the paper's own six-point-template iterates
`Q_d=T_(4,2)[Q_(d-1)]`.  The exact cap polynomial is

\[
 c_{Q_d}(z)=z\prod_{\ell=0}^{d-1}
 (6+15\,6^\ell z+10\,6^{2\ell}z^2).
\]

Take `q=floor(d log 6)`.  On `floor(sqrt d)` successive top levels, choose a
cap in an earlier block and continue a history in a later block; distribute
the cap vertices evenly over the selected levels.  An explicit monomial in
the cap polynomial gives

\[
 \log H_q(Q_d)=(\log6)^2d^2+O(d^{3/2}).
\]

The upper equality follows from `H_q<=binom(6^d,q)`.  Meanwhile

\[
 \log V(Q_d)=2(\log6)d^2+O(d).
\]

Thus the normalized history coefficient is exactly `1`, versus convex
coefficient `2/log 6=0.773705...`, and the gap is quadratic.  Already at
depth 18,

\[
 H_{47}(Q_{18})>47!V(Q_{18}).
\]

Do not use hinged histories as an intermediary unless the new object
retains substantially more geometry than hingedness.

Read
[agent_claude_review_audit/GLOBAL_HISTORY_AUDIT.md](agent_claude_review_audit/GLOBAL_HISTORY_AUDIT.md)
and run `agent_claude_review_audit/history_global_test.py`.

---

## 8. Convex-quadruple hypergraph and the live supersaturation target

A finite general-position planar set is convex if and only if every one of
its four-point subsets is convex.  The reverse direction follows from
Carathéodory: a non-extreme point lies inside a triangle of three others.

Therefore convex `k`-sets are exactly `K_k^(4)` cliques in the 4-uniform
hypergraph whose edges are convex quadruples.

Fixed-density information is insufficient.  A random abstract 4-graph has
well-controlled hereditary densities for every fixed collection of orders,
but clique number only `O((log n)^(1/3))`.  Thus `c_4,c_5,...,c_L` for fixed
`L`, even on all polynomial-size induced subsets, cannot force
`k=Theta(log n)` cliques without growing-order planar constraints.

Define `mu_k(n)` as the minimum number of convex `k`-sets in an `n`-point
configuration.  A clean local target is

\[
 \mu_k(2^{\rho k+o(k)})
 \ge2^{\sigma k^2-o(k^2)}.
\]

Incidence lifting then gives unrestricted coefficient

\[
 \Phi(\rho,\sigma)=
 \max_{0<\beta\le1/\rho}
 [\beta-(\rho-\sigma)\beta^2].
\]

At `rho=2`, the ordinary witness count has `sigma=1` and reproduces `1/4`.
Any theorem

\[
 \mu_k(2^{2k+o(k)})
 \ge2^{(1+\eta-o(1))k^2}
\]

improves the unrestricted lower coefficient to `(1+eta)/4`.  This is the
best incremental target currently identified.  It need not solve the whole
problem to be publishable.

Exact fixed-point calculations for infinitely iterated balanced Pascal
templates do **not** currently falsify a positive `eta`.  The optimized
quantity

\[
 -k^{-2}\log\Pr(\text{random `k`-set is convex})
\]

is approximately `0.168,0.247,0.313,0.379,0.390` at
`k=10,20,40,100,120`.  Its limit is unknown.

Read
[agent_upper_multitype/FOUR_CLIQUE_SUPERSATURATION.md](agent_upper_multitype/FOUR_CLIQUE_SUPERSATURATION.md)
and use `fixed_k_density.py` and `pascal_vk_probe.py`.

---

## 9. Convex closure, nested cages, and why multiplication fails

For a convex subset `K`, let

\[
 \iota_P(K)=|P\cap\operatorname{int}\operatorname{conv}K|.
\]

Every subset is uniquely determined by its hull-vertex set and a subset of
the ambient interior points.  Hence

\[
 2^N=1+N+\binom N2+
 \sum_{\substack{K\text{ convex}\\|K|\ge3}}2^{\iota_P(K)}.
\]

If `w=log V(P)`, some convex cage contains at least `N-1-w` other points.
Iterating gives at least

\[
 \left\lfloor\frac{N-5}{w+1}\right\rfloor
\]

pairwise disjoint convex cages of size at most `w+1`, with strictly nested
hulls.  Therefore a quasipolynomially extremal configuration has
`N/O(log^2 N)` small nested cages.

This does not multiply:

- two exact nested rational triangles can have `V=47<7*7`;
- uniform random-subset onion depth can be linear, since each fully selected
  triangle in a nested sequence requires a distinct removal layer;
- the coefficient-`1/2` blow-up family itself has many small nested cages but
  only quasipolynomially many convex subsets, ruling out a universal factor
  per cage or even `2^(Omega(D^epsilon))` from cage count alone.

A positive two-cage bound remains.  For outer cage `A` and inner cage `B`,
exposed surviving inner sets give at least

\[
 |A|\left(2^{\max(2,|B|/|A|)}-1\right)
\]

convex subsets using one point of `A` and points of `B`.  It is too weak in
the many-small-cage regime.

Read
[agent_upper_multitype/NESTED_CAGE_MULTIPLICITY.md](agent_upper_multitype/NESTED_CAGE_MULTIPLICITY.md)
and the cage sections of
[agent_claude_review_audit/HEREDITARY_MULTIPLICITY_BARRIER.md](agent_claude_review_audit/HEREDITARY_MULTIPLICITY_BARRIER.md).

---

## 10. Ranked next moves

### Priority A: growing-`k` supersaturation

This is the best incremental route.  Seek any fixed `eta>0` in

\[
 \mu_k(2^{2k+o(k)})
 \ge2^{(1+\eta-o(1))k^2}.
\]

Possible useful state:

- the full two-endpoint cap/cup path-count profile;
- growing systems of overlapping nonconvex quadruples plus rank-three
  signotope elimination;
- a planar flag or entropy inequality whose order grows with `k` and whose
  error is uniform for `n>=2^(rho k)`;
- stability: configurations with near-minimal `k`-set density might have to
  resemble recursive Pascal/blow-up order types.

Do not rely only on a fixed list of low-order densities.

### Priority B: common-two-endpoint entropy

Attack `(EM)` directly.  The strong-tree reset proof is the right model:
many failures of forward endpoint products should create persistent reverse
coordinate information that can be charged across scales.  In arbitrary
order types there is no given decomposition tree, so a successful argument
must construct an adaptive multiscale state while retaining **both** hull
endpoints.

The ordinary Baek--Balko vertex down-set labels retain maximum chain lengths
but forget the starting endpoint.  The false `44` versus `50` identity shows
why merely weighting those labels is insufficient.

### Priority C: upper construction outside the barriers

Any construction below `1/2` must plausibly use one of:

- state complexity growing with depth;
- macroscopic template jumps;
- noncanonical extremal cap--cup cells in the open Baek--Balko parameter
  range;
- mixed-triple geometry different from the almost-vertical endpoint rule.

Finite-state reflection/anti-alignment has been exhausted.  Horton/parity
interleavings tested numerically stayed far above `1/2` and did not suggest
a useful family.

### Suggested first task for a new instance

Work on Priority A.  Formulate a finite, falsifiable supersaturation lemma
at `n≈2^(2k)` and test it against:

1. canonical Pascal cells;
2. deep iterates of `T_(4,2)`;
3. Baek--Balko canonical `x`-blow-ups;
4. small complete order-type data through `N=9`;
5. the alternating least-index hinged obstruction.

Any proposed lemma should be accompanied immediately by an exact recurrence
or enumerator.  If it survives, derive the precise `eta` transferred through
the formula for `Phi(rho,sigma)` before investing in a full proof.

---

## 11. Prior-art and novelty position

The primary-source search found no public occurrence of the geometric
coefficient-`1/2` upper bound or the sharp total-count theorem for the
decomposable class.  This is high-confidence apparent novelty, not a proof
of priority.

Important positioning:

- generic and iterated order-type blow-ups are prior art (Han et al.);
- almost-vertical Erdős--Szekeres blow-ups are prior art (Baek--Balko);
- decomposable point sets and the terminology originate with
  Balko--Kynčl--Langerman--Pilz, not with this work;
- Baek--Balko's full JCTA theorem is numbered Theorem 7; the preliminary
  SoCG version uses Theorem 8 for the decomposable result;
- Baek--Balko Lemma 14 contains the endpoint-cluster structural phenomenon,
  but not the exact total enumeration or coefficient `1/2`;
- Huemer et al. have weighted convex-polygon identities, so do not claim the
  first exact convex-polygon enumeration of any kind;
- Székely's graph analogue also has upper coefficient `1/2`, but its
  probabilistic argument does not directly prove the geometric statement;
- the published/general public lower coefficient derivable from modern
  Erdős--Szekeres is `1/4`.

Do not claim:

- first blow-up construction;
- first iterated blow-up;
- full solution of Erdős 838;
- optimal unrestricted coefficient;
- proved existence of the unrestricted limit.

The full source audit is
[SUBMISSION_NOVELTY.md](SUBMISSION_NOVELTY.md).  Before submission, obtain
MathSciNet/zbMATH similarity clearance and ask a discrete geometer familiar
with Erdős--Szekeres constructions to review priority.

---

## 12. Paper status and presentation decisions

Current source: [paper/main.tex](paper/main.tex).  Current rendered copies:

- `phase2/loop/erdos838/paper/main.pdf`
- `output/pdf/erdos838_counting_convex_subsets.pdf`

The user explicitly preferred the original `article` formatting.  Keep:

- `\documentclass[11pt]{article}`;
- the original title and `\maketitle`-before-abstract flow;
- blank conventional `\author{}`;
- the Bregman-paper-style disclosure/contact footnote placed through
  `\date{\today\thanks{...}}`.

The disclosed contacts are:

- Nikol Savova, University of Oxford,
  `nikol.p.savova@gmail.com`;
- Sihao Huang, independent researcher,
  `sihao.c.huang@gmail.com`.

Do not switch back to `amsart` unless the user changes this instruction.

Citation/terminology fixes already made:

- mirror-decomposable, with explicit horizontal separation;
- reflection `rho(x,y)=(-x,y)`, not 180-degree rotation;
- primary attribution to BKLP 2017;
- Baek--Balko full JCTA numbering and Lemma 14;
- generic blow-up provenance;
- coefficient-1 classical estimate;
- finite-template coefficients approach `1/2` from above;
- epsilon selected afresh at each stage.

One phrase remains worth polishing before external circulation: the
abstract's “optimal universal coefficient `1/2` is attained within the
entire decomposable class” can be read as unrestricted optimality.  Prefer
“the universal lower coefficient `1/2` is sharp within this class” or
equivalent wording.

The closest-paper gate has in fact been completed internally: the full
open-access JCTA Baek--Balko article was read, not only the SoCG version.
The old Claude review file predates that resolution in places; treat the
later paper and `SUBMISSION_NOVELTY.md` as authoritative.

---

## 13. Verification commands

Run from the repository root.

### Paper construction and strong-class theorem

```sh
python3 phase2/loop/erdos838/lexicographic_blowup.py
python3 phase2/loop/erdos838/independent_check.py
python3 phase2/loop/erdos838/agent_geometry/audit_blowup_classification.py
python3 phase2/loop/erdos838/agent_asymptotic/endpoint_reset_certificate.py
```

Expected headline checks include:

- direct/formula 36-point count `(C,U,W)=(14136,14136,441399)`;
- exact 16-point nonconvex-macro exhaustion;
- reset arithmetic certificate passes.

### Unrestricted barriers

```sh
python3 phase2/loop/erdos838/agent_claude_review_audit/multiplicity_barrier_check.py
python3 phase2/loop/erdos838/agent_claude_review_audit/history_global_test.py
python3 phase2/loop/erdos838/agent_asymptotic/bb_xblowup_barrier.py --k 120
python3 phase2/loop/erdos838/agent_upper_multitype/heterogeneous_audit.py
python3 phase2/loop/erdos838/agent_upper_multitype/fixed_k_density.py \
  --k 10 20 40 --max-template 40 --precision 100
python3 phase2/loop/erdos838/agent_upper_multitype/nested_cage_search.py \
  --depth 2 3 4 5 --samples 3
```

Expected notable outputs:

- multiplicity and nested-triangle checks: `PASS`;
- history test: the `q!` comparison begins failing at depth 18, and the
  script still ends `PASS` because this is the certified counterexample;
- Baek pivot: `T(0.21)=0.508795545606`,
  `I(0.21)=0.502139632648`;
- heterogeneous exact coordinate audit:
  direct=formula `(498,323,1562)`;
- fixed-density values approximately `0.167935`, `0.247243`, `0.312947` at
  `k=10,20,40`.

Compile-check the Python artifacts:

```sh
python3 -m py_compile \
  phase2/loop/erdos838/agent_asymptotic/bb_xblowup_barrier.py \
  phase2/loop/erdos838/agent_claude_review_audit/*.py \
  phase2/loop/erdos838/agent_upper_multitype/*.py
git diff --check
```

Build the paper from `phase2/loop/erdos838/paper/` with `latexmk -pdf
main.tex`, or use the already configured Tectonic workflow if available.

---

## 14. Repository map

### Authoritative summaries

- `PROBLEM.md` — problem statement.
- `FULL_ATTACK.md` — earlier full attack and exact endpoint reduction.
- `UNRESTRICTED_ATTACK_20260813.md` — current unrestricted map.
- `INSTANCE_HANDOFF_20260813.md` — this restart document.
- `SUBMISSION_NOVELTY.md` — prior-art and claim audit.
- `paper/main.tex` — paper source.

### Upper construction and geometry

- `proof_blowup_half.md` — self-contained construction proof.
- `lexicographic_blowup.py` — exact construction verifier.
- `independent_check.py` — independent 36-point check.
- `agent_geometry/geometry_audit.md` — early exact geometry audit.
- `agent_geometry/half_audit.md` — blow-up classification audit.
- `agent_killsearch/EPSILON_EMERGENCY_AUDIT.md` — perturbation-scale audit.

### Strong-class lower theorem

- `agent_asymptotic/NEXT_ENDPOINT_ATTACK.md` — proof.
- `agent_geometry/NEXT_ENDPOINT_AUDIT.md` — reconstruction.
- `agent_killsearch/STRONG_TREE_HALF_REFEREE.md` — referee report.
- `agent_asymptotic/endpoint_reset_certificate.py` — arithmetic checker.

### Full-problem lower barriers

- `agent_asymptotic/FULL_REGULARIZATION_TRANSFER.md`
- `agent_asymptotic/INCIDENCE_REGULARIZATION_BARRIER.md`
- `agent_claude_review_audit/HEREDITARY_MULTIPLICITY_BARRIER.md`
- `agent_geometry/HISTORY_ATTACK.md`
- `agent_claude_review_audit/GLOBAL_HISTORY_AUDIT.md`
- `agent_upper_multitype/FOUR_CLIQUE_SUPERSATURATION.md`
- `agent_upper_multitype/NESTED_CAGE_MULTIPLICITY.md`

### Construction barriers

- `agent_upper_multitype/FINITE_STATE_BARRIER.md`
- `agent_asymptotic/FINITE_STATE_BARRIER_AUDIT.md`
- `agent_asymptotic/BAEK_BLOWUP_COUNT.md`
- `agent_geometry/BAEK_BLOWUP_COUNT_AUDIT.md`

### Counterexamples to tempting potentials

- `agent_killsearch/H_COUNTEREXAMPLE.md`
- `agent_killsearch/QUADRATIC_PROFILE.md`
- `agent_asymptotic/E_VS_W_COUNTEREXAMPLE.md`
- `agent_asymptotic/CAPPED_E_BELLMAN.md`
- `agent_killsearch/RECURRENCE_TRANSFER.md`

---

## 15. Operational and git state at this handoff

The unrestricted attack was committed and pushed in commit

```text
18fd244  Map unrestricted Erdos 838 barriers and live targets
```

The paper formatting/citation sequence immediately preceding it includes
commits `21672b2`, `3d0b863`, and related audits.  Always pull before
editing because the repository is shared.

At preparation time, unrelated working-tree items existed and were left
untouched:

- modified `phase2/loop/erdos791/full_attack2/primal/KOHONEN_ROLE_EXPANSION_CHECK.json`;
- untracked root `AGENTS.md`;
- untracked `tmp/`.

Do not stage or delete these as part of Erdős 838 work without checking
ownership.

---

## 16. Claim discipline for the next instance

Use these labels consistently:

- **THEOREM:** unrestricted upper `1/2`; sharp mirror-decomposable class
  theorem; finite-state barrier; canonical Baek barrier with the stated
  hypotheses; incidence/cage/history counterexamples.
- **COMPUTATIONAL EVIDENCE:** optimized fixed-`k` Pascal density trend;
  small order-type minima; computed Baek crossing `0.21616144...` unless
  accompanied by certified interval bounds.
- **CONJECTURE/TARGET:** unrestricted common-endpoint inequality `(EM)`;
  any growing-`k` supersaturation gain; unrestricted limit `1/2`.
- **APPARENT NOVELTY:** all publication-priority statements until human
  specialist/database clearance.

If a new route appears to solve the lower bound, attack it first with:

1. the six-point cell `T_(4,2)` and its iterates;
2. alternating least-index order types;
3. cap-heavy/cup-heavy anti-alignment;
4. exact small order-type data;
5. a separate agent or human reconstruction.

Several elegant claims survived dozens of small tests and were later killed
by large exact recursive examples.  Do not promote a scalar potential or
compression inequality without an asymptotic adversarial family check.
