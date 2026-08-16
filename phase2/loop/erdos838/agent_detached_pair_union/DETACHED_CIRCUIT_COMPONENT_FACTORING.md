# Detached circuits: exact component factoring and the irreducible child

**Date:** 2026-08-14.  All logarithms are base two.

## Verdict

There is an exact summed detached-shield theorem, but it stops at one
precisely identified child.  Partition the completion support into arbitrary
containers and join two containers when a bad planar four-circuit meets both.
The connected components of this circuit graph are not merely approximately
independent: their entire ordinary convex-face complexes form a direct
simplicial product.  If the component face counts are `V_a`, then

\[
                              V(Z)=\prod_a V_a.              \tag{1}
\]

For a uniform random completion, let `h_a` be the entropy of its trace in
component `a`, and let `M` be the number of completions.  Then the exact
Kraft/total-correlation identity is

\[
 \boxed{\log {V(Z)\over M}
   =\underbrace{\left(\sum_a h_a-\log M\right)}_{\rm correlation}
    +\sum_a\underbrace{(\log V_a-h_a)}_{\rm local\ shield\ surplus}.} \tag{2}
\]

Thus independent circuit containers automatically multiply their full
detached shields, with no additional strong-glue assumption and no overlap
loss.  If this product fails to give `D^gamma` gain, both the total
correlation and the sum of all local shield surpluses are below
`gamma log D`.  A weighted entropy/rank inequality then localizes essentially
the original entropy density in one **circuit-connected** child.

That last child is genuinely necessary.  An exact rational scalable family
has four macroscopically separated pockets, `L` nested triangles per pocket,
and `M=L^4` rank-12 completion faces.  Every two distinct completions have a
nonconvex detached union, but strict `3+1` circuits run between neighboring
pockets and make the circuit graph connected.  Hence geographic separation
of the pockets, or localization of the completion-pair witness to a first
differing pocket, does **not** justify multiplying the four unrestricted
local complexes.

The remaining statement is therefore not “sum independent container
shields”—that is (1).  It is a quantitative theorem inside a single
circuit-connected support, or a use of the `D` extension labels/common-base
histories that survives this localization.  A theorem about the unrestricted
complex of that one child alone risks being an Erdős-838-equivalent
restatement.

## 1. Four-local direct-product theorem

Let `Z` be a finite planar point set in general position and let

\[
                         Z=X_1\sqcup\cdots\sqcup X_s       \tag{3}
\]

be any partition.  A **bad circuit** is a four-set which is not in convex
position.  Define the circuit graph `G` on `[s]` by joining distinct `i,j`
when some bad circuit meets both `X_i` and `X_j`.  Let
`C_1,...,C_t` be its connected components, put

\[
                 Z_a=\bigcup_{i\in C_a}X_i,\qquad
                 V_a=|\mathcal F(Z_a)|,                    \tag{4}
\]

and include the empty face in every complex.

> **Theorem 1 (circuit-component factoring).**  The restriction of the
> convex-position complex to `Z` is the simplicial join
> 
> \[
>             \mathcal F(Z)=\mathcal F(Z_1)*\cdots*
>                            \mathcal F(Z_t).               \tag{5}
> \]
> 
> In particular, (1) holds exactly.

**Proof.**  One implication in (5) follows by deletion.  Conversely, suppose
`F intersect Z_a` is convex for every `a`, but `F` is not.  Planar
Caratheodory gives a bad four-set `C subset F`.  It cannot lie in one `Z_a`, since the
corresponding local trace is convex.  It therefore meets two original
containers in different components.  Those two containers are adjacent in
`G` by the definition of `G`, a contradiction.  This proves (5), and the
face choices in distinct components are uniquely recoverable, giving (1).
QED.

The theorem works equally well if one defines the graph directly on labels.
The container version is useful because a first-divergence descent already
comes with named local supports.  Notice that circuits wholly inside one
container do not create graph edges; they are counted exactly by its local
complex.

## 2. Exact Kraft and total-correlation identities

Let `\mathcal Q\subseteq\mathcal F(Z)` be `M` distinct completion faces and
let `Q` be uniform on `\mathcal Q`.  Write

\[
 Q_a=Q\cap Z_a,\qquad h_a=H(Q_a),\qquad
 T=\sum_a h_a-H(Q).                                      \tag{6}
\]

The tuple `(Q_1,...,Q_t)` determines `Q`, so `H(Q)=log M` and `T>=0` is the
total correlation of the component traces.  Also every value of `Q_a` is a
face of `Z_a`, hence `h_a<=log V_a`.  Taking logarithms in (1) gives (2).

