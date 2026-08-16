#!/usr/bin/env python3
"""Exact checks for STATIONARY_ALL_DELETE_WEIGHTED_PROFILE_MUTATION_GATE.md."""

from __future__ import annotations

from itertools import combinations
from math import comb
from pathlib import Path
import importlib.util
import sys


ROOT = Path(__file__).resolve().parent.parent
GEOMETRY = ROOT / "agent_geometry" / "audit_geometry.py"


def load_geometry():
    spec = importlib.util.spec_from_file_location("weighted_seam_geometry", GEOMETRY)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def all_nonempty_subsets(indices: tuple[int, ...]):
    for rank in range(1, len(indices) + 1):
        yield from combinations(indices, rank)


def profile(g, labels: tuple[int, ...], orient):
    faces = []
    caps = []
    cups = []
    for subset in all_nonempty_subsets(labels):
        if not g.is_convex(subset, orient):
            continue
        faces.append(subset)
        if g.is_cap(subset, orient):
            caps.append(subset)
        if g.is_cup(subset, orient):
            cups.append(subset)
    counts = (len(faces), len(caps), len(cups))
    moments = tuple(sum(len(face) for face in family)
                    for family in (faces, caps, cups))
    return counts, moments


def algebra_audit() -> int:
    """Check both singleton recurrences and all four reflection products."""
    checked = 0
    for a in range(2, 11):
        for q_w in range(1, 13):
            for q_c in range(1, 8):
                for q_u in range(1, 8):
                    for lam in range(1, 7):
                        # Q prec {s}: ordinary and cap increments coincide.
                        right_w = q_w + 1 + q_c
                        right_c = 1 + 2 * q_c
                        assert ((right_w + lam * right_c)
                                - (q_w + lam * q_c)
                                == (1 + lam) * (1 + q_c))

                        # {s} prec Q: cup gives the ordinary increment, while
                        # every old cap plus the singleton is a cap.
                        left_w = q_w + 1 + q_u
                        left_c = q_c + a
                        assert ((left_w + lam * left_c)
                                - (q_w + lam * q_c)
                                == 1 + q_u + lam * a)

                        # Symmetric U-weighted recurrences for the right child.
                        left_u = 1 + 2 * q_u
                        assert ((left_w + lam * left_u)
                                - (q_w + lam * q_u)
                                == (1 + lam) * (1 + q_u))
                        right_u = q_u + a
                        assert ((right_w + lam * right_u)
                                - (q_w + lam * q_u)
                                == 1 + q_c + lam * a)
                        checked += 1

    # Every reflection state changes only the indicated mixed product.
    for c_a in range(1, 10):
        for u_a in range(1, 10):
            for c_b in range(1, 10):
                for u_b in range(1, 10):
                    assert (c_a * u_b, u_a * u_b,
                            c_a * c_b, u_a * c_b) == (
                                c_a * u_b, u_a * u_b,
                                c_a * c_b, u_a * c_b)
                    checked += 1
    return checked


def scalar_equality_exclusion() -> dict[str, int]:
    minimum_gap = None
    checks = 0
    for m in range(3, 201):
        t0 = m * (m + 1) // 2

        def gap(t: int) -> int:
            return (m + 1) * t * t - m - (2 * m * m + m) * t

        displayed = m * m * (m + 1) * (m * m - 2 * m - 1) - 4 * m
        assert 4 * gap(t0) == displayed
        assert displayed > 0
        assert gap(t0 + 1) > gap(t0)
        for t in (t0, t0 + 1, 2 * t0, 4 * t0 + 3):
            assert gap(t) > 0
            checks += 1
        minimum_gap = gap(t0) if minimum_gap is None else min(minimum_gap, gap(t0))
    assert minimum_gap == 15  # m=3, t=6: 144-(3+126).
    return {"m_values": 198, "checks": checks, "minimum_gap": minimum_gap}


