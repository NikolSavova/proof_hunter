# Erdős #791: second full-problem attack

Date: 2026-08-13

## Verdict

The normalized-limit problem is **not resolved**, and no published numerical
bound was improved.  This attack did, however, turn the two proposed closure
paths into exact theorems and expose their principal obstructions.

For

```text
R(k)=max{n: some |A|<=k has [0,n] subset A+A},
alpha_-=liminf R(k)/k^2,  alpha_+=limsup R(k)/k^2,
```

the strongest positive bridge is:

> If bases approaching `alpha_+` admit phased/carry role assignments of cost
> `k+o(k)`, then `alpha_-=alpha_+`.

This condition is real rather than vacuous: rolewise expansion of Kohonen's
certificate gives an infinite family

```text
k_t=42t+7,   role cost L_t=42t+8,   range >=510t^2+t-1,
```

so the defect is exactly one.  It only approaches the already known
`85/294`, not `alpha_+`.

The sharp obstruction is:

> If every tile clause contains a current pair and the current-role
> compatibility graph has chromatic number `r`, a near-lossless lift can
> exist only at density `c<=1/2-1/(4r)`.

The present five-role language has `r=4`, hence ceiling `7/16`.  A language
capable of handling the full presently allowed interval through `0.4585`
needs at least seven current-compatible colors, or must assemble blocks
nonlocally without a current-pair witness.

The analytic route also became precise.  Diffuse independent rounding leaves
a positive density of holes; aggregate residues remain relaxation-neutral
even at growing modulus; and exact no-slack microtiles form only complementary
pairs.  A correlated construction that clusters all holes into `o(k)` blocks
of length `o(k)` would nevertheless close the problem by an exact absorber.

## 1. Multitype amplification theorem

The elementary tiles are

```text
V=[0,t], H=t[0,t-1], S=(t+1)[0,t-1],
T0=(t-1)[0,t], T1=T0+1,
```

with even `t`.  A finite typed macro certificate of role cost `L` covering
`m` macro squares expands to a literal basis of size at most `L(t+1)` and
range at least `mt^2-1`.  Therefore

```text
alpha_- >= m/L^2.
```

If certificates supported on `k_r` distinct coordinates satisfy

```text
n_r/k_r^2 -> alpha_+,   L_r/k_r -> 1,
```

then taking the fixed-certificate bound for every `r` and then `r->infinity`
gives `alpha_- >= alpha_+`.  This proves equality.

The exact Kohonen rolewise expansion verifies that bounded role defect can
persist under scaling.  It has defect one and the formulas displayed in the
verdict; checks pass through even `t=20`, while the elementary interval
identity in the proof establishes every even `t`.

## 2. Unique-sum and chromatic obstruction

For a coordinate basis `C`, put an edge `{a,b}` in its unique-sum graph when
`a+b` is a required target and has no other unordered representation.
Deleting the coordinates with multiple roles leaves this graph colorable by
the current-role compatibility graph.  If the role defect is `d`, the number
`e` of unique off-diagonal edges therefore obeys

```text
e <= C(k,2)-C(k-d,2)+t_r(k-d),
```

where `t_r` is the exact Turan number.  Its leading term is
`(r-1)(k-d)^2/(2r)`.

Representation counting gives

```text
e >= 2(n+1)-C(k+1,2)-k.
```

Writing `n/k^2->c`, `d/k->x` yields

```text
2c-1/2 <= (r-1)/(2r)+x/r-x^2/(2r),
x >= 1-sqrt(2r(1-2c)) when the right side is positive.
```

For the current `K5-L0L1` interaction graph, `r=4`; near-lossless typing
forces `c<=7/16`.  At `c=0.4585`, this language would require at least
`0.185138... k` defect.

There is also a finite lower bound.  Every essential coordinate needs one
role, and a coordinate whose required double is represented only as `a+a`
needs a second role.  Thus role cost is at least

```text
number of essential coordinates + number of unique diagonal coordinates.
```

Every extremal basis is essential because `R(k)>R(k-1)`.  The bound is tight
for every extremal basis through `k=9`, but not universally sufficient:
`{0,1,3,4,5}` covers through 9, has only two unique diagonals, yet needs role
cost eight rather than seven.

A separate universal static-color conjecture is false.  The range-38 basis

```text
{0,1,2,3,4,9,14,17,18,24,28}
```

has a `K5` in its unique-sum graph on `{0,1,9,14,24}`.  The positive witness
is directly checked; CP-SAT found no such clique at any smaller range.

## 3. Exact carry triangle and its cost

The constructive lane found a genuine three-way carry tile.  For even `t`,
the three pair footprints

```text
H+S, H+T0, and a one-block shift of S+T0
```

cover one complete `t^2` block, in either carry orientation.  This adds exact
triangle clauses to the typed predicate, and 200 random macro-to-literal
checks at `t=2,4,6,8` pass.

It is not a free triangle.  The three footprints contribute exactly
`3t^2/2` incidences to cover `t^2` points, an overlap excess of `t^2/2`.
Consequently disjoint local triangle cells have at most `2/3` of their raw
edge capacity.  Exact cyclic searches through eight macro states are far
below the record.  A useful successor must share those duplicated half-blocks
across neighboring carry states; a Boolean macro-square model discards the
information needed to do this.

