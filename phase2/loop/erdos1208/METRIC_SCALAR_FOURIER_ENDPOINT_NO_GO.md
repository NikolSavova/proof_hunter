# Fourier form and an endpoint-positivity no-go for the metric scalar charge

## 1. Verdict

Keep the notation of `METRIC_SCALAR_PAIR_SUM_CHARGE.md`.  Thus

\[
 B=B_q=\delta(H_q),\qquad D=\delta(\Sigma),
 \qquad |B|=h,\quad |D|=N=\binom k2,
\]

and the live charge has coefficient `C=18`.  Its energy has the exact
one-dimensional Fourier form

\[
 \boxed{
 \mathcal M_{q,18}
 =\int_{\mathbb T}|S_B(\theta)|^2
                    |S_D(18\theta)|^2\,d\theta,}            \tag{1.1}
\]

where `S_E(theta)=sum_(n in E)e^(2 pi i n theta)`.  After deleting the
identical-record diagonal,

\[
 \boxed{
 \mathcal M_{q,18}-hN
 =\int_{\mathbb T} (|S_B|^2-h)
                    (|S_D(18\theta)|^2-N)\,d\theta.}        \tag{1.2}
\]

The contribution with three distinct edge labels is at most `4h^2` by
Proposition 2.1 of the scalar-charge note.  Consequently (1.2), up to that
already acceptable term, is exactly the four-distinct-label problem.

There is an exact coefficientwise-positive square lift of (1.1), given in
Section 3 below.  However, its unsquared scalar polynomial is **not** an
endpoint-positive spectrum.  This failure is unavoidable, not a defect of
one choice of orientation:

> **Radial endpoint no-go.**  For every `k` divisible by `9` there is a
> polynomial-height integral distance-Sidon set `A` of size `k` for which
> the natural symmetrized squared-distance spectrum satisfies
> \[
>  k+2\sum_{d\in D}\cos(2\pi d/3)=-k^2/3.       \tag{1.3}
> \]
> More generally, a scalar shift `c` which makes
> `c+S_D+conjugate(S_D)` nonnegative for every distance-Sidon endpoint set
> must have
> \[
>  c\ge k^2/3+k=(2/3+o(1))N.                   \tag{1.4}
> \]

Since `18*(1/54)=1/3`, dilation by `18` retains this exact negative mode.
Thus the positive endpoint autocorrelation cannot be pushed through the
squared-norm map by this natural radialization and then used as an
unsquared positive factor at the scalar frequency.  In particular, the
direct radial analogue of the load-bearing condition
`|widehat(1_A)|^2>=0` in the Gaussian Fourier lift does not exist.

This is a rigorous no-go for **positivity-preserving radial Fourier lifts**,
not a counterexample to the metric scalar estimate.  A proof may still use
the endpoint decorations before radial projection, or use arithmetic of the
four squared distances.  It cannot obtain that missing information merely
by declaring the scalar squared-distance spectrum positive definite.

## 2. Exact Fourier form and the four-label core

Use the convention

\[
 S_E(\theta)=\sum_{x\in E}e^{2\pi i x\theta}.
\]

The Fourier coefficient of `|S_E|^2` at `r` is `r_(E-E)(r)`.  Haar
orthogonality in (1.1) imposes `a+18b=0` and therefore gives

\[
 \int |S_B(\theta)|^2|S_D(18\theta)|^2\,d\theta
 =\sum_r r_{B-B}(18r)r_{D-D}(-r),              \tag{2.1}
\]

which is the physical-space collision formula exactly.

Also `int |S_B|^2=h` and, since multiplication by `18` preserves Haar
measure, `int |S_D(18 theta)|^2=N`.  Expanding the right side of (1.2)
therefore proves the centered identity.

Let `R_3` be the number of ordered off-diagonal collisions using exactly
three distinct unordered edge labels, and let `R_4` be the corresponding
number using four.  The repeated-label proposition says

\[
 R_3\le4h^2,
\]

while injectivity of the metric label gives the exact decomposition

\[
 \boxed{
 R_4=\int (|S_B|^2-h)(|S_D(18\theta)|^2-N)\,d\theta-R_3.}   \tag{2.2}
\]

