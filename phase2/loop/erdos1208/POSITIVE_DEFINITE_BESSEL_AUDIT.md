# Positive-definite and Bessel audit for Erdős #1208

## 1. Verdict

Let `A subset {0,...,m}^2` be distance-Sidon and put `k=|A|`.  Write

\[
 h=1_A\circ 1_A,
 \qquad
 H(\theta)=\widehat h(\theta)=|\widehat {1_A}(\theta)|^2.
\]

Then `h(0)=k`, every nonzero coefficient of `h` is one, and the
nonzero coefficients occur in antipodal pairs with distinct squared norms.
In particular

\[
 H(\theta)=k+2\sum_{\{a,b\}\in\binom A2}
 \cos(2\pi\theta\cdot(a-b))\ge0.              \tag{1.1}
\]

This note audits four ways of using (1.1).

1. The first mixed quarter-turn moment is exactly `k^2`.  Combining this
   with the peak of `H` at the origin gives only `k=O(m)`.
2. The next mixed moment has exactly the right peak scale: an upper bound
   `O(k^(5+o(1)))` would prove `k<=m^(2/3+o(1))`.  It is false.  Dense
   perpendicular Golomb rulers make this moment `Omega(k^6)`.
3. Rotation averaging gives the valid scalar Bessel inequalities

   \[
   k+2\sum_{\{a,b\}}J_0(2\pi\rho|a-b|)\ge0.    \tag{1.2}
   \]

   A single Delsarte-style radial kernel which is uniformly negative on
   every allowable lattice radius cannot be strong: the full square grid
   forces its negativity to be only `O(m^(-2))`.  Thus any viable radial LP
   must depend on the *occupied* radii and use their endpoint compatibility;
   a universal sign kernel cannot approach the cube-root exponent.
4. Even the scalar Bessel cone on an adaptively selected set of radii has
   exponent-level pseudoconfigurations: there are `K=Theta(m)` and
   `Theta(K^2)` distinct integer squared radii at most `2m^2` for which the
   Bessel sum is nonnegative for every frequency.  The construction has the
   correct quadratic number of shells, but not the exact coefficient
   identity `number of shells=K(K-1)/2`.  Thus an argument using only power
   scales cannot work; an exact argument could still use that identity.

These are rigorous barriers to the most direct positive-definite attacks.
They do not rule out a nonlinear or configuration-adaptive use of (1.1).

## 2. Exact first and second moments

Let `D=A-A` and `D*=D minus {0}`.  Distance-Sidonicity gives

\[
 h=k\delta_0+1_{D^*}.                           \tag{2.1}
\]

Parseval immediately yields

\[
 \int_{\mathbb T^2}H=k,
 \qquad
 \int_{\mathbb T^2}H^2
   =k^2+|D^*|=2k^2-k.                            \tag{2.2}
\]

Let `J(x,y)=(-y,x)`, and write `H_J(theta)=H(J theta)` (the choice of `J`
or `J^{-1}` is immaterial here).  There is no nonzero element of
`D intersect JD`.  Indeed, `d=Je` would give `|d|=|e|`; radial uniqueness
then gives `e=plus or minus d`, while a nonzero real vector is not equal to
either quarter-turn of itself.  Hence the Fourier supports of `H-k` and
`H_J-k` are disjoint.  Therefore

\[
 \boxed{\int_{\mathbb T^2}H(\theta)H_J(\theta)\,d\theta=k^2.} \tag{2.3}
\]

Equivalently, the centered functions `H-k` and `H_J-k` are exactly
orthogonal in `L^2` even though they have the common height `k^2-k` at the
origin.

## 3. Why (2.3) recovers only the linear grid bound

If

\[
 \|\theta\|_\infty\le {1\over16m},
\]

then the arguments `2 pi theta dot a`, as `a` ranges over the square, lie
in an interval of length at most `pi/4`.  After multiplying the exponential
sum by one phase, all of its summands have real part at least `1/sqrt(2)`.
Consequently

