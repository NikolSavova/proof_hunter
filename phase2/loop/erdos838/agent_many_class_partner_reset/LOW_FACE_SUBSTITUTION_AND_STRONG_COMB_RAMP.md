# Low-face substitution in the tangent reset: exact strong-comb payment and ramp

**Date:** 2026-08-15. All logarithms are base two. Counts \(C,U,W\)
mean nonempty caps, cups, and ordinary convex subsets in the displayed
left-to-right chart.

## Verdict

The uniform signed fresh-partner itinerary does **not** force any macro
label cell to be convex or Boolean. Every macro label in the scalable
tangent-line reset can be replaced by an independently chosen arbitrary
rational planar order type. If all replacement cells have the same size
\(D\), every class-pair matching expands from size \(m\) to size \(mD\),
still covers every physical label, still uses a fresh physical partner for
every neighbouring class, and still has pair-node degree one. The hidden
point remains in the higher-index \(L\)-cell. The whole construction can
again be nested behind the common edge \(uv\).

There is nevertheless an exact within-class payment. In a vertical
infinitesimal substitution, the \(q=2m\) cells of one class form a convex
strong comb. If cell \(i\) has profile \((n_i,C_i,U_i,W_i)\), then

\[
\boxed{
\begin{aligned}
 C(Y)&=\sum_i C_i\left(1+\sum_{j>i}n_j\right),\\
 U(Y)&=\sum_j U_j\prod_{k<j}(1+n_k),\\
 W(Y)&=\sum_iW_i+
       \sum_{i<j}C_iU_j\prod_{i<k<j}(1+n_k).
\end{aligned}}                                         \tag{1}
\]

This recurrence kills stationary substitution. If the same \(D\)-point
child \(Q\) is used in all \(q\) cells, then

\[
 W(Y)=qW(Q)+C(Q)U(Q)
 { (1+D)^q-1-qD\over D^2},                              \tag{2}
\]

and \(C(Q)U(Q)\ge W(Q)\). At the live minimal cell count
\(q=2(t-1)=(1/3+o(1))\log n\), the universal quarter-scale child reservoir
would therefore pay coefficient \(1/3+1/4=7/12>1/2\).

The sharp escape is an endpoint-profile ramp. With
\(q=(\alpha+o(1))\log D\) and local profile product at coefficient \(c\),
the scalar max-plus value of (1) is exactly

\[
                            \max\{\alpha,c\}.            \tag{3}
\]

For the live values \((\alpha,c)=(1/3,1/4)\), the recurrence can remain at
coefficient \(1/3\), not \(1/2\), provided the cell charts ramp from
cap-poor/cup-rich to cap-rich/cup-poor. Thus the tangent reset moves the
low-face question to a precise existing obstruction: can actual
\(D\)-point low-face order types realize a \(\Theta(\log D)\)-cell
endpoint ramp? The circuit signs place no further restriction on those
internal charts.

No such low-face planar ramp is constructed here. Consequently this note
is a substitution theorem and a sharp recurrence barrier, not a sub-half
construction and not a closure of Erdős 838.

## 1. Arbitrary child order types survive every reset matching

Start with the rational general-position macro reset from
*SCALABLE_STRETCHABLE_PARTNER_RESET_AND_FACE_AUDIT.md*. Its macro labels
are

\[
                 L_{i,a},R_{i,a}\qquad
                 (0\le i<t,\ 0\le a<m),                 \tag{4}
\]

and for every \(i<j\), \(0\le a<m\), the four designated macro labels form
a strict nonconvex \(2+2\) circuit whose hidden point is \(L_{j,a}\).

At every macro label \(z\), choose an arbitrary rational \(D\)-point
general-position order type \(Q_z\). Choose two independent rational
linear functionals \(f_z,h_z\), with \(f_z\) generic. For sufficiently
small positive rational \(\eta_z\), the two functionals

\[
                    f_z,\qquad g_z=f_z+\eta_zh_z        \tag{5}
\]

induce the same strict order on \(Q_z\). The affine chart
\(x\mapsto(f_z(x),g_z(x))\) is nonsingular and therefore preserves the
child order type, up to the deliberately chosen orientation.

Replace macro point \(z=(x_z,y_z)\) by

\[
       X_z=\{(x_z+\varepsilon^2f_z(p),
               y_z+\varepsilon g_z(p)):p\in Q_z\}.      \tag{6}
\]

For all sufficiently small rational \(\varepsilon>0\):

1. a triple in one cell has the child sign;
2. a triple in three cells has the macro sign;
3. if the first two points in the global \(x\)-order lie in one cell, its
   sign is negative; and
4. if the last two lie in one cell, its sign is positive.

These statements follow by taking the first nonzero term in the determinant
as \(\varepsilon\to0\). They are finitely many strict rational
inequalities, so exact halving finds a valid rational \(\varepsilon\).

