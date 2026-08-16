#!/usr/bin/env python3
"""Checks for FERRERS_UPPER_JUMP_APPLICABILITY_GATE.md."""

from math import comb, log2


def fixed_three_wrapper_checks():
    coefficient = 0.31
    gains = []
    for L in (20, 40, 80, 160, 320, 640):
        alpha = log2(3) / L
        beta = 1 - alpha
        output = coefficient + (1 - 2 * coefficient) * alpha * beta
        gain = output - coefficient
        gains.append(gain)
        assert gain > 0
        assert gain <= (1 - 2 * coefficient) * log2(3) / L
    assert all(left > right for left, right in zip(gains, gains[1:]))
    assert gains[-1] < 0.001
    return gains


def profile_entropy_checks():
    theta = 0.4
    rows = []
    for L in (40, 50, 60, 80, 100, 140):
        labels = 2**L
        rank = int(theta * L)
        full_log = log2(comb(labels, rank))
        core = rank // 2
        common_core_log = log2(comb(labels - core, rank - core))
        disjoint_log_upper = log2(labels // rank)

        # A representative subquadratic thinning loss O(L log L).
        thinning_loss = L * log2(max(L, 2))
        assert full_log - thinning_loss > 0
        assert common_core_log - thinning_loss > 0
        assert disjoint_log_upper <= L
        assert disjoint_log_upper / (L * L) <= 1 / L

        rows.append(
            (
                L,
                full_log / (L * L),
                common_core_log / (L * L),
                thinning_loss / (L * L),
                disjoint_log_upper / (L * L),
            )
        )

    # Ratios approach theta and theta/2; the thinning coefficient vanishes.
    assert rows[-1][1] > 0.35
    assert rows[-1][2] > 0.15
    assert rows[-1][3] < rows[0][3]
    return rows


def reflected_skew_checks():
    for t in (10, 20, 40, 80):
        coefficient = 0.3
        log_weight = coefficient * t * t
        # Type A has (log C,log U)=(0,log W); type B is reflected.
        log_c_left = 0.0
        log_u_right = 0.0
        forward_log = log_c_left + log_u_right
        assert forward_log == 0
        delta = 0.5 * log_weight - min(log_c_left, log_u_right)
        assert abs(delta - 0.5 * coefficient * t * t) < 1e-12


def main():
    gains = fixed_three_wrapper_checks()
    rows = profile_entropy_checks()
    reflected_skew_checks()
    print("fixed-three gains:", " ".join(f"{value:.6g}" for value in gains))
    for L, full, core, thin, disjoint in rows:
        print(
            f"L={L:>3}: full/L^2={full:.6f}, "
            f"common-core/L^2={core:.6f}, thinning/L^2={thin:.6f}, "
            f"disjoint/L^2<={disjoint:.6f}"
        )
    print("reflected quadratic anti-alignment checked")
    print("all Ferrers/upper-jump applicability checks passed")


if __name__ == "__main__":
    main()
