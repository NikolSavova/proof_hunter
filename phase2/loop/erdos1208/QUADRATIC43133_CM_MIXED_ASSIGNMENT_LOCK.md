# Mixed-inertia and prime-assignment lock for the quadratic-43133 CM record

## 1. Verdict

The certified construction

\[
 E=\mathbb Q(\sqrt{43133}),\qquad
 |T|=223,\quad d=221,\quad N=11765
\]

remains optimal under the two local variations considered here:

1. every mixture of inertia square caps, fourth-power caps, and uncapped
   inertia at the 223 ramified ideals; and
2. every non-prefix assignment of odd prime ideals to the ramified and
   useful roles, even after optimistically declaring every unramified ideal
   useful.

Thus these variations do not improve

\[
 \boxed{F_2(n)\ll n^{0.49369772}}.                    \tag{1.1}
\]

The lock is joint: it does not merely treat mixed caps on the fixed prefix
and reassignment in the all-square case separately.  It also allows a new
ramified set to lower the sign/dyadic constraint rank and thereby raise the
generator rank from 221 to 222 or 223.  The exact assignment dual is applied
to every cap count in every resulting ray-color class.  A concavity
certificate then excludes every dyadic anchor at the headline exponent, so
reoptimizing the anchor cannot recover the loss.

Run

```text
python3 phase2/loop/erdos1208/verify_quadratic43133_cm_mixed_assignment_lock.py
```

The script requires PARI/GP for the rank-aware ray-color calculation.  It
first reruns the independent class-number, signature, Kummer,
usefulness, root-discriminant, and endpoint audit in
`verify_hostile_quadratic43133_cm.py`; it then reconstructs all calculations
specific to this lock.

## 2. Exact weighted Golod--Shafarevich budget

Let `s_2`, `s_4`, and `s_0` denote the numbers of inertia generators capped
at orders two, four, and no finite order.  Thus

\[
 s_2+s_4+s_0=223.
\]

With `N` Frobenius-square relators, the conservative weighted
Golod--Shafarevich polynomial is

\[
 P(z)=1-221z+(222+s_2+N)z^2+s_4z^4.                  \tag{2.1}
\]

For the canonical rank 221, every `s_2` and every
`0<=s_4<=223-s_2` have largest certified integer value

\[
 \boxed{N=11988-s_2}.                                \tag{2.2}
\]

Indeed, the quadratic coefficient then equals 12,210.  At `z=2/221` its
contribution to (2.1) is `-1/221^2`; even the largest possible quartic term
does not erase it because

\[
 16\cdot223<221^2.                                    \tag{2.3}
\]

Adding one further quadratic relator makes the discriminant of the
quadratic truncation

\[
 221^2-4\cdot12211=-3,                                \tag{2.4}
\]

so the nonnegative quartic term cannot restore negativity.  The verifier
checks (2.1) exactly for every admissible pair `(s_2,s_4)`.

An uncapped tame inertia ideal contributes exponent `1/2` to `log D_L`,
whereas a fourth-power cap contributes `3/8`.  Equation (2.2) shows that
adding the fourth-power relator costs no Frobenius slot.  Hence every
uncapped ideal is strictly dominated.  Write

\[
 j=223-s_2.
\]

At an optimum the `j` nonsquare caps are therefore fourth-power caps, the
useful count is `11765+j`, and a fourth cap replaces a square-cap exponent
`1/4` by `3/8`.

The verifier repeats the exact calculation for ranks 222 and 223.  Writing

\[
 M_d=\left\lfloor{d^2-1\over4}\right\rfloor,
\]

the general useful count is

\[
 N_j=M_d-(d+1)-223+j.                                \tag{2.5}
\]

Thus the all-square counts for `d=221,222,223` are respectively
`11765,11874,11985`.  At `z=2/d` every allowed quartic total remains
strictly negative.  One extra quadratic relator has quadratic discriminant
`-3` for odd `d` and `0` for even `d`, so it cannot satisfy the strict GS
criterion.

## 3. All-depth joint assignment dual

For a prime ideal of norm `Q`, put `y=log Q` and

\[
 c(Q)={y\over2},\qquad
 g_k(Q)={1\over4}\log A_k(Q^{-2}),
\]

where the `g_k` are the successive local-depth gains.  At a fractional
frontier slope `lambda`, define the all-depth useful-role value