More importantly, every selected macro four-circuit is strict. Hence
there are four neighbourhoods such that **every** transversal through its
four replacement cells has the same hidden-cell circuit sign. The
internal order types and charts are irrelevant to that fact.

For neighbour \(j\), retain the cyclic macro factor

\[
 \{\{L_{i,a},R_{i,a+r_i(j)}\}:0\le a<m\}.              \tag{7}
\]

Inside each paired macro-cell pair, match physical index \(s\) to physical
index \(s\), \(0\le s<D\). Match the resulting physical pair to the
same-index pair in the other class. Thus every macro edge expands to
\(D\) physical circuit edges. For every class pair:

\[
\begin{array}{c|c}
\text{matching size}&mD=|Y_i|/2\\
\text{load of every physical label}&1\\
\text{physical pair-node degree}&1.
\end{array}                                             \tag{8}
\]

Across all neighbouring classes every physical label has load \(t-1\).
Different neighbours use different macro partner cells, so no physical
pair is reused and the pair-node graph has no triangle.

Finally apply the projective nesting map from the preceding report to the
whole substituted configuration. It preserves every child order type,
every circuit sign, and every face, while putting all labels in the
common-\(uv\) pocket with the opposite-side endpoint colors defined.
The profiles in (1) are then understood in the pulled-back construction
chart (6); projective nesting changes the displayed affine direction but
does not erase that marked chart or the ordinary-face identity.

This proves:

> **Theorem 1 (projectively universal tangent reset).** For every
> \(t\ge2\), \(m\ge t-1\), \(D\ge1\), and every family of rational
> \(D\)-point planar order types assigned to the \(2mt\) macro labels,
> there is a rational general-position substitution satisfying (8), label
> load \(t-1\), zero pair-node triangles, the transitive hidden-cell rule,
> and the common-\(uv\) pocket conditions.

In particular, neither the signed itinerary nor the common carrier gives
an induced-face lower bound stronger than the one already present in the
arbitrary children.

## 2. Exact strong-comb recurrence

Fix one class and list its \(q=2m\) macro cells in increasing \(x\)-order:

\[
                       X_1,\ldots,X_q.                  \tag{9}
\]

The macro centers lie on a strictly convex parabola, with every ordered
macro triple positive. The four sign rules after (6) classify every
ordinary face.

If a face meets only one cell \(X_i\), its trace may be any of the \(W_i\)
local faces. If it meets at least two cells, let \(i<j\) be the first and
last active cells. Its trace in \(X_i\) must be a cap, its trace in
\(X_j\) must be a cup, and every intermediate active cell contributes
exactly one point. Conversely every such choice is ordinary: triples in
the endpoint cells use the cap/cup signs, triples using an intermediate
singleton use the macro-cup sign, and all four-subsets are convex.

The active cells and their physical traces recover every choice. Summing
over \(i,j\) proves the \(W\)-line of (1). The same classification for a
global cap says that its first cell contributes a cap and it has either no
other active cell or one singleton in one later cell. For a global cup,
its last cell contributes a cup and every earlier cell is empty or a
singleton. These give the \(C,U\) lines.

Thus (1) is an equality for heterogeneous arbitrary order types, not a
formal downset approximation.

There is one universal local relation:

\[
                              C_iU_i\ge W_i.             \tag{10}
\]

Indeed a convex local face is recovered from its two directed boundary
chains in the chosen \(x\)-chart. One chain is a cap and the other is a
cup, so the boundary-pair encoding injects local faces into
\(\mathcal C_i\times\mathcal U_i\).

For identical children, substituting \(n_i=D\),
\(C_i=C\), \(U_i=U\), \(W_i=W\) in (1) gives

\[
\begin{aligned}
C(Y)&=C\left(q+\binom q2D\right),\\
U(Y)&=U{(1+D)^q-1\over D},\\
W(Y)&=qW+CU{(1+D)^q-1-qD\over D^2},                    \tag{11}
\end{aligned}
\]

which proves (2) and the stationary \(7/12\) payment.

## 3. Exact low-parent gradient theorem

The heterogeneous escape has a rigid necessary form. Take equal cell
sizes \(D\), put

\[
                      r=\log_D(D+1),                   \tag{12}
\]

and suppose

\[
             W_i\ge D^h\quad(1\le i\le q),\qquad
             W(Y)\le D^p.                              \tag{13}
\]

Write \(a_i=\log_D C_i\). The \(ij\) term in (1), (10), and (13) give

\[
 C_i\,{D^h\over C_j}(D+1)^{j-i-1}\le D^p.
\]

Therefore:

> **Theorem 2 (endpoint-gradient dichotomy).** Under (13), every
> \(i<j\) satisfies
> \[
>       \boxed{\quad
>       a_j-a_i\ge h+(j-i-1)r-p.
>       \quad}                                         \tag{14}
> \]

The same statement with cap and cup reversed follows by reflection.
In particular,

