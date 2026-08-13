# Erdős 838: the proposed tree potential is false

**Date:** 2026-08-13. All logarithms are base (2). Counts (C,U,W)
exclude the empty set.

## Result

The proposed strong-glue invariant

\[
H(T):=W(T)\sqrt{\frac{\min(C(T),U(T))}{\max(C(T),U(T))}}
\stackrel{?}{\ge}2^{\frac12(\log |T|)^2}                 \tag{1}
\]

is false. There is an explicit recursively specified tree on

\[
n=2^{455}
\]

leaves for which the reverse strict inequality holds. The construction and
comparison use only the exact integer recurrences

\[
\begin{aligned}
C(A\prec B)&=C(B)+(|B|+1)C(A),\\
U(A\prec B)&=U(A)+(|A|+1)U(B),\\
W(A\prec B)&=W(A)+W(B)+C(A)U(B).                 \tag{2}
\end{aligned}
\]

The reproducible certificate is
[tree_potential_adversary.py](/Users/sihaohuang/Desktop/Coding/proof_hunter/phase2/loop/erdos838/agent_killsearch/tree_potential_adversary.py).
Run

```bash
python3 phase2/loop/erdos838/agent_killsearch/tree_potential_adversary.py \
  --scan-asymptotic --exhaustive 13
```

from the repository root. Runtime was about (2.3) seconds on the current
machine.

## 1. Exact power-of-two counterexample

Let (T_{m,i}) be the Pascal strong-decomposition cell

\[
T_{m,i}=T_{m-1,i-1}\prec T_{m-1,i},\qquad
|T_{m,i}|={m\choose i},                           \tag{3}
\]

with singleton boundary cells. Take the first (2^{35}) leaves, in their
ordered leaf order, of (T_{41,27}), delete the remaining suffix, and
suppress unary vertices. Call the resulting ordered full binary template
(S). This is again a valid strong-decomposition tree.

The cap and cup substitution polynomials of (S) have respective degrees

\[
p=27,\qquad q=14.                                 \tag{4}
\]

This follows exactly from the compressed prefix recursion in the artifact.
At a binary node the degree pair obeys

\[
p(T)=\max(p(B),p(A)+1),\qquad
q(T)=\max(q(A),q(B)+1),                           \tag{5}
\]

and a unary node created by deletion is suppressed. The script asserts
((p,q)=(27,14)).

Starting with a singleton (Q_0), substitute (Q_{t-1}) for every leaf of
(S) to obtain (Q_t). Thus

