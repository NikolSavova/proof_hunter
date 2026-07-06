# Bruhat/Brenti proving plan (drafted 2026-07-06, Sihao session — Sihao owns)

> The compute phase is done (see HANDOFF §3): ~320k+ intervals checked, zero
> violations, structure found. What remains is Engine-A mathematics + writeup.
> Items in priority order; 1 and 5 first, together.

1. **Prove F2 (anchor theorem):** min log-concavity ratio of the Mahonian
   numbers ([m]_q! coefficients) = 1 + 36/m^3 + o(m^-3), and the minimum is
   central. Route: adapt Canfield–Janson–Zeilberger Thm 4.6/eq. (4.11)
   (they prove the 1+sigma^-2 central ratio for the central Gaussian binomial;
   local CLT transfer) to the q-factorial + a tail argument. Cross-examine
   per house rule before trusting. Numeric ground truth for every lemma is
   already in `results/` (exact ratios A4–A10).
2. **F1 for a provable subclass:** for rationally smooth v, P_[e,v] factors as
   a product of q-integers (Carrell–Peterson) -> log-concave (Hoggar), and its
   central ratio may compare cleanly against the full group's product formula.
   Target: "F1 holds for all rationally smooth lower intervals."
3. **F3 for short intervals:** equality a_k^2 = a_{k-1}a_{k+1} forces small
   rank numbers; ride the existing classification of length<=4-5 Bruhat
   intervals (arXiv 2110.00862 line) for a complete short-interval equality
   classification.
4. **The 0.91x offset in F2's fit:** likely a second-order Edgeworth term;
   nailing it sharpens the constant (optional polish).
5. **Paper skeleton NOW:** statements, verification tables (A7/B6/E6 land via
   CI), vetted citation scaffold (see results/theory_probe*.md). Writing
   forces precise wording of F1/F3 — that is mathematical work.

**Verification-artifact rule applies to proofs too:** every combinatorial
lemma gets a numeric check against the engines; the key lemma gets a Lean
attempt at the end if feasible. Never ship a single-model proof.

**Parked compute (not blockers):** A10 deep slab via Rust port or CI chunks;
OpenEvolve margin-minimization over the perturbed-braid family.
