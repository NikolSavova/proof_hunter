# Equal-centroid nine-anchor symmetry: exact identities and a charge barrier

## 1. Verdict

Let `T={t_0,t_1,t_2}` and `U={u_0,u_1,u_2}` be disjoint triples in a
distance-Sidon set, with

\[
 \sum_i t_i=\sum_j u_j.                                      \tag{1.1}
\]

The full `3 by 3` symmetry gives useful exact identities, but it does not
produce a new symmetric quadratic metric coordinate.  Every
translation- and rotation-invariant quadratic statistic which is invariant
under independent permutations of `T` and `U` is a linear combination of
the two inertias `I(T),I(U)`.  In particular the nine cross distances and
the nine opposite-edge clean incidences collapse, after averaging, to those
same two scalars.

There is an endpoint-sensitive way not to average: charge every one of the
nine clean incidences by the two opposite side lengths.  This gives a very
small sufficient gate and is almost injective on all stored stresses.
Nevertheless it has genuine polynomial-height distance-Sidon examples with
a polynomially heavy charge class.  Thus the natural alternatives are
sharp:

* averaging the nine anchors loses the endpoints and returns to the old
  relative-inertia gate;
* retaining the anchors preserves endpoints, but no uniform
  divisor-multiplicity theorem is possible for the resulting scalar.

This is a no-go for the **quadratic symmetrization shortcut**, not a
disproof of the ambient equal-centroid bound.

## 2. The nine clean incidences

Put `s=sum T=sum U`.  For every `(i,j)`, set

\[
 q_{ij}=t_i-u_j.                                             \tag{2.1}
\]

The opposite pair sums obey

\[
 \sum_{r\ne i}t_r+q_{ij}=\sum_{r\ne j}u_r.                  \tag{2.2}
\]

Thus `(T minus {t_i},U minus {u_j})` is a clean pair-sum
incidence at the realized cross edge `q_ij`.  All six endpoints are
distinct.  An ordered equal-centroid pair supplies nine such incidences;
an unordered pair supplies eighteen after reversing `T,U`.

Write

\[
 \ell_i=|t_{i+1}-t_{i+2}|^2,\qquad
 r_j=|u_{j+1}-u_{j+2}|^2                                  \tag{2.3}
\]

with indices modulo three, and

\[
 c_{ij}=|t_i-u_j|^2.                                        \tag{2.4}
\]

Then

\[
 I(T)=\sum_i\ell_i,\qquad I(U)=\sum_jr_j.                   \tag{2.5}
\]

## 3. Cross-block and row-opposite identities

Translate the common centroid to zero.  Since
`sum_i t_i=sum_j u_j=0`, the variance identity gives

\[
 \boxed{\sum_{i,j}c_{ij}=I(T)+I(U).}                         \tag{3.1}
\]

There is a stronger endpoint-sensitive form.  For every row and column,

\[
\boxed{
 \ell_i+\sum_jc_{ij}={2I(T)+I(U)\over3},\qquad
 r_j+\sum_ic_{ij}={I(T)+2I(U)\over3}.}                      \tag{3.2}
\]

Indeed, if `S_T=sum_i |t_i|^2`, then `I(T)=3S_T` and

\[
 \ell_i=2S_T-3|t_i|^2,qquad
 \sum_jc_{ij}=3|t_i|^2+S_U.                                \tag{3.3}
\]

Adding proves the first identity; the second is symmetric.  Thus each
equal-centroid pair gives three four-distance decompositions of each of two
`O(m^2)` integers.  But the two integers in (3.2) are an invertible linear
change of coordinates from `(I(T),I(U))`; they are not a new invariant.

## 4. Classification of symmetric quadratic metric statistics

### Proposition 4.1

On the locus (1.1), every real quadratic scalar `Q(T,U)` which

1. is invariant under common translations and rotations, and
2. is invariant under `S_3 x S_3`, acting separately on `T` and `U`,

has the form

\[
 \boxed{Q(T,U)=aI(T)+bI(U)}                                  \tag{4.1}
\]

up to an additive constant.

### Proof

After translating the common centroid to zero, an invariant quadratic is a
linear combination of orbit sums of dot products.  The `T-T` orbit sums
are `sum_i|t_i|^2` and `sum_(i ne i')t_i dot t_i'`; their sum is
`|sum_i t_i|^2=0`, so this contributes only a multiple of
`sum_i|t_i|^2=I(T)/3`.  The `U-U` terms similarly give `I(U)/3`.
The only `T-U` orbit sum is

\[
 \sum_{i,j}t_i\mathbin\cdot u_j
 =\left(\sum_it_i\right)\mathbin\cdot
  \left(\sum_ju_j\right)=0.                                \tag{4.2}
\]

This proves (4.1).  In particular, summing any quadratic charge uniformly
over the nine anchors cannot retain which endpoint occupied which row or
column.  QED.

## 5. The unaveraged internal-edge charge

Let `mathcal R(A)` be the set of ordered records `(T,U,i,j)` above.  If
`C(A)` is the number of unordered disjoint equal-centroid triangle pairs,
then

\[
 |\mathcal R(A)|=18C(A).                                    \tag{5.1}
\]

For a fixed integer `C_0>1`, define

\[
 \phi(T,U,i,j)=\ell_i+C_0r_j.                               \tag{5.2}
\]

This is genuinely endpoint-decorated: the two edge sums differ by the
realized cross edge `q_ij`.  It has at most
`2(C_0+1)m^2+1` integer values.  If its energy

