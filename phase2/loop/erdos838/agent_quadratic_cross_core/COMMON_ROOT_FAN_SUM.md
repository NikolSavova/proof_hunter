# Common-root fans: a summed antichain bank and the exact residual

## 1. Why the ambient rooted-triangle pigeonhole is unusable

For a source of rank `r`, an exterior blocked addition can be assigned to
one of only `O(r^3)` rooted circuits inside that source.  This sourcewise
factor is harmless.  Identifying the chosen circuit as an ambient label
triple is not harmless: there are

\[
                         3\binom n3=2^{\Theta(r)}              \tag{1}
\]

possible tags at linear codimension.  Although (1) costs only `O(r)` bits
and therefore preserves quadratic entropy, it can exceed the entire target
gain `d^epsilon`.  A fixed-power EIC argument must sum over cells with
polynomial ordinary-face overlap; it cannot first choose a common ambient
triangle.

There is a canonical way to do this for the antichain half of the fixed-edge
insertion poset.

## 2. The fixed-edge insertion poset

Projectively normalize a retained edge to

\[
                  b=(-1,0),\qquad c=(1,0),\qquad a=(0,1).
\]

For an apex `x=(s,t)`, `t>0`, put

\[
             L(x)={1+s\over t},\qquad R(x)={1-s\over t}.       \tag{2}
\]

Then

\[
 a\in\operatorname{int}\operatorname{conv}\{b,c,x\}
 \quad\Longleftrightarrow\quad
 L(x)<1,\ R(x)<1.                                             \tag{3}
\]

Here `L+R=2/t>0`; either coordinate may be negative.  For two apices on
the same side of `bc`, define `x preceq y` when
`x in conv{b,c,y}`.  Direct barycentric calculation gives

\[
             x\preceq y
 \quad\Longleftrightarrow\quad
             L(x)\ge L(y)\text{ and }R(x)\ge R(y).             \tag{4}
\]

Thus this is exactly a two-dimensional dominance poset.  Moreover

\[
 \{b,c,x,y\}\text{ is convex}
 \quad\Longleftrightarrow\quad x,y\text{ are incomparable}.   \tag{5}
\]

If a `D`-point blocker neighborhood has width `w` and height `q`, Dilworth
gives `wq>=D`; hence it has either an antichain or a chain of size at least
`sqrt(D)`.  This square-root dichotomy is sharp for a square dominance
grid.

## 3. Tangent cells avoid ambient tagging

A **pure tangent record** is a tuple `(R,I,x;b,c)` with the following
properties.

* `A=R union I` is a convex source and `R union {x}` is its repaired target.
* `b,c in R` are the two tangency endpoints of `x` on `A`; `I` is the
  deleted open boundary interval and depends only on `A,b,c`.
* `bc` is an edge of `R`, all other points of `R` lie on one side of its
  line, and `x` lies on the other side.

For a fixed source, its exterior repair records split among at most
`r(r-1)` oriented tangent endpoint pairs (the orientation records which of
the two boundary intervals is hidden).  Once the oriented endpoints are
fixed, `R` and `I` are fixed.  Therefore one may keep a largest cell
sourcewise, losing only `r^2`; no ambient pigeonhole occurs.

Inside a cell `kappa=(R;b,c)`, sources are indexed by their hidden intervals
`I`.  Write `N(I)` for the selected blockers of that source, ordered by
(4).  If `x,y in N(I)` are incomparable, then

\[
                         R\cup\{x,y\}                          \tag{6}
\]

is an ordinary convex face: concatenate the retained boundary arc from
`c` to `b` with the convex two-apex arc from `b` to `c`.  Crucially, (6)
does not retain `I`.

## 4. A summed antichain theorem

Thin the kept neighborhoods so every source has exactly `D>=4` records.
Call a source **wide** if the width of `N(I)` is at least `sqrt(D)`.  For an
incomparable pair in a cell define its hidden multiplicity

\[
 \lambda_\kappa(x,y)=
   |\{I:x,y\in N(I)\}|,
 \qquad \Lambda=\max_{\kappa,x,y}\lambda_\kappa(x,y).         \tag{7}
\]

