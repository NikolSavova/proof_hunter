# Erdős 838 Gate A: exact reflection-order search

**Date:** 2026-08-13
**Scope:** reverse-product trace target, reduced words, graded profile, and
fixed-`x` realizability.  This is a computational theorem/report, not a proof
of the asymptotic lower bound.

## Verdict

The reverse-product target survives the gate.

* Every commutation class of reflection orders through `N=7` was enumerated
  exactly.  The counts are `1,2,8,62,908,24698` for `N=2,...,7`.
* The exact minimum traces are
  `3,7,14,26,44,72`.  In particular, at `N=7` the minimum normalized value is

  ```text
  log2(72)/log2(7)^2 = 0.7828620500255113 > 1/2.
  ```
* A trace-minimizing class at every `N<=7` has a rational realization with
  `x_i=i`.  Thus the worst order found in the broader pseudoline state space
  is already stretchable in the required strong sense; stretchability does
  not hide a smaller exact example at these sizes.
* Coxeter annealing found no larger counterexample.  The best records through
  `N=20` all have normalized trace above `0.73` (the `N=20` run is visibly
  search-limited and is not a claimed minimum).
* The graded mean-size statistic is also encouraging.  Through `N=7`, its
  exact minimizer always coincides with the trace minimizer.  The exact minimum
  of `mu-log2(N)` is `-0.168466...` at `N=7`; the lowest heuristic value is
  `-0.194690...` at `N=8`.  There is no evidence here that the deficit grows.

Gate-A outcome is therefore the first branch in the plan: it is reasonable to
attack the stronger all-reflection-order theorem and to use Coxeter moves as
proof tools.  The computation does **not** prove the asymptotic RPR inequality.

## 1. Exact evaluator

The implementation is `reflection_order_gate.py`.

For a reduced word of `w_0 in S_N`, start with the wire order
`0,1,...,N-1`.  At generator `s_i`, record the labels on the two adjacent
wires and swap them.  These recorded pairs are the root sequence.  A word is
rejected unless every swap increases Coxeter length and the final permutation
is decreasing.

For a root `(i,j)`, `i<j`, the code applies the row update

```text
row_j <- row_j + z row_i.
```

It computes both the forward and reverse products.  At `z=1` it reports the
Frobenius product, the full endpoint matrices, their totals, and the largest
endpoint product.  Polynomial rows give the exact graded partition function

```text
Z(z) = Nz + <A(z),B(z)> - N.
```

An independent derivative sweep maintains values and derivatives under

```text
V_j <- V_j + V_i,
D_j <- D_j + V_i + D_i.
```

It therefore computes `Z'(1)` without expanding polynomials.  Every saved
graded certificate checks both `Z(1)` and `Z'(1)` against these independent
states.

The self-test converts exact coordinates into a reduced word and agrees with
the pre-existing `reflection_trace.py` code on both required cases:

```text
T_(4,2):        (C,U,V,M) = (31,31,50,9)
36-point cell:  (C,U,V,M) = (14136,14136,441399,24336)
```

For the six-point cell the graded profile is
`(v_1,...,v_6)=(6,15,20,9,0,0)`.

## 2. Why the class enumeration is exhaustive

Two adjacent generators with indices differing by more than one commute.  In
the root sequence, these are disjoint crossings; their transvections commute,
so the trace and graded polynomial are constant on each commutation class.

The code builds the Coxeter heap of a word.  Occurrences are ordered whenever
their generator labels are equal or adjacent, and transitive predecessor and
successor closures are stored as bitsets.  The lexicographically least linear
extension is a canonical key for the commutation class.

A long braid can be exposed precisely when its three heap occurrences form a
convex three-element interval.  For every wire triple, the code tests that
criterion, constructs an explicit linear extension in which the interval is
consecutive, checks that its letters are `i,i+1,i` or `i+1,i,i+1`, performs
the braid, and canonicalizes the result.  Breadth-first search from the bubble
word then visits the graph of commutation classes.  Matsumoto connectivity of
reduced words makes this exhaustive.  As a strong implementation check, the
number of visited classes reproduces

```text
N = 3,4,5,6,7:  2, 8, 62, 908, 24698.
```

In addition, the script separately enumerated all `292864` individual reduced
words at `N=6`; its trace histogram and minimum agree with the 908-class run.

## 3. Exact results

| `N` | classes | min trace | minimizing classes | graded profile `v_1,v_2,...` | `log V/log^2 N` | min `mu-log N` |
|---:|---:|---:|---:|---|---:|---:|
| 2 | 1 | 3 | 1 | `2,1` | 1.584963 | +0.333333 |
| 3 | 2 | 7 | 2 | `3,3,1` | 1.117530 | +0.129323 |
| 4 | 8 | 14 | 4 | `4,6,4` | 0.951839 | 0 |
| 5 | 62 | 26 | 22 | `5,10,10,1` | 0.871848 | -0.052697 |
| 6 | 908 | 44 | 12 | `6,15,20,3` | 0.817032 | -0.130417 |
| 7 | 24698 | 72 | 152 | `7,21,35,9` | 0.782862 | -0.168466 |

