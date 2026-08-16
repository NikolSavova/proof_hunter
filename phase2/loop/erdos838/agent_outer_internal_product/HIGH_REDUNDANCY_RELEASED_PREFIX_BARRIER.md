# High conditional redundancy does not give a released-prefix support bank

**Date:** 2026-08-15.  All logarithms are base two and the empty face is
counted unless explicitly removed.

## Verdict

The high-redundancy residue in the weighted release identity has two
additional splits which are essential before applying an ambient support
bank.  For a fixed visible deletion mask \(J\),

\[
 \boxed{\quad
 \mathbb E(R_U\mid J)
   =\bigl(\log|\Omega_J|-H(D\mid J)\bigr)
      +I(D;U\mid J).\quad}                              \tag{1}
\]

Thus conditional redundancy can be information already carried by the
released output.  Moreover, if \(Z_{J,i}\) is the actual support of the
\(i\)-th deleted coordinate in this mask class and
\(P_J=\prod_{i\in J}|Z_{J,i}|\), then

\[
 \log|\Omega_J|-H(D\mid J)
 =\log{|\Omega_J|\over P_J}
   +\bigl(\log P_J-H(D\mid J)\bigr).                   \tag{2}
\]

Only the last term in (2) is intrinsic correlation redundancy on the
actual completion support.  The first is unused global-alphabet slack.
Consequently \(R_U\) in WEIGHTED_POSITION_RELEASE_ENTROPY.md is not,
without further hypotheses, literally the selected-family \(R\) in
HIGH_REDUNDANCY_SUPPORT_BANK.md.  The weighted full-alphabet support
Cauchy theorem remains valid for all of \(R_U\); what fails is retaining
\(F\), or interpreting an overloaded global support label as a label
which occurs in the particular fibre.

There is an exact weighted ambient discharge for the intrinsic term.  In
one fixed output fibre \(u=(B,F,J)\), let the distinct completions have
weights at most one, total weight \(m_u\), coordinate supports \(Y_i\),

\[
 P_u=\prod_{i\in J}|Y_i|,\qquad
 T_u=\log P_u-H(D\mid U=u),\qquad
 N_u=\left|\bigcup_{i\in J}Y_i\right|.                 \tag{3}
\]

Then

\[
 \boxed{\quad
 {V(P)\over m_u}\ge {f(N_u)2^{T_u}\over P_u}.
 \quad}                                                \tag{4}
\]

This bank is **unprefixed**: it consists of ordinary faces of the induced
support union.  No analogous theorem retaining the released face \(F\) is
possible.  A scalable rational two-cloud construction below has

\[
       T_u=(r-1)\log d=\Theta(r^2)                     \tag{5}
\]

but

\[
 \boxed{\quad
 \{F\cup S:S\subseteq\text{completion support},
                 F\cup S\text{ ordinary}\}=\{F\}.
 \quad}                                                \tag{6}
\]

Even the source-retaining selected downshadow has only

\[
                         1+d(2^r-1)                    \tag{7}
\]

faces, independent of the much larger redundancy factor \(d^{r-1}\).
Replicating the fibre over \(H\) released faces produces the complete
\(d\) by \(H\) source--released-face core, with exact Hall density

\[
                         {dH\over d+H}.                 \tag{8}
\]

This is precisely the dense face--face residue in
RELEASED_FACE_HALL_LABEL_PRIMITIVE_GATE.md.  The construction exposes two
detached Boolean cloud banks and is therefore not a low-face
counterexample.  It proves that high \(R_U\) cannot be closed by a local
ambient/downshadow bank which retains \((B,F,J)\), nor by treating the
unprefixed support bank as a private copy for every released face.

## 1. The exact redundancy decomposition

In one mask class, \(\Omega_J\) is deterministic and \(J\) is visible in
\(U\).  By the definition

\[
                         R_u=\log|\Omega_J|-H(D\mid U=u),          \tag{9}
\]

averaging and using
\(H(D\mid J)-H(D\mid U,J)=I(D;U\mid J)\) proves (1).  Splitting the first
term at the product of the actual marginal supports proves (2).

