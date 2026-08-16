# Circuit-localized hard-core attack on Erdős 838

**Date:** 2026-08-14  
**Verdict:** no complete proof is claimed.  This lane does produce a new
rank-three geometric input: a sharp localization theorem for second
extensions.  A bad curvature step can occur only when extension mass is
concentrated in three consecutive tangent pockets.  This is precisely the
planar condition absent from the known abstract 4-flag barriers.  The
remaining problem is now a three-pocket, two-orientation stack inequality.

The report also records two necessary corrections.  Edge-pocket link
factorization is false (adjacent pockets interact), and the proposed
pointwise half-curvature inequality is asymptotically false on a realizable
fixed-template vertical construction.  A block-smoothed version remains
consistent with all data.

Throughout, `P` is an `n`-point set in planar general position,
`F_r` is its family of convex-position `r`-subsets, and

\[
 v_r=|F_r|,\qquad
 p_r={ (r+1)v_{r+1}\over(n-r)v_r}.
\]

For `A in F_r`, let

\[
 U(A)=\{q\notin A:A+q\in F_{r+1}\},\qquad u(A)=|U(A)|.
\]

Thus

\[
 {1\over v_r}\sum_{A\in F_r}u(A)
 ={(r+1)v_{r+1}\over v_r}=(n-r)p_r.                 \tag{1}
\]

## 1. Tangent pockets and the failure of factorization

Write a convex polygon `A` counterclockwise as
`a_0,...,a_(r-1)`, and orient every edge so that `A` lies in its left
half-plane.  An exterior point `q` is individually addable to `A` if and
only if it violates exactly one of these `r` support inequalities.  Denote
by `R_i(A)` the points violating only the support line of
`a_i a_(i+1)`.  Then

\[
 U(A)=\bigsqcup_{i\in\mathbb Z/r\mathbb Z}R_i(A).    \tag{2}
\]

It is tempting to claim that choices in different pockets are independent.
They are not.  Take

\[
 A=((0,0),(3,0),(3,3),(0,3)),\quad
 q=(1,-10),\quad x=(-10,1).
\]

The six points are in general position.  Both `A+q` and `A+x` are convex;
`q` and `x` lie in the bottom and left edge pockets.  But `A+q+x` is not
convex: `(0,0)` is hidden.  Consequently neither

\[
 Z_{\operatorname{link}(A)}(z)=\prod_i Z_i(z)       \tag{3}
\]

nor independence of distinct pockets is valid.  The exact failure is local:
the two pockets in this example are adjacent.

## 2. The nonadjacent-pocket theorem

> **Theorem 1 (pair conflicts are cyclically local).**
> Let `A` be a convex `r`-gon, `r>=4`.  If
> `q in R_i(A)` and `x in R_j(A)`, where `i` and `j` are neither equal nor
> adjacent modulo `r`, then
> \[
> A+q+x\in F_{r+2}.                                  \tag{4}
> \]

**Proof.**  The support line of edge `i` strictly separates `q` from every
point of `A+x`, because `q` violates that inequality while `x`, being in a
different pocket, satisfies it.  Hence `q` is extreme in `A+q+x`; the same
argument makes `x` extreme.  At an old vertex `a_k`, at most one of its two
incident edges can be one of the nonadjacent selected edges `i,j`.  The
other incident edge remains a support edge for the whole set and certifies
that `a_k` is extreme.  Thus every point of `A+q+x` is extreme.  QED.

This elementary support-line argument is a concrete rank-three
oriented-matroid circuit-elimination constraint.  It fails in the abstract
complete-3-skeleton-plus-disjoint-facets barrier.

Put

\[
 m_i(A)=|R_i(A)|,\quad u=\sum_i m_i,
 \quad M(A)=\max_i(m_{i-1}+m_i+m_{i+1}).             \tag{5}
\]

Let `lambda_2(A)` be the number of unordered pairs `{q,x}` for which
`A+q+x` is convex.  Theorem 1 gives

\[
\begin{aligned}
 \lambda_2(A)
 &\ge \sum_{\{i,j\}\text{ nonadjacent}}m_i m_j\\
 &=\frac12\left(u^2-\sum_i m_i(m_{i-1}+m_i+m_{i+1})\right)\\
 &\ge {u(u-M(A))\over2}.                             \tag{6}
\end{aligned}
\]

Every convex `(r+2)`-face is counted from each of its
`binom(r+2,2)` rank-`r` subfaces, so

\[
 \sum_{A\in F_r}\lambda_2(A)=\binom{r+2}{2}v_{r+2}. \tag{7}
\]

Combining (1), (6), and (7), and writing
`U_r=(n-r)p_r`, proves the exact curvature bound

