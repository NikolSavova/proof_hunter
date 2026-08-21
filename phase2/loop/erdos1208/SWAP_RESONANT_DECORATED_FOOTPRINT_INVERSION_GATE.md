# Decorated inversion of the three resonant footprints

## 1. Outcome

The quadratic footprints in
`SWAP_RESONANT_LINE_FOOTPRINT_PACKING_GATE.md` were previously charged only
through their maximum undecorated depth in `D+D`.  This note identifies the
exact information hidden by that maximum.  A footprint incidence becomes
one-to-one after retaining

1. the physical difference `d=t_1-t_2`, and
2. one natural completion vertex.

The decoration is not artificial.  In all three resonances, `(d,kappa)`
also determines a second completion vertex in the literal reservoir

\[
 \mathcal V_K=\{(r,A,B):r\in\mathcal P_K,
                  A,A+r,B,B+Jr\in D\}.             \tag{1.1}
\]

Thus high off-diagonal resonant footprint depth is exactly reuse of endpoint-labelled
edges between completion vertices.  There is no remaining local footprint
multiplicity.

Use the reverse-record notation

\[
 q=c-X,\qquad p=q+t,\qquad
 Y=\ell+Jp,\qquad W=\ell+Lt,\qquad Z=W+Jq=Y+t,
                                                        \tag{1.2}
\]

where `L=I+J`.  Fix the recursive shift `u` and one oriented physical
endpoint role throughout.  For an ordered footprint representation
`(t_1,t_2)`, put `d=t_1-t_2`.  The diagonal `d=0` must be separated:
one star of size `h` has at most `h` footprint points arising only from
diagonal pairs.  Since the full footprint has size at least `h^2/2`, the
set `Phi^ne` of points admitting a representation with `t_1 ne t_2`
satisfies

\[
 |\Phi^\ne|\ge |\Phi|-h\ge h^2/2-h,               \tag{1.2a}
\]

and in particular `|Phi^ne|>=h^2/4` for `h>=4`.  All completion-edge
statements below concern this off-diagonal support.  The discarded
diagonal incidence mass is linear in the star sizes and belongs to the
already-separated low/matching charge.

The three inversion keys are

\[
\begin{array}{c|c|c}
\text{fixed coordinate}&z&\kappa\\ \hline
q&Y_1+Z_2&(p_1,X,\ell)\\
p&X_1+Z_2&(p,X_1,\ell)\\
Z&X_1+Y_2&(q_1,X_1,W_1).
\end{array}                                          \tag{1.3}
\]

For each row, the map

\[
 (\text{star},z,\text{chosen ordered representation})
 \longmapsto (u,\text{role},z,d,\kappa)              \tag{1.4}
\]

is injective.  If a point of `Phi^ne` has several ordered non-diagonal
representations, choosing the lexicographically first one therefore gives
an injective map on the *off-diagonal footprint incidences* themselves.

Consequently, for fixed `(u,role,z)` the footprint depth is the number of
edges in a simple bipartite graph

\[
 G_{u,\mathrm{role},z}
 \subset \{\text{physical differences }d\}
          \times\mathcal V_K.                       \tag{1.5}
\]

The remaining global theorem can now be stated without a vague depth
parameter: pack these simple, endpoint-realizable completion-edge graphs.
A matching-like graph is diffuse in both physical differences and
completion vertices; any failure of that diffuse charge has a genuine
high-degree completion core.  Abstract graph theory is still insufficient,
but the exact geometric object to which it must be applied is now fixed.

There is an immediate corrected aggregate consequence.  In a band
`lambda_g<2L`, let all active stars have `H<=h_sigma<2H` with `H>=4`, and
let `Delta^ne` be the maximum depth of their off-diagonal footprints.  Then

\[
\boxed{
 \sum_\sigma\lambda_{g(\sigma)}h_\sigma
 \le {8L\Delta^\ne|D+D|\over H}.}                \tag{1.6}
\]

Indeed (1.2a) gives `sum h_sigma^2<=4 Delta^ne|D+D|`, while
`sum h_sigma<=H^{-1}sum h_sigma^2`.  This is the valid successor to the
earlier maximum-depth charge: high depth coming only from diagonal
representations can no longer create a false obstruction.  Stars of size
at most three remain in the explicitly matching-heavy metric branch.

## 2. Fixed `q`: the `JT+LT` footprint

Fix `q`, hence `X=c-q`.  For an ordered pair `(t_1,t_2)`, set

\[
 z=Y_1+Z_2,\qquad d=t_1-t_2,
 \qquad \kappa=(p_1,X,\ell),\quad p_1=q+t_1.       \tag{2.1}
\]

The first component of the footprint is already encoded by the corner:

\[
 Y_1=\ell+Jp_1.                                    \tag{2.2}
\]

Since

\[
 Z_2=\ell+Jp_1+t_1-Ld,                             \tag{2.3}
\]

the inverse is

\[
\boxed{
 t_1=z-2(\ell+Jp_1)+Ld,\quad
 t_2=t_1-d,\quad q=p_1-t_1,\quad c=X+q.}           \tag{2.4}
\]

The centre invariant `H`, all six `D` vectors, and the physical neighbour
labels then follow from (1.2).  The oriented role selects the physical
endpoint uniquely by directed-vector Sidonicity.

