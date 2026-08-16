# Directed profile contexts: exact cycle/DAG audit and the one-chamber shell

**Date:** 2026-08-15.  This continues
`QUADRATIC_TRACE_RECTANGLE_OR_SHIELD.md` at the conjunction of high mark
reuse, bad trace unions, high release load, and high one-side reuse.
All logarithms are base two.

## Verdict

The proposed directed-context split is combinatorially exact, but it is
not by itself a geometric multiplication theorem.

* A Hall-dense directed context graph has a nonempty weighted minimum-degree
  core.  If the core is acyclic, a topological source and sink carry the
  whole core degree in one direction.  If it is cyclic, it contains a
  directed context cycle.
* A directed cycle of pairwise compatible clouds need not glue: an exact
  seven-point example has all three pair unions convex and its three-way
  union nonconvex.  The missing circuit has split `1+2+1` across the three
  clouds and is invisible on every edge.
* High degree at one physical cloud does not imply several quantitatively
  separated projective directions.  A degree-`K` star may lie in one
  arbitrarily small containment chamber.  The correct statement needs an
  actual per-chamber load bound `M`; only then does degree `d` give at least
  `ceil(d/M)` direction chambers.

There is an exact `16 by 16` rational nested-shell product exhibiting both
failures on the live four-target data.  It has 256 actual records, every
trace union is bad, the first-mark load is 64, the canonical minimum
release has full-face load 8 and downface load 128, the canonical one-side
shield has load 16, and the four-target Hall load is `256/49`.  All 16
queries at a repeated outer word lie in the same strict containment
chamber.

This finite product scales to quadratic record entropy by increasing the
number of role clusters.  Whether arbitrary multi-point children create a
coefficient-half omitted-gap bank is **not** automatic.  The tempting
formula

\[
       B_{\rm gap}\stackrel{?}{\ge}
       D^{t-3}\left(\prod_{i=1}^t(V(X_i)-1)\right)^{1/t}.       \tag{1}
\]

This requires every local boundary profile to remain convex after the
macro gap is opened.  The exact strong-separation endpoint counterexample
has a four-block shell where all local faces exist but every ambient
endpoint profile of rank at least three is killed by one retained guard.
Thus strong separation and a common cyclic order do not prove (1).  The
natural one-chamber product is a genuine profile-compatibility survivor,
not a closed branch.

Finally, canonical radial decoding removes history names but not this
actual star.  Fixing `(A,e)` determines peel depth and carrier, but the
same actual source and one of its actual triangles can coexist with many
distinct actual opposite-cloud faces `F`.  Those are geometric records,
not chronology metadata.  Their `W,C` Hall targets are the available
payment.

## 1. The exact weighted graph split

Let `Gamma` be a finite directed multigraph of physical cloud states.  An
edge is one actual anti-aligned two-cloud context, with nonnegative weight.
Forget direction when taking incident degree.

> **Lemma 1 (weighted core).**  If the total edge weight is `H` and there
> are `N` nonisolated vertices, `Gamma` has a nonempty induced subgraph of
> minimum weighted incident degree at least `H/N`.

**Proof.**  Repeatedly delete a vertex of current incident weight strictly
less than `H/N`.  Charge an edge when its first endpoint is deleted.  If
all vertices were deleted, every edge would be charged exactly once, and
the total charge would be strictly less than `N(H/N)=H`, a contradiction.
QED.

The threshold may of course be replaced by any `d` with `H>dN` to obtain
strict minimum degree greater than `d`.

> **Lemma 2 (cycle or one-way star).**  A directed graph of minimum
> undirected weighted degree `delta` either contains a directed cycle, or
> has a source of weighted outdegree at least `delta` and a sink of
> weighted indegree at least `delta`.

**Proof.**  If it is acyclic, take any topological source and sink.  Every
edge incident with the source is outgoing, and every edge incident with
the sink is incoming.  Their undirected degrees are at least `delta`.
QED.

Now partition the query germs at every physical vertex into projective
direction chambers.  Let

\[
 M=\max_{x,\mathcal C}\{
       \hbox{incident edge weight at }x\hbox{ in chamber }\mathcal C\}.
                                                               \tag{2}
\]

Then a vertex of incident weight `d` meets at least `ceil(d/M)` chambers.
In particular, the often-invoked four-direction itinerary requires the
honest inequality

\[
                              d>3M.                     \tag{3}
\]

