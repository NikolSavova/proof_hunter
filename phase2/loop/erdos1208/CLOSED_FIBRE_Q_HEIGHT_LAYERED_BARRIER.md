# The closed-fibre \(Q\) gate: height equality and the layered radial barrier

## 1. Verdict

Let \(A\subset[0,m]^2\cap\mathbb Z^2\) be distance-Sidon, let
\(\mathscr D=(A-A)\setminus\{0\}\), and put \(N=k(k-1)\).  Retain the
notation of `LARGE_DETERMINANT_CLOSED_FIBRE_ENERGY_GATE.md`:

\[
 \mathcal Q_D(A)=\sum_{w,r}
 \min\left\{\binom{B_w(r)}2,\alpha_{w,D}(r)B_w(r)\right\}. \tag{1.1}
\]

The proposed estimate

\[
 \sum_D\mathcal Q_D(A)
 \le m^{o(1)}(k^3+m^2)                              \tag{1.2}
\]

survives every genuine distance-Sidon stress tested.  Two rigorous facts
substantially narrow its scope.

1. There is a lossless universal high-height estimate

   \[
    \boxed{\sum_D\mathcal Q_D(A)\le {N^2\over2}.}    \tag{1.3}
   \]

   Hence (1.2) is already proved whenever \(m\ge N\), in particular in
   the exponent range \(m\ge k^{2+o(1)}\).

2. The explicit Euclideanized finite-field parabola has

   \[
    k=p,\qquad m=\Theta(p^2),\qquad
    \sum_D\mathcal Q_D(A_p)=\Theta(p^4)=\Theta(m^2). \tag{1.4}
   \]

   Thus the ambient term in (1.2) is sharp for this exact functional.

There is also a decisive no-go result.  Common endpoint realization and
directed-vector uniqueness do **not** suffice.  For every odd prime \(p\)
there is an actual integer point set \(A_p^{\rm lay}\), with

\[
 k=p^2,qquad m=O(p^3)=O(k^{3/2}),                   \tag{1.5}
\]

whose directed differences are all distinct, but whose horizontal
closed-fibre contribution obeys

\[
 \boxed{\mathcal Q^{\rm hor}(A_p^{\rm lay})
 \ge {1\over3}p^7-O(p^6)=\Omega(k^{7/2}).}          \tag{1.6}
\]

This would violate (1.2) by a factor \(k^{1/2}\).  The set is not
distance-Sidon: reflected difference vectors create equal Euclidean
norms.  An explicit dominance transform turns it into a genuine
distance-Sidon set while preserving (1.6), but raises the height to
\(O(p^4)=O(k^2)\), where \(m^2\) pays for all the mass.

Consequently the load-bearing input is now exact: a proof of (1.2) must
couple **Euclidean radial uniqueness with ambient height across different
closed fibres**.  The endpoint cocycle, vector injectivity, the exact
closing equation, and any pointwise fibre estimate are insufficient.

## 2. Two universal reductions

For a fixed primitive direction \(w\), let \(e_w=|T_w|\).  For every
\(r\ne0\), the dyadic bands partition \(T_w\):

\[
 \sum_D\alpha_{w,D}(r)=e_w.                         \tag{2.1}
\]

The fibres partition \(\mathscr D\), so \(\sum_rB_w(r)=N\).  Also every
unordered endpoint edge supplies exactly one positive content to exactly
one primitive direction.  Distance-Sidonicity makes these contents
distinct inside each direction, and hence

\[
 \sum_we_w={N\over2}.                               \tag{2.2}
\]

Using the linear side of every minimum gives

\[
\begin{aligned}
 \sum_D\mathcal Q_D(A)
 &\le\sum_{w,r\ne0}B_w(r)\sum_D\alpha_{w,D}(r)\\
 &\le N\sum_we_w={N^2\over2},                       \tag{2.3}
\end{aligned}
\]

which proves (1.3).

There is a second useful reduction.  Define the direction-restricted
pair energy

\[
 \mathcal P(A)=\sum_{w,r\ne0}\binom{B_w(r)}2.       \tag{2.4}
\]

It counts unordered pairs \(q,q'\in\mathscr D\) for which \(q-q'\) is
parallel to an endpoint-edge direction.  Since

\[
 g|r|=|\det(gw,q)|\le2m^2,                          \tag{2.5}
\]

at most \(1+\lceil\log_2(2m^2)\rceil\) determinant
bands can be active.  Therefore

\[
 \boxed{
 \sum_D\mathcal Q_D(A)
 \le\bigl(1+\lceil\log_2(2m^2)\rceil\bigr)\mathcal P(A).} \tag{2.6}
\]

The flat estimate

\[
 \mathcal P(A)\le m^{o(1)}(k^3+m^2)                 \tag{2.7}
\]

