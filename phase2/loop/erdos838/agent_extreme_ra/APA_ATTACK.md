# Arbitrary-point amortization after the hull-rooted kill

**Date:** 2026-08-14  
**Status:** killed exactly.  The identities remain useful as a postmortem.

The skinny-wrapper counterexample kills every induction which insists on a
global hull point.  The algebraic induction, however, does not require the
deleted point to be extreme.  This leaves one clean replacement target.

## 1. Arbitrary-point RA and induction

For any point `e` (not necessarily a hull point), write

\[
 Z_P(s)=Z_{P-e}(s)+sR_e(s).
\]

If `|P|=n`, `H(P-e)<=2`, and

\[
 2Z_{P-e}(1/2)+nR_e(1/2)\leq4R_e(1),                       \tag{RA-e}
\]

then `H(P)<=2`.  Indeed, the inductive hypothesis gives
`(n-1)Z_{P-e}(1/2)<=2Z_{P-e}(1)`, and adding (RA-e) divided by
two gives the desired `nZ_P(1/2)<=2Z_P(1)`.

Put

\[
 W=Z_P(1/2),\qquad
 W_e=\sum_{A\ni e}2^{-|A|},\qquad
 V_e=|\{A:e\in A,\ A\text{ convex}\}|.
\]

Since `R_e(1/2)=2W_e` and `Z_{P-e}(1/2)=W-W_e`, (RA-e) is

\[
 W+(n-1)W_e\leq2V_e.                                      \tag{1}
\]

Summing (1) over every point gives the sufficient all-point average

\[
 \boxed{
 nZ_P(1/2)+(n-1)\frac12Z'_P(1/2)\leq2Z'_P(1).}             \tag{APA}
\]

Thus APA for every planar configuration would prove HW2 by arbitrary-point
deletion induction.  Section 3 records the exact planar counterexamples.

## 2. Exact equivalent forms

Let `v_k` be the number of convex `k`-sets.  APA is the rank inequality

\[
 \sum_{k=0}^n
 \left(2k-\frac{n+(n-1)k}{2^k}\right)v_k\geq0.             \tag{2}
\]

Let `u(A)` denote the up-degree of a face.  Double-counting covers gives

\[
 \sum_Au(A)=Z'_P(1),\qquad
 \sum_Au(A)2^{-|A|}=2\cdot\frac12Z'_P(1/2).
\]

Therefore the toggle form is

\[
 2\sum_Au(A)\geq
 n\sum_A2^{-|A|}+\frac{n-1}{2}\sum_Au(A)2^{-|A|}.           \tag{3}
\]

Finally put

\[
 E_k=(k+1)v_{k+1},\qquad
 B_k=(n-k)v_k-E_k,
\]

so `B_k` is the number of blocked rank-`k` addition incidences.  The
integrated boundary form is

\[
 \sum_{k=0}^{n-1}
 \left(2-\frac{n-1}{2^{k+1}}\right)E_k
 \geq n\sum_{k=0}^n2^{-k}v_k,                              \tag{4}
\]

or, equivalently, replace `E_k` by `(n-k)v_k-B_k`.  The coefficient in
(4) changes sign at `k=log_2(n-1)-1`.  Blocked incidences below that scale
help, whereas blocked/maximal mass above that scale hurts.  Thus APA lands
on the same maximal-pocket reset gate as the graded-ratio attack, but in a
single integrated inequality rather than rank by rank.

In mean notation, with

\[
 \mu_t=tZ'_P(t)/Z_P(t),\qquad H=nZ_P(1/2)/Z_P(1),
\]

APA is

\[
 H\left(1+(1-1/n)\mu_{1/2}\right)\leq2\mu_1.               \tag{5}
\]

## 3. Exact planar kills

The search eventually crossed both proposed boundaries.

1. `agent_apa_rank/verify_apa_counterexample.py` gives an exact 44-point
   planar configuration with

   \[
   \frac{\text{APA LHS}}{\text{APA RHS}}
   =\frac{1179202571}{1178290176}>1.
   \]

   Its profile is
   `(1,44,946,13244,70450,99093,43597,8726,1075,53)`.  Although
   APA fails, 21 of its 44 points still satisfy the individual RA-e
   inequality.  So this first certificate kills averaging but not existence.

