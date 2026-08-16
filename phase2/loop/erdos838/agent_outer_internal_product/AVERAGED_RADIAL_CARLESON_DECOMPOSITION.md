# Averaged radial capture: a Carleson decomposition and the exact remaining tilt

**Date:** 2026-08-15  
**Verdict:** the averaged activity-weighted TPC/KL bound is not closed.  Two
rigorous advances are banked:

1. at every peeling depth, the capture cost splits into an interval-container
   Carleson term and a radial-degree tilt; the first term obeys an exact
   log-sum bound, while the second is bounded by a data-processed radial
   crowding moment; and
2. in the nested-cap counterexample to pointwise RMC, the complete bad
   parent activity at both depths is exponentially small.  The common
   Boolean cage is paid once after parent occurrences are aggregated.

Thus the pointwise failure does not threaten activity-weighted TPC.  A full
proof still needs a planar bound on the aggregate radial crowding/interval
incidence in the low-rank slice.  No quadratic-KL planar counterexample with
half-Gibbs mean `O(log n)` is claimed.

All logarithms are base two.

## 1. Endpoint occurrence laws

Let `P` be an `n`-point configuration in increasing `x`-order, let

\[
 F=F_P(1/2),\qquad \pi(U)={2^{-|U|}\over F},              \tag{1}
\]

and for an endpoint pair `e=(x,y)` write

\[
 G_e=\sum_{U:\,\min U=x,\max U=y}2^{-|U|},\qquad
 F_e=F_{(x,y)}(1/2).                                      \tag{2}
\]

The capture factor is

\[
                         \lambda_e={4G_e\over F_e}.       \tag{3}
\]

Put `p_e=G_e/F`; this is the unpeeled endpoint subprobability law, with

\[
                     P_2:=\sum_ep_e=\Pr_\pi\{|U|\ge2\}.  \tag{4}
\]

At depth `j`, let

\[
 q_{j,e}=\Pr_\pi\{|U|\ge2j+2,\ e_j(U)=e\},\qquad
 \tau_j=\sum_eq_{j,e}.                                    \tag{5}
\]

Thus `tau_j=Pr(floor(|U|/2)>=j+1)`.  Whenever `q_(j,e)>0`, define the
endpoint activity tilt

\[
                         h_{j,e}={q_{j,e}\over p_e}.       \tag{6}
\]

Finally put

\[
             \mathcal A={1\over4F}\sum_eF_e.             \tag{7}
\]

### The Boolean-core bound and its exact second-moment barrier

If an actual parent is `T=S union {x,y}`, every subtrace of `S` is
compatible with the endpoint pair, by heredity.  More is true.  Let `a_I(T)`
be the number of labels `z` in the open endpoint interval, outside `S`, for
which `T union {z}` is convex.  For each such `z`, all traces
`R union {z}`, `R subseteq S`, are compatible, and these one-`z` cubes are
disjoint.  Therefore

\[
 \boxed{
 Z_e(1/2)\ge(3/2)^{|S|}\left(1+{a_I(T)\over2}\right).}    \tag{7a}
\]

In particular, if `I_e` denotes the set of labels in the open interval,

\[
 \boxed{
 \log{1\over\lambda_e}
 \le (|I_e|-|S|)\log(3/2)
      -\log\left(1+{a_I(T)\over2}\right).}               \tag{7b}
\]

Dropping the last term and summing along a face gives the universal
omitted-depth bound

\[
 -\log L(U)
 \le\log(3/2)\sum_{j<\lfloor |U|/2\rfloor}
       (|I_{e_j}|-|S_{j+1}|).                             \tag{7c}
\]

The sum counts every omitted label once for each selected endpoint pair
which surrounds it.  This alone cannot yield `O(mu log(mu+2))`.  Its
addable-label part has an exact second-moment value.  If

