# Planar shelling-antimatroid / Tutte attack

**Date:** 2026-08-14  
**Verdict:** no proof of Erdős 838 is claimed.  The antimatroid formulation
does isolate an exact bivariate target, but Gordon's one-variable expected
rank polynomial provably loses information needed at half weight.  More
strongly, both the natural one-root amortized induction and its whole-hull
(onion-layer) repair have exact planar counterexamples.  The counterexample
is a 63-point rational configuration and leaves the original HW2 inequality
with exponential slack.  Thus the next state must retain a tangent
arc/pocket, not merely a Tutte evaluation of a scalar rooted minor.

## 1. Exact Tutte and bivariate formulations

Let `C` run over the closed sets of the affine convex geometry of a
general-position planar point set `P`.  Put

\[
 h(C)=|\operatorname{ext}C|,\qquad i(C)=|C|-h(C),
\]

and define the hull/interior polynomial

\[
 B_P(u,v)=\sum_{C\text{ closed}}u^{h(C)}v^{i(C)}.       \tag{1}
\]

For the dual shelling antimatroid, Gordon's feasible-set expansion is

\[
 f_P(t,z)=\sum_C t^{|C|}(1+z)^{i(C)}
          =B_P(t,t(1+z)).                              \tag{2}
\]

Consequently

\[
 \boxed{Z_P(s)=B_P(s,1)=f_P(s,s^{-1}-1)}.              \tag{3}
\]

In particular, the strong half-weight target is

\[
 \boxed{n f_P(1/2,1)\le2f_P(1,0)}.                    \tag{HW2}
\]

The Boolean intervals `[ext(C),C]` partition `2^P`, giving the exact
bivariate curve

\[
 \boxed{B_P(x,1+x)=(1+x)^n}.                           \tag{4}
\]

Equivalently, the corank-nullity expansion gives

\[
 Z_P(1/2)=2^{-n}\sum_{S\subseteq P}2^{r(S)}
         =\mathbb E_T2^{n-|\operatorname{cl}T|}.        \tag{5}
\]

Equations (1)--(5) are exact.  The difficulty is moving from the universal
curve (4), or expected-rank data, to the off-curve point `(u,v)=(1/2,1)`.

## 2. Gordon's cyclic expected-rank data do not determine half weight

For an interior point `x`, Gordon cyclically orders the minimal feasible
stems `F_1,...,F_k` exposing `x` and proves

\[
 \Pr(x)=p_x\left(\sum_i p_{F_i}-\sum_i p_{P-F_i}\right)+p_P. \tag{6}
\]

The complement terms in (6) are the planar information absent from a generic
antimatroid.  Nevertheless, aggregating them into the one-variable expected
rank polynomial loses information needed by HW2.

There are two exact, rationally realizable eight-point configurations in
`expected_rank_collision_certificate.json` with the same polynomial

\[
 \operatorname{er}(p)=
 4p+3p^2+4p^3+p^4-p^5-4p^6-3p^7+4p^8,              \tag{7}
\]

and the same `V=Z(1)=133`, but with convex profiles

\[
\begin{aligned}
 &(1,8,28,56,33,6,1),\\
 &(1,8,28,56,33,7,0).
\end{aligned}                                         \tag{8}
\]

Their half-weight values differ exactly:

\[
 2^8Z_1(1/2)=5444,\qquad 2^8Z_2(1/2)=5448.          \tag{9}
\]

The verifier independently reconstructs every closed set, checks (7)--(9),
checks the coefficient antisymmetry from Gordon's planar theorem, and checks
(4) coefficientwise.  The full tables `X_(h,i)` in the certificate separate
the pair.  Hence an argument using only `er(p)`--even all of it, not merely a
few derivatives--cannot prove HW2.

## 3. A sharp rooted induction, and why it was attractive

Let `e` be a global hull vertex.  Write

\[
 Z_0(s)=Z_{P-e}(s),\qquad
 R_e(s)=\sum_{\substack{A\text{ convex}\\e\in A}}s^{|A|-1}.
\]

Then

\[
 Z_P(s)=Z_0(s)+sR_e(s).                            \tag{10}
\]

The following rooted amortization condition would have solved HW2 exactly:

\[
 \boxed{2Z_0(1/2)+nR_e(1/2)\le4R_e(1).}           \tag{RA}
\]

Indeed, if HW2 holds on `P-e`, then

\[
\begin{aligned}
 nZ_P(1/2)
 &=nZ_0(1/2)+\frac n2R_e(1/2)\\
 &\le2Z_0(1)+Z_0(1/2)+\frac n2R_e(1/2)\\
 &\le2Z_0(1)+2R_e(1)=2Z_P(1).
\end{aligned}                                      \tag{11}
\]

`RA` survived 2,000 random configurations through `n=14`, exact Pascal,
nested-triangle and Horton families, all 24,698 type-A reflection
commutation classes at `n=7`, and the saved upper-bound adversaries through
`n=30`.  It is also nearly sharp on the saved records (an individual hull
ratio reaches `0.97579` at `n=30`).

Pointwise `RA` was already known not to hold for every hull vertex.  In the
apex/concave-chain family, the apex ratio is `1.78795` at `n=13`, while the
two chain endpoints have ratio `0.16505`.  The two-deep-endpoint wrapper
similarly makes both horizontal endpoints fail.  This initially suggested
an existential hull choice.

