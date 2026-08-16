# Fixed-parent seam jets: exact cross-completion after four labels

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The internal vertices of a fixed convex parent do **not** support a
quadratic-entropy left--right coupling.  Let `T` be a fixed strictly convex
parent, let every point of a nonempty petal `L` lie to the left of `T`, and
let every point of a nonempty petal `R` lie to its right.  Assume

\[
                         T\cup L,\qquad T\cup R                 \tag{1}
\]

are both convex.  Each petal is a single boundary ear replacing one parent
edge.  If the two edges are disjoint, the ears commute.  If the edges are
distinct and adjacent, compatibility is one turn at their common parent
vertex.  If the edges coincide, they necessarily equal an empty
`x`-monotone side of `T`; after normalizing this root edge, compatibility is
**exactly two seam turns** involving at most four actual petal labels.

Consequently every fixed-parent family partitions into at most

\[
                         4(1+n^2+n^4)                            \tag{2}
\]

complete left--right cross-completion cells.  At bounded parent rank this
costs only `O(log n)` bits.  A quadratic source family therefore retains its
leading entropy in one complete cell.  More strongly, all active cells may
be summed with local output load one.

This closes the proposed **parent-coupling gate**.  It does not by itself
force a coefficient gain: if `M` selected pairs occupy active cells and `C`
is the number of all ambient cross-completions in those cells, the exact
gain is `C/M`, which can be `2^{o((log n)^2)}` in the marked Reed--Solomon
regression.  That remaining loss belongs to ambient-container extraction,
not to hidden internal vertices of `T`.

The exact verifier is

```text
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_parent_seam_jet_completion.py
```

It exhausts `396` pairs of multi-vertex rooted ears and `7,754` singleton
fixed-parent pairs, checks the edge-splice and two-turn classifications
against direct convex-hull computation, checks profile constancy and the
completion-bank identity, and verifies strict rational counterexamples at
an empty side and a one-vertex side.  It also checks the exact `B<M^2`
square-loss witness for the separated face-pair bank.

## 1. Canonical petals are ears at the endpoint

Assume all point abscissae are distinct; an arbitrarily small shear achieves
this without changing the order type.  Let `a` and `b` be the leftmost and
rightmost vertices of `T`.

> **Lemma 1 (endpoint-ear localization).**  If every point of `L` lies
> strictly left of `a` and `T union L` is convex, then the points of `L`
> form one consecutive block in the cyclic boundary order.  Deleting this
> block replaces it by a parent edge `g_L`, and `g_L` is incident with `a`.
> Symmetrically, `R` replaces an edge `g_R` incident with `b`.

**Proof.**  Choose a vertical line strictly between `L` and `T`.  Its
intersection with the convex polygon `conv(T union L)` is a segment, so the
part of the polygon boundary on its left is one connected boundary arc.
It contains every vertex of `L` and no vertex of `T`.  Thus `L` is one
cyclic block.  Restricting the cyclic order to `T` gives the cyclic order of
the convex parent, so the two parent neighbours of the block are consecutive
vertices of `T` and form an edge `g_L`.

The two boundary chains from the leftmost vertex of `T union L` to its
rightmost vertex are `x`-monotone.  After either chain first enters `T`, it
cannot later encounter a parent vertex with smaller abscissa.  One of the
two remaining parent arcs contains the unique leftmost parent vertex `a`;
hence its first parent vertex is `a`.  Therefore one endpoint of `g_L` is
`a`.  The proof for `R` is the reflection in a vertical line.  QED.

Write the two parent chains from `a` to `b` as

\[
 a,u_1,\ldots,u_s,b,qquad
 a,d_1,\ldots,d_t,b.                                    \tag{3}
\]

Lemma 1 immediately gives the vulnerable-vertex classification observed in
the random audits:

* if one chain has at least two internal vertices, its first and last edges
  are disjoint, so no internal vertex of that chain can be a seam;
* if it has exactly one internal vertex `z`, its first and last edges meet
  only at `z`;
* if it has no internal vertex, its edge is `ab` and can meet an insertion
  on the other chain at `a` or `b`, or can be used by both ears.

Thus a long opposite chain does **not** protect an endpoint adjacent to an
empty chain.  Section 5 gives a strict rational example.

## 2. Distinct insertion edges

Orient the boundary of `T` counterclockwise.  If an ear `X` replaces the
oriented edge `uv`, write its inserted boundary path as

\[
                         u,x_1,\ldots,x_p,v.             \tag{4}
\]

