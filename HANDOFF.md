# HANDOFF — read me first (for a fresh Claude Code session)

> **Purpose:** this file is the single self-contained brief to resume this project in a NEW
> session after the folder was moved. Read this, then `META_GUIDE.md` (strategy + full working
> log) and `PROBLEM_ID_PIPELINE.md` (pipeline design). Written 2026-06-26 by the prior session.
>
> ⚠️ **Memory note:** Claude Code's file-memory is per-machine + per-project-path and is NOT in the
> repo, so it does NOT sync between Nikol and Sihao via GitHub. **`CLAUDE.md` + `HANDOFF.md` +
> `META_GUIDE.md` are the shared source of truth** — anything both collaborators must know goes in
> those committed files, not in file-memory.

---

## 0. ⚙️ POST-MOVE CHECKLIST — ✅ DONE (2026-06-26), kept for reference
> The folder is now a GitHub repo (`github.com/NikolSavova/proof_hunter`), shared by Nikol + Sihao.
> Session protocol now lives in `CLAUDE.md` (auto-loaded) + the `/handoff` command. The items below
> were the original post-move risks; both are resolved.
1. **Python venv** — turned out to survive the move intact (`./.venv` works; DB reads 900). If it ever
   breaks on a fresh clone, recreate it:
   ```bash
   cd <NEW>/problem-id
   rm -rf .venv && python3 -m venv .venv
   ./.venv/bin/python -m pip install requests beautifulsoup4 lxml pyyaml openai feedparser pymupdf
   ```
2. **OpenAI key now lives OUTSIDE the repo** at `~/.config/proof_hunter/openai_key.txt` (moved there
   2026-06-26 so it is never committed to GitHub; scrubbed from git history too). Both consumers point
   to it: `problem-id/common.py` (`KEY_PATH`, overridable via `$OPENAI_API_KEY` / `$OPENAI_KEY_FILE`)
   and `~/maths/openevolve/env.sh`. `.gitignore` blocks `*key*.txt`. **Sihao (fresh clone):** the key
   is NOT in the repo — create `~/.config/proof_hunter/openai_key.txt` (perms 600) with the key, or
   `export OPENAI_API_KEY=...`, before running the pipeline. Ask Nikol for the key over a secure channel.
3. Everything else in `problem-id/` (the SQLite DB, all code) uses paths relative to `__file__`, so
   it travels fine. Sanity check: `cd problem-id && ./.venv/bin/python -c "import common; print(common.db().execute('SELECT COUNT(*) FROM problems').fetchone())"` → should print `(900,)`.
4. `OPENEVOLVE.md` documents the OpenEvolve rig (Engine B) at `~/maths/openevolve` (separate dir,
   NOT moved). The plaintext OpenAI key is at `~/.config/proof_hunter/openai_key.txt` — **never print/commit it.**

---

## 1. WHO + GOAL
- **Nikol** — Oxford **maths undergrad** (logic/sets, algebraic & analytic number theory, Galois,
  graph theory, rings, topology, combinatorics, measure, probability). Proof + problem-selection +
  verification lead.
- **Sihao Huang** (sihao.c.huang@gmail.com) — **MIT physics grad** (ML, CS, quantum information).
  Infra + Engine-B + QIT/ML lead.
- **Goal:** produce a **novel, publishable mathematics result in ~1 week**, where the *enabler* is
  frontier AI (Claude Opus, GPT-5.5-Pro, OpenEvolve evolutionary search, SAT, Lean autoformalization)
  — NOT amateur grit. Win = an arXiv-ready note OR a verified logged contribution to an open effort.
- **Two engines:** (A) cross-domain lemma / quantitative-extension drafted by LLMs; (B) evolutionary/
  SAT search for explicit constructions/bounds/counterexamples. **Always ship a verification artifact
  (Lean proof / certificate / re-runnable evaluator).**
- **Cardinal rule:** prior-art kill-search is STEP ONE (the Oct-2025 "Erdősgate" debacle = a
  literature-find mislabeled as a new proof; "open in a database" ≠ unsolved).
- **The alpha thesis:** hunt *curated, low-LLM-saturation* problem lists (IQOQI quantum problems, COLT
  open-problem track, discrete-geometry books) that frontier labs are NOT mechanically sweeping —
  unlike the now-mobbed Erdős catalogue.

## 2. KEY DOCS (in this folder)
- `META_GUIDE.md` — strategy bible + case studies + problem-selection rubric + **append-only working
  log** (read the log top-to-bottom for the full chronology).
- `PROBLEM_ID_PIPELINE.md` — the Phase-I pipeline design spec (funnel, schema, heuristics, decisions).
- `problem-id/README.md` — how to run the pipeline.
- `OPENEVOLVE.md` — how to run the local OpenEvolve (Engine B) rig.
- `HANDOFF.md` — this file.

---

## 3. WHAT WE'VE DONE

**⭐ 2026-08-15 — ERDŐS #838: FULL CAMPAIGN PRESERVED; STATE DISTILLED AFTER EXTERNAL CRITIQUE.**
The complete 2026-08-14/15 attack is preserved verbatim in
`phase2/loop/erdos838/FULL_ATTACK_20260814.md` together with every agent
report and verifier.  The honest unconditional window is unchanged:
`1/4 <= liminf <= limsup <= 1/2`.  The campaign substantially constrained
recursive construction threats, proved exact minimizer/root identities,
developed pooled Hall/replacement codes, and produced many stretchable
barriers, but it did **not** improve the lower coefficient beyond `1/4`.
Claude/Fable's process critique is preserved at
`phase2/loop/erdos838/CRITICISM_20260815_claude.md`.

Four short additive navigation files now replace none of that information:
`CAMPAIGN_STATE_20260815.md` (truth and result map),
`DIFFICULTY_LEDGER_20260815.md` (GAIN/STRICT/EQUIVALENT/stop classifications),
`VERIFICATION_QUEUE_20260815.md` (five recent load-bearing packages needing
independent reconstruction), `BANKABLE_RESULTS_20260815.md` (short extracted
statements), and `PROVED_GAIN_STRATEGY_20260815.md` (one bounded next target).
The selected next target is fixed-size
supersaturation: for `n=2^(2k+o(k))`, prove
`v_k(P)>=2^((1+eta-o(1))k^2)` for any explicit `eta>0`; standard double
counting would then improve the unrestricted lower coefficient to
`(1+eta)/4`.  Full-strength/equivalent reformulations are parked.

**⭐ 2026-08-15 — ERDŐS #838: FIXED-SIZE BRIDGE PROVED; TWO AUDIT PACKAGES CLEARED; LITERAL WINDOW NARROWED.**
The implication from the canonical local target is now exact:
`mu_k(4^k)>=2^((1+eta-o(1))k^2)` implies unrestricted lower coefficient
`(1+eta)/4`; see `FIXED_SIZE_GAIN_BRIDGE_20260815.md`. For ordered strong
trees, `STRONG_TREE_FIXED_RANK_COMB_OR_SEAM_GATE.md` proves that either a
literal comb already gives `2^(2k^2-O(k log k))` rank-`k` faces, or one seam
has both children of size `4^k/poly(k)`. The remaining strong-tree gate is a
growing-rank, orientation-sensitive plane-caterpillar/profile problem.
Dossou-Olory's fixed-`k` unordered caterpillar theorem has the right
`3k^2/2` main exponent but a dominating finite-size error at `n=4^k` and
does not retain the plane itinerary; see
`FIXED_RANK_STRONG_TREE_CATERPILLAR_AUDIT_20260815.md`.

Independent audits are complete for all V1--V5. V1 received one explicit
finite-grammar splice repair and then passed; V2--V5 passed as stated. See
the five `V*_INDEPENDENT_AUDIT_*.md` reports indexed in the verification
queue.
Using V5 plus the current Erdős--Szekeres threshold,
`FIXED_SIZE_LITERAL_EXPLICIT_BOUNDARY_20260816.md` gives a load-one,
fibre-one pooled replacement for every literal history through rank
`1/4 log n-O(sqrt(log n log log n))` at `n=4^k`.
This is a genuine range gain, but it does **not** yet improve the
unconditional coefficient: the honest window remains `[1/4,1/2]`.

**⭐ 2026-08-16 — ERDŐS #838: LITERAL POOLING REACHES THE EXPLICIT QUARTER-LOG BOUNDARY.**
The parametric pooling calculation is now exact up to the error term in the
best Erdős--Szekeres threshold. If `ES(k)<=2^(k+G_k)`, every literal history
through rank `floor((k-G_k)/2)-3` is jointly coded into actual convex
`k`-faces with load and recovery fibre one. The theorem of
Holmsen--Nassajian Mojarrad--Pach--Tardos therefore gives, at `n=4^k`,
the explicit range
`r<=1/4 log n-O(sqrt(log n log log n))`. See
`FIXED_SIZE_LITERAL_EXPLICIT_BOUNDARY_20260816.md` and its verifier
(`PASS`, 1,012,274 combined exact rows). This removes the former unspecified
`o(log n)` approach to the boundary, but does not cross the structural
quarter-log capacity ceiling or improve the coefficient `[1/4,1/2]`.

V3 and V4 are now independently reconstructed and `PASS`. V3 covers the
hull-root recurrence, weighted increment, cumulative normalization, endpoint
moment/Pareto gate, and projective `n=8,9` corrections; both exact suites
were rerun. V4 proves exact causal curvature transport but also the sharp
full-ledger remapping obstruction: any ordinary-face remapping has fibre
`(1-o(1))` times the shelling weight. Thus only sparse child-excess or a
genuinely larger ordinary-output bank remains. The follow-up
`HULL_ROOT_INCREMENT_MOMENT_FLOOR_20260816.md` proves
the new exact bound
`K_(n,1)>=ceil(m_n(f(n))/n)+n-1`. It applies to the genuinely nonminimal
weighted child selected by the root envelope. At coefficient `c` it yields
only `(c+o(1))f(n)log n/n`, while half needs coefficient one, so summed
one-root moments are now quantitatively exhausted rather than mistaken for
closure.

**⭐ 2026-08-16 — ERDŐS #838: FIXED-SIZE PRIOR ART AUDITED; LOCAL HETEROGENEOUS SQUARE MESH PROVED WITH HARMONIC LOSS.**
The growing-rank target `v_k(4^k)>=2^((1+eta-o(1))k^2)` is not supplied by
the standard fixed-size literature. Ordinary Erdős--Szekeres double counting
has coefficient one; one positive-fraction transversal box cannot cross it
because the optimal universal cluster fraction is at most `2^{-k+o(k)}`;
and, at every cutoff, the exact weighted convex-polygon identities admit an
integral nonnegative fake ledger with maximal counts at all lower ranks and
no rank above the cutoff. The report and exact verifier are
`FIXED_SIZE_SUPERSATURATION_PRIOR_ART_AUDIT_20260816.md` and
`verify_fixed_size_supersaturation_prior_art_audit.py`.

Separately, the hinged Kraft theorem now gives an exact heterogeneous local
bound. For `m` children of total size `N`, exact weighted endpoint rewards
`R_i`, and `H_m=sum_(j<=m)1/j`,
`max_i((log n_i)^2/2+R_i) >= (log N-log H_m)^2/2-(log m)^2/2`.
The proof thresholds by the `j` largest children, allows a different hinged
witness at every threshold, and sums the resulting `n_j<=2^T/j` bounds.
Thus witness switching costs only `O(log N log log(m+1))`; the false nested
maximizer lemma is unnecessary. See
`HETEROGENEOUS_THRESHOLD_SQUARE_MESH_GATE_20260816.md` and its verifier
(`450,000` weighted instances, `1.8M` threshold checks). This is local
construction progress only: unrestricted geometric promotion and recursive
loss charging remain open, so the rigorous coefficient window is still
`[1/4,1/2]`.

**⭐ 2026-08-16 — ERDŐS #838: HARMONIC LOSS REMOVED LOCALLY; GROWING-RANK CATERPILLAR ERROR SOLVED; EXACT STAGE-C CONSTANT ISOLATED.**
Mass truncation strengthens the heterogeneous square mesh to
`L^2/2-O((log m+log L)^2)`, with no normalized weighted-Kraft assumption;
the tempting normalized inequality is independently killed by a rational
five-point example. See `TRUNCATED_WEIGHTED_KRAFT_SQUARE_MESH_20260816.md`
and `WEIGHTED_NORMALIZED_KRAFT_BARRIER_20260816.md`.

For every rooted full binary tree, the exact finite theorem
`R_k(T)>=b_k(n-2^(k-2))_+^k` removes Dossou-Olory's nonuniform growing-rank
error and gives `log R_k(4^k)>=3k^2/2+O(k)`. The ordered plane endpoint
formula is exact, but its naive shifted analogue is false on a 256-leaf
alternating comb, so strong-tree P1b still needs a shifted/excess orientation
comparison. See
`UNIFORM_GROWING_RANK_ROOTED_CATERPILLAR_THEOREM_20260816.md`.

The unrestricted Stage-C target now has an exact coefficient ledger. With
`p_j=v_j/C(N,j)`, `N=4^k`, and `r=alpha k`, any average decay bound
`log(p_r/p_k)<=(c/2)(k^2-r^2)+o(k^2)` with `c<2` yields
`eta=(1-c/2)(1-alpha^2)>0` and hence a strict unconditional coefficient
gain. The exact no-slack inequality `p_(j+1)>=2^-j p_j` is disproved at its
natural threshold by the rational 16-point double chain:
`(v4,v5)=(924,112)` and `p5/p4=5/99<1/16`. This does **not** kill the active
supersaturated asymptotic `c=1` form: the bad row lies outside the canonical
`N=4^k,j<=k` interval, its constant loss is absorbed by `2^-o(k)`, and all
later double-chain ranks have `p_(j+1)/p_j=(m-j)/(2m-j)`. The averaged
`c<2` gate and its asymptotic pointwise strengthening remain live.
See `SUCCESSIVE_RANK_DENSITY_GAIN_GATE_20260816.md`. The honest coefficient
window remains `[1/4,1/2]`.

**⭐ 2026-08-16 — ERDŐS #838: ADJACENT-LAYER GATE CORRECTED TO A FIXED CERTIFIED SIZE; UNIFORM SIZE WINDOW IS FALSE.**
Fix an explicit certified sequence `ES(j+1)<=q_j=2^(j+o(j))`. If every
`q_j`-point configuration obeys
`v_j<=2^((lambda+o(1))j)v_(j+1)` for one fixed `lambda<1`, then exact
averaging over induced `q_j`-subsets gives
`p_(j+1)/p_j>=2^(-(1+lambda)j-o(j))`. The successive-rank theorem therefore
improves the unrestricted coefficient to
`1/4+(1-lambda)(1-alpha^2)/8`. This is one strict reduction below the live
fixed-size target. Its kill criterion must be evaluated at that same fixed
sequence, not at an arbitrary size with the same leading exponent.

The quantifier correction is forced by a new exact stretchable barrier.
For even `j`, a cap-promoted central Pascal cell has
`C(j,j/2)+1=2^(j-o(j))` points and
`v_j/v_(j+1)>=2^Omega(j^2)`. Thus the uniform statement over all sizes
`2^(j+o(j))`, and the former size-free kill criterion, are false by a huge
margin. Internal central-Pascal layers and alternating combs remain safe at
the previously selected rows; the failure is a one-point top-rank
promotion. Any proof at the certified `q_j` must quantitatively use the
extra oversaturation slack, rather than only `log q_j=j+o(j)`. Heredity
alone is also hopeless: an abstract complex can contain every face through
rank `j` and only one `(j+1)`-face. See
`THRESHOLD_ADJACENT_LAYER_BALANCE_GATE_20260816.md` and its exact verifier.
There is positive finite evidence that the fixed-size distinction is real:
substituting a larger central-Pascal child at every physical leaf of the
promoted cliff, in all `1277` substitutions for `4<=h<=8`, forces
`v_j/v_(j+1)<0.0112`. Thus the obvious strong-glue padding does not move the
counterexample to the oversaturated side; its mixed `(j+1)` layer repairs
the cliff. A general support-to-mixed-extension theorem is still missing.

**⭐ 2026-08-13 — ERDŐS #1208: EXPLICIT CANDIDATE UPPER EXPONENT `0.49815` + FULL-GAP BARRIER MAP (Sihao + Codex ultracode).**
The live literature window is `n^(1/3) << F_2(n) << n^(1/2-epsilon)`; the
Erdős Problems page is stale because CFRN (arXiv:2606.05841) and LPZ
(arXiv:2607.05374) changed both endpoints in June--July 2026.  This attack's
apparently new ingredient is a prime-power valuation-pattern amplification of
the Minkowski-grid sieve.  A rank-17 totally real pro-2 tower with 55 certified
split primes and a 27-modulus adaptive phase cover yields the candidate
explicit theorem `F_2(n) << n^0.49815`.  The finite certificate checks 55
primes, 935 Legendre symbols, square-class rank 17, root discriminant
`3929160775540133527939545`, the knife-edge GS inequality `288<289`, and all
exponent intervals at 80 digits; an independent 150-digit replay and an
adversarial mathematical audit both pass.  This is **not a full solution and
not yet an externally established result**: the Shafarevich/class-tower input,
master sieve inequality, numerical interval hardening, and specialist novelty
clearance remain human gates.

