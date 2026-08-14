# Erdős 838: planar affine-lattice mean attack

**Date:** 2026-08-13
**Verdict:** the minimizer-only mean inequality is not proved, and no
counterexample family was found.  The attack produces two exact reductions:
an iterated deletion--variance identity and a Boolean-interval coverage
inequality.  Together they isolate the missing planar statement as control of
external points blocked by rooted four-circuits.  Generic shattering
extremality supplies no information.  The exact `n=9` lex minimizer is
3-decomposable, but the affine-lattice scalar statistics tested here do not
distinguish that cyclic structure.

All logarithms are base two.  The empty convex subset is included throughout.
Thus `V` is one more than the nonempty reverse-product trace.

## 1. Exact deletion--variance identity

Let `A` be a uniformly random convex subset of an `n`-point configuration
`P`, and put

```text
mu(P)=E|A|,                 sigma(P)^2=Var(|A|).
```

For `p in P`, write `V_p=V(P-p)` and `mu_p=mu(P-p)`.  Directly counting a
convex subset once for every point it omits gives

```text
sum_p V_p       = (n-mu)V,                               (1)
sum_p V_p mu_p  = n mu V - V E|A|^2.                    (2)
```

Consequently, under the deletion law

```text
Pr(delete p)=V_p/((n-mu)V),                              (3)
```

one has the exact identity

```text
mu(P)-E_p mu(P-p)=sigma(P)^2/(n-mu(P)).                  (4)
```

This law has a simple coupling: choose uniformly a pair `(A,p)` with `A`
convex and `p notin A`, then delete `p`.  Conditional on the child ground set,
`A` is again a uniform convex subset.  Iterating (4) down to the empty ground
set therefore gives the exact variance ladder

```text
mu(P)=E [ sum_(m=1)^n sigma(P_m)^2/(m-mu(P_m)) ],        (5)
```

where `P_n=P` and `P_(m-1)` is obtained from `P_m` by (3).

This makes the required scale transparent.  If the deletion-chain average
variance were at least `1/ln 2-o(1)`, then (5) would give

```text
mu(P) >= (1/ln 2-o(1)) ln n = log2 n-o(log n).           (6)
```

But a pointwise variance bound of this strength is false even on the exact
small low-trace records.  Their variances lie between about `0.707` and
`0.94`, whereas `1/ln 2=1.442695...`.  Thus a successful variance proof must
be averaged along the deletion chain, become asymptotic, or use a
minimizer-specific compensation when the variance is small.  Equation (5),
not a universal one-step variance inequality, is the viable statement.

## 2. Boolean intervals give a planar coverage target

For a uniform closed set `K`, put

```text
H=|ext(K)|,       I=|K|-H,       O=n-|K|.
```

Thus `H` is distributed as `|A|`, `I` counts points in the relative interior
of the selected hull, and `O` counts points outside that hull.  The Boolean
interval identity at `t=1` is

```text
2^n = sum_K 2^I = V E[2^I].                           (7)
```

Jensen and `I=n-H-O` give the universal inequality

```text
boxed:  log V <= mu + E O.                            (8)
```

This converts the surviving low-mean QMS branch into an explicitly planar
coverage problem.

> **Low-mean coverage target.**  If `P_n` minimizes `V` and
> `mu(P_n)<(1-o(1))log n`, prove
>
> ```text
> E O <= mu^2/2-mu+o(mu^2).                           (9)
> ```

Equations (8)--(9) give
`log V<=mu^2/2+o(mu^2)`, exactly branch (B) of the already-proved low-mean
minimizer dichotomy.  Hence (9), only on low-mean minimizers, suffices for the
coefficient `1/2` theorem.

There is a sharper rooted-circuit interpretation.  For a convex subset `A`,
let `u(A)` be its up-degree: the number of `p` for which `A union {p}` remains
convex.  Every addable point lies outside `conv(A)`, and average up-degree
equals average down-degree in the finite face poset.  Therefore

```text
E u(A)=mu,
E O=mu+E B,                                           (10)
```

where `B(A)` is the number of **blocked exterior points**: points outside the
hull which cannot be added while preserving all vertices of `A`.  If `p` is
blocked, some `b in A` ceases to be extreme in `A union {p}`.  Since `b` was
extreme in `A`, planar Carathéodory supplies `a,c in A` such that

```text
b in conv{a,c,p}.                                     (11)
```

Thus `(a,c,p;b)` is a rooted four-circuit.  Conversely, such a rooted circuit
supported on `A union {p}` blocks `p`.  The low-mean coverage target is
equivalently

```text
E B <= mu^2/2-2mu+o(mu^2).                            (12)
```

This is the exact new geometric bottleneck.  A proof must control the
multiplicity of exterior points sharing tangent/rooted-circuit witnesses.
The tangent-pruning work elsewhere in this campaign shows why a naive
bounded-fibre assertion is unavailable: long visible chains carry unbounded
history.  Deletion minimality must be used to show either that these fibres
are small on average or that a large fibre already creates sufficiently many
other convex subsets.

## 3. A second differentiated Boolean identity

The verifier also checks the two derivatives of

```text
(1+t)^n=sum_K t^H(1+t)^I.
```

