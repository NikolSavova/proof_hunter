# Parabolic endpoint-product incidence: Singer ambient sharpness

## Status

Fix a primitive direction $w$ and a transverse displacement $c$.  In
adapted integer coordinates, write the fibres of $A$ as $A_r$ and form

\[
 P_{w,c}=\{(r,b-a):a\in A_r,\ b\in A_{r+c}\}.          \tag{0.1}
\]

Distance-Sidonicity makes the second coordinates in (0.1) globally
distinct.  Hence, for three prescribed distinct levels, two endpoint-product
points determine at most one third collinear point.  This gives the exact
local bound

\[
 T(r_0,r_1,r_2)
 \le \min\{b_{r_0}b_{r_1},b_{r_1}b_{r_2},
                 b_{r_2}b_{r_0}\},
 \qquad b_r=|A_r||A_{r+c}|.                            \tag{0.2}
\]

This elementary product bound is best possible in aggregate order.  Using
Singer perfect difference sets and a six-colour probabilistic argument, one
gets infinitely many distance-Sidon sets

\[
 A\subset[m]^2,qquad k=|A|\asymp q,qquad m=O(q^2),   \tag{0.3}
\]

with

\[
 \boxed{\Omega(q^4)=\Omega(m^2)}                       \tag{0.4}
\]

clean, fully transverse, equal-area ordered triangle pairs of trace $2$,
all inside one cell $(w,c)$ and using only three source levels.

Thus the desired upper bound
$m^{o(1)}(k^3+m^2)$, if true, is ambient-sharp already in the parabolic
branch.  There can be no power saving over the $m^2$ term, no uniform
divisor-size cell load, and no argument that treats a three-level
endpoint-product cell as negligible.  What remains is a matching upper
bound when many directions, transverse shifts, and level triples interact.

## 1. Exact three-level product bound

Choose $z_w\in\mathbb Z^2$ with $\det(w,z_w)=1$.  A directed difference
with transverse coordinate $c$ has the unique form

\[
 y-x=c z_w+s w,qquad r=\det(w,x).                     \tag{1.1}
\]

If two labelled correspondences give the same $s$, then they give the same
directed difference vector.  A nonzero directed vector has at most one
realization in a distance-Sidon set.  After deleting the diagonal
correspondences when $c=s=0$, the points of $P_{w,c}$ therefore have
distinct second coordinates.  Its vertical fibre at $r$ has size

\[
 b_r=|A_r||A_{r+c}|.                                  \tag{1.2}
\]

Fix three distinct levels $r_0,r_1,r_2$.  A point in either two vertical
fibres determines a unique nonvertical line, and that line meets the third
vertical fibre in only one location.  Since $P_{w,c}$ is a set, there is at
most one third point.  Choosing each of the three possible pairs proves
(0.2).

For trace $2$, the collinear lines have the form

\[
 s=\alpha+\lambda r,qquad \lambda\ne0,               \tag{1.3}
\]

and give the affine map

\[
 (a,r)\longmapsto(a+\alpha+\lambda r,r+c).             \tag{1.4}
\]

Thus (0.2) is an endpoint-product incidence bound for the actual
determinant-one parabolic maps, not for the raw displacement relaxation.

## 2. Singer input

For every prime power $q$, Singer's theorem supplies a perfect difference
set

\[
 G\subset\mathbb Z_N,qquad |G|=q+1,qquad
 N=q^2+q+1,                                           \tag{2.1}
\]

meaning that each nonzero $x\in\mathbb Z_N$ has a unique ordered
representation

\[
 x=b-a,qquad a,b\in G.                               \tag{2.2}
\]

We use odd prime powers so that $2$ is invertible modulo $N$.  The input is
the classical result of J. Singer, *A theorem in finite projective geometry
and some applications to number theory*, Trans. AMS 43 (1938), 377--385,
doi:10.1090/S0002-9947-1938-1501951-4.

Consider triples of nonzero group elements satisfying

\[
 x_0+x_2=2x_1.                                        \tag{2.3}
\]

There are $N^2-O(N)$ such ordered triples.  Replace each $x_i$ by its
unique representation $(a_i,b_i)$ from (2.2).  All six endpoints are
distinct for all but $O(q^3)$ triples.  Indeed, for any prescribed equality
between endpoints from two representation pairs, choosing the shared
endpoint and the other two endpoints gives only $O(q^3)$ possibilities;
the third group difference and its representation are then forced.

Colour the elements of $G$ independently and uniformly with the six
colours

\[
 S_0,S_1,S_2,T_0,T_1,T_2.                             \tag{2.4}
\]

A six-distinct solution has the prescribed colour pattern
$a_i\in S_i$, $b_i\in T_i$ with probability $6^{-6}$.  Hence some colouring
retains $\Omega(q^4)$ solutions of (2.3).

## 3. Lifting the modular records to exact integer records

Represent the elements of $G$ by integers in $[0,N-1]$.  For a retained
solution put

\[
 \Delta_i=b_i-a_i.
\]

Equation (2.3) says

\[
 \Delta_0+\Delta_2-2\Delta_1=\ell N                 \tag{3.1}
\]

