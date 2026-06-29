# problem-id — Phase I pipeline (implementation)

Implements `../PROBLEM_ID_PIPELINE.md`. Durable, append-only problem DB + funnel.

## Setup (done once)
```bash
cd problem-id
python3 -m venv .venv
./.venv/bin/python -m pip install requests beautifulsoup4 lxml pyyaml openai feedparser
```
OpenAI key is read from `~/.config/proof_hunter/openai_key.txt` (override with `$OPENAI_API_KEY`
or `$OPENAI_KEY_FILE`). Kept outside the repo; never printed/committed.

## Run the whole funnel
```bash
# end-to-end: filter -> triage -> kill-search(top 50) -> report
./.venv/bin/python run.py
./.venv/bin/python run.py --ingest iqoqi colt_pmlr      # also run those ingesters first
./.venv/bin/python run.py --no-killsearch               # stop before the expensive Stage 3
./.venv/bin/python run.py --ks-limit 1                  # smoke-test the kill-search path
```

## Or run stages individually
```bash
# Stage 0 — ingest (Tier-A first). --limit for smoke tests.
./.venv/bin/python corpus/iqoqi.py            # IQOQI Open Quantum Problems (30)
./.venv/bin/python corpus/colt_pmlr.py        # COLT open-problem track (41, 2019-2025)
./.venv/bin/python corpus/west_graphtheory.py # Douglas West graph-theory conjectures (~33, Tier-A)
./.venv/bin/python corpus/arxiv_openproblems.py  # arXiv "open problem(s)" papers

# Stage 0.5 — compilation-expansion: split survey / "open problems in X" papers into
# individual child problems (LLM, scope-aware, idempotent). Surveys score low AS A UNIT
# but hide our best low-saturation single problems, so we do NOT gate on parent composite.
./.venv/bin/python corpus/expand_compilations.py --dry --limit 3   # preview extraction
./.venv/bin/python corpus/expand_compilations.py --workers 3       # expand all un-expanded compilations

# Stage 1 — cheap LLM-free filter + dedup (ingested -> prefiltered|rejected|duplicate)
./.venv/bin/python triage/filter.py

# Stage 2 — batch triage (gpt-5-mini, structured output, your key)
./.venv/bin/python triage/score.py            # scores all prefiltered/ingested
./.venv/bin/python triage/score.py --recompute  # re-derive composites after editing rubric.yaml (no API)

# Stage 2.5 — research-grade gate (for expansion children): reject children of recreational/
# benchmark/applied-engineering/deep-machinery survey papers per ../PROBLEM_CRITERIA.md. Run
# AFTER expansion (idempotent). --dry to preview the drop list before applying.
./.venv/bin/python triage/research_grade_gate.py --dry   # preview which parents/children get dropped
./.venv/bin/python triage/research_grade_gate.py         # apply (rejects junk children)

# Stage 3 — kill-search top finalists (gpt-5.5-pro + web search; EXPENSIVE, throttled)
./.venv/bin/python killsearch/killsearch.py --top 50
./.venv/bin/python killsearch/killsearch.py --model gpt-5.5 --top 50   # cheaper model

# Stage 4 — ranked review table -> review/finalists.md
./.venv/bin/python review/report.py --stage finalist --top 50
```

## Stage-3 / gpt-5.5-pro operational notes
- Pro models run via the **Responses API** and force **>= medium reasoning** — slow (~1-3 min/call) and token-heavy.
- Org **TPM cap is 200k**; one Pro+web-search call can approach it. Mitigated by `search_context_size="low"`,
  a 12s inter-call sleep, and 60s-backoff retries on 429 (see `killsearch/killsearch.py` constants).
- Therefore Stage 3 runs ONLY on the ~50 finalists, never the whole corpus — that's why Stages 1-2 must cut first.

## Layout
- `common.py` — DB schema/helpers, rubric loading, composite scoring, OpenAI client.
- `rubric.yaml` — **the heuristics** (locked v1 weights + scope + thresholds). The thing we tune.
- `corpus/` — one ingester per source. `iqoqi.py` is the reference implementation.
- `triage/score.py` — Stage-2 scorer (rubric → JSON schema → composite + gates).
- `killsearch/` — Stage-3 (to wire to a Claude Workflow on survivors).
- `review/report.py` — Stage-4 ranked table.
- `db/problems.sqlite` — the durable store (append-only across sprints; do not reset).

## Stages a problem moves through
`ingested → (triaged | filtered | rejected) → deep → finalist`
- triaged = passed Stage-2 cutoff; filtered = scored but below cutoff; rejected = hard gate.

## Status
- ✅ Stage 0 (IQOQI), Stage 2 (scorer), Stage 4 (report) working end-to-end.
- ⏭️ Next: more Tier-A ingesters (COLT/PMLR, West, Barbados, arXiv-open-problems), then Stage-3 kill-search workflow.
