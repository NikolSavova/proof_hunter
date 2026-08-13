# Referee audit of NEXT_ENDPOINT_ATTACK.md

**Date:** 2026-08-13  
**Scope:** mathematical audit only; no literature or priority claims.  
**Verdict:** **PASS WITH MINOR REVISIONS.** I found no counterexample or
coefficient-level gap. Conditional only on the previously established exact
max-plus recurrences and the strong-tree cap--cup product estimate, the proof
does establish
\[
 \log_2 M(T)\ge \frac12(\log_2 n)^2-O((\log n)^{3/2})
\]
for every ordered full binary strong-decomposition tree.

The argument is unusually robust: it never needs a local Bellman inequality.
The same global value \(\mu=\log M(T)\) caps every forward product and every
subtree coordinate, so a failed cross creates a coordinate gain that survives
all intervening ancestors. The heavy-path dichotomy supplies either
\(\Theta(\sqrt L)\) nested reset opportunities at almost full scale or
\(\Theta(L^{5/2})\) same-direction comb choices.

## 1. Dependency check

Let \(S\) be an \(s\)-leaf subtree of the ambient \(n\)-leaf tree \(T\), and
write \(L=\log n\), \(\mu=\log M(T)\). The proof uses three inputs.

### 1.1 Radial endpoint bound

The earlier product theorem gives
\[
 C(S)U(S)\ge
 2^{\frac12(\log s)^2-\log s}.
\]
Since \(C(S)\le sX(S)\) and \(U(S)\le sY(S)\),
\[
 x(S)+y(S)\ge \frac12(\log s)^2-3\log s.
\]
This is exactly (3). It is weaker than the direct max-endpoint radial bound
recorded elsewhere, but sufficient.

### 1.2 Coordinate cap by the global maximum

For a fixed left endpoint, the cap family consists of its singleton plus
families indexed by the right endpoint. Since
\(c(p,q)u(p,q)\le M(S)\) and \(u(p,q)\ge1\),
\[
 X(S)\le 1+(s-1)M(S)\le sM(S).
\]
The reflected statement gives \(Y(S)\le sM(S)\). The recurrence for \(M\)
is monotone, so \(M(S)\le M(T)\), and hence
\[
 x(S),y(S)\le\mu+\log s\le\mu+L.
\]
Thus (4)--(5) are valid. The singleton term is omitted in the prose of the
draft, but the asserted inequality is still correct because of the auxiliary
convention \(M\ge1\).

### 1.3 Relation between \(W\) and \(M\)

The endpoint identity gives
\[
 M\le W\le n+\binom n2M\le 2n^2M
\]
under the convention \(M\ge1\). Consequently
\[
 \log M\ge\log W-2L-1.
\]
The pure-comb branch may therefore prove a lower bound on \(W\) and transfer
it to \(\mu\) with only \(O(L)\) loss. In the reset branch the proof already
bounds \(\mu\) directly.

## 2. Audit of the reset algebra

Assume at a selected node \(P=A\prec B\) that both children satisfy
\[
 x_A+y_A\ge F,\qquad x_B+y_B\ge F
\]
and all four coordinates are at most \(\mu+L\). Define
\[
 D=F-\mu,\qquad \ell=D-L.
\]
Then every child coordinate is at least \(\ell\): for example,
\[
 x_A\ge F-(\mu+L)=D-L.
\]
The cross term in the exact recurrence is globally capped:
\[
 x_A+y_B\le m(P)\le\mu.
\]
It follows that
\[
\begin{aligned}
 x_B
 &\ge F-y_B
 \ge F-(\mu-x_A)
 =D+x_A\ge2D-L,\\
 y_A
 &\ge F-x_A
 \ge F-(\mu-y_B)
 =D+y_B\ge2D-L.
\end{aligned}
\]
The parent inherits \(x_B\) and \(y_A\), so
\[
 x_P,y_P\ge h_0:=2D-L.
\]
There is no hidden orientation assumption here: \(x_B\) and \(y_A\) are
exactly the reverse pair inherited by the two max recurrences.

Now let a later selected ancestor have path child \(H\) and opposite child
\(Q\), with \(x_Q+y_Q\ge F\).

- If \(H\) is the left child, then the forward term gives
  \(x_H+y_Q\le\mu\). Therefore
  \[
  x_Q\ge F-y_Q\ge F-(\mu-x_H)=x_H+D.
  \]
  The parent has \(x\ge x_Q\ge x_H+D\) and \(y\ge y_H\).

