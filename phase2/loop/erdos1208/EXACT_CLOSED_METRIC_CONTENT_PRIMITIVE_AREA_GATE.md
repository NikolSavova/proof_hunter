# Exact closure: metric contents and the primitive-area gate

## Status

The exact-dilation subfamily in
`GLOBAL_DIRECTIONAL_PAIR_ENERGY_PROJECTIVE_DILATION_AUDIT.md` has more
arithmetic structure than the flat projective relaxation.  If

\[
 q=b-a,\qquad q'=d-c,\qquad r=f-e
\]

and

\[
 g(b+c-a-d)=h(f-e),
\]

then, after orienting \(r\), the case \(h=g\) is precisely

\[
 q-q'=r.                                                \tag{0.1}
\]

Thus its three endpoint-edge vectors form an exact zero-sum triangle.
For a nonzero integer vector \(u\), put

\[
 c(u)=\gcd(|u_1|,|u_2|),\qquad L(u)=|u|^2.             \tag{0.2}
\]

If \(u_1+u_2+u_3=0\), put \(c_i=c(u_i)\), \(L_i=L(u_i)\),

\[
 D=|\det(u_1,u_2)|,qquad t=\gcd(c_1,c_2,c_3).         \tag{0.3}
\]

The exact metric/content laws are

\[
 \boxed{
 c_i\mid L_j-L_k,qquad
 c_ic_j\mid D,qquad
 t^2\mid D.}                                           \tag{0.4}
\]

The resulting **primitive-area key**

\[
 \boxed{\kappa(u_1,u_2,u_3)=\left(t,{D\over t^2}\right)} \tag{0.5}
\]

has only \(O(m^2)\) possible nonzero values for vectors in an
\(m\)-square.  It retains exact metric contents and the full ambient
\(m^2\) budget, unlike the flat direction energies discarded at the route
reset.

There is a rigorous tail theorem.  If \(\mathcal H_{\ge T}\) is the set
of clean noncollinear exact-closure hyperedges with common scale
\(t\ge T\), then

\[
 \boxed{
 |\mathcal H_{\ge T}|
 \le \sum_{d\ge T}
   \min\left\{k^2(k-1)^2,{16m^4\over d^4}\right\}
 \ll {m^4\over T^3}.}                                  \tag{0.6}
\]

Consequently this part is at the desired scale whenever

\[
 T\ge
 \left({m^4\over k^3+m^2}\right)^{1/3}.               \tag{0.7}
\]

The key is not pointwise divisor-small.  Polynomial-height balanced
modular-parabola lifts are genuine distance-Sidon sets, preserve every
exact edge content, and have \(\Omega(k^4)\) clean exact closures
distributed among only \(k^{2+o(1)}\) primitive-area values.  Hence one
cell of (0.5) has load \(k^{2-o(1)}\), and the charge energy is
\(k^{6-o(1)}\).  This rules out a near-injective or near-diagonal use of
(0.5).

The durable conclusion is therefore a theorem/barrier pair:

* the high common-content-scale tail is now paid directly by the ambient
  square;
* the remaining hard branch is \(t\) small, already including \(t=1\);
* that branch needs a global, size-biased packing theorem across
  primitive-area cells.  No per-cell divisor estimate can close it.

This does not solve Erdős 1208, but it is an exact content-aware
replacement for the discarded \(h/g\)-projective relaxation.

## 1. From \(h=g\) to a clean zero-sum edge triangle

Write the projective identity as

