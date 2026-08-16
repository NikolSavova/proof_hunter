# All-loop normal form does not force a side-respecting strong-glue chamber

**Date:** 2026-08-15. This attacks the minimizer-specific bridge left by
the Pascal all-loop regression.

## Verdict

Fixed signed singleton-by-triple circuits do **not** force the source and
target sides into a strong-glue chamber, even after subquadratic thinning.

There is an exact scalable rational construction with:

* \(m\) source roles of alphabet size \(A\);
* \(k\) target roles of alphabet size \(A\), plus three fixed anchors;
* \(A^m\) convex full source transversals and \(A^k\) convex full target
  transversals;
* every nonempty partial source transversal incompatible with every target
  transversal;
* one fixed signed \(1+3\) circuit for every incompatibility: the same
  target anchor is hidden by the same two target anchors and any retained
  source label; and
* every line through labels from two distinct source roles has fixed target
  anchors on both sides.

The last property forbids any strong-glue split which keeps the source
cloud on one side and the target cloud on the other while retaining two
source roles. Consequently a side-respecting strong-glue extraction has at
most

\[
                         (1+mA)A^k                                \tag{1}
\]

distinct source-target outputs, versus the full bad rectangle

\[
                         A^{m+k}.                                 \tag{2}
\]

For

\[
             m=\lfloor\alpha\log A\rfloor,\qquad
             k=\lfloor\beta\log A\rfloor,                         \tag{3}
\]

the loss is

\[
 \frac{A^{m+k}}{(1+mA)A^k}
   =2^{(\alpha-o(1))(\log A)^2}.                                 \tag{4}
\]

This is quadratic-exponential, not polynomial or \(2^{O(\log n)}\).
Thus the all-loop predicate cannot be promoted to a useful strong-glue
reset by line-arrangement thinning, signed-circuit homogenization, or
one-point extension typing alone.

The construction remains valid when every macro source/target role is
replaced by an arbitrary rational planar child and only singleton
transversals are selected. Therefore the obstruction is not caused by
nonstretchability or by a finite four-point anomaly.

This is a local classification barrier, not a sub-half construction. The
two separate transversal banks are ordinary, and arbitrary child
substitution may create large one-gap/profile banks. A minimizer-specific
theorem can still rule out the configuration by charging those ambient
banks. What is false is the direct implication

\[
 \text{complete fixed-sign all-loop rectangle}
 \Longrightarrow
 \text{source--target strong-glue chamber at subquadratic loss}.  \tag{5}
\]

## 1. Rational macro construction

Fix \(m\ge2\), put

\[
 R=10,\qquad \delta=\frac1{10},\qquad
 \eta=\frac1{100m^2},                                             \tag{6}
\]

and take target anchors

\[
                   a=(-R,0),\qquad b=(0,1),\qquad c=(R,0).        \tag{7}
\]

The source macro roles lie on a tiny strictly convex parabola above \(b\):

\[
                   d_i=(\eta i,\,1+\delta+\eta i^2),
                   \qquad1\le i\le m.                            \tag{8}
\]

For the additional target roles choose distinct rational
\(-R<t_s<R\) and put

\[
                   u_s=\left(t_s,\frac{t_s^2-R^2}{R^2}\right),
                   \qquad1\le s\le k.                            \tag{9}
\]

The points \(a,u_1,\ldots,u_k,c\) lie on a strictly convex lower
parabola, while \(a,b,c\) form the upper chain. Hence

\[
                         \{a,b,c,u_1,\ldots,u_k\}                 \tag{10}
\]

is in convex position. The source macros (8) are also in convex position.

Replace every \(d_i\) and \(u_s\) by an \(A\)-point cluster in a
sufficiently small rational neighborhood. The cluster can be an
arbitrarily prescribed rational order type, after an affine rescaling.
There are only finitely many strict macro determinants, so one common
rational scale preserves:

* convexity and cyclic type of every one-label-per-role source
  transversal;
* convexity and cyclic type of every target transversal retaining
  \(a,b,c\); and
* all circuit and straddling inequalities proved below.

This is the standard lexicographic blow-up argument, but no strong-glue
sign is imposed inside or between the clusters.

## 2. One fixed signed loop blocks every record

For \(d=(x,y)=d_i\), the anchor \(b\) lies in
\(\operatorname{int}\operatorname{conv}\{a,c,d\}\) exactly when

\[
                         |x|<R(y-1).                              \tag{11}
\]

Here

\[
 |x|\le\frac1{100m},\qquad
 R(y-1)\ge R\delta=1,                                             \tag{12}
\]

so (11) holds with a fixed positive margin. It therefore holds for every
label \(x\) in every sufficiently small source cluster:

\[
                         b\in\operatorname{int}
                         \operatorname{conv}\{a,c,x\}.            \tag{13}
\]

Thus \(\{a,b,c,x\}\) is always the same signed \(1+3\) circuit, with the
same hidden target label \(b\).

Every target word contains \(a,b,c\). Every nonempty partial source word
contains some \(x\). Their union contains (13), hence is nonconvex. This
proves the complete bad rectangle, including every source deletion
history until the source trace is empty.

