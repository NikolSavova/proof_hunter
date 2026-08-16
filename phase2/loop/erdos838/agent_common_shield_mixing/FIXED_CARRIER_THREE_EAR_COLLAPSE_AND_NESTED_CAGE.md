# Fixed-carrier three-ear collapse and the nested support cage

**Date:** 2026-08-15. All faces are ordinary (convex-position) subsets.

## Verdict

A literal common carrier is strictly stronger than intersecting source
supports. It kills the three-ear Helly obstruction completely.

Let \(B\) be one ordinary carrier, let \(R_i\supseteq B\) be ordinary
contexts, and suppose the repair edge \(e_i\) is a boundary edge of both
\(B\) and \(R_i\). If the exposed-ear cells of the \(R_i\) meet pairwise,
then all \(e_i\) are the same physical edge \(e\), and one point
infinitesimally across \(e\) repairs every \(R_i\) simultaneously. In fact,
connectedness of the pairwise-intersection graph suffices.

Thus the exact nine-point minimizer obstruction does **not** survive this
literal state: its three sources have only one common label, not a common
edge-bearing carrier.

The collapse is not yet an ordinary-face multiplier in the original
configuration. A scalable rational nested cage has a common triangle
\(B\), a common hidden root \(z\), one common exposed repair edge \(uv\),
and \(q\) contexts \(R_t=B\cup\{a_t\}\). One nearby point repairs all
contexts, but

\[
                 R_s\cup R_t\text{ is nonordinary}\qquad(s\ne t). \tag{1}
\]

Among faces retaining \(B\), the original configuration has only \(q+1\)
outputs. The re-embedded configuration has \(2q+2\), still linear. The
common repaired carrier has history load \(q\); the full repaired context
has load one but retains only one source index. Hence common-carrier repair
solves the geometric three-ear feasibility problem, while the
two-source-to-one-face decoder remains a separate operation.

## 1. Literal fixed-carrier theorem

For an ordinary set \(R\) and a boundary edge \(e=uv\), write
\(\mathcal C(R,e)\) for the open ear cell of positions \(p\) such that
\(R\cup\{p\}\) is ordinary and \(p\) is inserted between \(u,v\) on its
boundary.

> **Theorem 1 (fixed-carrier three-ear collapse).** Let \(B\) be ordinary
> with at least three points. Let \(R_1,\ldots,R_t\) be ordinary sets
> containing the same literal point set \(B\). For each \(i\), assume
> \(e_i\) is a boundary edge of both \(B\) and \(R_i\). Form the graph on
> \([t]\) in which \(ij\) is an edge when
> \[
>             \mathcal C(R_i,e_i)\cap\mathcal C(R_j,e_j)
>                          \ne\varnothing.                       \tag{2}
> \]
> On every connected component of this graph, all \(e_i\) are one physical
> edge \(e\), and
> \[
>                       \bigcap_i\mathcal C(R_i,e)\ne\varnothing. \tag{3}
> \]
> In particular, pairwise feasibility implies simultaneous feasibility.

**Proof.** If \(p\in\mathcal C(R_i,e_i)\), heredity makes
\(B\cup\{p\}\) ordinary. Deleting \(R_i\setminus B\) preserves the cyclic
order, so \(p\) is still inserted through \(e_i\). Hence

\[
                         \mathcal C(R_i,e_i)
                              \subseteq\mathcal C(B,e_i).         \tag{4}
\]

The open ear cells of two distinct boundary edges of one convex polygon
are disjoint: the insertion edge of \(p\) in \(B\cup\{p\}\) is unique.
Therefore every graph edge in (2) forces \(e_i=e_j\), and connectedness
forces one physical edge \(e=uv\).

Let \(x\) lie in the relative interior of \(uv\), and let \(n\) point
strictly outward across \(uv\). For each finite polygon \(R_i\), the point
\(x+\epsilon n\) replaces the edge \(uv\) by
\(u(x+\epsilon n)v\) for every sufficiently small \(\epsilon>0\).
All other supporting inequalities have positive slack at \(x\). Taking
the minimum of the finitely many permissible \(\epsilon\)'s proves (3).
\(\square\)

The requirement that \(e_i\) remain an actual boundary edge of \(R_i\) is
essential. Saying only that \(e_i\) is an edge of a named subface \(B\),
while other retained labels cover that edge, does not give (4).

## 2. Why the nine-point minimizer barrier is excluded

In the exact nine-point example of
THREE_EAR_MINIMIZER_BARRIER_AND_ORDER_THREE_GATE.md, the three source
triangles are

