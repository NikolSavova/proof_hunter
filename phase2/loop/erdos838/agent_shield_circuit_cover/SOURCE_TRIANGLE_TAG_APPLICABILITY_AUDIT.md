# Source--triangle tagging: exact live mapping and the face-alphabet boundary

**Date:** 2026-08-15.  This adversarially audits
QUASIPOLY_SOURCE_TRIANGLE_TAG_CLOSURE against the corrected cycle/DAG and
source-mask branches.  All logarithms are base two.

## Verdict

The tagged-mass theorem is correct, and it closes the exact stationary
common-triangle tensor of FULL_WORD_TRIANGLE_REUSE_SCALE_BARRIER at the
\(n^{\Theta(\log\log n)}\) scale.

In that tensor a context is one actual base word.  Its row and column
alphabets are genuine physical point clouds, every row has an actual old
source face, and a selected three-set is an actual ambient triangle.  The
pair consisting of one canonical source face and the triangle distinguishes
the quadratic base word up to the already certified source-description
load.  There is no rank loss and no requirement that the source--triangle
union be convex.

The theorem must **not** be applied one reduction earlier to an arbitrary
dense rectangle whose rows and columns are multi-point faces.  A family of
\(a\) source faces is not a physical \(a\)-point cloud.  It supplies
neither \(\binom a3\) ambient triangles nor the local inequality on which
the tagged Cauchy step rests.  Choosing one representative point from
every face can have arbitrarily high reuse and returns precisely to the
high-projection-reuse residue in QUADRATIC_TRACE_RECTANGLE_OR_SHIELD.

Thus the exact scope is:

* **closed:** the stationary all-role/triangle blocker after a
  singleton-cloud or actual role-cell extraction;
* **still open:** a dense face-by-face rectangle before that extraction,
  or a multi-point profile product whose row/column count greatly exceeds
  the size of its physical label support; and
* **still fixed-power open:** even the singleton-cloud case when an
  \(n^{3/2}\) tag loss is not free.

At the quasipolynomial scale, no direction-spectrum potential or recursive
decorated two-mark construction is needed for the stationary physical
triangle branch.  The corrected directed-profile audit remains relevant
for fixed-power estimates and for the face-alphabet branch outside the
tag theorem's hypotheses.

## 1. The abstract tagged theorem is sound

For context \(c\), let

* \(\mathcal A_c\) be \(a_c\ge1\) actual ordinary old-source faces;
* the opposite active side have size \(b_c\);
* the simple record graph have \(e_c\le a_cb_c\) edges; and
* all edges in the dyadic layer carry common upper weight \(w_c\).

Put \(t_c=\max(a_c,b_c)\).  The additional geometric hypothesis is that
the larger side is represented by a role-coloured physical point cloud of
exactly \(t_c\) distinct labels.  When \(t_c\ge6\), take all its actual
three-point subsets:

\[
                   {\cal I}_c={Y_c\choose3}
                    \quad\hbox{or}\quad{Z_c\choose3},
 \qquad i_c={t_c\choose3}.                              \tag{1}
\]

The local inequality is

\[
                  e_c^2\le {54\over5}a_ci_c.           \tag{2}
\]

Indeed \(e_c^2\le a_c^2b_c^2\le a_ct_c^3\) and
\(\binom{t_c}{3}\ge5t_c^3/54\).

Define the compressed source occurrence load

\[
        \kappa_A=\max_A\sum_{c:A\in{\cal A}_c}w_c.      \tag{3}
\]

Choose one canonical \(A_c\in\mathcal A_c\).  Every incidence \((c,T)\),
\(T\in\mathcal I_c\), is tagged by the formal decoder pair \((A_c,T)\).
For a fixed pair its weight is at most

\[
 \sum_{c:A_c=A,\ T\in{\cal I}_c}w_c
       \le\sum_{c:A\in{\cal A}_c}w_c\le\kappa_A.       \tag{4}
\]

There are at most \(V(P)\) choices of \(A\) and at most \(\binom n3\)
actual triangles.  Therefore

\[
          \sum_cw_ci_c\le
               \kappa_AV(P){n\choose3},\qquad
          \sum_cw_ca_c\le\kappa_AV(P).                 \tag{5}
\]

Multiplying (2) by \(w_c\), summing, and applying Cauchy proves

\[
 \boxed{\displaystyle
  \sum_cw_ce_c\le
    \kappa_A\left(5+
      \sqrt{{54\over5}{n\choose3}}\right)V(P).}        \tag{6}
\]

The first term handles \(t_c\le5\), where \(e_c\le5a_c\).

The tag \((A,T)\) is not asserted to be one ordinary face.  It is a
polynomial-size decoder state used only to sum the triangle incidences.
Consequently:

1. \(A\cup T\) may be nonconvex;
2. \(T\) may lie on either active side;
3. \(T\) may meet \(A\); and
4. the rank of \(A\) is unchanged.

These observations remove the apparent union/rank mismatch.  The only
substantive geometric requirement is the actual \(t_c\)-point cloud in
(1).

## 2. Exact map of the stationary tensor

Use the notation of FULL_WORD_TRIANGLE_REUSE_SCALE_BARRIER.  A context is
indexed by a base word

\[
             \omega\in[D]^q,\qquad
             B_\omega=B_0\cup\{z_{1,\omega_1},\ldots,
                                      z_{q,\omega_q}\}.            \tag{7}
\]

The two active physical clouds are \(G\) and \(X\), each of size \(m\).
The complete context has

