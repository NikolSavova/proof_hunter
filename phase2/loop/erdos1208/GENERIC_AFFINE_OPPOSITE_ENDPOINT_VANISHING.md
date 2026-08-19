# Generic affine images have no orthogonal rich tail

## 1. Theorem

Let `A_0` be a finite vector-Sidon subset of the rational plane: every
nonzero directed difference has one ordered endpoint representation.  There
is an invertible rational linear map `T` such that, for `A=T A_0` and
`D=A-A`, both of the following hold:

1. `A` is distance-Sidon;
2. for every nonzero translation `q`,

\[
 R_D(q)R_D(Jq)=0.                                  \tag{1.1}
\]

After clearing denominators, `A` is integral.  In particular the
support-adaptive popular set is empty, the opposite-endpoint off-diagonal
count is zero, and

\[
 \mathcal E_\perp(D)=R_D(0)^2=|D|^2.              \tag{1.2}
\]

Thus the final difficulty in Erdos 1208 is entirely an affine-resonant
phenomenon.  Vector-Sidon configurations become trivial for the orthogonal
tail after a generic change of metric; a proof for the square grid must use
the special interaction between its complete differences and the fixed
quarter-turn.

## 2. Proof

Put

\[
 D_0=A_0-A_0,\qquad X_0=D_0-D_0.                  \tag{2.1}
\]

There are two finite lists of bad algebraic conditions on `T`.

First, for nonzero `d,e in D_0` with `e!=+-d`, exclude

\[
 \|Td\|^2=\|Te\|^2.                               \tag{2.2}
\]

Each is a proper polynomial condition: one may choose a positive-definite
quadratic form that separates the two non-antipodal vectors.  Avoiding all
conditions (2.2), together with `det T=0`, makes `T A_0` distance-Sidon.
Vector-Sidonicity of `A_0` ensures that no two genuinely different endpoint
pairs have identical or antipodal base differences.

Second, for every nonzero `x,y in X_0`, exclude

\[
 JT x=T y.                                         \tag{2.3}
\]

This is again a proper algebraic condition.  If `x,y` are independent, their
two images under `T` may be chosen independently and need not be a
quarter-turn pair.  If they are dependent, (2.3) would ask a nonzero real
vector to be a real scalar multiple of its quarter-turn, which is impossible.

The complement of finitely many proper real algebraic sets is nonempty and
contains rational matrices.  Choose rational `T` there.  If `R_D(q)>0`, then
`q` is a difference of two elements of `D=T D_0`, so `q=T x` for some
`x in X_0`.  If also `R_D(Jq)>0`, then `Jq=T y` for some `y in X_0`.  For
`q!=0` this is exactly the forbidden relation (2.3).  This proves (1.1), and
(1.2) follows because `R_D(0)=|D|`.

## 3. Exact Costas control

The theorem is qualitative, but the Welch--Costas controls show the same
effect before taking a fully generic matrix.  The table records

\[
 (\mathcal O_K,\ |\operatorname{im}\Xi|,
   \max\nu,\ \sum\nu^2)
\]

at the adaptive threshold.

\[
\begin{array}{c|c|r|r|r|r}
p&\text{metric}&\mathcal O_K&|\operatorname{im}\Xi|&\max\nu&\sum\nu^2\\ \hline
7&\text{raw Costas}&4,342&2,340&8&11,170\\
7&\text{distance-separated}&24&24&1&24\\
11&\text{raw Costas}&607,206&54,475&105&13,026,498\\
11&\text{distance-separated}&160&160&1&160
\end{array}                                           \tag{3.1}
\]

The raw arrays are vector-Sidon but repeat Euclidean norms.  The displayed
integral shears/stretches are the smallest transformations found by the
existing exact search that separate all norms.  Norm separation collapses
the size-biased load from `2.57...` and `21.45...` to exactly one in these
two cases.  This is evidence for the reopened cross-fibre conjecture, not a
proof of it for an arbitrary distance-Sidon set.

Run `verify_generic_affine_opposite_endpoint_vanishing.py` for (3.1) and for
direct checks that the stretched configurations are distance-Sidon.
