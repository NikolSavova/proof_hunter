# Gaussian-multiplier orthogonality and its sharp packing ceiling

## 1. Verdict

Let `A subset [0,m]^2` be distance-Sidon, let `k=|A|`, and put

\[
 H(\theta)=|\widehat {1_A}(\theta)|^2.
\]

The familiar quarter-turn identity `int H(theta)H(J theta)=k^2` belongs to
an exact family.  For every Gaussian integer `alpha=a+bi`, write

\[
 M_\alpha=\begin{pmatrix}a&-b\\ b&a\end{pmatrix},
 \qquad H_\alpha(\theta)=H(M_\alpha^T\theta).  \tag{1.1}
\]

If `alpha` and `beta` have the same norm and `alpha!=plus or minus beta`,
then

\[
 \boxed{\int_{\mathbb T^2}H_\alpha H_\beta=k^2.}            \tag{1.2}
\]

Thus, after quotienting the Gaussian integers of norm `n` by sign, there
are

\[
 r(n)={r_2(n)\over2}                                      \tag{1.3}
\]

pairwise orthogonal centered copies `H_alpha-k`.  All their quadratic
identities are explicit:

\[
 \boxed{
 \left\|\sum_\alpha c_\alpha(H_\alpha-k)\right\|_2^2
 =k(k-1)\sum_\alpha|c_\alpha|^2.}             \tag{1.4}
\]

The full family still gives no power improvement over the linear grid
bound.  A sharp Fourier-support/Bessel count gives

\[
 \boxed{
 r(n)k(k-1)\le
 \bigl(2\lfloor m\sqrt{2n}\rfloor+1\bigr)^2-1,}           \tag{1.5}
\]

and hence

\[
 k\ll1+m\sqrt{n/r(n)}.                         \tag{1.6}
\]

But

\[
 r(n)\le2\tau(n)=n^{o(1)},                    \tag{1.7}
\]

and even the elementary inequality `r(n)<=2n` shows that optimizing (1.6)
can never give `o(m)`.  Its best scale occurs already at `n=1`, where the
two copies are `H` and `H_J`.

This remains true in the most favorable multi-norm fantasy.  If `Gamma` is
any family of Gaussian multipliers of norm at most `N` whose transformed
nonzero Fourier supports are pairwise disjoint, then

\[
 |\Gamma|k(k-1)\ll m^2N,
 \qquad |\Gamma|\ll N.                         \tag{1.8}
\]

Even an optimally dense family `|Gamma| asymp N` yields only `k=O(m)`.
Therefore the whole **quadratic multiplier-orthogonality plus frequency
packing method** bottoms out at

\[
 \boxed{k\le m^{1+o(1)},}                     \tag{1.9}
\]

not at the desired `m^(2/3+o(1))`.

This is a scoped no-go.  It does not rule out a nonlinear theorem coupling
higher mixed moments to endpoint factorization or to ambient additive
support.  It shows that adding arbitrarily many exact rational-rotation
second-moment identities to the known quarter-turn identity supplies no
power gain by Bessel, origin localization, or raw Fourier packing.

## 2. Exact multiplier identities

Let

\[
 h=1_A\circ1_A=k\delta_0+1_{D^*},
 \qquad D^*=(A-A)\setminus\{0\}.               \tag{2.1}
\]

Distance-Sidonicity says that the nonzero coefficients are all one and
that two vectors of `D^*` have the same norm only when they are negatives
of each other.  The Fourier support of `H_alpha-k` is

\[
 M_\alpha D^*.                                 \tag{2.2}
\]

Suppose `N(alpha)=N(beta)=n` and a nonzero frequency lies in both supports:

\[
 M_\alpha d=M_\beta e,
 \qquad d,e\in D^*.                            \tag{2.3}
\]

Taking norms gives `|d|=|e|`.  Radial uniqueness forces `e=plus or minus d`.
Equation (2.3) then says

\[
 M_{\alpha-\beta}d=0
 \quad\hbox{or}\quad
 M_{\alpha+\beta}d=0.                         \tag{2.4}
\]

Multiplication by a nonzero Gaussian integer is nonsingular, so (2.4) is
impossible unless `alpha=beta` or `alpha=-beta`.  Consequently distinct
classes modulo sign have disjoint nonzero supports.

Haar orthogonality now gives, for distinct classes,

\[
 \int H_\alpha H_\beta=k^2,                  \tag{2.5}
\]

while Haar invariance under the torus endomorphism `M_alpha^T` gives

\[
 \int H_\alpha^2=2k^2-k.                     \tag{2.6}
\]

Thus `F_alpha=H_alpha-k` satisfy

\[
 \langle F_\alpha,F_\beta\rangle
 =\begin{cases}k(k-1),&\alpha=\beta\pmod{\pm1},\\
                 0,&\text{otherwise},
   \end{cases}                                  \tag{2.7}
\]

which proves (1.4).  In particular, for the unweighted sum

\[
 \boxed{
 \int\left(\sum_\alpha H_\alpha\right)^2
 =r(n)^2k^2+r(n)k(k-1).}                      \tag{2.8}
\]

There are no unaccounted quadratic correlations left to exploit.

The same argument has a direct-sum interpretation.  For distinct classes
`alpha,beta`, the map

