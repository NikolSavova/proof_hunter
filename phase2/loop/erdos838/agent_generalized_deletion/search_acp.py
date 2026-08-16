#!/usr/bin/env python3
"""Anneal the activity-compensated peak (ACP) functional.

This searches type-A reflection orders.  Such orders need not be stretchable,
so an output above one is only an oriented-matroid lead until rational planar
coordinates are supplied.  The objective is evaluated by dual-number matrix
products and never expands the rank polynomial.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
GATE = ROOT / "agent_reflection_gate"
EXTREME = ROOT / "agent_extreme_ra"
sys.path[:0] = [str(GATE), str(EXTREME)]

import reflection_order_gate as gate  # noqa: E402
from search_all_point_ra import value_moment  # noqa: E402


def score(n: int, word: tuple[int, ...]) -> tuple[float, dict[str, float]]:
    roots = gate.root_sequence(n, word)
    value, moment = value_moment(n, roots, 1.0)
    half, half_moment = value_moment(n, roots, 0.5)
    h_value = n * half / value
    mu_one = moment / value
    mu_half = half_moment / half
    delta = mu_one - mu_half
    acp = h_value * max(0.0, 1.0 - delta)
    return acp, {
        "H": h_value,
        "mu_one": mu_one,
        "mu_half": mu_half,
        "delta": delta,
        "ACP": acp,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("seed_file", type=Path)
    parser.add_argument("--steps", type=int, default=100_000)
    parser.add_argument("--seed", type=int, default=838)
    parser.add_argument("--temperature", type=float, default=0.004)
    parser.add_argument("--output", type=Path, default=Path("/tmp/acp_best.json"))
    args = parser.parse_args()

    data = json.loads(args.seed_file.read_text())
    n = data["n"]
    word = tuple(data["word_zero_based"])
    rng = random.Random(args.seed)
    current, current_stats = score(n, word)
    best_score, best_word, best_stats = current, word, current_stats
    evaluated = accepted = 0
    print(f"start n={n} score={current:.12g} stats={current_stats}", flush=True)

    for step in range(args.steps):
        commuting, braids = gate.coxeter_moves(word)
        if commuting and (not braids or rng.random() < 0.8):
            word = gate.apply_commutation(word, rng.choice(commuting))
            continue
        candidate_word = gate.apply_braid(word, rng.choice(braids))
        candidate, candidate_stats = score(n, candidate_word)
        evaluated += 1
        phase = (step % 20_000) / 19_999
        temperature = args.temperature * (1 - phase) + 0.000001
        difference = candidate - current
        if difference >= 0 or rng.random() < math.exp(difference / temperature):
            word, current, current_stats = candidate_word, candidate, candidate_stats
            accepted += 1
        if current > best_score:
            best_score, best_word, best_stats = current, word, current_stats
        if (step + 1) % 20_000 == 0:
            print(
                f"step={step+1} evaluated={evaluated} current={current:.12g} "
                f"best={best_score:.12g}",
                flush=True,
            )

    result = {
        "n": n,
        "score": best_score,
        "stats": best_stats,
        "word_zero_based": list(best_word),
        "steps": args.steps,
        "evaluated_braids": evaluated,
        "accepted_braids": accepted,
        "seed": args.seed,
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "word_zero_based"}))


if __name__ == "__main__":
    main()
