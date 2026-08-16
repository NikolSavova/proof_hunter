#!/usr/bin/env python3
"""Stretchable fixed-x anneal for the rankwise near-maximal statistic.

At n=24, ell=5 and every convex four-face automatically has
u(A)<=20=4(4+1).  The dominant rankwise Hall term is therefore exactly
2*v_4/Z(1), which can be evaluated from the rank polynomial without
enumerating links after every coordinate move.  The final record is replayed
by ``rankwise_nearmax_audit.py`` to include all ranks.
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
sys.path[:0] = [str(HERE), str(GATE)]

import reflection_order_gate as gate  # noqa: E402
from search_acp_coordinates import coordinate_word  # noqa: E402


def score(ys: list[float]) -> tuple[float, list[int], tuple[int, ...]]:
    n = len(ys)
    word = coordinate_word(ys)
    evaluation = gate.evaluate_word(n, word, graded=True)
    profile = [1] + list(evaluation.graded[1:])
    return 2.0 * profile[4] / sum(profile), profile, word


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed-file", type=Path, default=HERE / "planar_acp_record.json")
    parser.add_argument("--steps", type=int, default=30_000)
    parser.add_argument("--seed", type=int, default=838)
    parser.add_argument("--temperature", type=float, default=0.002)
    parser.add_argument("--output", type=Path, default=Path("/tmp/rnp24.json"))
    args = parser.parse_args()

    data = json.loads(args.seed_file.read_text())
    if data["n"] != 24:
        raise ValueError("this exact proxy is specialized to n=24")
    source = data.get("y_coordinates", data.get("ys"))
    ys = list(map(float, source))
    rng = random.Random(args.seed)
    current, current_profile, current_word = score(ys)
    best = current, ys[:], current_profile, current_word
    print(f"start score={current:.12f}", flush=True)
    for step in range(args.steps):
        candidate = ys[:]
        point = rng.randrange(1, 23)
        sigma = 10 ** rng.uniform(-5.0, 0.0)
        candidate[point] += rng.gauss(0.0, sigma)
        try:
            value, profile, word = score(candidate)
        except ValueError:
            continue
        phase = (step % 10_000) / 9_999
        temperature = args.temperature * (1 - phase) + 1e-8
        difference = value - current
        if difference >= 0 or rng.random() < math.exp(difference / temperature):
            ys, current, current_profile, current_word = candidate, value, profile, word
        if current > best[0]:
            best = current, ys[:], current_profile, current_word
        if (step + 1) % 10_000 == 0:
            print(f"step={step+1} current={current:.12f} best={best[0]:.12f}", flush=True)

    output = {
        "n": 24,
        "objective_2v4_over_V": best[0],
        "ys": best[1],
        "profile": best[2],
        "word_zero_based": list(best[3]),
        "steps": args.steps,
        "seed": args.seed,
    }
    args.output.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({k: v for k, v in output.items() if k not in ("ys", "word_zero_based")}))


if __name__ == "__main__":
    main()