There is also a pointwise version.  Put

\[
 Y_{u,i}=\{d_i:\Pr(D=d\mid U=u)>0\},\qquad
 P_u=\prod_i|Y_{u,i}|.                                \tag{10}
\]

Then exactly

\[
 R_u=\underbrace{\log{|\Omega_J|\over P_u}}_{\text{conditional support deficit}}
       +\underbrace{\bigl(\log P_u-H(D\mid U=u)\bigr)}_{\text{intrinsic correlation}}.
                                                               \tag{11}
\]

A deterministic completion over \(u\) can therefore have the maximum
first term even though there is no local completion family to multiply.
If different deterministic completions have different released outputs,
the corresponding part of the average is recorded by the
mutual-information term in (1).

This decomposition does not retract the exact full-alphabet estimate in
HIGH_REDUNDANCY_RELEASE_HALL_BARRIER.md.  Directly from (9) and (12),

\[
                         m_u\le|\Omega_J|\,2^{-R_u}.    \tag{11a}
\]

Together with the induced face bank on
\(\bigcup_{i\in J}X_i\), this gives the support-reservoir Cauchy/rank-tax
bound there even when some global labels are unused over \(u\).  The
distinction matters only at the next decoder step: such an unused label
does not certify that \(B\cup\{x\}\) is a source subface for this \(u\).

For (4), write the unnormalised completion weights as \(0<w_d\le1\) and
\(m_u=\sum_dw_d\).  Under the conditional law, every atom has probability
at most \(1/m_u\).  Hence

\[
             H(D\mid U=u)\ge\log m_u                  \tag{12}
\]

(when \(m_u<1\) the right side is negative and the statement is
automatic).  Thus \(m_u\le2^H=P_u\,2^{-T_u}\).  Every completion \(D\) is a
subface of the ordinary source \(B\cup D\), so it is ordinary.  The whole
induced support has at least \(f(N_u)\) ordinary faces.  Dividing this
bank by the preceding bound on \(m_u\) proves (4).  Notice that neither
the proof nor its output contains \(F\).

## 2. A stretchable quadratic-redundancy prefix barrier

Use two small, lexicographically composed rational clouds \(Y,Z\).  Choose
their charts as opposite pure parabolic chains and their composition
directions so that the two facing profiles are

\[
       \{S\ne\varnothing:|S|\le2\}.                   \tag{13}
\]

Equivalently, every subset of one cloud is ordinary, while a subset
meeting both clouds is ordinary exactly when both nonempty cloud traces
have rank at most two.  This is the anti-aligned case of the exact
two-block recurrence in DENSE_HALL_TWO_CLOUD_PROFILE_BARRIER.md.  The
realization is rational and scalable: shrink \((j,j^2)\) into a small
neighbourhood of \((1/100,50099/10000)\) and \((j,-j^2)\) into a small
neighbourhood of \((0,-4)\).  All required strict signs persist for
sufficiently small rational scale.

Let \(|Y|=rd\) and partition its cyclic order into \(r\) consecutive role
supports

\[
                         X_i=\{y_{i,a}:a\in[d]\}.       \tag{14}
\]

For every \(a\in[d]\), take the diagonal completion

\[
                         D_a=\{y_{i,a}:i\in[r]\}.       \tag{15}
\]

The \(D_a\) are pairwise disjoint ordinary rank-\(r\) faces and every role
support has size \(d\).  Let \(F\) be any fixed rank-\(s\) face of \(Z\),
where \(s\ge3\), and take

\[
                  B=\varnothing,\qquad J=[r],\qquad U=F.          \tag{16}
\]

Each source \(A_a=D_a\) is ordinary, as is \(U\).  By (13), however,

\[
                         F\cup S\text{ is nonordinary}            \tag{17}
\]

for every nonempty \(S\subseteq Y\).  Thus deleting all of \(A_a\) is the
unique minimum-cardinality release, and (6) follows.  The visible empty
role set recovers \(J\) exactly.

