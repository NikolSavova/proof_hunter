# Dense Hall cores do not align two independent cloud profiles

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The surviving dense old-source by released-face Hall core does **not**, by
itself, force a cross-column fan/cap--cup bank at the
`n^(Theta(log log n))` scale.  There is an exact scalable planar regression
which simultaneously has:

1. a complete `m` by `m` source--release incidence rectangle;
2. a fixed common-cage or fixed-root fan `1+3` signature in every column;
3. all five ordinary decoder targets `W,Q,C,A,E`;
4. unit ordered-pair decoder load for `(A,C)` and `(E,W)`; and
5. independently arbitrary rational order types in the row and column
   clouds.

After the two clouds are placed in their open cage cells, their ordinary
cross-cloud traces satisfy the exact two-block recurrence

\[
 V(Y\cup Z)=V(Y)+V(Z)+R(Y)A(Z),                         \tag{1}
\]

where `R(Y)` and `A(Z)` are the two directional profiles facing the other
cloud.  The common-cage signatures impose no relation between these two
profiles.  In particular, take opposite pure parabolic chains of size `m`
and orient them so that both facing profiles contain only singletons and
pairs.  With

\[
                 T_m=2^m-1,\qquad
                 S_m=m+{m\choose2},                    \tag{2}
\]

the two clouds have `V(Y)=V(Z)=T_m`, but

\[
                R(Y)A(Z)=S_m^2=\Theta(m^4).             \tag{3}
\]

Thus no fixed positive power of `V(Y)V(Z)`, and in particular no
quasipolynomial scale-recovery multiplier, follows from Hall density plus
the per-column cage/fan signature.  Since convexity is hereditary, adding
any subset of the fixed five anchors cannot repair a nonconvex cloud trace;
there are at most `2^5 S_m^2` anchor-decorated faces meeting both clouds.

This is an applicability barrier, not a low-face construction.  The two
internal banks `V(Y),V(Z)` remain and may pay in a particular global
argument.  A positive theorem must use their profile energy through a
third/cyclic role, correlate the two child charts by actual chronology, or
route to an internal bank by Cauchy.  Two-cloud density and circuit
signatures alone cannot provide the alignment.

## 1. Universal cage rectangle with five decoded targets

Let

\[
 B=\{l=(-3,0),r=(3,0),t=(0,5)\},\qquad
 v=(-2,-1),\quad u=(2,-1).                              \tag{4}
\]

There are disjoint open disks `U_G` around

\[
                       g_0=(1/100,50099/10000)           \tag{5}
\]

and `U_X` around `x_0=(0,-4)` such that, for every `g in U_G` and
`x in U_X`, all of

\[
 B\cup\{g\},\quad B\cup\{g,v,u\},\quad B\cup\{x\},
 \quad B\cup\{v\},\quad \{x,v\}                        \tag{6}
\]

are ordinary, while `B union {g,x,v}` is nonconvex.  These are finitely
many strict orientation conditions at `(g_0,x_0)`, so sufficiently small
disks preserve them.

Choose distinct clouds `G={g_1,...,g_m} subset U_G` and
`X={x_1,...,x_m} subset U_X`.  Record `(i,j)` has the five targets

\[
\begin{aligned}
 W_j&=\{x_j,v\},                 &Q&=B\cup\{v\},\\
 C_j&=B\cup\{x_j\},             &A_i&=B\cup\{g_i\},\\
 E_i&=B\cup\{g_i,v,u\}.&&
\end{aligned}                                                   \tag{7}
\]

Every target is ordinary.  Moreover

\[
                 v\in\operatorname{int}\triangle(l,x_j,r),      \tag{8}
\]

so `{l,x_j,r,v}` is one common-cage signed circuit for the whole `j`th
column, independent of `i`.  The pair `(A_i,C_j)` recovers `B,g_i,x_j`,
and `(E_i,W_j)` recovers the same row and column together with `u,v`.
Thus both ordered-pair loads are one for canonical unit records.

For any record subfamily using `a` rows and `c` columns, its size is at
most `ac`, while the actual target union has at least

\[
                              2a+2c+1                         \tag{9}
\]

members: `A_i,E_i` for every row, `W_j,C_j` for every column, and `Q`.
The ratio `ac/(2a+2c+1)` is increasing in both variables.  Therefore the
exact five-target fractional Hall load of the complete rectangle is

\[
                              \lambda_5={m^2\over4m+1}.       \tag{10}
\]

This preserves, and slightly strengthens, the `W,Q,C,A` core.  Omitting
`E` recovers the known value `m^2/(3m+1)`.

### 1.1 The same regression in the pocket-label-hidden fan class

The endpoint-hidden cage is not essential.  Keep `B,g_0` as above and put

\[
 v^*=(1/10,-4),\qquad u^*=(2,-3),\qquad x_0^*=(-2,-1).   \tag{10a}
\]

At the central configuration,

\[
 x_0^*={1\over4}v^*+{57\over80}l+{3\over80}r.           \tag{10b}
\]

Thus the **pocket label** is hidden by a triangle containing the endpoint,
which is exactly the rooted-fan signed class.  Nevertheless

