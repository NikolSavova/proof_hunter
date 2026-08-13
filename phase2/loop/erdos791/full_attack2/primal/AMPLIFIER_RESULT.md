# Erdős #791 full attack 2 — multitype amplifier bridge

## Verdict

No lower-bound improvement was obtained.  The sharpest outcome is an exact
conditional closure criterion, together with a broad obstruction to it.

Let `alpha_-` and `alpha_+` be the liminf and limsup of `n(k)/k^2`.  If a
limsup-extremal sequence of finite bases admits phased role assignments of
cost `k+o(k)`, then the typed substitution below proves

```text
alpha_- = alpha_+.
```

Thus a near-lossless role assignment would resolve Erdős #791, not merely
improve the constructive constant.  On the other hand, in the full phased
language, including the new triangle clauses, a unique-sum/Turán argument
proves that such assignments are impossible whenever `alpha_+>7/16`.  More
precisely, a density-`c` coordinate basis with role defect `delta` must satisfy

```text
delta/k >= 1-sqrt(8-16c)-o(1)       when c>7/16.          (0)
```

The other main positive result is the missing genuinely quadratic **carry
triangle** among `H,S,T0`.  It is exact, but intrinsically lossy locally: its
three useful pair shapes contribute `3t^2/2` point-incidences to cover one
`t^2` square, so exactly `t^2/2` incidences are duplicated.

This narrows the amplifier bridge substantially:

- `k+o(k)` typed cost is now an exact full-closure target;
- the target is ruled out by unique-sum density if `alpha_+>7/16`;
- triangle-free typed amplifiers were already bounded by `1/4`;
- a real triangle now exists, but it pays an exact `3/2` local incidence cost;
- cyclic and direct-AP macro attempts did not turn that triangle into a
  competitive integer initial-interval lift;
- any successful amplifier must amortize the overlap by sharing the duplicated
  portions with neighboring macro squares, not count the triangle locally.

As always, improving the construction-side constant alone would not resolve
the full Erdős problem.

## 1. Typed substitution and full-closure corollary

Let `t` be even, `B=t^2`, and

```text
V  = [0,t],
H  = {it       : 0<=i<t},
S  = {i(t+1)   : 0<=i<t},
T0 = {i(t-1)   : 0<=i<=t},
T1 = T0+1.
```

For finite macro sets `I,J,K,L0,L1`, define

```text
A_t=(V+B I) union (H+B J) union (S+B K)
    union (T0+B L0) union (T1+B L1).
```

Its role cost is

```text
L=|I|+|J|+|K|+|L0|+|L1|,
```

and `|A_t|<=L(t+1)`.  Each ordinary phased macro clause in
`typed_predicate.py` certifies a full `B`-square.  The carry-triangle lemma
below adds two further clauses.  Therefore, if the enlarged predicate covers
macro squares `0,...,m-1`, then

```text
[0,m t^2-1] subset A_t+A_t,
liminf n(k)/k^2 >= m/L^2.
```

This is the requested exact macro-to-literal bridge for any finite typed/carry
certificate.  It is sufficient, not necessary.

The evenness restriction on `t` causes no asymptotic gap.  For a fixed
certificate and arbitrary large target cardinality `K`, choose the largest
even `t` with `L(t+1)<=K` and pad the constructed basis if necessary.  Then

```text
n(K)/K^2 >= ((m t^2)-1)/K^2 -> m/L^2.
```

Consequently every one finite certificate proves

```text
alpha_- >= m/L^2.                                      (1)
```

### Full-closure corollary

Suppose there are active coordinate sets `C_r`, `|C_r|=k_r`, and phased typed
certificates supported on `C_r` which cover `[0,n_r]`, have role costs `L_r`,
and obey

```text
n_r/k_r^2 -> alpha_+,       L_r/k_r -> 1.
```

Apply (1) to each fixed `r` and then let `r` tend to infinity:

```text
alpha_- >= limsup_r (n_r+1)/L_r^2 = alpha_+.
```

The reverse inequality is automatic, hence the limit exists.  This is the
precise multitype amplifier bridge requested in this lane.

