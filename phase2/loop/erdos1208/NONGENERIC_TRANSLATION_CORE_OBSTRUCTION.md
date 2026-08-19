# No abelian eight-corner core has distance-Sidon geometry

## 1. Result

This note removes the nongeneric-specialization caveat from
`EDGE_DISJOINT_TRANSLATION_CORE_OBSTRUCTION.md`.

Let the relation records be a finite elementary abelian group

\[
 V=\mathbb F_2^m,
\]

and let the eight corner matchings be translations by eight distinct
nonzero shifts which span `V`.  The six endpoint-role labels initially are
the cosets of the corresponding four-shift face spaces.  We now allow an
arbitrary further identification of those formal labels, including
identifications between different endpoint roles.

**Theorem 1.1 (complete abelian-core obstruction).**  There is no such
connected translation system whose records are distinct transverse
relations in a planar distance-Sidon set and whose eight corner projections
all have degree at least two.

The proof is a finite computer-assisted exhaustion over exact Gaussian
rational arithmetic.  It has two stages:

1. the earlier Fourier classification reduces all 27,970 formal full cores
   to 27,389 systems with a nontrivial forced record kernel and 581 systems
   with a universal squared-distance collision; and
2. an exact conflict-directed partition closure eliminates all 581 residual
   systems in 793 states, with at most five states for any one system.

The verifier uses no floating-point arithmetic and no randomized step.

## 2. Why arbitrary endpoint identifications reduce to a finite closure

For one translation system, let `L` be its finite set of formal endpoint
labels.  A hypothesized realization determines a partition `P` of `L`:
two labels lie in the same block exactly when they denote the same point of
the ambient set.  Quotient the Gaussian equations

\[
 a_0-a_1-b_0+b_1-Jc_0+Jc_1=0                 \tag{2.1}
\]

by `P` and compute their nullspace over `Q(i)`.  Every quotient point is a
Gaussian-linear form in a basis of the nullspace.

The following propagation rules are necessary in every distance-Sidon
specialization.

1. **Forced point equality.**  If two quotient point forms are identical,
   merge their partition blocks.
2. **Forced equal norm.**  Suppose two distinct formal point-pairs have the
   same Hermitian squared-norm form.  In an actual distance-Sidon
   specialization, either the two unordered endpoint pairs are equal, in
   one of their two orientations, or both pairs collapse to zero.  Thus
   there are exactly three branches:

   \[
   (a=c,b=d),\qquad(a=d,b=c),\qquad(a=b,c=d).   \tag{2.2}
   \]

3. **Invalid relation.**  Reject a state if one of the three directed edges
   in a relation collapses, or if two records acquire the same six endpoint
   labels.
4. **Corner linearity.**  Reject a state if two distinct records share two
   corner keys.

The fourth rule is a geometric consequence, not an extra genericity
assumption.  If the two corners differ in one bit, the records share both
endpoints of one directed edge and one endpoint of each other edge.  The
two Gaussian relation equations then make a realized difference equal to a
quarter-turn of another realized difference; distance-Sidonicity forces
both to vanish and the records coincide.  If the corners differ in two or
three bits, two complete directed edges, or all six endpoints, are already
shared and the same conclusion is immediate.

These rules are exhaustive.  Follow the partition of any alleged actual
realization down the search tree.  At every universal norm collision that
partition satisfies one branch of (2.2).  Hence it reaches a survivor if a
realization exists.  Finding no survivor proves nonexistence; the search
does not assume that unforced point labels remain distinct.

The exact squared-norm signature of a linear form

\[
 \ell(t)=\sum_j z_jt_j
\]

is its Hermitian Gram vector

\[
 (\overline z_rz_s)_{r\le s}.                  \tag{2.3}
\]

Equality of these signatures over `Q(i)` is precisely equality of the two
squared-norm polynomials for all complex parameter choices.  Thus no finite
field or numerical coincidence enters the certificate.

## 3. The two exhaustive branches

The canonical active-character coalescing from the earlier Fourier audit
has common six-role kernel `K_*`.  In each of the 27,389 `empty-core`
systems one has `|K_*|>1`.  Translation records which differ by an element
of `K_*` therefore have all six endpoint forms equal in every solution.
They are the same oriented relation, contradicting record distinctness.
The exact kernel histogram is

| `|K_*|` | systems |
|---:|---:|
| 2 | 1,400 |
| 4 | 3,880 |
| 8 | 7,996 |
| 16 | 10,169 |
| 32 | 3,925 |
| 64 | 19 |

The remaining 581 systems enter the partition closure.  Its exact search
profile is

| item | count |
|---|---:|
| systems | 581 |
| partition states | 793 |
| forced-point propagation states | 107 |
| universal norm-conflict states | 35 |
| terminal record collapses | 42 |
| terminal corner-nonlinearity states | 609 |
| survivors | **0** |

The canonical 256-record cube takes five states.  All three repairs of its
first universal distance collision create corner nonlinearity; the only
remaining branch forces a point coalescence and then collapses.

Run

```bash
python3 phase2/loop/erdos1208/verify_nongeneric_translation_core_obstruction.py
```

for the complete subspace enumeration, record-kernel check, and exact
partition closure.  `search_nongeneric_translation_core.py` also permits a
single system to be inspected independently.

## 4. Consequence for arbitrary corner matchings

Combine Theorem 1.1 with the stability theorem in
`CORNER_MATCHING_COMMUTATOR_DICHOTOMY.md`.  Let `X` carry eight
fixed-point-free, edge-disjoint corner involutions, and let

\[
 B=\{x:\tau_i\tau_jx\ne\tau_j\tau_ix
       \text{ for some }i<j\}.
\]

The stability theorem removes at most `256|B|` records and decomposes the
rest into connected abelian translation orbits.  Theorem 1.1 rules out
every such orbit, including all nongeneric endpoint identifications.
Therefore

\[
 \boxed{|X|\le256|B|.}                          \tag{4.1}
\]

The previous alternative `commutator defects versus nongeneric stable
orbits` has collapsed to **commutator defects alone**.  This is a real
strengthening, but not the full size-biased theorem: (4.1) is useful only
after the defect population is charged to endpoint/support data.

There is also a clean internally rich corollary.  Suppose every fibre of
each of the eight corner partitions on `X` has size at least `t`.  Pair each
fibre, leaving at most one fixed record.  Across all colours the fixed set
`F` has size at most `8|X|/t`.  Apply the canonical-word argument to
`B union F`; outside its 256 word-preimages one obtains a forbidden
fixed-point-free abelian orbit.  Hence

\[
 |X|\le256|B|+{2048\over t}|X|.                \tag{4.2}
\]

In particular, for `t>=4096`, every choice of the eight near-perfect fibre
matchings has

\[
 |B|\ge |X|/512.                               \tag{4.3}
\]

This resolves the earlier odd-fibre bookkeeping for an internally rich
core.  Extracting such a core from the externally popular tail, or charging
the resulting commutator defects directly, remains open.
