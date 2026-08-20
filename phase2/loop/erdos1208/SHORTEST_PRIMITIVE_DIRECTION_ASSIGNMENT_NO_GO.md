# Shortest primitive direction assignment: a constituent-charge no-go

## Status

Let (A\subset[0,m]^2\cap\mathbb Z^2) be distance-Sidon and let
\(\mathcal H_A\) be its endpoint-labelled zero-sum matching hypergraph.
For an active primitive unoriented direction (w), write

\[
 e_w=|\{g>0:gw\in(A-A)\setminus\{0\}\}|,
 \qquad
 M_w={m\over\|w\|_\infty}.                            \tag{0.1}
\]

Assign every hyperedge (h=\{q_1,q_2,q_3\}) to a direction (w(h))
among its three primitive directions having the smallest sup-norm, or
equivalently the largest (M_w).  Break genuine ties lexicographically,
and put

\[
 A_w=|\{h\in\mathcal H_A:w(h)=w\}|.                   \tag{0.2}
\]

The proposed canonical pointwise estimate

\[
 A_w\stackrel?\le C(ke_w+M_w^2)                       \tag{0.3}
\]

is false.  More strongly, there are genuine polynomial-height Euclidean
distance-Sidon sets for which

\[
 \boxed{
  \max_w{A_w\over ke_w+M_w^2}=\Omega(k).}              \tag{0.4}
\]

The proof does not depend on choosing the shortest direction.  It rules
out **every rule which assigns each hyperedge to one of its own three
primitive directions**.

The obstruction is again the Euclideanized modular parabola.  Almost all
of its fourth-order hyperedge mass avoids its one short horizontal
direction.  A strong shear makes all remaining constituent directions
long, so their total pointwise budget is only (O(k^3)), while they must
receive \(\Omega(k^4)\) records under any constituent assignment.

This sharpens the conclusion of
DIRECTIONAL_MIDPOINT_POINTWISE_NO_GO_GLOBAL_GATE.md.  A successful
cross-direction charge must sometimes send a hyperedge to a direction
which is **not present in that hyperedge**.  Merely choosing its best of
three directions cannot access the ambient compensator.

## 1. Exact three-direction identity

Write the three directed vectors of a hyperedge as

\[
 q_i=\lambda_iw_i,
 \qquad \lambda_i\in\mathbb Z\setminus\{0\},           \tag{1.1}
\]

where each (w_i) is primitive and unoriented under a fixed sign
convention.  The closing condition is

\[
 \lambda_1w_1+\lambda_2w_2+\lambda_3w_3=0.             \tag{1.2}
\]

If the hyperedge is noncollinear, its common signed determinant obeys

\[
\boxed{
 \lambda_1\lambda_2\det(w_1,w_2)
 =\lambda_2\lambda_3\det(w_2,w_3)
 =\lambda_3\lambda_1\det(w_3,w_1).}                   \tag{1.3}
\]

Indeed (q_3=-q_1-q_2) gives

\[
 \det(q_2,q_3)=\det(q_1,q_2)=\det(q_3,q_1).
\]

Identity (1.3) is the full three-direction arithmetic available to the
canonical rule.  Selecting the smallest \(\|w_i\|_\infty\) is the most
favourable local choice for the (M_w^2) term.  Nevertheless, the
construction below defeats it by a polynomial factor.

Plainly

\[
 \sum_wA_w=|\mathcal H_A|.                             \tag{1.4}
\]

Thus (0.3), summed over (w), would prove the desired ambient theorem,
since

\[
 \sum_we_w=\binom k2,
 \qquad
 \sum_wM_w^2\le4m^2H_m.                               \tag{1.5}
\]

The failure below is therefore specifically a failure of pointwise
localization, not of the still-live global sum.

## 2. Modular-parabola mass avoiding the short direction

Let (p) be an odd prime and take

\[
 P_p=\{(x,[x^2]_p):0\le x<p\}\subset[0,p-1]^2.        \tag{2.1}
\]

This is integer vector-Sidon.  Exact integer triple sums occupy fewer
than (9p^2) cells, while there are \(\binom p3\) unordered triples.
Cauchy--Schwarz and endpoint cancellation give

\[
 |\mathcal H_{P_p}|=\Omega(p^4).                       \tag{2.2}
\]

The only horizontal primitive direction is (w_0=(1,0)).  Since every
nonzero quadratic-residue level contains exactly two points,

\[
 e_{w_0}={p-1\over2}.                                  \tag{2.3}
\]

A fixed directed endpoint edge has hypergraph degree at most
(2\binom{p-2}{2}).  There are (2e_{w_0}) directed horizontal edges,
so the number of hyperedges containing any horizontal vector is at most

\[
 4e_{w_0}\binom{p-2}{2}=O(p^3).                       \tag{2.4}
\]

Consequently

\[
 \Omega(p^4)                                           \tag{2.5}
\]

hyperedges have all three primitive directions nonhorizontal.  Under
every assignment to a constituent direction, every one of these records
must be assigned to a nonhorizontal direction.

