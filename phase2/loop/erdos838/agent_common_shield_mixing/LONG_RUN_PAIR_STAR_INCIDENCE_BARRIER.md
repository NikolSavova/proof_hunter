# The long-run pair-star incidence graph can be empty at the live deficit scale

**Date:** 2026-08-15. All logarithms are base two.

> **Least-counterexample retraction.**  The target-normalized record-mass
> calculation below is correct, as are the empty full-context incidence and
> decoder-load statements.  But this particular planar chart is not a
> globally live least-counterexample barrier: its outside-word family and
> its one-sided child releases already form ordinary face banks at or above
> the half-scale target.  See LONG_RUN_LEAST_COUNTEREXAMPLE_REAUDIT.md for
> the exact audit and the strictly weaker four-local obstruction that
> survives global normalization.

## Verdict

The sufficient incidence theorem in
RECOVERABLE_CARRIER_COARSENING_MASK_RUN_GATE, equations (24a)--(24c), is
sharp even after imposing the actual rank-safe and effective-branching
hypotheses.

There is a scalable rational construction with:

* one arbitrary prescribed \(m\)-point child order type, where
  \(m=\Theta(n/\log\log n)\);
* a pair-star \(\mathcal J\) satisfying
  \[
        |\mathcal J|\ge {V(Y)-m-1\over\binom m2};       \tag{1}
  \]
* \(q=\Theta(\log n)\) outside roles of size
  \(D=\Theta(n/\log n)\), split into two macro arcs;
* every partial outside transversal ordinary;
* uniform effective branching \(r_i=D\) at every outside role;
* literal record weights \(1/n\); and
* one fixed carrier/chamber chart, so the carrier description load is one.

Nevertheless, for every full outside word \(S\) and every
\(F\in\mathcal J\),

\[
                         F\cup S\notin\mathcal F(P).    \tag{2}
\]

Indeed, the pair-star pair can be named \(o,p\) so that for the canonical
left and right labels \(a(S),b(S)\),

\[
             p\in\operatorname{int}\triangle(o,a(S),b(S)).       \tag{3}
\]

Thus the compatible incidence graph \(E\) in (24a) is empty. This is a
fixed physical \(1+3\) circuit class, not metadata or an abstract
incompatibility graph.

The construction matches the required three-logarithm scale. Put

\[
 L=\log n,\qquad L_2=\log L,\qquad L_3=\log L_2,
 \qquad \Phi_C(x)={x^2\over2}-Cx\log x.                \tag{4}
\]

Choose

\[
 m=\left\lfloor{n\over L_2}\right\rfloor,\qquad
 q={L\over2}-(C-\tfrac12)L_2+O(1),\qquad
 D=\left\lfloor{n-m\over q}\right\rfloor.              \tag{5}
\]

Then

\[
 \log m=L-L_3+o(1),\qquad
 \log D^q=\Phi_C(L)+O(L).                              \tag{6}
\]

If the child meets the inductive benchmark
\(\log V(Y)\ge\Phi_C(\log m)\), its pair-star and the complete outside
word family give, with record weight \(1/n\), total record mass \(M\)
satisfying

\[
 \boxed{\qquad
 M\ge {2^{2\Phi_C(L)}
          \over n^{(1+o(1))L_3}}.
 \qquad}                                               \tag{7}
\]

Therefore this is exactly an
\(n^{\Theta(\log\log\log n)}\)-deficit regression.

Sparse fixed circuits do not automatically give a global charge. For the
\(|\mathcal J|D^q\) unweighted records, the raw circuit or its ordinary
three-point deletion has load exactly

\[
                         |\mathcal J|D^{q-2},           \tag{8}
\]

while the outside word has load \(|\mathcal J|\), the child face has load
\(D^q\), and the injective pair \((F,S)\) is a separated two-face state.
After multiplying by the record weight \(1/n\), every entry is divided by
\(n\). The actual carrier is fixed and the word roles are visible, so none
of these loads is a hidden chamber ambiguity.

This does **not** construct a sub-half point set. The complete ambient
face complex may contain multi-label faces inside the outside role cells
or other directional child profiles. Consequently the conclusion is
precise:

> rank-safe minimizer weights, complete mass-uniform role branching, the
> near-ambient child scale, and a recoverable carrier do not force the
> pair-star incidences or a bounded-load circuit tag. Any positive proof
> must use global minimality to charge an ambient multi-label/profile bank
> outside this trace complex.

