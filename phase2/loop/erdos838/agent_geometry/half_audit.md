# Independent audit of `proof_blowup_half.md`

## Verdict

I find no mathematical defect in the vertical lexicographic blow-up theorem.
The four orientation rules are simultaneously realizable over the rationals;
the necessity and sufficiency parts of the convex-subset classification are
correct; and the three substitution formulas follow exactly, including all
two-block and singleton endpoint cases.  The fixed-template asymptotics and
the passage from powers to arbitrary `N` are also sound.

The claim should nevertheless remain a candidate result until the prior-art
sweep is complete.  Two small exposition repairs would make the proof harder
to misread:

1. In the realizability paragraph, explicitly choose a **rational** epsilon
   below the finite determinant threshold.  Continuity first gives a real
   interval, and density of the rationals gives the claimed exact rational
   realization.
2. In the converse classification, add that a strict cap and a strict cup
   with the same left and right endpoints lie respectively above and below
   their common chord.  Hence the two constructed monotone chains do not
   cross and really are the two boundary chains of a convex polygon.

The proposed matching lower coefficient `1/2` for *all* binary strongly
decomposable trees is not proved here.  I obtained a rigorous cap--cup product
lower bound with coefficient `1/2`, but converting that product mass into
the correctly oriented cross terms in `W` remains the decisive obstruction.
An exact Pareto search through 19 leaves found no counterexample.

## 1. Exact rational realizability

Assume `S=(s_i)` and `Q=(q_j)` have rational coordinates strictly increasing
in both x and y.  This assumption costs nothing: if x is strictly increasing,
an integer shear `(x,y) -> (x,y+Mx)` with sufficiently large integer M makes
y strictly increasing and preserves every determinant.

For

```
p_(i,j) = (X_i + eps^2 x_j, Y_i + eps y_j),
```

the four determinant classes are as follows.

* One block: the determinant is `eps^3` times the determinant in Q.
* Three blocks: its limit at `eps=0` is the nonzero determinant in S.
* First two points in one block: the leading term is
  `-eps Delta_y(Q) Delta_x(S)`, so its sign is negative.
* Last two points in one block: the leading term is
  `+eps Delta_x(S) Delta_y(Q)`, so its sign is positive.

There are finitely many triples and finitely many strict x/y inequalities.
Thus all desired signs and coordinate orders hold throughout some interval
`0<eps<eps_0`.  Choosing a rational epsilon in that interval gives exact
rational coordinates and no collinear triple.  Since the output again has
rational coordinates increasing in x and y, the argument iterates without
any hidden compactness or limiting construction.

## 2. Necessity of the convex-subset classification

Let a convex subset X meet at least two macro-blocks.  Write `B_1,...,B_j`
for its occupied blocks in increasing order.

### First endpoint is a cap

The lower hull of X is a cup.  If it contained two selected points from the
first block and any later selected point, that triple would be negative by
the same-block rule, contradicting the cup condition.  Both hull chains share
the leftmost selected point, so the lower hull contains exactly that one
first-block point.  Every other selected point in the first block must lie on
the upper hull.  Therefore the whole first-block intersection is a cap.

The reflected argument says the last-block intersection is a cup.

### An intermediate block contributes at most one point

Suppose `a<b_1<b_2<c` are selected, with `b_1,b_2` in one intermediate
block and a,c in earlier/later blocks.  The triples `(a,b_1,c)` and
`(a,b_2,c)` have the same macro orientation, so `b_1,b_2` are on the same
side of line ac.  Meanwhile

```
chi(a,b_1,b_2)=+,    chi(b_1,b_2,c)=-.
```

If both points are above ac, convexity of the four-set would put both on its
upper chain and require the first sign to be negative.  If both are below,
they lie on its lower chain and the second sign must be positive.  Both cases
contradict the displayed signs.  Since every subset of a convex-position set
is again in convex position, X cannot contain such a pair.

### The occupied macro-set is convex