2. `agent_apa_rank/verify_half_weight_counterexample.py` gives an exact
   58-point planar configuration with

   \[
   H(P)=\frac{33994061}{16990512}>2.
   \]

   Every one of its 58 deletion children has `H<2`, and every individual
   RA-e margin is negative.  Its unique deepest onion point also fails.
   Therefore all of the following are false: finite `H<=2`, APA, existence
   of an arbitrary RA-e point, and the proposed innermost-onion repair.

This does **not** refute Erdős 838.  The asymptotic proof only needs
`H(P)=n^{o(1)}`, not the false sharp constant `2`.  What survives is an
approximate/amortized deletion target controlling the cumulative size of
local peaks of `H`, rather than forbidding every peak.

### A surviving activity-compensated peak target

The exact weighted-deletion identity gives

\[
 \mathbb E_{e\propto Z_{P-e}(1)}H(P-e)
 =\frac{n-1}{n}\frac{n-\mu_{1/2}}{n-\mu_1}H(P).             \tag{6}
\]

Put `Delta=mu_1-mu_(1/2)`.  Every downset has `mu_1<=n/2`, since deletion
injects the faces containing a fixed point into those omitting it.  It
follows from (6) that the much weaker scalar estimate

\[
 \boxed{H(P)[1-\Delta]_+\leq C}                             \tag{ACP}
\]

would imply

\[
 H(P)\leq\max_eH(P-e)+\frac{2C}{n}.                         \tag{7}
\]

Iterating (7) gives `H(P)=O(log n)=n^{o(1)}`, which is already enough for
the desired coefficient `1/2`.  This target exactly compensates the two
killed extremes: central Pascal towers can have `Delta->0` but then `H`
decays, whereas the hard 44- and 58-point records have `H` near two but
`Delta=0.606...` and `0.659...`, respectively.

The actual local-peak quantities
`n(H(P)-max_e H(P-e))` are about `0.1332` and `0.0718` on the 44- and
58-point certificates.  Thus an `O(1/n)` peak theorem survives the exact
kills with substantial slack.  Proving (ACP), or proving (7) directly by a
geometric deletion choice, is the clean replacement for exact RA.

All saved planar records are consistent with the concrete constant `C=1`.
The largest checked value of `H[1-Delta]_+` is about `0.7964` on the saved
24-point record; the 44- and 58-point exact kills give about `0.7424` and
`0.6820`.  Without the positive-part notation, the `C=1` proposal is
equivalent under the uniform face law for `K=|A|` to

\[
 n\,\mathbb E\bigl[(K+1-\mu_1)2^{-K}\bigr]\leq1.           \tag{8}
\]

Equation (8) is a particularly compact next target for rank-three charging.

## 4. Earlier evidence and generic barriers

Exact tests so far:

* every reflection-order commutation class through `n=7` (24,698 classes
  at `n=7`) passes; the worst ratio LHS/RHS is `0.734375`;
* 5,000 random rational/integer planar configurations through `n=14` pass;
* the exact 63-point outer-circle triangular wrapper passes with ratio
  about `6.93e-7`, although every outer hull point fails RA-e;
* the strongest saved 30-point planar record passes with ratio about
  `0.921`;
* direct reflection-order annealing raised the ratio above `0.95`; the later
  coordinate search produced the exact stretchable 44- and 58-point kills.

APA is not a generic downset or antimatroid inequality.  The abstract
3-truncation `v_k=binom(n,k)` for `k<=3`, zero thereafter, violates (2) by
order `n^4`.  Even the hypothetical rank-extension bounds
`a_{k+1}/a_k>=2^{-k}` for normalized densities `a_k=v_k/binom(n,k)` do not
by themselves imply exact APA: taking equality after rank three already
violates APA for moderate `n`.  Rank-three geometry and a nonlocal
maximal-face compensation are therefore load-bearing.

## 5. Computational search

`search_all_point_ra.py` evaluates APA with dual-number matrix products at
activities `1/2` and `1`, so it avoids expanding the full rank polynomial.
It performs Coxeter commutations and braid flips and writes the best word to
a JSON certificate.  A violation in this broad reflection-order class must
still be checked for stretchability before it is a planar counterexample.
