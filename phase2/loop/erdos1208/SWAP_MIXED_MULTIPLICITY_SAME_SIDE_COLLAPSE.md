# Mixed multiplicity: an exact same-side envelope and its barrier

## 1. Outcome

The mixed projected-key population has two logically different pieces:
simple occupied support and reuse of the same mixed key pair in several
endpoint groups.  This note gives an exact same-side envelope for the
second piece, then shows on the genuine hard rows that the envelope is far
too large.  The conclusion is a sharp no-go: mixed multiplicity cannot be
decoupled into separate `V` and `W` reuse energies.  The joint overlap of
the two role types is load-bearing.

Let `mathfrak G` be any finite family of endpoint groups.  A group `g`
contains a set `V_g` of projected moving-`V` keys and a set `W_g` of
projected moving-`W` keys.  Put

\[
 c(v,w)=|\{g:v\in V_g,\ w\in W_g\}|,                 \tag{1.1}
\]

and define the mixed incidence mass, support, and repeated-pair energy by

\[
 I_{VW}=\sum_{v,w}c(v,w),\qquad
 S_{VW}=|\{(v,w):c(v,w)>0\}|,                       \tag{1.2}
\]

\[
 C_{VW}=\sum_{v,w}{c(v,w)\choose2}.                 \tag{1.3}
\]

For one side, let

\[
 \mu_V(v)=|\{g:v\in V_g\}|,\qquad
 L_V=\sum_v{\mu_V(v)\choose2},                     \tag{1.4}
\]

and define `mu_W,L_W` symmetrically.  If

\[
 c_V(v,v')=|\{g:v,v'\in V_g\}|,
\]

put

\[
 C_{VV}=\sum_{\{v,v'\}}{c_V(v,v')\choose2},        \tag{1.5}
\]

and similarly define `C_WW`.  Then

\[
\boxed{
 C_{VW}\le C_{VV}+C_{WW}+\min\{L_V,L_W\}.}          \tag{1.6}
\]

Consequently

\[
\boxed{
 I_{VW}\le S_{VW}+C_{VV}+C_{WW}+\min\{L_V,L_W\}.}  \tag{1.7}
\]

Algebraically, pair multiplicity is bounded by three already geometric
populations:

1. reuse of one projected key in two groups, to which the four-norm inverse
   applies;
2. reuse of a pair of `V` keys; and
3. reuse of a pair of `W` keys.

The stress in Section 5 shows that this is not a target-scale reduction.
The last two quantities in (1.6) are the *full* same-side group energies.
They may include two keys from one neighbour fibre, whereas the existing
three-channel scalar theorem was stated for different neighbour fibres.
Section 3 separates their diagonal auxiliary remainder into one explicit
two-group physical-bundle population.  That population is enormous even
when the true mixed collision is small.  Hence (1.7) is a structural
classification and a rigorous barrier, not a closing reduction.

## 2. Exact group-overlap identity

For distinct groups `g,h`, write

\[
 a_{gh}=|V_g\cap V_h|,\qquad b_{gh}=|W_g\cap W_h|. \tag{2.1}
\]

Double counting a mixed key pair together with two witnessing groups gives

\[
\boxed{
 C_{VW}=\sum_{g<h}a_{gh}b_{gh}.}                    \tag{2.2}
\]

On one side the corresponding identities are

\[
 L_V=\sum_{g<h}a_{gh},\qquad
 C_{VV}=\sum_{g<h}{a_{gh}\choose2},                \tag{2.3}
\]

and likewise for `W`.  For nonnegative integers `a,b`, assume `a>=b`.
Then

\[
 {a\choose2}+{b\choose2}+b-ab
 ={(a-b)(a-b-1)\over2}\ge0.                       \tag{2.4}
\]

Therefore

\[
 ab\le {a\choose2}+{b\choose2}+\min\{a,b\}.       \tag{2.5}
\]

Sum (2.5), use (2.2)--(2.3), and bound
`sum min(a_gh,b_gh)` by both `L_V` and `L_W`.  This proves (1.6).
Finally, every positive integer `c` satisfies

\[
 c\le1+{c\choose2}.                                \tag{2.6}
\]

