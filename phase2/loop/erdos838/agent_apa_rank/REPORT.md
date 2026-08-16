# Averaged arbitrary-point deletion is false

**Date:** 2026-08-14  
**Verdict:** the proposed all-point average

\[
 nZ_P(1/2)+\frac{n-1}{2}Z'_P(1/2)\leq2Z'_P(1)       \tag{APA}
\]

is false for a planar point set in general position.  The first exact
rational counterexample has 44 points.  A stronger exact 58-point example
also has `H>2`, has `H<2` after every one-point deletion, and defeats every
individual rooted inequality, including the unique deepest onion point.
Thus the constant-two average, existential, and deepest-point deletion
routes all fail.  The asymptotic target `H=n^o(1)` remains open.

## 1. Exact certificate

The rational coordinates are stored as terminating decimals in
`verify_apa_counterexample.py`; Python parses them with `Fraction`, so no
floating-point assertion enters the certificate.  All
`binom(44,3)=13244` determinants are nonzero.  Two independent exact
enumerations agree on the convex-subset rank profile:

\[
 (v_0,\ldots,v_9)
 =(1,44,946,13244,70450,99093,43597,8726,1075,53).       \tag{1}
\]

The first enumeration directly multiplies the upper- and lower-monotone
path polynomials for every horizontal endpoint pair.  The second uses the
reverse reflection-order matrix product.

From (1),

\[
\begin{aligned}
 Z(1)&=237229,& Z'(1)&=1150674,\\
 Z(1/2)&=\frac{5206251}{512},&
 \frac12Z'(1/2)&=\frac{22095989}{512}.
\end{aligned}
\]

Consequently

\[
 \frac{\text{APA LHS}}{\text{APA RHS}}
 =\frac{1179202571}{1178290176}
 =1.000774338120256\ldots,                              \tag{2}
\]

and the strict violation is

\[
 \text{LHS}-\text{RHS}=\frac{912395}{512}>0.            \tag{3}
\]

The half-weight ratio itself is still below two:

\[
 H(P)=\frac{44Z(1/2)}{Z(1)}
 =\frac{57268761}{30365312}=1.8859928394\ldots .         \tag{4}
\]

Thus this is a counterexample only to the stronger induction lemma, not to
the target half-weight theorem.

## 2. Where the violation lives

Writing APA as

\[
 \sum_kv_k\left[2k-\frac{44+43k}{2^k}\right]\geq0,
\]

the contributions to **LHS minus RHS** of the original APA inequality are

\[
\begin{array}{c|rrrrrrrrrr}
k&0&1&2&3&4&5&6&7&8&9\\ \hline
&44&1826&26961&413875/2&387475
&-6044673/32&-10158101/32&-6313261/64
&-996525/64&-465605/512.
\end{array}                                             \tag{5}
\]

Ranks at most four create `622,243.5` units of debt.  Ranks five through
nine repay all but `912395/512`.  This confirms that the failure is exactly
an integrated low-rank/high-rank compensation defect, not a numerical edge
case in one coefficient.

## 3. Individual deletion margins

For a point `e`, put

\[
 m_e=2V_e-Z(1/2)-43W_e,
\]

where `V_e` is the number of convex faces containing `e` and `W_e` is their
half-weight.  Positive `m_e` is precisely the individual arbitrary-point RA
inequality.  Exact deletion replay gives

\[
 \sum_em_e=-\frac{912395}{512},
\]

with 21 positive and 23 negative margins.  The worst point has
`m_e=-1449197/512`; the best has `m_e=1370859/512`.  Hence averaging has
genuinely failed even though many valid induction points remain.

This leaves the sharper live question:

> Does every planar point set have **some** point satisfying the individual
> arbitrary-point rooted amortization inequality?

The counterexample does not answer that question.

## 4. The finite half-weight strengthening is also false

A continuation of the same search gives an exact 58-point general-position
configuration with profile

\[
 (1,58,1653,30856,220958,428915,284982,76995,15100,2179,210).
\]

For this configuration,

\[
 Z(1)=1061907,\qquad Z(1/2)=\frac{1172209}{32},
\]

and hence

\[
 \boxed{
 H(P)=\frac{58Z(1/2)}{Z(1)}
 =\frac{33994061}{16990512}
 =2.000767310602529\ldots>2.}
\]

The strict excess is `13037/16990512`.  This kills the attractive finite
strengthening `H<=2`.  It does **not** kill the asymptotic target
`H(P)=n^o(1)`, which is all that the coefficient-one-half proof needs.

This example is deletion-minimal for the strict threshold: every one of its
58 one-point deletions has `H<2`.  Consequently every individual
arbitrary-point RA margin is strictly negative.  Thus the same exact
configuration kills the existential arbitrary-point deletion lemma, not
just its average.

It also kills the proposed innermost-onion rescue.  The exact onion-layer
sizes are

```text
4,4,4,4,4,4,4,6,6,6,7,4,1.
```

The unique deepest point is input label 53, and its rooted margin is
`-1695735/512`.  Hence neither an arbitrary point nor a deepest-layer point
can support the constant-two induction.

The independent verifier is `verify_half_weight_counterexample.py`.

## 5. The finite excess does not amplify by standard composition

The 58-point configuration can itself be used as the outer template in the
exact homogeneous directional composition.  Its cap and cup profiles were
computed directly from the rational order type, and the exact scalar
composition recurrence was evaluated at both activities.  The resulting
half-weight ratios at depths one, two, and three are

```text
2.000767310602529, 0.027692998601684, 0.000008275685580.
```

They continue to decrease rapidly.  Hence this finite counterexample does
not bootstrap into a counterexample to `H=n^o(1)` through the standard
vertical blow-up.  The checker is `amplification_probe.py`.

## 6. Reproduction

Run from the repository root:

```bash
python3 phase2/loop/erdos838/agent_apa_rank/verify_apa_counterexample.py \
  > /tmp/apa_counterexample.json

python3 phase2/loop/erdos838/agent_apa_rank/verify_half_weight_counterexample.py \
  > /tmp/half_weight_counterexample.json

python3 phase2/loop/erdos838/agent_apa_rank/amplification_probe.py \
  > /tmp/half_weight_amplification.json
```

The verifiers check general position, two exact parent-profile enumerations,
every displayed fraction, all 44 and all 58 deletion profiles, the rank
decomposition, the onion layers, and the signs of all individual rooted
margins.  The composition probe derives both cap/cup profiles from the same
exact rational order type.
