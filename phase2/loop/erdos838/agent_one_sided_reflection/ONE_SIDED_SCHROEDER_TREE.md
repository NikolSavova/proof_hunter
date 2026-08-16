# One-sided reflection orders are Schroeder trees, and they pay exponentially

## Status

This note closes the **exactly one-sided** reflection-order branch and gives
an explicit quantitative stability statement for a sparse set of two-sided
cells.  The proof is elementary and order-type invariant.  The accompanying
verifier is

```text
python3 phase2/loop/erdos838/agent_one_sided_reflection/verify_one_sided_schroeder.py
```

It exhausts the class through eight points, checks the classification and a
rational stretchable realization of every member, and audits all numerical
claims below.

Throughout, points are labelled `0,...,n-1` in increasing x-coordinate and
are in general position.  Write `chi(i,j,k)` for the orientation of the
ordered triple `i<j<k`, with values `+` and `-`.  A cup is a subset all of
whose triples have sign `+`; a cap is defined with sign `-`.  Sets of size at
most two count as both.

## 1. The exact classification

Call an ordered point set **one-sided** if, for every `i<k`, all points
strictly between `i` and `k` lie on the same side of the chord `ik`.  Thus
there is a sign

\[
 s_{ik}=\chi(i,j,k)\qquad(i<j<k)                         \tag{1}
\]

which is independent of `j`.

### The four-point closure law

For every `a<b<c<d`,

\[
 \boxed{s_{ac}=s_{bd}\quad\Longrightarrow\quad
        s_{ad}=s_{ac}.}                                  \tag{2}
\]

Indeed, if the two signs are positive, the three consecutive chord slopes
on the four selected points satisfy

\[
 m_{ab}<m_{bc}<m_{cd}.
\]

Consequently `chi(a,b,d)>0`, and one-sidedness of the interval `[a,d]`
gives `s_ad=+`.  The negative case is the reversed inequality.

There is a useful converse in purely combinatorial form.  Put one symbol on
each of the `n-1` adjacent gaps.  For gaps `p<q`, define

\[
 p\prec q\quad\Longleftrightarrow\quad s_{p,q+1}=+.       \tag{3}
\]

Taking `(a,b,c,d)=(p,q,q+1,r+1)` in (2) shows that this
tournament has no directed triangle: if the comparisons of `(p,q)` and
`(q,r)` agree, the comparison of `(p,r)` agrees with them.  Hence `prec` is
a total order.  Let `pi` be the corresponding permutation of the gaps, so

\[
 s_{ik}=+\quad\Longleftrightarrow\quad \pi_i<\pi_{k-1}.
                                                               \tag{4}
\]

For four distinct gap positions `x<y<z<w`, the only possible failures of
(2) are

\[
 \pi_y<\pi_w<\pi_x<\pi_z
 \quad\hbox{or}\quad
 \pi_z<\pi_x<\pi_w<\pi_y.
\]

Their relative patterns are respectively `3142` and `2413`.  We have
therefore proved:

> **Classification theorem.**  One-sided sign systems on `n` ordered
> points are in bijection with permutations of `n-1` avoiding `2413` and
> `3142`, via (4).

For completeness, the standard elementary characterization of separable
permutations is recalled next.  A direct sum `alpha+beta` places all entries
of `alpha` before and below all entries of `beta`; a skew sum places all
entries of `alpha` before and above all entries of `beta`.  A permutation is
**separable** if it is obtained from singletons by direct and skew sums.
These are exactly the permutations avoiding `2413` and `3142`.  One quick
proof uses the inversion graph.  Four entries induce a chordless four-vertex
path exactly when their pattern is `2413` or `3142`.  A graph with no
induced four-vertex path and at least two vertices is disconnected or has
disconnected complement.  Applied recursively to an inversion graph,
these two alternatives are precisely direct-sum and skew-sum decompositions.

It follows that every one-sided system has a nontrivial pivot `c` such that

