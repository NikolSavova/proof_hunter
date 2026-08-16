# Entropy-sensitive semialgebraic transcripts: independent audit and proof

**Date:** 2026-08-15.  Entropies and divergences are in bits.

## Verdict

The proposed transcript lemma is correct for every finite-support
distribution on positive planar orientation triples.  No weighted global
regularity theorem is actually needed.  The fixed-density homogeneous
subrectangle theorem, iterated a constant number of times by eight-way
product splits, gives the required constant-branching rectangle partition
with product-marginal exceptional mass at most `1/4`.  Its weighted form
follows cleanly by cloning and projecting clone subsets back to their
supports.

Let `P` be supported on

\[
 E=\{(x,y,z):\operatorname{orient}(x,y,z)>0\}            \tag{1}
\]

and put

\[
 \operatorname{TC}(P)
   =D(P\Vert P_XP_YP_Z).                                  \tag{2}
\]

There is a deterministic leaf transcript `C` such that every leaf is an
exact product rectangle `A_C x B_C x D_C`, every transversal of
that rectangle lies in `E`, and

\[
 \boxed{\qquad H(C)\le K_0(1+\operatorname{TC}(P))\qquad} \tag{3}
\]

for an absolute constant `K_0`.  The constant obtained from the published
Fox--Pach--Suk bounds is enormous but independent of the support and of
`P`.

For a uniform family of `M` positive consecutive-triple words
`W=(X_1,...,X_r)`, distinguish entropy correlation from support
redundancy:

\[
 R_{\rm ent}=\sum_iH(X_i)-H(W)
 \le R_{\rm supp}
 =\log\prod_i|\operatorname{supp}X_i|-\log M.            \tag{4}
\]

The inequality can be strict when coordinate marginals are nonuniform;
deleting unused labels does not make them uniform.  Applying (3) to each
consecutive triple
and intersecting the resulting coordinate rectangles gives one global
positive homogeneous product cell containing at least

\[
                         M\,2^{-O(r+R_{\rm ent})}
                    \ge M\,2^{-O(r+R_{\rm supp})}        \tag{5}
\]

distinct selected words.  The key overlap estimate is exact:

\[
 \sum_{j=1}^{r-2}\operatorname{TC}(X_j,X_{j+1},X_{j+2})
                              \le2R_{\rm ent}.            \tag{6}
\]

The audit found no flaw in the partite, weighted, product-intersection, or
entropy-to-distinct-words steps.  Two qualifications must remain explicit.

1. The theorem is stated for finite support, which is the application here.
   For general measures, infinite total correlation makes (3) vacuous; a
   finite-TC extension needs ordinary measure approximation.
2. Consecutive positive triples imply a global ordinary face only in the
   already-established ordered-chain setting (for example an `x`-ordered
   simple chain).  The transcript theorem itself supplies homogeneous
   consecutive orientations, not simplicity or the ambient order.

The exact numerical verifier is

```text
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_entropy_semialgebraic_transcript.py
```

It checks the KL partition identity, child-product correction, binary
high-node charge, transcript-depth accounting, (6) on exact rational random
laws and block regressions, and the entropy-to-distinct-support inference.

## 1. Weighted constant-error rectangle partition

The only geometric input is the fixed-arity homogeneous rectangle theorem.
For planar orientation it says that there is an absolute `alpha>0` such
that, for three finite point classes with uniform weights, either the
positive relation or its complement contains a product rectangle whose
three coordinate subsets each have relative size at least `alpha`.

This is Lemma 4.1 of Fox--Pach--Suk, obtained by applying their density
theorem at density at least one half.  Strict positivity and its complement
are both constant-complexity semialgebraic relations.  The explicit local
constant used in the companion audit may be taken as

\[
                         \alpha={1\over8\,3^{120}},       \tag{7}
\]

although its value is irrelevant here.

### Weighted extension

Let `mu_1,mu_2,mu_3` be probability weights on finite coordinate classes.
For rational weights, replace a point of weight `a/N` by `a` labeled twin
clones carrying the same coordinates.  Apply the uniform theorem to the
three clone classes.  If `A'_i` is the clone subset returned in class `i`,
let `A_i` be its coordinate support.  Every transversal of
`A_1 x A_2 x A_3` has a transversal of selected clones with the
same coordinates, hence the same relation value.  Moreover

