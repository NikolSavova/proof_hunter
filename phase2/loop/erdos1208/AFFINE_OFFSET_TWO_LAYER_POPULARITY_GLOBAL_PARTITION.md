# Affine offsets: two-layer popularity and the exact global pair partition

## 1. Outcome

The affine-offset obstruction in the quadratic normalization is not real.
Fix

\[
 \lambda_q=\theta q+\eta,\qquad
 F_\theta(r)=f(r)-{\theta\over2}r^2,\qquad
 A_q=\alpha_q-{\theta\over2}q^2.                     \tag{1.1}
\]

The parent equation is

\[
 F_\theta(r+q)-F_\theta(r)=A_q+\eta r.               \tag{1.2}
\]

Define two sheared copies of the normalized graph

\[
\begin{aligned}
 B_\theta&=\{(r,F_\theta(r)):r\in R\},\\
 C_{\theta,\eta}
 &=\{(r,F_\theta(r)+\eta r):r\in R\}.
                                                               \tag{1.3}
\end{aligned}
\]

Then every parent parameter \(p_q=(q,A_q)\) is an \(L\)-popular
cross-difference in \(B_\theta-C_{\theta,\eta}\), while every child
occupancy is the ordinary self-difference multiplicity

\[
 K_{p-p'}=r_{B_\theta-B_\theta}(p-p').               \tag{1.4}
\]

Because the map \((r,y)\mapsto(r,y+\eta r)\) is an additive shear,

\[
 E_+(B_\theta,C_{\theta,\eta})
 \le\sqrt{E_+(B_\theta)E_+(C_{\theta,\eta})}
 =E_+(B_\theta).                                    \tag{1.5}
\]

Consequently the through-origin coherent-block theorem extends verbatim
to every affine offset:

\[
 \boxed{
 W(P_{\theta,\eta},B_\theta)
 \le {4\over3}
 {k^3D(H_\theta)(k+2D(H_\theta))\over L^2},}         \tag{1.6}
\]

where

\[
 H_\theta=\left\lfloor
 {2(m-1)\over\|w\|_\infty|\theta|}
 \right\rfloor,\qquad
 D(H)=\sum_{j=1}^H\left\lfloor {H\over j}\right\rfloor.
                                                               \tag{1.7}
\]

Thus \(\eta\ne0\) causes no local loss.

There is also a canonical global partition.  Every parent pair with
different shifts determines a unique line

\[
 \theta={\lambda_c-\lambda_d\over c-d},\qquad
 \eta=\lambda_c-\theta c=\lambda_d-\theta d.         \tag{1.8}
\]

For a dyadic family of patches with \(L\le |S_p|<2L\), let

\[
 n_R(q)=|\{(a,b)\in R^2:a-b=q\}|,
 \qquad
 Q_R(h)=\sum_q n_R(q)n_R(q-h),                       \tag{1.9}
\]

and let \(T(h)\) be the total number of nonhorizontal collinear triples
in the derivative cell at shift \(h\).  A support-pair injection proves
the exact global estimate

\[
 \boxed{
 W_L\le {1\over(L-1)^2}
 \sum_{h\ne0}Q_R(h)T(h).}                            \tag{1.10}
\]

This sums all \(\eta\)'s and all \(\theta\)'s without charging an affine
block more than once.  The remaining obstruction is therefore the
one-dimensional weighted cell-energy gate on the right of (1.10), not
affine-offset popularity.

The elementary budgets

\[
 \sum_hQ_R(h)=|R|^4\le k^4,\qquad
 Q_R(h)\le E_+(R):=\sum_qn_R(q)^2\le k^3             \tag{1.11}
\]

show the exact coherent/distributed split.  Additively distributed
transverse levels have small \(Q_R(h)\); an interval-like coherent level
set has \(Q_R(h)=\Theta(k^3)\) on \(\Theta(k)\) shifts, as on the
parabola.  The latter case is precisely where quadratic height must pay.

## 2. Exact two-layer normalization

Fix a primitive direction \(w\), choose \(z_w\) with
\(\det(w,z_w)=1\), and write the graph-like set as

\[
 x_r=r z_w+f(r)w\in[1,m]^2,\qquad r\in R,\quad |R|\le k.
                                                               \tag{2.1}
\]

A derivative patch \(p=(q,\lambda_q,\alpha_q)\) has tail support
\(S_p\) and satisfies

\[
 f(r+q)-f(r)=\alpha_q+\lambda_qr\qquad(r\in S_p).
                                                               \tag{2.2}
\]

On the affine projection line \(\lambda_q=\theta q+\eta\), (1.1)
turns (2.2) into (1.2).  For every \(r\in S_p\),

