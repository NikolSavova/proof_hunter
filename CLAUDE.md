# CLAUDE.md — working protocol for Proof Hunter

> Auto-loaded by Claude Code every session, and committed to GitHub so it loads identically
> for **both collaborators**. Keep it short; it costs context on every load. The substance
> lives in `HANDOFF.md` (live state) and `META_GUIDE.md` (strategy + append-only log).

## What this project is (one paragraph)
An AI-leveraged run at a **novel, publishable maths result in ~1 week**, where the enabler is
frontier AI (Opus, GPT-5.5-Pro, OpenEvolve, SAT, Lean). Two engines: **A** = LLM cross-domain
lemma / quantitative-extension; **B** = evolutionary/SAT search for explicit constructions/bounds.
Every result ships a **verification artifact**. Phase I (problem-identification pipeline in
`problem-id/`) is built and has run once. Full context: read `HANDOFF.md` first, then `META_GUIDE.md`.

## Collaborators (work from different machines, sync via GitHub)
- **Nikol** — Oxford maths undergrad · proof / problem-selection / verification lead.
- **Sihao** (sihao.c.huang@gmail.com) — MIT physics grad · infra / Engine-B / QIT lead.
- **Assume the other person has worked since you last saw the repo.** Always `git pull` before
  starting, and leave a clean handoff + commit when you stop.

## Git auth (per machine — `/load` pulls and `/handoff` pushes automatically)
Auth is via **SSH** (`origin` = `git@github.com:NikolSavova/proof_hunter.git`). Each collaborator
configures this **once per machine** (keys are per-machine; they do NOT sync via the repo):
1. `ssh-keygen -t ed25519 -C "you@email" -f ~/.ssh/id_ed25519 -N ""`
2. Add `~/.ssh/id_ed25519.pub` to GitHub → Settings → SSH and GPG keys → New SSH key.
3. `git remote set-url origin git@github.com:NikolSavova/proof_hunter.git`
4. Test: `ssh -T git@github.com` (expect "Hi <user>! You've successfully authenticated").
Once set, `/load` runs `git pull --rebase` and `/handoff` runs `git pull --rebase` + `git push`
with no password prompts. If a push fails on auth, this machine's key isn't on the account yet.

## The secret — NEVER commit
The OpenAI key lives **outside the repo** at `~/.config/proof_hunter/openai_key.txt` (perms 600).
`.gitignore` blocks `*key*.txt` as a backstop. Never print, paste, or commit it. On a fresh clone
the key file must be recreated locally (set `$OPENAI_API_KEY` or write that file).

## ▶ Session START protocol
**Step 0 — remind the human to set up the session for deep work** (print this first, every session):
> 🔧 Before we dig in, set your session up:
> • **Auto-accept edits** — press **Shift+Tab** to cycle into auto-accept mode (no per-edit prompts).
> • **High reasoning effort** — bump effort to high (via `/config`); this is deep maths/research work.
> • **Ultracode** — include the word **"ultracode"** in your prompt to opt into multi-agent
>   workflow orchestration (parallel search, adversarial verify, kill-search at scale). Worth it for
>   pipeline runs, prior-art sweeps, and finalist deep-passes; skip it for quick edits.

**Then load context and orient:**
1. `git pull` — pull the other collaborator's work before touching anything.
2. Read `HANDOFF.md` (live state + next steps) — the single source of truth. Skim `META_GUIDE.md`
   §8 (recent working-log entries) and `PROBLEM_ID_PIPELINE.md` if you'll touch the pipeline.
3. Sanity-check the pipeline if you'll use it:
   `cd problem-id && ./.venv/bin/python -c "import common; print(common.db().execute('SELECT COUNT(*) FROM problems').fetchone()[0])"`
   → prints the corpus size (900 as of the last run).

## ⏹ Session CLOSE protocol  ← do ALL of this when asked to "close the session" / "wrap up" / "write the handoff"
The goal: a fresh session (or the other collaborator) can fully resume from the repo alone.
1. **Update `HANDOFF.md` in place** so it reflects *current* reality — it is the live "state of
   the world," kept current (not append-only). Refresh especially: §3 (what we've done), §4 (what
   still needs building), §7 (immediate next action). It must stay self-contained.
2. **Append a dated entry to `META_GUIDE.md` §8 Working log** (newest first): what changed this
   session, decisions made, open questions, approximate spend. This is the permanent chronology.
3. **Capture in-flight state explicitly**: anything half-done, any command mid-run, any decision
   awaiting a human, and the exact file paths touched. Don't assume memory carries over.
4. **Write a note to the other collaborator** if your work changes what they should do next
   (e.g. "Sihao: added the West ingester; pull and re-run `triage/score.py`").
5. **Git hygiene**: `git status`; confirm no secrets / `.venv` / `__pycache__` / `.DS_Store`
   staged; stage the real changes; commit with a clear message. **Push so the collaborator can
   pull** (pushing the handoff is the whole point — push at session close unless told otherwise).
6. **Update file-memory** if a durable fact changed.
7. **End with a 3–5 line summary** to the human: what shipped, what's next, what needs their input.

## House rules (from the strategy bible — don't violate)
- **Prior-art kill-search is step one, never skipped** — "open in a database" ≠ unsolved (Erdősgate).
- **Never ship a single-model proof** — cross-examine with the other model, then Lean it.
- **Run the cheap sampling baseline before any evolutionary search** (Engine B).
- Pipeline idempotency: `score.py` skips already-scored problems; the durable DB is append-only —
  growing the corpus never re-spends. Use `--rescore` only to force re-scoring.
