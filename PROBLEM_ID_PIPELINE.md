# Problem-Identification Pipeline — Design Spec (v0, for review)

> **Status:** DESIGN DOCUMENT — for Nikol + Sihao to review before any code is written.
> **Created:** 2026-06-24. **Companion to:** `META_GUIDE.md` (this realizes its "Phase I").
> **Decision taken:** design-first, build-after. Nothing here is implemented yet.

---

## 1. Why this exists (the thesis)

**Problem selection is the bulk of the challenge, not the solve.** Our first selection pass
sampled **~25 scored / ~60 considered** candidate problems against a universe of **tens of
thousands** — under **0.1% coverage**, and a *convenience sample* biased to whatever a few web
searches surfaced first. The four finalists are "best of the first 25 we tripped over," not "best
available." This pipeline replaces convenience sampling with an instrumented, high-recall funnel.

### The alpha thesis (Nikol): hunt the *neglected, curated* lists
Famous catalogues (Erdős problems, Millennium-class lists) are now **mechanically swept by frontier
labs** — the DeepMind `formal-conjectures` repo, GPT-5 Erdős runs, etc. Their marginal value is
falling fast. The **alpha is in precisely-stated, self-contained problems that live in
lower-traffic, field-specific compilations** — COLT's open-problem track, Werner's IQOQI quantum
list, discrete-geometry problem books — which (a) are curated by leading researchers (so they're
*real* and *meaningful*), yet (b) are **not on any LLM's worklist yet.** We therefore make
**"LLM-saturation" a first-class *inverted* heuristic**, and weight curated-compilation sources highly.

---

## 2. Design principles

1. **High recall first, precision later.** Over-collect at Stage 0–1 (cheap); spend judgment only on
   survivors. Better to triage 30k and keep 40 than to hand-pick 25.
2. **Every stage is logged & re-runnable.** We tune heuristics by inspecting what each stage dropped.
   Silent truncation is forbidden — log every cap.
3. **Heuristics are explicit and versioned.** The scoring function is a file we edit, not vibes.
4. **Cheap model → escalate.** Stage-2 triage runs a cheap model (gpt-5-mini) on everything; only
   survivors get expensive Opus/GPT-5.5-Pro analysis.
5. **Verifiability and novelty are gates, not scores.** A problem with no self-certifying win-condition,
   or that fails the Erdősgate prior-art check, is *cut*, regardless of how attractive it looks.
6. **The DB is a durable, append-only asset.** `problems.sqlite` persists across *all* sprints; re-runs
   augment and re-score but never reset it, and provenance/history is preserved. We build the corpus once
   and grow it — a compounding asset, not a throwaway per iteration. *(Locked: Q6.)*

