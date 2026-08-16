# Multirole endpoint--pocket transfer and the double-circuit residue

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The endpoint-codegree dichotomy has an exact multirole upgrade at the
missing `n^{Theta(log log n)}` scale.  Fix a released pocket face and its
actual convex base.  Individually compatible singleton endpoints inserted
on pairwise nonadjacent boundary gaps commute.  If `k_i` endpoints are
compatible at gap `i`, one output fibre contains at least

\[
                       \left(\prod_i\max(1,k_i)\right)^{1/3}       \tag{0}
\]

ordinary faces.  In particular, if `rho q` of `q=Theta(log n)` roles each
retain `K=(log n)^D` compatible endpoints, this is at least

\[
                         K^{\rho q/3}
                    =n^{\Theta(D\log\log n)}             \tag{1}
\]

ordinary faces while retaining the pocket face and the released base.

The entropy form (0) is sharper at the live scale.  If each role matching
has `m=n^{1-o(1)}` edges, only `Theta(log log n)` roles with
`k_i=m^{Omega(1)}` already restore (1).  Conversely, if the logarithm of
the product in (0) is below `Theta((log n)log log n)`, all but
`O(log log n)` of `Theta(log n)` candidate roles have
`k_i<m^{1/2}` and hence have both endpoints incompatible on
`m-m^{1/2}` matching edges.

The complementary alternative is equally exact.  If a role has a
matching of `m` bad pairs but fewer than `K` compatible endpoints, at least
`m-K` matching edges have **both** endpoints incompatible.  Hence every
pocket face which fails the rich-role condition produces double marked
endpoint--pocket circuits in at least `(1-rho)q(m-K)` cells.

There is also a strictly stronger, role-free version.  Partition every
singleton-compatible endpoint by its unique **actual** insertion edge `g`
of the released polygon.  If `H_g` is the number (including the empty set)
of all endpoint subsets which form a rooted convex ear at `g`, then one
ordinary output fibre has size at least

\[
                            \left(\prod_g H_g\right)^{1/3}.       \tag{1a}
\]

This counts the entire rooted local face reservoir, not only singleton
choices.  Low entropy in (1a) has an exact common-edge residue: at a gap
with many endpoints, either many endpoint pairs are rooted faces or a
large dominance-nested family gives fixed-edge `1+3` circuits.  Pair data
do **not** characterize the full rooted reservoir; an exact six-point
example below has every endpoint pair compatible but its three-endpoint
union nonconvex.

This is the desired path/transfer dichotomy, with one important scope
condition.  Its gaps must be actual consecutive edges of the **released**
base `C_(c,F)=(A setminus G) union F`, and the output must recover the
context with load `Lambda`.  Old source gaps destroyed by retaining `F` or
deleting `G` cannot be used.  The six-point cage in
`ENDPOINT_POCKET_CODEGREE_DICHOTOMY.md` shows this qualification is
necessary.

Thus the positive branch is closed conditionally at the exact recovery
scale.  The live geometric residue is now narrower: most released pocket
faces must destroy the endpoint alphabet in a linear number of actual
boundary roles, yielding a weighted multirole double-circuit tensor.

## 1. Nonadjacent singleton ears commute

Let `C` be a strictly convex polygon.  A point `x` is an **ear at edge
`uv`** if `C union {x}` is strictly convex and its cyclic word replaces
the edge `uv` by `u,x,v`.

> **Lemma 1 (independent-ear insertion).**  Let `I` be a collection of
> pairwise nonadjacent boundary edges of `C`.  Choose one ear `x_i` at every
> edge `i in I`.  Then
>
> \[
>                              C\cup\{x_i:i\in I\}       \tag{2}
> \]
>
> is strictly convex in the simultaneously expanded cyclic word.

**Proof.**  Write `H_j` for the open interior halfplane of the oriented
edge `j` of `C`.  The ear region at edge `j` is

\[
                 R_j=H_j^c\cap\bigcap_{k\ne j}H_k.       \tag{3}
\]

