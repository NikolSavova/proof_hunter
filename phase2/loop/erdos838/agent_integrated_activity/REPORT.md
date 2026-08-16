# Integrated activity along the deletion path

**Date:** 2026-08-14  
**Verdict:** the full theorem is not closed in this lane.  There is, however,
a substantially sharper exact target than the one-step deletion inequality.
The half-activity deletion chain has an explicit path law, and the desired
half-weight inequality splits exactly into an accumulated normalized-variance
term and a path relative entropy.  The accumulated-variance term alone
survives all exhaustive and planar tests performed here.  A pointwise version
for every deletion order is false on an exact 24-point planar configuration,
so the expectation in the candidate theorem is essential.

All logarithms in this report are natural.  Put `h=1/2`, and include the empty
convex subset in every partition function.

## 1. The KL-corrected one-step identity

Write

\[
 Z_S(t)=\sum_{A\text{ convex in }S}t^{|A|},\qquad
 \mu_t(S)=t\frac{Z'_S(t)}{Z_S(t)},\qquad
 L(S)=\log\frac{Z_S(1)}{Z_S(h)}.
\]

For `p in S`, define the activity-`t` deletion law

\[
 q_t(p\mid S)=
 \frac{Z_{S-p}(t)}{\sum_xZ_{S-x}(t)}
 =\frac{Z_{S-p}(t)}{(m-\mu_t(S))Z_S(t)},\qquad m=|S|.       \tag{1}
\]

Set

\[
 r(S)=\log\frac{m-\mu_h(S)}{m-\mu_1(S)}.                    \tag{2}
\]

The likelihood ratio is

\[
 \log\frac{q_h(p\mid S)}{q_1(p\mid S)}
 =L(S)-L(S-p)-r(S).
\]

Taking expectations in the two directions gives the exact pair

\[
 \boxed{L(S)=\mathbb E_{q_h}L(S-p)+r(S)+D(q_h\Vert q_1),}   \tag{3}
\]

\[
 \boxed{L(S)=\mathbb E_{q_1}L(S-p)+r(S)-D(q_1\Vert q_h).}   \tag{4}
\]

This is strictly sharper than the arithmetic-mean recursion for `H`: it
identifies all deletion heterogeneity as a relative-entropy correction.

Moreover, since `d mu_t / d log t = Var_t K`, (2) is precisely

\[
 \boxed{
 r(S)=\int_h^1\frac{\operatorname{Var}_t K(S)}{m-\mu_t(S)}
 \,d\log t.}                                               \tag{5}
\]

Thus the scalar drift is not merely related to activity variance; it is its
exact normalized integral.

## 2. Explicit deletion-path law and martingale identity

Starting at `P`, repeatedly delete using (1), and let

\[
 P=S_n\supset S_{n-1}\supset\cdots\supset S_0=\varnothing
\]

be the resulting path.  Denote its law by `mathbb P_t`.  Multiplying the
transition probabilities makes every intermediate partition function
cancel:

\[
 \boxed{
 \mathbb P_t(\pi)=\frac1{Z_P(t)}
 \prod_{m=1}^n\frac1{m-\mu_t(S_m)}.}                        \tag{6}
\]

Define the path functional

\[
 X(\pi)=\sum_{m=1}^n r(S_m)
 =\sum_{m=1}^n\int_h^1
 \frac{\operatorname{Var}_tK(S_m)}{m-\mu_t(S_m)}\,d\log t. \tag{7}
\]

Equations (5)--(6) imply

\[
 \boxed{\frac{d\mathbb P_1}{d\mathbb P_h}(\pi)
       =\exp(X(\pi)-L(P)),}                                \tag{8}
\]

and hence

\[
 \boxed{\mathbb E_h e^X=e^{L(P)},\qquad
 L(P)=\mathbb E_hX+D(\mathbb P_h\Vert\mathbb P_1).}        \tag{9}
\]

The first equality can also be read as a multiplicative martingale: if
`M(S)=exp L(S)`, then

\[
 \mathbb E_{q_h}M(S-p)=M(S)e^{-r(S)}.
\]

## 3. The surviving exact candidate theorem

The strongest clean statement supported by the campaign is

> **Integrated deletion-path conjecture.**  For every general-position
> planar point set `P` of size `n`, or at least for every minimum-count one,
> \[
> \boxed{\mathbb E_{\mathbb P_h}X\ge\log(n/2).}             \tag{IDP}
> \]

By (9), `(IDP)` is stronger than `H(P)<=2`, and therefore closes Erdős 838.
For the asymptotic theorem the weaker right side `(1-o(1))log n` suffices.

There are two equivalent formulations worth retaining:

\[
 D(\mathbb P_h\Vert\mathbb P_1)
 \le L(P)-\log(n/2)=\log\frac2{H(P)},                       \tag{10}
\]

and the Bellman recursion

\[
 R(S)=r(S)+\mathbb E_{q_h}R(S-p),\quad R(\varnothing)=0,
 \qquad R(P)\ge\log(n/2).                                  \tag{11}
\]

Equation (10) is perhaps the most promising proof interface.  It asks for an
information-contraction theorem: the information about the activity retained
by the whole deletion order must fit inside the half-weight slack.

## 4. What the exact data say

The direct `2^20` hull and subset-zeta calculation on the saved planar record
with profile

\[
 (1,20,190,1140,2415,866,135,8)
\]

gives

\[
 \begin{array}{rcl}
 L(P)&=&2.527898864024565,\\
 R(P)=\mathbb E_hX&=&2.525362476602472,\\
 D(\mathbb P_h\Vert\mathbb P_1)&=&0.002536387422094,\\
 \log(20/2)&=&2.302585092994046.
 \end{array}
\]

Thus the path entropy is tiny and the stronger variance term has slack
`0.222777383608426`.

Exhausting every type-A reflection-order commutation class through seven
wires gives:

| `n` | classes | minimum `R` | `log(n/2)` | minimum over individual paths |
|---:|---:|---:|---:|---:|
| 3 | 2 | 0.863046 | 0.405465 | 0.863046 |
| 4 | 8 | 1.098612 | 0.693147 | 1.098612 |
| 5 | 62 | 1.306030 | 0.916291 | 1.295503 |
| 6 | 908 | 1.461036 | 1.098612 | 1.450509 |
| 7 | 24,698 | 1.603007 | 1.252763 | 1.578965 |

Direct hull/zeta tests on standard realizable families also pass `(IDP)`:

| family | `n` | `R` | `log(n/2)` |
|---|---:|---:|---:|
| dyadic Horton | 8 | 2.018582 | 1.386294 |
| dyadic Horton | 16 | 3.024032 | 2.079442 |
| nested triangles | 9 | 1.897416 | 1.504077 |
| nested triangles | 15 | 2.450425 | 2.014903 |
| parabola / all points convex | arbitrary | `n log(4/3)` | `log(n/2)` |

For the parabola the formula is exact at every size: `Z=(1+t)^n`, every
deletion is identical, `r=log(4/3)`, and the path KL is zero.

The abstract uniform rank-three complex shows that planarity is essential.
It contains every set of size at most three but has
`L=log(Z(1)/Z(1/2))=O(1)`, and so violates `(IDP)` for large `n`.  Rooted
four-circuit geometry, not merely the complete 2-skeleton, must enter a proof.

## 5. The expectation cannot be removed

The tempting pointwise strengthening

\[
 X(\pi)\ge\log(n/2)\quad\text{for every deletion order }\pi
\]

is false.  On the exact integer-coordinate 24-point half-weight record, the
original-label deletion order

```text
4,12,16,1,14,9,18,2,10,11,15,5,22,13,19,17,20,3,6,7,0,8,21
```

leaves label `23` last and has

\[
 X=2.473702217824751<\log12=2.484906649788000.
\]

Every state polynomial and rational endpoint mean on this path is replayed in
`certificate.json`.  A beam search on the exact 30-point record finds an even
larger pointwise deficit (`2.61478` versus `log 15=2.70805`), but that row is
reported only as search evidence because its full path was not banked here.

This counterexample is conceptually useful: a proof has to use the `q_h`
weights or an equivalent information argument.  No deterministic nested-set
inequality can establish `(IDP)`.

## 6. Other scalar potentials that were audited

For the face measures `nu_t(A)=t^|A|/Z(t)`, define the two endpoint
divergences

\[
 D_h=D(\nu_h\Vert\nu_1)=L-(\log2)\mu_h,
 \qquad
 D_1=D(\nu_1\Vert\nu_h)=(\log2)\mu_1-L.                    \tag{12}
\]

Their sum is `(log 2)(mu_1-mu_h)`.  Under `q_h`, differentiation of the
omitted-point identity gives

\[
 D_h(S)-\mathbb E D_h(S-p)
 =r(S)+D(q_h\Vert q_1)
  -(\log2)\frac{\operatorname{Var}_hK}{m-\mu_h}.           \tag{13}
\]

The exact records rule out the simplest fixed linear correction.  At `n=8,9,
20,24`, the drifts of both endpoint divergences are negative while the `L`
drift is already below `log(n/(n-1))`; at `n=30`, both divergence drifts are
positive while the `L` drift is still short.  Likewise the drift of
`mu_1-mu_h` changes sign between the 24- and 30-point records.  Consequently
no sign-uniform addition/subtraction of these scalar endpoint potentials gives
the desired one-step induction across the exact records.

Block deletion does not repair this.  If `q_t^(m)(Q)` is proportional to
`Z_Q(t)` over all `m`-subsets, then

\[
 L(P)=\mathbb E_{q_h^{(m)}}L(Q)
 +\log\frac{\mathbb E_h\binom{n-K}{m-K}}
             {\mathbb E_1\binom{n-K}{m-K}}
 +D(q_h^{(m)}\Vert q_1^{(m)}).                             \tag{14}
\]

On the exact 20-point record, the ratio of this block drift to `log(n/m)` is
`0.7350` at `m=10`; its maximum over all proper block sizes is only `0.8776`
at `m=3`.  The full path succeeds even though every fixed block scale fails.

## 7. Remaining proof gate

The precise missing statement is now (10), or equivalently `(IDP)`.  A planar
proof has to charge the path relative entropy to the half-weight slack.  At a
state `S`, the only difference between deletion probabilities comes from the
ratios `Z_{S-p}(h)/Z_{S-p}(1)`.  Those ratios change when deleting `p` removes
rooted four-circuit obstructions.  The plausible geometric route is therefore:

1. expose, under `q_h`, the first scale at which a rooted circuit blocks a
   deletion;
2. charge the local log-likelihood fluctuation to the same circuit's creation
   of activity variance at a later state;
3. prove bounded expected reuse of a rooted circuit along the random deletion
   path.

One-step visible-chain fibres are known to be exponential, so the last charge
must be multistep.  The advantage of (10) is that it asks only for a total
information budget, not a bounded fibre at each state.

## 8. Reproduction

```bash
python3 phase2/loop/erdos838/agent_integrated_activity/integrated_activity.py

python3 phase2/loop/erdos838/agent_integrated_activity/exhaustive_path_variance.py

python3 phase2/loop/erdos838/agent_integrated_activity/family_path_probe.py

c++ -O3 -std=c++17 \
  phase2/loop/erdos838/agent_integrated_activity/block_deletion_probe.cpp \
  -o /tmp/block_deletion_probe
/tmp/block_deletion_probe
```

The Python certificates use exact rational partition functions and moments;
floating point appears only in logarithms and KL displays.  The C++ program
classifies all `2^20` subsets by exact integer orientations and performs the
subset zeta transforms with integers before taking logarithms.
