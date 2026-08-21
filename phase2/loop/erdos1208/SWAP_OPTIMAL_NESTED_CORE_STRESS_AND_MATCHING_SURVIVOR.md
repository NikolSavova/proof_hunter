# Optimal swap cores: exact stress and the matching-heavy survivor

## 1. Outcome

This note computes the **true minimum quadratic orientation energy** of the
adaptive swap multigraph from
`SWAP_OPTIMAL_ORIENTATION_NESTED_CORE_GATE.md`.  It gives no proof of the
remaining geometric estimate, but it materially narrows the direct route.

The exact profiles separate genuine complete-difference examples from the
radial impostors more strongly than the earlier peeling orientation:

* on the genuine Costas stresses through size 37, the optimal maximum load
  is between `3` and `13`, within a factor `1.27` of `K=|D+D|/|D|`;
* on radial transversals of sides `4,5,6,8`, it is `10,18,35,85`, and its
  ratio to `K` grows from `2.40` to `16.37`;
* the normalized quadratic energy `E_2/(K|E|)` remains below `0.39` in every
  genuine row but grows from `1.50` to `9.66` on the radial rows.

The optimizer also identifies the actual dyadic core carrying the nested
mass.  The dangerous genuine branch is not a common-endpoint star.  In the
Costas-37 maximizing core, `482201/997675=48.33%` of the edge copies have
four fixed difference vectors whose **eight physical endpoints are all
distinct**.  Another `34.47%` has only a cross-role endpoint contact.  Thus
a shared-head/shared-tail theorem cannot close the direct gate.  The next
geometric lemma must retain the full matching-like endpoint realization and
the affine relation between its four directed edges.

## 2. Exact path-reversal optimizer

Let an orientation of a loopless multigraph have outdegrees `x_v`.  A
directed path from `u` to `v` may be reversed; only its endpoints change,
and the quadratic energy changes by

\[
 (x_u-1)^2+(x_v+1)^2-x_u^2-x_v^2
 =2(x_v-x_u+1).                                      \tag{2.1}
\]

Hence a path from a load at least two larger to a load at least two smaller
strictly improves the energy.  Conversely, suppose no such path exists.
Compare the orientation with any other orientation and keep only the edge
copies on which they differ.  In the current orientation those copies
decompose into directed cycles and directed paths from vertices losing
outdegree to vertices gaining outdegree.  Every such path has endpoints
`u,v` with `x_u<=x_v+1`.  Moving the first unit has nonnegative energy cost
by (2.1); every later removal or addition has a still larger marginal cost.
Thus the comparison cannot lower the energy.

This proves the exact certificate:

> An orientation minimizes `sum_v x_v^2` if and only if no directed path
> joins vertices whose loads differ by at least two in the improving
> direction.

The analyzer starts with a canonical orientation and reverses maximal
energy-decreasing batches along such paths.  The affine invariant
`z=ell-(I+J)b` makes every stored component small (at most 47 vertices in
the rows below), so the exact optimization remains inexpensive even when
the global graph has more than a million edge copies.  The generic
verifier also compares this optimizer with exhaustive enumeration on fixed
and random multigraphs.

## 3. Exact profiles

Write `N=|D|`, `S=|D+D|`, `K=S/N`, `m_E=|E(G_sw)|`, and let `E_2` be the
minimum squared-outdegree energy.  For the optimal loads set

\[
 U_t=\{v:x_v\ge t\},\qquad e_t=|E(G_{sw}[U_t])|.       \tag{3.1}
\]

The columns `t_*` and `e_*` give the dyadic level maximizing `t e_t`.

