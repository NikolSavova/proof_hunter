# Erdős 838 lower-bound campaign — break_lemma (gpt-5.6-sol, effort=max, 2026-08-13 14:16)

> Target: log C + log U >= (1/2 - o(1))(log N)^2 for ARBITRARY point sets.
> With Theorem 1.1 already proved, this resolves Erdős 838 outright.

I did not find the requested counterexample. Two rigorous obstructions emerged, one of which changes the logic of the proposed campaign.

## 1. The product-refutation lane is not separate from improving \(W\)

Write
\[
C(P)=N+\sum_{p<q}c(p,q),\qquad
U(P)=N+\sum_{p<q}u(p,q).
\]
The endpoint identity gives
\[
W(P)=N+\sum_{p<q}c(p,q)u(p,q).
\]
Since all terms are positive,
\[
\boxed{\max\{C(P),U(P)\}\le W(P)
 \le N+(C(P)-N)(U(P)-N).} \tag{1}
\]
The lower inequality follows from \(c(p,q),u(p,q)\ge1\); the upper inequality is the diagonal-sum bound
\[
\sum_e c_eu_e\le \left(\sum_e c_e\right)\left(\sum_e u_e\right).
\]

Consequently, a family satisfying
\[
\log C(P)+\log U(P)
 <\left(\frac12-\delta\right)(\log N)^2
\]
would also satisfy
\[
\log W(P)
 <\left(\frac12-\delta+o(1)\right)(\log N)^2. \tag{2}
\]
Thus any requested counterexample would simultaneously improve the current coefficient-\(1/2\) upper construction for \(W\). The product lemma cannot fail while a coefficient-\(1/2\) universal lower bound for \(W\) survives.

Conversely, the proposed product lemma does **not** by itself imply the claimed coefficient-\(1/2\) lower bound for \(W\). Indeed, from the other side of (1),
\[
\log W(P)\ge \max\{\log C(P),\log U(P)\}
\ge \frac12\bigl(\log C(P)+\log U(P)\bigr).
\]
Therefore the target would give only
\[
\log W(P)\ge
\left(\frac14-o(1)\right)(\log N)^2. \tag{3}
\]
The displayed inequalities from Section 5 similarly yield
\[
CU\le N^4M^2\le N^4W^2,
\]
and hence again only coefficient \(1/4\), not \(1/2\).

This factor-of-two loss is genuine at the level of endpoint arrays. For example, if cap mass \(H\) is concentrated at one endpoint pair and cup mass \(H\) at another, with opposite statistics equal to \(1\), then \(CU\asymp H^2\) while \(\sum_ec_eu_e\asymp H\). This is only an algebraic example, not a claim of geometric realizability, but it proves that the cited inequalities cannot perform the asserted conversion. An additional endpoint-localization theorem would be necessary.

## 2. Exact obstruction for recursively interleaved high–low sets

I tested the canonical Horton-type route. It produces far too many caps and cups.

Let
\[
H_m=\{p_0,\ldots,p_{2^m-1}\},\qquad p_i=(i,y_i),
\]
be defined recursively as follows. Starting with \(y_0=0\), put
\[
y_{2j}=\varepsilon_m y_j,\qquad
y_{2j+1}=1+\varepsilon_m y_j,\qquad
\varepsilon_m=2^{-m-4}.
\]
These are exact dyadic rational coordinates.

Inductively \(0\le y_j<2\). A line through two odd-indexed points has height at least \(1-\varepsilon_m2^m>15/16\) throughout the relevant \(x\)-range, whereas every even-indexed point has height at most \(2\varepsilon_m\le1/16\). Similarly, every line through two even-indexed points lies below every odd-indexed point. Thus the odd subsequence is high above the even subsequence, and both induced parity subsequences are affine copies of \(H_{m-1}\). This also proves general position inductively.

For a mixed increasing triple, writing \(E\) for even/low and \(O\) for odd/high:

* with two \(E\)'s and one \(O\), the sign is \(+\) exactly when \(O\) is an endpoint;
* with two \(O\)'s and one \(E\), the sign is \(+\) exactly when \(E\) is the middle point.

This gives explicit large families of distinct cups and caps.

### Cups

