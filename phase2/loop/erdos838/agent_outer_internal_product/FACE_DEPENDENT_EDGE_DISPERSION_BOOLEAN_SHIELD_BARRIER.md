# Face-dependent cage edges: an acyclic critical-dilution barrier

**Date:** 2026-08-15.  All logarithms are base two.  This continues
`THREE_CLOUD_COMMON_EDGE_DOMINANCE_TRICHOTOMY.md`.

## Verdict

Dispersion of the carrier edge does **not** by itself force a directed
cycle, a two-ended return module, or a good mixed face.  There is a
scalable rational planar construction with

* `M=2^h s^2` distinct carrier faces;
* `s^2` distinct physical exposed edges, every edge fibre having density
  exactly `1/s^2`;
* a directed physical-edge graph equal to the acyclic orientation
  `K_{s,s}` from a left endpoint class to a right endpoint class;
* one common child chamber and an arbitrary labelled child order type,
  partitioned into named clouds, whose whole union is a strict dominance
  chain over **every** carrier edge; and therefore
* zero good carrier-plus-cross-cloud-pair unions.

Taking `h=s` and carrier support `p=h+2s=3s` gives

\[
                 {1\over s^2}\le p^{-\theta_*},
 \qquad \theta_*=2-\log_2 3,                            \tag{1}
\]

for all large `s`.  Thus the proposed fixed-edge-fibre threshold is
strictly satisfied while the directed graph remains a DAG.

The construction exposes its own payment: all `h+2s` carrier labels lie
on one convex parabolic arc, so they supply a detached Boolean shield of
size

\[
                       2^{h+2s}.                         \tag{2}
\]

Relative to the selected carrier family, this is the multiplier

\[
                    {2^{h+2s}\over 2^h s^2}
                         ={2^{2s}\over s^2}.             \tag{3}
\]

Consequently the correct global alternative is not “edge dispersion
forces a cycle.”  It must be

> a low fixed-edge fibre either creates a mixed/return bank **or** the
> dispersed physical endpoints themselves carry a detached shield/profile
> bank.

This report is a sharp stretchable barrier to the first alternative alone.
It does not provide a low-face construction and does not close coefficient
one half.

## 1. The carrier alphabet and its exact decoder

Take the lower parabola

\[
                         \Gamma=\{(z,z^2-1):z\in\mathbb R\}.      \tag{4}
\]

Choose three ordered rational sets on it:

\[
 \begin{aligned}
 L&=\{\ell_1,\ldots,\ell_s\}\quad &&\text{in a tiny interval left of }(-1,0),\\
 C&=\{c_1,\ldots,c_h\}\quad &&\text{with }-1/2<c_x<1/2,\\
 R&=\{r_1,\ldots,r_s\}\quad &&\text{in a tiny interval right of }(1,0).
                                                               \tag{5}
 \end{aligned}
\]

Every subset of `L union C union R` is in convex position.  For

\[
        J\subseteq C,\qquad \ell\in L,\qquad r\in R,     \tag{6}
\]

put

\[
                         B(J,\ell,r)=J\cup\{\ell,r\}.    \tag{7}
\]

This is an ordinary face and `ell r` is its exposed closing edge: every
selected middle point lies strictly below the chord `ell r`, by strict
convexity of the parabola.  Hence there are exactly

\[
                         M=2^h s^2                       \tag{8}
\]

carrier contexts.  For a fixed physical edge `ell r`, precisely the
`2^h` choices of `J` use it.  Its fibre density is therefore exactly
`1/s^2`.

The physical decoder is literal.  From the labelled carrier face in (7),
intersection with the three fixed carrier classes recovers `J,ell,r`.
No edge-choice metadata is needed.

## 2. One universal child cage works for every dispersed edge

Let `Q={(a_i,b_i)}` be any finite rational general-position order type,
with any partition of its labels into named clouds.  After a generic
orientation-preserving affine preprocessing, assume the `a_i` are
distinct.  For sufficiently small positive rational `epsilon`, put

