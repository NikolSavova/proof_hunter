"""Deep pass — high-confidence vetting of the top finalists with a strong model + web search.

Runs AFTER the bulk kill-search, on the best few survivors only. A stronger model + a deeper
prompt: re-confirm genuine openness, give an explicit go/maybe/no-go for a 1-week attack, and
name the first concrete step. This is the de-risking read before committing Phase II.

DURABLE + RESUMABLE (rewritten 2026-06-30, Sihao):
- Each verdict is written to the DB (new `deeppass` column, JSON) the instant it completes. The
  SQLite DB is the synced source of truth, so progress SURVIVES A HANDOFF — pull the repo and a
  collaborator sees every verdict computed so far. (The old version wrote ONLY to an uncommitted
  local .md and truncated it on every run, so a stopped run lost everything and couldn't resume.)
- On restart it SKIPS any finalist that already has a `deeppass` verdict, i.e. it picks up exactly
  where a stopped run left off instead of recomputing from scratch. `--force` recomputes anyway.
- Still NON-DESTRUCTIVE to the rest of the pipeline: it ONLY writes the new `deeppass` column.
  Existing kill-search verdicts (`killsearch`), `stage`, and `drop_reason` are left exactly as-is.
- The .md (OUT, below) is a RENDERED VIEW of the DB, rebuilt after every problem — never the
  source of truth, never truncated mid-progress.

Run-2 finalists are identified machine-independently from the committed dossier
(review/finalists_run2_detailed.md), not from any per-machine scratch file.

NOTE — two independent reads exist for the run-2 top-8 (2026-06-30): Nikol's is canonical in
`review/deeppass_run2.md`; Sihao's (this tool's renderer) is in `review/deeppass_run2_sihao.md`.
They were cross-examined (see HANDOFF section 3). This renderer writes the *_sihao.md file so a
re-run never overwrites Nikol's read; the DB `deeppass` column holds the Sihao-run verdicts.

Model: default gpt-5.5. gpt-5.5-pro is unusable for a BATCH on a 200k-TPM org (one Pro+web call
saturates the minute -> every call exhausts retries and fails); use `--model gpt-5.5-pro` only for
1-2 hand-picked problems via --ids, never the full top-8.

Usage:
    python killsearch/deeppass.py --top 8                      # top-8 run-2 finalists by composite
    python killsearch/deeppass.py --ids arxiv-openproblem:..#3 # specific problems (e.g. run-1 anchors)
    python killsearch/deeppass.py --ids <id> --model gpt-5.5-pro --force   # 1-2 picks, strongest model
"""
from __future__ import annotations
import argparse, json, pathlib, re, sys, time
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import common  # noqa: E402
import killsearch  # reuse the robust background-response poller  # noqa: E402

# Default to gpt-5.5 (non-pro): gpt-5.5-pro on this org's 200k TPM cannot sustain a multi-problem
# batch (one Pro+web call saturates the minute -> every call exhausts retries and fails). Use
# `--model gpt-5.5-pro` only for 1-2 hand-picked problems, never a batch.
MODEL = "gpt-5.5"
REVIEW = pathlib.Path(__file__).resolve().parents[1] / "review"
OUT = REVIEW / "deeppass_run2_sihao.md"        # rendered view (Nikol's read stays in deeppass_run2.md)
RUN2_DOSSIER = REVIEW / "finalists_run2_detailed.md"

SCHEMA = {
    "type": "object", "additionalProperties": False,
    "properties": {
        "still_open": {"type": "boolean"},
        "openness_confidence": {"type": "string", "enum": ["low", "medium", "high"]},
        "verdict": {"type": "string", "enum": ["green", "amber", "red"]},
        "closest_prior": {"type": "string"},
        "why_not_already_done": {"type": "string"},   # deeper: why is this still open?
        "one_week_recommendation": {"type": "string", "enum": ["go", "maybe", "no-go"]},
        "first_concrete_step": {"type": "string"},     # what to literally do on day 1
        "key_risk": {"type": "string"},
        "engine": {"type": "string", "enum": ["A", "B", "both"]},
    },
    "required": ["still_open", "openness_confidence", "verdict", "closest_prior",
                 "why_not_already_done", "one_week_recommendation", "first_concrete_step",
                 "key_risk", "engine"],
}

