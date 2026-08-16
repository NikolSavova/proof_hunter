# Erdős 838: strict minimizer mean-gain strategy

**Date:** 2026-08-16
**Status:** strategy and exact implication preserved; the route is now parked by
`STRICT_MINIMIZER_MEAN_GAIN_AUTOPSY_20260816.md`.  No coefficient improvement
is claimed here.

All logarithms are base two and the empty convex subset is included.  For an
`n`-point general-position configuration `P`, write `V(P)` for the number of
convex subsets and

```text
mu(P) = (1/V(P)) sum_(A convex) |A|.
```

This note replaces the parked fixed-size threshold-layer attack with a direct
minimizer target.  It records the exact implication, the geometric form to be
tested, and a precommitted kill rule before a new large search begins.

## 1. Exact deletion implication

Double-counting `(A,x)` with `A` convex and `x notin A` gives

```text
sum_(x in P) V(P-x) = (n-mu(P))V(P).                 (1)
```

If `P` minimizes `V` among `n`-point configurations, then

```text
f(n-1) <= f(n)(1-mu(P)/n).                           (2)
```

Consequently, if some fixed `a>0` satisfies

```text
mu(P) >= (a-o(1))log n                               (3)
```

for every large minimizer, summing `-log(1-mu/n)` gives

```text
log f(n) >= (a/2-o(1))(log n)^2.                     (4)
```

The strict target

```text
mu(P) >= (1/2+epsilon-o(1))log n                     (M4a)
```

therefore improves the unconditional coefficient from `1/4` to
`1/4+epsilon/2`.  Unlike the full mean conjecture `mu>=log n-O(log log n)`,
this asks only for any fixed positive margin above half-logarithmic mean.

## 2. Equivalent blocked-point sufficient condition

Represent a convex subset by the closed hull `K=conv(A) intersect P`.  Put

```text
H=|ext(K)|,       I=|K|-H,       O=n-|K|.
```

Under the uniform law on closed hulls, `E H=mu`.  Let `B(K)` be the number of
exterior labels that are not addable as a new extreme point.  Edge balance in
the convex-subset poset gives

```text
E O = mu + E B.                                      (5)
```

The Boolean-interval identity and Jensen give

```text
2^n = sum_K 2^I,
log V <= n-E I = mu+E O = 2mu+E B.                  (6)
```

Thus any fixed `delta>0` for which every low-mean minimizer satisfies

```text
E B <= (1-delta)mu^2+o(mu^2)                         (M4b)
```

implies `log V <= (1-delta+o(1))mu^2`.  Combining this with (2), or comparing
the two asymptotic differential inequalities directly, yields

```text
log f(n) >= (1/[4(1-delta)]-o(1))(log n)^2.          (7)
```

Therefore either (M4a) or (M4b) is a genuine strict gain.  Full coefficient
one-half would require the much stronger asymptotic factor `1/2` in (M4b),
which is not the present target.

## 3. Geometry and finite calibration

A blocked exterior label `p` has a rooted planar circuit

```text
b in conv{a,c,p},       a,b,c in ext(K).             (8)
```

The task is not to bound these witnesses pointwise: arbitrarily many exterior
points can share one visible ear.  Minimizer status must instead force one of
two outcomes:

1. the average rooted-circuit multiplicity is a fixed factor below `mu^2`; or
2. a high-multiplicity ear supports enough additional convex subsets to
   contradict minimality.

The exact stored closure certificates give

```text
n=9 minimizer:   E B/mu^2 = 0.2974...,
n=17 record:     E B/mu^2 = 0.5105...,
n=20 record:     E B/mu^2 = 0.5605....               (9)
```

These survive (M4b), but the stronger-looking inequality
`E B<=E binom(H,2)` already fails at `n=17`.  Universal non-minimizer claims
are therefore outside the route.

The exact all-face reflection-order stress audit sharpens that warning:

```text
n=44 nonminimizer:  E B/mu^2 = 1.100265...,
n=58 nonminimizer:  E B/mu^2 = 1.350137....          (9a)
```

Every one of the `237,229` and `1,061,907` closed hulls, respectively, was
reconstructed from the certified rational slope order and exact half-plane
masks.  Thus even the coefficient-one blocked-point inequality is false
universally.  By contrast the exact `n=8,9` minimizers have ratios
`0.247736...` and `0.297417...`.  Any proof of (M4b) must use global
minimality through a relocation or mutation comparison; planarity alone is
already ruled out.

## 4. Stress list and stop rule

Before attempting a proof, test (M4b) against:

- all exact rational closure certificates in the repository;
- balanced Pascal and vertically substituted Pascal families;
- nested-triangle/common-ear cages and fixed-edge dominance examples;
- the certified 58-wire/reflection-order record where relevant;
- strong glues whose bivariate `(H,I)` enumerators can be computed exactly.

The route is **killed** if a stretchable minimizing sequence is found with

```text
mu <= (1/2+o(1))log n       and       E B/mu^2 -> 1,  (10)
```

or if two further reductions fail to produce a quantitative `epsilon` or
`delta`.  A counterexample among arbitrary non-minimizers only kills a
universal strengthening; it does not kill M4.

## 5. Immediate bounded task

Build an exact bivariate stress table and then prove or refute the first
candidate aggregate statement:

> In a low-mean global minimizer, high rooted-circuit multiplicity in one
> exposed ear either contributes at most `(1-delta)mu^2` on average or admits
> a one-point relocation whose face-count decrease is at least the excess.

No new named residual should be introduced until this statement has an exact
constant and a checked implication to (M4b).

The stress table is implemented by
`verify_strict_minimizer_mean_gain_stress.py`.  Its large exact rows refute the
universal blocked-point inequality.  The minimizer-only relocation comparison
then reaches the already-open multi-point mutation interface, while the
variance reformulation reaches P1d.  Under the precommitted two-reduction stop
rule there is therefore no remaining bounded task in this lane; see the
autopsy before reusing either sufficient condition.
