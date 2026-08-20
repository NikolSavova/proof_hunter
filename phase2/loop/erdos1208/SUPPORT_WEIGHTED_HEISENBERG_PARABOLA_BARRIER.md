# Support-weighted Heisenberg mass: quadratic normalization and sharp parabola barrier

## 1. Outcome

The support-weighted Heisenberg quantity

\[
 W_L=\sum_g
 r^+_{\Gamma_L\Gamma_L^{-1}}(g){K_g\choose3}          \tag{1.1}
\]

cannot in general be bounded by
\(m^{o(1)}(k^3+m^2)\).  The integer parabola is a genuine
distance-Sidon counterexample to that proposed scale.

For every \(L\), take

\[
 A_L=\{(r,r^2):0\le r<2L\}.                            \tag{1.2}
\]

This is distance-Sidon for every \(L\), not merely for the sizes checked
computationally.  In the dyadic band consisting of derivative shifts
\(1\le q\le L\), the line occupancies range from \(L\) to \(2L-1\), and

\[
 T_L
 =\sum_{s=L}^{2L-1}{s\choose3}
 ={2L\choose4}-{L\choose4}
 =\Theta(L^4).                                        \tag{1.3}
\]

However the exact weighted mass is

\[
 \boxed{
 W_L=\sum_{h=1}^{L-1}(L-h){2L-h\choose3}
 =\Theta(L^5).}                                       \tag{1.4}
\]

The set (1.2) lies in a square of side

\[
 m=(2L-1)^2+1=\Theta(L^2),
\]

so

\[
 k^3+m^2=\Theta(L^4),\qquad
 W_L=\Theta\left({(k^3+m^2)^2\over k^3}\right).        \tag{1.5}
\]

Thus \(W_L\) can exceed \(k^3+m^2\) by a factor \(\Theta(k)\), while
Erdos #1208 itself remains at the correct \(m^2\) scale.  The parabola
also has reverse multiplicity \(L-1=\Theta(k)\), realized by one long
coherent quadratic parameter block.

This changes the target.  Since the tail-triple second moment gives

\[
 {T^2\over k^3}\lesssim P\le W,                       \tag{1.6}
\]

the correct sufficient weighted estimate is

\[
 \boxed{
 W\le m^{o(1)}{(k^3+m^2)^2\over k^3},}                \tag{1.7}
\]

not \(W\le m^{o(1)}(k^3+m^2)\).  The parabola shows that (1.7), if true,
would be sharp up to subpolynomial factors.

There is also an exact normalization behind this example.  On any affine
shift--slope block

\[
 \lambda_q=\theta q+\eta,                              \tag{1.8}
\]

subtracting the coherent quadratic term converts child-line occupancies
into ordinary difference multiplicities of a transformed graph.  The
weighted Heisenberg problem on such a block is therefore an additive
popular-difference correlation, with the parabola degenerating to a
one-dimensional arithmetic progression.  This is the right framework for
a support-sensitive incidence theorem.

## 2. Quadratic normalization of an affine parameter block

Let a patch have parameters \((q,\lambda_q,\alpha_q)\), and suppose the
chosen parameter block satisfies (1.8).  Define

\[
 F(r)=f(r)-{\theta\over2}r^2,\qquad
 A_q=\alpha_q-{\theta\over2}q^2.                       \tag{2.1}
\]

For patches at shifts \(c,d\), put \(h=c-d\).  Their child quotient has
slope \(\theta h\) and intercept

\[
 \beta_{c,d}
 =\alpha_c-\alpha_d-\theta(c-d)d.                     \tag{2.2}
\]

On every tail \(t\) of that child line,

\[
\begin{aligned}
 F(t+h)-F(t)
 &=d_h(t)-\theta ht-{\theta\over2}h^2\\
 &=\beta_{c,d}-{\theta\over2}h^2\\
 &=A_c-A_d.                                           \tag{2.3}
\end{aligned}
\]

Let

\[
 B_\theta=\{(r,F(r)):r\in R\},\qquad
 P_\theta=\{(q,A_q):q\text{ indexes a patch in the block}\}.
\]

Then the full occupancy of the child quotient is exactly

\[
 K_{c,d}
 =r_{B_\theta-B_\theta}
   \bigl(c-d,A_c-A_d\bigr).                            \tag{2.4}
\]

Consequently the block contribution to (1.1) is the exact additive
correlation

