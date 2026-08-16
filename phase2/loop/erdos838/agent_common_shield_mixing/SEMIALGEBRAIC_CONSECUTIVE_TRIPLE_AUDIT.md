# Semialgebraic consecutive-triple extraction: an ambient theorem and a selected-family barrier

**Date:** 2026-08-15.  All logarithms are base two.

## Verdict

Consecutive orientation constraints admit a strong **ambient-support**
extraction.  Let `X_1,...,X_r` be planar coordinate supports in general
position.  There are subsets `Y_i subset X_i` such that every product
transversal has a homogeneous orientation at every consecutive triple and

\[
                   |Y_i|\ge c_0^3|X_i|,
 \qquad c_0={1\over8\,3^{120}}.                           \tag{1}
\]

Thus the ambient Cartesian product loses only

\[
                          c_0^{3r}=2^{-O(r)},              \tag{2}

not `2^{-O(r log r)}` or `2^{-O(r^2)}`.  This follows by applying the
explicit Fox--Pach--Suk density theorem to one consecutive triple at a
time.  Each coordinate is shrunk at most three times, and previously fixed
orientation signs survive further restriction.  No growing-arity
regularity lemma is needed.

However, (1) does **not** imply that the extracted product cell contains a
selected source word.  There is an exact scalable planar concentration
barrier.  For parameters

\[
 N=2^d,\qquad r=3d,\qquad n=3dN,                          \tag{3}
\]

put all points on the parabola and group the coordinates into `d` blocks
of three interleaved color classes.  In each block a selected word must use
the same index in all three colors.  The resulting family has

\[
                         M=N^d=2^{d^2}                    \tag{4}

convex words, with `r=Theta(log n)` and
`log M=(1-o(1))(log n)^2`.  Yet every coordinate product cell on which all
consecutive orientation relations are homogeneous contains at most **one**
selected word.  Therefore any cover or partition of this family into such
cells needs at least `M` cells.  Direct same-type promotion loses the full
quadratic entropy.

The barrier has exactly quadratic support correlation:

\[
 P_0=\prod_i|X_i|=N^{3d}=M^3,
 \qquad\log(P_0/M)=2\log M.                               \tag{5}
\]

It is therefore consistent with a theorem allowed to charge projection
redundancy.  Indeed the entire constructed support is in convex position,
so the example is paid by an enormous ambient face bank.  What it rules
out is the proposed **retention** inference from local semialgebraic
homogeneity alone.

There is also an exact global density statement.  Let `F` be any family of
`M` chain-valid words, let `P_0=product_i|X_i|`, and put
`epsilon=M/P_0`.  Applying Corollary 1.2 of Fox--Pach--Suk once to the
`r`-ary relation defined by the `r-2` consecutive determinant inequalities
gives a positive homogeneous product box with

\[
 |Y_i|\ge
 {\epsilon^3\over 3^{40r}(r-2)^2}|X_i|.                 \tag{6}

This use of the primary theorem is uniform and explicit, but at
`r=kappa log n` its `3^{40r}` loss occurs in every coordinate.  Writing
`R=log(P_0/M)`, its bank size `B=product_i|Y_i|` only satisfies

\[
 \boxed{
 \log B\ge\log M-(3r-1)R
              -40r^2\log3-2r\log(r-2).}                 \tag{7}

Even at `R=0`, (7) loses a fixed multiple of `(log n)^2`, not
`o((log n)^2)`.  The polynomial regularity theorem likewise has an exponent
whose constant depends on the arity `r`, and its exceptional cells are
measured in product volume.  A selected family can put all its mass in
those cells, exactly as the diagonal construction does.

Hence the semialgebraic route makes real progress but does not close the
promotion gate.  The remaining low-redundancy regime is precise:

> prove a selected-family weighted version of the local extraction whose
> loss is `2^{O(R+r log r)}`, rather than the `(3r-1)R+Theta(r^2)` loss in
> (7), or use planar face banks to charge `R` before extraction.

The diagonal family proves that some explicit dependence on `R` is
unavoidable.

## 1. Primary theorem and constants

The source is Fox, Pach, and Suk,
[*A polynomial regularity lemma for semi-algebraic hypergraphs and its
applications in geometry and property testing*](https://arxiv.org/abs/1502.01730),
Theorem 1.1 and Corollary 1.2.

For a `k`-partite semialgebraic hypergraph in `R^d` of complexity `(t,1)`
and edge density at least `epsilon`, their corollary gives a complete
product with, in every vertex class,

\[
 { |P_i'|\over|P_i|}
 \ge {\epsilon^{d+1}\over
       2^{20kd\log(d+1)}t^d}.                            \tag{8}

This is obtained from their Theorem 1.1 with

\[
 C=2^{20m\log(m+1)}t^{m/k},
 \qquad m={d+1\choose d}-1=d.                            \tag{9}

These formulas matter here.  The asymptotic notation in the polynomial
regularity theorem is only for fixed `k,d,t,D`; it cannot be read as having
a uniform constant when `k=r=Theta(log n)`.

For one planar orientation constraint, take

\[
                       k=3,\quad d=2,\quad t=1.           \tag{10}

The positive and negative orientations partition the product, so one sign
has density at least `1/2`.  Equation (8) gives three subsets, all of whose
transversals have that sign, each of relative size at least

\[
 { (1/2)^3\over2^{120\log3}}={1\over8\,3^{120}}=c_0.    \tag{11}

No hidden dependence on `r` occurs in this local constant.

For the global chain-valid relation, take

\[
                k=r,\quad d=2,\quad t=r-2,\quad D=1.     \tag{12}

The `t` polynomials are the signed `3 by 3` affine determinants on
consecutive coordinate triples.  Substituting (12) into (8) gives (6)
exactly.  Multiplying (6) over all `r` coordinates and using
`epsilon=2^{-R}`, `P_0=M2^R`, gives (7).

For comparison, the full same-type theorem in the same paper gives a
per-coordinate fraction

\[
                         2^{-O(d^3r\log r)}.              \tag{13}

At `d=2`, multiplying (13) over `r` coordinates costs
`2^{-O(r^2 log r)}`.  It is strictly worse than (7) for this local chain
relation and should not be used here.

## 2. Local consecutive-triple extraction

> **Theorem 1 (unsigned consecutive-triple cell).**  Let
> `X_1,...,X_r subset R^2` be finite, pairwise disjoint, and in general
> position.  There are `Y_i subset X_i` satisfying (1) such that for every
> `j=1,...,r-2`, the sign
> 
> \[
>                    orient(y_j,y_{j+1},y_{j+2})          \tag{14}
> \]
> 
> is independent of the choices `y_i in Y_i`.

**Proof.**  Start with `Y_i=X_i`.  Process the consecutive triples in any
order.  On `(Y_j,Y_(j+1),Y_(j+2))`, one of the two orientation signs has
product density at least one half.  Apply (11) to replace each of the three
sets by a subset of relative size at least `c_0` on which that sign is
homogeneous.  Restriction cannot destroy a sign fixed at an earlier step.

Every coordinate occurs in at most three consecutive triples.  It is
therefore shrunk by at most `c_0^3`, proving (1).  QED.

Multiplying (1) gives

\[
                         \prod_i|Y_i|\ge c_0^{3r}P_0.     \tag{15}

Thus if the desired sign sequence were irrelevant, or if a selected word
were guaranteed to survive, the extraction loss would be only `O(r)` bits.
If the cell contains one chain-valid selected word, every homogeneous sign
in (14) must be the chain-valid sign, and then the entire cell is a valid
ambient transversal bank.

The last sentence is the exact missing condition.  The theorem selects a
large cell by product volume; it has no reason to preserve a correlated
family supported on a thin diagonal.

## 3. Exact parabola concentration barrier

Let

\[
                              p(s)=(s,s^2).                \tag{16}

For three distinct real parameters,

\[
 orient(p(a),p(b),p(c))
      =\operatorname{sign}\bigl((b-a)(c-a)(c-b)\bigr).   \tag{17}

Fix integers `d>=1`, `N>=2`, and split the `r=3d` coordinate positions
into blocks `j=0,...,d-1`.  Put `B_j=3Nj` and define

\[
\begin{aligned}
 X_{3j+1}&=\{p(B_j+3t):0\le t<N\},\\
 X_{3j+2}&=\{p(B_j+3t+1):0\le t<N\},\\
 X_{3j+3}&=\{p(B_j+3t+2):0\le t<N\}.                    \tag{18}
\end{aligned}

All `3dN` points are distinct and in general position.  For an index word
`tau=(t_0,...,t_(d-1)) in[N]^d`, define the selected source

\[
 Q_\tau=\bigcup_j\{
 p(B_j+3t_j),p(B_j+3t_j+1),p(B_j+3t_j+2)\}.              \tag{19}

The parameters in (19) are strictly increasing in coordinate order.
Hence every consecutive determinant is positive and every `Q_tau` is in
convex position on the parabola.  The sources are distinct and (4) holds.

> **Theorem 2 (one word per homogeneous cell).**  If
> `(Y_1,...,Y_r)` is a coordinate cell whose consecutive triple
> orientations are all homogeneous, then
> 
> \[
>       \left|\{\tau:Q_\tau\in\prod_iY_i\}\right|\le1.  \tag{20}
> \]

**Proof.**  Suppose the cell contains `Q_sigma,Q_tau` with
`sigma!=tau`.  Choose a block `j` with, say, `sigma_j<tau_j`.  The three
coordinate sets in that block contain both matching triples.  They
therefore also contain the mixed transversal with parameters

\[
 B_j+3\tau_j,\qquad B_j+3\sigma_j+1,
                    \qquad B_j+3\tau_j+2.                \tag{21}

The middle parameter in (21) is smaller than the first, while the third is
larger.  Equation (17) says this mixed labeled triple is negative.  But the
matching `tau_j` triple is positive.  The block is not homogeneous, a
contradiction.  QED.

Any homogeneous cell meeting the selected family automatically has the
positive sign at every consecutive triple, because its contained selected
word has that sign.  Thus Theorem 2 applies even if the proposed extraction
does not prescribe the signs in advance.

With `N=2^d`, equations (3)--(5) follow.  Since

\[
                 \log n=d+\log(3d),\qquad r=3d,          \tag{22}

we have

\[
 {\log M\over(\log n)^2}longrightarrow1,
 \qquad {r\over\log n}\longrightarrow3.                 \tag{23}

The concentration is therefore exactly at the requested logarithmic-rank,
quadratic-entropy scale.

## 4. Why polynomial regularity does not repair retention

The polynomial semialgebraic regularity theorem partitions the ambient
vertex set so that the total **product volume** of nonhomogeneous part
tuples is at most an error parameter `eta`.  It does not say that an
arbitrary selected measure assigns at most `eta` mass to those tuples.

In the barrier,

\[
                  {M\over P_0}=M^{-2}=2^{-2d^2}.          \tag{24}

Thus every selected word may lie in exceptional product cells even when
the regularity error is far smaller than every inverse polynomial in `n`
or `r`.  To force product-volume error below the selected density already
requires `eta<2^{-2d^2}`.  Even a polynomial dependence on `1/eta` then
has `2^{Theta(d^2)}` parts before any `r`-coordinate pattern is chosen.

This is not a defect of the 2016 constants.  It is the standard mismatch
between product-measure regularity and a singular correlated measure.  A
useful replacement must either regularize directly with respect to the
selected word measure or charge the correlation entropy `R`.

## 5. Exact remaining gate

The results above settle the applicability question as follows.

* Ambient supports: consecutive semialgebraic homogeneity costs only
  `2^{O(r)}` by Theorem 1.
* Selected source family: no `2^{o((log n)^2)}` retention theorem is
  possible without a correlation term, by Theorem 2.
* The primary global density theorem does include correlation through
  `epsilon=M/P_0`, but amplifies its bit cost by `3r` and also loses
  `40r^2log3`; equation (7) is not coefficient-free at `r=Theta(log n)`.

The strongest plausible next statement is a weighted dichotomy of the form

\[
 \text{homogeneous selected mass}
      \quad\text{or}\quad
 \text{ordinary face bank of gain }2^{\Omega(R)},         \tag{25}

with only `2^{O(r log r)}` additional load.  The diagonal construction
shows that the `R` term in (25) is necessary and sufficient on the sharp
concentration model.  Neither the fixed-arity regularity theorem nor the
growing-arity same-type lemma currently supplies (25).

## Verification

Run

```bash
python3 phase2/loop/erdos838/agent_common_shield_mixing/verify_semialgebraic_consecutive_triple_audit.py
```

The checker uses integer and rational arithmetic.  It verifies the primary
constant substitutions, the linear ambient-loss accounting, the global
density bound, every orientation in a finite parabola model, exhaustive
two-word cell collisions, and the scalable entropy/redundancy identities.
