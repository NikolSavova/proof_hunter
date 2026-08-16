# Excess-rank completion compression ends at a dense face rectangle

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The excess-rank, fixed-physical-label endpoint has an exact rank-compression
theorem, but ordinary downshadows alone do not close it.

Let a retained release record be

\[
                         \omega=(A,F,U,D),              \tag{1}
\]

where \(A=B\cup D\) and \(U=B\cup F\) are ordinary faces, the source and
pocket alphabets are disjoint, and \(D\) is the deleted completion of
fixed rank \(s\).  Suppose a rank/mask/state bucket has total record weight
\(M_s\), with every original source atom of weight at most one.

For every \(0\le t\le s\), counting completion \(t\)-traces gives an actual
ordinary face \(I\) with

\[
 \boxed{\quad
 M_I:=\sum_{\omega:I\subseteq D_\omega}w_\omega
 \ge {\binom{s}{t}\over\binom Nt}\,M_s.
 \quad}                                                \tag{2}
\]

The face \(B\cup I\) is ordinary for every incident record.  However,
\((B\cup I,U)\) recovers only \((B,F,J,I)\), not the rest of \(D\).  The
unconditional set-system cap on that residual multiplicity is

\[
                         \binom{N-t}{s-t}.              \tag{3}
\]

This creates a sharp quadratic-scale conflict when \(s=\Theta(L)\) and
\(\log N=\Theta(L)\):

* \(t=O(\log L)\) costs only \(O(L\log L)\) bits in (2), but (3) remains
  \(2^{\Theta(L^2)}\);
* making (3) at most \(2^{O(L\log L)}\) requires
  \(s-t=O(\log L)\), while (2) then costs \(\Theta(L^2)\) bits.

Thus rank compression by an ordinary source downshadow cannot
simultaneously preserve the live quadratic mass and make the projected
pair decoder quasipolynomial.

Retaining the full completion does give an exact decoder.  The pair

\[
                              (D,U)                     \tag{4}
\]

recovers \(B=U\cap\text{source roles}\), \(F=U\cap\text{pocket}\), and
\(A=B\cup D\).  Fractional Hall therefore routes the records either with
low global face load or to a dense completion-face by released-face core.
The live normalization forces the latter.  If

\[
 W\ge V(P)/\Xi,\qquad M_s\ge WH/\Gamma,                \tag{5}
\]

then one physical deleted label \(x\) lies in records of total weight at
least \(sM_s/N\).  The exact two-target Hall density on those records is
at least

\[
 \boxed{\quad
 \eta_x\ge {sM_s\over2NV(P)}
       \ge {sH\over2N\Gamma\Xi}.
 \quad}                                                \tag{6}
\]

For \(\Gamma\Xi=2^{O(L\log L)}\) and
\(\log H=(c-o(1))L^2\), this is still
\(2^{(c-o(1))L^2}\).  Weighted pruning produces a core of that scale.
Equation (6) is a localization theorem, not a contradiction.

There is a scalable rational equality regression.  Take two anti-aligned
convex \(p\)-point clouds and let both face alphabets consist of all
rank-\(s\) subsets.  Their incidence graph is complete, every mixed union
is bad for \(s\ge3\), and a fixed \(t\)-trace has exactly
\(\binom{p-t}{s-t}\) completion neighbours.  All ordinary mixed faces
have rank at most two in each cloud, so no bounded-anchor mixed profile
bank repairs the loss.

The regression is excluded by the live normalization in the bounded-rank
window.  Its full cloud bank has

\[
 V=1+2(2^p-1)+
       \left(p+\binom p2\right)^2,                     \tag{7}
\]

whereas \(W=\binom ps\).  If \(s=O(\log n)\) and \(n=2p+O(1)\), then
\(\log W=O((\log p)^2)=o(p)=\log V-o(p)\), so
\(W\not\ge V2^{-O(L\log L)}\).  Consequently this is an exact abstract
and planar barrier to downshadow compression, but not a live minimizer
counterfamily.

The remaining theorem is now narrow:

> in the excess-rank slice \(r-c\log N=\Omega(L)\), rule out a dense
> incompatible completion-face by released-face rectangle carrying
> \(W\ge V2^{-O(L\log L)}\), or show that it exposes a detached/profile
> bank beyond the two child face banks.

No fixed-power or coefficient-half closure is claimed.

