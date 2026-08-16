# Erdős 838: the retained-outer/pocket coexistence barrier

**Date:** 2026-08-14.  All logarithms are base two.

## Verdict

The natural stacked completed-reservoir theorem is false even with the full
ACP correlation.  Put an arbitrary planar order type into one strict
fixed-edge insertion chain, and keep the same outer convex prefix at every
repair.  Then every transition has

\[
                 A=(T-p)\cup I,
\]

with `p` an outward successor, a common retained outer face, and a common
tangent chord.  Nevertheless an ordinary convex face which retains that
tangent chord can contain **at most one** chain label.  Hence reservoir
codewords from different nested levels do not coexist with the retained
outer component.

This gives an exact trichotomy for a two-output decoder of a length
`Theta(log N)` chain history.

1. If both output faces retain the outer tangent chord, the inverse fibre is
   `2^((1-o(1))(log N)^2)`.
2. Even if only one of the two outputs must retain the chord and the other
   is an arbitrary ordinary face, the sharp coefficient-`1/2` construction
   forces fibre `2^((1/2-o(1))(log N)^2)`.
3. Splitting the chord between the outputs--one retains `u`, the other
   retains `v`--still forces fibre `2^((1/2-o(1))(log N)^2)` on the same
   sharp sequence.  The two output reservoirs collapse to the cup and cap
   families of the internal order type, whose product has only the ordinary
   face exponent.
4. If "retain the outer component" means only that the fixed outer prefix
   can be decoded, rather than that it coexists in an output face, the
   condition is vacuous.  The resulting unrestricted two-face statement is
   exactly the already-banked Erdős-838-equivalent universal-chain decoder.

Thus literal outer/pocket coexistence cannot close the component-surplus
branch.  A successful recursion must sometimes release at least one of the
two tangent guards in **both** outputs, and then recover the outer state by a
different amortized code.  Merely carrying the retained outer face consumes
one of the two face slots and recreates the quadratic one-slot obstruction.

## 1. An arbitrary order type behind a fixed retained chord

Let `Q={q_1,...,q_N}` be any planar point set in general position.  The
projective insertion-chain universality theorem gives an order-type
equivalent image

\[
                        X=\{x_1,\ldots,x_N\}
\]

above the chord

\[
                         u=(-1,0),\qquad v=(1,0)
\]

such that

\[
 x_i\in\operatorname{int}\operatorname{conv}\{u,v,x_j\}
                         \qquad(i<j).                 \tag{1}
\]

Choose a convex polygon `B` below `uv`, of size `b`, having `uv` as an
edge.  All choices may be made rational and in general position.  Choose a
further upper point `p` after `x_N`, so every `x_i` lies strictly inside
`conv{u,v,p}`.  Put

\[
                         P=B\cup X\cup\{p\}.         \tag{2}
\]

For `i<j`, both `B+x_i` and `B+x_j` are ordinary convex faces, while (1)
gives

\[
 \operatorname{ext}(B\cup\{x_i,x_j\})=B\cup\{x_j\}.\tag{3}
\]

Consequently the arrow `B+x_i -> B+x_j` is an exterior repair record with

\[
 R=B,\qquad I=\{x_i\},\qquad p=x_j,
 \qquad A=R\cup I=(T-p)\cup I.                      \tag{4}
\]

The final arrow to `B+p` has the same form.  Thus the construction has all
the geometric information certified by ACP Theorem 20: the complete outer
prefix is retained, the insertion edge is fixed, and the new label is an
outward successor.

For every `h`-subset `J={i_1<...<i_h}` of `[N]`, (3) gives the history

\[
 B+x_{i_1}\longrightarrow\cdots\longrightarrow B+x_{i_h}
                    \longrightarrow B+p.           \tag{5}
\]

Hence the history bank `H_h` has

\[
                            |H_h|={N\choose h}.       \tag{6}
\]

## 2. The guard-exclusion lemma

Let

\[
 \mathcal F_{uv}=\{F\subseteq P:F\text{ is convex and }u,v\in F\}.
\]

> **Lemma 1 (retained guards exclude stacked tips).**  Every member of
> `mathcal F_uv` contains at most one point of `X union {p}`.  Consequently
> \[
>            |\mathcal F_{uv}|\le 2^{b-2}(N+2).      \tag{7}
> \]
> If the complete outer face `B`, rather than only `u,v`, must be retained,
> the bound improves to `N+2`.

**Proof.**  Take two upper-chain points, ordered as `z_i<z_j`, where `p` is
after every point of `X`.  By (1) and the choice of `p`, `z_i` lies strictly
inside `conv{u,v,z_j}`.  Any set containing `u,v,z_i,z_j` is therefore not
in convex position.  This proves the first assertion.  Once the subset of
`B-{u,v}` and the zero-or-one upper point are specified, the face is
specified, which proves (7).  If all of `B` is required, only the upper
choice remains.  QED.

