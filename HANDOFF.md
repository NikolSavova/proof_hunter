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
   ./.venv/bin/python -m pip install requests beautifulsoup4 lxml pyyaml openai feedparser
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
repo (§0). **Run `/handoff` at the end of every working session so the other person can pull current state.**

**Top candidates from the run (for Phase II) — ON HOLD pending the §6/§7 corpus-broadening decision:**
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
  - **TWO LEVERS TO FIX (decided this session — do NOT deep-pass the current Erdős-heavy set first):**
    - **Lever A (real fix): broaden the corpus, then re-run** — compilation-expansion (highest ROI) +
      more Tier-A low-saturation ingesters (§4). This is the alpha thesis; the funnel can only surface
      what's in the barrel, and the barrel is 67% Erdős.
    - **Lever B (cheap, immediate, ~20 min): source-diversity quota at Stage-4** — change `review/report.py`
      to take top-N *per source* (or cap Erdős's share) instead of a global top-50, so the best
      COLT/IQOQI/arXiv problems surface with zero new ingest or spend. NOT YET IMPLEMENTED.
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

## 7. IMMEDIATE NEXT ACTION (updated 2026-06-26)
**Decision this session:** the gpt-5.5-pro deep pass is now ON HOLD — running it on the current
Erdős-heavy finalist list would double down on exactly the volume bias Nikol flagged (§6). New plan:
1. **Lever B first (cheap, ~20 min):** add a source-diversity quota to `review/report.py` (top-N per
   source / cap Erdős share) and regenerate `finalists.md` — re-balances what we already have, $0 spend.
2. **Lever A (real fix):** build the **compilation-expansion pass** (highest ROI — 13 top arXiv survey
   papers → ~150–250 new low-saturation problems) + 2–3 more Tier-A ingesters (West, Barbados,
   Brass–Moser–Pach, Hannover QI). Then re-run the funnel.
3. **THEN** the gpt-5.5-pro deep pass on a genuinely diversified finalist list → pick 1–3 for Phase II.
Awaiting Nikol's go-ahead on sequencing (Lever B now vs. straight to compilation-expansion).
