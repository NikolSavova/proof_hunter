# Erdős 838: total-count-capped cut/kernel audit

**Date:** 2026-08-13
**Verdict:** the total-`V` cap really does eliminate the known one-sided
padding mechanism, and I prove a quantitative version of that statement
below.  I did **not** prove the total-count-capped collision theorem, nor an
unrestricted coefficient above `1/4`.  More importantly, the previously
advertised conditional `1/3` calculation used an unproved marginal premise:

\[
 \log C(Q)+\log U(Q)\ge(1/2-o(1))(\log |Q|)^2.       \tag{M_{1/2}}
\]

`(M_(1/2))` is not a standard universal cap--cup product theorem; it was the
target of the earlier lower-bound campaign and remains open for arbitrary
point sets.  Even a proof of polynomial tangent mass and polynomial
total-capped collision would therefore not currently establish `1/3`.

The strongest new candidate isolated by this audit is

\[
 \boxed{\quad
 \rho_{L\mid R}:=\frac{X_{L\mid R}E^2}{S_LS_R}
 \ \ge\ V(P)^{-1/2}n^{-O(1)}.
 \quad}                                                \tag{SC}
\]

It survives all exact tests and the exponent `1/2` would be sharp on the
least-index alternating family.  But `(SC)` is a **conjecture**, not a
theorem: I did not find the needed uncrossing injection.

All logarithms below are base two.

## 1. Exact input: what is proved about cap/cup marginals

Write `C(Q),U(Q)` for the total nonempty cap and cup counts.  The universal
asymmetric cup--cap incidence argument gives the following asymptotic
tradeoff.  If `|Q|=M`, and along a subsequence

\[
 c=\lim\frac{\log C(Q)}{(\log M)^2},\qquad
 u=\lim\frac{\log U(Q)}{(\log M)^2},
\]

then

\[
 \boxed{\mathcal E(c,u)\ge\frac14},                \tag{1}
\]

where

\[
 \mathcal E(a,b)
 =a\log\frac{a+b}{a}+b\log\frac{a+b}{b}.          \tag{2}
\]

This is the theorem proved in
`campaign_lower_attack_direct_20260813.md`.  Since
`E(c,u)<=c+u`, it implies only

\[
 \log C(Q)+\log U(Q)
 \ge(1/4-o(1))(\log M)^2,                          \tag{3}
\]

not `(M_(1/2))`.  The formal balanced profile in that report shows that the
full system of black-box asymmetric cup--cap incidence inequalities cannot
improve the constant in (3).

This distinction matters because Sections 5 of both the cut-reset and
tangent-pruning reports insert `(M_(1/2))` with
`F=(1/2)(\log |Q|)^2`.  The subsequent algebra is correct *conditional on
that premise*, but the premise is not currently an unrestricted theorem.

## 2. New theorem: a global total cap forces two directional marginals

The entropy tradeoff nevertheless becomes genuinely stronger when combined
with a cap on the *total* number of convex subsets.

> **Theorem 1 (total-cap directional floor).**  Let `P_N` be an `N`-point
> sequence and put `L=log N`.  Suppose
> \[
>  \log V(P_N)\le(w+o(1))L^2.                     \tag{4}
> \]
> Let `Q_N subseteq P_N` have
> \[
>  |Q_N|=N^{\alpha+o(1)},\qquad 0<\alpha\le1.    \tag{5}
> \]
> Define `beta_alpha(w)` to be the unique nonnegative solution of
> \[
>  \mathcal E(w,\beta_\alpha(w))=\frac{\alpha^2}{4}. \tag{6}
> \]
> (If `2w<alpha^2/4`, (4) is itself impossible.)  Then
> \[
>  \boxed{
>  \min\{\log C(Q_N),\log U(Q_N)\}
>  \ge(\beta_\alpha(w)-o(1))L^2.}                \tag{7}
> \]

**Proof.**  Every cap and every cup of `Q_N` is a convex subset of `P_N`, so

