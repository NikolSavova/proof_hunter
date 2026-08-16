#!/usr/bin/env python3
"""Exact 58-point counterexample to the finite bound H(P) <= 2."""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations

from verify_apa_counterexample import direct_profile, half_value, matrix_profile, orient


RAW_POINTS = """
0.20786693113977422 -1029821364.9292413
0.80723338990293902 1056501906.8049138
1.9317380144309935 957557259.0526675
3.6603726095350479 782641862.60070944
4 -752125782
6.0238145446618718 633014083.58513331
5.9110604548858943 -624755653.28518164
6.9909790464137638 -539801039.44185472
7.9288615597158749 -471696032.84180236
9.2999472585782499 -149903557.42009604
9.8758705056974048 -330730348.24491662
10.643086590173722 398899661.48840737
11.878849664447513 -90467155.713217139
13.132169438499004 -19162226.899327293
14.433155175784432 -218052029.76120996
15.000133740535224 -680828472.95845509
15.156765171092808 53894876.776996464
17.240203071984798 -895380136.90764284
18.446029507889129 -27954270.925117567
18.983432563983971 -8979999.6867895834
19.874463895704348 -1187480404.273417
20.533884057397085 324693437.39405537
21.766002014077674 -1438346169.8524523
22.580346770772188 452105088.07908374
23.670287987276286 -1718199481.0401797
25.199971820901187 768612957.80679619
25.97080754082463 835370297.11568248
27.935673822567523 -2303552913.9358892
28.130440609791897 991613391.95034158
29.07851344397907 1063893084.438761
15.65266114625425 -744468665.44992423
10.407665901306956 410825581.01485282
20.476594331529569 317860560.5297187
10.607187999408977 -101665850.77965665
13.583347292975398 -175825382.3559975
14.818308280637382 -72773332.163382798
3.3003889800227242 -805081368.75900149
12.88766012267104 19089620.303640533
14.782714915578216 79079976.32025212
20.366520901597429 -1269606081.1704791
11.24712439260243 -75337637.854525939
13.725087185634271 356034118.24861819
4.0980393756862732 -744541816.12624192
14.645948010709617 -60869467.071546562
4.215615766184494 -734823322.752676
14.231894708885802 -211481259.90849373
6.8233997890029192 -554549830.13626146
23.915842688677035 669613789.96524835
12.701533063210793 341858935.09356284
13.969225026178064 11943632.235589715
3.8588344289264924 -762721615.11065722
23.184816161784134 595821200.37458014
9.6049962619344527 -350284713.37686586
13.587262034350033 -161045976.78929806
6.9639819251227957 530460311.18369341
14.974692681086196 64991438.163923964
11.090416686607872 -82225159.535504043
19.307054366343873 -1112043979.9958861
"""


EXPECTED_PROFILE = (
    1, 58, 1653, 30856, 220958, 428915,
    284982, 76995, 15100, 2179, 210,
)


def points():
    return tuple(
        (Fraction(x), Fraction(y))
        for x, y in (line.split() for line in RAW_POINTS.splitlines() if line.strip())
    )


def onion_layers(pts):
    remaining = list(range(len(pts)))
    layers = []
    while remaining:
        if len(remaining) <= 2:
            hull = remaining[:]
        else:
            ordered = sorted(remaining, key=lambda label: pts[label])
            lower = []
            for label in ordered:
                while (len(lower) >= 2
                       and orient(pts[lower[-2]], pts[lower[-1]], pts[label]) <= 0):
                    lower.pop()
                lower.append(label)
            upper = []
            for label in reversed(ordered):
                while (len(upper) >= 2
                       and orient(pts[upper[-2]], pts[upper[-1]], pts[label]) <= 0):
                    upper.pop()
                upper.append(label)
            hull = lower[:-1] + upper[:-1]
        layers.append(hull)
        hull_set = set(hull)
        remaining = [label for label in remaining if label not in hull_set]
    return layers


def main() -> None:
    pts = points()
    assert len(pts) == len(set(pts)) == 58
    determinants = [
        orient(pts[i], pts[j], pts[k])
        for i, j, k in combinations(range(58), 3)
    ]
    assert all(determinants)

    profile = direct_profile(pts)
    assert profile == EXPECTED_PROFILE
    assert matrix_profile(pts) == profile
    z_one = sum(profile)
    z_half = half_value(profile)
    h_value = Fraction(58) * z_half / z_one
    assert z_one == 1_061_907
    assert z_half == Fraction(1_172_209, 32)
    assert h_value == Fraction(33_994_061, 16_990_512) > 2
    assert h_value - 2 == Fraction(13_037, 16_990_512)

    moment_one = sum(rank * value for rank, value in enumerate(profile))
    moment_half = sum(
        (Fraction(rank * value, 2**rank) for rank, value in enumerate(profile)),
        Fraction(),
    )
    apa_ratio = (
        58 * z_half + 57 * moment_half
    ) / (2 * moment_one)
    assert moment_one == 5_515_707
    assert moment_half == Fraction(85_055_449, 512)
    assert apa_ratio == Fraction(5_935_970_545, 5_648_083_968) > 1

    children = []
    for label in range(58):
        child_profile = matrix_profile(pts[:label] + pts[label + 1 :])
        child_z_one = sum(child_profile)
        child_z_half = half_value(child_profile)
        child_h = Fraction(57) * child_z_half / child_z_one
        rooted_one = z_one - child_z_one
        rooted_half = z_half - child_z_half
        # Positive is the RHS-minus-LHS margin in individual RA_e.
        ra_margin = 2 * rooted_one - z_half - 57 * rooted_half
        children.append(
            {
                "label": label,
                "H_child": str(child_h),
                "H_child_decimal": float(child_h),
                "RA_margin_RHS_minus_LHS": str(ra_margin),
            }
        )

    assert all(Fraction(row["H_child"]) < 2 for row in children)
    assert all(Fraction(row["RA_margin_RHS_minus_LHS"]) < 0 for row in children)
    layers = onion_layers(pts)
    assert list(map(len, layers)) == [4, 4, 4, 4, 4, 4, 4, 6, 6, 6, 7, 4, 1]
    assert layers[-1] == [53]
    assert children[53]["RA_margin_RHS_minus_LHS"] == "-1695735/512"

    result = {
        "description": "exact planar counterexample to finite H<=2",
        "n": 58,
        "general_position_triples_checked": len(determinants),
        "minimum_absolute_determinant": str(min(map(abs, determinants))),
        "profile": list(profile),
        "Z_1": z_one,
        "Z_half": str(z_half),
        "H": str(h_value),
        "H_minus_2": str(h_value - 2),
        "APA_ratio": str(apa_ratio),
        "number_of_children_with_H_above_2": sum(
            Fraction(row["H_child"]) > 2 for row in children
        ),
        "number_of_points_passing_individual_RA": sum(
            Fraction(row["RA_margin_RHS_minus_LHS"]) >= 0 for row in children
        ),
        "onion_layers_by_input_label": layers,
        "deepest_point_label": 53,
        "deepest_point_RA_margin_RHS_minus_LHS": children[53][
            "RA_margin_RHS_minus_LHS"
        ],
        "children": children,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
