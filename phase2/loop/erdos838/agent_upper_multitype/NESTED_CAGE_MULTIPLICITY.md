# Erdős 838: what nested convex cages do and do not multiply

## Summary

Let `K_1,...,K_D` be pairwise disjoint convex subsets of a planar
general-position point set, ordered so that

```
conv K_{i+1} subset int(conv K_i).
```

Put `m_i=|K_i|` and `M=sum_i m_i`.  Nesting gives a useful exact tangency
count, but not a product over layers.  The rigorous universal bound obtained
here is

```
V(P) >= sum_i (2^{m_i}-1)
      + sum_{i<j} sum_{x in K_i} (2^{h_{ij}(x)}-1),       (1)
```

where `h_{ij}(x)` is the number of vertices of `K_j` that remain vertices
after adjoining `x`.  These exposure numbers satisfy

```
h_{ij}(x)>=2,                 sum_{x in K_i} h_{ij}(x)>=m_j.  (2)
```

Consequently

```
V(P) >= sum_i (2^{m_i}-1)
      + sum_{i<j} m_i(2^{max(2,m_j/m_i)}-1).       (3)
```

This should be combined with the general bound on the union of the cages,

```
V(P) >= f(M)
     >= 2^{(1/4-o(1))(log M)^2}.                  (4)
```

For uniformly bounded cage sizes, (3) is only quadratic in `D`, and (4) is
asymptotically stronger.  The nesting-specific gain becomes substantial only
when an inner cage is much larger than an outer cage.

There is no universal per-layer product in the regime produced by the
hull-partition argument.  An exact pair of nested triangles already refutes
the most naive product, and the paper's own iterated blow-ups plus the
nested-cage corollary refute every `2^{Omega(D)}` conclusion when the cage-size
cap is `O((log D)^2)`.

All convex-subset counts below are nonempty; adding the empty set changes each
display by at most one.

## 1. The exposed-arc lemma

Let `A` and `B` be convex-position point sets with

```
conv B subset int(conv A).
```

For `x in A`, define

```
F_x = B intersect vert(conv(B union {x})),
h_x = |F_x|.
```

Thus `F_x` is the far boundary arc of `B` between the two tangency vertices
seen from `x`.

### Lemma 1 (exposed arcs cover the inner cage)

For every `x in A`, `h_x>=2`, and

```
union_{x in A} F_x = B.                            (5)
```

In particular,

```
sum_{x in A}h_x >= |B|.                           (6)
```

#### Proof

The point `x` lies strictly outside `conv B`.  The two supporting tangents
from `x` to the polygon `conv B` have distinct contact vertices; general
position excludes a tangent through an edge of `B` and `x`.  Both contacts
remain vertices after `x` is adjoined, so `h_x>=2`.

Now fix `y in B`.  Choose a vector `u` in the interior of the normal cone of
`conv B` at `y`.  Then `y` is the unique maximizer of `u dot z` on `B`.
Because `y` lies in the interior of `conv A`, a small open ball about `y` is
contained in `conv A`.  Hence some vertex `x` of `A` satisfies

```
u dot x < u dot y.
```

The same functional `u` still uniquely exposes `y` in `B union {x}`.
Therefore `y in F_x`, proving (5), and (6) follows by double counting.
`square`

### Lemma 2 (two-layer multiplicity)

The number of convex subsets contained in `A union B`, meeting `A` in exactly
one point and meeting `B` nontrivially, is at least

```
sum_{x in A}(2^{h_x}-1)
 >= |A|(2^{max(2,|B|/|A|)}-1).                    (7)
```

#### Proof

The set `F_x union {x}` is the vertex set of `conv(B union {x})`, so it is in
convex position.  Every one of its subsets is therefore in convex position.
For fixed `x`, the sets

```
{x} union T,          emptyset != T subseteq F_x,
```

give `2^{h_x}-1` distinct convex subsets.  Sets belonging to different `x`
are distinct.  Finally, convexity of the exponential, (6), and `h_x>=2` give

```
sum_x 2^{h_x}
 >= |A| 2^{(sum_x h_x)/|A|}
 >= |A| 2^{max(2,|B|/|A|)}.
```

Subtracting `|A|` proves (7). `square`

## 2. Summing without overlap

Apply Lemma 2 to every ordered layer pair `i<j`.  A set counted for `(i,j)`
uses exactly one point of `K_i`, at least one point of `K_j`, and no other
cage.  Thus families belonging to different pairs have different layer
supports and are disjoint.  They are also disjoint from the nonempty subsets
lying within a single cage.  This proves (1), and Jensen gives (3).