\[
 \log C(Q_N),\log U(Q_N)\le(w+o(1))L^2.          \tag{8}
\]

Suppose (7) fails by a fixed `epsilon>0`.  Pass to a subsequence on which
the two normalized logarithms converge and on which the same one is the
minimum; call the limits `c,u`.  Applying (1) at scale
`log|Q_N|=(alpha+o(1))L` and using homogeneity of `E` gives

\[
 \mathcal E(c,u)\ge\frac{\alpha^2}{4}.            \tag{9}
\]

But `max(c,u)<=w` and
`min(c,u)<=beta_alpha(w)-epsilon`.  The partial derivatives of (2) are

\[
 \frac{\partial\mathcal E}{\partial a}
 =\log\frac{a+b}{a},\qquad
 \frac{\partial\mathcal E}{\partial b}
 =\log\frac{a+b}{b},                              \tag{10}
\]

so `E` is strictly increasing in each positive coordinate.  Hence

\[
 \mathcal E(c,u)
 \le\mathcal E(w,\beta_\alpha(w)-\epsilon)
 <\frac{\alpha^2}{4},                             \tag{11}
\]

a contradiction.  QED.

At the conjectured extremal cap `w=1/2` and for a macroscopic subset
`alpha=1`, the exact numerical constant is

\[
 \boxed{\beta_1(1/2)=0.05241420833383219\ldots.} \tag{12}
\]

Thus a globally quasipolynomial configuration cannot contain a linear-size
block with only polynomially many caps or only polynomially many cups.  This
is exactly the feature used by the known collision counterexamples: their
inflated all-cup/all-cap blocks have a polynomial count in the exposed
direction and hide their `2^r` internal mass from the chosen cut.  Theorem 1
shows that **every** macroscopic replacement block with the same one-sided
behavior violates a total-`V` cap, not just the literal convex chains used in
the stored construction.

The simpler observation `V(P)>=2^r-1` already kills the literal `r`-point
all-cup/all-cap padding blocks.  The value of Theorem 1 is that it also kills
attempts to replace them by arbitrary low-`V` blocks while retaining only
polynomial exposed cap or cup mass.

## 3. What a one-cut theorem would actually imply

Let `mu=wL^2+o(L^2)`.  Suppose a balanced cut satisfied polynomial tangent
mass `(T)` and polynomial collision.  If one also had a universal marginal
sum

\[
 \log C(I)+\log U(I)\ge(q-o(1))L^2              \tag{13}
\]

in each child, the global cap would give

\[
 \log\min(C(I),U(I))\ge(q-w-o(1))L^2.           \tag{14}
\]

Tangent plus collision would then imply

\[
 w\ge2(q-w),\qquad\hbox{hence}\qquad w\ge\frac{2q}{3}. \tag{15}
\]

This recovers `1/3` only with the **unproved** value `q=1/2`.  The established
black-box value `q=1/4` gives merely `1/6`, below the existing `1/4` lower
bound.  Using the full entropy tradeoff rather than only its sum, the
conditional polynomial cut inequality would give

\[
 w\ge2\beta_1(w).                                 \tag{16}
\]

Its equality point is

\[
 w=0.1814956144696798\ldots,                      \tag{17}
\]

again below `1/4`.  Therefore **even proving the proposed total-capped
collision and tangent lemmas would not, with present universal marginal
information, improve the known coefficient.**  A successful cut campaign
needs at least one of:

1. the missing marginal theorem `(M_(1/2))`;
2. a collision theorem that directly creates more than the product of the
   two minimum marginals; or
3. a multiscale persistence theorem that reuses directional mass across
   many cuts.

And even under `(M_(1/2))`, one balanced cut stops at `1/3`; reaching `1/2`
requires the third alternative.

## 4. The square-root total-count candidate

The exact data point to the interpolation inequality `(SC)`:

\[
 S_LS_R\le n^{O(1)}E^2X\sqrt{V(P)}.              \tag{18}
\]

