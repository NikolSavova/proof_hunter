# The one-dimensional residual: parent-shift minimum and parabola barrier

## 1. Outcome

The raw endpoint-correlation target

\[
 \sum_{h\ne0}Q_R(h)T(h)
 \le m^{o(1)}\,{L^2(k^3+m^2)^2\over k^3}             \tag{1.1}
\]

is false, even if the sum is restricted to differences of shifts actually
present in the parent dyadic band.  The integer parabola gives a genuine
distance-Sidon counterexample to (1.1) when \(L\asymp\sqrt{k}\).

This does **not** disprove the corrected weighted target

\[
 W_L\le m^{o(1)}{(k^3+m^2)^2\over k^3}.              \tag{1.2}
\]

On the same parabola band, \(W_L=\Theta(k^4)\), while the right side of
(1.2) is \(\Theta(k^5)\).  The failure comes from replacing the actual
number of parent pairs at shift difference \(h\) by the much larger
endpoint envelope \(Q_R(h)/(L-1)^2\).

Retaining the parent-shift distribution gives the corrected exact gate.
Let

\[
\begin{aligned}
 N_L(q)&=|\{p\in\Gamma_L:\text{the shift of }p\text{ is }q\}|,\\
 M_L(h)&=\sum_qN_L(q)N_L(q-h),                       \tag{1.3}\\
 Q_R(h)&=\sum_qn_R(q)n_R(q-h),\qquad
 n_R(q)=|\{(a,b)\in R^2:a-b=q\}|.
\end{aligned}
\]

Then

\[
 \boxed{
 W_L\le
 \sum_{h\ne0}
 \min\left\{
 M_L(h),\,{Q_R(h)\over(L-1)^2}
 \right\}T(h).}                                      \tag{1.4}
\]

Here \(T(h)\) is the total nonhorizontal collinear-triple mass in the
derivative cell at shift \(h\).  The first term remembers how many parent
pairs can actually have difference \(h\); the second is the nonshared-tail
endpoint injection.  Formula (1.4) sums all curvatures and affine offsets.

The surviving sufficient inequality is therefore

\[
 \boxed{
 \sum_{h\ne0}
 \min\left\{
 M_L(h),\,{Q_R(h)\over(L-1)^2}
 \right\}T(h)
 \le m^{o(1)}{(k^3+m^2)^2\over k^3}.}                \tag{1.5}
\]

Unlike (1.1), (1.5) is sharp enough to retain both sides of the intended
dichotomy:

- coherent short intervals of parent shifts are paid by \(M_L(h)\);
- distributed parent shifts with many potential endpoint decompositions
  are paid by \(Q_R(h)/(L-1)^2\).

This is the exact one-dimensional target left by the affine-block
partition.

## 2. Proof of the minimum-weight gate

Let \(\Gamma_L\) be a dyadic family of derivative-line patches satisfying

\[
 L\le |S_p|<2L.
\]

Fix a child line \(g\) with nonzero shift \(h\), and let
\(r_{\Gamma_L\Gamma_L^{-1}}^+(g)\) retain one orientation of every
unordered parent pair.

Every parent pair producing \(g\) has shifts \(q,q-h\).  Therefore,
without using any endpoint information,

\[
 r_{\Gamma_L\Gamma_L^{-1}}^+(g)\le M_L(h).           \tag{2.1}
\]

On the other hand, the canonical affine-line partition assigns the pair
a unique \((\theta,\eta)\).  Choosing one tail in each parent support
gives at least \((L-1)^2\) choices with distinct tails.  For a fixed
normalized child difference, each such choice injects into an ordered
quadruple of transverse levels whose two realized differences differ by
\(h\).  There are \(Q_R(h)\) such quadruples.  Hence

\[
 r_{\Gamma_L\Gamma_L^{-1}}^+(g)
 \le {Q_R(h)\over(L-1)^2}.                            \tag{2.2}
\]

Combining (2.1) and (2.2), multiplying by the child weight
\({K_g\choose3}\), and summing the child lines in cell \(h\) proves (1.4).

There is a useful companion packing bound.  In the derivative cell at
shift \(q\), every pair of derivative points determines at most one line,
so

\[
 N_L(q){L\choose2}\le {n_R(q)\choose2}.              \tag{2.3}
\]

Consequently

\[
\begin{aligned}
 N_L(q)&\le {n_R(q)(n_R(q)-1)\over L(L-1)},\\
 \sum_qN_L(q)
 &\le {E_+(R)-k^2\over L(L-1)}
 \le {k^3-k^2\over L(L-1)},                          \tag{2.4}\\
 \sum_hM_L(h)&=\left(\sum_qN_L(q)\right)^2.
\end{aligned}
\]

