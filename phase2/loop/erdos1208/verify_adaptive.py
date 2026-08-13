#!/usr/bin/env python3
"""High-precision certificate for the adaptive-modulus Erdős 1208 bound."""

from decimal import Decimal, getcontext

getcontext().prec = 80

ALPHA = Decimal(24913) / Decimal(50000)
D = Decimal(58644190679703485491635)
Q = [
    1133681, 2184101, 7932209, 8869649, 16145221, 25584389,
    30529061, 30589961, 43030381, 46633109, 47039849, 48473881,
    50266061, 50726381, 53683769, 58553249, 63169721, 71960489,
    78749789, 78827381, 85124441, 93586249, 93656741, 94521041,
    97978981, 98291969, 105702341, 112129709, 113626301, 118676549,
    147493369, 151475561, 151562629, 162387749, 163384621, 165163909,
    167300129, 169920869, 170390321, 175244281, 177916909, 184204121,
    188980601, 191165729, 192945749, 196193609, 196650341,
]

# Each row is (safe left endpoint, safe right endpoint, 47 depths).
ROWS = [
    ("4024.0", "4045.4", [6, 6] + [5] * 31 + [4] * 14),
    ("4043.0", "4071.6", [6, 6] + [5] * 32 + [4] * 13),
    ("4061.9", "4097.8", [6, 6] + [5] * 33 + [4] * 12),
    ("4080.9", "4124.0", [6, 6] + [5] * 34 + [4] * 11),
    ("4118.9", "4176.4", [6, 6] + [5] * 36 + [4] * 9),
    ("4176.1", "4255.0", [6, 6] + [5] * 39 + [4] * 6),
    ("4252.6", "4359.8", [6, 6] + [5] * 43 + [4] * 2),
    ("4353.5", "4497.8", [7] + [6] * 4 + [5] * 42),
    ("4490.7", "4672.0", [7, 7] + [6] * 10 + [5] * 35),
    ("4671.6", "4893.5", [7, 7] + [6] * 20 + [5] * 25),
    ("4892.4", "5156.3", [7, 7, 7] + [6] * 30 + [5] * 14),
    ("5151.0", "5458.2", [8, 7, 7, 7] + [6] * 41 + [5] * 2),
    ("5450.8", "5788.0", [8, 8] + [7] * 16 + [6] * 29),
    ("5774.9", "6124.8", [9, 8, 8, 8] + [7] * 29 + [6] * 14),
    ("6124.8", "6476.2", [9, 9] + [8] * 6 + [7] * 39),
    ("6459.3", "6790.9", [10] + [9] * 3 + [8] * 20 + [7] * 23),
    ("6772.6", "7073.6", [10, 10] + [9] * 3 + [8] * 34 + [7] * 8),
    ("7062.1", "7327.5", [11, 10] + [9] * 10 + [8] * 35),
    ("7326.4", "7549.0", [11, 11] + [10] * 2 + [9] * 20 + [8] * 23),
    ("7544.0", "7725.6", [12, 11] + [10] * 3 + [9] * 29 + [8] * 13),
    ("7715.4", "7861.8", [12, 11] + [10] * 3 + [9] * 38 + [8] * 4),
    ("7859.6", "7976.0", [12] + [11] * 2 + [10] * 5 + [9] * 39),
    ("7961.2", "8054.7", [12, 12] + [11] * 2 + [10] * 8 + [9] * 35),
]


def invariants(depths):
    assert len(depths) == len(Q) == 47
    log_m = sum(Decimal(k) * Decimal(q).ln() for q, k in zip(Q, depths))
    log_h = sum(Decimal(k + 1).ln() for k in depths)
    log_lambda = sum(
        sum(Decimal(q) ** Decimal(-e) for e in range(k + 1)).ln()
        for q, k in zip(Q, depths)
    )
    return log_m, log_h, log_lambda


def main():
    previous_right = None
    for index, (left_s, right_s, depths) in enumerate(ROWS, 1):
        left, right = Decimal(left_s), Decimal(right_s)
        log_m, log_h, log_lambda = invariants(depths)

        # First term: M^m <= n^ALPHA throughout the interval.
        assert log_m / (2 * left) < ALPHA

        # Let C(w)=log(D Lambda/H)+log(4+exp(2(log M-w))/D).
        # The second exponent is 1/2+C(w)/(4w).  The function
        # C(w)-(4*ALPHA-2)w is increasing on this interval: its
        # derivative is 2-4*ALPHA-2z/(4+z), and the z bound below
        # is a stronger sufficient condition for positivity.
        z_left = (2 * (log_m - left)).exp() / D
        assert z_left / 2 < 2 - 4 * ALPHA
        z_right = (2 * (log_m - right)).exp() / D
        c_right = D.ln() + log_lambda - log_h + (Decimal(4) + z_right).ln()
        assert c_right < (4 * ALPHA - 2) * right

        # The same z bound is <1, so R>=M throughout the interval.
        assert z_left < 1

        if previous_right is not None:
            assert left <= previous_right
            assert right >= previous_right
        previous_right = right
        print(
            index,
            left,
            right,
            "margin1",
            ALPHA - log_m / (2 * left),
            "margin2",
            (4 * ALPHA - 2) * right - c_right,
        )

    w0 = Decimal(ROWS[0][0])
    assert Decimal(ROWS[-1][1]) > 2 * w0
    print("covered:", w0, 2 * w0)
    print("certified exponent:", ALPHA)


if __name__ == "__main__":
    main()
