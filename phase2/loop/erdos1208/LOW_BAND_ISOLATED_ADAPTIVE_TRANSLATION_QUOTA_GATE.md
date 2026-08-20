# Isolated common translations: the adaptive quota gate

## 1. Outcome

Fix a physical wedge `w`, its determinant cutoff `L`, and a rich threshold
`T>=k`.  For each literal translation `q`, let

\[
 \Omega_q(w)=\{p:\ (p,q)\text{ is selected by }w,
              \ q\text{ is anchor-isolated in }Q_p\},
 \qquad e_q=|\Omega_q(w)|.                              \tag{1.1}
\]

Then the exact survivor from
`LOW_BAND_ISOLATED_MATCHING_RANK_BARRIER.md` is

\[
 I^Q(w)=\sum_qe_q.                                       \tag{1.2}
\]

Write `h_q=|H_q|` and `H_Q=sum_q h_q`.  When `H_Q>0`, define the adaptive
translation quota

\[
 \boxed{b_q=\left\lceil {k^2h_q\over H_Q}\right\rceil.} \tag{1.3}
\]

For each `q`, order the occurrences in `Omega_q(w)` by decreasing target
load `U_L(r(p))`, discard the first `b_q`, and call the remainder
`Omega_q^tail(w)`.  Put

\[
 \begin{aligned}
 E_{\rm ad}(w)&=\sum_q|\Omega_q^{\rm tail}(w)|,\\
 X_{\rm ad}(w)&=
   \sum_q\sum_{p\in\Omega_q^{\rm tail}(w)}U_L(r(p)).
 \end{aligned}                                           \tag{1.4}
\]

There is an exact implication

\[
 \boxed{
 I^Q(w)\le2k^2+E_{\rm ad}(w)
          \le2k^2+{X_{\rm ad}(w)\over T}.}              \tag{1.5}
\]

Consequently the single decorated estimate

\[
 \boxed{X_{\rm ad}(w)\le m^{o(1)}H_Q}                   \tag{1.6}
\]

would prove the desired local scale

\[
 I^Q(w)\le m^{o(1)}(H_Q/k+k^2).                         \tag{1.7}
\]

This is strictly sharper than the previous total-rich-lift target.  It
spends the allowed `k^2` term exactly where a fibre can be dense in selected
pairs, then asks for a constant-per-clean-start charge only on the residual
decorated records.

The quota cannot be replaced by one free occurrence per translation, nor
by a pointwise estimate `e_q<=m^(o(1))(1+h_q/k)`.  There are genuine
polynomial-height distance-Sidon families with one clean fibre satisfying

\[
 h_q=2M,\qquad e_q=M,\qquad U_N(r)\ge k=16M+16,          \tag{1.8}
\]

and with `q` the unique common translation of every selected source pair.
Thus a one-free target-rich lift is at least `k(M-1)`, polynomially larger
than `h_q`.  The adaptive quota (1.3) absorbs the family completely, because
for the singleton collection `Q={q}` it gives `b_q=k^2`.

No counterexample to (1.6) is known.  The contribution here is the correct
scale-sensitive reduction, a polynomial-height obstruction to every
unbalanced per-fibre replacement, and an exact verifier showing that the
adaptive tail is tiny on the main closure stress.

## 2. Proof of the adaptive reduction

Every nonzero translation `q` has a unique ordered anchor `(a,b)`, so there
are at most `k(k-1)<k^2` active translations.  Therefore

\[
 \sum_{q:e_q>0}b_q
 \le {k^2\over H_Q}\sum_{q:e_q>0}h_q
       +|\{q:e_q>0\}|
 <2k^2.                                                  \tag{2.1}
\]

For each `q`, the discarded and retained occurrences partition
`Omega_q(w)`, whence

\[
 e_q\le b_q+|\Omega_q^{\rm tail}(w)|.                   \tag{2.2}
\]

Summing (2.2) and using (2.1) proves the first inequality in (1.5).
Every retained occurrence is target-rich, so

\[
 X_{\rm ad}(w)\ge T E_{\rm ad}(w),                      \tag{2.3}
\]

which proves the second.  Since `T>=k`, (1.6) implies (1.7).

Discarding the occurrences of largest `U_L` makes `X_ad` the smallest
decorated tail among all choices with this quota.  Thus (1.6) is the weakest
version of the adaptive charge statement, not an artefact of an adverse
choice of representatives.

