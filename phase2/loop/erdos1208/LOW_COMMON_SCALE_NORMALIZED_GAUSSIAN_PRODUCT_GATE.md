# Low common scale: normalized Gaussian cells and the product gate

## Status

This note continues `EXACT_CLOSED_METRIC_CONTENT_PRIMITIVE_AREA_GATE.md`.
For a clean noncollinear exact-closure hyperedge, orient its three edge
vectors so that

\[
 u_1+u_2+u_3=0.                                      \tag{0.1}
\]

Put

\[
 t=\gcd(c(u_1),c(u_2),c(u_3)),\qquad
 a={|\det(u_1,u_2)|\over t^2}.                       \tag{0.2}
\]

Order the vectors by their distinct squared lengths and define the
normalized dot coordinate

\[
 x={u_1\mathbin\cdot u_2\over t^2}.                  \tag{0.3}
\]

The main new theorem is that every complete normalized Gaussian cell is
divisor-small:

\[
 \boxed{
 R(t,a,x)\le 24\tau(x^2+a^2)=m^{o(1)}.}             \tag{0.4}
\]

This turns a genuinely two-dimensional part of the low-common-content
branch into an ambient count.  If \(\mathcal H(Y)\) denotes the clean
noncollinear exact closures satisfying

\[
 |ax|\le Y,                                           \tag{0.5}
\]

then

\[
 \boxed{
 |\mathcal H(Y)|
 \le m^{o(1)}\bigl(m^2+mY^{3/4}\bigr).}              \tag{0.6}
\]

In particular,

\[
 \boxed{
 |ax|\le m^{4/3}\quad\Longrightarrow\quad
 |\mathcal H|\le m^{2+o(1)}.}                        \tag{0.7}
\]

The theorem includes all common scales \(t\), so it applies in particular
to the requested low-\(t\) branch.  Combined with the previous
\(m^4/T^3\) high-scale bound, the exact survivor is

\[
 t<T,\qquad |ax|>m^{4/3}.                            \tag{0.8}
\]

Thus both coordinates of the primitive Gaussian product must be jointly
large: small normalized area, small normalized dot product, and every
unbalanced pair whose product is below the threshold are now globally
paid by the full \(m^2\) budget.

This is not a full proof.  Balanced modular-parabola lifts stress the
remaining region sharply.  On the genuine \(p=23\), balanced-parameter
\(20\) certificate, all 8,588 noncollinear exact closures satisfy

\[
 |ax|>m^{4/3}.                                        \tag{0.9}
\]

They occupy heavy primitive-area cells but almost-diagonal complete
Gaussian cells.  Hence adding \(x\) repairs local multiplicity exactly,
while the unresolved issue is aggregation over many distinct large
\((a,x)\) cells.  No pointwise argument remains to be extracted.

The result is a substantive low-scale branch, not a solution of Erdős
1208.  The residual (0.8) still needs an endpoint-sensitive packing theorem
at the \(k^3+m^2\) scale.

## 1. Canonical normalized coordinates

Distance-Sidonicity makes the three squared edge lengths distinct.  Order
the three vectors so that

\[
 L_1=|u_1|^2<L_2=|u_2|^2<L_3=|u_3|^2.                \tag{1.1}
\]

Reversing all three vectors does not change any of \(t,a,x\), so the
coordinates are well-defined on an unoriented clean hyperedge.  Since
\(t\) divides both coordinates of every \(u_i\), put

\[
 v_i=u_i/t\in\mathbb Z^2,qquad
 \lambda_i=|v_i|^2=L_i/t^2.                           \tag{1.2}
\]

Then

\[
 a=|\det(v_1,v_2)|,qquad x=v_1\mathbin\cdot v_2.    \tag{1.3}
\]

The Gram determinant gives the exact Gaussian norm identity

\[
 \boxed{
 \lambda_1\lambda_2=x^2+a^2.}                       \tag{1.4}
\]

Equivalently, after identifying \(\mathbb Z^2\) with \(\mathbb Z[i]\),
the normalized Gaussian product \(v_1\overline{v_2}\) has real part
\(x\), imaginary part of absolute value \(a\), and norm
\(\lambda_1\lambda_2\).

## 2. Divisor-small complete cells

### Theorem 2.1

For fixed positive integers \(t,a\) and an integer \(x\), the number of
clean noncollinear exact-closure hyperedges with normalized coordinates
\((t,a,x)\) is at most

\[
 24\tau(x^2+a^2).                                     \tag{2.1}
\]

### Proof

Equation (1.4) says that \((\lambda_1,\lambda_2)\) is a positive factor
pair of \(x^2+a^2\).  There are at most \(\tau(x^2+a^2)\) ordered factor
pairs.

For fixed \(t\) and \(\lambda_i\), the original squared distance is
\(t^2\lambda_i\).  Distance-Sidonicity identifies its unordered endpoint
edge uniquely.  Each of the two edges has at most two orientations.  Once
the first two directed vectors are chosen, (0.1) forces the third vector,
whose endpoint realization is also unique if it exists.  Allowing the
three cyclic choices and both signs costs at most the displayed absolute
factor 24.  Endpoint cleanliness can only delete completions.  This proves
(2.1).

