# Mixed-inertia optimization of the quadratic-1949 CM tower

## 1. Record locked across the mixed-cap family

Reoptimizing the `Q(sqrt(1949))` CM/Eisenstein construction over the
ramified-ideal prefix and all inertia cap types recovers and strengthens the
optimization audit behind the current certificate:

\[
 \boxed{F_2(n)\ll n^{0.493711480}}.                      \tag{1.1}
\]

The winning arithmetic data are

\[
 |T|=227,\qquad d=225,\qquad N=12203,                 \tag{1.2}
\]

with a square cap on every inertia generator.  An earlier exploratory
combined calculation used 229 ramified ideals, rank 227, and the rounded
exponent `0.49371149`; the canonical combined record has since moved to the
227-ideal data in (1.2).  The new content here is that mixed fourth-power or
uncapped inertia, nearby prefixes, and arbitrary prime-ideal reassignment
cannot improve its two certified endpoint margins.

The exact endpoint anchor is

\[
 \alpha=0.493711480,\qquad w_0=43932.44.               \tag{1.3}
\]

Run `verify_quadratic1949_cm_mixed_inertia_rank225.py`.

## 2. Exact Kummer and arithmetic data

Let `E=Q(sqrt(1949))`.  For the first 227 odd prime ideals of `E`, the
explicit squareclass columns consist of `-1`, the norm-minus-one fundamental
unit, and 227 principal prime-ideal generators.  The two sign and two dyadic
constraints still have rank four.  Hence the certified Kummer kernel has
dimension

\[
 229-4=225.                                             \tag{2.1}
\]

The last ramified ideal is one of the ideals of norm 1,297.  The mod-3
CM-usefulness test is recomputed on this exact 225-dimensional kernel.  It
has zero rejections through the 12,203 required ideals; the last useful norm
is 134,129.  The relative base ideal above 1,949 remains in the useful list,
now at zero-based position 78.  Its Frobenius row is evaluated using

\[
 {1+\sqrt{1949}\over2}\longmapsto {1\over2}pmod{1949}
\]

and is nonzero on the Kummer kernel.

With square-capped inertia, the real-tower root discriminant is

\[
 D_L=\sqrt{1949}\prod_{\mathfrak p\in T}
      N_E(\mathfrak p)^{1/4},                           \tag{2.2}
\]

where

\[
 \log D_L=342.3225986272674925544177328313\ldots.      \tag{2.3}
\]

The CM compositum `L(zeta_3)` retains the already proved effective constant

\[
 C_{\rm Eis}={2\sqrt3\over\pi}<{71603\over64935}.      \tag{2.4}
\]

All relative-discriminant, maximal-order, covolume, projection, and norm
divisor-switch arguments are unchanged by shortening the ramified prefix.

## 3. Exact weighted Golod--Shafarevich optimization

Let

* `s_2` be the number of inertia-square relators;
* `s_4` be the number of inertia-fourth-power relators; and
* `s_0=227-s_2-s_4` be the uncapped count.

The conservative base relation count is 226.  With `N` Frobenius-square
relators, the exact weighted Golod--Shafarevich polynomial is

\[
 P(z)=1-225z+(226+s_2+N)z^2+s_4z^4.                   \tag{3.1}
\]

For every `0<=s_4<=227-s_2`, the maximum integer Frobenius count is exactly

\[
 \boxed{N=12430-s_2}.                                  \tag{3.2}
\]

Indeed, at `z=2/225`, taking the value in (3.2) makes the quadratic part

\[
 -{1\over225^2}.
\]

The quartic addition is at most

\[
 227\left({2\over225}\right)^4,
\]

and the sum remains negative because `16*227<225^2`.  On the other hand,
one extra Frobenius square makes the quadratic coefficient 12,657, whose
quadratic discriminant is

\[
 225^2-4(12657)=-3.                                    \tag{3.3}
\]

Thus even the quadratic truncation is positive for every real `z`, and the
nonnegative quartic term cannot restore infinitude.  This proves (3.2), not
just numerically.

An uncapped ideal is now strictly dominated by fourth-capping it: equation
(3.2) shows that the quartic cap costs no integer Frobenius slot, while its
root-discriminant exponent drops from `1/2` to `3/8`.  Consequently an
optimum has `s_0=0`.

For fixed `s_2`, the square caps belong on the largest ramified ideal norms
and the fourth-power caps on the smallest.  Both cap types have the same
relation count within (3.2), while changing a quartic cap on norm `Q` to a
square cap saves `(log Q)/8` in `log D_L`; the rearrangement inequality gives
the claimed assignment.

## 4. Why mixed caps do not improve the winning endpoint

Downgrading `j` square caps to fourth-power caps adds exactly `j` useful
Frobenius slots by (3.2).  Under the optimal cap assignment, it converts the
`j` smallest ramified ideals and adds the next `j` useful ideals after the
all-square frontier.

This trade can be compared exactly at either endpoint using the
fractional-knapsack dual.  For a useful ideal of norm `Q`, put

\[
 c(Q)={1\over2}\log Q,\qquad
 g_k(Q)={1\over4}\log A_k(Q^{-2}),                     \tag{4.1}
\]

and

\[
 V_\lambda(Q)=\sum_{k\ge1}(g_k(Q)-\lambda c(Q))_+.     \tag{4.2}
\]

If `lambda` is the active all-square frontier slope and `rho` is the
derivative of the master right side with respect to `log D_L`, convexity and
knapsack duality bound the endpoint-margin change for the `i`th downgrade
by