\[
 g(q-q')=hr.                                           \tag{1.1}
\]

The positive exact-dilation case is (0.1); the case \(h=-g\) becomes the
same identity after reversing \(r\).  Put

\[
 u_1=q,\qquad u_2=-q',\qquad u_3=-r.                   \tag{1.2}
\]

Then

\[
 u_1+u_2+u_3=0.                                       \tag{1.3}
\]

Distance-Sidonicity makes every nonzero directed difference recover its
ordered endpoints uniquely.  Thus if the six labels
\(a,b,c,d,e,f\) are distinct, (1.3) is exactly one clean endpoint
hyperedge, with no hidden representation multiplicity.  Conversely every
clean endpoint hyperedge has three choices of distinguished edge and is an
exact-dilation record after a suitable orientation.

The projective energy allowed arbitrary \(h/g\).  Equation (1.3) is the
additional integral closure that all statements below use.

## 2. Cyclic norm congruences and pair-content divisibility

Write

\[
 u_i=c_iw_i,qquad \gcd(|(w_i)_1|,|(w_i)_2|)=1.       \tag{2.1}
\]

From \(u_j+u_k=-u_i\),

\[
 L_j-L_k
 =(u_j-u_k)\mathbin\cdot(u_j+u_k)
 =-c_i(u_j-u_k)\mathbin\cdot w_i.                    \tag{2.2}
\]

This proves the first divisibility in (0.4), cyclically.  It includes the
more elementary distinguished-edge identity

\[
 |q|^2-|q-r|^2
 =2q\mathbin\cdot r-|r|^2
 =c(r)\left(2q\mathbin\cdot\operatorname{prim}(r)
             -c(r)|\operatorname{prim}(r)|^2\right). \tag{2.3}
\]

All three pairwise determinants have the same absolute value because of
(1.3).  Therefore

\[
 D=|\det(u_i,u_j)|
   =c_ic_j|\det(w_i,w_j)|,                            \tag{2.4}
\]

which proves \(c_ic_j\mid D\).  Since \(t\mid c_i,c_j\), it also proves
\(t^2\mid D\).

The side labels and area obey the metric Heron identity

\[
 \boxed{
 4D^2=2(L_1L_2+L_2L_3+L_3L_1)
       -(L_1^2+L_2^2+L_3^2).}                         \tag{2.5}
\]

Thus (0.4)--(0.5) are computable from the three unique squared-distance
labels together with their exact lattice contents.

## 3. Primitive-direction kernel and the meaning of \(t\)

Assume \(D\ne0\).  The integer matrix with columns
\(w_1,w_2,w_3\) has rank two.  Its signed-minor vector is

\[
 K=\bigl(\det(w_2,w_3),\det(w_3,w_1),
          \det(w_1,w_2)\bigr).                         \tag{3.1}
\]

Let \(d=\gcd(|K_1|,|K_2|,|K_3|)\).  Then \(K/d\) is the
primitive integral generator of the one-dimensional kernel.  Equation
(1.3) says that the signed content vector is an integral kernel vector, so

\[
 \boxed{(c_1,c_2,c_3)=t\,(|K_1|,|K_2|,|K_3|)/d}       \tag{3.2}
\]

after choosing the three primitive orientations compatibly.  In
particular the scalar in (3.2) is exactly
\(t=\gcd(c_1,c_2,c_3)\).

This gives a geometric interpretation of (0.5): divide the entire edge
triangle by its largest common integral dilation, then record its remaining
integer area.

## 4. The primitive-area range is ambient-sized

Every difference vector of points in \([0,m]^2\) lies in
\([-m,m]^2\), so

\[
 1\le D\le2m^2                                        \tag{4.1}
\]

in the noncollinear branch.  The number of possible keys (0.5) is at most

\[
 \sum_{t\le\sqrt2m}
 \left\lfloor{2m^2\over t^2}\right\rfloor
 \le {\pi^2\over3}m^2.                                \tag{4.2}
\]

This is the promised exact \(O(m^2)\)-range charge.  The collinear cell
\(D=0\) is not included; it is already bounded by the direction-occupancy
estimate \(O(m^2\log m)\) in
`AMBIENT_CENTROID_ENDPOINT_DIFFERENCE_HYPERGRAPH_GATE.md`.

## 5. High common-scale tail

Let \(\mathscr D=(A-A)\setminus\{0\}\).  For an integer \(d\ge1\), put

\[
 \mathscr D_d=\{u\in\mathscr D:d\mid c(u)\}.           \tag{5.1}
\]

If \(u\in\mathscr D_d\), then \(d^2\mid L(u)\).  The unordered squared
lengths are all distinct and lie in \([1,2m^2]\), while both orientations
of an edge occur in \(\mathscr D\).  Hence

\[
 \boxed{
 |\mathscr D_d|
 \le\min\left\{k(k-1),{4m^2\over d^2}\right\}.}      \tag{5.2}
\]

For a zero-sum directed triple, its first two vectors determine the third.
Thus the number of ordered zero-sum triples entirely in
\(\mathscr D_d\) is at most \(|\mathscr D_d|^2\).  Every clean hyperedge
whose exact common scale is \(t=d\) is among these triples.  Summing over
\(d\ge T\) proves the first inequality in (0.6), up to an inessential
absolute orientation factor.  Finally

\[
 \sum_{d\ge T}{16m^4\over d^4}
 \le {16m^4\over T^4}
     +16m^4\int_T^\infty{x^{-4}}\,dx
 \ll {m^4\over T^3},                                  \tag{5.3}
\]

which proves (0.6)--(0.7).

The proof uses both metric uniqueness and exact integral content.  It is
false for the flat \(h/g\) relaxation because there the three edge vectors
need not possess a common integral scale at all.

## 6. Sharp obstruction to pointwise charge control

Take the least-residue modular parabola

\[
 P_p=\{(x,[x^2]_p):0\le x<p\}.                        \tag{6.1}
\]

It is integer vector-Sidon and has \(\Omega(p^4)\) clean exact centroid
hyperedges.  Its determinants occupy only \(O(p^2)\) integer values.

Apply the balanced transform

\[
 L_s=\begin{pmatrix}s&-1\\1&s+1\end{pmatrix}.          \tag{6.2}
\]

The polynomial-height rough-sieve theorem in
`POLYNOMIAL_HEIGHT_BALANCED_SIEVE_GLOBAL_DIRECTIONAL_NO_GO.md` chooses
\(s=O(p^{16})\) so that:

1. \(L_sP_p\) is genuinely Euclidean distance-Sidon;
2. every transformed primitive active direction is primitive; and
3. the height is \(O(p^{17})\).

If a base edge is \(cw\) with \(w\) primitive, the second item gives
\(c(L_s(cw))=c\).  Thus the linear map preserves every edge content and
every common scale \(t\); it also multiplies every determinant by the same
nonzero integer \(\det L_s\).

The base determinants have only \(O(p^2)\) values.  For one determinant
\(D\), the possible common scales satisfy \(t^2\mid D\), so there are at
most \(\tau(D)=p^{o(1)}\) of them.  Consequently there are only
\(p^{2+o(1)}\) occupied primitive-area keys, carrying total load
\(\Omega(p^4)\).  Pigeonholing gives

\[
 \boxed{
 \max_z |\kappa^{-1}(z)|=p^{2-o(1)}.}                  \tag{6.3}
\]

Moreover, if \(R_\kappa(z)\) is the charge load, Cauchy gives

\[
 \sum_zR_\kappa(z)^2
 \ge {\Omega(p^8)\over p^{2+o(1)}}
 =p^{6-o(1)}.                                         \tag{6.4}
\]

Since the mass is only \(\Theta(p^4)\), no bound of the form

\[
 \sum_zR_\kappa(z)^2\le m^{o(1)}\sum_zR_\kappa(z)    \tag{6.5}
\]

is possible.  Indeed (6.3) itself is a fixed positive power of the
polynomial height.

For a small exact certificate, the balanced lift \(p=23,s=20\) has

\[
 k=23,\quad m=439,\quad
 |\mathcal H|=8652,\quad |\mathcal H_{\ne0}|=8588.     \tag{6.6}
\]

exact edge contents preserved, 278 occupied nonzero primitive-area keys,
maximum key load 156, and normalized charge energy

\[
 {\sum_zR_\kappa(z)^2\over|\mathcal H|}
 =72.69958081\ldots.                                  \tag{6.7}
\]

Thus the barrier is already visible well before the asymptotic sieve is
needed.

## 7. Exact remaining gate

The primitive-area key is useful only in a global, size-biased form.  The
high-scale theorem removes (0.7).  What remains is the family

\[
 t<\left({m^4\over k^3+m^2}\right)^{1/3},             \tag{7.1}
\]

especially the primitive branch \(t=1\).  Balanced Costas/parabola lifts
show that an occupied key may have polynomial load, but only at a height
where the full ambient \(m^2\) term can pay the aggregate.

A viable continuation must therefore prove a height-sensitive packing of
**all** heavy \((t,D/t^2)\) cells, with the six endpoints retained.  It
cannot bound cells independently, replace contents by primitive directions,
or discard exact closure.  The present theorem is a real tail reduction,
not a solution of that low-scale packing problem.

## 8. Verification

Run

    python3 phase2/loop/erdos1208/verify_exact_closed_metric_content_primitive_area.py

The verifier checks (0.4), the Heron identity, the signed-minor kernel law,
the range and high-scale counting inequalities, exact closure and
distance-Sidonicity, and primitive-area profiles on closure, modular, and
balanced modular certificates.
