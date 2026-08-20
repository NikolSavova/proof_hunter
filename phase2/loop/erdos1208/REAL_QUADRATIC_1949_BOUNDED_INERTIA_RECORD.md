# A real-quadratic bounded-inertia record at discriminant 1949

## 1. Result

The finite exceptional-splitting search over real quadratic bases produces a
strict improvement.  Take

\[
 E=\mathbb Q(\sqrt{1949}).
\]

Combining an explicit tame pro-2 presentation over `E`, inertia-square caps,
the all-depth prime-ideal frontier, and product-disk packing gives

\[
 \boxed{F_2(n)\ll n^{0.49371211}}.                \tag{1.1}
\]

This is strictly better than the rational-base rank-221 exponent
`0.49371397`.  The numerical gain is small, about `1.86e-6` in the exponent,
but the endpoint margins are much larger than the numerical allowance.  The
certificate is `verify_real_quadratic_1949_bounded_inertia.py`.

The construction uses 229 ramified prime ideals, has certified generator
rank at least 227, and caps 12,425 useful prime ideals.  The last ramified
and useful ideal norms are respectively 1,303 and 136,693.

## 2. Elementary arithmetic of the base

Put

\[
 \omega={1+\sqrt{1949}\over2},\qquad
 \omega^2=\omega+487.
\]

The integer 1,949 is prime and congruent to 5 modulo 8.  Hence `E` has
discriminant 1,949 and 2 is inert and unramified.  Minkowski's bound is

\[
 {1\over2}\sqrt{1949}<23.                          \tag{2.1}
\]

The prime ideals of norm below 23 lie over 2, 3, 5, 13, and 19.  The inert
ideals `(2)` and `(3)` are principal, and

\[
 \begin{aligned}
 N(-151-7\omega)&=-5,\\
 N(43+2\omega)&=-13,\\
 N(-23+\omega)&=19.
 \end{aligned}                                    \tag{2.2}
\]

Their conjugates handle the other primes over the split rational primes.
Thus every ideal class has a principal representative and `E` has class
number one.

The unit

\[
 \varepsilon=81333+3770\omega
 ={166436+3770\sqrt{1949}\over2}                  \tag{2.3}
\]

has norm `-1`.  Consequently `-1` and `epsilon` give the full two-dimensional
unit squareclass space and have independent signature vectors.

## 3. An explicit 227-dimensional Kummer subspace

Order the odd prime ideals of `E` by norm, retaining both ideals over a
split rational prime.  Let `T` be the first 229 ideals, using the deterministic
tie order in the verifier.  The final member has norm 1,303.  Class number
one gives independent squareclass generators for the 229 prime valuations,
together with `-1` and `epsilon`, for a total of 231 columns.

Impose four linear conditions:

1. positivity at each of the two real embeddings; and
2. at the dyadic completion, congruence to a unit square modulo `4`.

The second condition is sufficient for the quadratic Kummer extension to
be unramified above 2.  Indeed, if `a congruent b^2 mod 4`, then
`(b+sqrt(a))/2` is integral at 2 and the relative discriminant is odd.

The verifier constructs the finite ring

\[
 (\mathcal O_E/4\mathcal O_E)^\times
\]

directly.  It has 12 elements; its subgroup of square residues has three
elements, so the quotient contributes two binary conditions.  The combined
two-sign/two-dyadic matrix has exact rank four.  Therefore its kernel has
dimension

\[
 229+2-4=227.                                     \tag{3.1}
\]

Every kernel class defines a totally real quadratic extension unramified
outside `T`.  Hence the maximal totally real pro-2 group `G_T`, unramified
outside `T`, has generator rank

\[
 d(G_T)\ge227.                                    \tag{3.2}
\]

Only this lower bound is used.  The standard tame totally-real
Shafarevich presentation estimate over a real quadratic base is retained as
an external input:

\[
 r(G_T)\le d(G_T)+1.                              \tag{3.3}
\]

## 4. Useful-prime test and Golod--Shafarevich budget

Add one inertia-square relation at each ideal in `T`.  Tame inertia is
procyclic, normal closure handles all primes above a fixed base ideal, and
the resulting relative ramification index is at most two.  Every new
relation is a square and therefore leaves the Frattini quotient unchanged.

Now scan odd prime ideals outside `T` by norm.  An ideal of norm `Q congruent
1 mod 4` is automatically eligible because `-1` is a square in its residue
field.  If `Q congruent 3 mod 4`, the ideal has residue degree one over a
split rational prime.  For such an ideal the verifier evaluates its quadratic
Frobenius functional on all 231 Kummer generators.  The functional is
nonzero on the 227-dimensional kernel precisely when its row is not in the
four-dimensional constraint row space.

No ideal is rejected before 12,425 useful ideals have been selected.  Add
the square of the Frobenius at each selected ideal.  The conservative
relation count at `d=227` is

\[
 \begin{aligned}
 r&\le(227+1)+229+12425=12882,\\
 4r&=51528=227^2-1<227^2.                         \tag{4.1}
 \end{aligned}
\]

For a larger actual generator rank, the Golod--Shafarevich gap only
increases.  Thus the quotient is infinite.  A selected ideal of norm 3
modulo 4 has nonzero Frattini Frobenius, so after the square cap it has exact
relative residue degree two in finite layers whose kernels retain the
Frattini quotient.  Every selected residue field therefore contains a square
root of `-1`.

