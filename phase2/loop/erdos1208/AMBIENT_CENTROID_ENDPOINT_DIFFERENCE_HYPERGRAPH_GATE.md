# Ambient centroid collisions as an endpoint-labelled difference hypergraph

## Status

Let $A\subset\mathbb Z^2$ be distance-Sidon, $k=|A|$, and let

\[
 \vec E(A)=\{(a,b):a,b\in A, a\ne b\},
 \qquad \delta(a,b)=b-a.
\]

This note gives an exact endpoint-retaining formulation of the ambient
equal-centroid gate.  Define a 3-uniform hypergraph \(\mathcal H_A\) on
the **directed endpoint edges** \(\vec E(A)\).  A three-set

\[
 \{(a_1,b_1),(a_2,b_2),(a_3,b_3)\}
\]

is a hyperedge when its six endpoints are distinct and

\[
 \delta(a_1,b_1)+\delta(a_2,b_2)+\delta(a_3,b_3)=0.       \tag{0.1}
\]

Then:

1. \(\mathcal H_A\) is linear: two directed endpoint edges occur together
   in at most one hyperedge.
2. If \(C_6(A)\) is the number of ordered six-distinct solutions of
   \(a_1+a_2+a_3=b_1+b_2+b_3\), then

   \[
    \boxed{C_6(A)=6|\mathcal H_A|.}                       \tag{0.2}
   \]

3. All zero-sum triples of realized directed differences which are not
   endpoint matchings contribute only \(O(k^3)\).  Thus the conjectural
   ambient third-energy estimate is exactly

   \[
    \boxed{|\mathcal H_A|\le m^{o(1)}(k^3+m^2).}          \tag{0.3}
   \]

4. The entire **collinear displacement** subhypergraph is already closed:

   \[
    \boxed{|\mathcal H_A^{\rm col}|
      \le {8\over3}(m-1)^2H_{m-1}.}                     \tag{0.4}
   \]

   This includes the one-dimensional/Golomb and parabolic displacement
   stresses.  The exact survivor consists of endpoint-disjoint zero-sum
   difference triangles of nonzero determinant.

5. More generally, for every real \(D_0\ge1\), the low-determinant branch
   obeys

   \[
    \boxed{
    |\{h\in\mathcal H_A:0<|\det h|\le D_0\}|
    \ll D_0(k^2+mk)
    \ll D_0(k^3+m^2).}                                  \tag{0.5}
   \]

   Therefore every determinant band \(0<|\det h|\le m^{o(1)}\) is also
   closed.  The exact survivor is the large-area matching hypergraph.

This is a useful reset after the failure of scalar-load and pointwise
translation-reuse bounds: (0.3) retains every endpoint, while discarding
no metric information other than the lengths themselves.

There is also a decisive limitation.  Linearity, endpoint completeness,
vector-Sidonicity, and the matching condition do **not** imply a near-
\(k^3\) bound.  The finite-field parabola gives endpoint-complete linear
hypergraphs with \(\Theta(k^4)\) hyperedges.  Its integral lifts preserve
\(\Theta(k^4)\) centroid records, and an integral shear makes them genuine
Euclidean distance-Sidon sets at polynomial height.  Therefore any proof
of (0.3) must quantitatively couple the endpoint hypergraph to the actual
integer Euclidean norm and ambient height.  Pure pair-codegree, matching,
or finite-group arguments cannot close the gate.

This does not disprove (0.3).  The computed Euclidean lifts pay for their
fourth-order hypergraph mass through the $m^2$ term.

## 1. Directed vectors remember their endpoints

Distance-Sidonicity implies directed-vector Sidonicity:

\[
 \delta(a,b)=\delta(c,d)\ne0
 \quad\Longrightarrow\quad (a,b)=(c,d).                 \tag{1.1}
\]

Indeed the two directed vectors have the same norm.  The corresponding
unordered endpoint pairs must therefore agree.  Equality rather than
opposition of the vectors fixes their orientation.

Consequently \(\delta:\vec E(A)\to(A-A)\setminus\{0\}\)
is a bijection.  This is the exact feature lost by replacing the complete
difference set by an arbitrary radial transversal.

## 2. Exact centroid--hyperedge correspondence

Take an ordered clean centroid record

\[
 (a_1,a_2,a_3;b_1,b_2,b_3),
 \qquad a_1+a_2+a_3=b_1+b_2+b_3,                         \tag{2.1}
\]

