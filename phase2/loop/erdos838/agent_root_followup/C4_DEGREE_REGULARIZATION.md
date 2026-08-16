# Degree regularization for repair rectangles

**Date:** 2026-08-14

This note closes one analytic substep in the repair-rectangle route.  It does
**not** close Erdős 838: the remaining issue is to reach the near-product
branch without discarding a quadratic amount of component entropy.

All logarithms are base two.  Let `G=(L,R;E)` be a finite simple bipartite
graph, put `m=|E|` and `M=log m`, and sample `(X,Y)` uniformly from `E`.
Write `d_x,d_y` for the two endpoint degrees.  Then

\[
 J:=I(X;Y)=\mathbb E\log {m\over d_Xd_Y}.                 \tag{1}
\]

> **Lemma (mutual information to counted rectangles).**  If `M` tends to
> infinity and `J=o(M)`, then the ordered `C_4` homomorphism count of `G`
> (repeated vertices allowed) is at least
> \[
>                       m^2 2^{-o(M)}.                    \tag{2}
> \]

## Proof

Put

\[
 Z=\log {m\over d_Xd_Y},\qquad
 a=J+\sqrt{(J+1)M}.                                      \tag{3}
\]

Since `1<=d_X,d_Y<=m`, we have `-M<=Z<=M`.  If
`delta=Pr{Z<=a}`, then

\[
 J=\mathbb EZ\ge a(1-\delta)-M\delta,
\]

and hence

\[
 \delta\ge {a-J\over a+M}
 = {\sqrt{(J+1)M}\over J+\sqrt{(J+1)M}+M}=2^{-o(M)}.      \tag{4}
\]

Every good edge in `{Z<=a}` satisfies

\[
                         d_Xd_Y\ge m2^{-a}.              \tag{5}
\]

Partition the good edges by the two dyadic degree bins
`floor(log d_X),floor(log d_Y)`.  There are at most `(M+1)^2` bins, so one
bin spans a subgraph `H` with

\[
 m':=|E(H)|\ge {\delta m\over(M+1)^2}.                    \tag{6}
\]

Let `D_L,D_R` be the lower endpoints of its two degree bins, where degrees
are still measured in `G`.  From (5),

\[
                         D_LD_R\ge m2^{-a-2}.             \tag{7}
\]

Every active left vertex of `H` has degree at least `D_L` in `G`, whose
total degree is `m`; therefore `|L(H)|<=m/D_L`.  Similarly
`|R(H)|<=m/D_R`.  The standard twofold Cauchy--Schwarz inequality for a
bipartite adjacency matrix gives

\[
 \operatorname{hom}(C_4,H)
 \ge {m'^4\over |L(H)|^2|R(H)|^2}.                        \tag{8}
\]

Using (6)--(7), the right side is at least

\[
 m^2\,{\delta^4 2^{-2a-4}\over(M+1)^8}=m^2 2^{-o(M)},   \tag{9}
\]

because `J=o(M)` implies `a=o(M)` and (4) gives
`log(1/delta)=o(M)`.  This proves (2).  QED.

## Application and exact remaining gap

ACP Theorem 23 gives `J=o(r^2)` in its entropy-near-product repair branch;
there `M=Theta(r^2)`.  The lemma therefore converts its weighted `C_4`
statement into at least `|G|^2 2^{-o(r^2)}` actual ordered repair
rectangles.  The global cross-source decoder in
`agent_all_interval_isoperimetry/TWO_RECORD_UNCROSSING.md` maps those
rectangles to two convex faces with fibre `n^2 2^{2r}=2^{O(r)}`.  Thus the
near-product branch has the desired quadratic-coefficient two-face bound.

What remains unproved is the **component-surplus branch**.  A marginal can
have higher entropy per expected rank, but passing to that marginal may
discard a constant fraction of the original joint entropy.  Neither (1)--
(9) nor the existing density-preserving rank slice shows that every hard
record family reaches the near-product branch while preserving the two-face
budget.  Any claimed complete proof must address that loss explicitly.
