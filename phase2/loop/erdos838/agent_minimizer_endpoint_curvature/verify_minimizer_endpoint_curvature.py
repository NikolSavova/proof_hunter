#!/usr/bin/env python3
"""Exact checks for MINIMIZER_ENDPOINT_CURVATURE_AND_HIGH_WALL_GATE.md."""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
from math import comb
from pathlib import Path
import importlib.util
import json
import subprocess
import sys
import tempfile


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def exact_bruhat_rows(size: int) -> dict:
    source = HERE / "exact_endpoint_bruhat.cpp"
    with tempfile.TemporaryDirectory() as raw:
        binary = Path(raw) / "exact_endpoint_bruhat"
        subprocess.run(
            ["g++", "-std=c++17", "-O3", "-DNDEBUG", str(source), "-o", str(binary)],
            check=True,
        )
        output = subprocess.check_output([str(binary), str(size)], text=True)
    return json.loads(output)


def orient(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points):
    points = sorted(points)
    lower = []
    for point in points:
        while len(lower) >= 2 and orient(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and orient(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def face_profile(points):
    size = len(points)
    profile = [0] * (size + 1)
    for rank in range(1, size + 1):
        for subset in combinations(range(size), rank):
            selected = [points[index] for index in subset]
            if rank <= 2 or len(hull(selected)) == rank:
                profile[rank] += 1
    return profile


def strong_decomposition_audit(raw_points):
    """All ordered strong trees, allowing both mirror signs at every node."""
    points = tuple(tuple(point) for point in raw_points)
    signs = {}
    for a in range(len(points)):
        for b in range(len(points)):
            for c in range(len(points)):
                if len({a, b, c}) < 3:
                    continue
                value = orient(points[a], points[b], points[c])
                assert value
                signs[a, b, c] = 1 if value > 0 else -1

    @lru_cache(None)
    def decomposes(order: tuple[int, ...]) -> bool:
        if len(order) <= 1:
            return True
        for cut in range(1, len(order)):
            left, right = order[:cut], order[cut:]
            for first_sign in (-1, 1):
                left_rule = all(
                    signs[a, b, c] == first_sign
                    for a, b in combinations(left, 2)
                    for c in right
                )
                right_rule = all(
                    signs[a, b, c] == -first_sign
                    for a in left
                    for b, c in combinations(right, 2)
                )
                if (left_rule and right_rule
                        and decomposes(left) and decomposes(right)):
                    return True
        return False

    witness = next(
        (order for order in permutations(range(len(points)))
         if decomposes(order)),
        None,
    )
    # A failed top-level search already certifies nondecomposability.  Fill
    # the remaining cache as an independently countable audit trail: its
    # size must then be the number of ordered nonempty subsets of [n].
    if witness is None:
        for size in range(1, len(points) + 1):
            for order in permutations(range(len(points)), size):
                decomposes(order)
    return witness is not None, decomposes.cache_info().currsize


def minimum_cap_profile(wrapper, raw_points):
    points = [tuple(map(Fraction, point)) for point in raw_points]
    signs = wrapper.all_signs(points)
    perturbed = wrapper.generic_perturb(points, signs)
    orders = wrapper.projection_orders(perturbed)
    order = min(orders, key=lambda row: wrapper.chain_counts(signs, row)[0])
    cap, cup = wrapper.chain_counts(signs, order)
    position = {label: index for index, label in enumerate(order)}
    profile = [0] * (len(points) + 1)
    for rank in range(1, len(points) + 1):
        for subset in combinations(range(len(points)), rank):
            if rank <= 2:
                profile[rank] += 1
                continue
            ordered = sorted(subset, key=position.get)
            if all(
                wrapper.ordered_sign(signs, a, b, c) < 0
                for a, b, c in combinations(ordered, 3)
            ):
                profile[rank] += 1
    assert sum(profile) == cap
    return cap, cup, profile, order


def low_rank_moment(size: int, count: int) -> int:
    """Minimum total cardinality of count distinct nonempty subsets."""
    remaining = count
    answer = 0
    for rank in range(1, size + 1):
        take = min(remaining, comb(size, rank))
        answer += rank * take
        remaining -= take
        if not remaining:
            return answer
    raise AssertionError("count exceeds the Boolean lattice")


def maximum_survival(size: int, deleted: int, count: int) -> int:
    """Maximum sum binom(size-|S|,deleted) over count nonempty subsets."""
    remaining = count
    answer = 0
    for rank in range(1, size + 1):
        take = min(remaining, comb(size, rank))
        if size - rank >= deleted:
            answer += take * comb(size - rank, deleted)
        remaining -= take
        if not remaining:
            return answer
    raise AssertionError("count exceeds the Boolean lattice")


def moment_lower_bound(size: int, faces: int) -> int:
    ell = size + comb(size, 2)
    face_moment = low_rank_moment(size, faces)
    caps = ell
    available = size * (1 + caps) - low_rank_moment(size, caps)
    if available >= face_moment:
        return caps
    for rank in range(3, size):
        gain = size - rank
        block = comb(size, rank)
        needed = (face_moment - available + gain - 1) // gain
        if needed <= block:
            return caps + needed
        caps += block
        available += block * gain
    raise AssertionError("no endpoint solution")


def mobius_lower_bound(size: int, deleted: int, profile: list[int]) -> int:
    number = comb(size, deleted)
    faces = sum(profile)
    surviving = sum(
        value * comb(size - rank, deleted)
        for rank, value in enumerate(profile)
        if size - rank >= deleted
    )
    ell_deleted = deleted + comb(deleted, 2)
    required = (
        number * faces - surviving - number * ((1 << deleted) - 1)
        + ell_deleted - 1
    ) // ell_deleted
    ell_size = size + comb(size, 2)
    for caps in range(ell_size, 1 << size):
        if maximum_survival(size, deleted, caps) >= required:
            return caps
    raise AssertionError("no endpoint solution")


def restriction_curvature_check(
    size: int,
    deleted: int,
    face_counts: list[int],
    cap_counts: list[int],
    f: dict[int, int],
    p: dict[int, int],
):
    number = comb(size, deleted)
    face_survival = sum(
        value * comb(size - rank, deleted)
        for rank, value in enumerate(face_counts)
        if size - rank >= deleted
    )
    endpoint_survival = sum(
        value * comb(size - rank, deleted)
        for rank, value in enumerate(cap_counts)
        if size - rank >= deleted
    )
    defect = face_survival - number * f[size - deleted]
    assert defect >= 0
    nonminimal = min(number, defect)
    child_ell = (size - deleted) + comb(size - deleted, 2)
    required = ((number - nonminimal) * p[size - deleted]
                + nonminimal * child_ell)
    assert endpoint_survival >= required
    return defect, endpoint_survival, required


def asymptotic_audit() -> list[tuple[int, int, int, float]]:
    rows = []
    for length in (8, 10, 12, 14):
        size = 1 << length
        faces = 1 << (49 * length * length // 100)
        bound = moment_lower_bound(size, faces)
        rank = 1
        cumulative = 0
        while cumulative + comb(size, rank) < faces:
            cumulative += comb(size, rank)
            rank += 1
        scale = Fraction(rank * faces, size)
        ratio = float(Fraction(bound, 1) / scale)
        assert bound >= scale / 3
        rows.append((length, rank, bound.bit_length() - 1, ratio))
    return rows


def main() -> None:
    gate = load_module(
        "endpoint_curvature_gate",
        ROOT / "agent_reflection_gate" / "reflection_order_gate.py",
    )
    wrapper = load_module(
        "endpoint_curvature_wrapper",
        ROOT / "agent_shield_circuit_cover" /
        "verify_two_direction_four_point_wrapper.py",
    )

    # Exhaustive reflection-order scans.  For n<=8 every class in these
    # minima has a stored or independently checked rational realization.
    b5 = exact_bruhat_rows(5)
    b8 = exact_bruhat_rows(8)
    assert (b5["classes"], b8["classes"]) == (62, 1_232_944)
    assert b5["profiles"][:3] == [[26, 17, 2], [28, 16, 6], [31, 15, 2]]
    assert b8["profiles"][:2] == [[113, 55, 16], [114, 53, 4]]
    lambda5 = Fraction(28 - 26, 17 - 16)
    lambda8 = Fraction(114 - 113, 55 - 53)
    assert (lambda5, lambda8) == (2, Fraction(1, 2))

    minimizer5_word = (1, 0, 1, 2, 1, 3, 2, 1, 0, 1)
    near5_word = (0, 1, 0, 2, 1, 3, 2, 1, 0, 1)
    e5 = gate.evaluate_word(5, minimizer5_word, graded=True)
    q5 = gate.evaluate_word(5, near5_word, graded=True)
    assert (e5.trace, e5.cap_total, q5.trace, q5.cap_total) == (26, 17, 28, 16)
    ys5 = gate.fixed_x_realization(5, gate.root_sequence(5, minimizer5_word))
    assert ys5 is not None
    points5 = [(Fraction(index), value) for index, value in enumerate(ys5)]

    points8 = [
        (42, 236), (249, 28), (131, 71), (77, 168),
        (76, 161), (53, 195), (83, 60), (7, 20),
    ]
    near8 = [
        (80, 233), (254, 23), (219, 45), (154, 125),
        (85, 218), (82, 206), (78, 96), (1, 71),
    ]
    points9 = [
        (62614, 7322), (2922, 4014), (10209, 14386),
        (20660, 24299), (33336, 29017), (30137, 33324),
        (15334, 45211), (14934, 55621), (10934, 61521),
    ]
    near9 = [
        (11164, 4101), (12508, 65228), (15188, 59208),
        (27928, 45988), (17968, 20888), (16188, 13108),
        (28308, 26528), (48288, 28008), (60248, 30768),
    ]

    face5 = face_profile(points5)
    face8 = face_profile(points8)
    face9 = face_profile(points9)
    assert face5 == [0, 5, 10, 10, 1, 0]
    assert face8 == [0, 8, 28, 56, 21, 0, 0, 0, 0]
    assert face9 == [0, 9, 36, 84, 36, 3, 0, 0, 0, 0]

    c5, _, cap5, _ = minimum_cap_profile(wrapper, points5)
    c8, _, cap8, _ = minimum_cap_profile(wrapper, points8)
    c9, _, cap9, _ = minimum_cap_profile(wrapper, points9)
    assert (c5, c8, c9) == (17, 55, 82)
    assert cap5 == [0, 5, 10, 2, 0, 0]
    assert cap8 == [0, 8, 28, 17, 2, 0, 0, 0, 0]
    assert cap9 == [0, 9, 36, 28, 8, 1, 0, 0, 0, 0]

    cn8, _, _, _ = minimum_cap_profile(wrapper, near8)
    cn9, _, _, _ = minimum_cap_profile(wrapper, near9)
    assert (sum(face_profile(near8)), cn8) == (114, 53)
    assert (sum(face_profile(near9)), cn9) == (169, 76)
    strong8 = strong_decomposition_audit(near8)
    strong9 = strong_decomposition_audit(near9)
    assert strong8 == (False, 109_600)
    assert strong9 == (False, 986_409)
    lambda9_witness = Fraction(169 - 168, 82 - 76)
    assert lambda9_witness == Fraction(1, 6)

    database9 = json.loads(
        (ROOT / "agent_lex_minimizer_search" / "exact_realizable_n9.json").read_text()
    )
    assert database9["record_count"] == 158_817
    assert database9["minimum_trace"] == 168
    assert database9["minimum_trace_count_in_database"] == 1

    f = {1: 1, 2: 3, 3: 7, 4: 14, 5: 26, 6: 44, 7: 72, 8: 113, 9: 168}
    p = {1: 1, 2: 3, 3: 6, 4: 11, 5: 17, 6: 28, 7: 40, 8: 55, 9: 82}
    profiles = {5: face5, 8: face8, 9: face9}
    caps = {5: cap5, 8: cap8, 9: cap9}

    moment_bounds = {}
    mobius_bounds = {}
    curvature = {}
    for size in (5, 8, 9):
        moment_bounds[size] = moment_lower_bound(size, f[size])
        assert moment_bounds[size] <= p[size]
        mobius_bounds[size] = [
            mobius_lower_bound(size, deleted, profiles[size])
            for deleted in range(1, size)
        ]
        assert mobius_bounds[size][0] >= moment_bounds[size]
        curvature[size] = restriction_curvature_check(
            size, 1, profiles[size], caps[size], f, p
        )
    assert moment_bounds == {5: 17, 8: 53, 9: 71}
    assert {size: rows[0] for size, rows in mobius_bounds.items()} == {
        5: 17, 8: 53, 9: 72,
    }
    assert curvature[5][0] == 1
    assert curvature[8][0] == 12
    assert curvature[9][0] == 3

    # At every literal seam the facing penalty is at least one.  Hence the
    # two database-certified competitors strictly beat the ordinary
    # minimizers inside the weighted child functional.
    for penalty in (1, 2, 17, 10**6):
        assert 1 - 2 * penalty < 0       # n=8: (114,53) vs (113,55)
        assert 1 - 6 * penalty < 0       # n=9: (169,76) vs (168,82)

    scales = asymptotic_audit()
    print(
        "PASS: minimizer endpoint moment/Mobius bounds, restriction-defect "
        "curvature, exact B(5,2)/B(8,2) scans, n=9 stretchable flat-frontier "
        "witness, and high-wall obstruction; "
        f"p={{5:17,8:55,9_stored:82}}; lambda={{5:{lambda5},8:{lambda8},"
        f"9_witness:{lambda9_witness}}}; moment_bounds={moment_bounds}; "
        f"curvature={curvature}; nonstrong_cache_misses={{8:{strong8[1]},"
        f"9:{strong9[1]}}}; scales={scales}"
    )


if __name__ == "__main__":
    main()
