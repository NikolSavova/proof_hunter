# fast.py --sample — B7 D7 E7 (num=20000, d in [4,12], seed=7, procs=4)

Engine: root-action (fast.py), selftested against weyl.py + scaled.py + scaled_general.py.
A ratio < 1 would be a COUNTEREXAMPLE to Brenti Conj 2.11.

## B7  (sample, 399s)
- verdict: **all pass**
- min ratio: 1.000000 = 1 (margin 0) k=2
- witness: [2432, 24326767]
- ranks: [1, 2, 2, 2, 1]

## D7  (sample, 317s)
- verdict: **all pass**
- min ratio: 1.157143 = 81/70 (margin 396) k=4
- witness: [e, 436547543657]
- ranks: [1, 5, 14, 30, 54, 84, 111, 122, 109, 74, 34, 9, 1]

## E7  (sample, 669s)
- verdict: **all pass**
- min ratio: 1.142400 = 14641/12816 (margin 1825) k=5
- witness: [1342376, 4234542314376542314]
- ranks: [1, 8, 27, 56, 89, 121, 144, 149, 129, 87, 41, 11, 1]