It is the open angular cell bounded by the extensions of the two edges
adjacent to `j`.  If `x_i in R_i`, the two new supporting lines through
the endpoints of edge `i` cut only the closure of `R_i` from the old
halfplane arrangement.  Every nonadjacent ear cell `R_j` lies strictly in
both new interior halfplanes.  This follows directly by walking around the
cyclic line arrangement: the two boundary rays of `R_j` meet the old
polygon on the complementary boundary arc, whereas the new lines meet it
only at the two endpoints of edge `i`.

Consequently each new edge incident with `x_i` supports every old vertex
and every `x_j` on a nonadjacent edge.  Old edges not replaced remain
supporting because every ear violates only its own old edge inequality in
(3).  All edges of the expanded word are therefore strict supporting
edges.  QED.

Equivalently, this is the standard fact that stellar subdivisions of
pairwise nonincident edges of a convex polygon commute.  Adjacent edges
are deliberately excluded: their two ear cells can have an additional
seam turn.

If candidate gaps form a subgraph of the boundary-edge cycle, every set of
`r` available gaps has an independent subset of size at least `r/3`.
The weaker factor three handles odd cycles and arbitrary missing gaps
uniformly.

### 1.1 Full rooted reservoirs on actual gaps

For an actual boundary edge `g=uv` of `C`, let `X_g` be a set of labels
which are singleton ears at `g`.  The sets `X_g` are disjoint: a
singleton-compatible point has a unique insertion edge.  Define the rooted
ear complex

\[
 \mathcal K_g(C)=\{S\subseteq X_g:C\cup S\text{ is convex and replaces }
        uv\text{ by one boundary chain through }S\},\qquad
 H_g(C)=|\mathcal K_g(C)|.                              \tag{3a}
\]

It contains the empty set and every singleton, so

\[
                              H_g(C)\ge 1+|X_g|.         \tag{3b}
\]

> **Lemma 1a (independent rooted ears commute).**  If `I` is a set of
> pairwise nonadjacent boundary edges and `S_g in K_g(C)` for every
> `g in I`, then
>
> \[
>                              C\cup\bigcup_{g\in I}S_g                 \tag{3c}
> \]
>
> is convex in the word obtained by expanding all the selected edges.

**Proof.**  Order the points of each `S_g` along its rooted boundary chain.
They can be inserted successively: every prefix is a subset of the convex
set `C union S_g`, hence is convex, and the next point subdivides the next
descendant of the original edge `g`.  Descendants of two nonincident
original edges remain nonincident.  Lemma 1 is the local diamond saying
that two currently enabled subdivisions on such descendants commute.
Repeatedly exchanging adjacent independent insertions shows that every
linear extension of the within-chain orders is valid.  Its final polygon
is (3c).  QED.

Properly 3-color the boundary-edge cycle of `C`.  For one color `a`, choose
an arbitrary member of `K_g(C)` independently at every edge of that color.
Lemma 1a makes every union an ordinary face, and disjointness of the
`X_g` makes the map from choices to unions injective.  Choosing the richest
color proves the exact role-free bank

\[
 \boxed{\qquad
   B(C):=\max_{a\in\{0,1,2\}}\prod_{g:\,\gamma(g)=a}H_g(C)
       \ge \left(\prod_{g\in E(C)}H_g(C)\right)^{1/3}.
       \qquad}                                           \tag{3d}
\]

For varying released contexts put
`E(c,F)=sum_(g in E(C_(c,F))) log H_(c,F,g)`, choose the canonical richest
color, and define the exact output load

\[
 \Lambda_{\rm root}=\max_W\sum_{(c,F,(S_g)):\,
       W=C_{c,F}\cup\bigcup_gS_g}w_c .                   \tag{3e}
\]

The same grouping proof as Theorem 2 gives

\[
 \boxed{\qquad
       \sum_{(c,F)\in D}w_c\,2^{E(c,F)/3}
                 \le \Lambda_{\rm root}V(P).
       \qquad}                                           \tag{3f}
\]

Thus (3f) automatically merges named roles which land on the same actual
gap and uses every higher-rank rooted face available there.

### 1.2 What low rooted entropy forces, and what it does not

Write `k_g=|X_g|`, and let `a_g` be the number of unordered endpoint pairs
`{x,y}` for which `C union {x,y}` is convex.  Empty sets, singletons, and
these pairs are distinct members of `K_g(C)`, so

