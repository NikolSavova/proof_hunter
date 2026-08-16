# Weighted cap envelopes: the exact exponential transition and the minimizer endpoint parameter

**Date:** 2026-08-15. All face counts are nonempty and all logarithms are
base two.

## Verdict

For an (a)-point planar order type in a fixed generic projection chart,
write (W) for its ordinary-face count and (C) for its cap count. Define

\[
 g_C(a,t)=\min_Q\{W(Q)+tC(Q)\},\qquad t>0,                 \tag{1}
\]

where the minimum includes every realizable order type and every projection
chart. The dual envelope (g_U) is identical by reflection.

There are two exact positive conclusions.

First, a globally minimal literal seam (P=A\prec B) forces (A) and
(B) onto these true planar envelopes:

\[
 W_A+U_BC_A=g_C(a,U_B),\qquad
 W_B+C_AU_B=g_U(b,C_A).                                  \tag{2}
\]

Let (f(a)=\min_QW(Q)), and define the endpoint parameter

\[
 p(a)=\min\{C_\theta(Q):W(Q)=f(a),\ \theta
                 \text{ a generic projection chart}\}.       \tag{3}
\]

Then simultaneous child optimality gives the surprisingly strong bounds

\[
 \boxed{
 C_A\le p(a),\quad W_A-f(a)\le U_B\{p(a)-C_A\},
 }
 \qquad
 \boxed{
 U_B\le p(b),\quad W_B-f(b)\le C_A\{p(b)-U_B\}.
 }                                                            \tag{4}
\]

Thus an ordinary-face minimizer is not merely one possible competitor: it
upper-bounds the facing profile of every weighted child selected by a
globally minimal seam. This reduces the variational residue to the actual
directional endpoint profile (p(a)) of ordinary-face minimizers.

Second, the large-(t) end of (1) is completely rigid. Put

\[
                   \ell_a=a+{a\choose2}.                       \tag{5}
\]

The unique profile with (C=\ell_a) is the all-cup convex chain,
((W,C)=(2^a-1,\ell_a)). There is an exact critical value

\[
 T_a=\max_{Q:C(Q)>\ell_a}
       {2^a-1-W(Q)\over C(Q)-\ell_a}                            \tag{6}
\]

such that the all-cup profile minimizes (1) exactly for (t\ge T_a), and
is the unique minimizing profile for (t>T_a). For every (a\ge4),

\[
 \boxed{
 2^{a-3}-1\le T_a\le2^a-1-f(a)\le2^a-1-\ell_a.
 }                                                             \tag{7}
\]

The lower bound is stretchable and explicit. Hence the transition is
exponential in the child size, sharp up to a factor eight. This is a
barrier, not a fixed-gap closure: in the live near-ambient slice,
(a\gg(\log n)^2) while every seam penalty satisfies
(U_B<V(P)=2^{O((\log n)^2)}\). Thus (U_B\ll T_a), exponentially far
from the rigid cap-minimizer regime.

There is one further exact lower envelope from planar triple geometry. If
(W(Q)<H), put

\[
 k=\lceil\log(H+1)\rceil,qquad
 \Gamma(a,k)=\left\lceil{{a\choose3}\over{k\choose3}}\right\rceil.
                                                                    \tag{8}
\]

For (3\le k\le a), every such (Q) satisfies

\[
                       C(Q)\ge\ell_a+\Gamma(a,k).              \tag{9}
\]

Consequently a seam below a parent target (F), with
(k=\lceil\log(F+1)\rceil\le\min(a,b)), obeys

\[
 V(P)\ge f(a)+f(b)+
       \{\ell_a+\Gamma(a,k)\}\{\ell_b+\Gamma(b,k)\}.          \tag{10}
\]

For balanced near-ambient children and
(F=2^{c(\log n)^2}), the new product in (10) has only polynomial size,
about (n^6/(\log n)^{12}). It remains exponentially below (F) on the
quadratic-logarithmic scale. Thus triple-cover supersaturation improves the
rank-two baseline by a polynomial factor but does not rule out a fixed
sub-half gap.

