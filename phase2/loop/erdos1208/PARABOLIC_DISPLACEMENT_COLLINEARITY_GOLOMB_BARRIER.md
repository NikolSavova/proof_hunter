# Parabolic displacement collinearity: the Golomb six-row barrier

## Status

The trace-$2$ characterization by collinear displacement vectors, and the
trace-$-2$ characterization by collinear endpoint sums, are exact only
when the equal-area condition is retained.  They cannot be relaxed to a
raw collinear-triple theorem for $A-A$ or $A+A$.

More strongly, for arbitrarily large $h$ there are distance-Sidon sets
$A_h\subset[m]^2$ with

\[
 |A_h|=6h,\qquad m=O(h^2),                             \tag{0.1}
\]

for which $A_h-A_h$ contains $h^6$ ordered collinear triples with all six
endpoint labels distinct and with both endpoint triangles noncollinear.
There is an analogous construction in $A_h+A_h$.  Since

\[
 k^3+m^2=O(h^4),                                      \tag{0.2}
\]

this raw collinear count exceeds the desired scale by a quadratic factor.
Global uniqueness of nonzero directed differences and of their Euclidean
norms does not repair the loss.

The exact surviving formulation is two-dimensional.  For every
displacement-line direction $w$, one must retain both the source projection
$r=\det(w,x)$ and the longitudinal displacement coordinate $s$.  A
parabolic record is a collinear triple in the resulting $(r,s)$ plane, with
three distinct $r$-coordinates.  In the six-row obstruction the raw
displacements are collinear, but the $(r,s)$ points are usually not; the
equal-area equation is precisely their missing collinearity.

Thus this note is a rigorous no-go for the proposed one-coordinate route,
not a no-go for the corrected parabolic incidence gate.

## 1. A quadratic-length Golomb ruler

Let $p$ be an odd prime and define

\[
 g_i=2pi+(i^2\bmod p),\qquad 0\le i<p,                \tag{1.1}
\]

where the residue lies in $\{0,\ldots,p-1\}$.  The set
$G_p=\{g_0,\ldots,g_{p-1}\}$ is a Golomb ruler: all positive differences
are distinct.

Indeed, suppose $j>i$, $\ell>k$, and

\[
 g_j-g_i=g_\ell-g_k.                                  \tag{1.2}
\]

The residue terms in (1.1) differ by less than $p$, so (1.2) first forces
$j-i=\ell-k=:d$.  Reducing modulo $p$ then gives

\[
 (i+d)^2-i^2\equiv(k+d)^2-k^2\pmod p,
\]

hence $2d(i-k)\equiv0\pmod p$.  Since $0<d<p$, this gives $i=k$ and
$j=\ell$.

Consequently $G_p$ is also additive Sidon: an equality of two unordered
sums can be rearranged into an equality of positive differences.  By
Bertrand's postulate, for every $h$ one may choose

\[
 6h<p<12h,                                             \tag{1.3}
\]

and use the first $6h$ elements of $G_p$.  Their maximum is $O(h^2)$.

## 2. Trace-$\boldsymbol{+2}$ raw-displacement barrier

Partition those $6h$ ruler marks into six disjoint classes

\[
 X_0,X_1,X_2,Y_0,Y_1,Y_2,qquad |X_i|=|Y_i|=h.
\]

Fix $H=10$ and $R=20$, and put

\[
 A_h^+=
 \bigcup_{r=0}^2\{(Rx,r):x\in X_r\}
 \ \cup\
 \bigcup_{r=0}^2\{(Ry,H+r):y\in Y_r\}.               \tag{2.1}
\]

### Lemma 2.1

$A_h^+$ is distance-Sidon and lies in a box of side $O(h^2)$.

### Proof

Every unordered pair of points uses a different positive horizontal
difference, because the underlying ruler marks have distinct differences.
If two squared Euclidean distances were equal, then

\[
 R^2(d_1^2-d_2^2)=v_2^2-v_1^2,                        \tag{2.2}
\]

where $d_1\ne d_2$ are positive integers and
$|v_i|\le H+2=12$.  The left side has absolute value at least $R^2=400$,
while the right side has absolute value at most $144$, a contradiction.
The coordinate bound follows from (1.1)--(1.3). $\square$

If $[m]$ is taken to start at $1$, translate the whole configuration by
$(1,1)$; none of the arguments changes.

For each $r$, take every ordered correspondence

\[
 (Rx,r)\longmapsto(Ry,H+r),qquad x\in X_r, y\in Y_r.
\]

Its displacement is

\[
 \delta=(R(y-x),H).                                   \tag{2.3}
\]

Thus the $h^2$ displacement vectors from each of the three blocks, and all
$3h^2$ together, lie on the horizontal line of height $H$.  They are
distinct because directed differences in a distance-Sidon set are unique.