| family | `m_E` | `max x` | `t_*` | `e_*` | `E_2/(K m_E)` | `sum_t e_t/m_E` |
|---|---:|---:|---:|---:|---:|---:|
| closure 40 | 185258 | 6 | 1 | 120993 | 0.0139 | 0.9616 |
| Costas 11 | 1132 | 3 | 1 | 573 | 0.1519 | 0.5742 |
| Costas 17 | 10007 | 4 | 1 | 6106 | 0.1367 | 0.7915 |
| Costas 23 | 249337 | 8 | 2 | 178750 | 0.2924 | 2.5748 |
| Costas 29 | 761273 | 12 | 4 | 325704 | 0.3828 | 3.3836 |
| Costas 31 | 382551 | 13 | 2 | 198067 | 0.2270 | 2.1327 |
| Costas 37 | 1469656 | 13 | 2 | 997675 | 0.2728 | 2.7269 |
| radial 4 | 4165 | 10 | 4 | 3703 | 1.5044 | 6.0684 |
| radial 5 | 12358 | 18 | 8 | 10114 | 2.2930 | 10.4610 |
| radial 6 | 46645 | 35 | 16 | 36323 | 4.3508 | 20.5860 |
| radial 8 | 277974 | 85 | 32 | 233442 | 9.6600 | 49.9913 |

These values use edge-copy multiplicity throughout.  They satisfy exactly

\[
 E_2=\sum_{t\ge1}e_t+B,\qquad 0\le B\le m_E,           \tag{3.2}
\]

as proved in the preceding nested-core note.

## 4. Physical endpoint classification

For a core edge write its fixed cells as

\[
 (b,\ell),\qquad (b',\ell'),\qquad
 \ell'-\ell=(I+J)(b'-b).                                \tag{4.1}
\]

Every nonzero member of `D=A-A` has a unique ordered physical endpoint
pair.  The analyzer classifies an edge copy by endpoint contacts among the
four directed vectors:

* `B` or `L`: the corresponding pair shares a head or shares a tail;
* lowercase `b` or `l`: it has only a cross-oriented contact;
* `X`: some endpoint of `{b,b'}` meets an endpoint of `{ell,ell'}`;
* `---`: none of the eight physical endpoints coincide.

The largest two clean/mixed classes in the genuine cores are:

| family | core copies | `---` | `--X` | combined fraction |
|---|---:|---:|---:|---:|
| Costas 29 | 325704 | 125727 | 124786 | 76.91% |
| Costas 31 | 198067 | 80988 | 74756 | 78.63% |
| Costas 37 | 997675 | 482201 | 343916 | 82.80% |

This is a decisive routing fact.  The high-level core becomes increasingly
matching-heavy, not star-heavy.  The shared-endpoint channels developed in
earlier scalar and six-anchor notes can pay a remainder, but they do not see
the main survivor.

## 5. The direct next theorem

For a distance-Sidon set `A`, consider a dyadic optimal core `U_t` and keep
only the `---` edge copies.  Each such copy has eight distinct physical
endpoints supporting four directed differences satisfying (4.1), together
with the three moving memberships and two adaptive-popular shifts in the
swap normal form.

The immediate direct target is the matching-core estimate

\[
 \boxed{
   \sum_{t\ {\rm dyadic}} t\,
   |E_{---}(G_{sw}[U_t])|
   \le K N^{o(1)}|E(G_{sw})|.}                    \tag{5.1}
 \]

It must be paired with the endpoint-contact remainder, but (5.1) is the
load-bearing new branch.  A proof should use the fact that the four edge
labels in (4.1) come from one complete graph on `A`, not merely a radially
unique set of vectors.  The precise intended collision is:

1. two records in the same high-load cell give two endpoint matchings;
2. the affine equation (4.1) transports their endpoint differences through
   `I+J`;
3. unless the records lie in a low-index/one-dimensional family already
   paid by the ambient term, two different physical edges acquire the same
   squared length.

The third step is the missing lemma.  The stress calculation shows that it
should be sought in the eight-distinct matching branch, not by another
common-endpoint or radial-energy relaxation.

## 6. Verification

Run

```bash
python3 phase2/loop/erdos1208/verify_swap_optimal_orientation_nested_core.py
python3 phase2/loop/erdos1208/analyze_swap_optimal_nested_cores.py --extended
python3 phase2/loop/erdos1208/analyze_swap_optimal_nested_cores.py --larger
```

The first command exhaustively checks the optimizer on fixed and seeded
random multigraphs.  The analyzer then reconstructs the genuine swap
graphs, optimizes every invariant component, checks the exact nested-core
identity, and reports component, shift, fibre, load, and physical-endpoint
profiles.
