# Amplified third translations: local channels versus a transverse core

## 1. Outcome

The high-codegree amplification in
`SCALAR_BACKWARD_CELL_HIGH_CODEGREE_AMPLIFICATION.md` can be sharpened.
For every one-role base record, each third translation is either fully
endpoint-transverse or belongs to one of exactly fifteen local channels:

1. two shared-head anchor channels;
2. two shared-tail anchor channels;
3. four cross-orientation anchor-chain channels;
4. three endpoint channels in the good target role; and
5. four endpoint channels in the bad target role.

At most `15k-36` third translations are local.  More importantly, at the
literal live threshold `c(p)>=k`, every base record obeys the dichotomy

\[
 \boxed{
  T(C)\ge{c(p_C)\over2}
  \quad\hbox{or}\quad
  \max_j L_j(C)\ge {c(p_C)\over30}\ge {k\over30}.}      \tag{1.1}
\]

Here `T(C)` is the number of fully transverse third translations and the
`L_j(C)` are the fifteen channel loads.  This is pointwise and retains the
source pair, both base translations, the third translation, and the scalar
weight.

Consequently the entire high one-role term is bounded by `1/k` times the
sum of two strictly structured amplified masses: a fully endpoint-transverse
three-translation system and an endpoint-rich local-channel system.  The
four shared-head/shared-tail channels are directly compatible with the
existing clean-fibre closure; the cross channels and seven target-star
channels are the exact local mass still not covered by it.

The replacement amplification also splits exactly into

\[
 \sum_p\rho(p)^2V(p)
 \quad+\quad
 \sum_p\rho(p)(c(p)-\rho(p))V(p),                       \tag{1.2}
\]

separating pairs of rigid-pencil translations from a rigid translation
followed by a nonreplacement translation.  The first term retains the
nested replacement transition; the second retains an additional disjoint
target pair.  Existing unweighted `rho^2` control does not bound either
scalar-weighted term, so this split is a reduction, not a completion.

## 2. The fifteen channels

Fix an ordered source pair `p=(s,t)` and two translations

\[
 q_1,q_2\in Q_p,
\]

which form a one-role record.  Orient the roles so that

\[
 E(s+q_1)\cap E(s+q_2)\ne\varnothing,
 \qquad
 E(t+q_1)\cap E(t+q_2)=\varnothing.                    \tag{2.1}
\]

Write the ordered anchor of `q_i` as `(a_i,b_i)`, so `q_i=a_i-b_i`.
For a third translation `q_0` write its anchor `(a_0,b_0)` and target
edges

\[
 A_0=E(s+q_0),\qquad B_0=E(t+q_0).                     \tag{2.2}
\]

The anchor-local channels are the eight equalities

\[
\begin{array}{llll}
 a_0=a_1,&a_0=a_2,&b_0=b_1,&b_0=b_2,\\
 a_0=b_1,&a_0=b_2,&b_0=a_1,&b_0=a_2.
\end{array}                                             \tag{2.3}
\]

The first two are shared-head, the next two shared-tail, and the last four
are cross-orientation chains.  The good base target edges have a
three-point union

\[
 U_s=E(s+q_1)\cup E(s+q_2),\qquad |U_s|=3,              \tag{2.4}
\]

giving the three channels `x in A_0`, `x in U_s`.  The bad target edges
have a four-point union

\[
 U_t=E(t+q_1)\cup E(t+q_2),\qquad |U_t|=4,              \tag{2.5}
\]

giving the four channels `x in B_0`, `x in U_t`.

A third translation is **local** if at least one of (2.3)--(2.5) holds,
and **transverse** otherwise.  Thus a transverse record has its anchor
edge disjoint from both base anchor edges, its good-role target edge
disjoint from the three good base endpoints, and its bad-role target edge
disjoint from the four bad base endpoints.  All original clean conditions
remain in force as well.

## 3. Local capacity and the pointwise dichotomy

For a fixed `a`-point subset of `A`, the number of unordered edges meeting
it is

\[
 {k\choose2}-{k-a\choose2}=ak-{a(a+1)\over2}.           \tag{3.1}
\]