PROMPT = """You are a senior mathematician giving a GO/NO-GO read on whether a small AI-augmented \
team (Oxford pure-math undergrad + MIT physics/ML grad; tools: GPT-5.5-Pro, Claude Opus, OpenEvolve \
evolutionary search, SAT, Lean) could produce a NEW, verifiable, publishable result on this problem \
in ~1 WEEK. This is a higher-confidence second pass after a cheaper kill-search already marked it AMBER.

Use web search aggressively. Be decisive and concrete:
1. Re-confirm genuine openness — find the closest existing result; is the gap really still open, or \
derivable-on-sight from known work? (Erdősgate discipline: "listed as open" != unsolved.)
2. why_not_already_done: if it IS open, explain WHY it survived — what makes it non-trivial yet not hopeless.
3. one_week_recommendation: GO (clear self-certifying win achievable in a week), MAYBE (plausible but \
real risk), or NO-GO (too hard / likely already done / not self-certifying in a week). Earn a GO.
4. first_concrete_step: the literal Day-1 action (the SAT/MILP encoding, the lemma to draft, the \
evaluator to build). key_risk: the single thing most likely to sink it. engine: A (lemma/quant-extension) \
or B (search/construction) or both."""


def ensure_deeppass_col(con):
    """Add the `deeppass` column once. Additive + idempotent — never touches existing columns."""
    cols = [r[1] for r in con.execute("PRAGMA table_info(problems)").fetchall()]
    if "deeppass" not in cols:
        con.execute("ALTER TABLE problems ADD COLUMN deeppass TEXT")
        con.commit()


def run2_ids():
    """The run-2 finalist ids, parsed from the committed dossier headers (machine-independent).

    Header form: '## 1. [AMBER] arxiv-openproblem:2406.00790v2#2  (composite 4.8429, ...)'.
    """
    if not RUN2_DOSSIER.exists():
        return []
    ids = []
    for line in RUN2_DOSSIER.read_text().splitlines():
        m = re.match(r"^##\s+\d+\.\s+\[[A-Za-z-]+\]\s+(\S+)\s+\(composite", line)
        if m:
            ids.append(m.group(1))
    return ids


def deep_one(client, model, prob):
    import openai
    user = (f"PROBLEM (id {prob['id']}, source {prob['source']}, {prob['source_url']})\n"
            f"TITLE: {prob['title']}\nRESTATEMENT: {prob['restatement']}\n"
            f"WIN CONDITION: {prob['win_condition']}\nPRIOR KILL-SEARCH NOTES: "
            f"{json.loads(prob['killsearch'] or '{}').get('novelty_notes','')}\n\n"
            f"FULL TEXT:\n{(prob['statement'] or '')[:3500]}")
    tool = {"type": "web_search", "search_context_size": "low"}
    for attempt in range(killsearch.MAX_RETRIES):
        try:
            resp = client.responses.create(
                model=model,
                input=[{"role": "developer", "content": PROMPT},
                       {"role": "user", "content": user}],
                tools=[tool], reasoning={"effort": "high"},
                text={"format": {"type": "json_schema", "name": "deeppass",
                                 "schema": SCHEMA, "strict": True}},
                background=True,
            )
            resp = killsearch._retrieve(client, resp.id)
            if resp.status == "completed":
                return json.loads(resp.output_text)
            err = getattr(resp, "error", None)
            if "rate_limit" in str(getattr(err, "code", "")) or "rate_limit" in str(err):
                w = 70 * (attempt + 1); print(f"    (TPM; wait {w}s)"); time.sleep(w); continue
            raise RuntimeError(f"response {resp.status}: {err}")
        except openai.RateLimitError:
            w = 70 * (attempt + 1); print(f"    (429 TPM; wait {w}s)"); time.sleep(w)
        except openai.APIConnectionError:
            w = 20 * (attempt + 1); print(f"    (conn; retry {w}s)"); time.sleep(w)
        except TypeError:
            tool = {"type": "web_search"}
    raise RuntimeError("deep_one: exhausted retries")


