# Erdős 838: the matching-lower-bound frontier

> Working note, 2026-08-13.  The upper coefficient `1/2` is proved in
> `proof_blowup_half.md`.  This note records the strongest lower lemmas now
> available, the exact point at which they stop, and the most plausible route
> to the full problem.  All logarithms are base two.

## 1. Exact endpoint target

Put the points in increasing `x`-order.  For `s<t`, let `c(s,t)` and
`u(s,t)` be the numbers of caps and cups with endpoints `s,t`.  Splitting a
convex polygon into its upper and lower chains gives the exact identity

\[
 V(P)=1+|P|+\sum_{s<t}c(s,t)u(s,t).                 \tag{1}
\]

Thus a proof that the limit in problem 838 equals `1/2` is equivalent to

\[
 \sum_{s<t}c(s,t)u(s,t)
 \ge 2^{(1/2-o(1))(\log |P|)^2}.                  \tag{2}
\]

The issue is not producing cap mass and cup mass separately.  It is making
the two masses meet on the same endpoint pair.

## 2. A sharp product theorem for strong-decomposition trees

Suppose `T=A\prec B` is a strong glue, with `a=|A|` and `b=|B|`.  For
nonempty caps, cups, and convex subsets the exact recurrences are

\[
\begin{aligned}
 C(T)&=C(B)+(b+1)C(A),\\
 U(T)&=U(A)+(a+1)U(B),\\
 W(T)&=W(A)+W(B)+C(A)U(B).                        \tag{3}
\end{aligned}
\]

Put `R(T)=sqrt(C(T)U(T))`.  Cauchy--Schwarz gives

\[
 R(T)\ge \sqrt{b+1}\,R(A)+\sqrt{a+1}\,R(B).       \tag{4}
\]

Following the larger child from a tree with `n` leaves, let `m_i` be the
successive subtree sizes and let `s_i=m_i-m_{i+1}` be the discarded sibling
sizes.  Iterating (4) along this path gives

\[
 \log R(T)\ge {1\over2}\sum_i\log(s_i+1).          \tag{5}
\]

Write `d_i=log(m_i/m_{i+1})`, so `0<d_i<=1`.  The elementary estimate

\[
 \log(s_i+1)\ge d_i(\log m_i-1)                   \tag{6}
\]

follows from `d_i<=2s_i/m_i` and convexity of `(m_i/2)^d` for
`0<=d<=1`.  Since `sum d_i=log n` and

\[
 \sum_i d_i\log m_i
 ={1\over2}\left((\log n)^2+\sum_i d_i^2\right), \tag{7}
\]

we obtain the rigorous bound

\[
 \boxed{\quad
 C(T)U(T)\ge 2^{\frac12(\log n)^2-\log n}.
 \quad}                                           \tag{8}
\]

Its quadratic coefficient is sharp: balanced templates in the `1/2` upper
construction have `log C+log U=(1/2+o(1))(log n)^2`.

Equation (8) by itself gives only `W>=max(C,U)>=sqrt(CU)`, hence the old
coefficient `1/4`.  The missing step is still alignment with the oriented
cross term `C(A)U(B)` in (3).

## 3. Exact stability identity at one glue

There is more information than the Cauchy--Schwarz inequality records.
Expanding (3) gives the exact identity

\[
\begin{split}
 C(T)U(T)
={}&\left(\sqrt{b+1}\,R(A)+\sqrt{a+1}\,R(B)\right)^2\\
 &+\left(
 \sqrt{C(B)U(A)}-
 \sqrt{(a+1)(b+1)C(A)U(B)}
 \right)^2.                                      \tag{9}
\end{split}
\]

The second square is exactly the directional obstruction.  If the forward
term `C(A)U(B)` counted by `W` is much smaller than the reverse term
`C(B)U(A)`, then the product mass at the parent has quantitative slack over
(4).  A matching tree theorem should charge every bad forward alignment to
this slack; repeated bad alignments cannot simply be discarded.

