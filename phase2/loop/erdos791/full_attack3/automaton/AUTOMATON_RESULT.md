# Erdős #791 full attack 3: exact point-footprint carry automata

## Verdict

This lane produces exact elementary tile languages whose current-role graphs
contain `K_r` for **every fixed `r`**.  They are genuine
point-footprint constructions: each useful pair splits between the lower and
upper `t^2` blocks, and a self-loop in the carry automaton assembles the next
block from those two literal pieces.

The seven roles have slopes

```text
0, 10, 12, 15, 20, 30, 60.
```

After adding at most 120 endpoint phases to each elementary AP, **every two
distinct roles cover all residues modulo `t^2`**.  Hence their current-role
compatibility graph contains `K7`.  A `V/H` bootstrap covers the first block.
The resulting exact macro-to-literal theorem has asymptotic element cost one
per macro role placement.

The general family removes every finite version of the earlier chromatic
obstruction.  In particular, the optimized `K7` near-lossless density
threshold is

```text
1/2-1/(4*7)=13/28=0.464285... > 0.4585.
```

It does **not** resolve #791.  The missing bridge is sharper than role
coloring: adjacent macro targets must use carry-compatible edge states.  For
the canonical optimized `K7` lifts, the full 21-state graph at `t=251` has
only 25 of 441 transitions, and all strongly connected components are
singletons.  At tested scales `t=271,301,331,421`, only the 21 self-loops
remain.  Thus the `K_r` roles alone do not amplify arbitrary bases.  No new
finite ratio above `85/294` was found.

The lane also independently proves and audits the asymptotically lossless
three-tile modular triangle with block size `q^2-q+1`.  Its unphased carry
automaton has a one-way trap: once an exact state is used, the split `XZ`
state cannot be entered for `q>=4`.  Exhaustive translations give all nine
transitions at the exceptional scale `q=4`, but only seven at `q=5,6`.

## 1. Unbounded-clique elementary languages

For arbitrary fixed `r>=2`, let

```text
M=lcm(1,2,...,r-1),
D_r={0,M,2M,...,(r-1)M}.
```

If `a=iM<b=jM`, then `(b-a)=(j-i)M` divides `ab=ijM^2`, because `j-i`
divides `M`.  Define

```text
C_r=max_{a<b in D_r} max(v,u+v-b),
u=a^2/(b-a), v=b^2/(b-a).
```

This depends only on `r`, and crudely

```text
C_r <= 2(r-1)^2 M.
```

For example, take `t congruent 1 mod M` sufficiently large that
`t>max_{a<b}ab/(b-a)` and `t^2>t+2C_r`.  Then the tiles

```text
R_a(t)={ [i(t+a)]_(t^2) : -C_r<=i<=t+C_r-1 }
```

have size `t+O_r(1)` and every distinct pair covers all residues modulo
`t^2`, by the lattice proof below.  The current-role graph is therefore
`K_r`.  Since `r` is arbitrary, no obstruction depending only on a fixed
finite chromatic threshold can rule out this architecture.

`unbounded_cliques.py` implements the construction.
`verify_unbounded_cliques.py` checks its exact algebra through `r=8` and
literal residue coverage through `r=5`.

### Optimized seven-slope instance

Let `t>60`, `gcd(t,30)=1`, and `B=t^2`.  For

```text
D={0,10,12,15,20,30,60},   C=120,
```

define the canonical-residue tile

```text
R_a(t)={ [i(t+a)]_B : -C <= i <= t+C-1 } subset [0,B-1].
```

Also put

```text
V(t)=[0,t].
```

Since `gcd(t+a,t^2)=gcd(t+a,a^2)=1` for nonzero `a in D`, using
`gcd(t,a)=1`, and `t+240<B`,

```text
|R_0|=t,      |R_a|=t+240 for a!=0,      |V|=t+1.       (1)
```

The use of canonical residues is important: the negative and terminal
indices are fixed endpoint phases, not `O(t)` extra material.

### Pairwise modular-cover lemma

For every distinct `a,b in D`,

```text
R_a(t)+R_b(t) mod B = Z/BZ.                              (2)
```

#### Proof

Assume `a<b`, and put

```text
d=b-a,  u=a^2/d,  v=b^2/d,  h=ab/d.
```

For the displayed set `D`, `d` divides `ab` for all 21 pairs, so these are
integers.  Consider the homomorphism

```text
phi: Z^2 -> Z/BZ,       phi(i,j)=i(t+a)+j(t+b).
```

Its kernel contains

```text
p=(t-h,u),       r=(-v,t-b+v),                            (3)
```

because direct expansion gives

```text
phi(p)=B,       phi(r)=B,       det(p,r)=B.               (4)
```

At least one of `t+a,t+b` is a unit modulo `B` (when `a=0`, use `t+b`);
hence `phi` is onto and its kernel has index `B`.  Equations (3)--(4)
therefore give a basis of the full kernel.

Every coset has an integer representative in the half-open fundamental
parallelogram spanned by `p,r`.  Its coordinate bounds are

```text
-v <= i < t-h,
0  <= j < t-b+u+v.                                      (5)
```

