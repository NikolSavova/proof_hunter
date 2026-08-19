# The adaptive cross-pair `D^2` charge

## 1. Outcome

Let `D=A-A`, `N=|D|`, `S=|D+D|`, and `K=S/N`.  Keep the adaptive rich
fibres `Q_K(u,s)` and their ordered off-diagonal mass

\[
 \mathcal O_K=\sum_{u,s}|Q_K(u,s)|(|Q_K(u,s)|-1).             \tag{1.1}
\]

This note gives an unconditional charge of **all** configurations, including
the common-endpoint stratum, into `D^2`.  It produces a new sufficient
theorem:

\[
 \boxed{\sum_{b,y}\lambda(b,y)^2
 \le K N^{o(1)}\mathcal O_K.}                                \tag{1.2}
\]

Indeed, the charge is fibrewise injective, so Cauchy--Schwarz gives

\[
 \mathcal O_K^2\le N^2\sum_{b,y}\lambda(b,y)^2.
\]

Under (1.2), canceling `O_K` yields

\[
 \mathcal O_K\le N^2K N^{o(1)}=NSN^{o(1)},                  \tag{1.3}
\]

which is the missing adaptive-tail estimate and hence proves the cube-root
upper bound in Erdős 1208.

Estimate (1.2) is not proved.  It is weaker in scale than the previous
six-anchor target: the permitted average charge load is `K=S/N`, which may
be a power of `N`, rather than `N^{o(1)}`.  The price is that the proof must
use complete-difference endpoint realization.  The inequality fails by a
growing factor for abstract radial transversals.

## 2. Incidence triples and nine cross-pair charges

Fix a fibre `F=(u,s)`, put `w=s-u`, and for `q in Q_K(u,s)` define

\[
 X_F(q)=(x_q,y_q,v_q)
       =(u+q,\ w-q,\ w-(I+J)q)\in D^3.                       \tag{2.1}
\]

This triple globally recovers `(F,q)`: since `y_q-v_q=Jq`,

\[
 q=-J(y_q-v_q),\qquad u=x_q-q,\qquad
 w=y_q+q,\qquad s=u+w.                                      \tag{2.2}
\]

For every ordered `q!=p` in the same fibre and every `0<=i,j<=2`, charge
the configuration to

\[
 \Psi_{ij}(F,q,p)=(X_F(q)_i,X_F(p)_j)\in D^2.                \tag{2.3}
\]

Each of the nine routes is injective inside every individual fibre: once
`F` is fixed, every coordinate in (2.1) is an injective affine function of
its shift.  No midpoint, antipodal sign, or common-endpoint split is needed.

Let `d_ij(gamma)` be the global degree of the cell occupied by a
configuration `gamma`, and set

\[
 \mathcal B_\times=\sum_\gamma\min_{i,j}d_{ij}(\gamma).       \tag{2.4}
\]

Choosing a minimum-degree route gives a charge with second moment at most
`B_times`.  Consequently the symmetric sufficient theorem

\[
 \mathcal B_\times\le K N^{o(1)}\mathcal O_K                \tag{2.5}
\]

also proves (1.3).  The fixed route used in (1.2) is

\[
 \boxed{\Psi_{02}(F,q,p)=(u+q,\ w-(I+J)p).}                  \tag{2.6}
\]

The minimum-nine form is empirically stronger; the fixed route has a cleaner
collision system and already survives every complete-difference stress run.

## 3. Biclique and common-factor formulations

For a fibre `F`, put

\[
 B_F=u+Q_F,\qquad Y_F=w-(I+J)Q_F.                            \tag{3.1}
\]

The image of route (2.6) is exactly the biclique `B_F x Y_F` with its
canonical `q=p` matching deleted.  Thus the second moment is a coupled
cross-fibre overlap count.  For `G=(U,S')`, `W=S'-U`, put

\[
 \alpha=U-u,\qquad \beta=(I+J)^{-1}(W-w).
\]

Then

\[
 |B_F\cap B_G|
 =|Q_F\cap(Q_G+\alpha)|,
\]

and, with the corresponding sign convention for `beta`,

\[
 |Y_F\cap Y_G|
 =|Q_F\cap(Q_G-\beta)|.                                    \tag{3.2}
\]

The deleted matchings only reduce the intersection.  The desired estimate
is therefore a support-adaptive two-translation overlap theorem with an
allowed factor `K`.

There is also an exact linear common factor behind all nine routes.  For
`X=(x_0,x_1,x_2)=X_F(q)`, define