for one of only seven integers $\ell\in\{-3,\ldots,3\}$.  Pigeonholing
retains $\Omega(q^4)$ records with one common $\ell$.

Assign a lift $L_C\in\mathbb Z$ to each colour and replace a residue $g$ of
colour $C$ by

\[
 Z_g=g+NL_C.                                          \tag{3.2}
\]

Take all source lifts to be zero and choose the target lifts so that

\[
 (L_{T_0}-L_{S_0})+(L_{T_2}-L_{S_2})
 -2(L_{T_1}-L_{S_1})=-\ell.                           \tag{3.3}
\]

For example, set $L_{T_0}=-\ell$ and the other target lifts to zero.
Equations (3.1)--(3.3) now give the exact integer identity

\[
 (Z_{b_0}-Z_{a_0})+(Z_{b_2}-Z_{a_2})
 =2(Z_{b_1}-Z_{a_1}).                                 \tag{3.4}

The lifted set $\{Z_g:g\in G\}$ remains a Golomb ruler.  Equality of two
directed integer differences reduces modulo $N$ to equality of two group
differences, and (2.2) then identifies both ordered pairs.  Its diameter is
$O(N)$ because all lifts are bounded absolutely by three.

Fix $H=10$, $R=20$, and place a mark of source colour $S_i$ at

\[
 (RZ_g,i),                                            \tag{3.5}
\]

and a mark of target colour $T_i$ at

\[
 (RZ_g,H+i).                                          \tag{3.6}
\]

Translate the whole set into the positive quadrant.  It has $q+1$ points
and lies in a box of side $O(N)=O(q^2)$.  It is distance-Sidon: every
unordered point pair has a different positive horizontal difference, and
the factor $R$ makes a nonzero difference of horizontal squares larger
than every possible difference of vertical squares.

For a retained solution, map the three source points labelled $a_i$ to the
three target points labelled $b_i$.  Their displacements are

\[
 (R(Z_{b_i}-Z_{a_i}),H).
\]

By (3.4), their longitudinal coordinates are affine functions of the
levels $0,1,2$.  Thus the pair has equal signed area and its affine linear
part has determinant one and trace two.

## 4. Removing all nontransverse records

It remains to check that only $O(q^3)$ of the retained records can fail
full transversality.  Write the first two source horizontal side
coordinates as

\[
 p=R(Z_{a_1}-Z_{a_0}),\qquad
 q'=R(Z_{a_2}-Z_{a_1}),\qquad d=p-q',                 \tag{4.1}
\]

and let $\lambda$ be the horizontal displacement increment from level zero
to level one.  The target horizontal side coordinates are
$p+\lambda,q'+\lambda$.  Directly computing the $3\times3$ cross matrix
shows that a zero entry occurs exactly when

\[
 \lambda=0
 \quad\text{or}\quad
 d\in\{\lambda,-\lambda,2\lambda,-2\lambda\}.         \tag{4.2}
\]

The first three alternatives force equality of two distinct directed
differences in the lifted Golomb ruler, so they are impossible.  If
$d=2\lambda$, then

\[
 Z_{b_2}-Z_{b_0}=2(Z_{a_1}-Z_{a_0}).                  \tag{4.3}
\]

Choose the source pair $(a_0,a_1)$ in $O(q^2)$ ways.  The Golomb property
gives at most one target pair $(b_0,b_2)$ with the prescribed doubled
difference.  Choosing $b_1$ in $O(q)$ ways, equation (3.4) determines
$Z_{a_2}$ and hence at most one $a_2$.  Thus (4.3) occurs only $O(q^3)$
times.  The case $d=-2\lambda$ is identical with the other source side.

Source or target collinearity is impossible: modulo $N$ it would give two
representations of the same nonzero group difference.  Removing endpoint
coincidences and the $O(q^3)$ cases above leaves $\Omega(q^4)$ clean fully
transverse trace-$2$ records.  This proves (0.4).

## 5. Consequence for the aggregate gate

The Singer construction lives in a single endpoint-product cell with
$w=(1,0)$, $c=H$, and three source levels.  Typically each vertical fibre
has size $\Theta(q^2)$, so the right side of (0.2) is $\Theta(q^4)$; the
construction attains that order.  Since $m=\Theta(q^2)$, this is exactly
the $m^2$ term in the desired global estimate.

Therefore a successful upper bound must sum the local products in (0.2)
across all $(w,c)$ and level triples essentially without losing more than
$m^{o(1)}$.  Neither a per-cell divisor bound nor a saving from having only
three active levels is available.  The remaining problem is a global
endpoint allocation theorem controlling how often the same six fibre
classes can participate across different primitive directions.

## 6. Verification

The verifier uses the perfect difference set

\[
 \{0,1,6,21,28,44,46,54\}\subset\mathbb Z_{57}
\]

and an explicit six-colouring.  It checks the perfect-difference property,
the lifted Golomb and distance-Sidon properties, the endpoint-product
fibres, exact area equality, trace-$2$ displacement relation, and all nine
nonzero cross determinants.

Run:

```bash
python phase2/loop/erdos1208/verify_parabolic_endpoint_product_singer_ambient_sharpness.py
```

