# Dense two-sided cells: a rank-four trace star and its exact barrier

## Verdict

Let `B` be the number of two-sided endpoint pairs.  Dense two-sidedness has
a stronger rank-four consequence than the crude inequality
`B<=16 sum A(1/2)B(1/2)`: it forces a fixed two-point trace with many mixed
endpoint extensions.  Quantitatively, some pair is the peeled core of at
least

\[
                         {B^2\over n^3}                    \tag{1}
\]

convex quadrilaterals whose x-extreme chord is a diagonal.  In the live
residue `B>2n^2/(log n)^4`, this degree is larger than
`4n/(log n)^8`.

This does **not** by itself close the branch.  There is an exact rational
universality construction in which two fixed roots have a complete
`I times K` grid of such quadrilateral extensions while the detached clouds
`I` and `K` retain arbitrary prescribed order types.  Completeness at
rank one on each side therefore does not release either detached Boolean
shield.  A proof must use higher-rank path compatibility, repeated trace
stars, or a quantitative oriented-chain theorem.

The accompanying verifier is

```text
python3 phase2/loop/erdos838/agent_one_sided_reflection/verify_dense_two_sided_trace.py
```

It checks the incidence identity, the constants, a central Pascal
regression, and the rational universality construction.

## 1. Rank-four mass

For an endpoint pair `i<k`, put

\[
 r_{ik}=|\{j:i<j<k,\ \chi(i,j,k)=+\}|,
 \qquad
 s_{ik}=|\{j:i<j<k,\ \chi(i,j,k)=-\}|.                   \tag{2}
\]

These are exactly the quadratic coefficients of the two non-direct path
remainders.  Thus

\[
 [t^4]A_{ik}(t)B_{ik}(t)=r_{ik}s_{ik}.                    \tag{3}
\]

Choosing one intermediate point of each sign gives a convex quadrilateral:
the segment joining the two intermediate points crosses the endpoint chord.
Conversely, a convex four-set whose x-extreme chord is a diagonal arises
uniquely this way.  Hence

\[
 T:=\sum_{i<k}r_{ik}s_{ik}                                \tag{4}
\]

is exactly the number of mixed rank-four endpoint faces, or equivalently
the total number of their two-point peeled traces counted with extension
multiplicity.

If `(i,k)` is two-sided and `m=k-i-1`, then `r,s>=1`, `r+s=m`, and

\[
                         rs\ge m-1=k-i-2.                 \tag{5}
\]

There are fewer than `n` endpoint intervals of each positive value of
`k-i-2`.  Consequently, if the `B` bad intervals are arranged in increasing
order of this value, the `a`-th value is at least `a/n`.  Summing gives

\[
 \boxed{T\ge {B(B+1)\over2n}\ge {B^2\over2n}.}            \tag{6}
\]

At half activity, (3) also gives the useful strengthening

\[
 \boxed{
 E:=\sum_{i<k}A_{ik}(1/2)B_{ik}(1/2)
 \ge {T\over16}\ge {B^2\over32n}.}                       \tag{7}
\]

Thus the live `B`-dense residue actually has
`E=Omega(n^3/(log n)^8)`, much larger than the earlier sufficient threshold.

The same incidence statement holds without truncating to rank four.  For a
convex open trace `S`, let `d_x(S)` be the number of endpoint cells in which
`S` is obtained by deleting the two endpoints of a face from the `AB`
summand (both boundary paths non-direct).  Endpoint extremes make this
decoder unique on the full face, and evaluation at `1/2` gives exactly

\[
 \boxed{
 4E=\sum_S d_x(S)2^{-|S|}.}                               \tag{7a}
\]

In particular, for any cutoff `D`, the contribution of traces with
`d_x(S)<=D` is at most `D F_P(1/2)` on the right side of (7a).  Thus a
capture argument has an exact dichotomy: either the product mass spreads
into the ordinary half-weight face complex with bounded load, or it is
carried by high radial-extension traces.  Sections 2--3 show that even the
first nontrivial high-load trace can retain arbitrary detached order type;
that branch needs more than its degree.

## 2. A common rank-two core

For a pair `j<l`, let `d(j,l)` be the number of endpoint pairs `i<j<l<k`
for which `{i,j,l,k}` is convex and `ik` is its diagonal.  Double counting
(4) yields