### Scope (locked: Q2) — "moderate-wide"
Cast **wider than the four home fields, but not extremely wide.** Include a *one ring* of adjacency that's
plausibly tangential to our interests; exclude far/deep-machinery fields unless a specific problem is
self-certifying and tractable (the scorer's field-fit + saturation axes prune the rest).
- **Core:** combinatorics/graph theory · probability/measure · algebraic & analytic number theory · QIT.
- **Adjacent (include):** discrete geometry · theoretical CS / complexity · coding & information theory ·
  optimization / convex analysis · ML / learning theory (COLT) · mathematical physics / statistical mechanics.
- **Exclude (unless a concrete self-certifying problem surfaces):** deep-machinery algebraic geometry,
  geometric topology, set-theoretic forcing, hard PDE, and similarly far/obscure areas.

---

## 3. The funnel

| Stage | What | Method | In → Out | Owner |
|---|---|---|---|---|
| **0. Ingest** | Pull corpora into one normalized problem DB | scrapers / APIs / git / PDF-parse | sources → **10k–50k** | Sihao (infra) |
| **1. Cheap filter** | Drop solved / famous-hard / out-of-field; dedupe | regex + metadata rules | 50k → **~3k** | automated |
| **2. Batch triage** | Score every survivor on the rubric | gpt-5-mini, structured output | 3k → **~300** | automated (your key) |
| **3. Deep analysis + kill-search** | Prior-art/Erdősgate check, attack sketch, feasibility, LLM-saturation estimate | Opus + GPT-5.5-Pro + web | ~300 → **~50 (floor 40)** | Claude Workflows |
| **4. Human review** | Read the ~50 finalists, pick sprint targets | judgment | ~50 → **3–6** | Nikol + Sihao |

> **Finalist target (locked: Q3): ~50, hard floor 40.** Stage-2 composite cutoff is auto-tuned to land
> Stage-3 input (~300) such that ~50 survive Stage-3; if fewer than 40 clear, lower the cutoff and re-run
> Stage-3 on the next tranche rather than ship a short list.

Wall-clock target: Stages 0–2 in a day of compute once built; Stage 3 a few hours; Stage 4 a sitting.

---

## 4. Data schema (the problem record)

```jsonc
{
  "id": "src:local-id",                 // stable, e.g. "iqoqi:33", "colt2025:gu25b", "erdos:707"
  "statement": "verbatim problem text",
  "restatement": "one-sentence plain restatement (LLM-filled)",
  "source": "iqoqi-oqp",                // corpus key
  "source_url": "https://...",
  "field": ["quantum-info","combinatorics"],
  "year_posted": 2021,
  "last_progress": "2024 partial bound (cite)",   // LLM/most-recent-citation filled
  "status_claimed": "open|partial|unknown",
  "tags": ["self-certifying","quantitative-extension","construction","bound"],
  "formalized": "lean-stmt-url | null",
  // ---- scores (Stage 2, each 1-5) ----
  "scores": { "statability":_, "ai_tractability":_, "verifiability":_,
              "novelty_checkability":_, "meaningfulness":_, "crowdedness_inv":_,
              "one_week_shaped":_, "llm_saturation_inv":_, "self_certifying":_ },
  "composite": 0.0,                      // weighted sum
  // ---- Stage 3 ----
  "killsearch": { "still_open": true, "closest_prior": "cite", "verdict": "green|amber|red", "notes": "" },
  "attack_sketch": "engine A/B + how, why 1 week",
  "stage": "ingested|filtered|triaged|deep|finalist|rejected",
  "drop_reason": null
}
```

---

## 5. Corpus catalog

> Tiered by the alpha thesis. **Tier A (curated, low-saturation) is the priority.** Each entry:
> ingest method · rough size · LLM-saturation (★ = heavily swept, ☆ = neglected/our alpha).

### Tier A — curated, field-specific, *low-saturation* compilations (HIGHEST PRIORITY) ☆
- **IQOQI "Open Quantum Problems"** — oqp.iqoqi.oeaw.ac.at · Werner et al., curated, *explicitly lists
  problems "not receiving enough attention."* Scrape. ~dozens. ☆☆ (our QIT sweet spot, Sihao's edge).
- **Hannover OpenQIProblemsWiki** — qig.itp.uni-hannover.de/qiproblems · MediaWiki, scrape. ☆☆
- **"Some Open Problems in QIT"** quant-ph/0504166 · **"Five Open Problems in QIT"** PRX Quantum 3,010101
  (2022) · PDF-parse. ☆☆
- **COLT Open-Problem track** — PMLR, annual (e.g. v291 2025, "Open Problem: …"). *Purpose-built:
  precise, self-contained, theoretical, often a small prize.* Index PMLR by "Open Problem:" title prefix.
  ~10–20/yr × many years. ☆☆ (ML-theory; Sihao + Nikol's probability).
- **Douglas West, "Open Problems – Graph Theory & Combinatorics"** — dwest.web.illinois.edu/openp ·
  curated, categorized. Scrape. ~hundreds. ☆
- **Barbados Graph Theory Workshop** open-problem PDFs (annual) · PDF-parse. ☆☆
- **Brass–Moser–Pach, "Research Problems in Discrete Geometry"** (Springer 2005) + updates · OCR/known
  digitizations. ☆
- **arXiv "N open problems in X"** papers (e.g. "Seven open problems in applied combinatorics"
  arXiv:2303.11464) · these are a *genre* — query arXiv titles/abstracts for "open problem(s)". ☆
- **Survey-paper "Open Problems" sections** — mined from arXiv survey PDFs in our fields. ☆ (huge, noisy).

### Tier B — large general catalogues (high recall, rising saturation) ★
- **erdosproblems.com** (~1000+, tagged, + AI-contributions wiki for the Erdősgate guard) · scrape. ★★
  (still useful, but treat anything attractive as possibly-contested; mandatory wiki cross-check).
- **DeepMind `formal-conjectures`** (Lean, pre-formalized → verifiability solved) · git. ★★ (others mining it).
- **Open Problem Garden** (combinatorics/NT/geometry/graph, difficulty-tagged) · scrape. ★
- **Wikipedia "List of unsolved problems in mathematics"** + per-field lists · scrape. ★★ (famous = mobbed).

### Tier C — computational / generative sources (Engine-B targets) ☆
- **OEIS** — sequences with unknown next term or conjectured properties = search/evolution targets ·
  bulk download. ☆ (vast, niche).
- **Automated-conjecture systems** — Graffiti / GraphBrain / *TxGraffiti*, House of Graphs · these
  *emit* conjectures; we can harvest unproven ones. ☆☆ (very low human attention).

### Tier D — discussion sources (noisy, for recall) ★
- **MathOverflow `open-problem` tag**, math.SE · API. ★ (quality-variable; needs hard triage).

---

## 6. Heuristics — the scoring function (what we co-develop)

Each problem scored **1–5** per axis; **composite = Σ wᵢ·scoreᵢ**. Weights below are **LOCKED as the v1
defaults (Q1 — Nikol delegated)**; we may still tune later by reviewing Stage-4 outcomes, but v1 ships as-is.

| Axis | What it measures | Start weight |
|---|---|---|
| **self_certifying** ⭐ | Is success an *object / certificate / Lean statement* checkable by anyone? | **3.0** |
| **llm_saturation_inv** ⭐ (NEW) | Inverse of how mechanically-swept the source/problem is (Tier-A ☆ scores high; erdos/formal-conjectures score low) | **2.5** |
| **ai_tractability** | Could Engine A (one cross-domain lemma / quantitative extension) or Engine B (search) crack it? | 2.5 |
| **verifiability** | Lean-formalizable / certificate / re-runnable evaluator | 2.0 |
| **crowdedness_inv** | Inverse of citation-velocity + recent-arXiv-activity + hot-seminar presence | 2.0 |
| **meaningfulness** | Named problem / curated by a leader / people would care | 1.5 |
| **novelty_checkability** | Can we be *sure* in a day it's genuinely open? | 1.5 |
| **one_week_shaped** | A single nameable win-condition artifact | 1.5 |
| **statability** | One sentence to an undergrad | 1.0 |

**Hard gates (auto-reject, not scored):** equivalent to a famous-impossible problem (RH/P≠NP/…);
no self-certifying win-condition; fails the Stage-3 Erdősgate prior-art check.

**Special detectors (boost flags, set during triage):**
- *Quantitative-extension shape* — "known qualitative theorem lacking an explicit rate/constant" (the
  only peer-reviewed template; §2.6 of the guide). Strong boost.
- *Default-method-stalled* — problem stuck for years under one dominant technique (the Liam Price
  discrete-vs-continuous pattern). **(Decision, Q5 — Claude's call):** do NOT over-invest in automating
  this. Set it as a *cheap, low-confidence* Stage-2 flag (proxy: years-open ≥ ~10 **and** the abstract/
  literature names a single dominant method), used only as a small boost — and **surface it explicitly to
  human eyes at Stage 4**, where the discrete-vs-continuous judgment actually lives. Never gate on it.
- *Construction/bound target* — success = exhibit an object beating a public record → Engine B. Boost.

---

## 7. Stage-2 triage: prompt + structured output (concrete)

Run per problem (batched) on **gpt-5-mini**, escalate top-quartile ties to GPT-5.5-Pro.

**System sketch:** *"You are screening open math problems for a small AI-augmented team (Oxford pure-math
undergrad + MIT physics/ML grad). Tools: GPT-5.5-Pro, Opus, OpenEvolve (evolutionary search), SAT, Lean.
Score the problem on each axis 1–5 per the rubric. Be skeptical and calibrated; most problems are NOT a
good fit. Output ONLY the JSON schema."*

**Structured-output schema (forces calibrated, parseable scoring):**
```jsonc
{ "restatement": "string",
  "field": ["string"],
  "scores": { "statability":1, "ai_tractability":1, "verifiability":1, "novelty_checkability":1,
              "meaningfulness":1, "crowdedness_inv":1, "one_week_shaped":1, "llm_saturation_inv":1,
              "self_certifying":1 },
  "detectors": { "quantitative_extension":false, "default_method_stalled":false, "construction_target":false },
  "win_condition": "what artifact = success, or 'none' (→ auto-reject)",
  "suggested_engine": "A|B|both|none",
  "one_line_rationale": "string" }
```
Composite computed in code (not by the LLM) for consistency. Anything with `win_condition:"none"` or
composite below a tunable threshold is dropped (and logged).

---

## 8. Stage-3 deep analysis + kill-search (Claude Workflows)

For each of the ~300 survivors, a workflow `pipeline()` stage that:
1. **Prior-art kill-search** (the §3 discipline): adversarially try to prove it's already solved /
   the gap is closed; cross-check solved-lists + AI-contribution wikis. Verdict green/amber/red.
2. **LLM-saturation estimate**: has any AI pipeline / frontier-lab paper touched this exact problem?
3. **Attack sketch**: concrete Engine-A lemma or Engine-B evaluator; why 1 week is plausible.
4. **Verifiability concretization**: name the Lean statement / certificate / evaluator.

Red → cut. Amber → flag with the specific risk. Green → finalist. (This is the stage that caught A1's
critical-point-literature risk and confirmed B1/B2 — done by hand last round; here it's systematic.)

---

## 9. Stage-4 human review
Nikol + Sihao read the ~40 finalists (a ranked table + the attack sketch + kill-search verdict each),
pick **3–6** for the solve-sprint, split by engine/field. This is where domain taste — irreplaceable —
makes the final call.

---

## 10. Build plan (AFTER approval) — hybrid

```
AI-math/
  problem-id/
    corpus/            # one ingester per source → normalized records
      iqoqi.py  colt_pmlr.py  west_graphtheory.py  erdos.py  formal_conjectures.py
      arxiv_openproblems.py  oeis.py  ...
    db/problems.sqlite # the store (schema §4)
    triage/
      rubric.yaml      # the heuristics + weights (§6) — versioned, the thing we tune
      score.py         # batch gpt-5-mini scorer (your key), structured output (§7)
    killsearch/        # Stage-3 driver → hands survivors to a Claude Workflow
    review/
      finalists.md     # the ranked ~40 → ~6, regenerated each run
    run.py             # orchestrates 0→4; resumable; logs every drop
```
- **Bulk ingest + Stage-2 triage:** Python on **your OpenAI key** (scales to tens of thousands,
  hours-long, you own/re-run it).
- **Stage-3 kill-search:** my **Claude Workflows** on the ~300 survivors (adversarial verify is its
  strength).
- **Heuristics (`rubric.yaml`)** are the shared artifact we iterate together.

---

## 11. Cost & scale estimate (rough)
- Stage-2: ~3k survivors × ~1k output tokens on gpt-5-mini ≈ cheap (low single-digit $; minutes–hours).
- Escalation + Stage-3: hundreds of heavier calls — the main spend, still modest.
- Dominant cost is *engineering time on ingesters*, not tokens. Tier-A scrapers are small; arXiv/OEIS
  mining is the bigger build — stage it after Tier A proves the funnel.

---

## 12. Design decisions — LOCKED (2026-06-25)
All six resolved with Nikol; this section is now settled, not open.
1. **Heuristic weights** — ✅ **Locked at the §6 v1 defaults** (Nikol delegated). `self_certifying` (3.0)
   and `llm_saturation_inv` (2.5) dominate, as intended.
2. **Field scope** — ✅ **"Moderate-wide"** (see §2 Scope): core home fields + one ring of adjacency;
   exclude far/deep-machinery fields unless a concrete self-certifying problem surfaces.
3. **Finalist count** — ✅ **~50, hard floor 40** (§3 note governs the Stage-2 cutoff & re-run rule).
4. **Tier-A first** — ✅ **Confirmed.** Build IQOQI, COLT, West, Barbados, Brass–Moser–Pach,
   arXiv-"N-open-problems" ingesters before the Erdős/arXiv-survey/OEIS scale.
5. **Default-method-stalled detector** — ✅ **Claude's call:** cheap low-confidence Stage-2 flag +
   explicit Stage-4 human surfacing; never gate (see §6).
6. **Reusability** — ✅ **Durable, append-only DB** maintained across all sprints (§2 principle 6).

## 13. Build order (now unblocked)
1. Scaffold `problem-id/` + schema (§4) + `rubric.yaml` from the locked §6 weights.
2. **Tier-A ingesters first** (IQOQI · COLT/PMLR · West · Barbados · Brass–Moser–Pach · arXiv-open-problems).
3. Stage-1 cheap filter (incl. the §2 scope rule) → Stage-2 `score.py` (gpt-5-mini, your key, §7 schema).
4. Wire Stage-3 to a Claude Workflow kill-search; emit `review/finalists.md` (~50).
5. Then scale to Tier-B/C/D corpora and grow the durable DB.
