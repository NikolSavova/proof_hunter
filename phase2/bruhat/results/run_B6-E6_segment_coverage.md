# B6 + E6 segment-coverage record (runs were killed + resumed; union covers ALL bottom elements)

Verification of B6 and E6 ran in two segments each. Segment 1 (u=0..8999 for B6, u=0..5999 for E6)
was killed before writing a result file; its coverage + zero-violation evidence is the checkpoint
stream below (printed every 1000 bottom elements). Segment 2 (--from-u 9000 / --from-u 6000)
completed normally: run_B6_from9000_70875.md, run_E6_from6000_70876.md.

TOTALS: B6 = 193,249,546 (seg1, u<9000) + 157,426,463 (seg2) = 350,676,009 intervals, 0 violations.
        E6 = 181,265,790 (seg1, u<6000) + 284,984,923 (seg2) = 466,250,713 intervals, 0 violations.
        E6 min ratio overall = 1.028446 (seg1; witness not recorded by the checkpoint format —
        re-scan u<6000 if the witness interval is wanted for the writeup).

## B6 segment-1 checkpoint stream (killed run bkw0tbbrm, 2026-07-04)
```
B6: |W|=46080, maxlen=36, built+validated in 132.3s; checking all intervals...
  [checkpoint] u=1000/46080 intervals=34862336 violations=0 min_ratio=1.000000 elapsed=549s
  [checkpoint] u=2000/46080 intervals=63216868 violations=0 min_ratio=1.000000 elapsed=996s
  [checkpoint] u=3000/46080 intervals=87940322 violations=0 min_ratio=1.000000 elapsed=1395s
  [checkpoint] u=4000/46080 intervals=110581192 violations=0 min_ratio=1.000000 elapsed=1785s
  [checkpoint] u=5000/46080 intervals=129502376 violations=0 min_ratio=1.000000 elapsed=2090s
  [checkpoint] u=6000/46080 intervals=147704062 violations=0 min_ratio=1.000000 elapsed=2379s
  [checkpoint] u=7000/46080 intervals=164354958 violations=0 min_ratio=1.000000 elapsed=2653s
  [checkpoint] u=8000/46080 intervals=179350336 violations=0 min_ratio=1.000000 elapsed=2893s
  [checkpoint] u=9000/46080 intervals=193249546 violations=0 min_ratio=1.000000 elapsed=3116s
```

## E6 segment-1 checkpoint stream (killed run b4amu0da3, 2026-07-04)
```
E6: |W|=51840, maxlen=36, built+validated in 148.6s; checking all intervals...
  [checkpoint] u=1000/51840 intervals=41557514 violations=0 min_ratio=1.028446 elapsed=695s
  [checkpoint] u=2000/51840 intervals=76186672 violations=0 min_ratio=1.028446 elapsed=1283s
  [checkpoint] u=3000/51840 intervals=106615682 violations=0 min_ratio=1.028446 elapsed=1832s
  [checkpoint] u=4000/51840 intervals=133235218 violations=0 min_ratio=1.028446 elapsed=2287s
  [checkpoint] u=5000/51840 intervals=157634914 violations=0 min_ratio=1.028446 elapsed=2713s
  [checkpoint] u=6000/51840 intervals=181265790 violations=0 min_ratio=1.028446 elapsed=3117s
```
