# A failed global orthogonal energy-product gate for Erdos 1208

> **Status update (2026-08-18).**  The target below is false.  Dense
> perpendicular Golomb rulers give genuine integral distance-Sidon sets with
> `E_+(D),E_perp(D)=Omega(N^3)`, and hence product `Omega(N^6)`.
> `ORTHOGONAL_ENERGY_PRODUCT_RULER_BARRIER.md` contains the proof.  The exact
> complete-difference positivity in Section 3 is therefore insufficient; the
> support-sensitive gate `E_perp<=N^(1+o(1))|D+D|` remains live.

## 1. The new sufficient inequality

Let `A` be distance-Sidon, put

\[
 D=A-A,\qquad N=|D|=|A|(|A|-1)+1,
\]

and let `J` be the quarter-turn.  Write

\[
 R_D(q)=|\{(x,y)\in D^2:x-y=q\}|.
\]

Define the ordinary and orthogonal common energies

\[
 \mathcal E_+(D)=\sum_qR_D(q)^2,
 \qquad
 \mathcal E_\perp(D)=\sum_qR_D(q)R_D(Jq).        \tag{1.1}
\]

The formerly proposed target was

\[
 \boxed{\mathcal E_+(D)\mathcal E_\perp(D)
        \le N^{5+o(1)}.}                         \tag{1.2}
\]

It would resolve the cube-root exponent.  Indeed, with `S=|D+D|`, Cauchy gives

\[
 \mathcal E_+(D)\ge \frac{N^4}{S}.              \tag{1.3}
\]

Combining (1.2) and (1.3),

\[
 \mathcal E_\perp(D)
 \le \frac{N^{5+o(1)}}{\mathcal E_+(D)}
 \le N^{1+o(1)}S.                               \tag{1.4}
\]

This is exactly the already-proved orthogonal energy--support gate.  Hence

\[
 |D+D|\,|D+JD|\ge N^{3-o(1)},                   \tag{1.5}
\]

which gives `|A|<=m^(2/3+o(1))` in the `m` by `m` grid and settles Erdos
problem 1208 at the conjectural cube-root scale.

Unlike the switching charges, (1.2) is completely global.  It says that
ordinary additive concentration of the complete difference set and the
same concentration after a quarter-turn cannot coexist at full strength.

## 2. Exact evidence and the correct constant scale

The normalized quantity

\[
 U(A)=\frac{\mathcal E_+(D)\mathcal E_\perp(D)}{N^5}       \tag{2.1}
\]

has the following exact values.

\[
\begin{array}{c|r|r|r|c}
\text{family}&N&\mathcal E_+&\mathcal E_\perp&U(A)\\ \hline
\text{closure }15&211&491179&240353&0.282278\ldots\\
\text{closure }20&381&2590997&1735609&0.560136\ldots\\
\text{closure }25&601&8460337&6301921&0.679967\ldots\\
\text{closure }30&871&20508519&16135769&0.660135\ldots\\
\text{parabola }31&931&191031539&866761&0.236731\ldots\\
\text{quadratic }18&307&761635&101801&0.028431\ldots
\end{array}                                                   \tag{2.2}
\]

The sharp constant is not one.  The five-point lattice set

\[
 \{(0,0),(0,2),(2,4),(3,2),(3,3)\}              \tag{2.3}
\]

is distance-Sidon and has

\[
 (N,\mathcal E_+,\mathcal E_\perp)=(21,2941,1817),
 \qquad U=1.308438\ldots .                       \tag{2.4}
\]

Thus only the exponent-level `N^(o(1))` loss in (1.2) should be targeted.

## 3. Why the complete-difference input is exact

For a distance-Sidon set,

\[
 D\cap JD=\{0\}.                                 \tag{3.1}
\]

Indeed, a nonzero `d in D intersect JD` would give two segments of equal
length.  Distance-Sidonicity identifies their unordered endpoint pair, but a
nonzero vector cannot be its own quarter-turn or the quarter-turn of its
negative.

