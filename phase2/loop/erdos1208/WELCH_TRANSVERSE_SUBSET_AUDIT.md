# Welch–Costas stress test for the transverse local gate

## Plain-language summary

Ordinary distinct-difference configurations do **not** satisfy the proposed
linear transverse-overlap bound.  Welch Costas arrays have a fixed transverse
overlap containing about `0.44 N^2` solutions.  Their repeated Euclidean
lengths are therefore doing real work.  The direct counterexample test is to
retain as many of those solutions as possible while selecting a subset whose
Euclidean distances are all different.  Targeted exact searches through
ambient order `508` retained only about `1.7 k` solutions on `k` selected
points.  This does not prove the local theorem, but it is the strongest
structured falsification test currently run against it.

## 1. The exact host configuration

For a prime `p` and a primitive root `g`, let

\[
 W_p=\{(j,g^j\bmod p):0\le j<p-1\}.
\]

The `N=p-1` points form a Welch Costas array: every nonzero directed
difference has a unique ordered representation.  They are vector-Sidon, but
not distance-Sidon because different displacement vectors can have the same
Euclidean norm.  This is standard Costas-array structure; the broader
distinct-difference framework and its multi-hop sums are treated by
Blackburn--Etzion--Martin--Paterson, *Distinct Difference Configurations:
Multihop Paths and Key Predistribution in Sensor Networks*, arXiv:0811.3896.

For fixed `d in W_p-W_p`, put

\[
 m_d(B)=\#\{e\in B-B\setminus\{0\}:
 d-Je\in B-B,\ d\cdot e\ne0\}.                  \tag{1.1}
\]

On the full Welch hosts, a short popular difference gives genuinely
quadratic values:

| `p` | `N` | `d` | `m_d(W_p)` | `m_d/N^2` |
|---:|---:|---:|---:|---:|
| 127 | 126 | `(-4,9)` | 6,887 | 0.434 |
| 251 | 250 | `(-3,-5)` | 27,474 | 0.440 |
| 509 | 508 | `(-1,2)` | 114,191 | 0.443 |

Thus vector uniqueness, torsion-free coordinates, and the exclusion
`d dot e != 0` still permit a quadratic local overlap.  Any proof of the
local gate must use uniqueness of **norms**, not merely differences.

## 2. Radially unique subset search

`search_welch_transverse_subsets.py` fixes the endpoints of a popular `d`,
constructs a distance-Sidon subset of the Welch points, and anneals exact
vertex swaps to maximize the number of retained local solutions.  Every
proposal is rejected if it repeats a squared Euclidean distance.  The score
is updated from the exact endpoint sets of the full-host solutions.

The retained certificates are:

| ambient `p` | ambient `N` | subset `k` | exact `max_d m_d` | `max/k` |
|---:|---:|---:|---:|---:|
| 127 | 126 | 25 | 43 | 1.720 |
| 251 | 250 | 40 | 68 | 1.700 |
| 509 | 508 | 55 | 94 | 1.709 |

`verify_welch_transverse_subsets.py` stores the exact selected indices,
checks every squared distance, recomputes the full-host counts, and scans all
differences of each selected subset to certify the displayed maximum.  The
stable ratio is evidence for a linear bound; three finite cases are not an
asymptotic theorem.

## 3. Equivalent hereditary formulation

Let `d=p-q` be a fixed directed edge of a distance-Sidon set `A`.  A local
solution is an ordered quadruple

\[
 (u,v,x,y)\in A^4,
 \qquad u-v+J(x-y)=d,\quad d\cdot(x-y)\ne0.       \tag{3.1}
\]

The solutions form a four-partite linear relation hypergraph: any two
coordinate positions determine the whole quadruple.  For example, `(u,x)`
determines `(v,y)` because the map `A x A -> A+JA` is injective; the other
mixed pairs use the equally direct sum `A-JA`.  The within-edge pairs follow
from oriented-difference uniqueness.

