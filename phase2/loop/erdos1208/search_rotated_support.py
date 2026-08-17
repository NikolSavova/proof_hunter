#!/usr/bin/env python3
"""Adversarial local search for the rotated-support conjecture in Erdős #1208.

For a lattice distance-Sidon set ``A`` and ``J(x,y)=(-y,x)``, the conjectural
full-resolution lemma is ``|A+JA-JA| >= |A|^(3-o(1))``.  Earlier experiments
sampled random greedy, perpendicular-ruler, and stretched-Costas families but
did not optimize the support itself.  This script performs deterministic-seed
simulated annealing over one-point replacements, subject to the exact
distance-Sidon constraint, and minimizes the *full* support (including the
``b=c`` triples).

The support counter is updated in O(k^2) time per accepted or rejected valid
move.  Every reported best witness is independently recomputed from scratch.
This is a falsification/search artifact, not evidence of the conjecture by
itself.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
import json
import math
import random
from typing import Callable, Iterable


Point = tuple[int, int]


def distance_squared(left: Point, right: Point) -> int:
    return (left[0] - right[0]) ** 2 + (left[1] - right[1]) ** 2


def is_distance_sidon(points: list[Point]) -> bool:
    distances = [
        distance_squared(points[i], points[j])
        for i in range(len(points))
        for j in range(i)
    ]
    return len(distances) == len(set(distances))


def phi(left: Point, middle: Point, right: Point) -> Point:
    """Return left + J(middle-right), where J(x,y)=(-y,x)."""
    return (
        left[0] - middle[1] + right[1],
        left[1] + middle[0] - right[0],
    )


def support_counter(points: list[Point]) -> Counter[Point]:
    return Counter(phi(a, b, c) for a in points for b in points for c in points)


def support_size(points: list[Point]) -> int:
    return len(support_counter(points))


def parallel_line_bound(points: list[Point]) -> tuple[int, int, Point]:
    """Return the best exact parallel-line lower bound and its diagnostics.

    For a primitive direction ``v``, let ``k_h`` be the occupancies of the
    lines parallel to ``v``, put ``Q=sum_h k_h(k_h-1)``, and let ``p`` be the
    number of distinct projections of ``A`` onto ``v``.  The restricted
    triples with ``b,c`` on a common parallel line give at least ``k+pQ``
    outputs.  The returned tuple is ``(best_bound, richest_line, direction)``.
    """
    k = len(points)
    directions: set[Point] = set()
    for i, (x, y) in enumerate(points):
        for u, v in points[:i]:
            dx, dy = x - u, y - v
            divisor = math.gcd(abs(dx), abs(dy))
            dx, dy = dx // divisor, dy // divisor
            if dx < 0 or (dx == 0 and dy < 0):
                dx, dy = -dx, -dy
            directions.add((dx, dy))

    best = k
    best_richness = 1
    best_direction = (1, 0)
    for dx, dy in directions:
        line_occupancies = Counter(dx * y - dy * x for x, y in points)
        projection_count = len({dx * x + dy * y for x, y in points})
        oriented_parallel_pairs = sum(size * (size - 1) for size in line_occupancies.values())
        bound = k + projection_count * oriented_parallel_pairs
        if bound > best:
            best = bound
            best_richness = max(line_occupancies.values())
            best_direction = (dx, dy)
    return best, best_richness, best_direction


def translate_collision_profile(points: list[Point]) -> tuple[int, int]:
    """Count parallel and transverse intersecting pairs of translate blocks."""
    differences = {
        (x - u, y - v)
        for x, y in points
        for u, v in points
    }
    labels = list(differences)
    parallel = transverse = 0
    for index, (x, y) in enumerate(labels):
        for u, v in labels[:index]:
            if (v - y, x - u) not in differences:
                continue
            if x * v - y * u == 0:
                parallel += 1
            else:
                transverse += 1
    return parallel, transverse


def greedy_seed(k: int, side: int, rng: random.Random) -> list[Point]:
    """Construct a random greedy distance-Sidon set of exactly ``k`` points."""
    universe = [(x, y) for x in range(side) for y in range(side)]
    for _ in range(500):
        rng.shuffle(universe)
        chosen: list[Point] = []
        used: set[int] = set()
        for point in universe:
            new_distances = [distance_squared(point, old) for old in chosen]
            if (
                len(new_distances) == len(set(new_distances))
                and used.isdisjoint(new_distances)
            ):
                chosen.append(point)
                used.update(new_distances)
                if len(chosen) == k:
                    return chosen
    raise RuntimeError(f"failed to build a {k}-point seed in a {side} by {side} box")


def mian_chowla(count: int) -> list[int]:
    """Return the first ``count`` marks of the greedy Golomb ruler."""
    marks = [0]
    differences: set[int] = set()
    candidate = 1
    while len(marks) < count:
        new_differences = [candidate - old for old in marks]
        if (
            len(new_differences) == len(set(new_differences))
            and differences.isdisjoint(new_differences)
        ):
            marks.append(candidate)
            differences.update(new_differences)
        candidate += 1
    return marks


def perpendicular_seed(k: int) -> list[Point]:
    """Build the two-arm Golomb-ruler stress family for even ``k``."""
    if k % 2:
        raise ValueError("the perpendicular seed requires even k")
    marks = mian_chowla(k)
    half = k // 2
    first, second = marks[:half], marks[half:]
    for offset in range(100_000):
        points = [(mark, 0) for mark in first] + [
            (0, offset + mark) for mark in second
        ]
        if is_distance_sidon(points):
            return points
    raise RuntimeError("failed to find a valid perpendicular-ruler offset")


def affected_triples(k: int) -> list[list[tuple[int, int, int]]]:
    """Precompute triples affected by replacing each point index."""
    answer: list[list[tuple[int, int, int]]] = []
    for index in range(k):
        triples = {
            (a, b, c)
            for a in range(k)
            for b in range(k)
            for c in range(k)
            if index in (a, b, c)
        }
        answer.append(sorted(triples))
    return answer


@dataclass
class SearchState:
    points: list[Point]

    def __post_init__(self) -> None:
        if not is_distance_sidon(self.points):
            raise ValueError("initial set is not distance-Sidon")
        self.point_set = set(self.points)
        self.distances = {
            distance_squared(self.points[i], self.points[j])
            for i in range(len(self.points))
            for j in range(i)
        }
        self.representations = support_counter(self.points)
        self.affected = affected_triples(len(self.points))

    @property
    def support(self) -> int:
        return len(self.representations)

    def _local_counter(self, index: int) -> Counter[Point]:
        return Counter(
            phi(self.points[a], self.points[b], self.points[c])
            for a, b, c in self.affected[index]
        )

    def propose_replacement(
        self, index: int, candidate: Point
    ) -> tuple[int, Callable[[], None]] | None:
        """Return ``(new_support, commit)`` for a valid replacement.

        The state is restored before returning; calling ``commit`` applies the
        already-evaluated move without recomputing its local counters.
        """
        old_point = self.points[index]
        if candidate == old_point or candidate in self.point_set:
            return None

        old_distances = {
            distance_squared(old_point, point)
            for j, point in enumerate(self.points)
            if j != index
        }
        remaining_distances = self.distances - old_distances
        new_distances = [
            distance_squared(candidate, point)
            for j, point in enumerate(self.points)
            if j != index
        ]
        if (
            len(new_distances) != len(set(new_distances))
            or not remaining_distances.isdisjoint(new_distances)
        ):
            return None

        old_local = self._local_counter(index)
        self.points[index] = candidate
        new_local = self._local_counter(index)
        self.points[index] = old_point

        changed_keys = old_local.keys() | new_local.keys()
        support_delta = 0
        for output in changed_keys:
            before = self.representations[output]
            after = before - old_local[output] + new_local[output]
            assert after >= 0
            support_delta += int(after > 0) - int(before > 0)
        new_support = self.support + support_delta

        def commit() -> None:
            for output, multiplicity in old_local.items():
                self.representations[output] -= multiplicity
                if self.representations[output] == 0:
                    del self.representations[output]
            self.points[index] = candidate
            for output, multiplicity in new_local.items():
                self.representations[output] += multiplicity
            self.point_set.remove(old_point)
            self.point_set.add(candidate)
            self.distances.difference_update(old_distances)
            self.distances.update(new_distances)
            assert self.support == new_support

        return new_support, commit


def candidate_point(
    state: SearchState,
    index: int,
    side: int,
    rng: random.Random,
) -> Point:
    old_x, old_y = state.points[index]
    choice = rng.random()
    if choice < 0.50:
        return rng.randrange(side), rng.randrange(side)
    if choice < 0.85:
        radius = max(1, side // 12)
        return (
            min(side - 1, max(0, old_x + rng.randint(-radius, radius))),
            min(side - 1, max(0, old_y + rng.randint(-radius, radius))),
        )
    donor_x, donor_y = rng.choice(state.points)
    return (donor_x, rng.randrange(side)) if rng.random() < 0.5 else (
        rng.randrange(side), donor_y
    )


def anneal(
    initial: list[Point],
    side: int,
    steps: int,
    seed: int,
) -> tuple[list[Point], int, dict[str, int]]:
    rng = random.Random(seed)
    state = SearchState(initial[:])
    best_points = state.points[:]
    best_support = state.support
    valid_moves = accepted_moves = improving_moves = 0
    initial_temperature = max(1.0, len(initial) ** 2 / 8)
    final_temperature = 0.05

    for step in range(steps):
        index = rng.randrange(len(initial))
        candidate = candidate_point(state, index, side, rng)
        proposal = state.propose_replacement(index, candidate)
        if proposal is None:
            continue
        valid_moves += 1
        new_support, commit = proposal
        fraction = step / max(1, steps - 1)
        temperature = initial_temperature * (
            final_temperature / initial_temperature
        ) ** fraction
        delta = new_support - state.support
        if delta <= 0 or rng.random() < math.exp(-delta / temperature):
            commit()
            accepted_moves += 1
            if delta < 0:
                improving_moves += 1
            if state.support < best_support:
                best_support = state.support
                best_points = state.points[:]

    assert is_distance_sidon(best_points)
    assert support_size(best_points) == best_support
    return best_points, best_support, {
        "valid": valid_moves,
        "accepted": accepted_moves,
        "improving": improving_moves,
    }


def normalized(points: Iterable[Point]) -> list[Point]:
    points = list(points)
    minimum_x = min(x for x, _ in points)
    minimum_y = min(y for _, y in points)
    return sorted((x - minimum_x, y - minimum_y) for x, y in points)


def parse_sizes(value: str) -> list[int]:
    return [int(item) for item in value.split(",") if item]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sizes", type=parse_sizes, default=[8, 12, 16, 20])
    parser.add_argument("--steps", type=int, default=20_000)
    parser.add_argument("--restarts", type=int, default=4)
    parser.add_argument("--side-factor", type=float, default=2.5)
    parser.add_argument("--seed", type=int, default=1208)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    records = []
    for k in args.sizes:
        side = max(k + 1, math.ceil(args.side_factor * k))
        best_points: list[Point] | None = None
        best_support = k**3 + 1
        baseline_supports: list[int] = []
        total_stats = Counter()

        seeds: list[list[Point]] = []
        if k % 2 == 0:
            ruler = perpendicular_seed(k)
            ruler_side = max(max(x for x, _ in ruler), max(y for _, y in ruler)) + 1
            baseline_supports.append(support_size(ruler))
            # The ruler box is much larger than the dense search box.  Retain it
            # as a measured adversarial baseline, but do not anneal across two
            # incomparable coordinate scales.
            del ruler_side
        for restart in range(args.restarts):
            rng = random.Random(args.seed + 10_000 * k + restart)
            seeds.append(greedy_seed(k, side, rng))

        for restart, initial in enumerate(seeds):
            initial_support = support_size(initial)
            baseline_supports.append(initial_support)
            points, support, stats = anneal(
                initial,
                side,
                args.steps,
                args.seed + 1_000_000 * k + restart,
            )
            total_stats.update(stats)
            if support < best_support:
                best_points, best_support = points, support

        assert best_points is not None
        record = {
            "k": k,
            "side": side,
            "baseline_min": min(baseline_supports),
            "best_support": best_support,
            "ratio": best_support / k**3,
            "points": normalized(best_points),
            "moves": dict(total_stats),
        }
        line_bound, richest_line, line_direction = parallel_line_bound(best_points)
        parallel_collisions, transverse_collisions = translate_collision_profile(best_points)
        record.update(
            {
                "parallel_line_bound": line_bound,
                "richest_line": richest_line,
                "line_direction": line_direction,
                "parallel_collisions": parallel_collisions,
                "transverse_collisions": transverse_collisions,
            }
        )
        records.append(record)
        if not args.json:
            print(
                f"k={k:2d} side={side:3d} baseline={record['baseline_min']:6d} "
                f"best={best_support:6d} ratio={record['ratio']:.6f} "
                f"valid={total_stats['valid']} accepted={total_stats['accepted']} "
                f"line-bound={line_bound} rich={richest_line} dir={line_direction} "
                f"Epar={parallel_collisions} Etrans/k^3={transverse_collisions/k**3:.6f}"
            )
            print("  points", record["points"])

    if args.json:
        print(json.dumps(records, indent=2))


if __name__ == "__main__":
    main()