\[
 V_\lambda(Q)=
 \sum_{k\ge1}\bigl(g_k(Q)-\lambda c(Q)\bigr)_+.       \tag{3.1}
\]

Only finitely many terms are positive.  Fractional-knapsack duality gives

\[
 F_U(L)\le \lambda L+\sum_{Q\in U}V_\lambda(Q),       \tag{3.2}
\]

with equality for the prefix at its active slope.

Let `x=log D_L` and write the endpoint right side, apart from terms
independent of the assignment, as

\[
 \mathcal R_w(x)=x+
 \log\left(1+{e^{2(2\alpha-1)w-x}\over C_{\rm Eis}}\right).
\]

It is convex.  At the prefix, let `rho=R_w'(x)`.  Its tangent therefore
turns the assignment-dependent part of the margin into the role scores

\[
 \begin{array}{c|c}
 \text{role}&\text{dual score}\\ \hline
 \text{fourth-capped inertia}&-3\rho y/8\\
 \text{square-capped inertia}&-\rho y/4\\
 \text{useful}&V_\lambda(e^y)\\
 \text{unused}&0.
 \end{array}                                           \tag{3.3}
\]

The necessary monotonicities hold uniformly, not only for the three depths
visible at the endpoint.  If exactly `K` summands in (3.1) are active, then

\[
 V_\lambda(Q)=
 {1\over4}\log {K+1\over1+Q^{-2}+\cdots+Q^{-2K}}
 -{K\lambda y\over2},                                 \tag{3.4}
\]

and activity gives

\[
 V_\lambda'(y)>-{1\over4y}.                           \tag{3.5}
\]

In fact `V_lambda(Q)` is nonincreasing in `Q` for every `lambda`.  To see
this, put `t=Q^{-2}` and let `mu_K` be the weighted mean of
`0,...,K` with weights `1,t,...,t^K`.  Inactivity of depth `K+1` reduces the
claim to

\[
 2K g_{K+1}>y\mu_K.                                   \tag{3.6}
\]

Every available ideal has `Q>=9`.  The elementary inequalities
`log(1+u)>=u/(1+u)`, `log(1+u)<=u`, and `log Q<=Q` give the uniform rational
bounds

\[
 2K g_{K+1}\ge {1\over6}-{1\over2\cdot81^2}
 >{729\over6400}
 \ge y\mu_K.                                          \tag{3.7}
\]

The verifier checks the strict rational comparison in (3.7).

Here `alpha<1/2` and `log D_L>331`, so for every anchor `w>=0`,

\[
 \rho>{1\over1+e^{-100}/C_{\rm Eis}}
 >{1\over\log9}.                                     \tag{3.8}
\]

Equations (3.5) and (3.8) show that both

\[
 {\rho y\over4}+V_\lambda(e^y),\qquad
 {3\rho y\over8}+V_\lambda(e^y)                     \tag{3.9}
\]

increase with `y`.  Together with (3.7) and the direct exchange between the
coefficients `3/8` and `1/4`, every inversion can be removed.  Therefore,
for each fixed ray-color subspace and each fixed `j`, the optimistic optimal
assignment is exactly:

* the `j` smallest ideals allowed by that subspace receive fourth-power
  inertia caps;
* the next `223-j` allowed ideals receive square inertia caps; and
* the first `N_j` remaining ideals are formally useful.

Equal-norm conjugate ideals can tie but cannot improve the score.  Since the
actual first 11,765 useful-role ideals pass the Kummer test, the all-square
baseline is feasible.  For competitors the verifier deliberately declares
every remaining ideal useful, even the ideal above 3 where the Eisenstein
CM step is ramified.  This can only strengthen a competitor.

### Rank-changing ray colors

This point is load-bearing.  A non-prefix ramified set need not retain the
canonical four-row constraint rank.  The verifier reconstructs the exact
ray quotient for modulus `(4O_E; both real places)` using a certified BNF.
The two unit columns have rank two.  Modulo their span, prime-ideal columns
have four colors forming `F_2^2`.  If the selected colors span a subspace of
dimension `r`, then

\[
 d=223-r,\qquad r\in\{0,1,2\}.                       \tag{3.10}
\]

There are three one-dimensional subspaces and one zero-dimensional case.
The exchange theorem says that, within each subspace, the optimal ramified
set is its 223 smallest allowed ideals.  The exact data are

