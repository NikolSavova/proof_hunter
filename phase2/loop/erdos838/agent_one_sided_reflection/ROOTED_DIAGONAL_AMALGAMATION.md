# Rooted diagonal amalgamation: the exact two-tangent higher-history bank

## Verdict

The higher histories above a fixed two-point trace admit an exact planar
classification.  A rooted face on either side of the trace is completely
summarized, for purposes of gluing, by its two tangent neighbours at the
trace endpoints.  Two such side faces glue to a convex face if and only if
one tangent pair passes the left endpoint and the other passes the right
endpoint.  These are two independent dominance inequalities.

Moreover, summing the resulting local banks over **all** traces has
rank-`k` overlap at most `k-1`.  Thus the global reuse problem for these
banks is solved with polynomial, indeed linear, load.  At rank four the
sum is exactly the previously extracted mass

\[
                         T=\sum_{i<k}r_{ik}s_{ik}.          \tag{1}
\]

What remains is a local quantitative theorem forcing the two-tangent
profile contraction to grow beyond its singleton layer, or else charging
one of the detached side complexes.  The single-grid universality barrier
does not defeat the present theorem: arbitrary side order types are allowed,
but every compatible higher side-face pair is now counted, with globally
bounded overlap.

The exact verifier is

```text
python3 phase2/loop/erdos838/agent_one_sided_reflection/verify_rooted_diagonal_amalgamation.py
```

It exhausts all rooted side-face pairs in many rational configurations,
checks the two tangent inequalities against direct convex-hull computation,
and verifies the rankwise global overlap identity.

## 1. Rooted side faces

Fix labels `j<l` and direct the trace segment from `j` to `l`.  Let

\[
 L^\sigma=\{x<j:\chi(j,l,x)=\sigma\},\qquad
 R^{-\sigma}=\{y>l:\chi(j,l,y)=-\sigma\}.                \tag{2}
\]

A **left rooted side face** is a nonempty `X subset L^sigma` such that

\[
                         X\cup\{j,l\}                     \tag{3}
\]

is in convex position.  The segment `jl` is then a hull edge of (3), since
all points of `X` lie strictly on one side of its line.  On the other
boundary path from `j` to `l`, let

\[
 \tau_j(X),\tau_l(X)\in X                                 \tag{4}
\]

be the vertices adjacent to `j` and `l`.  They may coincide when `|X|=1`.
Define rooted right side faces `Y subset R^(-sigma)` and their two tangents
in the same way.

The word “face” in (3) is unrestricted: `X` need not be a pure cup or cap.
This is essential.  The tangent pair is the exact amount of its internal
order type visible to the opposite side.

## 2. Two-tangent amalgamation

Apply an orientation-preserving affine change taking

\[
                         j=(0,0),\qquad l=(1,0).           \tag{5}
\]

The labels retain their original x-order; no assertion about the first
coordinate after this normalization is needed.  For points `x,y` on
opposite sides of the root line, let `t(x,y)` be the coordinate at which
the line segment `xy` meets that line:

\[
 x+s(y-x)=j+t(x,y)(l-j).                                  \tag{6}
\]

The following is the exact higher-history theorem.

> **Theorem 1 (two-tangent amalgamation).**  Let `X` and `Y` be rooted side
> faces on opposite sides of `jl`.  Put
> \[
> x_j=\tau_j(X),\quad x_l=\tau_l(X),\qquad
> y_j=\tau_j(Y),\quad y_l=\tau_l(Y).
> \]
> Then
> \[
> \boxed{
> X\cup\{j,l\}\cup Y\text{ is convex}
> \iff t(x_j,y_j)>0\ \text{ and }\ t(x_l,y_l)<1.}          \tag{7}
> \]

**Proof.**  The convex polygons

\[
 A=\operatorname{conv}(X\cup\{j,l\}),\qquad
 B=\operatorname{conv}(Y\cup\{j,l\})                    \tag{8}
\]

