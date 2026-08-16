#!/usr/bin/env python3
"""Exact checks for MINIMIZER_COMMON_GUARD_PROFILE_MUTATIONS.md."""

from fractions import Fraction as Q
from itertools import combinations, permutations, product


def orient(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
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


def convex(points):
    return len(set(points)) == len(hull(points))


def rooted_profiles(points):
    faces = sum(convex([points[i] for i in range(4) if mask >> i & 1])
                for mask in range(1, 1 << 4))
    answer = set()
    for order in permutations(range(4)):
        position = {label: index for index, label in enumerate(order)}
        caps = cups = 10
        signs = []
        for triple in combinations(range(4), 3):
            i, j, k = sorted(triple, key=position.get)
            sign = orient(points[i], points[j], points[k])
            assert sign != 0
            caps += sign < 0
            cups += sign > 0
            signs.append(sign)
        if all(sign < 0 for sign in signs):
            caps += 1
        if all(sign > 0 for sign in signs):
            cups += 1
        answer.add((faces, caps, cups))
    return answer


def complete_menu():
    convex_seed = [(Q(0), Q(0)), (Q(1), Q(3)),
                   (Q(3), Q(2)), (Q(4), Q(0))]
    interior_seed = [(Q(0), Q(0)), (Q(1), Q(4)),
                     (Q(2), Q(1)), (Q(4), Q(0))]
    menu = rooted_profiles(convex_seed) | rooted_profiles(interior_seed)
    expected = {(15, 10, 15), (15, 12, 12), (15, 15, 10),
                (14, 11, 13), (14, 13, 11)}
    assert menu == expected
    return tuple(sorted(menu))


def recurrence(word):
    q = len(word)
    sizes = [1] + [4] * q + [1]
    faces = [1] + [state[0] for state in word] + [1]
    caps = [1] + [state[1] for state in word] + [1]
    cups = [1] + [state[2] for state in word] + [1]
    total = sum(faces)
    for i in range(q + 2):
        middle = 1
        for j in range(i + 1, q + 2):
            total += caps[i] * cups[j] * middle
            middle *= 1 + sizes[j]
    return total


def check_finite_global_mutations(menu):
    words = [(recurrence(word), word) for word in product(menu, repeat=3)]
    minimum = min(value for value, _ in words)
    minimizers = [word for value, word in words if value == minimum]
    chosen = ((15, 10, 15), (14, 11, 13), (15, 15, 10))
    assert minimum == 1561 and chosen in minimizers and len(minimizers) == 2

    replacement_rows = []
    for position in range(3):
        values = []
        for state in menu:
            changed = list(chosen)
            changed[position] = state
            values.append(recurrence(tuple(changed)))
        replacement_rows.append(sorted(values))
    assert replacement_rows == [
        [1561, 1646, 1734, 1820, 1996],
        [1561, 1561, 1562, 1577, 1577],
        [1561, 1644, 1730, 1814, 1986],
    ]
    swaps = []
    for position in (0, 1):
        changed = list(chosen)
        changed[position], changed[position + 1] = (
            changed[position + 1], changed[position])
        swaps.append(recurrence(tuple(changed)))
    assert swaps == [1664, 1842]
    return chosen, len(words), len(minimizers), replacement_rows, swaps


def prefix_suffix(caps, cups, size, position):
    q = len(caps)
    left = 0
    all_caps = [1] + caps + [1]
    all_cups = [1] + cups + [1]
    all_sizes = [1] + [size] * q + [1]
    block = position + 1
    for h in range(block):
        middle = 1
        for k in range(h + 1, block):
            middle *= 1 + all_sizes[k]
        left += all_caps[h] * middle
    right = 0
    for j in range(block + 1, q + 2):
        middle = 1
        for k in range(block + 1, j):
            middle *= 1 + all_sizes[k]
        right += all_cups[j] * middle
    return left, right


def check_scalar_euler_ramps():
    cases = 0
    for q in range(2, 41):
        d = 2 ** 8  # Any D>1 works; 256 keeps exact integers compact.
        caps = [d ** (i + 2) for i in range(q)]
        cups = [d ** (q + 1 - i) for i in range(q)]
        for i in range(q):
            left, right = prefix_suffix(caps, cups, d, i)
            assert (right - left) * (caps[i] - cups[i]) <= 0
        for i in range(q - 1):
            left, _ = prefix_suffix(caps, cups, d, i)
            _, right = prefix_suffix(caps, cups, d, i + 1)
            delta = (d * left * (cups[i + 1] - cups[i])
                     + d * right * (caps[i] - caps[i + 1])
                     + caps[i] * cups[i + 1]
                     - caps[i + 1] * cups[i])
            assert delta < 0
        cases += 1
    return cases


def pocket_point(left, right):
    return ((left - right) / (left + right), -Q(2) / (left + right))


def inside(point, triangle):
    signs = [orient(triangle[i], triangle[(i + 1) % 3], point)
             for i in range(3)]
    return all(value > 0 for value in signs) or all(value < 0 for value in signs)


def check_planar_realization():
    epsilon = Q(1, 1000)
    seeds = [
        [(Q(i), -Q(i * i)) for i in range(4)],
        [(Q(0), Q(0)), (Q(1), Q(4)),
         (Q(2), Q(1)), (Q(4), Q(0))],
        [(Q(i), Q(i * i)) for i in range(4)],
    ]
    clusters = []
    for parameter, seed in zip((Q(4), Q(1), Q(1, 4)), seeds):
        cluster = []
        for first, transverse in seed:
            left = (1 / parameter + epsilon * first
                    + epsilon * epsilon * transverse)
            right = (parameter + epsilon * first
                     - epsilon * epsilon * transverse)
            cluster.append(pocket_point(left, right))
        clusters.append(cluster)
    guard_left = (Q(-1), Q(0))
    guard_right = (Q(1), Q(0))
    points = [guard_left] + sum(clusters, []) + [guard_right]
    assert all(orient(*triple) != 0 for triple in combinations(points, 3))

    transversals = 0
    blocked = 0
    for labels in product(range(4), repeat=3):
        face = [guard_left]
        face.extend(clusters[i][labels[i]] for i in range(3))
        face.append(guard_right)
        assert convex(face)
        transversals += 1
    for cluster in clusters:
        for outer, inner in combinations(range(4), 2):
            assert inside(cluster[inner], [cluster[outer], guard_left, guard_right])
            blocked += 1

    actual = 0
    for mask in range(1, 1 << len(points)):
        actual += convex([points[i] for i in range(len(points)) if mask >> i & 1])
    assert transversals == 64 and blocked == 18 and actual == 1561
    return transversals, blocked, actual


def main():
    menu = complete_menu()
    _, words, minimizers, _, swaps = check_finite_global_mutations(menu)
    ramps = check_scalar_euler_ramps()
    transversals, blocked, faces = check_planar_realization()
    print("PASS: complete four-point profiles=5; "
          f"wrapper words={words}, minimizers={minimizers}, swaps={swaps}; "
          f"scalar Euler ramps={ramps}; planar transversals={transversals}, "
          f"blocked pairs={blocked}, faces={faces}")


if __name__ == "__main__":
    main()
