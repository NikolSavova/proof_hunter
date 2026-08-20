# Common-translation design matrices and the matching-defect barrier

## 1. Outcome

Fix a nonzero realized difference `q=a-b` and a clean fibre `H_q`.  For a
source edge `S={c,d}` and its target `T={e,f}`, put

\[
 r_S={\bf1}_T-{\bf1}_S,
 \qquad r_S\cdot P=q.                            \tag{1.1}
\]

The common-translation matrix has a sharp signed linearity property:
every pair of signed endpoint columns occurs together in at most one row.
After merging source and target copies, every pair of actual-point columns
occurs in at most four rows, and four is attained by genuine integral
distance-Sidon examples.

This permits a valid design-matrix compression, but not a contradiction.
After pruning half the rows, the role-copy matrix has corank

\[
 O(k^2/h_q).                                     \tag{1.2}
\]

Row-centering supplies exactly four unavoidable kernel directions: the two
role constants and the two coordinate vectors.  On the linearly transformed
finite-field parabola, fibres of quadratic order have no further kernel:
the exact role-copy ranks are `2n-3` before centering and `2n-4` after
centering.  Thus ordinary rank is already maximally rigid on a genuine
distance-Sidon heavy fibre.

There is nevertheless an exact matching consequence.  If `F` is any source
matching, let `x_F` be its endpoint indicator, `y_F` the target endpoint
degree vector, and `z_F=y_F-x_F`.  Then

\[
 {\bf1}\cdot z_F=0,
 \qquad P^Tz_F=|F|q,
 \qquad
 \boxed{\|z_F\|_2^2=2(W_F+O_F)}.                \tag{1.3}
\]

Here `W_F` is the number of unordered target wedges and `O_F` is the number
of target incidences outside the source vertex set.  Since `q` is nonzero,
`z_F` is nonzero, so every source matching forces a target wedge or an
endpoint escape.  In particular a source perfect matching on all available
vertices cannot map to any target graph with the same degree vector; a
target perfect matching is impossible.

The quantitative loss is decisive: an edge-colouring of a fibre only forces
`Omega(h_q/k)` such defects.  The desired scalar estimate needs control on
the scale `h_q`, so the matching-defect charge is short by a factor `k` in
the worst case.  The exact parabola profiles show that maximal matrix rank
and many matching defects coexist with a legal quadratic fibre.  Any
successful inverse must use the scalar large-area concentration in addition
to (1.1); support rank and endpoint degrees alone do not suffice.

## 2. Sharp pair-column cooccurrence

Use two copies of the active point set, one for the source role and one for
the target role.  The row belonging to `S={c,d}` and `T={e,f}` has `-1` in
the source columns `c,d` and `+1` in the target columns `e,f`.

**Proposition 2.1.**  Two signed columns occur together in at most one row.

**Proof.**  Two source columns determine the source edge, hence its unique
row.  Two target columns determine the target edge, and the translation map
`tau_q(S)=T` is injective.  Finally suppose a fixed source column `c` and a
fixed target column `e` occur in two rows.  The two source edges share `c`
and the two target edges share `e`, contradicting the star-to-matching
theorem in `METRIC_SCALAR_AGGREGATE_MANY_FIBRE_AUDIT.md`.  \(\square\)

After merging the two role copies, a pair `{u,v}` can occur with the four
sign patterns

\[
 (--),\quad(++),\quad(-+),\quad(+-),             \tag{2.1}
\]

each at most once.  Therefore the merged codegree is at most four.  This
constant cannot be improved: the transformed `p=31,43,61` parabola fibres
in the verifier all contain an actual-point column pair of codegree four.

## 3. What the design-matrix theorem really gives

Let `h=|H_q|`, and let `n` be the number of active actual endpoints.  Start
with the `h by 2n` signed role-copy matrix `C`.  Iteratively delete a column
of current degree less than

\[
 \kappa={h\over4n}                               \tag{3.1}
\]

together with all rows containing it.  Fewer than `2n*kappa=h/2` rows are
deleted.  The remaining matrix `C_0` has `m>=h/2` rows, four nonzeros per
row, minimum column degree at least `kappa`, and pair-column codegree one.

The Dvir--Saraf--Wigderson design-matrix theorem therefore gives

\[
 \operatorname{corank}C_0
 \le {m\,4\cdot3\over\kappa^2}
 \le {192n^2\over h}.                            \tag{3.2}
\]

Let `Q` be any rank-`m-1` row-centering operator.  Since every surviving
row still satisfies (1.1),

\[
 \operatorname{corank}(QC_0)
 \le1+{192n^2\over h}.                           \tag{3.3}
\]

The kernel of `QC_0` contains both independent role-constant vectors and
the `x`- and `y`-coordinate vectors repeated in the two roles.  When the
active endpoints are noncollinear these four vectors are independent.
Comparing with (3.3) yields only `h<=64n^2`, weaker than the trivial edge
bound.  No choice of constants in this application changes the exponent:
the design theorem measures a constant corank when `h` is quadratic, while
the affine realization already forces a constant-dimensional kernel.

