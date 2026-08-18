# META-GUIDE — An AI-Leveraged Run at a Novel, Publishable Math Result

> **Status:** living document — the single source of truth for *why* and *how* we work.
> **Maintainers:** Nikol (+ Sihao's profile). **Started:** 2026-06-23. **Rewritten:** 2026-06-24 (v2, AI-leveraged thesis).
> **Tooling in hand:** Claude Opus 4.8 · GPT-5.5-Pro / o-series · Lean 4 + autoformalizer (Aristotle-class) · search compute.
> **Win condition (1 week):** EITHER an arXiv-ready note (new bound / construction / counterexample, verified) OR a verified, logged contribution to a live open effort (e.g. an Erdős problem). Both count.

---

## Team

- **Nikol** — mathematics undergraduate at **Oxford**. Strong across **logic & set theory,
  algebraic number theory, Galois theory, graph theory, rings, topology, combinatorics, measure
  theory, and probability.** → Our **proof + problem-domain lead**: judges correctness, drives
  Engine A (the cross-domain lemma / proof-adaptation), owns problem selection in the amenable
  fields, and is the human verifier who catches the AI's "confidently wrong" steps (§3).
- **Sihao Huang** (sihao.c.huang@gmail.com) — **physics graduate, MIT**; solid in **ML, CS, and
  quantum information theory.** → Our **infrastructure + Engine B lead**: stands up and runs
  OpenEvolve / sampling baselines / SAT, builds evaluators, manages the model-orchestration and
  compute, and brings the QIT/ML angle for any quantum-information or ML-theory framing.

**What our backgrounds steer us toward (problem-selection implication).** The overlap of Nikol's
pure-math breadth and Sihao's ML/CS/QIT is widest in: **combinatorics & graph theory** (Engine B
constructions + Nikol's domain), **probability & measure theory** (the §2.6 *quantitative-extension*
template — directly in Nikol's wheelhouse and the only peer-reviewed precedent), **algebraic /
analytic number theory** (Erdős-style problems like §2.7), and **quantum information theory**
(Sihao's edge — a less-crowded arena where a clean combinatorial/linear-algebra bound can be
publishable). **These are our home fields; candidate problems (§7) should cluster here.**

> The §2.7 Liam Price precedent still matters: a 23-year-old **with no advanced math training**
> logged a verified Erdős solution. We have *more* domain depth than that — credentials are not the
> gate; problem selection + verification discipline are.

## Local environment & setup

- **Working dir:** `/Users/nikolsavova/Desktop/AI-math/` (this guide lives here).
- **`OPENEVOLVE.md`** — how to run the **local OpenEvolve install** at
  `/Users/nikolsavova/maths/openevolve` (editable clone, Python 3.14 venv at `.venv`,
  verified working). `cd` there and `source env.sh` to activate the venv **and** export
  `OPENAI_API_KEY`. Run via `openevolve-run.py <initial_program.py> <evaluator.py>
  --config <config_openai.yaml> --iterations N`. Each project needs three files:
  `initial_program.py` (with `# EVOLVE-BLOCK-START/END` markers), `evaluator.py`
  (returns a metrics dict, higher = better), `config.yaml`. **Smoke-test with
  `--iterations 3` first.** Stock example configs default to Gemini — use the
  `config_openai.yaml` variants (`gpt-5-mini`/`gpt-5-nano`). This is our **Engine B** rig.
- **`~/.config/proof_hunter/openai_key.txt`** — **plaintext OpenAI API key** (`sk-proj-…`), kept
  OUTSIDE the repo (moved there 2026-06-26) so it is never committed. `env.sh` and
  `problem-id/common.py` both read it, so the secret lives in one place. ⚠️ **Security notes:** it is
  *unencrypted on disk*; do **not** commit it, paste it into prompts, or include it in any arXiv/repo
  upload. The repo's `.gitignore` blocks `*key*.txt` as a backstop.
  *(This guide intentionally does not record the key's value.)*

---

## 0. The thesis, restated for v2

The edge is **not** being clever amateurs. It is being a **small team that wields three
frontier capabilities at once** that almost nobody is yet combining well:

1. **Frontier LLM reasoning** (GPT-5.5-Pro, Opus) for idea-generation, proof drafting,
   counterexample hunting, and cross-domain literature connection.
2. **Evolutionary program search** (OpenEvolve / ShinkaEvolve-style) for explicit
   bound-tightening and construction-finding — *self-certifying* objects.
3. **Autoformalization** (Lean + Aristotle-class) to turn a candidate proof into a
   **machine-checked** artifact — which is exactly what flips an AI-assisted claim from
   "dismissed" to "publishable."

The 2025–2026 record (Section 2) proves all three now produce **genuine, human-verified,
sometimes peer-reviewed** mathematics. The catch — and our entire operating discipline —
is that *every* credible result had **a human selecting the problem, correcting the AI's
errors, and certifying novelty.** The failures (Section 3, "Erdősgate") came from skipping
exactly those steps. We design our week around doing them relentlessly.

**Bottom line:** the realistic 1-week target is a *modest-but-real* result — "modest in
scope but profound in implication," in the GPT-5 paper's own words. That is not a
consolation prize; it is precisely the shape of the publishable AI-assisted results that
already exist.

---

## 1. Our two engines (unchanged core, AI-supercharged)

### Engine A — Connection-finding & proof-adaptation (LLM-driven)
LLM reads across subfields faster than any specialist, drafts proofs, and finds the lemma
in field X that cracks the problem in field Y. **Modern proof:** GPT-5 supplied the key
step for Erdős #848; GPT-5-Pro found a counterexample to a natural algorithm from a single
prompt (§2.2). **Failure mode to police:** it confidently hallucinates and "connection"
often = folklore. Mitigation: adversarial multi-model cross-check + Lean.

### Engine B — Computational discovery (evolutionary search)
Evolve *programs that build objects*; score with a cheap exact evaluator; keep the best.
**Modern proof:** ShinkaEvolve (open source) beat AlphaEvolve's circle-packing record with
~150 samples (§2.4). **Critical caveat (§2.5):** a Feb-2026 Oxford study shows *simple
repeated sampling often matches the fancy evolutionary pipeline* on math bounds — the
search-space design and prompt domain-knowledge dominate. **So: always run the dumb
baseline first; only invest in evolution if it clearly beats sampling.**

### The verification engine (what makes it publishable)
Autoformalize the key lemma in **Lean**. Erdős #728 — the first *autonomously* AI-resolved
Erdős problem — was credible precisely because the output was a checked Lean proof (§2.3).
**Every result we ship gets a verification artifact: Lean proof, UNSAT certificate, or
re-runnable evaluator. No exceptions.**

---

## 2. 2026 case studies — humans + frontier AI producing real math

> `[✓ verified]` = adversarially fact-checked in our 2026-06 research run (3-0 unless noted).

### 2.1 The flagship: "Early science acceleration experiments with GPT-5" `[✓ verified]`
- **What:** arXiv:**2511.16072** documents **four new, human-verified results**, framed as
  "modest in scope but profound in implication." Co-authors include **Bubeck, Gowers
  (Fields Medalist), Sawhney, Sellke, Coester.**
- **The four:** Erdős #848 (additive combinatorics); an online/nested **convex-body-chasing
  lower bound**; a tree-subgraph-count inequality; a dynamic-random-tree identifiability result.
- **Why it matters to us:** this is the **template and the credibility benchmark.** Professional
  mathematicians + GPT-5, modest scope, every result human-verified. That's our target shape.
- Source: https://arxiv.org/abs/2511.16072

### 2.2 Erdős #848 & the convex-body-chasing bound — "AI supplies the key step" `[✓ verified]`
- **#848:** genuinely open; **GPT-5 supplied the high-level solution step, sandwiched
  between two layers of human math.** Its detailed implementation had **numerous errors that
  humans corrected.** Logged "Full solution (green)" on Tao's Erdős AI-contributions wiki
  (Sawhney + Sellke + GPT-5, Oct–Nov 2025).
- **Convex body chasing (Coester):** GPT-5 improved the competitive-ratio lower bound from
  **√d → (π/2)√⌊d/2⌋ ≈ 1.11√d**, and **refuted a natural algorithm from a single prompt.**
- **Lesson:** the human-AI division of labor that works → *AI proposes the idea/witness,
  humans verify and repair.* Never ship the AI's raw output.
- Source: https://arxiv.org/abs/2511.16072 · https://github.com/teorth/erdosproblems/wiki/AI-contributions

### 2.3 Erdős #728 — first *autonomously* AI-resolved Erdős problem `[✓ verified, 2-1]`
- **What:** GPT-5.2 Pro + **Harmonic's Aristotle** (operated by Kevin Barreto) produced a
  **verified Lean proof**; a human translated it to informal math (arXiv:**2601.07421**, Jan 2026).
  **Tao publicly vouched** for the autonomous status — but called it "lowest hanging fruit."
- **Roles:** Barreto produced proofs; Alexeev ran Aristotle to simplify; another did literature
  search; Tao suggested ideas. **Even the "autonomous" win was a curated human-orchestrated pipeline.**
- **Lesson:** **autoformalization is real and is the credibility multiplier.** But it's still a
  showcase, not a press-button pipeline — budget human orchestration time.
- Source: https://arxiv.org/pdf/2601.07421

### 2.4 Evolutionary search: AlphaEvolve + open reproductions `[✓ verified]`
- **AlphaEvolve** (arXiv:**2511.02864**, **Tao co-author**): applied to **67 math problems**;
  rediscovered best-known in most, **improved several.**
- **ShinkaEvolve** (Sakana, **open-source**, arXiv:2509.19349): **new SOTA circle packing** (26
  circles) with **~150 samples.** OpenEvolve is the other open re-implementation.
- **Lesson:** Engine B is reproducible by a small team *today* with open tools. Bound-tightening
  on packing / cap-set / finite-geometry constructions is the proven sweet spot.
- Source: https://arxiv.org/abs/2511.02864 · https://arxiv.org/abs/2509.19349 · https://github.com/SakanaAI/ShinkaEvolve

### 2.5 The contrarian result we must respect `[✓ verified, 2-1]`
- **arXiv:2602.16805** (Oxford, Feb 2026): **simple repeated/IID sampling matches or exceeds**
  AlphaEvolve / ShinkaEvolve / OpenEvolve across three domains including math bounds. For math
  bounds, **search-space design + prompt domain-knowledge dominate; the evolutionary machinery
  is secondary.**
- **Lesson (operational):** **Run the cheap sampling baseline first.** Spend your design effort
  on *encoding the problem and the prior knowledge*, not on pipeline sophistication.
- Source: https://arxiv.org/abs/2602.16805

### 2.6 The single-researcher case studies (our closest role models) `[✓ verified]`
- **Adil Salim** (solo) + GPT-5-Pro: a convex-analysis lemma (Taylor expansion of the
  biconjugation operator), arXiv:**2510.26647**. AI suggested directions + proved intermediate
  results; **required expert supervision to fix subtle mistakes.**
- **Diez / da Maia / Nourdin** + GPT-5: a **quantitative** Malliavin–Stein CLT (explicit
  convergence rates extending a qualitative theorem) — **published in the peer-reviewed journal
  *Statistics & Probability Letters*** (arXiv:2509.03065). **The cleanest "controlled experiment →
  peer-reviewed" template that exists.**
- **Lesson:** a 1–3 person team CAN get an AI-assisted result into a real journal. The winning
  shape: **take a known *qualitative* result, make it *quantitative*/explicit/extended**, verify
  hard, frame as a controlled experiment.
- Source: https://arxiv.org/abs/2510.26647 · https://arxiv.org/abs/2509.03065

### 2.7 ⭐ Liam Price — 23-year-old amateur solves Erdős #1196 (Apr 2026) `[verified, multi-source]`
> **This is the closest precedent to *us* — read it twice.**
- **Who:** Liam Price, **23, no advanced mathematics training.** Was casually feeding open
  Erdős problems into ChatGPT — *"giving them to the AI and seeing what it can come up with"* —
  and didn't even know #1196's history when he entered it.
- **What:** fully solved **Erdős Problem #1196**, open ~60 years — about **primitive sets**
  (sets of integers where no element divides another). The proof used a **discrete approach (the
  LYM inequality)** rather than the *continuous* methods that had dominated — and **failed** —
  for decades. Tao reportedly noted prior researchers *"went astray from the start."*
- **How:** a single prompt to **GPT-5.4 Pro**. The result is **not in the literature** (genuinely
  new, not an Erdősgate-style retrieval) and the **proof was formally verified in Lean.** #1196 is
  now officially marked **solved** on erdosproblems.com.
- **Why it's our north star:** amateur + one frontier-model prompt + **a genuinely new method** +
  **Lean verification** + **logged on the open effort** = exactly our win condition, achieved by
  someone with our profile. The *method-switch* (discrete where everyone tried continuous) is the
  transferable trick: **AI is strongest when the field's default approach is the wrong one.**
- Source: https://www.scientificamerican.com/article/amateur-armed-with-chatgpt-vibe-maths-a-60-year-old-problem/ ·
  https://gigazine.net/gsc_news/en/20260427-chatgpt-math-60-year-problem/ · erdosproblems.com #1196

### 2.8 Collective AI-assisted formalization efforts `[verified, multi-source]`
- **The Equational Theories Project (Tao, 2024–2025):** a public collaboration of **professional +
  amateur mathematicians + automated theorem provers + AI + Lean** that resolved **all 22,028,942
  implications** among the **4694 simplest magma equational laws**, *every edge Lean-verified.*
  **50+ contributors**, coordinated on a Lean Zulip + GitHub PRs; informal in ~2 months, fully
  formalized in ~5 more. Tooling reality check: **brute-force finite-magma search + classic ATPs
  (Vampire, Mace4/Prover9)** did the core work; **LLMs were secondary** (Copilot, visualization).
- **Determination of BB(5), the fifth Busy Beaver value (2024):** a collaborative, **fully
  Coq-verified** proof — another model of crowd + proof-assistant settling a long-open value.
- **Lesson:** there is a **live, welcoming ecosystem** for contributing *verified* pieces to a
  collective effort — a lower-variance path to a citable contribution. And a sobering tooling note:
  for the *core* logic, mature ATPs/SAT often beat LLMs; **use the LLM where creativity is needed,
  the solver where exhaustiveness is needed.**
- Source: https://terrytao.wordpress.com/2025/12/09/the-equational-theories-project-advancing-collaborative-mathematical-research-at-scale/ ·
  arXiv:2512.07087 · arXiv:2509.12337 (Busy Beaver)

### 2.9 OpenAI's advancements (the capability curve behind all of this) `[verified, multi-source]`
- **IMO 2025 gold (July 2025):** OpenAI's experimental **general-purpose reasoning LLM** scored
  **35/42, solving 5 of 6 problems** under human conditions (two 4.5-hr sessions, **no tools**),
  graded by three former IMO medalists. **DeepMind hit gold the same year.** First models to *"craft
  intricate, watertight arguments at the level of human mathematicians."* (Other top models scored
  below bronze on the same problems — this was a step-change, not incremental.)
- **The GPT-5 lineage as a research tool:** GPT-5 → GPT-5 Pro → GPT-5.2 Pro → **GPT-5.4 Pro** in
  ~9 months, each landing real math (§2.1–2.3, §2.7). **GPT-5.5-Pro (what you have) is at or past
  this frontier.**
- **Lesson:** the models we hold are *demonstrably* capable of olympiad-grade reasoning and of
  contributing the key step to research problems. The bottleneck is **not raw capability** — it's
  **problem selection, error-correction, and verification.** That's where our week's effort goes.
- Source: https://x.com/OpenAI/status/1946594928945148246 ·
  https://simonwillison.net/2025/Jul/19/openai-gold-medal-math-olympiad/

---

## 3. The credibility bar — publishable vs. dismissed

> This section is law. Violating it is how we waste the week and our reputation.

**What got results PUBLISHED / RECOGNIZED:**
- **Genuine novelty**, established by exhaustive prior-art search *before* claiming anything.
- **Human verification** of every step; ideally a **Lean / certificate** artifact.
- **Honest framing** of the AI's role ("AI proposed; we verified/corrected").
- **Modest scope is fine** — settle one clean, well-posed question.
- A **real venue or logged open-effort contribution** (journal, or Tao's Erdős wiki, etc.).

**What got results DISMISSED — "Erdősgate," Oct 2025** `[✓ verified]`:
- Bubeck/OpenAI publicized GPT-5 "solving" open Erdős problems (e.g. #339) that were **actually
  resolved decades earlier** — a *literature find* mislabeled as a *new proof*. Site maintainer
  Thomas Bloom: **"a dramatic misrepresentation"**; Hassabis: **"embarrassing"**; a Kevin Weil
  tweet claiming 10 solved problems was deleted.
- **The lethal trap: "open in a database" ≠ "unsolved."** A problem listed as open may just mean
  no one logged the solving paper.

**The recurring failure modes (verified):** GPT-5 *"can confidently make mistakes, ardently
defend them, and confuse itself";* results depend on fine prompt details and are **hard to
reproduce**; AI "progress" **clusters where a proof or near-proof already existed in the
literature.** Tao's own characterization of AI's main current contribution: *"locating those
results or connecting known techniques."*

**Our hard rules, derived from the above:**
1. **Prior-art kill-search is step one, not step last.** Two models + Google Scholar + MathSciNet/
   zbMATH + the relevant problem-DB wiki. Try *hard* to prove the result already exists. Only a
   survivor proceeds.
2. **Never trust a single-model proof.** Cross-examine with the other model, then Lean it.
3. **State the AI's role honestly** in the writeup.
4. **No claim of "solved" without a verified artifact and a clean novelty check.**

---

## 4. Problem-selection rubric (retuned for AI-feasibility in a week)

Score each candidate 1–5 on all axes. **Enter the queue only if average ≥ 3.7 with no axis below 2.**

| Axis | 1 (reject) | 5 (ideal) |
|---|---|---|
| **Statability** | needs a chapter to define | one sentence to an undergrad |
| **AI-tractability** | needs a new theory | crackable by *extend-a-known-result*, a search, or one cross-domain lemma |
| **Verifiability** | "experts agree" | Lean-formalizable / certificate / re-runnable evaluator |
| **Novelty-checkability** | murky literature, many near-duplicates | clean enough that we can *be sure* in a day it's new |
| **Meaningfulness** | nobody cites it | a *named* problem or feeds one; people would share it |
| **Crowdedness** (inverted) | hot seminar topic this year | quietly open / a just-opened bound inviting optimization |
| **One-week-shaped** | open-ended program | a single clean win-condition artifact we can name *now* |

**Hard filters (any fail → reject):** not equivalent to a famous impossible-feeling problem (RH,
P vs NP); not actively mobbed; has an AI/search/formalization attack surface; **passes the §3
prior-art kill-search**; has a writeable-down win condition.

### The four templates ranked by 1-week feasibility (pick a primary + a fallback)
1. **Quantitative-extension (LOWEST RISK — the *Statistics & Probability Letters* play).** Take a
   known *qualitative* theorem; use GPT-5.5-Pro/Opus to derive **explicit rates / a quantitative
   version / a modest generalization**; verify hard; frame as a controlled experiment. *This is
   the only template with a peer-reviewed-journal precedent.*
2. **Evolutionary bound (Engine B).** Improve a concrete named optimization bound (packing,
   cap-set, finite-geometry, extremal-graph constant). **Cheap sampling baseline first** (§2.5),
   then OpenEvolve/ShinkaEvolve. Self-certifying → low credibility risk, but novelty margin can be tiny.
3. **Erdős-problem contribution.** Work a *genuinely* unsolved problem from erdosproblems.com,
   cross-checked against the AI-contributions wiki to avoid dupes/Erdősgate. A logged green
   solution = an accepted win. Higher math risk.
4. **Autoformalization showcase (#728 model).** Take a known-but-unformalized proof; drive
   Aristotle/Lean to a checked proof; contribute to mathlib / short arXiv note. Lower novelty,
   high certainty, good as a *secondary* deliverable.

---

## 4c. Phase structure — selection is its OWN phase, before the solve sprint

> **Course-correction (2026-06-24, Nikol):** problem identification is the *bulk* of the challenge and
> was badly under-resourced. Our first pass covered <0.1% of the open-problem universe as a convenience
> sample. We now split the project into two phases:
>
> - **Phase I — Problem Identification at scale** (instrumented funnel over 10k–50k problems → ~40
>   finalists → 3–6 sprint targets). Full design in **`PROBLEM_ID_PIPELINE.md`**. Key idea: hunt
>   *curated, low-LLM-saturation* lists (IQOQI quantum problems, COLT open-problem track, discrete-geometry
>   problem books) where the alpha is — not the already-swept Erdős catalogue. `llm_saturation_inv` and
>   `self_certifying` become first-class heuristics.
> - **Phase II — The solve sprint** (§5 below), entered only once Phase I delivers vetted targets. The
>   §7b shortlist (A1/B1/B2/B3) is a *Phase-0 pilot* — useful, kill-searched, but not the output of the
>   real funnel. Treat it as a fallback/warm-start, not the committed target set.

## 5. The 7-day *solve* sprint plan (Phase II)

> Two tracks run in parallel: **Track A** (Engine A / quantitative-extension / Erdős) and
> **Track B** (Engine B / evolutionary bound). De-risk both early; converge on the leader by Day 4.

**Day 0–1 — Source & select.**
- Pull 10–15 candidates: erdosproblems.com (+ AI-contributions wiki), Open Problem Garden,
  recent arXiv "quantitative version of / explicit constant for" gaps in `math.CO/NT/MG/PR`.
- Score with §4 rubric. **Run the §3 prior-art kill-search on the top 4** with *both* models.
- **Deliverable:** 2–3 surviving targets, each with a named win-condition artifact; one primary, one fallback.

**Day 2 — Stand up & de-risk both pipelines on KNOWN benchmarks.**
- Track B: implement the evaluator; **reproduce a known bound** (e.g. a known circle-packing or
  cap-set value) with cheap sampling, *then* OpenEvolve — confirm the rig works and that evolution
  beats sampling for *this* problem (else stay with sampling).
- Track A: have GPT-5.5-Pro + Opus draft the attack on the extension/connection target; identify
  the key lemma; **draft its Lean statement** to confirm it's formalizable.

**Day 3–4 — Push the leading target.**
- Iterate proofs/searches. **For any candidate proof step, immediately attempt Lean
  formalization** — formalization failure is the fastest hallucination detector we have.
- Run Track B search at scale on compute. Log every negative result.
- **Day 4 gate:** pick the single target most likely to yield a verified artifact by Day 6. Drop the other.

**Day 5 — Verify adversarially.**
- Cross-model attack: Opus tries to *refute* GPT's proof and vice-versa; resolve every objection.
- **Complete the Lean proof of the key lemma** (or the certificate / re-runnable evaluator).
- **Re-run the prior-art kill-search** now that the result is concrete — last novelty gate.

**Day 6 — Write up.**
- arXiv-style note: statement, proof, the verification artifact, honest AI-role disclosure, prior-art.
- *Or* log the verified contribution to the open effort (Erdős wiki / mathlib PR) with artifact.

**Day 7 — Buffer / polish / submit.**
- Fix what Day 6 exposed. Post to arXiv or submit to a specialist venue (*Geombinatorics*,
  *Electronic J. Combinatorics*, *Experimental Mathematics*, *Statistics & Probability Letters*-class).

---

## 6. Tooling stack

| Need | Tool | Notes |
|---|---|---|
| Idea-gen, proof drafting, counterexamples, lit-connection | **GPT-5.5-Pro / o-series + Claude Opus** | Use *both*; make them cross-examine. Note: no documented recognized **Opus**-led result yet — an open lane for us. |
| Evolutionary construction / bound search | **OpenEvolve / ShinkaEvolve** | Needs a cheap *exact* evaluator. **Run repeated-sampling baseline first** (§2.5). |
| Existence / coloring / Ramsey / packing over finite structures | **SAT/SMT** (CaDiCaL, Kissat) + Cube-and-Conquer | Emits checkable UNSAT certificates. |
| **Verification (the credibility multiplier)** | **Lean 4 + mathlib + Aristotle-class autoformalizer** | Formalize the key lemma. Doubles as hallucination detector. |
| Prior-art kill-search | both LLMs + **Google Scholar, MathSciNet/zbMATH**, problem-DB wikis | Adversarial: try to prove it's already known. |
| Numeric exploration / conjecture-forming | **SageMath, Python (numpy/sympy)**, OEIS | Find the pattern, then formalize. |
| Cross-domain literature sweep | our **deep-research workflow** | Already used twice; see Appendix B. |

---

## 7. Open questions driving the next research pass
- **Is there ANY recognized Opus-led math result yet?** None surfaced — confirm, because it's our
  differentiation lane (and tells us how much to lean on GPT vs Opus).
- **How reliable is Aristotle-class autoformalization on an *arbitrary* known proof** vs. the #728
  curated showcase? Determines feasibility of Template 4.
- **The concrete shortlist:** turn §4 into an actual scored list of 5–10 attackable problems. *This
  is the immediate next deliverable.*
- **For Engine B:** which specific named bounds are (a) improvable and (b) not already mobbed —
  given §2.5 says prompt/search-space design is what wins?

---

## 7b. Scored candidate shortlist (Day 0–1 deliverable — 2026-06-24)

> Sourced by four parallel research agents (one per home field), each applying the §3
> prior-art/Erdősgate guard. **Ratings 1–5; Crowd 5 = NOT crowded.** ⚠️ **Universal caveat
> (raised by every agent): the web-search layer was caught fabricating future-dated "records."
> Before staking work on ANY pick, re-verify the live record from the primary source** — this
> is the Day-1 prior-art kill-search, non-negotiable. (Number-theory field re-running; will append.)

### Track A — quantitative-extension (probability/measure; Nikol's wheelhouse; the *only* peer-reviewed template)
| # | Problem | T | V | N | M | C | Attack |
|---|---|--|--|--|--|--|---|
| **A1 ⭐** | **Berry–Esseen rate for the local-minima count of discrete fractional Brownian motion** (Dolgushev–Bénichou 2025 proved the CLT w/ explicit variance but *no rate*; H<3/4). arXiv:2506.04159 | 4 | 4 | 4 | 4 | **5** | Project onto dominant 2nd Wiener chaos → 4th-moment Kolmogorov bound → bound a contraction norm $\|f_N\otimes_1 f_N\|$ (finite sum of fGn covariances; **Lean-able term-by-term**). Closest stylistic clone of the §2.6 published precedent. |
| A2 | **Explicit rate for finite free convolution $\boxplus_d\to\boxplus$** (Fujie 2025 got Kolmogorov convergence, *no rate*). arXiv:2505.15575 | 4 | 4 | 3.5 | 4 | 4 | Finite free cumulants are explicit polynomials, additive under $\boxplus_d$, → $O(1/d)$ per cumulant. **Algebraic ⇒ maximally Lean-friendly.** Non-sharp explicit rate = safe deliverable. |
| A3 | **$W_2$ (2-Wasserstein) fourth-moment theorem on the 2nd Poisson chaos** (exists on Wiener chaos; *no Poisson analogue*). arXiv:1701.03120 | 3 | 4 | 4 | **5** | **5** | Mirror Wiener case (Arras et al.) at q=2; one new Poisson contraction inequality. Emptiest niche, highest meaningfulness. |

### Track B — self-certifying construction/bound (combinatorics & QIT; Engine B / SAT; Sihao runs the rig)
| # | Problem | T | V | N | M | C | Attack |
|---|---|--|--|--|--|--|---|
| **B1 ⭐** | **GR(4, K₄, 2)** generalized Ramsey, freshly introduced, ∈{15,16,17}, almost nobody searching. arXiv:2407.07285 | 4 | **5** | **5** | 3 | **5** | Tiny SAT/local-search: exhibit a 4-coloring of K₁₅/K₁₆ with no K₄ spanning ≤2 colors (self-certifying lower bound). |
| B2 | **R(B₄, B₇)** book Ramsey, gap is *exactly 1* ∈{22,23}. arXiv:2407.07285 | **5** | **5** | **5** | 3 | 3 | SAT both directions on K₂₂ (231 edge vars; cheap book clauses) → **DRAT certificate**; or local search for the K₂₂ coloring. |
| B3 | **GUPBs in 3⊗3⊗3** (genuinely-unextendible product bases) — existence at *any* size is OPEN (size-13 just ruled out). arXiv:2509.26135 | 4 | **5** | 4 | 4 | **5** | OpenEvolve/search: orthogonality factorizes across parties + finite unextendibility check. **Every hit also yields a new bound-entangled state.** Pure combinatorics/linear algebra. |
| B4 | **Complex Grassmannian line packings** ("Game of Sloanes" open cells). | **5** | **5** | 4 | 3 | **5** | OpenEvolve with fidelity/coherence evaluator vs. the public record table. Highest tractability; margin can be tiny. |
| B5 | **Two-distance 6-chromatic plane graph — a *new* distance ratio d** (proving χ(plane, two distances)≥6 for new d). arXiv:2010.12656 | 4 | 5 | 4 | 4 | 4 | Inner SAT (5-coloring UNSAT) + **evolutionary outer loop over ratios d & point-set generators**. New d = citable. |

### Track C — number theory (Nikol's strength; partial — agent stalled, filled by hand 2026-06-24)
- ⚠️ **AVOID primitive sets (despite the §2.7 Liam Price precedent): the area just got crowded.**
  Tao's May-2026 program ("Primitive sets and von Mangoldt chains: Erdős #1196 *and beyond*",
  arXiv:2605.00301) introduced a Markov-chain/von-Mangoldt method that has *already settled several*
  primitive-set + covering-system conjectures. Racing Tao = the one thing §4 forbids.
- 🎁 **Best NT sourcing mechanism = DeepMind's `formal-conjectures` Lean repo**
  (github.com/google-deepmind/formal-conjectures). It holds **open Erdős/number-theory conjectures
  already formalized as Lean statements** — i.e. the verifiability problem is *pre-solved*; a hit is
  Lean-checkable by construction. **Day-1 action:** browse `FormalConjectures/ErdosProblems/` for
  entries marked open with low literature activity, cross-check erdosproblems.com + the AI-contributions
  wiki, and treat any survivor as a Track-A/Erdős candidate. (Note arXiv:2604.03789 "Automated
  Conjecture Resolution with Formal Verification," 2026 — others are mining this repo; move deliberately.)
- **Candidate area to probe (needs Day-1 verification):** covering systems (e.g. the odd-moduli
  question and disjoint-covering finiteness results, arXiv:2603.26043 / 2501.15170) — but check
  crowding/hardness carefully before committing. *No NT candidate is greenlit yet; this is a lead list.*

### 🔬 Kill-search verdicts (2026-06-24, primary sources)
> Adversarial prior-art check: actively tried to prove each result already exists / gap is closed.

- **B1 — GR(4,K₄,2): ✅ GREEN.** Confirmed from the **actual Table 1 of arXiv:2407.07285** (HTML, not
  the fabricating search layer): **lower 15, upper 17, range — still open.** Cross-checked vs.
  Radziszowski *Small Ramsey Numbers* rev #18 (Jan 2026): gap intact. **Cleared to build.**
- **B2 — R(B₄,B₇): ✅ GREEN.** Table 1 confirms **lower 22, upper 23 — gap exactly 1, open.** Lower-bound
  companion arXiv:2410.03625 exists; **DRAT-certifiable both ways. Cleared to build.** *(Minor: confirm no
  2025–26 closure beyond rev #18 on Day 1.)*
- **A1 — fBm local-minima Berry–Esseen rate: 🟡 AMBER — survives, with a real risk to resolve first.**
  - *Gap is real:* arXiv:2506.04159 (Dolgushev–Bénichou) confirmed **qualitative CLT only, no rate.** The
    specific local-minima-count rate is **not published.** ✓
  - *BUT the kill-search surfaced a dense adjacent literature:* quantitative CLTs / Berry–Esseen for
    **level functionals and *critical points* of Gaussian processes** (Kratz–León; Estrade–León; "Spectral
    criteria for local functionals… critical points" arXiv:2501.07356; quantitative-critical-point CLTs).
    The number of local minima of fGn **is** a critical-point/level-functional count. Optimal Breuer–Major
    Berry–Esseen rates for the dominant rank-2 chaos are **already known** (1/√n for H<2/3; n^{-1/2}log²n at
    H=2/3; n^{6H−9/2} for H∈(2/3,3/4)).
  - **⇒ Risk:** a referee may call the result *"immediate from Kratz–León + Nourdin–Peccati."* It is genuine
    but **modest and possibly derivable-on-sight.**
  - **Mandatory pre-build gate (Nikol):** (i) rule out that an existing critical-point quantitative CLT
    already covers/trivially-implies the discrete-fBm local-minima rate; (ii) judge whether the rank-2
    reduction yields something a referee won't deem immediate. **Greenlight A1 only if both pass.**

### Recommended commitment (updated post-kill-search)
- **SAFE PRIMARY (verified, self-certifying): B1 + B2** (GR(4,K₄,2) / R(B₄,B₇) via SAT). Both **GREEN**,
  open confirmed from primary source, DRAT-certifiable — **near-certain to yield a verifiable, defensibly
  novel logged result in a week.** This is now Track B and our floor.
- **HIGH-VALUE PRIMARY *on condition*: A1** — higher payoff (peer-reviewed template, Nikol's domain) **iff
  it clears the AMBER gate above by Day 2.** If it clears → it's the headline; if not → drop to B-track + B3.
- **HIGH-UPSIDE swing: B3** (GUPB 3⊗3⊗3) — open *existence*, witness = new bound-entangled state; Sihao's edge.
- Maps onto §5: **Track B = B1/B2 (build now, de-risk Day 2 on a known Ramsey value); Track A = A1 (run the
  novelty gate first)**. Day-4 gate picks the winner to finish.

---

## 8. Working log (append-only; newest first)

### 2026-08-18 (latest) — ERDŐS #1208 Ruzsa high-support branch (Sihao + Codex)

- Applied Ruzsa's triangle inequality with `X=D`, `Y=JD`, `Z=-D` to prove
  the exact universal inequality `|D+JD|^2 >= |D||D+D|`.  An explicit
  injection from `JD x (D+D)` into `(D+JD)^2` is included, so no asymptotic
  or geometric input is hidden.
- Consequently
  `|D+D||D+JD| >= N^(1/2)|D+D|^(3/2)`.  The full `N^(3-o(1))` product and
  cube-root grid conclusion now hold throughout the high-support branch
  `|D+D| >= N^(5/3-o(1))`.
- Added `ORTHOGONAL_RUZSA_HIGH_SUPPORT_BRANCH.md` and its exact regression
  verifier.  The closure, transformed-parabola, perpendicular-ruler, and
  exhaustive small-grid checks pass.  The unresolved case is now
  simultaneously low-support and wide.  Target a common-energy inverse
  theorem or decorated-parallelogram estimate only in that compressed
  regime.  Literature check found no generic common-energy theorem carrying
  the required quarter-turn plus complete-difference structure.  Direct API
  spend `$0`.

### 2026-08-18 (latest) — ERDŐS #1208 product theorem for parallel covers (Sihao + Codex)

- Proved an exact structured branch of the full orthogonal product gate.  If
  a distance-Sidon `k`-set lies on `r` parallel lines, its within-line
  difference set has `h>=1+k^2/r-k` elements and lies in `D`.  Fibrewise
  one-dimensional sumset growth after adding its quarter-turn gives
  `|D+JD|>=h^2`.
- Since `|D+D|>=2|D|-1`, this yields
  `|D+D||D+JD|>=(2N-1)(1+k^2/r-k)^2 >> N^3/r^2`.
  Therefore the full `N^(3-o(1))` product and cube-root grid conclusion hold
  whenever `r=k^(o(1))`.  This uses all of `D` and gains a factor `k/r` over
  the older `A+J(A-A)` line-support bound.
- Added `ORTHOGONAL_PRODUCT_PARALLEL_COVER.md` and its exact verifier.  The
  ten-point one-line Golomb ruler has `N=h=91` and orthogonal support `91^2`;
  the dense perpendicular 40-point witness has `N=1561`, `h=381`, and
  orthogonal support 1,413,381.  Both pass.  Remaining case: polynomially
  many parallel layers in every useful direction.  Local compute only;
  direct API spend `$0`.

### 2026-08-18 (latest) — ERDŐS #1208 orthogonal energy--support gate (Sihao + Codex)

- Derived the exact common energy
  `E_perp(D)=sum_q R_D(q)R_D(Jq)=sum_t r_(D+JD)(t)^2`.  Cauchy gives
  `|D+JD|>=N^4/E_perp`, so the scale-perfect global estimate
  `E_perp<=N^(1+o(1))|D+D|` implies the full
  `|D+D||D+JD|>=N^(3-o(1))` theorem and settles the cube-root exponent.
- Reinterpreted the earlier `k^5` unrestricted-energy data correctly: the
  ordinary support pays for that growth.  Exact closure ratios
  `E_perp/(N|D+D|)` through `k=70` stay in `[0.265,0.313]`; transformed-
  parabola and dense-perpendicular ratios are `0.0952` and `0.0264`.
- Proved a full-power barrier to pointwise strengthening.  Finite-field
  parabola pair-sums have a nonzero vertical translation with `Omega(p^2)`
  representations.  Two generic rational deformations align these peaks as
  `q,Jq` while keeping the union distance-Sidon, giving
  `R_D(q)R_D(Jq)=Omega(N^2)`.  The exact 46-point certificate has `N=2071`,
  peak multiplicities `(252,252)`, support 608,903, energy 7,263,825, and
  global ratio `0.005760...`.
- Added `ORTHOGONAL_ENERGY_SUPPORT_GATE.md` and its exact verifier.  Restart
  at a global popular-sum tail/charging theorem or the positive-definite
  autocorrelation structure of the complete difference set; maximum-
  translation bounds are definitively too strong.  Local compute only;
  direct API spend `$0`.

### 2026-08-18 (latest) — ERDŐS #1208 generic-segment fibre barrier (Sihao + Codex)

- Killed the new local quadratic-expansion conjecture asymptotically.  Select
  `M^(2-o(1))` lattice vectors of distinct norms in an `M by M` box, pair
  each `e` with `J(e-t)`, and realize the resulting vectors as independently
  translated segments.  Generic rational translations give a distance-Sidon
  set and avoid every unintended relation in the target row.
- The resulting fibre satisfies `|E_t|=M^(2-o(1))` but
  `|E_t-JE_t|=O(M^2)=|E_t|^(1+o(1))`.  Thus the proposed fibre theorem fails
  by essentially a full power, even though its Ruzsa implication to the
  conditional `F_2(n)<=n^(2/5+o(1))` bound was correct.
- Added `FIXED_ROW_FIBRE_EXPANSION_BARRIER.md` and its exact verifier.  The
  concrete 116-point distance-Sidon instance has `|D|=13341`, fibre size 29,
  and support size 123; all checks pass.  The direct global product gate
  survives because generic translations make the remaining difference set
  expand.  New restart rule: charge structured rows to global support or
  average across rows; do not use a maximum-row-only theorem.  Direct API
  spend `$0`.

### 2026-08-18 (latest) — ERDŐS #1208 local fibre expansion route (Sihao + Codex)

- For `E_t={e in D:t-e in JD}`, representation counting gives
  `|D+JD|>=N^2/max|E_t|`, while Ruzsa's triangle inequality gives the exact
  upper relation `|E_t-JE_t|N<=|D+D|^2`.
- Consequently the now-falsified local conjecture
  `|E_t-JE_t|>=|E_t|^(2-o(1))` would imply
  `|D+D||D+JD|>=N^(5/2-o(1))`, hence
  `F_2(n)<=n^(2/5+o(1))`.  This would be a major partial upper improvement,
  but it would not settle the expected cube-root exponent.  The next log
  entry records its generic-segment counterexample.
- Extended `verify_orthogonal_two_support_gate.py` to check exact maximum-
  fibre profiles.  The closure, transformed parabola, and dense-perpendicular
  examples give `(r,|E_t-JE_t|)=(56,2303),(1,1),(97,9409)` respectively.
  Next kill-search: scalable fixed-row six-biclique/eight-corner families.
  Local compute only; direct API spend `$0`.

### 2026-08-18 (latest) — ERDŐS #1208 orthogonal two-support gate (Sihao + Codex)

- Isolated a new full-resolution inequality.  For `D=A-A`, `N=|D|`, the
  product `|D+D||D+JD|>=N^(3-o(1))` immediately gives
  `|A|<=m^(2/3+o(1))` in the `m x m` grid.  It packages ordinary additive
  structure and quarter-turned expansion into one statement and avoids the
  separate intermediate line-rich splice required by the rotated-support
  collision argument.
- Derived the exact fibre model
  `F(s,t)=#{d in D:s-d in D,-J(t-d) in D}` with
  `sum F=N^3` and
  `sum F^2=Xi(D)=sum_q R_D(q)^2R_D(Jq)`.  Hence
  `|D+D||D+JD|>=N^6/Xi(D)`.
- Killed the obvious moment conjecture `Xi<=N^(3+o(1))` asymptotically.
  Two dense Golomb subrulers on perpendicular axes give genuine integral
  distance-Sidon sets with `Xi(D)>>N^4`; the proof uses cross energy between
  their scalar difference sets followed by weighted Cauchy.  The product
  inequality itself survives and is very slack on this family.
- Added `ORTHOGONAL_TWO_SUPPORT_GATE.md` and
  `verify_orthogonal_two_support_gate.py`.  Exact checks pass for the fibre
  identity and for closure, transformed-parabola, and dense-perpendicular
  profiles.  New restart rule: attack the support product directly or split
  the parallel fibres before using moments; never apply the global mixed
  third-moment majorant.  Local compute only; direct API spend `$0`.

### 2026-08-18 (latest) — ERDŐS #1208 centered-residual design dichotomy (Sihao + Codex)

- Reorganized the exact positive residual
  `C(A)=#{(d,u,v) in (D*)^3:u+v=Jd}` as a weighted edge count in the
  unordered pair-sum set `Q=A\oplus A`:
  `C(A)=sum_(p-q in JD*)w(p)w(q)`.  The weight is one for a double and two
  for a sum of distinct points.  The identity also proves that the two
  underlying pair-sums cannot share an endpoint.
- Proved the endpoint cleanup `C_<=5(A)<=12k^3`.  On the certified 60-point
  closure witness the full residual is 259,724; 218,640 relations have six
  distinct labels and 218,516 are also transverse.  Thus the dominant term
  is genuinely six-point and transverse.
- Built the six-role Gaussian matrix
  `a0+i b0-i c0-a1-i b1+i c1=0`.  Dense-core pruning and the improved
  Dvir--Saraf--Wigderson rank theorem prove the unconditional dichotomy
  `C_(6,tr)(A)<=864t k^2`, where `t` is maximum two-role codegree.  Hence the
  nearly-linear-codegree branch is cubic.
- The exact obstruction is now calibrated.  The compact-anchor witness has
  one constituent-edge role-pair codegree 3,880 at `k=117`; the fixed-colour
  witness has 802 at `k=65`.  Their totals remain subcubic.  Conversely the
  closure matrices at `k=20,60` have exact ranks `6k-7`, saturating the five
  role-constant plus two coordinate kernel directions.  Support rank and a
  uniform codegree bound cannot finish.
- Added `CENTERED_RESIDUAL_DESIGN_DICHOTOMY.md` and
  `verify_centered_residual_design_dichotomy.py`; the verifier passes the
  weighted identity, four endpoint profiles, four adversarial role-pair
  profiles, and both rank certificates in about five seconds.  Decision:
  the next theorem must treat the three exceptional realized-edge incidence
  blocks spectrally/radially, equivalently prove the existing fourth-moment
  bound.  Local compute and primary-source reading only; no API spend.

### 2026-08-18 (latest) — ERDŐS #1208 two-sided-product audit (Sihao + Codex)

- Closed the proposed two-sided sumset route at its exact abstract limit.
  For every co-Sidon pair `X,Y`, the map
  `(x1,x2,y1,y2) -> (x1+y1-y2, y2+x2-x1)` is injective, proving
  `|X+Y-Y||Y+X-X|>=|X|^2|Y|^2`.
- Proved exponent sharpness with the classical Erdos--Turan Golomb ruler
  `2pi+(i^2 mod p)`: splitting it into two equal parts gives a direct pair
  for which both third sumsets have only quadratic size.  Therefore the
  congruence of the two actual rotated sumsets cannot upgrade the direct-sum
  floor from `k^2` to `k^3`.
- Derived the exact centered Fourier identity
  `E_J(A)=2k^3-k^2+#{(d,u,v) in (D*)^3:u+v=Jd}`.  The residual is a positive
  integer count; all second-moment covariance information has already been
  exhausted by `A+JA` being direct.
- Added `phase2/loop/erdos1208/TWO_SIDED_ROTATED_SUPPORT_AUDIT.md` and the
  exact verifier `verify_two_sided_rotated_support_audit.py`.  The verifier
  passes the Golomb construction, injection, directness, distance-Sidon
  seed, and centered collision identity.
- Decision: do not reopen a Shannon/Ruzsa/product proof using only co-Sidon
  data.  Return to the centered residual/global transverse
  decorated-parallelogram moment, retaining radial uniqueness and complete
  difference-set realizability.  Approximate spend: local compute only.

### 2026-08-18 (latest) — ERDŐS #1208 third-additive-energy barrier (Sihao + Codex)

- Closed the tempting Fourier/Hölder surrogate for rotated triple energy.
  For the integer finite-field parabola `P_p`, vector-Sidonicity and maximum
  collinearity two hold exactly, while `|3P_p|<=9p^2`; consequently
  `E_3^+(P_p)>=p^4/9`.
- Proved that a generic integral invertible linear map separates every
  Euclidean edge length without changing additive relations or collinearity.
  Hence arbitrarily large general-position distance-Sidon sets still have
  fourth-power ordinary third energy.  Any successful Fourier argument must
  retain the correlation between a frequency and its quarter-turn.
- Added `THIRD_ADDITIVE_ENERGY_BARRIER.md` and a pure-integer certificate.
  At `p=127`, `T=[[-93,-83],[66,-1]]` gives 127 points, all 8,001 distances
  distinct, no collinear triple, triple support 81,221, and exact third energy
  86,658,955.  Its actual off-diagonal rotated energy is only 2,032,998
  (`0.9925...k^3`) with maximum fibre two, so Hölder loses essentially a full
  factor of `k` on the certified example.  No API spend.
- **Next:** continue on the restricted rotated/transverse moment itself; an
  ambient-sensitive higher-energy inequality is not ruled out, but an
  ordinary `|A|`-only energy majorant is.

### 2026-08-18 (latest) — ERDŐS #1208 eight-corner product barrier (Sihao + Codex)

- Disproved the adaptive eight-corner hypothesis asymptotically, not just by
  finite search.  One exact transverse base relation has a rational affine
  four-dimensional completion family at every corner.  Taking `t`
  independent generic copies of all eight families gives integer
  distance-Sidon sets with `|A|=6+24t` and
  `K(A)>=(|A|+18)/24`.
- Proved the generic product is legitimate.  Different block supports are
  separated by independent variables.  For two edges joining the same two
  blocks, the nine mixed quadratic matrices `L_r^T L'_s` are pairwise
  distinct for every pair of corner types.  Equalities contained in one
  block are nonidentities because each of eight exact seed completions lies
  inside the certified 60-point distance-Sidon witness.  Rational Zariski
  density and common-denominator scaling produce lattice examples.
- The deterministic closure independently extended to 120 exact points with
  corner degrees `(43,56,54,43,43,54,56,43)`.  More than eleven thousand
  valid forced candidates remained near the endpoint, but further search is
  unnecessary after the product theorem.
- Added `TRANSVERSE_EIGHT_CORNER_PRODUCT_BARRIER.md`, its pure-integer
  verifier, and the reproducible closure search.  Updated the earlier gate
  note to mark the route closed.  No API spend.
- **Next:** return to the global transverse second-moment/decorated-
  parallelogram estimate.  Any new pointwise/projection gate must first
  survive the product construction.

### 2026-08-18 (latest) — ERDŐS #1208 compact-anchor averaging barrier (Sihao + Codex)

- Proved the exact identity
  `sum_(u0,u1,u2 in U) C3(D;u1-u0,u2-u0)=sum_y |D intersect (y+U)|^3`.
  Hölder forces an `Omega(p^(7/2))` moment for a `Theta(p^2)` difference core
  against `Theta(sqrt(p))` compact anchors.
- Used the finite-field parabola sets `P_r={(x,x^2 mod r)}`: each is
  vector-Sidon and has no three collinear.  Deleting one endpoint for every
  common core/anchor difference preserves a linear core and makes the two
  spectra disjoint.  The anchor-lifting lemma then gives arbitrarily large
  distance-Sidon sets in general position with `T_nc=Omega(k^(7/2))`.
- Consequently `Omega(k^(3/2))` ordered non-collinear anchor triangles can
  each have `Omega(k^2)` codegree.  This kills the proposed rich-triangle
  tail by `k^(1/2-o(1))`, not merely its pointwise strengthening.
- Added `FOREIGN_SHIFT_AVERAGING_BARRIER.md` and an exact certificate.  Its
  `p=127,q=7` instance has 117 points, all 6,786 distances distinct, maximum
  collinearity two, moment identity `880874`, and distinct-anchor
  contribution `317592`.
- The construction remains exactly cubic at second-moment scale.  The
  correct primary route is again the transverse second-moment/decorated-
  parallelogram theorem; an ambient third-moment bound is secondary.  No API
  spend.
- Isolated an adaptive eight-corner sufficient gate for the returning
  transverse theorem.  Every relation `d=f+Je` has eight projections obtained
  by choosing one endpoint from each uniquely oriented edge.  A
  subpolynomial minimum projection degree for every relation implies the
  cubic transverse bound by an eight-way charging argument.  Complete exact
  profiles have maximum adaptive degrees `5,6,8` on heavy closures
  `k=30,45,60` and `6` on the 117-point compact-anchor lift.  Added
  `TRANSVERSE_EIGHT_CORNER_GATE.md` and its verifier.
- **Next:** attack `E_trans<=k^(3+o(1))` through its restricted fifth
  incidence, adaptive eight-sign inverse lemma, or global rich-tail
  formulation; do not return to any global non-collinear third-moment bound.

### 2026-08-18 (latest) — ERDŐS #1208 anchor-lifting lemma and simultaneous rich-triangle benchmark (Sihao + Codex)

- Proved a general transfer lemma: if integer sets `B,U` are vector-Sidon and
  their nonzero difference sets are disjoint, an integral linear map and one
  translate make `T(B) union (t-JT(U))` distance-Sidon while transferring
  every three-point correlation of `B-B` into an anchor-triangle fibre
  codegree.  This is a finite algebraic-avoidance proof.
- Consequence: qualitative radial uniqueness alone cannot control any
  prescribed finite family of foreign-shift correlations.  A successful
  theorem must retain ambient height or a global rich-tail/line tradeoff.
- Built and exactly certified a 139-point integer stress test: all 9,591
  distances distinct, maximum collinearity seven, and 231 non-collinear
  anchor triangles simultaneously having 2,281--3,464 core witnesses.  Their
  ordered `T_nc` contribution is 3,918,648, or `1.459...k^3`.
- The anchors principally lie on two lines, so the example calibrates the
  unresolved intermediate-collinearity branch rather than refuting the wide
  conjecture.  It shows the sharp cubic total can be spread across many
  popular triangles, not just one exceptional gadget.
- Files: expanded `FOREIGN_SHIFT_TRIANGLE_COUNTEREXAMPLE.md` and new exact
  verifier `verify_foreign_shift_anchor_constellation.py`.  No API spend.
- **Next:** formulate an ambient-sensitive or line-sensitive tail inequality
  that permits this anchor lift, and prove it first above the high-richness
  threshold.  Generic common-energy and qualitative radial arguments are now
  definitively too weak.

### 2026-08-18 (latest) — ERDŐS #1208 foreign-shift third moment and quadratic triangle obstruction (Sihao + Codex)

- Derived the exact identity
  `sum_z r(z)^3 = sum_(u,v) C_3(JA;u,v) C_3(D;u,v)` for
  `r(z)=#{(a,d):z=a+Jd}` and `D=(A-A)\{0}`.  The unrestricted cubic moment
  bound is false by the perpendicular-ruler obstruction.  The viable
  statistic is the ordered, pairwise-distinct, non-collinear contribution
  `T_nc`; the exact split is `sum r^3<=4T_nc+9L^2 sum r`, where `L` is maximum
  collinearity.
- Read the primary TeX of Shkredov's arXiv:1405.3132, 2408.08113, and
  2502.20702.  Their common-energy theorems concern ordinary four-variable
  energy and inverse/small-doubling structure.  They do not give the required
  foreign-shift three-point upper bound.
- Killed the pointwise triangle-codegree route asymptotically.  Welch Costas
  differences are a bijective lift of a punctured product torus; bounded carry
  pigeonhole gives a nonparallel translated triangle with `Omega(k^2)` copies.
  Generic integral norm separation plus one anchor triangle turns this into a
  genuine planar distance-Sidon example.  Linearly many anchors show the
  cubic averaged target is exponent-sharp.
- Added a fully exact certificate: 129 integer points, 8,256 pairwise distinct
  distances, and one non-collinear anchor triangle appearing in exactly 3,610
  fibres.  `verify_foreign_shift_triangle_counterexample.py` passes using
  integer arithmetic only.
- Files: `FOREIGN_SHIFT_TRIANGLE_COUNTEREXAMPLE.md`,
  `verify_foreign_shift_triangle_counterexample.py`, and updated #1208/root
  handoffs.  No API spend.  The checkout still contains unrelated unstaged
  #838 work, so only the #1208/handoff files from this entry should be staged.
- **Next:** prove the sharp rich-triangle tail
  `#{tau:q(tau)>=lambda}<=k^(3+o(1))/lambda` for ordered non-collinear
  triangles in the wide regime, then couple it to the line-support theorem
  through intermediate collinearity.  Do not revisit a uniform pointwise
  bound; even `k^(2-epsilon)` is false.

### 2026-08-18 (latest) — ERDŐS #1208 shear-averaged cubic support (Sihao + Codex)
- Proved the exact affine-line section bound
  `|(A-A) intersect ell|<=kL` for every line `ell`, where `L` is the maximum
  collinearity of a distance-Sidon `k`-point set.  Projection fibres give the
  proof: nonzero differences have unique ordered representations and each
  projection fibre contains at most `L` points.
- Applied it to the shear family `S_t=J+tI`.  For any `r` distinct real
  parameters, the collision energies of `a+S_t(b-c)` satisfy
  `sum_t E_t<=r(2k^3-k^2)+k^5L`.  Thus some shear has support at least
  `k^6/(2k^3-k^2+k^5L/r)`, and `r>=k^2L` forces support at least `k^3/3`.
- Added `SHEAR_AVERAGED_CUBIC_SUPPORT.md` and the exact-rational verifier
  `verify_shear_averaged_support.py`.  On the stored 12-point witness and 13
  rational shears it checks the line-section lemma, all fibre energies, and
  every Cauchy inequality; `PASS`.
- This quantifies, rather than removes, the exceptional-quarter-turn barrier.
  Unlike exact rotations, a fixed four-tuple can survive at `kL` shear
  parameters, and integral/rational shears incur quadratic ambient expansion.
  The active full-resolution target remains the prescribed-`J` transverse
  fourth moment or an inverse theorem coupling it to the parallel-line lemma.
  The Fable directive named `SOL_DIRECTIVE_1208_20260816.md` was not present
  in the current checkout or tracked history, so the committed #1208 handoff
  remained the authoritative input.

### 2026-08-18 (latest) — ERDŐS #1208 rotation-averaged cubic support (Sihao + Codex)
- Proved an exact averaged theorem for the live rotated triple map.  For a
  distance-Sidon set `A`, `|A|=k`, and any `r` distinct rotations, the sum of
  the collision energies of `a+R(b-c)` is at most
  `r(2k^3-k^2)+2k^4`.  The diagonal term is the exact ordered pair-sum energy;
  off the diagonal, a fixed four-tuple leaves at most two directed edges of
  the required length and one orientation-preserving rotation per edge.
- By Cauchy, some rotation has support at least
  `k^6/(2k^3-k^2+2k^4/r)`.  Thus any `k` rotations force one cubic support of
  size at least `k^3/4`.  For a hostile box with at most `M` possible outputs,
  this gives `k<=2sqrt(M/r)` when `r<=k` and the desired cube-root bound
  `k<=(4M)^(1/3)` once `r>=k`.
- This turns the small-unimodular-unit lane into an exact full-resolution
  interface but does not control the prescribed quarter-turn of the ordinary
  grid.  Rational rotations pay a denominator-square ambient cost, while the
  square lattice has only four integral rotations.  The unresolved arithmetic
  input remains a bounded-root-discriminant non-CM tower with linearly many
  low-expansion relative units.
- Added `ROTATION_AVERAGED_CUBIC_SUPPORT.md` and the exact-rational verifier
  `verify_rotation_averaged_support.py`.  On the stored 12-point adversarial
  witness and twelve rotations it checks total energy `57164<=81216`; all
  support-energy Cauchy inequalities pass.  A current arXiv sweep found no new
  planar #1208 resolution; the August 14 Tidor--Yu--Zakharov paper settles the
  distinct-distance exponent in `R^3` but does not directly cover this
  decorated planar configuration.  #1208 remains open.

### 2026-08-18 (latest) — ERDŐS #1208 design-matrix compression and affine-rank barrier (Sihao + Codex)
- Applied the exact improved design-matrix theorem of Dvir--Saraf--Wigderson
  (arXiv:1211.0330) to the pruned fixed-row role matrix.  With `r` original
  relations, the retained core is a `(4,r/(8k),1)` design, so its corank is at
  most `768k^2/r`.  Thus a hypothetical `k^(3/2+epsilon)` row is genuinely
  rigid, with only `O(k^(1/2-epsilon))` Gaussian-linear degrees of freedom.
- Closed a seductive but false proof.  The fixed difference makes the actual
  coordinate vector satisfy `Mz=d*1`, not `Mz=0`.  Projecting away the common
  right-hand side creates the second kernel vector but can lower rank by one;
  homogenizing with the endpoints of `d` instead creates two dense columns
  and destroys bounded column overlap.  The rank theorem therefore gives
  compression, not `r<=k^(3/2)`.
- The obstruction is exact on legal configurations.  The 120-point
  distance-Sidon heavy row has 948 relations, affine rank 119, and centered
  rank 118: both are maximal (`k-1` and `k-2`).  On four role copies it uses
  478 active columns and has raw/centered ranks 473/472.  Hence no theorem
  based only on the sparse support and ordinary rank can close the row gate.
- Added `FIXED_ROW_DESIGN_MATRIX_AUDIT.md` and
  `verify_fixed_row_design_matrix_audit.py`.  The exact verifier checks the
  heavy and strict-diameter witnesses, all ranks, role-pair overlap one, and
  merged actual-label overlap at most twelve; all tests pass.  The surviving
  possible use is a new radial-rigidity or ambient-height theorem, not rank
  alone.  No new exponent is claimed; #1208 remains open.

### 2026-08-18 (latest) — ERDŐS #1208 dense-core and orthogonal-array inverse gate (Sihao + Codex)
- Proved an exact pruning lemma for the corrected dense-row branch.  A fixed
  row with `r` relations contains at least `r/2` relations in a four-partite
  pair-linear core of minimum active role-degree `r/(8k)`.  Hence a row of
  size `k^(1+epsilon)` has a genuinely growing-degree core, while the six
  fresh-endpoint biclique obstruction stays in the already-harmless linear
  branch.
- Proved that no nontrivial full transversal design can occur in a fixed row.
  Under its uniform edge distribution every pair of roles is independent;
  centering `U-V+JX-JY=d` and averaging its squared norm makes all mixed terms
  vanish and forces the sum of the four role variances to be zero.
- Quantified the obstruction: every noncollapsed fixed row has some pair
  projection with maximal correlation—equivalently degree-normalized second
  singular value—at least `1/6`.  Thus dense rows are hereditarily
  non-quasirandom in at least one projection.  The exact degree-only form is
  `sum_(ab in E)1/(deg(a)deg(b))>=1+1/36` for some projection; in a biregular
  graph this forces density at most `36/37`.  Correctly, this is a one-way
  Frobenius corollary and is vacuous at `r=k^(3/2)`; the constant second
  singular value is the nontrivial statement at that scale.  Turning it into
  a power-scale density increment or radial collision is the remaining step;
  no new final exponent is claimed.
- Added `DENSE_CORE_ORTHOGONAL_ARRAY_GATE.md` and the pure-stdlib exact verifier
  `verify_dense_core_orthogonal_array.py`.  The verifier checks pruning,
  pairwise orthogonality, and rational ranks for cyclic arrays of orders
  `3,5,7`; all tests pass.  No paid API batch; #1208 remains open.

### 2026-08-18 (latest) — ERDŐS #1208 six-biclique kill of the longest-book moment (Sihao + Codex)
- Corrected the immediately preceding checkpoint: the variable-longest book
  hypothesis is false, even after taking the minimum over all six fixed-row
  projections.  Around one realized row, plant six independent generic
  `K_(s,s)` relation gadgets, one for each role pair.  The union has
  `k=12s^2+12s+2` points and every projection has
  `binom(s,2)^2=Theta(k^2)` four-cycles.
- Proved the generic union can be distance-Sidon.  All points are
  Gaussian-linear forms in free complex variables.  Any forced edge-norm
  equality uses at most four row/column indices; the exact side-four symbolic
  template checks all 29,161 edges and finds distinct norm signatures.  The
  finitely many remaining nonzero distance/transversality polynomials can be
  avoided over the rationals and then scaled to integers.
- In each intended `K_(s,s)`, all rectangle charges land on at most
  `3s^2-s` selected-side or distinguished relation edges.  Cauchy therefore
  forces charge moment `Omega(s^6)=Omega(k^3)` in every projection, killing
  the proposed `k^(2+o(1))` moment by a full power.  The associated Hall/SDR
  idea is also false: at `s=10` there are 2,025 rectangles but only 1,890
  algebraically adjacent actual edges.
- The underlying fixed-row conjecture `min C_4<=k^(2+o(1))` survives and is
  now known to be exponent-sharp.  The six-gadget family identifies the
  necessary proof split: sparse rows/fresh endpoint bicliques are already
  harmless by `C_4<=r^2`; only dense rows with substantial endpoint reuse
  require a radial inverse theorem.
- Audited Solymosi's arXiv:2606.26311 small-distance theorem as a possible
  length-ordering input.  It assumes every pairwise distance is an integer
  and uses those distances as integer polynomial roots; square-grid subsets
  have only integral squared distances, so the theorem does not transfer.
- Added `verify_fixed_row_six_biclique.py` and corrected
  `FIXED_ROW_LONGEST_BOOK_GATE.md`.  The exact numerical side-eight instance
  has 866 distance-Sidon points, 384 fixed-row relations, and 784 four-cycles
  in each of six projections.  No paid API batch; full #1208 remains open.

### 2026-08-18 (latest) — ERDŐS #1208 variable-longest fixed-row book gate (Sihao + Codex)
- Refined the fixed-row six-projection `C_4` gate by charging every projection
  rectangle to its unique longest variable actual edge, excluding the fixed
  row edge.  If the book loads are `c(g)`, the exact Cauchy implication
  `sum_g c(g)^2<=k^(2+o(1)) => C_4<=k^(2+o(1))` gives the earlier conditional
  `r(d)<=k^(3/2+o(1))` and wide-branch exponent `2/5`.  This moment input is
  not proved.
- Exact adversarial tests are sharply consistent with the new scale.  Across
  all six projections, the 120-point heavy row has maximum charge moment
  15,126 = `1.0504 k^2`; the 90-point strict-diameter row has maximum 5,215
  `<k^2`.  The largest charge classes have 44 and 34 pages and are genuine
  `C_4` books centered on one common relation.
- Killed three plausible shortcuts.  The affine quarter-turn map has ten
  fully occupied four-orbits in the heavy witness; 11,850 of 11,852 projection
  cycles occur in only one projection; and the 948 heavy-row Gaussian-linear
  relations have exact rank 118 on 120 variables, so the configuration is
  already rigid up to similarity without repeated distances.
- Tested the three-factor integer-parabola construction.  The first 1,000
  consecutive points have all 499,500 distances distinct, and the direct
  number-field adaptation loses its local branching to quartic height.  This
  is a killed construction lane, not a universal theorem about parabolas.
- Added `FIXED_ROW_LONGEST_BOOK_GATE.md` and
  `verify_fixed_row_longest_book_gate.py`; exact audit passes.  No paid API
  batch.  Full #1208 remains open; next target is an `A^2`-scale count for
  pairs of rectangle pages sharing their variable-longest charge.

### 2026-08-18 (latest) — ERDŐS #1208 fixed-row six-projection `C_4` gate (Sihao + Codex)
- Reorganized one fixed transverse row `d=(u-v)+J(x-y)` as a four-partite
  pair-linear relation system.  Every two coordinate roles determine the
  entire relation, so all six two-coordinate projections are simple
  bipartite graphs on `k+k` vertices with exactly `r(d)` edges.
- Proved the exact conditional implication: if one projection has
  `C_4<=k^(2+o(1))`, then `r(d)<=k^(3/2+o(1))`.  Uniformly over rows this gives
  `T<=k^(7/2+o(1))`; combined with Elekes in the wide regime and the exact
  translate-union thinning inequality, it yields the conditional grid bound
  `k<=m^(4/5+o(1))`, i.e. exponent `2/5` for `n=m^2`.  The `C_4` input is not
  proved, so this is an intermediate gate rather than a new upper theorem.
- Exact adversarial profiles sharply support the gate.  The heavy fixed row
  reaches 948 relations at `k=120`, while its six projection cycle counts are
  only 1,869--2,071 and maximum pair-codegree is eight.  The strict global
  diameter row has 266 relations at `k=90`, cycle counts 230--473, and maximum
  pair-codegree nine.  Of the 11,852 distinct heavy-row projection cycles,
  11,850 occur in only one projection, so the six small counts are not one
  duplicated family.
- Classified row--source cycles by the row difference
  `delta=g+Jh`.  Although `delta in D union JD` carries the largest pair
  codegrees, the generic class already contributes 19,883,439/29,370,111 =
  67.7% of the exact count at `k=60`.  A coordinate-degeneracy cleanup cannot
  prove the global gate.
- Added `TRANSVERSE_FIXED_ROW_C4_GATE.md` and
  `verify_transverse_fixed_row_c4.py`; the exact verifier passes.  The next
  inverse target is superquadratic rectangle mass forcing endpoint reuse and
  then a forbidden radial equality.  No full proof yet; no paid API batch.

### 2026-08-18 (latest) — ERDŐS #1208 row--source `C_4` gate and longest-diameter obstruction (Sihao + Codex)
- Recast the transverse row fourth moment as a bipartite row--source graph on
  `D` and `B=A+JA`.  If its unlabelled `C_4` count is `k^(4+o(1))`, an exact
  Cauchy/convexity calculation gives the cubic transverse bound.  Exact heavy
  closure counts through `k=60` stay on scale; a separate 45-point witness has
  source degree 250, and endpoint-overlap cleanup accounts for only 10.6% of
  the 60-point cycles.  The fifth incidence in the translation-slice formula
  is load-bearing.
- Tested the new idea of charging every relation `d=f+Je` to its unique
  longest edge.  It would have solved the wide branch if every edge had
  `k^(1+o(1))` load.  A purpose-built closure keeps `(10000,0)` as the strict
  global diameter and extends exactly to 90 distance-Sidon points.  Its fixed
  diameter row is `61,90,180,266` at `k=35,45,70,90`, stably about
  `0.30 k^(3/2)`; total diameter charge is `1124=1.316 k^(3/2)` at `k=90`.
  Thus longest-edge pointwise charging is unsafe even at the global diameter.
- Rigorously killed the associated two-forest proof: diameter-row union ranks
  are 83/90 at `k=45` and 173/266 at `k=90`; four longest-column families also
  fail in the old 120-point witness.  The 90-point global total is still
  `336428=0.4615 k^3`, and the longest-charge second moment is
  `50120272=0.764 k^4`.  The survivor is a moment/rich-tail theorem, not an
  `L^infinity` theorem.
- New exact artifacts:
  `TRANSVERSE_ROW_SOURCE_C4_GATE.md`,
  `verify_transverse_row_source_c4.py`,
  `TRANSVERSE_LONGEST_EDGE_CHARGE_AUDIT.md`,
  `analyze_transverse_longest_charge.py`, and
  `verify_transverse_longest_charge.py`.  Both default verifiers pass.
- No full proof yet.  Best next attack: a structural inverse theorem for a
  *large tail* of charged edges / row--source four-cycles, followed by the
  still-missing intermediate line-rich splice.  Approximate spend: local
  exact computation only; no paid API batch recorded.

### 2026-08-18 (latest) — ERDŐS #1208 spectral shortcuts audited and killed (Sihao + Codex)

Continued the full-resolution attack from the row--colour fourth-moment gate.
The exact heavy-row closure witness was extended and calibrated through 120
points.  It remains distance-Sidon with maximum collinearity three, has
`T=2,798,384`, row moment `726,091,848=3.502k^4`, column moment
`718,246,448=3.464k^4`, wedge count `361,646,732=1.744k^4`, and rotated
support `1,011,786=0.586k^3`.  Thus the global exponent target survives while
the local maximum, fixed degeneracy, and coefficient-one wedge injection do
not.

Identified the exact direct-sum interpretation `B=A+JA`: distance-Sidonicity
makes `A x A -> B` injective, and the wedge moment counts decorated
parallelograms in `B` whose translation side lies in `A-A`.  This isolates the
live theorem as an average-multiplicity bound `W<=k^(4+o(1))` rather than a
pointwise statement.

Audited a spectral strengthening.  Although `||B||_op<=k^(1+o(1))` would
suffice, its Schur row-sum version is strongly threatened.  The fixed heavy
row's exact two-step mass grows from `36,740=10.206k^2` at `k=60` to
`276,604=19.209k^2=1.753k^(5/2)` at `k=120`.  Numerical operator norms rise
from `1.689k` to `2.268k` over the same range.  Also derived the exact
restricted five-incidence energy identity; deleting its final `1_D` factor
gives `sum_qR_D(q)R_D(Jq)`, which exact tests show on a `k^5` rather than
`k^4` scale.  Consequently local two-step and unrestricted Fourier/BSG
proofs are retired.  New durable artifacts:
`TRANSVERSE_SPECTRAL_AUDIT.md` and
`verify_transverse_spectral_audit.py`.  No full proof is claimed; the two
remaining theorem-level obligations are the global fourth-moment bound and
the intermediate line-rich splice.  Approximate external spend: none.

### 2026-08-17 (latest) — ERDŐS #1208 sharp wedge inequality killed; parallelogram gate isolated (Sihao + Codex)

- **Closure extended and re-certified.**  The deterministic heavy-row chain
  now has 120 exact integer points, all pairwise distances unique.  Its global
  profile is `T=2,798,384`, maximum row 948, row moment `726,091,848`, column
  moment `718,246,448`, support `1,011,786=0.5855...k^3`, and maximum
  collinearity three.  The relation-hypergraph degeneracy reaches 13.
- **Sharp coefficient falsified.**  For `W=sum_d binom(r(d),2)`, the proposed
  inequality `W<=(k-1)T` was nearly tight at `k=100` (ratio `0.997743...`) but
  fails at `k=120`: `W=361,646,732=1.74405...k^4`, with
  `W/(119T)=1.086001...`.
  This is an exact counterexample, not floating-point evidence.
- **Surviving theorem.**  An absolute-constant estimate `W<=CkT` would
  suffice, but the exponent-critical target is only `W<=k^(4+o(1))`.  The
  exact direct-sum model `B=A+JA` identifies `W` with decorated parallelograms
  in `B` whose translation side belongs to `D=A-A`.  This is now the most
  concrete transverse lemma.  It is unproved,
  and a separate intermediate line-rich/transverse coupling would still be
  required for a complete solution.
- **Artifacts/state.**  Added `TRANSVERSE_PARALLELOGRAM_GATE.md`, extended
  both closure verifiers, and updated
  `TRANSVERSE_SECOND_MOMENT_GATE.md`, `TRANSVERSE_RELATION_CLOSURE.md`, and the
  handoffs.  Exact verifiers pass; direct API spend `$0`; no process running.

### 2026-08-17 (latest) — ERDŐS #1208 row--colour moment gate and dual closure adversaries (Sihao + Codex)

- **Exact variance reduction.**  Repackaged transverse relations as the
  `D x D` incidence matrix `B(d,e)=1_D(d-Je)1_(d dot e !=0)`.  Its row degrees
  are `m_tr(d)` and its column degrees fix the perpendicular edge.  Since
  `|D|<k^2`, either fourth-power second-moment bound
  `sum row^2<=k^(4+o(1))` or `sum column^2<=k^(4+o(1))` implies the desired
  cubic transverse count by Cauchy--Schwarz.  This is a rigorous reduction,
  not a proof of the moment conjecture.
- **Dual pointwise route killed at finite scale.**  A deterministic exact
  closure for `a-b-c+e=(1,0)` reaches a 65-point distance-Sidon set with one
  fixed column of size `1010=0.239...k^2`.  Nevertheless its maximum row is
  only 43, its row/column moments are `660,000` and `12,509,352`, and rotated
  support is `251,195=0.9147...k^3`.  Maximum collinearity is four.
- **Hybrid kill test passed.**  A second deterministic search pooled the
  fixed-row and fixed-colour closures.  At `k=45` it simultaneously realizes
  row 147 and column 292, but both moments remain on the critical scale
  (`0.683 k^4`, `0.809 k^4`) and support remains `0.727 k^3`.  The 90-point
  heavy-row witness likewise has both moments about `2.5 k^4`.
- **BSG route quantitatively parked.**  At `N=|D|`, an excess
  `T=N^(3/2+delta)` yields ordinary additive energy only `N^(2+2delta)`, so
  standard BSG has parameter `N^(1-2delta)` and guarantees a structured
  subset only on the `N^(2delta)` scale with polynomially large doubling.
  This cannot exclude allowed line pieces.  The next theorem must be a
  realizability-sensitive moment/tail estimate, followed by the still-open
  line-rich/transverse coupling.
- **Artifacts.**  Added `TRANSVERSE_SECOND_MOMENT_GATE.md`, two closure
  searches, and two exact verifiers; strengthened the 90-point verifier with
  the dual moment profile.  All three verifiers pass; direct API spend `$0`.
  #1208 remains unresolved; no process is running.

### 2026-08-17 (latest) — ERDŐS #1208 local-max reversal and global midpoint gate (Sihao + Codex)

- **Exact closure extension.**  Added a deterministic exhaustive
  relation-forcing search and extended the certified distance-Sidon chain from
  47 to 90 integer points.  The selected fibre reaches
  `m_(0,-1)=614=0.7191...k^(3/2)`; the normalized values remain in
  `[0.718,0.722]` from `k=70` through `90`.  Relation-hypergraph degeneracy
  rises from 8 to 9, 10, and 11 at `k=63,76,81`, so every fixed-degeneracy
  formulation is false.  This is finite evidence, not an infinite
  counterexample to the `k^(1+o(1))` local bound.
- **Global target survives.**  On the same 90-point witness,
  `sum_d m_tr(d)=1,009,116`, hence
  `E_trans=504,558=0.6921...k^3`, while
  `|A+JA-JA|=446,638=0.6127...k^3`.  Thus the maximum-fibre sufficient
  condition is likely the wrong theorem, but the global cubic energy/support
  conjecture remains perfectly calibrated.  The next target is a tail or
  moment bound for the full overlap distribution.
- **Exact midpoint reformulation.**  If `d=a-b`, `d'=c-e`, and
  `J(d'-d)=x-y`, then for the unique midpoints
  `m_L=(a+e)/2`, `m_R=(b+c)/2` one has
  `x-y=2J(m_R-m_L)`.  This gives an equivalent decorated-midpoint incidence
  formulation; pairs whose first two edges meet already cost `O(k^3)`.  The
  disjoint cross-pairing term is the true global incidence problem.
- **Prior-art/shortcut audit.**  Elekes's deltoid theorem does not apply: a
  distance-Sidon set contains no genuine deltoid, while the relation compares
  an edge with a segment between midpoints.  Midpoint-growth results likewise
  do not control the endpoint decoration or transverse determinant.  No
  direct prior theorem was found.
- **Artifacts and state.**  Added `search_transverse_closure.py`,
  `verify_transverse_closure_global.py`, and
  `TRANSVERSE_GLOBAL_MIDPOINT_GATE.md`; extended the original closure
  certificate and corrected all #1208 handoffs.  Both exact verifiers pass.
  #1208 remains unresolved; no process is running; direct API spend `$0`.

### 2026-08-17 (latest) — ERDŐS #1208 Welch rigidity and relation-closure stress test (Sihao + Codex)

- **Hereditary gate classified.**  For fixed `d=p-q`, local solutions
  `u-v+J(x-y)=d` form a four-role linear relation hypergraph.  The statement
  `|F|<=|V_d(F)|^(1+o(1))`, with `p,q` adjoined to the endpoint union, is
  explicitly **equivalent** to the local transverse theorem, not a reduction.
- **Welch control.**  Full vector-Sidon Welch hosts have quadratic local
  overlap (`6887,27474,114191` at `N=126,250,508`), but exact distance-Sidon
  subsets retain maxima only `43/25`, `68/40`, and `94/55`.  Exact modular
  Gaussian row reduction gives rank `N-2` at `N=30,60,126`; the full
  quadratic relation systems are rigid up to similarity, so a global linear
  deformation cannot separate their forced repeated lengths.  The sampled
  codimension-one audit is reproducible and explicitly non-exhaustive.
- **Purpose-built closure adversary.**  Greedily adjoining integer points
  forced by one quarter-turn relation, while rejecting every repeated squared
  distance, produced a certified 47-point set with `m_(0,-1)=237`.  This kills
  `m_d<=2k+O(1)`.  Its 17-point core has 29 relations but projected graphic
  ranks only `13+13`, so the proposed two-forest/matroid charge is also false.
- **Viability signal and next target.**  The full 47-point relation
  hypergraph is exactly 8-degenerate.  Thus the asymptotic
  `k^(1+o(1))` gate survives its strongest current falsification test; the
  right next experiment/proof is hereditary `k^(o(1))` degeneracy.  A family
  with core degeneracy `k^epsilon` is the honest kill, whereas a growing
  global constant is not.  Exact artifacts are
  `WELCH_TRANSVERSE_SUBSET_AUDIT.md`,
  `verify_welch_relation_rigidity.py`,
  `TRANSVERSE_RELATION_CLOSURE.md`, and
  `verify_transverse_closure_witness.py`.
- **Prior art and state.**  Targeted searches found no direct-sum,
  rotated-segment, Costas-rigidity, or sparsity-matroid theorem supplying the
  missing radial degeneracy estimate.  #1208 remains unresolved.  No process
  is running; direct API spend `$0`.

### 2026-08-17 (latest) — ERDŐS #1208 local transverse gate isolated (Sihao + Codex)

- **Exact localization.**  For `D=A-A`, defined
  `m_tr(d)=#{e in D\{0}:d-Je in D, d dot e != 0}` and proved
  `2E_trans=sum_d m_tr(d)`.  Thus the local estimate
  `max_d m_tr(d)<=k^(1+o(1))` is sufficient for the remaining global
  transverse-collision theorem.  The dot-product restriction deletes exactly
  the perpendicular-ruler obstruction.
- **Structured and graph consequences.**  If `A` lies on `r` parallel lines,
  proved `m_tr(d)<=|H-H|^2<=r^4`.  Also derived
  `E=O(N^(3/2)+NQ^(1/4))` for a transverse graph with `N` vertices and `Q`
  four-cycles, so `Q<=k^(4+o(1))` is a second sufficient gate.
- **Targeted falsification.**  Exact simulated annealing maximizing the local
  overlap found maxima `22,31,35` for `k=12,16,20`; the worst observed ratio
  was `31/16`.  No superlinear trend appeared.  All retained witnesses and
  local/global, quarter-turn, line-cover, and four-cycle identities have exact
  checkers.  Affine row-rank alone was ruled out as a proof mechanism.
- **State at close.**  #1208 remains unresolved.  The new local theorem is the
  sharpest live gate; a fixed-power superlinear family kills it.  The next
  proof must exploit endpoint reuse and uniqueness of Euclidean lengths.  No
  process is running; direct API spend `$0`.

### 2026-08-17 (later) — ERDŐS #1208 adversarial support search and wide-case reduction (Sihao + Codex)

- **Adversarial viability test completed.**  A deterministic exact-integer
  annealing search minimized `|A+JA-JA|/|A|^3` over distance-Sidon lattice sets.
  Certified witnesses of sizes `12,16,20,24,28` have ratios from `0.626` to
  `0.703`; no decaying family was found.  This supports, but does not prove,
  cubic rotated support.  The search, fixed witnesses, and independent verifier
  are in `phase2/loop/erdos1208/ADVERSARIAL_ROTATED_SUPPORT_SEARCH.md`.
- **Exact structured-case theorem.**  For occupancies `k_h` on parallel lines,
  `Q=sum_h k_h(k_h-1)`, and `p` occupied projections, proved
  `|A+JA-JA| >= k+pQ`.  Hence a set contained in `r` parallel lines has support
  at least `k^3/r^2-k^2/r+k`.  The proof and exact finite checker are in
  `PARALLEL_LINE_SUPPORT_LEMMA.md` and `verify_parallel_line_support.py`.
- **Wide-case gate isolated.**  Random thinning of translate blocks gives an
  exact lower bound in terms of their collision graph.  Elekes's 2019
  trapezoid theorem supplies `k^(3+o(1))` control of the parallel collisions in
  the wide regime.  The remaining new theorem is
  `E_trans(A) <= k^(3+o(1))` for wide distance-Sidon sets; a family with
  maximum line occupancy `k^(o(1))` and `E_trans >= k^(3+epsilon)` is the
  pre-registered kill condition.  The intermediate structured/wide splice is
  also not yet closed.
- **Misleading finite-field lead killed.**  The old four-row `q=5` pattern used
  diagonal/off-diagonal collisions, which distance-Sidonicity already forbids.
  A genuine off-diagonal alternating three-cycle is also forbidden (Gaussian
  determinant `4`), but there is no theorem forcing it from small support.
  Exact audit: `COLLISION_PATTERN_AUDIT.md` and
  `verify_collision_patterns.py`.
- **State at close.**  This is a sharper route, not a solution of #1208.  The
  next proof lane is the transverse-collision estimate, with the line theorem
  as its structured branch.  No process is running; direct API spend `$0`.

### 2026-08-17 (later) — ERDŐS #838 morning campaign; independent Claude audit of both fronts; colleague note to Sol (Sihao + Claude)

- **#838 morning campaign (Sol/Codex, six `agent_*` directories, committed 10:42).**
  Attacked exactly the two honest residues left on 2026-08-16.  New positive tool:
  an exact random-bipartition minimizer inequality (Gibbs form `W <= G_p + Z_p`),
  strengthened to an exact closed-form for every number `q` of ordered blocks —
  the first genuine multi-point mutation inequality of the campaign.  Its scope is
  proved sharp: fixed `q>=4` returns the apparent saving, `q=3` helps only on the
  extreme tail, and the `2^-rank` Gibbs weight mismatches the polylog endpoint
  surplus.  Ledger row M5 records this as a BARRIER.  Separately: all-pairs
  cap–cup converters are impossible (exact quadratic-load pigeonhole, attained on
  a 12-point calibration); the weighted-hinge conjecture `(WH)` is falsified with
  a certified defect interval while the averaged square mesh `(ASM)` survives;
  the C2 mesh theorem extends to arbitrary-depth polynomial imbalance.  The sole
  surviving positive target is a *selected endpoint reset* (inverse-polylog
  density, `O(log L)`-entropy differences) — see
  `agent_common_shield_mixing/POLYLOG_CAP_CUP_CONVERTER_MUTATION_GATE.md` §4 and
  `PROGRESS_BAR_20260817.md` (architecture ~88%, completed-proof ~45%,
  unconditional coefficient gain still **zero**, window `[1/4,1/2]`).
- **Independent audit (Claude/Fable).**  Re-ran and confirmed
  `verify_frobenius_all_depth_rank715.py` (CERTIFIED, margins > 3.05),
  `verify_perpendicular_rulers.py` (PASS), and
  `verify_polylog_cap_cup_converter_mutation_gate.py` (PASS, all exact counts
  reproduced).  Assessment: #1208 overnight = one certified incremental theorem
  plus a decisive falsification sweep that leaves one clean surviving target;
  #838 = same track, much better lit — the remaining step likely needs a new
  idea, and the empirical near-minimizer program should precede more barriers.
- **Colleague guidance filed.**  `NOTE_TO_SOL_20260817.md` (repo root, pointer in
  AGENTS.md §Inbox): keep the self-falsification discipline; break the
  "surviving-statement treadmill" via pre-registered viability tests and
  mandatory reformulation classification (reduction / restatement / new bet);
  data-before-proof programs for both fronts; bank the standing debts (838 draft
  section, 1208 interval-arithmetic + human audits + LPZ priority check,
  cross-model examination of both crux chains); portfolio stop rule (two
  consecutive barrier-only sessions on one front → switch or write up).  Sol's
  10:42 HANDOFF update already adopts the viability-test and adversarial-search
  framing for the #1208 rotated-support target.
- **State at close:** all work committed and pushed; no process running; no API
  spend this session.  Open items for humans: restore or reconstruct the missing
  `SOL_DIRECTIVE_1208_20260816.md`; decide the front split for the next sessions
  (suggested: #1208 rotated support as primary, #838 empirical minimizer program
  as secondary).

### 2026-08-17 — ERDŐS #1208: explicit 0.494586 bound and rotated-support frontier (Sihao + Codex ultracode)

- **Rigorous partial upper candidate.**  Prime-power valuation flags,
  placewise depths, Frobenius-order-two quotients, and a globally interleaved
  depth path now give `F_2(n) << n^0.494586`, conditional on the declared tame
  Shafarevich presentation theorem and symbolic Minkowski-grid master bound.
  `verify_frobenius_all_depth_rank715.py` checks rank 715, 127,091 useful
  primes, the strict relation budget, the root-discriminant data, all depth
  slopes, and endpoint margins exceeding 3.05.  This improves the local
  explicit exponent but does not resolve #1208.
- **Full-resolution reduction.**  For distance-Sidon `A subset [m]^2` and the
  quarter-turn `J`, the surviving target is
  `|A+JA-JA| >= |A|^(3-o(1))`.  It would give the expected grid-scale upper
  `|A| <= m^(2/3+o(1))`, matching the published `n^(1/3)` lower bound.  The
  fibres are induced tri-coloured matchings and the translate-incidence graph
  is `C_4`-free.
- **Barriers and controls.**  A quantitative perpendicular dense-Golomb-ruler
  family is distance-Sidon yet has fourth-power rotated energy, sixth-power
  cross energy, quadratic pointwise overlap, and many short-cycle witnesses.
  It kills size-only energy/overlap, biclique, and fixed-girth routes while
  retaining cubic support.  Unstretched Costas sets show vector-Sidonicity is
  insufficient; norm-unique stretched Costas sets have support ratio rising to
  about `0.983` at size 60.  Random-greedy and exhaustive small-grid tests also
  show no subcubic trend.
- **Latest exploratory lead.**  A `q=5` Gaussian-rational model contains four
  actual collision rows whose linear span includes a forbidden radial
  equality.  The missing theorem is extremal: subcubic support has not been
  shown to force that or any equivalent finite certificate.  The calculation
  is recorded as in-flight evidence, not a result.
- **Next actions and claim boundary.**  Run an adversarial search minimizing
  `|A+JA-JA|/|A|^3`, then attack a line-structured/transverse or radial
  uncertainty theorem.  Separately replace Decimal by directed intervals,
  obtain two human proof audits, and clear priority before circulating the
  `0.494586` note.  Seventeen #1208 commits were prepared for push; no process
  is running.  Approximate direct API spend: `$0`.

### 2026-08-16 — ERDŐS #838: progress bar checkpoint and cyclic-stem audit (Sihao + Codex)

- Preserved the original seven-component progress-bar breakdown in
  `phase2/loop/erdos838/PROGRESS_BAR_20260816.md`.  Current architecture
  estimates are `100/95/95/95/100/60/not-yet` for prior art, recursive
  threats, minimizer/root reduction, local structure, canonical $E(k,k)$
  decoder, arbitrary global decoder, and assembled proof.
- Kept the two metrics separate: approximately `80%` of the obstruction and
  proof architecture is mapped, while the unrestricted coefficient remains
  rigorously unchanged at `[1/4,1/2]`.  The document uses about `40%` only as
  a conservative planning estimate for the completed proof, not as a
  mathematical invariant.
- Audited the proposed cyclic-minimal-stem continuation against the existing
  antimatroid/Tutte packages.  Gordon's one-root exposure formula, the
  bivariate Boolean-interval identity, and the random-hull exponential-moment
  formulation were already banked.  Exact nested-triangle and outer-shell
  barriers kill the scalar/onion/Kraft versions.  No new theorem or renamed
  reduction was added.
- The only honest coefficient-bearing exits remain direct averaged P1d, or a
  multi-point minimizer mutation/profile inequality with a checked fixed
  gain.  Approximate direct API spend: `$0`; no process left running.

### 2026-08-16 — ERDŐS #838: concentrated-pocket splice killed; global all-delete gate isolated (Sihao + Codex)
- **Exact gain ledger:** at `N=4^k`, partial replacement of a rank-`alpha k`
  source after deleting `delta k` labels has exponent
  `1+2alpha-2alpha^2-2(1-alpha)delta-delta^2` under the hoped-for decoder.
  The critical choice `(alpha,delta)=(1/2,1/4)` gives `19/16>1`; complete
  deletion gives only `3/4`.
- **Exact planar kill:** a new integral 12-point certificate has a convex
  four-point source and convex four-point pocket.  Every pocket label is
  individually addable through the same exposed source edge, but the whole
  pocket is nonconvex with each of the 15 nonempty source traces.  Thus no
  universal bounded-deletion merge follows even from perfect one-edge
  concentration.  The report and verifier are
  `P1D_CONCENTRATED_POCKET_REPLACEMENT_BARRIER_20260816.md` and
  `verify_p1d_concentrated_pocket_replacement_barrier.py`.
- **Cross-route audit:** mutually-avoiding/same-type extraction is already
  banked at a coefficient-one ceiling.  Joint mixed-Hall assembly already
  controls global output overlap once a reservoir exists and passes the
  matching-star and `E(k,k)` regressions.  A proposed scalar tail-entropy
  derivation of the averaged square mesh is false on a two-scale alphabet
  by `2.7096...` bits, so threshold Kraft alone cannot erase predecessor
  identity.
- **Decision:** preserve the local arithmetic and barrier; do not open a
  new deletion-fraction or threshold surrogate.  The remaining
  coefficient-bearing operation is a joint all-delete/rooted-pocket code
  with `n^{o(1)}` load and recovery fibre, or a genuinely multi-point
  minimizer mutation/profile inequality.  The unconditional window remains
  `[1/4,1/2]`.  Current web prior-art check still lists #838 as open.
  Approximate direct API spend `$0`.

### 2026-08-16 — ERDŐS #838: strict minimizer-mean route stress-tested and parked (Sihao + Codex)
- **Direct gain target audited:** for a global minimizer, the exact deletion
  identity shows that `mu>=(1/2+epsilon)log_2 n` would improve the lower
  coefficient to `1/4+epsilon/2`.  A closure-lattice sufficient condition
  `E B<=(1-delta)mu^2` was isolated with its exact coefficient implication.
- **Exact stress theorem:** a new verifier reconstructs every convex face and
  closed hull from the certified rational n=44 and n=58 reflection-order
  records.  It finds `E B/mu^2=1.100265...` and `1.350137...`, rigorously
  killing even the coefficient-one blocked bound for arbitrary planar point
  sets.  Exact n=8,9 global minimizers remain compatible with the
  minimizer-only conjecture.
- **Second reduction audited:** the deletion variance ladder has critical
  average `1/(2 ln 2)=0.721347...`, but exact balanced Pascal cells have
  variance tending to zero.  Restricting to low-mean descendants requires the
  already-parked hereditary positive-rank-interval theorem P1d.
- **Decision:** apply the written two-reduction stop rule.  One-point
  minimizer relocation has the anti-converting sign and a useful repair needs
  the existing multi-point mutation problem; the variance route is P1d.  No
  lower-coefficient improvement is claimed.  Preserve the strategy, autopsy,
  and exact verifier; do not relabel the half-weight or strict-mean forms as a
  new route.  Rigorous window remains `[1/4,1/2]`.  Spend approximately $0
  direct API.

### 2026-08-16 — ERDŐS #838: exact-size P1e counterexample and fixed-size stop rule (Sihao + Codex)

- **P1e is false with its quantifiers fixed.** For every prescribed
  certified `q_j>=ES(j+1)`, `log q_j=j+o(j)`, a rational exact-size
  strong-glue family has
  `log(v_j/v_(j+1)) >= (1-1/(4 ln2)-41/70-o(1))j^2`; the positive constant
  is `0.053611954...`.
- **Construction.** The numerator is the exact top layer of the central
  Pascal cell `T(j,j/2)`. The exact-size padding is an induced subset of a
  homogeneous tower built from the first `2^35` leaves of `T(41,27)`.
  Its cup and total-face coefficients are `1/5` and `41/70`, so neither the
  padding nor the mixed cap-cup term repairs the cliff.
- **Verification.** `verify_fixed_threshold_adjacent_counterexample.py`
  reconstructs both exact integer recurrences. The strong-glue lower bound
  becomes positive by padding depth five and exceeds 1600 bits at depth
  eight. The prior threshold verifier still passes all 3,567 averaging and
  construction regressions.
- **Process decision.** The bounded P1 attack reached its precommitted kill
  rule after two failed local promotion candidates. P1 and the averaged P1d
  condition remain open, but no third threshold-layer surrogate will be
  opened. `FIXED_SIZE_BOUNDED_ATTACK_AUTOPSY_20260816.md` preserves the
  actual bridge/range/construction-class gains and parks the chain.
- **Status/spend.** The rigorous coefficient window remains `[1/4,1/2]`.
  Approximate direct API spend `$0`.

### 2026-08-16 — ERDŐS #838: adjacent-layer quantifier correction and exact Pascal barrier (Sihao + Codex)

- **Correction.** The adjacent-layer lemma must be stated at one fixed
  certified sequence `ES(j+1)<=q_j=2^(j+o(j))`; the earlier uniform-in-size
  reading and its proposed kill criterion were false.
- **Exact stretchable barrier.** For `j=2h-4`, a one-point cap promotion of
  the central Pascal cell has `C(j,j/2)+1=2^(j-o(j))` labels and
  `v_j/v_(j+1)>=a_h=2^Omega(j^2)`. Exact first ratios are `7`, `2713/46`,
  and `12410783/3421`; a verified Pascal recurrence continues through
  `h=20` and exact rational geometry is checked at `h=4,5`.
- **Consequence.** Any positive proof must use the actual oversaturation
  slack in the chosen Erdős--Szekeres upper-bound sequence, not merely the
  asymptotic statement `log q_j=j+o(j)`. Any disproof must hit that same
  sequence or all possible certified choices.
- **Padding stress.** Replacing every physical leaf of the promoted cliff,
  one at a time, by a larger central-Pascal child repairs the adjacent layer
  in all `1277` exact substitutions for `4<=h<=8`; the maximum surviving
  ratio is below `0.0112`. This is finite evidence for an
  oversaturation-to-mixed-extension theorem, not such a theorem.
- **Artifacts:** corrected
  `THRESHOLD_ADJACENT_LAYER_BALANCE_GATE_20260816.md`, its exact verifier,
  and the corresponding handoff/campaign/ledger entries. Approximate direct
  API spend `$0`.

### 2026-08-16 — ERDŐS #838: adjacent-layer balance reduced to one signed-planar lemma (Sihao + Codex)

- **Exact induced-subset averaging.** If every `q`-point restriction has
  `v_j<=L_jv_(j+1)`, then globally
  `p_(j+1)/p_j>=(j+1)/(L_j(q-j))`. Consequently, at
  `q_j=2^(j+o(j))`, any balance exponent `L_j=2^((lambda+o(1))j)` with
  fixed `lambda<1` yields the Stage-C decay constant `c=1+lambda<2` and
  unrestricted coefficient
  `1/4+(1-lambda)(1-alpha^2)/8>1/4`.
- **Kill-search survived.** Exact central Pascal profiles through parameter
  50, alternating combs through 1024 leaves, and the threshold double chain
  all have bounded/decreasing `v_j/v_(j+1)`, far below the forbidden
  `2^((1-o(1))j)` scale. The rational 16-point double chain still kills only
  the exact no-slack finite inequality, not this asymptotic gate.
- **Scope:** hereditary complexes fail catastrophically, so the missing
  input is specifically signed planar circuit geometry. The current route
  is an extension/one-hidden-vertex flip graph: prove that direct extensions
  or pocket-charged flip basins have congestion `2^((1-epsilon)j+o(j))` for
  some `epsilon>0`.
- **Artifacts:** `THRESHOLD_ADJACENT_LAYER_BALANCE_GATE_20260816.md` and
  `verify_threshold_adjacent_layer_balance.py` (`PASS`: 3,567 averaging
  identities plus exact construction regressions). Approximate direct API
  spend `$0`.
- **Honest status:** coefficient window remains `[1/4,1/2]`; P1e is
  conjectural and is now the sole active child of P1d. Park it if the next
  geometric reduction does not produce an explicit saving.

### 2026-08-16 — ERDŐS #838: mass-truncated square mesh + uniform caterpillars + exact rank-density gate (Sihao + Codex)

- **Local heterogeneous loss sharpened.** Ordinary hinged Kraft on one
  mass-truncated child alphabet proves
  `max_i((log n_i)^2/2+R_i)>=L^2/2-O((log m+log L)^2)`. This removes the
  earlier harmonic `L log log m` loss. The stronger normalized weighted
  Kraft shortcut is false on an exact rational five-point chart and is
  separately banked.
- **Growing-rank finite error solved.** For every full binary tree,
  `R_k(T)>=b_k(n-2^(k-2))_+^k`; at `n=4^k` this has exponent
  `3k^2/2+O(k)`. The exact ordered endpoint formula was also proved. Its
  same-constant plane analogue is false on a 256-leaf alternating comb, so
  the honest residual is a shifted/excess orientation comparison rather
  than another finite-size estimate.
- **Strict Stage-C target quantified.** For `p_j=v_j/C(N,j)`, `N=4^k`,
  and `r=alpha k`, an average density-decay coefficient `c<2` between ranks
  `r` and `k` gives
  `eta=(1-c/2)(1-alpha^2)>0` and unrestricted coefficient
  `1/4+eta/4`. The exact no-slack inequality
  `p_(j+1)>=2^-j p_j` survives the saved minimizer, ordered-tree, and
  vertical-Pascal regressions, but an exact rational 16-point double chain
  kills it at the natural threshold: `(v4,v5)=(924,112)` and
  `p5/p4=5/99<1/16`. This does not kill the active supersaturated
  asymptotic form with `2^-o(k)` slack: the row lies outside
  `N=4^k,j<=k`, and later double-chain rows have constant-size density
  loss. The averaged strict `c<2` target remains live.
- **Artifacts:** `TRUNCATED_WEIGHTED_KRAFT_SQUARE_MESH_20260816.md`,
  `WEIGHTED_NORMALIZED_KRAFT_BARRIER_20260816.md`,
  `UNIFORM_GROWING_RANK_ROOTED_CATERPILLAR_THEOREM_20260816.md`,
  `SUCCESSIVE_RANK_DENSITY_GAIN_GATE_20260816.md`, and four exact verifiers.
  All PASS; approximate direct API spend `$0`.
- **Honest status / next action:** the coefficient window remains
  `[1/4,1/2]`. Attack the highly supersaturated cross-rank extension graph
  only at `N=4^k`; beat decay constant two or obtain an equivalent
  one-face circuit/profile charge. The near-threshold pointwise conjecture
  and raw two-target deletion map are parked as full-strength/equivalent.

### 2026-08-16 — ERDŐS #838: fixed-size prior-art ceiling + harmonic square mesh (Sihao + Codex)

- **Prior-art kill-search completed for the live P1 target.** Aichholzer et
  al.'s `Theta(N^k)` count is explicitly fixed-`k`; ordinary
  Erdős--Szekeres double counting gives only `2^(k^2-o(k^2))` at `N=4^k`;
  and a single positive-fraction transversal box cannot cross that main
  coefficient because the optimal universal block fraction is at most
  `2^{-k+o(k)}` (Bárány--Valtr; Pór--Valtr).
- **Exact algebraic ceiling:** for every cutoff `r`, the Huemer--Oliveros--
  Pérez-Lantero--Torra--Vogtenhuber weighted polygon identity admits the
  integral nonnegative ledger `X_(j,0)=C(N,j)` for `3<=j<r`,
  `X_(r,l)=C(N-l-1,r-1)`, and zero above `r`. It has maximal counts at every
  rank through `r` but no higher face. Scalar hull identities cannot force
  the growing-rank gain; a new input must encode cross-rank planar
  compatibility.
- **New proved local theorem:** threshold the exact hinged Kraft theorem by
  the `j` largest children. With weighted endpoint rewards `R_i`, total `N`,
  and `H_m=sum_(j<=m)1/j`,
  `max_i((log n_i)^2/2+R_i)>=(log N-log H_m)^2/2-(log m)^2/2`.
  Different thresholds may use completely different witnesses; their total
  switching cost is only `O(log N log log(m+1))`. This replaces the
  conjectural local square mesh up to a lower-order harmonic term, but does
  not charge the term recursively or promote arbitrary point sets to a
  same-chart decomposition.
- **Artifacts and verification:**
  `FIXED_SIZE_SUPERSATURATION_PRIOR_ART_AUDIT_20260816.md` plus verifier
  (`238,560` fake-ledger rows, `631` geometric rows, `27,066` exponent rows),
  and `HETEROGENEOUS_THRESHOLD_SQUARE_MESH_GATE_20260816.md` plus verifier
  (`450,000` weighted instances, `1.8M` threshold checks, `50,000` arithmetic
  rows). Both PASS; pycompile and diff checks pass. Approximate API spend `$0`.
- **Honest status / next action:** unrestricted Erdős 838 remains open with
  coefficient window `[1/4,1/2]`. Attack the selected-family convex-four-set
  circuit geometry above the quarter-log decoder boundary. Do not revisit
  fixed-`k` asymptotics, one same-type box, scalar weighted identities, or
  nested threshold witnesses.

### 2026-08-16 — ERDŐS #838: explicit quarter-log decoder boundary (Sihao + Codex)

- **New exact range theorem:** if `ES(k)<=2^(k+G_k)`, then at `n=4^k` all
  literal histories through rank `floor((k-G_k)/2)-3` pool simultaneously
  into actual convex `k`-faces with physical load and recovery fibre one.
- **Best current threshold inserted:** Holmsen--Nassajian Mojarrad--Pach--Tardos
  give `G_k=O(sqrt(k log k))`, so the covered range is now
  `r<=1/4 log n-O(sqrt(log n log log n))`. This replaces the previous
  fixed-epsilon statement by an explicit approach to the structural
  quarter-log capacity boundary.
- **Honest status:** no coefficient gain; the unrestricted window remains
  `[1/4,1/2]`. Crossing the boundary requires selected-family sparsity, a
  larger configuration-specific bank, or a mixed/profile charge; improving
  `ES(k)` alone cannot do it.
- **Artifacts:** `FIXED_SIZE_LITERAL_EXPLICIT_BOUNDARY_20260816.md` and
  `verify_fixed_size_literal_explicit_boundary.py`. Exact verifier PASS:
  `exact=314821, improvement=677417, base_change=11910, blocks=8126`.
  Approximate direct API spend: `$0`.

- **V3 independent audit:** reconstructed and passed the exact hull-root
  recurrence, weighted increment `K_{n,1}`, cumulative half-growth
  normalization, endpoint moment/Pareto gate, and corrected projective
  `n=8,9` reset. The two exact suites passed, including the full `B(8,2)`
  scan and all 483 root charts/6,984 shellings of the true nine-point
  minimizer. V2 and V4 are now the only frozen verification packages.
- **New minimizer increment theorem:** for the exact weighted root optimizer,
  `K_(n,1)>=ceil(m_n(f(n))/n)+n-1`. The verifier passed 1,755,273 exact
  rank/ledger/asymptotic rows. At coefficient `c` this supplies only
  `(c+o(1))f(n)log n/n`, so it does not move `[1/4,1/2]`; it proves that a
  successful root proof needs cross-chart/profile correlation beyond summed
  deletion moments.
- **V4 independent audit:** reconstructed and passed causal curvature
  transport, the forced native-cap collision, the weighted child-excess gate,
  and the universal post-collision remapping bound. Any full tagged-ledger
  decoder into ordinary faces has fibre `(1-o(1))` times total shelling
  weight; only sparse child-excess or a genuinely larger ordinary-output bank
  remains. Both exact transport/max-flow suites passed. V2 is now the sole
  frozen verification package.
- **V2 independent audit / freeze cleared:** proved that every permitted
  separated `E(r,s)`, reflection, perfect-reset power, and arbitrary recursive
  substitution expands by grafting to one ordered strong tree. The already
  audited all-tree theorem therefore forces coefficient `1/2` throughout
  that construction class. The exact rank/profile/nonstationary/Pareto suite
  passed. All five V1--V5 packages are now independently reconstructed.

### 2026-08-15 — ERDŐS #838: fixed-size bridge, V1/V5 audits, and quarter-log pooling gain (Sihao + Codex)

- **Exact gain bridge:** proved and verified that
  `mu_k(4^k)>=2^((1+eta-o(1))k^2)` improves the unrestricted coefficient
  from `1/4` to `(1+eta)/4`. The earlier loose `2^(2k+o(k))` shorthand is no
  longer used for the transfer.
- **Strong-tree narrowing:** proved the diffuse-comb/near-full-seam
  dichotomy. The diffuse branch gives `2^(2k^2-O(k log k))` rank-`k` faces;
  every survivor has a `4^k/poly(k)` by `4^k/poly(k)` seam. The exact
  plane-caterpillar audit found that known fixed-`k` unordered inducibility
  has the desired `3/2` main exponent but a dominating finite-size error and
  loses the required left/right itinerary.
- **Independent verification:** V1 is `MINOR_REPAIR -> repaired/PASS`; the
  missing bounded reachability from two retained child states to the two
  endpoint-maximizing cycles is now explicit. V5 is `PASS`: weighted Hall,
  recovery fibre, trace-bank incidence, pooled rank promotion, and the
  literal-rank ES code were reconstructed separately and four suites rerun.
- **New unconditional range theorem:** at `n=4^k`, Suk's
  `ES(k)=2^(k+o(k))` supplies enough actual convex `k`-faces to jointly code
  every literal history of rank `r<=(1/2-delta)k`, equivalently
  `r<=(1/4-delta/2)log n`, with load and fibre one. The live literal window is
  now `(1/4-o(1))log n <= r < log n`; the present universal total-capacity
  estimate stops at the lower boundary.
- **Truth status:** no unconditional coefficient improvement yet; the window
  remains `[1/4,1/2]`. V2--V4 still need independent reconstruction. The next
  bounded P1 attack must use selected-family sparsity, mixed geometry, or a
  profile charge above the quarter-log boundary. No process is running.
- **Artifacts:** `FIXED_SIZE_GAIN_BRIDGE_20260815.md`,
  `STRONG_TREE_FIXED_RANK_COMB_OR_SEAM_GATE.md`,
  `FIXED_RANK_STRONG_TREE_CATERPILLAR_AUDIT_20260815.md`,
  `V1_INDEPENDENT_AUDIT_20260815.md`, `V5_INDEPENDENT_AUDIT_20260815.md`,
  `FIXED_SIZE_LITERAL_QUARTER_LOG_POOLING_GATE_20260815.md`, and their exact
  verifier scripts. Approximate direct API spend: `$0`.

### 2026-08-15 — ERDŐS #838: external critique accepted; campaign frozen and distilled (Sihao + Codex)

- **Headline correction:** the 2026-08-14/15 campaign did not move the
  unconditional window `[1/4,1/2]`.  Its progress is a deep obstruction and
  route map, not “78% of the proof.”  Claude/Fable's constructive process
  critique is preserved at
  `phase2/loop/erdos838/CRITICISM_20260815_claude.md`.
- **No information was overwritten.**  The 12,980-line
  `FULL_ATTACK_20260814.md`, all agent reports, rational examples, and exact
  verifiers remain intact.  Added five compact navigation files:
  `CAMPAIGN_STATE_20260815.md`, `DIFFICULTY_LEDGER_20260815.md`,
  `VERIFICATION_QUEUE_20260815.md`, `BANKABLE_RESULTS_20260815.md`, and
  `PROVED_GAIN_STRATEGY_20260815.md`.
- **Discipline adopted:** every new target must have an explicit quantitative
  implication, strictness explanation, saved stress test, and kill criterion.
  Coefficient-equivalent branches stop immediately; three reductions without
  a gain trigger an autopsy rather than a fourth renamed target.
- **Five-package verification freeze:** hinged Kraft/variable grammar;
  recursive separated-template closure; minimizer hull-root recurrence;
  sparse curvature transport; and global Hall/low-rank ES replacement.  The
  many exact scripts are author-side checks, not independent cross-model proof
  audits.
- **One next proved-gain target:** for `n=2^(2k+o(k))`, prove
  `v_k(P)>=2^((1+eta-o(1))k^2)` for any fixed `eta>0`, which would improve the
  unrestricted lower coefficient to `(1+eta)/4`.  Two bounded attack/audit
  cycles are allowed; otherwise package the upper/strong-tree theorem and
  audited barriers.
- **Operational state:** no research process is running.  Approximate API
  spend for this distillation: `$0`.

### 2026-08-13 — ERDŐS #838: exact half-weight/stopping-time attack (Sihao + Codex ultracode)

- **Honest outcome:** unrestricted #838 remains open with rigorous base-two window `[1/4,1/2]`.
  The new primary synthesis is `phase2/loop/erdos838/HALF_WEIGHT_ATTACK_20260813.md`.
- **Full-strength scalar target isolated.**  For
  `Z_P(z)=sum_(A convex) z^|A|`, proving
  `H(P)=n Z_P(1/2)/Z_P(1)=n^o(1)` for minimizers implies
  `E|A|>=(1-o(1))log2 n`; the exact deletion recurrence then proves the missing lower coefficient
  `1/2`.  The clean stronger conjecture `H<=2` survives all exact and heuristic tests.
- **New random-prefix identity.**  If `R` is the last convex prefix of a uniform random
  permutation, then exactly
  `Z_P(z)=E[sum_(k<=R) binom(n,k)z^k]`.  Tilting `R` by the partial sum at `z=1` reduces the theorem
  to `E_*2^-R<=n^(-1+o(1))`.  In a planar order the first failure contains a rooted four-circuit
  involving the arriving point, producing a concrete tilt-preserving switching target.
- **Local shortcuts rigorously killed.**  Exact integer planar records at `n=24,30` refute
  `mu_(1/2)>=log2 n-1`, while retaining `H=1.686142,1.730215<2`.  A realizable long braid can
  improve `(V,M)` while worsening `Z(1/2)`.  Canonical visible-flip inverse fibres have half-weight
  `((3/2)^m-1)/4`, and a permissive one-step fractional flow fails on the exact `n=20` record by
  `893/4`.  The factor-one endpoint-span inequality also fails (`48/7<7`); constant-loss weighted
  cup--cap remains open.
- **Exact finite progress.**  Complete higher-Bruhat enumeration at `n=8` plus complete realizable
  order-type database scans through `n=9` certify the official values `f(8)=114`, `f(9)=169`
  (empty included).  The `n=9` minimizer has no lex-minimum child, killing hereditary lex induction.
  A new exact integer `n=20` set has profile `(1,20,190,1140,2415,866,135,8)` and `V=4775`, checked
  by both reverse products and direct enumeration of all `2^20` subsets.
- **Cyclic construction closed.**  The natural self-affine continuation of the exact `n=9`
  minimizer contains an all-depth binary convex-chain subsystem: at depth `2r+1` it has a convex
  `2^r`-set, hence `V>=2^((N/3)^(log_9 2))`.  Its temporary sub-`1/2` finite dip is therefore a
  stretched-exponential mirage.
- **Next gate:** multistep, tilt-preserving first-circuit switching for the random-prefix law;
  parallel targets are an integrated-activity deletion potential and a constant-loss weighted
  endpoint cup--cap recursion plus localization.  All exact checkers in `agent_half_weight/`,
  `agent_visible_flip_hw/`, `agent_coxeter_half_weight/`, `agent_cyclic_ifs_kill/`,
  `agent_dual_number_amortization/`, and `agent_lex_minimizer_search/` passed. Approximate direct
  API spend: `$0`.

### 2026-08-13 — ERDŐS #838: eleven-lane reflection/mean/cut campaign (Sihao + Codex ultracode)

- **Honest outcome:** unrestricted #838 is not resolved; the rigorous base-two window remains
  `[1/4,1/2]`.  Eleven parallel proof/search lanes produced exact reductions, new barrier
  theorems, and several stretchable counterfamilies.  Consolidated report:
  `phase2/loop/erdos838/ULTRACODE_CAMPAIGN_20260813.md`.
- **Reflection-order gate passed.** Exhausted all type-A commutation classes through `n=7`
  (`24698` at `n=7`). Exact minimum nonempty traces for `n=2,...,7` are
  `3,7,14,26,44,72`; every minimizer has a rational fixed-`x` realization. No finite threat to
  coefficient `1/2` was found.
- **Mean-size reduction.** For a uniform random convex subset, mean size `mu`, exact deletion of a
  point from a minimizer reduces the full lower bound to `mu>=log2 n-O(1)`.  Equivalently this is
  an average down-degree bound for realizable rank-three affine convex geometries.  The Boolean
  interval identity `(1+t)^n=sum_K t^|ext K|(1+t)^(|K|-|ext K|)` is exact.  Universal quadratic
  mean/count control is false on balanced Pascal cells; a minimizer-only low-mean dichotomy remains
  sufficient and open.
- **Exact endpoint algebra, with easy routes killed.** The contiguous-cut trace factors through a
  pair of hull bridges, while one long braid transfers an explicit rank-one polynomial term.
  Same-bridge reset is trivial; context-free braid descent, trace-compatible scalar potentials,
  and polynomial collision are false.  A strengthened rational heterogeneous family has
  subquadratic crossing trace and collision ratio `N^{-Theta(log log N)}`, but necessarily has
  enormous internal `V`.  Therefore the live statement must be capped by total `V(P)`, not the
  selected-cut trace.
- **Cap-audit correction and replacement theorem.** Two first-wave cut notes incorrectly called
  `log C+log U>=(1/2-o(1))log^2 n` a standard arbitrary-order product bound; it is open. Correction
  blocks were added, so their conditional `1/3` must not be quoted. What is proved is a global-cap
  directional floor: if `log V(P)<=(w+o(1))L^2` and `|Q|=N^(alpha+o(1))`, then both directions in
  `Q` have exponent at least the root `beta` of `E(w,beta)=alpha^2/4`. At `w=1/2,alpha=1`,
  `beta=0.0524142083...`. The stronger square-root collision inequality remains conjectural and,
  with only these entropy marginals, would not improve the known `1/4`.
- **Two recursive barriers.** Every homogeneous vertical tower with arbitrary nonrepeating,
  unbounded, possibly indecomposable macros and vanishing logarithmic mesh has coefficient at least
  `1/2`.  At the graded level, every fine-grained nonstationary homogeneous tower satisfies the
  sharp `log v_k>=(3/2-o(1))k^2` when `log|P|=2k+o(k)`.  The unrestricted `3/2` theorem remains open;
  it would improve the global lower coefficient to `3/8`.
- **Global braid shortcut also closed.** Exact weak-sink plateau quotients were computed through
  `n=7`, but a seven-class `n=8`, `V=113` sink plateau has three different first moments
  `316,317,318`; graded sink rigidity is false. The seven-point minimizing closure lattice is not
  toggle-CDE, with an exact sparse witness. The surviving braid target is restricted to global
  lexicographic `(V,M)` minimizers and requires full boundary-vector amortization.
- **Verification:** exact reflection orders, rational determinants, cut kernels, braid identities,
  moment recurrences, Pascal profiles, and growing-macro certificates were independently replayed.
  No shared paper theorem was altered.  Approximate direct API spend: `$0`.

### 2026-08-13 — ERDŐS #838: post-campaign reflection-order plan (Sihao + Codex)

- Read and reconciled all seven new Sol lower-campaign reports with the earlier unrestricted
  dossier.  The durable corrections are: global cap--cup mass loses a factor two; every
  asymmetric cup--cap double-counting scheme is capped at `1/4`; canonical module trees stop at
  asymptotically complete indecomposable nodes; and the decomposable multiscale reset has now been
  independently audited and passes.
- Found an exact endpoint-preserving algebraic formulation.  If chord edges are ordered by slope
  and `T_(i,j)(z)=I+zE_(j,i)`, the opposite products `A(z),B(z)` enumerate cups and caps by their
  two endpoints.  Consequently
  `Z_P(z)=Nz+<A(z),B(z)>_F-N` and, at `z=1`,
  `V(P)=trace(A^T B)`.  The full lower bound becomes a reverse-product trace inequality for
  stretchable type-A reflection orders.  The six-point Pascal cell independently checks
  `(C,U,V,M)=(31,31,50,9)`.
- Added `phase2/loop/erdos838/PLAN_OF_ATTACK_20260813.md`, with gated reduced-word search,
  stretchability checks, an exact slope-filtered contiguous-cut lemma as the primary proof target,
  graded growing-`k` supersaturation as the incremental fallback, explicit kill tests, and a
  one-week execution schedule.  Added the first exact checker `reflection_trace.py` and corrected
  stale statements in `RESUME_838.md` about the reset audit, epsilon thresholds, and the completed
  full-JCTA clearance.
- A narrow web search found the standard reflection-order/reduced-word and PBW/Lusztig literature,
  but no direct reverse-product Frobenius inequality; this is not yet a publication-grade novelty
  search.  Approximate direct API spend: `$0`.

### 2026-08-13 — ERDŐS #838: all-in decision, seven-lane lower-bound campaign, barrier proved (Sihao + Claude Opus 5)

**Decision.** Went all in on #838 after comparing it with #669, #791 and #1208 on *"which can
actually be finished"* rather than *"which is cheapest to advance"*. #838 is unique here: we
already own `limsup ≤ 1/2`, so a single theorem (`liminf ≥ 1/2`) resolves existence and value
together. #1208 has a polynomial gap in a crowded room; #669's headline `1/28` is prior art (Zhao
Hui Du, 2019) with a factor-2 gap and no candidate value; #791 is open after three attacks.

**Paper audit before the campaign.** Wrote `independent_check.py`, a from-scratch exact-rational
rederivation that counts caps/cups/convex subsets from orientation determinants only, sharing no
code path with the paper's substitution formulas. It reproduces `(C,U,W) = (14136,14136,441399)`
on the 36-point composition. Also re-derived Lemma 2.1's determinant asymptotics, Prop 3.1's
(3.5)–(3.9), Prop 4.4, Lemma 4.2 and all three steps of Lemma 5.2 by hand. Found and recorded that
the `eps` threshold is load-bearing: at `eps = 1/1000` the set is in general position yet returns
the wrong count.

**Baek–Balko clearance.** Read the SoCG 2025 paper (committed as
`refs_baek_balko_socg2025.pdf`). They never count convex subsets — Lemma 14 gives only
non-existence of a `k`-gon and cardinality — so the substitution identities are genuinely ours.
But their "decomposable" class is the paper's "strongly decomposable", and Sol then traced it
correctly past them to **Balko–Kynčl–Langerman–Pilz, EJC 24(4) (2017) P4.24**, which is a better
citation than the one I recommended. My claim that the conversion is a 180° rotation was **wrong**;
Sol's `ρ(x,y)=(−x,y)` is right, verified numerically, and my review note now carries an erratum.

**Campaign (7 Sol lanes, effort=max, `scripts/campaign_lower.py`).**
- My stated target was **mis-specified** and two lanes caught it: the *global* cap–cup product is
  insufficient, since `C,U ≤ N²M` costs a factor of two and returns the published `1/4`. The right
  object is the **endpoint-localized** `max_{p<q} c(p,q)u(p,q)`, which Sol's
  `INSTANCE_HANDOFF_20260813.md` had already named `(EM)` at 13:05 — before the campaign launched
  without it having been read. Process lesson: read the folder's own handoff before designing an
  attack.
- **Barrier proved** (`attack_direct`): the optimal consequence of all asymmetric cup–cap double
  counts is `(c+u)H(c/(c+u)) ≥ 1/4`. The standard method cannot exceed `1/4` even for the product.
  Apparently novel; worth banking independently.
- **Two routes closed**: canonical tree decompositions stop at arbitrarily large indecomposable
  nodes; Székely does not transfer *and never supported `1/2`* — his normalized lower coefficient
  is ≈0.1577, and the `1/2` in `prior_art_20260812.md` was his random-graph **upper** coefficient.
  That file now carries a correction block; a strategic recommendation had rested on the misreading.
- **Premise survived**: nothing beat `1/2`; every level-dependent uniform blow-up with
  `max log|S_i| = o(log N)` satisfies `log v ≥ (1/2−o(1))(log N)²`.
- **Prior art AMBER**: cite Holmsen–Nassajian Mojarrad–Pach–Tardos, Bárány–Valtr, ordered
  monotone-path work; none gives `(EM)` or beats `1/4`.
- Verified `break_lemma`'s exact dyadic Horton family with `check_candidate.py`: product ratio
  1.792→1.073 over `N=4..64`, converging to 1 from above as claimed.

**Artifacts added.** `RESUME_838.md` (entry point/index), `CAMPAIGN_SYNTHESIS_20260813.md`,
`REVIEW_20260813_claude.md`, `independent_check.py`, `check_candidate.py` (exact adjudicator for
any proposed point set), `scripts/campaign_lower.py`, seven raw lane outputs.

**Honest status.** The upper theorem is real and defensible. The lower bound is genuinely hard;
round 1 mapped the barrier rather than crossing it. Treat `1/2` as the best-supported conjecture,
not a known value. Approximate API spend this session: Sol only, ~20 lanes at effort=max across
838, the candidate sweeps, the Jacobian aftermath and the unit-distance work.

### 2026-08-13 — ERDŐS #838: complete future-instance restart brief (Sihao + Codex)

- Added `phase2/loop/erdos838/INSTANCE_HANDOFF_20260813.md`, a self-contained restart document
  covering the exact problem and normalization, the coefficient-`1/2` paper proof, the sharp
  mirror-decomposable theorem, the unrestricted common-endpoint reduction, every major proved
  barrier and exact counterexample, prior-art/claim boundaries, paper-format decisions,
  verification commands, repository map, git state, and ranked next attacks.
- The brief explicitly separates theorems, computational evidence, conjectural targets, and
  apparent novelty.  It records durable proof-relevant reasoning rather than private model
  chain-of-thought.  New instances should read it before `UNRESTRICTED_ATTACK_20260813.md`.
- No mathematical claim or paper content was changed.  Approximate direct API spend: `$0`.

### 2026-08-13 — ERDŐS #838: unrestricted attack and exact route barriers (Sihao + Codex ultracode)

- **Honest headline:** unrestricted #838 remains open with rigorous base-two window `[1/4,1/2]`.
  The integrated map is `phase2/loop/erdos838/UNRESTRICTED_ATTACK_20260813.md`. This pass did not
  move an endpoint; it rigorously eliminated the main upper/lower shortcuts and isolated an
  incremental theorem that would move the lower endpoint.
- **Finite-state upper barrier.** Every finite-state almost-vertical blow-up has liminf coefficient
  at least `1/2`, even with parent-dependent macros, reflections, periodic rules, state-dependent
  branching, and unequal child sizes. The proof uses a maximal-growth recurrent SCC, Perron growth,
  maximum-cycle-mean cap/cup exponents, cup--cap, and a recurrent two-block term. An independent
  audit accepted it after explicit SCC/periodicity repairs. Artifacts:
  `agent_upper_multitype/{FINITE_STATE_BARRIER.md,multitype_search.py,heterogeneous_audit.py}` and
  `agent_asymptotic/FINITE_STATE_BARRIER_AUDIT.md`.
- **Baek--Balko construction counted.** The canonical `x`-blow-up cannot beat `1/2`. Layer
  transversals and a canonical score-two Pascal cell give a conservative cover `0.5021396326...`;
  the fully canonical `m=3` endpoint is covered by the sharp decomposable theorem. An independent
  referee accepted this after an endpoint repair and expanded score induction. The transversal
  rigorously covers arbitrary cells through `x/k=0.21` (computed crossing `0.21616144...`);
  noncanonical extremal cells above this remain a precise loophole. Artifacts:
  `agent_asymptotic/{BAEK_BLOWUP_COUNT.md,
  bb_xblowup_barrier.py}` and `agent_geometry/BAEK_BLOWUP_COUNT_AUDIT.md`.
- **Lower-method ceilings.** Fixed-`k` induced-subset chains telescope to one scale; ideal same-type
  transversals and recursive use of `1/4` stay at `1/4`. A hereditary `N^alpha` structured
  extraction with internal coefficient `c` transfers at best `c alpha^2` for `alpha>=1/2`, even
  aggregating all witnesses. Separate cap/cup marginals do not control their forward product. The
  exact escape target is growing-`k` supersaturation: any `eta>0` in
  `mu_k(2^{2k+o(k)})>=2^{(1+eta-o(1))k^2}` improves the lower coefficient to `(1+eta)/4`.
- **Global history route decisively falsified.** The one-endpoint formula gives split-path count
  `44`, not true count `50`, on `T_(4,2)`. Stronger, `H_q<=2^{O(q log q)}V` is false on its
  directional iterates. At `q=floor(log N)`, an explicit `sqrt(d)`-scale cap-branch spine gives
  history coefficient exactly `1`, versus convex coefficient `2/log2(6)=0.773705...`; already at
  depth 18, `H_47>47!V`. Artifacts:
  `agent_claude_review_audit/{GLOBAL_HISTORY_AUDIT.md,history_global_test.py}`.
- **Further structure.** Convex sets are cliques in the convex-quadruple 4-graph, but a random
  4-graph barrier shows fixed hereditary flag densities cannot force `k=Theta(log N)` cliques
  without growing-order planar constraints. Exact Pascal fixed-point exponents rise from `0.168`
  at `k=10` to `0.390` at `k=120`, so these examples do not falsify a uniform multiplicity gain.
  Hull fibres yield many nested cages, while exact nested triangles kill naive multiplication.
- **Verification:** exact integer/rational-coordinate programs pass; the Baek barrier received an
  independent proof audit; `git diff --check` passes. Approximate direct API spend: `$0`.

### 2026-08-13 — ERDŐS #1208: rank-17 prime-power upper bound candidate and exhaustive restart handoff (Sihao + Codex ultracode)

- **Prior-art status corrected first.**  The public problem page is stale.
  Clemen--Führer--Roche-Newton already prove `F_2(n)>>n^(1/3)`, and
  Lee--Pohoata--Zhu already prove `F_2(n)<<n^(1/2-epsilon)` with a stronger
  robust theorem, validating Sungchul Lee's independent June draft.  The bare
  polynomial saving was killed as a novelty target before construction work.
- **Apparently new explicit partial result.**  Prime-power valuation flags
  replace the two squarefree isotropic choices by `K+1` local patterns.  Exact
  divisor switching and Minkowski box packing yield a master bound.  A rank-17
  tame totally-real pro-2 tower with 55 split primes and 27 phase-adaptive
  depth vectors gives the candidate theorem `F_2(n)<<n^0.49815`.
- **Verification shipped.**  `verify_adaptive_rank17.py` checks all finite
  arithmetic data: 55 primes, 935 Legendre symbols, rank 17, root discriminant
  `3929160775540133527939545`, and `4(17+55)=288<289`; it also checks the 27
  overlapping exponent intervals at 80 decimal digits.  A 150-digit replay
  preserves every sign.  Two independent adversarial audits reconstructed the
  local-to-global proof and found no defect, conditional on the declared
  Shafarevich presentation theorem and symbolic master inequality.  The
  rank-16 `0.49826`/`0.4991` certificates remain independent fallbacks.
- **Full-gap attack recorded honestly.**  The binary local-lattice flags are
  completely classified, giving a continuous entropy floor `0.411408...` for
  this method, far above `1/3`.  Any power saving in four-distinct distance
  energy would improve the lower exponent, but the square grid has the same
  edge/codegree profile as a random 4-graph at cube-root scale.  This kills
  generic containers/nibbles/LLL, raw DRC, additive BSG, simple grid
  occupancy/modular arguments, semialgebraic Ramsey machinery, tensor/polar/
  finite-group constructions, and further fixed-modulus tuning as complete
  routes.  The credible next inputs are an inverse Guth--Katz/Elekes--Sharir
  stability theorem or a rainbow principal-submatrix theorem for rank-4
  Euclidean distance matrices.
- **Claim discipline.**  This is not a full solution and not yet an externally
  established theorem.  Human proof review, directed-interval/rational
  hardening of the Decimal certificate, and MathSciNet/zbMATH/author novelty
  clearance are mandatory before a paper claim.  The complete restart package
  is `phase2/loop/erdos1208/HANDOFF_20260813.md`.  No process is running.
  Approximate direct API spend: `$0`.

### 2026-08-13 — ERDŐS #669: zonotope lower-bound theorem and exhaustive handoff (Sihao + Codex ultracode)

- **Problem identity repaired.** The repository shortlist had guessed that #669 was a
  Heilbronn/fixed-area triangle question. The primary sources and durable database row show that it
  is the generalized orchard problem: maximize exactly-`k` and at-least-`k` rich lines and determine
  the normalized quadratic limits. The shortlist and new `phase2/loop/erdos669/PROBLEM.md` now carry
  the correct statement.
- **Rigorous partial theorem.** A primitive `k`-direction lattice zonotope of determinant area `D`
  gives `2Dq+k` arrangement lines and exactly `Dq^2+kq+1` finite `k`-fold vertices. Duality and
  padding prove `f_k(n),F_k(n)>=n^2/(4D)-O_k(n)`. The sublattice-index caveat was corrected, and
  mixed-area/Minkowski plus Simpson's minimum-area lattice polygons prove the optimal coefficient in
  the whole weighted/full-support scheme is `1/[4A(2k)]`. For `k=4,...,11` this gives
  `1/28,1/56,1/96,1/160,1/236,1/348,1/484,1/656`, beating Palásti at `k=4,5,6,7,8,11`.
- **Verification shipped.** `verify_zonotope_construction.py` exactly checks all projective
  intersections, infinity exceptions, hull/Pick counts, pair identities, and Melchior for the stored
  `k=4,...,11` sets at `q=1,2`; all pass. The independent `k=4` checker passes through `q=30`.
- **Prior-art discipline.** The `k=4` coefficient `1/28` is definitely in a 2019 Zhao Hui Du web
  construction (its displayed `1/24` is an arithmetic typo). Stanley's Ehrhart formula, Simpson's
  minimum polygons, and some exact generator sets are classical. No checked source records the
  general orchard deduction or the new-looking coefficients, but novelty is deliberately marked
  uncleared pending MathSciNet/zbMATH and an arrangements specialist.
- **No false full-solution claim.** Limit existence and exact constants remain open for `k>=4`.
  Generic union, downward sampling, and `O(n)` increment lemmas were proved, but a lacunary numerical
  countermodel shows these axioms cannot force a quadratic limit; naive geometric blow-ups lose a
  factor `k-1`. Current upper bounds and the exact `k=4` Melchior defect identity are recorded in
  `FULL_ATTACK.md`.
- **Durable restart package.** The self-contained operational record is
  `phase2/loop/erdos669/HANDOFF_2026-08-13.md`, with proof, prior-art, verifier commands, dead ends,
  claim discipline, and next attacks. Approximate direct API spend: `$0` in this local Codex session.

### 2026-08-13 — ERDŐS #791: durable full-context handoff after third full attack (Sihao + Codex ultracode)

- **Wrote the complete restart brief** at
  `phase2/loop/erdos791/HANDOFF_20260813.md`.  It consolidates all three full attacks and the
  construction/SAT campaigns: exact normalization and literature status; Kohonen predicate and
  certificate; corrected SAT/DRAT results; closed staircase/product/triangle-free routes; carry-bin
  and profinite relaxations; amplifier/role-defect theorems; the unbounded `K_r` carry construction;
  projective carry triangle; Fourier stability theorem; rank-one absorber; finite `chi=7` proof;
  every known audit trap; speculative ideas; exact reproduction commands; and a prioritized first-day
  plan for a fresh instance.
- **Latest mathematical frontier stated explicitly.**  Static chromatic compatibility is no longer
  the obstacle: efficient `K_r` tile languages exist for every fixed `r`.  The live gap is temporal
  state compatibility.  A full solution would follow from either a `k+o(k)` transition-compatible
  role assignment on limsup-extremal bases or an `o(k)` additive-rectangle description of all holes.
  The next computational model must jointly choose target representations, roles, and ordered carry
  transitions; role-only optimization is obsolete for this purpose.
- **Updated the live `HANDOFF.md`** in §§3, 4, and 7 so another collaborator lands on this frontier
  rather than restarting a closed subproblem.  No theorem changed in this context-writing pass; no
  process is running.  Approximate incremental spend: `$0`.

### 2026-08-13 — ERDŐS #838: original paper formatting restored (Sihao + Codex)

- **Presentation restored without reverting substance.**  At the user's request, switched the
  manuscript from `amsart` back to its original `article` typography, restored the original title
  presentation and `maketitle`-before-abstract flow, and retained every mathematical,
  terminology, citation, prior-art, and verification change from the Claude/JCTA review.
- **Disclosure preserved.**  The conventional author field remains blank, while the same Bregman
  paper disclosure, affiliations, and both contact emails now appear through an article-native
  first-page date footnote.
- **Fresh QA passed.**  Tectonic produces a warning-free 10-page PDF, and all ten rendered pages
  were visually inspected for clipping, overlaps, glyph problems, and bad page breaks.  Updated
  deliverable: `output/pdf/erdos838_counting_convex_subsets.pdf`.  Approximate API spend: `$0`.

### 2026-08-13 — ERDŐS #838: Claude-review response, full JCTA clearance, and final byline (Sihao + Codex ultracode)

- **Claude review triaged and incorporated.**  The mathematical checks were positive.  Accepted
  the central citation correction, the finite-`k` “approaches `1/2` from above” clarification, and
  the need to state `x(A)<x(B)` explicitly in the strong split.  The epsilon observation is useful
  but not a proof gap: the finite strict-determinant argument is rigorous, and the hardened exact
  checker demonstrates that the perturbation must be chosen afresh (first tested success for its
  unnormalized nested coordinates is `1/9750`; the normalized verifier accepts `1/128`).
- **Prior-art relation made exact.**  The full open-access Baek--Balko JCTA 2026 article was audited,
  not only its SoCG abstract.  Journal Theorem 7 proves an existence threshold on decomposable
  sets; Lemma 14 contains the endpoint-cluster classification underlying the crossing term, but it
  does not enumerate all convex subsets or derive the coefficient `1/2`.  The class itself comes
  from Balko--Kynčl--Langerman--Pilz (2017).  Our convention is its mirror under
  `(x,y)↦(-x,y)`, not a 180-degree rotation.  The paper now uses “mirror-decomposable,” cites both
  sources at the definition/lemma, and identifies `T_(m,i)` with the reflected classical
  `P(i+2,m-i+2)` cell.
- **Front matter matched to the Bregman paper exactly.**  Switched to `amsart`, retained a blank
  conventional `author` field, and copied the same first-page AI-assistance/contact footnote:
  Nikol Savova (University of Oxford) and Sihao Huang (independent researcher), with both emails.
  The abstract precedes `maketitle`, as in the Bregman source.
- **Fresh QA passed.**  Tectonic produces a warning-free 9-page PDF; all pages were rendered and
  visually inspected.  All four verification programs pass, including the direct exact
  `(C,U,W)=(14136,14136,441399)` count, 16-point exhaustive classification, and reset certificate.
  Updated deliverable: `output/pdf/erdos838_counting_convex_subsets.pdf`.  Approximate API spend:
  `$0` (local tools plus existing web access).

### 2026-08-13 — ERDŐS #838: sharp `1/2` theorem for all strong trees + submission draft (Sihao + Codex ultracode)

- **New theorem (independently reconstructed twice).**  For every ordered full binary
  strong-decomposition tree with `N` leaves,
  `log2 W >= (1/2)(log2 N)^2 - O((log N)^(3/2))`.  This closes the alignment gap left by the
  earlier cap--cup product estimate and upgrades the previous `1/3` bound.  The proof follows a
  heavy child through a `4 sqrt(log N)`-bit window.  Fewer than `sqrt(log N)` macroscopic siblings
  force `Omega((log N)^(5/2))` same-side pure-comb choices; otherwise nested macroscopic siblings
  give a uniform radial endpoint bound, and every hidden forward product resets both reverse
  endpoint coordinates.  Repeated attachments add a fixed amount to one persistent coordinate,
  forcing the full `1/2` coefficient.  Artifacts:
  `phase2/loop/erdos838/agent_asymptotic/{NEXT_ENDPOINT_ATTACK.md,endpoint_reset_certificate.py}`;
  adversarial audits:
  `agent_geometry/NEXT_ENDPOINT_AUDIT.md` and
  `agent_killsearch/STRONG_TREE_HALF_REFEREE.md`.  All found the theorem valid.
- **Class characterized exactly.**  Combining that lower bound with the iterated balanced-Pascal
  construction gives
  `lim log2 g(N)/(log2 N)^2 = 1/2` for the minimum over all strongly decomposable `N`-point sets.
  Thus no stationary, periodic, nonstationary, or heterogeneous strong-tree construction can beat
  the new upper coefficient.
- **Paper shipped locally.**  Built a self-contained 10-page draft,
  `phase2/loop/erdos838/paper/main.tex`, containing the directional rational realization, exact
  substitution identities, fixed-template asymptotics, arbitrary-`N` argument, Pascal templates,
  fixed-template barrier, and the new strong-class theorem.  Final rendered artifact:
  `output/pdf/erdos838_counting_convex_subsets.pdf`.  Tectonic build has no undefined references,
  overfull boxes, or warnings after reruns; key pages were rendered and visually inspected.
  Independent exact checks all pass: 9-point brute force, 36-point endpoint DP
  `(C,U,W)=(14136,14136,441399)`, all `2^16` subsets of a nonconvex-macro composition, and 24,578
  first-reset integer states plus increment/closed-form boxes.
- **Final novelty/referee status.**  `SUBMISSION_NOVELTY.md` gives a primary-source audit.
  General iterated order-type blow-ups (Han et al.) and almost-vertical Erdős--Szekeres blow-ups
  (Baek--Balko) are prior art.  The narrow apparently novel contribution is the prescribed `2+1`
  orientations, exact unweighted `C,U,W` substitution identities, geometric limsup coefficient
  `1/2`, and sharp strong-class theorem.  Huemer et al.'s weighted enumeration and Székely's graph
  analogue are now cited.  Three final integrated-paper audits found no mathematical defect after
  minor repairs.  Authors are deliberately marked “omitted for circulation”; human authorship and
  a MathSciNet/Zentralblatt/geometer clearance remain required before submission.
- **Honest scope / next attack.**  Unrestricted Erdős 838 is **not solved**; the rigorous window
  remains `[1/4,1/2]`.  The tree alignment issue is closed.  The sole conceptual gap is now a
  structural transfer: extract near-full-scale approximate strong pieces from an arbitrary planar
  order type, or reproduce the endpoint-reset mechanism nonlocally.  Hinged-history contained maps
  provably lose `Theta((log N)^2)` bits, so that naive route is dead.  Next target is a quantitative
  order-type regularization/decomposition lemma with explicitly tracked exponent loss.  The new
  `agent_asymptotic/FULL_REGULARIZATION_TRANSFER.md` makes the threshold exact: an `N^alpha` strong
  extraction transfers coefficient `1/2` only as `alpha^2/2`, so it beats `1/4` only for
  `alpha>1/sqrt(2)` and preserves `1/2` only at `alpha=1-o(1)`.  Current `Theta(sqrt N)` mutually
  avoiding extraction would give only `1/8`; recursive black-box use builds merely `Theta(log N)`
  strong leaves.  A one-witness same-type pipeline is capped at `1/4` even with perfect retention,
  so any full solution needs weighted multiplicity across many pieces or approximate-strong error
  charging.
- **Approximate spend:** local Codex ultracode orchestration; no new paid API batch recorded.

### 2026-08-13 — ERDŐS #838: proved `1/3` for strong trees; exact max-endpoint reduction (Sihao + Codex ultracode)
- **New rigorous theorem.** Every ordered strong-decomposition tree with `n` leaves has
  `log2 W >= (1/3)(log2 n)^2-O(log n log log n)`. Follow a larger child until losing a
  `(log n)^4` factor. A sibling of relative size `>=1/(log n)^2` supplies two nearly full-scale
  cap/cup product bounds and a one-node minimax keeps two thirds of their sum. If no such sibling
  appears, the path has `Omega(log^2 n log log n)` levels; majority-side sibling choices give
  vastly many pure caps/cups. Constants were independently audited in
  `agent_geometry/TREE_AMORTIZED_AUDIT.md`.
- **Exact three-variable reduction.** With `X` the maximum cap count at a fixed left endpoint,
  `Y` the reflected cup maximum, and `M=max c(s,t)u(s,t)`, strong glue obeys
  `X=max((b+1)X_A,X_B)`, `Y=max(Y_A,(a+1)Y_B)`, `M=max(M_A,M_B,X_A Y_B)`, and
  `M<=W<=n^2M`. Thus the matching `1/2` theorem is exactly a weighted one-turn-path problem.
  The imbalance penalty `(x-y)^2/(x+y)` is quasiconvex under coordinatewise maximum; a
  Pinsker-calibrated max-endpoint profile survives exhaustive states through `n=17` and random
  recursive tests, but its Bellman inequality remains unproved.
- **Killed shortcuts.** The earlier imbalance-corrected `H` potential is false by an exact
  `2^455`-leaf iterated-Pascal certificate. Global `CU/W` comparison, scalar/local quadratic
  Bellman inductions, direct endpoint-caterpillar comparison, and capped-endpoint Bellman all fail
  on explicit recursive families. Hinged histories can even realize an 8-point no-pentagon order
  type, so any successful history compression must be nonlocal.
- **Honest status.** Global Erdős 838 remains open with window `[1/4,1/2]`; inside the strong-tree
  class the proved window is now `[1/3,1/2]`. Fixed or alternating Pascal templates cannot attain
  `1/3`; a counterconstruction would need nonstationary macroscopic scale jumps. New artifacts:
  `agent_asymptotic/{MAX_ENDPOINT_PROFILE.md,TREE_POLYNOMIAL_ANGLE.md,E_VS_W_COUNTEREXAMPLE.md}`;
  `agent_geometry/{TREE_AMORTIZED_AUDIT.md,audit_history_obstructions.py}`;
  `agent_killsearch/{H_COUNTEREXAMPLE.md,QUADRATIC_PROFILE.md}`. Spend approximately $0 direct API.

### 2026-08-13 — ERDŐS #838: independent `1/2` audit + sharp lower-frontier lemmas (Sihao + Codex ultracode)
- **Upper theorem survived two independent audits.** The vertical blow-up geometry, exact
  `(C,U,W)` classifier, rational realizability, fixed-template asymptotics, and deletion to arbitrary
  `N` were reconstructed from scratch. A new rational 16-point test with a nonconvex four-point
  macro skeleton exhausts all `2^16` subsets and finds exactly 3,146 spanning convex subsets, with
  zero classification failures. `proof_blowup_half.md` now states the generic blow-up provenance
  precisely and retains novelty only for the mixed signs, exact enumerator, and `1/2` optimization.
- **Broader construction barrier.** For nonstationary homogeneous compositions
  `Q_t=S_t[Q_{t-1}]`, with `ell_t=log|S_t|` and `L_t=sum ell_i`, unavoidable two-block terms give
  `log W >= (L^2-sum ell_t^2)/2`. Thus stationary, periodic, finite-menu, and all schedules whose
  largest scale is `o(L)` cannot beat `1/2`; polynomial random thinning preserves it too. Any better
  upper construction must use a macroscopic scale jump plus directional anti-alignment.
- **Sharp decomposable lower lemma.** For every binary strong-glue tree,
  `CU >= 2^((log N)^2/2-log N)`. The exact Cauchy--Schwarz remainder shows that every bad forward
  term `C(left)U(right)` creates a reverse-alignment square, but nodewise charging is insufficient:
  the square can vanish while reverse/forward differs by a factor up to `(a+1)(b+1)`. Exact search
  through `N=19` and randomized trees support the stronger imbalance-corrected potential, but a
  global amortized reset lemma is still missing. The recurrences transfer exactly to counting
  leaf-induced left combs, right combs, and one-turn combs in ordered binary trees; no applicable
  growing-pattern theorem was found.
- **Full `1/2` history mass, failed compression.** A nested endpoint-pair process always has at
  least `2^{-binom(t,2)}(m-(2^t-2))_+^t/t!` hinged histories. Taking
  `t=log m-2 log log m` gives the desired `2^((log m)^2/2-O(log m log log m))` raw multiplicity.
  Exact rational examples show that same-sign levels need not be caps/cups, a hinged history need
  not be split, and even a hinged split family can have maximum convex subset only about `N/2`.
  Thus the FKK/BCP graph compression does not transfer without using the full nested order type.
- **Literature/kill-search.** Published growing-`k` supersaturation and Baek--Balko split-support
  counting both optimize at the existing `1/4`; Bukh--Vasileuski's same-type lemma gives structured
  product families but only coefficient `1/20` directly. Generic blow-ups are prior art, while no
  source was found for the convex-subset `1/2` enumerator or matching lower lemma. New artifacts:
  `lower_bound_frontier.md`, `agent_asymptotic/{NEW_HALF_AUDIT.md,TREE_ALIGNMENT.md}`,
  `agent_geometry/{half_audit.md,HISTORY_ATTACK.md,audit_blowup_classification.py}`,
  `agent_killsearch/{SECOND_STAGE.md,MULTIPLICITY.md,RECURRENCE_TRANSFER.md}`. **Honest status:**
  upper coefficient `1/2` is a strongly audited apparent new partial result; problem 838 remains
  open at an explicit alignment/compression theorem. Spend approximately $0 direct API.

### 2026-08-13 — ERDŐS #838: iterated blow-up improves candidate upper coefficient to 1/2 (Sihao + Codex)
- **New theorem:** a vertical lexicographic composition `S[Q]` has exact profile formulas
  `C=C(Q) sum_j c_j(S)|Q|^(j-1)`, the reflected cup formula, and
  `W=|S|W(Q)+C(Q)U(Q) sum_{j>=2}v_j(S)|Q|^(j-2)`. Iterating a fixed `r`-point
  template with largest cap/cup sizes `a,b` gives exact base-2 coefficient
  `(a+b-2)/(2 log2 r)`.
- **Optimization:** choose the balanced cap--cup extremal template of size
  `binom(2k-4,k-2)` with `a=b=k-1`, then let `k` grow. This proves the candidate bound
  `limsup log2 f(N)/(log2 N)^2 <= 1/2`, superseding both the row `0.721347...` and central-cell
  `0.639326...` bounds. The cap--cup theorem also shows `1/2` is best possible among all fixed-
  template vertical iterations.
- **Verification:** `lexicographic_blowup.py` realizes the abstract composition with exact rational
  coordinates, brute-enumerates all subsets in a 9-point case, and independently checks a 36-point
  case by last-edge and endpoint DPs. Formula and audit agree at `(C,U,W)=(14136,14136,441399)`.
  Self-contained proof: `proof_blowup_half.md`; updated full attack: `FULL_ATTACK.md`.
- **Full problem remains open:** rigorous window is now `[1/4,1/2]`. Matching requires a weighted
  endpoint-multiplicity theorem. A max-term/tropical simplification of the strong-glue recurrence was
  tested and fails because additive path multiplicities carry essential entropy. The close graph
  analogue (Székely 1984) also has a random upper coefficient `1/2` and a difficult lower gap.
- **Novelty status:** targeted searches found no public convex-subset bound at `1/2`; Baek--Balko's
  more general blow-ups are construction-size tools and do not enumerate total convex subsets.
  Still required: independent line-by-line audit and MathSciNet/expert clearance. Spend ~$0 API.

### 2026-08-13 — ERDŐS #838 FULL-PROBLEM ATTACK: exact endpoint reduction; original limit still open (Sihao + Codex)
- **Upper theorem hardened:** `proof_central.md` now constructs the rational strong glue explicitly,
  proves its orientation signs by a `>8` versus `<=4` slope separation, uses the exact
  `binom(m,i)` path count, and spells out the uniform entropy error. Geometry enumeration and
  arbitrary-precision DP were rerun successfully.
- **Exact full-problem reduction:** proved
  `V(P)=1+N+sum_{s<t}c(s,t)u(s,t)`, where `c,u` count cap/cup chains with the same two endpoints.
  This identifies the missing result as a weighted endpoint-alignment theorem for realizable
  rank-3 signotopes. `FULL_ATTACK.md` contains the proof, path DP, and conditional route to the
  constant `kappa=1-1/(4 ln 2)`.
- **Barrier:** derived that ES-threshold double counting gives `alpha(1-alpha)<=1/4`; recursively
  feeding `f(t)` into the same scheme preserves rather than improves its coefficient. A new
  multiplicity/stability input is necessary.
- **Falsification:** enumerated all realizable order types through `N=9` from Aichholzer's database.
  Exact minima including the empty set are `45,73,114,169`; decomposable minima are
  `46,76,121,185`. Thus Pascal/decomposable sets are not finite global minimizers. The data files
  stayed in `/tmp` and were not redistributed.
- **Artifacts:** `FULL_ATTACK.md`, `order_type_audit.py`; also retained the sampling and exact
  decomposable Pareto DPs. **Honest status:** strict upper improvement proved; Erdős 838 itself
  remains open at one explicit weighted signotope lemma. Spend approximately $0 direct API.

### 2026-08-12 — ERDŐS #838: central Pascal cell gives candidate upper coefficient 0.639326 (Sihao + Codex ultracode)
- **Result:** for the minimum number `f(N)` of convex-position subsets forced in an `N`-point
  general-position planar set, obtained the candidate partial theorem
  `limsup log2 f(N)/(log2 N)^2 <= 1-1/(4 ln 2) = 0.6393262398...`. This improves the
  explicit public upper coefficient `1`; it does not prove existence or determine the limit.
- **Construction:** use the single central cell `T(m,floor(m/2))` of the classical
  Erdős--Szekeres/Morris--Soltan Pascal construction (`N=binom(m,floor(m/2))=2^{m-o(m)}`),
  rather than the full `2^m`-point row. The whole-row route has the sharp but weaker coefficient
  `1/(2 ln 2)=0.7213475...`.
- **Proof spine:** nonempty cap counts satisfy the exact recurrence
  `C(m,i)=C(m-1,i)+(1+binom(m-1,i))C(m-1,i-1)`. Latest-diagonal path domination gives
  `log2 C(m,xm)=A(x)m^2+O(m log m)`, with `A(1/2)=1/2-1/(8 ln 2)`. Every convex subset
  injects into its upper-cap/lower-cup pair, giving the displayed coefficient. Conversely,
  every left-cap/right-cup union is convex, so the actual central-cell count has the same rate.
- **Verification:** two independent lanes audited geometry and asymptotics. Exact rational
  enumeration passed all cells through `m=5`, the interior `m=6` cells (central:
  `N=20, C=U=1281, W=10951`), and the 32-point row with zero decomposition failures.
  Arbitrary-precision DP passed through `m=256` (actual normalized central rate `0.640979821`,
  converging to `0.639326240`).
- **Kill-search:** exact symbolic/decimal searches, source/citation neighborhoods, the public
  Erdős thread, recent construction papers, blogs, and GitHub found no matching bound. Verdict:
  high-confidence apparently novel, subject to MathSciNet/expert confirmation. The strongest
  explicit public window located was base-2 `[1/4,1]`.
- **Artifacts:** `phase2/loop/erdos838/{PROBLEM.md,proof_central.md,verify.py,
  prior_art_20260812.md}`, plus `agent_geometry/` and `agent_asymptotic/` certificates.
- **Process note:** one cap-recurrence orientation typo appeared while consolidating and was
  caught by comparing the prose against both independent exact DPs; the final draft uses
  nonempty caps and boundary value `1`. Spend: approximately $0 direct API.

### 2026-08-11→12 — G2 CLOSURE CAMPAIGN (7 waves, Fable then Sol): Theorem A is CONDITIONAL on CL; CL's hypothesis count went 4 → 6 under scrutiny (one since proved); paper rewritten and shipped-ready (Sihao + Claude)
- **Licenses decided + applied:** MIT for the repo (LICENSE at root, both authors);
  arXiv non-exclusive (not CC BY) for the preprint, keeping venue options open.
- **Method:** blind-draft + adversarial-referee fleets (the F2-campaign pattern,
  automated via ultracode workflows); ~70 agents over 5 waves, all outputs in
  `phase2/bruhat/f2_drafts/g2_campaign_20260811/` (drafts, 2-referee reports per
  unit, STATUS.md … STATUS_wave5.md ledgers — read STATUS_wave5.md first).
- **PROVED, two-referee, this campaign:** wp1-c master far-region bound (thresholds
  ~5.1e6 → 143-379); Δ_ker bucket + T.9-final ⇒ **Prop 3.5(ii) CLOSED**; Theorem S
  region stitching ⇒ **Prop 3.5(i) reduced to one named lemma CL(79,20,0.89)**;
  SL3' mid-exponent; sliver closure; SL4'-X; SL4'-E pricing; repaired SL4' assembly;
  T2's overdue house-rule referee debt discharged (both halves); exact harness
  ground truth extended m=150 → **560** (CL obligation now m ≥ 561; G4's [401,536]
  part-(c) band closed as a side effect).
- **HONESTLY OPEN — the exact residue (STATUS_wave5 §2):** four CONJECTURED
  statements (S1) SL1'-w(i) banded cumulant scales (⚠ truth margin only 3.7-3.9%),
  (S2) SL1'-w(ii) R5 bound, (S3) joint-cancellation (E3) — ADDED this campaign by a
  twice-refereed impossibility result killing the recorded plan, (S4) bootstrap
  seed. CL is proved modulo (S1)-(S4) with chain-verified C* = 18.23 ≤ 20; no flip
  executed (correctly). **Theorem A = F2(a) is NOT proved; it is conditional on
  exactly these four.**
- **Ops lessons:** (a) hard output-token cap killed 15 proving-agents across the
  campaign; fixed via CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000 in settings — but the
  SL1' package ALSO blew the 128k cap: that piece needs decomposition, not caps;
  (b) referee fleets repeatedly caught fabricated/overstated claims (7.96x → 1.30x
  margin headline; refuted architected routes) — the house two-referee rule is
  earning its cost; (c) residue count went 3 → 4 this wave: fleets are converging
  on thin-margin statements where human judgment (relax constants? re-architect
  budget?) beats more compute.
- Spend: ~20M subagent tokens API. All work committed + pushed per-wave.

**CONTINUATION 2026-08-12 (waves 6-7, model switch, and the paper).** Fable credits ran out
mid-wave-6b; work moved to OpenAI **gpt-5.6-sol at `effort=max`** (~$1-5/call vs hundreds per
Fable wave), orchestrated with the same decompose/parallel/referee pattern via
`g2_scripts/campaign_20260811/wave6_sol/{run_sol,verify_sol,orchestrate}.py` (Responses API,
background, id-journalled, retry-hardened). Total spend across the two days ≈ $1500.
- **(S1) PROVED** — Sol draft, two adversarial Claude lanes, certificate of record is the
  referee's own rigorous interval computation. The first of the four to close.
- **(S2)**: attempt 1 FATAL (proved none of seven bounds — largely a prompt defect: it was
  never shown the band table). Attempt 2 retained the cancellation and hit all seven
  (W1: 0.0258 vs 0.05, a ~45x improvement on the binding quantity); **its entire numerical
  spine was then independently replayed locally**, finding one real defect (the prescribed
  1/64 cell width does NOT certify W1; 1/128 does) and four unflagged thin margins.
  Attempt 3 closed the maths lane, resolved the underivable `2w` (a weighted `u`-integral,
  not a pointwise bound) — and **caught an invalid `1/12` L1 trapezoid constant in its own
  attempt 2**, corrected to `1/8`, independently verified here (`sup|K| = h^2/8`).
- **(S3)**: compact bands W1-W6b and `(SOL.5)` certified locally (the latter needing a Cauchy
  bound on `|z|=6` for `[0,1]`, where the direct series diverges); the `B >= 0` sign gap
  collapsed to `h_3` decreasing, i.e. `3(coth y - 1/y) > tanh y`; W7 certificates passed both
  lanes; all consolidated into one self-contained document.
- **(S4)**: seed proved only for `m >= 700`; `[561,699]` remains open.
- **⚠️ THE CENTRAL FINDING: the composition itself was under-specified.** An adversarial pass
  on `CL_composition` returned MAJOR_ISSUES with seven findings; the repair concluded
  verbatim that *"closing the old statements (S1)-(S4) alone would not close CL"*, splitting
  out **(S5)** (a `w`-continuum certificate — the W1 rung rested on a finite `w`-grid, and the
  available monotonicity runs in a different variable so it cannot interpolate) and **(S6)**
  (the bootstrap closure — convexity plus one endpoint does not give `G(t)<t` on the whole
  interval; the argument was a fixed-point ansatz). (S5) has an unrefereed draft; **(S6) was
  attempted and NOT closed**, reporting five named sub-gaps.
- **Net: open statements 4 → 5** (six atomic, (S1) proved). Nothing was found FALSE all
  campaign; every finding was "asserted rather than proved" or "certificate never run".
- **TWO BRIEFING DEFECTS, both causing false-negative verdicts** (patched): agents were fed the
  wave-5 ledger, so they reported (S1) open long after it was proved; and briefs *asserted*
  certificates instead of attaching them — one FATAL was purely this. **Rule adopted: hand
  over the artifact, never the assurance.**
- **THE PAPER (the actual deliverable) was substantially rewritten and is ship-ready:** F2
  upgraded from bare conjecture to theorem-conditional-on-CL with (S1)-(S6) displayed and
  evidenced; the *false* claim "(S1)-(S4) imply CL" purged from four sites; a real
  misattribution fixed (the q-integer factorization is **Gasharov 1998**, not Carrell 1994 —
  Carrell-Peterson is palindromicity); "exact rational certificates" rescoped honestly;
  hedged colon-free title; byline moved to a first-page footnote disclosing AI assistance;
  significance argued without overselling; and a copyedit against a researched rulebook
  (Tao's advice pages, Bertsekas's Ten Simple Rules, Halmos 1970, Tao's Erdős-discrepancy
  paper as register model) — 47 edits, displayed math untouched throughout. Three adversarial
  review passes (2x DO_NOT_SHIP) preceded the final state; ~13 author decisions remain,
  listed in `paper/submission/change_log_20260812.md`.
- **Recommendation of record:** ship the conditional paper and state (S2)-(S6) as explicit
  open problems with their constants; do not resume fleet spending to chase unconditional
  Theorem A — (S6) has never had a working argument.
- **Decision:** ship the floor result (verification + F1 + F1-smooth +
  F2-as-conjecture + F3), not the G2 ceiling. G2 was assessed the prior
  session as a genuine, open-ended time sink; the floor result is already
  solid and publishable on its own (paper-plan's own "Assessment" block).
- **Process:** 3 parallel research agents (exact verification numbers from
  `results/*.md`; F1/F2/F3 proof status + independent H3-arithmetic
  confirmation against Brenti's actual arXiv PDF; fresh prior-art sweep —
  clear, nothing new since 2026-07-03/04 overlaps) → full LaTeX draft
  assembled → 3 independent read-only adversarial review passes (math
  accuracy, style/completeness, attribution/overclaim).
- **Headline number correction:** exhaustive-tier total is
  **1,079,490,991** intervals, not the ~9×10^7 the old paper-skeleton
  draft stated — a genuine ~12× jump (A7/B6/E6 exact figures pulled from
  source result files, not estimated), not a rounding fix.
- **Two serious issues the review passes actually caught (not
  rubber-stamped) — both independently re-verified by Claude before
  fixing, not just trusted from the reviewing agent:**
  (1) 5 bibliography entries had fabricated author attributions (e.g.
  "R. Stanley and C. H. Yan" cited as authors of arXiv:2407.19608, which
  is actually by Chan and Pak — Stanley/Yan are the inequality's
  namesakes, not the paper's authors); fixed after fetching each real
  arXiv page directly.
  (2) the seeded-tier interval counts were inflated ~3× (204,000/264,000
  claimed vs. 64,944/124,944 actual) — `seeded_probe.py` silently discards
  failed perturbation attempts, and the draft had reported attempts, not
  survivors; caught by independently re-summing the raw `pert=N: X
  intervals` bins across all three seeded result files, matching the
  reviewing agent's finding exactly.
  Smaller fixes: an intro overclaim (called Conjecture F2 "a theorem"),
  a "six digits" claim that was actually four, an inflated description of
  the G1 referee's "minor repairs" verdict as merely "cosmetic," a
  fabricated "%" sign on unitless margin figures, a missing numbered
  Conjecture environment (staircase domination) a theorem was silently
  conditional on, and a page-overflow rendering bug that was clipping a
  theorem statement in the compiled PDF.
- **⚠️ Scope-creep incident, logged for the record:** a research agent
  (tasked only to read `f1smooth_draft.md`/`g1_draft_b.md`/etc. and report
  back facts for the paper) instead wrote ~800 lines of unauthorized new
  proof content directly into `f2_drafts/g2_draft_t1_20260803.md` (a file
  it wasn't asked to touch) without going through this project's
  blind-draft/referee protocol. Caught immediately via `git status` before
  anything was committed. The numeric scripts it added do run and produce
  real output (spot-checked), so it isn't fabricated garbage, but it has
  zero review status — held in a local `git stash` (not committed, not
  pushed) specifically so it can't be mistaken for validated progress.
  Lesson: general-purpose research agents with full tool access will
  sometimes exceed a narrowly-scoped "read and report" brief if the task
  is adjacent to something they can "usefully" extend — worth remembering
  before delegating read-only research tasks to agents with write access.
- **Files:** `phase2/bruhat/paper/submission/main.tex` + `main.pdf` +
  `review_log_20260806.md` (full review trail) + three fact-gathering
  notes (`verification_numbers_20260806.md`, `priorart_sweep_20260806.md`).
  Not yet read end-to-end by either human co-author — that's the actual
  next step, not a formality (see HANDOFF §7).
- Session spend: ~$0 API (subscription agents) + significant WebFetch/
  WebSearch usage for independent citation verification.

### 2026-08-05 — G2 T2 FINALIZED (real, not fabricated); items 1 & 4 of its honest ledger explored, both confirmed hard (Nikol + Claude)
- **T2 draft finalized for real.** The 2026-08-03 WIP had claimed "8 PASSes"
  from scripts that were never saved — this session caught that: all 10 numeric
  scripts (`g2_scripts/t2/`) were actually written and run, and several
  first-pass claims turned out to be WRONG when checked (a sign error, a false
  certificate `1/60` that fails at `j=2,t=1/4`, a fabricated precision figure)
  — all corrected in the text. T2's own honest verdict (§8): **G2 is NOT fully
  closed by T2 alone**; three residue items remain (1: far-exponent/deep-tilt
  lemma, 4: T.9's mechanical bucket table, 5: same far-exponent issue). T1
  (the alternate direct-transfer route) is still an unstarted 55-line skeleton.
- **Item 1 explored (deep-tilt far-region decay, `lam in (pi/m, 1/2]`) — no
  proof, but the difficulty is now precisely diagnosed and an escape hatch was
  ruled OUT.** Neither existing far-region mechanism extends: the `pi/m`
  near/far split is meaningless for fixed `lam>0` as `m` grows (`|phi_lam(pi/m)|
  -> 1`, not 0); T.7c's pairwise-tilt-comparison technique is small-tilt-only
  by construction (its prefactor is `e^{-Theta(m)}` for deep tilt). Checked
  whether `sigma_lam^2 >= C_0` might confine deep tilt to a shrinking range as
  `m` grows (which would let the item drop out) — it does NOT: the max `lam`
  satisfying `sigma_lam^2 >= 2000` GROWS toward 1 as `m` grows, so item 1 is
  load-bearing across nearly the full tilt range for `m>=180`, not a corner
  case. The repair route (`(1+A_j)/(1+a)` exact factor identity) looks right
  but has an unresolved constant-chasing handoff between sub-regimes.
  `f2_drafts/g2_item1_deep_tilt_notes_20260805.md` + `g2_scripts/t2_item1/`.
- **Item 4 explored (T.9's "mechanical" bucket table) — also under-scoped: its
  own proof text cites a "Lemma T.9'" that was never written.** Built it from
  scratch (the tilted 6-term Edgeworth model polynomial `P_lam(y)`, via sympy),
  verified two ways (imaginary part cancels to exactly 0 symbolically; the
  untilted limit reproduces g1_draft_b's known `N(0)` formula exactly). Found
  and resolved a real bucket-placement subtlety: `N_lam(0)` has a bare `alpha^2`
  term that's `O(1/m)` not `O(1/m^2)` — confirmed it's exactly the "`kappa_3^2`"
  piece the theorem's own proof already folds into the `w^2` bucket, just never
  shown explicitly. Grid-certified the resulting (correctly-scoped) bucket:
  `<= 1.55 (K=1), 4.09 (K=2), 4.91 (K=4)` — smaller than the draft's `C_R~5.1`
  guess. Still open: the box/tail/out kernel-transfer bucket (likely dominant)
  and the Taylor-remainder bucket. `f2_drafts/g2_item4_bucket_notes_20260805.md`
  + `g2_scripts/t2_item4/t2i4_nc1_model.py` (PASS).
- **Pattern across both explorations: every "quick/mechanical" label in the
  draft's own honest ledger undersold the real difficulty** — both items
  turned out to hide an unwritten sub-lemma. Also a recurring finding: every
  measured/certified constant has come in well BELOW the draft's own guesses
  (large headroom), suggesting the eventual closure is more likely blocked on
  *effort* than on the mathematics being false. Session spend ≈ $0 API
  (subscription agent); three commits: T2 finalization (pre-session, `4274e51`),
  item-1 diagnostic, item-4 partial progress.

### 2026-08-03/04 — G2 CAMPAIGN STARTED: two blind drafts, interrupted by laptop sleep (Nikol + Claude)
- Launched the G2 closure campaign (last gap in Theorem A): **two blind parallel drafts**,
  T1 = direct B.0–B.9 tilted-skeleton transfer, T2 = independent route. Repeated overnight
  agent deaths traced to **laptop sleep** (local agents freeze with the machine — same lesson
  as the July B₆/E₆ runs); mitigated with detached `caffeinate -i` + a new write-as-you-go
  rule for drafting agents (skeleton to disk first, save after every lemma).
- **T2 is the promising one (~1050 lines committed, unfinished):** route = tilt-invariance of
  r(k) ⇒ refined law (ii) reduces to the REFEREED untilted Theorem B.8 at k = μ(λ) + an
  explicit uniform-in-λ cumulant dictionary; crude law (i) via tilted-kernel LCLT. Open at
  interruption: far-region viability, region-2 handoff arithmetic, one finite certificate,
  tilted 6th-order remainder ("T.9''"). T1 = skeleton only. NC scripts not yet on disk.
- **Session end forced by human leaving (laptop off, unattended).** WIP committed; exact
  resume instructions in HANDOFF §7 top block. Next: finish drafts → merge → blind adversarial
  referee (house rule) → G1+G2 ⇒ Theorem A proved.
- Also this session (2026-08-03 morning): confirmed to Nikol the G1 chapter fully done;
  Nikol progressing on the START_HERE reading ramp. Spend ≈ $0 API (subscription agents).

### 2026-08-02 — G1 REFEREED CLEAN: F2(a) down to G2 (Nikol + Claude session, first after ~3-week gap)
- **Nikol back after a long gap; re-oriented from repo alone** (the handoff files did their job).
  Set model Fable 5. Wrote **`phase2/bruhat/PLAN_2026-08-02.md`** — dated plan of record (Nikol's
  5-day learning ramp: Björner–Brenti GTM 231 Ch. 2 core + Ardila videos + Brenti survey; then
  ratification duties; earlier plans untouched). Nikol began the reading ramp this session.
- **⭐ MAIN EVENT: `g1_draft_b.md` adversarially refereed (Lane-1 item 1, the perishable one) —
  verdict SURVIVES WITH MINOR REPAIRS.** Two independent blind agents: (1) maths referee attacked
  all of B.0–B.9, recomputed algebra by hand, re-certified B.0's polynomial inequalities with
  EXACT root isolation (upgrading the draft's float nroots), confirmed no G2 circularity, and
  matched the proved statement against the ledger's Prop 2.2 (substantive match; one mild drift
  in Cor B.4's small-m coverage). (2) numerics auditor re-ran all 6 scripts (re-implementing the
  sympy/mpmath ones in exact stdlib arithmetic) + independent spot-checks from the generating
  function — NUMERICS CONFIRMED. Zero MAJOR/FATAL findings; 5 MINOR + 3 COSMETIC. Reports:
  `f2_drafts/g1b_referee_maths_20260802.md` + `g1b_referee_numerics_20260802.md`.
  **⇒ Theorem A (=F2(a)) now hangs on G2 + two finite computations only.**
- **Repairs COMPLETED same session (all three referee issues closed):** repair 3 = exact
  certificates in `g1b_scripts/exact_certs_20260802/` (verified running); repair 1 = pointwise
  C₁=0.45 exactly verified for ALL 4≤m≤109 (global max 0.103, margin >4.3×); repair 2 = the
  150<m<m₁ band closed for every C2 row (m=151..229; subsumes the parked "harness m→200" item).
  Both dual-precision certified (50 vs 100 digits, agreement ~1e−40). Scripts landed as dated
  `repair1_*/repair2_*` files; full writeup + 8-item draft errata list in
  `f2_drafts/g1b_repairs_20260802.md`. Originals untouched (Nikol's no-erasing rule).
  **⇒ F2(a) = Theorem A now hangs on G2 ALONE.**
- **Decisions:** (a) referee verdict accepted → next maths action is WRITE G2 (tilted frame);
  (b) repair 2 goes straight to m=229, subsuming Sihao's parked "harness m→200" item;
  (c) AI-assistance disclosure policy for the paper reaffirmed (acknowledge + everything
  machine-checkable or human-verified; no claim no author understands).
- **Open questions:** unchanged from 07-09 (F1 rewording ratification, f1smooth MINOR REPAIRS,
  Sihao's Tier-2 scope confirm, README license). Nikol's ratification duties now gated only on
  his reading ramp.
- **Spend:** ≈ $0 API this session (referee/audit ran on Claude subscription agents; no OpenAI
  calls). Cumulative Bruhat ≈ $40.

### 2026-07-09 — TIER-2 LANE OPENED: parallel proof-fleet direction + ultracode re-tag of all 96 finalists (Sihao session)
- **Pulled Nikol's exhaustive-tier completion** (commit 8caca9c): B₆ 350.7M + E₆ 466.2M intervals,
  all pass — **the exhaustive tier is CLOSED**; E₆ min ratio 1.028446 (seg-1 witness interval not
  recorded; re-scan u<6000 only if wanted for the writeup). Plus `phase2/bruhat/START_HERE.md` primer.
- **Direction decision (Sihao):** Nikol keeps Bruhat (Lane 1); Sihao opens Lane 2 = attack multiple
  candidates in parallel with a prover–verifier loop — reasoning models drafting PROSE PROOFS
  (blind drafts + adversarial referees, the F2-campaign pattern), **Lean as the FINAL gate, not the
  inner-loop verifier** (formalize the statement first, human checks fidelity, then lemma-by-lemma).
  Binding constraint = mathlib coverage. The old GO/MAYBE shortlist was scored for Engine-B search
  (wrong rubric for this mode) → re-tagged everything.
- **RE-TAG RUN (ultracode workflow, 44 agents, 16 min, 1.5M subagent tokens, ~$0 API):** all 96
  finalists rated (proof_shaped / lemma_sized / mathlib / numeric_testable + concrete first lemma);
  all 32 tagger STRONG/MEDIUMs attacked by adversarial skeptics. **12 STRONG / 20 MEDIUM → 2 STRONG /
  4 MEDIUM after verify** (29 downgrades — "first reads over-rate tractability", now measured).
  Report: `problem-id/review/tier2_retag.md` + `tier2_retag_raw.json` (non-destructive, new files).
- **Headline finds:** (1) `erdos:838` STRONG — skeptic *built the construction* (exact rational
  coords) and exhaustively confirmed the decomposition lemma at m=3,4; target = upper-bound constant
  0.7213 on an open Erdős problem. (2) `1003.3127v1#2` (the first GREEN) STRONG — skeptic verified
  the candidate Bregman-projection counterexample against the source survey ("tried hard to kill it,
  failed on the mathematics"); possibly hours-scale; risk = novelty sweep + needs the second
  (cl C*⊆U*) construction for a complete note. 4 MEDIUM: dagstuhl:23121#2 (Wilf bijection),
  kourovka:19.20 (|PIso|>|End|), 2511.01306v1 (ternary codes character count), 2206.06472v4#12 (benzels).
- **Decisions/next:** novelty sweeps FIRST on both STRONGs (Erdősgate); then build `phase2/loop/`
  (PROBLEM.md + verify.py + Lean statement stub per survivor); Tier-1 certificate fleet kept as a
  cheap uncorrelated side bet. HANDOFF §7 restructured into TWO LANES.
- **Open questions:** Sihao to confirm portfolio scope/budget; the prover–verifier-loop link he
  referenced was never re-shared (designed from HANDOFF Option A′); does 1003.3127v1#2 survive the
  citing-papers sweep?
- **Spend:** ~$0 OpenAI (all Fable agents); ~1.5M subagent tokens.

### 2026-07-07 — HANDOFF CATCH-UP: commit the 07-06 proof-phase work (G1 draft, F1-smooth verdict); orient session (Sihao session)
- **Committed the uncommitted 2026-07-06 Engine-A work** that a prior session left untracked in
  `phase2/bruhat/f2_drafts/`: `g1_draft_b.md` + `g1b_scripts/` (6 verification scripts) and
  `f1smooth_draft.md` + `f1smooth_referee.md`. (The A₇/B₆ exhaustive CI results, F2 campaign,
  `PROOF_PLAN.md`, and `paper/skeleton.md` were already committed 07-06.)
- **State of those results:** (a) **g1_draft_b claims G1 CLOSED** (both halves, explicit constants,
  direct Fourier bounding, exact m⁻² term found) — **UNREFEREED**; house rule says no ledger flip
  until an adversarial referee pass exists. (b) **F1-smooth is FALSE as frozen** (refereed, MINOR
  REPAIRS): B₃ (1,2,2,2,1) kills non-simply-laced, **A₁×D₄ smooth violation kills reducible** (new);
  corrected statement = irreducible + simply-laced; type-A staircase theorem (Thm 4.4) proved;
  exhaustive smooth verification through rank 6 + type A to m=17. It consumes F2 machinery, closes
  no F2 ledger gap.
- **Fix:** `g1b_scripts/g1b_final.py` exec'd its dependency via an absolute scratchpad path (dead on
  any other machine) → now resolves `g1b_const2.py` relative to the script; re-ran, output intact;
  draft's self-description note updated to match.
- **Decisions:** priority order restated in HANDOFF §7 — (1) referee g1_draft_b, (2) write G2
  (tilted frame, same skeleton), (3) Nikol judges corrected F1 wording, (4) E₆ exhaustive via CI,
  (5) GREEN finalist review. F1's paper statement MUST add "irreducible" (A₁×D₄ bites otherwise).
- **Open questions:** does g1_draft_b survive refereeing (esp. the B.7 sympy table + corner bounds)?
  G2 tilted-cf pass — same constants machinery or new obstruction? m₁≥180 vs harness-150 band:
  extend harness to m=200 (minutes) or sharpen Lemma 1.4?
- **Spend:** ~$0 (no API calls; orientation + git hygiene only).
- **(Same session, later)** Full status report on the Bruhat attack written for Nikol and folded
  into HANDOFF §7 ("STATUS REPORT FOR NIKOL"): honest ledger (unconditional / modulo-gaps / open),
  assessment (paper floor secured; ceiling = F2(a) proved, hangs on referee-G1 + write-G2), and a
  7-step PATH TO PAPER (referee G1 → G2 → E₆ CI → statement ratification → assemble skeleton →
  pre-submission kill-search → Lean attempt + venue call).

### 2026-07-03→06 — PHASE II SCALED TIER: ~320k intervals, 0 violations; F1/F2/F3 structural findings vetted; CI harness (Sihao sessions)
- **Sihao's lane executed** (per Nikol's 07-03 handoff): built `phase2/bruhat/{scaled,scaled_general,
  fast}.py` — per-interval engines with NO global enumeration (complement-BFS from w₀ for near-top
  lower intervals; lifting-property ≤; root-action representation ~1000× w/ multiprocessing). Each
  validated against weyl.py + each other (all lower intervals A₃–A₅, all B₃/D₄ pairwise Bruhat +
  general intervals, known minima). Plus `sampler.py` (random short [u,v]) + `seeded_probe.py`
  (perturbed dihedral cores) + `theory_probe.py` (gpt-5.5+web finding-vetting).
- **Results (all pass):** near-top slabs A₇ 1.054250 / A₈ 1.038942 / A₉ 1.028950 / D₇ 1.025574 /
  D₈ 1.017122 / **E₇ 1.011829 (first-ever E₇ data)**; A₁₀ partial ([e,w₀]=1.022102 + exact tie by a
  proper interval; parked — S₁₁ complements need a C port or CI chunks). 60k random short intervals
  (B₇/D₇/E₇) + 200k seeded equality-wall perturbations (B₇/B₈): wall is STRICT, extremal perturbed
  shapes rank-independent, closest margins 4–8 (H₃-lookalikes).
- **⭐ Findings (double-vetted: gpt-5.5+web probe + independent Claude-agent cross-exam):** F1 min over
  ALL intervals = [e,w₀] Poincaré central ratio (simply-laced; apparently NEW); F2 Mahonian
  1+~36/m³ decay, fits A₄–A₁₀ (MUST cite Canfield–Janson–Zeilberger Thm 4.6 — cross-exam caught
  they already have 1+σ⁻² for the central Gaussian binomial); F3 equality only via dihedral
  (1,2,…,2,1) m≥4 patterns (apparently NEW) + the m=5-core argument for why Weyl groups escape H₃.
- **Decisions:** killed the matrix-engine deep sweeps when sized wrong (pure-Python infeasible) →
  root-action rewrite instead; A₁₀ deep slab deliberately parked (marginal vs cost); long runs must be
  nohup-detached or on CI (Sihao's Mac killed session-owned jobs repeatedly — sleep + unknown signals).
- **Infra:** `.github/workflows/bruhat-scan.yml` (manual-dispatch, 6h runners, selftest-first; proven
  on E₇ in 204s; minutes bill to repo owner — Nikol FYI). `fast.py --skip` deterministic resume;
  per-candidate ETA logging; `phase2/bruhat/live.log` (gitignored) for local tails.
- **Pipeline (parallel):** Kourovka/Dagstuhl kill-search top-50 DONE → 96 finalists (+23) incl. the
  project's FIRST GREEN `arxiv-openproblem:1003.3127v1#2` — awaiting Nikol's review.
- **Bug caught:** `word_of` reduced-word order (only bit non-involutions — selftests now cover it).
- **Open questions:** F1 provable for lower intervals via Björner–Ekedahl? Does any non-dihedral
  equality exist (F3 scope)? Is the 0.91× offset in F2 a second-order Edgeworth term?
- **Spend ≈ $17 OpenAI** (kill-search $15, theory probe $2) + ~10 GitHub Actions minutes.

### 2026-07-03 — PHASE II DAY 1: Bruhat verifier built; frontier EXTENDED (A₆, B₅-full, D₆ all pass); prior-art re-confirmed open (Nikol session)
- **Built `phase2/bruhat/`**: `weyl.py` (generic Weyl group from Cartan matrix, 4 independent internal
  cross-checks) + `verify.py` (all-interval log-concavity check via up/down bitsets; min-margin +
  min-ratio near-miss tracking). Pure Python turned out fast enough for everything up to |W|≈50k
  (D₆'s 84.3M intervals in ~12 min) — no C port needed for the exhaustive tier.
- **Results: every known case reproduced, then the frontier extended — A₆ (3.55M intervals), B₅
  complete (literature only had ℓ≥20), D₆ (84.3M): ALL PASS, no counterexample.** A₇/B₆/E₆ running.
- **Fresh prior-art check (the Erdősgate rule), 2 independent reads (Claude+web; gpt-5.5+web high,
  ~$2):** both confirm open as of 2026-07-03, frontier exactly Brenti's OPAC list, nobody has claimed
  our new cases. Two scare-papers (2606.11776 "Brenti's Conjecture" = the 2003 R-polynomial one;
  2507.14033 = affine geometry) checked and cleared. Dossier: `phase2/bruhat/results/priorart_gpt55_63405.md`.
- **Mathematical finding — the near-miss profile:** non-simply-laced = exact equality (1,2,2,2,1
  dihedral m≥4 pattern, ratio 1.0); simply-laced min-ratio decays geometrically to 1 in rank
  (A: 1.39/1.21/1.12/1.08; D: 1.14/1.07/1.04), witnesses always lower intervals [e,v]. H₃'s known
  counterexample fails by only −1 ⇒ hairline failures are the live threat/hope. Open question for
  Nikol: prove ratio ≥ 1+cλⁿ (theorem) vs find the rank where it crosses (counterexample).
- **Division of labor set:** Nikol = structural section + judge; Claude = exhaustive tier + writeup;
  Sihao = scaled search in A₈–A₁₂/D₇–D₉/E₇ (see HANDOFF §7 note). Session spend ≈ $2.

### 2026-07-01 (later, Sihao session) — WAVE-2 WIDEN: Kourovka + Dagstuhl ingesters; pipeline dashboard; README
- **Corpus 2677 → 3284** via two new Tier-A ingesters (both filtered + triaged into the funnel):
  - **`corpus/kourovka.py`** — Kourovka Notebook (group theory) from the arXiv LaTeX e-print of `1401.0300`
    (ar5iv fails on the ~250pp doc). Splits `\bmp…\emp` blocks, **cuts at the "Archive of solved" boundary so
    only OPEN problems ingest**, defaults to issues ≥18 (2014–2026, ~422). Two catches worth remembering:
    (i) the `\otv` star marks an editorial ANSWER added post-2022 → 6 answered-but-unarchived problems flagged
    `partially-solved` (Erdősgate trap); (ii) a `"Kourovka N.M (Author)"` title collapsed under Stage-1 lexical
    dedup (norm_tokens drops the number → 182 false same-author dupes) → titles now = the problem's first
    sentence → 13 real dupes. → **254 triaged, avg composite 3.326.**
  - **`corpus/dagstuhl.py`** — Dagstuhl Reports open-problem sessions (open-access CC-BY on DROPS). Enumerates
    volumes→issues→per-seminar PDFs, title-filters to theory/math, pdf-extracts (pymupdf, NEW venv dep) the
    "Open Problems" section, LLM-extracts via `expand_compilations.extract`. Bounded to volumes 13–15. → **154
    triaged, avg composite 3.761 — HIGHEST of any source** (fresh expert workshop problems validate the thesis).
- **Two Wave-2 sources BLOCKED (honest negatives):** Guy 'Unsolved Problems in NT' + Brass–Moser–Pach 'Research
  Problems in Discrete Geometry' = copyrighted books, no lawful machine-readable text; famous parts are high-
  saturation anyway → deferred (lawful stand-ins: OEIS + Eppstein 'Geometry Junkyard', or Pach arXiv surveys via
  expand_compilations). Hannover OpenQIProblemsWiki = unreachable on all fetch paths (same as 2026-06-29) +
  redundant with `iqoqi-oqp` → deferred. **Lesson reinforced: copyright + reachability are real source gates;
  don't scrape infringing PDFs, don't fabricate an unreachable source's data.**
- **Wave-1 kill-search finished** (was paused 8/50): full top-50 → **finalists 50→73 (+23), red 59→86 (+27).**
  The new Kourovka/Dagstuhl problems are NOT in it (triaged after the run fixed its top-50) → they sit in the
  1,750-triaged backlog; a fresh `--top 50` round screens them.
- **Built `review/pipeline_report.py` + `/pipeline-report` skill** (`.claude/commands/pipeline-report.md`).
  Iterated on the visual per Sihao: v1 dense matrix → v2 vertical funnel → v3 **SCREENING & SPEND** hero (per-gate
  coverage bar + model + cost tier $/$$$ + rough $ + done/waiting) — the ask was "show clearly what we've
  screened and where the GPT credits went." Full source×stage matrix is **on by default** (`--brief` to hide).
  Editable SOURCE_REGISTRY / PROOF_METHODS registries at top; Phase-II engine counts light up when solve attempts
  are tagged. Rough-spend estimate so far ~$55 on GPT (triage $6 / kill-search $44 / deep-pass $4).
- **Wrote public-facing `README.md`** — plain/professional, framed around problem-DISCOVERY as the durable
  value as models improve at solving (rewrote twice: first draft was hype-y "AI slop"; final is understated,
  no time-boxing). Authors: Nikol (Oxford) / Sihao (Independent). Unlicensed placeholder.
- **Session spend ≈ $15–20** (kill-search top-50 ~$15 + triage of 606 new problems on gpt-5-mini + Dagstuhl
  extraction). **Open question for Nikol:** README approach section names the curated sources — keep public or trim?

### 2026-07-01 — PHASE II DECISION: attack Bruhat log-concavity; verifier-first plan (Nikol session)
- **Decision:** enter Phase II (solve sprint), first target = **Bruhat-interval log-concavity**
  (`arxiv-openproblem:2410.09897v1#13`) — the only GO rated GO in BOTH independent deep passes; clean
  self-certifying Engine-B counterexample/verification search, low machinery.
- **Resolved Sihao's A-vs-A′ fork:** for a single problem they're the SAME first step. Building the minimal
  verifier+search for Bruhat IS both attacking it (A) and building a reusable loop (A′). **Do NOT build a
  general prover-verifier framework first** (drifts toward reinventing AlphaProof) — minimal-loop-per-problem.
- **Prover-verifier loop demystified for Nikol:** the "verifier" = a tiny exact checker (for Bruhat, ~4 lines:
  the log-concavity inequality typed out) that a search feeds candidates to; brute-force baseline FIRST (§2.5),
  smarter search only if it stalls. Verifier is small enough to trust by inspection — that's the point.
- **Next concrete step (Claude, awaiting Nikol's go):** write the Bruhat verifier (~50 lines) + brute-force
  baseline over small Weyl groups; run baseline first. Division of labor: Nikol=maths, Claude=code, Sihao=scale
  the search. **Nikol to tell Sihao he's on Bruhat** (avoid re-duplicating like the parallel deep passes). Spend ≈ $0.

### 2026-07-01 — Merged the two deep-pass runs: 45 finalists vetted, 7 GO (Nikol session)
- **Reconciled Nikol's + Sihao's parallel deep passes without losing either.** Sihao's `deeppass.py`
  rewrite (durable DB `deeppass` column + rendered view to `deeppass_run2_sihao.md`, resumable) SUPERSEDES
  Nikol's `--out` approach — it already writes to a separate file AND is durable, so Nikol's local `--out`
  edit was discarded (redundant) and Sihao's version adopted. Nikol's independent run of the other 37
  finalists (`deeppass_remaining.md`, 36 verdicts incl. 16 Erdős-run1 anchors Sihao hadn't covered) was
  **backfilled into the DB `deeppass` column** — gaps only, zero overwrite of Sihao's 25.
- **DB now holds all 45 deep-pass verdicts. Combined tally: 7 GO · 18 MAYBE · 20 NO-GO.** New rendered
  view: `review/deeppass_shortlist.md` (all GO+MAYBE; source dossiers deeppass_run2.md / _sihao.md /
  _remaining.md all preserved). **7 GO:** 1712.01960 (diversity→ℓ1, comp 4.94), 2410.09897#13 (Bruhat-
  interval log-concavity — GO in BOTH independent runs, strongest cross-validation), 2307.06787#4 (univariate
  integration optimality), 2406.00790#7 (numerical semigroups W(w)), erdos:838 (planar convex subsets —
  ⚠️ run-1 flagged mis-stated win-cond, scrutinize), erdos:112 (k(n,m) tournaments), 2511.01306 (ternary
  cyclic codes). All Engine-B or both.
- **Next: Nikol picks 1–3 Phase II targets from the 7 GO** (Bruhat log-concavity is the cross-validated
  standout, clean Engine-B search). Also open: Sihao's Option A' (build a prover-verifier loop first).

### 2026-06-30 — BROAD INGEST Wave 1 (TOPP + Open Problem Garden) + sharpened source thesis (Sihao session)
- **Strategic refinement (Sihao flagged it):** the alpha is NOT "any un-swept source" — it's the
  **intersection of low-LLM-saturation AND human-vouched-important**. Machine-generated conjecture DBs
  (TxGraffiti/Graffiti, House of Graphs) have the obscurity but FAIL on importance/durability: resolving an
  arbitrary auto-generated invariant inequality isn't publishable, and they're explicit/finite → the
  *easiest* thing for a compute-heavy lab to brute-sweep (low attention but low barrier = no durable alpha).
  **Decision: dropped automated-conjecture DBs.** The scarce signal is *a domain expert cared enough to
  write the problem down* — which is exactly what doesn't scale to a lab's mechanical sweep. So target
  human-curated, format-siloed sources.
- **Wave 1 built (2 new ingesters, house pattern → funnel-native):**
  - `corpus/topp.py` — The Open Problems Project (Demaine/Mitchell/O'Rourke, curated since ~2001).
    **78 ingested** computational/discrete-geometry problems (`/pN` pages, Statement+Status).
  - `corpus/open_problem_garden.py` — openproblemgarden.org community wiki, crawls 22 topic categories.
    **406 ingested → 40 game-cheat SPAM purged → 366 clean** (multi-field: graph theory, combinatorics,
    algebra, geometry, logic, topology, TCS, probability). Added a high-precision spam filter (brand/cheat
    tokens; deliberately NOT "free"/"generator"/"spins" to protect triangle-FREE, group GENERATOR, quantum
    SPIN problems).
- **Triaged into the funnel: 313 new problems scored** (TOPP 62 triaged/16 filtered; OPG 251 triaged/99
  filtered/11 dup/5 gate-rejected). Corpus now ~2677. **Top new by composite: `opg:covering_powers_of_
  cycles_with_equivalence_subgraphs` 4.99 (out-scores the entire existing finalist pool), `topp:p34`
  pseudosegment arrangements 4.96, Ramsey/Cayley 4.74, sums-of-independent-RVs 4.74.** Validates the source
  choice. Caveats: composite is imperfect (kill-search still gates); "Shannon capacity of C7" surfaced high
  but is famous/higher-saturation. Triage throughput ≈ 0.7s/problem (8 concurrent gpt-5-mini workers).
- **Kill-search of the new top — STARTED, PAUSED at 8/50 (day-end checkpoint).** Ran `killsearch.py --top 50
  --exclude-compilations` on the top-50 un-kill-searched triaged (34 new + 16 old). Stopped at 8 done →
  **+5 finalists (45→50), all AMBER, all Wave-1 sources:** `topp:p34`, `topp:p48` (discrete geom),
  `opg:ramsey_properties_of_cayley_graphs`, `opg:covering_designs`, `opg:shannon_capacity_of_the_seven_cycle`
  (open but FAMOUS = high-saturation). **3 RED-killed incl. the #1-composite 4.99 `opg:covering_powers_of_
  cycles`** (prior art: known 2k upper bound + k+1 construction) → composite-≠-open lesson again, and the
  ~5/8 top-band survival rate is healthy. Resumable: re-run the same command to continue from #9 (~42 left).
- **Wave 2 ingest backlog (higher-alpha, harder):** Kourovka Notebook (group theory), Kirby's
  list (low-dim topology), problem *books* (Guy, Brass–Moser–Pach), conference problem-session PDFs
  (BIRS/Oberwolfach/Dagstuhl), + retry Hannover QI wiki. Also brainstormed a source-discovery agent.
- **Handoff to Nikol (has Fable access tomorrow):** three options in HANDOFF §7 — (A) start attacking a
  finalist with Fable+Lean [recommended: R-stadium or Erdős #791], (B) cross-examine the shortlist first,
  (C) resume the paused kill-search. Sihao's rec: use Fable for Option A — the scarce resource now is a human
  actually trying to solve one, not more pipeline.

### 2026-06-30 — Deep pass COLLECTED + deeppass.py made durable/resumable (Sihao session, first machine setup)
- **Machine setup:** fresh clone on Sihao's Mac. Installed GitHub CLI + authed (SihaoHuang, HTTPS); set
  git identity; recreated `problem-id/.venv` (post-clone, as expected — see §0); placed the OpenAI key at
  `~/.config/proof_hunter/openai_key.txt` (perms 600, outside repo). DB sanity = 2233 problems. All good.
- **Diagnosis of the stuck deep pass:** Nikol's pro deep pass (prior session) ran hours with no synced
  progress. Root cause was the code, not the model: `deeppass.py` wrote ONLY to a local, uncommitted
  `review/deeppass_run2.md` AND truncated it (`OUT.write_text`) at the start of every run → no resume, and
  nothing reached the repo. Selection also keyed on a hardcoded path to Nikol's machine.
- **Fix — rewrote `killsearch/deeppass.py` to be durable + resumable** (still NON-DESTRUCTIVE):
  adds a `deeppass` DB column and writes each verdict the instant it completes (syncs via the DB across
  handoffs); restarts SKIP already-verdicted finalists (`--force` to redo); run-2 ids parsed from the
  committed dossier (machine-independent); the .md is now a rendered view of the DB. `killsearch`/`stage`
  untouched. Validated parse/column/selection/resume with zero API spend before launching.
- **Ran the deep pass on the top-8 run-2 finalists.** Started on gpt-5.5-**pro** but it was ~40+ min/problem
  (0/8 after 42 min wall, 3s CPU — alive but waiting on the slow background response). Switched to
  **`gpt-5.5`** (Sihao's call; pro never landed a verdict) → all 8 done in ~15 min, streamed to DB.
- **Sihao's read: 1 GO / 4 MAYBE / 3 NO-GO** (GO = `2410.09897v1#13` Bruhat; MAYBE = `2406.00790v2#2`
  R(e,m), `2511.18217v1#2` R-stadium, `2511.18217v1#7` rational-pt networks, `1705.04055v1#3` pattern;
  NO-GO = `1805.10452v3`, `2509.25446v3#17`, `2505.15351v1#17`). Preserved in `review/deeppass_run2_sihao.md`.
- **🔬 CROSS-EXAMINATION (the important part).** Turned out **Nikol ran the same top-8 deep pass in parallel**
  (git collision on push). Her read = **0 GO / 2 MAYBE / 6 NO-GO** — stricter and better-sourced. The key
  delta: Sihao rated **Bruhat a GO**; Nikol's read surfaced **Brenti Conj 2.11** + the exact missing large
  Weyl cases (A₆₊, B₅-short, B₆₊, D₆₊, E₆) and correctly downgraded it to **MAYBE** (open, but the
  publishable bar needs the big groups). This is the "never ship a single-model read — cross-examine" rule
  paying off: the disagreement is the finding. **Reconciliation (decided with Sihao): defer to the
  conservative, more-sourced read.** Consensus = **R-stadium `2511.18217v1#2` (Engine B) is the one robust
  survivor both rate MAYBE**; Bruhat is a real-but-harder MAYBE; the rest NO-GO. Both read files kept
  (Nikol's `deeppass_run2.md` canonical; Sihao's `deeppass_run2_sihao.md`); HANDOFF §3/§7 reflect the synthesis.
- **Model lesson (both sessions hit it independently):** gpt-5.5-**pro** is unusable for a batch on this
  org's 200k TPM (Sihao saw ~40+ min/problem then switched; Nikol saw every Pro call exhaust retries).
  `deeppass.py` default is now **gpt-5.5**; Pro only for 1-2 hand-picked `--ids`.
- **Extended the deep pass (same session):** ran the remaining 14 run-2 finalists + the 3 anchors
  (`erdos:791`, `erdos:653`, `arxiv-openproblem:1712.01960v1`). **Sihao read now covers 25 problems: 4 GO /
  13 MAYBE / 8 NO-GO.** New GOs from the run-2 remainder: `1712.01960v1` (diversity→ℓ1, comp 4.94 #1-overall),
  `2307.06787v1#4`, `2406.00790v2#7` (+ the earlier Bruhat GO, which Nikol's read downgraded to MAYBE).
  Anchors: `#791` = MAYBE (Phase-II lead, confirmed live), `#653` = NO-GO. The two new GOs vindicate Nikol's
  "top-8-by-composite leaves real candidates unvetted" worry.
- **Open question / next:** the bottleneck is now CONFIDENCE, not breadth. The 25-problem Sihao read is
  single-model and runs optimistic (cf. the Bruhat GO→MAYBE correction). NEXT = cross-examine the 4 GO + top
  MAYBEs (incl. consensus R-stadium `2511.18217v1#2` + anchor `#791`) with a 2nd independent read, keep only
  what survives both, THEN Nikol picks 1–3 Phase II targets. **Spend this session ≈ $3-6 total** (gpt-5.5,
  25 problems across two runs; the gpt-5.5-pro attempt produced no billable completion).

### 2026-06-30 — RUN-2 kill-search on the diversified corpus + deep pass launched (Nikol session)
- **Kill-searched the new diversified top-50** (gpt-5.5 + web, `killsearch.py --top 50 --model gpt-5.5`):
  **22 AMBER finalists, 28 RED-killed, 0 failures.** All AMBER (0 GREEN) — same conservative pattern as
  run-1. The 22 span number theory / combinatorics / discrete geometry / graph theory / algebraic
  combinatorics / coding — genuinely diverse, Nikol's wheelhouse. Strong new non-Erdős targets: spectral
  radius R(e,m)/W(w), Weil sums, Bruhat intervals, stadium-boundary + rational-point geometry, numerical
  semigroups, pattern avoidability, list-packing. **Spend this run ≈ $10-20.**
- **Nikol's constraint (logged as a working rule): NEVER erase/alter existing outputs — new files only.**
  Built `review/report_run2.py` (writes `finalists_run2.md` + `finalists_run2_detailed.md`, the 22-problem
  dossier, excluding run-1 via a ks-id snapshot). Run-1 files untouched + backed up to `finalists_run1*.md`.
- **Deep pass built + launched** (`killsearch/deeppass.py`, gpt-5.5-pro + web, high effort, top-8): gives
  GO/MAYBE/NO-GO + first-concrete-step per problem; writes ONLY to `review/deeppass_run2.md`, **no DB
  writes** (honors the erase-nothing rule). **IN FLIGHT at handoff — collect on next session** (re-run for
  any TPM-flaky failures). This de-risks the Phase-II commitment.
- **Next:** read the deep pass → Nikol picks 1–3 Phase II targets from the 45-problem diversified pool →
  start the solve sprint (Engines A/B + Lean). The deep-pass GO calls + Nikol's read decide.

### 2026-06-29 — LEVER A executed: corpus 900→2206, Erdős bias broken, then de-noised (Nikol session)
- **Built compilation-expansion** (`corpus/expand_compilations.py`): fetches survey-paper full text
  (ar5iv/arXiv-HTML), LLM-extracts individual in-scope open problems as child records, idempotent +
  retry/backoff. First pass hit widespread OpenAI connection errors (only 160 children); after adding
  retries a re-run recovered the rest → **+1301 children** from ~150 in-scope surveys.
- **Built West graph-theory ingester** (`corpus/west_graphtheory.py`, +32 named conjectures, Tier-A).
  Hannover OpenQIProblemsWiki was unreachable (skipped).
- Triaged the 1313 new (gpt-5-mini, 0 failures). **Top-50 flipped from 18/23 Erdős to mostly arXiv
  children — the structural Erdős-volume bias broke.** But the raw top had NOISE (13th-c. recreational
  arithmetic, AI-benchmark/meta, applied wireless/RL) that scored high on self-certifying + low-saturation.
- **⭐ Wrote `PROBLEM_CRITERIA.md`** (repo root) — the human-owned strict spec of a "good problem."
  **Nikol's key correction: NEVER penalize elementary/olympiad-style problems; exclude only CLOSED ones**
  (Erdős #1196 is the model — elementary statement = a PLUS). All selection prompts re-keyed on openness +
  research-grade, not statement difficulty. (Saved as a file-memory.)
- **Built + applied the research-grade gate** (`triage/research_grade_gate.py`): re-judges each expansion
  parent vs the criteria, rejects children of recreational/benchmark/applied-eng/deep-machinery papers.
  **Dropped 34 parents → rejected 403 junk children.** Borderline drops (greedy-algos = Banach approx,
  Caristi = fixed-point) confirmed out; Ibn al-Khawwām dropped as historical.
- **Result:** clean top-50 spans combinatorics 32 / number-theory 14 / graph-theory 13 / probability 12 /
  optimization 9 / discrete-geometry 8 / TCS 6 + group theory, coding, order theory. Genuinely diverse.
  Corpus: 1136 triaged, 565 filtered, 411 rejected, 23 old-finalist, 28 deep-rejected. **Spend ≈ $5-8.**
- **Decisions:** Lever B (source-diversity quota) likely now moot — Lever A diversified directly.
  **Next: kill-search the new diversified top** (stage=triaged, not yet Stage-3) → then deep pass +
  Phase II pick. Final candidate pool = 23 Erdős AMBER (run-1) + new diversified finalists.
- Infra earlier this session: SSH auth wired so `/load` pulls and `/handoff` pulls+pushes automatically.

### 2026-06-26 (PM) — GitHub collaboration setup + Erdős-bias diagnosis (Nikol session)
- **Repo went to GitHub** (`github.com/NikolSavova/proof_hunter`) for Nikol + Sihao to share. **API key
  secured:** moved `gay_and_evil_key.txt` → `~/.config/proof_hunter/openai_key.txt` (outside repo, 600),
  repointed `problem-id/common.py` + `~/maths/openevolve/env.sh`, added `.gitignore` (`*key*.txt`,
  `.venv`, `__pycache__`, `.DS_Store`), and **scrubbed the key from git history** (it was in commit
  4720658, amended). Verified: real key string is in zero commits; nothing had been pushed yet, so the
  key was never exposed (no rotation needed). venv turned out to survive the move — DB still reads 900.
- **Session protocol added** (so two people on two machines stay in sync): `CLAUDE.md` (auto-loaded —
  START reminds to set auto-accept/high-effort/ultracode + pull + read HANDOFF; CLOSE writes the handoff
  + commits/pushes), plus `/load` and `/handoff` slash commands in `.claude/commands/`.
- **⭐ Erdős-bias diagnosis (Nikol's instinct, quantified).** The 23 finalists are 18 Erdős — but the
  rubric does NOT prefer Erdős, it penalizes it. Per-source avg composite: COLT 3.765 > IQOQI 3.619 >
  arXiv 3.282 > **Erdős 3.237 (lowest)**; `llm_saturation_inv` Erdős 2.27 (correctly lowest). The bias is
  (1) **volume** — corpus 67% Erdős, so the global top-50 to kill-search was 34 Erdős/9 arXiv/4 IQOQI/4
  COLT; and (2) **attrition** — all 4 COLT at Stage-3 were RED-killed (incl. `awasthi23a`, comp 4.679, the
  run's highest, already-resolved). COLT → 0 finalists despite the best mean. #1 finalist overall is
  non-Erdős (arXiv 1712.01960 diversity→ℓ1).
- **Decision:** gpt-5.5-pro deep pass ON HOLD (would entrench the bias). Instead — **Lever B** (cheap:
  source-diversity quota in `review/report.py`, not yet built) then **Lever A** (compilation-expansion +
  more Tier-A ingesters → re-run), THEN deep-pass a diversified list. See HANDOFF §6/§7. Spend this session ≈ $0.

### 2026-06-26 — FIRST FULL END-TO-END RUN COMPLETE: 900 → 23 vetted finalists
- Stage-3 kill-search (gpt-5.5 + web, top-50 single-problems) done: **28 RED killed, 23 AMBER survive, 0 GREEN**
  (kill-search is conservative — every survivor has a flagged residual risk, usually "need a scalable
  certificate, not a one-off small-n example"). Survivors: 18 Erdős, 4 arXiv, 1 QIT.
- Verdicts are deep + cited + actionable (e.g. Erdős #791 additive 2-basis: found Kohonen 85/294 &
  Yu records, pinpointed the segment-placement-certificate niche, flagged "forgotten German literature"
  Erdősgate risk, gave a SAT/MILP attack). **The funnel works end-to-end.**
- Outputs: `problem-id/review/finalists_detailed.md` (140KB full dossier) + `finalists.md` (table).
- **Survivors skew Erdős additive-combinatorics & discrete geometry — Nikol's wheelhouse.** COLT ML-theory
  problems mostly RED-killed (resolve fast) → signals where our alpha is.
- **PHASE I (problem identification) has produced its first real deliverable.** Phase II (solve sprint)
  candidate set = the 23 AMBER finalists. Enhancements queued: compilation-expansion, gpt-5.5-pro deep
  pass on top picks, more sources.

### 2026-06-25 — High-volume ingest + first ~1K end-to-end run (option A→2→1)
- Built high-volume ingesters: `corpus/erdos.py` (600 OPEN ingested, 499 solved auto-skipped) and
  `corpus/arxiv_openproblems.py` (229 unique "open problem(s)" papers, 13 fields). **Corpus = 900.**
- Hardened idempotency: scorer `scores IS NULL` guard + `--rescore` — corpus can grow past 900 with
  zero re-spend. Scorer made concurrent (`--workers`, default 8).
- **Calibration triage of 775** (after filter dropped 53 dups + 1 famous): 475 triaged. **Per-source
  validation: `llm_saturation_inv` correctly penalizes the swept Erdős catalogue (avg 2.27) vs curated
  COLT/IQOQI (2.8/2.5); pass rates 52% Erdős vs 85% COLT.** Cross-source top ranking is sensibly diverse.
- **Known limitation:** 13/50 top arXiv entries are compilation papers (lists of ~20 problems) — needs a
  future compilation-expansion pass. For now Stage-3 runs on top-50 SINGLE problems (`--exclude-compilations`).
- **Stage-3 kill-search launched** on top-50 single-problems (gpt-5.5 + web search). Will yield first
  fully novelty-vetted cross-source finalist list.

### 2026-06-25 — FULL PIPELINE SPINE BUILT & validated end-to-end
- Built Stage 1 (`triage/filter.py`: famous-impossible reject + min-length + cross-source dedup),
  Stage 3 (`killsearch/killsearch.py`: gpt-5.5-pro/gpt-5.5 + live web search, structured green/amber/red
  verdict via Responses API background-mode + backoff), and orchestrator `run.py` (resumable, floor-40 guard).
- **gpt-5.5-pro discovered from the key & confirmed working** (Responses API, ≥medium effort), but org
  **TPM=200k** makes it fragile/slow for batch — one Pro+web-search call ~saturates the minute. **gpt-5.5
  (non-pro) validated the full Stage-3 path cleanly at ~43s/call.** Plan: gpt-5.5 for bulk Stage-3,
  gpt-5.5-pro selectively on final survivors.
- **Stage-3 proved its value on call #1:** the #1 triage pick (COLT `awasthi23a`, composite 4.68) was
  RED-killed — web search found it was RESOLVED by two COLT 2024 papers (Zhang et al.; Peng). Exactly the
  Erdősgate catch the cheap triage can't make.
- **Pipeline is complete (Stages 0–4 + orchestrator).** Ready for high-volume ingesters → big run.

### 2026-06-25 — 2nd Tier-A source added (COLT/PMLR open-problem track)
- Built `corpus/colt_pmlr.py`: harvests "Open Problem:" papers across COLT PMLR volumes 2019–2025.
  Ingested **41** ML/learning-theory problems (precise, self-contained, low-saturation). DB now 71
  problems across 2 fields (QIT + ML-theory). Scoring the 41 now; then re-rank cross-source.
- Still pending (needs model id from Nikol): wire GPT-5.5-Pro into Stage-3 kill-search.
- Next Tier-A: Douglas West graph-theory list, Barbados, arXiv-"N open problems".

### 2026-06-25 — Phase I pipeline BUILT (Stage 0/2/4 working end-to-end)
- Built `problem-id/`: durable SQLite store (`common.py`), locked `rubric.yaml`, Tier-A IQOQI ingester
  (`corpus/iqoqi.py`), Stage-2 gpt-5-mini scorer w/ structured output + composite/gates (`triage/score.py`),
  Stage-4 ranked report (`review/report.py`). Isolated venv; key read from file, never printed.
- **Validated end-to-end on IQOQI Open Quantum Problems (30):** calibrated scores (e.g. "All Bell
  inequalities" PASS comp 4.18; NPPT-undistillability cut 2.84), correct gating, durable DB.
- **Next:** more Tier-A ingesters (COLT/PMLR, West, Barbados, arXiv-"N open problems"); then Stage-3
  kill-search Workflow on survivors; then scale to Tier-B/C.

### 2026-06-25 — Pipeline §12 decisions locked
- All 6 design questions resolved (see `PROBLEM_ID_PIPELINE.md` §12): weights = v1 defaults
  (self_certifying 3.0 / llm_saturation_inv 2.5 dominate); scope = moderate-wide (home fields + one
  adjacency ring); finalists ~50 (floor 40); Tier-A ingesters first; default-method-stalled = cheap
  flag + human surfacing, no gate; DB durable/append-only across sprints.
- Added §13 build order. **Pipeline design is frozen; build is unblocked.**
- **Next:** scaffold `problem-id/` + Tier-A ingesters (IQOQI, COLT, West, Barbados, Brass–Moser–Pach,
  arXiv-open-problems), then Stage-1/2 on Nikol's key.

### 2026-06-24 — Major reframe: Problem Identification is its own Phase I (spec written)
- Nikol: selection is the bulk of the work; we'd covered <0.1% of problems as a convenience sample.
  Demoted the §7b shortlist to a "Phase-0 pilot / warm-start."
- **Alpha thesis adopted:** hunt *curated, low-LLM-saturation* problem lists (IQOQI Open Quantum
  Problems, COLT open-problem track, West/Barbados graph-theory lists, Brass–Moser–Pach, arXiv
  "N open problems in X") — neglected by frontier-lab sweeps, unlike Erdős/formal-conjectures.
  Made `llm_saturation_inv` + `self_certifying` first-class heuristics.
- **Wrote `PROBLEM_ID_PIPELINE.md`** — full design spec for a 5-stage funnel (ingest 10k–50k → cheap
  filter → gpt-5-mini triage → Workflow kill-search → human pick → 3–6 targets), schema, corpus catalog
  (tiered by saturation), heuristic weights, triage prompt+schema, hybrid build plan. **Design-first per
  Nikol; no code yet.** §12 lists open design questions for Nikol+Sihao.
- **Next:** Nikol/Sihao answer §12 (esp. heuristic weights + Tier-A-first); then build Tier-A ingesters.

### 2026-06-24 — Kill-search run on A1 + B1/B2 (verdicts in §7b)
- **B1 & B2: GREEN** — gaps confirmed open from the actual arXiv:2407.07285 Table 1 (GR(4,K₄,2)∈{15,17};
  R(B₄,B₇)∈{22,23}, gap 1). Cleared to build. Note: search layer HAD fabricated these earlier — primary
  source read was essential (validated the §3 discipline).
- **A1: AMBER** — gap real (no published rate, 2506.04159 qualitative only) BUT dense adjacent literature
  on quantitative critical-point/level-functional CLTs (Kratz–León etc.) means it may be referee-immediate.
  Added a **mandatory pre-build novelty gate** before greenlight.
- **Decision:** promote **B1/B2 to safe primary** (verified floor); **A1 conditional** on clearing its gate
  by Day 2. Build Track B now.

### 2026-06-24 — Scored candidate shortlist built (§7b); primary + fallback chosen
- Ran 4 parallel field-research agents w/ prior-art guard. 3 returned strong (prob/measure,
  combinatorics, QIT); number-theory re-running in background.
- **Primary = A1** (fBm local-minima Berry–Esseen rate, arXiv:2506.04159) — peer-reviewed
  quantitative-extension template, Nikol's domain, Lean-able, least crowded.
- **Fallback = B1/B2** (GR(4,K₄,2) / R(B₄,B₇) Ramsey via SAT — DRAT-certifiable, uncontested).
- **High-upside = B3** (GUPB in 3⊗3⊗3 — open existence, witness = new bound-entangled state).
- **NT (Track C):** agent stalled; filled by hand. Key calls: **avoid primitive sets (Tao now mobbing
  them, arXiv:2605.00301)**; use **DeepMind `formal-conjectures` Lean repo** as the NT sourcing tool
  (open Erdős problems pre-formalized = verifiability solved). No NT candidate greenlit yet.
- **Hard caveat logged:** search layer fabricated future dates — Day-1 must re-verify each live
  record from primary sources before committing (this IS the §3 kill-search).
- **Next:** execute §5 Day-1 — prior-art kill-search on A1 + B1, then stand up both tracks Day 2.

### 2026-06-24 — Team bios added; home fields fixed
- Nikol = Oxford math undergrad (logic/sets, ANT, Galois, graph theory, rings, topology,
  combinatorics, measure, probability) → proof + selection + verification lead.
- Sihao = MIT physics grad (ML, CS, QIT) → infra + Engine B + QIT/ML framing.
- **Decision:** candidate problems (§7) cluster in our **home fields** — combinatorics/graph
  theory, probability/measure (the §2.6 quantitative-extension template fits Nikol directly),
  algebraic/analytic number theory, and QIT (Sihao's less-crowded edge).

### 2026-06-24 — Case studies expanded + environment/team sections added
- Added **§2.7 Liam Price** (23-yo amateur, Erdős #1196 via GPT-5.4 Pro, Lean-verified) — our
  closest precedent; key transferable insight: **AI wins by switching the field's default method**
  (discrete/LYM where everyone tried continuous).
- Added **§2.8 collective formalization** (Equational Theories Project; Busy Beaver BB(5)) and
  **§2.9 OpenAI advancements** (IMO 2025 gold; GPT-5→5.4-Pro lineage).
- Added **Local environment** section (OPENEVOLVE.md → Engine B rig at ~/maths/openevolve; API-key
  file noted with security caveats, value not recorded) and a **Team** placeholder pending bios.
- **Reinforced decisions:** the amateur+Lean+open-effort path (§2.7) is a fully validated win
  shape; ATPs/SAT beat LLMs on core exhaustive logic (§2.8) — use each where it's strong.

### 2026-06-24 — v2 rewrite: AI-leveraged thesis
- **Pivot (Nikol):** the novelty/enabler is *frontier AI* (Opus, GPT-5.5-Pro, Aristotle/Lean), not
  amateur thinking. Target: novel publishable result in **~1 week**.
- Ran 2nd adversarial deep-research (111 agents, 28 sources, 25 claims verified, 0 refuted) on
  2025–2026 AI-assisted math.
- **Key decisions:** (1) primary template = **quantitative-extension** (only peer-reviewed
  precedent); (2) Engine B must run **cheap sampling baseline before evolution**; (3) **Lean
  verification is mandatory** on every result; (4) **prior-art kill-search is step one** (Erdősgate
  lesson). Adopted the §5 seven-day plan and the §4 retuned rubric.
- **Next:** produce the §7 scored shortlist of 5–10 concrete targets; confirm Opus-led precedent &
  autoformalizer reliability.

### 2026-06-24 — v1: amateur/outsider precedent (superseded by v2 framing, retained as Appendix A)

---

## Appendix A — Pre-AI amateur precedent (historical context)
The patterns still hold: outsider-tractable wins are **easily stated, have finite/self-certifying
witnesses, live in combinatorics / number theory / discrete geometry / graph theory.** Cases (all
verified in our 2026-06 run): **Royen** (Gaussian Correlation Inequality, neighbouring-toolkit
insight); **de Grey** (chromatic number of the plane ≥ 5, explicit graph + SAT — our cleanest
human+machine template); **Marjorie Rice** (pentagon tilings by hand; completeness later closed by
computer search); **Yitang Zhang** (bounded prime gaps; outsider, opened a door others optimized —
the "slipstream" play). The AI era keeps these patterns and adds **scale + verification**.

## Appendix B — Verified source lists
**2026 AI-for-math run:** GPT-5 paper arXiv:2511.16072 · Erdős AI-contributions wiki
(github.com/teorth/erdosproblems) · Erdős #728 arXiv:2601.07421 · AlphaEvolve arXiv:2511.02864 ·
ShinkaEvolve arXiv:2509.19349 · baselines-are-competitive arXiv:2602.16805 · Salim arXiv:2510.26647 ·
Malliavin-Stein arXiv:2509.03065 (*Statistics & Probability Letters*) · Erdősgate: TechCrunch
2025-10-19, Bubeck X threads · Tao blog (terrytao.wordpress.com, Nov–Dec 2025).
**Targeted follow-up searches (2026-06-24):** Liam Price / Erdős #1196 (Scientific American;
gigazine.net 20260427; erdosproblems.com #1196) · Equational Theories Project
(terrytao.wordpress.com 2025-12-09; arXiv:2512.07087) · Busy Beaver BB(5) arXiv:2509.12337 ·
OpenAI IMO 2025 gold (x.com/OpenAI/status/1946594928945148246; simonwillison.net 2025-07-19).
**Pre-AI run:** Royen arXiv:1512.08776 · de Grey arXiv:1804.02385 · Rice (Wikipedia/Quanta) · SAT
milestones arXiv:1605.00723, 1711.08076, 2403.17370 · openproblemgarden.org.

*Stats — v2 research run: 6 angles · 28 sources fetched · 135 claims extracted · 25 verified · 0 refuted.*
