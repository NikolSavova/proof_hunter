#!/usr/bin/env python3
"""Exact checks for DENSE_HALL_TWO_CLOUD_PROFILE_BARRIER.md."""

from fractions import Fraction as Q
from itertools import combinations
from math import comb


def orient(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points):
    points = sorted(set(points))
    if len(points) <= 2:
        return points

    def half(sequence):
        answer = []
        for point in sequence:
            while len(answer) >= 2 and orient(answer[-2], answer[-1], point) <= 0:
                answer.pop()
            answer.append(point)
        return answer

    return half(points)[:-1] + half(reversed(points))[:-1]


def convex(points):
    return len(hull(points)) == len(set(points))


def nonempty_subsets(points):
    for mask in range(1, 1 << len(points)):
        yield tuple(points[i] for i in range(len(points)) if mask >> i & 1)


def hall(records):
    best = Q(0)
    for mask in range(1, 1 << len(records)):
        targets = set()
        demand = 0
        for index, bank in enumerate(records):
            if mask >> index & 1:
                demand += 1
                targets.update(bank)
        best = max(best, Q(demand, len(targets)))
    return best


def hall_audit():
    for size in range(1, 4):
        records = [
            (f"W{j}", "Q", f"C{j}", f"A{i}", f"E{i}")
            for i in range(size) for j in range(size)
        ]
        assert hall(records) == Q(size * size, 4 * size + 1)

    for size in range(1, 101):
        best = max(
            Q(rows * columns, 2 * rows + 2 * columns + 1)
            for rows in range(1, size + 1)
            for columns in range(1, size + 1)
        )
        assert best == Q(size * size, 4 * size + 1)
    return Q(9, 13)


B = [(Q(-3), Q(0)), (Q(3), Q(0)), (Q(0), Q(5))]
V = (Q(-2), Q(-1))
U = (Q(2), Q(-1))
G0 = (Q(1, 100), Q(50099, 10000))
X0 = (Q(0), Q(-4))


def embed(center, offsets, epsilon):
    return [
        (center[0] + epsilon * Q(a), center[1] + epsilon * epsilon * Q(b))
        for a, b in offsets
    ]


def cage_audit(guards, pockets):
    whole = B + [V, U] + guards + pockets
    assert all(orient(*triple) != 0 for triple in combinations(whole, 3))
    assert convex(B + [V])
    for guard in guards:
        assert convex(B + [guard])
        assert convex(B + [guard, V, U])
    for pocket in pockets:
        assert convex(B + [pocket])
        assert convex([pocket, V])
        for guard in guards:
            assert not convex(B + [guard, pocket, V])

    # The five targets recover the complete row/column record.
    decoded = {}
    for i, guard in enumerate(guards):
        for j, pocket in enumerate(pockets):
            targets = (
                frozenset([pocket, V]),
                frozenset(B + [V]),
                frozenset(B + [pocket]),
                frozenset(B + [guard]),
                frozenset(B + [guard, V, U]),
            )
            assert targets not in decoded
            decoded[targets] = (i, j)
    assert len(decoded) == len(guards) * len(pockets)


def cross_count(guards, pockets):
    guard_subsets = list(nonempty_subsets(guards))
    pocket_subsets = list(nonempty_subsets(pockets))
    return sum(convex(left + right)
               for left in guard_subsets for right in pocket_subsets)


def arbitrary_order_type_audit():
    # Each fourth offset lies inside the triangle of the first three.
    guard_offsets = [(-3, 0), (4, 3), (1, -4), (Q(2, 3), Q(-1, 3))]
    pocket_offsets = [(-4, 0), (3, 4), (2, -5), (Q(1, 3), Q(-1, 3))]
    epsilon = Q(1, 10 ** 6)
    guards = embed(G0, guard_offsets, epsilon)
    pockets = embed(X0, pocket_offsets, epsilon)
    cage_audit(guards, pockets)
    assert not convex(guards) and not convex(pockets)

    guard_subsets = list(nonempty_subsets(guards))
    pocket_subsets = list(nonempty_subsets(pockets))
    right = sum(convex(subset + (pockets[0],)) for subset in guard_subsets)
    left = sum(convex((guards[0],) + subset) for subset in pocket_subsets)
    crossing = cross_count(guards, pockets)
    assert (right, left, crossing) == (11, 13, 143)
    assert crossing == right * left
    return right, left, crossing


