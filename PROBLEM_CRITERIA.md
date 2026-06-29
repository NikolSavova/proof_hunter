# PROBLEM_CRITERIA — what counts as a "good problem"

> **Purpose.** This is the **human-owned, strict definition** of which open problems our pipeline
> should keep. Nikol owns it; edit it freely. The automated stages (the extractor scope-gate, the
> Stage-2 triage rubric, the research-grade gate) are *approximations of this document* — when they
> disagree with it, this document wins and we fix the prompts. `rubric.yaml` is the machine-readable
> scoring weights; THIS file is the plain-English spec of what we're hunting and what we throw out.
>
> **Status:** v1 draft, 2026-06-29 — **awaiting Nikol's review/edits.** Nothing is rejected in the DB
> based on these criteria until Nikol approves this file.

---

## 1. The goal (what "good" means here)
A problem is **good** for us if a 2-person AI-augmented team could plausibly produce a **modest but
genuinely-new, verifiable, publishable** result on it **in ~1 week**, using LLMs (Opus/GPT-5.5-Pro),
evolutionary/SAT search, and Lean. Not "famous and hard" — *tractable, checkable, and not already
done.* The whole pipeline exists to separate these from the ~tens of thousands of open problems that
are not this shape.

> **Note on elementary / olympiad-flavoured problems (they are WELCOME).** An elementary, low-machinery,
> beautifully-statable *open* problem is a **top-tier target**, not a lesser one — it maximises
> statability and usually self-certifiability, and needs no specialist apparatus. Our north star
> (META_GUIDE §2.7, Erdős #1196 / Liam Price) is exactly this shape. We exclude problems that are
> *closed* (already solved), never problems that are *simple to state*. Difficulty of statement is
> not a proxy for significance.

## 2. HARD INCLUSION — all of these must hold (else reject)
1. **Research-grade.** Posed as a current open problem by working mathematicians/scientists in a
   research venue — not a puzzle, exercise, or historical curiosity.
2. **In scope.** Lives in our fields (§5) — core: combinatorics, graph theory, probability/measure,
   number theory, quantum information; or the adjacency ring (discrete geometry, TCS/complexity,
   coding/information theory, optimization/convex analysis, ML-theory, math-physics/stat-mech).
3. **Self-certifying win condition.** Success is a *checkable object* — an explicit construction,
   a certificate, a bound with a proof we can verify, a Lean statement, or a re-runnable evaluator —
   **not** "experts would agree." Write the win-condition artifact down in one line, or reject.
4. **Statable.** The problem can be stated to a strong undergrad in a few sentences.
5. **Genuinely open.** Not already solved in the literature (this is what the kill-search verifies);
   "listed as open in a database" is NOT sufficient evidence of openness.

## 3. HARD EXCLUSION — any of these → reject (regardless of how attractive it looks)
These are the categories the **research-grade gate** auto-rejects; this list is the spec it follows.
- **Closed / not-genuinely-open** — has a known or readily-findable published solution: worked
  exercises, textbook or competition problems with published answers, and historical problem lists
  whose entries have since been resolved. **Excluded because they are not *open* — NOT because they
  are elementary.** An elementary or olympiad-*flavoured* statement is a PLUS, not a minus (see §1
  note); the disqualifier is the existence of a solution, which is exactly what the kill-search checks.
  *(e.g. most entries in "A List of Open Problems… Posed by Ibn al-Khawwām (13th c.)" are closed
  historical arithmetic — but if any entry is genuinely open and non-trivial, it stays.)*
- **Benchmark / meta** — AI/LLM benchmark or evaluation collections, "test-time learning",
  verifier-design tasks, ML-evaluation harnesses. *(e.g. "ThetaEvolve: Test-time Learning…".)*
- **Applied-engineering** — wireless/6G/networking, UAVs, applied deep learning, reinforcement-learning
  *systems*, federated learning, data mining, hardware, computer vision applications, control
  engineering, bioinformatics. *(e.g. "NTN-based 6G Localization", "Federated Learning…".)*
- **Deep-machinery-excluded** — needs heavy specialist apparatus and has no concretely self-certifying
  artifact in a week: algebraic geometry, operator algebras / von Neumann (II₁) factors, geometric
  topology, hard PDE, advanced Banach-space geometry. *(Keep ONLY if a specific problem is concretely
  self-certifying.)*
- **Famous-impossible** — equivalent to RH, P vs NP, Millennium-class, twin primes, Collatz, Goldbach.
- **No checkable win condition** — if success can't be written as an artifact anyone can verify.
- **Actively mobbed** — a hot seminar topic this year / a frontier-lab is visibly racing it (e.g. the
  primitive-sets area post-Tao 2026). Being *quietly* open is part of the alpha.

## 4. Scoring (the soft ranking, after the hard gates) — from `rubric.yaml`
Survivors of §2–§3 are scored 1–5 on each axis; composite = weighted average (weights in parentheses).
The two dominant axes encode our edge:
- **self_certifying (3.0)** — is success an object/certificate/Lean stmt anyone can check?
- **llm_saturation_inv (2.5)** — is this NOT being mechanically swept by frontier-lab LLM efforts?
- ai_tractability (2.5) · verifiability (2.0) · crowdedness_inv (2.0) · meaningfulness (1.5) ·
  novelty_checkability (1.5) · one_week_shaped (1.5) · statability (1.0).
- **Boosts:** quantitative-extension (+0.30, a known qualitative theorem lacking an explicit
  rate/constant), construction-target (+0.20, beat a public record), default-method-stalled (+0.15).

## 5. Field scope (locked "moderate-wide")
- **CORE:** combinatorics · graph theory · probability/measure · number theory · quantum information.
- **ADJACENT (ok):** discrete geometry · theoretical CS/complexity · coding & information theory ·
  optimization/convex analysis · ML/learning theory · mathematical physics/statistical mechanics.
- **EXCLUDE unless a concrete self-certifying problem surfaces:** algebraic geometry · geometric
  topology · set-theoretic forcing · hard PDE · operator algebras.

## 6. How the criteria are enforced (where each gate sits)
1. **Ingest / compilation-expansion** (`corpus/`) — the extractor applies §3 + §5 as a first scope gate.
2. **Stage-1 filter** (`triage/filter.py`) — famous-impossible + too-short + dedup. LLM-free.
3. **Stage-2 triage** (`triage/score.py`) — scores §4; drops below composite cutoff (3.2).
4. **Research-grade gate** (`triage/research_grade_gate.py`) — re-judges expanded papers against §3
   and rejects children of recreational/meta/applied/deep-machinery sources. *(This is the new step.)*
5. **Stage-3 kill-search** (`killsearch/`) — verifies §2.5 (genuinely open) adversarially.
6. **Stage-4 human review** — Nikol + Sihao make the final call; §7 edge cases live here.

## 7. Edge cases that need a HUMAN (don't let a gate decide these)
- A problem in an *excluded* field (e.g. algebraic geometry) that nonetheless has a clean
  self-certifying finite witness → a human may rescue it.
- "Applied-sounding" but mathematically clean problems (e.g. a coding-theory or optimization problem
  with an exact certificate) → keep; the gate sometimes over-rejects these. **Currently flagged for
  your call:** "Greedy algorithms: a review and open problems" and "Caristi fixed-point consequences"
  were auto-dropped — verify whether that's right.
- Borderline meaningfulness: a precise, checkable, open problem that no one would care about is still
  a weak pick — meaningfulness is a real axis, not a formality.
