# Erdős #791: full-closure attempt

Date: 2026-08-13

## Verdict

This attempt did **not** resolve Erdős #791 and did not improve the published
asymptotic construction constant `85/294`.

The original three-tile/Kohonen-neighbourhood approach is incremental.  Its
finite certificates are rigorous and useful, but no amount of local search
around one certificate can prove that the normalized extremal function has a
limit.  The new reflected, phase-shifted direction is a more substantive
opening: it creates exact coverage mechanisms absent from the three-tile
language and has enough pair capacity in principle to beat `85/294`.  However,
the two natural scalable ways of organizing it are now proved insufficient.
So it is a real research route, not a near-term closure argument.

The precise remaining open problem is stronger than the old question
`g(n) ~ 2 sqrt(n)`, which Mrose's 1979 construction already disproved.  If

```text
R(k) = max {r : some A with |A| <= k has [0,r] subset A+A},
```

then even the existence of `lim R(k)/k^2` (equivalently
`lim g(n)^2/n`) remains open in the current primary literature.  The published
interval is

```text
85/294 <= liminf R(k)/k^2 <= limsup R(k)/k^2 <= 0.4585... .
```

Thus a full resolution needs either a universal upper bound matched by a
scalable construction, or a new theorem forcing the lower and upper normalized
limits to agree.  A one-off finite record would improve one side only.

## What was established

### 1. Exact asymptotic reduction and barriers

Writing

```text
alpha_- = liminf R(k)/k^2,   alpha_+ = limsup R(k)/k^2,
```

we proved the exact inverse identities

```text
liminf g(n)^2/n = 1/alpha_+,
limsup g(n)^2/n = 1/alpha_-.
```

A verified family of sizes `K_t = ell*t+O(1)` and ranges
`N_t = m*t^2+O(t)`, with bounded size gaps, proves
`alpha_- >= m/ell^2`.  If its ratio matched a universal upper bound, this
interpolation would close the full problem.

The obvious amplification mechanisms cannot do that:

- mixed-radix Cartesian products multiply normalized efficiencies, each less
  than one, so iteration collapses;
- ordinary concatenation gives only linear range in its size;
- the known small-cardinality cyclic digit iteration increases additive order,
  whereas #791 must stay at order two;
- cyclic coverage alone does not control integer carries.

These are proved obstructions for the named mechanisms, not a general no-go
theorem.

### 2. A nonlocal analytic reduction

For any asymptotic sequence with `R_j/k_j^2 -> c`, the scaled empirical
measures have a subsequential weak limit `mu` on `[0,1]` satisfying

```text
mu * mu >= 2c Lebesgue measure on (0,1).
```

This is a rigorous continuous relaxation of the discrete problem.  It points
toward a carry-aware, multi-bin copositive/SOS hierarchy.  But the relaxation
by itself is loose (`1/4 <= C_conv <= 1/2`), and a single nonnegative test
weight provably cannot improve the elementary `c <= 1/2` counting bound.  A
completeness theorem retaining lattice coverage, collisions, and carries is
missing.  This is therefore a concrete analytic program, not a claimed finite
reduction of #791.

### 3. A new exact phased construction language

Adding the reflected tile in two phases yields a five-list macro certificate
with four material coverage clauses omitted from the initial campaign.  The
elementary inclusions were checked for every even scale through `t=100`, and
160 randomized abstract certificates were checked against literal integer
sumsets at `t=2,4,6,8`.

It contains a perfect alternating-parity gadget

```text
K  = 2[0,k-1],
L0 = 2k[0,h-1],
L1 = 1 + 2k[0,h-1],
```

which certifies `m=2kh` with `ell=k+2h+2`.  In isolation its limiting density
is at most `1/4`, since `(k+2h)^2-8kh=(k-2h)^2`; appending it as a disjoint tail
therefore lowers Kohonen's density.

More strongly, the full unbounded serial arithmetic-block staircase
containing Kohonen's construction was optimized symbolically.  For all its
parameters,

```text
m/ell^2 <= 85/294,
```

