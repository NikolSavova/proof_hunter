# Endpoint--pocket codegree: the exact coexistence dichotomy

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The convex-pair ear theorem does not by itself multiply the high-root
pocket bank.  The exact missing coordinate is already visible one endpoint
at a time.

For a released convex base `C_F=B union F` and a disjoint matching edge
`e={a_e,b_e}`, let

\[
 g(e,F)=1_{C_F\cup\{a_e\}\text{ convex}}
       +1_{C_F\cup\{b_e\}\text{ convex}}\in\{0,1,2\}.  \tag{1}
\]

Every compatible endpoint identifies its matching edge.  Thus large total
`g` gives a one-face endpoint--pocket bank with no pair-index loss.  At the
other extreme, if the normalized total compatibility is at most `theta`,
at least a `1-theta` share of pair--pocket incidences have `g=0`.  Each such
incidence supplies **two** canonical bad four-circuits, and each circuit
necessarily meets both the endpoint and the actual pocket trace `F`.

With weighted contexts and arbitrary cross-context reuse, the exact global
inequality is

\[
 \boxed{\quad
   \sum_cw_c\sum_{e\in M_c}\sum_{F\in H_c}g_c(e,F)
       \le \Lambda V(P).\quad}                          \tag{2}
\]

Here `Lambda` is the actual maximum total input weight decoded by one
ordinary output; bases, roots, guards, carriers, and pocket descriptions
are all included.  There is no implicit copy of `V` per context.

There is one further exact descent.  Put

\[
 h(e,F)=1_{F\cup\{a_e\}\text{ convex}}
       +1_{F\cup\{b_e\}\text{ convex}}.                 \tag{2a}
\]

Always `g<=h`.  Large `h` gives not just the detached face
`F union {v}`, but also the unconditional source marginal `B union {v}`
and released face `B union F`.  Fractional Hall routing among these
actual targets supersedes the raw detached load.  Low Hall density pays
linearly; high density localizes a fixed geometric `(B,F,v,e)` pair and
leaves only source-mask/chronology multiplicity.  If `h` is also small,
the two canonical circuits for most incidences lie wholly inside
`F union {a_e}` and `F union {b_e}`.  Thus the exact alternatives are:

1. attached endpoint--pocket faces with the context retained;
2. detached/base marginal faces with exact fractional Hall load;
3. a high-Hall fixed-pair fibre, charged to source masks or actual
   chronology multiplicity; or
4. a double detached circuit rectangle inside one pocket child.

This is a genuine reduction, not a closure.  A six-point rational cage has
a convex pair ear over a base `B` and a convex released pocket base
`C=B union {x}`, but **both** endpoints become hidden after `x` is retained.
Its detached two-sets `{x,a}` and `{x,b}` remain convex, so the example
lands sharply in branch 2 and demonstrates context erasure rather than
branch 2.  The raw detached collision is therefore not the live atom.  The
residue is either fixed-pair source history or the weighted family of
double detached circuits.

## 1. Fixed-context endpoint bank

Let `B` and every `B union F`, `F in H`, be ordinary faces.  Assume a
matching `M` on labels disjoint from every pocket trace.  Require also that

\[
                       B\cup\{v\}\text{ is convex}       \tag{3}
\]

for every endpoint `v` of `M`.  This is the source-side compatibility
which makes a subsequent failure genuinely involve the pocket rather than
an already bad base seam.

For every compatible triple `(e,F,v)`, output

\[
                         \Phi(e,F,v)=B\cup F\cup\{v\}.   \tag{4}
\]

> **Lemma 1 (matching endpoint decoder).**  Inside one recoverable
> context, the outputs (4) are all distinct, and their number is exactly
>
> \[
>                              \sum_{e,F}g(e,F).          \tag{5}
> \]

**Proof.**  Disjointness recovers `F` as the intersection with the pocket
support.  The unique nonbase endpoint `v` recovers its matching edge `e`.
The output itself records which endpoint was used.  QED.

If `g(e,F)=2` and the local four-set consisting of `e` and the two tangent
neighbors of its gap is convex, the context-compatible insertion lemma
from `CONVEX_BAD_PAIR_EAR_PROMOTION.md` additionally makes
`B union F union e` an ordinary face.  This stronger output is optional:
one compatible endpoint already retains both the pair index and the
pocket trace.

## 2. Weighted global decoder

Let `c` range over arbitrary marked contexts and assign nonnegative weights
`w_c`.  Context `c` contains `B_c`, a matching `M_c`, and a pocket family
`H_c`.  The output map is (4) with the context subscript.  Define

\[
 \Lambda=\max_W\sum_{(c,e,F,v):\Phi_c(e,F,v)=W}w_c.       \tag{6}
\]