lie in opposite closed halfplanes and share the hull edge `jl`.  Delete
that edge from the boundary of each polygon and concatenate the two
remaining boundary paths.  Every turn of the resulting simple polygon is
already convex except possibly the turns at `j` and `l`.

At `j`, the two incident non-root edges go to `x_j` and `y_j`.  Their turn
is convex exactly when their intersection with the root line lies strictly
to the right of `j`, which is `t(x_j,y_j)>0`.  Similarly the turn at `l` is
convex exactly when the line through `x_l,y_l` meets the root line strictly
to the left of `l`, namely `t(x_l,y_l)<1`.  If both inequalities hold, the
concatenated boundary is a strictly convex polygon containing every vertex
of `A` and `B`; if either fails, the corresponding root is a reflex turn.
This proves (7).  \(\square\)

The theorem is stronger than checking every cross quadrilateral.  Only two
tangent pairs are tested.  Once (7) holds, deletion from the glued convex
face implies automatically that **every** `{x,j,l,y}` with `x in X,y in Y`
is convex.

## 3. Dominance coordinates and the profile contraction

Suppose for definiteness that `x` is above and `y` below the horizontal
root line.  Put

\[
 \alpha_x={-x_x\over y_x},\quad
 \beta_x={1-x_x\over y_x},\qquad
 A_y={x_y\over-y_y},\quad
 B_y={x_y-1\over-y_y}.                                   \tag{9}
\]

Direct solution of (6) gives

\[
 t(x,y)>0\iff A_y>\alpha_x,qquad
 t(x,y)<1\iff B_y<\beta_x.                               \tag{10}
\]

Thus (7) consists of one dominance comparison at each endpoint:

\[
 A_{y_j}>\alpha_{x_j},qquad B_{y_l}<\beta_{x_l}.          \tag{11}
\]

This gives an exact matrix form.  Let
`M^sigma_(p,q)(z)` be the generating polynomial of left rooted side faces
with tangent pair `(p,q)`, weighted by `z^|X|`; define
`N^(-sigma)_(r,s)(z)` on the right.  The local glued-face polynomial is

\[
\boxed{
 H_{jl}^{\sigma}(z)=z^2
 \sum_{p,q,r,s}
 M^\sigma_{p,q}(z)N^{-\sigma}_{r,s}(z)
 \mathbf1[t(p,r)>0]\mathbf1[t(q,s)<1].}                  \tag{12}
\]

Sum (12) over the two choices of `sigma`.  The decoder is exact: from a
glued face and the marked trace `jl`, its left and right traces, and hence
their tangent states, are recovered uniquely.

Formula (12) is the promised two-ended cap/cup bank in its correct general
form.  Pure rooted cap and cup histories occupy triangular submatrices of
`M,N`; arbitrary internal convex histories are retained rather than erased.

## 4. Global overlap is only the rank

Let `v_k(P)` be the number of rank-`k` convex faces.  A glued face counted
by (12) contains no selected label strictly between `j` and `l`; hence
`j,l` are consecutive in its x-order.  Conversely, take a convex face `Q`
and two consecutive selected vertices `j<l`.  If `jl` is a diagonal of
`Q`, all earlier selected vertices lie on one side of its line and all later
ones on the other.  The two resulting side polygons are rooted side faces,
and Theorem 1 reconstructs `Q`.

For completeness, the separation assertion is just x-monotonicity of a
convex polygon.  Its upper and lower boundary chains are both monotone in
the original x-coordinate.  Two consecutive vertices in the combined
x-order which lie on the same chain are adjacent on that chain, so their
segment is a hull edge.  If their segment is a diagonal, they therefore lie
on different chains; the earlier vertices and later vertices occupy the two
opposite arcs cut out by the diagonal, and hence its two open halfplanes.

Therefore the multiplicity with which `Q` occurs in the sum of all local
banks is exactly the number of its consecutive-x pairs which are diagonals.
It is at most `|Q|-1`.  Rank by rank,

\[
 \boxed{
 \sum_{j<l,\sigma}[z^k]H_{jl}^{\sigma}(z)
 \le (k-1)v_k(P).}                                       \tag{13}
\]

