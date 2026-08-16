# Fixed-size pooling below one quarter of the ambient logarithm

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

Let \(N=4^k\), and let \(P\) be any \(N\)-point planar set in general
position. Fix \(\delta>0\). Every collection of literal temporal histories
of ranks

\[
                   1\le r\le(1/2-\delta)k              \tag{1}
\]

can be pooled into the ordinary convex \(k\)-faces of \(P\), with amplified
demand \(N2^{-r}\) per rank-\(r\) history, using output load one and recovery
fibre one, for all sufficiently large \(k\).

Since \(\log N=2k\), this is the literal-rank range

\[
                   r\le(1/4-\delta/2)\log N.            \tag{2}
\]

It strictly improves the direct \(r=o(\sqrt{\log N})\) replacement range in
**GLOBAL_RANK_THREE_ES4_REPLACEMENT_CODE.md**. Together with the identity code
for \(r\ge\log N\), the unresolved literal window is narrowed to

\[
          (1/4-o(1))\log N\le r<\log N.                 \tag{3}
\]

The result is a decoder-range theorem, not the fixed-size supersaturation
claim P1. It says that histories in (1) cannot be the obstruction to P1's
pooled promotion step.

The geometric input is Andrew Suk's theorem

\[
                         ES(k)=2^{k+o(k)}.               \tag{4}
\]

Source: Andrew Suk,
[On the Erdos--Szekeres convex polygon problem](https://arxiv.org/abs/1604.08657).

## 1. The ordinary rank-\(k\) reservoir

Put \(t_k=ES(k)\). Every \(t_k\)-subset of \(P\) contains an ordinary convex
\(k\)-subset. Double counting a convex \(k\)-face together with a containing
\(t_k\)-set gives

\[
 v_k(P)\ge {\binom Nk\over\binom{t_k}k}.                 \tag{5}
\]

Write

\[
                         t_k\le2^{k+g_k},\qquad g_k=o(k). \tag{6}
\]

The elementary estimates

\[
 \binom Nk\ge(N/k)^k,\qquad
 \binom{t_k}k\le(e t_k/k)^k\le(4t_k/k)^k               \tag{7}
\]

give the convenient exact-scale lower bound

\[
 v_k(P)\ge\left({N\over4t_k}\right)^k
          \ge2^{\,k(k-g_k-2)}.                           \tag{8}
\]

Thus the one physical rank-\(k\) bank has \(2^{k^2-o(k^2)}\) outputs in
every configuration.

## 2. Total literal demand

A literal rank-\(r\) history is recovered by its physical support, so there
are at most \(\binom Nr\) of them. Give each history

\[
                         q_r=\left\lceil{N\over2^r}\right\rceil \tag{9}
\]

unit-capacity slots. Since \(r\le k<\log N\),

\[
 q_r\le {2N\over2^r}.                                   \tag{10}
\]

Using \(\binom Nr\le(eN/r)^r\le(4N/r)^r\), the rank-\(r\)
slot demand satisfies

\[
 \begin{aligned}
 T_r
 &\le\binom Nr\,{2N\over2^r}\\
 &\le2^{\,r(2k+1)+2k+1}.                                \tag{11}
 \end{aligned}
\]

If \(R=\lfloor(1/2-\delta)k\rfloor\), pooling all ranks at most \(R\)
costs at most

\[
 \sum_{r\le R}T_r
 \le2^{\,R(2k+1)+2k+1+\lceil\log R\rceil}.              \tag{12}
\]

The exponent gap between (8) and (12) is

\[
 2\delta k^2-k g_k-O(k+\log k),                         \tag{13}
\]

which is positive for all sufficiently large \(k\), because \(g_k=o(k)\).
Therefore the single ordinary bank in (8) has at least the total ceiling
demand in (12).

## 3. Exact block decoder

Canonically order all literal histories first by rank and then by physical
support. Canonically order the convex \(k\)-faces of \(P\). Give each history
the next \(q_r\) unused faces and put flow

\[
                         {N2^{-r}\over q_r}\le1          \tag{14}
\]

on every assigned face. The blocks are disjoint, so the physical output has
load at most one. Its index in the globally known face bank identifies its
unique block, and hence recovers the rank and the literal support. Thus the
recovery fibre is exactly one; no history label is retained geometrically.

The code pools every rank in (1) simultaneously. Independent per-rank codes
would unnecessarily reuse the same bank.

## 4. Scope

The fixed gap \(\delta>0\) is essential for this argument. Suk's
\(2^{k+o(k)}\) error is multiplied by \(k\) in (8), so the present estimates
do not reach the boundary \(r=k/2\). More importantly, the universal
rank-\(k\) reservoir estimate (8) cannot certify absorption of **all**
literal rank-\(r\) histories by total capacity once
\(r>(1/2+o(1))k\): their total amplified demand has leading exponent
\(2kr>k^2\), while (8) guarantees only \(k^2-o(k^2)\) bank bits. Particular
configurations may have a larger rank-\(k\) bank; crossing this boundary
uniformly requires additional geometry or a smaller selected history family.

The theorem also assumes literal histories. Multiple temporal records with
the same physical support contribute their genuine multiplicity and require
an additional incidence or recovery bound.

## 5. Verification

Run

~~~text
python3 phase2/loop/erdos838/verify_fixed_size_literal_pooling.py
~~~

The verifier checks the double-count identity, the binomial estimates, the
exact pooled slot inequality under its displayed sufficient exponent
condition, and explicit block allocations on bounded integer instances.