For vectors in an \(m\)-square,

\[
 |x|,a\le {2m^2\over t^2},qquad
 x^2+a^2\le8m^4.                                     \tag{2.2}
\]

The uniform divisor bound makes (2.1) \(m^{o(1)}\), proving (0.4).
\(\square\)

The theorem is the exact local repair demanded by the heavy
primitive-area cells.  Their load is not hidden multiplicity: it must be
spread over polynomially many distinct normalized dot products.

## 3. Counting the low-product region

Let \(a\ge1\), \(b=|x|\ge0\).  From (2.2), a cell can occur only when

\[
 t\le {\sqrt2m\over\sqrt{\max(a,b)}}                 \tag{3.1}
\]

for \(b>0\).  When \(b=0\), the number of possible \((t,a)\) is at most

\[
 \sum_{t\le\sqrt2m}
 \left\lfloor{2m^2\over t^2}\right\rfloor
 =O(m^2).                                             \tag{3.2}
\]

For \(b>0\) and \(ab\le Y\), the number of possible cells is at most a
constant times

\[
 m\sum_{ab\le Y}{1\over\sqrt{\max(a,b)}}.            \tag{3.3}
\]

By symmetry, restrict to \(a\ge b\).  If \(a\le\sqrt Y\), there are at
most \(a\) choices of \(b\), and their contribution is

\[
 \sum_{a\le\sqrt Y}{a\over\sqrt a}=O(Y^{3/4}).       \tag{3.4}
\]

If \(a>\sqrt Y\), there are at most \(Y/a\) choices, and

\[
 \sum_{\sqrt Y<a\le Y}{Y/a\over\sqrt a}
 =O(Y^{3/4}).                                         \tag{3.5}
\]

Thus (3.3) is \(O(mY^{3/4})\).  Multiply the total cell count from
(3.2)--(3.5) by the divisor-small load in Theorem 2.1.  This proves (0.6),
and (0.7) follows on taking \(Y=m^{4/3}\).

For an explicit low-common-scale cutoff \(t<T\), the same proof gives the
slightly sharper cell envelope

\[
 O\left(m^2+\sum_{ab\le Y}
   \min\left\{T,{m\over\sqrt{\max(a,b)}}\right\}\right), \tag{3.6}
\]

again up to \(m^{o(1)}\).  Formula (0.6) is cleaner and already uniform in
\(T\).

## 4. Stress profiles and the exact barrier

The verifier quotients no reversal symmetry, so every physical hyperedge
normally contributes the harmless baseline pair of reversed directed
records.  It reports

\[
 (H,\ |\operatorname{supp}(t,a)|,\max R(t,a),
 |\operatorname{supp}(t,a,x)|,\max R(t,a,x),
 E_{t,a,x}/H,\ H(|ax|\le m^{4/3})).                   \tag{4.1}
\]

\[
\begin{array}{c|r|r|r|r|r|c|r}
\text{family}&H&|\operatorname{supp}(t,a)|&\max R(t,a)&
|\operatorname{supp}(t,a,x)|&\max R(t,a,x)&E/H&\text{low product}\\ \hline
\text{closure }20&432&187&6&215&4&2.018519&54\\
\text{closure }40&8274&2752&24&4130&4&2.006768&346\\
\text{modular }23&8588&278&156&4211&4&2.077317&402\\
\text{modular }43&126462&1412&664&62005&8&2.079202&2656\\
\text{balanced }23&8588&278&156&4216&4&2.072660&0
\end{array}                                           \tag{4.2}
\]

The complete cells are essentially diagonal on every stress, including
the heavy primitive-area examples.  But this does not finish the global
sum: the balanced lift moves all of its mass into distinct large-product
cells.  Its large ambient height pays that support, exactly as a correct
\(m^2\)-sensitive theorem must allow.

The critical-height closure profile is more important diagnostically than
the tall modular one.  Already at \(k=40,m=223\), only about 4.2 percent of
its noncollinear mass lies in (0.7).  Therefore the product theorem is a
real rigorous deletion, but not numerically close to exhausting the hard
core.

## 5. Remaining gate

Combining the two content-aware theorems leaves only

\[
 \boxed{
 t<T,qquad
 \left|{\det(u_1,u_2)\over t^2}
       {u_1\mathbin\cdot u_2\over t^2}\right|
 >m^{4/3-o(1)}.}                                      \tag{5.1}
\]

Every fixed full Gaussian cell in this region is already divisor-small.
The missing estimate is purely an aggregate packing theorem for many
large primitive Gaussian products, with the common endpoint coboundary and
six-label cleanliness retained.  Radial uniqueness or local factorization
alone has now been fully spent.

## 6. Verification

Run

    python3 phase2/loop/erdos1208/verify_low_common_scale_normalized_gaussian_product.py

The verifier checks exact zero-sum orientation, common-scale divisibility,
the Gram/Gaussian identity, the divisor cell bound, the elementary product
cell count, genuine distance-Sidonicity, and every profile in (4.2).
