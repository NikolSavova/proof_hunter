# Cyclic stems, random half-hulls, and the low-mean minimizer gate

**Date:** 2026-08-14  
**Verdict:** this lane does not close Erdős 838.  It does put Gordon's planar
antimatroid theorem on the exact half-weight probability space: the desired
partition function is the **exponential moment of the number of points
omitted by the convex hull of a random half-sample**, while Gordon's cyclic
minimal-feasible-set formula computes its first moment.  Thus the missing
upgrade is now unambiguously a joint-exposure/tail theorem, not another
Tutte-polynomial substitution.

The second requested route, the low-mean minimizer dichotomy, also remains
open.  A natural entropy--variance deletion induction for its quadratic
potential is false on the exact nine-point minimizer, for every direct block
size.  Central Pascal cells remain the universal QMS counterfamily but lie
in the high-mean branch.  An exact 58-point planar record lies in a genuine
finite low-mean regime and still violates sharp QMS, but is **not known to be
a minimizer**.  These distinctions are essential.

All logarithms below are base two.  The empty convex subset is included.

## 1. The exact random-hull form of the half-weight target

Let `P` have `n` points.  For a closed set `K` in its affine convex geometry,
write

\[
 H(K)=|\operatorname{ext}K|,\qquad
 I(K)=|K|-H(K),\qquad
 O(K)=n-|K|.
\]

There are two natural probability laws on closed sets:

\[
 \pi_0(K)=\frac1V,\qquad
 \pi_1(K)=\frac{2^{I(K)}}{2^n},                 \tag{1}
\]

where `V=Z_P(1)` is the number of closed sets.  The Boolean-interval identity
`sum_K 2^I=2^n` normalizes `pi_1`.

The second law has a direct sampling interpretation.  Choose a Bernoulli
half-subset `T` of `P` and put `K=cl(T)`.  Then

\[
 \Pr(\operatorname{cl}T=K)=\frac{2^{I(K)}}{2^n},             \tag{2}
\]

because the subsets generating `K` are precisely

\[
 \operatorname{ext}K\subseteq T\subseteq K.
\]

Let `A` be the shelling antimatroid dual to the affine convex geometry.  Its
rank on `S=P-T` is

\[
 r_{\mathcal A}(S)=n-|\operatorname{cl}T|=O(K).              \tag{3}
\]

Consequently Gordon's expected rank at `p=1/2` is exactly

\[
 \boxed{\operatorname{er}_{\mathcal A}(1/2)
       =\mathbb E_{\pi_1}O.}                                \tag{4}
\]

The previously found Tutte bridge sharpens at the next line:

\[
 \begin{aligned}
 Z_P(1/2)
 &=\sum_K2^{-H(K)}\\
 &=2^{-n}\sum_K2^{I(K)+O(K)}\\
 &=\boxed{\mathbb E_{\pi_1}2^{O}}.                          \tag{5}
 \end{aligned}
\]

Thus Gordon computes the first moment of the exact random variable whose
exponential moment is the half-weight target.  In factorial-moment form,

\[
 Z_P(1/2)=\sum_{j\ge0}\mathbb E_{\pi_1}{O\choose j}
 =\sum_{X\subseteq P}\Pr_{\pi_1}(X\cap K=\varnothing).       \tag{6}
\]

Gordon's theorem is the `j=1` layer of (6).  The unrestricted asymptotic
half-weight statement is precisely

\[
 \mathbb E_{\pi_1}2^O\le \frac{V}{n^{1-o(1)}}.              \tag{7}
\]

The disproved finite strengthening `H(P)<=2` would replace the right side by
`2V/n`.

## 2. What the cyclic stem theorem gives exactly

Fix an interior point `x`, and put `U=P-{x}`.  Let
`F_1,...,F_k` be the inclusion-minimal open-halfplane traces which must be
pruned to expose `x`, in cyclic order.  Gordon's planar theorem says

\[
 U\setminus(F_i\cup F_{i+1})=F_{\tau(i)}                 \tag{8}
\]

for a permutation `tau`.  If `a_i=|F_i|`, cyclic
inclusion--exclusion therefore gives

\[
 \Pr(x\notin\operatorname{cl}T)
 =\frac12\left(
   \sum_i2^{-a_i}
  -\sum_i2^{-(n-1-a_i)}
  +2^{-(n-1)}\right).                                      \tag{9}
\]