\[
 \boxed{
 W(P_\theta,B_\theta)
 =
 \sum_{p,p'\in P_\theta}^{+}
 {r_{B_\theta-B_\theta}(p-p')\choose3}.}              \tag{2.5}
\]

The superscript \(+\) denotes the chosen orientation of each unordered
parent pair.  The affine offset \(\eta\) cancels from every quotient, so
(2.3)--(2.5) hold for every affine line (1.8), not only one through the
origin.

If \(\eta=0\), the individual parent-patch equation also normalizes to

\[
 F(r+q)-F(r)=A_q\quad(r\in S_q),                       \tag{2.6}
\]

so \(P_\theta\) itself is a set of \(L\)-popular differences of
\(B_\theta\).  The fully coherent branch is therefore a popular-difference
problem in an abelian plane.

## 3. Exact parabola computation

For (1.2),

\[
 f(r)=r^2,\qquad \theta=2,\qquad
 F(r)=0.
\]

The derivative cell at shift \(q\) is the full line

\[
 d_q(r)=q^2+2qr,\qquad 0\le r<2L-q,                   \tag{3.1}
\]

with Heisenberg parameter

\[
 g_q=(q,2q,q^2).
\]

For \(c>d\),

\[
 g_cg_d^{-1}
 =(c-d,2(c-d),(c-d)^2).                               \tag{3.2}
\]

Thus a quotient depends only on \(h=c-d\).  Among the \(L\) parent shifts
\(1,\ldots,L\), it has \(L-h\) representations, while its child line has
all \(2L-h\) possible tails.  This proves (1.4).

The leading asymptotics are

\[
 W_L\sim {49\over120}L^5,\qquad
 T_L\sim {5\over8}L^4.                                \tag{3.3}
\]

Also

\[
 {W_Lk^3\over(k^3+m^2)^2}
 \longrightarrow {49\over3840}>0,                    \tag{3.4}
\]

which makes the sharpness in (1.5) quantitative.

In the normalized coordinates, \(B_2=\{(r,0):0\le r<2L\}\) and
\(P_2=\{(q,0):1\le q\le L\}\).  Hence

\[
 r_{P_2-P_2}(h,0)=L-h,\qquad
 r_{B_2-B_2}(h,0)=2L-h,
\]

and (2.5) becomes exactly (1.4).  The large weighted mass is the ordinary
additive energy of two aligned intervals after quadratic normalization.

## 4. The integer parabola is distance-Sidon

For an edge \(i<j\), write

\[
 a=j-i,\qquad s=i+j.
\]

Its squared Euclidean length is

\[
 D(i,j)=a^2(1+s^2),\qquad 1\le a\le s.                \tag{4.1}
\]

Suppose two edges give

\[
 a^2(1+s^2)=b^2(1+t^2).                               \tag{4.2}
\]

If \(s=t\), then \(a=b\), and the endpoint pair is recovered uniquely from
\((a,s)\).  Otherwise relabel so \(s>t\).  Equation (4.2) then gives
\(b>a\).  Write

\[
 a=gA,\qquad b=gB,\qquad (A,B)=1,
\]

so \(B>A\).  Coprimality in (4.2) implies that, for some integer \(n\),

\[
 s^2+1=B^2n,\qquad t^2+1=A^2n.                       \tag{4.3}
\]

Subtracting the cross-products gives

\[
 (sA-tB)(sA+tB)=B^2-A^2.                              \tag{4.4}
\]

The first factor on the left is a positive integer.  But the second edge
condition \(b\le t\) implies \(B\le t\), and therefore

\[
 0<sA-tB
 ={B^2-A^2\over sA+tB}
 <{B^2\over tB}\le1,                                  \tag{4.5}
\]

a contradiction.  Thus (4.2) has no distinct edge solutions, proving that
(1.2) is distance-Sidon for every \(L\).

This argument is a short negative-Pell gap principle: two solutions of
\(x^2-ny^2=-1\) cannot both satisfy the endpoint constraint needed by
distinct parabola edges.

## 5. Consequence for the residual strategy

The isolated-preimage stress showed that local reverse multiplicity need
not create a long parameter path.  The parabola now shows the complementary
global obstruction: a long coherent path can make \(W_L\) one factor of
\(k\) larger than the target record count, and this factor is legitimately
paid by ambient quadratic height.

Therefore a successful weighted incidence theorem must distinguish:

1. **Coherent quadratic blocks**, where normalization produces highly
   additive \(B_\theta\) and the large value in (1.7) is paid by \(m^2\);
2. **Distributed short-path blocks**, where the reverse slope-packing
   theorem should force \(W\) down toward the \(k^3\) scale.

An unqualified estimate of \(W\) at the record scale is false.  The next
viable target is either the sharp global bound (1.7), or a dichotomy saying
that every contribution above \(m^{o(1)}(k^3+m^2)\) in (1.1) lies in a
quadratically normalized additive block whose height pays the extra
factor.

## 6. Verification

Run

    python phase2/loop/erdos1208/verify_support_weighted_heisenberg_parabola_barrier.py

The verifier checks the exact Heisenberg quotient, child occupancies,
formulae (1.3)--(1.5), the quadratic normalization, reverse multiplicity,
the Pell-gap identities, and every squared distance for
\(2L=8,16,32,64,128,200\).
