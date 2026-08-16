# The beta/hull-diagonal route: exact identities and a formal barrier

## Verdict

The two natural bivariate identities are exact and useful, but they do **not**
by themselves force either of the estimates wanted for Erdős 838.  More
precisely, for every \(n\geq 5\) there is a nonnegative integral coefficient
table \(g_{h,i}\), with the correct general-position rows in hull sizes
\(0,1,2\) and the correct total number \(\binom n3\) of triples, which satisfies
coefficientwise

\[
G(x,1+x)=(1+x)^n
\]

and the complete planar beta/reflection identity below, but has

\[
\frac{G_x(1,1)}{G(1,1)}=4-O(n^{-1}),\qquad
\frac{nG(1/2,1)}{G(1,1)}=\frac n{16}+O(1).
\]

Thus the hull diagonal, even supplemented by every coefficient of the
Bernoulli beta identity, cannot supply the missing internal-mass term.  A
successful argument must insert genuinely planar positive information not
visible to these identities: for example a cap/cup endpoint product, a
tangent-rectangle count, or at minimum the first Erdős--Szekeres consequence
that nine points contain a convex pentagon.

The table below is deliberately a **formal coefficient table**, not a
realizable order type.  For \(n\geq 9\) it has \(v_5=0\), so the convex-pentagon
theorem immediately excludes realizability.  That is the point of the
construction: it identifies exactly what the analytic diagonal data omit.

## 1. The exact hull diagonal

For a planar point set \(P\) in general position put

\[
G_P(x,y)=\sum_{K\ {\rm in\ convex\ position}}
              x^{|K|}y^{i_P(K)},
\]

where \(i_P(K)=|\operatorname{conv}(K)\cap(P\setminus K)|\).  Every subset
\(A\subseteq P\) has a unique set \(K\) of vertices of its convex hull, and
then

\[
K\subseteq A\subseteq K\cup
  \bigl(\operatorname{conv}(K)\cap(P\setminus K)\bigr).
\]

Consequently the Boolean lattice is partitioned into the intervals indexed
by \(K\), and weighting every selected point by \(x\) gives

\[
\boxed{G_P(x,1+x)=(1+x)^n.}\tag{1}
\]

In particular \(G_P(1,2)=2^n\).  The target rank polynomial is
\(Z_P(s)=G_P(s,1)\), so

\[
V(P)=G_P(1,1),\qquad
\mu(P)=\frac{G_{P,x}(1,1)}{G_P(1,1)}.
\]

## 2. The exact beta identity, including the singleton correction

Let \(R\subseteq P\) retain each point independently with probability \(p\).
A convex-position set \(K\) is closed and free in the restricted convex
geometry exactly when every point of \(K\) is retained and every ambient
point inside \(\operatorname{conv}(K)\) is omitted.  Hence the expected
alternating free-set sum is

\[
\sum_K(-1)^{|K|-1}|K|p^{|K|}(1-p)^{i_P(K)}
  =pG_{P,x}(-p,1-p).
\]

Gordon's planar beta theorem identifies this alternating sum with the number
of interior points when the restriction has at least two elements.  A
one-point restriction contributes one to the free-set sum but has no interior
point.  Therefore the exact expectation is

\[
\boxed{
pG_{P,x}(-p,1-p)
=\mathbb E\,i_R(R)+np(1-p)^{n-1}.
}\tag{2}
\]

In particular

\[
0\le pG_{P,x}(-p,1-p)\le np,
\]

because \(i_R(R)+{\bf1}_{|R|=1}\le |R|\).

The expected number of vertices of \(\operatorname{conv}(R)\) can be read
from (1).  With \(q=p/(1-p)\), it is

\[
(1-p)^nqG_{P,x}(q,1+q).
\]

Since every nonempty restricted set is the disjoint union of its hull
vertices and interior points, (2) gives the full reflection identity

\[
\boxed{
G_{P,x}(-p,1-p)
+(1-p)^{n-1}G_{P,x}\!\left(\frac p{1-p},
                          \frac1{1-p}\right)
=n+n(1-p)^{n-1}.
}\tag{3}
\]

Thus the formal barrier below satisfies not merely the inequality from beta,
but every coefficient of the exact equality (3).

## 3. An explicit nonnegative integral countertable

Write \(g_{h,i}=[x^hy^i]G(x,y)\).  Fix

\[
g_{0,0}=1,\qquad g_{1,0}=n,\qquad
g_{2,0}=\binom n2,
\]

put all coefficients with \(h\geq5\) equal to zero, and define
\(a_i=g_{3,i}\), \(c_i=g_{4,i}\) as follows.

If \(n=2m\), let

\[
a_i=
\begin{cases}
n+4(m-2-i)(m-1-i),&0\leq i\leq m-2,\\
0,&m-1\leq i\leq n-3.
\end{cases}\tag{4e}
\]

If \(n=2m+3\), let

\[
a_i=
\begin{cases}
n-1+4(m-i)^2,&0\leq i<m,\\
(n-1)/2,&i=m,\\
0,&m<i\leq n-3.
\end{cases}\tag{4o}
\]

Finally set

\[
c_i=\sum_{j=0}^i
   \left(a_j-\binom{n-j-1}{2}\right),
\qquad 0\leq i\leq n-4. \tag{5}
\]

These numbers are nonnegative integers for every \(n\geq5\).

### Nonnegativity

Once the nonzero part of \(a\) ends, (5) telescopes to

\[
c_i=\binom{n-i-1}{3}>0.
\]

On the initial part the increments
\(a_i-\binom{n-i-1}{2}\) are first nonnegative and then nonpositive, so the
running sum has no interior minimum.  Its two relevant endpoint values are
positive: the right one is covered by the displayed binomial formula, while
at the left endpoint the value is