\[
 R_1=\{0,1,6\},\qquad R_2=\{0,1,7\},\qquad R_3=\{1,3,8\},          \tag{5}
\]

with repair edges \(61,71,38\). Their literal common intersection is only
\(\{1\}\). There is no common rank-two edge, let alone a common ordinary
carrier whose boundary contains all three repair edges. Thus that genuine
minimizer-safe Helly cage does not test Theorem 1.

This distinction is physical, not semantic:

* merely intersecting sources can support three unrelated ear charts;
* a literal common carrier identifies insertion edges in one cyclic
  boundary, making distinct charts disjoint and equal charts locally
  simultaneous.

## 3. Scalable nested support cage

The following family shows exactly what Theorem 1 does not prove. Fix
\(q\ge3\), put \(\delta=1/(100q^2)\), and let

\[
\begin{aligned}
 u&=(-2,0),&v&=(2,0),&w&=(0,6),&B&=\{u,v,w\},\\
 z&=(0,1),&m&=(1,3),&n&=(3,1),&d&=(-2,6).
\end{aligned}                                                     \tag{6}
\]

For \(1\le t\le q\), define

\[
                         a_t=m+tn+\delta t^2d,                    \tag{7}
\]

and set \(R_t=B\cup\{a_t\}\). The point \(a_t\) lies in the ear cell of
the carrier edge \(vw\). Therefore \(R_t\) is an ordinary quadrilateral,
and the different edge \(uv\) remains exposed in every \(R_t\). The common
root \(z\) is strictly inside \(B\), so

\[
                         R_t\cup\{z\}\text{ is nonordinary}       \tag{8}
\]

through the same retained carrier triangle.

The point

\[
                              p=\left(0,-{1\over100q}\right)      \tag{9}
\]

lies in every \(\mathcal C(R_t,uv)\). Thus moving the common root label
from \(z\) to \(p\) repairs all \(q\) contexts in one common chart, exactly
as Theorem 1 predicts.

For \(1\le s<t\le q\), put

\[
 b_{s,t}=m-\delta st\,d.
\]

Since \(\delta st<1/2\), the point \(b_{s,t}\) lies strictly inside the
segment \(vw=\{m+\lambda d:|\lambda|\le1/2\}\). Directly,

\[
                         a_s={s\over t}a_t+
                              \left(1-{s\over t}\right)b_{s,t}.   \tag{10}
\]

Thus \(a_s\) is strictly inside the triangle
\(\operatorname{tri}(v,w,a_t)\), proving (1). In particular no ordinary
face retaining \(B\) can retain two different source labels \(a_s,a_t\).

All displayed coordinates are rational. The verified \(q=14\) instances
before and after moving \(z\) are in general position. At any exceptional
parameter where a cross triple is collinear, an arbitrarily small rational
perturbation of \(z\) or \(p\), inside its open cell, preserves every strict
claim and gives a general-position realization.

## 4. Exact face and history ledger

Let

\[
 P_{\rm old}=B\cup\{z\}\cup\{a_1,\ldots,a_q\},\qquad
 P_{\rm new}=B\cup\{p\}\cup\{a_1,\ldots,a_q\}.                    \tag{11}
\]

Heredity together with (8) and (10) gives the complete \(B\)-retaining
face ledgers:

\[
\begin{aligned}
 \{F\in\mathcal F(P_{\rm old}):B\subseteq F\}
     &=\{B\}\cup\{B\cup\{a_t\}:1\le t\le q\},\\
 \{F\in\mathcal F(P_{\rm new}):B\subseteq F\}
     &=\{B,B\cup\{p\}\}\\
     &\quad{}\cup\{B\cup\{a_t\},B\cup\{p,a_t\}:1\le t\le q\}.
                                                                    \tag{12}
\end{aligned}
\]

Their sizes are \(q+1\) and \(2q+2\). For the \(q\) marked bad histories
\((R_t,z)\):

* routing every history to the common repaired carrier \(B\cup\{p\}\) has
  decoder load exactly \(q\);
* routing it to \(B\cup\{p,a_t\}\) has load one, but exports only one
  source index;
* there is no old or new one-face output retaining \(B\) and two distinct
  source indices;
* the ordered two-face output
  \((B\cup\{a_s\},B\cup\{a_t\})\) decodes \((s,t)\) with load one, but this
  is precisely the unconverted square-to-linear interface.

At \(q=14\), the exact ledger is

\[
 \#\mathcal F_B(P_{\rm old})=15,\qquad
 \#\mathcal F_B(P_{\rm new})=30,\qquad
 \binom{14}{2}=91\text{ bad two-source unions}.                  \tag{13}
\]