\[
\begin{aligned}
 &(r+q,F_\theta(r+q))
 -(r,F_\theta(r)+\eta r)\\
 &\hspace{35mm}=(q,A_q)=p_q.                         \tag{2.3}
\end{aligned}
\]

Hence

\[
 r_{B_\theta-C_{\theta,\eta}}(p_q)\ge |S_p|\ge L.
                                                               \tag{2.4}
\]

For two patches at shifts \(c,d\), the affine offset cancels:

\[
 F_\theta(t+c-d)-F_\theta(t)=A_c-A_d                \tag{2.5}
\]

on the child line.  Therefore its full occupancy is exactly

\[
 K_{c,d}
 =r_{B_\theta-B_\theta}
   (c-d,A_c-A_d).                                    \tag{2.6}
\]

Both signs in the construction are load-bearing: the \(+\eta r\) is
placed on the tail copy \(C_{\theta,\eta}\), while the parameter remains
\((q,A_q)\) with no additional shear.

## 3. Cross-energy gives the same block theorem for every offset

For finite additive sets \(X,Y\), write

\[
 E_+(X,Y)=\sum_zr_{X-Y}(z)^2.
\]

Counting the same quadruples by their internal differences gives

\[
 E_+(X,Y)
 =\sum_zr_{X-X}(z)r_{Y-Y}(z)
 \le\sqrt{E_+(X)E_+(Y)}.                             \tag{3.1}
\]

The shear in (1.3) is an invertible additive linear map, so

\[
 E_+(C_{\theta,\eta})=E_+(B_\theta).
                                                               \tag{3.2}
\]

Let \(P_{\theta,\eta}\) be the set of normalized parameters \(p_q\)
of the selected patches on this affine line.  From (2.4),

\[
\begin{aligned}
 r_{P_{\theta,\eta}-P_{\theta,\eta}}(x)
 &\le {1\over L^2}
 \sum_y r_{B_\theta-C_{\theta,\eta}}(y)
        r_{B_\theta-C_{\theta,\eta}}(y-x)\\
 &\le {E_+(B_\theta,C_{\theta,\eta})\over L^2}
 \le {E_+(B_\theta)\over L^2}.                       \tag{3.3}
\end{aligned}
\]

The coherent-block height theorem supplies

\[
\begin{aligned}
 E_+(B_\theta)&\le2k^2+4kD(H_\theta),\\
 E^\#(B_\theta)
 :=\sum_{x\ne0}r_{B_\theta-B_\theta}(x)
    \bigl(r_{B_\theta-B_\theta}(x)-1\bigr)
 &\le4kD(H_\theta),                                  \tag{3.4}\\
 \sum_{x\ne0}{r_{B_\theta-B_\theta}(x)\choose3}
 &\le {k\over6}E^\#(B_\theta).
\end{aligned}
\]

Distinct parent parameters have nonzero difference.  Multiplying (3.3)
by the child weight in (2.6), summing, and using (3.4) proves

\[
\begin{aligned}
 W(P_{\theta,\eta},B_\theta)
 &\le {E_+(B_\theta)\over L^2}
 \sum_{x\ne0}{r_{B_\theta-B_\theta}(x)\choose3}\\
 &\le {4\over3}
 {k^3D(H_\theta)(k+2D(H_\theta))\over L^2}.
                                                               \tag{3.5}
\end{aligned}
\]

No step depends on the magnitude, sign, or denominator of \(\eta\).
If \(\theta=0\), every child line is horizontal and fixed-shift vector
injectivity gives \(K_{c,d}\le1\), so its weighted mass is zero.

## 4. Canonical partition of all parent pairs

Let \(\Gamma_L\) be the full dyadic patch family.  Pairs with equal shifts
have child shift zero and triple weight zero.  Every remaining unordered
pair belongs to exactly one affine projection line by (1.8).  Therefore

