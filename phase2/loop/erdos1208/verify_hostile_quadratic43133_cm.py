#!/usr/bin/env python3
"""Independent exact audit of the Q(sqrt(43133)) CM candidate."""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
from math import isqrt


getcontext().prec = 100

FIELD_DISCRIMINANT = 43_133
OMEGA_CONSTANT = (FIELD_DISCRIMINANT - 1) // 4
RAMIFIED_COUNT = 223
GENERATOR_RANK = 221
USEFUL_COUNT = 11_765
ALPHA = Decimal("0.49369772")
W0 = Decimal("42282.8215")
EPSILON = Decimal("1e-25")
C_FRACTION = Fraction(71_603, 64_935)
C_UPPER = Decimal(C_FRACTION.numerator) / Decimal(C_FRACTION.denominator)

FUNDAMENTAL_UNIT = (11_516_800_325_138_112_653, 111_443_097_178_087_930)

# For every split rational prime occurring in the audited 223-ideal prefix
# (plus the neighboring 231-ideal cross-check), one
# exact generator a+b*omega of a prime above p.  The conjugate generates the
# other prime.  These are checked by norm and residue root below.
PRINCIPAL_GENERATORS: dict[int, tuple[int, int]] = {
    13: (420397, 4068),
    17: (-313, 3),
    23: (33590113, 325037),
    37: (-76483, 733),
    41: (7617, -73),
    43: (6867923, -65821),
    47: (298368427, -2859512),
    53: (3942386234, 38148767),
    59: (1215625773, 11763085),
    71: (-104, 1),
    89: (-17149528862, 164358153),
    97: (-3965, 38),
    101: (34103, 330),
    103: (-42050, 403),
    107: (13042784475, 126209386),
    109: (-3617, -35),
    131: (209, -2),
    137: (104, 1),
    151: (27047227, -259216),
    157: (6381705, 61753),
    167: (-1511134688, -14622597),
    173: (-329099028, -3184549),
    179: (-347982, 3335),
    181: (5158012007, 49911852),
    191: (-929020431, 8903573),
    197: (9188458860, -88060619),
    223: (-26816, 257),
    227: (496147, 4801),
    229: (-624607943, -6044061),
    233: (117397, 1136),
    239: (20179304, -193395),
    241: (13183807, 127574),
    263: (19015, 184),
    269: (-7292388, 69889),
    271: (-271499, 2602),
    277: (-103, 1),
    281: (-3339, 32),
    283: (40392215, 390858),
    307: (-413, -4),
    331: (-6018993, 57685),
    337: (-4278, 41),
    347: (-106, 1),
    349: (-230538127, 2209438),
    379: (-109853, -1063),
    389: (-49667, 476),
    397: (-11161, -108),
    401: (-93968237, -909290),
    419: (-3026, 29),
    421: (-765044, -7403),
    431: (-196622977, 1884401),
    433: (827, 8),
    439: (-366198727, 3509586),
    457: (-127558350, -1234327),
    467: (-162707827, 1559364),
    479: (-5594528, 53617),
    487: (-1824125712, 17482109),
    503: (-6669146695, -64534449),
    521: (-7716853, 73957),
    523: (-2713, 26),
    541: (-577431, 5534),
    547: (2135742631, 20666658),
    569: (73982328, 715895),
    577: (-723, -7),
    593: (-2400, 23),
    599: (1447, 14),
    601: (-5170063, 49549),
    607: (-311, -3),
    631: (1757, 17),
    641: (1757338, 17005),
    661: (22143182716, 214270005),
    677: (15547, -149),
    683: (-101, 1),
    709: (160583, -1539),
    727: (2177735, 21073),
    739: (-521, 5),
    751: (-400113877, 3834623),
    757: (-57284, 549),
    773: (-108, 1),
    787: (2598132, 25141),
    797: (-6924, -67),
    809: (14396382719, -137972471),
    811: (-3896668, 37345),
    821: (3018529, 29209),
    823: (-46773920, -452611),
    829: (-3472203, 33277),
    839: (-19754839, 189327),
    877: (731, -7),
    881: (-1033, -10),
    883: (-100, 1),
    887: (1544724801, 14947634),
    907: (-37912727652, -366865073),
    919: (-4904, 47),
    929: (-653914, 6267),
    937: (-613544, -5937),
    967: (-209, -2),
    971: (14921, -143),
    983: (-1605838, -15539),
    991: (852936632, 8253499),
    1009: (30781, -295),
    1013: (-45574, -441),
    1021: (3351368404, 32429743),
    1033: (-73098694843, -707344464),
    1039: (-20826703, -201531),
    1061: (54518919, -522500),
    1087: (-56656510445, 542986311),
    1103: (-8565783, 82093),
    1109: (-434029027, 4159660),
    1163: (490247491, 4743913),
    1187: (-1120429, 10738),
    1201: (691788169, 6694135),
    1249: (1426361, -13670),
    1259: (-308, -3),
}


