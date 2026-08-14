# The Coxeter half-weight attack

**Date:** 2026-08-13
**Verdict:** the sharp inequality

\[
   H(R):=\frac{nF_R(1/2)}{F_R(1)}\le 2                    \tag{HW}
\]

survives every exact and heuristic test performed here, but is not proved.
The principal rigorous result of this pass is negative and useful: the most
natural pointwise sufficient condition at activity `1/2` is false, even for
integer-coordinate planar point sets.  Thus a proof of (HW) has to use the
activity integral, not only its left endpoint.  Seeded Coxeter search improves
the unrestricted type-A records slightly to `H=1.59751, 1.69099, 1.73497` at
`n=20,24,30`; none is a counterexample.

## 1. Normalization

For a type-A reflection order `R`, put

\[
B_R(z)=\prod_R(I+zE_{ji}),\qquad
A_R(z)=\prod_{R^{\rm rev}}(I+zE_{ji})=B_R(-z)^{-1},
\]

with products interpreted in the row-update convention.  The raw Frobenius
trace

\[
Q_R(z)=\langle A_R(z),B_R(z)\rangle_F
\]

has constant term `n`: its diagonal entries encode the singletons only after
specialization at `z=1`.  The actual all-subsets convex partition function is

\[
\boxed{F_R(z)=1+nz+Q_R(z)-n.}                            \tag{1}
\]

Equation (HW), and everything below unless explicitly labelled `Q`, uses
`F`.  This distinction matters.  For example, the literal activity mean of
`Q` already fails the clean lower target at the eight-point lexicographic
minimum; that is merely a grading-normalization artifact.

Every reduced word supplies a type-A reflection order (equivalently, a
pseudoline/allowable-sequence order).  It need not be stretchable by straight
lines.  The three `planar_seed` records below *are* stretchable because their
words are reconstructed and checked from the saved integer fixed-`x`
coordinates.  The three `seeded` records obtained after arbitrary long braids
are certified only in the broader reflection-order class.

## 2. Exact activity lemma

Let

