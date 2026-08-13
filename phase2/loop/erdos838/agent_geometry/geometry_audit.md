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
cap recurrence and verifies `V(n,i) <= C(n,i)U(n,i)`.

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
