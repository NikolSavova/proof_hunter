# The onion/Hall gate: an exponential common-restart obstruction

**Date:** 2026-08-14  
**Verdict:** the rankwise near-maximal inequality `(RNP)` is neither proved
nor disproved here.  What is disproved is the proposed missing premise that
the source can be recovered, with polynomial ambiguity, from a recursively
halved tangent/onion endpoint stack.  There are exponentially many
near-maximal rank-`r` faces with the same exterior ear replacement, the same
two tangent endpoints, and the same interior onion pocket.  Any restart that
does not deliberately write the source identity into the selected target
face loses `Omega(r)` bits.  This narrows the final Hall gate: a successful
map must be a genuine target-face encoder, not an endpoint-only decoder.

## 1. The target being audited

Put `ell=ceil(log_2 n)` and

\[
 N_r=|\{A\in\mathcal F_r(P):u(A)\le4(r+1)\}|.
\]

The rankwise inequality

\[
 N_{\ell-g}\le (\log n)^{O(1)}2^{-g}V(P)             \tag{RNP}
\]

would imply the near-maximal mean lemma and hence close Erdős 838.  The
suggested geometric proof sends a blocked point through either an exterior
ear replacement or an interior onion restart, recursively keeps one of two
arcs, and hopes that the endpoint stack identifies the source with only
`r^{O(1)}` inverse ambiguity.

The construction below shows that this last hope is false if the target face
does not itself carry a linear-size source code.

## 2. A parametric exact construction

Fix `r>=5`, put `M=5r` and `L=M-1`, and take the integer concave chain

\[
 q_i=(i,i(L-i)),\qquad 0\le i\le L,                 \tag{1}
\]

together with

\[
 p=(-1,M^2).                                        \tag{2}
\]

Choose an index `c` strictly between `0` and `L`.  Inside the open triangle
`q_0q_cq_L`, choose an arbitrary finite rational set `Q` so that the whole
configuration is in general position.  Such choices exist because at each
step only finitely many lines are forbidden and rational points are dense in
the open triangle.

For every `(r-3)`-set

\[
 S\subseteq\{q_1,\ldots,q_{L-1}\}\setminus\{q_c\},
\]

define

\[
 A_S=\{q_0,q_c,q_L\}\cup S.                         \tag{3}
\]

There are exactly

\[
 {5r-3\choose r-3}                                  \tag{4}
\]

such sources.

> **Theorem 1 (common ear and common onion).**  Every `A_S` is a rank-`r`
> convex face.  In the ambient set
> `P={q_0,...,q_L,p} union Q` it satisfies
> \[
> u(A_S)=4r\le4(r+1).                                \tag{5}
> \]
> Moreover all sources have simultaneously
> \[
> \operatorname{ext}(A_S\cup\{p\})=\{p,q_0,q_L\},   \tag{6}
> \]
> with tangent endpoints `q_0,q_L`, and
> \[
> P\cap\operatorname{int}(\operatorname{conv}A_S)=Q.\tag{7}
> \]
> In addition, every convex face containing `p` contains at most two of the
> chain vertices `q_i`.

**Proof.**  The points in (1) lie on a strictly concave parabola, so every
subset is in convex position.  Every omitted chain point is therefore
addable to `A_S`.  Each point of `Q` lies inside the fixed triangle
`q_0q_cq_L`, hence inside every `conv(A_S)`, so it is blocked.

For `0<j<L`, the point `q_j` lies strictly inside the triangle
`pq_0q_L`.  Indeed its height is positive, while comparison with the line
`pq_L` reduces to

\[
 j(L-j)<\frac{M^2}{L+1}(L-j)=M(L-j),
\]

which is just `j<M`; the third side is automatic since `j>=0`.  Thus `p`
hides every chain vertex except the two endpoints, proving (6), so `p` is
also blocked.  The only addable points are consequently the `M-r=4r`
omitted chain vertices, proving (5).

