# Relation-closure adversary for the transverse local gate

## Plain-language summary

A purpose-built closure search found a substantially stronger local-overlap
family than coordinate annealing or Welch-subset selection.  It starts from
the 16-point exact witness and repeatedly adds a point that completes as many
quarter-turn relations as possible, rejecting every repeated Euclidean
distance.  The certified chain now reaches 120 points with local overlap
`948` and exact relation-hypergraph degeneracy `13`.

The numerical law is the important correction:

\[
 m_d=0.7212\ldots\,k^{3/2}\quad\hbox{at }k=120,
\]

with essentially the same normalized value from `k=47` through `k=120`.
This is not an asymptotic construction, so it does not rigorously refute
`m_d<=k^(1+o(1))`; it is nevertheless strong evidence that the maximum-fibre
lemma is false.  It also kills every fixed-degeneracy version.  Crucially, the
same 120-point set still has transverse energy only `0.810 k^3` and rotated
support `0.586 k^3`.  The global cubic theorem survives while its local-max
sufficient condition is now the wrong primary target.

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

`search_transverse_closure.py` reproduces the deterministic extension.
`verify_transverse_closure_witness.py` stores the resulting chain and checks:

| `k` | `m_d` | `m_d/k` | core relations | two graphic ranks |
|---:|---:|---:|---:|---:|
| 17 | 36 | 2.118 | 29 | `13+13` |
| 29 | 113 | 3.897 | 96 | `26+26` |
| 44 | 216 | 4.909 | 196 | `41+41` |
| 47 | 237 | 5.043 | 216 | `44+44` |
| 60 | 339 | 5.650 | 317 | `57+57` |
| 63 | 364 | 5.778 | 342 | `60+60` |
| 70 | 422 | 6.029 | 400 | `67+67` |
| 76 | 478 | 6.289 | 456 | `73+73` |
| 80 | 514 | 6.425 | 492 | `77+77` |
| 81 | 525 | 6.481 | 503 | `78+78` |
| 90 | 614 | 6.822 | 592 | `87+87` |
| 100 | 719 | 7.190 | 696 | `97+97` |
| 105 | 773 | 7.362 | 750 | `102+102` |
| 110 | 830 | 7.545 | 807 | `107+107` |
| 120 | 948 | 7.900 | 925 | `117+117` |

The maximum is attained at both signs of the stored `d`; the table uses
`d=(0,-1)`.  All `binom(k,2)` squared distances are checked exactly, and all
directed differences are therefore unique.  The normalized values
`m_d/k^(3/2)` stay close to `0.72` through `k=120`.  This stability is why the chain is now a serious asymptotic
warning rather than merely a large constant.

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

## 3. Fixed degeneracy is false

The full 47-point relation hypergraph has degeneracy exactly `8`, but this was
a finite-range artifact.  The degeneracy becomes `9` at `k=63`, `10` at
`k=76`, `11` at `k=81`, `12` at `k=108`, and `13` at `k=120`.  Therefore no
universal constant-degeneracy theorem can prove the
local gate.

An upper bound of `k^(o(1))` on degeneracy is not formally excluded by 120
points.  The observed scale is instead compatible with `sqrt(k)`, and the
overlap is compatible with `Theta(k^(3/2))`.  Promoting the deterministic
chain to an infinite family with a fixed positive exponent would rigorously
kill the local lane.  Until that is ruled out, the local gate should not be
used as the lead proof target.

## 4. The global cubic target survives

`verify_transverse_closure_global.py` checks the full distribution at `k=120`:

* `|D|=14281` and `sum_d m_tr(d)=2,798,384`, hence
  `E_trans=1,399,192=0.8097... k^3`;
* `max_d m_tr(d)=948=0.7212... k^(3/2)`;
* 24 oriented differences have overlap at least 512;
* `|A+JA-JA|=1,011,786=0.5855... k^3`.

Thus a square-root-heavy exceptional fibre is fully compatible with cubic
total energy and cubic support.  The correct replacement is a tail or moment
bound for the whole overlap distribution, not an `L^infinity` bound.  A
minimal viable statement is still

\[
 \sum_{d\in D}m_{\rm tr}(d)\le k^{3+o(1)}.
\]

The certified tail is broad rather than concentrated (`4228` differences have
overlap at least 256), so even a proof by deleting only a constant number of
exceptional fibres is not calibrated to this example.

## 5. Deltoids do not control the hard relations

Elekes's deltoid theorem counts four points of `A` whose side lengths come in
two adjacent equal pairs.  A distance-Sidon set contains no nondegenerate
deltoid at all.  A local relation `u-v+J(x-y)=d`, however, creates a translated
diagonal in `A+JA`; it creates no deltoid in `A`.  Pairs of relations produce a
deltoid only in the endpoint-sharing role patterns that radial uniqueness
already forbids individually.  The disjoint-endpoint relations—the hard
mass—do not map to deltoids, and the prior-art `O(k^(8/3) log k)` theorem would
be too weak even if they did.  This closes the deltoid-overlap shortcut.