There is also a count-only form.  If `M_a` is the number of distinct
component traces, then

\[
 {V(Z)\over M}
  =\left(\prod_a{V_a\over M_a}\right)
    \left({\prod_aM_a\over M}\right).                     \tag{7}
\]

Both factors on the right are at least one.  The first is the product of
the unrestricted local shield surpluses; the second is the exact projection
redundancy/Kraft factor.  Consequently

\[
 V(Z)<D^\gamma M
 \quad\Longrightarrow\quad
 T<\gamma\log D,
 \qquad
 \sum_a(\log V_a-h_a)<\gamma\log D.                       \tag{8}
\]

Thus a failure of fixed-power expansion cannot be blamed on uncontrolled
overlap between independent detached banks: component identity is retained
by the output face itself.

## 3. Entropy-density localization

Put

\[
             \rho_a=\mathbb E|Q_a|,qquad
             g_a=\log V_a-h_a.                            \tag{9}
\]

If every completion has rank `q`, then `sum_a rho_a=q`.  For every
`lambda>=0`, weighted averaging gives a component with `rho_a>0` such that

\[
 {h_a-\lambda g_a\over\rho_a}
 \ge {\log M-\lambda\log(V(Z)/M)\over q}.                 \tag{10}
\]

Indeed, sum the numerators.  Since `sum h_a>=log M` and
`sum g_a<=log(V(Z)/M)` by (2), their sum is at least the numerator on the
right; divide by `sum rho_a=q`.

At the live scale

\[
       \log M=\Theta((\log D)^2),\qquad q=\Theta(\log D), \tag{11}
\]

failure of a `D^gamma` product bank changes the right side of (10) by only
`O_gamma(1)`.  Hence one circuit-connected component retains the leading
`Theta(log D)` entropy per expected completion label.  This is the rigorous
decision-tree alternative:

* multiple circuit components pay by the exact product (1)--(2); or
* all leading entropy can be localized to a circuit-connected descendant.

Iteration does not lose an ambient-container factor.  The potential in
(10) is additive, so the usual first-divergence/Kraft loss is precisely the
already visible `log(V/M)` term.

## 4. Exact splice with the extension labels

The component theorem can be applied without discarding the live
one-point-extension alphabet.  Suppose every rank-`q` completion `Q` has a
set `Y_Q` of exactly `D` labels such that

\[
                         Q\cup\{y\}\in\mathcal F(P)
                         \qquad(y\in Y_Q).                 \tag{11a}
\]

Let `\mathcal S` be the family of distinct rank-`q+1` faces produced in
(11a).  The map `(Q,y) -> Q union {y}` has load at most `q+1`: once its
output `R` and the distinguished label `y in R` are specified,
`Q=R-{y}`.  If completion and extension labels belong to disjoint named
classes, as in the live outer/internal decomposition, the load is one.
Write `mu` for either valid decoder bound.  Therefore

\[
                         |\mathcal S|\ge {DM\over\mu},
               \qquad \mu\le q+1.                         \tag{11b}
\]

> **Corollary 2 (extension-preserving localization).**  If
> 
> \[
>                       V(P)\ge\mu D^\epsilon|\mathcal S|, \tag{11c}
> \]
> 
> then `D^2M<=D^(1-epsilon)V(P)`.  Otherwise apply (2) and (10), with
> `mathcal S` as the completion family and rank `q+1`.  For every
> `lambda>=0`, one circuit component satisfies
> 
> \[
> {h_a-\lambda g_a\over\rho_a}
> \ge {\log(DM/\mu)-\lambda(\epsilon\log D+\log\mu)
>        \over q+1}.                                      \tag{11d}
> \]

The first assertion follows immediately from (11b).  For the second,
failure of (11c) bounds `log(V/|mathcal S|)` by
`epsilon log D+log mu`, and (10) applies.  In the live disjoint-role cell,
`mu=1`, so there is no decoder loss at all.  Thus the extension alphabet
does not have to be erased before the circuit descent.  Either its extra
`log D` entropy creates the required fixed-power surplus, or it survives in
the trace distribution of one circuit-connected extended child.  Equation
(11d), rather than a completion-only maximal layer, is the sharper object a
final local theorem should use.

There is a second exact test inside each extension star.  Fix a common face
`F` and assume `F union Q union {y}` is ordinary for every `y in Y_Q`.  Let
`E_2` count the indexed unordered pairs for which

\[
                         F\cup Q\cup\{y,z\}\in\mathcal F(P). \tag{11e}
\]

