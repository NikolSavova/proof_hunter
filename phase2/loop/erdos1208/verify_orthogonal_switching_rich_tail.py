#!/usr/bin/env python3
"""Exact checks for ORTHOGONAL_SWITCHING_RICH_TAIL_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict

from verify_orthogonal_two_support_gate import difference_set
from verify_third_additive_energy_barrier import parabola, transform
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Gaussian = tuple[int, int]
Form = tuple[Gaussian, ...]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def rotate(point: Point) -> Point:
    return -point[1], point[0]


def linear(point: Point) -> Point:
    """Apply I+J, or multiplication by 1+i."""
    return point[0] - point[1], point[0] + point[1]


def norm(point: Point) -> int:
    return point[0] * point[0] + point[1] * point[1]


def is_distance_sidon(points: list[Point]) -> bool:
    values = [
        norm(subtract(points[i], points[j]))
        for i in range(len(points))
        for j in range(i)
    ]
    return len(values) == len(set(values))


def switching_profile(points: list[Point]) -> tuple[int, int, int, int]:
    """Return energy, image, maximum fibre, and switching second moment."""
    assert is_distance_sidon(points)
    differences = difference_set(points)
    representations: dict[Point, list[tuple[Point, Point]]] = defaultdict(list)
    for first in differences:
        for second in differences:
            representations[add(first, rotate(second))].append((first, second))

    fibres: Counter[tuple[int, Point, Point]] = Counter()
    energy = 0
    for pairs in representations.values():
        energy += len(pairs) * len(pairs)
        for first, second in pairs:
            for third, fourth in pairs:
                candidates = (
                    (norm(first), first[0], first[1], 0, 0, first),
                    (norm(second), second[0], second[1], 1, 0, second),
                    (norm(third), third[0], third[1], 0, 1, third),
                    (norm(fourth), fourth[0], fourth[1], 1, 1, fourth),
                )
                _, _, _, role, representation, selected = max(candidates)
                other_sum = (
                    add(third, fourth)
                    if representation == 0
                    else add(first, second)
                )
                fibres[role, selected, other_sum] += 1

    return energy, len(fibres), max(fibres.values()), sum(
        value * value for value in fibres.values()
    )


def verify_small_profiles() -> None:
    families = (
        ("closure-20", POINTS[:20], (1_735_609, 777_087, 25, 4_826_721)),
        (
            "parabola-31",
            transform(parabola(31)),
            (866_761, 866_761, 1, 866_761),
        ),
    )
    for name, points, expected in families:
        actual = switching_profile(points)
        assert actual == expected
        energy, image, maximum, moment = actual
        print(
            name,
            "energy", energy,
            "image", image,
            "average", energy / image,
            "maximum", maximum,
            "moment/energy", moment / energy,
        )


def concrete_quadratic_instance() -> tuple[list[Point], Point]:
    base = [
        (8616, -1225),
        (11171, 92),
        (10484, 97),
        (9642, 1079),
        (441, 444),
        (596, -776),
        (206, 1471),
        (-169, -1341),
    ]
    common = (10_047_804, 10_060_149)
    translation = (-5_701_128_840_458_471_915_810,
                   -198_100_141_253_716_133_533_119)
    segment_translation = (
        521_382_104_484_310_251_747_232_670_856_326_248,
        -1_188_031_046_822_481_430_910_859_261_515_051_614,
    )
    longest = (10_060_149, -10_047_804)
    left, right = base[:4], base[4:]
    first_copy = [
        add(translation, subtract(common, linear(point)))
        for point in left
    ]
    second_copy = [
        add(translation, tuple(-value for value in linear(point)))
        for point in right
    ]
    points = (
        base
        + first_copy
        + second_copy
        + [segment_translation, add(segment_translation, longest)]
    )
    return points, longest


def verify_quadratic_instance() -> None:
    points, longest = concrete_quadratic_instance()
    assert len(points) == 18
    assert is_distance_sidon(points)
    differences = difference_set(points)
    assert len(differences) == 307

    physical = []
    for first in differences:
        second = tuple(-value for value in first)
        fourth = subtract(rotate(longest), linear(first))
        if (
            fourth in differences
            and norm(longest) > max(norm(first), norm(second), norm(fourth))
            and add(longest, rotate(fourth)) == add(first, rotate(second))
        ):
            physical.append((first, fourth))

    assert len(physical) == 16
    assert 2 * len(physical) == 32
    print(
        "quadratic fibre",
        "points", len(points),
        "differences", len(differences),
        "physical", len(physical),
        "ordered", 2 * len(physical),
    )


def gaussian_multiply(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gaussian_conjugate(value: Gaussian) -> Gaussian:
    return value[0], -value[1]


def form_subtract(left: Form, right: Form) -> Form:
    return tuple(
        (a[0] - b[0], a[1] - b[1])
        for a, b in zip(left, right)
    )


def hermitian_signature(form: Form) -> tuple[int, ...]:
    """Coefficient signature of the real polynomial |form|^2."""
    signature: list[int] = []
    for value in form:
        signature.append(value[0] * value[0] + value[1] * value[1])
    for row in range(len(form)):
        for column in range(row + 1, len(form)):
            value = gaussian_multiply(
                form[row], gaussian_conjugate(form[column])
            )
            signature.extend(value)
    return tuple(signature)


def symbolic_points(side: int = 4) -> list[Form]:
    """Complex-linear coefficient forms for the generic construction."""
    # Variables: 2*side base points, c, T, W.
    variable_count = 2 * side + 3
    common_index = 2 * side
    translation_index = common_index + 1
    segment_index = common_index + 2

    def form(entries: dict[int, Gaussian]) -> Form:
        return tuple(entries.get(index, (0, 0)) for index in range(variable_count))

    points: list[Form] = []
    for index in range(2 * side):
        points.append(form({index: (1, 0)}))
    for index in range(side):
        points.append(form({
            index: (-1, -1),
            common_index: (1, 0),
            translation_index: (1, 0),
        }))
    for index in range(side, 2 * side):
        points.append(form({
            index: (-1, -1),
            translation_index: (1, 0),
        }))
    points.append(form({segment_index: (1, 0)}))
    points.append(form({
        common_index: (0, -1),
        segment_index: (1, 0),
    }))
    return points


def verify_symbolic_genericity() -> None:
    points = symbolic_points()
    signatures: dict[tuple[int, ...], tuple[int, int]] = {}
    for first in range(len(points)):
        for second in range(first):
            signature = hermitian_signature(
                form_subtract(points[first], points[second])
            )
            assert signature not in signatures, (
                signatures.get(signature), (first, second)
            )
            signatures[signature] = first, second
    assert len(points) == 18
    assert len(signatures) == 153
    print("symbolic side-four signatures", len(signatures))


def main() -> None:
    verify_small_profiles()
    verify_symbolic_genericity()
    verify_quadratic_instance()
    print("orthogonal switching rich-tail gate: PASS")


if __name__ == "__main__":
    main()