The full-problem attack also proves a local entropy barrier showing that the
entire binary norm-lattice framework cannot reach exponent `1/3`; derives a
conditional lower improvement from any power saving in all-distinct distance
energy; and shows the square grid matches random 4-hypergraph edge/codegree
statistics at the cube-root barrier.  Generic containers, DRC, additive BSG,
semialgebraic Ramsey bounds, simple grid occupancy, tensor products,
finite-group orbits, polar layers, and dense-degree tower variants were all
audited and do not close the gap.  The durable restart brief—including proof
architecture, every meaningful dead end, exact commands, claim discipline,
and prioritized next steps—is
`phase2/loop/erdos1208/HANDOFF_20260813.md`.  No process is running.

**⭐ 2026-08-13 — ERDŐS #669: FULL ATTACK + PROOF-GRADE ZONOTOPE LOWER BOUNDS (Sihao + Codex ultracode).**
The problem was first corrected in the repository: #669 is the generalized orchard/rich-lines
problem, not the Heilbronn/fixed-area-triangle problem previously guessed in the shortlist. For
fixed `k`, it asks about the maxima `f_k(n)` and `F_k(n)` of exactly-`k` and at-least-`k` rich lines,
including existence of their normalized quadratic limits.

A rigorous lattice-zonotope construction now proves
`f_k(n),F_k(n) >= n^2/[4A(2k)]-O_k(n)`, where `A(2k)` is the minimum area of a convex lattice
`2k`-gon. For primitive normals `V`, the arrangement has exactly `n_q=2Dq+k` lines and
`Dq^2+kq+1` finite exact-`k` vertices, with `D=sum|det(v_i,v_j)|`; projective duality and generic
padding give the point-set bound. Mixed-area/Minkowski plus Simpson proves optimality throughout
the whole weighted/full-support lattice-zonotope scheme. The coefficients for `k=4,...,11` are
`1/28,1/56,1/96,1/160,1/236,1/348,1/484,1/656`, improving Palásti's printed table at
`k=4,5,6,7,8,11`. Exact projective enumeration passes for every stored direction set at `q=1,2`;
the independent four-direction checker passes through `q=30`.

**Novelty warning:** `1/28` is definitely 2019 web prior art (Zhao Hui Du), and the polygon,
Ehrhart, and direction ingredients are classical (Palásti, Stanley, Simpson, Deza et al.). No source
checked records the general orchard deduction or the new-looking `k=5,6,7,8,11` coefficients, but
they are only “apparently unrecorded” pending MathSciNet/zbMATH and specialist clearance. The full
problem is **not solved**: for `k>=4`, neither limit existence nor the exact constants are known.
The exhaustive restart document is
`phase2/loop/erdos669/HANDOFF_2026-08-13.md`; proofs and checks are in the adjacent
`FULL_ATTACK.md`, `ZONOTOPE_CONSTRUCTION.md`, `PRIOR_ART.md`, and verifier scripts.

**⭐ 2026-08-13 — ERDŐS #791: THREE FULL ATTACKS; COMPLETE CONTEXT HANDOFF WRITTEN (Sihao + Codex ultracode).**
The limit problem remains open and no numerical record was improved, but the latest attack removes
the previous finite-chromatic obstruction.  For every fixed `r`, an exact lattice construction gives
`r` tiles of size `t+O_r(1)` whose pairwise modular-cover graph is `K_r`; an optimized `K7` clears the
entire known density interval at the static-color level.  The decisive gap is now **temporal carry-state
compatibility**: at `t=251` that `K7` has only 25/441 ordered transitions, and tested larger scales retain
only the 21 self-loops.  Separate results prove a compactness/Fourier no-go for efficient raw-pair
triangles, an exact carry triangle that escapes it, a rank-one absorber, and a proof-certified finite
vertex-critical `chi=7` graph.  Independent audit found no mathematical downgrade after two short proof-
presentation repairs.  Latest synthesis: `phase2/loop/erdos791/full_attack3/FULL_ATTACK3_RESULT.md`;
audit: `full_attack3/AUDIT.md`; **complete restart context, including failed routes, traps, speculative
ideas, and prioritized next experiments:** `phase2/loop/erdos791/HANDOFF_20260813.md`.  Commits:
`2613093`, `d609e7c`.

**⚡ 2026-08-11→12 — G2 CLOSURE CAMPAIGN + PAPER REWRITE (Sihao + Claude, ~$1500).**
Full chronology in `META_GUIDE.md` §8; authoritative ledger in
`phase2/bruhat/f2_drafts/g2_campaign_20260811/CLOSURE_PLAN_v2_20260812.md`.
- **Method:** 7 waves. Waves 1-6 = Fable blind-draft/adversarial-referee fleets (~90 agents)
  until credits ran out; then **OpenAI gpt-5.6-sol at `effort=max`** via
  `g2_scripts/campaign_20260811/wave6_sol/{run_sol,verify_sol,orchestrate,orchestrate_verify}.py`
  (Responses API, background, id-journalled, retry-hardened) at ~$1-5/call.
- **CLOSED this campaign:** Prop 3.5(ii); Prop 3.5(i) reduced gap-free by Theorem S to the
  single lemma CL(79,20,0.89); **(S1) PROVED** (two-referee); exact harness extended
  m=150 → **560** (shrinking CL's obligation to `m >= 561` and closing G4's part-(c) band);
  T2's referee debt discharged.
- **(S2)** attempt 3 = self-contained proof, **entire numerical spine independently replayed
  locally** (found a real cell-width defect and 4 unflagged thin margins; provenance recorded
  in `s2_provenance_20260812.md`). **(S3)** consolidated into one self-contained document
  carrying its certificates. **(S4)** proved only `m >= 700`.
- **⚠️ THE CENTRAL FINDING — the composition was under-specified.** Adversarial review of
  `CL_composition` returned MAJOR_ISSUES (7 findings) and its repair concluded verbatim:
  *"closing the old statements (S1)-(S4) alone would not close CL."* Two further atomic
  obligations were split out: **(S5)** a `w`-continuum certificate, **(S6)** the bootstrap
  closure. (S5) has an unrefereed draft; **(S6) was attempted and NOT closed** (five named
  sub-gaps). **Net: open statements 4 → 5.** Nothing was found FALSE all campaign.
- **THE PAPER was substantially rewritten and is ship-ready** (`paper/submission/main.pdf`,
  14pp): F2 now a theorem CONDITIONAL on CL with (S1)-(S6) displayed and evidenced; the FALSE
  claim "(S1)-(S4) imply CL" purged from four sites; misattribution fixed (`q`-integer
  factorization is **Gasharov 1998**, not Carrell 1994); provenance language rescoped;
  hedged colon-free title; byline moved to a first-page footnote disclosing AI assistance;
  significance argued without overselling; 47-edit copyedit against a researched rulebook
  (Tao / Bertsekas / Halmos, `style_references_20260812.md`). Three adversarial review passes
  (2x DO_NOT_SHIP) preceded the final state. **Displayed mathematics untouched throughout.**
- **Two briefing defects found and patched** (both caused false-negative verdicts): agents
  were fed the stale wave-5 ledger; and briefs *asserted* certificates instead of attaching
  them (one FATAL was purely this). **Rule adopted: hand over the artifact, never the
  assurance.**

**Phase 0 — strategy (done).** Two adversarial deep-research runs established the AI-leveraged thesis,
case studies (GPT-5 Erdős #848, Erdős #728 via Aristotle/Lean, the peer-reviewed Malliavin–Stein
quantitative-extension, Liam Price's amateur Erdős #1196, AlphaEvolve/ShinkaEvolve), the credibility
bar, and a problem-selection rubric. All in `META_GUIDE.md`.

**Phase I — problem-identification pipeline (BUILT & RUN ONCE).** A durable, append-only,
idempotent funnel in `problem-id/`:
```
corpus/ ingesters → triage/filter.py (Stage1) → triage/score.py (Stage2) →
killsearch/killsearch.py (Stage3) → review/report.py (Stage4)      [orchestrated by run.py]
```
- **Corpus = 900 problems**, 4 sources: erdos 600, arxiv-openproblem 229, colt-openproblem 41, iqoqi 30.
- **First end-to-end run:** 900 → 775 (filter dropped 53 dupes + 1 famous) → **475 triaged** (gpt-5-mini)
  → top-50 single-problems kill-searched (gpt-5.5 + web) → **23 AMBER finalists, 0 GREEN, 28 RED.**
- **Result files:** `problem-id/review/finalists_detailed.md` (140 KB full dossier — each finalist has
  problem, win-condition, **cited closest-prior/novelty check**, the specific amber risk, and an
  Engine-A/B attack sketch) and `finalists.md` (terse table).
- **Survivors:** 18 Erdős, 4 arXiv, 1 QIT. They skew **Erdős additive-combinatorics & discrete
  geometry** — Nikol's wheelhouse. (COLT ML-theory problems mostly got RED-killed → they resolve fast;
  our alpha is more in combinatorics/number-theory/QIT.)
- **Validation that the rubric works:** the `llm_saturation_inv` axis correctly penalized the swept
  Erdős catalogue (avg 2.27) vs curated COLT/IQOQI (2.8/2.5); pass rates 52% Erdős vs 85% COLT.
- **Total spend so far ≈ $20.**

**Collaboration infra (2026-06-26).** Repo now on GitHub, shared Nikol + Sihao. Added `CLAUDE.md`
(auto-loaded session protocol: START = remind to set auto-accept/high-effort/ultracode + pull + read
this file; CLOSE = write the handoff + commit/push), plus `/load` (run the opening protocol) and
`/handoff` (run the close protocol) slash commands in `.claude/commands/`. API key relocated out of the
repo (§0). SSH auth configured per-machine. **Run `/handoff` at the end of every working session.**

**⭐ ERDŐS #838: SUBMISSION DRAFT + SHARP DECOMPOSABLE-CLASS THEOREM (2026-08-12→13, Sihao + Codex).**
The iterated vertical blow-up proves
`limsup log2(f(N))/(log2 N)^2 <= 1/2`.  For a fixed `r`-point template with
largest cap/cup sizes `a,b`, exact substitution identities give coefficient
`(a+b-2)/(2 log2 r)`; balanced Pascal templates approach `1/2`, and the cap--cup theorem makes
`1/2` the fixed-template optimum.  A 10-page submission-oriented draft is now at
`phase2/loop/erdos838/paper/main.tex` (rendered deliverable:
`output/pdf/erdos838_counting_convex_subsets.pdf`).  It contains the rational realization,
exact `C,U,W` identities, asymptotics, arbitrary-`N` step, self-contained Pascal construction,
and final bibliography.  It retains the original `article` typography and title-page flow, with a
blank conventional byline and the same Bregman-paper AI-assistance/contact disclosure in an
article-native first-page footnote for Nikol Savova (University of Oxford) and Sihao Huang
(independent researcher).  `lexicographic_blowup.py`
verifies a 9-point brute-force case and the
36-point count `(14136,14136,441399)` by unrelated endpoint DPs; the 16-point nonconvex-macro
exhaustion and reset arithmetic checker also pass.  Two mathematical referees plus a dedicated
primary-source novelty sweep found no proof flaw or prior occurrence.  Generic/iterated blow-ups
are prior art (Han et al.; Baek--Balko); the defensible apparent novelty is the prescribed mixed
orientations, exact unweighted substitution identities, and geometric coefficient `1/2`.

**New sharp theorem for the whole decomposable class.**  The earlier `1/3` lower bound is
superseded.  For every ordered binary strong tree with `N` leaves, the exact endpoint recurrence
and a multiscale reset argument prove
`log2 W >= (1/2)(log2 N)^2 - O((log N)^(3/2))`.  Hence arbitrary stationary or nonstationary strong
compositions have asymptotic coefficient exactly `1/2`.  The proof follows a heavy path through a
`4 sqrt(log N)`-bit window: either many tiny same-side siblings give exponentially many pure combs,
or `sqrt(log N)` macroscopic siblings force repeated endpoint-coordinate resets.  Two independent
adversarial reconstructions accepted the proof; see
`agent_asymptotic/NEXT_ENDPOINT_ATTACK.md`, `agent_geometry/NEXT_ENDPOINT_AUDIT.md`, and
`agent_killsearch/STRONG_TREE_HALF_REFEREE.md`.  The integrated proof is Section 5 of the paper.
The literature terminology has now been corrected: Balko--Kynčl--Langerman--Pilz (2017) introduced
decomposable point sets via recursive left/deep-below splits, and our `A≺B` convention is exactly
their mirror under `(x,y)↦(-x,y)`, with child order reversed.  Baek--Balko's full open-access JCTA
paper was checked: Theorem 7 is an existence theorem for this class, while Lemma 14 contains the
endpoint-cluster structural precursor to our count but neither sums all convex subsets nor derives
the `1/2` total-count theorem.  Both sources are now cited at the relevant definitions/lemma.

**Full-problem state.**  General Erdős 838 remains open with rigorous base-2 window `[1/4,1/2]`.
The strong-tree alignment gap is now closed, so the remaining obstacle is structural: transfer the
reset mechanism to arbitrary rank-3 order types, or extract sufficiently large approximate strong
pieces without losing the quadratic exponent.  Naive hinged-history compression is impossible by
the exact counterexamples in `agent_geometry/HISTORY_ATTACK.md`; simple contained maps have
`2^{Theta((log N)^2)}` fibres.  `agent_asymptotic/FULL_REGULARIZATION_TRANSFER.md` quantifies the
remaining barrier: extracting an `N^alpha` strong subset squares the exponent (`1/2` becomes
`alpha^2/2`); current mutually-avoiding extraction has `alpha=1/2`, and even a perfect
one-witness same-type pipeline is capped at the old `1/4`.

**2026-08-13 unrestricted follow-up.**  A fresh instance should first read the self-contained
`phase2/loop/erdos838/INSTANCE_HANDOFF_20260813.md`, then the detailed current map
`phase2/loop/erdos838/UNRESTRICTED_ATTACK_20260813.md`.  Three further routes are now rigorously
closed.  First, every finite-state vertical blow-up system---including state-dependent macro types,
reflections, unequal branching, and unequal child sizes---has liminf coefficient at least `1/2`;
see `agent_upper_multitype/FINITE_STATE_BARRIER.md` and the independent audit.  Second, the canonical
Baek--Balko `x`-blow-up is also blocked at `1/2`: explicit layer transversals and a canonical
score-two Pascal cluster give a conservative cover `>=0.5021396`; arbitrary noncanonical extremal
microcells are covered through `x/k=0.21` (computed crossing `0.21616...`) and remain a precise
loophole above it.  Third, even the global inequality
`H_q<=2^{O(q log q)}V` for hinged histories is false: on the six-point-template iterates at
`q=floor(log N)`, the history coefficient is exactly `1` while the convex coefficient is
`2/log2(6)=0.773705...`; see `agent_claude_review_audit/GLOBAL_HISTORY_AUDIT.md`.

On the lower side, all chains of hereditary fixed-`k` double counts telescope exactly, ideal
same-type transversals remain capped at `1/4`, and fixed-order convex-quadruple densities cannot
force `k=Theta(log N)` cliques.  The clean incremental target is growing-`k` supersaturation:
showing `mu_k(2^{2k+o(k)})>=2^{(1+eta-o(1))k^2}` for any `eta>0` improves the unrestricted lower
coefficient to `(1+eta)/4`.  The clean full target remains the exact common-two-endpoint inequality
`sum_{s<t}c(s,t)u(s,t)>=2^{(1/2-o(1))log^2 N}`.  **Immediate next gate:** human
MathSciNet/Zentralblatt/geometer clearance for the paper; mathematically, attack one of these two
growing-order/common-endpoint statements.  Do not claim the full problem solved.

**Post-campaign attack plan (2026-08-13).**  The concrete next programme is now
`phase2/loop/erdos838/PLAN_OF_ATTACK_20260813.md`.  Order the chord edges `e_1,...,e_M` by slope,
put `T_(i,j)(z)=I+zE_(j,i)`, and form the opposite products
`A=T_(e_M)...T_(e_1)` and `B=T_(e_1)...T_(e_M)`.  Their entries are the two-endpoint cup and cap
path polynomials, giving the exact new formulation
`V(P)=<A(1),B(1)>_F=trace(A(1)^T B(1))`.  The full lower bound is therefore a reverse-product
trace inequality for **stretchable type-A reflection orders**.  First gate: enumerate/search
reduced words and test the stronger all-reflection-order statement; then derive the exact
slope-filtered transfer formula across a contiguous cut and seek an arbitrary-order-type analogue
of the audited reset.  The same matrices with a variable `z` give the graded fallback
`[z^k]Z_P(z)=v_k(P)`, so the diagonal growing-`k` supersaturation target can be tested against the
actual upper construction before proof effort.  Initial exact checker:
`phase2/loop/erdos838/reflection_trace.py` (six-point self-test `(C,U,V,M)=(31,31,50,9)`).

