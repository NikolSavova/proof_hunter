# An exact four-direction lower construction for Erdős #669 at \(k=4\)

## Theorem

For every integer \(q\ge2\), there is a set of \(14q\) points in the real
projective plane that spans at least \(7q^2\) lines containing exactly four of
the points. Consequently,

\[
f_4(n)\ge \frac{n^2}{28}-O(n)
\quad\text{and}\quad
F_4(n)\ge \frac{n^2}{28}-O(n).
\]

Because a finite projective point set can be moved into an affine chart by a
projective transformation, the same statement holds in \(\mathbb R^2\).

## Construction in the dual plane

Take the following \(14q\) distinct projective lines, displayed in an affine
chart:

\[
\begin{array}{lll}
H_i: y=i,       &0\le i<3q, &\text{(3q) horizontal lines},\\
V_j: x=j,       &0\le j<3q, &\text{(3q) vertical lines},\\
D^-_c:x-y=c,    &-2q\le c<2q, &\text{(4q) lines},\\
D^+_d:x+y=d,    &q-1\le d<5q-1, &\text{(4q) lines}.
\end{array}
\]

At a grid point \((j,i)=V_j\cap H_i\), exactly one line of each diagonal
family passes through it. Hence it is a vertex of multiplicity exactly four if
and only if

\[
-2q\le j-i<2q
\quad\text{and}\quad
q-1\le i+j<5q-1.
\tag{1}
\]

No fifth arrangement line can pass through such a point: within each of the
four parallel families, a finite point is on at most one line.

## Exact count

There are \(9q^2\) grid points before imposing (1). The rejected points form
four disjoint corner triangles.

For the difference constraint, the two rejection counts are

\[
\sum_{s=1}^{q-1}s=\frac{q(q-1)}2,
\qquad
\sum_{s=1}^{q}s=\frac{q(q+1)}2,
\]

and therefore total \(q^2\). The sum constraint rejects another two disjoint
triangles of the same sizes, hence another \(q^2\) points. Thus precisely

\[
9q^2-q^2-q^2=7q^2
\]

finite vertices have multiplicity four.

Upon projective completion, each parallel family meets at its direction point
at infinity. Those four points have multiplicities \(3q,3q,4q,4q\). For
\(q\ge2\), none has multiplicity four, so the complete projective arrangement
still has exactly \(7q^2\) fourfold vertices. (When \(q=1\), the two diagonal
direction points are two extra fourfold vertices; this is why the theorem was
stated for \(q\ge2\).)

Projective duality now sends the \(14q\) arrangement lines to \(14q\) points
and the \(7q^2\) fourfold vertices to \(7q^2\) lines containing exactly four
dual points. Choose a new line at infinity avoiding the finite dual point set,
then send it to infinity by a projective transformation. All dual points
become affine, no determined line is lost, and every incidence multiplicity is
preserved. This proves the subsequence bound

\[
f_4(14q)\ge7q^2=\frac{(14q)^2}{28}.
\]

For arbitrary \(n\), take \(q=\lfloor n/14\rfloor\), dualize the construction,
and add the remaining \(n-14q\) points generically. There are only finitely many
forbidden lines and incidences at each addition, so the new points can be chosen
not to lie on any of the certified four-point lines and not to create unwanted
coincidences with them. All \(7q^2\) certified lines remain exactly four-rich.
Since \(q=n/14+O(1)\), the claimed \(n^2/28-O(n)\) bound follows.

## Why \(3:3:4:4\)?

This is a continuous optimization of the classical four-direction grid
truncation. Give the horizontal and vertical families normalized widths \(a\)
each and the two diagonal families widths \(c\) each, with
\(2a+2c=1\). Center all four intervals. In the regime \(a\le c\le2a\), the
normalized density of fourfold grid vertices is the square area minus its four
clipped corners:

\[
\Phi(a)=a^2-2\left(a-\frac c2\right)^2
=a^2-2\left(\frac{3a}{2}-\frac14\right)^2,
\qquad c=\frac12-a.
\]

Differentiating gives

\[
\Phi'(a)=\frac32-7a,
\]

so the optimum in this symmetric centered family is

\[
a=\frac3{14},\qquad c=\frac2{7}=\frac4{14},
\qquad \Phi(a)=\frac1{28}.
\]

Palásti's 1986 truncation uses the ratio \(1:1:3/2:3/2\), whose normalized
coefficient is \(7/200\). The ratio \(3:3:4:4\) above gives \(1/28\), a relative
gain of \(50/49-1=1/49\), approximately \(2.04\%\).

This optimization is **not new**. A Chinese orchard-problem page by Zhao Hui Du,
first committed on 2019-10-20, describes deleting the unproductive corner
diagonals to obtain an octagonal arrangement with \(14m+O(1)\) lines and
\(7m^2+O(m)\) fourfold points. Its displayed conclusion \(n^2/24+O(n)\) is an
arithmetic typo: the two preceding counts give \(n^2/28+O(n)\). The theorem
above supplies explicit intercept sets, an exact \(7q^2\) count, projective
bookkeeping, and a machine check for that prior asymptotic construction.

The continuous optimization is offered only as an explanation of the
parameters. The integer theorem rests on the exact count above, not on a
limiting-area argument.

## A general upper bound from Melchior

Let \(t_r\) be the number of vertices incident with exactly \(r\) lines in a
non-pencil arrangement of \(n\) real projective lines. Pair counting and
Melchior's inequality say

\[
\binom n2=\sum_{r\ge2}\binom r2t_r,
\qquad
t_2\ge3+\sum_{r\ge4}(r-3)t_r.
\]

For fixed \(k\ge4\), the weight

\[
w(r)=\binom r2+r-3
\]

is increasing for \(r\ge k\). Therefore

\[
\binom n2
\ge 3+\sum_{r\ge k}\left(\binom r2+r-3\right)t_r
\ge3+\left(\binom k2+k-3\right)\sum_{r\ge k}t_r.
\]

Dualizing back to points yields

\[
F_k(n)\le
\max\left\{1,\frac{\binom n2-3}{\binom k2+k-3}\right\}
=\frac{n^2}{(k-2)(k+3)}+O(n).
\]

For \(k=4\), the non-pencil term is
\((\binom n2-3)/7=n^2/14+O(n)\). The outer maximum accounts for a pencil,
which has one rich point/line.

This general upper bound is included to sharpen the window, not as a novelty
claim. For \(k\ge5\), Shnurnikov's stronger published arrangement inequality
improves the asymptotic denominator further to \(k^2+3k-15\); see
PRIOR_ART.md. It does not improve the \(k=4\) bound used here.

## Verification

Run:

```bash
python3 verify_four_direction.py --max-q 20
```

The script uses exact integer projective coordinates. It verifies by two
independent routes:

1. the closed-form grid predicate has exactly \(7q^2\) solutions;
2. all pairwise line intersections are canonicalized, their complete
   multiplicities are enumerated, every certified point has multiplicity exactly
   four, the pair identity holds, and Melchior's inequality holds.

It also exhaustively checks the one-parameter centered symmetric family at
budgets \(14q\), confirming that \(3q:3q:4q:4q\) maximizes the certified core
count within that discrete family for the tested range.
