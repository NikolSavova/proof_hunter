# A scalable counterexample to the weighted `C4` inequality

## Result

The proposed universal inequality

\[
 W\le m^2C                                                   \tag{1}
\]

is false, and its failure is unbounded.  Here `A` is the `0,1`
biadjacency matrix of a finite simple bipartite graph,

\[
\begin{aligned}
 m&=\sum_{ij}A_{ij},\\
 C&=\sum_{i,k,j,l}A_{ij}A_{il}A_{kj}A_{kl},\\
 W&=\sum_{i,k,j,l}A_{ij}A_{il}A_{kj}A_{kl}
                 d_i d_k e_j e_l,
\end{aligned}
\]

and `d_i,e_j` are the two degree sequences.

The counterexample is particularly elementary: start with a complete
bipartite core and attach the same number of pendant leaves to every
core vertex.

## Construction

For positive integers `n,t`, let `G_{n,t}` be obtained from `K_{n,n}`
as follows.

* Attach `t` new column-side leaves to each of the `n` core rows.
* Attach `t` new row-side leaves to each of the `n` core columns.

Thus each side has `n(1+t)` vertices.  Every core vertex has degree

\[
 D=n+t,
\]

every new vertex has degree one, and

\[
 m=n^2+2nt=n(n+2t).                                      \tag{2}
\]

## Exact count

Count ordered row pairs according to their types.  A core row paired
with itself has `D` common columns.  Two distinct core rows have the
`n` core columns in common.  A core row and a leaf row have one common
column, and two leaf rows have a common column precisely when they are
attached to the same core column.  Consequently

\[
\begin{aligned}
 C
 &=nD^2+n(n-1)n^2+2n^2t+nt^2\\
 &=n^4+4n^2t+2nt^2.                                      \tag{3}
\end{aligned}
\]

For the weighted count, the sum of the column degrees in a core row is

\[
 h=nD+t.
\]

The same four row-pair types give

\[
\begin{aligned}
 W={}&nD^2h^2+n(n-1)D^2(nD)^2
       +2n^2tD^3+nt^2D^2\\
   ={}&nD^2\bigl(n^3D^2+4ntD+2t^2\bigr).                 \tag{4}
\end{aligned}
\]

For example, `G_{7,8}` is a `63` by `63` bipartite graph and has

\[
 (m,C,W)=(161,4865,127044225).
\]

Therefore

\[
 m^2C-W=-938560<0.                                        \tag{5}
\]

## An unbounded family

Set `t=n^2`.  Equations (2)--(4) reduce to

\[
\begin{aligned}
 m&=n^2(2n+1),\\
 C&=n^4(2n+5),\\
 W&=n^7(n+1)^2(n^3+2n^2+5n+6),                           \tag{6}\\
 m^2C-W
 &=-n^7\bigl(n^5-4n^4-18n^3-4n^2+12n+6\bigr).           \tag{7}
\end{aligned}
\]

For `n>=7`, the polynomial in parentheses is positive.  Indeed,

\[
 n^5-4n^4-18n^3-4n^2+12n+6
 =n^3(n^2-4n-18)-4n^2+12n+6,
\]

and `n^2-4n-18>=3` in this range.  Hence every `G_{n,n^2}` with
`n>=7` violates (1).  More strongly,

\[
 \frac{W}{m^2C}
 =\frac{(n+1)^2(n^3+2n^2+5n+6)}
        {n(2n+1)^2(2n+5)}
 \sim \frac n8.                                           \tag{8}
\]

Thus no constant-factor version `W<=K m^2C` holds universally either.

## What happens to the signed genuine-rectangle residue

This family also kills a proof based on retaining the helpful genuine
rectangles in the exact degenerate/genuine decomposition.  Write the
integer-scaled identity as

\[
 m^2C-W=\Delta+G,                                         \tag{9}
\]

where `Delta=m^2 sum_e delta_e>=0` is the already-certified degenerate
slack and

\[
 G=\sum_{\substack{i\ne k,\ j\ne l\\
                    A_{ij}A_{il}A_{kj}A_{kl}=1}}
       (m^2-d_i d_k e_j e_l)                              \tag{10}
\]

is the signed genuine contribution.

In `G_{n,t}`, every genuine rectangle lies wholly in the complete core.
There are `n^2(n-1)^2` ordered genuine rectangles, and each has degree
product `D^4`.  For `t=n^2`, this gives

\[
 G=-n^8(n-1)^2(n^2+4n+2).                                \tag{11}
\]

There are no helpful genuine rectangles at all.  Directly summing the
three edge types in `delta_e` gives

\[
 \Delta=n^7(6n^4+13n^3+4n^2-10n-6).                     \tag{12}
\]

Equations (11) and (12) sum to (7).  Thus the failure is exactly in the
signed residue requested here: the nonnegative degenerate budget is too
small even before any positive-part relaxation.

## Consequence for counted repair `C4`s

The implication

\[
 W\text{ large}\quad\Longrightarrow\quad
 C\ge W/m^2
\]

cannot be used in ACP or in the counted-repair step.  In fact the loss
cannot be repaired by a universal constant, since (8) diverges.  Any
replacement must retain an additional restriction present in the repair
incidence graph (for example a degree cap, near-biregularity, or a
geometric/history constraint); it cannot be a theorem about arbitrary
finite simple bipartite graphs.

## Verification artifact

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_weighted_c4_scalable_counterexample.py
```

The verifier constructs the adjacency matrices, recomputes `C,W`, the
edgewise degenerate certificates, and the signed genuine sum using exact
integer arithmetic.  It also checks the closed forms on a grid of
parameters and the scalable counterexample at `n=7`.
