# Erdős 838: half-weight attack

**Date:** 2026-08-13
**Verdict:** the asymptotic half-weight inequality remains open.  The exact
constant-two target survives every available test, but the most tempting
activity proof of it is false on explicit planar configurations.  The useful
new output is an exact random-prefix representation which turns the problem
into a geometric stopping-time estimate, together with an exact deletion
recursion and independently replayable counterexamples to two overly strong
local targets.

The empty convex subset is included throughout.  Put

\[
 Z_P(z)=\sum_{A\text{ convex}}z^{|A|},\qquad
 H(P)=\frac{nZ_P(1/2)}{Z_P(1)},\qquad
 \mu_z=z\frac{Z'_P(z)}{Z_P(z)}.
\]

## 1. What would solve the problem

The target

\[
 H(P)=n^{o(1)}                                                   \tag{HW}
\]

implies the required mean estimate.  Indeed, under the uniform law on convex
subsets,

\[
 \frac{Z_P(1/2)}{Z_P(1)}=\mathbb E2^{-|A|}
 \ge 2^{-\mathbb E|A|},
\]

so (HW) gives

\[
 \mu_1\ge \log_2n-o(\log n).
\]

The already proved deletion argument then gives the lower coefficient
`1/2` for `log f(n)/(log n)^2`.  The attractive exact conjecture is

\[
 \boxed{H(P)\le2.}                                               \tag{HW2}
\]

No counterexample to (HW) or (HW2) was found.

There is an activity-half sufficient condition:

\[
 \mu_{1/2}\ge\log_2 n-1\quad\Longrightarrow\quad H(P)\le2,       \tag{1}
\]

because under the `z=1/2` Gibbs law,

\[
 \frac{Z_P(1)}{Z_P(1/2)}=\mathbb E_{1/2}2^{|A|}
 \ge2^{\mu_{1/2}}.
\]

Section 3 shows that the premise of (1) is false.  The asymptotic weakening
`mu_(1/2) >= log n-o(log n)` remains viable and is itself enough for (HW).

## 2. Exact interfaces

### 2.1 Weighted up-degree

Let `u(A)` be the number of points which can be added to `A` while preserving
convex position.  Double-counting cover relations in the independence
complex gives, for every activity `z`,

\[
 \mathbb E_z u(A)=\frac{\mu_z}{z}.                                \tag{2}
\]

Thus the surviving activity target is equivalently

\[
 \mathbb E_{1/2}u(A)\ge(2-o(1))\log_2n.                           \tag{3}
\]

This is a clean weighted level-flow statement.  Pointwise versions are
impossible: an outer triangle can have up-degree zero while containing all
other points.

### 2.2 Deletion recursion

For `p in P`, write `Z_p(z)=Z_{P-p}(z)`.  The omitted-point identity

\[
 \sum_pZ_p(z)=(n-\mu_z)Z_P(z)                                    \tag{4}
\]

implies the exact recursion

\[
 \boxed{
 \mathbb E_{p\propto Z_p(1)}H(P-p)
 =\frac{n-1}{n}\frac{n-\mu_{1/2}}{n-\mu_1}H(P).}                 \tag{5}
\]

If `R_n=max H(P)` over the relevant class of `n`-point orders, then

\[
 R_n\le \frac n{n-1}\frac{n-\mu_1(P)}{n-\mu_{1/2}(P)}R_{n-1}    \tag{6}
\]

at an `H`-maximizer `P`.  This is rigorous but not self-closing.  On the
adversarial records the activity gap `mu_1-mu_(1/2)` is about `0.53--0.59`,
so multiplying (6) naively permits a positive power of `n`.  A proof from
(5) must exploit slack among the children or add a second potential.

The exact checker verifies (5) on all twenty deletions of the saved `n=20`
configuration, preserving the original (non-equally-spaced after deletion)
coordinates.

### 2.3 Reflection-order matrix form

For a reflection order `R` on the positive roots of type `A`, set

\[
 B_R(z)=\prod_{\alpha\in R}(I+zE_\alpha),\qquad
 A_R(z)=\prod_{\alpha\in R^{\rm rev}}(I+zE_\alpha).
\]

Nilpotence of every `E_alpha` gives the exact inverse relation

\[
 A_R(z)=B_R(-z)^{-1}.                                             \tag{7}
\]

Moreover,

\[
 Z_R(z)=1+nz+\langle A_R(z),B_R(z)\rangle_F-n.                    \tag{8}
\]

Thus (HW2) is the pure Coxeter/matrix inequality

\[
 n\{1+n/2+\langle B_R(-1/2)^{-1},B_R(1/2)\rangle_F-n\}
 \le2\{1+\langle B_R(-1)^{-1},B_R(1)\rangle_F\}.                 \tag{9}
\]

The identity (7) is promising, but total positivity alone does not currently
compare the two Frobenius pairings.  The earlier ten-wire certificate also
shows that an individual trace-descending long braid can increase the left
half-weight.

## 3. Exact obstruction to the activity-half shortcut

The saved integer fixed-`x` point configurations give the following exact
profiles:

\[
\begin{array}{c|l|c|c|c}
n& (v_0,v_1,\ldots)&H&\mu_{1/2}-(\log_2n-1)&\operatorname{Var}_{1/2}|A|\\
\hline
20&(1,20,190,1140,2415,866,135,8)&1.596531&+0.048353&0.848463\\
24&(1,24,276,2024,5378,2679,413,43,3)&1.686142&-0.022595&0.813858\\
30&(1,30,435,4060,13975,10607,3158,481,30)&1.730215&-0.082571&0.846232.
\end{array}
\]

Hence `mu_(1/2) >= log_2 n-1` is already false at `n=24`, and again at
`n=30`.  These are actual integer planar configurations, not pseudoline
orders.  Their slope orders and profiles are reconstructed exactly by
`half_weight_audit.py`; the independent direct-hull program elsewhere in the
repository additionally checks all `2^20` subsets of the first row.

The half-activity variances are also below one.  Therefore an induction which
needs a pointwise variance near `1/ln 2` is unavailable at activity one-half
just as it is at activity one.

This does **not** refute (HW2): all displayed `H` values remain below two.
The coordinate search reached its largest saved value `H=1.783466...` at
`n=31`; the rows are unrelated finite records and do not form a growing
counterfamily.

## 4. New random-prefix representation

This is the cleanest new structural reduction.

Let `F` be any simplicial complex on `[n]`; later take `F` to be the convex
subsets.  Choose a uniformly random permutation `pi` of `[n]`, and let

\[
 R(\pi)=\max\{r:\{\pi_1,\ldots,\pi_r\}\in F\}.                   \tag{10}
\]

Because `F` is hereditary, membership fails forever after the first bad
prefix.  If `v_k` is the number of `k`-faces, then

\[
 \Pr(R\ge k)=\frac{v_k}{\binom nk}.                               \tag{11}
\]

Writing

\[
 S_r(z)=\sum_{k=0}^r\binom nkz^k,
\]

and taking coefficients in (11) proves the exact mixture identity

\[
 \boxed{Z_F(z)=\mathbb E_\pi S_{R(\pi)}(z).}                      \tag{12}
\]

Now tilt the law of `R` by `S_R(1)`:

\[
 \Pr_*(R=r)=\frac{\Pr(R=r)S_r(1)}{Z_F(1)}.
\]

Then

\[
 \frac{H(F)}n
 =\mathbb E_*\rho_n(R),\qquad
 \rho_n(r)=\frac{S_r(1/2)}{S_r(1)}.                              \tag{13}
\]

For `r<(n+1)/3`, comparison with the top binomial term gives

\[
 \rho_n(r)
 \le 2^{-r}\frac{n-r+1}{n-3r+1}.                                \tag{14}
\]

Indeed, going down `j` levels from the top term in `S_r(1/2)` costs at most
`(2r/(n-r+1))^j`.  Conversely,

\[
 \rho_n(r)\ge
 2^{-r}\left(1-\frac{r}{n-r+1}\right),                          \tag{15}
\]

by upper-bounding `S_r(1)` with the corresponding geometric series.
Thus uniformly for `r=o(n)`,

\[
 \rho_n(r)=(1+O(r/n))2^{-r}.                                    \tag{16}
\]

The function `rho_n(r)` is decreasing in `r`, so larger stopping ranks are
harmless.  Consequently (HW) is reduced, up to negligible large-`r` terms,
to the tilted stopping-time estimate

\[
 \boxed{\mathbb E_*2^{-R}\le n^{-1+o(1)}.}                       \tag{PST}
\]

Unlike a restatement in terms of the final face-size distribution, `R` has a
direct geometric failure event.  Conditional on `R=r`, the first bad prefix
is created by the newly arriving point and a rooted four-circuit supported on
three previous points.  This suggests attacking (PST) by switching the first
witness rather than by trying to control all blocked points of an arbitrary
face simultaneously.

The certificate verifies (11)--(12) coefficientwise for the exact `n=20,24,30`
profiles.

## 5. Endpoint factorization: useful, but not enough by itself

With points sorted by horizontal coordinate, every nonsingleton convex face
has unique left and right endpoints `(i,j)` and decomposes into an upper and a
lower convex chain.  Hence

\[
 Z_P(z)=1+nz+\sum_{i<j}U_{ij}(z)C_{ij}(z).                       \tag{17}
\]

A natural weighted Erdős--Szekeres lemma would be

\[
 \mu_{1/2}(U_{ij})+\mu_{1/2}(C_{ij})
 \ge \log_2(j-i+1)-O(1).                                        \tag{WES}
\]

It passes every exact endpoint array at `n=8,9` (the worst observed deficit
is less than `0.18`).  Proving (WES) would be genuine progress: by Jensen it
would compare the endpoint product at activities one and one-half with a
factor proportional to its horizontal span.

The exact factor-one version is false.  In the saved eight-point minimizer,
the endpoint pair `(0,6)` has span seven and polynomial

\[
 U_{0,6}(z)C_{0,6}(z)=z^2+5z^3.
\]

Therefore its activity ratio is

\[
 \frac{F(1)}{F(1/2)}=\frac6{7/8}=\frac{48}7<7.                   \tag{18}
\]

A constant-loss WES remains plausible.  However, even a per-endpoint factor
`c(j-i+1)` does not immediately prove (HW), because many faces could be
concentrated in short horizontal intervals.  A complete proof needs a second
charge: localized endpoint mass must either have a much stronger activity
ratio (as a large Boolean subcomplex does), or create comparable faces in
many translated intervals.

## 6. Why generic convex-geometry machinery does not close the gap

The convex faces are the independent sets of the 4-uniform hypergraph whose
edges are the nonconvex four-tuples.  Equivalently they are the extreme-point
sets of closed sets in the Euclidean convex geometry.  Thus `|A|` is the
down-degree in the meet-distributive closure lattice.

Generic antimatroid, NBC-complex, shellability, or toggle-CDE statements do
not supply (HW).  Abstract convex geometries can have much smaller degree,
and the campaign already has an exact failure of the relevant toggle-CDE
property.  The load-bearing facts must be rank-three planarity, the rooted
four-circuit location, and probably global extremality.  A targeted literature
search found the standard convex-geometry/NBC identifications but no theorem
controlling `sum_K 2^{-|ext K|}` at the required `1/n` scale.

## 7. Recommended next attack

The best primary route is now (PST), in parallel with its endpoint version.

1. Choose an `H`-maximizing reflection order, not merely a trace minimizer.
   Global `H`-maximality gives a ratio inequality for every reachable braid
   state, stronger than lexicographic `(V,M)` minimality.
2. Expose the first rooted four-circuit in a random permutation and switch its
   arrival order.  Seek a bounded- or subpolynomial-fibre map from low `R` to
   larger `R`, with the crucial `S_R(1)` tilt retained.
3. Prove constant-loss (WES) by a weighted cup--cap recursion.  Then add a
   localization dichotomy: short-span mass either has exponentially strong
   activity decay or can be charged to many intervals.
4. Continue adversarial coordinate search for `H>2` and, more importantly,
   for a nested family with growing `H`.  The existing isolated records do
   not answer the asymptotic question.

At present there is no full proof and no counterfamily.  The sharp advance is
that the failed one-parameter shortcut has been removed, while (PST) gives a
specific planar switching problem whose success would prove (HW) directly.

## 8. Reproduction

Run

```bash
python3 phase2/loop/erdos838/agent_half_weight/half_weight_audit.py
```

It writes `certificate.json` and checks the exact profiles, `H`, half-activity
means and variances, the random-prefix mixture, and the `n=20` deletion
recursion.
