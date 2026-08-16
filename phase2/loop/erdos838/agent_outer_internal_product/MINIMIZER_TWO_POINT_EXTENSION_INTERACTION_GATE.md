# Two-point extension interactions in a global minimizer

**Date:** 2026-08-15. All logarithms are base two and \(V\) counts nonempty
ordinary faces.

## Verdict

There is an exact order-two strengthening of the singleton minimizer
inequality, but positivity of the natural pair interaction does not furnish
an endpoint converter.

Fix \(Q\) and two new positions \(u,v\). Let

\[
\begin{aligned}
 A_Q(u)&=\bigl|\{R\subseteq Q:R\cup\{u\}\text{ is ordinary}\}\bigr|,\\
 J_Q(u,v)&=\bigl|\{R\subseteq Q:R\cup\{u,v\}\text{ is ordinary}\}\bigr|.
\end{aligned}                                                     \tag{1}
\]

The empty base \(R=\varnothing\) is included in both counts. One has the
exact Möbius decomposition

\[
 V(Q+u+v)=V(Q)+A_Q(u)+A_Q(v)+J_Q(u,v),                            \tag{2}
\]

and

\[
 V(Q+u+v)-V(Q+u)-V(Q+v)+V(Q)=J_Q(u,v)\ge0.                       \tag{3}
\]

Thus the absolute pair interaction is always nonnegative, in every
configuration. Its deletion map lands in
\(\overline{\mathcal F}(Q)=\mathcal F(Q)\cup\{\varnothing\}\), so

\[
                              J_Q(u,v)\le V(Q)+1.                 \tag{4}
\]

It is only one more copy of the base-face reservoir. If an interaction
output retains variable supports \(B,C\subseteq Q\), heredity forces
\(B\cup C\) to have been ordinary already.

For a globally minimal \(n\)-point configuration \(P\), put
\(Q=P-\{x,y\}\), \(N=n-2\). Comparing with three explicit two-anchor strong
glues gives

\[
\boxed{
 V(P)-V(Q)\le
 3+\min\{3C(Q),\,3U(Q),\,C(Q)+U(Q)+N\}.}                          \tag{5}
\]

Summing (5) gives exact second-moment cap/cup inequalities, stated in
Theorem 2 below. These are genuinely stronger data than the deletion first
moment, though they do not improve its leading asymptotic scale by
themselves.

The correct simultaneous-relocation interaction is not (3). Relative to
the actual anchors, define

\[
\begin{aligned}
 \Delta_x(u\mid y)
   &=A_Q(u)-A_Q(x)+J_Q(u,y)-J_Q(x,y),\\
 \Delta_y(v\mid x)
   &=A_Q(v)-A_Q(y)+J_Q(x,v)-J_Q(x,y),\\
 K_{x,y}(u,v)
   &=J_Q(u,v)-J_Q(u,y)-J_Q(x,v)+J_Q(x,y).
\end{aligned}                                                     \tag{6}
\]

Then the exact discrete-Hessian identity is

\[
 \Delta_{xy}(u,v)
   =\Delta_x(u\mid y)+\Delta_y(v\mid x)+K_{x,y}(u,v).              \tag{7}
\]

Separate self-minimality gives the first two terms nonnegative. A two-point
mutation decreases \(V\) precisely when

\[
          K_{x,y}(u,v)<
              -\Delta_x(u\mid y)-\Delta_y(v\mid x).               \tag{8}
\]

The mixed interaction \(K\) has both signs even on the true five-point and
exact nine-point minimizers. On the tested rational chambers the nine-point
minimizer has

\[
                         -25\le K\le47,                           \tag{9}
\]

yet every tested simultaneous move has nonnegative total change. The
negative interaction is absorbed by the separate extension costs. The
balanced twelve-point Pascal wrapper instead has simultaneous changes as
low as \(-313\), and violates (5) for every pair; order-two minimality
rejects it rather than converting its endpoint rectangle.

There is one further exact anti-alignment. Let
\[
 a_Q=\min_u A_Q(u)
\]
over one-point extension cells, and let \(J_Q^{\min}\) be the minimum of
\(J_Q(u,v)\) over joint general-position positions with
\(A_Q(u)=A_Q(v)=a_Q\). Global minimality gives

\[
 [A_Q(x)-a_Q]+[A_Q(y)-a_Q]+J_Q(x,y)\le J_Q^{\min}.                \tag{10}
\]

