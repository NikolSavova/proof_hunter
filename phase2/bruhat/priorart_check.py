"""One-off targeted prior-art check for Brenti's Conjecture 2.11 (rank
log-concavity of Bruhat intervals in Weyl groups) before we commit the week.

Cross-examination pass (house rule: never trust a single model's read):
Claude's own web sweep found the frontier = A_n/D_n n<=5, B_4, B_5 long
intervals, F_4, dihedral; H_3 counterexample; conjecture open for Weyl groups.
This script asks gpt-5.5 + web to independently confirm or refute that.

Usage:  ../../problem-id/.venv/bin/python priorart_check.py
Writes: results/priorart_gpt55_<pid>.md  (new file per run; never overwrites)
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "problem-id"))
import common  # noqa: E402

PROMPT = """You are doing a rigorous prior-art search for a mathematics research project.

TARGET: Brenti's Conjecture 2.11 (from F. Brenti, "Some open problems on Coxeter groups
and unimodality", OPAC proceedings; restated as Problem #13 in the survey arXiv:2410.09897):
For every WEYL group W and u <= v in Bruhat order, the interval [u,v] is rank log-concave,
i.e. the sequence a_k = #{z in [u,v] : l(z)-l(u)=k} satisfies a_k^2 >= a_{k-1} a_{k+1}.

Search the literature (arXiv, journals, MathOverflow, preprints, 2000-2026) and answer:

1. STATUS: Is this conjecture still open as of mid-2026? Has anyone proved it, disproved
   it, or published a counterexample in any Weyl group?
2. VERIFICATION FRONTIER: Exactly which cases have been computationally verified, by whom,
   where published? (Our current understanding: A_n for n<=5, D_n for n<=5, B_n for n<=4,
   B_5 restricted to intervals of length >= 20, F_4, and dihedral groups — with an explicit
   H_3 counterexample showing it fails for non-crystallographic Coxeter groups. Confirm or
   correct this, with sources.)
3. RECENT WORK: Any 2024-2026 papers touching rank sequences / log-concavity of Bruhat
   intervals (e.g. the asymptotic Brunn-Minkowski work arXiv:2311.17980, anything newer)?
   Anyone who verified A_6, B_5 (short intervals), B_6, D_6, E_6, or announced such a
   computation (including blog posts, GitHub repos, conference talks)?
4. VALUE: If someone completed the verification for A_6/A_7, B_5/B_6, D_6 and E_6 (or found
   a counterexample), would that be a publishable contribution? Where do such computational
   verification notes usually land?

Be specific, cite URLs, and clearly separate confirmed facts from your uncertainty. If you
find NOTHING contradicting our understanding, say so explicitly."""


def main():
    model = os.environ.get("PA_MODEL", "gpt-5.5")
    client = common.openai_client()
    resp = client.responses.create(
        model=model,
        input=[{"role": "user", "content": PROMPT}],
        tools=[{"type": "web_search", "search_context_size": "high"}],
        reasoning={"effort": "high"},
    )
    text = resp.output_text
    usage = getattr(resp, "usage", None)
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, f"priorart_gpt55_{os.getpid()}.md")
    with open(out, "w") as f:
        f.write(f"# Prior-art check: Brenti Conj 2.11 — {model} + web, high effort\n\n")
        f.write(text)
        if usage:
            f.write(f"\n\n---\nusage: {usage}\n")
    print(text)
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