Equivalently, the union of every local two-tangent bank has decoder load at
most `k-1` on rank `k`.  At the live ranks `k=Theta(log n)`, this loss is
only polynomial.

For `k=4`, a represented face has the form `{i,j,l,k}` with `ik,jl` its
two diagonals, and it has exactly one eligible trace.  Hence

\[
 \boxed{
 \sum_{j<l,\sigma}[z^4]H_{jl}^{\sigma}(z)
 =T=\sum_{i<k}r_{ik}s_{ik}.}                              \tag{14}
\]

This recovers the dense rank-four extraction as the singleton layer of the
full higher-history bank.

## 5. The exact remaining inequality

Equations (12)--(14) eliminate global face reuse for the rooted-diagonal
lane.  A sufficient next theorem can now be stated without ambiguity:

> For the trace profiles generated by one unit reflection order, either the
> total contraction in (12), at ranks `Theta(log n)`, gains a fixed power
> over its singleton/rank-four demand, or one of the omitted rooted side
> complexes supplies an ordinary face bank of the same fixed-power gain
> with bounded aggregate trace load.

The first alternative pays globally by (13).  The second still needs a
trace-selection or ancestor telescope: the single complete-grid
universality construction shows that a detached side complex can have an
arbitrary order type, and the same detached face may be offered to many
root traces.  What is no longer open is compatibility or mixed-face
overlap: both are exactly resolved by the two tangent guards in (11).

This also identifies the scalable regression which every proposed local
inequality must survive.  In the central Pascal cells the tangent-profile
matrices are strongly anti-aligned; the forward contraction (12) is the
oriented cap--cup product which attains coefficient one half.  Replacing
`M,N` by their scalar totals or by unrestricted detached face counts loses
precisely the two endpoint comparisons and is invalid.

## 6. A scalable matching-star regression

There is an exact obstruction even stronger than a single universal
complete grid.  For every `m,q>=1` there is a rational general-position
configuration, in four consecutive x-blocks

\[
 X=(x_1,\ldots,x_m)<J=(j_1,\ldots,j_q)
 <L=(l_1,\ldots,l_q)<Y=(y_1,\ldots,y_m),                \tag{15}
\]

such that **every one of the `q^2` root traces** `j_a l_b` has the same
mixed-extension graph

\[
 \{x_i,j_a,l_b,y_k\}\text{ is a mixed convex quadrilateral}
 \iff i+k=m+1.                                          \tag{16}
\]

Thus each trace has `m` extensions, the total repeated-star mass is
`q^2m`, but the graph on the two outer clouds is a perfect matching.  No
glued face using those clouds can have more than one vertex on either side:
deletion from such a face would make every pair in \(X'\times Y'\) an edge
of (16), whereas a matching contains no nontrivial complete bipartite
graph.  Consequently the outer-cloud part of (12) is supported only at
rank four, despite arbitrarily many identical trace stars.

Here is a robust realization.  Before a generic rational perturbation put

\[
 x_i=(-2,i),\qquad y_k=(2,k-m-1),                         \tag{17}
\]

and put all `j_a` near `(-delta,c)` and all `l_b` near
`(delta,c)`, where `delta=1/(100m)` and `c=delta/4`.  At the
unperturbed root segment, the line `x_i y_k` has height
`(i+k-m-1)/2` at abscissa zero.  If `i+k=m+1`, it meets the horizontal
root segment transversally at abscissa `-2c/i`, strictly between
`-delta` and `delta`.  Otherwise its central height has absolute value at
least `1/2`, and throughout the root window it stays separated from the
root segment.  These are finitely many strict open conditions.  A small
rational perturbation can therefore split all coincident block
x-coordinates, put the whole set in general position, and preserve exactly
(16).

This is not a counterexample to (12)--(13): it is a sharp regression against
trying to bootstrap `T` from singleton compatibility alone.  Any successful
coefficient-half argument must exploit the other labels in the rooted side
profiles, or charge their ordinary face complexes with an aggregate
telescope.  The trace mass by itself admits no higher-rank continuation.
