# Incremental and plateau-search ledger

No record certificate was found. These runs are heuristic or bounded graph
explorations, not nonexistence proofs.

The C++ incremental engine maintains the exact three-tile predicate while
changing only affected pair-sum counters. Recorded seeded runs:

| target | counts | proposals | accepted | best |
|---|---:|---:|---:|---:|
| `m=511` | `(8,17,17)` | 100,000,000 | 4,003,497 | 510/511, prefix 510 |
| `m=511`, guided hole repair | `(8,17,17)` | 50,000,000 | 1,912,019 | 510/511, prefix 510 |
| `m=535` | `(9,17,17)` | 50,000,000 | 2,010,430 | 518/535, prefix 510 |
| `m=116`, guided hole repair | `(6,7,7)` | 100,000,000 | 6,935,915 | 115/116, prefix 115 |

Random-start sweeps used five million proposals at each `ell=18,...,30`; the
compact `ell*_random_v2.json` files record every best state. None reached its
record-breaking threshold.

For the 20/115 seed, exactly one nontrivial one-coordinate replacement retains
115/116 coverage: shifting the high K block start from 68 to 72 fills square
115 and transports the unique hole to 68. `plateau_graph.py` exhausts the
connected component under single-coordinate moves while allowing up to a
chosen number of temporary holes. With `--max-holes 6`, the component has
4,002 states and contains no 116/116 placement. This is a bounded landscape
statement, not a claim about paths through seven or more holes.