The scope-honest endpoint is therefore: weighted seam minimality has been
reduced to the unknown minimizer parameter (p(a)), while both the exact
large-penalty transition and the strongest elementary cap-triple cover are
on the wrong scale. A closure needs a new theorem on directional profiles
of ordinary-face minimizers, or a mutation which crosses the high wall
without paying the whole endpoint transition. No half-coefficient closure
is claimed.

## 1. Envelope calculus and the ordinary-minimizer comparison

For fixed (a), only finitely many pairs ((W,C)) occur. Hence (g_C(a,t))
is a nondecreasing, concave, piecewise-linear function whose slopes are
integer cap counts. If (0<t_1<t_2), and (Q_i) is optimal at (t_i),
adding the two optimality inequalities gives

\[
                         C(Q_2)\le C(Q_1).                       \tag{11}
\]

Thus the selected cap slope decreases monotonically with the penalty.

Now suppose (P=A\prec B) is a literal strong glue and is globally
(V)-minimal among all ((a+b))-point configurations. Holding (B) fixed
and physically reembedding an arbitrary (a)-point configuration (Q) in
the left strong-glue chart gives

\[
 W_A+W_B+C_AU_B\le W(Q)+W_B+C(Q)U_B.
\]

This proves the first equality in (2); the second is symmetric.

Choose an ordinary-face minimizer (Q_a) and a projection chart attaining
(p(a)). Equation (2) gives

\[
             W_A+U_BC_A\le f(a)+U_Bp(a).                       \tag{12}
\]

Since (W_A\ge f(a)), rearranging proves the first box in (4). Reflection
turns the minimum cap count of a minimizer into the minimum cup count of a
minimizer, proving the second box.

The comparison is strict in a useful sense: if (W_A>f(a)), then
(C_A<p(a)). Thus every ordinary-count penalty paid by the selected child
must buy a literal decrease in its facing endpoint count. What is missing
is an asymptotic lower description of this Pareto tradeoff for planar
minimizers.

For orientation, the exact unique nine-point ordinary minimizer has
(f(9)=168) and (p(9)=82), after all 72 generic projection chambers are
enumerated. The stored eight-point minimizer has (f(8)=113) and a chamber
with (C=56), so (p(8)\le56). These finite values show that (p(a)) can
be substantially smaller than (f(a)), but do not determine its
asymptotic scale.

## 2. Exact all-cup transition

Every singleton and pair is a cap, so (C\ge\ell_a). If equality holds,
there is no cap triple. Therefore every ordered triple is a cup, the whole
configuration is an all-cup convex chain, and all its nonempty subsets are
ordinary. This proves

\[
                  C=\ell_a\quad\Longleftrightarrow\quad
                  (W,C)=(2^a-1,\ell_a).                        \tag{13}
\]

For any other profile,

\[
\begin{aligned}
 &[W(Q)+tC(Q)]-[2^a-1+t\ell_a]\\
 &\qquad=(C(Q)-\ell_a)
 \left[t-{2^a-1-W(Q)\over C(Q)-\ell_a}\right].                \tag{14}
\end{aligned}
\]

Taking the maximum proves the transition statement (6). Since
(W(Q)\ge f(a)) and (C(Q)-\ell_a\ge1), the upper bounds in (7) follow.

### A one-flip stretchable lower witness

Use the integer coordinates

\[
 p_0=(0,0),\qquad p_1=(1,5),\qquad
 p_i=(i,2i^2)\quad(2\le i<a).                                  \tag{15}
\]

Relative to the all-cup parabola, exactly the triple (012) changes sign.
With the cap convention chosen accordingly, it is the sole cap triple and
there is no cap face of rank at least four. Hence

\[
                         C=\ell_a+1.                            \tag{16}
\]

