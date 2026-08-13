# Capped endpoint-caterpillar Bellman: exact failure and the needed credit

All logarithms are base two. This note records a false global comparison, a
clean universal substitute, and an exact counterexample to the proposed
capped local Bellman inequality. The counterexample identifies what a future
amortized proof must retain.

## 1. Two exact facts about `E`

Let `E(T)` count nonempty endpoint-rooted induced caterpillars. For
`T=A prec B`, `a=|A|`, `b=|B|`,

\[
 E_T=(b+1)E_A+(a+1)E_B-ab.                        \tag{1}
\]

The global comparison

\[
 \log E_T\le\log W_T+O(\log n\log\log n)          \tag{2}
\]

is false. The explicit alternating-caterpillar family and exact formulas
are in `E_VS_W_COUNTEREXAMPLE.md`; it has `log E=n+o(1)` and
`log W=n/2+O(1)`.

There is nevertheless a sharp elementary power comparison:

\[
 \boxed{E(T)\le C(T)U(T)\le W(T)^2.}               \tag{3}
\]

For the first inequality, induct on the tree. Using (1) and the child
inequalities, it is enough to compare

\[
 (b+1)C_AU_A+(a+1)C_BU_B-ab
\]

with the exact expansion

\[
 C_TU_T=(b+1)C_AU_A+(a+1)C_BU_B+C_BU_A
              +(a+1)(b+1)C_AU_B.                 \tag{4}
\]

The latter is larger. Every cap and cup is convex, so
`W>=max(C,U)` and the second inequality follows. The alternating
caterpillar has `log W/log E -> 1/2`, so the exponent in (3) is best
possible.

## 2. The proposed hard cap

Put `L_n=log n`, and for a fixed constant `K` define

\[
 F_K(n,E)=\min\{\log E,{1\over2}L_n^2\}
             -K L_n\log\max\{2,L_n\}.             \tag{5}
\]

The endpoint-caterpillar lemma gives

\[
 \log E(T)\ge {1\over2}L_n^2-O(L_n\log L_n).       \tag{6}
\]

Thus the local Bellman inequality

\[
 \log\left(2^{F_K(a,E_A)}+2^{F_K(b,E_B)}+C_AU_B\right)
 \stackrel?\ge F_K(a+b,E_T)                        \tag{7}
\]

would imply the desired tree theorem by induction. It is false for every
fixed `K`.

## 3. Exact asymptotic counterexample to (7)

Let `S` be the first `2^35` leaves of the Pascal cell `T(41,27)`, and let
`X_t` be its `t`-fold homogeneous leaf substitution. Put

\[
 N=|X_t|=2^{35t},\qquad L=\log N=35t.              \tag{8}
\]

The cap and cup substitution degrees of `S` are respectively 27 and 14.
Its longest endpoint-rooted caterpillar has 41 macro leaves, so the
endpoint-caterpillar multiplier has degree 40. Standard leading-degree
unrolling, or direct iteration of the exact recurrence, gives

\[
\begin{aligned}
 \log C(X_t)&=\left({27\over70}+o(1)\right)L^2,\\
 \log U(X_t)&=\left({14\over70}+o(1)\right)L^2,\\
 \log E(X_t)&=\left({40\over70}+o(1)\right)L^2.
                                                               \tag{9}
\end{aligned}
\]

In particular `E(X_t)` is above the cap in (5). Now take the anti-aligned
parent

\[
 Y_t=\overline{X_t}\prec X_t.                     \tag{10}
\]

Both children have capped value

\[
 F_K(N,E(X_t))={1\over2}L^2-KL\log L.             \tag{11}
\]

The forward product visible to `W` is

\[
 C(\overline{X_t})U(X_t)=U(X_t)^2,
 \qquad \log U(X_t)^2=\left({28\over70}+o(1)\right)L^2.
                                                               \tag{12}
\]

This is below the cap by `L^2/10`, so for every fixed `K` it is eventually
smaller than the child term (11). Equation (1) shows that `E(Y_t)` is also
above its cap. Hence the left side of (7) is

\[
 {1\over2}L^2-KL\log L+1+o(1),                    \tag{13}
\]

whereas its right side is

\[
 {1\over2}(L+1)^2-K(L+1)\log(L+1).                \tag{14}
\]

Their difference is

\[
 -L+O(K\log L),                                   \tag{15}
\]

which tends to minus infinity for every fixed `K`. Increasing the reserve
constant therefore cannot repair the hard-cap Bellman lemma.

The reproducible exact-integer artifact is `capped_e_counterexample.py`.
For `K=4`, it first reports failure at `t=11`, where `L=385`, with gap

\[
 -344.366873255\ldots\text{ bits}.                \tag{16}
\]

All counts are generated from leaves by the exact strong-glue recurrences;
floating point is used only to display logarithms.

## 4. What must be amortized

The family (10) is not remotely a counterexample to the desired theorem.
Indeed

\[
 \log W(X_t)=\left({41\over70}+o(1)\right)L^2,     \tag{17}
\]

so each child carries a surplus of `3L^2/35+o(L^2)` over the target. That
quadratic stored surplus dwarfs the `L+O(log L)` local loss in (15). The
hard cap fails precisely because it erases this credit before the
anti-aligned merge.

An amortized proof must retain surplus, but cannot retain it linearly without
bound: the alternating caterpillar has `log E=Theta(n)` and only
`log W=(1/2+o(1))log E`. A useful credit function `Xi(e,L)` should have

\[
\begin{array}{ll}
\text{(i)}&\Xi(\tfrac12L^2,L)=0,\\
\text{(ii)}&\Xi((\tfrac12+\delta)L^2,L)=\Omega_\delta(L^2),\\
\text{(iii)}&\Xi(e,L)=O(L^2)\quad(e\to\infty).
\end{array}                                        \tag{18}
\]

One natural bounded reservoir is

\[
 \Xi(e,L)=L^2\left(1-{L^2\over2e}\right)_+.       \tag{19}
\]

For the prefix-Pascal children in (9), this retains `L^2/8+o(L^2)`; for
the alternating caterpillar it remains only `O(L^2)`, harmless compared
with its `Theta(n)` convex-set count. This suggests testing a potential

\[
 {1\over2}L^2+c\,\Xi(\log E,L)-K L\log L          \tag{20}
\]

or, more safely, retaining the two-dimensional attainable region

\[
 \left(\log W-{1\over2}L^2,\;
       \log E-{1\over2}L^2\right).                \tag{21}
\]

I have not proved a Bellman property for (20). The rigorous conclusion is
that a hard cap cannot support a local induction: a proof must carry a
bounded amount of quadratic excess credit across scales.