Degree without (2) proves no multi-direction statement.  Subdividing one
open chamber into differently named directions does not help: the query
cross-ratios can be made arbitrarily close and carry no uniform entropy.

## 2. A context cycle does not imply a cyclic face product

Use the exact blocks

\[
\begin{aligned}
 B&=\{(-5,1),(-1,11),(2,9),(11,1)\},\\
 F&=\{(2,-10),(9,-4)\},\qquad v=(5,-6).                \tag{4}
\end{aligned}
\]

All of

\[
                         B\cup F,\qquad B\cup\{v\},
                         \qquad F\cup\{v\}             \tag{5}
\]

are ordinary convex faces.  Orient the three abstract compatible edges

\[
                         B\longrightarrow F
                          \longrightarrow\{v\}
                          \longrightarrow B.            \tag{6}
\]

Nevertheless `B union F union {v}` is bad: the four-set

\[
                         \{(-1,11),(2,-10),(9,-4),v\}   \tag{7}
\]

has `v` strictly inside the triangle of the other three points.  Circuit
(7) meets all three blocks and no pairwise edge sees it.

Thus a cycle theorem needs a joint seam condition.  One exact sufficient
condition is 4-local closure: if every four-subset of the proposed cyclic
union is ordinary, planar Caratheodory implies that the whole union is
ordinary.  Pairwise edge compatibility checks only four-sets supported on
at most two cycle vertices and does not establish this condition.

This counterexample attacks a theorem which uses only the directed graph
and pairwise-convex edge predicates.  A more restrictive geometric edge
orientation may encode extra tangent or circuit data; such data must be
stated and checked rather than inferred from the existence of the cycle.

## 3. Exact one-chamber four-target product

All coordinates in this section are divided by `10000`.  The four outer
role supports are

\[
\begin{array}{c|cc}
0&(-99988,17)&(-100000,17)\\
1&(-2,-100016)&(12,-99992)\\
2&(100016,5)&(100019,-3)\\
3&(-3,100010)&(1,99995),
\end{array}                                             \tag{8}
\]

and the four inner supports are

\[
\begin{array}{c|cc}
0&(-60020,-29988)&(-59992,-29983)\\
1&(-29983,-60020)&(-30014,-60013)\\
2&(-7,-30005)&(-9,-29994)\\
3&(-30010,13)&(-29980,-12).
\end{array}                                             \tag{9}
\]

Put

\[
                          b=(5,7),\qquad v=(4,7).       \tag{10}
\]

Choose one point from every inner role to obtain `G`, and one from every
outer role to obtain `F`.  Exact orientation arithmetic gives, for every
one of the `16*16=256` pairs,

\[
\begin{array}{c|c}
\text{ordinary}&G,F,G+b,F+b,F+v,\{b,v\}\\
\text{bad}&G+F,F+b+v.
\end{array}                                             \tag{11}
\]

More strongly, every point of `G` is strictly inside `conv(F)`, while `v`
is strictly hidden in `F+b+v`.  All 18 ground points are in general
position.

The four Hall targets are

\[
 A_G=G+b,\quad C_F=F+b,\quad W_F=F+v,\quad Q=\{b,v\}.  \tag{12}
\]

They have respectively `16,16,16,1` distinct values, so the densest
complete-subrectangle load is

\[
        \max_{1\le a,c\le16}{ac\over a+2c+1}
                             ={256\over49}.             \tag{13}
\]

Choose the first inner and outer roles as the mark projection.  One mark
pair has 64 preimages.  On the ordered trace

\[
                 (G_0,G_1,G_2,G_3,F_0,F_1,F_2,F_3),   \tag{14}
\]

the lexicographically first minimum release always deletes positions
`(0,2,4)`.  Thus `tau=3`, every full released rank-five face has load 8,
and allowing all its nonempty downfaces raises the exact maximum load to
128.  There are two disjoint bad four-circuits.  Their union is the whole
trace; the canonical side tie selects the rank-four inner shield `G`,
whose exact load is 16.

Exhausting the whole 18-point ground set gives 6023 ordinary faces,
including the empty face, with rank vector

\[
                (1,18,153,816,1880,2008,966,177,4).     \tag{14a}
\]

Thus this finite gadget is safely high-face.  The value verifies the local
regression but says nothing by itself about the scalable arbitrary-child
recurrence.

This is precisely the simultaneous high-reuse behavior left by the
previous trace theorem.  Direct all context edges from the outer word to
the inner word, the side on which the canonical shield is stored.  The
graph is an acyclic complete bipartite graph.  Every repeated vertex has
degree 16, but all incident trace pairs have the same strict containment
order type.  Shrinking the role disks makes every query germ lie in an
arbitrarily small common projective chamber.

