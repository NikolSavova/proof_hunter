# The lattice-zonotope construction for exact \(k\)-fold vertices

## Status and claim discipline

This note gives a self-contained construction theorem and identifies its exact
finite multiplicity count.  It also optimizes the construction, first for a
fixed set of directions and then over direction sets for \(4\leq k\leq 11\).

The determinant minimization is **not new**: its small values are the minimum
areas of convex lattice \(2k\)-gons computed by R. J. Simpson in 1990.  The
connection of those polygons to the orchard problem, and the resulting lower
coefficients beyond \(k=4\), have not yet received a sufficient literature audit.
Accordingly, the comparisons with Palásti below mean only "larger than the
coefficient printed in Palásti's 1986 paper," not "new state of the art."

## 1. Exact construction theorem

Let \(k\geq 3\), and let

\[
V=\{v_1,\ldots,v_k\}\subset\mathbb Z^2
\]

be primitive, pairwise nonparallel vectors which generate \(\mathbb Z^2\) as an
abelian group.  Write \(R(a,b)=(-b,a)\), and set

\[
 Z=\sum_{i=1}^k[0,Rv_i],\qquad
 D=\sum_{1\leq i<j\leq k}|\det(v_i,v_j)|.
\tag{1}
\]

For each \(i\), put

\[
 m_i=\min_{x\in Z}v_i\mathbin\cdot x,
 \quad M_i=\max_{x\in Z}v_i\mathbin\cdot x,
 \quad w_i=M_i-m_i.
\tag{2}
\]

All these numbers are integers.  For an integer \(q\geq1\), form the projective
line arrangement whose affine members are

\[
 \mathcal A_q(V)=
 \{v_i\mathbin\cdot x=t:
       i=1,\ldots,k,\; qm_i\leq t\leq qM_i,\;t\in\mathbb Z\}.
\tag{3}
\]

### Theorem 1

The arrangement (3) has

\[
 n_q=2Dq+k
\tag{4}
\]

distinct lines.  Its finite vertices of multiplicity exactly \(k\) are
precisely the lattice points of \(qZ\), and hence their number is

\[
 t_k^{\rm fin}(\mathcal A_q(V))
   =|qZ\cap\mathbb Z^2|
   =Dq^2+kq+1.
\tag{5}
\]

For \(q\geq2\), no point at infinity has multiplicity \(k\), so (5) is also the
exact number of projective \(k\)-fold vertices.  Consequently

\[
 f_k(n)\geq \frac{n^2}{4D}-O_k(n).
\tag{6}
\]

On the subsequence \(n=n_q\), the slightly sharper exact relation is

\[
 t_k(\mathcal A_q(V))
 =\frac{n_q^2}{4D}+1-\frac{k^2}{4D}
 \qquad(q\geq2).
\tag{7}
\]

### Proof: area, widths, and line count

The two-dimensional zonotope area formula gives

\[
 \operatorname{area}(Z)
 =\sum_{i<j}|\det(Rv_i,Rv_j)|=D.
\tag{8}
\]

The width in (2) is additive under Minkowski sums, so

\[
 w_i=\sum_{j=1}^k|v_i\mathbin\cdot Rv_j|
     =\sum_{j=1}^k|\det(v_i,v_j)|.
\tag{9}
\]

It follows that \(\sum_iw_i=2D\).  Family \(i\) contains exactly
\(qw_i+1\) integer levels, proving (4).  Pairwise nonparallelity makes lines
from different families distinct, and distinct levels in one family are
obviously distinct.

### Proof: identification of every finite \(k\)-fold vertex

A finite point lies on at most one line from each of the \(k\) parallel
families.  It therefore has multiplicity \(k\) if and only if it lies on one
line from every family.  The latter condition says

\[
 v_i\mathbin\cdot x\in\mathbb Z,
 \qquad qm_i\leq v_i\mathbin\cdot x\leq qM_i
 \quad(1\leq i\leq k).
\tag{10}
\]

Because the \(v_i\) generate \(\mathbb Z^2\), their dual lattice is also
\(\mathbb Z^2\): the integrality conditions in (10) are equivalent to
\(x\in\mathbb Z^2\).  The edges of \(Z\) are translates of the segments
\([0,Rv_i]\), two for each \(i\), so its supporting facet normals are exactly
the directions \(\pm v_i\).  Thus the inequalities in (10) are exactly the
supporting-half-plane description of \(qZ\).  This proves

\[
 \{\text{finite }k\text{-fold vertices}\}=qZ\cap\mathbb Z^2.
\tag{11}
\]

