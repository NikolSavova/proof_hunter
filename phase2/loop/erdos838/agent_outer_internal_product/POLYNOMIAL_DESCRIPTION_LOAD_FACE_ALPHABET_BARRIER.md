# Polynomial description load holds for label-primitive records, but fails for released-face alphabets

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

There is an exact polynomial description theorem on the rank-safe slice,
but only after the terminal records are genuinely **label primitive**.
Fix an actual source `A` of rank `r=O(log n)`.  Every state currently used
by the canonical radial/endpoint branch which consists of

* a fixed number of subsets or ordered traces of `A`;
* a fixed number of external point labels;
* root, side, gap, circuit-sign, and dyadic flags; and
* canonical radial depth/carrier data

has at most

\[
                     L_{lab}\le C(r+1)^c2^{cr}n^s=n^{O(1)}       \tag{1}
\]

values over one actual source.  Here `c,s,C` are absolute constants fixed
by the branch.  The radial depth and carrier are in fact decoded by the
source and endpoint pair and need no separate factor.  After fixing one
such state and one dyadic layer, all distinct release labels can be pooled
into a single simple one-row star.  The exact dyadic argument then gives

\[
                               \kappa_A<2L_{lab}.        \tag{2}
\]

This proves the polynomial-load prerequisite for any supplied terminal
family whose records are sets of actual `(source,label)` edges and whose
remaining marks have the bounded form above.  Splitting the same geometric
edge into several named histories is metadata and must be canonicalized or
charged to (1); it cannot contribute genuine demand.

The hypothesis is not automatic from rank-safe marking.  There is a
scalable rational regression with

* one rank-three canonical source and root;
* one deterministic `m`-point rooted pocket;
* one fixed guard and one fixed column label `x`; and
* `2^(m-1)` distinct actual released pocket faces `F` containing `x`.

All records have the same source, root, guard, circuit class, and column.
They are not duplicated chronology: the set `F` is a different actual
ordinary face in every record.  Erasing `F` and pooling to the edge `(A,x)`
loses a factor `2^(m-1)`; retaining `F` makes the description alphabet
exponential.  Thus no unconditional `n^O(1)` description bound follows
from source rank, canonical roots, or endpoint/depth decoding alone.

The regression is paid by its released-face bank—there really are
`2^(m-1)` distinct ordinary outputs.  It is therefore not a hard minimizer
counterfamily.  It identifies the exact missing upstream dichotomy:

> either the dense promotion produces label-primitive records, so (1)--(2)
> close the source load, or a variable released-face/support word remains
> in the record and must be charged by an actual bounded-overlap face bank
> before applying the source--triangle tag theorem.

Consequently, the polynomial-description prerequisite in
`END_TO_END_QUASIPOLY_GATE_AUDIT.md` is proved for the label-primitive
terminal branch but remains open for the full pocket-face/product
promotion.

There is one important relaxation.  Polynomial load is stronger than the
finite-gap argument needs.  Every subset, partition, matching, and ordering
description supported **entirely on** a rank-`O(log n)` source costs only
`2^{O((log n)loglog n)}`.  The rich-role threshold `K=(log n)^D` has an
arbitrarily large fixed `D`, so it can absorb any fixed coefficient in
this source-internal description cost.  This does not absorb a linear
number of freely chosen ambient labels or the face alphabet in (12), whose
cost is quadratic-exponential rather than quasipolynomial.

## 1. Canonical state tuple on a rank-safe source

Let `A` be an actual ordinary source of rank `r`.  The following tuple is
large enough to dominate the geometric states in the canonical
root/guard/endpoint descent:

\[
 \Theta=(\mathbf S,\mathbf z,\varepsilon).              \tag{3}
\]

Here

* `mathbf S=(S_1,...,S_c)` is a fixed-length list of subsets, ordered
  traces, or masks in `A` (root trace, retained base/deleted guard,
  blocker cover, and source-side circuit trace);
* `mathbf z=(z_1,...,z_s)` is a fixed-length list of external labels
  (blocked mark, endpoint pair, a bounded circuit witness, and any fixed
  opposite-side anchor); and
* `epsilon` is one of `C(r+1)^c` branch flags, order positions, signed
  circuit roles, sides, colors, and gap indices.

This deliberately overcounts.  A root is a triple in `A`, not an arbitrary
subset; a source circuit trace has rank at most three; and the endpoint
pair uses only two external labels.  Nevertheless the crude bound

\[
 |\{\Theta\text{ over fixed }A\}|
       \le C(r+1)^c(2^r)^c n^s                          \tag{4}
\]

is enough.  On the rank-safe slice `r<=Kmu=O(log n)`, (4) is polynomial.

