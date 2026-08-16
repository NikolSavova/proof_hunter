# Live dense completion cores transfer normalization to both face sides

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The live dense \(D\)-versus-\(U\) Hall core is substantially more rigid
than an arbitrary face rectangle: its normalization transfers to both
vertex alphabets.

Let \(\mathcal R\) be weighted release records with two ordinary targets

\[
                         D_\omega,\qquad U_\omega,      \tag{1}
\]

where the ordered pair recovers the literal geometric record.  Suppose
every fixed pair has weight at most \(\delta\).  If the Hall density is
\(\eta\), then for every \(K<\eta\) there is a nonempty core of minimum
weighted target degree greater than \(K\), and each side of that core has
more than

\[
                              {K\over\delta}            \tag{2}
\]

distinct actual faces.

Apply this to the rank-\(s\) fixed-label core from
EXCESS_RANK_FIXED_LABEL_DOWNSHADOW_GATE.md.  If

\[
\begin{aligned}
 W&\ge V(P)/\Xi,\\
 M_s&\ge WH/\Gamma,\\
 H&\ge V(P)/\Theta,
\end{aligned}                                          \tag{3}
\]

then its Hall density obeys

\[
                         \eta\ge {sH\over2N\Gamma\Xi}.  \tag{4}
\]

Taking \(K=\eta/2\) gives two distinct face families
\(\mathcal D_*,\mathcal U_*\) satisfying

\[
 \boxed{\quad
 |\mathcal D_*|,|\mathcal U_*|
 \ge {sV(P)\over4N\Gamma\Xi\Theta\delta}.
 \quad}                                                \tag{5}
\]

On the live rank-safe slice,

\[
 N\le n,\qquad
 \Gamma\Xi\Theta\delta=2^{O(L\log L)},\qquad L=\log n,
                                                               \tag{6}
\]

so both sides have size \(V(P)2^{-O(L\log L)}\).  In particular the
completion faces, not merely the original sources, form another
live-normalized family.

Every member of \(\mathcal D_*\) contains the fixed label \(x\).  Delete
that common label; heredity gives an injective family of ordinary
rank-\((s-1)\) faces.  After the \(e^{-(s-1)}\) unordered role-colouring
loss, the exact four-local/projection theorem applies to a retained family
\(\mathcal E\subseteq\{D-\{x\}:D\in\mathcal D_*\}\).  If its role box has
volume \(P_0\) and redundancy

\[
                         R_D=\log(P_0/|\mathcal E|),    \tag{7}
\]

then the following two exact dichotomies hold.

1. **Four-local dichotomy.**  Either at least \(P_0/2\) ambient completion
   words are ordinary, in which case (5) forces

   \[
                         R_D=O(L\log L).                \tag{8}
   \]

   Or four physical completion roles contain a polynomial-density box of
   one fixed signed \(1+3\) circuit type.
2. **Projection-entropy dichotomy.**  Independently, a large one-gap term
   produces its ordinary extension bank, while a large blocker term fixes
   a physical completion role and a canonical source triple blocking a
   polynomial fraction of that role alphabet.  At the present
   \(2^{O(L\log L)}\) normalization loss, the fixed-power one-gap gain
   need not close the family.

Thus the live core cannot remain a featureless high-redundancy alphabet:
quadratic completion redundancy forces the four-local physical box, while
the projection split separately measures one-gap versus rooted-blocker
entropy.  This is an unconditional reduction, but not the desired
composition theorem: none of these conclusions forces the new ordinary
faces or blocker labels to coexist with the released family
\(\mathcal U_*\).

The missing coupling is sharp.  In a strongly separated two-cloud chart,
let \(R(Y)\) and \(A(Z)\) be the two facing directional profiles.  The
exact mixed bank is

\[
                    \mathcal R(Y)\times\mathcal A(Z),  \tag{9}
\]

so for selected side families
\(\mathcal D\subseteq\mathcal F(Y)\) and
\(\mathcal U\subseteq\mathcal F(Z)\),

\[
 V(P)\ge
 |\mathcal D\cap\mathcal R(Y)|\,
 |\mathcal U\cap\mathcal A(Z)|.                       \tag{10}
\]

Even when both selected families have the live sizes in (5), planarity
alone gives no lower bound on either selected profile intersection.
The anti-aligned rank-\(s\) parabolic clouds make both intersections zero
and attain the complete incompatible rectangle.  They are not live,
because their detached Boolean banks dwarf the bounded-rank alphabets.
The arbitrary-child nested construction shows that this anti-alignment is
projectively robust locally, but does not upper-bound the full recursively
assembled face complex.