\[
 E_\phi=\sum_z|\phi^{-1}(z)|^2                              \tag{5.3}
\]

satisfied

\[
 E_\phi\le m^{o(1)}|\mathcal R(A)|,                         \tag{5.4}
\]

then Cauchy--Schwarz and (5.1) would give
`C(A)<=m^(2+o(1))`, the ambient centroid gate.  This is the
full-symmetry analogue of the metric scalar charge, without an arbitrary
auxiliary edge.

For `C_0=18`, its normalized energies on closure `40,80,120`, Costas `22`,
and the 127-point parabola image are respectively

\[
 1.0663\ldots,\ 1.0911\ldots,\ 1.1065\ldots,\
 1.0503\ldots,\ 1.0261\ldots.                              \tag{5.5}
\]

The maximum loads are at most five.  The next theorem shows that this
finite near-injectivity is not asymptotic.

## 6. Genuine planted heavy classes

### Theorem 6.1

There are arbitrarily large integral distance-Sidon sets `A` of polynomial
height for which the charge (5.2), with `C_0=18`, has a fibre of size
`|A|^eta` for an absolute `eta>0`.  Every record in the fibre is one of the
nine clean incidences of a disjoint equal-centroid triangle pair.

### Proof

Let

\[
 D_X=\{n\le X:n=x^2+y^2\text{ for some }x,y\in\mathbb Z\}.
\]

Writing `R=|D_X|`, Landau--Ramanujan gives
`R=X(log X)^(-1/2+o(1))`.  Pigeonholing all pairs in `D_X^2` by
`a+18b` produces a value `N_X` with

\[
 |\{(a,b)\in D_X^2:a+18b=N_X\}|
 \ge {R^2\over19X+1}=X^{1-o(1)}.                            \tag{6.1}
\]

The pairs form a matching in each coordinate.  After a constant-factor
pruning, all labels `a,b` are mutually distinct.  Choose vectors
`w_a,w_b` of norms `a,b`.  A fixed value of any one of
`w_a+w_b,w_a-w_b` has only `X^{o(1)}` preimages: substituting
`w_a=r-w_b` into `|w_a|^2+18|w_b|^2=N_X` gives

\[
 |19w_b-r|^2=19N_X-18|r|^2,                                 \tag{6.2}
\]

and the two-squares divisor bound applies.  A further subpolynomial
pruning therefore makes all four signed sums distinct.  Applying the same
conic argument to the finite list of three-point offset patterns removes
every unintended center-independent triple-sum identity.  Only a fixed
power loss is needed, so `X^eta` candidates remain for some absolute
`eta>0`.

Keep `r=X^eta` pairs, for a sufficiently small fixed `eta>0`.  Choose an
even vector `q`, a common scale `S`, and free centers `P_i`, and put

\[
\begin{aligned}
 a_0&=0,& b_0&=-q,\\
 c_i&=P_i+Sw_{a_i},&d_i&=P_i-Sw_{a_i},\\
 e_i&=P_i+q/2+Sw_{b_i},&f_i&=P_i+q/2-Sw_{b_i}.
\end{aligned}                                               \tag{6.3}
\]

Then

\[
 a_0+c_i+d_i=b_0+e_i+f_i,                                  \tag{6.4}
\]

so `T_i={a_0,c_i,d_i}` and `U_i={b_0,e_i,f_i}` are disjoint
equal-centroid triples.  The incidence which omits `a_0,b_0` has charge

\[
 |c_i-d_i|^2+18|e_i-f_i|^2
 =4S^2(a_i+18b_i)=4S^2N_X,                                 \tag{6.5}
\]

independent of `i`.

It remains only to make the ambient set genuine.  Equalities between two
unintended squared distances and unintended equal triple sums are
nonzero polynomials of degree at most two in `q,P_1,...,P_r`.  The only
polynomials independent of the centers are controlled edge distances and
fixed local offset patterns; label disjointness and the two pruning steps
above make these nondegenerate, after excluding finitely many quadratic
conditions on `q`.  All remaining forbidden polynomials are
nonzero.  The elementary grid nonvanishing lemma chooses integer values
outside their union in a box whose side is larger than the total degree of
their product.  There are only `r^O(1)` factors, so all coordinates have
height polynomial in `X` and `r`.

This specialization is distance-Sidon and has no equal-triple-sum pairs
besides (6.4).  Equation (6.5) gives a charge load `r`.  Since the height is
`X^O(1)`, this load is a fixed positive power of both `|A|=4r+2` and the
height.  QED.

The theorem rules out pointwise or near-diagonal divisor bounds for the
unaveraged charge.  It does not rule out a size-biased inequality with an
additional endpoint-reuse budget, nor does it rule out a direct theorem for
the inertia fibres.

## 7. Consequence for the large-area programme

Full triangle symmetry supplies no missing determinant coordinate at
quadratic scale.  The row and column identities (3.2) are exact and
endpoint-sensitive as decompositions, but their values are only the two
inertias.  Keeping the decompositions separately leads to (5.2), whose
heavy planted fibres are genuine.  Therefore a continuation of the
large-area scalar programme must use a non-quadratic endpoint-reuse
inequality (or a size-biased compensation theorem); uniform nine-anchor
averaging alone cannot close the core.

Run

```text
python3 phase2/loop/erdos1208/verify_equal_centroid_nine_anchor_symmetry.py
```

for exact checks of (2.2), (3.1)--(3.3), the record count, the stored
charge profiles, and a 14-point planted distance-Sidon certificate.
