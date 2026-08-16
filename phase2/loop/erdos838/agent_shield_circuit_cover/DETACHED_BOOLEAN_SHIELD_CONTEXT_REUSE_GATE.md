# Detached Boolean shields: the exact context-reuse gate

**Date:** 2026-08-15.  All logarithms are base two.  This continues
`HEREDITARY_FACE_TAG_CAUCHY_GATE.md` at the rooted-to-dense-context
promotion branch.

## Verdict

There are exactly two elementary ways in which a detached side shield can
pay a dense anti-aligned rectangle.

1. Treat its faces as an ordinary output bank.  If the old-source bank has
   load \(\kappa_A\), the shield bank has load \(\Lambda_S\), and the local
   demand satisfies \(e_c^2\le \Gamma a_cs_c\), then

   \[
       \sum_c w_ce_c\le
          \sqrt{\Gamma\kappa_A\Lambda_S}\,V(P).          \tag{1}
   \]

2. Pair each shield face with a canonical actual old source.  If the shield
   faces used as tags have rank at most \(k\), this eliminates their raw
   context reuse and gives

   \[
       \sum_c w_ce_c\le
       \sqrt\Gamma\,\kappa_A
       \sqrt{\sum_{j\le k}{n\choose j}}\,V(P).           \tag{2}
   \]

Both bounds are exact Cauchy statements.  They also expose an exact gap.
For a balanced \(m\) by \(m\) rectangle, \(a=m\) and \(e=m^2\), so the
one-side shield reservoir in (1) or (2) must have

\[
                            s\ge m^3/\Gamma.             \tag{3}
\]

Let the desired terminal multiplier be

\[
                            K=n^{\sigma\log\log n}.      \tag{4}
\]

If the hard branch has \(m=n^{\tau\log\log n+o(\log\log n)}\) with
\(\tau\ge\sigma\), then a rank
\(k=c\log\log n+o(\log\log n)\) Boolean subshield can satisfy (3) only if

\[
                              c\ge 3\tau,                \tag{5}
\]

whereas (2) is cheaper than \(K\) only if

\[
                              c<2\sigma.                 \tag{6}
\]

Equations (5)--(6) are incompatible.  Thus the accepted rank-\(k\) tag
gate cannot promote the hard balanced rectangle merely by taking
low-rank faces of one detached Boolean shield.

Taking the **full** Boolean shield repairs the local deficit, but can have
quadratic-entropy global reuse.  The exact construction of
`QUADRATIC_BASE_WORD_DETACHED_REUSE_BARRIER.md` has
\(M=D^q\) actual convex base contexts sharing the same side clouds.  A
detached face has load \(M\).  Even after attaching at most \(h\) chosen
base-role labels, some tagged output has load at least

\[
                    {D^{q-h}\over(q+1)2^q}.              \tag{7}
\]

For \(q=\Theta(\log n)\), \(D=\Theta(n/q)\), reducing this even to the
two-bank Cauchy allowance \(K^2/n^{O(1)}\) requires

\[
                    q-h\le(2\sigma+o(1))\log\log n.     \tag{8}
\]

So a tag of rank \(O(\log\log n)\) is not enough: the output must retain
all but \(O(\log\log n)\) of the \(\Theta(\log n)\) base roles.  The same
construction permits arbitrary prescribed rational low-face order types
in both side clouds.  This is a scalable, ACP-compatible context-reuse
regression, not a local counting objection.

Consequently the promotion branch needs a genuinely mixed face which
coexists with almost the whole base word, or a separate global
composition theorem paying those base roles.  A canonical source paired
with an unrestricted high-rank detached face is only a formal two-face
state; it has \(V^2\), rather than \(V\), possible values and does not give
a linear Hall bound.

## 1. Source--shield Cauchy with actual output load

Let \(P\) be an \(n\)-point planar general-position set and write
\(V=V(P)\).  For every weighted context \(c\), let

