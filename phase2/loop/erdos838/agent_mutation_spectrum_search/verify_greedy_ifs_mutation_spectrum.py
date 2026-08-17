#!/usr/bin/env python3
"""Exact cyclic-IFS stress for ordered-block mutation selection."""

from __future__ import annotations

import importlib.util
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
LEX = ERDOS / "agent_lex_minimizer_search"
sys.path.insert(0, str(ERDOS))
sys.path.insert(0, str(LEX))

import reflection_trace as rt  # noqa: E402
import triangular_ifs_probe as tp  # noqa: E402

CONTROL_PATH = HERE / "verify_mutation_spectrum_controls.py"
SPEC = importlib.util.spec_from_file_location("mutation_controls", CONTROL_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load mutation-spectrum controls")
controls = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(controls)

Point = tuple[Fraction, Fraction]


def cyclic_depth_three() -> list[Point]:
    data = json.loads((LEX / "exact_realizable_n9.json").read_text())
    points = sorted(tuple(map(Fraction, point)) for point in data["coordinates_as_stored"])
    groups = ((0, 1, 5), (2, 3, 4), (6, 7, 8))
    clusters = [[points[index] for index in group] for group in groups]
    macro = [tp.centroid(cluster) for cluster in clusters]
    maps, _ = tp.make_maps(
        macro,
        clusters,
        ((0, 1, 2), (2, 0, 1), (0, 2, 1)),
        Fraction(1),
    )
    answer = tp.expand(tp.expand(macro, maps), maps)
    assert len(answer) == 27 and rt.evaluate(sorted(answer))[2] == 22862
    return answer


def greedy_sequence() -> dict[int, list[Point]]:
    current = cyclic_depth_three()
    answer: dict[int, list[Point]] = {}
    while len(current) >= 10:
        answer[len(current)] = sorted(current)
        if len(current) == 10:
            break
        candidates = []
        for index in range(len(current)):
            child = sorted(current[:index] + current[index + 1 :])
            cap, cup, value, _ = rt.evaluate(child)
            candidates.append(((value, cap + cup, index), index))
        _, omitted = min(candidates)
        current = current[:omitted] + current[omitted + 1 :]
    return answer


def profile(points: list[Point], mask: int, cache: dict[int, tuple[int, int, int]]):
    if mask not in cache:
        subset = [points[index] for index in range(len(points)) if mask >> index & 1]
        cache[mask] = rt.evaluate(subset)[:3]
    return cache[mask]


def sparse_three_minimum(points: list[Point], maximum_moved: int):
    points = sorted(points)
    n = len(points)
    full = (1 << n) - 1
    cache: dict[int, tuple[int, int, int]] = {0: (0, 0, 0)}
    ambient = rt.evaluate(points)[2]
    best = ambient
    best_masks = None
    assignments = 0
    for moved in range(1, maximum_moved + 1):
        for outside in itertools.combinations(range(n), moved):
            outside_mask = sum(1 << index for index in outside)
            for choices in range(1 << moved):
                left = sum(
                    1 << outside[index]
                    for index in range(moved)
                    if choices >> index & 1
                )
                right = outside_mask ^ left
                middle = full ^ outside_mask
                f_left = profile(points, left, cache)
                f_middle = profile(points, middle, cache)
                f_right = profile(points, right, cache)
                value = (
                    f_left[2]
                    + f_middle[2]
                    + f_right[2]
                    + f_left[0] * f_middle[1]
                    + f_middle[0] * f_right[1]
                    + f_left[0] * f_right[1] * (1 + middle.bit_count())
                )
                assignments += 1
                if value < best:
                    best = value
                    best_masks = left, middle, right
    return best, best_masks, assignments, len(cache)


def normalize(points: list[Point], reflect: bool = False) -> list[Point]:
    if len(points) <= 1:
        return [(Fraction(0), Fraction(0)) for _ in points]
    points = sorted(points)
    xmin, xmax = points[0][0], points[-1][0]
    ymin = min(point[1] for point in points)
    ymax = max(point[1] for point in points)
    xscale = xmax - xmin
    yscale = max(ymax - ymin, Fraction(1))
    sign = -1 if reflect else 1
    return [
        ((x - xmin) / xscale, sign * (y - ymin) / yscale)
        for x, y in points
    ]


def horizontal_glue(left: list[Point], reflected_right: list[Point]) -> list[Point]:
    epsilon = Fraction(1, 10**9)
    return sorted(
        [(epsilon * x, epsilon * epsilon * y) for x, y in left]
        + [
            (1 + epsilon * x, 1 + epsilon * epsilon * y)
            for x, y in reflected_right
        ]
    )


def main() -> None:
    sequence = greedy_sequence()
    expected = {
        27: 22862, 26: 18336, 25: 14831, 24: 11924, 23: 9566,
        22: 7526, 21: 5976, 20: 4732, 19: 3688, 18: 2852,
        17: 2211, 16: 1676, 15: 1260, 14: 947, 13: 695,
        12: 504, 11: 358, 10: 248,
    }
    assert {n: rt.evaluate(points)[2] for n, points in sequence.items()} == expected

    exhaustive = {}
    for n in (10, 12, 14):
        row = controls.q_block_spectrum(sequence[n], 3)
        exhaustive[n] = (
            row["minimum_slack"], row["all_blocks_nonempty_minimum_slack"]
        )
    assert exhaustive == {10: (0, 18), 12: (0, 43), 14: (0, 98)}

    sparse = {}
    for n in (16, 18, 20):
        best, masks, assignments, cache_size = sparse_three_minimum(sequence[n], 4)
        sparse[n] = (best, masks, assignments, cache_size)
    assert sparse[16][0] == 1676 and sparse[16][1] is None
    assert sparse[18][0] == 2852 and sparse[18][1] is None
    assert sparse[20][0] == 4681
    masks = sparse[20][1]
    assert masks is not None
    assert tuple(mask.bit_count() for mask in masks) == (1, 19, 0)

    points20 = sequence[20]
    left = [points20[index] for index in range(20) if masks[0] >> index & 1]
    middle = [points20[index] for index in range(20) if masks[1] >> index & 1]
    assert masks[2] == 0
    mutated = horizontal_glue(normalize(left), normalize(middle, reflect=True))
    assert rt.evaluate(mutated)[:3] == (1765, 2142, 4681)
    post_best, post_masks, post_assignments, post_cache = sparse_three_minimum(mutated, 4)
    assert post_best == 4681 and post_masks is None

    print(
        "PASS: cyclic greedy values n=10..27; q3 exhaustive=%s; "
        "sparse n16/18/20=(%d,%d,%d); mutation=(1765,2142,4681); "
        "post-mutation sparse=%d; assignments=(%d,%d) caches=(%d,%d)"
        % (
            exhaustive,
            sparse[16][0], sparse[18][0], sparse[20][0], post_best,
            sparse[20][2], post_assignments, sparse[20][3], post_cache,
        )
    )


if __name__ == "__main__":
    main()
