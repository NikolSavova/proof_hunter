# Total positivity halves the ideal-packing box and improves the #1208 upper exponent

## Result

The squared algebraic distances in the prime-power construction are not
merely bounded in absolute value.  In every real embedding they are
strictly positive.  Using a one-sided ideal-packing lemma in `[0,Y]^d`
therefore replaces the factor

\[
 4+\frac{\mathcal M^2}{R^2}
 \quad\hbox{by}\quad
 2+\frac{\mathcal M^2}{R^2}                       \tag{1.1}
\]

in the non-uniform master inequality.  Applying this to the existing
rank-713 all-depth Frobenius tower gives the strict improvement

\[
 \boxed{F_2(n)\ll n^{0.49458525}}.                 \tag{1.2}
\]

This note changes neither the arithmetic tower nor the local prime-power
frontier.  It strengthens only the global ideal packing.  The exact finite
certificate is `verify_total_positive_one_sided_rank713.py`.

## 1. The one-sided ideal-packing lemma

Let `K` be a totally real number field of degree `d`, let `a` be a nonzero
integral ideal, and put

\[
 \delta=N(\mathfrak a)^{1/d}.
\]

### Lemma

For every `Y>=0`,

\[
 \#\{\eta\in\mathfrak a:
       0\le\sigma_j(\eta)\le Y\ (1\le j\le d)\}
 \le \left(1+\frac{Y}{\delta}\right)^d.            \tag{2.1}
\]

### Proof

If `0 != gamma in a`, then `(gamma) subset a`, so ideal norms give

\[
 |N_{K/\mathbb Q}(\gamma)|=N((\gamma))
 \ge N(\mathfrak a)=\delta^d.                       \tag{2.2}
\]

Partition each coordinate interval `[0,Y]` into the cells
`[j delta,(j+1)delta)` below the final cell and
`[floor(Y/delta)delta,Y]` as the final cell.  There are
`floor(Y/delta)+1 <= 1+Y/delta` cells; if `Y/delta` is an integer, the final
cell is a singleton.  If two embedded ideal points lay in the same product
cell, their nonzero difference `gamma` would satisfy

\[
 |\sigma_j(\gamma)|<\delta\qquad(1\le j\le d),
\]

and hence

\[
 |N_{K/\mathbb Q}(\gamma)|
 =\prod_j|\sigma_j(\gamma)|<\delta^d,
\]

contradicting (2.2).  Thus every product cell contains at most one ideal
point, proving (2.1).  Boundary points cause no loss: the displayed
partition ensures strict coordinate differences within every nonsingleton
cell.  `QED`

For comparison, applying the same argument to the symmetric box `[-Y,Y]^d`
uses intervals of total length `2Y` and gives

\[
 \left(1+\frac{2Y}{\delta}\right)^d.                \tag{2.3}
\]

Thus (2.1) is exactly the claimed factor-two saving; it is not a change in
the normalization of `Y`.

## 2. Why every squared distance lies in the positive box

Let `B subset O_K` lie in a translate of a Minkowski box of side `R`, and
let `A subset B^2`.  For an ordered pair of distinct points of `A`, write
its coordinate difference as `(u,v)` and define

\[
 \eta=u^2+v^2.
\]

For every real embedding `sigma_j`, the side-length convention gives

\[
 |\sigma_j(u)|\le R,
 \qquad |\sigma_j(v)|\le R.
\]

Consequently

\[
 0<\sigma_j(\eta)
   =\sigma_j(u)^2+\sigma_j(v)^2
 \le2R^2.                                           \tag{3.1}
\]

The lower inequality is strict.  If one real embedding made both terms
zero, injectivity of that field embedding would give `u=v=0`, contrary to
the two points being distinct.  Total reality is load-bearing here: it turns
every conjugate of `eta` into a sum of two real squares.

The divisor switch in the existing proof counts these actual values of
`eta`.  Hence for every integral ideal `a` appearing there, it is legitimate
to use

\[
 \mathfrak a\cap[0,2R^2]^d                         \tag{3.2}
\]

rather than the symmetric relaxation
`a intersect [-2R^2,2R^2]^d`.  No sign is lost when `eta` is placed in the
larger divisibility ideal, because ideal membership does not change its
real conjugates.

## 3. Improved non-uniform master inequality

Retain the notation of `proof_placewise_depths.md`:

\[
 \mathfrak M=\prod_{i,j}\mathfrak p_{i,j}^{K_{i,j}},
 \qquad \mathcal M=N(\mathfrak M)^{1/d},
\]

and let `H` and `Lambda` be its pattern count and divisor sum.  For
`b | M`, put

\[
 x=N(\mathfrak b)^{1/d}.
\]

Then `x<=M`, and the shortest-vector scale for `M b` is

\[
 N(\mathfrak M\mathfrak b)^{1/d}=\mathcal Mx.
\]

Apply (2.1) with `Y=2R^2`:

\[
\begin{aligned}
 |\mathfrak M\mathfrak b\cap[0,2R^2]^d|
 &\le\left(1+\frac{2R^2}{\mathcal Mx}\right)^d\\
 &=\left[\frac{R^2}{\mathcal Mx}
     \left(2+\frac{\mathcal Mx}{R^2}\right)\right]^d\\
 &\le\left[\frac{R^2}{\mathcal Mx}
     \left(2+\frac{\mathcal M^2}{R^2}\right)\right]^d.
                                                               \tag{4.1}
\end{aligned}
\]