\[
 \sum_{j<l}d(j,l)=T.
\]

Since there are fewer than `n^2/2` pairs,

\[
 \boxed{
 \max_{j<l}d(j,l)>{2T\over n^2}\ge {B^2\over n^3}.}       \tag{8}
\]

In particular, if

\[
 B>{2n^2\over(\log_2n)^4},
\]

some two-point face has more than

\[
                         {4n\over(\log_2n)^8}             \tag{9}
\]

mixed two-endpoint extensions.  This is a concrete low-rank source star
extracted solely from the matrix residue.

One geometric description may be useful in a later container argument.
Apply an affine change taking the trace chord to
`j=(0,0), l=(1,0)`.  Suppose `y_i>0` and `y_k<0`.  The segment `ik` crosses
the open trace segment precisely when

\[
 {x_k\over-y_k}>{-x_i\over y_i},\qquad
 {x_k-1\over-y_k}<{1-x_i\over y_i}.                       \tag{10}
\]

Thus each of the two side orientations of the extension graph is a
two-dimensional dominance-range graph.  Notice that opposite sides of the
line `jl` alone are not sufficient: the intersection with the line may
fall outside the segment `jl`.

## 3. Why the trace star is not yet a shield

The following construction kills any claim that a complete grid of
rank-four extensions forces one of the detached clouds to be convex.

> **Universality regression.**  Let `X,Y` be arbitrary finite rational
> general-position point sets.  There is a rational realization consisting
> of affine copies `I` of `X` and `K` of `Y`, together with points `j,l`,
> ordered
> \[
>                    I<j<l<K,                              \tag{11}
> \]
> such that every set `{i,j,l,k}` with `i in I, k in K` is in convex
> position and has diagonals `ik,jl`.

**Construction.**  Normalize both inputs into the unit square.  For a
sufficiently small positive rational `epsilon`, put

\[
\begin{aligned}
 I&=(-2,2)+\epsilon X,\\
 j&=(0,0),\qquad l=(1,0),\\
 K&=(3,-2)+\epsilon Y.                                   \tag{12}
\end{aligned}
\]

At `epsilon=0`, every segment from the left centre to the right centre
crosses the open segment `jl` at `(1/2,0)`.  The inequalities are strict, so
they persist for all sufficiently small rational `epsilon`.  Internal
orientations in each cloud are multiplied by `epsilon^2` and are therefore
unchanged.  Every possible new collinearity excludes at most finitely many
values of `epsilon`, so a sufficiently small rational value can also be
chosen outside all of them.  This proves the claim.

The construction can already realize

\[
                         B\ge |I||K|.                      \tag{13}
\]

Taking `|I|` about `n/(log n)^4` and `|K|=n-o(n)` places it exactly at the
live density scale while leaving the near-full detached cloud `K`
unrestricted.  Even taking both clouds linear gives a constant-density bad
chord graph without forcing either cloud's face complex.

This is not a counterexample to the desired coefficient-one-half theorem:
additional faces using several cloud points may pay.  It is an exact barrier
to a **rank-four-only** proof.  The missing assertion must say that many
quadrilateral extensions have compatible higher histories, or else charge
the arbitrary detached cloud recursively without losing the required
cross-term.

## 4. Pascal stress test

The central strong-glue Pascal cells show that (6)--(8) are in the correct
regime but do not by themselves overshoot the sharp construction.  The
verifier obtains:

\[
\begin{array}{c|r|r|r|r}
n&B&T&\max d(j,l)& B/n^2\\ \hline
6&4&9&4=2^2&0.111111\\
20&119&2223&81=9^2&0.297500\\
70&2036&399469&1156=34^2&0.415510\\
252&29777&70552355&15625=125^2&0.468900
\end{array}
\]

Thus the asymptotically sharp Pascal family has a positive density of
two-sided cells and `Theta(n^4)` mixed rank-four mass.  Its maximum trace
star is already a balanced, essentially full two-ended grid of quadratic
size.  The missing payment in precisely this regression is the oriented
cap--cup product of the two detached Pascal children.  Any proposed
dense-cell inequality predicting more than coefficient one half, or
replacing that oriented product by unrestricted child faces, should be
tested here first.