## 4. Whole-hull amortization and the exact 63-point obstruction

A still cleaner repair was to delete the entire outer hull.  Let `H` be the
global hull, `h=|H|`, and `I=P-H`.  Define

\[
 \Phi(P)=2Z_P(1)-|P|Z_P(1/2).
\]

The onion monotonicity

\[
 \Phi(P)\ge\Phi(I)                                  \tag{12}
\]

is equivalent to

\[
 \boxed{
 hZ_I(1/2)+n\bigl(Z_P(1/2)-Z_I(1/2)\bigr)
 \le2\bigl(Z_P(1)-Z_I(1)\bigr).}                   \tag{ORA}
\]

Iteration of (12) over onion layers would prove HW2.  `ORA` survived 5,000
random tests, every structured family above, all 24,698 `n=7` reflection
classes, and the saved `n=20,24,30` upper records.

Both `RA` and `ORA` are nevertheless false on the same exact rational point
set.

Take sixty distinct rational points on the unit circle, written as

\[
 q(t)=\left({1-t^2\over1+t^2},{2t\over1+t^2}\right),           \tag{13}
\]

and put them strictly inside the outer triangle

\[
 (-1000,-1000),\quad(1001,-997),\quad(1/7,1002).               \tag{14}
\]

The exact rational parameters are stored in
`verify_outer_triangle_barrier.py`.  The script verifies every determinant,
strict containment, and every partition function by the independent
cap/cup matrix factorization.  All inner subsets are convex, so

\[
 Z_I(1)=2^{60},\qquad Z_I(1/2)=(3/2)^{60}.          \tag{15}
\]

For the full 63-point set, the exact count is

\[
 Z_P(1)=1152921523934399448
       =2^{60}+19327552472.                         \tag{16}
\]

The onion ratio `LHS(ORA)/RHS(ORA)` is

\[
 2.855924130798966\ldots>1.                         \tag{17}
\]

and **each of the three hull vertices** fails `RA`, with ratios

\[
 2.8559420204\ldots,quad
 2.8559420720\ldots,quad
 2.8560262321\ldots.                                \tag{18}
\]

Thus neither an existential hull choice nor a whole-layer scalar
amortization can work.

This is not a counterexample to HW2.  Quite the opposite:

\[
 {63Z_P(1/2)\over2Z_P(1)}
 =1.0046235246\cdot10^{-6}.                         \tag{19}
\]

Geometrically, each outer vertex retains only subsets supported on a tangent
arc of the inner circle (with polynomially many choices on the visible arc).
The rooted shell therefore has the `poly(m)2^(m/2)` tangent-arc scale, while
the abandoned Boolean core has half mass `(3/2)^m`.  Scalar rooted deletion
throws away precisely the compensating faces that make (19) tiny.

## 5. What a viable bivariate/rooted induction must retain

The two exact barriers draw a sharp boundary.

1. The one-variable expected-rank polynomial does not determine half weight.
2. Adding `V=Z(1)` to expected rank still does not determine half weight.
3. A scalar link polynomial at one hull vertex is insufficient.
4. Even summing scalar links over the entire outer hull is insufficient.

Gordon's cyclic stems point to the missing state: a **rooted tangent
interval** (equivalently, two tangent endpoints and the pocket between them).
In the 63-point obstruction, this state retains the half-circle Boolean mass
instead of collapsing it into a polynomial outer-rooted link.  This agrees
with the independent repair theorem: a blocked insertion hides one cyclic
interval, but the population inside the corresponding replacement cone is
an arbitrary smaller instance and must be recursively retained.

The most credible continuation is therefore vector-valued:

* index a rooted minor by its two tangent endpoints / cyclic interval;
* use Gordon's consecutive-stem complement pairing as the exact transition;
* aggregate nonadjacent pockets only after preserving the interval history;
* seek a block-smoothed inequality, since pointwise curvature and scalar
  endpoint localization both have exact counterfamilies.

This is essentially the tagged maximal-pocket reset in Tutte language.  The
new contribution here is proof that the direct scalar deletion-contraction
potentials `RA` and `ORA` cannot implement that reset, even after allowing
the choice of any outer hull vertex or amortizing over the whole outer layer.

## 6. Reproduction

From the repository root:

```bash
python3 phase2/loop/erdos838/agent_planar_tutte/verify_planar_tutte_barriers.py
python3 phase2/loop/erdos838/agent_planar_tutte/verify_outer_triangle_barrier.py
python3 phase2/loop/erdos838/agent_planar_tutte/rooted_amortization_probe.py --random 2000 --max-n 14
python3 phase2/loop/erdos838/agent_planar_tutte/rooted_amortization_word_probe.py --max-n 30
```

The first two commands are deterministic exact certificates.  The latter
two record the finite evidence that made `RA`/`ORA` plausible before the
outer-triangle obstruction was found; they are retained to show sharpness,
not as evidence for a surviving conjecture.

## Source

The cyclic stem formula and planar coefficient antisymmetry used above are
from G. Gordon, *Expected Rank in Antimatroids*, Advances in Applied
Mathematics 32 (2004), 299--318, especially Section 4.
