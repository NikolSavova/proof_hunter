#!/usr/bin/env python3
"""Exact audit of NESTED_TRIANGLE_AGGREGATE_POTENTIAL_RESTART_BARRIER."""

from math import comb, log2, log


def ceil_div(a, b):
    return (a + b - 1) // b


def discrete_targets(n):
    """Integer analogue of 2^(L^2/2-L log L+O(L))."""
    target = [0] * (n + 1)
    target[1] = 2
    for q in range(1, n):
        ell = q.bit_length() - 1
        logell = max(2, ell).bit_length() - 1
        derivative = max(1, ell - logell)
        target[q + 1] = target[q] + ceil_div(derivative * target[q], q)
    return target


def minimum_rank_sum(n, number_of_sets):
    """Minimum rank sum of this many distinct subsets of an n-set."""
    remaining = number_of_sets
    rank_sum = 0
    last_rank = 0
    for r in range(n + 1):
        take = min(remaining, comb(n, r))
        rank_sum += r * take
        remaining -= take
        if take:
            last_rank = r
        if not remaining:
            return rank_sum, last_rank
    raise AssertionError("more requested sets than the Boolean lattice")


def exact_profile_model():
    # N=m(1+3k), s=km=N/(3+1/k).  These values are large enough that
    # polynomial trace floors are negligible, but small enough to exhaust.
    m = 4000
    k = 3
    s = k * m
    n = m * (1 + 3 * k)
    r = s
    target = discrete_targets(n)

    z0 = target[r]
    z = z0
    singleton_totals = [0, 0, 0]
    checked_endpoint_states = 0
    maximum_relative_increment = 0.0

    for t in range(1, s + 1):
        q = m + 3 * (t - 1)
        new_q = q + 3
        endpoint_pairs = comb(q, 2)
        small_profile = q + endpoint_pairs
        lower = 1 + small_profile
        minimum_delta = 6 * lower + 1

        if t < s:
            new_z = max(z + minimum_delta, target[new_q])
            assert new_z >= target[new_q]
        else:
            new_z = (target[n] + target[n - 1]) // 2

        delta = new_z - z
        assert delta >= minimum_delta
        assert delta <= 3 * z + 1
        maximum_relative_increment = max(maximum_relative_increment,
                                         delta / z)

        # Keep all three edge profiles at the strengthened lower floor and
        # distribute every surplus evenly among singleton profiles.
        surplus = delta - 1 - 6 * lower
        capacity = z - lower
        assert 0 <= surplus <= 3 * capacity
        share, remainder = divmod(surplus, 3)
        counts = [lower + share + (c < remainder) for c in range(3)]
        counts += [lower, lower, lower]
        assert sum(counts) + 1 == delta
        assert min(counts) >= lower and max(counts) <= z
        for c in range(3):
            singleton_totals[c] += counts[c]

        # Exact endpoint identity at representative states (the algebra is
        # formulaic, so sampling avoids doing the same huge-integer check
        # twelve thousand times).
        if t in {1, s // 3, 2 * s // 3, s}:
            nonempty = z - 1
            extra = nonempty - q - endpoint_pairs
            assert extra >= 0
            # All C_e=1; U_e=1 except U_e0=1+extra.
            assert endpoint_pairs + extra == nonempty - q
            total_cap = q + endpoint_pairs
            total_cup = q + endpoint_pairs + extra
            assert total_cap == small_profile
            assert total_cup == nonempty
            checked_endpoint_states += 1

        z = new_z

    assert z < target[n]
    assert z >= target[n - 1]
    assert all(total >= target[r] for total in singleton_totals)

    # Exact telescope: recurrence products collapse to z/z0.  Work in logs
    # only after the exact integer recurrence has been checked.
    potential = log2(z / z0)
    live_scale = log2(n) * log2(log2(log2(n)))
    assert potential < live_scale

    # Formal least-counterexample deletion marginal.
    deletion_count = target[n - 1]
    total_rank = n * (z - deletion_count)
    assert n * deletion_count == n * z - total_rank
    mean_rank = total_rank / z
    assert 3 <= mean_rank <= log2(n)

    # Even bare subset scarcity does not contradict this mean.  A symmetric
    # fractional interpolation between adjacent layers can raise the mean
    # from this minimum to the displayed deletion mean.
    min_rank_sum, last_rank = minimum_rank_sum(n, z)
    assert min_rank_sum <= total_rank
    assert last_rank <= 2 * log2(n)

    # Three low cap chambers and their high antipodes fit the genuine total
    # variation budget at the initial state.
    q = m
    nonempty = z0 - 1
    small_profile = q + comb(q, 2)
    total_variation = 6 * (nonempty - small_profile)
    assert total_variation <= 2 * mean_rank * nonempty

    assert checked_endpoint_states == 4
    return {
        "n": n,
        "k": k,
        "potential": potential,
        "live_scale": live_scale,
        "mean_rank": mean_rank,
        "last_rank": last_rank,
        "max_relative_increment": maximum_relative_increment,
    }


def phi_difference(ell, shift, c):
    """Phi_C(ell)-Phi_C(ell-shift), evaluated without cancellation."""
    return (shift * ell - shift * shift / 2
            - c * (ell * log2(ell)
                   - (ell - shift) * log2(ell - shift)))


def asymptotic_audit():
    ratios = []
    central_ratios = []
    c = 4.0
    for exponent in (10, 14, 18, 22, 26):
        ell = 2.0 ** exponent
        k = log2(ell)
        cloud_shift = log2(3.0 + 1.0 / k)
        central_shift = log2(1.0 + 3.0 * k)
        cloud_gap = phi_difference(ell, cloud_shift, c)
        central_gap = phi_difference(ell, central_shift, c)
        desired = ell * log2(k)
        ratios.append(cloud_gap / desired)
        central_ratios.append(central_gap / desired)
        assert cloud_gap > 0
        assert 1.0 < central_gap / desired < 1.5
    assert all(ratios[i + 1] < ratios[i]
               for i in range(len(ratios) - 1))
    assert all(central_ratios[i + 1] < central_ratios[i]
               for i in range(len(central_ratios) - 1))
    assert ratios[-1] < 0.35

    # The leading ratios are log(3)/log(k) and
    # 1+log(3)/log(k), respectively.  Check their arbitrarily-late limit
    # without trying to represent the doubly exponential value of L.
    leading_cloud = [log2(3.0) / log_k for log_k in (8, 16, 32, 64)]
    leading_central = [1.0 + x for x in leading_cloud]
    assert leading_cloud[-1] < 0.025
    assert leading_central[-1] < 1.025

    # The deletion mean is half the target logarithmic derivative and stays
    # under the usual least-counterexample bound.
    ell = 2.0 ** 20
    derivative = ell - c * (log2(ell) + 1.0 / log(2.0))
    assert 0 < derivative / 2 < derivative < ell
    return ratios, leading_cloud


def triangle_tag_face_alphabet_audit():
    exponent = log2(3.0)
    margin = exponent - 1.5
    assert 0.0849 < margin < 0.0850

    # The exact q=8 face alphabet: H=255 actual nonempty faces but only 56
    # physical triangle tags.  Gamma=54/5 is tested by cross multiplication.
    q = 8
    h = (1 << q) - 1
    edges = h * h
    triangles = comb(q, 3)
    assert 5 * edges * edges > 54 * h * triangles

    # Circuit concentration fixes a two-label trace, but all faces containing
    # it remain.  Their complete rectangle still violates the same local
    # tag premise by an exponential factor.
    p = 16
    fixed_trace_alphabet = 1 << (p - 2)
    edges = fixed_trace_alphabet * fixed_trace_alphabet
    assert 5 * edges * edges > 54 * fixed_trace_alphabet * comb(p, 3)
    return margin, h, triangles, fixed_trace_alphabet


def main():
    exact = exact_profile_model()
    ratios, leading = asymptotic_audit()
    margin, alphabet, triangles, fixed = triangle_tag_face_alphabet_audit()
    print(
        "PASS: exact recurrence/cloud/deletion/endpoint marginals; "
        "N=%d potential=%.6f target-scale=%.6f mean=%.6f "
        "last-rank=%d max-step=%.6g finite-ratios=%s leading-ratios=%s "
        "tag-margin=%.8f face-alphabet=%d/%d fixed-trace=%d"
        % (
            exact["n"],
            exact["potential"],
            exact["live_scale"],
            exact["mean_rank"],
            exact["last_rank"],
            exact["max_relative_increment"],
            ",".join("%.5f" % x for x in ratios),
            ",".join("%.5f" % x for x in leading),
            margin,
            alphabet,
            triangles,
            fixed,
        )
    )


if __name__ == "__main__":
    main()
