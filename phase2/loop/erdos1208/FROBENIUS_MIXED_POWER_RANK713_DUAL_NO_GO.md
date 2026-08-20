# Mixed Frobenius power caps: a rank-713 dual no-go

## 1. Verdict

The proposed arithmetic strengthening is valid, but it does **not** improve
the optimized rank-713 exponent.  If a selected Frobenius lift `g_q` is
given the relation

\[
 g_q^{2^s}=1,
\]

then that new relator has Zassenhaus degree at least `2^s`.  The weighted
Golod--Shafarevich polynomial may therefore be written

\[
 1-dt+dt^2+\sum_{s\geq1}N_st^{2^s}.               \tag{1.1}
\]

The quotient makes the residue degree at `q` divide `2^s`.  When
`q=3 mod 4`, a nonzero Frattini class keeps the order even in the finite
layers used by the construction, so `-1` remains a square in the residue
field.  These parts of the proposal are sound.

Nevertheless, using only these order caps and the Frattini parity information,
even **arbitrary** mixtures of caps `2,4,8,...` at rank 713 cannot certify an exponent

\[
 \alpha\leq 0.49458538428.                         \tag{1.2}
\]

This is just below the continuous square-cap optimum
`0.4945853842805...`; the published finite certificate rounds upward to
`0.49458539`.  Thus higher Frobenius powers cannot improve the substantive
constant.  The obstruction is residue-degree dilution, not a defect in the
weighted GS relation count.

## 2. Arithmetic interface

Let `F` be a free pro-2 group mapping onto the tame presentation and let
`x` lift `g_q`.  The Zassenhaus filtration satisfies

\[
 x^{2^s}\in F_{(2^s)}.
\]

Adjoining this word therefore contributes `t^(2^s)` to the GS polynomial.
In the quotient, the decomposition-group image of Frobenius has order
dividing `2^s`, hence every residue degree divides `2^s`.  The all-depth
comparison from `proof_frobenius_all_depth_rank713.md`, iterated, shows that
the guaranteed `k`th local increment is

\[
 g_{q,f,k}=\frac1f\log\left(
   \frac{k+1}{k}\frac{1-q^{-fk}}{1-q^{-f(k+1)}}
 \right),\qquad f=2^s.                            \tag{2.1}
\]

It decreases when `f` is replaced by `2f`.

At rank `d`, (1.1) implies, for every `0<t<1`,

\[
 N_2<\frac d t-\frac1{t^2}-d\leq\frac{d^2}{4}-d. \tag{2.2}
\]

For `d=713`, this gives the exact integer cap

\[
 N_2\leq126379.                                    \tag{2.3}
\]

At `t=2/713`, retaining all 126,379 square relators leaves enough weighted
slack for exactly 31,773 appended fourth-power relators.  The first of those
new primes is 1,685,153.  Its best fourth-power local slope is already below
the right active square-cap slope, so the direct sorted frontier ignores the
whole appended block.  The next section rules out non-prefix and traded
assignments as well.

## 3. The two-endpoint dual

For any cap assignment, let `F(L)` be its fractional local-depth frontier.
Put

\[
 \lambda=\frac{2-4\alpha}{2\alpha},\qquad
 C=\log(4D).
\]

If a dyadic interval `[w,2w]` works, with `L=2 alpha w`, then, even after
dropping the positive correction in the master inequality,

\[
 F(L)-\lambda L\geq C,qquad
 F(2L)-2\lambda L\geq C.                          \tag{3.1}
\]

For any slope `mu`, fractional knapsack duality gives

\[
 F(x)\leq \mu x+\sum_i(g_i-\mu c_i)_+,
 \qquad c_i=\log q_i.                              \tag{3.2}
\]

Use the two active square-cap slopes

\[
 \mu_1=0.0250331867794\ldots,qquad
 \mu_2=0.0158106310462\ldots                       \tag{3.3}
\]

and choose `theta=0.7950278173...` so that

\[
 \theta\mu_1+2(1-\theta)\mu_2
 =\lambda(2-\theta).                               \tag{3.4}
\]

Taking the `theta,1-theta` weighted average of (3.1), and applying (3.2),
cancels `L`.  Therefore a necessary condition is

\[
 \sum_q W_{f_q}(q)\geq C,                          \tag{3.5}
\]

where

\[
 W_f(q)=\sum_{k\geq1}\left[
 \theta(g_{q,f,k}-\mu_1\log q)_+
 +(1-\theta)(g_{q,f,k}-\mu_2\log q)_+
 \right].                                         \tag{3.6}
\]

## 4. A generous mixed-cap upper bound

Grant every useful prime a free order-four cap.  By (2.1), this also
dominates every cap `f>=8`.  Then permit at most 126,379 primes to be upgraded
from order four to order two.  This relaxation ignores *all* GS cost of the
order-four and higher relators, so it dominates every genuine mixed quotient.

The upgrade value is

\[
 \Delta(q)=W_2(q)-W_4(q).
\]

The verifier checks every prime in the finite exceptional range and finds
that `Delta(q)` strictly decreases.  Past that range `W_4(q)=0`; every
supported summand of `W_2(q)` decreases because, writing `x=log q`,

\[
 \frac{d}{dx}g_{q,2,k}
 \leq\frac1{q^2-1}<\mu_2\qquad(q\geq5419).         \tag{4.1}
\]

Thus the best 126,379 upgrades are exactly the first 126,379 useful primes.
Moreover `W_4` has already vanished before their endpoint.  The relaxed
mixed upper bound consequently collapses exactly to the pure square-cap
dual sum.  With 90-digit arithmetic,

\[
 \sum_qW_{f_q}(q)-\log(4D)
 \leq -2.52\cdot10^{-6}.                           \tag{4.2}
\]

This contradicts the necessary condition (3.5), proving (1.2).

The bound covers arbitrary placement of the caps and every local modulus
depth, not just monotone prime blocks.  It is rank-specific, and it uses only
the residue-degree guarantee supplied by the imposed order cap.  Extra
arithmetic information proving that many fourth-capped Frobenius elements
actually have order two would be a genuinely stronger input.  The theorem
also does not claim that a remote presentation rank could never support a
different mixed optimum.  Coarse sweeps of ranks 8 through 713 and explicit
shifted-block stress tests all remain weaker, but those diagnostics are not
used in the theorem.

## 5. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_frobenius_mixed_power_rank713_dual.py
```

The verifier regenerates the primes, checks the exact GS caps, recomputes
the active local slopes and dual cancellation, checks the finite upgrade
ordering, and evaluates (4.2) with 90-digit `Decimal` arithmetic.