Several apparent history fields do not enlarge (3).

1. The deterministic pocket `X_T` is a function of the canonical root
   `T`.
2. For canonical symmetric radial peeling, `(A,e)` determines the depth
   and retained carrier.
3. The minimum guard/cover and first bad circuit are deterministic after
   their input labels and the global tie order are fixed.
4. An active support set is not a description of a one-row terminal
   context.  After fixing `Theta` and a weight layer, take the union of all
   its distinct actual column labels.  Every edge from `A` to one of those
   labels is retained in the resulting simple star.  Arbitrary triples of
   distinct planar labels are ordinary, so the source--triangle tag theorem
   needs no common support geometry at this stage.

Item 4 is why exponentially many differently named support containers are
metadata when they induce the same set of actual source--label edges.

## 2. Exact weighted pooling theorem

Let `u` range over canonical marked occurrences above one actual source
`A`, with weights `alpha_u` satisfying

\[
                              \sum_u\alpha_u\le1.       \tag{5}
\]

Every descendant label record has weight `beta<=alpha_u`, a state
`Theta`, and one actual column label `x`.  Bucket it by

\[
             2^{-k-1}\alpha_u<\beta\le2^{-k}\alpha_u.  \tag{6}
\]

Assume the records are globally simple after `(u,Theta,k)` is fixed: each
actual column `x` occurs at most once.  Pool all of their columns into one
row star and round its common edge weight up to `2^{-k}alpha_u`.

> **Theorem 1 (rank-safe label-state compression).**  If each occurrence
> uses at most `L` states, then the actual source-target load of the pooled
> contexts is less than `2L`.  In particular, (4) gives (2).

**Proof.**  For fixed `(u,Theta)`, the source is entered once in every
nonempty layer and hence receives load at most

\[
                       \sum_{k\ge0}2^{-k}\alpha_u<2\alpha_u.     \tag{7}
\]

Sum over at most `L` states and then over `u`; (5) gives the claim.  Edge
demand is preserved up to the factor-two upward rounding because every
distinct column remains an edge of the pooled star.  QED.

This theorem also pinpoints the duplicate rule.  Several literal copies of
the same `(u,Theta,x)` cannot be distinct edges in a simple star.  If they
carry no further actual mark, they are duplicate metadata and must be
counted once.  If they carry a further actual label, it belongs in
`mathbf z` and costs at most a polynomial factor.  If they carry an actual
set of unbounded rank, Theorem 1 does not apply; that is the face-alphabet
case below.

## 3. Exact released-face regression

For `m>=4`, take the rational source triangle

\[
             A=T=\{(-3,0),(3,0),(0,4)\}.               \tag{8}
\]

For `1<=j<=m`, put `t_j=j` and

\[
 x_j=\left({1-t_j^2\over4(1+t_j^2)},
            1+{t_j\over2(1+t_j^2)}\right).             \tag{9}
\]

The points `X={x_1,...,x_m}` lie on the circle with center `(0,1)` and
radius `1/4`, strictly inside `T`.  They are in convex position and the
whole configuration is in general position.  Thus every `F subseteq X` is
an ordinary face, while `A union {x_j}` is nonconvex for every `j`.

The source `A` has only one triple, so every blocked point is assigned to
the canonical root `T`.  All rooted circuits have the same interior class,
and the deterministic largest rooted pocket is `X`.  This is a genuine
rank-three incidence of the marking scheme, with

\[
                              \omega(A,T)={m\over m+3}. \tag{10}
\]

It is also heavy in the rank-safe definition for all `m>=4`.  Indeed
`R>=m`, the Boolean `X` bank and the trivial bound `V<=2^{m+3}` give
`mu>=m/16`, and hence

\[
 {D_0\over2}
  ={m+3-2\mu\over2(R-2)\mu}
  \le {8(m+3)\over m(m-2)}<m.                           \tag{11}
\]

Fix the guard `G=A`, fix the column `x=x_1`, and for every
`S subseteq X-{x}` take the actual released face

\[
                              F_S=\{x\}\cup S.          \tag{12}
\]

Deleting `G` releases `F_S` itself.  There are exactly

\[
                              H=2^{m-1}=2^{n-4}         \tag{13}
\]

records.  They have identical `(A,T,G,x)` and lie in one dyadic layer with
weight `omega(A,T)`, but their actual face marks `F_S` are pairwise
distinct.

If `F_S` is omitted from the description, the `H` records become `H`
parallel copies of the same edge `(A,x)`, so a simple-star pooling preserves
only one edge.  If demand is preserved by treating `F_S` as a state, then
`L>=H`, which is exponential in `n`.  These are not chronology aliases:
each `F_S` is a different actual ordinary face.  Conversely the family
`{F_S}` is a load-one face bank of size `H`, explaining exactly how the
regression is paid.