Triangle clauses do not lower the optimal role cost for any extremal basis
through `k=9` or for the tested published families.

## 4. Growing-scale analytic path

Four rigorous results delimit the rounding route.

1. **Independent-rounding barrier.**  With total expected size `k`, maximum
   diffuse selection probability tending to zero, and an `o(k)` deterministic
   core, the expected missed-target fraction is at least

   ```text
   exp(-1/(2c)).
   ```

   At `c=85/294` this is `0.177389...`.  With constant probability any repair
   needs `Omega(k)` new elements.  Thus ordinary sample/alter cannot close the
   limit.

2. **Growing aggregate residues are neutral.**  The convolution relaxation
   on `[0,1] x Z/qZ` has exactly the continuous relaxation constant for every
   `q`.  When `q=o(N)`, actual target mass is product-uniform up to normalized
   discrepancy `O(q/N)`.  Residues must therefore be coupled to differences,
   collisions, or carry position; aggregate modular mass alone adds nothing.

3. **Mesoscopic absorber.**  If holes lie in `b` aligned blocks of length
   `L`, adjoining `[0,L-1]` and the `b` block starts repairs everything at
   cost at most `L+b`.  Producing `L=o(k)` and `b=o(k)` along an
   `alpha_+`-approaching construction would prove `alpha_-=alpha_+`.

4. **Exact microtile factorization.**  If two `q`-element integer tiles have
   a cross-sum containing `q^2` consecutive values, their normalized
   polynomials multiply to `1+z+...+z^{q^2-1}`.  Squarefreeness gives every
   normalized tile at most one complementary partner and no self-partner;
   the exact interaction graph is a matching.  For prime `q` this specializes
   to the standard fine interval/coarse progression pair.  Thus exact
   no-slack many-direction microtiles cannot escape the bipartite `1/4`
   barrier.  Approximate tiles and adjacent-carry splits remain open.

## 5. Exact computation

The exact fixed-coordinate optimizer channels every role and pair-sum
variable in both directions and independently verifies decoded coverage.

- Every interval-range extremal basis was exhaustively enumerated through
  `k=9`.  For `k=9`, `3,365,856` candidates exclude range 33 and exactly two
  bases attain range 32.  Both have optimal role cost `13=k+4`.
- Among extremizers at every `k=4,...,9`, the best cost is `k+4`.  One `k=8`
  extremizer needs `16=2k`; a compressed proof trace certifies that cost at
  most 15 is impossible.
- Kohonen's 41-coordinate macro union has exact minimum role cost 42 in the
  three-tile, five-list, and triangle-enhanced models.
- Published restricted/global diagnostics through cardinality 41 reinforce
  that bounded defect is a property of structured bases, not all bases.

These finite facts are lemma-discovery evidence and exact scoped results;
they are not asymptotic extrapolations.

## 6. What remains most hopeful

### A. Point-footprint carry automaton with at least seven current colors

This is the strongest constructive route.  The new triangle supplies a real
quadratic interaction, while the chromatic theorem specifies what the next
language must achieve.  Search states should own the two parity triangles
inside each macro block and allow neighboring cells to reuse the exact
`t^2/2` overlap.  A seven-color current graph would clear the entire known
upper interval; a nonlocal automaton could evade the chromatic hypothesis.

### B. Approximate microtile factorization plus mesoscopic absorption

Prove a stability theorem for `q+o(q)` tiles whose pair sums cover almost all
of a `q^2` block, including how their missing regions transfer across a carry.
If a correlated tiling makes the residual holes occupy only `o(k)` short
blocks, the absorber closes the problem.  Exact tiles, independent rounding,
and aggregate residues are now rigorously excluded, so the lemma must use
both slack and carry geometry.

### C. Structured near-lossless typing below `7/16`

Kohonen gives an exact scalable defect-one example at `85/294`, and small
extremizers have a best defect of four through `k=9`.  A theorem selecting
limsup-extremal bases with sublinear unique-diagonal/temporal defect would
close the limit if `alpha_+<=7/16`.  Without such an analytic upper bound,
the present five-role language cannot cover the high-density case.

The first two routes are therefore the true full-interval attacks.  The third
is a cleaner conditional route and a source of structural conjectures.

## Verification map

- `primal/AMPLIFIER_RESULT.md`: typed closure theorem, scalable Kohonen
  expansion, chromatic obstruction, carry triangle, and exact scope.
- `analytic/ROUNDING_AND_TILING.md`: rounding barrier, growing residues,
  absorber, and microtile factorization.
- `computation/EXTREMAL_ROLE_RESULTS.json`: all extremizers through `k=9`.
- `computation/K9_ENUMERATION_RESULT.json`: exhaustive `R(9)=32` census.
- `computation/STRUCTURAL_BOUND_AUDIT.json`: essential-plus-diagonal bound.
- `computation/KOHONEN_MACRO_ROLE_RESULTS.json`: exact macro optima.
- `computation/K8_DRAT_AUDIT.json`: proof-producing ordinary five-list lower
  bound, hashes, and exact scope.
- `ROLE_DEFECT_NOTES.md`: finite patterns and counterexamples.
- `UNIQUE_K5_SEARCH.json`: checked `K5` witness and finite search.
- `AUDIT.md`: independent theorem-by-theorem audit.

No unconditional resolution or numerical record is claimed.
