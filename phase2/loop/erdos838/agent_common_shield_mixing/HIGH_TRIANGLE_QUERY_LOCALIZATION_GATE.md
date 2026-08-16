# Reused internal triangles: source compression, mixed circuits, and the one-direction star

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The high-`Lambda_3` residue in
`DENSE_HALL_INTERNAL_TRIANGLE_CAUCHY.md` can be sharpened without losing
the `n^(Theta(log log n))` scale.

First, the five-target overlap may be replaced by the load of the old
source targets alone.  If a context has `a` old-source rows, `b` release
columns, `e<=ab` records, and `t=max(a,b)>=6`, then the old-source bank of
size `a` and the triangle bank in the larger cloud satisfy

\[
 a{t\choose3}\ge {5\over54}e^2.                         \tag{1}
\]

Consequently, if `kappa_A` is the actual weighted overlap of the compressed
old-source bank and `Lambda_triangle` is the overlap of the selected
larger-cloud triangles, then

\[
 \boxed{\displaystyle
 M\le5\kappa_A V(P)
   +\sqrt{54\over5}\sqrt{\kappa_A\Lambda_\triangle}\,V(P).}
                                                                  \tag{2}
\]

This compression is compatible with the genuine minimizer weights.  A
source is entered only once in each dyadic record-weight layer, not once
per release neighbor.  If the total canonical mark weight of one actual
source is at most one and its upstream description load is `L`, then

\[
                         \kappa_A<2L.                    \tag{3}
\]

No release-alphabet factor occurs in (3).  This is different from routing
every record directly to its source target, whose load really is multiplied
by the release degree.

Thus, for a target multiplier
`K=n^(sigma log log n)`, failure of (2) fixes an actual triangle with
weight `K^(2-o(1))` whenever `L=n^O(1)`.  The fixed triangle has an exact
geometric dichotomy.  If its union with the retained base is ordinary, the
base--triangle union is a decoded mixed output.  Otherwise, because the
base, the triangle, and every base-plus-singleton union are ordinary, a
canonical bad four-circuit is necessarily `2+2` or `3+1`.  There are only
sixteen signed fixed-triangle classes.  Hence the full scale survives in
one common cage/rooted-fan class.

The SCC/direction continuation does **not** close that class by itself.
There is an exact scalable planar family with `2^r` distinct genuine
source bases, one reused actual triangle, one common insertion direction,
and a depth-one directed star.  Its triangle load is `2^r`, with no
duplicate chronology metadata and no fourth direction query.  The family
is paid by a Boolean base bank of the same size, so it is not a low-face
counterexample.  It proves that the surviving operation is a global
source-downshadow/cyclic-profile payment, not graph-theoretic SCC or
`PGL_2` coherence alone.

For the later quasipolynomial scale-recovery gate, this residue is now
closed by `QUASIPOLY_SOURCE_TRIANGLE_TAG_CLOSURE.md`: pairing every
triangle incidence with one canonical source face costs only
`{n choose3}` decoder tags and gives a final `O(kappa_A n^(3/2))` loss.
The circuit/star analysis below remains the correct fixed-power audit.

## 1. Source-compressed internal-bank Cauchy

Let `c` range over weighted simple bipartite record contexts.  Its active
old-source targets form an actual ordinary family `mathcal A_c` of size
`a_c`.  Its other active side has size `b_c`, and its record graph has
`e_c<=a_cb_c` edges.  Every context record has common layer weight `w_c`.
Put

\[
 \kappa_A=\max_A\sum_{c:A\in\mathcal A_c}w_c.           \tag{4}
\]

For `t_c=max(a_c,b_c)>=6`, choose the rank-three bank from the larger
role-colored cloud:

\[
 \mathcal I_c=
 \begin{cases}
 {Y_c\choose3},&a_c\ge b_c,\\
 {Z_c\choose3},&b_c>a_c,
 \end{cases}
 \qquad i_c=|\mathcal I_c|={t_c\choose3}.               \tag{5}
\]

Every member is an actual ordinary triangle.  Define

\[
 \Lambda_\triangle=
   \max_T\sum_{c:T\in\mathcal I_c}w_c.                  \tag{6}
\]

> **Theorem 1 (asymmetric internal Cauchy).**  Equation (2) holds, where
> `M=sum_c w_c e_c`.  Contexts with `t_c<=5` contribute the first term;
> the other contexts contribute the second.

**Proof.**  Since `t=max(a,b)`,

\[
                at^3\ge a^2b^2\ge e^2.                 \tag{7}
\]

For `t>=6`, `{t choose3}>=5t^3/54`, proving (1).  Multiply its square-root
form by `w_c`, sum, and apply Cauchy:

\[
 \begin{aligned}
 \sum_{t_c\ge6}w_ce_c
 &\le\sqrt{54\over5}
   \sqrt{\sum_cw_ca_c}\sqrt{\sum_cw_ci_c}\\
 &\le\sqrt{54\over5}
   \sqrt{\kappa_A\Lambda_\triangle}\,V(P).
 \end{aligned}                                          \tag{8}
\]

If `t_c<=5`, then `e_c<=a_cb_c<=5a_c`; summation gives
`5 kappa_A V(P)`.  All bank overlaps in (4),(6) are computed on actual
ordinary faces, without formal context tags.  QED.

The source bank in Theorem 1 is deliberately asymmetric.  It works even
when the larger side is the release side: equation (7) uses the old-source
factor `a` and the larger-cloud triangle factor `t^3`.  No normalized load
assumption on `C,W,Q`, or `E` is needed.

### 1.1 Exact dyadic compression of genuine source weights

Suppose an actual source `A` has canonical upstream weights of total at
most one.  Its record neighbors may have unequal descendant weights
`beta<=alpha`, where `alpha` is the upstream source-mark weight.  Bucket
the positive `beta` into

\[
                  2^{-k-1}\alpha<\beta\le2^{-k}\alpha. \tag{9}
\]

Replace every edge in a nonempty bucket by its upper endpoint and enter
the source target once for that bucket.  The edge demand grows by less
than two, while the total source-target layer weight is at most

\[
                         \sum_{k\ge0}2^{-k}\alpha=2\alpha.          \tag{10}
\]

Summing canonical source marks and allowing description multiplicity `L`
proves (3).  This is the correct interface with
`MINIMIZER_WEIGHTED_LOOP_COVER_GATE.md` and
`WEIGHTED_HISTORY_DOMINATION_AND_COMPLEMENT_NO_GO.md`.

There is a tempting but incorrect alternative.  If a source of weight
`alpha` has `d` genuine released neighbors and every record is routed to
the same target `A`, that target receives load `d alpha`, not `alpha`.
Theorem 1 avoids this multiplication because it uses one source occurrence
per **layer** together with the internal triangle bank.  Dividing every
record weight by `d` would also remove the desired release multiplier and
is not an admissible repair.

### 1.2 Quantitative high-triangle localization

Let `M_thick` be the thick contribution.  If

\[
 M_{\rm thick}>K V(P),                                  \tag{11}
\]

then (8) forces

\[
             \boxed{\displaystyle
              \Lambda_\triangle>{5\over54}{K^2\over\kappa_A}.}  \tag{12}
\]

If only the total `M` is known and `5 kappa_A<=K/2`, then
`M>K V(P)` implies `M_thick>K V(P)/2` and the right side of (12) becomes
`5K^2/(216 kappa_A)`.

For `K=n^(sigma log log n)` and `kappa_A=n^O(1)`, both bounds are
`K^(2-o(1))`.  Conditioning on a polynomial number of child supports,
tangent cells, or projective chamber itineraries therefore preserves the
required `n^(Theta(log log n))` scale.

## 2. Base--triangle mixed output or one fixed circuit class

Fix an actual triangle `T={x_1,x_2,x_3}` attaining (6), and suppose the
role-colored retained base of context `c` is `B_c`.  The Hall targets give

\[
 B_c\text{ ordinary},\qquad
 B_c\cup\{x_i\}\text{ ordinary}\quad(1\le i\le3).      \tag{13}
\]

The singleton assertion uses `A` targets if `T` is on the old-source side
and `C` targets if it is on the release side.

If

\[
                         O_{c,T}=B_c\cup T               \tag{14}

\]

is ordinary, its role traces recover `B_c` and `T`.  Hence the good
incidences have the exact one-face accounting

\[
 \sum_{(c,T):\,O_{c,T}\ {m ordinary}}w_c
       \le\Lambda_{BT}V(P),                             \tag{15}
\]

where `Lambda_BT` is only the remaining actual history multiplicity of
the decoded pair `(B_c,T)`.  In particular, if at least half of the
selected triangles of every thick context are good, Theorem 1 improves to

\[
 M_{\rm thick}\le
       \sqrt{108\over5}\sqrt{\kappa_A\Lambda_{BT}}\,V(P).         \tag{16}
\]

Now suppose (14) is nonconvex.  A bad four-subset cannot lie wholly in
`B_c` or `T`.  It also cannot use one point of `T` and three of `B_c`, by
(13).  Thus every canonical bad circuit is exactly

\[
                    2T+2B\quad\hbox{or}\quad3T+1B.      \tag{17}
\]

For `2+2`, choose one of the three pairs of `T` and one of the four
possible interior labels of the four-circuit.  For `3+1`, the `T` trace is
fixed and again there are four possible interior labels.  Therefore there
are at most

\[
                            3\cdot4+1\cdot4=16           \tag{18}

\]

