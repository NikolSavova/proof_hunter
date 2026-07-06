"""Blind F2 proof draft from GPT-5.5-Pro (fallback gpt-5.5 on failure).

Sends F2_SPEC.md + the exact ground-truth table to the model, asks for a
complete draft proof per the spec's rules. Output: f2_drafts/draft_pro.md.

Usage:  ../../problem-id/.venv/bin/python f2_pro_draft.py
"""

import os
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "problem-id"))
import common  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    spec = open(os.path.join(HERE, "F2_SPEC.md")).read()
    table = subprocess.run(
        [sys.executable, os.path.join(HERE, "mahonian.py"), "--mmax", "40"],
        capture_output=True, text=True, check=True).stdout
    prompt = (
        "You are a research mathematician. Produce a COMPLETE draft proof of "
        "the theorem in the following spec, following its rules exactly "
        "(numbered lemmas, NUMERIC CHECK lines, honest GAP markers).\n\n"
        f"=== SPEC ===\n{spec}\n\n"
        f"=== EXACT GROUND TRUTH (mahonian.py --mmax 40) ===\n{table}\n"
        "Write the full draft now."
    )
    client = common.openai_client()
    for model in (os.environ.get("PA_MODEL", "gpt-5.5-pro"), "gpt-5.5"):
        try:
            resp = client.responses.create(
                model=model,
                input=[{"role": "user", "content": prompt}],
                reasoning={"effort": "high"},
            )
            text = resp.output_text
            if not text.strip():
                raise RuntimeError("empty response")
            break
        except Exception as e:  # TPM/availability fallback
            print(f"[{model} failed: {e}]", file=sys.stderr)
            text = None
    if text is None:
        sys.exit("both models failed")
    outdir = os.path.join(HERE, "f2_drafts")
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, "draft_pro.md")
    with open(out, "w") as f:
        f.write(f"# F2 blind draft — {model}, high effort\n\n" + text)
    print(f"wrote {out} ({len(text)} chars, model={model})")


if __name__ == "__main__":
    main()