Let \(\nu_2\) be the \(2\)-adic valuation. Choose integers
\[
h_0>h_1>\cdots>h_{r-1}>0,
\qquad \nu_2(h_j)=j.
\]
Then
\[
\{p_0,p_{h_{r-1}},\ldots,p_{h_0}\}
\]
is a cup. Indeed, \(h_0\) is the unique odd index and is the rightmost selected point; after deleting it and dividing all remaining indices by \(2\), the same assertion recurs.

### Caps

Choose
\[
g_0<g_1<\cdots<g_{r-1}<2^m-1,
\qquad \nu_2(g_j+1)=j.
\]
Then
\[
\{p_{g_0},\ldots,p_{g_{r-1}},p_{2^m-1}\}
\]
is a cap. Here \(g_0\) is the unique even index and is leftmost; after deleting it and mapping each odd index \(i\) to \((i-1)/2\), the assertion recurs.

Take
\[
r=m-\lceil2\log m\rceil-5.
\]
Partition \(\{1,\ldots,2^m-2\}\) into \(r\) ordered intervals of common length
\[
D\ge \frac{2^m}{2r}.
\]
Each interval contains at least \(D/2^{j+2}\) integers satisfying either
\(\nu_2(n)=j\) or \(\nu_2(n+1)=j\). Assigning the intervals in reverse order for cups and forward order for caps gives
\[
C(H_m),U(H_m)
 \ge \prod_{j=0}^{r-1}\frac{D}{2^{j+2}}.
\]
Consequently,
\[
\log C(H_m),\log U(H_m)
 \ge r\log D-\frac{r(r-1)}2-2r
 =\frac12m^2-O(m\log m).
\]
Since \(m=\log|H_m|\),
\[
\boxed{\log C(H_m)+\log U(H_m)
 \ge (\log|H_m|)^2-O(\log|H_m|\log\log|H_m|).} \tag{4}
\]
Thus this standard interleaved Horton family has normalized cap–cup product coefficient at least \(1\), twice the proposed threshold.

The robust feature is the multiplicity of nested endpoint choices: although the constructed caps and cups have only \(O(\log N)\) points, at level \(j\) there are roughly \(2^{m-j}/m\) choices for the new endpoint. Multiplying these choices over the levels produces \(2^{m^2/2-O(m\log m)}\) chains of each sign.

## 3. Precise point where interleaving might still help

For a general two-layer configuration \(P=A\cup B\), with \(B\) high above \(A\) but with arbitrary interleaving in \(x\), define for \(S\subseteq A\)
\[
\ell_B(S)=|\{b\in B:b<\min S\}|,\qquad
r_B(S)=|\{b\in B:b>\max S\}|.
\]
The mixed-sign rules give the exact formula
\[
U(P)=U(A)+U(B)+
 \sum_{S\in\mathcal U(A)}
 \bigl((\ell_B(S)+1)(r_B(S)+1)-1\bigr), \tag{5}
\]
and symmetrically
\[
C(P)=C(A)+C(B)+
 \sum_{T\in\mathcal C(B)}
 \bigl((\ell_A(T)+1)(r_A(T)+1)-1\bigr). \tag{6}
\]
A mixed cup consists of a cup in the low layer together with at most one high point on each side; a mixed cap is the reflected statement.

Equations (5)–(6) identify the possible attack: arrange most cups of \(A\) to span nearly all of \(B\), while simultaneously arranging most caps of \(B\) to span nearly all of \(A\). The attempt dies because nesting that suppresses one sum creates endpoint choices in the opposite sum. I could not turn this compensation into a universal inequality, but the Horton calculation shows that straightforward recursive interleaving makes the compensation much stronger, not weaker.

**VERDICT: PARTIAL (no counterexample).** Any counterexample to the proposed cap–cup product lemma would automatically be a coefficient-below-\(1/2\) construction for \(W(P)\); meanwhile the proposed lemma itself would imply only the existing coefficient-\(1/4\) lower bound for \(W\). Moreover, the exact rational Horton family above satisfies
\[
\log C(H_m)+\log U(H_m)\ge(\log|H_m|)^2-O(\log|H_m|\log\log|H_m|),
\]
so recursive high–low interleaving is obstructed by multiscale endpoint multiplicity.