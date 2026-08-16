# Endpoint localization ladder: the marker rungs are false

**Date:** 2026-08-14  
**Verdict:** the proposed `m^(5/3)` either-marker inequality and the proposed
`m^(3/2)` one-marker inequality are false by a polynomial factor.  In fact,
no positive power of the horizontal span can be put in front of the endpoint
half-mass if the compensating mass is required to retain one or both root
markers.  A simple integral family proves this.  The span-squared inequality
against the **full interval mass** survives the family with exponential
slack, but I did not prove it.  Even if true, its naive global aggregation is
only harmonic and does not improve the present `1/4` lower coefficient.

All logarithms below are base two.  A monotone path with `e` edges has
weight `z^e`; hence an upper/lower path pair has weight `z` to the number of
vertices in its convex union.

## 1. A general two-deep-endpoint wrapper

Let `Q={q_1,...,q_M}` be any point set in increasing horizontal order.  Add
points `l,r` strictly to its left and right, at the same sufficiently large
negative height.  More explicitly, after an affine normalization one may
take

\[
 l=(-1,-B),\qquad r=(M+1,-B),
\]

where `B` is large enough.  Then, for all `a<b`,

\[
 \chi(l,q_a,q_b)=\chi(q_a,q_b,r)=\chi(l,q_a,r)=-.       \tag{1}
\]

Write

\[
 C_Q(z)=\sum_{\substack{S\subseteq Q\\S\ne\varnothing\\
                         S\text{ is a cap}}}z^{|S|}.     \tag{2}
\]

The signs (1) give exact identities

\[
 \boxed{
 F_{lr}(z)=z^2(1+C_Q(z)),\quad
 L_{lr}(1)=R_{lr}(1)=2(1+C_Q(1)),\quad
 E_{lr}(1)=3(1+C_Q(1)).}                                \tag{3}
\]

Indeed, in a convex face containing `l`, the lower (cup) path is direct: a
cup using two points of `Q` would begin with a negative turn.  The upper path
is exactly a cap subset of `Q`.  The same statement holds at `r`, and with
both endpoints present.  Conversely every cap subset, together with any
nonempty choice of the two deep endpoints, is convex.  This proves (3)
without an asymptotic or a generic-position perturbation.

The full interval mass is correspondingly

\[
 Z_{Q\cup\{l,r\}}(1)=Z_Q(1)+3(1+C_Q(1)).                 \tag{4}
\]

Thus the surviving full-interval span-squared conjecture, even on this
special wrapper, contains the nontrivial directional assertion

\[
 M^2(1+C_Q(1/2))\ \lesssim\ Z_Q(1)+C_Q(1).               \tag{5}
\]

This is a useful reformulation of what remains: abandoning both endpoint
markers is not cosmetic, but supplies all of the missing capacity.

## 2. Exact integral counterfamily

Now specialize to

\[
 q_a=(a,a^2),\quad 1\le a\le M,\qquad
 l=(-1,-B),\quad r=(M+1,-B),\qquad B=(M+2)^3.             \tag{6}
\]

The determinant signs are exact:

\[
\begin{aligned}
 \chi(q_a,q_b,q_c)&=(b-a)(c-b)(c-a)>0,\\
 \chi(l,q_a,q_b)&=(b-a)(ab+a+b-B)<0,\\
 \chi(q_a,q_b,r)&=(b-a)\{-B-a^2-(a+b)(M+1-a)\}<0,\\
 \chi(l,q_a,r)&=-(M+2)(a^2+B)<0.
\end{aligned}                                             \tag{7}
\]

In particular the points are in general position.  The middle parabola is a
strict cup, so its only cap subsets have size zero, one, or two.  Put

\[
 A_M=1+M+\binom M2=\frac{M^2+M+2}{2}.                    \tag{8}
\]

Equations (3) become

