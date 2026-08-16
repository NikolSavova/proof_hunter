# Nested triangles: the macroscopic vertex-cloud fixed-gap gate

**Date:** 2026-08-15. This continues
`FIRST_INCOHERENT_SIBLING_NESTED_TRIANGLE_BARRIER.md` and uses the exact
outermost-trace recurrence in
`agent_common_shield_mixing/NESTED_TRIANGLE_PARTIAL_TRACE_TELESCOPE.md`.

## Verdict

The three vertex clouds of a linear nested-triangle array are macroscopic.
Their induced face complexes occur inside the singleton terms of the exact
partial-trace telescope with load one. This improves the natural induction
restart from the small central child of size \(n/\log\log n\) to a cloud of
size \((1-o(1))n/3\). The remaining target loss is only

\[
                         n^{\log_2 3+o(1)},                  \tag{1}
\]

rather than \(n^{\Theta(\log\log\log n)}\).

There is, however, no automatic multiplication of the three cloud banks.
For two clouds, ordinary mixed unions have an exact load-one decoder. If
they do not already supply the target, then all but a

\[
                         2^{-(1/2-o(1))(log n)^2}           \tag{2}
\]

fraction of the Cartesian product of their face families is bad. Every bad
pair contains a planar four-circuit meeting both faces. Thus failure of the
polynomial fixed-gap gain promotes the nested-shell residue to an
almost-complete **face-by-face cross-circuit rectangle**.

This is a genuine sharpening but not closure. A single physical circuit
may witness a huge rectangle when the two face families share a small
root. Controlling that projection reuse is exactly the rooted
circuit/shield problem; the nesting recurrence alone supplies no bounded
decoder for it.

## 1. Maximum-layer cloud telescope

Let

\[
 P_0=Y,\qquad P_t=P_{t-1}\dot\cup T_t,\qquad
 P_{t-1}\subset\operatorname{int}\operatorname{conv}T_t,  \tag{3}
\]

and fix an arbitrary labeling

\[
                         T_t=\{x_{t,1},x_{t,2},x_{t,3}\}.
\]

The three vertex clouds are

\[
                         X_c=\{x_{t,c}:1\le t\le s\}.      \tag{4}
\]

No geometric coherence of this coloring is assumed. Write
\(H_c=V(X_c)\), and define

\[
 b_{t,c}=|\{F\in\mathcal F(X_c\cap P_t):x_{t,c}\in F,\
                 F\cap\{x_{u,c}:u>t\}=\varnothing\}|.      \tag{5}
\]

The last condition merely says that \(t\) is the maximum layer of \(F\).

> **Theorem 1 (cloud-to-singleton injection).** For each \(c\),
> \[
>                         \sum_{t=1}^s b_{t,c}=H_c.         \tag{6}
> \]
> Moreover, deleting \(x_{t,c}\) maps every face counted by \(b_{t,c}\)
> injectively into the compatible singleton profile
> \(\mathcal A_t(\{x_{t,c}\})\) of the outermost-trace recurrence. Hence
> \[
>  \sum_{t=1}^s\sum_{c=1}^3
>       |\mathcal A_t(\{x_{t,c}\})|
>                 \ge H_1+H_2+H_3.                         \tag{7}
> \]

**Proof.** Every nonempty face of \(X_c\) has a unique maximum layer
\(t\), proving (6). If \(F\) has maximum \(t\), then
\(F\setminus\{x_{t,c}\}\subset P_{t-1}\) and its union with the singleton
trace is the original ordinary face \(F\). The output recovers its layer,
color, and inner trace from physical labels, so the map has load one.
Summing gives (7). \(\square\)

This theorem counts recursively accumulated partial traces, not merely the
six first-order extensions of the original central family. It is also
sharp as an accounting identity: (6) is just the maximum-layer partition
of the induced cloud bank.

## 2. Exact fixed-gap normalization

Let the final size be \(N=2^L\), let the number of selected partner roles
be \(k=(1+o(1))\log L\), and let the central size be
\(m=N/\Theta(k)\). The circuit array has \(s=km\) triangle layers, so after
discarding harmless constant conventions,

\[
                         |X_c|=s=(1-o(1))N/3,qquad
                         \log s=L-\log_2 3+o(1).           \tag{8}
\]

For the campaign target

\[
                         \Phi_C(x)=x^2/2-Cx\log x,
\]

put \(a=\log_2 3\). Direct expansion gives

\[
                  \Phi_C(L)-\Phi_C(L-a+o(1))
                         =(a+o(1))L.                       \tag{9}
\]