def prime_sieve(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            count = (limit - p * p) // p + 1
            sieve[p * p : limit + 1 : p] = b"\x00" * count
    return [n for n in range(2, limit + 1) if sieve[n]]


def gf2_rank(rows: list[int]) -> int:
    pivots: dict[int, int] = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def norm(element: tuple[int, int]) -> int:
    a, b = element
    return a * a + a * b - OMEGA_CONSTANT * b * b


def conjugate(element: tuple[int, int]) -> tuple[int, int]:
    a, b = element
    return a + b, -b


def multiply(
    left: tuple[int, int], right: tuple[int, int]
) -> tuple[int, int]:
    a, b = left
    x, y = right
    return a * x + OMEGA_CONSTANT * b * y, a * y + b * x + b * y


def negative_at_embedding(element: tuple[int, int], conjugate_place: bool) -> int:
    a, b = element
    rational_part = 2 * a + b
    radical_part = -b if conjugate_place else b
    if rational_part >= 0 and radical_part >= 0:
        return 0
    if rational_part <= 0 and radical_part <= 0:
        return 1
    rational_square = rational_part * rational_part
    radical_square = radical_part * radical_part * FIELD_DISCRIMINANT
    assert rational_square != radical_square
    if rational_part > 0:
        return int(rational_square < radical_square)
    return int(radical_square < rational_square)


def tonelli_shanks(value: int, p: int) -> int:
    value %= p
    assert value and pow(value, (p - 1) // 2, p) == 1
    if p % 4 == 3:
        return pow(value, (p + 1) // 4, p)
    odd_part = p - 1
    power_of_two = 0
    while odd_part % 2 == 0:
        power_of_two += 1
        odd_part //= 2
    nonresidue = 2
    while pow(nonresidue, (p - 1) // 2, p) != p - 1:
        nonresidue += 1
    m = power_of_two
    c = pow(nonresidue, odd_part, p)
    t = pow(value, odd_part, p)
    root = pow(value, (odd_part + 1) // 2, p)
    while t != 1:
        i = 1
        test = t * t % p
        while test != 1:
            test = test * test % p
            i += 1
        multiplier = pow(c, 1 << (m - i - 1), p)
        root = root * multiplier % p
        t = t * multiplier * multiplier % p
        c = multiplier * multiplier % p
        m = i
    assert root * root % p == value
    return root


def prime_ideals(primes: list[int], norm_limit: int):
    ideals: list[tuple[int, int, str, int | None]] = []
    for p in primes:
        if p == 2 or p > norm_limit:
            continue
        if FIELD_DISCRIMINANT % p == 0:
            ideals.append((p, p, "ramified", None))
            continue
        symbol = pow(FIELD_DISCRIMINANT % p, (p - 1) // 2, p)
        if symbol == 1:
            square_root = tonelli_shanks(FIELD_DISCRIMINANT, p)
            inverse_two = (p + 1) // 2
            roots = sorted(
                {
                    (1 + square_root) * inverse_two % p,
                    (1 - square_root) * inverse_two % p,
                }
            )
            assert len(roots) == 2
            ideals.extend((p, p, "split", root) for root in roots)
        else:
            assert symbol == p - 1
            if p * p <= norm_limit:
                ideals.append((p * p, p, "inert", None))
    ideals.sort(
        key=lambda row: (
            row[0],
            row[1],
            row[2],
            row[3] if row[3] is not None else -1,
        )
    )
    return ideals


def local_increment(norm_q: int, depth: int) -> Decimal:
    q = Decimal(norm_q)
    t = Decimal(1) / (q * q)
    power = Decimal(1)
    total = Decimal(1)
    previous_total = Decimal(1)
    for _ in range(1, depth + 1):
        previous_total = total
        power *= t
        total += power
    current = Decimal(depth + 1) / total
    previous = Decimal(depth) / previous_total
    return (current / previous).ln() / 4


def main() -> None:
    # Field, integral basis, and safe CM constant.
    primes = prime_sieve(300_000)
    assert 1 + 4 * OMEGA_CONSTANT == FIELD_DISCRIMINANT
    assert FIELD_DISCRIMINANT % 8 == 5
    assert all(
        FIELD_DISCRIMINANT % p
        for p in primes
        if p * p <= FIELD_DISCRIMINANT
    )
    sqrt_three_upper = Fraction(1_351, 780)
    assert sqrt_three_upper**2 > 3
    x = Fraction(1, 5)
    atan_fifth_lower = sum(
        (-1) ** j * x ** (2 * j + 1) / (2 * j + 1) for j in range(4)
    )
    pi_lower = 16 * atan_fifth_lower - 4 * Fraction(1, 239)
    assert pi_lower > Fraction(333, 106)
    assert 2 * sqrt_three_upper / Fraction(333, 106) == C_FRACTION

    # Minkowski gives a representative of norm <104 in every ideal class.
    # The dyadic and inert small ideals are rational principal ideals; every
    # split prime ideal below 104 is generated by a checked certificate.
    assert FIELD_DISCRIMINANT < 208 * 208
    small_split_primes = [13, 17, 23, 37, 41, 43, 47, 53, 59, 71, 89, 97, 101, 103]
    assert all(abs(norm(PRINCIPAL_GENERATORS[p])) == p for p in small_split_primes)
    small_odd_ideals = [
        (row[0], row[1], row[2])
        for row in prime_ideals(primes, 103)
    ]
    assert {(q, p) for q, p, _ in small_odd_ideals} == {
        (9, 3), (13, 13), (17, 17), (23, 23), (25, 5),
        (37, 37), (41, 41), (43, 43), (47, 47), (49, 7),
        (53, 53), (59, 59), (71, 71), (89, 89), (97, 97),
        (101, 101), (103, 103),
    }
    for p in small_split_primes:
        assert sum(1 for q, rational, kind in small_odd_ideals if q == p and rational == p and kind == "split") == 2
    for p in (3, 5, 7):
        assert sum(1 for q, rational, kind in small_odd_ideals if q == p * p and rational == p and kind == "inert") == 1

    assert norm(FUNDAMENTAL_UNIT) == -1
    assert negative_at_embedding(FUNDAMENTAL_UNIT, False) == 0
    assert negative_at_embedding(FUNDAMENTAL_UNIT, True) == 1
    signature_rows = [0b11, 0b10]  # -1 and the displayed norm-minus-one unit
    assert gf2_rank(signature_rows) == 2

    ideals = prime_ideals(primes, 300_000)
    ramified = ideals[:RAMIFIED_COUNT]
    assert ramified[-1] == (1_163, 1_163, "split", 646)

    ramified_generators: list[tuple[int, int]] = []
    used_split_primes: set[int] = set()
    for norm_q, p, kind, root in ramified:
        if kind == "inert":
            generator = (p, 0)
        else:
            assert kind == "split" and root is not None
            used_split_primes.add(p)
            first = PRINCIPAL_GENERATORS[p]
            second = conjugate(first)
            generator = first if (first[0] + first[1] * root) % p == 0 else second
            assert (generator[0] + generator[1] * root) % p == 0
        assert abs(norm(generator)) == norm_q
        ramified_generators.append(generator)
    assert len(used_split_primes) == 108
    assert used_split_primes.issubset(PRINCIPAL_GENERATORS)

    # Exact sign and square-mod-4 constraints.
    units_mod_four = [
        (a, b)
        for a in range(4)
        for b in range(4)
        if norm((a, b)) % 2
    ]

    def multiply_mod_four(
        left: tuple[int, int], right: tuple[int, int]
    ) -> tuple[int, int]:
        product = multiply(left, right)
        return product[0] % 4, product[1] % 4

    squares = frozenset(multiply_mod_four(u, u) for u in units_mod_four)
    cosets: list[frozenset[tuple[int, int]]] = []
    for unit in units_mod_four:
        coset = frozenset(multiply_mod_four(unit, square) for square in squares)
        if coset not in cosets:
            cosets.append(coset)
    assert len(units_mod_four) == 12 and len(squares) == 3 and len(cosets) == 4

    def coset_index(element: tuple[int, int]) -> int:
        residue = element[0] % 4, element[1] % 4
        return next(i for i, coset in enumerate(cosets) if residue in coset)

    identity = cosets.index(squares)
    nonidentity = [i for i in range(4) if i != identity]
    bits = {identity: 0, nonidentity[0]: 1, nonidentity[1]: 2}
    representatives = [next(iter(coset)) for coset in cosets]
    last = coset_index(
        multiply_mod_four(
            representatives[nonidentity[0]], representatives[nonidentity[1]]
        )
    )
    assert last == nonidentity[2]
    bits[last] = 3
    for left in units_mod_four:
        for right in units_mod_four:
            assert bits[coset_index(multiply_mod_four(left, right))] == (
                bits[coset_index(left)] ^ bits[coset_index(right)]
            )

    def constraint_column(element: tuple[int, int]) -> int:
        signs = negative_at_embedding(element, False)
        signs |= negative_at_embedding(element, True) << 1
        return signs | (bits[coset_index(element)] << 2)

    kummer_generators = [(-1, 0), FUNDAMENTAL_UNIT] + ramified_generators
    columns = [constraint_column(element) for element in kummer_generators]
    constraint_rows = [
        sum(
            ((column >> bit) & 1) << index
            for index, column in enumerate(columns)
        )
        for bit in range(4)
    ]
    constraint_rank = gf2_rank(constraint_rows)
    assert len(columns) == 225
    assert constraint_rank == 4
    assert len(columns) - constraint_rank == GENERATOR_RANK

    def frobenius_functional(
        ideal: tuple[int, int, str, int | None]
    ) -> int:
        norm_q, p, kind, root = ideal
        assert norm_q == p and kind in ("split", "ramified")
        if kind == "ramified":
            assert p == FIELD_DISCRIMINANT
            root = (p + 1) // 2
        assert root is not None
        functional = 0
        for index, (a, b) in enumerate(kummer_generators):
            residue = (a + b * root) % p
            assert residue
            if pow(residue, (p - 1) // 2, p) == p - 1:
                functional |= 1 << index
        return functional

    useful: list[tuple[int, int, str, int | None]] = []
    rejected: list[tuple[int, int, str, int | None]] = []
    base_ideal_position: int | None = None
    for ideal in ideals[RAMIFIED_COUNT:]:
        norm_q, p, _, _ = ideal
        eligible = True
        if norm_q % 3 == 2:
            functional = frobenius_functional(ideal)
            eligible = gf2_rank(constraint_rows + [functional]) > constraint_rank
        else:
            assert norm_q % 3 == 1
        if eligible:
            if p == FIELD_DISCRIMINANT:
                base_ideal_position = len(useful)
            useful.append(ideal)
        else:
            rejected.append(ideal)
        if len(useful) == USEFUL_COUNT:
            break
    assert not rejected
    assert base_ideal_position == 4_190
    assert useful[-1] == (129_629, 129_629, "split", 2_193)

    relation_bound = (GENERATOR_RANK + 1) + RAMIFIED_COUNT + USEFUL_COUNT
    assert relation_bound == 12_210
    assert 4 * relation_bound == GENERATOR_RANK**2 - 1

    log_root_discriminant = Decimal(FIELD_DISCRIMINANT).ln() / 2
    for norm_q, _, _, _ in ramified:
        log_root_discriminant += Decimal(norm_q).ln() / 4

    increments: list[tuple[Decimal, Decimal, Decimal, int, int, int]] = []
    maximum_fourth_slope = Decimal(0)
    for ideal_index, (norm_q, _, _, _) in enumerate(useful):
        cost = Decimal(norm_q).ln() / 2
        previous: Decimal | None = None
        for depth in range(1, 5):
            gain = local_increment(norm_q, depth)
            if previous is not None:
                assert previous > gain
            previous = gain
            slope = gain / cost
            if depth <= 3:
                increments.append((slope, cost, gain, norm_q, depth, ideal_index))
            else:
                maximum_fourth_slope = max(maximum_fourth_slope, slope)
    increments.sort(reverse=True)
    seen = {index: 0 for index in range(USEFUL_COUNT)}
    for _, _, _, _, depth, ideal_index in increments:
        assert depth == seen[ideal_index] + 1
        seen[ideal_index] = depth

    def envelope(target: Decimal) -> tuple[Decimal, int, Decimal, Decimal]:
        cost_sum = Decimal(0)
        gain_sum = Decimal(0)
        for index, (slope, cost, gain, _, _, _) in enumerate(increments):
            if cost_sum + cost >= target:
                fraction = (target - cost_sum) / cost
                assert 0 <= fraction <= 1
                return gain_sum + fraction * gain, index, fraction, slope
            cost_sum += cost
            gain_sum += gain
        raise AssertionError("target exceeds frontier")

    def rhs(alpha: Decimal, w: Decimal) -> Decimal:
        exponent = 2 * (2 * alpha - 1) * w - log_root_discriminant
        correction = (Decimal(1) + exponent.exp() / C_UPPER).ln()
        return C_UPPER.ln() + log_root_discriminant + (2 - 4 * alpha) * w + correction

    left = envelope(2 * ALPHA * W0)
    right = envelope(4 * ALPHA * W0)
    assert maximum_fourth_slope < right[3]
    margins = [
        left[0] - rhs(ALPHA, W0) - EPSILON,
        right[0] - rhs(ALPHA, 2 * W0) - EPSILON,
    ]
    assert min(margins) > Decimal("0.0005")

    def endpoint_margin(alpha: Decimal, endpoint: int) -> Decimal:
        if endpoint == 1:
            return envelope(2 * alpha * W0)[0] - rhs(alpha, W0)
        assert endpoint == 2
        return envelope(4 * alpha * W0)[0] - rhs(alpha, 2 * W0)

    brackets: list[tuple[Decimal, Decimal]] = []
    for endpoint in (1, 2):
        low = Decimal("0.49369771")
        high = ALPHA
        assert endpoint_margin(low, endpoint) < 0
        assert endpoint_margin(high, endpoint) > 0
        for _ in range(120):
            middle = (low + high) / 2
            if endpoint_margin(middle, endpoint) > 0:
                high = middle
            else:
                low = middle
        brackets.append((low, high))

    def profile(stop: int) -> dict[int, int]:
        out: dict[int, int] = {}
        for _, _, _, _, depth, _ in increments[: stop + 1]:
            out[depth] = out.get(depth, 0) + 1
        return out

    print("field/class number/signatures: CERTIFIED", FIELD_DISCRIMINANT)
    print("T last / columns / constraints / d:", ramified[-1], len(columns), constraint_rank, GENERATOR_RANK)
    print("useful / rejected / last:", len(useful), len(rejected), useful[-1])
    print("base ideal useful position:", base_ideal_position)
    print("relations / log RD:", relation_bound, log_root_discriminant)
    print("left:", left[1], left[2], profile(left[1]))
    print("right:", right[1], right[2], profile(right[1]))
    print("right / max fourth slopes:", right[3], maximum_fourth_slope)
    print("margins:", *margins)
    print("fixed-anchor threshold brackets:", *brackets)
    print("hostile audit F_2(n) << n^0.49369772: CERTIFIED")


if __name__ == "__main__":
    main()