\[
 \boxed{
 p_{r+1}\ge
 {\sum_{A\in F_r}u(A)(u(A)-M(A))
  \over v_rU_r(n-r-1)}.}                             \tag{8}
\]

In particular, if `M(A)<=alpha u(A)` for every relevant `A`, Jensen gives

\[
 \boxed{
 p_{r+1}\ge(1-\alpha){n-r\over n-r-1}p_r.}          \tag{9}
\]

A useful averaged form uses

\[
 \theta_r={\sum_Au(A)M(A)\over\sum_Au(A)^2}.
\]

Then

\[
 {p_{r+1}\over p_r}\ge
 (1-\theta_r){n-r\over n-r-1}.                      \tag{10}
\]

Thus a ratio appreciably below `1/2` forces more than half of the relevant
second-moment extension mass into a cyclic window of three tangent pockets.
This is the promised common-endpoint supersaturation dichotomy:

* dispersed tangent mass gives the desired curvature immediately;
* all difficulty is localized to three consecutive pockets.

The exact checker verifies (4) on 8,173 nonadjacent extension pairs from
13,925 convex faces in twenty random integer records.  This is only a
finite audit; the proof above is deterministic.

There is also an exact graph formulation of the maximal-face part.  On
`U(C)`, form the **extension-conflict graph** `G_C`, joining `q` and `x`
when `C+q+x` is nonconvex.  A cover `C+a` is maximal if and only if `a` is a
universal vertex of `G_C`.  Indeed, points already bad for `C` stay bad by
heredity, while every other addable point must conflict with `a`.  Hence, if
`M_r` denotes the number of maximal rank-`r` faces and `d(C)` the number of
universal vertices of `G_C`,

\[
 \boxed{rM_r=\sum_{C\in F_{r-1}}d(C).}              \tag{10a}
\]

By Theorem 1, the closed neighbourhood of each such universal vertex is
contained in its own edge pocket and the two adjacent pockets.  Thus
maximal faces are not an additional diffuse obstruction: they are exactly
the fully concentrated endpoint of the same three-pocket alternative in
(10).

## 3. Exact repair classification

The maximal-face obstruction can also be stated without ambiguity.  Let
`S` be nonconvex and suppose `S-x` is convex.  Write

\[
 B=\operatorname{ext}(S),\qquad D=S\setminus B.
\]

The sets `B` and `D` are convex-position sets (`D` is a subset of the
convex repair).  There are exactly two structural cases.

> **Lemma 2 (singleton or ear replacement).**
>
> 1. If `x in D`, then `D={x}`.
> 2. If `x=b_i in B`, every point of `D` lies in the open ear triangle
>    \[
>    \operatorname{conv}(b_{i-1},b_i,b_{i+1}),
>    \]
>    and `D` is precisely a convex replacement chain between
>    `b_(i-1)` and `b_(i+1)`.  Equivalently,
>    `(B-x) union D` is obtained by replacing the single hull vertex `x`
>    by that inward chain.

**Proof.**  If an interior point other than `x` remained after deleting an
interior `x`, the hull `B` would be unchanged and the remaining interior
point could not be extreme.  Hence `D={x}`.

Now let `x=b_i` be a hull vertex.  Removing it replaces the two incident
hull edges by the diagonal `b_(i-1)b_(i+1)`.  The part of `conv(B)` lost in
this operation is exactly its open ear triangle at `b_i`.  Every member of
`D` must be outside `conv(B-x)` in order to be extreme after the deletion,
so it lies in that ear.  Since the repaired set is convex, all members of
`D` occur on the single hull chain joining the two neighbours.  The converse
is immediate from the same hull description.  QED.

Together with the at-most-three-repairs lemma from the tilted-switch lane,
this classifies every inverse history of a failed two-extension as either a
singleton interior insertion or one of at most two hull-ear replacements.

It also shows why counting *all* nested pairs `(B,D)` is too loose.
On the saved twenty-point record, at size seven there are 72,739 subsets
whose first two onion layers are separately convex, but only 1,593 have any
convex one-point deletion.  Since `v_7=8`,

\[
 {72739\over 2^6\,7v_7}=20.295\ldots,
 \qquad
 {1593\over 2^6\,7v_7}=0.444\ldots.                 \tag{11}
\]

The ear-interlacing condition is load-bearing.

## 4. An exact two-extension moment identity

There is a second useful way to expose the repair term.  For a nonface `S`,
let

\[
 d(S)=|\{x\in S:S-x\text{ is convex}\}|.
\]

Double-count rank-`r` faces with two individually addable points.  If both
points can be added together, the resulting `(r+2)`-face is counted
`binom(r+2,2)` times.  If their joint addition is nonconvex, the two added
points are repairs of the resulting nonface, and every pair of repairs
arises uniquely this way.  Therefore

