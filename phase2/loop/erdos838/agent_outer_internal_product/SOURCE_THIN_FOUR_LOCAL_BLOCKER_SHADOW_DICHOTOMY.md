# Source-thin rooted downsets: four-local blocker/shadow dichotomy

## Verdict

For one selected ordinary source word \(W\) and one ordinary rooted seam
\(Y\), planar four-locality gives an exact combinatorial model. The rooted
compatibility downset

\[
 \mathcal D(Y,W)=\{S\subseteq W:Y\cup S\text{ is ordinary}\}      \tag{1}
\]

is the independence complex of a hypergraph of cross-circuit traces of rank
at most three.

This has two sharp consequences.

1. True codimension-one compatibility is rigid: either \(Y\cup W\) is
   ordinary and all \(q=|W|\) one-label omissions work, or at most three
   work.
2. The useful graded replacement is a minimum-cover versus disjoint-blocker
   matching dichotomy. If \(\tau_r\) is the minimum trace-cover size and
   \(\nu_r\) the maximum disjoint-blocker matching size for record \(r\),
   then
   \[
                         \nu_r\le\tau_r\le3\nu_r.          \tag{2}
   \]

Deleting a canonical minimum cover and one extra tag gives
\(q-\tau_r\) seam-retaining ordinary shadows. Alternatively, a canonical
root label from each disjoint blocker gives \(\nu_r\) source-retaining
codimension-one shadows. For weighted record mass \(W_0\), their incidence
masses \(I_C,I_B\) satisfy

\[
                         I_C+3I_B\ge qW_0.               \tag{3}
\]

Thus one of the two physical banks has linear incidence mass. The remaining
issue is exactly its decoder load. The cover bank can omit \(\tau_r+1\)
role labels, while the blocker bank omits only one label but forgets the
rooted seam/history.

The anti-aligned two-arc construction is a sharp stretchable load barrier:
its trace hypergraph is \(K_{k,k}\), so \(q=2k\) and
\(\tau=\nu=k\). With role alphabet \(D\), the two certified banks have only
\(Mk/D\) and \(Mk/D^{k+1}\) distinct outputs. Hence (3) cannot be converted
to an \(Mq\) one-face bank without controlling physical completion degree or
source-history load.

This is an exact positive dichotomy and an exact applicability barrier, not
an unconditional half-coefficient closure.

## 1. Four-local circuit-trace representation

Let the selected word be

\[
                 W_r=\{x_{r,1},\ldots,x_{r,q}\},         \tag{4}
\]

with one point in each of \(q\) disjoint role colours. Assume the role
ground is disjoint from the seam and source-base ground, so an output's
occupancy mask distinguishes word labels from retained anchors. Assume both
\(W_r\) and the literal rooted seam \(Y_r\) are ordinary. A set of planar
general-position points is ordinary if and only if each of its four-point
subsets is ordinary: if one point is hidden, planar Carathéodory supplies a
triangle hiding it.

Define \(\mathcal H_r\) to be the inclusion-minimal nonempty role traces
\(T\subseteq[q]\) for which some four-point nonordinary subset of
\(Y_r\cup W_r\) has word-side trace
\(\{x_{r,i}:i\in T\}\). No bad four-set lies wholly in \(Y_r\) or wholly in
\(W_r\). Therefore

\[
                              1\le |T|\le3.              \tag{5}
\]

Four-locality gives the exact identity

\[
 S\in\mathcal D_r
   \quad\Longleftrightarrow\quad
 T\nsubseteq S\text{ for every }T\in\mathcal H_r.       \tag{6}
\]

Thus \(\mathcal D_r\) is precisely the independence complex of the
rank-three hypergraph \(\mathcal H_r\).

## 2. Codimension-one rigidity

Let

\[
 A_r=\{i\in[q]:W_r\setminus\{x_{r,i}\}\in\mathcal D_r\}. \tag{7}
\]

By (6), \(i\in A_r\) exactly when \(i\) meets every edge of
\(\mathcal H_r\). Hence

\[
 A_r=
 \begin{cases}
 [q],&\mathcal H_r=\varnothing,\\
 \displaystyle\bigcap_{T\in\mathcal H_r}T,
       &\mathcal H_r\ne\varnothing.
 \end{cases}                                                  \tag{8}
\]

Every edge has rank at most three, proving:

> **Theorem 1 (all or at most three).** For every record,
> \[
>             |A_r|=q\quad\text{or}\quad |A_r|\le3.      \tag{9}
> \]

