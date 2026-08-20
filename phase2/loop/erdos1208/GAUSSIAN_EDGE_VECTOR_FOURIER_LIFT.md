# Fourier lift and shifted-positive excess for the Gaussian edge charge

> **Status caveat (2026-08-19).**  The Fourier identities and compensation
> inequality in this note are correct, but the underlying Gaussian energy
> target is false.  The genuine two-arm distance-Sidon family in
> `GAUSSIAN_EDGE_VECTOR_TWO_ARM_BARRIER.md` forces the excess in (1.4) to be
> polynomially too large.  This note is therefore a diagnostic description
> of where that family concentrates endpoint spectrum, not a remaining
> sufficient gate for the full problem.

## 1. Result

Keep the notation of `GAUSSIAN_EDGE_VECTOR_CHARGE.md`.  Thus `A` is a
distance-Sidon set of size `k`,

\[
 \Sigma=A\mathbin\oplus A,
 \qquad N=|\Sigma|=\binom k2,
\]

`U` contains the canonically oriented edge vector belonging to every
pair sum in `Sigma`, and `U_q` is the corresponding subset belonging to a
clean start fibre `H_q`.  Put `h_q=|H_q|` and

\[
 \lambda=3(I+J).
\]

There is an exact positive Fourier lift of the Gaussian vector energy.  If

\[
 \alpha=1_A\circ1_A
        =k\delta_0+1_U+1_{-U},                  \tag{1.1}
\]

define

\[
 \mathcal L_q
 :=\int_{\mathbb T^2}
   |\widehat {1_{U_q}}(\theta)|^2
   |\widehat {1_A}(\lambda^T\theta)|^4\,d\theta. \tag{1.2}
\]

Then

\[
 \boxed{
 \mathcal G_q
 \le N h_q+\frac12\mathcal X_q,}               \tag{1.3}
\]

where the shifted-positive excess

\[
 \boxed{
 \mathcal X_q
 :=\mathcal L_q-(2k^2-k)h_q
 =\sum_{z\ne0}(\alpha*\alpha)(z)
                  r_{U_q-U_q}(-\lambda z)\ge0.} \tag{1.4}
\]

Formally, the single estimate

\[
 \boxed{
 \mathcal X_q\le m^{o(1)}N(h_q+k)}              \tag{1.5}
\]

for all realized `q` would imply the Gaussian charge gate and hence the
cube-root upper bound in Erdős problem 1208.  The two-arm barrier shows that
this estimate does not hold in general.

This is a rigorous partial branch, not a proof of (1.5).  Its value is that
the whole diagonal has been removed inside a genuinely nonnegative
complete-endpoint spectrum.  On the stored perpendicular-ruler and Costas
stresses, `X_q=0` exactly.  On every other stored genuine stress tested
below, `X_q<=0.142 N h_q`.

There is also a precise limitation.  Squaring the complete-difference
spectrum erases its sign.  The canonical radial-transversal pseudomodel
still has `X_q=N^(3-o(1))`, a full power above the target `N^2`.  Thus a
proof of (1.5) must ultimately use the unsquared autocorrelation positivity

\[
 \widehat\alpha=|\widehat {1_A}|^2\ge0           \tag{1.6}
\]

or the clean endpoint factorization.  Positivity of the lifted square
alone is insufficient.

## 2. Exact Fourier expression for the Gaussian energy

Use the convention

\[
 \widehat f(\theta)=\sum_{x\in\mathbb Z^2}
 f(x)e^{2\pi i x\cdot\theta}.
\]

Set

\[
 F=\widehat {1_U},
 \qquad F_q=\widehat {1_{U_q}}.
\]

Since the Fourier coefficients of `|F|^2` and `|F_q|^2` are respectively
`r_(U-U)` and `r_(U_q-U_q)`, Haar orthogonality gives

\[
 \boxed{
 \mathcal G_q
 =\int_{\mathbb T^2}|F_q(\theta)|^2
            |F(\lambda^T\theta)|^2\,d\theta.}  \tag{2.1}
\]

Indeed, a surviving Fourier term satisfies
`u_q-u'_q=-lambda(u-u')`, exactly the collision equation in the vector
charge.  The torus endomorphism caused by `lambda` is harmless; composition
with its transpose is the correct pullback of lattice frequencies.

