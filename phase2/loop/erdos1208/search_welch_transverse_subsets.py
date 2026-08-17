#!/usr/bin/env python3
"""Try to retain a large transverse overlap inside a Welch Costas set.

The full Welch set is vector-Sidon and has quadratic transverse local overlap,
but repeats Euclidean lengths.  This script fixes a popular difference ``d``
of the full set, selects a distance-Sidon subset containing the endpoints of
``d``, and anneals vertex swaps to maximize the number of retained local
solutions.  It is a direct falsification test for the local gate in
``TRANSVERSE_LOCAL_GATE.md``.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
import math
import random

from analyze_affine_costas_energy import is_distance_sidon, welch


Point = tuple[int, int]


def subtract(a: Point, b: Point) -> Point:
    return a[0] - b[0], a[1] - b[1]


def rotate(a: Point) -> Point:
    return -a[1], a[0]


def squared_norm(a: Point) -> int:
    return a[0] * a[0] + a[1] * a[1]


def full_difference_data(
    points: list[Point],
) -> tuple[dict[Point, tuple[int, int]], list[Point]]:
    edge = {
        subtract(points[i], points[j]): (i, j)
        for i in range(len(points))
        for j in range(len(points))
    }
    return edge, list(edge)


def local_solutions(
    points: list[Point], d: Point
) -> tuple[tuple[int, int], list[frozenset[int]]]:
    edge, differences = full_difference_data(points)
    if d not in edge:
        raise ValueError(f"{d=} is not a directed difference")
    fixed = edge[d]
    solutions: list[frozenset[int]] = []
    for e in differences:
        if e == (0, 0) or d[0] * e[0] + d[1] * e[1] == 0:
            continue
        je = rotate(e)
        f = d[0] - je[0], d[1] - je[1]
        if f in edge:
            solutions.append(frozenset(fixed + edge[e] + edge[f]))
    return fixed, solutions


def candidate_differences(
    points: list[Point], sample: int, rng: random.Random
) -> list[Point]:
    edge, differences = full_difference_data(points)
    nonzero = [d for d in differences if d != (0, 0)]
    shortest = sorted(nonzero, key=squared_norm)[:sample]
    if len(nonzero) <= sample:
        return shortest
    random_sample = rng.sample(nonzero, sample)
    # Preserve order while removing duplicates.
    return list(dict.fromkeys(shortest + random_sample))


def choose_popular_difference(
    points: list[Point], sample: int, rng: random.Random
) -> tuple[Point, int]:
    best_d = (0, 0)
    best_score = -1
    for d in candidate_differences(points, sample, rng):
        _, solutions = local_solutions(points, d)
        if len(solutions) > best_score:
            best_d, best_score = d, len(solutions)
    return best_d, best_score


def random_valid_subset(
    points: list[Point], fixed: tuple[int, int], target: int, rng: random.Random
) -> set[int] | None:
    selected = set(fixed)
    norms = {squared_norm(subtract(points[fixed[0]], points[fixed[1]]))}
    order = [i for i in range(len(points)) if i not in selected]
    rng.shuffle(order)
    for vertex in order:
        new_norms = [
            squared_norm(subtract(points[vertex], points[other]))
            for other in selected
        ]
        if len(new_norms) != len(set(new_norms)) or norms.intersection(new_norms):
            continue
        selected.add(vertex)
        norms.update(new_norms)
        if len(selected) == target:
            return selected
    return None


def retained_score(selected: set[int], solutions: list[frozenset[int]]) -> int:
    return sum(solution <= selected for solution in solutions)


def anneal(
    points: list[Point],
    fixed: tuple[int, int],
    solutions: list[frozenset[int]],
    target: int,
    steps: int,
    seed: int,
) -> tuple[set[int], int, dict[str, int]] | None:
    rng = random.Random(seed)
    selected = random_valid_subset(points, fixed, target, rng)
    if selected is None:
        return None

    norm_counts: dict[int, int] = defaultdict(int)
    for i in selected:
        for j in selected:
            if i < j:
                norm_counts[squared_norm(subtract(points[i], points[j]))] += 1
    assert max(norm_counts.values(), default=0) <= 1

    incident: list[list[int]] = [[] for _ in points]
    required = [len(solution) for solution in solutions]
    held = [0] * len(solutions)
    for index, solution in enumerate(solutions):
        for vertex in solution:
            incident[vertex].append(index)
        held[index] = len(solution & selected)

    score = sum(held[index] == required[index] for index in range(len(solutions)))
    best = set(selected)
    best_score = score
    fixed_set = set(fixed)
    accepted = valid = 0

    for step in range(steps):
        removable = tuple(selected - fixed_set)
        if not removable:
            break
        old = rng.choice(removable)
        new = rng.randrange(len(points))
        if new in selected:
            continue

        remaining = selected - {old}
        removed_norms = [
            squared_norm(subtract(points[old], points[other]))
            for other in remaining
        ]
        for norm in removed_norms:
            norm_counts[norm] -= 1
            if norm_counts[norm] == 0:
                del norm_counts[norm]

        new_norms = [
            squared_norm(subtract(points[new], points[other]))
            for other in remaining
        ]
        feasible = (
            len(new_norms) == len(set(new_norms))
            and not norm_counts.keys() & set(new_norms)
        )
        if not feasible:
            for norm in removed_norms:
                norm_counts[norm] += 1
            continue
        valid += 1

        changed = set(incident[old]) | set(incident[new])
        old_complete = sum(held[index] == required[index] for index in changed)
        for index in incident[old]:
            held[index] -= 1
        for index in incident[new]:
            held[index] += 1
        new_complete = sum(held[index] == required[index] for index in changed)
        trial_score = score - old_complete + new_complete

        fraction = step / max(1, steps - 1)
        temperature = 2.0 * (0.02 / 2.0) ** fraction
        delta = trial_score - score
        if delta >= 0 or rng.random() < math.exp(delta / temperature):
            selected.remove(old)
            selected.add(new)
            for norm in new_norms:
                norm_counts[norm] += 1
            score = trial_score
            accepted += 1
            if score > best_score:
                best, best_score = set(selected), score
        else:
            for index in incident[new]:
                held[index] -= 1
            for index in incident[old]:
                held[index] += 1
            for norm in removed_norms:
                norm_counts[norm] += 1

    answer = [points[index] for index in sorted(best)]
    assert len(answer) == target
    assert is_distance_sidon(answer)
    assert retained_score(best, solutions) == best_score
    return best, best_score, {"valid": valid, "accepted": accepted}


def parse_sizes(value: str) -> list[int]:
    return [int(item) for item in value.split(",") if item]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--primes", type=parse_sizes, default=[61, 101, 127])
    parser.add_argument("--targets", type=parse_sizes, default=[])
    parser.add_argument("--difference-sample", type=int, default=300)
    parser.add_argument("--steps", type=int, default=20_000)
    parser.add_argument("--restarts", type=int, default=4)
    parser.add_argument("--seed", type=int, default=1208)
    args = parser.parse_args()

    for prime_index, prime in enumerate(args.primes):
        points = welch(prime)
        rng = random.Random(args.seed + prime)
        d, full_score = choose_popular_difference(
            points, args.difference_sample, rng
        )
        fixed, solutions = local_solutions(points, d)
        targets = args.targets or [max(4, round(len(points) ** (2 / 3)))]
        print(
            f"p={prime} N={len(points)} d={d} full_local={full_score} "
            f"fixed={fixed}"
        )
        for target in targets:
            best_result = None
            for restart in range(args.restarts):
                result = anneal(
                    points,
                    fixed,
                    solutions,
                    target,
                    args.steps,
                    args.seed + 100_003 * prime_index + restart,
                )
                if result is None:
                    continue
                if best_result is None or result[1] > best_result[1]:
                    best_result = result
            if best_result is None:
                print(f"  k={target}: no valid seed")
                continue
            selected, score, stats = best_result
            subset = [points[index] for index in sorted(selected)]
            print(
                f"  k={target} retained={score} ratio={score/target:.6f} "
                f"valid={stats['valid']} accepted={stats['accepted']}"
            )
            print("   indices", sorted(selected))
            print("   points", subset)


if __name__ == "__main__":
    main()