The factor `1/2` is the probability that `x` itself is absent from `T`.
For a hull point the probability is simply `1/2`.  Summing (9) is exactly
(4).

On the exact configuration attaining `f(9)=169`, the hull has three points.
The six interior cyclic stem-size lists are

```text
1,3,4     1,3,4     2,3,3,4,4
2,3,3,4,4 2,3,3,4,4 1,3,4.
```

Direct rational evaluation gives

\[
 \operatorname{er}(1/2)=\mathbb E_{\pi_1}O={387\over128},
 \qquad
 \mathbb E_{\pi_1}2^O=Z(1/2)={875\over32}.                 \tag{10}
\]

The verifier independently enumerates the halfplane cells, finds the minimal
stems, reconstructs their Gordon adjacency cycle, checks (8) set by set, and
checks (9) against brute-force inclusion--exclusion.  It then independently
enumerates all closed sets and verifies both equalities in (10).

The obstruction is now sharp: (9) controls only single-point exposure.  An
upper bound on (5) requires simultaneous control of

\[
 \Pr(x_1,\ldots,x_j\notin\operatorname{cl}T)                \tag{11}
\]

summed over all `j` and all `j`-sets.  The one-point cyclic cycles for
different roots share halfplanes and can be strongly positively correlated.
No valid bounded-overlap theorem for these joint cycles was found.

## 3. The exact change-of-measure obstruction

The uniform closed-set law is the mean-size/QMS law, while Gordon naturally
lives under the interior-weighted law.  Their relative entropy is exactly

\[
 \boxed{
 D_2(\pi_0\Vert\pi_1)
 =n-\log V-\mathbb E_{\pi_0}I
 =\mu+\mathbb E_{\pi_0}O-\log V.}                          \tag{12}
\]

This is precisely the slack in the Boolean-coverage inequality
`log V <= mu + E_0 O`.  On the exact nine-point minimizer,