The merged matrix `R` has pair-column codegree four.  Its centered kernel
contains `1,X,Y`, and gives the same `O(n^2/h)` compression and the same
quadratic barrier.

## 4. Exact maximal-rank genuine stress

Let

\[
 P_p=\{(x,x^2\bmod p):0\le x<p\}                \tag{4.1}
\]

and apply the explicit integral linear map from
`METRIC_SCALAR_UNIVERSAL_MATRIX_AND_RULER_STRESS.md`.  The resulting set is
integral and distance-Sidon; the linear map preserves every clean relation
and every coefficient matrix.

For the largest clean fibres at `p=31,43,61`, the two anchors are inactive,
so `n=p-2`.  Exact reduction modulo `1,000,003` gives

\[
\begin{array}{c|r|r|r|r|r|r}
p&h&n&\operatorname{rank}C&\operatorname{rank}QC&
 \operatorname{rank}R&\operatorname{rank}QR\\ \hline
31&86&29&55&54&27&26\\
43&171&41&79&78&39&38\\
61&336&59&115&114&57&56
\end{array}                                      \tag{4.2}
\]

Thus

\[
 \operatorname{nullity}C=3,\quad
 \operatorname{nullity}QC=4,
 \quad
 \operatorname{nullity}R=2,\quad
 \operatorname{nullity}QR=3.                    \tag{4.3}
\]

All are the maximum ranks allowed by the affine equations.  For example,
before centering the role-copy kernel consists unavoidably of affine
functions in the two roles whose constant offset compensates their common
value on `q`; this is three-dimensional.  Centering removes that one scalar
condition and makes the unavoidable dimension four.  The merged statement
is the analogous two- and three-dimensional version.

This finite stress does not merely show that a crude estimate has poor
constants.  It identifies the conceptual obstruction: a legal heavy fibre
can make the common-translation system as rigid as algebraically possible.
There is no extra nullity for a rank inverse to extract.

## 5. The matching-defect identity

Let `F subset H_q` be a matching of `L` source edges.  Let `S_F` be its set
of `2L` source endpoints.  For every active vertex `v`, put

\[
 x_v={\bf1}_{v\in S_F},\qquad
 y_v=\deg_{\tau_q(F)}(v),\qquad z_v=y_v-x_v.    \tag{5.1}
\]

Summing the row equations gives

\[
 \sum_vz_v=0,
 \qquad
 \sum_vz_vP_v=Lq.                              \tag{5.2}
\]

In particular `z` cannot vanish.  Define

\[
 W_F=\sum_v\binom{y_v}{2},
 \qquad
 O_F=\sum_{v\notin S_F}y_v.                    \tag{5.3}
\]

Since `sum y_v=2L=sum x_v` and `x_v` is zero or one,

\[
\begin{aligned}
 \|z\|_2^2
 &=\sum_vy_v^2+2L-2\sum_{v\in S_F}y_v\\
 &=\sum_vy_v(y_v-1)+2O_F\\
 &=2(W_F+O_F),                                  \tag{5.4}
\end{aligned}
\]

proving (1.3).  If `F` is perfect on all vertices available to a clean
fibre, target edges cannot escape, so `O_F=0`; hence `W_F>=1`.  This proves
the proposed perfect-matching obstruction in the stronger degree-sequence
form.

Every simple graph with `h` edges on `n` vertices can be greedily
edge-coloured into at most `2n-1` matchings, and every matching has at most
`floor(n/2)` edges.  Consequently any matching partition has at least

\[
 B\ge\left\lceil{h\over\lfloor n/2\rfloor}\right\rceil
 =\Omega(h/n)                                   \tag{5.5}
\]

nonempty blocks, and (5.4) forces at least `B` total wedge-or-escape units.
But this is only `Omega(h/k)`.  Without an additional scalar or geometric
weight, it cannot pay for a bound on the `h` scale.

## 6. Exact verification and verdict

The companion verifier checks Proposition 2.1, sharp merged codegree four,
all four ranks in (4.2), the common-translation equations, and (5.4) on a
canonical matching partition of each tested genuine fibre.  At `p=61` its
59 matching blocks have total squared discrepancy `1090`; all `545` defect
units are endpoint escapes for this partition.

Run

```text
python3 phase2/loop/erdos1208/verify_common_translation_design_matrix_matching_defect.py
```

The common translation has now been fully exploited at the level of sparse
matrix support and endpoint degrees.  It gives a sharp linear design and an
exact matching-defect charge, but both stop at the quadratic endpoint
barrier.  The surviving route must correlate these defects with the
large-area scalar collision blocks (or use an arithmetic height theorem);
ordinary rank, BSG matchings, or endpoint incidence alone cannot close the
scalar gate.