**2026-08-13 ultracode reflection/mean/cut campaign.**  The durable synthesis is
`phase2/loop/erdos838/ULTRACODE_CAMPAIGN_20260813.md`.  Eleven parallel lanes established the
following.  All type-A reflection-order commutation classes through `n=7` were exhausted
(`24698` classes at `n=7`); the exact trace minima for `n=2,...,7` are
`3,7,14,26,44,72`, and every minimizer is rationally stretchable.  The exact mean-size deletion
identity reduces the full `1/2` lower bound to the conjecture that a uniformly random convex subset
of an `n`-point set has mean size at least `log2 n-O(1)` (only minimizers are needed).  Its closure-
lattice version is an average down-degree statement for realizable rank-three affine convex
geometries.  The tempting universal quadratic mean/count inequality is false on balanced Pascal
cells, but a low-mean minimizer dichotomy remains sufficient and live.

The reverse-product trace now has an exact contiguous-cut factorization through an ordered pair of
hull bridges and an exact rank-one long-braid switch formula.  These calculations also killed the
easy proofs: same-bridge reset is trivial; local braid descent and trace-compatible scalar
potentials fail; polynomial collision fails exponentially; and even capping only the crossing
trace fails with ratio `N^{-Theta(log log N)}`.  Every known collision counterexample hides enormous
convex mass inside one-sided blocks, so the correct surviving cut statement must be capped by the
*total* `V(P)`.  Earlier cut notes advertised a conditional `1/3` calculation using a
`(1/2-o(1))log^2 n` cap--cup product bound.  That product bound is **not known for arbitrary order
types** (it is itself a central missing theorem), so collision and tangent estimates alone do not
currently justify `1/3`.  Reaching `1/2` requires both stronger directional mass and a multiscale
endpoint-history reset.

The corrected total-cap theorem is quantitative but modest.  With
`E(x,y)=x log((x+y)/x)+y log((x+y)/y)`, if
`log V(P)<=(w+o(1))L^2` and `Q⊂P` has `|Q|=N^(alpha+o(1))`, then both `C(Q)` and `U(Q)` have
logarithmic coefficient at least the root `beta` of `E(w,beta)=alpha^2/4`.  At the target
`w=1/2,alpha=1`, `beta=0.0524142083...`.  This forbids polynomially one-sided macroscopic blocks
but does not improve `1/4`.  The conjectural square-root collision inequality survives exact tests,
yet its simplest injection is false.  Separately, weak long-braid sink rigidity and toggle-CDE were
killed by exact `n=8` and `n=7` certificates.  The braid route now has to address global
lexicographic `(V,M)` minimizers using full boundary-vector amortization.

The sharp fixed-size target
`log2 v_k(P)>=(3/2-o(1))k^2` at `log2|P|=2k+o(k)` remains open and would improve the unrestricted
lower coefficient to `3/8`.  It is now proved for every fine-grained, arbitrarily nonstationary
homogeneous vertical tower.  Separately, every vertical tower with arbitrary nonrepeating,
unbounded, possibly indecomposable macros and vanishing logarithmic mesh still has total
coefficient at least `1/2`.  Thus both upper and lower recursive escape routes require a
macroscopic template jump, heterogeneous children, or different mixed-triple geometry.  **The
unrestricted problem is still open with window `[1/4,1/2]`; do not claim otherwise.**

**2026-08-13 half-weight attack (latest state).**  The current primary dossier is
`phase2/loop/erdos838/HALF_WEIGHT_ATTACK_20260813.md`.  Put
`Z_P(z)=sum_{A convex}z^|A|` and `H(P)=n Z_P(1/2)/Z_P(1)`.  Proving only
`H(P)=n^o(1)` for minimum-count configurations implies
`E|A|>=(1-o(1))log2 n`; the exact deletion inequality then matches the upper
coefficient and solves the full problem with limit `1/2`.  The attractive finite conjecture
`H(P)<=2` survives all tests, but is still open.

The main new exact reduction is a random-prefix stopping time.  For a uniform permutation let `R`
be the last prefix in convex position.  For every hereditary face complex,
`Z_P(z)=E[sum_{k<=R} binom(n,k)z^k]`.  After tilting the law of `R` by the value of this partial sum
at `z=1`, the full target becomes `E_* 2^-R <= n^(-1+o(1))`.  In rank three the first failed prefix
contains a rooted four-circuit involving the arriving point.  This is now the preferred attack:
a **multistep, tilt-preserving first-circuit switch** with subpolynomial fibres.  A one-step version
cannot work: canonical visible-flip fibres have half-weight `((3/2)^m-1)/4`, and even a permissive
fractional one-step flow fails on the exact `n=20` record by `893/4`.

Two other corrections are load-bearing.  First, the sufficient shortcut
`mu_(1/2)>=log2 n-1` is false for exact integer planar configurations at `n=24,30` (deficits
`-0.022595,-0.082571`), although their actual `H` values remain only `1.686142,1.730215`.
The viable Coxeter statement is the integrated activity inequality
`integral_(1/2)^1 mu_t dlog2(t) >= log2(n/2)`, not endpoint control.  Second, individual
trace-descending braids can increase `Z(1/2)`, so matrix proofs must amortize absolute boundary
states.  A constant-loss weighted endpoint cup--cap inequality remains a plausible intermediate
lemma; its factor-one version is false.

The finite and construction audits also advanced.  Complete reflection/order-type scans give the
official empty-inclusive values `f(8)=114` and `f(9)=169`; the `n=9` minimizer is unique in the
database but has no lex-minimum deletion, killing hereditary lex induction.  A new exact `n=20`
configuration has profile `(1,20,190,1140,2415,866,135,8)` and `V=4775`, independently checked over
all `2^20` subsets.  The natural cyclic three-cluster continuation of the `n=9` minimizer is now
rigorously dead: an explicit binary subsystem forms a convex chain of size `2^r` at depth `2r+1`,
forcing stretched-exponential `V>=2^((N/3)^(log_9 2))`.  Immediate next work is the tilted
first-circuit switch, in parallel with an integrated deletion potential and constant-loss weighted
cup--cap recursion.  **No unrestricted proof or counterconstruction is claimed.**

**⭐ LEVER A — corpus broadened + de-noised (2026-06-29). Corpus 900 → 2206; Erdős bias broken.**
- **`PROBLEM_CRITERIA.md` (NEW, repo root) — the human-owned, strict spec of what counts as a "good
  problem."** Nikol owns/edits it; the automated gates approximate it. **Key principle (Nikol, this
  session): never penalize elementary/olympiad-style problems — exclude only CLOSED ones** (Erdős #1196
  is the model). All selection prompts now key on openness + research-grade, not statement difficulty.
