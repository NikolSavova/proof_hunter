# HANDOFF — read me first (for a fresh Claude Code session)

> **Purpose:** this file is the single self-contained brief to resume this project in a NEW
> session after the folder was moved. Read this, then `META_GUIDE.md` (strategy + full working
> log) and `PROBLEM_ID_PIPELINE.md` (pipeline design). Written 2026-06-26 by the prior session.
>
> ⚠️ **Memory note:** the prior session's file-memory lives under the OLD project path
> (`~/.claude/projects/-Users-nikolsavova-Desktop-AI-math/memory/`). After the move it will NOT
> auto-load. THIS file + `META_GUIDE.md` are the source of truth. (Optionally copy those memory
> files into the new project's memory dir.)

---

## 0. ⚙️ POST-MOVE CHECKLIST (do this first — the move breaks two things)
1. **Recreate the Python venv** (venvs hard-code absolute paths and do not survive a move):
   ```bash
   cd <NEW>/problem-id
   rm -rf .venv && python3 -m venv .venv
   ./.venv/bin/python -m pip install requests beautifulsoup4 lxml pyyaml openai feedparser
   ```
2. **OpenAI key now lives OUTSIDE the repo** at `~/.config/proof_hunter/openai_key.txt` (moved there
   2026-06-26 so it is never committed to GitHub). Both consumers already point to it:
   `problem-id/common.py` (`KEY_PATH`, overridable via `$OPENAI_API_KEY` / `$OPENAI_KEY_FILE`) and
   `~/maths/openevolve/env.sh`. On a fresh machine/clone, recreate that file with the key (ask Nikol).
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

**Top candidates from the run (for Phase II):**
1. **Erdős #791** — additive 2-basis `g(n)` (minimal `A⊆{0..n}` with `A+A ⊇ {0..n}`). Records:
   Kohonen 2017 upper `85/294`, Yu 2015 lower. **Concrete attack:** SAT/MILP search for a better
   *segment-placement certificate* beating Kohonen's `85/294` — scalable & Lean-checkable. Strongest
   Engine-B fit. (Amber risk: a one-off small example isn't enough; need a *parametric/scalable* tiling.)
2. **Erdős #653** — max number of distinct "distance counts" of n planar points; gap `0.7n` (Csizmadia)
   to `n−cn^{2/3}`. Gadget-substitution attack.
3. **arXiv 1712.01960** — worst-case distortion embedding an n-point *diversity* into ℓ1; LP/cut-cone
   duality attack with rational certificates.

## 4. WHAT STILL NEEDS TO BE BUILT
**Pipeline scale-up (the "bigger intake" we discussed — currently ~900, goal tens-of-thousands):**
- [ ] **Compilation-expansion pass** (HIGH PRIORITY). 13/50 top arXiv hits are *survey papers listing
  ~10-20 problems each*, ingested as one record. Build an LLM step that splits each compilation into
  individual problem records, then triages those. The surveys likely hide great single problems.
- [ ] **More high-volume ingesters:** DeepMind `formal-conjectures` Lean repo (git clone + parse .lean
  — pre-formalized = verifiability solved); **OEIS** (unknown-next-term / conjectured-property = Engine-B
  targets); **full-text arXiv mining** (grep "we conjecture / remains open" in PDFs — the real
  tens-of-thousands, noisy, biggest build); automated-conjecture DBs (Graffiti/TxGraffiti, House of Graphs).
- [ ] **More Tier-A curated lists** (the alpha): more COLT years, Douglas West's graph-theory page,
  Barbados workshop PDFs, Brass–Moser–Pach discrete-geometry, MathOverflow `open-problem` tag,
  IQOQI sibling lists (Hannover OpenQIProblemsWiki). Pattern: copy `corpus/iqoqi.py` or `colt_pmlr.py`.
- [ ] **gpt-5.5-pro deep pass** on the top ~8 finalists (higher-confidence novelty read before
  committing a week). NOTE: org TPM=200k makes gpt-5.5-pro slow/fragile — throttle hard (it's wired in
  `killsearch.py` via background-mode + 70s backoff; pass `--model gpt-5.5-pro`).
- [ ] Optional: embeddings-based dedup (Stage-1 currently uses lexical Jaccard ≥0.80 on titles).

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
- **The corpus is Erdős-heavy (600/900), which biases survivors toward Erdős.** To actually exploit the
  low-saturation alpha thesis, the next ingest should prioritize **more curated Tier-A lists +
  compilation-expansion**, not more Erdős. Right now we're somewhat fighting our own thesis by volume.
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

## 7. IMMEDIATE NEXT ACTION (suggested first thing in the new session)
Run the post-move checklist (§0), confirm the DB reads 900, skim `review/finalists_detailed.md`, then ask
Nikol: **gpt-5.5-pro deep pass on the top ~8 → then pick problems for Phase II?** (My recommendation.)