\[
 H(\theta)\ge{k^2\over2},
 \qquad
 H_J(\theta)\ge{k^2\over2}.                    \tag{3.1}
\]

The square in (3.1) has area `1/(64m^2)`.  Using nonnegativity away from it
and (2.3),

\[
 k^2=\int HH_J
 \ge {k^4\over4}\,{1\over64m^2}.
\]

Thus

\[
 \boxed{k\le16m.}                              \tag{3.2}
\]

The constants are unimportant.  The point is the scale: the exact mixed
second moment and band limitation have only enough strength for the usual
linear bound, not `m^(2/3)`.

## 4. The tempting next moment, and its exact obstruction

The same origin square gives

\[
 \int_{\mathbb T^2}H^2H_J^2
 \ge {k^8\over16}\,{1\over64m^2}
 ={k^8\over1024m^2}.                            \tag{4.1}
\]

Therefore the estimate

\[
 \int H^2H_J^2\le k^{5+o(1)}                  \tag{4.2}
\]

would imply `k^3<=m^(2+o(1))` and settle the desired exponent.

But (4.2) is false by a full power.  Since `D=-D`, Parseval gives, for the
unweighted difference-set polynomial,

\[
 \int |\widehat {1_D}(\theta)|^2
          |\widehat {1_D}(J\theta)|^2\,d\theta
 =\sum_q R_D(q)R_D(Jq)=:E_\perp(D),             \tag{4.3}
\]

where `R_D(q)=|D intersect (D+q)|`.  All coefficients in (2.1) are at
least those of `1_D`, so coefficientwise convolution and Parseval imply

\[
 \int H^2H_J^2\ge E_\perp(D).                  \tag{4.4}
\]

The dense perpendicular-ruler construction in
`ORTHOGONAL_ENERGY_PRODUCT_RULER_BARRIER.md` supplies arbitrarily large
integral distance-Sidon sets with

\[
 |D|=Theta(k^2),
 \qquad
 E_\perp(D)=Omega(|D|^3)=Omega(k^6).            \tag{4.5}
\]

Thus the mixed fourth-power moment can be a full factor `k` above (4.2).
The failure is not caused by dropping radial uniqueness or by passing to an
abstract positive polynomial: it occurs for genuine complete difference
sets of genuine integral distance-Sidon configurations.

An ambient-sensitive or support-sensitive upper bound is not ruled out.
Indeed, the live inequality

\[
 E_\perp(D)\le |D|^{1+o(1)}|D+D|
\]

was designed precisely to pay for the perpendicular-ruler example.

## 5. Rotation averaging

Averaging (1.1) over the Euclidean circle `theta=rho(cos phi,sin phi)` and
using

\[
 {1\over2\pi}\int_0^{2\pi}
 e^{2\pi i\rho u_\phi\cdot d}\,d\phi
 =J_0(2\pi\rho|d|)
\]

gives (1.2).  If `n_{ab}=|a-b|^2`, these are distinct integers in
`{1,...,2m^2}`.

More generally, let `nu` be any probability measure on nonnegative
frequencies and define

\[
 K_\nu(n)=\int J_0(2\pi\rho\sqrt n)\,d\nu(\rho). \tag{5.1}
\]

Integrating (1.2) against `nu` gives the radial linear-programming
inequality

\[
 0\le k+2\sum_{\{a,b\}}K_\nu(n_{ab}).           \tag{5.2}
\]

If `K_nu(n)<=-eta` on every occupied squared radius, then (5.2) yields

\[
 k\le1+eta^{-1}.                                \tag{5.3}
\]

The issue is obtaining a negative coefficient of the required size.

## 6. Universal radial LP kernels are quantitatively blocked

Here is a sharp obstruction to choosing `nu` independently of the
configuration.

**Lemma 6.1 (full-grid obstruction).**  Suppose that

\[
 K_\nu(x^2+y^2)\le-\eta                         \tag{6.1}
\]

for every nonzero `(x,y) in {-m,...,m}^2`.  Then

\[
 \boxed{\eta\le {1\over (m+1)^2-1}.}           \tag{6.2}
\]

