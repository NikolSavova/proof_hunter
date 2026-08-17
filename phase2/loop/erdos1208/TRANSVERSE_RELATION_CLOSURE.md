# Relation-closure adversary for the transverse local gate

## Plain-language summary

A purpose-built closure search found a substantially stronger local-overlap
family than coordinate annealing or Welch-subset selection.  It starts from
the 16-point exact witness and repeatedly adds a point that completes as many
quarter-turn relations as possible, rejecting every repeated Euclidean
distance.  The resulting 47-point set is still distance-Sidon and has local
overlap `237`, a ratio of `5.04` relations per point.  This kills the tempting
exact bounds `m_d<=2k` and the proposed two-forest/matroid proof, but it does
not kill the asymptotic target `m_d<=k^(1+o(1))`: the stored relation
hypergraph is only 8-degenerate.

## 1. Exact closure family

Fix `d=(0,-1)`.  Starting from the 16-point witness in
`verify_transverse_search_witnesses.py`, generate every integer point forced
by one equation

\[
 u-v+J(x-y)=d                                      \tag{1.1}
\]

after choosing three of the four endpoint roles from the current set.  Among
the candidates that preserve uniqueness of every squared distance, add one
maximizing the new exact local overlap.  The first point is `(12,49)`.

`verify_transverse_closure_witness.py` stores the resulting chain and checks:

| `k` | `m_d` | `m_d/k` | core relations | two graphic ranks |
|---:|---:|---:|---:|---:|
| 17 | 36 | 2.118 | 29 | `13+13` |
| 29 | 113 | 3.897 | 96 | `26+26` |
| 44 | 216 | 4.909 | 196 | `41+41` |
| 47 | 237 | 5.043 | 216 | `44+44` |

The maximum is attained at both signs of the stored `d`; the table uses
`d=(0,-1)`.  All `binom(k,2)` squared distances are checked exactly, and all
directed differences are therefore unique.

## 2. Exact proof mechanisms killed

The bound `m_d<=2k+O(1)` is false already at `k=17`, and the ratio continues
to rise through the stored chain.

A more structural proposal was to delete the `O(k)` relations touching the
fixed endpoints `p,q`, then partition every remaining relation either into a
forest of its `e=(x,y)` endpoint edges or a forest of its `f=(u,v)` endpoint
edges.  Matroid union requires every subfamily to satisfy

\[
 |F|\le r_E(F)+r_F(F).                              \tag{2.1}
\]

The 17-point core has `29>13+13`, so (2.1) fails without needing a matroid
solver.  At 47 points the defect is much larger: `216>44+44`.  Thus a proof
cannot charge every relation to only those two graphic forests.

## 3. What survives

The full 47-point relation hypergraph has degeneracy exactly `8`: repeatedly
delete a point of minimum current relation degree, and the largest minimum
encountered is eight.  Hence this adversary itself satisfies the hereditary
linear estimate `|F|<=8|V(F)|`.  Its growing global ratio comes from adding
new constant-degree relation completions, not from a dense core of minimum
degree tending as a power of `k`.

This supplies the next calibrated viability test.  A proof of the local gate
may seek a `k^(o(1))` degeneracy bound, or a partition into more geometric
forest-like charges, but it may not assume a small absolute overlap constant
or the two-forest inequality.  Conversely, a closure family whose degeneracy
grows like `k^epsilon` would be a genuine asymptotic counterexample and would
kill the lane.