There is a second exact form of the exclusion which covers the natural
attempt to split the two guards between the outputs.  In the chain order,
call a nonempty subset of `X` a **cup** if all of its increasing triples
have positive orientation and a **cap** if they all have negative
orientation.  Write `U(Q),C(Q)` for their respective totals; projective
universality preserves these totals, up to interchanging the two signs.

> **Lemma 2 (one guard exposes only one hull chain).**  The ordinary faces
> of `X union {u}` which contain `u` are in bijection with the cups of `X`,
> together with the singleton `{u}`.  The analogous faces containing `v`
> are in bijection with the caps, together with `{v}`.  Consequently, in
> the full set `P`,
> \[
>  |\{F\in\mathcal F(P):u\in F\}|\le2^b(U(Q)+1),
>  \qquad
>  |\{F\in\mathcal F(P):v\in F\}|\le2^b(C(Q)+1).    \tag{7a}
> \]

**Proof.**  For `i<j`, the tangent-coordinate formula gives

\[
 \chi(u,x_i,x_j)>0,\qquad \chi(v,x_i,x_j)<0.         \tag{7b}
\]

Thus the radial order of the `x_i` around `u` is the chain order.  The
sequence `u,x_(i_1),...,x_(i_s)` is the boundary of a convex polygon exactly
when every triple of the `x_(i_j)` has positive sign, which is exactly the
cup condition.  Reversing the radial order at `v` gives the cap condition.
This proves the bijections.  In `P`, delete the optional terminal point `p`
and the other `b-1` base points.  Deletion preserves convex position, and
the deleted-set indicators make this an injection into at most `2^b`
copies of the corresponding rooted family.  This proves (7a).  QED.

Lemma 1 is the exact failure of the stacked-compatibility hypothesis in the
global symmetric reservoir code.  Local completed reservoirs exist at
every transition, but a codeword chosen at one level is hidden by every
later codeword as long as the outer tangent chord survives.

There is also the general ambient-face upper bound

\[
                         V(P)\le 2^{b+1}V(Q).        \tag{8}
\]

Indeed intersection with `X` maps an ordinary convex face of `P` to a
convex face of `X`, and its intersection with the `b+1` extra points
`B union {p}` supplies the remaining bits.  The map is injective.

## 3. Exact two-output congestion

> **Theorem 2 (retained-outer two-output barrier).**  For every map
> `Phi:H_h -> F(P)^2`:
>
> * if both coordinates of every output lie in `mathcal F_uv`, then
>   \[
>    \max |\Phi^{-1}(F_1,F_2)|
>       \ge {\binom Nh\over 2^{2b-4}(N+2)^2};        \tag{9}
>   \]
> * if at least one coordinate of every output lies in `mathcal F_uv`, then
>   \[
>    \max |\Phi^{-1}(F_1,F_2)|
>       \ge {\binom Nh\over
>       2^{2b}(N+2)V(Q)}.                            \tag{10}
>   \]
>   (The harmless factor two for the choice of guarded coordinate is
>   included.)

**Proof.**  In the first case the range has size at most
`|mathcal F_uv|^2`; combine (6) and (7).  In the second case its size is at
most `2|mathcal F_uv|V(P)`; combine (7)--(8).  Pigeonhole gives (9)--(10).
QED.

Take `h=floor(log N)`, `b=O(log N)`, and choose `Q` from the explicit
directional-blow-up sequence for which, writing `L=log N`,

\[
                 \log V(Q)\le(1/2+o(1))L^2.         \tag{11}
\]

Stirling's formula gives

\[
                 \log {N\choose h}=L^2-O(L\log L). \tag{12}
\]

The logarithms of the lower bounds (9) and (10) are therefore respectively

\[
                (1-o(1))L^2,
        \qquad (1/2-o(1))L^2.                       \tag{13}
\]

In particular, no `2^{o(L^2)}` decoder exists under either natural
containment meaning of retained-outer coupling.

The split-guard alternative is no better.  If the first output contains
`u` and the second contains `v`, Lemma 2 bounds the range by

\[
                      2^{2b}(C(Q)+1)(U(Q)+1).        \tag{13a}
\]

For the explicit iterated directional blow-ups, the exact cap/cup
recurrences give

\[
             \log(C(Q)+1)+\log(U(Q)+1)
                       =(1/2+o(1))L^2               \tag{13b}
\]

along the balanced diagonal sequence.  Hence every map of `H_h` to a
split-guard output pair has fibre at least

\[
                        2^{(1/2-o(1))L^2}.           \tag{13c}
\]

Allowing the two guard assignments to swap adds only a factor two.  Thus
even collectively preserving the root chord, with neither individual face
containing both endpoints, still spends half of the required quadratic
history capacity.  The reason is exact: a one-guard completion is a
one-sided cap/cup reservoir, while an arbitrary convex face needs both hull
chains.