\[
 q_i=(\varepsilon a_i,
             1+3\varepsilon a_i+\varepsilon^2b_i).       \tag{9}
\]

Relative to the limiting edge from `u=(-1,0)` to `v=(1,0)`, the points
`q_i` lie in one ear cell and, in increasing `a_i` order, satisfy

\[
                    q_i\in\operatorname{int}
                        \operatorname{conv}\{u,v,q_j\}\qquad(i<j).\tag{10}
\]

All inequalities in (10) are strict.  After fixing the finite child,
choose the two endpoint intervals in (5) sufficiently small.  Openness of
strict orientation signs then upgrades (10) simultaneously to

\[
 q_i\in\operatorname{int}
       \operatorname{conv}\{\ell,r,q_j\}
 \quad\text{for every }\ell\in L, r\in R, i<j.         \tag{11}
\]

Rational choices avoiding the finitely many collinearity walls are dense,
so the whole configuration may be rational and in general position.

Equations (7) and (11) imply, for every carrier context,

\[
 \begin{aligned}
 B(J,\ell,r)\cup\{q_i\}&\text{ is convex},\\
 B(J,\ell,r)\cup\{q_i,q_j\}&\text{ is nonconvex}
                                           \qquad(i\ne j).       \tag{12}
 \end{aligned}
\]

The first line holds because `q_i` is a singleton insertion ear at the
closing edge.  The second holds because the inner child point in (11) is
hidden.  The affine map in (9) has positive determinant
`epsilon^3`, so every intrinsic child orientation sign and every named
child face bank is preserved.

For singleton outputs, the map

\[
              (J,\ell,r,i)\longmapsto
                    B(J,\ell,r)\cup\{q_i\}              \tag{13}
\]

has load one: physical class intersection recovers all four entries.
For two different named child clouds, every candidate obtained by adding
one label from each is bad.  This is genuine geometric incompatibility,
not decoder coalescence.

## 3. The directed edge/chamber graph is acyclic

Orient every used physical edge from its endpoint in `L` to its endpoint
in `R`.  The common child chamber lies above every such edge and the
carrier middle alphabet lies below it.  The directed physical-edge graph
is therefore exactly

\[
                            \vec K_{s,s}:L\longrightarrow R.      \tag{14}
\]

The order `L<R` is a topological ordering.  There is no directed cycle,
no directed path of length two, and no first-return chamber.  All edges
query the **same** child chamber, so chamber dispersion also vanishes.
The graph has many undirected four-cycles, but they do not produce a
two-ended cap/cup return: both edges at every such corner have the same
forward orientation and the same total dominance profile.

Thus a counting argument that turns many physical carrier edges into a
directed cycle is false even with fibre density `Theta(p^{-2})`, much
smaller than the critical `p^{-theta_*}`.

## 4. Why the barrier is paid

The full physical carrier support

\[
                            S=L\cup C\cup R              \tag{15}
\]

is itself a convex face of rank `h+2s`.  Hence all `2^{h+2s}` subsets of
`S` are ordinary, proving (2).  The mask of an output subset recovers it
with load one globally; this is not a per-edge spend of the same bank.

For `h=s`, the selected carrier contexts have logarithm `s+2log s`, while
the detached shield has logarithm `3s`.  The shield surplus `2s-O(log s)`
is exponentially larger than the polynomial three-cloud deficit.  Any
live counterexample resembling this DAG must therefore destroy the convex
endpoint shield while retaining its `s^2` dispersed exposed edges and the
common child chamber.  That is precisely the extra planar/profile input
not encoded by fibre density.

## 5. Verification

`verify_face_dependent_edge_dispersion_barrier.py` uses exact rational
arithmetic for `s=3,h=5` and a seven-label two-cloud child.  It verifies:

1. general position of all 18 points;
2. every carrier face, its exposed closing edge, and the exact `1/s^2`
   fibre density;
3. load-one singleton outputs;
4. singleton compatibility and pair incompatibility for every carrier
   context and every cross-child pair;
5. acyclicity of the directed `K_{s,s}`; and
6. all `2^{h+2s}` detached carrier subsets.
