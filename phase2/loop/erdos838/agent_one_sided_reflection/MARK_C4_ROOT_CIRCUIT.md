# Singleton mark graphs: common-core rectangles or a rooted circuit shadow

## Verdict

The genuine singleton-ear residual has an exact local $C_4$ dichotomy.
For a convex retained core $R$, every repair record

\[
 (R,x,p),\qquad A=R\cup\{x\},\quad T=R\cup\{p\},
 \quad\operatorname{ext}(A\cup\{p\})=T,                \tag{1}
\]

canonically identifies one edge $uv$ of $R$.  Both $x$ and $p$
insert through $uv$, and

\[
                         x\in\operatorname{int}
                         \operatorname{conv}\{u,v,p\}. \tag{2}
\]

Thus $\{u,v,x,p\}$ is a rooted $1+3$ circuit.

If four records with the same core form a mark rectangle

\[
                         \{x_1,x_2\}\times\{p_1,p_2\}, \tag{3}
\]

then all four marks use the same edge $uv$.  There are exactly two cases.

1. Both same-side pairs are insertion-incomparable.  Then
   $R\cup\{x_1,x_2\}$ and $R\cup\{p_1,p_2\}$ are ordinary convex faces,
   and their ordered pair recovers the rectangle injectively.
2. At least one same-side pair is nested.  Its inner point $a$ and outer
   point $b$ give the canonical circuit
   $a\in\operatorname{int}\operatorname{conv}\{u,v,b\}$.  Every other
   point of $R$ lies on the opposite side of $uv$.  The rectangle is
   localized to one detached rooted shield component.

Consequently the total number of good common-core rectangles is at most

\[
                               V(P)^2.                  \tag{4}
\]

Every excess rectangle is canonically charged to a rooted nesting circuit.
This is the requested planar circuit/tangent localization.  It is not by
itself a fixed-power closure: strict insertion chains make every rectangle
bad, and their detached tip order type is projectively universal.

There is a scalable full-ACP regression.  Take $2^k$ Boolean upper-cap
cores sharing $uv$, an $a$-point inner insertion chain $X$, and a
$b$-point outer chain $Y$.  Every $p\in Y$ repairs every
$R\cup\{x\}$, so

\[
 |E|=2^k a b,\qquad \lambda(x,p)=2^k,\qquad G_R=K_{a,b}. \tag{5}
\]

All $C_4$'s take the circuit branch.  A scalable rational realization
has two conspicuous detached shields: the upper cap has $2^k$ faces and
the discarded mark cap has $2^{a+b}$ faces.  Hence it is not an EIC
counterexample.  Projective universality can replace the discarded cap by
an arbitrary planar order type without changing a single ACP record; doing
so turns the missing product into the unrestricted face problem.  The
regression therefore identifies the exact remaining theorem: aggregate the
rooted circuit shadows across genuinely varying cores and marks, rather
than proving another local insertion-chain bound.

Exact verifier:

    python3 phase2/loop/erdos838/agent_one_sided_reflection/verify_mark_c4_root_circuit.py

## 1. The three projections and the exact Loomis--Whitney barrier

Let \(\mathcal E\subseteq\mathcal R\times X\times Y\) be the selected
singleton-ear records and write

\[
 \Pi_S=\{(R,x):(R,x,p)\in\mathcal E\},\quad
 \Pi_T=\{(R,p):(R,x,p)\in\mathcal E\},\quad
 \Pi_M=\{(x,p):(R,x,p)\in\mathcal E\}.                 \tag{H1}
\]

These are the source, repaired-target, and rank-two mark projections.
If sources and targets have rank at most \(r+1\), then

\[
 |\Pi_S|\leq(r+1)V(P),\qquad
 |\Pi_T|\leq(r+1)V(P),\qquad
 |\Pi_M|\leq V(P).                                     \tag{H2}
\]

For example, a source face \(A\) has at most \(|A|\) representations
\(A=R\cup\{x\}\); the other bounds are identical or immediate.
The discrete Loomis--Whitney inequality gives

\[
 |\mathcal E|^2\leq|\Pi_S||\Pi_T||\Pi_M|
                    \leq(r+1)^2V(P)^3.                 \tag{H3}
\]

The tensor regression of Section 4 attains equality in the first
inequality.  With \(M=2^k\) cores and complete mark alphabets of sizes
\(a,b\),

\[
 |\mathcal E|=Mab,\quad
 |\Pi_S|=Ma,\quad |\Pi_T|=Mb,\quad |\Pi_M|=ab,
\quad |\mathcal E|^2=|\Pi_S||\Pi_T||\Pi_M|.             \tag{H4}
\]

All four objects in (H4) are realized by actual planar ACP incidences and
ordinary faces.  Hence no abstract three-projection or entropy inequality
can yield the fixed-power EIC' saving.  One must use faces outside these
three projections.  The common-core rectangle theorem below supplies the
first such planar alternative.

## 2. The unique insertion edge

Let $R$ be a set in convex position and $q\notin R$ such that
$R\cup\{q\}$ is in convex position.  The two neighbours of $q$ in the
new polygon are consecutive vertices $u,v$ of $R$.  Call

\[
                              e_R(q)=uv               \tag{6}
\]

the insertion edge.  Removing $q$ replaces the two edges $uq,qv$ by
$uv$, and therefore

\[
 \operatorname{conv}(R\cup\{q\})-\operatorname{conv}(R)
 \subseteq\operatorname{conv}\{u,v,q\}.                \tag{7}
\]