For comparison, every ordinary additive basis `C`, `|C|=k`,
`[0,n] subset C+C`, has the universal but lossy assignment

```text
I=J=C, K=L0=L1=empty.
```

It has `L=2k`, certifies `m=n+1`, and therefore gives only
`(n+1)/(4k^2)`.  `cross_cover_amplifier.py` constructs and literally checks
this `V/H` lift.  The entire problem is removing that factor-four role loss.

### An exact scalable bounded-defect family (but only at known density)

Kohonen's published placement itself expands to a structured sequence meeting
the desired role-cost condition.  Retain the inherited role while replacing
each macro coordinate by its elementary segment at an even scale `t`.  The
expanded coordinate union has

```text
k_t=42t+7,       L_t=42t+8=k_t+1.
```

The ordinary typed predicate certifies at least

```text
m_t=510t^2+t
```

macro unit squares.  The first `510t^2` follow by substituting the original
`42/510` certificate.  The extra `t` are also transparent: the terminal
placement pair `137 in I`, `372 in K` has sum `509`, and

```text
[0,t]+{i(t+1):0<=i<t}=[0,t^2+t-1].
```

Thus its `I+K` pair alone extends the final block through `510t^2+t-1`.
Role defect one is therefore rigorously scalable, not a one-off feature of
the 41-coordinate macro union.  However

```text
m_t/k_t^2 -> 510/42^2=85/294,
```

which is only the known lower-bound density.  The full-closure corollary
needs such bounded/sublinear defect on a sequence approaching `alpha_+`.
`kohonen_role_expansion.py` verifies the exact predicate and size formulas
for every even `t<=20`; the displayed elementary argument proves the scalable
formulas for all even `t`.

## 2. Unique-sum role-defect obstruction

Let `C` be the union of all active macro coordinates in a phased certificate,
`|C|=k`, and suppose it certifies `[0,n]`.  The role cost is `L=k+delta`.
For each `q<=n` having a unique unordered representation

```text
q=a+b,  a<b,  a,b in C,
```

put the edge `{a,b}` in the unique-sum graph `G`.

Every phased coverage clause, including both triangle orientations, contains
a **current** pair sum at `q`.  Its two roles form an edge of

```text
K_5 minus the edge L0--L1.
```

Indeed the possible current types are

```text
IJ, IK, IL0, IL1, JK, JL0, JL1, KL0, KL1.
```

Delete from `C` every coordinate carrying two or more roles.  There are at
most `delta` such coordinates.  On the remaining unique-sum graph, each
coordinate has one role; merging the nonadjacent colors `L0,L1` yields a
proper four-coloring.  Hence deleting at most `delta` vertices makes `G`
four-colorable.

If `d` vertices are deleted from a `k`-vertex graph with this property, its
number `e` of edges satisfies the exact bound

```text
e <= C(k,2)-C(k-d,2) + floor(3(k-d)^2/8).               (2)
```

The first term counts every possible edge incident to a deleted vertex; the
last term is the exact four-partite Turán bound on the remainder.

There are at most `C(k+1,2)` unordered pairs in total.  If `u` target sums
have unique representations, counting one representation for a unique sum
and at least two for every other target gives

```text
u >= 2(n+1)-C(k+1,2).
```

At most `k` of these are diagonal, so

```text
e >= 2(n+1)-C(k+1,2)-k.                                (3)
```

Combining (2)--(3), writing `n/k^2->c` and `delta/k->x`, gives

```text
2c-1/2 <= 3/8+x/4-x^2/8.
```

In particular `x=o(1)` forces `c<=7/16`; solving the quadratic above
`7/16` gives (0).  At the published upper endpoint `c=0.4585`, the necessary
defect fraction is at least `0.185138...`.  This does not rule out a
record-beating amplifier: the available defect headroom there is
`sqrt(c/(85/294))-1=0.259313...`.  It does rule out the exact near-lossless
closure route in the high-`alpha_+` regime.

Diagonal unique sums give a second, simpler obstruction: if `2a<=n` is
represented only by `a+a`, then `a` itself must carry at least two distinct
roles.  `role_defect_obstruction.py` computes the actual unique graph, (2),
and the representation-count lower bound (3) for any supplied coordinate
basis.