Thus a minimizer suppresses pair interaction relative to two independent
minimum cells. If the actual anchors are themselves \(Q\)-minimum
extensions, they minimize \(J_Q\) among those cells. This is again the
opposite sign from a converter theorem.

The surviving geometric target is precise: use circuit structure to show
that a heavy marked endpoint rectangle forces either an already-ordinary
base-support union, or a candidate pair move satisfying (8). Neither
absolute positivity (3), the scalar moment bounds, nor separate
self-minimality supplies that implication.

## 1. Coefficientwise Möbius decomposition

Define

\[
\begin{aligned}
 L_Q(u;z)&=\sum_{\substack{R\subseteq Q\\
                R\cup\{u\}\text{ ordinary}}}z^{|R|},\\
 I_Q(u,v;z)&=\sum_{\substack{R\subseteq Q\\
                R\cup\{u,v\}\text{ ordinary}}}z^{|R|}.
\end{aligned}                                                     \tag{11}
\]

The four possible anchor masks give

\[
 \Phi_{Q+u+v}(z)=\Phi_Q(z)+zL_Q(u;z)+zL_Q(v;z)+z^2I_Q(u,v;z),     \tag{12}
\]

where \(\Phi_Q\) includes the empty face. Hence

\[
 \Phi_{Q+u+v}-\Phi_{Q+u}-\Phi_{Q+v}+\Phi_Q
                         =z^2I_Q(u,v;z)                           \tag{13}
\]

coefficientwise. Setting \(z=1\) proves (2)--(3).

The map

\[
              R\cup\{u,v\}\longmapsto R                          \tag{14}
\]

injects the interaction family into
\(\overline{\mathcal F}(Q)\), proving (4). More importantly, if
\(B\cup C\subseteq R\), then \(B\cup C\) is ordinary by heredity. Pair
interaction cannot turn a bad unchanged support union into a face.

## 2. Three canonical pair mutations

Let \(E\) be the unique two-point order type. Its nonempty face, cap, and
cup counts are all three:

\[
                              V(E)=C(E)=U(E)=3.                   \tag{15}
\]

There are three relevant strong-glue configurations:

\[
                              Q\prec E,\qquad
                              E\prec Q,\qquad
                              \{u\}\prec Q\prec\{v\}.              \tag{16}
\]

The exact strong-glue recurrences give

\[
\begin{aligned}
 V(Q\prec E)-V(Q)&=3+3C(Q),\\
 V(E\prec Q)-V(Q)&=3+3U(Q),\\
 V(\{u\}\prec Q\prec\{v\})-V(Q)
                 &=3+C(Q)+U(Q)+N.
\end{aligned}                                                     \tag{17}
\]

If \(P\) is globally \(V\)-minimal at size \(n=N+2\), replace \(x,y\) by
each realization in (16). The base faces of \(Q\) are unchanged, so taking
the least right side in (17) proves (5).

The mixed placement in (17) may also be read from (2):
the two separate extension terms are \(1+C(Q)\) and \(1+U(Q)\), while the
two-anchor interaction is exactly \(N+1\). It contains only the empty and
singleton base traces.

## 3. The order-two deletion moments

For a face \(F\) of rank \(r\), the number of label pairs meeting \(F\) is

\[
             w_2(r)={n\choose2}-{n-r\choose2}.                    \tag{18}
\]

Therefore

\[
 \sum_{\{x,y\}}\{V(P)-V(P-\{x,y\})\}
             =\sum_{F\in\mathcal F(P)}w_2(|F|).                   \tag{19}
\]

For the endpoint complexes,

\[
\begin{aligned}
 \sum_{\{x,y\}}C(P-\{x,y\})
     &=\sum_{A\in\mathcal C(P)}{n-|A|\choose2},\\
 \sum_{\{x,y\}}U(P-\{x,y\})
     &=\sum_{B\in\mathcal U(P)}{n-|B|\choose2}.
\end{aligned}                                                     \tag{20}
\]

> **Theorem 2 (second-moment minimizer inequalities).** Every globally
> minimal \(P\) satisfies
> \[
> \begin{aligned}
> \sum_Fw_2(|F|)
>   &\le3{n\choose2}
>       +3\sum_{A\in\mathcal C(P)}{n-|A|\choose2},\\
> \sum_Fw_2(|F|)
>   &\le3{n\choose2}
>       +3\sum_{B\in\mathcal U(P)}{n-|B|\choose2},                 \tag{21}\\
> \sum_Fw_2(|F|)
>   &\le(n+1){n\choose2}
>       +\sum_{A\in\mathcal C(P)}{n-|A|\choose2}
>       +\sum_{B\in\mathcal U(P)}{n-|B|\choose2}.
> \end{aligned}
> \]

