# Max-endpoint reduction and a quadratic-profile route

All logarithms are base two. This note develops the exact max-plus form of
the ordered-tree problem. It gives two rigorous lemmas—the radial lower
bound and a quasiconvexity fact for the imbalance penalty—and isolates one
finite-dimensional Bellman inequality which would prove tree alignment.

## 1. Exact max-plus recurrence

For an ordered strong-decomposition tree `T`, let

* `X(T)` be the maximum, over a left endpoint, of the number of caps with
  that left endpoint;
* `Y(T)` be the reflected maximum for cups with a fixed right endpoint;
* `M(T)=max\{1,\max_{s<t}c(s,t)u(s,t)\}`.  The added one is only a
  logarithmic base convention; for every nontrivial tree it equals the
  actual endpoint maximum.

At `T=A prec B`, `a=|A|`, `b=|B|`, direct endpoint classification gives

\[
\begin{aligned}
 X_T&=\max\{(b+1)X_A,X_B\},\\
 Y_T&=\max\{Y_A,(a+1)Y_B\},\\
 M_T&=\max\{M_A,M_B,X_AY_B\}.                    \tag{1}
\end{aligned}
\]

Also

\[
 C\le nX,\qquad U\le nY,
 \qquad M\le W\le n+n^2M.                        \tag{2}
\]

Thus, for `n>=2`, `log W=log M+O(log n)`, and the tree conjecture is exactly
a weighted one-turn-path theorem for (1).

Put

\[
 x=\log X,\qquad y=\log Y,\qquad m=\log M.         \tag{3}
\]

Then (1) becomes max-plus linear apart from the size weights.

## 2. Rigorous radial lower bound

Every such tree satisfies

\[
 \boxed{x(T)+y(T)\ge {1\over2}(\log n)^2-\log n.} \tag{4}
\]

Indeed put `Q=sqrt(XY)`. From (1),

\[
 Q_T\ge\sqrt{b+1}\,Q_A,
 \qquad Q_T\ge\sqrt{a+1}\,Q_B.                   \tag{5}
\]

Follow a larger child from the root and write `s_i` for the discarded
sibling sizes. Iterating (5) gives

\[
 \log Q_T\ge {1\over2}\sum_i\log(s_i+1).          \tag{6}
\]

The heavy-path estimate already proved for the sum recurrence gives

\[
 \sum_i\log(s_i+1)\ge {1\over2}(\log n)^2-\log n.
                                                               \tag{7}
\]

Since `x+y=2log Q`, (4) follows (in fact (6)--(7) give a slightly stronger
linear term depending on the normalization used in (7)).

## 3. Quasiconvexity of the imbalance penalty

Define

\[
 \phi(r,s)={(r-s)^2\over r+s}\quad(r,s\ge0),       \tag{8}
\]

with `phi(0,0)=0`. For two points `p=(r,s)` and `q=(u,v)`, let their
coordinatewise maximum be

\[
 p\vee q=(\max(r,u),\max(s,v)).                   \tag{9}
\]

Then

\[
 \boxed{\phi(p\vee q)\le\max\{\phi(p),\phi(q)\}.}\tag{10}
\]

Proof: if one point supplies both maxima there is nothing to show. Otherwise
suppose, after relabelling, that `r>=u` and `v>=s`, so the maximum is
`(r,v)`. If `r>=v`, the function `t -> phi(r,t)` decreases on `[0,r]`, and
`s<=v`, so `phi(r,v)<=phi(r,s)`. If `v>=r`, the function
`t -> phi(t,v)` decreases on `[0,v]`, and `u<=r`, so
`phi(r,v)<=phi(u,v)`. This proves (10).

There is also the exact one-sided Lipschitz bound

\[
 \phi(r+t,s)\le\phi(r,s)+t,
 \qquad\phi(r,s+t)\le\phi(r,s)+t.                 \tag{11}
\]

For example

\[
 {\partial\phi\over\partial r}
 ={(r-s)(r+3s)\over(r+s)^2}\le1,                 \tag{12}
\]

and the second inequality is symmetric.

At a glue, put `alpha=log(a+1)`, `beta=log(b+1)`. The parent coordinates
are

\[
 (x_T,y_T)=(x_A+\beta,y_A)\vee(x_B,y_B+\alpha).
                                                               \tag{13}
\]

Consequently (10)--(11) give the rigorous stability estimate

\[
 \phi(x_T,y_T)\le
 \max\{\phi(x_A,y_A)+\beta,\phi(x_B,y_B)+\alpha\}.
                                                               \tag{14}
\]

This is exactly the type of direction-sensitive stability that failed for
the sum recurrences.

## 4. Candidate absolute profile

Let

\[
 \kappa={1\over2\ln2},\qquad
 \mathcal P_K(T)={1\over2}L^2+\kappa\phi(x,y)
                  -K L\log\max\{2,L\},\quad L=\log|T|.        \tag{15}
\]

The desired one-step inequality is

