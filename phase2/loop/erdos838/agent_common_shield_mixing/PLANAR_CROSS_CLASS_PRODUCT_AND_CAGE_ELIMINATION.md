# Planar cross-class product and fixed-edge cage elimination

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

The complete cross-compatible color-class cage from
LONG_RUN_LEAST_COUNTEREXAMPLE_REAUDIT cannot occur in a planar
least counterexample.  An exact four-local product theorem makes arbitrary
internal face banks multiply.  At the live class size
\(g\asymp n/(L\log L)\), the proved quarter lower bound shows that just
two fully cross-compatible classes already exceed
\(2^{\Phi_C(L)}\) for the fixed-gap constant \(C=3\).  The proposed
\(t\asymp L\) abstract cage would instead have
\(\Theta(L^3)\) logarithmic face mass.

The exact weaker residue is now:

* every pair of large child classes has a cross-bad-four hypergraph with
  linear vertex-cover number, hence a linear matching of physically
  disjoint circuits; and
* in the homogeneous fixed-\(uv\) pocket, every caged child pair and every
  opposite-side outside label releases through exactly one endpoint.
  Equal endpoint colors amplify to an ordinary partial-transversal shield.

The latter bank has exact physical decoder load one, but a fixed child pair
supplies only the square root of the outside product.  It does not retain
an arbitrary rich child face or the omitted outside choices.  Thus it does
not yet close the global \(n^{\Theta(\log\log\log n)}\) deficit.  The
remaining operation is a bounded-history composition of the dense
cross-circuit matchings with the rich internal child bank.

## 1. Exact cross-class product theorem

Let \(P\) be a planar point set in general position, and let
\(Y_1,\ldots,Y_t\) be disjoint subsets.  Write \(\mathcal F(Y_i)\) for
the ordinary convex subsets of \(Y_i\).

> **Theorem 1 (four-local class product).**  Suppose every four-set
> \(Q\subseteq\bigcup_iY_i\) that meets at least two classes is convex.
> Then
> \[
>       \bigcup_{i=1}^t F_i\in\mathcal F(P)
>       \quad\hbox{for every }F_i\in\mathcal F(Y_i),   \tag{1}
> \]
> and consequently
> \[
>       V(P)\ge\prod_{i=1}^t|\mathcal F(Y_i)|.         \tag{2}
> \]

**Proof.**  Let \(F=\bigcup_iF_i\).  Every four-subset of \(F\) either
lies in one \(F_i\), in which case it is convex by heredity, or meets at
least two classes, in which case it is convex by hypothesis.  A planar
set in general position is convex if and only if each of its four-subsets
is convex.  Hence \(F\) is convex.  The classes are disjoint, so the union
map in (1) is injective.  This proves (2). \(\square\)

The proof uses the actual ordinary-face criterion, not a formal downset
identity.  It is valid verbatim for a uniform acyclic rank-three oriented
matroid.

## 2. Quantitative kill of the abstract cage

Use the campaign-safe bound

\[
 \log f(s)\ge {1\over4}(\log s)^2-{1\over2}\log s.     \tag{3}
\]

In the abstract cage,

\[
 t=(1/6+o(1))L,\qquad
 g={n\over tL_2}(1+o(1)),\qquad
 \log g=L-L_2-L_3+O(1).                              \tag{4}
\]

If even two classes \(Y_i,Y_j\) had every mixed four-set convex, Theorem 1
and (3) would give

\[
\begin{aligned}
 \log V(P)
 &\ge {1\over2}(\log g)^2-\log g\\
 &= {1\over2}L^2-L(L_2+L_3)+O(L).                    \tag{5}
\end{aligned}
\]

For \(\Phi_C(L)=L^2/2-CLL_2\) and \(C=3\), the right side of (5) exceeds
\(\Phi_C(L)\) by

\[
                  2LL_2-LL_3+O(L)>0.                 \tag{6}
\]

Using all \(t\) classes gives

\[
 \log V(P)\ge {t\over4}(\log g)^2-O(tL)
              =(1/24+o(1))L^3,                       \tag{7}
\]

far above the half target.  This rigorously reclassifies the complex in
the re-audit report: it is a useful abstract four-uniform independence
complex, but not a planar or oriented-matroid candidate once the known
internal face supply is imposed.

## 3. Exact pruning and the dense cross-circuit residue

For two disjoint supports \(Y,Z\), let

\[
 \Gamma(Y,Z)=
 \{Q\in\tbinom{Y\cup Z}{4}:Q\cap Y,Q\cap Z\ne\varnothing,
                         \ Q\text{ nonconvex}\}.       \tag{8}
\]

