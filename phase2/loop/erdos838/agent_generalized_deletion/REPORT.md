# Activity-compensated generalized deletion

**Date:** 2026-08-14  
**Verdict:** ACP with constant one survives every planar and compositional
test in this lane, but is not proved.  No unrestricted solution of Erdős 838
is claimed.  The main progress is an exact local-record derivative identity
which turns ACP into a concrete charging theorem for the total mass of a
deletion peak.  A natural stronger logarithmic surrogate is killed by the
exact 58-point configuration.

Write

\[
 Z(t)=\sum_{A\text{ convex}}t^{|A|},\qquad
 H={nZ(1/2)\over Z(1)},\qquad
 \mu_t={tZ'(t)\over Z(t)},\qquad
 \Delta=\mu_1-\mu_{1/2}.
\]

The surviving proposal is

\[
 \boxed{H(P)[1-\Delta(P)]_+\leq1.}\tag{ACP}
\]

More generally, a uniform right side `C_n=n^o(1)` is enough for the full
coefficient-one-half theorem.

## 1. Why this target is enough

The exact `Z(1)`-weighted deletion identity is

\[
 \mathbb E_e H(P-e)
 ={n-1\over n}{n-\mu_{1/2}\over n-\mu_1}H(P).       \tag{1}
\]

Since every downset has `mu_1<=n/2`, (ACP) implies

\[
 H(P)\leq\max_eH(P-e)+{2\over n}.                    \tag{2}
\]

Iteration gives `H(P)=O(log n)`.  If the right side of (ACP) is instead
`C_n=n^o(1)`, the same argument gives
`H(P)<=sum_(m<=n)2C_m/m=n^o(1)`, still closing Erdős 838.

## 2. Three exact reformulations

### Exponential size bias

Let `K=|A|` under the half-weight law

\[
 \Pr_h(A)={2^{-|A|}\over Z(1/2)}.
\]

Then the uniform face law is exactly the `2^K`-size bias of this law.  Hence

\[
 H={n\over\mathbb E_h2^K},\qquad
 \Delta={\mathbb E_h[K2^K]\over\mathbb E_h2^K}-\mathbb E_hK. \tag{3}
\]

When `Delta<1`, (ACP) is therefore the single moment inequality

\[
 \boxed{
 n\{\mathbb E2^K(1+\mathbb EK)-\mathbb E[K2^K]\}
 \leq(\mathbb E2^K)^2.}                                \tag{4}
\]

This formulation is useful for distributional/variance attacks.  It also
makes the generic barrier transparent: a complete-three-skeleton truncation
has `K` concentrated near three and violates (4) by a polynomial factor.
Planar circuit overlap, not a generic downset inequality, must enter.

### A derivative at the activity-doubling endpoint

Define

\[
 F_P(t)=t{Z_P(t/2)\over Z_P(t)}.                         \tag{5}
\]

Direct differentiation gives

\[
 {d\log F_P\over d\log t}=1+\mu_{t/2}-\mu_t.
\]

Consequently

\[
 \boxed{H(P)[1-\Delta(P)]_+=n[F'_P(1)]_+.}             \tag{6}
\]

Thus ACP is a boundary-slope theorem for one scalar ratio, not a pointwise
lower bound on the activity gap.  Central Pascal cells have `Delta->0`, but
their endpoint value `nF(1)=H` simultaneously tends to zero.

### Conditional Bernoulli law

Let `B_p` be a Bernoulli-`p` subset of `P` and let `C` be the decreasing
event that `B_p` is in convex position.  The face law at activity `t` is the
law of `B_p` conditional on `C`, where `p=t/(1+t)`.  Therefore

\[
 \Delta
 =\mathbb E(|B_{1/2}|\mid C)-\mathbb E(|B_{1/3}|\mid C), \tag{7}
\]

and

\[
 H=n(3/4)^n{\Pr(B_{1/3}\in C)\over\Pr(B_{1/2}\in C)}.   \tag{8}
\]

ACP is accordingly a sharp-threshold statement for the rooted-circuit
independence event.  Generic 4-uniform sharp-threshold machinery cannot be
enough, because the abstract complete-three-skeleton barrier has the same
monotonicity and witness size.

## 3. New local-record peak identity

For a Bernoulli-`t` restriction `R subseteq P`, weight the restriction by its
number `Z_R(1)` of convex faces.  Its weighted mean `H` is exactly

\[
 \mathcal A_P(t)=
 {ntZ_P(t/2)+(1-t)(t/2)Z'_P(t/2)\over Z_P(t)}.           \tag{9}
\]

Indeed `E Z_R(1)=Z_P(t)`, while a fixed face `A` contributes
`t^|A| E(|R|\mid A subseteq R)=t^|A|\{|A|+(n-|A|)t\}`
to the numerator.  At `t=1`,

\[
 \mathcal A_P(1)=H(P),\qquad
 \mathcal A'_P(1)=H(P)\left(1-\Delta-{\mu_{1/2}\over n}\right). \tag{10}
\]

Expanding the Bernoulli restriction at `t=1` gives a second exact expression:

\[
 \boxed{
 \mathcal A'_P(1)
 ={1\over Z_P(1)}\sum_{e\in P}Z_{P-e}(1)
       \{H(P)-H(P-e)\}.}                                \tag{11}
\]

Finally, since

\[
 {H\mu_{1/2}\over n}={{1\over2}Z'(1/2)\over Z(1)},
\]

(6), (10), and (11) yield the exact **peak-budget identity**

\[
 \boxed{
 H(1-\Delta)
 ={\frac12Z'(1/2)\over Z(1)}
 +{1\over Z(1)}\sum_e Z_{P-e}(1)\{H(P)-H(P-e)\}.}       \tag{12}
\]

This is the cleanest target found in this lane.  At a one-deletion local
maximum every term in the sum is nonnegative, and ACP is precisely

\[
 \sum_e Z_{P-e}(1)\{H(P)-H(P-e)\}
 \leq Z(1)-\frac12Z'(1/2).                              \tag{PB}
\]

The right side is an unusually generous face budget:

\[
 Z(1)-\frac12Z'(1/2)
 =\sum_k(1-k2^{-k})v_k\geq\frac12Z(1),                 \tag{13}
\]

because `k2^-k<=1/2` for every positive integer `k`.  Thus the remaining
problem is no longer to forbid local peaks.  It is to charge their total
`Z(P-e)`-weighted height to at most one copy of the rank-weighted face slack
in (13).  The planar first-switch theorem is naturally matched to (PB):
nonmaximal deletion loss can be routed through repair incidences, while a
maximal loss must recurse inside its retained two-tangent pocket.

For a global record of `H` over all restrictions, (9) also gives
`A_P(t)<=H(P)` for every `0<=t<=1`; (PB) asks for a quantitative upper bound
on the final left derivative, not merely its nonnegativity.

## 4. Exact kills and stress tests

### The logarithmic surrogate is false

Since `1-x<=exp(-x)`, the attractive stronger inequality

\[
 \log{Z(1)\over Z(1/2)}+\Delta\geq\log n              \tag{14}
\]

would imply ACP.  It is false on the exact 58-point configuration:

\[
 H={33994061\over16990512},\qquad
 \Delta={4376001835655\over6638810360336},
\]

and

\[
 H e^{-\Delta}=1.0349739\ldots>1.                     \tag{15}
\]

So a proof must use the actual factor `1-Delta`, not replace it by an
exponential or a symmetrized-KL bound.

### The 58-point obstruction passes ACP

On the same exact configuration,

\[
 H(1-\Delta)
 ={21873815738583\over32075277558016}
 =0.6819525006\ldots.                                  \tag{16}
\]

All 58 children lie below the parent.  The verifier independently rebuilds
all child profiles and checks (11)--(12), so this test includes the actual
local peak rather than only the parent rank polynomial.

### Stretchable coordinate search

A fixed-`x` rational coordinate anneal found the exact 24-point order type in
`planar_acp_record.json`.  Its exact matrix profile has

\[
 H(1-\Delta)=0.8839445277\ldots<1.                     \tag{17}
\]

This improves the earlier stretchable records in this lane, but remains
comfortably below one.  Type-A braid annealing, which searches the larger
class of possibly nonstretchable allowable sequences, reached only about
`0.817` from the older seed in the recorded runs.

### Composition amplification did not occur

The exact 58-point template was iterated by the homogeneous directional
composition recurrence, carrying values and logarithmic derivatives at both
activities.  Depth one is (16); at every depth from two through eight the
activity gap is already larger than one, so ACP's positive part is zero.

The balanced central Pascal templates `S_h`, for every `3<=h<=30` and every
homogeneous depth through 20, were evaluated with log-dual recurrences.  The
largest ACP value was exactly the two-point base value `3/4`; large central
cells have `Delta->0` but `H->0`.  Hence neither the sharp known upper
constructions nor homogeneous amplification of the finite `H>2` obstruction
threatens ACP.

These are stress tests, not a compactness proof: a heterogeneous tangent
recursion could behave differently.

## 5. Low-addable-face target: no scalable obstruction found

The parallel charging lane proposed the sufficient estimate

\[
 N(P)=\sum_{r<L}(L-r)\#\{A:|A|=r,\ u(A)\leq4(r+1)\}
 \leq O(\log\log n)Z_P(1),\qquad L=\lceil\log_2n\rceil. \tag{18}
\]

I audited (18) exactly using rooted circuits.  For every triple `T`, store
the bit mask of roots `p` for which `T+p` is nonconvex.  OR-ing these masks
over the triples of a candidate face both tests convexity and returns every
blocked addition, so the reported `u(A)` values require no floating geometry.

| exact planar family | `n` | `N/Z(1)` |
|---|---:|---:|
| best ACP coordinate record | 24 | 0.618922 |
| APA counterexample | 44 | 0.145370 |
| finite `H>2` counterexample | 58 | 0.030806 |
| central Pascal `m=4,5,6,7` | 6, 10, 20, 35 | 0.529412, 0.558511, 0.423028, 0.206466 |
| vertical `T_(4,2)[T_(4,2)]` | 36 | 0.146620 |
| guarded templates `k=3,4,5` | 7, 11, 25 | 0.346535, 0.347222, 0.186287 |
| guarded `k=3` vertical square | 49 | **0.00106630** |

The last line is a generic rational realization with block-dependent positive
scales; all triples are noncollinear.  It directly tests the indecomposable
guarded family that defeats near-spanning structural regularization.  The
ratio collapses by more than two orders of magnitude under one vertical
iteration.  Thus neither the sharp central constructions nor the guarded
indecomposable construction suggests growth of `N/Z(1)`; both point toward a
constant bound, substantially stronger than the required `O(log log n)`.
This is finite evidence, not a proof of (18).

## 6. What a successful proof now needs

The most concrete route is (PB), not the killed logarithmic surrogate.

1. Expand each positive child loss in (11) into rooted face incidences.
2. Use the first-switch theorem to charge the nonmaximal part with bounded
   multiplicity to the slack weights `1-k2^-k` in (13).
3. For a maximal face, retain the two tangent endpoints and recurse into its
   concentrated three-pocket cone.  The homogeneous stress tests indicate
   that repeated recursion either accumulates activity gap past one or
   drives `H` down; the missing statement is a rigorous heterogeneous
   version of that dichotomy.

An `n^o(1)` multiplicity in this charge is sufficient.  The already banked
coefficient-one-quarter theorem gives only the baseline
`H<=n^(3/4+o(1))`: split the half-weight sum at
`k=(1/4-o(1))log_2 n`.  Thus existing total-count lower bounds alone cannot
produce the needed generalized envelope; local planar overlap is essential.

## 7. Reproduction

Run

```bash
python3 phase2/loop/erdos838/agent_generalized_deletion/verify_acp.py
python3 phase2/loop/erdos838/agent_generalized_deletion/low_addable_audit.py
```

The audit interprets every saved decimal coordinate as an exact rational,
checks general position, reconstructs the full profile, verifies (3)--(6)
and (11)--(12), replays every deletion of the 58-point certificate, and runs
the deterministic composition stress.  `search_acp.py` searches arbitrary
type-A reflection orders; `search_acp_coordinates.py` stays inside exact
stretchable fixed-`x` order types.  The low-addable audit writes
`low_addable_certificate.json` and independently checks its rank counts
against the reflection-matrix profile.
