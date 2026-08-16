# Source reuse: a stretchable balanced one-ended profile barrier

**Date:** 2026-08-15.  All logarithms are base two.  This continues
`ACYCLIC_EDGE_DAG_DOWNSHADOW_AND_REUSE_GATE.md`.

## Verdict

The exact source-reuse residue cannot be closed by retaining a bounded-rank
source tag together with the full carrier edge.  In a universal dominance
cage, every ordinary face containing that edge contains at most one source
label.  This is a geometric circuit obstruction, not decoder loss.

More strongly, there is a scalable rational stretchable family in which

* the actual source is a convex `q=2m`-label polygon with
  `H=2^q` ordinary faces;
* there are `s` left and `s` right carrier endpoints and `s^2` dispersed
  carrier edges;
* every source face of rank at least two is terminal-bad over every edge;
* records are weighted by `1/s^2`, so total weight over the `s^2` edges is
  exactly one for every actual source face;
* the total record mass is
  `W=2^q-q-1=(1-o(1))H`, while every edge fibre has relative weight
  exactly `1/s^2`; and
* both one-ended source profiles have size at most
  `q^2 2^{q/2+O(1)}`.

The whole configuration has the exact upper bound

\[
 V\le H+(2^s-1)(P_L+P_R)+(q+1)2^{2s},                 \tag{1}
\]

where `P_L,P_R<=q^2 2^{q/2+O(1)}`.  Taking, for example, `q=4s` gives

\[
                         V=(1+o(1))H=(1+o(1))W.          \tag{2}
\]

Thus no local theorem from

> actual source face + dispersed full edge + singleton completion +
> endpoint downshadow

can force the missing factor `s^{theta_*}`.  Even the entire ambient face
complex in this stretchable cell has only `(1+o(1))W` faces.  The endpoint
shield `2^{2s}` and both one-ended banks are exponentially smaller than
`W` at `q=4s`.

This is a **local/live-normalized interface barrier**, not a global
sub-half construction: `H=2^q` is an enormous Boolean source bank on
`q+2s` points.  Its consequence is nevertheless exact.  Any successful
global argument must use history outside this cell, a minimizer mutation
excluding the Boolean/balanced source, or a return module whose output
retains source information in a different physical component.  Rank-safe
endpoint Cauchy inside the cell cannot absorb the codegree.

## 1. Why a full-edge source tag is impossible

Let `e={u,v}` be a carrier edge and let `Q` be in its universal dominance
cage.  Thus its labels have a strict order `<` such that

\[
             x<y\quad\Longrightarrow\quad
             x\in\operatorname{int}\operatorname{conv}\{u,v,y\}.\tag{3}
\]

### Lemma 1 (full-edge tag rank at most one)

If `U subseteq {u,v} union Q` is ordinary and `e subseteq U`, then

\[
                              |U\cap Q|\le1.             \tag{4}
\]

**Proof.**  If `x<y` both belong to `U`, the bad four-set
`{u,v,x,y}` survives in `U` by (3). `square`

In particular, no carrier-interior downshadow changes (4): if an output
retains the full distinguished edge, adding any rank-two source tag
recreates the same circuit.  The only source-retaining outputs must omit
`u` or omit `v`.  They are genuinely one-ended.

There is always a two-output encoding: `{u,x,y}` and `{v,x,y}` are
ordinary triples and together recover the edge and the source pair.  But
this is a square bank, not one ordinary output; Cauchy incurs the familiar
square-root loss.

## 2. Balanced visible-arc profiles

Let `Q` be a strictly convex `q`-gon and let `z` be an exterior point.
The two tangents from `z` cut its boundary into a visible arc and a far
arc.  Suppose the visible arc contains at least `m` vertices.

### Lemma 2 (one-ended visible-arc bound)

The number `P_z` of subsets `A subseteq Q` for which `A union {z}` is
ordinary satisfies

\[
 P_z\le 2^{q-m}\sum_{i=0}^2{m\choose i}
       \le(q+1)^2 2^{q-m}.                               \tag{5}
\]

**Proof.**  Any three selected vertices on the visible convex chain, in
their boundary order, have the middle vertex inside the triangle formed
by `z` and the outer two.  Hence a compatible subset selects at most two
vertices of that arc.  Its choices on the far arc are unrestricted.
Counting proves (5). `square`

Take a centrally symmetric rational convex `q=2m`-gon and two antipodal
exterior direction chambers.  Each visible arc contains `m+O(1)` vertices.
Small open perturbations of either chamber preserve the same tangent
indices, so for finite endpoint clouds `L,R` in those chambers,

\[
               P_L:=\max_{\ell\in L}P_\ell,\qquad
               P_R:=\max_{r\in R}P_r
                    \le q^2 2^{q/2+O(1)}.               \tag{6}
\]

Now apply the orientation-preserving universal affine squeeze

\[
 (a_i,b_i)\longmapsto
  (\varepsilon a_i,
        1+3\varepsilon a_i+\varepsilon^2b_i).            \tag{7}
\]

Choose the generic first coordinates `a_i` distinct.  This preserves the
convex order type of `Q`.  Put `L` near `(-1,0)` and `R` near `(1,0)` on a
lower parabolic arc.  For small enough endpoint chambers and `epsilon`,
the strict universal containment (3) holds simultaneously for every
cross edge `ell r`, while the two one-ended visible-arc splits remain
balanced.  All conditions are open sign inequalities, so rational
general-position choices exist for every finite `q,s`.