> **Theorem 2 (vertex-cover pruning).**  If \(K\subseteq Y\cup Z\)
> meets every member of \(\Gamma(Y,Z)\), then
> \[
> V(P)\ge f(|Y\setminus K|)\,f(|Z\setminus K|).        \tag{9}
> \]
> Consequently, if the right side of (9) exceeds the minimizer target,
> no such cover \(K\) can exist.

**Proof.**  After deleting \(K\), every mixed four-set between the two
remaining supports is convex.  Apply Theorem 1. \(\square\)

Let \(\tau(\Gamma)\) and \(\nu(\Gamma)\) be the vertex-cover and matching
numbers.  The vertices of any maximal matching form a cover, so for this
four-uniform hypergraph

\[
                         \tau(\Gamma)\le4\nu(\Gamma). \tag{10}
\]

At the scale (4), deleting \(o(g)\) labels from each side does not change
(5) at its \(LL_2\) margin.  Hence a fixed-gap least counterexample must
satisfy, for every pair of such classes,

\[
            \tau(\Gamma(Y_i,Y_j))=\Omega(g),
 \qquad     \nu(\Gamma(Y_i,Y_j))=\Omega(g).            \tag{11}
\]

Thus the first genuinely live weakening of the complete cage contains a
linear family of label-disjoint cross-class circuits for every class
pair.  Each matching edge is its own physical four-label decoder.  A
constant pigeonhole retains one circuit sign type and one class-occupancy
type.  What is not automatic is the history load: the same physical
circuit can be reached from many source/completion records unless a
retained carrier, chronology mark, or source face is included.

## 4. Smallest fixed-edge elimination lemma

The common-\(uv\) cage itself is stretchable, so it cannot force a
carrier-retaining child pair.  It does force an endpoint release.

> **Lemma 3 (five-point endpoint XOR).**  Let \(u,v,z\) be a triangle,
> let \(y\) lie in its interior, and let \(x\) lie on the side of \(uv\)
> opposite \(y,z\).  Suppose both
> \(\{u,v,x,y\}\) and \(\{u,v,x,z\}\) are convex.  Then exactly one of
> \[
>                         \{u,x,y,z\},\qquad
>                         \{v,x,y,z\}                 \tag{12}
> \]
> is convex.

**Proof.**  Affinely normalize

\[
 u=(0,0),\quad v=(1,0),\quad z=(0,1),\quad
 y=(a,b),\quad a,b,c:=1-a-b>0,\quad x=(s,t),\ t<0.
\]

Put

\[
\begin{aligned}
 A&=s+t-1,\\
 P&=(1-a)t+bs-b,\\
 Q&=at-bs,\\
 \theta&=(1-b)s+a(t-1).
\end{aligned}
\]

For an ordered four-set, list the four signed affine-dependence
coefficients.  Convexity is exactly a \(2+2\) sign split.  The two assumed
convexities force

\[
 A<0,\qquad s>0,\qquad P<0,\qquad Q<0.
\]

Up to positive factors, the coefficient signs for the two sets in (12)
are

\[
\begin{array}{c|cccc}
 \{u,x,y,z\}&\theta&+&-&+\\
 \{v,x,y,z\}&\theta&-&+&-
\end{array}                                           \tag{13}
\]

Thus the first row has a \(2+2\) split exactly when \(\theta<0\), and the
second exactly when \(\theta>0\).  General position excludes
\(\theta=0\). \(\square\)

The proof is a rank-three circuit-sign calculation, so Lemma 3 also holds
for uniform acyclic rank-three oriented matroids with the corresponding
side covector.

Call the unique endpoint in (12) the color
\(\epsilon_x(y,z)\in\{u,v\}\).