This diagonal count is only a lower bound, not a formula for the optimum.
The exact counterexample `C={0,1,3,4,5}`, target `[0,9]`, has two unique
diagonal vertices but triangle-enabled optimum role cost `8=k+3`, strictly
larger than `k+2`.  Conversely, the audited restricted-AP family at
cardinalities `15,...,21` has eight unique diagonal vertices and optimum
exactly `k+8`, while Kohonen's `k=41` macro union has defect only one.  The
evidence supports an existential **structured** bounded-defect family; it
does not support a theorem that every additive basis has cost `k+O(1)` or
that diagonal uniqueness is the only obstruction.

### General chromatic obstruction and tile-design target

The same proof is not special to these five roles.  Suppose every coverage
clause of a typed amplifier contains a current pair and the graph of
current-compatible roles has chromatic number `r`.  After deleting at most
`delta` multiply-typed coordinates, composition with an `r`-coloring makes
the unique-sum graph `r`-colorable.  Turán's theorem replaces (2) by

```text
e <= C(k,2)-C(k-d,2)+t_r(k-d),                          (4)
```

Here `t_r(N)` is the exact Turan number.  If `N=ar+s`, `0<=s<r`, then

```text
t_r(N)=(N^2-[s(a+1)^2+(r-s)a^2])/2.
```

For fixed `r`, its leading term is `(r-1)N^2/(2r)`.

Consequently

```text
2c-1/2 <= (r-1)/(2r)+x/r-x^2/(2r),
x >= 1-sqrt(2r(1-2c))             when this is positive. (5)
```

In particular, near-lossless typing forces

```text
c <= 1/2-1/(4r).                                       (6)
```

The scope matters: this does not cover a point-footprint construction whose
square is assembled solely from past and future partial pieces, with no
current pair governed by one fixed compatibility graph.

Here the compatibility graph is exactly `K5-L0L1` and has chromatic number
four: `I,J,K,L0` form a `K4`, while `L0,L1` can be merged.  Formula (6) gives
`7/16`.  To leave near-lossless typing unobstructed all the way through the
published upper endpoint `0.4585`, a future tile language needs

```text
r >= 7
```

current-compatible colors, or it must escape the current-pair hypothesis.
This is a precise target for a genuinely stronger multitype amplifier.

### A structured sufficient condition

There is also an exact positive formulation.  If one can choose, for every
`q<=n`, a representation edge from `C+C` so that the chosen graph is
bipartite, then color its two parts `I,J`; duplicating the vertices used by
diagonal chosen representations gives a direct `I+J` certificate.  Its cost
is

```text
k + number of duplicated diagonal vertices.
```

Thus a sequence with a bipartite representation selection and `o(k)` needed
diagonal vertices satisfies the full-closure corollary.  This is a concrete
structured condition on arbitrary/limsup-extremal bases.  The dense
unique-sum graph is the obstruction to finding it.

## 3. Exact `H-S-T0` carry triangle

Put

```text
P_HS=H+S, P_HT=H+T0, P_ST=S+T0, Q=[0,B-1].
```

For every even `t`, both

```text
P_HS union P_HT union (P_ST+B) contains Q+B,             (A)
(P_HS+B) union (P_HT+B) union P_ST contains Q+B.         (B)
```

These are genuine triangles: all three pair types `HS`, `HT`, and `ST` are
needed with quadratic footprint.  At the macro level, square `q` is therefore
certified by either

```text
q in J+K and J+L0, q-1 in K+L0;                           (A')
q-1 in J+K and J+L0, q in K+L0.                           (B')
```

`triangle_predicate.py` implements exactly these clauses.

### Proof of (A) and (B)

Write `x=at+b` with `t<=a<=2t-1` and `0<=b<t`.

- If `a-b<=t-1`, choose `i=a-b`, `j=b`; then
  `x=it+j(t+1) in H+S`.
- If `a+b<=2t-2`, choose `i=a-t+b+1`, `j=t-b`; then
  `x=it+j(t-1) in H+T0`.
