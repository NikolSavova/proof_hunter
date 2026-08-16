# Exact two-direction exhaustion of the first rich common-guard wrapper

**Date:** 2026-08-15.  All counts are nonempty and all logarithms are base
two.

## Verdict

The smallest common-guard wrapper containing the complete rooted
four-point profile menu does **not** realize a two-level scalar ramp.
Exhausting all `8^3=512` words of rooted four-point order types, and every
generic reset chamber of a pair-direction-generic rational realization,
gives

\[
\boxed{
\begin{aligned}
 \min W&=1561,\\
 \min_{\text{word},\xi\ne\xi_0} C_\xi U_\xi&=134995,\\
 \min_{\text{word},\xi\ne\xi_0}{C_\xi U_\xi\over W}
       &={157113\over2546}>61,\\
 \min_{W=1561,\xi\ne\xi_0}C_\xi U_\xi&=157113>100W.
                                                               \tag{1}
\end{aligned}}
\]

Here `xi_0` is the assembly chamber; its reversal is also excluded.  Thus
the word which minimizes the exact first-cap/last-cup recurrence does not
offer a second low-energy chamber, even after all rooted chirotopes with the
same scalar `(W,C,U)` profile are separated.

This is a finite theorem, not an all-scale invariant.  It rules out the
first nontrivial rational bootstrap and shows that the five scalar rooted
profiles are not enough for a `Pi_2` search: there are eight rooted
chirotopes, and different chirotopes with the same scalar profile can have
different reset spectra.  An asymptotic proof still needs a structural
direction-uniform inequality; an asymptotic counterexample must exhibit a
new profile-menu phenomenon absent from all 512 atoms below.

No endpoint-product lemma for arbitrary atoms is used here.

## 1. The complete rooted four-point menu

Write four points as `p_0<p_1<p_2<p_3` in the assembly coordinate and put

\[
 \sigma=(\chi_{012},\chi_{013},\chi_{023},\chi_{123}).  \tag{2}
\]

Exactly eight sign words are realizable:

\[
\begin{gathered}
 ----,\quad ---+,\quad --++,\quad -+++,\\
 +---,\quad ++--,\quad +++-,\quad ++++ .               \tag{3}
\end{gathered}
\]

Here is a direct completeness check.  Let `a,b,c` be the three adjacent
edge slopes.  The first and fourth signs in (2) are the signs of `b-a` and
`c-b`.  If they agree, `a,b,c` are monotone and all four signs agree.  If
`a<b>c`, the two middle signs can change only in the order

\[
                      +---,\quad ++--,\quad +++-,        \tag{4}
\]

because `chi_013<0` puts a positive weighted average of `b,c` below `a`,
while `chi_023>0` puts `c` above a positive weighted average of `a,b`; these
two inequalities cannot hold simultaneously.  The valley case is the
reflection and gives the three negative-first words.  This proves (3).

The resulting actual pocket profiles form the familiar five-element menu

\[
 (W,C,U)=(15,10,15),(14,11,13),(15,12,12),
          (14,13,11),(15,15,10),                         \tag{5}
\]

but the two `3+1`, two `1+3`, and two balanced sign words remain distinct
rooted order types.  A `Pi_2` audit must keep that distinction.

## 2. Exact wrapper and chamber exhaustion

Normalize the common guard to `u=(-1,0),v=(1,0)`.  For the three roles use
macro parameters

\[
                         t=4,1,{1\over4}.                \tag{6}
\]

For a rational representative `(f,g)` of one of the eight words (3), put

\[
\begin{aligned}
 L&=t^{-1}+10^{-3}f+10^{-6}g,\\
 R&=t      +10^{-3}f-10^{-6}g,\\
 (x,y)&=\left({L-R\over L+R},-{2\over L+R}\right).      \tag{7}
\end{aligned}
\]

These are the exact common-pocket coordinates from
`COMMON_GUARD_PROFILE_RAMP_BARRIER.md`.  Cross-child and guard signs are
independent of the choice among (3), so the 512 words exhaust every rooted
four-point substitution into this macro wrapper.

The ordinary-face count is evaluated by the exact five-block recurrence

\[
 W=\sum_iW_i+
   \sum_{i<j}C_iU_j\prod_{i<h<j}(1+n_h),                 \tag{8}

\]

including the singleton guard blocks.  Thus (8), rather than a subset
sampling estimate, gives `min W=1561`.

For the reset audit, apply the rational perturbation