\[
 A_+(U)=\sum_{z\notin U:\,U\cup\{z\}\text{ convex}}
 \min\{|\{u\in U:u<z\}|,|\{u\in U:u>z\}|\},             \tag{7d}
\]

then adding `z` and reversing the deletion gives

\[
 \boxed{
 \mathbb E_\pi A_+(U)
 =2\,\mathbb E_\pi\left\lfloor{(K-1)^2\over4}\right\rfloor.}
                                                                    \tag{7e}
\]

Indeed a rank-`K` face `V={v_1<...<v_K}` receives twice its Gibbs weight
from each deletion, and
`sum_l min(l-1,K-l)=floor((K-1)^2/4)`.  Thus the Boolean-core observation is
valuable.  Without the depth weight the same deletion double count gives
the benign first-moment identity

\[
 \mathbb E_\pi|\{z\notin U:U\cup\{z\}\text{ convex}\}|=2\mu.          \tag{7f}
\]

It is precisely repeated radial nesting that upgrades this to the second
moment in (7e).  Hence a proof of `D=O(mu log(mu+2))` must use the negative
`log(1+a_I/2)` terms, higher compatible cubes, or planar circuit
first-divergence.  A first-moment argument on omitted labels is provably
insufficient.

## 2. Exact two-reference identity and Carleson decomposition

Let

\[
                 D_j=\sum_eq_{j,e}\log{1\over\lambda_e}  \tag{8}
\]

be the contribution of the `j`-th peel to the canonical KL divergence.

Normalize the interval-container masses into a probability law

\[
                         r_e={F_e\over4F\mathcal A}.      \tag{8a}
\]

Also write `qhat_j=q_j/tau_j` and `phat=p/P_2`.

> **Theorem 1 (two-reference identity).**  For every `j`,
> 
> \[
> \boxed{
> {D_j\over\tau_j}
> =\log{\mathcal A\over P_2}
> +D(\widehat q_j\Vert\widehat p)
> -D(\widehat q_j\Vert r).}                              \tag{8b}
> \]
> 
> Consequently
> 
> \[
> \boxed{
> D_j\le \tau_j\log{\mathcal A\over\tau_j}
>       +\sum_eq_{j,e}\log h_{j,e}.}                      \tag{9}
> \]

**Proof.**  Equations (3), (4), and (8a) give

\[
 {1\over\lambda_e}={\mathcal A r_e\over P_2\widehat p_e}.
                                                                    \tag{8c}
\]

Average its logarithm under `qhat_j` and use
`sum qhat log(r/phat)=D(qhat||phat)-D(qhat||r)`.  This proves
(8b).  Alternatively, since `q_(j,e)=p_eh_(j,e)`, (3) gives the exact
identity

\[
 \log{1\over\lambda_e}
 =\log{F_e\over4Fq_{j,e}}+\log h_{j,e}.                  \tag{10}
\]

The log-sum inequality applied to the first terms gives

\[
 \sum_eq_{j,e}\log{F_e\over4Fq_{j,e}}
 \le\tau_j\log{sum_eF_e/(4F)\over\tau_j},               \tag{11}
\]

which is (9).  QED.

The negative divergence in (8b) is important: (9) drops it.  It is the
exact cancellation available when the actual endpoint activity is far from
the normalized interval-reservoir law.  Thus a sharp averaged proof should
compare the radial endpoint tilt toward `phat` with the competing tilt away
from `r`, rather than separately bounding every capture factor.  This is the
precise sense in which interval cages are paid after aggregation: all
endpoint occurrences at the depth enter one normalized law before a
logarithm is taken.

There is an exact incidence formula for the Carleson mass.  For a face `S`,
let `N(S)` be the number of open endpoint intervals which contain `S`.  With
labels `0,...,n-1`,

\[
 N(\varnothing)=\binom n2,\qquad
 N(S)=\min(S)(n-1-\max(S))\quad(S\ne\varnothing).         \tag{12}
\]

Interchanging the face and interval sums yields

