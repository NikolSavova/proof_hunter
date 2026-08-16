#!/usr/bin/env python3
"""Exact scalar checks for COMMON_GUARD_PROFILE_RAMP_BARRIER.md."""

from fractions import Fraction as Q
from itertools import combinations, product


def recurrence_value(length, q):
    d = 2 ** length
    sizes = [1] + [d] * q + [1]
    caps = [1] + [d ** (i + 2) for i in range(q)] + [1]
    cups = [1] + [d ** (q + 1 - i) for i in range(q)] + [1]
    faces = [1] + [caps[i + 1] + cups[i + 1] for i in range(q)] + [1]
    total = sum(faces)
    largest_forward = 0
    largest_left_guard = 0
    largest_right_guard = 0
    for i in range(q + 2):
        middle = 1
        for j in range(i + 1, q + 2):
            term = caps[i] * cups[j] * middle
            total += term
            if 1 <= i < j <= q:
                largest_forward = max(largest_forward, term)
            elif i == 0 and j <= q:
                largest_left_guard = max(largest_left_guard, term)
            elif 1 <= i and j == q + 1:
                largest_right_guard = max(largest_right_guard, term)
            middle *= 1 + sizes[j]
    return (d, total, largest_forward, largest_left_guard,
            largest_right_guard, caps, cups)


def check_finite_ramp():
    last_ratio = None
    for length in range(16, 161, 4):
        q = length // 4
        (d, total, forward, left, right, caps, cups) = recurrence_value(
            length, q)
        assert all(caps[i + 1] * cups[i + 1] == d ** (q + 3)
                   for i in range(q))
        assert forward <= 2 * d ** (q + 2)
        assert left <= 2 * d ** (q + 1)
        assert right <= 2 * d ** (q + 1)
        assert d ** q <= total <= 4 * (q + 2) ** 2 * d ** (q + 3)
        # Rational sandwich for the normalized logarithmic exponent, using
        # only the certified monomial bounds rather than floating logs.
        lower = Q(q, length)
        upper = Q(q + 3, length) + Q(
            (4 * (q + 2) ** 2).bit_length(), length * length)
        assert lower <= Q(1, 4) <= upper
        last_ratio = (lower, upper)
    return last_ratio


def objective(alpha, c, xs):
    q = len(xs)
    ts = [alpha * Q(i, q - 1) if q > 1 else Q(0) for i in range(q)]
    ys = [xs[i] - ts[i] for i in range(q)]
    values = [alpha, c]
    values.extend(c + ys[i] - ys[j]
                  for i in range(q) for j in range(i + 1, q))
    values.extend(c - y for y in ys)
    values.extend(alpha + y for y in ys)
    return max(values)


