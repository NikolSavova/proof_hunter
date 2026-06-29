"""Stage-0.5 — compilation-expansion pass.

Many ingested records are SURVEY / "open problems in X" papers that each list 10-20
distinct open problems but were stored as ONE record (just the title + abstract). Those
surveys hide our best low-saturation single problems, but score poorly *as a unit* (a list
is not a sharp problem), so we must NOT gate on the parent's composite. This pass:

  1. selects compilation-tagged records (see corpus/arxiv_openproblems.py),
  2. fetches each paper's full text (ar5iv / arXiv HTML),
  3. asks gpt-5-mini to extract each DISTINCT, explicitly-posed OPEN problem that falls
     within our field scope (the LLM is also the scope filter — out-of-scope surveys like
     wireless / RL / deep-learning return an empty list),
  4. inserts each as its own child record (id `<parent>#<n>`, stage=ingested) so the normal
     Stage-1 filter + Stage-2 triage pick them up,
  5. marks the parent `expanded` so it is not re-expanded and is excluded from finalists.

Idempotent: a parent already marked `expanded` is skipped unless --force. Children flow
through filter/score normally; score.py's `scores IS NULL` guard means re-runs never re-spend.

Usage:
    python corpus/expand_compilations.py --dry --limit 3        # preview extraction, no DB writes
    python corpus/expand_compilations.py --ids arxiv-openproblem:2303.11464v1
    python corpus/expand_compilations.py --limit 40 --workers 4 # expand a batch
    python corpus/expand_compilations.py                        # expand all un-expanded compilations
"""
from __future__ import annotations
import argparse, json, pathlib, re, sys, time
import requests
from bs4 import BeautifulSoup

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import common  # noqa: E402

MODEL = "gpt-5-mini"
MAX_TEXT_CHARS = 48000     # keep the LLM context bounded; surveys' problem sections sit early/mid
MAX_PROBLEMS = 30          # hard cap of children per paper (runaway guard)

EXTRACT_SCHEMA = {
    "name": "compilation_expand",
    "strict": True,
    "schema": {
        "type": "object", "additionalProperties": False,
        "properties": {
            "in_scope": {"type": "boolean"},
            "problems": {
                "type": "array",
                "items": {
                    "type": "object", "additionalProperties": False,
                    "properties": {
                        "title": {"type": "string"},
                        "statement": {"type": "string"},
                        "field": {"type": "array", "items": {"type": "string"}},
                        "still_open": {"type": "boolean"},
                    },
                    "required": ["title", "statement", "field", "still_open"],
                },
            },
        },
        "required": ["in_scope", "problems"],
    },
}

def system_prompt(rubric: dict) -> str:
    s = rubric["scope"]
    return (
        "You extract INDIVIDUAL open mathematics problems from a survey / 'open problems in X' "
        "paper, for an AI-augmented research team (Oxford pure-math undergrad + MIT physics/ML grad). "
        "From the paper text, list every DISTINCT, explicitly-posed problem/conjecture/question that "
        "is presented as OPEN (unsolved). For each: a short title, a self-contained verbatim-or-faithful "
        "statement (include the key definitions/bounds/parameters needed to understand it standalone), "
        "its field(s), and still_open (false if the paper states it was since solved).\n\n"
        f"SCOPE FILTER. CORE fields: {s['core']}. ADJACENT (ok): {s['adjacent']}. The problems must be "
        "RESEARCH-GRADE open problems posed by working mathematicians. Set in_scope=false (and return an "
        "empty list) if the paper as a whole is primarily any of:\n"
        "- recreational / historical-curiosity (puzzles, medieval problem lists, olympiad-style exercises);\n"
        "- benchmark / meta (AI-LLM benchmarks, 'test-time learning', verifier-design / ML-evaluation tasks);\n"
        "- applied-engineering (wireless / 6G / networking, UAVs, applied deep learning, reinforcement-"
        "learning systems, federated learning, data mining, hardware, biology, control engineering);\n"
        f"- deep-machinery-excluded: {s['exclude_unless_self_certifying']} (algebraic geometry, operator "
        "algebras / von Neumann factors, geometric topology, hard PDE) unless concretely self-certifying;\n"
        "- otherwise outside mathematics / theoretical physics / TCS.\n"
        "If in scope, extract only the in-scope, research-grade problems (skip the rest). Do NOT invent "
        "problems not in the text. Prefer precise, self-certifying, construction/bound/quantitative "
        "problems. Cap at 30 problems. Output ONLY the schema."
    )

