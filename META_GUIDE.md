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