with six distinct endpoints.  Its three role-corresponding directed edges
form a matching, and (2.1) is exactly (0.1).  Conversely, a hyperedge of
\(\mathcal H_A\), together with an ordering of its three directed edges,
gives (2.1).  There are $3!=6$ such orderings, proving (0.2).

Equivalently, if $t_s$ counts three-subsets of $A$ with sum $s$, then

\[
 |\mathcal H_A|=6\sum_s t_s(t_s-1).                     \tag{2.2}
\]

Here $t_s(t_s-1)$ counts ordered pairs of distinct three-subsets.  Such
subsets are automatically disjoint: after cancelling a common point,
additive Sidonicity identifies the remaining unordered pairs.

Linearity is now immediate.  Given two vertices $e_1,e_2\in\vec E(A)$,
the vector of a possible third vertex is forced to be

\[
 -\delta(e_1)-\delta(e_2).
\]

By (1.1), it has at most one endpoint realization.  The realization may
fail the six-endpoint cleanliness condition, but it can never produce two
different hyperedges.

This proves a little more than an abstract pair-codegree statement.  For a
fixed directed edge $e=(a,b)$, its link gives a 2-bounded correspondence
between unordered source pairs and unordered target pairs.  Indeed, once
\(\{a_2,a_3\}\) is fixed, the target-pair sum is fixed by (2.1), and
additive Sidonicity gives at most one unordered target pair.  There are at
most two bijections between the two pairs, and both can genuinely occur.
The reverse statement is symmetric.  Thus

\[
 \deg_{\mathcal H_A}(e)\le 2{k-2\choose2}.               \tag{2.3}
\]

The quadratic order in (2.3) is real in finite-field models, so it is not
the missing estimate.

## 3. The automatic nonmatching part is only cubic

Every ordered zero-sum triple of realized differences is an ordered
solution of

\[
 a_1+a_2+a_3=b_1+b_2+b_3.                               \tag{3.1}
\]

If the three directed endpoint edges do not form a six-vertex matching,
some two of the six endpoint roles are equal.  There are 15 choices of a
pair of roles.  Fixing any one equality leaves at most $2k^3$ solutions.

For an equality between opposite sides, cancel the common variable; it is
free, and the remaining pair-sum equality has $2k^2-k$ ordered
solutions.  For an equality on one side, the standard Fourier bound is

\[
 \int_{\mathbb T^2}
 |\widehat{1_A}(2\theta)|
 |\widehat{1_A}(\theta)|^4\,d\theta
 \le k\int_{\mathbb T^2}|\widehat{1_A}(\theta)|^4d\theta
 =k(2k^2-k).                                            \tag{3.2}
\]

Haar measure is preserved by \(\theta\mapsto2\theta\).  A union bound
therefore gives

\[
 \#\{\text{nonmatching ordered solutions of (3.1)}\}
 \le30k^3.                                               \tag{3.3}
\]

Together with (0.2), this identifies \(\mathcal H_A\) as precisely the
nonautomatic part of the third additive energy.

## 4. The collinear displacement branch is ambient-paid

Let \(\mathcal H_A^{\rm col}\) consist of the hyperedges whose three
displacement vectors are collinear.  Since their sum is zero, their common
line passes through the origin.  Thus all three are integer multiples of
one primitive unoriented direction $w$.

Let

\[
 e_w=|\{\{a,b\}\in\tbinom A2:b-a\text{ is parallel to }w\}|. \tag{4.1}
\]

There are $2e_w$ directed endpoint edges in this direction.  Every
hyperedge produces six ordered choices of its first two vertices, while
the first two displacement vectors force the third.  Hence

\[
 6|\mathcal H_{A,w}^{\rm col}|\le(2e_w)^2,
 \qquad
 |\mathcal H_A^{\rm col}|\le {2\over3}\sum_we_w^2.       \tag{4.2}
\]

Put $M=m-1$ and $q=\|w\|_\infty$.  Every edge in direction $w$ has
vector \(\pm tw\), with $1\le t\le M/q$.  Two different endpoint edges
cannot use the same positive $t$, because they would have the same
Euclidean length.  Therefore

\[
 e_w\le\left\lfloor {M\over q}\right\rfloor.            \tag{4.3}
\]

There are at most $4q$ unoriented primitive integer directions of
sup-norm $q$.  Summing (4.3) gives

\[
 \sum_we_w^2
 \le4M^2\sum_{q=1}^M{1\over q}=4M^2H_M.                \tag{4.4}
\]

