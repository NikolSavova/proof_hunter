# High-codegree completion by replacement records and one-role wedges

## 1. Outcome

The additional nonreplacement translations close the pointwise
high-codegree dichotomy with no polynomial loss.

For an ordered source pair `p=(s,s')`, put

\[
 Q_p=\{q:s,s'\in H_q\},\qquad M=c(p)=|Q_p|.             \tag{1.1}
\]

Let `R_p subset Q_p` be the rigid replacement translations, and write

\[
 r=\rho(p)=|R_p|,
 \qquad n=|Q_p\setminus R_p|=M-r.                       \tag{1.2}
\]

Let `O(p)` be the number of translation pairs which make the two first
target edges meet in exactly one of the two source roles.  Then, for every
`M>=k`,

\[
 \boxed{O(p)\ge M-r.}                                   \tag{1.3}
\]

Consequently, for every nonnegative scalar weight `V(p)`,

\[
 \boxed{
 M V(p)\le rV(p)+O(p)V(p).}                             \tag{1.4}
\]

This removes both losses in the previous common-translation dichotomy:
there is no longer a `sqrt(k)` multiplying the replacement term and no
`k/K` multiplying the one-role term.  Summed over all `c(p)>=k`, the exact
remaining gate is

\[
 \boxed{
 Z_{\ge k}(V):=\sum_{p:c(p)\ge k}c(p)V(p)
 \le D_{\rm rep}(V)+D_{\rm one}(V),}                    \tag{1.5}
\]

where both right-hand terms have exact `q`-preserving switches.

The degree-two theorem for the directed anchor graph of `R_p` supplies an
additional quantitative alternative.  The number of shared-head or
shared-tail anchor wedges involving at least one nonreplacement translation
is large once `M` is substantially above `k`.  Its double switch is exact,
but the scalar weight remains attached to an arbitrary ordered pair of
starts, so existing closure estimates do not bound it at the required
scale.

Thus (1.5) is a genuine strengthening and the cleanest current reduction.
It does not yet prove the aggregate scalar theorem: global metric estimates
for `D_rep` and `D_one` remain open.

## 2. The two target-role graphs

For `q in Q_p`, write

\[
 e_0(q)=E(s+q),\qquad e_1(q)=E(s'+q).                   \tag{2.1}
\]

Both maps are injective.  A translation lies in `R_p` exactly when
`e_0(q)` and `e_1(q)` meet.  All such records have one rigid form

\[
 e_0(q)=\{x,u_q\},\qquad e_1(q)=\{y,u_q\},
 \qquad y-x=s'-s.                                       \tag{2.2}
\]

Thus the `R_p` edges form an `r`-edge star in each role, with centres `x`
and `y` and the same leaf set.  Two translation records overlap in both
roles if and only if both belong to `R_p`.  Therefore, if `W_i(p)` is the
endpoint-wedge count of the `M` target edges in role `i`,

\[
 I(p)={r\choose2},
 \qquad
 O(p)=W_0(p)+W_1(p)-2{r\choose2}.                       \tag{2.3}
\]

The point is to use the forced stars in (2.2), rather than applying
Cauchy--Schwarz to two arbitrary `M`-edge graphs.

## 3. Star-constrained endpoint energy

The following elementary graph lemma is the main new input.

**Lemma 3.1.**  Let `G` be a simple `M`-edge graph on `k` vertices which
contains an `r`-edge star at one specified centre.  Its wedge count
`W(G)=sum_v binom(d_v,2)` satisfies

\[
 W(G)\ge
 \begin{cases}
  2M^2/k-M,& kr\le2M,\\[2mm]
  {r\choose2}+{(2M-r)^2\over2(k-1)}-{2M-r\over2},
      &kr\ge2M.
 \end{cases}                                             \tag{3.1}
\]

**Proof.**  Let `d` be the degree of the specified centre.  Then `d>=r`
and Cauchy--Schwarz on the other `k-1` degrees gives

\[
 W(G)\ge {d\choose2}
 +{(2M-d)^2\over2(k-1)}-{2M-d\over2}.                   \tag{3.2}
\]

The right side is a convex function of `d`, minimized at `d=2M/k`.
If `r<=2M/k`, removing the constraint gives the first line of (3.1).  If
`r>=2M/k`, the function is increasing on `d>=r`, giving the second line at
`d=r`.  QED.

Apply Lemma 3.1 to both graphs in (2.3).  It gives the sharper piecewise
bound

\[
\boxed{
 O(p)\ge
 \begin{cases}
  4M^2/k-2M-r(r-1),&kr\le2M,\\[1mm]
  {(2M-r)^2\over k-1}-(2M-r),&kr\ge2M.
 \end{cases}}                                            \tag{3.3}
\]

We now prove (1.3).  In the first case, subtracting `M-r` from the first
line of (3.3) gives

\[
 F(r)={4M^2\over k}-3M+2r-r^2.                          \tag{3.4}
\]

This is concave on `0<=r<=2M/k`.  At its two endpoints,

\[
 F(0)=M(4M/k-3)\ge0,                                    \tag{3.5}
\]

and

\[
 F(2M/k)
 =M\left[{4M\over k}\left(1-{1\over k}\right)
          -3+{4\over k}\right]\ge0,                   \tag{3.6}
\]

because `M>=k`.  Hence `F(r)>=0` throughout the interval.

In the second case, put `n=M-r` and `B=2M-r=M+n`.  The second line of
(3.3) is

\[
 {B(B-k+1)\over k-1}.                                   \tag{3.7}
\]

Since `M>=k`, `B-k+1>=n+1`, so (3.7) is at least `n`.
This proves (1.3).

Notice that the proof includes `r=0`.  No replacement record is required
for the low-`r` branch; ordinary endpoint energy then supplies the full
charge.

## 4. Anchor wedges involving nonreplacement translations

Regard `Q_p` and `R_p` as directed simple graphs on the `k` anchor points.
The replacement transition theorem gives

\[
 \Delta^+(R_p),\Delta^-(R_p)\le2.                       \tag{4.1}
\]

Let `A_p^+` be the number of unordered pairs of `Q_p` edges with a common
head and at least one edge outside `R_p`; define `A_p^-` analogously for a
common tail.  Cauchy--Schwarz on the full anchor degrees and (4.1) give

\[
\boxed{
 2kA_p^+\ge M(M-k)-kr,
 \qquad
 2kA_p^-\ge M(M-k)-kr.}                                 \tag{4.2}
\]

Indeed, the full shared-head wedge count is at least
`M(M-k)/(2k)`, while the `R_p`-only wedge count is at most `r/2` because
every replacement outdegree is at most two.  The tail proof is identical.
In particular,

\[
 k(A_p^++A_p^-)ge M(M-k)-kr.                            \tag{4.3}
\]

Equations (1.3) and (4.3) are the requested quantitative dichotomy.  Near
the threshold `M=k`, the target one-role wedges pay every nonreplacement
translation.  Far above `k`, anchor wedges involving a nonreplacement edge
also grow quadratically unless `r` is correspondingly large.

The anchor statement alone cannot replace (1.3): a directed `k`-edge graph
can be one-regular, with no shared-head or shared-tail wedges at all.  The
target-star energy is what makes the threshold case work.

## 5. Exact weighted switches

Let `V(p)>=0` be arbitrary.  The replacement term in (1.5) is

\[
\begin{aligned}
 D_{\rm rep}(V)
 &:=\sum_p\rho(p)V(p)\\
 &=\sum_q
   \sum_{\substack{s,s'\in H_q,\ s\ne s'\\
          E(s+q)\cap E(s'+q)\ne\varnothing}}
       V(s,s').                                          \tag{5.1}
\end{aligned}
\]

For the one-role term, put

\[
 \mathcal I_{q,q'}=H_q\cap H_{q'},
 \qquad
 \mathcal G_{q,q'}=
 \{s\in\mathcal I_{q,q'}:
 E(s+q)\cap E(s+q')\ne\varnothing\}.                   \tag{5.2}
\]

Then

\[
\boxed{
 D_{\rm one}(V):=\sum_pO(p)V(p)
 =\sum_{q<q'}
   \sum_{\substack{s\in\mathcal G_{q,q'}\\
                   t\in\mathcal I_{q,q'}\setminus
                         \mathcal G_{q,q'}}}
       \bigl(V(s,t)+V(t,s)\bigr).}                      \tag{5.3}
\]

Equations (1.4), (5.1), and (5.3) prove (1.5).  They retain every clean
translation and any determinant qualification contained in `V`.

There is also an exact switch for the shared-head anchor alternative.  Let

\[
 \eta_q(s,t)=
 1_{E(s+q)\cap E(t+q)\ne\varnothing}.                   \tag{5.4}
\]

Then

\[
\boxed{
 \sum_pV(p)A_p^+
 =\sum_a\sum_{\{b,c\}\subset A\setminus\{a\}}
   \sum_{\substack{s,t\in H_{a-b}\cap H_{a-c}\\s\ne t}}
   V(s,t)\bigl(1-\eta_{a-b}(s,t)\eta_{a-c}(s,t)\bigr).}
                                                               \tag{5.5}
\]

The nonreplacement indicator in (5.5) is exact.  However, it is different
from the exceptional/nonexceptional indicator in the shared-head closure:
that indicator compares the two translations of one start, whereas
`eta_q(s,t)` compares two starts inside one translation.  Dropping the
indicator leaves an arbitrary pair weight `V(s,t)` on a fibre intersection.
The current closure theorem does not control that metric correlation.

## 6. Scalar specialization and exponent status

For the scalar problem, take

\[
 V(s,t)=W_{-(\delta(s)-\delta(t))/18,L},                 \tag{6.1}
\]

with zero weight when invalid.  Equation (1.5) becomes

\[
 \boxed{
 \sum_{\substack{p:c(p)\ge k}}c(p)W_{r(p),L}
 \le \mathcal R_L+\mathcal D_L,}                        \tag{6.2}
\]

where `R_L` is exactly the single-fibre replacement-transition mass and
`D_L` is exactly the mixed two-fibre one-role mass.  Unlike the previous
reduction, neither is multiplied by a power of `k`.

This materially changes the remaining target.  The planted replacement
barrier has `R_L=Omega(k^4)` at `H=Theta(k^2)`; after removal of the old
`sqrt(k)` loss it remains a full factor `k` below the `Theta(k^5)` scale
sufficient in the minimal rich band.  It is no longer close to refuting the
route.

The available generic upper bounds are still insufficient.  In a dyadic
target-load band `T<=U_L(r)<2T`,

\[
 W_{r,L}\le2(k-2)T.                                     \tag{6.3}
\]

Since the total number of replacement records is at most `2(k-2)H`, (5.1)
only gives

\[
 \mathcal R_L\ll k^2HT.                                 \tag{6.4}
\]

Similarly, the unweighted identity underlying (5.3) and the crude bounds
`|G_(q,q')|<=k-2`, `sum_(q<q')|I_(q,q')|<=NH` give

\[
 \mathcal D_L\ll k^2NHT.                                \tag{6.5}
\]

Both are too large in the dense range.  The anchor double switch (5.5)
does not improve them because the scalar weight is not preserved by the
known intersection estimate.  Thus the exact remaining theorem is now a
constant-loss global estimate for the sum of (5.1) and (5.3), rather than a
pointwise codegree dichotomy.

## 7. Stress profile

The full 43-point transformed-parabola stress, restricted to scalar-aligned
source pairs with `c(p)>=43`, has

\[
\begin{array}{c|r}
\text{high-codegree ordered pairs}&7972\\
\max c(p)&86\\
\max\rho(p)&26\\
\sum c(p)V(p)&77686\\
\sum\rho(p)V(p)&11578\\
\sum O(p)V(p)&377808\\
\sum(A_p^++A_p^-)V(p)&127488.
\end{array}                                               \tag{7.1}
\]

The minimum pointwise slack `rho(p)+O(p)-c(p)` on these 7972 pairs is 82;
the completion inequality is far from accidental equality on the hardest
stored metric stress.

## 8. Verification

`verify_high_codegree_replacement_completion.py` checks:

* the exact simultaneous-overlap classification;
* the indegree/outdegree-two theorem for every replacement pencil;
* both rational branches of (3.3), without numerical rounding;
* the high-codegree completion (1.3)--(1.4);
* the nonreplacement anchor-wedge bounds (4.2)--(4.3); and
* the scalar-weighted aggregate inequality and exact stress values in
  (7.1).

It runs on closure, Costas, parabola, and ruler families, including the full
43-point aligned high-codegree parabola block.
