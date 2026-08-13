# Role defect, unique diagonals, and the surviving existential bridge

## Exact observation

For an interval basis `A` covering `[0,n]`, let

```text
u(A,n)=#{a in A: 2a<=n and 2a has only the representation a+a}.
```

Every such coordinate must carry at least two elementary-tile roles in the
phased five-list language, so every typed certificate has role cost at least
`|A|+u(A,n)`.

Exact CP-SAT optimization gives equality in all of the following data:

- every interval-range extremal basis with `1<=|A|<=9`;
- the two published global cardinality-11, range-46 bases;
- the published extremal restricted bases tested at cardinalities 9 through
  21;
- Kohonen's macro-coordinate union, which has 41 distinct coordinates,
  range 509, `u=1`, and role cost 42.

For the published restricted AP family of cardinalities 15 through 21, the
defect is the constant eight.  The carry-triangle clauses do not lower any of
these optima.  A larger published restricted basis, at cardinality 41 and
range 536, has `u=12` but optimum role cost 54, so it needs one further
temporal/phase duplication.  The complete finite outputs are in
`computation/EXTREMAL_ROLE_RESULTS.json` and
`computation/PUBLISHED_ROLE_RESULTS.json`.

This pattern is structural evidence for an **existential** bounded-defect
sequence, which would activate the full-closure corollary in
`primal/AMPLIFIER_RESULT.md`.  It is not a universal theorem.

## Universal forms are false

The range-9 basis

```text
A={0,1,3,4,5}
```

has only two unique diagonals, `0` and `1`, but exact minimum phased cost
eight, exceeding `|A|+u=7`; the carry triangle still costs eight.  Thus
unique diagonals are not the only possible source of temporal/phase defect.
`computation/DIAGONAL_DEFECT_SEARCH.json` records this first counterexample
in an exhaustive sweep by increasing range.

Static four-colourability is also not universal.  The range-38 basis

```text
{0,1,2,3,4,9,14,17,18,24,28}
```

has a `K5` in its unique-off-diagonal graph on vertices
`{0,1,9,14,24}`.  The ten pair sums are independently checked in
`UNIQUE_K5_SEARCH.json`.  Its minimum phased cost is 15 for 11 coordinates.

## What would still close the problem

The data support only the following sharply scoped target:

> Find a sequence approaching `alpha_+` whose phased role defect is `o(k)`.

The unique-sum/Turan theorem in `primal/AMPLIFIER_RESULT.md` shows that this
is possible in the current five-role language only if `alpha_+<=7/16`.
More generally, a typed language with current-role compatibility chromatic
number `r` can be near-lossless only below

```text
c <= 1/2-1/(4r).
```

Thus a bridge robust throughout the presently allowed interval up to
`c=0.4585` needs at least seven current-compatible role colours, or a
nonlocal mechanism not captured by a finite current-role graph.

The diagonal pattern remains useful below that ceiling: it says what to seek
in structured limsup candidates, while the two counterexamples prevent an
unsupported universal claim.

## Source scope

The published finite bases were transcribed from Jukka Kohonen,
"A Meet-in-the-Middle Algorithm for Finding Extremal Restricted Additive
2-Bases," *Journal of Integer Sequences* 17 (2014), Article 14.6.8:
<https://cs.uwaterloo.ca/journals/JIS/VOL17/Kohonen2/kohonen5.html>.
Restricted extrema are used only as structural diagnostics; they are not
silently promoted to global extremizers.