## 4. Quadratic-entropy scaling

The finite example is an open order-type cell.  Starting from one point
in each support in (8)--(9), replace the four outer vertices and four inner
vertices by sufficiently short strictly convex chains having respectively
`t` and `s` macro roles.  The inner chain polygon remains in the strict
interior of every outer polygon, while the two ear conditions involving
`b,v` remain strict.  Put `D` rational points, in general position and of
any prescribed rational order type after affine shrinking, into a tiny
disk at each role.

Every singleton transversal in either set of roles is ordinary, every
inner--outer full trace is bad, and (12) remains valid.  There are

\[
             M_G=D^s,\qquad M_F=D^t,\qquad H=D^{s+t}    \tag{15}
\]

actual records and

\[
              M_G+2M_F+1                              \tag{16}
\]

four-target outputs.  A fixed cross-role mark pair has load
`D^(s+t-2)`.  Deleting the whole inner trace is a rank-`s` release to the
outer face and has load `D^s`; the full inner face is a one-side shield
with load `D^t`.  Taking `s,t=Theta(log D)` makes (15)
`2^{Theta((log D)^2)}` while preserving one common containment chamber.
For `s=t`, the displayed release deletes exactly half the trace rank, so
it lies in the low-deletion regime of the trace theorem.  This paragraph
does not claim that it is the canonical *minimum* release at larger ranks;
only the exact finite product in Section 3 has that stronger audit.

Consequently neither high projection reuse, bad trace density, release
reuse, shield reuse, nor high graph degree forces several separated
directions.

<!-- Retracted 2026-08-15: the following attempted Section 5 used the false
strong-separation-to-endpoint-profile implication.  It is retained only in
source history and hidden from rendered output.

## 5. Retracted cyclic profile argument

The outer role system in Section 4 is strongly separated around one
convex macro polygon.  Let its role supports be `X_1,...,X_t`, each of
cardinality `D`, and put

\[
                         H_i=V(X_i)-1.                  \tag{17}
\]

For a generic direction at role `i`, every nonempty local face is the
union of its two boundary chains.  If their two profile counts are
`L_i,R_i`, then

\[
                         L_iR_i\ge H_i.                 \tag{18}
\]

Omit outer macro role `j`.  A right profile at `j-1`, a left profile at
`j+1`, and one arbitrary singleton in every other retained role form one
ordinary detached face.  This gives a load-one bank

\[
                         B_j=R_{j-1}L_{j+1}D^{t-3}.     \tag{19}
\]

Multiplying (19) cyclically and using (18) proves (1).  This is the exact
`CENTRAL_SHELL_PROFILE_RECURRENCE` theorem; it applies to arbitrary local
order types and does not use the inner contexts, `b`, or `v`.

Write `D=2^L`, `t=(alpha+o(1))L`, and suppose

\[
                  \log H_i\ge(c-o(1))L^2              \tag{20}
\]

uniformly.  Then

\[
                  \log\max_j B_j
                    \ge(alpha+c-o(1))L^2.              \tag{21}
\]

The established universal quarter input gives `c=1/4`.  Hence the
balanced quadratic product `s=t=(1/4+o(1))L` has

\[
          \log H=(1/2+o(1))L^2,qquad
          \log B_{\rm gap}\ge(1/2-o(1))L^2.            \tag{22}
\]

The one-chamber construction therefore pays at coefficient one half even
when every role contains a projectively universal low-face child.  Such a
child changes `L_i,R_i` but cannot make their product smaller than `H_i`.

As a record routing, the detached bank is reused by all inner contexts;
equations (19)--(22) are an **absolute ambient bank**, not a claim of low
record congestion.  Thus it settles the coefficient-scale nested-shell
regression but does not by itself prove the desired fixed-power Hall
expansion for arbitrary overlapping outer decompositions.

-->

## 5. Why the obvious cyclic profile payment is unavailable

Let the outer role supports in Section 4 be \(X_1,\ldots,X_t\), and put

\[
                         H_i=V(X_i)-1.                  \tag{17}
\]

For a generic local direction, every nonempty face of \(X_i\) is the union
of its two boundary chains.  If the abstract chain counts are \(L_i,R_i\),
then the **local** injection

\[
                         L_iR_i\ge H_i                  \tag{18}
\]

