#!/usr/bin/env python3
"""Exact audit of the fixed-edge insertion-chain universality lemma.

Every planar order type with distinct first coordinates is sent, by an
explicit affine/projective map, to the apexes of a strict chain of nested
triangles over one fixed base edge.  The map has positive denominator on
the relevant convex hull, so it preserves every convex-position subset.
"""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
APA = ERDOS / "agent_apa_rank"
GEOMETRY = ERDOS / "agent_geometry"
for directory in (APA, GEOMETRY):
    sys.path.insert(0, str(directory))

from audit_geometry import cell  # noqa: E402
from verify_apa_counterexample import matrix_profile, orient  # noqa: E402
from verify_half_weight_counterexample import (  # noqa: E402
    EXPECTED_PROFILE as PROFILE_58,
    points as points_58,
)


Point = tuple[Fraction, Fraction]


def sign(value: Fraction) -> int:
    assert value
    return 1 if value > 0 else -1


def strict_shear(points: tuple[Point, ...]) -> tuple[int, list[tuple[Point, Fraction, Fraction]]]:
    """Return M and sorted points carrying strictly decreasing positive L,R."""
    ordered = sorted(points)
    assert len({point[0] for point in ordered}) == len(ordered)
    required = [
        (ordered[i][1] - ordered[j][1]) / (ordered[j][0] - ordered[i][0])
        for i in range(len(ordered))
        for j in range(i + 1, len(ordered))
    ]
    maximum = max(required, default=Fraction(0))
    shear = max(1, maximum.numerator // maximum.denominator + 1)
    lifted = [(a, b, b + shear * a) for a, b in ordered]
    assert all(lifted[i][2] < lifted[i + 1][2] for i in range(len(lifted) - 1))

    c_shift = max(a for a, _, _ in lifted) + 1
    d_shift = max(c for _, _, c in lifted) + 1
    rows = [
        ((a, b), c_shift - a, d_shift - c)
        for a, b, c in lifted
    ]
    assert all(left > 0 and right > 0 for _, left, right in rows)
    assert all(
        rows[i][1] > rows[i + 1][1] and rows[i][2] > rows[i + 1][2]
        for i in range(len(rows) - 1)
    )
    return shear, rows


def choose_horizontal_shear(raw: list[Point], left_right: list[tuple[Fraction, Fraction]]) -> Fraction:
    """Avoid equal output x-coordinates without changing the nesting order."""
    forbidden: set[Fraction] = set()
    for i, j in combinations(range(len(raw)), 2):
        s_i, t_i = raw[i]
        s_j, t_j = raw[j]
        assert t_i != t_j
        forbidden.add((s_j - s_i) / (t_i - t_j))
    for exponent in range(2, 4 * len(raw) + 20):
        epsilon = Fraction(1, 2**exponent)
        if epsilon not in forbidden and all(
            left + epsilon > 0 and right - epsilon > 0
            for left, right in left_right
        ):
            return epsilon
    raise AssertionError("failed to choose the harmless horizontal shear")


def transform(points: tuple[Point, ...]) -> tuple[int, Fraction, list[Point], list[tuple[Fraction, Fraction]]]:
    """Map an order type into one strict insertion chain over (-1,0),(1,0)."""
    shear, rows = strict_shear(points)
    raw: list[Point] = []
    left_right: list[tuple[Fraction, Fraction]] = []
    for _, left, right in rows:
        raw.append(((left - right) / (left + right), Fraction(2, left + right)))
        left_right.append((left, right))
    epsilon = choose_horizontal_shear(raw, left_right)
    image = [(x + epsilon * y, y) for x, y in raw]
    shifted = [(left + epsilon, right - epsilon) for left, right in left_right]

    for point, (left, right) in zip(image, shifted):
        x, y = point
        assert (x + 1) / y == left
        assert (1 - x) / y == right
    assert len({point[0] for point in image}) == len(image)
    return shear, epsilon, image, shifted


def choose_lower_vertex(points: list[Point]) -> Point:
    """Choose a rational third base vertex avoiding every existing secant."""
    upper = [(Fraction(-1), Fraction(0)), (Fraction(1), Fraction(0))] + points
    denominator = 2 * len(upper) * len(upper) + 3
    for numerator in range(-len(upper) ** 2, len(upper) ** 2 + 1):
        candidate = (Fraction(numerator, denominator), Fraction(-1))
        if all(orient(candidate, a, b) for a, b in combinations(upper, 2)):
            return candidate
    raise AssertionError("failed to find a generic lower base vertex")


def digest(points: list[Point]) -> str:
    payload = "\n".join(f"{x.numerator}/{x.denominator},{y.numerator}/{y.denominator}" for x, y in points)
    return hashlib.sha256(payload.encode()).hexdigest()


def audit(name: str, points: tuple[Point, ...], expected_profile: tuple[int, ...] | None = None,
          expected_total: int | None = None) -> dict[str, object]:
    points = tuple(sorted(points))
    n = len(points)
    assert all(orient(points[i], points[j], points[k]) for i, j, k in combinations(range(n), 3))
    shear, epsilon, image, coordinates = transform(points)

    # The homogeneous matrix [L:R:1] -> [L-R+2e:2:L+R] has determinant -4.
    # The preliminary affine map has determinant +1, so every chirotope sign flips.
    for i, j, k in combinations(range(n), 3):
        assert sign(orient(image[i], image[j], image[k])) == -sign(
            orient(points[i], points[j], points[k])
        )

    # Strict triangle nesting.  The displayed alpha,beta,lambda are the
    # barycentric coefficients of image[i] in (-1,0),(1,0),image[j].
    minimum_coefficient: Fraction | None = None
    for i in range(n):
        left_i, right_i = coordinates[i]
        for j in range(i + 1, n):
            left_j, right_j = coordinates[j]
            height_i = image[i][1]
            alpha = height_i * (right_i - right_j) / 2
            beta = height_i * (left_i - left_j) / 2
            lam = height_i * (left_j + right_j) / 2
            assert alpha > 0 and beta > 0 and lam > 0
            assert alpha + beta + lam == 1
            minimum_coefficient = min(
                value for value in (minimum_coefficient, alpha, beta, lam)
                if value is not None
            )

    lower = choose_lower_vertex(image)
    base = [(Fraction(-1), Fraction(0)), (Fraction(1), Fraction(0)), lower]
    assert orient(base[0], base[1], base[2]) < 0
    ambient = base + image
    assert all(orient(ambient[i], ambient[j], ambient[k]) for i, j, k in combinations(range(n + 3), 3))

    original_profile = matrix_profile(points)
    image_profile = matrix_profile(tuple(image))
    assert image_profile == original_profile
    if expected_profile is not None:
        assert original_profile == expected_profile
    if expected_total is not None:
        assert sum(original_profile) == expected_total

    return {
        "family": name,
        "n": n,
        "input_general_position_triples": comb(n, 3),
        "ambient_general_position_triples": comb(n + 3, 3),
        "strict_nesting_relations": comb(n, 2),
        "affine_shear_M": shear,
        "final_horizontal_shear": str(epsilon),
        "minimum_strict_barycentric_coefficient": str(minimum_coefficient),
        "lower_base_vertex": [str(lower[0]), str(lower[1])],
        "transformed_coordinate_sha256": digest(image),
        "profile_including_empty": list(original_profile),
        "V": sum(original_profile),
    }


def hard_fixed_x_records() -> list[tuple[str, tuple[Point, ...], int]]:
    path = ERDOS / "agent_dual_number_amortization" / "half_weight_search_records.json"
    data = json.loads(path.read_text())["exact_records"]
    out = []
    for n in (20, 24, 30):
        row = data[str(n)]
        points = tuple(
            (Fraction(i), Fraction(value))
            for i, value in enumerate(row[f"y_at_x_0_through_{n - 1}"])
        )
        out.append((f"saved_half_weight_n{n}", points, int(row["V"])))
    return out


def trie_kraft(words: list[tuple[int, ...]]) -> tuple[int, int, int]:
    """Return root square, diagonal, and exact first-divergence release."""
    assert len(words) == len(set(words))
    assert all(
        not (len(first) < len(second) and second[:len(first)] == first)
        for first in words for second in words
    )
    prefix_counts: dict[tuple[int, ...], int] = {(): len(words)}
    children: dict[tuple[int, ...], set[tuple[int, ...]]] = {}
    leaves = set(words)
    for word in words:
        for depth in range(1, len(word) + 1):
            prefix = word[:depth]
            prefix_counts[prefix] = prefix_counts.get(prefix, 0) + 1
            parent = prefix[:-1]
            children.setdefault(parent, set()).add(prefix)
    release = 0
    for prefix, descendants in children.items():
        release += prefix_counts[prefix] ** 2
        release -= sum(prefix_counts[child] ** 2 for child in descendants)
    diagonal = sum(prefix_counts[word] ** 2 for word in leaves)
    assert diagonal == len(words)
    assert release + diagonal == len(words) ** 2
    return len(words) ** 2, diagonal, release


def prefix_kraft_audits() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for depth in (8, 32, 128):
        words = [(0,) * index + (1,) for index in range(depth)] + [(0,) * depth]
        square, diagonal, release = trie_kraft(words)
        rows.append({
            "family": f"nested_stop_chain_depth_{depth}",
            "records": len(words),
            "root_square": square,
            "diagonal": diagonal,
            "first_divergence_release": release,
        })

    words = [()]
    for size in (2, 3, 4, 2):
        words = [prefix + (letter,) for prefix in words for letter in range(size)]
    square, diagonal, release = trie_kraft(words)
    rows.append({
        "family": "product_2x3x4x2",
        "records": len(words),
        "root_square": square,
        "diagonal": diagonal,
        "first_divergence_release": release,
    })

    # Symbolic full-tree audit for the ramp--plateau alphabets.  It uses
    # only integer counts and therefore handles astronomically many leaves.
    for height in range(3, 8):
        width = 2**height
        exponents = (
            [2**index for index in range(height)]
            + [width] * (width // 2)
            + [2**index for index in reversed(range(height))]
        )
        alphabets = [2**exponent for exponent in exponents]
        total = 1
        for size in alphabets:
            total *= size
        prefixes = 1
        release = 0
        descendants = total
        for size in alphabets:
            child_descendants = descendants // size
            release += prefixes * (descendants**2 - size * child_descendants**2)
            prefixes *= size
            descendants = child_descendants
        assert descendants == 1 and prefixes == total
        assert release + total == total**2
        rows.append({
            "family": f"ramp_plateau_height_{height}",
            "levels": len(alphabets),
            "log2_records": sum(exponents),
            "identity_verified": True,
        })
    return rows


def main() -> None:
    central = tuple((point.x, point.y) for point in cell(6, 3))
    records = [audit("central_Pascal_T_6_3", central, expected_total=10_952)]
    for name, points, total in hard_fixed_x_records():
        records.append(audit(name, points, expected_total=total))
    records.append(audit("saved_half_weight_n58", points_58(), expected_profile=PROFILE_58))

    result = {
        "claim": (
            "Every audited order type is preserved, up to global orientation reversal, "
            "inside one strict fixed-edge insertion chain."
        ),
        "theorem_scope": "all finite planar order types after a generic affine shear",
        "records": records,
        "quadratic_prefix_kraft": prefix_kraft_audits(),
    }
    output = HERE / "insertion_chain_universality_certificate.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
