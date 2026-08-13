# Unique-representation graphs and multitype amplification

For a finite interval basis `A` of range `n`, define `G_uniq(A,n)` on vertex
set `A`: distinct `a,b` are adjacent when `a+b<=n` has no other unordered
representation by `A`.  A diagonal uniquely represented target is recorded as
a loop.

This graph is a necessary compatibility object for every lossless typed
amplifier.  If a target has unique representation `{a,b}`, the roles assigned
to `a,b` must be an elementary-tile interaction capable of supplying that
target; a unique diagonal forces two compatible roles on the same element.

For the two-role cross-cover amplifier, deleting all dual-role vertices must
leave `G_uniq` bipartite.  Hence

```text
cross-cover cost >= |vertices incident to unique targets|
                    + odd-cycle-transversal(G_uniq),
```

plus one extra role for every forced loop vertex already counted once.
Nonunique targets may strengthen this lower bound.

For the phased five-list language, the current-sum interaction graph on
`I,J,K,L0,L1` is `K5` with the `L0-L1` edge deleted.  It contains a `K4`.
Thus four-colorability of `G_uniq` is a necessary first test for a no-duplicate
assignment into the `I,J,K,L0` roles, although it is far from sufficient:
consecutive and phase clauses couple adjacent target indices.

The exact experiments in this directory probe whether efficient interval
bases force a bounded-color or small-deletion unique graph.  Such a theorem
would materially support a multitype amplifier; high-chromatic near-extremal
examples would obstruct it.

## A static four-colour conjecture is false

Exhaustive enumeration of all interval bases through range 21 found no
chromatic number above four.  Nevertheless an exact CP-SAT search found the
following range-38 interval basis:

```text
A={0,1,2,3,4,9,14,17,18,24,28}.
```

The five vertices `{0,1,9,14,24}` form a `K5` in `G_uniq`: their ten pair
sums

```text
1,9,10,14,15,23,24,25,33,38
```

are all uniquely represented.  The finite model checked every range through
40 and found the first `K5` at range 38.  This is a finite CP-SAT result, not
a proof-producing global minimality theorem; the displayed positive witness
is independently checked by `search_unique_k5.py`.

The same basis has minimum five-list phased role cost 15 for 11 coordinates.
Thus static colour compatibility can itself force duplication, independently
of the additional consecutive-target constraints.  This kills the proposed
universal four-colour route.  It does not obstruct an **existential** bounded-
defect theorem selecting specially structured extremal bases; that sharper
possibility is the remaining typed-amplifier route.