is valid.  The invalid step is to assert that, after omitting macro role
\(j\), every right chain at \(j-1\) and every left chain at \(j+1\) can be
completed by singleton choices from all other retained roles.  Those are
new determinants involving two or three points from one child, and the
singleton-transversal type does not control them.

The exact counterexample is the four-block system

\[
\begin{aligned}
 X_1&=\{P_1,\ldots,P_m\},&
 P_u&=\left(2-\delta u^2,-\frac15+\delta u\right),
 &\delta&={1\over100m^2},\\
 X_2&=\{(4,0)\},&X_3&=\{(0,4)\},&X_4&=\{(0,0)\}.
                                                               \tag{19}
\end{aligned}
\]

Every singleton transversal has one positive cyclic type, and all
\(2^m-1\) nonempty subsets of \(X_1\) are local faces.  Nevertheless, for
every \(i<j<k\),

\[
               P_j\in\operatorname{int}
                    \operatorname{conv}\{P_i,P_k,(0,4)\}.      \tag{20}
\]

Therefore either adjacent omitted-gap context permits only rank-one and
rank-two traces from \(X_1\).  Each ambient endpoint family has size at most

\[
                           S_m=m+{m\choose2}.            \tag{21}
\]

At \(m=14\),

\[
                    S_m^2=11025<16383=2^{14}-1.         \tag{22}
\]

Thus no ambient families satisfying the two required gap compatibilities
can obey \(L_1R_1\ge H_1\).  This directly refutes (1) under strong
separation.

For the literal singleton-transversal shell, the full outer bank still has
size \(D^t\) and load one.  For arbitrary multi-point children, the absolute
local banks \(H_i\) also remain.  What is missing is precisely their
multiplication through a common ambient gap.  A positive theorem needs a
stronger radial/lexicographic container hypothesis that controls the
multi-point seam determinants, or a different global Cauchy/circuit bank.

## 6. What canonical history decoding does and does not remove

For a canonical radial source, fixed `(A,e)` uniquely determines peel
depth and retained carrier.  Therefore multiple names for that same
state do not contribute geometric load.  Weighted history domination
likewise bounds genuine duplicate chronology weight.

The star in Section 3 survives this cleanup.  Fix one actual inner word
`G`, the actual source `A=G+b`, the endpoint pair, and any actual triangle
of `G`.  It is incident with all 16 distinct actual outer words `F`.
These records have different actual `C_F,W_F`, so they cannot be identified
as histories of one selected tuple.  In the scaled construction the
opposite-cloud degree is `D^t`.

Thus the canonical decoder changes the final residue from

\[
        \text{``many reset histories''}
        \quad\hbox{to}\quad
        \text{``many distinct opposite-cloud faces.''}              \tag{23}
\]

The latter is exactly what the Hall target bank and the cyclic profile
bank must pay.  A proposed triangle-overlap bound which uses only `(A,e)`
is false; a bound which also retains an actual opposite-cloud target may
be true.

## 7. Exact surviving positive statement

The cycle/DAG program becomes rigorous under the following two extra
interfaces.

1. **Cycle interface.**  Profile exports around every selected directed
   cycle must have joint 4-local closure, or an equivalent recoverable
   seam theorem.  Pairwise convexity is insufficient by Section 2.
2. **Star interface.**  The incident load in each quantitative projective
   chamber must be at most `M`.  Only a core degree exceeding `3M` forces
   four chamber-distinct queries to the same physical child.  A merely
   large actual degree is insufficient by Sections 3--4.

Strong separation of a high-degree cyclic shell does not supply the
alternative payment: Section 5 is the exact obstruction.  The unclosed
case is a high-overlap stationary chamber in which local face entropy is
systematically anti-aligned with every ambient omitted-gap seam.  This is
the heterogeneous cap/cup-ramp or decorated direction-spectrum state.

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_directed_profile_cycle_dag_audit.py
```

The checker exhausts all orientations of all simple graphs through five
vertices and all integer-weighted four-vertex core examples with edge
weights `0,1,2`.  It verifies the exact seven-point directed-cycle
obstruction and all 256 records of (8)--(12), including general position,
containment, the four targets, circuits, minimum releases, downface loads,
shield loads, and (13).  Its expected final line is

```text
PASS: dags=29853 weighted_cores=728 cycle_points=7; nested rows=16 cols=16 records=256 V=6023 hall=256/49 mark=64 release=8 downface=128 shield=16 full_outer=16
```
