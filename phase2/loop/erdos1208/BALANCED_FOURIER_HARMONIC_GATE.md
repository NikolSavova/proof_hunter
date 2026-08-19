# A balanced Fourier gate that suppresses the ruler obstruction

## 1. The new sufficient moment

Let `A subset [0,m]^2`, `|A|=k`, be distance-Sidon, and write

\[
 H(\theta)=|\widehat{1_A}(\theta)|^2,
 \qquad H_J(\theta)=H(J\theta)
\]

on the two-dimensional torus.  Define the balanced harmonic moment

\[
 \boxed{
 \mathfrak B(A)=
 \int_{\mathbb T^2}
 {H(\theta)^2H_J(\theta)^2\over H(\theta)+H_J(\theta)}\,d\theta,}       \tag{1.1}
\]

with value zero when both terms vanish.

This is not one of the polynomial moments killed in
`POSITIVE_DEFINITE_BESSEL_AUDIT.md`.  If one of `H,H_J` is much larger than
the other, the denominator removes the large one.  Pointwise,

\[
 {1\over2}HH_J\min(H,H_J)
 \le {H^2H_J^2\over H+H_J}
 \le HH_J\min(H,H_J).                            \tag{1.2}
\]

Thus (1.1) measures only *balanced* simultaneous Fourier concentration.

### Proposition 1.1

If

\[
 \boxed{\mathfrak B(A)\le k^{3+o(1)}}             \tag{1.3}
\]

for every integral planar distance-Sidon set, then

\[
 k\le m^{2/3+o(1)},                              \tag{1.4}
\]

which resolves the power-law order in Erdős 1208.

### Proof

When `||theta||_infty<=1/(16m)`, all phases in the exponential sum lie in
an arc of length at most `pi/2`, after one common rotation.  Hence

\[
 H(\theta),H_J(\theta)\ge{k^2\over2}.
\]

Since both are at most `k^2`, the integrand in (1.1) is at least `k^6/32`
on a square of area `1/(64m^2)`.  Therefore

\[
 \boxed{\mathfrak B(A)\ge{k^6\over2048m^2}.}     \tag{1.5}
\]

Combining (1.3) and (1.5) proves (1.4).  QED.

The claim (1.3) is a new gate, not a proved theorem.

## 2. Exact balanced-tail formulation

Distance-Sidonicity gives

\[
 \int H^2=2k^2-k,
 \qquad
 \int HH_J=k^2.                                  \tag{2.1}
\]

The second identity follows from

\[
 (A-A)\cap J(A-A)=\{0\}.
\]

The portion of (1.1) on which `min(H,H_J)<=k` is already at most

\[
 k\int HH_J=k^3.                                 \tag{2.2}
\]

For `i,j>=0`, put

\[
 \Omega_{i,j}=
 \{2^ik\le H<2^{i+1}k,\quad
   2^jk\le H_J<2^{j+1}k\}.                      \tag{2.3}
\]

The joint large-spectrum estimate

\[
 \boxed{
 |\Omega_{i,j}|
 \le k^{o(1)}2^{-i-j-\min(i,j)}}                 \tag{2.4}
\]

implies (1.3), after summing only `O(log^2 k)` nonempty levels.  Conversely,
any fixed-power failure of (1.3) forces a fixed-power failure of (2.4) on
some dyadic level.

The known moments in (2.1) give

\[
 |\Omega_{i,j}|\ll
 \min\{2^{-i-j},2^{-2i},2^{-2j}\}.              \tag{2.5}
\]

This already proves (2.4) whenever `i>=2j` or `j>=2i`.  The entire missing
Fourier theorem is therefore confined to the balanced cone

\[
 {1\over2}i<j<2i,                                \tag{2.6}
\]

where both `A` and its quarter-turn have comparably large Fourier bias.
This is the spectral form of the Gaussian-core density increment: one large
coefficient can describe a ruler or a strip, while two balanced orthogonal
biases should force a genuinely two-dimensional resonant core.

## 3. A rigorous line branch

The balanced moment automatically handles the obstruction that destroys the
ordinary mixed third and fourth moments.

### Proposition 3.1

If `A` is collinear and distance-Sidon, then

