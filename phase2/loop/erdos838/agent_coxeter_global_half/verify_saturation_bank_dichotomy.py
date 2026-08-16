#!/usr/bin/env python3
"""Exact checks for SATURATION_BANK_DICHOTOMY.md."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from itertools import combinations
from pathlib import Path


Q = Fraction
Root = tuple[int, int]
ALPHA = math.log2(1.5)
HERE = Path(__file__).resolve().parent
N58_CERTIFICATE = (
    HERE.parent / "agent_cyclic_stem_hw" / "reflection_counter" / "certificate.json"
)


def all_downsets(rank: int):
    """Yield all Boolean downsets on `rank` labelled coordinates."""
    number_subsets = 1 << rank
    closures = []
    for subset in range(number_subsets):
        closure = 0
        child = subset
        while True:
            closure |= 1 << child
            if child == 0:
                break
            child = (child - 1) & subset
        closures.append(closure)
    for family in range(1 << number_subsets):
        if family == 0:
            continue
        if all(
            not (family & (1 << subset))
            or family & closures[subset] == closures[subset]
            for subset in range(number_subsets)
        ):
            yield family


def audit_abstract_downsets() -> tuple[int, int]:
    checked = 0
    equality_cases = 0
    for ground_rank in range(5):
        for family in all_downsets(ground_rank):
            checked += 1
            members = [
                subset
                for subset in range(1 << ground_rank)
                if family & (1 << subset)
            ]
            size = len(members)
            maximum_rank = max(member.bit_count() for member in members)
            weighted = sum((Q(1, 2) ** member.bit_count() for member in members), Q(0))
            phi = Q(size, 1 << maximum_rank) - 1 + Q(3, 2) ** maximum_rank
            assert weighted >= phi

            defect = math.log2(float(weighted)) - ALPHA * math.log2(size)
            assert defect >= -1e-12
            active = 0
            for member in members:
                active |= member
            is_cube = family == sum(1 << child for child in range(1 << ground_rank) if child & ~active == 0)
            if abs(defect) < 1e-12:
                equality_cases += 1
                assert is_cube
            if is_cube:
                assert abs(defect) < 1e-12
    return checked, equality_cases


def sign_points(signs: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    """Integer realization of chi(i,j,k)=signs[i]."""
    n = len(signs) + 2
    magnitude = 4 * n + 1
    points = [
        (i, signs[i] * magnitude ** (n - i)) for i in range(n - 2)
    ]
    points.extend(((n - 2, 0), (n - 1, 0)))
    return tuple(points)


def orientation(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> int:
    determinant = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )
    return (determinant > 0) - (determinant < 0)


def slope(a: tuple[int, int], b: tuple[int, int]) -> Q:
    return Q(b[1] - a[1], b[0] - a[0])


def root_order(points: tuple[tuple[int, int], ...]) -> tuple[Root, ...]:
    n = len(points)
    decorated = sorted(
        (slope(points[i], points[j]), i, j)
        for i, j in combinations(range(n), 2)
    )
    assert len({item[0] for item in decorated}) == len(decorated)
    roots = tuple((i, j) for _, i, j in decorated)

    wires = list(range(n))
    for i, j in roots:
        left = wires.index(i)
        right = wires.index(j)
        assert abs(left - right) == 1
        generator = min(left, right)
        assert wires[generator] < wires[generator + 1]
        wires[generator], wires[generator + 1] = (
            wires[generator + 1],
            wires[generator],
        )
    assert wires == list(reversed(range(n)))
    return roots


def product(n: int, roots: tuple[Root, ...], activity: Q) -> list[list[Q]]:
    matrix = [[Q(int(i == j)) for j in range(n)] for i in range(n)]
    for i, j in roots:
        matrix[j] = [x + activity * y for x, y in zip(matrix[j], matrix[i])]
    return matrix


def rich_polynomial(distance: int, activity: Q, alternating: bool) -> Q:
    if alternating:
        exponents = ((step - 1) // 2 for step in range(1, distance))
    else:
        exponents = (0 for _ in range(1, distance))
    return activity + activity * activity * sum(
        ((1 + activity) ** exponent for exponent in exponents), Q(0)
    )


def temporal_supports(
    u: int, v: int, positions: dict[Root, int], forward: bool
) -> set[int]:
    """Enumerate path supports as bitmasks on the global labels."""
    supports = set()
    internal = tuple(range(u + 1, v))
    for choice in range(1 << len(internal)):
        vertices = [u] + [
            internal[index]
            for index in range(len(internal))
            if choice & (1 << index)
        ] + [v]
        times = [positions[(a, b)] for a, b in zip(vertices, vertices[1:])]
        temporal = all(
            (left < right) if forward else (left > right)
            for left, right in zip(times, times[1:])
        )
        if temporal:
            supports.add(choice)
    return supports


def check_sign_family(n: int, alternating: bool) -> dict[str, object]:
    signs = tuple((1 if i % 2 == 0 else -1) if alternating else (1 if i == 0 else -1) for i in range(n - 2))
    points = sign_points(signs)
    for i, j, k in combinations(range(n), 3):
        assert orientation(points[i], points[j], points[k]) == signs[i]
    roots = root_order(points)
    positions = {root: index for index, root in enumerate(roots)}

    one = product(n, roots, Q(1))
    reverse_one = product(n, tuple(reversed(roots)), Q(1))
    half = product(n, roots, Q(1, 2))
    reverse_half = product(n, tuple(reversed(roots)), Q(1, 2))

    maximum_defect = 0.0
    for i, j in combinations(range(n), 2):
        distance = j - i
        if alternating or i == 0:
            expected_one = rich_polynomial(distance, Q(1), alternating)
            expected_half = rich_polynomial(distance, Q(1, 2), alternating)
        else:
            # Every label after the exceptional positive label is negative,
            # so a negative-start rich family is a full Boolean cube.
            expected_one = Q(1) * (1 + Q(1)) ** (distance - 1)
            expected_half = Q(1, 2) * (1 + Q(1, 2)) ** (distance - 1)
        rich_forward = signs[i] > 0 if i < n - 2 else True
        if rich_forward:
            assert one[j][i] == expected_one
            assert reverse_one[j][i] == 1
            assert half[j][i] == expected_half
            assert reverse_half[j][i] == Q(1, 2)
        else:
            assert one[j][i] == 1
            assert reverse_one[j][i] == expected_one
            assert half[j][i] == Q(1, 2)
            assert reverse_half[j][i] == expected_half

        x = one[j][i] * reverse_one[j][i]
        four_g = 4 * half[j][i] * reverse_half[j][i]
        maximum_rank = (distance // 2) if alternating else (1 if i == 0 and distance > 1 else distance - 1)
        # In the nonalternating family, negative-start intervals are strict caps.
        if not alternating and i > 0:
            maximum_rank = distance - 1
        bank = 1 << maximum_rank
        assert four_g * bank >= x
        defect = math.log2(float(four_g)) - ALPHA * math.log2(int(x))
        assert defect >= -1e-12
        maximum_defect = max(maximum_defect, defect)

        if n <= 12:
            forward_supports = temporal_supports(i, j, positions, True)
            reverse_supports = temporal_supports(i, j, positions, False)
            assert len(forward_supports) == one[j][i]
            assert len(reverse_supports) == reverse_one[j][i]
            forward_rank = max(mask.bit_count() for mask in forward_supports)
            reverse_rank = max(mask.bit_count() for mask in reverse_supports)
            assert forward_rank + reverse_rank == maximum_rank
            forward_active = 0
            reverse_active = 0
            for mask in forward_supports:
                forward_active |= mask
            for mask in reverse_supports:
                reverse_active |= mask
            assert forward_active & reverse_active == 0
            assert forward_active | reverse_active == (1 << (distance - 1)) - 1

    return {
        "n": n,
        "word_length": len(roots),
        "maximum_defect": maximum_defect,
        "extreme_X": one[n - 1][0] * reverse_one[n - 1][0],
        "extreme_four_G": 4 * half[n - 1][0] * reverse_half[n - 1][0],
    }


def audit_closed_forms() -> None:
    for distance in range(2, 65):
        rich_one = rich_polynomial(distance, Q(1), True)
        twice_rich_half = 2 * rich_polynomial(distance, Q(1, 2), True)
        if distance % 2 == 0:
            m = distance // 2
            assert rich_one == 3 * 2 ** (m - 1) - 1
            assert twice_rich_half == Q(5, 2) * Q(3, 2) ** (m - 1) - 1
        else:
            m = (distance - 1) // 2
            assert rich_one == 2 ** (m + 1) - 1
            assert twice_rich_half == 2 * Q(3, 2) ** m - 1

    for n in range(4, 65):
        distance = n - 1
        d = n - 2
        assert rich_polynomial(distance, Q(1), False) == d + 1
        assert 2 * rich_polynomial(distance, Q(1, 2), False) == 1 + Q(d, 2)
        assert 2 * (1 + Q(d, 2)) == d + 2


def longest_temporal_ranks(
    n: int, positions: dict[Root, int], forward: bool
) -> dict[Root, int]:
    """Maximum internal-support rank in every endpoint cell."""
    ranks = {}
    for u in range(n - 1):
        # best[a,b] is the maximum number of edges in a temporal path from
        # u whose last edge is (a,b).
        best: dict[Root, int] = {}
        for b in range(u + 1, n):
            best[(u, b)] = 1
            for a in range(u + 1, b):
                candidates = [
                    best[(k, a)]
                    for k in range(u, a)
                    if (k, a) in best
                    and (
                        positions[(k, a)] < positions[(a, b)]
                        if forward
                        else positions[(k, a)] > positions[(a, b)]
                    )
                ]
                if candidates:
                    best[(a, b)] = 1 + max(candidates)
            ranks[(u, b)] = (
                max(best[(a, b)] for a in range(u, b) if (a, b) in best) - 1
            )
    return ranks


def n58_regression() -> dict[str, object]:
    saved = json.loads(N58_CERTIFICATE.read_text())["finite_braid_record"]
    n = int(saved["n"])
    wires = list(range(n))
    roots = []
    for generator in map(int, saved["word_zero_based"]):
        i, j = wires[generator : generator + 2]
        assert i < j
        roots.append((i, j))
        wires[generator], wires[generator + 1] = j, i
    assert wires == list(reversed(range(n)))
    root_tuple = tuple(roots)
    positions = {root: index for index, root in enumerate(root_tuple)}

    forward_rank = longest_temporal_ranks(n, positions, True)
    reverse_rank = longest_temporal_ranks(n, positions, False)
    forward_one = product(n, root_tuple, Q(1))
    reverse_one = product(n, tuple(reversed(root_tuple)), Q(1))
    forward_half = product(n, root_tuple, Q(1, 2))
    reverse_half = product(n, tuple(reversed(root_tuple)), Q(1, 2))

    total_bank = 0
    minimum_product_ratio = float("inf")
    maximum_bank_dimension = 0
    for u, v in combinations(range(n), 2):
        x = int(forward_one[v][u])
        y = int(reverse_one[v][u])
        r = forward_rank[(u, v)]
        s = reverse_rank[(u, v)]
        bank = 1 << (r + s)
        four_g = 4 * forward_half[v][u] * reverse_half[v][u]
        total_bank += bank
        maximum_bank_dimension = max(maximum_bank_dimension, r + s)

        assert four_g * bank >= x * y
        phi_x = Q(x, 1 << r) - 1 + Q(3, 2) ** r
        phi_y = Q(y, 1 << s) - 1 + Q(3, 2) ** s
        assert four_g >= phi_x * phi_y
        defect = math.log2(float(four_g)) - ALPHA * math.log2(x * y)
        assert defect >= -1e-10
        assert math.log2(bank) + defect >= (
            (1 - ALPHA) * math.log2(x * y) - 1e-10
        )
        minimum_product_ratio = min(
            minimum_product_ratio, float(four_g * bank / (x * y))
        )

    assert total_bank == 55221
    assert total_bank <= int(saved["F_one"]) - 1 - n
    assert maximum_bank_dimension == 8
    u, v = 0, 57
    assert (forward_rank[(u, v)], reverse_rank[(u, v)]) == (3, 1)
    assert forward_one[v][u] * reverse_one[v][u] == 1950
    assert 4 * forward_half[v][u] * reverse_half[v][u] == Q(1431, 4)
    return {
        "n": n,
        "total_bank": total_bank,
        "nontrivial_faces": int(saved["F_one"]) - 1 - n,
        "maximum_bank_dimension": maximum_bank_dimension,
        "minimum_product_ratio": minimum_product_ratio,
    }


def main() -> None:
    checked, equality_cases = audit_abstract_downsets()
    audit_closed_forms()

    # Small rows explicitly enumerate every temporal support; large rows replay
    # the exact transvection products and closed forms.
    check_sign_family(10, alternating=True)
    check_sign_family(10, alternating=False)
    alternating_rows = [check_sign_family(n, alternating=True) for n in (16, 32, 48)]
    exceptional_rows = [check_sign_family(n, alternating=False) for n in (16, 32, 48)]
    n58 = n58_regression()

    print("saturation--bank dichotomy: PASS")
    print(f"abstract downsets checked={checked} equality cubes={equality_cases}")
    for name, rows in (("alternating", alternating_rows), ("one-exception", exceptional_rows)):
        for row in rows:
            print(
                f"{name:13s} n={row['n']:2d} word_length={row['word_length']:4d} "
                f"extreme X={row['extreme_X']} 4G={row['extreme_four_G']} "
                f"max_defect={row['maximum_defect']:.6f}"
            )
    print(
        f"n58 total_bank={n58['total_bank']} / {n58['nontrivial_faces']} "
        f"max_dimension={n58['maximum_bank_dimension']} "
        f"min_product_ratio={n58['minimum_product_ratio']:.6f}"
    )


if __name__ == "__main__":
    main()
