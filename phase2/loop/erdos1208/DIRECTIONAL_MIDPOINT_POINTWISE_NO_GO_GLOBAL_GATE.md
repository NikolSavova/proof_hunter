# Directional midpoint gate: pointwise no-go and live global sum

## Status

Let (A\subset[0,m]^2\cap\mathbb Z^2) be distance-Sidon, (k=|A|),
and let \(\mathcal H_A\) be the endpoint-labelled zero-sum matching
hypergraph.  For a primitive unoriented active direction (w), put

\[
 T_w=\{g>0:gw\in(A-A)\setminus\{0\}\},
 \qquad e_w=|T_w|,
 \qquad M_w={m\over\|w\|_\infty}.                     \tag{0.1}
\]

Orient (w) lexicographically positively.  Define (H_w) to be the
number of clean closed-fibre records with distinguished first vector
(gw), summed over (g\in T_w).  Equivalently, this is the clean
functional on the right of (0.4) in
LARGE_DETERMINANT_CLOSED_FIBRE_ENERGY_GATE.md, now summed over every
determinant fibre.  Then

\[
 \boxed{\sum_wH_w=3|\mathcal H_A|.}                    \tag{0.2}
\]

The proposed pointwise inequality

\[
 H_w\stackrel?\le C(ke_w+M_w^2)                        \tag{0.3}
\]

is false, even with an (m^{o(1)}) factor.  There is an infinite family
of genuine polynomial-height Euclidean distance-Sidon sets for which

\[
 \boxed{
  \max_w{H_w\over ke_w+M_w^2}=\Omega(k).}              \tag{0.4}
\]

The obstruction is the Euclideanized modular parabola.  It has
fourth-order centroid mass spread among many long primitive directions;
some of those directions have (e_w=1) and (M_w=O(1)).  Their local
load is quadratic, not linear, in (k).

The summed inequality

\[
 \boxed{
  \sum_wH_w\stackrel?\ll
  k\sum_we_w+\sum_wM_w^2}                              \tag{0.5}
\]

is not disproved.  In fact it would solve the ambient theorem, because

\[
 \sum_we_w={k(k-1)\over2},
 \qquad
 \sum_wM_w^2\le4m^2H_m.                               \tag{0.6}
\]

The full suite of genuine certificates tested here satisfies (0.5) with
constant one.  On the (p=43) shear the global ratio is
(0.106997\ldots), although the largest pointwise ratio is already
(11.057073\ldots).

Thus the useful outcome is a directional-coupling theorem and no-go:
one cannot prove (0.5) by proving (0.3) separately in every direction.
The compensating (M_w^2) mass can live in a direction different from
the directions carrying most of the hyperedges.  Any proof of the global
gate must transfer charge between directions.

## 1. Exact midpoint formulation

Let

\[
 \Sigma_2(A)=\{x+y:\{x,y\}\in\tbinom A2\}.            \tag{1.1}
\]

Every element of \(\Sigma_2(A)\) has a unique unordered endpoint pair.
Indeed, equality of two pair sums rearranges to equality of two directed
differences, and distance-Sidonicity makes the directed difference map
injective.  Write (P(s)\in\binom A2) for the pair represented by
(s\in\Sigma_2(A)).

For a positive realized vector (q=gw), let \(\epsilon(q)=(a,b)\) be
its unique directed endpoint edge, and define

\[
 L(q)=\left|\left\{
 s\in\Sigma_2(A):
 \begin{array}{l}
 s-q\in\Sigma_2(A),\\
 \epsilon(q),P(s),P(s-q)
 \text{ have six distinct endpoints}
 \end{array}
 \right\}\right|.                                    \tag{1.2}
\]

Then

\[
 \boxed{H_w=4\sum_{g\in T_w}L(gw).}                   \tag{1.3}
\]

To prove this, fix (q=b-a).  A clean segment

\[
 s\longrightarrow s-q                                \tag{1.4}
\]

in the pair-sum set supplies source pair (P(s)=\{c,e\}) and target
pair (P(s-q)=\{d,f\}), with