## 3. Euclideanizing shear and the budget contradiction

Apply the determinant-one shear

\[
 S_t(x,y)=(x+ty,y).                                    \tag{3.1}
\]

Choose an integer (t\ge2p) avoiding all squared-distance collision
polynomials.  There are (O(p^4)) unordered edge pairs and each gives a
nonzero polynomial of degree at most two, so a good

\[
 t=O(p^4)                                              \tag{3.2}
\]

exists.  The set (S_tP_p) is genuinely Euclidean distance-Sidon, has
height (m=O(p^5)), and preserves every hyperedge and direction
occupancy.

Let (w=(a,b)), (b\ne0), be a primitive direction before shearing.
Then \(|a|,|b|\le p\), and its primitive image is

\[
 w_t=(a+tb,b).                                         \tag{3.3}
\]

For (t\ge2p),

\[
 \|w_t\|_\infty\ge{t|b|\over2},
 \qquad
 M_{w_t}\le{3p\over|b|}.                              \tag{3.4}
\]

For a fixed \(|b|\), at most (2p+1) values of (a) occur.  Therefore

\[
 \sum_{b\ne0}M_{w_t}^2
 \ll p^2\sum_{b=1}^p{p\over b^2}
 \ll p^3.                                             \tag{3.5}
\]

Also

\[
 p\sum_{b\ne0}e_w\le p\binom p2=O(p^3).              \tag{3.6}
\]

Let (A_w^\star) be the loads produced by any rule assigning each
hyperedge to one of its constituent directions.  By (2.5),

\[
 \sum_{b\ne0}A_w^\star=\Omega(p^4).                   \tag{3.7}
\]

Equations (3.5)--(3.7) imply

\[
 \max_{b\ne0}{A_w^\star\over pe_w+M_w^2}
 \ge
 {\sum_{b\ne0}A_w^\star\over
  \sum_{b\ne0}(pe_w+M_w^2)}
 =\Omega(p).                                          \tag{3.8}
\]

Taking the shortest-primitive-direction rule gives (0.4).  Since
(k=p) and (m=O(p^5)), the loss in (3.8) is polynomial in the ambient
height and cannot be absorbed into (m^{o(1)}).

Why does this not contradict the desired global theorem?  The shear fixes
the horizontal direction, for which

\[
 M_{w_0}=m.                                            \tag{3.9}
\]

Its (m^2) budget can pay globally for the hyperedges in (2.5), but that
direction is absent from those hyperedges.  A constituent-only assignment
has no mechanism to make this transfer.

## 4. Exact certificate audit

For the genuine (p=43), (t=28) shear, the canonical shortest-direction
assignment has

\[
 \sum_wA_w=126852.
\]

Its largest pointwise ratio occurs at

\[
 w=(85,3),\qquad e_w=6,\qquad M_w={1175\over85},
 \qquad A_w=1648,
\]

and is

\[
 {1648\over43\cdot6+(1175/85)^2}
 ={476272\over129787}
 =3.669643\ldots.                                     \tag{4.1}
\]

The following larger genuine shear certificates show the predicted
growth.

\[
\begin{array}{c|rrrrrrrr}
p&7&13&23&43&47&59&71&79\\ \hline
\max_w A_w/(ke_w+M_w^2)
&0.125&0.305&1.356&3.670&4.698&6.144&9.103&10.113
\end{array}                                           \tag{4.2}
\]

The independent closure certificates are benign at the tested sizes:

\[
\begin{array}{c|rr}
\text{family}&|\mathcal H_A|&
\max_w A_w/(ke_w+M_w^2)\\ \hline
\text{closure-20}&432&0.169\\
\text{closure-40}&8280&0.349
\end{array}                                           \tag{4.3}
\]

These finite values are consistent with the asymptotic theorem: the
parabola, not the closure certificate, is the decisive constituent-charge
counterexample.

## 5. Consequence for the global directional program

The global directional midpoint bound remains a sufficient theorem:

\[
 \sum_wH_w\le m^{o(1)}
 \left(k\sum_we_w+\sum_wM_w^2\right).                 \tag{5.1}
\]

But Sections 2--3 show that (5.1) cannot arise by assigning each
hyperedge to its shortest, longest, largest-occupancy, or otherwise
preferred constituent direction and proving separate pointwise budgets.
The counterexample applies to every such assignment rule.

A viable charge must be nonlocal.  In the modular-parabola stress it must
detect that many long-direction records arise from one common shear and
send their mass to the short horizontal direction even though that
direction occurs in only (O(p^3)) of the hyperedges.  This is the exact
remaining cross-direction inverse theorem.

## 6. Verification

Run

    python3 phase2/loop/erdos1208/verify_shortest_primitive_direction_assignment_no_go.py

The verifier enumerates exact endpoint hyperedges from equal-centroid
triple cells, checks the three-vector closure, performs the canonical
assignment with deterministic tie-breaking, verifies the full (p=43)
extremizer, checks growth through (p=79), and audits the two closure
certificates.
