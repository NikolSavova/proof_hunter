# Weighted position colouring and direct release entropy

**Date:** 2026-08-15.  All logarithms and entropies are base two.

## Verdict

The complete-product hypothesis is unnecessary for the first
source--pocket cover gate.  A weighted family of rank-`O(log n)` marked
sources can be position-coloured at a cost `2^{O((log n)log log n)}`.
For the resulting arbitrary word family, adaptive circuit deletion has an
exact entropy decoder:

\[
 \boxed{\quad
 \mathbb E\sigma(A,F)\ge
       \log W+\log H-\log V(P).\quad}                 \tag{1}
\]

Here `W` is the retained source weight, `H` is the number of pocket faces,
and `sigma(A,F)` is the sum of the logarithms of the coordinate alphabet
sizes deleted from `A` in order to make its union with `F` convex.  The
deleted set may depend arbitrarily on both `A` and `F`.  No Cartesian
closure, semialgebraic extraction, output-load hypothesis, or context
description is used.

Applied to the rank-safe minimizer marking, one fixed `(root,rank)` chart
has

\[
 \log W\ge\log V(P)-O((\log n)\log\log n),             \tag{2}
\]

and therefore

\[
 \boxed{\quad
 \mathbb E\sigma(A,F)\ge
   \log H-O((\log n)\log\log n).\quad}                 \tag{3}
\]

Thus the previously conditional average-cover entrance is unconditional
on the rank-safe slice.  In particular, if the pocket induction gives
`log H=(c-o(1))(log n)^2`, the selected sources have mean adaptive circuit
cover entropy `(c-o(1))(log n)^2`.

This does **not** finish the complete-product promotion used later in the
campaign.  Equation (3) supplies a high-cost weighted circuit-cover law on
the selected words.  It does not make the circuit predicates homogeneous
on the ambient coordinate box, nor turn that law into the coalesced
label-by-label dense rectangle required by the terminal source--triangle
tag theorem.  The exact next promotion is now narrower:

> turn the high mean weighted cover cost in (3) into either a decoded
> one-face circuit/profile bank or a label-primitive dense context.

A scalable rational Reed--Solomon/double-parabola regression below shows
why selected-family Cartesian extraction cannot perform this last step.
It satisfies the actual common-root pocket hypotheses and gives every
source `Theta(log n)` disjoint singleton outer traces, but its selected
sources contain only `O(log log n)` disjoint recoverable modules.  The
example is harmless because two ambient convex chains give enormous face
banks.  Hence a valid final promotion must charge ambient geometry, not
only selected-source support.

## 1. Weighted position colouring

Fix an actual root triple `T` and a rank `r`.  Let `mathcal A` be distinct
ordinary faces of rank `r`, all containing `T`, with weights

\[
                    0<w_A\le1,\qquad W_0=\sum_Aw_A.    \tag{4}
\]

Start the cyclic order of every `A` at a fixed label of `T` and use the
same orientation.  First fix the three positions occupied by `T`.  One
position pattern retains weight at least

\[
                         W_0/{r\choose3}.               \tag{5}
\]

Colour every nonroot ambient label independently and uniformly by the
remaining `s=r-3` positions.  A source is aligned when its label in every
nonroot position receives that position colour.  Its alignment probability
is `s^{-s}`.  Hence some colouring retains a family `mathcal E` of weight

\[
 \boxed{\quad W\ge {W_0\over {r\choose3}(r-3)^{r-3}}.\quad}          \tag{6}
\]

The used colour classes `X_1,...,X_r` are pairwise disjoint; the three root
classes are singletons.  Every retained source is an ordered word with
exactly one label in every `X_i`.  The colouring can be made deterministic
by taking the first maximizing colouring, so (6) creates no hidden
description multiplicity.

The argument is valid without `T`: ordinary random `r`-colouring retains
`W_0/r^r`.  The fixed-root form (6) is useful because the deterministic
pocket `X_T` is disjoint from every used source support.

## 2. The direct entropy decoder

Let `X` be a point set disjoint from all coordinate supports and let
`mathcal H subseteq mathcal F(P|X)` be a family of `H` ordinary pocket
faces.  For every `(A,F) in mathcal E times mathcal H`, choose **any**
source deletion set

\[
                         G(A,F)\subseteq A              \tag{7}
\]

for which

\[
                         U(A,F)=(A\setminus G(A,F))\cup F             \tag{8}
\]

is ordinary.  Such a choice always exists, since `G=A` leaves `F`.  Let
`J(A,F)` be its coordinate mask and put

\[
             \sigma(A,F)=\sum_{i\in J(A,F)}\log |X_i|. \tag{9}
\]

Singleton root roles have cost zero.  One may, and below does, choose a
minimum-cost guard.  By planar Caratheodory this is exactly a minimum-cost
vertex cover of the split-circuit outer-trace hypergraph for the particular
pair `(A,F)`.