\[
                         \mu_i(A_i)\ge {|A'_i|\over N}\ge\alpha.          \tag{8}
\]

Thus the support rectangle is homogeneous and has the required weighted
coordinate masses.  Labeled twins cause no geometric issue: the
semialgebraic predicate depends only on their coordinate image, and the
partite density proof counts vertices with multiplicity.  Approximate
arbitrary finite weights by rationals.  There are only finitely many
support rectangles, so a constant subsequence gives (8) in the limit.

This proves the weighted homogeneous-subrectangle theorem without asking a
regularity partition to respect clone fibers.

### Constant-error partition

Start from any product rectangle `U_1 x U_2 x U_3` with product law
`Q=mu_1mu_2mu_3`.  If it is nonhomogeneous, use (8) to find a homogeneous
subrectangle `A_1 x A_2 x A_3` with at least an `alpha` share of
each conditional coordinate weight.  Splitting every `U_i` into `A_i` and
its complement partitions the parent into eight product rectangles, one of
which is homogeneous and has conditional `Q`-mass at least `alpha^3`.

Do this simultaneously in every currently nonhomogeneous leaf for

\[
 t_0=\left\lceil{\log(1/4)\over\log(1-\alpha^3)}\right\rceil            \tag{9}
\]

rounds.  The remaining nonhomogeneous leaves have total `Q`-mass at most
`1/4`.  The final collection is a disjoint partition into at most

\[
                              B_0=8^{t_0}                 \tag{10}
\]

exact product rectangles.  This is the constant-error weighted regularity
statement needed below.  It is partite from the outset and avoids the
same-part issue in converting the nonpartite equitable formulation of the
polynomial regularity lemma.

## 2. The recursive transcript

At a node `v`, let `P_v` be the conditional input law on its current
product rectangle and let

\[
                              Q_v=(P_v)_X(P_v)_Y(P_v)_Z.  \tag{11}
\]

Apply Section 1 to partition the rectangle into at most `B_0` product
children.  Terminate every homogeneous child.  A homogeneous negative or
zero child has `P_v`-mass zero because `P_v` is supported on (1).  Recurse
on every nonhomogeneous child.

Let `mathcal E_v` be the union of the nonhomogeneous child indices, and put

\[
 \theta_v=P_v(\mathcal E_v),\qquad
 \eta_v=Q_v(\mathcal E_v)\le1/4.                         \tag{12}
\]

Every positive-mass terminal child is therefore a positive homogeneous
product rectangle.  Nested rectangle intersections keep every later node
an exact product.

## 3. The KL potential telescope

Let `J` be the child index at node `v`, with laws `p_J,q_J` under `P_v,Q_v`.
For a child rectangle `j`, let `Q_{v,j}` be `Q_v` conditioned on that
rectangle.  It is still a product law.  The KL chain rule gives

\[
 \operatorname{TC}(P_v)
 =D(p_J\Vert q_J)+
      \sum_jp_jD(P_{v,j}\Vert Q_{v,j}).                  \tag{13}
\]

There is a small but important correction here: `Q_(v,j)` need not be the
product of the **child** marginals.  Nevertheless

\[
 D(P_{v,j}\Vert Q_{v,j})
 =\operatorname{TC}(P_{v,j})+
   \sum_{i=1}^3D((P_{v,j})_i\Vert(Q_{v,j})_i)
 \ge\operatorname{TC}(P_{v,j}).                         \tag{14}
\]

Thus data processing from `J` to the exceptional indicator yields

\[
 \operatorname{TC}(P_v)
 \ge d_2(\theta_v\Vert\eta_v)
       +\sum_{j\in\mathcal E_v}p_j\operatorname{TC}(P_{v,j}).           \tag{15}
\]

Call a node **high** if `theta_v>1/2`.  Since `eta_v<=1/4`,

\[
 d_2(\theta_v\Vert\eta_v)
 \ge c_*=d_2(1/2\Vert1/4)
       ={1\over2}\log{4\over3}>0.                       \tag{16}
\]

If `pi_v` is the probability of reaching `v`, telescoping (15) over any
finite truncation gives

\[
                      \sum_{v\ {\rm high}}\pi_vc_*
                                  \le\operatorname{TC}(P).              \tag{17}
\]

At a low node at least `pi_v/2` input mass terminates immediately.  These
terminal masses are disjoint for different low nodes, so

\[
                              \sum_{v\ {\rm low}}\pi_v\le2.             \tag{18}
\]

The expected number `L` of partition steps is the sum of all internal-node
reach probabilities.  Equations (17)--(18) prove

\[
                         \mathbb E L\le2+{operatorname{TC}(P)\over c_*}.
                                                                    \tag{19}
\]

In particular the recursion terminates almost surely.  With finite support,
every positive-mass atom terminates at finite depth.

Each step has at most `B_0` outcomes.  The entropy chain rule along the
tree, or the usual prefix-code inequality, gives

\[
 H(C)\le(\log B_0)\mathbb E L
       \le(\log B_0)\left(2+{\operatorname{TC}(P)\over c_*}\right),     \tag{20}
\]

which is (3).  No geometric parameter grows with the support.

## 4. Consecutive triples and the factor two

Let `W=(X_1,...,X_r)` have an arbitrary finite joint law.  By the chain rule,

\[
 R_{\rm ent}=\sum_iH(X_i)-H(W)
   =\sum_{i=2}^rI(X_i;X_1,...,X_{i-1}).                  \tag{21}
\]

For one window,

\[
 \operatorname{TC}(X_j,X_{j+1},X_{j+2})
 =I(X_{j+1};X_j)+I(X_{j+2};X_j,X_{j+1}).                \tag{22}
\]

Data processing bounds the first term by the chain increment in (21) at
`i=j+1`, and the second by the increment at `i=j+2`.  Summing (22), the
first family uses a subset of the increments in (21), and so does the
second.  This proves (6).  No stationarity, Markov property, or equal
support size is used.

Apply Theorem (3) separately to the `r-2` consecutive triple laws.  Let
`C_j` be their leaf transcripts.  Then

\[
 H(C_1,...,C_{r-2})
 \le\sum_jH(C_j)
 =O\left(r+\sum_j\operatorname{TC}_j\right)
 =O(r+R_{\rm ent}).                                      \tag{23}
\]

Fix one combined transcript value `c` of maximum probability.  Shannon
entropy satisfies

\[
                       \Pr[C=c]\ge2^{-H(C)}.             \tag{24}
\]

For uniform selected words, (24) retains at least the number in (5) of
**distinct** words.  This is not merely incidence mass: the transcript is
a deterministic function of the word.

For coordinate `i`, intersect the one, two, or three leaf-coordinate sets
assigned to it by the consecutive triple transcripts.  These intersections
form a global product cell.  Every consecutive triple product is a subset
of its positive homogeneous leaf rectangle.  All retained words lie in
the global cell, proving the claimed exact product intersection.

## 5. Stress tests and sharpness

The diagonal parabola family in
`SEMIALGEBRAIC_CONSECUTIVE_TRIPLE_AUDIT.md` has one selected matching triple
per index and requires one homogeneous leaf per selected index.  For one
block with `N` indices,

\[
                         H(C)=\log N,qquad
                         \operatorname{TC}(P)=2\log N.   \tag{25}
\]

Thus it is fully consistent with (3); the correlation charge is necessary.
For `d` independent blocks,
`R_ent=R_supp=2d log N`, and the retained-cell loss allowed
by (5) is quadratic, exactly as the barrier requires.

The constant in (20) is not intended to be quantitative.  With (7), the
macro branching `B_0` in (10) is astronomical.  At coefficient scale this
is still an absolute constant per unit of total correlation, hence produces
the asserted `O(r+R_ent)` exponent.  Improving the constant has no bearing on
the proof interface.

## 6. Audit conclusion

All four proposed danger points have exact resolutions.

* **Partite/weighted/clones:** use the partite homogeneous rectangle
  theorem, clone only to obtain one weighted homogeneous support rectangle,
  then build the constant-error partition by product splits.
* **Exact product intersections:** every recursive child is a rectangle;
  coordinatewise intersections of overlapping triple leaves remain a
  rectangle and preserve positivity by restriction.
* **KL chain rule:** the conditioned parent-product law is not the child
  marginal product, but the correction in (14) is nonnegative.
* **Entropy to distinct words:** after the weighted lemma is rounded before
  recursion, the transcript is deterministic, so the maximum transcript
  atom literally contains `M Pr[C=c]` selected words.

Subject only to the pre-existing ordered-chain implication from positive
consecutive turns to an ordinary convex face, the entropy-sensitive
semialgebraic extraction gate is certified.
