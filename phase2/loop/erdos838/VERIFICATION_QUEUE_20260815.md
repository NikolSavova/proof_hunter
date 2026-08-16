# Erdős 838: independent verification queue

The recent campaign has extensive exact author-side verification but has not
received comparable independent cross-model proof reconstruction.  Freeze
publication claims resting on the following packages until each receives a
fresh proof attempt from another model with the source artifact attached.

**Local integrity rerun, 2026-08-15:** all nine verifier suites associated
with V1--V5 passed, including `16,142,517` exact nonstationary ledgers,
`8,232` weighted Hall networks, the recursive ES schedule census, the
minimizer/root finite scans, sparse-curvature certificates, pooled rank
promotion, and the global rank-three ES(4) code.  This confirms that the saved
artifacts run; it does not change their independent-audit status.

## Queue (maximum five packages)

### V1. Hinged Kraft and variable-arity grammar closure

**Independent status, 2026-08-15:** `MINOR_REPAIR`, repaired and `PASS`.
The independent reconstruction found that the finite-grammar proof needed to
state explicitly how two retained child states reach the cap- and
cup-maximizing cycles before the final product splice. Strong connectivity
makes both paths bounded, so the correction changes only the lower-order
term. The source was patched and both verifier suites rerun successfully.
See `V1_INDEPENDENT_AUDIT_20260815.md`.

Claims to reconstruct:

1. the merged cup/cap word is prefix-free;
2. `sum_i 2^{-(alpha_i+beta_i)} <= 1`;
3. the Perron/circulation step gives a same-edge cycle with sufficient reward;
4. the resulting coefficient is at least `1/2` for the stated grammar class.

Artifacts:

- `agent_nonstrong_ramp_search/HINGED_DIAGONAL_FLOOR_LOG.md`
- `agent_nonstrong_ramp_search/verify_hinged_diagonal_floor_log.py`
- `agent_nonstrong_ramp_search/NONSTATIONARY_HOMOGENEOUS_HALF_CLOSURE.md`

### V2. Recursive separated-template construction closure

Claims to reconstruct:

1. expansion of every permitted macro/child schedule produces one ordered
   strong-decomposition tree;
2. stationary tropical coefficients and finite correction terms are correct;
3. perfect-reset powers do not evade the strong-tree lower theorem.

Artifacts:

- `agent_many_class_partner_reset/RECURSIVE_ES_RAMP_HALF_CLOSURE.md`
- `agent_many_class_partner_reset/verify_recursive_es_ramp_half_barrier.py`

### V3. Minimizer hull-root recurrence and endpoint curvature reduction

**Independent status, 2026-08-16:** `PASS`. The hull-root recurrence and
converse extension were reconstructed geometrically, the normalization in
the cumulative half-growth criterion was checked, the endpoint moment/Pareto
reduction was rederived, and the projective-root correction at `n=9` was
included explicitly. Both exact suites passed. See
`V3_INDEPENDENT_AUDIT_20260816.md`.

Claims to reconstruct:

1. the projective hull-root extension/deletion recurrence for `f(n+1)`;
2. the definition and exact role of `K_{n,1}`;
3. the cumulative curvature condition equivalent/sufficient for half;
4. the corrected `n=8,9` finite values and projective-root saturation.

Artifacts:

- `agent_minimizer_endpoint_curvature/MINIMIZER_ENDPOINT_CURVATURE_AND_HIGH_WALL_GATE.md`
- `agent_minimizer_endpoint_curvature/verify_minimizer_endpoint_curvature.py`
- `agent_hull_root_envelope_dynamic/HULL_ROOT_ENVELOPE_AND_CHART_RESET_GATE.md`
- `agent_hull_root_envelope_dynamic/verify_hull_root_envelope.py`

### V4. Sparse curvature transport and native-cap collision

**Independent status, 2026-08-16:** `PASS`. The curvature conservation law,
causal layer construction, weighted native/child-excess inequality, and
universal remapping load bound were reconstructed directly. Both exact
transport/max-flow suites passed. See `V4_INDEPENDENT_AUDIT_20260816.md`.

Claims to reconstruct:

1. sparse layer selection retains the claimed amount of curvature;
2. the shelling/remapping load lower bounds are exact;
3. the native-cap collision really has full load;
4. the child-excess alternative is stated without assuming the desired bound.

Artifacts:

- `agent_sparse_curvature_transport/SPARSE_CURVATURE_TRANSPORT_AND_NATIVE_COLLISION.md`
- its verifier(s) in the same directory
- `agent_post_collision_remapping/POST_COLLISION_REMAPPING_MINIMAX.md`

### V5. Global mixed-Hall assembly and low-rank ES replacement

**Independent status, 2026-08-15:** `PASS`. The Hall cut condition,
recovery-fibre condition, and bank-incidence factor were reconstructed
separately. The rank-four/rank-five matching-star allocations, joint
coherent-root (E(k,k)) allocation, and literal-rank ES replacement were
also checked from their exact capacity inequalities. Four verifier suites
passed. See `V5_INDEPENDENT_AUDIT_20260815.md`.

Claims to reconstruct:

1. the weighted Hall condition and recovery-fibre condition are independent
   and correctly composed;
2. rank incidence gives the asserted global superposition load;
3. pooled rank-four/rank-five allocation has the claimed load/fibre;
4. the ES(4) code handles all literal rank-three histories and extends to
   `r=o(sqrt(log n))` with subpolynomial overhead.

Artifacts:

- `agent_coxeter_global_half/ABSTRACT_MIXED_HALL_ASSEMBLY.md`
- `agent_coxeter_global_half/JOINT_DETACHED_BANK_RANK_PROMOTION.md`
- `agent_coxeter_global_half/GLOBAL_RANK_THREE_ES4_REPLACEMENT_CODE.md`
- the three corresponding `verify_*.py` programs

## Verdict format

Each external audit must return one of `PASS`, `MINOR_REPAIR`, `MAJOR_GAP`, or
`FALSE`, with:

- a self-contained reconstruction;
- exact lemma dependencies;
- a check that no statement silently assumes the unrestricted lower bound;
- rerun output for every numerical certificate;
- a short scope statement saying exactly what the result does **not** prove.
