# Incremental placement search

`anneal.cpp` maintains the exact generalized-Mrose tile predicate while
updating only pair sums affected by each coordinate mutation. It supports
multi-coordinate proposals and fixed type counts. A negative run is heuristic,
never a nonexistence claim.

```bash
c++ -O3 -std=c++20 anneal.cpp -o anneal
./anneal --target 511 --bound 510 --counts 8,17,17 \
  --steps 100000000 --restarts 100 --seed 791 --output result.json
```

See `RUNS.md` for the recorded campaign and `plateau_graph.py` for the targeted
20/115 near-miss component exploration.