\[
 \mu_t=t\frac{F'_R(t)}{F_R(t)}.
\]

Under the probability law proportional to `t^|S|` on convex subsets,

\[
 \frac{d\mu_t}{d\log t}=\operatorname {Var}_t |S|\ge0.   \tag{2}
\]

Consequently

\[
 \log\frac{F_R(1)}{F_R(1/2)}
   =\int_{1/2}^{1}\mu_t\,d\log t
   \ge (\log2)\mu_{1/2}.                               \tag{3}
\]

This proves the rigorous implication

\[
 \boxed{\mu_{1/2}\ge\log_2n-1\quad\Longrightarrow\quad H(R)\le2.} \tag{4}
\]

More generally, `mu_(1/2) >= log_2 n-C` gives `H<=2^C`, while
`mu_(1/2)>=(1-o(1))log_2 n` gives the asymptotic fallback
`F(1)/F(1/2)>=n^(1-o(1))`.

There is a useful probabilistic reading.  A Bernoulli-`p` subset has
probability proportional to `(p/(1-p))^|S|` after conditioning on being
convex.  Therefore `mu_(1/2)` is the expected size of a `p=1/3` random subset
conditioned to be convex.  This is the cleanest entropy formulation found in
this pass.

## 3. The pointwise half-mean target is false, stretchably

The fixed-`x` integer records already stored in
`../agent_dual_number_amortization/half_weight_search_records.json` give the
following exact replays.

| `n` | `H=nF(1/2)/F(1)` | `mu_(1/2)` | `mu_(1/2)-(log_2 n-1)` |
|---:|---:|---:|---:|
| 20 | `4879/3056 = 1.596531...` | `82218/24395 = 3.370280...` | `+0.048353...` |
| 24 | `584943/346912 = 1.686142...` | `694594/194981 = 3.562363...` | **`-0.022595...`** |
| 30 | `226845/131108 = 1.730215...` | `925363/241968 = 3.824297...` | **`-0.082571...`** |

The verifier checks the integer coordinates for general position, sorts all
slopes exactly, reconstructs a reduced word, and evaluates both matrices over
`Fraction`.  Thus the last two rows rigorously refute the antecedent of (4)
for actual planar configurations, not merely nonstretchable reflection
orders.

This does **not** refute (HW).  In fact the rows retain substantial integral
slack:

\[
 \log_2\frac{F(1)}{F(1/2)}-(\log_2n-1)=\log_2\frac2H>0. \tag{5}
\]

At `n=30` this slack is about `0.209`.  Activity variance between `1/2` and
`1` raises the integrated mean enough to compensate for the negative endpoint
deficit.  The surviving sharp target is therefore exactly

\[
 \boxed{\int_{1/2}^{1}\mu_t\,d\log t\ge\log(n/2),}       \tag{6}
\]

or an amortized substitute for (6), rather than a pointwise bound at `1/2`.

## 4. Unrestricted Coxeter search

`half_weight_search.cpp` maximizes `H` by simulated annealing on ordinary
reduced words.  Adjacent short commutations change only the representative;
adjacent long braids move between commutation classes.  The objective
direction is **maximization**: large `H` is adversarial.  Because random
reduced words have very many faces and tiny `H`, useful runs must be seeded at
the planar low-face records.

Exact replay of the best saved outputs gives:

| `n` | starting planar `H` | unrestricted braid `H` | status |
|---:|---:|---:|---|
| 20 | `1.596531...` | `9355/5856 = 1.597507...` | valid reflection order |
| 24 | `1.686142...` | `582891/344704 = 1.690990...` | valid reflection order |
| 30 | `1.730215...` | `3618075/2085376 = 1.734975...` | valid reflection order |

The braid outputs are not claimed stretchable.  They show that leaving the
realizable subspace buys only a small finite improvement in these runs.  They
are heuristic lower bounds on the maximum of `H`, not upper bounds and not a
proof of (HW).  Together with the earlier exhaustive census through `n=7`,
they leave (HW) alive but increasingly close to its proposed constant.

## 5. What the algebraic approaches did and did not give

The inverse identity `A(z)=B(-z)^(-1)` supplies alternating coefficient
relations.  Its degree-two part is the positive conservation law

\[
 (A_2)_{j,i}+(B_2)_{j,i}=j-i-1,
\]

but higher-degree identities contain cancellations.  I found no valid total
positivity, PBW/canonical-basis, Hecke, or singular-value comparison that
relates the two *different specializations* `z=1/2` and `z=1` with the factor
`n/2`.  Determinant one and entrywise positivity are far too weak.

The earlier exact ten-wire braid already shows that lexicographic descent in
`(F(1),F'(1))` can increase `F(1/2)`.  The new endpoint counterexamples show
that even the stronger-looking direct estimate (4) cannot be the proof.
Thus the two shortest Coxeter strategies are genuinely blocked:

1. orient every long braid by the unweighted lexicographic objective and
   deduce half-weight monotonicity;
2. prove (HW) from the single endpoint value `mu_(1/2)>=log_2n-1`.

What remains plausible is an absolute, activity-integrated charge.  In matrix
terms it must control the common prefix/suffix bases over the whole interval
`1/2<=t<=1`; switch differences alone have no absolute anchor.  In deletion
terms it should amortize the variance integral rather than demand a fixed
variance or a fixed endpoint mean at every size.

## 6. Reproduction

From the repository root:

```bash
c++ -O3 -std=c++17 \
  phase2/loop/erdos838/agent_coxeter_half_weight/half_weight_search.cpp \
  -o /tmp/half_weight_search

python3 phase2/loop/erdos838/agent_coxeter_half_weight/verify_half_weight.py \
  --output phase2/loop/erdos838/agent_coxeter_half_weight/certificate.json

python3 phase2/loop/erdos838/agent_coxeter_half_weight/verify_half_weight.py \
  phase2/loop/erdos838/agent_coxeter_half_weight/planar_seed_n20.json \
  phase2/loop/erdos838/agent_coxeter_half_weight/planar_seed_n24.json \
  phase2/loop/erdos838/agent_coxeter_half_weight/planar_seed_n30.json \
  --output phase2/loop/erdos838/agent_coxeter_half_weight/planar_certificate.json
```

The first Python command verifies the unrestricted braid records.  The second
also matches the words against the exact saved planar coordinates.  No
floating-point claim is used in either certificate.

## 7. Bottom line

* `H<=2`: open; no counterexample found.
* `n^(1-o(1))F(1/2)<=F(1)`: also open in this pass.
* `mu_(1/2)>=log_2n-1`: **rigorously false even for planar point sets**.
* Best next version of this route: prove the integrated inequality (6), or a
  deletion-chain amortization of its activity variance, with a constant slack
  allowed at `t=1/2`.
