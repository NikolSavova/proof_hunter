# Parabolic graph directions: derivative incidence and curvature

## Status

The few-fibre theorem leaves directions in which the projection of $A$ has
many singleton fibres.  In that regime the local-min envelope alone cannot
see the longitudinal coordinates: for the integer parabola it is
$\Theta(k^4)$.  Retaining those coordinates gives a useful exact reduction
and a new height theorem.

Fix a primitive direction $w$ and suppose first that every occupied
$w$-fibre contains one point.  Write the occupied transverse levels as
$R$, and choose $z_w\in\mathbb Z^2$ with $\det(w,z_w)=1$.  There is an
integer-valued function $f$ on $R$ such that

\[
 x_r=r z_w+f(r)w.                                    \tag{0.1}
\]

For a nonzero shift $c$, define its derivative graph

\[
 P_c=\{(r,d_c(r)):r,r+c\in R\},
 \qquad d_c(r)=f(r+c)-f(r).                          \tag{0.2}
\]

Clean trace-$2$ records are precisely nonhorizontal collinear triples in
the sets $P_c$.

This note proves:

1. **Generic incidence term.**  If $n_c=|P_c|$ and $L_c$ is its maximum
   nonhorizontal line occupancy, then

   \[
    T_w\ll k^3\log k+\sum_{c\ne0}n_cL_c^2.           \tag{0.3}
   \]

   Thus the Szemeredi--Trotter main term already has the desired
   near-$k^3$ size.  Only rich derivative lines remain.

2. **Exact curvature-height lemma.**  If one derivative line contains a
   directed path of $L$ consecutive shift-$c$ correspondences and has
   slope $\lambda\ne0$, then, for $A\subset[m]^2$ and
   $q=\|w\|_\infty$,

   \[
    m-1\ge {|\lambda c|q\over2}\lfloor L/2\rfloor^2.
                                                               \tag{0.4}
   \]

   In particular $L\ll\sqrt{m/(q|\lambda c|)}$.  This turns every
   path-rich exceptional line into an ambient-height contribution.

3. **Full-cell theorem.**  Suppose $R=\{1,\ldots,K\}$.  If all points of
   $P_c$ lie on one nonhorizontal line, then its slope is a nonzero integer
   and

   \[
    m-1\gg {qK^2\over c}\qquad(c\le K/3).            \tag{0.5}
   \]

   Moreover, among shifts $1\le c\le K/2$, the number $J$ of such full
   cells satisfies

   \[
    J\ll 1+{m\over qK}.                              \tag{0.6}
   \]

   Their total collinear-triple contribution is therefore

   \[
    \ll K^3+{mK^2\over q}.                           \tag{0.7}
   \]

   In particular this branch is at most $O(m^2+K^3)$ whenever
   $q\ge K^2/m$.  The integer parabola has $q=1$, $m\asymp K^2$ and attains
   the order of (0.5)--(0.7).

4. **Matching-rectangle theorem.**  Let $t\ge3$, suppose the levels
   $0,\ldots,3t$ are occupied, and suppose that for every
   $t\le c\le2t$, the $t$ derivative points

   \[
    \{(r,d_c(r)):0\le r<t\}                          \tag{0.8}
   \]

   lie on one line.  Each individual shift graph in (0.8) is a matching:
   its tail and head blocks are disjoint.  Nevertheless the cocycle forces
   $f$ to be quadratic on an interval of length $2t$, and

   \[
    m-1\gg qt^2.                                     \tag{0.9}
   \]

   The $(t+1)\binom t3=\Theta(t^4)$ triples in this planted matching
   rectangle are therefore $O(m^2)$.

The unresolved residual is now specific: irregular rich derivative lines
whose tail shift graph has many short components, but which do not assemble
into the Cartesian matching rectangle (0.8), together with partial rich
lines that do not cover the whole cell.  Curvature cannot see an isolated
matching edge.  A finish must extract enough overlapping patches for the
cocycle, or charge the remaining matching components through their
endpoints.  This is strictly narrower than the raw local-min summation
problem.

## 1. Adapted coordinates and the derivative graph

The vectors $z_w,w$ form a unimodular basis, up to sign, so (0.1) has an
integer coefficient $f(r)$.  A correspondence $x_r\mapsto x_{r+c}$ has
displacement

\[
 x_{r+c}-x_r=c z_w+d_c(r)w.                         \tag{1.1}
\]

By the exact parabolic lift, three such correspondences define a
determinant-one trace-$2$ affine map exactly when

\[
 d_c(r)=\alpha+\lambda r                              \tag{1.2}
\]