\[
                   a_q-a_1\ge h+(q-2)r-p.              \tag{15}
\]

The recurrence also contains the all-singleton source bank:

\[
 W(Y)\ge D^2(D+1)^{q-2}\ge D^q,                        \tag{16}
\]

and every local bank survives, so \(p\ge\max\{q,h\}\). If a parent is
near this scalar lower envelope with \(p=q+o(q)\), equation (15) forces
almost the entire local endpoint-product exponent \(h\) to move from the
cup coordinate into the cap coordinate across the class.

This is the recoverable within-class conclusion supplied by the low-face
hypothesis: either a forward profile term already pays, or the cells carry
a long signed endpoint ramp. It is stronger than a scalar induced-face
bank, but it does not itself prohibit the ramp.

## 4. Sharp max-plus barrier

Let \(L=\log D\), \(q=(\alpha+o(1))L\), and suppose the relevant local
profiles have quadratic-scale product

\[
 {\log C_i\over L^2}=x_i+o(1),\qquad
 {\log U_i\over L^2}=c-x_i+o(1),\qquad 0\le x_i\le c.  \tag{17}
\]

Put \(t_i=i/L\) and \(y_i=x_i-t_i\). A forward term in (1) has normalized
exponent

\[
                         c+y_i-y_j+o(1)\qquad(i<j),     \tag{18}
\]

while the local and all-singleton banks have exponents \(c\) and
\(\alpha\). Consequently every scalar instance has value at least
\(\max\{c,\alpha\}\).

This is sharp. If \(c\ge\alpha\), choose

\[
                         x(t)=t+{c-\alpha\over2}.       \tag{19}
\]

Then \(y\) is constant and all forward terms have exponent \(c\). If
\(\alpha\ge c\), choose

\[
                         x(t)=\min\{t,c\}.              \tag{20}
\]

Now \(y(t)=0\) up to \(t=c\) and \(y(t)=c-t\) afterwards. Hence
\(y(s)-y(t)\le\alpha-c\) for \(s<t\), and every forward exponent is at
most \(\alpha\). Equations (19)--(20) prove (3).

At the live tangent-reset values, take the smallest allowed
\(m=t-1\). The class count in the dense-circuit regime is
\(t=(1/6+o(1))\log n\), so

\[
              q=2m=(1/3+o(1))\log n,\qquad
              \alpha={1\over3}.                         \tag{21}
\]

The campaign-safe child reservoir gives \(c=1/4\). Formula (20) becomes

\[
                     x(t)=\min\{t,1/4\},                \tag{22}
\]

and the exact recurrence can stay at coefficient \(1/3\). By contrast,
using one stationary chart makes \(x\) constant and the first-to-last term
has coefficient \(c+\alpha=7/12\).

Thus a low-face substituted tangent reset must use genuinely heterogeneous
child order types or projection charts with endpoint exponent spread
\(1/4-o(1)\). The circuit matching does not couple these charts: its
four cells may be shrunk independently before the common global scale is
chosen.

## 5. What remains open

The new exact fork is:

1. **Positive route:** prove that actual low-face \(D\)-point order types
   cannot supply the ramp (22) in \(\Theta(\log D)\) independently
   recharted copies, or show that cross-class reuse couples their endpoint
   charts after all.
2. **Construction route:** exhibit actual low-face child order types and
   charts realizing (22), then iterate without a stationary chart
   reappearing at the next scale.

The scalar ramp alone is not a planar construction. Realizing it with
\(\log W_i=(1/4+o(1))(\log D)^2\) would already resolve the central
heterogeneous cap/cup anti-alignment problem. Conversely, Theorem 1 means
that no proof may infer a rich individual child merely from the tangent
reset signs.

The exact theorem banked here is therefore: arbitrary-order-type
substitution is possible; stationary substitution pays above one half;
and every low parent forces the quantitative endpoint gradient (14).
There is no claim of global synthesis closure.

## 6. Verification

Run

~~~text
python3 phase2/loop/erdos838/agent_many_class_partner_reset/verify_low_face_substitution_profile.py
~~~

The exact rational regression uses \(t=3,m=2,D=4\), hence 48 points. It
alternates a nonconvex four-point child and its mirror in every class,
checks 24 physical circuit edges, label load two, pair-node degree one,
zero pair-node triangles, and the common-\(uv\) nesting. Exhausting every
subset of one 16-point class gives

\[
\begin{array}{c|c}
\text{cell profiles}&
(4,13,11,14),(4,11,13,14),(4,13,11,14),(4,11,13,14)\\
\text{direct class }(C,U,W)&(344,1976,6170)\\
\text{recurrence }(C,U,W)&(344,1976,6170).
\end{array}                                             \tag{23}
\]

It also verifies the Cartesian trace description in every one of the 15
nonempty active-cell patterns, checks the sharp max-plus ramps in 2,856
exact rational cases, and checks 218 cleared finite instances of the
gradient inequality (14). It prints PASS.