Summing (2.6) over occupied mixed pairs and applying (1.6) proves
(1.7).

There is also a sharp density diagnostic.  Cauchy--Schwarz on the occupied
support gives

\[
 I_{VW}^2\le S_{VW}(I_{VW}+2C_{VW}),               \tag{2.7}
\]

so any substantial gap between incidence mass and support forces the
same-side populations in (1.6).

## 3. The same-side diagonal is a physical-edge bundle

Every projected key occurrence in a geometric group has a unique neighbour
fibre.  Fix two groups `g,h` and one role type.  Their `a=a_gh` common keys
form a bipartite multigraph `B_gh`: the left vertex of a common key is its
neighbour fibre in `g`, and the right vertex is its neighbour fibre in `h`.
Parallel edges are allowed because distinct keys can use the same two
fibres.

Let `D_gh` be the number of unordered pairs of edges in `B_gh` with no
common endpoint, and let `Delta_gh` be its maximum vertex degree.  Every
non-disjoint edge pair is incident to one of the two endpoints of either
edge.  Hence

\[
 {a\choose2}-D_{gh}\le a(\Delta_{gh}-1),          \tag{3.1}
\]

or equivalently

\[
 {a_{gh}\choose2}
 \le D_{gh}+a_{gh}(\Delta_{gh}-1).                \tag{3.2}
\]

Let `C_VV^cross` count collisions of a fixed pair of `V` keys which occupy
different neighbour fibres in each witnessing group.  Double counting two
keys and two groups gives

\[
 C_{VV}^{\rm cross}=\sum_{g<h}D_{gh}.              \tag{3.3}
\]

Consequently

\[
\boxed{
 C_{VV}\le C_{VV}^{\rm cross}
 +\sum_{g<h}a_{gh}(\Delta^V_{gh}-1),}              \tag{3.4}
\]

and symmetrically for `W`.  Combining (1.7) and (3.4) gives

\[
\boxed{
\begin{aligned}
 I_{VW}\le {}&S_{VW}+C_{VV}^{\rm cross}+C_{WW}^{\rm cross}
             +\min\{L_V,L_W\}\\
 &+\sum_{g<h}\bigl[
 a_{gh}(\Delta^V_{gh}-1)+b_{gh}(\Delta^W_{gh}-1)
 \bigr].
\end{aligned}}                                      \tag{3.5}
\]

The two cross terms in (3.5) are precisely the population addressed by the
existing same-role three-channel codegree minima.  The only new
multiplicity term is the final fibre-star sum.  A large summand means that
two distinct endpoint groups reuse many identical projected keys through
one fixed neighbour fibre in one of the groups.  This retains both group
owners, the common projected keys, and the literal neighbour cell; it is a
sharper density-increment object than full same-side energy.

For the actual projected keys this general star has an exact further
collapse.  A `V` key is `(r,A)` and its physical directed edge is `A+r`; a
`W` key is `(r,B)` and its physical directed edge is `B`.  In one fixed
endpoint group and oriented role, the physical edge determines the
neighbour fibre: the neighbour is `(c+t,ell+Lt)`, so its first coordinate
determines `t` in the `V` role and its second coordinate does so in the `W`
role.  Consequently two common keys use the same part in `g` if and only if
they have the same physical edge, if and only if they use the same part in
`h`.

Thus `B_gh` is a matching of part pairs with possible parallel edges.  If

\[
 m_{gh}(e)=|\{\hbox{common keys of physical edge }e\}|,       \tag{3.6}
\]

then exactly

\[
 {a_{gh}\choose2}=D_{gh}+\sum_e{m_{gh}(e)\choose2}.          \tag{3.7}
\]

Define the physical-bundle energies

\[
 B_V=\sum_{g<h}\sum_e{m^V_{gh}(e)\choose2},qquad
 B_W=\sum_{g<h}\sum_e{m^W_{gh}(e)\choose2}.                 \tag{3.8}
\]

Then (3.4) sharpens to the identities

\[
 C_{VV}=C_{VV}^{\rm cross}+B_V,qquad
 C_{WW}=C_{WW}^{\rm cross}+B_W,                            \tag{3.9}
\]

and (3.5) sharpens to

