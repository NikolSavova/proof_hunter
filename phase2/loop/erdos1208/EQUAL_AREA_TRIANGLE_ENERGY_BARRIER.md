# Equal-area triangle energy: a general-position fourth-order barrier

## 1. Verdict

For an ordered triangle of distinct points put

\[
 \Delta(a,b,c)=\det(b-a,c-a),
 \qquad r(d)=|\{(a,b,c):\Delta(a,b,c)=d\}|,               \tag{1.1}
\]

and define the signed-area energy

\[
 \mathcal E_\Delta(A)=\sum_d r(d)^2.                     \tag{1.2}
\]

The direct area route would need

\[
 \mathcal E_\Delta(A)\le m^{o(1)}k^3                    \tag{1.3}
\]

for a distance-Sidon set `A subset [0,m]^2`, after disposing of the
collinear part.  Estimate (1.3) is false by a full factor `k`, even in
general position and at polynomial height.

More strongly, there are arbitrarily large integral distance-Sidon sets
`A`, with `k=|A|`, height `m<=k^9`, and no three collinear, for which

\[
 \boxed{
 \mathcal E_\Delta^{(6)}(A)\gg k^4,}                     \tag{1.4}
\]

where `E_Delta^(6)` counts only equal-area pairs whose two triangles have
six distinct vertices.  Thus deleting the zero-area cell, all same-triangle
symmetries, and every shared-vertex collision does not repair the moment.

The mechanism is structural.  Equal signed area is invariant under
determinant-one affine maps.  A vector-Sidon integer set can be made
Euclidean distance-Sidon by a polynomial-height unimodular specialization,
without changing a single area class.  A dense modular parabola already has
fourth-order area energy.

The purely collinear branch is harmless for the original problem: a
collinear integral distance-Sidon set is a Golomb ruler and has

\[
 \binom k2\le m.                                          \tag{1.5}
\]

It is nevertheless catastrophic for area energy, since every triangle has
area zero.  The general-position construction (1.4) shows that this is not
merely a ruler pathology.

## 2. Why near-diagonal area energy would have closed the problem

There are

\[
 R=k(k-1)(k-2)                                           \tag{2.1}
\]

ordered, pairwise-distinct triangles.  Since every coordinate difference
lies in `[-m,m]`, the signed doubled area has at most `4m^2+1` possible
values.  Cauchy--Schwarz gives

\[
 \mathcal E_\Delta(A)
 \ge {R^2\over4m^2+1}.                                   \tag{2.2}
\]

Combining (2.2) with (1.3) would give

\[
 k^3\le m^{2+o(1)},                                      \tag{2.3}
\]

which is exactly the cube-root upper bound.  The rest of this note proves
that distance uniqueness supplies no such upper moment, even after the
strongest overlap pruning.

## 3. The collinear/ruler branch

Suppose `A` lies on an affine line.  There are a primitive vector
`w in Z^2`, a point `a_0`, and distinct integers

\[
 n_1<\cdots<n_k
\]

such that `A={a_0+n_iw}`.  All Euclidean distances are distinct precisely
only if all positive gaps `n_j-n_i` are distinct.  Put `L=n_k-n_1`.
There are `binom(k,2)` distinct positive integer gaps in `[1,L]`, so

\[
 \binom k2\le L.                                         \tag{3.1}
\]

Because the points lie in an `m by m` box and at least one coordinate of
the primitive vector has absolute value at least one, `L<=m`.  This proves
(1.5), and hence `k=O(sqrt(m))` in the collinear branch.

On the other hand, its area energy is `R^2=Theta(k^6)`.  A proof based on
area must therefore split this branch.  Sections 5--6 show that splitting
all collinear triples still leaves a fourth-order obstruction.

## 4. Unimodular Euclideanization

### Lemma 4.1

Let `P subset Z^2` be an `n`-point vector-Sidon set contained in a box of
height `M`.  There is an integer

\[
 0\le t\le2\binom{\binom n2}{2}                           \tag{4.1}
\]

such that

\[
 S_t(x,y)=(x+ty,y)                                       \tag{4.2}
\]

