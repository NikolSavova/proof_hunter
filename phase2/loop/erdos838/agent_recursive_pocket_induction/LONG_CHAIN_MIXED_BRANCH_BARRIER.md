# A universal-chain obstruction to one-slot pocket induction

**Date:** 2026-08-14  
**Verdict:** projective universality can be used constructively, but in the
opposite direction from the hoped-for one-face pocket induction.  A single
fixed-edge insertion chain supports

\[
                      2^{(1-o(1))(\log n)^2}
\]

distinct monotone repair histories which have the same final hull, the same
fixed tangent edge, and the same surviving outer prefix.  On the explicit
coefficient-`1/2` upper-bound configurations, the *entire* ordinary face
complex has only

\[
                      2^{(1/2+o(1))(\log n)^2}
\]

members.  Consequently a mixed light/heavy recursion cannot freeze the
light output and ask the heavy chain history to terminate in one ordinary
face: its inverse fibre is necessarily
`2^{(1/2-o(1))(log n)^2}`.  This remains true even though every transition
stays at the same insertion edge and preserves the complete outer base.

This is a planar, stretchable obstruction to that proof architecture, not
a counterexample to Erdős 838.  It says that both final face reservoirs may
be needed to encode even *one* long-chain history.  Theorem 31's
codimension-rank collapse does not by itself control the erased past-tip
history.  Any successful mixed branch must either cross-code the heavy
history into both outputs, or prove an additional geometric restriction
which forbids the history family below.

All logarithms are base two and the empty face is counted.

## 1. Universal chain rotation histories

Fix a convex polygon `B` and a boundary edge `uv`.  In the exterior
insertion cell of `uv`, use tangent coordinates

\[
 \ell(x)={x_1-u_1\over x_2-u_2},\qquad
 r(x)={v_1-x_1\over x_2-u_2}
\]

after the affine normalization `u=(-1,0),v=(1,0)`.  As proved in
`../agent_cyclic_stem_hw/INSERTION_CHAIN_UNIVERSALITY.md`, every finite
planar order type `Q={q_1,...,q_N}` has a projectively equivalent image

\[
                         X=\{x_1<\cdots <x_N\}
\]

for which both tangent coordinates strictly decrease.  Hence

\[
 x_i\in\operatorname{int}\operatorname{conv}\{u,v,x_j\}
                         \quad(i<j).                 \tag{1}
\]

Choose one further point `p` in the same cell, with both tangent
coordinates smaller than those of `x_N`.  Thus every `x_i` is strictly
inside `conv{u,v,p}`.  All choices may be rational and generically
perturbed while preserving the strict relations.

> **Theorem 1 (all-subset same-edge history bank).**  For every positive
> integer `h<=N`, every set of indices
> \[
>                  J=\{i_1<\cdots <i_h\}\subseteq[N]
> \]
> gives a valid monotone exterior-repair history
> \[
> B+x_{i_1}\longrightarrow B+x_{i_2}\longrightarrow\cdots
> \longrightarrow B+x_{i_h}\longrightarrow B+p.             \tag{2}
> \]
> At every arrow the new point is inserted across the same edge `uv`, it
> hides precisely the preceding chain tip, and it retains every point of
> `B`.  The histories in (2) are distinct and all have the same terminal
> face `B+p`.  Therefore there are exactly `binom(N,h)` of them.

**Proof.**  The polygon `B+x_j` is convex because `x_j` lies in the open
insertion cell of the boundary edge `uv`.  If `i<j`, (1) gives

\[
 \operatorname{ext}(B\cup\{x_i,x_j\})=B\cup\{x_j\}.          \tag{3}
\]

Thus adding `x_j` to the convex source `B+x_i` is an exterior repair which
hides exactly `x_i`; no vertex of `B` is affected.  The same argument with
`p` proves the final arrow.  The chronology in (2) recovers the index set
`J`, so different `J` give different histories.  QED.

The important point is that `J` is an **arbitrary** subset.  Its tip set
`{x_i:i in J}` need not be in convex position.  The projective chain can
carry an arbitrary internal order type, so the collection of valid
rotation histories is the whole Boolean layer `binom(X,h)`, not the
rank-`h` face layer of `X`.

## 2. The one-slot lower bound

Put

