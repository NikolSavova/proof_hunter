# Rankwise near-maximal Hall target

**Date:** 2026-08-14  
**Verdict:** no scalable counterfamily was found.  The rankwise statistic is
slightly larger than one on an exact stretchable 24-point record, so the
tempting finite bound `K<=1` is false.  In every scalable central, vertical,
and guarded family tested, even the stronger profile-only upper bound on `K`
decreases rapidly.  The data support a universal constant bound.  A focused
kill-pass also disproved the sharp-looking `K<=17/16`; the next empirical
boundary is `K<=16/15`, while the safer target `K<=4/3` has ample margin.
Neither is proved, so this is not a proof of RNP or Erdős 838.

Put

\[
 L=\lceil\log_2n\rceil,
 \qquad
 N_r(P)=\#\{A:|A|=r,\ A\text{ convex},\ u(A)\leq4(r+1)\},
\]

and

\[
 \boxed{K(P)=\max_{r<L}{2^{L-r}N_r(P)\over Z_P(1)}.}     \tag{1}
\]

The proposed rankwise near-maximal Hall theorem is
`K(P)<=poly(log n)`.  The charging lane shows that this would close the
remaining maximal-pocket part of the half-weight proof.

## 1. Exact rooted-circuit evaluator

For each triple `T` of point labels, store the bit mask

\[
 B(T)=\{p:T\cup\{p\}\text{ is a nonconvex quadruple}\}. \tag{2}
\]

For a candidate set `A`, form

\[
 B(A)=\bigcup_{T\in\binom A3}B(T).                      \tag{3}
\]

The rooted-circuit characterization gives simultaneously

\[
 A\text{ is convex}\iff A\cap B(A)=\varnothing,
 \qquad
 u(A)=|P\setminus(A\cup B(A))|.                         \tag{4}
\]

Thus all `N_r` values below are exact integer censuses.  Saved decimal
coordinates are interpreted as rational numbers, every determinant is tested
exactly, and the resulting face counts are independently checked against the
reflection-matrix rank polynomial.

## 2. Finite constant one is false

A stretchable fixed-`x` coordinate anneal at `n=24` found the exact rational
order type in `planar_rnp_record.json`, with profile

```text
(1,24,276,2024,5358,1962,379,39,1).
```

Here `L=5`.  Every convex four-face is automatically counted in `N_4`, since

\[
 u(A)\leq n-4=20=4(4+1).
\]

Consequently

\[
 K(P)={2v_4\over Z(1)}={10716\over10064}
 ={2679\over2516}=1.064785373609\ldots>1.              \tag{5}
\]

The rank-three term is only `4*483/10064=0.19197...`, so rank four genuinely
maximizes (1).  This exact example kills `K<=1`, but not any asymptotic or
polylogarithmic form.  The effect is partly a small-`n` ceiling coincidence:
`n+1=5L`, making the near-maximal threshold vacuous at the top audited rank.

The search took 110,000 stretchable coordinate moves in four passes; the final
20,000-move low-temperature pass did not improve (5).  The prior ACP-optimized
record had `K=1.05156`; direct optimization raised it past `17/16` to (5),
still `71/37740=0.0018813...` below `16/15`.

Exhaustion of all type-A reflection commutation classes through seven points
gave maxima

| `n` | 3 | 4 | 5 | 6 | 7 |
|---:|---:|---:|---:|---:|---:|
| maximum `K` | .7500 | .5333 | .7407 | .6667 | .5753 |

and produced no smaller finite obstruction.

## 3. Exact planar stress records

The full link census gives:

| configuration | `n` | exact `K` |
|---|---:|---:|
| RNP coordinate record | 24 | **1.064785** |
| ACP coordinate record | 24 | 1.051561 |
| APA counterexample | 44 | .154416 |
| finite `H>2` counterexample | 58 | .034237 |
| central Pascal `m=4` | 6 | .588235 |
| central Pascal `m=5` | 10 | .638298 |
| central Pascal `m=6` | 20 | .588934 |
| central Pascal `m=7` | 35 | .375205 |
| vertical `T_(4,2)[T_(4,2)]` | 36 | .255396 |
| guarded templates `k=3,4,5` | 7, 11, 25 | .415842, .416667, .352793 |
| guarded `k=3` vertical square | 49 | **.002133** |