This cannot be repaired by adjoining further ambient labels.  Convex
position is hereditary, so every superset of the nonordinary subset
\(F\cup S\) is also nonordinary.  Hence no ordinary face of the full
configuration contains both all of \(F\) and even one label of \(Y\).

Give the \(d\) completions equal weight.  Their conditional entropy is
\(\log d\), whereas \(|\Omega_U|=d^r\), so

\[
                  R_U=r\log d-\log d=(r-1)\log d.      \tag{18}
\]

Here every conditional role support is the full \(X_i\), so all of (18)
is intrinsic correlation, not alphabet slack.  Taking
\(r=\Theta(\log d)\) makes it quadratic in \(r\).

The weighted release identity is exact term by term.  If \(\mathcal H\)
is any family of \(H\) rank-\(s\) faces of \(Z\) and records are all pairs
\((D_a,F)\), then

\[
\begin{aligned}
 \sigma&=r\log d,\\
 H(A,F)&=\log d+\log H,\\
 H(U)&=\log H,\\
 \mathbb E R_U&=(r-1)\log d.
\end{aligned}                                          \tag{19}
\]

Therefore \(\sigma=H(A,F)-H(U)+\mathbb E R_U\) exactly.

The selected source downsets cannot pay (18).  Since the diagonal words
are disjoint, their union is

\[
 \left|\bigcup_{a=1}^d2^{D_a}\right|
      =1+d(2^r-1),                                    \tag{20}
\]

proving (7).  The full unprefixed support union is much larger—because
\(Y\) is convex, it has \(2^{rd}\) faces—but every one of its nonempty
members is incompatible with the retained \(F\).

## 3. Exact global Hall interface

Take \(\mathcal H={Z\choose s}\), \(H={|Z|\choose s}\).  The release
records form a complete bipartite graph between the \(d\) actual source
faces \(D_a\) and the \(H\) actual released faces \(F\).  For a
subrectangle using \(a\) rows and \(h\) columns, its record/target ratio is
at most

\[
                              {ah\over a+h}.            \tag{21}
\]

This is increasing in both variables, so the fractional Hall density is
exactly (8).  Every ordered pair \((D_a,F)\) has load one.  Fixing \(F\)
leaves all \(d\) source-face neighbours, while the only output retaining
that \(F\) and any part of the completion support is \(F\) itself.  Thus
the prefix-preserving load is exactly \(d\).

Allowing every nonempty selected source downface as a second target gives
the exact complete-tensor Hall ratio

\[
                 {dH\over d(2^r-1)+H}.                \tag{22}
\]

Indeed a subrectangle with \(a\) rows and \(h\) columns sees
\(a(2^r-1)+h\) distinct nonempty targets, and the ratio is again
increasing in \(a,h\).  In particular (22) tends to \(d\) when
\(H\gg d2^r\); the selected downshadow does not discharge the completion
redundancy.

If instead all records may use the single detached ambient bank
\(2^Y-\{\varnothing\}\), the exact Hall ratio is

\[
                 {dH\over (2^{rd}-1)+H}.               \tag{23}
\]

This is the correct global use of the support bank: one merged bank, not
one copy for each \(F\).  It can still have load close to \(d\) when the
released family is larger than the bank.  In this particular realization
the other cloud has the Boolean bank \(2^Z\), which pays that regime.
This is why the example is a retained-prefix and consolidation barrier
rather than an EIC counterexample.

Equations (21)--(23) connect the high-\(R_U\) residue directly to the
dense face--face Hall core.  A valid positive theorem must do at least one
of the following:

1. globally route the unprefixed support unions with their true merged
   overlap;
2. exploit an external detached bank, as \(2^Z\) does here; or
3. add a geometric compatibility/history hypothesis which makes a
   nontrivial part of the support coexist with \(B\cup F\).

High conditional redundancy and source facehood alone imply none of the
three.

## 4. The strongest exact intrinsic-support reduction

Although a released-prefix bank is false, congestion of the unprefixed
ambient banks has an exact physical-label witness.  This gives a direct
general interface to the released-face Hall core.