> **Lemma 1 (a singleton repair preserves its insertion edge).** Every
> record (1) satisfies
> 
> \[
>                         e_R(x)=e_R(p)=uv
> \]
> 
> for one edge $uv$ of $R$, and (2) holds.

**Proof.** Since $R\cup\{x\}$ is convex,
$x\notin\operatorname{conv}R$.  Since $p$ hides $x$ and the configuration
is in general position,
$x\in\operatorname{int}\operatorname{conv}(R\cup\{p\})$.  If
$uv=e_R(p)$, (7) and $x\notin\operatorname{conv}R$ force $x$ into the
open triangle $uvp$.  A point in this open ear triangle, but outside
$\operatorname{conv}R$, inserts through the same edge $uv$.  Hence
$e_R(x)=uv$, proving the lemma.  QED.

General position makes $\{u,v,x,p\}$ a rooted $1+3$ circuit, canonically
selected by the insertion edge.  There can be other triangles of
$R\cup\{p\}$ containing $x$; no uniqueness among all rooted circuits is
claimed.

## 3. Common-core $C_4$'s

For a fixed core $R$, let $G_R\subseteq X\times Y$ contain $xp$ when
(1) is a selected record.  A simple rectangle is a choice of distinct
$x_1,x_2,p_1,p_2$ for which all four cross edges occur.

By Lemma 1,

\[
 e_R(x_i)=e_R(p_j)\qquad(i,j\in\{1,2\}).                \tag{8}
\]

The rectangle is connected, so (8) gives one common root edge $uv$.
For two completions $a,b$ through the same edge, exactly one of the
following holds:

* $a\in\operatorname{int}\operatorname{conv}\{u,v,b\}$;
* $b\in\operatorname{int}\operatorname{conv}\{u,v,a\}$;
* $R\cup\{a,b\}$ is convex.

This is immediate in the two endpoint tangent coordinates: containment is
strict reverse dominance, while incomparability exposes both points on the
new boundary chain.

> **Theorem 2 (rectangle face-or-circuit dichotomy).** A rectangle (3)
> either produces the two ordinary faces
> 
> \[
>       F_X=R\cup\{x_1,x_2\},\qquad
>       F_Y=R\cup\{p_1,p_2\},                           \tag{9}
> \]
> 
> or canonically produces a rooted circuit
> 
> \[
>       (uv;a,b),\qquad
>       a\in\operatorname{int}\operatorname{conv}\{u,v,b\}. \tag{10}
> \]

Choose the $X$-side first when both sides are nested, and use the ambient
label order to break the remaining tie.  Thus (10) is canonical.

If $X,Y$ are disjoint mark alphabets, the map from a good rectangle to
$(F_X,F_Y)$ is injective:

\[
 R=F_X\cap F_Y,qquad
 \{x_1,x_2\}=F_X-R,qquad
 \{p_1,p_2\}=F_Y-R.                                    \tag{11}
\]

This proves (4).  Without recoverable mark colours, guessing which output
is the $X$-face and the two pair assignments costs at most eight.

Writing

\[
 \operatorname{rect}(G_R)
   =\sum_{p<q}{d_R(p,q)\choose2},                        \tag{12}
\]

where $d_R(p,q)$ is the common $X$-degree, Theorem 2 gives the exact
aggregate alternative

\[
 \sum_R\operatorname{rect}(G_R)\leq V(P)^2+B,           \tag{13}
\]

where $B$ is the number of canonically rooted bad rectangles.  In
particular, every rectangle beyond the two-face budget contributes one
explicit circuit shadow, not an unspecified incompatible union.

## 4. The all-bad tensor regression

Normalize $u=(0,0),v=(1,0)$.  Put $k$ rational points on a strict upper
cap between the roots.  For every subset $S$ of that cap let

\[
                         R_S=\{u,v\}\cup S.             \tag{14}
\]

All $2^k$ cores are convex and retain the edge $uv$.

On the lower side use tangent coordinates $A>B$ and the inverse map

\[
                         z(A,B)=
 \left({A\over A-B},-{1\over A-B}\right).               \tag{15}

Choose a strict reverse-dominance chain

\[
 x_1\prec\cdots\prec x_a\prec p_1\prec\cdots\prec p_b, \tag{16}
\]

where $a\prec b$ means
$A_a>A_b$, $B_a<B_b$.  Then for every $S,i,j$,

\[
 \operatorname{ext}(R_S\cup\{x_i,p_j\})=R_S\cup\{p_j\}. \tag{17}
\]

Equation (5) follows.  Every same-side pair is nested, so Theorem 2 sends
every one of the

\[
                         2^k{a\choose2}{b\choose2}
\]

rectangles to (10), always with the same root edge $uv$.

For an explicit scalable choice, enumerate all $m=a+b$ marks by
$A_i=m+1-i$ and $B_i=-A_i^2$.  Then (16) holds.  The points
$(A_i,B_i)$ lie on a strict parabola, and the map (15) is projective with
positive denominator $A_i-B_i$ on every point.  It therefore preserves
their convex order type, so the mark points form a strict detached cap and
give $2^{a+b}$ ordinary faces.  Generic rational perturbations, if needed,
avoid all accidental collinearities while preserving these strict
inequalities.  The upper cap
independently gives $2^k$.  These are real shield payments and must not be
discarded when using the regression.  On the other hand, the projective
universality theorem allows the complete mark chain in (16) to have an
arbitrary prescribed planar face complex.  Thus neither shield alone
proves the required mixed $2^k a b$ bank in general; a valid continuation
must sum circuit-rooted core faces and detached mark faces without assuming
their coexistence.