## 5. Root discriminant and normalized local items

The absolute root-discriminant contribution from the base is
`sqrt(1949)`.  At a ramified prime ideal `p`, order-two relative inertia and
tame different theory contribute

\[
 (N\mathfrak p)^{(1/2)/[E:\mathbb Q]}
 =(N\mathfrak p)^{1/4}.
\]

Thus every finite layer has root discriminant at most

\[
 D_E=\sqrt{1949}\prod_{\mathfrak p\in T}
       (N\mathfrak p)^{1/4},                     \tag{5.1}
\]

and

\[
 \log D_E=
 345.9076570676278148043732942604249588957\ldots. \tag{5.2}
\]

For a useful prime ideal of norm `Q`, one all-depth marginal has normalized
cost and gain

\[
 c_{\mathfrak q,k}={\log Q\over2},\qquad
 g_{\mathfrak q,k}={1\over4}\log A_k(Q^{-2}),    \tag{5.3}
\]

where

\[
 A_k(t)={k+1\over k}{1-t^k\over1-t^{k+1}}.
\]

These are the degree-two specialization of the exact prime-ideal
normalization.  There is no factor-of-two amplification hidden in (5.3).

## 6. Disk endpoint certificate

Use the product-disk constant `4/pi`, bounded safely by `424/333`, and take

\[
 \alpha=0.49371211,\qquad w_0=44705.08.           \tag{6.1}
\]

The two dyadic endpoint margins, after subtracting `10^(-25)`, are

\[
 0.0009550783190\ldots,\qquad
 0.0019043033849\ldots.                           \tag{6.2}
\]

At the right endpoint the active local slope is

\[
 0.0189753749211\ldots,
\]

while the largest omitted fourth-depth slope is

\[
 0.0155556568713\ldots.                            \tag{6.3}
\]

The inherited per-ideal depth monotonicity excludes every later depth.
Concavity between the two endpoints, dyadic layer selection, and placewise
rounding then prove (1.1).

For the fixed anchor in (6.1), a 120-digit bisection places the first
endpoint zero at

\[
 0.49371210473886831959\ldots,                    \tag{6.4}
\]

while the second endpoint zero is
`0.49371210472541555475...`.  Thus the eight-decimal headline in (1.1)
lies safely above both numerical thresholds.  These threshold digits are a
diagnostic; the theorem uses the positive margins (6.2).

For comparison, the rational certificate has `d=221`, 222 ramified rational
primes, 11,767 useful caps, and `log D=672.4345...`.  The present field has
`d>=227`, 229 ramified ideals, 12,425 useful caps, and `log D_E=345.9077...`.
Each quadratic-base local item in (5.3) is half of the corresponding
rational item, so the smaller logarithmic discriminant is not by itself an
amplification.  The strict gain comes from the finite distribution of the
first prime-ideal norms together with the slightly larger relation budget.

Run

```text
python3 phase2/loop/erdos1208/verify_real_quadratic_1949_bounded_inertia.py
```

The verifier reconstructs the class-number-one proof, unit signatures,
prime-ideal decomposition, all 229 principal generators, the four-constraint
Kummer rank, every exceptional Frobenius test, the relation budget, root
discriminant, globally sorted frontier, omitted depths, and both endpoints.

## 7. How the field was found and scope

A diagnostic scan covered all 607 positive fundamental discriminants at
most 2,000.  It deliberately granted generator rank equal to the number of
ramified ideals, used the balanced base relation count, and treated every
earliest unramified ideal as useful.  Most small-root-discriminant fields
were already worse than the rational record in this favorable model:
`D=5,8,12,13` had old-target optimized margins approximately
`-0.75,-1.10,-1.14,-1.18`.  Exceptional early splitting, rather than small
root discriminant alone, identified `D=1949`.

Restoring a conservative two-rank-loss allowance left positive old-target
margin for discriminants 1,949, 1,397, 1,781, and 1,013 in the coarse model.
Only 1,949 is used here, and only for 1,949 are the Kummer rank, class group,
and useful-prime tests certified exactly.  The scan is a search diagnostic,
not a theorem that 1,949 is globally optimal over real quadratic fields or
arbitrary ramification sets.

For `E=Q(sqrt(1949))` itself, the honest Kummer matrix has rank four for
every tested prefix from 221 through 237 ramified ideals, and the actual
useful-prime test has zero rejections throughout.  Reoptimizing each prefix
gave the following continuous threshold diagnostic:

\[
\begin{array}{c|c|c|c}
|T|&d&\text{useful caps}&\alpha_{\rm threshold}\\ \hline
223&221&11765&0.4937122610\\
225&223&11983&0.4937121477\\
227&225&12203&0.4937121142\\
229&227&12425&0.4937121057\\
231&229&12649&0.4937121175\\
233&231&12875&0.4937121533\\
235&233&13103&0.4937122435\\
237&235&13333&0.4937123898
\end{array}                                             \tag{7.1}
\]

The finer fixed-anchor computation (6.4) confirms that 229 is the best
nearby honest prefix and motivates the safe rounded exponent in (1.1).

The declared external inputs are the number-field tame Shafarevich relation
bound, Golod--Shafarevich infinitude theorem, the prime-ideal local-depth
lemma, and the product-disk Minkowski master inequality.  The bounded-inertia
quotient and all field-specific arithmetic are checked in the artifact.
