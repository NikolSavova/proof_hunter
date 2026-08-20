# Metric scalar charge: cross-edge factorization and the low-area branch

## 1. Outcome

This note factors every four-distinct-edge scalar collision into
endpoint-realized complete differences.  The factorization proves a uniform
radius-difference/signed-area multiplicity bound and the quantitative branch

\[
 \boxed{
 T_q^{(4)}\bigl(|2\det(v,v')|\le L\bigr)
 \le (2L+1)m^{o(1)}h^2.}                                  \tag{1.1}
\]

Here `h=|H_q|`, `v,v'` are the two arbitrary-edge displacement vectors,
and `T_q^(4)` is the squareclass-transverse four-edge core from
`METRIC_SCALAR_SQUARECLASS_TRANSVERSE_GATE.md`.  Since `h<=N`, taking

\[
 L=\left\lfloor{N\over h}\right\rfloor                     \tag{1.2}
\]

makes (1.1) `m^{o(1)}hN`.  Thus all parallel target pairs and, more
generally, the entire low-target-area branch are harmless.  Any polynomial
failure of the scalar gate must have

\[
 \boxed{|2\det(v,v')|>N/h}                                 \tag{1.3}
\]

up to the inessential rounding in (1.2), in addition to the previous
four-edge and squareclass-transverse conditions.

This is a proved branch, not a bound for the remaining large-area core.

## 2. Four complete-difference factors for two edges

Let the two canonically oriented source edges be

\[
 u=c-d,qquad u'=c'-d'.                                    \tag{2.1}
\]

Define the four cross-edge differences

\[
 \alpha=c-c',\qquad \beta=d-d',\qquad
 \rho=c-d',\qquad \sigma=d-c'.                            \tag{2.2}
\]

All four belong to the complete directed difference set `A-A` and retain
their ordered endpoint realizations.  Direct expansion gives the exact
parallelogram and factor identities

\[
\begin{aligned}
 \alpha+\beta&=\rho+\sigma,\\
 u-u'&=\alpha-\beta,\\
 u+u'&=\rho-\sigma,\\
 |u|^2-|u'|^2
   &=(\alpha-\beta)\mathbin\cdot(\rho-\sigma),\\
 \det(\alpha-\beta,\rho-\sigma)
   &=2\det(u,u').
\end{aligned}                                               \tag{2.3}
\]

The analogous target factors are

\[
 \gamma=x-x',\quad\zeta=y-y',\quad
 \tau=x-y',\quad\omega=y-x'                               \tag{2.4}
\]

for `v=x-y`, `v'=x'-y'`.  They satisfy

\[
\begin{aligned}
 \gamma+\zeta&=\tau+\omega,\\
 v-v'&=\gamma-\zeta,\qquad v+v'=\tau-\omega,\\
 |v|^2-|v'|^2
   &=(\gamma-\zeta)\mathbin\cdot(\tau-\omega),\\
 \det(\gamma-\zeta,\tau-\omega)
   &=2\det(v,v').
\end{aligned}                                               \tag{2.5}
\]

Together with the clean target endpoints `e,f,e',f'`, the full scalar
collision system is

\[
\begin{aligned}
 (c-c')+(d-d')&=(e-e')+(f-f'),\\
 (\alpha-\beta)\mathbin\cdot(\rho-\sigma)
 +18(\gamma-\zeta)\mathbin\cdot(\tau-\omega)&=0.
\end{aligned}                                               \tag{2.6}
\]

If the source squared-distance squareclasses differ, then `u,u'` cannot be
parallel, so the last determinant in (2.3) is nonzero.  The same statement
holds on the target side.  Indeed, parallel integral vectors are integer
multiples of one primitive vector and their squared norms have the same
squarefree kernel.

## 3. Fixed radius difference and signed area

Identify an integral vector with a Gaussian integer.  For two canonical
edge vectors `w,w'`, put

\[
 P=w-w',\qquad R=w+w',\qquad
 r=|w|^2-|w'|^2,qquad d=2\det(w,w').                       \tag{3.1}
\]

Then

\[
 \boxed{P\overline R=r-id.}                                \tag{3.2}
\]

The sign of the imaginary part follows from
`Im(P overline R)=-det(P,R)` and
`det(P,R)=2det(w,w')`.

**Lemma 3.1 (radius-area multiplicity).**  Fix integers `r,d`, not both
zero.  Among the canonical edge vectors of a distance-Sidon set in an
`m` by `m` box, the number of ordered pairs `(w,w')` satisfying (3.1) is
`m^{o(1)}`, uniformly in `r,d`.

**Proof.**  Equation (3.2) is a factorization of the fixed nonzero Gaussian
integer `r-id`.  The Gaussian divisor bound gives only

\[
 |r-id|^{o(1)}=m^{o(1)}                                    \tag{3.3}
\]

ordered factor pairs `(P,overline R)`, since all coordinates in (3.1) are
`O(m)` and hence `|r-id|=O(m^2)`.  A factor pair determines

\[
 w={R+P\over2},\qquad w'={R-P\over2}.                      \tag{3.4}
\]

Parity and endpoint-realizability can only discard possibilities.
Distance-Sidonicity makes the canonical edge-vector map injective, so each
surviving vector pair determines at most one ordered edge pair.  \(\square\)

For two distinct edge labels, `r` is automatically nonzero by global
distance uniqueness.  In particular Lemma 3.1 includes `d=0`, the parallel
case; no separate direction count is required.

## 4. Proof of the low-area branch

Fix an ordered pair of distinct source edges `(s,s')` in `H_q`.  A scalar
charge collision requires

\[
 |v|^2-|v'|^2
 =-{\delta(s)-\delta(s')\over18}.                           \tag{4.1}
\]

If the right side is not integral there is no completion.  Otherwise it is
a fixed nonzero integer because the source edge labels are distinct.  For
each fixed signed doubled area

\[
 d=2\det(v,v'),qquad |d|\le L,                             \tag{4.2}
\]

Lemma 3.1 supplies at most `m^{o(1)}` ordered target-edge pairs.  There are
`2L+1` possible integers `d` and at most `h(h-1)` ordered source pairs.
This proves (1.1).

Because `1<=N/h` and `h<=N`, substituting (1.2) gives

\[
 (2L+1)m^{o(1)}h^2\le3m^{o(1)}hN.                          \tag{4.3}
\]

Thus this branch fits inside the desired scalar energy budget.  Notice the
asymmetry: the small set is the source fibre, so one can choose its `h^2`
ordered pairs and complete into the large target edge set.  Applying the
same argument with source and target interchanged would cost `N^2` and does
not close the opposite low-source-area branch.

## 5. Exact surviving core and limitation

Combining this note with the squareclass-transverse theorem and the
three-edge cleanup leaves only collision rows satisfying all of the
following:

1. the four charge edges are distinct;
2. the source pair or target pair changes squared-distance squareclass;
3. the target edges are nonparallel and have
   `|2det(v,v')|>N/h`;
4. all eight target factors in (2.2) and (2.4) are complete differences
   with their endpoint realizations;
5. both equations in (2.6) hold, together with the two clean-start
   decorations.

The Gaussian factorization does not by itself bound the large-area core.
It controls the multiplicity after both the real part `r` and imaginary
part `d` are fixed, whereas the scalar charge fixes only `r`.  Summing over
the still-available `Theta(m^2)` signed areas would lose far more than the
cube-root budget.  The next step must therefore charge large target area to
endpoint incidence or show that many occupied signed areas force an equal
two-dimensional endpoint norm.  A black-box Gaussian divisor estimate with
the area coordinate discarded cannot do this.

Run `verify_metric_scalar_cross_edge_determinant_branch.py` for exact checks
of every factor identity and sign, fixed-`(r,d)` multiplicities, the finite
low-area completion inequality, and the stored closure, Costas, parabola,
ruler, and resonant two-arm stresses.
