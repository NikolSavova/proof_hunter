# Hereditary face alphabets: the exact rank-\(k\) tag gate

**Date:** 2026-08-15.  This attacks the
rooted-to-dense-context promotion prerequisite after
SOURCE_TRIANGLE_TAG_APPLICABILITY_AUDIT.  All logarithms are base two.

## Verdict

There is an exact replacement for the physical-triangle argument whenever
the dense face rectangle exposes sufficiently many **actual low-rank
ordinary tags**.  If context \(c\) has \(a_c\) old sources, demand \(e_c\),
and \(i_c\) ordinary tags of rank at most \(k\), then the local condition

\[
                         e_c^2\le\Gamma a_ci_c          \tag{1}
\]

gives the global bound

\[
 \boxed{\displaystyle
       \sum_cw_ce_c\le
          \sqrt\Gamma\,\kappa_A
          \sqrt{\sum_{j=0}^k{n\choose j}}\;V(P).}      \tag{2}
\]

Here \(\kappa_A\) is the dyadically compressed old-source occurrence
load.  The tags need not coexist with the source in one convex face; the
formal pair \((A,T)\) is only a decoder state.

Equation (2) gives an exact terminal-scale criterion.  For

\[
                    K=n^{\sigma\log\log n},             \tag{3}
\]

polynomial \(\Gamma,\kappa_A\), and

\[
                    k\le(2\sigma-\varepsilon)\log\log n,          \tag{4}
\]

the loss in (2) is \(o(K)\).  Thus any face rectangle satisfying (1) at a
free tag rank closes.

Heredity alone does **not** imply (1).  If the opposite alphabet contains
\(b\) faces of rank at most \(r\), the union of every individual
hereditary downset has at most

\[
                    b\sum_{j=0}^{\min(k,r)}{r\choose j}
                       \le b2^r                         \tag{5}
\]

distinct tags.  In a balanced complete \(m\) by \(m\) rectangle, (1)
requires \(i_c\ge m^3/\Gamma\).  Even taking every subface of every
alphabet face can work only if

\[
                              m^2\le\Gamma2^r.          \tag{6}
\]

For \(m=n^{\Theta(\log\log n)}\) and \(r=O(\log n)\), (6) fails by a
quasipolynomial factor.  No single-face downshadow tag argument can promote
that rectangle.

There is a scalable planar trace-level regression.  Take two oppositely
oriented parabolic clouds of \(p\) points and let both alphabets consist of
all rank-\(r\) faces, \(r\ge3\).  Every row and column is ordinary, but in
the anti-aligned chart every row--column union is bad.  The alphabet size
is \(m=\binom pr\), while its complete rank-\(r\) downshadow has only
\(\sum_{j\le r}\binom pj\) tags, rather than \(m^3\).  At
\(r=\Theta(\log\log n)\), this gives the precise
\(n^{\Theta(\log\log n)}\) face-alphabet obstruction.

The regression is not a low-face construction: each parabolic cloud is in
convex position and has a detached Boolean shield.  It is also stated at
the stripped trace/source--release level, not as a new full ACP
four-target lift.  It proves that rooted-to-dense promotion needs an
additional physical-support, mixed-union, or detached-shield operation;
heredity by itself is insufficient.

## 1. Weighted rank-\(k\) tag theorem

Let \(P\) be an \(n\)-point planar general-position set and let \(V=V(P)\).
For every weighted simple context \(c\), suppose:

* \(\mathcal A_c\) is a nonempty family of \(a_c\) actual ordinary
  old-source faces;
* the record demand is \(e_c\), with common dyadic upper weight \(w_c\);
* \(\mathcal T_c\) is a set of \(i_c\) actual ordinary faces of rank at
  most \(k\); and
* (1) holds.

Define

\[
                  \kappa_A=
                    \max_A\sum_{c:A\in\mathcal A_c}w_c.            \tag{7}
\]

> **Theorem 1 (source--rank-\(k\) tag Cauchy).**  Equation (2) holds.
> More generally, a family of exceptional contexts satisfying
> \(e_c\le\beta a_c\) contributes at most
> \(\beta\kappa_AV\).

**Proof.**  Choose one canonical \(A_c\in\mathcal A_c\).  Tag every
incidence \((c,T)\), \(T\in\mathcal T_c\), by \((A_c,T)\).  A fixed pair
has weight at most

\[
       \sum_{c:A_c=A,\ T\in\mathcal T_c}w_c
          \le\sum_{c:A\in\mathcal A_c}w_c\le\kappa_A.  \tag{8}
\]