## 1. Exact trace compression

Let the completion ground set have at most \(N\) labels.  Count pairs
\((\omega,I)\), with \(I\in{D_\omega\choose t}\), using record weight
\(w_\omega\).  Their total weight is

\[
                         \binom st M_s.                \tag{8}
\]

There are at most \(\binom Nt\) possible traces, proving (2).  Since
\(B\cup D\) is ordinary, heredity makes both \(I\) and \(B\cup I\)
ordinary.

For one fixed \((B,F,J,I)\), the labels of \(D-I\) can be any
\((s-t)\)-subset of the remaining \(N-t\) labels.  This proves (3).
The cap is attained by the complete rank-\(s\) family, so no smaller
universal expression follows from facehood.

When \(t=o(s)\), Stirling gives

\[
 \log{\binom Nt\over\binom st}
       =t\log{N\over s}+O(t\log(t+2)).                 \tag{9}
\]

For \(s-t=k\), the residual cap obeys

\[
 \log\binom{N-t}{s-t}
       =k\log{N\over k}+O(k+\tfrac{k t}{N}).           \tag{10}
\]

With \(s=\Theta(L)\), \(\log N=\Theta(L)\), equations (9)--(10) give the
two bullets in the verdict.  More elementarily:

\[
 t\le C\log L\Longrightarrow
     \log{\binom Nt\over\binom st}=O(L\log L),          \tag{11}
\]

whereas

\[
 s-t\le C\log L\Longrightarrow
     \log\binom{N-t}{s-t}=O(L\log L)                   \tag{12}
\]

but then \(\log\binom Nt=\Theta(L^2)\).  The middle range loses a fixed
quadratic fraction on both sides and offers no quasipolynomial decoder.

The special case \(t=1\) fixes a genuine physical completion label:

\[
       \max_x\sum_{\omega:x\in D_\omega}w_\omega
                    \ge {sM_s\over N}.                 \tag{13}
\]

This is stronger than choosing a singleton from the full ambient support
union: every record counted in (13) actually contains \(x\), so
\(B\cup\{x\}\) is a certified source subface.

## 2. Decoder-safe Hall localization

Fix \(x\) from (13), and retain only records with \(x\in D\).  Give every
record the two actual targets

\[
                         D_\omega,\qquad U_\omega.      \tag{14}
\]

The role/pocket partition recovers \(B,F\) from \(U\); adjoining \(D\)
recovers \(A\).  Hence an ordered target pair has only the already-fixed
metadata load.  With literal geometric records it has load one.

Let \(\mathcal R_x\) be the fixed-\(x\) records and define