def strip_version(arxiv_id: str) -> str:
    return re.sub(r"v\d+$", "", arxiv_id)

def fetch_fulltext(arxiv_id: str) -> tuple[str | None, str]:
    """Return (text, source_tag). Tries ar5iv then arXiv native HTML. None if unavailable."""
    base = strip_version(arxiv_id)
    attempts = [
        (f"https://ar5iv.org/abs/{base}", "ar5iv"),
        (f"https://arxiv.org/html/{arxiv_id}", "arxiv-html"),
        (f"https://arxiv.org/html/{base}", "arxiv-html"),
    ]
    for url, tag in attempts:
        try:
            r = requests.get(url, timeout=40, headers={"User-Agent": "problem-id research pipeline"})
            if r.status_code != 200 or "<html" not in r.text.lower():
                continue
            soup = BeautifulSoup(r.text, "lxml")
            # drop bibliography / nav / scripts to save tokens
            for sel in soup.select("script, style, nav, header, footer, .ltx_bibliography, "
                                   ".ltx_appendix, .ltx_acknowledgements"):
                sel.decompose()
            article = soup.find("article") or soup.find("div", class_="ltx_page_content") or soup.body
            text = re.sub(r"\n{3,}", "\n\n", article.get_text("\n")) if article else ""
            if len(text.strip()) > 1200:   # got a real body, not a stub/error page
                return text[:MAX_TEXT_CHARS], tag
        except Exception:
            continue
    return None, "none"

def extract(client, rubric, title: str, text: str, effort: str) -> dict:
    user = f"PAPER TITLE: {title}\n\nPAPER TEXT (may be truncated):\n{text}"
    kwargs = dict(
        model=MODEL,
        messages=[{"role": "system", "content": system_prompt(rubric)},
                  {"role": "user", "content": user}],
        response_format={"type": "json_schema", "json_schema": EXTRACT_SCHEMA},
        max_completion_tokens=8000,
    )
    last = None
    for attempt in range(4):  # retry transient connection/rate-limit errors with backoff
        try:
            try:
                resp = client.chat.completions.create(reasoning_effort=effort, **kwargs)
            except TypeError:
                resp = client.chat.completions.create(**kwargs)
            return json.loads(resp.choices[0].message.content)
        except Exception as e:
            last = e
            if attempt < 3:
                time.sleep(3 * (attempt + 1))
    raise last

def select_parents(con, ids=None, limit=None, force=False):
    if ids:
        q = "SELECT * FROM problems WHERE id IN (%s)" % ",".join("?" * len(ids))
        rows = con.execute(q, ids).fetchall()
    else:
        # compilation-tagged, still a container (not yet expanded), not garbage
        cond = "tags LIKE '%compilation%' AND stage NOT IN ('rejected','duplicate')"
        if not force:
            cond += " AND tags NOT LIKE '%expanded%'"
        rows = con.execute(f"SELECT * FROM problems WHERE {cond} ORDER BY year_posted DESC").fetchall()
    return rows[:limit] if limit else rows