> **Theorem 1 (weighted adaptive release entropy).**  Give `A` probability
> `w_A/W`, choose `F` independently and uniformly from `mathcal H`, and
> use any deterministic choices (7).  Then (1) holds.

**Proof.**  The ordinary output `U` reveals

1. `F=U cap X`;
2. every retained source label, by intersection with the disjoint role
   supports; and
3. the deletion mask `J`, because every original word occupied every role.

Thus the only input information not determined by `U` consists of the
deleted source coordinates.  Conditional entropy gives

\[
\begin{aligned}
 H(A,F)
   &\le H(U)+H(A_J\mid U)\\
   &\le \log V(P)+\mathbb E\sum_{i\in J}\log|X_i|.
                                                               \tag{10}
\end{aligned}
\]

Every source atom has probability at most `1/W`, because `w_A<=1`.
Consequently `H(A)>=log W`, while independence gives
`H(A,F)=H(A)+log H`.  Rearranging (10) proves (1).  QED.

This is a one-face theorem.  The mask is not appended as metadata: it is
visible as the set of unoccupied role colours.  The pocket face is also
retained, so the exponential face-alphabet obstruction to projected-column
decoders does not occur.

The proof extends verbatim to nonuniform pocket weights `v_F<=1`: replace
`log H` by `log sum_F v_F`.  It also permits randomized guard selection by
including the private random seed and then fixing a seed no worse than the
mean, but no randomization is needed here.

### 2.1 Exact completion-redundancy identity

The proof contains a useful equality.  Conditional on an output `U=u`,
write

\[
 B=u\setminus X,\qquad F=u\cap X,\qquad J=J(u),         \tag{11}
\]

and let `D=A_J` be the deleted completion word.  Its ambient completion
box is

\[
                         \Omega_u=\prod_{i\in J}X_i.   \tag{12}
\]

Define the conditional support redundancy

\[
 R_u=\log|\Omega_u|-H(D\mid U=u)\ge0.                 \tag{13}
\]

Because `(U,D)` recovers `(A,F)` exactly and
`sigma=log|Omega_U|`, the entropy chain rule gives the identity

\[
 \boxed{\quad
 \mathbb E\sigma
    =H(A,F)-H(U)+\mathbb E R_U.\quad}                  \tag{14}
\]

Thus there is no third abstract overlap variable hidden in Theorem 1.

* If `E R_U` is small, almost all surviving information lies in
  product-like completion fibres with one fixed released base `B`, pocket
  face `F`, and visible mask `J`.  The redundancy-charged transcript
  theorem can be applied inside those fibres without first extracting a
  global source product.
* If `E R_U` is large, the precise residue is a high-redundancy
  common-base completion family.  It must be paid by an ambient
  support/downshadow bank while retaining `(B,F,J)`; simply counting the
  detached completion support once is not globally summable.

Identity (14) is therefore an exact low-redundancy-product versus
high-redundancy-common-base split.  Proving that the second branch is
summable, or that the first branch yields a label-primitive circuit
rectangle, is equivalent to the remaining promotion at this level.

## 3. Unconditional minimizer splice

Use the rank-safe weights `omega(A,T)` from
`MINIMIZER_WEIGHTED_LOOP_COVER_GATE.md`.  On the live cutoff
`|A|<=h=K mu=O(log n)`, their total weight is `beta V(P)` for a fixed
`beta>0`, and