\[
|Q_t|=(2^{35})^t=2^{35t}.                         \tag{6}

The artifact evaluates every occurrence of (2) with Python integers. At
(t=13), it obtains

\[
\begin{aligned}
\operatorname{bitlength} C(Q_{13})&=81710,\\
\operatorname{bitlength} U(Q_{13})&=42322,\\
\operatorname{bitlength} W(Q_{13})&=123123,
\end{aligned}
\]

with (C>U). Because (log |Q_{13}|=455), squaring (1) would require the
exact integer inequality

\[
W(Q_{13})^2U(Q_{13})
\ge C(Q_{13}),2^{455^2}.                         \tag{7}
\]

Instead, the bit lengths of the two sides of (7) are respectively

\[
288566<288735.                                    \tag{8}
\]

This alone is an exact certificate of strict failure; floating-point logs
are not used. For reproducibility, the SHA-256 prefixes of the two exact
integers are respectively

```text
4559e78a9047b0f02ace
d57706fa01c2c9ad1533
```

The first failure in this family is (t=13). At (t=12), (1) still holds.
The base-two logarithmic deficit

\[
\frac12(\log n)^2-log W+rac12|\log C-\log U|
\]

is (-27.5587\ldots) at (t=12) and (84.0844\ldots) at (t=13).

## 2. Why failure is asymptotic, and how far it goes

For any fixed (r)-leaf template whose cap and cup substitution-polynomial
degrees are (p,q), homogeneous iteration gives

\[
\begin{aligned}
\log C(Q_t)&=\frac{p\log r}{2}t^2+O(t),\\
\log U(Q_t)&=\frac{q\log r}{2}t^2+O(t),\\
\log W(Q_t)&=\frac{(p+q)\log r}{2}t^2+O(t).
                                                               \tag{9}
\end{aligned}
\]

The last line follows by taking the final cross term in (2), and the reverse
bound follows by unrolling the same recurrence. Hence, if (p\ge q),

\[
\lim_{t\to\infty}\frac{\log H(Q_t)}{(\log |Q_t|)^2}
=\frac{p+3q}{4\log r}.                            \tag{10}
\]

For the exact power-of-two template above, this is

\[
\frac{27+3\cdot14}{4\cdot35}
=\frac{69}{140}=0.492857142857\ldots<\frac12.     \tag{11}
\]

So a finite failure was unavoidable.

Full off-center Pascal cells give a stronger asymptotic obstruction. Put
(i=xmge m/2). Then

\[
r={m\choose i},\qquad p=i,qquad q=m-i,qquad
\log r=(h_2(x)+o(1))m,                            \tag{12}
\]

where (h_2) is binary entropy. Formula (10) tends to

\[
g(x)=\frac{3-2x}{4h_2(x)}.                        \tag{13}
\]

Numerical one-dimensional optimization gives

\[
\min_{1/2<x<1}g(x)
=0.453339497509\ldots
\quad\text{at}\quad x=0.682328\ldots.            \tag{14}
\]

Thus (1) is not just barely false. The proposed potential's best universal
quadratic coefficient is at most (0.45334ldots) within the classical
Pascal family. The stationary template already realizes the optimum of this
model; elaborate anti-aligned scheduling is unnecessary.

## 3. Homogeneous and nonstationary template optimization

The preceding calculation also explains why the counterexample is the
right adversarial shape. If a template has (r) leaves, cap degree (p),
and cup degree (q), the Erdős--Szekeres/Pascal bound gives

\[
r\le {p+q\choose p}.                              \tag{15}
\]

For fixed (p,q), maximizing (r) minimizes (10); asymptotically this is
attained by the Pascal cell. Optimizing the remaining ratio (p/(p+q))
is exactly (13).

The same conclusion holds for nonstationary schedules with no macroscopic
single-level jump. Suppose at level (j) the template has log-size
(ell_j) and degrees (p_j,q_j), and put
(L_j=\ell_1+\cdots+\ell_j). Leading terms satisfy

\[
\begin{aligned}
\log C&=\sum_jp_jL_{j-1}+o(L^2),\\
\log U&=\sum_jq_jL_{j-1}+o(L^2),\\
\log W&=\sum_j(p_j+q_j)L_{j-1}+o(L^2).            \tag{16}
\end{aligned}
\]

By the triangle inequality, mixing templates of opposite imbalance can only
*increase* the resulting (H) compared with charging the absolute
imbalance at each level separately. For one-sided schedules the normalized
rate is a weighted average of

\[
\frac{2(p_j+q_j)-|p_j-q_j|}{4\ell_j}.             \tag{17}
\]

It therefore cannot beat the best stationary value (14). Alternating mirror
templates resets imbalance and is favorable to (H), not adversarial.

This also proves a broader negative statement. Replacing (H) by

\[
H_\theta=W\left(\frac{\min(C,U)}{\max(C,U)}\right)^\theta
\quad(\theta>0)                                  \tag{18}
\]

cannot retain coefficient (1/2) for any fixed (	heta>0). Near
(x=1/2), the excess of (1/(2h_2(x))) above (1/2) is quadratic in
(|x-1/2|), while the penalty in (18) is linear. The original proposal is
(	heta=1/2).

## 4. A replacement profile that survives this obstruction

The failure mechanism suggests penalizing imbalance **quadratically**, not
linearly. A concrete candidate is

\[
\boxed{
\Psi(T)=\log W(T)
-\kappa\frac{(\log C(T)-\log U(T))^2}
                  {\log C(T)+\log U(T)},
\qquad \kappa=\frac1{2\ln2}.}                    \tag{19}
\]

For a homogeneous Pascal cell with bias (x), (19) has normalized rate

\[
\frac{1-\kappa(2x-1)^2}{2h_2(x)}.                \tag{20}
\]

The standard binary-entropy/Pinsker inequality

\[
h_2(x)\le1-\frac{(2x-1)^2}{2\ln2}                \tag{21}
\]

shows that (20) is at least (1/2), with asymptotic equality at the central
cell. Thus (kappa=1/(2\ln2)=0.7213475\ldots) is exactly calibrated to the
off-center Pascal obstruction.

This is only a candidate global invariant, not a proof. Its present evidence
is nevertheless materially better than that for (1):

* exhaustive enumeration of every distinct exact ((C,U,W)) triple through
  13 leaves finds no violation of
  (Psi(T)\ge\frac12(\log|T|)^2);
* its worst deficit decreases from (-1.08496\ldots) at two leaves to
  (-2.69945\ldots) at 13 leaves;
* on the exact counterexample family above, its deficit at (t=13) is
  (-10587.05\ldots), while the linear-penalty potential has already failed.

The artifact reproduces both the exhaustive test and these diagnostics.

## 5. Consequence for the proof strategy

The absolute imbalance term (|d|=\tfrac12|\log(C/U)|) cannot be used in a
sharp coefficient-(1/2) global potential. Slightly off-center Pascal trees
have only a quadratic surplus of convex-set entropy above (1/2), while
(|d|) extracts a first-order charge. This is an intrinsic asymptotic
counterexample, not a failure of a proposed one-step induction.

Any viable strengthened invariant must retain a quadratic entropy profile,
something equivalent to (19), or more detailed endpoint/path data. The
original unpenalized tree-alignment conjecture for (W) is **not** refuted:
the same off-center Pascal family has

\[
\lim\frac{\log W}{(\log n)^2}
=\frac1{2h_2(x)}>\frac12.                         \tag{22}
\]

Only the stronger (H)-invariant is killed.