The same example applies to a variable support word which is itself an
actual pocket face.  Merely selecting one canonical label of that word
does not turn the product into a label-primitive record family.

## 4. Quasipolynomial relaxation and exact coefficient threshold

Let the fixed-gap induction exponent be `a=1/2-delta` and put `L=log n`.
Deletion minimality gives

\[
                              \mu\le(2a+o(1))L.         \tag{14}
\]

In the rank-safe marking theorem, choose the cutoff parameter
`K_0=2+epsilon`.  It retains a positive constant fraction of the marked
mass and gives

\[
                    r=|A|\le\kappa L,\qquad
                    \kappa=(2+\epsilon)2a+o(1)<2+\epsilon.       \tag{15}
\]

Suppose a global state uses `c_0` independent combinatorial objects on
`A`, each no more numerous than all maps from `A` to `r+1` colors.  This
overcounts subsets, set partitions, matchings, orderings, source masks,
and role assignments.  Their total number is at most

\[
 L_A\le(r+1)^{c_0r},qquad
 \log L_A\le(c_0\kappa+o(1))L\log L.                   \tag{16}
\]

A fixed number of external labels contributes only `O(L)` further bits.
Thus the triangle-tag terminal loss becomes

\[
          \log\bigl(2L_A n^{3/2}\bigr)
             \le(c_0\kappa+o(1))L\log L.              \tag{17}
\]

The deterministic rooted pocket has size

\[
 m\ge {n-2\mu\over8(R-2)\mu}
       \ge {n\over(16a^2+o(1))L^3}.                    \tag{18}
\]

Therefore passing the inductive bank from scale `m` back to `n` loses

\[
 aL^2-a(\log m)^2
                   \le(6a+o(1))L\log L,               \tag{19}
\]

whose limiting coefficient is at most `3`.  If other retention steps cost
`C_ret L log L` bits, a terminal multiplier

\[
                         n^{\sigma\log L}               \tag{20}
\]

closes all these losses whenever

\[
                    \boxed{\sigma>6a+c_0\kappa+C_{ret}.}         \tag{21}
\]

This condition is compatible with the rich-role mechanisms.  For example,
the multirole endpoint bank with `rho q` good roles,
`q>=kappa_0L`, and `K=L^D` has

\[
 K^{\rho q/3}
       \ge n^{(\rho\kappa_0D/3)\log L}.                \tag{22}
\]

Since every balanced role contains `n^{1-o(1)}` candidate endpoints, any
fixed `D` is allowed for large `n`.  Hence choosing

\[
 D>{3(6a+c_0\kappa+C_{ret})\over\rho\kappa_0}          \tag{23}
\]

beats every fixed source-internal description coefficient.  The analogous
convex-ear coefficient is linear in `D` as well.

The limitation is exact.  Choosing `Theta(r)` **ambient** labels freely
costs

\[
                            n^{\Theta(r)}=2^{\Theta(L^2)},        \tag{24}
\]

which no fixed `D` in (22) absorbs.  A partition or matching of a fixed
decoded `r`-set is safe; selecting the `r` external labels on which that
structure lives is not.  In the current chain:

* one endpoint pair, blocked label, or bounded circuit witness is safe;
* canonical masks, roots, orderings, and partitions of `A` are safe by
  (16);
* a whole matching/support alphabet of external labels must be erased by
  row-star pooling or retained in an output; and
* an arbitrary released pocket face is fatal, as (12)--(13) demonstrate.

Thus `L=n^O(1)` may be relaxed to
`L=2^{C_L L log L+O(L)}` with a proved constant `C_L`, but the upstream
label-primitive/face-bank dichotomy is still necessary.

## 5. Consequence for the live chain

The exact decoders already banked remove the following potential
superpolynomial losses on a rank-`O(log n)` source:

* root choice and source-side circuit traces;
* base/guard/cover masks;
* tangent edge, endpoint pair, and canonical radial depth;
* finitely many signed circuit and side/gap states; and
* arbitrary names for the same active label support.

What they do not remove is an actual released face, completion word, or
support face of unbounded rank.  Such a word can have exponentially many
values over one fixed source and one fixed projected label, as (12) shows.

Therefore the proposed global state tuple proves polynomial description
load only after the upstream promotion is known to be label primitive, or
after every remaining face word is retained by a bounded-overlap ordinary
output.  The latter is the still-open coexistence/global-overlap branch;
it cannot be replaced by chronology canonicalization.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_polynomial_description_load_face_alphabet.py
```

Expected output:

```text
PASS: polynomial label states, dyadic pooling, and exponential actual face alphabet
```
