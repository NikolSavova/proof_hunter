# Two-reference transport: exact Hall demand and a planar monotonicity kill

**Date:** 2026-08-15  
**Verdict:** the exact inequality

\[
 D(\widehat q_j\Vert\widehat p)
 \le D(\widehat q_j\Vert r)                              \tag{0}
\]

is false for planar point configurations, already on nine rational points.
This finite failure does not refute an asymptotic `o(log n)` allowance in the
low-mean branch.  The strongest unconditional consequence of the
two-reference identity is instead an exact global bridge: a quadratic
canonical KL cost with mean radial depth `O(log n)` forces a fixed-power
**inverse-capture parent demand**.  That demand has a literal weighted Hall
interpretation and is the correct interface with the rooted-fibre theorem.

All logarithms are base two.  The notation `F,G_e,F_e,lambda_e,p_e,q_(j,e),
tau_j,P_2,A,r_e` is that of
`AVERAGED_RADIAL_CARLESON_DECOMPOSITION.md`.

## 1. The joint lift is conditioning on compatibility

Let

\[
 \mathcal X=\{(e,S): S\text{ is a convex face in the open interval }I_e\}.
                                                                    \tag{1}
\]

Define the interval-container incidence law

\[
 R(e,S)={2^{-|S|}\over4F\mathcal A}.                     \tag{2}
\]

It is a probability law because `4FA=sum_e F_e`.  Let `C` be the event that
`e union S` is convex.  On `C`, define the ordinary parent Gibbs law

\[
 P(e,S)={2^{-(|S|+2)}\over FP_2}.                         \tag{3}
\]

> **Theorem 1 (constant-density compatibility conditioning).**
> 
> \[
> \boxed{P=R(\,\cdot\mid C),\qquad R(C)={P_2\over\mathcal A},
> \qquad {P(e,S)\over R(e,S)}={\mathcal A\over P_2}.}    \tag{4}
> \]

**Proof.**  Equations (2)--(3) have a constant ratio `A/P_2` on `C`.
Summing (3) over compatible incidences gives one because a nontrivial face
has a unique endpoint pair.  Therefore `R(C)=P_2/A` and (4) follows.  QED.

At radial depth `j`, lift the actual endpoint law to the actual parent
incidence law

\[
 Q_j(e,S)={d_j(e\cup S)2^{-(|S|+2j+2)}\over F\tau_j}.    \tag{5}
\]

Its endpoint marginal is `qhat_j`.  Applying the KL chain rule to `Q_j`
against both reference laws in (4) recovers the two-reference identity as a
difference of conditional-core divergences:

\[
\begin{aligned}
 {D_j\over\tau_j}
 &=\log{\mathcal A\over P_2}
   +D(\widehat q_j\Vert\widehat p)-D(\widehat q_j\Vert r)\\
 &=\mathbb E_{e\sim\widehat q_j}\left[
   D(Q_j(S\mid e)\Vert R(S\mid e))
  -D(Q_j(S\mid e)\Vert P(S\mid e))\right].              \tag{6}
\end{aligned}
\]

The second line is exact, not a bound.  Conditional on `e`, `P(S|e)` is the
full interval Gibbs law conditioned on endpoint compatibility.  Hence (6)
states precisely that capture cost is the information cost of this
conditioning under the actual radial core law.

## 2. Global inverse-capture/Hall demand

Put

\[
                         S_j=\sum_e{q_{j,e}\over\lambda_e},
 \qquad M=\sum_j\tau_j=\mathbb E_\pi\lfloor K/2\rfloor.  \tag{7}
\]

Jensen at one depth and then log-sum across depths give the following exact
bridge.

> **Theorem 2 (global cap-weighted demand bridge).**
> 
> \[
> \boxed{
> D_j\le\tau_j\log{S_j\over\tau_j},\qquad
> D=\sum_jD_j\le M\log{\sum_jS_j\over M}.}                \tag{8}
> \]
> Equivalently,
> \[
> \boxed{\sum_jS_j\ge M\,2^{D/M}.}                      \tag{9}
> \]

**Proof.**  Under `qhat_j`, the positive random variable is
`1/lambda_e`, so Jensen gives the first inequality.  Apply log-sum to the
sequences `(tau_j)` and `(S_j)` for the second.  Exponentiation gives (9).
QED.

There are three equivalent exact forms of the demand:

\[
\begin{aligned}
 S_j
 &=\sum_e{q_{j,e}\over\lambda_e}\\
 &=\mathcal A\sum_er_eh_{j,e}\\
 &={1\over4^{j+1}F}\sum_eF_e\,\overline d_{j,e},          \tag{10}
\end{aligned}
\]

where

\[
 \overline d_{j,e}
 ={1\over G_e}\sum_{T:\,e(T)=e}d_j(T)2^{-|T|}           \tag{11}
\]

is the compatible-cell half-Gibbs mean radial degree.

The Hall interpretation is literal.  Give every actual depth-`j` parent
occurrence of endpoint `e` and activity weight `w` the normalized interval
demand

