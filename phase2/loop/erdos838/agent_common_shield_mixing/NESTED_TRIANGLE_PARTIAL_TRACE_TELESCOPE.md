# Nested-triangle partial-trace telescope

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The singleton/edge interface in
FIRST_INCOHERENT_SIBLING_NESTED_TRIANGLE_BARRIER has an exact
load-one recurrence.  If

\[
 P_t=P_{t-1}\,\dot\cup\,T_t,\qquad
 P_{t-1}\subset\operatorname{int}\operatorname{conv}T_t,
                                                               \tag{1}
\]

then every new ordinary face has a unique nonempty trace
\(G\subset T_t\).  A full trace \(G=T_t\) cannot coexist with any old
label, so all mixed faces use a singleton or edge.  Consequently

\[
 Z_t=Z_{t-1}
     +\sum_{\substack{G\subset T_t\\|G|=1,2}}
        |\{F\in\mathcal F(P_{t-1}):F\cup G\text{ convex}\}|
     +1.                                                    \tag{2}
\]

Here \(\mathcal F\) includes the empty face and
\(Z_t=|\mathcal F(P_t)|\).  Every summand in (2) is a literal Hall bank:
the output \(F\cup G\) recovers \(t,G,F\), so its geometric decoder load
is one.

This does not supply the desired fixed-gap multiplier.  At the live scale
\(k\asymp\log\log n\), \(m\asymp n/\log\log n\), there are
\(s=km=\Theta(n)\) triangle layers.  Even if every original central face
coexisted with all six partial traces at every layer, the resulting
first-order bank would have size only \(O(n)V(Y)\).  But induction from
the central size to the ambient size requires

\[
 {2^{\Phi_C(\log n)}\over2^{\Phi_C(\log m)}}
       =n^{(1+o(1))\log\log\log n}.                    \tag{3}
\]

Thus the missing gain must come from recursive faces carrying partial
traces from many earlier layers.  Singleton/edge Hall overlap with the
original rich central bank, by itself, is quantitatively incapable of
closing the branch.

The exact surviving state is a six-profile multiplicative potential.  A
proof must lower-bound that potential using planar endpoint structure, or
exclude a profile-sparse common-guard child by minimizer-specific input.

## 1. Exact trace recurrence

Let \(P_0=Y\), and let \(T_1,\ldots,T_s\) be disjoint triangles satisfying
(1) successively.  For \(G\subseteq T_t\), define

\[
 \mathcal A_t(G)=
 \{F\in\mathcal F(P_{t-1}):F\cup G\in\mathcal F(P_t)\}. \tag{4}
\]

> **Theorem 1 (outermost-trace decomposition).**  For every \(t\),
> \[
> Z_t=Z_{t-1}+R_t+1,\qquad
> R_t=\sum_{\substack{G\subset T_t\\|G|=1,2}}
>                         |\mathcal A_t(G)|.            \tag{5}
> \]
> Moreover, the map
> \[
>             (t,G,F)\longmapsto F\cup G               \tag{6}
> \]
> is injective over all \(t\), all traces of rank one or two, and all
> \(F\in\mathcal A_t(G)\).

**Proof.**  Partition a face \(W\subseteq P_t\) by its trace
\(G=W\cap T_t\).

* If \(G=\varnothing\), then \(W\in\mathcal F(P_{t-1})\).
* If \(|G|=1,2\), then \(W=F\cup G\) for the unique
  \(F=W\cap P_{t-1}\), and it is counted by (4).
* If \(G=T_t\), then \(F\) must be empty: every old label lies strictly
  inside the triangle and would be hidden.  This gives the final \(+1\).

The triangle labels in an output recover \(t\) and \(G\); deleting them
recovers \(F\).  Different outermost layers use disjoint labels.  This
proves (5) and (6). \(\square\)

No circuit-description factor or pair decoder is hidden in (6).  A
carrier, source mark, or chronology label already retained in \(F\)
remains retained.  Conversely, if several genuine histories have already
collapsed to the same physical \(F\), (6) cannot distinguish them; their
history multiplicity remains an external load.

## 2. Weighted Hall form

Let \(\mathcal H\subseteq\mathcal F(P_{t-1})\) be a recoverable inner
family with nonnegative weights \(w(F)\).  The exact routed mass through a
trace \(G\) is

\[
             h_t(G)=\sum_{F\in\mathcal H\cap\mathcal A_t(G)}w(F).
                                                               \tag{7}
\]

If \(w(F)\le1\) is the actual canonical marked weight and \(F\) decodes
its mark, (6) routes (7) with physical output load at most one.  Across all
six traces and all layers, the outputs remain disjoint.

For the original central family \(\mathcal H=\mathcal F(Y)\), denote the
corresponding profile by \(\mathcal A_t^Y(G)\).  Even in the impossible
best case

\[
                    |\mathcal A_t^Y(G)|=Z_0
 \quad\text{for every }t,G,                            \tag{8}
\]

the number of faces carrying a central face and exactly one partial trace
is at most

\[
                           6sZ_0.                      \tag{9}
\]

Equation (9), not overlap, is the first-order bottleneck: its multiplier is
only \(O(n)\).

## 3. Universal low-rank trace bank

There is a sharp unconditional polynomial floor.  Put
\(N_{t-1}=|P_{t-1}|\).  Every old set of rank at most two is convex and
remains convex after adding one new vertex, because the result has rank at
most three.  Every old set of rank at most one remains convex after adding
one new edge.  Therefore, for each singleton \(x\subset T_t\) and edge
\(e\subset T_t\),