\[
             (x_i,y_i)\longmapsto
       (x_i+10^{-30}2^i,\ y_i+10^{-30}3^i).              \tag{9}

The verifier checks every triple sign before and after (9), so the full
order type and (8) are unchanged.  It also checks that all 91 pair slopes
are distinct.  Consequently there are exactly 182 oriented generic
projection orders.  Every one is enumerated by the critical values of
`x+s y`.  In each order, cap and cup totals are computed by the independent
last-two-points recurrence

\[
 C(i,j)=1+\sum_{h<i:\chi(h,i,j)<0}C(h,i),\qquad
 U(i,j)=1+\sum_{h<i:\chi(h,i,j)>0}U(h,i).                \tag{10}

\]

Summing (10), adding the 14 singletons, and minimizing over the 180 genuine
reset orders proves every assertion in (1).

The perturbation is important.  The aesthetically symmetric coordinates
have coincident pair directions and only 174--176 displayed chambers.
Equation (9) proves that (1) is not an artifact of those missing chambers.

## 3. What the finite theorem says about `Pi_2`

For a child `Q`, the one-direction state

\[
                       (W(Q),C_{\xi_0}(Q),U_{\xi_0}(Q))  \tag{11}

\]

is sufficient to evaluate (8), but it cannot predict a reset.  The exact
state is the paired spectrum

\[
 \Pi_2(Q)=\{(C_\xi,U_\xi;C_\eta,U_\eta):\xi\ne\eta\}.  \tag{12}

The eight patterns in (3) already demonstrate the loss in collapsing (12)
to the five rows (5).  Nevertheless, retaining the complete rooted state
still produces the strong finite separation (1).  In particular:

* the scalar minimizers with `W=1561` do not minimize reset energy;
* the global reset minimum `134995` is attained by a nonminimal assembly
  word; and
* optimizing the ratio rather than either numerator gives a third regime,
  but its exact value remains above 61.

This suggests a useful positive target.  If an `A`-point, `q`-role wrapper
obeys, uniformly in the reset direction,

\[
 \log(C_\xi U_\xi)
   \ge \log W_{\rm assembly}+\gamma q\log A-o(q\log A)  \tag{13}
\]

for some fixed `gamma>0`, then a low-energy scalar ramp cannot bootstrap.
The finite theorem verifies a strong version of (13) at `A=4,q=3`, but does
not supply a scale-independent `gamma`.

## 4. Fixed-gap coefficient accounting

The two-direction issue also has a precise fixed-gap threshold.  Let

\[
                         L=\log n,\qquad
                  m={n\over L^K}.                        \tag{14}
\]

At the coefficient-half target, the loss between the desired parent bank
and an inductive pocket bank is

\[
\begin{aligned}
 \Delta
 &= {1\over2}\left[L^2-(L-K\log L)^2\right]\\
 &=K L\log L-{K^2\over2}(\log L)^2.                     \tag{15}
\end{aligned}
\]

Thus ambient inheritance of the pocket is not a finite-induction closure.
It needs a recoverable multiplier

\[
 R\ge2^\Delta
   ={n^{K\log L}\over2^{(K^2/2)(\log L)^2}}.            \tag{16}
\]

More generally, at coefficient `c` replace the leading `K` in (15) by
`2cK`.

Suppose the cover/source structure supplies `q` independent alphabets of
size `n^{beta+o(1)}` with subquadratic decoder loss.  Then

\[
                         \log R=(\beta q+o(q))L,          \tag{17}

\]

so (16) closes exactly when

\[
                         \beta q\ge K\log L+o(\log L).   \tag{18}

\]

This explains why `Theta(log log n)` genuinely `n`-scale source roles are
the right threshold.  In contrast, `Theta(log log n)` alphabets of only
polylogarithmic size yield `2^{O((log log n)^2)}`, far below (16).  The live
role of `Pi_2` in the fixed-gap branch is therefore to determine whether the
inductive pocket bank can be multiplied by the source bank with the
`n^{Theta(log log n)}` recovery in (16), not merely whether it survives as
an ambient subset.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_two_direction_four_point_wrapper.py
```

Expected output:

```text
PASS: rooted types=8, words=512, chambers/word=182, min W=1561, min reset CU=134995, min reset CU/W=157113/2546, min reset CU among W-minimizers=157113
```

The certificate uses only exact `Fraction` arithmetic.  It checks all eight
seed sign words, the five actual local profiles, preservation of all triple
signs under (9), distinctness of all pair slopes, the exact recurrence (8),
and all `512*182` projection profiles.
