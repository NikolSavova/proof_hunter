#!/usr/bin/env python3
"""Exact adversarial checks for the mean-size route to Erdos 838.

The statistic is computed with the empty set included, as is natural for the
closed-set lattice.  Thus V=W+1, where W is the number of nonempty convex
subsets, and mu=Z'(1)/(W+1).  All counts and first moments are integers;
floating point is used only for the displayed logarithms.

The script has four independent lanes:

* exhaustive strong-glue states through a requested number of leaves;
* balanced Pascal cells T_(m,m/2), the exact counterfamily to QMS;
* exact rational Horton and nested-triangle configurations;
* replay of saved reduced-word certificates.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import asdict, dataclass
from fractions import Fraction
from pathlib import Path

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
GATE = ROOT / "agent_reflection_gate"
GRADED = ROOT / "agent_graded_supersat"
NESTED = ROOT / "agent_upper_multitype"
for path in (GATE, GRADED, NESTED):
    sys.path.insert(0, str(path))

from mean_size_probe import dyadic_horton, evaluate as evaluate_points  # noqa: E402
from nested_cage_search import nested_triangles  # noqa: E402
from reflection_order_gate import evaluate_word  # noqa: E402


@dataclass(frozen=True)
class State:
    n: int
    cap: int
    cup: int
    convex: int
    cap_moment: int
    cup_moment: int
    convex_moment: int


LEAF = State(1, 1, 1, 1, 1, 1, 1)


def glue(left: State, right: State) -> State:
    """Exact value/derivative recurrence for A prec B."""
    a, b = left.n, right.n
    return State(
        a + b,
        right.cap + (b + 1) * left.cap,
        left.cup + (a + 1) * right.cup,
        left.convex + right.convex + left.cap * right.cup,
        right.cap_moment
        + (b + 1) * left.cap_moment
        + b * left.cap,
        left.cup_moment
        + (a + 1) * right.cup_moment
        + a * right.cup,
        left.convex_moment
        + right.convex_moment
        + left.cap_moment * right.cup
        + left.cap * right.cup_moment,
    )


def metrics(n: int, convex: int, moment: int) -> dict[str, float | int]:
    closed_sets = convex + 1
    mean = moment / closed_sets
    return {
        "n": n,
        "closed_sets": closed_sets,
        "first_moment": moment,
        "mu": mean,
        "mu_minus_log2_n": mean - math.log2(n),
        "qms_ratio": math.log2(closed_sets) / (0.5 * mean * mean),
    }


def pascal_cells(max_m: int, selected: set[int]) -> list[dict[str, object]]:
    """Build the full Pascal row by exact strong-glue moment recurrences."""
    row = [LEAF]
    out: list[dict[str, object]] = []
    for m in range(1, max_m + 1):
        row = [LEAF] + [glue(row[i - 1], row[i]) for i in range(1, m)] + [LEAF]
        if m % 2 == 0 and m in selected:
            state = row[m // 2]
            item: dict[str, object] = {
                "family": f"T_({m},{m//2})",
                "state": asdict(state),
                **metrics(state.n, state.convex, state.convex_moment),
                "maximum_convex_size": m,
            }
            out.append(item)
    return out


def exhaustive_strong(nmax: int) -> list[dict[str, object]]:
    """Exhaust every distinct exact seven-coordinate state through nmax."""
    states: list[set[State]] = [set() for _ in range(nmax + 1)]
    states[1] = {LEAF}
    out = []
    for n in range(2, nmax + 1):
        current: set[State] = set()
        for a in range(1, n):
            for left in states[a]:
                for right in states[n - a]:
                    current.add(glue(left, right))
        states[n] = current
        minimum = min(
            current,
            key=lambda state: state.convex_moment / (state.convex + 1),
        )
        maximum_qms = max(
            current,
            key=lambda state: metrics(n, state.convex, state.convex_moment)[
                "qms_ratio"
            ],
        )
        out.append(
            {
                "n": n,
                "distinct_states": len(current),
                "minimum_mean_state": asdict(minimum),
                "minimum_mean_metrics": metrics(
                    n, minimum.convex, minimum.convex_moment
                ),
                "maximum_qms_state": asdict(maximum_qms),
                "maximum_qms_metrics": metrics(
                    n, maximum_qms.convex, maximum_qms.convex_moment
                ),
            }
        )
    return out


def generic_x(points: list[tuple[Fraction, Fraction]]) -> list[tuple[Fraction, Fraction]]:
    """Apply an exact determinant-one shear until all x-coordinates differ."""
    for shear in range(1, 10_000):
        transformed = [(x + shear * y, y) for x, y in points]
        if len({point[0] for point in transformed}) == len(points):
            return sorted(transformed)
    raise AssertionError("failed to find a generic rational shear")


def geometric_families() -> dict[str, list[dict[str, object]]]:
    horton = []
    for level in range(1, 9):
        points = dyadic_horton(level)
        value, moment, _ = evaluate_points(points)
        horton.append({"level": level, **metrics(len(points), value, moment)})

    cages = []
    for depth in (2, 3, 4, 6, 8, 10, 12):
        best: dict[str, object] | None = None
        # Includes the exact V=44 two-triangle certificate at seed 2844.
        for seed in range(838 + 1000 * depth, 838 + 1000 * depth + 8):
            cage_list = nested_triangles(depth, seed)
            raw = [point for cage in cage_list for point in cage]
            points = generic_x(raw)
            value, moment, _ = evaluate_points(points)
            item = {"depth": depth, "seed": seed, **metrics(len(points), value, moment)}
            if best is None or item["mu_minus_log2_n"] < best["mu_minus_log2_n"]:
                best = item
        assert best is not None
        cages.append(best)
    return {"horton": horton, "nested_triangles_minimum_of_8": cages}


def replay_reduced_words() -> list[dict[str, object]]:
    choices = {
        7: (GATE / "classes_n7.json", "minimum_mean_certificate"),
        8: (GATE / "heuristic_trace_n8.json", "certificate"),
        9: (GATE / "heuristic_trace_n9.json", "certificate"),
        10: (GRADED / "mean_heuristic_n10.json", "certificate"),
        12: (GRADED / "mean_heuristic_n12.json", "certificate"),
        16: (GRADED / "mean_heuristic_n16.json", "certificate"),
        20: (GRADED / "mean_heuristic_n20.json", "certificate"),
    }
    out = []
    for n, (path, key) in choices.items():
        data = json.loads(path.read_text())
        certificate = data[key]
        word = tuple(map(int, certificate["word_zero_based"]))
        evaluation = evaluate_word(n, word)
        claimed = certificate["evaluation"]
        for field in ("trace", "first_moment", "cup_total", "cap_total"):
            if evaluation.summary()[field] != claimed[field]:
                raise AssertionError(f"certificate replay failed: {path}, {field}")
        out.append(
            {
                "n": n,
                "source": str(path.relative_to(ROOT)),
                "fixed_x_rational_realization": certificate.get(
                    "fixed_x_rational_y"
                )
                is not None,
                "word_zero_based": list(word),
                **metrics(n, evaluation.trace, evaluation.first_moment),
            }
        )
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strong-n", type=int, default=13)
    parser.add_argument("--pascal-max-m", type=int, default=256)
    parser.add_argument("--output", type=Path, default=HERE / "certificate.json")
    args = parser.parse_args()
    selected = {4, 6, 8, 12, 20, 32, 48, 64, 96, 128, 192, 256}
    selected = {m for m in selected if m <= args.pascal_max_m}
    result = {
        "conventions": {
            "closed_sets": "empty set included",
            "mu": "Z'(1)/Z(1)",
            "logs": "base 2",
            "exactness": "all values and first moments exact integers",
        },
        "qms_counterfamily": pascal_cells(args.pascal_max_m, selected),
        "strong_glue_exhaustive": exhaustive_strong(args.strong_n),
        "geometric_families": geometric_families(),
        "reduced_word_replay": replay_reduced_words(),
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(f"wrote {args.output}")
    for item in result["qms_counterfamily"]:
        print(
            item["family"],
            f"log2n={math.log2(item['n']):.6f}",
            f"mu-log2n={item['mu_minus_log2_n']:+.6f}",
            f"QMS-ratio={item['qms_ratio']:.9f}",
        )


if __name__ == "__main__":
    main()
