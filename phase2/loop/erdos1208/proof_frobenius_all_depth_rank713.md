# Rank-713 optimization of the quadratic-Frobenius depth envelope

## Result

Optimizing the rank as well as the globally sorted local-depth envelope in
`proof_frobenius_all_depth_rank715.md` gives the slightly stronger explicit
upper bound

\[
 \boxed{F_2(n)\ll n^{0.49458539}}.                 \tag{1}
\]

The complete finite certificate is
`verify_frobenius_all_depth_rank713.py`.  This is a strict numerical
improvement over `0.494586`, not a resolution of Erdos #1208.  The same two
declared mathematical inputs remain in force: the tame totally-real
Shafarevich presentation theorem and the non-uniform prime-power master
inequality in `proof_placewise_depths.md`.

## 1. Exact arithmetic presentation

Let `T` consist of the first 714 odd rational primes.  Positive odd
quadratic discriminants supported on `T` form a 713-dimensional vector
space over `F_2`.  An explicit basis is

* every singleton `p in T` with `p=1 mod 4`; and
* `3p` for every `p in T`, `p!=3`, with `p=3 mod 4`.

Thus the tame totally-real presentation has generator rank 713 and base
relation rank at most 713.

Select the first 126,379 unramified odd primes under the order-two
Frobenius criterion of `proof_frobenius_order_two.md`: either `q=1 mod 4`,
or `q=3 mod 4` and its Frobenius class is nonzero in the displayed Frattini
quotient.  Adjoining the Frobenius-square relators preserves the generator
rank and gives

\[
 d=713,\qquad
 r\le 713+126379=127092,
\]

with the one-unit strict Golod--Shafarevich certificate

\[
 4r=508368<508369=713^2.                            \tag{2}
\]

The last ramified and useful primes are respectively 5,417 and 1,685,119.
The verifier constructs the square-class vectors and checks their exact
`F_2`-rank, generates every prime by an exact sieve, performs every Legendre
test in the useful-prime definition, and finds no rejected `3 mod 4` prime
before the cutoff.  It also checks that the ramified and useful sets are
disjoint.

The root-discriminant bound is

\[
 D=\prod_{p\in T}p,
\]

and the exact integer product has 2,304 decimal digits.  Its certified
high-precision logarithm is

\[
 \log D=
 5304.6399570964594595269993248943299977668422347921\ldots . \tag{3}
\]

As in the rank-715 construction, quotienting by the Frobenius squares makes
every useful prime have residue degree at most two in every selected tower
layer; the nonzero Frattini classes retain exact residue degree two.

## 2. All-depth residue-degree comparison

The earlier note checked the residue-degree-one versus residue-degree-two
comparison separately through depth three.  In fact it holds at **every**
depth by one AM--GM inequality.

For `0<t<1` and `k>=1`, put

\[
 A_k(t)=\frac{k+1}{k}\frac{1-t^k}{1-t^{k+1}}.
\]

At a residue-degree-one prime the `k`th increment contributes
`log A_k(q^{-1})` per normalized unit, while the guaranteed
residue-degree-two contribution is

\[
 \Delta_q(k)=\frac12\log A_k(q^{-2}).               \tag{4}
\]

It is enough to prove `A_k(t)^2>=A_k(t^2)`.  Cancelling positive factors,
and multiplying the resulting difference by `k`, reduces it exactly to

\[
\begin{aligned}
 &1-(2k+1)t^k+(2k+1)t^{k+1}-t^{2k+1}\\
 &\qquad=(1-t)\left(\sum_{j=0}^{2k}t^j-(2k+1)t^k\right)\ge0. \tag{5}
\end{aligned}
\]

The last inequality is AM--GM, since the geometric mean of
`1,t,...,t^{2k}` is `t^k`.  Thus (4) is a valid uniform lower gain for every
depth, not only the first three.

There is also a short all-depth proof of decreasing marginal gains.  Write

\[
 b_k(t)=\frac{1+t+\cdots+t^k}{k+1}
       =\frac1{1-t}\int_t^1x^k\,dx.
\]

The moment sequence `b_k(t)` is log-convex by Cauchy--Schwarz.  Since
`A_k(t)=b_{k-1}(t)/b_k(t)`, it follows that `A_k(t)` and hence
`Delta_q(k)` decrease with `k`.  Therefore once the fourth-depth slopes lie
below the active cutoff, so do all later depths.  The verifier additionally
checks the required depth-prefix order directly for every item in the finite
frontier used here.