\[
                         P=B\cup X\cup\{p\},
 \qquad b=|B|.
\]

Intersection with `X` sends every convex subset of `P` to a convex subset
of `X`.  Remembering also its intersection with the `b+1` extra points is
injective.  Hence the completely general bound

\[
                    \boxed{V(P)\le 2^{b+1}V(X)=2^{b+1}V(Q).} \tag{4}
\]

No compatibility between an internal face and the outer base is assumed
in (4).

> **Corollary 2 (one-face history congestion).**  Every map from the
> histories (2) to ordinary convex faces of `P` has maximum fibre at least
> \[
>                 \boxed{{\binom Nh\over 2^{b+1}V(Q)}.}       \tag{5}
> \]
> More generally, if a fixed history on the other side of a mixed branch
> supplies at most `A` possible first outputs, then every map of that
> mixed slice to ordered face pairs has fibre at least
> \[
>                         {\binom Nh\over A V(P)}.             \tag{6}
> \]

Both statements are just the pigeonhole principle, using (4) for (5).
Notice that (6) permits an arbitrary joint code between the two outputs;
only the number `A` of first-output choices available above the fixed light
history is used.

## 3. Quadratic asymptotics on the sharp upper construction

The explicit iterated directional blow-ups in `../paper/main.tex` give a
sequence `Q` with `N=|Q|`, `L=log N`, and

\[
                         \log V(Q)\le(1/2+o(1))L^2.           \tag{7}
\]

Apply Theorem 1 after the projective chain transfer, and take

\[
                         h=\lfloor L\rfloor,
 \qquad b=\lceil L\rceil.                                  \tag{8}
\]

Then the ambient set still has logarithmic size `L+o(1)`, while

\[
 \log\binom Nh
   =h\log(N/h)+O(h)
   =L^2-O(L\log L)=(1-o(1))L^2.                             \tag{9}
\]

Equations (4), (7), and (8) give

\[
                         \log V(P)\le(1/2+o(1))L^2.          \tag{10}
\]

Thus (5) is

\[
       \max\text{ fibre}\ge 2^{(1/2-o(1))L^2}.              \tag{11}
\]

The same conclusion follows from (6) whenever `log A=o(L^2)`.  In
particular, the codimension-`sqrt(L)` downface choices of a fixed light
history and every polynomial/local endpoint code have only
`2^{o(L^2)}` possibilities.  Freezing such a light output cannot leave one
face slot for the heavy history.

The construction deliberately saturates the two-face scale:
`V(P)^2=2^{(1+o(1))L^2}` is large enough in exponent to encode the
`binom(N,h)=2^{(1-o(1))L^2}` histories.  Hence it does **not** disprove a
genuinely two-output mixed decoder.  It proves that allocating one output
to each side independently is too rigid.

## 4. Consequences for the proposed Theorem 31 recursion

At every level of (2), the active base, insertion edge, and protected
prefix are fixed.  A heavy atom of Theorem 31 therefore sees no difficulty
in the current rank-`b` base.  Nevertheless it can carry the entire choice
of the previously erased tips, namely `log binom(N,h)=Theta(L^2)` bits.
Deleting `sqrt(b)` base labels or retaining the Boolean cube of `B` does
not encode those tips: the latter has only `2^b=2^{O(L)}` members.

This isolates the invalid inference:

\[
 \text{common label + common codimension prefix}
 \quad\not\Longrightarrow\quad
 \text{the attached history has residual entropy }O(\sqrt b\log n).
                                                                    \tag{12}
\]

The residual *current base* has that many label choices; the erased past
does not.  A correct recursive state must retain a face-valued encoding of
the past tips, or keep both final output slots open until that encoding is
performed.  Projective universality says that declaring the past-tip set
to be an ordinary face is exactly the original convex-subset problem.

The result also blocks the simplest attempt to reach the useful
`(3/4)(log n)^2` simple-support threshold from cumulative blocker histories.
The raw histories certainly have enough entropy, but their common terminal
hull collapses all of it.  Turning them into a simple support with ordinary
face endpoints requires a two-face encoding at the full coefficient-one
scale; it cannot be obtained by assigning the terminal hull to one endpoint
and an inductively chosen internal face to the other.

## 5. The exact large-cloud versus history-entropy law

