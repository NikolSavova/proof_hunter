# High transversal does not defeat a common-pocket ear product

**Date:** 2026-08-15. All logarithms are base two.

## Verdict

The natural high-transversal replacement for the stationary all-loop
example is rationally realizable, but it is not live. Suppose that on each
of \(m\) disjoint boundary-ear carriers there are

* \(A\) source labels \(x_{i,a}\);
* \(A\) pairwise vertex-disjoint target triangles \(T_{i,b}\); and
* every \(x_{i,a}\) lies strictly inside every \(T_{i,b}\).

Then every source--target choice is bad through an actual \(1+3\) circuit,
and the released trace hypergraph has \(A\) disjoint triangles at each of
\(m\) chronology levels. Thus the weighted root dispersion is exactly
\(A\), with no fixed physical root.

Write

\[
 T_{i,b}=\{\ell_{i,b},z_{i,b},r_{i,b}\}
\]

in the order in which the target ear replaces its carrier edge. A common
interior source \(x_{i,a}\) immediately gives the two ordinary half-triangle
ears

\[
 K\cup\{\ell_{i,b},x_{i,a}\},\qquad
 K\cup\{x_{i,a},r_{i,b}\}.                               \tag{1a}
\]

Thus, when the actual source mark is recoverable, one left endpoint and
that mark already encode the whole \(A\times A\) local rectangle.
Independently, a common interior point forces every crossed endpoint pair

\[
                         \{\ell_{i,b},r_{i,c}\}          \tag{1}
\]

to be an admissible ear. Nonadjacent carriers commute. Hence

\[
 K\cup\bigcup_{i=1}^m
        \{\ell_{i,b_i},r_{i,c_i}\}                       \tag{2}
\]

is an ordinary face for every two words \(b,c\in[A]^m\). The vertices in
(2) recover both words, so these are \(A^{2m}\) distinct faces with decoder
load one.

If the source and target word alphabets are both \([A]^m\), fix arbitrary
roles and use the even simpler mixed bank

\[
 K\cup\bigcup_{i=1}^m
        \{\ell_{i,b_i},x_{i,a_i}\}.                      \tag{2a}
\]

It directly recovers the source word \(a\) and target word \(b\).
Alternatively, the endpoint-only bank (2) can encode the source word via
arbitrary rolewise bijections to target triangles. Either bank injects the
whole bad record rectangle into ordinary faces:

\[
                         M=A^{2m}\le V.                  \tag{3}
\]

Thus this diffuse-root gadget cannot satisfy
\(M\ge V^2/2^{O(L\log L)}\) once \(V\) is on the
quadratic-exponential scale. Unlike the stationary-root payment, the
payment here is an actual cross-triangle endpoint product.

The scope is important. The theorem uses literal ears on nonadjacent edges
of one retained convex carrier. Same-type singleton transversals or
Bárány--Pach strong separation alone do **not** imply (2); the exact
counterexample in `STRONG_SEPARATION_ENDPOINT_PROFILE_COUNTEREXAMPLE.md`
still applies. Therefore a live survivor must make a positive density of
the disjoint circuit traces systematically nonseparated from their carrier
contexts.

## 1. The one-ear tangent lemma

Let \(uv\) be an oriented edge of a strictly convex carrier \(K\). Apply
an affine chart in which

\[
                 u=(-1,0),\qquad v=(1,0),               \tag{4}
\]

and the exterior ear pocket lies in \(y>0\). For a point \(p=(s,t)\) in
that pocket define its two endpoint slopes

\[
       \alpha(p)={t\over 1+s},\qquad
       \beta(p) ={t\over 1-s}.                           \tag{5}
\]

For two pocket points \(p,q\), the boundary word \(u,p,q,v\) is a strict
convex ear, in this order, exactly when

\[
                    \alpha(p)>\alpha(q),\qquad
                    \beta(p)<\beta(q).                  \tag{6}
\]

These are the determinant inequalities at the two internal turns.

Let \(T_b=(\ell_b,z_b,r_b)\) be a triangular ear and let \(x\) be strictly
inside \(T_b\). Along a convex ear, \(\alpha\) strictly decreases and
\(\beta\) strictly increases. Moreover \(\alpha(x)\) is a positive
denominator-weighted average of the three values of \(\alpha\) at the
vertices of \(T_b\); the same is true of \(\beta(x)\). Consequently

