#!/usr/bin/env python3
"""Exact/numerical verifier for the third-cloud KK terminal gate."""

from itertools import combinations
from math import comb, log2
from pathlib import Path
import random
import sys


ROOT = Path(__file__).resolve().parents[1]
COMMON = ROOT / "agent_common_shield_mixing"
sys.path.insert(0, str(COMMON))
import verify_dense_hall_two_cloud_profile_barrier as dense  # noqa: E402


def real_binom(x, q):
    answer = 1.0
    for i in range(q):
        answer *= (x - i) / (i + 1)
    return answer


def lovasz_parameter(size, q):
    lo, hi = float(q - 1), float(q)
    while real_binom(hi, q) < size:
        hi *= 2
    for _ in range(100):
        mid = (lo + hi) / 2
        if real_binom(mid, q) < size:
            lo = mid
        else:
            hi = mid
    return hi


def two_shadow(family):
    return {
        frozenset(edge)
        for face in family
        for edge in combinations(face, 2)
    }


def kk_small_audit():
    # Exhaust all nonempty triple families on five labels.
    triples = [frozenset(part) for part in combinations(range(5), 3)]
    checked = 0
    for mask in range(1, 1 << len(triples)):
        family = [triples[i] for i in range(len(triples)) if mask >> i & 1]
        x = lovasz_parameter(len(family), 3)
        shadow = two_shadow(family)
        assert len(shadow) + 1e-9 >= real_binom(x, 2)
        checked += 1

    # Random larger uniform families.
    rng = random.Random(8381519)
    for support, rank in ((8, 3), (9, 4), (10, 5)):
        layer = [frozenset(part)
                 for part in combinations(range(support), rank)]
        for _ in range(200):
            size = rng.randrange(1, len(layer) + 1)
            family = rng.sample(layer, size)
            x = lovasz_parameter(size, rank)
            assert len(two_shadow(family)) + 1e-7 >= real_binom(x, 2)
            checked += 1
    return checked


def threshold_audit():
    a = log2(3)
    theta = 2 - a
    kappa_star = 1 / a
    assert abs(theta - 0.4150374992788438) < 1e-14
    assert abs(kappa_star - 0.6309297535714574) < 1e-14

    # The KK exponent 1/kappa strictly beats a below the cutoff.
    for epsilon in (0.01, 0.03, 0.05, 0.1):
        kappa = kappa_star - epsilon
        assert 1 / kappa > a

    # The cross-singleton-pair rectangle has exactly theta spare powers.
    assert abs(2 - a - theta) < 1e-15

    # Audit the asymptotic lower exponent from (14) at increasing d.
    C = 3.0
    previous = None
    for d in (512, 1024, 2048, 4096, 8192):
        kappa = kappa_star - 0.05
        q = int(kappa * d)
        log_m = 0.5 * d * d - C * d * log2(d) - d
        lower_log_x = log_m / q + log2(q) - log2(2.718281828459045)
        exponent = 2 * lower_log_x / d
        if previous is not None:
            assert exponent > previous
        previous = exponent
    assert previous > a + 0.1
    return a, theta, kappa_star


def complement_induction_audit():
    C = 3.0

    def phi(d):
        return 0.5 * d * d - C * d * log2(d)

    # An o(R) deletion changes the target by o(log R).
    normalized = []
    for d in (64, 128, 256, 512, 1024):
        fraction = 1 / (log2(d) ** 2)
        d2 = d + log2(1 - fraction)
        gap = phi(d) - phi(d2)
        normalized.append(gap / d)
    assert all(normalized[i + 1] < normalized[i]
               for i in range(len(normalized) - 1))
    assert normalized[-1] < 0.02

    # A constant-density complement costs only a fixed power.
    for fraction in (0.1, 0.25, 0.5):
        d = 1024
        d2 = d + log2(1 - fraction)
        gap = phi(d) - phi(d2)
        assert 0 < gap < 3 * d

    # Fixed disjoint supports make the good-union decoder injective.
    support_s = frozenset(range(5))
    support_t = frozenset(range(5, 10))
    rows = [frozenset(part) for part in combinations(support_s, 2)]
    columns = [frozenset(part) for part in combinations(support_t, 3)]
    outputs = {row | column for row in rows for column in columns}
    assert len(outputs) == len(rows) * len(columns)
    return normalized[-1], len(outputs)


def canonical_cross_circuit(edge, face):
    union = tuple(sorted(set(edge) | set(face)))
    for part in combinations(union, 4):
        part = frozenset(part)
        ext = part & frozenset(edge)
        inside = part & frozenset(face)
        if not ext or not inside:
            continue
        if not dense.convex(tuple(part)):
            return part, len(ext), len(inside)
    raise AssertionError("bad union without cross circuit")


def three_cloud_saturation():
    size, rank = 5, 3
    first_block = dense.parabolic_cloud(dense.G0, 2 * size, 1)
    x1, x2 = first_block[:size], first_block[size:]
    x3 = dense.parabolic_cloud(dense.X0, size, -1)
    faces = [frozenset(part) for part in combinations(x3, rank)]

    whole = x1 + x2 + x3
    assert all(dense.orient(*triple) != 0
               for triple in combinations(whole, 3))
    assert all(dense.convex(face) for face in faces)
    assert all(dense.convex(part)
               for cloud in (x1, x2)
               for part in combinations(cloud, 3))

    types = {1: 0, 2: 0}
    outputs = set()
    for x in x1:
        for y in x2:
            for face in faces:
                candidate = frozenset([x, y]) | face
                assert not dense.convex(tuple(candidate))
                assert not dense.convex((x,) + tuple(face))
                assert not dense.convex((y,) + tuple(face))
                circuit, external, internal = canonical_cross_circuit(
                    frozenset([x, y]), face
                )
                assert external + internal == 4
                assert (external, internal) in ((1, 3), (2, 2))
                types[external] += 1
                outputs.add(candidate)

    records = size * size * comb(size, rank)
    assert len(outputs) == records == 250
    assert sum(types.values()) == records
    return records, types


def main():
    kk = kk_small_audit()
    constants = threshold_audit()
    complement = complement_induction_audit()
    records, types = three_cloud_saturation()
    print("PASS: third-cloud KK gate",
          f"kk_checks={kk}",
          f"a/theta/kappa={constants}",
          f"complement={complement}",
          f"parabolic_records={records}",
          f"circuit_types={types}")


if __name__ == "__main__":
    main()
