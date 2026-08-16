# Mask-cascade entropy dichotomy

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

There is an exact accounting theorem for the nonseparated-mask residue.
It does not bound the length of a geometric deletion cascade; instead it
shows that every failure of the one-face profile bank must erase a
macroscopic amount of coordinate-support entropy.

Let `X_1,...,X_q` be pairwise disjoint supports, let
`E subseteq product_i X_i` be a family of `M` ordinary singleton words,
and put `m_i=|X_i|`.  Fix `g`, and let `J` be a family of `J` nonempty
ordinary local faces contained in `X_g`.  For every pair `(x,F) in E times
J`, choose canonically a retained mask

\[
 S(x,F)\subseteq[q]\setminus\{g\}
\]

for which

\[
                 F\cup\{x_i:i\in S(x,F)\}
\]

is ordinary.  Such a mask always exists because `S=emptyset` leaves the
ordinary face `F`.  Write `D(x,F)=([q]-{g})-S(x,F)` and define its erased
alphabet cost

\[
                         K(D)=\prod_{i\in D}m_i.        \tag{1}
\]

The rule may be the actual geometric cascade, the maximum-retained-cost
mask, or any deterministic choice.

> **Theorem 1 (mask-cascade dichotomy).**  For every `T>=1` and
> `0<theta<=1`, either more than `(1-theta)MJ` pairs have `K(D)>T`, or
>
> \[
>                 V(P)\ge {\theta MJ\over 2^{q-1}m_gT}. \tag{2}
> \]

**Proof.**  If at least `theta MJ` pairs have `K(D)<=T`, one of the at
most `2^{q-1}` deletion masks contains at least
`theta MJ/2^{q-1}` of them.  Fix it.  Its ordinary output recovers `F` by
intersection with `X_g`, every retained coordinate value, and the mask
from the missing coordinate supports.  Only the original value `x_g` and
the values in the deleted supports are forgotten.  The load is at most
`m_gK(D)<=m_gT`, proving (2).  QED.

Suppose `d=log D_0`, `q<=kappa d`, `m_i<=D_0`,

\[
 \log M=(a+o(1))d^2,\qquad \log J=(c+o(1))d^2.         \tag{3}
\]

Take `theta=1/2` and `T=2^{(c-epsilon)d^2}`.  Since
`q+log m_g=O(d)`, the second branch gives

\[
                   \log V(P)\ge(a+epsilon-o(1))d^2.    \tag{4}
\]

Consequently, if no fixed coefficient gain occurs, more than half of all
source/profile pairs satisfy

\[
       \sum_{i\in D(x,F)}\log m_i
                         \ge(c-o(1))d^2.               \tag{5}
\]

At the live values `a=kappa=1/4`, `c=1/8`, a hard cascade therefore erases
at least half of the selected source-support entropy on a positive fraction
of all pairs.  A bounded or submacroscopic cascade is no longer a possible
obstruction.

This theorem is only an accounting reduction.  It does not turn the
erased coordinates into a second compatible face and does not prevent a
projectively universal root-bad profile from forcing a macroscopic mask.
The surviving geometric target is now: charge these macroscopic erased
arcs by a recoverable outer/circuit shield, or prove that several such
profile insertions can share the erased entropy without a square loss.

The exact verifier is

```text
python3 phase2/loop/erdos838/agent_root_followup/verify_mask_cascade_entropy.py
```

It exhausts finite weighted mask systems, checks the decoder inequality,
and audits the live coefficient arithmetic.