So there is no gradual theorem producing \(\Theta(q)\) genuine
codimension-one seam-compatible shadows from a nonempty circuit family.
The full-compatible branch in
THIRD_CYCLIC_MERGED_DOWNFACE_HISTORY_LOAD_GATE.md is exactly the first case
of (9).

## 3. Canonical cover and first-blocker banks

Let \(J_r\) be the lexicographically first minimum vertex cover of
\(\mathcal H_r\), with \(|J_r|=\tau_r\). Let
\(\mathcal M_r\) be the lexicographically first maximum matching, with
\(|\mathcal M_r|=\nu_r\). A maximal matching has a union of at most
\(3\nu_r\) vertices meeting every edge, while every cover meets every
matching edge. This proves (2).

There are two literal ordinary outputs.

### Cover-tag output

For every \(i\notin J_r\), put

\[
 C(r,i)=Y_r\cup
 \bigl(W_r\setminus\{x_{r,j}:j\in J_r\cup\{i\}\}\bigr). \tag{10}
\]

The set \(J_r\) meets every bad trace, so (6) makes (10) ordinary. It
retains the seam and all but \(\tau_r+1\) word labels. There are exactly
\(q-\tau_r\) tagged incidences for record \(r\).

### First-blocker source output

Let \(X_r=A_r^0\cup W_r\) be the actual ordinary source face, where the
role-free source base \(A_r^0\) is retained literally. For every
\(T\in\mathcal M_r\), choose its first role
\(\rho(T)=\min T\), and put

\[
                         B(r,T)=X_r\setminus\{x_{r,\rho(T)}\}.
                                                               \tag{11}
\]

This is ordinary by source heredity. Matching edges are disjoint, so their
first roles are distinct; the missing role in (11) identifies which
blocker was selected once the completed record is known. Crucially, (11)
deletes only one physical label, not the whole circuit trace. There are
exactly \(\nu_r\) such incidences.

For nonnegative record weights \(w_r\), define

\[
 \begin{aligned}
 W_0&=\sum_rw_r,\\
 I_C&=\sum_rw_r(q-\tau_r),\\
 I_B&=\sum_rw_r\nu_r.
 \end{aligned}                                                \tag{12}
\]

Equation (2) gives the global identity

\[
 I_C+3I_B
   =\sum_rw_r(q-\tau_r+3\nu_r)
   \ge qW_0.                                                   \tag{13}
\]

Let \(\Delta_C,\Delta_B\) be the actual weighted output loads of (10) and
(11). Then

\[
 I_C\le\Delta_CV(P),\qquad I_B\le\Delta_BV(P).          \tag{14}
\]

In particular, either

\[
 V(P)\ge {qW_0\over2\Delta_C}
 \quad\text{or}\quad
 V(P)\ge {qW_0\over6\Delta_B}.                         \tag{15}
\]

This is the exact weighted cover-or-blocker theorem.

## 4. Literal completion-load bounds

Suppose role \(i\) has physical alphabet size \(d_i\), and write
\(d=\max_i d_i\). Assume:

* the total weight of records with one fixed completed source face \(X_r\)
  is at most \(\Lambda_X\); and
* the total weight of records with one fixed literal completed pair
  \((Y_r,W_r)\) is at most \(\Lambda_Y\). Here the seam is fixed or
  recovered from its disjoint anchor colours; any additional seam decoder
  ambiguity must be included in \(\Lambda_Y\).

Role colours expose the deleted-role mask. Completing (11) requires only
one missing role label, so

\[
                         \Delta_B\le\Lambda_X d.         \tag{16}
\]

For (10), the deleted mask is \(J_r\cup\{i\}\). After a completed pair is
fixed, the canonical cover fixes the tag uniquely. Therefore

\[
 \Delta_C\le\Lambda_Y
   \max_{r,\ i\notin J_r}
          \prod_{j\in J_r\cup\{i\}}d_j.                \tag{17}
\]

The role-completion product in (17) is unavoidable.

For a threshold \(t\), let \(W_{\le t}\) and \(W_{>t}\) be the weighted
masses with \(\tau_r\le t\) and \(\tau_r>t\). Restricting the two banks
gives

\[
 \begin{aligned}
 V(P)&\ge{(q-t)W_{\le t}\over\Lambda_Yd^{t+1}},\\
 V(P)&\ge{(t+1)W_{>t}\over3\Lambda_Xd}.
 \end{aligned}                                                \tag{18}
\]

