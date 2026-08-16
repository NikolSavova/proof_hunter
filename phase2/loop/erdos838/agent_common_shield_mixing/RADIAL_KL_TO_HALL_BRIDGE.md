# Radial KL to Hall: exact half-Gibbs routing and marked-fibre descent

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

**Subsequent correction.**  The weighted fixed-fibre endpoint described
below is now closed by
`WEIGHTED_HISTORY_DOMINATION_AND_COMPLEMENT_NO_GO.md`: genuine canonical
history weights sum to at most `V(P)` (up to the explicit description
load).  Thus the last sentence of this report's original verdict should be
read as the interface that was open at the time, not as the current live
gap.  The remaining auxiliary issue is raw multiplicity, treated in
`RAW_RANK_MATCHED_ENDPOINT_DICHOTOMY.md`.

The averaged radial cross moment has an exact Hall interpretation; no
rank bucket or cardinality approximation is needed.  Put

\[
 S_j=\sum_e{q_{j,e}\over\lambda_e},\qquad
 S=\sum_jS_j,\qquad M=\sum_j\tau_j.                       \tag{1}
\]

The radial KL divergence `D=sum_j D_j` satisfies

\[
                         \boxed{S\ge M2^{D/M}}.            \tag{2}
\]

For every endpoint occurrence `(j,e)`, use as its bank all ordinary faces
`W` in the open endpoint interval `I_e`.  Give `W` half-Gibbs capacity

\[
                         \pi(W)={2^{-|W|}\over F}.         \tag{3}
\]

Route the amount

\[
             a((j,e),W)={q_{j,e}2^{-|W|}\over4G_e}        \tag{4}
\]

to `W`.  The total routed demand is exactly `S`.  More importantly, the
load normalized by the capacity of an actual face is

\[
 \boxed{\ell(W)={1\over4}
       \sum_{j,e:\,W\subset I_e}h_{j,e}},                 \tag{5}
\]

and

\[
                  \boxed{S=\mathbb E_{W\sim\pi}\ell(W)}. \tag{6}
\]

Thus there is one actual common interval face `W` with

\[
                  \sum_{j,e:\,W\subset I_e}h_{j,e}\ge4S. \tag{7}
\]

The maximizing face is allowed to be empty, consistently with the face
count throughout the project.  This causes no loss in the Hall descent:
`W=emptyset` simply retains the full occurrence family, and the marked
shield bank below fixes a nonempty geometric target.  If a nonempty
interval face is specifically required, the empty face contributes exactly

\[
             S_\varnothing={1\over4F}\sum_{j,e}h_{j,e}.   \tag{7c}
\]

Hence either `S_emptyset>=S/2`, which already gives total radial-history
weight at least `2FS`, or some nonempty `W` has normalized load at least
`(S-S_emptyset)/(1-1/F)>=S/2` (when `F>1`).

This is the requested exact preservation of the `q/G` normalization:
the occurrence weight in the common-face fibre is the radial likelihood
ratio `h=q/p`, not an unlicensed unit count.

It is also a weight on genuine histories.  If `omega` is one of the
`d_j(T)` depth-`j` histories above parent `T` with endpoint `e`, give it

\[
                       w_\omega={2^{-|T|}\over4^jG_e}.     \tag{7a}
\]

Then

\[
              \sum_{\omega:\,(j,e)}w_\omega=h_{j,e}.      \tag{7b}
\]

Thus (7) may be expanded into actual repair/source histories before marks,
shield faces, or tangent states are pigeonholed; no averaged endpoint is
mistaken for one geometric occurrence.

There is also an exact weighted continuation to the Hall obstruction.  Let
the occurrences in (7), with weights `h_(j,e)`, have total actual-bank union
`mathcal U_W`.  Either

\[
       \sum h_{j,e}\le D_0^{1-\epsilon}|\mathcal U_W|,    \tag{8}
\]

so this whole cap-weighted parent demand is already paid by ordinary
faces, or it is a weighted Hall-dense subfamily.  If every occurrence has
at least `K` actual marked shield targets `(p,F)` of rank at most `b`, and
at most `T` tangent states, the dense branch contains one fixed
`(p,F,tau)` fibre of weight at least

\[
 \boxed{{K\over bT}
        {\sum h_{j,e}\over|\mathcal U_W|}}
       >{K D_0^{1-\epsilon}\over bT}.                    \tag{9}
\]

Hence a quadratic blocker reservoir `K=2^{Theta((log D_0)^2)}` loses no
leading coefficient while passing from the common interval face to the
fixed marked-shield/tangent omitted-petal atom.

