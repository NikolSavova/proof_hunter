#!/usr/bin/env python3
"""Exact checks for COUPLED_PARETO_TWO_ANCHOR_GATE.md."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path
import importlib.util
import json
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def points_from(certificate: dict, name: str):
    return [tuple(point) for point in certificate["configurations"][name]["coordinates"]]


def minimum_cap(wrapper, base, points) -> int:
    if len(points) <= 2:
        return (1 << len(points)) - 1
    return base.minimum_cap_profile(wrapper, points)[0]


def singleton_root_row(wrapper, base, points, deleted: int):
    """Return (child V, root endpoint count) and audit the root signs."""
    labels = tuple(index for index in range(len(points)) if index != deleted)
    root_order = None
    for order in permutations(labels):
        signs = {
            1 if base.orient(points[order[i]], points[order[j]], points[deleted]) > 0
            else -1
            for i, j in combinations(range(len(order)), 2)
        }
        if len(signs) == 1:
            root_order = order
            break
    assert root_order is not None

    child = [points[index] for index in labels]
    child_v = sum(base.face_profile(child))
    parent_v = sum(base.face_profile(points))
    endpoint = parent_v - child_v - 1

    relabel = {old: new for new, old in enumerate(labels)}
    signs = wrapper.all_signs([tuple(map(Fraction, point)) for point in child])
    order = tuple(relabel[index] for index in root_order)
    cap, cup = wrapper.chain_counts(signs, order)
    assert endpoint in (cap, cup)
    return child_v, endpoint


def stored_induced_bipartition_scan(wrapper, base, points):
    """Best glue of the displayed realizations' two induced order types."""
    size = len(points)
    full = (1 << size) - 1
    cache = {}
    for mask in range(1, full + 1):
        child = [points[index] for index in range(size) if mask >> index & 1]
        cache[mask] = (
            sum(base.face_profile(child)),
            minimum_cap(wrapper, base, child),
        )

    best = None
    count = 0
    for mask in range(1, full):
        left_v, left_c = cache[mask]
        right_v, right_u = cache[full ^ mask]
        value = left_v + right_v + left_c * right_u
        if best is None or value < best:
            best, count = value, 1
        elif value == best:
            count += 1
    assert best is not None
    return best, count


