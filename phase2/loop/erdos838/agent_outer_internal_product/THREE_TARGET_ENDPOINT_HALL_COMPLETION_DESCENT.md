# Three-target endpoint Hall and the completion/downshadow descent

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

**Strengthening.**  `DETACHED_BASE_ENDPOINT_HALL_STRENGTHENING.md`
supersedes the source-ear hypothesis below for the live detached branch:
the already assumed face `Q=B union {v}` is an unconditional second Hall
target.  The present report remains the stronger completion descent when
the old pair ear `E=A union e` is also known to be convex.

After endpoint and role coloring, the dense two-sided residue of
`DETACHED_LOAD_SOURCE_EAR_HALL.md` really does localize to one matching
pair.  In such a component a record has the form

\[
 A=B\cup G,\qquad e=\{v,u\},\qquad
 W=F\cup\{v\},\quad E=A\cup e,\quad C=B\cup F.          \tag{1}
\]

All three displayed targets are ordinary faces: `W` is the detached
endpoint face, `E` is the retained old source ear, and `C` is the
guard-released pocket face.  Fractional Hall routing to all three targets
has the exact optimal load

\[
 \boxed{\displaystyle
 \lambda _3=\max_{\varnothing\ne\mathcal R'\subseteq\mathcal R}
 {\sum_{r\in\mathcal R'}w_r\over
  |\bigcup_{r\in\mathcal R'}\{W_r,E_r,C_r\}|}.}          \tag{2}
\]

Hence `sum_r w_r <= lambda_3 V(P)`.  If `lambda_3>K`, deletion of
low-degree targets leaves a nonempty three-uniform core of weighted
minimum degree greater than `K`.  If the ordered triple multiplicity is at
most `Delta_3`, each surviving target is incident with more than
`K/Delta_3` distinct pairs of other targets.  This is an exact linear
payment/dense-core dichotomy; no face budget is spent once per endpoint
pair.

The high-`C` fibre has an exact geometric interpretation.  Fixing `C` and
the role supports fixes `B,F`; fixing the endpoint component fixes `e`.
The varying source ears are

\[
                         E_G=B\cup G\cup e.              \tag{3}
\]

Heredity therefore exposes the completion downshadow bank

\[
 \mathcal D(B,e;\mathcal Q)
   =\{B\cup S\cup e:S\subseteq G\text{ for some }G\in\mathcal Q\}, \tag{4}
\]

where `mathcal Q` is the family of guards/completions in the fibre.  This
is the precise descent supplied by guard release.  The unresolved issue is
global downshadow overlap: many high-`C` fibres can reuse the same faces in
(4), so (4) is not by itself a fixed-power theorem.

Planarity does **not** rule out a dense three-target core.  There is a
scalable rational common-cage rectangle with `m^2` records but only `m`
targets of each kind, and consequently exact `lambda_3=m/3`.  It preserves
the actual source pair-ear convexity and actual guard release.  However,
the same realization exposes two convex support shields of size
`2^m`.  Thus this regression is harmless for the face count and sharply
identifies the live statement: every dense core would have to expose a
large completion/pocket support bank with globally controlled overlap.
That final global statement is not proved here.

## 1. Localization to one endpoint pair

Assume a canonical endpoint orientation for which each chosen endpoint
`v` determines its unique matching pair `e(v)`.  Also retain the target
role coloring: a `W` target contains exactly the chosen endpoint, whereas
an `E` target contains exactly the two labels of the pair.  Then

\[
 W\longmapsto v\longmapsto e(v),\qquad E\longmapsto e.  \tag{5}
\]

Consequently the bipartite `W--E` incidence graph is the disjoint union of
components indexed by `e`.  Its target sets are genuinely disjoint across
components, so summing Hall capacities over components uses the global
ordinary-face budget once, not once per `e`.

Inside a fixed component, and after choosing which endpoint is `v`, the
left target determines `F=W\setminus\{v\}` and the right target determines
`A=E\setminus e`.  Thus records are precisely weighted incidences between
source bases `A` and pocket traces `F`, with the deleted guard relation
`B=A\setminus G` retained.  Any ambiguity still present after this
coloring is the actual canonical history/root multiplicity; denote it by
`Delta`, rather than declaring it to be one.

The released target `C` need not determine `e` and may be shared by
different endpoint components.  For that reason the theorem below is
stated after fixed-`e` localization.  Globally one must retain the actual
load of a `C` face across components.

## 2. Exact three-target fractional Hall

Let `mathcal R` be a finite family of records of the form (1), with
nonnegative weights `w_r`, and suppose `W_r,E_r,C_r` are ordinary faces.
Coincidences between any of the three target types are allowed: all unions
below are unions of actual faces, not typed formal copies.

> **Theorem 1 (three-target Hall).**  The minimum possible maximum load in
> a fractional routing which sends `w_r` from every record to its target
> set `\{W_r,E_r,C_r\}` is exactly (2).  In particular,
>
> \[
>                            \sum_rw_r\le\lambda _3V(P). \tag{6}
> \]

**Proof.**  Join a source to record `r` with capacity `w_r`, join `r` to
each distinct face among `W_r,E_r,C_r` with infinite capacity, and join
every target face to the sink with capacity `lambda`.  Max-flow/min-cut
says that the demand is routable if and only if

\[
 \sum_{r\in\mathcal R'}w_r
  \le\lambda\,|\bigcup_{r\in\mathcal R'}\{W_r,E_r,C_r\}|             \tag{7}
\]

for every record subfamily.  This proves (2).  Summing target loads over
the at most `V(P)` actual ordinary faces proves (6).  QED.

> **Corollary 2 (three-sided dense core).**  If `lambda_3>K`, a nonempty
> record subfamily remains after pruning and every one of its target faces
> has incident record weight greater than `K`.

Choose a family violating (7) at `lambda=K`.  Repeatedly delete a target
of current incident weight at most `K`, together with every incident
record.  If the process deleted all targets, charge each record when its
first target is deleted.  The total charged weight would be at most `K`
times the original number of targets, contrary to the violation.

Define the actual ordered-triple load

\[
 \Delta _3=\max_{W,E,C}\sum_{r:(W_r,E_r,C_r)=(W,E,C)}w_r.            \tag{8}
\]

At a fixed surviving target, every ordered pair of its other two targets
contributes at most `Delta_3`; hence its degree greater than `K` supplies
more than `K/Delta_3` distinct incident target pairs.  Notice that this
does not assert that both individual neighbor sets have that size.

## 3. Decoder and completion downshadow

In one fixed-`e` component, role supports give the exact decoder

\[
 F=W\setminus\{v\},\qquad A=E\setminus e,\qquad
 B=C\setminus F,\qquad G=A\setminus B.                  \tag{9}
\]

Thus `(W,E,C)` recovers the full geometric record.  Formula (8) is exactly
the residual multiplicity of canonical descriptions with those recovered
labels.

Now fix a `C` target.  Equations (9) fix `B,F`; the endpoint component
fixes `e`.  Let `mathcal Q_C` be the family of distinct completions `G`
in this fibre.  Since (3) is convex, every subset of it is convex, and in
particular every face in (4) is ordinary.  More quantitatively, if a
completion `G` has record weight `beta_G`, then generating every one of its
subsets gives

\[
 \sum_{G\in\mathcal Q_C}\beta_G2^{|G|}
 \le \Lambda_{\rm down}(C,e)\,V(P),                    \tag{10}
\]

where the *actual* output load is

\[
 \Lambda_{\rm down}(C,e)=
 \max_H\sum_{G\in\mathcal Q_C}\beta_G
       |\{S\subseteq G:B\cup S\cup e=H\}|.             \tag{11}
\]

For distinct labels the set `S` is recovered from `H`, so (11) is simply
`max_S sum_{G superset S} beta_G`.  Equations (10)--(11) are exact, but the
empty subtrace shows why one cannot replace `Lambda_down` by one.

A useful special case is a common base with pair ears.  If `A` is fixed
and `A\cup e_j` is convex for `m` distinct endpoint pairs, then

\[
                     \{S\cup e_j:S\subseteq A,1\le j\le m\}          \tag{12}
\]

is a load-one bank of exactly `2^{|A|}m` ordinary faces.  Across varying
bases its correct global form is

\[
 \sum_g2^{|A_g|}\sum_{r\in\mathcal R_g}w_r
       \le\Lambda_{\rm bool}V(P),                       \tag{13}
\]

with `Lambda_bool` the actual output multiplicity.  Hence a base of rank
at least `epsilon log D` gives a fixed-power gain whenever this multiplicity
is subpower.  Cross-base reuse/container promotion remains external.

## 4. A genuine planar dense common-cage rectangle

Take

\[
\begin{aligned}
 l&=(-3,0),&r&=(3,0),&t&=(0,5),\\
 a&=(-2,-1),&b&=(2,-1),&B&=\{l,r,t\}.                  \tag{14}
\end{aligned}
\]

For `1<=i,j<=m`, choose pairwise distinct rational points in sufficiently
small general-position perturbations of

\[
 g_i=(z_i,5+z_i-z_i^2),\quad z_i={i\over100m},
 \qquad
 x_j=(s_j,-4+s_j^2),\quad s_j={2j-m-1\over200m}.         \tag{15}
\]

The perturbations may be chosen sequentially to avoid the finitely many
old lines.  All required properties are strict and therefore persist:

\[
\begin{array}{ll}
 B\cup\{a,b,g_i\}\text{ is convex},&
 B\cup\{x_j\}\text{ is convex},\\
 \{x_j,a\}\text{ is convex},&
 B\cup\{g_i,x_j,a\}\text{ is nonconvex}.               \tag{16}
\end{array}
\]

For the last assertion, `a` lies strictly inside
`triangle(l,x_j,r)`.  Moreover the two large sets

\[
 B\cup\{a,b\}\cup\{g_1,\ldots,g_m\},
 \qquad B\cup\{x_1,\ldots,x_m\}                         \tag{17}
\]

are themselves convex.

Define

\[
 A_i=B\cup\{g_i\},\quad G_i=\{g_i\},\quad e=\{a,b\},
 \quad F_j=\{x_j\}.                                    \tag{18}
\]

For every pair `(i,j)` this is an actual record with

\[
 W_j=\{x_j,a\},\qquad E_i=B\cup\{g_i,a,b\},
 \qquad C_j=B\cup\{x_j\}.                              \tag{19}
\]

There are `m^2` records and exactly `m` targets of each type.  More
generally, a record subfamily meeting `i` rows and `j` columns has at most
`ij` records and at least `i+2j` targets.  Therefore

\[
             \lambda _3=\max_{1\le i,j\le m}{ij\over i+2j}
                         ={m\over3}.                    \tag{20}
\]

This is a scalable planar high-density regression preserving both source
pair-ear convexity and guard release.  It disproves any proposed theorem
that planarity bounds `lambda_3` absolutely.

It also displays the intended alternative.  By (17), heredity supplies a
Boolean cube of at least `2^m` ordinary faces on the guard support and a
second cube of at least `2^m` faces on the pocket support.  The common-cage
rectangle has only `m^2` marked records, so these shields pay it
overwhelmingly.  What is not proved is that an arbitrary dense core admits
such a common convex support after a globally summable thinning.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos838/agent_outer_internal_product/verify_three_target_endpoint_hall.py
```

Expected output:

```text
PASS: three-target Hall, dense pruning, decoder counts, and planar common-cage rectangle
```

The verifier exhausts Hall subfamilies for small rectangles, checks the
closed formula (20), checks dense-core pruning, and uses exact rational
orientation arithmetic to certify (16)--(17) and general position through
forty labels.  Arbitrary scale follows from the open rational perturbation
argument above, not from extrapolating the finite computation.
