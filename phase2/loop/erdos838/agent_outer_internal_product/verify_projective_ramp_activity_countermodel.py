#!/usr/bin/env python3
"""Exact verifier for PROJECTIVE_RAMP_ACTIVITY_COUNTERMODEL.md."""


def model(q, L):
    B = q * L + 2
    H = L + 2
    T = B + q * H + q * L + 4

    landmarks = []
    for i in range(q):
        landmarks.append((i * T, L * i, ("assembly", i)))
        for s in range(q + 1):
            landmarks.append((i * T + B + s * H, L * s,
                              ("calibration", i, s)))
    landmarks.sort()

    length = landmarks[-1][0] + 1
    exponent = [None] * length
    for index in range(len(landmarks) - 1):
        position, value, _ = landmarks[index]
        next_position, next_value, _ = landmarks[index + 1]
        exponent[position] = value
        current = value
        for place in range(position + 1, next_position + 1):
            current += (current < next_value) - (current > next_value)
            exponent[place] = current

    assert all(value is not None for value in exponent)
    assert exponent[0] == 0
    assert exponent[-1] == q * L

    cyclic = exponent + [q * L - value for value in exponent]
    return B, H, T, landmarks, exponent, cyclic


def components(indicator):
    return sum(indicator[i] and not indicator[i - 1]
               for i in range(len(indicator)))


def verify(q, L):
    B, H, T, landmarks, exponent, cyclic = model(q, L)
    D = 2 ** L
    V = D ** q
    half = len(exponent)

    # The exponent word is cyclic and every wall changes C,U by at most two.
    assert max(abs(cyclic[(i + 1) % len(cyclic)] - cyclic[i])
               for i in range(len(cyclic))) <= 1
    counts = [2 ** value for value in cyclic]
    cups = counts[half:] + counts[:half]
    assert all(c * u == V for c, u in zip(counts, cups))
    assert all(max(counts[(i + 1) % len(counts)], counts[i])
               <= 2 * min(counts[(i + 1) % len(counts)], counts[i])
               for i in range(len(counts)))

    # phi_i(t)=t+iT calibrates all q+1 reset levels and spreads at assembly.
    assembly = 0
    for i in range(q):
        image = assembly + i * T
        assert counts[image] == D ** i
        assert cups[image] == D ** (q - i)
        for s in range(q + 1):
            image = B + s * H + i * T
            assert counts[image] == D ** s
            assert cups[image] == D ** (q - s)

    # Every nontrivial superlevel activity has exactly 2q-1 components.
    for threshold_exponent in range(1, q * L + 1):
        active = [value >= threshold_exponent for value in cyclic]
        assert components(active) == 2 * q - 1

    # Exact saturation of TV(C) <= 2 mu V for formal rank 2q-1.
    total_variation = sum(abs(counts[(i + 1) % len(counts)] - counts[i])
                          for i in range(len(counts)))
    rank_mass = (V - 1) * (2 * q - 1)
    assert total_variation == 2 * rank_mass


def main():
    for q in range(2, 10):
        for L in range(1, 6):
            verify(q, L)
    print("PASS: translated ramps calibrate and spread; CU=V; wall ratio<=2; "
          "components=2q-1; TV=2 mu V")


if __name__ == "__main__":
    main()