def expand_one(client, rubric, parent, effort, dry):
    raw = json.loads(parent["raw"] or "{}")
    arxiv_id = raw.get("arxiv_id") or parent["id"].split(":", 1)[-1]
    text, src = fetch_fulltext(arxiv_id)
    if not text:
        return {"id": parent["id"], "status": "no-fulltext", "children": []}
    out = extract(client, rubric, parent["title"], text, effort)
    if not out.get("in_scope"):
        return {"id": parent["id"], "status": f"out-of-scope ({src})", "children": []}
    probs = [p for p in out["problems"] if p.get("still_open", True)][:MAX_PROBLEMS]
    children = []
    for i, p in enumerate(probs, 1):
        stmt = p["statement"].strip()
        if len(stmt) < 40:
            continue
        children.append({
            "id": f"{parent['id']}#{i}",
            "source": parent["source"],
            "source_url": parent["source_url"],
            "title": p["title"].strip()[:300],
            "statement": (f"{p['title'].strip()}\n\n{stmt}")[:8000],
            "field": p.get("field") or json.loads(parent["field"] or "[]"),
            "year_posted": parent["year_posted"],
            "status_claimed": "open",
            "tags": ["tier-a", "low-saturation", "arxiv-openproblem", "expanded-child", "single-problem"],
            "stage": "ingested",
            "raw": {"arxiv_id": arxiv_id, "parent_id": parent["id"], "child_index": i,
                    "fulltext_source": src},
        })
    return {"id": parent["id"], "status": f"{len(children)} problems ({src})",
            "children": children}

def run(ids=None, limit=None, workers=4, dry=False, force=False, effort="low"):
    con = common.db()
    rubric = common.load_rubric()
    client = common.openai_client()
    parents = select_parents(con, ids, limit, force)
    print(f"[expand] {len(parents)} compilation papers to process "
          f"(model={MODEL}, effort={effort}, workers={workers}, dry={dry})")

    total_children = 0
    def work(parent):
        return expand_one(client, rubric, parent, effort, dry)

    results = []
    if workers <= 1:
        for p in parents:
            try: results.append(work(p))
            except Exception as e: results.append({"id": p["id"], "status": f"ERROR {repr(e)[:80]}", "children": []})
    else:
        from concurrent.futures import ThreadPoolExecutor, as_completed
        with ThreadPoolExecutor(max_workers=workers) as ex:
            futs = {ex.submit(work, p): p for p in parents}
            for fut in as_completed(futs):
                p = futs[fut]
                try: results.append(fut.result())
                except Exception as e:
                    results.append({"id": p["id"], "status": f"ERROR {repr(e)[:80]}", "children": []})

    # persist in the main thread (sqlite write safety)
    for res, parent in [(r, next(pp for pp in parents if pp["id"] == r["id"])) for r in results]:
        n = len(res["children"])
        total_children += n
        flag = "DRY " if dry else ""
        print(f"  {flag}{res['id']:34} -> {res['status']}")
        if dry:
            for c in res["children"]:
                print(f"        · {c['title'][:88]}")
            continue
        for c in res["children"]:
            common.upsert(con, c)
        if not res["status"].startswith("no-fulltext") and not res["status"].startswith("ERROR"):
            # mark parent expanded (idempotency + exclude from finalists) even if 0 children (out-of-scope)
            tags = json.loads(parent["tags"] or "[]")
            if "expanded" not in tags:
                tags.append("expanded")
            praw = json.loads(parent["raw"] or "{}"); praw["expanded_children"] = n
            con.execute("UPDATE problems SET tags=?, raw=? WHERE id=?",
                        (json.dumps(tags), json.dumps(praw), parent["id"]))
    con.commit()
    print(f"[expand] {'(dry) ' if dry else ''}extracted {total_children} child problems "
          f"from {len(parents)} compilations -> {common.DB_PATH}")
    return total_children

# allow run.py to call ingest() uniformly (no-op-safe wrapper)
def ingest():
    return run()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids", nargs="*", default=None, help="specific parent ids to expand")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--dry", action="store_true", help="preview extraction, no DB writes")
    ap.add_argument("--force", action="store_true", help="re-expand already-expanded parents")
    ap.add_argument("--effort", default="low", choices=["low", "medium", "high"])
    a = ap.parse_args()
    run(a.ids, a.limit, a.workers, a.dry, a.force, a.effort)
