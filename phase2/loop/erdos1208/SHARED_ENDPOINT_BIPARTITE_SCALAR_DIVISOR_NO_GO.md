# Shared-endpoint bipartite metric amplification is divisor-limited

## 1. Outcome

The most natural attempt to violate the surviving outer-normalized gate is
to replace the large scalar star by a dense fixed-gap bipartite graph.  If
`L` arm types are all paired through the same `M` physical endpoints, the
first-edge graph is `K_(L,M)` and has

\[
 L{M\choose2}+M{L\choose2}                            \tag{1.1}
\]

endpoint wedges.  Taking `L,M=Theta(k)` would give `Theta(k^3)` scalar
wedge weight and would indeed defeat the large-star `Nk^3` equality scale.

This amplification is impossible at polynomial height in a genuine
integral distance-Sidon set.  For every nonzero scalar gap `r`,

\[
 \boxed{L\le\tau(|r|)=m^{o(1)},}                      \tag{1.2}
\]

where `tau` is the divisor function and all coordinates have magnitude at
most `m`.  Consequently every such shared-endpoint bipartite block has

\[
 \boxed{W_r^{\rm block}\le m^{o(1)}k^2.}             \tag{1.3}
\]

The classical perpendicular two-axis quadratic-gap family evades a
`k`-only version of (1.3) by taking `r` and the coordinate height
exponential in `L`.  Its factor pairs exactly saturate the mechanism in
(1.2).  Thus the exponential height in that counterexample is essential,
not an artifact of its construction.

This theorem does not settle the outer-normalized gate: an arbitrary
fixed-gap graph need not decompose efficiently into complete
shared-endpoint blocks with the same partner endpoints.  It does rule out
the most efficient known route from the sharp `Theta(k^2)` large star to a
forbidden `k^(2+epsilon)` polynomial-height scalar wedge weight.

## 2. General shared-endpoint theorem

Let `A subset Z^2` be distance-Sidon.  Fix distinct common endpoints

\[
 Y=\{y_1,\ldots,y_M\}\subset A,qquad M\ge2,           \tag{2.1}
\]

and a nonzero integer `r`.  Suppose there are `L` distinct ordered arm
pairs `(a_i,b_i)` in `A` such that, for every `i` and every `y in Y`,

\[
 |y-a_i|^2-|y-b_i|^2=r.                               \tag{2.2}
\]

Endpoints coinciding inside a displayed edge are excluded.  Then

\[
 \boxed{L\le\tau(|r|).}                               \tag{2.3}
\]

### Proof

Fix `y_1!=y_2` and subtract their two instances of (2.2).  This gives

\[
 (y_1-y_2)\mathbin\cdot(b_i-a_i)=0.                   \tag{2.4}
\]

Write `v=(y_2-y_1)/g`, where `g` is the gcd of the two coordinates, and
let

\[
 n=(v_2,-v_1)                                         \tag{2.5}
\]

be the primitive integral normal.  Every integral vector perpendicular to
`v` is an integral multiple of `n`, so

\[
 b_i-a_i=t_i n,qquad t_i\in\mathbb Z\setminus\{0\}. \tag{2.6}
\]

Using one endpoint `y in Y`, factor the gap as

\[
\begin{aligned}
 r
 &=|y-a_i|^2-|y-b_i|^2\\
 &=(b_i-a_i)\mathbin\cdot(2y-a_i-b_i)\\
 &=t_i\,[n\mathbin\cdot(2y-a_i-b_i)].                \tag{2.7}
\end{aligned}
\]

The bracket is an integer.  Hence `t_i` divides `r`.

If `|t_i|=|t_j|`, then

\[
 |a_i-b_i|^2=t_i^2|n|^2=t_j^2|n|^2=|a_j-b_j|^2.      \tag{2.8}
\]

Distance-Sidonicity forces the two unordered arm edges to be identical.
The reverse orientation changes the sign of (2.2), so it cannot produce a
second arm at the same nonzero `r`.  Thus the positive integers `|t_i|`
are distinct divisors of `|r|`, proving (2.3).

