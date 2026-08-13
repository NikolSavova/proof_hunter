# Erdős #791 full attack — constructive/primal lane

## Verdict

No lower-bound improvement was found.  This lane closes a broad class of the
remaining phased constructions:

- a genuinely interleaved finite-state cycle was derived in which the same
  `L0/L1` placements serve two consecutive macroscopic rectangles;
- the cycle reaches the exact density ceiling `1/4` but cannot exceed it;
- more generally, **every role-separated finite-state/AP/carry architecture
  whose efficient component-interaction graph is triangle-free has density at
  most `1/4`**, independently of its periods, translations, or carry states;
- therefore a record construction must obtain more than
  `23 ell^2/588 = 0.0391156... ell^2` covered squares from genuinely
  non-bipartite/dual-role interactions.

This is a constructive lower-bound investigation only.  Even a record here
would improve one side of Erdős #791, not resolve the full problem.

## 1. An exact interleaved phase cycle

Let `k>=1`, `h>=2`, and put `M=2kh`.  Define macro placement sets

```text
I  = 2[0,k-1],
J  = empty,
K  = M+2[0,k-1],
L0 = 2k[0,h-1],
L1 = 1+2k[0,h-1].
```

This is genuinely interleaved.  The same `L0,L1` placements first pair with
`I` on `[0,M-1]` and then with `K` on `[M,2M-1]`; they are not copied into a
second serial gadget.

The relevant pair sums are

```text
I+L0 = {0,2,...,M-2},
I+L1 = {1,3,...,M-1},
K+L0 = {M,M+2,...,2M-2},
K+L1 = {M+1,M+3,...,2M-1}.
```

For the first interval, every even square is directly certified by `I+L0`,
and every odd square `q` is certified by

```text
q-1 in I+L0, q in I+L1.
```

For the second interval, every square except `M` is certified by one of the
two alternating `K/L` clauses.  The boundary square `M` is directly certified
by `0+M in I+K`.  Thus the abstract prefix is exactly

```text
m=2M=4kh,
ell=2k+2h.
```

The first uncovered square is `2M`: all `I/L` sums end below `M`, all `K/L`
sums end at `2M-1`, and, because `h>=2`, the largest `I+K` sum is at most
`2M-4`.

The density identity is

```text
ell^2-4m = 4(k-h)^2,
```

so this entire unbounded family has `m/ell^2<=1/4`, with equality at `k=h`.
The recorded equality instance is `(k,h)=(10,10)`, hence
`(ell,m)=(40,400)`.

### Macro-to-literal theorem

For even outer scale `t`, set `B=t^2` and

```text
V  = [0,t],
H  = {it:0<=i<t},
S  = {i(t+1):0<=i<t},
T0 = {i(t-1):0<=i<=t},
T1 = T0+1.
```

The literal basis is

```text
A_t=(V+B I) union (H+B J) union (S+B K)
    union (T0+B L0) union (T1+B L1).
```

The elementary phase lemmas imply

```text
[0,m t^2-1] subset A_t+A_t,
|A_t| <= ell(t+1).
```

Consequently the cycle is a scalable finite additive 2-basis family.  The
independent verifier checks the recorded certificate literally for
`t=2,4,6`; all pass.  A separate regression checks the exact prefix identity
for all `1<=k<=15`, `2<=h<=15`, and checks 160 random abstract placements
against literal sumsets for `t=2,4,6,8`.

## 2. The triangle-free interaction obstruction

The `1/4` ceiling is not peculiar to the displayed progressions.

### Current-sum injection

Every square certified by the phased predicate belongs to a *current* macro
pair-sum set:

- direct clauses visibly have `q in X+Y`;
- a consecutive clause has both `q-1,q in X+Y`, hence in particular
  `q in X+Y`;
- every mixed or alternating phase clause also has `q` in one of its two
  current-phase sumsets.

Distinct squares have distinct current sum values.  Hence, if a collection
of component pairs is responsible for a set of squares, their number is at
most the number of component pairs:

