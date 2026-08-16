# Erdős 838: campaign state after the 2026-08-14/15 attack

This is a short navigation document, not a replacement for any prior record.
The complete chronological attack remains in `FULL_ATTACK_20260814.md`; every
agent report and verifier is preserved.  This note separates theorem progress,
barrier progress, and verification status so that they are not conflated.

## 1. Rigorous theorem state

For

\[
 f(n)=\min_{|P|=n}|\{A\subseteq P:A\text{ is in convex position}\}|,
\]

the unconditional window remains

\[
 \frac14\le \liminf_{n\to\infty}\frac{\log_2 f(n)}{(\log_2 n)^2}
 \le \limsup_{n\to\infty}\frac{\log_2 f(n)}{(\log_2 n)^2}
 \le \frac12.
\]

The 2026-08-14/15 campaign did **not** improve the unconditional lower
coefficient beyond `1/4`.  Every `3/8` statement in the master attack is
conditional on an additional extraction or allocation theorem.  Every larger
coefficient attached to a recurrence family is a closure theorem for that
family, not an unrestricted lower bound.

The upper coefficient `1/2` and the matching lower theorem for recursively
mirror-decomposable/strong-tree configurations predate this campaign and have
the strongest existing independent audit.

## 2. What the campaign genuinely added

The campaign materially narrowed both construction and proof routes.  The
following packages are the most plausible bankable results, but the recent
ones still require independent cross-model reconstruction before publication.

### A. Construction-side closure

- A universal hinged endpoint Kraft inequality gives the exact diagonal
  reward `h >= ceil(log_2 m)` for an arbitrary ordered point set.  It closes
  bounded-state and variable-arity finite-menu homogeneous grammars at
  coefficient `1/2`.
- Nonstationary homogeneous compositions with changing chart menus still obey
  the half lower coefficient, subject to the explicitly stated same-chart
  splice hypothesis.
- Recursive separated `E(r,s)`, reflection, and perfect-reset templates expand
  to a strong-decomposition tree and therefore cannot produce a genuine
  sub-half construction.  The exact scalar Bellman ramp can mimic half only
  if its low-face children are genuinely non-strong-decomposable.
- The stronger weighted-hinge inequality `(WH)` was disproved by an exact
  stretchable five-point example.  A square-mesh Bellman inequality survives
  extensive finite tests but remains conjectural.

Primary sources:

- `agent_nonstrong_ramp_search/HINGED_DIAGONAL_FLOOR_LOG.md`
- `agent_nonstrong_ramp_search/NONSTATIONARY_HOMOGENEOUS_HALF_CLOSURE.md`
- `agent_nonstrong_ramp_search/WEIGHTED_HINGE_FALSE_SQUARE_SURVIVES.md`
- `agent_many_class_partner_reset/RECURSIVE_ES_RAMP_HALF_CLOSURE.md`

### B. Minimizer and root reductions

- Exact deletion and hull-root identities reduce the desired half lower bound
  to a near-`log n` mean-rank/curvature statement for minimizers.
- The weighted hull-root increment now has the unconditional exact floor
  `K_(n,1)>=ceil(m_n(f(n))/n)+n-1`. At a putative coefficient `c` this is
  `(c+o(1))f(n)log n/n`; the cumulative half gate needs coefficient one, so
  the theorem exposes rather than closes the missing profile correlation.
- The endpoint-envelope formulation identifies the required one-seam Pareto
  curvature and records exact small-`n` saturation, including projective hull
  roots missed by affine contiguous-cut searches.
- Sparse curvature can be transported to a small exceptional layer, but its
  native-cap portion has a full common-output collision.  The surviving branch
  must be carried by child excess or by genuinely new geometric outputs.

Primary sources:

- `agent_minimizer_endpoint_curvature/MINIMIZER_ENDPOINT_CURVATURE_AND_HIGH_WALL_GATE.md`
- `agent_hull_root_envelope_dynamic/HULL_ROOT_ENVELOPE_AND_CHART_RESET_GATE.md`
- `agent_sparse_curvature_transport/SPARSE_CURVATURE_TRANSPORT_AND_NATIVE_COLLISION.md`
- `HULL_ROOT_INCREMENT_MOMENT_FLOOR_20260816.md`

