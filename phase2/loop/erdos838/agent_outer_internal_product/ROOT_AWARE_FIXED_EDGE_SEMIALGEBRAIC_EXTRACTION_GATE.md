# Root-aware fixed-edge semialgebraic extraction and the homogeneous nested-ear barrier

**Date:** 2026-08-15. An ordinary set means a set in strictly convex
position. All configurations are in affine general position.

## Verdict

Fixing a literal source face and one exposed edge gives a clean quantitative
promotion, provided a positive fraction of the rooted transversals already
coexist with that face. If \(F\) has rank \(r\), \(e\) is an exposed edge
of \(F\), and \(X_1,\ldots,X_k\) are ordered ear roles at \(e\), let
\(\varepsilon\) be the density of tuples for which

\[
                         F\cup\{x_1,\ldots,x_k\}                 \tag{1}
\]

is ordinary in the prescribed rooted cyclic order. Fox--Pach--Suk gives
subsets \(Z_i\subseteq X_i\) on which every tuple is good and

\[
 { |Z_i|\over |X_i|}
 \ge {\varepsilon^3\over 3^{40k}t^2},
 \qquad t\le (r+k)^2.                                           \tag{2}
\]

Every partial \(Z\)-transversal then coexists with \(F\), so the rooted
one-face bank has exact size

\[
                              \prod_{i=1}^k(1+|Z_i|).             \tag{3}
\]

For

\[
\begin{gathered}
 k=\alpha\log_2\log_2 n,\qquad r=O(\log n),\\
 |X_i|\ge {n\over(\log n)^B},\qquad
 \varepsilon\ge(\log n)^{-C},
\end{gathered}                                                   \tag{4}
\]

(3) is

\[
                 n^{\alpha\log_2\log_2 n-o(\log\log n)}.         \tag{5}
\]

This is the requested anchored \(n^{\Theta(\log\log n)}\) coexistence bank,
with an exact global output-load form below.

The positive-density premise is indispensable. There is a scalable rational
family with one fixed carrier triangle \(B\), one exposed edge \(e\), and
\(k\) ordered role blocks such that

* every singleton is inserted through the same edge \(e\);
* the entire labelled rooted order type of
  \(B\cup\{x_1,\ldots,x_k\}\) is constant over all transversals, so all
  \(\binom{k+3}{3}\) rooted orientation predicates are fixed;
* every external transversal is ordinary by itself; but
* every rooted transversal using at least two external labels is bad.

Every cross-role pair has the same fixed-edge \(1+3\) circuit. Thus fixing
polynomially many pocket signs, edge signatures, and interval signatures
does not imply positive rooted density. The construction is paid by a
Boolean absolute bank on the external support, so it is a sharp promotion
barrier, not a live low-face counterexample. The remaining alternative is:

1. prove positive rooted density from marked/minimizer history; or
2. charge the dense fixed-edge circuit rectangle to its absolute
   support/downshadow bank with globally controlled history load.

No half-coefficient closure is claimed.

## 1. Rooted semialgebraic extraction

Let \(F=(f_1,\ldots,f_r)\) be ordinary in cyclic order and let \(e=uv\)
be one boundary edge. Let \(X_1,\ldots,X_k\) be disjoint point sets in the
open ear cell of \(e\). Fix the intended order in which these roles replace
\(e\), and define

\[
 \mathcal G_F=\{(x_1,\ldots,x_k):
       F\cup\{x_1,\ldots,x_k\}\text{ is ordinary in that order}\}. \tag{6}
\]

Write the proposed cyclic boundary word and require every oriented boundary
edge to support every nonincident point. This expresses (6) as a
conjunction of at most

\[
                         t\le (r+k)(r+k-2)<(r+k)^2               \tag{7}
\]

strict determinant inequalities. Every determinant is affine in the two
coordinates of each one of its point arguments when all other arguments
are fixed. Thus (6) is a \(k\)-partite semialgebraic relation in
\(\mathbb R^2\) of complexity \((t,1)\) in the separate-degree sense of
Fox--Pach--Suk. General position handles strict signs.

Put

\[
 \varepsilon={|\mathcal G_F|\over\prod_i|X_i|}.                  \tag{8}
\]

Corollary 1.2 of Fox--Pach--Suk, with arity \(k\), dimension \(d=2\),
and complexity \((t,1)\), gives a complete product

\[
                         Z_1\times\cdots\times Z_k
                              \subseteq\mathcal G_F              \tag{9}
\]

and

\[
 |Z_i|\ge
 {\varepsilon^{d+1}\over
   2^{20kd\log_2(d+1)}t^d}|X_i|
 = {\varepsilon^3\over3^{40k}t^2}|X_i|.                         \tag{10}
\]