> **Theorem 2 (weighted endpoint--pocket bank).**  Equation (2) holds.
> Consequently, if
>
> \[
> N=\sum_cw_c|M_c||H_c|,
> \qquad
> \sum_cw_c\sum_{e,F}g_c(e,F)\ge\theta N,               \tag{7}
> \]
>
> then
>
> \[
>                             V(P)\ge{\theta N\over\Lambda}.       \tag{8}
> \]

**Proof.**  The left side of (2) is the total weighted number of generating
records.  Group it by the ordinary output `W`.  Every group has weight at
most `Lambda`, and there are at most `V(P)` outputs.  This proves (2) and
(8).  QED.

When `F=W cap X_T`, an endpoint identifies `e`, and the retained remainder
identifies `B_c`, the only load comes from the genuinely omitted data such
as `(T,G)`; this recovers the familiar marked-release decoder.  If the
remainder does not recover the base or carrier, that multiplicity remains
in (6).  Merely saying that the supports are disjoint does not remove it.

## 3. Exact low-codegree alternative

For one incidence put

\[
 z=1_{g=0},\qquad o=1_{g=1},\qquad t=1_{g=2}.            \tag{9}
\]

Pointwise `z+o+t=1` and `g=o+2t`, so

\[
                              z\ge1-g.                   \tag{10}
\]

After summing with the context weights:

> **Corollary 3 (double-incompatibility mass).**  If the compatibility sum
> in (7) is at most `theta N`, then the total weight of incidences with
> `g(e,F)=0` is at least
>
> \[
>                              (1-\theta)N.              \tag{11}
> \]

For such an incidence both `B union F union {a_e}` and
`B union F union {b_e}` are nonconvex.  Because `B union F` and
`B union {v}` are convex, a minimal nonconvexity witness has four points in
general position, contains `v`, and meets `F`.  Equivalently, for each
endpoint `v in e` there is a canonical `1+3` circuit

\[
                    Q(e,F,v)\subseteq B\cup F\cup\{v\},
 \qquad v\in Q(e,F,v),\quad Q(e,F,v)\cap F\ne\varnothing.          \tag{12}
\]

To see the last assertion directly, any witness avoiding `v` would lie in
the convex set `B union F`, while one avoiding `F` would lie in the convex
set `B union {v}`.  Planar Caratheodory reduces a hidden point and its
containing triangle to four labels.  Choosing the first witness in a fixed
global order makes (12) canonical.  The two circuits in (12) retain
different endpoint labels and hence different matching marks.

Thus the low branch is not an unmarked statement that “some seam is bad.”
It is a weighted rectangle indexed by `(e,F)`, with two marked
endpoint--pocket circuits in every surviving cell.

### 3.1 Detached endpoint descent

Define `h(e,F)` by (2a).  Every attached output is also a detached face, so
`g(e,F)<=h(e,F)`.  For a detached compatible record output

\[
                              \Psi(e,F,v)=F\cup\{v\}.     \tag{12a}
\]

The named pocket support recovers `F`, and the matching recovers `e` from
`v`; what (12a) may erase is the surrounding base/context.  Define its
actual weighted load

\[
 \Lambda_{\rm det}=\max_W
   \sum_{(c,e,F,v):\Psi_c(e,F,v)=W}w_c.                  \tag{12b}
\]

The same grouping proof as Theorem 2 gives

\[
\boxed{\quad
  \sum_cw_c\sum_{e,F}h_c(e,F)
          \le\Lambda_{\rm det}V(P).\quad}              \tag{12c}
\]

Equation (12c) is valid but not the sharp global route.  Every detached
record `r=(c,e,F,v)` also has the two ordinary faces

\[
 W_r=F\cup\{v\},\qquad Q_r=B_c\cup\{v\},\qquad
 C_r=B_c\cup F.                                      \tag{12c.1}
\]

The first is detached compatibility, the second is the standing
source-side hypothesis (3), and the third is the released pocket face.
Define the exact three-target Hall density