In the first branch, (7) also gives
`S<=D_0^(1-epsilon)|mathcal U_W|/4<=D_0^(1-epsilon)V(P)/4`,
so it pays the cross moment which generated the KL bound, not merely an
unrelated occurrence statistic.

The bridge is conditional only at the correct place: (8) is a direct
ordinary-face payment, while failure of (8) is literally the Hall
obstruction.  No inference from cap-weighted demand to *unweighted* history
count is made.  Such an inference needs rank matching.  The exact formula

\[
 {N_{j,e,r}\over C_{e,s}}
   ={q_{j,e,r}\over p_{e,s}}\,2^{r+2j-s}                \tag{10}
\]

shows the obstruction: parent-history count `N_(j,e,r)` and baseline
endpoint-face count `C_(e,s)` differ from the likelihood ratio by the
rank mismatch `s-(r+2j)`.  Therefore the half-Gibbs weighted bridge is the
rigorous endpoint.  Replacing its weights by unit multiplicities without
controlling this mismatch is false in general.

At low mean, (2) is quantitatively strong.  If `M<=C log n` and
`D>=c(log n)^2`, then

\[
                         S\ge M n^{c/C}.                 \tag{11}
\]

Thus a quadratic KL term forces fixed-power cap-weighted demand into the
ordinary-face/Hall dichotomy (8)--(9).  This bridges the averaged radial
decomposition to the exact Hall invariant; the only remaining geometric
step is to discharge the weighted dense omitted-petal fibre.

## 1. Jensen produces the cap-weighted demand

Recall

\[
 D_j=\sum_eq_{j,e}\log{1\over\lambda_e},
                 \qquad \tau_j=\sum_eq_{j,e}.             \tag{12}
\]

Weighted Jensen at one depth gives

\[
 D_j\le\tau_j\log\left(
            {1\over\tau_j}\sum_e{q_{j,e}\over\lambda_e}
                                      \right).             \tag{13}
\]

Applying the same log-sum step across depths, or applying Jensen once to
all pairs `(j,e)`, gives

\[
 D\le M\log{S\over M}.                                   \tag{14}
\]

Exponentiating proves (2).  This is sharper for the present purpose than
separately bounding interval Carleson mass and radial tilt: their product
has become the single positive demand `q/lambda`.

Using `lambda_e=4G_e/F_e`, `p_e=G_e/F`, and
`h_(j,e)=q_(j,e)/p_e`, one may also write

\[
 {q_{j,e}\over\lambda_e}
       ={q_{j,e}F_e\over4G_e}
       ={F_e\over4F}h_{j,e}.                              \tag{15}
\]

Thus (1) is exactly the interval-reservoir mass times radial crowding,
with neither factor replaced by a pointwise maximum.

## 2. Exact half-Gibbs Hall routing

Let `mathcal I_e` be the ordinary face family induced by the open endpoint
interval.  Its half-weight is

\[
                         F_e=\sum_{W\in\mathcal I_e}2^{-|W|}.          \tag{16}
\]

For occurrence `(j,e)`, sum (4) over its bank:

\[
 \sum_{W\in\mathcal I_e}a((j,e),W)
       ={q_{j,e}F_e\over4G_e}
       ={q_{j,e}\over\lambda_e}.                         \tag{17}
\]

Summing (17) proves that the routed demand is `S`.  For a fixed ordinary
face `W`, divide its received mass by (3):

\[
 {\sum_{j,e:W\in\mathcal I_e}
           q_{j,e}2^{-|W|}/(4G_e)\over2^{-|W|}/F}
 = {1\over4}\sum_{j,e:W\in\mathcal I_e}{q_{j,e}F\over G_e}
 = {1\over4}\sum_{j,e:W\in\mathcal I_e}h_{j,e}.         \tag{18}
\]

This proves (5).  Finally

\[
 \sum_W\pi(W)\ell(W)
       =\sum_{j,e,W}a((j,e),W)=S,                         \tag{19}
\]

which is (6).  Since `pi` is a probability distribution on ordinary
faces, (7) follows.

Equivalently, define the capacity-Hall congestion of contexts `c` with
demands `d_c` and banks `B_c` by

\[
 \lambda^*_\pi=
 \max_{\varnothing\ne A}
       {\sum_{c\in A}d_c\over
        \pi(\bigcup_{c\in A}B_c)}.                       \tag{20}
\]