at their three levels.  Full transversality requires $\lambda\ne0$.
Consequently the desired graph-like record count is the number of
nonhorizontal collinear triples in the planar point sets $P_c$.

The cell sizes obey

\[
 \sum_{c\ne0}n_c=k(k-1),\qquad n_c\le k,             \tag{1.3}
\]

because every ordered pair of occupied transverse levels has one nonzero
difference.

## 2. The generic Szemeredi--Trotter contribution

For a planar set of $n$ points with maximum relevant line occupancy $L$,
the standard rich-line consequence of the Szemeredi--Trotter theorem is

\[
 T(P)\ll n^2\log n+nL^2,                             \tag{2.1}
\]

where $T(P)$ counts collinear triples.  It follows by summing the usual
$O(n^2/t^3+n/t)$ bound for lines incident to at least $t$ points over
dyadic $t$.

Apply (2.1) to each $P_c$.  From (1.3),

\[
 \sum_c n_c^2\le k\sum_c n_c<k^3.                  \tag{2.2}
\]

Equations (2.1)--(2.2) prove (0.3).  The same statement holds if one removes
all lines above a chosen richness threshold: the retained lines contribute
the $k^3\log k$ main term, and only the explicitly rich tail remains.

## 3. Constant second difference on a path

Let a line (1.2) contain the correspondences with tail levels

\[
 r_j=r_0+jc,\qquad 0\le j<L.                         \tag{3.1}
\]

Thus the associated vertices are $x_{r_0},\ldots,x_{r_0+Lc}$.  Put
$\delta_j=x_{r_{j+1}}-x_{r_j}$.  From (1.1)--(1.2),

\[
 \delta_{j+1}-\delta_j=\lambda c w.                 \tag{3.2}
\]

Choose a coordinate $u$ for which $|w_u|=q$.  The scalar sequence
$X_j=(x_{r_j})_u$ has constant second difference

\[
 X_{j+2}-2X_{j+1}+X_j=\lambda c w_u.                \tag{3.3}
\]

For any scalar sequence with constant second difference $D$,

\[
 X_0-2X_s+X_{2s}=Ds^2.                              \tag{3.4}
\]

If all $X_j$ lie in an interval of length $M=m-1$, the left side of (3.4)
has absolute value at most $2M$.  Taking $s=\lfloor L/2\rfloor$ proves
(0.4).

This argument is insensitive to a large linear drift: the second
difference removes it exactly.  It is therefore stronger than bounding the
longitudinal coordinate range directly.

## 4. Complete interval projections

Assume now $R=\{1,\ldots,K\}$ and all of $P_c$ lies on
$d_c(r)=\alpha_c+\lambda_c r$.

Because $d_c(r)$ is integral at consecutive $r$, $\lambda_c\in\mathbb Z$.
Full transversality says $\lambda_c\ne0$.  The shift graph on the interval
is the union of at most $c$ directed paths, one of which has at least

\[
 L\ge \left\lfloor{K-c\over c}\right\rfloor         \tag{4.1}
\]

edges.  For $c\le K/3$, substituting $|\lambda_c|\ge1$ and (4.1) into
(0.4) proves (0.5), with an absolute implied constant.  The restriction is
essential for this path argument: at $c=K/2$ the shift graph can be a pure
matching.

There is also a useful coexistence restriction.  The displacement vectors
in this cell are

\[
 c z_w+(\alpha_c+\lambda_c r)w,
 \qquad 1\le r\le K-c.                              \tag{4.2}
\]

Their coordinate in a direction where $|w_u|=q$ ranges by
$|\lambda_c|q(K-c-1)$, but every displacement coordinate lies in
$[-(m-1),m-1]$.  Hence, for $c\le K/2$ and $K\ge4$,

\[
 |\lambda_c|\ll {m\over qK}.                        \tag{4.3}
\]

The slopes belonging to two different full cells are distinct.  Indeed,
if $c>d$ and $\lambda_c=\lambda_d$, then for every
$1\le r\le K-c$,

\[
 f(r+c)-f(r+d)=
 (\alpha_c-\alpha_d)+\lambda_c r-\lambda_d r
 =\alpha_c-\alpha_d.                               \tag{4.4}
\]

When $K-c\ge2$, (4.4) gives the same nonzero directed difference vector
for two different ordered endpoint pairs.  Distance-Sidonicity implies
vector-Sidonicity, so this is impossible.  Thus the $\lambda_c$ are
distinct nonzero integers in the range (4.3), proving (0.6).  Multiplying
by the trivial $O(K^3)$ triples in one cell gives (0.7).

If $c=1$ is a full cell, summing its affine first difference shows directly
that $f$ is quadratic on the whole interval.  Formula (0.4) then gives
$m\gg qK^2$.  This is the exact quadratic mechanism exhibited by the
integer parabola.