```text
# certified squares <= Sum_{active edges uv} |X_u||X_v|.       (1)
```

Collisions and overlaps only reduce the left-hand side.

### Weighted Mantel bound

Suppose the active component-interaction graph `G` is triangle-free and the
component sizes are `x_v`, with `Sum x_v=ell`.  Then

```text
Sum_{uv in E(G)} x_u x_v <= ell^2/4.                            (2)
```

For completeness, this has a short weighted proof.  If two positive-weight
vertices `u,v` are nonadjacent, merge the weight of the one with smaller
weighted-neighbor sum into the other.  The objective does not decrease and
the positive support shrinks.  Repeating leaves positive weight on a clique.
A triangle-free graph has clique size at most two, and the final objective is
`ab<=ell^2/4`.

Equations (1) and (2) prove:

> Any phased construction whose useful macroscopic component interactions
> are triangle-free has `m/ell^2<=1/4`.

This remains true with arbitrary finite-state carry transitions, translations,
unequal periods, repeated cycles, and sharing of a coarse `L` chain by many
fine chains.  Those operations change where rectangles land, but not the
pair-count bound.

## 3. Quantitative escape condition

Allow `R` prefix squares to use interactions outside a chosen triangle-free
role graph.  The same proof gives

```text
m <= ell^2/4 + R.
```

Since

```text
85/294 - 1/4 = 23/588,
```

a strict improvement over Kohonen forces

```text
R > 23 ell^2/588.                                               (3)
```

Thus at `ell=42`, at least 70 squares must come from non-bipartite/dual-role
interactions; a handful of boundary carries cannot suffice.  For the recorded
`ell=40` interleaved cycle, a record would require at least 63 such squares.
Its role audit finds zero: every one of its 400 squares is assigned to the
fine/coarse edges `I-L` or `K-L`.

This is the main narrowing result.  It rules out all architectures where
finite-state carries merely repair `O(ell)` boundary holes in an otherwise
bipartite fine/coarse tiling.

## 4. Consequence for mixed-radix AP boxes

In a common carry-free mixed-radix box, associate to each component the digit
coordinates it varies freely.  Two components generate a full product
rectangle only when their variable digit masks are complementary.  Therefore
the efficient interaction graph is a disjoint union of bipartite graphs
between a mask and its complement.  Section 2 applies, so every such common-
box construction has density at most `1/4`, even if the rectangles are
interleaved by a finite-state scheduler.

To beat `85/294`, a construction must therefore do at least one of the
following at quadratic scale:

1. make a component genuinely dual-role rather than merely a disjoint union
   of fine and coarse subcomponents;
2. exploit carry interactions that create a triangle of efficient component
   pairings;
3. obtain at least the exceptional mass in (3) from same-role pair sumsets.

A union of separate fine and coarse subcomponents does not evade the theorem:
counting the subcomponents separately leaves a bipartite interaction graph.

## 5. Exact scope

Closed by this lane:

- the natural two-edge finite-state cycle reusing `L` across consecutive
  rectangles;
- arbitrary triangle-free/bipartite component-role cycles, including any
  number of states and arbitrary carry scheduling;
- common carry-free mixed-radix box/AP constructions;
- variants where only subquadratically many boundary squares use off-role
  carry repairs.

Not closed:

- a dual-role component whose *same placements* support two complementary
  digit roles;
- a carry automaton producing a triangle of quadratic-size pair sumsets;
- the unrestricted five-list phased predicate;
- the analytic upper-bound side of Erdős #791.

No lower-bound record, and therefore no resolution of #791, is claimed.

## Reproduction

```bash
cd phase2/loop/erdos791/full_attack/primal

python3 interleaved_cycle.py --k 10 --h 10 \
  --output interleaved_cycle_40_400.json
python3 primal_verify.py interleaved_cycle_40_400.json --direct-t 2 4 6
python3 role_obstruction.py interleaved_cycle_40_400.json
python3 -m unittest -v test_primal.py
```