\[
 \eta_x=\max_{\varnothing\ne\mathcal R'\subseteq\mathcal R_x}
 {\sum_{\omega\in\mathcal R'}w_\omega\over
  |\{D_\omega:\omega\in\mathcal R'\}
       \cup\{U_\omega:\omega\in\mathcal R'\}|}.         \tag{15}
\]

The two-target max-flow theorem gives

\[
                    \sum_{\omega\in\mathcal R_x}w_\omega
                              \le\eta_x V(P).           \tag{16}
\]

There are at most \(V(P)\) targets of each kind.  Combining (13) and
(16) proves the first inequality in (6); (5) proves the second.

If \(\eta_x>K\), iterative deletion of target vertices of incident weight
at most \(K\) leaves a nonempty core of minimum weighted degree greater
than \(K\).  Thus every \(K<sH/(2N\Gamma\Xi)\) is available in the
normalized setting.  This is the exact dense core which rank compression
must resolve.

There is a weaker projected pair

\[
                     E_\omega=B_\omega\cup\{x\},
                     \qquad U_\omega=B_\omega\cup F_\omega.       \tag{17}
\]

It recovers \((B,F,J,x)\), as in the preceding report, but it need not
recover \(D\).  Its exact residual pair load is

\[
 \Delta(E,U,x)=
   \sum_{\omega:(E_\omega,U_\omega,x)=(E,U,x)}w_\omega,            \tag{18}
\]

which may be as large as the completion degree (3).  Therefore the
statement that \((E,U)\) “recovers the state” is safe only after the
completion word has genuinely been coalesced or separately tagged.  It
does not by itself recover the literal release record.

## 3. Anti-aligned rank-face equality regression

Use the rational anti-aligned two-cloud chart from
DENSE_HALL_TWO_CLOUD_PROFILE_BARRIER.md.  Let \(Y,Z\) each contain \(p\)
points and have opposite pure-parabolic facing profiles.  Every subset
of one cloud is ordinary, while a set meeting both clouds is ordinary
exactly when each nonempty trace has rank at most two.

Take

\[
             \mathcal D={Y\choose s},\qquad
             \mathcal U={Z\choose s},\qquad
             M_0=\binom ps.                            \tag{19}
\]

For every \((D,U)\in\mathcal D\times\mathcal U\), both targets are
ordinary and \(D\cup U\) is nonordinary when \(s\ge3\).  The record graph
is \(K_{M_0,M_0}\), so its exact Hall density is \(M_0/2\).

For a fixed \(t\)-face \(I\subset Y\),

\[
 |\{D\in\mathcal D:I\subseteq D\}|
                       =\binom{p-t}{s-t}.              \tag{20}
\]

Consequently the projected pair \((I,U)\) has exactly this load for every
\(U\).  Equation (20) attains (3).  At \(t=1\), each physical label lies
in \(\binom{p-1}{s-1}M_0\) records, attaining the averaging scale in
(13).

The exact ordinary-face count of the union is (7): the empty face, the
two nonempty Boolean cloud banks, and

\[
             \left(p+\binom p2\right)^2                \tag{21}
\]

mixed faces with ranks one or two on both sides.  In particular, adding
any fixed bounded anchor set can multiply (21) only by a constant, by
heredity.  This kills every theorem based only on rank compression,
facehood, and a bounded repaired mixed profile.

## 4. Why the equality regression is not live

Put \(n=2p+O(1)\), \(L=\log n\), and suppose \(s\le C L\).  The source
face alphabet satisfies

\[
 \log W=\log\binom ps
       \le s\log{ep\over s}=O(L^2),                   \tag{22}
\]

whereas (7) gives

\[
                         \log V(P)=p+O(1).              \tag{23}
\]

Since \(p=\Theta(n)\), the gap is \(\Theta(n)\), much larger than every
allowed \(O(L\log L)\) description or rank-bucketing loss.  Hence the
anti-aligned rank-\(s\) alphabet cannot satisfy the live condition
\(W\ge V(P)2^{-O(L\log L)}\).

This observation uses the detached Boolean banks, not a generic
set-system inequality.  Fixed-edge projective universality can replace a
cloud by an arbitrary child order type, but it does not prove that the
entire child face family has the same rank-at-most-two facing profile.
Producing such a low-profile child while keeping
\(W\ge V2^{-O(L\log L)}\) is exactly the missing geometric construction;
ruling it out is exactly the desired positive profile theorem.

## 5. Live endpoint

By the corrected transfer theorem, quadratic high completion redundancy
is already restricted to

\[
                         r-c\log N=\Omega(L).           \tag{24}
\]

Suppose the surviving branch still carries the quadratic adaptive-cover
mean

\[
                   \mathbb E\sigma\ge(c-o(1))L^2.       \tag{24a}
\]

Since \(\sigma\le |J|\log N\le |J|L\) and the rank-safe cutoff gives
\(|J|\le R_0L\), the part with \(|J|<cL/2\) contributes at most
\((c/2)L^2\) to the mean.  The complementary part therefore has
probability at least \(c/(2R_0)-o(1)\).  After one of only \(O(L)\) rank
buckets is fixed, it has

\[
                         s=|J|=\Omega(L)                \tag{25}
\]

and loses only a polynomial factor.  If (24a) has already been spent in
an earlier branch, (25) is not asserted.  Under this explicit live
high-cover hypothesis, equations (2), (6), and (25) are the strongest
unconditional downshadow consequences:

* small traces preserve mass but leave quadratic completion ambiguity;
* full completions give a decoder and force a dense Hall core;
* the planar anti-aligned model realizes both failures, but violates live
  source normalization because of its detached Boolean banks.

What remains is a geometry-plus-normalization theorem, not a stronger
Kruskal--Katona estimate.

## Verification

Run

    python3 phase2/loop/erdos838/agent_outer_internal_product/verify_excess_rank_fixed_label_downshadow.py

The verifier checks all binomial trace identities and Hall values, exact
decoder reconstruction, the rational anti-aligned geometry, the complete
rank-face codegrees, and the full face-count formula (7).