\[
                    H_g\ge 1+k_g+a_g,
 \qquad
 b_g:=\binom{k_g}{2}-a_g
      \ge \binom{k_g}{2}-H_g+1+k_g.                    \tag{3g}
\]

Every one of the `b_g` bad pairs is an exact fixed-edge rooted circuit.
Indeed, the two points are individually ears at `uv`; by the two-point ear
lemma in `CONVEX_BAD_PAIR_EAR_PROMOTION.md`, failure of their union is
equivalent to one endpoint lying strictly inside the triangle formed by
`u,v` and the other endpoint.

After normalizing `u=(0,0)`, `v=(1,0)` and writing an endpoint as
`p=(xi,-eta)`, put

\[
                 L(p)={\xi\over\eta},\qquad
                 R(p)={1-\xi\over\eta}.                 \tag{3h}
\]

One endpoint is hidden by the other exactly when both tangent coordinates
are ordered in the same direction.  Hence the bad-pair relation is the
comparability relation of the two-dimensional dominance poset.  If `w_g`
is its width, then every pair in an antichain is good, and therefore

\[
 \binom{w_g}{2}\le a_g\le H_g-1-k_g,
 \qquad
 w_g\le
 \left\lfloor{1+\sqrt{1+8(H_g-1-k_g)}\over2}\right\rfloor.       \tag{3i}
\]

Dilworth then supplies a dominance-nested chain, all with the same root
edge, of length at least

\[
 \left\lceil {k_g\over w_g}\right\rceil.               \tag{3j}
\]

Equations (3g)--(3j) are the rigorous common-edge cage/fan conclusion when
`H_g=o(k_g^2)`.  They deliberately make no higher-rank claim.  Pairwise
root compatibility is insufficient: take

\[
 C=\{u=(-1,0),\,b=(0,-2),\,v=(1,0)\},\qquad
 x=(-3/40,7/8),\ z=(3/40,7/8),\ y=(2/15,8/9).           \tag{3k}
\]

All three points are singleton ears at the edge `vu`, and all three pairs
are rooted ears.  Nevertheless

\[
 z={3\over244}u+{13\over61}x+{189\over244}y             \tag{3l}
\]

has positive coefficients summing to one, so `C union {x,z,y}` is
nonconvex.  Here `H_g=7`, not `8`.  This is the exact higher rooted `1+3`
residue: no invalid assertion such as `H_g>=2^(width)` is used.

### 1.3 Cup--cap sharpening of the higher rooted residue

The preceding warning does not make the higher residue structureless.
First discard a long dominance chain.  In the remaining antichain, all
endpoint pairs are rooted faces, and the ordinary cup--cap theorem applies
to the **triple** signs.

> **Lemma 1b (fixed-edge cup--cap dichotomy).**  Let `X_g` have `k`
> endpoints and let `D>=2`.  Either its dominance poset contains a chain
> of length `D`, or it contains an antichain `Y` of size
>
> \[
>                              w\ge{k\over D-1}.  \tag{3m}
> \]
>
> Order `Y` by increasing left tangent coordinate.  Let `A` be the
> largest size of a good cap (a rooted face at `g`) and `B` the largest
> size of an oppositely oriented cup.  Then
>
> \[
> w\le {A+B-2\choose A-1},\qquad
> H_g\ge2^A,\qquad
> B\ge {\log w\over\log(2A)}.               \tag{3n}
> \]

**Proof.**  If the dominance height is below `D`, Dilworth gives width
at least `k/(D-1)`; take a maximum antichain `Y`.  Normalize the
root edge as in (3h).  On `Y`, increasing `L` forces decreasing `R`, and
therefore strictly increasing ordinary horizontal coordinate.  For an
ordered triple `i<j<k`, compare `p_j` with the chord `p_i p_k`.
All old base vertices other than the root-edge endpoints retain unchanged
supporting edges, while pair compatibility fixes the tangent order of
`p_i,p_j,p_k`.  Hence the sign of `chi(p_i,p_j,p_k)` has only two
possibilities: one places `p_j` on the exposed rooted chain, and the
opposite places it inside the polygon obtained from `C union {p_i,p_k}`.
The same sign is good for every ordered triple.  Thus a subset of `Y` is
a rooted face whenever all of its triples have the good orientation.
Every subset of a good cap is again a good cap, proving `H_g>=2^A`.

