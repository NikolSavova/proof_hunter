#!/usr/bin/env python3
"""Exact search and accounting for depth-varying vertical macro towers.

Every reported finite count uses Python integers.  Coordinates are integral,
and slope comparisons use exact ``Fraction`` arithmetic.  The scalar tower
recurrence is the exact vertical-composition recurrence, not an estimate.

A schedule ``r1,r2,...`` uses an independently searched rational macro of
size ``rt`` at level t and substitutes the preceding construction into every
macro point.  This is a growing-state class: neither the macro type nor its
size is required to repeat.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
import random
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence


HERE = Path(__file__).resolve().parent
GATE_PATH = HERE.parent / "agent_reflection_gate" / "reflection_order_gate.py"
SPEC = importlib.util.spec_from_file_location("reflection_order_gate_growing", GATE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"cannot load {GATE_PATH}")
gate = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = gate
SPEC.loader.exec_module(gate)

Point = tuple[int, int]
Profile = tuple[int, ...]


def orient(a: Point, b: Point, c: Point) -> int:
    value = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return (value > 0) - (value < 0)


def hull_size(points: Sequence[Point], indices: Sequence[int]) -> int:
    selected = sorted((points[i], i) for i in indices)
    if len(selected) <= 2:
        return len(selected)

    def half(items: Iterable[tuple[Point, int]]) -> list[tuple[Point, int]]:
        out: list[tuple[Point, int]] = []
        for item in items:
            while len(out) >= 2 and orient(out[-2][0], out[-1][0], item[0]) <= 0:
                out.pop()
            out.append(item)
        return out

    lower = half(selected)
    upper = half(reversed(selected))
    return len(lower[:-1] + upper[:-1])


def slope_roots(points: Sequence[Point]) -> tuple[tuple[int, int], ...]:
    if any(points[i][0] >= points[i + 1][0] for i in range(len(points) - 1)):
        raise ValueError("x coordinates must be strictly increasing")
    for i, j, k in itertools.combinations(range(len(points)), 3):
        if orient(points[i], points[j], points[k]) == 0:
            raise ValueError(f"collinear triple {i},{j},{k}")
    slopes = sorted(
        (
            Fraction(points[j][1] - points[i][1], points[j][0] - points[i][0]),
            i,
            j,
        )
        for i in range(len(points))
        for j in range(i + 1, len(points))
    )
    return tuple((i, j) for _, i, j in slopes)


def subset_profiles(points: Sequence[Point]) -> tuple[Profile, Profile, Profile]:
    """Return cap, cup, convex profiles, with exact exhaustive classification."""
    r = len(points)
    cap = [0] * (r + 1)
    cup = [0] * (r + 1)
    convex = [0] * (r + 1)
    for mask in range(1, 1 << r):
        indices = tuple(i for i in range(r) if mask >> i & 1)
        triples = tuple(itertools.combinations(indices, 3))
        cap[len(indices)] += all(orient(points[i], points[j], points[k]) < 0 for i, j, k in triples)
        cup[len(indices)] += all(orient(points[i], points[j], points[k]) > 0 for i, j, k in triples)
        convex[len(indices)] += hull_size(points, indices) == len(indices)
    return tuple(cap), tuple(cup), tuple(convex)


def chain_profile(n: int, roots: Sequence[tuple[int, int]]) -> Profile:
    """Recover the exact chain-size profile from the graded transvections."""
    matrices = gate._poly_product_matrix(n, roots)
    profile = [0] * (n + 1)
    profile[1] = n
    for terminal in range(n):
        for initial in range(terminal):
            for edges, count in enumerate(matrices[terminal][initial]):
                if count:
                    profile[edges + 1] += count
    return tuple(profile)


def polynomial_value(profile: Profile, n: int, shift: int) -> int:
    return sum(
        multiplicity * n ** (degree - shift)
        for degree, multiplicity in enumerate(profile)
        if degree >= shift
    )


@dataclass(frozen=True)
class Macro:
    points: tuple[Point, ...]
    roots: tuple[tuple[int, int], ...]
    caps: Profile
    cups: Profile
    convex: Profile
    trace: int
    first_moment: int

    @classmethod
    def from_points(cls, points: Sequence[Point]) -> "Macro":
        pts = tuple(points)
        roots = slope_roots(pts)
        evaluation = gate.evaluate_roots(len(pts), roots, graded=True)
        cups = chain_profile(len(pts), roots)
        caps = chain_profile(len(pts), tuple(reversed(roots)))
        convex = tuple(evaluation.graded or ()) + (0,) * (len(pts) + 1 - len(evaluation.graded or ()))
        if len(pts) <= 11:
            subset_caps, subset_cups, subset_convex = subset_profiles(pts)
            if (caps, cups, convex) != (subset_caps, subset_cups, subset_convex):
                raise AssertionError("subset census and graded path profiles disagree")
        if sum(convex) != evaluation.trace:
            raise AssertionError((sum(convex), evaluation.trace))
        if sum(k * value for k, value in enumerate(convex)) != evaluation.first_moment:
            raise AssertionError("graded first moment mismatch")
        graded = tuple(evaluation.graded or ()) + (0,) * (len(convex) - len(evaluation.graded or ()))
        if graded != convex:
            raise AssertionError("reflection-product graded profile mismatch")
        return cls(pts, roots, caps, cups, convex, evaluation.trace, evaluation.first_moment)

    @property
    def r(self) -> int:
        return len(self.points)

    @property
    def largest_cap(self) -> int:
        return max(i for i, count in enumerate(self.caps) if count)

    @property
    def largest_cup(self) -> int:
        return max(i for i, count in enumerate(self.cups) if count)

    def certificate(self) -> dict[str, object]:
        return {
            "r": self.r,
            "points": [list(point) for point in self.points],
            "root_order": [list(root) for root in self.roots],
            "cap_profile": list(self.caps),
            "cup_profile": list(self.cups),
            "convex_profile": list(self.convex),
            "largest_cap": self.largest_cap,
            "largest_cup": self.largest_cup,
            "trace": self.trace,
            "first_moment": self.first_moment,
        }


def compose_exact(macros: Sequence[Macro]) -> dict[str, object]:
    """Apply the exact scalar vertical recurrence to a macro schedule."""
    size = caps = cups = convex = 1
    records: list[dict[str, object]] = []
    sum_log_square = 0.0
    for level, macro in enumerate(macros, 1):
        old_size, old_caps, old_cups, old_convex = size, caps, cups, convex
        cap_multiplier = polynomial_value(macro.caps, old_size, 1)
        cup_multiplier = polynomial_value(macro.cups, old_size, 1)
        caps = old_caps * cap_multiplier
        cups = old_cups * cup_multiplier
        convex = (
            macro.r * old_convex
            + old_caps * old_cups * polynomial_value(macro.convex, old_size, 2)
        )
        size = old_size * macro.r
        log_size = math.log2(size)
        log_r = math.log2(macro.r)
        sum_log_square += log_r * log_r
        certified_floor = 0.5 * (log_size * log_size - sum_log_square)
        reward = macro.largest_cap + macro.largest_cup - 2
        assert macro.r <= 1 << reward
        assert cap_multiplier * cup_multiplier >= old_size**reward
        records.append(
            {
                "level": level,
                "macro_size": macro.r,
                "size": size,
                "caps": caps,
                "cups": cups,
                "convex": convex,
                "es_reward": reward,
                "es_exact_power_bound": 1 << reward,
                "cap_multiplier": cap_multiplier,
                "cup_multiplier": cup_multiplier,
                "cap_cup_multiplier_exact_floor": old_size**reward,
                "normalized": math.log2(convex) / (log_size * log_size),
                # This floor applies to log(C_d U_d), hence to W at the next
                # nontrivial level.  It is included as an audit of the proof's
                # telescoping identity, not as a floor for current W_d.
                "log2_cap_cup_product": math.log2(caps) + math.log2(cups),
                "telescoping_floor": certified_floor,
                "telescoping_slack": math.log2(caps) + math.log2(cups) - certified_floor,
            }
        )
    return {
        "levels": records,
        "final": records[-1] if records else {"size": 1, "caps": 1, "cups": 1, "convex": 1},
    }


def random_points(n: int, rng: random.Random, bound: int = 10**8) -> tuple[Point, ...]:
    while True:
        points = tuple((i, rng.randrange(-bound, bound + 1)) for i in range(n))
        try:
            slope_roots(points)
        except ValueError:
            continue
        return points


def point_trace(points: Sequence[Point]) -> int:
    return gate.evaluate_roots(len(points), slope_roots(points)).trace


def search_macro(n: int, trials: int, seed: int) -> Macro:
    """Coordinate evolution, retaining an exact stretchable trace record."""
    rng = random.Random(seed)
    current_points = random_points(n, rng)
    current_trace = point_trace(current_points)
    best_points, best_trace = current_points, current_trace
    for step in range(trials):
        # Periodic independent restart crosses order-type chambers that a
        # one-coordinate mutation may not reach on useful time scales.
        if step and step % max(50, trials // 8) == 0:
            candidate_points = random_points(n, rng)
        else:
            ys = [point[1] for point in current_points]
            changed = rng.randrange(n)
            if rng.random() < 0.7:
                ys[changed] = rng.randrange(-10**8, 10**8 + 1)
            else:
                ys[changed] += rng.randrange(-10**7, 10**7 + 1)
            candidate_points = tuple((i, y) for i, y in enumerate(ys))
        try:
            candidate_trace = point_trace(candidate_points)
        except ValueError:
            continue
        phase = (step % max(50, trials // 8)) / max(49, trials // 8 - 1)
        temperature = max(0.01, 0.2 * (1.0 - phase))
        delta = math.log(candidate_trace) - math.log(current_trace)
        if delta <= 0 or rng.random() < math.exp(-delta / temperature):
            current_points, current_trace = candidate_points, candidate_trace
        if candidate_trace < best_trace:
            best_points, best_trace = candidate_points, candidate_trace
    result = Macro.from_points(best_points)
    if result.trace != best_trace:
        raise AssertionError("record trace changed during certificate construction")
    return result


def schedule_sizes(text: str) -> list[int]:
    result = [int(item) for item in text.split(",") if item]
    if not result or any(value < 2 or value > 40 for value in result):
        raise ValueError("schedule sizes must lie in [2,40]")
    return result


def exact_log2_ratio(numerator: int, denominator: int) -> float:
    return math.log2(numerator) / (math.log2(denominator) ** 2)


def selftest() -> None:
    triangle = Macro.from_points(((0, 0), (1, 2), (2, 1)))
    assert triangle.caps == (0, 3, 3, 1)
    assert triangle.cups == (0, 3, 3, 0)
    assert triangle.convex == (0, 3, 3, 1)
    result = compose_exact([triangle, triangle])
    # Re-evaluate the second level from the exact first-level totals and the
    # macro polynomials, independently of ``compose_exact``'s loop state.
    expected_c = 7 * (3 + 3 * 3 + 3**2)
    expected_u = 6 * (3 + 3 * 3)
    expected_w = 3 * 7 + 7 * 6 * (3 + 3)
    final = result["final"]
    assert final["caps"] == expected_c
    assert final["cups"] == expected_u
    assert final["convex"] == expected_w
    print(json.dumps({"status": "PASS", "triangle_square": final}, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("selftest")
    search = sub.add_parser("search")
    search.add_argument("--schedule", default="5,6,8,10,12")
    search.add_argument("--trials", type=int, default=200)
    search.add_argument("--seed", type=int, default=838)
    search.add_argument("--output", type=Path)
    check = sub.add_parser("check")
    check.add_argument("certificate", type=Path)
    args = parser.parse_args()

    if args.command == "selftest":
        selftest()
        return
    if args.command == "search":
        sizes = schedule_sizes(args.schedule)
        library: dict[int, Macro] = {}
        for offset, size in enumerate(sorted(set(sizes))):
            library[size] = search_macro(size, args.trials, args.seed + 1009 * offset)
        macros = [library[size] for size in sizes]
        result = {
            "schema": "exact integral coordinates and integer vertical-composition counts",
            "schedule": sizes,
            "trials_per_distinct_size": args.trials,
            "seed": args.seed,
            "macros": {str(size): library[size].certificate() for size in sorted(library)},
            "tower": compose_exact(macros),
        }
        encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
        print(encoded, end="")
        if args.output is not None:
            args.output.write_text(encoded)
        return

    data = json.loads(args.certificate.read_text())
    macros: dict[int, Macro] = {}
    for key, value in data["macros"].items():
        macro = Macro.from_points(tuple(tuple(point) for point in value["points"]))
        if macro.certificate() != value:
            raise AssertionError(f"macro certificate mismatch at size {key}")
        macros[int(key)] = macro
    schedule = [int(value) for value in data["schedule"]]
    tower = compose_exact([macros[size] for size in schedule])
    if tower != data["tower"]:
        raise AssertionError("tower certificate mismatch")
    print(json.dumps({"status": "PASS", "schedule": schedule, "final": tower["final"]}, sort_keys=True))


if __name__ == "__main__":
    main()