For the 21 pairs, direct integer arithmetic gives

```text
v <= 120,       u+v-b <= 120.                            (6)
```

Thus every representative in (5) lies in
`[-120,t+119]^2`, precisely the index box defining the two tiles.  This
proves (2).  The largest required phase is attained by `(a,b)=(30,60)`, where
`v=120`.

`seven_slope_tiles.py` performs all algebra in integers.
`search_slope_clique.py` exhausts all seven-subsets of integer slopes
`[0,60]`: there are 42 with the divisibility property, and the minimum phase
radius under these lattice bounds is 120, first attained by the displayed
set.  This is a bounded design optimum, not a global optimum over all slopes.

## 2. Literal carry automaton

For an edge `e={a,b}`, let

```text
S_e=R_a+R_b,
L_e=S_e intersect [0,B-1],
U_e=(S_e intersect [B,2B-1])-B.
```

The modular-cover lemma is exactly

```text
L_e union U_e=[0,B-1].                                  (7)
```

This gives one carry state for every edge of `K7`.  Its transition rule is

```text
e -> f  iff  U_e union L_f=[0,B-1].                      (8)
```

Equation (7) proves all 21 self-loops `e->e` symbolically.  These loops are
the useful nonlocal assembly: if the same pair type has macro sums at both
`s-1` and `s`, its upper footprint from `s-1` and lower footprint from `s`
cover the literal block `[sB,(s+1)B-1]`.  No assertion that either footprint
is a full square is made.

`footprint_transition_audit.py` constructs the full **ordered** transition
graph at `t=251`.  It finds all 21 required self-loops and only four additional
transitions, hence 25 of the possible 441.  Deleting self-loops leaves a DAG:
all 21 strongly connected components are singletons.  The canonical phases
therefore emphatically do not make all edge-state transitions.

The scale scan is equally revealing:

```text
t:                    61   67   71  101  127  151  181  211  241  251  271  301  331  421
number transitions: 399  440  441  376  338  254  200  100   33   25   21   21   21   21
```

The nearly universal graphs at small scales occur because the fixed
`C=120` endpoint overhead dominates the core tile.  Cross-state coverage
collapses as the scale grows; at the four largest tested scales only
self-loops remain.  The missing cross-state portions are already macroscopic
at `t=251` (independent bitset checks find missing sets of thousands of
points).  This is exact finite evidence, not a proof that every sufficiently
large scale has only self-loops.

This is the decisive closure gap: adjacent targets represented by different
role pairs cannot generally be chained.  Only the self-loops are used in the
theorem; their validity for all admissible `t` follows from (2).

## 3. Exact macro-to-literal amplifier

Let `P_V` and `P_a (a in D)` be finite sets of nonnegative macro positions,
and define

```text
A_t=(V+B P_V) union union_{a in D} (R_a+B P_a).          (9)
```

Call macro square `s` certified if either

```text
s in P_V+P_0,                                            (direct bootstrap)
```

or, for some distinct `a,b in D`,

```text
{s-1,s} subset P_a+P_b.                                  (carry self-loop)
```

### Amplifier theorem

If the rule above certifies `s=0,...,m-1`, and

```text
L=|P_V|+sum_{a in D}|P_a|,
```

then for every admissible `t`,

```text
[0,m t^2-1] subset A_t+A_t,
|A_t| <= L(t+240).                                      (10)
```

Consequently the finite macro certificate proves

```text
liminf n(k)/k^2 >= m/L^2.                               (11)
```

To justify the liminf, not merely a construction subsequence, fix the macro
certificate and take admissible scales in a bounded-gap progression.  For the
optimized family these are the sufficiently large integers coprime to 30; for
the general family take `t=1 mod M`.  Given an arbitrary large cardinality
budget `k`, choose the largest admissible `t` with `L(t+240)<=k` (or
`L(t+2C_r)<=k` generally).  Then `t=k/L+O(1)`, so (10) gives
`R(k)/k^2 >= (mt^2-1)/k^2 -> m/L^2`.

#### Proof

`R_0={0,t,...,(t-1)t}`, so

```text
V+R_0=[0,t^2].
```

This proves every direct-bootstrap square.  For a self-loop square, the
macro sum at `s` contributes `sB+L_e`; the macro sum at `s-1` contributes
`sB+U_e`.  Equation (7) proves their union is the whole square.  Taking the
union over certified squares gives the interval in (10), and (1) gives its
size bound.  To pass from these scales to the liminf over every cardinality,
fix the macro certificate and, for arbitrary large `k`, choose the largest
`t congruent 1 mod 30` with `L(t+240)<=k`.  These admissible scales have
bounded gaps, so `t=k/L+O(1)`.  Pad `A_t` with arbitrary new integers to size
exactly `k`; its range cannot decrease.  Therefore

```text
n(k)/k^2 >= (m t^2-1)/k^2 -> m/L^2,
```

which proves (11).

This is an exact amplifier theorem with asymptotically zero elementary-tile
overhead.  `automaton_predicate.py` implements precisely its macro rule, and
`literal_verify.py` expands the actual integers.  The included `3 by 3` grid
certificate has `L=8,m=9`; literal checks pass at `t=61,67`.  It is only a
regression example, not a competitive construction.