\[
 \begin{array}{ll}
 s_{ik}=+&\text{for every }i<c<k,\quad\text{or}\\
 s_{ik}=-&\text{for every }i<c<k,                         \tag{5}
 \end{array}
\]

and the two overlapping child intervals `[0,c]` and `[c,n-1]` are again
one-sided.  Iterating gives a signed shared-pivot tree.  Contracting adjacent
nodes of equal sign gives the unique signed reduced Schroeder tree.  Hence
the number of systems on `n` points is the large Schroeder number
`R_(n-2)`:

\[
 2,6,22,90,394,1806\qquad(n=3,4,5,6,7,8).                \tag{6}
\]

### Every classified system is stretchable

The classification is not merely a signotope statement.  Every system in
(4) has a rational straight-line realization.

Induct on its signed shared-pivot tree.  Realize each child as a polygonal
chain with consecutive x-coordinates.  A transformation

\[
 e\longmapsto ae+b\qquad(a>0)                            \tag{7}
\]

of all adjacent slopes is induced by an orientation-preserving affine map
and therefore preserves the child's signs.  At a positive node with `m`
gaps, compress the left slopes into `[0,eta]` and the right slopes into
`[1,1+eta]`, where `0<eta<1/m`, then identify the two copies of the pivot.
At a negative node exchange the two slope intervals.

To check a positive node, take a triple whose two extreme vertices straddle
the pivot.  If its middle vertex is on the left, its first chord slope is at
most `eta`, whereas its second is a weighted average containing at least
one right gap and is at least `1/m>eta`.  If the middle vertex is on the
right, the second chord slope is at least `1`, whereas the first is at most
`1-1/m+eta<1`.  Thus every such triple is positive.  The negative case is
the reflection.  Choosing rational `eta` at every node gives rational
slopes and hence rational coordinates.

There is also an intrinsic interpretation of `pi` in any realization: it is
exactly the relative order of the adjacent edge slopes.  For gaps `p<q`,
the signs of the triples `(p,p+1,q+1)` and `(p,q,q+1)` are both
`s_(p,q+1)`.  If this sign is positive, the first inequality says that the
left edge slope is below a weighted average of the middle and right slopes,
while the second says that a weighted average of the left and middle slopes
is below the right edge slope.  If the left edge slope were at least the
right one these inequalities would contradict each other.  Hence

\[
 s_{p,q+1}=+\quad\Longleftrightarrow\quad e_p<e_q.         \tag{8}
\]

This also supplies a direct geometry audit of the permutation encoding.

## 2. The long cup-or-cap theorem

Let `p(P)` and `q(P)` be the maximum sizes of a cup and a cap in a one-sided
system `P`.

> **Theorem (Schroeder-tree cup-cap product).**
> For every one-sided ordered set of `n` points,
> \[
> \boxed{(p(P)-1)(q(P)-1)\ge n-1.}                        \tag{9}
> \]

**Proof.**  Induct on the shared-pivot decomposition.  Suppose first that
the root sign is positive, with child intervals `L,R` of sizes `n_L,n_R`
and shared pivot, so `n=n_L+n_R-1`.

Choose maximum cups in both children.  If both contain the pivot, their
union loses only the duplicated pivot.  If neither contains it, their union
loses nothing.  If exactly one contains it, delete the pivot from that cup.
In every case the two traces now agree about pivot membership, their union
is a cup by (5), and

\[
 p(P)-1\ge (p(L)-1)+(p(R)-1).                             \tag{10}
\]

On the other hand, a cap of size at least three cannot meet both open sides
of the pivot: three of its points would have extreme endpoints straddling
the pivot and hence positive orientation.  Therefore

\[
 q(P)-1=\max\{q(L)-1,q(R)-1\}.                            \tag{11}
\]

Writing `a=p(L)-1`, `b=q(L)-1`, `c=p(R)-1`, and `d=q(R)-1`,
the inductive hypothesis and (10)--(11) give

\[
 (p(P)-1)(q(P)-1)
 \ge(a+c)\max(b,d)
 \ge ab+cd
 \ge(n_L-1)+(n_R-1)=n-1.
\]