## 3. Globally sorted frontier and dyadic certificate

For every useful prime `q`, form the first three items

\[
 \left(\log q,\Delta_q(k)\right),\qquad k=1,2,3,
\]

and sort all `3*126379` items by decreasing gain-to-cost ratio.  The exact
depth-prefix condition makes the resulting fractional-knapsack frontier
`F(L)` realizable by the residue-degree-two placewise rounding lemma.
Moreover the verifier computes every fourth-increment slope and proves that
their maximum lies strictly below the active slope at the right endpoint.
So no omitted depth can improve this certified phase interval.

Take

\[
 \alpha=0.49458539,\qquad w_0=1034317.              \tag{6}
\]

The master inequality is valid at scale `w` if

\[
 F(2\alpha w)\ge
 \log(4D)+(2-4\alpha)w+
 \log\left(1+\frac{e^{2(2\alpha-1)w}}{4D}\right).   \tag{7}
\]

The difference between the two sides is concave, so it is enough to check
`w_0` and `2w_0`.  With 90-digit Decimal arithmetic and after subtracting a
numerical allowance of `10^{-25}`, the certified margins are

\[
 0.03009888659436\ldots,
 \qquad
 0.02388656735046\ldots .                           \tag{8}
\]

The left endpoint uses 79,947 full first increments and a fractional first
increment.  At the right endpoint the full-item profile is

\[
 126379\text{ first},\qquad 30843\text{ second},
 \qquad396\text{ third},                            \tag{9}
\]

followed by one fractional second increment.  The right active slope is

\[
 0.01581063104625\ldots,
\]

whereas the maximum fourth-increment slope is only

\[
 0.01297698331012\ldots .                           \tag{10}
\]

For sufficiently large `n`, choose the usual degree-`2^j` layer with

\[
 w=\frac{\log n}{2[K:\mathbb Q]}\in[w_0,2w_0).
\]

The positive fixed margins absorb the `O(1/[K:Q])` placewise rounding loss.
Equation (7) and the non-uniform master inequality give (1), with the finite
initial range absorbed into the implied constant.

## 4. What increasing the rank does

Rank growth is beneficial only in a finite window for this construction.
The exact GS allowance grows quadratically,

\[
 N_r=\left\lfloor\frac{r^2-1}{4}\right\rfloor-r,
\]

so the optimized exponent improves from rank 400 toward the low 700s.
A floating-point scan of the same exact discrete frontier gives the following
diagnostic values (the theorem above does not rely on their last digits):

| rank | relaxed balanced exponent |
|---:|---:|
| 400 | 0.4946536034 |
| 600 | 0.4945913104 |
| 675 | 0.4945859798 |
| 700 | 0.4945854501 |
| 713 | **0.4945853843** |
| 715 | 0.4945853856 |
| 725 | 0.4945854354 |
| 800 | 0.4945878486 |
| 1000 | 0.4946062984 |

There is also a rigorous asymptotic obstruction.  Let `p_{r+2}` be the
smallest odd prime not in the prefix ramification set.  Every useful prime
has `q>=p_{r+2}`, while every guaranteed residue-degree-two increment obeys

\[
 \Delta_q(k)\le\frac12\log2.
\]

Hence every frontier slope is at most

\[
 c_r=\frac{\log2}{2\log p_{r+2}},
 \qquad F(L)\le c_rL.                               \tag{11}
\]

If (7) holds at any positive scale, dropping its positive constant terms and
using `L=2alpha w` gives the necessary condition

\[
 2\alpha c_r\ge2-4\alpha,
 \qquad
 \alpha\ge
 \frac{2}{4+\log2/\log p_{r+2}}.                  \tag{12}
\]

The right side tends to `1/2` as `r` tends to infinity.  Thus this
worst-residue-degree-two prime-power family **must eventually worsen back
toward the square-root exponent**.  The numerical turning point near rank
713 is not an accident that can be removed by merely taking the presentation
rank larger.  A substantial further improvement requires a better local
residue-degree mechanism or a different arithmetic quotient, not rank
growth alone.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_frobenius_all_depth_rank713.py
```

The verifier performs the arithmetic, presentation, local-frontier,
fourth-depth, and endpoint checks described above and prints
`target F_2(n) << n^0.49458539: CERTIFIED`.