\[
\begin{array}{c|c|c|c|c}
r&d&N_0&\text{last ramified norm}&\log D_L\\ \hline
2&221&11765&1163&331.6124924085\ldots\\
1&222&11874&2909&376.9020615317\ldots\\
1&222&11874&2939&382.5071467150\ldots\\
1&222&11874&2939&382.5071467150\ldots\\
0&223&11985&6637&427.5642991987\ldots.
\end{array}                                           \tag{3.11}
\]

The extra one or two generators are paid for by a much larger ramified norm
product.  All five rows of (3.11), crossed with all 224 mixed cap counts,
enter the all-anchor certificate below.

## 4. Exact endpoint and all-anchor exclusion

At the certified all-square anchor

\[
 \alpha=0.49369772,\qquad w_0=42282.8215,
\]

the active dual slopes are

\[
 \lambda_L=0.0305082501064\ldots,\qquad
 \lambda_R=0.0190310817846\ldots.                    \tag{4.1}
\]

Changing the `i`th smallest ramified square cap into a fourth cap adds the
`i`th post-frontier ideal in the optimistic useful list.  Its change in the
dual upper bound is

\[
 V_{\lambda_e}(Q_i^{\rm add})
 -{\rho_e\over8}\log Q_i^{\rm ram}.                  \tag{4.2}
\]

For all 223 pairs, penalty minus useful value is at least

\[
 0.2746530721670\ldots\quad(e=L),\qquad
 0.2133873332681\ldots\quad(e=R).                    \tag{4.3}
\]

Thus every nontrivial mixed assignment has smaller margins at both
certified endpoints.

The verifier also removes the possibility of repairing the loss by changing
the anchor.  For each nonwinning combination in the five ray-color rows of
(3.11) and all 224 mixed counts, it chooses a finite-precision separator
near the crossing of the two endpoint margins and then reevaluates
everything with 100-digit decimal arithmetic.  At every separator:

* the left margin is negative and has positive derivative;
* the right margin is negative and has negative derivative.

Each endpoint margin is concave in the anchor.  Hence the left margin is
negative on the entire interval to the left of the separator, while the
right margin is negative on the entire interval to its right.  The worst
certified slacks over this full cross-product are

\[
 \begin{array}{c|c|c}
 &\text{margin}&\text{anchor derivative}\\ \hline
 L&-0.2012583761\ldots&>0.0041929146\ldots\\
 R&-0.4002410902\ldots&<-0.0128418312\ldots.
 \end{array}                                          \tag{4.4}
\]

The prefix assignment theorem of Section 3 holds for every anchor, so this
is simultaneously an exclusion of all non-prefix assignments.  Finally, if
`e` is the endpoint scale, `lambda` the active frontier slope, and `z` the
positive exponential correction ratio, direct differentiation gives

\[
 {\partial M_e\over\partial\alpha}
 =2ew\lambda+{4ew\over1+z}>0.                         \tag{4.5}
\]

Therefore exclusion at `0.49369772` also excludes every smaller exponent
in this family.

## 5. Numerical profile and scope

As a redundant diagnostic, the verifier reoptimizes the anchor for all 224
values of `j` in each of the five ray-color rows.  In the canonical rank-221
row the threshold worsens monotonically:

\[
\begin{array}{c|c|c}
j&\alpha_*&w_*\\ \hline
0&0.493697713823&42282.82\\
1&0.493698891667&42297.54\\
10&0.493713852652&42472.16\\
50&0.493811794173&43570.49\\
100&0.493956346191&45227.82\\
223&0.494326898958&49886.33
\end{array}                                           \tag{5.1}
\]

The all-square rank-222 and rank-223 diagnostics are already worse than
`0.49386` and `0.49404`, respectively.  For the canonical row the active
right slope exceeds the largest omitted fourth-depth slope
`0.0157605409659...`.  In rank-changing rows the verifier explicitly keeps
every depth down to slope `0.01`, below every active endpoint slope, and
uses decreasing local marginals to exclude the rest.  The floating
thresholds are diagnostic; the GS identities, ray-color assignment dual,
and 100-digit concavity exclusion are the rigorous lock.

This result closes mixed tame inertia powers and arbitrary prime-ideal
assignment for the fixed `D=43133`, 223-ideal Kummer presentation.  It does
not rule out a different base field, a different presentation with a better
generator/relation trade, or a new geometric packing mechanism.
