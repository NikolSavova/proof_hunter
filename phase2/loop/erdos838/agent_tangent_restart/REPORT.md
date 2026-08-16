# Dynamic two-tangent restart for Erdős 838

**Date:** 2026-08-14  
**Verdict:** the unrestricted lower bound is not closed here.  This lane does
prove two all-orders extensions of the circuit-localized geometry and an exact
binary recursion for a single tangent cone.  Together they remove the alleged
`r log r` cost of updating the middle tangent: selected tangent histories are
canonically recoverable.  The remaining obstruction is more specific.  A
binary recursion may exclude arbitrarily many outer alternatives before it
selects a pivot, and those excluded points must be paid for by a bivariate
rooted/unrooted potential.  The scalar onion-layer potential proposed during
this attack is false on an exact 63-point configuration.

Throughout, `P` is in planar general position, `A=(a_0,...,a_(r-1))` is a
counterclockwise convex polygon, and every edge is oriented with `A` in its
left half-plane.  Let

\[
 R_i(A)=\{q\notin A:q\text{ violates precisely the support inequality of }
 a_i a_{i+1}\}.
\]

These are the edge pockets of the points individually addable to `A`.

## 1. A whole pocket is exactly a two-rooted chain problem

For `Q subset R_i(A)`, put `e_i={a_i,a_(i+1)}`.

> **Lemma 1 (two-root reduction).**
> \[
>  A\cup Q\text{ is convex}\quad\Longleftrightarrow\quad
>  e_i\cup Q\text{ is convex}.                                  \tag{1}
> \]

**Proof.**  Every point of `Q` is beyond the line of `e_i` and lies in all
the other support half-planes of `A`.  Thus the old boundary path from
`a_(i+1)` to `a_i` which avoids `e_i` remains on the boundary of
`conv(A union Q)`.  The complementary boundary path is exactly the outer
path from `a_i` to `a_(i+1)` in `conv(e_i union Q)`.  All old vertices are
therefore extreme, and all points of `Q` are extreme in the first hull if
and only if they are extreme in the second. `square`

Define the nonempty rooted-chain polynomial

\[
 L_i^A(z)=\sum_{\substack{\varnothing\ne Q\subseteq R_i(A)\\
                    e_i\cup Q\text{ convex}}}z^{|Q|}.             \tag{2}
\]

The identity (1) is useful because the point set inside one cone can have an
arbitrary order type, but it enters the state only through two fixed tangent
roots.

## 2. All-orders compatibility on a matching of edge pockets

Pair locality from the circuit-hardcore lane extends from single points to
arbitrary rooted chains.

> **Theorem 2 (matching-pocket compatibility).**  Let
> `I subset Z/rZ` contain no two equal or cyclically adjacent indices.  For
> each `i in I`, choose `Q_i subset R_i(A)` so that `A union Q_i` is convex.
> Then
> \[
>  A\cup\bigcup_{i\in I}Q_i\text{ is convex}.                    \tag{3}
> \]

**Proof.**  By Lemma 1, each `Q_i` is the convex replacement chain for the
single edge `a_i a_(i+1)`.  Replace those edges in the cyclic boundary word
of `A` by their chains.  The selected edges have disjoint endpoint pairs.
Every local turn internal to a replacement chain, and each turn joining that
chain to an unchanged old edge, occurs in the convex polygon `A union Q_i`.
Every remaining turn occurs in `A`, so all are strict and have the same
orientation.

For completeness, the resulting boundary word is simple.  The replacement
at edge `i` lies beyond its support line and in every other support
half-plane.  Its outward region is separated from the outward region of a
nonadjacent replacement by the unchanged old edge(s) between them.  Thus two
replacement arcs can meet neither each other nor a nonincident old boundary
arc.  The simple, consistently turning boundary word contains every listed
point as a vertex, proving (3). `square`

Consequently, if `link(A)` is the simplicial link of `A`, then coefficientwise

\[
 \boxed{
 Z_{\operatorname{link}(A)}(z)\ \geq\
 \sum_{I\text{ independent in }C_r}\prod_{i\in I}L_i^A(z).}      \tag{4}
\]

Here the empty matching contributes one.  This is the correct replacement
for the false product over *all* edge pockets.  Adjacent pockets interact;
an arbitrary matching of nonadjacent pockets genuinely factors.

## 3. A block extension inequality

Write

\[
 m_i(A)=|R_i(A)|,\quad u(A)=\sum_i m_i(A),\quad
 M(A)=\max_i(m_{i-1}+m_i+m_{i+1}).                              \tag{5}
\]

Let `lambda_s(A)` count `s`-sets `X subset P minus A` for which `A union X`
is convex.  Restrict (4) to one-point chains.  Construct an ordered matching
of `s` pockets greedily.  After `j` pockets have been chosen, their forbidden
three-windows have total weight at most `j M(A)`.  Dividing the ordered count
by `s!` gives

\[
 \boxed{
 \lambda_s(A)\ge {1\over s!}
 \prod_{j=0}^{s-1}(u(A)-jM(A))_+.}                              \tag{6}
\]

Double counting extensions gives

\[
 \sum_{A\in F_r}\lambda_s(A)={r+s\choose s}v_{r+s}.             \tag{7}
\]

For `a_r=v_r/binom(n,r)` and
`p_r=a_(r+1)/a_r`, (6)--(7) yield the exact block inequality

\[
 \boxed{
 {a_{r+s}\over a_r}=\prod_{j=0}^{s-1}p_{r+j}
 \ge {\mathbb E_{A\in F_r}
       \prod_{j=0}^{s-1}(u(A)-jM(A))_+
       \over (n-r)_s}.}                                        \tag{8}
\]

