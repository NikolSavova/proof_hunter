# Least-counterexample re-audit of the long-run pair-star gate

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The planar construction in LONG_RUN_PAIR_STAR_INCIDENCE_BARRIER is a
correct local empty-incidence example, but it is **not** a globally live
least-counterexample barrier.  Its complete outside transversal bank has
the half-target exponent after an allowed constant change in the number of
roles.  In the exact six-point child regression, every outside word also
coexists with every child singleton, and each nonempty one-sided context
coexists with a constant fraction of the selected pair-star.

The hoped-for converse is also false at the level of heredity, four-local
obstructions, effective branching, and the literal weight floor.  A
complete role product can be moved polynomially below the target without
losing any branching.  More strongly, Section 3 gives an explicit
four-uniform independence complex whose **entire** face family is below the
target, while its weighted long-run record mass remains within

\[
             n^{\Theta(\log\log\log n)}
\]

of the target square and its carrier pair-star incidence graph is empty.

This is not asserted to be a planar order type.  Thus the exact surviving
gate is geometric: planar circuit elimination or stretchability must rule
out the color-class cage, or must create a mixed child/carrier face bank.  Local
mass normalization alone cannot do it.

> **Planar follow-up.**  The color-class cage is in fact ruled out
> immediately once planar four-locality is restored.  Because every
> cross-class four-set in the abstract complex is a face, unions of
> arbitrary internal planar faces are faces, so their counts multiply.
> Two near-\(n\) classes already beat the fixed-gap target, and the
> \(t\asymp L\) classes used below give exponent \(\Theta(L^3)\).
> Therefore Section 3 is only an abstract set-system warning, not the
> surviving planar obstruction.  The exact product and pruning theorems,
> and the resulting dense cross-circuit residue, are in
> PLANAR_CROSS_CLASS_PRODUCT_AND_CAGE_ELIMINATION.md.

## 1. The previous planar regression is globally paid

Write

\[
 L=\log n,\qquad L_2=\log L,\qquad L_3=\log L_2,
 \qquad \Phi_C(L)=\tfrac12L^2-CLL_2.                 \tag{1}
\]

The old construction has

\[
 m=\lfloor n/L_2\rfloor,
 \qquad D=\lfloor(n-m)/q\rfloor,
 \qquad q=\tfrac12L-(C-\tfrac12)L_2-B+O(1).         \tag{2}
\]

Since

\[
 \log D=L-L_2+1+o(1),
\]

its complete outside word bank has

\[
 \log D^q
 =\Phi_C(L)-(B-\tfrac12)L+O(L_2^2).             \tag{3}
\]

In particular, with the unshifted real value \(B=0\), the correction is
\(+L/2+o(L)\).  Integer or parity rounding changes (3) by only \(O(L)\),
and increasing \(q\) by a fixed number restores a positive linear margin.
Thus the allowed \(O(1)\) in the old display can make

\[
                       D^q\ge 2^{\Phi_C(L)}.          \tag{4}
\]

That ordinary word bank alone violates the proposed least-counterexample
inequality.  Moreover every full word coexists with each of the \(m\)
child singletons, so in any such chart

\[
                       V\ge mD^q.                    \tag{5}
\]

Consequently a genuine least counterexample must satisfy

\[
                       D^q<2^{\Phi_C(L)}/m            \tag{6}
\]

if this complete singleton-release chart survives.

The exact rational six-point instance makes the defect visible even before
asymptotics.  Its selected pair-star has size 13.  There are eight nonempty
partial contexts on either outside side.  The left side has 32 compatible
incidences out of 104, exactly four star faces per context; the right side
has 24 out of 104, exactly three per context.  All 16 full words coexist
with all six child singletons.  Only the full pair-star versus full-word
incidence is empty.

Hence the previous report's target-normalized record calculation and its
empty full-context incidence statement remain valid, but its claim to be a
globally live obstruction is retracted.