**Proof.** Sum each of the three branches of (5) separately and apply
(19)--(20). \(\square\)

These identities retain the second rank moments discarded by the singleton
bound. Dropping them gives only constant-factor variants of the first-moment
endpoint lower bound. A coefficient improvement requires correlation between
the ranks and the actual two-point circuit interactions.

## 4. Separate minima and the mixed Hessian

Global minimality with \(y\) fixed gives

\[
       A_Q(x)+J_Q(x,y)\le A_Q(u)+J_Q(u,y),                         \tag{22}
\]

so \(\Delta_x(u\mid y)\ge0\). The analogous inequality holds for \(y\).
Simultaneous relocation gives

\[
 A_Q(x)+A_Q(y)+J_Q(x,y)
       \le A_Q(u)+A_Q(v)+J_Q(u,v).                                \tag{23}
\]

Subtracting the two one-coordinate changes proves (7). Equation (8) is
therefore necessary and sufficient for the displayed pair mutation to
decrease the face count.

To prove (10), choose \(u,v\) among the individual minimum cells so that
\(J_Q(u,v)=J_Q^{\min}\), and apply (23). The two excess terms are
nonnegative by the definition of \(a_Q\).

Notice the direction: (10) upper-bounds the actual interaction. A large
interaction available after separately minimizing the anchors is allowed to
be hidden by their actual joint placement.

## 5. Exact finite audits

### 5.1 Five points

The rational five-point minimizer from
MINIMIZER_SINGLETON_ENDPOINT_SURPLUS_GATE.md has \(V=26\). Every pair
saturates (5): the minimum canonical mutation has the same 26 faces.
Nevertheless the sampled exact relocation Hessians range from \(-7\) to
\(5\). Thus mixed-Hessian nonnegativity already fails at the first
nontrivial global minimizer.

### 5.2 Nine points

The exact rational database minimizer has nonempty profile

\[
                         (v_1,v_2,v_3,v_4,v_5)
                              =(9,36,84,36,3)                     \tag{24}
\]

and \(V=168\). Across its 36 pair deletions, the slack in (5) ranges from
11 to 20. The verifier tests rational exterior cells for every pair. The
mixed Hessian has both signs as in (9), every separate change is
nonnegative, and every simultaneous change is nonnegative. Negative
interaction alone does not overcome the first-order cell costs.

The assertion that this order type is globally minimal uses the documented
exhaustive realizable-order-type database certificate already stored in
agent_lex_minimizer_search/exact_realizable_n9.json.

### 5.3 Balanced Pascal wrapper

For \(P=T(4,2)\prec T(4,2)\),

\[
                              (C,U,V)=(248,248,1061).              \tag{25}
\]

Every one of its 66 pair deletions violates (5); the violation ranges from
261 to 367 faces. Sampled simultaneous relocations decrease \(V\) by as
much as 313. Hence this exact endpoint-rectangle barrier is decisively
nonminimal already at order two. It cannot calibrate a theorem which uses
(5), but it remains a valid barrier to arguments using only local endpoint
capacity.

## 6. Scope

The order-two attack proves:

* the coefficientwise two-anchor Möbius identity;
* the exact three-branch pair-deletion minimizer inequality;
* three second-rank-moment endpoint inequalities;
* the precise negative-Hessian threshold for a decreasing pair mutation;
* pair-interaction anti-alignment relative to independent minimum cells; and
* exact \(n=5,n=9\), and Pascal audits.

It does not prove that a heavy bad endpoint rectangle makes (8) hold.
Absolute interaction positivity is tautological and bounded by the same base
face reservoir. The missing planar theorem must correlate negative
four-circuit interactions across the two endpoint anchors strongly enough
to dominate their separate relocation costs.

## 7. Verification

The verifier verify_minimizer_two_point_extension_interaction_gate.py
uses exact rational arithmetic. It exhausts all faces, caps, cups, and pair
deletions of the \(n=5,n=9,n=12\) configurations. It checks (2)--(8),
(18)--(21), the exact finite profiles, and deterministic rational relocation
cells. It reports both signs of \(K\) on the two genuine minimizers and the
decreasing pair mutations in the Pascal wrapper.