No arbitrary-child splice or coefficient-half conclusion is asserted.

## 1. Arbitrary child order types admit the common cage

Let \(Y_0\) be any rational general-position realization with face count
\(H\). By double counting pair--face incidences, some pair
\(\{o,p\}\) has the coface family

\[
 \mathcal J=\{F\in\mathcal F(Y_0):\{o,p\}\subseteq F\},
 \qquad
 |\mathcal J|\ge {H-m-1\over\binom m2}.                \tag{9}
\]

Choose affine coordinates \(f,g\) on the child with all \(f\)-values
distinct and \(f(p)>f(o)\). For small rational \(\varepsilon>0\), put

\[
 \begin{aligned}
 A_y&=A_0+\varepsilon f(y)+\varepsilon^2g(y),\\
 B_y&=B_0+\varepsilon f(y)-\varepsilon^2g(y),
 \end{aligned}                                        \tag{10}
\]

where \(A_0=B_0>0\), and map

\[
 (A,B)\longmapsto
       \left({A-B\over A+B},-{2\over A+B}\right).      \tag{11}
\]

The map from \((f,g)\) to \((A,B)\) is invertible affine, and (11) is
projective with one positive denominator on the finite child. Hence it
preserves the labelled order type and the complete face complex of
\(Y_0\). Both tangent coordinates increase with \(f\), so \(p\) is
strictly nested inside \(o\) relative to the two macro anchor directions.

Put \(q/2\) role cells on a short left arc and \(q/2\) on a short right
arc of a rational convex parabola. Every cell has \(D\) labels and is
shrunk until every partial transversal has the macro order type. The
nesting inequalities are open, so the child and cells can be chosen in
rational ambient general position with

\[
       p\in\operatorname{int}\triangle(o,a,b)          \tag{12}
\]

for every left label \(a\) and every right label \(b\).

Every full word contains a canonical left--right pair. Since every
\(F\in\mathcal J\) contains \(o,p\), equation (12) proves (2). The word
itself is ordinary and its disjoint role traces recover every coordinate.
There is one fixed chart and no carrier decoder loss.

The construction can retain the actual marked-root provenance. Choose
three further points \(T\) on the same convex macro shell so that the
small child lies strictly inside \(\triangle(T)\), while \(T\) together
with every outside word is convex. Then every child label belongs to one
fixed rooted pocket of the ordinary marked source \(T\cup S\). The
stationary root \(T\) can be deleted once, at constant description cost;
the coarsened outside context in (2) is the remaining word \(S\). Equation
(12), which is independent of \(T\), still makes every pair-star
incidence bad. Thus the regression survives the genuine rooted entrance
rather than manufacturing weights after the root has been forgotten.

The construction permits arbitrary prescribed rational order types inside
all role cells as well: only one label per cell is used in the word trace.
It does not assume those cells are convex clouds.

## 2. Actual role-forest mass hypotheses

Give each outside word one upstream marked-source occurrence of weight
\(1/n\), then expand that marked occurrence over the pair-star faces
\(F\in\mathcal J\). This is the same whole-record duplication used by the
marked pocket release bank; it does not fractionally split the source
mark.

At a role node, every label class has the same number of word
continuations and the same profile multiplicity. Therefore

\[
 b_{i,z}={b_i\over D},\qquad
 r_i={b_i\over\max_zb_{i,z}}=D.                       \tag{13}
\]

Thus the example satisfies the strongest possible effective branching,
not merely large support. The outside rank is

\[
                         q=(1/2+o(1))L<2L,             \tag{14}
\]

so it lies inside the rank-safe cutoff. The point budget is literal:
\(m+qD\le n\).

The upstream per-source marked weight remains \(1/n\). After release, one
source is incident with \(|\mathcal J|\) profile copies, each still of
weight \(1/n\). This is the desired release multiplier, not a violation of
the upstream row cap. Dividing those copies by \(|\mathcal J|\) would
erase the very mass that the long-run composition is supposed to count.

## 3. Three-logarithm parameter audit

Let \(\ell=\log m=L-L_3+o(1)\). If
\(H\ge2^{\Phi_C(\ell)}\), then for large \(n\), (9) gives

\[
             \log|\mathcal J|
       \ge \Phi_C(\ell)-2\ell-O(1).                   \tag{15}
\]

The choice of \(q\) in (5) is obtained by solving
\(q(L-\log q)=\Phi_C(L)\) to first lower order. Since
\(\log q=L_2-1+o(1)\),

