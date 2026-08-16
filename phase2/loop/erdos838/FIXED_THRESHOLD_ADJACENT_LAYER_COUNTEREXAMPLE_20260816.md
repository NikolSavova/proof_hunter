# Fixed-threshold adjacent-layer balance is false

**Date:** 2026-08-16. All logarithms are base two. This note supersedes the
open-status conclusion, but not the exact finite calculations, in
THRESHOLD_ADJACENT_LAYER_BALANCE_GATE_20260816.md.

## Verdict

The adjacent-layer target is false even at an arbitrarily prescribed
certified Erdős--Szekeres upper sequence. More precisely, let \(j\) run
through the even integers and let

\[
 q_j\geq ES(j+1),\qquad \log q_j=j+o(j).
\]

There are rational general-position \(q_j\)-point configurations \(Q_j\)
such that

\[
 \boxed{
 \log {v_j(Q_j)\over v_{j+1}(Q_j)}
 \geq\left(1-{1\over4\ln2}-{41\over70}-o(1)\right)j^2.}
 \tag{1}
\]

The constant is positive:

\[
 1-{1\over4\ln2}-{41\over70}
 =0.053611954064\ldots .                                  \tag{2}
\]

In particular no estimate

\[
 v_j(P)\leq 2^{(\lambda+o(1))j}v_{j+1}(P)                \tag{3}
\]

holds at the fixed sizes \(q_j\), for any constant \(\lambda\). Thus the
route labelled P1e in DIFFICULTY_LEDGER_20260815.md is closed. The
counterexample does not disprove fixed-size supersaturation P1 or averaged
density decay P1d: it is a sharp obstruction only to reducing them to one
adjacent layer at an Erdős--Szekeres threshold.

The construction uses two previously verified strong-glue families. Its
new content is their coefficientwise splice at the exact prescribed size.

## 1. The rank-\(j\) core

Put \(j=2h-4\), and take the central Pascal cell

\[
                       P_j=T(j,j/2).
\]

It has

\[
 |P_j|={j\choose j/2}=2^{j-o(j)}                         \tag{4}
\]

points and maximum convex-face rank exactly \(j\). If \(a_j\) is the
number of maximum caps in the left child at the top split, the exact graded
strong-glue recurrence gives

\[
                         v_j(P_j)=a_j^2.                  \tag{5}
\]

The central-Pascal path estimate in agent_asymptotic/DERIVATION.md gives,
with

\[
                  \beta=1-{1\over4\ln2},                 \tag{6}
\]

the two estimates

\[
 \log v_j(P_j)=\beta j^2+O(j\log j),\qquad
 \log C(P_j)={\beta\over2}j^2+O(j\log j).                \tag{7}
\]

Here \(C\) denotes the total nonempty cap count in the chosen chart. The
first equality is not a total-face estimate: it is the exact top-rank
layer (5).

## 2. A skew low-face padding tower

Let \(S\) be the first \(2^{35}\) leaves of the Pascal cell \(T(41,27)\),
with the unused suffix deleted and unary nodes suppressed. Let \(X_t\) be
its \(t\)-fold homogeneous leaf substitution. The exact strong-glue
recurrences give

\[
\begin{aligned}
 |X_t|&=2^{35t},\\
 \log U(X_t)&={14\over70}(\log|X_t|)^2+O(\log|X_t|),\\
 \log V(X_t)&={41\over70}(\log|X_t|)^2+O(\log|X_t|).
\end{aligned}                                             \tag{8}
\]

These are the exact integer recurrences audited in
agent_asymptotic/capped_e_counterexample.py and
agent_killsearch/QUADRATIC_PROFILE.md.

Let

\[
                         D_j=q_j-|P_j|.                    \tag{9}
\]

The classical lower construction gives
\(ES(j+1)\geq2^{j-1}+1\), while
\({j\choose j/2}=o(2^j)\). Hence \(D_j>0\) and

\[
                         \log D_j=j+o(j).                  \tag{10}
\]

Choose \(t_j\) minimally with \(2^{35t_j}\geq D_j\), and let \(Z_j\) be
any \(D_j\)-point induced subset of \(X_{t_j}\). Heredity gives

\[
 U(Z_j)\leq U(X_{t_j}),\qquad V(Z_j)\leq V(X_{t_j}).      \tag{11}
\]

Since \(35t_j\leq\log D_j+35\), equations (8)--(11) imply

\[
\begin{aligned}
 \log U(Z_j)&\leq {1\over5}j^2+o(j^2),\\
 \log V(Z_j)&\leq {41\over70}j^2+o(j^2).
\end{aligned}                                             \tag{12}
\]

Both \(P_j\) and \(Z_j\), and their strong glue below, have rational
general-position realizations.

## 3. Exact-size splice and the layer gap

Form the separated strong glue

\[
                              Q_j=P_j\prec Z_j.            \tag{13}
\]

It has exactly \(q_j\) points. The coefficientwise face recurrence is

\[
 V_{Q_j}(z)=V_{P_j}(z)+V_{Z_j}(z)+C_{P_j}(z)U_{Z_j}(z).   \tag{14}
\]

Since \(P_j\) has maximum face rank \(j\), equations (5) and (14) give

\[
\begin{aligned}
 v_j(Q_j)&\geq a_j^2,\\
 v_{j+1}(Q_j)&\leq V(Z_j)+C(P_j)U(Z_j).
\end{aligned}                                             \tag{15}
\]

By (7) and (12), the two terms in the denominator have exponents at most

\[
 {41\over70}j^2+o(j^2),\qquad
 \left({\beta\over2}+{1\over5}\right)j^2+o(j^2).          \tag{16}
\]

The first is larger. Indeed \(\ln2<1\) gives

\[
 {\beta\over2}+{1\over5}<{3\over8}+{1\over5}
 ={23\over40}<{41\over70}.                              \tag{17}
\]

Combining (7), (15), and (16) proves (1). Positivity does not require a
decimal estimate: the elementary bound
\(\ln2>2(2-1)/(2+1)=2/3\) gives

\[
 \beta-{41\over70}>{5\over8}-{41\over70}={11\over280}>0.\tag{18}
\]

The induced-subset padding in (9)--(12) is what resolves the former
quantifier caveat. The construction works at the prescribed integer
\(q_j\), not merely at another size with the same leading logarithm.

## 4. What remains open

The counterexample has a very narrow rank cliff but still has total face
coefficient at least \(\beta>1/2\), inherited from its central Pascal core.
It therefore says nothing against the conjectured half lower bound for the
total number of convex subsets. It also does not kill an averaged
successive-density theorem on a positive fraction of ranks: the bad layer
can be isolated.

The correct conclusion is strategic. Fixed-size supersaturation cannot be
proved by demanding uniform adjacent-layer balance at a threshold size.
Any surviving P1/P1d argument must average across a genuine rank interval
or use total face mass; one exceptional promoted layer is unavoidable even
after exact-size padding.

## 5. Verification

Run:

    python3 phase2/loop/erdos838/verify_fixed_threshold_adjacent_counterexample.py

The verifier reconstructs the central-Pascal top layer and cap count, the
skew tower's exact integer state, and the strong-glue upper bound in (15).
For \(t=1,\ldots,8\) it takes the nearest even \(j\geq35t\). The exact
lower bound for \(\log_2(v_j/v_{j+1})\) becomes positive at \(t=5\) and
then grows rapidly; the last row exceeds \(1600\) bits. These finite rows
are regression checks. The asymptotic proof is equations (4)--(18).