signed fixed-triangle classes.  Choosing the first bad circuit in a fixed
global order and pigeonholing (18) retains at least one sixteenth of the
bad incidence weight.  These are precisely the common-edge cage and
rooted-fan states; no vague nonconvexity remains.

## 3. What the SCC and direction split really says

Make every signed two-cloud circuit context a directed edge between its
two physical completed children.  With edge weights retained, strongly
connected components give an exact partition:

* every edge internal to a nontrivial component lies on a directed cycle;
* component-crossing edges form a DAG; and
* after fixing `T` and its child `X`, all retained edges are incident with
  `X`, unless an actual multi-level history identifies another occurrence
  of `X`.

Thus a fixed-triangle fibre is already a cycle-versus-oriented-star split.
The cycle branch pays by a cyclic profile product only when the profile
unions around the cycle are jointly ordinary and their decoder marks are
retained.  Graph incidence alone does not imply either property.

For the star, group the weight by actual direction queries to `X`.  For
any `0<eta<1`, either the three heaviest direction bins carry at least
`(1-eta)` of the weight, in which case one direction carries at least
`(1-eta)/3`, or weight at least `eta` lies beyond the three heaviest bins
and genuinely queries a fourth or later direction.  Only the latter is a
multiquery state on the same physical child.

For a child of size `N` queried in `q` retained directions, its coherent
profile itinerary has at most

\[
                             O((qN^2)^3)                 \tag{19}

\]

possibilities by the projective-hyperplane theorem in
`BAD_PAIR_RANK4_PIQ_CLASSIFICATION.md`.  At the scale of (12), fixing this
itinerary loses only `2^O(log n)`.  Equation (19) is a localization cost,
not an ordinary-face bank.  In particular, up to three directions can be
independently reset by `PGL_2`, and even four coherent directions do not
by themselves make the corresponding profile unions ordinary.

## 4. Exact planar one-direction star barrier

The following construction shows that high triangle reuse need not enter
the fourth-direction branch, even after duplicate histories are removed.
Let

\[
 a=(0,0),\quad b=(4,0),\quad d=(4,4),\quad c=(0,4),     \tag{20}
\]

and put `delta=1/3600` and

\[
 P_t=(2-\delta t^2,-1/5+\delta t),\qquad1\le t\le6.    \tag{21}
\]

Fix `T={P_1,P_2,P_3}`.  For any `r>=1`, put

\[
 s_k={4k\over r+1},\qquad
 q_k=\left(s_k,5-{(s_k-2)^2\over10}\right),
       \qquad1\le k\le r.                              \tag{22}
\]

Let `S={q_1,...,q_r}` and, for every `R subseteq S`, define

\[
                         B_R=\{a,b,d,c\}\cup R.         \tag{23}

\]

The upper points in (22), together with `c,d`, have strictly decreasing
successive slopes.  Hence every `B_R` is ordinary.  The points (21) are
singleton ears at the opposite edge `ab`, so nonadjacent-ear composition
gives

\[
                         B_R\cup\{P_t\}\text{ ordinary}             \tag{24}
\]

for every `R,t`.  On the other hand, the strict determinant calculation
for the parabolic blocker gives

\[
                 P_2\in\operatorname{int}\triangle(P_1,P_3,c).     \tag{25}

\]

Therefore `B_R union T` is nonconvex for every `R`.  All `2^r` contexts
reuse the same actual triangle and the same bottom-edge query direction.
Their actual source/base targets are distinct, so unit weights obey the
per-source cap and there is no chronology duplication.  The directed
query graph is an outward depth-one star and has no directed cycle or
fourth direction.

This is not an EIC' construction: the `2^r` faces `B_R` are already a
Boolean bank, and (24) gives six more such banks.  It is the exact
bounded-depth hierarchy payment missing from graph theory.  Taking

\[
                   r=\lceil2\sigma(\log n)(\log\log n)\rceil       \tag{26}

\]

uses only `o(n)` labels and gives triangle load
`2^r=n^(2sigma log log n+o(1))`, exactly the scale forced by (12).
Arbitrary extra general-position labels may pad the ambient set to `n`;
ordinary-subset status is intrinsic and is unchanged.

The remaining global theorem must therefore say that many such DAG/star
fibres cannot reuse their Boolean source/downshadow payment without
creating a cyclic profile bank or an actual chronology mark.  Neither SCC
decomposition nor coherent-itinerary counting states that theorem.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_high_triangle_query_localization.py
```

The checker verifies (1)--(2) for every side-size pair through 100,
audits rational dyadic and Cartesian-release weights, exhausts the
sixteen circuit signatures, checks the SCC/direction alternatives, and
enumerates every Boolean base in (20)--(25) through `r=10` using exact
rational convex-hull arithmetic.  All audited configurations are in
general position.  At arbitrary `r`, an arbitrarily small rational generic
perturbation preserves the finite strict inequalities if an accidental
cross-family collinearity occurs.
