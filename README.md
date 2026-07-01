# Proof Hunter

Proof Hunter is a pipeline for discovering open mathematics problems that are tractable, verifiable,
and genuinely unsolved, and presenting them as a scored, literature-checked shortlist.

As language models become more capable at proving theorems and constructing examples, the binding
constraint shifts from solving to selection: deciding which open problems are worth attempting, which
are actually still open, and which admit a result that can be checked. Proof Hunter is built around
that selection problem. The larger share of the work here is in discovery — ingesting problems at
scale, scoring them, and verifying that they are unsolved — rather than in any single attempt to
solve one.

The project is ongoing and the code here is the tooling.

## Why problem discovery

Most open problems are poor targets for an automated or semi-automated effort. Many are famous and
hard, many require heavy specialized machinery, and many have already been resolved in a paper that a
keyword search does not surface. Useful targets are the opposite: tractable, checkable, and genuinely
unsolved. They are also comparatively rare, which is why finding them is worth a dedicated system.

Two signals drive selection:

- **Low exploration** — problems that are not already the subject of intense automated or manual
  attention.
- **Expert curation** — problems that a working mathematician considered worth writing down.

In practice these are concentrated in curated, single-topic problem lists (for example the Kourovka
Notebook, IQOQI's open quantum problems, and Dagstuhl workshop problem sessions) rather than in
either the well-known unsolved-problem collections or automatically generated conjecture databases.

Before any problem is treated as open, it is checked against the literature. A problem being listed as
open in a database is not sufficient evidence that it is unsolved.

## Pipeline

The identification pipeline is a durable, append-only funnel over a single SQLite corpus. Each stage
screens the survivors of the previous one, and re-running the pipeline never re-scores problems that
have already been processed. The expensive stages run only on the highest-scoring candidates, so cost
stays bounded.

```
ingesters -> filter -> triage -> kill-search -> deep-pass -> shortlist
              rules    LLM        literature     LLM
              + dedup  scoring    prior-art      review
```

- **Ingesters** pull problems from curated sources into the corpus, one module per source.
- **Filter** removes duplicates and out-of-scope entries with deterministic rules (no model calls).
- **Triage** scores each problem against a rubric for tractability, verifiability, and openness.
- **Kill-search** checks the top-scoring candidates against the published literature.
- **Deep-pass** is a closer review of the survivors, producing a recommendation for each.

`review/pipeline_report.py` prints a status dashboard showing, for each stage, how many problems have
been screened, how many are waiting, and the approximate model spend.

## Solving

Shortlisted problems are attempted with two complementary methods. Every claimed result must be
accompanied by a verification artifact — a Lean proof, an explicit certificate, or a re-runnable
evaluator — so that the result does not depend on trusting a model's output.

- **Derivation.** Language models draft a proof, a cross-field lemma, or a sharpened bound;
  independent models cross-check each other, and the statement is formalized in Lean.
- **Search.** Evolutionary search, SAT/MILP solvers, and problem-specific evaluators look for explicit
  constructions, bounds, or counterexamples that a small, trusted checker can verify.

## Installation

Requires Python 3.10+ and an OpenAI API key.

```bash
cd problem-id
python3 -m venv .venv
./.venv/bin/python -m pip install requests beautifulsoup4 lxml pyyaml openai feedparser pymupdf
```

The API key is read from `~/.config/proof_hunter/openai_key.txt`, or from the `OPENAI_API_KEY`
environment variable. It is kept outside the repository and is never committed.

## Usage

```bash
cd problem-id

# Status dashboard
./.venv/bin/python review/pipeline_report.py
./.venv/bin/python review/pipeline_report.py --detailed

# Add a source, then run the funnel (idempotent; only new problems are processed)
./.venv/bin/python corpus/kourovka.py
./.venv/bin/python triage/filter.py
./.venv/bin/python triage/score.py --workers 8
./.venv/bin/python killsearch/killsearch.py --top 50 --model gpt-5.5
```

See [`problem-id/README.md`](problem-id/README.md) for the full pipeline reference.

## Repository structure

| Path | Contents |
|------|----------|
| `problem-id/` | The identification pipeline. |
| `problem-id/corpus/` | Source ingesters, one per problem list. |
| `problem-id/triage/` | Filtering and scoring. |
| `problem-id/killsearch/` | Prior-art check and deep-pass review. |
| `problem-id/review/` | Reporting, including the status dashboard. |
| `PROBLEM_ID_PIPELINE.md` | Pipeline design and schema. |
| `PROBLEM_CRITERIA.md` | Definition of a suitable problem. |
| `META_GUIDE.md` | Strategy notes, case studies, and working log. |
| `OPENEVOLVE.md` | Notes on the evolutionary-search setup. |

## Authors

- Nikol Savova — Oxford
- Sihao Huang — Independent

## License

Not yet licensed. All rights reserved by the authors pending a license decision.