Consequently the sum

\[
 A+JA                                                   \tag{3.2}
\]

is direct: `a+Jb=c+Jd` implies `a-c=J(d-b)`, hence both differences vanish.
In particular,

\[
 |A+JA|=|A|^2.                                    \tag{3.3}
\]

There is also an exact positive-definite autocorrelation identity.  If
`k=|A|`, then

\[
 1_A\circ1_A=1_D+(k-1)\delta_0.                  \tag{3.4}
\]

After embedding the finite configuration into a sufficiently large finite
torus and taking the unnormalized Fourier transform,

\[
 \widehat{1_D}(\xi)=|\widehat{1_A}(\xi)|^2-(k-1). \tag{3.5}
\]

Thus the spectrum of `1_D` is a fixed negative shift of a nonnegative
spectrum.  Parseval rewrites (1.1) as

\[
 \mathcal E_+(D)=\frac1{|G|}\sum_\xi
       |\widehat{1_D}(\xi)|^4,                   \tag{3.6}
\]

\[
 \mathcal E_\perp(D)=\frac1{|G|}\sum_\xi
       |\widehat{1_D}(\xi)|^2
       |\widehat{1_D}(J\xi)|^2.                 \tag{3.7}
\]

The direct sum (3.3) additionally gives exact control of the unshifted joint
spectrum:

\[
 \frac1{|G|}\sum_\xi
 |\widehat{1_A}(\xi)|^2|\widehat{1_A}(J\xi)|^2
 =|A+JA|=k^2.                                    \tag{3.8}
\]

Equations (3.5)--(3.8) turn (1.2) into a rotated fourth-moment uncertainty
principle for a shifted nonnegative spectrum.  This is the main structural
advantage over the seven-incidence switching expansion.

## 4. Radial uniqueness alone fails polynomially

The canonical radial transversals from
`RADIAL_ORTHOGONAL_PRODUCT_BARRIER.md` violate (1.2) by a growing power-scale
factor.  Their exact normalized products are

\[
\begin{array}{c|r|c}
\text{box side}&N&U\\ \hline
8&83&4.4090\ldots\\
12&165&7.7268\ldots\\
20&395&15.1898\ldots\\
30&815&27.6310\ldots
\end{array}                                                   \tag{4.1}
\]

Hence (3.1), central symmetry, and one point per radius do not prove the
energy product.  Any proof must use (3.4), or an equivalent fact that `D` is
the complete difference set of one distance-Sidon configuration.

## 5. Proof routes and falsification criterion

The most credible routes are now:

1. **Shifted-positive Fourier inequality.**  Use (3.5), (3.8), and the exact
   first two moments forced by additive Sidonicity to show that a large
   fourth moment cannot remain aligned with its quarter-turn.
2. **Dyadic spectral inverse theorem.**  If both factors in (1.2) are
   polynomially too large, extract a common high spectrum for `D` and `JD`.
   Lift it through (3.4) to simultaneous additive structure in `A` and `JA`,
   contradicting the directness of (3.2) or forcing the already-solved
   high-support branch.
3. **Physical-space common-energy inverse theorem.**  Large
   `E_+(D)E_perp(D)` gives many translations on which both `D` and `JD` have
   large overlap.  The inverse theorem must retain the unique endpoint
   decorations; a generic BSG conclusion ending at a rank-two progression
   merely returns to the grid.

A decisive kill is an infinite family of distance-Sidon sets with

\[
 \mathcal E_+(D)\mathcal E_\perp(D)
   \ge N^{5+\varepsilon}                          \tag{5.1}
\]

for fixed `epsilon>0`.  The dense perpendicular-ruler family supplies exactly
this with `epsilon=1`: both factors are `Omega(N^3)`.  It was inadvertently
omitted from the original profile table.  The gate is therefore closed.

Run `verify_orthogonal_energy_product_gate.py` for all exact profiles in
Sections 2 and 4.