\[
\begin{aligned}
 |\mathcal A_t(\{x\})|
   &\ge 1+N_{t-1}+\binom{N_{t-1}}2,\\
 |\mathcal A_t(e)|
   &\ge 1+N_{t-1}.                                    \tag{10}
\end{aligned}
\]

Summing (10) over \(s=\Theta(n)\) layers gives only \(n^{O(1)}\) faces.
This is far below both the half-scale target and the multiplier (3).
Thus merely observing that every triangle releases six ordinary partial
traces cannot close the fixed-gap induction.

## 4. Exact multiplicative potential

Define

\[
             \rho_t={R_t+1\over Z_{t-1}}.              \tag{11}
\]

The additive recurrence (5) telescopes multiplicatively:

\[
 {Z_s\over Z_0}
       =\prod_{t=1}^s(1+\rho_t),\qquad
 \log{Z_s\over Z_0}
       =\sum_{t=1}^s\log(1+\rho_t).                    \tag{12}
\]

This is an exact Carleson-type accounting identity, not an inequality.
Partial traces from many layers are already included: a face
\(F\in\mathcal A_t(G)\) may itself carry traces from any subset of earlier
layers.

Group the \(s=km\) triangles into the \(k\) original partner roles.  If
the final configuration reaches the fixed-gap target, (3) and (12) force

\[
 \sum_{t=1}^s\log(1+\rho_t)
        \ge (1+o(1))(\log n)(\log\log\log n).           \tag{13}
\]

Equivalently, some partner-role block carries at least a \(1/k\) share of
the potential in (13).  A proof of the desired multiplier is now exactly
a lower bound of this size on the six compatible-trace profiles.

## 5. Least-counterexample normalization

Let \(N=|P_s|=2^L\), \(k=(1+o(1))L_2\), and
\(m=N/(3k)(1+o(1))\).  Then

\[
 \log m=L-\log(3L_2)+o(1)=L-L_3-O(1).                 \tag{14}
\]

For

\[
                   \Phi_C(x)=x^2/2-Cx\log x,
\]

a direct expansion gives

\[
 \Phi_C(L)-\Phi_C(\log m)
       =(1+o(1))LL_3.                                 \tag{15}
\]

Hence (3).  The verifier checks the ratio in (15) at four large dyadic
values of \(L\).  By contrast,

\[
                         \log(6s)=L+O(1),              \tag{16}
\]

so the complete first-order central Hall bank in (9) misses (15) by a
factor \(L_3\) in the exponent.

This corrects a possible normalization error: the load-one release of
\(\Theta(n)\) singleton/edge traces is real, but polynomial multiplicity
does not repair an \(n^{\Theta(L_3)}\) deficit.

## 6. Exact zero-profile stress

The rich-face overlap in (7) has no pointwise positive lower bound.  In
the shield verifier's rational five-point central child, the central face

\[
          F=\{(-3,-2),(3,-2),(-2,4)\}                 \tag{17}
\]

is convex.  For each of the first fifteen nested containing triangles and
for every one of its three singleton and three edge traces,

\[
                         F\cup G\text{ is nonconvex}. \tag{18}
\]

Thus one genuine central face has zero degree in the entire 90-incidence
partial-trace Hall graph.  Geometrically, each outer vertex lies in a
vertex cone of \(F\), while every outer edge hides part of \(F\).

This is not a globally live counterexample: a single rank-three face has
negligible mass, and other central faces or partner-only trace faces may
pay.  Its exact implication is that a proof of (13) must use aggregate
profile balance of a minimizer; it cannot assert that each rich central
face admits a singleton or edge from every containing triangle.

## 7. Trace-complex recurrence barrier

Equations (5) and (12) give the requested scalable trace-complex
recurrence.  At the level of hereditary four-local data, it is consistent
to place essentially all high central mass in states like (18), leave
only the polynomial floors (10), and obtain

\[
                       Z_s=Z_0+n^{O(1)}.               \tag{19}
\]

The finite stress proves the local state is planar.  A scalable planar
realization carrying quadratic-exponential mass in that state is **not**
proved.  Such a realization would be precisely a common-guard/profile-ramp
upper construction, an open construction-side branch of the campaign.

Therefore this report neither proves the half theorem nor constructs a
sub-half order type.  It sharply replaces the informal “partial traces
may pay” statement by the exact missing inequality:

\[
 \boxed{\quad
 \sum_t\log\!\left(
  1+{1+\sum_{|G|=1,2}|\mathcal A_t(G)|\over Z_{t-1}}
 \right)
 \ \ge\ (1+o(1))LL_3.
 \quad}                                                \tag{20}
\]

Possible inputs capable of proving (20) are:

* an all-direction endpoint-energy lower bound for the actual minimizer;
* a fixed-root telescope showing partner-role blocks cannot all reset;
* a profile-balance mutation excluding high mass in the state (18); or
* a bounded-load composition that retains an inner multi-trace face,
  rather than repeatedly returning to \(\mathcal F(Y)\).

## 8. Verification

Run

    python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_nested_triangle_partial_trace_telescope.py

The script exhausts four nested rational triangles over the five-point
central child.  It verifies (5), the output decoder, every low-rank floor
in (10), and the exact product identity (12).  It checks all 90 zero-profile
incidences in (18) and the fixed-gap expansion (15).  It prints PASS.
