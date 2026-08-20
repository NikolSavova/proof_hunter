# A single active color kills the standalone parent-energy gate

## 1. Outcome

The critical-range estimate proposed after the colored \(L^2\) reduction,

\[
 \mathfrak A_{L,J}
 \stackrel{?}{\le}m^{o(1)}{k^4\over J^5}
 \qquad(J\ge\sqrt{k}),                              \tag{1.1}
\]

is false, even for integral distance-Sidon graphs of polynomial height and
even when there is only one active normalized color.

For every sufficiently large integer \(n\), there is an integral
distance-Sidon graph with

\[
 \begin{aligned}
 k&=2n^2+8n,\\
 L&=2n>\sqrt{k},\\
 J&=n^2>\sqrt{k},
 \end{aligned}                                      \tag{1.2}
\]

and two selected \(L\)-rich parent patches whose quotient is one child
line of occupancy exactly \(J\).  The two parent supports are disjoint.
For its unique active color,

\[
 \boxed{
 C=1,\qquad K=J,\qquad
 \mathfrak A_{L,J}=1,qquad
 W_{L,J}={J\choose3}.}                              \tag{1.3}
\]

But

\[
 {k^4\over J^5}
 ={16\over n^2}\left(1+{4\over n}\right)^4=o(1),   \tag{1.4}
\]

and the construction has height \(m=k^{O(1)}\), so an \(m^{o(1)}\)
factor cannot repair (1.1).

This is not a counterexample to the desired derivative mass bound.  In
fact

\[
 W_{L,J}=\Theta(J^3)=\Theta(k^3),                   \tag{1.5}
\]

which is exactly target-safe on the formal cube-root critical scale.  The
failure comes from replacing the actual child sixth moment by its worst-case
Szemerédi--Trotter envelope before estimating the parent energy.  In this
example

\[
 \mathfrak B_{L,J}={J\choose3}^2=\Theta(k^6),       \tag{1.6}
\]

whereas the global envelope \(k^3J^3+k^2J^5\) has order \(k^7\).
The lost factor of \(k\) is exactly the false saving demanded in (1.1).

Therefore the surviving colored target must retain either

\[
 \sum_h\sqrt{\mathfrak A_{h,L,J}\mathfrak B_{h,J}} \tag{1.7}
\]

or the equivalent joint color tail

\[
 N_L(C,J)
 \ll m^{o(1)}{(k^3+m^2)^2\over k^3CJ^3}.           \tag{1.8}
\]

The parent energy cannot be bounded at the worst-case child-line scale
independently of how many such child colors actually occur.

## 2. What one parent pair really contributes

Let

\[
 g_-=(d,\lambda,\alpha),\qquad
 g_+=(d+h,\lambda+\mu,\alpha+\mu d+\beta).          \tag{2.1}
\]

For the Heisenberg quotient convention used in the derivative ledger,