> **Lemma 2 (distinct-edge splice).**  Suppose `g_L` and `g_R` are distinct.
>
> 1. If they are vertex-disjoint, `T union L union R` is convex.
> 2. If they meet at `z`, let `ell` and `r` be the two petal neighbours of
>    `z` in the spliced cyclic word.  Then
>    
>    \[
>       T\cup L\cup R\text{ is convex}
>       \iff \chi(\ell,z,r)\text{ has the parent boundary sign}. \tag{5}
>    \]

**Proof.**  Insert both ear paths into the cyclic parent word.  The resulting
word is simple: its two arcs between the global leftmost and rightmost
vertices are the corresponding `x`-monotone arcs inherited from (1).  If
the replaced parent edges are disjoint, every consecutive turn occurs in
one of `T`, `T union L`, or `T union R`.  All turns are strict and have the
same sign, so the simple polygon is strictly convex.

If the edges meet at `z`, all turns remain inherited except the one at `z`,
where both incident edges changed.  A simple polygon is strictly convex if
and only if all its turns have the same strict sign, proving (5).  QED.

After fixing the two actual neighbours `(ell,r)`, (5) is constant.  This is
the scalar/Ferrers tangent inequality at a one-vertex parent side.  Sorting
rays about `z` makes its compatibility matrix a Ferrers matrix.

## 3. The same edge has a four-label seam jet

Suppose `g_L=g_R=g`.  Lemma 1 forces `g={a,b}`, so one parent chain is empty.
Both ears lie in the same open halfplane outside the line of `g`.  Deleting
the other parent vertices gives the exact equivalence

\[
 T\cup L\cup R\text{ is convex}
 \iff \{a,b\}\cup L\cup R\text{ is convex}.             \tag{6}
\]

Indeed necessity is deletion.  Conversely, the rooted polygon on the right
and `T` lie in opposite halfplanes and share `g`; concatenate their non-root
boundary paths.  The endpoint turns already occur in one of the two convex
polygons in (1), so the concatenation is convex.

The rooted child in (6) is not a new unrestricted order type.  It has an
exact finite jet.

Apply an orientation-preserving affine map which keeps the `x`-order, sends

\[
                         a=(0,0),\qquad b=(1,0),          \tag{7}
\]

and puts the ears below the root line.  Their rooted boundary paths have
the forced orders

\[
 a,\ell_1,\ldots,\ell_p,b,qquad
 a,r_1,\ldots,r_q,b,                                    \tag{8}
\]

where every `ell_i` has negative abscissa and every `r_i` has abscissa
greater than one.  Put `ell_0=a` when `p=1` and put `r_2=b` when `q=1`.

> **Theorem 3 (same-edge seam-jet criterion).**  In the normalization (7),
> 
> \[
> \boxed{
> \{a,b\}\cup L\cup R\text{ is convex}
> \iff
> \chi(\ell_{p-1},\ell_p,r_1)>0
> \text{ and }
> \chi(\ell_p,r_1,r_2)>0.}                              \tag{9}
> \]
> 
> For an upper root side, reverse the boundary orientation; the same
> statement holds with the common parent sign.

**Proof.**  Vertical separation forces the cyclic order of a convex union
to be

\[
                 a,\ell_1,\ldots,\ell_p,
                   r_1,\ldots,r_q,b.                    \tag{10}
\]

Every consecutive turn in (10) occurs in one of the rooted polygons (8),
except the turns at `ell_p` and `r_1`.  These are exactly the two signs in
(9), so necessity is immediate.

For sufficiency, unwrap the directed edge angles along the non-root paths.
In each strictly convex rooted polygon they increase strictly.  Since the
`ell` vertices lie left of `a` and the `r` vertices right of `b`, the two
lists occur in the order displayed in (10): the first edge `a ell_1` has
angle in `(pi,3pi/2)`, while the last edge `r_qb`, after unwrapping, has
angle in `(5pi/2,3pi)`.  The two inequalities in (9) are precisely the two
missing strict angle comparisons at the splice.  The inherited root edge
then has unwrapped angle `3pi`.  Hence the complete cyclic edge-angle list
is strictly increasing through one turn.  The standard turning-angle
criterion says that (10) is the boundary of a strictly convex polygon.
QED.

The criterion uses only the seam jet

\[
                    (\ell_{p-1},\ell_p,r_1,r_2),         \tag{11}
\]

with root endpoints used as padding.  Internal vertices of either rooted
ear are invisible to the other side after (11) is fixed.

## 4. Exact complete-profile bank