The complete-difference positivity is visible before squaring.  From
(1.1),

\[
 P(\theta):=\widehat\alpha(\theta)
 =|\widehat {1_A}(\theta)|^2
 =k+F(\theta)+\overline{F(\theta)}\ge0.          \tag{2.2}
\]

Thus the canonical one-sided edge spectrum satisfies the shifted real-part
constraint

\[
 \operatorname{Re}F(\theta)\ge-k/2.            \tag{2.3}
\]

Equation (2.3) is much stronger than radial uniqueness, but it controls
only the real part of `F`, whereas (2.1) contains `|F|^2`.  The lift below
is an exact way to retain the endpoint autocorrelation without asserting a
false pointwise modulus bound.

## 3. Coefficientwise positive lift

Convolving (1.1) with itself gives

\[
 \begin{aligned}
 \alpha*\alpha
 ={}&k^2\delta_0+2k(1_U+1_{-U})\\
   &+1_U*1_U+1_{-U}*1_{-U}
     +2(1_U*1_{-U}).                            \tag{3.1}
 \end{aligned}
\]

The last convolution is exactly `r_(U-U)`.  Every other displayed
coefficient is nonnegative, so

\[
 \boxed{
 \alpha*\alpha\ge k^2\delta_0+2r_{U-U}}
 \quad\text{coefficientwise}.                  \tag{3.2}
\]

Multiplying (3.2) by `r_(U_q-U_q)(-lambda z)` and summing over `z` proves

\[
 \mathcal L_q\ge k^2h_q+2\mathcal G_q.         \tag{3.3}
\]

Here Parseval and `P^2=|widehat(1_A)|^4` give the two equivalent exact
forms