**Proof.**  Take the full grid `X={0,...,m}^2`, of size
`M=(m+1)^2`.  For every `rho`, positive definiteness of the Bessel kernel
(or just rotation averaging a square modulus) gives

\[
 0\le {1\over2\pi}\int_0^{2\pi}
 \left|\sum_{x\in X}e^{2\pi i\rho u_\phi\cdot x}\right|^2d\phi
 =M+2\sum_{\{x,y\}\in\binom X2}J_0(2\pi\rho|x-y|).
\]

Integrate against `nu` and apply (6.1).  This gives

\[
 0\le M-2\eta\binom M2=M-\eta M(M-1),
\]

which is (6.2).  QED.

A universal sign certificate inserted into (5.3) therefore gives at best
`k=O(m^2)`.  The lemma does not say that an adaptive kernel, negative only
on the particular radial transversal of `A`, is impossible.  It says that
such adaptivity is essential.  A one-kernel Delsarte proof which treats all
lattice radii as forbidden distances cannot see the cube-root scale.

## 7. The generic Turán packing dual is tautological here

There is also a direct obstruction to applying only the support-packing side
of the two-dimensional positive-definite Turán theory.  Suppose
`Lambda subset Z^2` has

\[
 (\Lambda-\Lambda)\cap D^*=\varnothing.         \tag{7.1}
\]

Then the translates `A+lambda`, `lambda in Lambda`, are pairwise disjoint.
Indeed, an equality `a+lambda=a'+lambda'` would put
`lambda-lambda'=a'-a` in `D`; (7.1) then forces both sides to be zero.
Consequently every upper density of `Lambda` is at most `1/k`.

The standard packing dual for a positive-definite function supported on
`D` bounds

\[
 {\sum_d h(d)\over h(0)}={k^2\over k}=k
\]

by the reciprocal density of such a packing set.  But the preceding
disjoint-translate argument says that this reciprocal is always at least
`k`.  Thus the support-packing Turán certificate is exactly tautological on
the autocorrelation support.  A useful two-dimensional semidefinite or
trigonometric-polynomial argument has to use more than a packing set
avoiding `D`.

## 8. Exponent-level scalar Bessel pseudoconfigurations

The preceding universal-kernel obstruction still permits a kernel adapted
to the occupied radii.  At the level of the scalar inequalities themselves,
however, there is a stronger barrier.

**Theorem 8.1.**  There is an absolute constant `C` such that, for every
positive integer `R`, one can find a set

\[
 S_R\subset\{1,\ldots,2R^2\},
 \qquad |S_R|={R^2\over4}+O(1),                 \tag{8.1}
\]

and an integer `K_R<=CR` for which

\[
 \boxed{K_R+2\sum_{n\in S_R}J_0(T\sqrt n/R)\ge0
        \quad\hbox{for every }T\ge0.}          \tag{8.2}
\]

Consequently `|S_R|=Theta(K_R^2)`: positivity of the scalar rotation
average, unit shell weights, distinct integral squared radii, and a
quadratic number of shells are jointly compatible with `K_R=Theta(R)`.

**Proof.**  Let `sigma` be normalized area measure on the disk of radius
`a=1/sqrt(2)`, and let `f` be the density of `|X-Y|^2` when `X,Y` are
independent with law `sigma`.  The overlap-area formula for two disks shows

\[
 \operatorname{supp}f\subset[0,2],\qquad
 0\le f\le2,\qquad \int_0^2f=1,                \tag{8.3}
\]

and `f` is decreasing, hence has total variation at most two.  Its Hankel
transform is an autocorrelation square:

\[
 \Phi(T):=\int_0^2f(x)J_0(T\sqrt x)\,dx
 =\left({2J_1(aT)\over aT}\right)^2\ge0.       \tag{8.4}
\]

Put `p_n=f(n/R^2)/4` for `1<=n<=2R^2`.  Thus `0<=p_n<=1/2`.
Use balanced rounding: if `P_N=sum_(n<=N)p_n`, set