Let `E` be any selected family of pairs `(L,R)` satisfying (1) and such that
`T union L union R` is convex.  Partition it first by the ordered gap pair
`(g_L,g_R)` and then as follows:

* no further label for disjoint gaps;
* the two neighbours in (5) for adjacent gaps;
* the four-label jet (11) for equal gaps.

There are at most four ordered gap pairs by Lemma 1, and therefore at most

\[
              S\le 4(1+n^2+n^4)                        \tag{12}
\]

joint states.  For a state `sigma`, let `A_sigma` and `B_sigma` be the left
and right projection supports of the selected pairs in that state.  Lemmas
2 and Theorem 3 imply:

> **Theorem 4 (fixed-parent cross-completion).**  For every active state
> `sigma`, every pair in `A_sigma` times `B_sigma` is convex with `T`.  The
> rectangles for different states are disjoint as labelled `(L,R)` pairs.
> Thus, writing
> 
> \[
> M=|E|,\qquad
> C=\sum_{\sigma\text{ active}}|A_\sigma||B_\sigma|,     \tag{13}
> \]
> 
> one has `C>=M`, and the ordinary faces
> 
> \[
>                 L\cup U\cup R,qquad U\subseteq T,     \tag{14}
> \]
> 
> over all active rectangles are distinct.  Therefore
> 
> \[
>                         V(P)\ge 2^{|T|}C.              \tag{15}
> \]

**Proof.**  Compatibility is constant in every state by the preceding
classification, and the state of a labelled pair is intrinsic, so the
rectangles are disjoint.  Every set in (14) is a subset of a convex
completion and is ordinary.  Its intersections with the fixed left region,
`T`, and the fixed right region recover `(L,U,R)`, proving injectivity. QED.

At a fixed canonical depth, the trace-retaining output also recovers `T` by
peeling the prescribed number of extreme pairs.  The Boolean variants in
(14) are a local bonus; no global cross-parent load claim is needed here.

If `N` is the ambient point count and

\[
 \log M=(alpha+o(1))(\log N)^2,
 \qquad
 \log(C/M)=(delta+o(1))(\log N)^2,                      \tag{16}
\]

then (15) gives coefficient at least `alpha+delta`.  Since (12) has only
`O(log N)` bits, one active complete state retains coefficient `alpha`.
There is, however, no unconditional positive `delta`: a full rectangle has
`C=M`, while the marked high-rate MDS family in
`MDS_MODULE_EXTRACTION_BARRIER.md` has
`C/M=2^{o((log N)^2)}` and no linear collection of selected modules.  Its
ambient one-gap containers pay separately.  Thus (15) is the sharp local
dichotomy: **quadratic completion surplus gains a coefficient; otherwise
the residue is already entropy-near-complete after coefficient-free seam
localization.**

## 5. Sharp short-side examples

The endpoint qualification cannot be omitted.  Let

\[
 T=\{(-3,0),(3,0),(2,3),(0,4),(-2,3)\},
 \quad L=\{(-6,-12)\},\quad R=\{(4,1)\}.                \tag{17}
\]

The upper parent chain has three internal vertices and the lower chain is
the empty edge from `(-3,0)` to `(3,0)`.  Both `T union L` and `T union R`
are strictly convex and the seven points are in general position, but
`T union L union R` hides `(3,0)`.  The two insertion edges meet at that
endpoint.  Hence “the opposite parent arc is long” does not imply automatic
cross-completion.

The one-internal-vertex inequality is already sharp on the diamond

\[
 T=\{(-2,0),(0,-2),(2,0),(0,2)\},
 \quad L_y=(-3,y),\quad R_z=(3,z).                       \tag{18}
\]

Whenever the individual insertions use the two lower edges, the only new
turn is at `(0,-2)` and

