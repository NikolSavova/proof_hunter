#!/usr/bin/env python3
"""Verify the height/equality stresses for the closed-fibre Q functional."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from math import comb, gcd
import sys

sys.path.insert(0, "phase2/loop/erdos1208")

from verify_colored_derivative_l2_correlation_gate import VALUES  # noqa: E402
from verify_transverse_closure_witness import POINTS  # noqa: E402


Point = tuple[int, int]
Direction = tuple[int, int]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def norm2(vector: Point) -> int:
    return vector[0] * vector[0] + vector[1] * vector[1]


def primitive_unoriented(vector: Point) -> tuple[Direction, int]:
    divisor = gcd(abs(vector[0]), abs(vector[1]))
    direction = vector[0] // divisor, vector[1] // divisor
    if direction[0] < 0 or (direction[0] == 0 and direction[1] < 0):
        direction = -direction[0], -direction[1]
    return direction, divisor


def vector_sidon(points: list[Point]) -> bool:
    seen: set[Point] = set()
    for first, left in enumerate(points):
        for second, right in enumerate(points):
            if first == second:
                continue
            vector = subtract(right, left)
            if vector in seen:
                return False
            seen.add(vector)
    return True


def distance_sidon(points: list[Point]) -> bool:
    labels = [
        norm2(subtract(right, left))
        for left, right in combinations(points, 2)
    ]
    return len(labels) == len(set(labels))


def ambient_side(points: list[Point]) -> int:
    return max(
        max(point[0] for point in points) - min(point[0] for point in points),
        max(point[1] for point in points) - min(point[1] for point in points),
    )


def closed_q_profile(
    points: list[Point],
) -> tuple[int, int, Counter[int], int, int]:
    """Return Q, pair energy P, dyadic Q profile, |W|, and max e_w."""
    differences: list[Point] = []
    contents: defaultdict[Direction, list[int]] = defaultdict(list)
    for first, left in enumerate(points):
        for right in points[first + 1 :]:
            vector = subtract(right, left)
            direction, content = primitive_unoriented(vector)
            contents[direction].append(content)
            differences.extend((vector, (-vector[0], -vector[1])))

    # The tested inputs are vector-Sidon, so contents really are sets T_w.
    assert all(len(row) == len(set(row)) for row in contents.values())

    q_profile: Counter[int] = Counter()
    pair_energy = 0
    for (first, second), direction_contents in contents.items():
        fibre_sizes = Counter(
            first * vector[1] - second * vector[0]
            for vector in differences
        )
        for residue, fibre_size in fibre_sizes.items():
            if residue == 0:
                continue
            pair_cap = comb(fibre_size, 2)
            pair_energy += pair_cap
            alpha = Counter(
                (content * abs(residue)).bit_length() - 1
                for content in direction_contents
            )
            for exponent, multiplicity in alpha.items():
                q_profile[1 << exponent] += min(
                    pair_cap, multiplicity * fibre_size
                )

    directed_size = len(differences)
    q_total = sum(q_profile.values())
    assert q_total <= directed_size * directed_size // 2
    return (
        q_total,
        pair_energy,
        q_profile,
        len(contents),
        max(map(len, contents.values())),
    )


def residue_parabola(prime: int) -> list[Point]:
    return [(value, value * value % prime) for value in range(prime)]


def lifted_residue_parabola(prime: int) -> list[Point]:
    return [
        (value + prime * (value * value % prime), value * value % prime)
        for value in range(prime)
    ]


def verify_modular_equality_model() -> dict[int, tuple[int, int, int]]:
    expected_q = {
        7: 488,
        11: 3_500,
        17: 19_956,
        23: 80_444,
        31: 268_650,
        43: 988_328,
    }
    output: dict[int, tuple[int, int, int]] = {}
    for prime, expected in expected_q.items():
        native = residue_parabola(prime)
        lifted = lifted_residue_parabola(prime)
        assert vector_sidon(native)
        assert distance_sidon(lifted)
        native_profile = closed_q_profile(native)
        lifted_profile = closed_q_profile(lifted)
        # The determinant-one shear preserves every closed fibre and band.
        assert native_profile[:3] == lifted_profile[:3]
        assert native_profile[0] == expected
        output[prime] = expected, native_profile[1], ambient_side(lifted)

    # The previous audit stopped its cutoff list at the largest clean band.
    # The full Q sum has one further nonempty band of mass eight.
    profile_43 = closed_q_profile(lifted_residue_parabola(43))[2]
    assert profile_43[2_048] == 8
    assert sum(profile_43.values()) == 988_328
    assert sum(value for cutoff, value in profile_43.items() if cutoff < 2_048) == 988_320
    return output


def least_nonsquare(prime: int) -> int:
    squares = {value * value % prime for value in range(prime)}
    return next(value for value in range(2, prime) if value not in squares)


def layered_vector_sidon(prime: int) -> list[Point]:
    """Encode {(t,t^2): t in F_{p^2}} into p horizontal layers."""
    nonsquare = least_nonsquare(prime)
    radix = 2 * prime
    points = []
    for first in range(prime):
        for second in range(prime):
            square_first = (first * first + nonsquare * second * second) % prime
            square_second = 2 * first * second % prime
            longitudinal = (
                first + radix * square_first + radix * radix * square_second
            )
            points.append((longitudinal, second))
    assert vector_sidon(points)
    return points


def dominance_euclideanize(points: list[Point], prime: int) -> list[Point]:
    multiplier = 3 * prime
    output = [
        (multiplier * first + second, second)
        for first, second in points
    ]
    assert distance_sidon(output)
    return output


def horizontal_q(points: list[Point]) -> tuple[int, int, int]:
    differences: list[Point] = []
    contents = []
    for first, left in enumerate(points):
        for right in points[first + 1 :]:
            vector = subtract(right, left)
            differences.extend((vector, (-vector[0], -vector[1])))
            if vector[1] == 0:
                contents.append(abs(vector[0]))
    assert len(contents) == len(set(contents))

    sizes = Counter(vector[1] for vector in differences)
    output = 0
    for residue, fibre_size in sizes.items():
        if residue == 0:
            continue
        cap = comb(fibre_size, 2)
        alpha = Counter(
            (content * abs(residue)).bit_length() - 1
            for content in contents
        )
        output += sum(
            min(cap, multiplicity * fibre_size)
            for multiplicity in alpha.values()
        )
    return output, len(contents), max(sizes.values())


def verify_layered_barrier() -> dict[int, tuple[int, int, int, int]]:
    expected = {
        3: (486, 378, 668),
        5: (24_800, 18_500, 6_663),
        7: (298_214, 217_462, 26_256),
        11: (7_914_368, 5_630_130, 165_138),
    }
    output = {}
    for prime, row in expected.items():
        base = layered_vector_sidon(prime)
        if prime >= 5:
            assert not distance_sidon(base)
            # In the a=0 slice, b=1->2 and b=p-1->p-2 are reflections.
            first = subtract(base[2], base[1])
            second = subtract(base[prime - 2], base[prime - 1])
            assert first[0] == second[0] and first[1] == -second[1]
            assert norm2(first) == norm2(second)
        lifted = dominance_euclideanize(base, prime)
        q_horizontal, edge_count, _maximum_fibre = horizontal_q(lifted)
        exact_lower = 2 * sum(
            comb(height * prime * prime, 2)
            for height in range(1, prime)
        )
        assert edge_count == prime * comb(prime, 2)
        assert (q_horizontal, exact_lower, ambient_side(lifted)) == row
        assert q_horizontal >= exact_lower
        output[prime] = (
            q_horizontal,
            exact_lower,
            ambient_side(lifted),
            len(lifted),
        )
    return output


def verify_stored_stresses() -> dict[str, tuple[int, int, int, int]]:
    expected = {
        "closure-20": (18_282, 17_760, 20, 75),
        "closure-40": (225_150, 205_062, 40, 223),
        "closure-60": (896_292, 787_498, 60, 447),
        "integer-parabola-40": (630_172, 193_968, 40, 1_521),
        "multi-arc-24": (15_082, 12_804, 24, 1_207_274),
    }
    families = {
        "closure-20": POINTS[:20],
        "closure-40": POINTS[:40],
        "closure-60": POINTS[:60],
        "integer-parabola-40": [(value, value * value) for value in range(40)],
        "multi-arc-24": list(enumerate(VALUES)),
    }
    for name, points in families.items():
        assert distance_sidon(points)
        profile = closed_q_profile(points)
        actual = profile[0], profile[1], len(points), ambient_side(points)
        assert actual == expected[name]
    return expected


def verify_height_cap(points: list[Point]) -> None:
    assert distance_sidon(points)
    side = ambient_side(points)
    differences = [
        subtract(right, left)
        for first, left in enumerate(points)
        for second, right in enumerate(points)
        if first != second
    ]
    contents: defaultdict[Direction, set[int]] = defaultdict(set)
    for left, right in combinations(points, 2):
        direction, content = primitive_unoriented(subtract(right, left))
        contents[direction].add(content)
    for (first, second), row in contents.items():
        assert len(row) <= side // max(abs(first), abs(second))
        sizes = Counter(
            first * vector[1] - second * vector[0]
            for vector in differences
        )
        longitudinal_bound = side * (abs(first) + abs(second))
        for residue, size in sizes.items():
            if residue:
                assert size <= longitudinal_bound + 1


def main() -> None:
    modular = verify_modular_equality_model()
    layered = verify_layered_barrier()
    stresses = verify_stored_stresses()
    verify_height_cap(lifted_residue_parabola(23))
    verify_height_cap(POINTS[:40])
    print(
        "PASS",
        {
            "modular": modular,
            "layered": layered,
            "stresses": stresses,
            "corrected_p43_Q": 988_328,
            "high_height_subrange": "Q <= N^2/2 <= m^2/2 when m >= N",
        },
    )


if __name__ == "__main__":
    main()