\[
 \eta_H=\max_{\varnothing\ne\mathcal R'\subseteq\mathcal R}
 {\sum_{r\in\mathcal R'}w_r\over
  |\bigcup_{r\in\mathcal R'}\{W_r,Q_r,C_r\}|}.          \tag{12c.2}
\]

The record-to-target max-flow/min-cut theorem gives the unconditional
strengthening

\[
                  \sum_cw_c\sum_{e,F}h_c(e,F)
                         \le \eta_HV(P).             \tag{12c.3}
\]

After endpoint/base/pocket role coloring, the ordered pair `(W_r,Q_r)`
recovers `v`, its matching edge `e`, `F`, and `B`.  Thus parallel-edge
load at a fixed pair is exactly the weight of source/guard histories with
the same geometric `(B,F,v,e)`, not an unexplained detached collision.
Hall pruning of any subfamily denser than `K` leaves a core of weighted
minimum target degree greater than `K`; bounded ordered-pair load turns
this into literal base-by-pocket expansion.  Unbounded pair load fixes
the geometric record and descends to the Boolean source-mask/chronology
bank.  This is proved and sharply verified in
`../agent_outer_internal_product/DETACHED_BASE_ENDPOINT_HALL_STRENGTHENING.md`
and `../agent_shield_circuit_cover/DETACHED_PAIR_SOURCE_MASK_HALL.md`.

Hence `sum h>=theta N` closes through a detached bank whenever
the Hall density (12c.2) is controlled; using only `Lambda_det` is a
weaker fallback.  If instead `sum h<=theta N`, at least
`(1-theta)N` incidences have `h=0`.  For every such incidence and each
endpoint `v in e`, the nonconvexity is already in `F union {v}`.  A
canonical planar witness satisfies

\[
                         Q_{\rm det}(e,F,v)\subseteq F\cup\{v\},
 \qquad v\in Q_{\rm det},\quad Q_{\rm det}\cap F\ne\varnothing.   \tag{12d}
\]

This is strictly stronger than (12): no carrier, root, guard, or base
label appears.  Circuit-component factoring may now be applied inside the
detached support.  Its known irreducible residue is one circuit-connected
child; no claim is made here that (12d) solves that child.

## 4. Exact convex-ear/pocket cage

Put

\[
 \begin{aligned}
 l&=(-3,0),& r&=(3,0),& t&=(0,5),\\
 a&=(-2,-1),& b&=(2,-1),& x&=(0,-4).
 \end{aligned}                                          \tag{13}
\]

Let `B={l,r,t}` and `C=B union {x}`.  Exact hull computation gives

\[
 B\cup\{a\},\ B\cup\{b\},\ B\cup\{a,b\},\ C           \tag{14}
\]

all in convex position.  Moreover `{l,a,b,r}` is a convex quadrilateral,
so `{a,b}` is a genuine commuting ear over the old base `B`.

Nevertheless

\[
      a\in\operatorname{int}\operatorname{conv}\{l,x,r\},
 \qquad
      b\in\operatorname{int}\operatorname{conv}\{l,x,r\}.          \tag{15}
\]

Hence neither `C union {a}` nor `C union {b}` is convex: this cell has
`g(e,{x})=0`, and its two circuits share the pocket-rooted cage
`{l,x,r}`.

On the other hand `{x,a}` and `{x,b}` are two-point faces, so
`h(e,{x})=2`.  The attached bank is killed while the detached bank is
perfect.  If many different retained bases reuse the same labels
`x,a,b`, all of those records collapse to the same two detached outputs;
that multiplicity is exactly `Lambda_det` in (12b), not a geometric
failure of the detached faces.

All twenty triples of the six points in (13) are noncollinear.  The failure
therefore is open and survives arbitrary sufficiently small rational
perturbations or substitution into a larger strict chart.  It proves that
ear promotion relative to the source base does not certify coexistence
with a released pocket face; the tangent base must be recomputed after the
pocket is retained.

There is also a taut sharp positive converse.  If `C`, not merely `B`,
admits both endpoints individually through the same gap and the local
four-set is convex, Lemma 1 of the ear report applied directly to `C`
gives `C union {a,b}` convex.  Thus no additional pair obstruction remains
after endpoint codegree two.  All of the difficulty is in proving that the
live pocket distribution has large endpoint compatibility, or releasing
the double circuits from (12).

## 5. High-root scope

For the canonical high-root pocket, every `x in X_T` initially lies inside
the root triangle `T`.  Therefore no nonempty pocket trace can coexist
with a source output retaining all of `T`; this is an immediate `1+3`
cage, independent of any pair ear.  The marked release operation must first
delete a guard hitting that cage.  After deletion the relevant base is

\[
                         C_{A,T,F,G}=(A\setminus G)\cup F,          \tag{16}
\]

not the original source skeleton `A`.  Bad-pair classification relative
to neighbors in `A` supplies no endpoint-codegree lower bound for (16), as
(13)--(15) demonstrate in the smallest possible model.

The exact positive input still needed is therefore one of:

1. a lower bound for the weighted compatibility sum in (7), with the
   actual marked-release load (6); or
2. a low-density fractional Hall route (12c.3) for the detached sum;
3. in the high-Hall branch, a source-mask/chronology charge for the fixed
   geometric pair; or
4. a face/shield release of the double detached circuit rectangle (12d).

This separates the old-base ear geometry, which is solved, from pocket
coexistence, which is not.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_endpoint_pocket_codegree.py
```

The checker verifies (13)--(15) and general position using exact integer
arithmetic, extracts both attached endpoint--pocket four-circuits and
checks the perfect detached branch, exhausts every
finite `g in {0,1,2}` pattern through eight cells to check (10)--(11), and
checks (2),(12c) on exact rational weighted decoder tables with deliberate
cross-context collisions.  The unconditional Hall strengthening and its
fixed-pair mask descent are separately verified by
`verify_detached_base_endpoint_hall.py` and
`verify_detached_pair_source_mask_hall.py`.