The last inequality has the correct direction because `x<=M`.  Summing
(4.1) and using

\[
 \sum_{\mathfrak b\mid\mathfrak M}\frac1{N(\mathfrak b)}
 =\Lambda                                             \tag{4.2}
\]

gives

\[
 2\sum_{\mathfrak b\mid\mathfrak M}
 |\mathfrak M\mathfrak b\cap[0,2R^2]^d|
 \le2\left[
 \frac{R^2\Lambda^{1/d}}{\mathcal M}
 \left(2+\frac{\mathcal M^2}{R^2}\right)
 \right]^d.                                         \tag{4.3}
\]

The leading `2` remains: it is the two orientations of the unique unordered
edge realizing a nonzero squared distance.  Total positivity does not remove
that orientation multiplicity.

Comparing (4.3) with the unchanged same-coset lower bound, and using
`(|A|-M^d)^2 <= |A|(|A|-M^d)` when `|A|>=M^d`, yields

\[
 \boxed{
 |A|\le \mathcal M^d+\sqrt2R^d
 \left[(\Lambda/H)^{1/d}
 \left(2+\frac{\mathcal M^2}{R^2}\right)
 \right]^{d/2}.}                                    \tag{4.4}
\]

This proves (1.1).  All square roots, powers of `d`, and orientation factors
are identical to the old master inequality.

## 4. Exponent normalization and endpoint condition

Let the tower root discriminant be at most `D`, take

\[
 R=\sqrt D\,n^{1/(2d)},
 \qquad w=\frac{\log n}{2d},
\]

and put

\[
 L=\log\mathcal M,
 \quad
 G=\frac1d\log\frac H\Lambda,
 \quad
 z=\frac{\mathcal M^2}{R^2}
   =\frac{e^{2(L-w)}}D.                              \tag{5.1}
\]

Equation (4.4) becomes

\[
 |A|\le n^{E_1}+\sqrt2n^{E_2},
\]

where

\[
 E_1=\frac L{2w},
 \qquad
 E_2=\frac12+
 \frac{\log D-G+\log(2+z)}{4w}.                    \tag{5.2}
\]

On the globally sorted local-depth frontier, choose `L=2 alpha w`.  If
`F(L)` denotes the guaranteed value of `G`, both terms are at most
`n^alpha` provided

\[
 F(2\alpha w)\ge
 \log(2D)+(2-4\alpha)w+
 \log\left(1+
 \frac{e^{2(2\alpha-1)w}}{2D}\right).              \tag{5.3}
\]

Indeed,

\[
 \log D+\log(2+z)
 =\log(2D)+\log(1+z/2),                             \tag{5.4}
\]

which verifies both the factor `2D` and the denominator `2D` in (5.3).
The exponent `2(2alpha-1)w` is negative because `alpha<1/2`; no sign is
reversed in (5.3).

The sorted frontier `F` is concave.  The final logarithm on the right of
(5.3) is convex in `w`, while the remaining term is affine.  Therefore the
margin is concave on the full dyadic phase interval, and checking its two
endpoints remains sufficient.

## 5. Rank-713 finite certificate

Use exactly the arithmetic data of
`proof_frobenius_all_depth_rank713.md`:

\[
 d_{\rm gen}=713,
 \qquad N_{\rm useful}=126379,
 \qquad 4(713+126379)=713^2-1.                      \tag{6.1}
\]

The ramified and final useful primes remain `5417` and `1685119`, and

\[
 \log D=
 5304.6399570964594595269993248943299977668422\ldots .
                                                               \tag{6.2}
\]

Set

\[
 \alpha=0.49458525,
 \qquad w_0=1034277.                                \tag{6.3}
\]

The verifier evaluates (5.3) at `w_0` and `2w_0`.  After subtracting a
numerical allowance of `10^-25`, the margins are

\[
 0.0126543362360\ldots,
 \qquad
 0.0310022342030\ldots .                            \tag{6.4}
\]

The right endpoint contains

\[
 126379\text{ first increments},\quad
 30837\text{ second increments},\quad
 396\text{ third increments},                      \tag{6.5}
\]

followed by one fractional second increment.  Its active slope is

\[
 0.0158107974708\ldots,
\]

whereas the largest omitted fourth-depth slope is

\[
 0.0129769833101\ldots .                            \tag{6.6}
\]

Since later marginal gains decrease, no omitted depth can improve the
frontier on this phase interval.  The fixed positive margins absorb the
`O(1/[K:Q])` placewise rounding error along the tower.  This proves (1.2).

Run

```bash
python3 phase2/loop/erdos1208/verify_total_positive_one_sided_rank713.py
```

The verifier regenerates the prime sets, the rank-713 square-class basis,
every useful-prime Legendre condition, the strict integer
Golod--Shafarevich budget, the prefix-compatible all-depth frontier, the
fourth-depth exclusion, the direct-versus-factored form of (5.3), and the
two endpoint margins.

## 6. Scope

The proof retains the two declared external inputs of the earlier upper
bound: the tame totally real Shafarevich presentation theorem and the
non-uniform prime-power construction.  The new ingredient—the one-sided
packing lemma and its insertion into the master inequality—is elementary
and proved above.

The numerical improvement is small but strict:

\[
 0.49458525<0.49458539.
\]

It does not resolve Erdős #1208; it advances the certified upper frontier.
