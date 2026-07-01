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
repo (§0). SSH auth configured per-machine. **Run `/handoff` at the end of every working session.**

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
**Pipeline scale-up (the "bigger intake" — now at 2206, goal tens-of-thousands):**
- [x] ✅ **Compilation-expansion pass** — DONE (`corpus/expand_compilations.py`, +1301 children) + the
  **research-grade gate** (`triage/research_grade_gate.py`) to de-noise it. See §3.
- [x] ✅ **One more Tier-A ingester** — Douglas West graph theory DONE (`corpus/west_graphtheory.py`, 32).
- [ ] **Kill-search the new diversified top** (IMMEDIATE NEXT — see §7). The new arXiv-children + West
  problems are stage=`triaged`, NOT yet kill-searched. Run Stage-3 on the top ~50 to find genuinely-open
  ones: `./.venv/bin/python killsearch/killsearch.py --top 50 --model gpt-5.5`. ~$10-25.
- [ ] **More high-volume ingesters:** DeepMind `formal-conjectures` Lean repo; **OEIS**; **full-text
  arXiv mining**; automated-conjecture DBs (Graffiti/TxGraffiti, House of Graphs).
- [ ] **More Tier-A curated lists:** more COLT years, Barbados PDFs, Brass–Moser–Pach, MathOverflow
  `open-problem` tag. (Hannover OpenQIProblemsWiki was UNREACHABLE 2026-06-29 — retry later.)
- [ ] **gpt-5.5-pro deep pass** on the top ~8 finalists once the diversified set is kill-searched (org
  TPM=200k → throttle; `--model gpt-5.5-pro`).
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

## 7. IMMEDIATE NEXT ACTION — ⭐ NIKOL, START HERE (updated 2026-06-30 EOD, Sihao)
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