Equations (1.4) and (2.4) preserve the parent-line budget that the raw
\(Q_RT\) gate discarded.

## 3. Genuine parabola counterexample to the raw target

Let \(k=t^2\), \(L=t\), and

\[
 A_k=\{(r,r^2):0\le r<k\}.                            \tag{3.1}
\]

This is distance-Sidon.  It lies in a square of side

\[
 m=(k-1)^2+1=\Theta(k^2).                             \tag{3.2}
\]

At shift \(q\), all \(k-q\) derivative points lie on the line

\[
 d_q(r)=q^2+2qr.
\]

Select the dyadic band

\[
 q\in\{k-2L+1,\ldots,k-L\}.                           \tag{3.3}
\]

It contains exactly \(L\) patches, with occupancies
\(L,\ldots,2L-1\).  The realized positive parent-shift differences are
\(1\le h<L\), and

\[
 M_L(h)=L-h.                                         \tag{3.4}
\]

For the interval of transverse levels,

\[
 n_R(q)=k-|q|\quad(|q|<k).
\]

Uniformly for \(1\le h\le L/2\),

\[
 Q_R(h)=\Theta(k^3),\qquad
 T(h)={k-h\choose3}=\Theta(k^3).                     \tag{3.5}
\]

It follows that the left side of the raw target (1.1), even restricted to
the realized shifts \(1\le h<L\), is

\[
 \sum_{h=1}^{L-1}Q_R(h)T(h)
 =\Theta(Lk^6)=\Theta(k^{13/2}).                     \tag{3.6}
\]

But (3.2) gives

\[
 {L^2(k^3+m^2)^2\over k^3}
 =\Theta(k^6).                                      \tag{3.7}
\]

Thus (1.1) fails by \(\Theta(\sqrt{k})\), beyond every
subpolynomial loss.

The actual weighted mass is instead

\[
\begin{aligned}
 W_L
 &=\sum_{h=1}^{L-1}(L-h){k-h\choose3}\\
 &=\Theta(L^2k^3)=\Theta(k^4),                       \tag{3.8}
\end{aligned}
\]

whereas the corrected target (1.2) is \(\Theta(k^5)\).  Moreover,

\[
 M_L(h)=L-h
 \ll {Q_R(h)\over(L-1)^2}=\Theta(k^2),               \tag{3.9}
\]

so the minimum in (1.4) chooses \(M_L(h)\), and (1.4) is an equality in
order of magnitude (indeed exact after summing the unique child line in
each cell).

This is a sharp no-go: any proof that discards \(M_L(h)\) before summing
the child-cell weights necessarily loses a polynomial factor on a genuine
distance-Sidon family.

## 4. Exact remaining branches

Write

\[
 \omega_L(h)=
 \min\left\{
 M_L(h),{Q_R(h)\over(L-1)^2}
 \right\}.                                           \tag{4.1}
\]

The remaining task is to prove

\[
 \sum_h\omega_L(h)T(h)
 \le m^{o(1)}{(k^3+m^2)^2\over k^3}.                 \tag{4.2}
\]

The two elementary endpoint estimates are

\[
\begin{aligned}
 \sum_h\omega_L(h)
 &\le\left(\sum_qN_L(q)\right)^2,\\
 \omega_L(h)
 &\le {E_+(R)\over(L-1)^2}.                          \tag{4.3}
\end{aligned}
\]

They close any branch where either the parent shift set has sufficiently
small additive pair mass or the child triple mass is sufficiently spread
between cells.  The hard residual must simultaneously have:

1. a concentrated parent-shift autocorrelation \(M_L(h)\);
2. large endpoint difference autocorrelation \(Q_R(h)\);
3. large nonhorizontal child triple mass \(T(h)\) on the same shifts.

The parabola realizes all three, but quadratic height pays it.  A finish
must show that any other simultaneous concentration either produces the
same coherent quadratic block/height or is reduced by the minimum in
(4.1).  The derivative cocycle must be applied with \(N_L(q)\) retained;
using \(Q_R(h)\) alone is provably too lossy.

## 5. Verification

Run

    python phase2/loop/erdos1208/verify_one_dimensional_min_weight_gate_parabola_barrier.py

The verifier checks exact interval formulae for \(n_R,Q_R,M_L,T\);
distance-Sidonicity for the tested parabola sizes; the dyadic patch
packing inequalities; the failure ratio in (3.6)--(3.7); the safety of
the corrected target; and equality of the minimum-weight bound with the
actual parabola mass.