In particular, the two exact planar counterexamples that killed constant-two
deletion have very small rankwise near-maximal mass.  There is no sign that
their local peak can amplify RNP.

## 4. Rigorous scalable profile upper bounds

For counterfamily testing it is unnecessary to enumerate `u(A)`: simply use

\[
 K(P)\leq
 \max_{r<L}{2^{L-r}v_r(P)\over Z_P(1)}.                 \tag{6}
\]

The right side is computed exactly by the graded directional-composition
recurrences.  Because it counts **all** faces, decay in (6) rules out a hidden
near-maximal subfamily at the tested ranks.

### Central Pascal cells

| Pascal parameter `m` | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 12 | 14 | 16 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| profile upper bound (6) | .588 | .638 | .589 | .566 | .513 | .135 | .104 | .0668 | .0433 | **.0290** |

After the harmless increase from `m=4` to `m=5`, the bound decreases, with a
sharp drop when the ceiling `L` stops following the top low rank.  These are
the balanced constructions that approach the expected coefficient one-half;
they do not threaten RNP.

### Indecomposable guarded towers

For each fixed guarded template, the exact cap, cup, and convex profiles were
fed into the homogeneous vertical recurrence through depth eight.

| template | depth 1 upper | depth 2 upper | depth 3 upper | depth 8 upper |
|---|---:|---:|---:|---:|
| guarded `k=3`, size 7 | .415842 | .0819655 | 9.14e-4 | 1.91e-36 |
| guarded `k=4`, size 11 | .416667 | .0095245 | 1.73e-5 | 6.32e-51 |
| guarded `k=5`, size 25 | .401454 | .0066256 | 3.18e-8 | 6.77e-57 |

The guarded towers are the explicit scalable obstruction to extracting a
near-spanning decomposable subset.  Yet their rankwise profile upper bounds
collapse superpolynomially in these exact finite recurrences.  This is the
strongest evidence from this lane: the main known indecomposable construction
behaves much better than the required `poly(log n)` envelope.

Wrappers likewise cannot amplify the statistic in the tested regime.  They
create a few small maximal hull faces, but their large internal Boolean or
convex mass makes the denominator overwhelm the factor `2^(L-r)`.

## 5. Stronger finite targets suggested by the data

The numerically sharp conjecture left by the optimized record is

\[
 \boxed{2^{L-r}N_r(P)\leq{16\over15}Z_P(1)
 \quad\text{for every }r<L.}                            \tag{RNP-16/15}
\]

The constants `1` and `17/16` are definitely false by (5).  The optimized
record lies only `0.0018813` below `16/15`, so this boundary also needs more
kill-search before being trusted.  At its maximizing rank the conjecture is
the profile balance `14v_4<=16(V-v_4)`; the record misses equality by
`16V-30v_4=284`.  The robust fallback `K<=4/3` has substantial finite margin
and is still far stronger than the polylogarithmic theorem needed for Erdős
838.  Every exact record and every rigorous profile upper bound in this audit
satisfies both surviving targets.  No structural reason for either particular
constant is claimed.

A proof should charge each low-addable rank-`r` face to roughly `2^(L-r)`
ordinary convex faces.  The threshold `u(A)<=4(r+1)` says that almost every
external point is blocked.  The exact nested-repair classification then
places those blockers into consecutive tangent replacement intervals.  The
missing Hall statement is that either these intervals generate the required
number of distinct tangent-pocket faces, or their concentration recurses to
a retained two-tangent instance without losing more than a constant number
of histories.  The profile data show that repeated recursion has ample mass;
the unresolved step is bounded inverse multiplicity.

## 6. Reproduction

Run

```bash
python3 phase2/loop/erdos838/agent_generalized_deletion/rankwise_nearmax_audit.py
```

It verifies (5) from exact rational coordinates, imports the exact rooted-link
censuses, computes central Pascal profile bounds through `m=16`, and computes
the three guarded vertical recurrences through depth eight.  It writes
`rankwise_nearmax_certificate.json`.  The stretchable search driver is
`search_rankwise_nearmax.py`.
