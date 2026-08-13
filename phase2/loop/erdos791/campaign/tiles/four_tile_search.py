#!/usr/bin/env python3
"""Search the reflected-diagonal four-tile certificate language for #791.

For t >= 2 use the elementary segments

    V = [0,t]
    H = {i*t       : 0 <= i < t}
    S = {i*(t+1)   : 0 <= i < t}
    T = {i*(t-1)   : 0 <= i <= t}.

Copies of T are allowed one of two bounded translations (phase 0 or phase 1).
The conservative, t-independent square predicate implemented here is

  I+J, I+K, I+L0,
  consecutive(J+K), consecutive(J+L0),
  phase-matched adjacent pairs in K+L0 and K+L1.

The last rule uses the exact lemma that, writing D=S+T and t even,

    D union (D+1) union (D+t^2) union (D+t^2+1)

contains [t^2,2t^2-1].  In fact only the placements D at macro q-1 and
D+1 at macro q are needed: their union contains square q.  Thus a phase-0
sum at q-1 and phase-1 sum at q certify square q (and, symmetrically, a
phase-1 sum at q-1 and phase-0 sum at q).  Phase-1 T copies are deliberately not
credited in V+T or H+T; those shifted shapes need additional local lemmas.

This is a deterministic simulated-annealing baseline, not an exhaustive
search.  It uses Python integers as bitsets so millions of candidates are
cheap to evaluate and every reported certificate can be checked independently
by ``four_tile_verify.py``.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import time
from pathlib import Path


KOHONEN = {
    "I": [0, 5, 112, 117, 122, 127, 132, 137],
    "J": list(range(10, 107, 6)),
    "K": [0, 1, 2, 3, 4, 224, 225, 226, 227, 228, 229, 367, 368, 369, 370, 371, 372],
    "L0": [],
    "L1": [],
}
NAMES = tuple(KOHONEN)


def sum_bits(left: set[int], right: set[int], limit: int) -> int:
    out = 0
    for a in left:
        for b in right:
            q = a + b
            if 0 <= q < limit:
                out |= 1 << q
    return out


def coverage_bits(placement: dict[str, set[int]], limit: int) -> int:
    I, J, K, L0, L1 = (placement[name] for name in NAMES)
    ij = sum_bits(I, J, limit)
    ik = sum_bits(I, K, limit)
    il = sum_bits(I, L0, limit)
    jk = sum_bits(J, K, limit)
    jl = sum_bits(J, L0, limit)
    kl0 = sum_bits(K, L0, limit)
    kl1 = sum_bits(K, L1, limit)
    return ij | ik | il | (jk & (jk << 1)) | (jl & (jl << 1)) | (
        (kl0 << 1) & kl1
    ) | ((kl1 << 1) & kl0)


def prefix_length(bits: int, limit: int) -> int:
    missing = (~bits) & ((1 << limit) - 1)
    return limit if not missing else (missing & -missing).bit_length() - 1


def score(placement: dict[str, set[int]], limit: int) -> tuple[int, int, int]:
    bits = coverage_bits(placement, limit)
    prefix = prefix_length(bits, limit)
    covered = bits.bit_count()
    # A smooth-ish term rewards filling early holes without making the known
    # 510-prefix seed impossible to leave temporarily.  Eight dyadic prefix
    # windows are cheap to compute and dominate late, irrelevant coverage.
    windows = 0
    width = limit
    weight = 1
    while width:
        windows += weight * (bits & ((1 << width) - 1)).bit_count()
        width //= 2
        weight *= 2
    scalar = 200 * prefix + 3 * windows + covered
    return scalar, prefix, covered


def clone(p: dict[str, set[int]]) -> dict[str, set[int]]:
    return {name: set(values) for name, values in p.items()}


def randomize_types(
    rng: random.Random,
    base: dict[str, set[int]],
    counts: dict[str, int],
    bound: int,
) -> dict[str, set[int]]:
    """Retain as much of a seed as counts allow, then fill random coordinates."""
    out: dict[str, set[int]] = {}
    for name in NAMES:
        values = list(base[name])
        rng.shuffle(values)
        chosen = set(values[: counts[name]])
        while len(chosen) < counts[name]:
            chosen.add(rng.randrange(bound + 1))
        out[name] = chosen
    return out


def propose(
    rng: random.Random,
    placement: dict[str, set[int]],
    bound: int,
    radius: int,
) -> tuple[str, int, int] | None:
    nonempty = [name for name in NAMES if placement[name]]
    name = rng.choice(nonempty)
    old = rng.choice(tuple(placement[name]))
    if rng.random() < 0.72:
        new = max(0, min(bound, old + rng.randint(-radius, radius)))
    else:
        new = rng.randrange(bound + 1)
    if new == old or new in placement[name]:
        return None
    return name, old, new


def anneal(
    rng: random.Random,
    initial: dict[str, set[int]],
    bound: int,
    limit: int,
    steps: int,
    radius: int,
) -> tuple[dict[str, set[int]], tuple[int, int, int], int]:
    current = clone(initial)
    current_score = score(current, limit)
    best = clone(current)
    best_score = current_score
    accepted = 0
    for step in range(steps):
        move = propose(rng, current, bound, radius)
        if move is None:
            continue
        name, old, new = move
        current[name].remove(old)
        current[name].add(new)
        candidate_score = score(current, limit)
        delta = candidate_score[0] - current_score[0]
        progress = step / max(1, steps - 1)
        temperature = 5000.0 * (0.01 ** progress) + 0.2
        if delta >= 0 or rng.random() < math.exp(delta / temperature):
            current_score = candidate_score
            accepted += 1
            if candidate_score > best_score:
                best, best_score = clone(current), candidate_score
        else:
            current[name].remove(new)
            current[name].add(old)
    return best, best_score, accepted


def parse_counts(raw: str) -> dict[str, int]:
    values = [int(x) for x in raw.split(",")]
    if len(values) != len(NAMES) or any(x < 0 for x in values):
        raise argparse.ArgumentTypeError("counts must be five nonnegative integers I,J,K,L0,L1")
    return dict(zip(NAMES, values))


def serializable(p: dict[str, set[int]]) -> dict[str, list[int]]:
    return {name: sorted(p[name]) for name in NAMES}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--counts", type=parse_counts, default=parse_counts("8,17,17,0,0"))
    parser.add_argument("--bound", type=int, default=600)
    parser.add_argument("--limit", type=int, default=620)
    parser.add_argument("--steps", type=int, default=250_000)
    parser.add_argument("--restarts", type=int, default=8)
    parser.add_argument("--radius", type=int, default=12)
    parser.add_argument("--seed", type=int, default=79104)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    started = time.monotonic()
    global_best: tuple[dict[str, set[int]], tuple[int, int, int]] | None = None
    total_accepted = 0
    for restart in range(args.restarts):
        initial = randomize_types(rng, {k: set(v) for k, v in KOHONEN.items()}, args.counts, args.bound)
        best, best_score, accepted = anneal(
            rng, initial, args.bound, args.limit, args.steps, args.radius
        )
        total_accepted += accepted
        if global_best is None or best_score > global_best[1]:
            global_best = (best, best_score)
        print(
            f"restart={restart + 1}/{args.restarts} prefix={best_score[1]} "
            f"covered={best_score[2]}/{args.limit} accepted={accepted}",
            flush=True,
        )
    assert global_best is not None
    placement, final_score = global_best
    ell = sum(args.counts.values())
    result = {
        "status": "FOUND_RECORD" if final_score[1] * 294 > 85 * ell * ell else "NO_RECORD",
        "scope": "Heuristic search in the conservative reflected-diagonal certificate language.",
        "seed": args.seed,
        "counts": args.counts,
        "ell": ell,
        "bound": args.bound,
        "limit": args.limit,
        "steps_per_restart": args.steps,
        "restarts": args.restarts,
        "accepted_moves": total_accepted,
        "wall_seconds": time.monotonic() - started,
        "score": final_score[0],
        "certified_prefix": final_score[1],
        "covered_in_window": final_score[2],
        "record_threshold": (85 * ell * ell) // 294 + 1,
        "placement": serializable(placement),
    }
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
