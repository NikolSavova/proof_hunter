---
description: Open the session — set up the session, load all project context, and orient
---

Run the **Session START protocol** from `CLAUDE.md` now:

1. **Remind me (the human) to set up the session** — print the setup reminder: switch on
   **auto-accept edits** (Shift+Tab), bump **reasoning effort to high** (`/config`), and add
   **"ultracode"** to prompts for heavy multi-agent work (pipeline runs, prior-art sweeps, deep-passes).
2. **`git pull`** — sync the other collaborator's work before touching anything.
3. **Load context:** read `HANDOFF.md` (live state + next steps; the single source of truth), then
   skim `META_GUIDE.md` §8 (recent working-log entries). Read `PROBLEM_ID_PIPELINE.md` and
   `problem-id/README.md` too if this session will touch the pipeline.
4. **Sanity-check the pipeline** if you'll use it:
   `cd problem-id && ./.venv/bin/python -c "import common; print(common.db().execute('SELECT COUNT(*) FROM problems').fetchone()[0])"`
   → prints the corpus size (900 as of the last run).
5. **Summarize for me** in a few lines: where the project stands, what the immediate next action is
   (per `HANDOFF.md` §7), and anything awaiting my input.

If `$ARGUMENTS` is non-empty, focus the orientation on that topic.