Under the measure proportional to `2^I`, put `X=H+I/2`.  Exact logarithmic
differentiation at `t=1` gives

```text
E_2^I X = n/2,
Var_2^I(X) + E_2^I I/4 = n/4.                     (13)
```

This is a complete second-moment description under the interior-weighted
law, but it still does not control uniform `H`: the exponential change of
measure can concentrate on a few large-interior hulls.  Formula (8) extracts
the strongest immediate uniform consequence via Jensen.  Any stronger use of
(13) needs minimizer-specific correlation between `H`, `I`, and `O`.

## 4. Why shattering extremality is vacuous here

The independent sets of an affine convex geometry form a simplicial complex
`F`.  For **every** simplicial complex, not just a planar one,

```text
S is shattered by F  iff  S belongs to F.          (14)
```

Indeed, if `S in F`, heredity supplies every trace on `S`.  Conversely, if
`S` is shattered, some face has trace `S`, hence contains `S`, and heredity
again gives `S in F`.  Therefore every simplicial complex is
shattering-extremal in the equality-of-cardinalities sense relevant here.
No planar expansion can follow from that label alone.  The rooted-circuit
locations, not merely the collection of shattered sets, are essential.

Generic antimatroid or toggle-CDE arguments are similarly insufficient: the
campaign already has an exact rational non-toggle-CDE witness at `n=7`, and
abstract convex geometries can have chain-like closure lattices.  Planar
rooted four-circuits and minimizer status are load-bearing.

## 5. Exact realizable minimizer and cyclic structure

The separate exhaustive realizable order-type database now gives the unique
lex minimizer at `n=9`:

```text
nonempty trace = 168,
profile         = 9,36,84,36,3,
first moment    = 492.
```

Including the empty set, the exact affine-lattice statistics are

```text
V                       = 169,
mu                      = 492/169,
variance                = 21576/28561 = 0.755432...,
mean interior I         = 111/169,
mean omitted O          = 918/169,
mean blocked exterior B = 426/169.
```

The verifier independently confirms standard 3-decomposability.  After
sorting the stored integral coordinates, the clusters are

```text
{0,1,5}, {2,3,4}, {6,7,8}.
```

The exact integer projection directions

```text
(867574037,-497308043),
(910323393, 413897717),
(505573743, 862783397)
```

put each of the three clusters between the other two in turn.  This is a
genuine cyclic triangular structure outside the vertical-composition
barriers.

However, the tested affine-lattice scalars do not detect it.  A nearby
stretchable `V=170` record has

```text
mu=497/170, variance=22441/28900,
mean omitted=923/170, mean blocked=426/170,
```

nearly the same values.  At `n=17` and `n=20`, independently evolved
low-trace records have mean deficits `-0.35988` and `-0.34287`, and variances
`0.70734` and `0.76333`.  None falsifies `mu>=log n-O(1)`, but none supports a
large pointwise variance gap either.

The exact rational cyclic three-cluster IFS probe in
`agent_lex_minimizer_search/triangular_ifs_certificate.json` also fails to
produce a counterexample family.  Its mean deficits at sizes
`9,27,81,243` are

```text
-0.24135, -0.09558, +1.49155, +5.81492,
```

while its normalized traces are

```text
0.73567, 0.64048, 0.63938, 0.70831.
```

These IFS rows use the nonempty convention of that certificate; adding the
empty set changes only the finite displayed values, not the upward trend.

The finite dip turns upward, and there is no evidence for coefficient below
`1/2` or for an unbounded negative mean deficit.

## 6. Honest conclusion and next lemma

The minimizer-only inequality

```text
mu >= log n-O(1)
```

remains open.  The best new theorem-level statements are (5) and (8).
Together they suggest a precise minimizer-specific dichotomy:

1. sufficiently large variance accumulates along the weighted deletion chain
   and pays for `log n` through (5); or
2. low variance/rank concentration forces the blocked rooted-circuit mass in
   (12) to be at most quadratic in `mu`, yielding QMS through (8).

The unproved content is the second implication.  A viable proof must retain
tangent-pair multiplicities or use a large-fibre-to-many-faces alternative;
rank counts, shattering extremality, interior-weighted moments, and generic
toggle symmetry do not suffice.

## 7. Verification

From the repository root:

```bash
python3 -m py_compile \
  phase2/loop/erdos838/agent_planar_lattice_mean/planar_lattice_mean.py

python3 phase2/loop/erdos838/agent_planar_lattice_mean/planar_lattice_mean.py \
  phase2/loop/erdos838/agent_growing_state_upper/LARGE_MACRO_CERTIFICATE.json \
  --sizes 9,17,20 \
  --direct-n9 \
  phase2/loop/erdos838/agent_lex_minimizer_search/exact_realizable_n9.json \
  --output phase2/loop/erdos838/agent_planar_lattice_mean/CERTIFICATE.json
```

The checker enumerates every convex subset at the displayed sizes,
reconstructs every affine closure, verifies the full coefficientwise Boolean
interval identity, both differentiated identities in (13), both deletion
identities (1)--(2), the variance gap (4), and the three exact projection
orders of the `n=9` decomposition.  All stored finite quantities before the
displayed decimal conversions are integers or reduced rational numbers.