The same data determine the companion completion vertex

\[
 \boxed{\kappa'=(p_1-d,X,\ell)\in\mathcal V_K.}     \tag{2.5}
\]

Thus a decorated fixed-`q` footprint is an edge between two completion
vertices with the same `(X,ell)` coordinates.

## 3. Fixed `p`: the `T+T` footprint

Now `p` and

\[
 Y=\ell+Jp                                             \tag{3.1}
\]

are fixed.  Put

\[
 z=X_1+Z_2,\qquad d=t_1-t_2,
 \qquad \kappa=(p,X_1,\ell).                       \tag{3.2}
\]

Then

\[
\boxed{
 t_2=z-X_1-\ell-Jp,\quad
 t_1=t_2+d,\quad q_1=p-t_1,\quad c=X_1+q_1.}       \tag{3.3}
\]

The companion completion vertex is

\[
 \boxed{\kappa'=(p,X_1-d,\ell)\in\mathcal V_K.}    \tag{3.4}
\]

This time the edge has fixed popular coordinate and moves the first
completion start by `d`.

## 4. Fixed `Z`: the corrected `(I-J)T-T` footprint

For the third resonance the natural corner is on the `q` side.  Put

\[
 z=X_1+Y_2,\qquad d=t_1-t_2,
 \qquad \kappa=(q_1,X_1,W_1).                     \tag{4.1}
\]

The fixed coordinate is visible directly from the corner:

\[
 Z=W_1+Jq_1.                                      \tag{4.2}
\]

Hence

\[
\boxed{
 t_2=Z-z+X_1,\quad t_1=t_2+d,\quad
 c=X_1+q_1,\quad \ell=W_1-Lt_1.}                 \tag{4.3}
\]

The companion corner is

\[
\boxed{
 \kappa'=\bigl(q_1+(I-J)d,\ X_1-(I-J)d,\ W_1-Ld\bigr)
 \in\mathcal V_K.}                                \tag{4.4}
\]

Indeed fixed `Z` gives

\[
 X_1-X_2=(I-J)d,\qquad
 q_2-q_1=(I-J)d,\qquad W_1-W_2=Ld.                \tag{4.5}
\]

This is the completion-space repair of the genuine Costas-23 constant-`Z`
barrier.

## 5. Exact depth graph and the next dichotomy

For every star `sigma` and every `z in Phi_sigma`, choose one ordered
representation canonically and form `(d,kappa)` by the appropriate row of
(1.3).  Sections 2--4 prove that two incidences with the same
`(u,role,z,d,kappa)` coincide.  Therefore the images for fixed
`(u,role,z)` are the edges of a simple bipartite graph (1.5), and

\[
 \boxed{\Delta_{u,\mathrm{role}}(z)
       =|E(G_{u,\mathrm{role},z})|.}              \tag{5.1}
\]

Every edge additionally carries the deterministic companion map

\[
\begin{aligned}
 T_q^d(p,X,\ell)&=(p-d,X,\ell),\\
 T_p^d(p,X,\ell)&=(p,X-d,\ell),\\
 T_Z^d(q,X,W)&=(q+(I-J)d,X-(I-J)d,W-Ld).          \tag{5.2}
\end{aligned}
\]

Thus it is not merely an edge of an abstract bipartite graph: both of its
completion endpoints lie in `mathcal V_K`, and the endpoint role recovers
one physical three-point star in `A`.

For thresholds `R,S`, iterative deletion gives the exact alternative:

* at most `R|D_*|+S|V_*|` edges are removed while a physical-difference
  vertex has degree below `R` or a completion vertex has degree below `S`;
* if edges remain, the surviving labelled graph has minimum degrees at
  least `R` and `S` on its two sides.

Here `D_*` and `V_*` are the active vertex sets of the particular depth
graph.  This is deliberately a structural statement, not yet a target-scale
bound.  It isolates the only genuine survivor: a simultaneously rich
physical-difference/completion-edge core.  A matching-heavy footprint is
now diffuse in a literal endpoint reservoir and should be charged globally;
a nonmatching footprint has the dense common completion structure required
for the next density increment.

## 6. Verification and scope

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_resonant_decorated_footprint_inversion.py
```

The verifier exhausts the three inverse maps on finite integer boxes,
checks all companion-corner transformations, verifies the off-diagonal
support and aggregate inequalities and the bipartite pruning identity, and
reconstructs the genuine constant-`Z` Costas-23 row.

The exact stored residual profiles sharply distinguish diagonal from
off-diagonal depth.  For transformed Costas primes `29,31,37`, respectively,
the pairs

\[
 (\text{off-diagonal incidences},\text{diagonal-only incidences})
 =(158,9426),(52,7038),(88,6960),                 \tag{6.1}
\]

have maximum off-diagonal depths `2,1,1`; decorated load and completion-edge
reuse are one in all three rows.  These values are stress evidence, not a
uniform bounded-depth claim.  The theorem above is the exact reason the
large diagonal counts are harmless.

This theorem removes the *local* depth ambiguity.  It does not yet bound
the total number of simple decorated completion edges.  The next proof must
sum the diffuse edges from their endpoint labels and show that any excess
minimum-degree core creates a forbidden equal-distance pair.  Replacing the
new graph by its unlabelled degree sequence would return to the already-dead
one-factorization model.