Equations (4.2)--(4.4) prove (0.4).  Notice that this theorem uses the
actual Euclidean endpoint realization twice: to identify directed vectors
with endpoint edges, and to make the scalar multiples $t$ Golomb-unique.

For a collinear distance-Sidon set all of \(\mathcal H_A\) lies in this
branch.  The classical ruler inequality \(\binom k2\le M\) then makes the
$m^2$ payment transparent.  In a noncollinear set, (0.4) removes exactly
the determinant-zero displacement cells without a pointwise load claim.

The noncollinear hypergraph is

\[
 \mathcal H_A^{\ne0}
 =\{h\in\mathcal H_A:
     \det(\delta(e_1),\delta(e_2))\ne0\}.               \tag{4.5}
\]

The absolute determinant is independent of the chosen two vertices of a
zero-sum triple and has only $O(m^2)$ possible values.  Computation shows
that its individual cells can already have substantial load on sheared
parabolas; no uniform divisor-load assertion is made here.  The missing
theorem is an aggregate bound for (4.5), not another treatment of the
collinear case.

### 4.1 The low-determinant lattice-coset theorem

For a directed realized difference \(q_1=(u,v)\), put

\[
 g=\gcd(|u|,|v|),\qquad w=q_1/g,\qquad Q=\|w\|_\infty.
\]

Fix a nonzero integer \(d\).  The equation

\[
 \det(q_1,q_2)=d                                      \tag{4.6}
\]

has no integral solution unless \(g\mid d\).  When it is soluble, all
solutions are one affine lattice coset

\[
 q_2=q_2^{(0)}+nw,\qquad n\in\mathbb Z.                \tag{4.7}
\]

One coordinate of \(w\) has absolute value \(Q\), so its intersection with
\([-M,M]^2\) contains at most

\[
 1+\left\lfloor {2M\over Q}\right\rfloor              \tag{4.8}
\]

points.  There are at most \(2D_0/g\) nonzero signed multiples of \(g\)
in \([-D_0,D_0]\).  Summing (4.8) over those determinants and then over
all directed realized \(q_1\) gives at most

\[
 2D_0k(k-1)+4D_0M
 \sum_{q\in(A-A)\setminus\{0\}}{1\over\|q\|_\infty}    \tag{4.9}
\]

ordered pairs \((q_1,q_2)\).

The remaining reciprocal sum is endpoint-metric.  If an unordered edge
has squared length \(n\), then
\(\|q\|_\infty\ge\sqrt{n/2}\), and its two orientations contribute at
most \(2\sqrt{2/n}\).  The \(\binom k2\) values of \(n\) are distinct
positive integers.  Hence

\[
 \sum_{q\in(A-A)\setminus\{0\}}{1\over\|q\|_\infty}
 \le2\sqrt2\sum_{n=1}^{\binom k2}n^{-1/2}
 \le4k.                                                \tag{4.10}
\]

Every hyperedge in the determinant band gives six ordered choices of
\((q_1,q_2)\), all with the same absolute determinant.  Dividing
(4.9) by six and using (4.10) proves the first inequality in (0.5).
Finally \(mk\le(m^2+k^2)/2\le(m^2+k^3)/2\), proving the second.

This theorem retains the actual endpoint metric through (4.10), while the
lattice-coset step (4.7) retains the signed area.  It covers fixed,
polylogarithmic, and more generally subpolynomial determinant cutoffs.
It does not sum the bands extending to determinant \(\Theta(m^2)\);
that large-area tail is the exact new incidence gate.

## 5. A finite-field endpoint-complete barrier

Let $p$ be an odd prime and put

\[
 P_p=\{(x,x^2):x\in\mathbb F_p\}\subset\mathbb F_p^2.   \tag{5.1}
\]

This set is directed-vector Sidon.  If two nonzero differences agree,
then their first coordinates give the same nonzero $h=x-y$, while their
second coordinates give $h(x+y)$.  Hence both the difference and sum of
the endpoints agree, which fixes the ordered pair.

There are $R={p\choose3}$ unordered source triples, and their sums have
only $p^2$ values.  If $t_s$ denotes their loads modulo $p$, then

\[
 \sum_s t_s(t_s-1)
 \ge {R^2\over p^2}-R=\Theta(p^4).                      \tag{5.2}
\]

Different triples in one cell are disjoint, by the same pair-sum
cancellation used above.  Therefore the endpoint-labelled hypergraph of
the finite-field parabola has

\[
 |\mathcal H_{P_p}|=6\sum_st_s(t_s-1)=\Theta(p^4).       \tag{5.3}
\]

