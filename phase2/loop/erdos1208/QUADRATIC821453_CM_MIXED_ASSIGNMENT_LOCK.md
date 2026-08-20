# Mixed-inertia and arbitrary-assignment lock for quadratic 821453

## 1. Verdict

Within the bounded-inertia Eisenstein-CM construction over

\[
 E=\mathbb Q(\sqrt{821453}),                           \tag{1.1}
\]

the certified all-square configuration

\[
 |T|=219,\qquad d=217,\qquad N=11335                 \tag{1.2}
\]

is the unique survivor at `alpha=0.49369313` after allowing all of the
following simultaneously:

1. any mixture of square and fourth-power inertia caps;
2. arbitrary reassignment of prime ideals to inertia and useful roles; and
3. every possible change of the exact sign/mod-4 ray rank under that
   reassignment.

The independent verifier is

```text
python3 phase2/loop/erdos1208/verify_quadratic821453_cm_mixed_assignment_lock.py
```

It does not import or modify the separate mixed-inertia verifier.  It uses
the already hostile-audited field and endpoint primitives, then rebuilds the
weighted Golod--Shafarevich, assignment-dual, ray-rank, and all-anchor
checks.

## 2. Exact weighted Golod--Shafarevich budget

Let `j` of the 219 inertia generators receive fourth-power caps, and let the
remaining `219-j` receive square caps.  If the safe generator rank is `d`,
put

\[
 M_d=\left\lfloor{d^2-1\over4}\right\rfloor.          \tag{2.1}
\]

The quadratic relation budget consists of the Shafarevich charge `d+1`,
the `219-j` inertia squares, and `N_j` useful Frobenius squares.  Saturating
it gives

\[
 N_j=M_d-(d+1)-(219-j)=N_0+j.                        \tag{2.2}
\]

The three possible ranks and all-square counts are

\[
\begin{array}{c|c|c}
d&M_d&N_0\\ \hline
217&11772&11335\\
218&11880&11442\\
219&11990&11551.
\end{array}                                           \tag{2.3}
\]

At `x=2/d`, the weighted GS polynomial is

\[
 P(x)=1-dx+M_dx^2+jx^4.                               \tag{2.4}
\]

The verifier checks (2.4) as an exact rational number for all

\[
 d\in\{217,218,219\},\qquad0\le j\le219,             \tag{2.5}
\]

and finds it strictly negative in every cell.  One additional quadratic
relation makes the quadratic discriminant `-3` for odd `d` and zero for
even `d`; the nonnegative quartic term cannot restore strict negativity.

An uncapped tame inertia generator is dominated by a fourth-power cap: the
fourth cap does not consume a quadratic slot, reduces the root-discriminant
exponent from `1/2` to `3/8`, and remains allowed by (2.4).  Thus square and
fourth caps exhaust the optimum within this family.

## 3. Rank-aware ray classes

The exact ray group calculation supplies two independent unit columns in a
four-dimensional sign/mod-4 quotient.  Prime-ideal columns modulo their
span have four colors in `F_2^2`.  Consequently an arbitrary 219-ideal set
has one of five relevant color spans:

\[
\begin{array}{c|c|c|c}
\text{case}&\operatorname {rank}C&d&
\text{last ideal in the smallest allowed }T\\ \hline
\text{full}&4&217&1213\\
\text{line 1}&3&218&3089\\
\text{line 2}&3&218&3389\\
\text{line 3}&3&218&3467\\
\text{zero}&2&219&8009.
\end{array}                                           \tag{3.1}
\]

The three rank-three rows are the three hyperplanes containing the unit
span; the rank-two row is the unit span itself.  These five rows exhaust all
subspaces.  Thus the apparent generator gain from lower ray rank is retained
exactly rather than assumed away.

## 4. Joint all-depth assignment dual

For a useful ideal of norm `Q`, set

\[
 c(Q)={\log Q\over2},\qquad
 g_k(Q)={1\over4}\log A_k(Q^{-2}),                   \tag{4.1}
\]

and at tangent slope `lambda` define

\[
 V_\lambda(Q)=\sum_{k\ge1}(g_k(Q)-\lambda c(Q))_+ .  \tag{4.2}
\]

If `rho` is the derivative of the endpoint right side with respect to
`log D_L`, the assignment-dependent dual scores are

\[
\begin{array}{c|c}
\text{role}&\text{score}\\ \hline
\text{fourth-capped inertia}&-3\rho\log Q/8\\
\text{square-capped inertia}&-\rho\log Q/4\\
\text{useful}&V_\lambda(Q)\\
\text{unused}&0.
\end{array}                                           \tag{4.3}
\]

Every available norm is at least nine.  The verifier rechecks the strict
rational inequality underlying the uniform all-depth facts

* `V_lambda(Q)` is nonincreasing in `Q`;
* `V'_lambda(log Q)>-1/(4 log Q)` whenever the active depth is fixed.

All tested root discriminants exceed 300 and `alpha<1/2`, so at every
anchor

\[
 \rho>{1\over\log9}.                                  \tag{4.4}
\]

It follows that both

\[
 {\rho\log Q\over4}+V_\lambda(Q),\qquad
 {3\rho\log Q\over8}+V_\lambda(Q)                   \tag{4.5}
\]

increase with `Q`.  Successive exchanges in (4.3) prove that, for each ray
row and each fixed `j`, the optimistic optimum is exactly:

1. the `j` smallest allowed ideals receive fourth caps;
2. the next `219-j` allowed ideals receive square caps; and
3. the first `N_j` remaining ideals receive useful roles.

For every competing row, all of these remaining ideals are declared useful
without running the CM/Kummer test.  This can only favor the competitor.
The actual winning `j=0` useful list was separately certified with zero
rejections in the hostile arithmetic audit.

## 5. Endpoint and all-anchor exclusion

For the winning cell, the safe upper bound

\[
 {2\sqrt3\over\pi}<{71603\over64935}                 \tag{5.1}
\]

at `w=40752.9517` gives endpoint margins

```text
0.00117455846108839...
0.00117473610479516...
```

For exclusions the verifier instead uses the favorable lower bound

\[
 {11978\over10863}<{2\sqrt3\over\pi}.                \tag{5.2}
\]

Smaller constant means a smaller endpoint right side, so failure with
(5.2) rigorously implies failure with the true constant.

Every one of the other `5*220-1=1099` cells receives its own exact
high-precision separator.  At that separator both endpoint margins are
negative, the left derivative is positive, and the right derivative is
negative.  Concavity therefore excludes every anchor.  The closest cells
in the five ray rows are:

\[
\begin{array}{c|c|r}
\text{case}&j&\text{largest common margin}\\ \hline
\text{rank 4}&1&-0.2561378303\ldots\\
\text{rank 3, line 1}&0&-37.9839198902\ldots\\
\text{rank 3, line 2}&0&-42.5609677401\ldots\\
\text{rank 3, line 3}&0&-44.6533819353\ldots\\
\text{rank 2}&0&-87.0516524957\ldots.
\end{array}                                           \tag{5.3}
\]

Thus even the single fourth-cap change is separated from the theorem
exponent by a margin over 0.25 in the logarithmic endpoint inequality.
The rank-reducing non-prefix branches are much farther away.

## 6. Scope

This locks mixed order-two/order-four tame inertia and arbitrary prime-ideal
assignment for the fixed `D=821453`, `|T|=219` presentation.  It does not
exclude a different ramified count, a higher-order weighted presentation,
or a different base field.  Combined with the hostile arithmetic audit, it
shows that the theorem exponent `0.49369313` is not an artifact of having
prematurely fixed either the inertia orders or the norm-prefix assignment.