\[
 a+c+e=b+d+f.                                         \tag{1.5}
\]

There are exactly two bijections from the source pair to the target pair.
Each gives one endpoint-matching hyperedge containing the distinguished
edge ((a,b)).  Conversely every such hyperedge recovers its segment and
bijection.  Finally, each hyperedge is counted twice by the two choices
of the second vector after (q) is distinguished.  Hence every clean
segment contributes four to (H_w), proving (1.3).

Equivalently, if \(\deg(q)\) is the hypergraph degree of the directed
edge representing (q), then

\[
 \deg(q)=2L(q),
 \qquad
 H_w=2\sum_{g\in T_w}\deg(gw).                        \tag{1.6}
\]

Reversing all three directed edges is a fixed-point-free involution on
hyperedges.  It exchanges positive and negative direction orientations.
Thus the positive directed vertices carry half the total degree
(3|\mathcal H_A|), and (1.6) proves (0.2).

This midpoint identity is the exact formulation suggested by the
directional heuristic: (H_w) counts decorated segments of the complete
pair-sum set with differences in \(T_ww\).

## 2. The global right side has the correct size

Every unordered edge of (A) belongs to exactly one primitive direction,
and distinct scalar contents in one direction are forced by distinct
distances.  Therefore

\[
 \sum_we_w=\binom k2.                                  \tag{2.1}
\]

If \(\|w\|_\infty=s\), the fact that some (gw) is realized implies
(1\le s\le m\).  There are at most (4s) primitive unoriented integer
directions with sup-norm (s).  Consequently

\[
\begin{aligned}
 \sum_wM_w^2
 &\le\sum_{s=1}^m4s\left({m\over s}\right)^2\\
 &=4m^2H_m.                                           \tag{2.2}
\end{aligned}
\]

Combining (0.2), (2.1), and (2.2), the global conjecture (0.5) would give

\[
 |\mathcal H_A|\ll k^3+m^2\log m
 =m^{o(1)}(k^3+m^2),                                  \tag{2.3}
\]

which is exactly the ambient endpoint-hypergraph gate.

## 3. Rigorous counterexample to the pointwise bound

Let (p) be an odd prime and take the least-residue parabola

\[
 P_p=\{(x,[x^2]_p):0\le x<p\}\subset[0,p-1]^2.        \tag{3.1}
\]

It is integer vector-Sidon.  Its \(\binom p3\) unordered triples occupy
fewer than (9p^2) exact integer sum cells, so Cauchy--Schwarz and
endpoint cancellation give

\[
 |\mathcal H_{P_p}|=\Omega(p^4).                       \tag{3.2}
\]

The only horizontal direction has

\[
 e_{(1,0)}={p-1\over2},                                \tag{3.3}
\]

because every nonzero quadratic-residue level contains two points.  A
fixed directed edge has hypergraph degree at most
(2\binom{p-2}{2}).  By (1.6), the complete horizontal contribution is
therefore only

\[
 H_{(1,0)}\le4e_{(1,0)}\binom{p-2}{2}=O(p^3).          \tag{3.4}
\]

It follows from (0.2), (3.2), and (3.4) that the nonhorizontal directions
carry

\[
 \sum_{w_y\ne0}H_w=\Omega(p^4).                       \tag{3.5}
\]

Now apply the determinant-one shear

\[
 S_t(x,y)=(x+ty,y).                                    \tag{3.6}
\]

Choose (t\ge2p) outside the integer roots of all squared-distance
collision polynomials.  There are (O(p^4)) edge pairs and at most two
roots per pair, so one may choose (t=O(p^4)).  The set (S_tP_p) is a
genuine Euclidean distance-Sidon set of height (m=O(p^5)), while all
centroid records and direction occupancies are preserved.

Write a primitive nonhorizontal direction before shearing as (w=(a,b)),
where (1\le|b|\le p) and \(|a|\le p\).  Its image is the primitive
direction

\[
 w_t=(a+tb,b).
\]