* \(\mathcal A_c\) be a family of \(a_c\) actual ordinary old-source faces;
* \(\mathcal S_c\) be a family of \(s_c\) actual ordinary detached shield
  faces;
* \(e_c\) be its demand and \(w_c\ge0\) its weight; and
* \(e_c^2\le\Gamma a_cs_c\).

Define the two genuine one-face loads

\[
 \kappa_A=\max_A\sum_{c:A\in\mathcal A_c}w_c,
 \qquad
 \Lambda_S=\max_F\sum_{c:F\in\mathcal S_c}w_c.          \tag{9}
\]

> **Theorem 1 (two-bank detached-shield Cauchy).**  Under these hypotheses,
> equation (1) holds.

**Proof.**  Double-counting incidences gives

\[
        \sum_cw_ca_c\le\kappa_AV,
        \qquad
        \sum_cw_cs_c\le\Lambda_SV.                    \tag{10}
\]

Therefore

\[
\begin{aligned}
 \sum_cw_ce_c
 &\le\sqrt\Gamma\sum_c
       \sqrt{(w_ca_c)(w_cs_c)}\\
 &\le\sqrt\Gamma
       \sqrt{\sum_cw_ca_c}\sqrt{\sum_cw_cs_c}\\
 &\le\sqrt{\Gamma\kappa_A\Lambda_S}\,V.
\end{aligned}                                          \tag{11}
\]

This proves the theorem.  Notice that a common shield used in \(M\)
unit-weight contexts has \(\Lambda_S=M\), even if its detached faces are
all distinct from the old sources.  Hence (1) closes a target \(KV\) only
when

\[
                       \Lambda_S\le {K^2\over
                                      \Gamma\kappa_A}.  \tag{12}
\]

This square allowance is the strongest elementary benefit of the
two-bank Cauchy.

## 2. Canonical-source tagging and the rank budget

Suppose now that each context has a canonical
\(A_c^\star\in\mathcal A_c\).  If every member of \(\mathcal S_c\) has
rank at most \(k\), tag a shield incidence by the formal pair
\((A_c^\star,F)\).  A fixed pair has weight at most \(\kappa_A\), and the
number of possible second coordinates is

\[
                         N_k=\sum_{j=0}^k{n\choose j}.  \tag{13}
\]

Thus

\[
             \sum_cw_cs_c\le\kappa_AVN_k.              \tag{14}
\]

Together with the first inequality in (10), Cauchy gives (2).  This is
exactly the positive rank-\(k\) escape: the source and tag do **not** need
to coexist in one convex face, but the tag rank must be globally small.

For \(k=c\log\log n+o(\log\log n)\),

\[
                      \sqrt{N_k}
          =n^{(c/2)\log\log n+o(\log\log n)}.           \tag{15}
\]

Now specialize to a balanced complete face rectangle.  It has
\(a=m\), \(e=m^2\), hence (3).  Even when the detached support is in
convex position, its rank-at-most-\(k\) Boolean subshield contains at most

\[
                    \sum_{j\le k}{p\choose j}\le N_k  \tag{16}
\]

faces.  Taking logarithms of (3) at the scale
\(m=n^{\tau\log\log n+o(\log\log n)}\) forces (5), while
(15) and the target (4) force (6).  If \(m\ge K/n^{O(1)}\), then
\(\tau\ge\sigma\) at leading order, so there is no feasible \(c\).

This is not an artifact of using only two banks.  With one source family
and \(b\) low-rank tag reservoirs, the exact Holder hypothesis

\[
              e_c^{b+1}\le\Gamma a_c\prod_{j=1}^b i_{c,j}          \tag{17}
\]

gives a global multiplier \(N_k^{b/(b+1)}\).  In the balanced case, equal
rank budgets require

\[
 c\ge(2+1/b)\tau,
 \qquad
 c<(1+1/b)\sigma,                                      \tag{18}
\]

again impossible for \(\tau\ge\sigma\).  Any fixed number of independent
low-rank shield tags has the same exponent mismatch.