The disjoint outer/internal roles recover `(Q,{y,z})` from the face, so
these are `E_2` distinct ordinary outputs.  Therefore

\[
 E_2\ge D^{1+\epsilon}M
 \quad\Longrightarrow\quad
 D^2M\le D^{1-\epsilon}V(P).                              \tag{11f}
\]

If (11e) fails, a bad four-circuit must contain **both** `y,z`: a circuit
missing either one lies in one of the assumed one-point-extension faces.
Its other two labels form a root pair in `F union Q`.  Hence, when (11f)
fails, at least half the completions have a root pair which supports at
least

\[
 {\binom D2-2D^{1+\epsilon}\over
       \binom{|F|+q}{2}}                                  \tag{11g}
\]

bad extension pairs.  This follows by first discarding the completions with
more than `2D^(1+epsilon)` compatible pairs and then pigeonholing their bad
pairs among the possible roots.  Equations (11e)--(11g) are the exact
extension-star compatible-pair/spanning-tree alternative.

The rooted branch cannot be closed from its circuit graph alone, even if
one root supports **every** extension pair.

> **Proposition 3 (rooted universality barrier).**  Given any finite rational
> planar order type `Y` in general position, there is an affine copy `Y'`
> and two rational points `u,v` such that every triangle `{u,v,y}` is
> ordinary, but
> 
> \[
>                    \{u,v,y,z\}\notin\mathcal F(P)
>                         \qquad(y\ne z\in Y').             \tag{11h}
> \]
> 
> The induced order type on `Y'` is exactly the prescribed one.

**Proof.**  Choose a generic affine height coordinate, translate it so the
distinct heights `h_i` are positive, and let `x_i` be the transverse
coordinate.  Apply the order-type-preserving affine map

\[
                          (x_i,h_i)\longmapsto(\delta x_i,h_i). \tag{11i}
\]

Put `u=(-1,0),v=(1,0)`.  If `h_i<h_j`, the horizontal section of the
triangle `uvy_j` at height `h_i` is centered at
`delta h_i x_j/h_j` and has half-width `1-h_i/h_j`.  Since the set is
finite, a positive rational `delta` can be chosen so that

\[
       \delta|h_jx_i-h_ix_j|<h_j-h_i                     \tag{11j}
\]

for every pair.  Then `y_i` lies strictly inside `conv{u,v,y_j}`.  This
proves (11h), while (11i) preserves every orientation among labels of `Y`.
Avoiding the finitely many additional values of `delta` which create a
root-involving collinearity makes the whole configuration general position.
QED.

Thus a monochromatic rooted circuit clique, a rooted spanning tree, or even
the complete rooted bad graph can hide an **arbitrary** detached `D`-point
order type.  Extracting a `D^epsilon` bank from that object alone is the
unrestricted one-pocket problem.  What remains usable is correlation across
the quadratically many distinct extension stars: common-root reuse must be
charged together with their recoverable `Q` labels, not by a per-star
circuit argument.

The barrier is compatible with the whole completion residue, not only with
one isolated star.

> **Proposition 4 (simultaneous two-shield regression).**  Given integers
> `s,L>=2` and any rational `D`-point order type `Y`, there is a rational
> general-position configuration with a common root face `F={u,v}` and
> 
> \[
>              M=L^s\quad\hbox{rank-}3s\quad
>              \hbox{completions }Q_w\quad(w\in[L]^s)     \tag{11k}
> \]
> 
> such that:
> 
> 1. `F union Q_w union {y}` is ordinary for every `w,y`;
> 2. `Q_w union Q_w'` is nonconvex for every `w ne w'`;
> 3. `F union Q_w union {y,z}` is nonconvex for every `w` and `y ne z`,
>    witnessed by the same root pair `u,v`; and
> 4. the detached extension set has exactly the prescribed order type `Y`.

**Construction.**  Take `s+1` vertices in strict convex position.  At each
of the first `s` vertices make a sufficiently small outward lexicographic
blow-up containing `L` nested triangles, and let a completion choose one
whole triangle from every blow-up.  At the last vertex use `u,v` as the
base of the local outward triangle and insert the affine-flattened copy from
Proposition 3.  Macro strict convexity proves item 1.  At the first coordinate
where two words differ, one selected triangle lies inside the other, proving
item 2.  Proposition 3 proves items 3--4.  All conditions are finite and
strict, so successive scales and then a generic rational perturbation give
general position.  QED.

Taking `s=Theta(log D)` and `L=D^a` makes (11k) a genuine
`2^{Theta((log D)^2)}` family of rank `Theta(log D)` with a common `D`-repair
alphabet.  It is not a counterexample to the desired inequality: its
detached local shield complexes pay.  It is an exact counterexample to a
structural shortcut claiming that connectedness plus the disjoint `DM`
extension stars must itself create a compatible-pair bank.  The quantitative
proof must count and globally recover the two detached shields.

## 5. A realizable connected regression

The following construction kills a tempting overstrengthening of Theorem 1.
Take four macro centers at the vertices of a square.  Near each center put a
very small outward-facing triangle.  Inside it put `L` strictly nested
near-homothetic triangles

\[
                       T_{j,1}\subset\cdots\subset T_{j,L}
                       \qquad(j=1,2,3,4).                  \tag{12}
\]

The triangles can be confined to an arbitrarily small neighborhood of their
macro centers.  For a word `w in [L]^4`, set

\[
                         Q_w=\bigcup_{j=1}^4T_{j,w_j}.      \tag{13}
\]

Choose the macro triangles thin enough that every `Q_w` is a strict convex
12-gon.  These are finitely many open orientation inequalities.  Homothetic
nesting gives, for `w ne w'`, an index `j` where one of the selected
triangles lies strictly inside the other.  Therefore

\[
             |\mathcal Q|=L^4,\qquad |Q_w|=12,\qquad
             Q_w\cup Q_{w'}\notin\mathcal F(P).            \tag{14}
\]

A sufficiently small generic rational perturbation preserves all strict
containments and completion faces while removing every collinearity.  Thus
(14) is a scalable exact planar family of pairwise detached-incompatible
rank-12 completions.

It is false that the four macro pockets are circuit-independent.  In the
rational square model the checker finds strict bad circuits with three
points in pocket `j` and one in pocket `j+1`, for every cyclic `j`.  The
circuit graph of the four pockets is connected.  Geometrically, a triangle
from a neighboring macro changes which of two nearly radial nested-layer
points is exposed.  Shrinking the pockets does not remove this strict local
support-order phenomenon.

The four connecting witnesses use only two fixed nested layers.  Keeping
those layers and inserting arbitrarily many additional rational homothetic
layers preserves the witnesses, so connectedness is not a small-`L`
artifact.

This distinction is important:

* the completion-pair obstruction can be certified inside a first differing
  pocket, because two complete nested triangles occur there;
* the unrestricted shield of that pocket contains mixed partial triangles;
  those partial faces need not join the other pocket shields;
* the `3+1` cross-circuits record exactly why the direct product is illegal.

Thus “all bad completion pairs have a local witness” is weaker than “all bad
four-circuits are local.”  Only the latter hypothesis triggers Theorem 1.

## 6. The irreducible child and the circularity warning

The component descent cannot prove a gain after the support becomes
circuit-connected.  This is not a technical omission.  If `P` has maximum
convex-face rank `q` and `\mathcal L_q` is its top layer, then any two
distinct members of `\mathcal L_q` have nonconvex detached union: their union
has more than `q` labels.  Hence the top layer of an arbitrary hard order
type is itself a pairwise detached-incompatible completion family.

Consequently, a theorem asserting a fixed-power surplus for every
circuit-connected pairwise detached-incompatible family, using only its
unrestricted support complex, would already be a fixed-power statement
about the total number of convex subsets versus a hard layer of an arbitrary
planar order type.  That is essentially the coefficient-scale content being
sought in Erdős 838, not a free consequence of four-locality.

The live atom must therefore retain extra structure that the top-layer
reduction forgets.  The available candidates are:

1. the `D` one-point extension labels `Y_Q` attached to every completion;
2. recoverable common-base/source histories across different cells; or
3. a genuine geometric separation theorem proving that the relevant
   first-divergence containers have no cross-circuits and hence fall under
   Theorem 1.

Equation (2) is the exact accounting interface for any such input.  It
eliminates global overlap between truly independent circuit containers and
identifies the only possible hiding place: one circuit-connected child with
near-saturated local face entropy.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_detached_pair_union/verify_detached_circuit_component_factoring.py
```

The checker uses exact rational arithmetic.  It verifies Theorem 1 on random
general-position configurations and partitions by exhaustive face
enumeration; audits (7), (2), (10), and the one-point extension decoder on
actual uniform-rank completion subfamilies; verifies the rooted universality
construction on arbitrary rational order types; verifies a finite simultaneous
completion/extension instance of Proposition 4; and constructs the perturbed
nested-triangle family.  For that regression it checks general position,
every rank-12 completion, every detached completion pair, and the connected
cross-pocket circuit graph.