There is a sharp quantitative version which answers the possible
"all clouds are sublinear" escape.  Let `L=log n`.  Suppose a same-edge
chain history has at most

\[
                           h=(\alpha+o(1))L
\]

distinct tips, and the union `Q_*` of every tip label which can occur in
the branch has

\[
                           |Q_*|\le n^{\beta+o(1)}.            \tag{13}
\]

The chain order forces the chronology of a chosen tip set, so the number
of histories is at most

\[
 \sum_{j\le h}\binom{|Q_*|}{j}
       \le 2^{(\alpha\beta+o(1))L^2}.                         \tag{14}
\]

This exponent is sharp: the construction of Theorem 1, restricted to any
`n^{beta+o(1)}` chain labels, has

\[
 \binom{|Q_*|}{h}=2^{(\alpha\beta-o(1))L^2}                  \tag{15}
\]

histories.  It is equally sharp with `h` disjoint consecutive level
clouds of size `|Q_*|/h`, by taking one label from each cloud.

Thus a coefficient-`1/2` ambient face slot controls the raw history entropy
from (13) only in the range

\[
                           \alpha\beta\le {1\over2}.          \tag{16}
\]

For the critical depth `alpha=1`, a history bank larger than one sharp face
complex forces only

\[
                           |Q_*|>n^{1/2+o(1)},                \tag{17}
\]

not an almost-spanning cloud.  Consequently the hypothesis
`|Q_*|<=n^{1-delta}` still permits a quadratic one-slot obstruction for
every fixed `delta<1/2`; take `beta=1-delta` in (15).  Only
`delta>=1/2` makes the elementary entropy cap (14) sufficient.

Nor does induction on `Q_*` repair the deficit.  Even granting the desired
Erdős-838 lower coefficient to the smaller configuration gives only

\[
             \log V(Q_*)\ge(1/2-o(1))\beta^2L^2.             \tag{18}
\]

Against the sharp history bank (15), the unencoded exponent is

\[
       \left(\alpha\beta-{\beta^2\over2}-o(1)\right)L^2.     \tag{19}
\]

It is positive whenever `alpha>beta/2`, including the whole critical-depth
range `alpha=1, 0<beta<=1`.  This is the precise circularity of one-pocket
induction: the internal convex-face mass has the square-in-`log |Q_*|`
coefficient, while arbitrary monotone histories have the product
`h log |Q_*|` coefficient.

If only each *individual* level cloud is bounded but their cumulative union
is not, even (14) is unavailable.  Disjoint level clouds attain the same
product exponent.  Any useful positive dichotomy must therefore control
either cumulative union size as in (13), or impose cross-level convex
compatibility which cuts the arbitrary-subset bank down to the face complex.

Equations (14)--(19) give the requested large-cloud dichotomy, but also show
its limitation: a `sqrt(n)` threshold, rather than an almost-spanning-cloud
threshold, is the most entropy alone can prove at depth `log n`.

## 6. Cross-level faces do not supply a local supersaturation

The natural positive escape is to use ordinary faces meeting two different
levels of the chain, rather than faces internal to one cloud.  The universal
construction gives a sharp negative answer to any statement which only
uses the internal pocket.

Take a coefficient-`1/2` upper-bound configuration `Q_*` on

\[
                         q=n^{\beta+o(1)}
\]

points and transfer it into one strict insertion chain.  Partition the
chain order into

\[
                         h=(\alpha+o(1))L
\]

consecutive nonempty clouds `C_1,...,C_h` of sizes differing by at most
one.  Select one tip from each cloud and insert the tips in cloud order.
Every such selection is a valid same-edge history, so its history bank has

\[
 \prod_{j=1}^h|C_j|
   =2^{(\alpha\beta-o(1))L^2}                       \tag{20}
\]

members.

Let `F_cross` be **all** ordinary convex faces of `Q_*` which meet at least
two clouds.  This definition is more generous than a pair-of-levels
reservoir: it permits a face to use arbitrarily many labels in arbitrarily
many levels.  Nevertheless

\[
 |F_{\rm cross}|\le V(Q_*)
       =2^{(\beta^2/2+o(1))L^2}.                    \tag{21}
\]

If instead one keeps a separate reservoir for every ordered or unordered
pair of levels, a face is repeated at most `h^2` times and the total is at
most