\[
 \boxed{\mathfrak B(A)<4k^3.}                   \tag{3.1}
\]

### Proof

After translation, write `A={t v:t in R}` for a primitive integral vector
`v`.  The one-dimensional set `R` is a Golomb ruler.  Consequently its
one-dimensional squared exponential sum `X` satisfies

\[
 \mathbb E X=k,qquad \mathbb E X^2=2k^2-k.     \tag{3.2}
\]

The torus homomorphism

\[
 \theta\longmapsto(v\cdot\theta,Jv\cdot\theta)
\]

is surjective and preserves Haar measure.  Hence `H` and `H_J` have the
law of two independent copies `X,Y`.  Split their product space into
`X>=Y` and `Y>X`.  On the first part the integrand is at most `XY^2`; on
the second it is at most `X^2Y`.  Dropping the restrictions and using
independence gives

\[
 \mathfrak B(A)
 \le 2(\mathbb EX)(\mathbb EX^2)
 =2k(2k^2-k)<4k^3.                               \tag{3.3}
\]

QED.

The same argument has a useful mult-line extension.

### Proposition 3.2

If `A` is covered by `r` parallel lines, then

\[
 \boxed{\mathfrak B(A)<4r^3k^3.}                \tag{3.4}
\]

### Proof

Partition `A` into its intersections `A_1,...,A_r` with the lines and put

\[
 U(\theta)=\sum_{\ell=1}^r
 |\widehat{1_{A_\ell}}(\theta)|^2.
\]

Cauchy gives `H<=rU` and `H_J<=rU_J`.  The integrand in (1.1) is increasing
in both variables and homogeneous of degree three, so

\[
 \mathfrak B(A)
 \le r^3\int UU_J\min(U,U_J).                  \tag{3.5}
\]

If `v` is the common primitive direction, the magnitude of every line sum
depends only on `v dot theta`.  The torus homomorphism from the preceding
proof therefore makes `U,U_J` independent copies of one random variable.
Moreover

\[
 \mathbb E U=k,
 \qquad
 \mathbb E U^2
 =k^2+\sum_{\ell=1}^r|A_\ell|^2-k<2k^2.        \tag{3.6}
\]

For (3.6), nonzero one-dimensional difference frequencies belonging to
different lines are disjoint: otherwise two within-line segments of `A`
would have the same Euclidean length.  Splitting into `U>=U_J` and its
complement as before bounds the last integral in (3.5) by
`2(E U)(E U^2)<4k^3`.  This proves (3.4).  QED.

Thus (1.3) is already rigorous for every subpolynomial parallel-line cover.
This also helps explain why perpendicular Golomb rulers can have maximal
ordinary mixed energy while remaining harmless for (1.1): their large
Fourier mass lives primarily on imbalanced strips.

## 4. Stress tests and scope

High-resolution torus evaluations give the following ratios.  These are
numerical diagnostics, not proof of (1.3).

\[
\begin{array}{c|c}
\text{family}&\mathfrak B(A)/k^3\\ \hline
\text{closure }k=20,60,120&1.153,1.414,1.619\\
\text{perpendicular rulers }k=16,40&0.860,1.092\\
\text{fixed-colour closure }k=65&0.816\\
\text{hybrid closure }k=45&1.153\\
\text{determinant-prime Costas }k=10\ldots42&0.735\ldots0.805
\end{array}
\]

In particular, the dense perpendicular-ruler family that makes
`int H^2 H_J^2` as large as `Omega(k^6)` does not inflate the balanced
moment.  The closure chain is the strongest stored stress and grows slowly
enough to remain compatible with a subpolynomial factor.

The next proof task is now precise: prove (2.4) in the balanced cone using
the complete-difference identity

\[
 \widehat{(k-1)\delta_0+1_{A-A}}=|\widehat{1_A}|^2
\]

and ambient-height control of the resulting two-dimensional resonance
core.  Ordinary second moments supply every imbalanced level for free.

`verify_balanced_fourier_harmonic_gate.py` checks (1.2), both exact moments
in (2.1), the line and parallel-cover moment identities, and finite-torus
regression profiles on three exact distance-Sidon witnesses.