is thus a precise sufficient endpoint-height inequality.  It is sharp on
the structured stresses below.  It remains unproved in the critical
range; (2.6) is a localization, not a solution.

## 3. What radial uniqueness proves inside one fibre

Fix \(w=(w_1,w_2)\) and \(r\ne0\).  For \(q\in\mathscr D\) with
\(\det(w,q)=r\), put \(s=w\mathbin\cdot q\).  The identity

\[
 \|w\|^2\|q\|^2=s^2+r^2                             \tag{3.1}
\]

shows that the absolute values \(|s|\) are distinct inside this fibre.
Indeed equal values would give equal edge lengths; distance-Sidonicity
would force \(q'=q\) or \(q'=-q\), and the latter has determinant
\(-r\).  Since \(|s|\le m(|w_1|+|w_2|)\),

\[
 \boxed{B_w(r)\le m(|w_1|+|w_2|)+1.}                \tag{3.2}
\]

Every positive content satisfies
\(g\max(|w_1|,|w_2|)\le m\), so

\[
 e_w\le {m\over\max(|w_1|,|w_2|)}.                 \tag{3.3}
\]

Consequently each individual closed fibre contributes at most

\[
 B_w(r)e_w\le2m^2+m.                                \tag{3.4}
\]

This is the sharp pointwise height restriction.  It still cannot prove
(1.2): the layered model below places a polynomial number of large fibres
next to one another.  A successful theorem must globally pack the
different \((w,r)\), rather than applying (3.2)--(3.4) independently.

## 4. The genuine \(m^2\) equality model

For an odd prime \(p\), put \(y_x=[x^2]_p\) and

\[
 A_p=\{(x+py_x,y_x):0\le x<p\}.                     \tag{4.1}
\]