The ceiling in (1.3) costs the second `k^2` in (2.1).  It can be removed by
integer apportionment of exactly `k^2` quota units according to the weights
`h_q/H_Q`, but the constant is irrelevant at `m^(o(1))` precision and the
ceiling version is canonical.

## 3. What a decorated tail record knows

Let `p=(s,t)` be retained in the adaptive tail.  Use the notation

\[
 \sigma_s=P_c+P_d,qquad
 \sigma_t=P_g+P_h,qquad
 d_{p,q}=r_{s,q}-r_{t,q}                                \tag{3.1}
\]

from the preceding rank-barrier note.  If

\[
 g_q(p)=\delta(\tau_q(s))-\delta(\tau_q(t)),             \tag{3.2}
\]

then its exact quadratic affine residual is

\[
 2d_{p,q}\cdot\rho
 =g_q(p)-\bigl(\delta(s)-\delta(t)\bigr)
       +2q\cdot(\sigma_s-\sigma_t).                     \tag{3.3}
\]

Every one of the `U_L(r(p))` decorations is an ordered target edge pair
`(v,v')` satisfying

\[
 \delta(v)-\delta(v')=r(p),\qquad
 |2\det(v,v')|>L,                                       \tag{3.4}
\]

while the selector gives `delta(s)-delta(t)=-18r(p)`.
Thus (3.3) becomes

\[
 \boxed{
 2d_{p,q}\cdot\rho
 =g_q(p)+18\bigl(\delta(v)-\delta(v')\bigr)
       +2q\cdot(\sigma_s-\sigma_t).}                   \tag{3.5}
\]

There is simultaneously the Gaussian residual.  For canonically oriented
source edge vectors `u_s,u_t`, put

\[
 Z_s=(u_s-u_t)\overline{(u_s+u_t)}
    =-18r(p)-i a_s,                                      \tag{3.6}
\]

and for the decorated pair put

\[
 Z_v=(v-v')\overline{(v+v')}=r(p)-i a_v.                \tag{3.7}
\]

Then

\[
 \boxed{Z_s+18Z_v=-i(a_s+18a_v).}                       \tag{3.8}
\]

Equations (3.5) and (3.8) preserve all of the information requested by the
live gate: the literal common `q`, both clean role targets, the scalar
selector, and the determinant-qualified external record.  Existing divisor
theorems control a fixed value of the area residual in (3.8), but the large-
area branch allows it to vary over polynomially many values.  Ordinary rank
controls the affine left side of (3.5), but its right side also varies.

The remaining theorem (1.6) must therefore couple these two residuals on
the adaptive tail.  Applying either one separately returns the earlier
Gaussian-area or affine-rank barriers.

## 4. A genuine one-fibre obstruction to unbalanced charging

Fix `M` and put

\[
 H=8M+8,qquad k=16M+16,qquad N={k\choose2}.             \tag{4.1}
\]

Choose a polynomial integer `t_0` and use the vertical marks

\[
 \{0,10,24,26,35,55\}t_0.                              \tag{4.2}
\]

They form a Golomb ruler and satisfy

\[
 24^2-26^2=-10^2,qquad 55^2-35^2=18\cdot10^2.          \tag{4.3}
\]

Take `H` horizontal points `(z_i,0)` from a polynomial-span Golomb ruler,
with every `z_i>N`, and the six vertical points `(0,ct_0)` from (4.2).
The usual one-parameter finite avoidance makes this two-axis subsystem
distance-Sidon at polynomial height.

Put

\[
 r=-(10t_0)^2.                                           \tag{4.4}
\]

For each horizontal point there are two determinant-qualified target
records of gap `r`:

\[
 \begin{aligned}
 &(H_iO,H_iY_{10}),\\
 &(H_iY_{24},H_iY_{26}).
 \end{aligned}                                          \tag{4.5}
\]

Their doubled determinants exceed `N` once the horizontal offset is chosen
large enough.  Hence

\[
 U_N(r)\ge2H=16M+16=k.                                  \tag{4.6}
\]

The two edges `OH_1,OH_2`, with partners `H_1Y_10,H_2Y_10`, form a physical
wedge which selects the displayed shift `r`.

Now choose one anchor pair `(a,b)` and set `q=a-b`.  Put

\[
 K=900t_0^2.                                             \tag{4.7}
\]

For `1<=j<=M`, choose distinct small parameters `z_j` and the two vectors

\[
 u_j=(K-z_j,z_j+1),\qquad
 u'_j=(K-z_j-1,z_j).                                    \tag{4.8}
\]

They obey

\[
 |u_j|^2-|u'_j|^2=2K=1800t_0^2=-18r.                   \tag{4.9}
\]

Install each vector as an edge at an independent centre.  For every source
edge with pair sum `s`, choose one free target endpoint and define the other
so that its target pair sum is `s+q`.  This uses eight new points per `j`,
plus the two anchors.  Together with the two-axis subsystem the total point
count is exactly (4.1).

The free centres and target endpoints can be specialized so that

* all distances and pair sums are distinct;
* all `2M` displayed rows are clean;
* `H_q` consists exactly of the displayed source edges; and
* for every planted pair `p_j=(u_j,u'_j)`, one has
  `Q_(p_j)={q}`.

Indeed, the intended equalities are affine identities.  All unintended
distance equalities are nonzero quadratic polynomials, and unintended pair
sum translations or extra common translations are nonzero linear
polynomials in the independent centres/endpoints.  The only fixed distance
labels are those in (4.8); they are distinct when `K>4M+2`.  There are
polynomially many bad polynomials of degree at most two, so the grid
nonvanishing lemma gives an integral specialization of polynomial height.

Take the fibre collection `Q={q}`.  Then

\[
 h_q=2M,qquad e_q=M,qquad c_Q(p_j)=1,                  \tag{4.10}
\]

and `q` is isolated for every selected pair.  This proves (1.8).  In
particular, after discarding only one occurrence, the decorated tail has
mass at least

\[
 k(M-1),                                                 \tag{4.11}
\]

versus `H_Q=2M`.  This rules out a one-free or pointwise `h_q/k` charge by a
factor `k^(1-o(1))`.  On the other hand, the adaptive quota is `b_q=k^2`,
so (1.4) has empty tail, as it should: the permitted local `k^2` term pays
for this concentrated fibre.

## 5. Exact stress profiles

On each closure prefix, the verifier chooses the maximum rich exact wedge
at `L=floor(N/k)` and `T=k`.  The columns below are

* `I`, the isolated mass;
* `Q_act`, the number of translations carrying it;
* `E_1`, the mass after one free occurrence per translation;
* `H_act`, the fibre mass of those translations;
* `X_1`, the corresponding optimally trimmed rich lift;
* `B=sum b_q`, the adaptive quota budget;
* `E_ad`, the adaptive tail count; and
* `X_ad`, its rich lift.

\[
\begin{array}{c|r|r|r|r|r|r|r|r|r}
k&H_Q&I&Q_{act}&E_1&H_{act}&X_1&B&E_{ad}&X_{ad}\\ \hline
20&648&8&5&3&15&60&12&0&0\\
30&3816&57&48&9&344&416&107&0&0\\
40&12420&224&172&52&2211&3157&367&9&523\\
50&26532&523&420&103&6880&7503&842&15&1073
\end{array}                                               \tag{5.1}
\]

At `k=50`, the unbalanced one-free lift already exceeds the active fibre
mass, while the adaptive tail lift is only `0.0405 H_Q`.  The one-free
pointwise `h_q/k` bound is also false on 83 active translations there; only
the aggregate adaptive allocation has the correct behavior.

The companion verifier also constructs a 64-point exact instance of
Section 4.  Its profile is

\[
 (k,N,H,h_q,e_q,E_1,U_N(r),X_1,b_q,E_{ad},r,-18r)
 =(64,2016,32,6,3,2,64,128,4096,0,-100,1800),            \tag{5.2}
\]

where `H=32` denotes the horizontal-pencil size.  It enumerates every clean
fibre and verifies `Q_(p_j)={q}` exactly for all three planted pairs.

Run

```text
PYTHONPATH=phase2/loop/erdos1208 \
python3 phase2/loop/erdos1208/verify_low_band_isolated_translation_excess_gate.py
```

## 6. Verdict

The isolated matching gate is not pointwise in `q`.  A single fibre may use
a linear number of selected scalar pairs and a linear determinant-rich
target cell at polynomial height.  The `k^2` local allowance is essential
and must be allocated according to fibre mass.

After that allocation, the full problem has the precise residual form
(1.6): at most `m^(o(1))` determinant-rich decorations per clean start,
aggregated only over translations whose selected-pair density exceeds the
adaptive baseline `k^2/H_Q`.  Equations (3.5) and (3.8) give the two exact
arithmetic coordinates available for proving it.  No known construction
violates this adaptive tail, and all stored closure stresses leave only a
small residual.
