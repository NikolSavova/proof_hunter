# G2 closure campaign — 2026-08-11 (Sihao session, run log)

**What this is:** a 7-draft blind-draft + adversarial-referee fleet on the G2
residue items (T2 §8 items 1, 2, 4, 5) + the overdue house-rule referee pass on
`g2_draft_t2_20260803.md` itself + a synthesis STATUS.md. Goal: close G2 ⇒
Theorem A = F2(a) fully proved.

**Work packages:** wp1 a–d = four independent routes at the deep-tilt
far-region lemma (items 1+5); wp2 a–b = the two remaining bucket-table pieces
(item 4); wp3 a = the C₀=2000→small region-2 handoff (item 2). Each draft gets
a maths referee + a numerics referee (default-to-refute, re-run everything).
Blind protocol: drafts can't read each other or `g2_draft_t1_20260803.md`.

**Run state (as of 2026-08-11 ~15:00 PT):**
- Attempt 1 died at the session rate limit (~90 min in, 0 agents completed).
- Attempt 2 (API credits) relaunched ~12:35 PT, run ID `wf_b991443b-682`;
  as of ~15:00 all 7 drafts still in flight (200–330 KB of transcript each),
  0 completed, no draft files on disk yet.
- Resume machinery (Sihao's machine, session `0c711691…`): script at
  `~/.claude/projects/-Users-sihaohuang-Desktop-Coding-proof-hunter-phase2-bruhat/0c711691-81ac-42b2-8712-819b1ee08f6b/workflows/scripts/g2-closure-campaign-wf_b991443b-682.js`,
  resume with `resumeFromRunId: wf_b991443b-682`, args `{"date": "20260811"}`.
  Completed agents replay from cache; in-flight work at interruption re-runs.
- Raw transcripts (survive any crash, machine-local):
  `~/.claude/projects/-Users-sihaohuang-Desktop/0c711691-81ac-42b2-8712-819b1ee08f6b/subagents/workflows/wf_b991443b-682/agent-*.jsonl`
  — mineable if a draft dies mid-write.

**Expected outputs (when done):** `wp*_draft_*.md`, `referee_{maths,numerics}_wp*_*.md`,
`referee_t2_{maths,numerics}.md`, `STATUS.md` — all in this directory; scripts
under `../g2_scripts/campaign_20260811/`.

**House rules that bind any consumer of these outputs:** nothing here counts
until BOTH referees pass it (SURVIVES / MINOR_REPAIRS); STATUS.md's ledger has
an explicit no-grade-inflation rule. Do not erase or overwrite; new files only.
