# Restriction peaks and dyadic curvature for Erdős 838

**Date:** 2026-08-14  
**Verdict:** the global restriction-peak hypothesis has a clean, exact
multiscale consequence: the dyadic log-partition increment has a
one-unit-per-octave lower envelope, and its endpoint curvature is at most
one.  There is also a stronger fixed-cardinality/factorial-moment hierarchy
which is not visible from Bernoulli restrictions alone.

These facts do **not** close `H=n^o(1)` and do not improve the unconditional
`H<=n^(3/4+o(1))` exponent.  This limitation is sharp at the scalar level.
Complete rank truncations are coherent hereditary systems, are global
restriction peaks, have the required
`2^(1/4-o(1))(log n)^2` total mass, and still have
`H=n^(3/4+o(1))`.  Planarity must therefore enter through a quantitative
rank-repair theorem which rules out an approximate logarithmic rank shelf;
the restriction identities and the known total-count theorem cannot do it.

Throughout, the empty face is counted,

\[
 Z(t)=\sum_{A\in\mathcal F}t^{|A|},\qquad
 \mu_t={tZ'(t)\over Z(t)},\qquad
 \sigma_t^2=\operatorname {Var}_t|A|,
 \qquad H={nZ(1/2)\over Z(1)}.
\]

Here `F` is the family of convex-position subsets.  Let `P` be a **global
restriction record**, meaning

\[
 H(Q)\le h:=H(P)\qquad(\varnothing\ne Q\subseteq P).       \tag{R}
\]

Any point set has a restriction satisfying (R), so an upper bound for these
records would suffice for the unrestricted problem.

## 1. The full fixed-size restriction hierarchy

The Bernoulli identity in the prompt is

\[
 \mathbb E[V(X)H(X)]
 =n\alpha Z(\alpha/2)+(1-\alpha)(\alpha/2)Z'(\alpha/2),
 \qquad \mathbb EV(X)=Z(\alpha).                         \tag{1}
\]

Under (R), it gives, for every `0<=alpha<=1`,

\[
 n\alpha Z(\alpha/2)+(1-\alpha)\mu_{\alpha/2}Z(\alpha/2)
 \le hZ(\alpha).                                        \tag{2}
\]

There is a strictly more granular necessary condition.  Average (R) over
all `m`-subsets, with weight `V(Q)`.  A fixed rank-`k` face occurs in exactly
`binom(n-k,m-k)` of them, so

\[
 \boxed{
 m\,{\sum_kv_k2^{-k}{n-k\choose m-k}
       \over\sum_kv_k{n-k\choose m-k}}\le h
 }
 \qquad(1\le m\le n).                                  \tag{3}
\]

Equation (1) is a positive binomial mixture of (3), while pointwise
nonnegativity in `alpha` cannot recover all the coefficientwise statements
(3).

There is a useful probability form.  Let `p` be the uniform face law and
let `q` be its `2^(-K)` tilt, where `K=|A|`.  If `d=n-m`, (3) is exactly

\[
 \boxed{
 {\mathbb E_q(n-K)_d\over\mathbb E_p(n-K)_d}
 \le {n\over n-d}.}                                    \tag{4}
\]

Thus the half-weight law, although biased toward smaller faces, may enlarge
every factorial moment of the omitted size by only the displayed factor.
The case `d=1` is the endpoint mean inequality below; the whole sequence
`d=1,...,n-1` is a genuine all-orders restriction constraint.

## 2. Exact multiscale curvature envelope

Put `L=ln 2` and

\[
 \Psi(\alpha)=\log {Z(\alpha)\over Z(\alpha/2)}
 =\int_{\alpha/2}^{\alpha}\mu_s\,d\log s.              \tag{5}
\]

Since `h=n exp(-Psi(1))`, (2) becomes

\[
 \Psi(\alpha)\ge \Psi(1)+
 \log\left(\alpha+(1-\alpha){\mu_{\alpha/2}\over n}\right). \tag{6}
\]

Also

\[
 {d\Psi(\alpha)\over d\log\alpha}
 =\mu_\alpha-\mu_{\alpha/2}
 =\int_{\alpha/2}^{\alpha}\sigma_s^2\,d\log s\ge0.    \tag{7}
\]

Combining (6)--(7) gives the strongest direct scalar consequence of all
Bernoulli restrictions:

\[
 \boxed{
 0\le\int_\alpha^1(\mu_t-\mu_{t/2})\,d\log t
 \le-\log\left(\alpha+(1-\alpha){\mu_{\alpha/2}\over n}\right).
 }                                                       \tag{MC}
\]

For `alpha<=1/2`, the left side has the exact curvature decomposition

\[
\begin{aligned}
 &\int_{\alpha/2}^{\alpha}\log(2s/\alpha)\sigma_s^2\,d\log s
 +(\log2)\int_\alpha^{1/2}\sigma_s^2\,d\log s\\
 &\hspace{35mm}
 +\int_{1/2}^1\log(1/s)\sigma_s^2\,d\log s.             \tag{8}
\end{aligned}
\]

So (MC) is not merely an endpoint derivative: it controls a triangularly
smoothed variance integral over every scale from `alpha/2` to one.

Letting `alpha` tend to one yields

\[
 \boxed{
 \Delta:=\mu_1-\mu_{1/2}
 =\int_{1/2}^1\sigma_s^2\,d\log s
 \le1-{\mu_{1/2}\over n}.}                             \tag{9}
\]

In particular, every global record is automatically in the `Delta<1`
branch of the activity-compensated program.  Moreover,

\[
 \boxed{
 \mu_{1/2}\le\log_2(n/h)\le\mu_1\le\mu_{1/2}+1.}      \tag{10}
\]

Thus at a restriction peak, proving `H=n^o(1)` is equivalent up to an
additive constant to proving the peak-mean target
`mu_1=(1-o(1))log_2 n`.  Curvature alone does not supply that lower bound.

Two other exact consequences are occasionally useful.  From (6) and the
fact that `Psi(alpha)/L<=mu_alpha`,

\[
 \mu_\alpha\ge\log_2(n/h)+
 \log_2\left(\alpha+(1-\alpha){\mu_{\alpha/2}\over n}\right)
 \ge\log_2(n\alpha/h).                                 \tag{11}
\]

And at the dyadic activities `alpha=2^(-j)`, (6) telescopes.  If
`R=log_2(n/h)` and `J=floor R`, then

\[
 \log_2 Z(1)\ge (J+1)R-{J(J+1)\over2}
 ={R^2\over2}+O(R).                                    \tag{12}
\]

This is a lower-growth certificate for a record with given `h`; its
direction is not enough to upper-bound `h`.

## 3. What the known count theorem gives

Let `K` be the rank under the uniform face law.  Entropy subadditivity and
concavity give

\[
 \log_2 Z(1)\le n\,h_2(\mu_1/n)
 \le\mu_1\log_2(en/\mu_1).                            \tag{13}
\]

The established planar lower bound

\[
 \log_2 Z(1)\ge(1/4-o(1))(\log_2n)^2                  \tag{14}
\]

therefore implies

\[
 \mu_1\ge(1/4-o(1))\log_2 n.                          \tag{15}
\]

Equations (9)--(10) then give

\[
 \boxed{H(P)\le n^{3/4+o(1)}.}                        \tag{16}
\]

This recovers, but does not improve, the unconditional rank-split bound
already present elsewhere in the campaign.  Feeding (MC) at smaller
activities does not improve the coefficient: the next section gives a
coherent obstruction satisfying the whole hierarchy.

## 4. Scalar sharpness: complete rank truncations

On an `N`-element abstract ground set, take the hereditary family

\[
 \mathcal U_{N,r}=\{A:|A|\le r\}.                      \tag{17}
\]

Every `m`-element restriction is the same complete rank-`r` truncation, with

\[
 Z_m(t)=\sum_{k=0}^{\min(r,m)}{m\choose k}t^k.          \tag{18}
\]

Fix `0<c<1` and set `r=(c+o(1))log_2N`.  At the top size,

\[
 \log_2 Z_N(1)=(c+o(1))(\log_2N)^2,
 \qquad H_N=N^{1-c+o(1)}.                              \tag{19}
\]

Choose `m_*<=N` maximizing `H_m`.  This is, by construction, a global
restriction peak.  Since `H_(m_*)>=H_N`, first `m_*>=N^(1-c+o(1))`, hence
`m_*` is much larger than `r^2`.  Uniformly in that range, the top rank
dominates both sums in (18), so

\[
 H_m=m2^{-r}(1+O(r/m)).                                 \tag{20}
\]

It follows that `m_*=(1-o(1))N`, and (19) holds with `m_*` in place of `N`.
Taking `c=1/4` produces a global restriction peak satisfying the known
count scale but having

\[
 H=m_*^{3/4+o(1)},\qquad \Delta=o(1).                  \tag{21}
\]

The same family has at least
`2^(1/4-o(1))(log_2 s)^2` members on every restriction size `s`; allowing
the known lower theorem at every random-restriction scale therefore does not
remove the obstruction.

This is not planar, and that distinction is exactly load-bearing.  In a
planar general-position set, if every four points are in convex position,
then every point is extreme: otherwise Carathéodory gives a triangle
containing it.  Hence the entire set, and then every subset, is in convex
position.  An exact shelf (17) with `r>=4` is impossible.  What is still
missing is a **quantitative** planar version: low curvature plus large mass
below rank `log n` must force enough repair/extension mass above that rank.
The existing cover identities and coarse first-switch moment bounds do not
yet give this stability statement.

## 5. Exact profile kills

The verifier records the following exact stress tests.

### The saved 58-point profile

For

\[
 (v_0,\ldots,v_{10})=
 (1,58,1653,30856,220958,428915,284982,76995,15100,2179,210),
\]

one has

\[
 H={33994061\over16990512},\qquad
 \Delta={4376001835655\over6638810360336}.
\]

The exact Bernoulli gap polynomial in (2) has nonnegative Bernstein
coefficients on `[0,1]`; hence it satisfies the whole all-`alpha` scalar
inequality, not just a grid.  Every fixed-size inequality (3) also passes,
with equality only at `m=58`; `m=57` is second best.  This does **not** prove
that all actual restrictions have smaller `H` (the profile averages cannot
see each restriction), but it shows that none of the symmetric scalar peak
tests detects the hard record.

It also retains the known exact kill

\[
 He^{-\Delta}=1.0349739\ldots>1,                       \tag{22}
\]

so the exponential replacement of `1-Delta` remains unavailable.

### Central Pascal cells

The twenty-point central Pascal profile

\[
 (1,20,190,1140,3225,4260,2116)
\]

satisfies the endpoint inequality (9), but it is not a global restriction
peak.  At the exact interior activity `alpha=1/8`,

\[
 hZ(\alpha)-\mathbb E[V(X)H(X)]
 =-{37467223311\over22968008704}<0,                    \tag{23}
\]

and the `V`-weighted average restriction value is
`195011719/161409280>H`.  The fixed-size hierarchy locates the strongest
average at `m=4`.  Therefore endpoint curvature is necessary but cannot be
used as a surrogate for the full peak hypothesis.

### Abstract three-truncation

For `v_k=binom(n,k)` at `k<=3` and zero above,

\[
 H\sim n/8,\qquad \Delta\sim3/n.                       \tag{24}
\]

For large `n`, the ambient size is the global restriction peak.  At `n=256`
the exact values in the certificate are `H=32.382375...` and
`Delta=0.011944...`.  This kills every generic claim that small curvature,
the all-orders restriction hierarchy, or global peak status by itself makes
`H` subpolynomial.  The logarithmic-rank truncations in Section 4 show that
adding the known total-count scale still stops exactly at exponent `3/4`.

## 6. Bottom line

The restriction-peak idea successfully localizes the remaining theorem:

\[
 \text{global peak}\Longrightarrow
 \Delta<1,\quad
 \mu_1=\log_2(n/H)+O(1),\quad
 \text{the full hierarchy (4) and (MC)}.                \tag{25}
\]

Consequently no separate high-curvature branch is needed at a global
record.  The desired `H=n^o(1)` is equivalent, at such a record, to the
planar assertion

\[
 \boxed{\text{a planar global restriction peak has }
 \mu_1\ge(1-o(1))\log_2n.}                              \tag{26}
\]

The stronger target `mu_1>=log_2 n-O(log log n)` would give a
polylogarithmic bound for `H` and is the natural quantitative form for the
activity-compensated induction.

Neither the restriction identities, the known `1/4` count theorem, nor
generic rank/entropy facts prove (26); complete rank truncations certify the
barrier.  A successful continuation must use quantitative planar repair
overlap to rule out an approximate shelf near rank `(1/4)log n` (and then
bootstrap that lower edge toward `log n`).

## 7. Reproduction

Run

```bash
python3 phase2/loop/erdos838/agent_restriction_peak_curvature/verify_peak_curvature.py
```

It writes `certificate.json` and checks all displayed exact rational values,
the all-`alpha` Bernstein certificate for `n=58`, every fixed-size
restriction inequality for that profile, the Pascal interior witness, and
the finite complete-truncation peaks.
