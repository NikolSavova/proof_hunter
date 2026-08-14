# Exact lexicographic minima, deletion stability, and the cyclic-cluster fork

**Date:** 2026-08-13
**Status:** two new exact finite values and a rejected natural asymptotic
continuation; no proof of the full asymptotic Erdős 838 problem.

## 1. Headline verdict

The finite minimizer search can now be made exhaustive one order farther in
the full reflection-order model and two orders farther for actual point sets.
Write

\[
 V^+(P)=\#\{\varnothing\ne A\subseteq P:A\text{ is in convex position}\},
 \qquad M(P)=\sum_A |A|.
\]

Then:

* among **all** 1,232,944 type-\(A_7\) reflection-order commutation classes,
  the lexicographic minimum of \((V^+,M)\) is
  \((113,316)\); 2,080 classes minimize the count and 724 also minimize the
  first moment;
* the complete realizable order-type database independently gives the same
  eight-point minimum, with 12 order types minimizing the count and four
  minimizing \((V^+,M)\);
* among all 158,817 realizable nine-point order types, the unique database
  minimizer is

  \[
    Z(z)=9z+36z^2+84z^3+36z^4+3z^5,
    \qquad (V^+,M)=(168,492).                    \tag{1}
  \]

The official frozen problem defines `v(P)` using all subsets and therefore
includes the empty set.  Thus the corresponding exact official values are

\[
                         \boxed{f(8)=114,\qquad f(9)=169}.              \tag{2}
\]

Every mean, variance, and deletion identity below uses the nonempty
convention, so that the probability space is exactly the partition function
used in the mean-size attack.  Adding the empty set changes `V` to `V+1` but
does not change `M` or the unnormalized second moment.

These finite theorems sharpen the attack but do not establish an asymptotic
mean bound.  The deficits continue to move downward:

\[
  \mu_8-\log_2 8=-0.2035398230\ldots,
  \qquad
  \mu_9-\log_2 9=-0.2413535729\ldots.            \tag{3}
\]

The simple strengthened guess `mu >= log2(n)-1/4` survives by only
`0.0086464...` at nine points.

## 2. Why the coverage is exhaustive

### 2.1 Eight points: all reflection orders

For every triple `a<b<c`, a reflection order restricts to exactly one of

```text
ab < ac < bc,              bc < ac < ab.
```

`exact_bruhat.cpp` stores that choice as one bit.  These packet orientations
give the precedence heap on the 28 positive roots.  A packet is flippable
exactly when its three roots form a convex interval of the heap.  Breadth-first
search from the bubble order therefore enumerates the higher Bruhat order
`B(8,2)`, equivalently all commutation classes of reduced decompositions of
`w_0 in S_8`.  A lexicographically least topological order supplies a
canonical root sequence, and exact transvection products give `V` and `M`.

The implementation reproduces all previous class counts and minima through
seven points, including

```text
n=7: 24,698 classes, (V,M)=(72,190), 152 lex classes.
```

At eight points it gives

```text
classes                         1,232,944
minimum V+                            113
V+-minimizing classes               2,080
minimum M within V+=113                316
lex-minimizing classes                 724
```

Every generic planar point set, after sorting by horizontal coordinate and
then by edge slope, supplies one of these reflection orders.  Commuting
disjoint roots does not change either transvection product.  Hence 113 is a
lower bound for actual eight-point sets.  One winning class has the exact
fixed-`x` realization

```text
x = 0,1,2,3,4,5,6,7
y = 0,-8786,-19571,-55024,-81143,-23929,-5381,3167,
```

which supplies the matching upper bound.  This proves the eight-point result
without relying on the external order-type database.

### 2.2 Eight and nine points: all realizable order types

The Aichholzer--Aurenhammer--Krasser database contains one integer-coordinate
representative of every inequivalent realizable order type, retaining one
member of each reflection pair.  Convex-subset profiles are invariant under
relabeling and reflection.  Its documented record counts are 3,315 and
158,817, exactly the counts parsed by the scanners.

There are three independent checks:

1. `scan_order_types.cpp` reads every coordinate representative and
   recomputes the complete rank polynomial by cap--cup endpoint
   factorization.
2. `verify_database_profiles.py` independently scans the provider's aligned
   `kgons` files, without reading slopes or multiplying matrices.