The first output retains at least \(q-t-1\) word labels and is genuinely
almost full when \(t=o(q)\). The second retains all but one source label
and carries \(t/3\) disjoint first-blocker choices. Equation (18) displays
the exact residual: intermediate cover entropy can cancel the tag factor,
while large physical alphabet or source-history load can cancel the
blocker factor.

## 5. Regression audits

### Maximum-child prefix

For the pure prefix downset \(\mathcal D=2^{[k]}\),

\[
 \mathcal H=\{\{i\}:k<i\le q\},\qquad
 \tau=\nu=q-k.                                          \tag{19}
\]

The cover bank deletes the whole tail and one prefix tag. The blocker bank
deletes one tail label from the ordinary source. This is exactly the old
prefix/history split: a tail role of branching \(D\) contributes
\((q-k)/D\), not \(q-k\), unless its completion degree is controlled.

### Anti-aligned two-arc rectangle

In the rational two-arc construction of
ALMOST_FULL_WORD_MIXED_BANK_BARRIER.md, take the rooted seam to be the
central pair \(\{o,p\}\). For one selected six-role word the verifier finds

\[
 \mathcal D
 =\{S:S\text{ lies wholly on one arc}\},\qquad
 \mathcal H=K_{3,3},\qquad \tau=\nu=3.                  \tag{20}
\]

For the complete four-label role product \(M=4^6\), exact loads are

\[
 \begin{array}{c|r|r|r}
 \text{bank}&\text{incidences}&\text{outputs}&\text{load}\\ \hline
 \text{first blocker}&12{,}288&3{,}072&4\\
 \text{cover plus tag}&12{,}288&48&256.
 \end{array}                                             \tag{21}
\]

Generally, for \(q=2k\) roles of alphabet \(D\), these two certified banks
have scales \(Mk/D\) and \(Mk/D^{k+1}\). When \(D\gg q\), neither supplies
an \(Mq\) output count. This stretchable example saturates both load terms
in (16)--(17); planarity does not improve the abstract dichotomy.

### Pascal all-delete terminal

At the central Pascal seam, a fixed noncap triple together with any one
released label is bad. After role colouring, the model is

\[
                    \mathcal H=\{\{1\},\ldots,\{q\}\},
                    \qquad\tau=\nu=q.                   \tag{22}
\]

The cover bank is terminal and retains no word label. The blocker bank has
\(q\) first-label incidences, but its physical completion degree is the
prefix branching/codegree; the exact Pascal DAG regression shows that this
can absorb the incidence gain. Thus Pascal tests \(\Delta_B\), not (13).

### Nested cage

The nested-carrier cage has only one physical blocker label in the rooted
word; its \(q\)-fold variation is external context history, not role rank.
Accordingly the theorem sees \(\nu=1\) and history load of order \(q\).
The separate convex chain of context labels is the ambient bank which pays
that example. This confirms that \(\Lambda_X\) cannot be omitted from (16).

## 6. Scope of the positive splice

The source-thin branch is paid whenever one of the following holds on the
relevant weighted slice:

1. \(\tau_r=o(q)\) and the cover-completion product in (17) is subpower at
   the required scale; or
2. \(\tau_r=\Omega(q)\), the blocker roles have bounded completion degree,
   and the actual-source history load \(\Lambda_X\) is controlled.

For three independently role-coloured components, three controlled
first-blocker source shadows can be combined by deleting one role in each
component from a common ordinary source face, giving the same
codimension-three constant-load mechanism as the corrected cyclic theorem.
This requires the three component words to lie in one literal source face;
the present one-component theorem does not manufacture that compatibility.

The remaining gate is precise: intermediate cover entropy with a large
completion product, or a large actual-source history load. A bare
first-missing-label count cannot remove either, as (20)--(22) show.

## 7. Verification

Run:

    python3 agent_outer_internal_product/verify_source_thin_four_local_blocker_shadow_dichotomy.py

The verifier:

1. exhausts all 166 rank-at-most-three antichains on four roles;
2. checks (6), (8), minimum covers, maximum matchings, and (13);
3. checks every prefix/all-delete model through ten roles;
4. reconstructs the rational anti-aligned \(K_{3,3}\) downset exactly;
5. enumerates all \(4^6\) words and verifies both load rows in (21); and
6. checks (13) on a nonuniform weighted family.

It prints PASS.
