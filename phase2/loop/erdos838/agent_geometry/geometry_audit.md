# Erdős #838: audit of the Pascal/Morris--Soltan geometry

## Verdict

The geometric decomposition and the proposed cap DP are correct for the
**sequential strong gluing** construction.  The row bound does count every
convex subset, but its diagonal case needs one sentence that was absent from
the short proposal: a convex subset contained in one block is encoded by its
upper cap and lower cup, so its number is at most `Cap * Cup`.

There is one statement-level caveat.  The decomposition lemma must say
"meeting at least two blocks."  A convex subset contained in one block need
not itself be a cap or a cup.  This does not damage the row bound because the
one-block case is handled by the upper/lower-hull injection.

The exact, standard-library-only certificate is `audit_geometry.py` in this
directory.  It constructs rational coordinates, checks every relevant
orientation, exhaustively enumerates small convex subsets, and independently
checks the cell DP.

## 1. A fully explicit rational strong glue

For points in increasing x-order write

`chi(p,q,r) = sign det(q-p,r-p)`.

A cap has all its triples `chi=-1`; a cup has all its triples `chi=+1`.
Call `A prec B` a strong glue when A is left and below B and

* `chi(a1,a2,b)=-1` for `a1<a2` in A and `b` in B;
* `chi(a,b1,b2)=+1` for `a` in A and `b1<b2` in B.

Here is an exact recursive realization.  Independently normalize A and B by
positive diagonal affine maps into `[0,1]^2`.  Their internal order types are
unchanged.  Let `mu` be the least internal pair-slope in either nonsingleton
copy and put

`eps = min(1/4, mu/(8+2*mu))`.

Map

`A -> {(eps*x,y)}` and `B -> {(1+eps*x,2+y)}`.

All cross-slopes are at most `3/(1-eps) <= 4`, whereas all internal slopes are
greater than 8.  Hence both strong-gluing conditions hold.  The construction
uses rational operations only.  Starting from singletons therefore produces
exact rational coordinates at every depth.

Define the Pascal cell

`T(n,i) = T(n-1,i-1) prec T(n-1,i)`,

with singleton boundary cells.  Form the row by sequential prefix gluing

`R_j = R_{j-1} prec T(n,j)` for `j=1,...,n`.

This last prefix condition is essential: merely demanding a pairwise relation
between individual blocks would not control triples drawn from three blocks.

For reference, the certificate produces the following row at `m=3` (block,
binary label, x, y):

```
0 000 0          0
1 100 355/154683 2/9
1 010 380/154683 8/27
1 001 5/2022     1/3
2 110 41/1011    2/3
2 101 55/1348    5/6
2 011 29/674     1
3 111 1          2
```

## 2. The row orientation law

Let `b(p)` be the block index.  Sequential strong gluing gives, for every
x-ordered triple `p<q<r` not lying in one block,

* `chi(p,q,r)=-1` if `b(q)<b(r)`;
* `chi(p,q,r)=+1` if `b(p)<b(q)=b(r)`.

Indeed, in the first case p and q were already in the prefix when r's block
was attached.  In the second, p was in the prefix and q,r were in the new
block.  Later positive diagonal affine maps preserve these signs.

## 3. Geometric decomposition lemma

Let a convex-position subset S meet blocks `B_k,...,B_l`, with `k<l`, where
k and l are its first and last occupied indices.

**First block.**  If `a<b<c` in `S cap B_k` had `chi(a,b,c)=+1`, choose any
`r` in a later occupied block.  The row law gives

`chi(a,b,r)=chi(a,c,r)=chi(b,c,r)=-1`.

The three edge tests then put b strictly inside triangle `a c r`, a
contradiction.  Thus `S cap B_k` is a cap.

**Last block.**  The reflected argument, using a point p in an earlier block,
shows that `S cap B_l` is a cup.

**Intermediate block.**  Suppose p is in an earlier block, `q<q'` are in an
intermediate block, and r is in a later block.  The row law gives

```
chi(p,q,q') = +1,
chi(p,q,r) = chi(p,q',r) = chi(q,q',r) = -1.
```

These are exactly the three edge tests placing q strictly inside triangle
`p q' r`.  Hence every intermediate block contributes at most one point.

This proves the proposed orientation (cap first, cup last).  The reversed
orientation is false in the exhaustive tests below.

## 4. Exact cell recurrence

Let `C(n,i)` count nonempty caps in `T(n,i)`.  In

`T(n,i)=A prec B`, with `A=T(n-1,i-1)` and `B=T(n-1,i)`,

a cap spanning A and B contains at most one B-point, since one A-point and two
B-points make a positive triple.  Conversely, every cap in A together with
one arbitrary B-point is a cap.  The cases wholly in A or wholly in B give the
exact recurrence

`C(n,i) = C(n-1,i) + (1+binom(n-1,i))*C(n-1,i-1)`.

The cup count is `U(n,i)=C(n,n-i)` by the symmetric recurrence (no coordinate
symmetry assumption is needed).

### Converse: every cap-left/cup-right union is convex

The converse needed to count convex subsets of one cell is also exact.  If
`T=A prec B`, X is a nonempty cap in A, and Y is a nonempty cup in B, then
`X union Y` is in convex position.

One transparent proof runs the monotone-chain hull algorithm.  On the upper
hull, every point of X is retained because triples in X and triples of type
`A,A,B` are negative.  As the points of Y are scanned, each previous Y-point
is popped because triples of type `A,B,B` and triples in Y are positive.  Thus
the upper hull is