3. `direct_hull_verify.py` takes the two winning integer configurations and
   examines every one of their `2^n` subsets by an exact monotone-chain hull
   test.

All three agree.  The winning nine-point coordinates, in the database's
stored order, are

```text
(62614, 7322), (2922, 4014), (10209,14386),
(20660,24299), (33336,29017), (30137,33324),
(15334,45211), (14934,55621), (10934,61521).
```

The smallest absolute orientation determinant among its 84 triples is
374,774, so general position is certified with a large integer margin.  Its
database record index is 151,740 (zero based).  It is the only database order
type with `V+=168`, hence also the unique lex minimum up to the database's
relabeling/reflection equivalences.

Exact file sizes, SHA-256 hashes, provider usage terms, completeness scope,
and retrieval commands are recorded in `DATABASE_PROVENANCE.md`.  The large
external files are not committed.

## 3. Rank profiles and the crossing-number connection

The eight-point count minima have precisely three profiles:

| profile from size 1 upward | order types | `M` |
|---|---:|---:|
| `(8,28,56,19,2)` | 2 | 318 |
| `(8,28,56,20,1)` | 6 | 317 |
| `(8,28,56,21)` | 4 | 316 |

Thus lexicographic moment minimization selects the last profile.  It moves
mass downward from size five to size four.

The number `v_4(P)` of convex quadrilaterals is exactly the number of
crossings in the straight-line drawing of `K_n`: each convex quadrilateral
has one crossing diagonal pair and every crossing determines its four
endpoints.  The provider's `crossn` data give rectilinear crossing minima 19
at `n=8` and 36 at `n=9`, agreeing with its documentation.  Consequently:

* the two count-minimizing eight-point types with profile `(19,2)` are also
  crossing-minimal, but the lex mean selects `v_4=21,v_5=0` instead;
* the unique nine-point convex-count minimizer has `v_4=36,v_5=3` and is one
  of the ten crossing-minimal nine-point order types.

This explains the visual three-cluster structure of the finite records, but
it also warns that minimizing crossings and minimizing all convex subsets
already diverge at eight points.

## 4. Variance and exact deletion stability

Let `K` be the size of a uniformly random **nonempty** convex subset and let
`R=sum k^2 v_k`.  For each deletion `P-p`, put `(V_p,M_p)` for its nonempty
count and first moment.  Double counting gives

\[
 \sum_p V_p=nV-M,\qquad \sum_pM_p=nM-R.           \tag{4}
\]

Therefore the `V_p`-weighted deletion mean is

\[
 \bar\mu_{\rm del}=\frac{nM-R}{nV-M},
 \qquad
 \mu-\bar\mu_{\rm del}=\frac{\operatorname{Var}(K)}{n-\mu}.            \tag{5}
\]

At the new minima:

| `n` | `(V,M,R)` | nonempty variance | decimal |
|---:|---|---|---:|
| 8 | `(113,316,960)` | `8624/12769` | 0.675385700 |
| 9 | `(168,492,1560)` | `139/196` | 0.709183673 |

For comparison, the exact variance sequence at lex minima for `n=2,...,9`
is

```text
0.22222, 0.48980, 0.57143, 0.65828,
0.65702, 0.67515, 0.67539, 0.70918.
```

Thus a finite bound `Var >= 1/ln 2` is false by a wide margin; even
`Var >= ln 2` fails at eight points.  The data instead cluster near `ln 2`,
but provide no theorem that the variance stays bounded below or converges.
If the empty set is included in the sampling law, the variances become
`2396/3249=0.73746...` and `21576/28561=0.75544...`; these are not the
quantities in (5) as used here.

There is a useful exact stability statistic.  If

\[
 g_n=\min_{|P|=n}V^+(P),qquad
 \Delta(P)=\sum_p(V(P-p)-g_{n-1}),                \tag{6}
\]

then

\[
 \Delta(P)=n(V(P)-g_{n-1})-M(P).                 \tag{7}
\]

It is a nonnegative integer.  Since each nonminimal deletion contributes at
least one, at least `n-Delta(P)` deletions are count-minimal whenever this is
positive.  This is a genuine general stability lemma.

For the eight-point lex winner,

```text
deletion V histogram: 72 x 3, 74 x 4, 76 x 1
Delta = 12
lex (72,190) children: 3.
```

For the unique nine-point winner,