The classical cup--cap recurrence now gives
`w<=binom(A+B-2,A-1)`.  If `B<=A`, the binomial coefficient is at most
`(2A)^B`, which gives the last inequality.  If `B>A` and
`A>=(log w)/2`, then `B>(log w)/2>=(log w)/log(2A)`.  If instead
`A<(log w)/2`, the crude binomial bound `w<=2^(A+B-2)` again gives
`B>(log w)/2>=(log w)/log(2A)`.  QED.

Every triple in the bad cup is a genuine rooted nonface.  Since all its
endpoint pairs are faces, a minimal planar witness uses all three
endpoints and one of the two fixed edge endpoints `u,v`.  No other old
base vertex can occur: it retains an incident supporting edge not equal
to `uv`.  Thus the bad cup is a homogeneous two-root `1+3` circuit
alphabet, even though the choice between `u` and `v` may depend on the
triple.

Taking `D=ceil(sqrt(k))` in Lemma 1b gives the useful exact corollary:
either there is a dominance-nested fixed-edge chain of length
`ceil(sqrt(k))`, or there is a triple-bad cup of length

\[
 B\ge {\log k\over 2\log(2\log H_g)}.                \tag{3o}
\]

At the live scale `log k=(1-o(1))L`, if one gap has
`log H_g>=3 sigma L log L`, (3d) already gives the
`n^(sigma log L)` one-face multiplier.  Otherwise (3o) gives a
two-root bad cup of length

\[
                         \Omega\!\left({L\over\log L}\right),       \tag{3p}
\]

unless the much larger `sqrt(k)` dominance cage occurs.  Hence actual-gap
concentration cannot remain an unspecified scalar loss: it becomes either
the required rooted face bank, a fixed-edge nested pair cage, or a
logarithmic-scale homogeneous triple-circuit fan.

## 2. Endpoint alphabets over a released pocket face

A marked context `c` carries:

* a pocket family `H_c`;
* for every `F in H_c`, an ordinary released base `C_(c,F)`;
* `q_c` named candidate gaps which are actual boundary edges of
  `C_(c,F)`; and
* at gap `i`, a matching `M_(c,i)` of `m_(c,i)` disjoint endpoint pairs.

The available gap list may depend on `(c,F)`; write `Gamma_(c,F)` for its
adjacency graph, a subgraph of a cycle.  An endpoint `v` is compatible when
it is an ear of `C_(c,F)` at its named gap.  Put

\[
 k_{c,i}(F)=\#\{v:v\text{ is a compatible endpoint of }M_{c,i}\}. \tag{4}
\]

Fix thresholds `K>=1` and `0<rho<=1`.  Call `(c,F)` **rich** if at least
`rho q_c` candidate roles obey `k_(c,i)(F)>=K`.

Choose canonically an independent set `I_(c,F)` of at least `rho q_c/3`
rich gaps.  At each selected gap retain any fixed `K` compatible endpoints
and apply Lemma 1.  This gives

\[
 \mathcal W_{c,F}=\left\{C_{c,F}\cup\{v_i:i\in I_{c,F}\}:
          v_i\text{ is one of the retained endpoints}\right\},
 \qquad
 |\mathcal W_{c,F}|\ge K^{\rho q_c/3}.                  \tag{5}
\]

Every output retains `F`, the released base, the active-role mask, and the
chosen endpoint labels.  Inside a fixed named context the decoder is
injective; an endpoint identifies its matching edge.

## 3. Weighted global transfer

Give context `c` a nonnegative weight `w_c`.  Define the actual rich-output
load

\[
 \Lambda=\max_W\sum_{(c,F,\mathbf v):
          W=C_{c,F}\cup\{v_i:i\in I_{c,F}\}}w_c.         \tag{6}
\]

> **Theorem 2 (weighted multirole transfer).**
>
> \[
> \boxed{\quad
>   \sum_c w_c\sum_{\substack{F\in H_c\\(c,F)\ \mathrm{rich}}}
>          K^{\rho q_c/3}
>       \le \Lambda V(P).\quad}                         \tag{7}
> \]

**Proof.**  Equation (5) supplies the indicated weighted generating
records.  Group them by their ordinary output; every group has total
weight at most (6).  QED.