Finally every omitted chain point lies outside the convex hull of all other
chain points, hence outside `conv(A_S)`.  The point `p` is outside as well,
whereas all of `Q` is inside the fixed anchor triangle.  This proves (7).
More generally, for `i<j<k`, the same line comparison with endpoints
`q_i,q_k` puts `q_j` strictly inside `conv{p,q_i,q_k}`.  Thus no convex face
containing `p` can contain three chain vertices.
QED.

If desired, choose

\[
 |Q|=2^{r+g}-5r-1.
\]

Then `|P|=2^{r+g}`, so `ell=r+g` and the sources occur at exactly the rank
`ell-g` in `(RNP)`, for any `g` for which the displayed cardinality is
positive.

## 3. Endpoint-stack recoverability is exponentially false

The count in (4) satisfies

\[
 {5r-3\choose r-3}\ge5^{r-3}.                       \tag{8}
\]

This follows termwise from
`binom(m,k)>= (m/k)^k` and `(5r-3)/(r-3)>5`.

Now consider any restart record which, besides the common repaired triangle
and common onion pocket, retains at most `O(log r)` source-vertex labels and
`r^{O(log r)}` auxiliary endpoint/orientation states.  This includes a
binary larger-arc recursion of depth `O(log r)` with `O(1)` endpoint labels
per level.  The total number of possible records is

\[
 (5r)^{O(\log r)}=2^{O((\log r)^2)}.                \tag{9}
\]

By (8)--(9), some record has inverse fibre

\[
 2^{\Omega(r)-O((\log r)^2)}=2^{\Omega(r)},          \tag{10}
\]

not `r^{O(1)}`.  In information language, distinguishing the sources needs
at least

\[
 \log_2{5r-3\choose r-3}=\Omega(r)                  \tag{11}
\]

bits, whereas the endpoint stack carries only `O((log r)^2)` bits.

This obstruction applies on both sides of the proposed dichotomy:

* the exterior point `p` gives the same ear replacement and tangent pair;
* every interior blocked point enters the same first onion pocket `Q`.

There is no way to evade the first item by carrying more of the old chain
in a convex target which still contains `p`: Theorem 1 says that such a
target can retain at most two source vertices.  The missing `Omega(r)` bits
must therefore be written using points of `Q` (or some other new pocket),
not by a more elaborate `p`-rooted endpoint word.

In particular there are only

\[
 \sum_{j=0}^2{5r\choose j}=O(r^2)                  \tag{12}
\]

convex faces supported on the chain together with `p` which contain `p`.
Any exterior-only assignment of the sources (3) to such targets has a fibre
of size at least `5^{r-3}/O(r^2)`.  Allowing a logarithmic endpoint word
enlarges the state space only to (9), and remains exponentially inadequate.

Recursively choosing the larger discarded exterior arc can retain `A_S`
itself, but that is not a Hall gain: it consumes the source face as its own
target and creates no capacity for the `Theta(n)` blocked labels.  Entering
the common onion pocket creates ample local capacity, but only if the chosen
inner target face is used as a binary code for `S`.  That is exactly the
global overlapping-pocket Hall problem, not endpoint recoverability.

## 4. What is and is not killed

Theorem 1 does **not** refute `(RNP)`.  In fact the common pocket `Q` can
contain enough convex faces to encode all sources, just as in the earlier
visible-pocket decoder.  It refutes the narrower proposed completion:

> “The recursively retained endpoint/onion stack by itself determines the
> source up to polynomial ambiguity.”

A viable proof of `(RNP)` must instead establish a Hall inequality in which
the selected target face stores `Omega(r)` bits of the outer source while
also allocating `Theta(n/2^r)` units per source across overlapping pockets.
The remaining problem is therefore capacity allocation, not recovery of a
short tangent stack.

## 5. Exact verification

Run

```bash
python3 phase2/loop/erdos838/agent_onion_hall/verify_onion_hall_obstruction.py
```

The audit uses `r=6`, `g=1`, and `n=128`.  It constructs 97 exact rational
inner points, checks every determinant in the 128-point configuration, and
checks all `binom(30,3)=4060` apex-rooted triples.  It then enumerates all
`binom(27,3)=2925` sources.  For every source it verifies convexity,
`u(A)=24`, the common repaired triangle, and the identical strict interior
pocket.  It writes `certificate.json` beside the script.