The map from a translation to its oriented anchor edge is injective, so
at most twice the `a=4` quantity have an anchor endpoint in the four base
anchor points.  The maps

\[
 q_0\longmapsto E(s+q_0),\qquad
 q_0\longmapsto E(t+q_0)                               \tag{3.2}
\]

are injective as well.  Applying (3.1) with `a=3` and `a=4` gives

\[
\begin{aligned}
 L(C)
 &\le 2(4k-10)+(3k-6)+(4k-10)\\
 &=15k-36.                                             \tag{3.3}
\end{aligned}
\]

Let `M=c(p_C)`, let `T(C)` be the transverse count, and let `L_j(C)` be
the fifteen channel loads, counted with overlap.  If `T(C)>=M/2`, the
first branch of (1.1) holds.  Otherwise more than `M/2` translations are
local.  Every local translation lies in at least one channel, so

\[
 \sum_{j=1}^{15}L_j(C)>{M\over2}.                       \tag{3.4}
\]

Pigeonhole proves the second branch of (1.1).

There is a useful ultra-high corollary.  If `M>=30k`, then (3.3) gives
`T(C)>=M/2`; hence no local alternative is needed in that range.

## 4. Weighted consequence

Let `\mathcal C_(>=k)` be the one-role base records whose source pair has
codegree at least `k`, and let

\[
 \mathfrak T(V)=
 \sum_{C\in\mathcal C_{\ge k}}T(C)
   \bigl(V(p_C)+V(p_C^{\rm op})\bigr).                  \tag{4.1}
\]

For each local-rich base record choose the first channel attaining the
second branch of (1.1), and define

\[
 \mathfrak L(V)=
 \sum_{C\text{ local-rich}}L_{j(C)}(C)
   \bigl(V(p_C)+V(p_C^{\rm op})\bigr).                  \tag{4.2}
\]

Then (1.1) gives the exact weight-preserving estimate

\[
 \boxed{
 D_{\rm one}^{\ge k}(V)
 \le {2\over k}\mathfrak T(V)
      +{30\over k}\mathfrak L(V).}                    \tag{4.3}
\]

Thus it is enough to prove

\[
 \mathfrak T(V)+\mathfrak L(V)\le m^{o(1)}Nk^4.        \tag{4.4}
\]

The local mass is no longer an arbitrary common-translation weight.  Its
chosen third translations form a star of degree at least `k/30` in one
specified anchor or target endpoint role.  In the shared-head and
shared-tail channels, the exact exceptional-total closure can be applied
without changing orientations.  A full proof must additionally control
the four cross-orientation chains and seven target roles, or show that
their endpoint stars force enough pair-sum support.

## 5. Replacement amplification

For a source pair `p`, split the third translation `q_0 in Q_p` according
to whether it belongs to the rigid replacement pencil `R_p`.  The exact
identity is

\[
\begin{aligned}
 \widetilde D_{\rm rep}(V)
 &=\sum_{p:c(p)\ge k}\rho(p)c(p)V(p)\\
 &=\sum_{p:c(p)\ge k}\rho(p)^2V(p)
   +\sum_{p:c(p)\ge k}\rho(p)(c(p)-\rho(p))V(p).
                                                               \tag{5.1}
\end{aligned}
\]

In the first term both translations lie in the same rigid pencil.  Their
two target roles share the fixed replacement centres and the nested source
transition is retained.  In the second term, the first translation is
rigid and the third is nonreplacement, so its two target edges are
disjoint.  The degree-two anchor theorem applies to the rigid translation
set, while the nonreplacement set supplies the additional target role.

The general amplification inequality remains

\[
 D_{\rm rep}^{\ge k}(V)
 \le {1\over k}\widetilde D_{\rm rep}(V).              \tag{5.2}
\]

## 6. Verification and stress

`verify_amplified_third_translation_local_transverse_dichotomy.py` checks:

* all fifteen channels and their union definition;
* the exact local capacity (3.3);
* the pointwise dichotomy (1.1) for literal `c(p)>=k` pairs;
* the ultra-high corollary and weighted finite form (4.3); and
* the replacement split (5.1).

It runs on scalar-aligned high-codegree pairs in the full 43-point
transformed-parabola stress, in addition to exhaustive small abstract
graphs.