## 2. A planar persistent-carrier trace cage

There is a useful exact planar strengthening of the local obstruction.
Take

\[
 u=(-1,0),\qquad v=(1,0),\qquad w=(0,-2),             \tag{7}
\]

put an arbitrary projectively nested child sufficiently close to
\((0,-1)\), and put the outside role cells in short disjoint intervals on
the upper arc

\[
                         y=1-x^2,qquad -1<x<1.        \tag{8}
\]

For every partial outside transversal \(S\):

1. \(\{u,v,w\}\cup S\) is convex;
2. every child label \(y\) lies in the root pocket, so
   \(\{u,v,w,y\}\) is nonconvex;
3. the released carrier \(K_S=\{u,v\}\cup S\) is convex;
4. \(K_S\cup\{y\}\) is convex for every child singleton; and
5. \(K_S\cup\{y,z\}\) is nonconvex for distinct nested child labels
   \(y,z\).

Thus every carrier-retaining pair-star incidence is bad, for every partial
context, with carrier/context decoder load one.  If the child has \(H\)
faces and there are \(q\) roles of size \(D\), the visibly retained trace
bank has exact size

\[
                     H+(m+1)(D+1)^q.                 \tag{9}
\]

The verifier uses the old rational six-point child and four two-label
roles.  It checks general position and all five assertions for all 81
partial contexts; the selected star has size 13, its incidence count is
zero, and (9) equals \(55+7\cdot81=622\).

This does **not** give a planar subtarget point set.  Faces deleting \(u\)
or \(v\), and faces taking multiple labels from a role cell, are not
controlled by (9).  The example only proves that retaining the actual
carrier does not by itself repair the normalization gap.

## 3. A globally subtarget four-local barrier

This section is deliberately nonplanar.  The follow-up quoted above gives
an exact planar contradiction; it should not be used as a candidate
order-type barrier.

The following finite set-system construction isolates precisely what a
planar proof must add.

Use fixed anchors \(u,v,w\).  Use \(tg\) child labels, split into
\(t\) color classes of size \(g\), and use \(qD\) outside labels split
into \(q\) roles of size \(D\).  Let the faces be the
independent sets of the following family of bad four-sets:

* a four-set containing two labels from the same outside role;
* four child labels from the same child color class;
* a four-set containing at least two child labels and at least one outside
  label;
* \(\{u,v,w,y\}\) for every child label \(y\); and
* \(\{u,v,y,z\}\) for every distinct child pair \(y,z\).

This complex is hereditary and every set of rank at most three is a face.
Every root source \(\{u,v,w\}\cup S\), with \(S\) a full outside
transversal, is a face.  Every released carrier plus one child label,
\(\{u,v\}\cup S\cup\{y\}\), is a face.  But every carrier plus a child
pair is bad.  Therefore the pair-star incidence graph is empty.  At every
outside role, the effective branching ratio is exactly \(D\).

A child-only face chooses at most three labels from each color class.  Put

\[
 A_g=\sum_{j=0}^3\binom gj={g^3+5g+6\over6},
 \qquad H=A_g^t.                                      \tag{10}
\]

The maximum child-face rank is \(3t\).  Fix two labels \(o,p\) in the
first class.  The exact number of child faces containing this pair is

\[
                         J=(g-1)A_g^{t-1}.             \tag{11}
\]

Let

\[
                         Q=(D+1)^q.                   \tag{12}
\]

Every face belongs to one of four types: rank at most three; no child and
a partial outside transversal; one child and a partial outside
transversal; or a child face, with no outside label.  Hence

\[
 |\mathcal I|
 \le O(n^3)+8Q+7mQ+6H.                               \tag{13}
\]

The constants 8 and 7 count anchor subsets; the full anchor triple is
forbidden in the one-child term.  The polynomial term also absorbs the
bounded-rank exceptional cases.