> **Lemma 4 (equal-color two-label amplification).**  In the setting of
> Lemma 3, let \(x,x'\) lie in the common opposite halfplane.  Assume all
> four carrier-singleton sets
> \(\{u,v,x,p\},\{u,v,x',p\}\), \(p\in\{y,z\}\), and
> \(\{u,v,x,x'\}\) are convex.  If
> \(\epsilon_x(y,z)=\epsilon_{x'}(y,z)\), then
> \[
>                         \{x,x',y,z\}\text{ is convex}. \tag{14}
> \]

**Proof.**  The equal colors say \(x,x'\) lie on the same side of the
line \(yz\), so \(yz\) is a supporting edge of the four-set in (14).
The carrier assumptions, with \(x,x'\) in the opposite halfplane, say
that \(u,v,z\), and hence the interior point \(y\), lie on the same side
of \(xx'\).  Thus \(xx'\) is the opposite supporting edge.  Both pairs
are exposed, proving (14).  Equivalently, this is the six-element circuit
elimination table obtained by applying (13) twice. \(\square\)

The common-halfplane condition is essential.  Section 6 gives an exact
rational six-point counterexample without it.

## 5. Exact fixed-pair role bank and decoder

Let \(X_1,\ldots,X_q\) be outside role cells.  Assume every partial
transversal \(S\) satisfies

\[
 \{u,v\}\cup S,\quad
 \{u,v,y\}\cup S,\quad
 \{u,v,z\}\cup S
 \quad\text{convex},                                  \tag{15}
\]

and all outside labels lie opposite the caged pair \(y,z\).  For
\(e\in\{u,v\}\), put

\[
 d_i^e=|\{x\in X_i:\epsilon_x(y,z)=e\}|,
 \qquad P_e=\prod_{i=1}^q(1+d_i^e),\qquad
 Q=\prod_{i=1}^q(1+|X_i|).                            \tag{16}
\]

> **Theorem 5 (fixed-pair shield bank).**  Every set
> \[
>                    \{e,y,z\}\cup S_e                \tag{17}
> \]
> is convex when \(S_e\) is a partial transversal using only
> \(e\)-colored labels.  These give \(P_u+P_v\) distinct faces, and
> \[
>                P_uP_v\ge Q,\qquad
>                \max(P_u,P_v)\ge\sqrt Q.             \tag{18}
> \]

**Proof.**  Check a four-subset of (17).  If it does not contain both
\(y,z\), it is contained in one of the faces in (15).  If it contains
\(e,y,z\) and one outside label, use its color.  If it contains
\(y,z\) and two outside labels, use Lemma 4.  Planar four-locality proves
(17).  Finally,
\[
 (1+d_i^u)(1+d_i^v)\ge1+d_i^u+d_i^v=1+|X_i|,
\]
and multiplication proves (18). \(\square\)

The decoder statement is literal: (17) retains \(e,y,z\) and every
selected outside label.  Across distinct child pairs, the banks are
disjoint because the physical pair \(y,z\) is retained.  Thus the
ordinary-face bank has load one.

This does **not** give a bounded-load routing of full outside words.
Choices of labels of the opposite color are erased; a fixed output can
have the full product of those omitted choices as preimages.  Nor does
(17) retain a rich child face \(F\supset\{y,z\}\).  These are exactly the
two multipliers still missing globally.

In the rational persistent-carrier regression, every one of the 15 child
pairs has

\[
                         (P_u,P_v)=(9,9),\qquad Q=81.
\]

Theorem 5 gives 18 faces per pair and 270 globally distinct faces.  The
verifier checks every one directly.

## 6. Exact stress test

The opposite-halfplane hypothesis in Lemma 4 cannot be deleted.  Take

\[
\begin{aligned}
u&=(0,0),&v&=(1,0),\\
z&=(-1248,-3772)/1000,&y&=(-473,-1845)/1000,\\
x&=(2525,-2834)/1000,&x'&=(4874,-3046)/1000.
\end{aligned}
\]

All triples are noncollinear.  The pair \(y,z\) is caged by \(uv\);
each of \(x,x'\) is individually carrier-compatible with \(y,z\);
\(\{u,v,x,x'\}\) is convex; and both labels have endpoint color \(v\).
Nevertheless \(\{x,x',y,z\}\) is nonconvex.  Here the outside labels lie
on the same side of \(uv\) as the child pair.

This also shows why an arbitrary chamber graph is insufficient: the
side covector supplied by the actual root/pocket geometry must be retained.

## 7. Remaining globally live branch

The complete cross-compatible color-class cage is closed.  A surviving
fixed-gap minimizer must instead provide the dense matchings (11).  The
fixed-edge pocket simultaneously supplies the endpoint shields of
Theorem 5.  What is still unproved is one of:

1. a bounded-history map combining a rich internal child face with one of
   its pair shields;
2. a cross-class circuit matching to cyclic profile bank with retained
   carrier/context; or
3. a planar theorem showing that the dense family in (11) forces a third
   ordinary mixed four-set pattern whose outputs decode the source.

The loss is no longer attributable to complete cross-class compatibility
or to a failure of local circuit elimination.

## 8. Verification

Run

    python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_planar_cross_class_cage_elimination.py

The exact script checks the class-product identity, the fixed-gap
inequalities, \(\tau\le4\nu\) on finite hypergraphs, 9,956 rational
instances of Lemma 3, 1,103 rational instances of Lemma 4, every face in
the 270-face role bank, and the opposite-side counterexample.  It prints
PASS.