\[
                   w\,{2^{-|W|}\over Z_e(1/2)}           \tag{12}
\]

for each interval face `W`, where `Z_e=4G_e` is the compatible-trace
half-weight.  Summing (12) over `W` gives `w/lambda_e`; summing all parent
occurrences gives `S_j`.  Thus `sum_j S_j` is the total fractional Hall
demand obtained by attaching the full interval reservoir to every actual
parent and normalizing its compatible cell to unit mass.  Formula (10)
shows the same demand from the reservoir side: interval capacity `F_e`
times compatible mean history degree.

This gives a sharp asymptotic consequence.  Put `L=log n`.  If

\[
                         M\le c_0L,qquad D\ge\delta L^2, \tag{13}
\]

then

\[
 \boxed{
 \sum_jS_j\ge M n^{\delta/c_0}.}                         \tag{14}
\]

Therefore an `o(L^2)` KL upper bound follows from the global Hall estimate

\[
                         \sum_jS_j=M n^{o(1)},            \tag{15}
\]

and the stronger `D=O(mu log(mu+2))` follows if

\[
                         \sum_jS_j\le M(\mu+2)^{O(1)}.   \tag{16}
\]

Unlike pointwise RMC, (15)--(16) aggregate actual activity before charging
any interval reservoir.  The nested-cap RMC counterexample is harmless at
this scale: its bad parent activities are exponentially small, so
`q/lambda` is only inverse-polynomial in the cap size.

Under (13), failure of (15) supplies exactly the fixed-power dense demand
needed by the global Hall program.  The marked localization theorem in
`../agent_common_shield_mixing/DENSE_HALL_ROOTED_FIBRE.md` then explains
what remains after recoverable/private interval targets are removed: a
common marked rooted-tangent fibre, not a diffuse collection of pointwise
bad cells.  No allocation of the demand (12) to ordinary faces with the
required congestion is proved here.

## 3. Exact planar kill of monotone two-reference transport

One might hope to prove (15) by showing (0), or even the stronger inverse-
moment monotonicity

\[
 {1\over\tau_j}\sum_e{q_{j,e}\over\lambda_e}
 \le{\mathcal A\over P_2}.                               \tag{17}
\]

Both statements are false in actual planar geometry.  Consider the nine
rational points, already listed in increasing `x`-order,

\[
\begin{split}
 &(152732,588305),(198972,629398),(253646,338142),\\
 &(271535,312524),(627261,872520),(773158,636702),\\
 &(848731,579029),(886929,449046),(913864,133077).
\end{split}                                               \tag{18}
\]

They are in general position.  Exact enumeration gives `449` convex faces,

\[
 F={9509\over256},\qquad \mathcal A={8335\over9509},     \tag{19}
\]

and at depth one

\[
 {S_1\over\tau_1}=1.030234802187\ldots
 >{\mathcal A\over P_2}=1.028885322799\ldots.            \tag{20}
\]

Moreover

\[
 D(\widehat q_1\Vert\widehat p)
 -D(\widehat q_1\Vert r)
 =0.000257048570\ldots>0.                                \tag{21}
\]

Thus neither Jensen monotonicity nor KL transport domination follows merely
from planar endpoint nesting.  The violation is a constant-size, very small
effect.  It does not contradict

\[
 D(\widehat q_j\Vert\widehat p)
 \le D(\widehat q_j\Vert r)+o(\log n)                    \tag{22}
\]

on the low-mean fixed-power slice.  Proving (22), however, requires a
genuinely asymptotic Hall/circuit argument; ordinary data processing has no
such sign.

For comparison, the exact audits of the saved `n58`, Pascal36, alternating30,
and the two-cap family all have a nonpositive divergence difference at every
visited depth.  Those examples support an approximate theorem but cannot
repair the exact counterexample (18).

## 4. Remaining gate

The two-reference route is now reduced without a hidden pointwise step:

1. quadratic KL in the low-mean branch forces the fixed-power aggregate
   demand (14);
2. each unit of that demand is the explicit parent/reservoir record (12);
3. sparse repeated cages contribute too little demand, as the two-cap audit
   proves; and
4. exact monotone transport is false, so the remaining saving must come from
   a global Hall allocation or a planar first-divergence localization of a
   dense subfamily.

No scalable planar configuration with `mu=O(log n)` and positive quadratic
divergence difference was found.  Conversely, no proof of (15), (16), or
(22) is claimed.

## 5. Verification

Run

```bash
python3 \
  phase2/loop/erdos838/agent_outer_internal_product/verify_two_reference_hall_demand.py
```

The verifier enumerates every subset of (18) using exact integer
orientations.  It reconstructs all endpoint, interval-container, and radial
laws; checks the constant-density joint lift (4), the two-reference identity
(6), all forms of the demand in (10), and the Jensen/log-sum bridge (8)--(9);
and certifies the strict rational inequality in (20) and the positive KL
difference (21).  It writes `two_reference_hall_demand_certificate.json`.
