#!/usr/bin/env python3
"""Exact/sampled type-A reflection-order census for Erdős 838.

Reduced words for the longest permutation are generated as adjacent swaps of
an increasing pair.  The pair of labels swapped at each step is the associated
positive-root/reflection order.  Opposite transvection products give the exact
convex-subset trace.  Polynomial products additionally recover the size
profile and the mean convex-subset size.
"""

from __future__ import annotations

import argparse
import random
from dataclasses import dataclass
from math import log2


Root = tuple[int, int]


@dataclass(frozen=True)
class Record:
    convex: int
    endpoint_max: int
    profile: tuple[int, ...]
    roots: tuple[Root, ...]

    @property
    def mean_size(self) -> float:
        return sum(k * value for k, value in enumerate(self.profile)) / self.convex


def integer_product(n: int, roots: list[Root] | tuple[Root, ...]) -> list[list[int]]:
    matrix = [[int(i == j) for j in range(n)] for i in range(n)]
    for i, j in roots:
        for column in range(i + 1):
            matrix[j][column] += matrix[i][column]
    return matrix


def polynomial_product(
    n: int, roots: list[Root] | tuple[Root, ...]
) -> list[list[list[int]]]:
    matrix = [[[0] * (n + 1) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[i][i][0] = 1
    for i, j in roots:
        for column in range(i + 1):
            source = matrix[i][column]
            target = matrix[j][column]
            for degree in range(n):
                target[degree + 1] += source[degree]
    return matrix


def evaluate(n: int, roots: list[Root] | tuple[Root, ...], graded: bool = True) -> Record:
    cups = integer_product(n, roots)
    caps = integer_product(n, tuple(reversed(roots)))
    convex = sum(
        cups[row][column] * caps[row][column]
        for row in range(n)
        for column in range(row + 1)
    )
    endpoint_max = max(
        [1]
        + [
            cups[row][column] * caps[row][column]
            for row in range(n)
            for column in range(row)
        ]
    )
    if not graded:
        profile = ()
    else:
        cup_poly = polynomial_product(n, roots)
        cap_poly = polynomial_product(n, tuple(reversed(roots)))
        values = [0] * (n + 1)
        values[1] = n
        for row in range(n):
            for column in range(row):
                for cup_degree, cup_count in enumerate(cup_poly[row][column]):
                    if not cup_count:
                        continue
                    for cap_degree, cap_count in enumerate(cap_poly[row][column]):
                        degree = cup_degree + cap_degree
                        if degree <= n:
                            values[degree] += cup_count * cap_count
        if sum(values) != convex:
            raise AssertionError((sum(values), convex))
        profile = tuple(values)
    return Record(convex, endpoint_max, profile, tuple(roots))


def exhaustive(n: int) -> tuple[int, Record, Record]:
    permutation = list(range(n))
    roots: list[Root] = []
    target = n * (n - 1) // 2
    count = 0
    best_trace: Record | None = None
    best_mean: Record | None = None

    def visit(inversions: int) -> None:
        nonlocal count, best_trace, best_mean
        if inversions == target:
            count += 1
            record = evaluate(n, roots)
            if best_trace is None or (record.convex, record.endpoint_max) < (
                best_trace.convex,
                best_trace.endpoint_max,
            ):
                best_trace = record
            if best_mean is None or record.mean_size < best_mean.mean_size:
                best_mean = record
            return
        for position in range(n - 1):
            if permutation[position] < permutation[position + 1]:
                left, right = permutation[position], permutation[position + 1]
                permutation[position], permutation[position + 1] = right, left
                roots.append((left, right))
                visit(inversions + 1)
                roots.pop()
                permutation[position], permutation[position + 1] = left, right

    visit(0)
    assert best_trace is not None and best_mean is not None
    return count, best_trace, best_mean


def random_root_order(n: int, rng: random.Random) -> tuple[Root, ...]:
    permutation = list(range(n))
    roots: list[Root] = []
    while True:
        choices = [i for i in range(n - 1) if permutation[i] < permutation[i + 1]]
        if not choices:
            return tuple(roots)
        position = rng.choice(choices)
        left, right = permutation[position], permutation[position + 1]
        permutation[position], permutation[position + 1] = right, left
        roots.append((left, right))


def sample(n: int, samples: int, seed: int) -> tuple[Record, Record]:
    rng = random.Random(seed)
    best_trace: Record | None = None
    best_mean: Record | None = None
    for _ in range(samples):
        roots = random_root_order(n, rng)
        record = evaluate(n, roots)
        if best_trace is None or (record.convex, record.endpoint_max) < (
            best_trace.convex,
            best_trace.endpoint_max,
        ):
            best_trace = record
        if best_mean is None or record.mean_size < best_mean.mean_size:
            best_mean = record
    assert best_trace is not None and best_mean is not None
    return best_trace, best_mean


def describe(n: int, label: str, record: Record) -> None:
    quadratic_ratio = log2(record.convex) / (0.5 * record.mean_size**2)
    print(
        f"n={n} {label}: V={record.convex} M={record.endpoint_max} "
        f"trace_rate={log2(record.convex) / log2(n) ** 2:.9f} "
        f"mean={record.mean_size:.9f} mean-logn={record.mean_size-log2(n):+.9f} "
        f"logV/(mean^2/2)={quadratic_ratio:.9f}"
    )
    print("  profile=", [(k, v) for k, v in enumerate(record.profile) if v])
    print("  roots=", record.roots)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--samples", type=int, default=0)
    parser.add_argument("--seed", type=int, default=838)
    args = parser.parse_args()
    if args.samples:
        best_trace, best_mean = sample(args.n, args.samples, args.seed)
        print(f"sampled {args.samples} reduced words")
    else:
        count, best_trace, best_mean = exhaustive(args.n)
        print(f"exhausted {count} reduced words")
    describe(args.n, "minimum trace", best_trace)
    describe(args.n, "minimum mean", best_mean)


if __name__ == "__main__":
    main()