It is linear and every vertex is an actual uniquely represented endpoint
difference.  One may even assign a distinct formal radius to every
unordered endpoint edge.  Thus endpoint completeness plus abstract radial
injectivity still permits fourth-order mass.  What is missing from that
formal model is compatibility of all radii with one positive-definite
integral quadratic form of controlled height.

## 6. Genuine Euclidean lifts: the height term is necessary

Use least nonnegative representatives in (4.1), obtaining a vector-Sidon
set in $[0,p-1]^2$.  Exact integer triple sums occupy at most $9p^2$
cells, so

\[
 \sum_s t_s(t_s-1)
 \ge {R^2\over9p^2}-R=\Omega(p^4)                       \tag{6.1}
\]

for all sufficiently large $p$.

For an integer $t$, apply the determinant-one shear

\[
 S_t(x,y)=(x+ty,y).                                     \tag{6.2}
\]

For two distinct unordered endpoint vectors $v\ne\pm w$, equality of
their post-shear squared norms is a nonzero quadratic polynomial in $t$:

\[
 (v_x+tv_y)^2+v_y^2=(w_x+tw_y)^2+w_y^2.                 \tag{6.3}
\]

It has at most two integer roots.  Hence some

\[
 0\le t\le2{\binom p2\choose2}                         \tag{6.4}
\]

avoids every collision.  The sheared set is genuinely Euclidean
distance-Sidon, has polynomial height $m=O(p^5)$, and preserves every
triple-sum equality.  Thus genuine distance-Sidon sets can have
\(\Omega(k^4)\) endpoint-hypergraph mass; a theorem without the $m^2$
alternative is false.

Small computed instances show the intended ambient behavior more sharply.
For the least-residue parabola, the first successful nonnegative shears are

\[
\begin{array}{c|rrrrrrrr}
p&7&11&13&17&19&23&29&43\\ \hline
t&4&6&6&11&10&13&14&28\\
m&21&62&80&189&183&249&409&1175.
\end{array}                                             \tag{6.5}
\]

Their exact integer centroid-pair counts are respectively

\[
 4,24,66,232,538,1442,3316,21142.                       \tag{6.6}
\]

The last family has $6\cdot21142$ directed hyperedges while
$m^2=1{,}380{,}625$; it is dense enough to kill a near-$k^3$ theorem,
but is comfortably paid for by the ambient term.

Its determinant profile also locates the residual accurately:

\[
\begin{array}{c|rrrrr}
|\mathcal H|&|\mathcal H^{\rm col}|&
|\{0<|\det h|\le10\}|&|\operatorname{supp}|\det h||&
\max_d|\{h:|\det h|=d\}|\\ \hline
126852&390&5278&1060&774.
\end{array}                                             \tag{6.7}
\]

Thus neither the collinear cell nor a fixed handful of tiny determinants
accounts for the finite-field stress.  The mass really moves into the
many-cell, nonzero-area tail, exactly as (0.4)--(0.5) predict.

## 7. Exact remaining theorem

After the scalar and pointwise-reuse failures, the live ambient statement
can be written without an auxiliary charge:

> **Endpoint difference-hypergraph gate.**  If
> $A\subset[m]^2$ is distance-Sidon, then the linear matching hypergraph
> \(\mathcal H_A\) defined by (0.1) has
> \(|\mathcal H_A|\le m^{o(1)}(k^3+m^2)\).

The finite-field and Euclideanized parabola audits show what a proof must
do.  It cannot use only:

* pair codegree one;
* the fact that every hyperedge is a three-edge endpoint matching;
* unique realization of every directed difference;
* injective formal norm labels; or
* a pointwise upper bound on one link degree.

It must show that a dense family of **nontransitive** zero-sum difference
triangles forces enough arithmetic height in the single Euclidean norm
realizing all endpoint edges.  Equivalently, it needs a quantitative
integer-Euclidean stability theorem for the finite-field/Singer-type
endpoint designs.  This is the precise remaining gap; linear-hypergraph
packing by itself bottoms out at $O(k^4)$.

## 8. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_ambient_centroid_endpoint_difference_hypergraph_gate.py
```

The verifier checks directed-vector injectivity, the exact factor in
(0.2), hypergraph linearity, the fixed-link 2-bounded property, the
collinear and low-determinant envelopes, finite-field parabola counts,
shear certificates, Euclidean distance uniqueness, determinant profiles,
and preservation of exact centroid records.