def rooted_fan_audit():
    # Pocket-label-hidden signed class: x lies in triangle(v,l,r), while
    # all W,Q,C,A,E targets remain ordinary.
    fan_v = (Q(1, 10), Q(-4))
    fan_u = (Q(2), Q(-3))
    fan_x0 = (Q(-2), Q(-1))
    weights = (Q(1, 4), Q(57, 80), Q(3, 80))
    assert sum(weights) == 1 and all(weight > 0 for weight in weights)
    assert tuple(
        weights[0] * fan_v[axis]
        + weights[1] * B[0][axis]
        + weights[2] * B[1][axis]
        for axis in range(2)
    ) == fan_x0

    guard_offsets = [(-3, 0), (4, 3), (1, -4), (Q(2, 3), Q(-1, 3))]
    pocket_offsets = [(-4, 0), (3, 4), (2, -5), (Q(1, 3), Q(-1, 3))]
    epsilon = Q(1, 10 ** 6)
    guards = embed(G0, guard_offsets, epsilon)
    pockets = embed(fan_x0, pocket_offsets, epsilon)
    whole = B + [fan_v, fan_u] + guards + pockets
    assert all(orient(*triple) != 0 for triple in combinations(whole, 3))
    for guard in guards:
        assert convex(B + [guard])
        assert convex(B + [guard, fan_v, fan_u])
    for pocket in pockets:
        assert convex(B + [pocket])
        assert convex([pocket, fan_v])
        for guard in guards:
            assert not convex(B + [guard, pocket, fan_v])

    guard_subsets = list(nonempty_subsets(guards))
    pocket_subsets = list(nonempty_subsets(pockets))
    right = sum(convex(subset + (pockets[0],)) for subset in guard_subsets)
    left = sum(convex((guards[0],) + subset) for subset in pocket_subsets)
    crossing = cross_count(guards, pockets)
    assert (right, left, crossing) == (11, 13, 143)
    return right, left, crossing


def parabolic_cloud(center, size, sign):
    epsilon = Q(1, 10 ** 5 * size * size)
    offsets = [(index, sign * index * index) for index in range(1, size + 1)]
    return embed(center, offsets, epsilon)


def parabolic_profile_audit():
    checked = 0
    last = None
    anchor_decorated = None
    for size in range(2, 8):
        small = size + comb(size, 2)
        total = (1 << size) - 1
        for guard_sign in (-1, 1):
            for pocket_sign in (-1, 1):
                guards = parabolic_cloud(G0, size, guard_sign)
                pockets = parabolic_cloud(X0, size, pocket_sign)
                cage_audit(guards, pockets)
                assert sum(convex(subset) for subset in nonempty_subsets(guards)) == total
                assert sum(convex(subset) for subset in nonempty_subsets(pockets)) == total
                guard_profile = small if guard_sign == 1 else total
                pocket_profile = small if pocket_sign == -1 else total
                crossing = cross_count(guards, pockets)
                assert crossing == guard_profile * pocket_profile

                # Any anchor-decorated cross face has one of these traces.
                assert crossing * (1 << 5) <= 32 * max(
                    small * small, small * total, total * total
                )
                checked += 1
                last = (size, guard_sign, pocket_sign, crossing)

                if size == 4 and guard_sign == 1 and pocket_sign == -1:
                    anchors = B + [V, U]
                    points = guards + pockets + anchors
                    anchor_decorated = 0
                    for mask in range(1, 1 << len(points)):
                        if not any(mask >> index & 1 for index in range(size)):
                            continue
                        if not any(mask >> (size + index) & 1
                                   for index in range(size)):
                            continue
                        subset = [points[index] for index in range(len(points))
                                  if mask >> index & 1]
                        anchor_decorated += convex(subset)
                    assert anchor_decorated <= 32 * small * small
    assert anchor_decorated == 1800
    return checked, last, anchor_decorated


def main():
    hall_value = hall_audit()
    arbitrary = arbitrary_order_type_audit()
    rooted_fan = rooted_fan_audit()
    parabolic = parabolic_profile_audit()
    print(
        "PASS: five-target Hall=%s; arbitrary profiles=%dx%d=%d; "
        "rooted-fan=%dx%d=%d; "
        "parabolic systems=%d last=%s anchor-cross=%d"
        % (hall_value, arbitrary[0], arbitrary[1], arbitrary[2],
           rooted_fan[0], rooted_fan[1], rooted_fan[2],
           parabolic[0], parabolic[1], parabolic[2])
    )


if __name__ == "__main__":
    main()