Choose independently one correspondence from each block.  This gives
$h^6$ ordered collinear displacement triples.  Their six endpoints are
distinct because the six ruler classes are disjoint.  The three source
points, on rows $0,1,2$, would be collinear only if

\[
 x_0+x_2=2x_1,                                        \tag{2.4}
\]

which contradicts the additive-Sidon property of the ruler marks.  The
same argument applies to the target points on rows $H,H+1,H+2$.

This proves the difference-set assertion in the status.  Notice that it
already retains six distinct endpoint labels and nonzero source and target
areas.  What it does not retain is equality of those two areas.

## 3. Trace-$\boldsymbol{-2}$ raw-sum barrier

Use the same six ruler classes, but put the target classes on rows
$H,H-1,H-2$:

\[
 A_h^-=
 \bigcup_{r=0}^2\{(Rx,r):x\in X_r\}
 \ \cup\
 \bigcup_{r=0}^2\{(Ry,H-r):y\in Y_r\}.                \tag{3.1}
\]

The proof of distance-Sidonicity is identical.  For a correspondence
between the two classes indexed by $r$, the endpoint sum is

\[
 \sigma=(R(x+y),H).                                   \tag{3.2}
\]

All $3h^2$ such sums are distinct, since the ruler is additive Sidon, and
they lie on one horizontal line.  Choosing one from each block gives
$h^6$ collinear sum triples.  The source and target triangles are again
noncollinear by (2.4).  This proves the sumset assertion.

## 4. The exact two-coordinate parabolic lift

The obstruction identifies the coordinate that must not be discarded.
Let $w\in\mathbb Z^2$ be a primitive direction and choose
$z_w\in\mathbb Z^2$ with $\det(w,z_w)=1$.

### Trace $+2$

For an ordered correspondence $x\mapsto y$, write

\[
 \delta=y-x=c z_w+s w,
 \qquad c=\det(w,\delta),
 \qquad r=\det(w,x).                                  \tag{4.1}
\]

For fixed $(w,c)$, let $P^+_{w,c}$ be the labelled set of points $(r,s)$
arising in this way.  For three noncollinear source points, the
correspondences define a trace-$2$ determinant-one affine map exactly when
their $(r,s)$ points lie on a line

\[
 s=\alpha+\lambda r.                                  \tag{4.2}
\]

Indeed, (4.1)--(4.2) give

\[
 y=x+c z_w+\alpha w+lambda\det(w,x)w,                \tag{4.3}
\]

whose linear part is
$I+\lambda w\otimes(v\mapsto\det(w,v))$.  The rank-one term is nilpotent,
so the linear part has determinant one and trace two.  Conversely, every
nonscalar trace-$2$ map has this form.

For a source edge $e=x_j-x_i$,

\[
 Q_M(e)=-\lambda\bigl(r_j-r_i\bigr)^2.                \tag{4.4}
\]

Thus full transversality forces $\lambda\ne0$ and the three
$r$-coordinates to be pairwise distinct.

### Trace $-2$

Replace $\delta$ in (4.1) by $\sigma=y+x$.  A line (4.2) now gives

\[
 y=-x+c z_w+\alpha w+lambda\det(w,x)w,               \tag{4.5}
\]

whose linear part has determinant one and trace $-2$.  Formula (4.4)
continues to hold.  This is the exact sumset lift.

In the six-row barriers, all raw displacement or sum vectors lie on one
line, but the associated longitudinal coordinates $s$ are arbitrary
functions of the source level $r$.  Only the much smaller subcollection
satisfying (4.2) has equal area.  Therefore the $s$-coordinate is not a
technical decoration; it contains the entire missing determinant-one
condition.

## 5. Consequence for the proof route

No estimate of the form

\[
 \#\{\text{clean endpoint-labelled collinear triples in }A-A\}
 \le m^{o(1)}(k^3+m^2)                                \tag{5.1}
\]

can hold, even when `clean` includes six distinct labels and noncollinear
source and target triples.  The same is true for $A+A$.

The live parabolic gate is instead the aggregate line energy of the
two-coordinate sets $P^\pm_{w,c}$, restricted to lines with nonzero slope
and three distinct first coordinates.  The squareclass/value-cell theorem
from `THREE_SIDE_INVARIANT_COUPLING_PARABOLIC_SHARPNESS_GATE.md` still gives
the correct $O(m^2\log m)$ ambient range.  What remains is an
endpoint-sensitive estimate for the loads of the lines (4.2).  Raw
difference-set or sumset collinearity cannot supply it.

## 6. Verification

Run:

```bash
python phase2/loop/erdos1208/verify_parabolic_displacement_collinearity_golomb_barrier.py
```