Notice that this is the external-loop sign of the Pascal strong-glue
example: the singleton source label is not hidden; one fixed point of the
target triple is hidden.

## 3. The target straddles every cross-role source line

For \(i<j\), the line through the macro points \(d_i,d_j\) has slope
\(i+j\) and equation

\[
          \ell_{ij}(x)=1+\delta-\eta ij+(i+j)x.                    \tag{14}
\]

At the three target anchors,

\[
\begin{aligned}
 \ell_{ij}(0)&>1,\\
 \ell_{ij}(-R)&<0,\\
 \ell_{ij}(R)&>0.
\end{aligned}                                                     \tag{15}
\]

Hence \(a\) is strictly above the line while \(b,c\) are strictly below
it. The margins are uniform in \(1\le i<j\le m\), so after sufficiently
small cluster blow-up:

> for every \(x\in X_i\), \(y\in X_j\) with \(i\ne j\), the fixed target
> anchors are not contained in one open halfplane bounded by \(xy\).

This is invariant under every affine or projective rechart.

A necessary condition for a strong-glue split
\[
                         S\prec T\quad\text{or}\quad T\prec S      \tag{16}
\]

is that, for every pair of labels in \(S\), all labels of \(T\) lie on
one fixed side of their line. It is exactly the uniform \(2+1\)
orientation condition. Taking \(S\) from the source roles and
\(T\) containing \(a,b,c\), (15) shows that \(S\) can meet at most one
source role.

This obstruction is stronger than mixed adjacent seams: it applies to
every pair of distinct source roles and survives every projection chamber.

## 4. Exact entropy loss

The full source alphabet has \(A^m\) full words. Allowing arbitrary partial
words gives \((A+1)^m\), but a side-respecting strong split may retain
labels from at most one source role. Its entire distinct partial-word
alphabet is therefore bounded by

\[
                         1+mA.                                   \tag{17}
\]

The target side still has \(A^k\) words, giving (1).

With total point count

\[
                         n=(m+k)A+3,                              \tag{18}
\]

choice (3) has \(\log n=(1+o(1))\log A\). Hence

\[
\begin{aligned}
 \log A^m&=(\alpha+o(1))(\log n)^2,\\
 \log A^k&=(\beta+o(1))(\log n)^2,\\
 \log\frac{A^m}{1+mA}
   &=(\alpha-o(1))(\log n)^2.                                   \tag{19}
\end{aligned}
\]

No polynomial decoder load can restore the discarded source history:
after collapse there are only \(1+mA\) actual ordinary source outputs.

Thus even a complete live two-family all-loop cell need not contain a
side-respecting strong-glue subcell of comparable quadratic entropy.

## 5. Scope of the barrier

There is a decisive global limitation on this example.  Its released-side
bad circuits all have the same hereditary physical root

\[
                              T=\{a,b,c\}.
\]

Consequently the fixed-root corollary of
`../agent_outer_internal_product/LIVE_ROOT_TRANSVERSAL_ENTROPY_GATE.md`
applies verbatim.  If the selected record mass is \(M\), the endpoint-pair
load is \(\delta\), and the ambient ordinary-face count is \(V\), then

\[
                    M\le 2\delta V\,2^3 3!=96\delta V. \tag{20}
\]

Thus the construction cannot occur on a live slice with
\(M\asymp V^2/2^{O(L\log L)}\).  Equivalently, when its local parameters
are scaled to quadratic transversal entropy, ordinary ambient banks must
explode enough to pay the fixed rooted rectangle.  The construction is a
sharp kill of the proposed **local classification** from circuit signs to
side-respecting strong glue, not a live-normalized counterexample.

The theorem rules out classification from:

* all singleton-by-triple circuit signs, even with one common physical
  circuit and one common hidden label;
* all one-point extension cells of source labels relative to the target;
* complete source deletion chronology;
* stretchability and general position; and
* quadratic source and target transversal entropy.

It does not rule out:

* a global Cauchy charge using the two detached transversal banks;
* a one-gap or directional-profile bank created by the role blow-ups;
* a theorem using the fixed-gap minimizer inequality; or
* an interleaved decomposition which does not keep the source and target
  alphabets on opposite sides.

The last item would need a new decoder: the live multiplication step
requires the actual source and target alphabets to remain recoverable as
the two factors. The strong-glue reset presently proposed is
side-respecting, so (15)--(19) are the relevant obstruction.

## 6. Verification

Run

    python3 phase2/loop/erdos838/agent_shield_circuit_cover/verify_all_loop_nonstrong_transversal_barrier.py

The exact rational verifier uses \(m=3\), \(k=2\), and \(A=2\). It checks:

1. general position of all 13 points;
2. all eight source and four target full words are ordinary;
3. all 26 nonempty partial source words times all four target words are
   bad through the same hidden anchor \(b\);
4. all 12 cross-role source pairs have target anchors on both sides; and
5. the side-respecting source alphabet collapses to \(1+mA=7\).

Expected output:

    PASS: fixed signed all-loop rectangle with convex source/target words; Dwords=8, Uwords=4, partials=26, bad_pairs=104, straddled_cross_role_pairs=12, one-role_collapse=7