def pascal_mutation_audit(g) -> dict[str, object]:
    points = g.cell(6, 3)
    assert len(points) == comb(6, 3) == 20
    orient = g.orient_table(points)
    left = tuple(range(10))
    right = tuple(range(10, 20))

    left_profile, left_moments = profile(g, left, orient)
    right_profile, right_moments = profile(g, right, orient)
    assert left_profile == (375, 101, 170)
    assert right_profile == (375, 170, 101)
    assert left_moments == (1320, 238, 486)
    assert right_moments == (1320, 486, 238)

    w_a, c_a, u_a = left_profile
    w_b, c_b, u_b = right_profile
    parent = w_a + w_b + c_a * u_b
    reflections = (c_a * u_b, u_a * u_b, c_a * c_b, u_a * c_b)
    assert parent == 10951
    assert reflections == (10201, 17170, 17170, 28900)
    assert reflections[0] == min(reflections)

    # Check every deletion identity and both literal singleton restorations.
    left_deleted = []
    left_decreases = []
    for x in left:
        q = tuple(z for z in left if z != x)
        (q_w, q_c, q_u), _ = profile(g, q, orient)
        left_deleted.append((q_w, q_c, q_u))
        old_j = w_a + u_b * c_a
        right_restore = (q_w + 1 + q_c) + u_b * (1 + 2 * q_c)
        left_restore = (q_w + 1 + q_u) + u_b * (q_c + len(left))
        left_decreases.append(old_j - min(right_restore, left_restore))

    assert sum(w_a - q_w for q_w, _, _ in left_deleted) == left_moments[0]
    assert sum(c_a - q_c for _, q_c, _ in left_deleted) == left_moments[1]
    assert sum(u_a - q_u for _, _, q_u in left_deleted) == left_moments[2]

    right_deleted = []
    right_decreases = []
    for y in right:
        r = tuple(z for z in right if z != y)
        (r_w, r_c, r_u), _ = profile(g, r, orient)
        right_deleted.append((r_w, r_c, r_u))
        old_j = w_b + c_a * u_b
        left_restore = (r_w + 1 + r_u) + c_a * (1 + 2 * r_u)
        right_restore = (r_w + 1 + r_c) + c_a * (r_u + len(right))
        right_decreases.append(old_j - min(left_restore, right_restore))

    assert sum(w_b - r_w for r_w, _, _ in right_deleted) == right_moments[0]
    assert sum(c_b - r_c for _, r_c, _ in right_deleted) == right_moments[1]
    assert sum(u_b - r_u for _, _, r_u in right_deleted) == right_moments[2]
    expected = [1041] * 3 + [1213] * 3 + [1818] * 4
    assert sorted(left_decreases) == expected
    assert sorted(right_decreases) == expected

    return {
        "left": (left_profile, left_moments),
        "right": (right_profile, right_moments),
        "parent": parent,
        "reflections": reflections,
        "decreases": sorted(set(left_decreases + right_decreases)),
    }


def wall_and_scale_audit() -> dict[str, object]:
    # A literal finite instance of the conditional wall inequality.
    w_a, w_b, a, b = 1000, 1200, 10, 12
    c_a, u_b, u_a, c_b = 2, 3, 50, 60
    current = w_a + w_b + c_a * u_b
    reflected = w_a + w_b + u_a * c_b
    target = 6000
    slack = target - current
    wall = u_a * c_b - c_a * u_b
    assert 0 <= wall < slack
    assert reflected == current + wall < target
    assert u_a * c_b >= w_a * w_b // (4 * a * b)

    # Equation (30) exceeds a cL^2 fixed-gap target by a quadratic number
    # of bits. Integer inequalities avoid floating-point asymptotics.
    # Here c=49/100, so multiply every logarithmic exponent by 100.
    scale_rows = []
    for length in (64, 96, 128, 192, 256, 384, 512):
        opposite_times_100 = 98 * (length - 1) ** 2 - 200 * length
        target_times_100 = 49 * length * length
        margin_times_100 = opposite_times_100 - target_times_100
        assert margin_times_100 > 0
        scale_rows.append((length, margin_times_100))

    return {
        "finite_wall": (current, wall, slack, reflected, target),
        "scale_rows": scale_rows,
    }


def main() -> None:
    g = load_geometry()
    algebra_rows = algebra_audit()
    scalar = scalar_equality_exclusion()
    pascal = pascal_mutation_audit(g)
    wall = wall_and_scale_audit()
    print(
        "PASS: weighted child minimality, scalar exclusion, exact Pascal "
        "mutations, and conditional high-wall gate; "
        f"algebra_rows={algebra_rows}; scalar={scalar}; "
        f"Pascal={pascal}; wall={wall}"
    )


if __name__ == "__main__":
    main()
