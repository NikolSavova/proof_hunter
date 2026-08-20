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

There is a quantitative result in this framework.  If \(R\) is the
largest normalized parameter-difference multiplicity in the block and

\[
 H=\left\lfloor {2(m-1)\over \|w\|_\infty|\theta|}\right\rfloor,
\qquad
 D(H)=\sum_{n=1}^H\left\lfloor {H\over n}\right\rfloor,
\]

then for \(\theta\ne0\)

\[
 \boxed{
 E_+(B_\theta)\le 2k^2+4kD(H),\qquad
 W(P_\theta,B_\theta)
 \le {Rk\over6}\bigl(2k^2+4kD(H)\bigr).}             \tag{1.9}
\]

For \(\theta=0\), instead \(W(P_\theta,B_\theta)=0\).  Thus every single
coherent affine block is controlled by the product of its parameter-path
multiplicity and its available curvature height.  The parabola has
\(R=\Theta(k)\) and \(H=\Theta(k^2)\), so (1.9) recovers its
\(k^5\) mass up to one logarithm.

When the affine parameter line passes through the origin
(\(\eta=0\)) and every selected parent patch has at least \(L\) tails,
the popular-difference information gives the stronger estimate

\[
 \boxed{
 W(P_\theta,B_\theta)
 \le {4\over3}{k^3D(H)(k+2D(H))\over L^2}.}          \tag{1.10}
\]