For a subfamily `F`, let `V_d(F)` be the union of all its endpoint labels
together with the two fixed endpoints `p,q`.  The local conjecture is
equivalent, up to constants and subpolynomial factors, to the hereditary
endpoint-density statement

\[
 |F|\le |V_d(F)|^{1+o(1)}.                       \tag{3.2}
\]

Indeed, (3.2) applied to the full family gives the local gate.  Conversely,
`V_d(F)` is itself a distance-Sidon subset containing `p,q`, so the local gate
applied to it bounds every subfamily.  This is an **equivalent reformulation**,
not a proof-level reduction.

The formulation explains both sides of the computation.  A prescribed
finite biclique can be realized by giving most relation edges fresh target
endpoints, so bounded forbidden patterns cannot establish (3.2).  The full
Welch array reuses endpoints quadratically but repeats norms.  The selected
subsets show that enforcing radial uniqueness has so far restored hereditary
linear-scale reuse.

## 4. What would settle this lane

A proof of (3.2), even with a `polylog(k)` factor, proves
`max_d m_tr(d)<=k^(1+o(1))` and hence the global transverse collision bound.
A counterexample is equally decisive: a sequence of radially unique subsets
with `m_d>=k^(1+epsilon)` for a fixed positive `epsilon` kills the local lane.

The next proof-level question is therefore not whether the relation
hypergraph is linear--abstract linear hypergraphs can have quadratic size--but
whether superlinear *endpoint reuse* forces two difference vectors of `A` to
have the same norm.  The Welch host is the calibrated family on which such an
argument must visibly turn quadratic reuse into a norm collision.

## 5. Rigidity and why the obvious deformation does not give a counterexample

There is a tempting way to try to defeat the local conjecture.  Regard the
point coordinates as complex variables `z_j`.  Every retained relation is the
Gaussian-linear equation

\[
 z_u-z_v+i(z_x-z_y)=z_p-z_q.                    \tag{5.1}
\]

If the quadratic Welch family had a third global kernel direction in addition
to constants and the original coordinate vector, a generic deformation in
that direction could preserve all local relations while separating its
repeated Euclidean lengths.

This does not happen for the tested full hosts.  The exact checker
`verify_welch_relation_rigidity.py` reduces their sparse Gaussian relation
matrices modulo `65537`, with `i` represented by `256`, and certifies

| `N` | relations | rank |
|---:|---:|---:|
| 30 | 350 | 28 |
| 60 | 1,480 | 58 |
| 126 | 6,887 | 124 |

The constant and Welch coordinate vectors already give a two-dimensional
kernel.  A nonzero `(N-2)`-minor modulo this Gaussian prime therefore proves
rank exactly `N-2` over `Q(i)`.  Every complex realization preserving the full
relation family is consequently only a complex similarity and translation of
the Welch realization; its repeated lengths are forced.

Sampled codimension-one subfamilies initially looked much more flexible, but
the rich ones merely freed one to three point labels while leaving a rigid
Welch core.  In the `N=60` audit, sampled deformations supported on one, two,
or three labels preserved up to `1431`, `1351`, and `1273` of the `1480`
relations, whereas every sampled deformation affecting at least five labels
preserved at most `67`.  These latter figures are a deterministic search
observation, not an exhaustive bound.

There is also no free tensor amplification.  If
`P=X+R Y={x+Ry:x in X,y in Y}` contains at least two faithfully represented
fibres and `|X|>=2`, the segment between two fixed points of `X` occurs with
the same displacement in every `Y`-fibre.  Thus the full Cartesian product is
not distance-Sidon.  A code with both coordinate projections injective avoids
that repetition but has size at most the smaller alphabet, so it does not
multiply the number of vertices.  Any counterexample amplification must
therefore couple the fibres while preserving the quarter-turn equations; the
naive scale-separated product cannot do it.