\[
\boxed{
 I_{VW}\le S_{VW}+C_{VV}^{\rm cross}+C_{WW}^{\rm cross}
       +\min\{L_V,L_W\}+B_V+B_W.}                          \tag{3.10}
\]

The new diagonal survivor is therefore a precise `d=0` same-role cell:
two distinct endpoint groups reuse two or more projected shifts over one
literal oriented physical edge.  There is no general neighbour-star
geometry left.

## 4. Load-layer form

Every mixed codegree satisfies

\[
 c(v,w)\le\min\{\mu_V(v),\mu_W(w)\}.              \tag{4.1}
\]

If `H_r` is the subgraph of the simple mixed support induced by keys of
group load at least `r` on both sides, then the layer-cake identity gives

\[
 \sum_{(v,w)\in E(H)}\min\{\mu_V(v),\mu_W(w)\}
 =\sum_{r\ge1}|E(H_r)|.                            \tag{4.2}
\]

Hence

\[
 I_{VW}\le\sum_{r\ge1}|E(H_r)|.                   \tag{4.3}
\]

This is the exact high-reuse alternative to (1.7).  It should not be used
naively: on a mostly simple support, (4.3) can overcount every edge by a
large endpoint load.  The preferred split is (1.7) for multiplicity and
the coloured-rectangle theorem for `S_VW`.

## 5. Exact geometric stress: the separate-side relaxation is dead

The augmented optimal-core analyzer gives the following rows on transformed
Costas sizes `29,31,37`:

\[
\begin{array}{c|r|r|r|r|r}
 k&I_{VW}&S_{VW}&C_{VW}&B_V+B_W&\text{right side of (1.7)}\\ \hline
29&38128&31830& 7724&1221044& 95045541\\
31&18984&13006&10658&1058616& 29621086\\
37&54560&47660& 8014&2573836&325262456
\end{array}                                                \tag{5.1}
\]

Here the last column includes `S_VW`; equivalently the collision envelope
alone is `95013711,29608080,325214796`.  The physical bundles constitute
`90.47%,96.68%,96.24%` of the full auxiliary same-side collision energy.
Meanwhile the true repeated mixed-pair energy remains only a small fraction
of the simple support.

Thus separate-side reuse loses between three and four orders of magnitude
on the exact hard rows.  The loss is not caused by mixed codegree: it comes
from group pairs which reuse many projected keys on only one side, almost
all through one physical edge, while having no corresponding reuse on the
other side.  The product

\[
 C_{VW}=\sum_{g<h}a_{gh}b_{gh}                         \tag{5.2}
\]

must be retained before summing either factor.  This is the exact
cross-role Carleson correlation.

Run

```bash
python3 phase2/loop/erdos1208/analyze_swap_optimal_nested_cores.py \
  --large-costas-only
```

to reproduce (5.1).

## 6. Geometric consequence and remaining gate

Apply the theorem with groups `(C,x,u)` in one adaptive load band and the
role-projected completion keys from
`SWAP_ROLE_PROJECTED_COMPLETION_RESERVOIR_GATE.md`.  Groups contain at most
one occurrence with a prescribed projected key, so the abstract sets above
are literal, not a relaxation with hidden multiplicity.

The theorem still gives a useful map of the populations:

* the simple support `S_VW`, handled by the coloured-rectangle switch;
* the single-key pair loads `L_V,L_W`, handled by the four-norm
  metric-cell Carleson programme; and
* the existing different-neighbour scalar collision terms; and
* the explicit two-group physical-bundle energies `B_V+B_W` in (3.10).

But the data prove that bounding these terms separately is the wrong next
task.  The correct mixed multiplicity target is the joint product (5.2), or
equivalently the sum of `binom(c(v,w),2)` before either projected-key role
is marginalized.  The five-channel mixed normal form must therefore be
used at the *pair-of-groups* level.  Section 3 explains exactly which false
`d=0` mass is introduced if the two roles are split prematurely.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_mixed_multiplicity_same_side.py
```

The verifier exhausts all group systems on two keys per side with up to
four groups, tests thousands of larger random systems, and checks every
identity and inequality above, including sharp cases of (2.5).