\[
                         \sum_T\omega(A,T)\le1          \tag{15}

for every actual source.  There are at most `{n choose3}h` root--rank
classes.  Hence one `(T,r)` has

\[
                 W_0\ge {\beta V(P)\over {n\choose3}h}.              \tag{16}
\]

Each individual weight in that class is at most one.  Apply (6).  Since
`r=O(log n)`, equations (6) and (16) give

\[
 \log {V(P)\over W}
 \le 3\log n+\log h+\log {r\choose3}+(r-3)\log(r-3)+O(1)
 =O((\log n)\log\log n).                               \tag{17}
\]

For the deterministic rooted pocket `X_T`, take all `H=V(P|X_T)` pocket
faces.  The marked-pocket disjointness says `A cap X_T=empty` for every
source in the class, exactly the support condition of Theorem 1.  Choosing
the minimum source guard for every `(A,F)` and substituting (17) into (1)
proves (3).

No global sum over roots is required.  Fixing one root costs only the
explicit polynomial factor in (16), and the one output in Theorem 1
already retains both the pocket face and all undeleted source coordinates.

## 4. Circuit consequence and its limit

For a fixed pair `(A,F)`, let `K(A,F)` be the rank-at-most-three
hypergraph of source traces of bad split four-circuits.  Give position `i`
cost `c_i=log|X_i|`.  The minimum integral vertex-cover cost is exactly
`sigma(A,F)`.  The standard threshold rounding of the fractional cover LP
gives

\[
                 \tau^*(A,F)\ge {1\over3}\sigma(A,F),  \tag{18}
\]

where `tau^*` is the fractional matching value with vertex capacities
`c_i`.  Indeed selecting every vertex with fractional cover value at least
`1/3` covers each edge and costs at most three times the LP optimum.

Combining (3) and (18) yields quadratic mean fractional circuit mass.
Every unit of this mass has an actual bad four-set, so fixing one, two, or
three circuit quadruples costs at most `n^4,n^8,n^12`, respectively.  This
is the promised direct interface with constant-rank circuit tags.

Constantly many tags do not, however, identify the pocket face or the
remaining `Theta(log n)` circuit history.  A common fixed circuit can be
reused by a complete face-by-face tensor, and three fixed circuit
quadruples leave the same obstruction on all other roles.  Thus (18) is a
correct localization device, not by itself a source--triangle terminal
context.

## 5. Low-redundancy fibres do promote to recoverable product cells

Identity (14) has a positive product consequence.  It uses the actual
common root, which supplies a common polar origin for all sources.

> **Lemma 2 (polar local-to-global convexity).**  Let `o` lie strictly
> inside a fixed triangle `T`.  Let
> `y_1,...,y_r` contain `T`, occur in increasing cyclic polar order about
> `o`, and satisfy
> 
> \[
>                 \operatorname{orient}(y_i,y_{i+1},y_{i+2})>0         \tag{19}
> \]
> 
> for every cyclic `i`.  Then the `y_i` form a strictly convex polygon in
> that order.

**Proof.**  The three rays through `T` have every cyclic gap strictly less
than `pi`, because `o` is inside their triangle.  The same is therefore
true after inserting the other rays.  The edge `y_i y_(i+1)` lies in the
closed angular sector between its endpoint rays; sectors of nonadjacent
edges have disjoint interiors.  Hence the polar-order polygon is simple.
Every turn of this simple polygon is positive by (19), so it is strictly
convex.  QED.

The polar order comparison about a fixed rational `o` and cut ray is a
fixed-complexity semialgebraic binary relation.  Thus the bounded-degree
entropy transcript used for orientation predicates applies to it as well.

For every release output `u`, put `B,F,J,Omega_u` as in (11)--(13).
Partition its conditional completions `D` as follows.  If `u union D` is
ordinary, it is already a decoded mixed output: its intersections with the
fixed pocket and source supports recover `(F,A)`.  No product promotion is
needed for those records.  Otherwise choose its first
bad four-circuit.  Since both `B union D` and `B union F=u` are ordinary,
the circuit meets both `D` and `F`.  Its class consists of

* its at most three variable completion positions;
* its at most three actual labels in the fixed set `u`; and
* one of the constantly many signed circuit types.

If global face rank is at most `R_max`, the number of classes per `u` is

\[
                         Q\le C r^3 R_{\max}^3.          \tag{20}
\]

For one **bad** class, impose the following `O(r)` bounded-degree predicates on
the completion coordinates:

1. adjacent polar-order comparisons in the full source word;
2. all cyclic consecutive turns (19); and
3. the constant number of signs of the fixed bad circuit.

Every selected completion satisfies them.  The redundancy-charged
semialgebraic transcript therefore retains a coordinate product on which
every ambient completion is an ordinary source by Lemma 2 and every
source--`F` union has the same fixed bad circuit (or belongs to the already
good class).

Let `C` denote the circuit class.  Although conditioning can increase
redundancy, its mean increase is bounded exactly:

\[
\begin{aligned}
 \mathbb E_{U,C}\bigl[\log|\Omega_U|-H(D\mid U,C)\bigr]
   &=\mathbb E R_U+I(D;C\mid U)\\
   &\le\mathbb E R_U+\log Q.                            \tag{21}
\end{aligned}
\]

The actual coordinate supports inside a class only reduce the left-hand
redundancy.  Apply the transcript in every nonempty `(u,C)` class and sum
the retained probabilities.  Convexity of `2^{-x}` and (21) give:

> **Theorem 3 (recoverable low-redundancy promotion).**  There is an
> absolute constant `A` such that the release law contains a combination
> of decoded good mixed records and selected bad records in complete
> product completion cells, of total effective probability at least
> 
> \[
>       2^{-A(r+\mathbb E R_U+\log Q)}                 \tag{22}
> \]
> 
> inside complete product completion cells.  Every cell retains the
> actual ordinary output `u=B union F`, the root `T`, and the visible mask
> `J`; every ambient transversal is an ordinary source; and every bad cell
> has one homogeneous actual four-circuit meeting `F` and the variable
> completion.

The cell's base context is not artificial metadata: it is the ordinary
face `u` which generated the fibre.  At most `Q` chosen circuit classes
are used per `u`.  Thus across varying bases the only extra class load in
this promotion is the polynomial factor (20), not the number of possible
pocket faces.

For `r=O(log n)` and `R_max=O((log n)^2)`, if
`E R_U=o((log n)^2)`, (22) preserves the full quadratic coefficient.  At
the sharper quasipolynomial scale it records the honest loss
`2^{O(r+E R_U)}`.  The high-`E R_U` branch remains the common-base
support/downshadow gate stated after (14).

## 6. Scalable marked MDS/double-parabola regression

The selected-source product conclusion is false even with the precise
marked-pocket geometry.  Let `p` be prime, `q<p`, and let `I_1,...,I_q`
be consecutive blocks of `p` integer indices.  Put `N=pq`, enlarge the
index interval by one point at each end, and set

\[
 z_i=(i,i^2-M^2),\qquad
 x_i=(i,10M^2+\tfrac1{10}i^2),                         \tag{23}
\]

where `M` is larger than every used absolute index.  Choose a large
triangle `T={l,r,t}` whose lower edge lies just below the `x`-chain, whose
top lies far above it, and whose interior contains every `x_i`.  The lower
`z`-chain lies outside that edge.  The parameters may be chosen rationally
and generically so that

* `T union {z_i}` is in convex position;
* the whole `x`-chain is in convex position;
* every `x_i` is inside `T`; and
* for every nonendpoint index,

\[
                  x_i\in\operatorname{int}
                       \operatorname{conv}\{z_i,x_{i-1},x_{i+1}\}.   \tag{24}
\]

The last assertion is the exact midpoint computation from the rational
double-parabola construction.

Take the length-`q`, dimension-`k=q-c` Reed--Solomon code over `F_p` and
map its `j`th symbol to one `z`-label in block `I_j`.  For every codeword
`a`,

\[
                  A_a=T\cup\{z_{j,a_j}:1\le j\le q\}  \tag{25}
\]

is an ordinary rank-`q+3` marked source.  The deterministic rooted pocket
of `T` contains the entire `x`-chain, since every `T union {x_i}` has
`x_i` interior while every `T union {z_i}` is convex.  Equation (24)
gives the `q` pairwise disjoint singleton source traces

\[
                         \{z_{j,a_j}\}.                 \tag{26}
\]

Thus every source has transversal number at least `q` (in fact at least
`q+1`, counting the common root circuit).

The selected family has size `p^{q-c}` and minimum Hamming distance
`c+1`.  Any disjoint recoverable Cartesian module changes a nonzero
codeword on at least `c+1` coordinates, so the number of disjoint variable
modules is at most

\[
                         \left\lfloor{q\over c+1}\right\rfloor.      \tag{27}

With `q=Theta(log n)` and `c=Theta(q/log log n)`, (27) is only
`O(log log n)` although the source entropy is `Theta((log n)^2)`.

This is an exact regression to any promotion theorem using only the
selected marked sources and their disjoint traces.  It is not a low-face
counterexample: both parabolic chains are convex, and the ambient source
transversal box has `p^q` ordinary faces.  Those are exactly the geometric
banks which a correct low-`V` promotion must charge.

## 7. What is now proved and what remains

The implication

\[
 \text{rank-safe marked mass + pocket reservoir}
 \Longrightarrow
 \text{quadratic mean adaptive cover entropy}           \tag{28}
\]

is unconditional by (3).  It replaces the complete-product and aggregate
released-output-load assumptions in the **average-cover entrance**.

The implication

\[
 \text{quadratic mean cover entropy}
 \Longrightarrow
 \text{coalesced label-primitive dense rectangle or decoded bank}     \tag{29}
\]

remains open only in the high-average-`R_U` common-base branch.  Role
colouring provides honest coordinates, (18) provides actual constant-rank
circuit tags, Theorem 3 handles low redundancy, and the output in Theorem
1 keeps the full pocket face.  What is missing is a summable
support/downshadow/profile theorem for the high-redundancy completion
fibres which retains their actual `(B,F,J)` base.  The MDS regression
proves that selected-word module extraction is not such a theorem.

`HIGH_REDUNDANCY_RELEASE_HALL_BARRIER.md` continues exactly this last
branch.  It proves the support-reservoir Cauchy theorem with its honest
global overlap and gives a scalable common-guard MDS tensor in which that
overlap equals the full released-face alphabet.  Consequently the final
missing input is planar cross-profile composition, not another entropy or
two-target Hall inequality.

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_weighted_position_release_entropy.py
```

The checker exhausts weighted position colourings and adaptive deletion
maps on small word systems, numerically audits the entropy inequality, and
then verifies an exact rational `q=3,p=5` marked Reed--Solomon instance:
general position, both convex chains, the common root pocket, every
double-parabola singleton trace, all codeword sources, the cover lower
bound, and the MDS distance certificate.