### C. Decoder and Hall assembly

- The local weighted Hall condition and global superposition/recovery fibre
  are cleanly separated.  Compatible mixed-face codes globalize with an exact
  rank-incidence factor.
- Natural history-preserving two-tangent decoders can have polynomial load,
  even for constant-rank stretchable examples.  Pooling records before coding
  is therefore essential.
- Pooled rank-four banks give constant load in the matching-star stress;
  rank-five gives fibre one.  A global Erdős--Szekeres replacement code handles
  every literal rank-three history and, more generally, ranks
  `r=o(sqrt(log n))` with subpolynomial overhead.
- At the canonical fixed-size scale `n=4^k`, pooling into the ordinary
  rank-`k` bank and using the Holmsen--Nassajian Mojarrad--Pach--Tardos
  bound `ES(k)<=2^(k+O(sqrt(k log k)))` gives load/fibre one for every
  literal

  \[
    r\le {1\over4}\log n-O(\sqrt{\log n\log\log n}).
  \]
- Identity is adequate at `r >= log n`.  The literal-history window

  \[
     {1\over4}\log n-O(\sqrt{\log n\log\log n})<r<\log n
  \]

  remains open, as does nonliteral path multiplicity not determined by the
  support.

Primary sources:

- `agent_coxeter_global_half/ABSTRACT_MIXED_HALL_ASSEMBLY.md`
- `agent_coxeter_global_half/JOINT_DETACHED_BANK_RANK_PROMOTION.md`
- `agent_coxeter_global_half/GLOBAL_RANK_THREE_ES4_REPLACEMENT_CODE.md`
- `FIXED_SIZE_LITERAL_QUARTER_LOG_POOLING_GATE_20260815.md`
- `FIXED_SIZE_LITERAL_EXPLICIT_BOUNDARY_20260816.md`

### D. Barrier and equivalence results

The attack produced many exact stretchable counterexamples to tempting local
lemmas: one-step half-weight flows, source-retaining Hall maps, automatic
ear-cell synchronization, direct cap--cup converters, support-only branching,
and local profile multiplication.  These are useful negative results.  They
must not be narrated as steps of a proof once the residual target is shown to
be coefficient-equivalent to the unrestricted problem.

## 3. What remains open

Three broad gates survive.  None is presently a theorem.

1. A quantitative fixed-rank supersaturation gain that improves the
   unrestricted coefficient above `1/4`.
2. A minimizer curvature/child-excess theorem that turns the exact root
   envelope into enough new ordinary faces.
3. A global, history-faithful decoder through the intermediate literal-rank
   window, or a profile charge for configurations in which such a decoder is
   absent.

The half-weight target, peak-mean target, unrestricted rectangle-or-shield
telescope, and general reset-chain decoder are full-strength or
coefficient-equivalent targets.  They are recorded but are not suitable as
the next reduction layer.

## 4. Verification status

The directory contains hundreds of exact verifier/certificate scripts and
many rational finite configurations. That is substantial author-side
verification, but it is not a substitute for independent proof
reconstruction. V1 and V3--V5 in `VERIFICATION_QUEUE_20260815.md` now have
such reconstructions; only V2 remains frozen pending the same treatment.

## 5. Progress accounting

- Obstruction/architecture map: approximately `75--80%` mature.
- Construction-side recursive threat map: highly constrained, but the general
  nonstrong square-mesh route remains open.
- Unconditional lower-bound progress beyond `1/4`: **none yet**.
- Full proof completion cannot responsibly be assigned the earlier `78%`
  number; the final bridge may contain most of the theorem's difficulty.

## 6. Navigation

- Full preserved chronology: `FULL_ATTACK_20260814.md`
- External process critique: `CRITICISM_20260815_claude.md`
- Difficulty/stop ledger: `DIFFICULTY_LEDGER_20260815.md`
- Independent audit queue: `VERIFICATION_QUEUE_20260815.md`
- Short bankable-results note: `BANKABLE_RESULTS_20260815.md`
- Single next quantitative target: `PROVED_GAIN_STRATEGY_20260815.md`
