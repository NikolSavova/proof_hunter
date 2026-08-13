#!/usr/bin/env python3
"""Sol copy-edit pass on the submission paper (prose/framing only, no mathematics).

Sends main.tex plus the author's edit brief to gpt-5.6-sol at max effort and archives the
returned edit list. Edits are applied by hand afterwards and the PDF recompiled; nothing
is written into main.tex by this script.
"""
import json, os, pathlib, time

import openai

ROOT = pathlib.Path(__file__).resolve()
BRUHAT = ROOT.parents[4]
PAPER = BRUHAT / "paper" / "submission"
KEY = (pathlib.Path.home() / ".config/proof_hunter/openai_key.txt").read_text().strip()
MODEL, EFFORT = "gpt-5.6-sol", "max"
IDS = ROOT.parent / "edit_ids.json"

brief = (PAPER / "edit_brief_20260812.md").read_text()
tex = (PAPER / "main.tex").read_text()

CTX = ("You are copy-editing a research paper in algebraic combinatorics for submission "
       "to a journal such as Electronic J. Combinatorics or Experimental Mathematics. "
       "You are editing PROSE AND FRAMING ONLY. The mathematics is settled and is not "
       "yours to change: no theorem, constant, numeral, table entry, equation, label, or "
       "scope condition may be altered. Follow the author's brief exactly.")

USER = (brief + "\n\n===== FULL SOURCE: main.tex =====\n" + tex)


def retry(fn, what, tries=60, wait=30):
    for i in range(tries):
        try:
            return fn()
        except (openai.APIConnectionError, openai.APITimeoutError, openai.InternalServerError) as e:
            print(f"  ({what}: {type(e).__name__}, retry {i+1}/{tries})", flush=True)
            time.sleep(wait)
    raise RuntimeError(what)


client = openai.OpenAI(api_key=KEY)
known = json.loads(IDS.read_text()) if IDS.exists() else {}
k = "paper_edit"
if k in known:
    print(f"resuming {known[k]}", flush=True)
    resp = retry(lambda: client.responses.retrieve(known[k]), "retrieve")
else:
    resp = retry(lambda: client.responses.create(
        model=MODEL, input=[{"role": "developer", "content": CTX},
                            {"role": "user", "content": USER}],
        reasoning={"effort": EFFORT}, background=True), "create")
    known[k] = resp.id
    IDS.write_text(json.dumps(known, indent=1))
    print(f"submitted ({MODEL}, effort={EFFORT}), id = {resp.id}", flush=True)

t0 = time.time()
while resp.status in ("queued", "in_progress"):
    if time.time() - t0 > 7200:
        raise TimeoutError()
    time.sleep(20)
    resp = retry(lambda: client.responses.retrieve(resp.id), "poll")
if resp.status != "completed":
    raise RuntimeError(f"{resp.status}: {getattr(resp, 'error', None)}")
out = PAPER / "edit_list_20260812.md"
out.write_text(f"# Sol copy-edit list ({MODEL}, effort={EFFORT}) — {time.strftime('%Y-%m-%d %H:%M')}\n\n"
               "> Proposed edits ONLY. Not yet applied to main.tex. Prose/framing pass per\n"
               "> edit_brief_20260812.md; the editor was instructed to change no mathematics.\n\n"
               + resp.output_text)
print(f"completed, {len(resp.output_text)} chars -> {out.name}", flush=True)