\[
                         h^2V(Q_*),                         \tag{22}
\]

which has the same quadratic exponent as (21).  In particular, the
guaranteed two-point cross-level faces contribute only
`O(q^2)` objects, whose logarithm is linear in `L`.

Thus even the union of every local cross-level reservoir leaves the
one-output deficit (19).  More strongly, allowing **both** output faces to
come from the internal pocket gives capacity at most

\[
             V(Q_*)^2=2^{(\beta^2+o(1))L^2}.         \tag{23}
\]

Comparison with (20) shows:

\[
 \begin{array}{c|c}
 \text{available local pocket outputs}&\text{necessary condition}\ \\ \hline
 \text{one arbitrary cross-level face}&\alpha\le\beta/2,\\
 \text{two arbitrary pocket faces}&\alpha\le\beta.
 \end{array}                                             \tag{24}
\]

At the critical depth `alpha=1`, every genuinely sublinear cumulative
cloud (`beta<1`) defeats even a two-face decoder confined to that pocket.
This is an exact planar countermodel to local cross-level supersaturation.
It does not rule out a global proof: the ambient filler/outer configuration
may have additional faces.  It proves that those **global** faces, or an
oriented compatibility with the retained outer component, are
load-bearing.  A recursion cannot close by invoking `V(Q_*)`, all
pair-of-level reservoirs of `Q_*`, or even `V(Q_*)^2` in isolation.

Projective universality is essential here.  The dominance chain controls
how tips replace one another over `uv`, but it imposes no lower bound on
the number of standalone cross-level convex subsets: their complete order
type is the chosen coefficient-half `Q_*`.

There is a fully nested realization in which `n` is the actual ambient
cardinality, rather than an external scale parameter.  Fix a balanced
template `S_k` from `paper/main.tex` and let

\[
                         P_d=S_k[P_{d-1}],\qquad |P_d|=r_k^d.
\]

A depth-`s` recursive microblock is a labelled copy of `P_s`.  Take
`s=floor(beta d)`.  With `L=log |P_d|`, that block has

\[
 |P_s|=|P_d|^{\beta+o(1)},\quad
 \log V(P_s)=(c_k\beta^2+o(1))L^2,\quad
 \log V(P_d)=(c_k+o(1))L^2,                         \tag{25}
\]

where

\[
                         c_k={k-2\over
                         \log\binom{2k-4}{k-2}}\downarrow{1\over2}.
\]

In the standard lexicographic realization the microblock is consecutive in
the `x`-order.  Apply the projective universality map to the **whole**
`P_d`, using that order.  The whole ambient configuration becomes one
strict insertion chain, the chosen `P_s` remains a consecutive active
subchain, and all face counts in (25) are preserved.  Add the `O(L)`-point
base and common outer tip.  Their presence multiplies the total face count
by at most `2^{O(L)}`.

Now partition the active `P_s` subchain into `h=(alpha+o(1))L` consecutive
clouds.  Equations (20)--(24) apply, while the **entire ambient face
complex**, including every possible face mixing the active levels with the
filler chain, has only

\[
                         2^{(1/2+o(1))L^2}                    \tag{26}
\]

members after the diagonal choice `k->infinity`.  Thus when
`alpha beta>1/2`, even all global cross-level faces cannot supply a
one-output terminalization of the history bank.  This is the requested
scalable planar family with sublinear active clouds and no hidden
cross-level face supersaturation above coefficient `1/2`.

The two-output ambient capacity in (26) has coefficient one and is not
contradicted.  Once again the exact surviving possibility is a genuinely
joint two-face code; a local one-face or pocket-only two-face recurrence is
ruled out.

## 7. Exact audit

Run

```bash
python3 phase2/loop/erdos838/agent_recursive_pocket_induction/verify_long_chain_mixed_barrier.py
```

The checker takes the certified 20-point hard order type with `V=4775`,
applies the exact rational projective chain map, constructs a generic base
and common outer tip, verifies every nesting/repair relation by exact hull
arithmetic, and checks all `binom(20,10)=184756` same-edge histories.  It
also checks (4) and the finite one-slot pigeonhole deficit.  The scalable
conclusion (11) is proved by (7)--(10), rather than inferred from the finite
example.