There is a threshold-free form.  Put

\[
             S(c,F)=\sum_i\log\max(1,k_{c,i}(F)).         \tag{7a}
\]

Properly color the boundary-gap cycle with at most three colors.  One color
class has at least `S(c,F)/3` of the total logarithmic weight and is an
independent set.  Choosing all compatible endpoints in those gaps and
applying Lemma 1 gives at least `2^{S(c,F)/3}` faces.  With the analogous
actual decoder load (still denoted `Lambda`),

> **Theorem 2a (entropy transfer).**  For any selected family `D` of
> context--pocket incidences,
>
> \[
> \boxed{\quad
>       \sum_{(c,F)\in D}w_c\,2^{S(c,F)/3}
>               \le\Lambda V(P).\quad}                 \tag{7b}
> \]

The threshold theorem is the consequence
`S(c,F)>=rho q_c log K`.  More usefully, every incidence with

\[
                         S(c,F)\ge3\sigma L\log L       \tag{7c}
\]

has an attached pocket-retaining multiplier at least
`2^{sigma L log L}=n^{sigma log L}`.

For uniform `q_c>=kappa L`, a weighted rich-face mass `R` gives

\[
                 V(P)\ge {R\over\Lambda}
                     2^{(\rho\kappa D/3)L\log L}         \tag{8}
\]

when `K=L^D`.  If `R` is an independent pocket/context bank already of the
target quadratic coefficient and `Lambda=2^{o(L log L)}`, (8) restores the
full lost `Theta(L log L)` induction scale.

This last sentence is conditional on **independence of the context mass**.
If the endpoint choices are already the labels indexing `R`, (7) must be
applied to the actual incidence family rather than multiplying the same
source word twice.

## 4. Poor roles force double circuits

For a fixed role and face abbreviate `m=m_(c,i)`, `k=k_(c,i)(F)`.  For an
edge `e`, let `g(e,F) in {0,1,2}` count its compatible endpoints and let
`z(e,F)=1_(g(e,F)=0)`.  The pointwise inequality from the preceding report
gives

\[
                 \sum_{e\in M_{c,i}}z(e,F)
                    \ge m-k.                            \tag{9}
\]

> **Corollary 3 (multirole double-circuit alternative).**  If `(c,F)` is
> not rich, then more than `(1-rho)q_c` roles have `k_(c,i)(F)<K`, and
> therefore the number of pair cells with two incompatible endpoints is at
> least
>
> \[
>                 \sum_{i:\,k_i(F)<K}(m_{c,i}-K)
>       \ge (1-\rho)q_c(m-K)                            \tag{10}
> \]
>
> whenever every matching has size at least `m`.

Every cell counted in (10) has the two canonical circuits (12) of
`ENDPOINT_POCKET_CODEGREE_DICHOTOMY.md`; each meets the actual `F` and its
marked endpoint.  If `m>=2K`, (10) is at least
`(1-rho)q_cm/2`.  Summing over the weighted nonrich faces loses no
additional factor.

The same statement holds with detached compatibility `h` in place of `g`.
Then every surviving circuit is wholly inside `F union {v}` and the only
unpaid child after circuit-component factoring is one detached
circuit-connected support.

The entropy form yields an optimized poor-role count.  Suppose all
matchings have size at least `m`, fix `0<alpha<1`, and put

\[
             R_\alpha(c,F)=|\{i:k_{c,i}(F)\ge m^\alpha\}|.          \tag{10a}
\]

Then (7a) gives

\[
             R_\alpha(c,F)\le{S(c,F)\over\alpha\log m}.            \tag{10b}
\]

Every other role has at least `m-m^alpha` double-incompatible matching
edges.  Therefore the exact number of double cells is at least

\[
 \boxed{\quad
 \left(q_c-{S(c,F)\over\alpha\log m}\right)_+
                 (m-m^\alpha).\quad}                    \tag{10c}
\]

At `q_c>=kappa L`, `log m=(1-o(1))L`, `alpha=1/2`, and
`S(c,F)=O(L log L)`, (10c) is `(kappa-o(1))Lm`: essentially every
candidate gap is doubly incompatible on essentially its whole matching.
Thus the scale-recovery threshold does not require a linear number of
polylogarithmic alphabets; logarithmically many polynomial alphabets also
pay, and failure makes the circuit tensor correspondingly denser.