## 5. The matching residual and the cocycle

For a line $\ell\subset P_c$, join two of its tail levels when they differ
by $c$.  Its components are directed paths.  If there are $u_\ell$
components and $t_\ell$ points on the line, one component has length at
least roughly $t_\ell/u_\ell$.  Therefore (0.4) gives the exact alternative

\[
 t_\ell\ll u_\ell
 \left(1+\sqrt{m\over q|\lambda c|}\right).          \tag{5.1}
\]

All path-dominant lines are consequently height-controlled.  The only way
a rich line can evade (5.1) is to have many components, approaching a
matching of isolated correspondences.

Different shifts are not independent.  Wherever all terms exist,

\[
 d_{c+d}(r)=d_c(r)+d_d(r+c),                         \tag{5.2}
\]

and

\[
 d_c(r)-d_d(r)=d_{c-d}(r+d)\qquad(c>d).             \tag{5.3}
\]

Thus two affine derivative patches with overlapping domains create a third
affine patch; equal slopes would create a repeated directed vector, as in
(4.4), while unequal slopes create nonzero curvature and invoke (0.4).
The missing global theorem is a patch-selection statement ensuring enough
overlap in (5.2)--(5.3) when many rich lines are matching-like.

## 6. What this proves and what it does not

### 6.1 A matching rectangle forces a quadratic block

Here is the promised cocycle theorem.  Assume the hypotheses around (0.8)
and write

\[
 d_c(r)=\alpha_c+\lambda_c r
 \qquad(0\le r<t).                                  \tag{6.1}
\]

For consecutive shifts $c,c+1$, subtraction cancels the common tail:

\[
 \begin{aligned}
 g(r+c)&:=f(r+c+1)-f(r+c)\\
       &=d_{c+1}(r)-d_c(r)\\
       &=(\alpha_{c+1}-\alpha_c)
          +(\lambda_{c+1}-\lambda_c)r.
 \end{aligned}                                      \tag{6.2}
\]

Thus the ordinary first difference $g(s)=f(s+1)-f(s)$ is affine on every
interval

\[
 [c,c+t-1],\qquad t\le c<2t.                        \tag{6.3}
\]

Consecutive intervals overlap in at least two integer points.  Two affine
functions agreeing at two points are identical, so one affine formula

\[
 g(s)=A+Bs                                            \tag{6.4}
\]

holds throughout $t\le s\le3t-2$.  The integer $B$ is nonzero.  If it were
zero, the directed differences

\[
 x_{s+1}-x_s=z_w+g(s)w                               \tag{6.5}
\]

would be identical for many distinct endpoint pairs, contradicting
vector-Sidonicity.  Hence one coordinate of the points
$x_t,\ldots,x_{3t-1}$ has constant nonzero second difference $Bw_u$.
Equation (3.4) proves (0.9).  Finally, every cell in (0.8) supplies at most
$\binom t3$ relevant triples, so their total is $O(t^4)=O(m^2/q^2)$.

This theorem is important because each one of the cells in isolation is a
pure matching: none contains a two-edge path.  The height appears only
after two adjacent shifts are coupled by (6.2).

### 6.2 Current boundary

The local-min envelope from the preceding note counts every triple of
active levels and therefore cannot distinguish a generic derivative graph
from a quadratic one.  The present lift restores precisely that lost
coordinate.

The following branches are now rigorous:

* the generic incidence contribution is $O(k^3\log k)$;
* every rich-line path pays the curvature-height bound (0.4);
* complete-interval, whole-cell rich lines obey the aggregate estimate
  (0.7), and close at ambient scale when $q\ge K^2/m$;
* a full shift-$1$ cell forces an exact quadratic and height $\Omega(qK^2)$.
* a full $t\times t$ rectangle of matching-like affine derivative patches
  forces a quadratic interval and pays $O(m^2)$ by (0.9).

What remains is not an arbitrary high-energy projection.  It is the
endpoint-realized family of partial affine derivative patches whose shift
graphs have many short components and whose tail/shift support avoids a
large Cartesian rectangle.  Any continuation should seek a
dependent-random-choice or Zarankiewicz extraction in that support while
retaining the affine line labels, rather than return to the local-min
envelope.

## 7. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_parabolic_graph_derivative_curvature_gate.py
```

The verifier checks the adapted derivative identities, the exact
second-difference height inequality, the integer-parabola saturation, the
distinct-slope coexistence statement on exact quadratic distance-Sidon graph
sets, randomized derivative graphs, and the $\sum n_c^2\le k^3$ incidence
budget.