\[
 \begin{aligned}
 \mathcal L_q
 &=\int |F_q(\theta)|^2P(\lambda^T\theta)^2\,d\theta\\
 &=\sum_z(\alpha*\alpha)(z)
                   r_{U_q-U_q}(-\lambda z).    \tag{3.4}
 \end{aligned}

At zero,

\[
 (\alpha*\alpha)(0)=\sum_x\alpha(x)^2
 =k^2+2N=2k^2-k.                               \tag{3.5}
\]

Subtracting the zero term in (3.4) gives (1.4).  Also

\[
 \mathcal L_q-k^2h_q
 =2Nh_q+\mathcal X_q.                           \tag{3.6}
\]

Combining (3.3) and (3.6) proves (1.3).  Equivalently,

\[
 \boxed{
 0\le2(\mathcal G_q-Nh_q)\le\mathcal X_q.}     \tag{3.7}
\]

This is the promised compensation inequality: all off-diagonal Gaussian
collisions are charged to a nonnegative, off-zero complete-endpoint
spectrum, with no diagonal loss.

The same excess can be written as a covariance:

\[
 \mathcal X_q
 =\int |F_q(\theta)|^2
   \bigl(P(\lambda^T\theta)^2-(2k^2-k)\bigr)\,d\theta. \tag{3.8}
\]

The integrand in (3.8) need not be pointwise nonnegative.  Its integral is
nonnegative because both factors have nonnegative nonzero Fourier
coefficients after the constant term is removed.  This distinction is why
a naive pointwise argument is unavailable but exact spectral compensation
still survives.

## 4. A rigorous diffuse endpoint-spectrum branch

Define the largest resonant nonzero endpoint coefficient

\[
 \mu_q:=\max\{(\alpha*\alpha)(z):z\ne0,
                    -\lambda z\in U_q-U_q\},   \tag{4.1}
\]

with `mu_q=0` if the set is empty.  Since `lambda` is injective and

\[
 \sum_{y\ne0}r_{U_q-U_q}(y)=h_q(h_q-1),
\]

(1.4) gives the exact bound

\[
 \boxed{\mathcal X_q\le\mu_q h_q(h_q-1).}       \tag{4.2}
\]

Hence (1.5), and therefore the full Gaussian gate, holds on every fibre
satisfying

\[
 \mu_qh_q(h_q-1)le m^{o(1)}N(h_q+k).           \tag{4.3}
\]

For the hard fibres `h_q>k`, the clean sufficient condition is

\[
 \mu_q\le m^{o(1)}{N\over h_q}.                \tag{4.4}
\]

This branch is elementary but nonvacuous: it isolates the only remaining
possibility as simultaneous popularity of a second-difference vector in
the complete endpoint autocorrelation and its Gaussian dilation in one
clean edge fibre.  A maximum coefficient theorem is not expected globally;
the likely next step is a dyadic version of (4.2).

## 5. Exact genuine profiles

The companion verifier computes

\[
 (\mathcal G_q,\mathcal L_q,\mathcal X_q,
   2(\mathcal G_q-Nh_q),
   \mathcal X_q-2(\mathcal G_q-Nh_q)).
\]

For the largest clean fibre in each stored family:

\[
\begin{array}{c|r|r|r|r|r}
\text{family}&\mathcal G_q&\mathcal L_q&\mathcal X_q
 &2(\mathcal G_q-Nh_q)&\text{slack}\\ \hline
\text{closure }30&6180&24968&188&180&8\\
\text{closure }40&18876&75226&2546&1872&674\\
\text{closure }80&207504&822960&21600&16848&4752\\
\text{source }45&22238&89326&1216&916&300\\
\text{perpendicular ruler }40&10920&44240&0&0&0\\
\text{Costas }22&7854&32164&0&0&0\\
\text{parabola image }43&159191&634561&9556&9556&0\\
\text{integer parabola }50&93097&373904&2654&2444&210
\end{array}                                      \tag{5.1}
\]

Thus the perpendicular-ruler family which killed several earlier Fourier
energies is exactly resonance-free after subtracting the forced endpoint
diagonal.  The maximum observed normalized excess is

\[
 {\mathcal X_q\over Nh_q}=0.141918\ldots
\]

on closure 40.  These are exact falsification data, not an asymptotic proof.

## 6. Radial square-spectrum no-go

Let `R_M` contain one lattice representative from each occupied radius in
an `M`-box, and choose a subset `U subset R_M` of triangular cardinality

\[
 N=\binom k2=M^{2-o(1)}.                       \tag{6.1}
\]

Set `U_q=U`, `h_q=N`, and form the formal complete radial coefficient

\[
 \alpha_M=k\delta_0+1_U+1_{-U}.                \tag{6.2}
\]

All vectors of `U+lambda U` lie in an `O(M)` box.  Cauchy--Schwarz gives

\[
 \mathcal G_M
 =\sum_zr_{U+\lambda U}(z)^2
 \ge {N^4\over O(M^2)}=N^{3-o(1)}.             \tag{6.3}
\]

The coefficientwise proof of (3.7) applies verbatim to (6.2), so

\[
 \mathcal X_M\ge2(\mathcal G_M-N^2)
 =N^{3-o(1)}.                                   \tag{6.4}
\]

This exceeds the desired `N(h_q+k)=N^(2+o(1))` by essentially a full
power.  Yet the lifted square

\[
 \widehat{\alpha_M*\alpha_M}=\widehat\alpha_M^{,2}
\]

is nonnegative pointwise simply because `alpha_M` is real and symmetric.
Therefore no argument using only positivity of the *squared* spectrum in
(1.2), or only the nonnegative coefficients of `alpha_M*alpha_M`, can
prove (1.5).

The pseudomodel need not satisfy `widehat(alpha_M)>=0`; that is exactly the
information erased by squaring.  A successful continuation must use the
unsquared shifted-positive condition (2.2), the zero-one spectral
factorization by `1_A`, or the clean source-to-target endpoint matching in
`H_q`.

## 7. Research consequence

The Fourier lift gives a real new branch but not a shortcut:

* the Gaussian energy has the exact mixed Fourier form (2.1);
* its entire off-diagonal part is bounded by half of the positive endpoint
  excess `X_q`;
* diffuse resonant endpoint spectrum is closed by (4.3);
* the two strongest stored additive adversaries have `X_q=0` exactly;
* radial uniqueness plus square-spectrum positivity remains insufficient.

The next viable Fourier question is therefore very specific: can the
unsquared positivity `P>=0` and the clean pair-sum shift defining `H_q`
force a dyadic bound for the common nonzero coefficients in (1.4)?  Generic
Hölder estimates for `P^2` discard the only condition which the radial
pseudomodel violates and should not be pursued.
