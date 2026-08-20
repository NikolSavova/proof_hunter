#!/usr/bin/env python3
"""Verify BALANCED_COSTAS_NEAR_SEPARATOR_LATTICE_AVERAGING_NO_GO.md."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import gcd, isqrt
import sys

sys.path.insert(0, "phase2/loop/erdos1208")

from analyze_affine_costas_energy import welch  # noqa: E402
from verify_balanced_costas_separator_exact_cutoff import (  # noqa: E402
    PRIME,
    WITNESS,
    canonical_edges,
    gram,
    is_separating,
    matrix_determinant,
)

Point = tuple[int, int]
Matrix = tuple[int, int, int, int]


def determinant(first: Point, second: Point) -> int:
    return first[0] * second[1] - first[1] * second[0]


def norm2(point: Point) -> int:
    return point[0] * point[0] + point[1] * point[1]


def canonical(point: Point) -> Point:
    negative = (-point[0], -point[1])
    return min(point, negative)


def apply(matrix: Matrix, point: Point) -> Point:
    a, b, c, d = matrix
    x, y = point
    return a * x + b * y, c * x + d * y


def lattice_line(point: Point, prime: int) -> tuple[int, int] | None:
    x, y = point[0] % prime, point[1] % prime
    if (x, y) == (0, 0):
        return None
    if x:
        return 1, y * pow(x, -1, prime) % prime
    return 0, 1


def lattice_memberships(point: Point, prime: int) -> set[tuple[int, int]]:
    line = lattice_line(point, prime)
    if line is None:
        return {(1, slope) for slope in range(prime)} | {(0, 1)}
    return {line}


def lattice_basis(line: tuple[int, int], prime: int) -> tuple[Point, Point]:
    if line == (0, 1):
        return (0, 1), (prime, 0)
    assert line[0] == 1
    slope = line[1]
    return (1, slope), (0, prime)


def gauss_reduce(first: Point, second: Point) -> tuple[Point, Point]:
    assert determinant(first, second) != 0
    while True:
        if norm2(second) < norm2(first):
            first, second = second, first
        quotient = round(
            (first[0] * second[0] + first[1] * second[1])
            / norm2(first)
        )
        candidate = (
            second[0] - quotient * first[0],
            second[1] - quotient * first[1],
        )
        if norm2(candidate) >= norm2(second):
            return first, second
        second = candidate


def basis_matrix(first: Point, second: Point) -> Matrix:
    matrix = (first[0], second[0], first[1], second[1])
    if matrix_determinant(matrix) < 0:
        matrix = (-first[0], second[0], -first[1], second[1])
    return matrix


def disk_vectors(radius: int) -> list[Point]:
    vectors: list[Point] = []
    for x in range(-radius, radius + 1):
        y_bound = isqrt(radius * radius - x * x)
        for y in range(-y_bound, y_bound + 1):
            if (x, y) != (0, 0):
                vectors.append((x, y))
    return vectors


def shell_energy(vectors: list[Point]) -> int:
    shells: Counter[int] = Counter()
    for vector in vectors:
        shells[norm2(vector)] += 1
    assert all(load % 2 == 0 for load in shells.values())
    return sum((load // 2) * (load // 2 - 1) // 2 for load in shells.values())


def verify_lattice_energy_identity(prime: int, radius: int) -> tuple[int, int]:
    lines = [(1, slope) for slope in range(prime)] + [(0, 1)]
    vectors = disk_vectors(radius)
    by_line = {
        line: [
            vector
            for vector in vectors
            if line in lattice_memberships(vector, prime)
        ]
        for line in lines
    }
    direct = sum(shell_energy(values) for values in by_line.values())

    representatives = sorted({canonical(vector) for vector in vectors})
    weighted = 0
    for first, second in combinations(representatives, 2):
        if norm2(first) != norm2(second):
            continue
        common = lattice_memberships(first, prime) & lattice_memberships(
            second, prime
        )
        weighted += len(common)

        first_mod = (first[0] % prime, first[1] % prime)
        if common and first_mod != (0, 0) and norm2(first) % prime:
            second_mod = (second[0] % prime, second[1] % prime)
            assert second_mod in {
                first_mod,
                ((-first_mod[0]) % prime, (-first_mod[1]) % prime),
            }
    assert direct == weighted
    return direct, min(shell_energy(values) for values in by_line.values())


def collision_hyperedges(points: list[Point]) -> set[frozenset[int]]:
    by_norm: dict[int, list[tuple[int, int]]] = {}
    for first, second in combinations(range(len(points)), 2):
        vector = (
            points[second][0] - points[first][0],
            points[second][1] - points[first][1],
        )
        by_norm.setdefault(norm2(vector), []).append((first, second))

    collisions: set[frozenset[int]] = set()
    for edges in by_norm.values():
        for first, second in combinations(edges, 2):
            support = frozenset(first + second)
            assert len(support) in (3, 4)
            collisions.add(support)
    return collisions


def greedy_delete(points: list[Point]) -> list[Point]:
    keep = set(range(len(points)))
    while True:
        induced = [points[index] for index in sorted(keep)]
        collisions = collision_hyperedges(induced)
        if not collisions:
            break
        support = next(iter(collisions))
        local_indices = sorted(keep)
        keep.remove(local_indices[next(iter(support))])
    return [points[index] for index in sorted(keep)]


def is_distance_sidon(points: list[Point]) -> bool:
    norms: set[int] = set()
    for first, second in combinations(points, 2):
        value = norm2(
            (
                second[0] - first[0],
                second[1] - first[1],
            )
        )
        if value in norms:
            return False
        norms.add(value)
    return True


def finite_near_separator(prime: int) -> tuple[int, int, int, Matrix]:
    base = welch(prime)
    edges = canonical_edges(base)
    lines = [(1, slope) for slope in range(prime)] + [(0, 1)]
    candidates: list[tuple[int, int, Matrix]] = []

    for line in lines:
        first, second = gauss_reduce(*lattice_basis(line, prime))
        matrix = basis_matrix(first, second)
        assert matrix_determinant(matrix) == prime
        for edge in edges:
            assert line in lattice_memberships(apply(matrix, edge), prime)
        transformed = [apply(matrix, point) for point in base]
        collision_count = sum(
            load * (load - 1) // 2
            for load in Counter(
                norm2(
                    (
                        transformed[second][0] - transformed[first][0],
                        transformed[second][1] - transformed[first][1],
                    )
                )
                for first, second in combinations(range(len(base)), 2)
            ).values()
        )
        candidates.append(
            (collision_count, max(map(abs, matrix)), matrix)
        )

    collision_count, height, matrix = min(candidates)
    transformed = [apply(matrix, point) for point in base]
    retained = greedy_delete(transformed)
    assert is_distance_sidon(retained)
    return collision_count, height, len(retained), matrix


def verify_gram_formulation() -> None:
    matrix = WITNESS
    assert matrix_determinant(matrix) == PRIME
    form = gram(matrix)
    assert form == (7_193, 4_627, 2_986)
    first, mixed, second = form
    assert first * second - mixed * mixed == PRIME * PRIME

    for x, y in canonical_edges(welch(PRIME)):
        value = first * x * x + 2 * mixed * x * y + second * y * y
        assert (
            second * value
            == (mixed * x + second * y) ** 2 + PRIME * PRIME * x * x
        )
        assert (
            first * value
            == (first * x + mixed * y) ** 2 + PRIME * PRIME * y * y
        )
    assert is_separating(form, canonical_edges(welch(PRIME)))


def main() -> None:
    energy_profiles = {
        (5, 18): verify_lattice_energy_identity(5, 18),
        (7, 28): verify_lattice_energy_identity(7, 28),
        (11, 45): verify_lattice_energy_identity(11, 45),
    }
    finite_profiles = {
        prime: finite_near_separator(prime) for prime in (11, 17, 23)
    }
    verify_gram_formulation()

    expected_energy = {
        (5, 18): (496, 52),
        (7, 28): (580, 54),
        (11, 45): (972, 52),
    }
    expected_finite = {
        11: (0, 3, 10, (1, 3, -3, 2)),
        17: (3, 4, 14, (2, -3, 3, 4)),
        23: (2, 5, 20, (-3, -5, 4, -1)),
    }
    assert energy_profiles == expected_energy
    assert finite_profiles == expected_finite

    print("balanced Costas near-separator lattice averaging: PASS")
    print("shell energy profiles:", energy_profiles)
    print("finite near-separators:", finite_profiles)
    print("p=263 witness Gram:", gram(WITNESS))


if __name__ == "__main__":
    main()