\[
 B\cup\{g_0\},\quad B\cup\{g_0,v^*,u^*\},\quad
 B\cup\{x_0^*\},\quad B\cup\{v^*\},\quad\{x_0^*,v^*\} \tag{10c}
\]

are all ordinary.  Again the assertions are strict, so small independent
clouds around `g_0,x_0^*` retain them.  The five targets (7), the Hall value
(10), arbitrary-order-type substitution, and recurrence (1) are unchanged.
Hence neither of the two signed `1+3` geometries forces profile alignment.

## 2. Independent order types and the exact two-cloud recurrence

Let `Y,Z` be arbitrary rational general-position configurations, each with
`m` labelled points.  Rotate their affine charts so their first coordinates
are distinct.  For sufficiently small positive rational `epsilon`, embed

\[
 (a,b)\in Y\longmapsto g_0+(\epsilon a,\epsilon^2b),
 \qquad
 (c,d)\in Z\longmapsto x_0+(\epsilon c,\epsilon^2d).       \tag{11}
\]

Positive affine maps preserve the two prescribed order types.  The first
order horizontal displacement and second order vertical displacement make
every mixed triple sign the standard two-block lexicographic sign.  Taking
`epsilon` smaller if necessary keeps both images inside the open cage
disks and avoids all cross-cloud/anchor collinearities.

For a nonempty face `S subset Y`, call it a **right profile** if adjoining
one arbitrary singleton from the `Z` block remains convex; define left
profiles of `Z` symmetrically.  Let their counts be `R(Y),A(Z)`.  Classify
an ordinary subset meeting both blocks by its first and last occupied
block.  Its `Y` trace must be a right profile and its `Z` trace a left
profile.  Conversely every such pair is ordinary by the lexicographic
mixed-triple signs.  The two labelled traces recover the choices, proving
(1) exactly.

Consequently the complete Hall rectangle and its column signatures coexist
with independently arbitrary child face and cap/cup profiles.  Planarity
adds the two-block recurrence, but no cross-child alignment inequality.

## 3. Scalable anti-aligned profile regression

Take the two child order types to be pure parabolic chains

\[
                         P_m^\pm=\{(s,\pm s^2):1\le s\le m\}.       \tag{12}
\]

Every nonempty subset of either chain is in convex position, so its
ordinary-face count is `T_m`.  In the composition chart, one directional
profile of a pure chain consists of all nonempty subsets, while the
opposite profile consists exactly of ranks one and two and has size `S_m`.
The two clouds can be reflected independently without changing their
order types or any cage sign involving only one label from a cloud.

Choose the guard curvature so its facing right profile is small and the
pocket curvature so its facing left profile is small.  Equation (1) becomes

\[
                    V(G\cup X)=2T_m+S_m^2,              \tag{13}
\]

and the number of faces with a nonempty trace in both clouds is exactly
`S_m^2`.  The four independent curvature choices realize the table

\[
\begin{array}{c|cc}
 &\text{pocket small}&\text{pocket large}\\ \hline
\text{guard small}&S_m^2&S_mT_m\\
\text{guard large}&T_mS_m&T_m^2.
\end{array}                                             \tag{14}
\]

Thus the same dense Hall/cage data are compatible with the full range from
polynomial to doubly exponential-in-rank cross-profile output.  A theorem
which sees only the rectangle and signed circuits cannot distinguish the
four cases.

Finally, let `K` be the five fixed anchors `B union {u,v}`.  If an ordinary
face `H subset G union X union K` meets both clouds, then its cloud trace
`H cap (G union X)` is ordinary by heredity.  Hence

\[
 \#\{H:H\cap G\ne\varnothing,\ H\cap X\ne\varnothing\}
          \le 2^{|K|}S_m^2=32S_m^2                       \tag{15}
\]

in the anti-aligned realization.  This rules out an alternative bounded-
anchor repair of the missing profile product while retaining both row and
column cloud traces.

## 4. Exact scope of the barrier

The regression kills the implication

\[
 \text{dense }A\times C\text{ Hall core + common signed cages}
 \quad\Longrightarrow\quad
 \text{large recoverable two-cloud composition bank}.             \tag{16}
\]

It does not kill three possible additional inputs:

1. a cyclic family of at least three compatible profile cuts, where the
   endpoint-product telescope prevents anti-alignment;
2. a weighted Cauchy route to the internal banks `V(Y),V(Z)` with globally
   summable overlap; or
3. a chronology constraint forcing the guard and pocket reflections to be
   correlated.

Those are exactly the extra invariants needed beyond `W,Q,C,A,E` and the
per-column circuit signature.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_dense_hall_two_cloud_profile_barrier.py
```

The checker uses exact rational arithmetic.  It verifies all common-cage
and rooted-fan decoder targets, exhausts the five-target Hall value for small rectangles,
checks the closed formula through size 100, realizes two independent
nonconvex four-point order types with the exact recurrence `11*13=143`,
and exhausts every subset of the four parabolic orientation pairs through
cloud size seven, obtaining exactly `S^2,ST,TS,T^2`.
