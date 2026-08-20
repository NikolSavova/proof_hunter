# Fully transverse equal-area gate and the fixed-area incidence branch

## Status

The corrected equal-area route remains live, but its unresolved part can be
narrowed twice beyond the parallel-side theorem.

1. Cyclic reindexing shows that all geometric triangle pairs having **any**
   parallel cross-side pair are already controlled by the corresponding-side
   theorem.  It is enough to study pairs for which all nine source--target
   side pairs are nonparallel.
2. For an integer distance-Sidon set, the load of every fixed nonzero signed
   area is $m^{o(1)}k^2$.  This follows from a divisor bound on coincident
   translated base lines and the Szemerédi--Trotter theorem.  Consequently
   the entire nonzero area energy is $m^{o(1)}k^5$, which proves the corrected
   target whenever $m\ge k^{5/2}$.

The genuinely open range is therefore

\[
 m<k^{5/2},                                             \tag{0.1}
\]

and the remaining records may be assumed six-distinct and fully transverse.
Exact closure-set stress shows that this is not cosmetic: between 99.1% and
99.9% of the six-distinct equal-area energy in the tested certificates is
already fully transverse.

## 1. General-position qualification for special-affine overlaps

Let $A\subseteq\mathbb Z^2$, and let $\mathcal G(A)$ be the finite family of
special-affine maps arising from pairs of ordered noncollinear triangles of
the same signed doubled area.  Put

\[
 B_g=A\cap g^{-1}A.
\]

If $T_{\rm nc}(B)$ is the number of ordered noncollinear triples of distinct
points in $B$, then the exact identity is

\[
 \boxed{
 \mathcal E_{\Delta,\ne0}(A)
 =\sum_{g\in\mathcal G(A)}T_{\rm nc}(B_g).}             \tag{1.1}
\]

Only in general position may $T_{\rm nc}(B_g)$ be replaced by
$(|B_g|)_3$.  For arbitrary distance-Sidon sets one merely has

\[
 \mathcal E_{\Delta,\ne0}(A)
 \le\sum_g(|B_g|)_3.                                   \tag{1.2}
\]

For the six-distinct energy, a term from $g$ is retained only when the
three selected arcs $x\mapsto g(x)$ have six distinct endpoints.

## 2. Cyclic upgrade to full transversality

Regard a geometric triangle as an unordered three-point set and its three
sides as an unordered set of directions.  A pair of geometric triangles of
the same nonzero absolute area has exactly 18 pairs of ordered
representatives with equal signed area: nine positive--positive and nine
negative--negative.

### Lemma 2.1

Let $T,U$ be two geometric triangles of the same nonzero absolute area.  If
some side of $T$ is parallel to some side of $U$, then at least six of their
18 equal-signed ordered representative pairs have a pair of corresponding
parallel sides.  Consequently

\[
 \boxed{
 E_{\rm any\ cross\ parallel}^{(6)}
 \le3E_{\rm corresponding\ parallel}^{(6)}.}           \tag{2.1}
\]

### Proof

Fix an orientation sign.  There are three cyclic orderings of each triangle.
A selected parallel side pair determines one cyclic shift between these
orderings for which the two sides correspond.  The three choices of the
source starting vertex then give three ordered representative pairs.  The
opposite orientation sign gives three more.  Thus at least six of the 18
pairs are counted by the corresponding-parallel energy.  Summing geometric
pairs proves (2.1).  QED.

Combining (2.1) with `CORRECTED_EQUAL_AREA_AMBIENT_GATE.md`, all records
having any parallel cross-side pair contribute at most

\[
 m^{o(1)}\bigl(k^3+m^2\log(2m)\bigr).                  \tag{2.2}
\]

It remains to count pairs with side vectors $e_1,e_2,e_3$ and
$e'_1,e'_2,e'_3$ satisfying