This is an equality, not merely a certified subset; in particular there are no
unaccounted rational \(k\)-fold vertices.

### Proof: Pick--Ehrhart count

The polygon \(Z\) is an integral zonogon of area \(D\).  Each primitive
generator \(Rv_i\) occurs as two boundary edge vectors, so the number of
lattice intervals on its boundary is \(B(Z)=2k\).  Pick's theorem, or the
two-dimensional Ehrhart polynomial, now gives

\[
 |qZ\cap\mathbb Z^2|
 =\operatorname{area}(Z)q^2+\frac{B(Z)}2q+1
 =Dq^2+kq+1,
\]

which proves (5).

### Proof: points at infinity

The lines of family \(i\) meet at one direction point at infinity, of
multiplicity \(qw_i+1\).  The \(k\) direction points are distinct.  Since every
nonzero determinant in (9) is a positive integer,

\[
 w_i\geq k-1.
\]

Hence \(qw_i+1>k\) for \(q\geq2\).  No infinity point is then exactly
\(k\)-fold.  When \(q=1\), family \(i\) contributes one additional projective
\(k\)-fold point precisely when \(w_i=k-1\); this is the only exception.

### Proof: duality, affine chart, and padding

Projective duality sends the \(n_q\) arrangement lines to \(n_q\) points and
each exactly \(k\)-fold vertex to a line containing exactly \(k\) dual points.
Choose a projective line avoiding the finite dual point set and declare it to be
the new line at infinity.  All dual points are then affine, and no counted line
is lost because every counted line contains \(k\) dual points.  Incidence
multiplicities are preserved.

For arbitrary sufficiently large \(n\), choose

\[
 q=\left\lfloor\frac{n-k}{2D}\right\rfloor
\]

and add the fewer than \(2D\) remaining points one at a time.  At each step,
choose the new point outside the finite union of all lines determined by two
current points.  No old exactly \(k\)-rich line gains a point.  Equations (6)
and (7) follow.

## 2. Sublattice correction

The spanning hypothesis in Theorem 1 is convenient but must not be silently
dropped.  For general primitive pairwise nonparallel \(V\), let

\[
 L=\langle v_1,\ldots,v_k\rangle_{\mathbb Z},\qquad
 h=[\mathbb Z^2:L]
   =\gcd_{i<j}|\det(v_i,v_j)|.
\tag{12}
\]

The common-level points form the dual lattice
\(L^*=\{x:v_i\cdot x\in\mathbb Z\ \forall i\}\), whose covolume is \(1/h\).
The exact finite \(k\)-fold vertices are \(qZ\cap L^*\).  Thus

\[
 t_k^{\rm fin}=hDq^2+O(q),\qquad n_q=2Dq+k,
\tag{13}
\]

and the asymptotic coefficient is

\[
 \frac{h}{4D}=\frac1{4(D/h)}.
\tag{14}
\]

The factor \(h\) is essential; counting only ordinary integer points would miss
valid rational concurrence points.

This correction does not improve the optimum below.  Choose a lattice basis
matrix \(A\) for \(L\), with \(|\det A|=h\), and write \(v_i=Au_i\).  Then the
\(u_i\in\mathbb Z^2\) generate \(\mathbb Z^2\), and

\[
 \frac Dh=\sum_{i<j}|\det(u_i,u_j)|.
\tag{15}
\]

The right side is the area of the lattice zonogon
\(\sum_i[0,Ru_i]\), which has \(2k\) vertices.  Hence allowing a proper
sublattice merely changes coordinates; it cannot beat the minimum-area lattice
\(2k\)-gon bound.

## 3. Optimality for fixed directions

The zonotope window is optimal among all interval truncations of the same
direction families.  Indeed, let \(Q\) be the bounded intersection of limiting
strips

\[
 a_i\leq v_i\mathbin\cdot x\leq b_i.
\]

After dilation, its common vertices have leading count
\(h\operatorname{area}(Q)q^2\), while the number of lines has leading term at
least \(q\sum_i w_Q(v_i)\).  Mixed area satisfies

\[
 2V(Q,Z)=\sum_i w_Q(v_i).
\tag{16}
\]

Minkowski's mixed-area inequality gives

\[
 V(Q,Z)^2\geq\operatorname{area}(Q)\operatorname{area}(Z)
 =D\operatorname{area}(Q).
\]

Therefore every such interval truncation has coefficient at most \(h/(4D)\),
with equality when \(Q\) is homothetic to \(Z\).  Thus (3) is not an arbitrary
window: it is the optimal one for the chosen directions.