This suggests the following sharply delimited intermediate theorem.

> **Tree alignment conjecture.**  Every binary strong-decomposition tree
> with `n` leaves satisfies
> \[
> W(T)\ge 2^{\frac12(\log n)^2-O(\log n\log\log n)}. \tag{10}
> \]

Exact Pareto dynamic programming verifies (10) through `n=19`; a
multiobjective beam continuation remains above the target through `n=64`.
Those computations are evidence, not a proof.

There is an exact pattern interpretation. For a leaf set `S`, suppress the
unary vertices in its minimal spanning subtree. Then `S` is a cap iff this
reduced ordered tree is a left comb, a cup iff it is a right comb, and convex
iff it is a left-comb branch joined to a right-comb branch. Consequently
(10) is a minimum-occurrence problem for induced **one-turn combs** in an
arbitrary ordered full binary tree. This makes the decomposable target
self-contained and may permit tree-profile methods, but the known fixed-size
caterpillar inducibility theorems are not uniform for size `Theta(log n)` and
count a different rooted pattern.

## 4. Why the graph multiplicity proof is the right comparison

Feige--Kenyon--Kogan proved that every red/blue complete graph on `n`
vertices has

\[
 2^{(1/4-o(1))(\log n)^2}
\]

monochromatic complete vertex sets.  Their Ramsey-tree proof counts nested
monochromatic-neighbourhood histories and loses only a factorial when many
histories encode the same clique.  Bal--Cutler--Pebody isolate the core
estimate particularly cleanly: if `a_1=n` and
`a_{j+1}=ceil((a_j-1)/2)`, then good histories of length `q` satisfy

\[
 \prod_{j=1}^q a_j
 \le |\mathcal X(G,q)|
 \le q!\,k(G)i(G).                                \tag{11}
\]

For planar point sets, a cap/cup extension remembers an endpoint *pair*,
not adjacency to every preceding vertex.  Consequently the graph history
does not transfer verbatim.  The rank-three signotope one-change axiom is
the extra geometric structure available to repair that loss of memory.

A sufficient new lemma would be a map from weighted endpoint histories to
shared-endpoint cap--cup pairs whose fibres have size
`2^{O(q log q)}`.  That loss is negligible for `q=Theta(log n)` and would
turn the modern `ES(k)=2^{k+o(k)}` scale into the desired exponent `1/2`.

The lower half of this proposal can now be proved. A nested endpoint-pair
process always generates

\[
 2^{\frac12(\log n)^2-O(\log n\log\log n)}
\]

hinged histories. The exact finite estimate is

\[
h_t(m)\ge 2^{-\binom t2}\frac{(m-(2^t-2))_+^t}{t!},
\]

with `t=floor(log m-2 log log m)`. However, the compression step is false in
its naive form: same-sign levels need not form caps or cups, and a hinged
history need not be split. Exact rational counterexamples and an infinite
split family with a linear convexity deficit are given in
`agent_geometry/HISTORY_ATTACK.md`. A successful compression must use the
full nested-bag order type, not merely the history sign word or split support.

## 5. Falsified shortcuts

The following do not close the gap.

1. The cap--cup product (8) without an alignment argument loses a factor
   two in the exponent.
2. Ordinary witness sampling, even with the sharp modern Erdős--Szekeres
   exponent, optimizes at `1/4`.
3. Random polynomial thinning of the iterated upper construction preserves
   its normalized coefficient.
4. Nonstationary homogeneous template compositions with no macroscopic
   scale jump cannot beat `1/2`; their unavoidable two-block terms already
   have coefficient `1/2`.
5. Generic convex-geometry closure theory is too weak: abstract convex
   geometries can have only linearly many closed sets.

The full problem is therefore reduced to a genuine multiplicity/stability
theorem, not another application of the existence theorem.