Choose one selected representative from every occupied block.  These points
form a subset of X and hence are in convex position.  All their blocks are
distinct, so their order type is precisely that of the corresponding subset
of S.  Thus the occupied block indices form a convex subset of S.  This also
covers the vacuous two-block case.

## 3. Sufficiency, including endpoint exceptions

Let B be a convex macro-subset with at least two points.  Choose a nonempty
cap E in its first block, a nonempty cup F in its last block, and one arbitrary
point in each other occupied block.

Take the upper macro-chain of B.  Replace its first endpoint by the entire cap
E and its last endpoint by the rightmost point of F.  Every triple in the
result is negative:

* triples inside E are negative;
* two points of E followed by a later point are negative;
* all remaining triples inherit a negative upper-chain macro triple.

This is a cap.  Dually, the leftmost point of E, the lower macro-chain, and
the whole cup F form a cup.  They share exactly the global left and right
endpoints (apart from the harmless degeneracies when E or F is a singleton).
A strict cap lies above its endpoint chord and a strict cup lies below it, so
the chains cannot cross.  Their union contains every selected point and is in
convex position.

Singletons are both caps and cups, so there is no missing endpoint case.
When B has exactly two points the same proof reduces to the earlier
strong-glue fact: every nonempty cap in the left block union every nonempty
cup in the right block is convex.

The data of a spanning convex set recover B, E, F, and all intermediate
points uniquely.  Consequently the formula

```
W(S[Q]) = |S| W(Q)
          + C(Q) U(Q) sum_{j>=2} v_j(S) |Q|^(j-2)
```

is exact.  The cap and cup classifications give the other two exact formulas
in the draft.

## 4. Independent finite census

The script `audit_blowup_classification.py` performs a direct exact test that
is separate from the endpoint-chain counter used by the main artifact.  Its
macro skeleton is the rational four-point set

```
(0,0), (1,11), (2,23), (4,40),
```

whose second point is interior to the triangle formed by the other three
before the orientation-preserving shear.  Thus the test genuinely rejects a
nonconvex four-block macro-set.  The same set is used as the micro-set; it has
both cap and cup triples.  With `eps=1/128`, all `2^16` subsets of the exact
rational composition are enumerated.

Result:

```
spanning convex subsets: actual = classified = 3146
classification failures: 0
converse failures:        0
(C,U,W):                  (988, 484, 3202)
```

Reproduce with

```
python3 phase2/loop/erdos838/agent_geometry/audit_blowup_classification.py
```

The existing independent 36-point endpoint DP additionally reproduces
`(C,U,W)=(14136,14136,441399)` for `T(4,2)[T(4,2)]`.

## 5. Audit of the fixed-template asymptotics

For a fixed r-point template S, put `n=|Q|`.  The cap multiplier in (2) is a
positive polynomial of degree `a-1`, and the cup multiplier has degree
`b-1`.  At iteration t, `log n=t log r`; summing those linear increments gives

```
log C_d = (a-1)(log r)d^2/2 + O_S(d),
log U_d = (b-1)(log r)d^2/2 + O_S(d).
```

The extra macro-convex polynomial in the W recurrence has fixed degree, so it
contributes only `O_S(d)` to the logarithm of a cross-block summand.  The last
such summand dominates on the quadratic scale.  Conversely `v_2(S)>0`, so
that last summand is at least a positive constant times `C_{d-1}U_{d-1}`.
This verifies equality (7), not just the upper bound.

For the central Pascal template, largest cap and cup sizes are both `k-1`
and its size is `binom(2k-4,k-2)`.  The cap--cup theorem gives the matching
fixed-template obstruction

```
r <= binom(a+b-2,a-1) <= 2^(a+b-2).
```

Thus every fixed template has coefficient at least `1/2`, and the balanced
templates approach it.  Deleting from the least power `r^d>=N` changes
`log N` by only `O_S(1)` and cannot create convex subsets, so the arbitrary-N
step is valid.  Taking the infimum of the resulting bounds over fixed k is
also legitimate.

## 6. Attack on the lower bound for all strong decomposition trees