\[
 \epsilon_n=\lfloor P_n+1/2\rfloor
              -\lfloor P_{n-1}+1/2\rfloor.     \tag{8.5}
\]

Then every `epsilon_n` is zero or one and

\[
 \left|\sum_{n\le N}(\epsilon_n-p_n)\right|\le1/2
 \quad\hbox{for every }N.                      \tag{8.6}
\]

Take `S_R={n:epsilon_n=1}`.  The bounded-variation Riemann-sum estimate,
(8.3), and (8.6) give (8.1).

We next bound the Bessel sum uniformly.  Write

\[
 \varphi_T(x)=J_0(T\sqrt x),
 \qquad
 V_T=\operatorname{Var}_{[0,2]}\varphi_T
     =\int_0^{\sqrt2T}|J_1(u)|\,du.             \tag{8.7}
\]

Summation by parts in (8.6) bounds the rounding error by
`(1+V_T)/2`.  The right Riemann-sum error for `f varphi_T`, after the
normalizing factor `1/4`, is at most

\[
 {1\over4}\operatorname{Var}(f\varphi_T)
 \le {1+V_T\over2}.                             \tag{8.8}
\]

Together with the nonnegative main term `(R^2/4)Phi(T)`, this proves

\[
 \sum_{n\in S_R}J_0(T\sqrt n/R)
 \ge-1-V_T.                                     \tag{8.9}
\]

Here (8.9) uses (8.7) with `T` replaced by the displayed dimensionless
frequency.  The standard fixed-order Bessel estimate
`|J_1(u)|<=C_1(1+u)^(-1/2)` gives

\[
 V_T\le C_2\sqrt{1+T}.                          \tag{8.10}
\]

Thus (8.9) is `>=-C_3R` for `0<=T<=R^2`.

For `T>=R^2`, use (8.6) and `p_n<=1/2`: if
`n_1<n_2<...` enumerate `S_R`, then `n_j>=2j-1`.  The standard bound
`|J_0(u)|<=C_4u^(-1/2)` and (8.1) give

\[
 \begin{split}
 \left|\sum_{n\in S_R}J_0(T\sqrt n/R)\right|
 &\le C_4\sqrt{R/T}\sum_{j\le |S_R|}n_j^{-1/4}\\
 &\le C_5{R^2\over\sqrt T}\le C_5R.            \tag{8.11}
 \end{split}
\]

Equations (8.9)--(8.11) give a uniform lower bound `-C_6R`.  Taking
`K_R=ceil(2C_6R)` proves (8.2).  QED.

The distinction from the real autocorrelation is exact and important.  In
the real problem the number of unordered shells is `K_R(K_R-1)/2`, whereas
Theorem 8.1 only gives `c K_R^2` for some unspecified absolute `c>0`.
It is therefore a decisive no-go for exponent-only manipulation of (1.2),
not a literal counterexample to all consequences of the exact
autocorrelation coefficients.

## 9. What remains genuinely open in this lane

The exact positive-definite input contains more than the scalar average:
the directions, the endpoint decoration, and the zero-one autocorrelation
factorization all disappear in (1.2).  The surviving possibilities are
therefore narrower than “apply Fourier positivity”:

1. a configuration-adaptive radial LP which uses the exact shell count
   `k(k-1)/2` (not merely `Theta(k^2)`) and the factorization constraints;
2. an ambient/support-sensitive estimate for a higher mixed moment, rather
   than the false size-only estimate (4.2);
3. a nonlinear use of the exact factorization `H=|widehat(1_A)|^2`, retaining
   the unique endpoint labels.

The general Turán theory of Kolountzakis--Révész supplies packing and
spectral estimates for positive-definite functions with prescribed support
(J. London Math. Soc. 74 (2006), 475--496,
doi:10.1112/S0024610706023234).  Its generic support bounds do not by
themselves encode the one-vector-per-norm constraint together with the
complete-difference factorization.  No primary source located in the
targeted search states the configuration-adaptive Bessel theorem required
in item 1.