\[
 \alpha(\ell_b)>\alpha(x)>\alpha(r_b),\qquad
 \beta(\ell_b)<\beta(x)<\beta(r_b).                     \tag{7}
\]

If the same \(x\) is interior to both \(T_b\) and \(T_c\), then

\[
 \alpha(\ell_b)>\alpha(x)>\alpha(r_c),\qquad
 \beta(\ell_b)<\beta(x)<\beta(r_c).                     \tag{8}
\]

Equations (6) and (8) prove that
\(K\cup\{\ell_b,r_c\}\) is convex. This is a complete rectangle, not a
density statement, so there is no thinning loss. If every source label
\(x_a\) lies inside every triangle, (7) also proves both faces in (1a)
for every pair \((a,b)\).

## 2. Multiplication on independent carrier edges

Let \(e_1,\ldots,e_m\) be pairwise nonadjacent edges of \(K\), and put all
local data for role \(i\) strictly inside the exterior ear pocket of
\(e_i\). Replacing any collection of these edges by strict convex ear
chains preserves every old turn of \(K\). Thus the one-ear conclusion
multiplies independently, proving that every set (2) is convex.

All triangle vertices and source marks are physically role-labelled.
Reading the source and left endpoint in (2a), or the left and right
endpoints in (2), reconstructs the corresponding two words. The local and
global decoder loads are one.

For source word \(a\in[A]^m\) and target word \(b\in[A]^m\), the union
contains, in every role \(i\), the circuit

\[
                         x_{i,a_i}+T_{i,b_i},            \tag{9}
\]

with \(x_{i,a_i}\) hidden by the triangle. At a fixed role its \(A\)
possible released traces are pairwise disjoint. Every trace occurs in
\(A^{2m-1}\) records, so the exact weighted dispersion is

\[
            {A^{2m}\over A^{2m-1}}=A,                  \tag{10}
\]

and the trace matching number is \(A\). The calculation repeats at every
remaining role. This is precisely the high-transversal regime left open
by
`../agent_outer_internal_product/LIVE_ROOT_TRANSVERSAL_ENTROPY_GATE.md`,
but here (2) pays it completely.

## 3. Context-retaining Hall form

The argument is global across varying carriers as long as the carrier mark
is literally retained. Let \(\mathcal K\) be any family of actual carrier
states. For \(K\in\mathcal K\), suppose there are \(b_K\) triangular ears
in one marked gap, with one common hidden pocket, and \(m_K\) selected
records assigned to this fibre.

First suppose that every record has a physical source mark \(x\), the pair
\((x,T_b)\) recovers the record inside its \(K\)-fibre, and \(x\) lies in
the common pocket. Send it directly to

\[
                              K\cup\{\ell_b,x\}.          \tag{11a}
\]

This is an ordinary face by (7), and it retains all three decoder
coordinates \(K,x,b\). Hence

\[
                \boxed{\displaystyle
                \sum_{K\in\mathcal K}m_K\le\lambda V(P),} \tag{11b}
\]

where \(\lambda\) is the literal carrier-mark load. There is no square
threshold in this source-primitive case.

If the physical hidden mark does **not** recover the full record, the
endpoint-only bank still applies whenever

\[
                              m_K\le b_K^2.              \tag{11}
\]

Choose a canonical injection from the records over \(K\) to ordered pairs
of its triangles. Send a record assigned to \((T_b,T_c)\) to

\[
                              K\cup\{\ell_b,r_c\}.       \tag{12}
\]

The one-ear lemma makes (12) an ordinary face. If the output recovers the
carrier state \(K\) and the two endpoint roles, this map is injective.
Therefore

\[
                \boxed{\displaystyle
                \sum_{K\in\mathcal K}m_K\le V(P).}      \tag{13}
\]

More generally, if one output has at most \(\lambda\) carrier-state
decodings, the right side is \(\lambda V(P)\). Differently named histories
with the same physical \(K\) must first be coalesced, while distinct
retained carrier faces or marked gaps cost no additional factor.

There is a stronger root-retaining version. Fix one physical hidden mark
\(x\) and let \(T_1,\ldots,T_b\) be all the triangular ears in its carrier
fibre which contain \(x\). Equations (7)--(8) show that

\[
                       K\cup\{\ell_i,x,r_j\}             \tag{13a}
\]

is an ordinary face for every ordered pair \(i,j\in[b]\). The output
retains the carrier, the hidden mark, and both triangle labels. Thus one
fibre supplies \(b^2\) rooted endpoint-module faces with load one. Unlike
the endpoint-only output (12), it cannot collide merely because different
hidden roots share the same triangles.

