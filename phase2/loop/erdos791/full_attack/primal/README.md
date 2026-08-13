# Erdős #791 full-attack primal lane

Read `PRIMAL_RESULT.md` for the theorem, proof, limitations, and reproduction
commands.

The principal artifacts are:

- `interleaved_cycle.py`: exact finite-state phase-reuse family;
- `phased_predicate.py`: abstract certificate predicate;
- `primal_verify.py`: independent literal `A_t+A_t` verifier;
- `role_obstruction.py`: quantitative triangle-free-role audit;
- `test_primal.py`: parameter and abstract-to-literal regressions.

No artifact claims an improvement over `85/294`.