`X union {rightmost point of Y}`.

On the lower hull, the negative turns pop all but the leftmost X-point, while
all Y-points are retained.  Thus the lower hull is

`{leftmost point of X} union Y`.

Their union is exactly `X union Y`, proving convexity.  This proof includes
all endpoint cases: a singleton is both a cap and a cup, and if X or Y is a
singleton the same hull description remains valid.

Let `W(n,i)` count nonempty convex subsets in `T(n,i)`.  The decomposition and
its converse give the exact recurrence

```
W(n,i) = W(n-1,i-1) + W(n-1,i)
         + C(n-1,i-1) U(n-1,i).
```

Direct enumeration agrees with this recurrence in every cell through `n=5`:

```
n=3:  1, 7,   7, 1
n=4:  1, 15, 50, 15, 1
n=5:  1, 31, 375, 375, 31, 1
```

It also agrees in the three nontrivial interior cells `i=2,3,4` at `n=6`:

```
i:          2     3     4
Cap:      266  1281  1051
Cup:     1051  1281   266
W:       2956 10951  2956
```

### Consequence for the central cell

For even `n=2m`, the product term in the central recurrence is exactly

`C(2m-1,m-1) U(2m-1,m) = C(2m-1,m-1)^2`.

On the other hand, the upper/lower-hull injection gives

`W(2m,m) <= C(2m,m)U(2m,m) = C(2m,m)^2`.

Therefore, once the exact cap recurrence has established

`log2 C(n,n/2) = (A(1/2)+o(1))n^2`,

the two displays squeeze the **actual**, not merely upper-bounded, central-cell
count to

`log2 W(n,n/2) = (2A(1/2)+o(1))n^2`.

For completeness, the needed cap asymptotic follows directly from the exact
recurrence, without a relaxation.  Unrolling it expresses `C(n,i)` as a sum
over `1 <= r_1 < ... < r_i <= n`, with path weight

`product_{j=1}^i (1+binom(r_j-1,j))`.

Every such sequence has `r_j <= n-i+j`, and every factor is nondecreasing in
`r_j`.  Thus the delayed path `r_j=n-i+j` is the largest one, giving

```
P(n,i) <= C(n,i) <= binom(n,i) P(n,i),
P(n,i) = product_{j=1}^i (1+binom(n-i+j-1,j)).
```

The logarithm of the multiplicative gap is only `O(n)`.  Stirling's formula
and a Riemann sum therefore give, for `i/n -> x`,

`log2 C(n,i)/n^2 -> A(x)`

with exactly the integral A used in the proposal.

The same argument works for either middle cell when n is odd.  Direct
integration gives

`A(1/2) = 1/2 - 1/(8 ln 2) = 0.319663119888880...`,

hence the central-cell rate is

`2A(1/2) = 1 - 1/(4 ln 2) = 0.639326239777759...`.

Since
`log2 binom(n,floor(n/2)) = n-o(n)`, this is also the coefficient of
`(log2 N)^2` for the number N of points in the central cell.

## 5. Why the row DP counts all convex subsets

For `k<l`, the decomposition gives at most

`C(n,k) U(n,l) product_{k<r<l} (1+binom(n,r))`

subsets whose first and last occupied blocks are k and l.

For `k=l`, let `V(n,k)` be the number of nonempty convex subsets inside the
cell.  Every such subset is uniquely determined by the pair (upper hull,
lower hull).  The upper hull is a cap and the lower hull a cup; therefore

`V(n,k) <= C(n,k) U(n,k)`.

Consequently the proposed bound, with an extra 1 for the empty set, is valid:

`1 + sum_{0<=k<=l<=n} C(n,k) U(n,l) product_{k<r<l}(1+binom(n,r))`.

The products deliberately overcount: not every formal cap/cup/singleton
choice is convex.  Overcounting is harmless for the desired upper bound.

## 6. Exact exhaustive results

All computations use `fractions.Fraction`; no floating-point orientation test
is used.

| row | points | convex subsets including sizes 0,1,2 | nontrivial (size >=3) | row bound | decomposition failures | reversed-orientation failures |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 8 | 131 | 94 | 201 | 0 | 2 |
| 4 | 16 | 2618 | 2481 | 3799 | 0 | 310 |
| 5 | 32 | 118241 | 117712 | 152699 | 0 | 33290 |

The `m=3,4` nontrivial counts reproduce the archived independent audit
exactly.  At `m=5` the size distribution is

```
size:   0   1    2     3      4      5      6  7
count:  1  32  496  4960  23220  49884  39648  0
```

For every cell through `m=5`, direct enumeration also agrees exactly with the
cap and convex-subset recurrences and verifies `V(n,i) <= C(n,i)U(n,i)`.

Reproduce with:

```
python3 phase2/loop/erdos838/agent_geometry/audit_geometry.py --m 3 4
python3 phase2/loop/erdos838/agent_geometry/audit_geometry.py --m 5 --max-subset-size 7
```

## Bottom line

No geometric counterexample was found.  With "sequential strong gluing" made
explicit and the one-block case separated, the geometry and row DP are
proof-complete.  Any remaining risk in the proposed `0.721347...` result lies
in the asymptotic analysis or prior-art/novelty claim, not in the geometric
decomposition.