Both centered factors in (2.2) have mean zero and, when their underlying
sets have more than one point, change sign.  Hence the
four-label deletion has not produced a nonnegative Fourier integrand; this
is precisely where an endpoint-positive lift would have been useful.

## 3. An exact direct scalar square lift

For any `c>=0`, form the symmetric scalar measure

\[
 \gamma_c=c\delta_0+1_D+1_{-D},
 \qquad
 P_c(\theta)=\widehat\gamma_c(\theta)
 =c+S_D(\theta)+\overline{S_D(\theta)}.         \tag{3.1}
\]

Define

\[
 \mathcal L_{q,c}
 =\int_{\mathbb T}|S_B(\theta)|^2P_c(18\theta)^2\,d\theta. \tag{3.2}
\]

Because `D` contains positive squared distances only,

\[
 (\gamma_c*\gamma_c)(0)=c^2+2N.                \tag{3.3}
\]

Moreover the two cross-convolutions between `1_D` and `1_(-D)` give

\[
 \boxed{
 \gamma_c*\gamma_c\ge
 c^2\delta_0+2r_{D-D}}
 \quad\hbox{coefficientwise}.                 \tag{3.4}
\]

Consequently

\[
 \boxed{
 \mathcal X_{q,c}:=
 \mathcal L_{q,c}-(c^2+2N)h
 \ge2(\mathcal M_{q,18}-hN)\ge0.}             \tag{3.5}
\]

This is the exact scalar counterpart of the Gaussian coefficientwise
square.  It is valid for every finite pair of integer sets `B subset D`;
it has not yet used endpoints.

That last fact is fatal to the proposed positivity step.  The polynomial
`P_c` is real, so its square in (3.2) is nonnegative even when `P_c` is
negative.  To recover unsquared endpoint positivity one would need `P_c>=0`
at the endpoint-sized shift `c=k`.  Theorem 4.1 shows instead that
`P_k(1/3)=-k^2/3`.  Raising the shift to the universally necessary scale
`c=Omega(N)` puts `Omega(N^2h)` into the zero-frequency part of (3.2), a
factor `N` above the target diagonal `Nh`; positivity alone then supplies
no useful upper bound for the excess in (3.5).

## 4. Why squared-norm radialization destroys endpoint positivity

For a distance-Sidon endpoint set, put

\[
 H_A(x)=\left|\sum_{a\in A}e^{2\pi i a\cdot x}\right|^2
 =k+2\sum_{u\in U}\cos(2\pi u\cdot x)\ge0,    \tag{4.1}
\]

where `U` contains one orientation of every nonzero edge.  The actual
radial pushforward of the endpoint autocorrelation is

\[
 \Theta_A(t)=\sum_{a,b\in A}e^{2\pi i t|a-b|^2}
 =k+2S_D(t).                                    \tag{4.2}
\]

Thus there is also the exact endpoint-enumerator form

\[
 \boxed{
 \mathcal M_{q,18}
 ={1\over4}\int_{\mathbb T}|S_B(\theta)|^2
       |\Theta_A(18\theta)-k|^2\,d\theta.}      \tag{4.2a}
\]

It retains the unsquared endpoint enumerator exactly, but that enumerator
is generally complex.  Its real symmetrization is `P_k`.
The reason positivity does not pass from (4.1) to (4.2) is algebraic:

\[
 u\longmapsto |u|^2
\]

is not a homomorphism.  In particular edge reversal sends `u` to `-u` but
does not send its squared norm to its additive inverse.  Pushforward of a
positive-definite function is safe under a group homomorphism; the norm map
has no such property.

### Theorem 4.1 (genuine polynomial-height obstruction)

For every `k=9r`, there is a distance-Sidon set `A subset Z^2`, contained
in a square of side `O(k^3)`, with exactly `r` points in each residue class
of `(Z/3Z)^2`.  For this set, equations (1.3) and (1.4) hold.

### Proof

First prescribe any sequence of `k` residue classes.  Construct the points
one at a time.  If `n` old points have already been chosen, a candidate
`x` in the next prescribed class is forbidden only when