> **Theorem 1 (summed wide-fan bank).**  If `E_w` is the number of kept
> records incident with wide sources and all target ranks are at most
> `r+1`, then
> \[
>                         E_w\le 4(r+1)\Lambda V.              \tag{8}
> \]
> Here `V` is the total number of ordinary convex subsets of the ambient
> point set.  The sum in (8) runs over every tangent cell; there is no
> factor depending on `n`.

**Proof.**  Choose a maximum antichain `W(I)` in every wide row.  It
contributes

\[
            \binom{|W(I)|}{2}\ge D/4                          \tag{9}
\]

incomparable pairs.  Within one cell, (7) says that each face (6) is hit by
at most `Lambda` hidden intervals.  Across different cells, a face `F` of
size at most `r+1` has at most `|F|` representations of the form (6): the
two inserted apices are consecutive on the boundary of `F`; deleting that
adjacent pair determines `R`, and their two external neighbors determine
`b,c`.  Thus every ordinary face is hit at most `(r+1)Lambda` times.
Summing (9) gives at least `E_w/4` pair events, which proves (8).  QED.

Suppose the original selected degree is `h`, so the largest-cell thinning
has `D>=h/r^2-1`.  If a fixed fraction of sources is wide and

\[
                         \Lambda\le D^{1-\epsilon},           \tag{10}
\]

then (8), with the discarded `r^2` factor restored, gives

\[
                         |E_w^{\rm original}|
                 \le r^{O(1)}h^{1-\epsilon}V.                 \tag{11}
\]

This is exactly the desired fixed-power saving on that branch.  It is a
genuine summed-over-cells theorem: (11) never selects an ambient triangle,
edge, retained core, or blocker pair.

The same argument with the one-blocker repaired targets gives the simpler
bound

\[
                         |E|\le r^{O(1)}\Mu V,                \tag{12}
\]

where `Mu` is the maximum number of hidden intervals producing one
canonical repaired target.  Hence `Mu<=D^{1-epsilon}` closes even before
using blocker pairs.  Theorem 1 is useful precisely when single-target
reuse is large but pair reuse drops.

## 5. Exact residual: chain fans or heavy hidden multiplicity

For every thinned row, Dilworth gives one of:

1. a wide antichain, paid by Theorem 1 unless (10) fails; or
2. a nested blocker chain of length at least `sqrt(D)`.

Failure of (10) has an exact geometric meaning: one retained core `R` and
one incomparable blocker pair `x,y` are shared by more than
`D^(1-epsilon)` distinct hidden intervals `I`.  All faces `R union I` are
ordinary, and `R union {x,y}` is ordinary, but the latter is deliberately
reused by the entire hidden family.  A chain row is the ordered analogue:
the repaired targets are nested in the fixed-edge insertion poset and can
also be reused by arbitrarily many hidden intervals.  Neither alternative
is forbidden by low addable degree.

Indeed Proposition 26 of `agent_acp_proof/REPORT.md` supplies the exact
scalable barrier.  Restrict one hidden microblock to one fixed label `a_0`.
With `p` retained blocks, `q` hidden blocks and alphabet size `M`, it leaves

\[
 |\mathcal R|=M^p,\qquad |\mathcal I|=M^{q-1},\qquad |Y|=M,   \tag{13}
\]

and every `(R,I,x)` is a repair record.  All records share the fixed chord
`uv`, the fixed rooted witness

\[
                   a_0\in\operatorname{int}\operatorname{conv}\{u,v,x\},
                                                                    \tag{14}
\]

and the same outer tangent cell.  The direct target `(R,x)` has fibre
`M^(q-1)`; a two-blocker output `(R,x,y)` has the same hidden fibre whenever
it is convex.  The construction can be placed in the low-addable slice.
Its internal two-ended face complexes eventually pay, so it is not a
counterexample to fixed-power EIC.  It proves that a common root, a large
fan, and low addable degree do **not** by themselves control `Lambda`.

Consequently the open theorem is now narrower:

\[
 \boxed{\text{A heavy hidden fibre over a common blocker pair, or a common
 nested blocker chain, must release a fixed-power internal mixed-face bank.}}
                                                                    \tag{15}
\]

This must recurse into the hidden coordinates, as the fixed-outer-cell
product shows.  Any argument using only the outer rooted fan is false.