\[
 W_L
 =\sum_{\theta,\eta}
 \sum_{\{p,p'\}\subset P_{\theta,\eta}}
 {r_{B_\theta-B_\theta}(p-p')\choose3}.              \tag{4.1}
\]

This is a partition, not a cover: even though one parameter vertex lies
on many projection lines, one parameter pair determines only one.

Fix \(\theta\), a normalized child difference \(x=(h,B)\), and orient
every parent pair counted by

\[
 r_{\theta,\eta}^+(x).
\]

For a patch \(p_c\), every tail \(r\in S_{p_c}\) gives the cross-difference
representation

\[
 p_c=(r+c,F_\theta(r+c))
     -(r,F_\theta(r)+\eta r).                        \tag{4.2}
\]

For an oriented pair \((p_c,p_d)\), choose independently
\(r\in S_{p_c}\) and \(s\in S_{p_d}\).  There are at least \(L^2\)
choices.  Fewer than \(2L\) have \(r=s\), so at least

\[
 L^2-(2L-1)=(L-1)^2                                 \tag{4.3}
\]

have \(r\ne s\).

For such a nonshared-tail choice, the four endpoint levels are

\[
 (r+c,r,s+d,s).
\]

They determine the two shifts \(c,d\).  Moreover \(p_c-p_d=x\) implies

\[
 B
 =F_\theta(r+c)-F_\theta(r)
  -F_\theta(s+d)+F_\theta(s)-\eta(r-s),              \tag{4.4}
\]

so

\[
 \eta=
 {F_\theta(r+c)-F_\theta(r)
  -F_\theta(s+d)+F_\theta(s)-B\over r-s}.            \tag{4.5}
\]

Thus the endpoint quadruple, \(\theta\), and \(x\) recover \(\eta\) and
both parent parameters uniquely.  This is an injection.

For fixed \(h=c-d\), the number of possible ordered endpoint quadruples
is exactly at most

\[
\begin{aligned}
 Q_R(h)
 &=|\{(a,r,b,s)\in R^4:(a-r)-(b-s)=h\}|\\
 &=\sum_qn_R(q)n_R(q-h).                             \tag{4.6}
\end{aligned}
\]

Consequently

\[
 \boxed{
 \sum_\eta r_{\theta,\eta}^+(x)
 \le {Q_R(h)\over(L-1)^2}.}                          \tag{4.7}
\]

This is the promised lossless summation over affine offsets.

## 5. Summing the curvatures

For \(h\ne0\), a nonhorizontal child line

\[
 d_h(t)=\beta+\mu t
\]

has the unique normalized curvature and intercept

\[
 \theta={\mu\over h},\qquad
 B=\beta-{\theta\over2}h^2.                          \tag{5.1}
\]

Hence summing (4.7) over \(\theta\) and \(x\) counts every
nonhorizontal child line exactly once.  If

\[
 T(h)=\sum_{\substack{\ell\text{ nonhorizontal}\\
                       \ell\subset P_h}}
 {|S_\ell|\choose3},                                 \tag{5.2}
\]

then (4.1) and (4.7) give (1.10).

The identities in (1.11) follow from correlation:

\[
 \sum_hQ_R(h)
 =\left(\sum_qn_R(q)\right)^2=|R|^4,
\]

and Cauchy--Schwarz gives

\[
 Q_R(h)\le\sum_qn_R(q)^2=E_+(R)\le |R|^3.
                                                               \tag{5.3}
\]

Two immediately closed subranges are therefore

\[
\begin{aligned}
 W_L
 &\le {E_+(R)\over(L-1)^2}\sum_hT(h),\\
 W_L
 &\le {|R|^4\over(L-1)^2}\max_hT(h).                 \tag{5.4}
\end{aligned}
\]

One formally sufficient inequality for the corrected target is

\[
 \boxed{
 \sum_{h\ne0}Q_R(h)T(h)
 \le m^{o(1)}\,{L^2(k^3+m^2)^2\over k^3}.}           \tag{5.5}
\]

This is strictly smaller than the former support-weighted Heisenberg
problem: all group parameters, affine offsets, and reverse paths have
been eliminated.  What remains is a positive correlation between the
additive-difference autocorrelation of the transverse level set and the
nonhorizontal collinear-triple mass in the matching derivative cell.

However, (5.5) is still too strong because (4.7) can greatly exceed the
actual number of parent pairs at shift difference \(h\).  The genuine
integer-parabola barrier and the corrected minimum-weight gate are proved
in \`ONE_DIMENSIONAL_MIN_WEIGHT_GATE_PARABOLA_BARRIER.md\`.

For an interval \(R\), \(Q_R(h)=\Theta(k^3)\) for
\(|h|\le k/2\).  The integer parabola simultaneously has
\(T(h)=\Theta(k^3)\) on \(\Theta(k)\) shifts, and (1.10) has order
\(k^5\) when \(L\asymp k\), exactly the corrected target.  Therefore
(5.5) must use the same quadratic-height payment as the coherent-block
theorem; a purely additive bound on \(R\) cannot improve it.

## 6. Verification

Run

    python phase2/loop/erdos1208/verify_affine_offset_two_layer_popularity_global_partition.py

The verifier checks:

1. the signs in (2.3), child normalization (2.5), and the Heisenberg
   quotient on two distinct nonzero-offset affine blocks;
2. cross-energy identity (3.1), shear invariance (3.2), and
   autocorrelation bound (3.3);
3. the exact canonical \((\theta,\eta)\) pair partition;
4. the nonshared-tail recovery formula (4.5) and injection (4.7);
5. the correlation identities (4.6), (5.3), and global estimate (1.10);
6. the parabola scaling profile, where (1.10) has the sharp \(k^5\)
   order.