def check_max_plus():
    # Exhaustive discrete audits in cases where the constant-y optimizer is
    # on the grid.  The universal lower bound max(alpha,c) is built into the
    # objective; the displayed optimizer attains it.
    checked = 0
    for denominator in (4, 6, 8):
        grid = [Q(i, denominator) for i in range(denominator + 1)]
        for alpha_units in range(1, denominator // 2 + 1):
            alpha = Q(alpha_units, denominator)
            for c_units in range(alpha_units, denominator + 1):
                c = Q(c_units, denominator)
                q = alpha_units + 1
                y = (c - alpha) / 2
                candidate = [alpha * Q(i, q - 1) + y for i in range(q)]
                assert all(0 <= x <= c for x in candidate)
                assert objective(alpha, c, candidate) == c

                # When the state space is small, exhaust every grid profile
                # and confirm that none beats max(alpha,c)=c.
                allowed = [x for x in grid if x <= c]
                if len(allowed) ** q <= 200000:
                    optimum = min(objective(alpha, c, xs)
                                  for xs in product(allowed, repeat=q))
                    assert optimum >= c
                checked += 1
    return checked


def check_ambient_child_barrier():
    # Finite integer shadow of Theorem 2: for q subpolynomial blocks, the
    # largest child loses only log(q) from the parent logarithmic size.
    checked = 0
    for exponent in range(20, 241, 20):
        parent = 2 ** exponent
        q = exponent ** 3
        child = (parent + q - 1) // q
        assert q * child >= parent
        # q=poly(log N), so the fractional logarithmic loss tends to zero.
        loss_bound = q.bit_length()
        assert child >= 2 ** (exponent - loss_bound)
        ratio_lower = Q((exponent - loss_bound) ** 2, exponent ** 2)
        assert ratio_lower > 0
        if exponent >= 120:
            assert ratio_lower > Q(1, 2)
        checked += 1
    return checked


def orientation(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for point in points:
        while (len(lower) >= 2
               and orientation(lower[-2], lower[-1], point) <= 0):
            lower.pop()
        lower.append(point)
    upper = []
    for point in reversed(points):
        while (len(upper) >= 2
               and orientation(upper[-2], upper[-1], point) <= 0):
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def convex(points):
    return len(set(points)) == len(hull(points))


def pocket_point(left, right):
    return ((left - right) / (left + right), -Q(2) / (left + right))


def strictly_inside(point, triangle):
    signs = [orientation(triangle[i], triangle[(i + 1) % 3], point)
             for i in range(3)]
    return all(value > 0 for value in signs) or all(value < 0 for value in signs)


def check_exact_planar_wrapper():
    # Three arbitrary four-point children.  The seed has one nonconvex
    # four-set; the projective pocket map preserves this order type while
    # its common first-order coordinate makes every pair guard-nested.
    seed = [(Q(0), Q(0)), (Q(1), Q(4)),
            (Q(2), Q(1)), (Q(4), Q(0))]
    epsilon = Q(1, 1000)
    clusters = []
    for parameter in (Q(4), Q(1), Q(1, 4)):
        cluster = []
        for first, transverse in seed:
            left = (Q(1) / parameter + epsilon * first
                    + epsilon * epsilon * transverse)
            right = (parameter + epsilon * first
                     - epsilon * epsilon * transverse)
            cluster.append(pocket_point(left, right))
        clusters.append(cluster)

    guard_left = (Q(-1), Q(0))
    guard_right = (Q(1), Q(0))
    points = [guard_left] + sum(clusters, []) + [guard_right]
    assert all(orientation(*triple) != 0 for triple in combinations(points, 3))

    transversals = 0
    for labels in product(range(4), repeat=3):
        face = [guard_left]
        face.extend(clusters[i][labels[i]] for i in range(3))
        face.append(guard_right)
        assert convex(face)
        transversals += 1
    assert transversals == 64

    blocked_pairs = 0
    for cluster in clusters:
        for outer, inner in combinations(range(4), 2):
            triangle = [cluster[outer], guard_left, guard_right]
            assert strictly_inside(cluster[inner], triangle)
            assert not convex([cluster[outer], cluster[inner],
                               guard_left, guard_right])
            blocked_pairs += 1
    assert blocked_pairs == 18

    local_faces = []
    positive_caps = []
    negative_caps = []
    for cluster in clusters:
        faces = caps_plus = caps_minus = 0
        for mask in range(1, 1 << 4):
            trace = [cluster[i] for i in range(4) if mask >> i & 1]
            faces += convex(trace)
            indices = [i for i in range(4) if mask >> i & 1]
            caps_plus += all(orientation(cluster[i], cluster[j], cluster[k]) > 0
                             for i, j, k in combinations(indices, 3))
            caps_minus += all(orientation(cluster[i], cluster[j], cluster[k]) < 0
                              for i, j, k in combinations(indices, 3))
        local_faces.append(faces)
        positive_caps.append(caps_plus)
        negative_caps.append(caps_minus)
    assert local_faces == [14, 14, 14]
    assert positive_caps == [13, 13, 13]
    assert negative_caps == [11, 11, 11]

    actual = 0
    for mask in range(1, 1 << len(points)):
        actual += convex([points[i] for i in range(len(points)) if mask >> i & 1])

    sizes = [1, 4, 4, 4, 1]
    caps = [1] + positive_caps + [1]
    cups = [1] + negative_caps + [1]
    faces = [1] + local_faces + [1]
    predicted = sum(faces)
    for i in range(5):
        middle = 1
        for j in range(i + 1, 5):
            predicted += caps[i] * cups[j] * middle
            middle *= 1 + sizes[j]
    assert actual == predicted == 1914
    return transversals, blocked_pairs, actual


def main():
    transversals, blocked, planar_faces = check_exact_planar_wrapper()
    lower, upper = check_finite_ramp()
    checked = check_max_plus()
    ambient = check_ambient_child_barrier()
    print("PASS: finite ramps L=16..160; final coefficient sandwich "
          f"[{lower}, {upper}]; max-plus parameter cases={checked}; "
          f"ambient-child cases={ambient}; planar transversals={transversals}, "
          f"blocked pairs={blocked}, faces={planar_faces}; "
          "quarter scalar fixed point exact, "
          "recursive half barrier exact")


if __name__ == "__main__":
    main()