The primary source is Fox, Pach, and Suk,
[*A polynomial regularity lemma for semi-algebraic hypergraphs and its
applications in geometry and property testing*](https://arxiv.org/abs/1502.01730),
Theorem 1.1 and Corollary 1.2. An orientation determinant is quadratic in
all coordinates together but degree one in each point block; the latter is
exactly their definition of \(D=1\).

Given a partial \(Z\)-transversal, fill empty roles arbitrarily and delete
the added points from the good full tuple. Heredity proves ordinaryness.
Disjoint role supports recover all choices, proving (3).

If the rooted ordinary tuples are not initially supplied in one prescribed
chain order, partition them by their at most \(k!\) role orders. One order
has density at least \(\varepsilon/k!\), to which (10) applies. At
\(k=\Theta(\log\log n)\), this adds only

\[
                 3k\log_2(k!)=O(k^2\log k)
                    =o(\log n\log\log n)                         \tag{10a}
\]

to the bank's logarithmic loss. Thus fixing the interval order is
quantitatively harmless; fixing a *good* rooted sign state is the genuine
issue.

## 2. Exact global weighted/load form

Let \(c\) range over rooted contexts

\[
              c=(F_c,e_c,X_{c,1},\ldots,X_{c,k_c}).              \tag{11}
\]

The faces \(F_c\) and extracted boxes may vary. Give context \(c\) weight
\(w_c\ge0\). Its output incidences are

\[
  (c,I,(z_i)_{i\in I})\longmapsto
       F_c\cup\{z_i:i\in I\},\qquad I\subseteq[k_c].              \tag{12}
\]

For unit ordinary-face capacity define the actual weighted output load

\[
 \Lambda=\max_G
 \sum_{c,I,(z_i):\,G=F_c\cup\{z_i:i\in I\}}w_c.                  \tag{13}
\]

Direct double counting gives

\[
 \boxed{\displaystyle
 V(P)\ge {1\over\Lambda}
       \sum_c w_c\prod_i(1+|Z_{c,i}|).}                          \tag{14}
\]

Thus different roots and histories are not silently assumed disjoint.
Their exact coalescence is (13).

For (4), put \(L=\log_2 n\). Since \(t\le(r+k)^2=L^{O(1)}\), (10) gives

\[
 \log_2|Z_i|
 \ge L-
 \bigl(B+3C+40\alpha\log_2 3+O(1)\bigr)\log_2L.                 \tag{15}
\]

Multiplying over \(k=\alpha\log_2L+O(1)\) roles yields

\[
 \log_2\prod_i(1+|Z_i|)
 \ge \alpha L\log_2L-O((\log L)^2),                             \tag{16}
\]

which proves (5). A global load
\(\Lambda=n^{o(\log\log n)}\) preserves the leading term.

## 3. Complementary cross-circuit pattern

Suppose \(F\cup\{x_i\}\) is ordinary for every singleton but a full tuple
is bad. Planar four-locality supplies a bad four-subset. It uses at least
two external labels because \(F\) and every singleton extension are
ordinary.

Choose the first bad four-subset in a fixed ordering of the \(r+k\)
labelled slots. There are at most

\[
                              \binom{r+k}{4}                     \tag{17}
\]

slot patterns. If the good density is below \(\eta\), one canonical
cross-circuit pattern therefore carries at least

\[
                       {1-\eta\over\binom{r+k}{4}}               \tag{18}
\]

of the full product measure. In the two-carrier/two-external subcase, the
pattern fixes two physical carrier labels and two external roles. If the
carrier pair is \(e\), this is exactly the dense fixed-edge circuit
rectangle. The rooted \(1+3\) circuit types and the three-external slot
patterns remain explicit alternatives.

Equations (10) and (18) form a rigorous rooted box-or-circuit-pattern
dichotomy. A bounded-load conversion of the circuit branch in an arbitrary
live family is not proved here.

## 4. Scalable homogeneous-bad fixed-edge family

Fix \(k,D\ge2\), put \(q=kD\), and set

\[
 \delta={1\over100q^2},\qquad
 u=(-2,0),\quad v=(2,0),\quad w=(0,6),\quad B=\{u,v,w\}.          \tag{19}
\]

Let

\[
 m=(1,3),\qquad n=(3,1),\qquad d=(-2,6),\qquad
 a_t=m+tn+\delta t^2d\quad(1\le t\le q),                        \tag{20}
\]

and split the sequence into consecutive roles

\[
 X_i=\{a_{(i-1)D+1},\ldots,a_{iD}\},\qquad1\le i\le k.           \tag{21}
\]

Every \(a_t\) lies in the open ear cell of the physical edge \(e=vw\), so
\(B\cup\{a_t\}\) is an ordinary quadrilateral. For \(s<t\), put

\[
                         b_{s,t}=m-\delta st\,d.                  \tag{22}
\]

The segment \(vw\) is
\(\{m+\lambda d:-1/2\le\lambda\le1/2\}\), and
\(-\delta st\in(-1/2,1/2)\). Moreover,

\[
 a_s={s\over t}a_t+
       \left(1-{s\over t}\right)b_{s,t}.                         \tag{23}
\]

Thus \(a_s\) lies strictly inside
\(\operatorname{tri}(v,w,a_t)\). Consequently

\[
              B\cup S\text{ is ordinary}
                 \quad\Longleftrightarrow\quad |S|\le1
              \qquad(S\subseteq\{a_1,\ldots,a_q\}).              \tag{24}
\]

Every cross-role pair has the same fixed-edge circuit

\[
                      a_s\in\operatorname{int}
                            \operatorname{tri}(v,w,a_t),          \tag{25}
\]

and the bad rectangle contains exactly

\[
                             \binom{k}{2}D^2                     \tag{26}
\]

distinct cross-role pairs.

The construction fixes much more than an edge signature. For \(r<s<t\),

\[
 \det(a_r,a_s,a_t)
   =20\delta(s-r)(t-r)(t-s)>0.                                  \tag{27}
\]

For \(s<t\),

\[
\begin{aligned}
 \det(u,a_s,a_t)
   &=(t-s)\{-6+\delta[24(s+t)+20st]\}<0,\\
 \det(v,a_s,a_t)
   &=(t-s)(-10+20\delta st)<0,\\
 \det(w,a_s,a_t)
   &=(t-s)(10+20\delta st)>0.                                   \tag{28}
\end{aligned}
\]

The signs with two carrier labels are also independent of \(t\):

\[
\begin{aligned}
 \det(u,v,a_t)&=4(3+t+6\delta t^2)>0,\\
 \det(v,w,a_t)&=-20t<0,\\
 \det(w,u,a_t)&=12+16t-24\delta t^2>0.                           \tag{29}
\end{aligned}
\]

Together with \(\det(u,v,w)>0\), equations (27)--(29) prove that every
labelled transversal

\[
                         (u,v,w,x_1,\ldots,x_k),
                         \qquad x_i\in X_i,                      \tag{30}
\]

has exactly the same full order type. Its convex hull is
\(B\cup\{x_k\}\), so it has four hull vertices and is bad for \(k\ge2\).
Thus fixing all \(\binom{k+3}{3}\) rooted triple signs still leaves
\(\varepsilon=0\) in (8).

Finally, the affine map \((t,t^2)\mapsto a_t\) is nonsingular because
\(\det(n,d)=20\). Hence \(\{a_1,\ldots,a_q\}\) is in convex position and
has the Boolean absolute bank

\[
                                  2^q.                            \tag{31}
\]

This explains how the example is paid: the external bank cannot be
multiplied by \(B\). Among outputs retaining \(B\), (24) leaves only
\(q+1\), versus the formal role count \((1+D)^k\).

## 5. Scope and live implication

The positive theorem is numerically strong enough: inverse-polylogarithmic
rooted density and polynomial-rank source faces lose only
\(O((\log\log n)^2)\) bits from the desired
\(\Theta(\log n\log\log n)\) multiplier. It retains the literal source
face and edge, so it plugs into a weighted source bank once (13) is
bounded.

The nested-ear family rules out promotion from same-type external
transversals, a common exposed edge, one-point ear/interval signatures, or
polynomially many rooted signs alone. Because (31) is huge, it does not
refute a theorem balancing rooted coexistence against an absolute
support/downshadow bank. It identifies the remaining global interface:
charge that absolute bank with the original source/history without
quadratic reuse across roots.

## 6. Verification

Run:

    python3 agent_outer_internal_product/verify_root_aware_fixed_edge_semialgebraic_extraction_gate.py

The exact verifier:

1. checks a positive fixed-edge anchored chain and every partial-role
   output;
2. checks the Fox--Pach--Suk arithmetic in (15)--(16);
3. verifies general position and (23), (27)--(29) for \(k=4,D=3\);
4. exhausts all \(3^4=81\) rooted transversals, finding one order type and
   hull size four;
5. verifies all \(\binom42 3^2=54\) fixed-edge cross-role circuits;
6. verifies that all twelve external labels are convex, the rooted ledger
   \(q+1=13\), and absolute capacity \(2^{12}=4096\); and
7. checks (14) on a finite weighted context system.

It prints PASS.