maps `P` to a Euclidean distance-Sidon set.  The output height, after a
translation, is `O(Mn^4)`.  Moreover

\[
 \det S_t=1,
 \qquad
 \Delta(S_ta,S_tb,S_tc)=\Delta(a,b,c).                   \tag{4.3}
\]

### Proof

Represent every unordered edge by either one of its two directed vectors.
Vector-Sidonicity says that distinct unordered edges have vectors
`v,w` with \(v\ne\pm w\).  Their squared lengths after (4.2) are

\[
 Q_v(t)=(v_x+tv_y)^2+v_y^2.                              \tag{4.4}
\]

The polynomial `Q_v-Q_w` is nonzero.  Indeed, equality of all three
coefficients would first give \(v_y=\pm w_y\); the linear and constant
coefficients then give \(v=\pm w\).  Each pair of edges
therefore forbids at most two integers `t`.  The interval in (4.1) has one
more integer than the total number of possible forbidden roots.  This
proves distance uniqueness.  The height and determinant assertions are
immediate.  QED.

The lemma is the central no-go: any high determinant energy already present
in a vector-Sidon model survives the imposition of distinct Euclidean
lengths at only polynomial height cost.

## 5. A one-copy general-position barrier

Let `p` be an odd prime and take least nonnegative residues

\[
 P_p=\{(x,[x^2]_p):0\le x<p\}.                           \tag{5.1}
\]

This is vector-Sidon.  Equality of two nonzero directed differences,
reduced modulo `p`, gives

\[
 x-y=u-v,
 \qquad x^2-y^2=u^2-v^2.                                 \tag{5.2}
\]

The first difference is nonzero modulo `p`, so (5.2) determines the sums
`x+y=u+v`, and hence the two ordered endpoints.

No three points of `P_p` are collinear: reduction modulo `p` would put three
points of the finite-field parabola on one line, whereas a nonvertical line
meets it in at most two points and a vertical line in one.

All triangles lie in a `(p-1) by (p-1)` box, so their signed areas occupy at
most

\[
 4(p-1)^2+1                                               \tag{5.3}
\]

integer values.  Every triangle is nonzero, and there are
`p(p-1)(p-2)` ordered triangles.  Therefore

\[
 \mathcal E_\Delta(P_p)
 \ge {p^2(p-1)^2(p-2)^2\over4(p-1)^2+1}
 \gg p^4.                                                \tag{5.4}
\]

Apply Lemma 4.1.  The resulting set `S_tP_p` is distance-Sidon, has no
three collinear, has height `O(p^5)`, and has exactly the same signed-area
loads.  Consequently no estimate

\[
 \mathcal E_\Delta(A)\le k^{4-epsilon}
 \quad\hbox{or}\quad
 \mathcal E_\Delta(A)\le m^{o(1)}k^3                    \tag{5.5}
\]

can hold for all polynomial-height distance-Sidon sets.

This already kills the raw area-energy route.  The next section removes the
possible objection that the energy in (5.4) might come from two triangles
sharing vertices.

## 6. A six-distinct-vertex strengthening

### Theorem 6.1

For every odd prime `p` there is an integral distance-Sidon set `A_p` with

\[
 |A_p|=2p,
 \qquad m(A_p)=O(p^9),
 \qquad \max_\ell|A_p\cap\ell|\le2,                      \tag{6.1}
\]

such that

\[
 \mathcal E_\Delta^{(6)}(A_p)\ge2\mathcal E_\Delta(P_p)
 \gg p^4\asymp |A_p|^4.                                 \tag{6.2}
\]

### Proof

Take two labeled copies of `P_p`.  We claim that there are
`T_1,T_2 in SL_2(Z)` and `R in Z^2` such that

\[
 A_p=T_1P_p\ \cup\ (R+T_2P_p)                            \tag{6.3}
\]

is distance-Sidon and has no three collinear.

This is a finite polynomial-avoidance statement.  Use the following
two-parameter family of integral determinant-one matrices:

\[
 \Phi(alpha,beta)
 =\begin{pmatrix}1&alpha\\0&1\end{pmatrix}
  \begin{pmatrix}1&0\\beta&1\end{pmatrix}
 =\begin{pmatrix}1+alpha beta&alpha\\beta&1\end{pmatrix}.
                                                               \tag{6.4}
\]