This is genuinely distance-Sidon.  If an edge is oriented by its labels,
write \(h=x-x'\in\{1,\ldots,p-1\}\) and
\(z=y_x-y_{x'}\).  Its squared length is

\[
 Q_p(h,z)=(h+pz)^2+z^2.                              \tag{4.2}
\]

The positive-\(z\), negative-\(z\), and opposite-sign intervals in
(4.2) are disjoint, so \(Q_p(h,z)\) recovers \((h,z)\).  Modulo \(p\),
\(z\equiv h(x+x')\) then recovers the endpoints.  Also (4.1) is the
determinant-one shear \((x,y)\mapsto(x+py,y)\), so every primitive
direction, content, residue, and dyadic determinant band in (1.1) is
preserved exactly.

The universal bound (1.3) gives \(\sum_D\mathcal Q_D=O(p^4)\).  The
finite-field parabola has \(\Omega(p^4)\) six-endpoint equal-centroid
matchings, with only \(O(p^2\log p)\) collinear ones.  The exact
closed-fibre identity gives the reverse inequality.  Hence (1.4).

Exact values are:

\[
\begin{array}{c|r|r|r}
p&m&\mathcal P&\sum_D\mathcal Q_D\\ \hline
7&33&440&488\\
11&107&2876&3500\\
17&285&17316&19956\\
23&429&69208&80444\\
31&888&223588&268650\\
43&1790&847864&988328
\end{array}                                          \tag{4.3}
\]

There is a small correction to the previous closed-fibre audit.  At
\(p=43\), the full sum is \(988328\), not \(988320\): the old cutoff list
stopped at the largest clean determinant band and omitted a final
\(D=2048\) band of \(Q\)-mass eight.  No earlier conclusion changes.

## 5. A critical layered countermodel without radial uniqueness

Let \(d\) be a nonsquare modulo \(p\), write
\(\mathbb F_{p^2}=\mathbb F_p[\omega]/(\omega^2-d)\), and put

\[
 t=a+b\omega,qquad
 t^2=c+e\omega,qquad
 c=a^2+db^2,\quad e=2ab.                            \tag{5.1}
\]

Take the representatives \(a,b,c,e\in\{0,\ldots,p-1\}\), set
\(R=2p\), and define

\[
 A_p^{\rm lay}
 =\{(a+Rc+R^2e,b):a,b\in\mathbb F_p\}.              \tag{5.2}
\]

The field parabola \(\{(t,t^2):t\in\mathbb F_{p^2}\}\) is vector-Sidon:
from a nonzero first difference \(h=t-u\), the second difference
\(h(t+u)\) recovers \(t+u\), hence both endpoints.  Because
\(R>2(p-1)\), equality of two integer differences in the first coordinate
of (5.2) recovers the three digit differences separately.  Thus (5.2) is
an actual integer vector-Sidon point set.  It is not distance-Sidon.  For
\(p\ge5\), compare the two edges in the \(a=0\) slice whose \(b\)-labels
are \(1\to2\) and \(p-1\to p-2\).  Since
\(c_{p-j}=c_j\), their displacement vectors have the form
\((u,1)\) and \((u,-1)\).  They are different endpoint edges with equal
Euclidean norm.

It has \(p\) horizontal rows of \(p\) points.  For \(w=(1,0)\),

\[
 e_w=p\binom p2={p^2(p-1)\over2},qquad
 B_w(r)=(p-|r|)p^2\quad(0<|r|<p).                  \tag{5.3}
\]

For a fixed \(r\), the values \(\alpha_{w,D}(r)\) partition \(e_w\).
Writing \(B=B_w(r)\), subadditivity of
\(x\mapsto\min\{\binom B2,Bx\}\) gives

\[
 \sum_D\min\left\{\binom B2,\alpha_{w,D}(r)B\right\}
 \ge\min\left\{\binom B2,e_wB\right\}
 =\binom B2,                                         \tag{5.4}
\]

because \(B\le2e_w\).  Summing both signs yields the exact lower bound

\[
\begin{aligned}
 \mathcal Q^{\rm hor}(A_p^{\rm lay})
 &\ge2\sum_{h=1}^{p-1}\binom{hp^2}{2}\\
 &={1\over3}p^7-{1\over2}p^6+O(p^5).               \tag{5.5}
\end{aligned}
\]

Since (5.2) has height \(O(p^3)\), this is the promised critical
countermodel to every proof using only endpoint realization and vector
injectivity.  It is not a counterexample to (1.2), because it has equal
Euclidean distances.

There is an explicit genuine Euclidean version.  Put \(L=3p\) and send

\[
 (x,y)\longmapsto(Lx+y,y).                           \tag{5.6}
\]

For displacement coordinates \((x,y)\), where \(|y|<p\), the intervals of

\[
 (Lx+y)^2+y^2                                       \tag{5.7}
\]

belonging to successive values of \(|x|\) are disjoint.  Indeed the
minimum at \(|x|=t\) exceeds the maximum at \(|x|=t-1\), since

\[
 (Lt-p+1)^2>
 (L(t-1)+p-1)^2+(p-1)^2\qquad(t\ge1).               \tag{5.8}
\]

If \(|x|\) is fixed, equality in (5.7) factors as

\[
 2(y-y')[Lx+y+y']=0
\]

when \(x'=x\), and as

\[
 2(y+y')[Lx+y-y']=0
\]

when \(x'=-x\).  Since \(L=3p>2(p-1)\), the bracketed factors cannot
vanish when \(x\ne0\).  The case \(x=0\) is immediate, so the vectors are
equal or opposite.  Vector-Sidonicity therefore makes (5.6)
distance-Sidon.  Its height is
\(O(p^4)\), while (5.3)--(5.5) remain valid (horizontal contents are only
rescaled and repartitioned among dyadic bands).  This proves the genuine
polynomial-height assertion in Section 1 and pinpoints the lost power.

## 6. Other genuine stresses

The stored critical closure prefixes remain compatible with (1.2):

\[
\begin{array}{c|r|r|r|r|c}
\text{family}&k&m&\mathcal P&\sum_D\mathcal Q_D&
 \mathcal Q/(k^3+m^2)\\ \hline
\text{closure-20}&20&75&17760&18282&1.342\\
\text{closure-40}&40&223&205062&225150&1.980\\
\text{closure-60}&60&447&787498&896292&2.156\\
\text{integer parabola-40}&40&1521&193968&630172&0.265\\
\text{multi-arc-24}&24&1207274&12804&15082&<10^{-7}
\end{array}                                          \tag{6.1}
\]

The closure constants grow slowly but show no polynomial excess; their
profile is compatible with a logarithmic loss over \(k^3+m^2\).  The
integer parabola and multi-arc constructions are paid overwhelmingly by
height.  None kills (1.2).

## 7. Exact survivor

The only unresolved regime is

\[
 m<k^{2-o(1)},                                       \tag{7.1}
\]

where neither (1.3) nor the ambient term alone closes the estimate.  The
layered construction proves that the required statement cannot follow
from the endpoint cocycle plus additive/vector Sidonicity.  The precise
missing theorem is a global version of (3.2): Euclidean radial uniqueness
must prevent too many direction-residue fibres from simultaneously
approaching their height caps.  Equivalently, (2.7) is a clean sufficient
form of that global packing statement.

## 8. Verification

Run

```text
python3 phase2/loop/erdos1208/verify_closed_fibre_q_height_layered_barrier.py
```

The verifier checks (1.3), the exact \(\mathcal P\) and \(\mathcal Q\)
profiles, the corrected \(p=43\) band, the finite-field Euclidean lifts,
the \(\mathbb F_{p^2}\) layered vector-Sidon construction, the explicit
dominance Euclideanization, the exact horizontal lower bound, the
pointwise height cap, and all rows of (6.1).
