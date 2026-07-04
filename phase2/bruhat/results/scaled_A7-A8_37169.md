# Scaled lower-interval near-miss scan — A7 A8 (cogap<=4, deepen)

Method: rank_seq([e,v]) = Poincare - complement-BFS; exact ints.
A ratio < 1 would be a COUNTEREXAMPLE to Brenti Conj 2.11.

## A7  (slab cogap<=4, 49s)
- verdict: **all pass**
- min ratio: 1.054250 = 919681/872356 (margin 757200) at k=14
- witness: v = [7, 6, 5, 4, 3, 2, 1, 0] (one-line), reduced word 1234567123456123451234123121, ell(v)=28
- ranks: [1, 7, 27, 76, 174, 343, 602, 961, 1415, 1940, 2493, 3017, 3450, 3736, 3836, 3736, 3450, 3017, 2493, 1940, 1415, 961, 602, 343, 174, 76, 27, 7, 1]

## A8  (slab cogap<=4, 687s)
- verdict: **all pass**
- min ratio: 1.038942 = 854275984/822255625 (margin 32020359) at k=18
- witness: v = [8, 7, 6, 5, 4, 3, 2, 1, 0] (one-line), reduced word 123456781234567123456123451234123121, ell(v)=36
- ranks: [1, 8, 35, 111, 285, 628, 1230, 2191, 3606, 5545, 8031, 11021, 14395, 17957, 21450, 24584, 27073, 28675, 29228, 28675, 27073, 24584, 21450, 17957, 14395, 11021, 8031, 5545, 3606, 2191, 1230, 628, 285, 111, 35, 8, 1]