This family has the two separation properties needed below.  First, if the
norm polynomials of `v,w` agree identically, setting `beta=0` and using the
coefficient argument from Lemma 4.1 gives \(v=\pm w\).  Second, the norm
polynomial of every nonzero `v` is nonconstant: vary `alpha` when `v_y` is
nonzero and vary `beta` when `v_y=0`.  Use independent parameter pairs for
`T_1,T_2`, together with the two coordinates of `R`.

For every two distinct labeled edges, equality of their squared lengths is
a nonzero polynomial in these six parameters:

* for two internal edges in one copy, nonzeroness follows from
  vector-Sidonicity and the first separation property of (6.4);
* for internal edges in different copies, the two matrices vary
  independently;
* an internal--cross comparison varies nontrivially with `R`;
* orienting cross edges from the first copy to the second, two of them have
  vectors `R+T_2y-T_1x` and `R+T_2y'-T_1x'`.  Their squared-length
  difference has linear coefficient

  \[
   2\{T_2(y-y')-T_1(x-x')\}                              \tag{6.5}
  \]

  in `R`, which is not identically zero unless the two labeled edges are
  equal.

Point coincidences and mixed collinear triples are likewise proper
polynomial conditions.  Triples internal to one copy are already
noncollinear.  Hence the product of all forbidden polynomials is nonzero.

There are `O(p^4)` factors, each of bounded degree after (6.4).  The grid
nonvanishing lemma supplies integer parameters of size `O(p^4)`: a nonzero
polynomial of total degree `D` cannot vanish on all of `{0,...,D}^6`.
The entries in (6.4) are quadratic in the parameters, so (6.1) follows.

Both transformations have determinant one.  Thus triangles wholly in the
first and second copies have identical signed-area load functions.  Every
pair consisting of one such triangle from each copy uses six distinct
vertices.  Both orders of the two copies contribute, giving (6.2).  QED.

## 7. Exact certificates

For `p=43`, the single shear `t=28` already makes `S_tP_p` distance-Sidon.
It has height `1175`, no collinear triple, and the exact profile

\[
\begin{array}{c|r}
\text{unordered absolute-area support}&1024\\
\text{maximum unordered load}&79\\
\mathcal E_\Delta&5,877,918\\
\mathcal E_\Delta^{(6)}&4,538,340
\end{array}                                               \tag{7.1}
\]

so even the six-distinct part is already visible within one copy.

There is also a 22-point exact two-copy certificate.  For `p=11`, use

\[
 T_1=\begin{pmatrix}339&-652\\13&-25\end{pmatrix},
 \qquad
 T_2=\begin{pmatrix}-17&312\\-3&55\end{pmatrix},
 \qquad R=(-17,-62).                                     \tag{7.2}
\]

Both determinants are one.  The union is distance-Sidon, has no collinear
triple, and fits after translation in a square of side `7591`.  Each copy
has signed-area energy `17,226`; the full union has

\[
 \mathcal E_\Delta=90,792,
 \qquad
 \mathcal E_\Delta^{(6)}=46,188.                         \tag{7.3}
\]

The two directions of the copy-to-copy contribution alone account for
`34,452` of (7.3).

Run

```text
python3 phase2/loop/erdos1208/verify_equal_area_triangle_energy_barrier.py
```

for every exact distance, determinant, collinearity, energy, overlap, and
height check.

## 8. Research consequence

Signed area has the perfect ambient range, but the wrong collision order.
At dense vector-Sidon scale, roughly `k^3` triangles can occupy only
`Theta(k^2)` determinant values, forcing fourth-order energy.  Unimodular
Euclideanization shows that distinct Euclidean lengths do not disturb this
affine phenomenon.

Therefore no proof of the cube-root bound can use an unweighted upper bound
for equal-area triangle energy, even after removing all collinear and
shared-label pairs.  Any future determinant argument must couple area to a
non-affine metric label (such as the trace coordinate) or to the clean
endpoint translation; area alone is a rigorously closed lane.