The mean column is an independent optimization, not merely the mean of the
trace record.  The optimizers happen to coincide throughout this exact range.

The complete trace histograms, endpoint matrices, reduced words, root
sequences, graded polynomials, and rational coordinates are in
`classes_n3.json` through `classes_n7.json`.  The all-reduced-word audit is in
`exhaustive_n2.json` through `exhaustive_n6.json`.

### Exact `N=7` minimum certificate

One zero-based reduced word is

```text
0 1 2 3 2 4 3 5 4 3 2 1 0 2 3 2 1 2 3 4 3
```

Its root order is

```text
01,02,03,04,34,05,35,06,36,56,46,26,16,24,25,45,15,14,12,13,23.
```

It gives `V=72`, endpoint maximum `8`, `(C,U)=(46,53)`, and
`Z(z)=7z+21z^2+35z^3+9z^4`.  The JSON contains rational `y_i` with `x_i=i`.
The checker verifies every comparison between incident chords exactly; any
remaining changes in total slope order exchange disjoint roots only and hence
do not affect the products.

## 4. Heuristic records

These are upper records for the minimum trace over reflection orders, not
certified minima.

| `N` | best trace | graded profile | normalized | `mu-log N` | fixed-`x` status |
|---:|---:|---|---:|---:|---|
| 8 | 113 | `8,28,56,20,1` | 0.757798 | -0.194690 | rational certificate |
| 9 | 187 | `9,36,84,54,4` | 0.751053 | -0.127144 | rational certificate |
| 10 | 301 | `10,45,120,104,21,1` | 0.746123 | -0.042858 | not certified with fixed `x` |
| 12 | 690 | `12,66,220,278,106,8` | 0.733776 | +0.029530 | not attempted |
| 16 | 3391 | `16,120,560,1168,1102,409,16` | 0.732968 | +0.330286 | not attempted |
| 20 | 20424 | `20,190,1140,3477,5842,5651,3087,904,113` | 0.766526 | +1.098264 | not attempted |

The higher-`N` deterioration is a search-quality warning, not mathematical
evidence.  Each run used randomized short commutations to expose long braids
and exact-integer annealing on the trace.  The saved JSON records all seeds,
move counts, reduced words, and matrices.

The `N=10` status means only that the dependency-free projection routine did
not produce an equally-spaced-`x` certificate within its iteration budget.  It
is not an infeasibility or nonstretchability certificate.

## 5. Mean-size route suggested by the data

Let `mu(P)=Z'_P(1)/Z_P(1)`, the mean size of a uniformly chosen convex subset.
For an actual point set, averaging over point deletions gives

```text
(1/N) sum_p V(P-p) = V(P)(1-mu(P)/N).
```

Thus a universal estimate

```text
mu(P) >= log2(N)-O(1)
```

would integrate through deletion to
`log2 f(N) >= (1/2)(log2 N)^2-O(log N)`.  The exact reflection-order data do
not falsify this: the worst observed deficit is less than `0.2` through the
well-searched range.  This is a sharper next conjecture than a bare finite-`N`
trace inequality because it exposes a one-step induction mechanism.

The important unresolved point is to prove the deletion identity and the mean
bound in the generalized reflection-order model in a way that retains the
two-endpoint interpretation.  For stretchable orders the deletion identity is
immediate from convex subsets.

## 6. Reproduction

Run from the repository root:

```sh
python3 phase2/loop/erdos838/agent_reflection_gate/reflection_order_gate.py selftest
python3 phase2/loop/erdos838/agent_reflection_gate/reflection_order_gate.py exhaustive 6
python3 phase2/loop/erdos838/agent_reflection_gate/reflection_order_gate.py classes 7
python3 phase2/loop/erdos838/agent_reflection_gate/reflection_order_gate.py \
  check phase2/loop/erdos838/agent_reflection_gate/classes_n7.json
```

The class enumeration is deterministic.  The heuristic search additionally
accepts `--steps`, `--restarts`, `--seed`, and
`--objective trace|mean-deficit`.

## 7. Claim boundary and next move

**Certified:** the algebraic evaluator, coordinate cross-checks, all reduced
words through `N=6`, all commutation classes through `N=7`, exact minima and
graded profiles in that range, and the stated rational fixed-`x`
realizations.

**Evidence only:** all results labeled heuristic, and any inference about the
asymptotic coefficient.

**Recommended next proof attack:** work directly on
`mu >= log2 N-O(1)` for all reflection orders.  In parallel, derive how
`Z'/Z` changes under a single long braid.  The exhaustive data show that both
trace and mean minima lie on sparse profiles with no convex sets beyond size
four through `N=7`; a braid-local monotonicity or a deletion-compatible heap
potential is now a concrete, falsifiable target.
