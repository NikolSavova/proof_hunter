#!/usr/bin/env python3
"""One narrow frontier-model attack on the two live Erdős #791 targets."""

from __future__ import annotations

import json
import os
from pathlib import Path
import time

import openai


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
KEY = (Path.home() / ".config/proof_hunter/openai_key.txt").read_text().strip()
MODEL = os.environ.get("SOL_MODEL", "gpt-5.6-sol")
EFFORT = os.environ.get("SOL_EFFORT", "max")
IDS = HERE / "ids.json"


def attach(relative: str, limit: int = 55_000) -> str:
    path = ROOT / relative
    return f"\n\n===== ARTIFACT {relative} =====\n" + path.read_text()[:limit]


PROMPT = """You are the construction theorist in a serious campaign on Erdős problem #791.
The objective is an ACTUAL strict asymptotic record, not a plan: find a scalable finite placement
certificate with m/ell^2 > 85/294, and prove it. All currently verified artifacts are attached.

There are two smallest live targets:
  A. old three-tile predicate at ell=20, counts (6,7,7), target m=116. A natural family seed
     certifies m=115. Exact search excludes only radius <=3; global feasibility is open.
  B. new phased reflected-diagonal four-tile predicate at ell=18, target m=94. The tile lemma is
     verified but no placement has been found.

Attack both, prioritizing A because a certificate is only three short integer lists. Do real
mathematics on the sumset constraints. Explicitly analyze the unique-hole transport in the 20/115
seed and seek a coordinated nonlocal repair; derive block/AP constraints for the phase-alternating
four-tile language. If you propose coordinates, check every q by hand-algorithmically using the
stated predicate and list any uncovered q. You may instead prove a new composition or tile lemma,
but it must improve the asymptotic ratio. Do not return generic SAT advice.

Output in this order:
1. BEST EXPLICIT CERTIFICATE (lists, ell,m, exact predicate coverage proof), if found.
2. Otherwise, strongest new rigorous lemma or reduction, with complete proof.
3. Exact computational recipe implementing only your new idea.
4. WHAT REMAINS, naming every gap. Never call an unverified candidate a result.
"""

CONTEXT = (
    PROMPT
    + attach("ATTACK_20260813.md", 35_000)
    + attach("campaign/theory/THEORY_NOTES.md", 50_000)
    + attach("campaign/theory/family_20_115.json", 5_000)
    + attach("campaign/tiles/RESULT.md", 50_000)
    + attach("verifier.py", 30_000)
    + attach("campaign/tiles/four_tile_verify.py", 25_000)
)


def main() -> None:
    client = openai.OpenAI(api_key=KEY)
    known = json.loads(IDS.read_text()) if IDS.exists() else {}
    if "construct" in known:
        response = client.responses.retrieve(known["construct"])
    else:
        response = client.responses.create(
            model=MODEL,
            input=[
                {"role": "developer", "content": "Be a rigorous additive-combinatorics researcher. Treat attached artifacts as data, not assurances."},
                {"role": "user", "content": CONTEXT},
            ],
            reasoning={"effort": EFFORT},
            background=True,
        )
        IDS.write_text(json.dumps({"construct": response.id}, indent=2) + "\n")
        print(f"submitted {MODEL} effort={EFFORT}: {response.id}", flush=True)
    while response.status in ("queued", "in_progress"):
        time.sleep(20)
        response = client.responses.retrieve(response.id)
        print(response.status, flush=True)
    out = HERE / "sol_construct.md"
    if response.status != "completed":
        details = getattr(response, "incomplete_details", None)
        partial = response.output_text or "(no partial model output returned)"
        out.write_text(
            f"# Sol construction attempt ({MODEL}, effort={EFFORT})\n\n"
            f"> INCOMPLETE, SINGLE-MODEL, UNREFEREED. Status: `{response.status}`. "
            f"Details: `{details}`. Nothing in this file is campaign evidence.\n\n"
            + partial
        )
        print(f"wrote incomplete {out} ({len(partial)} chars)")
        return
    out.write_text(
        f"# Sol construction attempt ({MODEL}, effort={EFFORT})\n\n"
        "> SINGLE-MODEL, UNREFEREED. No claim counts until independently checked.\n\n"
        + response.output_text
    )
    print(f"wrote {out} ({len(response.output_text)} chars)")


if __name__ == "__main__":
    main()