For a binary strong glue `T=A prec B`, let `a=|A|`, `b=|B|`.  The exact
nonempty-subset recurrences are

```
C(T) = C(B) + (b+1)C(A),
U(T) = U(A) + (a+1)U(B),
W(T) = W(A) + W(B) + C(A)U(B).
```

### A rigorous product-mass lower bound

Put `R(T)=sqrt(C(T)U(T))`.  Cauchy--Schwarz applied to the two displayed sums
for C and U gives

```
R(T) >= sqrt(b+1) R(A) + sqrt(a+1) R(B).          (L1)
```

This already forces the conjectured `1/2` coefficient in the *product* CU.
Here is a short proof with an explicit error term.  Starting at T, repeatedly
follow the larger child.  If the current subtree has m leaves, write s for
the smaller-child size and m' = m-s for the followed child.  Thus
`1<=s<=m/2`.  Iterating (L1) along this path gives

```
log R(T) >= (1/2) sum log(s+1).                   (L2)
```

Put `d=log(m/m')`, so `0<d<=1`.  The elementary inequality

```
log(s+1) >= d (log m - 1)                         (L3)
```

follows as follows.  We have
`d=-log(1-s/m)<=2s/m`.  For `x=m/2>=1` and `0<=d<=1`, convexity in d gives
`x^d<=1+d(x-1)<=s+1`, which is (L3).  If the successive logarithmic sizes are
`t_i=log m_i`, then `d_i=t_i-t_{i+1}`, `sum d_i=log n`, and

```
sum d_i t_i
 = ((log n)^2 + sum d_i^2)/2
 >= (log n)^2/2.
```

Substituting in (L2) yields

```
log R(T) >= (log n)^2/4 - (log n)/2,
C(T)U(T) >= 2^((log n)^2/2-log n).                (L4)
```

All logs here are base 2.  This is sharp in its quadratic coefficient for the
iterated balanced templates in the upper construction.

### Why (L4) does not yet prove the W lower bound

The cross term at a node is the **oriented** product `C(A)U(B)`.  Formula
(L4) controls the unoriented products `C(A)U(A)` and `C(B)U(B)`.  The mass can
be oppositely aligned: A may be cup-rich and B cap-rich, making the desired
cross term small even though both within-child products are large.  In that
case `W(A)+W(B)` is large, but I do not yet have an induction that recovers
the whole `1/2` coefficient without losing a constant fraction at repeated
misaligned nodes.

Using only `W>=max(C,U)>=sqrt(CU)`, (L4) recovers coefficient `1/4`, not
`1/2`.  Therefore a claimed proof that stops at the product inequality is
incomplete.  What is still needed is an alignment/partition-function lemma
showing that either enough `C(left)U(right)` mass occurs, or the recursively
misaligned child W-mass already pays the same quadratic entropy cost.

### Counterexample search

`decomposable_dp.py` computes the exact nondominated `(C,U,W)` frontier;
coordinatewise dominance is safe because all three recurrences are
monotone.  Exhaustion completed through n=19.  Selected minima, counting the
empty set in the displayed W, are

| n | minimum W | `log W/(log n)^2` |
|---:|---:|---:|
| 8 | 121 | 0.768763 |
| 12 | 543 | 0.706881 |
| 16 | 1758 | 0.673732 |
| 19 | 3801 | 0.659032 |

No finite counterexample to coefficient `1/2` appears.  A multiobjective
beam continuation gave rates `0.6268` at n=32 and `0.5924` at n=64, but that
part is heuristic and is evidence only.  The data are consistent with a
limit of `1/2`, while also showing that convergence is slow.

## Bottom line

The upper coefficient `1/2` proof survives the geometric, combinatorial,
rational-realizability, and asymptotic audits.  The matching lower bound for
arbitrary strongly decomposable trees remains a real theorem-sized gap.  The
new bound (L4) isolates it cleanly: total cap--cup partition mass already has
the right coefficient, and only its left-cap/right-cup alignment with the W
recurrence is missing.