Thus induction on any cloud and (7) reach the ambient target up to the
polynomial factor (1). This is substantially stronger than restarting
from \(Y\), whose deficit is \((1+o(1))L\log\log\log n\).

No constant number of additive cloud banks repairs (9). A further genuine
mixed or profile multiplier is still necessary.

## 3. Mixed-cloud Hall rectangle

Fix two colors \(i\ne j\), and let

\[
 \mathcal G_{ij}=\{(F_i,F_j)\in
       \mathcal F(X_i)\times\mathcal F(X_j):
                         F_i\cup F_j\text{ is convex}\}.   \tag{10}
\]

> **Theorem 2 (face rectangle or cross circuit).** The map
> \[
>                         (F_i,F_j)\longmapsto F_i\cup F_j \tag{11}
> \]
> is injective on \(\mathcal G_{ij}\). Every pair outside
> \(\mathcal G_{ij}\) contains a nonconvex four-set meeting both clouds.

**Proof.** The physical color classes are disjoint, so intersecting an
output in (11) with \(X_i,X_j\) recovers both inputs. If the union of two
convex sets is nonconvex, planar four-locality supplies a nonconvex
four-subset. Such a subset cannot lie in only one input because both inputs
are hereditary ordinary faces. Hence it meets both. \(\square\)

Assume strong induction supplies

\[
                         H_i,H_j\ge2^{\Phi_C(L-a+o(1))}.    \tag{12}
\]

If \(|\mathcal G_{ij}|\ge2^{\Phi_C(L)}\), (11) closes the
ambient target with load one. Otherwise the good density is at most

\[
 {2^{\Phi_C(L)}\over H_iH_j}
       \le 2^{\Phi_C(L)-2\Phi_C(L-a+o(1))}
       =2^{-(1/2-o(1))L^2},                               \tag{13}
\]

which proves (2). Therefore every unpaid cloud pair is an almost-complete
bad face rectangle with an actual cross-cloud four-circuit in every cell.

This formulation is quantitatively forgiving: a vanishingly small good
fraction would suffice. The surviving anti-alignment is correspondingly
extreme.

## 4. Why this stops at circuit projection reuse

Choose a canonical bad four-circuit in every bad cell of the rectangle.
There are at most \(O(N^4)\) physical circuit tags, so one tag may occur on
an enormous subrectangle. But this does not itself produce an ordinary
mixed face. A fixed circuit merely says that every face on each side
contains its corresponding one-, two-, or three-label trace. Removing that
trace leaves ordinary downfaces, while the released union may still contain
other bad circuits.

Consequently Theorem 2 interfaces exactly with the stable tournament core:

* diffuse circuit tags offer a polynomial-load trace bank;
* concentrated tags give a fixed-root circuit/shield component; and
* iterated removal needs the existing mask/run or endpoint-pocket decoder.

The nested-triangle hypothesis has done all the scale reduction available
for free: the required gain is now polynomial. It has not solved the
concentrated-root geometry.

The exact 12-point colorful-transversal barrier in
`COLORFUL_PAIR_ENDPOINT_TRANSVERSAL_BARRIER.md` also shows that endpoint
bits alone cannot replace this circuit state. Even a directed three-class
reset with convex internal classes may have no six-pair colorful face.

## 5. Finite exact audit

For six nested rational/integer triangles from the barrier verifier, the
three cloud face counts and their maximum-layer increments are

\[
\begin{array}{c|c|c}
c&H_c&(b_{1,c},\ldots,b_{6,c})\\ \hline
1&56&(1,2,4,7,14,28)\\
2&50&(1,2,4,8,13,22)\\
3&54&(1,2,4,8,13,26).
\end{array}                                                \tag{14}
\]

The exact mixed good/bad counts are

\[
\begin{array}{c|rr}
ij&|\mathcal G_{ij}|&H_iH_j-|\mathcal G_{ij}|\\ \hline
12&1230&1570\\
13&1120&1904\\
23&1036&1664.
\end{array}                                                \tag{15}
\]

The finite example is not anti-aligned: many mixed unions are good. The
verifier checks that every one of the remaining bad pairs contains an
actual cross-cloud four-circuit, illustrating Theorem 2 without assuming a
particular occupancy type.

## 6. Verification

Run

~~~text
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_nested_triangle_vertex_cloud_gate.py
~~~

The verifier checks (6) exactly for all three clouds, enumerates every
mixed pair and every required four-circuit, and audits (9) and (13) at four
large dyadic logarithmic scales.
