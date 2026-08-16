# Quadratic four-target cores: projection compression and trace rectangle-or-shield

**Date:** 2026-08-15.  This continues
`PAIRWISE_CONVEX_TRIPLE_CIRCUIT_COVER.md` at the high-projection-reuse
`A by C` residue.  All roles below are disjointly coloured and all point
sets are in planar general position.

## Verdict

There is an exact one-face rectangle-or-shield theorem after stripping the
common base.  Write

\[
                       A=B\cup G,\qquad C=B\cup F,       \tag{1}
\]

where `G` and `F` are ordinary faces by heredity.  For each record:

1. if `G union F` is convex, its full trace union is an ordinary mixed
   output;
2. if `G union F` is nonconvex, let `tau` be the minimum number of trace
   labels whose deletion makes it convex.  A minimum circuit transversal
   releases a mixed face of rank `|G|+|F|-tau`, while a disjoint circuit
   matching exposes a Boolean shield of rank at least `tau/2` wholly in
   one of the two ordinary sides.

Consequently every rank-`r=|G|+|F|` record canonically generates at least

\[
                              2^{r/3}-1                 \tag{2}

ordinary one-face outputs, either mixed trace downfaces or one-side shield
faces.  With `Lambda_tr` equal to the actual maximum weighted output load,

\[
                  \boxed{H(2^{r/3}-1)\le\Lambda_{\rm tr}V(P)}. \tag{3}
\]

The theorem is global and exact, but (3) is not a closure unless
`Lambda_tr` is controlled.  A dense row alphabet can reuse every column
shield, and a dense column alphabet can reuse every row shield.

The preliminary two-point projection is also exact.  Choosing one actual
row mark `g(G)` and column mark `f(F)` gives the ordinary face `{g,f}`.
Low load closes immediately; high load fixes a common mark pair and pushes
all entropy into the remaining traces.  This is the correct formal meaning
of “high projection reuse.”

A genuine quadratic-entropy lift of the singleton cage exists with
arbitrarily high single-mark reuse while retaining all four Hall targets
and the fixed bad `BFv` circuit.  In the natural vertex-blow-up lift,
however, every `G union F` is convex, so the trace-union bank has load one
and exactly the full row-by-column size.  Thus high projection reuse alone
does not produce a regression.  Any counter-lift must simultaneously make
most trace unions bad and make both the transversal-release and one-side
shield banks have high global load.

## 1. Exact cross-mark projection

Let `Omega` be a weighted family of records `(G,F)`, with nonempty traces
on disjoint row and column supports.  Choose canonical labels

\[
                         g(G)\in G,\qquad f(F)\in F.      \tag{4}
\]

Every two-point set

\[
                              P(G,F)=\{g(G),f(F)\}       \tag{5}
\]

is an ordinary face.  Define

\[
 \Delta_{\rm mark}=\max_P
       \sum_{\omega:P(G_\omega,F_\omega)=P}w_\omega.    \tag{6}
\]

> **Lemma 1 (mark projection bank).**
> 
> \[
>                              H\le\Delta_{\rm mark}V(P). \tag{7}
> \]

**Proof.**  Group the record weights by their actual two-point output (5).
Every group has weight at most (6), and there are at most `V(P)` ordinary
outputs.  QED.

For a complete unit-weight rectangle `mathcal G times mathcal F`, put

\[
 d_G=\max_x|\{G:g(G)=x\}|,\qquad
 d_F=\max_y|\{F:f(F)=y\}|.                              \tag{8}
\]

Then `Delta_mark<=d_Gd_F` and

\[
                 V(P)\ge{|\mathcal G||\mathcal F|\over d_Gd_F}. \tag{9}
\]

Failure at threshold `K` fixes one actual pair `(g,f)` carrying weight
greater than `K`.  Iterating the operation over role-coloured coordinates
either decodes the faces or arrives at a family with genuinely correlated,
high-reuse supports; merely counting the first marks is not enough.

## 2. Bad trace unions have a release/shield cover

Let `G,F` be disjoint ordinary faces, but suppose

\[
                              U=G\cup F                 \tag{10}
\]

is nonconvex.  Let `mathcal K(G,F)` be its nonconvex four-subsets.

> **Theorem 2 (two-side circuit cover).**  Every `K in mathcal K` meets
> both `G` and `F`, and hence has split
> 
> \[
>                    (1G,3F),\quad(2G,2F),\quad(3G,1F). \tag{11}
> \]
> 
> For `Z subseteq U`, the set `U-Z` is convex if and only if `Z` meets
> every member of `mathcal K`.  If `tau` and `nu` are the transversal and
> matching numbers of `mathcal K`, then
> 
> \[
>                              \nu\le\tau\le4\nu.        \tag{12}
> \]

**Proof.**  A bad four-set contained in one side would contradict the
convexity of that side, proving (11).  The release equivalence follows in
both directions from planar Caratheodory exactly as in the rooted theorem:
a surviving circuit obstructs convexity, while any remaining nonconvexity
contains a surviving bad four-set.  A matching lower-bounds every
transversal.  The union of the four-label edges in a maximal matching is a
transversal, proving the upper bound in (12).  QED.

Choose a canonical minimum transversal `Z`, a canonical maximum matching,
and put

\[
                         R=U-Z.                          \tag{13}
\]

The matched circuits use `4nu` distinct labels.  At least one side contains
at least `2nu>=tau/2` of them; call that canonical larger-side set `S`.
Then

\[
                  R\in\mathcal F(P),\qquad
                  S\subseteq G\text{ or }S\subseteq F, \tag{14}
\]

so both `R` and `S` are ordinary faces.

## 3. The trace rectangle-or-shield incidence theorem

For every record `omega=(G,F)` of trace rank
`r_omega=|G|+|F|`, define a nonempty ordinary output reservoir
`mathcal B_omega` as follows.

* If `G union F` is convex, use all nonempty subsets of `G union F`.
* If it is bad and `tau<=2r/3`, use all nonempty subsets of the released
  face `R` in (13).
* If it is bad and `tau>2r/3`, use all nonempty subsets of the one-side
  shield `S` in (14).

In the three cases respectively,

\[
 |\mathcal B_\omega|=2^r-1,\qquad
 |\mathcal B_\omega|=2^{r-\tau}-1,
 \qquad |\mathcal B_\omega|=2^{|S|}-1.                 \tag{15}
\]

Equations (12)--(14) imply in every case

\[
                         |\mathcal B_\omega|\ge2^{r/3}-1. \tag{16}
\]

Define the actual combined one-face load

\[
 \Lambda_{\rm tr}=\max_X
       \sum_{\omega:X\in\mathcal B_\omega}w_\omega.    \tag{17}
\]

> **Theorem 3 (weighted trace rectangle-or-shield).**
> 
> \[
> \boxed{
>   \sum_\omega w_\omega(2^{r_\omega/3}-1)
>                       \le\Lambda_{\rm tr}V(P).}       \tag{18}
> \]

**Proof.**  Count weighted incidences `(omega,X)` with
`X in mathcal B_omega`.  Equation (16) lower-bounds their total by the
left side of (18).  Grouping by the actual ordinary face `X` upper-bounds
it by `Lambda_tr V(P)`.  QED.

For uniform rank, (18) is (3).  The empty output was excluded because it
would carry the whole record mass and make the displayed load vacuous.
All mark, source, released-face, circuit, and context reuse is nevertheless
allowed and recorded exactly by (17).

### 3.1 When a fixed circuit guard really closes

Suppose a bad subfamily has one fixed **labelled** transversal `Z_0` such
that

\[
                    (G\cup F)-Z_0\text{ is convex}      \tag{19}
\]

for every record, and every label of `Z_0` is a fixed mandatory row or
column anchor.  The full released output in (19), together with the fixed
role supports, recovers `G,F` by adding `Z_0`.  Hence its load is exactly
the actual duplicate-record multiplicity.  A homogeneous fixed circuit
product is therefore harmless when one common bounded guard hits **all**
its circuits.  The projective-universal root-bad examples evade
root-admissibility, but not this labelled guard release.

If only the deleted role positions are fixed and each missing coordinate
support has size at most `D`, the output load is at most

\[
                          hD^{|Z|},                      \tag{20}
\]

where `h` is the actual multiplicity after the missing labels are restored.
Allowing any set of at most `t` deleted roles replaces this by the honest
description bound

\[
                    h\sum_{j=0}^t{r\choose j}D^j.       \tag{21}
\]

These are decoder bounds, not claims that `t` is automatically small.

## 4. A quadratic high-reuse lift that is paid by the trace bank

The singleton cage from the preceding report can be blown up without
losing any of the four target conditions.  Keep

\[
\begin{aligned}
B&=\{(-5,1),(-1,11),(2,9),(11,1)\},\\
v&=(5,-6),\qquad x=(2,-10),\qquad z=(9,-4).             \tag{22}
\end{aligned}
\]

Replace the source-ear vertex near `(0,-12)` by `p` consecutive macro
roles, and replace the two pocket vertices near `x,z` by `q` consecutive
macro roles, while retaining `x,z` as fixed pocket anchors.  Choose the
macro roles as sufficiently short rational convex chains in the relevant
ear cones.  Then replace each macro role by `D` rational points in a small
enough neighborhood.  Openness of the finitely many strict orientation
and containment signs gives, for every one-point-per-role pair of words,

\[
\begin{gathered}
 B\cup G,\quad B\cup F,\quad F\cup\{v\},\quad B\cup\{v\},
       \quad G\cup F\text{ convex},                    \tag{23}\\
 v\in\operatorname{int}\triangle((-1,11),x,z),
       \quad B\cup F\cup\{v\}\text{ nonconvex}.       \tag{24}
\end{gathered}
\]

The standard vertex-blow-up justification is elementary: first choose a
strict convex macro polygon in which the roles replacing each old vertex
form a short boundary chain inside the intersection of its finitely many
normal cones; then shrink each finite support until every transversal has
the macro signs.  Rational points are dense in all the resulting open
cells.

Let `mathcal G` and `mathcal F` be the two full products.  Then

\[
             |\mathcal G|=D^p,\qquad |\mathcal F|=D^q,
             \qquad H=D^{p+q}.                          \tag{25}
\]

One chosen row coordinate has reuse `D^{p-1}` and one column coordinate
has reuse `D^{q-1}`, so the mark-pair load is

\[
                          \Delta_{\rm mark}=D^{p+q-2}.  \tag{26}
\]

At `p,q=Theta(log D)`, (25) has quadratic logarithmic entropy and (26) is
also quadratic: this is a genuine high-projection-reuse lift.  Its four
Hall target density is

\[
                 \lambda_4={D^{p+q}\over D^p+2D^q+1}.  \tag{27}

\]

Nevertheless every mixed trace `G union F` in (23) is an ordinary face,
and role colouring decodes both words from it.  These are exactly
`D^{p+q}` distinct load-one outputs.  The natural quadratic lift therefore
pays through the good branch of Theorem 3.

The verifier gives a completely explicit finite instance with `p=q=2`,
`D=2`.  It has 4 row faces, 4 column faces, 16 records, mark-pair load 4,
four-target density `16/13`, and 16 distinct convex trace unions.

## 5. Exact surviving anti-alignment

Combining Lemma 1 and Theorem 3, a dense quadratic four-target core can
remain unpaid only if all of the following occur simultaneously.

1. Every bounded collection of row/column mark projections has high load.
2. Almost every trace union `G union F` is nonconvex.
3. In the low-`tau` cells, the mixed transversal-release/downshadow outputs
   have high global load; no common labelled guard has bounded decoder.
4. In the high-`tau` cells, the large one-side circuit shields are reused
   across the opposite face alphabet with comparably high load.

The singleton same-edge regression realizes items 2--3 locally but fails
item 1.  The quadratic vertex blow-up realizes item 1 but fails item 2.
Thus neither is a counterexample to (18).  Constructing all four items in
one stretchable bounded-rank family, or proving that planarity forbids
their coexistence, is the exact next gate.  The present theorem reduces
that gate to actual trace/downface loads without assuming a false tangent
edge or a fictitious mixed union.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_quadratic_trace_rectangle_or_shield.py
```

Expected output:

```text
PASS: bad-trace circuits=1 tau=1 nu=1 local_bank=7; lift rows=4 cols=4 records=16 hall4=16/13 mark_load=4 trace_load=1
```

The checker uses exact `Fraction` arithmetic.  It verifies the bad-trace
circuit splits, release/transversal equivalence, matching bound and local
`r/3` reservoir.  For the explicit lift it exhausts all sixteen
transversals, checks every condition in (23)--(24), verifies general
position, and computes the cross-mark, four-target, and trace-union loads
exactly.