```text
deletion V histogram: 113 x 6, 114 x 3
deletion (V,M): (113,317) x 3, (113,318) x 3, (114,321) x 3
Delta = 3
lex (113,316) children: 0.
```

In recurrence form,

\[
 g_8-g_7=41=\frac{M_8}{8}+\frac{12}{8},\qquad
 g_9-g_8=55=\frac{M_9}{9}+\frac{3}{9}.           \tag{8}
\]

The second identity is strikingly tight: six of the nine deletions are
global count minimizers.  But none is a lex minimizer.  Hence small deletion
excess alone cannot yield a hereditary lex-minimizer chain; (1) is an exact
counterexample to that tempting strengthening of (7).

## 5. Exact three-cluster structure

The standard projection definition says that a `3m`-point set is
3-decomposable if it has an equal partition `A,B,C` and three projection
directions putting, respectively, each of `A,B,C` strictly between the other
two clusters.

`cluster_structure.py` examines every 280 unordered partition candidates.
For a proposed order `L<M<R`, it solves the homogeneous strict inequalities

\[
 u\cdot(m-l)>0,\qquad u\cdot(r-m)>0
\]

and then verifies a returned integer `u` by exact dot products.  Results:

* the unique nine-point minimizer has exactly one `3+3+3` decomposition;
* the selected eight-point minimizer, which cannot be 3-decomposable in the
  standard equal-size sense, has exactly one balanced `3+3+2` projection
  analogue.

For the nine-point coordinates sorted by `x`, the clusters are

```text
A = {0,1,5},       B = {2,3,4},       C = {6,7,8}.
```

The exact integer projection-direction certificates are stored in
`cluster_certificates.json`.  The three directions are pairwise nonparallel,
so parallel supporting translates form an enclosing triangle with the
required projection orders.

## 6. The cyclic three-cluster continuation is not an escape

The three-cluster structure suggested a genuinely different mixed geometry
from the vertical blow-ups.  `triangular_ifs_probe.py` tests the most literal
self-affine continuation:

1. take the centroids of the three minimizing clusters as a macro triangle;
2. at each macro vertex fit the unique affine map carrying the macro triangle
   to the three observed cluster deviations;
3. choose an identification of the three micro vertices independently at
   each macro vertex;
4. recursively apply the same three maps.

At depth two the union is exactly the integer nine-point minimizer.  All
`6^3=216` identifications were evaluated exactly at depth three.  Their traces
range from 22,862 to 32,443 and their mean deficits from `-0.09558...` to
`+0.26207...`.  The depth-three lex-best identification is

```text
(0,1,2), (2,0,1), (0,2,1).
```

Iterating that identification gives:

| depth | `N=3^d` | `log2 V` | `mu` | `mu-log2 N` | normalized `log2 V` | max convex size |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 2.8074 | 1.7143 | +0.1293 | 1.1175 | 3 |
| 2 | 9 | 7.3923 | 2.9286 | -0.2414 | 0.7357 | 5 |
| 3 | 27 | 14.4807 | 4.6593 | -0.0956 | 0.6405 | 9 |
| 4 | 81 | 25.6990 | 7.8314 | +1.4915 | 0.6394 | 16 |
| 5 | 243 | 44.4835 | 13.7397 | +5.8149 | 0.7083 | 28 |
| 6 | 729 | 77.6602 | 24.3803 | +14.8705 | 0.8587 | 50 |
| 7 | 2187 | 134.7978 | 42.2083 | +31.1135 | 1.0951 | 88 |

Counts and means through depth five use exact rational coordinates and exact
integer products.  Depths six and seven use `logspace_ifs_probe.cpp`: it
sorts long-double slopes but then requires the resulting root list to pass
the full adjacency/`w_0` sorting-network check; path counts use stable
log-sum-exp and mean degrees use the exact weighted update formula.  The
maximum sizes use max-plus on the same checked order.  An independent exact
rational max-plus run in `agent_root_variance/cyclic_ifs_maxplus.py` confirms
the maximum-size sequence through depth six and supplies explicit digit-word
witnesses.

The observed ratios suggest

\[
          \log V(P_d),\ \max|Q| = 3^{(1/2+o(1))d}=N^{1/2+o(1)},          \tag{9}
\]

