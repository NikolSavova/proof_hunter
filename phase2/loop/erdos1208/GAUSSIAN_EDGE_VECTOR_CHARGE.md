# A Gaussian charge on canonically oriented edge vectors

## 1. Exact reduction

Let `A subset Z^2` be distance-Sidon, let `|A|=k`, and suppose both
coordinate widths of `A` are at most `m`.  Put

\[
 \Sigma=A\mathbin\oplus A,
 \qquad N=|\Sigma|=\binom k2,
\]

and let `H_q subset Sigma` be the clean start set associated with a
realized directed difference `q`, as in
`DILATED_INTERNAL_PAIR_SUM_CHARGE.md`.  A pair sum `s in Sigma` has a
unique unordered endpoint pair.  Order those endpoints lexicographically
and let

\[
 u(s)\in\mathbb Z^2
\]

be the resulting oriented edge vector.  These oriented vectors are
distinct, and distance-Sidonicity makes their squared norms pairwise
distinct: if `s!=t`, then `|u(s)|^2!=|u(t)|^2`.

Write

\[
 \lambda=3(I+J),\qquad J(x,y)=(-y,x),
\]

and define

\[
 \boxed{
 \Gamma_q(s,t)=u(s)+\lambda u(t),
 \qquad (s,t)\in H_q\times\Sigma.}             \tag{1.1}
\]

Put `U=u(Sigma)` and `U_q=u(H_q)`.  If `h=|H_q|`, the exact collision
energy is

\[
 \boxed{
 \mathcal G_q
 =\sum_{w\in\mathbb Z^2}
   r_{U-U}(w)r_{U_q-U_q}(-\lambda w).}          \tag{1.2}
\]

The zero term is exactly `Nh`.  Since every coordinate of `u(s)` has
absolute value at most `m` and every coordinate of `lambda u(t)` has
absolute value at most `6m`, the image of (1.1) has at most

\[
 (14m+1)^2                                                   \tag{1.3}
\]

keys.  Consequently the estimate

\[
 \boxed{
 \mathcal G_q\le m^{o(1)}N\bigl(|H_q|+k\bigr)}              \tag{1.4}
\]

for every `q` would prove

\[
 |A|\le m^{2/3+o(1)}.                                      \tag{1.5}
\]

This is a new sufficient gate, not a proof of (1.4).

### Proof of the implication

Two records collide precisely when

\[
 u(s)-u(s')=-\lambda\bigl(u(t)-u(t')\bigr),                 \tag{1.6}
\]

which gives (1.2).  If `h>k`, (1.4), (1.3), and Cauchy--Schwarz give

\[
 (hN)^2
 \le(14m+1)^2m^{o(1)}N(h+k)
 \le m^{2+o(1)}Nh.
\]

Thus `hN<=m^(2+o(1))`.  Fibres with `h<=k` contribute only `O(k^3)`
clean starts in total.  Summing the remaining estimate over the
`k(k-1)` realized directed differences and using

\[
 C_6(A)=4\sum_q|H_q|
\]

gives the ambient equal-centroid bound and the standard cube-root
conclusion.

## 2. Relation to the metric scalar charge

The squared norm of (1.1) is the compound metric charge

\[
 \chi_q(s,t)=|u(s)+\lambda u(t)|^2                         \tag{2.1}
\]

and expands as

\[
 \chi_q(s,t)
 =|u(s)|^2+18|u(t)|^2+2u(s)\cdot\lambda u(t).               \tag{2.2}
\]

Thus it combines the surviving distance-label charge with the directional
cross term.  The fixed bilinear charge killed in
`BILINEAR_EDGE_CHARGE_BARRIER.md` retained only the last term of (2.2);
on its Golomb-ruler arm the middle term is different for every edge and
removes that obstruction.

The vector charge is stronger than (2.1).  If `nu(z)` is the load of `z`
under (1.1), then the energy of (2.1) satisfies

\[
 \begin{aligned}
 \mathcal G_q\le \mathcal Q_q
 &=\sum_n\left(\sum_{|z|^2=n}\nu(z)\right)^2\\
 &\le \max_{n\ll m^2}r_2(n)\sum_z\nu(z)^2
 \le m^{o(1)}\mathcal G_q,                                  \tag{2.3}
 \end{aligned}
\]

by the divisor bound for representations as two squares.  Hence (1.4)
would also prove the scalar compound gate.  Conversely, (2.3) loses only a
subpolynomial factor, so the two formulations have the same exponent-level
target.

This charge is not the earlier pair-sum charge `s+lambda t`: it uses the
canonically oriented *edge displacement* belonging to each pair sum.  The
two exact energies are therefore different.

## 3. What a high load means

A load of size `r` at one vector `z` is an affine matching

\[
 u_i=z-\lambda v_i,
 \qquad u_i\in U_q,\quad v_i\in U.                         \tag{3.1}
\]

between two subsets of the complete directed difference set of `A`.
Radial uniqueness says all `|u_i|` and all `|v_i|` are distinct, but that
alone does not control (3.1).  The missing input is that `U` consists of
all canonically oriented edges of one endpoint set and that `U_q` comes
from clean equal-centroid configurations.

There is a sharp abstract warning.  Let `R_M` contain one first-quadrant
lattice representative of every occupied squared radius at most `M^2`.
Then `|R_M|=M^{2-o(1)}`, while `R_M+lambda R_M` lies in a box with only
`O(M^2)` lattice points.  Therefore

\[
 \sum_z r_{R_M+\lambda R_M}(z)^2
 \ge {|R_M|^4\over O(M^2)}
 =|R_M|^{3-o(1)}.                                          \tag{3.2}
\]

So (1.4) is false for arbitrary radially unique vector sets by nearly a
full power.  This is consistent with the fixed-row fibre barriers already
in the project.  A proof cannot stop at one vector per radius, ordinary
small doubling, or an affine matching; it must retain endpoint
realizability and the clean `H_q` decoration.

## 4. Exact profiles

The verifier chooses the largest clean fibre in each stored family and
reports

\[
 (k,m,q,h,N,hN,|\operatorname{im}\Gamma_q|,
   \mathcal G_q,\max\Gamma_q^{-1}).
\]

\[
\begin{array}{c|r|r|r|r}
\text{family}&hN&|\operatorname{im}\Gamma_q|&\mathcal G_q&\max\text{ load}\\ \hline
\text{closure }30&6090&6045&6180&2\\
\text{closure }40&17940&17482&18876&3\\
\text{closure }80&199080&194953&207504&4\\
\text{closure }120&906780&884353&952740&4\\
\text{source }45&21780&21557&22238&3\\
\text{perpendicular ruler }40&10920&10920&10920&1\\
\text{Costas }22&7854&7854&7854&1\\
\text{parabola image }43&154413&152024&159191&2\\
\text{integer parabola }50&91875&91264&93097&2\\
\text{integer parabola }120&2249100&2231784&2283940&3
\end{array}
\]

The largest normalized energy in the table is

\[
 {18876\over17940}=1.05217\ldots .                         \tag{4.1}
\]

The exact injectivity on the perpendicular-ruler and Costas stresses is
notable because those families killed several earlier global energy
proposals.  These finite profiles are evidence only; (3.2) records the
precise structural hypothesis that still has to be used.
