# Erdős 838: the capped guard-release telescope is automatic in the top window

**Date:** 2026-08-14.  All logarithms are base two.

## Verdict

The universal-chain and retained-outer barriers do **not** survive at the
actual capped Hall scale when

\[
                 r=\ell-O(\log\ell),\qquad
                 \ell=\lceil\log n\rceil .                 \tag{1}
\]

Indeed the cap is

\[
                         d\le 2^{\ell-r}=\ell^{O(1)}.        \tag{2}
\]

For every selected repair record, its source is already an ordinary convex
face.  Sending a record to its source has congestion at most `d`.  There is
also an exact quadratic version adapted to first divergence: send an ordered
pair of records to the ordered pair of their source faces.  Across the whole
repair tree, not separately at each node, the total charged mass over any
one output pair is at most `d^2`.  The first-divergence tag and both tangent
guards may be forgotten completely.

Thus the proposed guard-release telescope is true in this window for a
reason which uses no planar geometry.  More generally every rank window with
`ell-r=o(ell)` is automatic at the `n^{o(1)}`-congestion scale.  A genuinely
hard capped-Hall slice must have linear codimension along a subsequence,
`ell-r=Omega(ell)`.  The phrase *near-maximal face* in the low-addable
reduction must not be confused with *rank near ell*.

This does not prove Erdős 838: at a hard rank `r=(alpha+o(1))ell` with fixed
`alpha<1`, the same source projection costs
`d=n^{1-alpha+o(1)}`, which is much too large.  It does show that the
full-history universal-chain obstruction is overstrong for the capped top
window and should not be used to reject a proof targeted only at (1).

## 1. The linear capped projection

Let `F(P)` be the ordinary convex-face complex and `V(P)=|F(P)|`.  Let
`S subseteq F(P)` be any source family.  A capped selector is a finite
weighted repair family `E`, with source map

\[
                         \sigma:E\longrightarrow S,
\]

and nonnegative record weights `a_x`, such that

\[
                  \sum_{x:\sigma(x)=A}a_x\le d
                  \quad\hbox{for every }A\in S.              \tag{3}
\]

Unit weights are the usual choice of at most `d` marked repairs above each
source.  Since `sigma(x)` is itself a convex face,

\[
 \boxed{
   \sum_{x\in E}a_x\le d|S|\le dV(P).}                       \tag{4}
\]

This is simultaneously a count and a routing theorem: the map
`x mapsto sigma(x)` has weighted congestion at most `d`.

Put `g=ell-r`.  If `g<=C log ell`, the natural RNP cap satisfies
`d<=2^g<=ell^C`, and (4) gives

\[
                  d|S|\le \ell^C V(P)=n^{o(1)}V(P).          \tag{5}
\]

If one writes the demand as `n/2^r` rather than `2^(ell-r)`, it is no
larger, because `n<=2^ell`.  More generally, `g=o(ell)` gives
`d=2^g=n^{o(1)}` and the same conclusion.

In the cumulative-envelope notation this is the immediate bound

\[
 \max_{r\ge\ell-C\log\ell}
 {2^{\ell-r}N_r^{(24)}\over V(P)}\le\ell^C.                  \tag{5a}
\]

Thus no low-addable or repair theorem is needed in the top window.  Any
superpolynomial obstruction to the `K_u^(24)` envelope must occur below
`ell-C log ell` for every fixed `C`.

The per-source form (3) is the standard capped selector and is needed for a
low-congestion route.  A mere global inequality `sum a_x<=d|S|`, with all
mass allowed over one source, still proves the total count (4) but not the
claimed congestion of the source map.  Since the Hall construction chooses
the marks, imposing (3) is free.

## 2. Exact weighted first-divergence telescope

Put the selected records at the leaves of an arbitrary rooted tree.  The
tree may encode nested pockets, tangent rotations, or complete repair
transcripts.  For a node `s`, let

\[
                       e_s=\sum_{x\text{ below }s}a_x
\]

and, for an internal node, define

\[
                  w_s=e_s^2-\sum_{t\text{ child of }s}e_t^2. \tag{6}
\]

If the leaves are the individual records, direct telescoping gives

\[
 \boxed{
   \sum_{s\text{ internal}}w_s
       =e_{\rm root}^2-\sum_{x\in E}a_x^2.}                   \tag{7}
\]

Equivalently, `w_s` is the total weight `a_x a_y` of ordered distinct leaf
pairs whose first divergence is `s`.  Charge such a pair to

\[
                          (\sigma(x),\sigma(y))\in F(P)^2.   \tag{8}
\]