At a negative root, interchange cup and cap.  The cases `n<=2` are
immediate.  This proves (9).  \(\square\)

Consequently one of the two chains has size at least
`1+sqrt(n-1)`.  Every subset of a cup or cap is in convex position, so if
`V(P)` counts convex-position subsets, including the empty set,

\[
\boxed{V(P)\ge 2^{1+\sqrt{n-1}}.}                       \tag{12}
\]

This is far stronger than the desired
`2^((1/2-o(1))(log n)^2)` lower bound in the exactly one-sided regime.

One can also see directly that a convex subset of a one-sided set is either
a cup or a cap.  If both its upper and lower hull paths had an internal
vertex, the two internal vertices would lie on opposite sides of the chord
joining the extreme vertices, contrary to one-sidedness.  Thus, writing
`C,U` for the numbers of cups and caps including the empty set,

\[
 V=C+U-\left(1+n+{n\choose2}\right).                     \tag{13}
\]

Formula (13) explains why the oriented cup-cap cross-term is unnecessary
here: the tree already forces one pure family to contain a Boolean cube of
dimension at least `1+sqrt(n-1)`.

## 3. Sparse two-sided defects

The exact theorem has a useful robust corollary.  On the vertex set of an
arbitrary ordered point configuration, make a graph whose edges are the
endpoint pairs `(i,k)` for which the intermediate points occur on both sides
of chord `ik`.  Let `B` be the number of these two-sided pairs.  The
Caro--Wei bound gives an independent set of size

\[
 m\ge {n^2\over n+2B}.                                   \tag{14}
\]

Every endpoint pair inside this independent set is globally one-sided, and
hence its induced order type satisfies the hypotheses above.  Therefore

\[
 \boxed{
 \log_2 V(P)\ge
 1+\sqrt{{n^2\over n+2B}-1}.}                            \tag{15}
\]

(As usual, take an integer floor in (14); this changes (15) only by `O(1)`.)

This connects directly to the coupled-cell notation

\[
 a_{ik}(t)=t+A_{ik}(t),\qquad
 b_{ik}(t)=t+B_{ik}(t).
\]

A two-sided cell has a nonzero quadratic coefficient in each remainder.
All coefficients are nonnegative integers, so at `h=1/2`

\[
 A_{ik}(h)B_{ik}(h)\ge {1\over16}.
\]

Thus, with

\[
 E=\sum_{i<k}A_{ik}(1/2)B_{ik}(1/2),
\]

we have `B<=16E` and hence

\[
 \boxed{
 \log_2V(P)\ge
 1+\sqrt{{n^2\over n+32E}-1}.}                           \tag{16}
\]

In particular, writing `L=log_2 n`,

\[
 E\le {n^2\over8L^4}
 \quad\Longrightarrow\quad
 \log_2V(P)\ge(1/2-o(1))L^2.                            \tag{17}
\]

Equivalently, the reflection-order attack may now discard the entire
small-product regime (17).  Any unresolved configuration below the target
must have total two-sided product mass

\[
 \sum_{i<k}A_{ik}(1/2)B_{ik}(1/2)
 > {n^2\over8(\log_2n)^4}.                               \tag{18}
\]

This is a genuine global lower bound on the mixed term, not merely a count
of endpoint records.

## 4. Exact finite audit

The verifier reports the following exhaustive data:

\[
\begin{array}{c|rrrrrr}
n&3&4&5&6&7&8\\ \hline
\#\text{ one-sided systems}&2&6&22&90&394&1806\\
\min V&8&15&27&45&73&114
\end{array}
\]

For every member it checks (2), the bijection (4), avoidance of the two
patterns, recursive sum/skew decomposition, exact rational stretchability,
(9), and the face identity (13).  The minimum of
`(p-1)(q-1)-(n-1)` is zero at every tested size, so the product theorem has
the correct constant even though the induced face-count bound (12) is not
usually sharp.
