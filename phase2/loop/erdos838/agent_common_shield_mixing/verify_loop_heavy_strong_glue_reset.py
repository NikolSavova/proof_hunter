#!/usr/bin/env python3
"""Exact checks for LOOP_HEAVY_STRONG_GLUE_RESET_AUDIT.md."""

from fractions import Fraction as F
from itertools import combinations, product


def orient(p, q, r):
    return ((q[0] - p[0]) * (r[1] - p[1])
            - (q[1] - p[1]) * (r[0] - p[0]))


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    def half(sequence):
        out = []
        for point in sequence:
            while len(out) >= 2 and orient(out[-2], out[-1], point) <= 0:
                out.pop()
            out.append(point)
        return out

    return half(points)[:-1] + half(reversed(points))[:-1]


def convex(points):
    return len(points) == len(set(points)) == len(hull(points))


def face_profile(points):
    profile = [0] * (len(points) + 1)
    for mask in range(1, 1 << len(points)):
        chosen = [points[i] for i in range(len(points)) if mask >> i & 1]
        if convex(chosen):
            profile[len(chosen)] += 1
    return profile


def inside_triangle(point, a, b, c):
    signs = (orient(a, b, point), orient(b, c, point),
             orient(c, a, point))
    return all(value > 0 for value in signs) or all(value < 0 for value in signs)


def audit_reset_algebra():
    """Exhaust the logarithmic reset implication on small integer states.

    The atoms are represented by endpoint logs (x_i,y_i).  The right-comb
    recurrence is weakened by dropping the nonnegative size increments;
    this can only decrease inherited endpoint coordinates.  We retain only
    states satisfying the theorem's root coordinate ceiling.
    """
    checked = 0
    for q in range(3, 7):
        for radial in range(3, 8):
            for ceiling_loss in range(1, 4):
                choices = [(x, y) for x in range(radial + 4)
                           for y in range(radial + 4)
                           if x + y >= radial]
                # Exhausting all q-tuples would be unnecessarily large.
                # Dynamic states keep (X,Y,M) and are exactly equivalent.
                states = {(x, y, 0) for x, y in choices}
                for _ in range(1, q):
                    next_states = set()
                    for x, y in choices:
                        for old_x, old_y, old_m in states:
                            # New atom is the left child, old suffix the right.
                            new_x = max(x, old_x)
                            new_y = max(y, old_y)
                            new_m = max(old_m, x + old_y)
                            next_states.add((new_x, new_y, new_m))
                    states = next_states
                for root_x, root_y, mu in states:
                    if root_x > mu + ceiling_loss or root_y > mu + ceiling_loss:
                        continue
                    # The proof splits at mu >= F-L.  In the complementary
                    # branch it yields (q+1)mu >= qF-2L.
                    assert (mu >= radial - ceiling_loss
                            or (q + 1) * mu >= q * radial - 2 * ceiling_loss)
                    checked += 1
    assert checked > 1000
    return checked