\[
 \boxed{
 \sum_{A\in F_r}\binom{u(A)}2
 =\binom{r+2}{2}v_{r+2}
  +\sum_{\substack{|S|=r+2\\S\notin F}}\binom{d(S)}2.} \tag{12}
\]

For `r>=3`, planar repair degree is at most three, so
`binom(d,2)<=d`.  Since

\[
 B_{r+1}=\sum_{|S|=r+2,S\notin F}d(S),
\]

(12) yields

\[
 \sum_{A\in F_r}\binom{u(A)}2
 \le\binom{r+2}{2}v_{r+2}+B_{r+1}.                  \tag{13}
\]

This identity is exact on every rank of the saved record.  It is not by
itself strong enough near `r~log n`: the additive boundary error is the
maximal-pocket mass.  Theorem 1 is stronger when extensions are dispersed,
while Lemma 2 tells us exactly what must be treated in the concentrated
case.

## 5. Why pointwise half-curvature is not the answer

A very attractive proposed target was

\[
 {p_{r+1}\over p_r}\ge2^{-1-o(1)}                 \tag{14}
\]

uniformly through `(1-o(1))log_2 n`.  It would telescope to the desired
`p_r>=2^{-r-o(r)}`.  Statement (14) is false even on realizable sharp
construction families.

Take the central strong-glue template `S_10` and vertically iterate it
twelve times.  Here

\[
 \log_2n=163.820692\ldots.
\]

The curvature ratios below `0.9 log_2 n` have periodic bad blocks:

```text
r = 13,14,15:   0.4961, 0.4753, 0.4247
r = 29,30,31:   0.4795, 0.4606, 0.4128
r = 45,46,47:   0.4741, 0.4557, 0.4087
...
r =125,126,127: 0.4677, 0.4497, 0.4034
r =141,142,143: 0.4673, 0.4493, 0.4031.
```

The total excess

\[
 \sum_{r\le.9\log_2n}\max\{0,-\log_2(p_{r+1}/p_r)-1\}
 =4.5615\ldots=0.02784\ldots\log_2n.                \tag{15}
\]

Increasing the iteration depth repeats the blocks at positive density, so
the pointwise `o(1)` loss cannot hold.  The good ratios between bad blocks
are well above `1/2`; they compensate in the product.  The correct target
must therefore be block-smoothed or potential-amortized, not pointwise.

## 6. The remaining three-pocket stack gate

Equations (8)--(10) reduce the new work to the concentrated alternative.
The geometric state is much smaller than an arbitrary hypergraph link:

1. a middle tangent edge and its two adjacent edge pockets;
2. an orientation (`left` or `right`) recording which adjacent pocket
   dominates; and
3. under a failed addition, Lemma 2 replaces one hull vertex by a convex
   chain in its ear.

Repeated failures therefore create a laminar tangent stack.  The desired
completion is an amortized inequality of the form

\[
 -\log_2{p_{r+1}\over p_r}
 \le1+\Phi_{r+1}-\Phi_r+\varepsilon_r,              \tag{16}
\]

where `Phi` is a two/three-state tangent-stack potential and
`sum_(r<=log n) epsilon_r=o(log n)`.  Telescoping (16) gives
`p_r>=2^{-r-o(r)}` and closes Erdős 838.  The periodic `S_10` rows above are
the sharp regression test: `Phi` must store credit during the thirteen good
ranks and spend it during the three bad ranks.

An equivalent switching formulation is the tagged ear-reset lemma:

> Route every maximal boundary incidence through successive ear
> replacements, retain the left/right tangent stack, and end at an
> `(r+1)`-face.  The final face plus an `r`-bit push/pop word must determine
> the inverse history up to `2^{o(r)}` choices.

Theorem 1 supplies the dispersed steps with no serious loss; Lemma 2 makes
each concentrated push geometrically laminar.  What is not yet proved is
that the middle tangent edge is recoverable from the final face throughout
the stack.  Recording it afresh at every level would cost `r^{Theta(r)}`;
recoverability is exactly the last gate between the present localization
theorem and a full proof.

## 7. Verification

Run from the repository root:

```bash
python3 -m py_compile \
  phase2/loop/erdos838/agent_circuit_hardcore/circuit_hardcore_audit.py

python3 \
  phase2/loop/erdos838/agent_circuit_hardcore/circuit_hardcore_audit.py
```

The audit writes `certificate.json`.  It verifies the explicit
factorization counterexample; checks pair locality on random exact integer
records; exhausts repair structure, nested-pair counts, and (12) on the
saved twenty-point record; and evaluates the depth-twelve curvature
countertest by exact integer graded recurrence.