## 5. Exact scope in the high-root chart

The theorem needs an actual released boundary state.  Starting with a
source face `A`, deleting `G` and retaining `F` can:

* remove one or both neighbors of an old role;
* insert pocket vertices between those neighbors on the new hull; or
* make an old endpoint lie inside a pocket-rooted triangle.

Thus a bad-pair matching classified relative to `A` does not automatically
provide the gaps or the values (4) for `C_(c,F)`.  One must retain the
released mask/tangent state in `c`.  Once that state is fixed, Theorem 2 is
lossless except for the explicit global load (6).

### 5.1 Exact mask-run corollary

There is a useful purely cyclic precursor to the geometric gap list.  Let
`G` delete `t` roles from a cyclic source word of length `q`, with
`0<t<=q-3`, and let `r(G)` be the number of maximal cyclic runs of deleted
roles.  Thus at least three source roles remain, so the compressed cyclic
word still has ordinary boundary edges.

> **Lemma 4 (compressed gaps versus a long run).**  Before the pocket trace
> is inserted, deleting `G` creates exactly `r(G)` compressed boundary
> gaps between retained source labels.  Moreover
>
> \[
>                  \max\{\text{deleted run length}\}
>                         \ge\left\lceil{t\over r(G)}\right\rceil. \tag{11}
> \]

**Proof.**  Every deleted run has one retained predecessor and one retained
successor and compresses to their new boundary edge.  Distinct runs give
distinct edges, and every new nonoriginal retained--retained edge arises
this way.  The run lengths are positive integers summing to `t`, so their
maximum is at least their average.  QED.

Suppose `q>=kappa L`, `t>=tau L`, and all `r(G)` mask-created gaps survive
as actual boundary gaps after the pocket trace is retained, each carrying
at least `m^alpha` compatible endpoints, where `log m>=beta L`.  If

\[
                  r(G)\ge {3\sigma\over\alpha\beta}\log L,        \tag{12}
\]

then its endpoint entropy is at least `3 sigma L log L`, and Theorem 2a
gives the `n^{sigma log L}` pocket-retaining multiplier.  Otherwise Lemma 4
gives a deleted run of length

\[
        \Omega\left({L\over\log L}\right),              \tag{13}
\]

with the constant `tau alpha beta/(3 sigma)`.  Thus, under polynomial
endpoint availability, the mask branch is exactly

\[
 \boxed{\text{scale-recovering many-gap transfer}\qquad\text{or}\qquad
        \text{one deleted arc of length }\Omega(L/\log L).}       \tag{14}
\]

The caveat is essential: after `F` is retained, some of the `r(G)`
compressed source edges may cease to be boundary edges or may have zero
compatible endpoints.  Therefore the number of **actual** usable gaps is
at most `r(G)`, not equal to it.  If the mask has many runs but `F` destroys
most of them, the conclusion is the low endpoint-entropy/double-circuit
branch (10c), not the long-run branch.  The long run follows only when the
mask itself has `r(G)=O(log L)`; no gap destroyed by `F` is silently
reclassified as a mask run.

The exact remaining high-root task can now be stated without scalar
profiles:

> prove that a target share of released pocket faces retain polylogarithmic
> endpoint alphabets in a linear number of actual nonadjacent gaps, or
> charge the weighted tensor of `Omega(qm)` marked double circuits per
> nonrich pocket face supplied by (10).

The first branch gives precisely the scale-recovery multiplier, not merely
a factor `n`.  The second preserves the pocket trace, pair mark, role, and
released tangent context needed for a subsequent guard/shield descent.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_multirole_endpoint_pocket_transfer.py
```

The checker uses exact integer geometry to verify simultaneous singleton
ears and every rooted subset of two opposite three-label reservoirs.  It
also checks forty exact rational reverse-dominance systems, enumerating
their full rooted complexes to verify the cap/cup criterion, the
Erdos--Szekeres bound, and (3n).  Finally it exhausts every subset of cycle
gaps through length twelve, every matching compatibility vector used in
(9)--(10), and every nondegenerate cyclic deletion mask through length
fourteen, including the exact run/gap identity and longest-run bound in
Lemma 4.