def audit_parameter_bounds():
    """Conditional arithmetic when a half-quadratic atom input is assumed."""
    square_root_cases = linear_cases = 0
    for ell in range(256, 4097):
        # Work directly with a certified lower bound log s >= L-B log L,
        # using integer B=3 and floor(log_2 L) <= log_2 L.
        log_l_floor = ell.bit_length() - 1
        log_s = ell - 3 * (log_l_floor + 1)
        assert log_s > 0
        f_twice = log_s * log_s - 6 * log_s  # 2F

        q_root = max(3, int(ell ** 0.5))
        # Twice the theorem's second lower bound.
        lower_twice = F(q_root, q_root + 1) * f_twice - F(4 * ell, q_root + 1)
        # A deliberately loose O(L^(3/2)) certificate.
        assert lower_twice >= ell * ell - 40 * ell * int(ell ** 0.5)
        square_root_cases += 1

        q_linear = max(3, ell // 5)
        lower_twice = F(q_linear, q_linear + 1) * f_twice - F(4 * ell, q_linear + 1)
        # A loose O(L log L) certificate.
        assert lower_twice >= ell * ell - 20 * ell * (log_l_floor + 1)
        linear_cases += 1
    return square_root_cases, linear_cases


def loop_regression():
    """Rational loop family with deliberately nonhomogeneous 2+1 seams."""
    h = 5
    delta = F(1, 100 * h * h)
    curve = [(F(2) - delta * t * t, -F(1, 5) + delta * t)
             for t in range(1, h + 1)]
    b = (F(4), F(0))
    a = (F(0), F(0))

    parameters = (F(-2, 10000), F(1, 10000), F(3, 10000))
    centers = [(r, F(4) + F(1, 10000) - r * r) for r in parameters]
    rho = F(1, 10 ** 9)
    offset_sets = (
        ((-3, -1), (0, 4), (4, -2)),
        ((-4, -2), (1, 5), (3, -3)),
        ((-5, -1), (-1, 6), (4, -4)),
    )
    clusters = []
    for center, offsets in zip(centers, offset_sets):
        clusters.append([
            (center[0] + rho * dx, center[1] + rho * dy)
            for dx, dy in offsets
        ])

    ambient = curve + [b, a] + sum(clusters, [])
    assert all(orient(*triple) != 0 for triple in combinations(ambient, 3))

    # Every blocker label gives every parabola triple its 3+1 loop.
    loop_count = 0
    for i, j, k in combinations(range(h), 3):
        for blocker in sum(clusters, []):
            assert inside_triangle(curve[j], curve[i], curve[k], blocker)
            loop_count += 1
    assert loop_count == 90

    # The macro source transversals survive all independent child rotations.
    transversal_count = 0
    for source in curve:
        for labels in product(range(3), repeat=3):
            chosen = [source, b]
            chosen.extend(clusters[i][labels[i]] for i in range(3))
            chosen.append(a)
            assert convex(chosen)
            transversal_count += 1
    assert transversal_count == h * 3 ** 3

    # In the natural left-to-right macro order, already the triples with two
    # labels in the left cluster and one in the right have both signs.
    seam_signs = []
    for left, right in zip(clusters, clusters[1:]):
        left_order = sorted(left)
        signs = {
            orient(left_order[i], left_order[j], point) > 0
            for i, j in combinations(range(3), 2)
            for point in right
        }
        assert signs == {False, True}
        seam_signs.append(len(signs))

    mixed_blocker_profile = face_profile(sum(clusters, []))
    mixed_ambient_profile = face_profile(ambient)

    # A comparison placement with coherent near-slope-10 child secants.
    # This is used only as a finite stress test; no extremal assertion is
    # inferred from the two face counts.
    transverse = ((0, 3, -1), (1, -2, 4), (-2, 5, 1))
    coherent = []
    for center, values in zip(centers, transverse):
        child = []
        for f, g in zip((-1, 0, 1), values):
            child.append((center[0] + rho * f,
                          center[1] + 10 * rho * f + rho * rho * g))
        coherent.append(child)
    coherent_ambient = curve + [b, a] + sum(coherent, [])
    assert all(orient(*triple) != 0
               for triple in combinations(coherent_ambient, 3))
    for left_index, right_index in combinations(range(3), 2):
        left, right = coherent[left_index], coherent[right_index]
        assert max(point[0] for point in left) < min(point[0] for point in right)
        left_order = sorted(left)
        right_order = sorted(right)
        first = {orient(left_order[i], left_order[j], point) > 0
                 for i, j in combinations(range(3), 2) for point in right}
        second = {orient(point, right_order[i], right_order[j]) > 0
                  for point in left for i, j in combinations(range(3), 2)}
        assert first == {False} and second == {True}
    assert all(inside_triangle(curve[j], curve[i], curve[k], blocker)
               for i, j, k in combinations(range(h), 3)
               for blocker in sum(coherent, []))
    assert all(convex([source, b]
                      + [coherent[i][labels[i]] for i in range(3)] + [a])
               for source in curve for labels in product(range(3), repeat=3))
    coherent_blocker_profile = face_profile(sum(coherent, []))
    coherent_ambient_profile = face_profile(coherent_ambient)

    return (loop_count, transversal_count, seam_signs,
            mixed_blocker_profile, mixed_ambient_profile,
            coherent_blocker_profile, coherent_ambient_profile)


def main():
    algebra = audit_reset_algebra()
    root_cases, linear_cases = audit_parameter_bounds()
    (loops, transversals, seams, mixed_blocker_profile, mixed_ambient_profile,
     coherent_blocker_profile, coherent_ambient_profile) = loop_regression()
    mixed_blocker = sum(mixed_blocker_profile)
    mixed_ambient = sum(mixed_ambient_profile)
    coherent_blocker = sum(coherent_blocker_profile)
    coherent_ambient = sum(coherent_ambient_profile)
    mixed_mean = F(sum(rank * count for rank, count in enumerate(mixed_ambient_profile)),
                   mixed_ambient)
    coherent_mean = F(
        sum(rank * count for rank, count in enumerate(coherent_ambient_profile)),
        coherent_ambient)
    print("PASS: reset states=%d; conditional half-input cases=%d+%d; loops=%d; "
          "singleton transversals=%d; adjacent mixed seams=%s; "
          "faces mixed/coherent blocker=%d/%d ambient=%d/%d; means=%s/%s"
          % (algebra, root_cases, linear_cases, loops, transversals, seams,
             mixed_blocker, coherent_blocker, mixed_ambient, coherent_ambient,
             mixed_mean, coherent_mean))


if __name__ == "__main__":
    main()