There are at most \(V\) choices for \(A\) and at most

\[
                              N_k=\sum_{j=0}^k{n\choose j}          \tag{9}
\]

possible rank-at-most-\(k\) tags.  Therefore

\[
 \sum_cw_ca_c\le\kappa_AV,\qquad
 \sum_cw_ci_c\le\kappa_AVN_k.                         \tag{10}
\]

The square-root form of (1), followed by Cauchy and (10), gives

\[
\begin{aligned}
 \sum_cw_ce_c
 &\le\sqrt\Gamma
       \sum_c\sqrt{(w_ca_c)(w_ci_c)}\\
 &\le\sqrt\Gamma
       \sqrt{\sum_cw_ca_c}\sqrt{\sum_cw_ci_c}\\
 &\le\sqrt\Gamma\,\kappa_AV\sqrt{N_k},
\end{aligned}                                          \tag{11}
\]

which is (2).  The exceptional estimate is immediate from the first
inequality in (10).  QED.

The theorem is deliberately numerical once the tag reservoirs are
ordinary.  A tag can be a subface of a row, a subface of a column, a
circuit trace, or an unrelated canonical ambient triangle.  What matters
is its actual global rank-\(k\) identity and the local cardinality (1).

## 2. Terminal-scale optimization

For \(k=o(n)\),

\[
               N_k\le(k+1)\left({en\over k}\right)^k,
 \qquad
               \sqrt{N_k}=n^{k/2+o(k)}.                \tag{12}
\]

Suppose \(\Gamma\le n^{C_1}\) and \(\kappa_A\le n^{C_2}\), with fixed
constants.  If (4) holds, the exponent of the right-hand multiplier in
(2) is at most

\[
       {C_1\over2}+C_2+
          \left(\sigma-{\varepsilon\over2}\right)\log\log n
          +o(\log\log n),                              \tag{13}
\]

which is strictly below the exponent in (3) for large \(n\).  Thus (2)
closes an assumed \(KV\) deficit.

This is the exact tradeoff.  Increasing \(k\) creates more possible local
tags but spends \(n^{k/2}\) globally.  A proposed tag extraction must
verify both (1) and (4); quoting a large downshadow without the rank audit
is insufficient.

## 3. Physical-support triangle corollary

Suppose a context exposes an actual physical support \(U_c\) of size
\(p_c\).  Every three-point subset is ordinary, so one may take

\[
                         \mathcal T_c={U_c\choose3},
 \qquad i_c={p_c\choose3}.                              \tag{14}
\]

> **Corollary 2 (support-rich context).**  If
>
> \[
                 e_c^2\le\Gamma a_c{p_c\choose3}       \tag{15}
> \]
>
> for every retained context, then
>
> \[
              \sum_cw_ce_c\le
                 \sqrt\Gamma\,\kappa_A
                 \sqrt{\sum_{j=0}^3{n\choose j}}\;V(P).           \tag{16}
> \]

The original physical-cloud theorem is the case
\(p_c=\max(a_c,b_c)\) and \(\Gamma=54/5\).

For a complete balanced rectangle \(a_c=b_c=m\), (15) requires

\[
                          m^3\le\Gamma{p_c\choose3}.    \tag{17}
\]

Thus \(p_c=\Omega_\Gamma(m)\).  A face alphabet of size much larger than
its physical label support is exactly the branch which (16) cannot see.
More generally, a complete \(a\) by \(b\) rectangle needs

\[
                          p_c^3=\Omega_\Gamma(ab^2).    \tag{18}
\]

This is the promised quantitative support threshold.

## 4. Hereditary downshadow corollary and barrier

Let \(\mathcal B_c\) be the opposite face alphabet.  Define its
rank-\(k\) hereditary shadow

\[
 {\cal D}_{\le k}(\mathcal B_c)=
   \{T:\ |T|\le k,\ T\subseteq F
                    \text{ for some }F\in\mathcal B_c\}.           \tag{19}
\]

Every member is ordinary by heredity.  Therefore Theorem 1 applies with
\[
                         i_c=|{\cal D}_{\le k}(\mathcal B_c)|       \tag{20}
\]
whenever (1) is checked.

This yields a useful exact positive test, but no unconditional lower bound
of the needed magnitude.  If \(|\mathcal B_c|=b_c\) and every member has
rank at most \(r_c\), then a union bound gives

\[
 i_c\le b_c\sum_{j=0}^{\min(k,r_c)}{r_c\choose j}
                         \le b_c2^{r_c}.               \tag{21}
\]