Let \(c\) range over release contexts, with demand \(d_c\), released face
\(U_c=B_c\cup F_c\), and **actual conditional** completion-support union

\[
 Q_c^{\rm act}=\bigcup_{i\in J}
       \{d_i:\Pr(D=d\mid U=u_c)>0\}.                   \tag{23a}
\]

Put

\[
 \mathcal K_c=\mathcal F(P\mid Q_c^{\rm act})-\{\varnothing\},
 \qquad k_c=|\mathcal K_c|.                            \tag{24}
\]

Route \(d_c\) uniformly over \(\mathcal K_c\).  If \(S\in\mathcal K_c\)
and \(x\in S\), heredity gives

\[
             \{c:S\in\mathcal K_c\}
                 \subseteq\{c:\{x\}\in\mathcal K_c\}. \tag{25}
\]

Therefore this explicit routing has maximum raw output load at most

\[
 \boxed{\quad
 \Lambda_{\rm supp}\le
   \max_x\sum_{c:x\in Q_c^{\rm act}}{d_c\over k_c}.
 \quad}                                                \tag{26}
\]

This is the raw-count analogue of the half-capacity singleton theorem in
GLOBAL_SUPPORT_UNION_HALL_CONSOLIDATION.md.  It uses one global face
budget: repeated support unions contribute repeatedly to the right side
of (26), rather than receiving private copies of their bank.

For the literal fixed-output completion fibres, take \(d_c=m_c\) and use
the intrinsic redundancy notation (3).  Equations (12) and (24) give the
fully explicit bound

\[
 \boxed{\quad
 \Lambda_{\rm supp}\le
 \max_x\sum_{c:x\in Q_c^{\rm act}}
 {P_c\,2^{-T_c}\over f(N_c)-1}.
 \quad}                                                \tag{26a}
\]

Here the subtraction removes the empty face, so (26a) is used only for
nonempty support unions.  Thus intrinsic high redundancy really does
lower the global support load unless many completion supports share one
physical label.  Neither the alphabet-slack nor the output-information
terms in (1)--(2) enter (26a), which is the precise correction to applying
the unweighted support theorem directly to \(R_U\).

Fix a maximizing physical label \(x\).  For every incident context choose
one actual completion \(D\) containing \(x\).  Since \(B_c\cup D\) is an
ordinary source, its subface

\[
                         E_{c,x}=B_c\cup\{x\}           \tag{27}
\]

is ordinary.  The other target \(U_c=B_c\cup F_c\) is ordinary by release.
Apply the exact two-target fractional Hall theorem to the context weights

\[
                         a_c={d_c\over k_c}.            \tag{28}
\]

Writing \(C_x=\{c:x\in Q_c^{\rm act}\}\) and