\[
 \boxed{
 \max\{\mathcal P_K(A),\mathcal P_K(B),x_A+y_B\}
 \ge\mathcal P_K(T).}                              \tag{16}
\]

Together with (1), (16) would inductively prove
`m(T)>=P_K(T)`, hence the desired coefficient because the penalty is
nonnegative.

Exact exhaustive enumeration of all max-plus states through 15 leaves finds
(16) valid already for `K=1/2` (the minimum gap is zero at two leaves).
Random recursive valid-state tests through 10,000 leaves find no failure.
For `K>=1`, the exhaustive minimum is positive.

The coefficient `kappa` is not decorative. For homogeneous Pascal
templates, the entropy surplus in `x+y` and the quadratic imbalance term are
related by binary Pinsker at precisely this constant. Attempts to manufacture
an anti-aligned failure with imbalance `Theta(L log L)` from near-central
Pascal cells also create enough radial/entropy surplus in the forward term;
discarding that surplus gives false abstract counterexamples.

## 5. Exact remaining analytic gap

Equations (4) and (14) reduce (16) to a deterministic inequality in

\[
 A=\log a,\ B=\log b, x_A,y_A,x_B,y_B,            \tag{17}
\]

subject to

\[
 x_A+y_A\ge\tfrac12A^2-A,qquad
 x_B+y_B\ge\tfrac12B^2-B,                         \tag{18}
\]

and the stronger hereditary attainable-region restrictions implicit in
(1). Constraints (18) alone are not obviously sufficient: artificial
nearly balanced anti-aligned points can make a fixed-`K` local inequality
fail at very large scales. The issue is whether such points are attainable
without the entropy surplus calibrated by `kappa`.

Here is an explicit artificial failure for every fixed `K`. Take equal
child log-sizes `A=B`, put

\[
 r={A^2\over4}-{A\over2},\qquad
 D=cKA\log A\quad(1/2<c<1),                       \tag{18a}
\]

and assign

\[
 (x_A,y_A)=(r-D,r+D),\qquad
 (x_B,y_B)=(r+D,r-D).                              \tag{18b}
\]

Both radial sums equal the lower bound `A^2/2-A` in (18). For large `A`,
`D>A/2`, so after the two size shifts the anti-aligned parent is balanced
at `(r+D,r+D)`. Its profile is

\[
 {1\over2}(A+1)^2-K(A+1)\log(A+1)+o(1).           \tag{18c}
\]

Each child profile is

\[
 {1\over2}A^2+8\kappa c^2K^2(\log A)^2
       -KA\log A+o((\log A)^2),                   \tag{18d}
\]

so the parent exceeds it by `A-O_K((log A)^2)`. The forward term is
`x_A+y_B=2(r-D)`, and the parent exceeds that term by

\[
 (2c-1)KA\log A+2A-O(K\log A)>0.                 \tag{18e}
\]

Thus the radial floor plus arbitrary real coordinates cannot prove (16).
The exact missing hereditary assertion must forbid a state from lying at
the radial floor while carrying the intermediate imbalance
`Theta(A log A)`, or retain enough history to pay the subsequent reset.

The useful new facts are therefore (10) and (14). They show that coordinate
maxima never amplify normalized imbalance; only the additive size shifts can
increase it, by at most one unit of penalty per bit shifted. A complete proof
of (16) needs to combine that stability with a sharp attainable-region
version of (4), retaining radial surplus rather than only its lower bound.

There is a particularly useful equivalent form. Put

\[
 H(n)=L_n\log\max\{2,L_n\},
 \qquad P_0(n,x,y)=\tfrac12L_n^2+\kappa\phi(x,y).  \tag{19}
\]

Then (16) with constant `K` is precisely

\[
\begin{split}
P_0(T)\le\max\{&P_0(A)+K(H(n)-H(a)),\\
                &P_0(B)+K(H(n)-H(b)),\\
                &x_A+y_B+K H(n)\}.               \tag{20}
\end{split}
\]

This form separates the three ways the error is paid. A child which nearly
has size `n` receives only the tiny reserve increment `H(n)-H(a)`; the
forward cross term receives the full reserve. Exhaustive enumeration through
17 leaves shows that the smallest `K` needed in (20), over every valid local
merge in that range, is exactly `1/2`, attained at the two-leaf base. For
each `n>=3` the local required constant stays below `0.3814` through the
exhaustive range.

For comparison, without a reserve the worst exact local deficit through 17
leaves is `-2.220541348...` bits. It occurs at `n=17`, `a=8`, for

\[
(x_A,y_A,m_A)=(3,6,5),
\quad(x_B,y_B,m_B)=(7.1699250014,3.1699250014,6.1699250014).
                                                               \tag{21}
\]

The parent coordinates are `(7.1699250014,6.3398500029)`;
`P_0(T)=8.3904663499`, while the largest of the two child profiles and the
forward term is `6.1699250014`. Thus a reserve is genuinely necessary even
for the max recurrence. Equation (20), rather than a size-independent
`O(log L)` allowance, is the precise finite inequality to prove.