\[
\begin{aligned}
 F_{lr}(z)&=z^2+Mz^3+\binom M2z^4,\\
 L_{lr}=R_{lr}&=2A_M,\\
 E_{lr}&=3A_M,\\
 Z_{[l,r]}(1)&=2^M+3A_M.                                 \tag{9}
\end{aligned}

At half activity,

\[
 F_{lr}(1/2)=\frac{M^2+3M+8}{32}.                        \tag{10}
\]

Consequently

\[
 \boxed{
 \frac{F_{lr}(1/2)}{\max(L_{lr},R_{lr})}\longrightarrow\frac1{32},
 \qquad
 \frac{F_{lr}(1/2)}{E_{lr}}\longrightarrow\frac1{48}.}  \tag{11}
\]

For every fixed `alpha>0`, therefore,

\[
 \frac{(M+2)^\alpha F_{lr}(1/2)}{\max(L_{lr},R_{lr})}
 \longrightarrow\infty,
 \qquad
 \frac{(M+2)^\alpha F_{lr}(1/2)}{E_{lr}}
 \longrightarrow\infty.                                \tag{12}
\]

This refutes not only exponents `3/2` and `5/3`, but **every positive marker
exponent**.  Notice that the full interval behaves in the opposite way:

\[
 \frac{(M+2)^2F_{lr}(1/2)}{Z_{[l,r]}(1)}\longrightarrow0. \tag{13}
\]

The compensating faces are precisely the `2^M` subsets which abandon both
deep endpoints.  Any localization flow which insists on retaining a root
marker is therefore structurally incapable of seeing the compensation.

For completeness, the full convex profile is

\[
 v_k=\binom Mk
   +2\mathbf1_{0\le k-1\le2}\binom M{k-1}
   +\mathbf1_{0\le k-2\le2}\binom M{k-2}.                \tag{14}
\]

This independently gives (9).

## 3. A rigorous short-span escape

There is still a useful global reduction which needs no localization
conjecture.  Horizontally order an arbitrary `n`-point set.  Let
`Z_{<=D}(1/2)` be the half-weight of the empty face, all singletons, and all
convex faces whose exact endpoint span is at most `D`.

For an endpoint interval of length `m`, its endpoint link is a subfamily of
all subsets of the `m-2` internal points.  Coefficientwise,

\[
 F_{ij}(z)\le z^2(1+z)^{m-2}.                            \tag{15}
\]

There are `n-m+1` intervals of length `m`.  Summing the geometric series at
`z=1/2` gives the exact universal bound

\[
\begin{aligned}
 Z_{\le D}(1/2)
 &\le1+\frac n2+\frac n4\sum_{m=2}^{D}(3/2)^{m-2}\\
 &=\boxed{1+\frac n2(3/2)^{D-1}}.                        \tag{16}
\end{aligned}

Use the established lower bound

\[
 f(n)\ge2^{(1/4-o(1))(\log n)^2}.                        \tag{17}
\]

Put `lambda=log(3/2)` and, for fixed `epsilon>0`,

\[
 D=\left\lfloor
 \left(\frac1{4\lambda}-\epsilon\right)(\log n)^2
 \right\rfloor,
 \qquad
 \frac1{4\lambda}=0.4273778228378637\ldots .             \tag{18}
\]

Then (16)--(18) imply, uniformly for every point set and hence for every
minimizer,

\[
 \boxed{\frac{nZ_{\le D}(1/2)}{Z_P(1)}=o(1).}             \tag{19}
\]

Thus the half-weight theorem is reduced, without loss, to endpoint faces
whose horizontal span is at least

\[
 (0.4273778-o(1))(\log n)^2.                              \tag{20}
\]

More generally, a lower coefficient `c` in
`log f(n)>=(c-o(1))log^2 n` moves the escape threshold to
`(c/log(3/2)-o(1))log^2 n`.

This is only a support reduction, not a coefficient improvement: the
remaining spans are still merely polylogarithmic, not macroscopic.

## 4. What span-squared full localization would and would not give

The only rung of the numerical ladder not refuted here is

\[
 m^2F_{ij}(1/2)\le C Z_{P[i,j]}(1).                       \tag{FI2}
\]

I found neither a proof nor a counterexample.  The wrapper identity (5) is a
clean necessary subproblem for it.

Even a proof of `(FI2)` does not by itself improve the `1/4` coefficient.
After summing it over root intervals, a target face of exact span `d` is
charged through its superintervals with load

\[
 \sum_{I\supseteq A}|I|^{-2}
 =O\!\left(\log\frac nd+1\right),                         \tag{21}
\]

and short targets attain harmonic-order load.  The direct global conclusion
is only `Z(1/2)<=O(log n)Z(1)`, weaker than the trivial `Z(1/2)<=Z(1)` for
the half-weight target.  In the span/cardinality bootstrap, exponent two is
the critical value and reproduces the existing `1/4` fixed point; an
improvement needs either a power strictly above two against unmarked full
mass or a history-retaining escape which prevents the harmonic reuse.

The counterfamily shows why the latter history cannot be “retain one of the
old endpoints.”  Both endpoints sometimes have to be abandoned, and the
new face must carry a replacement location (a nested interval, tangent
cell, or pocket address) instead.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_endpoint_ladder_proof/verify_endpoint_ladder.py
```

The script:

1. constructs the integral coordinates (6);
2. checks every determinant and the exact formulas (7);
3. independently computes the root cup and cap polynomials by tangent-path
   dynamic programming;
4. independently sums the left- and right-marker endpoint masses;
5. brute-force checks the entire convex profile through twelve total points;
6. writes `certificate.json` using exact rational arithmetic.

