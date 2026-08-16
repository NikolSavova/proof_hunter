#!/usr/bin/env python3
"""Exact rational certificate disproving averaged arbitrary-point deletion.

The parent profile is computed directly from upper/lower monotone path
polynomials, using only rational orientation tests.  The independent
reflection-order evaluator is used for the 44 deletion profiles.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
GATE = ROOT / "agent_reflection_gate"
sys.path.insert(0, str(GATE))

import reflection_order_gate as gate  # noqa: E402


Point = tuple[Fraction, Fraction]
Poly = list[int]


RAW_POINTS = """
0.14320035642455314 -1031206880.0893034
0.89545077882264945 1026927085.8751155
1.8113483234275096 948481581.98880708
3.3039041431658003 796969813.15924132
4 -752125782
6.0642542299164814 627430866.50034666
5.8700701769702288 -628726290.8863647
6.9909790464137638 -541173062.77930892
7.901157507751754 -444404314.92435765
9.0219429378325984 -148106107.76755571
9.8866307634354715 -327073083.00560498
10.941889213074553 388188865.47833025
11.890954601473268 -74360578.294873685
13.128237350120774 -17607227.060482875
14.49703862989163 -218967041.93043113
14.900600736176514 -675317040.38562942
15.267436341785128 105991099.90829706
17.16836502836853 -858864050.59429157
18.125343971168967 -53246105.215401754
19.282805900148944 201120600.76060829
19.872569969307445 -1178539024.4120097
20.606712704737056 332206482.68648905
21.895475405763143 -1434328633.8739703
22.467776975836646 415290761.29099441
23.744511629821471 -1705552563.4465973
25.103996299605054 765405730.54659355
25.97080754082463 838201771.56005728
27.731513657498386 -2242483066.7382002
28.114198177419993 990217544.960325
29.112677478083278 1068864743.9701707
15.666961697287258 -747616757.5860368
10.330734970584682 412871097.5776639
20.213123363363341 315105486.09019423
10.59899350162525 -102441692.52775835
13.499287706574645 -188386792.24632609
14.852216726726327 -42140237.408297792
3.3008825460887707 -804560176.80202723
12.88766012267104 18435956.009858448
14.725798603821955 -135372530.10759696
20.35222929879178 -1254927085.4940932
11.388763226835147 -67840182.372566253
13.828183282341442 439871958.14338762
4.0980393756862732 -744116751.57846057
15.079504537081824 -25150571.366406821
"""


EXPECTED_PROFILE = (1, 44, 946, 13244, 70450, 99093, 43597, 8726, 1075, 53)


def points() -> tuple[Point, ...]:
    return tuple(
        (Fraction(x), Fraction(y))
        for x, y in (line.split() for line in RAW_POINTS.splitlines() if line.strip())
    )


def orient(a: Point, b: Point, c: Point) -> Fraction:
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def add_poly(a: Poly, b: Poly) -> Poly:
    answer = [0] * max(len(a), len(b))
    for i, value in enumerate(a):
        answer[i] += value
    for i, value in enumerate(b):
        answer[i] += value
    return answer


def multiply_poly(a: Poly, b: Poly) -> Poly:
    answer = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            answer[i + j] += x * y
    return answer


def rooted_paths(pts: tuple[Point, ...], left: int, sign: int) -> dict[int, Poly]:
    """Count monotone paths from ``left``, with z per path edge."""
    n = len(pts)
    edge: dict[tuple[int, int], Poly] = {
        (left, right): [0, 1] for right in range(left + 1, n)
    }
    totals: dict[int, Poly] = {}
    for right in range(left + 1, n):
        total = [0]
        for previous in range(left, right):
            if (previous, right) in edge:
                total = add_poly(total, edge[previous, right])
        totals[right] = total

        previous = right
        for target in range(previous + 1, n):
            path = [0]
            for before in range(left, previous):
                old = edge.get((before, previous))
                if (old is not None
                        and (orient(pts[before], pts[previous], pts[target]) > 0)
                        == (sign > 0)):
                    path = add_poly(path, [0] + old)
            if any(path):
                edge[previous, target] = path
    return totals


def direct_profile(raw_points: tuple[Point, ...]) -> tuple[int, ...]:
    """Endpoint decomposition, independent of the matrix-product checker."""
    pts = tuple(sorted(raw_points))
    profile: Poly = [1, len(pts)]
    for left in range(len(pts) - 1):
        upper = rooted_paths(pts, left, +1)
        lower = rooted_paths(pts, left, -1)
        for right in range(left + 1, len(pts)):
            contribution = multiply_poly(upper[right], lower[right])
            if len(profile) < len(contribution):
                profile.extend([0] * (len(contribution) - len(profile)))
            for rank, value in enumerate(contribution):
                profile[rank] += value
    return tuple(profile)


def slope_roots(raw_points: tuple[Point, ...]) -> tuple[tuple[int, int], ...]:
    pts = tuple(sorted(raw_points))
    roots = sorted(
        (
            (pts[j][1] - pts[i][1]) / (pts[j][0] - pts[i][0]),
            i,
            j,
        )
        for i in range(len(pts))
        for j in range(i + 1, len(pts))
    )
    return tuple((i, j) for _, i, j in roots)


def matrix_profile(raw_points: tuple[Point, ...]) -> tuple[int, ...]:
    evaluation = gate.evaluate_roots(
        len(raw_points), slope_roots(raw_points), graded=True
    )
    assert evaluation.graded is not None
    return (1,) + tuple(evaluation.graded[1:])


def half_value(profile: tuple[int, ...]) -> Fraction:
    return sum(
        (Fraction(value, 2**rank) for rank, value in enumerate(profile)),
        Fraction(),
    )


def main() -> None:
    pts = points()
    assert len(pts) == len(set(pts)) == 44
    determinants = [orient(pts[i], pts[j], pts[k]) for i, j, k in combinations(range(44), 3)]
    assert all(determinants)

    profile = direct_profile(pts)
    assert profile == EXPECTED_PROFILE
    assert matrix_profile(pts) == profile

    z_one = sum(profile)
    moment_one = sum(rank * value for rank, value in enumerate(profile))
    z_half = half_value(profile)
    moment_half = sum(
        (Fraction(rank * value, 2**rank) for rank, value in enumerate(profile)),
        Fraction(),
    )
    apa_lhs = 44 * z_half + 43 * moment_half
    apa_rhs = 2 * moment_one
    assert z_one == 237_229
    assert moment_one == 1_150_674
    assert z_half == Fraction(5_206_251, 512)
    assert moment_half == Fraction(22_095_989, 512)
    assert apa_lhs == Fraction(1_179_202_571, 512)
    assert apa_rhs == 2_301_348
    assert apa_lhs - apa_rhs == Fraction(912_395, 512) > 0

    # LHS minus RHS, decomposed by rank.
    rank_contributions = tuple(
        value * (Fraction(44 + 43 * rank, 2**rank) - 2 * rank)
        for rank, value in enumerate(profile)
    )
    assert sum(rank_contributions) == apa_lhs - apa_rhs

    # For point e, positive margin means that the individual arbitrary-point
    # rooted inequality still holds.  The negative sum is exactly RHS-LHS of
    # APA, as it must be.
    deletion_rows = []
    margins = []
    for label in range(44):
        child = matrix_profile(pts[:label] + pts[label + 1 :])
        rooted_count = z_one - sum(child)
        rooted_half = z_half - half_value(child)
        margin = 2 * rooted_count - z_half - 43 * rooted_half
        margins.append(margin)
        deletion_rows.append(
            {
                "label": label,
                "coordinate": [str(pts[label][0]), str(pts[label][1])],
                "RA_margin_RHS_minus_LHS": str(margin),
                "rooted_count_at_one": rooted_count,
                "rooted_half_mass": str(rooted_half),
            }
        )
    assert sum(margins) == apa_rhs - apa_lhs
    assert sum(margin > 0 for margin in margins) == 21
    assert sum(margin < 0 for margin in margins) == 23
    assert min(enumerate(margins), key=lambda item: item[1]) == (
        1, Fraction(-1_449_197, 512)
    )

    result = {
        "description": "exact stretchable counterexample to APA",
        "n": 44,
        "general_position_triples_checked": len(determinants),
        "minimum_absolute_determinant": str(min(map(abs, determinants))),
        "profile": list(profile),
        "Z_1": z_one,
        "moment_1": moment_one,
        "Z_half": str(z_half),
        "moment_half": str(moment_half),
        "H": str(Fraction(44) * z_half / z_one),
        "APA_LHS": str(apa_lhs),
        "APA_RHS": str(apa_rhs),
        "APA_ratio": str(apa_lhs / apa_rhs),
        "APA_violation_LHS_minus_RHS": str(apa_lhs - apa_rhs),
        "rank_contributions_LHS_minus_RHS": [str(value) for value in rank_contributions],
        "individual_RA_pass_count": sum(margin > 0 for margin in margins),
        "individual_RA_fail_count": sum(margin < 0 for margin in margins),
        "deletions": deletion_rows,
    }
    print(json.dumps(result, indent=2))
    print("APA rational counterexample: PASS", file=sys.stderr)


if __name__ == "__main__":
    main()