def main() -> None:
    certificate = json.loads((HERE / "coupled_pareto_certificate.json").read_text())
    base = load_module(
        "coupled_pareto_base",
        ROOT / "agent_minimizer_endpoint_curvature" /
        "verify_minimizer_endpoint_curvature.py",
    )
    wrapper = load_module(
        "coupled_pareto_wrapper",
        ROOT / "agent_shield_circuit_cover" /
        "verify_two_direction_four_point_wrapper.py",
    )

    names = ("ordinary_8", "flat_8", "ordinary_9", "flat_9", "killer_9")
    points = {name: points_from(certificate, name) for name in names}

    expected_profiles = {
        "ordinary_8": [0, 8, 28, 56, 21, 0, 0, 0, 0],
        "flat_8": [0, 8, 28, 56, 21, 1, 0, 0, 0],
        "ordinary_9": [0, 9, 36, 84, 36, 3, 0, 0, 0, 0],
        "flat_9": [0, 9, 36, 84, 38, 2, 0, 0, 0, 0],
        "killer_9": [0, 9, 36, 84, 42, 1, 0, 0, 0, 0],
    }
    expected_caps = {
        "ordinary_8": 55,
        "flat_8": 53,
        "ordinary_9": 82,
        "flat_9": 76,
        "killer_9": 71,
    }
    for name in names:
        profile = base.face_profile(points[name])
        assert profile == expected_profiles[name]
        assert sum(profile) == certificate["configurations"][name]["V"]
        assert minimum_cap(wrapper, base, points[name]) == expected_caps[name]

    # Complete B(8,2) scan.  Positive coefficients mean that retaining only
    # the least C at each V loses no coupled or weighted minimizer.
    b8 = base.exact_bruhat_rows(8)
    assert b8["classes"] == 1_232_944
    rows = b8["profiles"]
    weighted_one = min(v + c for v, c, _ in rows)
    weighted_one_rows = [(v, c) for v, c, _ in rows if v + c == weighted_one]
    assert weighted_one == 167
    assert weighted_one_rows == [(114, 53)]
    assert min(v + 2 * c for v, c, _ in rows) == 218

    coupled_88 = min(
        left_v + right_v + left_c * right_u
        for left_v, left_c, _ in rows
        for right_v, right_u, _ in rows
    )
    coupled_88_rows = [
        (left_v, left_c, right_v, right_u)
        for left_v, left_c, _ in rows
        for right_v, right_u, _ in rows
        if left_v + right_v + left_c * right_u == coupled_88
    ]
    assert coupled_88 == 1_806
    assert coupled_88_rows == [(255, 36, 255, 36)]
    assert coupled_88 - 2 * 113 == 1_580

    # The singleton specialization K_{8,1}.  It is exactly saturated by
    # the nonordinary, nonstrong eight-point frontier point.
    assert weighted_one - 113 == 54
    assert 113 + 1 + 54 == 168

    ordinary9_hull = [points["ordinary_9"].index(point)
                      for point in base.hull(points["ordinary_9"])]
    flat9_hull = [points["flat_9"].index(point)
                  for point in base.hull(points["flat_9"])]
    ordinary9_roots = sorted(
        singleton_root_row(wrapper, base, points["ordinary_9"], deleted)
        for deleted in ordinary9_hull
    )
    flat9_roots = sorted(
        singleton_root_row(wrapper, base, points["flat_9"], deleted)
        for deleted in flat9_hull
    )
    assert ordinary9_roots == [(114, 53)] * 3
    assert flat9_roots == [(113, 55), (114, 54), (117, 51)]
    assert all(v - 113 + c == 54 for v, c in ordinary9_roots)
    assert all(v - 113 + c == 55 for v, c in flat9_roots)

    # A third explicit nonstrong nine-point profile kills both displayed
    # profiles at every integer sibling endpoint u >= 1.
    for penalty in (1, 2, 45, 82, 10**6):
        assert (172 + 71 * penalty) - (168 + 82 * penalty) == 4 - 11 * penalty
        assert (172 + 71 * penalty) - (169 + 76 * penalty) == 3 - 5 * penalty
        assert 4 - 11 * penalty < 0
        assert 3 - 5 * penalty < 0

    # The exact mixed rectangle curvature of H(c,u)=Phi_a(c)+Phi_b(u)+cu.
    profiles8 = ((0, 55), (1, 53))
    profiles9 = ((0, 82), (1, 76), (4, 71))
    for delta0, c0 in profiles8:
        for delta1, c1 in profiles8:
            for epsilon0, u0 in profiles9:
                for epsilon1, u1 in profiles9:
                    h00 = delta0 + epsilon0 + c0 * u0
                    h11 = delta1 + epsilon1 + c1 * u1
                    h01 = delta0 + epsilon1 + c0 * u1
                    h10 = delta1 + epsilon0 + c1 * u0
                    assert h00 + h11 - h01 - h10 == (c0 - c1) * (u0 - u1)

    induced_expected = {
        "ordinary_8": (113, 16),
        "flat_8": (113, 12),
        "ordinary_9": (168, 6),
        "flat_9": (169, 10),
    }
    induced = {
        name: stored_induced_bipartition_scan(wrapper, base, points[name])
        for name in induced_expected
    }
    assert induced == induced_expected

    strong = {
        name: base.strong_decomposition_audit(points[name])
        for name in names
    }
    assert strong == {
        "ordinary_8": (False, 109_600),
        "flat_8": (False, 109_600),
        "ordinary_9": (False, 986_409),
        "flat_9": (False, 986_409),
        "killer_9": (False, 986_409),
    }

    print(
        "PASS: exact coupled Pareto envelope; "
        "K_8,1=54 at (114,53); K_8,8=1580 at two (255,36) profiles; "
        "ordinary-9 singleton roots=[(114,53)]x3; "
        "flat-9 roots=[(113,55),(114,54),(117,51)]; "
        "killer-9=(172,71); stored induced bipartitions="
        f"{induced}; all five configurations nonstrong"
    )


if __name__ == "__main__":
    main()