\[
 \eta_x=\max_{\varnothing\ne C'\subseteq C_x}
 { \sum_{c\in C'}a_c\over
   |\bigcup_{c\in C'}\{E_{c,x},U_c\}|},                \tag{29}
\]

one obtains

\[
                  \sum_{c:x\in Q_c^{\rm act}}{d_c\over k_c}
                              \le\eta_x V(P).           \tag{30}
\]

If \(\eta_x\) is small, (30) pays the singleton overload globally.  If it
is large, weighted pruning gives a nonempty dense bipartite core of actual
source subfaces \(E_{c,x}\) and released faces \(U_c\), all carrying the
same physical completion label \(x\).

In the marked release setting the source roles and the pocket are
disjoint, while \(J\) is visible from the empty source roles.  Hence the
ordered pair \((E_{c,x},U_c)\) recovers

\[
 B_c=E_{c,x}\cap U_c,\qquad
 x=E_{c,x}\setminus B_c,\qquad
 F_c=U_c\setminus B_c,\qquad J.                       \tag{31}
\]

After coalescing identical geometric records, any remaining pair load is
exactly the already-recorded source-internal description load.  Thus no
new support-union overlap variable remains: the high branch of (26) is a
fixed-physical-label instance of the dense face--face core in
RELEASED_FACE_HALL_LABEL_PRIMITIVE_GATE.md.

This reduction is not a solution of that core.  In particular, (30) does
not turn the family of source subfaces \(B_c\cup\{x\}\) into a comparably
large alphabet of independent physical labels.  It does show exactly
where a positive ambient-support argument must hand off.

## 5. Compatibility with the live normalization

The preceding barrier must not be promoted to a surviving minimizer
branch without imposing the corrected source-mass transfer.  Write
\(L=\log n\), let \(N\) be the full aligned source-support size, and let
\(c=1/2-\delta\) be the fixed-gap induction coefficient.  On the live
rank-safe chart,

\[
 \log W\ge\log V(P)-O(L\log L),\qquad
 \log{V(P)\over H}=O(L\log L).                         \tag{32}
\]

The exact transfer theorem in
HIGH_REDUNDANCY_RELEASE_HALL_BARRIER.md gives

\[
 \boxed{\quad
 \mathbb E R_U
 \le r\log(N/r)-c(\log N)^2+O(L\log L)
 = (r-c\log N)\log N-r\log r+O(L\log L).
 \quad}                                                \tag{33}
\]

Consequently every slice

\[
                         r\le c\log N+O(\log L)         \tag{34}
\]

is already in the low-redundancy product branch.  A quadratic high-\(R_U\)
residue can occur only in the excess-rank window

\[
                         r-c\log N=\Omega(L).           \tag{35}
\]

This qualification is compatible with the present regression.  Taking
\(r=\Theta(\log d)\) does put its diagonal code above the rank-tax line,
but its selected source weight is tiny compared with the detached Boolean
support bank \(2^Y\).  It therefore violates (32) by far more than
\(O(L\log L)\).  The regression kills an unconditional local
released-prefix theorem; it does not prove that the bad fibre carries
positive live marked mass.

Combining (33) with Section 4 leaves the following exact normalized
endpoint **inside the intrinsic actual-support subbranch**.

1. Only the excess-rank slice (35) needs a high-redundancy argument.
2. On that slice, (26a) pays every low weighted support-codegree family
   with one global ambient bank.
3. High weighted support codegree fixes one actual physical deleted label
   \(x\).
4. The two ordinary targets are then
   \(E=B\cup\{x\}\) and \(U=B\cup F\).  Their ordered pair recovers
   \((B,F,J,x)\) by (31).
5. After canonical coalescing, the only remaining multiplicity is the
   certified source-internal state load, at most
   \(2^{O(L\log L)}\) in the rank-safe description theorem.

Thus, in the intrinsic actual-support subbranch, the live unsolved object
is an excess-rank, fixed-physical-label dense graph of actual source
subfaces \(B\cup\{x\}\) against actual released faces \(B\cup F\).
Closing it requires either rank compression/source downshadows or a
planar mixed/profile bank for this graph.

There remains a separate full-alphabet branch: high \(R_U\) may be
dominated by conditional support deficit or output information in
(1)--(2).  The full support-Cauchy theorem still gives (11a), but a
congested label which is absent from the conditional support does not
produce (27).  That branch ends at the original cap-weighted global
support-overlap/profile gate, not at the fixed-\(x\) Hall graph.  The
present reduction does not close either endpoint, so no coefficient-half
conclusion is claimed.

## 6. Scope

This report proves the weighted intrinsic-support inequality (4), the
exact decompositions (1)--(2), and a scalable rational obstruction to any
\((B,F,J)\)-retaining support/downshadow theorem.  It does **not** close
the high-redundancy branch globally.  The detached Boolean banks make the
regression easy for the full face count, while an arbitrary low-face
support union still requires the global Hall/common-prefix machinery of
GLOBAL_SUPPORT_UNION_HALL_CONSOLIDATION.md.

## Verification

Run

    python3 phase2/loop/erdos838/agent_outer_internal_product/verify_high_redundancy_released_prefix.py

The verifier checks the entropy decompositions, the exact Hall formulas,
the diagonal downshadow count, and exact rational anti-aligned clouds.  It
exhausts every nonempty support subset against every released triple in
the small models and confirms that no retained mixed face exists.