- If \(H\) is the right child, the cross is \(x_Q+y_H\le\mu\), and similarly
  \(y_Q\ge y_H+D\). The parent has \(y\ge y_H+D\) and \(x\ge x_H\).

Thus a left-path attachment increases \(x\) by \(D\), a right-path
attachment increases \(y\) by \(D\), and neither ever decreases the other
coordinate. Intermediate unselected nodes cause no problem because both
coordinates are monotone.

Suppose one attachment direction occurs \(q_*\) times after the first reset.
Immediately before its \(j\)-th occurrence, the coordinate used in the
forward cross is at least \(h_0+(j-1)D\). The opposite child has the paired
coordinate at least \(\ell\). At the \(q_*\)-th occurrence,
\[
 \mu\ge h_0+(q_*-1)D+\ell=(q_*+2)D-2L.
\]
Substitution of \(D=F-\mu\) gives
\[
 \mu\ge \frac{q_*+2}{q_*+3}F-\frac{2L}{q_*+3}.
\]
All signs, gains, and the off-by-one are correct.

### Failed-cross interpretation

No extra hypothesis that a cross is “failed” is needed. Every selected
cross is at most the final maximum \(2^\mu\) tautologically. The useful
regime is \(\mu<F-L\), where \(D>L\) and hence \(\ell>0\). If instead
\(\mu\ge F-L\), the target already follows from the scale estimate for
\(F\).

## 3. Audit of the heavy-path dichotomy

Let \(v_0,\ldots,v_t\) be the path obtained by following a larger child,
with current sizes \(n_i\), discarded sibling sizes \(s_i\), and
\[
 z_i=\frac{s_i}{n_i},\qquad
 d_i=\log\frac{n_i}{n_{i+1}}=-\log(1-z_i).
\]
Stop at the first \(t\) with \(n_t<n/2^{4R}\), where
\[
 R=\lceil\sqrt L\rceil.
\]
For all sufficiently large \(L\), this stopping time exists before the path
ends because \(2^{4R}<n\). Also \(0<z_i\le1/2\), so \(d_i\le1\), and
\[
 \sum_{i<t}d_i=\log(n/n_t)>4R.
\]

Call level \(i\) large when \(z_i\ge1/L^2\). At every nonlarge level,
\[
 d_i=-\log_2(1-z_i)\le \frac{2}{L^2}
\]
for sufficiently large \(L\). If there are fewer than \(R\) large levels,
their total contribution is less than \(R\), so the number \(N_0\) of
nonlarge levels satisfies
\[
 4R<R+\frac{2N_0}{L^2},
 \qquad\text{hence}\qquad
 N_0>\frac32RL^2.
\]
The constants in (18) are therefore correct.

### 3.1 Pure-comb injection

At least \(N_0/2\) of these nonlarge levels have the same color:

- path continues into the left child and the sibling is on the right; or
- path continues into the right child and the sibling is on the left.

Fix one leaf in each sibling of the majority color and one leaf below the
stopping node. For each subset of the majority-colored levels, take the
corresponding fixed sibling leaves together with the terminal leaf.

This map from level subsets to leaf subsets is injective. Moreover, it
always produces a convex subset:

- in the first color, induction upward along the path says that a cap in
  the left path child plus at most one chosen leaf in the right sibling is a
  cap;
- in the second color, the reflected induction produces a cup.

Levels of the other color and unchosen majority levels contribute no point,
so the selected set simply remains inside the path child there. Thus all
\(2^{N_0/2}\) sets are distinct pure combs, and
\[
 \log W(T)\ge N_0/2>\frac34RL^2.
\]
Using \(W\le2n^2M\) gives
\[
 \mu>\frac34RL^2-2L-1,
\]
far stronger than the claimed \(\frac12L^2-O(L^{3/2})\).

The draft's phrase “every subset of the same-side sibling leaves” is
correct, but the two-line induction above should be inserted because this
is the only genuinely combinatorial injection in the proof.

### 3.2 Uniform heavy window

Suppose instead that at least \(R\) large levels occur before stopping.
At every such level,
\[
 n_i\ge n/2^{4R}.
\]
The followed child has size at least \(n_i/2\), and the sibling has size at
least \(n_i/L^2\). Hence their base-two log-sizes are at least
\[
 L-4R-1,\qquad L-4R-2\log L,
\]
respectively. With
\[
 \Delta=4R+2\log L+1,
\]
both are at least \(2^{L-\Delta}\) in size.