\[
 \boxed{4\mathcal A=\mathbb E_\pi N(S)},\qquad
 \mathcal A\le{1\over4}\binom n2.                       \tag{13}
\]

In particular, at depth zero `q_(0,e)=p_e`, so the tilt vanishes and

\[
 \boxed{
 D_0\le P_2\log{\mathcal A\over P_2}
     \le P_2\log{\binom n2\over4P_2}.}                   \tag{14}
\]

No planarity beyond the endpoint-face representation is hidden in this
estimate.

## 3. The tilt is a data-processed radial crowding moment

For a parent face `T`, let `d_j(T)` be its radial extension degree: the
number of faces which peel to `T` after `j` endpoint-pair deletions.  Given
survival to depth `j`, the parent-face law is

\[
 \sigma_j(T)={\pi(T)d_j(T)\over4^j\tau_j},\qquad |T|\ge2.\tag{15}
\]

The baseline is the half-Gibbs face law conditioned on rank at least two,

\[
                         \nu(T)={\pi(T)\over P_2}.        \tag{16}
\]

Their likelihood ratio is

\[
 {\sigma_j(T)\over\nu(T)}
 ={d_j(T)P_2\over4^j\tau_j}.                             \tag{17}
\]

Taking the endpoint pair is a deterministic map.  Data processing and
(17) therefore give

\[
\begin{aligned}
 \sum_eq_{j,e}\log h_{j,e}
 &=\tau_j\left[
 D\!\left({q_j\over\tau_j}\middle\|{p\over P_2}\right)
 +\log{\tau_j\over P_2}\right]\\
 &\le
 \boxed{\tau_j\,\mathbb E_{\sigma_j}
                  \log{d_j(T)\over4^j}.}                 \tag{18}
\end{aligned}
\]

Combining (9) and (18),

\[
 \boxed{
 D_j\le\tau_j\log{\mathcal A\over\tau_j}
      +\tau_j\mathbb E_{\sigma_j}\log{d_j(T)\over4^j}.}\tag{19}
\]

This is a genuine reduction: the only term not controlled by aggregated
interval incidence is the size-biased logarithmic radial degree.  It is the
same cross-child collision currency isolated by the second-moment route,
but now with no pointwise capture product.

For scale, let `R=floor(|U|/2)`, `M=E_pi R=sum_j tau_j`, and let `J` be the
number of possible depths under consideration.  Concavity of
`x log(1/x)` gives

\[
 \sum_{j<J}\tau_j\log{\mathcal A\over\tau_j}
 \le M\log{\mathcal A J\over M}.                         \tag{20}
\]

After the rigorous rank cutoff `|U|<4log n` from the radial-bucket report,
one may take `J<=2log n`.  Thus a subpolynomial effective interval mass
`mathcal A=n^{o(1)}` and an `o((log n)^2)` aggregate crowding moment would
close the averaged KL upper bound.  The global bound in (13) is only
quadratic, so (20) alone does not close it.

## 4. Exact activity of the asymmetric nested-cap failure

Use the rational configuration `P_m` and rank-four face

\[
 V_m=\{u_{-4},u_{-2},w_{m-1},w_m\}                       \tag{21}
\]

from `RMC_NESTED_CAP_COUNTEREXAMPLE.md`.  Its depth-zero parent is `V_m`.
Its depth-one parent is

\[
                         T_m=\{u_{-2},w_{m-1}\}.          \tag{22}
\]

The exact radial degrees are

\[
                         d_0(V_m)=1,\qquad d_1(T_m)=8.    \tag{23}
\]

Indeed a rank-four history over `T_m` chooses one of the two labels
`u_-6,u_-4` on the left and one of the four labels
`w_m,u_2,u_4,u_6` on the right; all eight resulting four-sets are convex.
There are no other labels outside the endpoint interval of `T_m`.

Consequently the **complete parent activity**, including all histories and
not only the selected face, is