\[
 (x,y)\longmapsto M_\alpha x+M_\beta y
\]

is injective on `A times A`.  Equation (1.2) is the Fourier form of this
directness.

## 3. Sharp Bessel and frequency-packing audit

Every `d in D^*` lies in `[-m,m]^2`.  If `N(alpha)=n`, then each coordinate
of `M_alpha d` has absolute value at most

\[
 m(|a|+|b|)\le m\sqrt{2n}.                    \tag{3.1}
\]

The `r(n)` supports in (2.2) are disjoint, each has `k(k-1)` elements, and
their union lies in the integer square from (3.1).  Counting frequencies
proves (1.5).

Equivalently, put `F=sum_alpha(H_alpha-k)`.  Its frequency support is in a
set `Omega` of size at most the right side of (1.5), while

\[
 F(0)=r(n)k(k-1),
 \qquad \|F\|_2^2=r(n)k(k-1).                 \tag{3.2}
\]

The reproducing-kernel inequality

\[
 |F(0)|^2\le|\Omega|\,\|F\|_2^2              \tag{3.3}
\]

is exactly (1.5).  This also proves sharpness within the available
quadratic data: arbitrary weights cannot improve it, because

\[
 \left|\sum c_\alpha\right|^2
 \le r(n)\sum|c_\alpha|^2.                    \tag{3.4}
\]

The arithmetic count is standard.  The two-squares formula gives

\[
 r_2(n)=4\sum_{d\mid n}\chi_{-4}(d),
\]

so `r(n)<=2 tau(n)`.  Also `tau(n)<=n`, hence `r(n)<=2n`; equality in the
ratio scale is attained at `n=1`, where `r(1)=2`.  Increasing the common
denominator can create a divisor-sized number of rational rotations, but
the common frequency square grows by the full area factor `n`.

### Origin localization is weaker

All `H_alpha` equal `k^2` at the origin.  On a square of area
`Omega(1/(m^2n))` around zero they are simultaneously at least `k^2/2`.
Combining this with (2.8) gives only

\[
 k^2\ll m^2n(1+1/r(n)),                       \tag{3.5}
\]

which loses the factor `r(n)` present in (1.5).  Thus overlapping the
common positive peaks does not unlock an extra many-rotation gain.

## 4. Even ideal cross-norm packing remains linear

The same ceiling does not depend on staying on one norm shell.  Let
`Gamma` be any finite family of nonzero Gaussian integers, modulo sign,
such that

\[
 M_\alpha D^*\cap M_\beta D^*=\varnothing
 \quad(\alpha\ne\beta),                       \tag{4.1}
\]

and suppose `N(alpha)<=N` throughout.  Every transformed support lies in
the integer square of radius `m sqrt(2N)`.  Therefore

\[
 |\Gamma|k(k-1)\ll m^2N.                      \tag{4.2}
\]

On the other hand the number of Gaussian integers in the disk
`a^2+b^2<=N`, modulo sign, is `O(N)`.  Hence no multiplier selection can
have `|Gamma|` larger than the denominator-area resource `N`.  Even granting
the best possible disjointness across all norm shells, (4.2) stops at a
linear bound.

For unequal norms, (4.1) is not automatic: a collision can occur when a
ratio of multiplier norms equals a ratio of two occupied squared radii.
That only reduces the available family.  The idealized calculation above
therefore gives the most favorable possible packing outcome.

## 5. Exact finite audit

The verifier checks the identities on a genuine 20-point distance-Sidon
closure.  For common norms

\[
 n=1,5,25,65,325,1105,
\]

the numbers of multiplier classes are respectively

\[
 r(n)=2,4,6,8,12,16.                           \tag{5.1}
\]

In every row it verifies:

1. every transformed nonzero support has `k(k-1)` frequencies;
2. the supports are pairwise disjoint;
3. all cross moments are exactly `k^2`;
4. the summed second moment is exactly (2.8); and
5. the union obeys the sharp frequency-box count (1.5).

It also enumerates all norm shells through `n=5000` and confirms that the
minimum of `n/r(n)` is `1/2`, attained at `n=1`.  Larger highly composite
examples display the expected denominator loss:

\[
\begin{array}{c|r|c}
n&r(n)&n/r(n)\\ \hline
1105&16&69.0625\\
5525&24&230.2083\ldots\\
27625&32&863.28125\\
160225&48&3338.0208\ldots\\
801125&64&12517.5781\ldots
\end{array}                                                    \tag{5.2}
\]

Run

```text
python3 phase2/loop/erdos1208/verify_gaussian_multiplier_orthogonality_audit.py
```

for the exact certificate.

## 6. Research consequence

The multiplier identities are exact and plentiful, but not dense enough
relative to their denominator cost.  At quadratic level they do nothing
more than place disjoint copies of the nonzero difference spectrum into a
larger frequency box.  Lattice-point packing then ends at the ordinary
linear exponent.

Any useful continuation must introduce information absent from (1.2)--
(1.8): for example a higher mixed moment with an ambient-sensitive error
term, an endpoint-decorated inverse theorem, or a number-field construction
where many exact unit rotations do not pay denominator area in the chosen
embedding.  Merely adding more rational rotations to the second-moment
system cannot reach the cube-root scale.