so this construction appears to have `V=2^{Theta(sqrt N)}`, enormously more
than quasipolynomial.  This is an inference, not a proved recurrence.  But
the finite direction is decisive: after a shallow dip, both the normalized
count and the mean deficit accelerate upward.  The natural cyclic
continuation neither refutes the mean-size conjecture nor improves the
coefficient-one-half upper construction.

The quantifier boundary matters.  All 216 micro identifications were searched
only at depth three, and only the depth-three lex winner was continued.
Different depth-dependent maps or a nonstationary three-cluster geometry are
not ruled out.  Also, shrinking the fitted deviations to an infinitesimal
scale crosses an order-type wall: the nine-point trace becomes 177 rather
than 168.  Thus the finite minimizer is not the first level of a clean
scale-separated substitution formula.

## 7. Full endpoint and braid-boundary checks

For the displayed coordinate directions, the endpoint product arrays are
fully recorded in `boundary_probe.json`.  Their endpoint-distribution
entropies are 4.73087 bits at `n=8` and 4.98840 bits at `n=9`, respectively
0.439 and 0.503 bits below uniform on the `n(n+1)/2` possible endpoint pairs.
The largest endpoint fibres are only 9 and 14.  Thus the minimizing mass is
spread across the full boundary array rather than concentrated in one cell.

For the canonical global reflection-order lex winner at eight points, all
eight heap-exposed long-braid neighbors have nonnegative, in fact strict,
dual-number slack.  The exact `(Delta V,Delta M)` histogram is

```text
(0,1) x2, (1,4) x1, (2,9) x1,
(3,12) x2, (4,17) x1, (4,19) x1.
```

This validates the full-boundary local necessary condition on the new global
minimum.  It does not yet suggest an amortization inequality: two directions
are count-neutral but cost only one unit of first moment, and endpoint cap or
cup totals themselves vary under the choice of generic horizontal direction.
The data support retaining the entire rank-one boundary vectors, as the
global braid report recommends, rather than replacing them by a scalar
balance statistic.

## 8. Reproduction and claim boundary

From the repository root:

```bash
c++ -O3 -std=c++17 phase2/loop/erdos838/agent_lex_minimizer_search/exact_bruhat.cpp -o /tmp/exact_bruhat
/tmp/exact_bruhat 7
/tmp/exact_bruhat 8

c++ -O3 -std=c++17 phase2/loop/erdos838/agent_lex_minimizer_search/scan_order_types.cpp -o /tmp/scan_order_types
/tmp/scan_order_types 8 b08 /path/to/otypes08.b08
/tmp/scan_order_types 9 b16 /path/to/otypes09.b16
python3 phase2/loop/erdos838/agent_lex_minimizer_search/verify_database_profiles.py --data-dir /path/to/data

python3 phase2/loop/erdos838/agent_lex_minimizer_search/direct_hull_verify.py
python3 phase2/loop/erdos838/agent_lex_minimizer_search/analyze_minimizers.py
python3 phase2/loop/erdos838/agent_lex_minimizer_search/cluster_structure.py
python3 phase2/loop/erdos838/agent_lex_minimizer_search/triangular_ifs_probe.py
python3 phase2/loop/erdos838/agent_lex_minimizer_search/boundary_probe.py

c++ -O3 -std=c++17 phase2/loop/erdos838/agent_lex_minimizer_search/logspace_ifs_probe.cpp -o /tmp/logspace_ifs_probe
/tmp/logspace_ifs_probe 7
```

**Certified internally:** the all-reflection-order result through `n=8`, its
rational realization, every reported exact evaluation/profile, direct hull
censuses of the winners, variance/deletion identities, cluster projection
certificates, and rational self-affine counts through depth five.

**Database-assisted:** exhaustiveness over realizable order types at `n=8,9`
uses the provider's documented completeness theorem and the exact external
file hashes in `DATABASE_PROVENANCE.md`.

**Numerical but strongly checked:** depth-six/seven log-space IFS counts.

**Not proved:** any asymptotic recurrence for the cyclic construction,
`mu>=log n-O(1)`, an amortized full-boundary braid theorem, or Erdős 838.

The best next lower-bound move remains the minimizer-specific mean theorem.
The deletion calculation says what a viable induction must handle: it should
be stable under near-minimal **count** deletions but cannot demand an actual
lex-minimal child.  The cyclic-cluster experiment, meanwhile, removes the
most natural finite-minimizer-derived counterfamily from the upper side.