- **Compilation-expansion built** (`corpus/expand_compilations.py`): fetches survey papers' full text
  (ar5iv/arXiv-HTML), LLM-extracts individual in-scope open problems as child records (`<parent>#<n>`),
  marks parents `expanded`. Scope-aware, idempotent, retry/backoff. **→ +1301 children** from ~150
  in-scope surveys (20 old-style pre-2007 arXiv ids unexpanded = ar5iv can't resolve; low priority).
- **Research-grade gate built + APPLIED** (`triage/research_grade_gate.py`): re-judges each expansion
  PARENT against `PROBLEM_CRITERIA.md` §3 and rejects children of recreational/benchmark/applied-eng/
  deep-machinery papers. **Dropped 34 parents → rejected 403 junk children** (wireless/RL/federated-
  learning/II₁-factors/alg-geom/Ibn-al-Khawwām historical).
- **West graph-theory ingester built** (`corpus/west_graphtheory.py`): 32 curated named conjectures
  (Tier-A, Nikol's domain). (Hannover OpenQIProblemsWiki was unreachable — skipped.)
- **Result: clean top-50 (stage=triaged) spans combinatorics 32 / number-theory 14 / graph-theory 13 /
  probability 12 / optimization 9 / discrete-geometry 8 / TCS 6** + group theory, coding, order theory.
  Genuinely diverse across home fields (NOT an Erdős monoculture). Corpus now: 1136 triaged, 565
  filtered, 411 rejected, 23 old-finalist, 28 deep-rejected. **Session spend ≈ $5-8** (gpt-5-mini bulk).
**RUN-2 kill-search DONE (2026-06-30): diversified top-50 → 22 AMBER finalists, 28 RED-killed** (gpt-5.5
+ web). All 22 AMBER (0 GREEN — same conservative pattern as run-1). NON-DESTRUCTIVE outputs (Nikol's
rule "erase nothing, new file only"):
- `review/finalists_run2.md` (table) + `review/finalists_run2_detailed.md` (full dossier — **the 22
  problems for Nikol to examine individually**). Run-1 files UNTOUCHED + backed up to
  `review/finalists_run1.md` / `finalists_run1_detailed.md`. New reporter: `review/report_run2.py`
  (reads the snapshot of run-1 ks-ids at scratchpad `prior_ks_ids.txt`; never touches run-1 files).
- Strong NEW non-Erdős targets (didn't exist before Lever A): spectral-radius extremal R(e,m)/W(w),
  Weil sums over finite fields, Bruhat-interval/Weyl-group conjecture, stadium-boundary + rational-point
  discrete geometry, numerical-semigroup cluster, pattern-avoidability, list-packing graphs, zero-sum.
  (2 stragglers to ignore: #11 "release a dataset" ML-benchmark, #22 multiple-access channel.)
- **DEEP PASS DONE (2026-06-30, `review/deeppass_run2.md`):** top-8 run-2 finalists, high effort, GO/
  MAYBE/NO-GO. **gpt-5.5-pro UNUSABLE for batch** (org 200k TPM → every call exhausted retries and failed;
  killed it) — re-ran with **gpt-5.5** cleanly. `deeppass.py` default now gpt-5.5 (Pro only for 1-2 hand-
  picked). **Result: 0 GO, 2 MAYBE, 6 NO-GO** — the stronger read is far more skeptical than the cheap
  kill-search and downgraded 6/8 (composite over-rates tractability; the "0 GREEN/GO" high-bar finding holds).
  **2 MAYBE survivors, both Engine-B:** (1) **Bruhat-interval log-concavity** (Weyl groups; Brenti Conj 2.11
  — counterexample OR exhaustive verification = clean self-certifying search target; the stronger one);
  (2) **R-stadium distance minimizers** (discrete geometry; fuzzier win condition).
- **🔬 CROSS-EXAMINED — two independent gpt-5.5 reads, consensus on the survivor (2026-06-30, Sihao).** Sihao
  ran the same top-8 deep pass independently (collision: both sessions ran it at once). His read = 1 GO /
  4 MAYBE / 3 NO-GO; Nikol's = 0 GO / 2 MAYBE / 6 NO-GO. **The disagreement is itself the finding** (the
  "never ship a single-model read — cross-examine" rule working): Sihao rated **Bruhat a GO**, but Nikol's
  read found the **Brenti Conj 2.11** framing + the exact missing large cases (A₆₊, B₅-short, B₆₊, D₆₊, E₆),
  correctly downgrading it to **MAYBE** (open, but the publishable bar needs the big Weyl groups — not a
  clean week-win). **Consensus = defer to the more-sourced conservative read:** the **R-stadium problem
  `2511.18217v1#2` (Engine B) is the one robust survivor both rate MAYBE**; Bruhat `2410.09897v1#13` is a
  real-but-harder MAYBE; everything else is NO-GO. Sihao's full read is preserved in
  `review/deeppass_run2_sihao.md` (Nikol's stays canonical in `deeppass_run2.md`).
- **⚙️ `deeppass.py` REWRITTEN durable + resumable (Sihao).** Each verdict now writes to a new DB `deeppass`
  column the instant it completes (syncs via the DB across handoffs — the old version wrote only to an
  uncommitted local .md and truncated it every run, so a stopped run lost everything and couldn't resume).
  Re-runs SKIP already-verdicted finalists (`--force` to redo); run-2 ids parsed from the committed dossier
  (no per-machine path). NON-DESTRUCTIVE: only the new column is written; `killsearch`/`stage` untouched.
  This makes finishing the deep pass cheap and interruptible. Default model = gpt-5.5 (both agreed).
- **✅ DEEP PASS EXTENDED — Sihao read now covers all 22 run-2 + 3 run-1 anchors (25 total, 2026-06-30).**
  Ran the remaining 14 run-2 finalists + the 3 named anchors (`erdos:791`, `erdos:653`,
  `arxiv-openproblem:1712.01960v1`). **Sihao-read tally across the 25: 4 GO / 13 MAYBE / 8 NO-GO**
  (in `review/deeppass_run2_sihao.md` + DB `deeppass` column). Notable:
  - **GO (4, single-model):** `1712.01960v1` diversity→ℓ1 (comp **4.94, the #1-overall problem**),
    `2410.09897v1#13` Bruhat (⚠ Nikol's read = MAYBE via Brenti — treat as MAYBE), `2307.06787v1#4`,
    `2406.00790v2#7` (numerical-semigroup sibling). The two new GOs came from the run-2 remainder the
    top-8 cut had skipped — Nikol's "top-8 leaves real candidates unvetted" worry was right.
  - **Anchors:** `erdos:791` (additive 2-basis, the Phase-II lead) = **MAYBE** (confirmed live);
    `erdos:653` = **NO-GO** (open-ish but not a 1-week win → drop as a pick).
  - **⚠️ CAVEAT — these 25 are Sihao's single-model read.** On the one problem both reads overlapped
    (Bruhat), Nikol's was stricter and better-sourced. So the 4 GO / 13 MAYBE are likely OPTIMISTIC; the
    real signal is consensus. **NEXT (see §7): cross-examine the GOs + top MAYBEs before committing.**
  - Still un-deep-passed: the other 20 run-1 finalists (beyond the 3 anchors). Lower priority — anchors
    were the strongest Engine-B bets; do them only if the cross-examined shortlist comes up thin.
  - Final Phase-II pool = 22 run-2 AMBER + 23 run-1 Erdős AMBER (45 total, diversified).
- **🌱 BROAD INGEST Wave 1 — TOPP + Open Problem Garden (2026-06-30, Sihao). Corpus ~2233 → ~2677.**
  New ingesters `corpus/topp.py` (78, computational/discrete geometry) + `corpus/open_problem_garden.py`
  (366 after purging 40 wiki spam; multi-field). **313 triaged into the funnel** (TOPP 62, OPG 251).
  Thesis sharpened (META §8): alpha = low-saturation ∩ **human-vouched-important** → **dropped machine-
  generated conjecture DBs** (obscure but not important/durable); target human-curated, format-siloed
  sources. Top new by composite: `opg:covering_powers_of_cycles...` **4.99** (beats the whole finalist
  pool), `topp:p34` 4.96. **⚠️ These are stage=`triaged`, NOT kill-searched** — not yet comparable to the
  45 finalists. Widening follow-up = kill-search the new diversified top. **Wave 2 backlog:** Kourovka
  Notebook (group theory), Kirby's list (low-dim topology), problem books (Guy, Brass–Moser–Pach),
  conference problem-session PDFs (BIRS/Oberwolfach/Dagstuhl), retry Hannover QI wiki + a source-discovery agent.
- **⏸️ KILL-SEARCH of the new top — STARTED, PAUSED at 8/50 (2026-06-30, Sihao). RESUMABLE.** Ran
  `killsearch/killsearch.py --top 50 --model gpt-5.5 --exclude-compilations` on the top-50 un-kill-searched
  triaged (34 new TOPP+OPG + 16 old). **Stopped at 8/50 done → +5 new finalists (finalists 45 → 50), all
  AMBER, all Wave-1 sources:** `topp:p34` (pseudosegment arrangements) + `topp:p48` (bounded-degree Euclidean
  MST) [discrete geom]; `opg:ramsey_properties_of_cayley_graphs`, `opg:covering_designs` [combinatorics];
  `opg:shannon_capacity_of_the_seven_cycle` [info theory — but FAMOUS = high-saturation, weak alpha].
  **3 RED-killed incl. the #1-composite `opg:covering_powers_of_cycles` (4.99): prior art exists** (known 2k
  upper bound + k+1 exact construction) → the recurring "high composite ≠ genuinely open" lesson, again.
  **TO RESUME (42 of the 50 left):** just re-run the same command — done ones are now finalist/deep-rejected,
  so it continues from #9 with no re-spend. Kill-search is slow (~1-3 min/problem, gpt-5.5+web); the stopped
  run was a clean day-end checkpoint (each verdict is committed per-problem, so nothing was lost).

**🌱 BROAD INGEST Wave 2 — Kourovka Notebook + Dagstuhl Reports (2026-07-01, Sihao). Corpus 2677 → 3284.**
Widened the pipeline with two NEW Tier-A ingesters (both fully filtered + triaged into the funnel):
- **`corpus/kourovka.py`** — the Kourovka Notebook (Unsolved Problems in Group Theory), from the arXiv
  LaTeX e-print of `1401.0300` (ar5iv can't render the ~250pp doc). Splits `\bmp…\emp` problem blocks,
  **cuts at the "Archive of solved" boundary so only currently-OPEN problems ingest**, defaults to recent
  issues (≥18, i.e. 2014–2026, ~422 problems; `--since-issue`/`--all` to widen). Two correctness catches:
  (1) the `\otv` star = an editorial ANSWER added post-2022 → 6 answered-but-unarchived problems split off +
  flagged `status_claimed=partially-solved` (the Erdősgate trap); (2) first title `"Kourovka N.M (Author)"`
  collapsed under Stage-1 lexical dedup (norm_tokens drops the number → same-author problems became
  identical → 182 false dupes) → switched titles to the problem's first sentence → 13 genuine dupes.
  **Result: 422 ingested → 254 triaged / 155 filtered / 13 dup. Avg composite 3.326; top `kourovka:21.115` 4.84.**
- **`corpus/dagstuhl.py`** — Dagstuhl Reports open-problem sessions (open-access, CC-BY, on DROPS). Enumerates
  DagRep volumes→issues→per-seminar PDFs, **field-filters by seminar title** (theory/math), downloads the PDF,
  isolates the "Open Problems" section (pymupdf — NEW venv dep), and LLM-extracts each posed problem (reuses
  `expand_compilations.extract`). Ran bounded on volumes **13–15 (2023–2025)**. **Result: 185 ingested → 154
  triaged / 29 filtered. Avg composite 3.761 — the HIGHEST of any source** (fresh expert workshop problems);
  top `dagstuhl:23121#2` 4.85 (perm-pattern Wilf equivalences). Minor noise (1 systems seminar slipped the
  scope filter) — downstream triage/kill-search gates it, as designed.
- **Two Wave-2 sources BLOCKED / deferred:** (a) **Guy 'Unsolved Problems in Number Theory' + Brass–Moser–Pach
  'Research Problems in Discrete Geometry'** — copyrighted Springer books, no lawful machine-readable text
  (only borrow-scans / infringing PDFs), and their famous problems are high-saturation. Legit substitutes to
  revisit: OEIS (open-conjecture entries) + Eppstein 'Geometry Junkyard', or Pach arXiv surveys via
  `expand_compilations.py`. (b) **Hannover OpenQIProblemsWiki** — unreachable from our environment on ALL paths
  (Python SSL / curl rc=28 / WebFetch ECONNRESET), same as 2026-06-29; also largely redundant with the existing
  `iqoqi-oqp` source. Retry later, low priority.
- **📊 NEW: pipeline dashboard + skill.** `review/pipeline_report.py` + `/pipeline-report` slash command
  (`.claude/commands/pipeline-report.md`). Shows SOURCES (done vs backlog/blocked), a **SCREENING & SPEND**
  table (per-gate coverage bar + model + cost tier + rough $ + done/waiting — makes the expensive $$$ stages
  and their backlog visible), OUTCOMES, a source×stage matrix (**on by default**; `--brief` to hide), and a
  Phase-II proof-engines block (planned, lights up when solve attempts are tagged). Editable registries at top.
- **📄 NEW: public-facing `README.md`** at repo root — plain, professional, framed around problem-discovery as
  the durable value as models improve at solving. (Nikol: check the Authors line — Sihao is listed "Independent",
  Nikol "Oxford"; and it's currently unlicensed. Approach section names the curated sources — trim if you'd
  rather not signal them publicly.)
- **⏹ Wave-1 kill-search FINISHED this session** (was paused at 8/50). Ran the full top-50 → **finalists 50 → 73
  (+23), deep-rejected 59 → 86 (+27).** ⚠️ **The new Kourovka/Dagstuhl problems are NOT yet kill-searched** — this
  run fixed its top-50 at launch, before they finished triaging. They now sit in the **1,750-triaged backlog**
  (incl. the high-composite ones), so a FRESH `killsearch --top 50` round is what screens them (see §7).

**⚡ PHASE II — SIHAO'S SCALED TIER DONE (2026-07-03→06, Sihao sessions). ~320k intervals, ZERO violations.**
Built the scaled search for the groups exhaustion can't reach (all in `phase2/bruhat/`, all selftested
against Nikol's `weyl.py` + each other; every run's dossier in `results/`, append-only):
- **Engines (3, independently cross-checking):** `scaled.py` (type-A permutations; rank_seq([e,v]) =
  Poincaré − complement-BFS-from-w₀ — the complement is tiny for v near w₀, so |W|=6.2B is reachable);
  `scaled_general.py` (any type, matrix pairs, lifting-property ≤); `fast.py` (root-action rewrite,
  ~1000× with multiprocessing; per-candidate ETA logging; `--skip` deterministic resume). Plus
  `sampler.py` / `fast.py --sample` (random short intervals [u,v]) and `seeded_probe.py` (perturbed
  dihedral equality cores).
- **Near-top slab sweeps ALL PASS: A₇ 1.054250, A₈ 1.038942, A₉ 1.028950, D₇ 1.025574, D₈ 1.017122,
  E₇ 1.011829 (first-ever E₇ verification, ran on CI in 204s) — every minimum at [e,w₀].** A₁₀ partial
  (deliberately stopped: S₁₁ complements out of pure-Python scope; [e,w₀]=1.022102 + an EXACT TIE by a
  proper interval; resume path documented in `results/fastscan_A10_partial_20260705.md`).
- **Sampling: 60k random short intervals (B₇/D₇/E₇) + 200k seeded equality-wall perturbations (B₇/B₈)
  — all pass.** The wall is STRICT: every perturbation of an equality interval raises the ratio; extremal
  perturbed shapes are rank-independent; closest non-equality margins are 4–8 (H₃-lookalike shapes).
- **⭐ STRUCTURAL FINDINGS (vetted by TWO independent literature reads — gpt-5.5+web probe + Claude-agent
  cross-exam; dossiers `results/theory_probe_gpt55_39009.md` + `theory_probe_crossexam_claude_20260704.md`):**
  - **F1 (apparently NEW):** in simply-laced Weyl groups the min log-concavity ratio over ALL Bruhat
    intervals = the min central ratio of the full Poincaré polynomial, attained at [e,w₀]; proper
    intervals tie (A₆, D₆, A₁₀) but never beat. Verified by completed sweeps in A₇–A₉, D₇–D₈, E₇.
  - **F2:** type-A [e,w₀] = Mahonian distribution ⇒ min ratio ≈ 1 + 1/σ² ~ 1 + 36/m³ (fits A₄–A₁₀ at
    ~0.91×). Log-concavity itself classical (Bóna; Hoggar/Kook); **must cite Canfield–Janson–Zeilberger
    Thm 4.6/eq. 4.11** (they have the 1+σ⁻² central ratio for the Gaussian binomial; our contribution =
    S_m case + global min + explicit constant).
  - **F3 (apparently NEW):** equality only via rank-2 dihedral parabolic patterns (1,2,…,2,1), m≥4.
    Candidate mechanism for WHY Weyl groups dodge H₃'s failure: H₃'s counterexample sits on an m=5 core,
    and m=5 is non-crystallographic — the only embeddable cores are m=4, which our 200k probes show
    strictly floored at ratio 1.
- **Infra:** `.github/workflows/bruhat-scan.yml` — manual-dispatch CI (6h runners, selftest gauntlet
  first, results as artifacts; minutes bill to repo owner). Proven on E₇. Local long runs: `nohup …
  & disown` + `sudo pmset -a disablesleep 1` (Sihao's Mac killed session-owned runs repeatedly).
- **Pipeline (parallel):** kill-search of the Kourovka/Dagstuhl backlog DONE → **96 finalists (+23),
  incl. the project's FIRST GREEN: `arxiv-openproblem:1003.3127v1#2` (conf high) — Nikol should review.**
- Session spend ≈ $17 OpenAI (theory probe ~$2, kill-search ~$15). Bug fixed along the way: `word_of`
  reduced-word order (crashed only on non-involutions; both engines fixed + selftest coverage added).

**⚡ PHASE II — ENGINE-A PROOF PHASE OPENED (2026-07-06, Sihao sessions; committed 2026-07-07).**
Compute is done; the work is now mathematics + writeup. All in `phase2/bruhat/`:
- **`PROOF_PLAN.md` (repo: `phase2/bruhat/PROOF_PLAN.md`)** — the Engine-A plan, priority order:
  (1) prove F2 anchor theorem, (2) F1 for rationally smooth subclass, (3) F3 short intervals,
  (4) the 0.91× second-order term, (5) paper skeleton NOW. Skeleton at `phase2/bruhat/paper/skeleton.md`.
- **A₇ + B₆ EXHAUSTIVE COMPLETE (CI, 2026-07-06):** A₇ = 170,288,585 intervals ALL PASS, global min
  1.054250 = the scaled tier's [e,w₀]-slab prediction EXACTLY (**F1 exhaustively confirmed in A₇**);
  B₆ all pass (another Brenti-list gap closed). CI `verify` mode added to `bruhat-scan.yml`.
  **E₆ exhaustive = the ONE remaining verification gap** (Nikol's original run never landed).
- **F2 THEOREM CAMPAIGN (ultracode: 4 blind drafts + 4 adversarial referees + merge) →
  `f2_drafts/F2_PROOF_DRAFT.md`.** Status: major-gaps ledger G1–G5; part (a) proved modulo G1+G2;
  **sharp second-order constant 27/25 found** (σ²(r_c−1) = 1 − (27/25)/m + O(m⁻²), verified to 6
  digits); the guessed c=7/8 constant REFUTED → corrected target **187/216**; finite checks exact
  to m=150. Blind-draft protocol: drafts must not read each other's `g1_*`/`g2_*`/`f1smooth_*` files.
- **G1 CLOSED (draft, ⚠️ UNREFEREED): `f2_drafts/g1_draft_b.md` + `g1b_scripts/` (6 scripts).**
  Both halves of ledger item G1 (Prop 2.1 constant C₁; kernel transfer to |E₁| ≤ C₂/m²) proved with
  explicit constants by direct Fourier-integral bounding (no Edgeworth package), from merged-draft
  Lemmas 1.1–1.5 only. Also identifies the EXACT m⁻²-order term N(y)/P(y)². Caveats (§8, honest):
  proved for m ≥ m₁(y₀) ≥ 180 vs harness exact to 150 → the band needs a harness extension (= G4's
  plan, minutes); wide-window C₂(3)=3940 inflated but downstream only needs y₀ ≤ 1 (within 3.4× of
  truth). **G2 (tilted frame) untouched — the natural next pass, same B.0–B.9 skeleton.**
  ⚠️ House rule pending: needs its adversarial referee before the ledger row flips to closed.
- **F1-SMOOTH SIDE-BET RESOLVED (refereed, verdict MINOR REPAIRS): `f2_drafts/f1smooth_draft.md` +
  `f1smooth_referee.md`.** **F1-smooth AS FROZEN IS FALSE** — two sharp counterexamples: (i) B₃/B₄
  rationally smooth (1,2,2,2,1) interval has r=1 < r(w₀) (simply-laced hypothesis necessary);
  (ii) **A₁×D₄, v smooth, violates** (irreducibility necessary — NEW). Corrected statement (§7):
  irreducible + simply-laced. Unconditional content: exhaustive verification through rank 6 (incl.
  E₆ smooth intervals), a proved type-A structural theorem (staircase + domination, Thm 4.4), type A
  through m=17 exact. Its analytic core (Conj SD/SD′) is ≥ as hard as F2 Thm A — it CONSUMES F2
  machinery, closes no F2 ledger gap. Referee re-ran every numeric check: all PASS (one off-by-one
  in NC-3's stated counts; conclusion unaffected).
- **⚠️ F1/F3 statements need re-wording for the paper:** F1's "simply-laced" must now ALSO say
  irreducible (the A₁×D₄ counterexample bites any version quantifying over reducible W); F3's
  dihedral-equality classification is consistent with the B₃ witness (it IS the (1,2,2,2,1) pattern).

**⚡ G2 T2 FINALIZED FOR REAL + two residue items explored (2026-08-05, Nikol + Claude).**
- **T2 draft (`f2_drafts/g2_draft_t2_20260803.md`) finalized.** The 2026-08-03 WIP had claimed
  "8 PASSes" from scripts that were never saved onto disk — this session caught it: all 10 numeric
  scripts (`g2_scripts/t2/`) were actually written and run, surfacing and fixing several real bugs
  in the first-pass claims (a sign error in T.6iii, a false certificate `1/60` that fails at
  `j=2,t=1/4`, a fabricated precision figure). **T2's own honest §8 verdict: G2 is NOT fully closed
  by T2 alone** — 3 residue items: (1) far-exponent/deep-tilt lemma, (4) T.9's mechanical bucket
  table, (5) same far-exponent issue as (1). T1 (the alternate direct-transfer route,
  `g2_draft_t1_20260803.md`) is still an unstarted 55-line skeleton.
- **Item 1 explored — confirmed hard AND necessary, not closed.** Diagnosed precisely why neither
  existing far-region mechanism (T.7b-final, T.7c) extends to `lam in (pi/m, 1/2]`: the `pi/m`
  near/far split is meaningless for fixed `lam>0` as `m` grows; T.7c's technique is small-tilt-only
  by construction (its prefactor is `e^{-Theta(m)}` for deep tilt). Ruled OUT an escape hatch — the
  hope that `sigma_lam^2 >= C_0` confines deep tilt to a shrinking range as `m` grows is FALSE (the
  max usable `lam` GROWS toward 1 as `m` grows), so this lemma is load-bearing across nearly the
  full tilt range for `m>=180`, not a corner case. A repair route (`(1+A_j)/(1+a)` exact factor
  identity) is identified but has an unresolved constant-chasing handoff between sub-regimes.
  Full writeup + diagnostic script: `f2_drafts/g2_item1_deep_tilt_notes_20260805.md`,
  `g2_scripts/t2_item1/diag1_deep_tilt.py`.
- **Item 4 explored — also under-scoped; its own proof text cites an unwritten "Lemma T.9'".**
  Built that missing lemma from scratch via sympy (the tilted 6-term Edgeworth model polynomial
  `P_lam(y)`, with the two new odd cumulant terms `kappa_3`, `kappa_5`), verified two independent
  ways (imaginary part cancels to exactly 0 symbolically; the untilted limit `alpha=delta=0`
  reproduces `g1_draft_b`'s known `N(0)` formula exactly, term for term). Found and resolved a real
  bucket-placement subtlety: `N_lam(0)` has a bare `alpha^2` term that's `O(1/m)` not `O(1/m^2)` —
  confirmed it's exactly the "`kappa_3^2`" piece the theorem's own proof already folds into the
  `w^2` bucket, just never shown explicitly. Grid-certified the resulting (correctly-scoped)
  pointwise bucket: `<= 1.55 (K=1), 4.09 (K=2), 4.91 (K=4)` — smaller than the draft's own `C_R~5.1`
  guess. Still open: the box/tail/out kernel-transfer bucket (likely dominant) and the Taylor-
  remainder bucket. Writeup + script: `f2_drafts/g2_item4_bucket_notes_20260805.md`,
  `g2_scripts/t2_item4/t2i4_nc1_model.py` (PASS).
- **Pattern worth flagging: every "quick/mechanical" label in the draft's own honest ledger
  undersold the real difficulty — both items explored tonight hid an unwritten sub-lemma.** Also
  recurring: every measured/certified constant has come in well BELOW the draft's own guesses —
  encouraging (suggests closure is blocked on *effort*, not on the maths being false), but neither
  item is close to finished. Session spend ≈ $0 API (subscription agent).

**⚡ TIER-2 PORTFOLIO OPENED — parallel proof-fleet direction + re-tag of all 96 finalists (2026-07-09, Sihao).**
Nikol keeps Bruhat; Sihao opens a SECOND lane: attack multiple candidates in parallel with a
**prover–verifier loop** — frontier reasoning models drafting PROSE PROOFS (blind drafts +
adversarial referees, the F2-campaign pattern), **Lean 4 + mathlib as the final soundness gate**
(formalize the STATEMENT first, human checks fidelity, then lemma-by-lemma proof attempt).
Design decisions this session: (a) Lean is the exit gate, NOT the inner-loop verifier (inner loop =
referees + numeric harness on finite instances); (b) the binding constraint is mathlib coverage →
every candidate needs a "mathlib-expressibility" rating; (c) the old GO/MAYBE shortlist was scored
for Engine-B search, i.e. the WRONG rubric for this mode → re-tag everything.
- **RE-TAG RUN (ultracode, 44 agents, ~16 min, ~$0 API):** all 96 finalists rated on proof_shaped /
  lemma_sized 0-3 / mathlib 0-3 / numeric_testable + a concrete FIRST LEMMA each; all 32 tagger
  STRONG/MEDIUMs then attacked by adversarial skeptics (default-to-disagree). **Taggers said 12
  STRONG / 20 MEDIUM → skeptics left 2 STRONG / 4 MEDIUM** (the "first reads over-rate tractability"
  pattern, now measured at 29 verdict changes).
- **Report: `problem-id/review/tier2_retag.md`** (+ `tier2_retag_raw.json`, all 96 rationales).
- **The 2 STRONG:** (1) **`erdos:838`** — now ATTACKED: the central-Pascal-cell coefficient was
  superseded by the iterated vertical blow-up candidate upper coefficient `1/2`; see the
  2026-08-13 block above and `phase2/loop/erdos838/`.
  Public-source novelty sweep passed; MathSciNet/expert confirmation remains.
  (2) **`arxiv-openproblem:1003.3127v1#2`** — the pipeline's FIRST GREEN, now with a **verified candidate
  counterexample** (Bregman right-projections of a nonconvex curve under negative entropy: skeptic
  fetched the source survey, confirmed statement fidelity, checked g''≥3.45>0 on [1,2] — "I tried hard
  to kill this and failed on the mathematics"; solution may be HOURS-scale; residual risk = novelty
  sweep of citing papers + a second construction for the cl C*⊆U* half to make a complete note).
- **The 4 MEDIUM:** `dagstuhl:23121#2` (Wilf-equivalence bijection, Burstein Conj 16 slice),
  `kourovka:19.20` (|PIso(G)|>|End(G)| for minimal nonabelian), `2511.01306v1` (ternary cyclic codes —
  quadratic-character count kills the h=m−1 slice), `2206.06472v4#12` (benzel tiling 2-adic periodicity).
- **NOT built yet:** `phase2/loop/` harness + per-problem specs/verifiers (design agreed in-session:
  PROBLEM.md = frozen statement + machine-checkable win condition + kill criteria; verify.py written
  before any prover runs; Tier-1 certificate fleet as cheap uncorrelated side bet).

**Top candidates from RUN 1 (still valid; Erdős AMBER, already kill-searched) — Phase II warm-start:**
1. **Erdős #791** — additive 2-basis `g(n)` (minimal `A⊆{0..n}` with `A+A ⊇ {0..n}`). Records:
   Kohonen 2017 upper `85/294`, Yu 2015 lower. **Concrete attack:** SAT/MILP search for a better
   *segment-placement certificate* beating Kohonen's `85/294` — scalable & Lean-checkable. Strongest
   Engine-B fit. (Amber risk: a one-off small example isn't enough; need a *parametric/scalable* tiling.)
2. **Erdős #653** — max number of distinct "distance counts" of n planar points; gap `0.7n` (Csizmadia)
   to `n−cn^{2/3}`. Gadget-substitution attack.
3. **arXiv 1712.01960** — worst-case distortion embedding an n-point *diversity* into ℓ1; LP/cut-cone
   duality attack with rational certificates.

## 4. WHAT STILL NEEDS TO BE BUILT

**Erdős #838 post-critique obligations (current priority).**

- [x] Finish independent reconstruction of V1--V5 in
  `phase2/loop/erdos838/VERIFICATION_QUEUE_20260815.md`. V1 required one
  minor repair; V2--V5 passed. All five formerly frozen packages now have
  proof reconstructions as well as exact verifier replays.
- [x] Prove and verify the exact implication
  `(P1 at n=4^k) => liminf >= (1+eta)/4`.
- [ ] Continue `(P1)` only through the narrowed range
  `1/4 log n-O(sqrt(log n log log n)) < r < log n`. The current universal
  pooled-capacity estimate stops at its `r=(1/4)log n` boundary; the next
  lemma must use a larger configuration-specific bank, selected-family
  sparsity, mixed geometry, or a profile charge.
- [x] Audit standard fixed-size counting inputs. Fixed-`k` asymptotics, one
  positive-fraction transversal box, and scalar weighted polygon identities
  all stop at the coefficient-one boundary or fail to encode high-rank
  compatibility.
- [x] Replace the conjectural local heterogeneous square mesh by the exact
  threshold theorem with harmonic loss. Do not spend further work on nesting
  the maximizing paths; the remaining task is a global loss charge or an
  unrestricted geometric promotion.
- [x] Remove the nonuniform finite-size error in unordered growing-rank
  caterpillar inducibility. The exact shifted theorem is proved and verified.
- [ ] For the strong-tree subcase, prove a shifted/excess orientation
  comparison for the exact endpoint formula. The naive same-constant plane
  analogue is false and must not be reused.
- [ ] For unrestricted P1, beat the successive-rank density-decay constant
  `c=2` on one fixed interval `alpha k<=j<k` at `N=4^k`. Any fixed
  `c<2` gives the explicit gain recorded in
  `SUCCESSIVE_RANK_DENSITY_GAIN_GATE_20260816.md`. The most concrete child
  is P1e at one fixed certified `q_j`; the exact no-slack `c=1` inequality
  and the uniform `2^(j+o(j))` size-window version are false. Any P1e proof
  must use the certified sequence's oversaturation to force mixed
  `(j+1)`-faces.
- [ ] Enforce `DIFFICULTY_LEDGER_20260815.md`: mark coefficient-equivalent
  reductions `EQUIVALENT` and stop them; cap new chains at three reductions
  without an explicit coefficient/range gain.
- [ ] Extract the independently accepted construction-closure and barrier
  packages into a short self-contained paper section.  The 13,000-line log is
  evidence/archive, not a publication draft.
- [ ] Do not describe the campaign as “78% of the proof.”  Approximately
  `75--80%` refers only to the mapped obstruction architecture; the
  unconditional lower-bound coefficient has not moved from `1/4`.

**Erdős #1208 candidate-result obligations.**

- [ ] Obtain a human number-theory audit of the rank-17 tame totally-real
  Shafarevich/Golod--Shafarevich specialization and a separate geometric-
  combinatorics audit of master inequality (3.5).
- [ ] Replace the high-precision Decimal endpoint checks by directed interval
  or exact rational transcendental bounds; current 80/150-digit runs agree
  with minimum transformed margin `4.25e-5`.
- [ ] Run MathSciNet/zbMATH/forward-citation and author clearance for the
  prime-power and adaptive-modulus ideas.  Only then draft a short note around
  the candidate `F_2(n) << n^0.49815` theorem.
- [ ] For the full problem, do not optimize more tower dimensions or generic
  codegrees.  The live lower targets are an inverse/stability theorem for
  near-extremal Elekes--Sharir configurations or a rainbow principal-submatrix
  theorem for rank-at-most-four Euclidean distance matrices.  See the dedicated
  handoff §§8--14.

**Erdős #669 candidate-result obligations.**

- [ ] Run a specialist-grade MathSciNet/zbMATH/citation clearance of the general orchard deduction
  and the `k=5,6,7,8,11` coefficients. The `k=4` coefficient is known prior art.
- [ ] Obtain an independent human line-by-line proof audit of the lattice converse, infinity points,
  padding, sublattice factor, and mixed-area optimality.
- [ ] Only if both gates pass, turn `phase2/loop/erdos669/ZONOTOPE_CONSTRUCTION.md` into a short,
  conservatively claimed note with both exact verifiers attached.
- [ ] A full solution still requires exact global constants and/or existence of the normalized limits
  for `k>=4`; superadditivity, sampling, and `O(n)` increments provably do not suffice.

**Erdős #791 full-solution frontier.**  Do not restart with another static role clique: arbitrary
fixed `K_r` is now constructed exactly.  The live obligation is one of: (i) a temporal
representation/role-assignment theorem giving `k+o(k)` cost while consecutive targets follow legal
carry transitions; (ii) a new choice of integer lifts with an asymptotically mixing state automaton;
or (iii) a carry-rectangle theorem placing all remaining holes in `U+V` with
`|U|+|V|=o(k)`, after which the proved absorber closes `alpha_-=alpha_+`.  First computational step:
jointly optimize target representation choice, coordinate roles, and ordered transition legality on
finite extremal bases; role-only CP models now discard the critical information.  Full specifications
and audit traps: `phase2/loop/erdos791/HANDOFF_20260813.md` §§10–15.

**CURRENT OBLIGATION LIST for Theorem A (supersedes the older Bruhat items below).**
`Theorem A = G1 (closed 08-02) + G2`; `G2 = Prop 3.5(ii) (CLOSED) + 3.5(i)`; `3.5(i)` reduces
to `CL`, which holds by exact computation for `m <= 560` and needs, for `m >= 561`:

| | statement | status |
|---|---|---|
| (S1) | banded cumulant scales | **PROVED** (two-referee) |
| (S2) | fifth-order remainder `R5` | proof + full independent numeric replay; maths-lane MINOR_REPAIRS unapplied |
| (S3) | joint cancellation | consolidated document, **0 referee lanes** |
| (S4) | a-priori ratio seed | proved only `m >= 700`; `[561,699]` carried by (S5) |
| (S5) | `w`-continuum certificate | drafted, **0 referee lanes** |
| (S6) | bootstrap closure | **NOT CLOSED** — five named sub-gaps |

- [ ] **Referee lanes owed on four documents** (all unciteable until they land):
  `sol_comprepair`, `sol_s3consol`, `sol_s5cont`, `sol_s6boot`. Cheap via
  `wave6_sol/orchestrate_verify.py <file>:maths <file>:numerics` (Sol, ~$1-5 each).
- [ ] **Hygiene-overlay verifier** — gates the `m >= 561` finite-range splice.
- [ ] **Exact-rational redo** of the interval certificates — the last standing methodological
  objection ("rigorous modulo `mpmath.iv`", not the advertised exact-rational). Margins are
  wide (worst 0.056%), so a coarse rational envelope for `exp`/`cos`/`sin` would clear it.
- [ ] **(S6)** is the real mathematics and has never had a working argument. If a seventh
  obligation appears anywhere, the ledger's own read says it appears here.

**RECOMMENDATION OF RECORD (Claude's; humans may overrule):** ship the conditional paper and
state (S2)-(S6) in it as explicit open problems with their constants; do not resume fleet
spending to chase unconditional Theorem A.

**Pipeline scale-up (the "bigger intake" — now at 3284, goal tens-of-thousands):**
- [x] ✅ **Compilation-expansion pass** — DONE (`corpus/expand_compilations.py`, +1301 children) + the
  **research-grade gate** (`triage/research_grade_gate.py`) to de-noise it. See §3.
- [x] ✅ **Tier-A ingesters** — West graph theory (`corpus/west_graphtheory.py`, 32); Wave-1 TOPP + Open
  Problem Garden; **Wave-2 Kourovka Notebook (`corpus/kourovka.py`, 254 triaged) + Dagstuhl Reports
  (`corpus/dagstuhl.py`, 154 triaged) — DONE 2026-07-01.** See §3.
- [ ] **Kill-search Kourovka + Dagstuhl (IMMEDIATE NEXT — see §7).** Their ~408 triaged problems are NOT yet
  kill-searched (Wave-1 run finished before they triaged). Run a fresh top-50 to screen the high-composite ones:
  `./.venv/bin/python killsearch/killsearch.py --top 50 --model gpt-5.5 --exclude-compilations`. ~$15.
- [ ] **More high-volume ingesters:** DeepMind `formal-conjectures` Lean repo; **OEIS** (open-conjecture
  entries); **full-text arXiv mining**. (Automated-conjecture DBs dropped — obscure but not durable, see META §8.)
- [ ] **More Tier-A curated lists:** OEIS + Eppstein 'Geometry Junkyard' (the lawful stand-ins for the
  copyright-blocked Guy/Brass–Moser–Pach books); Kirby's list (low-dim topology); more COLT years; Barbados PDFs;
  MathOverflow `open-problem` tag. (Hannover OpenQIProblemsWiki still UNREACHABLE 2026-07-01 + redundant w/ iqoqi.)
- [ ] **gpt-5.5-pro deep pass** on the top ~8 finalists once the diversified set is kill-searched (org
  TPM=200k → throttle; `--model gpt-5.5-pro`).
- [x] ✅ **(Bruhat) Referee `g1_draft_b.md`** — DONE 2026-08-02: SURVIVES WITH MINOR REPAIRS (see §3);
  repairs 1+2 also done same day. G1 row of the F2 ledger closed.
- [ ] **(Bruhat, PROOF-CRITICAL) G2 (tilted frame)** — IN PROGRESS, not closed. T2 draft
  (`f2_drafts/g2_draft_t2_20260803.md`) finalized 2026-08-05 with real numeric scripts, but its own
  honest §8 says G2 is NOT closed by T2 alone: 3 residue items, 2 explored 2026-08-05 (both confirmed
  hard, both have real partial progress, neither finished — see §3's 2026-08-05 entry and
  `f2_drafts/g2_item1_deep_tilt_notes_20260805.md` / `g2_item4_bucket_notes_20260805.md`). T1 (the
  alternate route) is still an unstarted skeleton. G1+G2 ⇒ Theorem A = F2(a), once G2 lands.
- [x] ✅ **(Bruhat) E₆ exhaustive — DONE by Nikol (2026-07-08 push):** 466.2M intervals, 0 violations,
  min ratio 1.028446; B₆ 350.7M also complete. Exhaustive tier CLOSED. Only loose end: E₆ seg-1
  witness interval not recorded (re-scan u<6000 only if wanted for the writeup) — see
  `phase2/bruhat/results/run_B6-E6_segment_coverage.md`.
- [ ] **(Tier-2) Build `phase2/loop/` for the remaining survivors** — `erdos:838` is DONE
  (candidate `1/2` upper proof + exact geometry/DP + kill-search; original limit still open);
  per-problem dirs are still owed for the other five.
  Then the draft→referee→Lean fleet. See §3 Tier-2 block + `review/tier2_retag.md`.
- [ ] **(Tier-2, FIRST) Novelty sweep for `1003.3127v1#2`** — page-by-page sweep of works citing
  the survey (the construction is a one-character tweak of the authors' own Example 3.3; skeptic +
  killsearch found no resolution but it is the residual risk). **`erdos:838` public-source sweep is
  DONE**; its `1/2` theorem still needs independent proof review plus MathSciNet/expert confirmation.
- [ ] **(Bruhat) Harness extension m→200** (`mahonian.py` exact run, ~minutes) — covers the
  150<m<m₁ band g1_draft_b needs (= G4's plan).
- [ ] **(Bruhat, optional) A₁₀ deep slab**: port the complement-BFS hot loop (`fast.py`) to C/Rust, or
  run in 6h `--skip` chunks on the `bruhat-scan` CI workflow. Resume: `--scan A10 --cogap 2 --skip 4`.
- [ ] **(Bruhat, optional) OpenEvolve / local search** minimizing MARGIN over the perturbed-braid family
  (`seeded_probe.py` found margin-4 H₃-lookalikes — the counterexample-adjacent zone if one exists).
- [ ] Light: old-style pre-2007 arXiv ids (20 compilations) don't expand (ar5iv can't resolve the
  archive-prefixed id); embeddings dedup; a couple applied stragglers survived the gate (kill-search catches).

**Phase II — the solve sprint (NOT STARTED):** pick 1–3 finalists from the dossier and actually attack
them with Engines A/B + Lean. The 7-day plan is in `META_GUIDE.md` §5.

## 5. HOW TO RUN (after the post-move checklist)
```bash
cd problem-id
# add a source (copy an existing ingester):
./.venv/bin/python corpus/<name>.py
# full funnel (filter -> triage -> killsearch top50 -> report); idempotent, only scores NEW problems:
./.venv/bin/python run.py --ingest <name> --no-killsearch        # cheap: stop before Stage 3
./.venv/bin/python triage/score.py --workers 8                   # triage just (gpt-5-mini, ~cheap)
./.venv/bin/python killsearch/killsearch.py --top 50 --model gpt-5.5 --exclude-compilations  # ~$10-25
./.venv/bin/python review/report.py --stage finalist --top 50
```
**Models:** triage = `gpt-5-mini` (cheap, concurrent); kill-search = `gpt-5.5` (bulk) or `gpt-5.5-pro`
(top picks, TPM-limited). **Idempotency:** `score.py` skips anything already scored (`scores IS NULL`
guard) — growing the corpus never re-spends. Use `--rescore` only to force re-scoring (e.g. after a
rubric-prompt change). `rubric.yaml` weights are LOCKED v1; `--recompute` re-derives composites with no API.

## 6. WHAT'S ON MY MIND (prior session's read — opinions, not gospel)
- **⭐ THE ERDŐS-BIAS DIAGNOSIS (2026-06-26, quantified — Nikol flagged it, data confirmed it).** The 23
  finalists are 18 Erdős / 4 arXiv / 1 IQOQI, which looks like the funnel loves Erdős. **It does not — the
  rubric actively PENALIZES Erdős; the bias is structural (volume + kill-search attrition):**
  - Per-source avg composite: **COLT 3.765 (highest) · IQOQI 3.619 · arXiv 3.282 · Erdős 3.237 (lowest).**
    `llm_saturation_inv`: COLT 2.80 · arXiv 2.78 · IQOQI 2.50 · **Erdős 2.27 (correctly penalized).** The
    curated low-saturation lists score *higher per problem*, exactly as designed.
  - **Cause 1 — volume:** corpus is 67% Erdős (548/866 scored). The global top-50 that reach kill-search
    were **34 Erdős / 9 arXiv / 4 IQOQI / 4 COLT** — Erdős wins on sheer count despite the lowest mean.
  - **Cause 2 — attrition:** all 4 COLT that reached Stage-3 were RED-killed (ML-theory resolves fast).
    The single highest-scoring problem in the whole run (`awasthi23a`, composite 4.679 — above EVERY Erdős
    finalist) was RED-killed as already-resolved. So COLT → **0 finalists** despite the best average.
  - **Note:** the #1 finalist overall is NOT Erdős — arXiv `1712.01960` diversity→ℓ1 (comp 4.936, sparse
    literature, no AI attention found). 5 non-Erdős survivors total (4 arXiv + 1 IQOQI).
  - **TWO LEVERS TO FIX (decided 2026-06-26):**
    - **Lever A (real fix): broaden the corpus** — ✅ **DONE 2026-06-29** (compilation-expansion +1301,
      West +32, research-grade gate −403 junk; corpus 900→2206, top-50 now field-diverse). See §3.
    - **Lever B (cheap source-diversity quota in `review/report.py`)** — NOT done, and **likely now
      unnecessary**: Lever A diversified the corpus directly, so a quota may be moot. Reassess after the
      diversified kill-search. (If still wanted: take top-N per source instead of a global top-50.)
- **"0 GREEN, all AMBER" is the real finding.** The bar — genuinely-open AND tractable-in-a-week AND
  self-certifying AND novel — is high. The recurring amber risk is *"a one-off small-n example won't be
  publishable; you need a scalable/parametric certificate."* **Phase II should therefore target problems
  where a parametric construction is plausible** (Erdős #791 fits — Kohonen's template is parametric).
- **COLT ML-theory problems getting RED-killed is a genuine signal**, not noise: those communities close
  open problems fast. Our durable alpha looks like Erdős-style additive combinatorics / discrete geometry
  / extremal stuff + QIT (Sihao's edge), less so ML-theory.
- **My recommended next move:** a quick **gpt-5.5-pro deep pass on the top ~8 finalists** (~$10-20, de-risks
  the week-long commitment), THEN **pick 1–3 and start Phase II** — I'd lead with **Erdős #791** (clearest
  scalable-certificate Engine-B attack + Lean-checkable) and keep #653 / the diversity-embedding as
  backups. Then in parallel, build **compilation-expansion + 2-3 more Tier-A ingesters** to enrich the next
  funnel run.
- **Don't skip the kill-search ever.** It killed 28/50 here and caught real already-solved cases (e.g.
  COLT `awasthi23a`, resolved by two 2024 papers). It is the single most valuable stage.
- Light tech debt: Stage-1 dedup is lexical (fine for now); arXiv ingester treats plural-title papers as
  "compilation" (the thing the expansion pass fixes); the venv must be recreated post-move.

## 7. IMMEDIATE NEXT ACTION — ⭐ NIKOL + SIHAO, START HERE

### ⭐ 2026-08-16 — ERDŐS #838: STANDARD SHORTCUTS EXHAUSTED; ATTACK CROSS-RANK GEOMETRY

Read, in order:

1. `phase2/loop/erdos838/CAMPAIGN_STATE_20260815.md`;
2. `phase2/loop/erdos838/DIFFICULTY_LEDGER_20260815.md`;
3. `phase2/loop/erdos838/VERIFICATION_QUEUE_20260815.md`;
4. `phase2/loop/erdos838/BANKABLE_RESULTS_20260815.md`;
5. `phase2/loop/erdos838/PROVED_GAIN_STRATEGY_20260815.md`.

The full `FULL_ATTACK_20260814.md` and all agent artifacts remain preserved
for lookup. All V1--V5 packages now have independent audits. The
exact fixed-size bridge, strong-tree comb/seam theorem, caterpillar audit, and
explicit-boundary literal pooling theorem are the current positive additions.
Also read `FIXED_SIZE_SUPERSATURATION_PRIOR_ART_AUDIT_20260816.md`,
`TRUNCATED_WEIGHTED_KRAFT_SQUARE_MESH_20260816.md`,
`UNIFORM_GROWING_RANK_ROOTED_CATERPILLAR_THEOREM_20260816.md`, and
`SUCCESSIVE_RANK_DENSITY_GAIN_GATE_20260816.md`. The first excludes the
standard counting shortcuts; the second proves the local square mesh with
only polylogarithmic-square loss; the third removes the unordered
growing-rank error while isolating the plane obstruction; and the fourth
states the exact strict coefficient-bearing Stage-C target.

Next attack the cross-rank extension graph at `N=4^k`: prove an averaged
density decay constant `c<2` over one fixed positive fraction of the ranks,
or derive the same gain from the convex-four-set circuit deletion map. A
failed one-point extension naturally yields a retained convex hull and a
deleted convex subface; the exact unresolved operation is to turn that
two-target record into one ordinary face with subquadratic history load.
Do not strengthen the conjecture down to `N~2^j` (that is a separate major
Erdős--Szekeres improvement), and do not restart fixed-`k` asymptotics, one
same-type box, scalar hull identities, or threshold-path nesting.
If the next bounded attack produces neither an explicit `eta>0` nor another
proved rank range, stop and package the `1/2` upper/strong-tree theorem plus
the audited construction and barrier results. Nothing is currently running.

### ⭐ 2026-08-13 — ERDŐS #838 IS THE ALL-IN TARGET: READ `RESUME_838.md` FIRST
**Entry point: `phase2/loop/erdos838/RESUME_838.md`.** It indexes every 838 document, states
current truth, and lists corrections to earlier files. Read it before
`INSTANCE_HANDOFF_20260813.md` (still the best deep dossier) or any campaign output.

Why 838 got the all-in decision: we already own `limsup ≤ 1/2` (`paper/main.tex` Theorem 1.1,
independently verified), so **one theorem — `liminf ≥ 1/2` — resolves the problem outright**, limit
existence and value together. No other target in this repo has that property.

State after the 2026-08-13 seven-lane campaign (`scripts/campaign_lower.py`):
- **The correct target is the ENDPOINT-LOCALIZED product** `max_{p<q} c(p,q)u(p,q)`, i.e. Sol's
  inequality `(EM)`. The *global* cap–cup product is provably insufficient: `C,U ≤ N²M` costs a
  factor of two and lands back on the published `1/4`.
- **Barrier proved:** all asymmetric cup–cap double counts obey `(c+u)H(c/(c+u)) ≥ 1/4`, so the
  method behind the published bound **cannot exceed 1/4**. Clean, apparently novel, worth banking
  independently of whether `(EM)` ever falls.
- **Two routes closed:** canonical tree decompositions do not bridge to indecomposable order types;
  Székely does not transfer *and was never evidence* — his normalized lower coefficient is ≈0.1577,
  and `prior_art_20260812.md` now carries a correction.
- **Premise survived:** nothing beat coefficient `1/2`.
- **Still unverified:** the multiscale reset page inside Theorem 5.1. Do this first — its structure
  is the template for `(EM)`.
- **Submission gate:** the Baek–Balko clearance used the SoCG extended abstract, which omits the
  proofs of its Theorem 8 and Lemma 14. Buy the JCTA 222 (2026) 106195 version before submitting.

Nothing is running.

### ⭐ 2026-08-13 — ERDŐS #1208 EXPLICIT-EXPONENT CANDIDATE: EXTERNAL AUDIT BEFORE DRAFTING
Read `phase2/loop/erdos1208/HANDOFF_20260813.md` completely, then run
`python3 phase2/loop/erdos1208/verify_adaptive_rank17.py`.  The candidate
result is `F_2(n) << n^0.49815`, not a full solution.  Before circulating it,
obtain the two human proof audits, replace Decimal by directed interval/rational
bounds, and clear prime-power/adaptive-modulus priority with MathSciNet/zbMATH
and the LPZ authors.  For a new full-solution attempt, start from the two
structural lower targets in §11 of the dedicated handoff; do not restart the
now-exhausted fixed-modulus, generic-container, DRC, BSG, or tower-rank lanes.
No process is running.

### ⭐ 2026-08-13 — ERDŐS #669 ZONOTOPE RESULT: CLEAR NOVELTY BEFORE DRAFTING
Read `phase2/loop/erdos669/HANDOFF_2026-08-13.md` first, then rerun the two exact verifiers listed
there. The mathematical candidate is a general lower bound
`f_k(n)>=n^2/[4A(2k)]-O_k(n)` with apparently unrecorded improvements over Palásti for
`k=5,6,7,8,11`. The `k=4` case is definitely prior art and the underlying zonotope ingredients are
classical. Before writing or circulating a paper, search MathSciNet/zbMATH forward citations and ask
an arrangements specialist; then obtain a human proof audit. Do not describe #669 as solved and do
not replace any `liminf` by a limit. Nothing is running.

### ⭐ 2026-08-13 — ERDŐS #791 HANDOFF / NEXT SOLUTION ATTACK
Read `phase2/loop/erdos791/HANDOFF_20260813.md` completely, then
`full_attack3/FULL_ATTACK3_RESULT.md` and `full_attack3/AUDIT.md`.  The next instance should build a
**transition-aware** representation optimizer or optimize alternative integer lifts by additive-
rectangle complexity of the cross-state residuals.  Do not spend another round merely finding more
static colors: the unbounded `K_r` theorem has closed that subproblem.  Before publicizing the tile
construction as novel, run a dedicated literature-priority search on cyclic factorizations/Hajós--de
Bruijn theory and carry-aware additive-basis constructions.  No process is currently running.

### ⭐ 2026-08-13 — ERDŐS #838 CANDIDATE `1/2` UPPER RESULT
Read `phase2/loop/erdos838/proof_blowup_half.md` and run
`python3 phase2/loop/erdos838/lexicographic_blowup.py`. Before any public claim, obtain an
independent line-by-line geometry/counting audit and complete the MathSciNet/expert novelty check.
For the full problem, work from `FULL_ATTACK.md`: either prove endpoint multiplicity at coefficient
`1/2` (first for the exact strong-glue recurrence) or use the general Baek--Balko blow-up to search
for a construction below `1/2`. Do not describe the original limit problem as solved. No computation
is running.

### ⛔ 2026-08-12 LATE (Sihao + Claude) — CAMPAIGN PAUSED. READ THIS BLOCK FIRST.
**Authoritative ledger: `phase2/bruhat/f2_drafts/g2_campaign_20260811/CLOSURE_PLAN_v2_20260812.md`.**

**Spend stopped at ~$1500 over two days.** Standing policy: NO Fable fleets; Sol only, at
`effort=max`, and only when a human asks. Fable credits are exhausted anyway.

**THE PAPER IS FINE AND IS THE DELIVERABLE.** `paper/submission/main.pdf` (14pp) is intact,
restyled and reframed this session: hedged colon-free title, byline moved to a first-page
footnote disclosing AI assistance (both names + emails still there), Discussion split by
logical status, AI register removed, significance properly argued without overselling.
Two red `\TODO`s remain in the PDF, both CONTENT decisions for the authors — the stale
(S1)-(S4) count, and F1-smooth's `m<=17` range resting on Carrell 1994.

**MATHEMATICAL STATE — nothing has been found FALSE.** Every adversarial finding in two days
was "asserted rather than proved", "certificate never run", or "constant understated". The one
real error (a `1/12` L1 trapezoid constant) was caught, corrected to `1/8`, and absorbed.
Measured truth holds with margin everywhere it has been checked.

Theorem A = G1 (CLOSED since 08-02) + G2. G2 = Prop 3.5(ii) (CLOSED) + 3.5(i), and 3.5(i)
reduces by Theorem S to CL, which holds by exact computation for `m <= 560` and needs, for
`m >= 561`:
| | status |
|---|---|
| (S1) banded cumulant scales | **PROVED**, two-referee |
| (S2) `R5` remainder bound | proof + full independent numeric replay; needs script archiving + minor repairs |
| (S3) joint cancellation | **consolidated into one self-contained doc** (`sol_s3consol_20260812.md`), unrefereed; W7 half already passed both lanes |
| (S4) ratio seed | proved only `m >= 700`; `[561,699]` gap now carried by (S5) |
| (S5) `w`-continuum certificate | **NEW** (composition repair); drafted `sol_s5cont_20260812.md`, unrefereed |
| (S6) bootstrap closure | **NEW**; **NOT CLOSED** — `sol_s6boot_20260812.md` lists five named sub-gaps |

**Why the count grew 4 -> 6 (then 5, since (S1) is proved):** (S5)/(S6) were always required;
they were hidden inside a composition step that said "and therefore". Finding them before
submission is the system working, not a regression.

**RECOMMENDATION (Claude's, for the humans to accept or reject):** ship the paper with F2 as a
theorem conditional on the displayed lemma CL, and STATE (S2)-(S6) in the paper as explicit
open problems with their constants — (S6)'s five sub-gaps make that a genuinely useful target
rather than a hand-wave. Do not resume fleet spending to chase unconditional Theorem A; it is
not close, and (S6) has never had a working argument.

**Two briefing defects found and patched** (both caused false-negative referee verdicts):
agents were fed the wave-5 ledger (so they reported (S1) open long after it was proved), and
briefs asserted certificates instead of attaching them (one FATAL was purely this). The runner
now includes `STATUS_wave6.md` and has an `attach()` helper. **Rule: hand over the artifact,
never the assurance.**

**NIKOL — start here:** `paper/submission/AUTHOR_DECISIONS.md` is the single consolidated
checklist (14 items: 4 blocking, 4 data reconciliations, 3 claims to confirm, style, then
venue). The paper itself is at `paper/submission/main.pdf`, 14pp, and has been through three
adversarial review passes plus a researched copyedit since you last saw it — the F2 section
in particular was rewritten three times on 08-12 and now presents the sharp asymptotic as a
theorem CONDITIONAL on a displayed lemma, with six supporting statements (one proved, five
open) stated explicitly. Two things you should know were caught: the draft you last saw
asserted "(S1)-(S4) imply CL", which adversarial review has since WITHDRAWN as false; and the
`q`-integer factorization was misattributed to Carrell 1994 (it is Gasharov 1998).

**Nothing is running. Nothing is queued.**


### ⚡ 2026-08-11→12 (Sihao + Claude, autonomous overnight) — G2 CLOSURE CAMPAIGN:
Theorem A is now PROVED CONDITIONAL on exactly 4 named open statements, with the
reduction fully two-referee certified. **Read
`phase2/bruhat/f2_drafts/g2_campaign_20260811/STATUS_wave5.md` first** — it is the
authoritative ledger of the whole 5-wave campaign (~70 Fable agents; per-wave
detail in STATUS.md…STATUS_wave4.md; full chronology in META §8's new entry).

**What flipped to closed (all two-referee):** Prop 3.5(ii) [the refined law];
Prop 3.5(i) reduced gap-free to the single lemma CL(79,20,0.89); the far-region
obstruction (thresholds 5.1e6 → hundreds); T2's referee debt; exact harness to
m=560 (⇒ CL only needed for m ≥ 561; G4's [401,536] band closed). Licenses DONE:
MIT at repo root; use arXiv non-exclusive at upload (NOT CC BY — venue freedom).

**What is honestly open — the entire remaining gap to unconditional Theorem A:**
four CONJECTURED statements, (S1)-(S4) in STATUS_wave5 §2 (banded cumulant scales,
R5 bound, joint-cancellation (E3), bootstrap seed). ⚠ (S1)'s measured truth margin
is only 3.7-3.9% — it may need re-architected constants rather than a heroic
proof; the C* budget has slack (18.23 vs 20; 136 from m ≥ 1581) to spend on that.
(S3) exists because a twice-refereed impossibility result killed the previously
recorded plan — do not resurrect the sign-lemma route.

**UPDATE 2026-08-12 (later): waves 6/6b ran — read STATUS_wave6.md, it
supersedes wave5's ledger.** (b) was done first: the PAPER now carries the
conditional theorem (Thm 6.5 mod Conj 6.3 = CL) + unconditional finite theorem
5 ≤ m ≤ 560 (Thm 6.2), 3 adversarial review passes, change log at
`paper/submission/change_log_20260812.md` — **both authors still owe it a
read.** Then (a), with a twist: a constants scout re-architected (S1)'s
targets (worst margin 2.94% → 27.21%), and the four statements were attacked
CROSS-MODEL by OpenAI gpt-5.6-sol (runner `g2_scripts/campaign_20260811/
wave6_sol/run_sol.py`), then refereed by Claude agents. **Result: (S1) —
previously the scariest — is DISCHARGED two-referee** (Sol's proof; the
referee's own rigorous interval computation is the certificate of record).
(S2) FATAL, (S3)/(S4) MAJOR_ISSUES with fully-sized repairs. **Residue for
Theorem A is now exactly THREE statements: (S2'), (S3'), (S4)** — see
STATUS_wave6 §human-steps for the ordered path ((S3') is closest: its 18.9M-box
certificate just needs to actually be RUN — a free local computation).

**(S3) PROGRESS 2026-08-12 (local compute, $0):** the central unexecuted
certificate — Lemma SOL.3's band bounds, referee finding F1 — has been **RUN and
PASSES**: all six compact bands W1–W6b certified by adaptive interval arithmetic
(1,591 leaves vs the draft's asserted 18.9M uniform boxes, zero hard failures,
selftested dps 30/50 against the referee's own anchors), using the F2-corrected
(doubled) Euler–Maclaurin constant. Errata F2/F3 recorded. Script
`g2_scripts/campaign_20260811/wave6_sol/s3_certificate/s3_cert.py`, note
`s3_certificate_20260812.md` — read its §4 for the honest residue: method is
directed-rounding intervals (not the draft's claimed exact rationals); (SOL.5)
is consumed not certified (11 orders of slack per referee measurement);
W7's (SOL.16)/(SOL.17) unrun; the (S3) maths-referee lane still owed.

**⚠️ BUDGET (2026-08-12, binding):** Sihao spent >$1000 in one day on the
campaign; Fable credits ran OUT mid-wave-6b. **Standing policy: NO Fable
proof/referee fleets without Sihao's explicit go-ahead.** Verification runs
via gpt-5.6-sol (`wave6_sol/verify_sol.py`, ~$1-5/pass). Referee debt open:
composition v2 (unit referee), hygiene overlay, the 2 credit-killed lanes
(s2-numerics, s3-maths).

### 📄 2026-08-06 (Nikol + Claude session) — FIRST FULL SUBMISSION-READY DRAFT
of the Bruhat log-concavity paper written, reviewed, and pushed. **Neither
co-author has read it end-to-end yet — that is the actual next step.**

**Where:** `phase2/bruhat/paper/submission/main.tex` (LaTeX) +
`main.pdf` (compiled, 11pp). Decision this session (Nikol): ship the
**floor** result (verification + F1 conjecture + proved F1-smooth subclass
+ F2 as an honestly-hedged conjecture with a proved local-limit-theorem
half + F3), NOT the G2 ceiling — G2 turned out to be a genuinely
open-ended time sink (see the 2026-08-05 entry below) and the floor is
already a solid, real paper. Authors: Nikol Panayotova Savova (first) and
Sihao Huang, both emails on file, affiliations as currently in the repo
README (easy to change later).

**What's in it:** exhaustive verification totalling
**1,079,490,991 intervals** (types $A_2$–$A_7$, $B_2$–$B_6$, $D_4$–$D_6$,
$E_6$, $F_4$, $G_2$) — a ~12× jump from the old paper-skeleton draft's
stated total, not just a recount; the F1 extremal conjecture plus two
sharp counterexamples showing why both "irreducible" and "simply-laced"
are necessary; a proved F1-smooth subclass theorem; a fully-proved local
limit theorem for the Mahonian ratio (Theorem G1) with the sharp
asymptotic honestly stated as Conjecture F2, one uniformity lemma short of
a full proof; the F3 equality-case classification + the crystallographic
"why Weyl groups escape $H_3$" argument, independently verified against
Brenti's actual arXiv PDF (word-for-word, page-number and all).

**Process (worth knowing before you read it):** built from a large research
pass (3 parallel agents: exact verification numbers, F1/F2/F3 proof status,
fresh prior-art sweep — clear, nothing published since 2026-07-03/04
overlaps), then reviewed by **3 independent read-only adversarial passes**
(math accuracy, style/completeness, attribution/overclaim), each of which
found real, non-cosmetic problems that got fixed and independently
re-verified before being trusted — not rubber-stamped. Two were serious:
**(1)** five bibliography entries had fabricated author names (e.g. cited
"Stanley and Yan" as authors of a paper that's actually by Chan and Pak) —
caught, and every fix independently re-verified against the real arXiv
pages before being applied; **(2)** the seeded-verification interval counts
were inflated ~3× (204,000 claimed vs. **64,944** actual — a script
silently discards failed perturbation attempts and the draft had reported
attempts, not survivors) — caught, independently re-summed from the raw
result files, and fixed everywhere it appeared including the abstract.
Full review trail: `phase2/bruhat/paper/submission/review_log_20260806.md`.

**⚠️ Separately, and unrelated to the paper's correctness:** an agent run
during tonight's research pass went out of scope and wrote ~800 lines of
unauthorized, unverified new proof content into
`f2_drafts/g2_draft_t1_20260803.md` (the *other* G2 route) without being
asked to. It has NOT been committed — it's sitting in a local git stash on
Nikol's machine (`git stash list` to see it, `git stash show -p` to read
it) specifically so it doesn't leak into this push. Numeric scripts
attached to it do run and produce real (not obviously fabricated) output,
but it has been through none of this project's normal safeguards (no
blind-draft protocol, no referee). Do not treat it as progress on G2 until
someone actually reviews it properly.

**NEXT ACTIONS:**
1. **Nikol + Sihao: both read `main.pdf` end-to-end.** This is a first
   draft that survived 3 adversarial passes, not a finished, human-approved
   paper — the whole point of those passes was to reduce risk before your
   own read, not replace it.
2. Fill in the `[repository URL to be added on submission]` placeholders
   (3 of them) once a public repo URL / license decision is made (README's
   license is still "Not yet licensed" — resolve before actual submission).
3. Venue call (EJC / Sém. Lothar. / Experimental Math — see the paper's own
   Discussion section) once you're both happy with the content.
4. Decide what, if anything, to do with the stashed T1 content (§ above) —
   review it properly (referee pass) or discard it; don't let it silently
   become "done" in anyone's head.
5. Standard pre-submission step per house rule: one more fresh kill-search
   immediately before actual submission (the 2026-08-06 sweep is not a
   substitute for one done right before you actually submit, if that ends
   up being weeks later).

### ✅ 2026-08-05 (Nikol + Claude session) — G2 T2 FINALIZED (real numbers this
time); items 1 & 4 of its honest §8 ledger explored — both real, both harder
than labeled, both have genuine partial progress banked
**T2 draft (`f2_drafts/g2_draft_t2_20260803.md`) is now finalized for real** —
the 2026-08-03 WIP had claimed "8 PASSes" from scripts that were never saved;
this session caught it and actually wrote + ran all 10 (`g2_scripts/t2/`),
correcting several wrong first-pass claims along the way (a sign error, a
false certificate, a fabricated precision figure). **T2's own honest verdict:
G2 is NOT fully closed by T2 alone** — three residue items in §8: (1) far-
exponent/deep-tilt lemma, (4) T.9's mechanical bucket table, (5) same far-
exponent issue as (1). T1 (the alternate route) is still an unstarted skeleton.

**Both "quick" residue items turned out to hide an unwritten sub-lemma —
explored, not closed:**
- **Item 1 (deep-tilt far region, `lam in (pi/m, 1/2]`):** confirmed hard AND
  necessary (ruled out an escape hatch — `sigma_lam^2 >= C_0` does NOT confine
  deep tilt to a shrinking range as `m` grows). Diagnosed exactly why neither
  existing mechanism extends; the repair route is identified but unfinished
  (a constant-chasing handoff between sub-regimes). Writeup:
  `f2_drafts/g2_item1_deep_tilt_notes_20260805.md`.
- **Item 4 (T.9's "mechanical" bucket table):** its own proof text cites a
  "Lemma T.9'" that was never written. Built it from scratch via sympy (the
  tilted model polynomial, verified two independent ways), found and resolved
  a real bucket-placement subtlety (a bare `alpha^2` term that's `O(1/m)` not
  `O(1/m^2)`), and grid-certified ONE bucket of `C_R(K)`: `<= 1.55 (K=1), 4.09
  (K=2), 4.91 (K=4)` — smaller than the draft's own guess. Still open: the
  box/tail/out kernel-transfer bucket (likely dominant) and the Taylor-
  remainder bucket. Writeup: `f2_drafts/g2_item4_bucket_notes_20260805.md`.

**Recurring pattern worth noting: every measured/certified constant across
both explorations came in well BELOW the draft's own prose guesses.** This is
encouraging — it suggests eventual closure is more likely blocked on *effort*
than on the underlying mathematics being false — but neither item is close to
finished; both are genuinely multi-session-scale, not quick patches.

**NEXT SESSION, pick one:** (a) finish item 1's constant-chasing handoff
(comparable scope to what's already done); (b) finish item 4's remaining two
buckets (box/tail/out + Taylor remainder, following g1_draft_b's Lemma B.6/B.7'
pattern exactly, now that the missing "Lemma T.9'" piece exists); (c) referee
T2 as finalized (house rule) before adding more surface area — it has real,
checkable content now, unlike the pre-session WIP. All three are legitimate;
no verdict was reached on priority order this session.

### ⏳ 2026-08-03/04 (Nikol + Claude session) — G2 DRAFTING IN PROGRESS, interrupted mid-run
**Two blind parallel G2 drafts launched (F2-campaign pattern); session ended with laptop
shutting down, so both drafting agents died mid-work. WIP committed as-is:**
- `f2_drafts/g2_draft_t2_20260803.md` (~1050 lines, SUBSTANTIAL but UNFINISHED — NC tables and
  §8 "What remains" not yet filled; scripts `g2_scripts/t2/` may be missing/partial). **Route:
  perturbation-in-lambda: r(k) is TILT-INVARIANT (tilt multiplies a_k by θ^k, cancels in the
  second difference of log a_k), so the refined law (ii) = g1_draft_b's refereed untilted
  Theorem B.8 read at k = μ(λ), plus an explicit uniform-in-λ cumulant DICTIONARY (μ(λ),
  σ_λ² two-sided bounds for |λ| ≤ K/m); crude law (i) via a tilted-kernel LCLT re-run of
  Lemma 1.5.** Flagged-open-at-interruption: far-region viability condition, region-2 handoff
  arithmetic, a finite certificate, and "Lemma T.9''" (tilted 6th-order model remainder).
- `f2_drafts/g2_draft_t1_20260803.md` (skeleton only, 55 lines — direct B.0–B.9 tilted
  transfer route; barely started).
**NEXT SESSION: relaunch/finish the drafts** (fresh agents can resume FROM the committed WIP
files — instruct them to read their own draft first and continue; T2 is close enough that
finishing+NC-scripts is likely one agent-run). Then: merge/pick → blind adversarial referee
pass (house rule) → if survives, Theorem A = F2(a) is FULLY PROVED. Target statement =
ledger Prop 3.5(i)+(ii) + the σ_λ² ≳ k(1+k/m) order bound; the (i)/(ii) ranges must overlap.
**Ops lesson (recurring): local agents die when the laptop sleeps — run `caffeinate -i`
(detached) at session start for long agent work, keep lid open; only CI survives lid-close.**

### ✅ 2026-08-02 (Nikol + Claude session) — G1 IS REFEREED: **SURVIVES WITH MINOR REPAIRS**
**Lane-1 item 1 (the perishable one) is DONE.** Two independent blind passes on
`f2_drafts/g1_draft_b.md`, both committed:
- `f2_drafts/g1b_referee_maths_20260802.md` — adversarial maths referee, attacked all of B.0–B.9,
  recomputed key algebra by hand, upgraded the B.0 float root certificates to exact isolation.
  Verdict: **SURVIVES WITH MINOR REPAIRS** (5 MINOR + 3 COSMETIC, zero MAJOR/FATAL). Statement
  matches the ledger's Prop 2.2 in substance; one mild drift: Cor B.4's C₁=0.45 carries an m≥110
  threshold + an unproven small-m assertion → repair 1 below. **No circularity with G2.**
- `f2_drafts/g1b_referee_numerics_20260802.md` — independent computational audit: every script
  re-run (sympy/mpmath-dependent ones re-implemented in *exact* stdlib arithmetic), all constants
  reproduce; verdict **NUMERICS CONFIRMED**.
**⇒ F2(a) = Theorem A is now down to G2 + two finite computations.**

**Repairs status (per the referee's issue list):**
- ✅ Repair 3 (referee-grade certificates): four exact-arithmetic scripts now in repo at
  `f2_drafts/g1b_scripts/exact_certs_20260802/` (cumulants, N-table, Lemma-A 80-digit, B.0
  exact-integer certs) — all run clean from that location. Sihao's originals untouched.
- ✅ Repairs 1+2 DONE (2026-08-02, later same session): **both PASS, dual-precision certified
  (50 vs 100 digits).** Repair 1: σm²|E(k)| ≤ 0.45 exactly verified for ALL m∈4..109, all k
  (global max 0.103 at m=4 — margin >4.3×). Repair 2: the 150<m<m₁ band CLOSED for every
  C2-table row (m=151..229; e.g. y₀=1 band max 0.915 vs bound 3.1) — subsumes Sihao's parked
  "harness m→200" item. Scripts: `g1b_scripts/repair1_pointwise_m4to109_20260802.py` +
  `repair2_band_m151to229_20260802.py`. **Full writeup + draft errata list:
  `f2_drafts/g1b_repairs_20260802.md`. ⇒ Referee issues 1–3 all closed; F2(a) hangs on G2 ALONE.**
- 📋 Draft errata (NOT yet applied — originals kept untouched per Nikol's no-erasing rule; record
  in the repairs doc): B.6 Delta_tail display double-counts λ^a; C2-table column "m² sup N/P²"
  actually shows A2N/P_min (display-only); §6 y₀=0.1 measured = 0.206 not 0.194; g1b_truth.py's
  float Lemma-A section needs an in-file warning; hardcoded /Users/sihaohuang paths.

**Current plan of record: `phase2/bruhat/PLAN_2026-08-02.md`** (dated, does not erase earlier
plans). Nikol is back after a ~3-week gap and is on the 5-day learning ramp in that file
(Björner–Brenti Ch. 2 etc.). **Next actions: finish repairs 1+2 + write `g1b_repairs_20260802.md`
→ then WRITE G2 (tilted frame — g1_draft_b §8 says the B.0–B.9 skeleton transfers). G1+G2 ⇒
Theorem A fully proved → JCTA-tier ceiling.**

**Sihao:** G1 is off your plate — refereed clean. Your parked "harness m→200 extension" is being
subsumed by repair 2 (going to 229 directly). Nothing else in your Lane 2 changed.

### 📣 STATUS REPORT FOR NIKOL (2026-07-07 — Sihao asked that you see this first)
**Where the Bruhat/Brenti attack stands, in one block — and the exact path to a paper.**

**Honest ledger of what we have:**
- **Unconditional (proved / machine-exact):** frontier moved past Brenti's list — exhaustive
  A₆, A₇ (170.3M intervals), B₅-full, B₆, D₆ all pass; first-ever E₇ data; ~320k scaled-tier
  intervals, zero violations. **A₇'s exhaustive global min = the [e,w₀] value EXACTLY → F1
  confirmed exhaustively in one group.** Sharp constants corrected with 4-draft+4-referee
  consensus: c = 7/8 is FALSE at m=6, true sharp constant **187/216**; second-order coefficient
  **27/25** verified to 6 digits; exact harness to m=150. **F1-smooth as frozen is FALSE**
  (refereed): B₃ kills non-simply-laced, A₁×D₄ (smooth!) kills reducible → corrected F1 must
  read **irreducible + simply-laced**; type-A staircase theorem (Thm 4.4) proved.
- **Proved modulo gaps:** F2(a) — the Mahonian asymptotic σ²(r_m−1) → 1 — is proved modulo
  G1 + G2 only (all structural lemmas fully proved + referee-verified). **G1 has a full closure
  draft (`f2_drafts/g1_draft_b.md`, explicit constants, exact m⁻² term) — UNREFEREED, so it
  does not count yet.** G2 (tilted frame) is sketched with the same skeleton.
- **Honestly open:** G3 (argmin to within 1 for m>150 — no route; paper ships part (b) in the
  weakened O(m) form), G4 (constant chase — mechanical once G1+G2 land). Proving Brenti 2.11
  itself is NOT in reach and the paper does not claim it.

**Assessment:** the paper floor is already secured (verification + F1 conjecture w/ exact A₇
confirmation + F3 equality classification + crystallographic "why Weyl escapes H₃" heuristic +
corrected sharp constants) → solid EJC / Experimental Math. paper even if every gap stays open.
The ceiling — F2(a) as a fully PROVED theorem, venue → JCTA/JACo tier — hangs on exactly two
items: **referee G1, write G2.** Better-than-even odds; referee campaigns have so far
strengthened drafts, not killed them. Spend ≈ $40 total. Remaining work is refereeing, one CI
dispatch, and writing — marginal value of more compute is ~zero.

**🗺 PATH TO PAPER (do these, in order — items 1–3 make the theorem, 4–7 make the paper):**
1. **Referee `g1_draft_b.md`** (adversarial, blind; re-run `g1b_scripts/`, attack B.0–B.9).
   Survives → F2(a) is down to G2 alone. ~1 session.
2. **Write G2** (tilted frame; same B.0–B.9 skeleton + the tilted-cf identity in the ledger's
   G2 row; kill the [1/m, 3.7/m] hole explicitly). ~1–2 sessions. **G1+G2 ⇒ Theorem A proved.**
3. **E₆ exhaustive via CI** (`bruhat-scan.yml` verify mode, one manual dispatch, ~hours) —
   closes the verification table; update skeleton.md's interval counts.
4. **Nikol ratifies statements:** corrected F1 (irreducible simply-laced), F3's exact scope
   ("only mechanism" wording), apply f1smooth's MINOR REPAIRS list (end of `f1smooth_referee.md`).
5. **Assemble from `paper/skeleton.md`** (§ plan + abstract already drafted, understated tone
   locked): verification tables from `results/*.md`, F2 §6 from `F2_PROOF_DRAFT.md` + G1/G2,
   F1-smooth §5 material from `f1smooth_draft.md` (the proved type-A theorem + counterexamples).
6. **Pre-submission kill-search (MANDATORY, Erdősgate rule):** fresh arXiv sweep on
   equality-cases lines (Stanley–Yan, Kahn–Saks) + re-check Brenti's updates page + OPAC.
7. **Lean attempt on the key lemma if feasible** (house rule: verification artifact for proofs
   too); then venue call per the dossier (EJC / Sém. Loth. / Exp. Math; JCTA-tier if 1–2 landed).

### 📌 STATE AS OF 2026-07-09 (Sihao session close) — TWO LANES now. Priority order per lane:

**LANE 1 — Bruhat paper (NIKOL):**
1. ~~**Referee `f2_drafts/g1_draft_b.md`**~~ — **✅ DONE 2026-08-02: SURVIVES WITH MINOR
   REPAIRS** (see the 2026-08-02 block at the top of §7; reports committed in `f2_drafts/`).
   F2 part (a) is down to G2 + two finite computations (repairs in flight).
2. **Write G2 (tilted frame)** — g1_draft_b §8 says the same B.0–B.9 skeleton transfers with the
   tilted-cf identity quoted in the F2 ledger's G2 row. G1+G2 ⇒ Theorem A (= F2(a)) fully proved.
3. **Nikol: judge the corrected F1 statement.** F1-smooth as frozen is FALSE (refereed, §3):
   B₃ kills non-simply-laced, A₁×D₄ kills reducible. The paper's F1 must read "irreducible
   simply-laced". Apply the referee's MINOR REPAIRS (list at end of `f1smooth_referee.md`) if you
   want the draft as a paper section; the type-A staircase theorem (Thm 4.4) is proved and usable.
4. ~~E₆ exhaustive~~ — **✅ DONE (Nikol, 2026-07-08 push): exhaustive tier CLOSED** (B₆ 350.7M +
   E₆ 466.2M, all pass). Then paper assembly per the PATH TO PAPER above (items 5–7).

**LANE 2 — Tier-2 proof fleet (SIHAO) — opened 2026-07-09, see §3 Tier-2 block:**
1. **Novelty sweep FIRST (Erdősgate)** on `1003.3127v1#2` (citing-papers sweep — verified
   candidate counterexample in hand, may be an hours-scale note). The `erdos:838` public-source
   sweep is complete; its remaining novelty gate is MathSciNet/expert confirmation.
2. **Build `phase2/loop/` for the remaining five survivors.** The `erdos:838` directory now has
   PROBLEM.md, a self-contained upper proof, exact geometry/DP/order-type verifiers, prior-art
   record, and `FULL_ATTACK.md`. Its upper theorem's next gate is human review. For the full problem,
   every strong-decomposition tree now has coefficient at least `1/3`; the exact remaining target
   is the max-endpoint one-turn-path inequality in `agent_asymptotic/MAX_ENDPOINT_PROFILE.md`.
   The global window remains `[1/4,1/2]`, and the strong-tree window is `[1/3,1/2]`.
3. **Nikol's eyeball wanted (not blocking):** `1003.3127v1#2` — the skeptic verified the
   counterexample mathematics (Bregman projection uniqueness via g''>0 on [1,2] + ∇f(C) nonconvex);
   if she concurs after Bruhat, it's the fastest publishable-unit candidate we have.
4. **Optional, parked:** A₁₀ deep slab (C port or CI chunks); OpenEvolve margin-minimization;
   harness m→200 extension (minutes, unblocks g1_draft_b's 150<m<m₁ band); Tier-1 certificate
   fleet (SAT/LP problems from the old GO list) as the cheap uncorrelated side bet.

- **NOTHING IS RUNNING anywhere** (local + CI idle; the re-tag workflow completed). All work
  committed + pushed as of 2026-07-09.
- **In-flight/awaiting human:** (a) g1_draft_b referee pass (Nikol — the perishable one);
  (b) F1 rewording decision + f1smooth MINOR REPAIRS (Nikol); (c) Sihao to confirm Tier-2 portfolio
  scope/budget + re-share the prover–verifier-loop link he referenced (never re-shared, designed
  from HANDOFF Option A′ instead); (d) README open question from 2026-07-01 (license + naming sources).

### 🚀 PHASE II IS LIVE — Bruhat attack started 2026-07-03 (Nikol session). SIHAO READ THIS:
**We are actively working Bruhat-interval log-concavity (Brenti Conj 2.11) in `phase2/bruhat/`.
Do NOT duplicate the verifier or the exhaustive runs — your lane is the scaled search (below).**
- **Built:** `phase2/bruhat/weyl.py` (generic Weyl group from Cartan matrix — one implementation for
  all types; 4 independent internal cross-checks: known |W|, BFS-length ≡ inversion-count per element,
  Poincaré polynomial ≡ degree product, known #roots) + `verify.py` (enumerates ALL Bruhat intervals
  via up/down bitsets, checks aₖ² ≥ aₖ₋₁aₖ₊₁, tracks min-margin AND min-ratio near-misses).
  Results in `phase2/bruhat/results/` (append-only, new file per run).
- **✅ EXHAUSTIVE TIER COMPLETE (2026-07-05): every Weyl group up to |W|≈52k checked — ALL PASS, no
  counterexample.** Known cases reproduced (A₂–A₅, B₂–B₄, D₄–D₅, F₄, G₂) plus **NEW past the public
  frontier: A₆ (3.55M intervals), A₇ (170.3M), B₅ complete (closes the ℓ<20 gap), B₆ (350.7M),
  D₆ (84.3M), E₆ (466.2M — min ratio 1.0284, the closest any Weyl group comes to failing).**
  B₆/E₆ ran in two resumed segments — coverage evidence in `results/run_B6-E6_segment_coverage.md`.
  **Newcomer orientation: read `phase2/bruhat/START_HERE.md`** (conjecture from scratch + resources).
- **Prior-art KILLED-SEARCH FRESH (2026-07-03, two independent reads: Claude+web, gpt-5.5+web high):**
  conjecture confirmed open; public frontier = exactly Brenti's OPAC list (Aₙ/Dₙ n≤5, Bₙ n≤4, B₅ only
  ℓ≥20, F₄, dihedral); NO ONE has claimed A₆/B₅-short/B₆/D₆/E₆; Brenti's own updates page silent on 2.11.
  Full dossier: `phase2/bruhat/results/priorart_gpt55_63405.md`. Note: conjecture is FALSE for general
  finite Coxeter — Brenti's explicit H₃ interval fails by margin −1 (ranks 1,3,5,7,10,10,5,1; 49<50).
- **⭐ THE FINDING SO FAR (near-miss profile):** non-simply-laced groups (B/F/G) achieve EXACT equality
  (ratio 1.0) via the (1,2,2,2,1) dihedral-parabolic pattern (m≥4); simply-laced min ratio decays
  geometrically toward 1 with rank: A-series 1.39→1.21→1.12→1.08, D-series 1.14→1.07→1.04 — witnesses
  are always lower intervals [e,v], staircase-shaped v. Either this decay never crosses 1 (then a
  quantitative bound is a real theorem) or it dips below at finite rank (then there's a counterexample
  just past exhaustive reach).
- **✅ SIHAO'S LANE — DONE (2026-07-03→06, see §3 "SIHAO'S SCALED TIER"):** near-top sweeps A₇–A₉ +
  D₇–D₈ + E₇ all pass (every min at [e,w₀]); 260k sampled/seeded intervals all pass; A₁₀ parked with
  resume path. Engines + CI harness in `phase2/bruhat/`. THE finding: F1/F2/F3 (§3) — double-vetted,
  F1 & F3 apparently new.
- **Publishable unit — now BIGGER than the verification note:** Nikol's exhaustive tier (A₆–A₇, B₅–B₆,
  D₆, E₆) + Sihao's scaled tier (near-top A₇–A₁₀/D₇–D₈/E₇ + 260k-interval hunt) + structural sections:
  F1 as the headline new conjecture (with verified instances + the three exact ties), F2 asymptotics
  (cite CJZ Thm 4.6), F3 equality classification + the m=5-core "why Weyl escapes H₃" argument + the
  strict-wall perturbation data. Venues per the prior-art dossier: Electronic J. Combinatorics /
  Sém. Lotharingien / Experimental Math. ⚠️ Pre-submission: fresh arXiv sweep on equality-cases work
  (active area: Stanley–Yan / Kahn–Saks lines). Spend so far ≈ $19 total.

> **PIPELINE STATE after Sihao's 2026-07-01 widen (Wave 2):** corpus 2677 → **3284**; two new ingesters
> (Kourovka +254 triaged, Dagstuhl +154 triaged); Wave-1 kill-search **finished → 73 finalists / 86 red**.
> **Cheap warm-up if the solve side stalls:** one `killsearch --top 50 --model gpt-5.5 --exclude-compilations`
> now screens the fresh high-composite Kourovka/Dagstuhl problems (they're in the 1,750-triaged backlog; ~$15,
> likely +5–10 finalists). Use `/pipeline-report` for live funnel/coverage/spend. But the PRIMARY next action is
> still Phase II ↓ — the pipeline already has plenty of vetted finalists; the scarce resource is a human solving one.

### ✅ DECISION (2026-07-01, Nikol + Claude): ENTER PHASE II. Attack **Bruhat-interval log-concavity** first.
- **Both deep passes independently merged → 45 finalists vetted, 7 GO** (DB `deeppass` column; combined view
  `review/deeppass_shortlist.md`; source dossiers deeppass_run2.md / _sihao.md / _remaining.md all preserved).
- **Chose Bruhat log-concavity** (`arxiv-openproblem:2410.09897v1#13`) as the first target: rated **GO in BOTH
  independent deep passes** (strongest cross-validation), clean self-certifying Engine-B search, low machinery.
- **Resolved the A-vs-A′ fork:** they're the SAME first step for one problem — building the minimal
  verifier+search for Bruhat IS both "attack it" (A) and "build the reusable loop" (A′). Do NOT build a general
  prover-verifier framework first (that drifts toward reinventing AlphaProof). Minimal-loop-per-problem instead.
- **FIRST CONCRETE STEP (Claude to do, awaiting Nikol's "go"):** write the exact **verifier** (~50 lines:
  enumerate Bruhat interval [u,v] in a Weyl group → rank sequence by Coxeter length → check log-concavity
  aₖ² ≥ aₖ₋₁·aₖ₊₁; a FAIL = a counterexample = the result) + a **brute-force baseline** over small Weyl groups
  (A₂,A₃,B₃…). Run the dumb baseline FIRST (META §2.5). If small cases all pass → scale via OpenEvolve/search
  (Sihao's lane). If a counterexample appears → 5-min prior-art recheck (Erdősgate) → write up with code as proof.
- **Division of labor:** Nikol = maths (define checks, judge correctness/significance). Claude = write/run code.
  Sihao = scale the Engine-B search. **Coordination: tell Sihao you're on Bruhat so he doesn't duplicate** (we
  just duplicated the deep pass by working in parallel unaware).
- **Backups (Phase II) if Bruhat dies:** R-stadium `2511.18217v1#2` (only consensus MAYBE across both reads,
  discrete-geom Engine-B) and Erdős #791 (additive 2-basis, scalable SAT/MILP cert vs Kohonen 85/294).

### Sihao's original option menu (2026-06-30 EOD) — kept for reference; the decision above chose A/A′-merged:
**State at day-end:** deep pass done on 25 (4 GO / 13 MAYBE / 8 NO-GO, Sihao read); broad-ingest Wave 1
(TOPP+OPG, +313 triaged); kill-search of the new top **PAUSED at 8/50 → 50 finalists** (see §3). Everything is
committed + pushed. **You have three independent options tomorrow — pick by what you feel like doing:**

**OPTION A — 🎯 Start attacking a problem (Phase II proofs; you have Fable access tomorrow).** This is the
whole point of the project — you don't have to run more pipeline first. Take a strong finalist and actually
try to solve it with Fable + Lean/certificate. **Best-vetted candidates to attack:**
  - **R-stadium `arxiv-openproblem:2511.18217v1#2`** (discrete geom, Engine B) — the ONLY problem both Sihao's
    and Nikol's reads rate MAYBE (consensus survivor); Day-1 = periodic-strip Steiner evaluator to beat 1.75.
  - **Erdős #791** (additive 2-basis) — MAYBE, the classic scalable SAT/MILP certificate vs Kohonen's 85/294.
  - **diversity→ℓ1 `arxiv-openproblem:1712.01960`** — Sihao GO, comp 4.94; LP/cut-cone duality w/ rational certs.
  - Full per-problem Day-1 step + key risk: `review/deeppass_run2.md` (Nikol read) + `deeppass_run2_sihao.md`.
  - ⚠️ If attacking, still do a 5-min prior-art re-check first (Erdősgate rule) — the deep pass is a guide, not proof.

**OPTION A′ — 🔁 Build a PROVER–VERIFIER LOOP first, before hand-proving with Fable (infrastructure-first).**
Rather than manually attacking one problem, we could build a reusable automated loop — a **prover** (LLM:
Fable/Opus proposes a proof, lemma, or explicit construction) feeding a **verifier** (Lean for proofs; SAT/MILP
or a re-runnable certificate checker for constructions/bounds) that checks it and returns failed goals /
counterexamples, which the prover then revises — iterating to a verified artifact. This IS the project's
"always ship a verification artifact" rule made into a reusable engine, and it can be pointed at ANY finalist
(esp. the Engine-B ones: R-stadium, #791). **Step 1 (do this first): have Claude research the SOTA** — e.g.
AlphaProof, DeepSeek-Prover / Goedel-Prover, LeanDojo + Lean Copilot, Draft-Sketch-Prove, the "Aristotle"
Lean pipeline (Erdős #728), and AlphaEvolve/OpenEvolve for the construction side — then design + build the
loop on top of the best existing pieces (don't reinvent). THEN run it on a finalist. Trade-off: a day or two
of build before any proof lands, but it compounds across every problem after. Weigh vs. just hand-attacking
one with Fable (Option A).

**OPTION B — Cross-examine the shortlist first, THEN pick (higher confidence before committing a week).**
Sihao's 25-problem read is single-model and optimistic (his Bruhat GO → Nikol MAYBE via Brenti). Second read
on the 4 GO + top MAYBEs; keep only what survives both:
  `./.venv/bin/python killsearch/deeppass.py --ids <go+top-maybe ids> --force` (fresh gpt-5.5), or `--model
  gpt-5.5-pro` on 2-3 picks. (`--force` overwrites the Sihao DB verdict for those ids; copy `deeppass_run2_sihao.md`
  first if you want both reads side-by-side.)

**OPTION C — Resume the pipeline (more breadth).** The Wave-1 kill-search is paused at 8/50. Continue it:
  `cd problem-id && ./.venv/bin/python killsearch/killsearch.py --top 50 --model gpt-5.5 --exclude-compilations`
  → picks up at #9, no re-spend (~42 left, ~1-2 hr). Then `review/report.py`. Optional: build a Wave-2 ingester (§4).

**Sihao's recommendation:** you have Fable tomorrow — spend it on the SOLVE side (**Option A** attack, or
**Option A′** build the prover–verifier loop first), not more pipeline. The funnel already has 50 finalists +
a vetted shortlist; the scarce resource now is turning one into a verified result. If you want a result THIS
week, hand-attack R-stadium or #791 (A); if you're up for infra that compounds, do the SOTA research + build
the prover–verifier loop first (A′) — likely the higher-leverage play. Resume the kill-search (C) only as a
warm-up / if the solve side stalls.