## 4. Minimizing the determinant sum

Let \(a(2k)\) be the minimum area of a strictly convex lattice polygon with
\(2k\) vertices.  Simpson computed \(a(2k)\) through \(k=11\).  Equations
(14)--(15) imply that the best coefficient in the lattice-zonotope construction
is at most \(1/(4a(2k))\).  Equality holds for Simpson's centrally symmetric
minimizers, whose successive primitive generator directions can be taken as

\[
\begin{split}
 &(0,1),(1,1),(1,2),(1,3),(1,4),(2,5),\\
 &(1,5),(2,7),(1,6),(2,9),(1,7).
\end{split}
\tag{17}
\]

Taking the first \(k\) vectors gives the following exact data.

| \(k\) | \(D=a(2k)\) | zonotope coefficient \(1/(4D)\) | Palásti 1986 | comparison |
|---:|---:|---:|---:|:---|
| 4 | 7 | \(1/28=0.0357143\) | \(7/200=0.035\) | larger, but \(1/28\) is known online prior art |
| 5 | 14 | \(1/56=0.0178571\) | \(2/135=0.0148148\) | larger than Palásti's table |
| 6 | 24 | \(1/96=0.0104167\) | \(47/4860=0.00967078\) | larger than Palásti's table |
| 7 | 40 | \(1/160=0.00625\) | \(3/490=0.00612245\) | larger than Palásti's table |
| 8 | 59 | \(1/236=0.00423729\) | \(1/270=0.00370370\) | larger than Palásti's table |
| 9 | 87 | \(1/348=0.00287356\) | \(3/1000=0.003\) | smaller |
| 10 | 121 | \(1/484=0.00206612\) | \(1/480=0.00208333\) | smaller |
| 11 | 164 | \(1/656=0.00152439\) | \(1/750=0.00133333\) | larger than Palásti's table |

For \(k=4\), the widths from (9) are \(3,4,3,4\), so this recovers the
\(3:3:4:4\) octagonal construction and its coefficient \(1/28\).  For example,
the \(k=5\) construction has widths \(4,7,5,5,7\), hence \(28q+5\) lines and
exactly \(14q^2+5q+1\) finite fivefold vertices.

The primary sources are:

- R. J. Simpson, ["Convex lattice polygons of minimum
  area"](https://doi.org/10.1017/S0004972700028525), *Bull. Austral. Math.
  Soc.* **42** (1990), 353--367.  Table 2 gives
  \(a(2k)=1,3,7,14,24,40,59,87,121,164\) for \(2\leq k\leq11\).
- Ilona Palásti, ["A construction for arrangements of lines with vertices of
  large multiplicity"](https://real-j.mtak.hu/5463/1/StudScientMath_21.pdf),
  *Studia Sci. Math. Hungar.* **21** (1986), 67--78.  The comparison column is
  transcribed from the table on p. 77.

There is also a clean all-\(k\) description even though there is no elementary
closed formula for the numbers \(a(2k)\): the best coefficient in this entire
scheme is exactly

\[
 c_k^{\rm zono}=\frac1{4a(2k)}.
\tag{18}
\]

I. Bárány and N. Tokushige proved that

\[
 \gamma=\lim_{m\to\infty}\frac{a(m)}{m^3}
\]

exists.  Therefore

\[
 c_k^{\rm zono}\sim\frac1{32\gamma}\,k^{-3}.
\tag{19}
\]

Their finite optimization strongly suggests
\(\gamma\approx0.0185067387\), which would make the constant in (19)
approximately \(1.68857\); the numerical value is not proved to be the exact
one.  See I. Bárány and N. Tokushige, ["The minimum area of convex lattice
\(n\)-gons"](https://doi.org/10.1007/s00493-004-0012-0), *Combinatorica*
**24** (2004), 171--185.

## 5. What is and is not established

The theorem rigorously gives an all-\(k\) quadratic construction, and Simpson's
table rigorously optimizes this particular lattice/parallel-family scheme for
\(k\leq11\).  It does **not** optimize over arbitrary real line arrangements and
does not prove existence of the limits in Erdős #669.

The apparent improvements over Palásti for \(k=5,6,7,8,11\) require a dedicated
post-1986 citation search before being presented as new.  The caution is concrete:
the \(k=4\) coefficient \(1/28\), although absent from Palásti's table, already
appears asymptotically on Zhao Hui Du's 2019 orchard-problem page.  At present the
safe claim is that the zonotope theorem independently derives and exactly verifies
these coefficients and exposes their connection to minimum-area lattice polygons.
