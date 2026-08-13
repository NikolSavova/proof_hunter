# Multitype amplifier bridge lane

Read `AMPLIFIER_RESULT.md` for the exact full-closure criterion, the
unique-sum/Turán role-defect obstruction, the carry-triangle theorem, and all
limitations.

Artifacts:

- `triangle_lemma.py`: exact elementary `H-S-T0` carry-triangle inclusion;
- `triangle_predicate.py`: enlarged macro predicate;
- `triangle_overlap_audit.py`: exact `3/2` incidence/footprint calculation;
- `triangle_cycle_search.py`: exhaustive small cyclic role-cost diagnostic;
- `test_triangle.py`: randomized macro-to-literal regression;
- `typed_verify.py`: independent literal verifier for ordinary typed
  and triangle-enhanced certificates;
- `cross_cover_amplifier.py`: universal (factor-four-loss) `V/H` lift;
- `role_defect_obstruction.py`: exact unique-sum graph audit;
- `kohonen_role_expansion.py`: scalable `k+1` role-cost family at the known
  `85/294` density;
- `triangle_role_batch.py`: exact triangle-enabled role optimization for all
  interval-range extremal bases through `k=8`.
- `ARBITRARY_BASIS_COUNTEREXAMPLE.json`: exact witness that unique diagonal
  count need not equal the role defect.

No artifact claims a new lower-bound record.