## 5. Canonical Farkas-edge localization: exact gain and exact gap

There is a useful polynomial bridge from the hard fractional-Helly branch
to a common physical edge, but it does not automatically meet the endpoint
dilution threshold.

Let a weighted law of ear contexts have total mass \(W\), and suppose
ordered bad triples have weight at least \(bW^3\). Canonically choose, for
each bad triple, a strict-Farkas certificate with one oriented boundary
inequality from each context. There are at most

\[
                 M^3,\qquad M=2\binom n2=n(n-1),                  \tag{14}
\]

ordered physical edge-and-side triples. If \(H_e\) is the total context
mass whose boundary contains the oriented edge \(e\), then the certificate
mass assigned to \((e_1,e_2,e_3)\) is at most
\(H_{e_1}H_{e_2}H_{e_3}\). Pigeonholing therefore proves

\[
                  \boxed{\max_eH_e\ge {b^{1/3}W\over M}.}         \tag{15}
\]

This is exact and requires no independence after the canonical assignment.
Every context in the resulting fibre shares one literal exposed physical
edge and one side, so the projective normalization in
FIXED_EDGE_CARRIER_ENDPOINT_DILUTION_GATE.md is applicable.

Two losses remain explicit. First, \(H_e\) is context mass, not necessarily
the number of distinct source faces. If one physical source face has
localized history mass at most \(\lambda\), the distinct fixed-edge family
has size at least \(H_e/\lambda\). Second, let \(p_e\) be the size of its
union support and let \(V_e\) be the number of ordinary faces on that
support. The fixed-edge theorem gives only

\[
 {C_eU_e\over V_e}
    \ge {H_e\over\lambda V_e}\binom{p_e}{2}.                      \tag{16}
\]

Writing \(\vartheta=2-\log_2 3\), the exact sufficient condition for the
desired \(p_e^{\log_2 3}\) endpoint surplus is

\[
 {b^{1/3}W\over M\lambda V_e}\ge p_e^{-\vartheta},
 \quad\text{equivalently}\quad
 V_e\le {b^{1/3}W\,p_e^\vartheta\over M\lambda}.                  \tag{17}
\]

The bare localization (15) does not imply (17). With \(M=\Theta(n^2)\),
\(\lambda=1\), \(p_e\asymp n\), and only \(V_e\le W\), it gives density
\(n^{-2}\), whereas (17) needs \(n^{-\vartheta}\). The missing factor is
\(n^{2-\vartheta}=n^{\log_2 3}\), exactly the terminal endpoint target.
Small support or low rank helps only if it also supplies the required
upper bound on \(V_e\); neither property alone changes (17).

The nested cage is an exact planar stress even for perfect edge
localization. All \(q\) contexts already share \(uv\), so \(M_{\rm eff}=1\)
and \(H_{uv}=W=q\). But the labels \(a_1,\ldots,a_q\) are themselves in
convex position, giving

\[
                         V_e\ge2^q-1,\qquad
 {H_{uv}\over V_e}\le {q\over2^q-1}.                            \tag{18}
\]

At \(q=14\), \(14/(2^{14}-1)<1/17\), which is already smaller than
\(17^{-\vartheta}\). Thus even zero edge-localization loss does not splice
to endpoint surplus without a support-face upper bound or an independent
ambient bank charge. In this example that ambient convex-chain bank is
precisely the correct payment; in a live application it must be routed
with its actual decoder.

## 6. Scope

The fixed-carrier hypothesis supplies a genuine positive theorem: the
three-ear Helly/Farkas residue disappears, so no further order-three
chamber classification is needed in this branch. It does **not** by itself
supply a recoverable cyclic or endpoint face bank in the original
configuration. The nested cage shows that one still needs one of:

1. an ordinary detached/source union hypothesis;
2. a bound on common-repair history reuse strong enough to pay the load
   \(q\);
3. a minimizer comparison proving that the simultaneous relocation to
   \(p\) decreases the *total* face count; or
4. a two-face-to-one-face composition theorem using an additional cyclic
   role.

The cage is a scalable applicability barrier, not a global low-face or
least-counterexample construction: the \(a_t\) form a convex parabolic
chain and carry their own large ambient face bank.

## 7. Verification

The exact verifier
verify_fixed_carrier_three_ear_collapse_and_nested_cage.py checks the
nine-point support intersection, then uses rational arithmetic at \(q=14\)
to verify general position in both configurations, all exposed-edge and
repair claims, all 91 nested pair failures, the barycentric identity (10),
the complete ledgers (12), and the stated decoder loads.