For (t\ge2p),

\[
 \|w_t\|_\infty\ge {t|b|\over2},
 \qquad
 M_{w_t}\le {3p\over|b|}.                             \tag{3.7}
\]

For each fixed \(|b|\), at most (2p+1) possible (a)'s occur.  Hence

\[
 \sum_{w_y\ne0}M_{w_t}^2
 \ll p^2\sum_{b=1}^p{p\over b^2}
 \ll p^3.                                             \tag{3.8}
\]

Also

\[
 p\sum_{w_y\ne0}e_w\le p\binom p2=O(p^3).            \tag{3.9}
\]

Dividing (3.5) by the sum of (3.8)--(3.9) shows that some nonhorizontal
direction obeys

\[
 {H_w\over pe_w+M_w^2}=\Omega(p).                     \tag{3.10}
\]

Since (k=p) and (m=O(p^5)), this disproves (0.3) with an absolute
constant or even with a subpolynomial loss.  Notice why the global bound
is not contradicted: the horizontal direction is fixed by the shear and
has (M_{(1,0)}=m), so its (M_w^2) term can pay globally for mass
living in completely different directions.

## 4. Exact certificate audit

For the genuine (p=43), (t=28) lift, (k=43) and (m=1175).  The
largest pointwise ratio occurs at

\[
 w=(539,19),\qquad e_w=1,\qquad H_w=528,
\]

and equals

\[
 {528\over43+(1175/539)^2}
 ={38348772\over3468257}
 =11.057073\ldots.                                    \tag{4.1}
\]

Yet globally

\[
 \sum_wH_w=380556,
 \qquad
 {\sum_wH_w\over
   43\sum_we_w+\sum_wM_w^2}
 =0.106997\ldots.                                     \tag{4.2}
\]

The maximum pointwise ratios along the standard genuine sheared-parabola
certificates are

\[
\begin{array}{c|rrrrrrrr}
p&7&11&13&17&19&23&29&43\\ \hline
\max_w H_w/(ke_w+M_w^2)
&0.459&1.067&1.811&2.082&3.335&4.575&5.262&11.057
\end{array}                                           \tag{4.3}
\]

The following independent genuine stresses all satisfy the summed
inequality with constant one.

\[
\begin{array}{l|r|r|r}
\text{family}&\sum_wH_w&
 \sum_wH_w/(k\sum e_w+\sum M_w^2)&
 \max_w H_w/(ke_w+M_w^2)\\ \hline
\text{closure-20}&1296&0.0314&0.619\\
\text{closure-40}&24840&0.0588&1.474\\
\text{Costas-17}&3816&0.0871&2.094\\
\text{Costas-23}&18684&0.2778&3.908\\
\text{two-arm-16}&3672&4.2\cdot10^{-11}&6.4\cdot10^{-11}
\end{array}                                           \tag{4.4}
\]

These computations are evidence only for the global gate.  The theorem
in Section 3 decisively rules out the pointwise route.

## 5. Exact remaining directional theorem

The viable statement is now precisely

> **Global directional midpoint gate.**  For every distance-Sidon
> (A\subset[0,m]^2),
> \[
>  \sum_w\sum_{g\in T_w}L(gw)
>  \le m^{o(1)}\left(
>       k\sum_we_w+\sum_wM_w^2\right).
> \]

By (1.3) and (2.3), this would prove the required ambient theorem.  The
parabola no-go shows that its proof must be a genuinely global transfer:
directions with excessive midpoint-segment load must force enough
reciprocal primitive-direction mass elsewhere.  No independent
per-direction estimate can do this.

## 6. Verification

Run

    python3 phase2/loop/erdos1208/verify_directional_midpoint_pointwise_no_go_global_gate.py

The verifier checks the exact midpoint identity against the independent
closed-fibre formulation, the factor (4) in (1.3), the full (p=43)
profile and extremizer, growth of the pointwise obstruction across eight
sheared parabolas, and the global inequality on the closure, Costas, and
two-arm certificates in (4.4).