- Otherwise `a-b>=t` and `a+b>=2t-1`.  Put `c=a-t`.  Then
  `c>=b` and `c+b>=t-1`.  If `c+b` is even, take

  ```text
  i=(c+b)/2, j=(c-b)/2.
  ```

  If it is odd, take

  ```text
  i=(c+b+1-t)/2, j=(c+t-b+1)/2.
  ```

  The inequalities put `0<=i<t`, `0<=j<=t`, and in either case
  `x-B=i(t+1)+j(t-1)`.  This proves (A).

For (B), write `x-B=ct+b`, `0<=c,b<t`.  The lower square is covered by
`H+S` when `c>=b`, and by `H+T0` when `b=0` or `c+b>=t-1`.  If neither holds,
then `b>c` and `c+b<=t-2`.  If `t+c+b` is even, take

```text
i=(t+c+b)/2, j=(t+c-b)/2;
```

otherwise take

```text
i=(c+b+1)/2, j=(2t+c-b+1)/2.
```

The same bounds give `x=i(t+1)+j(t-1)`, hence `x in S+T0`.  This proves
(B).

The algebra in the last bullet is the same two-parity calculation used for
the reflected-diagonal lemma.  `triangle_lemma.py` checks the exact inclusion,
including both carry orientations, for every even `t<=100`; all pass.

There is also an entirely independent end-to-end audit:
`test_triangle.py` generates 200 random typed macro placements and checks
every abstractly certified square against the literal integer sumset at
`t=2,4,6,8`.  All pass.

## 4. Exact local overlap obstruction

The triangle is not a free three-edge amplifier.  Intersect the three shapes
in (A) with the target square `Q+B`.  Direct digit counting gives

```text
|P_HS intersect (Q+B)|       = t(t-1)/2,
|P_HT intersect (Q+B)|       = t(t-1)/2,
|(P_ST+B) intersect (Q+B)|   = t(t+2)/2.
```

These are injective pair counts.  In `H+S`, reduction modulo `t` recovers
the `S` index, and membership in the upper square is equivalent to
`i+j>=t`; this gives `t(t-1)/2` pairs.  In `H+T0`, reduction modulo `t`
recovers the `T0` index on the relevant range (the only possible endpoint
ambiguity uses the excluded zero index), and the condition is `i+j>=t+1`;
again the count is `t(t-1)/2`.  For `S+T0`, even `t` gives
`gcd(t-1,t+1)=1`, and the allowed index ranges make the sum map injective.
The sums below `B` are the `t(t+1)/2` pairs with `i+j<=t-1`, together with
the `t/2` pairs satisfying `i+j=t` and `i<j`, for `t(t+2)/2` total.

Their union is all `t^2` target points, but their sizes sum to

```text
3t^2/2.
```

Thus the exact overlap excess is

```text
3t^2/2-t^2=t^2/2.                                      (C)
```

This is macroscopic, not a boundary error.  `triangle_overlap_audit.py`
checks all formulas through `t=100`.

Consequences:

1. A pair-count argument assigning one whole square to every `HS`, `HT`, and
   `ST` pair overcounts triangle capacity by a factor `3/2` locally.
2. Any amplifier based on disjoint triangle cells has effective output at
   most `2/3` of its raw three-edge incidence count.
3. For balanced type masses, raw triangle edge count is at most `L^2/3`, so
   the disjoint-cell interpretation gives at most `2L^2/9`, below even `1/4`.

The third statement is scoped to disjoint/local triangle cells.  Neighboring
cells might reuse the overlap portions, which is exactly the remaining
possibility.

## 5. Why the naive amplifier bridge fails

Suppose one tries to type an arbitrary macro additive basis `C` by assigning
each occurrence one of `H,S,T` and to replace every representation
`q=c+c'` by a triangle cell.  There are two obstacles.

### Role duplication

One triangle cell requires three simultaneous macro equalities:

```text
j+k=q,
j+l=q,
k+l=q-1
```

or the reverse-carry version.  Solving these equations gives

```text
j=(q+1)/2, k=l=(q-1)/2
```

in the first orientation.  Thus it is not obtained from one arbitrary
representation of `q`; it requires a rigid midpoint/carry relation among
three typed placements.  Generic bases do not supply this relation for a
positive density of `q`.