Here is the sign audit behind that scalable assertion.  First freeze the
limiting edge `(-1,0)(1,0)`.  For `a_i<a_j`, the two side-line tests for
the image of `i` against the triangle with apex the image of `j` have
leading terms respectively positive multiples of
`epsilon(a_j-a_i)` (the relevant limiting side slopes are `1` and
`-1`, whereas the source chain has slope `3`).  The base-line test is
strictly positive.  Hence the image of `i` lies strictly inside that
triangle for all sufficiently small positive `epsilon`.  There are only
finitely many pairs, so one `epsilon` works simultaneously.  The signs
remain strict when the two edge endpoints range over sufficiently small
disjoint chambers; choose `s` rational points in each chamber and then a
rational general-position perturbation.

Under the inverse of (7), the left endpoint chamber tends to vertical
infinity in one direction and the right chamber to vertical infinity in
the antipodal direction: the inverse second coordinate is
`(Y-1-3X)/epsilon^2`.  In a centrally symmetric `2m`-gon, a generic
direction at infinity has antipodal tangent vertices, so its visible
boundary arc contains `m+O(1)` vertices.  Tangent indices are locally
constant away from the finitely many vertex directions.  Shrinking the
two endpoint chambers therefore gives the simultaneous balanced bound
(6), independently of `s`.

## 3. The normalized actual-source rectangle

Let

\[
          \mathcal A=\{A\subseteq Q:|A|\ge2\},
          \qquad T=|\mathcal A|=2^q-q-1.                \tag{8}
\]

Every `A` is an actual ordinary source face.  For each

\[
                    (A,\ell,r)\in\mathcal A\times L\times R     \tag{9}
\]

assign weight `1/s^2`.  Then

\[
 \sum_{\ell,r}{1\over s^2}=1\quad\text{for every source }A,
 \qquad W=T.                                            \tag{10}
\]

Thus the construction obeys the rank-safe canonical rule “total marked
weight at most one over each actual source”; it is not an unnormalized
cartesian record count.

Every physical edge occurs with weighted mass `T/s^2`, giving relative
fibre `1/s^2`.  Every singleton completion `{ell,r,x}` is ordinary, while
every residual of `A` of rank at least two is bad with `ell r`.  The
singleton output has exact load

\[
 {1\over s^2}|\{A\in\mathcal A:x\in A\}|
             ={2^{q-1}-1\over s^2}.                     \tag{11}
\]

This is the literal source codegree left after the source face is erased.

### Exact audit of the source-retaining two-output bank

There is one canonical way to avoid that codegree.  For every record and
every `x in A`, retain the ordered pair of ordinary faces

\[
                         \bigl(A,\{\ell,r,x\}\bigr).     \tag{12}
\]

It recovers `A,ell,r,x` exactly.  Hence the number of distinct ordered
pairs in (12) is

\[
 s^2\sum_{A\in\mathcal A}|A|
       =s^2\bigl(q2^{q-1}-q\bigr),                       \tag{13}
\]

and ordinary two-coordinate Cauchy gives

\[
              V\ge s\sqrt{q2^{q-1}-q}.                  \tag{14}
\]

This is the rank-safe endpoint-fibre Cauchy estimate with the actual old
source retained.  At `q=4s`, its ratio to the source lower bound `H=2^q`
is

\[
     {s\sqrt{q2^{q-1}-q}\over2^q}
        =O\!\left(s\sqrt q\,2^{-q/2}\right)=o(1).        \tag{15}
\]

Thus retaining the old source removes output codegree only by moving the
argument to a two-face square whose square-root loss is fatal.  Enlarging
the second coordinate by a carrier-interior downshadow cannot improve
this locally: Lemma 1 says every ordinary second coordinate retaining the
full edge still has source rank at most one, and the full-complex count
below already includes all such choices.

## 4. Full face-count upper bound

Partition an arbitrary ordinary face of the whole configuration by its
trace `A` on `Q`.

* If `|A|<=1`, there are at most `(q+1)2^{2s}` choices.
* If `|A|>=2` and the endpoint trace meets both `L` and `R`, any chosen
  cross edge together with any source pair is a bad four-set.  This case
  is impossible.
* If `|A|>=2` and the nonempty endpoint trace lies only in `L`, heredity
  implies `A union {ell}` is ordinary for each selected `ell`.  For each
  of the `2^s-1` endpoint masks there are at most `P_L` choices of `A`.
  The same holds on the right.
* The endpoint-empty faces contribute exactly `H=2^q` source subsets.

This proves (1).  By (6), when `q=4s`,

\[
 {2^s(P_L+P_R)\over H}
       \le q^2 2^{-s+O(1)}=o(1),
 \qquad {(q+1)2^{2s}\over H}=o(1),                     \tag{16}
\]

which proves (2).

The bound counts **every** ordinary face, not only the selected source,
endpoint, or profile banks.  Therefore no alternative one-face routing
confined to these labels can manufacture an `s^{theta_*}` gain.

## 5. Verification

`verify_source_reuse_balanced_one_ended_profile.py` uses exact rational
coordinates with `q=8,s=2`.  It verifies:

1. central symmetry/convexity of the source and general position of all
   12 labels;
2. simultaneous terminal containment for every source pair and all four
   dispersed edges;
3. both one-ended profile counts (exactly `82` in the finite instance);
4. all `2^12` subsets, obtaining `V=829` and checking (1);
5. normalized source mass `W=247`, edge density `1/4`, and exact
   singleton load `127/4`.