with equality uniquely at `(r,u,s,z)=(5,6,17,2)`, giving `(ell,m)=(42,510)`.
The proof is an explicit nonnegative case analysis after an exact polynomial
identity, independently replayed over 7,346,380 parameter tuples.  Replacing a
high block by the reflected phase preserves `42/510`; adding the natural next
reflected block gives only `48/653`, below the record-beating target `48/667`.

Consequently, a phased construction must be genuinely interleaved: the same
placements must serve both the alternating `K/L` digit rectangle and long
`I/L` or `J/L` intervals.  Pure periodic, serial, and disjoint-tail uses are
closed.

### 4. Global exact search, with portable proofs where claimed

For the original three-list predicate and targets

```text
m(ell) = floor(85*ell^2/294)+1,   18 <= ell <= 24,
```

the elementary pair-capacity bound eliminates 450 of 706 canonical positive
type splits.  All 20 capacity-tight survivors were globally encoded, proved
UNSAT by CaDiCaL, and independently checked with `drat-trim`.  A complete
representative DRAT certificate is retained.  At `(ell,m)=(20,116)`, this
closes the five tight splits

```text
(2,9,9), (3,11,6), (6,11,3), (9,9,2), (11,6,3).
```

It does **not** close the other feasible splits.  In particular, four bounded
global runs on `(6,7,7)` accumulated 17,115,580 conflicts and
25,488,942,383 propagations but returned `UNKNOWN`; there is neither a model
nor an UNSAT proof.

For the enlarged phased predicate, exhaustive count-split CP-SAT runs found
no witness at `(ell,m)=(7,15)` or `(8,19)`.  These are exact solver conclusions
inside the encoded finite predicate but do not have retained portable proof
traces.  At `(9,24)`, 76 of 157 capacity-surviving splits timed out and the
result is correctly recorded as `UNKNOWN`.  Three larger phased searches at
the `(18,94)` record-beating target tested 600,000,000 mutation proposals;
their best covered prefix was 81.  They found no record and carry no negative
evidentiary weight.

## What would actually close the problem

There are now two credible but incomplete routes.

1. **Constructive:** solve the interleaved phase-compatibility problem so that
   one scalable five-list family exceeds `85/294`; to close rather than merely
   improve the lower bound, its ratio must eventually meet a universal upper
   bound (or be paired with a new matching upper bound).
2. **Analytic:** strengthen the weak-limit convolution theorem to a complete
   carry-aware finite hierarchy and obtain a rational certificate at
   `85/294`, matching Kohonen's family.

The first route has the clearer finite target and is the best next experiment.
The second is the route with a genuine chance of settling the existence of the
limit, but it requires a new compactness/completeness lemma, not merely larger
optimization runs.

## Verification map

- `theory/STATUS_AND_THEORY.md`: literature audit, inverse limits,
  interpolation, composition barriers, and weak-limit theorem.
- `theory/check_composition.py`: 169 exhaustive product checks, family checks,
  and inverse-function checks.
- `tiles/CLOSURE_RESULT.md`: phased lemmas, periodic gadget, and the global
  staircase obstruction.
- `tiles/test_phased_predicate.py` and `tiles/audit_staircase_identity.py`:
  literal/randomized phase checks and the 7,346,380-case identity audit.
- `sat/README.md`, `sat/EXTREMAL_RESULTS.json`, and
  `sat/ell20_m116_299.drat.gz`: exact global SAT scope, hashes, and retained
  proof.
- `root/`: independent enlarged-predicate encoding and small-cardinality
  count-split results.

## Primary status references

- Erdős Problems, [Problem #791](https://www.erdosproblems.com/791).
- Kohonen, [An improved lower bound for finite additive 2-bases](https://arxiv.org/abs/1606.04770).
- Yu, [A new upper bound for finite additive bases](https://doi.org/10.1016/j.jnt.2015.04.007).
- Faust--Tait, [Restricted additive bases](https://arxiv.org/abs/2507.23627),
  especially Conjecture 1.5 on equality of normalized limits.
- Nathanson, [Extremal problems and additive bases](https://arxiv.org/abs/2605.26425).
