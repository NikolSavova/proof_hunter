# Real-cubic bounded-inertia reoptimization

## Verdict

Adding inertia-square caps to the explicit base

\[
 E=\mathbb Q(\zeta_7)^+
\]

does substantially improve the old cubic certificate, from `0.49489` to

\[
 \boxed{F_2(n)\ll n^{0.4941486}}.                 \tag{1}
\]

It still does **not** beat the rational bounded-inertia certificate
`0.493714` in `BOUNDED_TAME_INERTIA_TOWER_IMPROVEMENT.md`.  Thus the cubic
base remains a rigorous but non-record branch after the new quotient is
included.  The finite certificate is
`verify_real_cubic_bounded_inertia.py`.

## Arithmetic and relation budget

Use the arithmetic of `REAL_CUBIC_PRO2_TOWER_AUDIT.md`: `E` is totally real
of degree three and discriminant 49, has class number one and full unit
signature rank, and 2 is inert.  Ramify at all three prime ideals above each
of the first `t=98` rational primes

\[
 p\equiv\pm1\pmod 7.
\]

The last such rational prime is 2,003.  There are `3t=294` tame ramified
prime ideals, and the conservative Kummer bound gives

\[
 d\ge3t-3=291,
 \qquad r_0\le d+2.                               \tag{2}
\]

At each of the 294 prime ideals, add the square of a generator of its
procyclic tame pro-2 inertia image.  The argument of
`BOUNDED_TAME_INERTIA_TOWER_IMPROVEMENT.md` works over `E` without change:
each square lies in the Frattini subgroup, one normal relation caps all
conjugates of that prime ideal, and the local ramification index becomes at
most two.

Select the first 6,861 unramified rational primes

\[
 q\equiv1,13\pmod {28}.                            \tag{3}
\]

The last is 499,969.  Every such `q` splits into three primes of norm `q` in
`E` and is 1 modulo 4.  Add one Frobenius-square relation at each of those
three primes.  At the conservative endpoint `d=291`, the complete relation
count is

\[
 \begin{split}
 r&\le(291+2)+294+3\cdot6861=21170,\\
 4r&=84680<84681=291^2.                            \tag{4}
 \end{split}
\]

For any larger actual `d`, the gap only improves because `d^2/4-(d+2)` is
increasing here.  The quotient is therefore infinite by the ordinary strict
Golod--Shafarevich inequality, and all useful residue degrees are at most
two.

## Root discriminant and local normalization

The absolute base contribution is `rd(E)=49^(1/3)`.  Above a ramified split
rational prime `p`, each of the three order-two inertia groups contributes

\[
 (N\mathfrak p)^{(1/2)/[E:\mathbb Q]}=p^{1/6}.
\]

Their product is `p^(1/2)`.  Hence every finite layer has

\[
 \operatorname{rd}(K)
 \le49^{1/3}\prod_{p\in T_{\mathbb Q}}p^{1/2},    \tag{5}
\]

and the verifier obtains

\[
 \log D=318.767346365585728821676928645\ldots.    \tag{6}
\]

For a useful split rational `q`, the three conjugate prime-ideal local
increments again group to the single rational-scale item

\[
 \left(\log q,\frac12\log A_k(q^{-2})\right).     \tag{7}
\]

Thus the calculation includes both the factor-three relation cost and the
degree-three normalization; there is no hidden cubic amplification.

## Numerical certificate

Apply the positive-disk master inequality with the safe rational constant
`4/pi<424/333`, target

\[
 \alpha=0.4941486,\qquad w_0=52282.               \tag{8}
\]

The verifier reconstructs the cubic arithmetic, both prime lists, the exact
one-unit Golod--Shafarevich margin, the first three globally sorted depth
increments, fourth-depth exclusion, and both dyadic endpoint inequalities.
The endpoint margins are

\[
 0.0258082041\ldots,qquad0.0579164379\ldots.      \tag{9}
\]

Run

```bash
python3 phase2/loop/erdos1208/verify_real_cubic_bounded_inertia.py
```

It prints

```text
cubic bounded-inertia F_2(n) << n^0.4941486: CERTIFIED
```

The exact finite optimum was searched over the same split-rational family;
the best sampled region is near `t=98`.  This optimization claim is not
needed for (1).  Most importantly, even this favorable cubic point remains
weaker than the fully verified rational rank-221 point.