For \(L\) large enough that \(L-\Delta>3\), the function
\[
 g(u)=\frac12u^2-3u
\]
is increasing on the relevant interval. Every child of every selected
large node therefore satisfies
\[
\begin{aligned}
 x+y
 &\ge g(\log s)\\
 &\ge \frac12(L-\Delta)^2-3(L-\Delta)\\
 &\ge F:=\frac12(L-\Delta)^2-3L.
\end{aligned}
\]
This verifies the uniform \(F\) used throughout the nested reset argument.

The \(R\) chosen large nodes are nested because they all lie on the same
heavy path. Order them deepest to highest. The deepest supplies the first
reset. For each later node, its path child contains the preceding selected
node, and monotonicity carries both accumulated coordinates to that child.
Among the \(R-1\) attachment directions, the more common one occurs
\[
 q_*\ge \left\lceil\frac{R-1}{2}\right\rceil
\]
times.

## 4. Final asymptotics and quantifiers

There are two cases.

1. If \(\mu\ge F-L\), then
   \[
   \mu\ge
   \frac12L^2-L\Delta+\frac12\Delta^2-4L
   =\frac12L^2-O(L^{3/2}).
   \]

2. If \(\mu<F-L\), then \(D>L\), so the reset lemma applies. With the actual
   majority count \(q_*\),
   \[
   \mu\ge
   F-\frac{F+2L}{q_*+3}.
   \]
   Since \(q_*=\Omega(\sqrt L)\), \(\Delta=O(\sqrt L)\), and
   \(F\le L^2/2\) for sufficiently large \(L\),
   \[
   \mu\ge\frac12L^2-O(L^{3/2}).
   \]

This proves the stated asymptotic with an absolute implicit constant. All
small \(n\) can be absorbed by increasing that constant.

The draft sets \(q=\lceil(R-1)/2\rceil\) after saying that one direction
occurs “at least” \(q\) times. Formally one should call the actual count
\(q_*\), apply the reset formula to \(q_*\), and then use monotonicity of
\[
 F-\frac{F+2L}{q+3}
\]
in \(q\) (valid once \(F+2L>0\)). This is a presentation repair, not a gap.

## 5. Adversarial checklist

| Potential failure mode | Audit result |
|---|---|
| A selected cross might exceed the root maximum | Impossible: the \(M\)-recurrence is monotone and contains that cross. |
| A gain might be lost at an intermediate node | Impossible: both \(X\) and \(Y\) are child-to-parent monotone. |
| Alternating attachment sides might cancel gains | No; they increment different coordinates and preserve the other. |
| The deepest reset may have the wrong orientation | No; it produces both reverse coordinates \(x_B,y_A\), so later orientation is irrelevant. |
| Opposite-child coordinates might be too small | The radial lower bound plus \(x,y\le\mu+L\) gives the uniform floor \(\ell=D-L\). |
| Large nodes might occur at incompatible scales | No; stopping after only \(4R\) bits of loss puts every selected child in the same \(L-\Delta\) window. |
| Same-color sibling choices might not be convex | They are caps or cups by a direct upward induction through the strong glues. |
| Counting may have large fibres | The chosen leaf in each sibling identifies its level, so the \(2^k\) map is injective. |
| The majority count has an off-by-one | The \(q_*\)-th occurrence has exactly \(q_*-1\) previous gains; (12) is correct. |
| The argument silently assumes balanced children | No; only the selected sibling lower threshold and larger-child property are used. |
| \(F\) could be negative or \(L-\Delta\) invalid | Only for bounded \(L\); explicitly begin with \(L\ge L_0\), then absorb smaller trees into the \(O(\cdot)\) constant. |

## 6. Revisions recommended before promoting the theorem

1. State at the start of Section 3: “Assume \(L\ge L_0\), where \(L_0\) is
   an absolute constant such that \(2^{4R}<n\), \(L-\Delta>3\), and the
   elementary logarithmic estimates below hold. Smaller \(n\) are absorbed
   into the final constant.”
2. In (4), include the singleton explicitly:
   \(X\le1+(s-1)M\le sM\), and mention \(M(S)\le M(T)\).
3. In the pure-comb case, spell out the upward cap/cup induction and then
   write explicitly
   \(\mu\ge\log W-2L-1\).
4. Replace \(q\) by the actual majority count \(q_*\), then lower-bound it by
   \(\lceil(R-1)/2\rceil\).
5. When applying (3) at the heavy nodes, state that
   \(u\mapsto u^2/2-3u\) is increasing for \(u>3\).
6. In the final paragraph, distinguish the proved lower bound on \(M\) from
   the immediate consequence for \(W\). The present conclusion is correct,
   but one explicit sentence would prevent the direction of (6) from being
   misread.

Subject to these local clarifications, I would accept the strong-tree
matching lower theorem as proved.