\[
c_0=2m^2-7m+7
\]

in the even case (with the finitely small cases checked directly) and

\[
c_0=2m^2-m+1
\]

in the odd case.  The exact verifier checks every row directly as an
additional safeguard.

### The hull diagonal

Let \(h_i=\binom{n-i-1}{2}\).  Polynomial division gives

\[
\frac{y^n-1-n(y-1)-\binom n2(y-1)^2}{(y-1)^3}
=\sum_{i=0}^{n-3}h_i y^i.
\]

Equation (5) is precisely

\[
a_i=h_i-c_i+c_{i-1},\qquad c_{-1}=c_{n-3}=0.
\]

Substitution proves (1) coefficientwise.  In particular
\(\sum_i a_i=\binom n3\), so the table has the correct number of triples.

### The beta reflection

After the hull-diagonal recurrence is substituted into (3), its remaining
conditions are exactly the reflection-pair identities

\[
a_i+a_{n-3-i}
=n+4t(t+1),\quad t=m-2-i
\]

for \(n=2m\), and

\[
a_i+a_{n-3-i}
=n-1+4t^2,\quad t=m-i,
\]

with \(2a_m=n-1\), for \(n=2m+3\).  Formulas (4e)--(4o)
place the entire required pair mass on the lower-index member (and split the
odd central pair evenly), so (3) follows coefficientwise.

## 4. Why the desired conclusion fails

Summing the explicit table gives

\[
v_4=\frac{n^4}{48}+O(n^3),\qquad
V=G(1,1)=\frac{n^4}{48}+O(n^3).
\]

All other positive-rank mass is in ranks at most three.  It follows that

\[
\mu=\frac{\sum_h hv_h}{\sum_hv_h}
=4-O(n^{-1}).
\]

Similarly the rank-four contribution dominates at activity \(1/2\):

\[
\frac{nG(1/2,1)}{G(1,1)}
=\frac n{16}+O(1).
\]

Thus neither \(\mu\geq\log_2n-o(\log n)\) nor subpolynomial half weight can
be inferred from (1) and (3), even with nonnegative integral coefficients and
the complete rank-\(\leq3\) skeleton.

## 5. Stress against realizable configurations

The verifier also enumerates all convex-position subsets of three exact
planar examples and checks (1) and (3) coefficientwise.

| configuration | \(n\) | \(V\) | mean rank | sampled range of beta/\(np\) |
|---|---:|---:|---:|---:|
| central Pascal \(T(4,2)\) | 6 | 51 | \(44/17\) | \(0.1042\) to \(0.7244\) |
| central Pascal \(T(5,2)\) | 10 | 376 | \(165/47\) | \(0.1184\) to \(0.5608\) |
| saved dyadic cliff | 17 | 2830 | \(12229/2830\) | \(0.1984\) to \(0.8118\) |

The beta upper bound therefore has comfortable slack on the known hard
profiles; treating it as nearly tight would lose precisely the information
needed in the low-mean branch.

## 6. The exact remaining gate

The atomic all-interval identity controls how a fixed hull owns its internal
Boolean cube, but it does not say that abundant internal mass creates
compatible **positive endpoint continuations**.  The countertable stores
quadratically and quartically many abstract faces while suppressing every
rank-five face, which no planar order type can do.

Accordingly, a viable continuation of this route needs a positive planar
inequality of one of the following forms:

1. an endpoint-polynomial inequality converting internal mass
   \(y\partial_yG\) into cap-before-cup or cup-before-cap products;
2. a tangent-pocket inequality forcing enough rank-\((h+1)\) faces from a
   large block of rank-\(h\) faces; or
3. a quantitative, rank-window version of Erdős--Szekeres strong enough to
   rule out the formal rank-four concentration with only \(n^{o(1)}\) loss.

Any consequence using only coefficient nonnegativity and evaluations or
derivatives of the two identities on their displayed curves is defeated by
this table.  Of course an additional planar inequality can itself be stated
in terms of \(G\); the point is that it will not follow from the two diagonal
identities.  To improve the known quarter exponent rather than merely recover
it, the missing term should distinguish cyclic endpoint patterns among faces
with the same pair \((h,i)\).

The ordinary Erdős--Szekeres hierarchy illustrates the distinction.  If
\(N(k)\) points always contain \(k\) in convex position, double counting
\(N(k)\)-subsets gives the valid positive coefficient inequality

\[
v_k\binom{n-k}{N(k)-k}\geq\binom n{N(k)},\qquad
v_k\geq\frac{\binom nk}{\binom{N(k)}k}. \tag{6}
\]

This already excludes the formal table (take \(N(5)=9\)), but with
\(N(k)=2^{k+o(k)}\) its optimization is the familiar quarter-exponent scale.
Thus a scalar rank-window constraint obtained only by applying
Erdős--Szekeres independently inside subsets does not close the gap either;
one needs compatibility or multiplicity across the endpoint continuations.

## 7. Verification

Run

    python3 phase2/loop/erdos838/agent_cyclic_stem_hw/beta_hull_constraints.py

The script:

- verifies both polynomial identities coefficientwise for every
  \(5\leq n\leq64\) and for \(n=80,96,128,192,256\);
- derives and audits the affine constraint system by exact rational RREF;
- checks nonnegativity, integrality, the mean and half-weight bounds;
- enumerates the three realizable stress configurations; and
- writes beta_hull_constraints_certificate.json, including complete formal
  tables for \(n=12\) and \(n=20\).

No floating-point arithmetic is used for any identity or inequality.