\[
\begin{aligned}
 q\log D
 &=\left({L\over2}-(C-\tfrac12)L_2+O(1)\right)
       (L-L_2+1+o(1))\\
 &=\Phi_C(L)+O(L),                                    \tag{16}
\end{aligned}
\]

proving (6). The total weighted record mass is

\[
                         M={|\mathcal J|D^q\over n}.   \tag{17}
\]

Combining (15)--(17),

\[
\begin{aligned}
 2\Phi_C(L)-\log M
 &\le \Phi_C(L)-\Phi_C(L-L_3)+3L+O(L)\\
 &=L L_3-\frac12L_3^2
   -C\{L\log L-(L-L_3)\log(L-L_3)\}+O(L)\\
 &=(1+o(1))L L_3.                                    \tag{18}
\end{aligned}
\]

This proves (7). The \(m^2\) pair-star loss and the \(1/n\) mark weight
cost only \(3L+O(1)\) bits, lower order than \(L L_3\).

Equation (7) is normalized to the proposed half benchmark
\(2^{\Phi_C(L)}\). It is not a proof that the assembled configuration
itself has at most that many faces. Establishing or exploiting that global
minimality bound is exactly the ambient-bank operation absent from the
local hypotheses.

## 4. Exact circuit and decoder loads

Index a full word by \(\omega\in[D]^q\). Let \(a_\omega,b_\omega\) be
its labels in the two roles adjacent to the central gap. The record family
is

\[
                     \mathcal R=\mathcal J\times[D]^q. \tag{19}
\]

The following loads are exact for uniform unweighted records:

\[
\begin{array}{c|c|c}
\text{retained state}&\text{number of states}&
                 \text{load of each state}\\ \hline
(o,p,a_\omega,b_\omega)&D^2&|\mathcal J|D^{q-2}\\
\{o,a_\omega,b_\omega\}&D^2&|\mathcal J|D^{q-2}\\
S_\omega&D^q&|\mathcal J|\\
F&|\mathcal J|&D^q\\
(F,\{o,a_\omega,b_\omega\})&|\mathcal J|D^2&D^{q-2}\\
(F,S_\omega)&|\mathcal J|D^q&1.
\end{array}                                             \tag{20}
\]

Every three-point circuit deletion in the second row is an actual ordinary
face, but it remembers only two outside word coordinates. The last row is
injective but is a separated pair of already ordinary faces, so it invokes
\(V(P)^2\), not one copy of \(V(P)\). Multiplication by \(1/n\) gives the
weighted loads.

There are two further sharp state bounds. Because of (12), an ordinary
output retaining a full word contains at most one child label. Hence all
such releases have at most

\[
                         D^q(m+1)                      \tag{21}
\]

states and some state has profile-history load at least
\(|\mathcal J|/(m+1)\). If instead the output keeps an arbitrary child
face but deletes all roles on at least one macro side, even optimistically
granting every candidate union yields at most

\[
              |\mathcal J|\{2(D+1)^{q/2}-1\}          \tag{22}
\]

states. This loses half the outside word entropy. Thus the common circuit
cannot be charged by its triangle, by the old source alone, by the child
face alone, by a rank-one release, or by deleting one complete side.

## 5. Exact remaining implication

The example rules out both proposed conclusions from the displayed local
data:

1. High effective branching and the near-ambient child size do not force
   even one compatible pair-star incidence per full outside context.
2. A common signed \(1+3\) circuit class does not have bounded aggregate
   load when its two outer labels record only two of \(\Theta(L)\) word
   coordinates.

It does not rule out a minimizer-specific theorem of the following form:

> if (2) holds on target-normalized mass (7), then some ambient multi-label
> role face or a directional child profile has enough globally bounded
> overlap to increase the actual \(V(P)\).

That is the exact next operation. It must use a face outside the
one-label-per-role trace complex; the pair-star incidence graph and the
fixed circuit tags contain no such information.

## 6. Verification

Run

~~~text
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_long_run_pair_star_incidence_barrier.py
~~~

The verifier imports the exact rational six-point arbitrary-child
realization from the shield audit, adds an exact common root triangle,
checks that every rooted source is ordinary and every child label is in
its pocket, enumerates all pair-star faces and all outside words, checks
that the compatible incidence graph is empty, and computes every load in
(20). It also checks complete effective branching, the rank and
point-budget formulas, and the corrected three-logarithm asymptotics
through \(L=2^{16}\).