This proves (1.7) for the full parabola block up to powers of
\(\log m\).  It also gives an explicit residual condition for every
through-origin coherent block, with no Freiman theorem needed.
The two-layer shear in
\`AFFINE_OFFSET_TWO_LAYER_POPULARITY_GLOBAL_PARTITION.md\` subsequently
extends the same estimate to every \(\eta\).

## 2. Quadratic normalization of an affine parameter block

Fix a primitive graph-like direction \(w\), choose
\(z_w\in\mathbb Z^2\) with \(\det(w,z_w)=1\), and suppose the
distance-Sidon set has one point on each occupied \(w\)-fibre.  If the
occupied transverse levels form \(R\), write

\[
 x_r=r z_w+f(r)w\in[1,m]^2\qquad(r\in R),            \tag{2.0}
\]

so \(|R|\le k\).  Its fixed-shift derivatives are
\(d_q(r)=f(r+q)-f(r)\).  A rich derivative-line patch is encoded by
\((q,\lambda_q,\alpha_q)\), meaning
\(d_q(r)=\alpha_q+\lambda_qr\) on its tail support.

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

## 5. A height bound for one coherent affine block

Let

\[
 r_B(x)=r_{B_\theta-B_\theta}(x),\qquad
 R=\max_x r^+_{P_\theta-P_\theta}(x),                 \tag{5.1}
\]

where the second multiplicity retains the chosen orientation of parent
pairs.  Put \(n_B=|B_\theta|\le k\) and write
\(q_w=\|w\|_\infty\).  Suppose first that
\(\theta\ne0\), and put

\[
 H=\left\lfloor{2(m-1)\over q_w|\theta|}\right\rfloor,
\qquad
 D(H)=\sum_{n=1}^H\left\lfloor{H\over n}\right\rfloor,
                                                               \tag{5.2}
\]

with \(D(0)=0\).  Then

\[
 \boxed{
 E_+(B_\theta):=\sum_x r_B(x)^2
 \le 2k^2+4kD(H).}                                   \tag{5.3}
\]

Indeed, an additive quadruple in \(B_\theta\) has indices

\[
 a+d=b+c.
\]

Set \(u=a-b\) and \(v=a-c\), so \(d=a-u-v\).  Equality in the second
coordinate, using \(F(r)=f(r)-\theta r^2/2\), gives the exact identity

\[
 f(a)+f(d)-f(b)-f(c)=\theta uv.                      \tag{5.4}
\]

The \(z_w\)-components cancel from
\(x_a+x_d-x_b-x_c\), and hence

\[
 x_a+x_d-x_b-x_c=\theta uv\,w.                       \tag{5.5}
\]

A coordinate attaining \(\|w\|_\infty\), together with
\(x_r\in[1,m]^2\), now yields

\[
 |\theta uv|q_w\le2(m-1).                            \tag{5.6}
\]

The solutions with \(u=0\) or \(v=0\) contribute at most \(2k^2\).
For each \(a\), the number of nonzero signed pairs \((u,v)\) with
\(|uv|\le H\) is at most \(4D(H)\).  This proves (5.3), including all
boundary effects.

The total child-triple mass of \(B_\theta\) obeys

\[
 \sum_x {r_B(x)\choose3}
 \le {k\over6}\sum_xr_B(x)^2
 ={k\over6}E_+(B_\theta),                            \tag{5.7}
\]

because \(r_B(x)\le k\).  Combining (2.5), (5.1), (5.3), and (5.7)
proves

\[
 \boxed{
 W(P_\theta,B_\theta)
 \le {Rk\over6}\bigl(2k^2+4kD(H)\bigr)
 \ll R\bigl(k^3+k^2H\log(2+H)\bigr).}                \tag{5.8}
\]

If \(\theta=0\), every child line has slope zero.  Injectivity of the
fixed-shift derivative implies that each such line has occupancy at most
one, so its triple weight vanishes and \(W(P_\theta,B_\theta)=0\).

Let \(S=k^3+m^2\).  Since

\[
 {S^2\over k^3}
 =k^3\left(1+{m^2\over k^3}\right)^2,                \tag{5.9}
\]

(5.8) proves the corrected target (1.7) for every coherent block
satisfying

\[
 R\left(1+{H\log(2+H)\over k}\right)
 \le m^{o(1)}
 \left(1+{m^2\over k^3}\right)^2.                   \tag{5.10}
\]

This is a genuine short-path/height dichotomy.  A block can remain
uncontrolled by (5.8) only when it has simultaneously large normalized
parameter-difference multiplicity \(R\) and large curvature budget
\(H\).  On the parabola, \(q_w=1,\theta=2\),
\(H=(k-1)^2\), and \(R=k/2-1\), so (5.10) is sharp apart from the
divisor logarithm.

There is a stronger conclusion when \(\eta=0\).  Suppose every selected
parent patch has between \(L\) and \(2L\) tails.  By (2.6),

\[
 r_B(p)\ge L\qquad(p\in P_\theta).                   \tag{5.11}
\]

Define the nontrivial factorial energy

\[
 E^\#(B_\theta)
 =\sum_{x\ne0}r_B(x)(r_B(x)-1).                      \tag{5.12}
\]

Every term in (5.12) is an ordered pair of distinct representations

\[
 B_a-B_b=B_c-B_d\ne0.
\]

With \(u=a-b\) and \(v=a-c\), both \(u\) and \(v\) are nonzero:
\(u=0\) would make the represented difference zero, while \(v=0\)
would make the two representations identical.  The proof of
(5.3) therefore has no degenerate contribution and gives

\[
 \boxed{E^\#(B_\theta)\le4kD(H).}                    \tag{5.13}
\]

Moreover,

\[
\begin{aligned}
 E_+(B_\theta)
 &=2n_B^2-n_B+E^\#(B_\theta)
 \le2k^2+E^\#(B_\theta),\\
 \sum_{x\ne0}{r_B(x)\choose3}
 &\le {k\over6}E^\#(B_\theta).
                                                               \tag{5.14}
\end{aligned}
\]

The first identity separates the zero difference and the diagonal
representation pairs exactly.

For every \(x\), (5.11) implies the popular-difference autocorrelation
bound

\[
\begin{aligned}
 r_{P_\theta-P_\theta}(x)
 &\le {1\over L^2}
 \sum_y r_B(y)r_B(y-x)\\
 &\le {E_+(B_\theta)\over L^2}.                      \tag{5.15}
\end{aligned}
\]

The last line is Cauchy--Schwarz.  Since distinct parent parameters have
nonzero difference, (2.5), (5.13)--(5.15) prove

\[
\begin{aligned}
 W(P_\theta,B_\theta)
 &\le {E_+(B_\theta)\over L^2}
       \sum_{x\ne0}{r_B(x)\choose3}\\
 &\le {4\over3}
       {k^3D(H)(k+2D(H))\over L^2}.                 \tag{5.16}
\end{aligned}
\]

Thus the corrected target follows for a through-origin coherent block
whenever

\[
 D(H)\bigl(k+2D(H)\bigr)
 \le m^{o(1)}\,{L^2(k^3+m^2)^2\over k^6}.           \tag{5.17}
\]

For the parabola, \(L\asymp k\), \(H\asymp k^2\), and
\(D(H)\ll k^2\log k\).  The two sides of (5.17) are respectively
\(O(k^4\log^2k)\) and \(\Theta(k^4)\), so the logarithmic loss is
absorbed by \(m^{o(1)}\).  This rigorously pays the entire coherent
parabola block at the sharp scale (1.7).

## 6. Consequence for the residual strategy

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
factor.  The bound (5.8) proves precisely this statement for one affine
parameter block, while (5.16) retains the full \(L\)-popular-difference
gain for a block through the origin.

The exact remaining gap is now global rather than local: affine parameter
blocks can overlap, and one must sum (5.8) without repeatedly charging the
same endpoints.  Equivalently, one needs a decomposition theorem showing
that the blocks with large product

\[
 R\left(1+{H\log(2+H)\over k}\right)
\]

either have bounded total overlap, or merge into a larger coherent
quadratic block whose ambient height pays their combined mass.  Distributed
short parameter paths already have small \(R\); the difficult residual is
the simultaneous large-\(R\), large-\(H\) family.  In the
through-origin branch, the smaller exact residual is the failure range of
(5.17).  For affine blocks with \(\eta\ne0\), parent popularity is restored
by using the cross-difference of \(B_\theta\) with its additive shear;
see \`AFFINE_OFFSET_TWO_LAYER_POPULARITY_GLOBAL_PARTITION.md\`.

## 7. Verification

Run

    python phase2/loop/erdos1208/verify_support_weighted_heisenberg_parabola_barrier.py

The verifier checks the exact Heisenberg quotient, child occupancies,
formulae (1.3)--(1.5), the quadratic normalization, reverse multiplicity,
the Pell-gap identities, the additive-energy height estimate (5.3), the
triple-energy inequality (5.7), the weighted estimate (5.8), and every
squared distance for \(2L=8,16,32,64,128,200\).  It also exhausts all
four-point integer graphs in a \(5\)-square for three nonzero rational
curvatures, checking (5.4)--(5.6), (5.13), the autocorrelation inequality
(5.15), and the popular-difference estimate (5.16).