\[
 V_\lambda(Q_i^{\rm add})
 -{\rho\over8}\log Q_i^{\rm ram}.                     \tag{4.3}
\]

The verifier sums every active depth in (4.2), not merely the first three.
For all 227 possible downgrades, the negative of (4.3) is at least

\[
 0.20117145\ldots\quad\hbox{at the left endpoint},
 \qquad
 0.13999576\ldots\quad\hbox{at the right endpoint}.   \tag{4.4}
\]

Therefore every mixed square/fourth-power configuration has strictly lower
margins at the winning exact anchor.  Together with the exact domination of
uncapped ideals, this closes all inertia types for the certified endpoint.

A complete floating-point reoptimization of all 228 values of `s_2` at this
prefix also turns monotonically toward all square caps.  The first downgrade
already raises the optimized threshold by about `8.0e-7`; the all-quartic
endpoint is near `0.49434`.  These extra decimals are search diagnostics;
the rigorous comparison is (4.3)--(4.4).

## 5. Nearby ramified prefixes

The all-square calculation was rerun for every prefix `200<=|T|<=260`, with
the exact integer relation budget and full local-depth frontier.  The
minimum occurs at 227 ideals.  Representative continuous thresholds are

\[
\begin{array}{c|c|c|c}
|T|&d&N&\alpha_{\rm threshold}\\ \hline
223&221&11765&0.4937116041\\
225&223&11983&0.4937115026\\
227&225&12203&0.4937114792\\
229&227&12425&0.4937114809\\
231&229&12649&0.4937115030\\
233&231&12875&0.4937115479\\
235&233&13103&0.4937116472\\
237&235&13333&0.4937118025
\end{array}                                             \tag{5.1}
\]

The turn is exceptionally shallow: prefixes 227 and 229 differ only in the
ninth decimal place.  The theorem uses the exact positive-margin rank-225
certificate rather than claiming the displayed floating digits as an
independent proof of global optimality.

## 6. Arbitrary prime-ideal assignment

For the winning counts, the initial ramified prefix and the following useful
prefix maximize each certified endpoint margin even in the optimistic
relaxation where every unramified odd ideal is declared useful.

Here is the prime-ideal version of the all-depth exchange argument.  For a
dual slope `lambda`, use `V_lambda` from (4.2).  If `y=log Q` and the active
depth prefix has length `K`, telescoping gives

\[
 \sum_{k=1}^K g_k(Q)
 ={1\over4}\log {K+1\over1+Q^{-2}+\cdots+Q^{-2K}}.     \tag{6.1}
\]

The derivative of (6.1) with respect to `y` is one half the weighted mean
of `0,1,...,K` with weights `Q^{-2e}`.  Since
`g_K(Q)<=1/(4K)`, activity implies

\[
 K\lambda<{1\over2\log Q}.                             \tag{6.2}
\]

Let `rho` be the discriminant derivative.  The ramification-versus-useful
score is

\[
 C_{\rho,\lambda}(Q)={\rho\over4}\log Q+V_\lambda(Q).
                                                               \tag{6.3}
\]

Equations (6.1)--(6.2) show that this score is increasing whenever

\[
 \rho>{1\over\log5}.                                   \tag{6.4}
\]

Moreover `V_lambda(Q)` is nonincreasing after the first useful norm `Q_0`
provided

\[
 \lambda>{Q_0^{-2}\over(1-Q_0^{-2})^2}.               \tag{6.5}
\]

Removing ramified/useful inversions using (6.3), then filling the useful
slots using (6.5), proves prefix dominance.  Equal-norm conjugate ideals
cause equality in an exchange but no improvement.

At the two exact endpoints the verifier obtains

\[
 \lambda_L=0.0304037230\ldots,\qquad
 \lambda_R=0.0189913278\ldots,                         \tag{6.6}
\]

and the conservative bound `rho>0.9999588`.  Conditions (6.4)--(6.5) have
enormous slack.  Every ideal in the actual prefix passes the exact Kummer
usefulness test, so the optimistic assignment relaxation is tight at the
certificate.  Arbitrary prime-ideal reassignment therefore does not improve
the two endpoint inequalities proving (1.1).

## 7. Exact endpoint verification

At (1.3), with the safe rational CM constant (2.4), the dyadic endpoint
margins after subtracting `10^-25` are

\[
 0.00013638258076\ldots,\qquad
 0.00033611498498\ldots.                               \tag{7.1}
\]

The fixed-anchor endpoint zeros are

\[
 0.49371147923552870467\ldots,\qquad
 0.49371147905265513461\ldots.                         \tag{7.2}
\]

At the right endpoint the active slope `0.01899132783...` is greater than
the maximum omitted fourth-depth slope `0.01556567325...`; decreasing
marginals exclude every later depth.  Concavity, dyadic layer selection,
and placewise rounding give (1.1).

Run

```text
python3 phase2/loop/erdos1208/verify_quadratic1949_cm_mixed_inertia_rank225.py
```

It reconstructs the exact Kummer kernel and mod-3 useful set, proves the
weighted GS formula for every cap count, checks the mixed-cap dual gaps and
arbitrary-assignment hypotheses, rebuilds the full active frontier, and
certifies both endpoint margins and threshold brackets.

## 8. Scope

This is a rigorous record and a clean no-go for mixed inertia at its exact
certificate.  The gain over `0.49371149` is only in the eighth-to-ninth
decimal range.  Mixed cap powers and prime-ideal reassignment do not provide
a route toward the conjectural exponent `1/3`; a substantial improvement
still needs a different arithmetic or geometric mechanism.