\[
 \det(e_i,e'_j)\ne0\qquad(1\le i,j\le3).              \tag{2.3}
\]

This is the **fully transverse** gate.

## 3. Fixed-area translated-line multiplicity

For a nonzero integer $d$ and an oriented edge $(a,b)$ define its top line

\[
 \ell_{ab,d}=\{x\in\mathbb R^2:
                  \det(b-a,x-a)=d\}.                  \tag{3.1}
\]

An incidence $c\in A\cap\ell_{ab,d}$ is exactly an ordered triangle
$(a,b,c)$ of signed doubled area $d$.

### Lemma 3.1

If $A\subseteq\{0,\ldots,m\}^2$ is distance-Sidon, every geometric line
occurs among the **incident** lines $\ell_{ab,d}$ with multiplicity at most

\[
 2\tau(|d|),                                            \tag{3.2}
\]

where $\tau$ is the positive divisor function.

### Proof

If several lines in (3.1) coincide, their base edges are parallel.  Choose
the common primitive unoriented direction $u$.  Write the directed edge
vector as $tu$, with signed $t\in\mathbb Z\setminus\{0\}$, and put
$\sigma_t=\det(u,a)$.  The line equation is

\[
 \det(u,x)=\sigma_t+\frac dt.                           \tag{3.3}
\]

Because the line is incident to an integer point of $A$, both sides except
$d/t$ are integers, so $t\mid d$.  For a fixed signed $t$, distance-Sidonicity
allows at most one oriented edge: two would have the same squared length
$t^2\lVert u\rVert^2$.  There are at most $2\tau(|d|)$ signed divisors.
QED.

### Theorem 3.2 (fixed nonzero area)

Let

\[
 r_A(d)=|\{(a,b,c)\in A^3:\ a,b,c\text{ distinct},
                    \ \Delta(a,b,c)=d\}|.
\]

For every $d\ne0$,

\[
 \boxed{r_A(d)\ll \tau(|d|)k^2\le m^{o(1)}k^2.}       \tag{3.4}
\]

### Proof

Discard top lines containing no point of $A$.  There are at most $k(k-1)$
distinct lines before multiplicity.  Lemma 3.1 bounds every weight by
$2\tau(|d|)$.  The Szemerédi--Trotter incidence theorem gives, for a set of
$k$ points and at most $k(k-1)$ distinct lines,

\[
 I\ll k^{2/3}(k^2)^{2/3}+k+k^2\ll k^2.
\]

Multiplying by the maximum line weight proves the first inequality.  Since
$|d|\le2m^2$, the standard divisor estimate proves the second.  QED.

This improves the general real-point fixed-area bound in the present
integer distance-Sidon setting.  For context, the best general bound is
$O(k^{20/9})$:

> Orit E. Raz and Micha Sharir, *The Number of Unit-Area Triangles in the
> Plane: Theme and Variations*, SoCG 2015 / Combinatorica 37 (2017),
> <https://arxiv.org/abs/1501.00379>.

## 4. A complete high-height branch

There are fewer than $k^3$ ordered noncollinear triangles in total.  Hence
Theorem 3.2 gives

\[
 \begin{aligned}
 \mathcal E_{\Delta,\ne0}(A)
 &=\sum_{d\ne0}r_A(d)^2\\
 &\le\left(\max_{d\ne0}r_A(d)\right)
       \sum_{d\ne0}r_A(d)\\
 &\ll m^{o(1)}k^5.                                     \tag{4.1}
 \end{aligned}
\]

Therefore:

### Corollary 4.1

If $m\ge k^{5/2}$, then

\[
 \boxed{
 \mathcal E_{\Delta,\ne0}^{(6)}(A)
 \le\mathcal E_{\Delta,\ne0}(A)
 \ll m^{o(1)}m^2
 \le m^{o(1)}(k^3+m^2).}                               \tag{4.2}
\]

Thus the corrected equal-area gate is already proved throughout the
high-height range.  In particular, the polynomial-height constructions in
`EQUAL_AREA_TRIANGLE_ENERGY_BARRIER.md`, whose heights are $k^5$ or larger,
cannot obstruct the corrected route.

## 5. Cross-determinant array in the remaining range

For a fully transverse pair, cyclically orient its side vectors so

\[
 e_1+e_2+e_3=0,qquad e'_1+e'_2+e'_3=0,qquad
 \det(e_1,e_2)=\det(e'_1,e'_2)=d\ne0.                  \tag{5.1}
\]

Define the $3\times3$ integer array

\[
 K_{ij}=\det(e_i,e'_j).                                 \tag{5.2}
\]

It has the exact properties

\[
 K_{ij}\ne0,qquad
 \sum_iK_{ij}=\sum_jK_{ij}=0,                          \tag{5.3}
\]

and its leading block satisfies the Plücker identity

\[
 \boxed{K_{11}K_{22}-K_{12}K_{21}=d^2.}                \tag{5.4}
\]

Indeed, if $E=[e_1\ e_2]$, $E'=[e'_1\ e'_2]$, and
$J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$, then the
leading block is $E^{\mathsf T}JE'$, whose determinant is
$\det(E)\det(E')=d^2$.

For a fixed source triangle, the leading $2\times2$ block determines
$e'_1,e'_2$ uniquely over $\mathbb Q$; if those are actual directed edge
vectors of a distance-Sidon set, each has at most one realization.  The
remaining obstruction is not fibre multiplicity but the number of possible
integer arrays (5.3)--(5.4) that can coexist with clean endpoints and metric
labels.

## 6. Stress result and exact remaining gate

The verifier computes six-distinct geometric area energy and its fully
transverse part on the closure certificates:

| $k$ | side $m$ | six-distinct energy | fully transverse | fraction |
|---:|---:|---:|---:|---:|
| 20 | 75 | 15,516 | 15,372 | 0.9907 |
| 40 | 223 | 258,624 | 256,824 | 0.9930 |
| 80 | 719 | 2,588,364 | 2,582,208 | 0.9976 |
| 120 | 1,514 | 9,058,968 | 9,048,816 | 0.9989 |

Thus parallel cross-sides are negligible on this adversarial family.  The
parallel theorem is valid and necessary, but it does not by itself reduce
the dominant generic energy.

After the results above, the exact live target is:

\[
 \boxed{
 m<k^{5/2},\quad
 \mathcal E_{\rm fully\ transverse}^{(6)}(A)
 \stackrel{?}{\le}m^{o(1)}(k^3+m^2).}                 \tag{6.1}
\]

A successful continuation must use the clean endpoint realization and the
six globally distinct metric labels of the two triangles to compress the
cross-determinant arrays (5.3)--(5.4).  Direction occupancy, fixed-area
incidence, and the special-affine overlap size alone have now been fully
accounted for.

## 7. Verification

Run:

```bash
python phase2/loop/erdos1208/verify_fully_transverse_equal_area_incidence_gate.py
```

The verifier checks the translated-line divisor lemma, exact fixed-area
loads, the cyclic factor-three reduction, the cross-determinant identities,
and the four closure profiles above.