\[
       \chi(L_y,(0,-2),R_z)=3(y+z+4).                   \tag{19}

Thus compatibility is exactly `y+z>-4`, a Ferrers threshold after either
alphabet is ordered.

Finally, a same-edge rooted child genuinely needs the second seam turn.
For `a=(-1,0)`, `b=(1,0)`, take

\[
 L=\{(-6,-9),(-6,-10)\},
 \qquad R=\{(2,-9),(3,-10)\}.                           \tag{20}

Each rooted four-set is strictly convex and all six points are in general
position.  The first seam turn is positive, the second is negative, and
`(2,-9)` is hidden in the union.  This kills a one-tangent summary but is
detected exactly by (9).

## 6. What this does and does not close

For a **fixed** parent, larger-parent geometry is no longer a live source
of anti-alignment.  Long parent arcs commute; empty and one-vertex arcs are
captured by at most four actual tangent-jet labels.  Any ordered-antichain
or interval partition applied after this point must preserve the root edge
and these jet labels; intersecting unrelated interval cells can switch the
root frame and invalidates the rectangle conclusion.

The remaining global questions are different:

1. whether the completion surplus `C/M` in (13) has a quadratic exponent;
2. if not, whether ambient left/right containers yield the recoverable
   one-gap bank; and
3. how trace-retaining banks over varying parents sum without reusing the
   same face.

None of these can be charged to internal vertices of one fixed `T`.

## 7. Audit of the separated omit-one-cell bank

The local counting theorem in
`agent_outer_internal_product/DOMINANCE_CELL_SEPARATED_ONE_GAP.md` is exact,
but its two-output nature creates a decisive square loss.  In that notation,

\[
 B_g=H_g\prod_{i\ne g}m_i,qquad
 B_*:=\max_gB_g\ge
 P_0\left(\prod_i{H_i\over m_i}\right)^{1/k}.           \tag{21}
\]

Since the bank consists of **ordered pairs** of ordinary faces, it gives
only `B_*<=V(P)^2`.  Relative to `M` selected records, the exact consequence
is therefore

\[
 \boxed{
 \log{V(P)\over M}\ge {1\over2}\left[
   \log{P_0\over M}
   +{1\over k}\sum_i\log{H_i\over m_i}
   -\log M\right].}                                    \tag{22}
\]

The final `-log M` is absent when one merely computes `log(B_*/M)`, but it
is mandatory when converting a face-pair bank to a face count.  Thus a
fixed-power multiplier in `B_*/M` is not enough: a fixed-power gain over
`M` requires

\[
 \log{P_0\over M}+{1\over k}\sum_i\log{H_i\over m_i}
       \ge \log M+2\varepsilon\log D.                   \tag{23}
\]

Under the fixed-occupancy estimate in that report, with
`log M=a(log D)^2` and `k=kappa log D`, the leading sufficient condition is

\[
                         {c_ta^2\over\kappa^2}>a,        \tag{24}
\]

up to any quadratic projection-redundancy contribution.  The conservative
universal constants do not satisfy (24) in the balanced regime.

The verifier of the outer report already contains a numerical exact witness
to this loss.  Its four conic cells have

\[
 (m_i)=(2,3,2,3),\quad (H_i)=(4,8,4,8),\quad
 P_0=36,\quad M=18,\quad B_*=96.                        \tag{25}
\]

Although `B_*/M=16/3`, one has `sqrt(96)<18=M`; the separated pair bank
does not improve even the raw selected count in this finite instance.

There is a sharp sufficient hypothesis for recovering a one-face bank.
For one omitted cell `g`, suppose a reservoir subfamily
\(\mathcal H_g^\star\subseteq\mathcal F(X_g)\) has a common rooted edge and a
fixed seam jet.  Suppose also that every aggregate trace from the other
cells is the canonical opposite petal at the same fixed parent, has a fixed
compatible seam jet, and is individually convex with that parent.  Then
Theorem 3 proves that

\[
 \left\{B\cup F\cup\bigcup_{i\ne g}T_i:
   F\in\mathcal H_g^\star,\ T_i\in\mathcal A_i\right\}  \tag{26}
\]

is a one-face bank of size
\(\lvert\mathcal H_g^\star\rvert\prod_{i\ne g}m_i\), with decoder load one in the fixed
cell system.  This removes the square loss.

However, a double interval/reverse-dominance partition of the **selected
singletons** does not establish that hypothesis.  Taking an arbitrary local
face changes its actual root neighbours and seam jet.  Intersecting two
ordered cells preserves coordinate intervals, not the boundary jet of a
multi-point face.  The positive-tangent `1+3` circuit in the outer report is
an exact counterexample: both singleton traces use compatible rooted states,
while the ordinary local face `{z,y}` has an incompatible jet and cannot be
mixed with the other trace.  Tagging all jets costs only `n^4`, but it proves
only that **some** reservoir jet is large, not that a compatible jet is
large.  A valid ordered-cell closure therefore needs one of:

1. a lower bound on the compatible-jet reservoir
   \(\lvert\mathcal H_g^\star\rvert\);
2. a circuit/shield payment for the incompatible reservoir mass; or
3. retention of the second output together with the stronger threshold
   (23).

This is the exact interface between the seam theorem and the proposed
ordered omit-one-cell route.