## 3. Why an unrestricted canonical pair does not close

If \(F\) is allowed arbitrary rank, the pair
\((A_c^\star,F)\) can indeed decode the context in favorable examples.
But there are at most \(V^2\) such pairs, not \(VN_k\).  Repeating the
preceding argument gives only

\[
                    \sum_cw_cs_c\le\kappa_AV^2         \tag{19}
\]

and hence a \(V^{3/2}\) demand bound.  This is not a linear-in-\(V\) Hall
payment.  Equivalently, the pair is a separated two-output bank; without
an ordinary convex union it cannot be counted as one ambient face.

This pinpoints the geometry still missing from the promotion theorem.
One needs either:

* bounded actual shield-face load, as in Theorem 1;
* low rank, as in (2); or
* coexistence of the source/history mark with the shield face in one
  ordinary convex output.

## 4. Exact quadratic-context regression

The following facts are Theorem 1 of
`agent_outer_internal_product/QUADRATIC_BASE_WORD_DETACHED_REUSE_BARRIER.md`
and are checked by its exact rational verifier.

There are \(q\) separated base roles, each with \(D\) choices, giving

\[
                             M=D^q                              \tag{20}
\]

distinct actual convex bases \(B_\omega\).  The same pocket cloud \(X\)
and guard cloud \(G\) work for every base.  Every base supports the full
\(m\) by \(m\) record rectangle, all five ordinary targets
\(W,Q,C,A,E\), both actual consecutive gaps, and every singleton
guard--pocket cross face.  The pair \((A,C)\) decodes
\((B_\omega,g_i,x_j)\) with unit multiplicity.

The complete base-retaining bank has exactly

\[
                            M(m+1)^2                         \tag{21}
\]

faces.  In contrast, every face lying wholly in the detached clouds and
fixed anchors is reused by all \(M\) bases.  If an arbitrary decoder adds
at most \(h\) selected labels from the base word, there are at most

\[
              \sum_{s=0}^h{q\choose s}D^s
                    \le(q+1)2^qD^h                         \tag{22}

possible augmentations.  Pigeonhole gives (7).

Put \(L=\log n\), \(q=\rho L+o(L)\), and
\(\log D=L-o(L)\).  Then

\[
 \log\operatorname{load}
       \ge(q-h)\log D-q-O(\log q).                       \tag{23}
\]

For the load to meet the two-bank threshold (12), where
\(K=n^{\sigma\log\log n}\) and \(\Gamma\kappa_A=n^{O(1)}\), equation
(23) forces (8).  In particular, attaching only
\(h=O(\log\log n)\) labels leaves load
\(2^{(\rho-o(1))L^2}\), while the allowable load is only
\(2^{(2\sigma+o(1))L\log L}\).

The construction is projectively universal inside every role and both
side clouds.  Their detached order types may therefore be arbitrary
rational low-face children.  This removes a possible escape in which the
regression was blamed on Boolean side complexity: Boolean complexity is
needed for the local positive payment, but the quadratic context reuse
and decoder lower bound survive for arbitrary side order types.

## 5. Exact scope

This report proves a promotion **gate and regression**, not a global
sub-half construction.  The quadratic base words themselves are ordinary
faces, and further multi-role composition may pay in the complete point
set.  What is ruled out is the proposed local-to-global operation:

> canonical old source + one low-rank side-shield state, or full detached
> shield + only \(O(\log\log n)\) remembered base labels.

Any successful promotion of the remaining anti-aligned rectangle must
use a mixed output recovering \(q-O(\log\log n)\) base roles, or explicitly
charge the ambient multi-role face bank.  Merely observing that the side
cloud is a Boolean shield does not provide a bounded-load global bank.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_detached_boolean_shield_context_reuse.py
```

Expected output:

```text
PASS: weighted two-bank Cauchy, rank-budget incompatibility, quadratic-context geometry, and decoder thresholds
```