### Footprint loss

Even when the equalities exist, equation (C) shows that half a square's worth
of point-incidences is duplicated.  The loss is order `t^2`, so it survives
the amplifier limit and cannot be hidden in the `o(q)` term.

Therefore the hoped-for statement

```text
"each macro representation becomes one independent full-square typed edge"
```

is false for the `H-S-T` triangle.  A valid amplifier theorem must track
footprint ownership across adjacent carry states.

## 6. Exact small extremal role audit with triangles

`triangle_role_batch.py` re-optimizes every interval-range extremal basis for
`1<=k<=8` with both carry-triangle clauses enabled.  Every result is CP-SAT
`OPTIMAL`, then independently checked by `triangle_predicate.py` and by
literal expansion at `t=2,4`.

The triangle clauses do **not** reduce any optimum.  In particular, among the
extremal bases at each `k=4,5,6,7,8`, the best role cost remains exactly

```text
k+4.
```

Some extremal bases require still more (one `k=8` basis costs `16`).  In
contrast, the union of Kohonen's published macro lists has `k=41`, range
`509`, and typed cost `42=k+1`.  This shows bounded defect is structurally
possible at useful density, but the small extremal data do not support a
general `k+O(1)` theorem.

The exact output is `TRIANGLE_ROLE_RESULTS.json`.

## 7. Periodic/cyclic macro search

`triangle_cycle_search.py` exhausts `J,K,L subsets Z_n` for `2<=n<=8` under
the two exact triangle clauses.  It minimizes role cost `|J|+|K|+|L|`.
The best densities `n/L^2` are:

```text
n:       2      3      4      5       6       7       8
best:  .2222  .1200  .1600  .1389   .1667   .1429   .1633
```

These are far below `85/294`.  This is only a finite cyclic diagnostic, not an
integer nonexistence theorem: wraparound does not certify an initial interval.
It nevertheless shows that the smallest finite-state triangle cycles have
poor role efficiency even before paying for an integer lift.

Direct three-AP macro searches were likewise weak: the best consecutive
triangle interval in the bounded sweep had density `0.12`.  This output was
used diagnostically and is not claimed as an exhaustive theorem.

## 8. Remaining amplifier target

What is now closed:

- the exact implication `near-lossless limsup typing => alpha_-=alpha_+`;
- near-lossless phased typing when `alpha_+>7/16`;
- triangle-free role graphs (`<=1/4`, previous lane);
- treating the new triangle as three independent full-square pairings;
- disjoint/local triangle-cell tilings;
- the smallest cyclic finite-state triangle templates;
- any arbitrary-basis typing argument that assumes one macro representation
  automatically yields the three midpoint/carry equalities.

What remains open:

- in the regime `alpha_+<=7/16`, a representation-selection theorem giving
  phased role defect `o(k)` for a limsup-extremal sequence;
- in the high-density regime, an amplifier whose current-role compatibility
  is not four-colorable, thereby escaping the unique-sum obstruction;
- a periodic carry complex in which the `t^2/2` overlap excess from one
  triangle is precisely the missing portion of adjacent triangles;
- a typed base with a positive density of midpoint/carry triples and bounded
  size gaps;
- a nonlocal ownership proof assigning literal points, rather than whole
  macro squares, across a triangle lattice.

The next constructive search should work at the **point-footprint automaton**
level.  A macro Boolean SAT model loses the critical overlap information.  Its
state must record which of the two parity triangles in a square have already
been supplied by neighboring `HS`, `HT`, and `ST` cells.

No construction-side record or full resolution is claimed.

## Reproduction

```bash
cd phase2/loop/erdos791/full_attack2/primal

python3 triangle_lemma.py --through 100
python3 triangle_overlap_audit.py --through 100
python3 triangle_cycle_search.py --through 8
python3 -m unittest -v test_triangle.py
python3 cross_cover_amplifier.py 0 1 3
python3 role_defect_obstruction.py 0 1 3
../../../../../problem-id/.venv/bin/python triangle_role_batch.py --seconds 30
python3 -m unittest -v test_obstruction.py
python3 kohonen_role_expansion.py --through 20
```