## 6. A balanced second split inside a heavy hidden fibre

Fix one of the heavy fibres from Section 5 and put the uniform law on its
hidden intervals.  Every interval `I` has the boundary order inherited from
the convex source.  Write

\[
             I=(L,J),\qquad |L|=\lfloor |I|/2\rfloor,
             \quad |J|=\lceil |I|/2\rceil,                    \tag{16}
\]

where `L` and `J` are the first and second boundary halves.  The ordered
pair `(L,J)` determines `I`.  Put `q=|I|`,
`rho=log_2|H|/q`, and fix `zeta>0`.

> **Theorem 2 (balanced entropy/rectangle split).**  At least one of the
> following holds.
>
> 1. One half has entropy density greater than `rho+zeta`; in particular
>    its ordinary-face support has that density.
> 2. The product of the two marginal laws assigns mass at least
>    `2^(-zeta q)` to compatible prefix--suffix pairs, and two independent
>    prefixes and suffixes form a complete compatible rectangle with
>    probability at least `2^(-4 zeta q)`.

**Proof.**  If neither marginal has the stated density surplus, then

\[
 I(L;J)=H(L)+H(J)-H(I)\le \zeta q.                            \tag{17}
\]

Data processing relative entropy through the support indicator gives
product support mass at least `2^{-I(L;J)}`.  Two applications of Cauchy
(the weighted `C_4` inequality) give the fourth power for rectangles.
If a marginal has entropy density above `rho+zeta`, its support cardinality
is at least its entropy exponential, and every member is a subface of an
`I`.  QED.

This theorem introduces no ambient label tag: the cut is by boundary rank,
not by a chosen ambient midpoint.  It applies equally to the nested-chain
branch, because each hidden interval is still split by its own canonical
boundary order.

The fixed-outer product explains exactly what the rectangle branch should
buy.  For `q` vertical hidden blocks of size `M`, the transversal source
bank has `M^q` members, whereas the elementary two-ended bank has

\[
                 \binom M2^2 M^{q-2}
       ={(M-1)^2\over4},M^q.                                 \tag{18}
\]

Thus it supplies an `Omega(M^2)` multiplier and immediately beats every
fixed power of a cap `D<=M`.  Formula (18) is why Proposition 26 is a test
case rather than a counterexample.

What does **not** follow from Theorem 2 is direct recursion on the larger
marginal.  A blocker which hides all of `I` need not block `L` or `J`, and
many completions can project to the same half.  The child state must retain
the completion weights and the outer tangent context.  Likewise, four
compatible concatenations in the rectangle branch need not by themselves
give a recoverable two-ended output when the two prefixes weave through
many internal tangent cells.

The exact remaining geometric atom can therefore be stated as follows.

> **Balanced hidden-fibre atom.**  A weighted dense rectangle of compatible
> hidden prefix--suffix chains either releases a forward two-ended ordinary
> face bank with polynomial global overlap, or disintegrates, with only a
> polynomial loss of record mass, into contextual child states of rank at
> most `ceil(q/2)`.

If this atom holds, the recursion depth is at most `ceil(log_2 r)`.  A loss
`r^C` at each level totals

\[
              r^{C\lceil\log_2r\rceil}
                  =2^{O((\log r)^2)}=n^{o(1)},                \tag{19}
\]

so it is compatible with the fixed-power saving.  The fixed-outer product
takes the first alternative by (18).  A one-vertex-at-a-time descent would
instead cost `r^{Theta(r)}` and is unusable; balancedness is load-bearing.

Theorem 2 proves the entropy/Cauchy half of this atom.  Recoverable
two-ended geometry, or a contextual child construction which preserves
the blocker mass, is still open.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_quadratic_cross_core/verify_common_root_fan.py
```

The verifier checks (2)--(5) on exact rational configurations, exhausts
small dominance posets and the width-height inequality, audits the summed
pair-event count on deterministic incidence systems, checks the `O(r)`
face-decomposition load, and verifies the scaling in (1) and (13).

The balanced entropy split, weighted rectangle inequality, product
two-ended multiplier, and recursion overhead are audited separately by

```bash
python3 phase2/loop/erdos838/agent_quadratic_cross_core/verify_hidden_fibre_telescope.py
```