Fix a sufficiently large constant \(B_0\), for example \(B_0=20\), and
choose

\[
\begin{aligned}
 m&=\lfloor n/L_2\rfloor,\\
 q&=\tfrac12L-(C-\tfrac12)L_2-B_0+O(1),\\
 D&=\lfloor(n-m)/q\rfloor.                             \tag{14}
\end{aligned}
\]

Choose \(t\) maximal subject to

\[
            \log H\le
            \Phi_C(L)-(L_3+B_0+2)L.                   \tag{15}
\]

Here \(g=\lfloor m/t\rfloor\).  Let the actual vertex count be
\(n'=3+tg+qD\).  Then \(n-n'=O(L)\), so
\(\log n'=L+o(1)\); replacing \(n\) by \(n'\) changes all the displayed
exponents by \(o(L)\), far below the margins used here.

Since \(\log A_g=3\log g-\log6+o(1)=3L-O(L_2)\), one
increment of \(t\) changes \(\log H\) by only \(O(L)\).  In particular,

\[
 t=(1/6+o(1))L,\qquad 3t=(1/2+o(1))L<2L.              \tag{16}
\]

Thus every selected child face obeys the actual rank-safe cap.
Then

\[
 \log Q=\Phi_C(L)-(B_0-\tfrac12)L+O(L_2^2),           \tag{17}
\]

and each term of (13) is strictly below \(2^{\Phi_C(L)}\) for all
sufficiently large \(n\).  Thus this is a genuinely global subtarget
complex, not merely a local record count.

Pair the fixed-pair star (11) with all full outside words and give every
record the literal weight \(1/n\).  Maximality in (15), together with
\(\log J=\log H-2\log g+O(1)\), yields

\[
\begin{aligned}
 \log M
 &=\log J+q\log D-L\\
 &\ge 2\Phi_C(L)-L L_3-O(L),                          \tag{18}
\end{aligned}
\]

so

\[
                 M\ge
 {2^{2\Phi_C(L)}\over n^{(1+o(1))L_3}}.               \tag{19}
\]

This has exactly the missing \(n^{\Theta(L_3)}\) scale while the entire
ambient face complex remains below target, and its child ranks are
strictly below \(2L\).

## 4. Exact consequence and remaining theorem

Equations (13)--(19) refute an attempted closure using only:

* hereditary downsets;
* bad witnesses of size four;
* near-uniform or complete effective branching;
* the \(1/n\) atom-weight floor;
* the rank-safe cap below \(2L\);
* a fixed recoverable carrier and context; and
* the mass-uniform sibling-ear versus fixed-edge-cage dichotomy.

They do not refute a planar theorem.  More strongly, the cross-class
product theorem now proves that they cannot be the convex four-sets of a
rank-three realization with the stated local face supply.

After the product theorem, the genuinely planar residue must instead have
many bad cross-class four-sets.  The exact vertex-cover pruning theorem
shows that each large class pair has a linear matching of disjoint bad
cross circuits.  What remains is to compose those matchings, at bounded
history load, into a mixed face or fixed-edge/cyclic shield.  See the
follow-up report.

The obsolete abstract obstruction would have simultaneously supported:

1. the complete outside transversal sources;
2. the fixed \(uv\) cage for every child pair; and
3. suppression of every mixed child/outside face bank.

It fails already because item 3 makes the internal class face banks
multiply.  The new globally normalized gate is the dense cross-circuit
matching residue, not this complete cross-compatible cage.

## 5. Verification

Run

    python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_long_run_least_counterexample_reaudit.py

The script checks:

* the exact old one-sided incidence counts and singleton escape;
* the rational planar persistent-carrier cage in general position;
* every face of a 17-vertex instance of the four-local complex;
* heredity, all rank-three faces, sources, releases, zero pair-star
  incidence, and exact branching; and
* the global exponent inequalities at four large dyadic values of \(L\).

It prints PASS.