The theorem holds verbatim for every fixed general family `D_r`, with the
size bound `L(t+2C_r)` in place of `L(t+240)`.  Thus the elementary overhead
remains asymptotically zero even as the fixed compatibility clique is made
arbitrarily large.  For each fixed `r`, the admissible progression
`t congruent 1 mod M` again has bounded gaps, so the same interpolation proves
the liminf statement.

### What a full closure theorem would now require

It suffices to find limsup-extremal coordinate bases `C_s`,
`|C_s|=k_s`, ranges `n_s`, and assignments to some fixed `K_r` language plus
`o(k_s)` duplicated/bootstrap placements such that each target is certified
by the actual transition rule.  For the scale-uniform theorem currently
proved, consecutive targets must use the same edge state.  Then
`L_s=k_s+o(k_s)`, and (11) gives

```text
alpha_- >= lim (n_s+1)/L_s^2 = alpha_+.
```

The previous unique-sum/Turán obstruction for an `r`-chromatic compatibility
graph only forces

```text
c <= 1/2-1/(4r)
```

under near-lossless typing.  The optimized instance has `r=7`, so it is not
obstructed up to the published upper endpoint `0.4585`; the unbounded family
removes every fixed chromatic threshold.  Neither fact supplies the missing
transition-compatible role assignment.

## 4. Projective modular triangle and its trap

For `q>=3`, put

```text
B=q^2-q+1,
X=(q-1)[0,q-1],
Y=[0,q-1],
Z={0} union {1+qj:0<=j<=q-2}.
```

All three tiles have size `q`, while `B/q^2->1`.  Exactly

```text
X+Y=[0,B-1],       Y+Z=[0,B-1],                         (12)
X+Z mod B=Z/BZ.                                         (13)
```

For (12), `X+Y` is the union of the touching intervals
`[i(q-1),i(q-1)+q-1]`; the corresponding intervals for `Y+Z` are also
adjacent and run from zero through `B-1`.

For (13), write a target as `aq+b`, with `0<=a<=q-2`, `0<=b<q`, together
with the terminal target `(q-1)q=B-1`.  Targets with `b=0` or `b=1` have the
immediate representations using `i=1` or `i=0`.  If `2<=b<q`:

- when `a+b>=q`, take `i=q+1-b`, `j=a-q+b`;
- when `a+b<=q-2`, take `i=q-b`, `j=a+b`, which represents the target plus
  `B`;
- on the boundary `a+b=q-1`, use the `Z` element zero and `i=a+1`.

These cases give (13), including endpoints.

Let `XY,YZ,XZ` denote their literal lower/upper footprint states.  The exact
transition graph for every `q>=4` is

```text
XY -> XY,YZ
YZ -> XY,YZ
XZ -> XY,YZ,XZ.                                         (14)
```

Indeed `XY,YZ` have full lower and empty upper footprints; `XZ` has modular
union full.  But `2` is absent from the lower `XZ` footprint for `q>=4`, so an
exact state cannot transition into `XZ`.  The split state is therefore a
one-way initial component, unusable after the exact bootstrap.

`verify_projective_triangle.py` checks all footprints and (14) through
`q=100`.  Exhausting all independent translations of `X,Y,Z` gives nine of
nine transitions at `q=4`, but maximum seven at `q=5,6`.  This finite phase
search is not a proof for every larger `q`; it is recorded because it rules
out the smallest scalable-looking repairs and isolates the `q=4` anomaly.

## 5. Scope and remaining routes

Established exactly:

- a `K_r` current-compatibility elementary language with fixed phase overhead
  for every fixed `r`, plus an optimized `K7` instance;
- a literal point-footprint automaton and amplifier theorem;
- a bootstrap tile for the initial block;
- the projective modular triangle and its unphased transition trap;
- independent symbolic, enumerative-residue, macro, and literal checks.

Not established:

- a near-lossless transition-compatible role assignment for arbitrary or
  limsup-extremal additive bases;
- an all-to-all or asymptotically mixing edge-state automaton;
- a finite certificate beating `85/294`;
- a proof that phase translations can never repair the projective triangle
  for all `q>=5`;
- equality of the liminf and limsup in Erdős #791.

The prioritized next step is a representation-hypergraph assignment theorem
that respects edge-state transitions, or a different choice of integer lifts
whose asymptotic transition graph mixes.  Increasing the role clique alone is
now known not to address this gap.

## Reproduction

```bash
cd phase2/loop/erdos791/full_attack3/automaton

python3 search_slope_clique.py --maximum 60
python3 verify_unbounded_cliques.py --through-r 8 --literal-through-r 5
python3 verify_seven_slope.py --t 251
python3 footprint_transition_audit.py --t 251
python3 transition_scale_scan.py
python3 literal_verify.py grid_example.json --t 61 67
python3 verify_projective_triangle.py --through 100
python3 projective_phase_search.py --through 6
python3 -m unittest -v test_automaton.py
```