\[
 (q,\lambda,\alpha)(q',\lambda',\alpha')
 =
 (q+q',\lambda+\lambda',
  \alpha+\alpha'+\lambda q'),                       \tag{2.2}
\]

one has

\[
 \boxed{g_+g_-^{-1}=(h,\mu,\beta).}                \tag{2.3}
\]

Suppose \(g_-\) and \(g_+\) are selected parent patches and the full child
line \((h,\mu,\beta)\) has tail set \(V\), \(|V|=J\).  The exact colored
derivative mass counts

\[
 {J\choose3}                                        \tag{2.4}
\]

for this parent pair.  There is no requirement that the two parent support
sets intersect, nor that a child triple translate back into either parent
support.

This distinguishes the exact mass from the recursive overlap quantity
\(P_L\).  A term of \(P_L\) begins with a common parent tail triple
\(U\subset S_{g_-}\cap S_{g_+}\) and maps it to a child record.  Such a
term is bounded above by the exact mass, but the reverse implication is
false.  In the construction below,

\[
 S_{g_-}\cap S_{g_+}=\varnothing,                   \tag{2.5}
\]

so the parent pair contributes zero to \(P_L\) and the full amount (2.4)
to \(W_{L,J}\).

Consequently the reverse-preimage bound for a child record decorated by a
translated common triple cannot be applied to every term of the colored
mass.

## 3. The separated-support planting

Fix

\[
 h=7,\qquad d=101,qquad L=2n,qquad J=n^2.          \tag{3.1}
\]

Choose three mutually disjoint collections of directed level pairs:

\[
 \begin{array}{c|c|c}
 \text{family}&\text{shift}&\text{number of pairs}\\ \hline
 \text{child}&h&J\\
 \text{lower parent}&d&L\\
 \text{upper parent}&d+h&L.
 \end{array}                                        \tag{3.2}
\]

All \(2J+4L\) endpoints are distinct.  This can be done inside an interval
of length \(O(J+L)=O(k)\): in a fresh block for shift \(q\), use tails

\[
 B+t(2q+3),\qquad 0\le t<s,                          \tag{3.3}
\]

and the corresponding heads obtained by adding \(q\).

Introduce parameters \(\mu,\beta,\lambda,\alpha\), and one private
variable \(y_e\) for every directed pair in (3.2).  Define \(f\) at the
two endpoints of each pair as follows:

\[
 \begin{array}{c|c}
 \text{family}&f(\text{head})-f(\text{tail})\\ \hline
 \text{child}&\beta+\mu r\\
 \text{lower parent}&\alpha+\lambda r\\
 \text{upper parent}&
  \alpha+\mu d+\beta+(\lambda+\mu)r,
 \end{array}                                        \tag{3.4}
\]

where \(r\) is the tail level, and put \(f(\text{tail})=y_e\).
Because all endpoints are distinct, these prescriptions are consistent.
They give the two parent parameters in (2.1), their common quotient
\((h,\mu,\beta)\), and the intended child line on all \(J\) child tails.
The two parent supports in (3.2) are disjoint by construction.

## 4. Polynomial-height distance-Sidon specialization

The formal construction in Section 3 has an integral specialization of
polynomial height satisfying all of the following simultaneously:

1. every unordered squared Euclidean distance is distinct;
2. each of the two selected parent lines has exactly its intended \(L\)
   tails;
3. the child line has exactly its intended \(J\) tails;
4. \(\mu\ne0\), so the child line is nonhorizontal.

Here is a direct polynomial-avoidance proof.  Every vertex belongs to one
private directed pair \(e\), and its second coordinate has the form

\[
 y_e+\epsilon P_e,qquad \epsilon\in\{0,1\},        \tag{4.1}
\]

where \(P_e\) is one of the three affine forms in (3.4).

For two distinct unordered point pairs, equality of squared distances is
a polynomial of degree at most two.  It is not the zero polynomial:

- if the two point pairs use different private occurrence pairs, a private
  variable \(y_e\) survives in the quadratic or linear part;
- if they use the same two occurrence pairs, comparison of the private
  variables reduces identity to equality up to sign of the corresponding
  endpoint offsets;
- the forms \(P_e\) are nonzero and no two distinct forms are equal up to
  sign.  Within one family this follows from their distinct tail levels;
  between families it follows from the independent \(\alpha\) or \(\beta\)
  coefficient.

The fixed horizontal-coordinate term cannot cancel the surviving variable
coefficient.  Thus every unwanted distance equality is a proper
hypersurface.

Likewise, an unintended incidence on one of the three derivative lines is
a nonzero linear polynomial.  A cross-occurrence candidate retains a
private \(y_e-y_{e'}\); a prescribed occurrence on the wrong line has a
different affine form \(P_e\).

There are \(O(k^4)\) forbidden polynomials, all of degree at most two.
Choose every parameter from an integer box of side larger than twice their
number.  The elementary Schwartz--Zippel union bound gives a simultaneous
integral specialization avoiding all of them.  Since the level interval is
\(O(k)\) and every value in (3.4) is affine with coefficients \(O(k)\), the
resulting graph lies in a square of side

\[
 m=k^{O(1)}.                                         \tag{4.2}
\]

A common vertical translation makes all coordinates positive without
changing any derivative line or distance.

## 5. Exact colored statistics

Select only the two parent patches in (2.1).  Their shifts differ, so they
determine one canonical affine projection line with

\[
 \theta={\mu\over h},qquad
 B=\beta-{\mu h\over2}.                              \tag{5.1}
\]

There is one oriented parent pair of this color and the child occupancy is
exactly \(J\).  Hence (1.3) follows.

For \(n>4\),

\[
 L^2=4n^2>2n^2+8n=k,                                \tag{5.2}
\]

and certainly \(J\ge\sqrt{k}\) for all sufficiently large \(n\).  Finally,
(1.4) proves that (1.1) fails by \(n^{2-o(1)}\).

The correct joint tail is sharp instead.  There is exactly one
\((C,J)=(1,n^2)\) color, and

\[
 CJ^3N_L(C,J)=J^3=\Theta(k^3).                       \tag{5.3}
\]

Thus the construction sits precisely at the allowable critical mass rather
than exceeding it.

## 6. Finite exact certificate

The verifier uses

\[
 n=20,quad L=40,quad J=400,quad k=960.            \tag{6.1}
\]

It deterministically specializes (3.4) and checks all
\({960\choose2}=460320\) squared distances.  It also checks exact parent
and child supports, disjointness of the parent supports, the quotient and
normalized-color signs, and

\[
 \mathfrak A_{L,J}=1>
 {960^4\over400^5}=0.082944.                         \tag{6.2}
\]

Run

    python phase2/loop/erdos1208/verify_single_active_color_parent_energy_gate_barrier.py

The conclusion is a correction to the proof target, not a resolution of
Erdős 1208: retain the actual child sixth moment or the joint \((C,J)\)
tail.  Do not ask the active parent energy to pay the hypothetical maximum
number of rich child colors when only one exists.