1. `|x-a_i|^2` equals one of the `O(n^2)` old squared distances, for one
   of the `n` old endpoints; or
2. `|x-a_i|^2=|x-a_j|^2` for two old endpoints.

The first conditions lie on `O(n^3)` circles and the second on `O(n^2)`
proper lines.  Each such curve contains `O(M)` lattice points in an
`M` by `M` square, whereas the prescribed residue class contributes
`Theta(M^2)` candidates.  Taking `M=Cn^3` with a sufficiently large
absolute constant leaves a candidate.  Induction gives a distance-Sidon
set of height `O(k^3)` in the prescribed classes.

Now prescribe every residue class exactly `r=k/9` times.  A squared
distance is divisible by `3` exactly when its two endpoints have the same
ordered residue class: a sum of two squares is `0 mod 3` only when both
coordinate differences are `0 mod 3`.  Hence, among the `N=binom(k,2)`
squared distances, precisely

\[
 N_0=9\binom r2={k^2\over18}-{k\over2}          \tag{4.3}
\]

are divisible by `3`.  At frequency `1/3`, the cosine is `1` on those
labels and `-1/2` on every other label.  Therefore

\[
 \begin{aligned}
 P_c(1/3)
 &=c+2N_0-(N-N_0)\\
 &=c+3N_0-N\\
 &=c-{k^2\over3}-k.                            \tag{4.4}
 \end{aligned}
\]

Putting `c=k` proves (1.3), while nonnegativity forces (1.4).  QED.

Equivalently, the radial cosine multiplier which sends the coefficient at
`u` in (4.1) to `cos(2 pi t|u|^2)` does not preserve even the cone of
genuine endpoint autocorrelations: at `t=1/3`, its value at `x=0` is
`-k^2/3`.

## 5. Adversarial checks

The exact verifier records three complementary behaviours.

1. **The resonant two-arm family does not hurt the scalar gate.**  On the
   same fibres that disprove the Gaussian vector charge, the scalar ratios
   `M/(hN)` at `s=8,16,32,50` are
   \[
    1,quad1,quad1.001736\ldots,quad1.002027\ldots.
   \]
   The maximum loads are respectively `1,1,2,3`.

2. **The Fourier excess correctly diagnoses the false Gaussian gate.**  On
   those fibres the shifted-positive excesses `X_q` from
   `GAUSSIAN_EDGE_VECTOR_FOURIER_LIFT.md` are
   \[
    0,quad540,quad116708,quad1904582.
   \]
   At `s=50` this is already `1.79796... N(h+k)`.  Asymptotically the
   compensation inequality and the two-arm lower bound give
   `X_q>=2(G_q-Nh)=Omega(s^6)`.

3. **Norm uniqueness alone is far too weak.**  For the canonical radial
   transversals, taking `B=D` gives `M/N^2` equal to
   `1.6305..., 5.0093..., 14.5216..., 46.2301...` at box sides
   `8,20,40,80`.  In contrast, the genuine dense perpendicular-ruler
   profile has ratio `10938/10920=1.001648...`.  Thus the present genuine
   endpoint stresses do not exhibit the large formal radial correlations;
   the scalar PSD formalism itself does not exclude them.

The finite data are consistent with the live scalar conjecture.  The
theorem above says only that its proof cannot come from a
positivity-preserving radialization of the endpoint spectrum.

Run

```text
python3 phase2/loop/erdos1208/verify_metric_scalar_fourier_endpoint_no_go.py
```

for the exact certificates.

## 6. Remaining viable Fourier question

Equation (2.2) is still a potentially useful Fourier formulation, but any
successful estimate must retain data which disappear under the norm map.
Concretely, it must attach the four scalar labels to their four endpoint
edges before using positivity, or prove a number-theoretic inverse theorem
for the dilation-specific equation

\[
 \delta(E_1)-\delta(E_2)
 =18\bigl(\delta(F_2)-\delta(F_1)\bigr)
\]

with four distinct edge labels.  A one-dimensional radial relaxation whose
only endpoint input is nonnegativity of the natural shifted scalar
polynomial cannot supply that step.