For `d_(j,e)=q_(j,e)/lambda_e` and `B_(j,e)=mathcal I_e`,
the full family already has density at least `S`, because its bank union
has `pi`-capacity at most one.  Equations (4)--(6) identify an explicit
routing and a concrete common-face load witness, not merely the formal
ratio (20).

## 3. Weighted descent to a marked tangent fibre

The marked Hall localization used previously remains exact for arbitrary
nonnegative occurrence weights.

> **Theorem 1 (weighted marked-tangent localization).**  Let occurrences
> `c` have weights `w_c`, let the union of all their actual target banks
> have `U` ordinary faces, and suppose every occurrence supplies at least
> `K` marked targets `(p,F)` with `|F|<=b`.  If every marked occurrence has
> one of at most `T` canonical tangent states, then one fixed
> `(p,F,tau)` bin has weight at least
> 
> \[
>                    {K\sum_cw_c\over bTU}.               \tag{21}
> \]

**Proof.**  Count weighted incidences `(c,p,F,tau)`.  Their total weight is
at least `K sum_c w_c`.  Each of the `U` ordinary faces has at most `b`
contained marks, and every marked occurrence has at most `T` state values.
There are at most `bTU` bins.  Pigeonhole proves (21).  QED.

Apply the theorem to the common-`W` fibre in (7), with
the genuine history weights (7a), whose endpoint sums are `h_(j,e)` by
(7b).  If (8) fails, substitute its strict reverse inequality into (21) to
obtain (9).  If the radial decomposition was already performed
inside a fixed `(p,F,tau)` atom, no pigeonhole is needed and (7) retains
the entire weight directly.

This is exactly compatible with inclusion-minimal Hall pruning.  In a
minimal weighted dense subfamily of density `rho`, deleting one context
shows that its private target measure is less than `w_c/rho`; here the
measure may be ordinary cardinality or any fixed additive capacity such as
`pi`.  The same cross-multiplication as in the unweighted theorem applies.  Thus a large
context-decodable splice bank exits, while the collision-dominated branch
descends through (21).

## 4. Exact raw-count audit and its barrier

For completeness, resolve the endpoint laws by rank.  Let

* `N_(j,e,r)` be the number of depth-`j` histories whose parent has rank
  `r` and endpoint pair `e`; and
* `C_(e,s)` be the number of ordinary endpoint faces of rank `s` counted
  in `G_e`.

Then directly from the half-weights,

\[
 q_{j,e,r}={N_{j,e,r}2^{-r}\over F4^j},\qquad
 p_{e,s}={C_{e,s}2^{-s}\over F}.                          \tag{22}
\]

Division proves (10).  In the matched slice `s=r+2j`, likelihood ratio is
literally raw Hall density `N/C`.  A mismatch of `b` upward ranks costs the
fixed factor `2^b`; this can be a fixed power when all ranks are only known
to be `O(log n)`.  Therefore (10) both validates the weighted bridge and
forbids silently replacing it by an unweighted statement.

The exact abstract equality model is simple.  Choose one rank pair with
`s=r+2j+b`, take `N=C`, and choose the half-weight normalization from
(22).  Then `q/p=2^b` although raw density is one.  With
`b=Theta(log D_0)`, a fixed-power radial tilt exists without any
fixed-power unweighted Hall density.  Such a model need not be planar, but
it decisively shows that rank matching or a geometric rank-transfer bank
is necessary for an unweighted conclusion.

## 5. Consequence and remaining boundary

Equations (2), (5), and (9) give the rigorous bridge requested:

\[
 \text{quadratic radial KL}
 \Longrightarrow
 \text{fixed-power common-face radial tilt}
 \Longrightarrow
 \begin{cases}
   \text{ordinary-face payment},\\
   \text{weighted Hall-dense fixed }(p,F,\tau)\text{ fibre}.
 \end{cases}                                             \tag{23}
\]

The cross moment cannot disappear between interval incidence and radial
crowding: it is the routed demand (17), and its average normalized load is
the actual common-face quantity (5).  The weighted dense omitted-petal
fibre named in the original version of this paragraph is discharged by the
subsequent genuine-history domination theorem.  For raw multiplicities,
same-parent-rank comparison removes the algebraic rank loss, but baseline
scarcity and varying-tag overlap remain; see
`RAW_RANK_MATCHED_ENDPOINT_DICHOTOMY.md`.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_radial_kl_to_hall_bridge.py
```

The checker verifies the Jensen bound, the exact demand identity (17), the
half-Gibbs load cancellation (18)--(19), weighted marked localization, and
the rank-resolved identity (10), all with rational input data except for
the displayed logarithmic Jensen comparison.