For a balanced complete \(m\) by \(m\) context, (1) and (21) imply the
necessary condition (6).  In the low-mean minimizer slice
\(r_c=O(\log n)\), the right side of (6) is polynomial in \(n\), while
\(m^2=n^{\Theta(\log\log n)}\).  Hence all per-face hereditary tags,
including the full downshadow \(k=r_c\), miss the required local reservoir
by a quasipolynomial factor.

Kruskal--Katona can sharpen a **lower** bound on (20) for a uniform
alphabet, but it cannot evade the upper bound (21).  The obstruction is
not overlap between shadows; one rank-\(r\) face simply contains only
\(2^r\) subfaces.

## 5. Exact anti-aligned face rectangle

Use the two infinitesimal parabolic clouds in
DENSE_HALL_TWO_CLOUD_PROFILE_BARRIER.  Give the first the sign for which
its facing right profiles have rank at most two, and give the second the
opposite sign for which its facing left profiles have rank at most two.
For cloud size \(p\), every nonempty local subset is ordinary.  The exact
two-block recurrence says a trace meeting both clouds is ordinary exactly
when its two traces belong to the facing profiles.

Fix \(r\ge3\) and take

\[
 \mathcal A={Y\choose r},\qquad
 \mathcal B={Z\choose r},\qquad
 m={p\choose r}.                                      \tag{22}
\]

Every member of \(\mathcal A\cup\mathcal B\) is an actual ordinary
rank-\(r\) face, but

\[
                         G\cup F\notin{\cal F}(P)
 \quad(G\in\mathcal A,\ F\in\mathcal B).               \tag{23}
\]

Thus the complete \(m\) by \(m\) source--release trace rectangle has
\(m^2\) bad records.  Choosing the first point of each face as a mark has
maximum projection load \(\binom{p-1}{r-1}\), so high mark reuse is
present as well.

The complete rank-\(r\) shadow on one side is only

\[
                    \sum_{j=0}^r{p\choose j},          \tag{24}
\]

whereas (1) with constant \(\Gamma\) would require order \(m^3\) tags.  At
\(p=7,r=3\), the exact values are

\[
       m=35,\quad m^2=1225,\quad
       |{\cal D}_{\le3}|=64,\quad m^3=42875.           \tag{25}
\]

The verifier checks all 1225 cross unions and finds every one bad.

For the scalable terminal regime, take \(p=\Theta(n)\) and
\(r=(\sigma+o(1))\log\log n\).  Stirling gives

\[
                 \log_n m=(\sigma+o(1))\log\log n.     \tag{26}
\]

The face ranks are \(O(\log\log n)\), well inside the minimizer cutoff,
yet (21) is exponentially too small relative to \(m^3\).

This is a rigorous planar regression for the tag extraction, not for the
whole lower-bound theorem.  Each cloud is convex-position and contributes
a detached Boolean shield of \(2^p\) faces.  Moreover (22)--(23) are the
stripped trace/source--release data; no new claim is made that every
upstream ACP root and endpoint mark can be attached simultaneously.  The
construction shows exactly where a positive promotion theorem must use
those extra marks or charge the detached shield.

## 6. What remains

The rooted-to-dense promotion now has an exact three-way menu.

1. **Support-rich:** (15) holds using actual physical triangles; the
   polynomial rank-three tag closes.
2. **Shadow-rich:** (1) holds for a hereditary rank-\(k\) shadow satisfying
   the free-rank condition (4); Theorem 1 closes.
3. **Tag-poor:** the context violates both.  In a balanced
   quasipolynomial rectangle, (6) shows that this is the generic
   possibility for bounded-rank face alphabets.  A new mixed-union,
   external-mark, or detached-shield theorem is required.

The anti-aligned parabolic family proves that the third branch is
stretchable and can make every mixed trace bad.  Its detached Boolean
shield identifies the natural next bank, but controlling that bank's
reuse across the rooted contexts is still the global operation.

## Verification

Run:

    python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_hereditary_face_tag_cauchy_gate.py

The checker verifies the weighted tag/Cauchy inequalities with overlapping
sources and tags, the support and hereditary thresholds, the free-rank
scale, and the exact \(p=7,r=3\) anti-aligned rational rectangle.  Its
expected line is:

    PASS: abstract=(Fraction(19, 15), 5, 6, Fraction(41, 5)) thresholds=36; rectangle alphabet=35 bad=1225 shadow=64 required=42875 mark_load=15; scale=81