\[
 \Phi(X)=\bigl(x_0+x_1,\ x_2+(I+J)x_0\bigr).                 \tag{3.3}
\]

Equations (2.1) give

\[
 \Phi(X_F(q))=(s,\ s+Ju),                                   \tag{3.4}
\]

independently of `q`; conversely (3.4) recovers `(u,s)`.  Hence the entire
relation is the ordered-pair system

\[
 X\ne Y,\qquad \Phi(X)=\Phi(Y),                              \tag{3.5}
\]

inside the special set of adaptive incidence triples.

This supplies a useful inverse certificate.  In a hypothetical subfamily
where all nine cross-coordinate projections were pairwise independent, the
two copies of the common random vector `Phi(X)=Phi(Y)` would have zero
covariance.  Its variance would therefore vanish, so the fibre label would
be constant.  But every route is injective inside one fibre.  Thus a full
cross-orthogonal-array obstruction is impossible over the plane.  The
missing quantitative step is a sparse density-increment theorem at the
`K`-scaled codegree level; ordinary dense regularity loses the required
power.

## 4. Exact collision system for the fixed route

Write a configuration as

\[
 (a,b,c,z_q,z_p,\ell_q,\ell_p)
 =(u,u+q,u+p,w-q,w-p,w-(I+J)q,w-(I+J)p).          \tag{4.1}
\]

Route (2.6) fixes `(b,ell_p)`.  For two preimages put

\[
 \delta=a_2-a_1,\qquad \pi=p_2-p_1.                         \tag{4.2}
\]

The fixed-key identities force

\[
 q_2-q_1=-\delta,\qquad w_2-w_1=(I+J)\pi.                   \tag{4.3}
\]

The seven form displacements are therefore exactly

\[
 \boxed{
 \delta,\ 0,\ \delta+\pi,\ \delta+(I+J)\pi,
 J\pi,\ (I+J)(\delta+\pi),\ 0.}                            \tag{4.4}
\]

Every nonzero entry in (4.4) is realized as a displacement between two
members of the complete difference set.  The verifier checks (4.1)--(4.4)
on every stored collision.

## 5. Exact calibration and the endpoint separation

For route (2.6), the profiles below are
`(N,S,mass,second moment,max load)`:

| family | profile | moment / `(K mass)` | moment / `S^2` |
|---|---:|---:|---:|
| closure 30 | `(871,62273,1420,1496,2)` | `0.014735` | `3.86e-7` |
| closure 40 | `(1561,156057,370516,1139274,26)` | `0.030757` | `4.68e-5` |
| Costas 23 | `(463,4513,498674,3020644,24)` | `0.621439` | `0.148309` |
| Costas 31 | `(871,9495,765102,3872958,33)` | `0.464351` | `0.042959` |
| Costas 37 | `(1261,13917,2939312,18630176,34)` | `0.574303` | `0.096189` |
| Costas 41 | `(1561,17875,4629690,30972628,44)` | `0.584229` | `0.096936` |
| Costas 43 | `(1723,19819,8451318,71515362,53)` | `0.735662` | `0.182069` |
| Costas 47, low support | `(2071,23427,25194336,361029280,71)` | `1.266785` | `0.657823` |

The `p=47` row is important: it disproves the attractive constant-one
version of (1.2), but remains fully compatible with the required
`N^{o(1)}` loss.

The same statement is decisively false without complete-difference endpoint
realization.  For the radial transversals of sides `8` and `12`, the fixed
route has moment/(K mass) approximately

\[
 20.59\quad\hbox{and}\quad72.34,                              \tag{5.1}
\]

while the minimum-nine degree envelope divided by `K mass` is approximately
`14.82` and `53.00`.  The factors grow rather than remaining subpolynomial
at the tested scale.  Thus (1.2) cannot be proved from radial uniqueness,
the affine identities, or biclique overlap alone.  The canonical endpoint
factorization of `D=A-A` must enter the quantitative density increment.

Run

```bash
python3 phase2/loop/erdos1208/verify_adaptive_cross_pair_d2_charge.py
python3 phase2/loop/erdos1208/verify_adaptive_cross_pair_d2_charge.py --extended
python3 phase2/loop/erdos1208/analyze_cross_endpoint_pair_charge.py
```

The new gate does not solve #1208.  Its advantage is a substantially larger
permitted load, a uniform treatment of normal and common-endpoint records,
an exact five-shift collision system, and a sharp empirical separation
between genuine complete differences and the strongest known radial
impostors.