The bad four-sets are exactly (012j), (3\le j<a). By planar
four-locality, a nonempty subset is bad exactly when it contains (012)
and at least one further label. Therefore

\[
 W=(2^a-1)-(2^{a-3}-1)=7\cdot2^{a-3}.                          \tag{17}
\]

The ratio in (6) is (2^{a-3}-1), proving the lower bound in (7). At
(a=4), the complete rooted order-type menu gives

\[
 g_C(4,t)=
 \begin{cases}
 14+11t,&0<t\le1,\\
 15+10t,&t\ge1,
 \end{cases}                                                   \tag{18}
\]

with a tie at (t=1). Thus (T_4=1), and both sides of (7) are exact.

## 3. Cap-triple covering lower envelope

Let (mathcal T_C(Q)) be the set of cap triples and put
(m_C=|\mathcal T_C(Q)|). If (Q) had an all-cup (k)-subset, all
(2^k-1) of its nonempty subsets would be ordinary. Thus
(W(Q)<H\le2^k-1) implies that every (k)-subset contains a cap triple.

Count pairs ((T,K)) with (T\in\mathcal T_C(Q)), (|K|=k), and
(T\subseteq K). This gives

\[
 m_C{a-3\choose k-3}\ge {a\choose k},
 \qquad
 m_C\ge{{a\choose3}\over{k\choose3}}.                        \tag{19}
\]

All these triples are distinct cap faces in addition to the singleton-pair
baseline, proving (9).

If (P=A\prec B) has (V(P)<F), then (W_A,W_B<F). Apply (9) to cap
triples in (A) and, dually, cup triples in (B). The strong-glue mixed
bank (C_AU_B), together with (W_A\ge f(a)) and (W_B\ge f(b)), proves
(10).

This argument is genuinely planar through the interpretation of all-cup
sets, but its terminal arithmetic is polynomial. For
(a,b\asymp n) and (k=O((\log n)^2)), one has

\[
 \Gamma(a,k)\asymp {a^3\over k^3},\qquad
 \Gamma(a,k)\Gamma(b,k)=n^{6-o(1)},                            \tag{20}
\]

whereas a fixed-gap target is (2^{\Theta((\log n)^2)}).

## 4. Exact surviving gate

The three exact facts now available for a globally minimal literal seam are

\[
\begin{gathered}
 C_A\le p(a),\qquad U_B\le p(b),                               \tag{21}\
 C_A\ge\ell_a+\Gamma(a,k),\qquad
 U_B\ge\ell_b+\Gamma(b,k),                                    \tag{22}\
 W_A-f(a)\le U_B\{p(a)-C_A\},\qquad
 W_B-f(b)\le C_A\{p(b)-U_B\}.                                \tag{23}
\end{gathered}
\]

Equation (22) is far below the scale at which (21) would become
contradictory. Equation (7) says that the completely rigid endpoint of the
envelope is exponentially farther away still. Therefore an envelope-only
proof needs new information about (p(a)) or about the curvature of the
Pareto frontier between (f(a)) and the cap baseline.

For a nonliteral cage, even (2) remains conditional on promoting the cage
to a physical two-block replacement chart. Common-edge trace matching by
itself does not supply that promotion.

## 5. Verification

Run:

    python3 agent_outer_internal_product/verify_weighted_cap_envelope_exponential_transition_gate.py

The verifier:

1. checks the monotone-slope and ordinary-minimizer comparison algebra on
   thousands of exact integer profile rows;
2. exhausts every subset of the rational one-flip witness through
   (a=16), proving (15)--(17) and the exact bad-set classification;
3. exhausts all rooted four-point sign types and proves (18);
4. checks the cap-triple covering inequality on the stored rational
   Pascal and minimizer configurations;
5. enumerates every projection chamber of the stored eight- and nine-point
   minimizers, recovering endpoint minima (56) and (82); and
6. verifies on exact integers that the all-cup transition lies above while
   the triple-cover bank lies below the fixed-gap target through
   (L=128).

It prints PASS.
