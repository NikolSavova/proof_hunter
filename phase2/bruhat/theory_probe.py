"""Targeted prior-art + theory probe on the STRUCTURAL FINDINGS of the scaled
search (Sihao, 2026-07-03) — Erdosgate discipline applied to our own findings
before they enter the writeup.

Findings to vet (from scaled.py / scaled_general.py runs, all exact arithmetic):
  F1. In every exhaustively-checked simply-laced Weyl group (A3-A8, D4-D7 near-top
      slabs), the MIN log-concavity ratio min_k a_k^2/(a_{k-1}a_{k+1}) over all
      Bruhat intervals equals the min central ratio of the FULL Poincare
      polynomial, attained at [e,w0] (proper intervals tie but never beat it).
  F2. For type A this rank sequence is the Mahonian distribution (permutations
      by inversions), whose log-concavity is classical; its CLT variance
      sigma^2 = m(m-1)(2m+5)/72 predicts min ratio ~ 1 + 1/sigma^2, matching
      our data (A7: pred .0612 vs actual .05425; A8: .0435 vs .03894) — so the
      A-series decay is POLYNOMIAL (~36/m^3), not geometric, and never crosses 1.
  F3. Non-simply-laced groups have proper intervals achieving EXACTLY 1
      (the (1,2,2,2,1) dihedral-parabolic family, braid m>=4), a hard floor.

Usage:  ../../problem-id/.venv/bin/python theory_probe.py
Writes: results/theory_probe_gpt55_<pid>.md (new file per run; never overwrites)
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "problem-id"))
import common  # noqa: E402

PROMPT = """You are vetting research findings about Brenti's Conjecture 2.11 (rank
log-concavity of Bruhat intervals in Weyl groups: for u<=v, a_k = #{z in [u,v]:
l(z)-l(u)=k} satisfies a_k^2 >= a_{k-1}a_{k+1}). We verified the conjecture
exhaustively in new cases and are now studying WHERE the minimum of the
log-concavity ratio r = min_k a_k^2/(a_{k-1}a_{k+1}) is attained. Our empirical
findings, computed with exact integer arithmetic:

(F1) In every simply-laced Weyl group checked (A_n n<=8 fully or near-top,
D_n n<=7), the global minimum of r over ALL Bruhat intervals equals the minimum
central ratio of the full Poincare polynomial of W — i.e. it is attained at the
whole group [e, w_0]; proper intervals sometimes TIE but never go lower.

(F2) For type A_{m-1} the rank sequence of [e,w_0] is the Mahonian distribution
(#permutations of S_m by inversion number). Using its variance
sigma^2 = m(m-1)(2m+5)/72, the heuristic r ~ 1 + 1/sigma^2 matches our data well
(A7: predicted 0.0612 vs actual 0.05425; A8: 0.0435 vs 0.03894). So along this
family, r - 1 decays polynomially (~36/m^3) and never crosses 1.

(F3) In non-simply-laced groups (B/F/G) proper intervals achieve r = 1 EXACTLY,
always (in our data) as the rank sequence (1,2,2,2,1) coming from rank-2
parabolic/dihedral intervals with braid order m>=4.

Search the literature (arXiv, journals, MathOverflow, 2000-2026) and answer,
citing URLs and separating confirmed facts from uncertainty:

1. Is F1 KNOWN, conjectured, or contradicted anywhere? Any published statement
   comparing log-concavity "tightness" of proper Bruhat intervals vs the full
   group? (Check Bjorner-Ekedahl "On the shape of Bruhat intervals" and its
   citation trail — what exactly do they prove about lower-interval rank
   sequences, and does anything there imply or refute F1?)
2. What is the strongest PUBLISHED result on log-concavity of the Mahonian
   numbers / coefficients of the q-factorial [m]_q! (strict log-concavity,
   quantitative bounds on the ratio, asymptotics)? Does anyone state the
   1 + Theta(1/m^3) rate of F2? Key names to check: Hoggar products of
   log-concave polynomials, q-log-concavity (Butler, Sagan, Su), recent
   asymptotic/local-CLT work on inversion numbers.
3. Is the equality characterization F3 (only rank-(1,2,2,2,1) dihedral
   patterns give equality in Weyl groups) stated anywhere, e.g. in Brenti's
   original OPAC paper or follow-ups?
4. Given 1-3: for a computational-verification note (new exhaustive cases
   A6-A7, B5-B6, D6-D7, E6 + these structural sections), which of F1/F2/F3
   would referees consider NEW, and which are folklore/known? Any specific
   related theorems we must cite to avoid rediscovery claims?

If you find NOTHING contradicting a finding, say so explicitly."""


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
    out = os.path.join(outdir, f"theory_probe_gpt55_{os.getpid()}.md")
    with open(out, "w") as f:
        f.write(f"# Theory/prior-art probe: scaled-search findings — "
                f"{model} + web, high effort\n\n")
        f.write(text)
        if usage:
            f.write(f"\n\n---\nusage: {usage}\n")
    print(text)
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