def select(con, ids, top):
    """Targets to deep-pass, ordered by composite desc. Default = top-N run-2 finalists."""
    if ids:
        rows = [con.execute("SELECT * FROM problems WHERE id=?", (i,)).fetchone() for i in ids]
        return [r for r in rows if r]
    targets = run2_ids()
    if not targets:
        # Fallback: all finalists by composite (e.g. dossier missing) — still durable + resumable.
        rows = con.execute("SELECT * FROM problems WHERE stage='finalist' AND killsearch IS NOT NULL "
                           "ORDER BY CAST(composite AS REAL) DESC").fetchall()
        return rows[:top]
    rows = []
    for i in targets:
        r = con.execute("SELECT * FROM problems WHERE id=?", (i,)).fetchone()
        if r:
            rows.append(r)
    rows.sort(key=lambda r: float(r["composite"] or 0), reverse=True)
    return rows[:top]


def render_md(con, model):
    """Rebuild the markdown view from the DB. Every finalist that has a deeppass verdict appears,
    ordered by composite desc. Called after each write so the file always reflects real progress."""
    from collections import Counter
    rows = con.execute("SELECT * FROM problems WHERE deeppass IS NOT NULL "
                       "ORDER BY CAST(composite AS REAL) DESC").fetchall()
    header = (f"# Deep pass (Sihao run) — high-confidence GO/NO-GO on the top run-2 finalists\n\n"
              f"_Model {model} + web search, high effort. Independent of Nikol's read in "
              f"`deeppass_run2.md` (the two were cross-examined — see HANDOFF section 3). Source of truth "
              f"is the DB `deeppass` column (durable across handoffs); this file is a rendered view._\n")
    parts = [header]
    for r in rows:
        dp = json.loads(r["deeppass"])
        parts.append(
            f"\n## [{dp['verdict'].upper()} · {dp['one_week_recommendation'].upper()}] {r['id']} "
            f"(composite {r['composite']}, openness conf {dp['openness_confidence']})\n"
            f"**Problem:** {r['restatement'] or r['title']}\n\n"
            f"**Win condition:** {r['win_condition']}\n\n"
            f"**Still open / closest prior:** open={dp['still_open']} — {dp['closest_prior']}\n\n"
            f"**Why not already done:** {dp['why_not_already_done']}\n\n"
            f"**1-week recommendation:** {dp['one_week_recommendation'].upper()} "
            f"(engine {dp['engine']})\n\n"
            f"**First concrete step:** {dp['first_concrete_step']}\n\n"
            f"**Key risk:** {dp['key_risk']}\n")
    rec = Counter(json.loads(r["deeppass"])["one_week_recommendation"] for r in rows)
    parts.append(f"\n---\n_Summary: {dict(rec)} across {len(rows)} problems._\n")
    OUT.write_text("".join(parts))


def run(ids=None, top=8, model=MODEL, force=False):
    con = common.db()
    client = common.openai_client()
    ensure_deeppass_col(con)
    rows = select(con, ids, top)
    done = {r["id"] for r in rows if r["deeppass"] is not None}
    todo = [r for r in rows if force or r["deeppass"] is None]
    if done and not force:
        print(f"[deeppass] resume: {len(done)} already done (skipping), {len(todo)} to do.")
    print(f"[deeppass] {len(todo)} finalists -> {model} (web, high effort). "
          f"Writing to DB `deeppass` column + {OUT.name} (view).")
    render_md(con, model)  # ensure the view reflects whatever is already in the DB
    for r in todo:
        prob = dict(r); t0 = time.time()
        try:
            dp = deep_one(client, model, prob)
        except Exception as e:
            print(f"  ! {r['id']} deep-pass failed: {repr(e)[:160]}"); continue
        # Persist immediately: durable across handoffs, and makes the run resumable.
        con.execute("UPDATE problems SET deeppass=? WHERE id=?", (json.dumps(dp), r["id"]))
        con.commit()
        render_md(con, model)
        print(f"  {r['id']}: {dp['verdict'].upper()}/{dp['one_week_recommendation'].upper()} "
              f"({time.time()-t0:.0f}s) eng={dp['engine']}  {dp['why_not_already_done'][:70]}")
        time.sleep(killsearch.INTER_CALL_SLEEP)
    print(f"[deeppass] done. View -> {OUT}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids", nargs="*", default=None)
    ap.add_argument("--top", type=int, default=8)
    ap.add_argument("--model", default=MODEL)
    ap.add_argument("--force", action="store_true", help="recompute even if a verdict already exists")
    a = ap.parse_args()
    run(a.ids, a.top, a.model, a.force)
