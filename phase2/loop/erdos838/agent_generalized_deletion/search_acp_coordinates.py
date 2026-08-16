#!/usr/bin/env python3
"""Stretchable fixed-x coordinate anneal for the ACP functional."""

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


def coordinate_word(ys: list[float]) -> tuple[int, ...]:
    n = len(ys)
    roots = sorted(
        ((ys[j] - ys[i]) / (j - i), i, j)
        for i in range(n)
        for j in range(i + 1, n)
    )
    return gate.word_from_roots(n, [(i, j) for _, i, j in roots])


def score(ys: list[float]) -> tuple[float, dict[str, float], tuple[int, ...]]:
    n = len(ys)
    word = coordinate_word(ys)
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
    }, word


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=24, choices=(20, 24, 30))
    parser.add_argument("--seed-file", type=Path)
    parser.add_argument("--steps", type=int, default=100_000)
    parser.add_argument("--seed", type=int, default=838)
    parser.add_argument("--temperature", type=float, default=0.006)
    parser.add_argument("--output", type=Path, default=Path("/tmp/acp_coordinates.json"))
    args = parser.parse_args()

    if args.seed_file:
        seed_data = json.loads(args.seed_file.read_text())
        if seed_data["n"] != args.n:
            raise ValueError("seed-file size differs from --n")
        ys = list(map(float, seed_data["ys"]))
    else:
        source = json.loads(
            (ROOT / "agent_dual_number_amortization" / "half_weight_search_records.json").read_text()
        )
        raw = source["exact_records"][str(args.n)][f"y_at_x_0_through_{args.n - 1}"]
        scale = max(map(abs, raw)) or 1
        ys = [float(y) / scale for y in raw]
        # Fix the vertical affine degrees of freedom without changing any
        # slope comparisons: subtract the line through the two endpoints.
        left, right = ys[0], ys[-1]
        ys = [
            y - left - (right - left) * x / (args.n - 1)
            for x, y in enumerate(ys)
        ]
    rng = random.Random(args.seed)
    current, current_stats, current_word = score(ys)
    best = (current, ys[:], current_stats, current_word)
    print(f"start score={current:.12g} stats={current_stats}", flush=True)

    for step in range(args.steps):
        candidate = ys[:]
        point = rng.randrange(1, args.n - 1)
        # Mixture of local and global moves crosses different order chambers.
        sigma = 10 ** rng.uniform(-4.0, 0.2)
        candidate[point] += rng.gauss(0.0, sigma)
        try:
            candidate_score, candidate_stats, candidate_word = score(candidate)
        except ValueError:
            continue
        phase = (step % 20_000) / 19_999
        temperature = args.temperature * (1 - phase) + 0.000001
        difference = candidate_score - current
        if difference >= 0 or rng.random() < math.exp(difference / temperature):
            ys = candidate
            current, current_stats, current_word = (
                candidate_score,
                candidate_stats,
                candidate_word,
            )
        if current > best[0]:
            best = current, ys[:], current_stats, current_word
        if (step + 1) % 20_000 == 0:
            print(
                f"step={step+1} current={current:.12g} best={best[0]:.12g}",
                flush=True,
            )

    result = {
        "n": args.n,
        "score": best[0],
        "stats": best[2],
        "ys": best[1],
        "word_zero_based": list(best[3]),
        "steps": args.steps,
        "seed": args.seed,
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k not in ("ys", "word_zero_based")}))


if __name__ == "__main__":
    main()