If `Y` contains three noncollinear points, (2.4) already forces
`b_i=a_i`, impossible for `r!=0`.  Hence every nontrivial block is
automatically supported on a line, with its arm differences normal to that
line; no axis assumption was used in the proof.

## 3. Polynomial-height consequence

If every coordinate of `A` has magnitude at most `m`, then every squared
distance is `O(m^2)`, so

\[
 0<|r|=O(m^2).                                        \tag{3.1}
\]

The standard divisor bound gives

\[
 \tau(|r|)=\exp\left(O\left({\log m\over\log\log m}\right)\right)
 =m^{o(1)}.                                           \tag{3.2}
\]

The determinant-qualified first edges `(a_i,y)`, if all present, form the
complete bipartite graph with parts `{a_i}` and `Y`.  Its endpoint-wedge
weight is exactly (1.1).  Since `L<=m^(o(1))` and `L,M<=k`,

\[
\begin{aligned}
 L{M\choose2}+M{L\choose2}
 &\le {1\over2}(LM^2+ML^2)\\
 &\le m^{o(1)}k^2,                                   \tag{3.3}
\end{aligned}
\]

which proves (1.3).  Discarding edges which fail the determinant cutoff
only decreases the left side.

The same proof permits translated or oblique common lines and arbitrary
integral arm locations.  Its two essential hypotheses are literal reuse
of the same endpoint set `Y` and the same arm pairing `(a_i,b_i)` across
that set.

## 4. Exact equality-model audit

The perpendicular quadratic-gap family takes

\[
 r=B^{2L+1},qquad
 a_i={B^{2L+1-i}+B^i\over2},qquad
 b_i={B^{2L+1-i}-B^i\over2}.                          \tag{4.1}
\]

Then

\[
 (a_i-b_i)(a_i+b_i)=B^iB^{2L+1-i}=r,                 \tag{4.2}
\]

so its `L` arms use `L` distinct divisors of `r`.  With `M=2L` common
vertical endpoints, the first-edge graph is `K_(L,2L)` and

\[
 W_r=L{2L\choose2}+2L{L\choose2}=3L^3-2L^2.          \tag{4.3}
\]

This is `Theta(k^3)` for `k=4L`, but

\[
 \tau(r)=2L+2,qquad m=B^{\Theta(L)}.                 \tag{4.4}
\]

Thus `L=O(log m)=m^(o(1))`, exactly consistent with (1.2)--(1.3).  A
polynomial-height realization with `L=k^epsilon` would contradict the
divisor bound.

## 5. Verification

The verifier reconstructs the exact distance-Sidon families for
`L=2,4,8`, checks every common-endpoint identity (2.2), extracts the
factorization (2.7), checks distinct absolute divisors, verifies that all
displayed edges pass the sharp determinant cutoff `N`, and recomputes the
complete bipartite wedge weight.  The profiles are

\[
\begin{array}{c|r|r|r|r|r}
L&k&\tau(r)&R_D(r)&W_r&\min|2\det|\\ \hline
2&8&6&8&16&483,160\\
4&16&10&32&160&7,073,843,080\\
8&32&18&128&1,408&1,516,341,085,497,881,320.
\end{array}                                           \tag{5.1}
\]

Run

```text
PYTHONPATH=phase2/loop/erdos1208 \
python3 phase2/loop/erdos1208/verify_shared_endpoint_bipartite_scalar_divisor_no_go.py
```

## 6. Exact remaining gap

The large-star barrier shows that one centre can carry `Theta(k^2)` wedge
weight at polynomial height.  The theorem above shows that duplicating
that star across a common endpoint reservoir cannot gain a power of `k`:
each independent arm type consumes a divisor of the fixed scalar.

To close the outer-normalized gate, one now needs a global decomposition
or incidence theorem saying that scalar graphs with wedge weight much
larger than `m^(o(1))k^2` contain enough shared-partner endpoint reuse to
enter the divisor theorem, with summable losses.  Ordinary dependent
random choice is not automatically sufficient: it may find a biclique in
the first-edge graph without synchronizing the unique partner edges.  The
uncontrolled survivor is precisely an irregular graph whose first edges
have high endpoint degree while their unique scalar partners avoid every
large common endpoint block.