If every cage has at least three vertices, the crude consequence is

```
V(P) >= 7D + 9 binom(D,2).                         (8)
```

This is a genuine nesting count, but it is only polynomial.  Independently,
the union `R=K_1 union ... union K_D` has `M` points and every convex subset
of `R` is also one of `P`, proving `V(P)>=f(M)` and hence (4).

No iteration of Lemma 2 is automatic.  After choosing an exposed arc in one
inner cage, the compatible arcs in a still deeper cage depend on the whole
previous choice, and the same final convex set can arise from many tangency
histories.  Treating the pair factors in (7) as independent is precisely the
fibre error exposed by the counterexamples below.

## 3. Exact smallest product failure: two nested triangles

Take the outer triangle

```
K_1 = {(0,0),(100,0),(0,100)}
```

and the inner triangle

```
K_2 = {(200/13,350/13),(275/8,175/4),(100/13,1100/13)}.
```

Every coordinate of every inner vertex is a strict positive barycentric
combination of the outer vertices, so `conv K_2` is strictly inside
`conv K_1`.  Exact determinant checks show that the six points are in general
position.  Their convex-subset profile, including the empty set, is

```
(v_0,v_1,v_2,v_3,v_4,v_5,v_6) = (1,6,15,20,3,0,0).
```

Thus they have exactly

```
V(K_1 union K_2)=44
```

nonempty convex subsets.  But each triangle separately has seven nonempty
convex subsets, and

```
(2^3-1)(2^3-1)=49>44.                             (9)
```

So even the weakest-looking product of the within-cage enumerators fails at
`D=2`, with equal cage sizes three.  The script `nested_cage_search.py`
constructs this example at depth `2`, seed `2844`, and recomputes `V=44` by
an orientation-only endpoint DP.

For another elementary failure, selecting one point from each nested layer
does not necessarily give a convex set.  The same script at depth `4`, seed
`4840`, has a transversal of four first-listed vertices whose hull has only
three vertices.  Hence the `product_i m_i` transversals cannot simply be
declared convex.

## 4. Asymptotic obstruction to every per-layer factor

The exact two-triangle example kills a literal product of within-layer
counts.  There is a stronger asymptotic obstruction in exactly the
polylogarithmic cage-size regime of Corollary 7.

Take any fixed-template iterated vertical blow-up from the upper-bound paper.
At depth `d` it has

```
N=r^d,                 log V=O(d^2)=O((log N)^2). (10)
```

Apply Corollary 7 of `HEREDITARY_MULTIPLICITY_BARRIER.md` to this point set.
It supplies nested disjoint cages satisfying

```
D >= N/O((log N)^2),       max_i m_i=O((log N)^2). (11)
```

Thus `log D=Theta(log N)` and the same ambient point set has

```
V=2^{O((log D)^2)},        max_i m_i=O((log D)^2). (12)
```

Consequently, no theorem based only on `D`, nesting, and the size cap
`m_i=O((log D)^2)` can force

```
V >= 2^{Omega(D^epsilon)}
```

for any fixed `epsilon>0`; in particular it cannot give a constant factor
greater than one per cage.  This is a rigorous existence argument, not a
heuristic picture of concentric polygons.

It does not settle the more restrictive question in which every cage has an
absolute constant number of vertices.  The two-triangle example shows that
the obvious product still fails there, but the best asymptotic bound for a
long sequence of nested triangles remains open in this audit.

## 5. Implication for the unrestricted lower-bound attack

For the cages produced by the hull-partition identity, the maximum cage size
is `w+1`, where `w=log V(P)`.  Equations (3)--(4) do not create a feedback
contradiction:

* when all `m_i=O(w)` are comparable, the tangency term is only polynomial in
  `D`;
* the general `f(M)` term is the existing hereditary `1/4` bound applied to
  the cage union;
* an exponential-in-`D` multiplication is impossible by (12).

The nested-cage route can still work only with extra geometric information
not present in strict containment alone: for example, a bounded-fibre rule
that composes compatible far arcs through many layers, or a theorem for
absolute-constant cages that is quantitatively stronger than (3).  The
correct state variable would have to record the two current support
directions (the tangent cone of the partial convex hull); multiplying raw
per-layer choices loses exactly that compatibility data.

## 6. Verification

From this directory:

```
python3 -m py_compile nested_cage_search.py
python3 nested_cage_search.py --depth 2 3 4 5 6 8 10 --samples 8
```

All coordinates and orientation decisions are exact rational arithmetic.
The endpoint cap/cup DP counts all convex subsets without using the tangency
lower bound.
