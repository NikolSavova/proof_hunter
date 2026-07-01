---
description: Show the pipeline dashboard — sources ingested vs backlog, the funnel (screened/pending per stage), and Phase-II proof engines
---

Run the **pipeline report** and show me the dashboard.

1. Run it (pass `$ARGUMENTS` through so `--detail` or `--source <name>` work):
   ```bash
   cd problem-id && ./.venv/bin/python review/pipeline_report.py $ARGUMENTS
   ```
2. **Print the dashboard output verbatim** inside a code block (it's pre-formatted ASCII — do not
   reword or re-tabulate it; the monospace layout is the point).
3. Add a 2–3 line read underneath: the current **bottleneck** (the stage with the most `queued` /
   `not yet screened` problems) and the **immediate next pipeline action** to clear it (usually
   resuming the kill-search on the triaged backlog, or triaging a source still at `ingested`).

Notes:
- The script is read-only (safe to run anytime, even while an ingest or kill-search is in flight).
- It auto-detects ingested sources from the DB; the backlog/blocked list and the Phase-II engines
  live in editable registries at the top of `review/pipeline_report.py` — update those as sources
  get added or proof engines get built.
- The full source × stage matrix is shown by default; pass `--brief` to hide it. `--source <name>`
  focuses one source.