It is a natural quantitative version of “anti-alignment has to be stored as
actual convex mass elsewhere.”  It is also the strongest power of `V` one
can reasonably hope for on this lane.  For the `n=2m` least-index alternating
family,

\[
 \log V=m+O(\log m),\qquad
 \rho\le2^{-m/2+O(\log m)},                       \tag{19}
\]

because the leftmost parity makes one of the two hull chains direct, while
the other chooses a subset of one parity.  Thus `(18)`, if true, has the
correct exponent.

The checker tested the lossless normalization `rho*sqrt(V)>=1` on:

* every noncollinear fixed-`x`, permutation-height configuration through
  `n=7` (`18,56,272,1000` cases);
* random reflection orders at `n=8,10,12,16`;
* exact alternating configurations through `n=80`; and
* the exact rational padded counterfamily at `n=16,24,32`.

The smallest observed value of `log(rho*sqrt(V))` was
`1.6182752421665534` bits.  These tests include nonstretchable reflection
orders, so the evidence is slightly stronger than a realizability-only
probe.  It is still finite evidence.

Even `(SC)` plus polynomial `(T)` would not close `1/3`.  Under the
hypothetical marginal coefficient `q=1/2`, its one-cut arithmetic is

\[
 w\ge2(1/2-w)-w/2,
 \qquad\hbox{so}\qquad w\ge\frac27.              \tag{20}
\]

With only the proved entropy tradeoff it gives
`(3/2)w>=2 beta_1(w)`, whose equality point is
`0.14499904908539524...`, again below `1/4`.

## 5. Why the missing proof is a genuine geometric problem

Write `a_(e,f)=K_L(e,f)` and `b_(e,f)=K_R(e,f)`.  Then

\[
 X=\sum a_{e,f}b_{e,f},\qquad
 S_L=\sum a_{e,f},\qquad S_R=\sum b_{e,f}.        \tag{21}
\]

For arbitrary nonnegative arrays, (18) is false; all of its content must
come from slope-order geometry.  A tempting proof maps a cup and cap sharing
their left endpoint to their union, perhaps after deleting one of the two
right terminals.  That map already fails on five exact integral points:

```text
y = [780092246, 375868377, 732272728, -441108479, 718948642]
cut after index 2
cup = [0,1,4],  cap = [0,2,3].
```

The union is not convex, and deleting either terminal still leaves a
nonconvex four-set.  The checker verifies all signs and hull tests.  A valid
proof therefore needs a multi-step tangent uncrossing.  Its essential
missing statement is something like:

> two independently chosen left/right partial hull pairs can be uncrossed
> into compatible crossing hull pairs, while all discarded tangent pieces
> are encoded by at most one additional convex subset, with only polynomial
> endpoint ambiguity.

Squaring such an injection is exactly the scale suggested by the
`sqrt(V)` term.  I found no proof that its fibres are polynomial, and the
five-point certificate shows why simply deleting an exposed endpoint is
insufficient.

## 6. Reproduction and final claim boundary

Run

```bash
python3 -m py_compile \
  phase2/loop/erdos838/agent_total_capped_kernel/total_cap_audit.py
python3 \
  phase2/loop/erdos838/agent_total_capped_kernel/total_cap_audit.py
```

The script writes `certificate.json`, recomputes (12), (17), and (20)'s
entropy analogue, exhausts the permutation-height cases, samples reflection
orders, and checks the alternating, padded, and five-point certificates.

**Final claim boundary.**

* Proved: Theorem 1, the quantitative macroscopic directional floor under a
  total-`V` cap.
* Corrected: total-capped collision plus `(T)` gives conditional `1/3` only
  after adding the still-open marginal theorem `(M_(1/2))`.
* Conjectural: the square-root collision inequality `(SC)`.
* Not obtained: a universal coefficient above `1/4`, a proof of `(T)`, a
  proof of total-capped collision, or the full coefficient `1/2`.