The obstruction is not an artefact of fixing `B`.  Let `mathcal R` be any
family of labelled outer cores which all contain `u,v`, and suppose every
`R+z`, `R in mathcal R` and `z in X union {p}`, is convex.  Give every core
the complete history bank (5).  Consider the literal completed-reservoir
interface in which an output attached to `R` has the form

\[
                         F=R\cup E,
             \qquad E\subseteq X\cup\{p\},          \tag{13d}
\]

and canonically recovers `R`.  Lemma 1 forces `|E|<=1`.  Therefore a map of
`mathcal R times H_h` to two such outputs has fibre at least

\[
                         {\binom Nh\over(N+2)^2},    \tag{13e}
\]

because the factor `|mathcal R|` cancels from demand and range.  For an
ordered pair of histories with independently chosen cores, with output `i`
retaining and recovering core `R_i`, the lower bound is

\[
                         {\binom Nh^2\over(N+2)^2}.  \tag{13f}
\]

Thus even a quadratic-entropy outer-core family cannot pay the pocket word
while it is literally retained in the two completed outputs.  Its entropy
only identifies which core is present; it is not a fresh codebook for the
erased tips.  To use outer entropy for those tips, a decoder must encode in
proper downfaces or alternative outer faces, i.e. it must cease to retain
the complete core in the sense of (13d).

The same count is even more severe if one proposes an unweighted map of an
**ordered pair** of complete histories to two faces.  Without any guard
condition at all, (8) gives fibre at least

\[
                  {\binom Nh^2\over V(P)^2}
                         =2^{(1-o(1))L^2}.           \tag{14}
\]

Thus a pair-valued component recursion cannot simply declare every full
history word to be a record.  It must use the first-divergence/Kraft weights
or otherwise pay histories before forming the square.  This distinction is
independent of the outer-prefix issue.

## 4. What survives

If neither output is required to contain `u,v`, its capacity is `V(P)^2`.
For a **single** history the exponent of this pool matches (12) on the sharp
construction.  A subquadratic-fibre theorem in that unrestricted form is
therefore equivalent, by projective universality, to the desired
coefficient-`1/2` lower bound for the arbitrary internal order type `Q`.

Accordingly the retained outer component does not provide a middle route:

* preserving it geometrically kills cross-level coexistence by Lemma 1;
* merely decoding a fixed copy of it adds no information and leaves the
  original universal-chain problem.

Any genuinely narrower positive theorem must use an operation not present
in the proposed stacked completed-reservoir statement: for example, split
or erase the tangent guards in both outputs, prove that the lost outer
prefix is charged at a previous first divergence, and use the released
unguarded pocket faces jointly.  The ACP correlation (4), even in its
strongest fixed-prefix form, does not itself supply that operation.

The exact surviving target is therefore a **guard-release first-divergence
telescope**, not a stacked-retention theorem.  If `e_s` is the number (or
the collision weight) of histories below a repair-tree state `s`, put

\[
                 w_s=e_s^2-\sum_{t\text{ child of }s}e_t^2. \tag{15}
\]

One must construct ordinary face families `mathcal A_s,mathcal B_s` such
that, with `K,L_A,L_B=2^{o(L^2)}`,

\[
 w_s\le K|\mathcal A_s||\mathcal B_s|,
 \qquad
 \sum_s|\mathcal A_s|\le L_AV(P),
 \qquad
 \sum_s|\mathcal B_s|\le L_BV(P).                  \tag{16}
\]

At a universal long-chain state, both output families in (16) must be free
to drop the tangent guards and use two-sided pocket faces; the erased outer
state must instead be recoverable from the first-divergence cell or already
charged at an ancestor.  Lemma 1 rules out keeping both guards, Lemma 2
rules out merely distributing one guard to each output, and unrestricted
two-sided pocket coding is 838-equivalent unless the ancestor charge is
load-bearing.  By the recoverable-cell Cauchy telescope, (16) would give the
needed global pair bound.  This is the narrow statement left alive by the
barrier.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_stacked_outer_pocket/verify_stacked_outer_pocket.py
```

The checker uses the saved rational 20-point order type with `V(Q)=4775`,
applies the exact projective insertion-chain transform, adjoins a generic
outer base and terminal tip, and verifies every nesting, repair, and ACP
projection identity by rational hull arithmetic.  It also audits (7)--(10)
and gives finite pigeonhole witnesses: a length-10 history mapped to two
guard-retaining outputs has fibre at least 96, while an ordered pair of
length-10 histories mapped to two arbitrary ambient faces has fibre at
least 6.  It verifies the exact one-guard identities
`|F_u|=1+U(Q)=1628` and `|F_v|=1+C(Q)=1605` before adjoining the base and
terminal point.  The symbolic variable-core cancellation in (13e)--(13f) is
checked with an arbitrary 123,457-core test family.
