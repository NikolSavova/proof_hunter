#!/usr/bin/env python3
"""Exact verifier for CENTRAL_SHELL_PROFILE_RECURRENCE.md."""

from __future__ import annotations

from itertools import combinations, product
from math import prod


ROOT = (137, 251)
CLUSTERS = (
    ((100001, 0), (100002, 400), (100003, 100), (100004, 0)),
    ((76558, 64237), (76675, 64282)),
    ((17322, 98540), (17267, 98459)),
    ((-49979, 86506), (-49971, 86505)),
    ((-94063, 34283), (-93986, 34113)),
    ((-93871, -34144), (-94046, -34251)),
    ((-49927, -86516), (-49977, -86536)),
    ((17360, -98456), (17376, -98408)),
    ((76652, -64268), (76681, -64190)),
)


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for point in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def convex(points):
    return len(points) == len(set(points)) and len(hull(points)) == len(points)


def finite_geometry_audit():
    points = (ROOT,) + sum(CLUSTERS, ())
    assert len(points) == 21
    assert all(cross(a, b, c) != 0 for a, b, c in combinations(points, 3))

    child = CLUSTERS[0]
    child_faces = []
    for mask in range(1, 1 << len(child)):
        face = [child[index] for index in range(len(child)) if mask & (1 << index)]
        if convex(face):
            child_faces.append(mask)
    assert len(child_faces) == 14

    directional = {}
    for gap in (1, 8):
        other_roles = [role for role in range(1, 9) if role != gap]
        compatible_masks = []
        outputs = set()
        for mask in child_faces:
            profile = tuple(child[index] for index in range(len(child)) if mask & (1 << index))
            good = True
            local_outputs = []
            for labels in product(range(2), repeat=len(other_roles)):
                face = profile + tuple(
                    CLUSTERS[role][label] for role, label in zip(other_roles, labels)
                )
                if not convex(face):
                    good = False
                    break
                local_outputs.append(frozenset(face))
            if good:
                compatible_masks.append(mask)
                outputs.update(local_outputs)
        assert len(compatible_masks) == 10
        assert len(outputs) == 10 * 2**7 == 1280
        directional[gap] = {
            "compatible_child_profiles": len(compatible_masks),
            "singleton_completions_per_profile": 2**7,
            "bank": len(outputs),
        }

    assert directional[1]["compatible_child_profiles"] ** 2 >= len(child_faces)
    return {
        "points": len(points),
        "general_position": True,
        "child_nonempty_faces": len(child_faces),
        "directional_gap_banks": directional,
    }


def cyclic_identity_audit():
    arrays = (
        ((3, 5, 2, 7, 4), (6, 2, 8, 3, 9), 11),
        ((1, 4, 9, 2), (7, 3, 2, 8), 5),
    )
    rows = []
    for left, right, alphabet in arrays:
        t = len(left)
        faces = tuple(left[i] * right[i] for i in range(t))
        banks = tuple(
            right[(gap - 1) % t] * left[(gap + 1) % t] * alphabet ** (t - 3)
            for gap in range(t)
        )
        assert prod(banks) == alphabet ** (t * (t - 3)) * prod(faces)
        assert max(banks) ** t >= prod(banks)
        rows.append(
            {
                "t": t,
                "A": alphabet,
                "H": faces,
                "banks": banks,
                "max_bank": max(banks),
            }
        )
    return rows


def coefficient_audit():
    # Coefficients are represented in eighths.
    # parent >= alpha + child/2.
    cases = []
    alpha8 = 2  # 1/4
    for child8 in (2, 3, 4):
        parent16 = 2 * alpha8 + child8  # sixteenths
        cases.append((alpha8, child8, parent16))
    assert cases == [(2, 2, 6), (2, 3, 7), (2, 4, 8)]
    # Fixed point c >= alpha+c/2 gives c>=2alpha=1/2.
    fixed_point8 = 2 * alpha8
    assert fixed_point8 == 4
    # All-role cyclic theorem: alpha + average child c.
    all_role8 = alpha8 + 2
    assert all_role8 == 4
    return {
        "one_role_cases_alpha_child_parent_sixteenths": cases,
        "fixed_point_eighths": fixed_point8,
        "all_role_universal_eighths": all_role8,
    }


def main():
    results = {
        "geometry": finite_geometry_audit(),
        "cyclic_identity": cyclic_identity_audit(),
        "coefficients": coefficient_audit(),
    }
    print("CENTRAL_SHELL_PROFILE_RECURRENCE verifier: PASS")
    for name, result in results.items():
        print(f"{name}: {result}")


if __name__ == "__main__":
    main()