Consequently the exact remaining statement is a **live profile
penetration theorem**:

> a rank-\(O(L)\) face family of size
> \(V(P)2^{-O(L\log L)}\), occurring as one side of the normalized dense
> Hall core, must put enough mass in the actual facing profile, or its
> avoided profile direction exposes another detached/composition bank
> with globally controlled overlap.

No such theorem is proved here, and no scalable live regression is
known.  The report rules out an arbitrary set-system/downshadow residue
and isolates the genuinely geometric normalization interface.  No
fixed-power or coefficient-half conclusion is claimed.

## 1. Weighted Hall pruning and distinct-side transfer

For a weighted record family with target sets
\(\{D_\omega,U_\omega\}\), define

\[
 \eta=\max_{\varnothing\ne\mathcal R'\subseteq\mathcal R}
 {\sum_{\omega\in\mathcal R'}w_\omega\over
  |\{D_\omega:\omega\in\mathcal R'\}
       \cup\{U_\omega:\omega\in\mathcal R'\}|}.         \tag{11}
\]

If \(\eta>K\), choose a witness and repeatedly delete a target vertex of
current incident weight at most \(K\), together with all incident
records.  If all vertices disappeared, charging a record to its first
deleted endpoint would bound the witness weight by \(K\) times its target
count, a contradiction.  This proves the nonempty minimum-degree core.

At one target vertex, each distinct opposite neighbour contributes pair
weight at most \(\delta\).  Weighted degree greater than \(K\) therefore
requires more than \(K/\delta\) distinct neighbours.  Both vertex sides
have that many members, proving (2).

In the fixed-label completion bucket, the preceding report proves (4).
Use \(K=\eta/2\), substitute \(H\ge V/\Theta\), and apply (2).  This gives
(5).  Notice that the full completion target \(D\) is retained.  Replacing
it by \(B\cup\{x\}\) would lose the completion word and invalidate the
pair cap \(\delta\).

The parameter \(N\) costs only one polynomial factor.  Under (6),

\[
 {4N\Gamma\Xi\Theta\delta\over s}=2^{O(L\log L)},      \tag{12}
\]

so (5) is exactly the live-normalization scale, not merely an absolute
large-family statement.

## 2. Four-local completion on the transferred left family

Delete the common \(x\) from every distinct \(D\in\mathcal D_*\), and
give the resulting distinct ordinary faces unit weight.  Apply unordered
injective role colouring.  Since \(s=O(L)\), one colouring retains at
least

\[
 { (s-1)!\over (s-1)^{s-1}}|\mathcal D_*|
                 \ge e^{-(s-1)}|\mathcal D_*|.         \tag{13}
\]

The loss is \(2^{O(L)}\), absorbed by (12).  Let
\(X_1,\ldots,X_{s-1}\) be the resulting pairwise disjoint physical role
supports and \(P_0=\prod_i|X_i|\).

Write \(M_D=|\mathcal E|\).  The four-local completion theorem says either
at least \(P_0/2\) ambient
words are ordinary, or four roles have nonconvex transversal density at
least \(1/(2\binom s4)\).  In the first case,

\[
             V(P)\ge P_0/2
               ={M_D\over2}\,2^{R_D}.                  \tag{14}
\]

Combining (14) with the lower bound
\(M_D\ge e^{-s}|\mathcal D_*|
       \ge V(P)2^{-C L\log L}\) proves (8).

In the second case, split by the interior role and apply fixed-arity
semialgebraic regularity.  Four subsets of the physical role supports
form a complete box of one signed \(1+3\) circuit, with relative product
size at least a fixed power of \(1/\operatorname{poly}(s)\).  This is an
actual label box, not a face-alphabet projection.

Independently, the missing-coordinate entropy theorem gives

\[
                         R_D\le G+B,                   \tag{15}
\]

and the ordinary one-coordinate extension bank gives

\[
                         {V(P)\over M_D}
                                  \ge2^{G/s}.           \tag{16}
\]

Equation (16) only implies
\(G\le s\,O(L\log L)\) from the live lower bound on \(M_D\).  Since
\(s=O(L)\), this can exceed the total possible \(O(L^2)\) redundancy and
is generally vacuous.  Thus a quadratic \(G\) gives a genuine fixed-power
one-gap bank but may still be swallowed by the quasipolynomial
normalization loss.  If instead \(B\) carries a specified positive share
of \(R_D\), the blocker theorem produces a physical role and canonical
source triple with the stated polynomial-density blocked alphabet.
Equations (14)--(16) give exact local alternatives, not a global closure.

These operations are all internal to the completion support.  A bad
four-role ambient box does not say which released faces use it; an
ordinary one-gap extension need not coexist with a released face.
This is why the reduction stops before a mixed bank.

## 3. Exact strongly separated profile interface

Suppose two disjoint point sets \(Y,Z\) occur in a lexicographically
strongly separated chart.  Call an ordinary nonempty face of \(Y\) a
right profile if adjoining one point from the \(Z\)-cell remains convex,
and define left profiles of \(Z\) symmetrically.  The two-block
classification gives exactly

\[
 V(Y\cup Z)=V(Y)+V(Z)-1+R(Y)A(Z),                     \tag{17}
\]

where the subtraction corrects the twice-counted empty face under the
convention that \(V\) includes it.

Every pair

\[
 (D,U)\in
 (\mathcal D\cap\mathcal R(Y))
 \times(\mathcal U\cap\mathcal A(Z))                  \tag{18}
\]

has ordinary union.  The disjoint support traces recover both factors,
so these are distinct mixed faces and (10) follows.

If \(|\mathcal D|,|\mathcal U|\ge V(P)/\Lambda\), then (10) only gives

\[
 {|\mathcal D\cap\mathcal R(Y)|\over|\mathcal D|}
 {|\mathcal U\cap\mathcal A(Z)|\over|\mathcal U|}
 \le {\Lambda^2\over V(P)}.                            \tag{19}
\]

Thus a core with almost no ordinary cross pairs may put one or both live
families almost entirely outside the facing profiles.  Equation (19) is
a localization, not a contradiction.

## 4. Exact nonlive regression and the realizability gate

Take opposite pure parabolic clouds \(Y,Z\), each with \(p\) points, in
the anti-aligned chart.  Both facing profiles consist exactly of ranks
one and two.  Fix \(x\in Y\).  For \(3\le s\le p\), set

\[
 \mathcal D=\{D\in{Y\choose s}:x\in D\},\qquad
             \mathcal U={Z\choose s}.                 \tag{20}
\]

Both intersections in (18) are empty, every pair in
\(\mathcal D\times\mathcal U\) has nonordinary union, and its Hall graph
is
\(K_{\binom{p-1}{s-1},\binom ps}\).  The complete face count is

\[
 V(Y\cup Z)
   =1+2(2^p-1)+
      \left(p+\binom p2\right)^2.                      \tag{21}
\]

For \(s=O(\log n)\), \(n=2p\),

\[
 \log\binom ps=O((\log n)^2)=o(p)=\log V(Y\cup Z)-O(1),             \tag{22}
\]

so neither side satisfies (5).  This is the exact reason the natural
anti-aligned stress test is not a live regression.

The projective nesting theorem permits an arbitrary rational order type
inside one cloud while preserving the total two-sided blocker geometry.
It proves that local circuit signs cannot force profile penetration.
However, its trace-complex upper bound omits multi-label role faces and
other macro masks; it is not an upper bound on the full recursive face
complex.  Therefore it does not produce a scalable family satisfying
(3), and it cannot be promoted to a live regression.

## 5. Scope

The new unconditional statement is the normalization transfer (5).
Together with the established four-local/projection theorem it reduces
the completion side to low redundancy, a physical four-role circuit box,
or a physical rooted blocker alphabet.  The exact unsolved step is to
couple one of those structures to the simultaneously live released side.

A proof of live profile penetration would close this interface.  A
counterexample must recursively realize two bounded-rank face families
of near-total face mass while keeping their facing profile product below
that mass, and must include every ambient multi-label/mask face.  The
existing anti-aligned and arbitrary-child constructions do not meet that
standard.

## Verification

Run

    python3 phase2/loop/erdos838/agent_outer_internal_product/verify_live_dense_completion_profile_gate.py

The verifier checks weighted Hall pruning and distinct-neighbour transfer,
the normalization arithmetic, the exact two-cloud recurrence, the
anti-aligned rank-face Hall rectangle, and the Boolean-bank normalization
gap.