If `M(A)<=rho u(A)` for every rank-`r` face and `(s-1)rho<1`, Jensen's
inequality and `E u=(n-r)p_r` give

\[
 \prod_{j=0}^{s-1}p_{r+j}
 \ge {((n-r)p_r)^s\over(n-r)_s}
      \prod_{j=0}^{s-1}(1-j\rho).                              \tag{9}
\]

At `s=2`, this recovers the second-moment curvature localization in the
circuit-hardcore report.  For arbitrary `s`, it says that a deficient block
of ranks is possible only through a genuinely concentrated cyclic tangent
window.  It does not handle the one-window extreme, which is the restart
case.

## 4. Exact QuickHull recursion inside one cone

Fix roots `u,v` and a point set `Q` strictly on one side of the line `uv`.
Let

\[
 R_{uv}(Q;z)=\sum_{\substack{C\subseteq Q\\
                       \{u,v\}\cup C\text{ convex}}}z^{|C|}.    \tag{10}
\]

Choose `x in Q` maximizing signed distance from `uv`.  Partition `Q-x` into

* `Q_L`: points beyond `ux`, on the side opposite `v`;
* `Q_R`: points beyond `xv`, on the side opposite `u`; and
* `Q_0`: the remaining points, which lie in the open triangle `uxv`.

The maximal-distance choice makes `Q_L` and `Q_R` disjoint.  A rooted face
which contains `x` cannot contain a member of `Q_0`, and its two boundary
pieces are independent rooted chains.  A rooted face which omits `x` is an
arbitrary rooted face of `Q-x`.  Hence

\[
 \boxed{
 R_{uv}(Q;z)=R_{uv}(Q-x;z)
       +zR_{ux}(Q_L;z)R_{xv}(Q_R;z).}                            \tag{11}
\]

This is a deterministic binary deletion/pivot recurrence.  In particular,
once the ambient rooted instance is fixed, a selected final face determines
the whole selected tangent stack: at every node its membership decides the
exclude/include branch, and an include branch has canonically determined
left and right children.  No fresh `log r`-bit middle-edge name is required
per selected level.

What (11) does **not** solve is the exclude branch.  A final rooted face can
exclude arbitrarily many successively outer pivots before selecting an inner
one.  Those alternatives are real source multiplicity, not tangent-state
ambiguity.  Moreover, the selected branch discards the arbitrary subinstance
`Q_0`.  Any full restart must keep a second, unrooted potential which pays
for excluded pivots and recursively absorbs these `Q_0` pockets.

## 5. Regression on the Pascal curvature obstruction

Pointwise half-curvature is false on central Pascal towers, but its failures
come in the final three ranks of each cap--cup period.  The verifier evaluates
the exact graded recurrence for central templates `h=4,6,8,10,12`.  For the
natural period `2h-4`, every tested full block satisfies

\[
 \prod_{j=0}^{2h-5}{p_{r+j+1}\over p_{r+j}}>2^{-(2h-4)}.         \tag{12}
\]

At depth eight, the smallest surplus over the right side, in bits, is
respectively

```text
h=4: 1.8184   h=6: 2.1602   h=8: 2.4478
h=10: 2.6531  h=12: 2.7585.
```

This is a regression test, not a universal theorem.  It confirms that the
all-orders/block state (8), rather than pointwise curvature, has the right
shape on the sharp construction.

## 6. A scalar restart that must not be used

During this attack a particularly attractive proposal was monotonicity of

\[
 \Phi(P)=2Z_P(1)-|P|Z_P(1/2)
\]

under removal of the outer hull.  If `H=ext(P)`, `I=P-H`, and `J_t` is the
weight of convex faces meeting `H`, this would say

\[
 |H|Z_I(1/2)+|P|J_{1/2}\le2J_1.                                \tag{13}
\]

The planar-Tutte lane has now killed (13) exactly.  Its configuration has 60
rational points in convex position inside a large rational outer triangle.
The ratio left/right in (13) is `2.855924...`; all three one-root variants
fail as well.  This is independently checked by
`agent_planar_tutte/verify_outer_triangle_barrier.py`.  The mechanism is
decisive: one outer tangent retains only a
semicircle-type rooted family, whereas the Boolean inner half-weight is
`(3/2)^60`.

Thus the discarded `Q_0` term in (11) cannot be paid by a scalar onion
monotonicity.  A successful induction must retain at least the pair

\[
 \bigl(Z_Q(z),\ R_{uv}(Q;z)\bigr)                               \tag{14}
\]

and allow tangent credit accumulated in one orientation to be spent after a
later split in the other.  This is consistent with both the outer-triangle
barrier and the periodic Pascal compensation.

## 7. Precise surviving gate

The new geometry reduces the live route to a bivariate weighted Hall/Bellman
inequality:

1. use the matching polynomial (4) whenever tangent mass occupies
   nonadjacent pockets;
2. in one concentrated pocket, apply the exact binary recurrence (11);
3. charge the exclude branch and every discarded middle pocket `Q_0` to
   unrooted convex mass `Z_(Q_0)`, while retaining both root orientations;
4. prove that total charge is at most `2^(r+o(r))` at rank `r`.

Steps 1--2 are now theorems.  Step 3 with only a scalar unrooted potential is
false by (13).  No valid bivariate inequality completing Step 4 is proved in
this report, so Erdős 838 remains open.

## 8. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_tangent_restart/tangent_restart_audit.py
```

The exact-integer audit checks 854,553 single-pocket instances of (1),
78,814 arbitrary two-pocket chain products, 77 products using at least three
matched pockets, and 122,880 rooted subsets in (11).  It also evaluates the
exact Pascal graded recurrences used in Section 5 and writes
`certificate.json` beside the script.