Every ordered leaf pair is charged exactly once.  For a fixed ordered
source pair `(A,B)`, the total charge is at most

\[
 \left(\sum_{\sigma(x)=A}a_x\right)
 \left(\sum_{\sigma(y)=B}a_y\right)\le d^2.                  \tag{9}
\]

The exclusion of the diagonal `x=y` can only decrease it.  Hence

\[
 \boxed{
   \sum_s w_s\le d^2|S|^2\le d^2V(P)^2.}                    \tag{10}
\]

At (1), `d^2=ell^{O(1)}=2^{o(r)}`.  This is the desired global
first-divergence reuse scale.  Unlike the stronger nodewise ansatz
`w_s<=K|A_s||B_s|` with separately summable families, (10) never pays the
same output pair once per state: uniqueness of first divergence performs
the telescope before congestion is measured.  No state tag has to be
absorbed into an output face.

In particular, a geometric *guard release* is unnecessary here.  The two
source outputs may retain both tangent guards: their `d^2` reuse is already
within the permitted scale.  Guard release becomes load-bearing only after
`d` itself is too large to absorb.

Notice that (10) is the square of the elementary linear bound (4).  It is
therefore the correct audit of the proposed pair telescope, but it does not
create new capacity beyond the cap already present.

## 3. Why the universal-chain obstruction disappears

Use the exact planar construction from
`../agent_stacked_outer_pocket/STACKED_OUTER_POCKET_BARRIER.md`.  It has a
fixed outer face `B`, a strict insertion chain `x_1<...<x_N`, and repairs

\[
                         B+x_i\longrightarrow B+x_j
                         \qquad(i<j).                         \tag{11}
\]

The full-history bank of length `h` has `binom(N,h)` members.  For
`h=floor(log N)`, its logarithm is

\[
                     (\log N)^2-O(\log N\log\log N).         \tag{12}
\]

But those histories are not distinct source faces or distinct selected
repair incidences.  They repeatedly reuse the same `N` states `B+x_i`.
If a complete history is assigned to its terminal state, the multiplicity
over one source can be as large as `binom(i-1,h-1)`, precisely what the
full-history pigeonhole argument exploits.

At the actual capped scale, take at most `d` successors at each state.  The
selected family then has at most `dN` records and maps back to its `N`
source faces with congestion `d`.  With

\[
                 N=2^L,\qquad h\sim L,\qquad d=L^{O(1)},
\]

the capped selector retains at most the fraction

\[
 {dN\over\binom Nh}=2^{-(1-o(1))L^2}                         \tag{13}
\]

of the full history bank.  Thus the quadratic fibres proved for the
uncapped bank say nothing about this selected family.

This audit remains at the requested rank.  Choose `|B|=r-1` with
`r=ell-O(log ell)`.  Then every state `B+x_i` is a rank-`r` convex face,
and (11) supplies `d` genuine exterior successors for all but the last `d`
states.  The capped repair mass is `Theta(dN)` and the source-face route has
exact congestion at most `d`.  Retaining or releasing the tangent chord is
irrelevant because the output is the original source.

If instead the histories are made from rank-`r` subsets of the embedded
arbitrary order type, only those subsets which are actual convex faces may
serve as source states.  Their number is at most `V(P)`, so (4) applies
again.  Projective universality cannot evade the cap.

## 4. Consequence for the remaining attack

There is no scalable planar counterexample to (4) or (10): both hold for
every abstract family of source faces.  The top-rank capped guard-release
branch is therefore closed, but only locally in rank.

The surviving geometric problem starts when

\[
                       r=(\alpha+o(1))\ell,
                       \qquad \alpha<1\text{ fixed},          \tag{14}
\]

because then `d=2^(ell-r)=n^(1-alpha+o(1))`.  Source projection has exactly
that polynomial congestion and is useless.  At (14), one genuinely needs
the forward two-ended surplus, nested-prefix Boolean capacity, or a
hierarchical guard-release theorem.  Universal-chain barriers remain
relevant only there, after they are reformulated for `d` selected incidences
per actual source rather than for all complete histories.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_capped_guard_release/verify_capped_guard_release.py
```

The checker exhausts small unit-weight capped assignments on a fixed prefix
tree, audits random integer-weighted trees, verifies the exact identity
(7), reconstructs every first-divergence charge and checks the `d^2`
source-pair bound (9).  It also checks the integer top-window inequalities
and compares `dN` with `binom(N,floor(log N))` on scalable universal-chain
parameters.