\[
 \mu={492\over169},\qquad
 \mathbb E_{\pi_0}O={918\over169},\qquad
 \mathbb E_{\pi_1}O={387\over128}.                         \tag{13}

Thus the tilt reduces the omitted mean from about `5.432` to `3.023`.
Gordon's exact weighted mean does not by itself control the uniform omitted
mean needed by the low-mean coverage target.

Equivalently, for
`pi_theta(K) proportional to 2^(theta I(K))`, interpolation gives

\[
 {d\over d\theta}\mathbb E_{\pi_\theta}O
 =(\ln2)\operatorname{Cov}_{\pi_\theta}(O,I).               \tag{14}
\]

A successful low-mean proof through this interface needs a minimizer-specific
bound on the accumulated negative covariance in (14), or a direct
multi-root extension of (9).  Universal antimatroid identities do not supply
either bound.

## 4. A tempting QMS deletion induction is false on a minimizer

Let a uniformly random convex subset of `P` have mean `mu` and variance
`sigma^2`.  Put `V_p=V(P-p)`, `mu_p=mu(P-p)`, and use the deletion law

\[
 q(p)={V_p\over(n-\mu)V}.                                    \tag{15}
\]

Two exact identities are

\[
 \mu-\mathbb E_q\mu_p={\sigma^2\over n-\mu},                \tag{16}
\]

and

\[
 \log V-\mathbb E_q\log V_p
 =H_2(q)-\log(n-\mu).                                       \tag{17}
\]

It is natural to hope that the entropy defect in (17) pays for the small
variance in (16), yielding

\[
 \log V-\mathbb E_q\log V_p
 \le \mu(\mu-\mathbb E_q\mu_p).                            \tag{18}
\]

An even cleaner induction for sharp QMS would use

\[
 \log V-\mathbb E_q\log V_p
 \le {1\over2}(\mu^2-\mathbb E_q\mu_p^2).                  \tag{19}
\]

Both are false on the exact realizable minimizer at `n=9`:

```text
log-count drift                         0.563764919990160
mu times mean drift                    0.361199592953470
ratio                                  1.560812722352056
quadratic-potential drift              0.353492137034477
quadratic drift minus log-count drift -0.210272782955682
log(9) - H(q)                          0.000012250840368
```

The deletion law is almost perfectly uniform, so entropy heterogeneity does
not compensate for variance `0.7554...`.

The failure is not repaired by deleting a fixed-size block directly.  For
each `m=1,...,8`, put

\[
 q_m(Q)={V(Q)\over\sum_{|R|=m}V(R)}.
\]

The exact subset-zeta replay finds

\[
 {1\over2}(\mu(P)^2-\mathbb E_{q_m}\mu(Q)^2)
 -\{\log V(P)-\mathbb E_{q_m}\log V(Q)\}<0                 \tag{20}
\]

for **every** `m`; the margins range from `-2.2882...` at `m=1` to
`-0.21027...` at `m=8`.  This rules out the most direct block-Bellman proof
of the minimizer QMS dichotomy.  It does not refute an asymptotic QMS theorem,
because finite linear or lower-order errors could absorb these margins.

## 5. Stress tests and the quantifier boundary

### Central Pascal cells: universal QMS is false, but in the high-mean branch

Exact recurrence values are:

| family | `mu-log n` | `log V/(mu^2/2)` |
|---|---:|---:|
| `T_(32,16)` | 2.471097 | 1.099359 |
| `T_(64,32)` | 3.131716 | 1.164508 |
| `T_(128,64)` | 3.720874 | 1.210563 |

These rigorously kill universal QMS and every argument which silently uses
it.  They do **not** refute the proposed minimizer dichotomy: their mean is
larger than `log n`, with growing positive slack, so they belong to branch
(A), not the low-mean branch.

### The 58-point record: low mean and QMS failure, but not a minimizer

For the exact planar profile

\[
(1,58,1653,30856,220958,428915,284982,76995,15100,2179,210)
\]

one has

\[
 \mu=5.194152595\ldots<0.9\log58,
 \qquad {\log V\over\mu^2/2}=1.483973600\ldots.             \tag{21}
\]

Thus even the finite universal implication
`mu <= 0.9 log n => log V <= mu^2/2` is false for planar sets.  Its one-step
quadratic-potential margin is also negative, `-0.0346387...`.

This record is **not known to attain `f(58)`**.  It therefore does not refute
the requested asymptotic statement for actual minimizers.  Nor does its
standard homogeneous composition produce an asymptotic low-mean family: as
recorded in the source attack, the finite half-weight excess rapidly decays
under iteration.

### The nine-point record: an actual minimizer, but only finite

Subject to the documented completeness of the realizable order-type
database, the nine-point configuration used above attains `f(9)=169`.
It refutes the zero-error local inductions (18)--(20).  It does not refute

\[
 \log V(P_n)\le(1/2+o(1))\mu(P_n)^2
\]

along an asymptotic sequence of low-mean minimizers.

## 6. Best remaining theorem interfaces

The cyclic route has reduced the missing geometric statement to either of
the following.

1. **Joint cyclic exposure.**  Prove (7) by summing the multi-root events
   (11), using common-endpoint/circuit elimination to prevent too many roots
   from reusing the same short halfplane certificate.
2. **Minimizer tilt control.**  In the branch
   `mu <= (1-epsilon)log n`, prove a minimizer-specific bound on the negative
   covariance integral (14) strong enough to give
   `E_0 O <= mu^2/2-mu+o(mu^2)`.
3. **Nonlocal pocket reset.**  Interpret a minimal stem as the first shelling
   time at which a point becomes exposed.  Gordon's complement-of-adjacent-
   unions rule supplies the exact cyclic reset, but the charge must retain a
   multi-root tag; one-point inclusion--exclusion loses precisely the joint
   history needed in (6).

The first target is closer to the unrestricted half-weight theorem.  The
second uses the minimizer quantifier but currently has no local deletion
proof, as (20) demonstrates.

## 7. Verification

From the repository root:

```bash
python3 \
  phase2/loop/erdos838/agent_cyclic_stem_hw/verify_cyclic_stem_bridge.py
```

The script writes `certificate.json`.  Stem sets, complement relations,
profiles, closed-set weights, Boolean-hull moments, and deletion counts are
checked with exact integer/rational arithmetic.  Logarithmic drift signs are
evaluated only after exact reconstruction and have margins far exceeding
floating-point error.  The 58-point child scan uses the independent exact
reflection-product profile routine.

## Source

Gary Gordon, *Expected rank in antimatroids*, Advances in Applied Mathematics
32 (2004), 299--318, especially Lemma 4.2 and Theorem 4.4:
<https://webbox.lafayette.edu/~gordong/pubs/exrank.pdf>.
