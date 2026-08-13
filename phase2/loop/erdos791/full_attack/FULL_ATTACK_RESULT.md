# Erdős #791: full-problem attack

Date: 2026-08-13

## Outcome

The full normalized-limit problem was **not resolved**.  The attack produced
several new structural theorems, eliminated two broad classes of proposed
closures, and isolated two precise bridges that would suffice for a solution.

For

```text
R(k)=max {n : some |A|<=k covers [0,n] by A+A},
alpha_-=liminf R(k)/k^2,  alpha_+=limsup R(k)/k^2,
```

the goal remains to prove `alpha_-=alpha_+` and ideally determine their common
value.  A finite construction record alone cannot do this.

## The strongest new results

### 1. A rigorous carry-bin hierarchy

At level `m`, divide elements and targets into `m` macroscopic bins.  An
unordered pair cell `(i,j)` has asymptotic capacity `p_i p_j` off the diagonal
and `p_i^2/2` on it, and may route representations only into target bins
`i+j` and `i+j+1`.  Let `U_m` be the largest uniformly routable normalized
target density.

We proved

```text
alpha_+ <= U_m,
U_(rm) <= U_m,
inf_r U_(2^r) = C_conv,
```

where `C_conv` is the continuous relaxation defined by probability measures
`mu` satisfying `mu*mu >= 2c lambda` on `(0,1)`.  The last equality uses a
dyadic rectangle compactness argument, symmetrized unordered-pair flows,
Portmanteau, and a monotone-class passage.

This makes the continuous relaxation computationally approachable by exact
finite max-flow plus a nonconvex outer optimization.  Exploratory outer
searches reached values from `0.5` at four bins down to `0.45597` at twenty
bins.  These are only **lower bounds on the relaxation optima**, not universal
upper certificates.

### 2. All fixed congruence information is still insufficient

Every asymptotic basis sequence has a subsequential probability measure on

```text
[0,1] times Z-hat
```

whose self-convolution dominates `2c` times Lebesgue–Haar measure.  This keeps
all fixed residue classes simultaneously.  Nevertheless, the profinite
relaxation constant equals `C_conv` exactly: projection gives one inequality,
and tensoring any continuous feasible measure with Haar measure gives the
other.

Therefore mod `2`, mod `4`, or even every fixed modulus cannot recover
pointwise lattice coverage.  A complete analytic hierarchy must retain a
scale growing with `k`, or equivalent mesoscopic collision/difference data.

### 3. A finite amplifier that would prove existence of the limit

If `V,H subset A` and `[0,n] subset V+H`, put `L=|V|+|H|`.  The explicit set

```text
union_{v in V} (v q^2+[0,q-1])
union_{h in H} (h q^2+q[0,q-1])
```

has at most `Lq` elements and covers `[0,(n+1)q^2-1]`.  Hence

```text
alpha_- >= (n+1)/L^2.
```

It follows immediately that `alpha_-=alpha_+` if limsup-extremal bases can be
chosen with cross-cover cost `|A|+o(|A|)`.  This is a precise sufficient lemma,
not a conjecture silently used in a proof.

The condition is nonformal.  Exact CP-SAT optimization on literal members of
Kohonen's family gave:

```text
outer t        2    3    4    5    6
|A_t|         91  133  175  217  259
cross cost    99  157  207  257  307
```

Thus the best published construction does not appear to have vanishing
cross-cover defect; for `t=3,...,6` the exact finite values follow
`50t+7` versus size `42t+7`.  No asymptotic formula is claimed from these five
computations.

### 4. A genuinely interleaved phased family, and a broad obstruction

The constructive lane found a family in which the same phase placements serve
two successive rectangles:

```text
ell=2k+2h,   m=4kh,   ell^2-4m=4(k-h)^2.
```

It is genuinely interleaved but has density at most `1/4`.  Its literal
integer expansions pass.

More generally, if the graph of component pairs responsible for current
macro sums is triangle-free, weighted Mantel gives

```text
m <= ell^2/4.
```

This rules out every role-separated finite-state/AP scheduler and every common
carry-free mixed-radix box whose efficient interaction graph is bipartite.
Beating Kohonen requires more than `23 ell^2/588` squares from dual-role,
same-role, or carry-generated triangular interactions—at least 70 squares
when `ell=42`.  Boundary repairs of only `O(ell)` squares cannot work.

### 5. A universal collision bound for the three-tile predicate

For list sizes `a=|I|,b=|J|,c=|K|`, every three-tile certificate satisfies

```text
m <= ab+ac+bc-min(b,c)
  <= floor(ell^2/3)-floor(ell/3).
```

The proof charges each component start of `J+K` either to a lost consecutive
edge or to forced overlap with direct coverage.  The bound is sharp for an
infinite family.  It eliminates 496 of 706 canonical type splits at the
record-beating targets `ell=18,...,24`, 46 more than raw pair capacity.

Its leading constant is still `1/3`.  An exact two-parity relaxation has a
matching rational primal and SOS dual at `1/3`, so parity counts alone cannot
close the remaining gap.

## What is dead, and what remains hopeful

Closed or seriously downgraded:

- local perturbation of Kohonen and its whole serial staircase family;
- appended, serial, or triangle-free phased gadgets;
- carry-free mixed-radix boxes;
- ordinary products and concatenation;
- macroscopic position plus all fixed congruence classes;
- cumulative population inequalities without convolution compatibility;
- parity-only duals.

The two most hopeful full-problem routes are now:

1. **Mesoscopic collision hierarchy.**  Refine the carry-bin flow model at a
   modulus/mesh `q(k)->infinity`, retaining multiplicities or differences at
   the scale where individual holes survive, and prove a deterministic
   rounding/design theorem.  Fixed-state compactness is provably too weak.
2. **A multitype finite amplifier.**  Generalize the cross-cover blow-up from
   two horizontal/vertical roles to the carry-generated triangle supplied by
   the phased elementary tiles.  A lossless or `o(k)`-loss role assignment for
   limsup-extremal bases would prove the limit exists.  The triangle-free
   theorem says a genuinely dual-role component or a quadratic carry triangle
   is mandatory.

The ordinary two-role cross-cover lemma is mathematically clean but currently
less hopeful, because the known record family shows a substantial finite
defect.  The multitype version is the natural attempt to remove that defect.

## Verification map

- `analytic/ANALYTIC_RESULT.md`: profinite no-go and cross-cover amplifier.
- `analytic/bipartite_blowup.py`: finite extremizers and literal amplifications.
- `analytic/profinite_cylinder_check.py`: 10,336,000 fixed-cylinder checks.
- `root/BIN_FLOW_HIERARCHY.md`: finite hierarchy and continuous completeness.
- `root/bin_flow_relax.cpp`: exact inner max-flow and heuristic outer search.
- `primal/PRIMAL_RESULT.md`: interleaved family and weighted-Mantel theorem.
- `primal/test_primal.py`: 225 family instances and randomized literal checks.
- `dual/THEOREM.md`: collision bound, exact type envelope, and parity dual.
- `dual/collision_bound.py`: more than 2.1 million difficult-set checks plus
  the full smaller census.
- `root/cross_cover_cpsat.py`: exact finite cross-cover optimizer used on
  Kohonen instances; solver optimality is recorded, but no portable SAT proof
  is claimed.

All theorem-level claims were independently cross-audited after the initial
proof drafts.  No file in this directory claims a resolution of #791.
