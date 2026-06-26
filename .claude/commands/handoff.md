---
description: Close the session — write the full handoff (update HANDOFF.md, append the working log, commit & push)
argument-hint: [optional extra notes to weave into the handoff]
---

Run the **Session CLOSE protocol** from `CLAUDE.md` now. Execute every step:

1. **Update `HANDOFF.md` in place** so it reflects current reality — refresh §3 (what we've done),
   §4 (what still needs building), §7 (immediate next action). It must stay self-contained: a fresh
   session or the other collaborator should be able to fully resume from `HANDOFF.md` alone.
2. **Append a dated entry to `META_GUIDE.md` §8 Working log** (newest first): what changed this
   session, decisions made, open questions, approximate spend.
3. **Capture in-flight state explicitly**: half-done work, any command mid-run, decisions awaiting a
   human, and the exact file paths touched.
4. **Note to the other collaborator** (Nikol ↔ Sihao) if your work changes what they should do next.
5. **Git hygiene**: `git status`; confirm **no secrets / `.venv` / `__pycache__` / `.DS_Store`** are
   staged (double-check no `*key*.txt`); stage the real changes; commit with a clear message; then
   **push** so the collaborator can pull.
6. **Update file-memory** if a durable fact changed.
7. **End with a 3–5 line summary**: what shipped, what's next, what needs human input.

If `$ARGUMENTS` is non-empty, weave those notes into the handoff as additional session context.