\[
 q_0(V_m)={1\over16F},\qquad
 q_1(T_m)={8\over16F}.                                   \tag{24}
\]

The Boolean-core bound (7a) sees two inner labels at depth zero and none at
depth one, while the two open intervals have respectively `m` and `m-2`
labels.  Hence both costs obey

\[
 \log{1\over\lambda_{f_0}}\le(m-2)\log(3/2),\qquad
 \log{1\over\lambda_{f_1}}\le(m-2)\log(3/2).             \tag{25}
\]

The exact contribution of these two bad parent states and its cage bound
are therefore

\[
\begin{aligned}
 D_{\rm cap}(m)
 &= {1\over16F}\log{1\over\lambda_{f_0}}
  + {8\over16F}\log{1\over\lambda_{f_1}}\\
 &\le {9\log(3/2)(m-2)\over16F}\\
 &\le
 \boxed{{9\log(3/2)(m-2)\over16(3/2)^m}.}               \tag{26}
\end{aligned}
\]

The last inequality uses the common low-cap face bank
`F>=(3/2)^m` once, after the two parent activities are added.  Thus the
pointwise capture quotient is exponential, but the entire corresponding
activity contribution is `O(m(3/2)^(-m))`.

The same accounting has a useful abstract form.

> **Lemma 2 (common-cage activity bound).**  Let `mathcal O` be any family
> of parent states `(j,T)`, with unnormalized occurrence activity
> 
> \[
> r(j,T)=d_j(T)2^{-(|T|+2j)}.                             \tag{27}
> \]
> 
> If the ambient configuration contains a common convex `m`-point cage,
> then
> 
> \[
> \boxed{
> \sum_{(j,T)\in\mathcal O}{r(j,T)\over F}
>        \log{1\over\lambda_{e(T)}}
> \le(3/2)^{-m}\sum_{(j,T)\in\mathcal O}r(j,T)
>        \log{1\over\lambda_{e(T)}}.}                   \tag{28}
> \]

**Proof.**  The cage contributes all of its subsets, of total half-weight
`(3/2)^m`, to `F`.  Divide the already-aggregated raw activity by this one
global lower bound.  QED.

The lemma is elementary but its order of operations is essential.  The
pointwise RMC failure multiplied the same cage denominator at successive
peels.  Equation (28) sums the actual parent occurrences first and spends
the global cage bank once.

## 5. Remaining gate

Equations (19)--(20) isolate two possible sources of a quadratic KL term in
the low-mean branch:

1. active endpoint intervals have polynomial aggregate container incidence
   rather than `n^{o(1)}` effective incidence; or
2. radial size-biasing creates a quadratic aggregate log-degree tilt.

The nested-cap regression has neither: its bad raw parent activity is
constant while its common cage has exponential half-weight, and its relevant
radial degrees are `1` and `8`.  A quadratic-KL counterexample with
`mu=O(log n)` would therefore need a prevalent family carrying nearly the
global halfmass, not a sparse collection of synchronized tangent parents.

A complete proof must partition the prevalent low-rank occurrences into
recoverable interval/cage groups for which the effective version of
`mathcal A` is subpolynomial, or prove that failure of such a partition
forces a large radial crowding bank.  This is exactly the global bounded-
reuse statement still absent from the cross-child collision theorem.

## 6. Verification

Run

```bash
python3 \
  phase2/loop/erdos838/agent_outer_internal_product/verify_averaged_radial_carleson.py
```

The verifier uses exact rational geometry and face weights.  On the complete
`m=8` nested-cap face system it reconstructs every endpoint cell and every
radial occurrence law, checks (9)--(19), the interval-incidence identity
(13), the tail sum (20), the Boolean-core bound (7a)--(7c), and the exact
addable-depth identity (7e).  At `m=21` it verifies `d_1(T_m)=8`, the exact
two-depth activity in (24), and the exponentially discounted bound (26).
It writes `averaged_radial_carleson_certificate.json`.