Thus a concentrated one-chamber family is paid unless it has genuine
same-carrier, nonprimitive load

\[
                              m_K>b_K^2.                 \tag{14}
\]

The inequality is sharp for an endpoint-only decoder. Below the square, the
two endpoint labels store the entire record name, even if the hidden
source is absent from the output. Above the square, no theorem using only
those two labels can be injective. The remaining high-load fibre must use
an additional actual source/profile coordinate or expose another bank.

For the balanced proposed gadget, (11a) applies directly because
\((x_{i,a},T_{i,b})\) is the literal record. It also has
\(m_K=A^2=b_K^2\), so the weaker endpoint-only theorem (13) applies at
equality. Multiplying independent marked gaps gives (3).

## 4. Global two-bank saving

The rooted modules give an exact global Hall inequality. Index the physical
carrier/root fibres by \(g\), let \(b_g\) be the number of triangular trace
occurrences in fibre \(g\), and put

\[
                    T=\sum_g b_g,\qquad B=\sum_g b_g^2. \tag{15}
\]

Let \(\mathcal S\) be the set of actual old-source faces used by the
records, \(S=|\mathcal S|\), and assume that the pair consisting of a
source face and a literal trace occurrence has record load at most
\(\delta\). Then

\[
                              M\le\delta ST.             \tag{16}
\]

Suppose every rooted output (13a) has at most \(\lambda\) carrier
decodings. The source bank and rooted-module bank give

\[
                         V(P)\ge S,\qquad V(P)\ge B/\lambda.
\]

Splitting according as \(S\ge B/\lambda\) or \(S\le B/\lambda\) yields

\[
 \boxed{\displaystyle
                         M\le
                    \delta\lambda\,{T\over B}\,V(P)^2.} \tag{17}
\]

Indeed, in the first case
\(ST\le(\lambda T/B)S^2\), and in the second
\(ST\le(\lambda T/B)(B/\lambda)^2\).

Consequently, if every nonempty active fibre has \(b_g\ge h\), then
\(B\ge hT\) and

\[
 \boxed{\displaystyle
                         M\le{\delta\lambda\over h}V(P)^2.} \tag{18}
\]

This is a fixed-power live saving as soon as \(h\ge n^\varepsilon\) and
\(\delta\lambda=n^{o(1)}\). It does not require the old source to be a
singleton, nor does it require the rooted module itself to encode the full
source. The two ordinary banks are the actual source faces and the
root-retaining endpoint modules.

For the proposed balanced gadget, take one fibre for each physical source
mark. Every fibre has \(b_g=A\), so (18) gains the full factor \(A\).
Equivalently, in each role the explicit ordinary bank

\[
              \{\ell_b,x_a,r_c:a,b,c\in[A]\}            \tag{19}
\]

has size \(A^3\), against only \(A^2\) source--target records.

## 5. What remains

At a live high-dispersion chronology level, a polynomial family of
disjoint released triangles cannot all occupy independent retained carrier
edges with a common hidden pocket. Otherwise their first/last endpoint
product gives the load-one bank (2).

Accordingly the remaining direction-circle split must retain the actual
carrier/context mark. If many traces share one literal carrier chamber,
the context-retaining theorem closes every source-primitive fibre by
(11b), and every nonprimitive fibre up to the exact square threshold (11).
The concentrated survivor must have repeated full source/history records
over the same \((K,x,T)\), or mass above the endpoint square. If chamber
support is diffuse, deleting a trace can erase the carrier name, and no
decoder follows merely from the number of chambers.
A valid continuation must either build a cyclic profile bank from those
varying physical seams or show that one chamber has high weighted load.
This report does not assert that strong separation supplies such a chamber.

## 6. Verification

Run

~~~text
python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_high_transversal_common_pocket_endpoint_product.py
~~~

The verifier uses two opposite nonadjacent edges of an exact rational
quadrilateral and \(A=3\). It checks general position, all source and
target words, all \(81\) bad source--target records, the six disjoint
released triangles, the exact dispersion \(h=3\) at both chronology
levels, all \(3^4=81\) cross-endpoint faces with decoder load one, and the
global and one-role source--left-endpoint injections. It exhausts the
root-retaining modules (19), obtaining \(3^6=729\) global and \(54\)
one-role outputs, and checks the two endpoint-only context injections at
the sharp square threshold \(m_K=b_K^2=9\).