\[
                    a_c=b_c=m,\qquad e_c=m^2.          \tag{8}
\]

For every \(g\in G\),

\[
                         A_{\omega,g}=B_\omega\cup\{g\} \tag{9}
\]

is an actual ordinary old-source target.  Base and guard role colours
recover \(B_\omega\) and \(g\) from (9), so different base words have
disjoint source families.  Choose one fixed canonical \(g_*\) and put
\(A_c=A_{\omega,g_*}\).

Take \(\mathcal I_c=\binom G3\) (or the corresponding bank in \(X\)).  The
physical triangles are common to all \(D^q\) contexts, so their raw
overlap is \(D^q\).  But

\[
                         (A_{\omega,g_*},T)             \tag{10}
\]

is different for every base word and every actual triangle.  For unit
contexts the pair load is one.  The verifier checks the smallest thick
case \(m=6\), where (2) is equality:

\[
                     5(6^2)^2=54\cdot6{6\choose3}.     \tag{11}
\]

This is exactly the stationary one-chamber/all-role blocker isolated in
DIRECTED_PROFILE_CYCLE_DAG_AUDIT.  Its fixed triangle, common circuit
sign, lack of directed cycles, and lack of separated directions do not
matter to (5)--(6).

## 3. Canonical source and context bookkeeping

The old source is unconditional in the live four-target branch:

\[
                         A=B\cup G\in{\cal F}(P).       \tag{12}
\]

Fixing \((A,e)\) in canonical radial peeling determines peel depth and
carrier.  Genuine history domination bounds the total weight of repeated
canonical descriptions.  After dyadic rounding, one actual source enters
once per nonempty weight layer; the geometric series costs less than two.
If the remaining certified description multiplicity is \(L\), then

\[
                              \kappa_A<2L.              \tag{13}
\]

There is one important coalescing rule.  If the same source and geometric
context are split into \(K\) separately named equal-weight one-column
contexts, their load in (3) is \(K\), not one.  They may be charged once
only after they are coalesced into one product context.  If distinct
tangent, root, or chronology states prevent coalescing, their number must
be included in \(L\).  Canonical radial decoding removes reset-depth
names; it does not erase distinct actual opposite-cloud marks.  Those
marks must appear as columns of the product or as certified context
descriptions.

In the stationary tensor, (9) already decodes the base word, so no
quadratic context loss remains.  On the minimizer slice \(L=n^{O(1)}\),
and (6) is \(n^{O(1)}V(P)\).  Every fixed polynomial is
\(o(n^{\sigma\log\log n})\), so the required scale-recovery deficit
closes.

## 4. The exact face-alphabet obstruction

Let \(Q\) be \(q\) points in convex position.  Its nonempty face family
has

\[
                              a=2^q-1                  \tag{14}
\]

actual ordinary members.  It is therefore a legitimate alphabet of
multi-point source faces.  But its physical ground support has only \(q\)
labels and hence only

\[
                              {q\choose3}               \tag{15}
\]

ambient triangles, not \(\binom a3\).

At \(q=8\), \(a=255\), while

\[
               {q\choose3}=56,\qquad
               {a\choose3}=2\,731\,135.                \tag{16}
\]

If both sides of a formal complete face rectangle have size \(a\), then
\(e=a^2\).  Substituting only the 56 actual triangles into (2) gives the
strict reverse inequality

\[
                         5e^2>54a{q\choose3}.           \tag{17}
\]

A triple of **faces** is not a rank-three ambient face tag.  Counting such
formal triples would cost up to \(V(P)^3\), destroying the linear
right-hand side of (6).  Choosing one representative point from every
source face gives at most \(q\) distinct representatives and can have
exponential projection load.

This is not a counterexample to Theorem (6), because it violates the
physical-cloud hypothesis (1).  It is a counterexample to silently
setting \(t_c\) equal to the number of multi-point row or column faces.

The exact nested-shell product in the corrected directed-profile report
has this form: its \(D^s\) inner rows and \(D^t\) outer columns are actual
transversal **faces**, supported on only \((s+t)D\) physical labels.  The
source tag exists, but the \(\binom{D^s}{3}\) or \(\binom{D^t}{3}\)
triangle bank does not.  Hence the source--triangle closure does not
resolve that multi-point profile product.

## 5. Consequence for the direction-spectrum task

At quasipolynomial scale, the stationary physical-triangle branch is
closed before the cycle/DAG split:

\[
 \text{stationary triangle tensor}
   \xrightarrow{\ (A,T)\ {\rm tags}\ }
   O(\kappa_An^{3/2})V(P).                              \tag{18}
\]

There is therefore no need to prove a direction-spectrum potential for
that branch.  Such a potential remains relevant in either of two settings.

1. At the fixed-power EIC scale, the \(n^{3/2}\) loss in (18) is not free.
2. Before singleton-cloud extraction, the active alphabets are
   multi-point faces and (1) is unavailable.

This cleanly reconciles the results.  The corrected cycle/DAG report
remains a valid warning against graph-only multiplication; the new tag
theorem bypasses its stationary **physical-cloud** example only at the
later quasipolynomial scale.

## Verification

Run:

    python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_source_triangle_tag_applicability_audit.py

The checker imports the exact stationary rational construction, verifies
the source/context/tag decoder at the first thick size, checks equality in
the local constant, and audits the \(q=8\) face-alphabet scope
obstruction.  The expected line is:

    PASS: stationary contexts=4 sources=24 tags=80 raw_T_load=4; face-alphabet sources=255 physical_T=56 formal_face_triples=2731135; context_loads=(37, 1)
